# Shrinking annular frame、Selberg 方差与零点条带传递

文档 060 用 fixed width interval 得到 strong full-spectrum frame。本笔记让
width 随 scale 缩小，把剩余 arithmetic tightness 精确改写为乘法短区间中
`Lambda-1` 的 weighted Selberg variance，并量化：任意 variance power
improvement 会给出多宽的全局零点条带。

核心标度是：width band `[eta,2eta]` 的 arithmetic diagonal 自然约为
`eta^2 logX`，而 fixed divisor mode 的 frame weight 为 `eta^3`。两者相差
一个 `eta`，所以在 `eta=X^(-theta)` 上的自然均方界会推出
`Re rho<=1/2+theta/2`；当 `eta=X^(-o(1))` 时正好得到 RH。

## 1. Shrinking-width multiplier

沿用定理 KB 的

`r_h(tau)=(itau+1/2)2sin(h tau)/tau`.              (1)

定义

`m_eta(tau)=int_eta^(2eta)|r_h(tau)|^2dh`.         (2)

### 命题 KF（cubic shrinking-frame law）

对每个 fixed compact frequency set，`eta->0` 时一致有

`m_eta(tau)=(28/3)(tau^2+1/4)eta^3`

`                                      +O_K(eta^5)`. (3)

特别地，对每个 fixed `tau` 存在正常数 `c_tau,C_tau`，使充分小 `eta` 下

`c_tau eta^3<=m_eta(tau)<=C_tau eta^3`.            (4)

#### 证明

在 compact `tau` 上一致展开

`sin(h tau)=h tau+O_K(h^3)`。

代入式 (1)，平方后主项为 `4(tau^2+1/4)h^2`。而

`int_eta^(2eta)h^2dh=7eta^3/3`，                  (5)

得到式 (3)；主系数严格正，给式 (4)。`□`

`eta^3` 是 width measure 的一个 `eta` 与单 channel amplitude squared 的
`eta^2` 的乘积。

## 2. 有限 weighted Selberg variance

令

`b_h(t)=sum_(e^(t-h)<n<=e^(t+h))`

`                         [Lambda(n)-1]/sqrt(n)`. (6)

定义每个 multiplicative block 的完全有限正量

`mathcal W(X,eta)=int_eta^(2eta)int_(logX)^(log2X)`

`                                      |b_h(t)|^2dt dh`. (7)

### 命题 KG（finite prime-pair Gram）

`mathcal W(X,eta)` 是 coefficients `Lambda(n)-1` 的正 Gram：

`mathcal W=sum_(m,n)[Lambda(m)-1][Lambda(n)-1]`

`                                  K_(X,eta)(m,n)`, (8)

其中

`K_(X,eta)(m,n)=1/sqrt(mn) int_(logX)^(log2X)`

` *[2eta-max(eta,|t-logm|,|t-logn|)]_+dt`.         (9)

kernel 只使用有限范围

`Xe^(-2eta)<m,n<=2Xe^(2eta)`                      (10)

并且正半定。

#### 证明

在式 (7) 展开平方。对固定 `t,m,n`，两个 membership indicators 在
`h in[eta,2eta]` 上同时为 `1` 的长度正是方括号，得到式 (9)。式 (10)
来自支撑；正性由原 feature Gram 表示。`□`

所以所需 Selberg variance 不含 continuum cross term，也不是渐近对象；它
对每个 `X,eta` 都是有限可计算正矩阵。

## 3. Variance exponent 检测零点条带

取 `eta_X=X^(-theta)`，其中 fixed `0<=theta<1`。令

`omega(theta)=limsup_(X->infinity)`

` log(max(1,mathcal W(X,eta_X)))/logX`.            (11)

### 定理 KH（shrinking-width zero-strip theorem）

在标准 finite-order explicit formula 条件下，

`omega(theta)>=max(0,2Theta-1-3theta)`.            (12)

因此若对某个 `delta>=0`，

`mathcal W(X,X^(-theta))`

`             <=X^(-2theta+delta+o(1))`,          (13)

则全部 zeta zeros 满足

`Re rho<=1/2+(theta+delta)/2`.                     (14)

特别地，自然 weighted Selberg bound

`mathcal W(X,X^(-theta))<=X^(-2theta+o(1))`       (15)

给条带 `Re rho<=1/2+theta/2`。

#### 证明

固定 zero `rho=beta+igamma`。normalized Chebyshev current 中相应 mode 为
`X^(rho-1/2)` 乘 nonzero fixed coefficient。命题 KF 说明 width band 对其
squared norm 乘 `X^(-3theta+o(1))`。Mellin singularity/finite-order
uniqueness 排除 fixed mode 的完全相消，故沿某子列

