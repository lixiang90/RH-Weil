# 研究分支看板

本文件记录尚未进入正式论文的探索路线。严格推导见 [`notes/174-nonconstructive-existence-and-branch-map.md`](notes/174-nonconstructive-existence-and-branch-map.md)。

## 当前队列

维护验收与恢复（2026-09-06）：David--Lapidus观察线、论文目录及GitHub Actions三项维护均已完成，[完整三组远程检查成功](https://github.com/lixiang90/RH-Weil/actions/runs/33982592142)。291--295四轮周期与纯PNT包络路线已收束。296--301的亚纯接口四轮周期也已收束：300给出真实全谱RH条件临界渐近；301证明近碰撞相位抵消及同解析germ的边界预算非一致性。**停止扩写固定候选的RH等价日程，不自动外推增长谱包或L函数族**。下一准入任务限一轮回查289-(53)的实际带符号相关输入与参数匹配；没有独立新输入或实质削减则继续保留观察，不能靠重写表示重启同类周期。`DL-AUDIT`未启动，资源门槛不变。

| ID | 角色 | 下一最小引理 | 晋级条件 | 状态 |
|---|---|---|---|---|
| NCE-1 | 主线 | finite SDP 的 cell-packet capture ratio、coercivity 与实际负响应 | capture remainder一致消失，one-sided packet budget可和 | one-sided atomic theorem 已完成 |
| NCE-2 | 概念线 | fiberwise harmonic scalars 的 external synthesis correspondence | 给出跨 `q` fibers 且限制 rank-one amplification 的 arithmetic map | canonical fiber 内交换子为零 |
| NCE-3 | 工具线 | random cells 是否降低 arithmetic-specific packet response | 保留 joint cancellation并优于 `Theta(1+Nh)` universal capacity | universal random-grid route 已到 sharp no-go |
| NCE-4 | 备用线 | moment positivity 与 determinant visibility 的 dilation lemma | 前提只含有限算术 moments | 观察 |
| NCE-5 | 备用线 | one-prime/one-block extension，预算增量可和 | extension 不调用完整 Weil positivity | 观察 |
| NCE-6 | 备用线 | bounded-resolvent/negative-trace 的 ultraproduct 稳定性 | 先独立得到统一预算 `C` | 观察 |
| NCE-7 | 非构造主线 | short-word effects 对实际 negative level sets 的 response-weighted capture | capture error共尾可和且不调用 Selberg/RH 等价输入 | degree-one universal moment route 已 sharp no-go |
| NCE-8 | 主线周期已收束；实际输入准入审计 | 限一轮回查289-(53)，固定A=1,a=1/4：是否有可核验的实际带符号相关估计覆盖剩余四阶预算及全部参数；先匹配范围，不换核扩写 | 得到新的独立算术输入、严格缩小剩余预算或定位具体适用障碍；否则保留观察 | 301已[T/N]闭合300-(50)，并给同germ两族相反边界行为；300真实ζ条件结果保留，禁止无簇控制的一致外推 |
| NCE-9 | 非构造补全 | 把 finite Cauchy-translate Schur block写成 joint signed Type I/II large-sieve form | uniform finite-block budget只用 length-side数据且弱于完整 RH criterion | finite satisfiability compactness与Gram/Schur判据已完成；33 translates捕获约23% package norm |
| MOM-1 | 四矩观察线 | 只在出现新的 actual determinant-correlation input 时恢复；不得继续增加 Möbius/divisor kernel 表示 | 新输入必须在 physical fiber 内先合并全部 divisor blocks，并直接给 `o(L^4)` global ledger | exact band/mass已闭合；cumulative、band energy、channel mass、raw pullback与 divisor separation五条候选证书均已 theorem/no-go；条件比例仍为 0.7569027 / 0.8784513 |
| NCE-10 | 非构造补全 | 增长的 arithmetic mixed localizers 与 divisor-visible resolvent closure | 每个有限 word level 近正且 Archimedean 有界，闭包恢复 divisor | scalar fourth moments 有 65 维严格 no-go；finite-satisfiability completion 已证明 |
| OBS-1 | 文献线 | canonical Hamiltonian 的局部质量一致界与 noncollapse | 从 Euler/Gamma 方程而非 zeros 证明 | 文献审计 |
| OBS-2 | 系统线 | tracial negative-square realization theorem | 与 Cauchy Hodge index 精确对应 | 文献审计 |
| DL-AUDIT | 限额结构审计 / 模型验证观察线 | 选定一个 David--Lapidus Weierstrass 模型，独立复核一条几何极化正性与 Frobenius 相容性命题及其谱识别依赖 | 一个非循环、可独立复核的模型命题，或严格定位通向算术 zeta 的缺失输入 | [R/O] 仅登记，未启动；最多一个 4--6 轮试审周期、资源不超过 10%，不替换 B 主线 |
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

当前周期为下列 **B1z**；B1u--B1y段落保留为前周期的输入、失败与证据记录，
其中“下一最小引理”“尚无质量下界”等均指当时状态。
273已闭合B1x的(G)，274闭合统一高频尾；275重新选择记录包络共尾序列，
进一步闭合增长低频，未解决剩余中频联合响应。新序列的性质不回填给271原程序。

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
- **B1w 本周期反向推进 [T/N]**：269在 \(0<\sigma<1\)、所有有限 \(N\ge Y\) 上证明同一中尺度带 \(I=[K_\sigma Y,2K_\sigma Y]\) 的实际响应至少为 \(c_\sigma L/Y^3\)，并得到 \(J_4/\mu^4\gg Y^{1-4\sigma}L/M^4\)。它使用保留0频率质量项的局部间距均值、真实prime bulk、BV连续端点及全cutoff lag矩，不把任意Bessel上界当作物理saving。268的非零质量保证比必要尺度低 \(Y^{1/4}/L^{3/4}\) 因子，但没有所选质量的同阶上界，故尚未否定该dyadic选择。
- **B1w 本周期两条辅助线**：辅助一由270保留signed Abel尾的 \(h^ae^{-h-d\sqrt L}\)，在261零点前提下将连续非减cutoff障碍推进到 \(h\ge(3/\kappa)L-b\sqrt L,\ 0\le b<0.8476836\)，删除cutoff上限；\(\sigma<1/2\) 无条件，中心参数预算仅蕴含RH。四次情形覆盖 \(N=\lfloor cY\log Y\rfloor,\ c\ge3/4\)，不声称边界最优。辅助二计算268所选源的full有限频带，旧冻结schedule探针本轮仅保留为历史记录。
- **B1w 当前证据与审计**：269/270两份独立只读证明审计均通过，修补了非零质量分支及零点前提的显式措辞。新增actual full脚本独立计算Brownian分母，\(m=4,6,8,10,12\)、\(T=128\) 的 \(J_{4,\le T}/\mu^4\) 为约0.697、1.601、6.742、27.816、24429.067；这些数值不推渐近无界。主代理重跑通过，30个连续项抽样及50位最小完整积分复核；全部仍[E]。
- **B1w 下一最小引理与止损纪律**：在同一268选择上，先判断 \(M^4/(Y^{1-4\sigma}L)\) 是否有一致正下界，或存在趋零的非零质量子序列；后者由269严格停止该schedule。前者只是必要检查，不能据此宣布full预算成立；要继续晋级仍须实际prime/continuum交叉控制或更强的响应下界。连续cutoff根序列和有限m的大比值都不能替代dyadic算术结论；不得继续扩写已闭合高频或普通乘子框架。
- **论文归属**：261--262及269--270已同步独立 `papers/abel-mass-obstruction-paper.tex` 与 `output/pdf/abel-mass-obstruction-paper.pdf`（10页），第7--8节给新增完整证明；263--268仍以Markdown为主，归Vaughan--Brownian response后续材料。该次论文同步按PDF技能完成两次编译和逐页渲染核验，无最终溢出或引用警告；2026-09-06仅迁移目录，不重新排版。不混入广义Weil结构或四矩比例论文；内部证明及复算不等于文献新颖性或外部同行评审已经完成。
- **B1x 本周期主线 [T/R]**：271证明正单调Stieltjes变换的双边振幅界，并以单位区间漂移把实cutoff振幅转移到整数最大质量。Littlewood经典无条件振荡与dyadic望远镜独立保证无穷多个窗口的 \(Z_m\gg_\sigma Y^{1/2-\sigma}\ell(Y)\)。认证严格阈值、对窗口交错搜索给可计算共尾序列 \(|M|>Y^{1/2-\sigma}\sqrt\ell\)。不保证每个dyadic成功，也不保证268首素数规则。
- **B1x 已缩小输入 [T/O]**：272结合267的实际prime-power高频界，在该新序列上证明 \(J_{4,>T_0}=O(\mu^4)\)，\(T_0=Y\sqrt L/\ell(Y)\)，因此full预算等价于 \(J_{4,\le T_0}=O(\mu^4)\)。更大频带 \(T_1=Y\sqrt{L/\ell}\) 之外是 \(O(\ell^{-1}\mu^4)\)。这里 \(\ell(Y)=\max(1,\log\log\log Y)\)，固定 \(0<\sigma<1/2\)。不是原首素数schedule的同序列改进。
- **B1x 独立算术输入与Weil接口**：Littlewood振荡 [R]、Stieltjes分部积分、dyadic几何求和、实际素数幂与267的加权均值；非构造/交错搜索不制造质量或正性。通过256-C仍仅条件性接入prime--continuum capture/Schur；Gamma、完整显式公式及上同调桥梁独立开放。没有预设响应正性或RH级负指数预算。
- **B1x 原下一最小引理 [原O，现273的T/R]**：对实际聚合乘积系数 \(b_k=\sum_{uv=k}a_ua_v\)，令 \(\delta_k\) 为不同乘积的最近log间距，原目标为 \(\mathcal G=\sum b_k^2/\delta_k\ll Y^{4-4\sigma}L\)，一致于 \(N\in[Y,2Y]\)。272-B证明一个对数saving足以使 \(J_{4,>Y}=o(\mu^4)\)；273现已证明更强的 \(\log(2L)\) 界，见B1y。
- **B1x 两条辅助线及当前证据**：辅助一为有限实际最大质量和逆最近间距实验；271的八个窗口 \(m=4,6,8,10,12,16,18,20\) 已50位抽查及主代理复算，全部尚未达到理论筛选阈值，不能称已找到共尾算法输出。辅助二为振荡文献量词审计：已核查的Schlage-Puchta及Révész结果给幂长区间，未直接提供每个dyadic窗口的结论；不声称穷尽文献。
- **B1x 复现与逆向复核**：两份独立只读审计通过271全部证明和272归一化、四项尾预算、cofinal量词、256接口及(G)条件性。主代理重跑两份新脚本：八个最大质量窗口及八个最近间距实例；后者两个独立MP50小例的最大相对差约 \(1.61\cdot10^{-16}\)。全部数值仅[E]；已修正“单个有限点可证伪未知常数渐近O界”的不当措辞。
- **B1x 主要反例与循环性**：271光滑分离bump反例证明全局 \(\Omega_\pm\) 本身不能推出每窗口下界；不是实际prime反例。269必要质量条件在新选择上被超过，但不推出联合response上界；270连续大cutoff障碍也未覆盖此序列。剩余频带预算可能仍有RH强度，尚未证明更弱；本篇特定选择不穷尽原自由存在性。
- **B1x 晋级与止损条件**：只有独立证明(G)、进一步缩小频带或给真实响应新上/下界才晋级。若(G)失败，停止此充分证书，不直接否定actual交叉抵消；若实际响应迫使本篇所选 \(J_{4,\le T_0}/\mu^4\) 无界，则停止该schedule。不得把八个有限窗口或平均支持稀疏度升为统一渐近结论。
- **B1x 论文归属与维护**：271--272归Vaughan--Brownian response，先保存完整Markdown证明和复现脚本，降低PDF同步频率。下一次更新障碍论文时补显式“大实数Y”到旧 `lem:uniformmoments`、`lem:signedtail`；对应269--270笔记已有限定。新颖性、有效高度与外部同行复核仍[O]。

- **B1y 本周期主线晋级 [T/R]**：273在固定 \(0<\sigma<1/2\)、全部有限 \(N\in[Y,2Y]\) 上证明 \(\mathcal G\ll_\sigma Y^{4-4\sigma}W,\ W=\log(2L)\)。小product与远邻先局部化；proper-power自身及对pure最近邻的污染总共 \(O(Y^{7/2-4\sigma}L^2)\)；纯prime近碰撞由BC固定行列式公式、单序列Selberg上界筛和保留product权的相容箱求和闭合。
- **B1y 独立算术输入**：BC正式论文Corollary 1 [R]、Chebyshev、267真实prime-power链与271的Littlewood共尾质量。273独立重建有限筛极小值、系数界、精确密度及正幂筛级别，未假定四素数相关渐近。两份独立内部审计通过；旧221共同主量显式去除 \(b=d\)，其旧遗漏低阶误差不影响最终上界。
- **B1y 实际响应缩频 [T]**：274在271同一序列 \(|M|>Y^{1/2-\sigma}\sqrt\ell\) 上证明 \(J_{4,>T_*}\ll_\sigma\ell^{-2}\mu^4=o(\mu^4)\)，\(T_*=Y\sqrt{W/L}=o(Y)\)。full预算等价于 \(J_{4,\le T_*}=O(\mu^4)\)。这是相对272的同序列改进，不覆盖268每dyadic首素数规则，也不是固定规范频带。
- **B1y 下一最小引理 [O]**：先估计274-(14)，即同一序列的 \((2\pi)^{-1}\int_{1\le|\xi|\le T_*}|\Re F-\Re C-M|^4\,d\xi/\xi^2\ll_\sigma M^4L\)。这是该中频实际响应的充分证书而非必要条件；\(|\xi|<1\) 的质量相对预算仍单独开放。不得由fixed-frequency PNT或仅正质量保证补出它。
- **B1y 两条辅助线与证据 [E]**：辅助一转向有限cutoff实际低/中频响应，保持全部交叉项；辅助二核验外部定理与归一化。本轮局部化脚本已主代理复算十例 \(Y=16,\ldots,4096\)，检查完整/纯支撑、异常自身、污染增量及邻接计数；两个最小例独立试除与MP50/Fraction复核通过。数值未认证271共尾选点，也未计算full \(J_4\)，不推渐近。
- **B1y 主要反例、循环性与Weil接口**：平均稀疏支撑可由相邻整数对反例击破；269中尺度必要下界与新相对尾相容，但不给低频上界。已完成部分只用独立无条件算术；剩余预算可能仍含RH强度，选择和紧性均未制造它。仍仅通过256-C条件性接入prime--continuum capture/Schur，Gamma、完整显式公式、上同调及两者桥梁独立[O]。
- **B1y 晋级与止损**：现在停止重复优化已够用的最近间距充分证书。只有证明274-(14)、真正response中的新抵消或更强下界才晋级；充分证书失败只停止该证书，真实响应若迫使所选schedule的比值无界才停止该schedule。不以外生反例、少量数值或增长的等价约束族代替新算术。
- **B1y 论文归属与未完成项**：273--274归独立Vaughan--Brownian response论文，先存完整Markdown和复现计算，不与Weil结构、四矩比例或连续cutoff障碍强行合篇。新颖性、有效常数/高度、一般L模型适用及外部同行评审仍[O]；本轮不更新PDF，后续集中同步。
- **B1z 本周期主线晋级 [T/R]**：275固定 \(0<\sigma<\beta<1/2\)，以历史记录 \(P_\beta(N)=\max_{n\le N}|R(n)|/n^\beta\) 构造新的可认证共尾序列，同时有 \(|M|>Y^{1/2-\sigma}\sqrt\ell\) 与 \(P_\beta(N)N^{\beta-\sigma}\ll_{\sigma,\beta}|M|\)。记录点保留 Littlewood 强振幅，cutoff不越过记录点；Stieltjes路径因而满足 \(\|H\|_1\ll|M|,\ \|H\|_2^2\ll M^2\)。精确端点及卷积估计给 \(J_{4,\le T}/\mu^4\ll1+T^2/L\)，无条件闭合 \(T=\sqrt L\)，低频只声称 O 而非 o。
- **B1z 独立算术输入与 Weil 接口**：Littlewood 无条件振荡 [R]、271正单调Stieltjes振幅、有限整数记录、严格不等式的交错认证；274统一高频定理和268真实正通道分母继续适用。选择不制造正性，275的全历史条件已由实际算术证明，不是任意新增公理。仍仅通过256-C条件性接入prime--continuum capture/Schur；Gamma、完整显式公式、上同调及其桥梁独立开放。
- **B1z 下一最小引理 [O，279缩小]**：沿275-B同一新序列，先固定 \(\sigma=1/4,\beta=3/8,h>2\)，估计279-(24)的 \(Q_{\sqrt L<|\xi|\le L}(r_l)\ll M^4L\)，其中只保留 \(K<n\le N,\ K=\lfloor N/L^h\rfloor\) 与匹配连续尾部。279已把早段联合差异压成相对little-oh，不能再将它当作未知误差。完整剩余仍为275-(30)的 \(\sqrt L<|\xi|\ll T_*\)；最高固定倍数壳已由274覆盖，只闭合此第一子区间不升级为全频带。277保证中频无通道预算同样必要；280的有限零点换表示不能自动证明它。
- **B1z 两条辅助线及证据 [E/T/N]**：辅助一是实际历史路径的有限复算，五个 \(Y=16,64,256,1024,4096\) 及50位独立最小例通过，全部仍未达到理论质量阈值。辅助二276保留真实素数正对角和连续负交叉，证明 \(V_Y(h)\gg hY^{1-2\sigma}L\) 对 \(0<h\le c_\sigma L/Y\) 一致成立；在 \(h=1/T_*\) 处排除任何固定对数损失的 \(V_Y(h)\ll M^2h^2L^A\)。不新增其他研究线。
- **B1z 主要反例与循环性审计**：275正源运输反例排除“端点大质量/窗口最大性自动控制全历史”，不是实际Lambda反例。276实际单误差障碍不否定双误差卷积；其独立Mellin重建又证明一个固定比例的全尺度平方根二阶矩输入已蕴含RH，不能暗作软假设。稀疏共尾条件与全尺度条件严格区分，未声称剩余中频输入已知弱于RH。
- **B1z 晋级、止损及论文归属**：只有进一步闭合非空增长频段、获得真实双误差saving或响应下界才晋级；停止单误差Lipschitz与只重写恒等式的路线。充分证书失败仅停止证书，实际响应强迫新序列比值无界才停止该序列。275--276先保留完整Markdown及一份可选SciPy复算脚本，归独立Vaughan--Brownian response材料；不更新PDF。内部独立审计通过，外部复核、新颖性、有效高度与论文级晋级仍[O]。DL-AUDIT仍未启动。
- **B1z 本轮结构审计 [T/N]**：277以连续 Abel 密度的单峰BV和保留的中心质量 \(+B\)，证明固定频率阈值以上 \(|\widehat p|^2+|\widehat c|^2\asymp S^2\)。所以275新序列的完整预算等价于 \(Q_{\mathbb R}=O(M^4L)\)，亦等价于 \(\|(G*G)'\|_2^2=O(M^4L)\)，这里 \(G\) 为真实累计误差的奇延拓。等价改写本身不算算术saving；其作用是严证第三正通道不能隐藏剩余中频。
- **B1z 固定全局模型障碍 [N]**：278构造同一 \(\lambda(n)\in[1/2,3/2]\)，沿 \(Y_j=2^{2^j},N_j=2Y_j\) 保留全局 \(R_\lambda=O(\sqrt x\,\ell)\)、\(\Omega_\pm\)、大质量、275指定严格guard及指数历史包络，却在固定宽度的 \(|\xi|\asymp L_j\) 带上有 \(J_{4,I_j}/\mu_j^4\asymp L_j\to\infty\)。同时同源双误差增量至少为 \(h_*^2M_j^4L_j^2\)，只排除 \(A<2\) 的对数损失，不排除任意 \(A\)。这是正整数替代源的真实响应反例，不是实际素数幂源，更未排除同模型另选cutoff成功。
- **B1z 本轮独立输入、辅助证据与止损**：277仅新增连续通道的解析比较；278为完全显式、所有尺度一致的光滑拼接和整数离散化，无外部未证假设。辅助一：四个实际窗口、三个频壳及MP50独立小例复算，均未达到理论质量阈值，只[E]。辅助二：定量guard、旧块误差、Fourier相位平均和自由选择量词的独立逆向审计。现在停止仅重复已由278满足的大小/正性/一致性条件来闭合中频，也停止把第三通道当额外saving来源；保留真正两份误差的素数算术任务。277--278属独立response论文材料，先存Markdown；Gamma和Weil桥梁、新颖性与外部论文审查仍[O]。
- **B1z 本轮实际算术晋级 [T]**：[279](notes/279-record-controlled-arithmetic-prefix-deletion.md)由已证历史包络得到 \(Q_{\le T}(r_e)\ll M^4(K/N)^{4\delta}(L+T^2)\)，\(\delta=\beta-\sigma\)；同时核对实际 \(M_l/M,S_l/S,D_l/D\to1\) 与连续尾部通道强制性。多对数频带 \(T=L^A,K=\lfloor N/L^h\rfloor\) 的阈值为 \(h\ge(2A-1)/(4\delta)\)，严格大于给little-oh；幂级 \(K=\lfloor Y^\kappa\rfloor,T=Y^\theta\) 在 \(\theta\le2\delta(1-\kappa)\)（包括等号）已给little-oh。只控制前缀，不证明尾部预算。
- **B1z 本轮独立算术输入与Weil接口**：279使用275独立振荡与历史记录、实际Chebyshev、匹配Stieltjes端点及正连续bulk；相对误差不是RH等价输入。仍仅经256-C接入prime--continuum capture/Schur，Gamma及上同调桥梁另列[O]。[280](notes/280-finite-zero-interface-and-fixed-mode-audit.md)的有限高度公式使用Kedlaya9.9已核验余项，保留全部实际 \(\Re\rho\)；\(V=\sqrt YL^{A+2}\) 与物理 \(T=L^A\) 不混淆，换表示不算新saving。
- **B1z 本轮辅助证据与反例审计 [T/E]**：280证明固定有限、共轭封闭且 \(\Re\rho\le1/2\) 的所选模式有 \(Q=O(Y^{2-4\sigma}L)=o(M^4L)\)，不扩展至增长集合。12个实际配置与MP50固定模板复算均通过、均未达到275质量门槛，仅[E]；有限中频首零点形状不能升级为渐近主导，较大比值也须检查小质量分母。278坏块位于 \(x\asymp Y\)，前缀删除不消除它，所以一般正源自动闭合路线仍被排除。
- **B1z 本轮晋级、止损与论文归属**：真正新增的是279已证的实际相对前缀误差；下一轮须有尾部实际估计、新反例或进一步误差削减，只扩展280等价表示就停止该动作。“多数尺度好”与275稀疏记录集的交叉选择必须另证；硬截断不能冒用完整Gamma指数衰减。279--280先存独立response论文Markdown材料与可选复算脚本，暂不更新PDF；内部独立审计不代替外部同行评审或新颖性证明。DL-AUDIT仍未启动。
- **算术边界**：不得用任意系数 Bessel 界替代实际响应估计；必须保留交叉项，并单独控制 continuum 和 Gamma 通道。
- **B1z 第四轮量词障碍 [T/N]**：[281](notes/281-all-cutoff-chirp-obstruction.md)取单一光滑误差 \(\mathcal R(x)=\sqrt x\,\ell(x)[3/4+\cos((\log x)^2/2)]\) 并固定离散化。它在所有充分大实 \(Y\)、所有整数 \(N\in[Y,2Y]\) 上均有 \(M\asymp Y^{1/2-\sigma}\ell>0\)、275指定严格guard及历史路径范数，却在 \(I=[L-2,L-1]\) 上满足 \(J_{4,I}/\mu^4\asymp L\)。因此仅凭已列软条件，连自由跳过尺度的共尾选择也不能保证成功；这次不再只是一条可跳过的坏序列。
- **B1z 主要反例的解析适用边界**：同一281模型的系数Dirichlet级数满足 \(\mathcal D_\lambda(1/2+q)\sim3\log\log(1/q)/(8q)\)，所以在 \(1/2\) 附近不可能亚纯。实际 \(-\zeta'/\zeta\) 的已知非循环解析性质已经排除此模型；不能因此把模型叫作Euler/函数方程反例，更不能说亚纯性已经产生实际中频上界。下一估计须说明怎样定量使用这个或其他真实算术区别。
- **B1z RH条件基准与循环性 [T/C]**：[282](notes/282-rh-conditional-endpoint-preserving-response-bound.md)在普通积分内使用显式公式并保留原端点 \(w_Y(N)R(N)\)。单位高度计数与积分后的 \(1/\rho\) 及BV衰减使零点和绝对可和；在明确假设 \(\Re\rho\le\vartheta\) 下得 \(|\widehat r|\ll|M|+Y^{\vartheta-\sigma}\log^2(2+|\xi|)\)。RH时同一275序列有 \(Q_{\ge1}\ll M^4\)、\(J_{4,\ge1}\ll\mu^4/L\) 及full \(J_4\ll\mu^4\)。仅[C]，不能倒用作RH证明；一般 \(\vartheta>1/2\) 仍有未被质量阈值吸收的振幅。
- **B1z 四轮决策、证据与论文归属**：275--282结束一个四轮周期。晋级的是新记录/低频、实际前缀删除以及全选择障碍；停止软范数与自由选择自动闭合路线。279尾部实际预算保持[O]，下一轮只在能具体使用真实亚纯性、有符号有限高度相关或素数乘法结构时推进，不重复等价换表示。实际早/晚段12配置与MP50端点复算通过但全部未达理论门槛，均[E]。完整证明经内部独立复核，材料归独立response论文；外部审查、新颖性、Gamma与Weil桥梁仍[O]。本轮不更新PDF，不启动DL-AUDIT。
- **B1z 新周期第1轮：实际解析输入 [T/R]**：[283](notes/283-fixed-cutoff-abel-mass-oscillation.md)精确计算固定比例 Abel 质量的 Mellin 乘子 \(\gamma(s,c)\)，独立证明 \(c\le1,\Re s>0\) 无零，并重建带留数幅值的 Landau 双向振荡。RH分支用端点保留的 \(A_\sigma(Y)=e^{-1}Y^{-\sigma}R(Y)+O(Y^{1/2-\sigma})\) 与 Littlewood；非RH分支用未被消去的离线零点极点。两种分支无条件给 \(A_\sigma(Y)=\Omega_\pm(Y^{1/2-\sigma}\ell(Y))\)，整数化不跨原子。此处具体使用真实 zeta 的已知解析结构，不是继续假设模型正性。
- **B1z 新周期联合记录与接口 [T/R]**：[284](notes/284-causal-abel-inverse-and-diagonal-record-selection.md)证明 \(F_\beta(z)=(z+\beta)\gamma(z+\beta-\sigma,1)\) 在所需半平面无零，并用减去首项后的可积 Bromwich 反演构造因果指数可积逆核。于是历史 \(R(n)/n^\beta\) 受过去 \(n^{-(\beta-\sigma)}A_\sigma(n)\) 控制；取后者的整数绝对值记录，得到 \(Y=N\)、\(|M|\gg Y^{1/2-\sigma}\ell\) 与新固定 guard。仅存在性，不称275算法、dyadic序列、双符号记录或已实现认证高度。
- **B1z 新周期实际误差削减 [T]**：将新 \(M^4\gg Y^{2-4\sigma}\ell^4\) 接入274-A的全部实Y统一算术高频定理，得到 \(T_{\rm diag}=Y\sqrt{\log(2L)/L}/\ell^2\) 外 \(J_4=O(\mu^4)\)；阈值再乘任意固定正幂 \(\ell^\varepsilon\) 则为 \(o(\mu^4)\)。完整预算等价于 \(\sqrt L<|\xi|\le T_{\rm diag}\) 的实际裸四阶预算，仍[O]。279前缀证明单独核对后适用于新guard，首带 \(T=L\) 的一般门槛是 \(h>1/(4(\beta-\sigma))\)，指定参数才是 \(h>2\)。
- **B1z 本轮独立输入、反例与循环性**：独立算术输入为无条件 Littlewood、zeta亚纯性/函数方程、标准显式公式和273--274真实乘积预算；因果逆本身只用权核分析，不产生振荡或正性。281仍排除仅历史包络/正源自动中频闭合；其最终正的对角质量不符合283的实际双向结论，但这不说明双向振荡足以闭合四阶。完整Weil与Gamma接口仍需256之外的独立输入，RH分支不从条件性命题单独倒推。
- **B1z 本轮辅助与证据**：主线限于实际固定cutoff解析结构，辅助一为因果逆/量词逆向审计，辅助二为一份有限复算脚本；未启动其它路线。全整数扫描 \(2\le N\le2^{18}\) 得正/负75,494/186,649样本、2,736相邻反号对，非连续根证书；九点直接复算差小于 \(5.20\cdot10^{-11}\)，有限Mellin恒等式MP50差小于 \(3.65\cdot10^{-42}\)，全部[E]。283由主代理与carrier_audit独立复核，284由主代理、gap_exception_audit、midband_compute独立复核；新高频/前缀推论另审通过。
- **B1z 新周期决策与止损**：联合记录桥梁和更小高频上端晋级为内部[T]，不再重复扩写因果逆表示；下一最小输入固定为284-(45)，成功后仍须处理 \(L<|\xi|\le T_{\rm diag}\)。若不能给真实交叉节省或严格缩小输入，则停止单纯改选record/改写零点和。283--284归独立Vaughan--Brownian response材料，先存Markdown与脚本，不更新PDF；论文新颖性、外部复核、有效高度及Goal阶段验收均未完成。
- **B1z 新周期第2轮：实际谱块删除 [T/R]**：[285](notes/285-shallow-zero-deletion-and-finite-deep-response.md)在284同一记录上，固定 \(A>1/2,0<a<3/8\)，删去全部 \(\Re\rho\le1/2+a\log L/L\) 的无限积分后零点和、\(|\Im\rho|>\sqrt YL^{3(A+1)/4}\) 的尾及已保留的真实端点。在 \(\sqrt L<|\xi|\le L^A\) 上，误差的 \(Q/(M^4L)=O(\ell^{-4})\)，四次方根相对误差 \(O(\ell^{-1})\)。原p/c/S/D保持，279前缀按一般 \(h>(2A-1)/(4(\beta-\sigma))\) 接回。实际未证输入缩为有限深右有符号和，不只是重写无限显式公式。
- **B1z 第2轮最右实部基准 [C]**：[286-A](notes/286-attained-spectral-edge-and-response-nonidentification.md)若实际 \(\Theta=\sup\Re\rho<1\) 且某零点达到它，单零点Landau幅值经归一化record转移给 \(|M|\gg Y^{\Theta-\sigma}\) 与同一guard；282一般实部估计于是闭合full \(J_4=O(\mu^4)\)。\(\Theta>1/2\) 情形亦成立，但仅条件性诊断，不是实际离线反例；未达到sup及\(\Theta=1\)仍未覆盖。
- **B1z 第2轮严格模型障碍 [T/N]**：286-B构造固定正整数源 \(\lambda(n)=1+F(n)-F(n-1)\in[1/2,3/2]\)，其 \(\mathcal D_\lambda\) 有留数 \(1,-1,-1\)，对应 \(Z=\exp\sum\lambda(n)n^{-s}/\log n\) 有非负Dirichlet系数、单值亚纯延拓和两个简单离线零点。完整格点误差以小频 \(q^2\)、中频 \(q\)、高频TV三段给 \(Q_E\ll Y^{3(1-\sigma)}\)，不是只计算连续模板。对 \(\theta>(3+\sigma)/4\)，强record上full预算成立；非共振参数另有dyadic好子序列。故正源+亚纯性+整数留数+此共尾预算不足以普遍识别中心线。
- **B1z 第2轮独立输入、边界与循环性**：285仅用284已证强记录、标准单位高度计数/显式公式及统一BV；主代理再次核验Kedlaya原书稿。286实际结论只[C]；模型[N]不具备已证的标准素数Euler乘积、完成函数方程、Gamma或Weil正性，不转移为RH反例。256原定理只承诺two-channel capture/Schur，不能把其缺失桥梁描述成自动成立；新实际整数序列也不未经审计回填其dyadic定义。
- **B1z 第2轮证据、辅助线与停止条件**：主线为实际中频删除；辅助一审计最右谱边界，辅助二检验一个固定亚纯模型。285、286经主代理及两份独立代理交叉复核；模型三窗口完整p/c与MP50复算通过，最大求积差 \(1.24\cdot10^{-10}\)，仅[E]。下一最小输入固定为285-(35)的 \(A=1,a=1/4\) 实际相关估计；不得因零点集合变有限就宣布已知弱于RH，也不得把普通计数替代 \(Y^{\Re\rho}\) 或实际signed交叉。停止声称mass归一化预算本身普遍识别中心线；若后续只有换表示则不再晋级。材料归独立response论文与其模型障碍节，本轮不更新PDF，新颖性、外部审查及Goal阶段验收仍未完成。
- **晋级条件**：解析证明有限实验中的增益不会随尺度消失，并将其转化为第二矩、负迹或截断 Weil 二次型的严格改善。
- **止损条件**：若尺度中性的下界迫使 Schur 因子趋于 `1`，或者 continuum 项必然抵消全部收益，则停止该参数族，不再增加新的核表示。
- **预期产物**：可独立陈述的 response Gram 定理，以及它对部分 Weil 比例或平方根共振楔的定量影响。

#### B1z 第3轮：独立密度输入的实际谱压缩（2026-09-06）

- **主线与最小引理**：287估计 \(\sum_{\Re\rho\ge1/2,\ |\Im\rho|>V}Y^{\Re\rho-\sigma}/|\Im\rho|^2\)，保留真实实部权重，而非只把响应换成有限零点和。辅助线限于288的有限Euler正性障碍；轻量脚本只做模型复算。
- **独立算术输入**：[R] Chourasiya--Simonič arXiv:2507.15184v2 的 Corollary 1/Table 1，全实部范围常数已核验；加上282积分后显式公式与284强记录。无RH假设、无紧性制造正性。
- **已证削减 [T/R]**：对 \(A>1/2\)，同一物理带 \(\sqrt L<|\xi|\le L^A\) 可把285高度改为 \(V=Y^{1/4}L^{(7+3A)/8}\)。高谱尾的质量相对四阶能量为 \(O(\ell^{-4})\)，连同已证浅层和端点删除，归一化四次方根误差为 \(O(\ell^{-1})\)。求和覆盖全部更高 dyadic 壳，物理频率与零点高度严格区分。
- **配置接口与循环性**：沿同一284实际记录，只替换待估计的频率函数，原 \(p,c,S,D,M\) 不变；277两通道预算转移仍适用。得到的是已知零密度的响应后果，不是新零密度定理，也不是已证明首带预算，更不覆盖全部 \(\sqrt L<|\xi|\le T_{\rm diag}\)。Gamma/完整Weil桥梁独立开放。
- **主要反例 [N]**：288证明有限Euler多项式若新增右半平面零点，必在同一素数的无穷多个幂次出现负对数导数系数。其显式模型虽有完成FE、素数幂支持与正Dirichlet系数，仍不满足正算术源；不能与286模型拼合成具备全部条件的反例。有限幂次非负检查也不足以替代全幂次公理。障碍不外推至有理因子、一般无限Euler乘积或真实RH。
- **当前证据**：主代理复核原文v2表格、全高度dyadic账本与物理归一化；独立代理交叉审计287/288。脚本用有理数核验两套独立递推至64阶；MP60完成FE样本误差 \(6.38\cdot10^{-62}\)，仅[E]。目录检查、11项目录回归及77项注册/模拟分发检查通过，未重跑77项重型计算。
- **下一最小输入 [O]**：固定 \(A=1,a=1/4\)，控制 \(\Re\rho>1/2+\log L/(4L)\)、\(|\Im\rho|\le Y^{1/4}L^{5/4}\) 内实际带符号和的四阶预算；优先检测中等谱高度的真实交叉，不用绝对计数顶替。已知估计尚不能把保留集合只缩到物理共振高度 \(|\Im\rho|\asymp L\)。
- **晋级/止损/论文归属**：本轮因真实谱尾有幂次削减而晋级；下轮仅在严格减少开放输入、证明交叉saving或明确相应障碍时继续。停止单纯改写有限表示及扩写同类有限Euler例子。287归独立response论文，288为配套结构边界；本轮不更新PDF，DL-AUDIT未启动，文献新颖性、外部审查及Goal阶段验收仍未完成。

#### B1z 第4轮与周期收束：增长阶局部化及联合模型障碍（2026-09-06）

- **主线与已解最小引理 [T]**：[289](notes/289-growing-resolvent-jets-and-polylog-spectral-localization.md)固定 \(A>1/2,0<a<3/8\)，取 \(m=\lceil L\rceil,h=mL^A,V=4h\)。对原积分核作 \(m\) 次移位分部积分，全部谱的端点系数先求和，以284实际历史记录控制；统一 Cauchy jet 界、稳定因果 primitive 和 \((h-\sigma)^{-j}\) 账本防止增长次数带来隐藏指数损失。在 \(\sqrt L<|\xi|\le L^A\) 上，全部浅层、全部 \(|\gamma|>V\) 新余项及完整端点误差满足 \(Q/(M^4L)=O(\ell^{-4})\)。首带保留高度成为 \(4\lceil L\rceil L\)，不是旧 \(I_\rho\) 的硬截断。
- **独立算术输入与配置接口 [T/R/O]**：仅用284已证实际共尾强记录、标准显式公式及单位高度 \(O(\log T)\) 计数；本步不再依赖287密度估计。先固定参数再令显式公式高度趋于无穷，随后证明对增长 \(m,h\) 一致的界。原物理 \(p,c,S,D,M\) 保持，277将裸预算转成原两通道加权预算；四次方根误差为 \(O(\ell^{-1})\)，不冒充能量的加性误差。上同调正极化、完整Weil current及Gamma不能从此自动产生。
- **辅助一：明确范围的联合反例 [T/N]**：[290](notes/290-positive-euler-duality-model-and-mass-moment-nonidentification.md)取固定 \(q\ge5\)，\(Z(t)=(1-qt+qt^2)/((1-t)(1-qt))\)。证明所有闭点数为正整数、Euler乘积真收敛，外代数/对偶/代数HL/超迹/行列式/FE严格相容，而分子仍有离线根。用它自己的离散极点背景，还对所有cutoff、所有正概率频率权证明全部质量相对偶矩界，并证明任意合法共同乘子的统一Schur增益。模型不是实际有限类型曲线、数域连续背景或Riemann zeta反例；缺失相容正极化。078已含companion失纯性，不将该组成机制再登记为新颖成果。
- **辅助二：既有桥梁的停止点 [T/N/O]**：回查194/195的条件response-to-negative-trace证书，确有公式而非“没有桥梁”。但256只给乘子后两通道相对改善；254固定二阶参数的非负软化代价为 \(2\rho=2S/3\to\infty\)，且没有原diagonal绝对控制。由此只否定该充分证书在原参数下的直接闭合，不推出负迹实际发散。固定 \(\sigma<1/2\) 的选定整数记录到完整current的参数/尺度/constant-mode/Gamma识别亦未完成，不能仅在末尾附加Gamma。
- **证据和循环性审计**：289由主代理、gap_exception_audit、midband_compute全文复核；290由主代理、carrier_audit、gap_exception_audit全文复核。新移位核6个合成零点参数的MP70精确恒等式探针通过，最大归一化差约 \(3.57\cdot10^{-71}\)，不认证实际零点或增长阶极限。Euler模型脚本以整数/Fraction核验闭点、对偶和全频primitive矩；几何权有理分支与真实Abel权浮点分支分开，后者 \(K=4,\ldots,24\) 的完整 \(J_4/\mu^4\) 为约3.16至7.10，均仅有限[E]。所有无穷量词来自证明，不来自实验、紧性或RH假设。
- **复现与仓库验收**：两份新脚本最终复跑通过；目录/TeX引用检查、11项目录回归、77项注册覆盖及模拟分发检查通过，未重跑77项重型数学计算或本轮完整远程CI。289与290另经独立交叉检查，实际zeta归约与离散模型的适用范围不冲突。
- **下一最小输入 [O]**：主线固定289-(53)：\(A=1,a=1/4\)，在同一284记录上证明保留的新有限深右谱包有 \(Q=O(M^4L)\)。即使闭合首带，\(L<|\xi|\le T_{\rm diag}\) 仍另需控制。辅助仅审计一个能替代发散软化项的低代价一侧证书，必须先给独立可检验的误差界；不暗设一致负指数或完整正性。
- **四轮决策、晋级与止损**：283--290周期完结，强记录与统一多对数谱局部化晋级为内部[T]，实际谱包相关估计保留主线；正Euler联合反例及特定软证书障碍保留为结构边界。下一周期仅继续这些已经缩小开放输入的任务；若只有更多换核/表示、一般计数、相对Schur改善或重复模型，就停止该动作，不把它登记为RH实质推进。
- **论文归属和未完成项**：289归独立Vaughan--Brownian响应论文材料；290归独立配置障碍/接口审计材料，不混入数域存在性或零点比例论文。本轮仅Markdown与两份轻量脚本，不更新PDF，DL-AUDIT未启动。文献新颖性、外部同行审查、正式论文级整合和Goal阶段验收仍[O]；未证明新零点比例、零密度或RH/GRH。

#### B1z 新周期第1轮：最优阶平方证书与实际谱区间（2026-09-06）

- **主线试探及停止记录**：三路检查289的 Erlang 短历史表示，初值和有限上端误差均可控制，但首带滤波模长为 \(1+O(1/m)\)，且先进卷积与配套微分互逆。只用guard仍留 \(T^2/L=L\) 损失，没有新actual signed saving。证据写入289第10节，不另建重复模型或长笔记；停止扩写该表示，289-(53)不升级。
- **辅助最小引理已解 [T/N]**：[291](notes/291-sharp-polynomial-square-negative-trace-certificates.md)通过显式正Jackson核卷积已知标量阶跃，构造 \(0\le b\le1,\deg b\le2m-2\)，直接给 \(0\le(-x)_++xb(x)^2\le3\pi S/m\)。全部degree-\(d\) contraction多项式的一致标量缺口又至少 \(S/(216d)\)，包括复系数情形；零次最小代价恰为 \(S/2\)。相对于187现有 \(\rho,\epsilon\) 上界的优化 \(S/\sqrt d\)，新平方证书达到 \(\Theta(S/d)\)，没有隐藏trace归一化或次数。
- **独立算术输入与实际障碍 [T/N]**：对未含Gamma的真实有限prime--continuum符号，唯一分解使素数相位流命中全0/全π邻域；连续背景在无限频率消失。由双边Chebyshev及偶素数幂界，本质谱含 \([-A+2A_{\rm even},A]\supset[-A/2,A/2]\)，其中 \(A_{\rm even}=O(Y^{1/2-\sigma})\)、\(A\asymp S^{\rm src}\asymp Y^{1-\sigma}\)。因此全实际谱上的一致多项式缺口至少 \(A/(432d)\)，不是把谱界选大了。固定每个Y再取相位高度极限，不提供统一命中高度或实际Cauchy积分下界。
- **与广义Weil配置的接口**：新 \(F(z)=-zb_{m,S}(z)^2\) 通过同一完整current的Chebyshev lag递推及共同差商 \([F(z)-F(M)]/(z-M)\)，精确进入194/195的Cauchy/Gram证书；完整 \(F(M)\)、全部signed通道和真实谱界均保留。充分误差账本为 \(|F(M)|+\sqrt{\mathbf1^*G\mathbf1}+3\pi S/m+\eta\)。只有独立算术控制和完整divisor识别后才可推出负迹结论；旧degree-two乘子、\(\mu^4\)预算和256增益不能直接挪用。
- **主要反例、循环性与范围**：通用下界可由一维谱点检验，但不能冒称每个实际谱分布的积分缺口都大。真实大频率相位可能有极小Cauchy质量，加入Gamma/有限维压缩/复Dirichlet源后双侧谱结论须另证。正核产生的是可计算effect而非算术正性；选择 \(m\asymp S\) 只控制近似误差，不控制高阶实际response。经典Jackson机制已从正式论文作者v2核验，不声明新方法或文献新颖性。
- **证据 [T/E]**：291核心全文经主代理与三名代理独立交叉核对；实际谱区间证明两路复核。新脚本的整数kernel卷积、MP60阶跃积分/Chebyshev及完整periodizedCauchy/lag response全部通过，最大后者误差约 \(1.41\cdot10^{-60}\)。样本符号是合成的，有限网格不是sup或渐近证书；主线没有把有限真实零点计算外推为(53)。
- **当时的下一最小引理；292后修订**：291的通用逼近阶已封口。292进一步证明固定左侧raw \(P_Y\) 在逼近误差 \(O(1)\) 时的signed平方响应也必发散，该绝对有界目标由[O]改为[N/停止]。只有正确右侧参数、完整通道及规范迹的实际估计仍可指向Weil；289-(53)中心化四阶预算本身仍[O]，须遵守下节的迁移门槛。
- **止损与论文归属**：本轮晋级的是证书误差改善及范围明确的次数障碍，不是RH算术正性的突破。停止固定次数的通用 \(O(1)\) 误差路线和Erlang“平滑自动节省”路线。291归独立有限迹证书/结构障碍材料；289只追加失败审计。仅Markdown及一份可复现脚本，不更新PDF、不启动DL-AUDIT；正式论文整合、外部审查和Goal阶段验收未完成。

#### B1z 新周期第2轮：实际负迹障碍与目标修订（2026-09-06）

- **已解最小引理 [T/R/N]**：[292](notes/292-record-carrier-negative-trace-obstruction.md)从原未中心化 \(P_Y=M\cos(Lt)+t\int H_Y\sin(tu)du\) 出发，用固定低频负井和全轴Plancherel/Cauchy上界证明284同一记录上正负迹均为 \(\Theta(|M|)\)。记录质量无需同时有两种符号；292-(14)核验Cauchy均值仍为 \(O_\sigma(1)\)，不能与 \(M=P_Y(0)\) 混同。
- **独立算术输入**：定量记录结论使用283无条件振荡及284因果历史转移；一般载波定理只用有限实源和相对历史 \(L^1,L^2\)。全整数尺度定性发散另用已知非平凡零点、函数方程、Euler开集及145正规族分析部分，不预设RH或离线零点。
- **配置接口与循环性**：仍是固定 \(0<\sigma<1/2\)、有限 \(N=Y\) raw符号；完整Weil使用 \(s=1/2+\delta_Y+it,\delta_Y>0\to0\) 及完整Abel尾。两者不默认等同。任何欲在原迹中补成有界负迹的修正，须在实际负井上贡献至少 \(c|M|-O(1)\) 的正质量；这只是必要条件，不把缺失补偿当公理。
- **主要障碍与停止 [N]**：固定Gamma项已严格核验为Cauchy-\(L^1\)的 \(O_\sigma(1)\)，不能修复原始符号；\(o(|M|)\) 修正同样失败。291若令 \(S/m=O(1)\)，其signed平方响应本身发散。停止追加固定Gamma、小常数、提高次数或质量归一化来制造同一raw负迹的 \(O(1)\) 目标；全Y定性结论也排除仅换共尾序列。
- **当前证据**：292包含全证明与删项反例；定量carrier平均误差为 \(O_I(|M|/L)\)，不把固定窗外推为全轴渐近。配套合成BV模型脚本只检验有限恒等式和误差账本，不认证任何实际记录或渐近定理。
- **下一最小任务 [O]**：明确一条右侧参数日程 \(\delta_Y>0,\delta_Y\to0\) 和完整Abel截断方案，先重建实际差值及原迹下的负井补偿，保持divisor germ和Poisson条件。只有出现独立误差削减或真实有符号抵消，才恢复289向完整目标的桥梁；仅重加权恒等式不算进展。
- **决策与论文归属**：修改主线目标；289-(53)中心化四阶问题门槛式保留观察，未宣布失败。292归独立response论文的适用边界，不扩写为RH证明。Markdown、有限复算、内部独立审计后提交；不更新PDF，DL-AUDIT未启动。新颖性、外部同行评审及Goal阶段验收仍[O]。

#### B1z 新周期第3轮：实际右移与独立有限接口（2026-09-06）

- **已解最小引理 [T]**：[293](notes/293-poisson-transport-and-right-shifted-record-currents.md)对同一284记录保留权与端点，令 \(W_a=e^{-au}H\)，证明 \(\tau_C|P_a|\le |M|e^{-aL}+a\|W_a\|_1+\|W_a\|_2/\sqrt2\)。在 \(\sigma'_Y=1/2+\delta_Y\) 上得到 \(O(|M|Y^{-(\beta-\sigma_0)})=o(|M|)\)。真实Chebyshev前缀进一步给 \(O(B^{(1-\sigma'_Y)/(1-\beta)})\)，而非只写半群收缩的 \(O(|M|)\)。
- **独立算术输入**：284强记录/指数历史和实际Chebyshev上界；Jensen缺口、正反三角不等式本身仅为分析工具。RH只用于独立条件基准，不参与上述实际相对缩减。
- **与Weil配置接口 [T/C]**：同一有限 \(N=Y\) 的 \(F_Y^\sharp\) 单独满足全纯性、Poisson admissibility与正确Euler开集，故可直接用145；不是声称与132完整Abel族相近。Gamma在 \(\sigma'\in[1/2,3/4]\) 的Cauchy-\(L^1\) 范数一致有界，实际均值也一致有界，所以 \(\kappa_Y^\sharp=\tfrac12\tau_C|P_a|+O(1)\)。此删项只适用于标量有界负迹，不适用于非线性Gram。
- **障碍如何被处理**：293证明右移修正和Poisson正负混合取消量均为 \(\Theta(|M|)\)，满足292要求的非微扰规模；中间迹与原迹双边可比，没有藏掉负质量。因此不能继续把“未付同阶补偿”列作已选右移的障碍，但绝对 \(O(1)\) 剩余量仍未证明。
- **循环性与条件基准 [C]**：RH下另证明全轴实部误差 \(O(Y^{-\delta}L^2/\sqrt\delta)\)，取 \(\delta_Y=(5/2)\log L/L\) 可趋零；只是安全日程，不称最优速率。逆向有界 \(\kappa^\sharp\) 仍推出RH，因此该预算不是独立弱公理，也不能把RH条件下的比较对象当成无条件正背景。
- **当前证据 [E]**：一份MP50合成混合原子脚本验证全周期Poisson/倾斜、完整加权端点公式和全轴Cauchy迹；不认证实际记录或渐近。既有143已经处理完整Abel的有限化，本轮不重新宣布解决该问题；新内容是已选记录的实际相对缩减及准确接口。
- **下一最小任务与止损 [O]**：固定上述日程、原规范迹与有限候选，在已证 \(1+B^{\theta_Y}\) 之外取得一个明确有符号算术节省，或证明所选估计机制的严格障碍。只扩写半群、重命名右侧 \(L^1\)、再调一般次数或调用全quadratic energy不晋级；147已排除后者。289只有证明能转移至此具体预算才恢复RH接口地位。
- **论文归属/决策**：实际右移定量界晋级为内部[T]，绝对存在性仍[O]；保留独立response论文材料与条件核验，不另建同义RH框架论文。不更新PDF，不启动DL-AUDIT；新颖性、外部同行评审、完整Goal验收均未完成。

#### B1z 新周期第4轮及周期决策：PNT节省与固定源饱和（2026-09-06）

- **已解最小引理 [T/R]**：[294](notes/294-pnt-envelope-gain-and-fixed-source-saturation.md)在同一实际记录上将293-C改进为 \(\tau_C|P_a|\ll T\asymp B^\theta e^{-bc\sqrt{\log B}/(1-\beta)^{3/2}}\)。外部输入仅为经典有符号PNT误差；265已有前缀界，新增的是正确右移原迹中的记录交点节省。定性PNT也已足够给统一 \(o(B^\theta)\)，但没有明确速率。
- **一般接口与独立输入**：若 \(|E(x)|\ll x e^{-\omega(\log x)}\)、\(\omega\to\infty,\omega'\to0\)，且独立有历史guard，则294-E给 \(\tau_C|P_a|\ll T_\omega=B e^{-bU}\)，\((1-\beta)U-\omega(U)=\log B\)。保留固定源界常数、完整端点及紧参数统一性，不把PNT当作记录选择的来源。
- **严格机制障碍 [N]**：[295](notes/295-fixed-positive-source-right-trace-saturation.md)构造一个固定 \(\lambda(n)\in[1/2,3/2]\)、\(\lambda(n)\to1\)，保留同一 \(\omega\)、匹配连续背景、完整截断、真正整数归一化Abel前缀记录及强质量，且对全部 \(\sigma'\in[1/2,3/4]\) 有 \(\tau_C(P_\pm)\asymp T_\omega\to\infty\)。负迹下界来自固定小频窗；全轴上界没有积分不合法的 \(O(1+|t|)\) 离散化余项。
- **主要反例的限制**：295的有限Poisson／Euler开集germ一致，但该germ在 \(s=1\) 非亚纯。真实zeta的已知亚纯延拓排除此模型；它没有素数幂支撑、Euler乘积、整函数整数除数或函数方程。不能将288/290保留的其他性质拼接给它，也没有证明所有模型子序列都失败。
- **Weil接口与循环性**：实际 \(\kappa_Y^\sharp=\tfrac12\tau_C|P_a|+O(1)\ll1+T\) 仍由293合法接入145。294只有无条件上界节省，295只有指定模型类的普遍估计障碍；均未证明RH或新的零点比例。真实绝对预算仍有RH等价强度，非构造方法不产生缺失输入。
- **当前证据 [E]**：45组MP50包络检查与主代理独立复跑通过；包括完整半轴范数、交点、积分常数和安全sup因子。只认证有限浮点公式一致性，不认证实际PNT常数、记录或渐近；295全尺度结论完全来自证明。
- **晋级／止损／下一最小任务**：本周期将定量右移与PNT剩余量节省保留为内部[T]，停止继续只换光滑次幂PNT包络、固定源一致性或历史soft norm。下一周期首先核对旧有限零点/深尾结果，尝试对固定有限非实Mellin极点包证明正确右侧交点尺度的严格缺口，并追踪高度与数量增长时的统一性损失；只出现等价重写或既有有限展开则不晋级。只有引入模型未保留的已知解析或真实算术限制，并得到独立量化结论，才继续。
- **论文归属与完成边界**：归独立response论文的“适用范围与估计障碍”材料，不另扩写同义RH框架。先保留Markdown，未更新PDF；文献新颖性、外部同行审查与Goal阶段验收仍[O]。David--Lapidus观察线未启动。

#### B1z 亚纯接口周期第1轮：临界边界层与端点审计（2026-09-06）

- **主线与已解最小引理 [T/N]**：[296](notes/296-critical-pole-boundary-layer-and-shift-schedule.md)对固定临界共轭极点包给出统一负迹渐近。令 \(L=\log Y,\ q=\delta L,\ E=e^{-q}\)，在 \(0\le q\le A\log\log L\) 中，主项为 \(4E\log L/[\pi^2(1+\gamma^2)]\)，误差为 \(O_{\gamma,A}(E[1+q+\log(1+q)])\)，即使主项趋零仍有相对渐近。正迹另有趋于 \(2/(1+\gamma^2)\) 的质量，不能与负迹混同。
- **独立输入与配置接口**：主线只用显式有限积分、Poisson恒等式及有界周期函数的调和积分估计，不用RH。模型 \(\Phi(w)=w^2+\gamma^2\) 是真整函数整数除数，有限候选满足Poisson与右半平面局部一致germ；因此相比295保留了亚纯除数结构。它只校验145/293的显式公式型接口，不构造数域上同调或实际素数源。
- **主要反例及删除假设**：即使极限对数导数正实，硬截断在 \(q-\log\log L\to-\infty\) 时仍有负迹发散；任意共尾日程不能由极限正性自动推出。改用三角形log权后，纯指数模型为Fejér正核，保留Abel因子也有 \(\kappa_-\le8e^{-q}/L\)；故不排除其他正则化、完整Weil配置或真实RH。任意有符号背景必须保留自身负迹。
- **辅助线与去重 [T/R/N]**：[297](notes/297-raw-pole-endpoint-splitting-obstruction.md)证明每个固定 \(Y>2\) 的原始复核满足 \(\tau_C|K_\rho|\ge c_Y/|\gamma|\)，经典Riemann--von Mangoldt计数遂使逐项绝对和发散；双端点补偿 \(I_\rho\) 则有跨实部共振的一致参数界。固定 \(Y\) 的定性可和性已隐含于282，只明确其量化范围，不重复登记为突破；实际配对实部的发散并未证明。
- **本轮停止的尝试**：固定有限谱边缘的幂次缺口大部分由旧280/282/286或更强幂次包络直接推出；不另写“有限包改写”长篇。297的粗尾 \(Y^{1-\sigma'}\log^2(2V)/V\) 尚不能在多对数高度给294所需小量，289的不同余核与中频四阶范数不得直接移植。
- **RH/GRH循环性审计**：已知模型的中心线除数只用于反例和核归一化，不能当作真实 \(\xi\) 的谱输入。296不改293明确安全日程下的RH等价性，也没有证明有界负迹是更弱的算术假设。有限计算不升级为一致极限或真实零点结论。
- **当前证据 [E/T]**：296全文由主代理与carrier_audit分别逆向复核；297全文由主代理与gap_exception_audit分别复核。9组MP50脚本由作者与主代理各自运行通过，另含6个原积分点检，代码的根分割和全部预算另经独立只读审计。所算局部primary负部不是全轴负迹，临界规则下有限比值仍远离1，不以实验认证渐近。布局及11项回归、77项注册/mock核验通过，未重跑77项重型计算。
- **下一最小引理 [O]**：对一个孤立的固定临界零点窗，将真实有限完成候选减去296单包后的余项先写成保留完整双端点的联合算术量，检验能否得到随 \(Y,\delta\) 一致的局部界，或足以传递负迹的局部 \(L^1\) 界。必须追踪其他零点、全谱尾和Gamma，不能用逐个复核绝对和替代。仅完成恒等式不晋级；若旧界仍差一个增长因子，应明确记录因子并停止同类改写。
- **晋级、止损与论文归属**：本轮晋级为内部可审计的日程校准和端点障碍，不登记为真实zeta的新算术节省。下一轮只继续上项单一余项问题；不扩写任意有限包，也不以Fejér模型的正性代替算术证明。材料暂归独立response论文的有限化审计附录；先用Markdown，不更新PDF。DL-AUDIT未启动；文献新颖性、外部同行审查与Goal阶段验收仍[O]。

#### B1z 亚纯接口周期第2轮：真实载波消去与局部预算强度（2026-09-06）

- **主线与已解最小引理 [T/N]**：[298](notes/298-actual-critical-window-and-fast-shift-obstruction.md)对293的真实有限 sharp--Abel 完成候选证明：任意 \(Y_j\to\infty,\delta_j>0\) 若 \(\delta_j\log Y_j-\log\log\log Y_j\to-\infty\)，则原 Cauchy 负迹趋于无穷。任何 \(\delta_j\to0\) 的有界负迹序列必须有 \(\delta_j\log Y_j\ge\log\log\log Y_j-O(1)\)。不再只停留于296的单包模型。
- **独立输入与精确配置接口**：保留真实 prime--continuum 源、完整整数端点、Gamma与补偿零点核；经典显式公式、单位高度计数、函数方程和零点存在性沿用282/285/293，主代理本轮再次核验Kedlaya书稿。固定频窗中，在RH下其余通道等于共同端点 \(-e^{-1-q}E(Y)\cos(t\log Y)/\sqrt Y\) 加统一 \(O(1)\)。非负测试由完整负半周期构成，先用Cauchy密度的固定下界，再精确消去任意大小的端点载波。接口仅为145/293显式公式型正规族，不构造上同调，也不默认两类Weil结构等价。
- **RH/GRH循环性审计**：局部下界 \(c e^{-q}\log[L/(1+q)]-C\)、\(0\le q\le\log\log L\)，明确为[C/RH]。无条件发散先假设有界子序列，通过已独立核验的293/145接口推出RH，再在同一子序列使用条件下界得矛盾；不能输出无条件增长率。主定理要求严格 \(\delta>0\)，不偷用未证明的边界Poisson版本，不需Littlewood记录或Mellin反演。
- **主要反例与适用边界**：固定数目、固定高度和固定实系数的同核中心模式减法仍满足障碍；需重新证明Poisson而非相减两个下界，再选择一个未删实际零点。更换三角权的296模型不受本定理排除；增长模式包、任意尺度相关修正、其他zeta/L模型及临界充分性都未覆盖。删除完整半周期的对称测试就不能无代价忽略共同载波。
- **辅助线一：强输入审计 [T/N]**：[299](notes/299-local-one-sided-budget-mellin-strength-audit.md)证明，对于固定 \(q\)、固定正宽紧频窗和一个指定符号，全部充分大整数 \(Y\) 的局部一侧 \(O((1+\log Y)^k)\) 预算与RH等价；允许减去固定有限实际临界包。证明独立重建Mellin--Volterra恒等式、复乘子无零、固定频率的正轴解析及Landau正性奇点论证，极点与对数级修正不会抵消。不将双解析余弦分支写成复变量函数的实部。此预算在RH下可取 \(k=3\)，并非被无条件排除；固定 \(q\)、全尺度及正宽窗口是本证明必要量词，稀疏共尾子序列不被覆盖。
- **辅助线二与证据 [E/T]**：九组MP50合成核复算由作者和主代理分别运行；载波消去残差 \(<2.51\cdot10^{-52}\)，矩形原函数与独立Fubini积分缩放差 \(<2.71\cdot10^{-50}\)，Abel误差/阶乘尾上界 \(<7.99\cdot10^{-4}\)。输出是非负测试的线性下界泛函，可能为负，不冒充完整负迹或实际零点实验。298经主代理、gap_exception_audit、midband_compute分别全文复核；299经主代理和midband_compute全文复核，并修正Taylor求和点必须严格位于解析圆盘内的措辞。布局、11项回归与77项注册/mock调度检查通过；未重跑重型计算。
- **下一最小引理 [O]**：仅核验RH下
  \[
   \tau_C\left|F_Y^\sharp(\delta+it)-\frac{\xi'}{\xi}(1/2+\delta+it)\right|
   \stackrel{?}{\ll}
   e^{-q}\frac{|E(Y)|}{\sqrt Y}
   +e^{-q}\log(2+1/\delta)+Y^{-1/2-\delta},
   \qquad q=\delta\log Y .
  \]
  必须证明全轴与参数一致性，不能把固定窗口的 \(O(1)\) 延伸到全轴；再单独审计小端点整数截断与临界日程。这里仍为[O]，即使证明也先属RH条件校准，不产生缺失的无条件正性。
- **晋级、止损与论文归属**：真实过快日程障碍晋级为内部[T/N]，局部预算仅登记为隐藏RH输入的审计，不因等价表达而继续扩写。停止亚临界日程、固定有限模式修复及未经算术证明的全尺度局部背景界；下一轮若只有恒等式或旧误差因子，停止同类改写。材料归独立response论文的有限化/亚纯接口障碍部分，先用Markdown、不更新PDF，不混入四矩比例或上同调存在性论文。DL-AUDIT未启动；本轮无新零点比例、零密度、零自由区或RH/GRH证明，新颖性、外部同行审查与Goal阶段验收仍[O]。

#### B1z 亚纯接口周期第3轮：全轴误差与真实临界常数（2026-09-06）

- **主线已解最小输入 [C/RH]**：[300-A](notes/300-endpoint-separated-global-error-and-critical-schedule.md)证明全部 \(Y\ge4,\ 0<\delta\le1/4\) 的全轴复模误差至多 \(C\{e^{-q}|E(Y)|/\sqrt Y+e^{-q}\log(2+1/\delta)+Y^{-1/2-\delta}\}\)。相比293的实部粗界，保留实际共同端点并将其余谱损失降至对数级。300-B在 \(1\le q\le L/4\) 给 \(1+\kappa\asymp1+e^{-q}(|E(Y)|/\sqrt Y+\log L)\)；不删除加1或扩至q<1。
- **配置接口与独立算术构造 [T]**：显式修正 \(\widehat F_Y=F_Y^\sharp+e^{-1}Y^{-s}E(Y)\) 不读取零点；等价于同一有限权在上端锚定为零，完整连续项/Gamma不变。通过有限实lag源、Gamma大半圆与Chebyshev重新核验Poisson/Euler-germ，未相减两个Poisson下界；整数截断跳跃精确抵消，修正族对实Y连续。它只校准显式公式型接口，不构造上同调或无条件正性。
- **真实全谱临界渐近 [C/RH]**：300-C对固定 \(A>0\)，统一 \(1\le q\le A\log\log L\)，给 \(\widehat\kappa_Y/(e^{-q}\log L)\to C_\zeta=2(\xi'/\xi)(3/2)/\pi^2>0\)。先固定有限对称谱包，负部上界用次可加性和正余谱，下界用隔离窗；以补偿差的两条可和尾预算控制遗漏谱，先Y趋无穷、再谱包增大。没有假设包间间距或固定包常数对族一致。
- **辅助一：无条件小端点整数 [T]**：300-D的 \(\mathcal C=\{n:E(n-1)>0\ge E(n)\}\) 共尾且 \(-1<E(n)\le0\)。用实际Mellin变换在正实轴解析、已知非实极点和非负Laplace的Landau性质证明弱双向无界，再保留完整整数差 \(\Lambda(n)-1\ge-1\)。不需RH、Littlewood强幅值或记录选择。原候选沿此序列有同一RH条件渐近，但这些点不继承284的强质量/历史账本。
- **RH循环性与停止边界**：在修正族全尺度或原族的小端点序列上，临界 \(q=\log\log L+c+o(1)\) 的RH条件极限是 \(C_\zeta e^{-c}>0\)，不是趋零。一般靠线序列的“有界 iff RH且偏移有下界”“趋零 iff RH且偏移趋正无穷”只作强度审计，不能登记为独立算术输入。原候选任意尺度仍需端点预算；298过快日程障碍也适用于修正族，未得到无条件速率。
- **独立外部输入与删除测试**：经典显式公式、单位高度计数、函数方程、非实零点存在性与Hadamard展开；主代理本轮再读Kedlaya第9章的相关条目。Euler开集识别不需要RH点态PNT率；差核TV包含所有跳跃，全轴估计不删s因子。若删RH，谱振幅与正余谱同时失效；若删隔离窗，局部下界不能从粗全轴尾恢复首项；若先取增长包，固定间隔常数失去依据。
- **辅助二、证据与审计 [E/T]**：六组合成核、48次MP50比较，原lag积分加解析尾对32阶展开的最大差 \(2.783\cdot10^{-39}\)，不超过显式阶乘尾；未计算实际零点或全轴Cauchy范数。脚本作者与主代理各自运行通过。全文逆向审计及仓库检查在300第11节登记；所有数值只[E]。
- **下一最小引理与晋级条件 [O]**：只检查300-(50)的高度差π/L双包碰撞模型；必须保留两对模式、Abel权和参数一致误差。若联合负迹的对数主项消失，即给固定包渐近不能无簇条件向族外推的精确障碍；若否，记录反例并停止该猜测。此模型随L变化，不能当作固定zeta或实际L函数的零点构造。
- **周期决策与论文归属**：本固定候选的条件日程校准闭合，停止继续改写等价预算；第4轮只做上项有限一致性测试并收束周期。300暂归独立response论文的有限化/亚纯接口部分，本轮仅Markdown、不更新PDF；外部文献定位和独立同行审查完成前不确认新颖性或Goal阶段验收。不并入四矩比例论文，不启动DL-AUDIT，无新RH/GRH、零点比例、零密度或零自由区。

#### B1z 亚纯接口周期第4轮及收束：临界簇相位障碍（2026-09-06）

- **主线最小引理已解 [T/N]**：[301](notes/301-cluster-phase-cancellation-and-nonuniform-divisor-families.md)验证300-(50)。两个等权共轭包间距π/L时，完整负迹至多 `e^-q(2π/q+4/(1-δ))`，统一q≥1、0<δ≤1/4；证明先合并振荡尾并保留非负Poisson背景。一般固定有限正权簇的主系数为 `4|Σm_j e^-ih_j|/[π²(1+γ²)]`，统一1≤q≤A loglogL；不把单包负部相加成等式。
- **独立输入与Weil接口**：仅指定完整sharp--Abel核、正权、Cauchy迹、精确resolvent和周期平均，无新增素数算术输入。有限实lag候选独立满足精确Poisson等式；整数权给中心轴整多项式除子。它是显式公式型有限迹接口的模型检验，没有构造上同调/极化，亦没有证明两类配置的桥梁或数域存在性。
- **辅助一与严格反例 [T/N]**：相干簇(0,0)和抵消簇(0,π)有相同极限除子(z²+γ²)²及同一解析germ，内部紧集误差为O_K(1/L+e^-aL)。沿q=(1/2)loglogL，前者负迹发散、后者趋零。这里不是Euler germ，也不是实际ζ反例；只排除这些定性收敛/Poisson结构决定靠界统一预算。负权与γ=0各另有明确删项反例。
- **辅助二、文献与循环性**：六组合成核MP50复算通过，分别检查原lag、合尾、Abel误差及完整非振荡尾范数，不计算full负迹或actualζ。Harris1978原文的窗口/移位核机制已核验，不能声称相位抵消是新方法；Cauchy负迹及同germ结果的具体文献优先权未核验。证明未假设RH或所求正性；内部模型定理不升级为无条件实际零点定理。
- **当前审计证据**：301由主代理、gap_exception_audit、midband_compute最终全文复核通过；carrier_audit独立重建双包界并审查同germ、删项反例及文献边界，均无必须修改项。目录/TeX链接检查、11项目录回归、77项注册覆盖及模拟分发检查通过；未重跑77项重型数学计算，也未将本轮新提交的远程CI声称为已通过。无数值到渐近、固定包到增长包或解析germ到Euler源的未经证明升级。
- **四轮决策**：296--297模型边界层、298--299真实过快日程障碍与强输入审计、300真实条件校准、301族非一致性，完成一个四轮周期。晋级内部[T/N]及[C/RH]的明确结论，停止扩写同一候选的RH等价预算；不新开增长簇模型调窗线，不自动推广L函数族。
- **下一有限任务与止损 [O]**：只对已缩小的289-(53)实际首带深右谱包预算做一轮准入审计，固定A=1,a=1/4，寻找实际带符号相关定理并逐项匹配源、物理频带、谱高度、权及四阶归一化。能给独立saving或严格缩小开放输入才启动下一周期；若只有一般计数、已有guard、合成相位或等价换表示，则保留观察并重选主线。首带闭合也不自动覆盖更高中频。
- **论文归属和未完成项**：301属独立有限迹/配置接口障碍材料，仅Markdown，不更新PDF。DL-AUDIT未启动。真实正性、RH/GRH、记录比例、新零密度、文献新颖性、外部审查及Goal阶段验收均未由本轮解决。

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

### DL-AUDIT：David--Lapidus 限额结构审计与模型验证（观察，未启动）

- **角色、限额与当前状态 [O]**：作为原 Weil 目标的模型验证接口，不另立 RH 主线，也不替换 B / NCE-8。维护三项完成前不启动；若随后启动，只安排一个 4--6 轮试审周期，累计研究资源不超过同期总资源的 10%，从观察/辅助份额内协调，不追加总预算或削减 B 主线份额。每轮只记录 Markdown 审计证据，不要求更新 PDF。期满必须作晋级、保留观察或停止决定，未经复核不自动续期。
- **独立输入 [O]**：需要选定 Weierstrass 模型的几何定义、上同调及定义域、配对/极化、Frobenius 类算子和 zeta 表示的可验证数据；若转向数域，另须给出不从零点反向定义的独立算术来源。分形模型中的几何输入不自动等同于数域算术输入，目前没有据此获得新的数域正性估计。
- **与广义 Weil 配置的接口 [O]**：先核对上同调分次、对偶/极化、Hodge 型正性、算子相容性、谱与 zeta 零极点的精确对应。显式公式型 Weil 二次型、素数/Gamma 项与迹公式的桥梁必须另列开放命题；不默认两类结构等价，不以该模型取代 256 的实际 prime--continuum 接口。
- **下一最小引理 [O]**：先固定 2024 文稿中的一个明确模型和一个几何极化正性与 Frobenius 相容性命题，逐项重建其定义、最小假设和证明，并核验谱识别依赖。有限、可证伪的审计问题是：正性及相容性是否由该模型的几何数据独立导出，还是使用了预设的复余维位置、纯性或待证谱结论？本次只登记此问题，不执行证明复核，也不同时审计整篇约 90 页文稿。
- **当前证据 [R/O]**：下列只记录此前已经核验的一手来源及其适用边界，不登记新的内部定理。

  - [R] Lapidus 2008 年《In Search of the Riemann Zeros》的作者公开序言区分分形膜的严格构造与关键模流的猜想性质；模流存在、吸引性质和通向 RH 的动力学图景不能当作已证输入。[作者序言与导论](https://math.ucr.edu/~lapidus/confidential/ISRZintro.pdf)
  - [R] 2015 年《Towards Quantized Number Theory: Spectral Operators and an Asymmetric Criterion for the Riemann Hypothesis》给出谱算子的非对称 RH 等价判据；等价判据本身不是独立可逆性证明。[作者预印本](https://arxiv.org/abs/1501.05362)，[正式论文](https://doi.org/10.1098/rsta.2014.0240)
  - [R] Cobler--Lapidus 2017 年文稿的行列式实现允许从零点/极点构造谱数据；作者明确指出直接用于 RH 仍需独立几何来源。此类实现不自动提供正性。[作者预印本](https://arxiv.org/abs/1705.06222)
  - [R] David--Lapidus 2024 年文稿《From Weierstrass to Riemann: The Frobenius Pass》在 Weierstrass 模型中提出并给出若干上同调、Hodge 型结构、Frobenius 类谱识别和双对象 zeta 函数方程的结果；已核验范围是作者摘要/引言及可检索原文，作用对象是该曲线的复余维，而非已识别的经典 Riemann 零点。[作者全文](https://hal.sorbonne-universite.fr/hal-04614665v3/file/Functional.pdf)，[作者出版目录](https://sites.google.com/view/clairedavid/accueil/articles-publications) [O] 全文独立证明审计、精确成立范围与最终出版版本核对尚未完成；以上文献记录不是对全部证明的背书。
- **主要反例与负向测试 [O]**：纳入具有函数方程但 RH 类比失败的模型作为测试；另对“从零点构造算子”“由对称性直接推出中心线”“有限模型成立便宣称极限成立”逐项检查。测试对象及出处须在试审时明确列出，目前不宣称已证明针对 David--Lapidus 模型的反例或障碍。
- **RH/GRH 循环性审计 [O]**：不得把归一化酉性、完整 Weil 正性、统一负指数界、RH 等价的可逆性、零点向中心线收敛或依赖零点构造的自伴性用作未解释的公理。模型函数方程不等于纯性；模型谱识别不等于算术谱识别；任何有限到整体、模流收敛及数域桥梁必须单独陈述并审计。
- **晋级与止损条件 [O]**：只有完整复核一个由独立几何数据推出的非循环模型命题，或把数域桥梁严格缩为一个明确且此前未解决的输入，才考虑晋级；不以术语相似、行列式重写或新的 RH 等价表述晋级。若一个试审周期内不能缩小输入、关键全文不可取得、依赖无法定位，或核心正性/吸引性质仍只是假设，则回到观察状态；若确认循环性，则停止该推理方向。不得因框架可持续扩写而续期。
- **预期论文归属 [O]**：先形成独立的 `DL-AUDIT` 文献/结构审计与模型验证笔记。只有达到论文级证明、依赖审计和独立复核后，才考虑单独模型论文或结构主稿中明确隔离的验证实例；不混入数域 RH 存在性证明、四阶矩比例论文或当前 Brownian 响应主定理链，不预先声称新颖性。

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

`DL-AUDIT` 尚未启动，故不改变上表现有分配；若启动，其不超过 10% 的限额从观察/辅助份额中协调，并保持 B 为当前主线。该限额不是在上表之外追加的并行预算。

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
