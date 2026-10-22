# KRY有限位／relative边界联合源：实际非标量门与无限level原域

2026-10-23；独立分支，供root消费，不改STATE／cadence。恢复Goal、STATE、579、405与C042后执行本次指定候选。本文构造两个及有限多个**实际有限Schwartz因子**协同变化的源，并核原du费用、405全平移关系和537非根；另核全level Hilbert完成。没有以完整Q或未知零点选择系数，没有构造成功的相对primitive循环或独立平方RR容量。

唯一外部原件为[Kudla–Rapoport–Yang1999](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)：§1(1.4)接受restricted tensor Schwartz输入；§2在各有限位取1_{O_{k,p}}、无穷位取weight1 Gaussian。以下主要是这些实际空间上的新候选计算；一般变化finite数据的算术循环／Green身份不得由fixed原件定理免费延出。外部事实的使用仅限这两个输入接口。

## 1. 一个不经单一c(r)的实际有限位源

保持579的k=Q(√−7)、φ*／Q／字符／自对偶Haar，ν=||φ*||²。令p=2，p位V_p=k⊗Q_p为二维Q_p空间，O=O_{k,p}。这里p不整除判别式，Haar取vol O=1。其他有限位因子固定，记其总平方范数ν_f>0；把它作为固定常数保留。

取两个真实局部Schwartz向量

\[
 e_0=1_O,\qquad e_1=p1_{pO},\qquad
 \langle e_i,e_i\rangle=1,\quad
 \langle e_0,e_1\rangle=p^{-1}=:\rho.                    \tag{1}
\]

1_{pO}是实际紧开lattice的indicator；系数p只是Hilbert归一化，不改变其实际有限位身份，也不使后面的实／复系数成为整循环。取a=2log p，s(u)=sech(u/2)，定义

\[
 c_j(r)=\int r(u)s(u-a_j)du,\qquad a_0=0,\ a_1=a,
 \quad V_2(r)=c_0(r)e_0+c_1(r)e_1.                       \tag{2}
\]

其来源不是任意probe标签：先取

\[
 \mathcal T_2r=e_0\otimes T_*r+e_1\otimes D_{-a}T_*r,
 \qquad T_*r=\int r(u)D_u\phi_*du,                       \tag{3}
\]

再对每一arch分支作同一个native weight1投影。579的Gaussian内积严格给

\[
 (1\otimes P_1)\mathcal T_2r=V_2(r)\otimes\phi_* .      \tag{4}
\]

所有compact smooth或全S_exp,C源均真实进入restricted Schwartz，再进入λ_C。源只依赖r、两个局部lattice及预先固定的a；没有Q或零点标签。a=2logp与二维变量x→px的dilation尺度相符；本计算不要求把这种尺度吻合宣布为算术principal同构。

[实际循环分支](finite-schwartz-and-actual-cycles.md)独立核了unnormalized ψ_j=1_{2^jO}的完整输出φ_j(τ)=φ_0(4^jτ)、positive cycles、负指标Green及constant degree的−2jh_k log2修正。它采用的具体两通道源是c_0ψ_A+c_aψ_1，ψ_A=ψ_0−ψ_1；本文(2)是c_0ψ_0+pc_aψ_1。两者是不同、均实际的finite源，不能把各自精确norm公式互换；但它们的coefficient-space都由同一(c_0,c_a)经可逆固定矩阵给出，故下文全Pan-span及finite非根核对该实际cycle源同样适用。消费循环公式须连同该分支原件前件，不能由本文的Schwartz计算单独领取。

该源不是579的rank1 c(r)模型：s(u)和s(u−a)线性独立，因此r↦(c_0,c_1)满射C²。对同一个r，两个finite分支实际可独立变化。

## 2. 原du／Dlog费用及全部mixed项

\[
 \int s(u)^2du=4,\quad
 J(a):=\int s(u)s(u-a)du=\frac{2a}{\sinh(a/2)},\quad0<J(a)<4.
                                                               \tag{5}
\]

故原du上(4)的实际平方范数为

\[
 \|V_2(r)\otimes\phi_*\|^2
 =\nu\nu_f\bigl(|c_0|^2+|c_1|^2
                    +2\rho\Re(c_0\overline{c_1})\bigr). \tag{6}
\]

没有丢mixed项。两个2×2 Gram同时由(1,±1)对角化，给**精确operator平方范数**

\[
 \|V_2\otimes\phi_*\|_{L^2(du)\to L^2(\mathbb A)}^2
   =\nu\nu_f(1+\rho)(4+J(a))
   \le8\nu\nu_f(1+\rho).                               \tag{7}
\]

