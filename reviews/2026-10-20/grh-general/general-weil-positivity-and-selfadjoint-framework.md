# 一般 g-integer 的 RH：完整除子、Weil 正性、实谱与行列式的准确接口

2026-10-20。本稿按 root 当前任务独立出稿，不改 STATE/cadence，不提交 Git。
已读恢复入口、原 Goal/C024/strategy/frontier、561 及本日历史审计与 direct-Fourier stop。
新的用户要求明确扩大对象类，故本稿不继续单位整数梳分类，也不复活已停止的直接 Fourier 运输。
本稿是一般条件鉴别与可自证的接口命题；它没有证明实际 ζ 的未知正性或新的成长费用。

## 1. 先把三个不同层次的“广义 RH”分开

对正的 distributional Beurling 系统，以对数变量 \(u\geq0\) 表示 g-integer 测度 \(M\)，
primitive g-prime 测度 \(P\)，prime-power 测度

\[
 \Pi=\sum_{k\geq1}\frac1k(k_\ast P),\qquad
 Z(s)=\int e^{-su}\,dM(u)=\exp\left(\int e^{-su}\,d\Pi(u)\right).
\]

等式最初只在绝对收敛半平面成立；单位原子、局部有限性、加权积分和交换另要证明。
这里 \(P\geq0\)、\(M\geq0\) 与零点侧正性是三件事。

1. **没有完成化/对偶时**，一个有意义的 RH 型目标是：在所声明的亚纯延拓域内，
   去除已列明极点后，\(Z(s)\ne0\) 于 \(\Re s>\beta\)。这是一侧谱界。
   \(\beta=1/2\) 只有在增长标度/极点已规范化后才有意义；一般系统没有先验中心。
2. **有完整反射对偶时**，若所选完成对象的全部相关零点关于
   \(\tau_c(s)=2c-\bar s\) 对称，则“右半平面无零 \(\Re s>c\)”
   与“全部相关零点在 \(\Re s=c\)”等价。反射本身只给成对性。
3. **给定实际算子实现时**，还可问其中心化生成元是否在指定的正 Hilbert 空间自伴。
   这比存在某个后验实谱模型更具体：Jordan 链、原域、闭性、谱覆盖及重数必须保留。

Beurling 文献中常把第一层称为 RH；它不能自动升级为第二或第三层。
物理侧 \(M\) 是否连续，与完成函数的零除子是否离散，也不是同一个问题。

## 2. 完成对象的最小记账

先固定已知背景因子 \(A(s)\)、中心 \(c\in\mathbb R\) 及完成对象

\[
 \Lambda(s)=A(s)Z(s).
\]

不能在知道目标零点之后任意选择 \(A\)。若 \(\Lambda\) 只有有限个极点 \(p_j\)，
精确阶数为 \(n_j\)，令

\[
 \Xi(s)=\left(\prod_j(s-p_j)^{n_j}\right)\Lambda(s).
\]

以下基本版本要求 \(\Xi\not\equiv0\) 是整函数、阶至多 1，全部相关零点在有限竖带中。
极点阶数必须精确：上式在原极点处通常非零，不能额外制造一个零点。
已知平凡零点若要剥除，须事先给明确因子和全除子恒等式。
函数域型对象可直接在 \(T=q^{-s}\) 中用有理函数分子；其 \(s\) 版本仍可使用本文接口。

反射条件采用

\[
 \Xi(s)=\varepsilon\,\overline{\Xi(2c-\bar s)},\qquad |\varepsilon|=1.
 \tag{2.1}
\]

非自对偶 L 函数须明确其对偶对象，或先组成保全部除子的对偶对，不能把两个函数静默当成一个。
本文只用 (2.1) 所蕴含的**完整带重数除子**对称。设零集为 \(\mathcal Z\)，
每个零点 \(\rho\) 的阶数 \(m_\rho\in\mathbb N\)，则

\[
 \tau_c\mathcal Z=\mathcal Z,\qquad m_{\tau_c\rho}=m_\rho.
\]

