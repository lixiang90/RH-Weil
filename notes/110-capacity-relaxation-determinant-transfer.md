# Capacity-relaxation determinant transfer

文档 108 的 directional route 使用 projected Green energy

`G_E=e^*bar H^(-1)e`，

文档 109 的 positive route 则用 balanced Schur bound 取代它。本节给第三种、在
finite audit 中几乎与 directional route 一样尖锐的描述：canonical representative
适应 cell error 所获得的 energy relaxation，恰等于一个 positive cell energy 与
两个 inverse capacities 之差。因而不需要显式形成 signed vector current 或求解
projected Green equation。

## 1. Cell-amplitude capacity path

令

`W_s=bar W+sE`, `0<=s<=1`,                        (1)

其中

`0<=E<=epsilon bar W`.                            (2)

令 `bar v` 是约束 `D^*v=1` 下的 minimum-`bar W` representative，`Z` 的
columns 张成 `ker D^*`。记

`delta(s)=C(W_s)^(-1)`, `delta_0=delta(0)`,        (3)

`bar H=Z^*bar WZ`, `E_0=Z^*EZ`,                  (4)

`e=Z^*Ebar v`, `q=bar v^*Ebar v`.                 (5)

取 square adapted basis

`Q=[bar v,Z]`.                                    (6)

因为 `Z^*bar Wbar v=0`，

`Q^*W_sQ=`

` [[delta_0+sq, se^*],`

`  [se, bar H+sE_0]]`.                            (7)

### 定理 UY（capacity-relaxation identity）

对每个 `0<=s<=1`，

`delta(s)=delta_0+sq`

`          -s^2 e^*(bar H+sE_0)^(-1)e`,           (8)

并且有 determinant quotient

`delta(s)=det(Q^*W_sQ)/det(bar H+sE_0)`.           (9)

特别地，

`delta'(0)=q`, `delta''(0)=-2G_E`,                (10)

其中 `G_E=e^*bar H^(-1)e`。在 actual endpoint `s=1`，定义 capacity
relaxation energy

`R_E=q-[delta(1)-delta(0)]`.                       (11)

则

`R_E=e^*(bar H+E_0)^(-1)e>=0`.                    (12)

#### 证明

约束 `D^*v=1` 下的每个 vector 唯一写成 `bar v+Zx`。式 (7) 对 lower-right
block 取 Schur complement，得到式 (8)。同一个 Schur complement 的 determinant
identity 给式 (9)。在 `s=0` 对式 (8) 微分得到式 (10)；取 `s=1` 并整理即得
式 (11)--(12)。`□`

式 (11) 有直接的变分解释：`delta_0+q` 是把 projected minimizer `bar v`
原封不动代入 actual metric 的 energy；`delta(1)` 是重新最小化后的 energy；两者
之差就是允许 null correction 后释放的能量。

## 2. Relaxation versus projected Green energy

### 定理 UZ（near-isometry of relaxation and Green energy）

在式 (2) 下，

`R_E<=G_E<=(1+epsilon)R_E`.                       (13)

#### 证明

式 (2) 在 null block 上给

`bar H<=bar H+E_0<=(1+epsilon)bar H`.              (14)

取 inverse 后次序反转：

`(1+epsilon)^(-1)bar H^(-1)`

` <=(bar H+E_0)^(-1)<=bar H^(-1)`.                (15)

左右以 `e` contraction，再用式 (12)，即得式 (13)。`□`

所以当 unit-cell relative error 只有百分之几时，两个 scalar 自动在同样百分比内；
这不是数值偶然，而是 Loewner order 的直接结果。

## 3. Capacity-only endpoint stability

令 `B_0=Z^*BZ`。定义 actual/projected null coercivities

`kappa_W=lambda_min(bar H+E_0,B_0)`,              (16)

`bar kappa=lambda_min(bar H,B_0)`.                (17)

显然

`kappa_W>=bar kappa`.                             (18)

文档 108 的 exact representative shift 是

`k_E=-Z(bar H+E_0)^(-1)e`.                        (19)

### 定理 VA（capacity-relaxation endpoint criterion）

定义

`eta_cap,W^2=C_BR_E/kappa_W`,                     (20)

`eta_cap,bar^2=C_BR_E/bar kappa`.                 (21)

则 exact shift radius 满足

`eta_dir<=eta_cap,W<=eta_cap,bar<=eta_G`,         (22)

其中 `eta_G^2=C_BG_E/bar kappa` 是文档 108 的 Green upper。

若 `A_hat_bar` 是 projected three-capacity susceptibility upper，令

`A_cap,W=(sqrt(A_hat_bar)+eta_cap,W)^2`.           (23)

则

`A_W<=A_cap,W`.                                   (24)

因此 minimum-`W` endpoint polynomial 满足

