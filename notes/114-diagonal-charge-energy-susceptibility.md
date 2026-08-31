# Diagonal charge-energy susceptibility

文档 113 把 finite-head three-capacity susceptibility 压缩成三个 positive charge
kernels。这里进一步利用 update 本身相对 base metric 很小这一事实，将每个 kernel
inverse quadratic form 在 factor `1+epsilon` 内替换成纯对角 positive energy。

结果是不再需要反演 `(M-1)x(M-1)` charge kernel；centerline upper 只含三组

`sum_m theta_m|C_m^*X_j^(-1)D|^2`

与三个 relative update norms。这种形式最适合 large-sieve、dyadic mean-square 或
直接算术能量估计。

## 1. Normalized charge Gram

令

`Y=X+UTheta U^*`, `X>0`, `Theta>0`,               (1)

并设

`E=UTheta U^*<=epsilon X`.                        (2)

定义 normalized charge Gram 与 response vector

`G=Theta^(1/2)U^*X^(-1)UTheta^(1/2)`,             (3)

`f=Theta^(1/2)U^*X^(-1)D`.                        (4)

### 定理 VK（normalized kernel contraction）

有

`0<=G<=epsilon I`,                                (5)

并且 Woodbury capacity loss 满足

`C_X-C_Y=f^*(I+G)^(-1)f`.                         (6)

#### 证明

令 `A=X^(-1/2)UTheta^(1/2)`。则

`AA^*=X^(-1/2)EX^(-1/2)<=epsilon I`,              (7)

而 `A^*A=G`。`AA^*` 与 `A^*A` 的非零 eigenvalues 相同，故式 (5) 成立。
文档 113 定理 VH 中

`K=Theta^(-1/2)(I+G)Theta^(-1/2)`，               (8)

将其代入 capacity correction `r^*K^(-1)r` 即得式 (6)。`□`

## 2. Diagonal capacity sandwich

定义 diagonal response energy

`q_X=||f||^2`

`   =D^*X^(-1)EX^(-1)D`

`   =sum_m theta_m|C_m^*X^(-1)D|^2`.              (9)

### 定理 VL（kernel-free inverse-capacity bounds）

有

`q_X/(1+epsilon)<=C_X-C_Y<=q_X`.                  (10)

只要 `q_X<C_X`，于是

`[C_X-q_X/(1+epsilon)]^(-1)`

` <=C_Y^(-1)<=[C_X-q_X]^(-1)`.                   (11)

#### 证明

式 (5) 给

`(1+epsilon)^(-1)I<=(I+G)^(-1)<=I`.              (12)

左右以 `f` contraction 并用式 (6)，得式 (10)。从 `C_Y=C_X-(C_X-C_Y)`
取 reciprocal 得式 (11)。`□`

所以 cross-cell kernel interaction 并未消失，而是被 positive relative update norm
统一控制；当 `epsilon` 为百分级时，对角能量自动给百分级甚至更好的 capacity loss。

## 3. Scalar three-energy probe

令

`X_j=X+jtB_perp`, `j in {-1,1}`,                  (13)

并假设

`E<=epsilon_jX_j`.                                (14)

记

`c_j=D^*X_j^(-1)D`,                               (15)

`q_j=D^*X_j^(-1)EX_j^(-1)D`.                     (16)

定义

`U_j=(c_j-q_j)^(-1)`,                             (17)

`L_j=[c_j-q_j/(1+epsilon_j)]^(-1)`.               (18)

定理 VL 给 updated inverse capacity `delta_j` 的 sandwich

`L_j<=delta_j<=U_j`.                              (19)

### 定理 VM（diagonal three-energy Weil criterion）

定义 kernel-free centered upper

`A_diag=C_B(U_1-L_(-1))/(2t)`.                    (20)

则 finite-head excess 满足

`A_head<=A_diag`.                                 (21)

再令文档 111 的 uniform variance-tail radius 为

`eta_M^2=C_Bepsilon_M^2/(2C_Mkappa_M)`,           (22)

则 exact spatial excess 满足

`A_W<=(sqrt(A_diag)+eta_M)^2`.                    (23)

若由式 (15)--(23) 构造的 Riesz upper 是

`o(sqrt(log N)/loglog(3N))`,                       (24)

则 fixed reduced-determinant strata 为 `o(1)`；在其余 Euler--Tate/Weil package
公理下，相应 zeta function 的 zeros 位于中心线。

#### 证明

文档 106 的 centered secant 给

`A_head<=C_B(delta_1-delta_(-1))/(2t)`.           (25)

式 (19) 对 plus point 取 upper、minus point 取 lower，得到式 (20)--(21)。文档
111 定理 VD 给式 (23)；再应用文档 100 定理 TM 与文档 094 定理 SP 得式
(24) 的结论。`□`

定理 VM 的全部 update-dependent quantities 均为 nonnegative scalar sums。它将文档
113 的三个 matrix resolvents 换成

`(c_+,q_+,epsilon_+)`, `(c_-,q_-,epsilon_-)`,      (26)

同时保持严格 directed upper。

## 4. Möbius finite-head specialization

对前 `M-1` 个 cell corrections，

`E_M=sum_(m<M)theta_mC_mC_m^*`,                  (27)

所以

`q_j=sum_(m<M)theta_m|C_m^*X_j^(-1)D|^2`.        (28)

`epsilon_j` 是 finite Gram pair `(E_M,X_j)` 的最大 generalized eigenvalue；也可
用任何显式 Loewner majorant替代。故剩余算术目标变为三组 weighted squared
cumulative-charge responses 的统一估计，不涉及 matrix inverse over cell indices。

## 5. Finite audit

下表中 `diag/loss` 是 central diagonal energy 对 exact capacity loss 的倍率；
`lower/exact` 与 `upper/exact` 是式 (20) 对 centered susceptibility 的双边倍率。

| `N` | `R` | `M` | `epsilon_0` | `diag/loss` | `epsilon_+` | `epsilon_-` | lower/exact | upper/exact |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 4 | 0.00994 | 1.00500 | 0.00713 | 0.01842 | 0.999837 | 1.000014 |
| 12 | 3 | 5 | 0.01553 | 1.00940 | 0.01362 | 0.02156 | 0.999171 | 1.000284 |
| 20 | 3 | 8 | 0.01320 | 1.00133 | 0.01199 | 0.01700 | 0.999478 | 1.000628 |
| 30 | 3 | 16 | 0.01382 | 1.00381 | 0.01209 | 0.01912 | 0.999864 | 1.000038 |

尽管 individual capacity-loss sandwich 允许约 `1%--2%`，centered difference 中
plus/minus errors 高度共同消除；strict scalar upper 仅松 `0.0014%--0.063%`。

## 6. 计算实现

`positive_rank_update_response_kernel_certificate` 现返回 normalized charge Gram、
relative update bound、diagonal response energy、capacity-loss 与 inverse-capacity
sandwich。新增 `positive_rank_update_diagonal_susceptibility_certificate`，直接构造
式 (20) 的 scalar lower/upper，并与 exact three-kernel susceptibility 交叉验证。
