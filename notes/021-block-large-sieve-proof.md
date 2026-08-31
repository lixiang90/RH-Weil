# 调制多项式 block large sieve 与弱 resonance 的解析消除

文档 020 把最后的新解析输入写成一个多井 block-frame bound。本笔记直接
证明它。核心技巧是不使用每口井各自的 prolate 本征向量，而是使用 sinc
kernel Taylor 多项式自然生成的调制多项式 core

`exp(i tau_j x), x exp(i tau_j x),...,x^(2R-2)exp(i tau_j x)`. (1)

分离频率上的这些 blocks 具有与井数无关的 Bessel bound；因此 Taylor
余项的联合 operator norm 只损失一个中心间距的倒数。对 resonance 尺度
`c,delta asymp theta`，这给出文档 020 定理 CB 中的 `q=1`，从而严格求和
全部弱 dyadic 层。

## 1. bandlimited Fourier 导数的分离采样

令 `f in L^2([-1,1])`，并对整数 `k>=0` 定义

`g_k(t)=int_(-1)^1 f(x)x^k exp(-itx)dx`.               (2)

于是 `g_k'(t)=-i g_(k+1)(t)`，且 Plancherel 给出

`int_R|g_k(t)|^2dt=2pi||x^kf||^2<=2pi||f||^2`.        (3)

### 引理 CC（separated derivative sampling）

若实数集 `{tau_j}` 是 `delta`-分离的，即 `|tau_i-tau_j|>=delta`，则对
每个 `k>=0`，

`sum_j|g_k(tau_j)|^2`

`<=B(delta)||f||^2`,                                  (4)

其中可取

`B(delta)=2pi(3+2/delta)`.                             (5)

#### 证明

令 `h=min(delta/2,1/2)`。区间
`I_j=[tau_j-h,tau_j+h]` 两两不交。对任意 `u in H^1(I_j)`，由微积分基本
定理、Cauchy–Schwarz，再对起点平均，

`|u(tau_j)|^2`

`<=(1/h)int_(I_j)|u|^2+2h int_(I_j)|u'|^2`.           (6)

取 `u=g_k`，对 `j` 求和并使用式 (3) 及 `g_k'=-ig_(k+1)`：

`sum_j|g_k(tau_j)|^2`

`<=2pi(1/h+2h)||f||^2`.                               (7)

由 `h=min(delta/2,1/2)`，右端不超过式 (5)。`□`

重要的是常数与采样点数无关，也与导数阶数 `k` 无关；后者来自
`|x|<=1`。

## 2. 多频带 sinc Taylor 余项的联合界

考虑频率井

`I_j=[tau_j-c,tau_j+c]`, `0<c<=1`,                    (8)

中心 `{tau_j}` 为 `delta`-分离。令 `E=union_jI_j`。对应的时间限制
concentration form 为

`int_E|hat f(t)|^2dt/(2pi)`，                           (9)

其逐井 kernel 是

`exp(i tau_j(x-y)) sin(c(x-y))/(pi(x-y))`.             (10)

定义有限维调制多项式 core

`Q_(R) = span{exp(i tau_j x)x^k: all j,0<=k<=2R-2}`.  (11)

### 定理 CD（polynomial-block large sieve）

若 `f perpendicular Q_(R)`、`R>=1`，则

`int_E|hat f(t)|^2dt/(2pi)`

`<= [B(delta)e^2 4^R c^(2R+1)]`

`   /[pi(2R+1)!] ||f||^2`.                            (12)

该界与井数无关。

#### 证明

对式 (10) 的 sinc 因子使用文档 020 式 (4) 的 Taylor 展开。所有 `n<R`
项含有 `(x-y)^(2n)`；展开后二边次数均至多 `2R-2`，故其 quadratic form
在 `Q_(R)^perp` 上为零。

对 `n>=R`，展开

`(x-y)^(2n)=sum_(k=0)^(2n)(-1)^k binom(2n,k)`

`                         x^(2n-k)y^k`.                (13)

相应 quadratic form 的绝对值由

`sum_j |g_(2n-k)(tau_j)g_k(tau_j)|`                   (14)

控制。对两个因子使用 Cauchy–Schwarz及引理 CC，式 (14) 至多
`B(delta)||f||^2`。再对 `k` 求和，二项式系数总和为 `4^n`。因此余项不超过

`B(delta)/pi * sum_(n=R)^infinity`

` 4^n c^(2n+1)/(2n+1)! ||f||^2`.                      (15)

当 `c<=1` 时，尾和不超过首项乘 `e^2`，得到式 (12)。`□`

定理 CD 是文档 020 所需的 block large-sieve theorem，而且给出显式
`delta^(-1)` 损失。

## 3. resonance 尺度给出 `q=1`

在阈值为 `theta` 的 dyadic resonance 层，取 maximal-separated centers。
引理 BU 允许使用物理频率半宽

`r_theta asymp theta/log x`.                           (16)

把时间区间缩放到 `[-1,1]` 后，频率同时乘以 `L/2=(log x)/2`，所以

`c_theta<=C_1theta`, `delta_theta>=C_2theta`.          (17)

### 推论 CE（weak resonance block bound with `q=1`）

对该层构造式 (11) 的 core。其正交补上的总 Fourier 质量满足

`int_(E_theta)|hat f|^2dt/(2pi)`

