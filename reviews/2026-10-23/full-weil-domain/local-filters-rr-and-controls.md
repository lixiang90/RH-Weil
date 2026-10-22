# Full local Weil强域：局部过滤、真正的λ核与同对象RR责任

2026-10-23；独占分支原件，提交root消费前为draft。不改STATE／cadence。输入为581的实际A1、J_w、完整预算和边界方向；本分支只付局部过滤与明确额外源候选的门，不领取算术Green／primitive容量。

## 1. 原对象、源与外部知识的边界

固定k=Q(√−7)、split2／11、native加法字符、自对偶Haar、无穷位Gaussian φ*与ν=||φ*||²。physical r=e^(u/2)f遍历ALLcomplex S_exp；原du和zero-extension Dlog不换。581的

\[
 F_w(r)=\sum_{j,k}H_{jk}^{-2}c_{a_{jk}}(r)e_{jk},
 \quad a_{jk}=2j\log2+2k\log11,
 \quad c_a(r)=\int r(u)\operatorname{sech}((u-a)/2)du
\]

已在A1中给全源注入及原范数上界，不再重复算新。具体候选大域是两个局部Feichtinger空间的projective tensor

\[
 \mathcal B=S_0(\mathbb Q_2^2)\widehat\otimes_\pi
                S_0(\mathbb Q_{11}^2).
\]

