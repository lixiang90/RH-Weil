# Positive rank-update charge-kernel compression

文档 111--112 将 exact spatial metric 统一约化到 finite-head metric

`W_M=bar W+UTheta U^*`,                            (1)

其中 `U` 的 columns 是前 `M-1` 个 cumulative-charge vectors，`Theta` 是 positive
cell-variance diagonal。本节用 Woodbury 与 matrix determinant lemma 把 finite-head
capacity、null determinant 与 three-capacity susceptibility 精确压缩到 charge
kernels。于是剩余算术问题可直接表述为有限 charge contractions 的谱估计。

## 1. Abstract positive update

令 `X>0`，`D` 为 response vector，`U: C^m -> V`，`Theta>0`，并定义

`Y=X+UTheta U^*`.                                 (2)

记

`K_X=Theta^(-1)+U^*X^(-1)U`,                     (3)

`r_X=U^*X^(-1)D`,                                 (4)

`c_X=D^*X^(-1)D`.                                 (5)

### 定理 VH（response charge-kernel formula）

有

`Y^(-1)=X^(-1)-X^(-1)UK_X^(-1)U^*X^(-1)`,        (6)

以及 exact response-capacity formula

`C_Y=c_X-r_X^*K_X^(-1)r_X`.                       (7)

特别地，inverse capacity 是

`delta_Y=[c_X-r_X^*K_X^(-1)r_X]^(-1)`.            (8)

#### 证明

式 (6) 是 Woodbury identity；左右以 `D` contraction 得式 (7)，取 reciprocal
得式 (8)。`□`

式 (7) 把 full-space inverse problem分成 base solve `X^(-1)` 与一个 `m x m`
positive charge kernel。所有 head corrections 的 interaction，包括 cross-cell
cancellation，都保留在 `K_X^(-1)` 中。

## 2. Metric and null determinants

取 `Z` spanning `ker D^*`，令

`H_X=Z^*XZ`, `U_0=Z^*U`,                          (9)

`K_(X,0)=Theta^(-1)+U_0^*H_X^(-1)U_0`.           (10)

### 定理 VI（metric/null determinant compression）

有

`det Y=det X det Theta det K_X`,                  (11)

`det(Z^*YZ)=det H_X det Theta det K_(X,0)`.       (12)

因此 adapted determinant quotient

`det(Q^*YQ)/det(Z^*YZ)=delta_Y`                   (13)

可完全由式 (8)、(11)--(12) 交叉认证。

#### 证明

matrix determinant lemma 给

`det(X+UTheta U^*)`

` =det X det(I+Theta U^*X^(-1)U)`

` =det X det Theta det K_X`，                     (14)

即式 (11)。对 null restriction
`H_X+U_0Theta U_0^*` 重复同一证明得式 (12)。式 (13) 是 response-coordinate
Schur complement identity。`□`

## 3. Three-kernel susceptibility

令 `B_perp` 是文档 106 的 canonical transversal endpoint block，并取 `t>0`
使

`X_j=X+jtB_perp>0`, `j in {-1,0,1}`。             (15)

对每个 `j` 定义

`K_j=Theta^(-1)+U^*X_j^(-1)U`,                   (16)

`r_j=U^*X_j^(-1)D`, `c_j=D^*X_j^(-1)D`,          (17)

`delta_j=(c_j-r_j^*K_j^(-1)r_j)^(-1)`.           (18)

### 定理 VJ（three-charge-kernel Weil criterion）

finite-head centered susceptibility upper 恰为

`A_hat_M=C_B(delta_1-delta_(-1))/(2t)`.           (19)

令文档 111 的 uniform variance-tail correction 为

`eta_M^2=C_Bepsilon_M^2/(2C_Mkappa_M)`,           (20)

其中 `epsilon_M=7/[3pi^2(M-1)]`。则

`A_W<=(sqrt(A_hat_M)+eta_M)^2`.                   (21)

若由式 (18)--(21) 得到的 Riesz upper 是

`o(sqrt(log N)/loglog(3N))`,                       (22)

则 fixed reduced-determinant strata 为 `o(1)`；在其余 Euler--Tate/Weil package
公理下，相应 zeta function 的 zeros 位于中心线。

#### 证明

对三个 base forms `X_j` 分别应用定理 VH，式 (18) 就是 updated forms
`Y_j=X_j+UTheta U^*` 的 inverse capacities。文档 106 定理 UL 给式 (19) 对
finite-head excess 的 upper；文档 111 定理 VD 给 tail transfer (21)。最后应用文档
100 定理 TM 与文档 094 定理 SP。`□`

定理 VJ 将 finite-head centerline condition 改写为三个 charge kernels
`K_-、K_0、K_+` 的 resolvent contractions。对其他 zeta/L-function，只要其 positive
corrections 也具有式 (2) 的 Gram factorization，同一 algebraic proof 原样适用。

## 4. Möbius specialization

在本项目中，

`U=[C_1,...,C_(M-1)]`,                            (23)

`Theta=diag(theta_1,...,theta_(M-1))`.             (24)

所以 kernel entries 是显式 finite arithmetic contractions

`(K_j)_(mn)=delta_(mn)/theta_m+C_m^*X_j^(-1)C_n`, (25)

response current 是

`(r_j)_m=C_m^*X_j^(-1)D`.                         (26)

剩余 susceptibility 问题遂等价于控制式 (25) 的 positive inverse quadratic forms，
而非 opaque full metric inverse。

## 5. Finite audit

对多个 finite-head samples，直接 full-matrix computation 与 charge-kernel prediction
的 relative residual 如下（50-digit arithmetic）：

| `N` | `R` | `M` | kernel rank | capacity residual | metric-det residual | null-det residual |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 4 | 3 | 7.2e-50 | 1.4e-49 | 3.3e-51 |
| 12 | 3 | 5 | 4 | 9.8e-50 | 3.8e-48 | 6.4e-50 |
| 20 | 3 | 8 | 7 | 1.3e-50 | 1.6e-48 | 5.0e-50 |
| 30 | 3 | 16 | 15 | 4.1e-49 | 1.9e-48 | 5.1e-51 |

回归还分别对 `X+/-tB_perp` 验证式 (18)，其 kernel inverse capacities 与直接
three-capacity computation 在 `1e-45` tolerance 内一致。

## 6. 计算实现

新增 `positive_rank_update_response_kernel_certificate`，返回 charge/response
kernels、Woodbury capacity、metric determinant、null determinant 及 direct
cross-check。`mobius_unit_cell_tail_projection_certificate` 现同时返回 head charge
columns、variance weights 与 kernel certificate。回归覆盖 central 与 `+/-t`
三种 metrics。
