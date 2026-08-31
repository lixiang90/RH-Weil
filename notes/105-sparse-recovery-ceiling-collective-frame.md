# Sparse incidence recovery 的最优指数与 collective-frame 必要性

文档 104 用 fixed squarefree nodes 证明了
`sigma_N>=c_R(log N)^(-2R)`。一个自然问题是：让 recovered nodes 随 `N`
移动，能否在同一 incidence-recovery 方法内改善这个 exponent？本节证明不能。
任何 bounded-cardinality node recovery 都必须支付末端差分的 condition number，
其最优 certificate rate 至多仍为 `(log N)^(-2R)`。

因此文档 104 的 exponent 在 sparse recovery 范畴内已经 sharp。若要达到 RH
路线所需的更强 purity，必须利用全部 unit-cell wedges 的 collective frame gain、
证明 response forcing 衰减，或直接控制 forcing-weighted spectral measure。

## 1. Maximal-node condition number

沿用文档 104 的 notation。取 `R` 个 squarefree nodes

`S={n_1,...,n_R}`, `M=max S`, `L=log N`.             (1)

exact sparse certificate 是

`gamma_(N,S)=sigma_min(D_(N,S))^2`

`             /(||T_S||^2 beta_R)`,                (2)

其中 `beta_R=lambda_max(B)`。令 `ell_M=log(1+1/M)`。

### 定理 UE（node-specific sparse ceiling）

对任意这样的 `S`，

`gamma_(N,S)`

` <=[R ell_M^2/beta_R]*(log M/L)^(2R)`             (3)

` <=[R/beta_R]*(R/e)^(2R)L^(-2R)`.                (4)

#### 证明

recovered matrix 的第 `R` 列满足

`||D_(N,S)e_R||^2`

` =sum_i(1-log(n_i)/L)^2(log(n_i)/L)^(2R)`

` <=R(log M/L)^(2R)`.                              (5)

故 `sigma_min(D)^2<=R(log M/L)^(2R)`。另一方面，最大 node `M` 的
Möbius-inversion row 中，cell `p_M` 只可能来自 top divisor increment `q_M`，
其 coefficient 精确为 `-1/ell_M`；proper divisors 不含 `p_M`。所以

`||T_S||>=1/ell_M`.                                (6)

把式 (5)--(6) 代入式 (2) 得式 (3)。又
`ell_M<=1/M`。令 `x=log M`，则

`(log M)^(2R)/M^2=x^(2R)e^(-2x)`                  (7)

在 `x=R` 取全局最大值 `(R/e)^(2R)`，得到式 (4)。`□`

这个 upper bound 不使用 node separation；即使 Vandermonde conditioning 完美，
incidence inversion 的 endpoint coefficient 也已强迫同一 exponent ceiling。

## 2. Sparse exponent 的 sharpness

### 定理 UF（fixed-cardinality recovery exponent theorem）

对每个 fixed `R`，在所有恰含 `R` 个 squarefree nodes、允许依赖于 `N` 的
sparse recovery certificates 中，最佳可能的 logarithmic exponent 精确为
`-2R`：

`c_R L^(-2R)<=sup_S gamma_(N,S)<=C_R L^(-2R)`.     (8)

这里 lower bound 对充分大 `N` 成立，`c_R,C_R>0` 只依赖 `R` 与 endpoint
weights。更一般地，任意 bounded-cardinality node family 的 exponent 仍不能优于
`-2R`。

#### 证明

lower bound 是文档 104 定理 UC：固定任一组 distinct squarefree nodes。upper
bound 是定理 UE 的式 (4)。若 node count 为固定 `K>=R`，式 (5) 的 `R` 改为
`K`，其余证明不变，故 exponent 不变。`□`

所以移动 nodes 只能优化常数。式 (7) 还预言 optimal maximal node 位于
`M~e^R` 的固定尺度，而非随 `N` 趋向 infinity。

## 3. Certificate-level centerline barrier

文档 102 定理 TV 的 shorted sufficient bound 包含

`Psi_N/gamma_N`,                                   (9)

其中定义 regression-forcing factor

`Psi_N=(aC_W-1)/(aC_W^2)`.                         (10)

### 定理 UG（sparse certificate forcing requirement）

若在定理 TV 中只用 bounded-cardinality sparse recovery lower bound
`gamma_(N,S)`，则要使 corresponding Riesz upper bound 达到

`o(sqrt(L)/loglog(3N))`,                            (11)

必须额外证明

`Psi_N=o(L^(1-2R)/(loglog(3N))^2)`.                (12)

