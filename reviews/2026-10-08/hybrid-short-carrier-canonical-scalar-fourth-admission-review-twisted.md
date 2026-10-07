# 原 short-carrier canonical scalar 四矩准入：独立全文审查

2026-10-08。结论：限定 PASS。独立实读最终源全部 370 行，逐项
重算 Fourier 符号、两层 height guards、精确采样密度和 cutoff
Dirichlet convolution。没有发现阻断。本审查确认原 shared-profile
ratio 到单个未移位标量四矩的一侧准入；尚未得到该标量四矩上界。

## 1. 最终来源与范围

canonical LF 只将 CRLF/lone CR 换成 LF，不 trim、删 EOF 或尾空白。

| 文件 | canonical LF SHA-256 | canonical bytes /行 |
|---|---|---:|
| [被审完整源](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 | 14699 /370 |
| [472](../../notes/472-original-short-carrier-fourth-compression-and-ratio-variance.md) | 9856885e932a892cf7c33ece82f430c2ec13004555eb52da2f1e8b1ec6bb2683 | 9037 /194 |
| [half-ratio 与 carrier criterion](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md) | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 | 11396 /276 |
| [原 half-Gram](../2026-10-07/hybrid-high-parity-gram-and-mobius-completion-research-radial.md) | 3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2 | 11380 /283 |
| [239](../../notes/239-vaughan-quotient-first-centering-and-divisor-kernel.md) | b35398ecdfbe65ce2ea04856a5e66f6676d61cc109b3de48e855b514db0cfa20 | 15736 /559 |
| [240](../../notes/240-mobius-pullback-adjacent-divisor-dispersion.md) | 1867e490fed07598e4f6c44952352d2c3a7a0dc4b066b6c1720e8a96d3a0ed8a | 14444 /460 |

冻结 criterion 源由本审查人参与推导，本次审查对象则是另一作者的
新增乘子准入，完整 proof 未用 criterion 的反方向上界替代。
原 $C^2$ even taper、finite normalizer、zero extension、half-Gram
cross 和 472 的共同 carrier 选点是明确输入；未新增 [R] 无零前件。
239/240 仅为既有对象范围，本文没有借其未付算术结论。

## 2. Fourier 符号、half-Gram 和原中心

采用 $R_sf(u)=f(u+s)$，直接相乘有

\[
 A_p^*A_qf(u)=b_pb_q\phi(u)\phi(u-\log p)^2
       \phi(u+\log(q/p))f(u+\log(q/p)).
\]

因此 $P_u$ 的频率是 $+\log p$，$\overline{P_u}P_H$ 的频率是
$+\log(q/p)$；终端乘子必须为 $\phi(u+\xi)$。被审 (3)–(5)
与此完全相符，没有右伴随平移或号数遗漏。
$p=q$ 项乘上外面的 $\phi(u)$ 后，准确是
$\phi(u)^2\sum b_p^2\phi(u-\log p)^2$，恢复原 $D_+$。
genuine high primes 的两次同向平移为空使输出位于 $I_+$；
本稿没有把一个全实线 trace 自由循环成有限 carrier trace。

两乘子只过滤同一个原 $P_H$；未重选 prime coefficients、
carrier phase 或逐 $u$ 的好高度。全局 finite polynomial 不属于
$L^4(\mathbb R)$，最终正文正确避免直接套用全轴 norm。

## 3. uniform BV 常数的独立核验

对 real Schwartz $f$，$g=f+iHf$ 的频率支撑在非负轴。
其 Fourier transform 是可积且有界的截半 Schwartz 函数；
四次卷积在零点的正频率积分仅有零测度端点。
$Hf=O(1/|t|)$ 保证 $g^4$ 可积，从而 $\int g^4=0$。
实部给
$\|Hf\|_4^4=6\int f^2(Hf)^2-\|f\|_4^4$；
Cauchy 的二次方程准确给 $\|H\|_{4\to4}\le1+\sqrt2$。

将 real inequality 对 $\operatorname{Re}(e^{i\theta}f)$ 积分，
利用 $\int_0^{2\pi}|\operatorname{Re}(e^{i\theta}z)|^4d\theta
=3\pi|z|^4/4$，complex 情形保持同一常数。
故半轴 projection 的安全常数为 $C_4=1+1/\sqrt2$。

compact $W^{1,1}$ 函数有
$m(\xi)=\int m'(v)1_{\xi\ge v}\,dv$；调制后的 projection 是
强 $L^4$ 连续族，可取强积分，得到
$\|T_m\|_{4\to4}\le C_4\|m'\|_1$。
这里不是错误的 operator-norm Bochner integral。
$m_{1,u}'$ 的 $L^1$ 恰为 $V_\ell$，终端 $m_{0,u}$ 的
$L^2$ norm 至多一，均与 $u,\ell$ 一致。

原 $\phi''$/$\phi'$ 的一致界也给
$\|(\phi^2)''\|_1=O(1)$。zero extension 的 $C^2$ 前件允许二次
分部积分，两个 convolution kernels 的远端均为 $O(|v|^{-2})$。
粗 kernel $L^1$ 可有 $\log\ell$，但 BV $L^4$ 常数没有从这项
粗界取得，正文未漏乘该增长。

## 4. 两层正高度 guard 和增长一致性

$J_0=[T,2T+s]$、$J_1=[T/2,3T]$、
$J_2=[T/4,4T]$ 的相邻 exterior separation 为 $cT$。
首乘子在 $J_1$ 的外部 tail 逐点为
$O(\mathfrak m_T/T)$，取 $L^4(J_1)$ 得
$O(\mathfrak m_TT^{-3/4})$。终端乘子在 $J_0$ 的外部 tail
逐点为 $O(\mathfrak m_T^2/T)$。
内部是真正 $L^4/L^2$ 函数，可用 BV、contraction 和 Hölder。

独核归一化后完整式：

\[
 T^{-1/2}\|z_u\|_{L^2(J_0)}
 \le N_\ell\mathcal M_T^{1/2}
 +C_\phi\frac{\mathfrak m_T}{T}\mathcal M_T^{1/4}
 +C_\phi\frac{\mathfrak m_T^2}{T}.
\]

两尾量分别为 $O(X^{-1/2}/\ell)$ 和 $O(\ell^{-2})$，
首尾仍乘 $\mathcal M_T^{1/4}$。未知 $\mathcal M_T$ 可增长，
所以平方后的 cross 没有被免费删为 additive $o(1)$。
height 0 的正相干峰在两个 guards 外；其全部贡献仍经 kernels
远尾付款，不是直接删去该峰。

## 5. 原 sigma+k 采样及 coefficient

精确 density 是
$\omega_T=(sd)^{-1}\sum_{k=0}^{d-1}1_{[T+k\eta,T+s+k\eta]}$。
每个区间长度为 $s$，故积分为一；任意高度的 lattice overlap
至多 $s/\eta+1$，给 (12)。$d\eta\le T$ 保证支撑在 $J_0$。
这些是 finite interval counts，保留端点 strips 与 floor。

(5) 的每列模平方乘 $\ell^{-1}\phi(u)^2$，非负 Fubini 给 (13)。
even taper 的 half integral 为 $a_\ell/2$，故乘上 $T$ 后
有限 prefactor 恰为
$A_T=a_\ell T(1+\eta/s)/(2d\eta)$。
没有漏一倍，也没有把 $a_\ell$ 免费替换成极限 $a$。

由原 uniform $D_+R_+$ cross，完整有限式为
$\operatorname{avg}r_\sigma+S_T/2
\le A_TE_T(\mathcal M_T)^2+C_\phi/\ell$。
只有后来先付 $\mathcal M_T=O(1)$，才可删误差、使用 (16)
或把 472 的 avg upper 转成共同合法 carrier 的 actual $q$ upper。
本文没有把 $q_{\rm sq}$ 当作完整实线 residual。

## 6. proper powers 和 sharp Möbius completion

平方 signal 的 base 是 $p$，平方列的 base product 是 $pq\le X$，
频率为 $2\log(pq)$。prime factorization 重数至多二，因此
其 weighted energy 至多 $2(\sum p a_p^2)^2$，
unweighted energy 至多 $2(\sum a_p^2)^2$。
对 $2t$ 使用 weighted MV 只改变固定常数，不按 $p^2q^2$
的长度 $X^2$ 误付。由 Chebyshev/Abel，
$\sum a_p^2\ll X^{-1/4}/\ell$、$\sum p a_p^2=O(1)$；
(17) 以及 normalized $L^4$ 小量正确。

对 $k\ge3$，$\sum_{p>y}\log p\,p^{-k/2}
\ll y^{1-k/2}$ 的常数由 $(k/2)/(k/2-1)\le3$ 一致控制。
$y=X^{1/(2k)}$ 给每项至多 $X^{-1/12}$，$O(\ell)$ 个
$k$ 被原 normalizer $\ell$ 抵消。因此 (18)/(19) 是真实 norm
差，而非在未知增长四矩上擅称 additive 小量。

独核 $\Lambda*\Lambda=\mu*\log^2-\Lambda\log$ 的导数符号。
令 $L=\Lambda1_{n\le\sqrt X}$、$U=\Lambda1_{n>X}$；
展开 $(\Lambda-L-U)^2$，在 $X<n\le X^2$ 上 $L*L=U*U=0$，
$-2U*\Lambda+2U*L=-2U*(\Lambda-L)$。故 (21) 的末项
必须同时保留 $a>X,b>\sqrt X$，而非仅保留 low correction。

另在内存独立用 formal prime-log symbols、$X=16,Y=4$，
对 $17\le n\le256$ 全部 240 个系数重新核等：直接原 high
卷积与显示 Möbius/两项 correction 完全一致。
这未写任何旧脚本或输出，也只核 finite algebra，不核算术 mean。

## 7. 可审结论

新付款是完整原 shared spatial windows 到一个未移位、原系数
scalar high 四矩的增长一致一侧接口，包含正高度 guards、精确
carrier 采样、proper-power norm 迁移和两个 factor cutoff。
它没有证明 ratio 与 scalar 四矩双向相等。

剩余 (22) 的长度仍为 $X^2$、高度仍为 $O(X)$；
简单 weighted MV 的 $O(1+X/\ell^2)$ 不能当成已付 $O(1)$。
Möbius 和两项 cutoff corrections 须联合 signed 估计；
ordinary Mertens prefix 或独立角色行合同没有免费完成此项。

限定 PASS 不包含 canonical scalar 四矩的新算术上界、实际 small-$q$、
比例、无零边界、field 改变、原全部 [R]、Lean 或 RH 认证。
