# 577后prime／pole平方身份准入：准确方向、旧连续族与全周期函数域

2026-10-22。本稿只承担独立分支输出，不建合同、不计轮、不改STATE。已恢复README／STATE、check/show、G20261014／C040／D20261022L及macro前沿；核读577、562、563、567和旧036、169、299的相应原件。固定0c4f与strong-old542＋555→557 whole leading4/5负惯性**上预算**，不将来源审查或下面旧族的直接计算升级为新经典正性。

## 1. 实际被付对象与所需方向

沿577，物理r=e^{u/2}f，Fourier约定\(\widehat r(t)=\int r(u)e^{-itu}du\)，全部complex源；compact先定义，405实际主关系在\(\mathcal S_{\exp}\)而非compact消费。完整Γ、指定FP/contact、全部proper powers与双pole均不改：
\[
 G_R=W_\Gamma+\phi_R(H-P),\qquad
 g_R(t)=\Gamma(t)+H_R(t)-P_R(t),
\]
\[
 P_R(t)=2\sum_{n\le e^R}a_n\cos(t\log n),\quad
 a_n=\frac{\Lambda(n)}{\sqrt n}\phi(\log n/R)\ge0,
\]
\[
 H_R(t)=2\int_{\mathbb R}\phi_R(u)\cosh(u/2)\cos(tu)du,
 \quad q_R=(P_R-\Gamma-H_R)_+.
 \tag{1}
\]
\(c_R=\|q_R\|_\infty\)，\(m_R=(2\pi)^{-1}\|q_R\|_1\)。这里a_n中的\(\Lambda(p^k)=\log p\)保留全部k；\(\phi(k\log p/R)\)没有被偷换为一个primitive权的幂。

要独立付c_R，实际需要同一线性量的上界\(P_R(t)\le\Gamma(t)+H_R(t)+\epsilon_R\)；要付m_R，需要实际正超额\((P_R-\Gamma-H_R)_+\)的积分小量。这些**描述目标**，不算新增输入。577已经证明本family的c_R→0、m_R→0或修补在D′消失各自⇔完整Weil正性／RH。等价不禁止将来独立证明，但禁止把目标换名后声称已经付款。

## 2. 正Euler、Toeplitz与非负三角多项式付出的实际不等式

P_R是正有限对称**物理测度**\(\phi_RP\)的Fourier变换，因此
\[
 (P_R(t_i-t_j))_{i,j}\succeq0,\qquad |P_R(t)|\le P_R(0).
 \tag{2}
\]
H_R也有相同Toeplitz性质，因为\(\phi_RH\)是正有限测度。两个正核的差H_R−P_R并不因而正；Γ的有限部分也不是可任意加入的正余量。

逐原子应用\(3\pm4\cos\theta+\cos2\theta=2(1\pm\cos\theta)^2\ge0\)，严格得到
\[
 3P_R(0)\pm4P_R(t)+P_R(2t)\ge0,
 \qquad P_R(t)\le\frac{3P_R(0)+P_R(2t)}4.
 \tag{3}
\]
正号版本给P_R(t)的lower，代入g_R只给upper；负号版本方向正确，但右边仍含P_R(0)。对三点Toeplitz矩阵还得到
\[
 P_R(2t)\ge2P_R(t)^2/P_R(0)-P_R(0)
 \quad(P_R(0)>0),
 \tag{4}
\]
没有产生与Γ＋H_R之间的新相消。577已付\(P_R(0)\ll e^{R/2}\)，(2)–(4)只恢复这个巨大绝对账。若单独把H_R(0)−P_R(0)作中心化，仍须证明**调制后**的signed比较；二者各自正Toeplitz不付它。

以上同样适用于安全Euler半平面\(\sum\Lambda(n)n^{-\sigma}\cos(t\log n)\)、σ>1。正primitive／正integer测度也给\(Z(s+\bar w)\)型正Gram（在实际绝对收敛域），但不是\(\Gamma+H_R-P_R\)的正Gram。对全纯延拓后的同名核，不能将原绝对收敛域的正性无误差延拓到临界处。

