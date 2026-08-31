# Tilted incidence sectors、显式整数 core/tail 与非退化 Weil 通道

文档 160 从 Vaughan identity 规范导出正交分裂

`K=K_sum direct-sum K_diff`,                      (1)

`K_sum=span{e_0,c_0}`, `K_diff=span{u,v}`.        (2)

其中 `e_0` 是 physical sum，`c_0` 是 coarse pair imbalance，`u,v` 是两个
internal pair boundaries。若 core 精确包含 `e_0`，文档 159 定理 ABX 说明 scalar
Feshbach objective 在 `epsilon->infinity` 有退化 infimum。本节改为每个 sector各取
一条略微 tilted line：

`C(tau,q)=span{e_0+tau c_0,qu+v}`.                (3)

当 `tau ne0` 时，式 (3) 不包含 exact physical direction；同时它仍完全服从
Vaughan incidence algebra，而不是任意四维 PCA plane。

有限审计给出一个极简冻结候选

`tau_0=1/20`, `q_0=3`,                            (4)

其整数 core seeds 为

`h=(21,21,19,19)`, `p=(3,-3,-1,1)`.              (5)

本节证明这一结构的一般矩阵定理、精确 projector stability、显式 core/tail
orthogonalization 与 conditional center-line criterion，并在两个未参与参数选择的
`N=320` blocks 上作 frozen audit。

## 1. Sector-separated Ky Fan structure

令 `G>=0` 是四 component label space上的 Gram，相对文档 160 式 (20) 的固定
unitary incidence basis写

`G_inc=W^*GW`.                                    (6)

令 `H_sum` 是 indices `(e_0,c_0)` 的 `2 x 2` compression，`H_diff` 是
indices `(u,v)` 的 compression。

### 定理 ACD（incidence-sector Ky Fan theorem）

在所有式 (3) 型 rank-two planes中，`tr(P_(C(tau,q))G)` 的最大值等于

`lambda_max(H_sum)+lambda_max(H_diff)`,           (7)

并由两个 blocks各自的 leading eigenline达到。若 affine charts有限，则最优参数
分别是 leading eigenvectors 的 ratios

`tau=x_c/x_e`, `q=x_u/x_v`.                       (8)

该最优解在两个 leading eigenvalues都 simple时唯一到各 line phase。

#### 证明

式 (1) 是正交直和，故式 (3) 的 projector也是两个 rank-one projectors的直和。
因此

`tr(P_CG)=<H_sum x,x>+<H_diff y,y>`,              (9)

其中 `x,y` 分别是两 sector中的 unit vectors。两项独立最大化，Rayleigh--Ritz给
式 (7)--(8)。`□`

实现 `vaughan_incidence_separated_channel_certificate` 返回两个 compressed blocks、
leading ratios、sector vectors、式 (7) residual及产生的 unitary core basis。

## 2. 两参数 projector angle

记 `C_1=C(tau_1,q_1)`、`C_2=C(tau_2,q_2)`。

### 定理 ACE（separated-plane exact angle theorem）

有

`||P_(C_1)-P_(C_2)||=max{s_sum,s_diff}`,           (10)

其中

`s_sum=|tau_1-tau_2|`

` /sqrt[(1+|tau_1|^2)(1+|tau_2|^2)]`,            (11)

`s_diff=|q_1-q_2|`

` /sqrt[(1+|q_1|^2)(1+|q_2|^2)]`.                (12)

#### 证明

两 planes及其 projectors都按式 (1) block diagonal。每个 sector内是两个
complex projective lines，文档 160 定理 ACB 的 Gram-determinant计算分别给式
(11)--(12)。block-diagonal operator norm是两 block norms的最大值，得到式 (10)。
`□`

函数 `incidence_separated_plane_angle_certificate` 同时计算式 (10) 与完整 `4 x 4`
projector difference，并回归验证两者一致。

## 3. 显式冻结整数 unitary basis

对式 (4)，除 core seeds式 (5) 外取 tail seeds

`h_perp=(19,19,-21,-21)`,

`p_perp=(-1,1,-3,3)`.                             (13)

### 定理 ACF（frozen tilted integer channel structure）

四个 normalized columns

`h/(2sqrt401), p/(2sqrt5),`

`h_perp/(2sqrt401), p_perp/(2sqrt5)`              (14)

构成实正交矩阵。前两列定义 fixed core `C_0`，后两列定义 fixed tail。对 physical
vector `e=(1,1,1,1)`，其坐标精确为

`W_0^Te=(40/sqrt401,0,-2/sqrt401,0)`.             (15)

因此

`||P_(C_0)e||^2/||e||^2=400/401`,

`||(I-P_(C_0))e||^2/||e||^2=1/401`.              (16)

特别地，`e notin C_0`，但 physical tail mass只有约 `.2494%`。

#### 证明

直接点积给

`h perp p,h_perp,p_perp`, `p perp p_perp`,

`||h||^2=||h_perp||^2=1604=4*401`,

`||p||^2=||p_perp||^2=20=4*5`.                   (17)

式 (1) 又使 sum-sector columns与 difference-sector columns互相正交，故式 (14)
unitary。计算四个 columns与 `e` 的点积得到式 (15)，继而得式 (16)。`□`

