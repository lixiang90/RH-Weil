# 固定marked-cusp泛函：实际Pan轨道与1728端点反测

2026-10-27；`/root/ell11_pan`独占原证明稿，现归[C047](../../../goals/contracts/C047-marked-cusp-borel-kernel-and-pan-gate.md)一轮预算，待root与独立fresh核。对象固定为本轮准入的g11、K11及∞单尖点配对，不调level/cusp、不构造Maass或算术lift。本稿新增的是这个**带符号核**的全局slit/Laplace表示，以及一个真实noncompact Pan的全部平移公式与大正平移严格非零；不把旧583的constant核正性运输到g11。

## 1. 输入、domain与原关系

取

\[
 g(q)=q\prod_{n\ge1}(1-q^n)^2(1-q^{11n})^2,
 \quad K(u)=\operatorname{CT}_q(e^{u j(q)}g(q)),
 \quad \ell(r)=\int_{\mathbb R}r(u)K(u)du.
\]

physical源为r=e^(u/2)f，S_exp由所有p_(N,k)=sup e^(N|u|)|D^k r(u)|固定。复线性/∞单cusp的角色不变，尚未解释为shadow系数、relativePic或Green类。原du及zero-extensionDlog全线平移不变；全S_exp费用不能被冒充为这个原norm的统一界。

本稿所需typed前件由同轮source分支逐项核，不能只凭q乘积名字采用：g是S2(Γ0(11))的无character cusp form，故ω=g(q)dq/q是X0(11)上的holomorphic differential；g在H中无零，因为η乘积的各因子不为零。X0(11)→X(1)=P1的j映射为finite cover，cusps为∞(width1)和0(width11)，有限branch values只有0、1728。Γ0(11)没有非平凡elliptic stabilizer，因而在两个有限branch值上局部ramification分别为3、2。下文给出用到这些前件的精确位置；不需要arithmetic模型、Petersson正号或未知ζ谱。

实际Pan不另造，复用[405 §4–5](../../../notes/405-f1-adelic-restriction-moments-and-radical.md)及[579 §3](../../../notes/579-kry-physical-gaussian-source-and-native-primitive-obstruction.md)已经核过的原件：

\[
 \eta(x)=\pi x^2(\pi x^2-3/2)e^{-\pi x^2},\quad
 h(u)=2\sum_{n\ge1}\eta(ne^u),\quad H(u)=e^{u/2}h(u),
\]
\[
 H>0,\quad H\in S_{exp},\quad
 p=(D^2-1/4)H\ne0,\quad
 B_\zeta(\tau_b p,s)=0\quad(b\in\mathbb R,s\in S_{exp}). \tag{1}
\]

η(0)=∫η=0及Poisson给两端的全部指数衰减；η自对偶，η(nλ)>0在λ≥1，故h在全部实u为正。每个固定b有p_(N,k)(τ_b p)≤e^(N|b|)p_(N,k)(p)，所以**这一个完整的实际Pan轨道全部在当前强源域内**；没有裁去noncompact尾、没有使用compact域中Pan交零。其Mellin规范为

\[
 M_H(t)=\int H(u)e^{tu}du
 =\frac12\xi_{Riemann}(t+1/2)>0\quad(t\in\mathbb R), \tag{2}
\]

其中正号直接来自H>0，不依赖RH。这里没有断言所有405像都自动满足任何更强新域；(1)这个逐b已核域内轨道足以反驳“消去全部关系”。

## 2. 选定j分支上的代数微分比

记a=1728。在j=∞附近取width1的inverse分支q=q(z)=z^−1+O(z^−2)，定义

\[
 R(z)=\frac{g(q(z))}{q(z)j_q(q(z))},\qquad
 R(z)\,dz=\omega.
\]

因为g=q+O(q²)、qj_q=−q^−1+O(q)，所以

\[
 R(z)=-z^{-2}+O(z^{-3}). \tag{3}
\]

