# 580：有限Schwartz—边界协同、局部cocycle与level塔的覆盖缺口

2026-10-23；接[579](579-kry-physical-gaussian-source-and-native-primitive-obstruction.md)，[C043](../goals/contracts/C043-kry-finite-schwartz-and-relative-boundary-gate.md)统一一轮。独立fresh修后限定PASS、root前件闭合，最终版本与消费范围见[收据](../reviews/2026-10-23/kry-finite-boundary/root-consumption-scope.json)。同G20261014／冻结0c4f；不创建runtime Goal，不将合同结束视为长期目标完成。

实际取得了不经单一c(r)的非标量有限位循环源，以及改变有限位延拓时的明确解析cocycle。它们仍不能同时通过全部405主关系和537非根门。无限单格补回compact源的可见性，却离开原Schwartz域，并有全S_exp的精确盲源；这个盲源的完整经典Weil型无条件为正。独立primitive二次容量仍未取得。

## 1. 对象与去重

唯一外部来源为[Kudla–Rapoport–Yang1999作者版](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)，其§1–3给实际Schwartz／标准section与局部积分，§4给含全部Γ的Mellin式，§5给native特殊循环，§6给负指标arch divisor。一般finite Schwartz的算术推广不是这里可直接引用的既成定理；下述split特例由实际模态问题和局部积分核出。来源事实、下列新计算及未付推论分开。

三份原证明分别是[有限位／实际循环及cocycle](../reviews/2026-10-23/kry-finite-boundary/finite-schwartz-and-actual-cycles.md)、[联合边界／405／原域](../reviews/2026-10-23/kry-finite-boundary/joint-relative-boundary-and-principal-gate.md)、[原费用／全level反测与对照](../reviews/2026-10-23/kry-finite-boundary/original-norm-levels-and-controls.md)。

固定k=Q(√−7)、native Gaussian φ*、加法字符和自对偶Haar，ν=||φ*||²不任意重标。物理源r=e^(u/2)f，原范数是du与zero-extension Dlog；全complex型和noncompact S_exp关系保留。579已付T*r=∫r(u)D_uφ*du及Gram νsech((u−v)/2)。令

\[
 s(u)=\operatorname{sech}(u/2),\qquad
 c_b(r)=\int r(u)s(u-b)du .                         \tag{1}
\]

它们来自同一原源的实际dilation／native投影，不是Q或零点标签。579单c失败、553旧bounded商及552高频机制均是输入，不重记新结果；新增是具体finite循环、局部导数修正及完整level类的精确覆盖／费用门。

## 2. split2：实际非标量源、完整常数与循环身份

在2位取ψ_j=1_{2^jO}，其他finite数据不变，j≥0。标准s-extension的完成化导数为φ_j。局部Whittaker在s0的换元及常数两腿的导数共同给

\[
 \phi_j(\tau)=\phi_0(4^j\tau),\qquad
 a_{0,j}(v)=a_{0,0}(v)-2jh_k\log2 .                 \tag{2}
\]

不是仅缩放正系数：负指标β₁同步以4^jv变化，constant通过局部intertwiner比R_j(0)=1、R'_j(0)=−2jlog2恢复。去constant的完整Mellin满足

\[
 \mathscr M_j(z)=4^{-jz}\mathscr M_0(z),\qquad
 \mathscr M_0=\Lambda_0\Lambda_\chi
 (\log7+\Lambda'_\chi/\Lambda_\chi-\Lambda'_0/\Lambda_0).
                                                               \tag{3}
\]

原完整Γ、伴随χ、全部prime powers都在(3)中。level因子由格固定；没有任意B(z)，也没有因此隔离出经典Weil型。

真实模态对象是(E,ι,z)，y=2^jz，Q(y)=n。其在4^j|n时同构Z(n/4^j)，否则空。split2的special cycles在char2为空；其余位可除性是y杀E[2^j]的étale刚性条件，所以是旧cycle的clopen子问题，厚度相同。不能用“2在base可逆”替代这个可除性证明。取ψ_A=ψ_0−ψ_1后，Z_A=Z−Z_1是真有效补集。n1、n4的degree分别检出两个独立family：

