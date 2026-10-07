# 原 thin-high / short-low 的整个 actual31：全符号固定位移 gate

2026-10-07。作者 twisted_research。状态：新完整推导，待独立全文审查。
只新增本报告，不修改旧来源、笔记、论文、审查、math、脚本、output 或 Git。

本次付清一个 **整个有符号 capped31 sector**：原 high range保留为
(X^(1/2),X^(11/20)]，原 low range取其 sharp子前缀 p<=X^(1/3)。
相对于既有 conductor-one [R] theta=7/8，证明同一原有限矩阵

\[
 \boxed{\operatorname{Tr}(C_t^3C_s)=o(d).}               \tag{1}
\]

这里包含全部16个方向、全部 genuine-prime标签、原carrier、所有内部P
和全部height，不先删重复标签。它不证明原完整high/low的整个31、
distinct22、467实际q/k前件或新的临界线比例。

## 1. 冻结前件与原对象

E、P、phi、a_L、b_p、R_s全部沿用
[非交替sign gate稿](hybrid-three-high-one-low-nonalternating-gate-research.md)
的 (1)–(3)。准确地

\[
 X=T/(2\pi),\ L=\log X,\ d=\lfloor XL\rfloor,
 \quad Ee_k=L^{-1/2}1_Ie^{i\tau_ku},\ I=[-L/2,L/2],
 \quad\tau_k=T+2\pi k/L,\quad P=EE^*,\quad Q=1-P.
                                                               \tag{2}
\]
\[
 b_p=\frac{\log p}{a_LL\sqrt p},\qquad
 B_R^\varepsilon=-\sum_{p\in R}b_pM_\phi
                      R_{\varepsilon\log p}M_\phi,
 \quad C_R^\varepsilon=E^*B_R^\varepsilon E,
 \quad C_R=C_R^++C_R^-.                                 \tag{3}
\]

所有平移先零延拓；原 even C² taper的支撑是I，0<=phi<=1，
phi及phi²的一、二阶导数L¹一致有界，a_L有固定正下界。
P始终是 interval上的原finite-carrier投影。
设

\[
 R_t=(X^{1/2},X^{11/20}]\cap\mathbb P,\qquad
 R_s=[2,X^{1/3}]\cap\mathbb P.                           \tag{4}
\]

这是原标签的一个明确sharp partition子块，不以别的系数或profile
倒填目标。three high和one low中的用词只指这些原high/low子范围。
新证明所用冻结证据如下；文本按CRLF及lone CR转LF，不trim。

| 输入 | canonical SHA256 |
|---|---|
| [446 canonical sharp prefix](../../notes/446-uniform-prime-twists-on-the-original-gabor-frame.md) | `08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf` |
| [463原双侧高度](../../notes/463-two-sided-height-stability-for-original-fourth-words.md) | `6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90` |
| [原finite-band bridge](hybrid-one-three-finite-band-admission-research.md) | `bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f` |
| [complex sign gate](hybrid-three-high-one-low-nonalternating-gate-research.md) | `ce1e000572fc2eecb0fe99211c3120ac0b901fb42dd973064b8b041adc3174bd` |

只需446的zeta、conductor1 sharp-prime推论及同一fixed-gap
logarithmic-control [R]。先固定a=22/25>theta=7/8，再令T趋于无穷。
不需要全导子moving coefficients的附加准入或未知whole fourth有界。

## 2. 16个方向的准确物理支持

先固定一个actual有限词，将low放在末位；其他三个low位置仅在实际
有限矩阵中作迹循环，保持循环后的high次序。没有先循环物理迹。
对 p,q,r in R_t，h in R_s和epsilon_i in {+1,-1}，记

\[
 s_i=\varepsilon_i\log p_i,\quad
 S_j=s_1+\cdots+s_j,\quad S=S_4,
 \qquad(p_1,p_2,p_3,p_4)=(p,q,r,h).                      \tag{5}
\]

如果epsilon_1=epsilon_2或epsilon_2=epsilon_3，两个相邻high
同向跳的长度和严格大于L。因此相应raw physical四词准确为零，
给12个signatures。剩余四个signatures有high方向(+,-,+)或(-,+,-)。

先取(+,-,+)。当low方向为负时，逐项上下界是

\[
 \begin{aligned}
 S&=\log p-\log q+\log r-\log h,\\
 S&> (1-11/20-1/3)L=7L/60,\\
 S&< (22/20-1/2)L-\log2=3L/5-\log2.
 \end{aligned}                                          \tag{6}
\]

