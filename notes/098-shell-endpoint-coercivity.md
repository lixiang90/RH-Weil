# Shell endpoint coercivity 与 response generalized spectral measure

文档 097 把 infinite correction Gram 化成 exact spatial Gram `W^sp` 与一个很小的
far completion，但 phase-box bound 仍逐 matrix entry 取绝对值，数值上相当松。
本节改用与 endpoint map 精确匹配的 quadratic mass。这样不仅得到更内在的
leverage bound，还能把 canonical response 在 generalized eigenmodes 上逐项
分解，直接识别哪些低能方向真正造成 coefficient explosion。

结果显示：不相交 spatial shells 之间存在正的 coercivity rotation gain；同时，
最低 generalized mode 往往占 endpoint `L2` leverage 的绝大部分，即使它对
capacity 的贡献并不总是大。下一步因此缩成一个具体的最低模 arithmetic
alignment 问题。

## 1. Endpoint quadratic mass

沿用文档 095 的 endpoint transform

`E:C^R -> C^(R+1)`                                 (1)

与 positive analytic weights `c_1,...,c_(R+1)`。定义

`B_c=E^*diag(c_ell^2)E`.                            (2)

### 定理 TB（quadratic endpoint coercivity form）

`B_c>0`，并且对所有 jet coefficients `alpha`，

`||Ealpha||_(c,2)^2=alpha^*B_c alpha`,              (3)

`||Ealpha||_(c,1)`

` <=sqrt(R+1)(alpha^*B_c alpha)^(1/2)`.             (4)

#### 证明

文档 095 定理 SQ 的 binomial matrix `E` 有 full column rank；positive diagonal
weights 保持 rank，所以式 (2) 正定。式 (3) 是定义，式 (4) 是有限维
Cauchy--Schwarz。`□`

相较 phase-box norm，`B_c` 不丢失 endpoint columns 之间的符号与相位关系。

## 2. Spatial-shell coercivity 与 rotation gain

对任意 correction Gram `W>0` 定义 generalized endpoint coercivity

`gamma(W;B_c)=inf_(alpha!=0)`

`                 alpha^*Walpha/(alpha^*B_calpha)`. (5)

等价地，`gamma(W;B_c)` 是 pencil `(W,B_c)` 的最小 generalized eigenvalue，
并且

`W>=gamma(W;B_c)B_c`.                               (6)

把 `0<y<N^2` 分成不相交整数 shells `I_s`，由文档 097 得

`W^sp=sum_s W_s`, `W_s>=0`.                         (7)

### 定理 TC（shell superadditivity and Hodge rotation）

令 `gamma_s=gamma(W_s;B_c)`，允许 singular shell 时 `gamma_s=0`。则

`gamma(W^sp;B_c)>=sum_s gamma_s`.                   (8)

差值

`Gamma_rot=gamma(W^sp;B_c)-sum_s gamma_s>=0`        (9)

称为 shell rotation gain。它严格为正恰表示不同 shells 的最低 endpoint-energy
directions 不能由同一个 coefficient vector 同时实现。

#### 证明

每个 shell 由式 (6) 满足 `W_s>=gamma_sB_c`。求和给
`W^sp>=(sum_s gamma_s)B_c`，再用式 (5) 即得式 (8)--(9)。`□`

这是一个 finite Hodge gluing mechanism：每个 shell 可以有很软的方向，但若
软方向随尺度旋转，总 polarization 仍获得额外 coercivity。

## 3. Canonical response 的 exact generalized spectral measure

令 `B_c=LL^*` 为 Cholesky factorization，并置

`K=L^(-1)W L^(-*)`.                                 (10)

取 orthonormal diagonalization

`K u_i=gamma_i u_i`, `0<gamma_1<=...<=gamma_R`,     (11)

以及 transformed response coordinates

`d_i=u_i^*L^(-1)D`.                                 (12)

仍记

`C=D^*W^(-1)D`,

`v=W^(-1)D/C`.                                      (13)

### 定理 TD（response generalized spectral identities）

有 exact formulas

`C=sum_i |d_i|^2/gamma_i`,                          (14)

`v^*B_cv`

` =[sum_i |d_i|^2/gamma_i^2]`

