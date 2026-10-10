# Independent review of the cubic-feedback interface barrier

Date: 2026-10-10. Reviewer: independent frontier/proof audit agent.

**Conclusion: PASS as an exact obstruction for the stated parameter interface, and PASS as a pure algebraic obstruction under the explicit three affine constraints. No new zero-free half-plane is proved.**

I read `zero-free/feedback-interface-barrier.md`, its original symbolic audit and its standard-library successor. I independently ran the original 36-item exact audit and the standard-library 38-item audit, preserving their separate output records in this audit directory. Both passed. The latter output is `feedback-interface-stdlib-independent.json`; all rational-function identities are checked by exact polynomial cross multiplication. Decimal values are for orientation, not sign certification. The continuous sign arguments are supplied in the written proof.

## Critical count and balanced geometry

For `alpha=5/6`, `37/50<=kappa<=1` and `1/50<=delta<=3/4`, the denominators `D`, `P`, `J` are strictly positive. The displayed finite-difference identity proves that the count `R_kappa(delta)` is increasing in kappa and strictly decreasing in delta. The critical solution `R=2/3` is unique and lies in `(3/8,1/2)`, wholly inside the actual count rectangle and below kappa. Neither a floor boundary nor a zero-capacity point is substituted for it.

In the balanced interface `M=1-e`, `h=(1+3e+b)/2`, `1/6<=e<=1/5`, the retained low inequality forces `e>=a=11/3-4B`; this already excludes `B<13/15`. At the actual moving count crossing, the high endpoint's b coefficient cancels exactly. At the more optimistic `kappa0=2B-1` and `d0=(5-9a)/(6+18a)`, the exact identity is

`R_kappa0(d0)-2/3 = p(a)/(2*(3a+1)*(153a^2-201a-20))`,

where `p(a)=657a^3-954a^2+21a+20`. For `eStar<a<=1/5`, both numerator and denominator are negative. Thus the actual crossing exceeds `d0`, and the retained endpoint expression is strictly positive for every allowed `e>=a`. The reference kappa0 can be below the proved `37/50` threshold; its use is solely an optimistic algebraic comparison with the actual admissible kappa, not a call to an unproved prime/count theorem outside its range.

This proves the current balanced parameter certificate cannot reach a bound below `sigmaStar=11/12-eStar/4`, approximately `0.874957019420098946`. It does not construct a bad arithmetic row, an actual zero or a counterexample to a stronger analytic method. In a contradiction argument actual kappa is constrained by the zero supremum beta; using `kappa>=2B-1` with beta>B is a valid relaxation. The obstruction concerns this fixed nonpositive endpoint certificate, rather than excluding arguments that use further beta-B information.

## General three-constraint statement

The more general statement explicitly assumes `B>=L0`, `B>=LK` and `B>=H_delta` for arbitrary real M,e and the moving crossing. The positive weights `(4+18delta,2,3)/(9+18delta)` cancel both M and e and give `B>=G(delta)=(18delta+7)/(18delta+9)`. Since delta exceeds 3/8, B exceeds 55/63. The same exact cubic identity and `G(d0)=B` exclude `B<sigmaStar`. At the stated star parameters, the three affine bounds meet, so the reduced model's bound is sharp.

The paper does **not** prove every possible physical general geometry must satisfy these three constraints. The report properly keeps that missing implication separate. This review likewise does not turn the reduced-model result into optimality of the whole source parameter system or of all arithmetic approaches. [Liu's fixed v1, Section 25](https://arxiv.org/html/2610.12234v1#S25) is a relevant comparison for a fixed-kappa three-constraint elimination, not a replacement for the moving-kappa proof.

## Rounding and the next numerical target

Restricting a continuous slot budget to integral whole slots cannot improve its optimistic minimum. With fixed finite K and the same uniform contracts, dyadic grid errors of size `O(1/log U)` change only constant/subpower factors, rather than creating a fixed `U^(-chi)` saving. The report correctly leaves open genuine arithmetic sparsity, new signed probe estimates and new correlations; it does not claim all integer structure is powerless.

For the unproved target `B=17499/20000`, the legal point `delta=19429/50000`, optimistic kappa `7499/10000` yields two positive exact gaps. If the two low terms stay fixed and `0<h<1`, an actual count saving must exceed

`1875081893/615723531225000 + 52361/1500000000`

`= 467366968772963/12314470624500000000`, approximately `0.00003795266422927858`.

This is a necessary local budget, not an attained saving or sufficient global certificate. It still requires an actual estimate, the remaining rectangle and all physical side conditions.

## Mixed-budget sharpness supplement

I independently read `mixed-budget-sharpness.md`. Its construction `N=floor(U^R)`, constant squared amplitudes `|M|^2=U^(delta*rLong)` and `|P|^2=U^(1-R)` meets all four stated marginal budgets with constant one, while the mixed sum is at least `U^(1+delta*rLong)/2`. Thus no uniform fixed power saving follows from those budgets alone. The split into `S^2 Q` is correct under `2delta*m+2qz=1-R`.

The long inverse polynomial exponent `rLong=3/(5-6delta)` is clearly distinguished from the physical total slot length eStar, and all exponents use the same U. The model is a finite scalar family, not a family of Hecke polynomials. It therefore proves logical insufficiency of the listed marginal inequalities, not failure of the desired actual arithmetic mixed moment. New information forbidding coincident peaks remains a legitimate research route.

## Formalization and inherited theorem scope

A read-only inspection of the separate formalization's current `docs/proof-status.md` confirms that `ArithmeticProbeObligation` has no proved inhabitant, and that the complete four-field Moments record, actual reflected low estimate and full raw-high assembly remain open. Existing generic continuation and energy statements do not close them.

The written cubic boundary theorem is relative to its explicit arithmetic input package, including the all-Hecke 7/8 bootstrap for the original fixed quadratic field. The present algebra does not strengthen that bootstrap, instantiate all missing physical data or certify a new unconditional theorem in Lean. The obstruction and the mixed scalar example can be published as precisely scoped research results without changing the claimed zero-free boundary.
