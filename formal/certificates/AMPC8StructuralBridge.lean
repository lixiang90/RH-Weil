-- Independent pure-definition bridges, authored locally; no upstream proof execution.
namespace AMW.Cert.PC8CL
open AMW.Cert AMW.Cert.Pyr AMW.Cert.PyrD AMW.Cert.PCell

def genericGsplit (ih : WF) (pos r : Nat) (s : St) : Nat :=
  let c := toCl s
  let q := qG c r
  let ca := cupd 7 PR SL ⟨c.L, c.U.set r q, c.A, c.B⟩ r (r + 1)
  let cb := cupd 7 PR SL ⟨c.L.set r q, c.U, c.A, c.B⟩ (r + 1) r
  let p := U (ih pos) (ofCl ca s.M)
  boolRec (motive := fun _ => Nat) (U (ih p) (ofCl cb s.M)) 0 (Nat.beq p 0)

def genericSsplit (ih : WF) (pos k : Nat) (s : St) : Nat :=
  let c := toCl s
  let q := qR c k
  let ca := cupd 7 PR SL ⟨c.L, c.U, c.A, c.B.set k q⟩ (pI PR k) (pJ PR k)
  let cb := cupd 7 PR SL ⟨c.L, c.U, c.A.set k q, c.B⟩ (pJ PR k) (pI PR k)
  let p := U (ih pos) (ofCl ca s.M)
  boolRec (motive := fun _ => Nat) (U (ih p) (ofCl cb s.M)) 0 (Nat.beq p 0)

theorem gsplit0_bridge (ih : WF) (pos : Nat) (s : St) : U (gsplit0 ih pos) s = genericGsplit ih pos 0 s := by
  cases s
  rfl

theorem gsplit1_bridge (ih : WF) (pos : Nat) (s : St) : U (gsplit1 ih pos) s = genericGsplit ih pos 1 s := by
  cases s
  rfl

theorem gsplit2_bridge (ih : WF) (pos : Nat) (s : St) : U (gsplit2 ih pos) s = genericGsplit ih pos 2 s := by
  cases s
  rfl

theorem gsplit3_bridge (ih : WF) (pos : Nat) (s : St) : U (gsplit3 ih pos) s = genericGsplit ih pos 3 s := by
  cases s
  rfl

theorem gsplit4_bridge (ih : WF) (pos : Nat) (s : St) : U (gsplit4 ih pos) s = genericGsplit ih pos 4 s := by
  cases s
  rfl

theorem gsplit5_bridge (ih : WF) (pos : Nat) (s : St) : U (gsplit5 ih pos) s = genericGsplit ih pos 5 s := by
  cases s
  rfl

theorem gsplit6_bridge (ih : WF) (pos : Nat) (s : St) : U (gsplit6 ih pos) s = genericGsplit ih pos 6 s := by
  cases s
  rfl

theorem ssplit02_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit02 ih pos) s = genericSsplit ih pos 0 s := by
  cases s
  rfl

theorem ssplit03_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit03 ih pos) s = genericSsplit ih pos 1 s := by
  cases s
  rfl

theorem ssplit04_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit04 ih pos) s = genericSsplit ih pos 2 s := by
  cases s
  rfl

theorem ssplit05_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit05 ih pos) s = genericSsplit ih pos 3 s := by
  cases s
  rfl

theorem ssplit06_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit06 ih pos) s = genericSsplit ih pos 4 s := by
  cases s
  rfl

theorem ssplit07_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit07 ih pos) s = genericSsplit ih pos 5 s := by
  cases s
  rfl

theorem ssplit13_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit13 ih pos) s = genericSsplit ih pos 6 s := by
  cases s
  rfl

theorem ssplit14_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit14 ih pos) s = genericSsplit ih pos 7 s := by
  cases s
  rfl

theorem ssplit15_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit15 ih pos) s = genericSsplit ih pos 8 s := by
  cases s
  rfl

theorem ssplit16_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit16 ih pos) s = genericSsplit ih pos 9 s := by
  cases s
  rfl

theorem ssplit17_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit17 ih pos) s = genericSsplit ih pos 10 s := by
  cases s
  rfl

theorem ssplit24_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit24 ih pos) s = genericSsplit ih pos 11 s := by
  cases s
  rfl

theorem ssplit25_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit25 ih pos) s = genericSsplit ih pos 12 s := by
  cases s
  rfl

theorem ssplit26_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit26 ih pos) s = genericSsplit ih pos 13 s := by
  cases s
  rfl

theorem ssplit27_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit27 ih pos) s = genericSsplit ih pos 14 s := by
  cases s
  rfl

theorem ssplit35_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit35 ih pos) s = genericSsplit ih pos 15 s := by
  cases s
  rfl

theorem ssplit36_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit36 ih pos) s = genericSsplit ih pos 16 s := by
  cases s
  rfl

theorem ssplit37_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit37 ih pos) s = genericSsplit ih pos 17 s := by
  cases s
  rfl

theorem ssplit46_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit46 ih pos) s = genericSsplit ih pos 18 s := by
  cases s
  rfl

theorem ssplit47_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit47 ih pos) s = genericSsplit ih pos 19 s := by
  cases s
  rfl

theorem ssplit57_bridge (ih : WF) (pos : Nat) (s : St) : U (ssplit57 ih pos) s = genericSsplit ih pos 20 s := by
  cases s
  rfl

theorem tm_bridge (k : ST) (s : St) : U (tm k) s = U k (ofCl (matC PR (toCl s)) s.M) := by
  cases s
  rfl
end AMW.Cert.PC8CL
#print axioms AMW.Cert.PC8CL.gsplit0_bridge
#print axioms AMW.Cert.PC8CL.gsplit1_bridge
#print axioms AMW.Cert.PC8CL.gsplit2_bridge
#print axioms AMW.Cert.PC8CL.gsplit3_bridge
#print axioms AMW.Cert.PC8CL.gsplit4_bridge
#print axioms AMW.Cert.PC8CL.gsplit5_bridge
#print axioms AMW.Cert.PC8CL.gsplit6_bridge
#print axioms AMW.Cert.PC8CL.ssplit02_bridge
#print axioms AMW.Cert.PC8CL.ssplit03_bridge
#print axioms AMW.Cert.PC8CL.ssplit04_bridge
#print axioms AMW.Cert.PC8CL.ssplit05_bridge
#print axioms AMW.Cert.PC8CL.ssplit06_bridge
#print axioms AMW.Cert.PC8CL.ssplit07_bridge
#print axioms AMW.Cert.PC8CL.ssplit13_bridge
#print axioms AMW.Cert.PC8CL.ssplit14_bridge
#print axioms AMW.Cert.PC8CL.ssplit15_bridge
#print axioms AMW.Cert.PC8CL.ssplit16_bridge
#print axioms AMW.Cert.PC8CL.ssplit17_bridge
#print axioms AMW.Cert.PC8CL.ssplit24_bridge
#print axioms AMW.Cert.PC8CL.ssplit25_bridge
#print axioms AMW.Cert.PC8CL.ssplit26_bridge
#print axioms AMW.Cert.PC8CL.ssplit27_bridge
#print axioms AMW.Cert.PC8CL.ssplit35_bridge
#print axioms AMW.Cert.PC8CL.ssplit36_bridge
#print axioms AMW.Cert.PC8CL.ssplit37_bridge
#print axioms AMW.Cert.PC8CL.ssplit46_bridge
#print axioms AMW.Cert.PC8CL.ssplit47_bridge
#print axioms AMW.Cert.PC8CL.ssplit57_bridge
#print axioms AMW.Cert.PC8CL.tm_bridge
