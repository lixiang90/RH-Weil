# 210. Local prime-power energy closes square-root alternating boxes

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 NCE-8 / local Vaughan rectangles

状态：dyadic von Mangoldt 能量、rectangular ratio spacing、局部
Montgomery--Vaughan 闭合、固定 determinant layer 的 degree-two Schur 结构为
[T]；有限审计为 [E]；跨越无界多个 radial boxes 的 coherence、中心 ratio 与
base-2 exceptional aggregate 为 [O]。

> **后续修正（笔记 211）**：本笔记 210-H 的单-pair `o(N)` 目标由
> 定理 210-D 的单-box 范数和 Cauchy 自动推出，不能作为路线晋级条件。
> `J asymp L` 个 radial boxes 即使每一对都是 `o(N)`，总体仍可达到主尺度。
> 正确的下一输入是 actual normalized multibox Gram 的 radial row sum 为
> `o(L)`；窗口正则性与 fixed-determinant maximum degree 均不足以验证它。

## 1. 修正与主要结论

笔记 209-E 在单个 box 中使用了全区间粗界

\[
 \sum_{n\le X}|b_n|^2\ll L^2.
\]

该界足以证明 sub-square-root closure，但在 dyadic box 上损失了一个完整的
\(L\) 因子。真实局部预算是

\[
 \sum_{Y\le n\le2Y}|b_n|^2\ll\log(2Y),
 \qquad
 \sum_{Y\le n\le2Y}|b_n|\ll\sqrt Y.
\tag{1}
\]

恢复式 (1) 后得到：

1. 若 numerator scale 为 \(A\)、denominator scale 为 \(B\)，则单个
   primitive rectangular ratio box 的 bulk Montgomery--Vaughan remainder 为

   \[
    O\!\left(
    \beta_L^4LAB\log(2A)\log(2B)
    \right).
   \tag{2}
   \]

2. 对任意 fixed \(\varepsilon>0\)，只要

   \[
    AB\le XL^{2-\varepsilon},
   \tag{3}
   \]

   整个真实 finite rectangular box 渐近对角化。
3. 特别地，balanced box \(A=B=Y\) 在

   \[
    Y\le\sqrt X\,L^{1-\delta}
   \tag{4}
   \]

   对任意 fixed \(\delta>0\) 都已闭合。故 \(Y\asymp\sqrt X\) 不是
   within-box hard core；笔记 209 中相反的判断来自全区间能量的过粗代入。
4. 对固定非零 determinant \(h=ad-bc\)，同一 rectangular box 上的有向
   incidence graph 的最大出度和入度都不超过 \(2\)。因此 \(h=\pm2\)
   actual response layer 已有 degree-two Schur bound，不需要猜测任意 Farey
   coefficient 的 Bessel 界。

这不闭合完整 alternating family：不同 dyadic radial boxes 之间仍可有非常近的
ratios。开放输入被移动到 **cross-box coherence** 以及
\(AB\gtrsim XL^2\) 的 within-box 区域，而不是宣称整个 alternating 四矩已解决。

## 2. Local von Mangoldt budgets

沿用

\[
 b_n=-\frac1{2\pi}\frac{\Lambda(n)}{\sqrt n},
 \qquad L=\log X.
\tag{5}
\]

令

\[
 \mathcal P(U)=\{n\in[U,2U]:\Lambda(n)\ne0\},
\]

\[
 W_2(U)=\sum_{n\in\mathcal P(U)}|b_n|^2,
 \qquad
 W_1(U)=\sum_{n\in\mathcal P(U)}|b_n|.
\tag{6}
\]

为使外部输入最小化，先给所需 Chebyshev bound 的 elementary derivation。对正整数
\(m\)，区间 \((m,2m]\) 中每个 prime 都整除 central binomial coefficient，故

\[
 \vartheta(2m)-\vartheta(m)
 \le \log {2m\choose m}\le 2m\log2.
\]

按 dyadic intervals 求和得到 \(\vartheta(t)\ll t\)。再把 primes 分成
\(p\le\sqrt t\) 与 \(p>\sqrt t\)，得到
\(\pi(t)\ll t/\log(2t)\)。因此以下引理不需要另加解析素数定理输入。

