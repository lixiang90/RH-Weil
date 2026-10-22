# 579. KRY实际Gaussian源、native循环与relative primitive首门

2026-10-23。[C042](../goals/contracts/C042-kry-gaussian-source-and-relative-primitive-gate.md)的一轮原件，同G20261014／冻结0c4f及全部≤538输入。三分支和独立fresh修后限定PASS已root核读，按收据范围统一结算一轮。这里构造了不以Q或零点标记的实际解析源及原件已证循环的标量接入；**尚未构造满足405/537的相对primitive循环映射，也未取得独立Weil正性**。

## 1. 具体结果及规范边界

固定KRY1999的q=7、有限Schwartz因子，φ*为其Lemma2.1(ii)实际weight1 Gaussian。无穷位的Q、加法字符、自对偶Haar及原φ*均固定，记ν=||φ*||²>0。令二维unitary dilation为

\[
 D_u\phi(x)=e^{u/2}\phi(e^{u/2}x),\qquad
 T_*r=\int_{\mathbb R}r(u)D_u\phi_*\,du.                 \tag{1}
\]

这个map确实进入Schwartz和KRY的诱导section，原du费用可以精确支付。但它及其radial section均注入，因此并未消去405主关系。投回原文已证的weight1线后，所有算术循环只乘一个系数

\[
 P_1T_*r=c(r)\phi_*,\qquad
 c(r)=\int r(u)\operatorname{sech}(u/2)\,du.             \tag{2}
\]

这个native入口的两个明确失败是：405实际Pan的每个平移都有c<0；存在固定537窗内的非零双pole-zero源c=0而完整Qζ>0。任何经此同一scalar的fixed linear relative primitive修复，都不能同时修好这两门。

本结论只停这个实际recipe及其指定修复。高K-types、变化finiteSchwartz、源依赖relativeframe、非有界/强拓扑height、变域及有费无限完成并未排除。相对载体必须先有新的非标量公式，而不是把全Pan的像按定义商掉。

原件：[Kudla–Rapoport–Yang1999作者版](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)，只消费§1(1.4)、Lemma2.1及Theorem3/§5–6的已定位循环接口，不重证所有CM变形理论。其底空间在Spec O_k上有限étale、generic dimension0；线性Arakelov degree不自动给曲线平方上的primitive mixed自交。详细分支见[源/section](../reviews/2026-10-23/kry-actual-source/dilation-schwartz-map.md)、[真实循环](../reviews/2026-10-23/kry-actual-source/cycles-relative-primitive-gate.md)和[历史/原费用](../reviews/2026-10-23/kry-actual-source/history-and-original-source-fees.md)。

## 2. 全S_exp映射、原费用及双pole矩

物理源为r=e^(u/2)f，ALLcomplex S_exp={r: sup e^(N|u|)|r^(j)(u)|<∞，∀N,j}。先在明确的raw坐标模型中取φ₀(x)=exp(−π|x|²)、Lebesgue dx；其ν₀=1/2。定义

\[
 T_0r(x)=\int r(u)e^{u/2}e^{-\pi e^u|x|^2}\,du.           \tag{3}
\]

对每一Schwartz半范数，微分缩放直接给

\[
 \sup_x|x^\alpha\partial^\beta T_0r(x)|
 \le C_{\alpha,\beta}\int |r(u)|
            e^{(1+|\beta|-|\alpha|)u/2}\,du.             \tag{4}
\]

所以S_exp→radial Schwartz连续；不是以某个L²极限替代Schwartz输入。在supp r⊂[−L,L]时，右侧可付
Cαβ√(2L)exp(|1+|β|−|α||L/2)||r||du。此半范数费用依L，不能升为成长统一费。

二维Gaussian积分和Plancherel给

\[
 \langle D_u\phi_0,D_v\phi_0\rangle
     ={1\over2\cosh((u-v)/2)},\quad
 \|T_0r\|^2={1\over2\pi}\int{\pi\over\cosh\pi t}|\widehat r(t)|^2dt.
                                                               \tag{5}
\]

Fourier约定为rhat(t)=∫r(u)e^(−itu)du。T₀由此延至全L²，operator squared norm恰π，且注入。native(1)用**同一个实际φ***的轨道，故不必识别OCR中的Gaussian宽度：

\[
 \langle D_u\phi_*,D_v\phi_*\rangle
       =\nu\operatorname{sech}((u-v)/2),\qquad
 \|T_*r\|^2={1\over2\pi}\int 2\pi\nu\operatorname{sech}(\pi t)
                              |\widehat r(t)|^2dt
 \le2\pi\nu\|r\|_{du}^2.                                \tag{6}
\]

