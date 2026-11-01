# C070: independent joint capture and three-ratio analysis

2026-11-01. SAME G20261027/runtime1793085111, frozen baseline0c4f.
This is one independent proof leg of the ONE C070 responsibility, not a second
contract or settlement. Only the fixed path X_j=exp(j), N_j=j^2 is considered.
No new source/PDF/web/numerics/scientific code or shared-state edit was used.

**PROVED:** a uniform, actual joint Hermite capture bound and its source-norm
consequences; an exact conditional three-test obstruction with explicit gap.
**OPEN:** the actual calibration-free delta_j, eventual positive denominator,
and the relative coherence estimate needed to apply that obstruction. In
particular, the absolute bound does NOT reject unbounded common calibration.

## 1. Object, measure and paid inputs

Use exactly the contract's actual full-Gram projection P_j=Pi_(exp(j)), not an
Euler weight or trial projection. In the receiver Mellin representation

    H=L2(R,dmu), dmu=dt/(2pi), A_r=M_f, f=rhat,
    rhat(t)=integral r(u)exp(-itu)du.

The source is the physical r=e^(u/2)bare. This calculation does not identify
native bare-du with physical r-du. Reflection check r(u)=r(-u) is complex-linear;
the adjoint source is separately r-dagger(u)=conj(r(-u)). The first slot of C_j
is linear as frozen in the contract.

Let h_n be the usual unit L2(dt) Hermite functions. The Mellin transforms of
the contract's log-Hermites are sqrt(2pi)(-i)^n h_n. Consequently the transformed
E_N has diagonal, relative to dmu, equal to 2pi sum_(n<N)|h_n(t)|^2. In all
localized traces the 2pi cancels dmu; E_N remains a receiver projection, not a
source window, multiplier, occupation R, or source E448.

The one actual arithmetic input used below is the paid fixed-eta localization
from the C052 source-localization proof, section6(4)-(5), also preserved in the
591 tail proof. For each FIRST FIXED eta>0 and B>0, the actual kernel satisfies

    sup_(eta<=|t|<=(log X)^B) k_X(t,t)
       <=exp[-(c_eta+o_(eta,B)(1))*sqrt(X)/log(X)],
    c_eta=4-4/sqrt(1+4eta^2)>0.

Here k_X=2pi rho_X includes the complete G_X inverse. No fixed-eta statement is
used at a moving eta_j. The proof below takes j to infinity before eta to zero.

## 2. Elementary Hermite estimates, with proof

Write K_N(t)=sum_(n<N)|h_n(t)|^2, N>=1. The following bounds suffice:

    K_N(t)<=2sqrt(2N)                         for every real t;       (H1)
    integral_(|t|>T) K_N(t)dt
         <=4N(N+1)^2/T^4                     for every T>0.          (H2)

For (H1), the oscillator L=-d^2/dt^2+t^2 has eigenvalues 2n+1 on h_n.
If v is a unit vector in span(h_0,...,h_(N-1)), then
||v'||_2^2<=<Lv,v><=2N-1. Its Gaussian decay permits integration of the
derivative of |v|^2 from t to infinity, giving

    |v(t)|^2<=2||v'||_2||v||_2<=2sqrt(2N-1).

Taking the evaluation supremum over this finite-dimensional unit ball gives
K_N(t) and proves (H1), including at zeros of any individual Hermite function.

For (H2), multiplication by t sends the first N Hermites into the first N+1
Hermites. The same oscillator energy bound gives, for n<N,

    ||t^2 h_n||_2^2<=(2N-1)(2N+1)<=4(N+1)^2.

Sum over n<N, then use 1_(|t|>T)<=t^4/T^4. This proves (H2). No asymptotic
Christoffel formula, moving-source estimate, or Mehler tail theorem is needed.

On the frozen path N=j^2 and T=j^2, these imply

    Tr(E_N 1_(|t|<=eta) E_N)<=4sqrt(2)*eta*j,                     (H3)
    Tr(E_N 1_(|t|>j^2) E_N)<=16/j^2.                             (H4)

These are exact receiver trace bounds in the specified measure.

## 3. PROVED actual joint capture lemma

Define the finite, nonnegative number

    b_j=sup_(||f||_infty<=1) ||P_j M_f E_(j^2)||_HS.

The supremum is over bounded measurable receiver multipliers; this is a norm
bound, not a claim that all such f are Fourier transforms of physical sources.
The claim is

    b_j^2=o(j).                                                   (J)

