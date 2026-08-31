# Abel resonance density 与 weighted-prolate Hodge core

文档 132 发现 exponential Abel impedance 在固定低高度 Pick set 上趋于被动，
却在随 scale 移动的 heights 产生强负 resonance wells。本节证明这些 wells
并非任意占据高频窗口：在任何固定横向裕量 `Re z>=delta>0` 上，它们的
相对测度是 `O_(delta,M)(log(T)^(-2))`，负部总质量是
`O_(delta,M)(T/log T)`（横坐标限制在固定 compact
`delta<=Re z<=M`）。

后一个 `L^1` bound 比单纯测度更适合 Hodge 理论。它使带限负乘法算子成为
trace class；剥离一个相对 Shannon dimension 为 `O(log(T)^(-1/2))` 的显式
weighted-prolate core 后，余空间负误差同样只有 `O(log(T)^(-1/2))`。
所以 Abel resonance 在每个高窗口上已被无条件压缩为“相对秩与误差同时趋零”
的有限核心。尚未解决的是这些 cores 随 `Y->infinity` 的总复杂度与 Feshbach
耦合。

## 1. Abel prime polynomial 与 archimedean barrier

固定 `0<delta<M<infinity`，令

`z=x+it`, `delta<=x<=M`, `s=1/2+z`,                 (1)

并沿用文档 132 的

`F_Y(z)=A_infinity(s)+I_Y(s)-P_(Y,x)(t)`,           (2)

其中

`A_infinity(s)=1/s-(1/2)log pi+(1/2)psi(s/2)`,     (3)

`I_Y(s)=int_1^infinity u^(-s)e^(-u/Y)du`,           (4)

`P_(Y,x)(t)=sum_(n>=2)Lambda(n)n^(-1/2-x)`

`                              *e^(-n/Y)e^(-itlog n)`. (5)

对 `delta<=x<=M`，coefficient square mass 有不依赖 `Y` 的初等上界

`B_2(Y,x)=sum_n Lambda(n)^2 n^(-1-2x)e^(-2n/Y)`

` <=sum_(n>=2)(log n)^2 n^(-1-2delta)=C_delta<infinity`. (6)

另一方面，uniform digamma asymptotic 给任意固定 `x` compact 上

`Re A_infinity(1/2+x+it)=(1/2)log(|t|/(2pi))+O_delta(1/|t|)`. (7)

把式 (4) 写成 `u=e^v` 后积分一次分部，得到

`|I_Y(1/2+x+it)|`

` <=C_(delta,M)(1+Y^(1/2-delta))/|t|`.              (8)

因此只要 `T` 相对 `Y` 足够大，在 `T<=|t|<=2T` 上

`Re[A_infinity(s)+I_Y(s)]>=c log T`                 (9)

可取某个绝对 `c>0`；下面固定例如 `c=1/4`，把有限小参数吸收到阈值中。

## 2. Exponentially weighted Dirichlet mean square

取

`N=ceil(Y log^2(YT))`，                              (10)

并把式 (5) 截为 `P_N`。由 `Lambda(n)<=log n`，tail 满足

`|P_(Y,x)(t)-P_N(t)|`

` <=int_N^infinity log(u)u^(-1/2-delta)e^(-u/Y)du`, (11)

在 `Y,T->infinity` 时比任意固定 `log T` 阈值小；指数 `e^(-N/Y)` 是
`e^(-log^2(YT))`。

### 引理 XY（Abel Dirichlet mean-square bound）

若 `T>=8NH_N`，则 uniformly for `delta<=x<=M`，

`int_T^(2T)|P_(Y,x)(t)|^2dt<=C_delta T`.            (12)

同一结论适用于 `[-2T,-T]`。

#### 证明

对 `P_N` 展开平方。diagonal 是

`T sum_(n<=N)|a_n|^2`。

非 diagonal pair 的 oscillatory integral绝对值至多
`2/|log(n/m)|`；使用