`   /[sum_i |d_i|^2/gamma_i]^2.                    (15)

因此可分别定义 capacity spectral weights

`p_i^cap=(|d_i|^2/gamma_i)/C`                       (16)

与 endpoint-leverage spectral weights

`p_i^end=(|d_i|^2/gamma_i^2)`

`          /sum_k |d_k|^2/gamma_k^2`;              (17)

两组 weights 都非负且和为 `1`，但一般并不相同。

#### 证明

由式 (10)，

`W=L K L^*`, `W^(-1)=L^(-*)K^(-1)L^(-1)`.          (18)

把 `L^(-1)D=sum_i d_i u_i` 代入 capacity，得到式 (14)。另一方面

`L^*v=K^(-1)L^(-1)D/C`，                           (19)

而 `v^*B_cv=||L^*v||^2`；逐 eigenmode 展开即得式 (15)。`□`

式 (15) 比只看 `gamma_1` 精确：最软 mode 只有在 `d_1` 不够小时才控制
canonical endpoint coefficients。

## 4. Quadratic leverage certificate

由式 (6) 与 `v^*Wv=1/C`，

`v^*B_cv<=1/[gamma(W;B_c)C]`.                       (20)

### 定理 TE（shell-coercive fixed-determinant criterion）

minimum-metric endpoint polynomial 满足

`R_c(P)<=c_1+|t|sqrt((R+1)/(gamma(W;B_c)C)).`       (21)

对文档 097 的 decomposition，若 `eta_N^#` 是 far relative majorant，则

`R_c(P_N)<=c_1+|t_N|`

` *sqrt((R+1)(1+eta_N^#)/(gamma_sp C_sp)),`         (22)

其中 `gamma_sp=gamma(W^sp;B_c)`。若式 (22) 右侧为

`o(sqrt(log N)/loglog(3N))`，则每个 fixed reduced-determinant principal
window 的 contribution 为 `o(1)`。

#### 证明

式 (4)、(20) 与 `alpha_min=tv` 给式 (21)。文档 097 的 far comparison 给
`W>=W^sp`，故 `gamma(W;B_c)>=gamma_sp`；又给
`C>=C_sp/(1+eta_N^#)`。代入式 (21) 得式 (22)。最后使用文档 094 定理 SP。
`□`

式 (22) 是 phase-box certificate 的 quadratic refinement；两个都是充分条件，
但这里把 endpoint cancellation 保留到最后一步，仅支付 unavoidable
`sqrt(R+1)`。

## 5. Dyadic-shell finite audit

取 shells

`[0,N],[N,2N],[2N,4N],..., [.,N^2]`.                (23)

下表使用 elementary weights `c_ell=ell`。`rot` 是
`Gamma_rot/gamma_sp`；`p_1^cap,p_1^end` 是最低 mode 在式 (16)--(17) 中的
比例：

| `N` | `R` | `gamma_sp` | `rot` | `p_1^cap` | `p_1^end` | exact `L1` leverage |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 2 | `1.95e-5` | 5.1% | 35.4% | 99.94% | 103.8 |
| 20 | 3 | `2.48e-7` | 26.3% | 0.80% | 83.0% | 162.7 |
| 30 | 2 | `2.10e-5` | 12.7% | 5.0% | 99.23% | 44.95 |
| 30 | 3 | `3.39e-7` | 27.1% | 36.8% | 99.89% | 788.4 |
| 50 | 3 | `3.59e-7` | 22.3% | 0.44% | 65.1% | 102.7 |
| 100 | 2 | `2.03e-5` | 13.2% | 0.99% | 95.2% | 19.12 |
| 100 | 3 | `4.21e-7` | 15.5% | 60.4% | 99.998% | 737.6 |

这些数据说明：

1. shell rotation gain 是真实且可观测的，最高约占 total coercivity 的四分之一；
2. capacity 可以主要来自较硬 modes，但 endpoint `L2` leverage 仍几乎完全由
   最低 mode 控制；
3. exact `L1` leverage 随 `N` 强烈振荡，不能由单调 capacity 解释。

因此下一步不应只估计 `gamma_sp` 或 `C_sp` 的乘积。更锐的目标是直接控制
式 (15) 的 arithmetic spectral measure，特别是最低 generalized eigenvector
与 Möbius response `D_N` 的 pairing `d_1`。这正是一个 finite parabolic
Feshbach alignment quantity。

## 6. 广义 Hodge 结构中的意义

对一般 polarized algebraic synthesis，`B_c` 表示由 local Euler/conductor
coordinates 拉回的 endpoint polarization，`W` 表示 global Hodge
polarization。pencil `(W,B_c)` 的 generalized eigenmodes 就是“global energy
相对于 local arithmetic complexity”的 Hodge slopes。定理 TC 给 spatial
gluing，定理 TD 给 Tate/response class 在这些 slopes 上的谱测度，定理 TE
则把该谱测度接到中心线所需的 local stability。

这比单一 spectral gap 更接近 Weil 机制：重要的不是所有 directions 都有
统一 gap，而是 distinguished Tate/trace class 不在错误的低-slope modes 上
积累过多质量。

## 7. 计算实现

`scripts/qw_matrix.py` 新增：

- `endpoint_quadratic_mass`；
- `endpoint_spatial_shell_coercivity`。

后者返回每个 shell 的 coercivity、rotation gain、最低 generalized direction、
其逐 shell energies，以及 response 的 exact capacity/endpoint spectral
weights。回归测试核对 shell Gram additivity、coercivity superadditivity、最低
mode normalization，并逐项验证式 (14)--(17) 与式 (20)--(21)。
