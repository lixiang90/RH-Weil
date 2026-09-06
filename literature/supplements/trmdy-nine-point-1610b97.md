# The nine-point record: 0.673311015335876…

A position-weighted **nine-point** (eight-gap) inequality on the same
certified window, replacing the seven-point certificate as the record
constituent:

    F(g₁..g₈) = (1/2500) Σ gᵢ + Σ_{0≤i<j≤8} a_ij w(y_j − y_i) ≥ 60817/10⁷

for all nonnegative gaps, with exact rational weights (denominator 10⁷,
reflection-symmetric, all eight span capacities exactly 2; see
`data/candidate-nine-point-p2500.json` and `src/zeta_ext/nine_point.py`).

**Certificate:** `certificates/nine-point-p2500-grid4000.txt` — exhaustive
interval subdivision, grid 1/4000, **116,580,892 nodes, depth 75**, 80
workers, 8140 s. Float minimum 0.0061000893…, margin 0.30146%; validated
pre-certification by exhaustive pressure-feasible zero-tuple enumeration
(3,003 tuples) plus ~45k unfiltered multistarts, independently reproduced
to 14 digits by a second lane.

**Assembly** (refined deduction, `docs/refined-deduction.md`): with
q = 8, m = 177, A = ε(m−q) = 1.0278073, Φ₁₇₇(A) = 1.02768760779…,
B_p = 8/2500:

    bound = (177·H_cert − 169·(8/2500)) / (177 − Φ₁₇₇(A))
          = 0.673311015335876023560779537187…  >  673311/10⁶.

Record: `certificates/nine-point-fast.txt`.

Nine points reach pair spans of eight gaps, capturing kernel energy toward
the horizon-8 ceiling (≈ 0.67340) that no seven-point certificate can see;
the campaign's ground-state analysis and exhaustive design search (LP master
gap 4.8·10⁻⁸) indicate this family is now within ~2·10⁻⁶ of exhausted.

## Final LP-converged variant: 0.673312742272245998…

The design LP was driven to convergence (master gap 4.8·10⁻⁸); the final
candidate (`data/candidate-nine-point-final.json`, target 15211/2500000,
margin 0.30037%, dual-lane validated to 13 digits with a doubled-budget
deep pass) was certified as a **cross-host split**: shards [0,64) of 96 on
trmd-metal-3 (78,458,316 nodes) and [64,96) on trmd-metal-4 (37,814,110
nodes), identical rigorous-table SHA-256 hashes on both hosts, disjoint
ranges covering every initial box. Record:
`certificates/nine-point-final-grid4000.txt`. Assembly at m = 177 gives

    0.673312742272245998143847403168…  >  6733127422/10¹⁰.