\[
 (\deg Z_A(1),\deg Z_1(1))=(2\log7,0),\quad
 (\deg Z_A(4),\deg Z_1(4))=(4\log7,2\log7).          \tag{4}
\]

令a=log4，定义实际源与实／复系数循环

\[
 \mathcal S(r)=\phi_*\otimes[c_0(r)\psi_A+c_a(r)\psi_1],
 \quad\mathcal C(r)=c_0(r)\mathbf Z_A+c_a(r)\mathbf Z_1. \tag{5}
\]

c_0、c_a独立，(4)保证target也独立，故这确实逃出579的单标量。finite norm μ=||ψ_0||²固定，两个壳支撑不交，全部mixed费用精确为

\[
 \|\mathcal S(r)\|^2=\nu\mu
 (\tfrac34|c_0|^2+\tfrac14|c_a|^2)
 \le4\nu\mu\|r\|_{du}^2.                           \tag{6}
\]

原Dlog亦支付该费；它不是height费。完整输出是c_0φ_0(τ)+(c_a−c_0)φ_0(4τ)，Mellin相应乘c_0+(c_a−c_0)4^-z。constant的degree已付不等于canonical relative链已付；source-dependent signed multiplier也未给有符号逆的正二次容量。

## 3. inert3：同初值不确定导数，明确localcocycle可支付

n27提供实际反测：旧Z(27)厚度为2、degree8log3；要求y=3z的真实模态问题同构Z(3)，厚度1、degree4log3。在相同初值ψ_3=1_{3O}下，标准延拓的局部raw Whittaker为（X=3^-s）

\[
 W_{27,3}^{std}(s)=\tfrac19+\tfrac29X+\tfrac23X^2
                         -\tfrac23X^3-\tfrac13X^4.
                                                               \tag{7}
\]

0值为0，raw导16log3/9；乘原L_3(s+1,χ)后导4log3/3，得到全系数16log3/3。因此几何点筛选、schematic可除性和标准导数三者不同。

这里可给具体解析修正。a_p=p^-1，c_p=χ_p(a_p)^-1|a_p|_p^-1，取

\[
 \Phi^{tr}_{\psi_p}(g,s)=c_p\Phi_0(gm(a_p),s),\quad
 \delta_p(g)=\lambda\psi_p(g)
       \log\frac{|a(g)|}{|a(gm(a_p))|}.               \tag{8}
\]

std、tr在s0同为λψ_p，导数差恰为δ_p；不是任意核标签。在wn(b)上log因子依|b|=p^k为+logp(k≤0)、0(k1)、−logp(k≥2)。局部W^tr_n(s)=p^-s W^0_{n/p²}(s)。全局rational automorphy还保χ_7(p)：inert时c_3=−1/3、χ_7(3)=−1，两负号相乘才得1/3。精确normalization是

\[
 E^{*,tr}(g_\tau,s)=p^{-1}E^{*,0}(g_{p^2\tau},s),\quad
 v^{-1/2}E^{*,tr}(g_\tau,s)
  =(p^2v)^{-1/2}E^{*,0}(g_{p^2\tau},s).              \tag{9}
\]

故classical导数φ^tr(τ)=φ_0(p²τ)。在n27恢复4log3，与schematic可除性一致；std−tr系数差4log3/3。constant亦协同：p3 std为a_0(v)−4h_klog3/3，tr为a_0(v)−2h_klog3，差2h_klog3/3。实际完成化差是原Eisenstein在s0对δ_p⊗其余native sections的值，不能因旧family incoherent就删掉该项。

固定p的compact-picture费||δ_p||≤logp||λψ_p||已付，源系数由原du支付。未付的是全高度／无限p尾费，以及此解析cocycle到同一个算术relative principal链和height的比较。这是明确新局部设施，尚未通过主关系或容量门。

## 4. 全405与537：有限非标量化仍失败

405实际P=(D²−1/4)H，H>0、H∈S_exp，所有τ_bP为真实关系。对任意finite distinct a_j，

\[
 c_{a_j}(\tau_bP)=-\tfrac12\int H(v)s^3(v+b-a_j)dv<0.
                                                               \tag{10}
\]

