# 层集 barrier--capacity 与 Abel defect 的平方根核心

文档 149 把数域 Hodge 结构的正确全局量确定为 Cauchy finite trace

`kappa_mu(H)=int_R H_-(t)dmu(t)`,

`dmu(t)=dt/[pi(1+t^2)]`.                           (1)

本节把该 trace拆成可加的高度块，并保留 Dirichlet mean-square估计中的
off-diagonal项，并用 Montgomery--Vaughan weighted Hilbert inequality将其
从粗 `N log N` 降到标准的 `N`。结果是一个新的无条件 localization：zeta Abel
candidate尚未控制的频率核心可从旧的 `Y polylog Y` 缩到

`sqrt(Y) delta^(-3/2)log Y`.                      (2)

这没有证明 RH，但把真正需要新 arithmetic cancellation的范围缩短了近一个
平方根。

## 1. Negative trace 的层集与分块恒等式

令 `(X,mu)` 是 probability space，`H:X->R` measurable且 `H_- in L1(mu)`。

### 定理 AAH（layer-cake Hodge-index identity）

有

`kappa_mu(H)=int_X H_-dmu`

` =int_0^infinity mu{x:H(x)<-u}du`.                (3)

若 `X` 被 measurable blocks `I_j` 分割，则

`kappa_mu(H)=sum_j int_(I_j)H_-dmu`.               (4)

对 Cauchy measure及 symmetric height shell

`I(T)={t:T<=|t|<2T}`, `T>0`,                      (5)

若 `M(T)=int_(I(T))H_-(t)dt`，则

`int_(I(T))H_-dmu<=M(T)/[pi(1+T^2)]`.             (6)

#### 证明

式 (3) 是 `H_-(x)=int_0^infinity 1_(H(x)<-u)du` 与 Tonelli theorem。
式 (4) 再用 nonnegative additivity；式 (6) 来自 shell上
`dmu/dt<=1/[pi(1+T^2)]`。`□`

式 (3)说明“井深 × 井宽”并非比喻，而是 negative Hodge index的 exact spectral
distribution formula。

## 2. Barrier 把 `L^p` 能量转成 negative capacity

考虑一个有限 Lebesgue-measure block `I`，并写

`H(t)=A(t)+R(t)+Re Q(t)`,                          (7)

其中 `A(t)>=b>0`, `|R(t)|<=r<b`。令 `beta=b-r`。

### 引理 AAI（`L^p` barrier--capacity inequality）

对任意 `p>1`，若 `E_p=int_I|Q(t)|^pdt<infinity`，则

`int_I H_-(t)dt`

` <=c_p E_p/beta^(p-1)`,                          (8)

其中

`c_p=(p-1)^(p-1)/p^p`.                            (9)

特别地，`p=2` 时常数为 `1/4`。

#### 证明

若 `H(t)<0`，则由式 (7)有

`H_-(t)<= (|Q(t)|-beta)_+`.                       (10)

对 `x>=0`，函数 `(x-beta)_+/x^p` 在
`x=p beta/(p-1)` 达到最大值 `c_p/beta^(p-1)`。逐点代入并积分即得式 (8)。`□`

相较于先用 Chebyshev估井宽、再用 Cauchy--Schwarz，式 (8)一步给出同阶结果，
并显式允许以后使用高矩或 mixed moments。

## 3. 可加的 block bounded-index Weil theorem

令 `F_n` 满足文档 145 定理 ZT的 Poisson admissibility与 Euler-germ convergence，
令 `H_n(t)=Re F_n(delta_n+it)`。取 core `|t|<T_(n,0)` 与 dyadic shells

`I_(n,k)={2^kT_(n,0)<=|t|<2^(k+1)T_(n,0)}`.      (11)

在每个 shell假设有式 (7)，参数记为 `beta_(n,k),p_(n,k),E_(n,k)`。

### 定理 AAJ（block-capacity bounded-index Weil theorem）

若存在 `B<infinity` 使

`int_(|t|<T_(n,0))(H_n)_-dmu`

` +sum_(k>=0) c_(p_(n,k))E_(n,k)`

`  /[pi(1+(2^kT_(n,0))^2)beta_(n,k)^(p_(n,k)-1)]`

` <=B`                                             (12)

对所有 `n` 成立，则相应 self-dual divisor的全部 zeros位于中心线。

#### 证明

对每个 shell应用引理 AAI，再用定理 AAH式 (6)求和，得到
`sup_n int(H_n)_-dmu<=B`，即 `sup_nJ_n<=pi B`。应用文档 145 定理 ZT，或等价地
应用文档 149 定理 AAE。`□`

