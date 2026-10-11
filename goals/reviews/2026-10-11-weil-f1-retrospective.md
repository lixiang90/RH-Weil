# Weil 类比与 F₁ 路线的历史复盘和下一步方向

2026-10-11。按用户要求，把研究重心转回数域 Weil 结构、F₁ 几何及其算术来源。本次回顾编号001–437的437篇笔记；438以后的近期无零界和比例常数优化不作为本次主线。早期 partial-Weil 配置仍纳入，因为它们检验的是从实际算术矩到 Weil 结论的桥梁。

这段研究已经得到明确的条件定理、实际局部构造、若干真正的算术误差估计和有针对性的反例。它没有构造出迫使通常 ζ 零点落在中心线的完整数域 Weil 结构。最需要解决的仍是：**从独立的算术或几何来源得到正性，并在同一对象上完成全局比较。** 晚期 F₁ 工作还把此前笼统的“缺少实现”具体化为主关系、算子域、边界读出和截面存在性之间的相容问题。

下面的方向判断基于这些已核读的内部结果，不是对所有 F₁ 理论的分类，也不是新的 RH 证明。旧笔记和论文保留原文；发现的后续修正以链接指出。

## 1. 最值得保留的成果

| 阶段 | 已经得到什么 | 尚未跨过什么 |
|---|---|---|
| 极化、Lefschetz 与迹公式 | [001](../../notes/001-polarized-weil-structure.md)证明相容正 Hermitian 型、全部幂迹增长或闭算子伴随条件能够迫使谱居中；[002](../../notes/002-global-existence-audit.md)分开空间、行列式、全局迹与正性。 | 条件定理没有提供数域上的实际正性来源；局部素数纯性不能直接约束全局 ζ 谱。 |
| 谱模型、正实函数与有限认证 | 已有把负迹、正规族和有限证书连到中心线结论的明确接口。 | 完整负迹预算、谱识别、域及尾项仍须独立证明；把这些列成存在性字段不减少其难度。 |
| 实际算术与有限 word | threshold/profinite 等构造确实增加了算术结构；完整 word 和有限负谱检测有严格公式。 | 检测负部不等于消除负部；内部正 Gram 不自动产生跨 fiber 的算术配对。 |
| partial-Weil 与 Brownian／Abel | [197](../../notes/197-partial-weil-proportions-regions-four-moments.md)明确有限矩的消费范围；[275](../../notes/275-record-envelope-and-growing-low-frequency-closure.md)、[279](../../notes/279-record-controlled-arithmetic-prefix-deletion.md)、[284](../../notes/284-causal-abel-inverse-and-diagonal-record-selection.md)、[289](../../notes/289-growing-resolvent-jets-and-polylog-spectral-localization.md)给实际记录选择、低频、前缀删除和余核谱高度缩减。 | 实际有符号交叉估计及完整 Gamma／参数迁移仍开放；相对矩预算不能自动替代完整 Weil 负迹预算。 |
| F₁ 的复提升与周期局部几何 | 单素数的实指数来源、解析周期商、Cartier 局部模型和实际截面不再只是名称。 | 局部周期商不自动实现全局主商、双次数、非局部交叉和 RR；真实平方也可能没有所需有限呈现或 Cartier 对角。 |
| F₁ 的源代数与边界 | [427](../../notes/427-f1-corner-product-algebra-and-unavoidable-trace-cocycle.md)、[429](../../notes/429-f1-original-unitary-crosses-the-fixed-corner-domain.md)、[435](../../notes/435-f1-haar-trace-of-all-source-conjugates.md)得到实际交换子、源作用和截止迹的公式。 | [436](../../notes/436-f1-physical-cutoff-of-the-source-cesaro-limit.md)、[437](../../notes/437-f1-finite-source-word-without-a-linear-physical-finite-part.md)证明原读出不能自动延拓到范数完成或全部有限源词。 |

