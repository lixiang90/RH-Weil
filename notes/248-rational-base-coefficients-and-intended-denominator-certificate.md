# 248. Rational base coefficients 与 intended Brownian 分母证书

日期：2026-09-03

分支：NCE-8 / 路线 B1；接口：B1f base arithmetic / finite one-sided spectral
certificate

状态：rational exponential/square-root enclosure、continuum composite-Simpson
interval、quartic coefficient ledger、production floating-response forward error及固定
`(Y,N,J)=(8,10,4)` intended Brownian denominator upper 为 [T]；当前浮点 good-cell
numerator margin为 [E]；directed trigonometric numerator与 scale-uniform B1a 为 [O]。
本笔记不更新 PDF，不声称 RH/GRH、新的零点比例或 asymptotic overlap。

## 1. 结论

笔记 247 对 binary64 surrogate response证明 exact rational Brownian diagonal upper

\[
 \widetilde D_p\le0.00055130411625587258,
 \qquad
 \widetilde D_c\le0.00015289136767059444.
\tag{1}
\]

本轮把 intended transcendental base coefficients与 production floating expansion
之间的全部误差传到 response TV norm，随后应用 247-D。最终得到：

### 定理 248-A（fixed intended denominator certificate）[T]

对参数

\[
 \sigma=\frac35,\quad Y=8,\quad N=10,\quad
 [\lambda_0,\lambda_4]=\left[\frac3{100},2\right],\quad J=4,
\tag{2}
\]

以及笔记 245--247 的 degree-two centered prime/continuum responses，有

\[
\boxed{
 D=P+C\le
 0.000735925241553713216150037691.}
\tag{3}
\]

式 (3)是单一 finite model的严格上界，不是随 `Y,N,J` 一致的估计。

证明由第 2--6 节给出；所有最终十进制上界都由 exact rational向上舍入。

## 2. Prime coefficients 的 rational enclosure

对 `n=p^k<=10`，prime atom weight为

\[
 w_n=(\log p)n^{-3/5}e^{-n/8}.
\tag{4}
\]

笔记 247-B 已用正项 `atanh` 级数给 `log p,log n` 有理 intervals。还需 enclosure
exponential。对 rational `x>=0`，置

\[
 E_m(x)=\sum_{j=0}^m\frac{x^j}{j!}.
\]

当 `x<m+2` 时，正项尾满足

\[
 0\le e^x-E_m(x)
 \le
 \frac{x^{m+1}}{(m+1)!}
 \frac1{1-x/(m+2)}.
\tag{5}
\]

对 `x<0` 使用 `e^x=1/e^{-x}` 并反转正 interval；对输入 interval利用 exponential
单调性只评估两个 endpoints。

### 引理 248-B（rational exponential enclosure）[T]

式 (5)产生 `e^I` 的 rational interval enclosure。当前脚本取 `m=24`；对式 (4)
的全部七个 prime powers

\[
 n\in\{2,3,4,5,7,8,9\},
\]

把 exact interval与当前 binary64 surrogate weight比较并求和，得到

\[
 \delta_p
 :=\|d_p-\widetilde d_p\|_{TV}
 \le0.000000000000000210817118608703.
\tag{6}
\]

#### 证明

式 (5)中第一个遗漏项之后，相邻项比至多 `x/(m+2)`，故由几何级数得到 tail
upper。区间乘法应用于式 (4)。two-sided atom的两个 half coefficients误差之和恰为
full weight误差，故七项求和给式 (6)。`square`

## 3. Continuum cell masses

原 incomplete-gamma写法可直接还原为 elementary integral：

\[
 C[a,b]=\int_a^b f(x)dx,
 \qquad
 f(x)=\exp\left(\frac{2x}{5}-\frac{e^x}{8}\right).
\tag{7}
\]

令 `g=log f`、`u=e^x/8`。则

\[
 g'=\frac25-u,\qquad g^{(k)}=-u\quad(k\ge2),
\]

且

