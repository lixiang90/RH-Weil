# Connes 近期论文的一手版本与证明边界

核验日期：2026-10-12。与[策略复盘](../../goals/reviews/2026-10-12-connes-frontier-and-equivalence-strategy.md)配套。
根代理及两条文献子任务分别核读下列指定章节，另一子任务复核本地旧合同。
不是所有论文及其全部参考文献的完整复审；没有新增公开PDF或改变历史归档统计。

## 1. 版本账本

| 文献 | 已核对版本／日期 | 一级来源 |
|---|---|---|
| Connes–van Suijlekom, Quadratic Forms, Real Zeros and Echoes of the Spectral Action | arXiv v1 2025-11-28；正式 CMP 406:312 (2025)，发表2025-11-18 | [arXiv](https://arxiv.org/abs/2511.23257)、[期刊](https://link.springer.com/article/10.1007/s00220-025-05493-1)、[作者正式PDF](https://www.waltervansuijlekom.nl/wp-content/uploads/2025/12/Araki-publCMP.pdf) |
| Connes–Consani–Moscovici, Zeta Spectral Triples | arXiv v1 2025-11-27；作者书目列2026 EMS系列 | [arXiv](https://arxiv.org/abs/2511.22755)、[全文](https://arxiv.org/html/2511.22755v1) |
| Connes, The Riemann Hypothesis: Past, Present and a Letter Through Time | arXiv v1 2026-02-03；JOMP 2(1), 1–52 (2026) | [arXiv](https://arxiv.org/abs/2602.04022)、[作者正式PDF](https://alainconnes.org/wp-content/uploads/JOMP_V02N01P01-2.pdf) |
| Connes–Consani–Moscovici, Zeta zeros and prolate wave operators | v1 2023-10-27，当前v2 2024-05-04；2024期刊版 | [版本页](https://arxiv.org/abs/2310.18423)、[v2全文](https://arxiv.org/html/2310.18423v2) |
| Connes–Consani, On the Jacobian of Spec Z | v1 2026-02-17 | [版本页](https://arxiv.org/abs/2602.15941) |
| Connes–Consani, On the Absolute Geometry of Spec Z | v1 2026-06-04 | [版本页](https://arxiv.org/abs/2606.06604) |
| Connes–Consani, The Absolute Twistor Line and the Geometry of overline Spec Z | v1 2026-08-31；编号虽为2609，首次提交为8月31日 | [版本页](https://arxiv.org/abs/2609.00299) |

作者[书目](https://alainconnes.org/fr/publications/)把 Quadratic Forms 列为2026年7月的条目，
与出版者正式记录不一致；采用期刊的2025年发表时间，不把书目日期当新定理日期。
版本时间采用提交历史，不能将HTML／PDF内的排版日期替代提交日期。

## 2. 实零点与半局部谱：准确消费范围

**Quadratic Forms。** 核读引言、§4–6，重点正式版定理6.1（p.17）及 Remark4.3。
定理有下有界、本质自伴、三角多项式 core、最低值单重孤立且偶等条件。
由半区间真实分布形成的特定矩阵结构是必需输入；
任意自伴矩阵并没有“最低向量 Fourier 变换全实零”的结论。
将最低值平移所得正商型不要求原型非负，不能拿它证明 Weil 正性。

**Zeta Spectral Triples。** 核读§3–5、§7–8；
定理3.6给连续算子的离散谱，定理5.10假设最低值 \(\epsilon_N\) 单重、
向量 \(\xi\) 为偶，且按 \(\delta_N(\xi)=1\) 正规化，给
\[
\det_{\rm reg}(D_{\log}^{(\lambda,N)}-z)
   =-i\lambda^{-iz}\widehat\xi(z).
\]
其自伴商内积来自 \(QW_\lambda^N-\epsilon_N I\)，不是原始 L²。
引理7.3给按论文规定标量正规化的 prolate 候选变换趋于 Ξ；
§8仍欠实际最低态的性质及与候选的足够强逼近。
固定λ的N极限不能支付λ增长的预算。

**2026综述。** 核读§4.1、§5–6、§7–8，未重审全部历史引用。
§6.6继续明确保留上述缺口。
§7.2的实位正性有规定支持窗及消失条件；
§7.4半局部迹中的算子不能直接视为正投影。
§7.5的相应热迹展开使用RH假设，不能反向作为无条件输入。
该文提供策略与数值证据，没有完成RH证明。

**2024 prolate。** 核读引言、§2、§3.6、§4.5–4.8、§5。
定理4.6及命题4.8给有限S的 Sonin 空间同构／整函数实现，
范数仍依赖S。其正算子迹与完整 Weil 分布的比较并未由这一同构自动得到。
形式算子关系也不能代替定义域、自伴延拓及全尺度误差。

## 3. 2026绝对几何：新增对象与未付接口

**Jacobian。** 核读引言与定理3.4、命题5.1、定理8.15及相关定义。
它用带刚性数据的秩一群及张量乘积描述 adelic/Picard 的幺半群扩张。
这里的 Jacobian 不是已经附有正极化并控制全部 ζ 谱的阿贝尔簇；
算术平方的交叉／Hodge 指数仍不是该文已证结论。

**Absolute Geometry。** 核读引言、§2–3、§5。
定理3.9连接任意 perfectoid 域 C 的局部点与其 tilt 的主单位盘；
定理3.16的 untilt 商识别另外假设特征p的域 F 代数闭。
§5末仍将相应 Frobenius 特征空间向周期轨道的下降列为后续工作。
本仓库371–375已经研究这类单素数桥，不能重新推荐为尚未做过的新任务。

**Absolute Twistor Line。** 核读摘要、引言、§2、§5–6、§7.1–7.2。
定理5.1与命题7.5提供复点、twistor实结构与奇整数Frobenius动力学。
该构造新增拱位的几何组织；未给完整ζ配对的正极化／有效对应不等式。
普通投影直线上的图次数与真正算术平方的交叉仍须另比较。
本次没有把局部复点或Hodge词汇升级成全局RH结论。

## 4. 本次文献核查的使用限制

以上定理可作为独立结构输入；未证的最低态识别、算术极限、
全局正性、主除子下降与正极化都保留为缺口。
实零函数的非零局部一致极限可以保留重零点：
最低态的单重条件不意味着极限 Ξ 必须有简单零点。

策略复盘的新优先级是研究同一真实 Weil 核的联合能量与算术来源，
并用保持分布结构的负对照检验算术敏感性。
这是一项方向判断，不是论文中已给的全局估计，也不是证明已找到突破口。
