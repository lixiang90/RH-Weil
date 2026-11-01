# Final independent scope review: regularized Rankin source

2026-11-01; /root/regularized_rankin_fresh, exclusive output. **Scope PASS, with the restrictions below.** This reviews source consumption and the elementary native controls, not a new mathematical contract, a classical Weil bridge or ROOT settlement. Same G20261027/runtime1793085111 and original0c4f baseline; C071 remains SPENT/stopped and its main normalized ratios OPEN. No authority, cadence, library, board or earlier proof file was edited by this reviewer.

## 1. Exact inputs and actual independent inspection

I read all four complete terminal inputs, not only their conclusions, and independently verified their byte/SHA256 identities:

| Input in this folder | Bytes | SHA256 |
| --- | ---: | --- |
| old-scope-and-bridge-obligations.md | 12710 | eff1dd7dfde9459eab1eb9ed2d6c9e7abd0f52d7007c0da555ddb5eef681e9a4 |
| native-theorem-and-regularization.md | 10678 | 8c2dbc6d6a6c98884f951db370ec49d76e37b18c1bf53ef73448c1a8eac067dd |
| root-typed-controls.md | 5368 | 8606827179166a228c5b63148a94e8b1e8aea92f5c1899d8e9623a17306171d3 |
| scope-and-source-gate.md | 3360 | 5dda0c05c50c8f360d1bd23e4dc4465ce1650927408921b6b8588deac2950845 |

