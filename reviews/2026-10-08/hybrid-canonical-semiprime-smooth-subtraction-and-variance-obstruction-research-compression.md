# 原 canonical 半素数主质量扣除与短区间方差的强弱障碍

2026-10-08。基线46106dc；只新增本研究源，不改冻结材料、math、Git。
目的为474剩余的 original positive-height scalar fourth upper。

结论：continuous 半素数主质量可以准确扣除，且 normalized mean-square
只变 additive O(ell^−4)，不要求未知 fourth bounded。正高度 phase 也能
在正确的短 log-window内用实际 BV bound传至 maximal centered discrepancy。
但该 discrepancy 的有用均方未支付。简单逐大素因子 Cauchy费用在
top product scale仍差一个X幂；已有7/8条带和 Selberg count不能自动
填上该联合差额。没有得到优于既有[R]的实际 whole upper、比例或边界。

[T] 以下连续主项、整实轴 Plancherel与实际BV恒等式；[R] 474的原对象、
Chebyshev、weighted MV、446的 fixed-gap sharp Perron；[O] 真正的新
canonical centered variance upper及独立全文审查。没有给未知预算换名字
之后称为成果，没有把 smaller-factor almost-prime family换成原high列。

## 1. 冻结对象及主文献

实读来源：

| 输入 | canonical LF SHA256 |
|---|---|
| [474 scalar准入](../../notes/474-original-short-carrier-canonical-scalar-fourth-admission.md) | 37306c6d403f48c93d5d0f92782088225084e2e4b6b694cd89644a75fe39e99f |
| [完整scalar source](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |

另实读[446 sharp Perron](../../notes/446-uniform-prime-twists-on-the-original-gabor-frame.md)
§§2–5。外部仅使用 primary papers：
[Coppola–Laporta, modified Gallagher lemma](https://arxiv.org/pdf/1301.0008)，
[general weighted version](https://arxiv.org/pdf/1411.1739)，
[Coppola, modified Selberg majorant](https://arxiv.org/pdf/1006.1229)，
[Simonič, explicit Selberg zero density](https://arxiv.org/pdf/1910.08274)。
本篇不用最新 almost-prime 搜索结果当成原 coefficient family定理。

保留 X=T/(2π)、ell=log X、Y=sqrt X、a_ell≥c_phi>0，
Lambda_H(n)=Lambda(n)1_(Y<n≤X)，c_H=Lambda_H*Lambda_H。
写未归一化的
\[
 \Psi_X(t)=\sum_{Y<n\le X}\Lambda(n)n^{-1/2+it},\qquad
 Q_X(t)=\Psi_X(t)^2
       =\sum_{X<n\le X^2}{c_H(n)\over\sqrt n}n^{it}.       \tag{1}
\]
J2=[T/4,4T]；widehat P_H=Psi_X/(a_ell ell)。genuine primes由474的
proper-power L4 norm差返回，不能在 unknown growth中先删 fourth差。
以下一直保留两 factor sharp cutoffs；没有以 full Lambda*Lambda替换c_H。

## 2. 准确continuous主质量：growth-uniform的additive小量

设 dλ_X(x)=1_(Y<x≤X)dx。其 multiplicative convolution 的普通x-density为
\[
 \rho_X(x)=\int_{Y<a\le X,\ Y<x/a\le X}{da\over a}
 =\begin{cases}
 \log(x/X),&X<x\le X^{3/2},\\
 \log(X^2/x),&X^{3/2}<x\le X^2,\\
 0,&\text{otherwise}.
 \end{cases}                                             \tag{2}
\]
这是由两个原 sharp intervals形成的 triangular log-density。
准确Fubini给
\[
 V_X(t)=\int_Y^X x^{-1/2+it}dx
 ={X^{1/2+it}-X^{1/4+it/2}\over1/2+it},\qquad
 \int_X^{X^2}\rho_X(x)x^{-1/2+it}dx=V_X(t)^2.             \tag{3}
\]
在J2，|V_X|≪X^−1/2、|V_X²|≪X^−1。Chebyshev同时给
|Psi_X|≤ΣLambda(n)/sqrt n≪sqrt X，故|Q_X|≪X。
令 F_X=Q_X−V_X²，则逐点
||Q_X|²−|F_X|²|≤2|Q_X||V_X²|+|V_X²|²≪1。因此
\[
 \left|{1\over T}\int_{J2}|\widehat P_H|^4dt
 -{1\over T(a_\ell\ell)^4}\int_{J2}|F_X(t)|^2dt\right|
       \ll_\phi\ell^{-4}.                               \tag{4}
\]
这比仅有 norm-difference更强，是真正 additive o(1)，无 fourth-growth
前件。没有按每个product dyad孤立扣除一个带 artificial endpoint 的主项，
也没有把rho_X(integer)的离散和等同(3)的continuous integral。

## 3. 对correct centered measure的整轴Gallagher支付

定义 compact signed measure（y=log x）
\[
 d\mu_X(y)=\sum_{X<n\le X^2}{c_H(n)\over\sqrt n}\delta_{\log n}(dy)
             -e^{y/2}\rho_X(e^y)dy .                     \tag{5}
\]
其 transform ∫e^(ity)dmu_X=F_X(t)。取
t0=17T/8、B=15T/8、δ=1/T、k_δ(y)=(1−|y|/δ)_+，
并定义 actual modulated centered short-window
\[
 E_X(y)=\int k_\delta(y-z)e^{it0 z}d\mu_X(z).             \tag{6}
\]
该phase不是自由改变原coefficients：它准确把J2移到[−B,B]。
kernel transform为δ sinc²(vδ/2)，在|v|≤B有模≥cδ，因为
Bδ/2=15/16<π。compact measure卷积在L2；Plancherel直接给
\[
 {1\over T}\int_{J2}|F_X(t)|^2dt
           \ll T\int_{\mathbb R}|E_X(y)|^2dy.            \tag{7}
\]
这里重证相应weighted Gallagher步骤用于atoms减continuous density；
不把仅有discrete coefficients的引用免费扩展成不同中心。
无height0窗口加入左侧，右侧仍保留真实 e^(it0 log n)。

## 4. phase的真实BV付款与所需maximal discrepancy

对x>0，令a_x=x e^−δ、b_x=x e^δ，并置
\[
 D_X(x;v)=\sum_{a_x<n\le v}c_H(n)-\int_{a_x}^v\rho_X(z)dz,
 \quad a_x\le v\le b_x,\qquad
 \mathcal D_X(x)=\sup_v|D_X(x;v)|.                        \tag{8}
\]
端点处原c_H均保留；D 是finite-variation signedmeasure的cumulative。
权 w_x(v)=k_δ(log(x/v))v^(-1/2+it0) 在a_x,b_x均为零，准确有
E_X(log x)=∫w_x(v)dD_X(x;v)=−∫D_X(x;v)dw_x(v)。
triangle derivative部分的variation≤C/sqrt x；v^(-1/2+it0)部分的
variation≤C(1+t0)δ/sqrt x≪1/sqrt x。于是
\[
 |E_X(\log x)|\ll x^{-1/2}\mathcal D_X(x),\qquad
 \int|E_X(y)|^2dy\ll\int_0^\infty{\mathcal D_X(x)^2\over x^2}dx.\tag{9}
\]
这支付了chirp的窗口费用。没有忽略其O(1) variation，也不假设 ordinary
single-h centered variance自动控制rowwise maximal prefixes。
(4)、(7)、(9)给一个具体**充分**预算
\[
 \int_0^\infty{\mathcal D_X(x)^2\over x^2}dx\ll {\ell^4\over T}.
                                                               \tag{10}
\]
不宣称其与scalar upper双向等价。原support仅扩张到
[X e^−δ,X² e^δ]。top x≈N≈X² 的window length≈N/T≈X，
该部分若沿(10)支付，需Jmax(N)=∫_(x≈N)Dcal_X(x)²dx≪X³ell4。
全部product scales必须在(10)共同计费；若每个dyad都另给ell4预算，
还有O(ell)个dyad费用，不能不计。

## 5. 原大因子范围为何不给one-prime shortcut

top product x≈cX²（c>0固定）迫使两个原factor都≈X，
固定a后另一factor区间长度≈(X²/T)/a≈1。
以同一个sharp截断Ψ的短和展开，必须估计这些unit-scale prime
windows对全部大a的联合二矩，而非只估计各窗口的期望。

具体，外部Λ-weight Cauchy给Σ_(a≈X)Λ(a)≪X；单独的inner unit
window二矩只能用Σ_(b≈X)Λ(b)²≪X ell。换变量x=a z后，
每个a的积分费用≪X²ell，故逐a Cauchy的累计级别为
\[
 J_{\rm Cauchy}(X^2)\ll X^4\ell .                       \tag{11}
\]
maximal inner prefixes在bounded-length interval含O(1)整数，同级估计
仍可付；这不会变成(10)所需X³ell4。smooth outer-factor correction
若仅用Ψ(z)−z=O(z^theta polylog z)，其square integral费用是
X^(2+2theta)polylog，theta=7/8时仍为X^(15/4)polylog。
这些是明确方法费用，不是实际Dcal或scalar moment的lower bounds。
原signed inner/outer terms可能相消；我们没有支付该相消。

small-prime-factor almost-prime定理处理a=X^o(1)或polylog因子时，
inner interval能长得多；它不能覆盖本top dyad的a≈X。存在性、
almost-everywhere asymptotic与此weighted maximal mean-square也不同。

## 6. Coppola majorant并不支付原center

Coppola1006.1229的主要majorant theorem要求real g、
supp g⊂[1,Q]且Q≤N+h，中心是divisor representation g*1的
Wintner mean。它不是任意 pointwise positive coefficient domination
即可传递centered Selberg variance的定理。
原c_H的μ-pullback含接近product scale本身的大divisors；保留
整个[N,2N]一般需要到2N的range，不能声称已有小divisor support。
此外positive-height e^(it0 log n)是complex且随T变化；直接对其引用
real-g结论未获准，改用(9)也仍需真正的maximal预算。
作者对G=1的讨论明确指出wrong divisor mean可留下trivial variance。
因此以|c_H|≤polylog·d2或某个divisor majorant替换它，再减一个
不同的主项，不是原rho_X-centered variance的付款。

## 7. weak whole bounds与7/8/Selberg密度的实际范围

可记录一个无条件但不构成当前突破的whole bound：在dyadic
P≤n≤2P≤O(X)，mass ΣΛ(n)/sqrt n≪sqrt P、weighted MV second≪log P。
故该块的L4 fourth≪P log P。L4 Minkowski按geometric dyads求和，
\[
 {1\over T}\int_{J2}|\widehat P_H(t)|^4dt\ll {X\over\ell^3}.
                                                               \tag{12}
\]
474显示的直接product-MV是X/ell²；(12)只省一个log。
等价Gallagher推导中δ=1/T、q≤X使inner log-window含至多一个整数，
对外factor weighted Cauchy可得到同一界。这个事实不支付centered
cross-factor cancellation；无需把它包装成新的Selberg成果。

更关键的是446已有[R]：任意fixed a>7/8，原sharp prefix在J2可同样
付sup|widehat P_H|≪X^(a−1/2)ell；其MV second为O(1)。于是
\[
 \mathcal M_T\ll_a X^{2a-1}\ell^2
             \ll_\epsilon X^{3/4+\epsilon}.              \tag{13}
\]
它比(12)更强；所以本文不把该raw log-saving称为新best actual upper。
(13)仍不提供(10)或474的finite constant目标。

Selberg的零点密度是count，不是加权四阶zero-feature correlation。
例如已核primary记录N(σ,T)≪T^[1−(σ−1/2)/4]logT。
在sharp Perron中单个β-layer residue的自然幅度是X^(β−1/2)。
即使只尝试正的diagonal fourth majorant，也出现
T^−1 N(β,CT)X^(4β−2)。要使其bounded，需要count exponent
≤3−4β；Selberg exponent不给此条件。β=3/4时阈值已为0，
Selberg exponent仍15/16；7/8条带只给β的上限。
这只是该positive-density方法的幂诊断，不是已证实际fourth的lower
bound，也不能反向称为新的3/4无零定理。zero residues之间的完整
signed cancellation仍可能有用，但count输入没有认证它。
新的BGL原行密度同样不能把primitive character rows免费映为本n^it列。

## 8. 当前结论

主质量和短窗chirp的准确付款见(4)、(9)；真正的剩余算术是(10)，
或直接对同一positive J2净估计F_X。当前简单大因子方法的费用(11)
与目标差固定X幂；majorant与density输入都缺同对象的联合相消。
未证明有用的新actual scalar upper，未完成whole fourth，没有新比例、
无零边界或新论文。本文的障碍只约束列出的证明路线，不断言数学上
不可能从原输入构造更好的signed方法。
