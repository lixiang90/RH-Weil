# 2026-10-08 零点比例公开前沿核查

检索日：2026-10-08。项目比较基线为 main
`0cb98a7de5c92c949efbe9cfb3012d7716194e0c` 的
[479](../../notes/479-original-type-ii-factor-reduction-and-diagonal-gauge.md)。
本次核查回答用户的条件请求：若项目比例已超过此前最佳，就撰写并发布论文。

**当前不能以新纪录为由发布比例论文。** 项目的简单临界线比例下界为
67.30581102819731…%，超过 Alpöge–Furman / Lamzouri 的 MT 基准，
但低于后续同口径研究稿。最新检索还找到十月六日的形式化登记值
67.34824%；其网页目标只写不同临界线零点，原始证明内部则先给简单临界线零点下界。
下文区分原作者的证明主张、平台验证报告和本轮实际核查范围。

## 1. 比较口径

分母 \(N(T)\) 计 \(0<\Im\rho\le T\) 的全部非平凡零点及重数；
分子 \(N_0^s(T)\) 计简单且满足 \(\Re\rho=1/2\) 的零点。
比较量为 \(\liminf N_0^s(T)/N(T)\)。
不同临界线零点 \(N_0^*(T)\) 可以含高重数点，不能从其下界反推简单性。
全部不同零点以及“简单或在临界线”的比例也不等于本比较量。

固定 dyadic 下界蕴含相同的前缀下界：对给定误差，把充分大的
\((T/2^{j+1},T/2^j]\) 求和；剩余有界高度的计数为 \(o(N(T))\)。
这是计数推论，不能借前缀 / dyadic 的记法排除同一结果。
表中百分数均为渐近下界，有限高度计算不参与排序。

## 2. 原始来源与当前状态

