import Mathlib.GroupTheory.QuotientGroup.Defs
import F1.Analysis.TraceRadical

/-!
Unit descent tests for note 406. Identifying a subgroup with geometric regular
units is an explicit input. No adele analysis, determinant theorem, or sheaf
construction is asserted by this module.
-/
namespace RHWeil.F1

variable {G H : Type*} [Group G] [Group H]

/-- A divisor label must be unchanged by multiplication by a regular unit. -/
def regularUnitInvariant (U : Subgroup G) (f : G →* H) : Prop :=
  ∀ g u, u ∈ U → f (g * u) = f g

theorem regularUnitInvariant_iff (U : Subgroup G) (f : G →* H) :
    regularUnitInvariant U f ↔ U ≤ f.ker := by
  constructor
  · intro h u hu
    have hx := h 1 u hu
    simpa using hx
  · intro h g u hu
    have hx : f u = 1 := h hu
    simp [map_mul, hx]

/-- The normality hypothesis is required; no quotient of arbitrary units is assumed. -/
theorem unitQuotient_factor_iff (U : Subgroup G) [U.Normal] (f : G →* H) :
    (∃ barf : G ⧸ U →* H, barf.comp (QuotientGroup.mk' U) = f) ↔ U ≤ f.ker := by
  constructor
  · rintro ⟨barf, hbar⟩ u hu
    have hm : QuotientGroup.mk' U u = 1 := (QuotientGroup.eq_one_iff u).mpr hu
    have hx := DFunLike.congr_fun hbar u
    change barf (QuotientGroup.mk' U u) = f u at hx
    simpa [hm] using hx.symm
  · intro h
    exact ⟨QuotientGroup.lift U f h, QuotientGroup.lift_comp_mk' U f h⟩

theorem unitQuotient_obstruction (U : Subgroup G) [U.Normal] (f : G →* H)
    (u : G) (hu : u ∈ U) (hfu : f u ≠ 1) :
    ¬ ∃ barf : G ⧸ U →* H, barf.comp (QuotientGroup.mk' U) = f := by
  intro h
  exact hfu ((unitQuotient_factor_iff U f).mp h hu)

/-- Killing a source relation with a nonzero moment prevents that moment from descending. -/
theorem moment_preservation_obstruction
    {E V : Type*} [AddCommGroup E] [Module ℝ E] [AddCommGroup V] [Module ℝ V]
    (C : E →ₗ[ℝ] V) (d : E →ₗ[ℝ] ℝ) (h : E)
    (hC : C h = 0) (hd : d h ≠ 0) :
    ¬ ∃ delta : V →ₗ[ℝ] ℝ, delta.comp C = d := by
  rintro ⟨delta, heq⟩
  have hx := DFunLike.congr_fun heq h
  change delta (C h) = d h at hx
  exact hd (by simpa [hC] using hx.symm)

end RHWeil.F1