### 引理 210-A（local prime-power energy and mass）[T]

对 \(U\ge3\)，

\[
 \boxed{
 W_2(U)\ll\log(2U),
 \qquad W_1(U)\ll\sqrt U.}
\tag{7}
\]

此外，\(\mathcal P(U)\) 的元素个数满足

\[
 \#\mathcal P(U)\ll\frac{U}{\log(2U)}.
\tag{8}
\]

#### 证明

Chebyshev 上界 \(\vartheta(t)=\sum_{p\le t}\log p\ll t\) 给

\[
 \sum_{U\le p\le2U}\frac{(\log p)^2}{p}
 \le \frac{\log(2U)}{U}\vartheta(2U)
 \ll\log(2U),
\tag{9}
\]

以及

\[
 \sum_{U\le p\le2U}\frac{\log p}{\sqrt p}
 \le U^{-1/2}\vartheta(2U)
 \ll\sqrt U.
\tag{10}
\]

指数 \(k\ge2\) 的 prime powers 在 \([U,2U]\) 中至多
\(O(\sqrt U\log U)\) 个。逐项使用

\[
 \frac{(\log p)^2}{p^k}\le\frac{(\log(2U))^2}{U},
 \qquad
 \frac{\log p}{p^{k/2}}\le\frac{\log(2U)}{\sqrt U},
\]

得到它们对式 (7) 的贡献分别为
\(O(U^{-1/2}\log^3 U)\) 与 \(O(\log^2U)\)，均被式 (7) 吸收。
Chebyshev 的 \(\pi(2U)\ll U/\log(2U)\) 与相同 prime-power 计数给式
(8)。\(\square\)

这里只用 elementary Chebyshev estimates；没有调用 PNT、零自由区域或任何
零点信息。

## 3. Rectangular primitive ratio boxes

令 \(2\le A,B\le X\)。定义

\[
 \mathcal R_{A,B}
 =\left\{
 \rho=\frac ab:
 a\in\mathcal P(A),\ b\in\mathcal P(B),
 \operatorname{base}(a)\ne\operatorname{base}(b)
 \right\}.
\tag{11}
\]

由定理 209-B，每个 \(\rho\in\mathcal R_{A,B}\) 对应唯一 pair \((a,b)\)。
置 \(s_\rho=\log\rho\)，并沿用

\[
 F_\rho^{bulk}
 =\beta_L^2e^{iTs_\rho}T_d(Q_\rho)D_d(s_\rho),
\]

\[
 Q_\rho=b_ab_bq_{x_a}q_{x_b}^{(s_\rho)}.
\tag{12}
\]

### 引理 210-B（rectangular log-ratio spacing）[T]

不同 \(\rho,\sigma\in\mathcal R_{A,B}\) 满足

\[
 |s_\rho-s_\sigma|\gg\frac1{AB}.
\tag{13}
\]

因此当 \(L\) 足够大时，圆周 frequencies \(s_\rho/L\pmod1\) 的间距为

\[
 \Delta_{A,B}\gg\frac1{LAB}.
\tag{14}
\]

#### 证明

写 \(\rho=a/b\)、\(\sigma=c/d\)。因 ratios 不同，

\[
 \left|\frac ab-\frac cd\right|
 =\frac{|ad-bc|}{bd}\ge\frac1{4B^2}.
\]

两 ratios 都在 \([A/(2B),2A/B]\)。在该区间对 logarithm 使用 mean-value
theorem，得到

\[
 |\log(a/b)-\log(c/d)|
 \ge\frac{B}{2A}\left|\frac ab-\frac cd\right|
 \ge\frac1{8AB}.
\]

同一 box 内两个 log-ratios 的差至多 \(\log4\)，所以除以 \(L\) 后不存在
接近一整圈的 wrap-around；式 (14) 成立。\(\square\)

### 引理 210-C（local symbol energy）[T]

定义

\[
 \mathscr S(A,B)
 =\sum_{\rho\in\mathcal R_{A,B}}
 \sum_{r\in\mathbb Z}|\widehat Q_\rho(r)|^2.
\]

