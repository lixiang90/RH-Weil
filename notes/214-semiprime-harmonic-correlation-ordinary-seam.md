# 214. 二素数谐和相关闭合 ordinary ratio seam

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 NCE-8 / alternating response Gram

状态：ordinary translated-overlap identity、determinant lift、
\((\Lambda*\Lambda)\) 谐和相关预算、全部 ordinary off-diagonal evacuation 与
primitive hyperbolic atomic diagonalization 为 [T]；Evans 的 almost-all
\(E_2\)-shift theorem 为 [R]；有限 flat-window 审计为 [E]；\(ab>X\) sector、
中心 ratio 与 dyadic exceptional family 为 [O]。

## 1. 本轮结论

笔记 213 把 aperture seam 的唯一开放部分缩成 real log-ratio differences 接近
零的 ordinary channel。本轮证明它也无条件为 \(o(N)\)。关键不是逐条
determinant layer 猜测相消，而是把四个 prime-power variables 合并成两个
二素数型变量

\[
 m=ad,\qquad n=bc,\qquad h=m-n=ad-bc.
\tag{1}
\]

记

\[
 \mathcal A(n)=(\Lambda*\Lambda)(n)
 =\sum_{uv=n}\Lambda(u)\Lambda(v).
\tag{2}
\]

ordinary Toeplitz main term的绝对值由单一谐和相关控制：

\[
 \boxed{
 \beta_L^4L
 \sum_{\substack{m\ne n\le C X\\C^{-1}\le m/n\le C}}
 \frac{\mathcal A(m)\mathcal A(n)}{|m-n|}.}
\tag{3}
\]

本轮证明，对每个 fixed \(C>1\)，

\[
 \boxed{
 \sum_{\substack{m\ne n\le C X\\C^{-1}\le m/n\le C}}
 \frac{\mathcal A(m)\mathcal A(n)}{|m-n|}
 =o(XL^4).}
\tag{4}
\]

因 \(\beta_L^4L\asymp L^{-3}\)、\(N\asymp XL\)，式 (3)--(4) 为
\(o(N)\)。再加上迹类 Hankel 余项与 finite/bulk transfer，全部 ordinary
off-diagonal pairs 均为 \(o(N)\)。结合笔记 212--213，得到

\[
 \boxed{
 \left\|
 \sum_{\substack{ab\le X\\\operatorname{base}(a)\ne\operatorname{base}(b)}}
 F_{a/b}^{fin}
 \right\|_{HS}^2
 =
 \sum_{\substack{ab\le X\\\operatorname{base}(a)\ne\operatorname{base}(b)}}
 \|F_{a/b}^{fin}\|_{HS}^2+o(N).}
\tag{5}
\]

这里的 pairs 是 von Mangoldt 支撑上的 primitive distinct-base singleton ratios；
中心 ratio 与同素数 chains 仍按笔记 209 单独处理。

式 (4) 的唯一非初等输入是 Natalie Evans 对一般 \(E_2\) 数的 almost-all
shift asymptotic。它是已发表的平均移位定理，不是 Hardy--Littlewood 的逐 shift
猜想，也不使用 RH。

## 2. Ordinary translated overlap 的六窗恒等式

写

\[
 x_a=\log a,\quad x_b=\log b,\quad
 x_c=\log c,\quad x_d=\log d,
\]

\[
 s=x_a-x_b,\qquad t=x_c-x_d,\qquad \Delta=s-t.
\tag{6}
\]

由笔记 211 的 radial symbol identity，

\[
 Q_{a/b}(u)
 =b_ab_b\phi(u)\phi(u-s)\phi(x_a-u)^2.
\tag{7}
\]

### 引理 214-A（ordinary six-window overlap）[T]

在周期零延拓约定下，几乎处处有

\[
 \boxed{
 \begin{aligned}
 Q_{a/b}(u)Q_{c/d}^{[\Delta]}(u)
 ={}&b_ab_bb_cb_d\,
 \phi(u)\phi(u-\Delta)\phi(u-s)^2\\
 &\times\phi(x_a-u)^2
 \phi(x_a+x_d-x_b-u)^2.
 \end{aligned}}
\tag{8}
\]

#### 证明

由 \(Q_{c/d}^{[\Delta]}(u)=Q_{c/d}(u-\Delta)\)，

\[
 \begin{aligned}
 Q_{c/d}^{[\Delta]}(u)
 =b_cb_d\,&\phi(u-\Delta)
 \phi(u-\Delta-t)\\
 &\times\phi(x_c-u+\Delta)^2.
 \end{aligned}
\]

