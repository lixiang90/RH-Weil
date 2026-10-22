# 素数幂累计误差的完整恒等式与原费用准入

2026-10-22。沿577的一个独立分支；本恒等式／费用核查本身不增数学轮，整轮候选联检是否准入由root统一结算。本文只核一个具体候选：先抵消PNT主项，再以有符号累计误差分部积分，能否独立支付实际负部修补。结论是恒等式合法，但现有PNT绝对包络不能支付；平方根包络作为经典全局前件已是RH责任。没有新的经典正号或成长净后果。

## 1. 冻结对象及必须保留的项

使用[577](../../../notes/577-full-gamma-positive-repairs-and-independent-budget-gap.md)及其[最终root收据](../gamma-retaining-positive-approximation/root-consumption-scope.json)的同一对象：

\[
 W_\zeta=W_\Gamma+H-P,\quad H=2\cosh(u/2)du,\quad
 P=\sum_{n=p^k\ge2}\Lambda(n)n^{-1/2}(\delta_{\log n}+\delta_{-\log n}),
\]
\[
 G_R=W_\Gamma+\phi_R(H-P),\quad g_R=\widehat G_R,
 \quad q_R=(-g_R)_+,\quad c_R=\|q_R\|_\infty,
 \quad m_R=(2\pi)^{-1}\|q_R\|_1.
\]

完整\(\Gamma(t)=\Re\psi(1/4+it/2)-\log\pi\)及577固定FP/contact不变。\(\phi_R(u)=\phi(u/R)\)是既定实偶、非负、正型光滑窗，支撑于[-R,R]；所有端点jets为0。R是算术截断，不是源半窗L。物理源仍\(r=e^{u/2}f\)，全部complex原du／zero-extension Dlog域；405真实非compact关系仍在\(\mathcal S_{\exp}\)。

## 2. 先扣主项的精确Stieltjes恒等式

为免与digamma的\(\psi\)混淆，记\(\Psi(x)=\sum_{n\le x}\Lambda(n)\)，包括全部proper powers。对u≥0定义

\[
 E(u)=\Psi(e^u)-e^u+1,\qquad A(u)=e^{-u/2}E(u).
                                                        \tag{1}
\]

\(E(0)=0\)，原点无原子；每个有界区间E为BV。\(+1\)是固定下端正规化，不是可调有限部分。正半轴上

\[
 dE(u)=d\Psi(e^u)-e^u du,
 \qquad (H-P)|_{u>0}=e^{-u/2}du-e^{-u/2}dE(u).             \tag{2}
\]

因此对所有实t，严格有

