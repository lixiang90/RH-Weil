# 566. 从分布构造正闭形式：函数域的完整热迹实现与经典源的检验

2026-10-20，C029；固定G20261014／0c4f≤538。用户要求执行565留下的构造门。
本轮得到一个明确成功例：**由函数域全递推和独立正能量矩阵，构造圆周bundle上的
正闭形式，并从heat kernel证明其普通热迹等于完整Weil热量，所有时间、周期和重数均保留。**
连续正反例和非酉边界揭示失败位置；经典ζ尚未得到这样的同源身份。

## 1. 三个对象不能合并

P／Π／M固定右半平面Z，预定完成化／权及全部背景后给完整分布W。
Weil型是Q_W(g)=W(g*g*)，g∈Cc∞(R;C)。目标热量是

\[
 k_t(u)=(4\pi t)^{-1/2}e^{-u^2/(4t)},\qquad\Theta_W(t)=W(k_t). \tag{1}
\]

另一Hilbert空间上的正闭形式e给K≥0；须另外从源证明
Tr e⁻ᵗᴷ=Θ_W(t)。若W为563的实偶有限指数阶完整分布，这个all-time identity给
全阶CM及全部complex compact Weil正性。此充分机制是565旧接口，本次检验实际构造。
fixed-window Q_L自己的算子热迹、目标Θ_W、任意自动平方算子的热迹是不同对象。

## 2. 最直接的正Π跳跃形式：真闭性，却没有普通热迹

选收敛σ，νσ=e^{−σu}Π为有限正测度，mσ为其总质量。在L²(R,dx)定义

\[
 e_\sigma[f]=\tfrac12\int\|T_uf-f\|^2d\nu_\sigma(u),
 \quad K_\sigma=\int[I-(T_u+T_{-u})/2]d\nu_\sigma(u).       \tag{2}
\]

0≤Kσ≤2mσI，所以(2)是domain全部L²的正闭Dirichlet形式。
但exp(−tKσ)≥exp(−2tmσ)I，无限维载体上所有t>0的ordinary trace均为∞。
bounded jump移到有限长度circle仍有同一问题；一般全线translation-invariant heat
作为非零Fourier乘子也不compact。保confinement、unbounded有限体积、换载体或另种trace逃逸。
safe Euler正计数的自动正性因此没有支付(1)。证明见
[直接jump原稿](../reviews/2026-10-20/grh-heat-forms/direct-jump-and-continuous-form-tests.md)。

## 3. 连续正反例：从源ODE得到正确K，自动C*C则换掉热量

562／563的positive continuous族Z_c=1+c/[s(s−1)]、0<c≤1/2给全部源身份

\[
 W_c''+dW_c=0,\quad W_c(0)=2,\ W_c'(0)=0,\quad d=c-1/4.    \tag{3}
\]

在C²标准内积直接定义e_c(v)=d||v||²。d≥0时它是正闭形式，K_c=dI₂。
由热方程与(3)，Θ_c′=−dΘ_c、Θ_c(0+)=2，故

\[
 \operatorname{Tr}e^{-tK_c}=2e^{-td}=\Theta_c(t),\qquad t>0. \tag{4}
\]

无须先读根。d=0仍用C²保trace2。d<0时同一源Θ_c递增，任何正K的ordinary heat trace
非增，故不能匹配。决定性输入d≥0由源参数独立核验；在这个有限类中与pure阈值等强，
具体证明并不因等价而循环。

对源companion C=[[0,1],[-d,0]]，自动标准平方C*C=diag(d²,1)始终正，
但其热迹e⁻ᵗᵈ²+e⁻ᵗ与(4)一阶导数相差(d−1)²，本族全部参数都不相同。
只有另付源内积G>0及C^{*_G}=−C，才有C^{*_G}C=dI₂。
这不是新的连续RH结果，而是正确内积／目标heat身份的固定反测试。

562的连续谱log混合另有正state热量2∫e⁻ᵗλdν(λ)，其中λ=τ²，ν是原混合测度的该映射像；其乘法算子在nonatomic L²(ν)上
没有有限ordinary heat trace；完成对象还有分支，失败严格entire除子前件。
因此本稿的ordinary-trace目标不是所有更广连续谱类RH的必要公理；state／半有限trace版本须另定对象。

## 4. 函数域：由全点数递推构造正闭形式，直接证明热迹身份

曲线C/F_q先由有理性／FE给P(T)、m=2g，q与grading由几何预先给出。令