式 (6) 给

\[
 u-\Delta-t=u-s,
\]

以及

\[
 x_c+\Delta=x_a+x_d-x_b.
\]

与式 (7) 相乘即得式 (8)。\(\square\)

这个 identity 显示 ordinary channel 的真实 radial mismatch 是
\(x_d-x_b\)，但仅用 \(0\le\phi\le1\) 已足以取得本轮绝对上界：

\[
 \left|
 \widehat{Q_{a/b}Q_{c/d}^{[\Delta]}}(0)
 \right|
 \le |b_ab_bb_cb_d|.
\tag{9}
\]

因此本轮不需要假设 window overlap 自身产生 radial decay；笔记 211-E 的
window-only no-go 不受影响。

## 3. Determinant lift 到 \(\Lambda*\Lambda\)

由式 (1)，

\[
 \Delta=\log\frac{ad}{bc}=\log\frac mn.
\tag{10}
\]

若 \(|\Delta|\le C_0\)，则 \(m/n\) 位于 fixed compact interval。又因

\[
 mn=abcd=(ab)(cd)\le X^2,
\tag{11}
\]

所以

\[
 m,n\le C_1X
\tag{12}
\]

其中 \(C_1\) 只依赖 \(C_0\)。

令

\[
 \mathcal D_d(\Delta)=\sum_{k=0}^{d-1}e^{ikh_0\Delta},
 \qquad h_0=2\pi/L.
\tag{13}
\]

当 \(|\Delta|\le C_0\)、\(L\) 足够大时，

\[
 |\mathcal D_d(\Delta)|
 \ll\min\left(d,\frac L{|\Delta|}\right).
\tag{14}
\]

由 logarithm 的 mean-value theorem 与 \(m/n\asymp1\)，

\[
 |\Delta|\asymp\frac{|m-n|}{\max(m,n)}.
\tag{15}
\]

### 定理 214-B（ordinary response majorized by semiprime harmonic energy）[T]

对任意 fixed \(C_0>0\)，所有满足 \(ab,cd\le X\)、
\(a/b\ne c/d\) 与 \(|s-t|\le C_0\) 的 translated-symbol Toeplitz main terms
的绝对值总和至多

\[
 \boxed{
 C\beta_L^4L
 \sum_{\substack{m\ne n\le C_1X\\C_1^{-1}\le m/n\le C_1}}
 \frac{\mathcal A(m)\mathcal A(n)}{|m-n|}.}
\tag{16}
\]

#### 证明

笔记 213-A 的 exact trace identity、式 (9) 与式 (14)--(15) 给单个 atom pair
的 main-term absolute bound

\[
 \begin{aligned}
 &\beta_L^4
 |b_ab_bb_cb_d|\,|\mathcal D_d(\Delta)|\\
 &\quad\ll
 \beta_L^4 L
 \frac{\Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)}
 {|m-n|\sqrt{mn}}
 \max(m,n)\\
 &\quad\ll
 \beta_L^4 L
 \frac{\Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)}{|m-n|}.
 \end{aligned}
\tag{17}
\]

常数 \((2\pi)^{-4}\) 已吸收到 \(C\) 中。固定 \(m=ad\)、\(n=bc\) 后，

\[
 \sum_{ad=m}\Lambda(a)\Lambda(d)=\mathcal A(m),
 \qquad
 \sum_{bc=n}\Lambda(b)\Lambda(c)=\mathcal A(n).
\tag{18}
\]

删除 distinct-base、primitive 与两个 hyperbolic cutoff 的限制只增大非负
majorant。式 (11)--(12) 再给式 (16)。\(\square\)

式 (18) 是严格降维：原来的四变量 Farey determinant incidence 被压成
\(\Lambda*\Lambda\) 的一维 additive shift correlation。

## 4. Elementary \(\Lambda*\Lambda\) budgets

### 引理 214-C（first moment, pointwise bound and second moment）[T]

一致地有

\[
 \sum_{n\le Y}\mathcal A(n)\ll Y\log Y,
\tag{19}
\]

\[
 0\le\mathcal A(n)\le(\log n)^2,
\tag{20}
\]

以及

\[
 \sum_{n\le Y}\mathcal A(n)^2\ll Y(\log Y)^3.
\tag{21}
\]

#### 证明