`R_c(P)<=c_1+|target|`

`          *sqrt((R+1)(1+A_cap,W)/C_B)`.          (25)

若式 (25) 是

`o(sqrt(log N)/loglog(3N))`,                       (26)

则 fixed reduced-determinant principal strata 全部为 `o(1)`；在其余
Euler--Tate/Weil package 公理下，相应 zeta function 的 zeros 位于中心线。

#### 证明

令 `x=(bar H+E_0)^(-1)e`。由式 (16)，

`x^*B_0x<=x^*(bar H+E_0)x/kappa_W`

`        =R_E/kappa_W`.                           (27)

乘 `C_B` 给第一项 inequality。式 (18) 给第二项；定理 UZ 给第三项。文档 108
定理 UR 的 reverse triangle inequality 与 `A_bar<=A_hat_bar` 给式 (24)。最后
代入文档 100 定理 TM 与文档 094 定理 SP，即得式 (25)--(26)。`□`

式 (11)、(9)、(16) 表明定理 VA 的输入全是 finite scalar/determinant/generalized-
eigenvalue data：

`q`, `C(bar W)`, `C(W)`, `kappa_W`, `A_hat_bar`.   (28)

没有 signed Green solve；尤其

`R_E=q-[det(Q^*WQ)/det(Z^*WZ)`

`       -det(Q^*bar WQ)/det(Z^*bar WZ)]`.          (29)

## 4. Möbius unit-cell specialization

对

`E=sum_m theta_mC_mC_m^*`，                       (30)

有 positive formula

`q=sum_m theta_m|C_m^*bar v|^2`.                  (31)

所以 `R_E` 是 positive cell response energy 与 inverse-capacity increment 的
exact deficit。虽然式 (11) 是两项相减，但半正定性先验保证 `R_E>=0`，定理 UZ
又给独立 condition check

`R_E<=G_E<=(1+epsilon)R_E`.                       (32)

在渐近论证中，可以用 determinant identities 直接估计式 (29)，也可用式 (32)
与 directional current 交叉认证。

## 5. Finite audit

下表仍用 `W=W^[0,N^2]`。`R_E/G_E` 显示 capacity relaxation 与 projected
Green energy 的接近程度；两种 radii 分别使用 actual/projected coercivity；最后
一列是定理 VA 的 `A_cap,W/A_W`。

| `N` | `R` | `R_E/G_E` | `eta_dir` | `eta_cap,W` | `eta_cap,bar` | `A_cap,W/A_W` |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 2 | 0.9848 | 0.0117 | 0.0117 | 0.0118 | 1.1198 |
| 10 | 3 | 0.9954 | 0.594 | 0.641 | 0.644 | 1.2995 |
| 20 | 3 | 0.9908 | 0.158 | 0.607 | 0.609 | 1.2915 |
| 30 | 2 | 0.9935 | 0.181 | 0.181 | 0.181 | 1.2876 |
| 30 | 3 | 0.9854 | 0.189 | 0.351 | 0.353 | 1.1166 |
| 50 | 3 | 0.9888 | 0.137 | 0.691 | 0.692 | 1.2732 |
| 100 | 2 | 0.9979 | 0.120 | 0.120 | 0.120 | 1.4627 |
| 100 | 3 | 0.9905 | 0.0764 | 0.144 | 0.145 | 1.0436 |

`R_E/G_E` 位于 `0.985--0.998`，与定理 UZ 的百分级 guarantee 一致。strict
actual-coercivity upper 只松 `1.0436--1.4627`，逐样本不劣于文档 108 的
projected Green upper；null dimension 为 1 时，`eta_cap,W=eta_dir` 精确成立。

## 6. 对经典 RH 的剩余量

定理 VA 把 continuous-to-discrete transfer 的 signed inverse problem 换成

`R_(E,N)=q_N-[C(W_N)^(-1)-C(bar W_N)^(-1)]`.      (33)

新的 determinant-relaxation 充分条件是

`sqrt(A_hat_(bar W,N))`

` +sqrt(C_(B,N)R_(E,N)/kappa_(W,N))`

` =o(sqrt(log N)/loglog(3N))`.                     (34)

这仍未证明经典 RH：缺失的是式 (34) 的统一渐近率。但它把所需输入缩成 positive
cell sum、两个 capacity determinant quotients 与一个 generalized eigenvalue，因而
提供了比显式 Green inverse 更适合 arithmetic determinant identities 的目标。

## 7. 计算实现

`endpoint_projection_alignment_stability_certificate` 现返回
`capacity_relaxation_energy`、actual/projected-coercivity radii 与 excess uppers，
并在 adapted basis 中独立计算 actual/projected determinant inverse capacities。
回归测试验证式 (9)、(13)、(22)、(24)，覆盖 null dimensions 1 与 2。
