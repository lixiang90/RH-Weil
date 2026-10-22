# 实际 adelic 限制、相对 DGA 与平方 RR：非谱底空间的具体检验

2026-10-22，用户指定研究门。沿同 G20261014、冻结 0c4f；C035保持已完成。
这是405/519等旧资产的链层实现、两份原件的定点核查及初等对照，不开C036，不新增573或数学轮。
原cadence=1、正式cycle14保持。最终审阅、root前件闭合与远程核验另留收据。

## 1. 结论与判断标准

**可以不以 Ξ 零除子为底空间，直接从实际 adelic restriction 构造保两 degree 的相对复形，
并补成显式非 unital DGA。** 主关系有实际源上的零同伦，537非根在同调及对应作用中均可见，
固定窗原du/Dlog与源Schwartz费用可列明。但此DGA quasi-isomorphic于旧405解析商；
它尚未把相对对象变成具有有效性、局部消失过滤和独立平方RR的算术截面对象。

**真实算术二次容量本来就存在。** P¹_Z的带metric截面数已有log#~a n²；
函数域真C×C有signed平方RR。不能把瓶颈笼统写成“算术曲线只有线性容量”或“没有平方”。
当前缺的是同一实际源、同一primitive方向、同一限制/乘法与完整Weil身份的耦合。
把外tensor的维数平方、正Hilbert范数或余核上的谱trace称为RR，均未闭合这一箭头。

检验次序为：405全principal/两degree → 537非根 → 原域/费用 → 实际复合 → 同对象容量 → 完整预算。
只通过前几门，不据此推正性。strong-old仍为542+555→557 whole leading4/5的负惯性上预算；
它不是实际负谱下界。actual低频、core、coupling、Ξ和长期完成门均未改变。

## 2. 原件、对象与物理坐标

本门定点核读两份primary：

