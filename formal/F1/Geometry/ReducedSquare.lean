import Mathlib.Analysis.Convex.Hull
import Mathlib.Data.Finset.Lattice.Basic
import Mathlib.Data.Real.Basic

/-! Finite Newton presentations and equality of their positive support functions.
The comparison with Connes--Consani's reduced square is explicitly separate.
-/

namespace RHWeil.F1

abbrev NewtonPresentation := Finset (ℤ × ℤ)

noncomputable def newtonValue (S : NewtonPresentation) (x y : ℝ) : WithTop ℝ :=
  S.inf (fun a => (((a.1 : ℝ) * x + (a.2 : ℝ) * y : ℝ) : WithTop ℝ))

def NewtonEquivalent (S T : NewtonPresentation) : Prop :=
  ∀ x y : ℝ, 0 < x → 0 < y → newtonValue S x y = newtonValue T x y

def newtonSetoid : Setoid NewtonPresentation where
  r := NewtonEquivalent
  iseqv := {
    refl := fun _ _ _ _ _ => rfl
    symm := fun h x y hx hy => (h x y hx hy).symm
    trans := fun h₁ h₂ x y hx hy => (h₁ x y hx hy).trans (h₂ x y hx hy) }

/-- Candidate presentation, not a claim to have formalized the whole ringed topos. -/
abbrev ReducedNewtonSquare := Quotient newtonSetoid

def upperNewtonHull (S : NewtonPresentation) : Set (ℝ × ℝ) :=
  {z | ∃ u ∈ convexHull ℝ
      ((fun a : ℤ × ℤ => ((a.1 : ℝ), (a.2 : ℝ))) '' (S : Set (ℤ × ℤ))),
      ∃ v : ℝ × ℝ, 0 ≤ v ∧ z = u + v}

/-- BP-SQUARE-01: finite convex separation, including the empty presentation. -/
theorem newtonEquivalent_iff_hull (S T : NewtonPresentation) :
    NewtonEquivalent S T ↔ upperNewtonHull S = upperNewtonHull T := by
  sorry

end RHWeil.F1
