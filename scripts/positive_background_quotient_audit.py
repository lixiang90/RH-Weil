#!/usr/bin/env python3
"""[E] Finite synthetic positive-background quotient audit, MP80 versus MP120.

Use eta=1/sqrt(2*A) on [-A,A] and the RAW-frequency convention
f_z(u)=eta(u)*exp(-i*z*u), not exp(-2*pi*i*z*u).
The analytic Gram kernel is sinc(A*(z-conj(w))).  Real nodes are distinct.
For each nonreal pair z,conj(z), g=(f_z+f_conj(z))/2 and
h=(f_z-f_conj(z))/(2*i) belong to the real-type Hilbert space.

We independently keep:
  - distance of h to the real-node span, and its Lagrange approximant;
  - the Schur residual after adding ALL positive g directions;
  - the whole finite operator Aop=sum f*f + 2*sum(g*g-h*h).
The original Aop is NOT its compression to the positive-span orthogonal
complement.  Congruence and MP eigenvalues check full inertia separately.

Four one-pair cases use n=2,4,6,8 real nodes in [-1,1], z=.2+.25i.
A two-pair case also uses z=.55+.35i and n=4.  All pairs have unit integer
multiplicity; trace Aop=n+2*k.  No actual zeros, large-height statement,
asymptotic, interval certification, or arithmetic frame estimate is tested.
The program writes no files.  All finite observations have status [E].
"""

from __future__ import annotations

import json
import time

import mpmath as mp


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def sinc(value):
    return mp.mpf(1) if value == 0 else mp.sin(value) / value


def vector_specs(nodes, pairs):
    real = [[(node, mp.mpf(1))] for node in nodes]
    positive, negative = [], []
    for z in pairs:
        positive.append([(z, mp.mpf("0.5")), (mp.conj(z), mp.mpf("0.5"))])
        negative.append([(z, -mp.j / 2), (mp.conj(z), mp.j / 2)])
    return real + positive + negative


def gram_matrix(specifications, width, tolerance):
    dimension = len(specifications)
    gram = mp.matrix(dimension)
    maximum_imaginary = mp.mpf(0)
    for i in range(dimension):
        for j in range(i, dimension):
            value = sum(
                coefficient * mp.conj(other_coefficient) * sinc(width * (z - mp.conj(w)))
                for z, coefficient in specifications[i]
                for w, other_coefficient in specifications[j]
            )
            maximum_imaginary = max(maximum_imaginary, abs(mp.im(value)))
            require(abs(mp.im(value)) <= tolerance, "real-type inner product")
            gram[i, j] = gram[j, i] = mp.re(value)
    return gram, maximum_imaginary


def principal(matrix, indices):
    return mp.matrix([[matrix[i, j] for j in indices] for i in indices])


def schur_residual(gram, positive_indices, target_indices):
    positive = principal(gram, positive_indices)
    cross = mp.matrix([[gram[i, j] for j in target_indices] for i in positive_indices])
    targets = principal(gram, target_indices)
    solution = mp.matrix(len(positive_indices), len(target_indices))
    for column in range(len(target_indices)):
        solved = mp.lu_solve(positive, cross[:, column])
        for row in range(len(positive_indices)):
            solution[row, column] = solved[row]
    residual = targets - cross.T * solution
    # Force symmetry only after recording no independent entry information is
    # lost: the exact Gram/Schur expression is real symmetric.
    return (residual + residual.T) / 2


def lagrange_coefficients(nodes, z):
    coefficients = []
    for j, node in enumerate(nodes):
        value = mp.mpc(1)
        for k, other in enumerate(nodes):
            if j != k:
                value *= (z - other) / (node - other)
        coefficients.append(mp.im(value))
    return mp.matrix(coefficients)


