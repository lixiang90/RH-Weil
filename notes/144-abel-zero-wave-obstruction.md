# Abel zero-wave 的显式负井与可数右最包障碍

文档 143 把 passive RH充分条件压成 finite stationary symbols 的 Cauchy
negative mass趋零；文档 145进一步表明仅需其一致有界。本节研究反方向：
假如 completed divisor 有离中心线 zero，Abel regularization会留下怎样的负质量？

结论分两层：

1. 单个 residue wave在相邻的一个 carrier half-period上有完全显式的负井；
2. 任意多项式计数的可数同阶 rightmost packet，即使相位随 `logY` 改变，
   也不能把全部负质量相消。

这还不是 RH 的证明。对 zeta，尚需从 primes无条件处理最右 real part只是
未达到的 supremum，或虽达到但有 zeros从左侧无限逼近该线、使 contour
remainder与主 packet同阶的情形。

## 1. Abel--Mellin residue 的符号

令

`D(s)=-zeta'(s)/zeta(s)`,

`S_Y(s)=sum_(n>=2)Lambda(n)n^(-s)e^(-n/Y)`.       (1)

由 `e^(-x)` 的 Mellin inversion，在绝对收敛直线上

`S_Y(s)=(1/(2pi i))int_((c))Gamma(w)Y^wD(s+w)dw`. (2)

把 contour左移但仍保留 `Re w>0`。`D` 在 `s+w=1` 的 residue为 `+1`，
在一个 `m_rho` 重 zeta zero处 residue为 `-m_rho`。所以越过的 residues给

`S_Y(s)=Gamma(1-s)Y^(1-s)`

` -sum_rho m_rho Gamma(rho-s)Y^(rho-s)+R_Y(s)`.  (3)

而文档 132 的 continuum为

`I_Y(s)=int_1^infinity x^(-s)e^(-x/Y)dx`

`       =Gamma(1-s)Y^(1-s)-int_0^1x^(-s)e^(-x/Y)dx`. (4)

因此 pole main term精确消去，而每个 zero在 `I_Y-S_Y` 中带 **正号**：

`+m_rho Gamma(rho-s)Y^(rho-s)`.                  (5)

若 `rho=1/2+a+i gamma`, `s=1/2+delta+it`，写

`b=a-delta>0`, `L=logY`，则式 (5)为

`m_rho Y^b Gamma(b+i(gamma-t))e^(i(gamma-t)L)`.   (6)

在 `t=gamma` 它为正；但高度移动 `O(1/L)` 后，carrier phase旋转到负半周。

式 (2)--(5) 是标准 Mellin contour bookkeeping；实际使用时必须另行给出 contour
remainder以及所有同阶 residues 的统一界，不能把单个 residue从完整显式公式中
无条件孤立出来。

## 2. 单波的显式 half-period certificate

对 `b>0` 定义

`A(b)=int_0^infinity e^(-x)x^(b-1)|logx|dx`.       (7)

Gamma积分的微分公式给

`Gamma'(b+iv)=int_0^infinity e^(-x)x^(b+iv-1)logx dx`,

故

`|Gamma'(b+iv)|<=A(b)`.                           (8)

该外部标准公式可见 NIST DLMF 5.9.19；这里从积分式直接得到所需不等式。

令 `R_Y(t)` 是除一个 `m` 重 zero wave外的全部 remainder，并假设在下述小区间

`|Re R_Y(t)|<=r_Y Y^b`.                            (9)

### 定理 ZN（explicit Abel carrier half-period obstruction）

取

`u_0=2pi/3`, `u_1=4pi/3`,

`I_Y=[gamma+u_0/L,gamma+u_1/L]`.                 (10)

令

`q_Y=mGamma(b)/2-mA(b)u_1/L-r_Y`.                 (11)

若 `q_Y>0`，则对

`G_Y(t)=mGamma(b+i(gamma-t))Y^(b+i(gamma-t))+R_Y(t)` (12)

有

`int_(I_Y)[-Re G_Y(t)]_+/(1+t^2)dt`

` >=Y^b q_Y (u_1-u_0)`

`   /{L[1+(|gamma|+u_1/L)^2]}`.                  (13)

#### 证明

写 `t=gamma+u/L`。式 (12) 的主项除以 `Y^b` 后是

`mGamma(b-iu/L)e^(-iu)`.                          (14)

在 `[u_0,u_1]` 上 `cosu<=-1/2`。由式 (8)和 mean-value integral，

`|Gamma(b-iu/L)-Gamma(b)|<=A(b)u/L`.              (15)

