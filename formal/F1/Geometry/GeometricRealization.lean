import F1.Geometry.Existence
import Mathlib.CategoryTheory.Sites.Sheaf
import Mathlib.Algebra.Category.ModuleCat.Basic

/-! Source-relative geometric contracts. All data below are inputs, not constructed
arithmetic objects. In particular, a DivisorSite is NOT certified to be the
Connes--Consani square. The separate anchoring obligations are specified in
blueprint/geometric-realization.md. No additional admissions are introduced.
-/

open CategoryTheory Opposite

namespace RHWeil.F1

/-- A site with a terminal object and an actual sheaf of realified divisors.
The module sheaf is an interface AFTER realification, not the F1 structure sheaf. -/
structure DivisorSite where
  Site : Type
  [category : SmallCategory Site]
  topology : GrothendieckTopology Site
  total : Site
  total_isTerminal : Limits.IsTerminal total
  divisors : Sheaf topology (ModuleCat ℝ)

attribute [instance] DivisorSite.category

abbrev LocalDivisor (S : DivisorSite) (U : S.Site) := S.divisors.obj.obj (op U)
abbrev GlobalDivisor (S : DivisorSite) := LocalDivisor S S.total

/-- Natural local principal-divisor maps and locally detectable effective cones.
The additive sheaf `functions` models a realified/logarithmic function group;
its identification with actual meromorphic units is an anchoring obligation.
In particular, locally principal does NOT mean globally principal. -/
structure LocalDivisorTheory (S : DivisorSite) where
  functions : Sheaf S.topology AddCommGrpCat
  principalMap : functions.obj ⟶ S.divisors.obj ⋙ forget₂ (ModuleCat ℝ) AddCommGrpCat
  effective : ∀ U : S.Site, Set (LocalDivisor S U)
  effective_zero : ∀ U, 0 ∈ effective U
  effective_add : ∀ U D E, D ∈ effective U → E ∈ effective U → D + E ∈ effective U
  effective_smul : ∀ U (c : ℝ) D, 0 ≤ c → D ∈ effective U → c • D ∈ effective U
  effective_restrict : ∀ {U V : S.Site} (i : V ⟶ U) D,
    D ∈ effective U → S.divisors.obj.map i.op D ∈ effective V
  effective_local : ∀ U (R : Sieve U), R ∈ S.topology U →
    ∀ D : LocalDivisor S U,
      (∀ (V : S.Site) (i : V ⟶ U), R i →
        S.divisors.obj.map i.op D ∈ effective V) → D ∈ effective U

/-- Real span of GLOBAL principal divisors. No false surjectivity onto Cartier divisors. -/
def globalPrincipal {S : DivisorSite} (L : LocalDivisorTheory S) :
    Submodule ℝ (GlobalDivisor S) :=
  Submodule.span ℝ (Set.range (L.principalMap.app (op S.total)))

