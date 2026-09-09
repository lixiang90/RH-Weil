import Mathlib.MeasureTheory.Integral.CircleAverage
import Mathlib.Analysis.Meromorphic.Basic
import Mathlib.Analysis.Calculus.ContDiff.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Log
import Mathlib.Data.Finsupp.Basic
import Mathlib.Algebra.BigOperators.Finsupp.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-! Actual circle integrals and the finite lifting formula of note 363 §4.
The admitted analytic identities are classical formalization tasks, not RH inputs.
-/

namespace RHWeil.F1

open scoped ContDiff

noncomputable def circlePoint (x θ : ℝ) : ℂ :=
  Complex.exp (((-x : ℝ) : ℂ) + (θ : ℂ) * Complex.I)

noncomputable def jensen (G : ℂ → ℂ) (x : ℝ) : ℝ :=
  Real.circleAverage (fun z => Real.log ‖G z‖) 0 (Real.exp (-x))

structure FiniteProfile where
  constant : ℝ
  slope : ℤ
  jumps : ℝ →₀ ℤ

noncomputable def FiniteProfile.value (P : FiniteProfile) (x : ℝ) : ℝ :=
  P.constant + (P.slope : ℝ) * x +
    P.jumps.sum (fun a n => (n : ℝ) * max (x - a) 0)

noncomputable def FiniteProfile.lift (P : FiniteProfile) (z : ℂ) : ℂ :=
  Complex.exp (P.constant : ℂ) *
    z ^ (-(P.slope + P.jumps.sum (fun _ n => n))) *
    P.jumps.prod (fun a n => (z - Complex.exp ((-a : ℝ) : ℂ)) ^ n)

/-- BP-JENSEN-00. Excludes accidental use of the nonintegrable default value. -/
theorem finiteLift_circleIntegrable (P : FiniteProfile) (x : ℝ) :
    CircleIntegrable (fun z => Real.log ‖P.lift z‖) 0 (Real.exp (-x)) := by
  sorry

/-- BP-JENSEN-01. Includes integrability at finitely many zero/pole angles.
At pole points Lean's totalized zpow has a value, irrelevant to the integral.
-/
theorem jensen_finite_lift (P : FiniteProfile) (x : ℝ) :
    jensen P.lift x = P.value x := by
  sorry

/-- BP-JENSEN-04: weak derivatives retain the breakpoint atoms.
Compact support removes boundary terms; no pointwise second derivative is used.
-/
theorem finiteProfile_weakSecond (P : FiniteProfile) (φ : ℝ → ℝ)
    (hφ : ContDiff ℝ ∞ φ) (hc : HasCompactSupport φ) :
    (∫ x : ℝ, P.value x * deriv (deriv φ) x) =
      P.jumps.sum (fun a n => (n : ℝ) * φ a) := by
  sorry

/-- BP-JENSEN-02: the two signs have the same circular mean. -/
theorem jensen_one_add_and_sub (x : ℝ) :
    jensen (fun z => 1 + z) x = max 0 (-x) ∧
    jensen (fun z => 1 - z) x = max 0 (-x) := by
  sorry

/-- Integral normalization for a nonzero constant. -/
theorem jensen_const_two (x : ℝ) :
    jensen (fun _ => (2 : ℂ)) x = Real.log 2 := by
  simp [jensen, Real.circleAverage_const]

theorem jensen_not_max_additive :
    jensen (fun z => (1 + z) + (1 - z)) 1 ≠
      max (jensen (fun z => 1 + z) 1) (jensen (fun z => 1 - z) 1) := by
  have hfun : (fun z : ℂ => (1 + z) + (1 - z)) = (fun _ => (2 : ℂ)) := by
    funext z
    ring
  rw [hfun, jensen_const_two, (jensen_one_add_and_sub 1).1,
    (jensen_one_add_and_sub 1).2]
  norm_num

end RHWeil.F1
