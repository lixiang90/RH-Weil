# 固定marked-cusp的Borel核、真实Pan费用与两腿退化

2026-10-27；C047预算一完整数学轮，G20261027／原0c4f基线。root按两独占稳定原稿重构；最终审查与消费状态见[前件收据](../reviews/2026-10-27/marked-cusp/root-consumption-scope.json)，draft不代消费。新本体是这个signed源核的完整compact-real Laplace表示及1728端点的定量真实Pan增长；一般Laplace唯一性、finite rank和两腿线性代数不另计。

## 1. 对象、费用和实际typed输入

q=e^(2πiτ)，j=q^-1+744+…；固定X=X0(11)及cusps {∞,0}，

\[
 g(\tau)=\eta(\tau)^2\eta(11\tau)^2
 =q\prod_{n\ge1}(1-q^n)^2(1-q^{11n})^2.
\]

官方eta变换式为唯一外部modular输入；[source原稿](../reviews/2026-10-27/marked-cusp/source-kernel-and-typed-controls.md)和[exact脚本](../scripts/ell11_source_controls.py)用12陪集、右乘S,T及其逆的48个Schreier关系核全部Dedekind phase为整数，故g∈S2(Γ0(11))、character trivial。两cusp宽1/11、阶均1，det-normalized Fricke eigenvalue−1；ω=g(q)dq/q在compactX上全纯无零。Γ0(11)无order2/3 elliptic stabilizer，index12/Riemann–Hurwitz给genus1，j-cover有限branch值0、1728，ramification为3、2，∞两局部轨道长度1、11。

这里是scalarΓ0(11)对象，不是原II2,2的Weilρ；没有构造Maass／算术Chow输入。physical r=e^(u/2)f，ALLcomplex S_exp按所有sup e^(N|u|)|D^k r|有限固定。复用583的F_r=L_r(j)、a_-m，定义

\[
 K(u)=\operatorname{CT}_q(e^{u j(q)}g(q)),\quad
 \ell(r)=\int r(u)K(u)du
        =\sum_{m\ge1}a_{-m}(r)c_g(m). \tag{1}
\]

对0<s<R<1，Cauchy给|a_-m|≤s^m p_As(r)、|c_g(m)|≤C_R R^-m，因此(1)绝对成立且|ℓ(r)|≤C_R s/(R−s) p_As(r)，p_A=∫|r|e^(A|u|)。若M_R=max|j|，则|K^(k)(u)|≤C_R M_R^k e^(M_R|u|)；fixed supp r⊂[−L,L]的原du费≤C_R√(2L)e^(M_R L)。zero-extension Dlog²=(2π)^−1∫log(2+|t|)|rhat|²≥log2||r||²，故同窗Dlog费乘(log2)^−1/2。全线强费和fixed窗原费不合并。

[实际有理证书](../reviews/2026-10-27/marked-cusp/source-controls.json)取s=1/1024、R=1/512，给M_s<1989.942、M_R<1754.306、C_R<0.0019608；E4³/Δ及q乘积exact核

\[
 (K(0),K'(0),K''(0),K'''(0))=(0,1,1486,2246795). \tag{2}
\]

## 2. 选sheet与全局signed cut

令a=1728，h=ω/dj在j=∞选width1局部分支，近∞

\[
 h(z)=\frac{g(q(z))}{q(z)j_q(q(z))}=-z^{-2}+O(z^{-3}). \tag{3}
\]

Ω=C\[0,a]并非simplyconnected；π1由绕整cut的环生成，其monodromy等于∞monodromy。width1使**所选sheet**固定，故h单值全纯于Ω，无须整个degree12 cover monodromy平凡。全局ω/dj的有限极点只可能来自dj=0；0和a的局部ramification给

\[
 h(z)=O(z^{-2/3}),\qquad h(z)=O((z-a)^{-1/2}), \tag{4}
\]

