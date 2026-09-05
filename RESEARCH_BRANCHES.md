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
| NCE-8 | 当前主线 | B1w：取 \(Y_m=2^m\)，在首个 \(q\in(Y_m,2Y_m)\) 的 \(q-1,q\) 中按268认证质量下界选cutoff，估计实际 \(J_{4,\le Y_m^2}/\mu_m^4\) | 给该增长频带的一致算术预算，或用实际下界否定所选schedule；不再只改写积分 | 267实际prime-power系数预算及全频乘子no-go [T/N]；268 \(|M|\gg Y^{-\sigma}\log Y\) 与 \(J_{4,>Y^2}=O((\log Y)^{-3}\mu^4)\) [T]；有限增长频带及Schur仍 [O] |
| NCE-9 | 非构造补全 | 把 finite Cauchy-translate Schur block写成 joint signed Type I/II large-sieve form | uniform finite-block budget只用 length-side数据且弱于完整 RH criterion | finite satisfiability compactness与Gram/Schur判据已完成；33 translates捕获约23% package norm |
| MOM-1 | 四矩观察线 | 只在出现新的 actual determinant-correlation input 时恢复；不得继续增加 Möbius/divisor kernel 表示 | 新输入必须在 physical fiber 内先合并全部 divisor blocks，并直接给 `o(L^4)` global ledger | exact band/mass已闭合；cumulative、band energy、channel mass、raw pullback与 divisor separation五条候选证书均已 theorem/no-go；条件比例仍为 0.7569027 / 0.8784513 |
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

## 近期主要路线 A--E（2026-09-04 阶段审计）

本节将当前技术分支压缩为五条主要路线，作为资源分配、晋级与止损的决策入口：A 为近期主线，B 为长期主线，C 为桥梁路线，D 为受限探索，E 为低风险验证路线。

### 路线 A / MOM-1：四阶矩增量（近期主线）

- **目标**：控制中心化四阶矩，严格改进当前约 `0.6725007` 的简单临界线零点比例。
- **当前基础**：零点侧尾项已经隔离；真实 m<=X adjacent family 已渐近对角化，m>X aggregate 已等价归约为 complex-symmetric boundary block 的 pseudocovariance BB^T。one-factor HS energy 为 O(N)；natural-scale covariance 不制造 phase cancellation；自然 lower/upper HS polarization 受 two-edge locality 阻断。首个 lower-boundary prime entry 的 normalized height mean square 又无条件趋于 1/(4 pi^2)，因此 uniform beta_L||B_X(T)||op=o(1) 路线严格失败。alternating ratio clusters 在 von Mangoldt 支撑下已分类：不同素数底 clusters 为 singleton，非中心同素数 chains 整体为 o(N)。恢复 dyadic local energy 后，任意单个 primitive box 在 AB<=XL^(2-epsilon) 均渐近对角化，且 fixed determinant graph 有 degree-two Schur bound；在 primitive 双曲区域 ab<=X 内，fixed aperture 的整条 radial chain 已由 signed Montgomery--Vaughan 压到 O(N/L)，所有 non-seam aperture crosses 绝对可和为 o(N)。其中 +/-L aliases 已由 translated-symbol support gap 与 trace-class remainder 闭合，+/-2L seams 已由双曲 ratio diameter 排空；ordinary pairs 又经 determinant lift 化为 (Lambda*Lambda) harmonic correlation，并由 Evans 的 almost-all E2-shift theorem 无条件闭合。整个 ab<=X primitive hyperbolic family 已 atomic diagonalize；定量化 Evans saving 后又闭合任意 fixed `kappa<1` 的 logarithmic supercritical collar `ab<=X L^kappa`。product/ratio 坐标证明卷积阶仍为 `Lambda*Lambda`，在 `ab asymp X L` transition layer，exact scalar kernel 的 resolution core 为 `|ad-bc| lesssim L`，而整层 atomic diagonal 已是 `O(N log L/L)=o(N)`；discriminant-uniform multiplicative upper-bound sieve 又把整个 fixed-`delta<1` transition resolution core 的 absolute main term压到 `O_delta(N L^{-(1-delta)/2}(log L)^5)=o(N)`。clustered vector-valued Fejér 大筛又把完整 transition aggregate（包括 oscillatory tail）压到 `o(N)`，并与 collar 拼接得到整个 primitive union 在任意 fixed `eta>0` 下对 `ab<=XL^(2-eta)` 的 atomic diagonalization。critical `ab asymp XL^2` 又被精确归约为四变量 factor-bin determinant incidence：elementary baseline 为 `D(H)<<RH L^2`，而任意 fixed `sigma<1` 的 `D(H)<<RH L^sigma(log L)^C` 已足够闭合全部 box ledger；`sigma=1` 仍停在主尺度。balanced critical box 已由二维 Selberg 上界筛与 Bettin--Chandee exact determinant main term 达到 natural scale；进一步以 moderate-aspect Kloosterman 外筛和 extreme-aspect 两线性形式直接筛无条件得到全部 factor boxes 的 `D(H)<<RH(log L)^C`，故 logarithmic-square critical shell 已闭合；笔记 232 证明 `ab>XL^2` 外仍有正主质量。笔记 233 再把 determinant incidence、Fejer ledger 与 finite transfer 一致延伸，闭合任意 `ab<=XL^(3-epsilon)`，同时证明 fixed-log saving 不能进入 `ab asymp X^(1+kappa)` 的幂级高乘积区。笔记 223 又以短高度 Hilbert 值 Montgomery--Vaughan 均值在 relative-dense heights 上闭合 adjacent `m>X` boundary pseudocovariance。笔记 224 进一步用 Henriot discriminant-uniform shifted sieve 闭合 bulk `3+1`，用频率间隙闭合 bulk `4+0`，并把它们与 adjacent defect 合成一次一侧均值选择；已覆盖的 `ab<=XL^(3-epsilon)` alternating primitive support 在同一点 uniform 为 `o(N)`。笔记 225 将每个有限四因子 Toeplitz word 减 bulk 精确分成三个 crossing-Hankel 项，其 scalar trace 只有 `O(log L)`；结合同一 shifted sieve 与短高度核，闭合 finite `3+1,4+0` signed boundary。至此 finite pure-prime 各 signed boundary 机制已闭合，但 fixed-power high-product alternating primitive off-diagonal 仍须补入一侧账本。笔记 226 又把 Gamma/pole-absorption 背景精确化为确定性零频 Toeplitz 主部 `S_L=T_d(phi^2/a-1)` 与算子范数 `O(1/L)` 的余项；Schatten telescoping 使该余项对四迹只有 `O(N/L)=o(N)`。笔记 227 用 `Omega=1,2` 的 discriminant-uniform shifted sieve 排空全部非零 mixed frequencies，并通过先平均完整非负四阶迹、再一次选点修复 good-set 交集缺口。笔记 228 已证明 relative-dense starting heights 足以覆盖 AF moving zero blocks，并把中心二、四矩接入 quartic rank--trace--inertia certificate；形式上得到 simple/distinct 常数 `0.7569027/0.8784513`。该记录级实例仍为 `[C]`；逆向审计已把当前算术缺口缩到 fixed-power high-product 的 actual signed determinant response；polylog cutoff `K<3` 已闭合。

