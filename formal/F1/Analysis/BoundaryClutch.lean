import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Logic.Function.Iterate
import Mathlib.Data.Complex.Basic
import Lean.Elab.Tactic.Omega

/-!
Algebraic checks for note 410: shift transport, the one-wrap phase,
a weighted permutation determinant, and the bounded integer drift obstruction.
Continuity, winding number, Fredholm theory, Morita equivalence and K-theory
are paper arguments, not hidden assumptions of these declarations.
-/
namespace RHWeil.F1

def integerShift (f : ℤ → ℂ) (j : ℤ) : ℂ := f (j - 1)

def stepWeighted (a : ℤ) (w f : ℤ → ℂ) (j : ℤ) : ℂ :=
  w j * f (j - a)

theorem stepWeighted_transport (a : ℤ) (w f : ℤ → ℂ) :
    integerShift (stepWeighted a (fun j => w (j + 1)) f) =
      stepWeighted a w (integerShift f) := by
  funext j
  simp only [integerShift, stepWeighted]
  congr 1
  · congr 1
    omega
  · congr 1
    omega

theorem geometricPhase_transport (z : ℂ) (hz : z ≠ 0) (g : ℤ → ℂ) (j : ℤ) :
    integerShift (fun k => z ^ k * g (k + 1)) j =
      z⁻¹ * (z ^ j * g j) := by
  simp [integerShift, zpow_sub₀ hz, div_eq_mul_inv,
    mul_comm, mul_assoc]

theorem weightedPermutation_det {ι : Type*} [Fintype ι] [DecidableEq ι]
    (σ : Equiv.Perm ι) (j₀ : ι) (z : ℂ) :
    Matrix.det ((Matrix.diagonal (fun j => if j = j₀ then z⁻¹ else 1)).submatrix σ id) =
      (Equiv.Perm.sign σ : ℂ) * z⁻¹ := by
  rw [Matrix.det_permute, Matrix.det_diagonal]
  simp

theorem iterate_unitDrift {X : Type*} (τ : X → X) (d : X → ℤ)
    (h : ∀ x, d (τ x) = d x + 1) (n : ℕ) (x : X) :
    d (τ^[n] x) = d x + n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Function.iterate_succ_apply', h, ih]
    omega

theorem no_bounded_unitDrift {X : Type*} (τ : X → X) (d : X → ℤ)
    (x : X) (M : ℤ) (hb : ∀ y, d y ≤ M)
    (h : ∀ y, d (τ y) = d y + 1) : False := by
  let n : ℕ := (M - d x).toNat + 1
  have hi := iterate_unitDrift τ d h n x
  have hu := hb (τ^[n] x)
  dsimp [n] at hi hu
  omega

end RHWeil.F1
