# `Lambda-1` centered Gram、frame 障碍与零自由条带指数

文档 050 的 finite pair formula 同时含 prime-pair、prime--continuum 与
background 三项。这里在系数层先完成 continuum centering：compact kernel
`phi` 的 Riemann sum 与其积分只差 `O(1)`，故剩余能量等价于单个 signed
sequence `Lambda(n)-1` 的正 Gram。

这个改写揭示两点：

1. kernel 对任意 coefficients 的 generic frame constant 按 `X` 线性增长，
   所以纯算子范数路线无效；
2. 只要实际 arithmetic vector `Lambda-1` 的 Rayleigh quotient 是 subpower，
   就已经推出 RH。

同时，本笔记证明 wavelet block growth exponent 精确等于最右零点偏移的
两倍。

## 1. Bounded-variation centering

令

`R(L)=sum_n phi(n/L)-Llog2`.                        (1)

### 命题 HY（uniform Riemann-sum remainder）

对所有 `L>=1`，

`|R(L)|<=Var(phi)=2`.                               (2)

因此若

`z_c(L)=sum_n[Lambda(n)-1]phi(n/L)`,                (3)

则

`z(L)=z_c(L)+R(L)`.                                (4)

定义 centered block energy

`C_c(X)=int_X^(2X)|z_c(L)|^2L^(-2)dL`.             (5)

它与文档 050 的 `C(X)` 满足

`|sqrt(C(X))-sqrt(C_c(X))|<=sqrt(2/X)`.            (6)

#### 证明

对 mesh `1/L` 的右端 Riemann sum 使用一维 Koksma/BV inequality：

`|(1/L)sum_n phi(n/L)-int phi|<=Var(phi)/L`.        (7)

文档 HS 给 `int phi=log2`，得到式 (2)–(4)。最后在
`L^2([X,2X],L^(-2)dL)` 中用反三角不等式，且

`int_X^(2X)|R(L)|^2L^(-2)dL<=4 int_X^(2X)L^(-2)dL`

`=2/X`，得到式 (6)。`□`

所以 continuum background 可以无损地吸收到 coefficient `-1`；误差甚至
随 block scale 消失。

## 2. 单一 centered pair Gram

记 `a_n=Lambda(n)-1`，并沿用 kernel `K_X(m,n)`。

### 定理 HZ（centered Gram and its diagonal）

有

`C_c(X)=sum_(m,n)a_m a_n K_X(m,n)>=0`.             (8)

其 centered diagonal

`D_c(X)=sum_n a_n^2K_X(n,n)`                       (9)

满足

`D_c(X)=(6-8log2)log2 logX+O(1)`.                 (10)

因此 `C,C_c` 具有相同的 bounded/subpower 性质及相同的 power-growth
exponent。

#### 证明

式 (8) 由式 (3) 平方积分。展开
`a_n^2=Lambda(n)^2-2Lambda(n)+1`。第一项由定理 HU 给式 (10) 的
logarithmic 主项；PNT/Riemann sum 使后两项在每个 `L` 上都是 `O(L)`，
乘 `L^(-2)` 在 `[X,2X]` 积分只贡献 `O(1)`。最后使用命题 HY。`□`

这是可用于 dispersion 的规范形式：一个确定的正 Gram kernel，作用于单个
零均值 arithmetic sequence。

## 3. Generic frame norm 必然线性增长

对有限 index set `X/2<n<=4X` 定义 weighted frame constant

`mathfrak F_X=sup_(c!=0)`

` [sum_(m,n)c_m conjugate(c_n)K_X(m,n)]`

` /[sum_n |c_n|^2K_X(n,n)]`.                       (11)

### 定理 IA（universal operator-frame no-go）

有

`mathfrak F_X >= [log2/(6-8log2)]X+O(1)`.          (12)

所以任何只估计 `K_X` 的通用 operator/frame norm、而不利用 coefficients
`Lambda(n)-1` 的算术符号与部分和，都至少损失一个 factor `X`。

#### 证明

在式 (11) 取 `c_n=1`。由命题 HY，

`sum_n phi(n/L)=Llog2+O(1)`.                       (13)

故 numerator 为

`int_X^(2X)L^(-2)|Llog2+O(1)|^2dL`

`=(log2)^2X+O(1)`.                                 (14)

denominator 为

`int_X^(2X)L^(-2)sum_n phi(n/L)^2dL`

`=(6-8log2)log2+O(X^(-1))`.                       (15)

相除得到式 (12)。`□`

这解释了为何 ordinary frame bound 不能解决问题：相邻 `n` 的 features
高度平行。所需 cancellation 属于特定 arithmetic vector，而不是 kernel
空间的所有方向。

## 4. Arithmetic Rayleigh criterion

定义实际 arithmetic quotient

`mathfrak R_ar(X)=C_c(X)/D_c(X)`.                   (16)

### 定理 IB（subpower arithmetic frame bound implies RH）

若

`mathfrak R_ar(X)=X^(o(1))`,                        (17)

特别是若它为 `O(log(X)^A)`，则 RH 成立。

更一般地，若对某个 `delta>=0`，

`mathfrak R_ar(X)=O_epsilon(X^(delta+epsilon))`,   (18)

则全部非平凡零点满足

`Re rho<=(1+delta)/2`.                             (19)

#### 证明

