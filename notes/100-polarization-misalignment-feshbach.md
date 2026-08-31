# Hodge--endpoint polarization misalignment 与 response-zero Feshbach current

文档 098 用 generalized eigenmodes 发现最低 spatial mode 往往主导 endpoint
leverage；文档 099 又把 infinite metric 完全夹在 finite matrices 之间。本节给
剩余 finite alignment 一个更直接的 basis-free 解释：同一 response constraint
在 global Hodge metric `W` 与 endpoint metric `B_c` 中各有一个 canonical
representative。endpoint coefficient explosion 恰好等于这两个 representatives
在 `B_c`-geometry 中的距离。

该距离完全发生在 response-zero subspace `ker D^*`，并由一个 exact Feshbach
formula 给出。于是最低 generalized-mode pairing 被重写为一个明确的
homogeneous Hodge current，而不再需要逐 eigenvector 跟踪。

## 1. 两种 canonical response representatives

令 `W>0` 是 global correction polarization，`B=B_c>0` 是文档 098 的
endpoint polarization，`D!=0` 是 boundary response。定义

`C_W=D^*W^(-1)D`, `C_B=D^*B^(-1)D`,                (1)

`v_W=W^(-1)D/C_W`, `v_B=B^(-1)D/C_B`.              (2)

两者都满足

`D^*v_W=D^*v_B=1`.                                  (3)

### 定理 TJ（two-polarization Pythagorean identity）

令 `k=v_W-v_B in ker D^*`。则

`v_B^*B k=0`,                                       (4)

并有 exact identity

`v_W^*Bv_W=1/C_B+k^*Bk`.                            (5)

定义 dimensionless polarization excess

`A(W,B;D)=C_B k^*Bk>=0`.                            (6)

则两个 representatives 的 `B`-alignment cosine 满足

`cos_B^2(v_W,v_B)=1/(1+A)`.                         (7)

#### 证明

由 `Bv_B=D/C_B` 与 `D^*k=0`，立刻得到式 (4)。展开
`(v_B+k)^*B(v_B+k)`，cross terms 消失，而
`v_B^*Bv_B=1/C_B`，得到式 (5)--(6)。又
`v_B^*Bv_W=1/C_B`，代入 Hilbert-space angle 定义即得式 (7)。`□`

所以 `A=0` 当且仅当两种 polarizations 选择同一个 canonical algebraic
representative；大的 `A` 正是 Hodge geometry 与 local Euler coordinates 的
错位。

## 2. Response-zero Feshbach formula

令 `Z:C^(R-1)->C^R` 的 columns 张成 `ker D^*`。定义

`H=Z^*WZ>0`,

`h=Z^*Wv_B`.                                        (8)

### 定理 TK（exact misalignment Feshbach current）

有

`v_W=v_B-ZH^(-1)h`,                                 (9)

以及

`A=C_B h^*H^(-1)Z^*BZ H^(-1)h`.                    (10)

这些表达式与所选 null basis `Z` 无关。

#### 证明

每个满足式 (3) 的 vector 唯一写成 `v_B+Zx`。其 `W`-energy 是

`v_B^*Wv_B+2Re(h^*x)+x^*Hx`.                        (11)

完成平方给唯一 minimizer `x=-H^(-1)h`。但 response constraint 下的
`W`-minimum 正是 `v_W`，故得到式 (9)。把
`k=-ZH^(-1)h` 代入式 (6) 得式 (10)。更换 null basis 只是 congruence，
不改变 vector `k` 或 quadratic form。`□`

`h` 是 endpoint-minimal representative 投向 response-zero Hodge directions
的 coupling；`H^(-1)` 是这些 homogeneous directions 的 Green operator。
因此式 (10) 是真正的 finite Feshbach obstruction。

## 3. Spatial-shell Feshbach currents

若文档 098 的 spatial decomposition 为

`W^sp=sum_s W_s`,                                   (12)

定义

`H_s=Z^*W_sZ`, `h_s=Z^*W_sv_B`.                    (13)

### 定理 TL（shell-current gluing）

有 exact additive identities

`H=sum_s H_s`, `h=sum_s h_s`,                       (14)

因而

`k=-Z(sum_s H_s)^(-1)(sum_s h_s)`.                 (15)

特别地，shell couplings 的 cancellation 与 accumulated null coercivity 必须
联合分析；只控制 `sum_s||h_s||` 或只控制每个 `lambda_min(H_s)` 都不能单独
决定 misalignment。

#### 证明

式 (14) 来自式 (12) 的线性 pullback；代入定理 TK 即得式 (15)。`□`