## 3. 两种“平方”及Selberg二阶身份不能直接置换

在Re s>1令
\[
 U(s)=\sum_{n\ge2}\Lambda(n)n^{-s}=-\zeta'(s)/\zeta(s).
\]
无条件代数身份为
\[
 -U'(s)+U(s)^2=\zeta''(s)/\zeta(s),
 \quad U(s)^2=\sum_n(\Lambda*\Lambda)(n)n^{-s}.
 \tag{5}
\]
u=log n坐标下，U²编码**和频**u+v／乘法卷积；它不是边界上的Hermitian平方\(|U(\sigma+it)|^2\)，后者编码**差频**u−v。Γ与pole的交叉项也没有包含在(5)中。

对实际有限多项式\(D_R(t)=\sum a_ne^{it\log n}\)，
\[
 |D_R(t)|^2=\sum_na_n^2+
 2\sum_{m<n}a_ma_n\cos(t\log(n/m)).                     \tag{6}
\]
这确实逐t非负，但新增的是ratio频率（通常非整数的log）、二次系数a_ma_n和contact \(\sum a_n^2\)。它不是(1)的线性prime-power项；将它用于g_R必须另证这些新增项与完整Γ／pole预算之间的有符号比较。\(2\Re D\le\epsilon|D|^2+\epsilon^{-1}\)这类完成平方只引入该新预算，没有消去它。

旧[036§4](../../../notes/036-max-kernel-prime-square.md)已明确：Selberg乘法卷积不等于max-kernel discrepancy平方，n=6即有\((\Lambda*\Lambda)(6)>0\)而\(\Delta\psi^2(6)=0\)。本稿不把这个旧区别重报为新定理。旧[169](../../../notes/169-selberg-profile-rh-equivalence-resonance-wedge.md)还核过：polylog尺度的全尺度Selberg-order profile本身可有RH全强度；旧[299](../../../notes/299-local-one-sided-budget-mellin-strength-audit.md)对另一匹配截断给出固定频窗一侧预算的RH强度。它们的截断／核不同于577，**不直接把其定理搬来认定本family所有局部预算等价**；本family等价由577自身的完整分布身份支付。

## 4. 二阶矩：实际能付的是平均／绝对账，不是负部消失

令X=e^R，\(A_R=\sum a_n^2\)。有限和给精确式
\[
 \int_{-T}^{T}P_R(t)^2dt=4TA_R
 +4\sum_{m\ne n}a_ma_n\frac{\sin(T\log(m/n))}{\log(m/n)}
 +4\sum_{m,n}a_ma_n\frac{\sin(T\log(mn))}{\log(mn)}.       \tag{7}
\]
没有零点输入，也没有删掉off-diagonal。由\(|\log(m/n)|\ge|m-n|/X\)、\(2a_ma_n\le a_m^2+a_n^2\)得到一个足够的初等绝对上界
\[
 \int_{-T}^{T}P_R^2\le4TA_R+O(X(1+\log X)A_R+(\sum a_n)^2).
 \tag{8}
\]
旧Chebyshev部分求和给\(A_R\le R\sum_{n\le X}\Lambda(n)/n\ll R^2\)，\(\sum a_n\ll X^{1/2}\)，故误差可取O(XR³)，不是趋零。更精细MV／prime correlation输入若适用可缩小这张平均账，但须写出同一577对象的净负部后果，不能凭“二阶矩已控”跳过这一步。

例如在一个区间I上若**另有**已付\(a_I=\inf_{t\in I}(\Gamma(t)+H_R(t))>0\)，则
\[
 \int_Iq_R(t)dt\le\frac1{4a_I}\int_IP_R(t)^2dt,         \tag{9}
\]
因为\((x-a)_+\le x^2/(4a)\)。该正确方向仍包含区间长度、二阶矩与a_I责任；它不付低频负区，且对577有效但可能巨大的完整高度T_R并不给总质量o(1)。对任意给定有限t网格或平均高度的成功，也不能直接给c_R的全t上界。这里不声称任何平均方法原理上无用；只是(2)–(9)尚未给实际q_R的小费用。