这是全线原du费用；原zero-extension Dlog控制du，也付该费。它不是height／Green／determinant line的费用，更不是完整Γ的log|t|二次预算。raw(3)可直接由579的T*界及有限Gram付原du上界；Schwartz半范数仍依fixed支撑窗与导数，不升级成长统一。

## 3. 405全orbit在非标量系数空间中已经张满

405实际正H∈S_exp和p_an=(D²−1/4)H非零；H>0，所有τ_b p_an仍为真实关系。为免与素数p混淆，下文记其为P。令k_j(u)=s(u−a_j)。合法分部积分给

\[
 c_j(\tau_bP)
 =-\frac12\int H(v)s(v+b-a_j)^3dv<0
 \quad(j=0,1;\ b\in\mathbb R).                         \tag{8}
\]

单个平移两分量皆负已经说明直接positive norm不消关系，但联合边界可能使用signed组合；不能仅凭这两个负号排除它。应检验整个orbit：

**有限orbit张满命题。** 对任意互异a_1,…,a_N，置
V_N(r)=(∫r(u)s(u−a_j)du)_j。则

\[
 \operatorname{span}_{\mathbb C}
       \{V_N(\tau_bP):b\in\mathbb R\}=\mathbb C^N.      \tag{9}
\]

证明：若线性泛函ℓ=(ℓ_j)消全部这些向量，对b作Fourier变换得到（反射／相位约定只改共轭）

\[
 \widehat P(\pm t)\,2\pi\operatorname{sech}(\pi t)
                 \sum_j\ell_j e^{ita_j}=0.             \tag{10}
\]

P̂(0)=−(1/4)∫H<0，故某个实开区间P̂非零。sech乘子处处非零；有限指数多项式于该开区间为零，解析唯一性及不同指数的线性独立迫ℓ_j全零。由有限维对偶得(9)。该证明使用实际完整noncompact关系，未将其裁成compact，也未假设任何ζ零点位置。

**固定relative复形推论。** 设这些N个实际finite／arch分支进入同一个固定线性相对复形，或同一个线性cycle／Arakelov群的复化；令Π为取同调、relative类、degree-zero或primitive类的固定线性读出。若

\[
 \Pi V_N(\tau_bP)=0\quad\forall b,
\]

则Π在这个全部N维family上为零。边界补偿B(r)即使依赖源，只要边界算子∂及最终quotient固定，关系条件仍是同一ΠV_N=0，(9)适用；无须假设B有界或目标Hausdorff。只对实线性读出时同时检P与iP可得同样结论。

这不排除随源变化的实际载体／边界算子、非线性cycles、strong非有界的无限family或新的全位coupling。也没有声称“有限Schwartz数据永不可能”：本命题严格针对(2)及N个不同shifted-sech native系数经固定线性相对操作的recipe。

## 4. 真实lattice inclusion与手添level edge不是同一件事

最便宜的实际解析relative pair是紧开嵌入pO⊂O的extension by zero：

\[
 \partial:\mathcal S(pO)\hookrightarrow\mathcal S(O),
 \quad H_1=0,\quad H_0=\mathcal S(O)/\mathcal S(pO).
                                                               \tag{11}
\]

在span{e_0,e_1}上，e_1是boundary，而[e_0]≠0。因此(2)进入此relative商后仍为c_0(r)[e_0]；它退回579，不能以第二分量抵消(8)。实际shell 1_O−1_{pO}在(11)中非零，不能直接改称principal边界。

若手添一条edge，规定∂b=e_0−e_1，则已选择**不同**的复形，而非(11)的lattice inclusion。即使暂许这条额外edge，最终固定线性quotient仍受(9)约束：消所有真实Pan的最终family必为0。对算术cycles的真正isogeny／pullback／pushforward关系，必须另给同对象的principal identity及完整arch项；函数的lattice包含本身没有提供它。

这里(11)是明确的Schwartz相对复形；没有未经证明把它等同KRY的算术relative divisor边界。该类型区别正是尚缺的实际比较之一。

## 5. 同时核537：有限family有数据给出的非根核

有限rank源另有不依赖Π的coverage失效。令I⊂(−17/16,17/16)为任意非空开区间。取N+1个互不相交的非零bumps ψ_ℓ∈C_c∞(I)。解已知有限线性系统

\[
 \sum_{\ell=1}^{N+1}x_\ell
       \int\psi_\ell(u)s(u-a_j)^3du=0\quad(1\le j\le N).
                                                               \tag{12}
\]

