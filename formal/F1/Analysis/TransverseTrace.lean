import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-! Geometric overlap of a normalized half-line tail, and obstructions to
reading its powers by a fixed affine/additive index pairing.
The p-adic Hilbert space, bundle and trace-class operators are paper constructions. -/
namespace RHWeil.F1

theorem coherentTail_hasSum (r : ℝ) (hr0 : 0 ≤ r) (hr1 : r < 1) (a : ℕ) :
    HasSum (fun n : ℕ => (1 - r ^ 2) * r ^ n * r ^ (n + a)) (r ^ a) := by
  have hr2 : r ^ 2 < 1 := by nlinarith
  have hne : 1 - r ^ 2 ≠ 0 := by linarith
  have h := (hasSum_geometric_of_lt_one (sq_nonneg r) hr2).mul_left
    ((1 - r ^ 2) * r ^ a)
  have hf : (fun n : ℕ => (1 - r ^ 2) * r ^ n * r ^ (n + a)) =
      (fun n : ℕ => (1 - r ^ 2) * r ^ a * (r ^ 2) ^ n) := by
    funext n
    simp only [pow_add]
    ring
  have hv : (1 - r ^ 2) * r ^ a * (1 - r ^ 2)⁻¹ = r ^ a := by
    field_simp
  rw [hf]
  rw [hv] at h
  exact h

theorem coherentTail_normalized (r : ℝ) (hr0 : 0 ≤ r) (hr1 : r < 1) :
    HasSum (fun n : ℕ => (1 - r ^ 2) * (r ^ n) ^ 2) 1 := by
  simpa [pow_two, mul_assoc] using coherentTail_hasSum r hr0 hr1 0

theorem coherentTail_overlap (r : ℝ) (hr0 : 0 ≤ r) (hr1 : r < 1) (a : ℕ) :
    (∑' n : ℕ, (1 - r ^ 2) * r ^ n * r ^ (n + a)) = r ^ a :=
  (coherentTail_hasSum r hr0 hr1 a).tsum_eq

theorem affine_secondDifference (x b : ℝ) (a : ℕ) :
    (((a + 2 : ℕ) : ℝ) * x + b) -
      2 * (((a + 1 : ℕ) : ℝ) * x + b) + ((a : ℝ) * x + b) = 0 := by
  push_cast
  ring

theorem geometric_secondDifference (r : ℝ) (a : ℕ) :
    r ^ (a + 2) - 2 * r ^ (a + 1) + r ^ a = r ^ a * (r - 1) ^ 2 := by
  simp only [pow_add, pow_one]
  ring

theorem coherentTail_not_affine (r : ℝ) (hr0 : 0 < r) (hr1 : r < 1)
    (x b : ℝ) :
    ¬ (x + b = r ∧ 2 * x + b = r ^ 2 ∧ 3 * x + b = r ^ 3) := by
  rintro ⟨h1, h2, h3⟩
  have hp : 0 < r * (r - 1) ^ 2 := mul_pos hr0 (sq_pos_of_ne_zero (by linarith))
  have hd := geometric_secondDifference r 1
  norm_num at hd
  nlinarith

theorem commonMixedTerm_weight (x y b w v : ℝ)
    (h1 : x + b = w) (h2 : 2 * x + b = w)
    (h3 : y + b = v) (h4 : 2 * y + b = v) : w = v := by
  linarith

end RHWeil.F1
