# 研究分支看板

本文件记录尚未进入正式论文的探索路线。严格推导见 [`notes/174-nonconstructive-existence-and-branch-map.md`](notes/174-nonconstructive-existence-and-branch-map.md)。

## 当前队列

| ID | 角色 | 下一最小引理 | 晋级条件 | 状态 |
|---|---|---|---|---|
| NCE-1 | 主线 | finite SDP 的 cell-packet capture ratio、coercivity 与实际负响应 | capture remainder一致消失，one-sided packet budget可和 | one-sided atomic theorem 已完成 |
| NCE-2 | 概念线 | fiberwise harmonic scalars 的 external synthesis correspondence | 给出跨 `q` fibers 且限制 rank-one amplification 的 arithmetic map | canonical fiber 内交换子为零 |
| NCE-3 | 工具线 | random cells 是否降低 arithmetic-specific packet response | 保留 joint cancellation并优于 `Theta(1+Nh)` universal capacity | universal random-grid route 已到 sharp no-go |
| NCE-4 | 备用线 | moment positivity 与 determinant visibility 的 dilation lemma | 前提只含有限算术 moments | 观察 |
| NCE-5 | 备用线 | one-prime/one-block extension，预算增量可和 | extension 不调用完整 Weil positivity | 观察 |
| NCE-6 | 备用线 | bounded-resolvent/negative-trace 的 ultraproduct 稳定性 | 先独立得到统一预算 `C` | 观察 |
| NCE-7 | 非构造主线 | short-word effects 对实际 negative level sets 的 response-weighted capture | capture error共尾可和且不调用 Selberg/RH 等价输入 | degree-one universal moment route 已 sharp no-go |
| NCE-8 | 构造主线 | 在 square-root Vaughan rectangle 上控制 exact Type I/II/continuum response Gram | all-ones Gram budget一致有界，且不退回 diagonal Selberg energies | exact divided-difference channelization已完成；有限 cross cancellation使 diagonal/full为1.95--3.36 |
| NCE-9 | 非构造补全 | 把 finite Cauchy-translate Schur block写成 joint signed Type I/II large-sieve form | uniform finite-block budget只用 length-side数据且弱于完整 RH criterion | finite satisfiability compactness与Gram/Schur判据已完成；33 translates捕获约23% package norm |
| MOM-1 | 四矩备用主线 | actual `m>X` adjacent boundary pseudocovariance 的 good-height little-oh | MT 窗 remainder 小于 0.0829099143，或闭合剩余 adjacent Gram | alternating/Farey primitive support（含完整 critical shell）已 atomic diagonalize |
| NCE-10 | 非构造补全 | 增长的 arithmetic mixed localizers 与 divisor-visible resolvent closure | 每个有限 word level 近正且 Archimedean 有界，闭包恢复 divisor | scalar fourth moments 有 65 维严格 no-go；finite-satisfiability completion 已证明 |
| OBS-1 | 文献线 | canonical Hamiltonian 的局部质量一致界与 noncollapse | 从 Euler/Gamma 方程而非 zeros 证明 | 文献审计 |
| OBS-2 | 系统线 | tracial negative-square realization theorem | 与 Cauchy Hodge index 精确对应 | 文献审计 |
| LONG-1 | 长期线 | threshold complex 的 dualizability 与 categorical supertrace | 获得非循环 positive categorical trace | 暂存 |
| LONG-2 | 长期线 | fixed-support function-field explicit-formula convergence | normalization 可随窗口统一审计 | 暂存 |

## 分支纪律

每条新分支必须记录：

1. 独立 arithmetic input；
2. 使用的非构造补全定理；
3. 推出中心线的精确接口；
4. RH/GRH 循环性审计；
5. 有限、可证伪的最小引理；
6. 晋级与停止条件。

只有在证明了一个不等价于 RH 的新引理，或把开放输入严格缩小后，分支才进入正式论文。若前提等价于完整 Weil positivity、uniform negative-index bound 或中心线本身，立即标记为“等价重述”并停止扩写。

## 近期主要路线 A--E（2026-09-01 阶段审计）

本节将当前技术分支压缩为五条主要路线，作为资源分配、晋级与止损的决策入口：A 为近期主线，B 为长期主线，C 为桥梁路线，D 为受限探索，E 为低风险验证路线。

### 路线 A / MOM-1：四阶矩增量（近期主线）

