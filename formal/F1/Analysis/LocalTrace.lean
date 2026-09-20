import F1.Analysis.TestFunctions
import Mathlib.MeasureTheory.Integral.Bochner.Set

/-!
Reusable checks for note 404. These do not assert an adelic global trace formula.
The positivity below proves convergence from continuity and compact support,
without using the admitted theorem weil_convergence.
-/
namespace RHWeil.F1

open MeasureTheory

theorem reflected_involutive (f : ℝ → ℝ) :
    reflected (reflected f) = f := by
  funext x
  simp only [reflected, neg_neg]
  rw [← mul_assoc, ← Real.exp_add]
  simp

theorem reflected_fixed_neg (k : ℝ → ℝ) (hk : reflected k = k) (x : ℝ) :
    k (-x) = Real.exp x * k x := by
  have h := congrFun hk (-x)
  simpa only [reflected, neg_neg] using h.symm

theorem selfConvolution_at_zero (f : ℝ → ℝ) :
    logConvolution f (reflected f) 0 = ∫ t : ℝ, Real.exp t * (f t) ^ 2 := by
  unfold logConvolution
  apply integral_congr_ae
  filter_upwards [] with t
  simp only [reflected, zero_sub, neg_neg]
  rw [pow_two]
  exact mul_left_comm (f t) (Real.exp t) (f t)

theorem selfConvolution_at_zero_pos (f : ℝ → ℝ)
    (hc : Continuous f) (hs : HasCompactSupport f) (hn : ∃ x, f x ≠ 0) :
    0 < logConvolution f (reflected f) 0 := by
  rw [selfConvolution_at_zero]
  have hcont : Continuous (fun t : ℝ => Real.exp t * (f t) ^ 2) :=
    Real.continuous_exp.mul (hc.pow 2)
  have hcompact : HasCompactSupport (fun t : ℝ => Real.exp t * (f t) ^ 2) := by
    rw [hasCompactSupport_iff_eventuallyEq] at hs ⊢
    exact hs.mono fun t ht => by
      change f t = 0 at ht
      change Real.exp t * (f t) ^ 2 = 0
      simp only [ht, zero_pow (by decide : 2 ≠ 0), mul_zero]
  rcases hn with ⟨x, hx⟩
  exact hcont.integral_pos_of_hasCompactSupport_nonneg_nonzero hcompact
    (fun t => mul_nonneg (Real.exp_pos t).le (sq_nonneg (f t)))
    (ne_of_gt (mul_pos (Real.exp_pos x) (sq_pos_of_ne_zero hx)))

theorem test_selfConvolution_at_zero_pos (f : TestFunction) (hn : ∃ x, f x ≠ 0) :
    0 < logConvolution f (reflected f) 0 :=
  selfConvolution_at_zero_pos f f.smooth.continuous f.compactSupport hn

/-- Addition of c times evaluation at zero; no linearity of D is assumed. -/
noncomputable def withIdentityCorrection (D : (ℝ → ℝ) → ℝ) (c : ℝ)
    (k : ℝ → ℝ) : ℝ :=
  D k + c * k 0

theorem identityCorrection_eq_of_zero (D : (ℝ → ℝ) → ℝ) (c : ℝ)
    (k : ℝ → ℝ) (hk : k 0 = 0) :
    withIdentityCorrection D c k = D k := by
  simp [withIdentityCorrection, hk]

theorem identityCorrection_self_difference (D : (ℝ → ℝ) → ℝ) (c : ℝ)
    (f : ℝ → ℝ) :
    withIdentityCorrection D c (logConvolution f (reflected f)) -
      D (logConvolution f (reflected f)) =
        c * ∫ t : ℝ, Real.exp t * (f t) ^ 2 := by
  rw [withIdentityCorrection, add_sub_cancel_left, selfConvolution_at_zero]

theorem identityCorrection_self_ne (D : (ℝ → ℝ) → ℝ) (c : ℝ) (hc : c ≠ 0)
    (f : TestFunction) (hf : ∃ x, f x ≠ 0) :
    withIdentityCorrection D c (logConvolution f (reflected f)) ≠
      D (logConvolution f (reflected f)) := by
  intro h
  have hz : c * logConvolution f (reflected f) 0 = 0 := by
    exact add_left_cancel (show D (logConvolution f (reflected f)) +
        c * logConvolution f (reflected f) 0 =
        D (logConvolution f (reflected f)) + 0 by
      simpa only [withIdentityCorrection, add_zero] using h)
  exact (mul_ne_zero hc (ne_of_gt (test_selfConvolution_at_zero_pos f hf))) hz

end RHWeil.F1
