# Bounded Cauchy defect 已足够：normality 与有限深度判据

文档 136 的 filtered passive theorem要求 `J_n->0`，因为它要在极限中得到
`Re F>=0`。但对中心线结论而言，positive-real其实不是最后一步所必需：只要
arithmetic logarithmic derivative germ能 **holomorphically** 延拓到整个右
半平面，就已经排除了右半平面 zeros；self-duality再排除左半平面 zeros。

本节利用这一点把文档 143 的 fully finite condition从

`negative Cauchy mass ->0`                       (1)

严格放宽为

`negative Cauchy mass stays bounded`.             (2)

所以要构造数域 Weil结构，不必先证明近似 Hodge forms渐近非负；证明其 worst
negative depth沿一条 cofinal filtration不向 `-infinity` 逃逸已经足够。

## 1. Lower-real-part normality lemma

### 引理 ZT1（one-point Carathéodory normality）

设 `Omega` 是 connected domain，`f_n` holomorphic于 `Omega`。若：

1. 对每个 compact `K subset Omega` 存在 `A_K<infinity`，使
   `Re f_n(z)>=-A_K` on `K`；
2. 在某个 `z_0 in Omega`，序列 `f_n(z_0)` bounded；

则 `{f_n}` locally bounded，因而是 normal family。

#### 证明

先在圆盘 `D(c,R)` 上假设 `Re f_n>=-A` 且 `f_n(c)` bounded。令
`g_n=f_n+A`。对 `0<r<R`，positive-real Carathéodory estimate给

`|g_n(z)-i Im g_n(c)|`

` <=[(R+r)/(R-r)]Re g_n(c)`, `|z-c|<=r`.          (3)

所以 `f_n` 在 `D(c,r)` 一致有界。由 `Omega` connected，任意 compact `K`
可用从 `z_0` 出发的有限 overlapping disk chains覆盖。上一圆盘的 bound给下一
圆盘中心值的 bound；逐盘应用式 (3)，得到 `K` 上的一致 bound。Montel theorem
给 normality。`□`

注意这里只需要 lower bound；不需要 `Re f_n` 的负部趋零。

## 2. Bounded-defect Weil structure theorem

沿用文档 136。令 `F_n` 是 `C_+` 上 holomorphic arithmetic candidates，
`delta_n->0`，并写

`J_n=int_R[-Re F_n(delta_n+it)]_+/(1+t^2)dt`.      (4)

假设 Poisson admissibility：对 `x>delta_n`，

`Re F_n(x+iy)>=-(1/pi)int_R (x-delta_n)W_n(t)`

`                         /[(x-delta_n)^2+(y-t)^2]dt`, (5)

其中 `W_n=[-Re F_n(delta_n+it)]_+`。

### 定理 ZT（bounded-defect normal Weil theorem）

设：

1. `{F_n}` 满足式 (5)；
2. 在非空 open set `U subset C_+`，`F_n` locally uniformly收敛到 arithmetic
   germ `F_ar`；
3. `sup_n J_n<infinity`。

则 `{F_n}` 在整个 `C_+` locally uniformly收敛到 `F_ar` 的唯一 holomorphic
continuation。

若 `F_ar=Phi'/Phi`，其中 `Phi` 是 real-type、center-self-dual、order至多一的
entire divisor，则 `Phi` 的全部非零 zeros位于中心轴。

#### 证明

固定 compact `K subset C_+`。当 `n`充分大时，`x-delta_n`在 `K` 上有正
下界。和文档 136 式 (18)相同，存在 `C_K` 使 Poisson kernel满足

`(x-delta_n)/[(x-delta_n)^2+(y-t)^2]`

` <=C_K/(1+t^2)`.                                 (6)

由式 (4)--(6)及 `sup J_n<infinity`，得到

`Re F_n(z)>=-A_K` on `K`                          (7)

且 `A_K`与 `n` 无关。在 `U` 取一个基点；germ convergence使该点的
`F_n` bounded。引理 ZT1给 local boundedness与 normality。

任意 subsequential limit在 `U` 上等于 `F_ar`；identity theorem说明全部
subsequential limits相同，故整个序列 locally uniformly收敛到唯一 holomorphic
continuation `F`。

若 `F_ar=Phi'/Phi`，则 meromorphic continuation的 uniqueness给
`F=Phi'/Phi` wherever右侧有定义。若 `Phi` 在 `C_+` 有 zero，右侧在那里有
nonremovable pole，不可能等于 holomorphic `F`。故右半平面无 zeros；
self-duality把任意左半平面 zero反射到右半平面，所以全部 zeros位于中心轴。
`□`

