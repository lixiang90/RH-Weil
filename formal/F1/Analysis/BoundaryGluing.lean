import Mathlib.Data.Finsupp.Defs
import Mathlib.Data.Finset.Max
import Mathlib.Data.Real.Basic
import Lean.Elab.Tactic.Omega
import Mathlib.Tactic.Ring

/-! Algebra used by the two-place extension calculation.
No C*-algebra, Morita, PV, Bott, quotient topology or geometric existence
claim is encoded by these elementary consequences. -/
namespace RHWeil.F1

theorem finiteShiftInvariant_zero {M : Type*} [Zero M]
    (f : ℤ →₀ M) (h : ∀ j : ℤ, f (j + 1) = f j) : f = 0 := by
  classical
  by_contra hn
  have hs : f.support.Nonempty := Finsupp.support_nonempty_iff.mpr hn
  let m := f.support.max' hs
  have hm : m ∈ f.support := Finset.max'_mem _ _
  have hnext : m + 1 ∉ f.support := by
    intro hmem
    have hle := Finset.le_max' f.support (m + 1) hmem
    change m + 1 ≤ m at hle
    omega
  have hz : f (m + 1) = 0 := by simpa using hnext
  have hnonzero : f m ≠ 0 := by simpa using hm
  exact hnonzero ((h m).symm.trans hz)

def boundaryRank (v : ℤ × ℤ) : ℤ := -(v.1 + v.2)

theorem boundaryRank_kernel (a b : ℤ) :
    boundaryRank (a, b) = 0 ↔ a = -b := by
  simp only [boundaryRank]
  omega

theorem boundaryRank_surjective : Function.Surjective boundaryRank := by
  intro n
  exact ⟨(-n, 0), by simp [boundaryRank]⟩

theorem boundaryRank_positive_zero (a b : ℤ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (h : boundaryRank (a, b) = 0) : a = 0 ∧ b = 0 := by
  simp only [boundaryRank] at h
  omega

theorem boundaryRank_signed_iff (a b : ℤ) :
    boundaryRank (a, -b) = 0 ↔ a = b := by
  simp [boundaryRank_kernel]

theorem unequalLength_residual (m L M : ℝ) (hm : m ≠ 0) (hLM : L ≠ M) :
    m * L - m * M ≠ 0 := by
  rw [← mul_sub]
  exact mul_ne_zero hm (sub_ne_zero.mpr hLM)

theorem cyclicDegrees_determinant (m n d c : ℝ) :
    (m * d) * (n * c) - (n * d) * (m * c) = 0 := by
  ring

end RHWeil.F1