\[
 \frac{f^{(4)}}f
 =g^{(4)}+4g'g^{(3)}+3(g'')^2+6(g')^2g''+(g')^4.
\tag{8}
\]

在 `[0,2]` 上，式 (5)严格验证 `e^(4/5)<3` 与 `e^2<8`，所以

\[
 f<3,\qquad u<1,\qquad |g'|<1,\qquad
 |f^{(4)}|<3(1+4+3+6+1)=45.
\tag{9}
\]

### 引理 248-C（eight-panel Simpson enclosure）[T]

对每个 rational interval `[a,b] subset [0,2]`，用偶数 `r=8` 个等长
subintervals、步长 `h=(b-a)/r` 作 composite Simpson sum `S_r`，则

\[
 |C[a,b]-S_r|\le\frac{b-a}{180}h^4\sup|f^{(4)}|
 \le\frac{b-a}{4}h^4.
\tag{10}
\]

在每个 Simpson node以引理 248-B enclosure `f`，再加入式 (10) 的 rational
remainder。对 small cell `[0,3/100]` 及四个 uniform cells求和并与 binary64
surrogate masses比较，得到

\[
 \delta_c
 :=\|d_c-\widetilde d_c\|_{TV}
 \le0.000007154150754425142514714306.
\tag{11}
\]

故完整 symbol满足

\[
 \delta_d\le\delta_p+\delta_c
 \le0.000007154150754635959633323008.
\tag{12}
\]

#### 证明

Composite Simpson remainder是标准 repeated-interpolation identity；式 (9)给其
全局 derivative upper。所有 quadrature weights为正，故 node intervals可逐项相加。
continuum two-sided half atoms的 TV误差仍等于 full cell-mass误差，得到式 (11)--(12)。
`square`

这里 enclosure的是 finite quadrature model自身的 cell masses；它不消除该 finite
model与完整 Archimedean current之间另行记录的 quadrature/tail remainder。

## 4. Quartic 与 response scalar

置

\[
 A=\|d_p\|,\quad C=\|d_c\|,\quad B=A+C,\quad M=A-C,
 \quad\kappa=\frac{\sqrt3}{2},\quad\ell=\kappa B.
\tag{13}
\]

`sqrt(3)` 用整数平方根给 enclosure：固定十进制 scale `10^q`，令

\[
 r=\left\lfloor10^q\sqrt3\right\rfloor;
\]

则 `r/10^q<=sqrt3<(r+1)/10^q`，其中 `r` 可由 `isqrt(floor(3*10^(2q)))`
以整数算术取得。

degree-two divided difference为

\[
 Q_{M,\ell}(X)=X^4+(M-2\ell)X^3+(M-\ell)^2X^2
 +M(M-\ell)^2X+M^2(M-\ell)^2.
\tag{14}
\]

response scalar恰为

\[
 s=-\frac{4}{9B^4}
 \left(\frac{\kappa}{\kappa+1/3}\right)^2.
\tag{15}
\]

将式 (12)--(15)代入笔记 247-E 的 convolution-polynomial TV ledger，得到

\[
 \|Q(d)-\widetilde Q(\widetilde d)\|_{TV}
 \le0.006804410613770658228023739385,
\tag{16}
\]

以及

\[
 |s-\widetilde s|
 \le0.000000009729220035856599427796.
\tag{17}
\]

全部 coefficients在此由式 (13)--(15)的 interval polynomial evaluation产生，不把
`Q` 的 desired spectral behavior当作输入。

## 5. Production floating expansion 的 forward error

仅有式 (16)--(17)还不够，因为式 (1) 的 surrogate energy来自 production
binary64 response map，其中每次 coefficient update会在绝对值不超过 `1e-14` 时
剪枝。

脚本先检查运行环境：radix `2`、mantissa `53` bits、normal exponent range
`[-1021,1024)`，且 `FLT_ROUNDS=1`。置

\[
 u=2^{-53},\qquad
 \gamma_n=\frac{nu}{1-nu},\qquad
 \tau_*=\frac{\operatorname{float}(10^{-14})}{1-u}+4\cdot2^{-1074}.
\tag{18}
\]