所以式 (9)、(14)--(15)给 `Re G_Y(t)<=-q_YY^b`。区间长度为
`(u_1-u_0)/L`，且其中

`1+t^2<=1+(|gamma|+u_1/L)^2`，                    (16)

积分即得式 (13)。`□`

实现 `single_abel_zero_wave_half_period_certificate` 逐项返回式 (7)--(13)；
它是公式审计，不是 interval arithmetic。

例如取 `a=.2, delta=.02, gamma=14, m=1, r_Y=.01`，得到：

| `logY` | Gamma variation bound | normalized negative margin | 式 (13) 的 `J_Y` lower bound |
|---:|---:|---:|---:|
| 50 | `2.5342` | `.02168` | `.03692` |
| 100 | `1.2671` | `1.2888` | `8.943e3` |
| 200 | `.63356` | `1.9224` | `4.392e11` |

这里快速增长来自 `Y^(.18)`；数值只核对 bound的尺度与实现，不主张存在这样
的 zeta zero，也不作为 RH反证。

## 3. 一个 exposed off-line zero 已足够阻止 defect 消失

### 定理 ZO（residue-dominant off-line zero forces divergent defect）

设 `a>0`，`delta_Y->0`。若存在 `rho=1/2+a+i gamma` 及固定 `m>=1`，使
Abel candidate在式 (10) 上具有式 (12)，并且

`r_Y=o(1)`,                                       (17)

则其 Cauchy defect满足

`J_Y >=c_(a,gamma,m)Y^(a-delta_Y)/logY`           (18)

对充分大 `Y` 成立。特别地 `J_Y->infinity`，不可能满足文档 136/143 的
`J_Y->0` 判据。

#### 证明

因为 `delta_Y->0`，有 `b->a`，`Gamma(b)->Gamma(a)>0`，`A(b)` 在 `a`
附近有界。故式 (11)最终至少为 `mGamma(a)/4`。式 (13)给式 (18)。又因
`b>a/2` 最终成立，右侧至少按 `Y^(a/2)/logY` 增长。`□`

所以一个相对于其它 terms 局部 exposed的离线 zero不会只留下“很窄、因而
Cauchy weight看不见”的井；其宽度是 `1/logY`，但深度是 `Y^(a-delta)`，
乘积仍发散。

## 4. 有限个同阶 waves 也不能永久相消

单波 dominance不是必须的。设 distinct ordinates
`gamma_1,...,gamma_m` 都位于同一 rightmost line `Re rho=1/2+a`，并令

`A_(delta,zeta)(t)=sum_(j=1)^m m_j zeta_j`

`                    *Gamma(a-delta+i(gamma_j-t))`, (19)

其中 `|zeta_j|=1`。实际 Abel phases是 `zeta_j=e^(i gamma_jlogY)`。

### 引理 ZP1（finite Gamma translates are uniformly noncancelling）

对任意有内点的 compact interval `I` 与 `0<=delta<=a/2`，存在 `c_I>0`，
使

`int_I |A_(delta,zeta)(t)|dt>=c_I`                (20)

对全部 phase vectors `zeta in T^m` 成立。

#### 证明

先证固定 `delta` 下 functions
`Gamma(a-delta+i(gamma_j-t))` 线性无关。若一组线性组合在 `I` 上为零，
analytic continuation使它在实轴上为零。Euler积分把该组合写成函数

`e^((a-delta)v-e^v)sum_j c_je^(i gamma_jv)`       (21)

的 Fourier transform。Fourier uniqueness及有限 exponential polynomial的
线性无关性给全部 `c_j=0`。因此式 (19)不可能恒零。参数集
`[0,a/2]timesT^m` compact，式 (20)左侧连续且处处正，故有正的统一最小值。
`□`

### 引理 ZP2（uniform rapid-carrier averaging）

若 `K` 是 `C(I)` 中 compact的一族 functions，且
`inf_(A in K)int_I|A(t)|dt>0`，则

`int_I[-Re(e^(-iLt)A(t))]_+dt`

` ->(1/pi)int_I|A(t)|dt`                          (22)

当 `L->infinity`，并且收敛对 `A in K` 一致。

#### 证明

先对 constant `A` 在完整 carrier periods上积分；`[-cos]_+` 的周期平均为
`1/pi`。把 `I` 分成短 cells，uniform continuity使每个 `A in K` 在 cell内
接近常数；两端不完整 periods的总误差为 `O(1/L)`。先固定 cell mesh再令
`L->infinity`，最后用 `K` 的共同 modulus of continuity令 mesh趋细。`□`

