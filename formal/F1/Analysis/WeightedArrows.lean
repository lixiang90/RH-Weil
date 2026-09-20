import Mathlib.Algebra.Module.Pi
import Mathlib.Algebra.Module.LinearMap.End
import Mathlib.Data.Int.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
Coordinate algebra for the actual crossed-product representation in note 407.
These operators act on all functions. Their restriction to Hilbert space,
trace-class properties, determinants, and adele identifications are separate
analytic statements, not assumptions silently installed as instances.
-/
namespace RHWeil.F1

variable {G K : Type*} [Group G] [CommRing K]

/-- Coefficient multiplication followed by inverse left translation. -/
def weightedPull (q : G) (a : G → K) : Module.End K (G → K) where
  toFun f x := a x * f (q⁻¹ * x)
  map_add' f g := by funext x; simp [mul_add]
  map_smul' c f := by funext x; simp [smul_eq_mul, mul_left_comm]

theorem weightedPull_mul (q r : G) (a b : G → K) :
    weightedPull q a * weightedPull r b =
      weightedPull (q * r) (fun x => a x * b (q⁻¹ * x)) := by
  ext f x
  simp [weightedPull, mul_inv_rev, mul_assoc]

theorem weightedPull_pow_form (q : G) (a : G → K) (n : ℕ) :
    ∃ b : G → K, weightedPull q a ^ n = weightedPull (q ^ n) b := by
  induction n with
  | zero =>
      refine ⟨fun _ => 1, ?_⟩
      ext f x
      simp [weightedPull]
  | succ n ih =>
      obtain ⟨b, hb⟩ := ih
      refine ⟨fun x => a x * b (q⁻¹ * x), ?_⟩
      rw [pow_succ', hb, weightedPull_mul, pow_succ']

noncomputable def deltaFunction (x : G) : G → K := by
  classical
  exact fun y => if y = x then 1 else 0

theorem weightedPull_diagonal_zero (q : G) (a : G → K) (x : G) (hq : q ≠ 1) :
    weightedPull q a (deltaFunction x) x = 0 := by
  classical
  have hx : q⁻¹ * x ≠ x := by
    intro h
    have he : q⁻¹ * x = 1 * x := by simpa using h
    exact hq (inv_eq_one.mp (mul_right_cancel he))
  simp [weightedPull, deltaFunction, hx]

theorem weightedPull_pow_diagonal_zero (q : G) (a : G → K) (x : G)
    (n : ℕ) (hq : q ^ n ≠ 1) :
    (weightedPull q a ^ n) (deltaFunction x) x = 0 := by
  obtain ⟨b, hb⟩ := weightedPull_pow_form q a n
  rw [hb]
  exact weightedPull_diagonal_zero (q ^ n) b x hq

/-- Finite word order matches composition order in the crossed product. -/
def weightedWord (arrows : List (G × (G → K))) : Module.End K (G → K) :=
  arrows.foldr (fun item acc => weightedPull item.1 item.2 * acc) 1

theorem weightedWord_form (arrows : List (G × (G → K))) :
    ∃ b : G → K, weightedWord arrows = weightedPull ((arrows.map Prod.fst).prod) b := by
  induction arrows with
  | nil =>
      refine ⟨fun _ => 1, ?_⟩
      ext f x
      simp [weightedWord, weightedPull]
  | cons item rest ih =>
      obtain ⟨b, hb⟩ := ih
      refine ⟨fun x => item.2 x * b (item.1⁻¹ * x), ?_⟩
      simp only [weightedWord, List.foldr_cons] at *
      rw [hb, weightedPull_mul]
      rfl

theorem weightedWord_diagonal_zero (arrows : List (G × (G → K))) (x : G)
    (h : (arrows.map Prod.fst).prod ≠ 1) :
    weightedWord arrows (deltaFunction x) x = 0 := by
  obtain ⟨b, hb⟩ := weightedWord_form arrows
  rw [hb]
  exact weightedPull_diagonal_zero _ _ _ h

theorem weightedPull_inverse_pair (q : G) (a b f : G → K) (x : G) :
    (weightedPull q a * weightedPull q⁻¹ b) f x =
      (a x * b (q⁻¹ * x)) * f x := by
  rw [weightedPull_mul]
  simp [weightedPull]

/-- With u=q² and q≥2, this controls the sign of the explicit Gaussian residue. -/
theorem loopResiduePolynomial_pos (u : ℝ) (hu : 4 ≤ u) :
    0 < 6 * u ^ 2 - 23 * u + 6 := by
  nlinarith [sq_nonneg (u - 4)]


/-- A degree-raising fixed-point recurrence with a lower support bound has zero solution.
This is the algebraic kernel test for multiplication by 1 minus a degree-one element. -/
theorem lowerBoundedRecurrence_zero {V : Type*} [Zero V]
    (f : ℤ → V) (F : ℤ → V → V) (N : ℤ)
    (hzero : ∀ n, F n 0 = 0)
    (hlower : ∀ n < N, f n = 0)
    (hrec : ∀ n, f (n + 1) = F n (f n)) :
    ∀ n, f n = 0 := by
  intro n
  have hbase : f N = 0 := by
    have h := hrec (N - 1)
    simpa [hlower (N - 1) (by omega), hzero] using h
  refine Int.inductionOn' n N hbase ?_ ?_
  · intro k _ hk
    rw [hrec k, hk, hzero]
  · intro k hk _
    exact hlower (k - 1) (by omega)

end RHWeil.F1