- **目标**：控制中心化四阶矩，严格改进当前约 `0.6725007` 的简单临界线零点比例。
- **当前基础**：零点侧尾项已经隔离；真实 m<=X adjacent family 已渐近对角化，m>X aggregate 已等价归约为 complex-symmetric boundary block 的 pseudocovariance BB^T。one-factor HS energy 为 O(N)；natural-scale covariance 不制造 phase cancellation；自然 lower/upper HS polarization 受 two-edge locality 阻断。首个 lower-boundary prime entry 的 normalized height mean square 又无条件趋于 1/(4 pi^2)，因此 uniform beta_L||B_X(T)||op=o(1) 路线严格失败。alternating ratio clusters 在 von Mangoldt 支撑下已分类：不同素数底 clusters 为 singleton，非中心同素数 chains 整体为 o(N)。恢复 dyadic local energy 后，任意单个 primitive box 在 AB<=XL^(2-epsilon) 均渐近对角化，且 fixed determinant graph 有 degree-two Schur bound；在 primitive 双曲区域 ab<=X 内，fixed aperture 的整条 radial chain 已由 signed Montgomery--Vaughan 压到 O(N/L)，所有 non-seam aperture crosses 绝对可和为 o(N)。其中 +/-L aliases 已由 translated-symbol support gap 与 trace-class remainder 闭合，+/-2L seams 已由双曲 ratio diameter 排空；ordinary pairs 又经 determinant lift 化为 (Lambda*Lambda) harmonic correlation，并由 Evans 的 almost-all E2-shift theorem 无条件闭合。整个 ab<=X primitive hyperbolic family 已 atomic diagonalize；定量化 Evans saving 后又闭合任意 fixed `kappa<1` 的 logarithmic supercritical collar `ab<=X L^kappa`。product/ratio 坐标证明卷积阶仍为 `Lambda*Lambda`，在 `ab asymp X L` transition layer，exact scalar kernel 的 resolution core 为 `|ad-bc| lesssim L`，而整层 atomic diagonal 已是 `O(N log L/L)=o(N)`；discriminant-uniform multiplicative upper-bound sieve 又把整个 fixed-`delta<1` transition resolution core 的 absolute main term压到 `O_delta(N L^{-(1-delta)/2}(log L)^5)=o(N)`。clustered vector-valued Fejér 大筛又把完整 transition aggregate（包括 oscillatory tail）压到 `o(N)`，并与 collar 拼接得到整个 primitive union 在任意 fixed `eta>0` 下对 `ab<=XL^(2-eta)` 的 atomic diagonalization。critical `ab asymp XL^2` 又被精确归约为四变量 factor-bin determinant incidence：elementary baseline 为 `D(H)<<RH L^2`，而任意 fixed `sigma<1` 的 `D(H)<<RH L^sigma(log L)^C` 已足够闭合全部 box ledger；`sigma=1` 仍停在主尺度。balanced critical box 已由二维 Selberg 上界筛与 Bettin--Chandee exact determinant main term 达到 natural scale；进一步以 moderate-aspect Kloosterman 外筛和 extreme-aspect 两线性形式直接筛无条件得到全部 factor boxes 的 `D(H)<<RH(log L)^C`，故完整 critical shell 与 alternating/Farey primitive support 已闭合。下一门槛回到 adjacent `m>X` boundary pseudocovariance；中心 block 与 dyadic family仍独立开放。
- **最小引理 A1c**：构造 relative gaps 为 o(T) 的共同 good heights，在其上证明 beta_L||B_X(T)||op=o(1)，或直接证明 note 206 的 BB^T pseudocovariance little-oh。必须保留两个实际 prime responses、exterior Gabor index 与无共轭 phase；所有四矩通道须共享同一 good-height set。
- **A2 状态 [T]**：已按 `V>=U^delta` / `V<U^delta` 分区闭合完整 critical shell。moderate 区用 Bettin--Chandee 外筛；extreme 区固定短 prime powers 后直接筛两条 affine forms，并以 `g=(b,d)` 的长度/shift 精确抵消保留 same-base pairs。当前最小引理恢复为 A1c。
- **晋级条件**：经严格归一化和区间认证得到
  \[
  b_4<0.3275499074,
  \]
  或者严格缩小交替比值通道所需的开放算术输入。
- **止损条件**：若匹配下界证明所选窗口或响应无法达到上述阈值，则停止继续调窗；将结果整理为四阶矩方法极限/no-go 定理，并把研究主力转向路线 B。
- **预期产物**：边界紧性引理、交替比值分块公式、完整四阶矩预算表，以及有理数或区间算术证书。