`log(n/m)>=(n-m)/N`                                 (13)

与 `2|a_ma_n|<=|a_m|^2+|a_n|^2`，得到

`int_T^(2T)|P_N(t)|^2dt`

` <=(T+4NH_N)sum_(n<=N)|a_n|^2`.                   (14)

式 (6) 与 `T>=8NH_N` 给 `O_delta(T)`。式 (11) 的 uniform tail 对整个
窗口的平方积分为 `o(T)`，吸收进常数。`□`

这里不使用 PNT、zero-free region 或 zeros；只用 coefficient bound与有限
Dirichlet polynomial 的 elementary Hilbert estimate。

文档 150 随后用 Montgomery--Vaughan weighted Hilbert inequality把式 (14)的
`NH_N` 改进为 `N`，并将此改进用于 Cauchy negative trace的平方根 localization。

## 3. 负井测度与负质量

定义窗口负部

`W_(Y,x,T)(t)=[-Re F_Y(x+it)]_+ 1_[T,2T](t)`,       (15)

以及其支撑 `E_(Y,x,T)`。

### 定理 XZ（Abel negative-well density and mass）

固定 `0<delta<M`。存在常数 `C_(delta,M),T_(delta,M)`，使对
`Y>=2`、`delta<=x<=M`、

`T>=max(T_(delta,M), C_(delta,M)Y log^3(YT))`       (16)

都有

`|E_(Y,x,T)|<=C_(delta,M)T/log^2 T`,                (17)

`int_T^(2T)W_(Y,x,T)(t)dt<=C_(delta,M)T/log T`.     (18)

#### 证明

式 (16) 保证 `T>=8NH_N` 并使式 (8)、(11) 都小于式 (9) 的一半。若
`Re F_Y<0`，则式 (2)、(9) 强迫

`|P_(Y,x)(t)|>=c log T`.                            (19)

Chebyshev 与引理 XY 给

`|E| c^2log^2T<=int_T^(2T)|P|^2<=C_delta T`,       (20)

即式 (17)。在 `E` 上，

`W<=|P|1_E`.                                       (21)

Cauchy--Schwarz、式 (12) 与 (17) 给

`int W<=(int|P|^2)^(1/2)|E|^(1/2)`

`      <=C_delta T/log T`,                         (22)

得到式 (18)。`□`

密度 `O(log^(-2)T)` 与负质量 `O(log^(-1)T)` 是不同层次：前者只说明井
稀疏，后者能直接控制 weighted concentration operator 的 trace。

## 4. Weighted-prolate core theorem

令 `H_B=L^2([-B,B])`，Fourier convention 为

`hat f(t)=int_(-B)^B f(y)e^(-ity)dy`,               (23)

所以 `int|hat f|^2/(2pi)=||f||^2`。对任意
`W>=0`, `W in L^1(R)`，定义 positive compact operator

`C_W=(1/(2pi))F^*M_WF`.                             (24)

其 quadratic form 是

`<C_Wf,f>=int W(t)|hat f(t)|^2dt/(2pi)`.            (25)

### 定理 YA（weighted resonance Hodge-core theorem）

`C_W` 是 positive trace class，且

`Tr C_W=(B/pi)int_R W(t)dt`.                        (26)

给定 `epsilon>0`，令 `Q_(W,epsilon)` 为 `C_W` 的 eigenvalues
`>epsilon` 所对应空间，则

`dim Q_(W,epsilon)<=B/(pi epsilon)int W`,           (27)

并对 `f perpendicular Q_(W,epsilon)`，

`int W|hat f|^2dt/(2pi)<=epsilon||f||^2`.           (28)

#### 证明

式 (24) 的 integral kernel在 diagonal `y=y'` 上恒为

`(1/(2pi))int W`。对长度 `2B` 的区间积分给式 (26)。positive eigenvalues
之和等于 trace，所以大于 `epsilon` 的 eigenvalue个数至多
`Tr C_W/epsilon`，给式 (27)。在其正交补上用 spectral theorem 得式
(28)。`□`

