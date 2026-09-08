"""Floating candidate: add four explicit truncated, stopped costs."""

import numpy as np

from radius_five_continuation_plan_search import Plans


class StoppedPlans(Plans):
    def value(self, states, exact=False):
        states = np.atleast_2d(states)
        best, choice = super().value(states, exact=exact)
        kernel = self.kernel if exact else self.fast
        internal = np.zeros(len(states))
        for m in range(1, 5):
            internal += (self.eta*states[:, m-1]/(2*np.pi)-self.alpha-self.margin
                         +2*np.sum(kernel(np.cumsum(states[:, m-1:], axis=1))**2, axis=1))
            improved = internal < best
            best[improved] = internal[improved]
            choice[improved] = len(self.items)+m-1
        return best, choice

    def extend(self, transition, tail_id):
        raise NotImplementedError("Stopped branches need their own exact update rule")