这些成果的共同价值是确定了必须保留的算术数据和实际损失，并排除了具体的捷径。笔记数量、有限模型吻合度和接口字段数量本身不衡量离 RH 还有多远。

## 2. 正性来源是核心：用一对正反基准检查新路线

[307](../../notes/307-odd-polarization-and-elliptic-degree-benchmark.md)是一个应当保留的正基准。对真实曲线
\(E/\mathbf F_5:y^2=x^3-x\)，几何上的次数正性给出

\[
\deg([m]-[n]\pi)=m^2+2mn+5n^2=(m+n)^2+4n^2.
\]

因此可以在识别复特征值之前取得正型，并核验
\(F^{\mathsf T}HF=5H\)。它还暴露并修正了早期奇次 primitive 极化中令标量星算子等于恒等的错误：奇次实向量的自乘为零，不能这样得到正定型。修正后的相容复结构有真实函数域模型检验。

[290](../../notes/290-positive-euler-duality-model-and-mass-moment-nonidentification.md)提供负基准。固定

\[
Z(t)=\frac{1-qt+qt^2}{(1-t)(1-qt)},\qquad q\ge5,
\]

有正整数闭点 Euler 数据、精确反射函数方程、分次外代数、非退化 Poincaré 配对、代数 Hard Lefschetz 及相容超迹／行列式。它自己的正源还满足全部 cutoff 上的正权质量相对偶矩界和 common-multiplier Schur 增益。但两个 Frobenius 根的模分居 \(\sqrt q\) 两侧，与它们相容的正定权一极化不存在。

这不是实际代数曲线或 ζ 的反例。它说明上述抽象代数和正 Euler 条件仍缺一项会约束谱增长的正性。新候选应当解释：它从哪条独立定理取得307中由次数提供、290中恰好缺失的性质。任意另选一个正内积，或把归一化算子声明为酉，不能完成这一点。

与 RH 等价的存在性目标可以是有效研究目标。真正的问题是把尚未证明的目标当作已经实现的输入；“等价”本身不等于循环证明。

## 3. 几项反复出现的教训

**先检查目标是否识别中心线。** [286](../../notes/286-attained-spectral-edge-and-response-nonidentification.md)证明：若实际最右零点实部 \(\Theta<1\) 且上确界被达到，那么对应记录的净质量也随 \(Y^{\Theta-\sigma}\) 增长，质量归一化后的四阶预算仍可闭合。这里的离线情况是假设性的条件诊断，不是实际 ζ 反例；它揭示该证明机制尚未识别中心线。[290](../../notes/290-positive-euler-duality-model-and-mass-moment-nonidentification.md)则给出独立构造的联合模型反例。相对缩减必须接到完整 current 的绝对或可和预算，不能只展示一个趋于稳定的比值。

**局部、有限和全局之间需要明确的统一性。** [174](../../notes/174-nonconstructive-existence-and-branch-map.md)的逆极限分支要求非空紧有限包、连续相容限制及相应的可和误差，紧性本身不产生这些条件。196／202的有限可满足性补全可以免除预先选择相容 witnesses，但仍要逐有限约束提供统一预算。有限 PSD completion、同一处的正迹，或未经比较、延拓与统一预算认证的稀疏好序列本身都不够。单条共尾序列并非一律不足：[145](../../notes/145-bounded-defect-normality.md)在共同 Euler germ、Poisson admissibility 和有界负 Cauchy depth 下已经能够推出正规族／中心线。尤其不能把“几乎所有尺度好”与独立选择的极稀疏记录序列混用。有限认证只有在所需阶数、截断、参数和尾项上统一时，才可进入无限结论。

