# Mellin 对角化、biharmonic 两矩 Hodge core 与低频归约

文档 053 把 primitive homogeneous Gram 化成四个 prefix moments。本笔记
从乘法 Fourier/Mellin 侧重新对角化它，发现四矩 kernel 中有一个可稳定
剥离的 massive Laurent 因子。剥离后只剩通用算子

`(-partial_t^2+1/4)^(-2)`,

其 Green kernel 只需两个 prefix moments。进一步用 Hilbert/large-sieve
均方界无条件移除 `|tau|>=X^(1/4)` 的全部频率尾；RH 难点于是集中在一个
长度 `X^(1/4)` 的低频 core。

## 1. 精确 Mellin--Plancherel 公式

令 `x_n` 为任意有限复序列，并定义

`D_x(tau)=sum_n x_n n^(-1/2-itau)`.                (1)

primitive kernel 的 Mellin transform 为

`M_chi(s)=int_0^infinity chi(r)r^(s-1)dr`.         (2)

### 定理 IR（homogeneous Mellin diagonalization）

有闭式

`M_chi(s)=(1-2^(1-s))`

`         [2^s+2^(1-s)-3]/[s(s-1)]`,              (3)

以及精确 Plancherel 恒等式

`sum_(m,n)x_m conjugate(x_n)K_infty(m,n)`

`=(1/(2pi))int_R |M_chi(1/2+itau)|^2`

`                         |D_x(tau)|^2dtau`.       (4)

#### 证明

命题 HS 的 `phi` 分段积分给

`M_phi(s)=[2^s+2^(1-s)-3]/[s(s-1)]`.

由 `chi(r)=phi(r)-2phi(2r)` 得第一因子 `1-2^(1-s)`，即式 (3)。令

`g(t)=e^(-t/2)chi(e^(-t))`。

则 `hat g(tau)=M_chi(1/2+itau)`，且

`e^(-t/2)sum_n x_n chi(ne^(-t))`

`=sum_n x_n n^(-1/2)g(t-logn)`.                   (5)

对式 (5) 用 Fourier Plancherel；左侧平方积分在 `L=e^t` 下正是
homogeneous Gram，得到式 (4)。`□`

## 2. cubic massive spectral weight

记

`b(tau)=3-2sqrt2 cos(tau log2)`.                   (6)

### 定理 IS（exact cubic massive factor）

临界 Mellin weight 精确为

`|M_chi(1/2+itau)|^2`

`=b(tau)^3/(tau^2+1/4)^2`.                        (7)

而且

`b_-=3-2sqrt2<=b(tau)<=3+2sqrt2=b_+`.             (8)

#### 证明

在 `s=1/2+itau`，令 `theta=tau log2`。式 (3) 的两个 dyadic factors
满足

`|1-sqrt2 e^(-itheta)|^2=b(tau)`,                 (9)

`2^s+2^(1-s)-3=-b(tau)`,                          (10)

并且 `|s(s-1)|^2=(tau^2+1/4)^2`。相乘即得式 (7)；式 (8) 来自
`-1<=cos theta<=1`。`□`

三次方的来源很清楚：原 prime wavelet 给两个 massive factors，primitive
Tate 差分再给一个。由于 `b_->0`，它们属于临界酉谱上的 boundedly
invertible geometry，而不是零点信息本身。

## 3. 剥离 massive factor：通用 biharmonic Gram

定义

`mathcal H(x)=(1/(2pi))int_R |D_x(tau)|^2`

`                              /(tau^2+1/4)^2dtau`. (11)

### 定理 IT（stable massive stripping and Green kernel）

若 `mathcal E(x)` 表示式 (4) 的 primitive Gram，则

`b_-^3 mathcal H(x)<=mathcal E(x)<=b_+^3 mathcal H(x)`. (12)

此外

`mathcal H(x)=sum_(m,n)x_m conjugate(x_n)G(m,n)`,  (13)

其中

`G(m,n)=[2+|log(m/n)|]/max(m,n)`.                  (14)

这个 kernel 正半定，并且是 log-line 上
`(-partial_t^2+1/4)^(-2)` 的 Green kernel 经权重共轭所得。

#### 证明

式 (12) 由式 (7)–(8) 点态积分。标准 residue/Fourier 计算给

