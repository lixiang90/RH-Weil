import Mathlib.LinearAlgebra.Matrix.ConjTranspose
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.FinCases

/-! Algebraic identities for note 415.
The two-by-two blocks are actual matrices over arbitrary, potentially
noncommutative rings. Involution hypotheses imply an actual self-adjoint
idempotent, with no admission. Positivity, continuous functional calculus,
ideal membership, Hilbert-space estimates and trace convergence are not
formalized by this module. -/
namespace RHWeil.F1

/-- A two-by-two matrix over a potentially noncommutative ring. -/
def block2 {R : Type*} (x y z w : R) : Matrix (Fin 2) (Fin 2) R :=
  fun i j => if i = 0 then (if j = 0 then x else y) else (if j = 0 then z else w)

section Ring
variable {R : Type*} [Ring R]

theorem block2_mul (x y z w X Y Z W : R) :
    block2 x y z w * block2 X Y Z W =
      block2 (x*X+y*Z) (x*Y+y*W) (z*X+w*Z) (z*Y+w*W) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply,
      show (Finset.univ : Finset (Fin 2)) = {0, 1} from rfl, block2]

theorem block2_one : block2 (1 : R) 0 0 1 = 1 := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [block2]

theorem dilation_left (t ts a b : R)
    (ha : a*a = 1-ts*t) (hb : b*b = 1-t*ts)
    (ht : t*a = b*t) (hs : a*ts = ts*b) :
    block2 ts a (-b) t * block2 t (-b) a ts = 1 := by
  rw [block2_mul]
  have h1 : ts*t+a*a = 1 := by rw [ha]; abel
  have h2 : ts*(-b)+a*ts = 0 := by rw [hs]; noncomm_ring
  have h3 : (-b)*t+t*a = 0 := by rw [ht]; noncomm_ring
  have h4 : (-b)*(-b)+t*ts = 1 := by simp only [neg_mul_neg]; rw [hb]; abel
  rw [h1,h2,h3,h4,block2_one]

theorem dilation_right (t ts a b : R)
    (ha : a*a = 1-ts*t) (hb : b*b = 1-t*ts)
    (ht : t*a = b*t) (hs : a*ts = ts*b) :
    block2 t (-b) a ts * block2 ts a (-b) t = 1 := by
  rw [block2_mul]
  have h1 : t*ts+(-b)*(-b) = 1 := by simp only [neg_mul_neg]; rw [hb]; abel
  have h2 : t*a+(-b)*t = 0 := by rw [ht]; noncomm_ring
  have h3 : a*ts+ts*(-b) = 0 := by rw [hs]; noncomm_ring
  have h4 : a*a+ts*t = 1 := by rw [ha]; abel
  rw [h1,h2,h3,h4,block2_one]

theorem defect_diagonal (t ts : R) :
    (1-ts*t)-(1-t*ts) = t*ts-ts*t := by noncomm_ring

theorem commutator_transfer (t ts x : R) :
    (t*ts-ts*t)*x = (t*(ts*x)-(ts*x)*t)-ts*(t*x-x*t) := by
  noncomm_ring

/-- The diagonal idempotent used for a relative index class. -/
def firstBlock : Matrix (Fin 2) (Fin 2) R := block2 1 0 0 0

theorem firstBlock_idempotent : (firstBlock : Matrix (Fin 2) (Fin 2) R) *
    firstBlock = firstBlock := by
  simp [firstBlock, block2_mul]

theorem dilation_projection (t ts a b : R) :
    block2 t (-b) a ts * firstBlock * block2 ts a (-b) t =
      block2 (t*ts) (t*a) (a*ts) (a*a) := by
  simp [firstBlock, block2_mul]