- **A1u 止损 [N/E]**：笔记 241 证明 arbitrarily separated divisor columns仍通过 common multiples共享 exact numerator rows，故 divisor distance与 synthesis positivity不推出 off-block Schur decay。finite actual matrices中 separated signed part在四个尺度均大于最终 response，并与 near blocks反号抵消。式 `sum|C_ij|^2=o(L^6)` 仍是正确充分条件，但不再作为优先输入。
- **A1v 恢复条件 [O]**：只有出现一条新的 determinant/frequency correlation estimate，能在每个 physical fiber 内先保留 `sum_(i,j)C_ij^(q)` 并给 global `o(L^4)`，MOM-1 才恢复。仅改变 divisor partition、取 block absolute values或使用 full operator norm不算进展。
- **A2 状态 [T/C]**：笔记 228 闭合 moving-block zero-counting 量词，并证明当前中心偶矩不能直接调用 13/18 Christoffel 数值；quartic inertia implication 为 [T]，实例化的新比例在完整 prime-side 逆向复核前保持 [C]。
- **晋级条件**：经严格归一化和区间认证得到
  \[
  b_4<0.3275499074,
  \]
  或者严格缩小交替比值通道所需的开放算术输入。
- **止损条件**：若匹配下界证明所选窗口或响应无法达到上述阈值，则停止继续调窗；将结果整理为四阶矩方法极限/no-go 定理，并把研究主力转向路线 B。
- **预期产物**：边界紧性引理、交替比值分块公式、完整四阶矩预算表，以及有理数或区间算术证书。

### 路线 B / NCE-8：Vaughan--Brownian 响应预条件（长期主线）

当前周期为下列 **B1w**；B1u--B1v段落保留为前周期的输入、失败与证据记录，
其中“下一最小引理”“尚无质量下界”等均指当时的固定schedule，不覆盖268的新选择。

