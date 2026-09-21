import Mathlib.Tactic.Ring
import Mathlib.Data.Int.Basic
import Lean.Elab.Tactic.Omega

/-! Algebraic bookkeeping for the radial finite part in note 422.
The analytic sequence space, infinite sums, operator ideals and trace domains
are proved separately. No summability or arithmetic existence is assumed here. -/
namespace RHWeil.F1

structure RadialFinitePartData (R : Type*) where
  finitePart : R
  pEdge : R
  qEdge : R
  corner : R

def radialTranslate {R : Type*} [CommRing R] (a b : R)
    (d : RadialFinitePartData R) : RadialFinitePartData R :=
  ⟨d.finitePart - a*d.pEdge - b*d.qEdge + a*b*d.corner,
   d.pEdge - b*d.corner, d.qEdge - a*d.corner, d.corner⟩

theorem radialTranslate_zero {R : Type*} [CommRing R]
    (d : RadialFinitePartData R) : radialTranslate 0 0 d = d := by
  cases d
  simp [radialTranslate]

theorem radialTranslate_add {R : Type*} [CommRing R]
    (a b c e : R) (d : RadialFinitePartData R) :
    radialTranslate a b (radialTranslate c e d) =
      radialTranslate (a+c) (b+e) d := by
  cases d
  simp only [radialTranslate, RadialFinitePartData.mk.injEq]
  constructor
  · ring
  constructor
  · ring
  constructor
  · ring
  · trivial

theorem radialTranslate_inverse {R : Type*} [CommRing R]
    (a b : R) (d : RadialFinitePartData R) :
    radialTranslate (-a) (-b) (radialTranslate a b d) = d := by
  rw [radialTranslate_add]
  simpa using radialTranslate_zero d

theorem radialRectangle_subtraction {R : Type*} [CommRing R]
    (n m corner pTail qTail interior : R) :
    (n*m*corner + n*pTail + m*qTail + interior) -
      n*(m*corner+pTail) - m*(n*corner+qTail) +
      n*m*corner = interior := by
  ring

theorem radialComm_reverseShift {R : Type*} [CommRing R]
    (a b : R) (d : RadialFinitePartData R) :
    d.finitePart - (radialTranslate (-a) (-b) d).finitePart =
      -a*d.pEdge - b*d.qEdge - a*b*d.corner := by
  simp only [radialTranslate]
  ring

theorem radialQuadrant_sourceAnomaly (n : ℤ) :
    (-n)*max 0 (-1) + (-1)*max 0 (-n) - (-n)*(-1) =
      -(max 0 n) := by
  by_cases hn : 0 ≤ n
  · rw [max_eq_left (by omega : (-1:ℤ) ≤ 0),
        max_eq_left (by omega : -n ≤ 0), max_eq_right hn]
    omega
  · rw [max_eq_left (by omega : (-1:ℤ) ≤ 0),
        max_eq_right (by omega : 0 ≤ -n), max_eq_left (by omega : n ≤ 0)]
    omega

end RHWeil.F1
