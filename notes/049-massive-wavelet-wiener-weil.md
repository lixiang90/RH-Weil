# Massive prime wavelet、Wiener inverse 与广义结构定理

文档 048 的 local prime wavelet multiplier 在开临界条带无零。本笔记
证明更强的临界结构：对数尺度上的 wavelet differential 等于一个
massive nearest-neighbor translation operator 作用在 normalized Chebyshev
current 上。该 operator 在任意酉 translation representation 中都有统一
谱隙和显式指数衰减 inverse。

最后把这个机制抽象为 Laurent-wavelet Weil 结构定理：compact Mellin
wavelet 的 translation polynomial 只要在单位圆无零，有限 arithmetic
Sobolev Grams 的临界 GNS 极限就能稳定恢复原 current，并产生中心线算子。

## 1. Prime-wavelet differential identity

令 `h=log2`，并沿用文档 048：

`f(t)=e^(-t/2)[psi(e^t)-e^t]`,

`y(t)=e^(-t/2)z(e^t)`.                             (1)

记 `T_hg(t)=g(t+h)`。定义 Laurent translation operators

`N=sqrt2(T_h+T_(-h))-3I`,

`B=-N=3I-sqrt2(T_h+T_(-h))`.                       (2)

### 命题 HM（exact massive-wavelet identity）

在局部绝对连续/分布意义下，

`(partial_t-1/2)y=Nf=-Bf`.                         (3)

#### 证明

对 mode `E(x)=x^rho`，文档 048 的式 (24) 给

`z(e^t)=W(rho)e^(rho t)`,

`W(rho)=[2^rho+2^(1-rho)-3]/(rho-1)`.              (4)

归一化后 `f,y` 的 mode 都是 `e^((rho-1/2)t)`。`partial_t-1/2`
作用于 `y` 的乘子是

`(rho-1)W(rho)=2^rho+2^(1-rho)-3`,                 (5)

而 `N` 在同一 mode 上的乘子为

`sqrt2[2^(rho-1/2)+2^(-(rho-1/2))]-3`

`=2^rho+2^(1-rho)-3`.                              (6)

这证明 Mellin dense class；由式 (22) 的 compact kernel 和分布连续性推广
到 arithmetic `E`。也可直接对移动积分端点求导。`□`

所以 wavelet smoothing 的唯一微分损失由一个明确的一阶算子恢复；剩余
translation polynomial 是有质量而非临界的。

## 2. Massive lattice Hodge operator

### 定理 HN（spectral gap and explicit Wiener inverse）

设 `U_t` 是任意 Hilbert 空间上的强连续酉群。令

`B_h=3I-sqrt2(U_h+U_(-h))`.                         (7)

则 `B_h` 正、自伴、可逆，并满足

`(3-2sqrt2)I<=B_h<=(3+2sqrt2)I`.                   (8)

其 inverse 在 operator norm 下绝对收敛为

`B_h^(-1)=sum_(n in Z)2^(-|n|/2)U_(nh)`.           (9)

特别地，

`||B_h^(-1)||=1/(3-2sqrt2)=3+2sqrt2`.              (10)

#### 证明

由谱定理，`U_h` 的 spectral variable 为 `e^(itheta)`，`B_h` 的 symbol 是

`b(theta)=3-2sqrt2 cos(theta)`.                    (11)

其范围正是式 (8)。令 `r=2^(-1/2)`；Poisson kernel 恒等式给

`sum_(n in Z)r^|n|e^(intheta)`

`=(1-r^2)/(1-2r cos(theta)+r^2)`

`=1/[3-2sqrt2 cos(theta)]`.                        (12)

Fourier series 的系数绝对可和，functional calculus 给式 (9)。最大 inverse
值在 `theta=0`，得到式 (10)。`□`

这与定理 HH 的 core gap 是同一个常数来源：一个出现在 endpoint AR(1)
covariance 的谱底，另一个出现在其 massive precision/translation 多项式。

## 3. 临界 Sobolev frame 等价

### 定理 HO（prime current and wavelet Sobolev norm are equivalent）

在任意 translation-invariant Hilbert/Besicovitch space 中，若式 (3) 成立，
则

`(3-2sqrt2)||f||<=||(partial_t-1/2)y||`

`                    <=(3+2sqrt2)||f||`.           (13)

并且

`f=-sum_(n in Z)2^(-|n|/2)`

`              T_(nh)(partial_t-1/2)y`.            (14)

在 Fourier variable `xi`，wavelet multiplier 还满足精确两侧界

`(3-2sqrt2)/sqrt(xi^2+1/4)`

`<=|W(1/2+i xi)|`

`<=(3+2sqrt2)/sqrt(xi^2+1/4)`.                     (15)

#### 证明

式 (13)–(14) 是命题 HM 与定理 HN。对 `rho=1/2+i xi`，令
`x=2^(rho-1)`，则 `|x|=2^(-1/2)`，式 (4) 的 numerator 为
`(x-1)(2x-1)/x`。三角不等式分别给

`3-2sqrt2<=|(x-1)(2x-1)/x|<=3+2sqrt2`;            (16)

而 `|rho-1|=sqrt(xi^2+1/4)`，得到式 (15)。`□`

因此 wavelet `L^2` 是一个一阶 smoothing，但 wavelet `H^1` 与原
Chebyshev current `L^2` 完全等价。任何利用 Sobolev tightness 构造连续
Weil 结构的证明，既不会丢 arithmetic information，也不会凭 smoothing
免费获得 RH。