因此若 `Psi_N` 没有这种 compensating decay，sparse recovery certificate 本身
不可能认证 centerline rate。

#### 证明

文档 102 式 (28) 中，除 bounded constants 与 base term 外，squared Riesz
upper contribution 为 `(R+1)Psi_N/gamma_(N,S)`。要使其为
`o(L/(loglog(3N))^2)`，必须有

`Psi_N/gamma_(N,S)=o(L/(loglog(3N))^2)`.           (13)

定理 UF 表明 certificate 能提供的 `gamma` 至多为 `C_RL^(-2R)`；代入式
(13) 得式 (12)。`□`

这是 certificate no-go，而不是 RH 的反证：actual `sigma_N` 可以远大于
sparse lower，exact forcing spectral measure 也可以远小于 worst-direction bound。

## 4. Collective unit-cell amplification

文档 103 的 unit-cell frame 使用全部 cells，通过

`bar S=(1/bar a)sum_(m<n)w_mnw_mn^*`               (14)

聚合，而不逐 node 逆转 divisibility operator。定义在某个 finite search range
`M_0` 上的 collective amplification

`G_coll=bar sigma_unit/max_(S subset [2,M_0])gamma_(N,S)`. (15)

### 命题 UH（collective route separation）

`bar sigma_unit` 与 sparse ceiling 不受同一个 recovery-condition-number upper
bound 约束。事实上式 (14) 直接累积 projected observations，而定理 UE 的
`1/ell_M` loss 只在尝试逐个恢复 divisor atoms 时出现。因此若
`G_coll` 随 `N` 增长，改善必须来自 genuine collective frame geometry，不能由
重新选择 finitely many nodes 解释。

这是结构上的区别：Weil-style intersection positivity 通常也是大量 cycles 的
Gram/minor sum，而不是先反演出少数 individual cycles 再取最坏 singular value。

## 5. Finite audit

下表对 squarefree nodes `<=20` 穷举。`gamma_best` 是最佳 sparse certificate，
`bar sigma_unit` 是文档 103 的 full unit-cell lower。搜索上限只用于 finite audit；
定理 UE--UF 不依赖该上限。

| `N` | `R` | best nodes | `gamma_best` | `bar sigma_unit` | `G_coll` |
|---:|---:|:---|---:|---:|---:|
| 30 | 2 | `[2,5]` | `7.48e-7` | `2.09e-5` | 28.0 |
| 30 | 3 | `[2,5,11]` | `1.72e-9` | `3.37e-7` | 196 |
| 100 | 2 | `[2,5]` | `2.90e-7` | `2.02e-5` | 69.7 |
| 100 | 3 | `[2,6,13]` | `5.60e-10` | `4.19e-7` | 748 |

扩大到 `N=1000` 而仍搜索 nodes `<=20`，best sets 为 `[2,7]` 与
`[2,7,17]`；scaled values `gamma_best(log N)^(2R)` 约为
`1.62e-4` 与 `9.47e-6`，继续符合 fixed exponent。best maximal nodes 也接近
`e^2`、`e^3` 的预言。

finite data 中 collective gain 明显增长，尤其 `R=3`；这并未证明其 asymptotic
增长，却说明全部-cell structure 已包含 sparse recovery 看不到的大量 positivity。

## 6. 下一步的严格分叉

定理 UF--UG 排除了“只优化有限 recovered nodes 就达到 RH threshold”的路线。
剩余三条彼此独立、均保持 actual zeta problem 的路线是：

1. **Collective-frame route**：直接证明 unit-cell wedge/minor sum 的
   `bar sigma_unit` 具有强于 `L^(-2R)` 的 lower bound；
2. **Forcing route**：证明 regression factor `Psi_N` 满足式 (12) 或更强的
   forcing-weighted版本；
3. **Spectral-alignment route**：绕开 `sigma_N`，直接估计文档 102 式 (18) 的
   shorted spectral second moment。

第一条最接近 Weil 猜想的“许多 cycles 共同产生 Hodge positivity”，第二条最接近
Nyman--Beurling extremizer alignment，第三条是逻辑上最弱但算术上最定向的充分
条件。

## 7. 计算实现

`mobius_cell_vandermonde_recovery_certificate` 现额外返回 node-specific sparse
upper 与定理 UE 的 universal envelope。新增
`mobius_sparse_recovery_search`，对有限 squarefree candidate range 穷举并返回
最佳 exact certificate，用于复现上表。

回归测试核对 exact lower 不超过两个 analytic ceilings，并核对 finite search
至少改进或保持默认 node choice。搜索只承担实验审计，定理 UF 的 upper proof
不依赖枚举。