### 路线 B / NCE-8：Vaughan--Brownian 响应预条件（长期主线）

- **目标**：利用 Type I、Type II 与 continuum/Gamma 通道之间的真实交叉抵消，证明 square-root Vaughan rectangle 上的统一增益。
- **当前基础**：已有精确响应分解和有限矩阵实验；full Gram 相对于 diagonal budget 显示出显著改善，但尚未证明该改善在尺度增长时保持。
- **最小引理 B1**：固定一个平方根矩形和一个物理响应方向，写出完整 Type I/II/continuum Gram，并证明严格小于 `1`、与尺度无关的 response-specific Schur 因子。
- **算术边界**：不得用任意系数 Bessel 界替代实际响应估计；必须保留交叉项，并单独控制 continuum 和 Gamma 通道。
- **晋级条件**：解析证明有限实验中的增益不会随尺度消失，并将其转化为第二矩、负迹或截断 Weil 二次型的严格改善。
- **止损条件**：若尺度中性的下界迫使 Schur 因子趋于 `1`，或者 continuum 项必然抵消全部收益，则停止该参数族，不再增加新的核表示。
- **预期产物**：可独立陈述的 response Gram 定理，以及它对部分 Weil 比例或平方根共振楔的定量影响。

### 路线 C / VIS-1：离线零点深度可见性（桥梁路线）

- **目标**：不直接要求完全 Weil 正性，而是把负迹或负惯性转化为距离临界线至少 `eta` 的零点计数或密度上界。
- **核心对象**：离线零点除数特征在正背景商空间中的最小奇异值或下框架界
  \[
  v_T(\eta).
  \]
- **最小引理 C1**：在有限高度和固定 `eta>0` 下，证明压缩后离线零点特征的显式下框架界，并追踪它随 `T`、`eta` 和窗口参数的退化速度。
- **晋级条件**：将 `v_T(eta)` 与已有负迹预算结合，得到新的零密度估计、平均零自由区域，或者有限高度上的定量排除结论。
- **止损条件**：若解析估计和有限模型都表明最小奇异值以不可补偿的速度趋于零，则停止追求统一深度界，只保留固定高度或族平均版本。
- **路线定位**：这是从“零点比例”通向“零点位置控制”的桥梁，不应表述为 RH 的直接证明路线。

### 路线 D / NCE-10：混合词局部化与紧性完备化（受限探索）

- **目标**：寻找一个低复杂度、算术可估计并保持 divisor visibility 的有限 localizer system，使其正性可以通过紧性/GNS 极限传递。
- **已知限制**：65 维反例已经证明，前四个标量矩不足以推出完全正性；因此必须保留 mixed word moments 和 localizing matrices。
- **最小引理 D1**：在有限 Gabor 截断上构造最小 mixed-word localizer，并使用精确算术或 SDP 判断哪些词是消除负方向所必需的。
- **晋级条件**：
  1. 词长和矩阵规模具有统一控制；
  2. 每个约束都能归约到现有 Type I/II 可估计对象；
  3. divisor visibility 具有统一下界；
  4. 没有暗中调用完整 Weil positivity。
- **止损条件**：若所需词长随截断维数增长，或者约束已经等价编码完整 Weil positivity，则标记为“循环重述”并停止扩张框架。
- **资源限制**：在路线 A 或 B 的关键引理取得实质进展前，本路线只承担小比例探索工作。

### 路线 E / BENCH-1：函数域与 L 函数族平均基准（低风险验证）

- **目标**：在算术更可控的环境中闭合 partial Weil、Hodge/response Gram 或四阶矩机制，识别经典 zeta 情形中真正缺失的输入。
- **候选环境**：
  1. 函数域 zeta/L 函数；
  2. 原始 Dirichlet 特征平均；
  3. 具有可用大筛和精确迹公式的有限 L 函数族。
- **最小引理 E1**：选择一个明确模型，完整复现正部分、误差部分、深度特征和 finite-to-bulk 接口，并闭合至少一个在经典 zeta 情形中仍然开放的门槛。
- **晋级条件**：得到可以独立发表的函数域或族平均定理，或者唯一化经典 zeta 路线中缺失的算术输入。
- **止损条件**：若模型中的正性仅由已知 RH、有限域纯性或现成谱定理自动给出，因而无法测试本项目机制，则更换模型，不将该结果作为经典 RH 路线的证据。
- **路线价值**：承担架构验证、归一化核对和反例搜索，而不是宣称直接推进经典 RH。