/-- Actual sheaves of sections indexed by global divisors, with effective-divisor
extraction. This does not yet assert invertibility over an arithmetic structure sheaf. -/
structure GeometricSections {S : DivisorSite} (L : LocalDivisorTheory S) where
  sections : GlobalDivisor S → Sheaf S.topology (Type)
  zeroSection : ∀ D, (sections D).obj.obj (op S.total)
  admissible : ∀ D, Set ((sections D).obj.obj (op S.total))
  admissible_ne_zero : ∀ D s, s ∈ admissible D → s ≠ zeroSection D
  divisorOf : ∀ D, {s : (sections D).obj.obj (op S.total) // s ∈ admissible D} →
    GlobalDivisor S
  divisorOf_effective : ∀ D s, divisorOf D s ∈ L.effective S.total
  divisorOf_equivalent : ∀ D s, divisorOf D s - D ∈ globalPrincipal L

/-- Comparison to a FIXED local geometric source, not an existentially chosen tag.
The arithmetic map is additive and homogeneous on the actual test functions;
pointwise hypotheses avoid installing a duplicate function-space module structure. -/
structure SourceRealization {S : DivisorSite} (L : LocalDivisorTheory S) where
  model : SquareModel
  globalComparison : model.Divisor ≃ₗ[ℝ] GlobalDivisor S
  principal_iff : ∀ D, D ∈ model.principal ↔ globalComparison D ∈ globalPrincipal L
  effective_iff : ∀ D, D ∈ model.effective ↔ globalComparison D ∈ L.effective S.total
  intersection_symmetric : ∀ D E, model.intersection D E = model.intersection E D
  principal_radical : PrincipalRadical model
  degree_descent : DegreeDescent model
  arithmetic_add : ∀ f g h : TestFunction, (∀ x, h x = f x + g x) →
    model.arithmeticDivisor h = model.arithmeticDivisor f + model.arithmeticDivisor g
  arithmetic_smul : ∀ (c : ℝ) (f h : TestFunction), (∀ x, h x = c * f x) →
    model.arithmeticDivisor h = c • model.arithmeticDivisor f

/-- Admissible global sections of the supplied sheaves. Their line-bundle origin
and the geometric meaning of admissibility remain separate anchoring obligations.
Nonzero alone need not permit a Cartier divisor; nonzero EFFECTIVE divisors are
deduced later using principal radical descent. -/
def GeometricRR {S : DivisorSite} {L : LocalDivisorTheory S}
    (R : SourceRealization L) (H : GeometricSections L) : Prop :=
  ∀ f : TestFunction, ZeroMoments f →
    0 < R.model.intersection (R.model.arithmeticDivisor f) (R.model.arithmeticDivisor f) →
    ∃ c : ℝ, c ≠ 0 ∧
      ∃ s : (H.sections (R.globalComparison (c • R.model.arithmeticDivisor f))).obj.obj
        (op S.total), s ∈ H.admissible (R.globalComparison (c • R.model.arithmeticDivisor f))

theorem effectiveRepresentative_of_geometricRR {S : DivisorSite}
    {L : LocalDivisorTheory S} (R : SourceRealization L) (H : GeometricSections L)
    (hRR : GeometricRR R H) : EffectiveRepresentativeExistence R.model := by
  intro f hf hp
  obtain ⟨c, hc, s, hs⟩ := hRR f hf hp
  let D := R.globalComparison (c • R.model.arithmeticDivisor f)
  let E := H.divisorOf D ⟨s, hs⟩
  refine ⟨c, R.globalComparison.symm E, hc, ?_, ?_⟩
  · apply (R.effective_iff _).mpr
    simpa only [LinearEquiv.apply_symm_apply] using H.divisorOf_effective D ⟨s, hs⟩
  · apply (R.principal_iff _).mpr
    simpa only [map_sub, LinearEquiv.apply_symm_apply] using H.divisorOf_equivalent D ⟨s, hs⟩

theorem sectionExistence_of_geometricRR {S : DivisorSite}
    {L : LocalDivisorTheory S} (R : SourceRealization L) (H : GeometricSections L)
    (hRR : GeometricRR R H) : SectionExistence R.model :=
  sectionExistence_of_effectiveRepresentative R.model R.principal_radical
    (effectiveRepresentative_of_geometricRR R H hRR)

theorem nonpositive_of_geometricRR {S : DivisorSite}
    {L : LocalDivisorTheory S} (R : SourceRealization L) (H : GeometricSections L)
    (hrigid : EffectiveRigidity R.model) (hRR : GeometricRR R H) : WeilNonpositive :=
  nonpositive_of_existence R.model R.degree_descent hrigid
    (sectionExistence_of_geometricRR R H hRR)

/-- This is still source-relative. The source must separately pass G0--G8 anchoring
and analytic comparison obligations; there is deliberately no witness here. -/
def SourceRelativeExistence (S : DivisorSite) (L : LocalDivisorTheory S) : Prop :=
  ∃ (R : SourceRealization L) (H : GeometricSections L),
    EffectiveRigidity R.model ∧ GeometricRR R H

end RHWeil.F1
