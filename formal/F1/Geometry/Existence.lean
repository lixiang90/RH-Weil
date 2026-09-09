import F1.Analysis.Weil

/-! Open geometric input is represented by hypotheses, never by a global axiom.
This interface has no built-in positivity or RH conclusion.
-/

namespace RHWeil.F1

structure SquareModel where
  Divisor : Type
  [additive : AddCommGroup Divisor]
  [realModule : Module ℝ Divisor]
  degree : Divisor →ₗ[ℝ] ℝ
  codegree : Divisor →ₗ[ℝ] ℝ
  intersection : Divisor →ₗ[ℝ] Divisor →ₗ[ℝ] ℝ
  principal : Submodule ℝ Divisor
  effective : Set Divisor
  arithmeticDivisor : TestFunction → Divisor
  degree_identification : ∀ f, degree (arithmeticDivisor f) = degreeMoment f
  codegree_identification : ∀ f, codegree (arithmeticDivisor f) = codegreeMoment f
  trace_identification : ∀ f,
    intersection (arithmeticDivisor f) (arithmeticDivisor f) = weilSelf f

attribute [instance] SquareModel.additive SquareModel.realModule

def LinearlyEquivalent (M : SquareModel) (D E : M.Divisor) : Prop :=
  D - E ∈ M.principal

/-- Research input: principal equivalence preserves BOTH degrees. -/
def DegreeDescent (M : SquareModel) : Prop :=
  ∀ D E, LinearlyEquivalent M D E →
    M.degree D = M.degree E ∧ M.codegree D = M.codegree E

/-- Research input: effectivity and zero bidegree force the zero divisor. -/
def EffectiveRigidity (M : SquareModel) : Prop :=
  ∀ E : M.Divisor, E ∈ M.effective →
    M.degree E = 0 → M.codegree E = 0 → E = 0

/-- The missing RR existence step includes nontriviality.
The real nonzero scalar permits either sign and a positive rescaling.
No witness of this proposition is supplied for the arithmetic square.
-/
def SectionExistence (M : SquareModel) : Prop :=
  ∀ f : TestFunction, ZeroMoments f →
    0 < M.intersection (M.arithmeticDivisor f) (M.arithmeticDivisor f) →
    ∃ (c : ℝ) (E : M.Divisor), c ≠ 0 ∧ E ∈ M.effective ∧ E ≠ 0 ∧
      LinearlyEquivalent M E (c • M.arithmeticDivisor f)

theorem nonpositive_of_existence (M : SquareModel)
    (hdeg : DegreeDescent M) (hrigid : EffectiveRigidity M)
    (hex : SectionExistence M) : WeilNonpositive := by
  intro f hf
  by_contra h
  have hself : 0 < M.intersection (M.arithmeticDivisor f) (M.arithmeticDivisor f) := by
    rw [M.trace_identification]
    exact lt_of_not_ge h
  obtain ⟨c, E, hc, heff, hne, hlin⟩ := hex f hf hself
  have hd := hdeg E (c • M.arithmeticDivisor f) hlin
  have hD : M.degree E = 0 := by
    rw [hd.1, map_smul, M.degree_identification, hf.1, smul_zero]
  have hC : M.codegree E = 0 := by
    rw [hd.2, map_smul, M.codegree_identification, hf.2, smul_zero]
  exact hne (hrigid E heff hD hC)

/-- Conditional on explicit geometric research inputs AND the classical bridge. -/
theorem rh_of_existence (M : SquareModel)
    (hdeg : DegreeDescent M) (hrigid : EffectiveRigidity M)
    (hex : SectionExistence M) : RiemannHypothesis :=
  weilCriterion.mp (nonpositive_of_existence M hdeg hrigid hex)

/-- Bare abstract package only. Identifying it with the arithmetic square is
a separate research obligation, not encoded by this existential statement.
Deliberately no theorem inhabits this type. -/
def BareExistenceProblem : Prop :=
  ∃ M : SquareModel, DegreeDescent M ∧ EffectiveRigidity M ∧ SectionExistence M

/-- A geometric intersection pairing must descend through principal relations.
Both slots are explicit; symmetry is not assumed by the old minimal interface. -/
def PrincipalRadical (M : SquareModel) : Prop :=
  ∀ P ∈ M.principal, ∀ D, M.intersection P D = 0 ∧ M.intersection D P = 0

theorem intersection_eq_of_equivalent (M : SquareModel) (hP : PrincipalRadical M)
    {D E : M.Divisor} (h : LinearlyEquivalent M D E) :
    M.intersection D D = M.intersection E E := by
  have hl := (hP (D - E) h D).1
  have hr := (hP (D - E) h E).2
  have hl' : M.intersection D D = M.intersection E D := by
    simpa only [map_sub, LinearMap.sub_apply, sub_eq_zero] using hl
  have hr' : M.intersection E D = M.intersection E E := by
    simpa only [map_sub, sub_eq_zero] using hr
  exact hl'.trans hr'

theorem nonzero_of_positive_representative (M : SquareModel) (hP : PrincipalRadical M)
    {D E : M.Divisor} {c : ℝ} (hc : c ≠ 0)
    (hself : 0 < M.intersection D D) (hlin : LinearlyEquivalent M E (c • D)) :
    E ≠ 0 := by
  intro hz
  have heq := intersection_eq_of_equivalent M hP hlin
  rw [hz] at heq
  have hp : 0 < c * c * M.intersection D D :=
    mul_pos (mul_self_pos.mpr hc) hself
  simp only [map_zero, map_smul, LinearMap.smul_apply,
    smul_eq_mul] at heq
  apply ne_of_gt hp
  calc
    c * c * M.intersection D D = c * (c * M.intersection D D) := mul_assoc _ _ _
    _ = 0 := heq.symm

/-- Weaker RR input: effectivity only. Nonzero representatives follow from descent
of the pairing and strictly positive self-intersection. No geometric witness supplied. -/
def EffectiveRepresentativeExistence (M : SquareModel) : Prop :=
  ∀ f : TestFunction, ZeroMoments f →
    0 < M.intersection (M.arithmeticDivisor f) (M.arithmeticDivisor f) →
    ∃ (c : ℝ) (E : M.Divisor), c ≠ 0 ∧ E ∈ M.effective ∧
      LinearlyEquivalent M E (c • M.arithmeticDivisor f)

theorem sectionExistence_of_effectiveRepresentative (M : SquareModel)
    (hP : PrincipalRadical M) (hex : EffectiveRepresentativeExistence M) :
    SectionExistence M := by
  intro f hf hp
  obtain ⟨c, E, hc, he, hl⟩ := hex f hf hp
  exact ⟨c, E, hc, he, nonzero_of_positive_representative M hP hc hp hl, hl⟩

end RHWeil.F1