### 引理 248-D（pruned convolution forward error）[T]

设 finite real-valued maps `a,b` 支撑于 cancellative abelian group，support
sizes为 `m,n`；它们以 imaginary part恒为零的 binary64 complex containers实现，
且其 real coefficients视为 exact dyadic rationals。production convolution使用
round-to-nearest complex multiply/add及上述 pruning rule。则

\[
\boxed{
 \|a*b-\operatorname{flconv}(a,b)\|_1
 \le\gamma_{4\min(m,n)}\|a\|_1\|b\|_1+mn\tau_*.}
\tag{19}
\]

若输入 maps本身分别带 TV errors `epsilon_a,epsilon_b`，右端再加

\[
 \|b\|_1\varepsilon_a+
 \|a\|_1\varepsilon_b+\varepsilon_a\varepsilon_b.
\tag{20}
\]

对应的 scale和有限 map-sum rules为

\[
\begin{aligned}
 E_{\rm scale}&\le |z|E_a+\gamma_4|z|\|a\|_1+m\tau_*,\\
 E_{\rm sum}&\le\sum_jE_j+\gamma_{4r}\sum_j\|a_j\|_1
 +\left(\sum_j|\operatorname{supp}a_j|\right)\tau_*.
\end{aligned}
\tag{21}
\]

#### 证明

固定一个 output group element。因 group cancellative，每个 left support atom至多
配一个 right atom，故其 convolution bucket至多有 `min(m,n)` 项。标准逐运算
round-to-nearest误差 telescoping给该 bucket的 absolute error至多
`gamma_(4 min(m,n))` 乘对应 absolute product sum；factor `4` 保守覆盖 real-embedded
complex container内的 real-embedded multiply/add。对所有 buckets求和时 absolute
product sums恰总计
`||a||_1||b||_1`。每个 pair即使触发 pruning，也至多引入 `tau_*` 的 additive
perturbation；求和给 `mn tau_*`。输入误差展开
`(a+Delta a)*(b+Delta b)` 给式 (20)。scale与 map sum同理。`square`

subnormal项由式 (18)显式覆盖；本实例无 overflow。`scripts/test_b1f_forward_error.py`
另在小 maps上把 exact dyadic convolution与 production output逐系数比较，验证实际
error不超过式 (19)--(21)的 rational bound。

以 production code的相同运算顺序重放 powers、式 (14)、centering、response
convolution与 scalar multiplication；每一步同时传播式 (19)--(21)。脚本还断言重放
map逐 coefficient等于 `degree_two_centered_response_channel_maps` 的实际输出。

support energy使用再次精确居中的 surrogate map，因此另加入 output mass residual。
最终 production-expansion TV errors为

\[
 \varepsilon_{p,{\rm fl}}
 \le0.000000000358943933352368611363,
\]

\[
 \varepsilon_{c,{\rm fl}}
 \le0.000000000348067855921300265406.
\tag{22}
\]

## 6. Response TV 与 Brownian transfer

把式 (6)、(11)、(16)、(17)、(22) 代入笔记 247-(18)，并加入 production
forward errors，得到

\[
 \varepsilon_p
 \le0.000051726627534797886965409388,
\]

\[
 \varepsilon_c
 \le0.000073973952867749963297974559.
\tag{23}
\]

所有 base lags满足 `|lambda|<3`：continuum nodes小于 `2`，且式 (5)验证
`e^3>10`，故 `log n<3` for `n<=10`。response是一个 centered component与 quartic
measure的 convolution，所以支撑于 `(-15,15)`；共同 support length可取

\[
 L=30.
\tag{24}
\]

对两个 channels分别以 `tau=1/100` 应用笔记 247-D：

\[
 D_j\le\frac{101}{100}\widetilde D_j
 +101\cdot30\,\varepsilon_j^2.
\tag{25}
\]

将式 (1)、(23) 代入式 (25)并相加，exact rational arithmetic给式 (3)。这完成
定理 248-A。`square`

