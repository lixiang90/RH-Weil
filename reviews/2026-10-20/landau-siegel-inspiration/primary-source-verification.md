# Landau–Siegel 来源、版本与核查范围

2026-10-20。独立来源核查稿；本稿不改 STATE、不消耗数学轮，不认证整套外部证明。

## 1. 已实际取得的原始记录

**OpenAI。** [原稿目录](https://github.com/openai/math/tree/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026)和其 README 将作者记为 OpenAI、日期记为 2026-10-01。GitHub API 实核仓库 main 为 `1581d4cbdd69a0faf34b2089614fe2a814316a6a`，该提交时间 2026-10-12T21:55:24Z，是 PR 锁定配置的合并提交；不能把此提交时间误写为论文首次公开时间。目录包含 paper.pdf（404812 bytes，Git blob `e31b1a244f251439b01d930c906f4e0c91dfc3a8`）及 build/paper.tex（31166 bytes，blob `7e41c77c252348369ca0fb99cbe389271ba6ce86`）。本核查者实际读取目录/API/README 元数据；root 另外已通过 connector 取得并读取 [build/paper.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex) 的引言、定理与论证组织，因此已超出仅定位 PDF 的阶段，但未作整篇证明的独立审计，不把原证明每步当作已复核。

**Banks。** [arXiv:2610.15483v1](https://arxiv.org/abs/2610.15483v1)，题名 *On the OpenAI proof that Landau–Siegel zeros do not exist*，作者 William D. Banks；arXiv 记录首次提交为 2026-10-11 09:35:35 UTC，19页。实际读取 arXiv 元数据、摘要及 HTML 来源。摘要的精确量词是：存在绝对 q₀、δ₀>0，对 conductor q≥q₀ 的 primitive real Dirichlet character，任一 real zero β∈(0,1) 满足 (1−β)log q≥δ₀；给出 q₀=10¹⁰、δ₀=0.003。全 q≥3 的同一常数还结合 Lu–Zaman–Zhao 的有限导子计算，不能把此计算当作本文新证明的一部分。作者说其核心想法来自 OpenAI，新增明确常数和呈现；署名归属不替代数学核查。

**Kerr。** [arXiv:2610.21099v1](https://arxiv.org/abs/2610.21099v1)，题名 *A simpler proof that there are no Landau–Siegel zeros*，Bryce Kerr；首次提交 2026-10-15 02:01:25 UTC。本核查者取得元数据、摘要和 HTML 来源；root 另已读关键段并记录其小高度多项式与 Masser 非消失实现。两者读取范围应分开，不能由“简化”二字推出对截图每个细节的认可。

## 2. root 已实读、此稿仅承接定位的来源

- [Green 记录页](https://hexagonmath.org/2610.00311v2)及[五页 PDF](https://hexagonmath.org/pdf/2610.00311v2)：*On Landau–Siegel zeros*，Ben Green。root 已取得并读 PDF；记录顶页日期 10月17日，而 history 的 v2 为 10月18日，应保留版本区分。这里的标识是 **hexagon**，不是同号 arXiv，域名也不是 hexagon.ai。本核查者先前对猜测的 /abs/ 路径访问失败，不构成原文不存在的证据。
- [Tao 2026-10-19 原文](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/)：root 已读解释并定位其对后续改进的提及。本文不把 Tao 的说明当作独立的形式化检查或期刊审稿结论。
- **Kevin Barreto 三页稿**：本轮逐行数学审核的直接输入是用户所附三页截图，题名 *An elementary proof of the non-existence of Landau–Siegel zeros*。尚未取得公开稳定 URL；其“GPT-6 Astra”归属是作者在截图中的说明，不能独立支付任何非零性或整除论证。截图使用 Wronskian 代替 resultant 的具体内容由 root 的机制审核承担。

## 3. 形式化：确实查到范围说明，未运行证明核

实际读取了固定提交的 [lean/docs/003.md](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/docs/003.md)。该文档宣称的范围包括 ζ 和全部 Dirichlet L 的 Re(s)>7/8 零区、Q(√−3) 上有限阶 Hecke L 的对应零区，以及存在一个共同 c>0，使所有 q≥3、primitive nonprincipal **real** χ 和全部 real β∈(0,1) 满足 (1−β)log q≥c；包括两种奇偶性，没有给出 c 的明确值，且不排除 (0,1) 中其他实零点。

同时实际读取 [ComparatorChallenges/SiegelZeros.lean](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/lean/ComparatorChallenges/SiegelZeros.lean)：其目标确实使用 Mathlib 的 DirichletCharacter.LFunction，并把实值性、primitive、nonprincipal、q≥3、0<β<1 逐项写入量词。该文件两个目标以 `sorry` 结束，但它是 **comparator challenge 模板**；不能据此指控实际解答含 sorry，也不能把模板当作已证明结果。本轮未追踪完整解答依赖、可信公理清单或构建日志，未运行 Lean 核，因此只可说“仓库公布了相应形式化范围与目标”，不可说“本轮已核验其 Lean 证明”。更不能由该项目推断 Barreto 的 Wronskian 证明已形式化。

仓库 [README](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/README.md)和 [history](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/history.md)明确区分有无形式化及更正版本。这是应保存版本的理由，不是证明正确或错误的数学证据。

## 4. 主稿 §1 的来源与域审核

`goals/reviews/2026-10-20-landau-siegel-determinant-and-weil-facilities.md` §1 对原稿、后续版本、截图和形式化范围的区分可消费；Banks 常数和 Green 版本日期应依上述量词解释。该主稿把研究对象限定为 primitive nonprincipal **real** χ 是必要的。

截图首段已经写 primitive nonprincipal **real** Dirichlet character；后续 χ(p)=(d/p) 的二次特征表示是在这个域内使用。本核查者初读时漏看 real，一度发送了要求补足此词的错误消息；root 对照原图纠正，现撤销该疑点。主稿无需为此添加截图缺陷。

结论应表述为对外部新证明的局部审核、机制比较和启发。uniform logarithmic real-zero exclusion 不推出完整 RH，也不等于一般 g-integer 分布的完整 Weil 正性；“最简化”不是本轮可认证的全局最优性质。
