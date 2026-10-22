# 582：完整局部Weil强域、实际Green源与primitive首门

2026-10-23；接[581](581-arithmetic-weighted-two-prime-completion-and-relative-capacity-gap.md)，[C045](../goals/contracts/C045-full-local-weil-domain-and-actual-green-source.md)一轮。独立fresh最终限定PASS、root前件闭合，最终版本见[收据](../reviews/2026-10-23/full-weil-domain/root-consumption-scope.json)。保G20261014／冻结0c4f，不创建runtime Goal，不将合同结算当宏观完成。

第一项设施可以完成：A1确能嵌入一个有实际函数身份、保完整局部Weil作用的强域，费用可算。第二项得到一个读取整个物理源的native循环／Green family，而非只读c(r)；但该family未消405主关系。局部消失过滤及全Weil稳定不自动给算术regulator或primitive二次RR；本轮没有经典Weil正性的新证明。

## 1. 来源、对象与本轮新增责任

S0／Feichtinger空间本身是既有调和分析设施，原件见[Enstad–Jakobsen–Luef2019](https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2018.12.004.pdf)。本轮直接核实际二维split模型的原子、矩阵费用及581源的运输；不将既有理论冒称新外部定理。native算术对象及Green核仍用[Kudla–Rapoport–Yang1999](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf) §1、§5、§6。一般Schwartz／full-Weil算术cycle functor并未由该原件给出。

原证明为[完整局部强域与源费用](../reviews/2026-10-23/full-weil-domain/full-local-domain-and-source-fees.md)、[实际循环／Green与principal门](../reviews/2026-10-23/full-weil-domain/actual-regulator-cycle-and-principal-test.md)、[局部过滤／λ核／容量对照](../reviews/2026-10-23/full-weil-domain/local-filters-rr-and-controls.md)。

固定k=Q(√−7)、split2／11、nativeQ／ψ／Haar／Gaussian φ*及ν=||φ*||²，原physical r=e^(u/2)f遍历ALLcomplex S_exp。du、zero-extension Dlog、Schwartz半范数和算术height严格分开。581的H_jk=2^|j|11^|k|、w=H^-2、e_jk、c_a及F_w(r)保持原定义，不按Q或零点选取。

## 2. 非抽象的full-local强域；A1的费用得到运输

在V_p=Qp²、Q(x)=−x₁x₂、自对偶L=Zp²取window g=1_L。以B_Q极化定义STFT，实际原子

\[
 h_{a,\xi}(x)=\psi(B_Q(x,\xi))1_{a+L}(x),\quad
                  (a,\xi)\in(V_p/L)^2
\]

是L²正交标准基。STFT绝对值在每个phase-space coset恒定、每块体积1，所以

\[
 \|F\|_{S_{0,p}}=\int|V_gF|=\sum_{a,\xi}|\langle F,h_{a,\xi}\rangle|.
                                                               \tag{1}
\]

这是实际C₀∩L¹∩L²函数的Banach强域，原Bruhat函数稠密；不是把L²改名Schwartz。点乘／卷积有界、Fourier等距，origin与integral连续。normalized球满足精确费用

\[
 \|p^j1_{p^jL}\|_{S_{0,p}}=p^{|j|},\quad
 A_1\hookrightarrow\mathcal B:=S_{0,2}\widehat\otimes_\pi S_{0,11},\quad
 \|F_w(r)\|_{\mathcal B}\le{36\over5}\|r\|_{du}.     \tag{2}
\]

H恰是这条算术格轨道的S0范数；权指数2仍不是被唯一确定的正极化。范数控制全部实际合成与mixed项，Dlog亦支付。

完整Weil生成元的精确范数为

\[
 \|\omega(n(b))\|=\max(1,|b|_p),\quad
 \|\omega(m(a))\|=\max(|a|_p,|a|_p^{-1}),\quad
 \|\omega(w)\|=1 .                                  \tag{3}
\]

chirp证明直接积分ψ(−b x₁x₂)：|b|>1时有|b|²个Fourier系数，各模长|b|^-1；包括p2而未除2。K=SL₂(Zp)等距，Cartan分解因此给不依赖word的精确式

