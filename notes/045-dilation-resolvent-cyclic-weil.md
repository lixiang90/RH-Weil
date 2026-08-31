# Dilation resolvent 与循环 Weil--GNS 结构

文档 044 证明单个 triangular Riesz coefficient 已能检测全部非平凡零点。
本笔记把这个标量 detector 提升成更接近有限域 Weil 证明的代数对象：一个
归一化 dilation `U`、一个 arithmetic vector `eta`，以及其稳定差

`xi=(U-r)eta`, `0<r<1`.                              (1)

若有限 arithmetic Gram 截断在临界边界保持 tight，它们的极限自动产生
循环 Hilbert 空间和酉 `U`。因 `U-r` 自动可逆，triangular vector `xi`
与 primitive vector `eta` 生成同一个空间。这里 `U` 扮演归一化 Frobenius；
酉性就是中心线纯性。

## 1. Arithmetic primitive 与稳定差

先取 zeta 数据

`E(x)=psi(x)-x`,

`C(X)=int_1^X E(x)dx`,

`kappa=3/2`, `p(t)=e^(-kappa t)C(e^t)`.              (2)

对 `h>0`，令 `q=e^h`、`r=q^(-kappa)`，并定义

`d_h(t)=p(t+h)-r p(t)`                               (3)

`=q^(-kappa)e^(-kappa t)int_(e^t)^(q e^t)E(x)dx`.  (4)

特别地，`q=2` 时，文档 044 的 `A(X)` 满足

`d_(log 2)(log X)=(2X)^(-3/2)A(X)`.                 (5)

因此 `d_h` 完全由有限 prime--continuum 数据定义，不使用零点。

### 命题 GO（stable Frobenius-resolvent lemma）

设 `U` 是 Hilbert 空间 `H` 上的酉算子，`0<r<1`。则

`U-rI` 可逆，

`(U-rI)^(-1)=sum_(m>=0)r^m U^(-m-1)`,               (6)

且

`||(U-rI)^(-1)||<=1/(1-r)`.                         (7)

若 `xi=(U-rI)eta`，则 `xi` 与 `eta` 的 bilateral `U`-orbit 生成同一
闭子空间。

#### 证明

把 `U-rI=U(I-rU^(-1))`，对严格压缩 `rU^(-1)` 使用 Neumann 级数即得
式 (6)–(7)。`xi` 显然属于 `eta` 的循环空间；式 (6) 又说明 `eta` 属于
`xi` 的循环空间。`□`

这一步是 triangular smoothing 的代数无损性：其 spectral polynomial
`z-r` 在单位圆上没有零点。它比仅说 Mellin multiplier 非零更接近
Frobenius 模的语言。

## 2. 无条件有限正 Gram 结构

对 `sigma,T>0` 与非负整数 `j,k`，先定义真正有限的 arithmetic Gram

`G_(sigma,h,T)(j,k)`

`=2sigma int_0^T d_h(t+jh)conj(d_h(t+kh))`

`                         *e^(-2sigma t)dt`.         (8)

它只使用 `x<=exp(T+(max(j,k)+1)h)` 的有限 prime 数据。若 `T->infinity`
极限收敛，记 Abel Gram entries 为

`G_(sigma,h)(j,k)`

`=2sigma int_0^infinity d_h(t+jh)conj(d_h(t+kh))`

`                         *e^(-2sigma t)dt`.         (9)

只要该积分收敛。每个有限主块记为 `G_(sigma,h)^[N]`。

### 命题 GP（finite positive dilation Grams）

1. 每个 `T<infinity` 的 `G_(sigma,h,T)^[N]` 都是只含有限 prime 数据的
   正半定矩阵；每个收敛的 `G_(sigma,h)^[N]` 也正半定；
2. infinite Abel Gram 满足精确 shift identity

   `G(j+1,k+1)=e^(2sigma h)[G(j,k)-B_(sigma,h)(j,k)]`, (10)

   其中

   `B_(sigma,h)(j,k)=2sigma int_0^h`

   `d_h(t+jh)conj(d_h(t+kh))e^(-2sigma t)dt`;        (11)

3. 对 zeta，由初等界 `psi(x)=O(x log x)`，式 (9) 至少在
   `sigma>1/2` 无条件收敛；经典定量 PNT
   `E(x)=O(x exp(-c sqrt(log x)))` 还给出 `sigma=1/2` 的收敛。

#### 证明

对任意有限向量 `a=(a_j)`，

`a*G a=2sigma int_0^infinity`

`|sum_j a_j d_h(t+jh)|^2e^(-2sigma t)dt>=0`,        (12)

证明 infinite Gram 的正性；把上限换成 `T` 同样证明 finite arithmetic
Gram 的正性。式 (10) 由 `u=t+h` 换元并减去 `[0,h]` 边界积分得到；有限
`T` 版本另有一个显式 `[T,T+h]` 上边界项，它在收敛极限消失。
初等界给 `C(X)=O(X^2log X)`，故 `d_h(t)=O(e^(t/2)(1+t))`；这给
`sigma>1/2`。定量 PNT 经一次积分给
`d_h(t)=O(e^(t/2-c' sqrt(t)))`，在 `sigma=1/2` 仍平方可积。`□`