则

\[
 \boxed{
 \mathscr S(A,B)\le W_2(A)W_2(B)
 \ll\log(2A)\log(2B).}
\tag{15}
\]

#### 证明

每个 cluster 为 singleton，且 \(0\le q_x\le1\)。Parseval 给

\[
 \sum_r|\widehat Q_{a/b}(r)|^2
 \le |b_a|^2|b_b|^2.
\]

对 \((a,b)\) 求和并使用引理 210-A 即得。\(\square\)

## 4. Local Montgomery--Vaughan closure

### 定理 210-D（rectangular finite ratio diagonalization）[T]

设

\[
 T\asymp X,
 \qquad N\asymp XL,
 \qquad d\asymp TL,
 \qquad \beta_L\asymp L^{-1}.
\tag{16}
\]

对任意 fixed \(\varepsilon>0\)，若式 (3) 成立，则

\[
 \boxed{
 \left\|\sum_{\rho\in\mathcal R_{A,B}}F_\rho^{fin}\right\|_{HS}^2
 =
 \sum_{\rho\in\mathcal R_{A,B}}
 \|F_\rho^{fin}\|_{HS}^2+o(N).}
\tag{17}
\]

little-oh 对满足式 (3) 的 dyadic boxes 一致。

#### 证明：bulk cross term

对笔记 209 的 diagonal-fibre identity 逐 diagonal 应用定理 205-B。引理
210-B 与 210-C 给

\[
 \begin{aligned}
 &\left|
 \left\|\sum_{\rho\in\mathcal R_{A,B}}F_\rho^{bulk}\right\|_{HS}^2
 -\sum_{\rho\in\mathcal R_{A,B}}\|F_\rho^{bulk}\|_{HS}^2
 \right|\\
 &\qquad\ll
 \beta_L^4LAB\,W_2(A)W_2(B)\\
 &\qquad\ll
 \frac{AB}{L}
 \le XL^{1-\varepsilon}=o(N).
 \end{aligned}
\tag{18}
\]

这正是式 (2)。同时

\[
 \sum_{\rho\in\mathcal R_{A,B}}
 \|F_\rho^{bulk}\|_{HS}^2
 \le\beta_L^4dW_2(A)W_2(B)
 \ll N/L^2.
\tag{19}
\]

故 bulk aggregate 的平方范数为 \(O(N)\)。

#### 证明：finite aggregate defect

记 \(E_\rho=F_\rho^{fin}-F_\rho^{bulk}\)。笔记 204 的 uniform Hankel
estimate 给

\[
 \|E_{a/b}\|_{HS}
 \ll\beta_L^2\sqrt{1+\log L}\,|b_ab_b|.
\]

因此不使用任何跨 cluster cancellation，直接由引理 210-A 得

\[
 \begin{aligned}
 \left\|\sum_{\rho\in\mathcal R_{A,B}}E_\rho\right\|_{HS}^2
 &\ll
 \beta_L^4(1+\log L)W_1(A)^2W_1(B)^2\\
 &\ll\frac{AB(1+\log L)}{L^4}=o(N),
 \end{aligned}
\tag{20}
\]

其中最后一步使用式 (3)。此外

\[
 \sum_{\rho\in\mathcal R_{A,B}}\|E_\rho\|_{HS}^2
 \ll\beta_L^4(1+\log L)W_2(A)W_2(B)
 \ll\frac{1+\log L}{L^2}.
\tag{21}
\]

式 (19)--(21) 和 Cauchy--Schwarz 表明 finite/bulk diagonal sums 相差
\(o(N)\)，且 aggregate replacement 产生 \(o(N)\) 误差。结合式 (18) 得
式 (17)。\(\square\)

### 推论 210-E（balanced square-root closure）[T]

对任意 fixed \(\delta>0\)，若

\[
 A=B=Y\le\sqrt X\,L^{1-\delta},
\]

则式 (17) 成立。特别地，\(Y\asymp\sqrt X\) 的单个 dyadic primitive
box 无条件闭合。\(\square\)