保持原Haar时ν是已给Gaussian积分常数，不是可选择完成化的B(s)。raw ν₀=1/2只说明(5)的明确模型；不能把它未经对齐当成原件所有norm的数字。

原zero-extension Dlog控制du，所以(6)也付其到Gaussian Hilbert像的费用，未换成导数norm。Schwartz、section、Green和height费用不由这条Hilbert上界自动支付。

在native规范中两个矩的实际含义为

\[
 T_*r(0)=\phi_*(0)\mu_+(r),\qquad
 \int T_*r\,dx=\left(\int\phi_*dx\right)\mu_-(r),
 \quad\mu_\pm(r)=\int e^{\pm u/2}r(u)du.                 \tag{7}
\]

因此双pole-zero恰使值0/积分消失，但它们远弱于405全主关系。对全S_exp的交换积分由带权绝对界付，不删经典目标的pole。

## 3. 诱导section仍未给principal关系

KRY的实际λ_C(φ)(g)=(ω(g)φ)(0)确实接收(1)。在finite g=1后，arch g=wn(b)的评价是径向函数的一维Fourier变换，乘固定非零Weil常数及坐标缩放。radial Schwartz若这些评价对全部实b为零，Fourier唯一性给φ=0。故λ_CT_*在此源像上仍注入。

raw坐标可写这个实际读出为

\[
 F_b(r)=\int r(u){e^{u/2}\over e^u-2ib}\,du.             \tag{8}
\]

字符/Q规范可改变式中非零的2，不能改变注入结论。b=0与identity只读(7)的两个矩，不能由两个零值声称整个section为零。

甚至在双pole-zero源上，原du/Dlog也没有到固定compact section sup的全线统一界：选非零compact双矩零r，必有b₀≠0使F_b₀(r)≠0。令τ_ar(u)=r(u−a)，则

\[
 F_{e^ab_0}(\tau_ar)=e^{-a/2}F_{b_0}(r).                \tag{9}
\]

a→−∞时源的两个矩仍零、原norm平移不变，而b→0处读出无界。这里用的是实际源族，非全空间逆norm替代实际费用。每fixed源或fixed窗的强半范数仍合法。

最重要的类型区别是：s=0的λ等变性，不自动使standard s-extension的E′与raw dilation右平移互换。高K-type源的循环/Green导数不能由原件fixed-weight定理免费延出。以下只对严格回到原weight1线的(2)使用已证循环身份。

## 4. Native投影的精确系数、405全平移及537漏失

Gaussian轨道与原Gaussian的内积除以ν恰为sech(u/2)，给(2)，并有

\[
 \|c\|_{(L^2(\mathbb R))^*}^2=4,\qquad
 \|c\|_{(L^2(-L,L))^*}^2=4\tanh(L/2),\qquad
 \|P_1T_*r\|^2=\nu|c(r)|^2.                              \tag{10}
\]

所以native scalar原du全线费≤4ν||r||²，fixed窗进一步乘tanh(L/2)。这是同一原源上的费用，不是算术height界。

[405](405-f1-adelic-restriction-moments-and-radical.md)给真实h=Eη>0、H=e^(u/2)h>0，且

\[
 p=(D^2-1/4)H\in\mathcal P_{an},\quad p\ne0,
 \quad B_\zeta(p,s)=0\ (s\in S_{\exp}).                 \tag{11}
\]

保全部fixed平移，不将这个noncompact关系裁成compact。写s₀(u)=sech(u/2)，直接微分有s₀″−s₀/4=−s₀³/2；(4)的强衰减许可分部积分，从而

\[
 \boxed{c(\tau_ap)=-\tfrac12\int H(v)
                \operatorname{sech}^3((v+a)/2)dv<0\quad\forall a\in\mathbb R.}
                                                               \tag{12}
\]

这比只检双pole矩强：整个原件native循环入口不消这个真实关系轨道。raw T*则由(6)保每个非零Pan，正能量同样不下降。

另一方向，native入口还会漏实际非根。取非零非负偶φ∈Cc∞((−1,1))，令

\[
 \psi(u)=u\phi(u),\qquad r_*=(D^2-1/4)\psi.              \tag{13}
\]

r*为非零实奇compact源，μ±(r*)=0，c(r*)=0。由[537](537-source-exact-weil-window-positive-tail-admission.md)的全complex fixed17/16窗定理，

\[
 Q_\zeta(r_*)\ge2^{-49162}\|r_*\|^2>0.                  \tag{14}
\]

非零性也可由compact函数不可能解(D²−1/4)ψ=0直接看出。不用未知零点或Q来选择源。若只取正ψ而非奇ψ，则c((D²−1/4)ψ)<0，所以此scalar保某些非根，却不覆盖所有537源；两种量词不能合并。分支另给两个bump的非奇同类见证。

