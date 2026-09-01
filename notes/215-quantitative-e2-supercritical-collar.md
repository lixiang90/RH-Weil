# 215. 定量 \(E_2\) saving 与 supercritical logarithmic collar

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 NCE-8 / alternating response Gram

状态：product-excess/ratio 坐标恒等式、定量二素数谐和相关、任意
\(\kappa<1\) 的 supercritical logarithmic collar atomic diagonalization 为
[T]；\(\kappa=1\) 处的 absolute-Evans 推理上限为 [N]；transition layer 的
response-weighted shifted correlation 为 [O]。本笔记不更新 PDF。

## 1. 本轮结论

笔记 214 已闭合 \(ab\le X\) 的 primitive distinct-base ratio family。本轮把
该区域严格推进到

\[
 ab\le Z_\kappa:=X(\log X)^\kappa,
 \qquad 0\le\kappa<1.
\tag{1}
\]

首先加强笔记 214-F。对每个 fixed \(C>1\) 与每个 fixed
\(\vartheta>0\)，有

\[
 \boxed{
 \mathfrak H_C(Y)
 =o_{C,\vartheta}\!\left(
 Y(\log Y)^{3+\vartheta}\right).}
\tag{2}
\]

这里

\[
 \mathfrak H_C(Y)
 =
 \sum_{\substack{m\ne n\le CY\\C^{-1}\le m/n\le C}}
 \frac{(\Lambda*\Lambda)(m)(\Lambda*\Lambda)(n)}{|m-n|}.
\tag{3}
\]

其次，若 \(\mathcal P_\kappa(X)\) 表示所有满足

\[
 2\le a,b\le X,\qquad
 \Lambda(a)\Lambda(b)\ne0,\qquad
 \operatorname{base}(a)\ne\operatorname{base}(b),\qquad
 ab\le Z_\kappa
\tag{4}
\]

的 ordered pairs，则

\[
 \boxed{
 \left\|
  \sum_{(a,b)\in\mathcal P_\kappa(X)}F_{a/b}^{fin}
 \right\|_{HS}^2
 =
 \sum_{(a,b)\in\mathcal P_\kappa(X)}
 \|F_{a/b}^{fin}\|_{HS}^2+o(N).}
\tag{5}
\]

不同素数底保证每个 ratio cluster 是 singleton，所以式 (5) 的右端确实是
atomic diagonal sum。式 (5) 包含新的超临界 collar

\[
 X<ab\le X(log X)^\kappa.
\tag{6}
\]

该推进不使用 RH、零点密度猜想或 fixed-shift Hardy--Littlewood 猜想。唯一
非初等输入仍是 Evans 的 almost-all \(E_2\)-shift theorem。

## 2. Product excess 与 ratio 的精确坐标

置

\[
 L=\log X,\qquad
 e=\log\frac{ab}{X},\qquad
 s=\log\frac ab.
\tag{7}
\]

若 \(x_a=\log a\)、\(x_b=\log b\)，则线性反演给

\[
 \boxed{
 x_a=\frac{L+e+s}{2},\qquad
 x_b=\frac{L+e-s}{2}.}
\tag{8}
\]

因为 \(0\le x_a,x_b\le L\)，必有

\[
 |e|\le L,\qquad |s|\le L-|e|,
\tag{9}
\]

端点处只需加入由 \(a,b\ge2\) 产生的 fixed positive gaps。

### 引理 215-A（exact supercritical support depth）[T]

对笔记 211 的 singleton alternating symbol

\[
 Q_{a/b}(u)
 =b_ab_b\phi(u)\phi(u-s)\phi(x_a-u)^2,
\tag{10}
\]

其基本周期内支撑包含于

\[
 \begin{cases}
 [(e+s)/2,L/2],&s\ge0,\\
 [(e+s)/2,L/2+s],&s\le0.
 \end{cases}
\tag{11}
\]

特别地，支撑长度至多

\[
 \boxed{
 \lambda(e,s)=\frac{L-e-|s|}{2}.}
\tag{12}
\]

#### 证明

笔记 213-B 的 interval intersection 实际只使用
\(2\le a,b\le X\)，不使用 \(ab\le X\)。将式 (8) 代入其左端
\(x_a-L/2\) 即得 \((e+s)/2\)。若 \(s\ge0\)，右端为 \(L/2\)；若
\(s\le0\)，右端为 \(L/2+s\)。两种情形的长度都等于式 (12)。
\(\square\)