所以有限正性不是猜想：它已经由普通 `L^2` Gram 恒等式无条件构造。
开放问题是这些正 form 能否在 `sigma downarrow0` 时不逃向无穷。

## 3. Tight Gram 极限产生归一化 Frobenius

### 定理 GQ（tight finite Grams imply a cyclic unitary structure）

固定 `h>0`。假设

`sup_(0<sigma<=sigma_0)G_(sigma,h)(0,0)<infinity`.   (13)

则存在 `sigma_n downarrow0`，使所有有限 entries 同时收敛。任一这样的
cofinal 极限满足

`G(j+1,k+1)=G(j,k)`                                 (14)

并定义一个正 Toeplitz kernel。其 GNS 完备化给出：

- 一个循环 Hilbert 空间 `H_h`；
- 一个酉 bilateral shift `U_h`；
- 一个循环向量 `xi_h`，满足

  `<U_h^j xi_h,U_h^k xi_h>=G(j,k)`.                 (15)

令 `r=e^(-3h/2)`。则

`eta_h=(U_h-rI)^(-1)xi_h`                           (16)

存在，且 `eta_h` 与 `xi_h` 生成同一个循环空间。

#### 证明

由式 (10) 的 diagonal 情形、Cauchy--Schwarz 和固定有限区间的局部平方
可积性，式 (13) 给每个固定 `j,k` 一致有界；取对角子列得到逐 entry
极限。式 (11) 含因子 `2sigma`，故该边界项在极限中消失，式 (10) 给
式 (14)。正半定性在有限矩阵极限下
保持。把指标由 `N` 按差值延拓到 `Z` 后，标准 Toeplitz GNS 构造给出酉
bilateral shift 与式 (15)。式 (16) 及循环性来自命题 GO。`□`

这是一个真正的“有限结构存在性 -> 极限 Weil 结构”定理：输入只有显式
arithmetic vectors 的有限正 Gram 与一个 tightness 界；酉 Frobenius 不是
预先指定的零点对角算子，而是由 GNS 极限产生。

## 4. 对 zeta 的中心线定理

以下固定 `h=log2`，写 `d=d_(log2)`。令

`J_sigma=2sigma int_0^infinity |d(t)|^2e^(-2sigma t)dt`. (17)

### 定理 GR（cyclic dilation-Weil criterion for RH）

下列条件等价：

1. RH 成立；
2. `J_sigma<infinity` 对每个 `sigma>0` 成立；
3. `sup_(0<sigma<=1)J_sigma<infinity`；
4. 式 (8) 的 finite arithmetic Grams 先沿 `T->infinity` 收敛，再沿
   `sigma downarrow0` tight，并由定理 GQ 产生循环酉 dilation 结构。

#### 证明：2 推出 RH

对 `Re z>0` 取 `0<sigma<Re z`。加权 Cauchy--Schwarz 证明

`L_d(z)=int_0^infinity d(t)e^(-zt)dt`               (18)

绝对收敛并解析。由式 (5) 与命题 GK，令 `s=z+1/2`，得到

`L_d(z)=2^(-3/2){[2^(s+1)-1]D(s)/[s(s+1)]`

`                         -3/[2(s-1)]}`,            (19)

其中 `D=-zeta'/zeta`。若有 `Re rho>1/2` 的非平凡零点，式 (19) 在
`z=rho-1/2` 有 pole；其 multiplier 非零，和式 (18) 的解析性矛盾。函数
方程排除中心线左侧零点。

#### 证明：RH 推出 3 和 4

对 `psi` 的经典显式公式积分一次。零点部分绝对收敛，因为其系数为

`b_gamma=-m_gamma[2^(i gamma)-2^(-3/2)]`

`                    /[rho(rho+1)]`,                (20)

而 `sum_rho |rho|^(-2)<infinity`。故

`d(t)=sum_gamma b_gamma e^(i gamma t)+o(1)`          (21)

是一个有界的 uniform almost-periodic 主项加衰减项。因此式 (17) 对
`0<sigma<=1` 一致有界，所有 Gram entries 有极限，并满足定理 GQ。

显然 3 推出 2；4 包含式 (13)，而 zeta 的大 `sigma` 收敛已由命题 GP
给出，故同样推出 2。`□`

定理 GR 没有证明 RH。它精确说明需要为已经存在的有限正 arithmetic
Grams 补上的唯一条件：临界 Abel tightness。

## 5. RH 下的谱测度与去平滑

### 命题 GS（zero spectral measure of the cyclic structure）

在 RH 下，Abel Gram 极限唯一，且

`G(j,k)=sum_gamma |b_gamma|^2 e^(i gamma(j-k)log2)`. (22)

所以 `U_(log2)` 的循环谱测度是单位圆上的纯点测度

`mu_xi=sum_gamma |b_gamma|^2 delta_(2^(i gamma))`,  (23)

