import Mathlib.Algebra.Algebra.Basic

/-!
Defect algebra for a left inverse B*V=1 (B=V* in the isometry application).
These statements verify the wandering-defect direction and its power sectors.
Hilbert norms, convergence, C*-quotients, traces and K-theory remain paper proofs.
-/
namespace RHWeil.F1
variable {A : Type*} [Ring A]

theorem leftInverseDefect_mul (B V : A) (h : B * V = 1) :
    (1 - V * B) * V = 0 := by
  rw [sub_mul, one_mul, mul_assoc, h, mul_one, sub_self]

theorem leftInverseDefect_left (B V : A) (h : B * V = 1) :
    B * (1 - V * B) = 0 := by
  rw [mul_sub, mul_one, ← mul_assoc, h, one_mul, sub_self]

theorem leftInverseDefect_idempotent (B V : A) (h : B * V = 1) :
    (1 - V * B) * (1 - V * B) = 1 - V * B := by
  calc
    _ = (1 - V * B) - ((1 - V * B) * V) * B := by
      rw [mul_sub, mul_one, ← mul_assoc]
    _ = _ := by rw [leftInverseDefect_mul B V h, zero_mul, sub_zero]

theorem leftInverse_powers (B V : A) (h : B * V = 1) (n : ℕ) :
    B ^ n * V ^ n = 1 := by
  induction n with
  | zero => simp
  | succ n ih =>
    calc
      B ^ (n + 1) * V ^ (n + 1) =
          B ^ n * ((B * V) * V ^ n) := by
            rw [pow_succ, pow_succ']
            simp only [mul_assoc]
      _ = 1 := by rw [h, one_mul, ih]

theorem leftInverseDefect_distinctPowers (B V : A) (h : B * V = 1)
    (m n : ℕ) :
    (1 - V * B) *
      (B ^ m * (V ^ (m + (n + 1)) * (1 - V * B))) = 0 := by
  calc
    _ = (1 - V * B) *
        ((B ^ m * V ^ m) * (V ^ (n + 1) * (1 - V * B))) := by
          rw [pow_add]
          simp only [mul_assoc]
    _ = (1 - V * B) * (V ^ (n + 1) * (1 - V * B)) := by
          rw [leftInverse_powers B V h, one_mul]
    _ = ((1 - V * B) * V) * (V ^ n * (1 - V * B)) := by
          rw [pow_succ']
          simp only [mul_assoc]
    _ = 0 := by rw [leftInverseDefect_mul B V h, zero_mul]

theorem leftInverseDefect_ne_zero (B V : A) (h : V * B ≠ 1) :
    1 - V * B ≠ 0 := by
  intro hz
  exact h (sub_eq_zero.mp hz).symm

end RHWeil.F1
