# 246. Lipschitz good-cell 收敛定理与 coefficient rationalization gate

日期：2026-09-03

分支：NCE-8 / 路线 B1；接口：one-sided spectral good arcs / finite Brownian
ratio capture

状态：trigonometric-symbol Lipschitz bounds、midpoint-to-cell lower certificate及
finite strict-good energy的网格收敛为 [T]；double-precision zeta lower sums与分辨率
实验为 [E]；transcendental coefficient/lag 的有理区间封装为 [O]。本笔记不更新
PDF，不声称 uniform B1a、RH/GRH 或新的零点比例。

## 1. 本轮推进

笔记 245-D 给出一个抽象 interval enclosure template，但尚未说明如何从 finite
trigonometric symbols系统地产生这些 enclosures，也未证明加密网格能恢复真实
good-set energy。本轮补齐这两个有限分析环节。

主要结果是：

1. `W_p,W_c,d-hat,Q(d-hat)` 都有由 atom moments显式给出的 global Lipschitz
   constants；
2. 一个 midpoint value加 `L h/2` 即给整个 cell的保守 enclosure；
3. 只累计整格满足 ratio和 `|Q|` 下界的 cells，得到真正的一侧 lower sum；
4. 对任意固定 finite symbol，当 `h->0` 时这些 lower sums收敛到 strict-good set上的
   全部 energy，不会因证书机制本身永久丢失正质量。

在当前 double-precision zeta模型中，格宽从 `0.01` 减到 `0.005` 后，宽
`[1/4,4]` band的保守 lower/exact diagonal由 `0.0988` 增到 `0.1999`
（scale 8），由 `0.0252` 增到 `0.1645`（scale 16）。因此粗格的下降主要是
enclosure resolution损失；但由于 coefficients和 lags尚非 directed intervals，
这些仍只标 `[E]`。

## 2. 显式 Lipschitz constants

沿用笔记 244--245。令

\[
 W_p(\xi)=\int(1-\cos(\xi x))da(x),
 \qquad
 W_c(\xi)=\int(1-\cos(\xi x))db(x),
\tag{1}
\]

其中 `a,b` 为 finite nonnegative even atomic measures。令完整 signed symbol为 `d`，
并置

\[
 S=\|d\|_{TV},
 \quad
 L_p=\int|x|da(x),
 \quad
 L_c=\int|x|db(x),
 \quad
 L_d=\int|x|d|d|(x).
\tag{2}
\]

对笔记 245-(4) 的 quartic `Q=Q_(M,l)`，定义

\[
 Q'_*=4S^3+3|M-2\ell|S^2
 +2|M-\ell|^2S+|M||M-\ell|^2,
\tag{3}
\]

以及

\[
 L_Q=Q'_*L_d.
\tag{4}
\]

### 引理 246-A（global symbol Lipschitz ledger）[T]

对任意实 `xi,eta`，

\[
\begin{aligned}
 |W_p(\xi)-W_p(\eta)|&\le L_p|\xi-\eta|,\\
 |W_c(\xi)-W_c(\eta)|&\le L_c|\xi-\eta|,\\
 |\widehat d(\xi)-\widehat d(\eta)|&\le L_d|\xi-\eta|,\\
 |Q(\widehat d(\xi))-Q(\widehat d(\eta))|
 &\le L_Q|\xi-\eta|.
\end{aligned}
\tag{5}
\]

#### 证明

由 `|cos u-cos v|<=|u-v|`，前两式直接对 atoms求和。类似地，
`|exp(-iux)-exp(-ivx)|<=|x||u-v|` 给第三式。又因
`|d-hat|<=S`，在 disk `|z|<=S` 上由式 (3)逐项三角估计得到
`|Q'(z)|<=Q'_*`。沿连接两个 symbol values的线段积分 `Q'`，结合第三式即得
第四式。`square`

这些 constants完全由 finite atom ledger计算，不依赖采样点之间的启发式平滑。

## 3. Midpoint cell certificate

固定 positive-frequency cell

\[
 I=[t-r,t+r],\qquad t-r>0.
\tag{6}
\]

从 midpoint values定义

\[
\begin{aligned}
 p^-&=\max\{0,W_p(t)-L_pr\},&
 p^+&=W_p(t)+L_pr,\\
 c^-&=\max\{0,W_c(t)-L_cr\},&
 c^+&=W_c(t)+L_cr,\\
 q^-&=\max\{0,|Q(\widehat d(t))|-L_Qr\}.
\end{aligned}
\tag{7}
\]

实际机器实现还须在每个误差半径中加入 directed-rounding与 coefficient enclosure
误差；式 (7)先陈述 exact-real arithmetic版本。

### 定理 246-B（verified midpoint cell lower bound）[T]

固定 `0<m<=M_0<infinity`。若

