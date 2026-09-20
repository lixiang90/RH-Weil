import Mathlib.Analysis.Calculus.ContDiff.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Measure.Haar.OfBasis
import Mathlib.Analysis.SpecialFunctions.Exp

/-! Shared test functions, moments, reflection and convolution for the F1 analysis. -/
namespace RHWeil.F1

open scoped ContDiff

structure TestFunction where
  toFun : ℝ → ℝ
  smooth : ContDiff ℝ ∞ toFun
  compactSupport : HasCompactSupport toFun

instance : CoeFun TestFunction (fun _ => ℝ → ℝ) := ⟨TestFunction.toFun⟩

noncomputable def degreeMoment (f : TestFunction) : ℝ :=
  ∫ x : ℝ, Real.exp x * f x

noncomputable def codegreeMoment (f : TestFunction) : ℝ :=
  ∫ x : ℝ, f x

def ZeroMoments (f : TestFunction) : Prop :=
  degreeMoment f = 0 ∧ codegreeMoment f = 0

noncomputable def reflected (f : ℝ → ℝ) (x : ℝ) : ℝ :=
  Real.exp (-x) * f (-x)

noncomputable def logConvolution (f g : ℝ → ℝ) (x : ℝ) : ℝ :=
  ∫ t : ℝ, f t * g (x - t)

end RHWeil.F1