## 5. Fixed determinant layers

对 \(h\in\mathbb Z\setminus\{0\}\)，令有向边集

\[
 \mathcal E_h(A,B)=
 \left\{(a/b,c/d)\in\mathcal R_{A,B}^2:ad-bc=h\right\}.
\tag{22}
\]

### 引理 210-F（degree-two determinant incidence）[T]

\(\mathcal E_h(A,B)\) 的每个顶点出度和入度都至多为 \(2\)。

#### 证明

固定 source \(a/b\)。因 \(\gcd(a,b)=1\)，方程

\[
 ad\equiv h\pmod b
\]

把 \(d\) 限制在模 \(b\) 的唯一剩余类。区间 \([B,2B]\) 长为 \(B\)，且
\(b\ge B\)，所以至多含该剩余类中的两个整数；每个 \(d\) 又唯一决定
\(c=(ad-h)/b\)。故出度至多为 \(2\)。

固定 target \(c/d\) 后交换角色，\(bc\equiv-h\pmod d\) 同理给入度至多
为 \(2\)。\(\square\)

定义第 \(h\) 层的 exact bulk cross response

\[
 \begin{aligned}
 \mathcal C_h
 ={}&\beta_L^4
 \sum_{(\rho,\sigma)\in\mathcal E_h(A,B)}
 e^{iT(s_\rho-s_\sigma)}\\
 &\times\sum_r
 \widehat Q_\rho(r)\overline{\widehat Q_\sigma(r)}
 \sum_{k\in I_r}e^{ikh_0(s_\rho-s_\sigma)},
 \end{aligned}
\tag{23}
\]

其中 \(h_0=2\pi/L\) 是 Gabor spacing；它与 arithmetic determinant
\(h\) 不同。

### 定理 210-G（fixed-layer actual-response Schur bound）[T]

\[
 \boxed{
 |\mathcal C_h|
 \ll
 \beta_L^4
 \min\!\left(d,\frac{LAB}{|h|}\right)
 W_2(A)W_2(B).}
\tag{24}
\]

特别地，在式 (3) 下，\(h=\pm2\) 两层各自均为 \(o(N)\)。

#### 证明

由

\[
 \frac{\rho}{\sigma}=\frac{ad}{bc}=1+\frac h{bc}
\]

以及 \(ad,bc\asymp AB\)，有

\[
 |s_\rho-s_\sigma|\gg\frac{|h|}{AB}.
\tag{25}
\]

有限几何和故满足

\[
 \left|\sum_{k\in I_r}e^{ikh_0(s_\rho-s_\sigma)}\right|
 \ll\min\!\left(d,\frac{LAB}{|h|}\right).
\tag{26}
\]

引理 210-F 说明每个 layer adjacency matrix 的最大行和、列和都至多为
\(2\)，所以其 \(\ell^2\) operator norm 至多为 \(2\)。固定 \(r\) 对实际
vector \((\widehat Q_\rho(r))_\rho\) 应用 Schur test，再对 \(r\) 求和并用
引理 210-C，得到式 (24)。最后代入 \(|h|=2\)、式 (3) 与
\(W_2(A)W_2(B)\ll L^2\)，即得 \(o(N)\)。\(\square\)

这里估计的是 actual Toeplitz response vector，不是任意系数的普通 Bessel
预算。它闭合 fixed layer，但不允许把无穷多个 \(h\)-layers 的绝对值直接相加。

## 6. 对笔记 209 的精确修正

笔记 209 的定理 209-A--D、209-F 均保持不变；209-E 的
sub-square-root 结论也仍正确。需要修正的是对其 sharpness 的解释：

1. 式 209-(26) 的 \(\mathcal S_Y\ll L^4\) 是合法但非局部的上界。
2. 在单个 dyadic box 内应改用

   \[
    \mathcal S_Y\ll(\log Y)^2,
   \]

   因而 \(Y\asymp\sqrt X\) 的 remainder 是 \(O(X/L)=o(N)\)，不是
   main scale。
3. 开放引理 209-G 的 \(h=\pm2\) within-box 版本已由定理 210-G 闭合，故不再是
   下一瓶颈。
