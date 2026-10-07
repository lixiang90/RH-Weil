# 原 short-carrier canonical scalar 四矩准入：独立全文审查

2026-10-08。compression_bridge。只新增本审查，不改源、旧文件、math、Git。

结论：**限定 PASS**。完整实读待审源全部370行，对原对象、局部 Lp 乘子、
两级正高度 guard、准确 carrier 密度、growth-uniform 费用、proper powers
及两个 sharp factor cutoff 的卷积修正，未发现阻断。
这是 actual shared-profile ratio 到 canonical scalar fourth 的一侧准入；
正高度 scalar mean-square 上界仍是 [O]，没有实际 O(1) fourth、新比例或边界。

## 1. 精确绑定与实读范围

待审源：[完整 scalar admission 研究](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md)。
实测 UTF-8 canonical LF SHA256 为
`f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7`，
14699 bytes / 370 lines；只统一 CRLF/lone CR 到 LF，不 trim。
此结论只绑定该版本，不借有限脚本运行替代分析证明。

以下五个 source-bound 输入均实测 hash 与待审源一致；472、twisted
whole-ratio 源和原 high half-Gram 源同时全文实读，239/240只用于范围比较，
本审查不重新认证其无限分析合同。

| 输入 | canonical LF SHA256 |
|---|---|
| [472 原短 carrier 四阶桥](../../notes/472-original-short-carrier-fourth-compression-and-ratio-variance.md) | 9856885e932a892cf7c33ece82f430c2ec13004555eb52da2f1e8b1ec6bb2683 |
| [完整 half-ratio 和 uniform cross](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md) | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 |
| [原 half-Gram 与 Möbius identity](../2026-10-07/hybrid-high-parity-gram-and-mobius-completion-research-radial.md) | 3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2 |
| [239 既有 Vaughan 范围](../../notes/239-vaughan-quotient-first-centering-and-divisor-kernel.md) | b35398ecdfbe65ce2ea04856a5e66f6676d61cc109b3de48e855b514db0cfa20 |
| [240 既有 adjacent-divisor 范围](../../notes/240-mobius-pullback-adjacent-divisor-dispersion.md) | 1867e490fed07598e4f6c44952352d2c3a7a0dc4b066b6c1720e8a96d3a0ed8a |

## 2. 原 physical 算子和 shared window：源(2)–(5)

由 R_s f(u)=f(u+s)，准确有
Gf(u)=φ(u)Σ_(p,q)b_p b_q φ(u−log p)²φ(u+log(q/p))f(u+log(q/p))。
high shifts 大于 ell/2，A=Π_-AΠ_+，G=A*A 仅在 I_+；这只用于 physical
算子，不把 E*A E 称为 nilpotent。E_sigma 的 interval zero extension
与最后一个 φ 因子相容。

m_1,u(ξ)=φ(u−ξ)² 作用在 P_H 的 prime frequencies log p，给 P_u；
overline(P_u)P_H 的 frequencies 是 log(q/p)，m_0,u(ξ)=φ(u+ξ)
再给最后一个路径窗。故源(4)、(5)逐有限频率展开精确成立。
其 p=q 部分为 φ(u)Σb_p²φ(u−log p)²，乘外部 φ(u) 正好是原 D_+。
没有剔除 shared u、换 same-prime center 或引入新的 prime family。

## 3. 真正 Lp 乘子与 guard：源(6)–(11)

实 Schwartz f 的 g=f+iHf 具有非负 Fourier support，g 的 Fourier
transform可积，四次卷积在零点为零；g⁴ 可积。因此 int g⁴=0 的
实部等式合法，Cauchy 后解 y²≤6y−1，给 ||H||_4≤1+sqrt2。
real projection 对 angle 积分将同一界传至 complex f。
半轴 projection 的 triangle upper 是 C4=(1+||H||_4)/2=1+1/sqrt2。
此处没有称该 projection bound 为 sharp norm。

compact W^(1,1) multiplier 的 m(ξ)=int m'(v)1_(ξ≥v)dv 为准确 BV
分解，频率平移对应 unit modulation，强 L4 积分给 C4||m'||_1。
故 m_1,u 的 L4 norm≤C4 V_ell，m_0,u 的 L2 norm≤1，均 uniform in u。
phi² 的二阶 L1 bound由 phi、phi'、phi'' 的原假设推出。

两 kernel 的远 tail |K(v)|≤C_phi/|v|² 源自原真实 zero extension 的
二次分部积分。其全 kernel L1 可能有 log ell 费用，源没有用这个
粗 L1 bound 冒充 uniform L4 multiplier norm。
有限 prime polynomial不在 L4(R)；源先对 P_H1_J2 或
overline(P_u)P_H1_J1 使用真正 Lp operator，再处理其有界补集。