这些向量随b的complex线性张成是全部C^N：若Σd_jc_aj(τ_bP)=0，Fourier后是一个在0附近非零的因子乘Σd_j e^-ita_j；指数多项式唯一性迫d_j全零。没有裁掉noncompact Pan尾，也没有读取零点位置。

因此，**只经这些finite通道的固定线性relative／primitive读出**若消全部405，就杀整family；固定∂的补偿即使依赖源也不能改变其最终quotient。这不排真正变化的载体／边界算子或读取额外原源的构造。真实Schwartz inclusion S(2O)→S(O)的相对商仍保shell非零，不能把shell手称boundary；手添level边是不同复形。

非线性coverage另有直接反测：在537窗内取N+1个不交bumps ψ_k，解已知矩阵∫ψ_k s³(u−a_j)的零向量，令r=(D²−1/4)Σx_kψ_k。r≠0，双pole矩精确零且全部c_aj=0，而原537给

\[
 Q_\zeta(r)\ge2^{-49162}\|r\|_{du}^2>0.             \tag{11}
\]

选源不读Q；任何只读这些数据、在零数据为零的后处理也漏此源。两个通道能救回579那个特定奇源，但任意有限个通道仍漏别的537非根。局部cocycle若仍仅由同一finite vector加权，也受此门约束。

## 5. 无限单格：合法du费用、compact注入、Schwartz域失守

令ℓ=2log2，e_j=2^j1_{2^jO}、c_j=c_{jℓ}。全部finite向量合法，Gram G_jk=2^-|j−k|。其Riesz上下界1/3、3，sech sampling还有有限Bessel常数A_ℓ，故

\[
 \sum_j|c_j(r)|^2\le A_\ell\|r\|_{du}^2,\qquad
 \|\phi_*\otimes\sum_jc_je_j\|^2\le3\nu\mu A_\ell\|r\|_{du}^2.
                                                               \tag{12}
\]

这是真实际Hilbert源费，不能声称无限level必然发散；未投影raw单位化lift却对每个固定非零r有(N+1)||T*r||²量级实际费用。两种源不可混用norm。

对compact r，c_j=2e^-jℓ/2 F(e^-jℓ)，F(z)=∫r(u)e^{u/2}/(1+ze^u)du在0附近解析。若全部j≥0系数消失，则F全部矩为零，compact区间多项式稠密性给r=0。因此无限半塔已保每个537非根。可是其finite径向值F_n=Σ_{j≤n}2^jc_j若在0附近局部常值，就迫c_j最终零，再迫r=0。**每个非零compact源的无限native塔都不在原Bruhat-Schwartz域中。**

有限截断合法且L²收敛不支付λ、E′、Green／cycle延拓。例如Σ_{j=0}^N(ψ_j−ψ_{j+1})→ψ_0在L²成立，左侧每项在origin为0、极限为1；而λφ(1)=φ(0)。原Schwartz拓扑中的连续boundary评价确实丢失。该障碍只用j≥0，不需负level算术推广；j<0在本轮仅为analytic Hilbert计算。

## 6. 全S_exp精确盲源；完整经典Γ／全部powers／poles逐项检验

compact注入不能外推全S_exp。对任意整数K≥1，A=Kπ/ℓ，取

\[
 R_A(u)=e^{-u^2}\{\sin((A+2\pi)u)
                  +e^{-2\pi A}\sin((A-2\pi)u)\}.    \tag{13}
\]

它是实际非compact S_exp源，不用Q或零点选系数。令g_A=e^-u²sin(Au)；r_A=[g_A(u+iπ)+g_A(u−iπ)]/(4π)是R_A的非零常数倍，且r̂_A=(coshπt)/(2π) ĝ_A。因此

\[
 r_A*s=g_A,\qquad c_j(R_A)=0\ (j\in\mathbb Z),\qquad
 \mu_+(R_A)=\mu_-(R_A)=0.                           \tag{14}
\]

最后两矩由cosh(±iπ/2)=0精确消失。原du范数趋(1/2)√(π/2)>0。完整目标Γ(t)=Reψ(1/4+it/2)−logπ及其固定FP/contact在Gaussian频包上给Q_Γ(R_A)=logA||R_A||²+O(1)，而自相关的实际一致界为

