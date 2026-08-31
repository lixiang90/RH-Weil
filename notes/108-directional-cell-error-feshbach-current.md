# Directional cell-error Feshbach current 与 sharpened discrete criterion

文档 107 用 full Loewner relative error 控制 unit-cell projection 对 endpoint
alignment 的影响。该 bound 完全严格，但仍把 cell error 的所有 null directions
都视为 adversarial，有限审计可松至 7 倍。本节证明一个精确的二次 Feshbach
formula：actual/projected canonical representatives 的差只由单个定向 error
current `Z^*E bar v` 驱动。

对 Möbius unit cells，这个 current 是 cumulative charges 的显式 bilinear sum。
用它替代 worst-direction Poincaré gap 后，严格 actual-excess upper 在测试样本中
只松 `1.04--1.46` 倍。

## 1. Projected canonical splitting

令

`W=bar W+E`, `bar W>0`, `E>=0`,                    (1)

并令 `bar v` 是 response constraint `D^*v=1` 下的 minimum-`bar W`
representative。取 columns spanning `ker D^*` 的 `Z`。则

`Z^*bar W bar v=0`.                                (2)

定义

`bar H=Z^*bar WZ`,

`H_W=Z^*WZ=bar H+Z^*EZ`,                           (3)

以及 directional error current

`e=Z^*E bar v`.                                    (4)

### 定理 UR（exact projection-error Feshbach shift）

actual canonical representative 满足

`v_W=bar v-ZH_W^(-1)e`.                            (5)

令

`k_E=-ZH_W^(-1)e`.                                 (6)

则

`D^*k_E=0`,                                        (7)

并且 exact endpoint shift radius 为

`eta_dir^2=C_B k_E^*Bk_E`.                         (8)

两种 excess 满足

`|sqrt(A_W)-sqrt(A_bar)|<=eta_dir`.                (9)

#### 证明

每个 feasible vector 唯一写成 `bar v+Zx`。其 `W`-energy 为

`bar v^*Wbar v+2Re(e^*x)+x^*H_Wx`.                (10)

完成平方给唯一 minimizer `x=-H_W^(-1)e`，即式 (5)。式 (7) 来自
`D^*Z=0`。式 (8) 是定义；式 (9) 对
`sqrt(A)=sqrt(C_B)||v-v_B||_B` 使用 reverse triangle inequality。`□`

与文档 107 定理 UN 不同，式 (5) 不需要先把 `E` majorize 为
`epsilon bar W`，也不损失 error current 的方向信息。

## 2. Directional Green upper

令 projected null endpoint coercivity 为

`bar kappa=lambda_min(bar H,Z^*BZ)`.               (11)

定义 scalar error Green energy

`G_E=e^*bar H^(-1)e`.                              (12)

### 定理 US（directional Green stability）

有

`eta_dir^2<=eta_G^2:=C_BG_E/bar kappa`.            (13)

因此

`sqrt(A_W)<=sqrt(A_bar)+eta_G`.                    (14)

#### 证明

令 `B_0=Z^*BZ`、`x=H_W^(-1)e`。由式 (11)，

`x^*B_0x<=x^*bar Hx/bar kappa`.                    (15)

又 `H_W>=bar H`。写

`H_W=bar H^(1/2)(I+K)bar H^(1/2)`, `K>=0`.         (16)

若 `f=bar H^(-1/2)e`，则

`x^*bar Hx=||(I+K)^(-1)f||^2<=||f||^2=G_E`.       (17)

乘 `C_B` 并使用式 (8) 得式 (13)；再由式 (9) 得式 (14)。`□`

`G_E` 只测量 error 对 projected canonical response class 的 coupling，再由
projected null Green operator传播；对与 `bar v` 正交的巨大 error modes 完全不
收费。

## 3. Möbius charge-current formula

对文档 103 的 unit-cell error，

`E=sum_m theta_m C_mC_m^*`,                        (18)

其中

`theta_m=1/[m(m+1)]-log^2(1+1/m)`.                (19)

### 定理 UT（explicit cumulative-charge forcing current）

directional current 有 exact finite expansion

`e=sum_m theta_m (Z^*C_m)(C_m^*bar v)`.            (20)

因此

`G_E=`

` [sum_m theta_m conjugate(C_m^*bar v) Z^*C_m]^*`

` bar H^(-1)`

` [sum_n theta_n conjugate(C_n^*bar v) Z^*C_n]`.   (21)

#### 证明

把式 (18) 代入定义 `e=Z^*Ebar v` 并交换 finite sum，即得式 (20)；代入式
(12) 得式 (21)。`□`

