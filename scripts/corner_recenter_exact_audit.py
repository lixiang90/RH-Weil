"""Exact rational checks for the corner recentering input to note 425.

All vectors are finite atoms plus one normalized geometric tail.  Inner
products evaluate the infinite tail by its closed geometric sum, never by
floating point or a truncated tail.  The two rational models are not actual
prime parameters.  Finite-grid checks do not replace the general proofs of
orthogonality, infinite strong limits, operator domains, or arithmetic bridges.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ZERO = F(0)
ONE = F(1)


@dataclass(frozen=True)
class Vector:
    rho: F
    root: F
    atoms: tuple[tuple[int, F], ...] = ()
    tail_start: int | None = None
    tail_scale: F = ZERO

    def atom_dict(self):
        return dict(self.atoms)

    def tail_at(self, index):
        if self.tail_start is None or index < self.tail_start:
            return ZERO
        return self.tail_scale * self.root * self.rho ** (index-self.tail_start)

    def at(self, index):
        return self.atom_dict().get(index, ZERO) + self.tail_at(index)

    def shifted(self, amount):
        return Vector(self.rho, self.root,
                      tuple((j+amount, a) for j, a in self.atoms),
                      None if self.tail_start is None else self.tail_start+amount,
                      self.tail_scale)

    def scaled(self, scalar):
        scalar = F(scalar)
        return Vector(self.rho, self.root,
                      tuple((j, scalar*a) for j, a in self.atoms if scalar*a),
                      self.tail_start if scalar*self.tail_scale else None,
                      scalar*self.tail_scale)

    def plus(self, other):
        assert (self.rho, self.root) == (other.rho, other.root)
        starts = [v.tail_start for v in (self, other) if v.tail_start is not None]
        anchor = max(starts) if starts else None
        atoms = {}
        tail_scale = ZERO
        for vector in (self, other):
            for j, a in vector.atoms:
                atoms[j] = atoms.get(j, ZERO) + a
            if vector.tail_start is not None:
                for j in range(vector.tail_start, anchor):
                    atoms[j] = atoms.get(j, ZERO) + vector.tail_at(j)
                tail_scale += vector.tail_scale * vector.rho ** (anchor-vector.tail_start)
        return Vector(self.rho, self.root,
                      tuple(sorted((j, a) for j, a in atoms.items() if a)),
                      anchor if tail_scale else None, tail_scale)


def atom(rho, root, index):
    return Vector(rho, root, ((index, ONE),))


def ball(rho, root, start):
    return Vector(rho, root, (), start, ONE)


def wave(rho, root, start):
    # w_N = rho e_N - sqrt(1-rho^2) b_{N+1}.
    return atom(rho, root, start).scaled(rho).plus(
        ball(rho, root, start+1).scaled(-root))


def positive_tail_projection(vector):
    """Physical H=1_(j>=0), kept as an exact atom-plus-tail vector."""
    atoms = tuple((j, a) for j, a in vector.atoms if j >= 0)
    if vector.tail_start is None:
        return Vector(vector.rho, vector.root, atoms)
    anchor = max(0, vector.tail_start)
    scale = vector.tail_scale * vector.rho ** (anchor-vector.tail_start)
    return Vector(vector.rho, vector.root, atoms, anchor, scale)


def inner(left, right):
    assert (left.rho, left.root) == (right.rho, right.root)
    la, ra = left.atom_dict(), right.atom_dict()
    result = sum((a*ra.get(j, ZERO) for j, a in la.items()), ZERO)
    result += sum((a*right.tail_at(j) for j, a in la.items()), ZERO)
    result += sum((a*left.tail_at(j) for j, a in ra.items()), ZERO)
    if left.tail_start is not None and right.tail_start is not None:
        result += (left.tail_scale * right.tail_scale * left.root**2
                   * left.rho**abs(left.tail_start-right.tail_start)
                   / (ONE-left.rho**2))
    return result


def projector_basis(rho, root, n):
    return [atom(rho, root, j) for j in range(-n, n)] + [ball(rho, root, n)]


def negative_basis(rho, root, k):
    return [atom(rho, root, j) for j in range(-k, 0)] + [ball(rho, root, 0)]


def shell_basis(rho, root, n):
    return [atom(rho, root, -n-1), wave(rho, root, n)]


def trace_shift(basis, amount):
    return sum((inner(v, v.shifted(amount)) for v in basis), ZERO)


def zeros(rows, cols):
    return [[ZERO for _ in range(cols)] for _ in range(rows)]


def multiply(left, right):
    assert len(left[0]) == len(right)
    return [[sum((left[i][k]*right[k][j] for k in range(len(right))), ZERO)
             for j in range(len(right[0]))] for i in range(len(left))]


def subtract(left, right):
    return [[a-b for a, b in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def add(left, right):
    return [[a+b for a, b in zip(lrow, rrow)] for lrow, rrow in zip(left, right)]


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def common_coordinate_data(vectors):
    """A finite orthonormal basis containing every supplied infinite vector."""
    anchors = [v.tail_start for v in vectors if v.tail_start is not None]
    atoms = [j for v in vectors for j, _ in v.atoms]
    anchor = max(anchors + [j+1 for j in atoms] + [0])
    lower = min(anchors + atoms + [anchor])
    return lower, anchor


def coordinates(vector, lower, anchor):
    result = [vector.at(j) for j in range(lower, anchor)]
    tail = ZERO if vector.tail_start is None else (
        vector.tail_scale * vector.rho ** (anchor-vector.tail_start))
    result.append(tail)
    return result


def projector_matrix(basis, lower, anchor):
    size = anchor-lower+1
    result = zeros(size, size)
    for vector in basis:
        v = coordinates(vector, lower, anchor)
        for i in range(size):
            for j in range(size):
                result[i][j] += v[i]*v[j]
    return result


def tensor_inner(left, right):
    return inner(left[0], right[0])*inner(left[1], right[1])


def tensor_basis(left, right):
    return [(v, w) for v in left for w in right]


def tensor_trace_shift(basis, a, b):
    return sum((inner(v, v.shifted(a))*inner(w, w.shifted(b))
                for v, w in basis), ZERO)


def cross_trace(left, right, a, b):
    """Tr(P_left lambda_(a,b) P_right) from finite rank-one products."""
    return sum((inner(v[0], w[0].shifted(a))*inner(v[1], w[1].shifted(b))
                * tensor_inner(w, v) for v in left for w in right), ZERO)


def reduced_rank(matrix):
    data = [row[:] for row in matrix]
    row = 0
    for col in range(len(data[0])):
        pivot = next((i for i in range(row, len(data)) if data[i][col]), None)
        if pivot is None:
            continue
        data[row], data[pivot] = data[pivot], data[row]
        factor = data[row][col]
        data[row] = [x/factor for x in data[row]]
        for i in range(len(data)):
            if i != row and data[i][col]:
                factor = data[i][col]
                data[i] = [x-factor*y for x, y in zip(data[i], data[row])]
        row += 1
        if row == len(data):
            break
    return row


def four_component(a, b):
    return [[ONE, F(-a), F(-b), F(a*b)],
            [ZERO, ONE, ZERO, F(-b)],
            [ZERO, ZERO, ONE, F(-a)],
            [ZERO, ZERO, ZERO, ONE]]


def audit():
    counts = {}

    def check(name, condition, detail=None):
        if not condition:
            raise AssertionError((name, detail))
        counts[name] = counts.get(name, 0)+1

    models = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))]
    shifts = range(-5, 6)
    for rho, root in models:
        check('rational_tail_normalization', rho**2+root**2 == ONE)
        for n in range(5):
            b = ball(rho, root, n)
            w = wave(rho, root, n)
            check('ball_norm', inner(b, b) == ONE, (rho, n))
            check('wave_norm', inner(w, w) == ONE, (rho, n))
            check('ball_wave_orthogonality', inner(b, w) == ZERO, (rho, n))
            recursion = atom(rho, root, n).scaled(root).plus(
                ball(rho, root, n+1).scaled(rho))
            lower, anchor = common_coordinate_data([b, recursion])
            check('ball_exact_recursion', coordinates(b, lower, anchor)
                  == coordinates(recursion, lower, anchor), (rho, n))
            for a in shifts:
                check('ball_shifted_trace', inner(b, b.shifted(a)) == rho**abs(a),
                      (rho, n, a))
                check('wave_shifted_trace', inner(w, w.shifted(a)) == F(a == 0),
                      (rho, n, a))
                check('R_N_shifted_trace', trace_shift(projector_basis(rho, root, n), a)
                      == F(2*n*(a == 0))+rho**abs(a), (rho, n, a))
                check('S_N_shifted_trace', trace_shift(shell_basis(rho, root, n), a)
                      == F(2*(a == 0)), (rho, n, a))
            for a in range(-4, 5):
                for bshift in range(-4, 5):
                    check('wave_translates_orthogonal', inner(w.shifted(a), w.shifted(bshift))
                          == F(a == bshift), (rho, n, a, bshift))

            rn, rn_next = projector_basis(rho, root, n), projector_basis(rho, root, n+1)
            shell = shell_basis(rho, root, n)
            lower, anchor = common_coordinate_data(rn+rn_next+shell)
            pm, next_pm, sm = [projector_matrix(v, lower, anchor) for v in (rn, rn_next, shell)]
            check('R_N_projection_matrix', multiply(pm, pm) == pm, (rho, n))
            check('S_N_projection_matrix', multiply(sm, sm) == sm, (rho, n))
            check('R_increment_exact_matrix', subtract(next_pm, pm) == sm, (rho, n))
            check('R_shell_product_zero_matrix', multiply(pm, sm) == zeros(len(pm), len(pm)),
                  (rho, n))

            shifted_r = [v.shifted(-n) for v in rn]
            negative_r = negative_basis(rho, root, 2*n)
            lower, anchor = common_coordinate_data(shifted_r+negative_r)
            check('R_recenter_exact_matrix', projector_matrix(shifted_r, lower, anchor)
                  == projector_matrix(negative_r, lower, anchor), (rho, n))
            shifted_shell = [v.shifted(-n) for v in shell]
            expected_shell = [atom(rho, root, -2*n-1), wave(rho, root, 0)]
            lower, anchor = common_coordinate_data(shifted_shell+expected_shell)
            check('S_recenter_exact_matrix', projector_matrix(shifted_shell, lower, anchor)
                  == projector_matrix(expected_shell, lower, anchor), (rho, n))
            check('wave_recenter_exact_coordinates',
                  coordinates(w.shifted(-n), lower, anchor)
                  == coordinates(wave(rho, root, 0), lower, anchor), (rho, n))
        for k in range(7):
            physical = negative_basis(rho, root, k)
            finite_w = [wave(rho, root, n) for n in range(-k, 0)]
            escaped_ball = ball(rho, root, -k)
            all_vectors = physical+finite_w+[escaped_ball]
            lower, anchor = common_coordinate_data(all_vectors)
            physical_pm = projector_matrix(physical, lower, anchor)
            w_pm = projector_matrix(finite_w, lower, anchor)
            ball_pm = projector_matrix([escaped_ball], lower, anchor)
            check('R_minus_exact_wavelet_plus_escaped_ball_matrix',
                  physical_pm == add(w_pm, ball_pm), (rho, k))
            check('escaped_ball_orthogonal_to_finite_wavelet_block',
                  all(inner(escaped_ball, w) == ZERO for w in finite_w), (rho, k))
            if k:
                projected_wave = positive_tail_projection(wave(rho, root, -k))
                expected = ball(rho, root, 0).scaled(-root*rho**(k-1))
                hlo, han = common_coordinate_data([projected_wave, expected])
                check('H_negative_wave_exact_ball_tail',
                      coordinates(projected_wave, hlo, han)
                      == coordinates(expected, hlo, han), (rho, k))
                hull_vectors = finite_w+[positive_tail_projection(w) for w in finite_w]
                hlo, han = common_coordinate_data(hull_vectors+physical)
                hull_coordinates = [coordinates(w, hlo, han) for w in hull_vectors]
                check('minimal_H_reducing_hull_rank', reduced_rank(hull_coordinates) == k+1,
                      (rho, k))
                hull_target = projector_matrix(physical, hlo, han)
                check('minimal_H_reducing_hull_inside_physical_R_minus',
                      all(multiply(hull_target, [[x] for x in row]) == [[x] for x in row]
                          for row in hull_coordinates), (rho, k))
                # H on this common finite basis is diagonal, with nonnegative
                # atoms and the final tail retained.  This verifies reducing,
                # not merely containment of the sampled vectors.
                hdiag = [F(j >= 0) for j in range(hlo, han)]+[ONE]
                hm = [[hdiag[i] if i == j else ZERO for j in range(len(hdiag))]
                      for i in range(len(hdiag))]
                check('physical_R_minus_reduces_H_matrix',
                      multiply(hm, hull_target) == multiply(hull_target, hm), (rho, k))
            for a in shifts:
                check('R_minus_K_shifted_trace', trace_shift(negative_basis(rho, root, k), a)
                      == F(k*(a == 0))+rho**abs(a), (rho, k, a))
                check('finite_negative_wavelet_block_shifted_trace',
                      trace_shift(finite_w, a) == F(k*(a == 0)), (rho, k, a))
                check('escaped_ball_shifted_trace', inner(escaped_ball, escaped_ball.shifted(a))
                      == rho**abs(a), (rho, k, a))
                check('physical_minus_wavelet_trace_is_escaped_ball_trace',
                      trace_shift(physical, a)-trace_shift(finite_w, a) == rho**abs(a),
                      (rho, k, a))

    (rp, sp), (rq, sq) = models
    wp, wq = wave(rp, sp, 0), wave(rq, sq, 0)
    labels = [(a, b) for a in range(-4, 5) for b in range(-4, 5)]
    for np in range(4):
        for nq in range(4):
            r_p, r_q = projector_basis(rp, sp, np), projector_basis(rq, sq, nq)
            s_p, s_q = shell_basis(rp, sp, np), shell_basis(rq, sq, nq)
            old_p, old_q = tensor_basis(r_p, s_q), tensor_basis(s_p, r_q)
            rm_p, rm_q = negative_basis(rp, sp, 2*np), negative_basis(rq, sq, 2*nq)
            positive_p, positive_q = tensor_basis(rm_p, [wq]), tensor_basis([wp], rm_q)
            negative_p = tensor_basis(rm_p, [atom(rq, sq, -2*nq-1)])
            negative_q = tensor_basis([atom(rp, sp, -2*np-1)], rm_q)
            all_recentered = positive_p+positive_q+negative_p+negative_q
            for i, v in enumerate(all_recentered):
                for j, w in enumerate(all_recentered):
                    check('recenter_four_channels_orthogonal_projection_gram',
                          tensor_inner(v, w) == F(i == j), (np, nq, i, j))
            for a, b in labels:
                op, oq = tensor_trace_shift(old_p, a, b), tensor_trace_shift(old_q, a, b)
                pp, pq = tensor_trace_shift(positive_p, a, b), tensor_trace_shift(positive_q, a, b)
                check('original_half_trace_equals_positive_corner_trace', (op+oq)/2 == pp+pq,
                      (np, nq, a, b))
                check('each_original_shell_half_equals_positive_channel', op/2 == pp and oq/2 == pq,
                      (np, nq, a, b))
                check('negative_channel_trace_equals_positive_channel',
                      tensor_trace_shift(negative_p, a, b) == pp
                      and tensor_trace_shift(negative_q, a, b) == pq, (np, nq, a, b))
                rec_p = tensor_basis([v.shifted(-np) for v in r_p],
                                     [v.shifted(-nq) for v in s_q])
                rec_q = tensor_basis([v.shifted(-np) for v in s_p],
                                     [v.shifted(-nq) for v in r_q])
                check('full_recenter_shifted_trace', tensor_trace_shift(rec_p, a, b) == op
                      and tensor_trace_shift(rec_q, a, b) == oq, (np, nq, a, b))
                if a and b:
                    check('mixed_group_trace_zero', op == oq == pp == pq == ZERO,
                          (np, nq, a, b))
                check('original_mixed_channel_cross_trace_zero',
                      cross_trace(old_p, old_q, a, b) == ZERO
                      and cross_trace(old_q, old_p, a, b) == ZERO, (np, nq, a, b))
                check('positive_mixed_channel_cross_trace_zero',
                      cross_trace(positive_p, positive_q, a, b) == ZERO
                      and cross_trace(positive_q, positive_p, a, b) == ZERO, (np, nq, a, b))
            check('zero_label_positive_rank', tensor_trace_shift(positive_p+positive_q, 0, 0)
                  == F(2*(np+nq+1)), (np, nq))

    group_labels = [(a, b) for a in range(-2, 3) for b in range(-2, 3)]
    eye = identity(4)
    for a, b in group_labels:
        check('four_component_inverse', multiply(four_component(a, b), four_component(-a, -b)) == eye,
              (a, b))
        for u, v in group_labels:
            check('four_component_group_law', multiply(four_component(a, b), four_component(u, v))
                  == four_component(a+u, b+v), (a, b, u, v))
    n1, n2 = subtract(four_component(1, 0), eye), subtract(four_component(0, 1), eye)
    check('four_component_nilpotents', multiply(n1, n1) == multiply(n2, n2) == zeros(4, 4))
    check('four_component_commuting_nilpotents', multiply(n1, n2) == multiply(n2, n1))
    # Stack (S_i-1)^T equations for the invariant dual row.
    invariant_constraints = [[m[j][i] for j in range(4)] for m in (n1, n2) for i in range(4)]
    check('invariant_functionals_only_corner', reduced_rank(invariant_constraints) == 3
          and all(row[3] == ZERO for row in invariant_constraints))
    augmented = [row+[ZERO] for row in invariant_constraints] + [[ONE, ZERO, ZERO, ZERO, ONE]]
    coefficient = [row[:-1] for row in augmented]
    check('invariant_trace_normalization_inconsistent', reduced_rank(coefficient) == 3
          and reduced_rank(augmented) == 4)
    images = [[n1[i][j] for i in range(4)] for j in range(4)]
    images += [[n2[i][j] for i in range(4)] for j in range(4)]
    check('coinvariant_only_corner', reduced_rank(images) == 3
          and all(row[3] == ZERO for row in images))

    return {
        'status': 'passed_exact_fraction_checks',
        'arithmetic': 'fractions.Fraction; closed infinite geometric inner products; no float or tail truncation',
        'models': [{'rho': str(rho), 'sqrt_one_minus_rho_squared': str(root)} for rho, root in models],
        'ranges': {'N': [0, 4], 'R_minus_K': [0, 6], 'one_dimensional_shift': [-5, 5],
                   'wave_translate': [-4, 4], 'two_channel_Np_Nq': [0, 3],
                   'two_channel_group_labels': [-4, 4], 'four_component_group_labels': [-2, 2],
                   'escaped_ball_K': [0, 6], 'minimal_H_reducing_hull_K': [1, 6]},
        'checks': counts,
        'total_exact_assertions': sum(counts.values()),
        'definitions': {
            'b_N': 'sqrt(1-rho^2) rho^(j-N) for j>=N',
            'w_N': 'rho e_N - sqrt(1-rho^2) b_(N+1)',
            'R_N': 'sum_{-N<=j<N} P_ej + P_bN',
            'R_minus_K': 'sum_{-K<=j<0} P_ej + P_b0',
            'S_N': 'P_e_(-N-1) + P_wN',
            'wavelet_cutoff_split': 'R_minus_K = sum_{-K<=n<0} P_wn + P_b_(-K)',
            'H_negative_wave': 'H w_(-n) = -sqrt(1-rho^2) rho^(n-1) b0, n>=1',
            'minimal_H_reducing_hull': 'span(F_K + H F_K) = range(R_minus_K), K>=1',
            'positive_corner_channels': 'R_minus_(2Np,p) tensor P_w0q and P_w0p tensor R_minus_(2Nq,q)',
            'recenter': 'conjugation by lambda_(-Np) tensor lambda_(-Nq)',
        },
        'scope': ('Finite exact rational surrogate models and closed geometric-tail formulas. '
                  'No actual-prime floating-point certification, time factors, infinite strong-limit '
                  'or trace-domain certification, cyclic arithmetic comparison, positivity theorem or RH certificate.'),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=ROOT/'reviews/2026-10-04/f1-corner-recenter-exact-audit.json')
    args = parser.parse_args()
    result = audit()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'assertions': result['total_exact_assertions'],
                      'output': str(args.output)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