均为可积subpole。real q系数给h(bar z)=bar h(z)。设q_i=e^−2π、α=j_qq(q_i)/2>0，g(q_i)>0。选z>a对应q<q_i，实j在i的二阶极小值给

\[
 h(z)=-A(z-a)^{-1/2}+O(1),\quad
 A=\frac{g(q_i)}{2q_i\sqrt\alpha}>0. \tag{5}
\]

α>0也直接由j的正q系数二导看出。根在z>a取正，上bank根为i√(a−t)，故Im h_+(t)的右端主项为正。定义ν=(h_+−h_-)/(2πi)=Im h_+/π∈L1(0,a;R)，于是

\[
 \nu(t)=\frac{A}{\pi\sqrt{a-t}}+O(1),\qquad
 h(z)=-\int_0^a\frac{\nu(t)}{z-t}dt. \tag{6}
\]

Cauchy沿slit两bank的方向给这个负号；endpoint小圈因(4)趋零，∞因(3)消失。Plemelj亦核jump为+2πiν；无simple pole，故无遗漏原子或polynomial。h与右边之差跨cut延拓，端点subpole可去，∞趋零，Liouville闭合。

小正向q圈经j变为顺时针large-j圈；代(6)并在固定圈Fubini，准确有

\[
 \boxed{K(u)=\int_0^a e^{tu}\nu(t)dt}\quad(u\in C). \tag{7}
\]

∫ν=0、∫tν=1与(2)吻合；ν带符号，不能将其叫经典Weil的正谱测度。式(7)给|K^(k)(u)|≤a^k||ν||1 e^(a u_+)（u实）；对N>a，|ℓ(r)|≤||ν||1[1/N+1/(N−a)]p_(N,0)(r)。这份全源连续性不依赖数值算出||ν||1，旧Cauchy有理上费已独立付款。

## 3. 实际405关系：全部b公式及严格大正平移

不另造关系，沿405/579已付实际源

\[
 \eta(x)=\pi x^2(\pi x^2-3/2)e^{-\pi x^2},\quad
 h_0(u)=2\sum_{n\ge1}\eta(ne^u),\quad H=e^{u/2}h_0>0,
\]
\[
 H\in S_{exp},\quad p=(D^2-1/4)H\ne0,\quad
 B_\zeta(\tau_b p,s)=0\quad(b\in R,s\in S_{exp}). \tag{8}
\]

η自对偶且η(0)=∫η=0，Poisson和大正端正性付H的两端strong衰减/正号；固定b的全部seminorm费≤e^(N|b|)p_(N,k)(p)。所以整个这条真实noncompact Pan轨道在当前域，不裁尾、不用compact-only空测试。其原规范

\[
 M_H(t)=\int H(u)e^{tu}du=\xi_{Riemann}(t+1/2)/2>0
 \quad(t\in R) \tag{9}
\]

正号仅来自H>0，不预设RH。compact t、ν∈L1及H全部指数矩给每个实b的**同一个**精确式

\[
 \ell(\tau_bp)=\int_0^a e^{bt}(t^2-1/4)M_H(t)\nu(t)dt. \tag{10}
\]

右端密度w(t)=C0(a−t)^−1/2+O(1)，C0=A(a²−1/4)M_H(a)/π>0。令s=a−t，leading项积分√π b^−1/2，O(1)余项O(b^−1)、其余L1段O(e^−δb)，得

\[
 \boxed{\ell(\tau_bp)\sim
 \frac A{\sqrt\pi}(a^2-1/4)M_H(a)
 \frac{e^{ab}}{\sqrt b}>0\quad(b\to+\infty).} \tag{11}
\]

严格正号指所有充分大正b，不是每个b。可固定δ>0使w≥(C0/2)(a−t)^−1/2于右端，令Mδ=∫_0^(a−δ)|w|。对b≥1/δ，

\[
 \ell(\tau_bp)\ge(C0/e)e^{ab}/\sqrt b-M_\delta e^{(a-\delta)b}. \tag{12}
\]