4. 这不是对完整 Farey family 的闭合，因为把每个 dyadic box 分别对角化并不
   控制不同 boxes 之间的 cross terms。

## 7. 原单-pair 输入与 multibox 修正

### 推论 210-H（fixed-pair radial cross term；由 211-B 闭合）[T]

固定 ratio aperture \(A/B\asymp C/D\)，对相隔多个 dyadic radial scales 的
两个 primitive boxes \(\mathcal R_{A,B}\)、\(\mathcal R_{C,D}\)，有

\[
 2\operatorname{Re}
 \left\langle
 \sum_{\rho\in\mathcal R_{A,B}}F_\rho^{fin},
 \sum_{\sigma\in\mathcal R_{C,D}}F_\sigma^{fin}
 \right\rangle_{HS}
 =o(N)
\tag{27}
\]

成立。这由笔记 211-A--B 的定量单-box 范数与 Cauchy--Schwarz 自动得到。
但逐 pair 结论不能对 \(J\asymp L\) 个 boxes 无损求和；真正所需的 multibox
row-sum criterion 与 sharp no-go 见笔记 211-H--I。

笔记 211-C 已构造保持全部 local norm 与 pairwise little-oh、但 multibox aggregate
达到主尺度的 sharp [N]；笔记 211-E、211-G 又分别排除 window-only 与
maximum-degree-only 的径向衰减。

## 8. 公理作用、删除审计与适用范围

1. **local von Mangoldt energy**：负责把全局 \(L^4\) symbol budget 降为
   \(\log A\log B\)。删除后只能恢复笔记 209 的较弱阈值。
2. **prime-power singleton classification**：保证每个 ratio 只有一个
   arithmetic atom。删除后式 (15) 与 degree-two incidence 都会出现
   multiplicity factors。
3. **Toeplitz covariance**：把 matrix Gram 精确拆成 scalar diagonal fibres；
   删除后不能应用圆周 Montgomery--Vaughan。
4. **uniform Hankel regularity**：只用于式 (20)--(21) 的 finite transfer。
5. **dyadic localization**：保证 log-ratio compactness 与 determinant graph
   的 bounded degree。删除后不同 radial scales 的 cross coherence 无法由单-box
   定理控制；该 multibox 缺口由笔记 211 的 row-sum criterion 精确表述。

模型范围：

- Riemann zeta 满足引理 210-A 的全部 arithmetic input。
- 固定本原 Dirichlet \(L\) 函数的单位角色相位不改变绝对局部预算，但会改变
  cross-box phases。
- Dedekind 与一般 automorphic coefficients 需要另行证明 local Rankin--Selberg
  能量和 ratio multiplicity；不能直接引用本笔记的 singleton 定理。
- 函数域模型可用有界 Euler degree 验证相应 local energy，但这不建立
  cohomological Weil 结构与 explicit-formula 配置的自动等价。

## 9. RH/GRH 循环性与结论边界

- 本轮只使用 Chebyshev、有限 Toeplitz identity 与 Montgomery--Vaughan
  Hilbert inequality，不使用 RH、零密度或素数对猜想。
- 没有闭合 cross-box terms、中心 ratio 或 dyadic base-2 aggregate。
- 没有证明完整 alternating 四矩，也没有改善任何零点比例。
- 式 (17) 是单个 local box 的结论，不能无误差地对 \(O(L^2)\) boxes 求和。
- \(13/18\) 与 \(16/21\) 仍为条件性边界。

## 10. 可复现审计 [E]

脚本 `scripts/alternating_local_box_audit.py` 检查：

1. 三个增长 dyadic boxes 中 \(W_2/\log(2Y)\)、\(W_1/\sqrt Y\) 与
   prime-power count 的归一化；
2. \(h=\pm2\) determinant layers 的最大出度、入度均不超过 \(2\)；
3. layer adjacency 的数值 operator norm 不超过 \(2\)；
4. arithmetic determinant 与 log-ratio gap 的索引及常数方向。

有限实验只审计公式和索引，不证明跨尺度式 (27)。