这是X0(11)上的meromorphic function ω/dj所选的一个代数分支。它在

\[
 \Omega=\mathbb C\setminus[0,a]
\]

上**单值全纯**：finite cover在去掉0,a,∞后unramified；π1(Ω)由绕整条cut的环生成，该环等同∞附近的monodromy。所选cusp width1，故这个monodromy固定所选sheet。这里仅使用固定这个branch，不要求整个degree12 cover的monodromy平凡。有限处ω/dj只可能在dj=0的branch点有pole，Ω中没有这些点。

Laurent coefficients在实轴为实，唯一延拓给R(bar z)=overline R(z)。它在cut的两个bank上有解析boundary值R_±(t)，且R_−=overline R_+。在0的各相关局部coordinate w有z=const·w³+…、ω=holomorphic·dw，故

\[
 R(z)=O(z^{-2/3})\quad(z\to0). \tag{4}
\]

在a处选q_i=e^−2π，对z>a且靠近a的所选实branch有q<q_i。令

\[
 \alpha=\frac12j_{qq}(q_i)>0,\qquad
 A=\frac{g(q_i)}{2q_i\sqrt\alpha}>0.
\]

正号的支付不需q导数与τ导数混用：j在τ=i的S-fixed-point不变性给j_q(q_i)=0；583已付j=q^−1+744+Σ_(n≥1)c_nq^n且c_n≥0，所以j_qq(q_i)=2q_i^−3+Σn(n−1)c_nq_i^(n−2)>0。标准j−1728=E6²/Δ另核该branch值。g(q_i)>0由0<q_i<1的q乘积逐因子为正。所选inverse解满足

\[
 q-q_i=-\alpha^{-1/2}(z-a)^{1/2}+O(z-a),
\]
\[
 R(z)=-A(z-a)^{-1/2}+O(1). \tag{5}
\]

平方根在z>a取正。特别地，上bank t<a有(z-a)^1/2=i√(a−t)，从而Im R_+(t)的leading coefficient为**正**A，而非负号。

## 3. 紧实实cut上的signed密度与K的完整表示

定义一个真实signed L1密度（不是Weil表示ρ_L）

\[
 \nu(t)=\frac1\pi\operatorname{Im}R_+(t),\quad0<t<a.
\]

(4)–(5)给ν∈L1(0,a)，并且

\[
 \nu(t)=\frac{A}{\pi\sqrt{a-t}}+O(1)\quad(t\uparrow a). \tag{6}
\]

对slit contour作Cauchy变形，小endpoint圆因exponent<1贡献趋零，∞端因(3)消失，得到

\[
 \boxed{R(z)=-\int_0^a\frac{\nu(t)}{z-t}dt.} \tag{7}
\]

符号可由Plemelj核对：右边的upper-minus-lower jump为+2πiν，与R_+−R_−相同。两者之差延成整函数且在∞趋零，故为零；这也说明没有遗漏polynomial或point-mass项。端点若允许simple pole才会产生额外原子，本对象没有该pole。

取足够小的正向q圈，j像绕cut**顺时针**一次。因此

\[
 K(u)=-\frac1{2\pi i}\oint_{CCW}e^{uz}R(z)dz
 =\boxed{\int_0^a e^{tu}\nu(t)dt}. \tag{8}
\]

这个式子对全部complex u成立，右侧是compactly supported L1密度的整Laplace变换；没有抹平原physical源或偷换成unitary Mellin坐标。由(3)与(7)还可核

\[
 \int\nu=0,\qquad \int t\nu=1,
\]

分别与K(0)=0、K′(0)=CT(jg)=1相符。特别地，ν不是一个全局非负measure；右端局部正号不准升级为经典正分布。

完整强费可直接由(8)给出：对k≥0、实u，

\[
 |K^{(k)}(u)|\le a^k\|\nu\|_1 e^{a u_+}.
\]

取任意N>a，

