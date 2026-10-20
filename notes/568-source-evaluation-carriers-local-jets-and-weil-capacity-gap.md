# 568. 源定义评价载体、真实局部jets与完整Weil容量差

2026-10-20，C031，固定G20261014／0c4f≤538。用户明确优先评价行列式路线。
统一一完整数学检验；三个独占原稿、来源、终审和同步不另计轮。原Γ章节门本轮未执行。

**本轮回答：可以不读零点构造非退化的有符号评价载体；某些离散源甚至可构造真实局部étale/jet代数。
但这些设施并不独立给正的局部—全局容量差。连续正反例和正整数Euler反模型都能通过它们。
经典ζ已有同源评价公式，仍缺可乘的全局截面及其容量/局部消失比较。**

这一区分比“没有任何载体”更准确。下列构造不是新的独立经典正性定理，
也不是把此前未知H/预算身份改名后宣称存在；每个实际map和失败位置均明确。

## 1. 对象范围：完成与对偶先固定，不能偷偷选核

输入仍为log坐标上的P、全部powers Π、M=exp_*Π及其合法Mellin增长域。
固定completion、预定权、pole/contact和dual后，取本轮实偶Hermitian完整源W，

\[
 B_W(r,s)=W(r*s^*),\quad Q_W(r)=B_W(r,r),\quad
 s^*(u)=\overline{s(-u)},\quad r,s\in\mathcal D=C_c^\infty(\mathbb R;\mathbb C).
                                                               \tag{1}
\]

有有限指数阶增长时才延到复S_exp。一般非自对偶双对象先给左右配对，不会自动成为
(1)中的Hermitian型或共有中心；564–565的权、B(s)和分次识别责任原样保留。
本轮不从裸P证明任意W的自然完成化存在/唯一。

旧563的有限ODE/正能量、567的完整曲线Gram及RR、405的源关系、560的actual正迹均为输入。
下面新增的是实际carrier/局部jet的构造及同对象反测，不重计这些旧纯性/全源结果。

## 2. 一个确实存在、由源定义的评价商

对实偶W定义

\[
 J_W:\mathcal D\to C^\infty(\mathbb R),\quad J_Wr=W*r,
 \qquad B_W(r,s)=\int(J_Wr)(t)\overline{s(t)}dt.           \tag{2}
\]

分布与compact smooth卷积及其导数合法，故J连续于测试函数拓扑和C∞的局部半范数。
令R_W=kerJ_W，则

\[
 R_W=\{r:B_W(r,s)=0\ \forall s\},\quad
 V_W=\mathcal D/R_W\simeq J_W(\mathcal D).                \tag{3}
\]

R_W是闭卷积*理想，保持平移及微分。证明例如
B_W(a*r,s)=B_W(r,s*a*)，共轭给*稳定；(2)和测试分离给两种根定义相同。
V_W配对非退化，不假设其正。右侧的同构先指向量空间；商拓扑并不免费等于
C∞中像的子空间拓扑。一般Hermitian非偶W要相应调整反射，不能无条件沿用偶核公式。

所有e_(t,k)([r])=∂^k(J_Wr)(t)良定义，且全部点评价已分离V_W。
对任意m维子空间U⊂V_W及其基v_j，存在t_1,…,t_m使

\[
 \det(e_{t_i,0}(v_j))\ne0.                              \tag{4}
\]

否则全部点评价在U*中不张满，其共同核含非零类，但该类的J函数恒0，矛盾。
这给一个实际非零评价minor，不预用零点位置；既不保证每个U的Weil Gram非退化，
也不使minor成为整数，更不提供规范Hilbert/Krein完成。

关键限制：V_W的乘法来自源卷积，不是像函数的逐点乘法。
二维span{exp(at),exp(−at)}逐点相乘便产生新的频率；微分也不是该卷积乘法的Leibniz和式。
因此不能对这个载体直接套LS的多项式乘积及Frobenius整除证明。
式Q_W(r)=B_W([r],[r])是定义型同源身份；断言右侧正仍是原Weil正性。

## 3. 连续正反例：非零评价和容量已有，符号仍在另一笔配对里