- **目标**：利用 Type I、Type II 与 continuum/Gamma 通道之间的真实交叉抵消，证明 square-root Vaughan rectangle 上的统一增益。
- **当前基础**：exact divided-difference response与 Brownian Gram保持成立。笔记 242 发现旧 `U=V=floor(sqrt N)` 实验的 Type II严格为空；修正为 cube-root cutoff后 Type-II非零并与 Type-I强负相关，但三通道 diagonal/full 比依 decomposition改变。cutoff-invariant quantities 是合并 prime vector `u_p`、continuum vector `u_c` 及其 physical energy。
- **最小引理 B1a**：固定一个 response rectangle与非空 Vaughan cutoff，直接从 prime/continuum coefficients证明 `Re<u_p,u_c><=-delta(||u_p||^2+||u_c||^2)`，其中 `delta>0` 与尺度无关。Type-I/II 只作为估计 `u_p` 的内部坐标，不能分别取绝对值。
- **B1s 收束 [T/N]**：260的七扇区双边最优常数 \(3/8,11/16\) 与非平衡扰动界保持成立。261在实际系数上用 Mellin/Landau质量振荡及孤立素数原子证明连续尺度障碍；262将下界扩为 \(J_4(Y,N)\ge c_\sigma Y^{-6}N^{-3}/\log Y\)，同时覆盖全部整数 \(Y\le N\le Y^2/8\)。若 \(N=\lfloor\Phi(Y)\rfloor\)、\(\Phi\) 连续非减且 \(N/(Y\log Y)\to\infty\)，则在 \(\sigma<1/2\) 任何正幂 mass-only连续预算都失败。中心参数的这种预算至少蕴含 RH；未证逆命题。
- **B1t 收束 [T/N]**：263把无条件定量PNT转移为 \(\sup_{N\ge Y}|M|\ll_{\sigma,d}Y^{1-\sigma}e^{-d\sqrt{\log Y}}\)，每个固定 \(d<0.8476836\) 适用。连续源低lag正尾给 \(\mu^2/(t_H+\ell_H)\ll M^2e^{(1-\sigma)H}/Y^{2(1-\sigma)}\)。所以所有 \(H\le k\sqrt{\log Y}\)、固定 \(k<2(0.8476836)/(1-\sigma)\) 的正源绝对相对tail证书都无条件失败；包括259所有固定Q窗口、任意dyadic子序列及任意自由matched cutoff \(N\ge Y\)。这是充分证书的障碍，不是实际signed transfer、mass-only预算或Schur增益的否定。
- **B1u 当前周期（主线一条、辅助两条）**：主线为同一实际schedule的带符号截断：直接估计 \(\|\mathbf P-\mathbf P_H\|/(M^2\sqrt D)\) 并核对 \(|M_H|/|M|\)，禁止先用正源TV替换响应差。辅助一由264证明最优 \(E_2\ge E_1^2/H\)，故局部 \(J_{\rm loc}=O((M_H/S_H)^4)\) 当且仅当 \(E_{2,H}=O(LM_H^4)\)，原二阶输入自动缩为 \(E_{1,H}=O(M_H^2\sqrt{LH})\)。辅助二为固定 \(\sigma=1/4,Y=2^m,N=\lfloor Y\log^2Y\rfloor,\ 3\le m\le18\) 的有界能量/矩复算 [E]；全源数据不得套用局部响应判据。
- **B1u 独立输入与接口**：263障碍只用已发表的Fiori--Kadiri--Swidinsky定量PNT、精确Stieltjes边界项及正源几何；264基础引理只用有限零质量测度、支撑长度、Hermitian自相关与Cauchy。真正未决算术输入为264-(22)的局部 \(E_{2,H}\) 预算、质量匹配及实际signed response差，通过256的capture/Schur归约接入部分Weil配置。没有从紧性或选择原理制造正性；Gamma-complete及上同调桥梁仍独立开放。
- **B1u 当前证据与主要反例**：两份证明独立逆向复核通过所有cutoff量词、最优常数、非零/零质量分支及局部/full归一化。104个有理测度精确检查及1024个独立自相关斜率区间支持恒等式；双端点例取等，9个零一阶矩例仍有非零能量。实际全源 \(E_1/(LM^2)\) 在已算点从约0.387升至4.898，但只能记[E]；不能从有限趋势推出能量逃逸。260固定宽度正源反例、261--262实际连续质量振荡与263正尾下界分别阻止不同的推理，不能混写其量词。
- **相对闭合门槛与止损**：265已得到实际signed截断的绝对改进，但还不能相对full \(M^2\) 控制；仍须同时证明264-(22)的三项。若抽取 \(m_j\)，保留物理频率 \(t=m_j\xi\)。停止重试固定Q正尾证书；只证质量分离、只证二阶预算或只引用fixed-frequency PNT不晋级。262-(14)与266-(11)分别是full/local预算的必要条件，不是充分条件。
- **B1u 循环性审计**：264局部等价判据是已证明的分析归约，但实际能量估计没有随之得到。在局部预算和质量匹配已成立后，signed transfer与full预算由三角不等式互相推出；因此264-(22)是分开的开放输入账本，不能宣称它本身给出此前未知、更弱的算术定理。原256的自由cofinal存在性仍[O]；中心参数连续mass-only预算至少蕴含RH，不得当作软公理。
- **B1u 实际算术推进 [T]**：265保留signed weighted-PNT primitive，证明所有有限 \(N\ge Y\) 一致的 \(\|F_r\|\ll S\sqrt L E\)、\(J_4\ll E^2\)，其中 \(E=e^{-d\sqrt L},d<0.8476836\)。对任意固定 \(k\) 及 \(0\le H\le k\sqrt L\)，实际response差除以 \(S^2\sqrt D\) 至多 \(Ce^{-(1-\sigma)H}E\)，质量截断差至多 \(CSe^{-(1-\sigma)H}E\)。这是独立PNT产生的一份signed saving，不是两份saving；仍没有实际质量下界足以闭合相对预算。
- **B1v 下一最小引理 [O]**：固定队列所列的同一schedule，研究 \(A_4=\|F_{(r-r_H)*(r+r_H)}\|\) 与 \(B_4=\|F_{r_H*r_H}\|\) 的实际联合四阶系数，目标为 \(A_4+e^{-(1-\sigma)H}B_4=O(M^2\sqrt L)\)。265-(21)只对第三正通道取Young，已严格证明此输入充分闭合signed transfer；它不是把六阶full响应误差改名，也不宣称必要或已知弱于RH。优先寻找两份真实discrepancy之间的算术抵消，禁止把其中一个因子取TV后再声称获得了双saving。
- **本轮辅助证据与反例 [T/N/E]**：266给实际 \(E_{1,H}\ge c_\sigma Y^{-2\sigma}L^2\)（\(\log2\le H<L/6\)）及局部预算必要尺度 \(|M_H|\gg Y^{-\sigma}L^{3/4}H^{-1/4}\)。另有光滑严格正源满足更强二阶预算却使 \(E_2/(LM_H^4)\to\infty\)，包括 \(L\to\infty\) 版本；它排除纯二阶闭合，但不是von Mangoldt反例。四个实际局部窗的归一化二阶比不单调，没有触发实际schedule止损。30例Fraction截断恒等式、104例能量回归及独立50位小例均复算通过；全部计算仅[E]。
- **B1w 当前周期主线 [T/O]**：267证明实际prime-power卷积系数 \(B_0\ll Y^{2-4\sigma}L^2,\ B_1\ll Y^{4-4\sigma}L^2\)，常数不依有限cutoff。268在两个相邻cutoff中选择，得到 \(|M|\gg_\sigma Y^{-\sigma}L\)，并独立闭合完整响应的 \(J_{4,>Y^2}=O_\sigma(L^{-3}\mu^4)\)，\(0<\sigma<1/2\)。所以所选schedule的full预算严格归约为增长频带 \(J_{4,\le Y^2}=O(\mu^4)\)，不再把高频相对尾列作假设。
- **B1w 独立输入与Weil接口**：实际素数跳跃、共同端点、Chebyshev规模、prime-power唯一分解、Abel链几何，以及Montgomery--Vaughan加权均值；素数存在只需已核验PNT的定性部分。通过256-C接入条件性prime--continuum capture/Schur，不自动处理Gamma或上同调桥梁。既没有用紧性制造正性，也没有预设full预算。
- **B1w 下一最小引理及晋级条件 [O]**：在268同一可认证选择规则下，证明增长频带内的真实signed prime/continuum联合能量 \(J_{4,\le Y^2}\le C\mu^4\)，或严格缩小其中尚未控制的频率范围。仅用fixed-frequency PNT、变换成大矩阵、换partition或重复已闭合高频公式不晋级。这里规范频率是 \(|t|\le mY^2\)，不是fixed core。
- **B1w 辅助线与当前证据 [T/N/E]**：辅助一为原 \(N=\lfloor YL^2\rfloor\) schedule的有限频带探针，\(m=4,6,8,10\) 数据不推渐近。辅助二为267实际有限源的 \(\|\widehat r\|_\infty\ge B\) no-go，停止全频 \(o(S)\) 乘子路线，但不否定积分response-specific抵消。精确额外碰撞项 \(\mathcal C=O_\sigma(1)\) 在 \(\sigma>1/8\) 成立，不控制近碰撞。44个Fraction纤维恒等式、16个混合链界、48个连续项特殊函数抽样及6个素数跳跃cutoff探针已独立重跑；后两类仍为浮点[E]。
- **B1w 主要反例、循环性与止损**：新 \(N\in\{q-1,q\}\subset[Y,2Y)\) 不属261--262所排除的连续大cutoff类；不表示固定旧schedule或无cutoff源已解决。268的高频输入独立闭合，剩余低/中频预算仍可能具有RH强度，未声称更弱。若实际下界迫使所选 \(J_{4,\le Y^2}/\mu^4\) 无界，则停止此选择规则；不以外生正源或少量数值趋势代替实际反例。
- **论文归属**：261--262已经整理为独立 `abel-mass-obstruction-paper.tex`；263--268暂以Markdown保存，归Vaughan--Brownian response论文后续审计材料。当前轮不重排PDF；每几轮按数学成熟度再同步。不混入广义Weil结构或四矩比例论文；内部证明及复算不等于文献新颖性或外部同行评审已经完成。
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
| A / MOM-1 | 20% | 等待新的 determinant-correlation 输入 |
| B / NCE-8 | 60% | 当前主线 |
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

