# External period 的 positive capacity-loss certificate

文档 124 将 exact endpoint leverage 分解为单个外点 period `|F'(2)|` 与 sign
defect。主项仍是 signed inverse-Gram pairing。本节用 dual Hodge Gram 的 Schur
complement 把它完全正量化：外点 period 的平方正是 response line 从 external
probe capacity 中吸收的能量。该吸收量可由一次 positive rank-one metric update
及两个 determinant quotients 精确恢复。

这给出一个只含 positive capacities 的 generalized centerline criterion。但 finite
audit 表明 external probe 的总 capacity 很大，吸收比例又强烈波动；因此本节是
结构化归约而不是 RH 证明。

## 1. Dual two-class Hodge Gram

令 `W>0`、response `D`、external probe `q=q_ext`，并记

`C_D=D^*W^(-1)D`,                                 (1)

`C_q=q^*W^(-1)q`,                                 (2)

`K=D^*W^(-1)q`.                                   (3)

dual capacity Gram 为

`G_dual=[[C_D,K],[conj(K),C_q]]>=0`.              (4)

定义把 response class 短接后的 conditional probe capacity

`C_(q|D)=C_q-|K|^2/C_D`,                          (5)

以及 correlation fraction

`beta_ext=(C_q-C_(q|D))/C_q`

`        =|K|^2/(C_DC_q) in [0,1]`.               (6)

### 定理 WT（external period as Schur capacity loss）

canonical external leverage 满足

`L_ext:=|K|/C_D`

` =sqrt((C_q-C_(q|D))/C_D)`                       (7)

` =sqrt(beta_ext C_q/C_D).`                       (8)

并且

`C_(q|D)=det(G_dual)/C_D`.                        (9)

#### 证明

式 (4) 是 vectors `W^(-1/2)D,W^(-1/2)q` 的 Gram，故 positive semidefinite。
对其第一对角 block 作 Schur complement 得式 (5)、(9) 与非负性。重排式 (5)
并开平方给式 (7)；式 (6) 给式 (8)。`□`

当文档 124 的 endpoint coefficients 交错时，`L_1=L_ext`；一般则

`L_1=L_ext+Delta_alt`.                            (10)

## 2. 一次 positive update 的精确恢复

对任意 `s>0` 定义

`W_s=W+sDD^*`,                                    (11)

`C_q(s)=q^*W_s^(-1)q`.                            (12)

### 定理 WU（rank-one response absorption）

有

`C_q(s)=C_q-s|K|^2/(1+sC_D)`,                    (13)

所以 finite positive capacity loss

`Delta_q(s)=C_q-C_q(s)>=0`                        (14)

精确恢复 external leverage：

`L_ext^2=(1+sC_D)Delta_q(s)/(sC_D^2).`            (15)

此外

`C_D=[det(W+sDD^*)/det W-1]/s`,                  (16)

`C_q=det(W+qq^*)/det W-1`,                        (17)

`C_q(s)=det(W_s+qq^*)/det W_s-1`.                (18)

所以式 (15) 只需 positive matrices 的 determinant quotients。

#### 证明

Sherman--Morrison identity

`W_s^(-1)=W^(-1)-sW^(-1)DD^*W^(-1)/(1+sC_D)`    (19)

在两侧配对 `q` 得式 (13)--(15)。式 (16)--(18) 分别应用 rank-one matrix
determinant lemma。`□`

令 `s->infinity`，式 (13) 收敛到式 (5)，故 conditional capacity 是 response
polarization 无限增强后的正极限。

## 3. Positive-only external Weil criterion

沿用文档 124 的 sign defect `Delta_(alt,N)`，并令所有 quantities 可随 cutoff `N`
变化。

### 定理 WV（response-absorption centerline criterion）

若存在任意 positive amplitudes `s_N`，使

`c_1+|target|[sqrt((1+s_NC_D)Delta_q(s_N)`

`                         /(s_NC_D^2))`