### 路线组合与季度决策门

1. **第 1--2 周：冻结基线。**
   - 固定窗口、傅里叶约定和矩阵归一化；
   - 重跑全部脚本；
   - 为关键常数增加有理数或区间算术证书；
   - 建立“结论--引理--算术输入”依赖表。

2. **第 3--6 周：集中路线 A。**
   - adjacent channel 的整个 m<=X family 已完成；
   - 继续 supercritical Hankel aggregate 与 alternating ratio Gram；
   - 失败时形成明确反例、下界或尺度障碍。

3. **第 7--10 周：A/B 决策。**
   - 判断四阶矩预算是否可能越过比例改进阈值；
   - 同时只在一个固定平方根矩形上推进 B1；
   - 不扩展新的窗口族、响应族或核表示。

4. **第 11--12 周：晋级或止损。**
   - A 达到阈值：进入无条件比例改进论文的闭合阶段；
   - A 被证明不可达：主力切换到 B；
   - C 只有获得非退化可见性证据时才晋级；
   - D 保持受限探索状态；
   - E 负责独立验证架构和归一化。

注："周"是等效人类数学家的研究时间，AI的实际速度可能快得多。

建议资源比例：

| 路线 | 资源比例 | 定位 |
|---|---:|---|
| A / MOM-1 | 55% | 近期主线 |
| B / NCE-8 | 25% | 长期主线 |
| C / VIS-1 | 10% | 桥梁路线 |
| D / NCE-10 | 5% | 受限探索 |
| E / BENCH-1 | 5% | 验证与基准 |

每条路线只有在证明一个不等价于 RH 的新引理，或者严格缩小现有开放算术输入后，才能进入正式论文的主定理链。

## 文件约定

- 新笔记标题注明分支 ID，例如 `NCE-1`；
- 同一轮只保留一个主线，其余路线独立探索，不把未经证明的假设互相引用成结论；
- 每轮结束更新本表的“下一最小引理”和状态；
- Git branch 仍按交付任务管理；这里的 ID 表示数学思路分支，不强制创建长期 Git branch。

## 本轮分支成果