S0的定义取compact-open窗口的STFT L1范数，包含Bruhat–Schwartz，连续进入L1∩C0∩L2；translation／modulation以及Fourier有界。这些是既有调和分析设施，而非本轮算术新定理。原件可核[Enstad–Jakobsen–Luef2019 §3](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2018.12.004.pdf)的p-adic／adelic模型及[Jakobsen的LCA综述](https://arxiv.org/abs/1608.04566)。本分支以下局部命题直接由Weil生成元证明，不调用“所有λ读出分离整个S0”这一错误断言。

full local作用和A1→B的具体费用由同轮强域分支单独交付；本分支使用它时明示该依赖。不把S0 Banach范数、Weil Hilbert范数、算术height和截面容量相互替代。

## 2. 真实局部消失过滤存在，但不是单个Weil不变乘法理想

先只取一个split位p，V=Qp²，Q(x,y)=−xy；B_Q为其非退化polar pairing，全部Fourier按这一pairing和native selfdual Haar。局部Weil生成元为

\[
 \omega(n(b))F(x)=\psi(bQ(x))F(x),\qquad
 \omega(m(a))F(x)=\chi(a)|a|_pF(ax),\qquad
 \omega(w)F=\gamma_Q\widehat F.
                                                        \tag{1}
\]

这里|γ_Q|=1。定义闭理想I0={F∈S0:F(0)=0}。n(b)保I0，m(a)也保I0；但w把I0变为积分为零的闭子空间，而非同一个点消失理想。具体取L=Zp²、0∉a+L，F=1_(a+L)，则F(0)=0、∫F=1，故(ω(w)F)(0)=γ_Q≠0。p2可取a=(1/4,0)，避免误用a=1/2导致a+L与−a+L相同。

对U_N=p^N Zp²，条件F|_(U_N)=0也给真实闭子空间和乘法理想。n(b)保持；m(a)协同移动U_N；Fourier后变成一族积分条件

\[
 \int F(y)\psi(B_Q(x,y))dy=0\quad(x\in U_N).
                                                        \tag{2}
\]

因此可保完全合法的covariant family I_(g,N)=ω(g)I_N；失败的是“在每个Weil帧仍是原乘法下同一个point ideal”这一额外要求。它不排除带对偶极化的过滤族、非交换对象或另有代数结构的真实几何。

这些native开闭过滤尚不是Cartier消失阶。限制在一个固定compact-open K上时，S0(K)有单位1_K；U⊂K开闭，消失于U的理想由idempotent 1_K−1_U生成，其理想平方仍等于自身。它只记支持，不产生Cartier幂次增长。若再先固定局部常值level p^M，则U_N上的限制空间为有限维，维数p^(2(M−N))（M≥N）；放开M后又无限维。这个可计算局部容量不是全局surface RR的二次系数。未排有独立regular／Cartier结构的另一种过滤。

还有一个必须先过的typed门：S0保完整Weil作用且保点乘／卷积，不意味着ω是同一乘法代数的automorphism。n(b)已经精确给

\[
 \omega(n(b))(FG)=\psi(bQ)FG,\qquad
 [\omega(n(b))F][\omega(n(b))G]=\psi(2bQ)FG.            \tag{2a}
\]

取F=G=1_(Zp²)、b=p^−1，在x=y=1处两边不同；p2时分别为−1与1。Fourier另将点乘换成卷积。因此full-Weil Banach函数域不能未经桥接就当作equivariant DGA／Cartier层或算术截面乘法。合法修复可以采用tensor／分次对象、line cocycle或transported乘法与过滤，但这些修复及同对象算术身份须实际构造；本差式不排所有filtered或graded路线。

## 3. full λ的准确核：新增局部Weil作用不等于全部函数可见

定义λ_p(F)(g)=(ω(g)F)(0)。对F∈S0⊂L1，Q_*F是由

\[
 (Q_*F)(A)=\int_{Q^{-1}(A)}F(x)dx
\]

定义的有限复测度。SL2(Qp)=B∪BwN的Bruhat分解及(1)给精确命题

\[
 \boxed{\ker\lambda_p=
    \{F\in S_0:F(0)=0,\;Q_*F=0\}.}                    \tag{3}
\]

证明：小cell的读出是非零标量乘F(0)。大cell的基本读出为

\[
 \lambda_p(F)(wn(b))=
       \gamma_Q\int F(x)\psi(bQ(x))dx
       =\gamma_Q\widehat{Q_*F}(-b),                    \tag{4}
\]

其余left-B只乘非零标量。有限复测度的Fourier唯一性给(3)，反向由同一公式立即成立。S0的L1及有界点读出使公式全部合法；没有用未知零点或Weil正性。

等价地，(3)正是包含于I0的最大full-Weil invariant线性子空间：K=∩_g ω(g)^−1I0。K不是零空间。因此不能声称“把pointzero要求加到全部g后必把所有F杀掉”，也不能把λ_C在579实际radial arch源上的注入误推广到全部finite S0。

最便宜的非零核元素是odd coset。p2取L=Z2²、a=(1/4,0)，

\[
 h_o=1_{a+L}-1_{-a+L},\quad \|h_o\|_2^2=2.             \tag{5}
\]

两个coset不交，h_o≠0。Q为偶函数，所以Q_*h_o=0且h_o(0)=0；反射x↦−x与完整Weil作用交换，所有λ读出均为零。

核并不只由odd函数组成。p2另取L'=4Z2²、a'=(1,1)、o=diag(2,1/2)∈O(Q)，并置

\[
 G=1_{a'+L'}+1_{-a'+L'},\qquad h_e=G-G\circ o^{-1}.
                                                        \tag{6}
\]

四个coset两两不交：前两者坐标均为2-adic units，后两者第一坐标valuation1、第二坐标valuation−1；每个coset体积1/16。故h_e非零even、||h_e||²=1/4，且h_e(0)=0。o保Q且det o=1，换元给Q_*h_e=0，所以h_e∈kerλ。它不被简单±配对形式上消掉；是否在本CM模型上仍因真实toric／principal关系消失，必须另核，不能预报其Chow或Green类非零。

全两位λ至少包含kerλ_2⊗S0(Q11²)及对称另一项。这里不宣称全两位核仅由这两个tensor核相加；无需该更强结论即可反驳全S0可见性的误用。

## 4. 一个真正读取额外物理源的解析map；为何尚未是算术regulator

保579的actual T_*r=∫r(u)D_uφ*du。它在S_exp→arch Schwartz上连续且注入，并有原du费用

\[
 \|T_*r\|_2^2\le2\pi\nu\|r\|_{du}^2.                  \tag{7}
\]

以(5)为固定非零finite腿、另一位取e0=1_(Z11²)，定义

\[
 Y_or=T_*r\otimes h_o\otimes e_0.                       \tag{8}
\]

这是不经c(r)、不以Qζ或未知零点作标签的实际非标量源。它在原S_exp上进入arch Schwartz⊗finite Bruhat，注入且保每个537非根；若其余native腿范数因子记μ，则

\[
 \|Y_or\|^2\le4\pi\nu\mu\|r\|_{du}^2.                 \tag{9}
\]

原Dlog也支付该Hilbert费用。Schwartz半范数沿用579带权S_exp费用；fixed窗按其支撑L支付，不能由(9)冒称全Schwartz-du统一费。

但finite h_o∈kerλ，故标准section恒零、标准extension在全部s恒零；所有经同一λ及其标准Eisenstein导数的读出也为零。KRY型按特殊向量y计权的循环及只依赖Q(y)的native Green读出还受y↔−y配对：h_o(−y)=−h_o(y)，实际模态involution保持其厚度及Green项；只要这项weighted moduli读出在相应level定义，其odd加权和就抵消。这个直接失败只针对(8)的odd候选，不排kerλ中even元素的degree-zero arithmetic geometry，也不排具有额外boundary／Green数据的新regulator。

改用(6)也给同样合法而更小Hilbert费用的Y_e；其标准section仍零，而实际cycle／Green的toric比较未付。不能把它的非零局部函数像升级为非零算术类。

更明确地，||h_e||²=1/4使||Y_e r||²≤(πνμ/2)||r||du²。两个finite核腿都是实际Bruhat函数，故其S0范数是固定有限常数；这并不使arch Schwartz的全部半范数都得到同一du上界。k=Q(√−7)的class-number-one与native coarse模型还可能使特定degree-zero类本身消失；尚未核的cycle／Green比较必须在该真实模型先做，不能借large kerλ预报非零Pic0，亦不能把该模型的低维容量门推广到更高CM、算术曲面或open relative对象。

若把(8)附加到581 J_w，可以取同一实际函数和

\[
 X_r=\phi_*\otimes F_w(r)+Y_or .                        \tag{10}
\]

finite第一项在p2为even，第二项odd，故两项Hilbert正交，全部mixed项精确为零；各自费用相加即可。新的解析输出保全源，但标准λ输出和完整解析预算仍等于J_w的旧输出，额外源未被读取。这个“保留额外信息”的合法map尚未给arithmetic transgression，不构成容量新输入。

405首先阻止把(10)直接叫相对primitive。实际P=(D²−1/4)H、H>0与每个平移仍满足

\[
 c_a(\tau_bP)=-\tfrac12\int H(v)
           \operatorname{sech}^3((v+b-a)/2)dv<0 .       \tag{11}
\]

所以J_w原finite origin／integral及真实S-unit charge均不消失；加上λ零的Y_o不能取消这个charge。T_*的注入另给Y_o(τ_bP)≠0。若宣布把这些实际向量按定义商掉，只重建405旧商；若用任意chosen boundary全吞，须同时核537与真实principal身份，581已展示反向Koszul并不满足这一责任。

## 5. 强域费用不支付同对象primitive RR；完整预算的严格反测

设同轮强域分支已付连续嵌入A1→B，常数C_B固定。580／581明确的全S_exp双polezero源R_A满足

\[
 (R_A*s)(a)=4\pi e^{-\pi^2-\pi A}e^{-a^2}\sin(Aa),
 \qquad \mu_\pm(R_A)=0,
\]

其中s=sech(u/2)、A→∞。于是原A1定义直接给

\[
 \|F_w(R_A)\|_{A_1}
  \le4\pi e^{-\pi^2-\pi A}\sum_{j,k}H_{jk}^{-1},\quad
 \sum H^{-1}=\frac{18}{5}.                            \tag{12}
\]

固定g的ω(g)在B有界，所以任何固定有限个局部Weil帧的B读出仍指数小；其费用依g，不声称全g统一。有限个有界linear postprocessing同样无力给源的完整Weil容量。

反面是581已经支付的同一R_A完整目标

\[
 Q_\zeta(R_A)=(\log A)\|R_A\|_{du}^2+O(1),\qquad
 \|R_A\|_{du}^2\longrightarrow\tfrac12\sqrt{\pi/2}>0.
                                                        \tag{13}
\]

其中Γ(t)=Reψ(1/4+it/2)−logπ及FP/contact先完整进入型；全部素数幂按

\[
 |P(R_A)|\le8\sqrt{\pi/2}\sum_{n\ge2}
       \frac{\log n}{\sqrt n}e^{-(\log n)^2/2}<\infty
\]

支付无穷尾，双pole在实际源上精确为零而非从目标删除。这拒绝由有限个B有界局部帧范数推出Qζ≤CΣ||ω(g_i)F_w(r)||_B²+C0||r||du²的recipe。它是旧552高频／579Gaussian平滑机制在本实际强域中的核验，不是新classic正性或成长结果。

原537窗还可用581 §5.2的全部complex r_T：compact双polezero模板修正后，所有c_a一致O_N(T^−N)、原du范数不退化而Qζ~logT。此fixed窗反测与非compact R_A不同，不能混为成长窗结论。允许g随T增长、有明确付费的无界height、不同source-aware map或读取原r的真实Green项；(12)不排它们。

同对象RR仍须独立交付：实际算术载体和由r给出的可移动primitive循环；405每个全主关系的真实principal同构及537非根保留；局部消失量的schematic过滤、截面lift与乘法；global二次RR和fixed容量／可控误差；最后把完整Γ／proper powers／双pole预算与同一交数相认。按定义把Qζ拉回B的像、或规定其为未知height，只是等价组织。单纯S0函数乘法和(2)的可检验消失条件没有给这些算术前件。

## 6. 连续正反例和真实函数域对照

连续d=±1/16的native模型使用同一compact奇源r*=(D²−1/4)(uφ_even)、φ_even≥0非零，完整Weil分布分别为2cos(u/4)du和2cosh(u/4)du。其全部Euler repeats及双pole已包含、native Γ=0。分别得到

\[
 Q_+(r_*)=2\left|\int r_*(u)\sin(u/4)du\right|^2>0,
 \quad Q_-(r_*)=-2\left|\int r_*(u)\sinh(u/4)du\right|^2<0.
                                                        \tag{14}
\]

同一B、J_w、localWeil作用、局部过滤和extra vector的正Hilbert费用不能区分(14)。故这些universal local facilities不自动给distribution-sensitive signed身份。没有continuous→CM几何运输，不能称(14)反驳某个已构造的KRY算术cycle定理；也不能把Γ0的模型伪称保留classicΓ的反例。

真曲线C/F_q的两个finite places norm为q^degP、q^degQ，所以两步长总相称；不领取2／11 densegrid的全源注入。567中同一C×C给真实primitive correspondences

\[
 E_n=q^{-n/2}(\Gamma_n-F_1-q^nF_2),\quad
 -E_mE_n=a_{n-m},\quad
 a_n=q^{-|n|/2}(q^{|n|}+1-N_{|n|}),\quad a_0=2g,
\]

以及全returns公式

\[
 Q_C(r)=(\log q)\int_0^{\log q}
       \left\|\sum_jr(y+j\log q)E_{j+j_0}\right\|^2dy.
                                                        \tag{15}
\]

compact源取统一j0使所有真实Frobenius图指标非负；全S_exp使用已证Toeplitz完成，不假造负Frobenius。正号来自同一几何对象的RR、有效性、截面乘法和Hodge／Rosati，而非local Weil的“unitary”字样。H0/H2 poles、全部period aliases及proper powers均保留。换S0域或加入局部covariant family不会自动运输这条primitive mixed身份。

## 7. 消费范围与停止条件

本分支付了：真正covariant的点／开闭过滤、全λ准确核、odd及even明确非零核函数、读取原r的非标量解析extra候选及原Hilbert费用、其405／537与原完整预算门。S0大域与其生成元有界是独立调和分析设施，但“因此已有算术regulator／RR”不成立。

停止把pointfilter设为单一full-Weil invariant乘法理想、把extra kernel向量或有限个有界局部帧直接叫primitive容量的recipe。保degreezero arithmetic cycle、真实toric／boundary transgression、有费无界Green、source-aware强域和covariant filtered family。下一必须给同一对象上的实际principal／cycle／Green比较及其norm／高度运输；全λ核本身只是最小责任定位，不能按零谱标签定义答案。

宏观独立二次容量及542+555→557 whole leading4/5负惯性UPPER未改；不领取actualq／成长core／coupling／Ξ或长期Goal完成。