- [Universal raw Brownian limit 与 discrepancy-tilt reduction](notes/255-universal-raw-brownian-limit-and-discrepancy-tilt-reduction.md)：用 even centered source 的 minimum-of-two 恒等式证明 `D_raw~(logY)(A^2+B^2)/2~(logY)B^2` [T]；再证明 normalized frequency `t=mxi` 下 raw energy probability弱收敛到 universal density `(1-cos(tlog2))^2/(pi log2 t^2)` [T]，其 total mass解析上恰为 `1`。actual degree-two response probability精确等于该 raw measure 的 `q_kappa(mu,Delta)^2` tilt [T]。构造同一 raw probability上两个 locally vanishing bounded tilts，一个保持 tight、一个全部逃逸，证明 raw tightness加 local multiplier extinction逻辑上不足 [N]。18-component positive core 的 raw limit mass约 `0.1817399` [E]，其中第一 component约占 `0.1816044`；下一输入缩成 normalized actual tilt 的 global tail。
- [Quartic discrepancy capture 与 conditional Schur gain](notes/256-quartic-discrepancy-capture-and-conditional-schur-gain.md)：由 positive sources 得到全频率可行域 `|mu|<=1,|Delta|<=2`，并证明 explicit global envelope `|q_kappa|<=56(mu^2+Delta^2)` [T]；与 local positive quadratic jet 合成 actual capture 对 positive quartic energy 的一侧归约 [T]。把剩余输入具体化为 `J_4=int Delta^4dnu<=C_4mu^4` [O]；若成立，则任意 positive-mass nonresonant continuity core 都有 explicit actual capture 与 sign-pure uniform Schur gain [C]。该输入展开为 sources 的六阶非负 Brownian integral，不涉及零点定义，但其强度尚未判定。
- [Source-realizable mesoscopic tilt escape 与 triple-convolution ledger](notes/257-source-realizable-mesoscopic-tilt-escape.md)：证明 `S^4D_rawJ_4=||F_(r*r*p)||_2^2+||F_(r*r*c)||_2^2` 及两个 primitive-convolution upper bounds [T]。随后构造 lag 为 `L_m` 与 `L_m+sqrt(L_m)` 的 explicit positive sources：它们具有同一 universal raw limit并在所有 fixed physical windows上一致 matching，但 mesoscopic band `xi~m^(-1/2)` 给 `J_4>=c/m`、`J_4/mu^4>=cm^3`，且 actual `q_kappa^2` probability逃离每个 fixed normalized core [N]。这把 B1p 唯一化为 von Mangoldt-specific mesoscopic triple-convolution estimate；不反驳真实 zeta tightness。
- [Von Mangoldt triple convolution 与 logarithmic lag confinement](notes/258-von-mangoldt-triple-convolution-and-logarithmic-lag-confinement.md)：以 centered atom `k_lambda` 精确展开 actual `r*r*p,r*r*c` 的全部 triple coefficients和 six-lag Brownian kernel，并证明 centered discrepancy primitive等于 weighted PNT tail [T]。只用 `Lambda<=log`、exponential Abel cutoff与 continuum bulk lower，得到 source lag 的 lower exponential/upper superexponential envelope；继而把两个 discrepancy factors以任意 polynomial normalized-amplitude accuracy截到宽 `O(loglogY)` 的 lag window [T]。这严格排除 257 的 `sqrt(logY)` packet，却不提供 relative denominator；B1q 缩为 central window 内的 von Mangoldt signed Gram。
- [Carrier--collision decomposition 与 quantitative quartic decay](notes/259-carrier-collision-decomposition-and-quantitative-quartic-decay.md)：把全部六个 lag variables 截到 \(O(\log\log Y)\) central window 后，将 27-state Brownian kernel精确拆成 unequal-carrier finite-rank main与 equal-carrier collision [T]；carrier masses 为 \((1/8,-3/4,15/8,-5/2,15/8,-3/4,1/8)\)，主常数为 \(63/16\)。由 collision 的 absolute \(O(\log\log Y)\) ceiling 无条件推出 \(J_4=O(\mu^4+\log\log Y/\log Y)=o(1)\) [T]；但这仍弱于 mass-relative \(O(\mu^4)\)。B1r 唯一研究七个显式 short-interval collision sectors的 signed cancellation或 matching lower/no-go。
- [七扇区 sharp coercivity 与平衡 discrepancy 归约](notes/260-sharp-carrier-coercivity-and-balanced-discrepancy-reduction.md)：精确展开七个 carrier测度；质量平衡时各sector能量非负，六阶响应与四阶 discrepancy卷积能量双边等价，常数 \(3/8,11/16\) 均最优 [T]。对非平衡源给二阶/四阶能量的显式稳定性归约 [T]；固定宽正源例排除普遍 mass-only预算 [N]。独立审计修正259的全源推论：绝对任意幂次tail界必须补充相对 \(\mu^2\) 响应误差。B1s只继续实际算术能量比较。

- [Balanced-core multiplier degeneracy 与 energy reweighting obstruction](notes/254-balanced-core-multiplier-degeneracy-and-energy-reweighting.md)：把 actual degree-two divided difference与 response scalar按 `S=A+B` 完全无量纲化，得到 exact normal form `gamma Q=-(4alpha^2/9)q_kappa(mu,Delta)` [T]。其 quadratic jet 为 positive definite `kappa^2(Delta^2-3muDelta+3mu^2)`；在 `|mu|+|Delta|<=10^-3` 上显式证明 `0.09589(mu^2+Delta^2)<=q<=2.905(mu^2+Delta^2)` [T/N]。matched PNT core 上 `mu,Delta->0`，故 actual multiplier一致趋零，response/raw energy density ratio按 `(mu^2+Delta^2)^2` 消失；同一 PNT argument更证明每个 fixed physical-frequency window 上 multiplier都一致消失 [T/N]。这严格阻止把 B1i 的 finite `Q` lower 或 B1k 的 ratio core直接 cofinalize；尚未证明 normalized total capture趋零，下一输入必须在 `T_m->infinity` 的增长频带给 discrepancy-weighted denominator lower。

