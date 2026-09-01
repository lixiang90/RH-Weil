# 209. Alternating ratio multiplicity collapse 与 square-root determinant core

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 NCE-8 / Vaughan square-root rectangle

状态：alternating Toeplitz--Hankel 公式、von Mangoldt ratio-cluster 分类、
非中心同素数链消失、ratio direct-sum finite transfer、sub-square-root primitive
family 渐近对角化与 odd determinant parity gap 为 [T]；global cross-box determinant
layer response estimate 和 dyadic exceptional family aggregate 为 [O]；有限分类与
矩阵检查为 [E]。

> **后续修正（笔记 210）**：定理 209-A--F 的已证陈述保持成立，但本笔记把
> 单个 dyadic box 的 symbol energy 粗估为全区间 `O(L^4)`，因而误把
> `Y asymp sqrt(X)` 解释为 within-box hard threshold。笔记 210 恢复局部
> von Mangoldt 能量后，把闭合范围推进到 `Y <= sqrt(X)L^(1-delta)`，并闭合
> `h=+/-2` within-box layer。当前开放核心是跨 radial boxes 的 coherence 及
> `AB` 接近或超过 `XL^2` 的局部区域。

## 1. 本轮结论

笔记 201 把 alternating 四矩词按 reduced ratio \(\rho=a/b\) 聚类，并指出
一般 Farey fractions 的最小间距可达 \(X^{-2}\)。但实际系数不是任意 Farey
系数：\(\Lambda(a)\Lambda(b)\ne0\) 强制 \(a,b\) 为 prime powers。

本轮证明实际 ratio family 具有以下刚性。

1. 若 \(a=p^i,b=q^j\) 且 \(p\ne q\)，则 reduced ratio
   \(p^i/q^j\) 的 cluster **恰有一个 atom**。不存在增长的 common-multiple
   fibre。
2. 所有 multiplicity 大于一的非中心 clusters 都是同一素数底的 chains
   \(p^r\) 或 \(p^{-r}\)。这些非中心 chains 的整个 finite aggregate 满足

   \[
    \left\|G_{\mathrm{chain}}\right\|_{HS}^2
    \ll\beta_L^4d=o(N).
   \tag{1}
   \]

3. 中心 ratio \(\rho=1\) 是唯一不能删除的重复 cluster：

   \[
    F_1=\sum_n b_n^2R_nR_n^*.
   \tag{2}
   \]

   它是单个 PSD main block，应保留在 alternating diagonal，而不能混入
   generic Farey multiplicity。
4. alternating finite-to-bulk ratio defects 的 Hilbert direct-sum 预算仍为

   \[
    \sum_\rho\|F_\rho^{fin}-F_\rho^{bulk}\|_{HS}^2
    \ll1+\log L.
   \tag{3}
   \]

5. 对任意 fixed \(\delta>0\)，若 primitive ratios 的 numerator/denominator
   都落在 \([Y,2Y]\) 且

   \[
    Y\le X^{1/2-\delta},
   \]

   则整个真实 finite ratio family 渐近对角化：

   \[
    \boxed{
    \left\|\sum_{\rho\in\mathcal R_Y}F_\rho^{fin}\right\|_{HS}^2
    =\sum_{\rho\in\mathcal R_Y}\|F_\rho^{fin}\|_{HS}^2+o(N).}
   \tag{4}
   \]

6. 在临界 \(Y\asymp\sqrt X\) box 中，若把局部 symbol energy 粗估成全区间
   预算，则 ordinary Montgomery--Vaughan error 看似变成主尺度；笔记 210 证明该判断
   不 sharp。若排除 base \(2\)，任意两个不同
   primitive prime-power ratios 的 determinant

   \[
    a d-b c
   \]

   是非零偶数，故绝对值至少为 \(2\)。这给一个真实 parity gain，但只改善
   critical spacing 的常数，不能单独产生 little-oh。

因此 alternating/Farey 的开放输入不再是“全部长度 \(X^2\) 的任意 ratio
coefficients”，而被严格缩成：

- 跨越不同 radial boxes 的 primitive ratio coherence；
- 中心 block 与 primitive hard core 的 cross response；
- 至少一个 base 为 \(2\) 的稀疏 exceptional family；
- \(AB\gtrsim XL^2\) 局部区域及 actual Vaughan/continuum/Gamma 方向的 Schur cancellation。

## 2. Exact alternating Toeplitz--Hankel response

沿用笔记 204：

