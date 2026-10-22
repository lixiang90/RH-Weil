# 577：保完整Γ的正修补、原费用与未付算术预算

2026-10-22；C040，同G20261014／固定0c4f。沿576选择允许的真Γ修补，不续其宽尺度原料。新增的是一个实际、无零点输入的逐层连续正谱规则，以及完整Γ协同的L¹／Fourier-L¹和原源费用；修补消失仍承担完整Weil责任。本稿没有证明RH。

## 1. 同一完整目标与源

物理\(r=e^{u/2}f\)，\(\widehat r(t)=\int r(u)e^{-itu}du\)，\(r^*(u)=\overline{r(-u)}\)。第一变量线性，\(B_W(r,s)=W(r*s^*)\)。固定
\[
 W_\zeta=W_\Gamma+M,\qquad M=H-P,
 \quad H=2\cosh(u/2)du,
\]
\[
 P=\sum_{n=p^k\ge2}\frac{\Lambda(n)}{\sqrt n}
       (\delta_{\log n}+\delta_{-\log n}),\quad
 \Gamma(t)=\Re\psi(1/4+it/2)-\log\pi.                         \tag{1}
\]
569指定的完整FP/contact为
\[
 W_\Gamma(h)=\Gamma_0h(0)+\int_0^\infty2a(v)
       [h(0)-(h(v)+h(-v))/2]dv,
 \quad a(v)=\frac{e^{-v/2}}{1-e^{-2v}},\quad\Gamma_0=\Gamma(0).
                                                                  \tag{2}
\]
全部proper powers及双pole保留。compact全complex源先定义，405全主关系另在\(\mathcal S_{\exp}\)消费，原du与全线zero-extension Dlog／Hlog不换域。

选实偶、非负、非零\(\eta\in C_c^\infty((-1/2,1/2))\)，置
\[
 \phi=\eta*\eta^*/\|\eta\|_2^2,\quad\phi_R(u)=\phi(u/R),
 \quad\operatorname{supp}\phi_R\subset[-R,R],\quad R\ge1.
                                                                  \tag{3}
\]
\(0\le\phi\le1\)，正型，\(\phi(0)=1\)。记\(\kappa=-\phi''(0)=\|\eta'\|_2^2/\|\eta\|_2^2>0\)。由\(\phi''\)是\(-\eta'\)的自相关，\(\|\phi''\|_\infty=\kappa\)，故
\[
 0\le1-\phi_R(u)\le\kappa u^2/(2R^2).                       \tag{4}
\]
arithmetic截断R与物理源窗L始终分开。
有效计算时可固定\(\eta(u)=\exp[-1/(1-16u^2)]\)于\(|u|<1/4\)，外部取0；无需以未知目标选择窗口。

## 2. 每层保Γ的有限原数据

先取裸signed层
\[
 G_R=W_\Gamma+\phi_RM,\qquad g_R=\widehat G_R,
\]
\[
 g_R(t)=\Gamma(t)+2\int\phi_R(u)\cosh(u/2)\cos(tu)du
       -2\sum_{n\le e^R}\frac{\Lambda(n)}{\sqrt n}
                  \phi(\log n/R)\cos(t\log n).                \tag{5}
\]
求和每个幂都按真实\(\log p\)权进入；窗外余量明确为\((1-\phi_R)M\)，没有把它从目标删除。Γ没有被窗化。\(G_R\to W_\zeta\)于D′，无需RH。

\(B_R=\|\phi_RM\|_{TV}\)有独立粗预算
\[
 B_R\le8\sinh(R/2)+2\sum_{n\le e^R}\Lambda(n)/\sqrt n
        \ll e^{R/2}.                                       \tag{6}
\]
这里使用旧Chebyshev／555部分求和，不能以较弱\(\Lambda(n)\le\log n\)界报新前沿。\(g_R\)实偶连续且\(g_R(t)=\Gamma(t)+O_R(1)\to+\infty\)。digamma级数给Γ在正半轴递增；取有效整数\(T_R\)使\(\Gamma(T_R)>B_R+1\)，则全部负区都在\([-T_R,T_R]\)。粗\(T_R\)可达\(\exp(O(e^{R/2}))\)，有限高度不代表费用小。

定义完全不读取未知ζ零点的量
\[
 q_R(t)=(-g_R(t))_+,\quad c_R=\|q_R\|_\infty,
 \quad m_R=(2\pi)^{-1}\|q_R\|_1.                           \tag{7}
\]
q_R是非负连续紧支密度，\(c_R\le[-\Gamma_0]_++B_R\)。它是对显式有限数据函数的求值／积分规则，不是先选择正的未知零点测度。