The primary is Don Zagier, [The Rankin-Selberg method for automorphic functions which are not of rapid decay](https://people.mpim-bonn.mpg.de/zagier/files/rankin-selberg/fulltext.pdf), the locally pinned author-hosted scan at literature/local/2026-11-01-zagier-regularized-rankin/zagier-regularized-rankin-author.pdf. I independently verified797019bytes/SHA25640185aae600eebeca965d39de504c5468179fdfdb7db19fae0f03b1f66a640b1. The native reader records23 scanned pages. I visually inspected existing PNG indices0,1,4,8,9,10: printed415-416 definitions/measure,419 main theorem,423 equation26 and its rearrangement,424 equation27/residue28/RN29,425 primitive30/limit31/residue32 and its exceptions. No new PDF, web search, application, reference proof, numerical example or code experiment was used. The intervening direct-proof pages5-7 were read by the separate native reader; I do not mislabel that reader's complete proof inspection as my independent pixel inspection.

Recovery checked current README/STATE, research_state check and show, active Goal, stopped C071, current frontier/decision Y and latest causal stop. Structural check passed; it is not mathematical certification. Actual STATE identifies this one source gate as pending independent review, not a revived C071 proof. Current changes in the shared tree belong to ongoing ROOT work; their existence does not grant further scope. This child makes no independent live-runtime claim about the parent's Goal beyond the pinned observation and task identification.

## 2. Native domain, norm and object roles

The invariant measure is dmu=dxdy/y^2, with width-one cusp. The main theorem requires a continuous invariant F and a FINITE expansion

    phi(y)=sum_i c_i y^(alpha_i)log(y)^(n_i)/n_i!,
    F(x+iy)-phi(y)=O(y^(-N)) for EVERY N as y->infinity.

This is not merely slow growth. The all-N constants and finite exponents are attached to the particular F; there is no supplied uniform physical-source/growing-window norm estimate. Multiplication and conjugation preserve this native class, so native mixed products are legal. They still require an actual map from physical sources before they can establish physical coverage, common source norms or a full Weil identity.

The four objects remain distinct:

| Object | Native role | What it does not automatically provide |
| --- | --- | --- |
| R(F;s) | Linear subtracted Mellin transform of a0-phi, initially Re s sufficiently large | RN volume, positive Gram or holomorphic cofactor |
| R*(F;s)=Lambda(2s)R(F;s) | Completed meromorphic transform with functional equation | Entire xi, transported zeta-zero multiplicities or a positive pairing |
| RN(F) | Linear finite-part modular integral with the prescribed primitive | Positive Hilbert norm on the whole native class |
| Ordinary Gram | Integral of an integrable product, when its ordinary domain is justified | A finite-part value for divergent products |

Here Lambda(w)=pi^(-w/2)Gamma(w/2)zeta(w), the paper's zeta-star, is MEROMORPHIC, unlike xi(w)=w(w-1)Lambda(w)/2. In particular the theorem explicitly allows raw R to have poles at rho/2. A zero of Lambda(2s) can cancel a raw-R pole. The displayed factor Lambda(2s)R therefore does not alone prove that R* contains all zeta zeros with a holomorphic cofactor or transported multiplicities. The distinct old diagonal Rankin entire-cofactor statement cannot be imported into this transform.

The native s->1-s equation becomes w->2-w for w=2s. The actual classical zeta critical line Re w=1/2 is Re s=1/4, distinct from the Eisenstein unitary line Re s=1/2. These parameter distinctions were already paid in545, so they are not a new result of this review.

## 3. Critical formula and normalization checks

The page419 theorem agrees with the native terminal record: finite power/log hypotheses, raw possible poles0,1,alpha_i,1-alpha_i,rho/2, completed principal-part formula17, functional equation18, and ordinary identity19 only in its stated theta<Re s<1-theta strip with theta<1/2. A possible/simple pole statement is not an assertion that every residue is nonzero.

Pages423-424 independently confirm

    h_T(s)=sum_i (c_i/n_i!) partial_s^(n_i)
                    [T^(s+alpha_i-1)/(s+alpha_i-1)],
    R*=integral_(D_T) F E* dmu
       +integral_(D\D_T)(F E*-phi e)dmu
       -Lambda(2s)h_T(s)-Lambda(2s-1)h_T(1-s),
    e(y,s)=Lambda(2s)y^s+Lambda(2s-1)y^(1-s).

BOTH boundary terms in equation27 have MINUS signs. The entire mixed cusp subtraction phi e is retained. Neither dropping a term nor choosing independent finite-part constants is licensed. Upstream Eisenstein continuation and its cusp expansion remain cited inputs, not newly established by this source review.

Although the prose calls hatphi an antiderivative, equation30 fixes the weighted primitive: hatphi'(y)=phi(y)/y^2. For y^alpha it is y^(alpha-1)/(alpha-1) if alpha!=1, and log y if alpha=1. It has the prescribed nonconstant power/log form; an arbitrary additive constant would change RN and is not the native convention. Equations29 and31 give

    RN(F)=integral_(D_T)F dmu
          +integral_(D\D_T)(F-phi)dmu-hatphi(T)
         =lim_(T->infinity)[integral_(D_T)F dmu-hatphi(T)].

Equation32 gives Res_(s=1)R*=RN(F)/2 only without alpha0/1 terms. In general the corrected expression whose simple residue is RN(F)/2 is

    R*(F;s)
      +sum_(alpha_i=0) (-1)^(n_i)c_i Lambda(2s)/(s-1)^(n_i+1)
      -sum_(alpha_i=1) c_i Lambda(2s-1)/(s-1)^(n_i+1).

The alpha0 correction is PLUS and the alpha1 correction is MINUS. The supplied native record has both correctly. The constant control tests the exception: F=1 gives a0=phi=1 and R=R*=0, but hatphi(T)=-1/T and Vol(D_T)=pi/3-1/T yield RN(1)=pi/3. The correction +Lambda(2s)/(s-1) has residue Lambda(2)=pi/6, exactly RN(1)/2. No physical principal-class inference follows from a zero raw Mellin transform.

## 4. Exact negative-square control and its limited coefficient direction

Take smooth0<=chi<=1, chi=0 fory<=2 and chi=1 fory>=4. On the embedded width-one cusp let H=y chi(y), extended by0 below that cusp. This gives a smooth invariant function, not a physical405 source. Its square F=|H|^2 is in the native class with exact tail phi=y^2, alpha2 and all-N zero tail remainder. Formula30 fixes hatphi(T)=T. Thus for T>=4,

    integral_(D_T)|H|^2 dmu=integral_2^4 chi(y)^2dy+T-4,
    RN(|H|^2)=integral_2^4 chi(y)^2dy-4<-2.

Continuity and chi(2)=0 make the transition integral strictly less than2. This is a negative value on an actual native square. It refutes the automatic conclusion that RN(H conjugate(K)) is a positive Hilbert Gram on the ENTIRE native nonrapid class. The square is outside ordinary L2, so there is no contradiction with ordinary integral positivity. This example has alpha2; it does not depend on the alpha0/1 exception.

The direction is a failure of whole-class automatic positivity, not a lower bound for the physical Weil form and not a new classical negative direction. An indefinite Hodge intersection, primitive/sign-corrected restriction, relative quotient, paid signed comparison, unbounded construction or separately supplied physical image is not ruled out. Source/domain restrictions and their norms must be tested individually. The native facility may support legal signed constructions; this gate has not supplied one with the required physical identity.

## 5. Strongest-old deduction and remaining premise closure

The local old-scope record correctly distinguishes this newly reviewed author document from the older1981 Zagier and Garrett PDFs. Its bounded dedup supports one different source inspection, not novelty of every lemma or absence from every unindexed file. I rely on the pinned old-scope comparison for the historical source receipt; I did not reread the old PDFs.

Old545 already includes full two-source/four-term Maass-Selberg, removable cases, complete cusp Gram subtraction, actual quarter-line completed packets and original-norm direct compensated packets. The direct supplier is genuinely noncompact and bounded on the full original L2 line for fixedY, with a bound uniform in source-window length. Its frozen base2 blind band and compact/finite-rank repair limit retain their exact scope; paid cusp/different base/seed/noncompact/signed repairs remain legal. The old diagonal xi factor has an entire cofactor in its stated family, but diagonal cusp-square positivity does not pay all mixed cross terms. None of these old conclusions is newly proved or strengthened here.

The new native theorem supplies analytic continuation, a signed boundary identity and an RN prescription on its exact automorphic class. It does not furnish physical r=e^(u/2)f->F_r, original du/zero-extension Dlog and growing-window transport, actual405 principal descent,537 nonroot plus full-source visibility, sections/multiplication/mixedRR, or equality with the complete classical Weil pairing including Gamma=2theta-prime/FP-contact, every proper power and both poles. Products being native-admissible pays an intermediate domain, not these coverage/coupling arrows. No unbounded common calibration, source-adaptive tail or signed-core cost is closed by analytic continuation alone.

Strongest consumable classical assets therefore remain fixed17/16 full-complex positivity, finite9/8E448,605 ONE-head with ALL-complement positive completion in its one-direction scope,560/602 whole identities, and542+555->557 whole4/5 negative-inertia UPPER. The last is not PSD or a negative-inertia lower bound. There is no new whole-object consequence after deducting these assets. Actual principal/sections/mixed/growing signed-core/coupling/Xi obligations and all three long-Goal completion gates remain OPEN.

## 6. Terminal recommendation

**PASS for the stated bounded source consumption; no material formula or sign correction is required in the four terminal inputs.** Preserve the typed restrictions above in final ROOT consumption. The conditional controls in the historical old-scope memo are now confirmed by the separate native reader and this independent primary-image check; that does not retroactively make the old-scope agent a primary reader.

Recommended settlement is genuine native CITED facility, classical SOURCE0, incremental mathematics0, actual core bottleneck unchanged. The original direct proof was reviewed by the native reader; this fresh scope PASS is not a new independent proof of every upstream Eisenstein theorem or of RH. ROOT still must read and pin this terminal output before root consumption/publication. No C072,607, mathematics/cadence increment, Goal completion, application/chapter/reference/paper queue or revived C071 responsibility follows. This reviewer stops at this source gate and leaves authority updates and publication to ROOT.