`(1/(2pi))int_R e^(itau u)/(tau^2+1/4)^2dtau`

`=(2+|u|)e^(-|u|/2)`.                             (15)

把式 (1) 展开，令 `u=log(n/m)`；式 (15) 乘 `(mn)^(-1/2)` 后恰为
式 (14)。正性由式 (11) 或 Green operator 得到。`□`

## 4. 两个 prefix moments

定义

`P_0(n)=sum_(m<n)x_m`,

`P_1(n)=sum_(m<n)x_m logm`.                        (16)

### 定理 IU（exact two-moment Hodge energy）

有

`mathcal H(x)=2sum_n |x_n|^2/n`

` +2Re sum_n conjugate(x_n)n^(-1)`

`                    [(2+logn)P_0(n)-P_1(n)]`.    (17)

所以文档 053 的四个 local moments 在剥离可逆 massive geometry 后，只剩
两个 global prefix moments。

#### 证明

式 (14) 在 `m<n` 时为

`G(m,n)=[2+logn-logm]/n`。

先求 `m<n` 的和，再加 conjugate transpose 和 diagonal `2/n`，得到
式 (17)。`□`

有限域类比是：改变一个处处非退化的 polarization 不改变 Frobenius
weights。这里式 (12) 正是无限维版本——primitive Gram 与 universal
biharmonic polarization 有界等价，故中心线结论不依赖 massive factor 的
具体坐标选择。

## 5. 两矩有限 RH 判据与精确指数

对文档 053 的

`a_X(n)=[Lambda(n)-1]1_(X/4<n<=4X)`，             (18)

记

`mathcal H_2(X)=mathcal H(a_X)`,                   (19)

`mathcal D_2(X)=2sum_(X/4<n<=4X)[Lambda(n)-1]^2/n`. (20)

### 定理 IV（two-moment finite Hodge criterion）

以下条件等价：

1. RH；
2. `mathcal H_2(X)=X^(o(1))`；
3. `mathcal H_2(X)=O(log(X)^A)` 对某个固定 `A` 成立；
4. `mathcal H_2(X)/mathcal D_2(X)=X^(o(1))`。

并且

`mathcal D_2(X)=8log2 logX+O(1)`.                 (21)

若

`Theta=sup_rho Re rho`,                            (22)

则在定理 IG 的标准有限阶显式公式条件下，

`limsup_(X->infinity)`

` log(max(1,mathcal H_2(X)))/logX`

`=max(0,2Theta-1)`.                                (23)

#### 证明

式 (12) 说明 `mathcal H_2` 与定理 IP 的 `mathcal E_4` 只差固定双侧常数，
故四个等价条件和式 (21) 立即得到。对于式 (23)，一方面若
`A(t)=psi(t)-t=O_epsilon(t^(Theta+epsilon))`，Abel summation 与式 (14)
给上界 `X^(max(0,2Theta-1)+epsilon)`；另一方面文档 053 的式 (24) 将
primitive block 嵌入 finite Gram，而定理 IG 的非消失给相同下
`limsup`。`□`

这说明两矩 criterion 没有削弱问题：每个固定 power improvement 仍精确
对应一个更窄的全局零点条带。

## 6. 无条件高频尾与 `X^(1/4)` 低频 core

把式 (11) 在 `|tau|<=T` 与其补集分开。对

`c_n=a_X(n)/sqrt(n)`，有

`sum |c_n|^2=O(logX)`.                             (24)

### 定理 IW（large-sieve removal of the high-frequency tail）

对 `1<=T<=X`，

`int_(|tau|>=T)|D_(a_X)(tau)|^2`

`                    /(tau^2+1/4)^2dtau`

`<<logX[T^(-3)+XT^(-4)]`.                         (25)

同一界乘固定常数后适用于 primitive weight (7)。特别地，取

`T=X^(1/4)`，高频尾为 `O(logX)`。因此 RH 等价于低频条件

`int_(|tau|<=X^(1/4)) |D_(a_X)(tau)|^2`

`                    /(tau^2+1/4)^2dtau=X^(o(1))`. (26)

#### 证明

对任意 `Y>=1`，展开 Dirichlet polynomial 的平方并积分；diagonal 为
`O(Y sum|c_n|^2)`。off-diagonal kernel 为