- [Adjacent Montgomery--Vaughan 闭合与 Hankel family no-go](notes/205-adjacent-mv-boundary-no-go.md)：沿 Toeplitz diagonals 精确分解 finite bulk Gram，并用圆周 Montgomery--Vaughan 不等式证明整个 m<=X 真实 adjacent family 渐近对角化；同时构造一致正则的 rank-one Toeplitz--Hankel defects，使 direct-sum 能量为 B 而 aggregate 达到 KB。因此 near-resonance 已闭合，下一输入唯一化为 m>X 的 actual factorized supercritical boundary coherence；alternating/Farey 通道仍独立开放。
- [Supercritical boundary 伪协方差与 scale-sensitive covariance no-go](notes/206-supercritical-boundary-pseudocovariance.md)：证明实际无限 prime response 为 complex symmetric，并把 m>X aggregate 渐近等价地写成 boundary block 的无共轭 pseudocovariance BB^T；无条件闭合 beta_L^2||B||_HS^2=O(N)，同时以相同 BB*、相同全部奇异值而 BB^T 分别为 0/最大值的矩阵对排除 natural-scale covariance 自动产生 phase cancellation。该 no-go 不排除 vanishing operator norm。
- [Boundary quarter-turn 最优化与局部化障碍](notes/207-quarter-turn-optimization-locality-obstruction.md)：精确求解 finite boundary block 的最优实正交 quarter-turn defect；证明 beta_L||B||op=o(1) 与已知 HS energy 合并后足以闭合 supercritical aggregate；同时证明 finite-band 及真实 smooth Gabor locality 使自然 lower/upper pairing 的 HS defect 回到未极化基准。
- [Boundary entry 正均方与 good-height 桥梁](notes/208-boundary-entry-mean-square-good-height.md)：从首个 lower-boundary entry 提取实际 prime Dirichlet polynomial，证明其 beta-normalized height mean square 趋于 1/(4 pi^2)，严格排除 uniform operator-smallness；并证明 relative gaps 为 o(T) 的共同 good heights 足以把零点比例结论传到所有高度。下一输入缩成 exceptional good-height joint response 或直接 BB^T phase cancellation。
- [Alternating ratio multiplicity collapse 与原 square-root core](notes/209-alternating-ratio-cluster-square-root-core.md)：证明实际 von Mangoldt ratio clusters 除中心与同素数 chains 外均为 singleton；非中心 chains 整体为 o(N)，ratio defects 具有 O(log L) direct-sum 转移，并闭合 Y<=X^(1/2-delta) primitive boxes。其“square-root 是 within-box hard threshold”的解释已由笔记 210 修正；保留该条作为可审计的推导历史。
- [Local prime-power energy 与 square-root box closure](notes/210-local-prime-energy-square-root-box-closure.md)：恢复 W2(Y)=O(log Y) 与 W1(Y)=O(sqrt Y) 的 dyadic 算术预算，把单个 rectangular primitive box 的闭合范围推进到 AB<=XL^(2-epsilon)，从而无条件闭合 balanced square-root box。固定 h determinant incidence 的最大入/出度均为2，给 actual-response Schur bound并闭合 h=±2 within-box layer。下一输入改为跨 radial boxes 的可和 almost orthogonality。
- [Radial cross-box coherence 障碍](notes/211-radial-cross-box-coherence-obstruction.md)：证明 AB<=X 时每个 box norm 为 O(N/L^2)，故 fixed-pair o(N) 只是 Cauchy 后果；构造 J≈L 个 coherent vectors 使 pairwise o(N) 而 union 达到 N。alternating symbol 精确分解出 radial endpoint factor，admissible plateau windows 的 normalized row sum 为 Theta(L)；cross-scale determinant degree Schur 的 sqrt(lambda) 基线又由星图达到。其 absolute far-radial row-sum 条件后来由笔记 212 的 signed Montgomery--Vaughan route 绕过。
- [Hyperbolic radial-chain closure 与 aperture seam compression](notes/212-hyperbolic-radial-chain-aperture-seam.md)：证明 ab,cd<=X 时 distinct ratios 的 real log-gap 至少 1/(2X)；fixed aperture 的 symbol/mass budgets 为 O(L^3)/O(sqrt X)，从而整条 radial chain 为 O(N/L)。除普通邻接及 +/-L,+/-2L circular aliases 外，所有 aperture cross terms 绝对可和为 o(N)，把 primitive hyperbolic hard input 压成 O(L)-vertex/O(L)-edge seam Gram；tridiagonal PSD 反例说明 bounded degree 仍可保留 N/2 excess。
- [Radial alias seam 的精确支撑间隙与迹类闭合](notes/213-radial-alias-seam-support-gap.md)：建立 finite Toeplitz translated-symbol trace identity；证明 |(s-t)-L|<log2 时平移后的 high/low radial symbols 逐原子严格不交，间隙恰为 log b>=log2。trace-class Hankel factorization 把全部 +/-L finite seams 压到 o(N)，而 ratio diameter 直接排空 +/-2L seams；aperture hard input 因而唯一化为 ordinary neighboring seam Gram。
- [二素数谐和相关闭合 ordinary ratio seam](notes/214-semiprime-harmonic-correlation-ordinary-seam.md)：把 ordinary translated overlap 按 m=ad、n=bc、h=m-n 精确压成 (Lambda*Lambda)(m)(Lambda*Lambda)(n)/|m-n| 的谐和相关。利用 Evans 已发表的 almost-all E2-shift theorem，并以 elementary second moment 吸收小 shifts、exceptional shifts 与大 shifts，证明 harmonic energy=o(XL^4)；由此无条件闭合全部 ordinary pairs，并得到 ab<=X primitive hyperbolic ratio family 的 atomic diagonalization。
- [定量 E2 saving 与 supercritical logarithmic collar](notes/215-quantitative-e2-supercritical-collar.md)：将谐和二素数相关加强为对每个 `theta>0` 的 `o_theta(Y log^(3+theta)Y)`，并用 product-excess/ratio 坐标证明 determinant scale 为 `Y=X exp((e+e')/2)`、卷积阶仍是 Lambda*Lambda。由此对任意 fixed `kappa<1`，把完整 primitive atomic diagonalization 推进到 `ab<=X log^kappa X`；同时证明当前 absolute-Evans majorant 在临界 `kappa=1` 处逻辑上不推出 little-oh，把下一输入缩到 `ab asymp X log X` 的 response-weighted transition correlation。
- [Transition kernel resolution 与 Evans factor-bin 覆盖障碍](notes/216-transition-kernel-resolution-and-evans-gap.md)：把 transition bulk Gram 精确降为保留 six-window weight、Gabor index 和实际 height phase 的 scalar determinant kernel，识别 resolution threshold `H_res=Y/X`；证明整层 atomic diagonal 为 `O(N log L/L)=o(N)`，故 constant frame bound 已足够。正式文献审计证明 Evans 1.1 的指定 small-factor window 与 Evans 1.3 的 subexponential shift threshold 都不覆盖 balanced polylog core；有限实际核显示 absolute/diagonal 约 0.44--0.53，而 signed/diagonal 约 -0.04。
- [Discriminant-uniform sieve 闭合 transition resolution core](notes/217-discriminant-uniform-sieve-core-closure.md)：对 `f_z(n)=z^{Omega(n)}` 优化 Henriot--Holowinsky uniform shifted-multiplicative upper bound，得到 `Lambda*Lambda` 的逐 small-shift sieve saving；由此无条件证明 fixed `delta<1` 的整个 transition resolution core absolute contribution 为 `O_delta(N L^{-(1-delta)/2}(log L)^5)=o(N)`。同时识别 affine determinant fibers 并给出 `X=10000` 的 actual five-vertex prime-power core clique，说明 constant maximum-degree/frame 目标不必要且过强；下一输入只剩 oscillatory tail。
- [Clustered Fejér 大筛闭合 transition tail](notes/218-clustered-fejer-transition-closure.md)：证明 translated six-window overlap 是非负 Hilbert-cone Gram，并建立允许任意频率 multiplicity 的 clustered vector-valued Fejér inequality；由上一轮 core local mass 推出 fixed `delta<1` 的完整 transition finite aggregate 为 `o(N)`。与 collar 拼接后，整个 primitive union 对任意 fixed `eta>0` 在 `ab<=XL^(2-eta)` 内 atomic diagonalize；下一输入移到 critical logarithmic-square shell。
- [Critical logarithmic-square scalar-budget no-go](notes/219-critical-log-square-budget-no-go.md)：构造 density `1/L`、height `L^2` 的非负稀疏模型，同时满足 `sum A asymp RL`、`sum A^2 asymp RL^3` 及所有 `h<=L^2` 的 natural-size correlation `asymp RL^2`，却使 critical local proxy 为 `asymp N`。因此仅继续优化同类 scalar upper bounds 不能闭合顶层；下一输入必须保留 factorization/window 或跨通道结构。
- [Critical factor-bin determinant sieve threshold](notes/220-factor-bin-determinant-sieve-threshold.md)：对 ratio-compatible boxes 定义保留四个 `Lambda` factors 的 `D(H)`，证明 elementary `D(H)<<RH L^2`；再证明任何 `sigma<1` 的 `D(H)<<RH L^sigma(log L)^C` 足以闭合整个 critical shell，而 `sigma=1` 仍是 endpoint ceiling。其 direct-substitution no-go 仍有效，但 balanced case 的间接 Selberg 接口已由下一笔记补足。
- [Balanced critical Selberg--Kloosterman closure](notes/221-balanced-critical-selberg-kloosterman-closure.md)：把两个 smooth determinant coordinates 外置为二维 Selberg sieve，证明 Bettin--Chandee 主项的 exact density `1_((q1,q2)|h)(q1,q2)/(q1q2)`；其 `Y^(-1/20)` error saving 支撑 fixed positive sieve level，singular factor 又有 bounded first mean，故无条件得到单个 balanced critical box 的 natural bound `D(H)<<RH`（`sigma=0`）；该笔记把当时的下一输入缩为 unbalanced aspect-uniform ledger。
- [Unbalanced critical determinant shell closure](notes/222-unbalanced-critical-determinant-shell-closure.md)：以 long/short scales `U,V` 分区。`V>=U^delta` 时筛 long coordinates，Bettin--Chandee remainder 比 balanced case 更小；`V<U^delta` 时 fixed short factors把 determinant fiber化为长度 `K>U^(1-delta)` 的两线性形式筛。对任意 `g=(b,d)`，affine length 的 `g` 与 admissible shifts 的 `1/g` 精确抵消，故 same-base short powers也保留。最终一致得到 `D(H)<<RH(log L)^C`，由 note 220-B 闭合整个 critical shell。

