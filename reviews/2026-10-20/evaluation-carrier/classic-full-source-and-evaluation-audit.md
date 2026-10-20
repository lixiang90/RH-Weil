# 完整Weil源的平移评价载体：独立构造、非退化性与原范数的费用

2026-10-20；用户明确续作评价行列式路线。本稿是本轮独立原件，不修改STATE或主稿。
固定G20261014／0c4f≤538；563、565—567及560/405/552是输入。
本稿的实际检验不是再假设正H：直接由完整W构造一个非退化的有符号评价载体，
随后在连续正反例和实际经典Γ/pp/pole上核其性质与费用。它没有给出独立Weil正性。

## 1. 可直接构造的对象：卷积消去商，而不是未知Hilbert空间

先固定完成化、权、全部极点和原点规范，得到实偶Hermitian分布W；本稿的具体测试均在此类。
仅有裸P和宽Mellin对偶不能唯一恢复W，564/565的B(s)反测仍有效。
对A=Cc∞(R;C)，卷积和普通反射共轭r*(u)=overline{r(−u)}，定义

\[
 B_W(r,s)=W(r*s^*),\qquad (J_Wr)(t)=(W*r)(t).                 \tag{1}
\]

W实偶时，分布换元给

\[
 B_W(r,s)=\int_{\mathbb R}(J_Wr)(t)\overline{s(t)}dt.        \tag{2}
\]

每个J_Wr都C∞。J_W连续A→C∞(R)，取通常compact-open导数半范数。
若W有本仓规定的有限指数阶增长，A也可取复S_exp；经典物理空间e^(u/2)S_exp
作为集合仍是S_exp，乘此指数是明确的拓扑/卷积同构。以下在两种A分别成立。
一般Hermitian非偶情形可用J_Wr(t)=W_u(r(t+u))，不把此式与W*r无条件混同。

令R_W=ker J_W。式(2)及Cc∞分离分布说明

\[
 R_W=\{r:B_W(r,s)=0\ \forall s\in A\},\qquad
 V_W=A/R_W\simeq J_W(A).                                  \tag{3}
\]

R_W是闭卷积*理想：B_W(r*a,s)=B_W(r,s*a*)；它也保持平移及微分。
所以(3)给一个由源直接确定、Hermitian配对非退化的局部凸商。
“非退化”只指没有再与所有向量配对为零的非零类，绝不指正定。
平移τ_a在V_W上保持B_W；微分生成元在此配对下形式反对称，不是已证明的Hilbert自伴性。

点/jet评价

\[
 e_{t,k}([r])=(\partial_t^kJ_Wr)(t)
\]

良定义且连续于上述商拓扑。全部点评价已经分离V_W；若V⊂V_W是m维子空间，
任意基v_1,…,v_m可选t_1,…,t_m使det(e_{t_i,0}(v_j))≠0。
证明是：若点评价张成V*的真子空间，其共同零空间含非零v，便使代表函数J_Wv恒0，矛盾。
因此本轮确实得到一个不读取零点的非零评价minor设施。
但没有断言每个有限子空间上的B_W Gram非退化，更没有取得整数minor。