## 7. Numerator margin 仅为 [E]

笔记 246 的 double-precision good-cell lower/exact ratio为约 `0.19987`。用其与
surrogate diagonal形成的规划 anchor约为

\[
 N_{\rm float}\approx0.00014074755.
\tag{26}
\]

要结合严格式 (3)达到 `N_lower/D_upper>0.10`，只需 directed numerator证明

\[
 N_{\rm lower}>
 0.0000735925241553713216150037691.
\tag{27}
\]

式 (26)约为式 (27)的 `1.91` 倍，显示有明显数值余量 [E]；但在 cosine values、
cell ratio predicates和 lower density全部作 outward rational enclosure之前，不能把
该余量升级为 [T]。

## 8. 下一最小引理 B1g [O]

对同一固定实例和 `h=0.005`：

1. 用 rational range reduction和 alternating Taylor remainder enclosure每个
   midpoint的 `cos(xi lambda)`；
2. 从 base coefficient intervals同时 enclosure `W_p,W_c,d-hat`；
3. 对式 (14)作 interval evaluation，并加入笔记 246 的 cell Lipschitz radii；
4. 只保留整格满足 `[1/4,4]` ratio与 `|Q|>0` 的 cells；
5. 以 exact rational sum证明式 (27)。

完成后，式 (3) 与式 (27) 将给第一个 intended finite ratio certificate。随后才能研究
continuum refinement与 `Y,N` 增长，不得从单实例直接外推 uniform B1a。

晋级条件：输出 verified cell list的 hash、每格 rational lower、总 `N_lower` 与
`N_lower/D_upper>0.10`。止损条件：若 global Lipschitz error吃掉余量，先用 local
derivative intervals或将 `h` 减半；不得用 raw midpoint mask替代 whole-cell验证。

## 9. 删除、公理、循环性与模型范围

最小输入：finite prime powers、finite rational continuum mesh、elementary exponential
series、Simpson remainder、IEEE binary64 model、convolution TV algebra及笔记 247 的
Brownian perturbation theorem。

删除审计：

- 删除 Simpson fourth-derivative bound，continuum intervals不是证明；
- 删除 quartic coefficient errors，只控制 base symbol不能控制 response；
- 删除 pruning ledger，surrogate energy与 intended response之间仍有实现缺口；
- 删除再次 centering residual，式 (1)与 forward replay比较的对象不同；
- 删除 support length，TV error不能转成 Brownian `L2` error；
- 删除 directed numerator，式 (3)单独不能证明 ratio capture；
- 把 fixed `(8,10,4)` 结论外推到增长尺度，违反 finite-to-bulk纪律。

非同义反复审计：定理 248-A只给 denominator upper；desired numerator或 ratio并未写入
公理。它可以失败而不与任何定义矛盾。

循环性审计：未使用 zeros、RH/GRH、Weil positivity、PNT误差、Mertens平方根界或
bounded negative index。全部 arithmetic inputs是七个显式 prime-power weights与五个
finite continuum integrals。

适用范围：

- Riemann/Dedekind positive-coefficient finite models可直接使用；
- Dirichlet/automorphic complex coefficients需使用 complex rectangle arithmetic，并把
  real-embedded forward bound替换为完整 complex operation ledger；
- 函数域 degree lattice无需 transcendental lag enclosure，但 coefficient field需另行处理；
- 这是显式公式型 Weil response配置的一部分，不构造上同调、极化或 Hard Lefschetz
  bridge。

本轮把 B1f 中的 denominator与 base coefficient rationalization完全闭合；唯一紧邻
缺口已缩成 B1g 的 finite directed trigonometric numerator。scale-uniform physical
overlap仍是其后的独立算术定理，不由本轮有限证书产生。

后续：笔记 249 已以 directed trigonometric/fixed-point intervals 闭合 B1g，得到
该固定实例的 `N_lower/D_upper>0.19` 与 physical overlap gain [T]；当前进入第二
尺度 B1h，uniform B1a 仍为 [O]。