\[
 \begin{split}
 g_R(t)&=\Gamma(t)+J_R(t)+S_R(t),\\
 J_R(t)&=2\int_0^R\phi_R(u)e^{-u/2}\cos(tu)du,\\
 S_R(t)&=2\int_0^R A(u)
 \left[\left(\frac{\phi'(u/R)}R-\frac{\phi(u/R)}2\right)\cos(tu)
       -t\phi(u/R)\sin(tu)\right]du .
 \end{split}                                             \tag{3}
\]

证明只需将\(-2\int_0^R\phi_Re^{-u/2}\cos(tu)dE\)分部积分；上端窗为0，下端E为0，故没有遗漏端点。若采用\(\Psi(e^u)-e^u\)而不加1，下端必须另留常数，不能默删。所有prime-power原子、两个pole对应的\(e^{u/2}+e^{-u/2}\)均已进入(2)，不是只抵一个pole后换目标。WΓ原封不动，没有新contact。

\(J_R\ge0\)：它是\(\phi_R(u)e^{-|u|/2}\)的Fourier变换，两因子均正型；等价地是非负\(\widehat\phi_R\)与\((t^2+1/4)^{-1}\)的卷积。对固定t，\(J_R\to(t^2+1/4)^{-1}\)。这是一个可独立保留的正块；Γ+J_R并不因此处处非负，剩余S_R的符号不能丢。

## 3. 现有绝对累计误差实际给什么

定义原数据可算量

\[
 I_R=\int_0^R|A(u)|\phi(u/R)du,\quad
 I'_R=\int_0^R|A(u)|\,|\phi'(u/R)|du.
\]

直接而合法的界为

\[
 |S_R(t)|\le2(|t|+1/2)I_R+2I'_R/R,\quad
 q_R(t)\le[2(|t|+1/2)I_R+2I'_R/R-\Gamma(t)-J_R(t)]_+.
                                                        \tag{4}
\]

这只是一个绝对包络。它没有S_R相对于Γ／pole正块的方向信息。

旧555已经消费的无条件PNT给：每个先固定ε>0有有限Cε，使\(|\Psi(x)-x|\le\epsilon x+C_\epsilon\)对全部x≥1成立。代(4)得到

\[
 I_R+I'_R\ll_\phi\epsilon e^{R/2}+C_\epsilon+1.            \tag{5}
\]

这里先固定ε再R→∞，不能任取未知费用的ε(R)使右端消失。即使只看固定t，这个包络也没有给趋0的误差。它不是\(I_R\)或q_R发散的必要下界，更不是RH反证。

为检验更精细的现成输入，核了Johnston–Yang [2204.01980v2，Theorem 1.1](https://arxiv.org/html/2204.01980v2)：该文给无条件形如\(x(\log x)^b e^{-c\sqrt{\log x}}\)的\(|\Psi(x)-x|\)上界。它只作为包络类型对照；本次没有将其全部原证明重新消费为新设施，也不优化暂停的无零区域。代入(4)至多给

\[
 I_R+I'_R\ll 1+(1+R)^b\exp(R/2-c\sqrt R)                 \tag{6}
\]

的一类增长upper，实际窄支撑窗可有更好的R系数，但仍不产生signed下界或已付的小量；不将这个upper当实际费用的必要lower。所有\(xe^{-o(\log x)}\)包络面临同一加权尺度问题。

若**假设**全局平方根包络\(|\Psi(x)-x|\le C\sqrt x(1+\log x)^a\)，则

\[
 |A(u)|\ll(1+u)^a,\quad
 |S_R(t)|\ll(1+|t|)(1+R)^{a+1}.                           \tag{7}
\]

以a=2为例，直接三角界为\(O((1+|t|)R^3)\)，仍没有经这一候选算出q的小量。不能据此宣称“平方根误差不能推出经典RH”：在经典完整解析包中，全x的平方根／\(x^{1/2+o(1)}\)误差本来就与RH等强，见[Tao本人对式(6)及其逆向的说明](https://terrytao.wordpress.com/2013/07/19/the-riemann-hypothesis-in-various-settings/)。此处失败的是将绝对包络经(4)运输成实际修补费用的论证，绝非否定那个已知等价。

有限高度范围内验证平方根包络，也只支付对应有限u区间；没有任意cofinal R的实际q／尾费。不得把有限验证当全局独立前件。

## 4. 原du／Dlog与频高费用

分部积分的t因子是实际费用，不能藏进常数。577只给q_R负区在有效但可能极大的\([-T_R,T_R]\)内；(4)在全部该区间的最差t费为T_R。有限t带改善也不支付带外负部质量，\(m_R=(2\pi)^{-1}\int q_R\)尤其需要完整频高尾。

相同损失可在源端看出。令\(h=r*r^*\)，\(h_e(u)=(h(u)+h(-u))/2\)；对平方h_e为实函数。由(2)有

\[
 \begin{split}
 (\phi_R(H-P))(h)
 &=2\int_0^R\phi_Re^{-u/2}h_e du\\
 &\quad+2\int_0^R A(u)
 [ (\phi'_R-\phi_R/2)h_e+\phi_Rh'_e ]du .
 \end{split}                                             \tag{8}
\]

compact smooth源可逐项计算。若直接用\(\|h'_e\|_\infty\le\|r'\|_2\|r\|_2\)，则付的是H¹型源费用，不能当原du或Dlog统一费。取\(r_T(u)=e^{iTu}r_0(u)\)在同一固定窗，原du不变，Dlog范数平方仅\(\asymp\log(2+T)\)，导数费却\(\asymp T\)。因此此分部积分本身没有付原域全源统一norm。

若回到原signed measure的TV来取消t，则恢复577的\(O(e^{R/2})\)粗费／555的原prime行费；那是已付的旧绝对费用，不能报新signed正号。Γ在原du无界但原Dlog合法；(8)没有改变这一事实。

577已付的固定源窗比较仍原样有效：

\[
 |Q_{\widetilde V_R}(r)-Q_\zeta(r)|
 \le[D_L/R^2+\min(c_R,2Lm_R)]\|r\|_2^2,\quad
 D_L\ll(1+L^2)e^L.                                      \tag{9}
\]

本候选未改善其中实际修补那一项。Γ协同\(\mu_R\)的全线du／Fourier-L¹为R⁻²已在577支付，不能再次算成S_R的算术消失预算。L成长须保全部D_L与实际q_R费用；(4)也没有给L随R变化的统一新范围。

## 5. 连续正反例：PNT本身不能选择正号

采用562已付的真正positive continuous primitive族，不更换native Γ=0与完整双pole。令α+β=1，αβ=c，

\[
 d\Psi_c(e^u)=(e^u+1-e^{\alpha u}-e^{\beta u})du,
\quad E_c(u)=u-\frac{e^{\alpha u}-1}{\alpha}
                   -\frac{e^{\beta u}-1}{\beta}.          \tag{10}
\]

这是把完整prime-power密度\(u\,d\Pi_c\)积分得到的累计误差；全部Euler repeats都在其中。把E_c代(3)严格恢复\(\widehat{\phi_RW_c}\)。

- 正段c=5/16：α,β=1/2±i/4，\(W_c=2\cos(u/4)du\)，hard q_R=0。其\(\Psi_c(x)-x=O(\sqrt x+\log x)\)可直接从(10)验证。
- 负段c=3/16：α=3/4、β=1/4，\(W_c=2\cosh(u/4)du\)，\(\Psi_c(x)-x=O(x^{3/4})\)，仍满足真正PNT以及强于\(xe^{-c\sqrt{\log x}}\)的某个误差包络，但在577的实际compact双polezero负源上，正修补不能消失。

因此primitive正性、完整对偶和PNT主项／通常次幂误差并不足以给Weil正号。该负例没有平方根误差，不拿它反驳经典平方根等价；也不往Γ=0模型 graft经典Γ。两段的零点只在事后核模型，不参与系数选择。

## 6. 真函数域、405与537

真曲线的累计点数亦可写成离散Stieltjes／summation-by-parts式，但原模型的pole是完整周期lattice，不能用经典H连续密度替代。保全部returns／aliases后的原Weil分布

\[
 W_C=\ell\sum_{n\in\mathbb Z}\operatorname{Tr}(U^n)\delta_{n\ell}
\]

由已经独立支付的同对象H／RR正极化给正型，故\(\phi_RW_C\)也正型、hard q_R=0。绝对点数误差包络不是这个混合Gram正号的原证明；真正新输入在函数域来自几何极化／RR及其与trace的身份。只把其数值平方根误差移到一般g分布，未构造这个输入。

405的\(p=(D^2-1/4)H_0\ne0\)、所有固定平移及\(B_\zeta(p,s)=0\)均未被(1)–(8)改变。577各正层仍在高频有严格正密度，故\(Q_{\widetilde V_R}(p)>0\)，exact全关系仍失败。对每固定强源，旧577式(17)的\(O(R^{-2})\)尾是合法已付费用，加上实际q费用后才谈近似消去；(4)没有消除修补责任。553全线Pan稠密门也未解除。

537的\(L_0=17/16\)固定窗全complex非根仍有无条件
\(Q_{\widetilde V_R}\ge(\tau-D_{L_0}/R^2)\|r\|_2^2\)最终为正。这不是本候选的新后果，不能升级为任意成长窗正性。

## 7. 准确的未付signed责任与停止

(3)将所需signed估计写得很具体：须从实际累计误差与全部窗导数出发证明

\[
 S_R(t)\ge-\Gamma(t)-J_R(t)-\epsilon_R(t)
\]

并独立支付\(\|\epsilon_R\|_\infty\to0\)或\(\|\epsilon_R\|_1\to0\)等足够原费用。如果只把\(\epsilon_R=(-g_R)_+\)或“满足该式的最小误差”当定义，便完全回到577：此family中\(K_R\to0\)于D′、c_R→0、m_R→0都等价完整Weil正性／RH。正型闭锥只消费已经证明的极限，不创造这项signed输入。

本次实际得到的是一种完整、端点与原norm透明的候选重写及失败定位；Stieltjes分部积分、旧PNT、原prime行费、Γ小误差、正型闭锥均扣旧。没有新独立实际signed下界、原费用小量或成长coverage，strong-old542＋555→557 whole leading4/5负惯性上预算、actual core／coupling／Ξ均不变。

停止这一累计绝对误差入口，不调截断／频网格、不续全局平方根前件的新名称。它不排除未来真正给方向信息的算术相位相关、源依赖同对象容量或联合非局部恒等式；重新准入需要可核原数据输入与实际q原费用净后果。
