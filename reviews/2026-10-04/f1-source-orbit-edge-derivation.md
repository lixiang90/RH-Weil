# 真源轨道的实际边、交叉Gram与有限矩阵核

2026-10-04。从[414](../../notes/414-f1-deep-boundary-unitary-and-time-defect.md)的原u、c和独立M平方分割 \(d=d_q\)，以及[425](../../notes/425-f1-recentered-geometric-corner-and-source-period-finite-part.md)的实际V，独立推导[429](../../notes/429-f1-original-unitary-crosses-the-fixed-corner-domain.md)之后的源稳定域。本文不改笔记或索引。

可审结论：原 \(u^r\) 有准确有限系数公式；所有 \(V^*u^rV\) 实际为显式光滑乘法函数；其正时间端是有限带Toeplitz加秩一的周期Gram。任意固定有限源指标集的光滑周期有限传播矩阵核有精确本质范数、无迹类表示核；有限支持商上 \(1-\operatorname{Ad}u\) 单射。这构造真实准入并给新非紧耦合，不支付规范周期读出、算术主关系、RR或RH。

## 1. 保留原Hilbert表示的全p等距采样

仍在完整径向波形基中，\(\lambda_a w_j=w_{j+a}\)，物理时间 \(\mathsf T_s\phi(t)=\phi(t-s)\) 不变。置 \(L=\log p,M=\log q\)，\(c,d\ge0\) 光滑紧支且
\[
 \sum_j c(x+jL)^2=1,\qquad \sum_k d(x+kM)^2=1.
\]
定义
\[
 \mathscr S:L^2(\mathbb R_x;\ell^2(\mathbb Z_q))\longrightarrow\mathcal H,
 \qquad(\mathscr S\Phi)_{j,k}(t)=c(t)\Phi_k(t-jL).             \tag{1}
\]
全p平方和给 \(\|\mathscr S\Phi\|^2=\|\Phi\|^2\)，故为实际等距映射。直接换元给
\[
 (\mathscr S^*\Psi)_k(x)=\sum_j c(x+jL)\Psi_{j,k}(x+jL).       \tag{2}
\]
该等式先对有限支输入核验，再由等距性延拓，未把未压缩的形式采样当作有界。

令 \(R=\lambda_{1,q}\otimes\mathsf T_M\)，即 \((R\Phi)_k(x)=\Phi_{k-1}(x-M)\)。将(1)–(2)代回原源的有限系数和，得到
\[
 e=\mathscr S\mathscr S^*,\qquad v=\mathscr S R\mathscr S^*,
 \qquad u=(1-e)+\mathscr S R\mathscr S^*.                    \tag{3}
\]
例如 \(\mathscr S R\mathscr S^*\) 的(j,k)行是
\(\sum_a c(t)c(t-aL-M)\Psi_{j-a,k-1}(t-aL-M)\)，精确等于原v。源角e在全Hilbert空间并非有限秩。

因 \((1-e)\mathscr S=0\)，对每个整数r准确有
\[
 \boxed{u^r=(1-e)+\mathscr S R^r\mathscr S^*
 =1-e+\sum_a M_{c(t)c(t-aL-rM)}P_{(a,r)}.}                  \tag{4}
\]
固定r时末项只有有限个非零a。r=0给单位；负r由伴随成立。故反复源移动不必展开指数增长的字词，(4)已经保留其完整物理时间和径向次数。

## 2. 原V在源角及其补空间的准确分解

去除425共同时间酉因子后，\(A(h)=VU(h)V^*\)。V的p通道、q通道分别为
\[
 (V_p\phi)_{j,k}(t)=\mathbf1_{j<0}\delta_{k0}c(t)\phi(t-jL),
 \qquad(V_q\phi)_{j,k}(t)=\delta_{j0}\mathbf1_{k<0}d(t)\phi(t-kM).
\]
令
\[
 a(x)=\sum_{j<0}c(x+jL)^2,\quad
 b(x)=\sum_{k<0}d(x+kM)^2,\quad f(x)=c(x)d(x).               \tag{5}
\]
\(a,b\in[0,1]\)，充分负端为0、充分正端为1，\(V^*V=M_{a+b}\)。由(2)
\[
 (\mathscr S^*V\phi)_k(x)
 =\delta_{k0}a(x)\phi(x)+\mathbf1_{k<0}f(x)\phi(x-kM).       \tag{6}
\]
记其右边为 \(W\phi=P\phi+Z\phi\)，两项的q支撑正交。再令 \(F=(1-e)V\)，则
\[
 V=F+\mathscr SW,\qquad
 u^rV=F+\mathscr SR^rW.                                    \tag{7}
\]
这也说明源补空间的同一F在所有轨道列中不动，后面的Gram有一个共同秩一来源。

