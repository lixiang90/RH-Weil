import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Data.Int.GCD

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

/-- Parameterization of the complex unit-point graph. -/
def graphParam (m n : ℕ) (t : ℂˣ) :
    {p : ℂˣ × ℂˣ // RationalGraph m n p.1 p.2} :=
  ⟨(t ^ n, t ^ m), parametrization_mem m n t⟩

theorem graphParam_injective {m n : ℕ} (hmn : m.Coprime n) :
    Function.Injective (graphParam m n) := by
  intro s t h
  have hn : s ^ n = t ^ n := congrArg (fun p => p.val.1) h
  have hm : s ^ m = t ^ m := congrArg (fun p => p.val.2) h
  have hq : (s / t) ^ m = 1 ∧ (s / t) ^ n = 1 := by
    constructor
    · rw [div_pow, hm, div_self']
    · rw [div_pow, hn, div_self']
  exact div_eq_one.mp ((pow_eq_one_iff_of_coprime hmn).mp hq)

/-- Existence follows from mathlib's Bezout power lemma; n > 0 keeps the
chosen complex parameter nonzero. No scheme structure is asserted. -/
theorem graphParam_surjective {m n : ℕ} (hmn : m.Coprime n) (hn : 0 < n) :
    Function.Surjective (graphParam m n) := by
  rintro ⟨⟨z, w⟩, h⟩
  have hh : (w : ℂ) ^ n = (z : ℂ) ^ m := by
    simpa only [Units.val_pow_eq_pow_val] using congrArg (fun u : ℂˣ => (u : ℂ)) h
  obtain ⟨c, hw, hz⟩ := (pow_eq_pow_iff_of_coprime hmn.symm).mp hh
  have hc : c ≠ 0 := by
    intro hc
    apply z.ne_zero
    rw [hz, hc, zero_pow (Nat.ne_of_gt hn)]
  refine ⟨Units.mk0 c hc, ?_⟩
  apply Subtype.ext
  apply Prod.ext
  · apply Units.ext
    simpa only [graphParam, Units.val_pow_eq_pow_val, Units.val_mk0] using hz.symm
  · apply Units.ext
    simpa only [graphParam, Units.val_pow_eq_pow_val, Units.val_mk0] using hw.symm

/-- A genuine equivalence of point sets. The inverse uses classical choice;
regularity, projection degrees and comparison with arithmetic Psi remain open nodes. -/
noncomputable def graphEquiv {m n : ℕ} (hmn : m.Coprime n) (hn : 0 < n) :
    ℂˣ ≃ {p : ℂˣ × ℂˣ // RationalGraph m n p.1 p.2} :=
  Equiv.ofBijective (graphParam m n) ⟨graphParam_injective hmn, graphParam_surjective hmn hn⟩

end RHWeil.F1
