# Ratio-kernel tail square、临界正谱 no-go 与正背景重整化

文档 146 得到一个形式上很诱人的充分条件：finite symbol的 full Cauchy second
moment若一致有界，就能推出 RH。本节把该能量完全平方化，并据此发现它对 zeta
仍然过强：若 RH成立，临界线 zeros产生的 **正** Poisson spikes已迫使 full
second moment发散；若 RH不成立，文档 146 定理 ZY又由负 defect迫使它发散。

所以 full quadratic energy无论 RH真假都会发散，不能作为 zeta 存在性证明。
可保留的结构是它的 exact tail square，以及“先抽出一个非负 arithmetic
background，再只控制 residual energy”的重整化判据。

## 1. Ratio kernel 的 exact tail-square factorization

令 `nu` 是 `[0,infinity)` 上 finite complex measure，并定义

`A(nu)=int_0^infinity e^(-lambda)dnu(lambda)`,      (1)

`T_nu(u)=int_[u,infinity)e^(u-lambda)dnu(lambda)`. (2)

elementary kernel identity为

`e^(-|lambda-kappa|)=e^(-lambda-kappa)`

` +2int_0^min(lambda,kappa)e^(2u-lambda-kappa)du`. (3)

### 定理 ZZ（Cauchy--Green tail-square theorem）

有

`iint e^(-|lambda-kappa|)dnu(lambda)dconj(nu)(kappa)`

` =|A(nu)|^2+2int_0^infinity|T_nu(u)|^2du`.        (4)

若

`Q_nu(t)=int e^(-itlambda)dnu(lambda)`,

`P_nu(t)=Re Q_nu(t)`,                              (5)

则

`int_RP_nu(t)^2dt/[pi(1+t^2)]`

` =[Re A(nu)]^2+int_0^infinity|T_nu(u)|^2du`.     (6)

#### 证明

把式 (3)代入左侧并用 Fubini；第一项给 `|A|^2`，第二项恰给式 (2)的
absolute square积分，得到式 (4)。文档 146 定理 ZW给

`E_2(P)=[M_abs+Re A^2]/2`。                       (7)

将式 (4)代入，并用
`(|A|^2+Re A^2)/2=(Re A)^2`，即得式 (6)。`□`

实现 `stationary_cauchy_symbol_moments` 新增
`cauchy_green_tail_energy` 与 `cauchy_boundary_real_square`，逐项核对式 (6)。

## 2. Prime--continuum block 是加权 Chebyshev tail current

只看 Abel continuum减prime measure：

`dnu_(pc,Y)(lambda)`

` =e^((1-sigma)lambda)e^(-e^lambda/Y)dlambda`

` -sum_(n>=2)Lambda(n)n^(-sigma)e^(-n/Y)delta_(logn)`, (8)

其中 `sigma=1/2+delta`。令 `E(x)=psi(x)-x`，并取一致的 endpoint convention。

### 命题 ZZ1（multiplicative tail-current identity）

对 `x=e^u>=1`，

`T_(pc,Y)(logx)`

` =x[int_x^infinity y^(-sigma-1)e^(-y/Y)dy`

`   -sum_(n>=x)Lambda(n)n^(-sigma-1)e^(-n/Y)]`    (9)

` =-xint_[x,infinity)y^(-sigma-1)e^(-y/Y)dE(y)`. (10)

因此该 block的 Green tail energy为

`int_1^infinity x`

` *|int_[x,infinity)y^(-sigma-1)e^(-y/Y)dE(y)|^2dx`. (11)

#### 证明

式 (2)中令 `y=e^lambda`。continuous term变成
`xint_x^infinity y^(-sigma-1)e^(-y/Y)dy`；每个 `logn>=logx` 的 atom
变成式 (9)的 discrete tail。两者之差是 `dE=dpsi-dy` 的负 Stieltjes
integral，给式 (10)。最后 `du=dx/x`，代入式 (6)的 tail integral得到
式 (11)。`□`

式 (11)严格保留 prime--continuum cancellation；分别取 absolute values会退化
成无用的 `Y^(1/2)` 级 bound。它与文档 035--037 的 Chebyshev Abel current、
文档 047 的 ratio Green kernel是同一个 multiplicative Hodge geometry。

## 3. RH 分支中的 positive boundary spike

设 `rho=1/2+i gamma` 是一个 `m>=1` 重 critical-line zero。写

`F(z)=xi'(1/2+z)/xi(1/2+z)`。在 `z=i gamma` 附近

`F(delta+i(gamma+v))=m/(delta+iv)+H(delta+iv)`,    (12)

其中 `H` locally bounded。因此对充分小 `delta` 与 `|v|<=delta`，

`Re F(delta+i(gamma+v))>=m/(4delta)`.              (13)

在 RH 下，`E(x)=psi(x)-x=O(sqrt(x)log^2x)`。文档 132 的 partial-summation
argument对 moving line给显式误差

`sup_(|v|<=delta)|F_Y(delta+i(gamma+v))-F(delta+i(gamma+v))|`