这是文档 019 multiwell prolate theorem 的 weighted、无需先分井版本；其
eigenvectors 是负 multiplier 自身决定的 generalized prolate modes。

## 5. Abel resonance core 的相对秩

把定理 YA 用于式 (15)，再代入定理 XZ。

### 推论 YB（vanishing-error, density-zero Abel core）

在定理 XZ 条件下，取

`epsilon_T=(log T)^(-1/2)`.                         (29)

则存在一个显式 weighted-prolate core `Q_(Y,x,T)`，使

`dim Q_(Y,x,T)<=C_(delta,M)B T/sqrt(log T)`,        (30)

且在其正交补上

`int_T^(2T)W_(Y,x,T)|hat f|^2dt/(2pi)`

` <=(log T)^(-1/2)||f||^2`.                        (31)

窗口 `[T,2T]` 的 Shannon dimension 是 `asymp BT`，所以 core 的相对
dimension 与余空间负误差同时以 `O_(delta,M)(log(T)^(-1/2))` 趋零。

#### 证明

式 (18) 代入式 (27)，再取式 (29) 即得式 (30)；式 (31) 是定理 YA。
`□`

对固定 `Y,x`，prime polynomial 的 absolute mass有限，而 archimedean
barrier按 `(1/2)log|t|` 增长，所以 `W_(Y,x)(t)` 最终恒为零。故只有有限多个
dyadic windows需要 cores；合并后仍是有限维。这比文档 021 的一般
finite-codimension theorem多给了高窗口的相对秩衰减，但尚未给
`Y->infinity` 时的统一总秩。

## 6. 有限 resonance audit

代码新增：

- `zeta_abel_resonance_well_audit`：一次组装 Abel prime coefficients，扫描
  vertical window，返回 sampled wells、负质量、coefficient square mass、
  elementary mean-square bound 与解析 prime tail；
- `weighted_prolate_core_rank_bound`：实现式 (26)--(28) 的 trace/rank账本。

对文档 132 的 `Y=100,x=0.005,N=4000`，在 `[35,75]` 以 step `0.25`
扫描，得到：

- `23` 个 sampled negative components；
- sampled negative measure `13.25`；
- sampled negative mass `3.9821`；
- minimum `-0.76836` at `t=66`；
- prime tail bound `5.30e-17`。

这些 sampled measure/mass 是网格诊断，不是式 (17)--(18) 的 rigorously
enclosed integrals。若仅把 sampled mass代入 `B=2`、
`epsilon=1/sqrt(log75)=0.4813` 的 trace账本，得到 rank bound `6`；它说明
weighted core如何计算，但不是连续负集的 interval certificate。

## 7. 剩余 cofinal 障碍

本节无条件得到每个高窗口上的

`sparse negative wells`

` -> small L1 negative mass`

` -> trace-class weighted concentration`

` -> relative-rank-zero Hodge core`.               (32)

这解决了 Abel resonance 的 **余空间** 问题，但没有证明 RH，因为：

1. 负 support 的最高 frequency对 `Y` 的粗 bound仍可为
   `exp(O(Y^(1/2-delta)log Y))`；
2. 把所有 dyadic cores合并后的绝对 dimension尚无 cofinal bound；
3. core restriction 的 positivity及 core--complement Feshbach coupling尚未
   认证；
4. 最终必须令 `delta downarrow0`，而式 (6) 的 `C_delta` 会发散。

下一输入应把定理 YB 与文档 024 residual--Feshbach certificate结合：不用控制
core 的裸维数，而控制其 weighted residual Gram trace/Schatten norm，并寻找
对 `delta downarrow0` 稳定的 renormalized metric。若该 residual trace可沿
cofinal `(Y,delta,T)` 取到 `o(1)`，文档 015 的过滤结构定理即可推出 RH。
