import Mathlib.Tactic.NoncommRing

/-! Exact associativity and weighted commutator identities used in note 421.
The map need not be multiplicative or additive. These are ring identities;
Schatten ideals, partial trace domains, Fourier transforms and cyclic
cohomology of the analytic algebra are proved separately in the note. -/
namespace RHWeil.F1

def multiplicationDefect {A B : Type*} [Mul A] [Ring B]
    (t : A → B) (a b : A) : B := t (a*b)-t a*t b

section Defect
variable {A B : Type*} [Semigroup A] [Ring B]

theorem multiplication_defect_associativity (t : A → B) (a b c : A) :
    multiplicationDefect t (a*b) c - multiplicationDefect t a (b*c) =
      t a * multiplicationDefect t b c - multiplicationDefect t a b * t c := by
  simp only [multiplicationDefect, mul_assoc]
  noncomm_ring

theorem antisymmetrized_defect_boundary (t : A → B) (a b c : A) :
    (multiplicationDefect t (a*b) c - multiplicationDefect t c (a*b)) -
      (multiplicationDefect t a (b*c) - multiplicationDefect t (b*c) a) +
      (multiplicationDefect t (c*a) b - multiplicationDefect t b (c*a)) =
    (t a * multiplicationDefect t b c - multiplicationDefect t b c * t a) +
    (t b * multiplicationDefect t c a - multiplicationDefect t c a * t b) +
    (t c * multiplicationDefect t a b - multiplicationDefect t a b * t c) := by
  simp only [multiplicationDefect, mul_assoc]
  noncomm_ring

end Defect

theorem weighted_commutator_transfer {R : Type*} [Ring R] (w a d : R) :
    w*(a*d-d*a) = (w*a-a*w)*d + (a*(w*d)-(w*d)*a) := by
  noncomm_ring

end RHWeil.F1