它有非零解x，不读Q或零点。ψ=Σx_ℓψ_ℓ非零，r_*=(D²−1/4)ψ非零、compact且两个pole矩精确为0。分部积分给全部c_j(r_*)=0，而537的完整原型给

\[
 Q_\zeta(r_*)\ge2^{-49162}\|r_*\|_{du}^2>0.             \tag{13}
\]

故任何经此有限family的固定linear cycle、relative quotient或从零对象为零出发的二次height，都不能恢复完整Weil二次型。这个source自身没有被循环地按Q选取；严格正号来自已付537。对N=2，可取3bumps，矩阵两个row的叉积给显式x；两权函数的比值严格单调，适当有序小支撑可保证矩阵rank2。

这不要求全部537源均被杀；相反，(2)保有许多非根。失败是完整源覆盖，不是不存在任何正源像。

## 6. 不把无限levels误判为有限rank：实际Hilbert完成可保compact非根

一个更强候选是所有j∈Z的真实有限位向量

\[
 e_j=p^j1_{p^jO},\quad a=2\log p,\quad
 c_j(r)=\int r(u)s(u-ja)du,\quad
 \Phi_\infty(r)=\sum_{j\in\mathbb Z}c_j(r)e_j\otimes\phi_*.
                                                               \tag{14}
\]

e_j均为实际Bruhat-Schwartz，Gram为ρ^{|j−k|}。Poisson核的Fourier symbol给全部finitely supported z的真实mixed双边界预算

\[
 \frac{1-\rho}{1+\rho}\sum|z_j|^2
 \le\Big\|\sum z_je_j\Big\|^2
 \le\frac{1+\rho}{1-\rho}\sum|z_j|^2.                  \tag{15}
\]

所以ℓ²系数完成是L²(V_p)的一个闭子空间；非正交levels没有被误当orthogonal。sech translates的Gram为J((j−k)a)，且

\[
 C_a=4+2\sum_{m\ge1}J(ma)
    =4+4a\sum_{m\ge1}\frac{m}{\sinh(ma/2)}<\infty.
\]

因此

\[
 \sum_j|c_j(r)|^2\le C_a\|r\|_{du}^2,\quad
 \|\Phi_\infty(r)\|^2\le
 \nu\nu_f\frac{1+\rho}{1-\rho}C_a\|r\|_{du}^2.          \tag{16}
\]

这条全线原du/Dlog费用是真合法，不得以“无限level所以费用必无穷”否定它。Hilbert级别的(14)还在全部compact源上注入：下一节的moment证明说明若所有正j系数为0则r=0。因此每个537非零compact源在此完成中确实保留，不能把有限N的(12)直接扩成无限family结论。

仅保j≥0的半塔也有(15)–(16)，而且已足够下节的原域障碍；这使所有有限截断都可使用实际循环分支已核的j≥0身份。本文全j的负level只用于明确analytic Hilbert域与费用，不免费宣称原件已有其整循环／Green延拓。

## 7. 精确原域损失：任何非零compact源的(14)都不是Bruhat-Schwartz

取supp r⊂[−L,L]，z_j=e^{-ja}。对ja>L，有一致绝对收敛的实际公式

\[
 c_j(r)=2z_j^{1/2}F_r(z_j),\qquad
 F_r(z)=\int r(u)\frac{e^{u/2}}{1+ze^u}\,du
       =\sum_{m\ge0}(-z)^m\int r(u)e^{(m+1/2)u}du.
                                                               \tag{17}
\]

F_r在|z|<e^{-L}解析。如果c_j最终为0，z_j→0是其零点的内部聚点，故F_r≡0。令t=e^u，全部moments等于紧区间[e^{-L},e^L]上的复测度r(logt)t^{-1/2}dt的多项式矩；多项式稠密迫r=0。

另一方面，(14)在p位的径向值，在annulus x∈p^nO\p^{n+1}O上等于

\[
 F_n=\sum_{j\le n}p^jc_j(r).                             \tag{18}
\]

j→−∞一端由Cauchy–Schwarz及Σp^{2j}<∞绝对可付。若它是Bruhat-Schwartz，必在0的某个邻域locally constant；(18)遂对全部n≥N为常数，故p^{n+1}c_{n+1}=F_{n+1}−F_n=0。由(17)只能r=0。

**所以每个非零compact physical r的(14)均在合法L²完成中，却不在原restricted Schwartz空间中。** 这是实际源像的domain结论；不是用全空间逆norm下界替代actual费用。双pole-zero只消去(17)的m=0及负j对称端的首项；不使所有高矩为0，因而不修这个原域损失。