这是一条真正可模块化的广义结构定理：有限域 Hodge positivity使每块为零；数域
允许非零甚至加深的 negative blocks，只要求其 spectral capacities可和。

## 4. Montgomery--Vaughan 中高频 mean square

沿用文档 133 的 zeta Abel decomposition

`F_Y=A_infinity+I_Y-P_Y`.                          (13)

取 `x=delta`。截断

`P_N(t)=sum_(n<=N)Lambda(n)n^(-1/2-delta)e^(-n/Y)e^(-itlogn)`.

文档 133 引理 XY的 elementary proof在施加 `T>=8NH_N` 之前给出

`int_T^(2T)|P_N(t)|^2dt`

` <=(T+4NH_N)sum_(n<=N)|a_n|^2`.                  (14)

这里可使用更强的 Montgomery--Vaughan weighted Hilbert inequality（文献 23）。
标准 Dirichlet-polynomial mean-value consequence是，对任意长度 `T` 的区间，

`int |P_N(t)|^2dt`

` <=Tsum_(n<=N)|a_n|^2+Csum_(n<=N)n|a_n|^2`

` <=(T+CN)sum_(n<=N)|a_n|^2`,                     (15)

其中 `C` 是 absolute constant。频率 `lambda_n=logn` 的 local spacing
`delta_n asymp1/n` 正好产生 weighted term `n|a_n|^2`。

文档 134 的 elementary coefficient estimate又给

`sum|a_n|^2<=delta^(-3)`, `0<delta<=1`.           (16)

因此任意 `T` 上都保留有

`E_2(T)<=Cdelta^(-3)(T+N)`,                       (17)

而非只能在 `T>>N` 后使用 `E_2(T)<<delta^(-3)T`。

另一方面，vertical Stirling与一次分部给

`Re A_infinity(1/2+delta+it)>=c_0logT`,            (18)

`|I_Y(1/2+delta+it)|<=C(1+Y^(1/2-delta))/T`.      (19)

所以只要式 (19)与 prime truncation tail小于 `(c_0/2)logT`，引理 AAI可取
`beta asymp logT`。

## 5. Abel defect 的无条件平方根 localization

### 定理 AAK（square-root Cauchy-core localization）

固定 `0<alpha<1/3`，并令

`delta_Y=(logY)^(-alpha)`,                         (20)

`T_0(Y)=Y^(1/2)delta_Y^(-3/2)logY`.               (21)

则 zeta Abel candidates无条件满足

`int_(|t|>=T_0(Y))[-Re F_Y(delta_Y+it)]_+`

`                         /(1+t^2)dt=o(1)`.       (22)

同一结论适用于固定 degree、tempered coefficients
`|b(n)|<=dLambda(n)`，只改变依赖 `d` 的常数。

#### 证明

写 `L=logY`，固定 `A>2`，取 `T_1=YL^6`、

`N=ceil[AYL]=O(YL)`.                               (23)

把 tail integral作代换 `n=Yu`，其上界为
`O_A(Y^(1/2-delta-A)polylogY)`，故在全部
`T_0<=|t|<=2T_1` 上远小于 `logT`。又由式 (19)，在 `T>=T_0` 时

`Y^(1/2-delta_Y)/T`

` <=delta_Y^(3/2)Y^(-delta_Y)/L=o(1)`,            (24)

因为 `Y^(-delta_Y)=exp[-L^(1-alpha)]`。故式 (18)--(19)给 uniform barrier
`beta(T)>=c logT`。

由 Montgomery--Vaughan式 (15)--(17)，正负两个 height shells上都有

`E_2(T)<=Cdelta_Y^(-3)(T+YL)`.                    (25)

引理 AAI与 Cauchy weight给该 dyadic shell的贡献

` <=Cdelta_Y^(-3)[1/(TlogT)+YL/(T^2logT)]`.       (26)

从 `T_0` 到 `T_1` 对 dyadic `T` 求和，至多

`Cdelta_Y^(-3)/(T_0logT_0)`

` +Cdelta_Y^(-3)YL/(T_0^2logT_0)`

` =o(1)+O(L^(-2))`.                               (27)

在 `|t|>=T_1`，由于 `alpha<1/3`，`T_1=YL^6` 最终支配文档 136
推论 YM的 `delta`-dependent起始条件；该推论给

`O(delta_Y^(-3)/(T_1logT_1))=o(1)`.              (28)

合并式 (27)--(28)即得式 (22)。tempered degree `d` 的 coefficient square
mass至多增加 `d^2`，其余步骤不变。`□`

