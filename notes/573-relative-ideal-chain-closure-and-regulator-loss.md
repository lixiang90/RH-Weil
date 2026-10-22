# 573. 实际相对理想可使链闭合，却不能保留432电荷

2026-10-22。执行[C036](../goals/contracts/C036-relative-ideal-closure-and-regulator-charge.md)。
同G20261014、冻结0c4f，运行Goal现场null，未创建新实例。
本稿的新结果是一个实际理想闭合机制的完整准入反测；没有新增Weil正性、算术容量或ζ成长净预算。
三份独占推导、fresh审阅及root前件闭合另存，数学轮由同一cadence统一结算。

## 1. 新结论：一个537非根源已足阻止旧电荷下降

固定430–432的任意原合法两素数/分割、实际Hilbert表示、原酉u与采样V。令

\[
 A=A_{\rm src}=\operatorname{alg}(1,u,u^*,D_{\rm src}),\quad
 I=\mathcal S_1,\quad Q=A/I,\quad
 F_r=VU(r(-\cdot))V^*,\quad\delta F=F-uFu^*.
\]

此处U为原时间卷积，物理源r=e^(u/2)f；不是实际adelic DGA的Schwartz dilation。
本稿固定430的明确解析扩大域G_M及其A_src；未证明它等于原u/E生成的最小源代数。
后面的P、B等测试边在这个指定扩大域合法，跨到较小代数须重新核准入，不能直接外推。
原weighted链c_r=q(u*)⊗q(uF_r)有b₁c_r=q(δF_r)，432不能对非闭链赋Ω。

**命题。** 可明确选取

\[
 r_*=(D^2-\tfrac14)\psi_*\in C_c^\infty((-17/16,17/16)),\qquad
 \mu_\pm(r_*)=0,\quad Q_W(r_*)>0,
\]

使代数双侧理想

\[
 J_*=\langle I,\delta F_{r_*}\rangle_A \tag{1}
\]

具有以下性质：

1. c_(r*)在A/J_*上形式闭合，但存在T,T*∈J_*，其交换子有限秩且Tr[T,T*]=−4。
2. J_*上不存在限制到I为普通迹的循环线性泛函，不需连续性或正性假设。
   432的Ω也不能沿HH₁(A/I)→HH₁(A/J_*)因式分解。
3. 在C*(A)中，J_*的闭双侧理想恰为overline(D_src)，所以闭商消掉全部原raw源及其有L¹费用的延拓。

第2条同样适用于任何包含J_*的A-ideal；特别排除以一个共同扩大理想使全部weighted源链闭合、
并原样保留432Ω的机制。第3条不等于代数J_*=D_src；也不说商中的纯u部分为零。
不排额外非标量相对边、另一regulator、不同相对pair/强拓扑或有独立比较的无限转移。

## 2. 强旧与新增范围

424已证明自然对称修补的电荷抵消，427已有整个角点域上循环迹扩张的障碍，
431已付有限Gram、本质符号和有限源轨道边界单射，432已有非零HH₁电荷及有限旧轨道修补失败。
它们尚未给出：**由一个真实双moment零非根源的δF生成的新ideal，含哪个非零电荷见证，以及闭包究竟多大。**
本稿(1)和下述有限Γ隔离、−4见证、闭理想识别闭合这一具体缺口，故按C036统一一轮；
对称边、固定probe等旧后果不另计轮。相对原冻结基线，它仍只是限定机制的结构结果，
不满足宏观Goal完成门。strong-old542+555→557 whole leading4/5负惯性上预算、core/coupling/Ξ均未改变。

## 3. 有限Γ隔离：真实新ideal中的角点

记M=log q为旧第二素数周期。430/431给X=(V,uV)、

\[
 \Gamma(x)=[\gamma_{j-i}(x)]_{i,j=0,1}\succeq I_2,
 \qquad\gamma_0=2.
\]

Γ为光滑M周期矩阵。G_M为原光滑、联合M周期、有限传播核代数；
F(B)=XBX*，B∈M₂(G_M)。原件已付actual trace-class余项，故

\[
 q(F(B))q(F(C))=q(F(B\Gamma C)). \tag{2}
\]

对任意C,D∈G_M，取有限核矩阵

\[
 L_{0i}=C M_{(\Gamma^{-1})_{0i}},\quad
 R_{j0}=M_{(\Gamma^{-1})_{j0}}D,
\]