\[
 p^->0,qquad c^->0,qquad q^->0,
\tag{8}
\]

且

\[
 p^-\ge m c^+,
 \qquad
 p^+\le M_0c^-,
\tag{9}
\]

则整个 `I` 都落在 ratio good set

\[
 m\le W_p/W_c\le M_0.
\tag{10}
\]

此外，对 real two-sided response及 common scalar `gamma`，把 reflected cell `-I`
一起计入后有

\[
\boxed{
 \int_{I\cup(-I)}(W_p^2+W_c^2)d\omega_R
 \ge
 \frac{|\gamma|^2(q^-)^2}{\pi(t+r)^2}
 \bigl((p^-)^2+(c^-)^2\bigr)|I|.}
\tag{11}
\]

#### 证明

引理 246-A给 `W_p in [p^-,p^+]`、`W_c in [c^-,c^+]` 与
`|Q(d-hat)|>=q^-` 于整个 `I`。式 (8)--(9)给式 (10)。又对 `xi in I`，
`xi^(-2)>=(t+r)^(-2)`。代入笔记 245-(6)并在 `I` 积分；two-sided real
evenness使 `-I` 贡献相同，得到式 (11)。`square`

不同 verified cells两两不交时，式 (11)可直接求和。除去任何未验证 cell只会删除
非负能量，不需要给它们 upper bound。

## 4. 有限证书方法的收敛完备性

固定 `0<a<T<infinity`。定义 strict-good open set

\[
H=\{\xi\in[a,T]:
 mW_c(\xi)<W_p(\xi)<M_0W_c(\xi),
 \ W_pW_c|Q(\widehat d)|>0\}.
\tag{12}
\]

并令 closed-good set

\[
 G=\{\xi\in[a,T]:
 mW_c(\xi)\le W_p(\xi)\le M_0W_c(\xi),
 \ W_pW_c|Q(\widehat d)|>0\}.
\tag{12a}
\]

取一列 uniform partitions，mesh `h_n->0`。在每个 cell上用式 (7)--(9)判定，
并以式 (11)的 pointwise lower density构造和 `L_n`。

### 定理 246-C（strict/closed good-energy squeeze）[T]

在 exact-real arithmetic下，

\[
\boxed{
 \int_{H\cup(-H)}(W_p^2+W_c^2)d\omega_R
 \le\liminf_{n\to\infty}L_n
 \le\limsup_{n\to\infty}L_n
 \le\int_{G\cup(-G)}(W_p^2+W_c^2)d\omega_R.}
\tag{13}
\]

若 `G minus H` 的 energy为零，则 `L_n` 收敛且极限等于两端共同值。

特别地，只要 strict-good set携带正能量，就存在某个 finite mesh产生严格正的
machine-checkable lower sum；证书 schema本身不会永远返回零。

#### 证明

对任意 `xi in H`，式 (12)的所有不等式都有严格 margin。由连续性，存在包含
`xi` 的邻域，其闭包仍满足式 (8)--(9)。当 `h_n` 足够小时，包含 `xi` 的 grid
cell因引理 246-A的 enclosure半径趋零而被验证。相反，任何 verified cell都包含于
式 (10)的 good set，且 `q^-,p^-,c^->0`。

在 `H` 每一点，cell lower density随 `h_n->0` 收敛到 actual continuous density；
Fatou引理给式 (13)的第一个不等式。每个 verified cell都包含于 `G`，且其 lower
density逐点不超过 actual density，给最后一个不等式。中间不等式是定义。若
`G minus H` 为 energy-null，左右端相等，夹逼即给收敛。evenness给负半轴部分。
`square`

若 partitions不嵌套，`L_n` 不必单调，但极限仍成立。若需要单调 certificate，可用
dyadic nested partitions并保留父格已认证的 lower contribution与子格新下界中的
较大者。

## 5. Double-precision finite evidence [E]

`scripts/vaughan_spectral_ratio_capture_audit.py` 已实现引理 246-A与定理 246-B的
浮点先导版。每个误差半径另加入 `1e-12` safety padding，但这不是 directed interval
arithmetic，因此只记 [E]。

固定 frequency cutoff `256`、continuum cells `4` 和 band `[1/4,4]`：

| scale, cutoff | mesh `h` | raw band / exact `D` | Lipschitz lower / exact `D` | verified width |
|---:|---:|---:|---:|---:|
| 8, 10 | 0.010 | 0.5849 | 0.0988 | 41.07 |
| 8, 10 | 0.005 | 0.5849 | 0.1999 | 63.93 |
| 16, 15 | 0.010 | 0.7024 | 0.0252 | 16.13 |
| 16, 15 | 0.005 | 0.7026 | 0.1645 | 50.33 |

两次 refinement中 raw band mass保持稳定，而 conservative lower明显增长；这与
定理 246-C预言的 resolution recovery一致。数据尚不能证明 scale-uniform lower
bound：只比较两个很小的 finite models，且 coefficients、lags、Brownian denominator
都仍为浮点数。

