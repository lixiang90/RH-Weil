# Bellman-coboundary proof record

## Theorem

With the nonnegative window `v(s)=cos(1.47 s)` on `[-1/2,1/2]`, the certified
unconditional lower bound is

`liminf N_0^s(T,2T)/N(T,2T) >= 0.6731929114731422535099843283...`.

Unconditional means no Riemann-hypothesis, pair-correlation, or zero-density
conjecture is assumed.  The repository rerun passed; external independent
audit and peer review remain pending.

## Coboundary

For six gaps, let `F_0` be the uniform seven-point functional and define

```text
U(g1,...,g5) = (54 g1 - 123 g2 + 123 g4 - 54 g5)/1920000
               + 5971/300000 [w(g1)+w(g2)-w(g4)-w(g5)]
F_B(g1,...,g6) = F_0(g1,...,g6) + U(g2,...,g6) - U(g1,...,g5).
```

The redistributed coefficients are

```text
p = (946,1177,877,877,1177,946)/1920000
q = (31343/100000, 1/3, 105971/300000, 105971/300000, 1/3, 31343/100000).
```

They satisfy `sum(p)=1/320`, `sum(q)=2`; longer-span coefficients still sum
to `2`.  Thus the coboundary telescopes on periodic sequences while retaining
nonnegative finite-block pressure.

## Directed certificate

The kernel table is a 4,000-grid, 43,247-cell CWK2 file (SHA-256
`13213b84960fa629db0eac3ed7891148066313cba84f4fa151cfcce749d8fc2c`).  The
derivative table is an independent directed-MPFR 4.2.1 CWD2 reconstruction
(SHA-256 `035946b4368fbeab578720109039bb409877f2c3728b672a1c1daff6c3e6f375`;
the unavailable source package listed a different expected hash).

The GMP-backed C++20 verifier checks convex-tangent bounds.  Every binary64
endpoint is converted to an exact dyadic GMP rational and the Hessian is
rechecked by exact-positive-definite LDL.  All 64 initial boxes return
`verified=true` and prove `F_B >= 577/100000`.

```text
nodes=1126636  splits=563286  pressure=3477
interval=318922  tangent=240951  depth=55  unresolved=0
1126636 - 563286 = 3477 + 318922 + 240951 = 563350.
```

## Block conversion

For `m=183`, summing the seven-point inequalities gives
`E_m + P_m >= (577/100000)(m-6)`.  The redistributed pressure has total
`(m-6)/320`; averaging yields the tax `59/19520`.  The trace-energy envelope
in `docs/trace_energy_envelope.md` then gives
`B=1.0212287852929821661489401766...` and the final bound

```text
(H_alpha - 59/19520)/(1 - B/183)
  = 0.6731929114731422535099843283718888...
```

## Reproducibility and provenance

Run `powershell -ExecutionPolicy Bypass -File scripts/verify.ps1`.  It uses a
fresh repository-local `.tmp_test_zeta_verify_$PID` directory, regenerates and
byte-compares both tables, compiles the GMP verifier, and checks all 64 boxes.
The analytic framework is attributed to the pinned `ainta/zeta-simple-zeros`
commit only for its coarser `min(1,E)` lemma; the stability-enhanced envelope
and this Bellman argument are repository contributions.  See
`docs/provenance.md` for the Anthropic Section 7.1 source and trust boundary.