Chebyshev bound \(\psi(z)\ll z\) 与 partial summation 给

\[
 \begin{aligned}
 \sum_{n\le Y}\mathcal A(n)
 &=\sum_{u\le Y}\Lambda(u)\psi(Y/u)\\
 &\ll Y\sum_{u\le Y}\frac{\Lambda(u)}u
 \ll Y\log Y.
 \end{aligned}
\]

若 \(n\) 含三个以上不同 prime bases，则 \(\mathcal A(n)=0\)。若
\(n=p^j\)，则
\(\mathcal A(n)=(j-1)(\log p)^2\le(\log n)^2\)。若
\(n=p^iq^j\)、\(p\ne q\)，只有两个 ordered factorizations，故

\[
 \mathcal A(n)=2\log p\log q\le(\log n)^2.
\]

这证明式 (20)。式 (21) 由
\(\sum\mathcal A^2\le(\max\mathcal A)\sum\mathcal A\) 得到。\(\square\)

### 引理 214-D（proper-prime-power and factor-two error）[T]

令 \(\mathcal A_{oo}\) 只保留式 (2) 中 \(u,v\) 均为 odd primes 的项，并令

\[
 \mathcal E=\mathcal A-\mathcal A_{oo}\ge0.
\]

则

\[
 \sum_{n\le Y}\mathcal E(n)\ll Y.
\tag{22}
\]

此外，所有至少含一个 \(\mathcal E\) factor 的谐和 cross terms 总计

\[
 O\bigl(Y(\log Y)^3\bigr).
\tag{23}
\]

#### 证明

含 factor \(2\) 的 prime-prime terms 总质量由
\(\log2\,\psi(Y/2)\ll Y\) 控制。含 proper prime power
\(p^j\)、\(j\ge2\) 的 terms 至多

\[
 2\sum_{p^j\le Y,\ j\ge2}
 \log p\,\psi(Y/p^j)
 \ll
 Y\sum_p\sum_{j\ge2}\frac{\log p}{p^j}
 \ll Y.
\]

故式 (22) 成立。再用式 (20)，例如

\[
 \begin{aligned}
 \sum_{1\le h\le CY}\frac1h
 \sum_n\mathcal E(n)\mathcal A(n+h)
 &\le
 (\log(CY))^2
 \left(\sum_n\mathcal E(n)\right)
 \sum_{h\le CY}\frac1h\\
 &\ll Y(\log Y)^3.
 \end{aligned}
\]

交换两个 factors 及 \(\mathcal E\mathcal E\) 项相同，得到式 (23)。\(\square\)

所以谐和相关的主对象可以无损换成由 odd \(E_2\) numbers 支撑的
\(\mathcal A_{oo}\)。特别地，odd shifts 的主相关严格为零。

## 5. 外部 almost-all \(E_2\)-shift 输入

### 定理 214-E（Evans, general \(E_2\) correlations）[R]

固定 \(\varepsilon>0\)、\(B>0\)、\(A>3\)。若

\[
 \exp((\log Y)^{1-\varepsilon})\le H
 \le Y(\log Y)^{-A},
\tag{24}
\]

则除 \(O(H(\log Y)^{-B})\) 个 \(0<|h|\le H\) 外，\(E_2\) numbers 的
shift correlation 在 \((Y,2Y]\) 上满足 Hardy--Littlewood 型渐近。

本笔记只使用其以下上界后果。由 Chebyshev bound 和按较小 prime factor
求和，

\[
 \sum_{Y<n\le2Y}\mathbf1_{E_2}(n)
 \ll \frac{Y\log\log Y}{\log Y}.
\]

因此对 nonexceptional even \(h\)，Evans 的渐近给

\[
 \sum_{Y<n\le2Y}
 \mathbf1_{E_2}(n)\mathbf1_{E_2}(n+h)
 \ll
 \mathfrak S(h)Y
 \left(\frac{\log\log Y}{\log Y}\right)^2,
\tag{25}
\]

并使用同文记录的

\[
 \sum_{h\le H}\mathfrak S(h)\ll H.
\tag{26}
\]

来源：Natalie Evans, *Correlations of almost primes*, Mathematical
Proceedings of the Cambridge Philosophical Society 174 (2023), 301--344，
Theorem 1.3 与 Lemma 2.1。

这里没有使用逐 fixed shift 的 \(E_2\)-pair conjecture；允许的 exceptional
shifts 将由式 (21) 的 Cauchy budget 吸收。