`mathcal W(X,X^(-theta))`

`>=X^(2beta-1-3theta-o(1))`.                       (16)

对 `beta` 取 supremum 得式 (12)。式 (13) 与 (16) 比较：

`2beta-1-3theta<=-2theta+delta`，

即式 (14)。`□`

这是一个定量 Hodge transfer：短区间 variance 的每个 fixed power improvement
都有明确的 zero-free-strip 收益。

## 4. Subpower relative widths 已足以证明 RH

现在允许 `eta_X=X^(-o(1))`，例如 `eta_X=1/logX`。命题 KF 对每个 fixed
divisor frequency 给

`m_(eta_X)(gamma)=X^(-o(1))`.                     (17)

### 推论 KI（long-short-interval criterion for RH）

若某个 `eta_X=X^(-o(1))` 满足

`mathcal W(X,eta_X)<=eta_X^2 X^(o(1))`,           (18)

则 RH 成立。

#### 证明

若有 fixed off-center zero `beta>1/2`，式 (16) 中 `3theta` 替换为
`o(1)`，给 `X^(2beta-1-o(1))` 下界；式 (18) 是 subpower，矛盾。
`□`

式 (18) 是一个非常具体的 RH 攻击目标：只涉及长度约
`Xeta_X=X/log(X)^K` 的乘法短区间，并对 center scale 与 width 同时作均方。
这里没有声称 RH 自动给每个 fixed log-length block 的式 (18)：RH 的
pointwise bound 只直接给更粗估计，而 Besicovitch 长期均方也不能未经统一性
证明就替换成滑动 fixed block。故式 (18) 是严格充分条件，是否与 RH 反向
等价需要额外的 local-mean theorem。

后续文档 070 利用 critical coefficients `m_gamma/rho` 与 unit-window zero
count，证明了 fixed nondegenerate width band 的 Stepanov local-mean theorem。
但式 (18) 中 `eta_X->0`，还要求 constants 在 shrinking widths 下按 natural
`eta_X` normalization uniform；文档 070 的 fixed-width 结果不提供这一点，
所以上述证据边界对本笔记仍然有效。

## 5. 与标准 Selberg integral 的关系

令

`S(x,h)=sum_(xe^(-h)<n<=xe^h)[Lambda(n)-1]`.      (19)

在 `h=o(1)`、`x~X` 上，式 (6) 是 `x^(-1/2)S(x,h)` 加由 partial
summation 控制的同尺度 remainder。因此标准型 bound

`int_X^(2X)|S(x,h)|^2dx<<X^2 h log(X)^C`          (20)

uniformly for `eta<=h<=2eta`，连同相同的 endpoint partial-sum bound，
推出

`mathcal W(X,eta)<<eta^2 log(X)^C`.                (21)

当 `eta=log(X)^(-K)` 时，这会由推论 KI 证明 RH；所以式 (20) 在这一几乎
线性长度范围内不能被当作已知的无条件 Selberg estimate。

这也解释常见误区：短区间均方的某些无条件范围若只到
`h=X^(-theta)`、`theta>0` fixed，最多通过定理 KH 给一个固定零点条带，
不能令 `theta=0` 而不新增具有 RH 强度的输入。

## 6. Gamma--Euler transfer

### 定理 KJ（general shrinking-frame strip theorem）

对中心 `c/2` 的 paired Gamma--Euler current，若 shrinking-width energy
`mathcal W_Z(X,X^(-theta))` 满足

`mathcal W_Z<=X^(-2theta+delta+o(1))`,             (22)

则全部 divisor 满足

`Re rho<=c/2+(theta+delta)/2`.                     (23)

若 `eta_X=X^(-o(1))` 且 `mathcal W_Z<=eta_X^2X^(o(1))`，则全部 divisor
位于中心线。

#### 证明

定理 KE 的 multiplier 在 fixed frequency 上仍按 `eta^3` 缩放；normalized
mode 是 `X^(rho-c/2)`。重复定理 KH 的 exponent 比较。`□`

## 7. 证据边界

本笔记没有证明式 (18) 或 (20)。无条件 PNT 代入只给带正 power `X` 的
误差，远不足以达到 natural diagonal scale。真正的新结论是：

- strong annular tightness 被精确转成有限 weighted Selberg Gram；
- width shrinkage 的三次 spectral loss 已量化；
- 任意可证明的 variance exponent 都有明确的零点条带回报；
- polylog relative intervals 上的 natural mean-square bound 正好具有 RH
  强度，而不是普通短区间技术的自动推论。