- [Matched-endpoint PNT transfer 与 Schur ratio closure](notes/253-matched-endpoint-pnt-transfer-and-schur-ratio-closure.md)：在 `Y_m=2^m,N_m>=Y_m,L_m=logN_m,xi=t/m` 下，以 exact Stieltjes identity 和 qualitative PNT `psi=x+o(x)` 证明任意 fixed nonresonant compact `K` 上 `sup_K |P-C|/C->0` [T]，不需 PNT rate 或 cutoff-ratio upper。于是 prime/continuum ratio一致趋于 `1`，scalar Schur factor一致趋于 `1/2` [T]。又证明 18-component finite common core 可删除任意小的 resonant 邻域，同时保留两个尺度各 `>1/20` 的 certified lower [T]。ratio leg 已闭合；下一输入严格缩为 actual response-energy tight capture，或其 energy-escape obstruction。

- [Stieltjes transfer 与 fixed-lag cofinal obstruction](notes/252-stieltjes-transfer-and-fixed-lag-cofinal-obstruction.md)：以 `x=e^lambda` 精确证明 `P_(Y,N)-C^J_(Y,L)=R_(psi-x)+int_(e^L)^N F+Q_J` [T]，把 arithmetic discrepancy、endpoint mismatch 与 quadrature error 完全分账。由无条件 PNT [R] 证明：若 `Y_m=2^m,N_m>=Y_m` 而 continuum second lag moment有界，则任一固定非零 normalized phase的 prime/continuum ratio逃逸 [T/N]；若某 fixed 正长度 interval 保留统一 ratio upper，则 `M_(2,m)>=c m^2Y_m^(1-sigma)`，标准 continuum 因而必须满足 `liminf L_m/logY_m>=1` [T/N]。这排除 fixed `L=2` 的 cofinalization。

- [Exact dyadic phase common core 与 cofinal gate](notes/251-exact-dyadic-phase-common-core-and-cofinal-gate.md)：利用 `8=2^3,16=2^4` 把 `theta=xi log Y` 精确化为 `t=3xi,4xi`，无需 transcendental endpoint近似；两个 frozen whole-cell ledgers的整数网格交给 5,931 个 base cells、18 个 connected components、总 normalized width `29.655` [T]。parent pointwise lowers按 `1/3,1/4` exact splitting后，common core分别捕获 scale 8 的 `>0.0532943571` 与 scale 16 的 `>0.1132755926` diagonal，故两个 finite physical responses共享 `-z>D/85`、diagonal/full `>85/83` [T]。其 cofinal schedule 与 scalar `dpsi-dx` transfer 已由笔记 252--253 闭合；剩余缺口是 actual response-energy capture [O]。

- [第二尺度 directed overlap 与 uniformity gap](notes/250-second-scale-directed-overlap-and-uniformity-gap.md)：对预注册 `(Y,N,J,h)=(16,15,4,1/200)`，以 rational canonical atom ordering、production binary64逐系数 replay、TV transfer及全部 51,199 个 frequency cells 的 outward certificate证明 `D_upper=0.001025620093083457466797381202`、`N_lower=0.000163944504546660552689839988` 与 `N_lower/D_upper>0.159849154333328712>3/20` [T]；推出 fixed physical overlap `-z>(3/85)(P+C)`、diagonal/full `>85/79` [T]。第二尺度 raw band fraction上升而 rigorous capture下降，uniformity gap缩到归一化共同 core及 density lower [O]。

- [Directed trigonometric numerator 与 finite overlap 证书](notes/249-directed-trigonometric-numerator-and-finite-overlap-certificate.md)：以 Machin `pi` enclosure、degree-44 cosine Taylor remainder和 `10^-60` outward fixed-point arithmetic逐一审计 `1<=i<51200` 的全部 frequency cells [T]。12,785 个 positive cells通过 whole-cell ratio/Lipschitz判定，给 `N_lower=0.000140734590642330727559468708` 及 `N_lower/D_upper>=0.191234900905432370>0.19` [T]；结合 ratio factor `4/17` 推出该 fixed physical direction满足 `-z>(19/425)(P+C)`、diagonal/full `>425/387` [T]。scale-uniform overlap仍为 [O]，下一最小引理为第二尺度 B1h。

- [Rational base coefficients 与 intended Brownian 分母证书](notes/248-rational-base-coefficients-and-intended-denominator-certificate.md)：以 rational log/exp/square-root intervals与全局 `|f''''|<45` 的 eight-panel Simpson remainder认证七个 prime-power weights及五个 continuum masses [T]；base symbol TV error至多 `7.154150754635959633323008e-6`，经 quartic Banach ledger、production binary64 pruning/roundoff replay、再次居中残差与 Brownian TV transfer，得到固定 `(8,10,4)` intended diagonal `D_upper=0.000735925241553713216150037691` [T]。当时的浮点 numerator anchor为 [E]；笔记 249 已以 directed intervals闭合 ratio certificate [T]，当前进入第二尺度 B1h。

- [Exact lag quotient、cluster-safe Brownian 分母与 TV 稳定性](notes/247-exact-lag-quotient-and-brownian-denominator-stability.md)：由 Hermite--Lindemann [R] 证明 algebraic grid上的 formal lag可先精确商到 `(rational ratio, algebraic shift)`，并用正项 `atanh` 级数给 logarithmic positions有理 enclosure [T]；证明 position intervals重叠时仍成立的 cluster-hull primitive energy upper及 centered-measure TV transfer `E(mu)<=(1+tau)D_tilde+(1+tau^(-1))L epsilon^2` [T]。固定 `(8,10,4)` surrogate response从 `35103/33977` formal atoms压到 `22855/21425` canonical atoms，96项有理余项给 logarithmic positions 的最小间隙下界 `0.00004834486675790251`，对 surrogate 的 exact rational diagonal upper为 `0.00070419548392646702` [T]。B1f、B1g 已分别由笔记 248、249 闭合；当前最小引理为第二尺度 B1h。

- [Lipschitz good-cell 收敛定理与 coefficient rationalization gate](notes/246-lipschitz-good-cell-convergence-and-rationalization-gate.md)：由 finite atom first moments给出 `W_p,W_c,d-hat,Q(d-hat)` 的 global Lipschitz constants，并证明 midpoint enclosure验证的 good-cell lower sums在 mesh趋零时恢复全部 strict-good spectral energy [T]。真实 double-precision zeta audit中，mesh `0.01->0.005` 使宽 `[1/4,4]` band的 conservative lower/exact diagonal由 `0.0988->0.1999`（scale 8）、`0.0252->0.1645`（scale 16），而 raw band mass稳定 [E]；说明主要损失来自证书分辨率而非当前 finite spectral escape。笔记 247--249 已闭合第一尺度的 denominator、intended coefficients与 directed numerator [T]；当前进入第二尺度 B1h。