\[
 \boxed{\ \|\omega(g)\|_{\mathcal B(S_{0,p})}
              =\theta_p(g):=\max_{i,j}|g_{ij}|_p\ },\qquad
 |\lambda_p(F)(g)|\le\theta_p(g)\|F\|_{S_{0,p}} .    \tag{4}
\]

作用强连续；不是算子范数连续或全群统一有界。其余finite位可保原Bruhat并作restricted tensor；bad7保真实对偶格，不借split θ常数。arch可保Schwartz或取Gaussian-window S0；每个固定real Weil元素有界。故fixedarch φ*⊗F_w进入完整局部／adelic强域的原du/Dlog费用已付。原Bruhat并未恢复，也未因此扩张Eisenstein总和、Green／cycles或regulator。

若读取额外raw arch源T*r=∫rD_uφ*，S_exp上仍合法且注入，但真实维数2的Gaussian STFT给

\[
 \|T^*r\|_{S_{0,\infty}}
   \le4\sqrt\nu\int|r(u)|\cosh(u/2)du .              \tag{5}
\]

这是强源半范数。实际双polezero平移源r_T=τ_Tr₀有原du／Dlog固定，而T*r_T=D_TT*r₀的L∞范数为e^{T/2}||T*r₀||∞，所以不能借(2)宣称raw源有全线强范数du统一费。这里用sup而非origin：双polezero会使origin本来为零。

## 3. 局部过滤与全λ核：更多可操作函数不等于更多算术信息

I₀={F:F(0)=0}是真闭乘法理想，但Fourier将它变成integral-zero子空间。开闭U_N上的消失理想也可实际运输为ω(g)I_N；它不必在每帧仍是同一点乘理想。固定compact-open块内这些支持理想由idempotent生成，I_N²=I_N，不产生Cartier幂次消失增长。其固定level有限维费用不是surface RR。

另一类型门是Weil作用不是同一点乘代数的automorphism：

\[
 \omega(n(b))(FG)=\psi(bQ)FG,\qquad
 (\omega(n(b))F)(\omega(n(b))G)=\psi(2bQ)FG .         \tag{6}
\]

F=G=1_L、b=p^-1已给实际差，p2在(1,1)处为−1与1。Fourier还交换点乘／卷积。因而(1)的代数与群稳定性不能直接领取equivariant DGA、Cartier层或算术截面乘法；分次tensor／line-cocycle／transported结构仍可另行构造，未被排除。

full λ也不分离全部S0函数。对有限复测度Q_*F，Bruhat两cell与Fourier唯一性给

\[
 \ker\lambda_p=\{F\in S_{0,p}:F(0)=0,\ Q_*F=0\}.
                                                               \tag{7}
\]

它是I₀中最大的full-Weil稳定子空间，非零。原证明给odd coset h_o，也给even的O(Q)-差h_e，两者都是真Bruhat函数。故Y_or=T*r⊗h_o⊗e₀是读取全部原r、注入、原Hilbert费用≤4πνμ||r||du²的合法额外源，却被所有标准λ／Eisenstein读出杀掉；加到F_w不能取消405旧电荷。even核不能按±配对一概消除，但其非零函数也不等于非零算术Chow类。

这些结论仅停止指定kernel编码／点理想recipe，不排真实toric／degreezero／relative／higher几何。任何越过λ读取该额外信息的算术regulator必须另给实际映射。

## 4. 实际额外Green源：保整数频率、全源可见、逐项原费精确

保原native finite腿，采用arch-only全s right transport

\[
 \Phi_r^{tr}(g,s)=\int r(u)\Phi_0(gm(e^{u/2}),s)du,\quad
 \phi_r^{tr}(x+iv)=\int r(u)e^{u/2}\phi_0(x+i v e^u)du .
                                                               \tag{8}
\]

只变v、不变x；不是φ(e^uτ)，整数Fourier频率n保留。s0输入恰是T*r，通常不是其standard s-extension；两导数差的真实δ_u=λ(D_uφ*)log(|a(g)|/|a(gm(e^{u/2}))|)及其E(0,δ)必须保留。

