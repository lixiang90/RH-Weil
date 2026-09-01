# 211. Radial cross-box coherence：pairwise no-go 与窗口局部性障碍

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 NCE-8 / multiscale Vaughan response Gram

状态：单-box 定量范数、固定 pair 自动闭合、pairwise-to-union sharp no-go、
alternating symbol 的径向因子化、admissible plateau window 的径向不衰减、
cross-scale determinant degree 基线与 multibox Schur 充分条件为 [T]/[N]；有限
审计为 [E]；actual prime-power radial Gram 的算术行和衰减为 [O]。
> **后续修正（笔记 212）**：绝对 row-sum 条件 211-I 是充分但过强的。
> 在 `ab<=X` 的双曲区域，fixed real aperture 把 symbol energy 降为 `O(L^3)`，
> signed Montgomery--Vaughan bound 已直接给整条 radial chain `O(N/L)`。
> 当前缺口进一步压缩为普通 aperture 邻接与 `+/-L,+/-2L` circular alias
> seams 上的 `O(L)`-edge actual response Gram。

## 1. 本轮结论

笔记 210 把下一目标写成“一对相隔 radial boxes 的 cross term 为 \(o(N)\)”。
该目标是正确的，但不足以作为下一算术引理，因为它已经由单-box 范数和 Cauchy
自动推出。

本轮证明：

1. 对 \(AB\le X\) 的任一 primitive box aggregate \(G_{A,B}\)，

   \[
    \|G_{A,B}\|_{HS}^2\ll N/L^2.
   \tag{1}
   \]

   所以任意固定一对 boxes 的 cross term 都是 \(O(N/L^2)=o(N)\)。
2. 但约 \(J\asymp L\) 个 vectors 可各有平方范数 \(N/L^2\)，每一对内积也是
   \(o(N)\)，同时总和的平方范数仍为 \(\asymp N\)。因此“逐 pair
   little-oh”不能闭合 radial union。
3. 对同一 ratio \(s=x_a-x_b\)，alternating bulk symbol 精确因子化为

   \[
    Q_{a/b}(u)
    =b_ab_b\phi(u)\phi(u-s)\phi(x_a-u)^2.
   \tag{2}
   \]

   radial scale 只进入最后一个 endpoint factor。
4. 笔记 204 的窗口公理允许具有长 plateau 的标准 smooth cutoffs。对这种窗口，
   \(J\asymp L\) 个 radial symbol shapes 的两两 normalized correlation 一致
   有正下界，故 normalized Gram row sum 为 \(\Theta(L)\)。所以窗口正则性本身
   不可能给所需的 \(o(L)\) 行和。
5. 对 radial scale ratio \(\lambda=D/B\asymp C/A\ge1\)，固定 determinant
   layer 的度数 Schur 基线为 \(O(\sqrt\lambda)\)，而且抽象星图达到该阶。
   因此 maximum-degree 数据也不产生 radial decay。

剩余输入被严格定位为：actual prime-power determinant incidence、Gabor phase、
Type I/II/continuum cross response 中至少一项必须提供超出窗口与度数基线的
**multibox arithmetic cancellation**。

## 2. 单-box 定量范数与 fixed-pair 自动闭合

记

\[
 G_{A,B}^{fin}
 =\sum_{\rho\in\mathcal R_{A,B}}F_\rho^{fin}.
\tag{3}
\]

### 定理 211-A（quantitative local-box norm）[T]

在笔记 210 的假设下，

\[
 \boxed{
 \|G_{A,B}^{fin}\|_{HS}^2
 \ll
 \frac{N}{L^2}+\frac{AB}{L}
 +\frac{AB(1+\log L)}{L^4}.}
\tag{4}
\]

特别地，若 \(AB\le X\)，则式 (1) 成立；若固定 \(\varepsilon>0\) 且
\(AB\le XL^{2-\varepsilon}\)，则

\[
 \|G_{A,B}^{fin}\|_{HS}^2
 \ll N(L^{-2}+L^{-\varepsilon})=o(N).
\tag{4a}
\]

#### 证明

笔记 210-(18)--(19) 分别给 bulk off-diagonal remainder 与 diagonal：

\[
 \left|\|G_{A,B}^{bulk}\|_{HS}^2
 -\sum_\rho\|F_\rho^{bulk}\|_{HS}^2\right|
 \ll AB/L,
\]

\[
 \sum_\rho\|F_\rho^{bulk}\|_{HS}^2\ll N/L^2.
\]

笔记 210-(20) 又给

