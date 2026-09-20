import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic
import Lean.Elab.Tactic.Omega
import Mathlib.Tactic.Ring

/-! Elementary identities used by the explicit boundary-index computation.
The sequence identities do not assert boundedness on Hilbert spaces.
No C*-algebra, Fredholm index, topology or arithmetic realization is formalized here. -/
namespace RHWeil.F1
open scoped BigOperators

def positiveTailShift {M : Type*} [Zero M] (f : ℤ → M) (n : ℤ) : M :=
  if n < 0 then f n else if n = 0 then 0 else f (n - 1)

def positiveTailBack {M : Type*} (f : ℤ → M) (n : ℤ) : M :=
  if n < 0 then f n else f (n + 1)

theorem positiveTail_leftInverse {M : Type*} [Zero M] (f : ℤ → M) :
    positiveTailBack (positiveTailShift f) = f := by
  funext n
  by_cases hn : n < 0
  · simp [positiveTailBack, positiveTailShift, hn]
  · have hp : ¬ n + 1 < 0 := by omega
    have hz : n + 1 ≠ 0 := by omega
    simp [positiveTailBack, positiveTailShift, hn, hp, hz]

theorem positiveTail_rankOneDefect {M : Type*} [AddGroup M] (f : ℤ → M) (n : ℤ) :
    positiveTailShift (positiveTailBack f) n =
      f n - if n = 0 then f 0 else 0 := by
  by_cases hn : n < 0
  · have hz : n ≠ 0 := by omega
    simp [positiveTailShift, positiveTailBack, hn, hz]
  · by_cases hz : n = 0
    · subst n
      simp [positiveTailShift]
    · have hp : ¬ n - 1 < 0 := by omega
      simp [positiveTailShift, positiveTailBack, hn, hz, hp]

theorem positiveTail_injective {M : Type*} [Zero M] :
    Function.Injective (@positiveTailShift M _) := by
  intro f g h
  have h' := congrArg positiveTailBack h
  simpa only [positiveTail_leftInverse] using h'

theorem finiteFlux (a : ℕ → ℝ) (n : ℕ) :
    (∑ k ∈ Finset.range n, (a (k + 1) - a k)) = a n - a 0 := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    ring

theorem finiteFlux_one_to_zero (a : ℕ → ℝ) (n : ℕ)
    (h0 : a 0 = 1) (hn : a n = 0) :
    (∑ k ∈ Finset.range n, (a (k + 1) - a k)) = -1 := by
  rw [finiteFlux, h0, hn]
  ring

theorem weightedFiniteFlux (a w : ℕ → ℝ) (n : ℕ) :
    (∑ k ∈ Finset.range n, w k * (a (k + 1) - a k)) =
      w n * a n - w 0 * a 0 -
      ∑ k ∈ Finset.range n, (w (k + 1) - w k) * a (k + 1) := by
  induction n with
  | zero => simp
  | succ n ih =>
    simp only [Finset.sum_range_succ]
    rw [ih]
    ring

end RHWeil.F1
