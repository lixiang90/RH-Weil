# 危险 core 原命题定位：signed resolvent／trace comparison

2026-10-28；独占定位稿，待 root 消费。仅执行 STATE 的一次短 primary 定位，不是数学合同或迭代。没有修改 STATE、cadence、Git，没有下载论文，没有认证新证明。

## 1. 恢复与去重

实际读取 goals/README、STATE、G20261027、宏观前沿当前入口、D20261028E、唯一 next-actual-core-source-location-gate，以及 strongest-old-sonin-recovery-correction；运行 research_state.py check / show，结构检查通过，现场工作树起始为空。C047 已耗用并结算，canonical Ac/S1 action cone 全物理源精确为边界；不重开该路线。本定位没有创建 C048／585。

最强旧范围以恢复补正为准：F_L={p<e^(2L)}，L 大且 ALL |R|≥exp(16e^L) 时，实际完整 Sonin 误差 ε_F_L 一致趋零，原 du 高频乘子界已付。此次目标只在阈值以下，尤其 Γ≲e^L 危险 core 及其与补空间的 coupling。542+555→557 仍只是 whole leading4/5 负惯性 UPPER。

去重实际查阅 literature/manifest.json、literature/README、10-12 Connes recent-paper-audit、10-28 causal-strategy-source-scope，并定位现有 Sonin／prolate／Burnol 记录。排除已审 2006.13771、2310.18423、2511.23257、2511.22755、2602.04022，以及已有局部 prolate／最低态／θ=16／clipping。没有重读这些论文以充新来源；作者 2026 IR／UV 方向由 root 并行负责。

## 2. 实际检索账本

仅三批 web search，共九条 query；每条限定 primary 域 arxiv.org／alainconnes.org。没有第四批，没有沿参考文献串 paper。

| 批次 | 原 query | 实际结果 |
|---|---|---|
| 1 | `"Sonin" "semilocal" "resolvent"`；`"Sonin" "trace" "comparison" "semilocal"`；`"Weil" "Sonin" "signed" "error"` | 仅返回 Connes 作者出版目录，所显 Sonin、prolate、实位正性、最低态均已去重；没有新原命题。 |
| 2 | `"Sonin" "inverse" "Gram" "trace"`；`"Sonin" "covariance" Weil`；`"semi-local" "Weil" "error" "projection"` | 工具返回无结果。 |
| 3 | `"Sonin" "semilocal" "trace" -site:alainconnes.org -2310.18423 -2006.13771`；`"Weil" "semilocal" "signed" "trace"`；`"quasi-inner" "Sonin" "estimate"` | 工具返回无结果。 |