\[
 \|G_{A,B}^{fin}-G_{A,B}^{bulk}\|_{HS}^2
 \ll AB(1+\log L)/L^4.
\]

使用 \(\|u+v\|^2\le2\|u\|^2+2\|v\|^2\) 得式 (4)。当
\(AB\le X\) 时，\(AB/L\le X/L=N/L^2\)，最后一项更小。
\(\square\)

### 推论 211-B（fixed-pair cross term is automatic）[T]

若某个 fixed \(\varepsilon>0\) 下
\(AB,CD\le XL^{2-\varepsilon}\)，则 cross term 为 \(o(N)\)。在较自然的
\(AB,CD\le X\) 范围内，还有定量界

\[
 \boxed{
 |\langle G_{A,B}^{fin},G_{C,D}^{fin}\rangle_{HS}|
 \ll N/L^2=o(N).}
\tag{5}
\]

#### 证明

对定理 211-A 及式 (4a) 应用 Cauchy--Schwarz。\(\square\)

因此笔记 210-H 的“单对 boxes”版本已经闭合；它没有使用 determinant
equidistribution，也没有缩小完整 multibox 缺口。

## 3. Pairwise little-oh 不推出 radial union

### 障碍定理 211-C（pairwise-to-union sharp no-go）[N]

令 \(J=\lfloor L\rfloor\)。存在 Hilbert-space vectors
\(v_1,\ldots,v_J\)，使

\[
 \|v_j\|^2=N/L^2,
 \qquad
 |\langle v_j,v_k\rangle|=N/L^2=o(N)
\tag{6}
\]

对所有 \(j,k\) 成立，但

\[
 \left\|\sum_{j=1}^Jv_j\right\|^2
 \sim N.
\tag{7}
\]

#### 证明

取一个单位向量 \(e\)，并令

\[
 v_j=\frac{\sqrt N}{L}e.
\]

则式 (6) 显然，而

\[
 \left\|\sum_{j=1}^Jv_j\right\|^2
 =\frac{J^2N}{L^2}\sim N.
\]

\(\square\)

这个反例不声称实际 prime boxes 完全相同；它严格证明任何只记录单-box 范数与
“每个 fixed pair 是 \(o(N)\)”的论证都不足以推出整体结论。

## 4. Exact radial factorization

设 \(x=x_a\)、\(y=x_b\)、\(s=x-y\)。由

\[
 q_x(u)=\phi(u)\phi(x-u),
\]

以及圆周平移在非零支撑上的零延拓表达，

\[
 \begin{aligned}
 q_y^{(s)}(u)
 &=q_y(u-s)\\
 &=\phi(u-s)\phi(y-u+s)\\
 &=\phi(u-s)\phi(x-u).
 \end{aligned}
\tag{8}
\]

### 定理 211-D（alternating radial symbol identity）[T]

对 singleton ratio \(a/b\)，

\[
 \boxed{
 Q_{a/b}(u)
 =b_ab_b\phi(u)\phi(u-s)\phi(x_a-u)^2}
\tag{9}
\]

几乎处处成立。

#### 证明

把式 (8) 代入
\(Q_{a/b}=b_ab_bq_{x_a}q_{x_b}^{(s)}\) 即得。周期端点上的可能差异是
零测集；零延拓没有增加 alias support。\(\square\)

式 (9) 很重要：ratio aperture 控制 \(s\)，而 radial numerator scale 只平移
最后一个 cutoff。它也说明为什么不能仅从不同 integers 的标签推出 symbol
正交。

## 5. Window-only radial decay no-go

考虑笔记 204 允许的标准 plateau windows：\(0\le\phi_L\le1\)，支撑于
\([-L/2,L/2]\)，在

\[
 [-L/2+1,L/2-1]
\]

上等于 \(1\)，并在两个固定宽度 endpoint layers 内光滑过渡。它满足
\(a_L\ge a_0\) 及一致的
\(\|\phi'\|_1+\|\phi'\|_2+\|\phi''\|_1=O(1)\)。

固定 bounded \(s\)，定义去掉算术 scalar 的 shape

\[
 P_{s,x}(u)=\phi_L(u)\phi_L(u-s)\phi_L(x-u)^2.
\tag{10}
\]

### 障碍定理 211-E（admissible windows can have linear radial coherence）[N]

取

\[
 x_j\in[L/4,L/2],
 \qquad x_{j+1}-x_j=\log2.
\]

