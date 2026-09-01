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
| NCE-8 | 构造/非构造汇合 | common Volterra bound for the signed cumulative combination Q5-2aB Q4+a^2B^2 Q3 | mixture-integrated signed profile capacity与 soft/Gamma误差一致有界且不调用 full Selberg profile | high-order absolute-moment route被 coefficient tax停止；signed heat profile晋级 |
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