相同单位圆点发生 alias 时合并其权重。对 primitive vector
`eta=(U-2^(-3/2)I)^(-1)xi`，谱测度为

`mu_eta=sum_gamma m_gamma^2/[|rho(rho+1)|^2]`

`                         *delta_(2^(i gamma))`.    (24)

#### 证明

式 (21) 的绝对一致收敛允许逐项取 Abel mean；不同 ordinates 的交叉项
趋零，得到式 (22)。命题 GO 的 functional calculus 把每个谱权除以
`|2^(i gamma)-2^(-3/2)|^2`，与式 (20) 相消，得到式 (24)。`□`

因此 triangular factor 不只是“非零”：它能由一个有界稳定 resolvent
完全移除。该循环模型会把相同 ordinate、以及离散 dilation 下的 phase
alias 压到同一谱纤维；它不编码零点的几何重数。若要恢复精确 ordinates，
可同时保留连续平移群或两个对数比为无理数的 dilation。

## 6. 广义 Gamma--Euler 结构定理

设一个 Gamma--Euler datum 的 divisor 关于 `Re s=c/2` 对称，具有文档
031/035 的有限阶显式公式，且 divisor counting 足以保证一次 Riesz
平滑后的绝对收敛。令

`kappa=c/2+1`,

`C_Z(X)=int_1^X E_Z(x)dx`,

`p_Z(t)=e^(-kappa t)C_Z(e^t)`,                       (25)

`d_(Z,h)(t)=p_Z(t+h)-e^(-kappa h)p_Z(t)`.           (26)

### 定理 GT（general cyclic dilation-Weil structure theorem）

若对某个 `h>0`，

`2sigma int_0^infinity |d_(Z,h)(t)|^2e^(-2sigma t)dt` (27)

对每个 `sigma>0` 有限，则全部非平凡 divisor points 位于
`Re s=c/2`。若这些 Abel Grams 在 `sigma downarrow0` 还一致 tight，则它们
产生定理 GQ 的循环 Hilbert 空间，归一化 dilation `U_h` 酉，并且

`d_(Z,h)=(U_h-e^(-(c/2+1)h)I)eta_Z`.                (28)

反之，若中心线结论成立并满足上述标准 counting 条件，则式 (27) 一致
tight，所得 spectral points 为

`e^((rho-c/2)h)`,                                   (29)

故都在单位圆上。

#### 证明

式 (27) 对所有 `sigma` 的有限性使 `d_(Z,h)` 的 Laplace transform 在
`Re z>0` 解析。一个 divisor point `rho` 给出的 pole multiplier，在忽略
不影响 poles 的低端 entire correction 后，是

`e^((rho-c/2)h)-e^(-(c/2+1)h)`.                    (30)

它只能在 `Re rho=-1` 时为零，故在标准非平凡条带不消去任何右侧 point。
于是排除 `Re rho>c/2`，再由 divisor 对称排除左侧。tight GNS 与稳定
逆由定理 GQ、命题 GO 给出。中心线成立时，一次 Riesz 平滑使 divisor
展开绝对收敛，得到有界 almost-periodic signal 与式 (29)。`□`

GT 抽离出的 Weil 机制可以画成

`finite arithmetic Gram positivity`

`       + critical tightness`

`       -> cyclic GNS + unitary normalized dilation`

`       -> divisor purity / center line`.           (31)

它适用于标量或有限向量值 Euler 数据；向量情形把绝对值换成普通正定
Hermitian Gram 即可。

## 7. 存在性审计与下一输入

对经典 zeta，目前已经无条件得到：

1. `C(X)`、`d_h(t)` 和每个有限 quadrature Gram 都是有限 prime--continuum
   公式；
2. 所有这些有限 Grams 正半定；
3. 真 Abel Gram 在 `sigma>=1/2` 收敛；
4. `U-r` 的稳定逆常数恰为 `1/(1-r)`，不存在高模态放大灾难。

尚未得到的是把存在区间从 `sigma>=1/2` 推到任意 `sigma>0`，或等价地
证明 `sigma downarrow0` tightness。定理 GR 说明这一步具有 RH 的全部
强度，不能把它当作普通 compactness 引理。

但这个 formulation 比裸增长判据多提供两个可攻击接口：

- finite Gram/Toeplitz determinants：可尝试用 prime blocks、large sieve
  或 total positivity 给出与截断无关的上界；
- stable resolvent：可以先控制 triangular vector `xi`，再无损恢复
  primitive vector `eta`，无需逐个反演零点 multiplier。

数值脚本实现式 (2)–(5) 以及任意有限正 quadrature Gram。数值正性只审计
公式，不是 tightness 证书或 RH 证据。

例如取 `q=2`、四个 orbit vectors、采样 `t=0,0.1,...,2`，正权
`e^(-t/3)`，所得 Gram 本征值为

`6.753742e-5, 1.746676e-4, 5.148954e-4, 3.514065e-1`. (32)

它们的和为 `0.352163556`。这验证该有限 quadrature 的严格正性；它没有
控制采样长度趋于无穷或 `sigma downarrow0`，因而不提供 RH 的数值证书。