同样证明适用j≥0半塔：此时(18)从j=0求和、n<0的值为0；locally constant at0仍迫c_j最终0。所以即便不使用任何负level，也不能把compact输入的无限塔直接当作Schwartz循环输入。本文只报compact域注入；全S_exp的离散sampling可能有alias盲源，不能从compact moment论证外推全S_exp注入。新增实际连续边界若不经这些c_j或双pole data，也未被本障碍排除。

有限level截断Φ_N都合法，并按(16)在L²中趋Φ∞；但该收敛没有把λ_C的point0读出、Eisenstein standard extension／导数、Green或循环类自动延到极限。须给实际完成域与同一regulator的延拓、全部finite／arch／constant尾费。若直接定义一个unbounded form以使其pullback等于Q，这只是目标重新包装，尚非独立容量。

保留的逃逸是真正strong／unbounded relative几何或新的完成定理；本节没有排除它。

## 8. Locally finite source cells也不能静默修回全S_exp

可另取预定smooth partition η_j(u)=η(u−ja)、有限重叠M，定义
\(d_j(r)=\int r(u)η_j(u)s(u-ja)du\)。compact r只激活有限j，故Σd_je_j为实际finite Schwartz；全du费由

\[
 \sum|d_j(r)|^2\le M\Big(\int|η(v)s(v)|^2dv\Big)\|r\|^2
                                                               \tag{19}
\]

及(15)支付。可是405真实Pan非compact，通常激活无穷levels，仍需完成；不能只把compact源域当全主关系域。

此外，任一fixed537子窗只激活有限个cell系数；用该窗内足够多bumps解对应有限齐次系统，同时用r=(D²−1/4)ψ保双pole-zero，又产生非零537源落入所有d_j的核。因此这个局部有限修补保actual compact Schwartz，却重新丢完整非根覆盖。

若只用抽象level incidence ∂b_j=e_j−e_{j+1}，finite-support quotient至多读Σd_j；在ℓ²完成中closure im∂为全部ℓ²（其adjoint核要求constant∈ℓ²，只能0）。由此得到的Hausdorff quotient全零，不能成为独立primitive carrier。这里明确是该抽象incidence的结论，不声称它已是实际CM principal边界。

## 9. 与完整预算及continuous／函数域控制的关系

本计算没有截去经典目标的完整Γ／FP-contact、全部素数幂或两个pole。源的双pole-zero仅用于明确反测，目标pole预算仍保留。KRY native完整Mellin identity仍含Λ₀Λχ及两对数导数之差；变化finite向量只改变实际local sections，不能由(4)、(14)自动剥掉Λχ、完成Γ或有符号Euler逆。

对连续正反族，(2)与(14)的Gaussian／finite Hilbert Gram完全不读其native prime分布，所以同样为正；这不能识别其native完整Weil型相反的符号。有限family另有紧窗大核，与正连续型在紧窗上的二次读出缺失可直接核；没有建立continuous→CM的算术运输，故不称其反驳KRY定理。

真函数域的源是同一C×C上的完整Frobenius对应及其双degree primitive化；mixed交数和RR／Rosati正号来自该同一对象。finite level inclusion、Hilbert Gram或CM generic-dim0的线性degree均未提供这条二次比较。全base change／returns／aliases与H⁰/H²的pole角色必须一起保；本稿没有一条新的FF→CM transport。

## 10. Root消费边界与真正缺件

新可消费的具体门限是：(2)–(7)的实际两finite-branch非标量接口与原norm；(9)的全Pan orbit张满导致fixedrelative修复失败；(12)–(13)的537数据核；(14)–(18)的合法无限Hilbert完成／compact注入与准确Schwartz原域损失。无截断近似误差被藏在结论中。

扣除579 scalar门、405原关系、537固定窗、553全线bounded读出密度及旧有限Euler有符号费用；本稿没有新的经典Weil正性或同对象平方RR容量，也不改善542+555→557 whole4/5负惯性上预算。可用独立线性代数与Gaussian／局部Haar直接复核上述门。

下一真正交件须是：不经此有限native coefficient-space的实际全位cycle／relative boundary公式；若用(14)类完成，先给λ／循环／Green同域延拓和actual源尾费；再给405全主同构、537 coverage与原du/Dlog；最后是同对象的signed解卷积及primitive mixed二次容量。直接把Pan系数像定义为boundary、把Hilbert正Gram改称height、或把Q拉回到新完成上，均只包装旧源商／目标型。

本分支不继续调level数、cell宽或Gaussian参数；上述fixed有限recipe停止，实际强拓扑／非线性载体／新算术边界和有费完成定理保留。
