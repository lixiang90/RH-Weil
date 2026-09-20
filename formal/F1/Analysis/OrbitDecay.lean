import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
Finite-visit product estimates for note 408.
The orbit geometry, Banach crossed product, and spectral-radius conclusion
remain separate analytic obligations. No adele or RH assumptions are installed.
-/
namespace RHWeil.F1
open scoped BigOperators

theorem visitMajorant_product {ι : Type*} (s : Finset ι)
    (bad : ι → Prop) [DecidablePred bad] (ε C : ℝ) :
    (∏ i ∈ s, ε * (if bad i then C else 1)) =
      ε ^ s.card * C ^ (s.filter bad).card := by
  have h : (∏ i ∈ s, if bad i then C else 1) = C ^ (s.filter bad).card := by
    rw [← Finset.prod_filter]
    exact Finset.prod_const C
  rw [Finset.prod_mul_distrib, Finset.prod_const, h]

theorem visitMajorant_pointwise (f ε M : ℝ) (bad : Prop) [Decidable bad]
    (hε : 0 < ε) (hf : f ≤ M) (hout : ¬bad → f ≤ ε) :
    f ≤ ε * (if bad then max 1 (M / ε) else 1) := by
  by_cases hb : bad
  · rw [if_pos hb]
    have h : M ≤ max 1 (M / ε) * ε :=
      (div_le_iff₀ hε).mp (le_max_right 1 (M / ε))
    simpa [mul_comm] using hf.trans h
  · simpa [hb] using hout hb

theorem finiteVisitProductBound {ι : Type*} (s : Finset ι)
    (bad : ι → Prop) [DecidablePred bad] (f : ι → ℝ)
    (ε C : ℝ) (N : ℕ) (hε : 0 ≤ ε) (hC : 1 ≤ C)
    (hcard : (s.filter bad).card ≤ N)
    (hf : ∀ i ∈ s, 0 ≤ f i)
    (hmajor : ∀ i ∈ s, f i ≤ ε * (if bad i then C else 1)) :
    (∏ i ∈ s, f i) ≤ ε ^ s.card * C ^ N := by
  calc
    (∏ i ∈ s, f i) ≤ ∏ i ∈ s, ε * (if bad i then C else 1) :=
      Finset.prod_le_prod hf hmajor
    _ = ε ^ s.card * C ^ (s.filter bad).card := visitMajorant_product s bad ε C
    _ ≤ ε ^ s.card * C ^ N :=
      mul_le_mul_of_nonneg_left (pow_le_pow_right₀ hC hcard) (pow_nonneg hε _)

theorem orbit_interval_span (x l u h : ℝ) (m n : ℕ)
    (hh : 0 < h) (hl : l ≤ x - (n : ℝ) * h)
    (hu : x - (m : ℝ) * h ≤ u) :
    (n : ℝ) - (m : ℝ) ≤ (u - l) / h := by
  apply (le_div_iff₀ hh).2
  nlinarith

end RHWeil.F1
