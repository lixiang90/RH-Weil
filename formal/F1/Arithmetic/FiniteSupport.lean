import F1.Arithmetic.PrimeLocalization
import Mathlib.Data.Finsupp.Basic
import Mathlib.Data.Nat.Prime.Defs

/-! Finite-support coordinates before the Zariski sheaf comparison. -/

namespace RHWeil.F1

open scoped Classical

abbrev PrimeIndex := {p : ℕ // p.Prime}
abbrev ExponentData := PrimeIndex →₀ ℚ

/-- The coordinate constraints of a section over the set of closed primes U. -/
def IsSection (U : Set PrimeIndex) (a : ExponentData) : Prop :=
  (∀ p, a p ∈ primeCone p.val) ∧ (∀ p, p ∉ U → a p = 0)

noncomputable def restrict (U : Set PrimeIndex) (a : ExponentData) : ExponentData := by
  classical
  exact a.filter (fun p => p ∈ U)

@[simp] theorem restrict_apply (U : Set PrimeIndex) (a : ExponentData) (p : PrimeIndex) :
    restrict U a p = if p ∈ U then a p else 0 := by
  classical
  rfl

theorem restrict_isSection (U V : Set PrimeIndex) (a : ExponentData)
    (ha : IsSection U a) : IsSection V (restrict V a) := by
  classical
  constructor
  · intro p
    by_cases h : p ∈ V
    · simpa [h] using ha.1 p
    · simpa [h] using (primeCone p.val).zero_mem
  · intro p hp
    simp [hp]

theorem restrict_self (U : Set PrimeIndex) (a : ExponentData) (ha : IsSection U a) :
    restrict U a = a := by
  classical
  ext p
  by_cases hp : p ∈ U
  · simp [hp]
  · simp [hp, ha.2 p hp]

theorem restrict_restrict (U V : Set PrimeIndex) (hVU : V ⊆ U) (a : ExponentData) :
    restrict V (restrict U a) = restrict V a := by
  classical
  ext p
  by_cases hp : p ∈ V
  · simp [hp, hVU hp]
  · simp [hp]

end RHWeil.F1