`2sin(Ylog(n/m))/log(n/m)`。

区间 `(X/4,4X]` 上相邻 `log n` 的 separation 为 `>>1/X`；Hilbert
inequality 给 off-diagonal `O(X sum|c_n|^2)`。故

`int_Y^(2Y)|D_(a_X)(tau)|^2dtau<< (Y+X)logX`.      (27)

把 `|tau|>=T` dyadically 分解，在第 `Y` 块用 weight `O(Y^(-4))`，求和
得到式 (25)。令 `T=X^(1/4)` 后右侧为 `O(logX)`；结合定理 IV 得式
(26)。`□`

这是真正无条件移除的部分：证明 RH 不必控制任意高 twists，只需控制
`|tau|<=X^(1/4)` 的 centered short Dirichlet polynomial core。

## 7. 广义 massive-factor stripping theorem

### 定理 IX（Laurent-equivalent Weil polarizations）

设一个 Gamma--Euler primitive structure 的临界 Mellin multiplier 可分解为

`M(c/2+itau)=P(e^(ih tau))R(tau)`,                 (28)

其中 `P` 是 Laurent polynomial，且

`0<delta<=|P(z)|<=Delta` 对所有 `|z|=1`.          (29)

则由 `M` 定义的 finite/limit Grams 与由 `R` 定义的 Grams 满足

`delta^2 Q_R<=Q_M<=Delta^2 Q_R`.                  (30)

因此两者具有完全相同的：

- critical tightness 与 subpower filtration；
- GNS existence；
- divisor growth exponent；
- `Theta*=c-Theta` 中心线结论。

#### 证明

临界 translation representation 上 `P(U_h)` 由 continuous functional
calculus 有界可逆；Plancherel 后式 (29) 逐点给式 (30)。双侧 norm
equivalence 保持 tightness、completion 和 power exponent。若 divisor
trace compatible，定理 HQ/II 给最后两项。`□`

IX 是从 Weil 证明中抽离出的一个稳定性原则：处处非退化的 Laurent
correspondence 只改变 polarization 的等价范数，不改变 weights。

## 8. 有限两矩审计

脚本用式 (17) 的一次 prefix scan 计算：

| `X` | `mathcal H_2(X)` | diagonal | Rayleigh quotient |
|---:|---:|---:|---:|
| 8   | 0.2250888 | 4.894040 | 0.0459924 |
| 16  | 0.0104522 | 8.281594 | 0.00126210 |
| 32  | 0.00122873 | 12.083722 | 0.000101685 |
| 64  | 0.1109312 | 16.255832 | 0.00682408 |
| 128 | 0.1502438 | 20.339002 | 0.00738698 |

实现还独立验证了：

- 分段积分的 `M_chi` 模方等于 cubic massive weight；
- generic complex coefficients 上 Green 双和等于两矩单和；
- primitive 四矩 Gram 位于式 (12) 的双侧界内。

这些有限值不单调，也不证明 subpower 渐近；它们只排除公式、共轭和
归一化常数错误。

## 9. Selberg 路线的准确边界

式 (25) 表明普通 mean-value/large-sieve 已经足够处理高频。剩余低频中，
特别是每个固定 `tau` 邻域，weight 有严格正下界。若存在零点
`rho=beta+igamma`、`beta>1/2`，则 `tau` 接近 `gamma` 的 centered block
产生 `X^(2beta-1)` 能量；定理 IV 保证它不能被 massive 因子或高频尾
消除。

Selberg symmetry formula 可以继续把式 (17) 的 `P_0,P_1` 写成 von
Mangoldt convolution，但若只使用由初等 PNT 得到的
`A(x)=x^(1-o(1))`，代入式 (17) 仍只给 `mathcal H_2(X)=X^(1-o(1))`。
要得到 subpower，必须在低频 core 内获得平方根级联合 cancellation；这与
RH 等强，而不是一个可由逐项 symmetry identity 自动推出的估计。

下一步应集中于式 (26)：利用 twisted Selberg symmetry、residue-class
dispersion 或低频 prolate/frame 方法，联合控制至多 `X^(1/4)` 尺度的
twists，同时保留 `Lambda-1` 的符号相消。