**既不能免费增加正性，也不要要求多余正性。** [128](../../notes/128-acyclic-completion-no-free-purity.md)的完全 acyclic 补全在分次行列式变分中精确抵消；[129](../../notes/129-primitive-residual-rigidity.md)的有限正 primitive 若不成对，就留下额外行列式因子；[130](../../notes/130-regularized-residual-anomaly-accounting.md)要求低阶迹逐项解释。相反，[078](../../notes/078-ihara-ramanujan-hodge-structure.md)的 band 端点允许 tempered Jordan，不能要求每个有效模型都满足更强半单极化。[147](../../notes/147-ratio-tail-square-quadratic-no-go.md)还说明全二次能量会把正常的临界正尖峰也惩罚成发散。应证明足够的单侧或容量迹关系，同时保住原 ζ 因子，不能用更强但错误的目标替代它。

**保留同一个被估计对象。** raw 矩与 centered 矩、Brownian 四阶能量与 Weil 矩阵的 \(\operatorname{tr}G^4\)、普通 Dirichlet 系数正性与对数导数系数正性是不同条件。[197](../../notes/197-partial-weil-proportions-regions-four-moments.md)、[288](../../notes/288-finite-euler-deformation-positivity-obstruction.md)、[290](../../notes/290-positive-euler-duality-model-and-mass-moment-nonidentification.md)分别给出这种混用的明确边界。194／195已有条件 response-to-Weil 公式；不能把问题说成“完全没有桥梁”。尚缺的是同一完整对象的常数项、绝对能量、Gamma、识别误差和参数迁移的付款。

**漂亮的大小条件也可能已经具有 RH 强度。** [169](../../notes/169-selberg-profile-rh-equivalence-resonance-wedge.md)、[276](../../notes/276-short-increment-and-square-root-input-obstructions.md)、[299](../../notes/299-local-one-sided-budget-mellin-strength-audit.md)需要按实际范围阅读。固定频窗、单侧或 polylog 等字样并不保证条件弱：当量词覆盖全部足够大尺度时，Mellin 重建可以恢复 RH 的强度。不能把这样的未证输入称为常规 Bessel 界或软紧性结论。

**后续纠错优先于旧摘要。** 早期某些四矩笔记曾把截断计算称为完整闭合。232以后检查发现 \(ab\le XL^2\) 没有覆盖完整 physical alternating support；遗漏区的原子对角仍处于主尺度，高乘积 off-diagonal 没有闭合。另一方面，旧 \(U=V=\lfloor\sqrt N\rfloor\) 分解中的 Type II 实际恒零，242已修正。复用旧结果必须先检查支持集、分解量词及最新修订，不能按前篇的 complete 标签消费。

**反例要按假设集合逐项使用。** 正整数替代源可能不具有素数幂支撑或 Euler 乘积；某些饱和模型连亚纯延拓都不满足，而真实 ζ 已知满足。不能把不同模型各自保留的性质合并，声称得到了一个具有全部算术结构的反例。严格障碍的价值在于收窄指定构造，而非扩大成所有方法的不可能性。

**形式化消费引理与构造研究输入分开。** 局部代数定理通过 Lean，不提供尚缺的 `SourceRealization` 或全局 RR 实例；含已登记经典缺口的完整构建也不能替代传递公理审计。下一阶段应优先形式化已经获得的来源恒等式和反例，保持存在性字段的未实现状态。

## 4. F₁ 路线现在的具体障碍

不能再笼统地说“算术平方尚未构造”。既有 arithmetic/scaling site 有实际平方与对应，本仓库也有具体局部平方。真正要问的是哪一种平方支持所需的交叉、主关系和截面。

[402](../../notes/402-f1-intrinsic-ff-diagonal-conormal-obstruction.md)排除了指定普通 Fargues–Fontaine 平方中的 Cartier 对角方案：普通代数余切模在相应点具有无限维来源，不能按有限生成理想处理。这个结论不覆盖所有连续、导出或其他 F₁ 几何，但更换类别后需要重建来源与比较，不能沿用原接口的名字。

[403](../../notes/403-f1-support-locality-and-nonperfect-quotients.md)给出了比完整 RR 更早、也更便宜的检验。令非零 \(\varphi\ge0\) 支撑在零附近的小区间，取
\(f(x)=\varphi(x)\)、\(g(x)=\varphi(x-\log2)\)。两支集分离，而固定算术混合型满足