\[
 L=\log q,\quad a_0=m,\quad
 a_n=q^{-n/2}(q^n+1-N_n),\quad a_{-n}=a_n.
\]

全部闭点／proper powers和全部周期pole背景给源

\[
 W_C=L\sum_{n\in\mathbb Z}a_n\delta_{nL}.                \tag{5}
\]

假设从同一全递推已独立核出有限U、H=H*>0，满足U*HU=H及a_n=Tr Uⁿ（全部n）。
这一步的正能量不是对偶自动给的，563已用F5证书支付过。现在定义新的具体载体和形式：

\[
 \mathscr H=L^2((0,L),\mathbb C^m;Hdx),\quad
 V_U=\{f\in H^1:f(L)=Uf(0)\},\quad
 e_U[f]=\int_0^L f'^*Hf'\,dx.                           \tag{6}
\]

端点评价连续，V_U闭于H¹且含内部compact smooth源，故(6)稠密、正、闭。
分部积分及U*HU=H给表示算子

\[
 K_U=-\partial_x^2,\quad
 D(K_U)=\{f\in H^2:f(L)=Uf(0),\ f'(L)=Uf'(0)\}.          \tag{7}
\]

Neumann能量的min–max比较给Tr exp(−tK_U)≤mΣ_{k≥0}exp(−tπ²k²/L²)<∞，全部t>0。
从unitary延拓f(x+nL)=Uⁿf(x)直接构造

\[
 \mathcal K_U(t;x,y)=\sum_{n\in\mathbb Z}U^n k_t(x-y-nL). \tag{8}
\]

Gaussian尾控制全部局部time／空间导数；(8)满足(7)边界、热方程、半群律和初值，
因此就是K_U的heat kernel。取diagonal trace得到

\[
 \boxed{\operatorname{Tr}e^{-tK_U}
 =\frac{L}{\sqrt{4\pi t}}\sum_{n\in\mathbb Z}\operatorname{Tr}(U^n)e^{-n^2L^2/(4t)}
 =W_C(k_t),\quad\forall t>0.}                          \tag{9}
\]

最后一等号仅用全源(5)和trace递推，无ζ根输入。n=0保rank/contact，n≠0保所有period。
F5例y²=x³+x+1用N1=9、genus-one有理性给

\[
 A=\begin{pmatrix}0&-5\\1&-3\end{pmatrix},\quad
 U=A/\sqrt5,\quad H=\begin{pmatrix}1&-3/2\\-3/2&5\end{pmatrix},
 \quad\det H=11/4,\quad A^THA=5H.                       \tag{10}
\]

Cayley–Hamilton支付全部n。N2=27,N3=108仅作旧证书复核，不用有限枚举外推。
新结果是明确的closed-form/heat lift；同一U,H早已给563完整Weil平方和，
不再声称新的函数域纯性证明。详见
[函数域构造原稿](../reviews/2026-10-20/grh-heat-forms/function-field-holonomy-heat-construction.md)。

## 5. 非酉端点：形式照样为正，源身份严格失败

对任何可逆M，以f(L)=Mf(0)定义同一个导数能量，仍正、稠密、闭。
它的真实自然导数边界却是

\[
 M^*H_0 f'(L)=H_0 f'(0),                               \tag{11}
\]

只有M为H0-unitary才能换成f′(L)=Mf′(0)。擅用后者正是把未付极化塞进heat身份。
取290正Euler反模型q=5、P_−=1−5T+5T²，M=[[0,−5],[1,5]]/√5。
其源a_n=rⁿ+r⁻ⁿ、r=(√5+1)/2>1，(5)的热量在t→∞无界增长。
取最接近2t log r/L²的整数可直接给下界

\[
 \Theta_-(t)\ge\frac{L}{\sqrt{4\pi t}}
 \exp\!\left[t(\log r/L)^2-L^2/(16t)\right]\to\infty.     \tag{12}
\]

相同M的正形式算子反而有正gap，heat trace→0。它无常数零能量态，因为1不是M的特征值。
两者绝不相同；image sum虽收敛，也给另一个非自伴边界问题，不能冒充(11)的正算子。

## 6. 正Weil型本身也不能直接在原L²全线闭包