Vp的残余 \((1-e)V_p\) 只在输入变量的紧过渡区出现：其第j行系数为
\(c(t)[\mathbf1_{j<0}-a(t-jL)]\)。\(a-a^2\) 紧支，且t在c的固定紧支内，所以仅有限p行可能非零。Vq的源变换也只有有限p行，因为原 \(V_q\) 位于p=0，(4)只含有限p次数。q负端仍完整保留，不能称这些通道整体有限秩或迹类。

## 3. 每个源幂的深负p边与重复搬移

定义 \(V_r=u^rV\)，并用429的 \(I_n^j\phi=w_{-n,p}\otimes w_{j,q}\otimes\phi\)。对固定r，存在有限 \(N_r\)，使所有 \(n>N_r\) 的完整行准确为
\[
 I_n^{j*}V_r=\begin{cases}
 M_c\mathsf T_{rM-nL},&j=r,\\
 0,&j\ne r.
 \end{cases}                                               \tag{8}
\]
证明：上述有限p残余和Vq贡献取不到深行；源角的p项为
\(\delta_{jr}c(t)a(t+nL-rM)\phi(t+nL-rM)\)，充分大n使a恒为1。于是深行确实移到q=r，没有省略原时间作用。

令
\[
 A_{r,s}(h)=V_rU(h)V_s^*=u^rA(h)u^{-s}.
\]
对充分深n,m，完整行列核为
\[
 I_n^{r*}A_{r,s}(h)I_m^s
 =M_c\mathsf T_{(m-n)L+(r-s)M}U(h)M_c.                     \tag{9}
\]
若输出q次数不是r，或输入q次数不是s，该深块为零。原问题的 \(u^jA(h)u^k\) 对应 \(r=j,s=-k\)，时间位移为 \((m-n)L+(j+k)M\)。429的 \(B_M\) 和 \(B_0\) 正是这些准确块的特殊情形。

因此有限字词只涉及有限条水平负p边和一个有限p宽度的负q条带；但全部源幂需要无限多q水平边。单个有限水平边集合不可能对u、u*保持，因为最外一条会产生(8)中的新非零深边。该结论不排除一个真实无限边域。

## 4. 全部交叉Gram的实际光滑乘法公式

由(7)及正交性
\[
 G_r:=V^*u^rV=F^*F+W^*R^rW.                                \tag{10}
\]
对整数r置
\[
 z_r(x)=\sum_{k<0,\ k-r<0}f(x+kM)f(x+(k-r)M),\qquad
 \nu(x)=a(x)+b(x)-a(x)^2-z_0(x).                            \tag{11}
\]
\(z_{-r}=z_r\) 由移项核验；\(F^*F=M_\nu\)，故 \(\nu\ge0\)。所有和局部有限，函数均光滑有界。实际四项为
\[
\begin{aligned}
 P^*R^rP&=\mathbf1_{r=0}M_{a^2},\\
 P^*R^rZ&=\mathbf1_{r>0}M_{a(x)f(x-rM)},\\
 Z^*R^rP&=\mathbf1_{r<0}M_{a(x)f(x+rM)},\\
 Z^*R^rZ&=M_{z_r}.
\end{aligned}                                               \tag{12}
\]
例如第一交叉项从Z的q=−r行移到0，\(\mathsf T_{rM}\) 与行采样的 \(-rM\) 正好相消，留下 \(a(x)f(x-rM)\)；右交叉项同理。这一相消支付了完整源时间作用，不是先把时间变量评价成常数。

所以
\[
 \boxed{G_r=M_{g_r},\quad
 g_0=a+b,\qquad
 g_r=\nu+z_r+a(x)f(x-|r|M)\quad(r\ne0).}                   \tag{13}
\]
原 \(c,d\) 非负且 \(\nu\ge0\)，因此所有 \(g_{-r}=g_r\ge0\)。非零r时它不必为常数，有限Gram矩阵总为正半定。

这是反复源乘积的实际控制：
\[
 A_{i,j}(h)A_{k,l}(k_0)
 =V_iU(h)M_{g_{k-j}}U(k_0)V_l^*.                           \tag{14}
\]
一般中间项不是常数2；只有相同中间源指标的右端密度为2。