| 来源及版本 | 简单临界线比例 | 本轮核准的状态 |
|---|---:|---|
| [Alpöge–Furman v2](https://arxiv.org/abs/2608.13637v2)，2026-08-19；[Lamzouri v2，Theorem 1.1](https://arxiv.org/html/2609.02882v2)，2026-09-08 | 67.2500703679…% | 无条件 MT 基准；后者给另一直接 Hilbert 空间证明，同一数值。 |
| 本项目 479 | 67.30581102819731…% | 同一 MT 窗、六邻域及负对角调节；仓库内证明、独立线程审查和冻结区间检查已完成。未声称外部专家审查或端到端 Lean 认证。 |
| [Shi 当前作者仓库](https://github.com/yuhangshi888/zeta-simple-zeros-673316977)，稿件 2026-08-14 | 67.33169771424713…% | 作者仍标为待独立审查的研究稿候选；Lean 覆盖有限维支持平面和精确比较，导入的解析接口与七 / 九点大证书另列。 |
| [Devine，Zenodo 22066689](https://zenodo.org/records/22066689)，v1.0.3 / PDF v3，2026-08-23 | 67.3399% | 原文 Theorem 1 主张无条件；PDF 第1、7页说明完整形式化可重放数值包仍在准备。本轮未重放其全部证书。 |
| [Gebendorfer，Compatible triples](https://www.researchgate.net/publication/414060404_Compatible_triples_and_a_periodic-mixture_obstruction_for_a_critical-line_zero_certificate)，2026-09-07 | 67.34765075443219…% | Theorem 1.1，前缀简单临界线口径；无 RH 等额外数论猜想。作者注明内部验证已完成、独立审查与新颖性评估开放。 |
| [dani-ani0 的平台登记](https://www.riemannzeta.fun/submissions/dani-bound-2026)，2026-10-06 | 67.34824% 可由内部简单零点定理推出 | 平台报告 Lean / nanoda 验证；登记目标为不同临界线零点。下节说明从原始简单计数定理得到同值的推论。专家审查未记录；本轮未运行外部形式化工程。 |

以上是已定位的可比较来源，不是穷尽所有公开声明的排行榜，
也不把平台形式化登记等同于数学界已经确认的最终世界纪录。
即使暂不依赖最后一行的简单性推论，已有较高的同口径研究稿，
仍不能认领项目超过所有此前公开结果。

## 3. 十月六日形式化结果的计数核对

固定原始提交：
[`d272437e7ebeb17b87c8c3d7cece592aa23785ab`](https://github.com/josusanmartin/riemann/tree/d272437e7ebeb17b87c8c3d7cece592aa23785ab)。
固定上游的[计数定义](https://github.com/anthropics/zeta-23-lean/blob/3635e74826a4c1fcece7d1cd2b6fa75e43a00510/Zeta23/Statement.lean#L43)
将 `N0simple` 定义为临界线且重数为1的点数；
[解析输入定理](https://github.com/anthropics/zeta-23-lean/blob/3635e74826a4c1fcece7d1cd2b6fa75e43a00510/Zeta23/Final.lean#L291)
给出 `paperInputs_zeta`，未添加数论猜想前件。
[Solution.lean](https://github.com/josusanmartin/riemann/blob/d272437e7ebeb17b87c8c3d7cece592aa23785ab/submissions/dani-bound-2026/proof/Solution.lean)
中的 `Zeta23Ext.BridgeW.n_point_bound_w'_sqrt` 先证明
\[
 (\Phi_{\rm sqrt}-\varepsilon)N(T,2T)\le N_0^{\rm simple}(T,2T).
\]
随后 `AMW.am_dyadic_n_sqrt` 才使用
`N0simple_le_N0star'` 将结论减弱为不同临界线零点。
最终 `RiemannFail.kappa_le` 和 `cert_AM` 取八点、块长152，
得到登记值 \(6734824/10^7\le\Phi_{\rm sqrt}\)。
因此，同值简单临界线下界是原文件内部定理的直接实例化推论，
并非由不同计数的大小关系反推；前缀版再用上一节求和。

该方案联合调整余弦窗和八点压力，使用
\(f_\tau(E)=E\)（\(E\le\tau\)）与
\(f_\tau(E)=2\sqrt{\tau E}-\tau\)（\(E>\tau\)），\(\tau=8/7\)。
这是当前原比例路线值得对照的有限谱改进。
[平台合同](https://www.riemannzeta.fun/challenge)
固定计数定义和依赖；[验证方法](https://www.riemannzeta.fun/methodology)
说明两核、允许公理及执行范围。这里报告平台和源文件证据，
不声称本项目本轮复跑约1.9万行证明及其依赖。

## 4. 严格数值比较与发布决定

从[已提交检查点](../../output/hybrid-original-type-ii-factor-checkpoint.json)
读取 \(p_{\rm dg}\) 的有理上下端；其 canonical LF SHA256 仍为
`88ff98918fa6fda62996e848e120a7ffdf0030472b9709c94cb9f61ac5f09b1e`。
利用 \(C_0\) 和 \(p_{\rm dg}\) 的冻结有理包围，以 `Fraction` 精确验证
\[
 C_0<p_{\rm dg}<\frac{673399}{10^6}
 <\frac{54923339574680150762799}{81551975398437500000000}
 <\frac{6734824}{10^7}.
\]
Decimal 只显示差值，不负责判定。项目高于旧 \(C_0\) 约
0.05574066026 个百分点，低于十月六日登记值约
**0.04242897180 个百分点**。

本轮保存文献比较，暂不撰写或发布“刷新最佳比例”的论文。
后续保持原数域路线，先核读较强的窗 / 八点谱预算，再判断是否可用于实际零点接口；
原 Type II 完整四矩和无零边界的缺项仍须分别支付。
上述外部比例没有自动改善原 Hecke 全族深度、\(\kappa\) 或四阶常数。

## 5. 条件结果、待核高矩和撤稿

Devine 的超过67.92%部分另要求 BOX-DENS 或 PROFILE-DENS；
其 range-15 数值候选不能替代无条件主定理。
Gebendorfer 的0.674034是指定证书类的方法上限，方向不是零点比例下界。

[Wang，arXiv:2609.24167](https://arxiv.org/abs/2609.24167)
的 \(C_0+6.66624\ldots\times10^{-8}\) 改进已于2026-10-06撤回，
当前 v2 明确为 withdrawn；不纳入有效基准。

[Yang–Yang 的79.62%记录](https://zenodo.org/records/21975237)
作者自标 certified-candidate、外部审查待完成，另涉及高阶矩的实际解析渐近。
本轮核对了原文的高矩传递及有限有理证书，尚未取得完整解析链的独立认证；
不能仅将自存档标题作为已确认纪录。本项目的真实四矩预算仍须单独闭合。

本次核查只保存链接、版本、计数合同和比较结论；
没有新增外部 PDF 归档，也没有认证外部大证书或无限解析输入。
旧[305审计](../../notes/305-post-6725-literature-baseline-audit.md)保留历史检索状态。
