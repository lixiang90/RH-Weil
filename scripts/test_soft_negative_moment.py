"""Regression checks for soft negative effects and Cauchy lag moments."""

from __future__ import annotations

import numpy as np

from formal_lag_response import (
    cauchy_gaussian_mixture_band_ledger,
    cauchy_gaussian_mixture_cdf,
    degree_two_gaussian_response_upper_bound,
    degree_two_parity_exact_ledger,
    degree_two_response_frequency_map,
    exact_formal_moment,
    gaussian_heat_shell_ledger,
    gaussian_signed_layer_cake_ledger,
    stationary_response_from_frequency_map,
    two_sided_prime_continuum_symbol,
)

from soft_negative_moment import (
    cauchy_stationary_moments,
    cauchy_orbit_square_response,
    chebyshev_orbit_coefficients,
    chebyshev_soft_ledger,
    chebyshev_soft_polynomial,
    chebyshev_soft_series,
    negative_polynomial_hankel_response,
    polynomial_soft_ledger,
    high_order_vanishing_coefficient_tax,
    soft_negative_ledger,
    soft_transition_degree_lower_bound,
    spectral_moments,
)


def main() -> None:
    rng = np.random.default_rng(187)
    values = rng.normal(size=17)
    weights = rng.random(17)
    weights /= weights.sum()
    rho = 0.35

    soft = soft_negative_ledger(values, weights, rho)
    assert soft["soft_response"] <= soft["negative_mass"] + 1.0e-14
    assert soft["negative_mass"] <= soft["upper_bound"] + 1.0e-14
    assert 0.0 <= soft["deficit"] <= 2.0 * rho + 1.0e-14

    spectral_bound = float(np.max(np.abs(values)) + 0.1)
    series_coefficients = chebyshev_soft_series(
        spectral_bound=spectral_bound, rho=rho, degree=48
    )
    chebyshev = chebyshev_soft_ledger(
        values, weights, spectral_bound, rho, series_coefficients
    )
    assert np.max(np.abs(chebyshev["contraction_values"])) <= 1.0 + 1.0e-12
    assert chebyshev["negative_mass"] <= chebyshev["upper_bound"] + 1.0e-12

    # A modest power degree verifies the exact Hankel identity.  At high
    # degree, converting the well-conditioned Chebyshev series to monomials
    # is deliberately avoided because of catastrophic cancellation.
    coefficients = chebyshev_soft_polynomial(
        spectral_bound=spectral_bound, rho=rho, degree=12
    )
    polynomial = polynomial_soft_ledger(
        values, weights, rho, coefficients
    )
    assert np.max(np.abs(polynomial["contraction_values"])) <= 1.0 + 1.0e-12
    assert polynomial["negative_mass"] <= polynomial["upper_bound"] + 1.0e-12

    scaled_coefficients = coefficients / (
        1.0 + polynomial["uniform_spectral_error"]
    )
    moments = spectral_moments(
        values, weights, 2 * (len(scaled_coefficients) - 1) + 1
    )
    hankel_response = negative_polynomial_hankel_response(
        moments, scaled_coefficients
    )
    assert abs(hankel_response - polynomial["polynomial_response"]) <= 1.0e-8

    # P(t)=a+2c cos(lambda t).  The first two moments have closed forms.
    constant = 0.4
    cosine = -0.3
    lag = 0.7
    frequencies = np.array([0.0, lag, -lag])
    orbit_coefficients = np.array([constant, cosine, cosine], dtype=complex)
    cauchy_moments = cauchy_stationary_moments(
        frequencies, orbit_coefficients, 4
    )
    expected_first = constant + 2.0 * cosine * np.exp(-lag)
    expected_second = (
        constant**2
        + 4.0 * constant * cosine * np.exp(-lag)
        + 2.0 * cosine**2 * (1.0 + np.exp(-2.0 * lag))
    )
    assert abs(cauchy_moments[0] - 1.0) <= 1.0e-14
    assert abs(cauchy_moments[1] - expected_first) <= 1.0e-14
    assert abs(cauchy_moments[2] - expected_second) <= 1.0e-14
    assert np.max(np.abs(cauchy_moments.imag)) <= 1.0e-13

    # Verify the Chebyshev three-term frequency convolution against the
    # shifted Hankel response for a stable low-degree instance.
    orbit_bound = 1.5
    orbit_series = chebyshev_soft_series(orbit_bound, rho=0.4, degree=5)
    effect_frequencies, effect_coefficients = chebyshev_orbit_coefficients(
        frequencies,
        orbit_coefficients,
        orbit_bound,
        orbit_series,
    )
    orbit_response = cauchy_orbit_square_response(
        frequencies,
        orbit_coefficients,
        effect_frequencies,
        effect_coefficients,
    )
    power_in_scaled_variable = np.polynomial.Chebyshev(
        orbit_series
    ).convert(kind=np.polynomial.Polynomial).coef
    power_coefficients = power_in_scaled_variable / (
        orbit_bound ** np.arange(len(power_in_scaled_variable))
    )
    orbit_moments = cauchy_stationary_moments(
        frequencies, orbit_coefficients, 2 * len(power_coefficients) - 1
    )
    hankel_orbit_response = negative_polynomial_hankel_response(
        orbit_moments, power_coefficients
    )
    assert abs(orbit_response - hankel_orbit_response) <= 1.0e-10

    # Odd formal support has no odd exact moments.  Adding an even prime
    # power creates a parity breaker controlled by the perturbative ledger.
    odd_formal = two_sided_prime_continuum_symbol(
        prime_atoms=[(2, 0.4), (8, -0.15)],
        continuum_atoms=[(0.6, -0.2)],
    )["combined_map"]
    assert abs(exact_formal_moment(odd_formal, 3)) <= 1.0e-14
    assert abs(exact_formal_moment(odd_formal, 5)) <= 1.0e-14
    broken_formal = two_sided_prime_continuum_symbol(
        prime_atoms=[(2, 0.4), (4, 0.08), (8, -0.15)],
        continuum_atoms=[(0.0, -0.03), (0.6, -0.2)],
    )["combined_map"]
    bound = sum(abs(value) for value in broken_formal.values())
    parity = degree_two_parity_exact_ledger(
        broken_formal, spectral_bound=bound, rho=bound / 3.0
    )
    assert parity["breaker_l1_mass"] > 0.0
    assert abs(exact_formal_moment(broken_formal, 3)) <= (
        parity["odd_third_moment_bound"] + 1.0e-12
    )
    assert abs(exact_formal_moment(broken_formal, 5)) <= (
        parity["odd_fifth_moment_bound"] + 1.0e-12
    )
    assert abs(exact_formal_moment(broken_formal, 3)) <= (
        parity["odd_third_moment_l2_bound"] + 1.0e-12
    )
    assert abs(exact_formal_moment(broken_formal, 5)) <= (
        parity["odd_fifth_moment_l2_bound"] + 1.0e-12
    )
    assert abs(exact_formal_moment(broken_formal, 3)) <= (
        parity["odd_third_moment_norm_bound"] + 1.0e-12
    )
    assert abs(exact_formal_moment(broken_formal, 5)) <= (
        parity["odd_fifth_moment_norm_bound"] + 1.0e-12
    )

    # The Cauchy state is exactly a Gamma(1/2,1) mixture of normalized
    # Gaussian states.  The direct degree-two response map must reconstruct
    # both the original Cauchy response and every finite mixture band.
    response_map = degree_two_response_frequency_map(
        broken_formal, spectral_bound=bound, rho=bound / 3.0
    )
    continuum_nodes = (0.6,)
    direct_cauchy = stationary_response_from_frequency_map(
        response_map, continuum_nodes, lambda value: np.exp(-abs(value))
    )
    mixture = cauchy_gaussian_mixture_band_ledger(
        response_map,
        continuum_nodes,
        (0.0, 0.05, 0.4, 2.0, np.inf),
    )
    assert abs(mixture["total_response"] - direct_cauchy) <= 1.0e-12
    assert abs(
        cauchy_gaussian_mixture_cdf(0.7, np.inf) - np.exp(-0.7)
    ) <= 1.0e-14
    assert 0.0 < cauchy_gaussian_mixture_cdf(0.7, 0.4) < np.exp(-0.7)

    gaussian_scale = 0.7
    direct_gaussian = stationary_response_from_frequency_map(
        response_map,
        continuum_nodes,
        lambda value: np.exp(-(value**2) / (4.0 * gaussian_scale)),
    )
    gaussian_bound = degree_two_gaussian_response_upper_bound(
        broken_formal,
        continuum_nodes,
        spectral_bound=bound,
        rho=bound / 3.0,
        gaussian_scale=gaussian_scale,
    )
    assert abs(direct_gaussian) <= (
        gaussian_bound["response_upper_bound"] + 1.0e-12
    )
    heat_shells = gaussian_heat_shell_ledger(
        response_map, continuum_nodes, gaussian_scale
    )
    assert abs(heat_shells["total_response"] - direct_gaussian) <= 1.0e-12
    assert sum(heat_shells["counts"]) == (
        len(response_map)
        - sum(1 for lag in response_map if lag.is_zero())
    )
    layer_cake = gaussian_signed_layer_cake_ledger(
        response_map, continuum_nodes, gaussian_scale
    )
    assert abs(layer_cake["total_response"] - direct_gaussian) <= 1.0e-12
    assert abs(layer_cake["nonexact_response"]) <= (
        layer_cake["profile_capacity"] + 1.0e-12
    )
    assert layer_cake["profile_capacity"] <= (
        layer_cake["coefficient_variation"] + 1.0e-12
    )

    # A bounded additive soft error forces rho=O(1) while the spectral
    # interval may grow. Bernstein inequality then imposes a degree floor.
    degree_floor = soft_transition_degree_lower_bound(
        spectral_bound=100.0, rho=1.0, uniform_error=0.1
    )
    assert degree_floor > 27.0
    tax_order_one = high_order_vanishing_coefficient_tax(
        spectral_bound=100.0,
        rho=1.0,
        uniform_error=0.1,
        vanishing_order=1,
        relative_moment_scale=0.04,
    )
    tax_order_three = high_order_vanishing_coefficient_tax(
        spectral_bound=100.0,
        rho=1.0,
        uniform_error=0.1,
        vanishing_order=3,
        relative_moment_scale=0.04,
    )
    assert tax_order_one["applicable"] == 1.0
    assert tax_order_three["coefficient_ledger_lower_bound"] > (
        tax_order_one["coefficient_ledger_lower_bound"]
    )

    print("soft negative-effect and Cauchy moment checks passed")


if __name__ == "__main__":
    main()
