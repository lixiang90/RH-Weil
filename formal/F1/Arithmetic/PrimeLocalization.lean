import Mathlib.Algebra.Ring.Subring.Basic
import Mathlib.Algebra.Order.GroupWithZero.WithZero
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Data.Nat.Prime.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Positivity

/-! The ordered prime-local monoid in note 363. No RH assumptions occur here. -/

namespace RHWeil.F1

/-- The subring Z[1/p] inside Q. -/
def primeLocalization (p : ℕ) : Subring ℚ :=
  Subring.closure {((p : ℚ)⁻¹)}

theorem inverse_mem_primeLocalization (p : ℕ) :
    (p : ℚ)⁻¹ ∈ primeLocalization p :=
  Subring.subset_closure (by simp)

/-- Nonnegative exponents for the pointed monoid F₁[T^(Z[1/p]₊)]. -/
def primeCone (p : ℕ) : AddSubmonoid ℚ where
  carrier := {q | q ∈ primeLocalization p ∧ 0 ≤ q}
  zero_mem' := ⟨(primeLocalization p).zero_mem, le_rfl⟩
  add_mem' ha hb := ⟨(primeLocalization p).add_mem ha.1 hb.1, add_nonneg ha.2 hb.2⟩

/-- This ordinary pointed commutative monoid is not the whole spherical algebra. -/
abbrev PrimeStalk (p : ℕ) := WithZero (Multiplicative (primeCone p))

theorem div_prime_mem {p : ℕ} (hp : 0 < p) {q : ℚ} (hq : q ∈ primeCone p) :
    q / p ∈ primeCone p := by
  constructor
  · exact (primeLocalization p).mul_mem hq.1 (inverse_mem_primeLocalization p)
  · exact div_nonneg hq.2 (by positivity)

/-- Multiplication by p is surjective on its own nonnegative local cone. -/
theorem prime_scaling_surjective {p : ℕ} (hp : 0 < p) :
    ∀ q : ℚ, q ∈ primeCone p →
      ∃ r : ℚ, r ∈ primeCone p ∧ (p : ℚ) * r = q := by
  intro q hq
  refine ⟨q / p, div_prime_mem hp hq, ?_⟩
  have hpq : (p : ℚ) ≠ 0 := by positivity
  field_simp

/-- BP-ARITH-02: classical localization normal form; formalization gap, not a new conjecture. -/
theorem mem_primeLocalization_iff (p : ℕ) (hp : p.Prime) (q : ℚ) :
    q ∈ primeLocalization p ↔ ∃ a : ℤ, ∃ n : ℕ, q = (a : ℚ) / (p : ℚ) ^ n := by
  sorry

end RHWeil.F1