562–563已从真正positive P/fullΠ/M给出Z_c=1+c/[s(s−1)]，0<c≤1/2，
完整源满足全域ODE W''+dW=0、W(0)=2、W'(0)=0，d=c−1/4；这里Γ=0，双pole仍含0、1。
不求根，直接以级数定义C_d、S_d，满足C_d'=-dS_d、S_d'=C_d、初值(1,0),(0,1)。

从系数构造

\[
 A_d=\mathbb C[D]/(D^2+d),\quad D^*=-D,
 \quad\tau_d(a+bD)=2a=\operatorname{Tr}_{\rm reg}(a+bD).
                                                               \tag{5}
\]

e^(uD)=C_d(u)+S_d(u)D和ODE唯一性给τ(e^(uD))=W(u)。设
A_r=∫rC_d，B_r=∫rS_d，直接展开得全部compact复源的精确身份

\[
 Q_d(r)=\tau_d(v_r^*v_r)=2|A_r|^2+2d|B_r|^2,
 \qquad v_r=A_r+B_rD.                                   \tag{6}
\]

两个矩映射满射C²，因为C_d、S_d作为分布线性独立。这个正性阈值和有限能量身份归旧563。

本轮改查实际解空间S_d=span{C_d,S_d}的评价：F→(F(0),F'(0))是双射，
Wronskian恒1，每个非零解在一点的vanishing order至多1，维数容量为2。
全族还有真实统一上界|F(z)|≤exp(R/2)(|a|+R|b|)，|z|≤R。
固定同一两点0、1，得到

\[
 E_1=\begin{pmatrix}1&0\\C_d(1)&S_d(1)\end{pmatrix},
 \quad \det E_1=S_d(1)\ge23/24>0
 \quad(-1/4<d\le1/4).                                   \tag{7}
\]

d≤0时级数非负，d>0时交错级数给S_d(1)≥1−d/6。可是对应的Weil点Gram是

\[
 G_{0,1}=E_1\operatorname{diag}(2,2d)E_1^T,
 \qquad \det G_{0,1}=4dS_d(1)^2.                         \tag{8}
\]

固定d=±1/16，两侧都具有真实jet、同一个非零评价门、有限维容量和统一高度上界，
而(8)符号相反。取实偶小bump及其平移，还能把点Gram改成真正compact源的同号反测试，
不靠δ向量冒充测试函数。取正metric diag(2,2|d|)可造正插值容量，但负段不再等于(6)。

更窄的反测：d=±a²，z→iz给两个holomorphic解空间同构，保centered disk supnorm、
原点jet filtration及旋转后的|evaldet|。它不保physical实线/real *结构，
所以只否“忘掉实对偶的纯holomorphic容量自动付正号”，不排真正fixed-real joint条件。

阈值d=0时jet代数仍二维，而trace配对rad=CD，最小V_W为一维，Q=2|∫r|²。
原trace重数2以权保留，不能从商维数读普通det重数。faithful正Hilbert *作用会要求
D为skew-adjoint且D²=0，于是||Dv||²=0，反而错误排除这个真实正例。

还有一个必须拒绝的过强条件：即使W=2cos(τu)、τ>0为正型，半轴Hankel核W(u+v)给
2(|∫cos(τu)r|²−|∫sin(τu)r|²)，在任何正半轴开区间都可取compact r使其负。
Weil的差核不能无桥换成和核；其他反射、变量或核方案不在这个反测范围内。

## 4. 函数域：从closed points可造真实局部代数，却造不出全局容量

给q和全部b_d∈Z_≥0，不假设曲线存在，逐B构造

\[
 R_B=\prod_{d\le B}(\mathbb F_{q^d})^{b_d},\quad
 M_B=\sum_{d\le B}db_d.                                 \tag{9}
\]

有限可分性给perfect F_q trace pairing；可加局部jets k(v)[t_v]/t_v^(r_v)，
以λ_v(a)=Tr_[k(v)/Fq]([t_v^(r_v−1)]a)定义perfect residue pairing。
这是真实有限代数、真实评价和非退化配对；ordinary algebra trace在nilpotent方向可退化，不能混用。
参数/全局微分/gluing未由b_d指定，t→t^q通常也不是jet代数自同构。
这里不用正特征下可能退化的ordinary Wronskian。

另将几何点集X_B复线性化为H_B=C^(X_B)，计数内积为正，Frobenius置换V_B酉，

\[
 \operatorname{Tr}V_B^n=\sum_{d\mid n,d\le B}db_d=N_n
 \quad(1\le n\le B).                                   \tag{10}
\]

F_q配对与复点集内积是两个对象，没有F_q→C域嵌入，不是同一form的自动标量提升。
固定q=5，B=4，真曲线E:y²=x³+x+1与290的正整数Euler反模型给

| 对象 | N₁,…,N₄ | b₁,…,b₄ | 完整primitive二阶Gram的det |
|---|---|---|---:|
| 真实曲线 | 9,27,108,675 | 9,9,33,162 | 11/5 |
| 290反模型 | 1,11,76,451 | 1,5,25,110 | −1 |

所有B的(9)、jet配对及(10)两边都成立。最后一列和all-period Gram是567旧结果；
新增的是实际局部carrier也同时通过两边，仍不能支付primitive正号。
原因可明确写成

\[
 a_n=q^{n/2}+q^{-n/2}-q^{-n/2}\operatorname{Tr}V_B^n,
 \quad n\le B,\qquad a_0=2g.                            \tag{11}
\]

这是两个背景减一个raw正载体迹，正性不经过signed差传递。
V_B是raw closed-point置换，不是weight-one H¹；M_B→∞也不能冒充固定2g的contact。
逐n的finite-B稳定值不等于无限维unitary V^n存在ordinary trace。

真实曲线另给同一个函数域对所有局部环的diagonal source，以及

\[
 H^0(C,O(D))\xrightarrow{\rm ev_E}H^0(E,O(D)|_E),\quad
 \ker\mathrm{ev}_E=H^0(C,O(D-E)).                        \tag{12}
\]

degE>degD给injectivity，RR给h⁰(D)≥degD+1−g，限制/乘法/次数来自同一全局对象。
局部自由jet只给(12)右边，不能任选小子空间冒充左边。
要得到完整Weil型还须平方上的signed对应有效化、交重数和容量比较；567已恢复这条几何链，
本轮不以重新引用RR算新增正性。参见[CCM §2.3](https://arxiv.org/pdf/math/0703392v1)
及[Grothendieck §§1–2](https://denisevellachemla.eu/AG-Mattuck-Tate.pdf)。

若从全部N_n另取得精确有理分子P，A=Q[X]/(X^mP(X⁻¹))的regular trace可复原完整幂迹，
FE给X†=q/X；其trace Hermitian型在两例的det分别11、−5。身份是系数代数，
正号仍等价于该有限类的纯性；重根nilradical商还须保存trace权。这不是又一个独立输入。

## 5. 经典ζ：完整源给出真正评价公式，所有项保留

令Γ₀=ψ(1/4)−logπ、w(v)=2e^(−v/2)/(1−e^(−2v))、a_n=Λ(n)/√n。
由563/566既定完整规范，直接对任意compact复r有

\[
\begin{aligned}
 J_Wr(t)={}&e^{t/2}M_-(r)+e^{-t/2}M_+(r)+\Gamma_0r(t)\\
 &+\int_0^\infty w(v)\left[r(t)-\frac{r(t-v)+r(t+v)}2\right]dv\\
 &-\sum_{n\ge2}a_n[r(t-\log n)+r(t+\log n)],
 \qquad M_\pm(r)=\int e^{\pm u/2}r(u)du.                 \tag{13}
\end{aligned}
\]

近零二阶差分为O(v²)、w~1/v，大端指数可积。compact源在每个t邻域的prime和有限；
S_exp延拓另付绝对收敛。n=p^k权为logp/p^(k/2)，全部proper powers未改，Γ₀是固定contact。
同源配对恢复

\[
\begin{aligned}
 Q_W(r)={}&2\Re(M_+\overline{M_-})+\Gamma_0\|r\|_2^2
 +\tfrac12\int_0^\infty w(v)\|\tau_vr-r\|_2^2dv\\
 &-2\sum_{n\ge2}a_n\Re(r*r^*)(\log n).                 \tag{14}
\end{aligned}
\]

Γ₀可负、correlation可带符号、pole含odd负方向。把右边命名为A−L没有证明A≥L。
经典V_W无RH可证无限维：若rangeJ有限维，所有W*ρ_ε在同一个有限维smooth空间，
在D′趋W；有限维子空间闭，便使W光滑，违反log2处不可被平滑背景抵消的prime原子。
这与563的finite-ODE障碍同源，维数推论不重计新classic限制。

### 5.1 商、关系与budget各片的下降不能混为一谈

本小节的405 Gaussian源h、p不是compact函数，故明确使用physical
\(\mathcal A_{\exp}=e^{u/2}S_{\exp}=S_{\exp}\)及其扩张商
\(V_W^{\exp}=\mathcal A_{\exp}/\ker J_W\)，不是把它们放进§2的compact商。
(13)各项在此域绝对收敛，保证同一W的延拓；compact商向扩张商有自然线性单射，
因为\(\ker J_W|_{\mathcal A_{\exp}}\cap\mathcal D=\ker J_W|_{\mathcal D}\)。
以下“零类”和分片下降测试均指这个扩张商；compact复源的正性目标不因此变更。

旧f与physical r=e^(u/2)f的运输固定。405/552给
Q_W(r)=T(f,f)=2Re(d(f)overline{c(f)})−2B(f,f)。
Q_W的根包含整个physical I，所以J_W合法地消去e^(u/2)I；
旧B仅在I内有rad=P_an，I/P_an的degree双曲平面仍非零，不能改成同一个商。
非零p=Eη₀∈P_an被本J消去；r₀=(D²−1/4)ψ的Q_W>0由537已付，所以J_Wr₀≠0。
因此这个signed源map确能通过关系/非根测试，却不是独立构造了几何主除子/全局sections。
I还含更强zero-jet关系，本载体不证明I等于全部R_W，也不保faithful普通谱重数。

旧405的h=Eη满足d(h)=c(h)=1/4，physical r_h的J_W为0，但

\[
 P(r_h)=1/8,\qquad(\mathrm{arch}-\mathrm{prime})(r_h)=-1/8. \tag{15}
\]

任意实数t的t r_h是同一零类，各片却分别为±t²/8。
所以在这个非退化Q商上，无补偿地让pole和arch−prime分别成为代表无关budget会失败。
这只排**分别下降**；保留matched local cocycles、principal determinant line和405双次数扩张。
几何各局部范数允许协同变换，不要求各片单独为零。本式是旧405恒等式的角色消费，非新正性。

若其余源全部固定、唯contact改为Γ₀+c，J变J+cId；非零r_p既有关系迫c=0。
这只校准单独contact自由度，不排同时改核/完成化的所有B(s)。

### 5.2 point/jet在原Dlog上并非免费，合法平滑修复仍保留

固定I=(-L,L)、φ∈Cc∞(I)、φ(0)≠0，r_R=φe^(iRu)，R→∞。原zero-extension图范数取

\[
 \|r\|_D^2=(2\pi)^{-1}\int\log(2+|\xi|)|\widehat r(\xi)|^2d\xi.
\]

Γ∞(ξ)=log|ξ|−log(2π)+O(ξ⁻²)，据[digamma渐近5.11.2](https://dlmf.nist.gov/5.11.E2)，
分|ξ−R|≤R/2和Schwartz尾直接得

\[
 \|r_R\|_D^2=\log R\|\phi\|_2^2+O(1),\qquad
 \partial^kJ_Wr_R(0)=(iR)^k\phi(0)\log R+O(R^k).         \tag{16}
\]

这里fixed-window全部pp贡献O(R^k)，双pole每阶都任意快下降，并未删项。
所以point/jet读出对原Dlog、L²均不有界，k=0的比值已为常数倍sqrt(logR)→∞。
它不意味着Q_W(r_R)<0；该高频方向的Q反而为logR||φ||²+O(1)。

合法修复是固定smooth probe e_ψ(r)=B_W(r,ψ)，对fixed I,J有
|e_ψ(r)|≤C_(I,J)||r||_D||ψ||_D，来自Γ加权Cauchy–Schwarz、有限shift及pole矩。
所有compact probes仍分离全J像；有限probe/有限J不自动给全域coverage。
ψ_ε趋δ的费用通常||ψ_ε||_D²~ε⁻¹log(1/ε)||ψ||²，不允许无费取极限。
增强到H^s、s>k+1/2也可控制jet，但不能把额外norm费用静默转回原Dlog。
这仅拒本J的无费point/jet方案，不排所有评价map/非局部/relative或norm适应修复。

## 6. 容量差身份：哪些是等价组织，哪些才是独立输入

对实偶compact mollifierρ_ε，W_ε=W*(ρ_ε*ρ_ε*)是平滑核，且

\[
 \sum_{i,j}a_i\overline{a_j}W_\epsilon(x_i-x_j)
 =Q_W\!\left(\sum_i a_i\rho_\epsilon(\cdot-x_i)\right).  \tag{17}
\]

所有ε/所有有限点评价Gram为PSD与完整Q_W≥0等价：一向直接；反向以Riemann sums
在共同compact及各阶导数上逼近r*ρ_ε，再ε↓0，用D′连续性。
这是可用的分布侧评价字典，尚未给任何新独立符号来源。

要取得用户要求的LS式预算，仍需从额外结构证明：

1. **局部消失有意义且可乘。** 同一个global source→jets map有真实restriction/kernel/filtration；
   一般卷积像既非pointwise函数环，也无Frobenius reduction，不能从det≠0补出整数消失阶。
2. **容量由独立定理约束。** RR、collision degree、原norm高度或实际signed抵消先给上界，
   不按Q反定义容量。连续负例及函数域反模型应在这一项实际失败。
3. **全位相容。** 分片可用transition law/cocycle/det line配对下降，但须保完整Γ、pp、pole/contact，
   对所有compact complex组合有预算身份及趋0误差。换正metric或正Gram不等于原源。

例如非零D_n(r)的local lower L_n≤log|D_n|≤A_n只给A_n−L_n≥0；
必须另证(A_n−L_n)/c_n→Q_W(r)、c_n>0，且A_n确为不读取目标符号的独立上界。
本轮没有构造这个局部—全局预算。signed carrier身份(2)、代数trace身份(6)或PSD字典(17)
不支付它。走Weil判据时不必再额外索取谱det；若声称faithful谱实现才另付重数/无额外谱。

560的actual对照仍是每fixedL的完整Q=positive ordinary trace−signed compact K＋双pole。
本J只是搬运同一个全源，没有使K自动有利，也未取得成长core/coupling的新费。

## 7. 净后果、止损与后续选择

| 本轮实际得到 | 不得升级为 |
|---|---|
| 源定义signed评价商及有限维nonzero minor | positive Hilbert空间、整数格、局部整除或独立正性 |
| 连续正反/阈值的实际jet与配对，固定0/1评价门 | 非零det/统一容量足以付Weil号，或faithful jet action是类RH必要条件 |
| 真实étale/jet、raw正Frob精确复原截断N_n | global sections/RR，primitive正迹或无限ordinary trace |
| 经典完整J、关系/非根可见和原norm费用 | geometry principal/gluing已构造，或所有评价方法都失败 |
| naive分别下降及Hankel/无费point方案反测 | matched cocycle/det line/平滑或强norm修复均不可能 |

因此本轮有具体carrier和严格范围的反测，不是单纯来源回顾；统一结算568一轮。
但actual经典强旧542＋555→557 whole leading4/5、560成长K/core/coupling与Ξ门未改，
宏观瓶颈仍是同一完整源的独立global capacity/有效性或signed比较。

C031一次固定检验后停止，不继续增加B、jet阶数、continuous参数或unknown capacity公理。
新global source→jet候选必须给(12)式kernel/容量及其与primitive signed差的身份才重新准入。
没有此输入时，下一唯一动作恢复已保存的2402.06671v2双conormal固定权/finite-part对完整Γ来源门；
若仍须手调半轴权/contact，则停翻译并回560 actualreceiver signed准入。该门本轮未执行。
会改变选择的证据是实际global map、独立collision/RR预算或保全源的有利signed新估计，
不是换一个carrier名称或再次宣布所有Gram应正。

原稿与精确有限核查：
[连续](../reviews/2026-10-20/evaluation-carrier/continuous-carrier-and-budget-tests.md)、
[函数域](../reviews/2026-10-20/evaluation-carrier/function-field-evaluation-budget.md)、
[经典完整源](../reviews/2026-10-20/evaluation-carrier/classic-full-source-and-evaluation-audit.md)、
[整数/Fraction记录](../reviews/2026-10-20/evaluation-carrier/exact-algebra-checks.json)。