- [有限 Gabor 相邻通道的 Toeplitz--Hankel 转移](notes/204-toeplitz-hankel-adjacent-transfer.md)：建立精确有限 Toeplitz 乘积公式，证明 crossing Hankel 能量为 `O(log L)`；结合素数幂退化的可和预算，把 bulk exact-product edge tightness 无损传到真实有限 adjacent 压缩，并证明 `m>X` 无周期折返泄漏。该结果只控制乘积簇的 direct-sum 平方和；不同簇的 near-resonance Gram 与 alternating/Farey ratio Gram 仍开放。

- [Adjacent product bulk edge tightness](notes/203-adjacent-bulk-edge-tightness.md)：仅用无条件 Mertens 型 `sum Lambda(n)^2/n` 渐近，证明理想 bulk 的 exact-product adjacent endpoint mass 对一般端点消失阶 `kappa` 为 `O(delta^(2 kappa+2))`；平窗为 `O(delta^2)`，端点余弦窗为 `O(delta^4)`。因此下一开放桥梁严格缩成 edge-localized finite-to-bulk transfer，而非重新估计整个 adjacent arithmetic mass。

- [Archimedean localizer 非构造补全](notes/202-archimedean-localizing-weil-completion.md)：构造两个同维、同范数且前四矩完全相同的 65 维矩阵，一个正定、一个保留 (1/65) 负谱，严格排除 scalar-four-moment completion；同时证明增长 mixed localizers 的 finite-satisfiability compactness 定理。