\[
 R_T(x)=\beta_Le^{iTx}T_d(q_x)D_d(x),
 \qquad q_x(u)=\phi(u)\phi(x-u).
\tag{5}
\]

对 \(s=x-y\) 定义周期平移

\[
 q_y^{(s)}(u)=q_y(u-s\pmod L).
\tag{6}
\]

### 定理 209-A（exact alternating response）[T]

\[
 \boxed{
 R_T(x)R_T(y)^*
 =\beta_L^2e^{iTs}
 \left[T_d(q_xq_y^{(s)})
 -\mathcal H_d(q_x,q_y^{(s)})\right]D_d(s).}
\tag{7}
\]

#### 证明

因 \(q_y\) 实，\(T_d(q_y)^*=T_d(q_y)\)，故

\[
 R_T(y)^*=\beta_Le^{-iTy}D_d(-y)T_d(q_y).
\]

所以

\[
 R_T(x)R_T(y)^*
 =\beta_L^2e^{iTs}T_d(q_x)D_d(s)T_d(q_y).
\]

利用

\[
 D_d(s)T_d(q_y)=T_d(q_y^{(s)})D_d(s)
\]

以及笔记 204 的 exact finite-section product

\[
 T_d(f)T_d(g)=T_d(fg)-\mathcal H_d(f,g),
\]

得到式 (7)。\(\square\)

对 reduced positive rational \(\rho\)，置 \(s_\rho=\log\rho\)，并定义

\[
 F_\rho^{fin}
 =\sum_{a/b=\rho}b_ab_bR_T(x_a)R_T(x_b)^*,
\tag{8}
\]

\[
 Q_\rho(u)
 =\sum_{a/b=\rho}b_ab_b
 q_{x_a}(u)q_{x_b}^{(s_\rho)}(u),
\tag{9}
\]

\[
 F_\rho^{bulk}
 =\beta_L^2e^{iTs_\rho}T_d(Q_\rho)D_d(s_\rho).
\tag{10}
\]

式 (7) 给出 exact defect

\[
 E_\rho:=F_\rho^{fin}-F_\rho^{bulk}
 =-\beta_L^2e^{iTs_\rho}
 \sum_{a/b=\rho}b_ab_b
 \mathcal H_d(q_{x_a},q_{x_b}^{(s_\rho)})D_d(s_\rho).
\tag{11}
\]

与 adjacent 情形不同，式 (9) 的 support 不强制 \(ab\le X\)；ratio length
问题是真实的，不是周期 alias。

## 3. Von Mangoldt ratio multiplicity classification

### 定理 209-B（prime-power ratio multiplicity collapse）[T]

设 \(\Lambda(a)\Lambda(b)\ne0\)。

1. 若 \(a=p^i,b=q^j\)、\(p\ne q\)，则 cluster

   \[
    \{(c,d):\Lambda(c)\Lambda(d)\ne0,\ c/d=a/b\}
   \]

   只含 \((a,b)\)。
2. 若一个非中心 ratio cluster 含多个 pairs，则存在唯一 prime \(p\) 与
   \(r\ne0\)，使 ratio 为 \(p^r\)，所有 pairs 都是

   \[
    (p^{j+r},p^j)\quad(r>0)
   \]

   或其逆序。
3. ratio \(1\) 的 cluster 恰为 \((n,n)\)，其中 \(n\) 遍历全部 prime
   powers。

#### 证明

若 \(p\ne q\)，则 \(p^i/q^j\) 已既约。任何同 ratio pair 必写成

\[
 (c,d)=(kp^i,kq^j),\qquad k\in\mathbb N.
\]

因为 \(c\) 是 prime power 且被 \(p\) 整除，若 \(k>1\)，则 \(k\) 只能含
prime \(p\)。但此时 \(d=kq^j\) 同时含 \(p,q\) 两个 prime bases，不是
prime power，矛盾。所以 \(k=1\)。

若 \(p=q\)，ratio 为 \(p^{i-j}\)，得到同素数链。ratio 为 \(1\) 时
\(a=b\)，反之显然。\(\square\)

该定理删除了一般 Farey synthesis 中的 arbitrary common-multiple fibres；
实际 hard family 的 primitive clusters 是 rank one in arithmetic label。

## 4. Noncentral same-prime chains are negligible

令

\[
 G_{chain}^{fin}
 =\sum_p\sum_{i\ne j}
 b_{p^i}b_{p^j}R_T(i\log p)R_T(j\log p)^*.
\tag{12}
\]

### 定理 209-C（noncentral chain aggregate evacuation）[T]