原核若只有分布意义，不能先写K(t,s)=W(t−s)的点值。
(1)的源平滑是必要步骤；再生核Hilbert定理需已证正性，不能倒过来提供正性。
即使改走Krein完成也须付majorant/拓扑，不能由代数非退化自动声称规范Hilbert完成。
已有一手参考是[Alpay 1991作者记录](https://digitalcommons.chapman.edu/scs_articles/484/)
和[Constantinescu–Gheondea，Schwartz有界性条件](https://arxiv.org/abs/math/0212218)；
这里仅采用其“正负核分解/有界性仍是额外责任”的边界，不拿其完成定理支付RH。

## 2. 连续正反例：同一个非零det设施，不同的惯性

采用562/563已付真实positive P/Π/M族Z_c=1+c/[s(s−1)]，0<c≤1/2。
其完整W由源ODE给出，不先读根。

正段c>1/4，τ²=c−1/4，令
A(r)=∫cos(τu)r(u)du，C(r)=∫sin(τu)r(u)du，则

\[
 J_Wr(t)=2A(r)\cos(\tau t)+2C(r)\sin(\tau t),\qquad
 B_W(r,r)=2(|A(r)|^2+|C(r)|^2).                            \tag{4}
\]

负段0<c<1/4，ρ²=1/4−c，令A(r)=∫cosh(ρu)r(u)du、S(r)=∫sinh(ρu)r(u)du，则

\[
 J_Wr(t)=2A(r)\cosh(\rho t)-2S(r)\sinh(\rho t),\qquad
 B_W(r,r)=2(|A(r)|^2-|S(r)|^2).                            \tag{5}
\]

cos/sin及cosh/sinh各线性独立，故两个矩映射A→C²都满射；两个V_W均二维、评价非退化。
在坐标(A,C)或(A,S)下，取点0,h的评价矩阵，行列式分别4sin(τh)、−4sinh(ρh)，
选h避开正段的离散退化位置便都非零。
还可取实偶非负小支撑φ，令a=∫cos(τu)φ>0或a=∫cosh(ρu)φ>0，
用r_0=φ、r_1=φ(·−h)得到实际source Gram

\[
 2a^2\begin{pmatrix}1&\cos(\tau h)\\\cos(\tau h)&1\end{pmatrix},\quad
 2a^2\begin{pmatrix}1&\cosh(\rho h)\\\cosh(\rho h)&1\end{pmatrix}. \tag{6}
\]

其det分别4a⁴sin²(τh)>0、−4a⁴sinh²(ρh)<0。
非零evaluation det、全平移/反演对偶和完整source身份在两段都存在；这些设施不含正号。
阈值c=1/4时W=2，V_W只有一维，而目标分子有二重零点；这是565/566的旧重数边界。
本载体可以承担Weil型，但不能把cyclic rank自动称为带重数谱行列式的维数。

也不能把Toeplitz差核换成Hankel和核来取得一个“更几何”的正性：
即使真正段W=2cos(τu)，半轴上的Hankel型是

\[
 H(f,f)=\iint W(u+v)f(u)\overline{f(v)}dudv
       =2(|\!\int\cos(\tau u)f|^2-|\!\int\sin(\tau u)f|^2). \tag{7}
\]

在任意正半轴开区间，cos与sin的两个Cc∞矩线性独立；存在实f使cos矩0而sin矩非0，
于是H<0。此处τ>0；阈值另论。因此这类朴素Hankel/半轴反射正性不是一般类RH必要条件。
特殊Euclidean反射、换时间变量或不同核仍是另一种构造，未被(7)排除。

## 3. 非零minor没有自动生成LS所需的乘法与局部整除

V_W确有从A卷积诱导的代数乘法，但它不是函数J_Wr的逐点乘法。
例如(4)/(5)的函数空间span{e^(at),e^(−at)}，a=iτ或ρ，逐点乘法会产生1、e^(±2at)，
已超出原二维空间。J_W(r*s)一般也不等于(J_Wr)(J_Ws)。
通常时间导数满足D(r*s)=(Dr)*s=r*(Ds)，而不是局部截面乘法的Leibniz和式。
所以不能凭这个卷积代数对其point jets直接调用LS的(z^p−w)^h乘积整除论证。
可以另造对称代数或更大函数环，但须另给过滤、实际评价乘法及定量容量，不能免费继承B_W。

特别地，J_W评价值一般是复/超越数，不是Z格的坐标。
“把矩阵近似成有理数、清分母”即使保非零，也要付分母高度，并未构造Frobenius同余；
prime atom的平移长度log p也不提供模p剩余域、(α^p−α')的局部幂次或product formula。
连续正段证明literal有限位整除不是所有正例必要设施；负段说明只保评价与非退化又太弱。

## 4. 经典ζ：不读取零点的完整J_W公式

固定[563](../../../notes/563-distribution-side-weil-certificates-and-heat-complete-monotonicity.md)
和[566](../../../notes/566-source-closed-forms-and-full-weil-heat-trace-tests.md)的实际规范。
令Γ₀=ψ(1/4)−logπ，w(v)=2e^(−v/2)/(1−e^(−2v))，a_n=Λ(n)/√n。
对任意h∈Cc∞，完整线性源为

\[
\begin{aligned}
 W_\zeta(h)={}&\int 2\cosh(u/2)h(u)du+\Gamma_0h(0)\\
 &+\int_0^\infty w(v)\left[h(0)-\frac{h(v)+h(-v)}2\right]dv
 -\sum_{n\ge2}a_n[h(\log n)+h(-\log n)].                 \tag{8}
\end{aligned}
\]

对角差分在v=0为O(v²)，w(v)~1/v；大端w指数可积，所以这里没有任意finite-part常数。
它的Gamma乘子正是actual Γ∞(ξ)=Reψ(1/4+iξ/2)−logπ=2θ′(ξ)。
将(8)作用于r(t−·)直接得到

\[
\begin{aligned}
 (J_Wr)(t)={}&e^{t/2}M_-(r)+e^{-t/2}M_+(r)+\Gamma_0r(t)\\
 &+\int_0^\infty w(v)\left[r(t)-\frac{r(t-v)+r(t+v)}2\right]dv\\
 &-\sum_{n\ge2}a_n[r(t-\log n)+r(t+\log n)],\qquad
 M_\pm(r)=\int e^{\pm u/2}r(u)du.                         \tag{9}
\end{aligned}
\]

compact r下每个fixed t及其邻域的prime和只有有限多项；S_exp下由强下降支付绝对收敛和所有导数。
因此(9)是一个真正的由算术源定义的平滑评价映射，同时保留：

* 全部proper powers：n=p^k的权是log p/p^(k/2)，不是log(p^k)或只保k=1；
* 完整Γ差分及Γ₀ contact，不能只留穿孔的负核；
* 两个pole矩M±，其Hermitian型含一个负方向，不能改成两个独立正平方。

由(2)恢复的正是

\[
\begin{aligned}
 Q_W(r)={}&2\Re(M_+(r)\overline{M_-(r)})+\Gamma_0\|r\|_2^2\\
 &+\tfrac12\int_0^\infty w(v)\|\tau_vr-r\|_2^2dv
 -2\sum_{n\ge2}a_n\Re(r*r^*)(\log n).                    \tag{10}
\end{aligned}
\]

这是一条完整source identity，不是独立A−L≥0预算。Gamma正jump中的Γ₀可负；
prime反相关、双pole和各项coupling仍在。把(10)的右边称作“容量差”没有支付它的符号。
经典W在log2有非零负原子，而其余背景在那里光滑，故本轮V_W为无限维：
若其维数有限，任意近似单位r_ε给W*r_ε∈同一有限维平滑空间并在D′收敛到W；
有限维子空间在D′闭，便使W平滑，矛盾。这个结论不涉及零点位置。

## 5. 关系/非根双测试：完整Q与405的B必须分开消费

本节h=Eη及p=Eη₀不是compact函数，以下关系与零类测试明确在physical
A_exp=e^(u/2)S_exp=S_exp和V_W^exp=A_exp/kerJ_W中进行。
本稿§1的compact商仍单独保留；kerJ_exp∩Cc∞=kerJ_compact，故compact商向扩张商有自然线性单射；不另声称拓扑嵌入。
不将非compact源当作compact测试，所用全部源配对由(8)/(9)在S_exp的同一增长延拓支付。

在405旧变量f中，physical r=e^(u/2)f。405的完整算术B满足

\[
 2B(f,g)=d(f)\overline{c(g)}+c(f)\overline{d(g)}-T(f,g),
 \quad Q_W(r)=T(f,f)                                    \tag{11}
\]

（复数式按明确Hermitian极化理解）。已有I是完整ζ-zero关系像，P_an=I∩ker c∩ker d。
405只断言I内部rad B=P_an；I/P_an的两次数方向在B上是双曲平面，不能静默消去。
另一方面，完整Weil型Q_W=T的根包含整个physical e^(u/2)I；因此(3)的Q载体杀整个I，
是目标角色决定的合法操作，不是撤回405或把B的根空间改大。它不声称同时承载B/degree平面。

具体p=Eη₀∈P_an非零，在physical r_p=e^(u/2)p下，B_W(r_p,s)=0对全部s，故J_Wr_p=0。
更强的h=Eη∈I虽d(h)=c(h)=1/4、B(h,h)=1/16，physical Q却为0，也被J_W消去。
这正好验证两种角色不能互换。
另一方面552的r₀=(D²−1/4)ψ、ψ实偶非零且支撑在(−17/16,17/16)，
537给Q_W(r₀)>0，所以J_Wr₀不可能恒0，physical非根方向可见。
因此本候选实质通过relation/nonroot测试；但测试通过不等于RR/正性完成。

还应保留零点重数边界：卷积W的rad只需相应value消失，不自动要求ζ的每一高阶jet消失。
旧I有更强的整除/zero-jet关系，不能由本载体反推I等于全部rad。
给每个指数项乘重数会改变B_W权，却未必增加cyclic维数；(3)不是faithful谱行列式模型。

若其他全部项已固定，唯独将(8)contact改为Γ₀+c，则J变成J+cId。
由非零r_p及Jr_p=0可知，仍要求此已知源关系被消去就迫c=0。
这提供一个真实的contact校准检验；不能由此声称排除同时改动其他核/完成化的所有B(s)自由度，
也不提供正性。

还可以直接测试各项能否分别下降到V_W。取上述h=Eη，令r_h=e^(u/2)h。
由h∈I有[r_h]=0且J_Wr_h=0，但

\[
 P(r_h)=2d(h)c(h)=\tfrac18,\qquad
 (\text{arch}-\text{prime})(r_h)=-\tfrac18.              \tag{11a}
\]

对任意实t，tr_h仍代表同一零类，两项分别是t²/8、−t²/8。
所以完整pole与arch-minus-prime不能在这个Q非退化商上分别定义成代表无关的budget；
单独某片的norm/capacity也不可能在零类上有统一有限界。这是同一实际源的精确测试。
它只排“各片无补偿分别下降”的方案，完全不排principal determinant line、
matched local cocycle或degree-plane扩张：405已给A/P_an保留I/P_an双次数方向的解析修复，
在那里两个矩及相应pole确能下降；它仍不自动给局部sections、有效性或全位容量估计。
几何主关系通常正是允许各局部范数按协同变换律改变，而非要求每片单独为零。

## 6. 原fixed-window Dlog范数下，point/jet评价确实不有界

这是本轮对实际经典candidate的新费用检验，避免把S_exp连续性误读为原physical norm小费。
固定I=(−L,L)，取φ∈Cc∞(I)，φ(0)≠0，r_R(u)=φ(u)e^(iRu)，R→+∞。
傅里叶约定\hat r(ξ)=∫r(u)e^(−iξu)du；原自然form域是

\[
 D_{\log,I}=\{r\in L^2(I):\int\log(2+|\xi|)|\hat r(\xi)|^2d\xi<\infty\},
 \quad \|r\|_D^2=\frac1{2\pi}\int\log(2+|\xi|)|\hat r(\xi)|^2d\xi. \tag{12}
\]

这是537的同一域和等价图范数，所有函数仍按zero extension使用。
直接换元和φ的Fourier快速下降给

\[
 \|r_R\|_2=\|\phi\|_2,\qquad
 \|r_R\|_D^2=\log R\,\|\phi\|_2^2+O_\phi(1).          \tag{13}
\]

Γ∞(ξ)=log|ξ|−log(2π)+O(ξ^(−2))。把Fourier积分分成|ξ−R|≤R/2和其余，
近部用符号一阶差分，远部用\hatφ的任意阶下降，严格得到

\[
 (G_\infty*r_R)(0)=\phi(0)\log R+O_\phi(1).             \tag{14}
\]

事实上可保留−log(2π)φ(0)及O(1/R)，此处粗余量足够。
在t=0，(9)的全部prime项是有限n≤e^L的固定权求和，各点r_R(±logn)有界，故整体O_(I,φ)(1)。
两个pole矩是φ(u)e^(±u/2)的Fourier值，反复分部积分为O_(φ,M)(R^(−M))，所有M均可。
这些是完整pp/pole的准确费用，没有删除它们。因此

\[
 (J_Wr_R)(0)=\phi(0)\log R+O_{I,\phi}(1),\qquad
 \frac{|(J_Wr_R)(0)|}{\|r_R\|_D}\longrightarrow\infty.   \tag{15}
\]

对任意固定k≥0，同一符号估计，及有限prime项的求导展开，给

\[
 (\partial^kJ_Wr_R)(0)=(iR)^k\phi(0)\log R+O_{I,\phi,k}(R^k). \tag{16}
\]

故所有point/jet评价在原L²(I)和原Dlog图范数上均不有界。这个结论仅针对(9)的point/jet映射；
不声称全部评价载体或所有不同norm方案失败，也不把它误作Q负方向。
原Q_W(r_R)=logR||φ||²+O(1)仍是正的高频方向；问题是point读出比其form norm昂贵。

有两种合法修复，均须保存其实际费用：

1. **固定光滑probe。** 以e_ψ(r)=B_W(r,ψ)或平移ψ代替δ_t。
   对每个fixed I,J和ψ∈Cc∞(J)，有|B_W(r,ψ)|≤C_(I,J)||r||_D||ψ||_D。
   Γ项用|Γ∞|≤C log(2+|ξ|)及Cauchy–Schwarz；在I−J内prime位移仅有限多，
   各相关项用L²；pole用固定支撑下的指数矩界。这给原Dlog上真有界的平滑评价。
   r支持fixed I而允许probe在任意fixed J内时，全部compact probes仍分离全线J_W像；
   单一有限J或有限probe不自动给全域coverage。选有限多probe可以读出有限维子空间，
   但probe本身的范数和其向δ收缩的费用必须付。ψε=ε^(−1)ψ(·/ε)通常有
   ||ψε||_D²~ε^(−1)log(1/ε)||ψ||²，绝非uniform免费极限。
2. **增强源范数。** 在fixed I上H^s、s>k+1/2使k阶point jet有界，
   因∫(1+ξ²)^(−s)|ξ|^(2k)log²(2+|ξ|)dξ有限；有限shift/pole项同样可控。
   这是额外Sobolev费用，不能静默运输成原Dlog费用，更不独立给完整Q的符号。

## 7. 与560实际正迹比较：换载体尚未消掉同一个有符号责任

[560](../../../notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md)
已给每fixed L、同一原Dlog全部复源

\[
 Q_L(r)=t_{F_L}(r)-\langle r,K_{F_L,I}r\rangle
       +2|\langle r,\cosh(u/2)\rangle|^2
       -2|\langle r,\sinh(u/2)\rangle|^2,               \tag{17}
\]

t_F是实际ordinary正迹，K为原L²(I)自伴紧算子。其source身份和全部proper powers已付，
但K的符号/成长费和补空间coupling未付。
本轮J_W把(17)整个有符号源搬到一个非退化评价商，并未从独立局部有效性证明K≤可吸收项。
若按|detE|²构造正体积或按J*J造正型，(5)/(6)已经显示会换掉目标B_W。
若直接规定A_n−L_n=c_nQ_W+o(c_n)，再假设A_n是合法上界，仍把所需正性放入条件。

真正的独立输入须先给：与关系兼容、非根可见的实际局部截面乘法；
同一nonzero对象的非负局部消失量；不由Q定义的全局高度/维数上界；
最后证明预算差的全source比较，保Γ/contact/pp/poles和任意复mixed项及极限。
本轮没有这些输入，故不能以canonical、nondegenerate、det≠0三词替代Weil有效性或RR。

## 8. 根消费范围与新增量

* 对象/map：完整预定W、A的卷积*代数、J_W:A→C∞、R_W闭根理想、signed商V_W；
  不把pointwise函数乘法、literal整数格或Hilbert完成偷加进去。
* 源/量词：每个完整compact复源；有增长前件才延到S_exp；(13)—(16)为先fixed L、R→∞，
  不付L成长或不同norm低费运输。
* 实际测试：continuous正/负/阈值、Hankel拒真正例、classic完整J的relation/nonroot双测试、
  Γ导致point/jet原Dlog不可有界及固定smooth probe合法修复、零关系上各budget片不能分别下降。
* 已付/误差：Γ主项logR，fixed-window pp的O(1)、pole任意阶下降，k阶prime O(R^k)；
  没有删去contact或proper powers。quotient kills physical I是Q/T角色，405的B/P_an结论不改。
  (11a)只排分别无补偿下降，保matched local cocycle、det line与405已付双次数扩张。
* 未付：真实局部sections/有效性与product formula、budget身份、全mixed比较、合法无限域极限；
  本carrier的cyclic维数不保spectral multiplicity，原physical闭形式的566障碍不被重开。
* 净后果：给出实际可检验且有非零minor的source评价候选，并定位其local multiplication与norm费用；
  不是新classic Weil正性，不改最强旧542＋555→557 whole leading4/5，也未消560成长K/core/coupling。

本稿不主张世界优先权。代数消去商/核线性化是既有一般方法；新增的是本项目完整source、
旧关系角色、连续签名/Hankel负测与实际Γ原norm费用的同对象核验。