## 6. 谐和二素数相关定理

对 fixed \(C>1\)，定义

\[
 \mathfrak H_C(Y)
 =
 \sum_{\substack{m\ne n\le CY\\C^{-1}\le m/n\le C}}
 \frac{\mathcal A(m)\mathcal A(n)}{|m-n|}.
\tag{27}
\]

### 定理 214-F（harmonic semiprime correlation saving）[T]

\[
 \boxed{\mathfrak H_C(Y)=o(Y(\log Y)^4).}
\tag{28}
\]

#### 证明

先按 \(R<n\le2R\) 对较小变量作 dyadic 分解。comparability 只引入依赖
\(C\) 的有限个相邻 dyadic ranges。由引理 214-D，含 \(\mathcal E\) 的项为
\(O(R(\log R)^3)\)，故只需考虑 \(\mathcal A_{oo}\)。

置 \(\ell=\log R\)，并在定理 214-E 中固定

\[
 \varepsilon=1/4,\qquad A=4,\qquad B=3.
\]

再置

\[
 H_0=\exp(\ell^{3/4}).
\tag{29}
\]

把 positive shifts 分成三段；negative shifts 交换 \(m,n\) 即可。

**小 shifts：\(1\le h\le H_0\)。** 由 Cauchy--Schwarz 与式 (21)，每个
shift correlation 至多 \(O(R\ell^3)\)。因此

\[
 \sum_{h\le H_0}\frac1h
 \sum_{R<n\le2R}\mathcal A_{oo}(n)\mathcal A_{oo}(n+h)
 \ll R\ell^3\log H_0
 =R\ell^{15/4}
 =o(R\ell^4).
\tag{30}
\]

**中等 shifts：\(H_0<h\le R\ell^{-4}\)。** 按
\(H/2<h\le H\) dyadically 分块，并以该 block 的 upper endpoint \(H\)
应用定理 214-E；这样每次都有 \(H\le R\ell^{-4}\)。nonexceptional even
shifts 上，因

\[
 \mathcal A_{oo}(n)\le2\ell^2\mathbf1_{E_2}(n),
\tag{31}
\]

式 (25)--(26) 给每个 dyadic block 的总贡献

\[
 \ll R\ell^2(\log\ell)^2.
\tag{32}
\]

exceptional shifts 至多 \(O(H\ell^{-3})\) 个；式 (21) 给它们的 block
贡献

\[
 \ll R.
\tag{33}
\]

odd shifts 的 \(\mathcal A_{oo}\)-correlation 严格为零。中段只有
\(O(\ell)\) 个 dyadic blocks，所以式 (32)--(33) 合计

\[
 O(R\ell^3(\log\ell)^2)=o(R\ell^4).
\tag{34}
\]

**大 shifts：\(R\ell^{-4}<h\le CR\)。** 这里只有
\(O(\log\ell)\) 个 dyadic blocks。每个 block 直接用式 (21) 的 pointwise
Cauchy bound，得到

\[
 O(R\ell^3\log\ell)=o(R\ell^4).
\tag{35}
\]

这证明每个 sufficiently large dyadic \(R\) 的 little-oh。为得到全局一致性，
先把 \(R\le Y^{1/2}\) 的 ranges 用式 (21) 与 harmonic sum 粗估为
\(O(Y^{1/2}(\log Y)^4)\)。对 \(Y^{1/2}<R\le CY\)，所有参数在
\(R\to\infty\) 下统一，而 dyadic \(R\) 的几何和为 \(O(Y)\)。故总和为
\(o(Y(\log Y)^4)\)，证明式 (28)。\(\square\)

### 删除审计

若只保留式 (21)，则每个 shift 可为 \(O(YL^3)\)，对 \(O(L)\) 个 harmonic
dyadic ranges 求和只得到 \(O(YL^4)\)，恰好没有 little-oh。定理 214-E 的
almost-all shift saving 正是删除这一最后 logarithm；它不是装饰性引用。

## 7. Ordinary channel evacuation

### 定理 214-G（all ordinary main terms are absolutely summable）[T]

对 fixed \(C_0\)，式 (16) 的 ordinary Toeplitz main terms 总和为 \(o(N)\)。

#### 证明

定理 214-B、214-F 与
\(\beta_L^4L\asymp L^{-3}\) 给

\[
 \beta_L^4L\,o(XL^4)=o(XL)=o(N).
\]

\(\square\)

### 引理 214-H（ordinary Hankel and finite transfer remain negligible）[T]