\[
 |h_{R_A}(v)|\le4\sqrt{\pi/2}e^{-v^2/2},\quad
 |P(R_A)|\le8\sqrt{\pi/2}
       \sum_{n\ge2}\frac{\log n}{\sqrt n}e^{-(\log n)^2/2}<\infty.
                                                               \tag{15}
\]

所有Λ(n)包括proper powers都按0≤Λ(n)≤logn付完整尾费；不是prime截断。双pole在源上为零，目标预算没有删除。于是无需RH，

\[
 Q_\zeta(R_A)=\log A\,\|R_A\|_{du}^2+O(1)>0
                  \quad(K\text{充分大}).             \tag{16}
\]

只读全部c_j和双pole矩的zero-preserving relative构造，连此实际正非根也看不到。它是全单格native信息门，**不是**537 compact注入失败；真正额外boundary或continuous源信息仍可逃逸。

允许两prime的正负levels后，jℓ_p+kℓ_q稠密，全部采样为零迫r=0，故不能扩大成全位no-go。但指定**无权单位化**向量的tensor Gram有固定Riesz下界；对每个先固定非零r，c(a)在某个区间≥δ，该区间含无穷densegrid点，所以Σ_jk|c(jℓ_p+kℓ_q)|²=∞。这是实际源费，不是ambient逆norm。衰减权、单边／非Hilbert完成、源适应frames及新算术基没有被排除；其cycle、principal、height身份另欠。

## 7. 连续与函数域对照：真正的二次输入在哪里

连续d=±1/16族以579同一奇compact源检验，native完整Weil值异号；Gaussian、finite Gram及采样数据相同，正Hilbert能量不自动等于分布敏感的signed Weil型。没有continuous→CM运输，故不称这些模型反驳KRY。

真函数域在同一C×C取E_n=q^-n/2(Γ_n−F_1−q^nF_2)，混合交数−E_mE_n=a_{n−m}由同一点数数据给出；primitive Hodge负性来自同对象RR、实际截面乘法／有效性。完整源型是

\[
 Q_C(r)=(\log q)\int_0^{\log q}
          \big\|\sum_jr(y+j\log q)E_{j+j_0}\big\|^2dy.     \tag{17}
\]

这里先取compact源并统一平移j_0使全部活跃下标非负；mixed Gram只依指标差，型不变。全S_exp须另以已证Toeplitz型作独立完成，不假造负Frobenius图。它保全returns／aliases及H⁰,H²的pole角色。这里finite Gram ρ^|j−k|有全rank圆周Poisson谱，只依局部体积；不是由N_n给出的有限维primitive mixed交数。CM线性degree、localcocycle、shell有效性不提供这个同对象运输。

## 8. 净结果、停止与重新准入

新输入：actual非标量循环源及全常数；同初值延拓的明确localcocycle；finite全Pan span／537核；无限level的compact可见性与Schwartz域损失；全S_exp的实际正非根盲源及全Γ／powers尾费；dense双prime指定无权修复的实际费用。没有新的经典Weil正性、独立primitive容量或成长全源有符号估计。

完整KRY signed解卷积到Qζ、405 principal同构、同一整模型上的局部消失过滤／实际截面乘法／mixed二次RR容量仍欠。若把Q拉回新Hilbert完成、将Pan像按定义作boundary、或把已正Gram命名height，只回到旧商／等价改写。独立证明这些接口本身仍是合法路线。

停止本轮有限native通道的fixedrelative与单格Hilbert塔recipe，不续level数、Gaussian参数或下一paper。下一只准入**能读取这些c_j之外原源信息的实际relative边界／算术regulator公式**，或带实际cycle与强拓扑延拓定理的有权非整格族；先核405全关系、537及全S_exp非根、原du/Dlog，再谈同对象容量。若没有该新公式，只保一个章节级来源审查并停止，不另建数学合同。

局部载体／规范／coverage前沿改变；宏观独立容量瓶颈没有改变。strong-old542+555→557 whole leading4/5仍是负惯性UPPER，actualq、成长core／coupling／Ξ未改。固定窗、逐源／D′、强源与成长统一结论不合并，长期Goal保持open。