其他行列为零。周期光滑乘子保G_M，所以F(L),F(R)是实际原域元素。
在符号中LΓ=E₀₀C，ΓR=E₀₀D；δA(h)的符号为E₀₀U(h)−E₁₁U(h)。于是

\[
 F(L)\,\delta A(h)\,F(R)=VCU(h)DV^*+S,
 \qquad S\in I. \tag{3}
\]

左右腿按此顺序相消，不要求C,D与周期系数交换。
只使用二阶Γ逆；不写可能无界的无限Gram逆。因I包含于(1)，式(3)将商中的隔离变成真实代数ideal包含。

## 4. 537正窗内的实际源及胞元测试边

选0<L₀<min(M/2,17/16)、0<ε<L₀/8，取I₀⊂⊂(0,M)宽度小于ε，
非负实φ∈C_c∞(I₀)，||φ||₂=1，m_φ=∫φ>0。置φ_n(x)=φ(x−nM)。
取实偶χ∈C_c∞((-L₀,L₀))，χ=1于|t|≤2ε，令

\[
 c_\phi=m_\phi^{-2},\quad\psi_*=-4c_\phi\chi,\quad
 h_0=(D^2-\tfrac14)\psi_*=c_\phi(\chi-4\chi''),\quad
 r_*(t)=h_0(-t)=h_0(t). \tag{4}
\]

紧支分部积分使µ_±(r_*)=0；h₀在差集I₀−I₀上为常数c_φ，故非零。
537给该固定17/16窗内所有非零complex源完整Q严格正，所以r_*确为非根，未预设零点位置。

定义原全线算子

\[
 P=\sum_n|\phi_n\rangle\langle\phi_n|,\qquad
 B=\sum_n|\phi_{n+1}\rangle\langle\phi_n|. \tag{5}
\]

正交胞元给P投影、B*B=BB*=P、||P||=||B||=1。其核局部有限、光滑、联合M周期且有限传播，
故P,B,B*∈G_M。它们是实际代数中额外测试边，不是原u轨道上的形式无限平均。
同胞元矩阵元由c_φ(∫φ)²=1给1，异胞元差集不交h₀支撑，因此

\[
 PU(h_0)P=P. \tag{6}
\]

在(3)中分别取(C,D)=(P,P),(B,P),(B*,P)，利用BP=B、B*P=B*，得到

\[
 VPV^*,\quad T=VBV^*,\quad T^*=VB^*V^*\in J_*. \tag{7}
\]

## 5. −4电荷的有限秩见证与不可下降

430给V*V=M_m，0≤m≤2，充分左端m=0、充分右端m=2。
令ξ_n=Vφ_n，a_n=||ξ_n||²。不同n的ξ_n正交；a_n两端精确为0、2。
算子T在其闭张成空间外为零，在非零ξ_n上有

\[
 T\xi_n=a_n\xi_{n+1},\quad T^*\xi_n=a_n\xi_{n-1},\quad
 [T,T^*]\xi_n=a_n(a_{n-1}-a_{n+1})\xi_n.
\]

充分两端差为0，所以交换子有限秩。对N足够大，

\[
 \operatorname{Tr}[T,T^*]
 =\sum_{n=-N}^{N}a_n(a_{n-1}-a_{n+1})
 =a_{-N-1}a_{-N}-a_Na_{N+1}=-4. \tag{8}
\]

a_n=0的项本来为零，无需不存在的归一向量；不假设m单调。
若τ:J_*→C循环且τ|I=Tr，则τ([T,T*])=0而Tr=−4，矛盾。
更强地，ζ=q(T)⊗q(T*)∈Z₁(A/I)且Ω(ζ)=−4，但其在A/J_*的链像直接为0。
故不存在任意泛函Ω_J使Ω_J∘π_*=Ω，甚至不只限于trace型构造。
这是**原432电荷不能因式分解**，不是432电荷本身不规范。

## 6. 范数闭ideal的完整识别及源尾费用

设barJ为(1)在C*(A)中生成的闭ideal。D_src是A-ideal，故barJ⊂overline(D_src)。
由(7)，对原F_(i,j)(C)=u^iVCV*u^(−j)，原乘法及γ₀=2给

\[
 F_{i,0}(C)(VPV^*)F_{0,j}(D)=4F_{i,j}(CPD)+S,
 \quad S\in I. \tag{9}
\]