\[
 \boxed{
 \|G_{chain}^{fin}\|_{HS}^2
 \ll\beta_L^4d=O(N/L^4)=o(N).}
\tag{13}
\]

#### 证明

由 \(0\le q_x\le1\)，

\[
 \|R_T(x)\|_{op}\le\beta_L,
 \qquad
 \|R_T(x)\|_{HS}\le\beta_L\sqrt d.
\]

所以

\[
 \|R_T(x)R_T(y)^*\|_{HS}\le\beta_L^2\sqrt d.
\tag{14}
\]

另一方面，略去固定 \((2\pi)^{-2}\) 后，所有非中心 chain coefficients 的
\(\ell^1\) 和由

\[
 \begin{aligned}
 \sum_p(\log p)^2
 \sum_{i\ne j}p^{-(i+j)/2}
 &\ll
 \sum_p\frac{(\log p)^2}{p^{3/2}}<\infty
 \end{aligned}
\tag{15}
\]

控制。对式 (12) 使用三角不等式和式 (14)，得到
\(\|G_{chain}^{fin}\|_{HS}\ll\beta_L^2\sqrt d\)。平方即为式
(13)。\(\square\)

中心 ratio \(1\) 不满足式 (15)，因为它包含 \(i=j=1\) 的全部 primes；故
式 (2) 必须保留。这正是删除公理后的失效位置。

## 5. Alternating direct-sum finite transfer

### 定理 209-D（ratio-cluster direct-sum transfer）[T]

在笔记 204 的窗口正则性下，

\[
 \boxed{
 \sum_\rho\|E_\rho\|_{HS}^2\ll1+\log L.}
\tag{16}
\]

同时

\[
 \sum_\rho\|F_\rho^{bulk}\|_{HS}^2=O(N).
\tag{17}
\]

因此任意 ratio subset 的 finite/bulk diagonal sums 相差 \(o(N)\)。

#### 证明

笔记 204 的 uniform Hankel bound 给每个 ordered pair

\[
 \|\mathcal H_d(q_{x_a},q_{x_b}^{(s)})\|_{HS}^2
 \ll1+\log L.
\tag{18}
\]

对不同 prime bases，定理 209-B 说明每个 cluster 只有一个 pair，所以其
direct-sum contribution 至多

\[
 \beta_L^4(1+\log L)
 \left(\sum_{n\le X}|b_n|^2\right)^2
 \ll1+\log L.
\tag{19}
\]

对中心 cluster，三角不等式给

\[
 \|E_1\|_{HS}
 \ll\beta_L^2\sqrt{1+\log L}\sum_n b_n^2
 \ll\sqrt{1+\log L}.
\tag{20}
\]

对非中心 chains，式 (15) 给更小的
\(O(\beta_L^4(1+\log L))\) direct-sum contribution。合并得到式
(16)。

primitive bulk clusters 为 singleton，故其 diagonal energy 由

\[
 \beta_L^4d\left(\sum_n b_n^2\right)^2=O(d)=O(N)
\]

控制。中心 symbol 的 \(L^\infty\) norm 至多 \(\sum_n b_n^2=O(L^2)\)，
所以中心能量同样为 \(O(\beta_L^4dL^4)=O(N)\)。chains 用式
(15) 控制。得到式 (17)。最后如笔记 204，在 ratio Hilbert 直和中应用
\(|\|u\|^2-\|v\|^2|\le\|u-v\|(\|u\|+\|v\|)\)。\(\square\)

式 (16) 仍不是 family aggregate bound；定理 205-G 型 coherence no-go 仍提醒
我们不能从 direct sum 自动得到 \(\|\sum_\rho E_\rho\|\)。

## 6. Exact diagonal fibres and sub-square-root closure

对 bulk cluster，逐 entries 有

\[
 (F_\rho^{bulk})_{jk}
 =\beta_L^2\widehat Q_\rho(j-k)
 e^{i(T+kh)s_\rho}.
\tag{21}
\]

因此笔记 205 的 diagonal-fibre identity 原封不动变为

\[
 \left\|\sum_{\rho\in\mathcal R}F_\rho^{bulk}\right\|_{HS}^2
 =\beta_L^4\sum_{|r|<d}\sum_{k\in I_r}
 \left|\sum_{\rho\in\mathcal R}
 \widehat Q_\rho(r)e^{i(T+kh)s_\rho}\right|^2.
\tag{22}
\]

固定 \(Y\ge2\)，令 \(\mathcal R_Y\) 为所有 primitive distinct-base ratios
\(a/b\)，其中

\[
 Y\le a,b\le2Y.
\tag{23}
\]