- [Scalarized response spectrum、宽 ratio band 与 one-sided arc certificate](notes/245-scalarized-response-spectrum-and-one-sided-arc-certificate.md)：证明 degree-two common divided difference在每个 Fourier character上精确等于 scalar polynomial `Q_(M,l)(d-hat)`，从而无需展开四次 formal convolution [T]；并给 total-variation 高频尾界。真实 finite 数据中 scalarized integral重构 exact Brownian diagonal/cross达 `98%--99.5%`，宽 `[1/4,4]` ratio band对 exact diagonal捕获 `0.51--0.70`，但 ratio 1附近窄 band可降至 `0.0065` [E]。严格 supremum tail却为 exact energy的 `37--41` 倍，故改用 finite good arcs的一侧 lower certificate：任意已验证 good arcs携带 `kappa(P+C)` 即直接给 uniform overlap，无需估计其余频谱 [T]。下一最小引理 B1d 是实现带 coefficient误差账本的 interval good-arc certificate。

- [Symmetric Fourier 符号定理与 spectral-overlap gap 障碍](notes/244-symmetric-fourier-sign-and-spectral-overlap-no-go.md)：对任意非负 even measures `a,b`、exact centered opposite components和任意 common complex multiplier，Fourier--Plancherel给 `P=int W_p^2domega`、`C=int W_c^2domega`、`z=-int W_pW_cdomega<=0` 与 `E=int(W_p-W_c)^2domega` [T]。因此 finite zeta sign-pure prime/continuum physical cross的非正性不再只是数值现象。另一方面，显式 alternating multiplier族满足 `P_N=N-1/2,C_N=1,z_N=-1`，故 normalized gain `1/(N+1/2)->0` [N]：evenness、符号和 common response仍不给 uniform B1a。下一最小引理 B1c 是证明 actual response energy有固定比例落在 `m<=W_p/W_c<=M` 的 spectral ratio band。

- [Common-convolution 符号障碍与 physical cross-variation 分解](notes/243-common-convolution-sign-obstruction-and-cross-variation.md)：证明 Brownian primitive 与 common translation convolution交换，并证明非负 multiplier保持 opposite primitive cones [T]；但给出零质量整数 atomic multiplier，使 base pointwise cross非正、内积为 `-1`，卷积后整体内积翻为 `+2` [N]。真实 zeta finite audit逐点验证 base positive cross为零，而 degree-two response产生 `3%--9%` 的正 cross variation；signed总量仍负且 cross visibility约 `0.30--0.39` [E]。因此 base atom signs不足以证明 B1a；下一最小引理 B1b 是对 actual multiplier证明 `P_+<=theta P_-`、`theta<1`，随后独立证明 cross visibility。

- [Vaughan cutoff vacuity、physical quotient invariance 与 continuum Schur](notes/242-vaughan-cutoff-vacuity-and-physical-schur.md)：证明 exact Type-II support下界为 `(U+1)(V+1)`，所以旧 simultaneous square-root cutoff在 `n<=N` 上严格 vacuous [T]，撤销笔记 195 旧表的 Type-I/II evidence解释。common divided-difference response的线性性给 `u_I+u_II=u_p`，故 physical prime/continuum二通道 Gram与 cutoff无关；三通道 diagonal可由 split gauge任意放大 [T/N]。对 physical vector作 continuum Schur completion，把能量精确分成 shorted residual与 actual-coefficient mismatch，并证明只控其中一项不足 [T/N]。cube-root cutoff重算得到非零 Type-II、`rho_(I,II)=-0.91...-0.94`，总体负 cross仍主要来自 prime--continuum [E]。下一引理改为 cutoff-invariant uniform negative physical correlation。

- [Divisor-scale separation no-go 与 physical-fiber-first 原则](notes/241-divisor-scale-separation-no-go.md)：对任意 `r,s` 与 prime power `p>V`，取 `a=lcm(r,s)p`，则 Vaughan synthesis columns `T_r,T_s` 在同一 numerator row 上均至少含 `Lambda(p)`；以该 row 的 positive rank-one form得到不随 divisor distance衰减的 cross response [T/N]。对每个 actual determinant/frequency fiber，全部 dyadic blocks先求和精确恢复 `Lambda^*B_qLambda` [T]，而 decomposition-preserving gauge可令 blockwise absolute Gram budget二次发散 [N]。finite centered data中 separated block平方能量占 `9%--44%`，其 signed part在所有尺度都大于最终 response并与 near blocks反号抵消 [E]。因此 A1u 远块路线停止，234--241 周期结束；主力切换到 NCE-8 actual Vaughan--Brownian physical Gram。

- [Möbius pullback、相邻 divisor columns 与带符号 dyadic dispersion](notes/240-mobius-pullback-adjacent-divisor-dispersion.md)：定义 exact Vaughan synthesis `T_(a,r)=sum_(v>V,rvw=a)Lambda(v)`，证明 `Tmu=Lambda` 与 centered divisor kernel 的 pullback factorization `K=T^*B^cent T` [T]；所以 quotient 后出现 Möbius 坐标本身只是 original prime response 的精确重写。二维 Abel 把 actual direction精确变成 Mertens weights作用于 adjacent columns `U_r=T_r-T_(r+1)`；divisibility jump反例排除把这些 columns 当 smooth family [N]。dyadic vectors `Z_i` 等于 truncated Möbius synthesis加两个显式 endpoint columns，且 `sum|Z_i^*B^cent Z_j|^2=o(L^6)` 足以闭合 fixed cell [T/C]。finite audit逐项验证全部恒等式；entrywise Abel absolute retention从 `1.65e-2` 降至 `5.51e-4`，dyadic blocking改善约一数量级但仍有增长损失 [E]。下一最小输入缩成 separated dyadic blocks 的带符号 response mean-square。

- [Vaughan quotient-first centering 与 Möbius divisor response kernel](notes/239-vaughan-quotient-first-centering-and-divisor-kernel.md)：在 high cell 中把 one-factor channels精确写成 `P_U(a)=sum_(r<=U,v>V,rvw=a)mu(r)Lambda(v)` 与 `Q_U` 的互补范围，并给三个 Gram entries 的完整 divisor-range determinant sums。physical quotient使 response entries重构 original response、mass entries重构严格正 original mass，故 leading raw mass不可能靠 channel labels代数消失 [N]。linear shell centering与 quotient交换，而 exact band shell cancellation加 elementary incidence已把共同 constant-density main term压到 `O(L)` [T]；逐 channel absolute budgets受 ghost gauge影响。finite audit中 `X=3200,kappa=1/4` 的 response/entry-l1为0.0169而 mass/entry-l1为0.8646，仅记 [E]。下一输入缩成共同 centered kernel上 actual `mu tensor mu` direction的 bilinear estimate。

