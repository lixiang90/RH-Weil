# Response spectral measure and amplitude capacities

文档 115 将 finite-head obstruction 归一化为 response-selective mass `beta`。本节
证明该 mass 属于一个 canonical positive spectral measure；改变 cell-variance
amplitude 时，response capacity 是该测度的 Stieltjes transform。于是 `beta` 可由
finite determinant capacities 在显式误差内认证，而不必直接计算 cumulative-charge
mean square。

## 1. Canonical response measure

沿用文档 114 的 normalized data

`G=Theta^(1/2)U^*X^(-1)UTheta^(1/2)`,             (1)

`f=Theta^(1/2)U^*X^(-1)D`,                        (2)

`c=D^*X^(-1)D`.                                   (3)

令

`G e_i=lambda_i e_i`, `0<=lambda_i<=epsilon`,     (4)

并定义 positive response spectral measure

`nu_X=sum_i w_i delta_(lambda_i)`,                (5)

其中

`w_i=|e_i^*f|^2/c`.                               (6)

### 定理 VQ（response spectral-measure representation）

`nu_X` 支持在 `[0,epsilon]`，其总质量为

`nu_X([0,epsilon])=sum_iw_i=beta_X`.              (7)

其 moments 为

`m_k=int lambda^k dnu_X(lambda)`

`   =c^(-1)f^*G^kf`.                              (8)

#### 证明

文档 114 定理 VK 给 spectrum inclusion。Parseval identity 给

`sum_iw_i=||f||^2/c=q_X/c=beta_X`。               (9)

spectral theorem 直接给式 (8)。`□`

所以 `beta_X` 不是任意 error scalar，而是 normalized charge operator 在 canonical
response state 上的 spectral mass；`m_1/beta_X` 是 response-weighted mean update
eigenvalue。

## 2. Cell-amplitude Stieltjes transform

令

`Y_s=X+sUTheta U^*`, `s>=0`,                      (10)

`C(s)=D^*Y_s^(-1)D`.                              (11)

### 定理 VR（amplitude-capacity transform）

有 exact formula

`C(s)/c=1-s int_[0,epsilon]`

`                 dnu_X(lambda)/(1+s lambda)`.    (12)

若

`F(s)=int dnu_X(lambda)/(1+s lambda)`,             (13)

则 `F` completely monotone：

`(-1)^kF^(k)(s)`

` =k!int lambda^k/(1+s lambda)^(k+1)dnu_X>=0`.    (14)

在 `|s|<1/epsilon`，

`C(s)/c=1-sum_(k>=0)(-1)^km_ks^(k+1)`.           (15)

#### 证明

对 amplitude `s` 应用 Woodbury：

`C(s)=c-s f^*(I+sG)^(-1)f`.                      (16)

在 eigenbasis 中展开并除以 `c` 得式 (12)。对 finite positive sum逐项微分得
式 (14)；geometric series 给式 (15)。`□`

式 (12) 把整个 positive update path 编码为一个 compact-support Stieltjes moment
problem。不同 amplitudes 的 determinant capacities 是同一测度的 samples，而非
无关数据。

## 3. Capacity-sampled response mass

定义 amplitude-`s` relative capacity loss

`ell(s)=1-C(s)/C(0)`.                              (17)

### 定理 VS（determinant-sampled response criterion）

对每个 `s>0`，

`ell(s)/s<=beta_X`

` <=(1+s epsilon)ell(s)/s`.                       (18)

因此在文档 115 的 plus/minus transversal bases `X_j` 上，任选 sampling amplitudes
`s_j>0`，定义

`beta_j^lo=ell_j(s_j)/s_j`,                       (19)

`beta_j^up=(1+s_jepsilon_j)ell_j(s_j)/s_j`.       (20)

则 kernel-free upper

`A_samp=C_B/(2t){delta_+^0/[1-beta_+^up]`

` -delta_-^0/[1-beta_-^lo/(1+epsilon_-)]}`        (21)

满足 `A_head<=A_samp`。再加入文档 111 的 uniform tail radius `eta_M`，有

`A_W<=(sqrt(A_samp)+eta_M)^2`.                    (22)

若相应 Riesz upper 是

`o(sqrt(log N)/loglog(3N))`,                       (23)

则在其余 Euler--Tate/Weil package 公理下，相应 zeta zeros 位于中心线。

#### 证明

由式 (12)，

`ell(s)/s=int dnu/(1+s lambda)`.                  (24)

在 support `[0,epsilon]` 上，

`1/(1+s epsilon)<=1/(1+s lambda)<=1`.            (25)

积分并用 `int dnu=beta_X` 得式 (18)。对 plus point，定理 VP 的 upper 随
`beta_+` 增加，故代入 `beta_+^up`；对被减去的 minus lower，代入
`beta_-^lo` 仍给 directed upper，得到式 (21)。式 (22)--(23) 由文档 111、100、
094 的 transfer theorems。`□`

每个 `C_j(s_j)` 都可由文档 113 的 determinant quotient计算。因此定理 VS 将
response-selective charge mean square 换成有限 amplitude determinant data 与 support
bound `epsilon_j`。

## 4. Finite audit

`meanLambda=m_1/beta`；`loss/beta` 是 full-amplitude relative capacity loss 对 spectral
mass 的比值。

| `N` | `R` | `M` | support max | `beta` | meanLambda | loss/beta |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 4 | 9.94e-3 | 7.48e-4 | 5.02e-3 | 0.9950 |
| 12 | 3 | 5 | 1.55e-2 | 1.02e-3 | 9.44e-3 | 0.9907 |
| 20 | 3 | 8 | 1.32e-2 | 5.20e-4 | 1.34e-3 | 0.9987 |
| 30 | 3 | 16 | 1.38e-2 | 1.42e-3 | 3.84e-3 | 0.9962 |
| 50 | 3 | 30 | 1.21e-2 | 9.38e-4 | 3.29e-3 | 0.9967 |
| 100 | 3 | 100 | 1.15e-2 | 9.57e-4 | 2.07e-3 | 0.9979 |

response-weighted mean eigenvalue 显著低于 support maximum，解释了 capacity loss
为何比 worst-support bound 尖锐。回归在 amplitudes `0,1/2,1,2` 验证式 (12) 与
direct matrix capacities 在 `1e-45` tolerance 内一致，并逐 sample 验证式 (18)。

## 5. 计算实现

`positive_rank_update_response_kernel_certificate` 现返回 spectral eigenvectors、
response coordinates 与 normalized weights。新增
`positive_rank_update_amplitude_capacity_certificate`，从 `nu_X` 重建任意 nonnegative
amplitude capacity，并输出定理 VS 的 response-mass lower/upper。