定理 ZT 与文档 136 定理 YL的区别是：

- `J_n->0` 给 positive-real continuation及 positive Pick/Hodge structure；
- `sup J_n<infinity` 只给 holomorphic continuation，但这已经足以证明中心线
  purity。

因此 bounded negative depth 是比 asymptotic positivity 更弱、但仍具有完整
RH力量的广义结构。

## 3. RH 失败会迫使 defect 共尾发散

对 zeta 的 Abel candidates `F_Y`，Poisson admissibility与 Euler-open-set
convergence均由文档 136 无条件成立。

### 定理 ZU（cofinal divergence alternative）

若 RH不成立，则

`J_(Y,delta)->infinity`                            (8)

当 `Y->infinity`, `delta->0`，这里是 directed/cofinal意义：对每个
`M<infinity`，存在 `Y_M,delta_M>0`，使

`J_(Y,delta)>M`                                   (9)

只要 `Y>=Y_M`, `0<delta<=delta_M`。

同一结论适用于定理 ZT hypotheses下任何具有 off-center zero的 self-dual
Gamma--Euler divisor。

#### 证明

若式 (9)对某个 `M`失败，则对每个 integer `n` 可选

`Y_n>=n`, `0<delta_n<=1/n`, `J_(Y_n,delta_n)<=M`. (10)

这是一条 bounded-defect cofinal sequence；定理 ZT推出 RH，矛盾。一般情形
相同。`□`

这严格加强文档 144 定理 ZS 的 fixed positive gap。文档 144 的 residue-wave
分析在 rightmost layer可分离时进一步给 polynomial/exponential growth rate；
定理 ZU不需要 supremum达到，却不给显式 `M ->(Y_M,delta_M)` rate。

## 4. Fully finite bounded-depth criterion

沿文档 142--143 的 shared stationary quadrature，令 `v_n^sample` 是 finite
symbol的 midpoint negative-part sum，`E_n` 是 arithmetic quadrature、height
grid与tails的 total uniform error。exact stationary identity给

`|v_n^sample+J_n/pi|<=E_n`.                       (11)

### 定理 ZV（fully finite bounded-depth center-line criterion）

若沿任一 cofinal schedule：

`E_n->0`,                                         (12)

`inf_n v_n^sample> -infinity`,                    (13)

则相应 divisor的全部 zeros位于中心线。

反之，若存在 off-center zero，则每条满足式 (12)的 cofinal schedule都有

`v_n^sample->-infinity`.                           (14)

#### 证明

由式 (11)--(13)，

`J_n/pi<=-v_n^sample+E_n`                         (15)

一致有界；应用定理 ZT。若有 off-center zero，定理 ZU给 `J_n->infinity`，
再由式 (11)--(12)得到式 (14)。`□`

定理 ZV 比文档 143 定理 ZM 的 `v_n^sample>=-epsilon_n`, `epsilon_n->0`
严格弱。新的 finite target不再是证明 grids趋于非负，只需找一个与 filtration
无关的 finite lower floor。

实现 `zeta_abel_shared_stationary_certificate` 现在返回式 (11)对应的

- `cauchy_defect_over_pi_lower_bound`；
- `cauchy_defect_over_pi_upper_bound`；
- 乘回 `pi` 的 defect bounds；
- `total_functional_error_bound`。

这些仍是给定参数的 formula-level floating audit，不是 interval enclosure。

## 5. 对存在性问题的改变

此前 prime-side目标是 one-sided estimate

`int P_Y(t)_-dmu(t)=o(1)`.                        (16)

现在只需

`int P_Y(t)_-dmu(t)=O(1)`                         (17)

沿一条 cofinal schedule。虽然定理 ZT说明式 (17)仍有 RH强度，但它允许：

1. bounded数量的 persistent resonance wells；
2. 非恒定 passive-limit所必需的固定 variance；
3. Hodge form具有统一有限 negative depth，而不是逐层趋于 exact positivity。

文档 146 已执行第一步：Cauchy--Schwarz把 bounded negative depth降为 finite
symbol的 exact positive Cauchy second moment `O(1)`，并用 ratio-kernel Gram
在 `O(m logm)` 时间计算。后续应把该能量按 prime--continuum--Gamma signed
blocks展开，检查文档 036--047 与 070 的 Green/Selberg estimates能否控制它。
