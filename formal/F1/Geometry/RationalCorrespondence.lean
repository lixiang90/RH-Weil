import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic.Linarith

/-! Local complex-torus equations. No identification with arithmetic Ψ is assumed. -/

namespace RHWeil.F1

def RationalGraph (m n : ℕ) (z w : ℂˣ) : Prop :=
  w ^ n = z ^ m

theorem parametrization_mem (m n : ℕ) (t : ℂˣ) :
    RationalGraph m n (t ^ n) (t ^ m) := by
  dsimp [RationalGraph]
  simp only [← pow_mul, Nat.mul_comm m n]

theorem compose_integer_graphs {m r : ℕ} {z w v : ℂˣ}
    (h₁ : RationalGraph m 1 z w) (h₂ : RationalGraph r 1 w v) :
    RationalGraph (m * r) 1 z v := by
  simp only [RationalGraph, pow_one] at *
  rw [h₂, h₁, ← pow_mul]

theorem two_three_six {z w v : ℂˣ}
    (h₂ : RationalGraph 2 1 z w) (h₃ : RationalGraph 3 1 w v) :
    RationalGraph 6 1 z v := by
  exact compose_integer_graphs h₂ h₃

/-- The local tropical shadow, not yet the arithmetic correspondence. -/
def rationalShadow (m n : ℕ) (x y : ℝ) : ℝ :=
  max (-(n : ℝ) * y) (-(m : ℝ) * x)

theorem shadow_on_graph (m n : ℕ) (x y : ℝ) (h : (n : ℝ) * y = m * x) :
    rationalShadow m n x y = -(m : ℝ) * x := by
  unfold rationalShadow
  have h' : -(n : ℝ) * y = -(m : ℝ) * x := by linarith
  rw [h', max_self]

end RHWeil.F1
