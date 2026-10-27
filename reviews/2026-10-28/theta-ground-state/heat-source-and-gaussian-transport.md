# 固定theta基态谱：原源费用、条件热渐近与共同Gaussian运输

2026-10-28；C049，G20261027／1793085111／原0c4f。unit_modularity独占支持稿。已读STATE、README、check→show、Goal／前沿、D20261028P、新合同、原定义及05251a4c…准入审查，并读566全文及其完整目标原稿。本稿仅本地推导，不web／PDF／数值，不改STATE、cadence或Git；不混用另份prime反演稿。

**消费状态：以下以(C)为明示条件。** 原Dirichlet形式谱设施及两项count由另一独占稿承担，root对齐前，本稿不把候选问号式当定理。这里独立闭合从(C)到原源费用、严格两项heat、完整目标比较及D′→Gaussian的合法桥。新净后果若最终成立，只否定这一个固定谱规则的完整身份；旧Γ热公式不是本稿新结果。

## 1. 固定对象、条件及倍数

算子坐标x∈(0,∞)；Hθ为405的全整数theta源，固定原
\[
 A_\theta=-D_x^2+H_\theta''/H_\theta,
 \quad q_\theta[f]=\int_0^\infty|f'-(H_\theta'/H_\theta)f|^2dx,
 \quad f(0)=0.
\]
物理源变量始终u∈R、r=e^(u/2)f；x不与u认同。冻结以下实际前件：Aθ为该形式的非负自伴表示，compact resolvent，无零模；λj>0按全部重数列出。令
\[
 \mathcal N(T)=N_\theta(T^2)=\#\{j:\sqrt{\lambda_j}\le T\}.
\]
本腿需要的计数条件是
\[
 \tag{C}
 \mathcal N(T)=\frac{T}{2\pi}[\log(T/\pi)-1]+R(T),
 \quad R(T)=o(T).
\]
若另稿付到\(|R(T)|\le C\sqrt T\log(2+T)\)，下面同时给出相应定量余项。任何仅leading TlogT、未控制线性T误差的结果都不足以消费本结论。

记μj=√λj，
\[
 \nu_T=\sum_{\mu_j\le T}(\delta_{\mu_j}+\delta_{-\mu_j}),
 \quad M_T=\nu_T(\mathbb R)=2\mathcal N(T),
 \quad W_T(u)=\int e^{-i\tau u}d\nu_T(\tau).
 \tag{1}
\]
每个半线本征值的±频率各出现一次，零模已由前件排除；不改sector、不再除2。Fourier \(\widehat r(\tau)=\int r(u)e^{-i\tau u}du\)，Plancherel为dτ/(2π)。式(1)没有额外1/(2π)谱质量：逆Fourier所对应的是hat W_T=2πν_T。

## 2. 每层fullcomplex费用；不宣globaldu

对全部complex r,s∈L¹，定义
\[
 B_T(r,s)=\sum_{\mu_j\le T}
 [\widehat r(\mu_j)\overline{\widehat s(\mu_j)}
 +\widehat r(-\mu_j)\overline{\widehat s(-\mu_j)}].
\]
它与W_T(r*s*)一致，s*(u)=overline{s(−u)}，且
\[
 |B_T(r,s)|\le M_T\|r\|_1\|s\|_1,\qquad Q_T(r)\ge0.
 \tag{2}
\]
这里保留全部complex，而不是仅实偶源。若r,s支持在I_L=(−L,L)，零延拓后
\[
 |B_T(r,s)|\le2LM_T\|r\|_{du}\|s\|_{du},\qquad
 Q_T(r)\le4L\mathcal N(T)\|r\|_{du}^2.
 \tag{3}
\]
对原zero-extension Dlog能量
\(E_{\log}(r)=\int\log(2+|\tau|)|\widehat r(\tau)|^2d\tau/(2\pi)\)，
\[
 Q_T(r)\le\frac{2LM_T}{\log2}E_{\log}(r).
 \tag{4}
\]
这是fixed L、fixed T的原费用；不把growth T的质量并入常数。对S_exp、a>0，令\(p_{a,j}(r)=\sup e^{a|u|}|r^{(j)}(u)|\)，有
\[
 \|r\|_1\le2p_{a,0}(r)/a,\quad
 |B_T(r,s)|\le\frac{4M_T}{a^2}p_{a,0}(r)p_{a,0}(s).
 \tag{5}
\]
原physical map的强源费用须按r本身计，不把bare f的范数无声代入。

