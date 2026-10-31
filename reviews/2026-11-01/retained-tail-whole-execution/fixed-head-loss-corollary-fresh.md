# Same605: fixed-alpha positive-M envelope corollary

2026-11-01; `/root/retained_tail_representation/legendre_kernel_check`. Recovered STATE/check/show, same Goal1793085111/baseline0c4f, C068 reviewing/605 pending root settlement, D20261101D/frontier. Proof/document/hash reads only; no source, Fraction/scalar, matrix, Gram, inverse, consumer or sign run. Only this review is written.

**PASS as an immediate corollary within SAME605**, subject to final root consumption of its existing witness/source/ledger. Read positive-m-augmented-comparison.md12455/SHA256 `3cee59dd69586e9d7b20dcec007a3713d29352c7006695cbeb366ebd3d196a2f`, old-fee-recovery-fresh.md4974/SHA `a77888cd710f41a7abba87687e2724de009dbc6500bce5eddac16b3771895fc1`, and root-scalar-consumption.json10956/SHA `78534866762476619eaf553d8247b2d67d8b4fd2d9bbfd9337fae9b4001a04ae`. No alternate residual-envelope execution is needed.

## Types and operator order

E:C448->H is the native isometry in original complex H=L2((-9/8,9/8),du). All matrices below act on native C448. Let Ntrue=M+V(I+G)^-1V*, J=E*KE and R_K=K-EJE*, so E*R_KE=0 exactly. Hence

    Cret=J+E*Ntrue E.

Take ANY valid old-route uniformly positive bounded Nbar<=Ntrue. In particular the old deflation Nbar=aM+Vhat Ahat Vhat* has this property once its full-H source fee is paid. Put

    R=E*Nbar^-1E>0, A_E=E*Nbar E>0.

For any valid Hermitian Qbar>=R, finite positive inverse order gives Qbar^-1<=R^-1. Also the block Gram of [Nbar^(1/2)E,Nbar^(-1/2)E] is

    [[A_E,I],[I,R]]>=0.

Its Schur complement gives R>=A_E^-1, thus R^-1<=A_E. This uses bounded positive Nbar, not an inverse of the unbounded retained tail. It holds without commuting operators or replacing a full-H inverse by a head inverse.

The old penalty D_N=((I-P)Nbar E)*((I-P)Nbar E)>=0 is a Gram operator, not a scalar norm or arbitrary entry box. For alpha0=2^-122 and ANY beta0>=0,

    Pi=J+Qbar^-1-alpha0 I-beta0 D_N
       <=J+E*Nbar E-alpha0 I
       <=J+E*Ntrue E-alpha0 I=Cret-alpha0 I.

Thus every valid trial/residual/joint-Gram upper envelope Qbar is covered, including the exact best inverse compression. Additional rigorously subtracted source/finite-error losses cannot help. Improving the earlier coarse gamma193 to recovered216 also cannot evade this order comparison.

## Same source, strictness and scope

For the actual saved raw coefficients a, use u=D^(1/2)a, Djj=9/[4(2j+1)]. Then f=Eu=sum a_jp_j and ||u||^2=n=a*Da=int exp(-uvar)|r(uvar)|^2duvar. The stored root scalar record explicitly bounds the ACTUAL Cret Rayleigh strictly below alpha0, after adding source fee2^-224 to the independently replayed Chat value. This stronger transported bound is essential: Hpre<0 or Chat<alpha0 alone would not pay that fee. This review reads that existing exact record; it does not recompute it.

Consequently u*Pi u<=u*(Cret-alpha0 I)u<0 for EVERY valid Qbar/trial/Gram. Raw congruence is D^(1/2)PiD^(1/2)<=Cret_raw-alpha0D. If Qraw=D^(1/2)QbarD^(1/2), its raw inverse contribution is D Qraw^-1 D, not Qraw^-1. No physical norm or inverse normalization is changed.

This excludes the OLD fixed-alpha122 positive-M residual-envelope recipe as well as the selected covariance recipe, using the SAME witness and responsibility. It is not a second mathematical round, consumer run, whole-Lret/Q negative result, or boundary for all positive-M/Young methods. Smaller uniform loss, anisotropic losses or other decompositions remain logically possible; no parameter/consumer/source queue is authorized. Old actual Cret>2^-202 and full-Q finite-source positivity remain intact. Root should not list this same alpha122 residual envelope as an unexcluded fallback. All long-Goal gates and whole/principal/mixed/growing coverage remain separate.