阶至多 1 保证零点计数为多项式增长，且
\(\sum_{\rho\ne c}m_\rho/(1+|\rho-c|^2)<\infty\)。
“只在一条有限带内亚纯”不足以直接谈全球 canonical product；
本节整延拓是一个明确的充分版本。仅局部带对象可以另做局部除子命题，不能偷用全平面结论。

## 3. 一个可完全证明的广义 Weil 判据

### 3.1 全域测试空间与卷积平方

令 \(\mathcal E\) 为所有 entire \(F(s)\)，满足对每个 \(R,N>0\)，

\[
 \sup_{|\Re s-c|\le R}(1+|\Im s|)^N|F(s)|<\infty.
 \tag{3.1}
\]

这是“每个固定竖带内快速衰减”的全域空间，不是仅一组低频测试。
它在点乘及 \(F^\dagger(s)=\overline{F(2c-\bar s)}\) 下封闭。
也可由对数侧的

\[
 \mathscr S_{\exp}=\{h\in C^\infty(\mathbb R):
 \sup_u e^{a|u|}|h^{(k)}(u)|<\infty\quad(\forall a>0,\ k\ge0)\}
\]

通过 \(F(s)=\int h(u)e^{(s-c)u}\,du\) 得到。
逐竖线 Fourier 反演及移线证明 (3.1) 的逆像也属于该空间。
这里加法卷积 \(h*k\) 与 \(h^\dagger(u)=\overline{h(-u)}\) 对应上述点乘和反射。

定义**线性**零泛函及其**二次**形式

\[
 W_\Xi(h)=\sum_\rho m_\rho F_h(\rho),\qquad
 q_\Xi(h,k)=W_\Xi(h*k^\dagger)
 =\sum_\rho m_\rho F_h(\rho)
       \overline{F_k(\tau_c\rho)}.
 \tag{3.2}
\]

各级数由 (3.1)、有限竖带及零点计数绝对收敛；\(q\) 对全 complex 测试有效。
此外 \(W_\Xi\) 在 \(\mathscr S_{\exp}\) 上连续。具体若
\(|\Re\rho-c|\le B\)，分部积分 \(N\) 次给

\[
 |F_h(\rho)|\le C_{B,N}(1+|\Im\rho|)^{-N}
 \sum_{j\le N}\sup_u e^{(B+1)|u|}|h^{(j)}(u)|.
 \tag{3.2a}
\]

取 \(N\) 大于零点计数的多项式指数再加 1，便能逐绝对求和。
这才是应要求非负的对象 \(q(h,h)=W(h*h^\dagger)\)。
若把线性式 \(\mathcal A(f)-\langle\varpi,f\rangle-\langle\varpi,f^\sharp\rangle+H(f)\)
直接要求对所有 \(f\) 非负，替换 \(f\mapsto-f\) 就迫其恒零，不能作为 Weil 判据。

乘法变量用 \(\mathcal Mf(s)=\int_0^\infty f(x)x^s\,dx/x\) 时，
正确反演为 \(f^{\sharp_c}(x)=x^{-2c}\overline{f(x^{-1})}\)。
用户给的 \(x^{-1}\) 正是 \(c=1/2\) 的规范；中心变化后权也要随之变化。
取 \(h(u)=e^{cu}f(e^u)\)，就得到 (3.2) 的对数坐标和普通卷积平方。

### 3.2 命题与精确分离证明

**命题 A。** 在 §2 条件下，以下等价：

\[
 \Re\rho=c\quad(\forall\rho\in\mathcal Z)
 \quad\Longleftrightarrow\quad
 q_\Xi(h,h)\ge0\quad(\forall h\in\mathscr S_{\exp}).
 \tag{3.3}
\]

右侧也等价于仅要求**全部** \(h\in C_c^\infty(\mathbb R)\) 的正性；
这里“全部”仍含任意支撑尺度和 complex 测试。

**充分/必要的逐步证明。** 若所有零点在中心，\(\tau_c\rho=\rho\)，
于是右侧是 \(\sum m_\rho|F_h(\rho)|^2\ge0\)。
反过来，设 \(\rho_0\ne\tau_c\rho_0=\rho_1\)，该对的共同重数为 \(m\)。
置

\[
 G(s)=\frac{\Xi(s)}{(s-\rho_0)^m(s-\rho_1)^m}.
\]