式 (20) 保留不同 cells 的 vector cancellation；文档 107 的 Loewner/Poincaré
bound 则先取所有方向的 supremum，因而看不到这种 cancellation。

## 4. Sharpened determinant susceptibility transfer

在 `bar W` 上，用文档 106 的 three-capacity probe 构造

`A_hat_bar>=A_bar`.                                 (22)

### 定理 UU（directional cell-current centerline criterion）

定义

`A_dir=(sqrt(A_hat_bar)+eta_G)^2`.                 (23)

则

`A_W<=A_dir`,                                      (24)

并且 minimum-`W` endpoint polynomial 满足

`R_c(P)<=c_1+|target|`

`          *sqrt((R+1)(1+A_dir)/C_B)`.             (25)

若式 (25) 右侧为

`o(sqrt(log N)/loglog(3N))`,                        (26)

则全部 fixed reduced-determinant principal strata 为 `o(1)`；对满足其余
Euler--Tate/Weil package 公理的 zeta function，这迫使 zeros 位于中心线。

#### 证明

定理 US 与式 (22) 给

`sqrt(A_W)<=sqrt(A_bar)+eta_G`

`           <=sqrt(A_hat_bar)+eta_G`.              (27)

平方得式 (24)。再代入文档 100 定理 TM 并应用文档 094 定理 SP。`□`

定理 UU 的全部 quantities 都是 finite arithmetic data：unit-cell determinant
capacities、`bar H`、cumulative charges 与 scalar/vector contractions。它比定理
UQ 严格更定向，不再需要 full Poincaré relative eigenvalue。

## 5. Finite audit

下表仍取 exact `W^sp=W^[0,N^2]`。`diff` 是 observed
`|sqrt(A_W)-sqrt(A_bar)|`；`eta_dir` 是 exact shift norm，`eta_G` 是定理 US
upper；最后一列是定理 UU 的 `A_dir/A_W`。

| `N` | `R` | `diff` | `eta_dir` | `eta_G` | `A_dir/A_W` |
|---:|---:|---:|---:|---:|---:|
| 10 | 2 | 0.0117 | 0.0117 | 0.0119 | 1.120 |
| 10 | 3 | 0.583 | 0.594 | 0.646 | 1.300 |
| 20 | 3 | 0.154 | 0.158 | 0.612 | 1.292 |
| 30 | 2 | 0.181 | 0.181 | 0.182 | 1.288 |
| 30 | 3 | 0.188 | 0.189 | 0.355 | 1.117 |
| 50 | 3 | 0.0766 | 0.137 | 0.696 | 1.274 |
| 100 | 2 | 0.120 | 0.120 | 0.120 | 1.463 |
| 100 | 3 | 0.0745 | 0.0764 | 0.145 | 1.044 |

null dimension 为 1 时，`eta_dir` 与 observed difference 常精确一致；多维时
triangle angle 可再带来小量松弛。与文档 107 的 worst-direction upper
`1.25--7.08` 相比，directional Green upper 统一降至 `1.04--1.46`。

特别值得注意的是：尽管 full relative Poincaré error 约为百分之一，旧 stability
radius 会被极小 `bar kappa` 放大到数十；式 (12) 中 actual error current 对这些
最软 directions 的 pairing 却很小。这正是此前需要的 arithmetic alignment。

## 6. 对经典 RH 的新剩余量

经典 zeta 的 continuous-to-discrete error 现在只剩 scalar Green current

`G_(E,N)=e_N^*bar H_N^(-1)e_N`,                    (28)

其中 `e_N` 由式 (20) 的 cumulative charges 给出。要使定理 UU 达到中心线
阈值，只需联合控制

`sqrt(A_hat_(bar W,N))`

` +sqrt(C_(B,N)G_(E,N)/bar kappa_N)`.              (29)

相较文档 107，式 (29) 把 full error eigenvalue 换成一个 forcing-visible Green
quadratic form。下一步可尝试用 shell cancellation、cell-pair determinant identities
或 incidence recovery 直接估计 `e_N`，而无需改善所有 null directions。

## 7. 计算实现

`endpoint_projection_alignment_stability_certificate` 现额外返回
`error_null_coupling`、`actual_null_metric`、exact `directional_shift`、
`directional_stability_radius`、`directional_green_radius`，以及相应 actual-excess
upper bounds。

回归测试核对 exact representative reconstruction、reverse-triangle bound、
`eta_dir<=eta_G`、directional upper 对 actual excess 的支配，并验证 directional
Green certificate 不劣于先前的 uniform Poincaré certificate；覆盖 null dimensions
1 与 2。
