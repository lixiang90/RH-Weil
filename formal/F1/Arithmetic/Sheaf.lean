import F1.Arithmetic.FiniteSupport
import Mathlib.RingTheory.Spectrum.Prime.Topology
import Mathlib.Data.Nat.Prime.Int
import Mathlib.RingTheory.Ideal.Maximal
import Mathlib.Topology.Sheaves.Stalks
import Mathlib.Topology.Sheaves.Sheaf

/-! A concrete presheaf on the actual Zariski space Spec Z.
Only the exponent sheaf is constructed here. Adding the absorbing element
and comparing spherical algebras are separate blueprint nodes.
-/

open CategoryTheory Opposite TopologicalSpace

namespace RHWeil.F1

abbrev ArithmeticSpace := TopCat.of (PrimeSpectrum ℤ)

def pointOfPrime (p : PrimeIndex) : PrimeSpectrum ℤ :=
  ⟨Ideal.span {(p.val : ℤ)},
    Ideal.isPrime_span_singleton_of_prime (Nat.prime_iff_prime_int.mp p.property)⟩

def primesIn (U : Opens ArithmeticSpace) : Set PrimeIndex :=
  {p | pointOfPrime p ∈ U}

def ExponentSection (U : Opens ArithmeticSpace) :=
  {a : ExponentData // IsSection (primesIn U) a}

noncomputable def exponentPresheaf : ArithmeticSpace.Presheaf (Type) where
  obj U := ExponentSection U.unop
  map {U V} h := ↾fun a =>
    ⟨restrict (primesIn V.unop) a.val,
      restrict_isSection (primesIn U.unop) (primesIn V.unop) a.val a.property⟩
  map_id U := by
    apply ConcreteCategory.hom_ext
    intro a
    apply Subtype.ext
    exact restrict_self _ _ a.property
  map_comp {U V W} f g := by
    apply ConcreteCategory.hom_ext
    intro a
    apply Subtype.ext
    exact (restrict_restrict (primesIn V.unop) (primesIn W.unop)
      (fun _ hp => g.unop.le hp) a.val).symm

/-- BP-SHEAF-01: finite-cover gluing on the noetherian Zariski space. -/
theorem exponentPresheaf_isSheaf : exponentPresheaf.IsSheaf := by
  sorry

/-- BP-SHEAF-02: the genuine colimit stalk, not a separately named model. -/
theorem exponent_stalk_at_prime (p : PrimeIndex) :
    Nonempty (exponentPresheaf.stalk (pointOfPrime p) ≃ primeCone p.val) := by
  sorry

end RHWeil.F1