`                   +Delta_(alt,N)]`

` =o(sqrt(log N)/loglog(3N)),`                    (20)

则 fixed principal determinant strata 为 `o(1)`；连同完整 polarized Weil
package 与总尾公理即推出相应 zeta zeros 位于中心线。

等价地，主项条件可写成

`beta_(ext,N) C_(q,N)/C_(D,N)`

` =o(log N/[loglog(3N)]^2)`.                      (21)

#### 证明

定理 WU 表明式 (20) 方括号精确等于
`L_ext+Delta_alt=L_1`，故应用文档 120 定理 WE。式 (21) 来自定理 WT 并平方。
`□`

定理 WV 是一个适用于广泛 filtered Hodge packages 的正结构定理：只需 positive
polarization `W`、response class、固定 external Tate probe、endpoint sign defect
及 response-induced capacity absorption。它不要求输出 inverse matrix或 signed
polarization difference。

## 4. 经典 Möbius--Farey specialization

取 `W=W_N^[0,N^2]`、`D` 为 Möbius endpoint response，并取

`q_ext(p)=(p+2)2^(p-1)`.                          (22)

则式 (11)--(18) 对每个 fixed rank 无条件定义且可由 finite determinants 计算。
所以经典 zeta 的 external response-absorption structure 已存在；尚缺的是式 (20)
或 (21) 的 cofinal rate，以及 sign defect/growing determinant tails。

这个输入不是 pointwise Mertens bound。它要求 external evaluation representer 与
Möbius response representer 在 dual Hodge geometry 中具有足够小的 normalized
correlation，同时允许 `C_q` 本身很大。

## 5. Finite audit

`rho^2=beta_ext`，`def/L` 是 sign defect 占 exact leverage 的比例。

| `N` | `R` | `C_D` | `C_q` | `rho^2` | `L_ext` | `def/L` |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 3.506 | `1.566e5` | 0.3159 | 118.77 | 0 |
| 32 | 2 | 4.192 | `1.093e5` | 0.2991 | 88.32 | 0 |
| 100 | 2 | 2.955 | `1.188e5` | 0.00909 | 19.12 | 0 |
| 200 | 2 | 6.572 | `1.186e5` | 0.4705 | 92.13 | 0 |
| 8 | 3 | 3.512 | `1.975e7` | 0.00837 | 216.87 | 0 |
| 32 | 3 | 4.195 | `9.204e6` | `8.89e-4` | 44.16 | 0.3791 |
| 100 | 3 | 7.372 | `6.675e6` | 0.6009 | 737.64 | 0 |
| 200 | 3 | 7.303 | `6.341e6` | 0.1619 | 374.95 | 0 |
| 8 | 4 | 3.798 | `4.824e9` | 0.0781 | 9957.84 | 0 |
| 32 | 4 | 5.657 | `8.149e8` | 0.2582 | 6099.21 | 0 |
| 100 | 4 | 12.116 | `4.964e8` | 0.4783 | 4427.17 | 0 |
| 200 | 4 | 15.678 | `3.354e8` | 0.5802 | 3522.87 | 0 |

`C_q` 随 rank 极快放大，而 `rho^2` 从 `8.9e-4` 到 `0.60` 强烈波动，没有
显示式 (21) 所需的 uniform decay。个别小 correlation fraction 解释了某些尺度的
外点 period 降低，但不能外推为渐近结论。

## 6. 计算实现

新增 `endpoint_external_period_capacity_loss_certificate`。它计算 dual capacity Gram、
conditional capacity、correlation fraction、finite positive update loss、Schur-limit
loss及三组 determinant capacities。回归在 `s=0.7` 核对：

1. Sherman--Morrison direct/predicted capacities；
2. finite-loss、Schur-loss 与 signed direct leverage 三者一致；
3. 三个 rank-one determinant lemmas；
4. dual Gram determinant 与 capacity loss 非负。

全部 equalities 在 `1e-42` tolerance 内通过。