所以 product excess 增大时，physical radial support 变浅；ratio 靠近允许
端点时也有同样效应。这个几何增益是真实的，但本轮的 collar theorem 甚至不需
利用式 (12) 的小量，只需其 compact support 上界。

### 引理 215-B（determinant-scale identity）[T]

对第二个 atom 定义

\[
 e'=\log\frac{cd}{X},\qquad t=\log\frac cd,\qquad
 \Delta=s-t,\qquad m=ad,\quad n=bc.
\tag{13}
\]

则精确地

\[
 \boxed{
 \log m=L+\frac{e+e'+\Delta}{2},\qquad
 \log n=L+\frac{e+e'-\Delta}{2}.}
\tag{14}
\]

因而

\[
 \frac mn=e^\Delta,\qquad mn=X^2e^{e+e'}.
\tag{15}
\]

#### 证明

由式 (8) 及其 \((c,d)\) 版本，

\[
 \begin{aligned}
 \log(ad)
 &=\frac{L+e+s}{2}+\frac{L+e'-t}{2},\\
 \log(bc)
 &=\frac{L+e-s}{2}+\frac{L+e'+t}{2}.
 \end{aligned}
\]

整理即得式 (14)--(15)。\(\square\)

这回答了笔记 214-J 的第一个结构问题：product/ratio 双局部化后，ordinary
determinant lift 的乘法卷积阶仍是

\[
 \sum_{ad=m}\Lambda(a)\Lambda(d)= (\Lambda*\Lambda)(m),
 \qquad
 \sum_{bc=n}\Lambda(b)\Lambda(c)= (\Lambda*\Lambda)(n).
\tag{16}
\]

式 (16) 对删除 product/ratio cell restrictions 后的正 majorant 是精确的。
必须区分：在单个 cells 内，\(e(a,b)\) 与 \(e(c,d)\) 的条件会耦合
\(ad=m\)、\(bc=n\) 的四个 factors，所以 exact signed coefficient 是一个
restricted four-variable \(E_2\) correlation，而不必等于
\(\mathcal A(m)\mathcal A(n)\)。但它逐项由后者支配，且仍只含两组二重
divisor factorizations；不会出现 \(\Lambda^{*3}\)。

新的困难是式 (14) 的 **scale inflation**：当
\(e,e'>0\) 时，\(m,n\) 的自然尺度从 \(X\) 增大到

\[
 Y(e,e')=Xe^{(e+e')/2}.
\tag{17}
\]

### Product-ratio finite partition [T]

固定小常数 \(\omega>0\)，定义 cells

\[
 \mathcal C_{r,\nu}
 =\left\{(a,b):
 r\omega\le e<(r+1)\omega,
 \ \nu\omega\le s<(\nu+1)\omega
 \right\}.
\tag{18}
\]

由式 (9)，完整三角形只需 \(O(L^2)\) 个 cells；在式 (1) 的 collar 中，
\(r=O(\log L)\)，故只需

\[
 O(L\log L)
\tag{19}
\]

个 cells。式 (14) 说明任意一对 cells 对应一个 fixed multiplicative-width
的 \((m,n)\)-range。这个 partition 是 exact bookkeeping，不把正性或
cancellation 隐藏进 cells。

## 3. 定量二素数谐和相关

### 定理 215-C（quantitative harmonic semiprime saving）[T]

式 (2) 成立。

外部输入仍是 Evans, *Correlations of almost primes*, Theorem 1.3。其正式
陈述允许任意 fixed \(\varepsilon>0\)，并没有 “sufficiently small” 限制；
因此下面令 \(\varepsilon=1-\vartheta/2\) 合法。该限制出现在同文的
Theorem 1.4，而不是本证明使用的 Theorem 1.3。

来源：<https://doi.org/10.1017/S0305004122000251>。

#### 证明

若 \(\vartheta=1\)，笔记 214-F 已给
\(o(Y(\log Y)^4)\)；若 \(\vartheta>1\)，elementary
\(O(Y(\log Y)^4)\) 已是所需 little-oh。以下设
\(0<\vartheta<1\)。

按较小变量 \(R<n\le2R\) 作 dyadic 分解，并置

\[
 \ell=\log R,\qquad
 \eta=\vartheta/2,\qquad
 H_0=\exp(\ell^\eta).
\tag{20}
\]

在 Evans theorem 中取

\[
 \varepsilon=1-\eta,\qquad A=4,\qquad B=4.
\tag{21}
\]

则其允许的最小 shift 恰为
\(\exp(\ell^{1-\varepsilon})=H_0\)。沿用笔记 214-D，将 proper prime
powers 与 factor \(2\) 的总贡献控制为 \(O(R\ell^3)\)。只需处理 odd
prime-prime part \(\mathcal A_{oo}\)。

**小 shifts。** 由
\(\sum_{n\le CR}(\Lambda*\Lambda)(n)^2\ll R\ell^3\)，
Cauchy--Schwarz 给每个 shift correlation \(O(R\ell^3)\)。所以

\[
 \sum_{h\le H_0}\frac1h
 \sum_{R<n\le2R}\mathcal A_{oo}(n)\mathcal A_{oo}(n+h)
 \ll R\ell^{3+\eta}.
\tag{22}
\]

**中等 shifts。** 对
\(H_0<h\le R\ell^{-4}\) 按 \(H/2<h\le H\) 分块。对
nonexceptional even shifts，Evans asymptotic、
\(\mathcal A_{oo}(n)\le2\ell^2\mathbf1_{E_2}(n)\) 与 singular-series
平均上界给每个 block

\[
 O\bigl(R\ell^2(\log\ell)^2\bigr).
\tag{23}
\]

exceptional shifts 至多 \(O(H\ell^{-4})\) 个。每个相关由 Cauchy 控制为
\(O(R\ell^3)\)，而 block 内 \(1/h\ll1/H\)，故 exceptional contribution
为 \(O(R/\ell)\)。odd shifts 的 \(\mathcal A_{oo}\)-correlation 为零。
中段共有 \(O(\ell)\) 个 blocks，故总计

\[
 O\bigl(R\ell^3(\log\ell)^2\bigr).
\tag{24}
\]

**大 shifts。** 对
\(R\ell^{-4}<h\le CR\) 的 \(O(\log\ell)\) 个 dyadic blocks，逐 shift
Cauchy 给

\[
 O(R\ell^3\log\ell).
\tag{25}
\]

因为 \(\eta<\vartheta\)、\((\log\ell)^2=o(\ell^\vartheta)\)，
式 (22)、(24)、(25) 均为
\(o_\vartheta(R\ell^{3+\vartheta})\)。负 shifts 交换变量。小于
\(Y^{1/2}\) 的初始 dyadic ranges 用 elementary second moment 控制；其总量
为 \(O(Y^{1/2}(\log Y)^4)\)，也被式 (2) 吸收。对其余 ranges 有
\(\ell\asymp\log Y\)，按 \(R\) 作几何求和得到式 (2)。\(\square\)

定理 215-C 比笔记 214-F 的 little-oh 形式保留了可用于移动 cutoff 的明确
log saving。它仍只使用 almost-all shifts；exceptional shifts 由独立二阶矩
预算吸收。

## 4. 移动 product cutoff 的 aperture budgets

令 \(X\le Z\le X^2\)，并把笔记 212 的 aperture family 改为

\[
 \mathcal A_\nu(Z)
 =\left\{(a,b):
 2\le a,b\le X,
 \operatorname{base}(a)\ne\operatorname{base}(b),
 ab\le Z,
 s_{a/b}\in I_\nu
 \right\}.
\tag{26}
\]

记

\[
 \mathscr M_\nu(Z)
 =\sum_{(a,b)\in\mathcal A_\nu(Z)}|b_ab_b|.
\tag{27}
\]

### 引理 215-D（moving-cutoff aperture mass）[T]

对 fixed aperture width，一致地有

\[
 \mathscr M_\nu(Z)\ll\sqrt Z,
 \qquad
 \sum_\nu\mathscr M_\nu(Z)\ll L\sqrt Z.
\tag{28}
\]

此外，distinct ratios 在同一 real aperture 内的 log-spacing 至少
\(c/Z\)。

#### 证明

沿用笔记 212-B 的 dyadic rectangles。fixed aperture 把 \(p-q\) 限制在
有限个整数中，而 \(ab\le Z\) 给 \(p+q\le\log_2Z+O(1)\)。每个 rectangle
的 \(\ell^1\) mass 至多 \(O(2^{(p+q)/2})\)；沿 radial direction 求几何和
得到 \(O(\sqrt Z)\)。ratio range 长度为 \(O(L)\)，故第二式成立。

若 \(a/b>c/d\) 且二者小于 factor \(2\)，则

\[
 \frac{a/b}{c/d}-1=\frac{ad-bc}{bc}\ge\frac1{bc}.
\]

由 \((ad)(bc)=abcd\le Z^2\) 与 \(ad/bc<2\) 得 \(bc\le Z\)。于是
mean-value theorem 给 log-gap \(\gg1/Z\)。\(\square\)

## 5. Ordinary supercritical collar

### 定理 215-E（ordinary main terms up to \(XL^\kappa\)）[T]

固定 \(0\le\kappa<1\) 与 fixed \(C_0>0\)。对式 (4) 中所有满足

\[
 a/b\ne c/d,\qquad
 |\log(a/b)-\log(c/d)|\le C_0
\tag{29}
\]

的 atom pairs，其 Toeplitz translated-symbol main terms 的绝对值总和为
\(o(N)\)。

#### 证明

置 \(Z=XL^\kappa\)。笔记 214-B 的 six-window identity 与 determinant
lift 对移动 cutoff 原封不动成立。由

\[
 (ad)(bc)=(ab)(cd)\le Z^2
\]

及 \(ad/bc\asymp_{C_0}1\)，有 \(ad,bc\le C_1Z\)。删除 cell restrictions
与 factorization restrictions 后，正 majorant 至多

\[
 C\beta_L^4L\,\mathfrak H_{C_1}(Z).
\tag{30}
\]

取 fixed \(\vartheta=1-\kappa>0\)。由定理 215-C、
\(\log Z\asymp L\) 与 \(\beta_L\asymp L^{-1}\)，式 (30) 至多

\[
 o_{\kappa}
 \left(L^{-3}ZL^{3+\vartheta}\right)
 =o\left(XL^{\kappa+\vartheta}\right)
 =o(XL)=o(N).
\tag{31}
\]

\(\square\)

这已经回答 214-J 在 logarithmic collar 内的 shifted-convolution 分类：仍是
\(\Lambda*\Lambda\) harmonic correlation；没有新卷积阶。

## 6. Alias、far pairs 与 finite transfer

### 引理 215-F（alias support gap does not require \(ab\le X\)）[T]

设仅有

\[
 2\le a,b,c,d\le X.
\tag{32}
\]

若

\[
 s-t=L-\epsilon,\qquad |\epsilon|<\log2,
\]

则仍有 \(s\ge0\)、\(t\le0\)，并且

\[
 \operatorname{dist}
 \bigl(\operatorname{supp}Q_t^{[s-t]},
       \operatorname{supp}Q_s\bigr)
 \ge\log b\ge\log2.
\tag{33}
\]

此外

\[
 |s-t|\le2L-2\log2,
\tag{34}
\]

所以足够窄的 \(\pm2L\) aperture seams 仍为空。

#### 证明

由式 (32)，每个 ratio log 位于
\([-L+\log2,L-\log2]\)。若 \(s<0\)，则
\(s-t<L-\log2\)，与假设矛盾；同理 \(t>0\) 不可能。笔记 213-C 的 interval
计算随后只使用 \(x_b\ge\log2\)，逐字给出式 (33)。式 (34) 由上述 ratio
range 直接得到。\(\square\)

### 引理 215-G（all nonordinary bulk remainders are negligible）[T]

对 \(Z=XL^\kappa\)、任意 fixed \(\kappa<1\)：

1. non-seam far-aperture Toeplitz crosses 的绝对和为
   \[
   O\left(\frac{Z\log L}{L^2}\right)=o(N);
   \tag{35}
   \]
2. ordinary 与 \(\pm L\) bounded-band aperture pairs 的 Toeplitz-product
   Hankel trace remainders 总和为
   \[
   O\left(\frac{Z(1+\log L)}{L^3}\right)=o(N);
   \tag{36}
   \]
3. \(\pm L\) alias symbol main terms 逐 atom 为零，\(\pm2L\) pairs 为空。

#### 证明

笔记 212-E 的单 block-pair bound 中以引理 215-D 的
\(\mathscr M_\nu(Z)\ll\sqrt Z\) 替换 \(\sqrt X\)。对
\(O(L\log L)\) 的 reciprocal aperture-distance budget 求和，得到式 (35)。

对 bounded-band graph（包括 self-loops）只有 \(O(L)\) 个 block pairs。
笔记 213-D 的单 atom-pair trace-class bound 与式 (28) 给式 (36)。alias
symbol main term 和 \(\pm2L\) 陈述由引理 215-F 给出。\(\square\)

### 引理 215-H（aggregate finite/bulk transfer in the collar）[T]

令

\[
 E_\kappa
 =\sum_{(a,b)\in\mathcal P_\kappa(X)}
 (F_{a/b}^{fin}-F_{a/b}^{bulk}).
\tag{37}
\]

则

\[
 \|E_\kappa\|_{HS}^2
 \ll\frac{Z(1+\log L)}{L^2}=o(N).
\tag{38}
\]

#### 证明

uniform Hankel bound 给单 atom defect norm 至多

\[
 C\beta_L^2\sqrt{1+\log L}\,|b_ab_b|.
\]

由引理 215-D，全部 apertures 的 coefficient mass 总和为
\(O(L\sqrt Z)\)。三角不等式平方后得到

\[
 \|E_\kappa\|_{HS}^2
 \ll
 \beta_L^4(1+\log L)L^2Z,
\]

即式 (38)。\(\square\)

## 7. Supercritical collar atomic diagonalization

### 定理 215-I（complete primitive collar diagonalization）[T]

对每个 fixed \(0\le\kappa<1\)，式 (5) 成立。

#### 证明

先在 bulk 模型中分解 distinct atom pairs。ordinary pairs 由定理 215-E 为
\(o(N)\)；far-aperture、alias 与 endpoint pairs 由引理 215-G 为
\(o(N)\)。所以全部 bulk off-diagonal contribution 为 \(o(N)\)。笔记
209-D 对完整 ratio family 给

\[
 \sum_\rho\|F_\rho^{bulk}\|_{HS}^2=O(N),
\]

故 collar bulk aggregate 的 norm square 为 \(O(N)\)。

引理 215-H 与
\(|\|B+E\|^2-\|B\|^2|\le2\|B\|\|E\|+\|E\|^2\) 给 aggregate
finite/bulk norm-square 差为 \(o(N)\)。最后，笔记 209-D 还给任意 ratio
subset 的 atomic finite/bulk diagonal sums 差为 \(o(N)\)。合并三项得到式
(5)。\(\square\)

这是真正的 supercritical 推进，但只覆盖 product cutoff 的 logarithmic collar；
它不等于完整 \(ab>X\) sector。

## 8. \(\kappa=1\) 的当前方法障碍

### 障碍定理 215-J（absolute-Evans collar ceiling）[N]

只使用以下两项：

1. 对每个 fixed \(\vartheta>0\)，
   \(\mathfrak H_C(Y)=o_\vartheta(Y(\log Y)^{3+\vartheta})\)；
2. ordinary response 的正 majorant
   \(C\beta_L^4L\mathfrak H_C(Z)\)，

不能逻辑推出 \(Z=XL\) 时该 majorant 为 \(o(N)\)。

#### 证明

抽象预算

\[
 H_*(Y)=Y(\log Y)^3
\tag{39}
\]

对每个 fixed \(\vartheta>0\) 都满足
\(H_*(Y)=o_\vartheta(Y(\log Y)^{3+\vartheta})\)。但当
\(Z=XL\)、\(\log Z\asymp L\) 时，

\[
 \beta_L^4L H_*(Z)
 \asymp L^{-3}\,ZL^3
 =Z=XL\asymp N,
\tag{40}
\]

不是 little-oh。因此这两项上界本身不蕴含临界 collar closure。
\(\square\)

该障碍不声称实际 arithmetic sum 达到式 (39)，也不声称
\(\kappa=1\) 的 diagonalization 为假。它严格排除的是：继续只调 Evans
参数并对 six-window kernel 取绝对值，就能自动越过 \(ab=XL\) 的推理。

特别地，完整超临界 sector 所需的新输入不是 \(\Lambda^{*3}\)，而是至少以下
之一：

- transition scale \(Y\asymp XL\) 上的
  \(o(Y(\log Y)^3)\) response-weighted shifted-correlation bound；
- 保留 \(e^{iT\log(m/n)}\) 与 six-window overlap 的 signed cancellation；
- 利用 factorization restrictions
  \(e(a,b)\)、\(e(c,d)\) 的 restricted \(E_2\) correlation，而不把它们
  全部删除成 \(\mathcal A(m)\mathcal A(n)\)；
- 与 adjacent/continuum/Gamma physical directions 的统一 Schur cancellation。

## 9. 修正后的下一最小引理 215-K [O]

固定小常数 \(\delta>0\)，只研究 transition product layer

\[
 XL^{1-\delta}\le ab,cd\le XL^{1+\delta},
 \qquad |\log(a/b)-\log(c/d)|\le C_0.
\tag{41}
\]

对 exact translated six-window kernel、finite Dirichlet factor与相位
\(e^{iT\log(ad/bc)}\) 定义 response-weighted determinant sum。证明以下二者
之一：

1. 它为 \(o(N)\)，并明确指出 saving 来自 weighted \(E_2\) correlation、
   factorization restriction 还是 physical phase；
2. 构造主尺度 lower-bound model，证明必须与 adjacent/continuum/Gamma
   channels 联合消去。

该引理有限、可证伪，并且正好位于定理 215-I 与障碍定理 215-J 的交界；不再
重复已经闭合的 \(\kappa<1\) collar。

## 10. 公理作用、删除审计与循环性

1. **product cutoff \(ab,cd\le Z\)**：通过
   \((ad)(bc)\le Z^2\) 把 determinant scale 限制在 \(O(Z)\)。删除后式
   (30) 没有单一 arithmetic scale。
2. **product-excess/ratio coordinates**：给式 (14)，识别 scale inflation；
   它本身不提供 cancellation。
3. **von Mangoldt support**：给式 (16) 的 \(\Lambda*\Lambda\) collapse。
   删除后一般 coefficient family 需要新的 divisor correlation。
4. **Evans almost-all theorem**：给式 (2) 中几乎一个完整 logarithm 的 saving；
   exceptional shifts 仍由独立 second moment 控制。
5. **compact response window**：给 exact support、alias gap 与 uniform Hankel
   regularity；不负责二素数相关。
6. **finite/bulk direct-sum estimate**：只转移 atomic diagonals。aggregate
   transfer 另外由引理 215-H 证明，没有把 direct-sum 小量误当成 coherent sum
   小量。

删除审计：

- 删除 Evans 输入后，ordinary determinant majorant 回到
  \(O(ZL)\)，即使 \(Z=X\) 也停在主尺度。
- 删除 moving-cutoff mass budget 后，逐 atom Hankel remainder 不能对整个
  collar 求和。
- 删除 alias 的 translated symbol，\(\pm L\) Dirichlet resonance 会被错误地
  计成主项。
- 把定理 215-J 错读为 arithmetic lower bound 会过度声称；它只是当前正
  majorant 与已证上界之间的严格逻辑障碍。

循环性审计：全部输入位于 prime side。没有假设 RH/GRH、零点在中心线、Weil
二次型完全正、酉谱算子或一致有界负指数。式 (5) 仍只是部分四矩 response
Gram 的一个 sector，不推出新的零点比例。

## 11. 模型范围与部分 Weil 接口

- **Riemann zeta**：定理 215-I 直接扩大当前 primitive alternating sector。
- **本原 Dirichlet \(L\)**：绝对 majorant 不受 unit character phases 影响；
  signed transition lemma 215-K 必须重新保留角色相位。
- **Dedekind/automorphic \(L\)**：式 (16) 通常替换为 coefficient convolution；
  需要相应 almost-all shifted-correlation theorem。
- **函数域**：product excess 变成 degree excess，式 (14) 有离散 analogue；
  可检验 transition layer 是否由有限域大筛闭合。
- **无 Euler product 的负向模型**：卷积 collapse 失效，说明本轮不是函数方程
  或 RH 的同义改写。

在部分 Weil 配置中，定理 215-I 提供更大的 prime-side finite Gram
diagonalization 区域；障碍定理 215-J 则把尚缺输入定位为 transition-scale 的
response-weighted additive correlation，而不是“假设完整 Weil 正性”。
