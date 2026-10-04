import Lean.Elab.Tactic.Omega

/-! Exact lattice witnesses for note 423.  This module uses only Lean's core
integer theory.  It does not formalize trace ideals, cyclic theory, the analytic
source or RH.  The two product labels and their pointwise coefficient are
verified for every integer label and every lattice point. -/
namespace RHWeil.F1

def twistedLatticeStep (j : Int) : Int := if 0 ≤ j then 1 else 0

theorem twistedLattice_rankOne (j : Int) :
    twistedLatticeStep j * twistedLatticeStep (j-1) -
      twistedLatticeStep j * twistedLatticeStep (j+1) =
        -(if j = 0 then 1 else 0) := by
  by_cases hj : j = 0
  · subst j
    decide
  · by_cases hp : 0 < j
    · have h0 : 0 ≤ j := by omega
      have hm : 1 ≤ j := by omega
      have hplus : 0 ≤ j+1 := by omega
      simp [twistedLatticeStep, h0, hm, hplus, hj]
    · have h0 : ¬0 ≤ j := by omega
      simp [twistedLatticeStep, h0, hj]

theorem twistedLattice_twoDimensional (j k : Int) :
    (twistedLatticeStep j * twistedLatticeStep (j-1) -
      twistedLatticeStep j * twistedLatticeStep (j+1)) *
        (if k = 0 then 1 else 0) =
          -(if j = 0 ∧ k = 0 then 1 else 0) := by
  rw [twistedLattice_rankOne]
  by_cases hj : j = 0 <;> by_cases hk : k = 0 <;> simp [hj, hk]

theorem twistedWitness_forwardLabel (gamma : Int × Int) :
    (1 + (gamma.1-1), 0 + gamma.2) = gamma := by
  rcases gamma with ⟨r, s⟩
  congr 1 <;> omega

theorem twistedWitness_reverseLabel (gamma : Int × Int) :
    ((gamma.1-1) + 1, gamma.2 + 0) = gamma := by
  rcases gamma with ⟨r, s⟩
  congr 1 <;> omega

end RHWeil.F1