\[
 |\ell(r)|\le\|\nu\|_1
 \left(\frac1N+\frac1{N-a}\right)p_{N,0}(r). \tag{9}
\]

这是all-S_exp的明确连续性；固定源窗的原du/Dlog费用另由相同核的L2窗norm支付。没有把(9)改称全线统一原du界。由(6)同样作elementary endpoint积分，对每个固定k≥0有

\[
 K^{(k)}(u)\sim\frac{A}{\sqrt\pi}a^k
            \frac{e^{au}}{\sqrt u}\quad(u\to+\infty). \tag{9a}
\]

因此a=1728确是这份核的正向指数型，而不只是某个任意q圈给的粗upper；这里不额外宣称某一weighted seminorm在边界N=a的完整必要充分判别。

## 4. 一个真实Pan的全平移公式与严格反例

令p_b=τ_b p，p为(1)固定的真实非零关系。compact t范围、ν∈L1及H的全部指数矩允许Fubini和两次分部积分。对每一个实b，精确有

\[
 \boxed{\ell(p_b)=\int_0^a e^{bt}
       (t^2-1/4)M_H(t)\nu(t)dt.} \tag{10}
\]

这既保全部noncompact source尾，也保同一个physical differential D²−1/4。不是把不同Pan或不同regularization逐b重选。由(2)、(6)，其密度w(t)=(t²−1/4)M_H(t)ν(t)满足

\[
 w(t)=C_0(a-t)^{-1/2}+O(1),\qquad
 C_0=\frac{A}{\pi}(a^2-1/4)M_H(a)>0. \tag{11}
\]

因而elementary Laplace endpoint估计给

\[
 \boxed{\ell(p_b)\sim
   \frac A{\sqrt\pi}(a^2-1/4)M_H(a)
      \frac{e^{ab}}{\sqrt b}>0\quad(b\to+\infty).} \tag{12}
\]

这里最后正号的严谨意义是所有充分大的正b；不声称每个b都为正或非零。无需调用未经证明的“asymptotic级数收敛”：将t=a−s，leading Cs^−1/2在s∈(0,δ)的积分为C√π b^−1/2(1+o(1))，O(1)余项贡献O(b^−1)，其余L1部分为O(e^−δb)，乘回e^ab即得(12)。

若要一个不隐藏正号的阈值形式，固定0<δ<a−1使w(t)≥(C0/2)(a−t)^−1/2在a−δ<t<a成立，令

\[
 M_\delta=\int_0^{a-\delta}|w(t)|dt<\infty.
\]

对b≥1/δ，取最右宽1/b子区间，(10)直接给

\[
 \ell(p_b)\ge\frac{C_0}{e}\frac{e^{ab}}{\sqrt b}
                 -M_\delta e^{(a-\delta)b}. \tag{13}
\]

因此可固定任一整数b0≥1/δ且Mδ√b0 e^−δb0<C0/e；所有b≥b0的真实p_b都是域内严格反例。b0存在，且只依已给g/j及固定actual H，未用Qζ、ζ零点位置或可变level。**本稿没有实际计算b0的数值或浮点ell(p_b0)；严格结论来自(10)–(13)。**

## 5. 完整两cusp记录与仅依赖它的读出

source分支另外闭合的两端记录可直接与本反例合成，但不搜索新的补偿。对每个r∈S_exp，微分F_r(j)ω在X0(11)除∞与0外holomorphic。两个punctures的Laurent负部允许essential；在去掉两小圆的compact surface上用Cauchy/Stokes仍给精确residue定理。因此

\[
 R_\infty(r)=\ell(r),\qquad R_0(r)=-\ell(r). \tag{14}
\]

这里R0必须按归一化cusp local coordinate读取，不能把width11因子遗漏后称另一个独立通道。它是整个源的compact两cusp记录，不是一个未证明存在的算术类。

任何**固定**complex系数α、β给