J0⊂J1⊂J2 的两次外部距离均至少 cT，全部位于正高度。第一层 tail
点值≤C_phi m_T/T，L4(J1) 费用为 C_phi m_T T^(-3/4)。
第二层利用原正系数给 ||P_u||∞≤m_T，点值 tail≤C_phi m_T²/T。
L2 contraction 与 Hölder 后，归一化 z_u norm 精确付款为
N_ell sqrt(M_T)+C_phi(m_T/T)M_T^(1/4)+C_phi m_T²/T。
所有 u 共用 J2；没有把正高度窗口扩至 X² 或跨入 height0 coherent peak。

## 4. 原 finite carrier 的密度与增长：源(12)–(16)

准确 avg_sigma d^(-1)Σ_k f(sigma+k eta)=int omega_T(t)f(t)dt。
长度 s 的 grid intervals 在任一点最多 s/eta+1 条，所以源(12)有效；
int omega=1，最大 endpoint≤T+s+(d−1)eta≤2T+s。
这个 density 是对原 discrete carrier 作短 base-height 平均，不是把它
改为 continuous/global Fourier projection。

非负 Fubini、源(5)和 even window 给源(13)、(14)，prefactor
A_T=a_ell T/(2d eta)(1+eta/s) 保留 floor、overlap 和两个 endpoint strips。
half-Gram 已付 cross 满足 uniform O(1/ell)：其 log(q/p) 无 alias，
base sigma只进入两个 Hilbert coefficients 的单位相位。
又 ||D_+E_sigma||HS²/d=S_T/2，因而源(15)的左侧是准确
avg r_sigma+S_T/2，误差不乘未知 r 或 fourth。

若 M_T 增长，源保持 E_T(M_T)² 和 A_T 原式；没有把 relative o(1)
或 tail×M_T^(1/4) 改为 additive o(1)。只有先付款 M_T=O(1)，才能
得到源(16)的 limsup 和 bounded avg r。再用472的共同 good set 可选
同一 sigma；不同高度的后续算术估计不能直接合并。

## 5. Proper powers：源(17)–(19)

平方 prime 部分的 a_p=log p/(a_ell ell p)。Chebyshev 给
Σa_p²≪X^(-1/4)/ell、Σp a_p²=O(1)。P2² 的 base 是 pq≤X，
ordered prime-factor multiplicity至多2；frequencies为2log(pq)，
其 local gap由 base pq 控制。weighted MV于是给
T^(-1)int_J2 |P2|⁴≪(Σa_p²)²+T^(-1)(Σp a_p²)²。
没有错误按 p²q²≤X² 付款频率间距。

k≥3 时 Chebyshev partial summation 的 k/(k−2) 统一有界，
每段总质量≪X^(-(k−2)/(4k))；共 O(ell) 个 k，并除原 ell，
故其 pointwise总和≪X^(-1/12)。平方的 L4 norm为
O(X^(-1/8)ell^(-1/2)+X^(-1/4))，仍是 O(X^(-1/12))，
结合得到源(19)的 O(X^(-1/12)) norm差。
该 norm statement不要求 unknown scalar fourth bounded；只有已付
bounded upper之后，才能把两 fourth 的差写成 additive o(1)。

## 6. 未移位 Möbius completion 与两个 sharp cutoffs：源(20)–(22)

在 Re s>1，A(s)=−ζ'/ζ，A²=ζ''/ζ−(ζ'/ζ)'，逐系数是
Λ*Λ=μ*log²−Λ log。令 L=Λ1_(n≤Y)、U=Λ1_(n>X)，Y=sqrt X。
Λ_H=Λ−L−U；在 X<n≤X²，L*L=0、U*U=0，但 L*U 可能非零。
完整展开遂为 Λ*Λ−2Λ*L−2U*(Λ−L)，就是源(21)。
最后一个 upper correction 不能删，也不能与 low correction各自
取 absolute 后称为 net Möbius cancellation。X=16、n=95 的例子准确。

我独立在内存以 prime-log monomials精确比较 X=16、Y=4 的全部
17≤n≤256 共240个系数：原 high-high convolution 与源(21)的
full−low−upper全部相等。此有限复核不证明任何 infinite mean-square。

源(20) 使用同一 sharp Λ_H 系数、normalizer、未移位 phase n^it 和
product range X<n≤X²。源(22)除以(a_ell ell)^4后，恰是
widehat P_H在原J2正高度上的 bounded fourth任务；(19)才允许回到
genuine P_H，再由(15)传给原完整 ratio。这个方向是充分 upper。
没有反向 equivalence，也未将规范列映成原 character-row amplified合同。

## 7. 验收范围

本篇验收新的 actual analytic admission 和精确 cutoff algebra。
scalar fourth的观察长度仍O(X)，products仍可至X²；直接 weighted MV
的 error仍是 O(X/ell²)，没有由这次 Lp 窗口付款变成 O(1)。
原7/8 prefix、ordinary Mertens、任意系数大筛或旧 marked/plain输入，
均不能免费认证源(22)。新的 χ、scalar upper、实际比例、无零边界和
RH仍未付款。没有要求修改冻结源，限定 PASS 不覆盖这些 [O]。