只要该层含一个原子μ，原全线global du界便不成立：取∫φ≠0的compact smooth φ，\(r_R(u)=R^{-1/2}e^{i\mu u}\phi(u/R)\)，其L²范数固定而\(|\widehat r_R(\mu)|^2=R|\int\phi|^2\)。这不妨碍(2)–(5)，也不妨碍D′策略；逐层无需exact消405。

## 3. 从计数到真实温和分布与fixed源极限

(C)给\(\nu([-Y,Y])\le C(1+Y)\log(2+Y)\)，其中\(\nu=\sum_j(\delta_{\mu_j}+\delta_{-\mu_j})\)。Stieltjes分部积分给p>1、Y≥1时
\[
 \int_{|\tau|>Y}(1+|\tau|)^{-p}d\nu(\tau)
 \le C_pY^{1-p}\log(2+Y).
 \tag{6}
\]
故ν为正温和测度，\(W_\theta(h)=\int\widehat h(\tau)d\nu(\tau)\)定义S′分布，且W_T→Wθ于S′，从而于D′。例如
\[
 |W_\theta(h)|\le C\sup_\tau(1+|\tau|)^3|\widehat h(\tau)|.
 \tag{7}
\]
不是声称(1)的cos级数逐点收敛。

对每先fixed r,s∈Cc∞或S_exp，integration by parts给
\[
 |\widehat r(\tau)|\le\min(\|r\|_1,\|r^{(m)}\|_1|\tau|^{-m}).
\]
取整数m≥1，(6)支付B_T的全部谱尾，误差至多
\[
 C_m\|r^{(m)}\|_1\|s^{(m)}\|_1
       T^{1-2m}\log(2+T),\qquad T\ge1.
 \tag{8}
\]
S_exp中导数L¹费由相应p_a,m支付。于是得到全部fixed complex源的极限Bθ和正Qθ；不把这一逐源／强拓扑结论扩为所有global L²或成长窗／moving源统一费。仅这些收敛不识别完整Wζ。

## 4. 两项热迹：独立核±、ψ与余项

由谱质量及(C)的多项式增长，对每个先fixed t>0有普通热迹有限，且
\[
 \Theta_\theta(t)=\int e^{-t\tau^2}d\nu(\tau)
 =2\sum_j e^{-t\lambda_j}
 =2\operatorname{Tr}e^{-tA_\theta}
 =4t\int_0^\infty T e^{-tT^2}\mathcal N(T)dT.
 \tag{9}
\]
最后一步为Stieltjes分部积分，λ>0给下端质量0，Gaussian与count给上端0。它是普通trace，不是regularized trace或fixed-window Weil算子的热迹。

把(C)主式写成aTlogT+bT，a=1/(2π)，b=−(logπ+1)/(2π)。所需积分为
\[
 \int_0^\infty T^2e^{-tT^2}dT=\frac{\sqrt\pi}{4t^{3/2}},
\]
\[
 \int_0^\infty T^2\log T\,e^{-tT^2}dT
 =\frac{\sqrt\pi}{8t^{3/2}}[\psi(3/2)-\log t].
 \tag{10}
\]
独立核ψ常数：Gamma duplication的log导数在z=½给\(\psi(1/2)=\psi(1)-2\log2=-\gamma_E-2\log2\)；recurrence给\(\psi(3/2)=\psi(1/2)+2\)。所以(9)主项为
\[
 \boxed{\Theta_\theta(t)=
 \frac{\log(1/t)-\gamma_E-\log(4\pi^2)}{4\sqrt{\pi t}}
       +\mathcal E_\theta(t)}.
 \tag{11}
\]
这里log4π²而非log16π²，源于固定count的线性T项；不是舍去±或改变Dirichlet倍数。

严格余项来自\(4t\int T e^{-tT^2}R(T)dT\)。count只在大T给出，低T紧段的有界差给O(t)，无需在小T假用渐近式。若\(R(T)=O(\sqrt T\log(2+T))\)，变量y=√t T给
\[
 \mathcal E_\theta(t)=O(t^{-1/4}\log(2+1/t)),\quad t\downarrow0.
 \tag{12}
\]
若只付R=o(T)，先对任意ε选固定Tε使|R|≤εT，再拆有限head和tail，给\(\mathcal E_\theta=o(t^{-1/2})\)。所以两种前件均足以认证(11)的线性热常数；仅R=O(T)不足。