则有 \(J\asymp L\) 个 shapes，且存在与 \(L,j,k\) 无关的 \(c>0\)，使

\[
 \frac{|\langle P_{s,x_j},P_{s,x_k}\rangle_{L^2(du/L)}|}
 {\|P_{s,x_j}\|_2\|P_{s,x_k}\|_2}
 \ge c
\tag{11}
\]

对所有 \(j,k\) 成立。因此 normalized radial Gram 的每个 row sum 为
\(\Theta(L)\)。

#### 证明

除总长度 \(O(1)\) 的 endpoint layers 外，\(P_{s,x}\) 是区间

\[
 [x-L/2,L/2]
\]

的 indicator。故一致地有

\[
 \|P_{s,x}\|_2^2=1-x/L+O(1/L).
\tag{12}
\]

若 \(x_j\le x_k\)，两个 intervals 嵌套，因而

\[
 \langle P_{s,x_j},P_{s,x_k}\rangle
 =1-x_k/L+O(1/L).
\tag{13}
\]

在 \(x_j,x_k\in[L/4,L/2]\) 上，式 (12)--(13) 的 normalized ratio 具有
绝对正下界，例如任取小于 \(\sqrt{2/3}\) 的固定常数在充分大 \(L\) 后均可。
又 \(J\asymp L\)，故 row sum 为 \(\Theta(L)\)。\(\square\)

删除窗口之外的 arithmetic phases 后，式 (11) 达到障碍定理 211-C 的 coherence
方向。因此笔记 204 的窗口公理本身不能推出 multibox Schur row sum 为
\(o(L)\)。这不排除实际 prime ratios 的相位和 determinant incidence 提供所需
衰减。

## 6. Cross-scale determinant degree is not decay

令 source box 为 \(\mathcal R_{A,B}\)，target box 为
\(\mathcal R_{C,D}\)，并固定 \(h\ne0\)。定义 bipartite edges

\[
 ad-bc=h.
\tag{14}
\]

### 定理 211-F（cross-scale determinant degree bound）[T]

该 incidence matrix 的最大 row sum 与 column sum 分别至多

\[
 2+D/B,
 \qquad 2+B/D.
\tag{15}
\]

故其 \(\ell^2\) operator norm 至多

\[
 \boxed{
 \sqrt{(2+D/B)(2+B/D)}.}
\tag{16}
\]

若 \(D/B\asymp C/A=\lambda\ge1\)，该基线为 \(O(\sqrt\lambda)\)。

#### 证明

固定 \(a/b\) 后，\(d\) 位于模 \(b\) 的唯一剩余类；长度为 \(D\) 的 target
denominator interval 至多含 \(2+D/B\) 个候选。每个 \(d\) 唯一决定 \(c\)。
固定 \(c/d\) 并交换角色得到 column bound。Schur test 给式 (16)。
\(\square\)

### 障碍定理 211-G（degree-only Schur bound is sharp）[N]

对每个整数 \(\lambda\ge1\)，存在 row degree \(\lambda\)、column degree \(1\)
的 bipartite incidence matrix，其 operator norm 恰为 \(\sqrt\lambda\)。

#### 证明

取若干互不相交的 \(\lambda\)-leaf stars。每个 row 的平方范数为 \(\lambda\)，
不同 rows 正交，所以最大奇异值为 \(\sqrt\lambda\)。\(\square\)

因此 fixed determinant 的 congruence degree 信息本身不仅没有 radial decay，反而
允许 \(\sqrt\lambda\) 损失。任何改善必须使用 prime-power sparsity、权重或
oscillatory phases，而不能只重复 maximum-degree Schur test。

## 7. 正确的 multibox 充分条件

固定一个 ratio aperture，并令 \(G_1,\ldots,G_J\) 是其中满足
\(A_jB_j\le X\) 的 disjoint radial box aggregates；\(J\ll L\)。若
\(G_j\ne0\)，定义 actual normalized coherence

\[
 \gamma_{jk}
 =\frac{|\langle G_j,G_k\rangle_{HS}|}
 {\|G_j\|_{HS}\|G_k\|_{HS}},
 \qquad 0\le\gamma_{jk}\le1.
\tag{17}
\]

零 vector 的对应 entries 定义为 \(0\)。

### 定理 211-H（radial Schur row-sum certificate）[T]

若

\[
 R_L:=\max_j\sum_{k=1}^J\gamma_{jk}=o(L),
\tag{18}
\]

则

\[
 \boxed{
 \left\|\sum_{j=1}^JG_j\right\|_{HS}^2=o(N).}
\tag{19}
\]