## 5. 连续正反对照：连ordinary Selberg主预算也两段皆过

使用562已证有真正正primitive／全powers／正g-integers的旧族
\[
 Z_c(s)=1+\frac c{s(s-1)},\quad 0<c\le1/2,
 \quad \alpha+\beta=1,\quad\alpha\beta=c.
\]
模型自身Γ=0，完整双pole保留。设
\[
 v_c(u)=e^u+1-e^{\alpha u}-e^{\beta u}=u\,q_c(u)\ge0,
 \quad d\psi_c(u)=v_c(u)du.                              \tag{10}
\]
q_c是562的**全prime-power密度**，不是577的修补q_R；下标区分不可省略。由直接积分，U≥0时
\[
 \Psi_c(e^U)=e^U-1+U-
 \frac{e^{\alpha U}-1}{\alpha}-\frac{e^{\beta U}-1}{\beta}.
 \tag{11}
\]
令\(b_c=\max(\Re\alpha,\Re\beta)<1\)，则
\(\Psi_c(x)=x+O_c((1+\log x)x^{b_c})\)。因此对任意预先固定a>0，该误差也为\(O_{c,a}(x\exp(-a\sqrt{\log x}))\)。这只是固定c的幂节省，不给跨c趋0的统一常数。

ordinary Selberg二阶预算也可精确核算。安全半平面中
\[
 U_c(s)=\int_0^\infty e^{-su}v_c(u)du
 =\frac1{s-1}+\frac1s-\frac1{s-\alpha}-\frac1{s-\beta},
\]
\[
 -U_c'+U_c^2=Z_c''/Z_c
 =\mathcal L\{u v_c+v_c*v_c\}.                           \tag{12}
\]
右边是proper rational函数。在s=1的二阶主部恰为\(2/(s-1)^2\)，其余s=1项至多简单极点；其他极点只在0、α、β，实部<1，阶至多2。对c=1/4，α=β=1/2，二重零点只产生\(\operatorname{poly}(u)e^{u/2}\)，不会改变主项。有限partial fractions／Laplace唯一性给
\[
 \int_0^{\log x}[u v_c(u)+(v_c*v_c)(u)]du
       =2x\log x+O_c(x).                                \tag{13}
\]
这里\(u v_c\ge0\)、\(v_c*v_c\ge0\)；没有把和频平方改成Hermitian平方。因α、β非零，(11)在重根处字面也成立。

但完整Weil源为
\[
 W_c(u)=\begin{cases}2\cos(\sqrt{c-1/4}\,u),&c\ge1/4,\\
                     2\cosh(\sqrt{1/4-c}\,u),&c<1/4.
       \end{cases}                                      \tag{14}
\]
正段\(\phi_RW_c\)正型，hard修补为0。反段对既有实际compact双pole-zero源r_-有\(Q_{W_c}(r_-)<0\)，故任意正修补必须\(\liminf Q_{K_R}(r_-)\ge-Q_{W_c}(r_-)>0\)。它不能D′消失，且按原du／fixed窗Dlog有实际费用下限。

因此**正primitive、正integer、exact completion／对偶、双pole、有效PNT误差及ordinary Selberg的O(x)主预算**并不能在这一般类中决定完整Weil符号。该观察是旧562族的直接计算／准入反测，不是排除所有联合Selberg方法的新完整边界。Γ=0是该模型原规范，不能冒称它具有经典Γ；经典独有的额外signed输入仍可能避开此反测。

## 6. 真函数域：全部returns／aliases上平方来自哪一层