旧 localization只使用式 (14)在 `T>>NlogN` 后的简化，故把未知 core留在
`|t|<Y polylogY`。定理 AAK利用 weighted Hilbert off-diagonal账本，将其缩到
式 (21)。

## 6. 精确剩余判据

### 推论 AAL（square-root-core RH criterion）

沿式 (20)--(21)，若

`sup_Y int_(|t|<T_0(Y))[-Re F_Y(delta_Y+it)]_+`

`                              /(1+t^2)dt<infinity`, (29)

则 RH成立。若 RH不成立，则式 (29)的积分沿充分共尾的 `Y` 必趋于无穷。

#### 证明

定理 AAK把 exterior contribution压到零。式 (29)因而给 full defect一致有界，
应用定理 ZT。反向结论由定理 ZU与 exterior `o(1)` 相减。`□`

这把经典 RH 的无循环存在性问题进一步定位为长度
`sqrt(Y)delta^(-3/2)logY` 的 arithmetic core。现有 coefficient-only
Hilbert estimate在式 (26)中含
`YL/T^2`；要让它消失仍必需 `T` 超过约 `sqrtY`。因此继续缩小 core需要使用
von Mangoldt coefficients的真实相关性、one-sided cancellation或新的 positive
background，而不能只重复同一 off-diagonal absolute majorant。

## 7. Finite block audit

实现 `stationary_cauchy_block_negative_trace_audit`：

1. 接受任意 symmetric positive block edges；
2. 对每个正负 cell使用 exact Cauchy mass；
3. 用 `sum|c_jlambda_j|` 给 blockwise midpoint error；
4. 用 coefficient absolute mass控制最终 two-sided tail；
5. 返回每块 sampled negative trace、最深 symbol与 certified formula ledger。

实现 `abel_square_root_core_schedule` 对给定 `(Y,alpha)` 返回式 (20)--(28)的
`delta,T_0,T_1,N`，以及 intermediate diagonal/off-diagonal、continuum barrier
与 dyadic high-tail proxies；它用于识别日程中的主导项，不把省略的解析常数伪装成
interval certificate。

取 `alpha=.2,A=3` 的 schedule ledger为：

| `Y` | `delta` | `T_0/Y` | diagonal proxy | off-diagonal proxy | barrier proxy |
|---:|---:|---:|---:|---:|---:|
| `1e2` | .7368 | .728 | `6.1e-3` | .116 | `4.3e-3` |
| `1e4` | .6414 | .179 | `2.0e-4` | .0303 | `9.5e-5` |
| `1e8` | .5584 | .00441 | `6.5e-7` | .00814 | `2.3e-7` |
| `1e16` | .4861 | `1.09e-6` | `2.1e-11` | .00216 | `1.1e-11` |

账本显示当前渐近主项确为 weighted-Hilbert off-diagonal proxy；它趋零但远慢于
其它三项。这精确支持第 8 节把下一输入定位到 one-sided prime correlations。

对文档 149 相同的 shared-symbol参数，以 blocks
`[0,1],[1,2],...,[128,256]` 作诊断：

| `Y` | sampled total | `[0,8]` | `[8,32]` | `[32,256]` |
|---:|---:|---:|---:|---:|
| 2 | .22106 | .22106 | 0 | 0 |
| 5 | .11153 | .11151 | .000018 | 0 |
| 10 | .06251 | .06121 | .000714 | .000590 |
| 30 | .03191 | .02145 | .00670 | .00376 |

负容量总量下降时，部分质量确实向中高 blocks迁移。对应 covered-grid error约为
`.00058,.0028,.0072,.0232`，而 coefficient-mass tail bound仍较粗；所有数字均为
非区间 finite diagnostics，不证明式 (28)或 RH。

## 8. 下一步

平方根 core内的首要对象现在是

`int_(|t|<T_0) (Re P_Y-Re[A_infinity+I_Y])_+dmu`.  (30)

可行的下一推进应利用 prime coefficients而非 generic Dirichlet polynomial：

1. 把式 (29)按 thresholds作 layer cake，研究 large values而非 full variance；
2. 在 `t<<sqrtY` 区域使用 additive prime-pair correlations或 Selberg sieve
   majorants；
3. 将 pole/Gamma barrier保留在每一层，避免再次退化成 full `L2` energy；
4. 寻找能把 `YL` off-diagonal项替换为 `T polylogY` 的 one-sided estimate。

任何把式 (29)证明为 `O(1)` 的结果，经推论 AAL即直接推出 RH。