- [Band-energy Bessel 障碍与 exact physical-response Gram](notes/238-band-energy-bessel-no-go-and-physical-gram.md)：对 positive in-band density `1+epsilon cos(3pi t)`，exact finite all-ones Gabor response 为 `epsilon/2+O(1/M+M^2/Q)`，但 centered discrete band energy至少为 `epsilon sqrt(M/160)`，严格排除 ordinary band Bessel necessity。six-window overlap进一步实现为同/跨 cell Hilbert Gram；固定 off-support extension并只分解 numerator factor得到 exact `2 x 2` Vaughan quotient，但必须保留 `I=-II` composite ghost atoms。命题 238-H证明 ghost gauge可令 full Gram norm任意大而 physical vector不变。三 cutoff finite audit在 `kappa=1/4` 时出现0.0169--1的 physical/entry-l1比但不单调，仅记 [E]；下一引理缩成三个 explicit divisor-range determinant sums的 leading main-term cancellation。

- [累计差异并非带响应的必要输入：慢调制障碍](notes/237-cumulative-discrepancy-band-no-go.md)：构造正密度 `1+epsilon cos(2pi t/sqrt(M))`、`M=n^2`。其 constant reference 精确为 1，累计差异恰为 `epsilon sqrt(M)/(2pi)`；但 shifted consecutive-band Abel 求和给 exact finite Gabor response `O(M^(-1))`。在 `theta=3/4,M=X^(1/2)` 尺度上，cumulative gate 远大于 `L^4` 而实际 band response 已为 `o(L^4)`。这严格排除把笔记 235-H 的充分 certificate 当成必要或唯一输入；笔记 238 又排除 full band energy necessity，下一引理现为 actual physical-response Type-I--II factorization。

- [幂级高乘积 dyadic mass ledger 的初等闭合](notes/236-elementary-power-high-mass-ledger-closure.md)：对任意 fixed balanced exponent `1/2<theta<1`，置 `Y=X^theta,H=Y^2/X,M=max(H,Y/H)`。固定前三变量并对第四变量作 interval count，单用 `Lambda<=L` 与 Chebyshev 得 large-shift incidence `D_Y(S)<<Y^2SL`（`S>=Y`）；因此 exact dyadic bridge 的 central 与全部 shell mass-over-radius² 项总计 `O((H/M)L)<=O(L)=o(L^4)`。特别在 `theta=3/4` 取 `M=X^(1/2)` 后，唯一剩余输入是 cumulative discrepancies 的绝对 `o(L^4)` 总预算。
- [幂级高乘积 dyadic mass ledger 的初等闭合](notes/236-elementary-power-high-mass-ledger-closure.md)：对任意 fixed balanced exponent `1/2<theta<1`，置 `Y=X^theta,H=Y^2/X,M=max(H,Y/H)`。固定前三变量并对第四变量作 interval count，单用 `Lambda<=L` 与 Chebyshev 得 large-shift incidence `D_Y(S)<<Y^2SL`（`S>=Y`）；因此 exact dyadic bridge 的 central 与全部 shell mass-over-radius² 项总计 `O((H/M)L)<=O(L)=o(L^4)`。在 `theta=3/4` 取 `M=X^(1/2)` 后，cumulative discrepancies 的绝对 `o(L^4)` 总预算仍是一条充分旁路，但笔记 237 已证明它不是必要输入。

- [Exact finite dyadic band discrepancy 与幂级高乘积的 `L^4` 门槛](notes/235-exact-dyadic-band-discrepancy-and-L4-gate.md)：直接对 finite consecutive-Gabor kernel证明 pre-alias `1/t` envelope、dyadic bounded variation 与 constant-density shell cancellation；由 Stieltjes 分部积分把完整 fixed-power response 控制为 central discrepancy、dyadic shell discrepancies及显式 mass/edge 项。结合 `beta_L^4 D asymp X/L^3` 与 `N=XL`，得到全 box raw response 必须且由该桥梁充分压到 `o(L^4)`；严格排除仅证明 relative `o(B)` 的路线。实际 `theta=3/4` flat-window prime-power 数据中 `E log M/B` 从约 `0.0897` 降至 `0.0105`，但仅记为 `[E]`。

- [幂级高乘积 Gabor 带通核与 core--tail 分割障碍](notes/234-power-high-gabor-bandpass-and-core-tail-no-go.md)：在自然变量 `t=X log(ad/bc)` 中把 exact consecutive-Gabor response 写成离散频带 `[1,2]`，并证明极限核 `K(t)=sinc(pi t)cos(3pi t)` 的 Fourier support 为 `[1,2] union [-2,-1]`。其全质量为零但 coherent core `|t|<=1` 的质量为严格正常数 `0.023558003094...`，tail 精确补偿；因此 core-only lower-bound 止损判据严格失败。进一步把实际四-von-Mangoldt、six-window Gram 写成正 determinant measure 的 band Fourier coefficient，并给出一阶 cumulative-discrepancy 足以产生 signed saving 的定量桥梁。

- [Aperture--depth 坐标、三次对数 collar 与幂级高乘积障碍](notes/233-aperture-depth-third-log-collar-and-power-high-no-go.md)：精确参数化 `log(ab)/L=2-2delta-|q|`，证明 fixed-aperture high support 嵌套于 low support，并找到 genuine-prime determinant-2 near collisions。对笔记 222 的 proof 作 endpoint audit 后，将 natural incidence 一致推广到 fixed polylog bands，并由 Fejer/finite ledger无条件闭合任意 `ab<=XL^K,K<3`。同时证明任何 fixed-log incidence saving 都不能通过 positive local-energy schema进入幂级 high-product 区；下一输入唯一化为 actual signed determinant response 的 power saving或 lower bound。

- [Alternating 高乘积尾的支撑障碍与全局 atom ledger 修正](notes/232-alternating-high-product-support-obstruction.md)：全局 half-open atom ledger 证明 subcritical、transition、critical 之后还存在第四块 `ab>XL^2`。exact support depth 等于 `L(1-max(r,s))`，故 logarithmic-square cutoff 不是 physical support；平窗中该尾贡献 alternating 对角的精确 `5/8`，MT 窗数值约 `56.88%`。因此笔记 222 的 critical incidence theorem 保持成立，但“完整 primitive closure”降级；下一输入已由笔记 233 缩成 fixed-power high-product 的 signed response，而非继续增加 log savings。

