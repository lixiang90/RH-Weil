-- Locally authored generic minorant bridge; abstract large slope offset first.
namespace AMW.Cert.PCell
open AMW.Cert AMW.Cert.Pyr AMW.Cert.PyrD

def mcpB (B : Nat) (f : ℕ → ℕ) (L l1 l2 p1 p2 : ℕ) : ℕ :=
 Nat.add (Nat.mul (Nat.mul l1 (Nat.sub (hi32 (hi32 (f p1))) B)) (Nat.sub p1 L))
   (Nat.mul (Nat.mul l2 (Nat.sub (hi32 (hi32 (f p2))) B)) (Nat.sub p2 L))

def mcnB (B : Nat) (f : ℕ → ℕ) (L l1 l2 p1 p2 : ℕ) : ℕ :=
 Nat.add (Nat.mul (Nat.mul l1 (Nat.sub B (hi32 (hi32 (f p1))))) (Nat.sub p1 L))
   (Nat.mul (Nat.mul l2 (Nat.sub B (hi32 (hi32 (f p2))))) (Nat.sub p2 L))

def chgB (B : Nat) (f : ℕ → ℕ) (sg : Bool) (L0 l p : ℕ) : ℕ :=
 Nat.mul (Nat.mul l (boolRec (motive := fun _ => ℕ) (Nat.sub B (hi32 (hi32 (f p)))) (Nat.sub (hi32 (hi32 (f p))) B) sg)) (Nat.sub p L0)

def mcKB (B : Nat) (f : ℕ → ℕ) (sg : Bool) (L0 k m p r : ℕ) : ℕ :=
 boolRec (motive := fun _ => ℕ) (boolRec (motive := fun _ => ℕ) (boolRec (motive := fun _ => ℕ) 0
     (Nat.add (chgB B f sg L0 (Nat.sub 1024 m) p) (chgB B f sg L0 m r)) (Nat.beq k 3))
   (chgB B f sg L0 m p) (Nat.beq k 2))
   (chgB B f sg L0 1024 p) (Nat.beq k 1)

def mcpTB (B : Nat) (f : Nat → Nat) (L0 k m p r : Nat) : Nat :=
  mcpB B f L0 (mw1 k m) (mw2 k m) p r
def mcnTB (B : Nat) (f : Nat → Nat) (L0 k m p r : Nat) : Nat :=
  mcnB B f L0 (mw1 k m) (mw2 k m) p r

theorem mcpB_eq (B : Nat) (f : Nat → Nat) (L0 k m p r : Nat) : mcKB B f true L0 k m p r = mcpTB B f L0 k m p r := by
  unfold mcKB chgB mcpTB mcpB mw1 mw2
  cases k with
  | zero => simp [boolRec]
  | succ k =>
    cases k with
    | zero => simp [boolRec]
    | succ k =>
      cases k with
      | zero => simp [boolRec]
      | succ k =>
        cases k with
        | zero => simp [boolRec]
        | succ k => simp [boolRec, Nat.beq]

theorem mcnB_eq (B : Nat) (f : Nat → Nat) (L0 k m p r : Nat) : mcKB B f false L0 k m p r = mcnTB B f L0 k m p r := by
  unfold mcKB chgB mcnTB mcnB mw1 mw2
  cases k with
  | zero => simp [boolRec]
  | succ k =>
    cases k with
    | zero => simp [boolRec]
    | succ k =>
      cases k with
      | zero => simp [boolRec]
      | succ k =>
        cases k with
        | zero => simp [boolRec]
        | succ k => simp [boolRec, Nat.beq]

theorem mvK_eq_std (top : ℕ) (bk : ℕ → ℕ) (f : ℕ → ℕ) (L U k m p r : ℕ) : mvK top bk f L U k m p r = mvT top bk f L U k m p r := by
  unfold mvK mvT mval mwc mw1 mw2
  cases k with
  | zero => simp [boolRec]
  | succ k =>
    cases k with
    | zero => simp [boolRec]
    | succ k =>
      cases k with
      | zero => simp [boolRec]
      | succ k =>
        cases k with
        | zero => simp [boolRec]
        | succ k => simp [boolRec, Nat.beq]