## 5. 正端的周期Toeplitz与有限矩阵严格下界

定义全整数周期自相关
\[
 z_r^{\rm per}(x)=\sum_{k\in\mathbb Z}f(x+kM)f(x+(k-r)M),
 \qquad w(x)=1-z_0^{\rm per}(x).                            \tag{15}
\]
\(c^2\le1\)，故 \(0\le z_0^{\rm per}\le\sum_kd(x+kM)^2=1\)，\(w\ge0\)。这些函数M周期，\(z_{-r}^{\rm per}=z_r^{\rm per}\)。若 \(|r|M\) 大于f支集直径，则 \(z_r^{\rm per}=0\)；有限带宽只取决于原紧支。

对每个固定r，充分正的x使(11)的半轴约束全不影响非零项，并使(13)交叉项为零。于是
\[
 g_r(x)=\gamma_r(x)\quad(x\gg0),\qquad
 \boxed{\gamma_r=\delta_{r0}+w+z_r^{\rm per}.}              \tag{16}
\]
\(\gamma_0=2\)。取固定有限 \(J\subset\mathbb Z\)，令
\[
 X_J=(V_j)_{j\in J},\quad
 \Gamma_J(x)=[g_{k-j}(x)]_{j,k\in J},\quad
 \Gamma_J^+(x)=[\gamma_{k-j}(x)]_{j,k\in J}.                 \tag{17}
\]
准确有 \(X_J^*X_J=M_{\Gamma_J}\)。共同右阈值使 \(\Gamma_J=\Gamma_J^+\)；共同左阈值使 \(X_J=X_J\mathbf1_{[a_*,\infty)}\)。

令 \(P_x(\theta)=\sum_k f(x+kM)e^{ik\theta}\)，为有限Laurent和。\(z_r^{\rm per}\) 为 \(|P_x|^2\) 的Fourier系数，故对任意有限向量α
\[
 \alpha^*\Gamma_J^+(x)\alpha
 =\sum_j|\alpha_j|^2+w(x)\left|\sum_j\alpha_j\right|^2
 +\frac1{2\pi}\int_0^{2\pi}|P_x(\theta)|^2
                   \left|\sum_j\alpha_je^{ij\theta}\right|^2d\theta
 \ge\|\alpha\|^2.                                         \tag{18}
\]
因此 \(I\le\Gamma_J^+\le2|J|I\)。其正平方根和逆平方根光滑M周期、均有界。这是真实有限矩阵控制：单位矩阵来自独立深p边，\(w\mathbf1\mathbf1^*\) 来自源补空间不动部分，有限带Toeplitz项来自q通道的源角自相关。

**不能把它升级成默认有界的无限 \(\ell^2\) Gram。** 若w非零，选相同分量的长有限向量即可使Gram范数随 \(|J|\) 增长；常值的矩阵项 \(w\mathbf1\mathbf1^*\) 一般不定义有界无限矩阵。本文只使用每个有限J的正性和范数，不使用标准 \(M_\infty\) 算子范数。

## 6. 可控的实际周期有限传播核域

取矩阵核 \(B(x,y)\in C^\infty(\mathbb R^2;M_J)\)，满足
\[
 B(x+M,y+M)=B(x,y),\qquad
 B(x,y)=0\quad\text{若 }|x-y|>H_B                            \tag{19}
\]
对某有限 \(H_B\)。周期性及有限传播使核和全部导数在基本带上有界，Schur估计给实际有界算子 \(B\) 于 \(L^2(\mathbb R;\mathbb C^J)\)。核乘积和伴随保持(19)和光滑性。卷积测试 \(U(h)\)、其矩阵放置、以及插入光滑周期 \(\gamma_r\) 的有限字词都属此域。

光滑紧支乘法χ若放在B任一侧，\(M_\chi B\) 或 \(BM_\chi\) 的核两变量均光滑紧支，故为真实迹类。若再乘不光滑但有界的有限区间投影，仍由理想性为迹类。这是下节所有边界修正的准入，不是只靠紧支乘法本身称迹类。