对n,m>0，以e^{2πinx}为Fourier约定，定义native实／复divisor family

\[
 L_{n,v}(r)=\int r(u)e^{u/2}e^{-2\pi n v e^u}du,\quad
 \mathcal Z^+_{n,r}(v)=L_{n,v}(r)Z(n),                 \tag{9}
\]
\[
 \mathcal Z^-_{m,r}(v)=\int r(u)e^{u/2}e^{2\pi m v e^u}
                              Z(-m,v e^u)du .       \tag{10}
\]

每个positive项是实际有限cycle的complex加权，negative项在有限complex places上积分原β₁ arch divisor。不是整cycle、K-regulator或full-Weil cycle functor；按e(nτ)展开还须补相应exp因子。

原du核费用精确为

\[
 \|e^{u/2}e^{-2\pi n v e^u}\|_2^2={1\over4\pi nv},\qquad
 \|2e^{u/2}e^{2\pi mve^u}\beta_1(4\pi mve^u)\|_2^2
                         ={\pi\over6mv}.           \tag{11}
\]

第二式保完整2倍计数，依据∫₀∞e^{2y}β₁(2y)²dy=π²/12；实际a_n、N_λ(m)和全部cross／height费用不能省。S_exp付全部fixed(x,v)模态积分及微分，原du只给(11)的逐项fixed-height费，不代无限n总范数或成长容量。若r双polezero且L_{n,v₀}(r)≠0，取r_b=τ_br、v_b=v₀e^-b，则L_{n,v_b}(r_b)=e^{b/2}L_{n,v₀}(r)，原du／Dlog不变；这是实际源的高度费用，非ambient下界。

全部v>0的n1 family是r(logt)t^-1/2的Laplace变换，故在全S_exp注入。这确实比c(r)多读了源，不能再说未构造任何实际Green源；但它未给principal下降或primitive容量。

## 5. 先核405和537：非根恢复，主关系仍失败

μ±=0的源在v↓0有L_{n,v}(r)=−2πnv M_r(3/2)+o(v)，M_r(z)=∫r e^{zu}。405的真实P=(D²−1/4)H、H>0给M_P(3/2)=2M_H(3/2)>0，因此对每个固定b，

\[
 L_{1,v}(\tau_bP)=-4\pi v e^{3b/2}M_H(3/2)+o_b(v)<0
                          \quad(v\text{充分小}).     \tag{12}
\]

Z(1)的degree=2log7非零，故(9)在全部Pan平移上均有明确非principal输出。还须核完整协同：S_exp使每个fixed v的全x-Fourier级数绝对收敛；若完整family对所有x都是principal，其degree周期函数应恒零，每个Fourier系数都须为零。constant和负频项不能对所有x取消这个n1系数。因此对每个fixed b、小v存在x使完整family非principal，而不是只以子项否定整体。small-v门依b，不声称所有x、所有v同号或成长统一。

另取537窗内φ≥0偶compact，ψ=uφ、r_*=(D²−1/4)ψ。它双polezero、c(r_*)=0，而M_{r_*}(3/2)=2M_ψ(3/2)>0，故小v时L_{1,v}(r_*)≠0，且原537独立保证Qζ(r_*)≥2^-49162||r_*||du²>0。这一实际奇非根已被找回；注入／保非根不支付主关系这一独立责任。

## 6. 完整Γ、所有素数幂及pole／constant jet

设原a₀(v)=−h_k(logv+C₀)。实际constant不是只有μ+：