若把表中的 lower values暂时代入笔记 244-D，宽 band的 pointwise overlap constant为

\[
 \min\left\{\frac{1/4}{1+1/16},
 \frac4{17}\right\}=\frac4{17}.
\tag{14}
\]

所以对应 finite implication会给 `delta_lower=(4/17)kappa_lower`；但在完成有理区间
审计前，不将这些数值标为 `[T]`。

## 6. Rationalization gate

要把浮点 lower sum升级为真正 finite certificate，必须同时 enclosure：

1. prime weights `Lambda(n)n^(-sigma)exp(-n/Y)`；
2. continuum cell masses及其 quadrature remainder；
3. lags `log n` 与 continuum midpoints；
4. `M,ell,gamma` 和 quartic `Q` 的 coefficients；
5. midpoint trigonometric values；
6. exact Brownian denominator `D=P+C` 的上界。

只给 numerator下界而仍用浮点 `D` 不构成 ratio certificate。可接受实现是把每个
transcendental input转换成 rational interval，使用 outward-rounded sine/cosine与
polynomial interval evaluation，并最终输出

\[
 \boxed{N_{\rm lower}/D_{\rm upper}\ge\kappa_{\rm cert}>0.}
\tag{15}
\]

continuum quadrature模型与原完整 Archimedean current之间的 remainder必须另列，
不能由 finite interval certificate自动消失。

## 7. 下一最小引理 B1e [O]

先对单一 finite instance

\[
 (\mathrm{scale},N,\mathrm{cells})=(8,10,4),
 \qquad h=0.005,
\tag{16}
\]

完成式 (15) 的独立 rational/interval certificate，目标只要求

\[
 \kappa_{\rm cert}>0.10
\tag{17}
\]

for band `[1/4,4]`。该阈值低于当前浮点 lower `0.1999`，给 coefficient与 rounding
误差留下明确余量。

完成单实例后再推进：

1. `scale=16,N=15,cells=4`；
2. continuum mesh refinement；
3. 增长 scale下 `kappa_cert` 的稳定性；
4. 从 finite certificates抽取 uniform analytic prime/continuum estimate。

晋级条件：生成可由独立脚本重新验证的 rational endpoints、cell list、numerator
lower与 denominator upper。止损条件：若 outward rounding使 lower降至零，先加密
mesh；若任意 mesh都因 coefficient/quadrature uncertainty失败，则记录为 finite
certificate obstruction，而不是保留浮点主张。

## 8. 公理、删除审计与循环性

本轮 [T] 使用 finite atomic symbols、显式 first absolute moments、quartic derivative
bound、exact denominator和非负 spectral density。

删除审计：

- 删除 first-moment bounds，midpoint不能控制整格；
- 删除 strict ratio margins，边界 cells不保证有限步被验证；
- 删除 `|Q|>0` margin，energy lower可退化为零；
- 删除 exact或 upper-certified denominator，lower ratio没有证明意义；
- 删除 two-sided real symmetry，式 (11)的 reflected doubling失效；
- 把 `h=0.005` finite结果升级为 uniform scale theorem，违反 finite-to-bulk纪律。

非同义反复审计：246-A--C证明一个有限证书机制确实收敛，并非把目标 inequality
直接作为公理。式 (15)--(17)尚未完成，明确标为 [O]。

循环性审计：全部 [T] 只用 elementary harmonic analysis与 interval enclosure；
不调用 RH/GRH、Weil positivity、谱酉性、PNT误差、Mertens平方根界或 bounded
negative index。

## 9. 模型范围与论文接口

- **Riemann zeta**：B1e 是当前下一任务；单实例证书只验证有限配置，不推出 RH。
- **Dirichlet/automorphic L**：complex phases需要分别 enclosure real/imaginary parts，
  且 Note 244 的 sign theorem一般缺失。
- **Dedekind zeta**：nonnegative ideal coefficients允许同型 Lipschitz ledger；多
  Archimedean channels需使用 ratio cone而非 scalar interval。
- **函数域**：lags位于 degree lattice，rationalization更容易，可作为证书实现基准。
- **显式公式型 Weil 配置**：finite certified lower直接进入 Brownian physical Gram；
  不建立上同调极化或 Hard Lefschetz。
- **论文归属**：246-A--C 与 rationalization protocol归入 Vaughan--Brownian response
  论文的 finite-certification section。

本轮证明 B1d 的有限好弧 schema在解析上是完备的，并用分辨率实验排除了“保守
enclosure必然返回零”的担忧。唯一紧邻缺口现在是可独立复核的 transcendental
interval arithmetic；这句话只针对式 (16) 的单一 finite instance，scale-uniform
B1a 仍需要新的算术估计。