## 3. 保contact的正层与有费光滑修复

单加\(c_R\delta_0\)可正化，但会改变总contact。为保原contact，改取
\[
 K_R(u)=(2\pi)^{-1}\int q_R(t)e^{itu}dt,
 \qquad\widetilde V_R=G_R+K_R(u)du.                         \tag{8}
\]
K_R是实偶entire光滑函数，无额外δ或point-supported项；Γ的完整有限部分、奇性和指定contact逐层保留。且
\[
 \widehat{\widetilde V_R}=g_R+q_R=(g_R)_+\ge0,\quad
 Q_{\widetilde V_R}(r)=(2\pi)^{-1}\int(g_R)_+|\widehat r|^2dt\ge0.
                                                                  \tag{9}
\]
这无条件给每层正证书；没有证明K_R趋零。修补后的分布也未被证明来自新的正primitive g-system或canonical completed zeta：窗权\(\phi(k\log p/R)\)不自动是一个primitive权的全部幂，K_R另有谱身份。普通determinant／整数重数／算术截面均未自动取得。

若要求K为Schwartz，选\(\rho_R\in C_c^\infty([-2T_R,2T_R])\)实偶、0≤ρ≤1、在[-T_R,T_R]恒1，令
\[
 q_{R,\epsilon}=\rho_R\frac{\sqrt{g_R^2+\epsilon^2}-g_R}{2},
 \quad\epsilon_R=R^{-2}/(1+2T_R).                           \tag{10}
\]
则\(g_R+q_{R,\epsilon}\ge0\)，\(0\le q_{R,\epsilon}-q_R\le\epsilon/2\)，其L¹差≤2T_Rε≤R⁻²。逆Fourier为Schwartz，保contact且有明确附加费用；不是无误差的“抹平保正”。

**与576的类型区别。**如果g_R在一个开区间负，加入任意局部有限纯点正谱，仍无法取消负的绝对连续部分：在负区间去掉其全部原子，signed测度仍负。因此有限cos或576有限FF正混合不能逐层替代(8)的连续修补。D′极限可以产生连续谱，故这不否定576的闭包定理。

## 4. 完整Γ协同误差及原du的匹配阶

由(2)、\((1-\phi_R)(0)=0\)，严格得到
\[
 (1-\phi_R)W_\Gamma=-\mu_R(u)du,\quad
 \mu_R(u)=(1-\phi_R(u))a(|u|)\ge0,
 \quad G_R=\phi_RW_\zeta-\mu_Rdu.                           \tag{11}
\]
这里contact恰好消去，不能另选有限部分常数。令
\[
 e_R=\|\mu_R\|_1\le C_0/R^2,\quad
 C_0=\frac\kappa2J,\quad
 J=\int_{\mathbb R}u^2a(|u|)du
   =32\sum_{n\ge0}(4n+1)^{-3}.                             \tag{12}
\]
\(R^2e_R\to C_0>0\)由Taylor和dominated convergence给出。对全部原du源，卷积误差的operator norm**恰为e_R**：\(|\widehat\mu_R(t)|\le e_R\)，在t=0取等。因此(11)相对整块Weil窗化的全线du费用为匹配R⁻²阶。

物理\(-\mu_R\)是负测度不意味着其二次型为负；\(\widehat\mu_R\)可以变号。已付的是绝对费用。\(e_R\delta_0-\mu_Rdu\)倒确为正型，因为乘子\(\int\mu_R(u)(1-\cos tu)du\ge0\)，但它有contact，不能替代(8)宣称规范未改。

## 5. 无RH的Fourier-L¹预算

