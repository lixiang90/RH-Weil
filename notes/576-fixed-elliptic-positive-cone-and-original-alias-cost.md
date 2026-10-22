# 576：固定椭圆曲线生成正分布锥与原Dlog alias费用

2026-10-22；C039，一完整研究轮候选。同G20261014／冻结0c4f。函数域正性、563／566具体H及全递推为输入。本轮新增合成是：**一个固定真实曲线的基变换和centered缩放，保全部returns，稠密生成实偶正型分布锥；其向每个cosine证书的全部fixed窗原Dlog误差恰为1/log阶。**不证明经典目标属于该锥，不报独立经典容量、whole或RH后果。

## 1. 独立输入和旧资产扣除

固定真实曲线
\[
 E/\mathbb F_5:y^2=x^3+x+1,\quad N_1=9,\quad
 P(T)=1+3T+5T^2,
\]
及已付
\[
 F=\begin{pmatrix}0&-5\\1&-3\end{pmatrix},\quad
 H=\begin{pmatrix}1&-3/2\\-3/2&5\end{pmatrix}>0,
 \quad F^THF=5H,\quad U=F/\sqrt5.                          \tag{1}
\]
完整各次点数来自已证明有理性和递推，不从有限点数拟合。函数域有效性／RR的正号来源归[Milne／Weil原证明](https://www.jmilne.org/math/xnotes/pRH.pdf)、567；具体全周期实现见563／566。

562的连续正族已有cos核，再用标准缩放／Bochner即可得到解析正锥；正型锥闭、unscaled q≥2在(0,log2)的support gap、经典Γ非Radon也已付。本轮不重计这些。新处在于将一个固定真实函数域族接通该解析锥，并付下面全部原范数误差；不声称世界文献首次。

以下\(\widehat r(t)=\int r(u)e^{-itu}du\)，\(r^*(u)=\overline{r(-u)}\)，\(B_W(r,s)=W(r*s^*)\)，\(Q_W(r)=B_W(r,r)\)。物理\(r=e^{u/2}f\)，先用compact complex源，再按指定范数延拓。

## 2. 实际基变换与完整centered dilation

由(1)可写\(\operatorname{Tr}U^n=2\cos(n\theta)\)。\(\theta/(2\pi)\)无理：若\(e^{i\theta}\)为root of unity，则\(-3/\sqrt5=2\cos\theta\)为代数整数，其平方9/5亦然，与有理代数整数必为整数矛盾。

实际基变换\(E_m=E/\mathbb F_{5^m}\)的Frobenius为F^m。置\(Q=5^m\)、\(L_m=m\log5\)，其完整分布为
\[
 W_m=L_m\sum_{n\in\mathbb Z}2\cos(mn\theta)\delta_{nL_m}.
                                                                  \tag{2}
\]
对a>0，定义
\[
 Z_{m,a}(s)=\zeta_{E_m}\bigl(\tfrac12+a(s-\tfrac12)\bigr),
 \quad h=aL_m,
 \quad W_{m,a}=a(\mathrm{dil}_a)_*W_m
       =h\sum_{n\in\mathbb Z}2\cos(mn\theta)\delta_{nh}.     \tag{3}
\]
Poisson给全部实线谱
\[
 \sigma_{m,a}=\sum_{k\in\mathbb Z}
   \bigl(\delta_{(m\theta+2\pi k)/h}
          +\delta_{(-m\theta+2\pi k)/h}\bigr),\quad
 W_{m,a}(r*r^*)=\int|\widehat r|^2d\sigma_{m,a}\ge0.          \tag{4}
\]
相位可取模，重合按multiplicity2，\(\widehat W=2\pi\sigma\)。这保留全部returns和全部aliases，未剪掉任何谱。

缩放也运输全部已知degree／pole项：原s=0,1变为
\[
 s=\tfrac12\pm\frac1{2a}+\frac{2\pi i k}{h},\quad k\in\mathbb Z.
                                                                  \tag{5}
\]
不能只把comb间距缩小而保持原pole。每个点是独立正模型；它们尚不是固定经典\(\mathcal D_\zeta\)纤维的点。对完整分布逼近而言，中间点可以改变标签；若要几何fixed-label比较，则(5)必须另修并证明正性。

## 3. 一个真实正实权g-prime系统的Euler检验

中心平移一般不自动保primitive非负。本族可直接验证：取m≥2、0<a≤1，令
\[
 A=Q^{(1+a)/2}\ge5,\quad B=Q^{a/2},\quad
 C=Q^{-(1-a)/2}\le1,\quad x=e^{-hs},
\]
则
\[
 Z_{m,a}(s)=\frac{1-2B\cos(m\theta)x+B^2x^2}
                    {(1-Ax)(1-Cx)},\qquad
 \log Z_{m,a}=\sum_{n\ge1}\frac{c_n}{n}x^n,
 \quad c_n=A^n+C^n-2B^n\cos(mn\theta).                     \tag{6}
\]
真正powers反演定义
\[
 b_n=\frac1n\sum_{d\mid n}\mu(d)c_{n/d},\qquad
 Z_{m,a}=\prod_{n\ge1}(1-e^{-hns})^{-b_n}                  \tag{7}
\]
于绝对收敛右半平面。因为B/A=Q^-1/2≤1/5，
\[
 c_1\ge3A/5,\quad c_n\ge23A^n/25\ (n\ge2),\quad
 c_k\le7A^k/5+1.
\]
对K=⌊n/2⌋≥1，所有proper除数阶≤K，且
\[
 \sum_{k=1}^Kc_k\le(7/4)A^K+K
       \le(39/20)A^K\le39A^n/100.
\]
故
\[
 b_1\ge3A/5>0,\qquad b_n\ge\frac{53}{100n}A^n>0
       \quad(n\ge2).                                      \tag{8}
\]
这给实际正实权primitive\(P_{m,a}=\sum b_n\delta_{nh}\)，完整powers\(\Pi=\sum_{n,k}b_n\delta_{knh}/k\)，其卷积指数给正g-integer测度。局部有限因h>0，所有Euler身份在右半平面绝对收敛，再由(6)给有理亚纯延拓。

实权b_n不必整数；不称它是普通整数重数的离散g-prime counting。finite正混合的分布也不自动对应通常整数零重数的整个determinant。这里消费的是一般分布型g系统／正源证书。

## 4. 固定真实E可逼近任意预定cos核

无理圆旋转给\(m_j\to\infty\)及
\[
 \delta_j=\operatorname{dist}(m_j\theta,2\pi\mathbb Z)>0,
 \qquad\delta_j\to0.
\]
这可由pigeonhole／continued fraction独立选择，不读取任何经典ζ零点。对预定γ>0，取
\[
 h_j=\delta_j/\gamma,\qquad a_j=h_j/L_{m_j}\to0.
\]
最终满足§3的m≥2、a≤1。于是精确
\[
 W_{m_j,a_j}=h_j\sum_n2\cos(\gamma nh_j)\delta_{nh_j}
       \longrightarrow 2\cos(\gamma u)\,du\quad\text{于D′}. \tag{9}
\]
对任意compact C¹测试φ，逐cell微积分给
\[
 \left|h\sum_n2\cos(\gamma nh)\phi(nh)
       -\int2\cos(\gamma u)\phi(u)du\right|
 \le2h(\|\phi'\|_1+\gamma\|\phi\|_1).                       \tag{10}
\]
γ=0时取h_j=√δ_j、a_j=h_j/L_m；有效频率δ_j/h_j=√δ_j→0，加上(10)给极限2du。

## 5. 完整正混合闭包的精确范围

令\(\mathcal C_E\)为m≥2、0<a≤1的(3)的**有限非负实权混合**，不抹平、不剪aliases。则
\[
 \boxed{\ \overline{\mathcal C_E}^{\mathcal D'}
      =\{\text{实偶正型分布}\}.\ }                         \tag{11}
\]
一侧由(4)和正型锥闭。另一侧由(9)给全部cos核在闭包；闭包仍为闭凸锥。Bochner–Schwartz将任意实偶正型分布表示为对称正tempered测度的Fourier逆：先截断谱尾，再把compact正测度正求积，即由有限正cos混合逼近。

尾部不是无条件丢掉：若\(\int(1+t^2)^{-N}d\sigma<\infty\)，对Schwartz测试的尾由\(\sup_{|t|>T}(1+t^2)^{N+1}|\widehat\phi(t)|\)及额外\((1+T^2)^{-1}\)控制；compact谱上的求积由Fourier测试连续性完成。可使离散测度保持统一多项式增长，得到S′进而D′收敛。也可用闭锥包含所有cos的闭包论证，避免未经证明的“可数测试逐点即全D′”跳步。

这给真实几何族的新覆盖定理，但不是首次证明解析cos锥普适。其方法含义很明确：**允许任意基变换、centered尺度及正实权混合后，目标属于这个闭包，已经不比完整Weil正型更窄。**经典Wζ的成员判定仍承担RH责任；不能再以“函数域正性已知”宣布成员判定自动成立。

**整数混合也不单独消除经典成员责任。**令\(\mathcal C_E^{\mathbb N}\)只允许有限非负整数混合。对已固定的经典完整Wζ，仍有
\[
 W_\zeta\in\overline{\mathcal C_E^{\mathbb N}}^{D'}
       \quad\Longleftrightarrow\quad RH.                    \tag{11a}
\]
反向由正锥闭及Weil判据；正向在RH前件下，用经典完整显式公式的整数重数零点对，将Wζ写为\(\sum_{\gamma>0}m_\gamma2\cos(\gamma u)\)。零点计数的多项式增长使其截断在S′收敛，每个有限整数cos和再由(9)逼近。经典中心值不为零；一般偶完成化若有中心零，其偶重数也可由整数倍2cos0表示。这是**conditional且等价**的消费，使用RH选频率不能成为独立近似规则。并未声称整数混合闭包等于所有实偶正型分布，也未付极限普通determinant身份／trace尾费。

## 6. 全部fixed窗原Dlog的alias误差

固定R>0，\(\operatorname{supp}r\subset[-R,R]\)，采用原全线zero-extension
\[
 \|r\|_{H_{\log}}^2=(2\pi)^{-1}\int
 [1+\log(2+|t|)]|\widehat r(t)|^2dt.
\]
对\(W_{h,\gamma}=h\sum_n2\cos(\gamma nh)\delta_{nh}\)、Δ=2π/h，(4)给精确正差
\[
 Q_{h,\gamma}(r)=|\widehat r(\gamma)|^2+|\widehat r(-\gamma)|^2
          +R_{h,\gamma}(r),
\quad R_{h,\gamma}=\sum_{k\ne0,\,\pm}|\widehat r(\pm\gamma+k\Delta)|^2.
                                                                  \tag{12}
\]
若Δ≥max(2,4|γ|)，则
\[
 \boxed{0\le R_{h,\gamma}(r)
       \le\frac{C_R}{\log(2+\Delta)}\|r\|_{H_{\log}}^2.}     \tag{13}
\]
C_R在所述范围对γ一致，保所有complex源；不是逐个固定r的估计。

证明选\(\chi\in C_c^\infty\)在[-R,R]恒1，q=|hatχ|、w=1+log(2+|t|)。由χr=r和weighted Cauchy–Schwarz，
\[
 |\widehat r(\lambda)|^2\le(2\pi)^{-2}
   \left(\int\frac{q(\lambda-t)}{w(t)}dt\right)
   \left(\int q(\lambda-t)w(t)|\widehat r(t)|^2dt\right).
\]
第一括号≤Cχ/w(λ)：近区|t−λ|≤|λ|/2用w(t)可比w(λ)，远区用q的Schwartz尾。alias皆|λ|≥3Δ/4；每支Δ-separated，故\(\sup_t\sum_{k\ne0,\pm}q(\pm\gamma+k\Delta-t)\le C_\chi\)。Tonelli求和即(13)。两支重合仍计重数，常数至多倍增。

先在compact smooth源证明，再由固定窗Dlog core及两侧有界性延到整个zero-extension窗域。交叉B误差由正残差的Cauchy–Schwarz控制。有限正混合的费用为\(C_R\sum c_j/\log(2+\Delta_j)\)，权重／频率／源窗成长时必须共同支付，不把固定R常数当uniform成长结论。

γ=0的实际E序列另有有效频率√δ_j趋0；目标cos频率变化在fixed窗的Gram误差为\(O_R(\delta_j)\|r\|_2^2\)，再加(13)。

## 7. 原du不能同样变小，且1/log为匹配阶

固定\(\eta\in C_c^\infty((-R,R))\)、\(\int\eta\ne0\)，令λ_h=γ+Δ。取同窗b_±使\(\mu_i b_j=\delta_{ij}\)，其中\(\mu_\pm r=\int e^{\pm u/2}r\)。定义
\[
 r_h=e^{i\lambda_hu}\eta
      -\sum_{j=\pm}\mu_j(e^{i\lambda_h\cdot}\eta)b_j.         \tag{14}
\]
矩修正由compact分部积分为任意负幂。双pole矩严格0，且
\[
 \|r_h\|_2^2\to\|\eta\|_2^2,\quad
 R_{h,\gamma}(r_h)\ge|\widehat r_h(\lambda_h)|^2
                   \to|\int\eta|^2>0,
 \quad\|r_h\|_{H_{\log}}^2\sim\log\Delta\|\eta\|_2^2.       \tag{15}
\]
故全部fixed窗源上的du operator误差不趋0；Hlog中的1/log上界有同阶lower test。这是原source费用，不是辅助全空间norm下界；只对全源operator sharp，不声称每个源都必须花该费用。

## 8. 完整Γ可逼近的预算门及合法逃逸

因\(|\operatorname{Tr}U^{mn}|\le2g\)，一般曲线的scaled完整分布满足
\[
 |W_{C,a}|([-R,R])\le2g(2R+h).
\]
正混合若\(\sum c_jg_j\)和\(\sum c_jg_jh_j\)一致有界，则其D′极限是locally finite Radon测度。经典完整Γ在原点穿孔核为
\[
 -\frac{e^{-|u|/2}}{1-e^{-2|u|}}
      =-\frac1{2|u|}+O(1),                                \tag{16}
\]
pole背景平滑且prime首atom离0，所以Wζ非Radon，不能在此有界预算类中。共同紧支近似单位抹平只在稍大窗改变同一TV包络，仍不能越过该门。非Radon旧事实＋TV紧性本身为旧直接后果，本轮不重计。

**发散预算是合法修复，不能排掉。**例如已知
\(\Gamma(t)-\Gamma(0)\ge0\)，由digamma差的逐项非负级数可证；故\(W_\Gamma-\Gamma(0)\delta_0\)是独立正型分布，按(11)确有本族的完整正逼近，即使其局部非Radon。此例只展示预算发散可绕开TV门；原Γ的负contact必须补回，不能借正修补删除它。

恢复完整经典目标仍需同源处理
\[
 W_\zeta=W_\Gamma+2\cosh(u/2)\,du
   -\sum_{p,k\ge1}(\log p)p^{-k/2}
                  (\delta_{k\log p}+\delta_{-k\log p}).       \tag{17}
\]
Γ含既定contact，所有proper powers及两pole全保。生成某个Γ正修补不支付(17)的signed组合或独立容量；这是已有positiveΓ／compact残差责任的另一表示。

**D′逼近与统一原Hlog误差严格分开。**任意一个局部有限Radon分布V，在fixed窗都有\(|Q_V(r)|\le |V|([-2R,2R])\|r\|_2^2\)。本族每个有限混合、以及每个固定尺度的合法光滑化，均有这种有限常数。取同窗\(r_t=e^{itu}\eta\)，如(14)用超多项式小修正精确消双pole，则由\(\Gamma(t)=\log|t|+O(1)\)、fixed窗全部prime-powers项du有界，得到
\[
 \frac{Q_\zeta(r_t)}{\|r_t\|_{H_{\log}}^2}\to1,
 \qquad\frac{Q_V(r_t)}{\|r_t\|_{H_{\log}}^2}\to0.             \tag{17a}
\]
因此每个这样的V都有
\[
 \sup_{r\ne0,\ \operatorname{supp}r\subset[-R,R],\ \mu_\pm r=0}
 \frac{|Q_\zeta(r)-Q_V(r)|}{\|r\|_{H_{\log}}^2}\ge1.        \tag{17b}
\]
V的TV可随迭代任意发散，仍不能得到全源统一Hlog误差趋0；每个j先选更高t即可。这里的1由本Hlog／Γ首项规范给出，不是Q的正性假设。该门不否定D′／逐源／强form逼近；(13)只运输每个有限cos组合的alias差，不支付完整Γ谱截断的统一误差。允许每层保留真正的Γ奇性、不同更强源范数或源依赖截断，才可能绕过此特定统一norm门。此为旧Γ首项／有限TV责任的精确消费，不宣称排除了全部正逼近路线。

## 9. 405、537与真实几何载体的消费范围

若只证明完整W_j→Wζ于D′，则每个compact源的Q收敛足以传Weil正性；中间点不必逐层消经典405。然而D′本身不控制noncompact P_c，也不提供同一源商或actual截面lift。

本族确实一般不消405：其实际\(p=(D^2-1/4)H\)、H>0有\(\int p=-\tfrac14\int H\ne0\)；§4的常数极限给\(Q_0(p)=2|\int p|^2>0\)。单cos序列对这个快速衰减源也可由(10)的全线L¹导数版本直接收敛，故这是实际关系反测，而不只是map未定义。

更强要求“每个正谱证书精确消405的r_p”会由\(\int|\widehat r_p|^2d\sigma_j=0\)强制正谱位于\(\widehat r_p\)的实零集；405给该变换含\(s(s-1)\xi(s)\)。这会重新引入实际critical-line零标签，不能凭证书名字独立付款。若中间点只做分布近似，须另证明noncompact尾；不能将这一更强要求当D′策略必需。

对537 compact非根r0，若完整目标逼近真已付，则Q_j(r0)→Qζ(r0)>0，最终可见。任意cos或lattice本身并不自动见所有r0，更不成为405几何同构。

原dilation的准确norm为\(D_ar(v)=\sqrt a r(av)\)，
\[
 \|D_ar\|_2=\|r\|_2,\quad Q_{m,a}(r)=aQ_m(D_ar),\quad
 \|D_ar\|_{H_{\log}}^2=(2\pi)^{-1}\int
 [1+\log(2+a|t|)]|\widehat r(t)|^2dt.                       \tag{18}
\]
源窗扩为R/a；a≤1虽不增加此Hlog范数，也不消几何成长窗／capacity及trace尾费。正分布闭包不自动给普通determinant、整数重数、base change／Picard移动或RR设施极限。
双pole矩同时变为\(\mu_\pm(D_ar)=a^{-1/2}\int e^{\pm u/(2a)}r(u)du\)；原双pole-zero不自动是native双pole-zero。

## 10. 控制、净后果与停止

continuous正cos通过(11)；continuous负\(2\cosh(u/4)\)被旧compact双pole-zero 2×2负Gram排除。Gaussian卷积只乘其正数，Gaussian乘窗的Fourier仍有cos变号，不能自动制造正性；一般signed核固定粗乘窗可变正，故固定尺度也不反推原目标。详见分支稿，不把这些旧检验算新独立容量。

本轮新增实际设施为(3)–(11)的固定真实函数域生成／正Euler反演，以及(12)–(15)的原Dlog统一误差与sharp测试。它推进了“可用的正模型是否足够丰富、全部returns费用能否付”的具体问题。允许最宽缩放／正混合后，membership本身仍等价正性；停止继续调m、相位、抹平或以闭包换名RH。

下一须有经典分布侧独立选择近似权重／频率及(17)完整误差的输入，或回实际source→sections的同对象RR容量。没有这个实物，不串未知近似合同。固定pole／degree、原norm预算、算术marking等更刚性的类可能增加判别力，须给具体模型后再准入。

强旧仍542＋555→557 whole leading4/5负惯性上预算；actual成长core／coupling／Ξ及经典独立容量未变。局部正模型生成和费用瓶颈改变，宏观瓶颈未改变；Goal门open。本次是否一轮结算以fresh／root最终收据为准，不按分支或文件数计。
