import Mathlib.NumberTheory.LSeries.RiemannZeta
import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt
import Mathlib.NumberTheory.Harmonic.EulerMascheroni
import F1.Analysis.TestFunctions

/-! The arithmetic quadratic form is fixed by primes and the archimedean term.
Coordinates are x = log u here, unlike the Jensen coordinate -log |z|.
Source: Connes--Consani arXiv:1805.10501v1, §3, equations (12)--(14).
-/

namespace RHWeil.F1

noncomputable def arithmeticDistribution (h : ℝ → ℝ) : ℝ :=
  (∑' n : ℕ, ArithmeticFunction.vonMangoldt n * h (Real.log (n : ℝ))) +
  (∫ x in Set.Ioi (0 : ℝ),
    (Real.exp (2 * x) * h x - h 0) / (Real.exp (2 * x) - 1)) +
  (Real.log Real.pi + Real.eulerMascheroniConstant) / 2 * h 0

noncomputable def weilSelf (f : TestFunction) : ℝ :=
  arithmeticDistribution (logConvolution f (reflected f))

/-- BP-WEIL-00: convergence obligations for the actual test class.
These keep totalized integrals and sums from concealing missing analysis. -/
theorem weil_convergence (f : TestFunction) :
    (∀ x : ℝ, MeasureTheory.Integrable
      (fun t : ℝ => f t * reflected f (x - t))) ∧
    Summable (fun n : ℕ => ArithmeticFunction.vonMangoldt n *
      logConvolution f (reflected f) (Real.log (n : ℝ))) ∧
    MeasureTheory.IntegrableOn (fun x : ℝ =>
      (Real.exp (2 * x) * logConvolution f (reflected f) x -
        logConvolution f (reflected f) 0) / (Real.exp (2 * x) - 1))
      (Set.Ioi 0) := by
  sorry

def WeilNonpositive : Prop :=
  ∀ f : TestFunction, ZeroMoments f → weilSelf f ≤ 0

/-- BP-WEIL-01: classical analytic bridge still to be formalized.
This explicitly concerns mathlib's actual riemannZeta; it is not an RH proof.
The proof must establish convergence and check the source's normalization.
-/
theorem weilCriterion : WeilNonpositive ↔ RiemannHypothesis := by
  sorry

end RHWeil.F1