第一批目录入口为 [Connes publications](https://alainconnes.org/publications/)。这是本次有限检索的结果，不是“相关文献不存在”的数学断言。

## 3. Root 提供的实际候选：只绑定陈述

Root 另定位 [bramble_trace, Sharp Schatten asymptotics and Sonin trace localization for semilocal Fourier cutoffs](https://rstation.ai/problems/riemann_hypothesis/papers/2)，页面标 v2、2026-10-16 01:00 UTC；[固定 v2 Markdown](https://rstation.ai/api/v1/papers/riemann_hypothesis_2/versions/2/download)。作者是 rStation 账户 u/bramble_trace；原作者稿可供定位，平台的 Accept 标签不作期刊评审或数学认证。本分支浏览工具因 text/markdown 类型拒取 API，先核 HTML 所显 v2；root 随后取得原件于 literature/local/2026-10-28-core-source-location/bramble-trace-rstation-2-v2.md。本分支独立核得 61862 字节、raw SHA256 `541098314b2ddc5f8645babf82086e87d16c46188268cbc7ed6cfc1f98720058`，CRLF→LF 后 SHA 相同；没有另下载。

实际读取 §1 Fourier／Hilbert 规范、§6 开头 (6.1)–(6.3)、Theorem 6.5 的 (6.17)–(6.19) 及末尾范围说明。网页 locator 分别为 L34–55、L287–311、L557–571、L677；没有审消费 Theorem 6.5 proof，也没有审完上游证明。Root 随后提出固定 test 总迹的不同准入，本分支另读本地原件 Th6.2 陈述（565–587 行）、Th6.4 陈述与紧随范围（879–886 行）；不审其 proof。检索工具附带显示的 proof 段落不等于本稿认证其正确性。

原陈述的最小记录：固定 h∈C_c^∞(R)，p 沿素数趋∞，ℓ=log p、a=p^(-1/2)、f_ℓ=h+V_ℓh，V_ℓh(y)=h(y−ℓ)。S=S_<p 为实际前驱素数 Sonin 正交投影，G=(1+a)^2I−aSBS，B=2I+V_ℓ+V_ℓ*，W0=T_h*T_h。协方差 Tr(SW0B(I−S)BSG^(-1))=O_h(ℓ^(9/10))；相应 ΔT=O_h(aℓ^(9/10))，而 E=T−q_∞,P 的单增量为

\[
 E_{\le p}(f_\ell)-E_{<p}(f_\ell)
 =2\ell a\|h\|_2^2+O_h(a\ell^{9/10}).
\]

这是误差增加的正方向／Sonin 未吸收临界素数项；原文明确仅为一个变源、一个增量，不判完整 Weil 型符号。原规范是 log du 的 L²、未归一 Fourier F(t)=∫f(y)e^(−ity)dy，Mellin 侧 dt/(2π)；不是把 Euler embedding 当等距。B、W0 必须保 ambient 作用，G 及其逆只在 Ran S；否则 (I−S) 交叉项失去原域。

## 4. 与 560 的实际代入门

下列是陈述适配检查，不是对候选 proof 的核实或新数学结论。

| 门 | 本次能定位的输入 | 尚不能消费的范围 |
|---|---|---|
| 实际投影／全逆 | (6.3) 所标 range 是有限 Euler 乘子作用于实位 Sonin；6.5 明写 G^(-1) 和 ambient cross covariance。 | 未据有界同构称等距；与 560 的 B_F P(PB_F*B_FP)^(-1)PB_F* 的逐规范运输仍应单独核。 |
| 原源与 norm | f_ℓ 是 log 坐标卷积源，h 固定且常数依赖 h；它是光滑 compact 源，非裸求值向量。 | ALL 原 complex Dlog 源、共同源半范数及改变 h／support／frequency 时的 uniform 费没有由该陈述给出。不能混同项目 r=e^(u/2)f 中未经转换的 f。 |
| Γ／proper powers／pole | 5.2 的相位导数列 Γ−全部有限 prime powers；6.1 把 q_∞,P 的半局部规范引向既有来源。 | 这并不重新支付 Γ 的 FP/contact 或全规范原证明。q_∞,P 不含完整双 pole；同源同一步的 pole 差分会消去，但不能删除全型的两个 pole。 |
| 成长量词 | 真正 S_<p 背景，p→∞，固定 h 的特定变源；非先固定 F 后频高→∞。 | ℓ=log p 不是项目 support 半窗 L_w；完整窗 F_L_w 要覆盖其 autocorrelation 看见的全部素数。f_ℓ 跨度约 ℓ+diam(supp h)，只增 p 不自动覆盖该窗所有近 p 素数。 |
| 系数方向 | E=正迹−局部算术型，单步 ΔE 为正 leading；与 560(1) 的误差角色同向，而非有利 −K 符号。 | 不给 560(2) 中完整 Q_L_w 的下界、K_L_w 上界或 ε 的全源有符号 domination。不能将 ΔE>0 叫作 Q<0。 |
| core／coupling | 协方差确有 S／(I−S) 的真实交叉，不是 ordinary positive Gram。 | 这不是 Γ≲e^L 的全频 multiplier core／补空间 coupling 型界；也没有所有 L 的整窗联合比较。不同 p 用不同 f_ℓ，不准直接 telescoping。 |

目前最接近的是 560(1) 的同 F 误差单增量接口，尚不是 560(2) 完整窗的输入。规范匹配、缺失覆盖和 ALL-source 量词不能用“actual”标签补齐。即便候选定理最终通过来源审查，其最初可消费后果也只是该指定单增量不吸收 leading prime；不自动改善 whole4/5 或移除危险 core／primitive 瓶颈。

## 5. 不同的可准入候选：§6 固定源总迹增长

Root 指出同一原件中不同于 6.5 的总迹陈述，本分支独立确认其量词确能给 560 完整型一个可检验候选。Th6.4 给 ALL 先固定 smooth compact 源 a 的 T_X(a)∼4|hat a(0)|² sqrt(X)/(log X)²（非零均值情形）；Th6.2 对每个先固定非零 a、k=ord_0 hat a 给 T_X(a)≥c_a sqrt(X)/(log X)^(2k+2)，均为 X→∞，没有 changing-source uniform 费。此处 a 是 log 卷积物理源，避免和项目 r=e^(u/2)f 中的 f 混名。

以下仅是核审前的条件代入账本，不认证原定理。若实际 S_X／t_F、源及规范匹配且该陈述通过 proof 审查，取 X_L 使 {p≤X_L}=F_L={p<e^(2L)}、X_L/e^(2L)→1，即可原样进入 560(2)。严格 endpoint 不无声改变：e^(2L) 非素数时取 X_L=e^(2L)，恰为素数时取 X_L=e^(2L)−1/2。固定 a 的自相关可见素数早已全部包含，故 Q_W(a) 与 pole 两项不随 L 变；保持 P_pole=2|<a,cosh>|²−2|<a,sinh>|²，有

\[
 \langle a,K_La\rangle
 =t_{F_L}(a)-Q_W(a)+P_{\mathrm{pole}}(a).
\]

因此候选若核实，对 hat a(0)≠0 的预期完整误差结论是

\[
 \langle a,K_La\rangle\sim |\widehat a(0)|^2 e^L/L^2.
\]

系数为 **1**，因为 log X_L∼2L，原系数4除以4；不再扣 Fourier 2π。零均值的非零源只能先用 Th6.2 得到 c'_a e^L/L^(2k+2) 的 eventual 正 lower，不能从 Th6.4 的零 leading 系数捏造同样 sharp 渐近。

这已经是完整 K_L 的正方向增长候选，不是模型 receiver 或欠全源 coverage 的单素数增量。与旧安全高频 K_hi=o(1) 合成，若核实可把同一 fixed a 的该增长定位到 |R|<exp(16e^L) 的实际剩余 Fourier 乘子部分。**旧高层结论本身只能给此阈值以下／Γ≲16e^L，不能再缩成 θ≤1、固定有界频段或某个零频峰。** 更细定位须原文另有正确、可运输的陈述，当前不消费。Fourier 部分账本也不被叫作同一 compact 物理源。

最强旧比较实际核了 531 的正迹合法性、535／570 的 fixed-F 实际不定、560 的全窗式和粗全 H inverse 下界、571／572 模型 receiver 及恢复补正的 actual safe-high。它们没有直接给这个 cofinal、fixed-source、实际完整 K 的 positive lower：尤其 560(6) 的输入不是 Sonin evaluator／Weil source，fixed-F 不定也不蕴含 F_L 总迹增长。未在这些已消费强旧中找到相同结论；这不是审完整个仓库后宣称全局首创。

**建议仅准一个限定来源门：固定 v2 的 §6 Th6.2／6.4 与该固定源总迹结论的必要前件核审。** 首门先逐项确认 S_X 与 560 的实际投影／全 Gram 逆、dt/(2π) 和源 a 的字典，再审 uniform evaluation／trial-space 对实际加权范数及 cofinal X 的依赖；失败即止，不借 6.5 或下一 paper 续门。成功也只给“此完整误差不能在 ALL fixed compact 源上统一 o(1)／O(1)”的实际必要费用证据，不能推出 Q<0、RH、whole4/5 改善、一般 source-adapted signed 修复失败或 primitive 容量。

## 6. 当前结算边界

三批搜索本身没有新命中；root 的实物候选现已实际打开固定陈述并有可代完整型的条件测试，故与“只有 6.5，无新准入”的初步判断不同。推荐的是上述唯一来源核审，**不是已经取得数学结论或已经通过原证明**；最终是否准入与 STATE 迁移由 root 消费决定。

本分支 0 数学轮，不预记 C048／585，也不把有限检索无命中说成方法不可能。实际已付／未付 bottleneck 暂未改变；候选若审成，才会改变“完整误差能否无费统一小”的一条箭头，仍不消除危险 core 的有利 signed domination／coupling 或同一非零 primitive／mixed 容量。已付安全高频不再列为 unknown。看板／STATE／Git 的 root 同步属于另一个结算步骤，本稿不宣称已同步。