`<=C_R theta^(2R) ||f||^2`,                            (18)

其中 `C_R` 与井数、`x` 无关。相应负 multiplier 深度为
`O(theta P(x))` 时，整层负误差为

`O_R(P(x)theta^(2R+1))||f||^2`.                        (19)

#### 证明

定理 CD 中 `B(delta_theta)=O(theta^(-1))`，而
`c_theta^(2R+1)=O(theta^(2R+1))`，得到式 (18)；再乘层深度。`□`

所以文档 020 定理 CB 可无条件取 `q=1`。选择

`theta_*=P(x)^(-alpha)`,

`1/(2R+1)<alpha<1`,                                   (20)

则所有 `theta<=theta_*` 的弱层总误差

`O_R(P(x)theta_*^(2R+1))=o(1)`.                       (21)

**弱 resonance 的无限 dyadic 尾至此已经解析解决。**

## 4. 固定/强层也可移入显式有限核心

对 `theta>=theta_*` 只有 `O(log P(x))` 个 dyadic 层。每层负集在
archimedean multiplier 占优以前是紧的；取 maximal-separated cover 后井数
有限。定理 CD 允许为这些层选择随 `x` 增长的 `R_h`，使每层正交补误差
任意小。若缩放后的半宽暂时大于 `1`，可把井细分成半宽不超过 `1` 的
有限子井；这只扩大有限核心，不影响定理 CD 的适用性。由阶乘分母，固定
井宽时所需 `R_h` 随目标精度增长得很慢，但这里不声称关于 `x` 的有效统一
秩界。

下面把这一步的量词单独写清楚。仍令文档 019 式 (17)

`d_lambda(t)=[2P_lambda-K_infinity(t)-G_lambda(t)]_+`. (22)

### 推论 CF（finite-codimension analytic lower bound）

对每个固定 `lambda` 和每个 `epsilon>0`，存在一个显式有限维空间
`Q_(lambda,epsilon)`，使

`QW_lambda(f,f)>=-epsilon||f||^2`

`for all f perpendicular Q_(lambda,epsilon)`.          (23)

此外，可事先任取 `epsilon_lambda->0`，逐个构造相应的
`Q_(lambda,epsilon_lambda)`。

#### 证明

`d_lambda` 的支撑紧且 `D_lambda=||d_lambda||_infinity<infinity`。缩放测试函数
的支撑到 `[-1,1]` 后，用有限多个半宽 `c<=1`、中心 `delta`-分离的等宽井
覆盖该紧集；例如取所有与该紧集相交的单位网格中心，并使用半宽 `1` 的
井。取式 (11) 的全部
调制多项式并加入奇极点锚 `sinh(y/2)` 作为 core。

在其正交补上，奇极点负项为零。命题 BJ 与定理 CD 给出

`QW_lambda(f,f)`

`>=-D_lambda B(delta)e^2 4^R c^(2R+1)`

`   /[pi(2R+1)!] ||f||^2`.                            (24)

固定 `lambda,c,delta` 时，式 (24) 的系数随 `R->infinity` 趋零；选择有限的
`R` 使其不超过 `epsilon` 即得式 (23)。若覆盖分成有限个等宽/分离子族，
分别应用定理 CD 并把有限个误差相加即可。`□`

推论 CF 因而允许对每个 `x` 显式构造一个有限维 core `Q_x`，满足

`QW_lambda(f,f)>=-epsilon_x||f||^2`

`for all f perpendicular Q_x`,                         (25)

且可令解析 complement error `epsilon_x->0`。

这里“显式”指 core 由以下已知函数张成：

- 中心 prolate 模态；
- 每个非零井中心的调制多项式 `e^(it_jy)y^k`；
- 奇极点锚 `sinh(y/2)`。

必须强调：`Q_x` 的维数可能极其巨大，因为负集的最坏频率截止可达
`exp(O(P(x)))`。推论 CF 是一个有限余维归约，不是关于有限核复杂度、最低
特征值或 Schur 耦合的统一估计。推论 CE 的额外价值在于：弱 resonance 的
无限 dyadic 尾可用固定 `R` 和与井数无关的常数统一处理，而不必逐井把所有
困难方向塞进 core。

## 5. 剩余问题已变成有限核心正性与耦合

定理 CD/推论 CE/CF 给出相对于显式、但可能极大的有限核心的补空间控制，
却不能说明 `QW_lambda` 在 `Q_x` 上非负。完成 RH 仍需：

1. 用 interval arithmetic 计算 `QW_lambda|_(Q_x)`；
2. 给出 core–complement coupling 的联合尾界；
3. 证明文档 016 的 Schur 下界沿某 `x_j->infinity` 为 `-o(1)`。

这与早期直接截取 Fourier 模态不同：由 CE 得到的弱层部分是由 prime
resonance 几何决定的 Hodge core；CF 则保证其余部分至少可以有限余维化。
因此解析补空间已有无条件的 `o(1)` 下界，但该陈述始终是相对于一个随
`x`、目标误差变化且尚无可用秩界的 core。

若能进一步证明这些有限核心矩阵自身具有来自 Euler 数据的正 Gram/
intersection factorization，就会直接实现定义 BK 的全球 Hodge–Riemann
结构。当前开放障碍已经从无限维不确定性问题缩成该有限维算术正性。