#### 证明

由定理 211-A，\(\max_j\|G_j\|^2\ll N/L^2\)。所以

\[
 \begin{aligned}
 \left\|\sum_jG_j\right\|^2
 &\le\sum_{j,k}|\langle G_j,G_k\rangle|\\
 &\le \frac{CN}{L^2}\sum_j\sum_k\gamma_{jk}\\
 &\le \frac{CN}{L^2}JR_L=o(N),
 \end{aligned}
\]

因为 \(J\ll L\)。\(\square\)

式 (18) 是 prime-side actual response 的绝对 Schur 条件，严格强于所需 signed
aggregate estimate；它不是 RH 或 Weil positivity 的改写。障碍定理 211-E
说明窗口 alone 不能验证它。

## 8. 原 far-radial 充分条件（由笔记 212 绕过）

### 开放性质 211-I（absolute far-radial decorrelation）[O]

取同一 aperture 的 dyadic radial chain

\[
 A_j=2^jA_0,
 \qquad B_j=2^jB_0,
 \qquad A_jB_j\le X.
\]

对 actual prime-power Toeplitz aggregates，证明

\[
 \boxed{
 \max_j
 \sum_{|k-j|\ge\sqrt L}
 \gamma_{jk}=o(L).}
\tag{20}
\]

近端 \(|k-j|<\sqrt L\) 由 \(\gamma_{jk}\le1\) 自动贡献
\(O(\sqrt L)=o(L)\)，所以式 (20) 与定理 211-H 合并足以闭合该 aperture 的
radial union。笔记 212-C 已用更弱的 signed Montgomery--Vaughan estimate 直接
闭合该 union；因此式 (20) 不再是路线的必要开放输入。

证明式 (20) 时必须至少利用下列一个独立算术输入：

1. actual prime-power solutions of \(ad-bc=h\) 的 weighted incidence saving；
2. \(e^{iT\log(ad/bc)}\) 与 finite Gabor geometric sums 的 signed layer
   cancellation；
3. Type I/Type II/continuum/Gamma response 之间的统一 cross cancellation。

只用 local \(W_1/W_2\)、window overlap 或 maximum determinant degree 已分别被
定理 211-C、211-E、211-G 排除。

## 9. 公理删除、循环性与模型范围

1. **local prime energy**：只给式 (4)，不控制 \(R_L\)。删除后甚至 fixed-box
   rate 失效。
2. **window regularity**：给 finite Toeplitz transfer；定理 211-E 证明它不产生
   radial decorrelation。
3. **determinant congruence**：给式 (15)--(16)；定理 211-G 证明 degree-only
   使用已经 sharp，不能继续迭代同一路线。
4. **actual arithmetic response**：若坚持证明绝对性质 211-I，它是唯一可能增益来源；该性质已被笔记 212 的 signed route 绕过，没有被
   替换成 arbitrary-coefficient Bessel bound。

循环性审计：

- 式 (20) 完全位于 prime-side finite matrices，可独立于 zeros 检验。
- 本笔记没有证明式 (20)；笔记 212 证明它并非闭合 radial chain 所必需。完整 alternating 四矩和零点比例改进仍未得到。
- pairwise \(o(N)\) 不得再记录为分支晋级，因为它由 Cauchy 自动成立。
- 不能把 plateau no-go 外推为 actual zeta cross-box no-go；它只排除 window-only
  proofs。

模型范围：

- zeta 与固定本原 Dirichlet \(L\) 函数共享式 (9) 的窗口因子化；角色相位可能
  帮助或妨碍式 (20)，必须保留。
- Dedekind/automorphic coefficients 需要各自的 local Rankin--Selberg energy 与
  determinant-label multiplicity，不能自动使用 prime-power singleton 分类。
- 函数域中 radial degree 有限时，\(J\) 可能不增长；这解释了为何相同窗口障碍
  未必出现，但不建立两类 Weil 结构的等价桥梁。

## 10. 可复现审计 [E]

脚本 `scripts/radial_cross_box_obstruction_audit.py` 检查：

1. \(J=L\) 个相同 local vectors 的 pairwise/union sharp no-go；
2. 式 (9) 的 sampled exact factorization；
3. admissible plateau window 在增长 \(L\) 下的 normalized radial Gram 行和；
4. \(\lambda\)-leaf stars 的 operator norm 恰为 \(\sqrt\lambda\)。

这些有限检查审计公式、常数方向和反例索引，不证明开放式 (20)。
