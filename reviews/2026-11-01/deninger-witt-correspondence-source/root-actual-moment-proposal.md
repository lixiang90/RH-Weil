# ROOT actual proposal: exponential moments, finite-cycle test

This is one explicit admission test associated with the §5 source gate, not a theorem of Deninger's paper or an admitted mathematics contract. It uses the favorable base extension X=Spec C; that does not supply descent/integrality over Spec Z.

For physical complex r in C_c^infty(R), r=e^(u/2)f, define

    b_k(r)=integral r(u) exp(ku) du, k>=1,
    F_r(T)=exp(-sum_{k>=1} b_k(r)T^k/k).

Then F_r lies in the big Witt ring W(C)=1+TC[[T]]. In the source convention [a]=1-aT, gh_k(F)=-[T^k](T dlog F/dT), hence gh_k(F_r)=b_k(r). Witt addition is multiplication of series; F_(r+s)=F_r F_s. Fubini gives b_k(r*s)=b_k(r)b_k(s), so ghost injectivity in characteristic zero identifies F_(r*s) with the Witt product of F_r and F_s. This is a nonunital convolution-algebra map in ghost coordinates, not a C-linear map into an integral finite-cycle group under ordinary scalar multiplication.

For support in [-L,L],

    |b_k(r)| <= exp(kL) sqrt(2L)||r||_(L2du).

Each fixed coordinate is continuous in the physical norm on a fixed window; constants are not uniform in k or growing L. The logarithmic series converges at least for |T|<exp(-L). No norm or full-Weil functional on this completed target is supplied. Physical f-du and r-du norms differ by the prescribed e^(u/2) weight; this estimate is for r-du. No change to the original zero-extension Dlog domain is made.

Take the actual old591 g=psi*psi#, psi>=0 normalized, supported in (-1/16,1/16). Then g>=0 and is positive on an open interval. For any m and nonzero complex vector c,

    sum_(i,j=0)^m conjugate(c_i)c_j b_(i+j+1)(g)
      = integral exp(u)g(u)|sum_(j=0)^m c_j exp(ju)|^2 du > 0.

Thus the moment Hankel matrices are positive definite at every size. If F_g were rational, -T F_g'/F_g would be rational; its Taylor coefficients b_k would satisfy a fixed finite linear recurrence from some index onward. Choosing a sufficiently shifted Hankel block would then give dependent columns. The same integral proof with any positive exponential shift proves strict positivity of that block, a contradiction. Equivalently, a rational Witt element over C has finitely many roots/poles and ghosts that are a finite integer-weighted sum of powers. Therefore F_g is NOT in Wrat(C), even though it is a legitimate big Witt element. This excludes this direct finite-cycle realization already on one compact smooth source; it does not exclude growing finite approximations.

The native principal role is independent of this range failure. On A1_Z, Gamma2-Gamma3=div((T-2)/(T-3)) is a proper relative Cartier divisor. In the reduced correspondence ring of5.1 it maps to (1-2T)/(1-3T), which is nonzero as a Witt-group element (ordinary series not1). Quotienting Z Gamma0 is not quotienting all principal divisors. The ring identity therefore supplies no automatic physical405 descent.

If the same ghost prescription is extended to the old574 full relation P using its paid Mellin labels, b_k(P)=1/2(k^2-1/4)xi(k+1/2); b_1(P)=3xi(3/2)/8 is nonzero. This separately rejects exact descent of THIS completed ghost prescription to the physical principal quotient. It is not a new proof about P and does not require a noncompact relation to vanish at each layer of a compact-test Dprime approximation.

Finite jets survive: truncate F_r at degree m to obtain a polynomial with constant1, hence an element of Wrat(C), matching ghosts through m. The degree grows; formal T-adic convergence supplies no original du-Dlog/full-Weil estimate, no mixed arithmetic pairing and no favorable signed core/coupling. Relative/higher objects, source-dependent growing degrees and other completed constructions remain open rather than excluded.

Strongest-old consumption: old finite-End/W0 already describes finite characteristic polynomials; old574 supplies the exact physical relation labels, old591 supplies this actual g, and the rational-logderivative/positive-moment rank check is standard. The newly reviewed source adds its genuine native geometric identification, not a new classical source identity or whole-object consequence. Admission0/SOURCE0; no607/C071, no cadence increment, no general Witt/Weil no-go. The actual classical principal/sections/mixed/growing signed core and coupling bottleneck is unchanged.