\[
 A_{0,r}(v)=-h_k\{(\log v+C_0)\mu_+(r)+M'_r(1/2)\}.
                                                               \tag{13}
\]

即使μ±=0，M'_r(1/2)仍不可删；405的该项为e^{b/2}M_H(1/2)>0。先在Re z>1对(8)减(13)绝对换序，得到完整Mellin

\[
 \mathscr M_r(z)=M_r(1/2-z)\mathscr M_0(z),\quad
 \mathscr M_0=\Lambda_0\Lambda_\chi
    (\log7+\Lambda'_\chi/\Lambda_\chi-\Lambda'_0/\Lambda_0).
                                                               \tag{14}
\]

再继承亚纯身份。全部Γ(s/2)、Γ((s+1)/2)、proper prime powers、两端点与constant腿保留。双pole矩零只使M_r因子在z0、1为零，原mixed对象仍可能有M′确定的simple部分；不能与经典Weil双pole型混名。中心线上新增因子是r̂(t)，完整解析输出也全源可见。

(14)仍是signed KRY线性预算，不是Qζ的Hermitian平方。完整非constant预算另有非零核查：M_P(1/2-z)=z(z−1)M_H(1/2-z)，实z>1时严格正，原ℳ0(z)也由完整native非constant模态严格正，故不是删掉其他模态后才见失败。标准／transported δ不能删，signed逆及全部mixed费用没有由full-local域支付。经典目标始终保Γ(t)=Reψ(1/4+it/2)−logπ／FP-contact、所有Λ(p^k)=logp和双pole。旧R_A在有限固定局部帧中的实际强范数指数小而完整Qζ~logA，只拒绝相应有界容量recipe；这是552／579旧机制，不新计正号，不排有费无界Green比较。

## 7. 固定coarse载体的primitive门；函数域为何多出独立设施

原KRY Cor5.4、§6的coarse M=Spec O_H。对k=Q(√−7)，最近虚行／实格点的norm余项≤11/16<1给norm-Euclidean，故h_k=1、H=k。它只有一个complex place∞。在native实／复线性Arakelov divisor空间、模同系数principal span中，每个prime(π)满足[𝔭]=logN𝔭[∞]，因此

\[
 \widehat{\mathrm{Pic}}_{\mathrm{native}}(M)_{\mathbb R\text{ or }\mathbb C}
             \xrightarrow{\deg}\mathbb R\text{ or }\mathbb C
                    \quad\text{为同构}.             \tag{15}
\]

这里明示自然divisor系数线性化，不将抽象abelian群的无条件tensor与之混同。fixed coarse native类的degreezero部分为零；不能把已在这个类群中定义的degreezero输出叫隐藏primitive方向。它不否定(n,v)family丰富的读出，也不排stack高阶／relative／framed／higherCM、不同曲面或新regulator；更不说所有λ核都无几何解释。

实际Z(n)仍有native局部长度，但乘complex核没有产生物理源的整section、schematic消失阶或同对象截面乘法。S0支持理想／函数代数不能代这些设施。

连续d=±1/16模型使用同一537奇源、同一strong域／Weil作用／Green输入，native完整Weil型却异号；没有continuous→CM运输，不能称其反驳KRY。真函数域两place的norm步长相称，不能领取2／11 densegrid注入；正号仍来自同一C×C上的degreezero primitive对应、实际有效截面／乘法及RR/Hodge混合容量。全部returns／aliases和H⁰/H² pole扣除保留；compact源用统一j₀的非负Frobenius图，全S_exp另以已付Toeplitz型完成。这里full-local设施尚未运输该同对象二次身份。

## 8. 新输入、停止范围与下一准入

新可消费件是实际A1→S0/fullSL2矩阵高度费用、完整过滤与λ核、读取额外源的native循环／Green family及其精确原费／405失败／537恢复、constant jet与fixed coarse primitive门。Feichtinger一般理论、553旧商、552高频和567 RR来源都是输入；不宣称世界新颖性，也没有新的经典正性或whole预算净后果。

停止把full-Weil强域本身或本arch-only/native-divisor family当成功primitive regulator，不续群word／orbit／level／下一paper。下一只有**同一有非零primitive部分的实际算术载体**上的relative principal／Green cocycle与物理源映射，先405全关系／537及全源非根／原du-Dlog和全部尾费，再局部消失过滤、截面lift／乘法及mixed二次RR。未知height、按Q定义交数或按Pan像定义boundary仍是等价组织；其独立证明可以有意义，不能以改名支付前件。

局部full-action与实际Green源设施前沿改变，独立primitive容量主瓶颈未变。strong-old542+555→557 whole leading4/5仍为负惯性UPPER；actualq、成长core／coupling／Ξ未改，长期Goal open。