## 5. 同一compact crop合法连接D′与非compact Gaussian

取固定偶0≤χ∈Cc∞、χ=1于[−1,1]，记χ_R(u)=χ(u/R)，\(h_{R,t}=\chi_R k_t\)，\(k_t(u)=(4\pi t)^{-1/2}e^{-u^2/(4t)}\)。对每先fixed t>0，h_R,t→k_t于S_exp，因Gaussian压住全部固定指数权及有限阶cutoff导数。不能只凭D′收敛便代入k_t；以下分别核两侧。

**θ谱侧。** h_R,t→k_t于Schwartz，(7)给
\[
 W_\theta(h_{R,t})\longrightarrow\int e^{-t\tau^2}d\nu
 =\Theta_\theta(t).
 \tag{13}
\]
同一误差由ν_T≤ν对所有T的绝对谱配对控制。全cutoff谱侧也是\(W_T(k_t)=2\sum_{\mu_j\le T}e^{-t\lambda_j}\uparrow\Theta_\theta(t)\)，其合法性独立来自count和Gaussian，不来自D′测试许可。

**完整Wζ侧。** 保旧566／578原表达
\[
 W_\zeta=W_\Gamma+2\cosh(u/2)du
 -\sum_{n=p^k\ge2}\Lambda(n)n^{-1/2}
              (\delta_{\log n}+\delta_{-\log n}).
 \tag{14}
\]
Γ multiplier满足\(|\Gamma_\infty(\tau)|\le C\log(2+|\tau|)\)。对S_exp中的g，用\(|\widehat g|\le\min(\|g\|_1,\|g''\|_1/\tau^2)\)给
\[
 |W_\Gamma(g)|\le C(\|g\|_1+\|g''\|_1).
 \tag{15}
\]
这是完整Fourier multiplier定义，保FP及指定contact，没有把穿孔核当通常测度。pole项由\(\int e^{|u|/2}|g|du\)控制；pp项由
\[
 2p_{1,0}(g)\sum_{n\ge2}(\log n)n^{-3/2}<\infty
 \tag{16}
\]
控制。故Wζ在S_exp上连续，有限组p_1,0、p_1,2已足以控制这里的三项。具体对共同Gaussian crop，pole尾和全部pp尾都趋0；pp原尾为\(\sum_{n>e^R}\Lambda(n)n^{-1/2}e^{-(\log n)^2/(4t)}\)，Gaussian压住全部n，非只prime head。于是
\[
 W_\zeta(h_{R,t})\longrightarrow W_\zeta(k_t)
 =2e^{t/4}+\frac1{2\pi}\int e^{-t\tau^2}\Gamma_\infty(\tau)d\tau
 -\frac2{\sqrt{4\pi t}}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
             e^{-(\log n)^2/(4t)}.
 \tag{17}
\]
双pole恰给2e^(t/4)，没有删掉奇pole；所有proper powers同式保留。式(17)正是旧566(13)，不是另一个Γ热对象。

因此，**若假设**W_T→Wζ于D′，唯一极限先给Wθ(h_R,t)=Wζ(h_R,t)对每fixed R,t。再对同一crop令R→∞，(13)、(17)推出\(\Theta_\theta(t)=\Theta_\zeta(t)\)对每个t>0。顺序是T∞固定compact test、R∞固定t、最后才t↓0；无未付的joint R(T,t)交换。

若需要从实际compact卷积平方而非一般compact测试看同一桥，取g_t=k_(t/2)，g_R,t=χ_R g_t；则g_R,t→g_t于S_exp。加权L¹卷积估计
\[
 p_{a,j}(f*g)\le\|e^{a|\cdot|}f\|_1p_{a,j}(g)
 \le2p_{a+1,0}(f)p_{a,j}(g)
\]
给\(g_{R,t}*g_{R,t}^*\to g_t*g_t^*=k_t\)于同空间。两侧上述连续性同样适用。此操作只得到配对差异，不给经典负源。

## 6. 与已付完整目标比较及最终依赖范围