选整数b0≥1/δ且Mδ√b0 e^−δb0<C0/e后，√b e^−δb单调下降，全部b≥b0为反例。未算数值b0或声称得到浮点反例；(10)–(12)是严格证明。[完整Pan原稿](../reviews/2026-10-27/marked-cusp/pan-relation-test.md)给各域和方向细节。

同理每个固定k有K^(k)(u)∼A a^k e^(au)/(√π√u)。a=1728是实际正向指数型，非把q圈粗上界反用。原du、Dlog/Hlog范数平移不变，所以(11)给无全线统一原norm费用的必要结论；fixed窗及all-S_exp强费用仍合法。

## 4. 同一537控制与完整两腿

537为全17/16窗正性定理，没有唯一数值r*。沿583同small-evenφ族rφ=(D²−1/4)(uφ)，φ≥0非零偶、suppφ⊂(−2^−20,2^−20)，有双polezero且Qζ(rφ)>0。令V11=K''−K/4，(2)给V11′(0)=8987179/4>0；source有理证书给该窗内variation<17741.14，同时旧a0核的variation亦严格小于其正导数。因此**每个同一φ**同时有ℓ(rφ)>0与旧a0(rφ)>0。不冒充573另一固定χ源已评；只纠正旧gate的unique-sample措辞，不回滚537/583。

F_rω在X除两个cusps外全纯，essential奇点仍可用去两小disc的compact Stokes，故完整boundary记录为

\[
 \mathcal B(r)=(R_\infty,R_0)=(\ell(r),-\ell(r)). \tag{13}
\]

0坐标的width11/Fricke−1必须保留。若固定complex-linear T杀掉(11)任一非零Pan像，则T(1,−1)=0，遂杀全部source及rφ。更强的直接像集事实是：Pan允许全部complex倍数，因此一个非零p_b已给B(Pan)=B(S_exp)=C·(1,−1)。任何仅依赖这同一B数据、把全部Pan像送到同一个零/base值的postmap，即使非线性，也在整个源像上常值。不能把同B后换非线性当逃逸；未判的是带额外实际数据或不同source-map的源适应／非线性修复，而非所有Maass/relativePic/算术Chow。

## 5. 必须先扣的更强旧后果

405的H>0已蕴含一条标准compact-real Laplace唯一性门：任意固定finite complex measure μ、compact support⊂R，令ℓμ(r)=∫L_r(t)dμ(t)。若它杀(8)的全部平移，则Laplace唯一性迫

\[
 (t^2-1/4)M_H(t)\mu=0,
 \quad\operatorname{supp}\mu\subset\{-1/2,1/2\}. \tag{14}
\]

证明仅为compact支撑上对b微分得全部moments零，再用多项式稠密；M_H在实轴非零。故它在全部doublepolezero源上为零，L1密度型则μ=0。该lemma与两腿线性代数为强旧直接推论，不另计新数学。当前新增的是实际新K属于此signed-cut类的全局身份，以及(11)的**定量**Pan/必要增长；不是首次发现一般real-Laplace门。

不把(14)套到complex/unbounded谱、非固定/源适应、其他relative数据或D′正逼近中间层；后者不必逐层精确消Pan。553全线du/Hlog bounded门也未被错误用于指数增长核。

## 6. 净结论、停止与前件范围

本fixedsinglecusp读出保一个真实正窗非根，却不消实际Pan；完整两腿的同数据下降则杀全部像。停止本source的P_m/Green/height／level/cusp/补偿/paper自动续造，保真正不同的非标量relative边界、携带新实际数据的有费非局部/非线性/新source修复，须另给actual input/test/net。

新范围统一C047一完整数学轮；standardtyped/Cauchy/exactq、(14)和线性代数不另计。经典完整Γ/contact/properpowers/双pole、allcomplex原du/Dlog及mixed/growth/core/coupling/Ξ责任仍欠，542+555→557 whole leading4/5负惯性UPPER未改。本结果不是RH/正性或实质全方法类终结，长期Goal保持open。
