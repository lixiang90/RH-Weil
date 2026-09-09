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

end RHWeil.F1
