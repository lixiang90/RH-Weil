# Response-zero 广义谱与 transversal Hodge completion

文档 100 已把 endpoint coefficient explosion 精确写成 `ker D^*` 上的
Feshbach quotient。本节进一步把这个 quotient 完全谱化，并给出一个正的
transversal Hodge completion：它不改变 distinguished response class，只增强
齐次方向的 polarization，而且其对 misalignment 的作用有闭式公式。

这一步把剩余存在性问题分成两个可独立审计的量：response-zero generalized
coercivity 与 endpoint-minimal representative 产生的 spectral forcing。它也说明
需要构造的并非全空间上的 uniform spectral gap，而是一个只作用于
`ker D^*`、且不重新注入 forcing 的正 Hodge block。

## 1. Null-space whitening

沿用文档 100 的记号。令 `W>0`、`B>0`、`D!=0`，并令

`C_B=D^*B^(-1)D`, `v_B=B^(-1)D/C_B`.              (1)

取任意满列秩矩阵 `Z`，其像为 `ker D^*`，并定义

`H=Z^*WZ`, `B_0=Z^*BZ`, `h=Z^*Wv_B`.              (2)

取 Cholesky 分解 `B_0=LL^*`，令

`K_0=L^(-1)H L^(-*)`, `f=L^(-1)h`.                (3)

设 `K_0u_i=lambda_i u_i`，其中 `u_i` 标准正交、`lambda_i>0`，再令

`g_i=u_i^*f`.                                      (4)

### 定理 TN（null spectral Feshbach identity）

文档 100 的 dimensionless polarization excess 满足 exact identity

`A(W,B;D)=C_B sum_i |g_i|^2/lambda_i^2`.           (5)

令

`F_0=h^*B_0^(-1)h=sum_i|g_i|^2`,

`kappa_0=lambda_min(H,B_0)=min_i lambda_i`.         (6)

则

`A<=C_B F_0/kappa_0^2`.                            (7)

式 (5)--(7) 与 null basis `Z` 及 Cholesky factor 的选择无关。

#### 证明

由文档 100 定理 TK，null coordinate 为 `x=-H^(-1)h`，且

`A=C_B x^*B_0x`.                                   (8)

写 `y=L^*x`。由式 (3)，

`y=-K_0^(-1)f=-sum_i g_i u_i/lambda_i`.            (9)

而 `x^*B_0x=||L^*x||^2=||y||^2`，故式 (5) 成立。
同理 `F_0=||L^(-1)h||^2=sum_i|g_i|^2`；以
`lambda_i>=kappa_0` 逐项估计式 (5) 得式 (7)。更换 `Z` 或 Cholesky factor
只对同一两个内积空间作坐标变换，式 (8) 与 generalized spectrum 的 spectral
measure 不变。`□`

所以粗 bound 的松弛可精确分成两类：`kappa_0` 是否过小，以及 forcing mass
是否落在最低 generalized modes 上。仅有小 `F_0` 并不足够，因为 Green
operator 在式 (5) 中出现二次。

## 2. Canonical transversal completion

定义 affine response hyperplane 到其 homogeneous tangent space 的投影

`P=I-v_BD^*`.                                      (10)

它满足 `P^2=P`、`Pv_B=0`、`PZ=Z`。定义 positive semidefinite form

`B_perp=P^*BP`,                                    (11)

以及 completion flow

`W_tau=W+tau B_perp`, `tau>=0`.                    (12)

### 定理 TO（transversal Hodge completion flow）

对式 (12)，endpoint representative `v_B`、`C_B` 与 null forcing `h` 均不变；
null generalized eigenvalues 作纯平移

`lambda_i(tau)=lambda_i+tau`,                       (13)

而 spectral forcing `g_i` 不变。因此

`A(tau)=C_B sum_i |g_i|^2/(lambda_i+tau)^2`.        (14)

特别地，若 `h!=0`，则

`A'(tau)=-2C_B sum_i |g_i|^2/(lambda_i+tau)^3<0`,   (15)

并且

`A(tau)<=C_B F_0/(kappa_0+tau)^2`.                 (16)

#### 证明

`Pv_B=0` 给 `Z^*B_perp v_B=0`，所以 completion 不改变 `h`。另一方面
`PZ=Z` 给

`Z^*B_perp Z=Z^*BZ=B_0`.                           (17)

故 null pencil 从 `(H,B_0)` 变成 `(H+tau B_0,B_0)`；白化后恰为
`K_0+tau I`。式 (13)--(14) 由定理 TN 得到，逐项求导与估计即得
式 (15)--(16)。`□`

这个 completion 是“无 forcing 的纯横向极化”：它在 distinguished affine
representative 上为零，在每个 response-zero direction 上恰复制 endpoint
metric。任意在全空间直接加入 `tau B` 会同时改变 coupling，因此没有式
(13)--(14) 的刚性。

## 3. Fixed-determinant 结构定理

记文档 094 的 weighted endpoint Riesz norm 为 `R_c`，方向数为 `R`，constraint
target 为 `t`，base endpoint coefficient 为 `c_1`。

### 定理 TP（coercivity--forcing Riesz criterion）

minimum-`W` correction 满足

`R_c(P)<=c_1+|t| sqrt((R+1)/C_B`

`                    * (1+C_B F_0/kappa_0^2)).`    (18)

对 completed metric `W_tau`，右侧可将 `kappa_0` 替换为
`kappa_0+tau`。若所得右侧为

