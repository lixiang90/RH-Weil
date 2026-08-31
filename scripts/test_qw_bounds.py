"""Reproducible numerical sanity checks for the proved QW matrix bounds.

These checks detect formula/transcription errors.  They are not rigorous
interval certificates and are not evidence for RH.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np

from qw_matrix import (
    all_orders_candidate_tail_bound,
    boundary_vanishing_candidate_tail_bound,
    candidate_fourth_order_coefficient,
    candidate_leading_coefficient,
    finite_phase_third_order_candidate_tail_bound,
    fourth_order_candidate_tail_bound,
    exact_resolvent_tail_component,
    certificate_off_diagonal_bound,
    improved_off_diagonal_bound,
    improved_row_square_tail_bound,
    hybrid_even_candidate_tail_bound,
    off_diagonal_bound,
    q_nm,
    qw_entry,
    prime_graph_decomposition_for_function,
    prime_graph_symbol,
    prime_log_moment,
    prime_phase_sum,
    prime_mass,
    build_polarization_defect_matrices,
    archimedean_spectral_bottom,
    archimedean_multiplier,
    archimedean_quadratic_constant,
    central_resonance_radius,
    canonical_bad_multiplier,
    canonical_weil_multiplier,
    dirichlet_archimedean_multiplier,
    dirichlet_archimedean_spectral_bottom,
    gamma_euler_lower_bound,
    gamma_euler_multiplier,
    generalized_eigenvalues,
    largest_generalized_eigenvalue,
    phase_volume_obstruction_constant,
    prolate_trace_tail_bound,
    rank_one_resolvent_upper,
    residual_feshbach_lower_matrix,
    weighted_candidate_tail_bound,
    weighted_prime_gap_average,
    smoothed_prime_gap_sum,
    zeta_smoothed_gap_explicit_approximation,
    zeta_boundary_zero_gram,
    zeta_boundary_zero_abel_gram,
    two_channel_hodge_lower_eigenvalue,
    two_channel_schur_margin,
    chebyshev_abel_energy,
    chebyshev_prefix_hodge_energy,
    chebyshev_prefix_log_block_energy,
    chebyshev_step_block_variance,
    chebyshev_step_block_charges,
    reverse_brownian_green_kernel,
    reverse_dirichlet_laplacian,
    prefix_scalar_bridge_decomposition,
    discrete_brownian_bridge_green_kernel,
    dirichlet_bridge_laplacian,
    cesaro_orbit_metric,
    cesaro_orbit_gram,
    cesaro_orbit_energy,
    polarization_similitude_residual,
    ihara_frobenius_operator,
    ihara_hodge_metric,
    ihara_bass_matrix,
    primes_up_to,
    prime_orbit_schatten_sum,
    finite_prime_euler_inverse,
    finite_prime_regularized_determinant,
    finite_prime_regularization_counterterm,
    regularized_positive_residual_certificate,
    prime_critical_regularization_certificate,
    prime_regularization_anomaly_current_certificate,
    positive_real_pick_gram,
    positive_real_completion_certificate,
    stable_pole_passive_impedance_certificate,
    centerline_passive_impedance_certificate,
    zeta_renormalized_prime_impedance,
    zeta_renormalized_impedance_pick_certificate,
    zeta_abel_prime_impedance,
    zeta_abel_impedance_pick_certificate,
    zeta_abel_resonance_well_audit,
    zeta_abel_cauchy_negative_mass_audit,
    cayley_dirichlet_inner_value,
    finite_shift_autocorrelation,
    autocorrelation_toeplitz_gram,
    cauchy_correlation_dominating_gram,
    cauchy_capped_correlation_modulus_bound,
    capped_correlation_gram_certificate,
    correlation_first_column_objective_gram,
    loewner_interval_linear_minimum,
    loewner_interval_linear_minimum_numpy,
    correlation_stationarity_defect,
    stationary_capped_functional_minimum,
    stationary_cauchy_block_negative_trace_audit,
    stationary_modulated_interval_energy,
    gallagher_fejer_band_constant,
    balanced_vaughan_coefficients,
    vaughan_laurent_channel_data,
    balanced_vaughan_modulated_gram_audit,
    modulated_atomic_component_gram,
    component_gram_channel_spectrum,
    matrix_bessel_loewner_certificate,
    component_gram_vector_error_majorant,
    common_component_channel_basis,
    orthonormal_channel_basis_from_seeds,
    forced_physical_transverse_channel_basis,
    vaughan_paired_incidence_channel_certificate,
    vaughan_incidence_separated_channel_certificate,
    vaughan_incidence_separated_basis_from_ratios,
    incidence_separated_plane_angle_certificate,
    frozen_vaughan_tilted_incidence_basis,
    frozen_vaughan_tilted_channel_coefficients,
    component_projector_no_free_lunch_certificate,
    channel_projector_stability_certificate,
    component_channel_feshbach_majorant,
    optimal_real_rank_one_background_split,
    abel_continuum_lag_quadrature,
    balanced_vaughan_continuum_gauge_audit,
    constrained_real_quadratic_minimizer,
    simplex_scale_affine_quadratic_minimizer,
    multiscale_vaughan_continuum_gauge_audit,
    stationary_cauchy_symbol_moments,
    stationary_signed_orbit_laplacian_audit,
    single_abel_zero_wave_half_period_certificate,
    gamma_translate_l2_gram,
    zeta_abel_capped_loewner_quadrature,
    zeta_abel_shared_lag_loewner_quadrature,
    zeta_abel_shared_stationary_certificate,
    zeta_abel_shared_cauchy_energy_certificate,
    abel_shared_cofinal_discretization_schedule,
    weighted_prolate_core_rank_bound,
    abel_coefficient_square_mass_majorant,
    abel_cofinal_scaling_ledger,
    abel_cauchy_high_tail_bound,
    abel_square_root_core_schedule,
    weighted_hodge_inertia_density_bound,
    abel_cyclic_core_leakage_bound,
    abel_resolvent_core_leakage_bound,
    cauchy_resolvent_weight_constant,
    cauchy_weighted_core_gram_bound,
    dirichlet_convolution_matrix,
    dirichlet_inverse_coefficients,
    dirichlet_incidence_hodge_kernel,
    dirichlet_incidence_hodge_energy,
    beurling_fractional_feature,
    positive_gram_schur_distance,
    sampled_beurling_hodge_data,
    beurling_target_coupling,
    beurling_feature_norm_squared,
    normalize_beurling_gram_data,
    positive_gram_feshbach_distance,
    mobius,
    mobius_log_divisor_moment,
    polynomial_mobius_mollifier_coefficients,
    zeta_mollifier_low_convolution,
    beurling_mollifier_residual,
    beurling_mollifier_local_energy,
    linear_mobius_mollifier_slope,
    weighted_mertens_normalized_slope,
    chebyshev_ratio_mean,
    linear_mollifier_local_hodge_decomposition,
    reduced_denominator_density,
    beurling_periodic_fourier_energy,
    mollifier_conductor_amplitude,
    linear_mollifier_conductor_amplitude_majorant,
    parabolic_shell_diagonal_energy,
    farey_determinant_reduction,
    generic_unrestricted_farey_harmonic_correlation,
    coprime_farey_harmonic_reciprocity,
    finite_cotangent_dft,
    coprime_farey_cotangent_dft,
    coprime_farey_product_modulus_dft,
    euler_totient,
    linear_conductor_mellin_data,
    mobius_logarithmic_riesz_sum,
    coprime_mobius_logarithmic_riesz_sum,
    local_smooth_convolution_riesz_sum,
    mobius_logarithmic_riesz_moment,
    coprime_mobius_logarithmic_riesz_moment,
    local_smooth_convolution_riesz_moment,
    endpoint_polynomial_riesz_data,
    endpoint_direction_riesz_transform,
    endpoint_riesz_projection_certificate,
    mobius_endpoint_direction_spatial_gram,
    mobius_endpoint_direction_local_gram,
    mobius_endpoint_direction_periodic_gram,
    nyman_endpoint_spatial_far_certificate,
    endpoint_quadratic_mass,
    endpoint_polarization_alignment_certificate,
    endpoint_projection_alignment_stability_certificate,
    positive_rank_update_response_kernel_certificate,
    positive_rank_update_diagonal_susceptibility_certificate,
    positive_rank_update_amplitude_capacity_certificate,
    endpoint_completion_multiamplitude_susceptibility_certificate,
    endpoint_polyhedral_riesz_determinant_certificate,
    endpoint_alternating_external_phase_certificate,
    endpoint_external_period_capacity_loss_certificate,
    dual_observation_block_overlap_certificate,
    mobius_endpoint_external_dyadic_overlap_certificate,
    mobius_endpoint_periodic_conductor_overlap_certificate,
    mobius_endpoint_conductor_completion_gap_certificate,
    acyclic_completion_superdeterminant_certificate,
    primitive_residual_superdeterminant_certificate,
    mobius_endpoint_mertens_regression_certificate,
    mobius_endpoint_sparse_observation_flow_certificate,
    mobius_endpoint_interpolation_period_certificate,
    mobius_unit_cell_tail_projection_certificate,
    endpoint_spatial_block_wedge_certificate,
    endpoint_bidirectional_capacity_susceptibility,
    endpoint_transversal_hodge_shorting,
    endpoint_transversal_hodge_completion,
    endpoint_spatial_shell_coercivity,
    nyman_endpoint_periodic_sandwich_certificate,
    localized_endpoint_riesz_leverage_certificate,
    polynomial_conductor_amplitude_via_riesz,
    reduced_cosecant_square_sum,
    shortest_farey_kernel_row_sum,
    squarefree_shared_gcd_allowed_residues,
    squarefree_shared_gcd_primitive_correlation,
    beurling_periodic_piecewise_energy,
    linear_mollifier_periodic_mean_via_mertens,
    mean_zero_quadratic_mobius_mollifier,
    mobius_endpoint_direction_response_via_mertens,
    mobius_cell_vandermonde_recovery_certificate,
    mobius_sparse_recovery_search,
    minimum_metric_mean_zero_mobius_mollifier,
    constrained_hodge_projection,
    nested_response_capacity_update,
    nested_constrained_hodge_update,
    quadratic_hodge_energy,
    easy_hard_constrained_hodge_certificate,
    exterior_power_matrix,
    endpoint_orbit_metric,
    thresholded_endpoint_inertia,
    spectral_atom_from_couplings,
    coherent_scalar_spectral_atom,
    recover_integer_spectral_multiplicity,
    finite_tracial_spectral_determinant,
    finite_tracial_log_derivative,
    power_prefix_hodge_energy,
    power_prefix_hodge_kernel,
    power_prefix_dual_laplacian,
    chebyshev_abel_energy_dirichlet,
    max_kernel_matrix,
    finite_max_kernel_matrix,
    max_kernel_trace,
    max_kernel_eigenvalue,
    max_kernel_eigenfunction,
    chebyshev_bessel_coefficient,
    twisted_chebyshev_abel_energy,
    zeta_bessel_euler_coordinate,
    chebyshev_block_variance,
    chebyshev_block_variance_max_kernel,
    chebyshev_windowed_block_energy,
    chebyshev_windowed_fourier_coefficient,
    chebyshev_triangular_discrepancy,
    chebyshev_triangular_discrepancy_integral,
    chebyshev_primitive_discrepancy,
    chebyshev_normalized_primitive,
    chebyshev_normalized_error,
    chebyshev_dilation_riesz_signal,
    chebyshev_dilation_riesz_signal_derivative,
    chebyshev_dilation_quadrature_gram,
    chebyshev_dilation_sobolev_quadrature_gram,
    triangular_ratio_profile,
    homogeneous_triangular_current_kernel,
    triangular_plateau_kernel,
    triangular_local_variance_kernel,
    two_moment_endpoint_core,
    endpoint_core_toeplitz_parameters,
    critical_zeta_endpoint_core_matrix,
    geometric_max_prefix_energy,
    chebyshev_log_block_moment,
    chebyshev_dyadic_core_charge,
    chebyshev_prime_wavelet,
    prime_wavelet_kernel,
    chebyshev_prime_wavelet_local_charge,
    chebyshev_prime_wavelet_diagonal,
    chebyshev_prime_wavelet_pair_block,
    prime_wavelet_riemann_remainder,
    chebyshev_prime_wavelet_centered_charge,
    chebyshev_prime_wavelet_centered_diagonal,
    prime_wavelet_centered_frame_block,
    primitive_prime_wavelet_kernel,
    prime_wavelet_homogeneous_profile,
    primitive_prime_wavelet_homogeneous_profile,
    primitive_profile_chamber_coefficients,
    primitive_prime_wavelet_homogeneous_kernel,
    primitive_homogeneous_moment_energy,
    primitive_centered_homogeneous_block,
    primitive_prime_wavelet_mellin,
    primitive_prime_wavelet_spectral_weight,
    massive_biharmonic_hodge_kernel,
    massive_biharmonic_moment_energy,
    centered_biharmonic_hodge_block,
    massive_sobolev_green_polynomial,
    massive_sobolev_hodge_kernel,
    massive_sobolev_moment_energy,
    centered_dirichlet_polynomial,
    sampled_massive_sobolev_energy,
    centered_logarithmic_moments,
    centered_annular_euler_coordinate,
    centered_annular_mellin_multiplier,
    annular_frame_spectral_multiplier,
    annular_abel_pair_kernel,
    annular_abel_moment_pair_kernel,
    annular_gamma_sampling_pair_kernel,
    annular_abel_rkhs_pair_kernel,
    rkhs_taylor_moment_weight,
    radial_taylor_sampling_weight,
    taylor_dirichlet_polynomial,
    taylor_sobolev_core_energy,
    chebyshev_primitive_prime_wavelet_charge,
    primitive_prime_wavelet_riemann_remainder,
    chebyshev_primitive_prime_wavelet_centered_charge,
    chebyshev_normalized_primitive_prime_wavelet,
    chebyshev_primitive_prime_wavelet_diagonal,
    chebyshev_primitive_prime_wavelet_block,
    second_order_candidate_tail_bound,
    third_order_candidate_tail_bound,
    third_order_oscillatory_coefficient,
    twisted_prime_phase_data,
    w02,
    von_mangoldt,
)


def main() -> None:
    mp.mp.dps = 60
    lam = mp.sqrt(13)
    length = 2 * mp.log(lam)

    # The Bass vertex polynomial is the characteristic determinant of the
    # companion Frobenius, and its explicit Hodge form is a q-similitude.
    q_graph = mp.mpf("2")
    adjacency_k4 = mp.matrix(
        [[0 if row == column else 1 for column in range(4)] for row in range(4)]
    )
    ihara_frobenius = ihara_frobenius_operator(adjacency_k4, q_graph)
    ihara_metric = ihara_hodge_metric(adjacency_k4, q_graph)
    ihara_residual = polarization_similitude_residual(
        ihara_frobenius, ihara_metric, q_graph
    )
    assert max(abs(entry) for entry in ihara_residual) < mp.mpf("1e-50")
    ihara_variable = mp.mpc("0.17", "0.09")
    assert mp.almosteq(
        mp.det(mp.eye(8) - ihara_variable * ihara_frobenius),
        mp.det(ihara_bass_matrix(adjacency_k4, q_graph, ihara_variable)),
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )

    # The Hodge inertia counts adjacency weights outside/on the Ramanujan
    # interval, with one negative/null direction per offending scalar block.
    ramanujan_edge = 2 * mp.sqrt(q_graph)
    spectral_adjacency = mp.diag(
        [-4, -ramanujan_edge, -1, 0, ramanujan_edge, 4]
    )
    spectral_metric = ihara_hodge_metric(spectral_adjacency, q_graph)
    numeric_metric = np.array(
        [
            [complex(spectral_metric[row, column]) for column in range(12)]
            for row in range(12)
        ],
        dtype=np.complex128,
    )
    metric_eigenvalues = np.linalg.eigvalsh(numeric_metric)
    assert np.count_nonzero(metric_eigenvalues < -1e-10) == 2
    assert np.count_nonzero(np.abs(metric_eigenvalues) <= 1e-10) == 2

    # A prime-local Schatten determinant differs from the finite inverse
    # Euler product by exactly its missing low prime-power traces.
    assert primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    determinant_point = mp.mpc("0.6", "0.7")
    determinant_order = 3
    determinant_cutoff = 97
    regularized = finite_prime_regularized_determinant(
        determinant_point, determinant_order, determinant_cutoff
    )
    counterterm = finite_prime_regularization_counterterm(
        determinant_point, determinant_order, determinant_cutoff
    )
    assert mp.almosteq(
        regularized * counterterm,
        finite_prime_euler_inverse(determinant_point, determinant_cutoff),
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )
    assert prime_orbit_schatten_sum(mp.mpf("0.5"), 3, 97) < (
        prime_orbit_schatten_sum(mp.mpf("0.5"), 2, 97)
    )
    regularized_positive = regularized_positive_residual_certificate(
        mp.diag([mp.mpf("0.2"), mp.mpf("0.4")]), 3
    )
    assert regularized_positive["signed_logarithmic_remainder"] > 0
    assert regularized_positive["regularized_determinant"] > 1
    assert mp.almosteq(
        regularized_positive["logarithmic_remainder"],
        regularized_positive["integral_remainder"],
        rel_eps=mp.mpf("1e-49"),
        abs_eps=mp.mpf("1e-49"),
    )
    assert regularized_positive["identical_pair_regularized_ratio"] == 1
    critical_regularization = prime_critical_regularization_certificate(
        97, mp.mpf("0.7")
    )
    assert mp.almosteq(
        critical_regularization["reconstructed_euler_inverse"],
        critical_regularization["finite_euler_inverse"],
        rel_eps=mp.mpf("1e-49"),
        abs_eps=mp.mpf("1e-49"),
    )
    assert critical_regularization["cubic_schatten_sum"] < (
        critical_regularization["hilbert_schmidt_partial_sum"]
    )
    anomaly_current = prime_regularization_anomaly_current_certificate(
        mp.mpc("0.6", "0.7"), 97
    )
    assert mp.almosteq(
        anomaly_current["reconstructed_euler_log_derivative"],
        anomaly_current["euler_log_derivative"],
        rel_eps=mp.mpf("1e-49"),
        abs_eps=mp.mpf("1e-49"),
    )

    # A center-line divisor has an exact passive impedance realization.
    # Its positive-real Pick kernel is literally a resolvent-feature Gram.
    passive_points = [
        mp.mpc("0.3", "0.2"),
        mp.mpc("0.7", "-0.4"),
        mp.mpc("1.1", "0.8"),
    ]
    passive = centerline_passive_impedance_certificate(
        passive_points,
        [mp.mpf("1.2"), mp.mpf("2.4")],
        [2, 1],
        central_multiplicity=1,
    )
    assert passive["minimum_pick_eigenvalue"] > -mp.mpf("1e-48")
    assert max(
        abs(
            passive["pick_gram"][row, column]
            - passive["feature_gram"][row, column]
        )
        for row in range(len(passive_points))
        for column in range(len(passive_points))
    ) < mp.mpf("1e-48")
    assert all(mp.re(value) > 0 for value in passive["impedance_values"])
    shifted_passive = stable_pole_passive_impedance_certificate(
        passive_points,
        [mp.mpc("-0.2", "1.1"), mp.mpc("-0.8", "-1.1")],
        [2, 1],
    )
    assert shifted_passive["minimum_pick_eigenvalue"] > -mp.mpf("1e-48")
    assert max(
        abs(
            shifted_passive["pick_gram"][row, column]
            - shifted_passive["decomposed_gram"][row, column]
        )
        for row in range(len(passive_points))
        for column in range(len(passive_points))
    ) < mp.mpf("1e-48")
    off_center_point = mp.mpc("0.8", "0")
    off_center_value = -2 * off_center_point / (1 - off_center_point**2)
    off_center_pick = positive_real_pick_gram(
        [off_center_point], [off_center_value]
    )
    assert mp.re(off_center_pick[0, 0]) < 0
    off_center_completion = positive_real_completion_certificate(
        [off_center_point], [off_center_value]
    )
    assert off_center_completion["completion_charge"] > 0
    assert min(off_center_completion["completed_pick_eigenvalues"]) > (
        -mp.mpf("1e-48")
    )

    # The sharp Chebyshev cutoff plus its continuum pole tail is holomorphic
    # at s=1 and is made only from prime/Gamma data.  Finite Pick matrices are
    # diagnostic; their eventual locally bounded passive limit is the theorem.
    pole_point = mp.mpc("0.5", "0")
    pole_value = zeta_renormalized_prime_impedance(pole_point, 100)
    nearby_value = zeta_renormalized_prime_impedance(
        pole_point + mp.mpf("1e-20"), 100
    )
    assert mp.almosteq(
        pole_value,
        nearby_value,
        rel_eps=mp.mpf("1e-17"),
        abs_eps=mp.mpf("1e-17"),
    )
    renormalized_pick = zeta_renormalized_impedance_pick_certificate(
        passive_points, 100
    )
    assert renormalized_pick["pick_gram"].rows == len(passive_points)

    # Exponential Abel smoothing makes both the prime current and its
    # continuum comparison entire in s.  The incomplete-gamma transcription
    # and the analytic Lambda(n)<=log(n) truncation bound are checked here.
    abel_point = mp.mpc("0.3", "0.4")
    abel_scale = mp.mpf("5")
    abel_cutoff = 200
    abel = zeta_abel_prime_impedance(
        abel_point, abel_scale, abel_cutoff
    )
    direct_continuum = mp.quad(
        lambda variable: (
            mp.power(variable, -(abel_point + mp.mpf("0.5")))
            * mp.exp(-variable / abel_scale)
        ),
        [1, mp.inf],
    )
    assert mp.almosteq(
        abel["continuum_current"],
        direct_continuum,
        rel_eps=mp.mpf("1e-48"),
        abs_eps=mp.mpf("1e-48"),
    )
    assert abel["prime_tail_bound"] > 0
    abel_pick = zeta_abel_impedance_pick_certificate(
        passive_points, abel_scale, abel_cutoff
    )
    assert abel_pick["pick_operator_error_bound"] > 0
    assert abel_pick["completion_charge"] >= 0
    assert abel_pick["certified_minimum_lower_bound"] <= (
        abel_pick["minimum_pick_eigenvalue"]
    )
    assert abel_pick["minimum_pick_eigenvalue"] <= (
        abel_pick["certified_minimum_upper_bound"]
    )
    abel_resonance = zeta_abel_resonance_well_audit(
        mp.mpf("0.1"),
        mp.mpf("5"),
        200,
        mp.mpf("0"),
        mp.mpf("4"),
        mp.mpf("1"),
    )
    assert len(abel_resonance["heights"]) == 5
    assert abel_resonance["coefficient_square_mass"] > 0
    assert abel_resonance["elementary_mean_square_bound"] > 0
    cauchy_audit = zeta_abel_cauchy_negative_mass_audit(
        mp.mpf("0.1"),
        mp.mpf("5"),
        200,
        mp.mpf("4"),
        mp.mpf("1"),
        [mp.mpc("0.4", "0.7")],
    )
    assert cauchy_audit["sampled_full_line_cauchy_negative_mass"] >= 0
    assert len(cauchy_audit["sampled_resolvent_negative_energies"]) == 1
    assert cauchy_audit["sampled_resolvent_negative_energies"][0] >= 0
    assert mp.almosteq(
        cauchy_audit["exact_full_line_signed_cauchy_integral"],
        mp.pi * cauchy_audit["poisson_center_real_impedance"],
    )
    assert cauchy_audit["sampled_centered_quadratic_cauchy_integral"] >= 0
    assert cauchy_audit["sampled_capped_defect_per_pi"] >= 0
    assert cauchy_audit["sampled_unrestricted_character_negative_depth"] >= 0
    cayley_point = mp.mpc("0.2", "-0.3")
    cayley_first = cayley_dirichlet_inner_value(
        mp.log(2), cayley_point
    )
    cayley_second = cayley_dirichlet_inner_value(
        mp.log(3), cayley_point
    )
    assert mp.almosteq(
        cayley_first * cayley_second,
        cayley_dirichlet_inner_value(mp.log(6), cayley_point),
        rel_eps=mp.mpf("1e-48"),
        abs_eps=mp.mpf("1e-48"),
    )
    assert mp.almosteq(
        cayley_dirichlet_inner_value(mp.log(7), mp.mpc(0)),
        mp.mpf(1) / 7,
        rel_eps=mp.mpf("1e-48"),
        abs_eps=mp.mpf("1e-48"),
    )
    shift_correlations = finite_shift_autocorrelation(
        [mp.mpc(1, 1), mp.mpc(2, -1), mp.mpc(-1, "0.5")],
        normalize=True,
    )
    assert mp.almosteq(shift_correlations[0], 1)
    shift_gram = autocorrelation_toeplitz_gram(shift_correlations)
    shift_eigenvalues = mp.eighe(shift_gram, eigvals_only=True)
    assert min(
        shift_eigenvalues[index]
        for index in range(shift_eigenvalues.rows)
    ) >= -mp.mpf("1e-48")
    cap_nodes = [mp.mpf("0"), mp.mpf("0.4"), mp.mpf("1.1")]
    fine_modulus = cauchy_capped_correlation_modulus_bound(
        mp.mpf("1e-4")
    )
    coarse_modulus = cauchy_capped_correlation_modulus_bound(
        mp.mpf("0.1")
    )
    assert fine_modulus["combined_modulus_bound"] < (
        coarse_modulus["combined_modulus_bound"]
    )
    assert fine_modulus["combined_modulus_bound"] <= (
        fine_modulus["cauchy_l2_modulus_bound"]
    )
    cap_gram = cauchy_correlation_dominating_gram(cap_nodes)
    density_fraction = mp.mpf("0.35")
    capped_certificate = capped_correlation_gram_certificate(
        cap_nodes, density_fraction * cap_gram
    )
    assert capped_certificate["minimum_correlation_eigenvalue"] > 0
    assert capped_certificate["minimum_cap_complement_eigenvalue"] > 0
    stationary_cap_audit = correlation_stationarity_defect(
        cap_nodes, cap_gram
    )
    assert stationary_cap_audit["diagonal_spread"] <= 1e-14
    nonstationary_audit = correlation_stationarity_defect(
        cap_nodes,
        mp.diag([mp.mpf("0.1"), mp.mpf("0.2"), mp.mpf("0.3")]),
    )
    assert nonstationary_audit["diagonal_spread"] > 0
    constant_stationary_minimum = stationary_capped_functional_minimum(
        [mp.mpf("0")],
        [mp.mpf("-2")],
        mp.mpf("10"),
        100,
    )
    assert abs(
        constant_stationary_minimum["certified_stationary_lower_bound"] + 2
    ) <= 1e-12
    objective_coefficients = [mp.mpf("-2"), mp.mpc("0.4", "0.3"), mp.mpf("1")]
    objective_gram = correlation_first_column_objective_gram(
        objective_coefficients
    )
    loewner_minimum = loewner_interval_linear_minimum(
        cap_gram, objective_gram
    )
    loewner_minimum_numpy = loewner_interval_linear_minimum_numpy(
        cap_gram, objective_gram
    )
    assert abs(
        float(loewner_minimum["minimum_objective"])
        - loewner_minimum_numpy["minimum_objective"]
    ) <= 1e-12
    assert mp.almosteq(
        loewner_minimum["minimum_objective"],
        loewner_minimum["optimizer_objective"],
        rel_eps=mp.mpf("1e-45"),
        abs_eps=mp.mpf("1e-45"),
    )
    optimizer_certificate = capped_correlation_gram_certificate(
        cap_nodes, loewner_minimum["optimizer_gram"]
    )
    assert optimizer_certificate["minimum_correlation_eigenvalue"] >= (
        -mp.mpf("1e-45")
    )
    assert optimizer_certificate["minimum_cap_complement_eigenvalue"] >= (
        -mp.mpf("1e-45")
    )
    capped_quadrature = zeta_abel_capped_loewner_quadrature(
        horizontal_offset=mp.mpf("0.2"),
        scale=mp.mpf("2"),
        integer_cutoff=40,
        pole_end=mp.mpf("4"),
        pole_cells=2,
        gamma_start=mp.mpf("0.1"),
        gamma_end=mp.mpf("4"),
        gamma_cells=2,
        continuum_end=mp.mpf("3"),
        continuum_cells=2,
    )
    assert capped_quadrature["uniform_functional_error_bound"] > 0
    assert capped_quadrature["constant_probe_absolute_error"] <= (
        capped_quadrature["uniform_functional_error_bound"]
    )
    assert capped_quadrature["relaxed_minimum_objective"] <= (
        capped_quadrature["constant_probe_quadrature_value"]
    )
    shared_quadrature = zeta_abel_shared_lag_loewner_quadrature(
        horizontal_offset=mp.mpf("0.2"),
        scale=mp.mpf("2"),
        integer_cutoff=40,
        lag_start=mp.mpf("0.01"),
        lag_end=mp.mpf("4"),
        lag_cells=4,
        geometric_mesh=True,
    )
    assert shared_quadrature["constant_probe_absolute_error"] <= (
        shared_quadrature["uniform_functional_error_bound"]
    )
    assert shared_quadrature["uniform_functional_error_bound"] < (
        capped_quadrature["uniform_functional_error_bound"]
    )
    assert shared_quadrature["tail_error_bound"] > 0
    assert shared_quadrature["optimizer_stationarity"][
        "diagonal_spread"
    ] >= 0
    shared_stationary_minimum = stationary_capped_functional_minimum(
        shared_quadrature["lag_nodes"],
        shared_quadrature["correlation_coefficients"],
        mp.mpf("20"),
        400,
    )
    assert shared_stationary_minimum["sampled_stationary_minimum"] <= 0
    assert shared_stationary_minimum["certified_stationary_lower_bound"] <= (
        shared_stationary_minimum["sampled_stationary_minimum"]
    )
    constant_symbol_moments = stationary_cauchy_symbol_moments(
        [mp.mpf("0")], [mp.mpc("-2", "0")]
    )
    assert constant_symbol_moments["cauchy_mean"] == -2
    assert constant_symbol_moments["cauchy_second_moment"] == 4
    assert constant_symbol_moments["cauchy_centered_variance"] == 0
    assert constant_symbol_moments["cauchy_green_tail_energy"] == 0
    assert constant_symbol_moments["stationary_negative_mass_upper_bound"] == 2
    two_node_symbol_moments = stationary_cauchy_symbol_moments(
        [mp.mpf("0.3"), mp.mpf("1.1")],
        [mp.mpc("1.2", "-0.4"), mp.mpc("-0.7", "0.2")],
    )
    direct_modulus_square_moment = mp.fsum(
        coefficient_row
        * mp.conj(coefficient_column)
        * mp.exp(-abs(node_row - node_column))
        for node_row, coefficient_row in zip(
            [mp.mpf("0.3"), mp.mpf("1.1")],
            [mp.mpc("1.2", "-0.4"), mp.mpc("-0.7", "0.2")],
        )
        for node_column, coefficient_column in zip(
            [mp.mpf("0.3"), mp.mpf("1.1")],
            [mp.mpc("1.2", "-0.4"), mp.mpc("-0.7", "0.2")],
        )
    )
    assert mp.almosteq(
        two_node_symbol_moments["modulus_square_moment"],
        direct_modulus_square_moment,
    )
    assert mp.almosteq(
        two_node_symbol_moments["cauchy_second_moment"],
        two_node_symbol_moments["cauchy_boundary_real_square"]
        + two_node_symbol_moments["cauchy_green_tail_energy"],
    )
    signed_laplacian_audit = stationary_signed_orbit_laplacian_audit(
        [mp.mpf("0"), mp.mpf("0.7"), mp.mpf("1.3")],
        [mp.mpf("0.2"), mp.mpf("-1.1"), mp.mpf("0.8")],
        [mp.mpf("0"), mp.mpf("0.4"), mp.mpf("2")],
    )
    assert signed_laplacian_audit["maximum_identity_error"] < mp.mpf(
        "1e-50"
    )
    assert mp.almosteq(
        signed_laplacian_audit["degree_anomaly"], mp.mpf("-0.1")
    )
    assert all(
        record["positive_coefficient_laplacian"] >= 0
        and record["negative_coefficient_laplacian"] >= 0
        for record in signed_laplacian_audit["records"]
    )
    constant_negative_block_audit = (
        stationary_cauchy_block_negative_trace_audit(
            [mp.mpf("0")],
            [mp.mpf("-2")],
            [mp.mpf("0"), mp.mpf("1"), mp.mpf("3")],
            cells_per_block=32,
        )
    )
    assert abs(
        constant_negative_block_audit["full_negative_trace_upper_bound"]
        - 2
    ) < 1e-14
    assert constant_negative_block_audit["covered_grid_error_bound"] == 0
    assert abs(
        constant_negative_block_audit["covered_cauchy_mass"]
        + constant_negative_block_audit["cauchy_tail_mass"]
        - 1
    ) < 1e-15
    one_atom_modulated_energy = stationary_modulated_interval_energy(
        [mp.mpf("0.7")],
        [mp.mpc("2", "-1")],
        mp.mpf("13"),
        mp.mpf("0.4"),
    )
    assert mp.almosteq(
        one_atom_modulated_energy["modulated_interval_energy"],
        mp.mpf("0.4") * 5,
    )
    two_atom_modulated_energy = stationary_modulated_interval_energy(
        [mp.mpf("0"), mp.mpf("0.2")],
        [mp.mpf("1"), mp.mpf("1")],
        mp.mpf("3"),
        mp.mpf("0.4"),
    )
    expected_two_atom_energy = (
        2 * mp.mpf("0.4")
        + 2 * mp.mpf("0.2") * mp.cos(mp.mpf("0.6"))
    )
    assert mp.almosteq(
        two_atom_modulated_energy["modulated_interval_energy"],
        expected_two_atom_energy,
    )
    dense_audit_nodes = [
        mp.mpf("0"), mp.mpf("0.17"), mp.mpf("0.44"), mp.mpf("0.91")
    ]
    dense_audit_coefficients = [
        mp.mpc("0.3", "-0.2"),
        mp.mpc("-0.8", "0.1"),
        mp.mpc("1.2", "0.4"),
        mp.mpc("-0.5", "-0.7"),
    ]
    dense_audit_center = mp.mpf("5.3")
    dense_audit_width = mp.mpf("0.5")
    sliding_prefix_energy = stationary_modulated_interval_energy(
        dense_audit_nodes,
        dense_audit_coefficients,
        dense_audit_center,
        dense_audit_width,
    )
    dense_energy = mp.fsum(
        coefficient_j
        * mp.conj(coefficient_k)
        * mp.exp(
            -1j * dense_audit_center * (node_j - node_k)
        )
        * max(
            mp.mpf("0"),
            dense_audit_width - abs(node_j - node_k),
        )
        for node_j, coefficient_j in zip(
            dense_audit_nodes, dense_audit_coefficients
        )
        for node_k, coefficient_k in zip(
            dense_audit_nodes, dense_audit_coefficients
        )
    )
    assert mp.almosteq(
        sliding_prefix_energy["modulated_interval_energy"],
        mp.re(dense_energy),
    )
    assert abs(mp.im(dense_energy)) < mp.mpf("1e-50")
    fejer_band_data = gallagher_fejer_band_constant(
        mp.mpf("7"), mp.mpf("0.25")
    )
    assert mp.almosteq(
        fejer_band_data["log_window_width"],
        mp.mpf("0.25") / 7,
    )
    assert mp.almosteq(
        fejer_band_data["band_energy_multiplier"],
        fejer_band_data["dimensionless_gallagher_constant"] * 49,
    )
    assert fejer_band_data["minimum_fejer_weight_on_band"] > 0
    vaughan_decomposition = balanced_vaughan_coefficients(80, 4, 5)
    assert vaughan_decomposition["maximum_reconstruction_residual"] < (
        mp.mpf("1e-48")
    )
    for integer in range(1, 81):
        assert mp.almosteq(
            vaughan_decomposition["reconstruction"][integer],
            von_mangoldt(integer) - 1,
            rel_eps=mp.mpf("1e-48"),
            abs_eps=mp.mpf("1e-48"),
        )
    type_ii_lower = vaughan_decomposition["type_ii_support_lower_bound"]
    assert type_ii_lower == 30
    assert all(
        abs(vaughan_decomposition["components"]["type_ii"][integer])
        < mp.mpf("1e-50")
        for integer in range(1, type_ii_lower)
    )
    single_laurent = vaughan_laurent_channel_data(
        [(2, 3)], [mp.mpf(1)],
        [mp.mpf("0.1"), mp.mpf("0.2"), mp.mpf("0.3"), mp.mpf("0.4")],
    )
    expected_m0 = mp.mpf("0.5")
    expected_m1 = mp.log(2) / 2
    expected_l0 = mp.log(2) / 2 + mp.log(3) / 3
    single_record = single_laurent["cutoff_records"][0]
    assert mp.almosteq(single_record["mobius_value_at_one"], expected_m0)
    assert mp.almosteq(
        single_record["mobius_derivative_at_one"], expected_m1
    )
    assert mp.almosteq(
        single_record["truncated_mangoldt_value_at_one"], expected_l0
    )
    assert mp.almosteq(
        single_record["double_pole_vector"][2], -expected_m0
    )
    assert mp.almosteq(
        single_record["simple_pole_vector"][1], -expected_m0 * expected_l0
    )
    assert mp.almosteq(
        single_record["simple_pole_vector"][2],
        1 + expected_m0 * expected_l0 - expected_m1,
    )
    expected_m2 = -mp.log(2) ** 2 / 4
    expected_l1 = -(
        mp.log(2) ** 2 / 2 + mp.log(3) ** 2 / 3
    )
    assert mp.almosteq(
        single_record["mobius_second_laurent_coefficient"], expected_m2
    )
    assert mp.almosteq(
        single_record["truncated_mangoldt_derivative_at_one"], expected_l1
    )
    assert mp.almosteq(
        single_record["regular_constant_vector"][0],
        expected_m2 + expected_m0 * mp.stieltjes(1),
    )
    assert abs(single_record["regular_sum_residual"]) < mp.mpf("1e-50")
    mixed_laurent = vaughan_laurent_channel_data(
        [(2, 3), (4, 5)],
        [mp.mpf("0.25"), mp.mpf("0.75")],
        [mp.mpf("0.1"), mp.mpf("0.2"), mp.mpf("0.3"), mp.mpf("0.4")],
    )
    for key in (
        "scale_weight_sum_residual",
        "continuum_weight_sum_residual",
        "mixed_double_sum_residual",
        "mixed_simple_sum_residual",
        "balanced_simple_sum_residual",
        "mixed_regular_sum_residual",
        "regular_transverse_sum_residual",
    ):
        assert abs(mixed_laurent[key]) < mp.mpf("1e-50")
    for basis_name in (
        "singular_basis", "physical_double_basis", "physical_simple_basis"
    ):
        basis = mixed_laurent[basis_name]
        assert basis["core_rank"] == 2
        assert basis["unitarity_residual"] < mp.mpf("1e-50")
    for basis_name in (
        "singular_annihilator_basis", "physical_regular_basis"
    ):
        basis = mixed_laurent[basis_name]
        assert basis["core_rank"] == 2
        assert basis["unitarity_residual"] < mp.mpf("1e-50")
    singular_projector = mixed_laurent["singular_basis"]["core_projector"]
    annihilator_projector = mixed_laurent[
        "singular_annihilator_basis"
    ]["core_projector"]
    physical_vector = mp.matrix(mixed_laurent["physical_vector"])
    assert mp.norm(singular_projector * physical_vector) < mp.mpf("1e-49")
    assert mp.norm(
        annihilator_projector * physical_vector - physical_vector
    ) < mp.mpf("1e-49")
    assert mp.norm(
        singular_projector + annihilator_projector - mp.eye(4)
    ) < mp.mpf("1e-49")
    vaughan_gram = balanced_vaughan_modulated_gram_audit(
        60,
        4,
        5,
        center_height=mp.mpf("7.25"),
        log_window_width=mp.mpf("0.18"),
        horizontal_offset=mp.mpf("0.08"),
        abel_scale=mp.mpf("25"),
    )
    assert vaughan_gram["hermitian_residual"] < mp.mpf("1e-48")
    assert abs(vaughan_gram["energy_reconstruction_residual"]) < (
        mp.mpf("1e-47")
    )
    assert vaughan_gram["gram_total_energy"] >= 0
    assert all(
        mp.re(vaughan_gram["component_gram"][index, index])
        >= -mp.mpf("1e-48")
        for index in range(4)
    )
    first_component = vaughan_gram["component_names"][0]
    first_component_energy = stationary_modulated_interval_energy(
        vaughan_gram["lag_nodes"],
        vaughan_gram["weighted_components"][first_component],
        vaughan_gram["center_height"],
        vaughan_gram["log_window_width"],
    )["modulated_interval_energy"]
    assert mp.almosteq(
        first_component_energy,
        mp.re(vaughan_gram["component_gram"][0, 0]),
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert not vaughan_gram["continuum_cell_component_included"]
    synthetic_component_gram = mp.matrix([[4, 0], [0, 1]])
    synthetic_split = optimal_real_rank_one_background_split(
        synthetic_component_gram,
        [mp.mpf("2"), mp.mpf("1")],
        mp.mpf("2"),
    )
    assert mp.almosteq(synthetic_split["optimal_weights"][0], mp.mpf("0.75"))
    assert mp.almosteq(synthetic_split["optimal_weights"][1], mp.mpf("0.25"))
    assert mp.almosteq(synthetic_split["optimized_diagonal_budget"], mp.mpf("2.75"))
    assert mp.almosteq(synthetic_split["anchor_split_diagonal_budget"], mp.mpf("3"))
    assert mp.almosteq(synthetic_split["equal_split_diagonal_budget"], mp.mpf("3"))
    assert mp.almosteq(synthetic_split["full_discrepancy_energy"], mp.mpf("1"))
    assert abs(synthetic_split["energy_invariance_residual"]) < mp.mpf("1e-50")
    assert abs(synthetic_split["minimum_formula_residual"]) < mp.mpf("1e-50")
    synthetic_atomic_gram = modulated_atomic_component_gram(
        {
            "first": ([mp.mpf("0")], [mp.mpf("2")]),
            "second": ([mp.mpf("0.2")], [mp.mpf("1")]),
        },
        center_height=mp.mpf("3"),
        log_window_width=mp.mpf("0.4"),
    )
    assert synthetic_atomic_gram["hermitian_residual"] < mp.mpf("1e-50")
    assert mp.almosteq(
        synthetic_atomic_gram["component_gram"][0, 0],
        mp.mpf("1.6"),
    )
    continuum_quadrature = abel_continuum_lag_quadrature(
        sigma=mp.mpf("0.6"),
        scale=mp.mpf("12"),
        lag_start=mp.mpf("0.001"),
        lag_end=mp.mpf("5"),
        lag_cells=12,
        log_window_width=mp.mpf("0.1"),
    )
    assert abs(continuum_quadrature["mass_reconstruction_residual"]) < (
        mp.mpf("1e-50")
    )
    assert continuum_quadrature["localization_vector_norm_bound"] > 0
    vaughan_continuum_gauge = balanced_vaughan_continuum_gauge_audit(
        cutoff=40,
        mobius_cutoff=3,
        mangoldt_cutoff=4,
        center_height=mp.mpf("5"),
        log_window_width=mp.mpf("0.05"),
        horizontal_offset=mp.mpf("0.1"),
        abel_scale=mp.mpf("12"),
        continuum_lag_start=mp.mpf("0.001"),
        continuum_lag_end=mp.log(41),
        continuum_lag_cells=10,
    )
    gauge_split = vaughan_continuum_gauge["optimal_split"]
    assert abs(gauge_split["weight_sum_residual"]) < mp.mpf("1e-49")
    assert abs(gauge_split["minimum_formula_residual"]) < mp.mpf("1e-48")
    assert abs(vaughan_continuum_gauge["direct_energy_residual"]) < (
        mp.mpf("1e-47")
    )
    assert gauge_split["optimized_diagonal_budget"] <= (
        gauge_split["anchor_split_diagonal_budget"] + mp.mpf("1e-48")
    )
    assert gauge_split["optimized_diagonal_budget"] <= (
        gauge_split["equal_split_diagonal_budget"] + mp.mpf("1e-48")
    )
    quadratic_optimizer = constrained_real_quadratic_minimizer(
        mp.matrix([[1, 0], [0, 2]]),
        mp.matrix([[1, 1]]),
        [mp.mpf("1")],
    )
    assert mp.almosteq(
        quadratic_optimizer["variables"][0], mp.mpf(2) / 3
    )
    assert mp.almosteq(
        quadratic_optimizer["variables"][1], mp.mpf(1) / 3
    )
    assert mp.almosteq(
        quadratic_optimizer["minimum_objective"], mp.mpf(2) / 3
    )
    assert quadratic_optimizer["constraint_residual_norm"] < mp.mpf("1e-50")
    assert quadratic_optimizer["stationarity_residual_norm"] < mp.mpf("1e-50")
    simplex_optimizer = simplex_scale_affine_quadratic_minimizer(
        mp.matrix([
            [1, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]),
        scale_count=2,
        component_count=2,
    )
    assert mp.almosteq(
        simplex_optimizer["optimal_scale_weights"][0], mp.mpf(2) / 3
    )
    assert mp.almosteq(
        simplex_optimizer["optimal_scale_weights"][1], mp.mpf(1) / 3
    )
    assert mp.almosteq(
        simplex_optimizer["optimal_background_weights"][0], mp.mpf("0.5")
    )
    assert mp.almosteq(
        simplex_optimizer["minimum_objective"], mp.mpf(7) / 6
    )
    assert simplex_optimizer["minimum_scale_weight"] >= 0
    multiscale_gauge = multiscale_vaughan_continuum_gauge_audit(
        cutoff=40,
        cutoff_pairs=[(2, 3), (3, 4), (4, 5)],
        center_height=mp.mpf("5"),
        log_window_width=mp.mpf("0.05"),
        horizontal_offset=mp.mpf("0.1"),
        abel_scale=mp.mpf("12"),
        continuum_lag_start=mp.mpf("0.001"),
        continuum_lag_end=mp.log(41),
        continuum_lag_cells=10,
    )
    assert abs(mp.fsum(multiscale_gauge["optimal_scale_weights"]) - 1) < (
        mp.mpf("1e-48")
    )
    assert abs(mp.fsum(multiscale_gauge["optimal_continuum_weights"]) - 1) < (
        mp.mpf("1e-48")
    )
    assert abs(multiscale_gauge["direct_energy_residual"]) < mp.mpf("1e-46")
    assert multiscale_gauge["optimized_diagonal_budget"] <= (
        multiscale_gauge["best_single_scale_diagonal_budget"]
        + mp.mpf("1e-47")
    )
    assert multiscale_gauge["optimized_diagonal_budget"] <= (
        multiscale_gauge["equal_scale_diagonal_budget"]
        + mp.mpf("1e-47")
    )
    assert multiscale_gauge["optimized_diagonal_budget"] <= (
        multiscale_gauge["simplex_scale_diagonal_budget"]
        + mp.mpf("1e-47")
    )
    assert multiscale_gauge["simplex_scale_diagonal_budget"] <= (
        multiscale_gauge["best_single_scale_diagonal_budget"]
        + mp.mpf("1e-47")
    )
    assert multiscale_gauge["simplex_optimizer"]["minimum_scale_weight"] >= (
        -mp.mpf("1e-48")
    )
    simplex_channels = multiscale_gauge["simplex_channel_spectrum"]
    assert simplex_channels["spectral_reconstruction_residual"] < mp.mpf("1e-47")
    assert mp.almosteq(
        simplex_channels["physical_energy"],
        multiscale_gauge["direct_discrepancy_energy"],
        rel_eps=mp.mpf("1e-46"),
        abs_eps=mp.mpf("1e-46"),
    )
    assert simplex_channels["diagonal_majorant_loss_factor"] >= 1
    diagonal_channel_spectrum = component_gram_channel_spectrum(
        mp.matrix([[2, 0], [0, 1]])
    )
    assert mp.almosteq(diagonal_channel_spectrum["physical_energy"], 3)
    assert mp.almosteq(diagonal_channel_spectrum["stable_rank"], mp.mpf(9) / 5)
    assert mp.almosteq(
        mp.fsum(
            record["physical_energy_contribution"]
            for record in diagonal_channel_spectrum["channel_records"]
        ),
        3,
    )
    loewner_gram = mp.matrix([[1, mp.mpf("0.2")], [mp.mpf("0.2"), 2]])
    loewner_majorant = loewner_gram + mp.mpf("0.3") * mp.eye(2)
    loewner_certificate = matrix_bessel_loewner_certificate(
        loewner_gram, loewner_majorant
    )
    assert mp.almosteq(
        loewner_certificate["minimum_majorant_difference_eigenvalue"],
        mp.mpf("0.3"),
    )
    assert loewner_certificate["matrix_physical_upper_bound"] >= (
        loewner_certificate["physical_energy"]
    )
    error_majorant = component_gram_vector_error_majorant(
        loewner_gram,
        [mp.mpf("1"), mp.sqrt(2)],
        [mp.mpf("0.1"), mp.mpf("0.2")],
    )
    assert error_majorant["loewner_radius"] > 0
    error_certificate = matrix_bessel_loewner_certificate(
        loewner_gram, error_majorant["loewner_majorant"]
    )
    assert error_certificate["minimum_majorant_difference_eigenvalue"] >= 0
    common_basis = common_component_channel_basis(
        [
            mp.matrix([[3, 0, 0], [0, 1, 0], [0, 0, mp.mpf("0.2")]]),
            mp.matrix([[2, 0, 0], [0, mp.mpf("1.5"), 0], [0, 0, mp.mpf("0.1")]]),
        ],
        channel_rank=1,
    )
    assert common_basis["unitarity_residual"] < mp.mpf("1e-50")
    assert abs(common_basis["core_channel_basis"][0, 0]) > mp.mpf("0.999")
    feshbach_gram = mp.matrix([
        [2, mp.mpf("0.3"), mp.mpf("0.1")],
        [mp.mpf("0.3"), 1, mp.mpf("0.2")],
        [mp.mpf("0.1"), mp.mpf("0.2"), mp.mpf("0.5")],
    ])
    feshbach_majorant = component_channel_feshbach_majorant(
        feshbach_gram,
        mp.eye(3),
        channel_rank=1,
    )
    assert feshbach_majorant["minimum_majorant_difference_eigenvalue"] >= (
        -mp.mpf("1e-48")
    )
    assert feshbach_majorant["physical_upper_bound"] >= (
        feshbach_majorant["physical_energy"]
    )
    assert feshbach_majorant["decomposition_residual"] < mp.mpf("1e-48")
    assert feshbach_majorant["tail_threshold"] > (
        feshbach_majorant["tail_spectral_edge"]
    )
    seeded_basis = orthonormal_channel_basis_from_seeds(
        [[1, 0, 0], [0, 1, 0]], ambient_size=3
    )
    assert seeded_basis["unitarity_residual"] < mp.mpf("1e-50")
    assert seeded_basis["core_rank"] == 2
    projector_stability = channel_projector_stability_certificate(
        mp.matrix([[3, 0, 0], [0, 1, 0], [0, 0, mp.mpf("0.2")]]),
        mp.eye(3),
        channel_rank=1,
    )
    assert projector_stability["maximum_principal_sine"] < mp.mpf("1e-50")
    assert mp.almosteq(projector_stability["actual_tail_edge"], 1)
    assert mp.almosteq(
        projector_stability["principal_angle_tail_upper_bound"], 1
    )
    assert projector_stability["actual_coupling_norm"] < mp.mpf("1e-50")
    rotated_seeded_basis = orthonormal_channel_basis_from_seeds(
        [[1, 1, 0]], ambient_size=3
    )
    rotated_stability = channel_projector_stability_certificate(
        mp.matrix([[3, 0, 0], [0, 1, 0], [0, 0, mp.mpf("0.2")]]),
        rotated_seeded_basis["full_channel_basis"],
        channel_rank=1,
    )
    assert rotated_stability["principal_angle_tail_upper_bound"] >= (
        rotated_stability["actual_tail_edge"] - mp.mpf("1e-48")
    )
    assert rotated_stability["principal_angle_coupling_upper_bound"] >= (
        rotated_stability["actual_coupling_norm"] - mp.mpf("1e-48")
    )
    forced_physical_basis = forced_physical_transverse_channel_basis(
        mp.matrix([
            [3, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, mp.mpf("0.5")],
        ]),
        transverse_seeds=[[1, -1, 0, 0], [0, 0, -1, 1]],
    )
    assert forced_physical_basis["transverse_seed_rank"] == 2
    assert forced_physical_basis["basis"]["core_rank"] == 2
    assert forced_physical_basis[
        "physical_orthogonality_residual"
    ] < mp.mpf("1e-50")
    assert forced_physical_basis[
        "transverse_normalization_residual"
    ] < mp.mpf("1e-50")
    paired_incidence = vaughan_paired_incidence_channel_certificate(
        multiscale_gauge["simplex_component_gram"]
    )
    assert paired_incidence["incidence_unitarity_residual"] < mp.mpf("1e-50")
    assert abs(paired_incidence["ratio_quadratic_residual"]) < mp.mpf("1e-47")
    assert abs(paired_incidence["fixed_line_sine_residual"]) < mp.mpf("1e-48")
    assert abs(
        paired_incidence["fixed_to_unrestricted_sine_residual"]
    ) < mp.mpf("1e-48")
    assert paired_incidence["paired_spectral_gap"] >= 0
    assert paired_incidence["coarse_leakage"] <= 1
    separated_incidence = vaughan_incidence_separated_channel_certificate(
        multiscale_gauge["simplex_component_gram"]
    )
    assert abs(separated_incidence["trace_optimality_residual"]) < (
        mp.mpf("1e-47")
    )
    assert separated_incidence["sector_orthogonality_residual"] < (
        mp.mpf("1e-50")
    )
    assert separated_incidence["basis"]["unitarity_residual"] < (
        mp.mpf("1e-50")
    )
    fixed_tilted_incidence = vaughan_incidence_separated_basis_from_ratios(
        mp.mpf("0.1"), mp.mpf(8) / 3
    )
    assert fixed_tilted_incidence["sector_orthogonality_residual"] < (
        mp.mpf("1e-50")
    )
    assert fixed_tilted_incidence["physical_inclusion_residual"] > (
        mp.mpf("0.01")
    )
    separated_angle = incidence_separated_plane_angle_certificate(
        mp.mpf("0.05"), mp.mpf(3), mp.mpf("0.08"), mp.mpf("3.2")
    )
    assert abs(separated_angle["projector_sine_residual"]) < mp.mpf("1e-48")
    assert separated_angle["formula_projector_sine"] >= (
        separated_angle["physical_coarse_line_sine"]
    )
    frozen_tilted_basis = frozen_vaughan_tilted_incidence_basis()
    assert frozen_tilted_basis["unitarity_residual"] < mp.mpf("1e-50")
    assert mp.almosteq(
        frozen_tilted_basis["relative_physical_tail_mass"],
        mp.mpf(1) / 401,
    )
    assert mp.almosteq(
        frozen_tilted_basis["relative_physical_core_mass"],
        mp.mpf(400) / 401,
    )
    assert abs(frozen_tilted_basis["physical_mass_residual"]) < (
        mp.mpf("1e-50")
    )
    frozen_channel_coefficients = frozen_vaughan_tilted_channel_coefficients(
        80, 4, 5
    )
    assert frozen_channel_coefficients["maximum_formula_residual"] < (
        mp.mpf("1e-48")
    )
    assert frozen_channel_coefficients[
        "maximum_reconstruction_residual"
    ] < mp.mpf("1e-48")
    no_free_lunch = component_projector_no_free_lunch_certificate(
        frozen_tilted_basis["core_projector"],
        [1, 1, 1, 1],
        mp.mpf(7),
    )
    assert no_free_lunch["concentration_sector"] == "core"
    assert no_free_lunch["coupling_block_norm"] < mp.mpf("1e-48")
    assert no_free_lunch["tail_block_norm"] < mp.mpf("1e-48")
    assert mp.almosteq(
        no_free_lunch["physical_energy"],
        mp.mpf(7) * frozen_tilted_basis["physical_core_mass"],
    )
    assert no_free_lunch["gram_positivity_minimum"] >= -mp.mpf("1e-48")
    physical_core_basis = orthonormal_channel_basis_from_seeds(
        [[1, 1, 1], [1, -1, 0]], ambient_size=3
    )
    physical_core_coordinates_gram = mp.matrix([
        [2, 0, mp.mpf("0.3")],
        [0, 1, 0],
        [mp.mpf("0.3"), 0, mp.mpf("0.5")],
    ])
    physical_core_coupled_gram = (
        physical_core_basis["full_channel_basis"]
        * physical_core_coordinates_gram
        * physical_core_basis["full_channel_basis"].transpose_conj()
    )
    finite_optimizer_rejected = False
    try:
        component_channel_feshbach_majorant(
            physical_core_coupled_gram,
            physical_core_basis["full_channel_basis"],
            channel_rank=2,
        )
    except ValueError as error:
        finite_optimizer_rejected = "no finite optimizer" in str(error)
    assert finite_optimizer_rejected
    physical_core_feshbach = component_channel_feshbach_majorant(
        physical_core_coupled_gram,
        physical_core_basis["full_channel_basis"],
        channel_rank=2,
        tail_threshold=mp.mpf("2"),
    )
    assert physical_core_feshbach[
        "minimum_majorant_difference_eigenvalue"
    ] >= -mp.mpf("1e-48")
    combined_stationary_certificate = zeta_abel_shared_stationary_certificate(
        horizontal_offset=mp.mpf("0.2"),
        scale=mp.mpf("2"),
        integer_cutoff=40,
        lag_start=mp.mpf("0.01"),
        lag_end=mp.mpf("4"),
        lag_cells=4,
        height_cutoff=mp.mpf("20"),
        height_cells=400,
    )
    assert combined_stationary_certificate["quadrature"]["cap_gram"] is None
    discrepancy_nodes = combined_stationary_certificate["quadrature"][
        "prime_continuum_discrepancy_lag_nodes"
    ]
    discrepancy_coefficients = combined_stationary_certificate["quadrature"][
        "prime_continuum_discrepancy_coefficients"
    ]
    assert len(discrepancy_nodes) == len(discrepancy_coefficients)
    assert all(
        abs(mp.im(coefficient)) < mp.mpf("1e-50")
        for coefficient in discrepancy_coefficients
    )
    assert any(
        mp.re(coefficient) > 0 for coefficient in discrepancy_coefficients
    )
    assert any(
        mp.re(coefficient) < 0 for coefficient in discrepancy_coefficients
    )
    assert combined_stationary_certificate[
        "certified_full_hodge_lower_bound"
    ] <= combined_stationary_certificate["sampled_stationary_minimum"]
    assert combined_stationary_certificate[
        "cauchy_defect_over_pi_lower_bound"
    ] <= combined_stationary_certificate[
        "cauchy_defect_over_pi_upper_bound"
    ]
    assert mp.almosteq(
        combined_stationary_certificate["cauchy_defect_upper_bound"],
        mp.pi
        * combined_stationary_certificate[
            "cauchy_defect_over_pi_upper_bound"
        ],
    )
    assert combined_stationary_certificate[
        "cauchy_defect_over_pi_quadratic_upper_bound"
    ] >= combined_stationary_certificate[
        "cauchy_defect_over_pi_lower_bound"
    ]
    assert combined_stationary_certificate["moments"][
        "cauchy_second_moment"
    ] >= 0
    shared_energy_certificate = zeta_abel_shared_cauchy_energy_certificate(
        horizontal_offset=mp.mpf("0.2"),
        scale=mp.mpf("2"),
        integer_cutoff=40,
        lag_start=mp.mpf("0.01"),
        lag_end=mp.mpf("4"),
        lag_cells=4,
    )
    assert shared_energy_certificate["quadrature"]["cap_gram"] is None
    assert shared_energy_certificate[
        "cauchy_defect_over_pi_quadratic_upper_bound"
    ] >= 0
    assert mp.almosteq(
        shared_energy_certificate[
            "cauchy_defect_over_pi_quadratic_upper_bound"
        ],
        combined_stationary_certificate[
            "cauchy_defect_over_pi_quadratic_upper_bound"
        ],
    )
    cofinal_schedule_near = abel_shared_cofinal_discretization_schedule(
        mp.mpf("10")
    )
    cofinal_schedule_far = abel_shared_cofinal_discretization_schedule(
        mp.mpf("100")
    )
    assert cofinal_schedule_far["horizontal_offset"] < (
        cofinal_schedule_near["horizontal_offset"]
    )
    assert cofinal_schedule_far["lag_modulus_upper"] < (
        cofinal_schedule_near["lag_modulus_upper"]
    )
    assert cofinal_schedule_far["cauchy_height_tail_mass"] < (
        cofinal_schedule_near["cauchy_height_tail_mass"]
    )
    zero_wave_certificate = single_abel_zero_wave_half_period_certificate(
        horizontal_displacement=mp.mpf("0.2"),
        horizontal_offset=mp.mpf("0.02"),
        ordinate=mp.mpf("14"),
        scale=mp.exp(200),
        multiplicity=1,
        relative_remainder_bound=mp.mpf("0.01"),
    )
    assert zero_wave_certificate["has_positive_certificate"]
    exponent = zero_wave_certificate["residue_exponent"]
    logarithm = zero_wave_certificate["log_scale"]
    ordinate = zero_wave_certificate["ordinate"]
    phase_left = zero_wave_certificate["phase_left"]
    phase_right = zero_wave_certificate["phase_right"]
    normalized_model_defect = mp.quad(
        lambda phase: max(
            mp.mpf("0"),
            -mp.re(
                mp.gamma(exponent - 1j * phase / logarithm)
                * mp.exp(-1j * phase)
            ),
        )
        / (
            logarithm
            * (1 + (ordinate + phase / logarithm) ** 2)
        ),
        [phase_left, phase_right],
    )
    assert normalized_model_defect >= zero_wave_certificate[
        "normalized_cauchy_defect_lower_bound"
    ]
    gamma_translate_gram = gamma_translate_l2_gram(
        mp.mpf("0.3"),
        [mp.mpf("-2"), mp.mpf("0.5"), mp.mpf("4")],
    )
    gamma_translate_eigenvalues = mp.eighe(
        gamma_translate_gram, eigvals_only=True
    )
    assert min(gamma_translate_eigenvalues) > 0
    expected_gamma_translate_norm = (
        2 * mp.pi * mp.power(2, mp.mpf("-0.6")) * mp.gamma(mp.mpf("0.6"))
    )
    for diagonal in range(3):
        assert mp.almosteq(
            gamma_translate_gram[diagonal, diagonal],
            expected_gamma_translate_norm,
        )
    assert max(
        abs(
            gamma_translate_gram[row, column]
            - mp.conj(gamma_translate_gram[column, row])
        )
        for row in range(3)
        for column in range(3)
    ) < mp.mpf("1e-25")
    direct_gamma_translate_inner_product = mp.quad(
        lambda height: (
            mp.gamma(mp.mpf("0.3") + 1j * (mp.mpf("-2") - height))
            * mp.conj(
                mp.gamma(
                    mp.mpf("0.3") + 1j * (mp.mpf("0.5") - height)
                )
            )
        ),
        [-mp.inf, 0, mp.inf],
    )
    assert abs(
        gamma_translate_gram[0, 1]
        - direct_gamma_translate_inner_product
    ) < mp.mpf("1e-25")
    abel_core_rank = weighted_prolate_core_rank_bound(
        mp.mpf("2"),
        max(mp.mpf("0"), abel_resonance["sampled_negative_mass"]),
        mp.mpf("0.1"),
    )
    assert abel_core_rank["core_rank_bound"] >= 0
    assert abel_core_rank["complement_negative_error_bound"] == mp.mpf(
        "0.1"
    )
    horizontal_mass = abel_coefficient_square_mass_majorant(
        mp.mpf("0.1")
    )
    assert horizontal_mass["explicit_square_mass_majorant"] < mp.mpf(
        "0.1"
    ) ** -3
    cofinal_ledger = abel_cofinal_scaling_ledger(
        mp.mpf("0.1"), mp.mpf("1e6"), mp.mpf("2")
    )
    assert mp.almosteq(
        cofinal_ledger["delta_cubed_log_height"],
        mp.mpf("1000"),
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )
    assert cofinal_ledger["balanced_complement_tolerance"] == (
        cofinal_ledger["relative_shannon_core_bound"]
    )
    cauchy_tail_near = abel_cauchy_high_tail_bound(
        mp.mpf("0.2"), mp.mpf("100"), mp.mpf("2")
    )
    cauchy_tail_far = abel_cauchy_high_tail_bound(
        mp.mpf("0.2"), mp.mpf("10000"), mp.mpf("2")
    )
    assert cauchy_tail_far["two_sided_cauchy_high_tail_bound"] < (
        cauchy_tail_near["two_sided_cauchy_high_tail_bound"]
    )
    square_root_schedule = abel_square_root_core_schedule(
        mp.mpf("100"), mp.mpf("0.2")
    )
    assert mp.almosteq(
        square_root_schedule["horizontal_margin"],
        mp.log(100) ** mp.mpf("-0.2"),
    )
    assert square_root_schedule["prime_cutoff"] >= (
        3 * 100 * mp.log(100)
    )
    assert square_root_schedule["core_height"] < (
        square_root_schedule["high_tail_start"]
    )
    assert square_root_schedule["intermediate_diagonal_trace_proxy"] > 0
    assert square_root_schedule[
        "intermediate_off_diagonal_trace_proxy"
    ] > 0
    inertia_density = weighted_hodge_inertia_density_bound(
        mp.mpf("2"),
        mp.mpf("40"),
        max(mp.mpf("0"), abel_resonance["sampled_negative_mass"]),
        mp.mpf("0.1"),
    )
    assert inertia_density["negative_inertia_bound"] == (
        abel_core_rank["negative_inertia_above_tolerance_bound"]
    )
    assert inertia_density["negative_inertia_relative_shannon_bound"] >= 0
    cyclic_leakage_near = abel_cyclic_core_leakage_bound(
        mp.mpf("0.2"),
        mp.mpf("100"),
        mp.mpf("1"),
        mp.mpf("3"),
        mp.mpf("2"),
    )
    cyclic_leakage_far = abel_cyclic_core_leakage_bound(
        mp.mpf("0.2"),
        mp.mpf("10000"),
        mp.mpf("1"),
        mp.mpf("3"),
        mp.mpf("2"),
    )
    assert cyclic_leakage_far["core_projection_norm_bound"] < (
        cyclic_leakage_near["core_projection_norm_bound"]
    )
    resolvent_leakage = abel_resolvent_core_leakage_bound(
        mp.mpf("0.2"),
        mp.mpf("100"),
        mp.mpc("0.4", "3"),
        mp.mpf("2"),
        mp.mpf("2"),
    )
    assert resolvent_leakage["decay_exponent"] == 1
    assert resolvent_leakage["dyadic_geometric_factor"] == 2
    assert resolvent_leakage["profile_constant"] > 2
    assert resolvent_leakage["profile_constant"] < 4
    weight_constant = cauchy_resolvent_weight_constant(
        mp.mpc("0.4", "0.7"), mp.mpf("2")
    )
    for sampled_height in [mp.mpf("-4"), mp.mpf("0"), mp.mpf("3")]:
        truncated_profile = abs(
            (
                1
                - mp.exp(
                    -(mp.mpc("0.4", "0.7") - 1j * sampled_height)
                    * mp.mpf("2")
                )
            )
            / (mp.mpc("0.4", "0.7") - 1j * sampled_height)
        )
        assert (1 + sampled_height**2) * truncated_profile**2 <= (
            weight_constant["cauchy_weight_constant"]
        )
    core_gram = cauchy_weighted_core_gram_bound(
        mp.mpf("0.04"),
        mp.mpf("0.2"),
        [mp.mpc("0.4", "0.7"), mp.mpc("0.8", "-0.2")],
        mp.mpf("2"),
    )
    assert mp.almosteq(
        core_gram["balanced_spectral_threshold"], mp.mpf("0.2")
    )
    assert core_gram["gram_entry_bounds"].rows == 2
    assert mp.almosteq(
        core_gram["gram_entry_bounds"][0, 1],
        core_gram["gram_entry_bounds"][1, 0],
    )

    # Divisibility incidence is the finite global Dirichlet differential;
    # for zeta its exact inverse column is the Mobius function.
    incidence_size = 10
    zeta_coefficients = [mp.mpf(0)] + [mp.mpf(1)] * incidence_size
    zeta_incidence = dirichlet_convolution_matrix(zeta_coefficients)
    mobius_coefficients = dirichlet_inverse_coefficients(zeta_coefficients)
    expected_mobius = [0, 1, -1, -1, 0, -1, 1, -1, 0, 0, 1]
    assert all(
        mp.almosteq(actual, expected)
        for actual, expected in zip(mobius_coefficients, expected_mobius)
    )
    mobius_incidence = dirichlet_convolution_matrix(mobius_coefficients)
    incidence_identity = zeta_incidence * mobius_incidence
    assert max(
        abs(incidence_identity[row, column] - (row == column))
        for row in range(incidence_size)
        for column in range(incidence_size)
    ) < mp.mpf("1e-50")
    incidence_kernel = dirichlet_incidence_hodge_kernel(zeta_coefficients)
    incidence_energy = dirichlet_incidence_hodge_energy(zeta_coefficients)
    assert mp.almosteq(
        incidence_kernel[0, 0],
        incidence_energy,
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )
    assert mp.almosteq(
        incidence_energy,
        abs(mp.fsum(expected_mobius[1:])) ** 2 / incidence_size,
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )

    # Finite Nyman--Beurling packets are ordinary positive Gram/Schur
    # problems.  The Schur complement equals the direct least-squares error.
    beurling_points = [
        mp.mpf(value)
        for value in ("0.07", "0.11", "0.16", "0.23", "0.34", "0.50", "0.75", "1.1", "1.6", "2.2")
    ]
    beurling_weights = [mp.mpf("0.1")] * len(beurling_points)
    beurling_data = sampled_beurling_hodge_data(
        [1, 2, 3], beurling_points, beurling_weights
    )
    beurling_coefficients = (
        beurling_data["gram"] ** -1
    ) * beurling_data["coupling"]
    beurling_residual = (
        beurling_data["target"]
        - beurling_data["features"] * beurling_coefficients
    )
    direct_beurling_distance = mp.re(
        (
            beurling_residual.transpose_conj()
            * beurling_data["weights"]
            * beurling_residual
        )[0, 0]
    )
    assert mp.almosteq(
        direct_beurling_distance,
        beurling_data["distance_squared"],
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )
    assert beurling_fractional_feature(2, mp.mpf("2")) == mp.mpf("0.25")
    two_feature_distance = sampled_beurling_hodge_data(
        [1, 2], beurling_points, beurling_weights
    )["distance_squared"]
    assert beurling_data["distance_squared"] <= two_feature_distance
    normalized_gram, normalized_coupling = normalize_beurling_gram_data(
        beurling_data["gram"], beurling_data["coupling"], [1, 2, 3]
    )
    assert mp.almosteq(
        positive_gram_schur_distance(
            normalized_gram,
            normalized_coupling,
            beurling_data["target_norm_squared"],
        ),
        beurling_data["distance_squared"],
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )
    beurling_feshbach = positive_gram_feshbach_distance(
        normalized_gram,
        normalized_coupling,
        beurling_data["target_norm_squared"],
        1,
    )
    assert mp.almosteq(
        beurling_feshbach["distance_squared"],
        beurling_data["distance_squared"],
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )
    assert mp.almosteq(
        beurling_target_coupling(1), 1 - mp.euler
    )
    assert mp.almosteq(
        beurling_feature_norm_squared(1), mp.log(2 * mp.pi) - mp.euler
    )

    # Linear logarithmic Möbius smoothing turns the complete low
    # convolution defect exactly into Lambda(m)/log(N).
    mollifier_size = 30
    linear_mollifier = polynomial_mobius_mollifier_coefficients(
        mollifier_size, [1, -1]
    )
    low_convolution = zeta_mollifier_low_convolution(linear_mollifier)
    assert mp.almosteq(low_convolution[1], 1)
    for integer in range(2, mollifier_size + 1):
        assert mp.almosteq(
            low_convolution[integer],
            von_mangoldt(integer) / mp.log(mollifier_size),
            rel_eps=mp.mpf("1e-50"),
            abs_eps=mp.mpf("1e-50"),
        )
    assert mobius(30) == -1
    assert mobius(12) == 0
    assert mp.almosteq(mobius_log_divisor_moment(6, 1), 0)
    assert mp.almosteq(
        mobius_log_divisor_moment(6, 2),
        2 * mp.log(2) * mp.log(3),
    )
    assert abs(mobius_log_divisor_moment(30, 2)) < mp.mpf("1e-50")
    # The Mellin residual is represented by the same finite real-space vector.
    residual_point = mp.mpf("1.7")
    direct_residual = mp.fsum(
        linear_mollifier[index]
        * beurling_fractional_feature(index, residual_point)
        for index in range(1, mollifier_size + 1)
    )
    assert mp.almosteq(
        beurling_mollifier_residual(residual_point, linear_mollifier),
        direct_residual,
    )

    # The complete low potential is exactly a Chebyshev-ratio discrepancy.
    reciprocal_point = mp.mpf("7.3")
    local_residual = beurling_mollifier_residual(
        1 / reciprocal_point, linear_mollifier
    )
    mollifier_slope = linear_mobius_mollifier_slope(mollifier_size)
    local_chebyshev_value = mp.fsum(
        von_mangoldt(integer)
        for integer in range(2, int(mp.floor(reciprocal_point)) + 1)
    )
    assert mp.almosteq(
        local_residual,
        reciprocal_point * mollifier_slope
        - local_chebyshev_value / mp.log(mollifier_size),
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )

    # Abel summation gives the normalized slope as a weighted Mertens integral.
    assert mp.almosteq(
        mp.log(mollifier_size) * mollifier_slope,
        weighted_mertens_normalized_slope(mollifier_size),
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )

    # The local energy has an exact orthogonal scalar/variance decomposition.
    local_hodge = linear_mollifier_local_hodge_decomposition(mollifier_size)
    assert local_hodge["centered_variance"] >= 0
    assert local_hodge["scalar_mismatch"] >= 0
    assert mp.almosteq(
        local_hodge["ratio_mean"],
        chebyshev_ratio_mean(mollifier_size),
    )
    assert mp.almosteq(
        local_hodge["local_energy"],
        local_hodge["piecewise_energy"],
        rel_eps=mp.mpf("1e-48"),
        abs_eps=mp.mpf("1e-48"),
    )
    assert mp.almosteq(
        beurling_mollifier_local_energy(linear_mollifier)["local_energy"],
        local_hodge["local_energy"],
        rel_eps=mp.mpf("1e-48"),
        abs_eps=mp.mpf("1e-48"),
    )

    # Reduced Farey denominators diagonalize the unweighted periodic energy.
    periodic_size = 6
    periodic_mollifier = polynomial_mobius_mollifier_coefficients(
        periodic_size, [1, -1]
    )
    periodic_fourier = beurling_periodic_fourier_energy(periodic_mollifier)
    assert mp.almosteq(reduced_denominator_density(12), mp.mpf(2) / 3)
    assert mp.almosteq(
        periodic_fourier["periodic_mean_square"],
        beurling_periodic_piecewise_energy(periodic_mollifier),
        rel_eps=mp.mpf("1e-48"),
        abs_eps=mp.mpf("1e-48"),
    )
    assert mp.almosteq(
        periodic_fourier["mean"],
        linear_mollifier_periodic_mean_via_mertens(periodic_size),
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )
    for denominator in (1, 2, 5, periodic_size):
        amplitude = mollifier_conductor_amplitude(
            periodic_mollifier, denominator
        )
        divisor_sum = periodic_fourier["divisor_sums"][denominator]
        assert mp.almosteq(amplitude, denominator * divisor_sum)
        assert abs(amplitude) <= linear_mollifier_conductor_amplitude_majorant(
            periodic_size, denominator
        ) + mp.mpf("1e-50")
    shell_diagonal = parabolic_shell_diagonal_energy(
        linear_mollifier, mollifier_size
    )
    direct_shell_mass = mp.fsum(
        beurling_periodic_fourier_energy(linear_mollifier)[
            "conductor_masses"
        ][denominator]
        for denominator in range(
            int(mp.floor(mp.sqrt(mollifier_size))) + 1,
            mollifier_size + 1,
        )
    )
    assert mp.almosteq(shell_diagonal["conductor_mass"], direct_shell_mass)
    assert mp.almosteq(
        shell_diagonal["diagonal_energy"],
        direct_shell_mass / (2 * mollifier_size),
    )
    determinant_data = farey_determinant_reduction(12, 18, 6)
    assert determinant_data["gcd"] == 6
    assert determinant_data["left_quotient"] == 2
    assert determinant_data["right_quotient"] == 3
    assert determinant_data["lcm"] == 36
    assert determinant_data["primitive_necessary"]
    assert not farey_determinant_reduction(12, 18, 5)[
        "gcd_divides_determinant"
    ]
    cotangent_correlation = generic_unrestricted_farey_harmonic_correlation(
        5, 3, 1
    )
    initial_left = cotangent_correlation["initial_left"]
    initial_right = cotangent_correlation["initial_right"]
    direct_correlation = mp.fsum(
        1
        / (
            (initial_left + 3 * parameter)
            * (initial_right + 5 * parameter)
        )
        for parameter in range(-20000, 20001)
    )
    assert abs(
        direct_correlation - cotangent_correlation["correlation"]
    ) < mp.mpf("2e-5")
    reciprocal_correlation = coprime_farey_harmonic_reciprocity(3, 5, 1)
    assert mp.almosteq(
        reciprocal_correlation["correlation"],
        cotangent_correlation["correlation"],
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )
    assert abs(reciprocal_correlation["correlation"]) <= (
        reciprocal_correlation["uniform_bound"]
    )
    cotangent_dft = finite_cotangent_dft(7, 3)
    assert mp.almosteq(
        cotangent_dft["fourier_value"],
        cotangent_dft["cotangent_value"],
        rel_eps=mp.mpf("1e-49"),
        abs_eps=mp.mpf("1e-49"),
    )
    assert mp.almosteq(
        cotangent_dft["coefficient_l2_squared"],
        cotangent_dft["coefficient_l2_squared_closed"],
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )
    paired_dft = coprime_farey_cotangent_dft(3, 5, 1)
    assert mp.almosteq(
        paired_dft["correlation"],
        reciprocal_correlation["correlation"],
        rel_eps=mp.mpf("1e-49"),
        abs_eps=mp.mpf("1e-49"),
    )
    product_modulus_dft = coprime_farey_product_modulus_dft(3, 5, 1)
    assert mp.almosteq(
        product_modulus_dft["correlation"],
        reciprocal_correlation["correlation"],
        rel_eps=mp.mpf("1e-48"),
        abs_eps=mp.mpf("1e-48"),
    )
    assert product_modulus_dft["lifted_residue"] == 6
    negative_determinant_dft = coprime_farey_product_modulus_dft(
        3, 5, -1
    )
    assert mp.almosteq(
        negative_determinant_dft["correlation"],
        reciprocal_correlation["correlation"],
        rel_eps=mp.mpf("1e-48"),
        abs_eps=mp.mpf("1e-48"),
    )
    assert euler_totient(1) == 1
    assert euler_totient(30) == 8
    for denominator in (5, 7, 10):
        mellin_data = linear_conductor_mellin_data(
            mollifier_size, denominator
        )
        assert mp.almosteq(
            mellin_data["amplitude"],
            mollifier_conductor_amplitude(
                linear_mollifier, denominator
            ),
            rel_eps=mp.mpf("1e-49"),
            abs_eps=mp.mpf("1e-49"),
        )
        assert mp.almosteq(
            mellin_data["amplitude"],
            mellin_data["zero_residue_main_term"]
            + mellin_data["contour_remainder"],
            rel_eps=mp.mpf("1e-50"),
            abs_eps=mp.mpf("1e-50"),
        )
    endpoint_data = linear_conductor_mellin_data(
        mollifier_size, mollifier_size - 1
    )
    assert endpoint_data["endpoint_one_term"]
    assert mp.almosteq(
        endpoint_data["reciprocal_log_sum"],
        mp.log(mp.mpf(mollifier_size) / (mollifier_size - 1)),
    )
    riesz_argument = mp.mpf("11.3")
    assert mp.almosteq(
        coprime_mobius_logarithmic_riesz_sum(riesz_argument, 30),
        local_smooth_convolution_riesz_sum(riesz_argument, 30),
        rel_eps=mp.mpf("1e-49"),
        abs_eps=mp.mpf("1e-49"),
    )
    for power in (1, 2, 3):
        direct_moment = coprime_mobius_logarithmic_riesz_moment(
            riesz_argument, 30, power
        )
        convolution_moment = local_smooth_convolution_riesz_moment(
            riesz_argument, 30, power
        )
        assert mp.almosteq(
            direct_moment,
            convolution_moment,
            rel_eps=mp.mpf("1e-49"),
            abs_eps=mp.mpf("1e-49"),
        )
        if power == 1:
            assert mp.almosteq(
                mobius_logarithmic_riesz_moment(
                    riesz_argument, power
                ),
                mobius_logarithmic_riesz_sum(riesz_argument),
                rel_eps=mp.mpf("1e-50"),
                abs_eps=mp.mpf("1e-50"),
            )
    polynomial = [mp.mpf(1), mp.mpf(2), mp.mpf(-3)]
    polynomial_riesz = endpoint_polynomial_riesz_data(polynomial)
    assert polynomial_riesz["endpoint_coefficients"] == [
        mp.mpf(0),
        mp.mpf(4),
        mp.mpf(-3),
    ]
    assert polynomial_riesz["riesz_norm"] == 10
    polynomial_mollifier = polynomial_mobius_mollifier_coefficients(
        mollifier_size, polynomial
    )
    for denominator in (5, 7, 10):
        assert mp.almosteq(
            polynomial_conductor_amplitude_via_riesz(
                mollifier_size, denominator, polynomial
            ),
            mollifier_conductor_amplitude(
                polynomial_mollifier, denominator
            ),
            rel_eps=mp.mpf("1e-49"),
            abs_eps=mp.mpf("1e-49"),
        )
    transform = endpoint_direction_riesz_transform(2)
    assert transform == mp.matrix([[1, 1], [-1, -2], [0, 1]])
    leverage_metric = mp.matrix(
        [[mp.mpf("3"), mp.mpf("0.4")], [mp.mpf("0.4"), mp.mpf("2")]]
    )
    leverage_response = mp.matrix([mp.mpf("0.7"), mp.mpf("-0.5")])
    leverage_coupling = mp.matrix([mp.mpf("0.3"), mp.mpf("-0.2")])
    leverage_target = mp.mpf("-0.8")
    leverage = endpoint_riesz_projection_certificate(
        leverage_metric,
        leverage_response,
        leverage_target,
        leverage_coupling,
    )
    leverage_polynomial = [
        mp.mpf(1),
        -1 + leverage["alphas"][0],
        leverage["alphas"][1] - leverage["alphas"][0],
        -leverage["alphas"][1],
    ]
    leverage_endpoint = endpoint_polynomial_riesz_data(
        leverage_polynomial
    )
    assert all(
        mp.almosteq(
            leverage["endpoint_coefficients"][row],
            leverage_endpoint["endpoint_coefficients"][row + 1],
            rel_eps=mp.mpf("1e-49"),
            abs_eps=mp.mpf("1e-49"),
        )
        for row in range(3)
    )
    assert leverage["exact_riesz_norm"] <= (
        leverage["triangle_upper_bound"] + mp.mpf("1e-49")
    )
    assert leverage["response_leverage"] <= (
        leverage["response_leverage_energy_upper"] + mp.mpf("1e-49")
    )
    no_go_scale = mp.mpf("1e-6")
    no_go = endpoint_riesz_projection_certificate(
        mp.matrix([[no_go_scale**2]]),
        mp.matrix([no_go_scale]),
        mp.mpf(1),
    )
    assert mp.almosteq(no_go["capacity"], 1)
    assert mp.almosteq(no_go["correction_energy"], 1)
    assert no_go["exact_riesz_norm"] > mp.mpf("1e6")
    local_jets = mobius_endpoint_direction_local_gram(
        mollifier_size, 2
    )
    local_eigenvalues = mp.eigsy(
        local_jets["metric"], eigvals_only=True
    )
    assert local_eigenvalues[0] > 0
    split_local = mobius_endpoint_direction_spatial_gram(
        mollifier_size, 2, 0, 10
    )["metric"] + mobius_endpoint_direction_spatial_gram(
        mollifier_size, 2, 10, mollifier_size
    )["metric"]
    assert all(
        mp.almosteq(
            split_local[row, column],
            local_jets["metric"][row, column],
            rel_eps=mp.mpf("1e-48"),
            abs_eps=mp.mpf("1e-48"),
        )
        for row in range(2)
        for column in range(2)
    )
    local_test_alphas = mp.matrix([mp.mpf("0.3"), mp.mpf("-0.2")])
    combined_direction = [mp.mpf("0")] * (mollifier_size + 1)
    for offset, direction in enumerate(local_jets["directions"]):
        for integer in range(1, mollifier_size + 1):
            combined_direction[integer] += (
                local_test_alphas[offset] * direction[integer]
            )
    negative_direction = [-value for value in combined_direction]
    zero_direction = [mp.mpf("0")] * (mollifier_size + 1)
    pure_local_energy = (
        beurling_mollifier_local_energy(combined_direction)["local_energy"]
        + beurling_mollifier_local_energy(negative_direction)["local_energy"]
    ) / 2 - beurling_mollifier_local_energy(zero_direction)["local_energy"]
    gram_local_energy = mp.re(
        (
            local_test_alphas.transpose_conj()
            * local_jets["metric"]
            * local_test_alphas
        )[0, 0]
    )
    assert mp.almosteq(
        pure_local_energy,
        gram_local_energy,
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    localized = localized_endpoint_riesz_leverage_certificate(
        mp.matrix(
            [[mp.mpf("2"), mp.mpf("0.2")], [mp.mpf("0.2"), mp.mpf("1.5")]]
        ),
        mp.matrix(
            [[mp.mpf("0.3"), mp.mpf("0.1")], [mp.mpf("0.1"), mp.mpf("0.4")]]
        ),
        mp.matrix([mp.mpf("0.4"), mp.mpf("-0.3")]),
    )
    assert localized["full_response_leverage"] <= (
        localized["localized_upper_bound"] + mp.mpf("1e-49")
    )
    anchor_metric = mp.matrix(
        [[mp.mpf("2"), mp.mpf("0.2")], [mp.mpf("0.2"), mp.mpf("1.5")]]
    )
    anchor_response = mp.matrix([mp.mpf("0.4"), mp.mpf("-0.3")])
    anchor_base = endpoint_riesz_projection_certificate(
        anchor_metric, anchor_response, mp.mpf("1")
    )
    anchor_strength = mp.mpf("7")
    anchor_updated = endpoint_riesz_projection_certificate(
        anchor_metric
        + anchor_strength
        * anchor_response
        * anchor_response.transpose_conj(),
        anchor_response,
        mp.mpf("1"),
    )
    assert mp.almosteq(
        anchor_updated["response_leverage"],
        anchor_base["response_leverage"],
        rel_eps=mp.mpf("1e-49"),
        abs_eps=mp.mpf("1e-49"),
    )
    assert all(
        mp.almosteq(
            anchor_updated["alphas"][row],
            anchor_base["alphas"][row],
            rel_eps=mp.mpf("1e-49"),
            abs_eps=mp.mpf("1e-49"),
        )
        for row in range(2)
    )
    periodic_jets = mobius_endpoint_direction_periodic_gram(
        6, 2
    )
    periodic_test_alphas = mp.matrix([mp.mpf("0.3"), mp.mpf("-0.2")])
    periodic_combination = [mp.mpf("0")] * 7
    for offset, direction in enumerate(periodic_jets["directions"]):
        for integer in range(1, 7):
            periodic_combination[integer] += (
                periodic_test_alphas[offset] * direction[integer]
            )
    periodic_direct_data = beurling_periodic_fourier_energy(
        periodic_combination
    )
    periodic_direct = (
        abs(periodic_direct_data["mean"] - 1) ** 2
        + periodic_direct_data["oscillatory_energy"]
    )
    periodic_quadratic = mp.re(
        (
            periodic_test_alphas.transpose_conj()
            * periodic_jets["metric"]
            * periodic_test_alphas
        )[0, 0]
    )
    assert mp.almosteq(
        periodic_direct,
        periodic_quadratic,
        rel_eps=mp.mpf("1e-48"),
        abs_eps=mp.mpf("1e-48"),
    )
    spatial_far = nyman_endpoint_spatial_far_certificate(12, 2)
    assert spatial_far["localized"]["full_response_leverage"] <= (
        spatial_far["localized"]["localized_upper_bound"]
        + mp.mpf("1e-48")
    )
    endpoint_mass_data = endpoint_quadratic_mass(2)
    endpoint_mass_direct = (
        endpoint_direction_riesz_transform(2).transpose_conj()
        * mp.diag([1, 4, 9])
        * endpoint_direction_riesz_transform(2)
    )
    assert endpoint_mass_data["mass"] == endpoint_mass_direct
    alignment_metric = mp.matrix(
        [[mp.mpf("2"), mp.mpf("0.2")], [mp.mpf("0.2"), mp.mpf("1.5")]]
    )
    alignment_response = mp.matrix([mp.mpf("0.4"), mp.mpf("-0.3")])
    alignment = endpoint_polarization_alignment_certificate(
        alignment_metric, alignment_response
    )
    assert mp.almosteq(
        (alignment_response.transpose_conj() * alignment["metric_representative"])[0],
        1,
    )
    assert mp.almosteq(
        (alignment_response.transpose_conj() * alignment["endpoint_representative"])[0],
        1,
    )
    assert mp.almosteq(
        alignment["endpoint_norm"],
        alignment["endpoint_minimum"] + alignment["endpoint_excess"],
        rel_eps=mp.mpf("1e-48"),
        abs_eps=mp.mpf("1e-48"),
    )
    assert all(
        mp.almosteq(
            alignment["metric_representative"][row],
            alignment["endpoint_representative"][row]
            + alignment["feshbach_shift"][row],
            rel_eps=mp.mpf("1e-48"),
            abs_eps=mp.mpf("1e-48"),
        )
        for row in range(2)
    )
    assert mp.almosteq(
        alignment["endpoint_excess"],
        alignment["feshbach_endpoint_excess"],
        rel_eps=mp.mpf("1e-48"),
        abs_eps=mp.mpf("1e-48"),
    )
    assert alignment["exact_response_leverage_l1"] <= (
        alignment["response_leverage_l1_upper"] + mp.mpf("1e-48")
    )
    perfectly_aligned = endpoint_polarization_alignment_certificate(
        endpoint_mass_data["mass"], alignment_response
    )
    assert abs(perfectly_aligned["endpoint_excess"]) < mp.mpf("1e-48")
    assert alignment["dimensionless_excess"] <= (
        alignment["feshbach_excess_upper"] + mp.mpf("1e-48")
    )
    assert alignment["dimensionless_excess"] <= (
        alignment["feshbach_first_moment_upper"] + mp.mpf("1e-48")
    )
    spectral_excess = alignment["endpoint_capacity"] * mp.fsum(
        abs(alignment["null_spectral_forcing"][index]) ** 2
        / alignment["null_generalized_eigenvalues"][index] ** 2
        for index in range(1)
    )
    assert mp.almosteq(
        alignment["dimensionless_excess"],
        spectral_excess,
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        alignment["null_green_first_moment"],
        alignment["response_line_energy"]
        - 1 / alignment["metric_capacity"],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        alignment["shorted_forcing_green_mass"],
        alignment["response_line_energy"]
        * (
            alignment["response_line_energy"]
            * alignment["metric_capacity"]
            - 1
        ),
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        alignment["dimensionless_excess"],
        alignment["shorted_excess_prediction"],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert alignment["dimensionless_excess"] <= (
        alignment["shorted_excess_upper"] + mp.mpf("1e-48")
    )
    assert mp.almosteq(
        mp.fsum(alignment["null_endpoint_contributions"]),
        1,
        rel_eps=mp.mpf("1e-48"),
        abs_eps=mp.mpf("1e-48"),
    )
    shorting = endpoint_transversal_hodge_shorting(
        alignment_metric, alignment_response
    )
    residual_eigenvalues = mp.eigsy(
        shorting["residual_metric"], eigvals_only=True
    )
    assert abs(residual_eigenvalues[0]) < mp.mpf("1e-47")
    assert all(value >= -mp.mpf("1e-47") for value in residual_eigenvalues)
    shorted_boundary = (
        alignment["shorted_null_metric"]
        - shorting["maximal_strength"]
        * alignment["null_endpoint_mass"]
    )
    assert abs(mp.eigsy(shorted_boundary, eigvals_only=True)[0]) < mp.mpf(
        "1e-47"
    )
    beyond_shorting = (
        alignment["shorted_null_metric"]
        - (shorting["maximal_strength"] + mp.mpf("1e-10"))
        * alignment["null_endpoint_mass"]
    )
    assert mp.eigsy(beyond_shorting, eigvals_only=True)[0] < 0
    completion = endpoint_transversal_hodge_completion(
        alignment_metric,
        alignment_response,
        mp.mpf("3"),
    )
    assert completion["completed"]["dimensionless_excess"] <= (
        completion["base"]["dimensionless_excess"] + mp.mpf("1e-48")
    )
    assert mp.almosteq(
        completion["completed"]["dimensionless_excess"],
        completion["predicted_excess"],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        completion["completed_inverse_capacity"],
        completion["predicted_completed_inverse_capacity"],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        completion["base_inverse_capacity"],
        completion["determinant_base_inverse_capacity"],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        completion["completed_inverse_capacity"],
        completion["determinant_completed_inverse_capacity"],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert completion["susceptibility_excess_lower"] <= (
        completion["base"]["dimensionless_excess"]
        + mp.mpf("1e-47")
    )
    assert completion["base"]["dimensionless_excess"] <= (
        completion["susceptibility_excess_upper"]
        + mp.mpf("1e-47")
    )
    assert mp.almosteq(
        completion["completed"]["null_spectral_forcing"][0],
        completion["base"]["null_spectral_forcing"][0],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        completion["completed"]["null_generalized_eigenvalues"][0],
        completion["base"]["null_generalized_eigenvalues"][0] + 3,
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    two_scale_susceptibility = endpoint_transversal_hodge_completion(
        alignment_metric,
        alignment_response,
        alignment["shorted_coercivity"],
    )
    assert two_scale_susceptibility["susceptibility_factor"] <= (
        2 + mp.mpf("1e-48")
    )
    assert two_scale_susceptibility[
        "susceptibility_excess_lower"
    ] <= alignment["dimensionless_excess"]
    assert alignment["dimensionless_excess"] <= (
        two_scale_susceptibility["susceptibility_excess_upper"]
        + mp.mpf("1e-47")
    )
    bidirectional_susceptibility = (
        endpoint_bidirectional_capacity_susceptibility(
            alignment_metric, alignment_response
        )
    )
    assert bidirectional_susceptibility["forward_excess_lower"] <= (
        alignment["dimensionless_excess"] + mp.mpf("1e-47")
    )
    assert alignment["dimensionless_excess"] <= (
        bidirectional_susceptibility["centered_excess_upper"]
        + mp.mpf("1e-47")
    )
    assert bidirectional_susceptibility["centered_excess_upper"] <= (
        bidirectional_susceptibility["centered_excess_factor_upper"]
        + mp.mpf("1e-47")
    )
    assert bidirectional_susceptibility["centered_factor"] <= (
        mp.mpf(4) / 3 + mp.mpf("1e-48")
    )
    assert mp.almosteq(
        1 / bidirectional_susceptibility["plus"]["metric_capacity"],
        bidirectional_susceptibility[
            "predicted_plus_inverse_capacity"
        ],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        1 / bidirectional_susceptibility["minus"]["metric_capacity"],
        bidirectional_susceptibility[
            "predicted_minus_inverse_capacity"
        ],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        1 / bidirectional_susceptibility["plus"]["metric_capacity"],
        bidirectional_susceptibility[
            "determinant_plus_inverse_capacity"
        ],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        1 / bidirectional_susceptibility["minus"]["metric_capacity"],
        bidirectional_susceptibility[
            "determinant_minus_inverse_capacity"
        ],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    scalar_completion = endpoint_transversal_hodge_completion(
        mp.matrix([[mp.mpf("2")]]),
        mp.matrix([mp.mpf("0.5")]),
        mp.mpf("3"),
    )
    assert scalar_completion["completion_metric"] == mp.matrix([[0]])
    assert scalar_completion["completed"]["dimensionless_excess"] == 0
    scalar_shorting = endpoint_transversal_hodge_shorting(
        mp.matrix([[mp.mpf("2")]]),
        mp.matrix([mp.mpf("0.5")]),
    )
    assert scalar_shorting["maximal_strength"] == mp.inf
    wedge_frame = endpoint_spatial_block_wedge_certificate(
        12, 2, 0, 144, [0, 12, 24, 48, 96, 144]
    )
    assert wedge_frame["wedge_lower_coercivity"] > 0
    assert all(
        value >= -mp.mpf("1e-47")
        for value in mp.eigsy(
            wedge_frame["projected_remainder_metric"],
            eigvals_only=True,
        )
    )
    vandermonde_recovery = mobius_cell_vandermonde_recovery_certificate(
        12, 2, [2, 3]
    )
    assert all(
        mp.almosteq(
            vandermonde_recovery["recovered_vandermonde"][row, column],
            vandermonde_recovery["expected_vandermonde"][row, column],
            rel_eps=mp.mpf("1e-47"),
            abs_eps=mp.mpf("1e-47"),
        )
        for row in range(2)
        for column in range(2)
    )
    assert vandermonde_recovery["endpoint_coercivity_lower"] > 0
    assert vandermonde_recovery["endpoint_coercivity_lower"] <= (
        vandermonde_recovery["prefix_certificate"][
            "wedge_lower_coercivity"
        ]
        + mp.mpf("1e-47")
    )
    assert vandermonde_recovery["fixed_node_asymptotic_valid"]
    assert vandermonde_recovery["endpoint_coercivity_lower"] >= (
        vandermonde_recovery["fixed_node_asymptotic_lower"]
        - mp.mpf("1e-48")
    )
    assert vandermonde_recovery["endpoint_coercivity_lower"] <= (
        vandermonde_recovery["sparse_recovery_node_upper"]
        + mp.mpf("1e-48")
    )
    assert vandermonde_recovery["endpoint_coercivity_lower"] <= (
        vandermonde_recovery["sparse_recovery_universal_upper"]
        + mp.mpf("1e-48")
    )
    cubic_vandermonde_recovery = (
        mobius_cell_vandermonde_recovery_certificate(
            30, 3, [2, 3, 5]
        )
    )
    assert all(
        mp.almosteq(
            cubic_vandermonde_recovery["recovered_vandermonde"][
                row, column
            ],
            cubic_vandermonde_recovery["expected_vandermonde"][
                row, column
            ],
            rel_eps=mp.mpf("1e-47"),
            abs_eps=mp.mpf("1e-47"),
        )
        for row in range(3)
        for column in range(3)
    )
    assert cubic_vandermonde_recovery["fixed_node_asymptotic_valid"]
    assert cubic_vandermonde_recovery["endpoint_coercivity_lower"] >= (
        cubic_vandermonde_recovery["fixed_node_asymptotic_lower"]
        - mp.mpf("1e-48")
    )
    assert cubic_vandermonde_recovery[
        "endpoint_coercivity_lower"
    ] <= (
        cubic_vandermonde_recovery[
            "sparse_recovery_universal_upper"
        ]
        + mp.mpf("1e-48")
    )
    sparse_search = mobius_sparse_recovery_search(12, 2, 6)
    assert sparse_search["certificate_count"] > 1
    assert sparse_search["best_certificate"][
        "endpoint_coercivity_lower"
    ] >= vandermonde_recovery["endpoint_coercivity_lower"]
    direct_wedge_lower = mp.matrix(
        wedge_frame["wedge_lower_metric"].rows,
        wedge_frame["wedge_lower_metric"].cols,
    )
    for wedge_vector in wedge_frame["wedge_vectors"]:
        direct_wedge_lower += (
            wedge_vector * wedge_vector.transpose_conj()
            / wedge_frame["discrete_response_energy"]
        )
    assert all(
        mp.almosteq(
            direct_wedge_lower[row, column],
            wedge_frame["wedge_lower_metric"][row, column],
            rel_eps=mp.mpf("1e-47"),
            abs_eps=mp.mpf("1e-47"),
        )
        for row in range(direct_wedge_lower.rows)
        for column in range(direct_wedge_lower.cols)
    )
    assert wedge_frame["captured_coercivity_ratio"] <= (
        1 + mp.mpf("1e-47")
    )
    assert wedge_frame["response_energy_capture_ratio"] <= (
        1 + mp.mpf("1e-47")
    )
    assert wedge_frame["determinant_trace_coercivity_lower"] <= (
        wedge_frame["wedge_lower_coercivity"] + mp.mpf("1e-47")
    )
    cauchy_binet_sum = mp.mpf("0")
    normalized_block_columns = [
        wedge_frame["block_direction_integrals"][index]
        / mp.sqrt(wedge_frame["block_measures"][index])
        for index in range(len(wedge_frame["block_measures"]))
    ]
    for left_index in range(len(normalized_block_columns)):
        for right_index in range(
            left_index + 1, len(normalized_block_columns)
        ):
            minor = mp.matrix(
                [
                    [
                        normalized_block_columns[left_index][row],
                        normalized_block_columns[right_index][row],
                    ]
                    for row in range(2)
                ]
            )
            cauchy_binet_sum += abs(mp.det(minor)) ** 2
    assert mp.almosteq(
        mp.det(wedge_frame["projected_metric"]),
        cauchy_binet_sum,
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert all(
        value >= -mp.mpf("1e-47")
        for value in wedge_frame[
            "wedge_remainder_generalized_eigenvalues"
        ]
    )
    unit_wedge_frame = endpoint_spatial_block_wedge_certificate(
        8, 2, 0, 64, list(range(65))
    )
    assert unit_wedge_frame["unit_cell_partition"]
    assert all(
        mp.almosteq(
            unit_wedge_frame["projected_remainder_metric"][row, column],
            unit_wedge_frame["unit_cell_variance_metric"][row, column],
            rel_eps=mp.mpf("1e-47"),
            abs_eps=mp.mpf("1e-47"),
        )
        for row in range(2)
        for column in range(2)
    )
    assert all(
        value >= -mp.mpf("1e-47")
        for value in mp.eigsy(
            unit_wedge_frame["unit_cell_poincare_majorant"]
            - unit_wedge_frame["unit_cell_variance_metric"],
            eigvals_only=True,
        )
    )
    projection_stability = (
        endpoint_projection_alignment_stability_certificate(
            unit_wedge_frame["spatial_data"]["metric"],
            unit_wedge_frame["projected_metric"],
            unit_wedge_frame["spatial_data"]["response"],
            unit_wedge_frame["unit_cell_poincare_majorant"],
        )
    )
    assert all(
        value >= -mp.mpf("1e-47")
        for value in projection_stability[
            "error_majorant_gap_eigenvalues"
        ]
    )
    assert projection_stability[
        "exact_square_root_excess_difference"
    ] <= (
        projection_stability["alignment_stability_radius"]
        + mp.mpf("1e-47")
    )
    assert projection_stability["actual"][
        "dimensionless_excess"
    ] <= projection_stability["actual_excess_upper"] + mp.mpf("1e-47")
    assert all(
        mp.almosteq(
            projection_stability["actual"]["metric_representative"][row],
            projection_stability["projected"][
                "metric_representative"
            ][row]
            + projection_stability["directional_shift"][row],
            rel_eps=mp.mpf("1e-47"),
            abs_eps=mp.mpf("1e-47"),
        )
        for row in range(2)
    )
    assert projection_stability[
        "exact_square_root_excess_difference"
    ] <= (
        projection_stability["directional_stability_radius"]
        + mp.mpf("1e-47")
    )
    assert projection_stability["directional_stability_radius"] <= (
        projection_stability["directional_green_radius"]
        + mp.mpf("1e-47")
    )
    assert projection_stability["capacity_relaxation_energy"] <= (
        projection_stability["directional_green_energy"]
        + mp.mpf("1e-47")
    )
    assert projection_stability["directional_green_energy"] <= (
        (1 + projection_stability["error_relative_bound"])
        * projection_stability["capacity_relaxation_energy"]
        + mp.mpf("1e-47")
    )
    assert projection_stability["directional_stability_radius"] <= (
        projection_stability[
            "capacity_relaxation_actual_coercivity_radius"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "capacity_relaxation_actual_coercivity_radius"
    ] <= (
        projection_stability[
            "capacity_relaxation_projected_coercivity_radius"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "capacity_relaxation_projected_coercivity_radius"
    ] <= (
        projection_stability["directional_green_radius"]
        + mp.mpf("1e-47")
    )
    assert projection_stability["directional_green_energy"] <= (
        projection_stability[
            "directional_green_energy_error_schur_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "directional_green_energy_error_schur_upper"
    ] <= (
        projection_stability[
            "directional_green_energy_majorant_schur_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability["directional_green_energy"] <= (
        projection_stability[
            "directional_green_energy_error_balanced_schur_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "directional_green_energy_error_balanced_schur_upper"
    ] <= (
        projection_stability[
            "directional_green_energy_majorant_balanced_schur_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "directional_green_energy_majorant_balanced_schur_upper"
    ] <= (
        projection_stability[
            "directional_green_energy_majorant_schur_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability["directional_green_radius"] <= (
        projection_stability["directional_green_error_schur_radius"]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "directional_green_error_schur_radius"
    ] <= (
        projection_stability["directional_green_majorant_schur_radius"]
        + mp.mpf("1e-47")
    )
    assert projection_stability["directional_green_radius"] <= (
        projection_stability[
            "directional_green_error_balanced_schur_radius"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "directional_green_error_balanced_schur_radius"
    ] <= (
        projection_stability[
            "directional_green_majorant_balanced_schur_radius"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "directional_green_majorant_balanced_schur_radius"
    ] <= (
        projection_stability["directional_green_majorant_schur_radius"]
        + mp.mpf("1e-47")
    )
    assert projection_stability["actual"][
        "dimensionless_excess"
    ] <= (
        projection_stability["directional_actual_excess_upper"]
        + mp.mpf("1e-47")
    )
    assert projection_stability["actual"][
        "dimensionless_excess"
    ] <= (
        projection_stability[
            "capacity_relaxation_actual_coercivity_excess_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "capacity_relaxation_actual_coercivity_excess_upper"
    ] <= (
        projection_stability[
            "capacity_relaxation_projected_coercivity_excess_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "capacity_relaxation_projected_coercivity_excess_upper"
    ] <= (
        projection_stability["directional_green_excess_upper"]
        + mp.mpf("1e-47")
    )
    assert projection_stability["directional_actual_excess_upper"] <= (
        projection_stability["directional_green_excess_upper"]
        + mp.mpf("1e-47")
    )
    assert projection_stability["directional_green_excess_upper"] <= (
        projection_stability[
            "directional_green_error_schur_excess_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "directional_green_error_schur_excess_upper"
    ] <= (
        projection_stability[
            "directional_green_majorant_schur_excess_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "directional_green_majorant_schur_excess_upper"
    ] <= (
        projection_stability["actual_excess_upper"]
        + mp.mpf("1e-47")
    )
    assert projection_stability[
        "directional_green_majorant_balanced_schur_excess_upper"
    ] <= (
        projection_stability[
            "directional_green_majorant_schur_excess_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability["actual"][
        "dimensionless_excess"
    ] <= (
        projection_stability[
            "directional_green_majorant_balanced_schur_excess_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert projection_stability["projected_inverse_capacity"] <= (
        projection_stability["actual_inverse_capacity"]
        + mp.mpf("1e-47")
    )
    assert mp.almosteq(
        projection_stability["projected_inverse_capacity"],
        projection_stability[
            "determinant_projected_inverse_capacity"
        ],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        projection_stability["actual_inverse_capacity"],
        projection_stability["determinant_actual_inverse_capacity"],
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert projection_stability["actual_inverse_capacity"] <= (
        projection_stability["inverse_capacity_upper"]
        + mp.mpf("1e-47")
    )
    cubic_unit_wedge_frame = endpoint_spatial_block_wedge_certificate(
        8, 3, 0, 64, list(range(65))
    )
    cubic_projection_stability = (
        endpoint_projection_alignment_stability_certificate(
            cubic_unit_wedge_frame["spatial_data"]["metric"],
            cubic_unit_wedge_frame["projected_metric"],
            cubic_unit_wedge_frame["spatial_data"]["response"],
            cubic_unit_wedge_frame["unit_cell_poincare_majorant"],
        )
    )
    assert cubic_projection_stability["actual"][
        "dimensionless_excess"
    ] <= (
        cubic_projection_stability["actual_excess_upper"]
        + mp.mpf("1e-47")
    )
    positive_completion_susceptibility = (
        endpoint_completion_multiamplitude_susceptibility_certificate(
            unit_wedge_frame["projected_metric"],
            unit_wedge_frame["spatial_data"]["response"],
            [mp.mpf("0.02"), mp.mpf("0.05"), mp.mpf("0.1")],
        )
    )
    assert positive_completion_susceptibility[
        "susceptibility_lower"
    ] - mp.mpf("1e-43") <= projection_stability["projected"][
        "dimensionless_excess"
    ] <= positive_completion_susceptibility[
        "susceptibility_upper"
    ] + mp.mpf("1e-43")
    assert (
        positive_completion_susceptibility["susceptibility_upper"]
        - positive_completion_susceptibility["susceptibility_lower"]
    ) <= (
        positive_completion_susceptibility["relative_width_upper"]
        * projection_stability["projected"]["dimensionless_excess"]
        + mp.mpf("1e-43")
    )
    assert all(
        mp.almosteq(
            sample["completed_inverse_capacity"],
            sample["determinant_completed_inverse_capacity"],
            rel_eps=mp.mpf("1e-43"),
            abs_eps=mp.mpf("1e-43"),
        )
        for sample in positive_completion_susceptibility[
            "completion_samples"
        ]
    )
    polyhedral_riesz = endpoint_polyhedral_riesz_determinant_certificate(
        unit_wedge_frame["spatial_data"]["metric"],
        unit_wedge_frame["spatial_data"]["response"],
    )
    assert mp.almosteq(
        polyhedral_riesz["determinant_polyhedral_leverage"],
        polyhedral_riesz["exact_response_leverage_l1"],
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    assert polyhedral_riesz["exact_response_leverage_l1"] <= (
        polyhedral_riesz["quadratic_response_leverage_upper"]
        + mp.mpf("1e-43")
    )
    assert all(
        mp.almosteq(
            record["plus_capacity"],
            record["determinant_plus_capacity"],
            rel_eps=mp.mpf("1e-42"),
            abs_eps=mp.mpf("1e-42"),
        )
        and mp.almosteq(
            record["minus_capacity"],
            record["determinant_minus_capacity"],
            rel_eps=mp.mpf("1e-42"),
            abs_eps=mp.mpf("1e-42"),
        )
        for record in polyhedral_riesz["phase_records"]
    )
    alternating_external = endpoint_alternating_external_phase_certificate(
        unit_wedge_frame["spatial_data"]["metric"],
        unit_wedge_frame["spatial_data"]["response"],
    )
    assert mp.almosteq(
        alternating_external["alternating_phase"],
        alternating_external["direct_alternating_phase"],
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    assert mp.almosteq(
        alternating_external["sign_defect"],
        alternating_external["predicted_sign_defect"],
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    assert mp.almosteq(
        alternating_external["exact_weighted_l1"],
        abs(alternating_external["external_derivative"])
        + alternating_external["sign_defect"],
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    assert all(
        mp.almosteq(
            alternating_external["alternating_probe"][index],
            alternating_external["external_probe_expected"][index],
            rel_eps=mp.mpf("1e-45"),
            abs_eps=mp.mpf("1e-45"),
        )
        for index in range(2)
    )
    external_capacity_loss = (
        endpoint_external_period_capacity_loss_certificate(
            unit_wedge_frame["spatial_data"]["metric"],
            unit_wedge_frame["spatial_data"]["response"],
            amplitude=mp.mpf("0.7"),
        )
    )
    assert mp.almosteq(
        external_capacity_loss["updated_probe_capacity"],
        external_capacity_loss["predicted_updated_probe_capacity"],
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    assert all(
        mp.almosteq(
            external_capacity_loss[key],
            external_capacity_loss["direct_external_leverage"],
            rel_eps=mp.mpf("1e-42"),
            abs_eps=mp.mpf("1e-42"),
        )
        for key in [
            "external_leverage_from_finite_loss",
            "external_leverage_from_schur_loss",
        ]
    )
    assert mp.almosteq(
        external_capacity_loss["determinant_response_capacity"],
        external_capacity_loss["response_capacity"],
        rel_eps=mp.mpf("1e-42"),
        abs_eps=mp.mpf("1e-42"),
    )
    assert mp.almosteq(
        external_capacity_loss["determinant_probe_capacity"],
        external_capacity_loss["probe_capacity"],
        rel_eps=mp.mpf("1e-42"),
        abs_eps=mp.mpf("1e-42"),
    )
    assert mp.almosteq(
        external_capacity_loss["determinant_updated_probe_capacity"],
        external_capacity_loss["updated_probe_capacity"],
        rel_eps=mp.mpf("1e-42"),
        abs_eps=mp.mpf("1e-42"),
    )
    assert external_capacity_loss["correlation_fraction"] <= (
        1 + mp.mpf("1e-43")
    )
    assert external_capacity_loss["dual_capacity_gram_determinant"] >= (
        -mp.mpf("1e-43")
    )
    dyadic_external_overlap = (
        mobius_endpoint_external_dyadic_overlap_certificate(
            8, 2, right_endpoint=64
        )
    )
    overlap = dyadic_external_overlap["overlap"]
    assert all(
        abs(overlap["observation_metric_residual"][row, column])
        <= mp.mpf("1e-43")
        for row in range(2)
        for column in range(2)
    )
    assert mp.almosteq(
        mp.fsum(
            record["response_mass"]
            for record in overlap["block_records"]
        ),
        1,
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    assert mp.almosteq(
        mp.fsum(
            record["probe_mass"]
            for record in overlap["block_records"]
        ),
        1,
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    assert mp.almosteq(
        mp.fsum(
            record["block_current"]
            for record in overlap["block_records"]
        ),
        overlap["mixed_capacity"],
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    assert overlap["correlation_fraction"] <= (
        overlap["local_coherence_correlation_upper"]
        + mp.mpf("1e-43")
    )
    assert overlap["local_coherence_correlation_upper"] <= (
        overlap["overlap_correlation_upper"] + mp.mpf("1e-43")
    )
    assert overlap["external_leverage"] <= (
        overlap["local_coherence_external_leverage_upper"]
        + mp.mpf("1e-43")
    )
    assert overlap["local_coherence_external_leverage_upper"] <= (
        overlap["overlap_external_leverage_upper"]
        + mp.mpf("1e-43")
    )
    assert all(
        record["local_correlation_fraction"]
        <= 1 + mp.mpf("1e-43")
        for record in overlap["block_records"]
    )
    conductor_overlap = (
        mobius_endpoint_periodic_conductor_overlap_certificate(8, 2)
    )
    conductor = conductor_overlap["overlap"]
    assert all(
        abs(conductor["observation_metric_residual"][row, column])
        <= mp.mpf("1e-43")
        for row in range(2)
        for column in range(2)
    )
    assert conductor["correlation_fraction"] <= (
        conductor["local_coherence_correlation_upper"]
        + mp.mpf("1e-43")
    )
    assert conductor["local_coherence_correlation_upper"] <= (
        conductor["overlap_correlation_upper"] + mp.mpf("1e-43")
    )
    conductor_gap = mobius_endpoint_conductor_completion_gap_certificate(
        8, 2
    )
    assert conductor_gap["relative_spatial_minimum"] > 0
    assert conductor_gap["relative_spatial_maximum"] >= (
        conductor_gap["relative_spatial_minimum"]
    )
    assert mp.almosteq(
        conductor_gap["available_relative_error"],
        1 / conductor_gap["available_to_unit_dominance_ratio"],
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    assert conductor_gap["available_to_unit_dominance_ratio"] < 1
    assert conductor_gap["available_external_transfer_radius"] >= 0
    assert conductor_gap["half_error_external_transfer_radius"] >= 0
    acyclic_completion = acyclic_completion_superdeterminant_certificate(
        unit_wedge_frame["spatial_data"]["metric"],
        mp.mpf("0.1") * mp.eye(2),
        unit_wedge_frame["spatial_data"]["response"],
        external_capacity_loss["probe"],
    )
    assert mp.almosteq(
        acyclic_completion["superdeterminant_ratio"],
        1,
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    for base_key, reconstructed_key in [
        (
            "base_response_capacity",
            "reconstructed_super_response_capacity",
        ),
        (
            "base_probe_capacity",
            "reconstructed_super_probe_capacity",
        ),
        (
            "base_mixed_capacity",
            "reconstructed_super_mixed_capacity",
        ),
    ]:
        assert mp.almosteq(
            acyclic_completion[base_key],
            acyclic_completion[reconstructed_key],
            rel_eps=mp.mpf("1e-42"),
            abs_eps=mp.mpf("1e-42"),
        )
    assert mp.almosteq(
        acyclic_completion["base_response_capacity"]
        - acyclic_completion["even_response_capacity"],
        acyclic_completion["response_capacity_loss"],
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    assert mp.almosteq(
        acyclic_completion["base_probe_capacity"]
        - acyclic_completion["even_probe_capacity"],
        acyclic_completion["probe_capacity_loss"],
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    primitive_residual = primitive_residual_superdeterminant_certificate(
        unit_wedge_frame["spatial_data"]["metric"],
        mp.matrix([[mp.mpf("0.1")], [mp.mpf("0.2")]]),
        mp.matrix([[mp.mpf("0.3")], [mp.mpf("-0.1")]]),
        unit_wedge_frame["spatial_data"]["response"],
    )
    assert all(
        mp.almosteq(
            primitive_residual["primitive_residual_kernel"][row, column],
            primitive_residual["primitive_residual_alternative"][
                row, column
            ],
            rel_eps=mp.mpf("1e-43"),
            abs_eps=mp.mpf("1e-43"),
        )
        for row in range(1)
        for column in range(1)
    )
    assert mp.almosteq(
        primitive_residual["partially_paired_superdeterminant"],
        primitive_residual[
            "predicted_partially_paired_superdeterminant"
        ],
        rel_eps=mp.mpf("1e-42"),
        abs_eps=mp.mpf("1e-42"),
    )
    assert primitive_residual["primitive_residual_determinant"] > 1
    assert all(
        primitive_residual["primitive_residual_eigenvalues"][index]
        >= 1 - mp.mpf("1e-43")
        for index in range(
            primitive_residual[
                "primitive_residual_eigenvalues"
            ].rows
        )
    )
    assert mp.almosteq(
        primitive_residual["direct_partial_super_response_capacity"],
        primitive_residual[
            "predicted_partial_super_response_capacity"
        ],
        rel_eps=mp.mpf("1e-42"),
        abs_eps=mp.mpf("1e-42"),
    )
    mertens_regression = mobius_endpoint_mertens_regression_certificate(
        8, 2, right_endpoint=64
    )
    assert all(
        mp.almosteq(
            mertens_regression["mertens_response"][index],
            mertens_regression["spatial_data"]["response"][index],
            rel_eps=mp.mpf("1e-44"),
            abs_eps=mp.mpf("1e-44"),
        )
        and abs(mertens_regression["response_residual"][index])
        <= mp.mpf("1e-44")
        for index in range(2)
    )
    assert mp.almosteq(
        mertens_regression["regression_energy"],
        mertens_regression["metric_capacity"],
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    assert all(
        mp.almosteq(
            mertens_regression["canonical_representative"][index],
            mertens_regression["regression_representative"][index],
            rel_eps=mp.mpf("1e-43"),
            abs_eps=mp.mpf("1e-43"),
        )
        for index in range(2)
    )
    assert mp.almosteq(
        mertens_regression["polyhedral_regression_leverage"],
        mertens_regression["exact_response_leverage_l1"],
        rel_eps=mp.mpf("1e-42"),
        abs_eps=mp.mpf("1e-42"),
    )
    assert all(
        mp.almosteq(
            record["phase_mixed_numerator"],
            record["direct_mixed_numerator"],
            rel_eps=mp.mpf("1e-43"),
            abs_eps=mp.mpf("1e-43"),
        )
        and mp.almosteq(
            mp.fsum(
                shell["contribution"]
                for shell in record["shell_records"]
            ),
            record["phase_mixed_numerator"],
            rel_eps=mp.mpf("1e-43"),
            abs_eps=mp.mpf("1e-43"),
        )
        and record["shell_cancellation_ratio"] <= 1
        + mp.mpf("1e-43")
        for record in mertens_regression["phase_records"]
    )
    sparse_observation_flow = (
        mobius_endpoint_sparse_observation_flow_certificate(
            8, 2, prefix_endpoint=3, right_endpoint=64
        )
    )
    assert all(
        abs(
            sparse_observation_flow["observation_metric_residual"][
                row, column
            ]
        )
        <= mp.mpf("1e-43")
        for row in range(2)
        for column in range(2)
    )
    assert mp.almosteq(
        sparse_observation_flow["response_flow_energy"],
        sparse_observation_flow["mertens_data"]["metric_capacity"],
        rel_eps=mp.mpf("1e-43"),
        abs_eps=mp.mpf("1e-43"),
    )
    assert all(
        all(
            abs(record["sparse_constraint_residual"][index])
            <= mp.mpf("1e-43")
            for index in range(2)
        )
        and mp.almosteq(
            record["sparse_mixed_numerator"],
            record["direct_mixed_numerator"],
            rel_eps=mp.mpf("1e-42"),
            abs_eps=mp.mpf("1e-42"),
        )
        and mp.almosteq(
            record["sparse_mixed_numerator"],
            record["mertens_mixed_numerator"],
            rel_eps=mp.mpf("1e-42"),
            abs_eps=mp.mpf("1e-42"),
        )
        and record["sparse_to_minimal_energy_ratio"]
        >= 1 - mp.mpf("1e-42")
        and mp.almosteq(
            record["minimal_flow_norm_squared"],
            record["direct_minimal_flow_norm_squared"],
            rel_eps=mp.mpf("1e-42"),
            abs_eps=mp.mpf("1e-42"),
        )
        for record in sparse_observation_flow["phase_records"]
    )
    interpolation_period = (
        mobius_endpoint_interpolation_period_certificate(
            8, 2, [2, 3], right_endpoint=64
        )
    )
    assert mp.almosteq(
        interpolation_period["maximal_phase_leverage"],
        interpolation_period["exact_response_leverage_l1"],
        rel_eps=mp.mpf("1e-42"),
        abs_eps=mp.mpf("1e-42"),
    )
    assert all(
        mp.almosteq(
            record["normalized_interpolation_period"],
            record["direct_normalized_period"],
            rel_eps=mp.mpf("1e-43"),
            abs_eps=mp.mpf("1e-43"),
        )
        and mp.almosteq(
            interpolation_period["metric_capacity"]
            * record["normalized_interpolation_period"],
            record["mertens_mixed_numerator"],
            rel_eps=mp.mpf("1e-41"),
            abs_eps=mp.mpf("1e-41"),
        )
        and mp.almosteq(
            record["incidence_mixed_numerator"],
            record["mertens_mixed_numerator"],
            rel_eps=mp.mpf("1e-41"),
            abs_eps=mp.mpf("1e-41"),
        )
        and all(
            abs(record["incidence_constraint_residual"][index])
            <= mp.mpf("1e-42")
            for index in range(2)
        )
        and record["interpolation_coefficient_norm"]
        + mp.mpf("1e-42")
        >= record["highest_coordinate_lower"]
        and abs(record["normalized_interpolation_period"])
        <= record["interpolation_cauchy_upper"]
        + mp.mpf("1e-42")
        and record["incidence_to_prefix_minimal_energy_ratio"]
        >= 1 - mp.mpf("1e-42")
        for record in interpolation_period["phase_records"]
    )
    tail_projection = mobius_unit_cell_tail_projection_certificate(
        8, 2, 4
    )
    head_kernel = tail_projection["head_kernel_certificate"]
    assert all(
        mp.almosteq(
            head_kernel["updated_metric"][row, column],
            tail_projection["head_metric"][row, column],
            rel_eps=mp.mpf("1e-47"),
            abs_eps=mp.mpf("1e-47"),
        )
        for row in range(2)
        for column in range(2)
    )
    for predicted_key, direct_key in [
        ("predicted_updated_capacity", "direct_updated_capacity"),
        ("predicted_updated_determinant", "direct_updated_determinant"),
        (
            "predicted_updated_null_determinant",
            "direct_updated_null_determinant",
        ),
    ]:
        assert mp.almosteq(
            head_kernel[predicted_key],
            head_kernel[direct_key],
            rel_eps=mp.mpf("1e-45"),
            abs_eps=mp.mpf("1e-45"),
        )
    assert head_kernel["capacity_loss_lower"] <= (
        head_kernel["direct_capacity_loss"] + mp.mpf("1e-47")
    )
    assert head_kernel["direct_capacity_loss"] <= (
        head_kernel["capacity_loss_upper"] + mp.mpf("1e-47")
    )
    assert head_kernel["inverse_capacity_lower"] <= (
        head_kernel["direct_updated_inverse_capacity"]
        + mp.mpf("1e-47")
    )
    assert head_kernel["direct_updated_inverse_capacity"] <= (
        head_kernel["inverse_capacity_upper"] + mp.mpf("1e-47")
    )
    assert head_kernel["response_selective_ratio"] <= (
        head_kernel["relative_update_bound"] + mp.mpf("1e-47")
    )
    direct_inverse_capacity_ratio = (
        head_kernel["direct_updated_inverse_capacity"]
        * head_kernel["base_capacity"]
    )
    assert head_kernel["inverse_capacity_ratio_lower"] <= (
        direct_inverse_capacity_ratio + mp.mpf("1e-47")
    )
    assert direct_inverse_capacity_ratio <= (
        head_kernel["inverse_capacity_ratio_upper"]
        + mp.mpf("1e-47")
    )
    assert mp.almosteq(
        mp.fsum(head_kernel["response_spectral_weights"]),
        head_kernel["response_selective_ratio"],
        rel_eps=mp.mpf("1e-45"),
        abs_eps=mp.mpf("1e-45"),
    )
    amplitude_capacity = (
        positive_rank_update_amplitude_capacity_certificate(
            tail_projection["projected_metric"],
            tail_projection["frame"]["spatial_data"]["response"],
            tail_projection["head_update_columns"],
            tail_projection["head_variance_weights"],
            [mp.mpf("0"), mp.mpf("0.5"), mp.mpf("1"), mp.mpf("2")],
        )
    )
    assert all(
        mp.almosteq(
            value["predicted_capacity"],
            value["direct_capacity"],
            rel_eps=mp.mpf("1e-45"),
            abs_eps=mp.mpf("1e-45"),
        )
        for value in amplitude_capacity["values"]
    )
    assert all(
        value["response_mass_lower"] - mp.mpf("1e-45")
        <= head_kernel["response_selective_ratio"]
        <= value["response_mass_upper"] + mp.mpf("1e-45")
        for value in amplitude_capacity["values"]
    )
    assert all(
        value["response_mass_lower"] - mp.mpf("1e-45")
        <= head_kernel["response_selective_ratio"]
        <= value["response_mass_upper"] + mp.mpf("1e-45")
        for value in amplitude_capacity[
            "two_amplitude_response_mass_bounds"
        ]
    )
    multi_amplitude_bound = amplitude_capacity[
        "multi_amplitude_response_mass_bound"
    ]
    assert multi_amplitude_bound is not None
    assert multi_amplitude_bound[
        "response_mass_lower"
    ] - mp.mpf("1e-44") <= head_kernel[
        "response_selective_ratio"
    ] <= multi_amplitude_bound[
        "response_mass_upper"
    ] + mp.mpf("1e-44")
    assert (
        multi_amplitude_bound["response_mass_upper"]
        - multi_amplitude_bound["response_mass_lower"]
    ) <= (
        multi_amplitude_bound["relative_width_upper"]
        * head_kernel["response_selective_ratio"]
        + mp.mpf("1e-44")
    )
    base_alignment = endpoint_polarization_alignment_certificate(
        tail_projection["projected_metric"],
        tail_projection["frame"]["spatial_data"]["response"],
    )
    head_alignment = tail_projection["tail_stability"]["projected"]
    common_step = min(
        base_alignment["shorted_coercivity"],
        head_alignment["shorted_coercivity"],
    ) / 2
    head_susceptibility = endpoint_bidirectional_capacity_susceptibility(
        tail_projection["head_metric"],
        tail_projection["frame"]["spatial_data"]["response"],
        common_step / head_alignment["shorted_coercivity"],
    )
    diagonal_susceptibility = (
        positive_rank_update_diagonal_susceptibility_certificate(
            tail_projection["projected_metric"],
            tail_projection["frame"]["spatial_data"]["response"],
            tail_projection["head_update_columns"],
            tail_projection["head_variance_weights"],
            head_susceptibility["completion_metric"],
            common_step,
        )
    )
    assert mp.almosteq(
        diagonal_susceptibility["exact_centered_excess"],
        head_susceptibility["centered_excess_upper"],
        rel_eps=mp.mpf("1e-45"),
        abs_eps=mp.mpf("1e-45"),
    )
    assert diagonal_susceptibility[
        "diagonal_centered_excess_lower"
    ] <= (
        diagonal_susceptibility["exact_centered_excess"]
        + mp.mpf("1e-45")
    )
    assert diagonal_susceptibility["exact_centered_excess"] <= (
        diagonal_susceptibility["diagonal_centered_excess_upper"]
        + mp.mpf("1e-45")
    )
    for sign, direct_data in [
        (mp.mpf("1"), head_susceptibility["plus"]),
        (mp.mpf("-1"), head_susceptibility["minus"]),
    ]:
        compressed = positive_rank_update_response_kernel_certificate(
            tail_projection["projected_metric"]
            + sign
            * common_step
            * head_susceptibility["completion_metric"],
            tail_projection["frame"]["spatial_data"]["response"],
            tail_projection["head_update_columns"],
            tail_projection["head_variance_weights"],
        )
        assert mp.almosteq(
            compressed["predicted_updated_inverse_capacity"],
            1 / direct_data["metric_capacity"],
            rel_eps=mp.mpf("1e-45"),
            abs_eps=mp.mpf("1e-45"),
        )
        assert compressed["inverse_capacity_lower"] <= (
            compressed["direct_updated_inverse_capacity"]
            + mp.mpf("1e-45")
        )
        assert compressed["direct_updated_inverse_capacity"] <= (
            compressed["inverse_capacity_upper"] + mp.mpf("1e-45")
        )
    assert tail_projection["finite_tail_frame_bound"] <= (
        tail_projection["uniform_tail_frame_bound"]
        + mp.mpf("1e-47")
    )
    assert all(
        value >= -mp.mpf("1e-47")
        for value in mp.eigsy(
            tail_projection["tail_majorant"]
            - tail_projection["tail_error_metric"],
            eigvals_only=True,
        )
    )
    assert all(
        mp.almosteq(
            tail_projection["head_metric"][row, column]
            + tail_projection["tail_error_metric"][row, column],
            tail_projection["actual_metric"][row, column],
            rel_eps=mp.mpf("1e-47"),
            abs_eps=mp.mpf("1e-47"),
        )
        for row in range(2)
        for column in range(2)
    )
    assert tail_projection["tail_stability"]["actual"][
        "dimensionless_excess"
    ] <= (
        tail_projection["tail_stability"][
            "directional_green_majorant_balanced_schur_excess_upper"
        ]
        + mp.mpf("1e-47")
    )
    spectral_equivalence_upper = (
        1 + tail_projection["uniform_tail_frame_bound"]
    )
    assert mp.mpf("1") - mp.mpf("1e-47") <= tail_projection[
        "inverse_capacity_ratio"
    ] <= spectral_equivalence_upper + mp.mpf("1e-47")
    assert all(
        mp.mpf("1") - mp.mpf("1e-47")
        <= value
        <= spectral_equivalence_upper + mp.mpf("1e-47")
        for value in tail_projection["null_relative_eigenvalues"]
    )
    assert all(
        mp.mpf("1") - mp.mpf("1e-47")
        <= value
        <= spectral_equivalence_upper + mp.mpf("1e-47")
        for value in tail_projection["shorted_relative_eigenvalues"]
    )
    assert mp.mpf("1") - mp.mpf("1e-47") <= tail_projection[
        "null_coercivity_ratio"
    ] <= spectral_equivalence_upper + mp.mpf("1e-47")
    assert mp.mpf("1") - mp.mpf("1e-47") <= tail_projection[
        "shorted_coercivity_ratio"
    ] <= spectral_equivalence_upper + mp.mpf("1e-47")
    assert cubic_projection_stability["actual"][
        "dimensionless_excess"
    ] <= (
        cubic_projection_stability[
            "capacity_relaxation_actual_coercivity_excess_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert cubic_projection_stability["actual"][
        "dimensionless_excess"
    ] <= (
        cubic_projection_stability[
            "directional_green_majorant_balanced_schur_excess_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert cubic_projection_stability["actual"][
        "dimensionless_excess"
    ] <= (
        cubic_projection_stability[
            "directional_green_excess_upper"
        ]
        + mp.mpf("1e-47")
    )
    assert cubic_projection_stability["actual"][
        "dimensionless_excess"
    ] <= (
        cubic_projection_stability[
            "directional_green_majorant_schur_excess_upper"
        ]
        + mp.mpf("1e-47")
    )
    shell_coercivity = endpoint_spatial_shell_coercivity(
        12, 2, [0, 12, 24, 48, 144]
    )
    direct_spatial_metric = mobius_endpoint_direction_spatial_gram(
        12, 2, 0, 144
    )["metric"]
    assert all(
        mp.almosteq(
            shell_coercivity["total_metric"][row, column],
            direct_spatial_metric[row, column],
            rel_eps=mp.mpf("1e-47"),
            abs_eps=mp.mpf("1e-47"),
        )
        for row in range(2)
        for column in range(2)
    )
    assert shell_coercivity["total_coercivity"] >= (
        shell_coercivity["additive_coercivity"] - mp.mpf("1e-48")
    )
    reconstructed_shorted = mp.matrix(
        shell_coercivity["alignment_certificate"]["shorted_null_metric"].rows,
        shell_coercivity["alignment_certificate"]["shorted_null_metric"].cols,
    )
    for shell_shorted in shell_coercivity["shell_shorted_null_metrics"]:
        reconstructed_shorted += shell_shorted
    reconstructed_shorted += shell_coercivity["shorted_dispersion_matrix"]
    assert all(
        mp.almosteq(
            reconstructed_shorted[row, column],
            shell_coercivity["alignment_certificate"][
                "shorted_null_metric"
            ][row, column],
            rel_eps=mp.mpf("1e-47"),
            abs_eps=mp.mpf("1e-47"),
        )
        for row in range(reconstructed_shorted.rows)
        for column in range(reconstructed_shorted.cols)
    )
    total_response_line_energy = mp.fsum(
        shell_coercivity["shell_response_line_energies"]
    )
    mean_coupling_slope = (
        shell_coercivity["alignment_certificate"]["null_coupling"]
        / total_response_line_energy
    )
    direct_dispersion = mp.matrix(
        reconstructed_shorted.rows, reconstructed_shorted.cols
    )
    for shell_energy, shell_coupling in zip(
        shell_coercivity["shell_response_line_energies"],
        shell_coercivity["shell_null_couplings"],
    ):
        shell_slope = shell_coupling / shell_energy
        slope_difference = shell_slope - mean_coupling_slope
        direct_dispersion += (
            shell_energy
            * slope_difference
            * slope_difference.transpose_conj()
        )
    assert all(
        mp.almosteq(
            direct_dispersion[row, column],
            shell_coercivity["shorted_dispersion_matrix"][row, column],
            rel_eps=mp.mpf("1e-47"),
            abs_eps=mp.mpf("1e-47"),
        )
        for row in range(direct_dispersion.rows)
        for column in range(direct_dispersion.cols)
    )
    assert shell_coercivity["shorted_dispersion_coercivity"] >= 0
    assert shell_coercivity["alignment_certificate"][
        "shorted_coercivity"
    ] >= (
        shell_coercivity["additive_shorted_coercivity"]
        + shell_coercivity["shorted_dispersion_coercivity"]
        - mp.mpf("1e-48")
    )
    assert mp.almosteq(
        shell_coercivity["worst_endpoint_mass"],
        1,
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        mp.fsum(shell_coercivity["worst_shell_energies"]),
        shell_coercivity["total_coercivity"],
        rel_eps=mp.mpf("1e-46"),
        abs_eps=mp.mpf("1e-46"),
    )
    assert shell_coercivity["response_leverage_l2"] <= (
        shell_coercivity["response_leverage_l2_upper"]
        + mp.mpf("1e-48")
    )
    assert shell_coercivity["response_leverage_l1"] <= (
        shell_coercivity["response_leverage_l1_upper"]
        + mp.mpf("1e-48")
    )
    assert mp.almosteq(
        shell_coercivity["spectral_capacity"],
        shell_coercivity["capacity"],
        rel_eps=mp.mpf("1e-46"),
        abs_eps=mp.mpf("1e-46"),
    )
    assert mp.almosteq(
        shell_coercivity["spectral_endpoint_l2_squared"],
        shell_coercivity["response_leverage_l2"] ** 2,
        rel_eps=mp.mpf("1e-45"),
        abs_eps=mp.mpf("1e-45"),
    )
    assert mp.almosteq(
        mp.fsum(shell_coercivity["capacity_contributions"]),
        1,
        rel_eps=mp.mpf("1e-47"),
        abs_eps=mp.mpf("1e-47"),
    )
    assert mp.almosteq(
        mp.fsum(shell_coercivity["endpoint_l2_contributions"]),
        1,
        rel_eps=mp.mpf("1e-46"),
        abs_eps=mp.mpf("1e-46"),
    )
    assert all(
        mp.almosteq(
            mp.fsum(
                shell_metric[row, column]
                for shell_metric in shell_coercivity["shell_null_metrics"]
            ),
            shell_coercivity["alignment_certificate"]["null_metric"][row, column],
            rel_eps=mp.mpf("1e-46"),
            abs_eps=mp.mpf("1e-46"),
        )
        for row in range(1)
        for column in range(1)
    )
    assert all(
        mp.almosteq(
            mp.fsum(
                coupling[row]
                for coupling in shell_coercivity["shell_null_couplings"]
            ),
            shell_coercivity["alignment_certificate"]["null_coupling"][row],
            rel_eps=mp.mpf("1e-46"),
            abs_eps=mp.mpf("1e-46"),
        )
        for row in range(1)
    )
    assert 0 <= shell_coercivity["coupling_cancellation_ratio"] <= 1
    annulus_size = 6
    annulus_metric = mobius_endpoint_direction_spatial_gram(
        annulus_size,
        2,
        annulus_size**2,
        3 * annulus_size**2,
    )["metric"]
    annulus_periodic = mobius_endpoint_direction_periodic_gram(
        annulus_size, 2
    )["metric"]
    annulus_lower_difference = (
        annulus_metric
        - annulus_periodic / (9 * annulus_size**2)
    )
    annulus_upper_difference = (
        3 * annulus_periodic / annulus_size**2
        - annulus_metric
    )
    assert mp.eigsy(annulus_lower_difference, eigvals_only=True)[0] > 0
    assert mp.eigsy(annulus_upper_difference, eigvals_only=True)[0] > 0
    sandwich = nyman_endpoint_periodic_sandwich_certificate(
        12, 2, mp.mpf(1) / 9, mp.mpf("4")
    )
    assert sandwich["upper_capacity"] <= (
        sandwich["lower_capacity"] + mp.mpf("1e-48")
    )
    assert sandwich["quadratic_response_leverage_upper"] > 0
    assert sandwich["phase_box_response_leverage_upper"] > 0
    direct_cosecant_sum = mp.fsum(
        mp.csc(mp.pi * residue / 12) ** 2
        for residue in range(1, 12)
        if math.gcd(residue, 12) == 1
    )
    assert mp.almosteq(
        reduced_cosecant_square_sum(12),
        direct_cosecant_sum,
        rel_eps=mp.mpf("1e-49"),
        abs_eps=mp.mpf("1e-49"),
    )
    shortest_row = shortest_farey_kernel_row_sum(20, 40, 7)
    assert shortest_row["actual_sum"] > 0
    assert shortest_row["actual_sum"] <= (
        shortest_row["upper_bound"] + mp.mpf("1e-49")
    )
    assert squarefree_shared_gcd_allowed_residues(2, 3, 5, 1) == []
    allowed_mod_fifteen = squarefree_shared_gcd_allowed_residues(
        15, 2, 7, 1
    )
    assert len(allowed_mod_fifteen) == (3 - 2) * (5 - 2)
    shared_correlation = squarefree_shared_gcd_primitive_correlation(
        5, 2, 3, 1
    )
    shared_direct = mp.fsum(
        1 / ((1 + 2 * parameter) * (1 + 3 * parameter))
        for parameter in range(-30000, 30001)
        if math.gcd(1 + 2 * parameter, 10) == 1
        and math.gcd(1 + 3 * parameter, 15) == 1
    )
    assert abs(
        shared_direct - shared_correlation["correlation"]
    ) < mp.mpf("2e-5")

    # A single endpoint-vanishing quadratic direction removes the boundary
    # zero mode exactly, at the cost of an explicit semiprime low current.
    corrected = mean_zero_quadratic_mobius_mollifier(mollifier_size)
    corrected_coefficients = corrected["coefficients"]
    corrected_alpha = corrected["alpha"]
    corrected_fourier = beurling_periodic_fourier_energy(
        corrected_coefficients
    )
    assert abs(corrected_fourier["mean"]) < mp.mpf("1e-50")
    assert mp.almosteq(corrected_coefficients[1], 1)
    assert abs(corrected_coefficients[mollifier_size]) < mp.mpf("1e-50")
    corrected_low = zeta_mollifier_low_convolution(corrected_coefficients)
    for integer in range(2, mollifier_size + 1):
        expected = (
            (1 - corrected_alpha)
            * von_mangoldt(integer)
            / mp.log(mollifier_size)
            - corrected_alpha
            * mobius_log_divisor_moment(integer, 2)
            / mp.log(mollifier_size) ** 2
        )
        assert mp.almosteq(
            corrected_low[integer],
            expected,
            rel_eps=mp.mpf("1e-48"),
            abs_eps=mp.mpf("1e-48"),
        )

    # Each endpoint direction has an independent exact weighted-Mertens sum.
    for power in range(1, 4):
        direct_response = mp.fsum(
            mobius(integer)
            * (mp.log(integer) / mp.log(mollifier_size)) ** power
            * (1 - mp.log(integer) / mp.log(mollifier_size))
            for integer in range(1, mollifier_size + 1)
        )
        assert mp.almosteq(
            direct_response,
            mobius_endpoint_direction_response_via_mertens(
                mollifier_size, power
            ),
            rel_eps=mp.mpf("1e-49"),
            abs_eps=mp.mpf("1e-49"),
        )

    # Multi-direction Hodge projection removes the same zero mode without
    # dividing by an arbitrarily selected scalar response.
    projected = minimum_metric_mean_zero_mobius_mollifier(
        mollifier_size, 3
    )
    projected_coefficients = projected["coefficients"]
    assert abs(1 + mp.fsum(projected_coefficients[1:]) / 2) < mp.mpf("1e-49")
    assert mp.almosteq(projected_coefficients[1], 1)
    assert abs(projected_coefficients[mollifier_size]) < mp.mpf("1e-49")
    projected_low = zeta_mollifier_low_convolution(projected_coefficients)
    projected_polynomial = projected["polynomial_coefficients"]
    for integer in range(2, mollifier_size + 1):
        expected = mp.fsum(
            projected_polynomial[degree]
            * mobius_log_divisor_moment(integer, degree)
            / mp.log(mollifier_size) ** degree
            for degree in range(1, len(projected_polynomial))
        )
        assert mp.almosteq(
            projected_low[integer],
            expected,
            rel_eps=mp.mpf("1e-47"),
            abs_eps=mp.mpf("1e-47"),
        )
    responses = projected["responses"]
    alphas = projected["alphas"]
    null_direction = mp.matrix([responses[1], -responses[0], 0])
    assert abs((responses.transpose_conj() * null_direction)[0]) < mp.mpf("1e-50")
    alternative = alphas + null_direction
    metric = projected["metric"]
    optimal_cost = mp.re((alphas.transpose_conj() * metric * alphas)[0])
    alternative_cost = mp.re(
        (alternative.transpose_conj() * metric * alternative)[0]
    )
    assert optimal_cost <= alternative_cost

    # The actual constrained Hodge problem includes coupling to the base
    # residual; its closed formula agrees with direct quadratic evaluation.
    correction_metric = mp.matrix(
        [[mp.mpf("3"), mp.mpf("0.4")], [mp.mpf("0.4"), mp.mpf("2")]]
    )
    base_coupling = mp.matrix([mp.mpf("0.3"), mp.mpf("-0.2")])
    response = mp.matrix([mp.mpf("0.7"), mp.mpf("-0.5")])
    target_response = mp.mpf("-0.8")
    constrained = constrained_hodge_projection(
        correction_metric,
        base_coupling,
        mp.mpf("1.4"),
        response,
        target_response,
    )
    assert mp.almosteq(
        (response.transpose_conj() * constrained["coefficients"])[0],
        target_response,
    )
    assert mp.almosteq(
        constrained["constrained_energy"],
        constrained["direct_energy"],
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )

    # Adding one jet increases capacity by an exact Feshbach square/gap.
    core_metric = mp.matrix(
        [[mp.mpf("2"), mp.mpf("0.2")], [mp.mpf("0.2"), mp.mpf("1.5")]]
    )
    core_response = mp.matrix([mp.mpf("0.4"), mp.mpf("-0.3")])
    new_coupling = mp.matrix([mp.mpf("0.1"), mp.mpf("0.25")])
    new_metric = mp.mpf("1.2")
    new_response = mp.mpf("0.35")
    capacity_update = nested_response_capacity_update(
        core_metric,
        core_response,
        new_coupling,
        new_metric,
        new_response,
    )
    enlarged_metric = mp.matrix(3, 3)
    for row in range(2):
        for column in range(2):
            enlarged_metric[row, column] = core_metric[row, column]
        enlarged_metric[row, 2] = new_coupling[row]
        enlarged_metric[2, row] = mp.conj(new_coupling[row])
    enlarged_metric[2, 2] = new_metric
    enlarged_response = mp.matrix(
        [core_response[0], core_response[1], new_response]
    )
    direct_capacity = mp.re(
        (
            enlarged_response.transpose_conj()
            * enlarged_metric**-1
            * enlarged_response
        )[0, 0]
    )
    assert capacity_update["capacity_increment"] >= 0
    assert mp.almosteq(
        capacity_update["enlarged_capacity"],
        direct_capacity,
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )

    constrained_update = nested_constrained_hodge_update(
        core_metric,
        mp.matrix([mp.mpf("0.15"), mp.mpf("-0.22")]),
        core_response,
        mp.mpf("1.6"),
        mp.mpf("-0.7"),
        new_metric,
        new_coupling,
        mp.mpf("0.18"),
        new_response,
    )
    enlarged_coupling = mp.matrix(
        [mp.mpf("0.15"), mp.mpf("-0.22"), mp.mpf("0.18")]
    )
    direct_enlarged_projection = constrained_hodge_projection(
        enlarged_metric,
        enlarged_coupling,
        mp.mpf("1.6"),
        enlarged_response,
        mp.mpf("-0.7"),
    )
    assert constrained_update["energy_gain"] >= 0
    assert mp.almosteq(
        constrained_update["enlarged_constrained_energy"],
        direct_enlarged_projection["constrained_energy"],
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )
    assert mp.almosteq(
        constrained_update["core_constrained_energy"]
        - constrained_update["enlarged_constrained_energy"],
        constrained_update["energy_gain"],
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )

    # Spatially restricted Hilbert norms add as PSD quadratic blocks.  The
    # easy-block optimizer plus its hard leakage is a certified upper trial.
    easy_metric = mp.matrix(
        [[mp.mpf("2.2"), mp.mpf("0.1")], [mp.mpf("0.1"), mp.mpf("1.7")]]
    )
    hard_metric = mp.matrix(
        [[mp.mpf("0.6"), mp.mpf("-0.05")], [mp.mpf("-0.05"), mp.mpf("0.8")]]
    )
    easy_coupling = mp.matrix([mp.mpf("0.2"), mp.mpf("-0.1")])
    hard_coupling = mp.matrix([mp.mpf("-0.04"), mp.mpf("0.07")])
    block_response = mp.matrix([mp.mpf("0.5"), mp.mpf("-0.35")])
    block_certificate = easy_hard_constrained_hodge_certificate(
        easy_metric,
        easy_coupling,
        mp.mpf("1.1"),
        hard_metric,
        hard_coupling,
        mp.mpf("0.4"),
        block_response,
        mp.mpf("-0.6"),
    )
    assert block_certificate["hard_leakage"] >= 0
    assert block_certificate["certificate_slack"] >= -mp.mpf("1e-50")
    assert mp.almosteq(
        block_certificate["candidate_energy"],
        quadratic_hodge_energy(
            easy_metric + hard_metric,
            easy_coupling + hard_coupling,
            mp.mpf("1.5"),
            block_certificate["coefficients"],
        ),
        rel_eps=mp.mpf("1e-50"),
        abs_eps=mp.mpf("1e-50"),
    )

    # Theorem DR: the weighted endpoint gap tends to an Exp(rate=1/2)
    # law.  For g(v)=exp(-v), its limiting mean is 1/3.  This is a
    # transcription/asymptotic diagnostic, not a directed-error proof.
    gap_errors = []
    for endpoint in (101, 1009):
        average = weighted_prime_gap_average(
            mp.log(endpoint), lambda gap: mp.e ** (-gap)
        )
        gap_errors.append(abs(average - mp.mpf(1) / 3))
    assert gap_errors[1] < gap_errors[0]

    # Theorem DV: a compactly smoothed prime sum is reconstructed from its
    # pole, nontrivial-zero, and trivial-zero residues.  Numerical zeta zeros
    # make this a sign/normalization check only.
    endpoint = 1009
    width = mp.mpf(2)

    def gap_bump(gap: mp.mpf) -> mp.mpf:
        if 0 <= gap <= width:
            return gap**4 * (width - gap) ** 4
        return mp.mpf("0")

    def gap_laplace(value: mp.mpf | mp.mpc) -> mp.mpf | mp.mpc:
        return mp.quad(
            lambda gap: gap**4
            * (width - gap) ** 4
            * mp.e ** (-value * gap),
            [0, width],
        )

    direct_gap_sum = smoothed_prime_gap_sum(endpoint, gap_bump)
    explicit_gap = zeta_smoothed_gap_explicit_approximation(
        endpoint, gap_laplace, zero_count=12, trivial_count=8
    )
    assert abs(direct_gap_sum - explicit_gap["approximation"]) < mp.mpf(
        "2e-6"
    )

    # Proposition EB: the truncated zero-frequency Gram matrix is Hermitian
    # positive semidefinite.  A shifted Laplace transform supplies a second,
    # genuinely different boundary channel.
    zero_gram = zeta_boundary_zero_gram(
        [gap_laplace, lambda value: gap_laplace(value + mp.mpf("0.3"))],
        zero_count=6,
    )
    assert abs(zero_gram[0, 1] - mp.conj(zero_gram[1, 0])) < mp.mpf(
        "1e-50"
    )
    assert mp.re(zero_gram[0, 0]) >= 0
    assert mp.re(zero_gram[1, 1]) >= 0
    assert mp.re(mp.det(zero_gram)) >= -mp.mpf("1e-50")

    abel_gram_coarse = zeta_boundary_zero_abel_gram(
        [gap_laplace, lambda value: gap_laplace(value + mp.mpf("0.3"))],
        zero_count=6,
        sigma=mp.mpf("0.5"),
    )
    abel_gram_fine = zeta_boundary_zero_abel_gram(
        [gap_laplace, lambda value: gap_laplace(value + mp.mpf("0.3"))],
        zero_count=6,
        sigma=mp.mpf("0.05"),
    )
    for abel_gram in (abel_gram_coarse, abel_gram_fine):
        assert abs(
            abel_gram[0, 1] - mp.conj(abel_gram[1, 0])
        ) < mp.mpf("1e-50")
        assert mp.re(abel_gram[0, 0]) >= 0
        assert mp.re(abel_gram[1, 1]) >= 0
        assert mp.re(mp.det(abel_gram)) >= -mp.mpf("1e-50")

    def frobenius_distance(left: mp.matrix, right: mp.matrix) -> mp.mpf:
        return mp.sqrt(
            mp.fsum(
                abs(left[row, column] - right[row, column]) ** 2
                for row in range(left.rows)
                for column in range(left.cols)
            )
        )

    assert frobenius_distance(abel_gram_fine, zero_gram) < frobenius_distance(
        abel_gram_coarse, zero_gram
    )

    # Corollary EH: the closed-form lower eigenvalue and shifted determinant
    # agree with a direct Hermitian 2x2 calculation.
    left_diagonal = mp.mpf("1.25")
    right_diagonal = mp.mpf("-0.4")
    off_diagonal = mp.mpc("0.3", "-0.7")
    boundary_block = mp.matrix(
        [
            [left_diagonal, off_diagonal],
            [mp.conj(off_diagonal), right_diagonal],
        ]
    )
    direct_boundary_values = sorted(
        (mp.re(value) for value in mp.eig(boundary_block, left=False, right=False))
    )
    assert abs(
        direct_boundary_values[0]
        - two_channel_hodge_lower_eigenvalue(
            left_diagonal, right_diagonal, off_diagonal
        )
    ) < mp.mpf("1e-50")
    boundary_shift = mp.mpf("1.1")
    assert abs(
        two_channel_schur_margin(
            left_diagonal,
            right_diagonal,
            off_diagonal,
            boundary_shift,
        )
        - mp.det(boundary_block + boundary_shift * mp.eye(2))
    ) < mp.mpf("1e-50")

    # Equation (26): the exact piecewise-power implementation agrees with
    # direct quadrature and is monotone in the arithmetic cutoff.
    chebyshev_small = chebyshev_abel_energy(13, mp.mpf("0.75"))
    chebyshev_large = chebyshev_abel_energy(101, mp.mpf("0.75"))
    psi_value = mp.mpf("0")
    chebyshev_quad = mp.mpf("0")
    for integer in range(1, 13):
        if integer >= 2:
            psi_value += von_mangoldt(integer)
        chebyshev_quad += mp.quad(
            lambda value, current=psi_value: (
                (current - value) ** 2 * value ** mp.mpf("-3.5")
            ),
            [integer, integer + 1],
        )
    chebyshev_quad *= mp.mpf("1.5")
    assert chebyshev_small >= 0
    assert chebyshev_large >= chebyshev_small
    assert abs(chebyshev_small - chebyshev_quad) < mp.mpf("1e-50")
    for sigma_value in (mp.mpf("0.25"), mp.mpf("0.5"), mp.mpf("0.75")):
        for endpoint_value in (13, 101):
            assert abs(
                chebyshev_abel_energy(endpoint_value, sigma_value)
                - chebyshev_abel_energy_dirichlet(
                    endpoint_value, sigma_value
                )
            ) < mp.mpf("1e-50")

    # Theorems EZ/FA and Proposition FD: infinite and finite Green matrices
    # are positive, the finite correction is rank one, and the trace formula
    # agrees with integrating the diagonal kernel.
    kernel_points = [mp.mpf(1), mp.mpf(2), mp.mpf(5), mp.mpf(11)]
    kernel_sigma = mp.mpf("0.4")
    infinite_kernel = max_kernel_matrix(kernel_points, kernel_sigma)
    finite_kernel = finite_max_kernel_matrix(
        kernel_points, mp.mpf(13), kernel_sigma
    )
    assert min(mp.eigsy(infinite_kernel, eigvals_only=True)) >= 0
    assert min(mp.eigsy(finite_kernel, eigvals_only=True)) >= 0
    kernel_difference = infinite_kernel - finite_kernel
    assert abs(mp.det(kernel_difference)) < mp.mpf("1e-50")
    trace_integral = mp.quad(
        lambda value: (
            2
            * kernel_sigma
            / (1 + 2 * kernel_sigma)
            * value ** (-1 - 2 * kernel_sigma)
        ),
        [1, mp.inf],
    )
    assert abs(trace_integral - max_kernel_trace(kernel_sigma)) < mp.mpf(
        "1e-50"
    )

    # Theorems FF/FJ: normalized Bessel modes have unit L2 norm, satisfy the
    # Neumann boundary condition, and their reciprocal eigenvalues sum toward
    # the Green trace.
    first_mode_norm = mp.quad(
        lambda value: abs(
            max_kernel_eigenfunction(value, 1, kernel_sigma)
        )
        ** 2,
        [1, mp.inf],
    )
    assert abs(first_mode_norm - 1) < mp.mpf("1e-45")
    boundary_order = 1 / (2 * kernel_sigma)
    boundary_zero = mp.besseljzero(boundary_order, 1)
    assert abs(mp.besselj(boundary_order, boundary_zero)) < mp.mpf("1e-45")
    inverse_trace_5 = mp.fsum(
        1 / max_kernel_eigenvalue(index, kernel_sigma)
        for index in range(1, 6)
    )
    inverse_trace_20 = mp.fsum(
        1 / max_kernel_eigenvalue(index, kernel_sigma)
        for index in range(1, 21)
    )
    exact_kernel_trace = max_kernel_trace(kernel_sigma)
    assert 0 < inverse_trace_5 < inverse_trace_20 < exact_kernel_trace

    # Proposition FN: finite Fourier--Bessel partial sums are increasing
    # lower certificates for the exact finite Chebyshev energy.
    bessel_energy = chebyshev_abel_energy(13, mp.mpf("0.75"))
    bessel_coefficients = [
        chebyshev_bessel_coefficient(13, index, mp.mpf("0.75"))
        for index in range(1, 6)
    ]
    bessel_partial_3 = 2 * mp.fsum(
        abs(value) ** 2 for value in bessel_coefficients[:3]
    )
    bessel_partial_5 = 2 * mp.fsum(
        abs(value) ** 2 for value in bessel_coefficients
    )
    assert 0 < bessel_partial_3 < bessel_partial_5 < bessel_energy
    prefix_endpoint = 13
    prefix_energy = chebyshev_prefix_hodge_energy(prefix_endpoint)
    prefix_value = mp.mpf("0")
    direct_prefix_energy = mp.mpf("0")
    prefix_charges_exact = []
    for integer in range(1, prefix_endpoint):
        charge = von_mangoldt(integer) - 1
        prefix_charges_exact.append(charge)
        prefix_value += charge
        direct_prefix_energy += prefix_value**2 / (
            mp.mpf(integer) * (integer + 1)
        )
    assert abs(prefix_energy - direct_prefix_energy) < mp.mpf("1e-50")
    assert abs(
        prefix_energy
        - power_prefix_hodge_energy(
            prefix_charges_exact,
            mp.mpf("1"),
        )
    ) < mp.mpf("1e-50")
    next_prefix_energy = chebyshev_prefix_hodge_energy(prefix_endpoint + 1)
    endpoint_prefix = mp.fsum(prefix_charges_exact) + (
        von_mangoldt(prefix_endpoint) - 1
    )
    assert abs(
        next_prefix_energy
        - prefix_energy
        - endpoint_prefix**2
        / (mp.mpf(prefix_endpoint) * (prefix_endpoint + 1))
    ) < mp.mpf("1e-50")
    block_start = 8
    block_endpoint = 16
    block_prefix_energy = chebyshev_prefix_log_block_energy(
        block_start,
        block_endpoint,
    )
    assert abs(
        block_prefix_energy
        - (
            chebyshev_prefix_hodge_energy(block_endpoint)
            - chebyshev_prefix_hodge_energy(block_start)
        )
    ) < mp.mpf("1e-50")
    step_block_variance = chebyshev_step_block_variance(
        block_start,
        block_endpoint,
    )
    assert (
        step_block_variance
        / (mp.mpf(block_endpoint - 1) * block_endpoint)
        <= block_prefix_energy
        <= step_block_variance
        / (mp.mpf(block_start) * (block_start + 1))
    )
    local_block_charges = mp.matrix(
        chebyshev_step_block_charges(block_start, block_endpoint)
    )
    local_block_size = block_endpoint - block_start
    local_green = reverse_brownian_green_kernel(local_block_size)
    local_laplacian = reverse_dirichlet_laplacian(local_block_size)
    local_green_energy = (
        local_block_charges.transpose_conj()
        * local_green
        * local_block_charges
    )[0]
    assert abs(local_green_energy - step_block_variance) < mp.mpf("1e-50")
    assert max(
        abs(
            (local_green * local_laplacian)[row, column]
            - (1 if row == column else 0)
        )
        for row in range(local_block_size)
        for column in range(local_block_size)
    ) < mp.mpf("1e-50")
    local_mean, local_scalar_energy, local_bridge_energy = (
        prefix_scalar_bridge_decomposition(list(local_block_charges))
    )
    assert abs(
        local_scalar_energy + local_bridge_energy - step_block_variance
    ) < mp.mpf("1e-50")
    local_prefix_sum = local_block_size * local_mean
    assert abs(
        local_prefix_sum
        - chebyshev_triangular_discrepancy(block_start)
        - mp.mpf(block_start) / 2
    ) < mp.mpf("1e-50")
    constant_riesz_vector = local_green[:, 0]
    scalar_green = (
        constant_riesz_vector * constant_riesz_vector.transpose_conj()
        / local_block_size
    )
    bridge_green_full = local_green - scalar_green
    assert abs(
        (
            local_block_charges.transpose_conj()
            * scalar_green
            * local_block_charges
        )[0]
        - local_scalar_energy
    ) < mp.mpf("1e-50")
    assert abs(
        (
            local_block_charges.transpose_conj()
            * bridge_green_full
            * local_block_charges
        )[0]
        - local_bridge_energy
    ) < mp.mpf("1e-50")
    assert max(
        abs(bridge_green_full[0, index])
        + abs(bridge_green_full[index, 0])
        for index in range(local_block_size)
    ) < mp.mpf("1e-50")
    bridge_green = discrete_brownian_bridge_green_kernel(local_block_size)
    bridge_laplacian = dirichlet_bridge_laplacian(local_block_size)
    assert max(
        abs(bridge_green_full[row + 1, column + 1] - bridge_green[row, column])
        for row in range(local_block_size - 1)
        for column in range(local_block_size - 1)
    ) < mp.mpf("1e-50")
    fresh_charges = mp.matrix(list(local_block_charges)[1:])
    assert abs(
        (
            fresh_charges.transpose_conj()
            * bridge_green
            * fresh_charges
        )[0]
        - local_bridge_energy
    ) < mp.mpf("1e-50")
    assert max(
        abs(
            (bridge_green * bridge_laplacian)[row, column]
            - (1 if row == column else 0)
        )
        for row in range(local_block_size - 1)
        for column in range(local_block_size - 1)
    ) < mp.mpf("1e-50")
    generic_prefix_charges = [
        mp.mpc("1.25", "0.1"),
        mp.mpc("-0.75", "0.2"),
        mp.mpc("0.5", "-0.3"),
    ]
    generic_center_exponent = mp.mpf("0.7")
    generic_prefix_energy = power_prefix_hodge_energy(
        generic_prefix_charges,
        generic_center_exponent,
    )
    generic_mean, generic_scalar, generic_bridge = (
        prefix_scalar_bridge_decomposition(generic_prefix_charges)
    )
    generic_prefix = mp.mpc("0")
    generic_unweighted_energy = mp.mpf("0")
    for generic_charge in generic_prefix_charges:
        generic_prefix += generic_charge
        generic_unweighted_energy += abs(generic_prefix) ** 2
    assert abs(
        generic_scalar + generic_bridge - generic_unweighted_energy
    ) < mp.mpf("1e-50")
    assert abs(mp.im(generic_mean)) > mp.mpf("1e-6")
    similarity = mp.matrix(
        [
            [mp.mpc("1", "0.2"), mp.mpc("0.7", "-0.1")],
            [mp.mpc("0.1", "0.3"), mp.mpc("1.2", "0")],
        ]
    )
    phase_matrix = mp.diag(
        [mp.e ** (mp.j * mp.mpf("0.37")), mp.e ** (mp.j * mp.mpf("1.11"))]
    )
    similarity_inverse = similarity**-1
    tempered_operator = similarity * phase_matrix * similarity_inverse
    exact_polarization = (
        similarity_inverse.transpose_conj() * similarity_inverse
    )
    exact_polarization_residual = polarization_similitude_residual(
        tempered_operator,
        exact_polarization,
    )
    assert max(
        abs(exact_polarization_residual[row, column])
        for row in range(2)
        for column in range(2)
    ) < mp.mpf("1e-50")
    cesaro_radius = 40
    cesaro_metric = cesaro_orbit_metric(tempered_operator, cesaro_radius)
    assert abs(cesaro_metric[0, 1] - mp.conj(cesaro_metric[1, 0])) < mp.mpf(
        "1e-50"
    )
    assert mp.re(cesaro_metric[0, 0]) > 0
    assert mp.re(mp.det(cesaro_metric)) > 0
    cesaro_residual = polarization_similitude_residual(
        tempered_operator,
        cesaro_metric,
    )
    terminal_forward = tempered_operator ** (cesaro_radius + 1)
    terminal_backward = (tempered_operator**-1) ** cesaro_radius
    telescoping_boundary = (
        terminal_forward.transpose_conj() * terminal_forward
        - terminal_backward.transpose_conj() * terminal_backward
    ) / (2 * cesaro_radius + 1)
    assert max(
        abs(cesaro_residual[row, column] - telescoping_boundary[row, column])
        for row in range(2)
        for column in range(2)
    ) < mp.mpf("1e-48")
    similitude_scale = mp.mpf("5")
    scaled_frobenius = mp.sqrt(similitude_scale) * tempered_operator
    scaled_residual = polarization_similitude_residual(
        scaled_frobenius,
        exact_polarization,
        similitude_scale,
    )
    assert max(
        abs(scaled_residual[row, column])
        for row in range(2)
        for column in range(2)
    ) < mp.mpf("1e-49")
    lyapunov_radius = 40
    radial_operator = mp.diag([mp.mpf("2"), mp.mpf("1") / 3])
    radial_metric = cesaro_orbit_metric(radial_operator, lyapunov_radius)
    radial_exponent_estimate = (
        mp.log(max(radial_metric[0, 0], radial_metric[1, 1]))
        / (2 * lyapunov_radius)
    )
    assert abs(radial_exponent_estimate - mp.log(3)) < mp.mpf("0.08")
    expanding_vector = mp.matrix([[1], [0]])
    expanding_energy = cesaro_orbit_energy(
        radial_operator,
        expanding_vector,
        lyapunov_radius,
    )
    expanding_exponent_estimate = mp.log(expanding_energy) / (
        2 * lyapunov_radius
    )
    assert abs(expanding_exponent_estimate - mp.log(2)) < mp.mpf("0.08")
    packet_gram = cesaro_orbit_gram(
        radial_operator,
        mp.eye(2),
        lyapunov_radius,
    )
    assert abs(packet_gram[0, 1] - mp.conj(packet_gram[1, 0])) < mp.mpf(
        "1e-50"
    )
    assert mp.det(packet_gram) > 0
    jordan_radius = 80
    unipotent_operator = mp.matrix([[1, 1], [0, 1]])
    unipotent_metric = cesaro_orbit_metric(
        unipotent_operator,
        jordan_radius,
    )
    jordan_polynomial_exponent = mp.log(
        max(unipotent_metric[0, 0], unipotent_metric[1, 1])
    ) / mp.log(jordan_radius)
    assert abs(jordan_polynomial_exponent - 2) < mp.mpf("0.25")
    compound_left = mp.matrix(
        [[1, 2, 0], [0, 1, 1], [1, 0, 1]]
    )
    compound_right = mp.matrix(
        [[2, 0, 1], [1, 1, 0], [0, 1, 1]]
    )
    exterior_degree = 2
    compound_product = exterior_power_matrix(
        compound_left * compound_right,
        exterior_degree,
    )
    factored_compound = exterior_power_matrix(
        compound_left,
        exterior_degree,
    ) * exterior_power_matrix(compound_right, exterior_degree)
    assert max(
        abs(compound_product[row, column] - factored_compound[row, column])
        for row in range(compound_product.rows)
        for column in range(compound_product.cols)
    ) < mp.mpf("1e-50")
    assert abs(
        mp.det(exterior_power_matrix(compound_left, exterior_degree))
        - mp.det(compound_left) ** 2
    ) < mp.mpf("1e-50")
    endpoint_power = 30
    weight_operator = mp.diag([mp.mpf("2"), mp.mpf("1"), mp.mpf("1") / 3])
    weight_metric = endpoint_orbit_metric(weight_operator, endpoint_power)
    singular_slope_estimates = sorted(
        [
            mp.log(mp.sqrt(weight_metric[index, index])) / endpoint_power
            for index in range(3)
        ],
        reverse=True,
    )
    target_slopes = [mp.log(2), mp.mpf("0"), -mp.log(3)]
    assert max(
        abs(estimate - target)
        for estimate, target in zip(singular_slope_estimates, target_slopes)
    ) < mp.mpf("1e-50")
    upper_inertia, lower_inertia = thresholded_endpoint_inertia(
        weight_operator,
        endpoint_power,
        mp.mpf("0.1"),
    )
    assert (upper_inertia, lower_inertia) == (1, 1)
    exterior_iterate = exterior_power_matrix(
        weight_operator**endpoint_power,
        2,
    )
    exterior_norm = max(
        abs(exterior_iterate[row, column])
        for row in range(exterior_iterate.rows)
        for column in range(exterior_iterate.cols)
    )
    assert abs(mp.log(exterior_norm) / endpoint_power - mp.log(2)) < mp.mpf(
        "1e-50"
    )
    multiplicity_feature = mp.matrix(
        [[mp.mpc("1", "0.2")], [mp.mpc("-0.4", "0.7")], [mp.mpc("0.3", "0")]]
    )
    atom_multiplicity = 4
    coherent_atom = coherent_scalar_spectral_atom(
        multiplicity_feature,
        atom_multiplicity,
    )
    repeated_couplings = mp.matrix(
        multiplicity_feature.rows,
        atom_multiplicity,
    )
    for channel in range(multiplicity_feature.rows):
        for copy in range(atom_multiplicity):
            repeated_couplings[channel, copy] = (
                mp.sqrt(atom_multiplicity) * multiplicity_feature[channel]
            )
    repeated_atom = spectral_atom_from_couplings(repeated_couplings)
    assert max(
        abs(coherent_atom[row, column] - repeated_atom[row, column])
        for row in range(coherent_atom.rows)
        for column in range(coherent_atom.cols)
    ) < mp.mpf("1e-50")
    coherent_eigenvalues = np.linalg.eigvalsh(
        np.array(
            [
                [complex(coherent_atom[row, column]) for column in range(3)]
                for row in range(3)
            ]
        )
    )
    assert np.count_nonzero(
        coherent_eigenvalues > 1e-12 * coherent_eigenvalues[-1]
    ) == 1
    independent_couplings = mp.matrix(
        [[1, 0, 0], [0, 2, 0], [0, 0, 3], [1, 1, 1]]
    )
    independent_atom = spectral_atom_from_couplings(independent_couplings)
    independent_eigenvalues = np.linalg.eigvalsh(
        np.array(
            [
                [
                    complex(independent_atom[row, column])
                    for column in range(independent_atom.cols)
                ]
                for row in range(independent_atom.rows)
            ]
        )
    )
    assert np.count_nonzero(
        independent_eigenvalues > 1e-12 * independent_eigenvalues[-1]
    ) == 3
    feature_norm_squared = mp.fsum(
        abs(multiplicity_feature[index]) ** 2
        for index in range(multiplicity_feature.rows)
    )
    coherent_atom_weight = mp.re(
        mp.fsum(coherent_atom[index, index] for index in range(coherent_atom.rows))
    )
    assert recover_integer_spectral_multiplicity(
        coherent_atom_weight,
        feature_norm_squared,
    ) == atom_multiplicity
    try:
        recover_integer_spectral_multiplicity(
            coherent_atom_weight * mp.mpf("1.01"),
            feature_norm_squared,
        )
    except ValueError:
        pass
    else:
        raise AssertionError("non-square atom weight must be rejected")
    tracial_points = [
        mp.mpc("0.5", "2"),
        mp.mpc("0.5", "-3"),
        mp.mpc("1", "0"),
    ]
    tracial_weights = [3, 2, -1]
    determinant_point = mp.mpc("1.7", "0.4")
    tracial_determinant = finite_tracial_spectral_determinant(
        determinant_point,
        tracial_points,
        tracial_weights,
    )
    repeated_determinant = (
        (determinant_point - tracial_points[0]) ** 3
        * (determinant_point - tracial_points[1]) ** 2
        / (determinant_point - tracial_points[2])
    )
    assert abs(tracial_determinant - repeated_determinant) < mp.mpf("1e-50")
    tracial_log_derivative = finite_tracial_log_derivative(
        determinant_point,
        tracial_points,
        tracial_weights,
    )
    derivative_step = mp.mpf("1e-20")
    numerical_log_derivative = (
        finite_tracial_spectral_determinant(
            determinant_point + derivative_step,
            tracial_points,
            tracial_weights,
        )
        - finite_tracial_spectral_determinant(
            determinant_point - derivative_step,
            tracial_points,
            tracial_weights,
        )
    ) / (2 * derivative_step * tracial_determinant)
    assert abs(numerical_log_derivative - tracial_log_derivative) < mp.mpf(
        "1e-35"
    )
    generic_size = len(generic_prefix_charges)
    generic_max_kernel_energy = mp.fsum(
        left_charge
        * mp.conj(right_charge)
        * (
            mp.mpf(max(left_index, right_index)) ** (-generic_center_exponent)
            - mp.mpf(generic_size + 1) ** (-generic_center_exponent)
        )
        / generic_center_exponent
        for left_index, left_charge in enumerate(
            generic_prefix_charges,
            start=1,
        )
        for right_index, right_charge in enumerate(
            generic_prefix_charges,
            start=1,
        )
    )
    assert abs(generic_prefix_energy - generic_max_kernel_energy) < mp.mpf(
        "1e-50"
    )
    generic_hodge_kernel = power_prefix_hodge_kernel(
        generic_size,
        generic_center_exponent,
    )
    generic_dual_laplacian = power_prefix_dual_laplacian(
        generic_size,
        generic_center_exponent,
    )
    assert max(
        abs(
            (generic_hodge_kernel * generic_dual_laplacian)[row, column]
            - (1 if row == column else 0)
        )
        for row in range(generic_size)
        for column in range(generic_size)
    ) < mp.mpf("1e-50")
    generic_charge_vector = mp.matrix(generic_prefix_charges)
    kernel_prefix_energy = (
        generic_charge_vector.transpose_conj()
        * generic_hodge_kernel
        * generic_charge_vector
    )[0]
    assert abs(kernel_prefix_energy - generic_prefix_energy) < mp.mpf("1e-50")
    generic_test_vector = mp.matrix(
        [mp.mpc("0.4", "-0.2"), mp.mpc("-0.1", "0.3"), mp.mpc("0.7", "0.1")]
    )
    dual_energy = (
        generic_test_vector.transpose_conj()
        * generic_dual_laplacian
        * generic_test_vector
    )[0]
    pairing = (
        generic_charge_vector.transpose_conj() * generic_test_vector
    )[0]
    assert abs(mp.im(dual_energy)) < mp.mpf("1e-50")
    assert abs(pairing) ** 2 <= (
        generic_prefix_energy * mp.re(dual_energy) + mp.mpf("1e-50")
    )

    graph = prime_graph_decomposition_for_function(
        lambda y: 1 + y / 3 + mp.j * y**2 / 7,
        length,
    )
    assert graph["edge_energy"] >= 0
    assert graph["degree_energy"] >= 0
    for frequency in (
        mp.mpf("0"),
        mp.mpf("0.5"),
        mp.mpf("7.25"),
    ):
        full_multiplier = canonical_weil_multiplier(frequency, length)
        phase_reconstruction = (
            archimedean_multiplier(frequency)
            - 2 * mp.re(prime_phase_sum(frequency, length))
        )
        assert abs(full_multiplier - phase_reconstruction) < mp.mpf("1e-50")
        bad_multiplier = canonical_bad_multiplier(frequency, length)
        assert bad_multiplier >= 0
        assert abs(
            max(full_multiplier, mp.mpf("0"))
            - bad_multiplier
            - full_multiplier
        ) < mp.mpf("1e-50")
    assert abs(
        canonical_bad_multiplier(mp.mpf("0"), length)
        - (2 * prime_mass(length) - archimedean_spectral_bottom())
    ) < mp.mpf("1e-50")

    polarization, defect, qw_hodge, _ = (
        build_polarization_defect_matrices(mp.sqrt(13), cutoff=3)
    )
    exact_arch_bottom = (
        mp.digamma(mp.mpf("0.25")) - mp.log(mp.pi)
    ) / 2
    assert abs(
        archimedean_spectral_bottom() - exact_arch_bottom
    ) < mp.mpf("1e-50")
    for frequency in (mp.mpf("0.1"), mp.mpf("1"), mp.mpf("10")):
        arch_value = (
            mp.re(mp.digamma(mp.mpf("0.25") + mp.j * frequency / 2))
            - mp.log(mp.pi)
        ) / 2
        assert arch_value > exact_arch_bottom
        assert (
            arch_value - exact_arch_bottom
            <= archimedean_quadratic_constant() * frequency**2
        )
    central_delta = 2 * prime_mass(length) - exact_arch_bottom
    central_radius = central_resonance_radius(length, central_delta)
    for frequency in (
        -mp.mpf("0.9") * central_radius,
        mp.mpf("0"),
        mp.mpf("0.9") * central_radius,
    ):
        arch_value = dirichlet_archimedean_multiplier(
            frequency, 0, 1
        )
        phase_value = mp.re(prime_phase_sum(frequency, length))
        assert arch_value - 2 * phase_value < central_delta
    obstruction = phase_volume_obstruction_constant()
    assert obstruction > 1
    assert abs(
        obstruction
        - mp.sqrt(2) / mp.pi * mp.power(3, mp.mpf("1.5")) / 2
    ) < mp.mpf("1e-50")
    for threshold_ratio in (
        mp.mpf("0.1"),
        mp.mpf("0.5"),
        mp.mpf("2"),
        mp.mpf("10"),
    ):
        limiting_factor = (
            mp.sqrt(2)
            / mp.pi
            * (1 + threshold_ratio) ** mp.mpf("1.5")
            / threshold_ratio
        )
        assert limiting_factor >= obstruction - mp.mpf("1e-50")
    previous_trace_tail = mp.inf
    for rank_parameter in range(1, 7):
        trace_tail = prolate_trace_tail_bound(
            mp.mpf("0.5"), rank_parameter
        )
        assert trace_tail > 0
        assert trace_tail < previous_trace_tail
        previous_trace_tail = trace_tail
    first_trace_tail = prolate_trace_tail_bound(mp.mpf("1"), 1)
    first_eigenvalue_bound = (
        2 * mp.e**2 * 4 / (mp.pi * mp.factorial(3))
    )
    assert abs(
        first_trace_tail - mp.mpf("2.5") * first_eigenvalue_bound
    ) < mp.mpf("1e-50")
    assert abs(
        dirichlet_archimedean_spectral_bottom(0, 1)
        - archimedean_spectral_bottom()
    ) < mp.mpf("1e-50")
    for parity in (0, 1):
        dirichlet_bottom = dirichlet_archimedean_spectral_bottom(
            parity, 7
        )
        assert abs(
            dirichlet_archimedean_multiplier(
                mp.mpf("0"), parity, 7
            )
            - dirichlet_bottom
        ) < mp.mpf("1e-50")
        for frequency in (mp.mpf("0.1"), mp.mpf("2"), mp.mpf("15")):
            assert dirichlet_archimedean_multiplier(
                frequency, parity, 7
            ) > dirichlet_bottom
    conductor_shift = (
        dirichlet_archimedean_spectral_bottom(1, 35)
        - dirichlet_archimedean_spectral_bottom(1, 7)
    )
    assert abs(conductor_shift - mp.log(5) / 2) < mp.mpf("1e-50")
    assert abs(
        gamma_euler_lower_bound([0], [0], 7)
        - dirichlet_archimedean_spectral_bottom(0, 7)
    ) < mp.mpf("1e-50")
    common_shift_lower = gamma_euler_lower_bound(
        [0, 1, mp.mpf("2.5")],
        [mp.mpf("1.25")] * 3,
        11,
    )
    assert abs(
        gamma_euler_multiplier(
            mp.mpf("-1.25"),
            [0, 1, mp.mpf("2.5")],
            [mp.mpf("1.25")] * 3,
            11,
        )
        - common_shift_lower
    ) < mp.mpf("1e-50")
    separated_shift_lower = gamma_euler_lower_bound(
        [0, 1], [mp.mpf("-0.75"), mp.mpf("1.5")], 13
    )
    for frequency in (
        mp.mpf("-1.5"),
        mp.mpf("-0.75"),
        mp.mpf("0"),
        mp.mpf("2"),
    ):
        assert gamma_euler_multiplier(
            frequency,
            [0, 1],
            [mp.mpf("-0.75"), mp.mpf("1.5")],
            13,
        ) > separated_shift_lower

    def quartic_character_mod_5(k: int) -> mp.mpc:
        residue = k % 5
        return {
            0: mp.mpc(0),
            1: mp.mpc(1),
            2: mp.j,
            3: -mp.j,
            4: mp.mpc(-1),
        }[residue]

    def conjugate_quartic_character_mod_5(k: int) -> mp.mpc:
        return mp.conj(quartic_character_mod_5(k))

    twisted_energy_small = twisted_chebyshev_abel_energy(
        13, mp.mpf("0.75"), quartic_character_mod_5
    )
    twisted_energy_large = twisted_chebyshev_abel_energy(
        101, mp.mpf("0.75"), quartic_character_mod_5
    )
    conjugate_twisted_energy = twisted_chebyshev_abel_energy(
        101, mp.mpf("0.75"), conjugate_quartic_character_mod_5
    )
    assert 0 <= twisted_energy_small <= twisted_energy_large
    assert abs(twisted_energy_large - conjugate_twisted_energy) < mp.mpf(
        "1e-50"
    )

    cancellation_low = zeta_bessel_euler_coordinate(
        1, mp.mpf("0.75"), series_terms=60
    )
    cancellation_high = zeta_bessel_euler_coordinate(
        3, mp.mpf("0.75"), series_terms=80
    )
    assert cancellation_low["absolute_majorant"] >= abs(
        cancellation_low["coordinate"]
    )
    assert cancellation_high["absolute_majorant"] >= abs(
        cancellation_high["coordinate"]
    )
    assert cancellation_high["ratio"] > 100
    assert cancellation_high["ratio"] > cancellation_low["ratio"]

    # Proposition GC: piecewise integration and the independent finite
    # tent-kernel prime-square expansion agree exactly up to arithmetic
    # precision and produce a nonnegative block norm.
    for block_start in (13, 101):
        block_direct = chebyshev_block_variance(block_start)
        block_kernel = chebyshev_block_variance_max_kernel(block_start)
        assert block_direct >= 0
        assert abs(block_direct - block_kernel) < mp.mpf("1e-45")

    # Parseval audit for the endpoint-vanishing window used in note 043.
    windowed_energy = chebyshev_windowed_block_energy(13)
    windowed_coefficients = [
        chebyshev_windowed_fourier_coefficient(13, mode)
        for mode in range(-5, 6)
    ]
    windowed_partial = mp.mpf(13) * mp.fsum(
        abs(value) ** 2 for value in windowed_coefficients
    )
    assert 0 < windowed_partial < windowed_energy

    # Proposition GJ and inequality (13): the finite triangular prime formula
    # agrees with direct integration and is controlled by the block norm.
    for triangular_start in (13, 101):
        triangular = chebyshev_triangular_discrepancy(triangular_start)
        triangular_integral = chebyshev_triangular_discrepancy_integral(
            triangular_start
        )
        triangular_variance = chebyshev_block_variance(triangular_start)
        assert abs(triangular - triangular_integral) < mp.mpf("1e-45")
        assert abs(triangular) ** 2 <= (
            mp.mpf(triangular_start) * triangular_variance
        )

    # Equations (2)--(5) of note 045: the triangular coefficient is the
    # stable dilation difference (U-2^(-3/2))p.  A finite quadrature of
    # its orbit is an exact positive Gram matrix.
    for triangular_start in (13, 101):
        log_scale = mp.log(triangular_start)
        primitive = chebyshev_normalized_primitive(log_scale)
        shifted_primitive = chebyshev_normalized_primitive(
            log_scale + mp.log(2)
        )
        stable_difference = shifted_primitive - mp.power(2, -mp.mpf("1.5")) * primitive
        signal = chebyshev_dilation_riesz_signal(log_scale)
        scaled_triangular = chebyshev_triangular_discrepancy(
            triangular_start
        ) / mp.power(2 * triangular_start, mp.mpf("1.5"))
        assert abs(stable_difference - signal) < mp.mpf("1e-55")
        assert abs(signal - scaled_triangular) < mp.mpf("1e-55")

    assert chebyshev_primitive_discrepancy(1) == 0
    gram_times = [mp.mpf(index) / 10 for index in range(21)]
    gram_weights = [mp.e ** (-value / 3) for value in gram_times]
    dilation_gram = chebyshev_dilation_quadrature_gram(
        gram_times, 4, weights=gram_weights
    )
    assert mp.norm(dilation_gram - dilation_gram.T.conjugate()) < mp.mpf(
        "1e-55"
    )
    dilation_eigenvalues = mp.eigsy(dilation_gram, eigvals_only=True)
    assert min(dilation_eigenvalues) >= -mp.mpf("1e-50")

    # Proposition GU: the prime-error current, its Riesz potential, and
    # dilation form an exact de Rham square.  We evaluate away from prime
    # jumps so an independent centered difference audits both derivatives.
    audit_scale = mp.log(mp.mpf("13.25"))
    audit_step = mp.mpf("1e-8")
    kappa = mp.mpf("1.5")
    contraction = mp.power(2, -kappa)
    primitive_derivative = (
        chebyshev_normalized_primitive(audit_scale + audit_step)
        - chebyshev_normalized_primitive(audit_scale - audit_step)
    ) / (2 * audit_step)
    assert abs(
        primitive_derivative
        + kappa * chebyshev_normalized_primitive(audit_scale)
        - chebyshev_normalized_error(audit_scale)
    ) < mp.mpf("1e-14")

    signal_derivative = chebyshev_dilation_riesz_signal_derivative(
        audit_scale
    )
    signal_derivative_difference = (
        chebyshev_dilation_riesz_signal(audit_scale + audit_step)
        - chebyshev_dilation_riesz_signal(audit_scale - audit_step)
    ) / (2 * audit_step)
    assert abs(signal_derivative - signal_derivative_difference) < mp.mpf(
        "1e-14"
    )
    de_rham_right = chebyshev_normalized_error(
        audit_scale + mp.log(2)
    ) - contraction * chebyshev_normalized_error(audit_scale)
    assert abs(signal_derivative + kappa * chebyshev_dilation_riesz_signal(
        audit_scale
    ) - de_rham_right) < mp.mpf("1e-50")

    sobolev_gram = chebyshev_dilation_sobolev_quadrature_gram(
        gram_times,
        [mp.mpf(index) / 5 for index in range(4)],
        weights=gram_weights,
    )
    assert mp.norm(sobolev_gram - sobolev_gram.T.conjugate()) < mp.mpf(
        "1e-55"
    )
    sobolev_eigenvalues = mp.eigsy(sobolev_gram, eigvals_only=True)
    assert min(sobolev_eigenvalues) >= -mp.mpf("1e-50")

    # Theorems GZ--HA: audit the closed ratio profile against its defining
    # tent-feature integral, then check positivity of both K^0 and P-K^0.
    kernel_sigma = mp.mpf("0.35")
    kernel_center = mp.mpf("0.5")
    kernel_dilation = mp.mpf("2")
    kernel_c = 2 * kernel_center
    kernel_kappa = kernel_center + 1

    def direct_triangular_kernel(left: mp.mpf, right: mp.mpf) -> mp.mpf:
        maximum = max(left, right)
        minimum = min(left, right)
        breakpoints = [maximum / kernel_dilation]
        for point in (minimum, maximum):
            if point > breakpoints[-1]:
                breakpoints.append(point)
        breakpoints.append(mp.inf)

        def tent(scale: mp.mpf, source: mp.mpf) -> mp.mpf:
            return max(
                kernel_dilation * scale - max(scale, source),
                mp.mpf("0"),
            )

        exponent = 2 * kernel_kappa + 2 * kernel_sigma + 1
        integral = mp.quad(
            lambda scale: (
                scale ** (-exponent)
                * tent(scale, left)
                * tent(scale, right)
            ),
            breakpoints,
        )
        return (
            2
            * kernel_sigma
            * kernel_dilation ** (-2 * kernel_kappa)
            * integral
        )

    for left, right in (
        (mp.mpf("9"), mp.mpf("3")),
        (mp.mpf("9"), mp.mpf("6")),
        (mp.mpf("9"), mp.mpf("9")),
    ):
        closed = homogeneous_triangular_current_kernel(
            left, right, kernel_sigma
        )
        direct = direct_triangular_kernel(left, right)
        assert abs(closed - direct) < mp.mpf("1e-50")

    kernel_points = [mp.mpf(value) for value in (2, 3, 5, 9)]
    triangular_matrix = mp.matrix(
        [
            [
                homogeneous_triangular_current_kernel(
                    left, right, kernel_sigma
                )
                for right in kernel_points
            ]
            for left in kernel_points
        ]
    )
    defect_matrix = mp.matrix(
        [
            [
                triangular_local_variance_kernel(
                    left, right, kernel_sigma
                )
                for right in kernel_points
            ]
            for left in kernel_points
        ]
    )
    assert min(mp.eigsy(triangular_matrix, eigvals_only=True)) >= -mp.mpf(
        "1e-50"
    )
    assert min(mp.eigsy(defect_matrix, eigvals_only=True)) >= -mp.mpf(
        "1e-50"
    )
    assert triangular_local_variance_kernel(
        mp.mpf("9"), mp.mpf("3"), kernel_sigma
    ) == 0
    exponent = kernel_c + 2 * kernel_sigma
    plateau = triangular_ratio_profile(
        1 / kernel_dilation, exponent, kernel_dilation
    )
    assert plateau == triangular_ratio_profile(
        mp.mpf("0.25"), exponent, kernel_dilation
    )

    # Theorem HC: subtracting the two endpoint moments annihilates every
    # nonadjacent-scale coupling exactly.
    high_points = [mp.mpf("4.5"), mp.mpf("6"), mp.mpf("7.5")]
    high_weights = [mp.mpf("1.25"), mp.mpf("-0.5"), mp.mpf("0.75")]
    high_mass = mp.fsum(high_weights)
    high_weighted_mass = mp.fsum(
        weight * point ** (-exponent)
        for point, weight in zip(high_points, high_weights)
    )
    core_left, core_right = two_moment_endpoint_core(
        4, 8, exponent, high_mass, high_weighted_mass
    )
    centered_points = high_points + [mp.mpf("4"), mp.mpf("8")]
    centered_weights = high_weights + [-core_left, -core_right]
    assert abs(mp.fsum(centered_weights)) < mp.mpf("1e-55")
    assert abs(
        mp.fsum(
            weight * point ** (-exponent)
            for point, weight in zip(centered_points, centered_weights)
        )
    ) < mp.mpf("1e-55")
    low_points = [mp.mpf("1.1"), mp.mpf("1.7")]
    low_weights = [mp.mpf("0.8"), mp.mpf("-0.3")]
    long_range_coupling = mp.fsum(
        high_weight
        * low_weight
        * homogeneous_triangular_current_kernel(
            high_point, low_point, kernel_sigma
        )
        for high_point, high_weight in zip(
            centered_points, centered_weights
        )
        for low_point, low_weight in zip(low_points, low_weights)
    )
    assert abs(long_range_coupling) < mp.mpf("1e-55")

    # Theorems HF--HH: the merged endpoint core is a Brownian max kernel
    # and, after geometric weighting, an AR(1) Toeplitz form with a
    # cutoff-independent critical spectral margin.
    prefix_charges = [
        mp.mpf("1.25"),
        mp.mpf("-0.75"),
        mp.mpf("0.5"),
        mp.mpf("-0.125"),
    ]
    prefix_direct = mp.fsum(
        left_charge
        * right_charge
        * mp.power(2, -max(left, right))
        for left, left_charge in enumerate(prefix_charges)
        for right, right_charge in enumerate(prefix_charges)
    )
    assert abs(
        prefix_direct
        - geometric_max_prefix_energy(prefix_charges, mp.mpf("1"))
    ) < mp.mpf("1e-55")

    core_parameters = endpoint_core_toeplitz_parameters(mp.mpf("1"))
    assert abs(core_parameters["plateau"] - mp.mpf("1.5")) < mp.mpf(
        "1e-55"
    )
    assert abs(core_parameters["diagonal"] - mp.mpf(4) / 3) < mp.mpf(
        "1e-55"
    )
    assert abs(core_parameters["eta"] - mp.mpf(1) / 9) < mp.mpf(
        "1e-55"
    )
    core_size = 8
    critical_core = critical_zeta_endpoint_core_matrix(core_size)
    rho = 1 / mp.sqrt(2)
    weight = mp.diag([rho**index for index in range(core_size)])
    weight_inverse = mp.diag(
        [rho ** (-index) for index in range(core_size)]
    )
    normalized_core = (
        weight_inverse * critical_core * weight_inverse
    ) / (mp.mpf(3) / 16)
    expected_toeplitz = mp.matrix(
        [
            [
                rho ** abs(left - right)
                - (mp.mpf(1) / 9 if left == right else 0)
                for right in range(core_size)
            ]
            for left in range(core_size)
        ]
    )
    assert mp.norm(normalized_core - expected_toeplitz) < mp.mpf("1e-55")
    critical_margin = mp.mpf(26) / 9 - 2 * mp.sqrt(2)
    assert min(mp.eigsy(normalized_core, eigvals_only=True)) >= critical_margin

    # Proposition HI: independently integrate H(L), then verify the merged
    # endpoint weights equal the local two-block wavelet charge.
    for block_start in (8, 32):
        psi_value = mp.fsum(
            von_mangoldt(integer)
            for integer in range(2, block_start + 1)
        )
        direct_log_moment = mp.mpf("0")
        for integer in range(block_start, 2 * block_start):
            if integer > block_start:
                psi_value += von_mangoldt(integer)
            direct_log_moment += (
                psi_value
                * (1 / mp.mpf(integer) - 1 / mp.mpf(integer + 1))
                - mp.log(mp.mpf(integer + 1) / integer)
            )
        assert abs(
            chebyshev_log_block_moment(block_start) - direct_log_moment
        ) < mp.mpf("1e-55")

        left = mp.mpf(block_start)
        previous_h = chebyshev_log_block_moment(block_start // 2)
        current_h = chebyshev_log_block_moment(block_start)
        merged_from_endpoints = left * (2 * current_h - previous_h)
        assert abs(
            chebyshev_dyadic_core_charge(block_start)
            - merged_from_endpoints
        ) < mp.mpf("1e-55")

    # Propositions HM--HN: independently differentiate the continuous
    # prime wavelet away from prime endpoints and verify the massive
    # translation identity plus its bilateral Wiener inverse.
    wavelet_time = mp.log(mp.mpf("13.25"))
    wavelet_step = mp.mpf("1e-8")
    wavelet_derivative = (
        chebyshev_prime_wavelet(wavelet_time + wavelet_step)
        - chebyshev_prime_wavelet(wavelet_time - wavelet_step)
    ) / (2 * wavelet_step)
    wavelet_left = (
        wavelet_derivative
        - mp.mpf("0.5") * chebyshev_prime_wavelet(wavelet_time)
    )
    wavelet_right = (
        mp.sqrt(2)
        * (
            chebyshev_normalized_error(wavelet_time + mp.log(2))
            + chebyshev_normalized_error(wavelet_time - mp.log(2))
        )
        - 3 * chebyshev_normalized_error(wavelet_time)
    )
    assert abs(wavelet_left - wavelet_right) < mp.mpf("1e-14")

    wiener_ratio = 1 / mp.sqrt(2)
    for angle in (mp.mpf("0"), mp.mpf("0.7"), mp.pi):
        inverse_symbol = mp.fsum(
            wiener_ratio ** abs(index) * mp.e ** (mp.j * index * angle)
            for index in range(-400, 401)
        )
        massive_symbol = 3 - 2 * mp.sqrt(2) * mp.cos(angle)
        assert abs(massive_symbol * inverse_symbol - 1) < mp.mpf("1e-55")

    # Theorems HS--HT: the compact positive prime kernel reproduces the
    # wavelet charge, and the finite pair/cross/background expansion agrees
    # with an independent integral of the original H(L) formula.
    local_scale = mp.mpf("13.25")
    local_charge = chebyshev_prime_wavelet_local_charge(local_scale)
    moment_charge = mp.sqrt(local_scale) * chebyshev_prime_wavelet(
        mp.log(local_scale)
    )
    assert abs(local_charge - moment_charge) < mp.mpf("1e-55")
    phi_mass = mp.quad(prime_wavelet_kernel, [mp.mpf("0.5"), 1, 2])
    phi_square_mass = mp.quad(
        lambda value: prime_wavelet_kernel(value) ** 2,
        [mp.mpf("0.5"), 1, 2],
    )
    assert abs(phi_mass - mp.log(2)) < mp.mpf("1e-55")
    assert abs(phi_square_mass - (6 - 8 * mp.log(2))) < mp.mpf("1e-55")

    pair_start = 8
    pair_block = chebyshev_prime_wavelet_pair_block(pair_start)
    assert abs(
        pair_block["total"]
        - pair_block["prime_pair"]
        - pair_block["cross"]
        - pair_block["background"]
    ) < mp.mpf("1e-50")
    assert pair_block["diagonal"] > 0
    pair_breakpoints = [
        mp.mpf(integer) / 2
        for integer in range(2 * pair_start, 4 * pair_start + 1)
    ]
    independent_block = mp.fsum(
        mp.quad(
            lambda scale: chebyshev_prime_wavelet(mp.log(scale)) ** 2
            / scale,
            [left, right],
        )
        for left, right in zip(
            pair_breakpoints[:-1], pair_breakpoints[1:]
        )
    )
    assert abs(pair_block["total"] - independent_block) < mp.mpf("1e-48")
    assert abs(
        pair_block["diagonal"]
        - chebyshev_prime_wavelet_diagonal(pair_start)
    ) < mp.mpf("1e-55")

    # Propositions HY--HZ and Theorem IA: coefficient-level centering differs
    # from the continuum formula only by a uniformly bounded Riemann error,
    # while the all-coefficient frame quotient already grows on scale X.
    for scale in (mp.mpf("8"), mp.mpf("13.25"), mp.mpf("31.7")):
        remainder = prime_wavelet_riemann_remainder(scale)
        assert abs(remainder) <= 2
        assert abs(
            chebyshev_prime_wavelet_local_charge(scale)
            - chebyshev_prime_wavelet_centered_charge(scale)
            - remainder
        ) < mp.mpf("1e-55")

    centered_block = prime_wavelet_centered_frame_block(pair_start)
    assert centered_block["centered_diagonal"] > 0
    assert abs(
        centered_block["centered_diagonal"]
        - chebyshev_prime_wavelet_centered_diagonal(pair_start)
    ) < mp.mpf("1e-55")
    assert abs(
        mp.sqrt(pair_block["total"])
        - mp.sqrt(centered_block["centered_energy"])
    ) <= mp.sqrt(mp.mpf(2) / pair_start)
    assert centered_block["generic_rayleigh"] > 1

    # Propositions IE--IG: the second scale difference kills the continuum
    # term exactly, leaves a pure-prime degree-zero kernel, and its block
    # energy is a positive Gram despite chi changing sign.
    chi_mass = mp.quad(
        primitive_prime_wavelet_kernel,
        [mp.mpf("0.25"), mp.mpf("0.5"), 1, 2],
    )
    chi_square_mass = mp.quad(
        lambda value: primitive_prime_wavelet_kernel(value) ** 2,
        [mp.mpf("0.25"), mp.mpf("0.5"), 1, 2],
    )
    assert abs(chi_mass) < mp.mpf("1e-55")
    assert abs(chi_square_mass - (26 - 36 * mp.log(2))) < mp.mpf("1e-55")
    primitive_scale = mp.mpf("13.25")
    primitive_charge = chebyshev_primitive_prime_wavelet_charge(
        primitive_scale
    )
    primitive_from_difference = (
        chebyshev_prime_wavelet_local_charge(primitive_scale)
        - 2 * chebyshev_prime_wavelet_local_charge(primitive_scale / 2)
    )
    assert abs(primitive_charge - primitive_from_difference) < mp.mpf("1e-55")
    primitive_remainder = primitive_prime_wavelet_riemann_remainder(
        primitive_scale
    )
    assert abs(primitive_remainder) <= 6
    assert abs(
        primitive_charge
        - chebyshev_primitive_prime_wavelet_centered_charge(primitive_scale)
        - primitive_remainder
    ) < mp.mpf("1e-55")
    primitive_time = mp.log(primitive_scale)
    normalized_primitive = chebyshev_normalized_primitive_prime_wavelet(
        primitive_time
    )
    normalized_from_difference = (
        chebyshev_prime_wavelet(primitive_time)
        - mp.sqrt(2)
        * chebyshev_prime_wavelet(primitive_time - mp.log(2))
    )
    assert abs(normalized_primitive - normalized_from_difference) < mp.mpf("1e-55")

    primitive_block = chebyshev_primitive_prime_wavelet_block(pair_start)
    assert primitive_block["total"] >= 0
    assert primitive_block["diagonal"] > 0
    assert abs(
        primitive_block["diagonal"]
        - chebyshev_primitive_prime_wavelet_diagonal(pair_start)
    ) < mp.mpf("1e-55")
    assert abs(
        primitive_block["total"]
        - primitive_block["diagonal"]
        - primitive_block["off_diagonal"]
    ) < mp.mpf("1e-55")

    # The primitive scale polynomial has a uniform unit-circle gap and the
    # one-sided Wiener series is its inverse.  It kills the Tate eigenvalue
    # sqrt(2), which lies off the critical unitary spectrum.
    for angle in (mp.mpf("0"), mp.mpf("0.7"), mp.pi):
        primitive_symbol = 1 - mp.sqrt(2) * mp.e ** (-mp.j * angle)
        primitive_inverse = -mp.fsum(
            mp.power(2, -mp.mpf(index) / 2)
            * mp.e ** (mp.j * index * angle)
            for index in range(1, 400)
        )
        assert abs(primitive_symbol * primitive_inverse - 1) < mp.mpf("1e-55")
        assert abs(primitive_symbol) >= mp.sqrt(2) - 1
    assert abs(1 - mp.sqrt(2) * (1 / mp.sqrt(2))) < mp.mpf("1e-55")

    # Propositions IK--IL: the full homogeneous ratio profile is the exact
    # three-scale autocorrelation of the old positive wavelet profile.  Its
    # entries may be negative, while every finite kernel matrix stays PSD.
    for ratio in (
        mp.mpf("0.13"),
        mp.mpf("0.25"),
        mp.mpf("0.4"),
        mp.mpf("0.75"),
        mp.mpf("1"),
    ):
        phi_breakpoints = sorted(
            {
                mp.mpf("0"),
                *(
                    point
                    for breakpoint in (
                        mp.mpf("0.5"),
                        mp.mpf("1"),
                        mp.mpf("2"),
                    )
                    for point in (breakpoint, breakpoint / ratio)
                ),
            }
        )
        primitive_breakpoints = sorted(
            {
                mp.mpf("0"),
                *(
                    point
                    for breakpoint in (
                        mp.mpf("0.25"),
                        mp.mpf("0.5"),
                        mp.mpf("1"),
                        mp.mpf("2"),
                    )
                    for point in (breakpoint, breakpoint / ratio)
                ),
            }
        )
        direct_phi_profile = mp.quad(
            lambda value: prime_wavelet_kernel(ratio * value)
            * prime_wavelet_kernel(value),
            phi_breakpoints,
        )
        direct_primitive_profile = mp.quad(
            lambda value: primitive_prime_wavelet_kernel(ratio * value)
            * primitive_prime_wavelet_kernel(value),
            primitive_breakpoints,
        )
        assert abs(
            direct_phi_profile - prime_wavelet_homogeneous_profile(ratio)
        ) < mp.mpf("1e-50")
        assert abs(
            direct_primitive_profile
            - primitive_prime_wavelet_homogeneous_profile(ratio)
        ) < mp.mpf("1e-50")
    assert primitive_prime_wavelet_homogeneous_profile(mp.mpf("0.4")) < 0
    profile_points = [mp.mpf("1"), mp.mpf("1.7"), mp.mpf("3.2"), mp.mpf("7")]
    profile_matrix = np.array(
        [
            [
                float(
                    primitive_prime_wavelet_homogeneous_profile(
                        min(left, right) / max(left, right)
                    )
                    / max(left, right)
                )
                for right in profile_points
            ]
            for left in profile_points
        ]
    )
    assert np.linalg.eigvalsh(profile_matrix)[0] > -1e-12

    # Theorem IM--IN: within each ratio chamber the profile has four-moment
    # semiseparable rank.  The resulting prefix-moment single sum agrees with
    # the direct double Gram for a generic complex finite coefficient vector.
    for ratio in (
        mp.mpf("0.17"),
        mp.mpf("0.31"),
        mp.mpf("0.73"),
    ):
        a_value, b_value, c_value, d_value = (
            primitive_profile_chamber_coefficients(ratio)
        )
        factorized_profile = (
            a_value
            + b_value * mp.log(ratio)
            + (c_value + d_value * mp.log(ratio)) / ratio
        )
        assert abs(
            factorized_profile
            - primitive_prime_wavelet_homogeneous_profile(ratio)
        ) < mp.mpf("1e-55")

    audit_coefficients = {
        5: mp.mpc("1.1", "-0.2"),
        7: mp.mpc("-0.4", "0.3"),
        13: mp.mpc("0.8", "0.1"),
        23: mp.mpc("-0.2", "-0.7"),
        47: mp.mpc("0.5", "0.4"),
        97: mp.mpc("-0.3", "0.2"),
    }
    direct_homogeneous_energy = mp.fsum(
        left_value
        * mp.conj(right_value)
        * primitive_prime_wavelet_homogeneous_kernel(left, right)
        for left, left_value in audit_coefficients.items()
        for right, right_value in audit_coefficients.items()
    )
    moment_homogeneous_energy = primitive_homogeneous_moment_energy(
        audit_coefficients
    )
    assert abs(mp.im(direct_homogeneous_energy)) < mp.mpf("1e-55")
    assert abs(
        mp.re(direct_homogeneous_energy) - moment_homogeneous_energy
    ) < mp.mpf("1e-50")
    assert moment_homogeneous_energy >= 0

    centered_homogeneous = primitive_centered_homogeneous_block(pair_start)
    assert centered_homogeneous["energy"] >= 0
    assert centered_homogeneous["diagonal"] > 0
    assert abs(
        centered_homogeneous["rayleigh"]
        - centered_homogeneous["energy"]
        / centered_homogeneous["diagonal"]
    ) < mp.mpf("1e-55")

    # Theorems IR--IU: exact Mellin--Plancherel weight, stable removal of the
    # massive factor, and the resulting two-prefix-moment biharmonic Gram.
    for frequency in (
        mp.mpf("0"),
        mp.mpf("0.7"),
        mp.mpf("3.25"),
    ):
        mellin_value = primitive_prime_wavelet_mellin(
            mp.mpc("0.5", frequency)
        )
        assert abs(
            abs(mellin_value) ** 2
            - primitive_prime_wavelet_spectral_weight(frequency)
        ) < mp.mpf("1e-50")

    direct_biharmonic_energy = mp.fsum(
        left_value
        * mp.conj(right_value)
        * massive_biharmonic_hodge_kernel(left, right)
        for left, left_value in audit_coefficients.items()
        for right, right_value in audit_coefficients.items()
    )
    moment_biharmonic_energy = massive_biharmonic_moment_energy(
        audit_coefficients
    )
    assert abs(mp.im(direct_biharmonic_energy)) < mp.mpf("1e-55")
    assert abs(
        mp.re(direct_biharmonic_energy) - moment_biharmonic_energy
    ) < mp.mpf("1e-50")
    assert moment_biharmonic_energy >= 0

    biharmonic_block = centered_biharmonic_hodge_block(pair_start)
    massive_lower = (3 - 2 * mp.sqrt(2)) ** 3
    massive_upper = (3 + 2 * mp.sqrt(2)) ** 3
    assert (
        massive_lower * biharmonic_block["energy"]
        <= centered_homogeneous["energy"]
        <= massive_upper * biharmonic_block["energy"]
    )
    assert biharmonic_block["diagonal"] > 0

    # Theorems IY--JA: arbitrary-order massive Sobolev Green kernels are
    # exponential polynomials and require only r logarithmic prefix moments.
    assert massive_sobolev_green_polynomial(1, mp.mpf("0.7")) == 1
    assert abs(
        massive_sobolev_green_polynomial(2, mp.mpf("0.7"))
        - mp.mpf("2.7")
    ) < mp.mpf("1e-55")
    for order in (1, 2, 3, 4):
        direct_sobolev_energy = mp.fsum(
            left_value
            * mp.conj(right_value)
            * massive_sobolev_hodge_kernel(left, right, order)
            for left, left_value in audit_coefficients.items()
            for right, right_value in audit_coefficients.items()
        )
        moment_sobolev_energy = massive_sobolev_moment_energy(
            audit_coefficients, order
        )
        assert abs(mp.im(direct_sobolev_energy)) < mp.mpf("1e-50")
        assert abs(
            mp.re(direct_sobolev_energy) - moment_sobolev_energy
        ) < mp.mpf("1e-45")
        assert moment_sobolev_energy >= 0
    assert abs(
        massive_sobolev_moment_energy(audit_coefficients, 2)
        - moment_biharmonic_energy
    ) < mp.mpf("1e-50")

    # Theorems JF--JH: Poisson sampling turns the continuous Sobolev Gram
    # into finitely many positive twisted Dirichlet coordinates.  With a
    # fine grid and order four, alias plus truncation is already tiny.
    sampled_order = 4
    sampled_energy = sampled_massive_sobolev_energy(
        audit_coefficients,
        sampled_order,
        mp.mpf("0.05"),
        2400,
    )
    exact_sampled_target = massive_sobolev_moment_energy(
        audit_coefficients, sampled_order
    )
    assert abs(sampled_energy - exact_sampled_target) < mp.mpf("2e-12")
    assert abs(centered_dirichlet_polynomial(audit_coefficients, 0)) > 0

    # Theorems JK--JN: fixed exponential type compresses the slow frequency
    # window further to O(log X/log log X) centered logarithmic moments.
    taylor_center = mp.mpf("20")
    taylor_degree = 36
    taylor_cutoff = mp.mpf("1")
    logarithmic_moments = centered_logarithmic_moments(
        audit_coefficients, taylor_center, taylor_degree
    )
    for frequency in (mp.mpf("-1"), mp.mpf("-0.3"), mp.mpf("0.8")):
        exact_centered_value = (
            mp.power(taylor_center, mp.j * frequency)
            * centered_dirichlet_polynomial(audit_coefficients, frequency)
        )
        approximate_centered_value = taylor_dirichlet_polynomial(
            logarithmic_moments, frequency
        )
        assert abs(exact_centered_value - approximate_centered_value) < mp.mpf(
            "1e-35"
        )
    exact_taylor_core = mp.quad(
        lambda frequency: abs(
            centered_dirichlet_polynomial(audit_coefficients, frequency)
        )
        ** 2
        / (frequency**2 + mp.mpf("0.25")) ** sampled_order,
        [-taylor_cutoff, 0, taylor_cutoff],
    ) / (2 * mp.pi)
    moment_taylor_core = taylor_sobolev_core_energy(
        audit_coefficients,
        taylor_center,
        sampled_order,
        taylor_cutoff,
        taylor_degree,
    )
    assert abs(exact_taylor_core - moment_taylor_core) < mp.mpf("1e-35")

    # Theorems JV--JX: the zeroth logarithmic moment is already a rank-one
    # off-center divisor detector; its annular multiplier has no zeros in
    # either open half-plane.
    annular_scale = mp.mpf("16")
    annular_coefficients = {
        integer: von_mangoldt(integer) - 1
        for integer in range(5, 65)
    }
    annular_moment_zero = centered_logarithmic_moments(
        annular_coefficients, annular_scale, 1
    )[0]
    assert abs(
        annular_moment_zero
        - centered_annular_euler_coordinate(annular_scale)
    ) < mp.mpf("1e-55")
    assert abs(
        centered_annular_mellin_multiplier(0) - 2 * mp.log(4)
    ) < mp.mpf("1e-55")
    for mellin_value in (
        mp.mpc("0.2", "0.7"),
        mp.mpc("-0.3", "1.1"),
        mp.mpc("0.5", "0"),
    ):
        assert abs(centered_annular_mellin_multiplier(mellin_value)) > 0

    # Theorems KA--KD: averaging annular widths removes every critical-line
    # phase alias and produces a uniformly positive spectral frame.
    width_left = mp.log(2)
    width_right = 2 * mp.log(2)
    assert abs(
        annular_frame_spectral_multiplier(0, width_left, width_right)
        - (width_right**3 - width_left**3) / 3
    ) < mp.mpf("1e-55")
    for frequency in (
        mp.mpf("0.01"),
        mp.mpf("0.7"),
        mp.mpf("3"),
        mp.mpf("25"),
    ):
        direct_width_average = mp.quad(
            lambda width: 4
            * (frequency**2 + mp.mpf("0.25"))
            / frequency**2
            * mp.sin(width * frequency) ** 2,
            [width_left, width_right],
        )
        assert abs(
            direct_width_average
            - annular_frame_spectral_multiplier(
                frequency, width_left, width_right
            )
        ) < mp.mpf("1e-50")
        assert direct_width_average > 0
    shrinking_frequency = mp.mpf("1.3")
    for shrinking_width in (mp.mpf("1e-2"), mp.mpf("1e-3")):
        scaled_multiplier = annular_frame_spectral_multiplier(
            shrinking_frequency,
            shrinking_width,
            2 * shrinking_width,
        ) / shrinking_width**3
        limiting_multiplier = (
            mp.mpf(28)
            / 3
            * (shrinking_frequency**2 + mp.mpf("0.25"))
        )
        assert abs(scaled_multiplier - limiting_multiplier) < 50 * shrinking_width**2

    # Theorems KK, KQ, and KW: Abel pair moments and endpoint recurrence.
    abel_left_index = 13
    abel_right_index = 17
    abel_left_width = mp.mpf("0.6")
    abel_right_width = mp.mpf("0.5")
    abel_sigma = mp.mpf("0.8")
    direct_abel_pair = 2 * abel_sigma * mp.quad(
        lambda time: (
            1
            if abs(time - mp.log(abel_left_index)) < abel_left_width
            and abs(time - mp.log(abel_right_index)) < abel_right_width
            else 0
        )
        * mp.e ** (-2 * abel_sigma * time),
        [
            0,
            max(
                mp.log(abel_left_index) - abel_left_width,
                mp.log(abel_right_index) - abel_right_width,
            ),
            min(
                mp.log(abel_left_index) + abel_left_width,
                mp.log(abel_right_index) + abel_right_width,
            ),
            mp.log(abel_left_index) + abel_left_width + 1,
        ],
    )
    assert abs(
        direct_abel_pair
        - annular_abel_pair_kernel(
            abel_left_index,
            abel_right_index,
            abel_left_width,
            abel_right_width,
            abel_sigma,
        )
    ) < mp.mpf("1e-50")
    assert abs(
        annular_abel_pair_kernel(
            abel_left_index,
            abel_right_index,
            abel_left_width,
            abel_right_width,
            abel_sigma,
        )
        - annular_abel_moment_pair_kernel(
            abel_left_index,
            abel_right_index,
            abel_left_width,
            abel_right_width,
            abel_sigma,
            0,
        )
    ) < mp.mpf("1e-50")
    moment_order = 3
    direct_abel_moment = 2 * abel_sigma * mp.quad(
        lambda time: (
            time**moment_order
            if abs(time - mp.log(abel_left_index)) < abel_left_width
            and abs(time - mp.log(abel_right_index)) < abel_right_width
            else 0
        )
        * mp.e ** (-2 * abel_sigma * time),
        [
            0,
            max(
                mp.log(abel_left_index) - abel_left_width,
                mp.log(abel_right_index) - abel_right_width,
            ),
            min(
                mp.log(abel_left_index) + abel_left_width,
                mp.log(abel_right_index) + abel_right_width,
            ),
            mp.log(abel_left_index) + abel_left_width + 1,
        ],
    )
    assert abs(
        direct_abel_moment
        - annular_abel_moment_pair_kernel(
            abel_left_index,
            abel_right_index,
            abel_left_width,
            abel_right_width,
            abel_sigma,
            moment_order,
        )
    ) < mp.mpf("1e-50")
    lower_endpoint = max(
        mp.mpf("0"),
        mp.log(abel_left_index) - abel_left_width,
        mp.log(abel_right_index) - abel_right_width,
    )
    upper_endpoint = min(
        mp.log(abel_left_index) + abel_left_width,
        mp.log(abel_right_index) + abel_right_width,
    )
    next_kernel = annular_abel_moment_pair_kernel(
        abel_left_index,
        abel_right_index,
        abel_left_width,
        abel_right_width,
        abel_sigma,
        moment_order + 1,
    )
    recurrence_kernel = (
        (moment_order + 1)
        / (2 * abel_sigma)
        * annular_abel_moment_pair_kernel(
            abel_left_index,
            abel_right_index,
            abel_left_width,
            abel_right_width,
            abel_sigma,
            moment_order,
        )
        + lower_endpoint ** (moment_order + 1)
        * mp.e ** (-2 * abel_sigma * lower_endpoint)
        - upper_endpoint ** (moment_order + 1)
        * mp.e ** (-2 * abel_sigma * upper_endpoint)
    )
    assert abs(next_kernel - recurrence_kernel) < mp.mpf("1e-50")
    sampling_kernel = annular_gamma_sampling_pair_kernel(
        abel_left_index,
        abel_right_index,
        abel_left_width,
        abel_right_width,
        abel_sigma,
        moment_order,
    )
    direct_sampling_probability = mp.gammainc(
        moment_order + 1,
        2 * abel_sigma * lower_endpoint,
        2 * abel_sigma * upper_endpoint,
    ) / mp.factorial(moment_order)
    assert 0 <= sampling_kernel <= 1
    assert abs(sampling_kernel - direct_sampling_probability) < mp.mpf("1e-50")
    sampling_cutoff = (lower_endpoint + upper_endpoint) / 2
    truncated_sampling_kernel = annular_gamma_sampling_pair_kernel(
        abel_left_index,
        abel_right_index,
        abel_left_width,
        abel_right_width,
        abel_sigma,
        moment_order,
        sampling_cutoff,
    )
    direct_truncated_probability = mp.gammainc(
        moment_order + 1,
        2 * abel_sigma * lower_endpoint,
        2 * abel_sigma * sampling_cutoff,
    ) / mp.factorial(moment_order)
    assert 0 <= truncated_sampling_kernel <= sampling_kernel
    assert (
        abs(truncated_sampling_kernel - direct_truncated_probability)
        < mp.mpf("1e-50")
    )
    left_rkhs_parameter = mp.mpc("0.2", "0.1")
    right_rkhs_parameter = mp.mpc("-0.1", "0.3")
    direct_rkhs_pair = mp.quad(
        lambda time: (
            2
            * abel_sigma
            * mp.e
            ** (
                -abel_sigma
                * (2 - left_rkhs_parameter - mp.conj(right_rkhs_parameter))
                * time
            )
        ),
        [lower_endpoint, upper_endpoint],
    )
    rkhs_pair = annular_abel_rkhs_pair_kernel(
        abel_left_index,
        abel_right_index,
        abel_left_width,
        abel_right_width,
        abel_sigma,
        left_rkhs_parameter,
        right_rkhs_parameter,
    )
    reflected_rkhs_pair = annular_abel_rkhs_pair_kernel(
        abel_right_index,
        abel_left_index,
        abel_right_width,
        abel_left_width,
        abel_sigma,
        right_rkhs_parameter,
        left_rkhs_parameter,
    )
    assert abs(rkhs_pair - direct_rkhs_pair) < mp.mpf("1e-50")
    assert abs(rkhs_pair - mp.conj(reflected_rkhs_pair)) < mp.mpf("1e-50")
    radial_parameter = mp.mpf("0.35")
    radial_rkhs_pair = annular_abel_rkhs_pair_kernel(
        abel_left_index,
        abel_right_index,
        abel_left_width,
        abel_right_width,
        abel_sigma,
        radial_parameter,
        radial_parameter,
    )
    radial_abel_pair = annular_abel_pair_kernel(
        abel_left_index,
        abel_right_index,
        abel_left_width,
        abel_right_width,
        abel_sigma * (1 - radial_parameter),
    )
    assert (
        abs((1 - radial_parameter) * radial_rkhs_pair - radial_abel_pair)
        < mp.mpf("1e-50")
    )
    taylor_degree = 4
    taylor_radius = mp.mpf("0.6")
    taylor_argument = mp.mpf("0.7")
    direct_taylor_square = mp.fsum(
        (taylor_radius * taylor_argument) ** power / mp.factorial(power)
        for power in range(taylor_degree + 1)
    ) ** 2
    moment_taylor_square = mp.fsum(
        rkhs_taylor_moment_weight(
            moment_order,
            taylor_degree,
            taylor_radius,
        )
        * (2 * taylor_argument) ** moment_order
        / mp.factorial(moment_order)
        for moment_order in range(2 * taylor_degree + 1)
    )
    assert abs(direct_taylor_square - moment_taylor_square) < mp.mpf("1e-50")
    highest_taylor_weight = rkhs_taylor_moment_weight(
        2 * taylor_degree,
        taylor_degree,
        taylor_radius,
    )
    assert abs(
        highest_taylor_weight
        - taylor_radius ** (2 * taylor_degree)
        * mp.binomial(2 * taylor_degree, taylor_degree)
        / 2 ** (2 * taylor_degree)
    ) < mp.mpf("1e-50")
    radial_weight_degree = 8
    radial_weight_time = mp.mpf("1.7")
    radial_weight_sigma = mp.mpf("0.9")
    radial_weight = radial_taylor_sampling_weight(
        radial_weight_time,
        radial_weight_degree,
        radial_weight_sigma,
    )
    radial_weight_parameter = 1 - mp.mpf(1) / radial_weight_degree
    poisson_parameter = (
        radial_weight_sigma * radial_weight_parameter * radial_weight_time
    )
    poisson_cdf = mp.gammainc(
        radial_weight_degree + 1,
        poisson_parameter,
        mp.inf,
    ) / mp.factorial(radial_weight_degree)
    poisson_radial_weight = (
        2
        * radial_weight_sigma
        / radial_weight_degree
        * mp.e
        ** (-2 * radial_weight_sigma * radial_weight_time / radial_weight_degree)
        * poisson_cdf**2
    )
    assert radial_weight > 0
    assert abs(radial_weight - poisson_radial_weight) < mp.mpf("1e-50")
    radial_mass_degree = 80
    radial_mass_radius = 1 - mp.mpf(1) / radial_mass_degree
    radial_mass = mp.fsum(
        rkhs_taylor_moment_weight(
            moment_order,
            radial_mass_degree,
            radial_mass_radius,
        )
        for moment_order in range(2 * radial_mass_degree + 1)
    ) / radial_mass_degree
    assert abs(radial_mass - (1 - mp.e ** (-2))) < mp.mpf("0.03")

    for frequency in (mp.mpf("-3.5"), mp.mpf("0"), mp.mpf("2.25")):
        twisted = twisted_prime_phase_data(
            frequency, length, quartic_character_mod_5
        )
        reflected = twisted_prime_phase_data(
            -frequency, length, conjugate_quartic_character_mod_5
        )
        assert 0 <= twisted["graph_symbol"] <= 4 * twisted["mass"]
        assert abs(
            twisted["graph_symbol"] - reflected["graph_symbol"]
        ) < mp.mpf("1e-50")
    reconstruction_error = np.max(
        np.abs(polarization - defect - qw_hodge)
    )
    assert reconstruction_error < 1e-10
    assert np.linalg.eigvalsh((polarization + polarization.T) / 2)[0] > 0
    assert np.linalg.eigvalsh((defect + defect.T) / 2)[0] > 0
    hodge_epsilon = 0.1
    hodge_radius = largest_generalized_eigenvalue(
        polarization, defect, hodge_epsilon
    )
    shifted_qw_bottom = np.linalg.eigvalsh(
        (qw_hodge + qw_hodge.T) / 2
        + hodge_epsilon * np.eye(qw_hodge.shape[0])
    )[0]
    assert (hodge_radius <= 1 + 1e-10) == (
        shifted_qw_bottom >= -1e-10
    )
    stressed_defect = defect + 0.101 * np.eye(defect.shape[0])
    stressed_radii = generalized_eigenvalues(
        polarization, stressed_defect, hodge_epsilon
    )
    stressed_qw = polarization - stressed_defect
    negative_inertia = np.count_nonzero(
        np.linalg.eigvalsh(
            (stressed_qw + stressed_qw.T) / 2
            + hodge_epsilon * np.eye(stressed_qw.shape[0])
        )
        < -1e-10
    )
    hodge_crossings = np.count_nonzero(stressed_radii > 1 + 1e-10)
    assert negative_inertia > 0
    assert hodge_crossings == negative_inertia

    core_block = np.array([[4.0, 0.2], [0.2, 3.0]])
    coupling = np.array([[0.2, 0.1], [0.1, -0.1], [0.05, 0.2]])
    complement = np.diag([2.0, 3.0, 4.0])
    complement_gap = np.linalg.eigvalsh(complement)[0]
    residual_gram = coupling.T @ coupling
    feshbach_lower = residual_feshbach_lower_matrix(
        core_block, residual_gram, complement_gap
    )
    exact_schur = (
        core_block
        - coupling.T @ np.linalg.solve(complement, coupling)
    )
    assert np.linalg.eigvalsh(exact_schur - feshbach_lower)[0] > -1e-14
    full_threshold = np.block(
        [[core_block, coupling.T], [coupling, complement]]
    )
    action_on_core = full_threshold[:, :2]
    residual_from_action = (
        action_on_core.T @ action_on_core - core_block @ core_block
    )
    assert np.max(np.abs(residual_from_action - residual_gram)) < 1e-14
    anchor = np.array([0.3, -0.2])
    full_anchor = np.concatenate([anchor, np.zeros(3)])
    exact_resolvent = float(
        2
        * full_anchor
        @ np.linalg.solve(full_threshold, full_anchor)
    )
    certified_resolvent = rank_one_resolvent_upper(
        feshbach_lower, anchor
    )
    assert exact_resolvent <= certified_resolvent + 1e-14
    assert abs(graph["identity_error"]) < mp.mpf("1e-50")
    assert prime_graph_symbol(mp.mpf("0"), length) == 0
    second_log_moment = prime_log_moment(2, length)
    for frequency in (mp.mpf("0.1"), mp.mpf("1"), mp.mpf("17.5")):
        symbol = prime_graph_symbol(frequency, length)
        assert 0 <= symbol <= 4 * prime_mass(length)
        assert symbol <= frequency**2 * second_log_moment
        reconstructed = 2 * prime_mass(length) - 2 * mp.re(
            prime_phase_sum(frequency, length)
        )
        assert abs(symbol - reconstructed) < mp.mpf("1e-50")

    # Closed formula (4.2) agrees with its defining integral.
    for n, m in ((0, 0), (1, 1), (1, -2), (0, 3)):
        direct = mp.quad(
            lambda x: q_nm(x, n, m, length)
            * (mp.e ** (x / 2) + mp.e ** (-x / 2)),
            [0, length],
        )
        assert abs(w02(n, m, length) - direct) < mp.mpf("1e-50")

    # Each increasingly cancellation-aware bound still contains |W_nm|.
    pairs = ((0, 8), (1, 8), (3, 20), (-2, 20), (20, 21), (8, -9))
    for n, m in pairs:
        actual = abs(qw_entry(n, m, length))
        coarse = off_diagonal_bound(n, m, length)
        no_log = improved_off_diagonal_bound(n, m, length)
        preserving = certificate_off_diagonal_bound(n, m, length)
        assert actual <= preserving <= no_log <= coarse

    # A sampled part of the true tail is below the proved full-tail bound.
    for n in (0, 3):
        cutoff = 8
        partial = mp.fsum(
            abs(qw_entry(n, sign * m, length)) ** 2
            for m in range(cutoff + 1, 31)
            for sign in (-1, 1)
        )
        proved = improved_row_square_tail_bound(n, cutoff, length)
        assert partial <= proved

    # Theorem S controls a linear combination, not just each row separately.
    coefficients = {
        -2: mp.mpf("0.125"),
        -1: mp.mpf("-0.25"),
        0: mp.mpf("0.5"),
        1: mp.mpf("-0.25"),
        2: mp.mpf("0.125"),
    }
    cutoff = 8
    sampled = mp.mpf("0")
    for m in range(cutoff + 1, 25):
        for signed_m in (m, -m):
            component = mp.fsum(
                qw_entry(signed_m, n, length) * value
                for n, value in coefficients.items()
            )
            sampled += abs(component) ** 2
    assert sampled <= weighted_candidate_tail_bound(
        coefficients, cutoff, length
    )

    # If an even candidate has zero endpoint sum, Theorem V improves the
    # generic O(1/K) squared tail to O(log(K)^2/K^3).
    zero_boundary = {
        -1: mp.mpf("1"),
        0: mp.mpf("-2"),
        1: mp.mpf("1"),
    }
    cutoff = 4
    sampled = mp.mpf("0")
    for m in range(cutoff + 1, 25):
        for signed_m in (m, -m):
            component = mp.fsum(
                qw_entry(signed_m, n, length) * value
                for n, value in zero_boundary.items()
            )
            sampled += abs(component) ** 2
    accelerated = boundary_vanishing_candidate_tail_bound(
        zero_boundary, cutoff, length
    )
    second_order = second_order_candidate_tail_bound(
        zero_boundary, cutoff, length
    )
    third_order = third_order_candidate_tail_bound(
        zero_boundary, cutoff, length
    )
    finite_phase = finite_phase_third_order_candidate_tail_bound(
        zero_boundary, cutoff, 12, length
    )
    fourth_order = fourth_order_candidate_tail_bound(
        zero_boundary, cutoff, 12, length
    )
    all_orders = all_orders_candidate_tail_bound(
        zero_boundary, cutoff, 12, 6, length
    )
    generic = weighted_candidate_tail_bound(zero_boundary, cutoff, length)
    assert sampled <= accelerated <= generic
    assert sampled <= second_order
    assert sampled <= third_order
    assert sampled <= finite_phase
    assert finite_phase <= third_order
    assert sampled <= fourth_order
    assert sampled <= all_orders
    assert all_orders <= fourth_order

    for m in (5, 9, 17, -5):
        direct_component = mp.fsum(
            qw_entry(m, n, length) * value
            for n, value in zero_boundary.items()
        )
        assert mp.almosteq(
            direct_component,
            exact_resolvent_tail_component(zero_boundary, m, length),
            rel_eps=mp.mpf("1e-50"),
            abs_eps=mp.mpf("1e-50"),
        )

    # The signed fourth-order coefficient is checked separately, so a loose
    # final squared-tail majorant cannot conceal a sign transcription error.
    leading = candidate_leading_coefficient(zero_boundary, length)
    fourth = candidate_fourth_order_coefficient(zero_boundary, length)
    fourth_absolute_moment = mp.fsum(
        abs(value) * abs(n) ** 4 for n, value in zero_boundary.items()
    )
    p_mass = prime_mass(length)
    support_radius = 1
    for m in (5, 9, 17):
        actual = mp.fsum(
            qw_entry(m, n, length) * value
            for n, value in zero_boundary.items()
        )
        expansion = (
            leading["combined"] / m**2
            + third_order_oscillatory_coefficient(
                zero_boundary, m, length
            )
            / m**3
            + fourth["combined"] / m**4
        )
        theorem_af = (
            abs(leading["pole"]) * length**4
            / (256 * mp.pi**4 * m**6)
            + fourth_absolute_moment
            * (
                lam * (1 + mp.log(mp.pi * (m - support_radius)))
                + 2 * p_mass
            )
            / (mp.pi * m**4 * (m - support_radius))
        )
        assert abs(actual - expansion) <= theorem_af

    near_boundary = dict(zero_boundary)
    near_boundary[0] += mp.mpf("1e-8")
    hybrid = hybrid_even_candidate_tail_bound(near_boundary, cutoff, length)
    generic = weighted_candidate_tail_bound(near_boundary, cutoff, length)
    sampled_near = mp.mpf("0")
    for m in range(cutoff + 1, 25):
        for signed_m in (m, -m):
            component = mp.fsum(
                qw_entry(signed_m, n, length) * value
                for n, value in near_boundary.items()
            )
            sampled_near += abs(component) ** 2
    assert sampled_near <= hybrid <= generic

    print("QW formula, row-tail, and candidate-tail sanity checks passed.")


if __name__ == "__main__":
    main()
