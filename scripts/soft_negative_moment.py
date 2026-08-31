"""Finite ledgers for soft negative effects and Cauchy orbit moments.

The routines verify spectral-functional-calculus and finite lag identities.
They do not bound a cofinal zeta current and are not evidence for RH.
"""

from __future__ import annotations

import itertools

import numpy as np
from numpy.polynomial import Chebyshev, Polynomial


def soft_negative_amplitude(values: np.ndarray, rho: float) -> np.ndarray:
    """Return a_rho(x)=(-x)_+/((-x)_+ + rho)."""
    if rho <= 0.0:
        raise ValueError("rho must be positive")
    values = np.asarray(values, dtype=float)
    negative = np.maximum(-values, 0.0)
    return negative / (negative + rho)


def soft_negative_ledger(
    values: np.ndarray, weights: np.ndarray, rho: float
) -> dict[str, float | np.ndarray]:
    """Audit the additive-2-rho soft negative-index sandwich."""
    values = np.asarray(values, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if values.shape != weights.shape:
        raise ValueError("values and weights must have the same shape")
    if np.any(weights < 0.0) or not np.isclose(weights.sum(), 1.0):
        raise ValueError("weights must be a probability vector")
    amplitude = soft_negative_amplitude(values, rho)
    negative_mass = float(weights @ np.maximum(-values, 0.0))
    soft_response = float(-weights @ (values * amplitude**2))
    return {
        "amplitude": amplitude,
        "negative_mass": negative_mass,
        "soft_response": soft_response,
        "deficit": negative_mass - soft_response,
        "upper_bound": soft_response + 2.0 * rho,
    }


def chebyshev_soft_polynomial(
    spectral_bound: float, rho: float, degree: int
) -> np.ndarray:
    """Return ascending power coefficients of a Chebyshev interpolant."""
    if spectral_bound <= 0.0:
        raise ValueError("spectral bound must be positive")
    if rho <= 0.0:
        raise ValueError("rho must be positive")
    if degree < 0:
        raise ValueError("degree must be nonnegative")

    def target(value: np.ndarray) -> np.ndarray:
        return soft_negative_amplitude(value, rho)

    interpolant = Chebyshev.interpolate(
        target, degree, domain=[-spectral_bound, spectral_bound]
    )
    return interpolant.convert(kind=Polynomial).coef


def chebyshev_soft_series(
    spectral_bound: float, rho: float, degree: int
) -> np.ndarray:
    """Return Chebyshev coefficients in the scaled variable x / bound."""
    if spectral_bound <= 0.0:
        raise ValueError("spectral bound must be positive")
    if rho <= 0.0:
        raise ValueError("rho must be positive")
    if degree < 0:
        raise ValueError("degree must be nonnegative")

    def target(value: np.ndarray) -> np.ndarray:
        return soft_negative_amplitude(value, rho)

    interpolant = Chebyshev.interpolate(
        target, degree, domain=[-spectral_bound, spectral_bound]
    )
    return interpolant.coef


def chebyshev_soft_ledger(
    values: np.ndarray,
    weights: np.ndarray,
    spectral_bound: float,
    rho: float,
    coefficients: np.ndarray,
) -> dict[str, float | np.ndarray]:
    """Audit a soft certificate without converting to the power basis."""
    values = np.asarray(values, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if np.max(np.abs(values)) > spectral_bound + 1.0e-12:
        raise ValueError("spectrum lies outside the supplied bound")
    if values.shape != weights.shape:
        raise ValueError("values and weights must have the same shape")
    if np.any(weights < 0.0) or not np.isclose(weights.sum(), 1.0):
        raise ValueError("weights must be a probability vector")
    target = soft_negative_amplitude(values, rho)
    series_values = np.polynomial.chebyshev.chebval(
        values / spectral_bound, coefficients
    )
    error = float(np.max(np.abs(series_values - target)))
    if error > 1.0:
        raise ValueError("Chebyshev approximation error must not exceed one")
    contraction = series_values / (1.0 + error)
    response = float(-weights @ (values * contraction**2))
    absolute_mass = float(weights @ np.abs(values))
    negative_mass = float(weights @ np.maximum(-values, 0.0))
    return {
        "target_amplitude": target,
        "series_values": series_values,
        "contraction_values": contraction,
        "uniform_spectral_error": error,
        "negative_mass": negative_mass,
        "chebyshev_response": response,
        "absolute_mass": absolute_mass,
        "upper_bound": response + 2.0 * rho + 5.0 * error * absolute_mass,
    }


def polynomial_soft_ledger(
    values: np.ndarray,
    weights: np.ndarray,
    rho: float,
    coefficients: np.ndarray,
) -> dict[str, float | np.ndarray]:
    """Audit a contraction-rescaled polynomial soft-effect certificate.

    The approximation error is measured on the supplied finite spectrum.
    For a theorem on a whole interval, replace it by a certified uniform
    interval error.
    """
    values = np.asarray(values, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if values.shape != weights.shape:
        raise ValueError("values and weights must have the same shape")
    if np.any(weights < 0.0) or not np.isclose(weights.sum(), 1.0):
        raise ValueError("weights must be a probability vector")
    target = soft_negative_amplitude(values, rho)
    polynomial = np.polynomial.polynomial.polyval(values, coefficients)
    error = float(np.max(np.abs(polynomial - target)))
    if error > 1.0:
        raise ValueError("polynomial approximation error must not exceed one")
    contraction = polynomial / (1.0 + error)
    response = float(-weights @ (values * contraction**2))
    absolute_mass = float(weights @ np.abs(values))
    negative_mass = float(weights @ np.maximum(-values, 0.0))
    return {
        "target_amplitude": target,
        "polynomial_values": polynomial,
        "contraction_values": contraction,
        "uniform_spectral_error": error,
        "negative_mass": negative_mass,
        "polynomial_response": response,
        "absolute_mass": absolute_mass,
        "upper_bound": response + 2.0 * rho + 5.0 * error * absolute_mass,
    }


def spectral_moments(
    values: np.ndarray, weights: np.ndarray, maximum_power: int
) -> np.ndarray:
    """Return probability-weighted moments m_k through maximum_power."""
    if maximum_power < 0:
        raise ValueError("maximum power must be nonnegative")
    values = np.asarray(values, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if values.shape != weights.shape:
        raise ValueError("values and weights must have the same shape")
    return np.array(
        [weights @ values**power for power in range(maximum_power + 1)],
        dtype=float,
    )


def negative_polynomial_hankel_response(
    moments: np.ndarray, coefficients: np.ndarray
) -> float:
    """Return -tau[X p(X)^2] from shifted Hankel moments."""
    moments = np.asarray(moments)
    coefficients = np.asarray(coefficients)
    degree = len(coefficients) - 1
    if len(moments) <= 2 * degree + 1:
        raise ValueError("moments are too short for the polynomial degree")
    response = 0.0 + 0.0j
    for left, left_coefficient in enumerate(coefficients):
        for right, right_coefficient in enumerate(coefficients):
            response -= (
                np.conjugate(left_coefficient)
                * right_coefficient
                * moments[left + right + 1]
            )
    return float(np.real_if_close(response))


def cauchy_stationary_moment(
    frequencies: np.ndarray, coefficients: np.ndarray, power: int
) -> complex:
    """Exact Cauchy moment of sum d_w exp(-i w t).

    The normalized Cauchy characteristic function is exp(-|u|), so the
    power-th moment is the finite lag-resonance sum returned here.
    """
    if power < 0:
        raise ValueError("power must be nonnegative")
    frequencies = np.asarray(frequencies, dtype=float)
    coefficients = np.asarray(coefficients, dtype=complex)
    if frequencies.shape != coefficients.shape:
        raise ValueError("frequencies and coefficients must have the same shape")
    if power == 0:
        return 1.0 + 0.0j
    total = 0.0 + 0.0j
    for indices in itertools.product(range(len(frequencies)), repeat=power):
        frequency_sum = sum(frequencies[index] for index in indices)
        coefficient_product = np.prod([coefficients[index] for index in indices])
        total += coefficient_product * np.exp(-abs(frequency_sum))
    return complex(total)


def cauchy_stationary_moments(
    frequencies: np.ndarray, coefficients: np.ndarray, maximum_power: int
) -> np.ndarray:
    """Return exact stationary Cauchy moments through maximum_power."""
    return np.array(
        [
            cauchy_stationary_moment(frequencies, coefficients, power)
            for power in range(maximum_power + 1)
        ],
        dtype=complex,
    )


def _frequency_map(
    frequencies: np.ndarray, coefficients: np.ndarray, digits: int
) -> dict[float, complex]:
    result: dict[float, complex] = {}
    for frequency, coefficient in zip(frequencies, coefficients):
        key = round(float(frequency), digits)
        result[key] = result.get(key, 0.0 + 0.0j) + complex(coefficient)
    return {key: value for key, value in result.items() if abs(value) > 1.0e-15}


def _convolve_frequency_maps(
    left: dict[float, complex],
    right: dict[float, complex],
    digits: int,
) -> dict[float, complex]:
    result: dict[float, complex] = {}
    for left_frequency, left_coefficient in left.items():
        for right_frequency, right_coefficient in right.items():
            frequency = round(left_frequency + right_frequency, digits)
            result[frequency] = result.get(frequency, 0.0 + 0.0j) + (
                left_coefficient * right_coefficient
            )
    return {key: value for key, value in result.items() if abs(value) > 1.0e-14}


def chebyshev_orbit_coefficients(
    frequencies: np.ndarray,
    coefficients: np.ndarray,
    spectral_bound: float,
    series_coefficients: np.ndarray,
    digits: int = 12,
) -> tuple[np.ndarray, np.ndarray]:
    """Expand sum alpha_k T_k(P/B) by frequency convolution.

    ``digits`` is only a finite numerical keying convention.  Exact
    arithmetic applications should represent logarithmic frequencies by
    symbolic product/exponent data before merging resonances.
    """
    if spectral_bound <= 0.0:
        raise ValueError("spectral bound must be positive")
    base = _frequency_map(frequencies, coefficients, digits)
    q_previous = {0.0: 1.0 + 0.0j}
    combined: dict[float, complex] = {
        key: complex(series_coefficients[0]) * value
        for key, value in q_previous.items()
    }
    if len(series_coefficients) == 1:
        ordered = sorted(combined)
        return np.array(ordered), np.array([combined[key] for key in ordered])

    q_current = {
        key: value / spectral_bound for key, value in base.items()
    }
    for key, value in q_current.items():
        combined[key] = combined.get(key, 0.0 + 0.0j) + (
            complex(series_coefficients[1]) * value
        )
    for degree in range(1, len(series_coefficients) - 1):
        convolution = _convolve_frequency_maps(base, q_current, digits)
        q_next: dict[float, complex] = {}
        for key in set(convolution) | set(q_previous):
            value = (
                2.0 * convolution.get(key, 0.0 + 0.0j) / spectral_bound
                - q_previous.get(key, 0.0 + 0.0j)
            )
            if abs(value) > 1.0e-14:
                q_next[key] = value
        coefficient = complex(series_coefficients[degree + 1])
        for key, value in q_next.items():
            combined[key] = combined.get(key, 0.0 + 0.0j) + coefficient * value
        q_previous, q_current = q_current, q_next

    combined = {
        key: value for key, value in combined.items() if abs(value) > 1.0e-13
    }
    ordered = sorted(combined)
    return np.array(ordered), np.array([combined[key] for key in ordered])


def cauchy_orbit_square_response(
    symbol_frequencies: np.ndarray,
    symbol_coefficients: np.ndarray,
    effect_frequencies: np.ndarray,
    effect_coefficients: np.ndarray,
) -> float:
    """Return -int P(t)|b(t)|^2 dmu from finite frequency data."""
    total = 0.0 + 0.0j
    for frequency, coefficient in zip(symbol_frequencies, symbol_coefficients):
        for left_frequency, left_coefficient in zip(
            effect_frequencies, effect_coefficients
        ):
            for right_frequency, right_coefficient in zip(
                effect_frequencies, effect_coefficients
            ):
                total -= (
                    coefficient
                    * left_coefficient
                    * np.conjugate(right_coefficient)
                    * np.exp(
                        -abs(frequency + left_frequency - right_frequency)
                    )
                )
    return float(np.real_if_close(total))