Fix eta>0. Split the INPUT multiplier identity into the three disjoint regions
S0={|t|<=eta}, S1={eta<|t|<=j^2}, S2={|t|>j^2}. For j sufficiently large, and
M=||f||_infty, the central contribution obeys

    ||P_j 1_S0 M_f E_N||_HS
       <=||1_S0 M_f E_N||_HS
       <=M sqrt(4sqrt(2)*eta*j),

using contraction of P_j and (H3), not an assumed diagonal model of P_j.

For the middle contribution, ordinary HS-by-bounded multiplication gives

    ||P_j 1_S1 M_f E_N||_HS
       <=||P_j 1_S1||_HS ||M_f E_N||_op
       <=M [integral_S1 k_(exp(j))(t,t)dmu(t)]^(1/2)
       <=M (j/sqrt(pi)) exp[-c_eta exp(j/2)/(4j)].

The last line uses the paid localization with B=2 and FIRST FIXED eta. The
trace of P_j 1_S1 is legitimate by its finite-interval kernel diagonal; no
bare trace of P_j or full unweighted multiplier was taken.

For the far contribution, use contraction of P_j and the Hermite tail:

    ||P_j 1_S2 M_f E_N||_HS
       <=||1_S2 M_f E_N||_HS<=4M/j.

The triangle inequality therefore gives, uniformly in all bounded f,

    b_j<=sqrt(4sqrt(2)*eta*j)
             +(j/sqrt(pi))exp[-c_eta exp(j/2)/(4j)]+4/j.           (J1)

First let j grow with this eta fixed. Then
limsup b_j^2/j<=4sqrt(2)*eta. Since eta was any positive fixed number, (J)
follows. This is an ACTUAL joint X,N comparison: no fixed-X exhaustion and no
exchange of two limits was used. E_N was retained as an operator in every
inequality; it was never replaced by a frequency weight or by an occupation.

In particular, f=1 gives ||P_j E_N||_HS<=b_j. Thus for every bounded f,

    ||[P_j,M_f]E_N||_HS
      <=||P_j M_f E_N||_HS+||M_f P_j E_N||_HS
      <=2b_j||f||_infty.                                        (J2)

This is only an absolute estimate, not a statement of relative leading order.

## 4. PROVED physical source-norm and calibration consequences

The frozen id/check average and ||rhat||_infty<=||r||_1 give

    C_j(r)<=4b_j^2||r||_1^2=o(j)||r||_1^2,                       (S1)
    |C_j(r,s)|<=4b_j^2||r||_1||s||_1.                            (S2)

The o(j) coefficient is common to all L1 sources, including complex sources
and changing sources with a common L1 bound. It is not a uniform full-line
du or Dlog bound. For a FIRST FIXED source window [-L,L],

    C_j(r)<=8L b_j^2||r||_du^2.                                 (S3)

This states the actual sufficient fee, with receiver j and source L distinct.
Reading it in bare-du introduces the usual physical half-density weight;
there is no assertion of an unweighted isometry between the two source slots.
The full-Q Dlog domain, Gamma, contact, all prime powers and both poles are
not altered by this auxiliary source bound.

If some finite common positive calibration c_j matched the three frozen
targets, then in particular c_j C_j(g)->q0>0. From (S1) it follows necessarily

    c_j*j -> infinity.                                          (S4)

Indeed c_j*j=(c_j C_j(g))/(C_j(g)/j) on eventual positive-denominator layers.
This does NOT say c_j itself tends to infinity: C_j(g) might grow sublinearly.
It does NOT bound any allowed unbounded calibration, and hence does not settle
the contract. If infinitely many denominators vanish, calibration fails there;
this proof establishes neither that branch nor eventual strict positivity.

## 5. PROVED conditional three-ratio obstruction

This is a reduction for the actual fixed test, not an additional source family
or a claimed estimate for P_j. Set a=1/2 and form the even/odd parts of the
already-frozen translated test:

    u_a=(tau_a g+tau_(-a)g)/2,
    v_a=(tau_a g-tau_(-a)g)/2.

Their multiplier symbols are cos(at)G(t) and -i sin(at)G(t); g' has symbol
itG(t). No new tests or reflection convention are being selected.

Let F_j(r)=2^(-1/2)([P_j,A_r]E_N,[P_j,A_check(r)]E_N) in the direct sum of two
HS spaces, so ||F_j(r)||^2=C_j(r). Reflection invariance of this direct-sum
form makes every even source orthogonal to every odd source. Therefore

    C_j(tau_a g)=C_j(u_a)+C_j(v_a)                              (R1)

