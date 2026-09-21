import Mathlib.Tactic.NoncommRing

/-! Algebraic trace obstruction from an actual shift defect.
The operator realization, positivity, trace weights and norm density
are separate analytic statements, not assumptions hidden in these proofs. -/
namespace RHWeil.F1

theorem shift_commutator_defect
    {R : Type*} [Ring R] (s r e p : R)
    (hi : r*s=e) (hf : s*r=e-p) :
    r*s-s*r=p := by
  rw [hi, hf, sub_sub_cancel]

theorem cyclic_map_kills_shift_defect
    {R M : Type*} [Ring R] [AddCommGroup M]
    (tau : R →+ M) (s r e p : R)
    (hi : r*s=e) (hf : s*r=e-p)
    (hc : tau (r*s)=tau (s*r)) :
    tau p=0 := by
  rw [hi, hf, map_sub] at hc
  have h := congrArg (fun x : M => tau e-x) hc
  simp only [sub_self, sub_sub_cancel] at h
  exact h.symm

theorem nonzero_shift_defect_not_cyclic
    {R M : Type*} [Ring R] [AddCommGroup M]
    (tau : R →+ M) (s r e p : R)
    (hi : r*s=e) (hf : s*r=e-p)
    (hp : tau p≠0) :
    tau (r*s)≠tau (s*r) := by
  intro hc
  exact hp (cyclic_map_kills_shift_defect tau s r e p hi hf hc)

end RHWeil.F1
