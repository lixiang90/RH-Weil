# 原六次特征族的零点行密度与最终包络比较

2026-10-08。基线 2681813154243e10cf4602f4e88514355060d379。
本次沿原 Eisenstein 域和原六次特征继续研究，保留原行、自然零掩码、
固定算术数据和 primitive inducing character。

新增结果是相对原 [R] 的完整 raw 零点行计数，以及它与最终联合包络
的全域比较。新 raw 指数更强，但直接接入现有最终估计不会改善边界。
这项区分决定后续需要证明什么，不能将中间计数的节省写成新无零区域。

## 1. 全文来源与独立核对

canonical UTF-8 LF 仅统一 CRLF/lone CR，不 trim 或改变 EOF。

| 本次完整来源 | SHA256 |
|---|---|
| [全部原行的 primitive-zero 密度](../reviews/2026-10-08/hybrid-original-sextic-primitive-zero-density-research-compression.md) | 74ea809c6aef75638dc2bc115af2b592ff4feb999cd15e35adcfa4319235d52b |
| [最终包络的全参数比较](../reviews/2026-10-08/hybrid-original-density-envelope-dominance-research-root.md) | 6e1352c0f4660239c13f02bad622384c51e2df0035a5739743cb2bc78f76961e |
| [高行区间的严格连续余量](../reviews/2026-10-08/hybrid-high-bin-strict-certificate-research-twisted.md) | f33ace9d5600e5875ea05aa2ae32c0d70cd02610b6637cabcb53633965421138 |

密度全文已有 [root 独审](../reviews/2026-10-08/hybrid-original-sextic-primitive-zero-density-review-root.md)
和 [twisted 独审](../reviews/2026-10-08/hybrid-original-sextic-primitive-zero-density-review-twisted.md)，
两份限定 PASS 均绑定最终全文 hash。全域比较另有
[twisted 独审](../reviews/2026-10-08/hybrid-original-density-envelope-dominance-review-twisted.md)，
高行证书有 [root 独审](../reviews/2026-10-08/hybrid-high-bin-strict-certificate-review-root.md)。
这些审查认证各自显示推导，保留原 sextic sieve、标准 primitive Hecke AFE
等明确前件；不认证原 [R] 的全部外部分析输入或 RH。

## 2. 新 raw 行数估计实际覆盖什么

令 C(U;a,H) 为原 sixth-power-free 行 q_u≈U 中，至少一个原 presentation
的 primitive L 有 Re ρ≥a、|Im ρ|≤H 的行数。这是行数而非零点重数总和。
原 above-floor bin a>51/100 自带实际零点，才可纳入该估计；floor 仍独立
使用 #rows≪U。辅助 classical mollifier 不改变原物理探测器的槽或长度。

原理想唯一分解为 s w k，w 的非零估值为 2,…,5，k squarefree。
冻结 w 后，M≈U/Nw，R_w=N rad(w)≤(Nw)^(1/2)，真实导子≈M R_w。
先将任意列 n 唯一写为 c d²，固定 d 后保留全部零值和 row restriction；
再用原 squarefree sextic sieve。Mellin 分离导子相位和 dual root number，
得到对 moving w 一致的 critical second，三项为

\[
 \mathcal L_w=M+(M R_w)^{1/2}+M R_w^{1/3}.
\]

实际零点的 Gamma detector 在全实线上积分，付清 H=1 也存在的尾。
其 rowwise 高度和 partial maxima 由 Sobolev 与固定支撑分解处理。
最后计回 O((Nw)^(1/2)) 个 powerful parts，作连续分层优化，得到

\[
 C(U;a,H)\ll U^{G(a)+\epsilon}(1+H)^{p(a)+\epsilon},
 \qquad p(a)=1+\frac{2(1-a)}{3-2a},
\]

\[
 G(a)=\frac{8(1-a)}{7-6a}\quad(1/2<a\le5/6),
\]

以及高段的安全延伸

\[
 G_{\rm safe}(a)=\min\{1,7/13+(56/13)(7/8-a)_+\}
 \quad(5/6<a<1).
\]

特别地 C(U;7/8,H)≪U^(7/13+ε)(1+H)^(6/5+ε)。原 inverse-only raw
指数为 5/8，新指数节省 9/104。完整高段最优密度函数未在本次证明。
上述结论是 [T/R]，不是把 BGL 的 squarefree-row corollary 原样套给
原全部 sixth-power-free 元素行。

## 3. 为什么这个节省仍不改最终边界

在原 above-floor 域 δ=2a−1∈(1/50,3/4]，κ∈[37/50,1]、x=q/δ∈[0,1/2]，
令 c=1/(3κ)、D=3−(1+2c)x、P=(2−2cx)(1−x)。[450](450-plain-kappa-extension-and-actual-capacity.md)
的最终原 inverse/plain/slot/amplification 包络已经满足

\[
 2D-3P=2x(2+c-3cx)\ge0,
 \qquad R_{*,\kappa}\le r_0(\delta)=\frac{15-16\delta}{15-6\delta}.
\]

本次实际付清的两个 raw 指数与 r_0 的差分别为

\[
 \frac{\delta(25-24\delta)}{(4-3\delta)(15-6\delta)}>0
 \quad(\delta\le2/3),
\]

\[
 \frac{225-380\delta+168\delta^2}{13(15-6\delta)}>0
 \quad(2/3\le\delta\le3/4).
\]

因此对每个实际 above-floor bin，直接取 min 都仍是原最终包络。
即使高段进一步达到文献最优 g，也有完整全域严格支配证明。
δ=1/50 的闭端点仅用于代数延拓；不能将 floor 当成有实际零点的行。

[451](451-kappa-feedback-cubic-boundary-and-family-continuation.md) 的关键行在
a_*≈0.694291677133，原最终指数为 2/3，而新 raw 指数约 0.862897287510。
a_* 是行的 bin，不能与全族最高零点实部 β_* 混同。
另在 a≥73/86 的整个连续矩形，12 个精确双 Bernstein 系数均大于 1/25，
证明原 endpoint E_*<−1/125。高行计数只加强本已严格的区间，不能移动
唯一等号点。

## 4. 已付结果、剩余接口与复核

已付：原全行 raw 密度、所有 powerful 层和高度尾、最终包络全域比较、
高行区间严格连续证书。未付：密度与原共同 inverse/plain 槽的新的联合
放大计数，以及能改善实际比例的原正高度短窗 scalar fourth upper。
不能将两个独立 upper 相乘或机械取幂作为联合证明。

继续工作的主接口是 [472](472-original-short-carrier-fourth-compression-and-ratio-variance.md)
的原 short-carrier ratio 方差；新 scalar fourth 准入正在独审。
实际比例、σ_* 和已有边界论文保持原认证范围。本次没有新边界论文。

[精确检查器](../scripts/hybrid_detector_density_checkpoint.py) 核对连续 affine
分支、精确指数恒等式、全域差式、12 个 Bernstein 系数及全文 hash 绑定。
[输出证书](../output/hybrid-detector-density-checkpoint.json) 不替代分析证明。
本笔记另待 [全文独审](../reviews/2026-10-08/473-original-density-and-envelope-review-radial.md)。