def one_precision(n, pair_inputs, precision):
    with mp.workdps(precision):
        tolerance = mp.mpf(10) ** (-(precision - 20))
        width = mp.mpf(1)
        nodes = [-1 + mp.mpf(2) * j / (n - 1) for j in range(n)]
        pairs = [mp.mpc(real, imaginary) for real, imaginary in pair_inputs]
        k = len(pairs)
        require(len(set(nodes)) == n, "distinct real interpolation nodes")
        specifications = vector_specs(nodes, pairs)
        gram, imaginary_error = gram_matrix(specifications, width, tolerance)
        cholesky = mp.cholesky(gram)
        require(all(cholesky[j, j] > 0 for j in range(n + 2 * k)), "full Gram has full rank")
        positive_indices = list(range(n + k))
        negative_indices = list(range(n + k, n + 2 * k))
        residual = schur_residual(gram, positive_indices, negative_indices)
        real_only_residual = schur_residual(gram, list(range(n)), negative_indices)
        residual_eigenvalues = list(mp.eigsy(residual, eigvals_only=True))
        require(all(value > 0 for value in residual_eigenvalues), "strictly positive quotient residual / rank k")

        interpolation_errors, bounds_squared = [], []
        real_gram = principal(gram, list(range(n)))
        for j, z in enumerate(pairs):
            target = negative_indices[j]
            coefficients = lagrange_coefficients(nodes, z)
            cross = mp.matrix([gram[i, target] for i in range(n)])
            error_squared = gram[target, target] - 2 * (coefficients.T * cross)[0]
            error_squared += (coefficients.T * real_gram * coefficients)[0]
            bound = mp.exp(width * abs(mp.im(z))) * width**n / mp.factorial(n)
            bound *= mp.fprod(abs(z - node) for node in nodes)
            require(error_squared > 0, "Lagrange approximant residual is positive")
            require(residual[j, j] <= real_only_residual[j, j] + tolerance, "adding positive g directions contracts residual")
            require(real_only_residual[j, j] <= error_squared + tolerance, "orthogonal projection beats Lagrange approximant")
            require(error_squared <= bound**2 + tolerance, "explicit n-th divided-difference interpolation bound")
            interpolation_errors.append(error_squared)
            bounds_squared.append(bound**2)
            # Independent exact scalar point checks, with a pointwise bound.
            complex_coefficients = []
            for index, node in enumerate(nodes):
                complex_coefficients.append(mp.fprod(
                    (z - other) / (node - other)
                    for other_index, other in enumerate(nodes) if other_index != index
                ))
            for u in (-width, -width / 2, mp.mpf(0), width / 2, width):
                scalar_h = (mp.exp(-mp.j * z * u) - mp.exp(-mp.j * mp.conj(z) * u)) / (2 * mp.j)
                approximant = sum(mp.im(coefficient) * mp.exp(-mp.j * node * u)
                                  for coefficient, node in zip(complex_coefficients, nodes))
                point_bound = mp.exp(abs(mp.im(z) * u)) * abs(u)**n / mp.factorial(n)
                point_bound *= mp.fprod(abs(z - node) for node in nodes)
                require(abs(scalar_h - approximant) <= point_bound + tolerance, "pointwise real-coefficient Lagrange remainder")

        # In an orthonormal basis B*L^{-T}, B denoting the vector synthesis,
        # the whole self-adjoint matrix is L^T*D*L, NOT the Schur residual.
        diagonal = mp.diag([1] * n + [2] * k + [-2] * k)
        whole_operator = cholesky.T * diagonal * cholesky
        whole_eigenvalues = list(mp.eigsy(whole_operator, eigvals_only=True))
        positive_count = sum(value > 0 for value in whole_eigenvalues)
        negative_count = sum(value < 0 for value in whole_eigenvalues)
        require((positive_count, negative_count) == (n + k, k), "full operator inertia by Gram congruence")
        trace = sum(whole_operator[j, j] for j in range(n + 2 * k))
        trace_error = abs(trace - (n + 2 * k))
        require(trace_error <= tolerance * (n + 2 * k), "whole operator trace equals total multiplicity")
        whole_negative_trace = -sum(value for value in whole_eigenvalues if value < 0)
        compressed_negative_trace = 2 * sum(residual[j, j] for j in range(k))
        interpolation_trace_bound = 2 * sum(bounds_squared)
        require(compressed_negative_trace <= interpolation_trace_bound + tolerance, "compressed negative-trace upper bound")
        require(compressed_negative_trace <= whole_negative_trace + tolerance, "compression is not the whole negative trace")

        def strings(values):
            return [mp.nstr(value, precision) for value in values]

        return {
            "n_real_nodes": n, "nonreal_pairs": k, "precision": precision,
            "positive_inertia": positive_count, "negative_inertia": negative_count,
            "quotient_rank": k,
            "residual_diagonal": strings([residual[j, j] for j in range(k)]),
            "real_only_residual_diagonal": strings([real_only_residual[j, j] for j in range(k)]),
            "quotient_eigenvalues": strings(residual_eigenvalues),
            "whole_eigenvalues": strings(whole_eigenvalues),
            "interpolation_errors_squared": strings(interpolation_errors),
            "interpolation_bounds_squared": strings(bounds_squared),
            "whole_negative_trace": mp.nstr(whole_negative_trace, precision),
            "compressed_negative_trace": mp.nstr(compressed_negative_trace, precision),
            "compressed_trace_upper_bound": mp.nstr(interpolation_trace_bound, precision),
            "trace_error": mp.nstr(trace_error, precision),
            "maximum_imaginary_Gram_error": mp.nstr(imaginary_error, precision),
        }