\[
W_{\rm pol}(f,g)\ge\frac{\log2}{2}\int e^u\varphi(u)^2\,du>0.
\]

所以“高度比分层＋保支集叠加＋支集局部交叉”的组合不能实现全部测试函数上的 G6。有效的几何必须产生有来源的非局部项。该例没有双矩为零要求；不能通过改小测试类回避现有 G6。

相对迹方向也已有清楚的限界。427的实际交换子迹非零，阻止在原 corner 代数上同时延拓普通 trace-class 迹并保持标量循环性。429表明真实源单位 \(u\) 会跨出该 corner 域，加入 trace-class 小修正不能补救。435完成固定源共轭的截止迹，但436给出 operator-norm 极限与物理截止极限不交换的实际素数周期例子。437更进一步：合法有限词 \(A(h)uA(k)\) 的物理迹减去任意 \(aK\) 都可不收敛。

因此，原标量循环迹、原 corner 域和原线性有限部不能作为下一步的默认公理。427的循环余类目前还没有独立选择正确的素数周期权；保留余类也不等于已经有算术读出。全局 RR 和可容许非零截面仍是更后面的独立任务。

## 5. 下一周期只保留一条主线和一条核对线

**主线：先构造有算术来源的非局部相对配对，先检验双素数及无穷位，再考虑全局 RR。** 来源优先使用已存在的 adelic／scaling 数据；源代数与循环边界可以作为具体实现候选。对每个候选固定对象、允许运算、主关系、拓扑和读出规则，不能根据目标数值倒填配对。

第一项任务是得到真实源产生的边界链或相对类，并证明它怎样保留纯素数周期、怎样处理单位与混合项。需要先面对429、436、437，而非假设所有源词都有原线性有限部。若保留相位数据或采用平均，必须从算术来源导出选择原则，证明与允许的辅助分割和截止相容；任意选子列或自由减项不算实现。相对类还须避开128–130的“补全后一切抵消”：证明周期实际由哪个未被消去的边界／primitive 承载，并逐项解释低阶迹及原 Euler／Gamma 因子，不能只证明一个抽象链是闭的。

这可以先缩成一个具体的小任务。在437原 \(p=2,q=5\) 的合法分割和同一有限词上，保留原 \(L=\log2,M=\log5\)、周期函数 \(P\) 与物理球尾 \(H\)，定义 \(\overline P=M^{-1}\int_0^M P(\theta)\,d\theta\)。检验是否存在由 \(P\) 唯一确定的 \(G\in C^\infty(\mathbb R/M\mathbb Z)\)，具有零 Haar 均值并满足

\[
G(\theta+L)-G(\theta)=P(\theta+L)-\overline P.
\]

若能独立证明该方程及其正则性，437的精确式给

\[
T_K=K\overline P+G(KL)-G(0)+H(KL).
\]

这里 \(H\) 不能丢弃，零均值规范也不能由目标 Weil 值选择。Fourier 解含 \(z_n\widehat P(n)/(z_n-1)\)，\(z_n=e^{2\pi i nL/M}\)；只证明 \(L/M\) 无理不足以支付小分母，需要独立的 Diophantine 界和实际光滑性估计。本次没有完成这项证明。若失败，停止此相位方案；若成功，它仅解释这一个有限词的截止相位，仍需检验整个源域在乘积、\(u,u^*\) 下的相容性、辅助分割变化，以及由实际边通量得到的闭链。它不恢复旧标量有限部，也不自动选择素数权。

第二项任务是独立计算403的 \(\log2\) 分离支集混合例子。430–437目前使用双有限位 Hilbert 源，其中的物理实时间并不等于无穷位几何。完整检验需要把[404](../../notes/404-f1-adelic-periodic-orbits-and-mixed-local-trace.md)的有限 \(S=\{\infty,2,5\}\) 来源接到实际相对闭链，并核对403中包含实位积分的全部算术项；单独得到素数2的原子项只能算局部比较。通过标准是从来源算出正确的非局部算术项，并明确无穷位和主项；通过一个例子还不等于全G6。如果配对仍然局部，立即停止这条接法。