` <=C_gamma Y^(-delta)delta^(-3)(1+logY)^2+O(Y^-1)`. (14)

这里把 `|1-e^(-x/Y)|` 在 `x<=Y` 用 `x/Y`，在 `x>=Y` 用 `1`，再分别积分
`x^(-1-delta)log^2x`；第二个 differentiated cutoff term同阶。

### 定理 ZZ2（critical positive-spectrum quadratic no-go）

假设 RH，并取

`delta_Y->0`,

`Y^(-delta_Y)delta_Y^(-3)(1+logY)^2->0`.           (15)

令 finite shared symbols `P_Y` 对 exact arithmetic functional有 uniform capped
error `eta_Y->0`。则存在 `c_rho>0` 使

`E_2(P_Y)>=c_rho/delta_Y`                         (16)

对充分大 `Y` 成立。

#### 证明

式 (14)--(15)把式 (13)传给 Abel candidate boundary value
`u_Y(t)=Re F_Y(delta_Y+it)`；缩小常数后，在
`I_Y=[gamma-delta_Y,gamma+delta_Y]` 上

`u_Y(t)>=m/(8delta_Y)`.                            (17)

Cauchy measure在该固定高度邻域与 Lebesgue measure等价，所以

`int_(I_Y)u_Ydmu>=c_0>0`,

`mu(I_Y)<=C_0delta_Y`.                             (18)

uniform capped error意味着

`sup_(0<=theta<=1)|int(u_Y-P_Y)theta dmu|<=eta_Y`. (19)

分别取 positive/negative selectors可得
`int|u_Y-P_Y|dmu<=2eta_Y`。由式 (18)--(19)，最终

`int_(I_Y)|P_Y|dmu>=c_0/2`.                       (20)

在 `I_Y` 上用 Cauchy--Schwarz：

`E_2(P_Y)>=int_(I_Y)P_Y^2dmu`

` >=(c_0/2)^2/mu(I_Y)>=c_rho/delta_Y`.            (21)

`□`

文档 143 的 schedule `delta_Y=1/(4+sqrt(logY))` 满足式 (15)。

### 推论 ZZ3（full quadratic energy diverges regardless of RH）

沿任何满足文档 143 shared error `eta_Y->0` 及式 (15)的 cofinal schedule，
zeta finite symbols满足

`E_2(P_Y)->infinity`.                              (22)

#### 证明

若 RH成立，用定理 ZZ2。若 RH不成立，文档 146 定理 ZY由 negative defect
divergence给同一结论。`□`

所以文档 146 定理 ZX 是正确的广义充分定理，但其 hypothesis对这列 zeta
candidates永远不成立。固定 `delta=.1` 的 `.07--.12` 数值稳定只说明尚未进入
boundary spike regime。

## 4. 正背景 residual 才是可行的 quadratic 结构

full square失败是因为它同时惩罚 positive与negative spectrum。令

`P_n=B_n+R_n`, `B_n(t)>=0`.                        (23)

则 pointwise

`(P_n)_-<=(R_n)_-<=|R_n|`.                         (24)

### 定理 ZZ4（positive-background bounded-residual Weil criterion）

在文档 145 定理 ZT hypotheses下，若 arithmetic symbols有式 (23)的构造，
shared functional error `eta_n=O(1)`，且

`sup_n int_RR_n(t)^2dmu(t)<infinity`,              (25)

则 divisor全部 zeros位于中心线。

若 `B_n` 与 `R_n` 都由 finite orbit coefficients给出，式 (25)可用文档 146
定理 ZW的 exact Gram和本节定理 ZZ的 tail squares完全有限计算。

#### 证明

式 (24)、Cauchy--Schwarz与 shared error给

`J_n/pi<=sqrt(int R_n^2dmu)+eta_n=O(1)`.           (26)

应用文档 145 定理 ZT。`□`

定理 ZZ4准确恢复 Weil/Hodge机制：允许一个能量发散但已知非负的“纯谱/Hodge
background”承载中心线 zeros，只要求未解释 residual具有 bounded depth。

## 5. 新的存在性边界

对 zeta，不能把 `B_Y` 定义为“临界线 zeros的 Poisson sum”，因为这会预先使用
所求 divisor。有效构造必须从 primes/Gamma 或 finite positive squares独立得到
`B_Y>=0`。候选来源包括：

1. 文档 016--024 的 prime graph/archimedean positive polarization；
2. 文档 029 的 canonical positive part，但必须避免通过未知 spectral sign循环定义；
3. 文档 035--037 的 Chebyshev Green current中可由已知 pole/Gamma channels
   明确分离的 positive background。

剩余任务不再是证明 full ratio energy `O(1)`，而是构造一个 noncircular positive
background，使 **signed prime--continuum--Gamma residual** 的 ratio-tail energy
统一有界。文档 148已把该 background规范化为 negative-coefficient unitary
orbit edges产生的 graph Laplacian，并把充分条件写成 bounded degree anomaly加
两个 positive orbit Laplacians之间的 Loewner domination。