该函数 entire，在 \(\rho_0,\rho_1\) 非零，在其他所有零点为零。
取一次多项式 \(L(s)\)，使

\[
 F(s)=e^{(s-c)^2}G(s)L(s),\qquad
 F(\rho_0)=1,\quad F(\rho_1)=-1.
\]

两个插值值可任意指定，因为两点不同、两个前乘子都非零。
\(\Xi\) 阶至多 1，故固定竖带的增长由 \(e^{C_R|t|^{1+\epsilon}}\)
控制；Gaussian \(e^{(s-c)^2}\) 的 \(e^{-t^2}\) 使 \(F\in\mathcal E\)。
代入 (3.2) 后只有这对零点留下，得到

\[
 q_\Xi(F,F)=-2m<0.
\]

因此全域正性不能容纳任何离线反射对。证明没有忽略其余无穷多零点、重数或尾项。
更一般的有限阶整函数可选更高偶次的垂直衰减因子，得到同型结论；
genus \(\le1\) 对这一分离原理并非必要，主要方便 §5 的 determinant 规范。

**compact 测试版本的尾控制。** 对上述负测试的逆变换 \(h\in\mathscr S_{\exp}\)，
取固定 \(\chi\in C_c^\infty\)、在 \([-1,1]\) 上为 1，
令 \(h_R(u)=\chi(u/R)h(u)\)。由任意指数衰减及 Leibniz 公式，
\(h_R\to h\) 在 \(\mathscr S_{\exp}\) 的每个 seminorm 中成立。
卷积在该空间连续，(3.2a) 因而给
\(q_\Xi(h_R,h_R)\to-2m\)，所以某个 sufficiently large **有限** \(R\)
已经给合法 compact 负测试。这支付了本命题的 compact-test 版本，而非形式援引分离性。
若物理 explicit formula 已精确识别全部 compact 测试的 \(W_\Xi\)，
就不必再让其 prime/archimedean 各项单独延拓到该负测试的整个尾部。

**本命题的限制。** 此证明为了说明测试空间足够大，构造的分离测试使用了 \(\Xi\)；
它不提供独立的算术正性来源。若只有有限窗口/有限维测试的正性，或尚未付清竖带和零点计数，
上述 compact cutoff 极限仍不可消费。增长与全部测试是实质前件。