### 定理 ZP（finite rightmost residue packet obstruction）

假设在一个固定 compact interval `I` 上

`F_Y(delta_Y+it)`

` =Y^(a-delta_Y)e^(-itlogY)A_(delta_Y,zeta(Y))(t)+R_Y(t)`, (23)

其中式 (19)只有有限个非零 terms，且

`int_I|R_Y(t)|dt=o(Y^(a-delta_Y))`.                (24)

则存在 `c>0` 使

`int_I[-Re F_Y(delta_Y+it)]_+/(1+t^2)dt`

` >=cY^(a-delta_Y)`                               (25)

对充分大 `Y` 成立。因此 `J_Y` 发散。

#### 证明

式 (19)随参数形成 `C(I)` 中 compact族；引理 ZP1给 uniform positive `L1`
norm，引理 ZP2给 leading term的 uniform negative-part lower bound。在 compact
`I` 上 Cauchy weight有正下界。map `x->[-x]_+` 是 1-Lipschitz，故式 (24)
只能造成 `o(Y^(a-delta_Y))` 损失，得到式 (25)。`□`

## 5. 可数 rightmost packet 的紧性

有限性可以去掉。先记录一个 exact full-line Gram identity。令

`g_gamma(t)=Gamma(b+i(gamma-t))`, `b>0`。          (26)

### 引理 ZQ1（exact Gamma-translate Gram）

对任意 real `gamma,eta`，

`<g_gamma,g_eta>_(L2(R))`

` =2pi 2^(-2b-i(gamma-eta))Gamma(2b+i(gamma-eta))`. (27)

特别地，任意 distinct finite ordinates的 Gram严格正定。

#### 证明

Euler积分在 `x=e^v` 后给

`g_gamma(t)=int_R e^(bv-e^v)e^(i gamma v)e^(-itv)dv`. (28)

Plancherel把内积化为

`2pi int_R e^(2bv-2e^v)e^(i(gamma-eta)v)dv`，

再令 `x=e^v` 即得式 (27)。严格正定来自 distinct exponentials
`e^(i gamma v)` 的线性无关。`□`

现在设 `Gamma_*` 是可数 distinct ordinates，multiplicities `m_gamma>=1`，且

`sum_(|gamma|<=T)m_gamma=O((1+T)^A)`              (29)

对某个 finite `A` 成立。对 phases `|zeta_gamma|=1` 定义

`A_(b,zeta)(t)=sum_(gamma in Gamma_*)m_gamma zeta_gamma`

`                                      *Gamma(b+i(gamma-t))`. (30)

### 定理 ZQ（countable Gamma packet is uniformly noncancelling）

给定 `0<b_0<=b<=b_1` 与有内点 compact interval `I`，若 `Gamma_*` 非空并
满足式 (29)，则式 (30)在 `C(I)` 中 absolute/uniform convergent，而且

`inf_(b,zeta)int_I|A_(b,zeta)(t)|dt>0`.           (31)

#### 证明

vertical Stirling estimate在 bounded `b` 上一致给

`|Gamma(b+ix)|<=C(1+|x|)^(b_1-1/2)e^(-pi|x|/2)`. (32)

结合式 (29)，式 (30)及其局部 `t` derivatives都有 uniform exponential
tails。因此全部 phase vectors的像是 `C(I)` 中 compact族；更形式地，product
torus由 Tychonoff compactness，uniform tail使式 (30)定义连续映射。

只需证明像中不含 zero function。若某个式 (30)在 `I` 上恒零，uniform analytic
convergence与 identity theorem使其在整个 real axis恒零。令 tempered discrete
measure

`mu=sum_gamma m_gamma zeta_gamma delta_gamma`.     (33)

式 (29)保证 `mu` tempered。式 (28)说明 (30)是
`f_b(v) hat mu(v)` 的 Fourier transform，其中
`f_b(v)=e^(bv-e^v)` 是 nowhere-zero Schwartz function。故
`f_b hat mu=0` as a distribution。对任意 compactly supported smooth test
`phi`，`phi/f_b`仍 smooth且 compactly supported，所以 `hat mu=0`，进而
`mu=0`，与每个 coefficient的 modulus为正矛盾。于是 compact parameter image
上的 continuous positive functional `A->int_I|A|` 有严格正 minimum，得到
式 (31)。`□`

### 定理 ZR（countable rightmost-line obstruction）

把定理 ZP 的 finite sum换成满足式 (29)的完整 rightmost packet，并假设在固定
`I` 上