- [Connes–Consani–Marcolli 2007 v1](https://arxiv.org/html/math/0703392v1)，§§4.2–4.5、6.4、7.1–7.2：真实restriction、闭像cyclic余核、缩放作用及degree。
- [Connes–Consani 2015 v1](https://arxiv.org/html/1502.05580v1)，§§6.3–6.4、7：真实算术site平方、reduced对应及例外复合。

消费原文已证范围，未把2018§3.4平方RR研究计划升级为定理。详细来源与独占推导分别在
[限制链载体](../../reviews/2026-10-22/adelic-relative-square/actual-restriction-and-chain-carrier.md)、
[site复合](../../reviews/2026-10-22/adelic-relative-square/frobenius-square-and-composition.md)、
[容量与正反检验](../../reviews/2026-10-22/adelic-relative-square/quadratic-capacity-norm-and-controls.md)。
405/407/408/519/520/552/553/567/568的原范围保留，不声称本门重证其全部上游。

令F=S_exp,C，物理坐标r=Cf=e^(u/2)f，F_c=CF；两个集合相同，但norm/作用不能混写。
令S为偶Schwartz源η且η(0)=∫η=0。实际径向限制为

\[
 E_c\eta(u)=e^{u/2}2\sum_{n\ge1}\eta(ne^u),\qquad
 \mu_\pm(r)=\int e^{\pm u/2}r(u)du.
\]

E来自adelic群胚到idele群胚的限制及trace，并非从未知零点反造。
405/519已付其连续单射、闭像及实际Poisson对偶；像的完整零jet描述是后续识别。
记I=E(S)，P_an=I∩ker(c,d)。尤其I、P_an、完整Q的最小trace根不是同一个对象。

## 3. 实际相对复形、全principal同伦及537非根

在次数−1、0定义

\[
 \mathcal C=[S\xrightarrow{\partial}B],\quad
 B=F_c\oplus\mathbf C^2,\quad
 \partial\eta=(E_c\eta,-\mu_+(E_c\eta),-\mu_-(E_c\eta)),
 \qquad j(r)=[(r,0,0)]. \tag{1}
\]

直接计算与405两degree源基给

\[
 \ker j=CP_{\rm an},\quad H^{-1}(\mathcal C)=0,\qquad
 H^0(\mathcal C)\simeq(F_c/CI)\oplus\mathbf C^2\simeq F_c/(CP_{\rm an}). \tag{2}
\]

第一同构送[(g,a,b)]到([g],a+µ_+(g),b+µ_-(g))。
它是Fréchet分离商；不将径向二项复形冒称完整cyclic complex或某个structure sheaf。
405的h=Eη_h有c(h)=d(h)=1/4；所以j(Ch)=[(0,1/4,1/4)]。
裸余核F_c/CI会错误丢掉它，(1)保留。另一方面Q(Ch)=0，故其非零degree不要求忠实正能量。

实际dilation lift与chain action为

\[
 U_r\eta(x)=\int e^{-t/2}r(t)\eta(e^{-t}x)dt,\quad
 T_r^{-1}=U_r,\quad T_r^0(g,a,b)=(r*g,\mu_+(r)a,\mu_-(r)b).
\]

E_cU_rη=r*E_cη，U_rU_s=U_(r*s)，故T_rT_s=T_(r*s)。中心权e^(−t/2)不可删。
对每个实际q=Eη_q∈P_an，令r_q=Cq、K_q(g,a,b)=U_gη_q，则

\[
 \boxed{T_{r_q}=\partial K_q+K_q\partial.} \tag{3}
\]

degree零保证次数0等式；次数−1等式由E_c单射与卷积交换性给出。
这覆盖整个principal像，不止单p。特别405的p=(D²+D)h、η_0明确，因而无需形式除以Ξ。
对h不能照抄(3)：它在degree上的1/4作用并不消失。

537给r_0=(D²−1/4)ψ，0≠ψ∈C_c∞((-17/16,17/16))，µ_±=0且完整Q(r_0)>0。
若j(r_0)=0，则r_0∈CP_an，旧显式公式给Q=0，矛盾。
实际作用T_(r_0)也不全零：否则r_0*g对所有g均属闭Pan，紧支近似恒等元极限会使r_0∈Pan。
这里只用旧固定窗证书作非根见证，未升级成长或预设零点位置。

## 4. 乘法确实能补完：degree cocycle而非不可能性

裸逐分量乘法不使∂S成ideal。具体h边界与e_+=(0,1,0)相乘会给(0,−1/4,0)，不在像中。
但这一失败有明确合法修复。在B上定义

\[
 (g,a,b)\star(h,c,d)=
 (g*h,\;ac+a\mu_+(h)+c\mu_+(g),\;
 bd+b\mu_-(h)+d\mu_-(g)). \tag{4}
\]

Φ(g,a,b)=(g,a+µ_+(g),b+µ_-(g))将它同构到F_c×C²逐分量代数，
并将∂S送到CI×0×0。令B作用S只用首分量U_g，S^(−1)·S^(−1)=0。
双负次数Leibniz所需Peiffer等式U_(E_cη1)η2=U_(E_cη2)η1，由E_c单射直接成立。
因此得到交换、Fréchet乘法连续、非unital的DGA；j_0(r)=(r,0,0)是代数map，左乘即T_r。
e_+与h边界在(4)下乘积为0，说明degree协同并未被删除。

原F_c无卷积unit，不能将δ_0当原函数。canonical projection C→H^0是quasi-isomorphism，
即同调上仍为旧405商。这里实际补完了一项代数设施；不能继续声称“无法DGA”，
也不能把“有DGA”升级为有效Cartier除子、算术结构层、极化或RR容量。

对偶也可在实际源上同时写出。采用405的Fourier规范，Poisson给
E_c(hatη)(u)=E_cη(−u)。令Jη=overline(hatη)，r*=overline(r(−u))，
以及(g,a,b)†=(g*,bar b,bar a)，则J²=1、∂J=(∂)†，且†保持(4)。
E_c单射再给J U_r=U_(r*)J，故这是相容的反线性链对偶，交换两degree。
这付的是实际Poisson对偶，不是positive pairing；未从中产生极化或RR正号。

一般g分布可移植的是这一**有前件的构造配方**：先独立给等变E、卷积稳定源、两个指定字符，
再核实际像/闭性与Peiffer。经典E的单射使后者自动成立；一般E有核时须另证或保留更高复形，
不能直接宣称H^(−1)=0或quasiiso旧商。一般g-integer计数不会自行提供加法adeles、Poisson源、
字符恰为±1/2、整性格或有效对应；非自对偶时还需两边源及其对偶配对。
所以此配方没有把经典输入偷偷宣称为任意g分布的普遍定理，亦不以全类皆正为目标。

## 5. 原du/Dlog与源费用，固定窗不能偷换全线

取原Dlog²=(2π)^−1∫log(2+|t|)|rhat(t)|²dt，
并以du表示物理L²。用1+log版本时仅有等价norm，常数需运输。
对supp r⊂[−L,L]，目标卷积费在du及Dlog上均≤||r||_1≤√(2L)||r||_du；
每个degree的du dual norm为√(2sinh L)。
源半范数q_(a,b)(η)=sup|x^aη^(b)(x)|满足

\[
 q_{a,b}(U_r\eta)\le q_{a,b}(\eta)\int|r(t)|e^{\kappa t}dt
 \le q_{a,b}(\eta)\sqrt{\sinh(2\kappa L)/\kappa}\,\|r\|_{du},
 \quad\kappa=a-b-\tfrac12. \tag{5}
\]

κ=0按连续值√(2L)理解；此处整数a,b实际不会为0。
改用Dlog右边再除√log2。全S_exp源则是各带权L¹费用，不是单一全线L²界。
这些是代表元作用的上界，不是正商上的等距norm，也不是必要成长下界。

553已证明全physical Pan平移族在全线du/Dlog稠密；
因此任何全线原norm连续、消全部关系的Hausdorff正商map必退化，coset不变非线性map亦常值。
Fréchet/固定窗/变域/cofinal付费仍是合法逃逸。(1)未免费绕过这个强旧结论。
若后续局部值y_r=E A_Lr来自实际截面map，最小lift费≤||A_Lr||²；
不得以E全空间坏singular value当实际源必需费用。亦不能固定坏minor而忽略同对象的好minor。

## 6. 实际算术site复合与一个失败的源current

2015原件已给非Ξ定义的真实square与Frobenius对应。准确复合为

\[
 \Psi_\lambda\circ\Psi_\mu=
 \begin{cases}
 \Psi_{\lambda\mu},&\lambda\mu\notin\mathbf Q\ \text{或}\ \lambda,\mu\in\mathbf Q,\\
 \mathrm{Id}_\epsilon\circ\Psi_{\lambda\mu},&
 \lambda,\mu\notin\mathbf Q,\ \lambda\mu\in\mathbf Q.
 \end{cases} \tag{6}
\]

例如√2与其倒数复合为切向Id_ε。只保参数乘积会丢掉germ；它不能直接命名为Γ有限部分。
结构半环加法幂等，其literal加性群完成为0，故不能先普通群完成再张量C来取得全complex源。
这不排先构造cycle群、Witt/relative/derived提升再扩系数。

最直接的标签current C_r=exp_*(r(u)du)有固定窗TV≤√(2L)||r||_du，且单射。
因此保r_0，却不消p；明确

\[
 \int\lambda^{3/2}\,d\mathcal C_{Cp}(\lambda)=M_p(2)=\pi/6\ne0. \tag{7}
\]

另取Pan商会回旧关系。绝对连续双源可在a.e.标签模型忽略(6)的例外直线，
但diagonal trace/有限部分可能读到该零测集；没有证明原对应类别的积分、trace及费用相同。
原子Riemann和只可选弱拓扑逼近，不能在TV中逼近非零绝对连续current。
所以(6)与(1)都是真设施，却尚无可把两者粘成有效算术截面的自然比较map。

## 7. 二次容量正例，以及它们尚未支付什么

代数外平方C⊗C合法；(3)的同伦随tensor延伸。但completed tensor精确性、全cyclic比较另付。
有限维[U→V]的外平方χ=(dimU−dimV)²仅是Künneth。
取A=diag(1,−1)，Tr(A⊗A)=0而Tr(A²)=2：外tensor trace不能替composition交数。
407的非零源relative prime-arrow对象在每个idele fibre可缩；合法外平方仍可缩。
这只说明该fibre函子漏信息，不说明源relative范畴零；boundary/gluing/regulator仍可承担新输入。
非交换balanced tensor须先给双模，且不能丢Tor后凭空多算容量。

两个真实正例防止过强否定：

1. P¹_k限制到{0,1}，E_n:H⁰O(n)→k²，其外平方在真P¹×P¹上计算RΓO(n−2,n−2)，χ=(n−1)²。
   n=0的χ=1来自H²而非H⁰。primitive方向F1−F2相对ample F1+F2有D²=−2，
   O(n,−n)在n≥2时h¹=n²−1；它不是两个正截面数相乘得到的。
   若要求对两个fibre都degree零，P¹×P¹的数值primitive空间只有0，不能承担r_0。
2. 真算术曲面P¹_Z取O(1)标准toric metric与固定a>0的arch常数twist。
   n次整多项式小截面条件为sup |P(z)|/max(1,|z|)^n≤e^(an)。
   Cauchy与三角不等式给系数立方盒上下夹，从而
   log#Hhat⁰=a n(n+1)+O_a(n log n)。finite整性及arch高度都真实存在，已独立给n²容量。
   但a是外加twist，未有r→该线丛/metric/截面的关系相容map，也未有primitive Weil系数身份；
   按Q(r)选a会循环。旧552的真正metric同样不能因其存在而自动接上本题：p的energy非零，高频阶数也不符。

因此现有的独立二次容量可作为明确目标对象，却不是已付的classic同源输入。
下一步若能给实际比较map及primitive系数/误差，就可以改变选路；继续平方向量空间不会改变这一点。

## 8. 连续正反与函数域：正号究竟多用了什么

连续positive g-integer族的旧控制R_d=C[z]/(z²+d)、z†=−z，完整primitive trace型为
Q_d(A+Bz)=2|A|²+2d|B|²。d=±1/16都有非退化评价、同样的乘法/复合和外平方维数。
保dagger时tensor Gram为diag(4,4d,4d,4d²)，负d仍有负方向；换HS正metric等于换目标型。
d=0还要区分全jet与trace nilradical。这个检验只排“代数设施/评价非零/维数平方足够”，
不声称任意连续g系统已被赋予Q的加法adeles。

函数域真C/F_q则先有C×C上的实际对应、局部交重数、principal关系、截面乘法及RR。
RR的signed n²D²/2项配合有效性和固定容量推出Hodge index，
再由全部Frobenius graph交数/点数识别全period Weil Gram，最后扩张complex系数。
正号来自这段同对象几何，而非单独的restriction或标签乘法。
568真F5曲线与正Euler整数反模型都能通过finite局部jets/非零评价/外平方；primitive Gram行列式却为11/5与−1。
函数域的所有period aliases与H⁰/H² pole扣除不能删。

## 9. 完整Γ、素数幂、极点及独立性清单

对物理源继续使用完整规范

\[
\begin{aligned}
Q_W(r)={}&2\Re(\mu_+(r)\overline{\mu_-(r)})+
 [\psi(1/4)-\log\pi]\|r\|_{du}^2\\
&+\tfrac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}
 \|\tau_vr-r\|_{du}^2dv\\
&-2\sum_{p,k\ge1}(\log p)p^{-k/2}
 \Re(r*r^*)(k\log p),\qquad r^*(u)=\overline{r(-u)}.
\end{aligned} \tag{8}
\]

405的Tate/Fourier/Haar与568规范已付该解析身份，不因构造DGA而新增。
本门没有证明：(i)Γ/contact是同一平方截面的arch容量；
(ii)每个p^k项是其真实局部消失/整除阶；(iii)两个pole是同一RR缺陷；
(iv)三者在同一determinant line/截面对象上协同且付全mixed误差。
569的matched cocycle仍是合法设施，但它不自行付正号。

真正可晋级的新输入须是上述同对象比较中的实际定理，包含原norm与成长量词。
若只规定“容量二次系数=Q_W且非负”，就是Weil正性的等价/充分包；
若从独立的有效截面、乘法、RR、局部作用证明预算差等于(8)，才是想寻找的新机制。
不要求独立构造永远不能使用旧解析identity，而要求其正号来源不由零点位置或待证正性定义。

## 10. 停止范围、选择与精确下一门

本次付了source-defined非谱base载体及DGA，明确全关系/非根/费用；
也区分真实site复合、真实几何/算术n²容量与旧谱商包装。代数设施缺口缩小，宏观容量瓶颈未变。
没有新classic独立正性、whole预算或core后果；不计新数学轮，不将old cohomology的重新实现当新净定理。

当前入口在此停止，不续tensor次数、Frobenius样本、Gaussian/probe或2018研究计划。
下一仅准入**实际写出的非形式比较/相对regulator**：从(1)的源到非Ξ定义的算术square/relative截面，
通过整个Pan与r_0、保两degree，列原域/du/Dlog费用，并给同对象局部过滤或primitive容量的可判数据。
否则保一次来源定位，不能把这个缺口再命名为未知cohomology合同。
与之比较，重开Sonin高频/572运输只会回已付safe-high旧推论；只引用site已有square也没有信息差。
若出现actual低频signed比较、真正穿过idele纤维acyclicity的boundary量，或上述primitive RR比较，才改变排序。
合法relative/noncommutative/Fréchet/cofinal/源依赖修复仍保留；本次不声称排除这些方法类。