`frozen_vaughan_tilted_incidence_basis` 返回式 (13)--(16)及 exact residuals。

## 4. 非退化 Feshbach--Weil criterion

对每个 square-root core block的 Vaughan component Gram `G_(Y,k)`，相对式 (14)
写

`W_0^*G_(Y,k)W_0=[[A,B],[B^*,C]]`.                (18)

令

`x=(40/sqrt401,0)^T`, `y=(-2/sqrt401,0)^T`.       (19)

取任意 `epsilon_(Y,k)>||C||`，并置

`M_(Y,k)=diag(A+B(epsilon I-C)^(-1)B^*,`

`                 epsilon I)`.                   (20)

### 定理 ACG（frozen tilted-incidence center-line criterion）

在文档 157 定理 ABP 的 Gamma--Euler/explicit-formula hypotheses下，若 finite
approximants与 vector errors有文档 156 定理 ABJ 的 Loewner enclosure，且

`sup_Y sum_k beta_(Y,k)^(-1) {`

` x^*[A+B(epsilon I-C)^(-1)B^*]x`

` +epsilon||y||^2 + E_(Y,k) } < infinity`,        (21)

其中 `E_(Y,k)` 包含相应 vector-error radius与 core-exterior errors，则全部 divisor
zeros位于中心线。

同一结论适用于具有四项 exact convolution decomposition与式 (1) label-incidence
structure的一般 Gamma--Euler zeta/L data。

#### 证明

Schur completion给 `G<=W_0M W_0^*`。由式 (15)，physical compression正是式
(21) braces中前两项；ABJ加入严格 approximant enclosure。式 (21)遂给文档 156
定理 ABI所需的 weighted matrix-Bessel budget，core exterior由文档 150 定理 AAK
处理，得到中心线结论。`□`

ACG 与 exact-physical core有一个重要差别：`||y||^2=4/401>0`，所以
`epsilon->infinity` 会使式 (21)线性发散，不能用文档 159 定理 ABX 的退化把
Feshbach excess人为压到零。它仍是条件定理，因为尚未证明式 (21)；但条件已是一个
完全冻结、非退化、由小整数 incidence seeds定义的具体命题。

## 5. 参数冻结与九 block audit

先在文档 155--160 的九个已有 blocks上观察到 separated optima

`Re tau in [.0245,.0901]`, `|Im tau|<.0084`,

`Re q in [2.776,3.414]`, `|Im q|<.0122`.          (22)

据此冻结式 (4)，此后不再调整。定理 ACE给 fixed plane到每块 local separated
optimum的 sine为 `.0033--.0404`。

在这九块上，fixed `C_0` 的结果为

| quantity | range |
|:---|---:|
| physical overlap | `400/401` exact |
| principal sine to leading rank two | `.0339--.1660` |
| tail / `lambda_1` | `.0922--.1584` |
| coupling / `lambda_1` | `.0148--.0651` |
| excess at `epsilon=tail edge+lambda_1` | `.101%--.827%` |

旧 data-suggested integer plane的相应 principal sine为 `.0239--.1375`，略好但同阶；
新 plane的优势不是在同样本上逐项获胜，而是 seeds、orthogonal completion、physical
tail fraction与 incidence meaning全部有闭式。

## 6. 真正 held-out 的 `N=320` 审计

式 (4) 冻结后，新增两个未参与参数选择的 blocks：

| `(N,Y,T)` | fixed sine | tail/`lambda_1` | coupling/`lambda_1` | finite-threshold excess |
|---:|---:|---:|---:|---:|
| `(320,120,4)` | `.0421` | `.0743` | `.0265` | `.139%` |
| `(320,120,16)` | `.0353` | `.0695` | `.0308` | `.0667%` |

local separated parameters分别为

`tau=.03181+.00277i, q=3.24842-.00103i`,

`tau=.02042+.00018i, q=3.13130-.00005i`.          (23)

式 (10) 的 fixed-to-local sines为 `.0231,.0295`。在这两块上，新 fixed plane的
principal sine与 standardized excess都优于旧整数 plane；这只是 held-out finite
evidence，不是 asymptotic theorem。

## 7. 证据边界与下一步

现在对 zeta 已无条件构造：

- exact four-component Vaughan convolution fibers；
- fixed incidence splitting；
- fixed rational tilted core/tail；
- exact physical core/tail coordinates；
- 每个 finite block的 strict Feshbach--Loewner majorant。

仍未证明的是 ACG 式 (21) 的 cofinal uniform bound。finite principal angles不能代替
该 bound，也没有控制 continuum midpoint、prime truncation与全部 dyadic heights。

下一步比文档 160 更具体：相对式 (14)直接写出两个 core channel与两个 tail
channel的 Vaughan convolution formulas，识别哪些是 Type I、Type II、low-prime或
coarse-balanced combinations；然后对 `A,B,C` 分别寻找大筛/双线性 bounds。若式
(14) 使 core仍含等价于完整 target的循环分量，则必须回到 finite-trace negative
Hodge index而非 full positive energy。关键是证明式 (21)，而不是继续优化 seeds。