真曲线C/F_q保原\(\ell=\log q\)、全部点数N_n、归一化\(a_n=q^{-n/2}(q^n+1-N_n)\)、a_0=2g及所有周期极点，完整源是
\[
 W_C=\ell\sum_{n\in\mathbb Z}a_n\delta_{n\ell}.          \tag{15}
\]
567从同一C×C的RR／Hodge index给primitive对应E_n的\(-E_mE_n=a_{n-m}\)全Gram；563从实际点数递推给U,H>0及\(U^*HU=H\)。这些是独立几何正号，不是closed-place数的非负性或(5)。因此对全部complex compact源，完整all-alias源的平方和为
\[
 Q_{W_C}(r)=\ell\int_0^\ell
 \left\|\sum_jr(y+j\ell)E_{j+j_0}\right\|^2dy\ge0.
 \tag{16}
\]
支撑只令本源有限求和，不删掉(15)的returns／aliases。正型窗乘积\(\phi_RW_C\)仍正，native hard修补为0；这里nativeΓ／contact按函数域本身保留，不能插入经典Γ来改目标。

函数域的ordinary正Euler／(5)仍在其实际绝对收敛域成立，但预算必须保native周期：\(H^0,H^2\)给s=0、1及\(2\pi i k/\ell\)的**全部**极点副本，\(H^1\)给所有cohomological returns。\(\Psi_C(x)\)在\(x=q^m\)处跳跃，主项有log-periodic轮廓；不能要求它逐实x满足连续模型字面的\(\Psi=x+o(x)\)或Selberg \(2x\log x+O(x)\)，否则会误排真正正例。(15)–(16)使用完整系数／周期identity检验，没有把一个fundamental strip当完整Weil源。

旧290／567的q=5、g=1、N_1=1有全次数正整数primitive Euler、精确FE、全递推，但primitive Gram行列式−5；它再次说明仅closed-place Euler平方不是(16)。本稿没有重新证明290全部次数性，只消费567及其既有引用范围。真实曲线的有效性／RR是对这项缺失的同对象输入；只重命名(16)或为经典预设同样H，仍未付款。

## 7. 405／537、原du／Dlog及停止范围

以上候选并未改变577的实际层，故405非compact全主关系、537和原费必须按原范围保留：

* \(p=(D^2-1/4)H_0\)及其全部平移在\(\mathcal S_{\exp}\)，完整\(B_\zeta(p,s)=0\)。每层\((g_R)_+\)高频严格正，故\(Q_{\widetilde V_R}(p)>0\)，不能exact下降405商。正Euler／Toeplitz并未提供新的实际商映射。固定强源裸误差O(R⁻²)已由577的指数加权尾计费；加修补的费用仍含c_R或m_R。
* 537原L_0=17/16固定窗全complex非根由\(Q_{\widetilde V_R}\ge(\tau-D_{L_0}/R^2)\|r\|_2^2\)无条件最终保留；本分支没有扩大该窗或把它变成全线容量。
* fixed源窗[-L,L]全部原du／zero-extension Dlog的实际误差仍为\([D_L/R^2+\min(c_R,2Lm_R)]\|r\|_2^2\)，\(D_L\ll(1+L^2)e^L\)。Γ协同L¹／Fourier-L¹的R⁻²已独立付清，但不是prime／pole修补小量。成长时必须同时支付D_L/R²和实际修补费用；D′只给逐compact测试，不能冒充全线Hlog统一小费。553的主关系稠密性障碍不因Euler平方消失。

本分支净结论：已给具体候选的准确系数方向、和频／差频区别及连续族的同源便宜反测。没有新经典independent signed estimate、q_R消失、原norm改善、whole/core／coupling／Ξ后果。对(2)–(9)以及仅ordinary Selberg O(x)的入口在此停止；不自动续频窗、二阶矩或把\(\int q_R\)改名容量。合法未排的是有新同源Γ／pole身份、实际signed相关节省与完整尾费的联合论证，或真正同对象source→sections／RR容量。任何重准入应先写出其比577旧等价多支付的那一步。
