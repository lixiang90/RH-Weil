"""Floating search model: four-anchor costs with partial future words.

Each extra branch is I_4(s) + cross energies to a future word of length
0..4 + b. The four stopped costs I_1,...,I_4 and zero are always included.
"""

import numpy as np
from scipy.interpolate import CubicSpline


class PartialPlans:
    def __init__(self, kernel, alpha, eta, margin):
        self.kernel, self.alpha, self.eta, self.margin = kernel, alpha, eta, margin
        x = np.linspace(0., 640., 320001)
        self.fast = CubicSpline(x, kernel(x), extrapolate=False)
        self.items, self.by_key, self.groups = [], {}, None

    def add(self, gaps, offset):
        assert len(gaps) <= 4
        key = (tuple(map(float, gaps)), float(offset))
        # For nonnegative offset the stopped I_4 branch dominates this branch.
        if offset >= 0:
            return -5
        if key not in self.by_key:
            self.by_key[key] = len(self.items)
            self.items.append(dict(gaps=list(key[0]), offset=key[1]))
            self.groups = None
        return self.by_key[key]

    def build(self):
        self.groups = {}
        for length in range(5):
            ids = np.array([i for i, p in enumerate(self.items) if len(p["gaps"]) == length], dtype=int)
            if len(ids):
                paths = np.array([self.items[i]["gaps"] for i in ids])
                offsets = np.array([self.items[i]["offset"] for i in ids])
                prefix = np.cumsum(paths, axis=1)
                unique = [np.unique(prefix[:, j], return_inverse=True) for j in range(length)]
                self.groups[length] = ids, offsets, unique

    def value(self, states, exact=False):
        if self.groups is None:
            self.build()
        states = np.atleast_2d(states)
        kernel = self.kernel if exact else self.fast
        all_best, all_ids = [], []
        for low in range(0, len(states), 64):
            s = states[low:low+64]
            suffix = np.flip(np.cumsum(np.flip(s, axis=1), axis=1), axis=1)
            best, choice, internal = np.zeros(len(s)), np.full(len(s), -1, dtype=int), np.zeros(len(s))
            for m in range(1, 5):
                internal += (self.eta*s[:, m-1]/(2*np.pi)-self.alpha-self.margin
                             +2*np.sum(kernel(np.cumsum(s[:, m-1:], axis=1))**2, axis=1))
                improved = internal < best
                best[improved], choice[improved] = internal[improved], -1-m
            for length, (ids, offsets, unique) in self.groups.items():
                values = internal[:, None]+offsets[None, :]
                for j in range(length):
                    prefixes, inverse = unique[j]
                    for i in range(j, 4):
                        values += 2*kernel(suffix[:, i, None]+prefixes[None, :])[:, inverse]**2
                which = np.argmin(values, axis=1)
                candidate = values[np.arange(len(s)), which]
                improved = candidate < best
                best[improved], choice[improved] = candidate[improved], ids[which[improved]]
            all_best.extend(best.tolist())
            all_ids.extend(choice.tolist())
        return np.array(all_best), np.array(all_ids)

    def cost(self, words, exact=False):
        """Short costs sum existing prefixes; unspecified terms are not defined."""
        words = np.atleast_2d(words)
        kernel = self.kernel if exact else self.fast
        return (2*np.sum(kernel(np.cumsum(words, axis=1))**2, axis=1)
                +self.eta*words[:, 0]/(2*np.pi)-self.alpha)

    def residual(self, words, exact=False):
        words = np.atleast_2d(words)
        return self.cost(words, exact)+self.value(words[:, 1:], exact)[0]-self.value(words[:, :4], exact)[0]

    def extend(self, transition, tail_id):
        if tail_id == -5:
            previous = dict(gaps=[], offset=0.)
        else:
            assert tail_id >= 0, "Stopped depths 0..3 already give R>=delta exactly"
            previous = self.items[int(tail_id)]
        future = [float(transition[-1])]+previous["gaps"]
        offset = previous["offset"]+float(self.cost(np.array(future)[None, :], exact=True)[0])-self.margin
        return self.add(future[:4], offset)
