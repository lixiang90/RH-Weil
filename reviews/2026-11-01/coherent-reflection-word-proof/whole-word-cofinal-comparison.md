# C071 actual whole-word comparison: all denominators are nonzero

2026-11-01; /root/c071_word_algebra_proof. This is an actual proof contribution to the SAME ONE C071 attempt, not a new task budget or an authority-file settlement. Same G20261027/runtime1793085111 and original0c4f. The current Goal/STATE/check/show, C071, latest X/frontier and actual formation/wording limits were recovered. No web/PDF/source search, numerical pilot, science code, parameter change or authority edit is used.

## Result and exact remaining gap

Let F be any nonempty finite set of actual primes, ordered increasingly, and use the exact full-Gram projections of560 and the frozen relative factors

    W_F=product_(p in F, increasing written order) V_p,
    V_p=(2Pi_p-I)(2P-I).

Write p_star=max F. Then, in the ORIGINAL receiver Hilbert norm,

    ||W_F-I||op >= 2/p_star > 0.                                  (1)

Consequently, for the actual old591 source g and every integer j>=1,

    b_j=C_j(g,g)>0.                                               (2)

This removes the infinitely-many-zero-denominators branch of C071 and makes both frozen ratios well defined at EVERY layer. It does **not** give a quantitative lower bound on b_j, a normalized row-tail estimate, either ratio limit, or a rejection/pass of the fixed word. In particular (1) is a receiver operator norm statement, not a fixed-source energy bound. The main two-ratio comparison remains OPEN.

## 1. Paid source and moving upper boundary

Only one old analytic input is needed beyond standard strong-operator calculus: the actual532 full Sonin clipping estimate, explicitly stated with ALL finite intervals J, independently of position, length and endpoints. In physical log coordinates, for R large, with T_R=Gamma(R)=2 theta'(R)>0,

    ||P(e^(iRy)1_J)-e^(iRy)1_(J intersect [0,T_R])||2
       <= c_P R^(-1/4).                                         (3)

This is notes/532-actual-sonin-prime-symbol-and-compact-weil-bridge.md §2,(3). Its precise uniform quantifier is also retained in reviews/2026-10-14/joint-sonin-cross/full-inverse-carrier-error.md §1,(1). It includes the actual double-boundary Sonin projection and inverse; it is not a replacement by a single Hardy edge. T_R tends to infinity. No new uniform-in-F carrier estimate is claimed here.

Let M_R h(y)=e^(iRy)h(y), let U_a h(y)=h(y-a), and put

    S_R=M_R U_(T_R),
    P_R=S_R* P S_R,
    E_-=1_(-infinity,0).

For every fixed bounded interval J, apply (3) to the legal, moving interval J+T_R. After the unitary conjugation this gives

    ||P_R 1_J-1_(J intersect [-T_R,0])||2 <= c_P R^(-1/4).

For R large the latter indicator equals E_-1_J. Finite linear combinations of compact interval indicators are dense in L2(R); P_R and E_- are contractions. Hence

    P_R -> E_- strongly as R->infinity.                           (4)

The moving interval in this step is legal precisely because the OLD estimate has the all-interval quantifier. A fixed-J-only clipping statement would not prove (4).

## 2. Exact full-Gram factors pass to a half-line model

Fix F for this entire section. Conjugating the ambient translations gives

    S_R* U_l S_R=e^(-iRl)U_l.

Thus for each p in F, l_p=log p and q_p=p^(-1/2), the exact transformed B_p is

    B_(p,R)=I-alpha_(p,R)U_(l_p),
    alpha_(p,R)=q_p e^(-iR l_p).

Since F is finite, take a sequence R_n->infinity on which every alpha_(p,R_n) converges to alpha_p, |alpha_p|=q_p. This is ordinary compactness of a finite product of circles, not a simultaneous Diophantine estimate and not a uniform growing-F phase selection.

On the full H define the block extension

    C_(p,R)=P_R B_(p,R)*B_(p,R)P_R+(I-P_R).

It satisfies the uniform bounds

    (1-q_p)^2 I <= C_(p,R) <= (1+q_p)^2 I.

From (4), norm convergence of B_(p,R_n), and boundedness, C_(p,R_n) converges strongly to

    C_(p,-)=E_- B_(p,-)*B_(p,-)E_-+(I-E_-),
    B_(p,-)=I-alpha_p U_(l_p).

The lower bound proves strong convergence of their inverses: use

    C_(p,R)^(-1)-C_(p,-)^(-1)
      =C_(p,R)^(-1)(C_(p,-)-C_(p,R))C_(p,-)^(-1).

Therefore the exact conjugated projection converges strongly to

    Pi_(p,-)=B_(p,-)E_- C_(p,-)^(-1)E_- B_(p,-)*,

the orthogonal projection onto the CLOSED subspace B_(p,-)Ran(E_-). Closedness follows because B_(p,-) is boundedly invertible, with inverse norm <=(1-q_p)^(-1). All full Gram inverses were retained; no finite inverse truncation or scalar reciprocal was substituted.

Consequently

    S_(R_n)* W_F S_(R_n) -> W_(F,-) strongly,
    W_(F,-)=product_(p in F, increasing written order)
                (2Pi_(p,-)-I)(2E_--I).                          (5)

Only finite products occur. No pairwise commutation is assumed. The largest-prime factor still acts first.

## 3. Largest-prime corner of the exact half-line model