由定理 HZ，`D_c(X)=O(logX)`。式 (17) 给
`C_c(X)=X^(o(1))`，命题 HY 与定理 HV 推出 RH。式 (18) 给
`C(X)=O_epsilon(X^(delta+epsilon))`；下面定理 IC 把 block exponent 转成
零自由条带。`□`

IB 是一个真正的 centered large-sieve 目标：不要求 `O(1)` sharp
saturation，只要求 actual Rayleigh quotient 不出现固定幂增长。

## 5. Block exponent 精确检测最右零点

令

`Theta=sup{Re rho: rho is a nontrivial zeta zero}`, (20)

`delta_wave=limsup_(X->infinity)`

` log(max(1,C(X)))/logX`.                           (21)

### 定理 IC（wavelet exponent theorem）

有精确恒等式

`delta_wave=max(0,2Theta-1)`.                       (22)

因此任意 bound `C(X)=O_epsilon(X^(delta+epsilon))` 都给式 (19)；
`delta=0` 正是 RH。

#### 证明

零点 `rho` 对 normalized wavelet `y(logL)=L^(-1/2)z(L)` 的 mode 为

`-W(rho)L^(rho-1/2)/rho`,                           (23)

其中定理 HI 已证明 `W(rho)` 在开临界条带无零。固定 log-length block 的
平方积分于是把 real exponent `Re rho-1/2` 变成
`X^(2Re rho-1)`。标准 finite-order explicit formula、Riesz smoothing 与
Mellin singularity argument 给上界及不可消去的下 `limsup`；对趋近 supremum
的 zeros 取极限，得到式 (22)。若 `Theta=1/2`，RH 下绝对收敛展开给 bounded
blocks，外面的 `max(0,.)` 处理该情形。`□`

经典定量 PNT 只给 `C(X)<=X exp(-c sqrt(logX))`，其 power exponent 仍为
`1`；任何固定 power saving 都会立即给一个新的全局零自由条带。

## 6. 适合 dispersion 的有限目标

把 normalized correlation matrix 写成

`mathcal C_X(m,n)=K_X(m,n)/sqrt(K_X(m,m)K_X(n,n))`. (24)

定理 IA 说明 `||mathcal C_X||` 对全空间为 `Omega(X)`；但 IB 只需控制
特定向量

`b_n=[Lambda(n)-1]sqrt(K_X(n,n))`.                 (25)

可行输入可以是：

1. arithmetic restricted frame bound
   `b*mathcal C_X b<=X^o(1)||b||^2`；
2. 把 `a_n` 按 residue/short multiplicative intervals 分组后的 dispersion；
3. 利用 partial sums `sum_(n<=x)a_n=psi(x)-x` 的多尺度 cancellation；
4. 对 centered off-diagonal form直接证明 subpower，而非 sharp 主项。

第 4 项已足以证明 RH；只有要直接构造临界 Hilbert space 时才需文档 050
的精确 `O(1)` saturation。

## 7. Gamma--Euler centered-frame theorem

### 定理 ID（general centered arithmetic-frame structure）

设 Gamma--Euler data 满足定理 HX，并以其 continuum density 对 Euler
coefficients 作中心化 `a_Z(n)=Lambda_Z(n)-m_Z(n)`。若：

- centered finite Gram 与原 wavelet energy 相差 `o(X^epsilon)`；
- diagonal 有 `O(logX)` Rankin--Selberg bound；
- actual arithmetic Rayleigh quotient 为 `X^o(1)`，

则相应 divisor 全部位于中心线。固定幂 `X^delta` bound 给中心宽度
`delta/2` 的全局条带。

#### 证明

命题 HY–定理 IB 的证明只使用 BV wavelet、diagonal law、显式公式和
multiplier 非消失；复 coefficients 把 quadratic forms 换成 Hermitian
forms 即可。`□`

## 8. 证据边界

本笔记没有证明式 (17)。无条件已知 PNT partial-sum bound 代回 summation
by parts 只恢复 power exponent `1`，不能给 subpower arithmetic frame。
真正的新结论是：

- continuum 已无损吸收到 `Lambda-1`；
- generic operator norm 路线被定量排除；
- 证明 RH 所需的 centered bound 可从 sharp `O(1)` 放宽到任意 subpower；
- 每个 fixed power improvement 都有明确的 zero-free-strip 收益。

### 有限 centered/frame 审计

| `X` | `C_c(X)` | `D_c(X)` | arithmetic Rayleigh | generic Rayleigh | generic `/X` |
|---:|---:|---:|---:|---:|---:|
| 8 | 0.00124674 | 0.355542 | 0.00350659 | 12.1904 | 1.52379 |
| 16 | 0.00121097 | 0.563927 | 0.00214739 | 24.3837 | 1.52398 |
| 32 | 0.00135662 | 0.814280 | 0.00166603 | 48.7678 | 1.52399 |

定理 IA 预测 generic quotient `/X` 趋于

`log2/(6-8log2)=1.52399473629...`,                 (26)

与表中一致；actual arithmetic quotient 小约三到四个数量级。Riemann
remainders 在 `L=8,13.25,31.7` 分别为
`-0.01542,0.01011,-0.00387`，远小于统一界 `2`。这些有限值只审计
centering/frame 公式，不能证明 arithmetic quotient 的 subpower 渐近。