即使Q_W已经正，若其Fourier正测度有孤立原子γ0，它在原L²(du)上不可闭。
取φ∈Cc∞、∫φ=1，g_R(u)=R⁻¹eⁱᵞ⁰ᵘφ(u/R)。则||g_R||²→0，
但Fourier取值在γ0恒1、在其他谱上趋0；多项式增长及快速下降给Q(g_R−g_S)→0、
Q(g_R)→该原子质量>0，违反可闭性。
连续正例(4)的Weil型已如此，正确闭能量却在另一个C²载体上。
经典若Q_W正，Weil判据给RH并识别离散正测度，随即同样不可闭。
因此直接“Q正→原全线L²上的Friedrichs K→所需heat”不是可行推导。
这不排fixed支撑窗、增强source norm、GNS或不同载体；更广绝对连续性标准是
[Alpay–Jorgensen Theorem4.2](https://arxiv.org/pdf/1109.5273)的已有结果。

## 7. 经典完整Γ／primepowers／双pole：已执行的具体比较

保actual Γ∞(y)=Reψ(1/4+iy/2)−logπ，完整源是

\[
 \Theta_\zeta(t)=2e^{t/4}+\frac1{2\pi}\int_{\mathbb R}e^{-ty^2}\Gamma_\infty(y)dy
 -\frac2{\sqrt{4\pi t}}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}e^{-(\log n)^2/(4t)}. \tag{13}
\]

等价的finite-part/contact差分表达在563(13a)；不能把Γ穿孔核当通常正测度。
直接把全部prime改成正jump会遇到准确减项

\[
 -2\sum_{n\le X}a_n\Re h_f(\log n)
 =\sum_{n\le X}a_n\|T_{\log n}f-f\|^2-2A_X\|f\|^2,
 \quad A_X=\sum_{n\le X}a_n\to\infty.                   \tag{14}
\]

全线未减的primejump对每个非零L²源都∞，因为translations远处趋不相关且尾质量无限。
其domain={0}，不是稠密闭形式。compact源的(14)却在tail精确相消。
Γ有合法Dlog正jump，但它不消掉负degree/pole coupling。016/541/543已付fixed-window分解，
不能把该旧signed分解宣称为新的whole正形式或(13)的heat算子。

从(13)自身、Stirling和Gaussian尾，无RH可得

\[
 \Theta_\zeta(t)=\frac{\log(1/t)-\gamma_E-\log(16\pi^2)}{4\sqrt{\pi t}}+O(1),\quad t\downarrow0. \tag{15}
\]

普通有限紧metric graph的正Laplace energy只有总长/√(4πt)+O(1)，故不匹配(15)。
这不排无限图。实际可行逃逸是区间I_n=(0,1/n)的Dirichlet能量直和；它正闭、紧resolvent、
所有t ordinary trace-class，且不用ζ根可算

\[
 \operatorname{Tr}e^{-tK_{\rm div}}=\sum_{m\ge1}d(m)e^{-\pi^2m^2t}
 =\frac{\log(1/t)+3\gamma_E-2\log(2\pi)}{4\sqrt{\pi t}}+o(t^{-1/2}). \tag{16}
\]

它匹配log首项，但次项比(15)多4γ_E+log4>0，故这个具体形式仍非完整经典热量。
这是[Egger–Steiner无限量子图](https://arxiv.org/pdf/1104.1364)的缩放实例，来源及域证明见
[经典源审查原稿](../reviews/2026-10-20/grh-heat-forms/classic-full-source-form-and-heat-audit.md)。
调Weyl系数不足以给all-time源身份；不据此排其他无限图、confining算子或奇异几何。
relative/regularized trace也不自动CM，例如e⁻ᵗ−e⁻²ᵗ虽正却近0递增。

## 8. 真正输入、净后果及下一准入

本次非循环成功依赖的是**源已给全递推＋显式正H**，继而用(6)–(9)付清具体heat实现。
这些输入在F5独立可核；对一般g-integer，它们不是正P／宽对偶的自动后果。
新固定失败信息是：safe jump无ordinary trace；任意平方换heat；非unitary端点改导数条件；
physical-Q闭包不成立；finite graph/具体infinite graph不匹配完整经典源。
各失败仅限所证类，保换norm／载体、无限维、source适应、非局部和有控relative修复。

经典仍欠从(13)的同一算术输入构造明确Hilbert载体和正闭能量，并证明其all-time普通热迹身份。
只要求存在K、全CM或从未知实零点造K仍是RH等价改写；函数域旧H不代经典新正性。
actualζ强旧542+555→557 whole4/5、560成长K/core/coupling未改，宏观门open。
本合同一迭代结束后不调图长拟合零点；重准入须新同源迹公式／独立极化或具体actualsigned净费。
