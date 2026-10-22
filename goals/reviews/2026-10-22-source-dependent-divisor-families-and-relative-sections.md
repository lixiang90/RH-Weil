# 源依赖除子族与相对截面：实际映射、原费用和同对象容量

2026-10-22，执行用户指定的family／relative入口。同G20261014与冻结0c4f基线。
本报告的结论分清“实际解析截面存在”和“独立算术容量存在”：前者可以具体写出；后者本轮没有取得。
519/520谱商和553范数门已付，不因相对几何包装重新计数学轮，无573/C036。

## 1. 本次核查的问题与最强旧对照

[前次报告](2026-10-22-global-sections-local-evaluation-admission.md)已给regular finite frame的kernel、
有限格的原高度预算，但没有给覆盖非根的独立算术源map。用户明确允许源依赖的除子族或相对对应，
故本次不再试固定离散群上的裸加性map，而核三个实际构造及其原域、类与截面角色。

不能把已有结果当作新进展：405给主关系与两degree，519给实际像等于全部zero-jets，
520给原Fréchet商及重数，553已同时给全线L²／Dlog稠密、非线性类map退化和合法cofinal费用。
尤其“改成非线性family即可绕过稠密”并不正确：仍须改变553那个全线原norm连续且principal-coset不变的前件。
但fixed-window费用、原Fréchet拓扑、marked sections和relative cocycle均未因此被排除。

本次选择可检验的具体公式，不自动串下一篇论文，不续Sonin高频参数或线性RR来源。
它能判定：实际section在哪个范畴成功，单个主关系测试会漏什么，以及相对碰撞费用能否合法修复。
若只得到旧谱商与初等曲线容量，就在这条入口收口，不预建未知平方RR合同。

## 2. 全部主关系相容的实际global-section map

固定物理坐标和整变换

\[
 r(u)=e^{u/2}f(u),\qquad
 A_r(z)=\int_{\mathbf R}e^{zu}r(u)du=M_f(1/2+z),\qquad
 \Xi(z)=\xi_{\rm Riemann}(1/2+z).
 \tag{1}
\]

先取\(r\in\mathcal A_{\exp}=e^{u/2}S_{\exp,\mathbf C}=S_{\exp,\mathbf C}\)；compact源为其子域。
不假定\(\Xi\)的零点在虚轴。它由指定经典完成化／theta定义，包含完整Γ规范；并非由未知零点位置反造。
令

\[
 H(z)=(z^2-1/4)\Xi(z),\qquad
 Z_H=V(H)\subset\mathbf C_z,\quad
 \mathcal O_{Z_H}=\mathcal O_{\mathbf C}/(H),\qquad
 \pi:\mathbf P^1_{Z_H}\to Z_H.
 \tag{2}
\]

这里是局部有限、保重数的复解析底空间，通常总长度无限。不能把它称为有限算术scheme。
无需枚举零点，直接取coherent cokernel sheaf即可定义。令\(a_r=[A_r]_H\)，有

\[
 \boxed{\ \sigma_r=-a_rY\in\Gamma(\mathbf P^1_{Z_H},\mathcal O(1))\ },
 \qquad s_r=X-a_rY,\quad\Gamma_r=Z(s_r).
 \tag{3}
\]