这是 spatial Hodge gluing 的 response-zero 版本。不同 shells 可以通过
`h_s` 的相消降低 forcing，也可以通过 `H_s` 的软方向旋转增强 Green
denominator；两种机制必须保留在同一个 Feshbach quotient 中。

## 4. Misalignment-to-Riesz criterion

由文档 098 定理 TB，

`||Ev_W||_(c,1)<=sqrt(R+1)(v_W^*Bv_W)^(1/2)`.       (16)

### 定理 TM（polarization-aligned fixed-determinant criterion）

minimum-`W` mean-zero polynomial 满足

`R_c(P)<=c_1+|t|`

`              *sqrt((R+1)(1+A)/C_B).`             (17)

对 actual infinite metric，文档 099 的 sandwich 进一步给

`A_full<=C_B/(gamma_-C_+)-1`,                       (18)

其中右侧自动非负。若式 (17) 的右侧为

`o(sqrt(log N)/loglog(3N))`，则所有 fixed reduced-determinant principal
strata 为 `o(1)`。

#### 证明

把定理 TJ 式 (5)--(6) 代入式 (16)，再乘 constraint target `t` 并加入 base
endpoint coefficient `c_1`，得到式 (17)。文档 099 定理 TI 的 proof 给
`v_full^*Bv_full<=1/(gamma_-C_+)`；与
`v_full^*Bv_full=(1+A_full)/C_B` 比较即得式 (18)。最后应用文档 094
定理 SP。`□`

相较粗 gap criterion，式 (17) 把目标精确改写为：endpoint capacity `C_B`
必须足够大，且 polarization excess `A` 不能过快增长。

## 5. Finite spatial audit

以下对 exact `W^sp=W^[0,N^2]` 使用 elementary endpoint weights。`cos^2`
是式 (7)，`cancel` 是

`||sum_s h_s||_2/sum_s||h_s||_2`.                  (19)

| `N` | `R` | `C_B` | `A` | `cos^2` | exact `L1` leverage | `cancel` |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 2 | 0.149 | 675 | `1.48e-3` | 103.8 | 0.977 |
| 10 | 3 | 0.202 | 9506 | `1.05e-4` | 371.2 | 0.981 |
| 20 | 3 | 0.222 | 2046 | `4.88e-4` | 162.7 | 0.945 |
| 30 | 2 | 0.143 | 116 | `8.53e-3` | 44.95 | 0.684 |
| 30 | 3 | 0.207 | 46946 | `2.13e-5` | 788.4 | 0.658 |
| 50 | 3 | 0.213 | 880 | `1.14e-3` | 102.7 | 0.940 |
| 100 | 2 | 0.117 | 19.3 | `4.93e-2` | 19.12 | 1.000 |
| 100 | 3 | 0.178 | 34598 | `2.89e-5` | 737.6 | 0.976 |

`R=1` 时 response affine hyperplane 是单点，故恒有 `A=0`；这正是 quadratic
gauge 的 scalar rigidity。`R>=2` 时 excess 大且强烈振荡。多数样本的 shell
couplings 几乎同向，说明不能普遍期待仅靠 dyadic cancellation 消除 forcing；
`N=30` 的部分相消也不足以抵消很软的 null Green operator。

因此下一步的精确 arithmetic target 是式 (10) 或 (15)：利用 Möbius--Farey
determinant structure 联合控制

`h^*H^(-1)(Z^*BZ)H^(-1)h`,                         (20)

而不是分别估计 Gram 最小本征值、capacity 或 shell coupling absolute mass。

## 6. 广义结构解释

在 generalized Weil/Hodge package 中，`W` 是 global polarization，`B` 是由
local Euler coordinates 拉回的 arithmetic polarization，`D` 是 distinguished
Tate/trace functional。定理 TJ--TK 表明，结构存在性的定向条件是两种
polarizations 对 Tate affine class 选择近似相同的 canonical representative。

这提供一个比“统一 norm equivalence”弱得多的广义公理：只要求单个
distinguished affine class 的 polarization misalignment 消失或受控，而允许
response-zero complement 有任意坏 condition number。定理 TM 将该公理直接
接到 zeta fixed-determinant stability。

## 7. 计算实现

`scripts/qw_matrix.py` 新增
`endpoint_polarization_alignment_certificate`，返回两种 canonical
representatives、endpoint excess、alignment cosine、null basis、Feshbach
metric/coupling/shift 与 exact Riesz leverage。

`endpoint_spatial_shell_coercivity` 进一步返回逐 shell `H_s,h_s` 与 coupling
cancellation ratio。回归测试核对 constraint normalization、Pythagorean
identity、Feshbach reconstruction、shell-current additivity，以及 `W=B` 时
excess 精确为零。