- [相邻乘积与交替比值 Gram](notes/201-adjacent-product-alternating-ratio-gram.md)：六个 (2+2) words 精确分解为 (4\|Z^2\|_2^2+2\|ZZ^*\|_2^2)，差由换位子能量控制。compact-support path 强制 adjacent 的 (ab\le X)，故真正 (X^2) 障碍只在 alternating/Farey ratio Gram；端点余弦窗把边缘 overlap 从 (O(\ell)) 压到 (O(\ell^3))。

- [Gabor 边界 Schatten 审计](notes/200-gabor-boundary-schatten-gate.md)：无条件证明 zero-side tail 对四次迹为 (o(N))，把 finite-to-bulk 缩成 signed-kernel 的 intrinsic Schatten gate，并给具体 HS 充分目标 (o(L^3/(1+\log L)^2))。秩一反例证明二矩误差不能自动提升。

- [光滑窗四循环与配对对角泛函](notes/199-smooth-window-cyclic-fourth-diagonal.md)：精确推导 finite Gabor 四循环、非交换 word ledger 与任意偶窗的 \(D_{22}(\psi)\)。修正平窗 family 计数；得到 MT 窗 \(D_{22}=0.2445893820\ldots\) 和 remainder 预算 \(0.0829099143\ldots\)。余弦窗扫描显示四矩目标窗可能不同于二矩最优窗；新的硬点是 finite-to-bulk 边界及未配对近共振。

- [四矩二次通道与 Vaughan 接口](notes/198-quadratic-fourth-moment-vaughan-channel.md)：中心四矩精确分解为背景、线性素数项、二次素数项的三通道 PSD Gram；Schur residual 是正确的 response target。素数符号账本分离 2+2、3+1、4+0，并把改善 0.6725007... 的最小任务压成对角之外净预算小于 0.0608832407...。有限无权实验只验证恒等式与相消存在，不作为 zeta 渐近证据。

- [部分 Weil 比例、四矩和非零区域](notes/197-partial-weil-proportions-regions-four-moments.md)：澄清 13/18 是条件性 Christoffel 四矩层级；完整 rank--trace--inertia 账本在同一矩数据下给条件性 16/21 与互异比例 37/42，并给当前二矩纪录的一侧四矩改进阈值。

- [Nonconstructive Brownian response compactness](notes/196-nonconstructive-brownian-response-compactness.md)：统一 finite Sobolev budget经弱紧致性自动补全为 global response distribution；存在性等价于显式 finite Gram/Schur PSD 条件，但 compactness不制造统一算术常数。

- [Response-specific Vaughan--Brownian Gram](notes/195-response-specific-vaughan-brownian-gram.md)：公共 polynomial divided difference把 centered degree-two response精确分成 Type I/II/continuum primitive channels；完整 Brownian energy是其 PSD Gram 的 all-ones quadratic form，普通 Young bound被证明尺度中性。

- [Brownian primitive-energy certificate](notes/194-brownian-primitive-energy-cauchy-certificate.md)：direct Cauchy response由 global constant mode加一个 positive Brownian prefix-square Gram控制；degree-two情形得到单一 nonlinear response energy，而非三个独立 moments。

- [Balanced square / mass-correction no-go](notes/193-balanced-square-mass-correction-no-go.md)：zero-mass core具有 primitive convolution square，但 mass correction只有 O(abs M) 而非 O(abs M/B) 的 absolute bound，且有限审计显示主阶抵消；主对象升级为完整 divided-difference primitive。