\[
 L_{\alpha,\beta}(r)=\alpha R_\infty(r)+\beta R_0(r)
                   =(\alpha-\beta)\ell(r).
\]

若要求它消去全部Pan，甚至只要求它消去(13)任一已核非零p_b，则必α=β；这时它在全部S_exp上为零，包括同轮537 control。因此把0 cusp直接加回来的固定线性修补只给零读出，并不能同时消关系／保非根。

更一般，任意complex-linear映射或线性商T作用于这份实际两腿boundary image，因image包含于C·(1,−1)，T(R(p_b))=0与ell(p_b)≠0直接迫T(1,−1)=0，所以T在整个source image为零。这个代数论证不需要偷加有界性，也不把有限维角色误称完整source coverage。

还应把这份相同两腿数据的像集说完整，而不把“非线性”当作免费逃逸。记B(r)=(ell(r),−ell(r))，e=(1,−1)。取(13)中任一p_b使c=ell(p_b)≠0。当前Pan及source都允许全部complex倍数，因此对每个λ∈C，p_λ=(λ/c)p_b仍为域内真实Pan，且B(p_λ)=λe。由此准确有

\[
 B(\mathcal P_{an})=B(S_{exp})=\mathbb C e. \tag{15}
\]

所以对任意仅依赖同一B、与原源无额外依赖的postmap F:Ce→Y（Y可以只是带basepoint的集合，不必是向量空间，也不必假设连续／线性），若所有Pan像都被送到同一个basepoint，则F在整个Ce上为常值，故所有source的后续读出也相同，包括537 control。等价地，若F∘B要求对加上任意Pan保持不变，由B(Pan)=Ce便同样迫常值。单纯在同B之后换一个非线性函数、范数或商标签，不能修好关系同时保留非根。

这个像集结论仍严格限**同一r↦B(r)=(ell,−ell)以及只以这份B数据为输入的source-independent后处理**。带有额外实际数据或不同source map的非线性／source-adapted修复、另一份relative边界／非标量source、不同载体或有费新数据仍未判；它们必须不再仅依赖这条Ce数据，并另给实际公式和量词，不能只改名称。上述固定线性及像集corollary都是本同一新Pan反例的标准消费，不再计另一数学轮。

## 6. 原norm必要费用、strongest-old与停止范围

同一p_b的du、Hlog/Dlog全线范数平移不变，而(12)增长如e^(1728b)/√b。因此此marked-cusp读出没有全线统一原du／平移不变log图范数界；这个必要下界来自实际Pan轨道，不能与任一Cauchy粗upper混淆。每个fixed源窗与all-S_exp强连续性仍完全合法。

本结果直接否定当前**∞单尖点scalar functional自动消全部405关系**的责任，故按准入stop不再造P_m／relativePic／Green/height，也不换level、cusp或补偿参数。原537非根由同轮source控制分支另验；即使其可见，也不能抵消(12)的关系失败。这里只反驳当前单腿source操作及仅依赖其两腿B数据的后处理；带额外实际数据／不同source map的全cusp边界修复、不同relative carrier/非标量source或有费非局部修复未判，须另给公式，不由本稿授予。

与strongest-old比较：583的a0核有正q系数，现K带g11符号且K(0)=0，不能套旧positive constant证明；(7)–(12)是本对象的新全局signed-cut尾与actualPan平移信息。553的bounded读出稠密门未被用于指数增长核；fixed rank/Baire旧反测也不重计。542+555→557 whole leading4/5负惯性UPPER、完整Γ/contact/properpowers/双pole及经典growth/core/coupling/primitiveRR责任均未改变。

本稿范围若经root/fresh闭合，应作为新实际源门/全尾反测的一数学轮范围消费，不预写为source0或长期Goal完成。证明依赖typedg、branch覆盖/单值及Cauchy方向，须与source分支和独立fresh逐项对齐后才root消费；本文不是已获准的新Goal或新授权。