当low方向为正时，逐项上下界是

\[
 \begin{aligned}
 S&=\log p-\log q+\log r+\log h,\\
 S&> (1-11/20)L+\log2=9L/20+\log2,\\
 S&< (22/20-1/2+1/3)L=14L/15.
 \end{aligned}                                          \tag{7}
\]

另两个signatures将全部方向反转，位移是 (6)或(7)的负数。
因此所有四个交替high signatures的 **每一个原tuple** 都满足

\[
             7/60<|S|/L<14/15.                          \tag{8}
\]

这是应用任何均值估计前的tuple范围恒等约束，不是把近共振项删掉。
端点carrier alias位于S=±L，故亦与这些tuples有固定比例间隔。
物理五位置的其他支持限制继续保留在原phi因子中。

## 3. 原finite carrier核与不改变观测量的netgate

直接四次相乘零延拓平移，原physical四词的normalized trace为

\[
 \Big(\prod_{i=1}^4b_{p_i}\Big)K_d(S)\frac1L\int W(u)\,du,
 \quad W(u)=\phi(u)\phi(u+S)\prod_{j=1}^3\phi(u+S_j)^2,
                                                               \tag{9}
\]
\[
 K_d(S)=\frac{e^{i\lambda_+S}-e^{i\lambda_-S}}
                       {2id\sin(\pi S/L)},\qquad
 \lambda_+=T+(2d-1)\pi/L,\quad\lambda_-=T-\pi/L.        \tag{10}
\]

四个原负号的积为正。lambda_±是原floor d的实际endpoint，不替换为
连续height平均。选一个固定even kappa in C_c^infinity((-1,1))，
kappa=1于7/60<=|v|<=14/15，且在0的固定邻域为零。令

\[
 f_L(S)=\frac{\kappa(S/L)}{\sin(\pi S/L)},              \tag{11}
\]

在0与±L附近以零延拓定义。因为 (8)，在每个原tuple上将 (10)的
csc替换为f_L是准确相等，不新增标签、自由补偿或目标权重。
kappa仅用于表达该观测量已有的固定net位移gap。
记f_L(S)=f(S/L)，f固定smooth compactly supported，则

\[
 \|\widehat f_L\|_1=\|\widehat f\|_1=O(1),\qquad
 \int_{|\xi|>A}|\widehat f_L(\xi)|d\xi\ll(LA)^{-1}
 \quad(A\ge1).                                         \tag{12}
\]

第二式也可从||f_L''||_1=O(1/L)直接积分得到。
不存在另一个未付的near或±L dyadicalias子块。

## 4. 五个Fourier coordinates在应用canonical cancellation前一起分离

Fourier convention为hat g(xi)=int g(u)e^(-ixi u)du；固定2pi常数
吸入估计常数。原C²窗给g=phi或phi²时

\[
 \|\widehat g\|_1\ll\ell_0:=\log(2+L),\qquad
 \int_{|\xi|>A}|\widehat g(\xi)|d\xi\ll A^{-1}.
                                                               \tag{13}
\]

对 (9)中phi(u+S)、三个phi²(u+S_j)及 (11) **一同**Fourier分离。
保留phi(u)不展开。对固定u及五个Fourier coordinates，每个prime
只携一个自身的unit norm phase；p,q,r,h的四个sharp ranges始终独立。
例如phi²(u+S_j)只向前j个prime的height各加epsilon_i xi_j。
f_L的coordinate向四者各加epsilon_i xi_0。
共同endpoint相位e^{i lambda_± S}同样分别给每个prime
epsilon_i lambda_±。所以这是原tuple sum的准确有限重排。

没有先按netratio截取tuple后，套用错误的canonical卷积前缀。
所有共享窗依赖在移到单变量prefix估计之前已全部保留、分离。
总Fourier L¹费用O(ell_0^4)；u的归一化积分满足
L^-1 int|phi(u)|du<=1，不产生额外T或X。

### 4.1 原carrier的高height主区

当五个coordinates均|xi|<=T/100时，每个prime的实际height是
epsilon_i(lambda_±+至多五个signed coordinates)。因此其绝对值在
J=[T/2,3T]内；对T充分大，原floor endpoint也包含在内。
446给原sharp prime前缀

\[
 \sum_{p\le Y}\frac{\log p}{\sqrt p}p^{it}
 \ll_aY^{a-1/2}\log^2(2Y(3+|t|))
       +\frac{\sqrt Y}{1+|t|}+\log^2(2Y).                \tag{14}
\]

