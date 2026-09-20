import Mathlib.Algebra.Module.LinearMap.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-!
Algebraic bookkeeping for note 405. All geometric/analytic identifications are
explicit hypotheses. This module does not construct a principal-divisor theory.
-/
namespace RHWeil.F1

variable {E : Type*} [AddCommGroup E] [Module ℝ E]

/-- The arithmetic pairing retains the two moment terms omitted by a spectral trace. -/
noncomputable def momentCorrectedPairing
    (d c : E →ₗ[ℝ] ℝ) (T : E → E → ℝ) (x y : E) : ℝ :=
  (d x * c y + c x * d y - T x y) / 2

theorem momentCorrectedPairing_radical
    (d c : E →ₗ[ℝ] ℝ) (T : E → E → ℝ) (p : E)
    (hd : d p = 0) (hc : c p = 0)
    (ht : ∀ y, T p y = 0 ∧ T y p = 0) :
    ∀ y, momentCorrectedPairing d c T p y = 0 ∧
      momentCorrectedPairing d c T y p = 0 := by
  intro y
  simp [momentCorrectedPairing, hd, hc, (ht y).1, (ht y).2]

theorem quarterMoments_self_pairing
    (d c : E →ₗ[ℝ] ℝ) (T : E → E → ℝ) (v : E)
    (hd : d v = 1 / 4) (hc : c v = 1 / 4) (ht : T v v = 0) :
    momentCorrectedPairing d c T v v = 1 / 16 := by
  norm_num [momentCorrectedPairing, hd, hc, ht]

theorem quarterMoments_not_radical
    (d c : E →ₗ[ℝ] ℝ) (T : E → E → ℝ) (v : E)
    (hd : d v = 1 / 4) (hc : c v = 1 / 4) (ht : T v v = 0) :
    ¬ (∀ y, momentCorrectedPairing d c T v y = 0) := by
  intro h
  have hv := quarterMoments_self_pairing d c T v hd hc ht
  have hz := h v
  rw [hv] at hz
  norm_num at hz

theorem degree_basis_moments (d c : E →ₗ[ℝ] ℝ) (v w : E)
    (hdv : d v = 1 / 4) (hcv : c v = 1 / 4)
    (hdw : d w = 1 / 2) (hcw : c w = 1 / 4) :
    d (4 • (w - v)) = 1 ∧ c (4 • (w - v)) = 0 := by
  norm_num [map_smul, map_sub, hdv, hcv, hdw, hcw, smul_eq_mul]

theorem codegree_basis_moments (d c : E →ₗ[ℝ] ℝ) (v w : E)
    (hdv : d v = 1 / 4) (hcv : c v = 1 / 4)
    (hdw : d w = 1 / 2) (hcw : c w = 1 / 4) :
    d (8 • v - 4 • w) = 0 ∧ c (8 • v - 4 • w) = 1 := by
  norm_num [map_smul, map_sub, hdv, hcv, hdw, hcw, smul_eq_mul]

theorem remove_two_moments (d c : E →ₗ[ℝ] ℝ) (u v f : E)
    (hdu : d u = 1) (hcu : c u = 0)
    (hdv : d v = 0) (hcv : c v = 1) :
    d (f - d f • u - c f • v) = 0 ∧
    c (f - d f • u - c f • v) = 0 := by
  simp [map_smul, map_sub, hdu, hcu, hdv, hcv, smul_eq_mul]

theorem two_moment_coordinates_unique (d c : E →ₗ[ℝ] ℝ) (u v : E)
    (hdu : d u = 1) (hcu : c u = 0)
    (hdv : d v = 0) (hcv : c v = 1) (a b : ℝ)
    (h : a • u + b • v = 0) : a = 0 ∧ b = 0 := by
  constructor
  · have h' := congrArg d h
    simpa [map_add, map_smul, hdu, hdv, smul_eq_mul] using h'
  · have h' := congrArg c h
    simpa [map_add, map_smul, hcu, hcv, smul_eq_mul] using h'


/-- Inside the spectral trace kernel, the full pairing has exactly the zero-moment radical. -/
theorem trace_kernel_radical_iff_moments
    (d c : E →ₗ[ℝ] ℝ) (T : E → E → ℝ) (p u v : E)
    (hdu : d u = 1) (hcu : c u = 0)
    (hdv : d v = 0) (hcv : c v = 1)
    (ht : ∀ y, T p y = 0) :
    (∀ y, momentCorrectedPairing d c T p y = 0) ↔ d p = 0 ∧ c p = 0 := by
  constructor
  · intro h
    have hu : c p / 2 = 0 := by
      simpa [momentCorrectedPairing, hdu, hcu, ht u] using h u
    have hv : d p / 2 = 0 := by
      simpa [momentCorrectedPairing, hdv, hcv, ht v] using h v
    constructor
    · have h' := (div_eq_iff (by norm_num : (2 : ℝ) ≠ 0)).mp hv
      simpa using h'
    · have h' := (div_eq_iff (by norm_num : (2 : ℝ) ≠ 0)).mp hu
      simpa using h'
  · rintro ⟨hd, hc⟩ y
    simp [momentCorrectedPairing, hd, hc, ht y]

end RHWeil.F1