定义实际有限矩阵算子
\[
 F_B=X_J B X_J^*=\sum_{i,j\in J}u^i V B_{ij}V^*u^{-j}.       \tag{20}
\]
所有因子有界，有限和准确。产品中间真实Gram为 \(\Gamma_J\)。因为它在充分正端等于 \(\Gamma_J^+\)，而输入经 \(X_J^*\) 支撑于 \([a_*,\infty)\)，再经有限传播C只扩展有限距离，可用光滑左截断把 \(\Gamma_J-\Gamma_J^+\) 换成真正紧支矩阵函数f。\(BM_f\) 光滑紧支核迹类，所以
\[
 \boxed{F_BF_C-F_{B M_{\Gamma_J^+}C}\in\mathcal S_1.}        \tag{21}
\]
同理可在不同有限指标集之间先填零到共同有限集合，乘积的每个中间系数准确为 \(\gamma_{k-j}\)。单字母匹配指标退化为427的 \(2h*k\)；不匹配时必须携带周期系数。

所有有限J、(19)的矩阵核及 \(\mathcal S_1\) 的并集因此给一个实际非单位化星代数。左右乘u、u*只平移外侧源指标，保持这个并集。这里允许明确定义的周期核扩域；没有称它为由原A族生成的最小理想或最小C*代数。

## 7. 有限矩阵精确本质范数

**定理。** 对固定有限J及(19)中的B，
\[
 \boxed{\|F_B\|_{\rm ess}
 =\|M_{(\Gamma_J^+)^{1/2}}B M_{(\Gamma_J^+)^{1/2}}\|.}       \tag{22}
\]
右边是 \(L^2(\mathbb R;\mathbb C^J)\) 上的实际有界算子范数，不是逐点矩阵核范数或标准无限矩阵范数。

证明上界：取R使 \(\Gamma_J=\Gamma_J^+\) 于 \([R,\infty)\)，令 \(P_R=\mathbf1_{[R,\infty)}\)。由于 \(X_J\) 的输入左支集固定，\((1-P_R)X_J^*\) 和 \(X_J(1-P_R)\) 的相关输入仅在有限区间。按第6节的局部迹类核准入，
\[
 F_B-X_JP_RBP_RX_J^*\in\mathcal S_1.
\]
令 \(Y=X_JM_{(\Gamma_J^+)^{-1/2}}P_R\)，则 \(Y^*Y=P_R\)。置 \(D=M_{(\Gamma_J^+)^{1/2}}BM_{(\Gamma_J^+)^{1/2}}\)，有
\[
 X_JP_RBP_RX_J^*=Y(P_RDP_R)Y^*,\qquad
 \|F_B\|_{\rm ess}\le\|D\|.                                \tag{23}
\]

证明下界：固定单位紧支光滑矩阵向量ψ，取 \(\psi_n=\mathsf T_{nM}\psi\)。D对 \(\mathsf T_M\) 平移不变，且有限传播，故 \(D\psi_n=\mathsf T_{nM}D\psi\) 也紧支。n充分大时一切支集都落在共同右端，令
\[
 \eta_n=X_JM_{(\Gamma_J^+)^{-1/2}}\psi_n.
\]
\(\|\eta_n\|=1\)，且弱趋零。真实Gram在这些支集上就是 \(\Gamma_J^+\)，于是
\[
 \|F_B\eta_n\|
 =\|X_J B M_{(\Gamma_J^+)^{1/2}}\psi_n\|
 =\|D\psi_n\|=\|D\psi\|.                                  \tag{24}
\]
紧算子在η列上范数趋零，取所有单位紧支光滑ψ的上确界给下界 \(\|F_B\|_{\rm ess}\ge\|D\|\)。完成证明。

J为单点、B=U(h)时 \(\Gamma_J^+=2\)，(22)回到428的 \(2\|\widehat h\|_\infty\)。一般B不必平移不变于所有实数，只需本定理的M周期和有限传播。

## 8. 线性表示无核、商乘法及有限轨道独立性

因为 \(\Gamma_J^+\ge I\)，(22)给
\[
 F_B\text{紧}\Longleftrightarrow B=0,
 \qquad F_B\in\mathcal S_1\Longleftrightarrow B=0.            \tag{25}
\]
所以固定同一有限J，\(F_B+S=0\) 强制 \(B=0,S=0\)。特别线性表示核为零；任意两种有限表达先填零到共同J，再用(25)可知每个矩阵项相同，普通迹类余项也相同。这个唯一性只指本报告的实际周期有限传播核表示，不扩至任意有界中间B。

在有限矩阵商中准确乘法为
\[
 B\star C=B M_{\Gamma_J^+}C.                                \tag{26}
\]
归一化符号 \(D_B=(\Gamma_J^+)^{1/2}B(\Gamma_J^+)^{1/2}\) 使其变成普通有界矩阵算子的乘法，(22)给忠实本质范数表示。这里没有断言该像等于某个未经证明的全部矩阵C*代数。