还可证明
\[
 \|\mu_R''\|_{TV}\le C_2/R^2,\quad
 |\widehat\mu_R(t)|\le R^{-2}\min(C_0,C_2/t^2),\quad
 \|\widehat\mu_R\|_1\le4\sqrt{C_0C_2}/R^2.                 \tag{13}
\]
C₂只依赖固定窗口和指定Γ，可显式取自分支的(13)。关键不能将三项奇性分别取绝对值：令\(a(v)=1/(2v)+h(v)\)，h在[0,1]光滑，\(b=1-\phi(v/R)\)。对v>0，
\[
 (b/(2v))''=b''/(2v)-b'/v^2+b/v^3.
\]
b的\(\kappa v^2/(2R^2)\)项精确抵消；四阶Taylor余项给\(O(v/R^4)\)。h部分用\(|b|\le\kappa v^2/(2R^2)\)、\(|b'|\le\kappa v/R^2\)、\(|b''|\le\kappa/R^2\)积掉。v≥1用a及其导数指数尾。原点\(\mu_R\sim\kappa|u|/(4R^2)\)，二阶导含\(\kappa\delta_0/(2R^2)\)，必须计入TV。故C₂有限，再分段积分得(13)。

这是独立Γ／窗口误差，不是实际负谱q_R已经小的证明。

## 6. 修补的实际原费用与成长量词

对原全线L²，修补自身有
\[
 0\le Q_{K_R}(r)\le c_R\|r\|_2^2;
 \quad\operatorname{supp}r\subset[-L,L]\Longrightarrow
 Q_{K_R}(r)\le2Lm_R\|r\|_2^2.                              \tag{14}
\]
第一条为乘子sup，第二条为\(|\widehat r|\le\|r\|_1\)；二者取min，不拿辅助全空间lower当实际源费。

设
\[
 D_L=\frac\kappa2\int_{[-2L,2L]}u^2d(H+P)(u)
       \ll(1+L^2)e^L.
\]
完整Γ在比较中精确相消，全部相关proper powers仍在D_L，故对该窗全部complex原源有
\[
 |Q_{G_R}(r)-Q_\zeta(r)|\le D_LR^{-2}\|r\|_2^2,
\]
\[
 |Q_{\widetilde V_R}(r)-Q_\zeta(r)|
    \le[D_L/R^2+\min(c_R,2Lm_R)]\|r\|_2^2.                 \tag{15}
\]
mixed误差同样成立。经fixed窗core延至原zero-extension Dlog域，用\(\|r\|_2\le\|r\|_{H_{\log}}\)及既定Dlog等价常数即可。层本身含Γ，du上无界；**两层之差**在fixed窗du上有界，不可混写。

L成长时须保\(D_L/R^2\)与修补的共同预算；例如\((1+L^2)e^L/R^2\to0\)是充分条件，非必要阈值。没有全线全部支撑共享的小常数。光滑版本另加≤ε_R/2的du费或≤2T_Rε_R/(2π)的谱质量费。

## 7. 405全主关系：逐层失败与逐固定源运输

405实际\(p=(D^2-1/4)H_0\ne0\)、H₀>0，及其全部平移属于物理\(P_c\subset\mathcal S_{\exp}\)。完整目标无RH即有\(B_\zeta(p,s)=0\)。它们不是compact测试；只检\(P_c\cap C_c^\infty\)没有内容。

每个(9)在足够高频率有严格正密度；非零S_exp源的Fourier为非零整函数，故
\[
 Q_{\widetilde V_R}(p)>0\quad(0\ne p\in P_c).              \tag{16}
\]
因此逐层真Γ正证书确实不能下降405商。一般exact消p的正谱必须支持在\(\widehat p\)的实零集，405给其中含\(s(s-1)\xi(s)\)；这是验收约束，不能拿未知零点来选择本轮系数。

本recipe却能独立补上固定强源尾。对N>1/2，
\[
 A_N=\int u^2e^{-N|u|}d(H+P)(u)<\infty,
\]
其prime部分为\(\sum\Lambda(n)(\log n)^2n^{-N-1/2}\)。故对任意固定r,s∈S_exp，
\[
 |B_{G_R-W_\zeta}(r,s)|
 \le\frac{\kappa A_N}{2R^2}
       \sup_u e^{N|u|}|(r*s^*)(u)|.                        \tag{17}
\]
卷积半范数由更强指数源半范数控制，对其有界集统一；加(14)即给每个固定p及固定平移的近似消去费用。预算消失时所有固定关系配对趋0，但不是逐层actual几何主同构。

更强的“全部Hlog归一化主关系统一消去”被553排除。每层(9)在全线Hlog有界，高频compact调制源的Q/Hlog²趋1；Pan在该原norm稠密，故
\[
 \sup_{p\in P_c\setminus0}
 Q_{\widetilde V_R}(p)/\|p\|_{H_{\log}}^2\ge1              \tag{18}
\]
对每个R成立。逐固定p的(17)与(18)量词不同，不矛盾。完整Wζ若全线Hlog有界，杀稠密Pan会迫其为零，与537矛盾；因各层有界，\(\widetilde V_R-W_\zeta\)的全线Hlog operator绝对差sup对每层都是∞。固定窗小费不跨越这个门。

## 8. 537非根无需先消修补

537在固定L₀=17/16的全complex原域有\(Q_\zeta\ge\tau\|r\|_2^2\)，τ>0。由(15)裸层误差与Q_K≥0，直接得
\[
 Q_{\widetilde V_R}(r_0)
 \ge(\tau-D_{L_0}/R^2)\|r_0\|_2^2>0                     \tag{19}
\]
最终对该窗全部源成立。这是无条件raw非根可见性，不需要c_R或m_R先趋0；值收敛／upper与正确关系商仍需预算。不能把537这个旧固定窗推成任意成长窗的独立正号。

## 9. 哪个预算仍恰为RH

在**完整Weil正性／RH前件下**，\(\phi_RW_\zeta\)正型，其Fourier为非负密度k_R。由(11)
\[
 g_R=k_R-\widehat\mu_R,\quad
 0\le q_R\le(\widehat\mu_R)_+\le|\widehat\mu_R|.
\]
于是
\[
 c_R\le C_0/R^2,\qquad
 m_R\le2\sqrt{C_0C_2}/(\pi R^2).                          \tag{20}
\]
未付的正是k_R≥0，不能用此条件推导宣布(20)已独立成立。

反向若任意cofinal子列c_R→0或m_R→0，则K_R→0于D′（分别用\(c_R\|\widehat h\|_1/(2\pi)\)或\(m_R\|h\|_1\)），正层趋完整Wζ，闭锥给RH。因此对于**本特定family**，
\[
 RH\iff c_R\to0\iff m_R\to0\iff K_R\to0\text{于D′};       \tag{21}
\]
任一cofinal子列版本也等价；Schwartz修补多出的已付R⁻²不改变它。这里D′⇒sup／质量消失借助“极限正性⇒RH⇒(20)”的完整身份，绝不是一般D′拓扑控制sup的假定。

无条件现有prime／pole预算只给(6)及有限修补，没有趋零。若有实际compact负源Qζ(r)<0，正层和(15)会迫\(\liminf c_R\ge-Qζ(r)/\|r\|_2^2>0\)，或实际源Q_K不消失。仅把这些缺陷改名“容量差”仍是等价责任。等价并不禁止未来独立证明；本轮没有那项算术输入。

## 10. 连续正反例与真函数域

使用模型自身Γ/contact、全部powers与poles，不插入经典Γ改目标：

- 连续正段\(W_+=2\cos(u/4)du\)、Γ=0：\(\widehat{\phi_RW_+}\)是两份非负\(\widehat\phi_R\)，hard修补q_R=0；原误差O_L(R⁻²)独立成立。
- 连续负段\(W_-=2\cosh(u/4)du\)、Γ=0：已有实际compact双polezero\(r_-=r_1-\tau_hr_1\)，\(r_1=(D^2-1/4)\eta_0\)，全mixed Gram给Q₋(r₋)<0。正化必须\(\liminf Q_{K_R}(r_-)\ge-Q_-(r_-)>0\)，故修补不能D′消失。该模型g_R为Schwartz而非趋log∞，负部仍L¹但不声称它有有限高度支撑；经典有限高度结论只用在有真Γ的层。
- 真曲线\(W_C=\ell\sum_{n\in\mathbb Z}\operatorname{Tr}(U^n)\delta_{n\ell}\)由旧独立正H／RR及全递推给正型，原点contact保持，所有周期poles和aliases均保。\(\phi_RW_C\)正型，hard修补为0。不能只取一个fundamental strip。Schwartz soft版本即使在正例也可能多出小正质量，按(10)计费，不能写成精确0。

函数域的0费用来自已付同对象几何正号；它不能代付经典(20)的前件。独立原证明来源与trace/正性区分可参[Connes–Consani–Marcolli](https://arxiv.org/abs/math/0703392)及567既有核读。

## 11. 新输入、强旧和停止

本轮真正闭合了：真Γ/contact逐层的显式连续正修补（含有费Schwartz）；Γ协同全线du匹配R⁻²与Fourier-L¹预算；实际fixed窗全complex原费和强源尾；以及纯点正原料不能取消负ac的类型门。174的正部投影、562的闭锥、569 Γ规范、553密度和537固定窗均准确扣旧；没有从“取正部”得到新经典正性。

局部表示／费用瓶颈改变：576的漏Γ门已用合法真Γ层绕过，原费用的合法量词更清楚。宏观未付仍是从原素数幂／pole数据独立支付实际q_R的小质量／乘子预算，或从同一算术对象的有效截面／RR容量给这项signed比较。strong-old542＋555→557 whole leading4/5负惯性上预算与actual成长core／coupling／Ξ未改，Goal门open。

在这里停止窗口／负部recipe；不续调R、网格、soft参数或以未知正谱作求积。下一重新准入须给一个具体、未用RH的算术主要化或几何容量实物及净后果；只要求q_R趋0不构成新输入。其他联合、非局部、源适应、变域和有费无限修补均未被排除。C040一轮及cycle15复盘以最终fresh/root统一结算，不按分支或文件数计轮。