- [Cauchy cumulative capacity / centered Volterra](notes/192-cauchy-cumulative-capacity-centered-volterra.md)：Gaussian profile capacities的 Gamma mixture精确塌缩为原 Cauchy signed cumulative capacity；degree-two response在 centered discrepancy primitive上由一个共同五次 Volterra polynomial生成。

- [Vanishing-order tax / signed heat profile](notes/191-vanishing-order-tax-signed-heat-profile.md)：Bernstein transition floor与 coefficient-ledger lower bound排除 high-order zero 加 absolute moments 的组合；Gaussian response改写成 signed cumulative Abel--Volterra profile，并精确落到 balanced multiplicative short intervals。

- [Cauchy--Gaussian mixture / high-order route](notes/190-cauchy-gaussian-mixture-high-order-route.md)：Poisson tail迫使 Fourier cusp，不能直接换 Gaussian trace；Cauchy 的 Gamma--Gaussian 尺度混合把 broad scales交给 repeated-primitive PNT powers，把剩余 near 障碍缩成 multiplicative heat small-ball energy，并以 high-order ideal density给出非构造 vanishing-order amplification。

- [`NCE-1 finite cone`](notes/175-finite-arithmetic-cone-rank-one-separators.md)：finite polar cone、active-set KKT 与 rank-one correspondence separators；
- [`NCE-2 Hodge transgression`](notes/176-threshold-hodge-transgression-commutator.md)：small-spectrum-only no-go、inserted McKean--Singer transgression 与 shell-gradient commutator；
- [`NCE-3 random grids`](notes/177-random-log-grid-fejer-no-free-lunch.md)：random-shift Fejér identity、good-grid selection 与 convex randomization no-gain。
- [`三路线 occupancy 汇合`](notes/178-harmonic-synthesis-occupancy-barrier.md)：external harmonic synthesis capacity为 `Theta(1+Nh)`，排除 profinite diagonal经 universal Bessel直接闭合。
- [`One-sided atomic packets`](notes/179-one-sided-atomic-packet-hodge-criterion.md)：polar distance由 packet negative responses与 nonnegative synthesis coercivity控制；下一目标是 finite SDP capture ratio。
- [`Cell-cone capture / operator-system repair`](notes/180-cell-cone-capture-no-go-operator-system-repair.md)：单 partition的 capture error趋一；改用 one-sided pinching ledger加 off-cell trace-norm remainder。
- [`Packet--complement ledger`](notes/181-modulated-packet-complement-ledger.md)：压缩负谱、补空间负谱与 coupling 的精确拆分；单格复调制受 sharp 余维障碍限制。
- [`Kaplansky arithmetic order-density`](notes/182-kaplansky-arithmetic-order-density.md)：strong-dense 算术平方精确 norm 负谱迹；任何负方向都有 finite-word witness。
- [`Labelled incidence bicommutant`](notes/183-labelled-incidence-bicommutant.md)：threshold fiber 的 length/Dirac generators 无条件生成全部矩阵代数；全局问题缩为 cross-fiber transport 连通性与平方响应递推。
- [`Selberg--Volterra support connectivity`](notes/184-selberg-volterra-support-connectivity.md)：prefix hypergraph 精确控制 cross-fiber components；canonical transport 连通但 condition number 线性退化。
- [`Finite-word moment structure theorem`](notes/185-finite-word-moment-structure-theorem.md)：full-generating finite algebra 上 current positivity 等价于 degree至多 `d^2-1` 的 word-moment matrix PSD。
- [`Degree-one moment blindness`](notes/186-degree-one-moment-blindness-short-word-leverage.md)：bipartite degree-one moments只读取有限 features，存在任意大不可见负谱；高 degree问题等价于 point-effect leverage/capture。
- [`Soft negative effect / Cauchy moments`](notes/187-soft-negative-effect-cauchy-moment-certificate.md)：canonical soft polynomial square以 `2rho` 加逼近误差控制负谱迹，并有无零点输入的 finite lag-resonance 展开。
- [`Formal lag resonance audit`](notes/188-formal-lag-resonance-soft-direction-audit.md)：actual finite prime--continuum symbol上严格拆分 exact/near/far；degree two显示强 signed cancellation但尚未优于 arbitrary barrier。
- [`Parity-breaker exact evacuation`](notes/189-parity-breaker-exact-sector-evacuation.md)：odd exact moments由 lag character消失；even-prime-power breaker经 convolution `L2` 控制，degree-two exact bucket无条件共尾趋零。