def main():
    started = time.perf_counter()
    mp.mp.dps = 120
    cases = [(n, [("0.2", "0.25")]) for n in (2, 4, 6, 8)]
    cases.append((4, [("0.2", "0.25"), ("0.55", "0.35")]))
    maximum_relative_precision_difference = mp.mpf(0)
    for n, pairs in cases:
        coarse = one_precision(n, pairs, 80)
        fine = one_precision(n, pairs, 120)
        stability = mp.mpf(0)
        for name in ("residual_diagonal", "real_only_residual_diagonal", "quotient_eigenvalues",
                     "whole_eigenvalues", "interpolation_errors_squared"):
            for lower_precision, higher_precision in zip(coarse[name], fine[name]):
                low, high = mp.mpf(lower_precision), mp.mpf(higher_precision)
                require(high != 0, "no exact-zero surrogate in precision comparison")
                stability = max(stability, abs(low - high) / abs(high))
        require(stability < mp.mpf("1e-30"), "80/120-digit agreement resolves nonzero residuals and eigenvalues")
        maximum_relative_precision_difference = max(maximum_relative_precision_difference, stability)
        print(json.dumps({
            "status": "[E] PASS", "n_real_nodes": n, "nonreal_pairs": len(pairs),
            "whole_inertia_positive_negative": [fine["positive_inertia"], fine["negative_inertia"]],
            "quotient_rank": fine["quotient_rank"],
            "quotient_residual_squared": [mp.nstr(mp.mpf(value), 14) for value in fine["residual_diagonal"]],
            "interpolation_upper_squared": [mp.nstr(mp.mpf(value), 14) for value in fine["interpolation_bounds_squared"]],
            "whole_negative_trace": mp.nstr(mp.mpf(fine["whole_negative_trace"]), 14),
            "compressed_negative_trace": mp.nstr(mp.mpf(fine["compressed_negative_trace"]), 14),
            "compressed_trace_upper_bound": mp.nstr(mp.mpf(fine["compressed_trace_upper_bound"]), 14),
            "trace_error_at_120_digits": mp.nstr(mp.mpf(fine["trace_error"]), 8),
            "max_relative_80_120_difference": mp.nstr(stability, 8),
        }))
    print(json.dumps({
        "status": "PASS", "label": "[E] finite synthetic Gram/congruence audit only",
        "cases": len(cases), "precisions": [80, 120],
        "max_relative_80_120_difference": mp.nstr(maximum_relative_precision_difference, 12),
        "seconds": round(time.perf_counter() - started, 3),
        "actual_zeros_used": False, "asymptotic_or_interval_certification": False,
        "whole_operator_equals_compression": False,
    }))


if __name__ == "__main__":
    main()