所以所有F_(i,j)(CPD)∈J_*。取f,g∈C_c∞(0,M)、ℓ∈Z，
C=Σ_n|f_(n+ℓ)><φ_n|、D=Σ_n|φ_n><g_n|，则CPD为胞元Laurent秩一块。
431 §6已付这些块在overline(G_M)=C(S¹)⊗K(L²(0,M))中的范数稠密。
实际F_(i,j)的norm≤2||B||使该稠密性传到原表示，遂得

\[
 \boxed{\bar J=\overline{D_{\rm src}}.} \tag{10}
\]

不删去闭包，不声称代数J_*吞全部D_src。式(10)只灭原源ideal，不灭纯u商。
compact r的F_r当然被灭；对任意r∈L¹，还有自然bounded raw延拓，

\[
 \|F_r-F_{r_n}\|\le2\|r-r_n\|_1,\quad r_n\in C_c^\infty,\ r_n\to r\ (L^1). \tag{11}
\]

故C*商也消全S_exp的该raw map，包括Pan及所有非根。
这只是C*目标上的付费延拓，不自动扩展430的HH₁/trace-class链域；
全线du/Dlog不是统一L¹尾范数，不能抹掉(11)的尾费用。

## 7. 原源费用、范数角色与成长范围

对supp r⊂[−L,L]，真实源map满足

\[
 \|F_r\|\le2\|r\|_1\le2\sqrt{2L}\|r\|_{du}
 \le2\sqrt{2L/\log2}\|r\|_{Dlog},\qquad
 \|\delta F_r\|\le2\|F_r\|. \tag{12}
\]

所选r_*另有||r_*||_du≤c_φ(||χ||₂+4||χ''||₂)，Dlog由光滑紧支有限。
缩小φ支撑可能增大c_φ，未给统一免费源构造；只需每个固定合法模型中的实际源。
有限Γ逆norm≤1、P/B norm1、T norm≤2；trace-class余项准入使用指定核的光滑半范数，
未声称由任意r的du单范数统一控制其trace norm。
P/B是检验ideal的额外合法测试边，不是假定物理源产生这些边的低费用lift算法。
本稿没有把全空间下界当实际源必要费用，也没有给ζ成长尺度正性或低频core改善。

原operator norm下的链projective估计仅为代表费用，不宣称Ω在该完成中连续。
I在整个B(H)的operator norm不闭，不能据此直接判A/I是否分离；431已付D_src∩K=I。

## 8. 新相对边：可闭合，非零数值来自另一个闭循环

对每个原compact r，

\[
 z_r^0=c_r-q(F_ru^*)\otimes q(u)
 =1\otimes q(F_r)-b_2(q(u^*)\otimes q(u)\otimes q(F_r))
\]

确为闭链，原提升交换子严格相消，Ω(z_r⁰)=0。这是424在现域的直接旧实现；
不声称它的HH₁类为零。任何另一个修补与它之差均为闭一循环ζ_r，非零charge全来自Ω(ζ_r)。
闭性方程本身不选择ζ_r，更不选择算术比较。

已有真实角点闭循环ζ_(r,k)=q(A(r(−·)))⊗q(A(k))给

\[
 \Omega(\zeta_{r,k})=4\int u r(u)k(u)du. \tag{13}
\]

固定compact k的全线du精确费为4||uk||₂；Dlog精确平方dual费为
(16/2π)∫|widehat(uk)(t)|²/log(2+|t|)dt。
取k=u·overline(r₀)可保537，取k_r=u·overline(r)得正量4||ur||₂²，fixed窗≤4L²||r||du²。
但非零固定probe必失败某个405主关系P=Cp的实际平移：若4∫uk(u)P(u−a)du恒零，
Fourier乘积与widehatP非零a.e.迫uk=0。源依赖正量对P亦正，不能消关系。
这些是553强旧的具体测试，不计为本稿新ideal结论。
标量表达式的S_exp延拓不等于实际HH₁链域延拓；crop不是主关系。
只在compact源构造闭链时Pan∩C_c∞=0，不能宣称全405关系已通过。

## 9. 独立算术输入、正反控制与完整Weil项