theorem mslK_eq_std (f : ℕ → ℕ) (k m p r : ℕ) : mslK f k m p r = mslT f k m p r := by
  unfold mslK mslT msl mw1 mw2
  cases k with
  | zero => simp [boolRec]
  | succ k =>
    cases k with
    | zero => simp [boolRec]
    | succ k =>
      cases k with
      | zero => simp [boolRec]
      | succ k =>
        cases k with
        | zero => simp [boolRec]
        | succ k => simp [boolRec, Nat.beq]

theorem mcpK_eq_std (f : ℕ → ℕ) (L0 k m p r : ℕ) : mcK f true L0 k m p r = mcpT f L0 k m p r := by
  exact mcpB_eq 2000000000 f L0 k m p r

theorem mcnK_eq_std (f : ℕ → ℕ) (L0 k m p r : ℕ) : mcK f false L0 k m p r = mcnT f L0 k m p r := by
  exact mcnB_eq 2000000000 f L0 k m p r
end AMW.Cert.PCell
namespace AMW.Cert.PC8CL
open AMW.Cert AMW.Cert.Pyr AMW.Cert.PyrD AMW.Cert.PCell
theorem mcheckP_bridge {top : ℕ} {bk : ℕ → ℕ} {tD : ℕ} {bD : ℕ → ℕ} {f : ℕ → ℕ} {R : ℕ × ℕ × List (List ℕ)} (s : St)
   (k01 m01 p01 r01 k03 m03 p03 r03 k04 m04 p04 r04 k05 m05 p05 r05 k06 m06 p06 r06 k07 m07 p07 r07 k12 m12 p12 r12 k13 m13 p13 r13 k14 m14 p14 r14 k15 m15 p15 r15 k16 m16 p16 r16 k17 m17 p17 r17 k23 m23 p23 r23 k24 m24 p24 r24 k25 m25 p25 r25 k26 m26 p26 r26 k27 m27 p27 r27 k34 m34 p34 r34 k35 m35 p35 r35 k36 m36 p36 r36 k37 m37 p37 r37 k45 m45 p45 r45 k46 m46 p46 r46 k47 m47 p47 r47 k56 m56 p56 r56 k67 m67 p67 r67 : ℕ) (P0 P1 P2 P3 P4 P5 P6 S0 S1 S2 S3 S4 S5 S6 Cp Cm : ℕ) (h : mcheckP top bk tD bD f R s k01 m01 p01 r01 k03 m03 p03 r03 k04 m04 p04 r04 k05 m05 p05 r05 k06 m06 p06 r06 k07 m07 p07 r07 k12 m12 p12 r12 k13 m13 p13 r13 k14 m14 p14 r14 k15 m15 p15 r15 k16 m16 p16 r16 k17 m17 p17 r17 k23 m23 p23 r23 k24 m24 p24 r24 k25 m25 p25 r25 k26 m26 p26 r26 k27 m27 p27 r27 k34 m34 p34 r34 k35 m35 p35 r35 k36 m36 p36 r36 k37 m37 p37 r37 k45 m45 p45 r45 k46 m46 p46 r46 k47 m47 p47 r47 k56 m56 p56 r56 k67 m67 p67 r67 P0 P1 P2 P3 P4 P5 P6 S0 S1 S2 S3 S4 S5 S6 Cp Cm = true) :
   mcheckGZ top bk tD bD f R 8 7 BS TS cN (toCl s) [(k01, m01, p01, r01), (k03, m03, p03, r03), (k04, m04, p04, r04), (k05, m05, p05, r05), (k06, m06, p06, r06), (k07, m07, p07, r07), (k12, m12, p12, r12), (k13, m13, p13, r13), (k14, m14, p14, r14), (k15, m15, p15, r15), (k16, m16, p16, r16), (k17, m17, p17, r17), (k23, m23, p23, r23), (k24, m24, p24, r24), (k25, m25, p25, r25), (k26, m26, p26, r26), (k27, m27, p27, r27), (k34, m34, p34, r34), (k35, m35, p35, r35), (k36, m36, p36, r36), (k37, m37, p37, r37), (k45, m45, p45, r45), (k46, m46, p46, r46), (k47, m47, p47, r47), (k56, m56, p56, r56), (k67, m67, p67, r67)]
     [P0, P1, P2, P3, P4, P5, P6] [S0, S1, S2, S3, S4, S5, S6] Cp Cm = true := by
 simp only [mcheckP, mvK_eq_std, mcpK_eq_std, mcnK_eq_std, mslK_eq_std] at h; exact h
end AMW.Cert.PC8CL
#print axioms AMW.Cert.PC8CL.mcheckP_bridge