第三项任务是在真实主商上检验

\[
\ker\overline A\subset\ker M_0\cap\ker M_1\cap\operatorname{rad}W_{\rm pol}.
\]

这是403给出的必要条件。源边界若被宣布为主关系，需要证明它同时消掉两个次数并落在混合型根空间；普通 K 类为零或某个相对链为边界都不能单独代替这项证明。若改动 G5 的下降条件，必须公开改写并重证后续桥梁。

这三项形成一个可停止的可行性周期。可晋级结果是新的实际来源公式、正确的混合例子、合法主关系，或对指定候选的新反例。若4轮后只有新的抽象字段、同一周期公式的换表示或未经来源选择的正则化，就暂停该候选；最迟第8轮复盘。不把“寻找更多空间”作为没有结束条件的任务。

**核对线：用307与290检查主线所声称的正性。** 不重新包装已经完成的椭圆曲线计算；检验新构造能否说明真实次数正性如何进入，而联合离线模型为何不满足同一来源定理。若它对290也自动给“正极化”，说明存在性、相容性或识别环节有误，应先修复。只有在实际配对、主商和可容许截面接口成立后，才投入全局 RR 型截面存在性与有效刚性；也允许独立的算术 Hodge 型不等式作为正性来源，但须证明它作用于同一实际对应。

Brownian／Abel、一般 GNS／Pick、compactness 和高阶矩暂作参考工具。已经完成的低频、前缀和谱尾结论保留，尚未出现新的实际交叉输入时不继续扩写。近期零点比例与无零界保留原成果，按本次用户指定的研究重心暂不继续优化。

## 6. 外部来源和复盘范围

本次另外核对了四篇一手文献的 arXiv 版本页及摘要，以确定方向判断的对象范围，不将摘要核对写成全文证明审查。[Geometry of the scaling site](https://arxiv.org/abs/1603.03191v1)的 RR 在单素数周期轨道上；[The Riemann–Roch strategy, Complex lift of the Scaling Site](https://arxiv.org/abs/1805.10501v1)构造 adelic 复提升及热带下降；[Riemann–Roch for overline Spec Z](https://arxiv.org/abs/2205.01391v2)是另一套依赖球谱、整数维数和 Serre 对偶的算术 RR；[Weil positivity and Trace formula, the archimedean place](https://arxiv.org/abs/2006.13771v1)研究无穷位的压缩迹与 Weil 分布差。这些各自的构造不能凭“已有 RR”这一名称替代本项目所需平方、固定算术交叉和全局可容许截面证明。

本次基线为 `331107b2ba0716d2fb78ec1f605f05fe57393274`。编号001–437共437篇、119,521行，其中113篇全文深读、324篇核读主要命题、机制、结论与限制。逐篇原始 SHA-256、具体阅读范围和判断归档在[覆盖账本](../../reviews/2026-10-11/weil-f1-retrospective-coverage.json)；各阶段详评见[001–149](../../reviews/2026-10-11/weil-f1-retrospective/early.md)、[150–300](../../reviews/2026-10-11/weil-f1-retrospective/middle.md)、[301–437](../../reviews/2026-10-11/weil-f1-retrospective/late.md)。哈希记录本工作区原始字节，源引用另固定到基线提交，以免不同换行格式影响核对。没有独立重放全部历史计算、外部证明或 Lean 工程，内部结论仍保留原有引用与审查范围。

文档链接、437篇原字节及既有文件保留情况另见[核对记录](../../reviews/2026-10-11/weil-f1-retrospective-validation.json)。这是用户指定的历史回顾和方向调整，不增加新的数学研究轮，不声明新边界或比例。第四周期后的已完成数学轮数仍为1；后续实际研究按既有4–8轮规则复盘。研究进展以新增独立来源与已消费的证明输入衡量。