exactly, including complex scalar coefficients. Define

    A_j=sqrt(C_j(g)), B_j=sqrt(C_j(g')),
    e_j=||F_j(u_a-g)||, o_j=||F_j(v_a+a g')||.

Suppose, in addition to eventual A_j>0, the ACTUAL relative estimate

    e_j+o_j=o(A_j+B_j)                                         (RC)

holds. Then, writing k=q1/q0>0, the frozen error satisfies

    liminf delta_j >= a^2*k/(1+a^2)=k/5>0.                     (R2)

Proof: triangle inequalities give
|sqrt(C_j(u_a))-A_j|<=e_j and
|sqrt(C_j(v_a))-a B_j|<=o_j. On any subsequence with bounded delta_j, the ratio
r_j=B_j^2/A_j^2 is bounded because |r_j-k|<=delta_j. Hence (RC) implies
e_j/A_j,o_j/A_j->0 there. After a further subsequence r_j->r>=0, (R1) gives
C_j(tau_a g)/C_j(g)->1+a^2 r. The limiting error is therefore

    max(a^2 r,|r-k|)>=a^2 k/(1+a^2).

If a subsequence with a smaller finite limiting error existed it would
contradict this inequality; unbounded-error subsequences cannot lower liminf.
This proves (R2). With only delta_j->0 assumed, the same argument would give
the simpler contradiction C_j(tau_a g)/C_j(g)->1+a^2 k>1.

Crucially, (RC) is NOT proved by (J) or any old fixed-eta localization result.
It is written explicitly as a sufficient missing comparison, not as an input
whose truth is being presumed.

## 6. The exact unpaid relative step

The new absolute estimate controls e_j and o_j by O(b_j), but A_j+B_j has no
paid lower bound on that scale. It may be much smaller. Dividing absolute
o(j) errors by C_j(g), or multiplying them by an arbitrary c_j, is invalid.

Pointwise sin(at)=at+O(t^3), cos(at)=1+O(t^2) near zero does not prove (RC):
the commutator includes P_j acting BEFORE and AFTER multiplication, and the
right Hermite projection retains coherent cross terms. An operator-norm
small multiplier remainder does not give a bound relative to these two
particular commutator energies. The contractions in section3 deliberately
discard this coherence, so cannot recover the missing relative information.

The old proof of kernel localization first fixes eta and B; its interpolation
constants and thresholds depend on eta. Replacing eta by eta_j to force a
flat Hermite kernel on scale 1/j is unlicensed without a new quantified proof.
Even a valid moving absolute kernel bound alone would not automatically pay
a denominator lower bound or a relative commutator remainder.

An actual proof of (RC), or a different exact actual ratio comparison, could
settle this responsibility. None is supplied here. No general N(X), source
choice, gain rule, shifted/squeezed Hermite basis or alternate family is
introduced to circumvent this gap.

## 7. Strongest-old subtraction and result classification

The short paid chain for (J) is: actual full-Gram fixed-eta kernel localization
from C052/589 -> elementary Hermite energy/fourth-moment bounds -> simultaneous
X=exp(j), N=j^2 input split. This makes an actual joint cutoff upper explicit;
it does not reproduce a fixed-X full-HS endpoint. Because its ingredients are
paid localization plus standard finite-oscillator estimates, it is not claimed
as a new independent arithmetic input or a stronger classical whole result.

591's common occupation and positive-weight conclusions cannot be applied by
renaming E_N as R. 603 has a different output projection. 594's prime-linear
selfadjoint trace-word hypotheses remain absent. The old full Gram endpoint,
PSD, C+T=2bar(V), and the signed residual identity do not pay (RC).

Thus the actual three-ratio conclusion remains OPEN. Only the absolute joint
upper, its necessary c_j*j condition, and the conditional gap lemma are proved
here. No pass/failure of delta_j, cofinal PSD/D-prime limit, physical principal
map or new method-class boundary is asserted. Root must classify the complete
ONE C070 responsibility after reconciling the parallel proof and fresh audit;
this file does not consume a round or open a successor.

Whole17/16, fixed9/8 finite448, same605-head ALL-complement positive completion,
and whole leading4/5 negative-inertia UPPER are unchanged. Principal/sections/
mixed, dangerous core/coupling, growth/Xi and all three long-Goal gates remain
open. The original Gamma/contact/all proper powers/both poles and ALL-complex
source obligations remain in the target q0,q1; no odd pole was dropped.