### 定理 209-E（sub-square-root primitive ratio diagonalization）[T]

设 \(T\asymp X\)、\(N\asymp XL\)。对任意 fixed \(\delta>0\)，若

\[
 Y\le X^{1/2-\delta},
\tag{24}
\]

则式 (4) 成立。

#### 证明

若 \(a/b\ne c/d\) 且四个整数满足式 (23)，则

\[
 \left|\frac ab-\frac cd\right|
 =\frac{|ad-bc|}{bd}\ge\frac1{4Y^2}.
\]

所有 ratios 落在 \([1/2,2]\)，所以 logarithm 在该 compact interval 上
bi-Lipschitz。因而 frequencies

\[
 \frac{s_\rho}{L}\pmod1
\]

的圆周间距满足

\[
 \Delta\gg\frac1{LY^2}.
\tag{25}
\]

primitive clusters 为 singleton，Parseval 与 \(|q_xq_y^{(s)}|\le1\) 给

\[
 \mathcal S_Y
 :=\sum_{\rho\in\mathcal R_Y}\sum_r
 |\widehat Q_\rho(r)|^2
 \le\sum_{a,b}|b_a|^2|b_b|^2
 \ll L^4.
\tag{26}
\]

在式 (22) 每条 diagonal 上应用 Montgomery--Vaughan 圆周 mean square，
得到

\[
 \left|
 \left\|\sum_{\rho\in\mathcal R_Y}F_\rho^{bulk}\right\|_{HS}^2
 -\sum_{\rho\in\mathcal R_Y}\|F_\rho^{bulk}\|_{HS}^2
 \right|
 \ll\beta_L^4LY^2\mathcal S_Y
 \ll LY^2=o(N).
\tag{27}
\]