## 5. 真正接到循环后发生什么

固定finite Schwartz，(2)严格使原件native全Eisenstein derivative乘c(r)，故对正指标n有真实real/complex coefficient cycle map

\[
 C_n(r)=c(r)Z(n).                                      \tag{15}
\]

这是进入原件已证对象的实际线性接入；一般c(r)非整数，不冒称整线丛。q=7,n=1时原件公式给deg Z(1)=2log7>0。由(12)，C₁(p)的算术degree非零，因此不是principal Arakelov divisor；principal需同时包含有限除子及同一函数的arch项，其总degree为0。

现在允许任意fixed linear relative/degree-zero/primitive操作Π，实源/实循环取R线性，复源/复化循环取C线性；目标可以很大且无需假设正性。只要仍经(15)，就有

\[
 \Phi(r)=c(r)\Pi Z(1).                                 \tag{16}
\]

若ΠZ(1)≠0，Φ(p)≠0；若ΠZ(1)=0，整个family为0。若复循环上仅要求R线性，写成Re c(r)ΠZ(1)+Im c(r)Π(iZ(1))；同时消p和ip便迫两项均零，结论相同。统一对所有coefficients/arch/constant作fixed线性操作仍只有同一个c(r)，(13)被杀。fixed degree1参考项、fixed双边界投影、任意事后线性商均不能修复它。这个二择不依赖Hausdorff性、norm或height正性。

于是本次实际构造不是所求relative primitive lift：失败发生在主关系/非根层，早于signed解卷积与RR。新的源依赖frame或非标量关系操作不一定经c因子，未被(16)排除，但须先给公式和principality identity。

## 6. 原费用修复：实际高频源与合法polar逃逸

在raw模型中K=T₀*T₀的乘子w(t)=πsech(πt)。固定compact窗I和非零h∈Cc∞(I)，选同窗两个固定dual模板v±满足μ_i(v_j)=δ_ij。定义

\[
 r_\tau=e^{i\tau u}h(u)-\mu_+(e^{i\tau\cdot}h)v_+
                          -\mu_-(e^{i\tau\cdot}h)v_-.  \tag{17}
\]

模板可由不同位置的两bump矩阵取得，不读Q。两修正系数由反复分部积分为任意阶O_N(τ^−N)。直接用(5)并分频带给

\[
 \|r_\tau\|_{du}^2\to\|h\|^2>0,\quad
 \|r_\tau\|_{Hlog}^2=(\log\tau)\|h\|^2+O(1),\quad
 \|T_0r_\tau\|^2=O_N(\tau^{-N})\ (\forall N).            \tag{18}
\]

不夸大成exp(−πτ)，compact Fourier leakage可能主导该速度。同一源的完整经典型却有

\[
 Q_\zeta(r_\tau)=(\log\tau)\|h\|^2+O_I(1).             \tag{19}
\]

这是完整Γ(t)=log|t|−log(2π)+O(t^−2)的已付高频机制；fixed I的全部prime-power shifts为bounded原du form，两个pole在(17)中精确为零。nativeT*只多固定常数/坐标等距，不改变该费用比较。故bounded Gaussian energy加O(||r||²)不能恢复完整Γ预算；并未证明unbounded arithmetic height的费用也不可能付。

若方案要求**先**K^(-1/2)r∈L²，须有∫cosh(πt)|rhat|²<∞；这给holomorphic strip，非零compact源不可能满足。但不能因此排除direct组合：T₀K^(-1/2)在稠密域的polar factor U确实延为du到radialL²的酉映射。log-radial Fourier只乘Γ(1/2−it)的单位相位及反射。它是真合法补偿；是否回Schwartz/cycles须另外核。

U仍注入，不消405。若再接全域du/Hlog bounded、消全部Pan的Hausdorff Hilbert primitive读出，旧[553](553-principal-cyclic-closure-and-cofinal-readout-fees.md)密度即迫全零并杀537。此为旧直接后果，不另报新no-go。strong Frechet、非有界relative height、源依赖/变域及有费无限完成仍开放。

## 7. 有符号解卷积必须作用于同一实际源像

原件完整Mellin身份保持为

\[
 M_q(s)=\Lambda_0(s)\Lambda_\chi(s)
 \big(\log q+\Lambda_\chi'/\Lambda_\chi-\Lambda_0'/\Lambda_0\big)(s),
 \quad\Lambda_0=\pi^{-s/2}\Gamma(s/2)\zeta(s).            \tag{20}
\]