`F_Y(delta_Y+it)`

` =Y^(a-delta_Y)e^(-itlogY)A_(a-delta_Y,zeta(Y))(t)+R_Y(t)`, (34)

其中 `int_I|R_Y|dt=o(Y^(a-delta_Y))`。则仍存在 `c>0` 使

`J_Y>=cY^(a-delta_Y)`                              (35)

对充分大 `Y` 成立。

#### 证明

定理 ZQ给 amplitude family的 `C(I)` compactness与 uniform positive `L1`
norm；引理 ZP2对该 compact family作 uniform carrier averaging。Cauchy weight
在 `I` 上下有界，remainder由 negative-part map的 1-Lipschitz性吸收。`□`

对 zeta，标准 zero-counting甚至是 `O(TlogT)`，所以若最右 real part确由一条
zero line达到，则该线自身的有限或无限 multiplicity packet都满足式 (29)。
实现 `gamma_translate_l2_gram` 返回式 (27)的 finite Gram。

## 6. 不需要 rightmost zero 的定性 no-escape

定理 ZO--ZP给显式增长率，但带 residue-dominance/finite-packet假设。即使这些
假设不成立，文档 136 的 normal-family theorem仍给一个无条件的定性反命题。

### 定理 ZS（off-line divisor forces a uniform cofinal defect gap）

对 zeta 的 Abel candidates，若 RH不成立，则存在
`epsilon_0>0`, `Y_0>0`, `delta_0>0`，使

`J_(Y,delta)>=epsilon_0`                           (36)

对全部 `Y>=Y_0` 与 `0<delta<=delta_0` 成立。

沿文档 143 任一 total discretization error `E_Y->0` 的 fully finite schedule，
相应 sampled stationary minimum `v_Y^sample` 最终满足

`v_Y^sample<=-epsilon_0/(2pi)`.                   (37)

#### 证明

若式 (36)不成立，则对每个 integer `n` 可选
`Y_n>=n`, `0<delta_n<=1/n` 且 `J_(Y_n,delta_n)<1/n`。这些 candidates的
Poisson admissibility与 Euler open-germ convergence由文档 136 无条件成立；
定理 YL遂推出 RH，矛盾。

另一方面，定理 ZJ的 exact stationary minimum是 `-J_(Y,delta)/pi`。定理
ZK/ZL的同一个 Lipschitz、tail与 shared-quadrature ledger实际上给

`|v_Y^sample+J_(Y,delta)/pi|<=E_Y`.                (38)

最终取 `E_Y<=epsilon_0/(2pi)`，由式 (36)得到式 (37)。`□`

定理 ZS说明 supremum未达到或 near-rightmost remainder同阶只能破坏
ZO--ZR的显式增长率，不能让 defect沿任何 cofinal sequence逃到零。文档 145
定理 ZU进一步把这里的 fixed gap加强为共尾发散到 `infinity`。

## 7. 对广义结构定理的含义

文档 131--143 的 sufficient chain现在有一个部分 converse：

`finite rightmost off-line residue packet`

` + Mellin remainder lower order`

` -> moving Abel negative wells with macroscopic Cauchy mass`

` -> stationary capped minimum not tending to zero`.               (39)

这适用于任何 logarithmic Dirichlet series，只要 smoothing kernel的 Mellin
transform在 rightmost residues处非零；`Gamma(rho-s)`应替换为相应 transform。
因此“zero residue变成快速 carrier wave”是一个广义的 orbit/Hodge obstruction，
不依赖 zeta 的特殊局部因子。

对经典 zeta，定理 ZR尚不能无条件应用，因为 RH失败时并不知道：

1. `sup Re rho` 是否由某条 rightmost zero line达到；
2. 若达到，是否存在从左侧无限逼近 rightmost line的 zeros，使完整 contour
   remainder不能在移动 carrier windows上做到式 (34)的 lower-order bound。

这些不是 discretization问题，而是 divisor极值几何与 prime explicit formula的
真正 Tauberian问题。rightmost line内部的 infinite-packet cancellation已由
定理 ZQ排除；下一步应绕开“最右 real part达到且有 horizontal gap”的假设，
从 prime-side finite symbol直接证明 one-sided large-sieve/entropy inequality，
或对全部 near-rightmost layers建立 weighted Gamma-frame lower bound。

这里不能退回只控制二阶矩：文档 137 定理 YN--YO已证明 passive非恒定函数
可以有严格正 variance而 negative part为零。所需估计必须保留 pointwise
one-sided cancellation，或等价地保留完整 capped Toeplitz cone。