最后 \(\#\mathcal R_Y\le Y^2\)。由式 (16) 和 Cauchy，

\[
 \left\|\sum_{\rho\in\mathcal R_Y}E_\rho\right\|_{HS}^2
 \le Y^2\sum_\rho\|E_\rho\|_{HS}^2
 \ll Y^2\log L=o(N).
\tag{28}
\]

式 (16)--(17) 也给 finite/bulk diagonal sums 相差 \(o(N)\)。结合式
(27)--(28) 得式 (4)。\(\square\)

本节使用全区间 symbol budget，因此只得到较弱阈值；笔记 210 用局部预算证明普通 Farey large sieve 在 \(Y\asymp\sqrt X\) 仍为 little-oh。
本定理的 sub-square-root 结论仍正确，但不是 sharp boundary。

## 7. Odd primitive determinant parity

### 定理 209-F（odd-ratio determinant gap）[T]

设

\[
 \rho=\frac{p^i}{q^j},\qquad
 \sigma=\frac{r^k}{s^\ell}
\]

是不同 primitive ratios，且 \(p,q,r,s\) 都是 odd primes。则

\[
 \boxed{
 |p^is^\ell-q^jr^k|\ge2,
 \qquad p^is^\ell-q^jr^k\equiv0\pmod2.}
\tag{29}
\]

#### 证明

两个 products 都是 odd integers，所以其差为偶数。ratios 不同使差非零，
故绝对值至少 \(2\)。\(\square\)

在 square-root box 中，式 (29) 把 ordinary Farey determinant lower bound
从 \(1\) 提高到 \(2\)。parity alone 只能改进常数；真正使单-box remainder
成为 little-oh 的是笔记 210 的 local von Mangoldt energy。

若至少一个 prime base 为 \(2\)，parity argument 失效。该 dyadic exceptional
family 的 **diagonal square mass** 比全 family 少 \(L^{-2}\) 量级，因为

\[
 \sum_{i\ge1}b_{2^i}^2=O(1),
 \qquad \sum_n b_n^2=O(L^2).
\]

但在获得 family-frame bound 前，不能把较小 diagonal mass 自动升级为 aggregate
negligibility；它保留为单独 [O]。

## 8. Global/cross-box hard input（由笔记 210 修正）

对同一或跨 radial boxes 的 primitive ratios，近碰撞由 determinant layers

\[
 h=ad-bc\in\mathbb Z\setminus\{0\}
\tag{30}
\]

参数化。odd hard core 只含

\[
 h\in2\mathbb Z\setminus\{0\}.
\]

### 开放引理 209-G（global cross-box determinant-layer Schur bound）[O]

在跨越多个 radial prime-power boxes 或 \(AB\gtrsim XL^2\) 的局部区域中，对实际 Toeplitz fibres
\(\widehat Q_{a/b}(r)\) 和 Vaughan channel vector，证明一个一侧预算

\[
 G_{hard}\preceq(1+\varepsilon)D_{hard}+M,
 \qquad x^*Mx\le\eta N,
\tag{31}
\]

其中 \(\varepsilon,\eta\) 满足完整四矩余项阈值。估计必须：

1. 按 even determinant layers \(h=\pm2,\pm4,\ldots\) 保留符号；
2. 保留 actual rank-one primitive atoms，而非任意 Farey coefficients；
3. 联合 Type I/Type II 与 continuum/Gamma cross terms；
4. 单独处理 ratio \(1\) 和 dyadic exceptional family；
5. 使用 Fejer/Gram-positive localization，不能硬截断 off-diagonal 后声称 PSD。

笔记 210-G 已闭合同一 dyadic box 内的 \(h=\pm2\) layer。新的第一步是对相隔至少两个 dyadic radial scales 的一对 boxes 写出 exact cross response Gram，并证明其
Schur contribution 严格小于 ordinary absolute-value bound。该引理是有限、可证伪
的 cross-box 下一目标。

## 9. 公理作用、删除审计与适用范围

1. **von Mangoldt prime-power support**：负责定理 209-B 和式 (15)。删除后
   common-multiple ratio fibres 可任意增长，multiplicity collapse 失效。
2. **Toeplitz covariance**：负责式 (21)--(22)。删除后 scalar ratio large
   sieve 不能逐 matrix diagonal 应用。
3. **uniform Hankel regularity**：只负责式 (16) 的 finite transfer，不控制
   ratio family aggregate。
4. **全区间 symbol budget 与 sub-square-root scale**：负责本笔记式 (27) 的较弱 little-oh。删除式
   (24) 后，本笔记的粗预算失效；但笔记 210 表明局部预算仍可闭合到 \(Y\le\sqrt X L^{1-\delta}\)。
5. **odd prime bases**：只负责 determinant parity factor \(2\)。删除后仍有
   ordinary determinant lower bound \(1\)，但 dyadic family 必须分开。
6. **response-specific Schur input**：当前 [O]，没有被伪装成 Weil positivity
   或 uniform negative-index axiom。

模型范围：

- Riemann zeta 满足全部 [T] 输入。
- 固定本原 Dirichlet \(L\) 函数的角色相位不改变 multiplicity、direct-sum
  absolute budget 或 determinant parity；hard Schur cross phase 必须重新保留。
- Dedekind/automorphic coefficients 通常不再只支撑于单 prime powers；定理
  209-B 不能自动推广，需要 local Satake support multiplicity 分类。
- 函数域 Euler factors 的 degree 有界，ratio fibres 可按 Frobenius eigenvalue
  labels 精确分类；这提供一个检验 cohomological grading 是否对应 explicit
  ratio multiplicity 的正向模型，但不自动证明两类 Weil 结构等价。

## 10. RH/GRH 循环性与结论边界

- 本笔记原先没有证明 square-root hard Schur bound；其 within-box 版本后由笔记 210 闭合，但 global alternating 四矩仍未闭合。
- 没有改善简单零点或不同零点比例。
- 定理 209-E 本身只陈述 sub-square-root primitive boxes；更强的局部外推见笔记 210，但仍不能把单-box 结论外推为
  跨 radial boxes 的整体结论。
- parity factor \(2\) 是精确整数事实，不是渐近 cancellation。
- 中心 ratio \(1\) 和 dyadic exceptional aggregate 仍开放；较小 diagonal
  mass 不等于较小 family aggregate。
- \(13/18\) 与 \(16/21\) 仍只在相应四矩假设下成立。

## 11. 可复现审计 [E]

脚本 `scripts/alternating_ratio_cluster_audit.py` 检查：

1. 式 (7) 的 finite alternating Toeplitz--Hankel identity；
2. 所有 prime powers \(\le300\) 的 ratio multiplicity classification；
3. 非中心 same-prime \(\ell^1\) coefficient budget 的收敛趋势；
4. odd prime ratios 在三个 square-root boxes 中的 adjacent determinants 均为
   非零偶数，最小值为 \(2\)。

有限输出中，noncentral chain coefficient sums 在
\(X=10^3,10^4,10^5\) 时为

\[
 6.59678,\quad8.41756,\quad9.71244,
\]

增量递减；odd ratio boxes 的最小 determinant 均为 \(2\)。这些数据只审计
分类、索引和有限收敛，不证明式 (31) 或任何零点结论。