- [Alternating 中心块交叉缺口与短高度修复](notes/231-alternating-central-primitive-cross-repair.md)：逆向分拆完整 ratio Gram 后发现，笔记 209 明列开放的 `rho=1` central block 与 primitive hard core 交叉项并未被笔记 222/225 的旧拼接覆盖；分别控制两块范数只给 `O(N)`，并有二维 Hilbert 反例。利用中心 carrier phase 精确消失、finite response 的 `d beta^4` trace bound 及已审计 shifted prime-pair 上界，证明该交叉在每个 `X/sqrt(log X)` 短区间的 signed mean 为 `O(X sqrt(log X)(log log X)^2)=o(N)`，从而修复 central--noncentral component。笔记 232 随后发现 `ab>XL^2` primitive 内部漏区，记录级实例继续为 [C]。
- [中心四迹常数的十二路径独立重建](notes/230-cyclic-fourth-constant-reconstruction.md)：不调用预合并公式，枚举六个 `2+2` sign words 与每个 word 的两种 pairing，十二条累计路径严格分类为 `A_+,A_-,B` 各四条；背景 mixed placements 独立给出 adjacent/alternating orientations `8/4`。逐 raw path 三角分块积分重算 MT 的 `D22=0.244589382034`、`D0+Dmix+D22=0.252508968714`，未发现 orientation 或 normalization 错误。下一步转向内部 Fejer/box/frozen-grid 拼装。

- [四阶素数侧外部输入逆审计](notes/229-external-input-reverse-audit.md)：对照 Bettin--Chandee Corollary 1 验证 `Y^(39/20)` error、exact gcd density 与单序列 `n=ac` Selberg 展开，确认 remainder cost 是 `D^(39/10)` 而非误读的四-divisor cost；再按 Henriot 2014 勘误把 `rho-hat` 改为 `rho-check` 并记录 leading coefficient factor。对 `X,X+h` 的 primitive monic specialization，上界及 `z_j->0` 统一常数保持有效。
- [相对稠密高度到 AF moving zero block 的量词桥梁](notes/228-relative-dense-zero-block-transfer.md)：从原文 grid `alpha_k=u+2pi k/L` 重建长度 `T+O(1/L)` 的移动零点块；证明起点位移 `T/sqrt(log T)` 只改变 `o(N)` 个零点，故每个短区间一个 good height 足以传回固定 dyadic 与累计计数。中心二、四矩可直接进入 quartic inertia certificate，给条件常数 `0.7569026657/0.8784513329`；同时以两组同偶中心矩、不同三阶矩的显式谱测度证明当前数据不能代入 13/18 Christoffel 数值。记录级结论待 prime-side 全链逆向复核。

- [确定性背景 mixed-frequency evacuation 与非循环共同高度选择](notes/227-deterministic-background-mixed-frequency-closure.md)：证明 Lambda 与 Lambda*Lambda、Lambda 与 Lambda 的 discriminant-uniform shifted upper bounds；将含确定性 Toeplitz 背景的全部 one/two/three-prime 非零频率在 X/sqrt(log X) 高度窗上压到 o(N)。通过先平均整个非负 centered fourth trace、再选点并用 Schatten 三角控制 pure-prime norm，修复多个 good sets 未必相交的循环缺口。得到 MT centered fourth constant 0.2525089687；zero-counting 量词已由笔记 228 闭合，记录级实例待 prime-side 全链逆向复核。

- [Archimedean 背景的零频 Toeplitz 主部与四迹稳定归约](notes/226-archimedean-zero-frequency-background-reduction.md)：由显式公式、Stirling local flatness、正高度 Gabor localization 与临界 Plancherel，证明背景矩阵等于 `a^(-1)T_d(phi^2)` 加算子范数 `O(1/L)` 的 Hermitian 余项；结合已证 `tr P^4=O(N)`，该余项对完整第四迹只贡献 `O(N/L)=o(N)`。同时提取 zero-prime 与 balanced two-prime deterministic window functionals；MT 窗候选四矩为 `0.2525089687...`；非零 mixed frequencies 已由笔记 227 闭合，当前待办是记录级 prime-side 全链复核。

- [四因子 Toeplitz telescoping 与 pure-prime finite signed boundary 闭合](notes/225-fourfold-toeplitz-signed-boundary-closure.md)：证明任意四个有限 Toeplitz factors 与单一 bulk symbol 的差精确为三个 crossing-Hankel 项，并以 nuclear crossing inequality 将每个实际 scalar trace 一致压到 `O(1+log L)`，没有 `d asymp XL` 损失。结合笔记 224 的 shifted `E3` 算术输入，得到 finite `3+1,4+0` boundary 的 signed first means 为 `o(N)`，从而在每个 `X/sqrt(log X)` interval 内闭合完整 finite pure-prime `P^4` 一侧账本。另以单频反例证明把 absolute value 放入高度积分是严格更强且不必要的目标；下一输入只剩 Gamma/continuum mixed words 与最终正规化。
- [Shifted E3 sieve 与纯素数四阶词的共同短高度闭合](notes/224-shifted-e3-short-height-pure-prime-closure.md)：以 Henriot 的 discriminant-uniform shifted multiplicative upper bound 得到 `Lambda` 与三重 von Mangoldt 卷积在所有短 shifts 上的 `Delta(h)` 加权上界；由 bounded-mean discriminant factor 闭合 `3+1` 的 signed first mean，并用固定频率间隙闭合 `4+0`。把二者按真实系数与 adjacent 非负 defect 先相加，只选择一次高度，得到每个长度 `X/sqrt(log X)` interval 内的 pure-prime bulk 一侧 `o(N)` 结论；不声称各 signed word 逐点小。下一输入只剩 finite-to-bulk signed boundary 与 Gamma/continuum mixed words。
- [短高度 Hilbert--Montgomery--Vaughan 闭合 adjacent boundary](notes/223-short-height-hilbert-mv-adjacent-closure.md)：冻结 cutoff 与 Gabor 维数后，把 actual `m>X` product clusters 写成 Hilbert--Schmidt 值 Dirichlet 多项式。由 direct-sum 边界能量与 dimension-free Montgomery--Vaughan 均值，每个长度 `X/sqrt(log X)=o(X)` 的 interval 都含有 adjacent aggregate 为 `o(N)` 的高度；这沿 relative-dense heights 同时闭合 `BB^T` pseudocovariance，且不与单 entry 正均方 no-go 冲突。下一输入是其余四矩通道的共同高度非负账本。
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