所有 ordinary aperture pairs（包括 self-pairs \(\nu=\mu\)）上 exact
Toeplitz product 的 Hankel trace remainders 总和为

\[
 O\left(\frac{X(1+\log L)}{L^3}\right)=o(N).
\tag{36}
\]

整个 primitive \(ab\le X\) aggregate 的 finite/Toeplitz norm-square
transfer，以及其 atomic diagonal sums 的 transfer，都是 \(o(N)\)。

#### 证明

由笔记 213-D，单 atom-pair Hankel trace 至多

\[
 C\beta_L^4(1+\log L)|b_ab_bb_cb_d|.
\]

笔记 212-B 给每个 fixed aperture
\(\mathscr M_\nu\ll\sqrt X\)。ordinary bounded-band block-pair graph 在加入
所有 self-loops \((\nu,\nu)\) 后仍只有 \(O(L)\) 对；故对 coefficient mass
绝对求和得到式 (36)。

这里不能只引用逐 seam-edge 的 212-(16c)，因为它不覆盖同一 aperture 内部
的 distinct atom pairs。正确的 transfer 分成两部分：笔记 212-(16a) 给整个
primitive aggregate 的 finite/Toeplitz norm-square 差为 \(o(N)\)，笔记 209-D
给任意 ratio subset 的 atomic finite/bulk diagonal sums 差为 \(o(N)\)。两者
合起来同时覆盖 same-aperture internal cross terms 与跨 aperture seams。
\(\square\)

定理 214-G 实际控制所有 \(|s-t|\le C_0\) 的 distinct ordinary pairs，包含
同一 aperture 内部以及跨人工 partition boundary 的 pairs。因此 ordinary seam
不是只在 block level 被绕过，而是 atomically evacuated。

## 8. Primitive hyperbolic atomic diagonalization

### 定理 214-I（complete \(ab\le X\) primitive ratio diagonalization）[T]

式 (5) 成立。

#### 证明

把 distinct atom pairs 分成：

1. real difference \(|s-t|\le C_0\) 的 ordinary pairs；
2. non-seam far aperture pairs；
3. circular differences 接近 \(\pm L\) 的 aliases；
4. circular differences 接近 \(\pm2L\) 的 endpoint aliases。

第一类的 Toeplitz main 与 Hankel remainder 分别由定理 214-G 与引理 214-H
为 \(o(N)\)。第二类由笔记 212-E 与 212-F 为 \(o(N)\)。第三类由笔记
213-E 为 \(o(N)\)。第四类由笔记 213-F 根本为空。这四类覆盖所有不同
primitive ratios。最后，整个 aggregate 的 finite/Toeplitz norm-square
transfer 由 212-(16a) 给出，atomic diagonal transfer 由笔记 209-D 给出；
因此 finite 模型中的全部 off-diagonal contribution 为 \(o(N)\)，得到式
(5)。\(\square\)

这是对笔记 212-G 的重要限定：抽象 bounded-degree PSD path 确实可保留主尺度
excess，但实际 arithmetic ratio family 额外满足 Evans 型 \(E_2\)-shift
平均定理，所以该抽象反例不能嵌入当前 \(ab\le X\) primitive channel。

## 9. 与部分 Weil 配置的接口

定理 214-I 无条件闭合了 alternating 四矩中 primitive hyperbolic
\(ab\le X\) sector 的 finite response Gram。它提供的是 prime-side
trace budget，因此可直接进入笔记 197--198 的部分 Weil rank--trace--inertia
账本；它没有假设：

- zero-side positivity；
- RH/GRH 或临界线比例；
- 完整四矩匹配；
- 谱算子的酉性；
- uniform negative index。

尚不能据此声称改善 \(0.6725007\ldots\)，因为以下 sectors 尚未合并：

1. alternating \(ab>X\) supercritical sector；
2. center ratio \(a=b\)；
3. dyadic/common-base exceptional family；
4. adjacent、continuum 与 Gamma channels 的最终常数账本。

### 修正后的下一最小引理 214-J [O]

对 alternating \(ab>X\) sector，先从 exact support condition 导出一个
finite partition

\[
 \sum_j \mathcal G_j^{>X}
\]