`o(sqrt(log N)/loglog(3N))`,                        (19)

则文档 094 的全部 fixed reduced-determinant principal strata 为 `o(1)`。

#### 证明

文档 100 定理 TM 给

`R_c(P)<=c_1+|t|sqrt((R+1)(1+A)/C_B)`.             (20)

把定理 TN 的式 (7) 代入即得式 (18)；completed 情形用定理 TO 的式 (16)。
最后应用文档 094 定理 SP。`□`

### 推论 TQ（transversal-completion centerline package）

设某个 Euler--Tate zeta package 除中心线外的证明已归约为文档 094 的
fixed-determinant stability。若其 actual positive Hodge metric 可写成

`W_N=W_N^(0)+tau_N P_N^*B_NP_N`,                   (21)

且由 `W_N^(0)` 得到的 `C_(B,N),F_(0,N),kappa_(0,N)` 使式 (18)--(19)
成立，则该 package 的对应 zeta zeros 位于中心线。

这是真正的充分结构定理，但不是经典 RH 的现成证明：对 zeta，式 (21) 中
具有所需强度的 arithmetic transversal block 尚未构造。任意人为把
`tau_NP_N^*B_NP_N` 加进 optimization 会改变问题本身；它必须来自 actual
Nyman--Beurling / Möbius--Farey Gram、一个同构的 cohomological completion，
或可证明支配该 form 的真实正算术能量。

## 4. Exact finite audit

下表使用 exact spatial metric `W^sp=W^[0,N^2]` 与 elementary endpoint
weights。`upper/A` 是式 (7) 与 exact excess 的比；`mode_1` 是最低 null mode
对式 (5) 的贡献比例。

| `N` | `R` | `kappa_0` | `F_0` | `A` | `upper/A` | `mode_1` |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 2 | `3.01e-5` | `4.12e-6` | 675 | 1.00 | 1.000 |
| 10 | 3 | `1.33e-7` | `1.02e-5` | 9506 | 12262 | 0.959 |
| 20 | 3 | `2.50e-7` | `9.22e-6` | 2046 | 15955 | 0.827 |
| 30 | 2 | `2.21e-5` | `3.98e-7` | 116 | 1.00 | 1.000 |
| 30 | 3 | `5.36e-7` | `2.11e-6` | 46946 | 32.5 | 0.997 |
| 50 | 3 | `3.60e-7` | `8.36e-6` | 880 | 15582 | 0.649 |
| 100 | 2 | `2.05e-5` | `6.92e-8` | 19.3 | 1.00 | 1.000 |
| 100 | 3 | `1.06e-6` | `2.73e-7` | 34598 | 1.25 | 0.9999 |

`R=2` 的 null space 为一维，所以式 (7) 恒为等式。`R=3` 时单独使用
`kappa_0` 可非常浪费；式 (5) 的 forcing-weighted spectral measure 才是正确
对象。尽管 `F_0` 很小，`kappa_0` 更小，因而仍产生大的 excess。

为展示式 (14) 的相对尺度，下表给 `tau=m kappa_0` 后的
`A(tau)/A(0)`：

| `N,R` | `m=1` | `m=10` | `m=100` |
|---:|---:|---:|---:|
| 10,2 | 0.250 | 0.00826 | `9.80e-5` |
| 10,3 | 0.281 | 0.0478 | 0.0296 |
| 20,3 | 0.378 | 0.169 | 0.0978 |
| 30,3 | 0.252 | 0.0105 | `8.20e-4` |
| 50,3 | 0.510 | 0.325 | 0.161 |
| 100,3 | 0.250 | 0.00834 | `1.09e-4` |

一维 null space 时比值精确为 `(1+m)^(-2)`。多维偏离这个曲线的量直接测量
forcing 在较高 null modes 上的质量。

## 5. 对经典 RH 存在性问题的收缩

文档 099 已把 infinite tail 夹在显式 finite metrics 之间；本节进一步说明最理想
的 missing structure 是 actual arithmetic realization of `B_perp`。可行路线现在
可精确表述为以下三者之一：

1. 在 Möbius--Farey spatial Gram 中证明一组真实 blocks 的 pullback 至少支配
   `tau_N B_0`，并证明这些 blocks 对 `v_B` 的 coupling 足够小；
2. 构造一个 cohomological/adelic completion，其正 intersection form 经比较
   映射恰给 `P^*BP`，同时保持原 zeta determinant；
3. 不构造完整 block，而直接证明 spectral sum
   `sum_i|g_i|^2/lambda_i^2` 满足式 (19) 所需界。

第一条是最可计算的 finite target，第二条最接近 Weil 猜想的几何机制，第三条
是最弱的定向充分条件。当前数据只验证公式，不提供其中任何一个渐近界；因此
这里没有循环地宣称 RH 已证。

## 6. 计算实现

`scripts/qw_matrix.py` 的
`endpoint_polarization_alignment_certificate` 现返回 null endpoint mass、
generalized eigenvalues、spectral forcing、dual forcing mass、coercivity、
coercive upper bound 与逐 mode excess contributions。

新增 `endpoint_transversal_hodge_completion`，构造式 (10)--(12)，并同时返回
直接重算的 excess 与式 (14) 的 spectral prediction。回归测试核对 upper bound、
mode decomposition、completion monotonicity 与 exact shifted-spectrum identity。
