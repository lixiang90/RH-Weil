# True pi and the exact Machin denominator

2026-10-31; proof-only clarification by `/root/retained_tail_source_design`, same Goal1793085111/BE/C066spent. This appends the precise denominator condition to acceptance-obligation-audit.md section4 item4; the 16119-byte audit remains unchanged. No scalar/coefficient/seed calculation, source generation, code or numerical replay was performed.

A lower bound for true pi need not be a lower bound for the distinct exact rational p_pi. Future verification must not put an arbitrary independently computed true-pi lower endpoint into a denominator that is actually p_pi. Use the common rational lower bound3, with BOTH inequalities independently justified.

Let a_d be the160-term alternating rational sum for arctan(1/d), and p_pi=16a_5-4a_239, exactly the frozen source's Machin160 rational. Alternating-series bounds give

    a_5 >1/5-1/(3*5^3),  a_239 <1/239,
    arctan(1/5)>1/5-1/(3*5^3),  arctan(1/239)<1/239.

Consequently both p_pi and true pi exceed

    16(1/5-1/375)-4/239 >3.

The accepted Machin remainder is

    |pi-p_pi| <=16/(321*5^321)+4/(321*239^321) <2^-646.

These are the existing exact-series bounds and elementary algebra, not a new evaluation of the stored rational or of any source coefficient.

On the original H=L2((-9/8,9/8),du), let B be the true Fourier band compression for Omega256; Plancherel gives ||B||<=1. Let C_pi be the degree2046 sinc-kernel polynomial with denominator TRUE pi, and let Btilde be the SAME frozen polynomial with denominator p_pi. The existing full-H Taylor bound, using true pi>3, gives

    ||B-C_pi|| <=576^2049/(pi*2049!)
               <576^2049/(3*2049!) <2^-513.

In particular ||C_pi||<1+2^-513<2. Exactly, Btilde=(pi/p_pi)C_pi, so the separate normalization error is

    ||Btilde-C_pi||
      =|pi-p_pi|*||C_pi||/p_pi
      <(2/p_pi)|pi-p_pi| <2^-646,

where the last step uses p_pi>3, not a true-pi lower endpoint. Therefore

    ||B-Btilde|| <2^-513+2^-646.

This is the original global sinc error, on the same operator/domain/norm and with the same polynomial and exact denominator. It requires no producer scalar-box truth, coefficient-box nesting or new scalar normalization. The full h-to-final-center rounding fee <2^-520 is still additional; the original true-h error <2^-512 and rank-two fee depend on that complete check.

The audit's instruction to use independently true scalar bounds is thus consumed with this TWO-term decomposition: true-pi Taylor first, exact-p_pi normalization second. The older `exactSincBound` numeric record or a producer pi-box lower endpoint remains unconsumed unless separately justified. New authoritative norm brackets may use independently true pi because those formulas contain true pi itself. Old producer completion/checker STOP and all unconsumed-source restrictions remain unchanged; this clarification establishes no numerical acceptance, new signed consequence or mathematical iteration.