使每个 piece 的 product excess \(\log(ab/X)\) 与 ratio \(\log(a/b)\) 同时
局部化；然后证明其 off-diagonal Gram 归约到哪一个明确的 shifted-convolution
量。若该量仍是式 (27) 的 \(\Lambda*\Lambda\) harmonic correlation，则定理
214-F 可复用；若出现更长的 \(\Lambda^{*3}\) 或无 cutoff correlation，必须单独
标为新的算术输入。

## 10. 公理作用、删除审计与循环性

1. **Toeplitz modulation covariance**：给笔记 213-A 的 translated main term；
   删除后式 (8)、(16) 无法与 finite matrix response 对接。
2. **compact window bound \(0\le\phi\le1\)**：只给式 (9) 的 absolute
   majorant；不负责 arithmetic log saving。
3. **hyperbolic cutoff \(ab,cd\le X\)**：通过式 (11) 把 \(m,n\) 限制在
   \(O(X)\)。删除后 Evans theorem 的尺度不能直接套用。
4. **von Mangoldt multiplicative support**：负责 exact convolution identity
   (18)。一般 coefficients 不会自动产生 \(\Lambda*\Lambda\)。
5. **Evans almost-all shift theorem**：负责从 borderline \(O(XL^4)\) 删除一个
   logarithm；删除后 Cauchy 预算恰好停在主尺度。
6. **Hankel trace-class regularity**：只传递 main-term saving 到 finite
   Toeplitz product，不产生二素数相关估计。

循环性审计：Evans theorem 是整数侧 \(E_2\) additive correlation 的无条件平均
定理。它不引用 zeta zeros 的中心线位置；式 (28) 也明显弱于逐 shift
Hardy--Littlewood asymptotic。因此本轮不是把 RH 或完整四矩换名为“算术公理”。

结论不是公理改写：四变量 determinant response 经式 (18) 降为一维
\(\Lambda*\Lambda\) correlation，再由 small/middle/large shift 三段预算闭合；
其中 exceptional shifts 被独立的 second-moment bound 吸收。

## 11. 模型范围

- **Riemann zeta**：定理 214-I 直接适用于当前 primitive hyperbolic sector。
- **固定本原 Dirichlet \(L\)**：character phases 的绝对值为一，定理 214-B 的
  majorant保持；imprimitive/local bad-prime terms 需有限修正。
- **Dedekind/automorphic \(L\)**：需要相应 coefficient convolution 的 almost-all
  additive-shift theorem；Evans 的 scalar \(E_2\) 定理不能自动替代
  Rankin--Selberg 输入。
- **函数域**：degree shift 是离散的，可能用有限域几何或大筛直接验证 analogue；
  这仍不建立 cohomological 与 explicit-formula Weil structures 的等价。
- **无 Euler product 的负向模型**：式 (18) 失效，说明本轮 saving 来自真实
  arithmetic convolution，而非函数方程本身。

## 12. 可复现审计 [E]

脚本 `scripts/ordinary_seam_kernel_audit.py`：

1. 使用 \(T=2\pi X\)、\(d\approx XL\) 的精确 Gabor 时间格点；
2. 对 flat compact window 精确计算 translated interval overlap；
3. 对三个 aperture shifts 测量 actual signed ordinary neighbor main term 与
   absolute majorant；
4. 枚举实际 primitive distinct-base prime-power ratios；
5. 用 FFT 计算 \(\mathcal A=\Lambda*\Lambda\) 的完整谐和自相关；
6. 检查 \(\sum\mathcal A^2/(XL^3)\) 与 proper-prime-power error \(O(X)\)
   的尺度。

在 \(X=2000,5000,20000,100000\) 上，
\(\mathfrak H(X)/(XL^4)\) 从约 \(0.0642\) 降至 \(0.0532\)。这些数值只验证
索引、normalization 与理论 majorant 的方向；式 (28) 的证明来自定理 214-E
与三段解析预算，而不是有限外推。

## 13. 后续更新（笔记 215）

笔记 215 将本笔记的 little-oh 加强为：对任意 fixed \(\vartheta>0\)，有
\(o_\vartheta(Y(\log Y)^{3+\vartheta})\)，并引入 product excess
\(e=\log(ab/X)\) 与 ratio \(s=\log(a/b)\) 的精确坐标。determinant
scale 为 \(Y=X\exp((e+e')/2)\)，卷积阶仍是 \(\Lambda*\Lambda\)；由此
任意 fixed \(\kappa<1\) 的 supercritical collar
\(ab\le X(\log X)^\kappa\) 也已 atomic diagonalize。新的最小输入位于
\(ab\asymp X\log X\) 的 transition layer。