这给出了物理源到真实global section的复线性map，并给出了源依赖relative graph。
因为\(x-a_r\)是monic，即使base非约化也为非零因子；\(\Gamma_r\to Z_H\)为同构。
\(\sigma_r\)只是global section，其本身可能是零或零因子，未声称它的零 locus总为Cartier。
\(s_r\)则是定义相对有效Cartier图的regular section。
所用几何规则仅是[regular section／Cartier除子的标准对应](https://stacks.math.columbia.edu/tag/0C4S)；
本例的monic检查已直接给出，不援引未知正性。

### 2.1 实际kernel与405／537测试

405已付

\[
 A_{r_h}=\Xi/2,\quad A_{r_p}=H/2,\qquad
 r_h=e^{u/2}h,\quad r_p=e^{u/2}p.
\]

故\(\sigma_{r_p}=0\)。对全部指定解析主关系则有精确识别

\[
 \ker\sigma=e^{u/2}P_{\rm an},\qquad
 \ker(r\mapsto[A_r]_{\Xi})=e^{u/2}I.
 \tag{4}
\]

这里的实际源像／growth责任归519(1)–(3)和518的Mellin除法、Möbius重建：
对于原\(S_{\exp}\)源，全部完成零点jets恰刻画\(I=E(\mathscr S_{e,0})\)；
再加两个端点值零才是\(P_{\rm an}\)。没有把任意整函数可除性无费升级成源membership，
没有声称任意\(\Gamma(Z_H,\mathcal O)\)截面都来自源。

\(\Xi(\pm1/2)=1/2\)，所以

\[
 Z_H=Z_\Xi\sqcup\{-1/2\}\sqcup\{1/2\},\qquad
 a_{r_h}=(0,1/4,1/4).
 \tag{5}
\]

537的实际非根\(r_0=(\partial_u^2-1/4)\psi\)，\(0\ne\psi\in C_c^\infty((-17/16,17/16))\)，满足
\(A_{r_0}=(z^2-1/4)A_\psi\)。两个degree分量为零；primitive分量非零，
否则全部完成零点值零会给\(Q_W(r_0)=0\)，违背537的完整源严格正性。
因此(3)确实同时消去全部\(P_{\rm an}\)、保留\(r_0\)，并正确保留\(h\)的两个degree。

这是一条**不经\(J_W\)复合的实际解析截面映射**。但它把旧完成谱商放进了base，
不是独立构造了带算术有效性／RR的全局载体。省略零点枚举不等于省略completed divisor这一输入。
前次“未给实际map”的停止判断应理解为未给独立算术map，而不能扩成“任何实际解析map都不存在”。

### 2.2 不能交换的对象与乘法

\[
 \Gamma_r-\Gamma_0=\operatorname{div}(s_r/X).
\]

故这些图的相对Picard类恒定；源由**marked section**保存。
若改用线丛类来声称principal下降，就也丢掉\(r_0\)。不能在两个目标间切换着消费。
另一个可用对象是\(A_r/H\)模去entire sections的类；原始亚纯截面本身并不消去\(p\)，其值恰为\(1/2\)。
literal方程\(H(z)w=A_r(z)\)在\(H=0,A_r\ne0\)处空纤维，在共同零点处整条\(\mathbf A^1\)，
不能把它当成(3)的flat graph。

系数满足\(A_{r*t}=A_rA_t\)，对应源卷积；不是pointwise乘法。
\(\sigma_r\sigma_t\in\mathcal O(2)\)，\(\sigma_{r*t}\in\mathcal O(1)\)，不能直接认同。
加入分次和固定\(Y\)因子可以记录系数乘法，尚不产生算术对应的degree或有效性。
有重零点时，(2)保全部nilpotent jets；普通乘法trace只读重数加权的常数项。
全jet商、ordinary trace根商和最小Weil商仍然不同。

## 3. 原du／Dlog费用：固定窗成功，全线／全高度另付

对\(\operatorname{supp}r\subset(-L,L)\)、\(z=\alpha+i\gamma\)、\(k\ge0\)，有精确L² squared operator fee

\[
 \|r\mapsto A_r^{(k)}(z)\|_{L^2(-L,L)^*}^2
 =\int_{-L}^L u^{2k}e^{2\alpha u}du.
 \tag{6}
\]

对\(|\Re z|\le A\)直接给\(\sqrt{2L}L^ke^{AL}\|r\|_2\)上界。
原zero-extension范数固定为

\[
 \|r\|_{D_{\log}}^2=(2\pi)^{-1}\int\log(2+|t|)|\widehat r(t)|^2dt
 \ge\log2\|r\|_2^2.
\]

因此每个固定窗、有限局部读出均有可付上界；(6)不能称为Dlog的同一个精确Gram。
553已给真实restricted dual费用：对固定\(k\)、\(L\ge1\)、全部\(\gamma\)，中心读出为

\[
 \asymp_k\frac{L^{2k+1}}{1+\log(2+|\gamma|)};
\]

对每个先固定\(\alpha\ne0,\gamma,k\)，则为\(\asymp_{\alpha,\gamma,k}L^{2k}e^{2|\alpha|L}\)。
不对\(\alpha\to0\)偷换一致渐近，不把单坐标费当全部高度／jets的共同operator费。
从Taylor jet范数换到\(A_r/H\)的principal-part范数还含\(H\)的局部导数倒数，
不能无费uniform于高度、重数或间距。

553已证明全线\(L^2/D_{\log}\)中全部\(r_p\)平移的张成稠密。
故全线原norm连续、对全部principal coset不变的Hausdorff值map，即使非线性也常值。
(3)采用原Fréchet／解析局部拓扑及fixed-window收费，保持这个合法逃逸；没有一个免费的global bound。
原Fréchet中的主关系闭像与弱Hilbert拓扑中稠密不矛盾。

## 4. 不用谱商的实际族：哪些具体测试会失败

### 4.1 平滑探针移动图

取\(a(r)=\int r\zeta\)，\(\zeta\in C_c^\infty\)，拉回普适图\(X-a(r)Y\)。
有\(|a(r)|\le\|\zeta\|_2\|r\|_2\)，固定FS范数下
\(\log\|X-aY\|_{\sup}=\frac12\log(1+|a|^2)\)。
在同一\(\mathbf P^1\)上，\(V_n=H^0(\mathcal O(n))\)，有

\[
 \ker\big(V_n\to\mathbf C[x]/(x-a)^k\big)=(x-a)^kV_{n-k},\qquad
 \dim V_n=n+1.
 \tag{7}
\]

加权正交投影可以具体选择\(\zeta\)，使其同时杀\(r_p,r_h\)而在\(r_0\)非零；
但553的旧稠密／Fourier唯一性保证另有实际主关系\(\tau_a r_p\)不被消去。
因此单个405见证加537非根通过，是必要的便宜测试，不是全部principal下降证明。
该族在complex纤维成立，不能由\(\mathbf Z[t]\)上的普适式免费给任意复数参数配上全p-adic specialization。

### 4.2 实际adelic metric族

不经\(J_W\)也可取实源的\(L^2\)投影\(A_Pr=r-\langle r,P\rangle P/\|P\|^2\)，\(P=r_p\)，
再令\(\phi_r=\kappa_a*A_Pr\)、\(c_r=\|\kappa_a\|_2\|A_Pr\|_2\)、\(\Phi_r=c_r+\phi_r\)。
在\(\mathbf P^1_{\mathbf Q}\)的\(\mathcal O\)上取标准有限位metric和
\(\|1\|_\infty=e^{-\Phi_r(\log|z|)}\)。
Gaussian平滑给合法smooth adelic对象；逐源integrability可按552的曲率／nef-difference证明。

它的\(\sup\Phi_r\le2\|\kappa_a\|_2\|r\|_2\)，
\(\|\phi_r'\|_2^2\le(ae)^{-1}\|r\|_2^2\)可付；compactified曲率却仍有\(O_a(e^{2L})\)成长费用。
此族杀单个\(P\)，保\(r_0\)的非零vertical energy；任意非零平移\(\tau_bP\)又被送到非零energy，
故不消全部主关系。\(\mathcal O\)底层截面为\(\mathbf Z\)，其小截面消失预算仍只是
\(\log N\le\inf\Phi_r\)。这个预算在同一对象上成立，却没有从源产生经典prime-power消失阶。

只依\(M_\pm(r)\)改变metric／divisor的族可消全部\(P_{\rm an}\)，但也消掉\(r_0\)；
其fixed-window原范数费\(\sqrt{2\sinh L}\)不解决非根覆盖。
这些都是实际候选的失败位置，不是所有源依赖、relative或非局部构造不可能。

## 5. 同一相对对象的碰撞、局部消失与global容量

一个必要的付费修复不能漏掉：在\(\mathbf P^1_{\mathbf Z[t]}\)上取flat长度2除子
\(E_t: x(x-t)=0\)。即使\(t=0\)，它仍以basis\(\{1,x\}\)保留一阶jet。
对\(m\ge1\)，完整restriction满射，kernel为\(H^0(\mathcal O(m-2))\)，global容量为rank\(m+1\)。
选列\(\{1,x^m\}\)的真minor是\(t^{m-1}\)，裸双点评价的\(t^m\)多算了collision/frame费用。
完整截面空间总有好列\(\{1,x\}\)给minor 1。

所以\(-\log|t^{m-1}|\)在源norm趋零时发散，只拒固定坏minor／无费frame方案；
不能当成真实receiver或所有relative载体的必要原费用。
局部order \(m\)由\(x^m\)的global degree \(m\)准确支付，仍是曲线的一次容量。
这个实际修复既不产生567的signed平方RR二次项，也没有阻止源依赖截面的局部消失发生跳跃。

在(2)的有限截断底空间\(Z_T\)上，\(H^0(\mathbf P^1_{Z_T},\mathcal O(n))\)是
\(\Gamma(Z_T,\mathcal O)\)上的rank\(n+1\)自由模，其复维数为\((n+1)\operatorname{length}Z_T\)。
这是同对象的真实容量；但\(\operatorname{length}Z_T\)已经由完成零除子给定，
没有独立算术上界或控制原源所有mixed组合的预算。无穷底的普通总维数不能直接代有限RR容量。
complex analytic length也不是\(v_p(\Delta)\log p\)；全位specialization仍是独立责任。

## 6. 连续正反、函数域及完整经典源

连续正反例可用同一个有限代数检查。令\(R_d=\mathbf C[z]/(z^2+d)\)、\(z^\dagger=-z\)，
系数取复共轭；设\(\tau\)为regular multiplication trace。则

\[
 \tau\big((A+Bz)(A+Bz)^\dagger\big)=2|A|^2+2d|B|^2.
 \tag{8}
\]

\(d=1/16\)为正，\(d=-1/16\)有负方向，\(d=0\)保length／trace重数2但nilpotent方向为根。
三者都可作相同relative \(\mathbf P^1\)、monic图、局部评价及线性容量。
这些设施本身不选Weil号；把\(d\)换成\(|d|\)是在换配对。
当\(d\ne0\)时，两号的底层复代数甚至都同构于\(\mathbf C\oplus\mathbf C\)；
差别是\(\dagger\)在正段固定两个点、在负段交换两个点。普通复截面容量看不到这份实极化差别。
(8)是568有限配对的代数表达，未重复记新正性输入。

真函数域的独立设施顺序不同：先有\(C\times C\)上的实际signed对应和RR／Hodge，
再把交数线性扩张到复源组合。无需每个复源本身先成为一个整数Cartier除子。
相对spectral-base包装在真例和formal反模型中都能写出；只有前者的同一平方容量独立支付正号。
函数域推广还须保全周期aliases与\(H^0/H^2\)极点，不能拿单一有限分子商代全部连续时间源。

经典目标保持568既定全源型

\[
 \begin{aligned}
 Q_W(r)={}&2\Re(M_+\overline{M_-})+\Gamma_0\|r\|_2^2
 +\tfrac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}\|\tau_vr-r\|_2^2dv\\
 &-2\sum_{p,k\ge1}\log p\,p^{-k/2}\Re(r*r^*)(k\log p),\qquad
 \Gamma_0=\psi(1/4)-\log\pi.
 \end{aligned}\tag{9}
\]

所有Γ finite-part/contact、proper powers和两pole矩均保留。
旧显式公式把(9)识别为primitive \(\Xi\)部分的Weil trace；(2)中的degree两点只作405的双次数账本。
\(\sigma_h\ne0\)而\(Q_W(r_h)=0\)，所以全H-base上的忠实正norm即使存在也不能直接等于Q。
有重根时还须保trace nilradical，不能强迫全jets的忠实酉化而额外偷入简单性。

本轮没有证明(9)是同一section／det的“原arch容量−有限位消失”预算差。
若要求相对Gram恰等于(9)且全部PSD，仍是Weil正性的等价改写。
若B有额外零点，改成BH会给解析base增加分量／重数；若B是entire unit，base相同但主部frame规范仍可变。
本构造本身不独立排除这份完成化／规范自由。

## 7. 可消费结果、停止与重准入

[实际构造](../../reviews/2026-10-22/source-dependent-family/relative-divisor-construction.md)、
[关系／原norm](../../reviews/2026-10-22/source-dependent-family/relation-nonroot-and-original-norm.md)、
[同对象预算](../../reviews/2026-10-22/source-dependent-family/local-global-relative-budget.md)
保存完整推导、范围和旧资产归属；最终独立审阅与root收据另存。

本轮确认了实际解析section map，实际metric族和同对象relative评价／容量，
并区分marked section、principal graph、Picard类、trace根与全jets。
这些是旧谱商、旧范数门及初等曲线设施的具体组合／准入检验；没有新的独立经典容量或全源signed输入。
来源／旧推论0轮，无573/C036；原cadence1、正式cycle14、Goal版本和冻结基线保持。
strong-old542＋555→557 whole leading4/5上预算、actual低频/core/coupling/Ξ及宏观完成门均未改变。

后续必须有区别于已给完成谱商和任意外加平滑坐标的实际adelic／relative来源，
在同一对象上说明全部主关系、非根覆盖、原norm、局部order以及独立平方容量／预算身份。
或者给当前合法cofinal域上的实际全位新比较，支付完整误差。
只有named relation通过、正FS metric、曲线线性RR或未知PSD条件时停止，不调Gaussian参数、probe数或bad minor。
本次不继续自动串paper，也不以此停止或完成长期Goal。