## 4. Arithmetic GNS 中的稳定 current 重构

### 定理 HP（critical wavelet Grams reconstruct the prime current）

假设 finite prime-wavelet Grams 沿临界截断满足文档 GV 的 Sobolev
tightness。令其 GNS 极限为 `(H,U_t,A,xi_y)`，其中 `xi_y in Dom(A)` 代表
`y`。则

`xi_f=-B_h^(-1)(iA-1/2)xi_y`                       (17)

定义同一 Hilbert 空间中的 normalized prime-current vector，并满足

`(iA-1/2)xi_y=-B_h xi_f`.                          (18)

向量 `xi_f` 的 translation coefficients 是 finite arithmetic identity
(3) 的 cofinal 极限。令

`Theta=1/2+iA`;                                    (19)

则 `Theta*=1-Theta`。若显式公式 divisor 由该 cyclic subspace 实现，所有
可见 points 位于中心线。

#### 证明

Sobolev tightness 与定理 GV 给强连续 `U_t`、自伴 `A` 和
`xi_y in Dom(A)`。定理 HN 使式 (17) 有意义；finite identity (3) 对任意
shift test vector 取 Gram 极限给式 (18)。adjoint identity 来自 `A*=A`。
`□`

HP 比“先假设一个零点对角算子”更强：`xi_f`、`U_t` 与 `Theta` 都由 finite
prime-wavelet Grams 及一个有统一常数的 arithmetic identity 得到。

## 5. Laurent-wavelet Weil 结构定理

前述机制不依赖 zeta 的特殊三项 polynomial。设

`P(z)=sum_(n=-m)^m p_n z^n`, `p_(-n)=conj(p_n)`,   (20)

是 Hermitian Laurent polynomial，并假设

`delta_P=min_(|z|=1)|P(z)|>0`.                     (21)

令 `Q` 是一个 polynomial differential symbol。设 arithmetic signals
`f,y` 满足 finite/distribution identity

`Q(c/2+partial_t)y=P(T_h)f`.                       (22)

### 定理 HQ（general Laurent-wavelet center-line structure theorem）

假设：

1. `y` 的 finite Sobolev Grams 在临界边界 tight，并产生强连续 GNS
   representation `U_t=e^(itA)`；
2. 式 (22) 与 Euler/Gamma 显式公式在 finite truncations 上相容；
3. 对每个非平凡 divisor point `rho`，wavelet multiplier

   `P(e^(h(rho-c/2)))/Q(rho)`                      (23)

   在标准条带内不消失（removable points 按极限解释）；
4. divisor 关于 `Re s=c/2` 对称。

则：

- `P(U_h)` 有界可逆，`||P(U_h)^(-1)||<=delta_P^(-1)`；
- current vector 可由

  `xi_f=P(U_h)^(-1)Q(iA+c/2)xi_y`                 (24)

  稳定恢复；
- `Theta=c/2+iA` 满足 `Theta*=c-Theta`；
- 全部非平凡 divisor points 位于 `Re s=c/2`。

#### 证明

谱定理与式 (21) 给第一项；finite identity 的 Gram 极限给式 (24)。自伴
生成元给 adjoint identity。若有右侧 point，式 (23) 的非消失使 arithmetic
wavelet 的 Laplace transform 保留相应 pole；临界 tightness 则使该 transform
在右半平面解析，矛盾。divisor 对称排除左侧。`□`

HQ 是一个足够宽的广义结构定理：核心 algebra 不是特定 cohomology，而是

`positive finite Grams + unitary translation + elliptic Laurent polynomial`

`+ trace/divisor compatibility`.                   (25)

有限域的 normalized Frobenius polynomial、文档 001 的 polarized module、
以及这里的 prime-wavelet translation polynomial 都是“单位圆上无零/酉
可逆”这一纯性机制的不同实现。

## 6. Zeta 与 Gamma--Euler 的存在性审计

### 推论 HR（zeta massive-wavelet Weil datum）

zeta 的 finite data 无条件满足 HQ 的代数部分，其中

`P(z)=sqrt2(z+z^(-1))-3`,

`Q(s)=s-1`, `c=1`, `h=log2`,                       (26)

且 `delta_P=3-2sqrt2`。所有 finite signals、identity (3)、positive Grams
和 Wiener inverse coefficients 都显式可算。若其临界 Sobolev tightness
成立，则 RH。

更一般的 Gamma--Euler data 只需选择 compact Mellin wavelet，使其 Laurent
numerator 在单位圆无零、在标准条带不消去 divisor modes，即可应用 HQ。

尚未证明的是 zeta finite Grams 的临界 tightness。定理 HO 还表明：若要求
完整 Sobolev tightness，这与 normalized Chebyshev current 的临界 `L^2`
控制等价，仍具有 RH 的全部强度。较可能产生新估计的对象是较弱的 wavelet
`L^2` tightness；它已足以由定理 HJ 推出 RH，却不要求先控制导数。

### 数值恒等式审计

在非整数尺度 `L=13.25`，用步长 `10^(-8)` 的独立中心差分核对式 (3)，
误差为 `7.06e-18`。解析谱隙与 inverse norm 分别为

`3-2sqrt2=0.171572875253810`,

`3+2sqrt2=5.828427124746190`.                       (27)

在频率 `theta=0.7`，把式 (9) 截到 `|n|<=400` 后，与 exact inverse symbol
的误差为 `3.12e-61`。这些仅验证 finite arithmetic/difference 与 Wiener
公式，不检验临界 Gram tightness。