旧566(15)已无RH地付出
\[
 \Theta_\zeta(t)=
 \frac{\log(1/t)-\gamma_E-\log(16\pi^2)}{4\sqrt{\pi t}}+O(1).
 \tag{18}
\]
仅作规范复核：旧Γ对数主项的Gaussian积分为\([\psi(1/2)-\log t-2\log(2\pi)]/[4\sqrt{\pi t}]\)，以上独立核出的ψ(1/2)正给(18)；不再领取这个已付Γ结果。与(11)的常数方向为log16π²−log4π²=log4。因此在(C)及原谱设施下
\[
 \boxed{\Theta_\theta(t)-\Theta_\zeta(t)
 =\frac{\log2}{2\sqrt{\pi t}}+o(t^{-1/2})},
 \quad
 \lim_{t\downarrow0}\sqrt t(\Theta_\theta-\Theta_\zeta)
 =\frac{\log2}{2\sqrt\pi}>0.
 \tag{19}
\]
若使用较强count余项，o项可换成\(O(t^{-1/4}\log(2+1/t))\)，已吸收旧目标O(1)。系数不依赖未知ζ根或RH，也不重新证明Γ结果。

由第5节，(19)严格排除固定Wθ,T→完整Wζ于D′，并排除其all-time普通热身份。还可明确落到**一个真正fixed compact physical源**：先固定足够小t>0，使δt=Θθ(t)−Θζ(t)>0；取\(r_{t,R}=\chi_R k_{t/2}\)。第5节的共同卷积运输给
\[
 Q_\theta(r_{t,R})-Q_\zeta(r_{t,R})\longrightarrow\delta_t.
 \tag{20}
\]
再选一个有限R使此差>δt/2，此后r=r_t,R完全固定，\(f=e^{-u/2}r\)亦为合法compact physical前像。最后由(8)取谱cutoff T足够大，得
\[
 Q_T(r)-Q_\zeta(r)>\delta_t/4>0.
 \tag{21}
\]
所以不消失差可由真正compact卷积平方r*r*见证，不需要非法非compact测试。选择顺序为小t先固定、有限R随后固定、最后T∞；没有优化R、移动源反测或声称此源在旧17/16窗内。式(21)没有给Qζ(r)<0：两种型可以同时为正而数值不同。改变Dirichlet sector、x尺度、H幂、倍数、常数或另加补偿不在本合同内。

**付费／未付。** 本腿支付的是：(C)下的±规范、每层原L¹／strong／fixed窗du-zeroextensionDlog费；fixed源及分布极限；精确两项heat和余项；共同Gaussian／compact平方运输。原形式闭包、无零模、compact resolvent、全n势尾与严格(C)仍由另一稿/root对齐，不能由本腿倒推。即使其闭合，新增也仅是这个实际全整数theta谱规则的完整反测。10-14旧H尾、566旧目标、旧图失败均不重报；这里没有将Aθ与旧图或原非局部E_g认作同一算子。553不被强加为每层Pan义务。

不推Qζ负、不推RH反例，不改whole leading4/5负惯性UPPER、585必要费或actual corecross；不证明所有confining／relative／强源谱方法失败。root未闭(C)前本稿保持条件结果；root是否统一计轮及合同结算由实际前件消费决定。

## 7. 最终输入绑定

作者已冻结的实际谱输入为[spectral-domain-and-two-term-count.md](spectral-domain-and-two-term-count.md)，9724 bytes，LF SHA-256 `2a233e8b26962158d3fc7f035787c4b9a27d534919986fec398c1524d9bd879d`。其§1／§7明确交付本稿所需原Dirichlet域、λ1>0、compact resolvent及按≤／重数一次／无±2的计数；§5–6给到同一(C)的线性T项，余项为Oθ(√T(1+logT))，故本稿可使用较强的(12)。本稿已实际读取这些陈述及必要末端上下文；谱证明仍由该独占稿、fresh与root负责，不以本热推导反向认证其前件。

旧完整目标绑定`notes/566-source-closed-forms-and-full-weil-heat-trace-tests.md`，10582 bytes，LF SHA-256 `004f5438c918373e0ead73c0011ffb3883ef872c4977e356911dd910da177053`，实际使用(13)、(15)及其原源角色。准入审查7703 bytes／LF `05251a4c6fa794cb1b2361eabe0af7874b3afc6fcab6b5fb9137737acfdeef1e`只授权本首门，不充当(C)证明。本稿仍按“若消费这份谱输入，则推出(19)–(21)”交付；root统一前件消费／分类／结算保持独立状态，不在此无声升级。