raw Gaussian的Mellin Γ(1/2−it)不是可以直接替换(20)经典Γ(s/2)的因子。native scalar恒等式则保原件positive-index finite lengths、negative-index arch/Green及constant项，不把零指标自由改名经典pole预算。

对有限F，记B_F(s)=∏_{p∈F}(1−p^−s)(1−χ(p)p^−s)=Σa_F(n)n^−s。原源的真实逆因子操作是

\[
 A_{F,\sigma}r=\sum_n a_F(n)n^{-\sigma}\tau_{\log n}r,
 \qquad T_*\tau_a=D_aT_* .                             \tag{21}
\]

这只识别给定Mellin乘子在原source及Schwartz像上的实际操作；尚未证明它是KRY相对循环上的解卷积functor或height运算，也未识别完整(20)到Qζ的运输。actual像的全部mixed费用正好是

\[
 \|T_*A_{F,\sigma}r\|^2
 ={1\over2\pi}\int2\pi\nu\operatorname{sech}(\pi t)
      |B_F(\sigma+it)|^2|\widehat r(t)|^2dt.             \tag{22}
\]

原du/Hlog finite operator费用可付∏split(1+p^−σ)²∏inert(1+p^−2σ)∏ramified(1+p^−σ)，但不是预定r的实际费用。支撑安全扩大I+[0,2Σ_Flogp]；双pole-zero保持。每个位的二次逆多项式是原完整Euler因子的**精确**逆，不是截掉proper powers。

Reσ>1的全F signed绝对费统一有限；σ=1/2不能免费继承。分支给finite共同phase及长packet的actual成长源费用见证，明确L/τ依F，未把它称为fixed源费用或actual q_R necessary lower。完整Γ逆、无限prime tail、pole及signed交数比较仍未付。

即使只问finiteF能否修native405轨道，答案也是否定的：c(A_Fτ_ap)作为a的函数，其Fourier为非零有限Euler多项式、非零sech乘子及p的Fourier的乘积，故不恒零。不能由有限差分消掉整个实际Pan轨道；某个a上偶然抵消不等于全主关系下降。相应native像仍经一个scalar，(16)的固定relative限制保持。

## 8. 连续正反例及真函数域联检

采用(13)同一个奇源。562/578的native Γ=0连续族d=±1/16各保正primitive分布、双pole和完整对偶。其原公式给

\[
 Q_d(r_*)=2d(d+1/4)^2B_{\psi,d}^2,\quad
 B_{\psi,d}=2\int_0^1u\phi(u)
 \begin{cases}\sin(\sqrt d\,u)/\sqrt d,&d>0,\\
 \sinh(\sqrt{-d}\,u)/\sqrt{-d},&d<0\end{cases}du>0.       \tag{23}
\]

两号Weil值异号且非零，rawT*范数都正，nativec则都为0。故这些外加正能量/scalar不能自动识别native型。未构造这两个分布到CM几何的运输，不能称其满足或反驳KRY定理；它们只反测所提的通用source比较。

真实函数域的对应关系不同：在C×C上完整Frobenius图的双degree primitive化、所有mixed交数及同对象RR/有效截面乘法，独立给Hodge/Rosati正号。这里CM generic-dim0的degree不能替代该二次链。单个Gaussian系数不能编码全部mixed源；保H⁰/H²极点、全returns/aliases，不能只拿一个fundamental频带作比较。旧567/576的真FF正控制仍有效，本次没有新的FF→CM比较map。

## 9. 新旧、净后果与停止

本轮新消费限：actual KRY源Schwartz接口及exact原norm、native循环c(r)Z(n)、405轨道非principal和537显式漏失；连同有费polar逃逸、actual finiteEuler像的完整费用核查，组成一次候选全门。不是新的外部定理或经典独立容量。405Gaussian本身、545预逆/direct区别、552高频机制、553密度、上轮线性degree/signed逆负系数均扣旧。

strongest-old542+555→557 whole leading4/5负惯性**上预算**没有改善；actual q_R、同对象primitive容量、成长core/coupling及Ξ未付。局部前沿从“没有物理源接入”改为“有实际解析/标量循环接入，但principal及coverage精确失败”；核心瓶颈未变。

本recipe及fixed linear relative/primitive修复一轮止。不续Gaussian宽度、只增K投影阶、任意商/unknown height、finiteEuler参数或下一paper。重新准入须一条不再经c因子的实际源/边界公式，先在原S_exp给405主同构与537非零，再核同对象局部过滤、整截面乘法、二次容量及fullΓ/allpowers/poles的signed比较和原费用。变化finiteSchwartz、非局部relative、强拓扑/非有界height、源适应、变域和有费无限完成仍合法，但其名字本身不是输入。
