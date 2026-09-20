import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Data.Complex.Basic

/-!
Algebraic checks for the finite-chain inverse and backward-shift right inverse
in note 409. Analytic boundedness, infinite sums, kernels and adelic geometry
are separate paper proofs; these lemmas contain no such implicit assumptions.
-/
namespace RHWeil.F1
open scoped BigOperators

theorem nilpotentGeometric_right {A : Type*} [Ring A] (T : A) (n : ℕ)
    (hn : T ^ n = 0) :
    (∑ k ∈ Finset.range n, T ^ k) * (1 - T) = 1 := by
  simpa [hn] using geom_sum_mul_neg T n

theorem nilpotentGeometric_left {A : Type*} [Ring A] (T : A) (n : ℕ)
    (hn : T ^ n = 0) :
    (1 - T) * (∑ k ∈ Finset.range n, T ^ k) = 1 := by
  simpa [hn] using mul_neg_geom_sum T n

variable {A : Type*} [Ring A] [Algebra ℂ A]

theorem backwardResolvent_factor (B S : A) (z : ℂ)
    (hBS : B * S = 1) (hz : z ≠ 0) :
    1 - z • B = (-z) • (B * (1 - z⁻¹ • S)) := by
  rw [mul_sub, mul_one, mul_smul_comm, smul_sub, smul_smul, hBS]
  simp [hz, neg_smul, sub_eq_add_neg, add_comm]

theorem backwardResolvent_rightInverse (B S V : A) (z : ℂ)
    (hBS : B * S = 1) (hz : z ≠ 0)
    (hV : (1 - z⁻¹ • S) * V = 1) :
    (1 - z • B) * ((-z⁻¹) • (V * S)) = 1 := by
  rw [backwardResolvent_factor B S z hBS hz]
  rw [smul_mul_assoc, mul_smul_comm, smul_smul]
  have h : (B * (1 - z⁻¹ • S)) * (V * S) = 1 := by
    calc
      _ = B * (((1 - z⁻¹ • S) * V) * S) := by simp only [mul_assoc]
      _ = 1 := by rw [hV, one_mul, hBS]
  rw [h]
  simp [hz]

end RHWeil.F1