theorem dilation_projection_idempotent (t ts a b : R)
    (ha : a*a = 1-ts*t) (hb : b*b = 1-t*ts)
    (ht : t*a = b*t) (hs : a*ts = ts*b) :
    let p := block2 (t*ts) (t*a) (a*ts) (a*a)
    p*p = p := by
  dsimp
  rw [← dilation_projection t ts a b]
  let w := block2 t (-b) a ts
  let wa := block2 ts a (-b) t
  change (w * firstBlock * wa) * (w * firstBlock * wa) = w * firstBlock * wa
  have hwa : wa*w = 1 := dilation_left t ts a b ha hb ht hs
  calc
    (w * firstBlock * wa) * (w * firstBlock * wa) =
        w * (firstBlock * (wa*w) * firstBlock) * wa := by noncomm_ring
    _ = w * firstBlock * wa := by rw [hwa, mul_one, firstBlock_idempotent]

theorem defect_projection_difference (t ts a : R) (ha : a*a = 1-ts*t) :
    block2 (t*ts) (t*a) (a*ts) (a*a) - firstBlock =
      block2 (-(1-t*ts)) (t*a) (a*ts) (1-ts*t) := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [block2, firstBlock, ha]

theorem defect_projection_diagonal (t ts a : R) (ha : a*a = 1-ts*t) :
    let p := block2 (t*ts) (t*a) (a*ts) (a*a) - firstBlock
    p 0 0 + p 1 1 = t*ts-ts*t := by
  simp [block2, firstBlock, ha]

end Ring

section StarRing
variable {R : Type*} [Ring R] [StarRing R]

theorem block2_conjTranspose (x y z w : R) :
    (block2 x y z w).conjTranspose = block2 (star x) (star z) (star y) (star w) := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [block2, Matrix.conjTranspose_apply]

theorem sqrt_intertwining_adjoint (t a b : R)
    (ha : star a = a) (hb : star b = b) (ht : t*a = b*t) :
    a*star t = star t*b := by
  have h := congrArg star ht
  simpa only [star_mul, ha, hb] using h

theorem dilation_conjTranspose (t a b : R) (ha : star a = a) (hb : star b = b) :
    (block2 t (-b) a (star t)).conjTranspose = block2 (star t) a (-b) t := by
  simp [block2_conjTranspose, ha, hb]

theorem dilation_unitary (t a b : R) (ha : star a = a) (hb : star b = b)
    (haa : a*a = 1-star t*t) (hbb : b*b = 1-t*star t) (ht : t*a = b*t) :
    let w := block2 t (-b) a (star t)
    w.conjTranspose*w = 1 ∧ w*w.conjTranspose = 1 := by
  dsimp
  rw [dilation_conjTranspose t a b ha hb]
  exact ⟨dilation_left t (star t) a b haa hbb ht
    (sqrt_intertwining_adjoint t a b ha hb ht),
    dilation_right t (star t) a b haa hbb ht
    (sqrt_intertwining_adjoint t a b ha hb ht)⟩

theorem defect_projection_selfAdjoint (t a : R) (ha : star a = a) :
    (block2 (t*star t) (t*a) (a*star t) (a*a)).conjTranspose =
      block2 (t*star t) (t*a) (a*star t) (a*a) := by
  simp [block2_conjTranspose, star_mul, ha]

theorem defect_projection (t a b : R) (ha : star a = a) (hb : star b = b)
    (haa : a*a = 1-star t*t) (hbb : b*b = 1-t*star t) (ht : t*a = b*t) :
    let p := block2 (t*star t) (t*a) (a*star t) (a*a)
    p*p = p ∧ p.conjTranspose = p := by
  exact ⟨dilation_projection_idempotent t (star t) a b haa hbb ht
    (sqrt_intertwining_adjoint t a b ha hb ht), defect_projection_selfAdjoint t a ha⟩

end StarRing

/-- The scalar cancellation for a nonzero displacement of the inner shell vector.
The Hilbert-space inner-product formulas are independent analytic input. -/
theorem shell_overlap_cancel {R : Type*} [CommRing R] (rho : R) (n : ℕ) :
    -rho*(1-rho^2)*rho^n+(1-rho^2)*rho^(n+1) = 0 := by
  rw [pow_succ]
  ring

end RHWeil.F1