尤其 \(\sum_{i,j}u^iA(h_{ij})u^{-j}\in\mathcal S_1\) 强制所有 \(h_{ij}=0\)，因为矩阵核 \(B_{ij}=U(h_{ij})\) 在共同有限J中唯一，而卷积测试单射。因此非零h的有限共轭轨道 \(u^jA(h)u^{-j}\) 在迹类商中线性独立。

## 9. 真源共轭差在有限支持商上单射

源共轭的实际作用是
\[
 uF_{i,j}(B)u^*=F_{i+1,j+1}(B),                              \tag{27}
\]
中间时间核B不变。设一个有限支持矩阵B在商上被共轭固定，先将B与移位B填零到共同有限J；(25)强制每项满足 \(B_{ij}=B_{i-1,j-1}\)。沿每条对角继续移动最终离开有限支持，故所有项为零。

所以在这个**代数有限支持域**的迹类商上，\(\delta=1-\operatorname{Ad}u\) 是单射线性映射。更强地，对任意F在该域中而 \(F\notin\mathcal S_1\)，
\[
                         F-uFu^*\text{非紧}.                \tag{28}
\]
差矩阵非零，由(22)其本质范数严格正。这个结论准确扩展了429的单测试非紧见证；不说明任何规范读出必须取何值。

**不推广到算子范数完成中的无限支持固定点。** 无限Gram一般无统一 \(\ell^2\) 有界性，有限支持平移论证也不适用于无限矩阵。源稳定域的C*完成若研究不变元素，必须另证。

## 10. 新耦合与限制范围的两个明确例子

周期系数确可能非恒定，不能只用标量卷积和一个固定有限维矩阵补偿。合法反例：取 \(p<q\)，故 \(L<M\)。选宽度严格介于L、M的非负光滑紧支φ，其L平移正集覆盖R；用原414的平方和归一化得到c，仍有 \(\operatorname{diam}\operatorname{supp}c<M\)。再选合法M平方分割d，使 \(f=cd\ne0\)。则 \(f\) 的支集直径小于M，所有 \(z_r^{\rm per}=0\ (r\ne0)\)，而 \(z_0^{\rm per}\) 非零且有开区间为0，故不是常数。于是每个 \(r\ne0\) 的
\[
                         \gamma_r=1-z_0^{\rm per}
\]
非恒定。这个例子是在原允许的光滑分割族内构造，不把实际指定c、d偷偷换掉；对指定分割是否非恒定，应直接检查(15)。

若某个 \(\gamma_r\) 非恒定，取紧支光滑近似单位 \(h_\varepsilon,k_\varepsilon\)。\(U(h_\varepsilon)M_{\gamma_r}U(k_\varepsilon)\) 强趋 \(M_{\gamma_r}\)，后者不与某个实平移交换，所以至少一个合法ε的中间算子B不是纯卷积。它仍M周期、光滑、有限传播。若试图用任意纯卷积 \(U(g)\) 在同一外侧源指标下代替它，则 \(B-U(g)\ne0\)，(22)使相应角算子差非紧，不能用迹类余项隐藏新耦合。

第二个例子说明(22)的周期性限制确实有意义：取非零 \(\beta\in C_c^\infty\) 支撑于右端，令 \(B=|\beta\rangle\langle\beta|\)。它光滑有限传播但不M周期，\(F_B\) 是非零秩一迹类，故本质范数为0；而 \((\Gamma_J^+)^{1/2}B(\Gamma_J^+)^{1/2}\ne0\)。因此不能把本定理扩写成任意光滑紧支或任意有界B的无核公式。

同样，紧支乘法本身没有时间平滑，不能自动迹类；第6–7节的边界准入依赖光滑二维核和有限传播。原周期权重 \(\rho_p,\rho_q\) 也未由这些符号自动选出：波形换基后边模型暂时消去这些参数，而原Haar球截止仍是其来源。

本报告完成的是原真源的实际稳定边域输入、有限矩阵核与有限支持非紧障碍。相对余圈、原物理截止的规范传递、读出分类及其与算术主消失的配对仍需继续研究；RR、Weil正性和RH仍开放。

绑定基础版本：425 SHA256 `fe933bbb822bcc47df25511a700744ee222576012e4dc46a1f10d229d9b6afdd`；429 SHA256 `2b6caea39f3229205207694e9ed1acb514abbe7165c65f24aff981c135e39fc9`。本报告为解析推导，不宣称旧有限有理审计已经认证无限域或本质范数。