Lagarias 的原文 §3 用
\(\sum F(\rho)\overline{G(1-\bar\rho)}\) 定义 automorphic Weil 型，
明确区分 Hermitian 对称、中心线上的平方和及充分分离全部零点的测试。
其 Theorems 2.2/3.1 给 automorphic Li 正性与相应 RH 的精确等价接口。
本节命题是在所声明更强 entire 测试空间上的直接证明，并非声称该论文证明所有 Beurling 系统。
来源：[Lagarias, §3, pp.11–13](https://arxiv.org/pdf/math/0404394)。

## 4. 从正定分布到自伴：得到什么，没得到什么

### 4.1 Bochner–Schwartz 的正确对象

若一个线性分布 \(W\in\mathcal D'(\mathbb R)\) 在**全部**
\(h\in C_c^\infty(\mathbb R)\) 上满足 \(W(h*h^\dagger)\ge0\)，
它是 positive-definite distribution，按 Bochner–Schwartz 定理自动为 tempered，
存在唯一正 tempered 测度 \(\sigma\)，使

\[
 W(h*k^\dagger)=\int\widehat h(t)\overline{\widehat k(t)}\,d\sigma(t),
 \quad \widehat h(t)=\int h(u)e^{itu}\,du.
 \tag{4.1}
\]

傅里叶方向与常数由本式固定。\(\sigma\) tempered 只要求某个多项式权可积，
不自动给 \(\int (1+t^2)^{-1}d\sigma<\infty\)。后者是 genus-one determinant
的额外强条件。一般 \(W\) 是分布而非连续有界函数，不能只援引有限测度版本的 Bochner 定理。

研究论文 [Jorgensen–Tian, Theorem 2.1](https://arxiv.org/pdf/1712.07264)
给出 tempered-distribution 的正测度表示及相应 Hilbert 等距实现。
对 \(\mathcal D'\) 正定分布自动 temperateness 的标准扩展，
可另核 [Chung–Chung–Kim 的 Theorem 2, p.140](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/49688AE542CF2E144CD761D4E36BDDB5/S0027763000005456a.pdf/positive_definite_hyperfunctions.pdf)；
若使用时只已付 \(\mathscr S'\) 版本，直接把 \(W\in\mathscr S'\) 列为前件即可。

### 4.2 GNS/Stone 的域与 generator

由 \(q(h,k)=W(h*k^\dagger)\) 将 nullspace 商掉再完成，得正 Hilbert 空间。
平移 \(T_a h(u)=h(u-a)\) 保 \(q\)，且随 \(a\) 强连续，故诱导 unitary 群。
在 (4.1) 表示中，它是乘子 \(e^{iat}\)，其 Stone generator 为

\[
 (Dg)(t)=t g(t),\qquad
 \operatorname{Dom}D=\left\{g\in L^2(\sigma):\int t^2|g(t)|^2d\sigma(t)<\infty\right\}.
 \tag{4.2}
\]

这是指定最大域上的自伴乘法算子。测试函数的 Fourier 像在 \(L^2(\sigma)\) 中稠密：
若有正交向量，则其与 \(\sigma\) 的乘积分布由 temperateness/Cauchy–Schwarz 定义，
逆 Fourier 后杀掉全部 compact 测试，因此为零。
同理对 \((1+t^2)\sigma\) 得 graph-norm 稠密，故该测试域可作为 generator 的 core。
符号上原源的 \(i\,d/du\) 对应 \(D\)；仅写形式微分表达式不等于已经证明某个
其他边界条件/source quotient 上的自伴性。

### 4.3 普通正定性与 OS 反射正性有别

上面用的是全线 difference kernel \(W(u-v)\) 的卷积正定性。
Osterwalder–Schrader 反射正性通常从正半轴测试和 sum kernel \(C(u+v)\) 开始，
在合适连续性/收缩条件下重建 \(e^{-aH}\) 及 \(H\ge0\) 的 semigroup。
两者涉及不同测试域、核及 generator 符号；一个含“反射”字样的等式不能替另一种正性付款。
若提出 OS 路线，须另给反射、正半轴、重建空间以及与同一 \(\Xi\) 的 resolvent/determinant 恒等式。

一个可直接否定术语混用的测试是 \(W(u)=2\cos(\tau u)\)、\(\tau>0\)。
其谱测度 \(\delta_\tau+\delta_{-\tau}\) 为正；difference kernel 的形式为
\(2(|C_h|^2+|S_h|^2)\ge0\)，其中
\(C_h=\int_0^\infty h(u)\cos(\tau u)\,du\)、
\(S_h=\int_0^\infty h(u)\sin(\tau u)\,du\)。
但 OS sum kernel \(2\cos(\tau(u+v))\) 的形式为
\(2(|C_h|^2-|S_h|^2)\)。
在两个正位置放置小的 smooth compact bumps，用两系数令 \(C_h=0\)，
并选择相位差不为 \(\pi\) 整倍数，即可保持 \(S_h\ne0\)，得到严格负值。
故一个 genuine 中心线二零点模型已经满足 Weil 正型而不满足这个 OS 正性。
若 Kimi 的“反射正性”意指后者，便不是它声称的一般 RH 等价条件。

## 5. C4 隐藏的两种谱测度，尤其是重数

### 5.1 正谱测度不是自动的零点 counting measure

若 §3 的**完整**零泛函正性已付，则实际中心线零除子给

\[
 \sigma_{\rm div}=\sum_\gamma m_\gamma\delta_\gamma,
 \qquad \rho=c+i\gamma.
 \tag{5.1}
\]

但只给某个正测度的表示，不附完整 explicit-formula 身份，不能判定其为 (5.1)。
非零 entire 函数在有限平面的零点必孤立，阶数必为正整数；
因此与普通 entire 零除子**完全相同**的测度必须是局部有限纯点测度、原子质量为整数。
任意连续 \(\sigma\) 可以给合法自伴乘法算子，却不能把
\(\prod_{\gamma\in\operatorname{supp}\sigma}\) 当成普通 entire canonical product。
这不妨碍物理侧的连续 \(M,P\) 具有离散中心线零除子。

### 5.2 标量 \(L^2(\sigma)\) 丢掉了 determinant 的重数

即使 \(\sigma=\sum m_\gamma\delta_\gamma\)，在**标量** \(L^2(\sigma)\) 上，
每个支撑点的特征空间仍只有一维。质量 \(m_\gamma\) 只是内积权，可以酉吸收；
它是 cyclic spectral weight，不是 ordinary operator trace 的秩。

最便宜负测试是 \(F(z)=z^2\)、\(\sigma=2\delta_0\)。Weil 平方和为
\(2|\widehat h(0)|^2\)，完全正确；标量 \(L^2(2\delta_0)\) 上 \(D=0\)
只有一维，\(\det(z-D)=z\)，不等于 \(z^2\)。
有限秩两侧模型 \(F(z)=(z^2-\tau^2)^2\) 在 \(\pm\tau\) 各重数 2，
也有同样问题。这不是零点在零位置才发生的特殊现象。

要用 ordinary trace/determinant 保存全重数，必须改用

\[
 \mathcal K=\bigoplus_{\gamma}\mathbb C^{m_\gamma},\quad
 D|_{\mathbb C^{m_\gamma}}=\gamma I,\quad
 \operatorname{Tr}E_D=\sum m_\gamma\delta_\gamma.
 \tag{5.2}
\]

或使用明确给定的非标准 trace/相对 determinant；这时须把该 trace 本身列为数据。
GNS 的最小 cyclic 模型 (4.2) 与带完整重数的 trace 模型 (5.2) 可有相同实支撑，
却不是同一个 determinant 实现。

### 5.3 一个准确的 genus-one determinant 充分命题

令 \(F(z)=\eta\Xi(c+iz)\) 为相位规范化后的 real-type entire 函数。
若独立构造了自伴 \(D\) 具有 compact resolvent，\(m_0=\dim\ker D<\infty\)，
\(D_\perp^{-1}\) Hilbert–Schmidt，且已证明解析恒等式

\[
 F(z)=e^{a+bz}z^{m_0}\det{}_2(I-zD_\perp^{-1}),
 \tag{5.3}
\]

则 \(F\) 全部零点实，重数也准确。这里 \(\det_2\) 是 Hilbert–Schmidt
regularized determinant，等价于按特征空间重数的 \(E_1\) canonical product。
零特征值单列；\(a,b\) 和基点/相位/值的规范须独立固定。
\(\sum m_\gamma/(1+\gamma^2)<\infty\) 只支付乘积收敛，
还不支付 (5.3) 与 \(\Xi\) 的身份。

若一开始已有 \(F\) 的全部实零点，然后按这些零点定义 (5.2)，
再由 Hadamard 证明 (5.3)，这只是准确的后验等价，不是独立证明机制。
反之，几何/正形式先给实际 \(D\)，随后不利用未知零点位置证明 (5.3)，才是充分路线。
对于 meromorphic 完成对象，需要预先固定的 pole determinant/有限缺陷，不能把有符号除子
当成一张正谱测度；任意“有限秩缺陷”甚至能删掉有限个离线零点，故缺陷不可自由选择。

### 5.4 中心谱不保证指定 source generator 自伴

中心零除子保证存在某个按重数构造的对角自伴模型，却不保证预先指定的 source quotient
或伴随矩阵可酉化。例如 \(F(z)=z^2\) 可由 \(D=0\) 于 \(\mathbb C^2\) 实现；
同一个特征多项式也由非零 nilpotent
\(N=\begin{pmatrix}0&0\\1&0\end{pmatrix}\) 实现。
后者含 Jordan 链，不可能在任何正定内积下自伴；非零自伴 nilpotent 不存在。
无限维还须查指定拓扑、闭域和群是否允许等价正定 norm。
这正是旧 520/526 已要求保留的“完整 Jordan/source norm”责任。

## 6. 可直接算在复平面的 Pick 判据

在 §5.3 的 real-type、阶至多 1/实仿射 Hadamard 规范下，还有一个简洁等价：

\[
 F\text{ 全部零点实}
 \quad\Longleftrightarrow\quad
 M(z)=-\frac{F'(z)}{F(z)}
 \text{ 在 }\mathbb C_+\text{ 全纯且 }\Im M(z)\ge0.
 \tag{6.1}
\]

这里允许 \(F\) 无零点，此时 \(M\) 为实常数。非空除子时上半平面的虚部严格正。
**证明：** 实零点 genus-one product 给

\[
 M(z)=-b-\frac{m_0}{z}
 +\sum_{\gamma\ne0}m_\gamma
 \left(\frac1{\gamma-z}-\frac1\gamma\right),\quad b\in\mathbb R.
\]

固定上半平面紧集级数正规收敛，且

\[
 \Im M(x+iy)=\frac{m_0y}{x^2+y^2}
 +\sum_{\gamma\ne0}\frac{m_\gamma y}{(x-\gamma)^2+y^2}\ge0.
\]

反向只用 \(M\) 在上半平面全纯排除该处零点，再用 real-type 反射排除下半平面。
真实整数残数与整除子重数在此仍保留。
有限阶/规范不可忽略：例如 \(F(z)=e^{z^2}\) 根本无零点，
但 \(-F'/F=-2z\) 不是 Pick 函数。若允许这种额外零自由因子，左侧不推出右侧。

这给一个不写零点总和的分析条件，可尝试由完成化 log-derivative 直接验证。
然而对经典 \(\Xi\)，(6.1) 本身仍与 RH 等强；
positive primitive 的 Laplace 性质只在原收敛侧，并不自动支付含实际 \(\Gamma\)、
反射和 pole 修正的这个全上半平面 Pick 不等式。

## 7. 对 C1–C5 的逐条裁决

| 条件 | 保留/修正 | 未付或过强之处 |
|---|---|---|
| C1 | 有限阶、完整延拓、已固定背景、临界带、零点计数是合法前件 | 在一条带内亚纯不保证整个 canonical product；genus \(\le1\) 是方便的充分规范，并非所有类 RH 对象必需 |
| C2 | 保留精确反射及对偶身份；它固定中心并使 Weil 型 Hermitian | FE 不给中心零点；“模有限缺陷”只能是事先精确计算的缺陷，不能自由删有限离线零点 |
| C3 | 改为线性 \(W\) 在卷积平方上的全域正性；核/测试/complex/pole 全保留 | 对完整目标除子通常就是 RH 等价；显式平方和若独立于未知零点可成为证明输入。普通正定性与 OS 反射正性不可混用 |
| C4 | 需要完整带重数除子、纯点/整数质量、零位置单列、trace multiplicity、精确正规化 | 任意正 \(\sigma\) 或标量 \(L^2(\sigma)\) 的支持不能产生正确 determinant；连续 \(\sigma\) 无通常整个零乘积 |
| C5 | 有条件的 finite-to-global 充分路线，可保留为一个研究入口 | simple/even/边界非零不是一般 g-RH 必要条件；真正共同门是 real-zero 近似 entire 函数对同一非零 \(F\) 的紧集一致收敛 |

### 7.1 C5 的最简充分定理

若 entire \(F_n\) 的全部零点在 \(\mathbb R\)，且 \(F_n\to F\not\equiv0\)
紧集一致，则 \(F\) 的全部零点实。对上下半平面分别用 Hurwitz 即证；
某个非实零点也可用小圆盘和 Rouché 得直接矛盾。
不需要每个零点简单，也不需要 lowest eigenvector 为偶。
若 \(F_n=e^{a_n+b_nz}\det(z-D_n)\) 且 \(D_n=D_n^*\)，实零点前件自动成立，
但对目标 \(F\) 的非零局部一致收敛仍必须证明。
低谱数值吻合、强 resolvent 收敛或每个 cutoff 的某个正 Gram，单独均不能代替这个 determinant 身份。

### 7.2 C5 的确切近期来源范围

Connes–Consani–Moscovici 的 [*Zeta Spectral Triples*, Theorem 1.1, p.2](https://alainconnes.org/wp-content/uploads/zeta-spectral-triples-1.pdf)
确实假设其有限 Weil 矩阵的最低本征值简单、向量 even 且边界配对归一为 1；
随后在指定 quotient 的特定正内积上得到自伴 rank-one perturbation、
其 regularized determinant 与该向量 Fourier 变换的恒等式及实零点。
作者摘要、§1 和 §7–8 将归一化 determinant 向经典 \(\Xi\) 的收敛列为仍需完成的步骤。
因此 Kimi 的 C5 是一个具体构造的条件包，不是所有 Beurling/数域/函数域 RH 的普遍公理。
本稿只核上述原文范围，未据数值宣称其经典 RH 路线已闭合。

## 8. 是否能称为“解决”而非“等价”：可检验的因果判定

准确的充分定理当然可以写成：固定 \(A,c\)，支付完整 explicit formula，
在分离全除子的测试域上独立证明 \(W(h*h^\dagger)\ge0\)，则中心线结论成立。
也可走独立 \(D\) 加 (5.3)，或 real-zero determinant 近似加 §7.1。
这些一般定理都正确，不能因此说经典 ζ 已属于其正类。

对经典 ζ 的“成员资格”若包含完整 Weil 正性、精确 real-zero determinant 或 (6.1)，
便包含 RH 本身。先把这些作为公理再证明 RH，是等价组织；
证明它们来自独立的同对象 \(\Gamma\)/prime-power/pole 恒等式、
几何正极化或全域 uniform comparison，才改变实际瓶颈。

没有证据支持“经典 ζ 是一般正性锥的唯一极端点”。首先必须定义具体凸锥及其 affine slice；
完成化、Euler 卷积指数和固定 pole/背景约束通常不是简单线性条件。
其次数域、函数域、连续物理分布均可落入更宽的 RH 类，单位梳刚性不能代其分类。
“某个更窄类只有整数”只识别了该类；若给该类 RH 的唯一未付前件仍是 Weil 正性，
就没有逻辑上的捷径。

本仓可消费的短链保持：旧 290/561 负基准排除裸 FE 与普通正源的混同；
307 的同一 Frobenius/几何正极化说明什么才算独立来源；
520 的完整谱/source 商及 560 的逐 fixed-window 正迹减紧误差说明实际 ζ 的身份已有资产，
剩下的仍是全域正性/成长 signed 费用及 faithful determinant 极限。
本稿纠正并细化了一般类的公理，尤其付清测试分离证明和 C3→C4 的重数漏洞，
没有改变实际 ζ 的 whole 强旧 \(4/5\) 或成长 core 瓶颈。

## 9. 本原稿的消费记录

| 项目 | 精确状态 |
|---|---|
| 对象 | 正 Beurling \(P,\Pi,M\) 是物理侧；\(\Xi\) 是预先固定完成/去 pole 的整个对象；\(\sigma_{\rm div}\) 是零除子侧 |
| 域/范数 | §3 全 \(\mathscr S_{\exp}\)/竖带快速 entire；§4 正定分布在全 compact 测试及明确 Hilbert 最大乘法域；未给实际 Weil 原 \(du\) 的新费用 |
| 系数/重数 | 每个零点 \(m_\rho\in\mathbb N\)；离线反射对的负值精确为 \(-2m\)；scalar spectral weight 与 trace rank 分开 |
| 外部来源 | Lagarias §3 的 automorphic Weil 型；Bochner–Schwartz/GNS 的已知谱表示；CCM Theorem 1.1 的特定有限截断。未扩大为任意 Beurling 已知定理 |
| 独立证明 | 命题 A 的 entire 全域分离；genus-one Pick 判据；scalar \(L^2\) 的重数反测试；Hurwitz 最简充分命题 |
| 未付 | 经典 ζ 的独立完整正性、指定实际 source 的正 Hilbert 自伴域、全除子 determinant 身份/极限、cofinal 成长误差 |
| 强旧比较 | 普通 FE 负基准已有 290/561；谱识别已有 520；正迹减 compact 已有 560；本稿不是新的实际 whole 预算 |
| 轮次/交接 | 独立审查原稿，待 root 核消费；不自行结算。下一步核全模型表，特别连续有理模型系数 \(\kappa=1/4\)、中心 \(c=1/2\) 的双重中心零点是否正确保 trace multiplicity；无 pending producer/数值进程 |