principal峰与prime-power difference先保留；在本区才吸收。
每个thin-high sum是X^(11/20)与X^(1/2)两个sharp前缀之差。
对b归一化后分别有q_t<<X^((11/20)(a-1/2))L，
q_s<<X^((1/3)(a-1/2))L。由 (10)、(12)、(13)，高height主区为

\[
 \ll\frac{q_t^3q_s}{d}\ell_0^4
 \ll X^{-\eta}L^3\ell_0^4,\qquad
 \eta=1-(a-1/2)(3\cdot11/20+1/3)=739/3000.             \tag{15}
\]

这是对原物理trace整个tuple聚合的signed估计，不是在一个依赖prime
标签的error上再独立套canonical消去。

### 4.2 包含tau≈0 principal峰的整个ghost区

至少一个coordinate |xi|>T/100的union，由 (12)、(13)得Fourier
质量O(ell_0^4/T)。其余coordinates只取已经证明的L¹ norm，
四个prime sums使用原全height absolute mass

\[
 m_t\ll X^{11/40}/L,\qquad m_s\ll X^{1/6}/L,
 \qquad m_t^3m_s\ll X^{119/120}/L^4.                    \tag{16}
\]

由 (10)的真实1/d，全部ghost normalized费用为

\[
 \ll\frac{m_t^3m_s}{dT}\ell_0^4
 \ll X^{-121/120}L^{-5}\ell_0^4=o(1).                   \tag{17}
\]

该union包括所有coordinates互相抵消、高度靠0、正负prefix及principal
大峰；不在此区使用 (15)。原C²尾足够，没有假定原窗Schwartz。
由 (15)–(17)及十二个物理零signatures，整个rawphysical四词为o(d)。

## 5. 三个内部P及raw/good回到实际矩阵

complex sign gate稿§2–4的双方泄漏和raw/good恢复对每一个signature
均成立。这里总cap指数为s=119/60。它们具体给

\[
 \begin{aligned}
 &d^{-1}|\operatorname{Tr}(C_t^{\varepsilon_1}
 C_t^{\varepsilon_2}C_t^{\varepsilon_3}C_s^{\varepsilon_4})
 -\operatorname{Tr}(E^*B_t^{\varepsilon_1}
 B_t^{\varepsilon_2}B_t^{\varepsilon_3}B_s^{\varepsilon_4}E)|\\
 &\hspace{15mm}\ll X^{-739/3000}L^4+X^{-241/120}L^{-5}.
 \end{aligned}                                          \tag{18}
\]

证明顺序不可省略：rawactual与goodactual通过463双packet尾比较；
goodactual与goodphysical通过ell_i和ell_i*的六项两次crossing比较；
goodphysical再通过反向伴随链和suffix链的两侧bad guard回到rawphysical。
这里m乘子界是全height，q乘子界仅goodband，不把P与1_J交换。
第一个误差来自Lq_t³q_s/d，第二个来自T^-2m_t³m_s/d。
没有以未知全high fourth付款，也没有删除原有限carrier。

将16个signatures相加，(15)的ell_0^4最终小于L，得到一个明确版本

\[
 \frac{|\operatorname{Tr}(C_t^3C_s)|}{d}
 \ll X^{-739/3000}L^4
     +X^{-121/120}L^{-5}\ell_0^4
     +X^{-241/120}L^{-5}=o(1).                           \tag{19}
\]

另外三个low placements在实际finite trace中循环相等，所以其整个
capped31 coefficient也是4Tr C_t³C_s=o(d)。这里首先证明实际对象，
没有假设不同placement的物理trace可以自由循环。

## 6. 具体新增与保留范围

本次证明整个capped31子块，包含重复和distinct标签，并以真实range
sum付款；未将重复标签预算再次加入最终常数。它补足前一sign gate稿
在这个 **更小**范围里剩余的四个交替signatures。
原low的(X^(1/3),X^(1/2)]部分、原high的(X^(11/20),X]部分仍在原
whole31中保留，未在此付款。扩大caps时 (8)的fixedgap可以消失，
product near、alias或internalP的新误差必须另证。

量词：先固定原profile、[R] theta、fixedgap a=22/25及 (4)的两个
指数，再令T趋于无穷。常数不依赖当前prime、carrier row、Fourier
coordinates或T。没有新增movingmask准入、uniform family桥或新无零
边界。原467的q/k联合条件和完整四迹比例主预算仍未闭合。