For a single l>0 and alpha with |alpha|=q<1, set B=I-alpha U_l and let Pi_alpha project onto B Ran(E_-). Its range is supported in (-infinity,l), since B moves a negative-half-line input by at most l. Let E_(0,l) denote the future strip (0,l). We claim the EXACT compression

    E_(0,l) Pi_alpha E_(0,l)=q^2 E_(0,l).                         (6)

Here is a direct proof, with no finite-dimensional fit. Inside E_l H=L2((-infinity,l)), the orthogonal complement of B Ran(E_-) consists of h such that

    E_- B* h=0,
    h(y)=conjugate(alpha) h(y+l) for y<0.

Thus a future-strip value f in L2((0,l)) determines every past strip:

    h(s-nl)=conjugate(alpha)^n f(s),
    0<s<l, n=0,1,... .

Its norm squared is ||f||2^2/(1-q^2). The normalized map

    J_alpha f(s-nl)=sqrt(1-q^2) conjugate(alpha)^n f(s)

is an isometry onto that complement. The complement projection is J_alpha J_alpha*, whose compression to (0,l) is (1-q^2)I. Since Pi_alpha=E_l-J_alpha J_alpha*, equation (6) follows. The phase of alpha disappears from this compression.

Now put l_star=log p_star. Let l_prev be the largest log p among the other primes, or0 if F has one prime. The open strip

    I_star=(l_prev,l_star)

has positive length. For every smaller prime, both E_- and Pi_(p,-) vanish on I_star, because Ran(Pi_(p,-)) is supported in (-infinity,l_p). Hence its relative factor acts as identity there, on both sides:

    E_star V_(p,-)=E_star=V_(p,-)E_star.

The increasing written order now gives

    E_star W_(F,-) E_star=E_star V_(p_star,-) E_star.

On the positive strip the base reflection 2E_--I acts as -I. Apply (6) to obtain

    E_star(W_(F,-)-I)E_star=-2 q_(p_star)^2 E_star.                (7)

This corner cannot be canceled by the smaller-prime factors. This is an actual ordered-word conclusion; it does not assert that the different factors fail to commute pairwise. It also uses the precise ordering fixed in C071 rather than changing it for convenience.

## 4. Return to the actual word and the actual fixed source

Strong limits do not increase a uniform operator norm. Unitary conjugation preserves the operator norm, so (5)-(7) imply

    2q_(p_star)^2
       <= ||W_(F,-)-I||op
       <= ||W_F-I||op.

This proves (1) for EACH fixed finite F. Applying it separately to every F_j={p<=exp(j)} gives

    ||W_j-I||op >= 2/p_max(j) >= 2e^(-j),   j>=1.                (8)

There is no exchange of R->infinity with j->infinity: (8) is a universally quantified consequence of the fixed-F argument. It supplies no uniform model-approximation rate or source-energy comparison in a joint R,j limit.

Formation already paid that W_j-I has a continuous actual Fourier kernel K_j(t,v) and that

    [W_j,M_G] has HS kernel (G(v)-G(t))K_j(t,v).

For the SAME old591 g, G=|psi_hat|^2 is nonconstant real-analytic: G(0)=1 and G tends0 at infinity. Every real level set of G has measure zero. Fubini therefore says that G(t)=G(v) is a null subset of R2. If C_j(g,g)=0, its nonnegative summands force [W_j,M_G]=0. Its kernel then vanishes, so K_j vanishes almost everywhere off that null set; continuity forces K_j=0 everywhere. Thus W_j=I, contrary to (8). This proves (2).

The source role must not be lost in this argument. In fact

    S_R* A_g S_R=A_(e^(-iR dot) g),

which is NOT the same fixed g. Therefore the high-frequency boundary corner in (7) cannot be inserted as a lower bound on the original b_j=C_j(g,g). The proof uses it only to rule out the operator identity W_j=I, and then uses the actual fixed-source analytic-kernel argument qualitatively. It does not control how small b_j may be.

## 5. Cofinal test verdict and strongest-old net scope

The two frozen ratios are now defined for ALL j. The zero-denominator rejection alternative is false for this actual word. The proof does not determine whether

    C_j(tau_(1/2)g)/b_j ->1,
    C_j(g')/b_j ->q1/q0,

or whether their maximum error has positive limsup. Nor does it bound B_j(delta)/b_j. Source-independent common positive c_j may still grow without bound; no bounded-calibration hypothesis was introduced. Passing or rejecting the family remains unproved.

The new-to-this-attempt consequence is the largest-prime boundary corner and its actual whole-word nonidentity/all-layer denominator conclusion. Its dependencies are the old actual532 uniform moving-interval clipping, exact full inverse stability and standard half-line geometry. Kernel legality and initial C1 nonzero were already paid and are not re-counted. The above is not a new classical arithmetic input or improved full-Weil bound. No principal405 descent, full537 coverage, integral sections/mixed RR, growing signed-core/coupling or Xi result follows; whole17/16, finite9/8, ONE605-head/all-complement completion and whole4/5 negative-inertia UPPER are unchanged.

Classify (1)-(2) as a precisely scoped actual partial proof, subject to independent reverse audit and ROOT's strongest-old/net settlement. The remaining normalized fixed-source tail/ratio comparison is genuinely OPEN; receiver operator distance is not a substitute for it. This document does not renew C071, start another contract, change the order/cutoff/source/gain/receiver, or queue external sources/numerics. The ONE attempt must be settled by ROOT under its existing stop rule even if the main ratios remain unresolved.
