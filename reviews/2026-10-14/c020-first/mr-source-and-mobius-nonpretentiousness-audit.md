# C020: MR source quantifiers and the Möbius nonpretentiousness input

2026-10-14, independent source audit by /root/c017_prime_pole. Only this
file is owned by this agent. Source recovery and application-quantifier
verification consume zero research rounds; no STATE/cadence/Git mutation
or certification of the root's physical norm is made here.

## Recovery and fixed original

Recovered AGENTS, README, STATE, ran research_state.py check and show, and
read the active Goal, macro frontier, C020 and D20261014U. The structural
check passed, not a mathematical certificate. At entry Git was clean at
HEAD bc2a891e885f5cb4412c44c5f10df049cfc9127f. STATE named C020 ready,
latest mathematical 546 and cadence 0; source-entry notes 547/548 remain
zero-round evidence. Child get_goal was null, not the root runtime. The
fixed Goal baseline and paused-route constraints remain unchanged.

Read the frozen original arXiv:2007.15644v3, dated 9 June 2022, particularly
printed pages 3-5, the parameter setup at the start of section 3, the common
Archimedean frequency/bounded-period conclusion and final reduction on
printed pages 40-41. Checked its displayed formulas against the
[same-version original HTML](https://arxiv.org/html/2007.15644v3).
Local PDF-derived text is a search aid; in particular its missing overbar
in the distance formula must not change the definition.

    PDF: reviews/2026-10-14/c019-first/sources/
         higher-uniformity-bounded-multiplicative-2007.15644v3.pdf
    bytes: 1141003, pages: 107
    SHA256: fef1a239e616f40c57aa45e7df3397aebe880cde8ce5763acb815a24a171f6aa
    text SHA256: 834bc0d6a262663272e56b9f2bf4ab8f648ee93ce4938e7d1c16fa5b2ac79f5f

Both hashes agree with the frozen metadata. This audit also checked the
primary MRT 2015 argument cited as reference [25], equation (1.12), in
the [author-repository final PDF](https://www.utupub.fi/bitstream/handle/10024/157625/average-chowla%20-%20final%20version.pdf?isAllowed=y&sequence=1)
and the [arXiv original](https://arxiv.org/pdf/1503.05121). These supplementary
web originals are not claimed to have been frozen or hashed locally by
this child. Their published argument identifies the necessary VK
Dirichlet-L dependency and its reference to Montgomery's Ten Lectures,
section 9.5. That classical theorem is consumed as an unconditional
dependency; its full proof is not reconstructed or optimized here.

## 1. The exact distance convention matters

The fixed 2022 original defines

    D(f,g;Z)^2=sum_(p<=Z) [1-Re(f(p) conjugate(g(p)))]/p,
    M_2022(f;Z,Q)=inf_(|t|<=Z) inf_(chi mod q,q<=Q)
                     D(f,chi(n)n^(it);Z).              (1)

Both the prime cutoff and the time cutoff are Z, the first argument of M.
The infimum is over a finite set of Dirichlet characters when Q is fixed,
and a continuum of times in the specified finite interval. Imprimitive
characters are included; their primitive conductor is at most q.

M_2022 is a distance, not a squared distance. The older MRT 2015 notation
uses the squared distance in its M. A quantitative lower bound from that
paper must therefore be square-rooted before applying (1). Qualitative
divergence is unaffected. Increasing Q enlarges the comparison family and
can only decrease M; increasing Z changes both prime and time cutoffs, so
no simple monotonicity in Z is used in this audit.

For every prime, mu(p)=lambda(p)=-1. Hence the two prime distances, and
their M_2022 values, agree exactly for Möbius and Liouville. Although mu is
not completely multiplicative and vanishes at squareful integers, it is
multiplicative and 1-bounded, which is the original theorem's hypothesis.
No completion of mu at prime powers is made.

## 2. What Theorem 1.3 and Corollary 1.4 actually assert

Theorem 1.3 is an inverse theorem for the paper's weak polynomial-correlation
norm u^(k+1), not a pointwise centre theorem or an arbitrary-sequence theorem.
Fix k>=0 and 0<theta<1/2. For 1-bounded multiplicative f and

    X^theta<=H<=X^(1-theta),

an averaged weak-correlation lower threshold eta>0 forces

    M_2022(f;C X^(k+1)/H^(k+1),Q)<=K,

with constants depending only on k,eta,theta. Corollary 1.4 replaces that
premise with

    integral_X^(2X) sup_(|t|<=eps0 X^(k+1)/H^(k+1))
        |sum_(x<=n<=x+H) f(n)n^(it)| dx >= eta H X,      (2)

and allows constants C,Q,K depending additionally on fixed eps0>0.
These constants are uniform in X,H and f within the stated assumptions;
they are fixed after the threshold and structural parameters are fixed.
Neither result supplies a numerical decay rate by this statement alone.
The fullcentre average and its frequency supremum inside the integral
must both be retained.

The proof dependencies agree with these quantifiers. The introduction
explains the polynomial Taylor reduction of n^(it), including its finite
time range. Section 3 starts with k,theta,eta fixed and allows implicit
constants to depend on them. Its rigidity reduction produces a common
frequency T_0=O((X/H)^(k+1)) and a bounded periodic modulus q_0; proposition
3.13 bounds the latter. The final argument on printed page 41 uses the
complex-valued short-interval multiplicative theorem of MRT 2015 to force
bounded pretentious distance. The k=0 case is inherited from the original
MR short-interval result; the k=1 case comes from the original Fourier
uniformity paper [26], with the 2022 original explicitly removing its
earlier H^rho time loss. This is a published theorem/proof chain, not an
RH assumption or a use of arbitrary all-height phase recurrence.

The theorem does not apply directly to the cutoff/Abel-weighted sequence
mu(d)d^(-1/2)exp(-d/Y0)1_(D<d<=2D), nor to b_U or full Type II convolution.
For Corollary 1.4 one should keep f=mu and put t=-tau in the character;
weights and endpoints are separate transport responsibilities. The natural
character parameter is tau itself: no missing 2pi is inserted when using
n^(it) rather than the polynomial e(phase) notation.

## 3. Möbius meets the full finite-time prerequisite unconditionally

The primary MRT 2015 equation (1.12) uses the ordinary VK zero-free and
prime-sum estimates for Dirichlet L-functions to prove, for fixed Q and
each fixed small delta>0, uniformly over the allowed characters and
|t|<=Z,

    sum_(p<=Z) [1+Re(chi(p)p^(it))]/p
       >=(1/3-delta)loglog Z+O_(Q,delta)(1).             (3)

The article obtains this from its high-prime range
exp((log Z)^(2/3+delta))<=p<=Z and records the underlying VK dependency.
Conjugating chi and reversing t leaves the infimum unchanged, so (3)
applies to (1) with f=mu. In the fixed-Q use here all characters are in a
fixed finite family; no uniform growing-conductor or exceptional-zero
optimization is claimed. Any character-dependent bounded-head constants
are absorbed into that fixed family's constant. The published argument
also explicitly applies to mu since its prime values equal those of
lambda.

Consequently

    M_2022(mu;Z,Q)^2
       >=(1/3-delta)loglog Z+O_(Q,delta)(1),
    M_2022(mu;C D,Q)->infinity as D->infinity             (4)

for every fixed C>0 and Q>=1. The statement is uniform if C ranges in any
fixed positive compact interval. The square in (4) is essential when
quoting the older numerical exponent. No RH, Chowla conjecture or unknown
zeta-zero location has been assumed. This consumes an established VK
theorem as the source's prerequisite; it does not resume the paused
zero-free-region optimization route.

This is substantially stronger than verifying divergence only at each
fixed t separately: the infimum over the whole growing interval |t|<=Z
has been paid. It is also weaker in scope than permitting all real t at
each scale, which the fixed source never states.

## 4. Uniform square-root-length averages needed by the physical transport

The Gamma/norm reviewer needs the following exact source consequence:

    epsilon(D):=sup_(sqrt(D)/6<=H<=4sqrt(D))
       [1/(DH)] integral_D^(2D) sup_(|tau|<=6sqrt(D))
          |sum_(x<d<=x+H) mu(d)d^(-i tau)| dx ->0.       (5)

This follows from Corollary 1.4 and (4). Fix k=1, theta=1/4 and any fixed
eps0>0. For sufficiently large D, the whole H range in (5) lies inside
[D^theta,D^(1-theta)], and

    D/16 <= D^2/H^2 <=36D,
    eps0 D^2/H^2 >=eps0 D/16 >6sqrt(D).

For example the last inequality follows once sqrt(D)>96/eps0. Thus the
paper's character supremum covers the entire required tau interval,
uniformly in H. The sign t=-tau is immaterial.

If (5) failed at some fixed threshold eta>0 along D_j->infinity, choose
one bad H_j for each j. Corollary 1.4 would give fixed constants
C_eta,Q_eta,K_eta independent of j and H_j, with

    M_2022(mu;C_eta D_j^2/H_j^2,Q_eta)<=K_eta.

Its first parameter lies in
[C_eta D_j/16,36 C_eta D_j], so the uniform version of (4) contradicts it.
This proves the supremum over H outside the centre integral in (5), not
merely a statement for one preselected aspect sequence.

Replacing x<=d by x<d affects a null set of centres and does not change
the integral. All d, including non-squarefree ones with mu(d)=0, are kept.
The comparison does not exchange the frequency supremum with the centre
average: the original supremum is already inside that integral. It does
not prove a bound for every centre. It also does not move sup_H inside
the integral; a finite grid, endpoint errors and variable H(x) require the
separate physical-norm proof.

For the root's frozen sqrt(D)<=T<=6sqrt(D), h=1/T, |tau|<=T,
the physical window has length H(x)=x(exp(h)-1), of order sqrt(D) for
x of order D. On x in [D,2D], its length lies inside the range of (5) for
large D: the lower bound is sqrt(D)/6, and exp(1/T)-1<=2/T gives the upper
4sqrt(D). This verifies the finite-character source range. It does not
by itself pay variable-length selection, dyadic truncation, monotone BV
weight, conversion from averaged L1 to the original du L2 norm, or Gamma
form energy. Those are actual-source transport gates owned by the root
and the other reviewers.

The same argument allows every separately fixed B>=1:

    epsilon_B(D):=sup_(sqrt(D)/B<=H<=4sqrt(D))
       [1/(DH)] integral_D^(2D) sup_(|tau|<=B sqrt(D))
          |sum_(x<d<=x+H) mu(d)d^(-i tau)| dx ->0.       (6)

Indeed D^2/H^2 is in [D/16,B^2 D]; the lower polynomial-window condition
holds eventually for that fixed B, and eps0 D/16 eventually exceeds
B sqrt(D). After choosing a fixed bad threshold, the same inverse theorem
would force bounded M at a scale in
[C_eta D/16,C_eta B^2 D], contradicting (4). Constants and thresholds may
depend on B. Thus every fixed aspect sqrt(D)<=T<=B sqrt(D), with h=1/T
and |tau|<=B sqrt(D), has a legitimate source input. It also covers any
separately fixed cofactor kappa after choosing its finite B_kappa.
This is the quantifier "for every fixed B, then D tends to infinity";
it supplies no uniform claim for B=B(D), growing cofactor labels or all
real frequencies. The finite-grid/weight/physical-norm transport remains
separate, exactly as for (5).

## 5. Full-label coverage and final source ruling

The fixed finite cofactor mask kappa<=8 has a bounded aspect range and
finitely many shared physical cross terms. Raw mu at each such scale can
use (5); the exact common-product/Abel/phase factors must still be carried
through the old 164 synthesis. It is legitimate to consume this source
before that proof; it is not legitimate to declare the physical norm or
the mask proved from the source's name.

At the maximal full Type II cofactor kappa of order Y/U, with
U of order sqrt(Y)/log^2(Y) and T of order sqrt(Y), the raw length is

    D_kappa of order U,
    H_kappa of order D_kappa/T of order 1/log^2(Y).

It fails every polynomial lower bound D_kappa^theta required by the
frozen source. Increasing the finite character range does not repair
this length failure. Even where an individual label is covered,
qualitative o(1) does not pay a growing family of labels, their shared
collision multiplicity or Gamma/continuum coupling. Applying MR directly
to the nonmultiplicative b_U or full convolution remains invalid.

Paid source scope: the fixed theorem's average-centre, inside-sup,
finite-time quantifiers and the growing-time Möbius nonpretentiousness
prerequisite, including uniform H in (5). The convention correction from
squared M_2015 to distance M_2022 is explicit. No source-definition or
constant obstruction remains for that stated finite-aspect use.

Unpaid: the root's original-norm transport and exact finite-mask result,
all-label coverage, original complex Gamma/pole signed coupling, whole
core/count/nearPSD and Xi identification. This child source audit counts
zero rounds. If the root independently pays a new physical signed norm,
it may settle that actual result once under C020's rules; a finite head
alone still does not complete the macro Goal.
