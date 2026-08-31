# Multi-amplitude arbitrary-order response bounds

文档 117 的 two-amplitude Padé sandwich 将 response-mass certification error 降到
`O(epsilon^2)`。本节给任意阶版本：`k` 个 distinct positive amplitudes 产生 `k`
个 Stieltjes resolvents，其线性 span 中存在显式 lower/upper rational functions，
relative mass interval width 至多

`(product_i s_i)epsilon^k`。

因此只增加有限 determinant capacity samples，就能把 response-selective mass 的
认证精度提高到任意固定阶；证明只使用 positivity 与 compact spectral support。

## 1. k-resolvent rational sandwich

取 distinct amplitudes

`0<s_1<...<s_k`,                                  (1)

并定义

`D_k(lambda)=product_(i=1)^k(1+s_i lambda)`,      (2)

`S_k=product_(i=1)^k s_i`.                        (3)

令

`L_k(lambda)=1-S_k lambda^k/D_k(lambda)`,         (4)

`U_k(lambda)=1+S_k lambda^(k-1)`

`                    *(epsilon-lambda)/D_k(lambda)`. (5)

### 定理 VW（arbitrary-order resolvent sandwich）

`L_k` 与 `U_k` 都可唯一写成

`sum_(i=1)^k A_i/(1+s_i lambda)`,                 (6)

并且在 `0<=lambda<=epsilon` 上

`L_k(lambda)<=1<=U_k(lambda)`.                    (7)

partial-fraction coefficients 可显式取为

`A_i^lo=`

` -S_k(-1/s_i)^k/product_(j!=i)(1-s_j/s_i)`,      (8)

`A_i^up=`

` S_k(-1/s_i)^(k-1)(epsilon+1/s_i)`

` /product_(j!=i)(1-s_j/s_i)`.                   (9)

#### 证明

`D_k` 的 leading coefficient 是 `S_k`，故式 (4) 的 numerator
`D_k-S_klambda^k` degree至多 `k-1`。式 (5) 的 numerator

`D_k+S_kepsilon lambda^(k-1)-S_klambda^k`         (10)

同样因 leading terms cancellation 而 degree至多 `k-1`。因此二者均有式 (6) 的
unique partial fractions。在 pole `lambda=-1/s_i` 处取 residue numerator value，
即得式 (8)--(9)。式 (4)--(5) 的 error terms 在 support 上显然非负，故得式
(7)。`□`

## 2. Arbitrary-order mass bracket

令 `nu` 是支持于 `[0,epsilon]` 的 response spectral measure，

`beta=int dnu`,                                   (11)

`F(s_i)=int(1+s_i lambda)^(-1)dnu`.               (12)

### 定理 VX（k-amplitude response-mass certificate）

定义

`beta_k^lo=sum_i A_i^loF(s_i)`,                   (13)

`beta_k^up=sum_i A_i^upF(s_i)`.                   (14)

则

`beta_k^lo<=beta<=beta_k^up`,                     (15)

且

`beta_k^up-beta_k^lo`

` =int S_kepsilon lambda^(k-1)/D_k(lambda)dnu`    (16)

` <=S_kepsilon^k beta`.                           (17)

#### 证明

对定理 VW 的式 (7) 关于 positive measure积分，使用式 (6)、(11)--(12)，得到
式 (13)--(15)。由式 (4)--(5)，

`U_k-L_k=S_kepsilon lambda^(k-1)/D_k(lambda)`.    (18)

在 support 上使用 `lambda^(k-1)<=epsilon^(k-1)` 与 `D_k>=1`，得式
(16)--(17)。`□`

`k=1` 恢复文档 116 的单-sample bound；`k=2` 恢复文档 117。每增加一个 amplitude，
worst-case error 多获得一个 factor `epsilon`。

## 3. Multi-amplitude determinant Weil criterion

在 plus/minus transversal bases 上，分别使用任意 fixed orders `k_+、k_-` 与
amplitudes sets，构造

`beta_+^up`, `beta_-^lo`.                         (19)

### 定理 VY（arbitrary-order determinant response criterion）

定义

`A_multi=C_B/(2t){`

` delta_+^0/[1-beta_+^up]`

` -delta_-^0/[1-beta_-^lo/(1+epsilon_-)]}`。      (20)

则

`A_head<=A_multi`.                                (21)

加上文档 111 的 uniform tail radius，

`A_W<=(sqrt(A_multi)+eta_M)^2`.                   (22)

若相应 Riesz upper 是

`o(sqrt(log N)/loglog(3N))`,                       (23)

则在其余 Euler--Tate/Weil package 公理下，相应 zeta zeros 位于中心线。

#### 证明

定理 VX 给 directed response-mass brackets；按文档 115 定理 VP 的 monotonicity，
plus 插入 upper、minus 插入 lower，得到式 (20)--(21)。式 (22)--(23) 由文档
111、100、094。`□`

定理 VY 表明 charge mean square 不必作为额外 primitive input：对任意预定精度阶
`k`，它可以由有限个 positive-amplitude determinant capacities 认证，error 由已知
support bound的 `k` 次幂控制。

## 4. Finite audit

取 amplitudes `(1/2,1,2)`，故 `S_3=1`。比较文档 117 的 `k=2` interval 与
本节 `k=3` interval：

| `N` | `R` | `M` | k=2 width | k=3 width | k=3 lower/beta | k=3 upper/beta | theorem `epsilon^3` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 4 | 4.87e-5 | 4.60e-7 | 0.99999954 | 1.00000000 | 9.81e-7 |
| 12 | 3 | 5 | 1.42e-4 | 2.03e-6 | 0.99999799 | 1.00000001 | 3.75e-6 |
| 20 | 3 | 8 | 1.75e-5 | 7.80e-8 | 0.99999994 | 1.00000001 | 2.30e-6 |
| 30 | 3 | 16 | 5.17e-5 | 5.48e-7 | 0.99999947 | 1.00000001 | 2.64e-6 |
| 50 | 3 | 30 | 3.90e-5 | 3.46e-7 | 0.99999967 | 1.00000001 | 1.78e-6 |
| 100 | 3 | 100 | 2.35e-5 | 1.56e-7 | 0.99999986 | 1.00000001 | 1.53e-6 |

第三个 sample 又缩窄约 `70--220` 倍。所有 observed widths 均低于 universal
`epsilon^3`；差距来自 response measure 集中在 support 的低端。

## 5. 计算实现

`positive_rank_update_amplitude_capacity_certificate` 现对全部 distinct positive
amplitudes 计算式 (8)--(9) 的 partial-fraction coefficients 与定理 VX 的 multi-
amplitude bracket，并返回 theoretical relative-width upper。回归验证 exact mass
落在 interval 内且实际 width 不超过式 (17)。