同一P¹_Z的真实L_n=Z[X,Y]_n、(p^k,z^m) jets/整数kernel、
F_n^(a,m)=p^a z^m Z[z]_(≤n−m)乘法过滤及固定metric的log#~a n²仍是可用正控制。
真曲线restriction的δ(y)先是gluing障碍；δ=0后须actual global lift及原metric费用。
本稿没有从closedHH₁ charge产生这些对象。用有限个(13)作截面坐标虽有费，
若保持该全线连续延拓且全Pan下降，每个坐标由553为0；仅给正det/二次容量不补源桥。

连续d=±1/16的同类resolution/闭链设施可有相同代数、评价和局部有效性，
保真实dagger的Weil型却为2|A|²+2d|B|²，故新增HH₁电荷本身不付正极化。
函数域正例额外使用真C×C的对应、有效截面乘法、signed RR/Hodge及全部periods身份，
不能将局部交换子trace−4等同primitive交数。所有H⁰/H²与period aliases保留。

经典目标继续为568的完整物理规范

\[
\begin{aligned}
 Q_W(r)={}&2\Re(\mu_+\overline{\mu_-})+
 [\psi(1/4)-\log\pi]\|r\|_{du}^2\\
 &+\tfrac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}
           \|\tau_vr-r\|_{du}^2dv
 -2\sum_{p,k\ge1}(\log p)p^{-k/2}\Re(r*r^*)(k\log p).
\end{aligned} \tag{14}
\]

Γ/contact、全部pp、双pole/complex mixed均未省略，也未被(8)识别为新截面容量。
若只规定修补后charge=(14)且positive，仍是Weil等价/充分包；
独立新输入须从同一filtered整模型、可解截面及容量定理证明该身份和原费用。
底层使用旧谱商不自动排除新几何，但重新命名闭循环并不提供它。

## 10. 停止范围、下一准入与原件

本轮新增的净数学内容是(1)–(10)的actual minimalideal反测，不是新的RH正性。
任何包含所选δF_(r*)且要求原432Ω沿自然商下降的ideal修复都会失败；
norm-closed版本还丢全部raw源。该结论不排新的相对复形保留被杀的−4电荷作为边/角transgression。
若改regulator或目标，需要实际构造这份新数据并给fullPan/r₀/双degree及原norm比较。

有一个可直接给出的合法修复控制：保留商映射π:Q→Q_J=A/J_*的两层相对复形
R_n=C_n(Q)⊕C_(n+1)(Q_J)，d(x,y)=(bx,πx−by)。
则Ω_rel[(x,y)]=Ω([x])在H₁(R)上定义良好；(ζ,0)为真实相对循环且Ω_rel=−4。
若它为相对边界，其首分量ζ必为Q中的Hochschild边界，与Ωζ=−4矛盾。
所以被单商丢掉的电荷确可在这个实际pair中保留，不需H-unital/excision认同。
但(c_r,y)成为R循环仍要求bc_r=0，第二腿不能消掉其首分量边界；
这份pair及−4类尚未给出所求全源F_r的闭链映射，更未给整模型/filtered截面。
它是标准相对锥在本实际对象上的控制，不另计新轮，也不能将本稿边界扩成“所有relative ideal皆失电荷”。

在此停止理想扩大和对称边/probe参数，不续cell宽、shift幂或未知HH标签。
下一须给一个**不能被本商遗失的实际相对二层电荷/边数据**及其源映射：
闭性、原432电荷的变换律、405全关系相容、537保留与同一整模型过滤/lift分别核；
否则仅保已有准入反测，不自动开下一合同。保非标量边、不同relative pair、强拓扑/变域、
源依赖family及有独立收敛费用的无限传递等合法逃逸。
较小的原始源代数若尚未包含本稿P/B及Γ隔离乘子，也不由此反测排除。

独占原件：[新边](../reviews/2026-10-22/relative-chain-closure/new-edges-and-regulator-charge.md)、
[新ideal](../reviews/2026-10-22/relative-chain-closure/enlarged-ideal-and-trace-descent.md)、
[闭charge与算术](../reviews/2026-10-22/relative-chain-closure/closed-charge-source-and-arithmetic-tests.md)。
原proof主要用430/431/432已付的实际乘法与norm；本稿有限Γ/胞元/trace证明直接给出。
定点文献背景[Bräunling 1311.4202v2 Theorems1–3](https://arxiv.org/html/1311.4202v2)说明
excision/local-unit前件及相对链之间的比较；未无证明套用其到本ideal，更不由excision推出正号或规范源map。
本文A为unital，432的HH₁构造直接核定义；不将新的nonunital ideal的naive复形自动认作correct cyclic homology。
