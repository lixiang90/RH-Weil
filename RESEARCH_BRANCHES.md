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
| MOM-1 | 四矩备用主线 | weighted Gabor kernels 的 S4 finite-to-bulk bound 与未配对近共振 Gram | MT 窗 remainder 小于 0.0829099143，或优化窗总预算闭合 | exact cycle/word ledger、S4 gate 与一般 paired-diagonal window functional 已完成 |
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

## 文件约定

- 新笔记标题注明分支 ID，例如 `NCE-1`；
- 同一轮只保留一个主线，其余路线独立探索，不把未经证明的假设互相引用成结论；
- 每轮结束更新本表的“下一最小引理”和状态；
- Git branch 仍按交付任务管理；这里的 ID 表示数学思路分支，不强制创建长期 Git branch。

## 本轮分支成果

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
