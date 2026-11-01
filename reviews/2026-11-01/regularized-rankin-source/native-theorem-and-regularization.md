# Native source review: regularized Rankin-Selberg theorem

2026-11-01; /root/regularized_rankin_native. Terminal source review for ROOT consumption, not ROOT settlement, a mathematical contract or a new proof budget. Same G20261027/runtime1793085111 and original0c4f baseline; C071 remains spent/stopped. I recovered README/STATE/check/show, the active Goal, stopped C071, latest Y/causal review and current frontier before choosing evidence. No authority file, library, cadence or earlier proof was edited.

Primary: Don Zagier, [The Rankin-Selberg method for automorphic functions which are not of rapid decay](https://people.mpim-bonn.mpg.de/zagier/files/rankin-selberg/fulltext.pdf). The actual author-hosted scanned PDF has23 pages,797019bytes, SHA25640185aae600eebeca965d39de504c5468179fdfdb7db19fae0f03b1f66a640b1. Local original: literature/local/2026-11-01-zagier-regularized-rankin/zagier-regularized-rankin-author.pdf. I independently verified the file pin and visually inspected PDFindices0,1,4-10: printed415-416 minimum definitions(1)-(8), printed419 main theorem(13)-(19), printed420-424 direct proof(20)-(28), and printed424bottom/425 definitions(29)-(32). The shared-page product remarks only clarify the same renormalizable class. Later applications, triple-Eisenstein formulas, reference proofs and any other paper are not consumed. The numerical illustrations on indices2-3 are not inputs to this review. No OCR extraction is treated as evidence.

## 1. Native domain, measure and completion

Let M=PSL2(Z)\H and dmu=dx dy/y^2, with cusp width1. The native input is a continuous complex-valued invariant function F with constant Fourier coefficient a0(y) and a FINITE cusp expansion

    F(x+iy)=phi(y)+O(y^(-N)) for every N,
    phi(y)=sum_i (c_i/n_i!) y^(alpha_i)(log y)^(n_i),
    c_i,alpha_i in C, n_i in nonnegative integers.                 (13)-(14)

This is the full cusp expansion used by the proof, not a hypothesis merely about one finite list of Fourier coefficients or a free growth bound on a physical source. The number of terms, exponents and all remainder constants depend on F; the theorem gives no uniform original-du/Dlog source operator estimate over a new family r->F_r.

The standard Eisenstein series has E(z,s)=sum_(Gamma_infinity\Gamma)Im(gamma z)^s for Re s>1 and invariant measure as above. The paper's zeta*(w) is

    Lambda(w)=pi^(-w/2) Gamma(w/2) zeta(w)=Lambda(1-w),
    E*(z,s)=Lambda(2s)E(z,s).

Lambda is meromorphic with poles at0,1. It is NOT the entire xi(w)=w(w-1)Lambda(w)/2. E* is holomorphic away from s=0,1 and satisfies E*(z,s)=E*(z,1-s). This functional equation is a meromorphic linear identity; it is not a positive Hermitian pairing or a proof of any zero location.

## 2. Main theorem with its pole and residue qualifications

For Re s sufficiently large define

    R(F;s)=integral_0^infinity [a0(y)-phi(y)] y^(s-2)dy,
    R*(F;s)=Lambda(2s)R(F;s).                                  (15)-(16)

The theorem gives meromorphic continuation. The only POSSIBLE poles of the uncompleted R are at0,1,alpha_i,1-alpha_i and rho/2, where rho is a nontrivial zeta zero. Possible poles may cancel; the list does not assert their presence or constrain rho to the critical line. More precisely,

    R*(F;s)=sum_i c_i [ Lambda(2s)/(1-alpha_i-s)^(n_i+1)
                      +Lambda(2s-1)/(s-alpha_i)^(n_i+1)]
                +an entire function divided by s(s-1),           (17)
    R*(F;s)=R*(F;1-s).                                          (18)

If no alpha_i equals0 or1, the usual simple-residue formula at s=1 has the ordinary integral interpretation when F is integrable, namely when all Re alpha_i<1. For such an ordinary integral the uncompleted normalization is

    Res_(s=1) R(F;s)=(3/pi) integral_M F dmu.                     (8)

The alpha=0 or1 cases require the explicit extra terms described below; raw R-residues must not be used as renormalized volumes in those cases. If theta=max_i Re alpha_i<1/2, the ordinary Rankin-Selberg identity holds in theta<Re s<1-theta, as an identity away from poles. This convergence strip is a real hypothesis, not automatic for the nonrapid class.

## 3. Direct proof and complete boundary terms

The proof unfolds the truncated fundamental domain D_T, retaining the horoball correction, initially in an absolute-convergence half-plane. It then uses the COMPLETE constant term

    e(y,s)=Lambda(2s)y^s+Lambda(2s-1)y^(1-s),

with the removable s=1/2 value given by the log term in(24). The nonconstant part E*-e is entire in s and rapidly decreasing in the cusp. With

    h_T(s)=sum_i (c_i/n_i!) (d/ds)^(n_i)
                         [T^(s+alpha_i-1)/(s+alpha_i-1)],         (26)

the decisive exact identity is

    R*(F;s)=integral_(D_T) F E* dmu
             +integral_(D\D_T) [F E*-phi e] dmu
             -Lambda(2s)h_T(s)-Lambda(2s-1)h_T(1-s).              (27)

Both boundary terms, with these MINUS signs, are required. They cannot be replaced by a scalar height subtraction or discarded separately. The integrals on the right have meromorphic continuation with only the native completed Eisenstein poles; h_T supplies the remaining explicit principal parts. Taking T=1 identifies h_1(s)=-sum_i c_i/(1-alpha_i-s)^(n_i+1), while h_T-h_1 is entire. This proves(17)-(18). Residues give(28), including the alpha=0/1 exceptions; the ordinary strip identity follows by letting T tend to infinity where the required h_T terms vanish. No exchange over a growing physical source family is provided by this argument.

The known Eisenstein continuation, constant-term formula and rapid decay of the nonconstant part are upstream native inputs. They remain CITED classical facilities here, not independently reproved from their references. I did read the displayed direct unfolding/boundary argument itself in the pinned pages.

## 4. R, completed R and RN integral are different objects

The native renormalized integral is

    RN(F)=integral_(D_T) F dmu
           +integral_(D\D_T) (F-phi) dmu -hatphi(T),              (29)
    RN(F)=lim_(T->infinity)[integral_(D_T) F dmu-hatphi(T)].      (31)

It is independent of T. The explicit formula(30), rather than an informal unweighted primitive, fixes hatphi: its derivative is phi(y)y^(-2), consistent with the invariant cusp measure. For a pure term y^alpha with alpha!=1, hatphi(y)=y^(alpha-1)/(alpha-1); for alpha=1 it is log y. Log powers use precisely the factorial/derivative conventions in(30).

When no alpha_i is0 or1,

    Res_(s=1)R*(F;s)=RN(F)/2.                                  (32)

For general cusp expansions the paper first corrects R* by

    +sum_(alpha_i=0) (-1)^(n_i)c_i Lambda(2s)/(s-1)^(n_i+1)
    -sum_(alpha_i=1) c_i Lambda(2s-1)/(s-1)^(n_i+1),

then takes the simple residue. In particular F=1 has a0=phi=1 and R(1;s)=R*(1;s)=0, whereas hatphi(T)=-1/T and Vol(D_T)=pi/3-1/T give RN(1)=pi/3. The alpha=0 correction has residue Lambda(2)=pi/6, correctly RN(1)/2. Thus a zero of the raw transform is not a zero renormalized volume, let alone the project's physical principal relation.

## 5. Checked native negative-square control

The proposed control is valid with the native normalization, without any conditional convention. In the embedded cusp y>2 choose a smooth chi with0<=chi<=1, chi=0 at/below2 and chi=1 at/above4. Define H(z)=y chi(y) in that cusp and0 outside, extending as an invariant smooth function on M. It is well-defined because this is the width1 embedded cusp; vanishing near its lower boundary makes the extension smooth. Then

    F=H conjugate(H)=chi(y)^2 y^2>=0,
    phi_F(y)=y^2, alpha=2, n=0, hatphi_F(T)=T.

For T>=4,

    integral_(D_T) F dmu=integral_2^4 chi(y)^2dy+(T-4),
    RN(F)=integral_2^4 chi(y)^2dy-4 < -2.                         (33-control)

The strict inequality follows from the smooth transition: chi is strictly below1 on a nonempty interval near2, so its squared integral is strictly below2. This is an actual square in the native renormalizable class. Consequently RN(H conjugate(K)) is not automatically a positive Hilbert Gram on that WHOLE nonrapid class. The measure, sign and coefficient are independently checked against(29)-(31), not guessed by subtracting an arbitrary counterterm. For this alpha=2 example(32) also applies; its completed residue is RN(F)/2, with the same negative sign.

This control has a limited role. It does not rule out an indefinite Hodge intersection, a primitive/sign-corrected restriction, another relative pairing, a signed same-object comparison or a differently supplied positive subspace. RN agrees with the ordinary integral on the integrable part of this native class. No claim that all regularized or all modular Weil routes fail follows from one negative square. The classical SOURCE0 recommendation below depends on the missing physical bridge, not on that false generalization.

## 6. Consumption recommendation and exact unpaid bridge

The function class is closed under products and conjugation, so native mixed RN pairings can be formed. This gives a genuine regularized analytic facility. It does NOT supply a map from ALL physical complex r=e^(u/2)f to an actual primitive automorphic/cohomological carrier, prove the image of the full noncompact405 relations, retain537 nonroot plus full-source coverage, or transport original du/zero-extension Dlog and growing-window/source seminorms. It does not identify RN(H_r conjugate(H_s)), R(H_r conjugate(H_s);s), or the residue above with the complete classical Weil pairing including its Gamma/contact, all proper powers and both poles. The factor Lambda(2s), its parameter roles and its residue exceptions cannot be silently replaced by entire xi on the required source line.

Old545 already consumed the full mixed Maass-Selberg/quarter-line/direct-packet/cusp scope. This new main theorem's nonrapid subtraction is a different native identity, but it supplies no new paid signed-core/cofactor/principal bridge by itself. Fixed17/16 full-complex positivity, finite9/8E448, same605 ONE-head/all-complement positive completion,560/602 whole identities and whole4/5 negative-inertia UPPER are unchanged. The actual principal/sections/mixed/growing signed-core/coupling bottleneck and all three Goal gates remain open.

Recommendation: **genuine native CITED facility; classical SOURCE0; standard/native-control increment0.** Keep the R/R*/RN distinctions and the negative-square control as precise source qualifications. No C072/607, cadence change, new mathematical responsibility or follow-up application/chapter/paper queue is authorized by this review. Stop this source gate after ROOT reconciles its separate old-scope record and any final review.
