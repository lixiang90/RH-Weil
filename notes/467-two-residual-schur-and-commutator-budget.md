# 467：两平方残差的严格 Schur 预算与整个22交换子

2026-10-07。原Eisenstein / AF路线。新有限推导，待另一作者全文独审。
本稿把已付low4、整个13和原加权二矩放进同一个真实Gram约束。
另给一个尚未支付的联合算术条件；没有新的实际零点比例或无零边界。

## 1. 同一原矩阵及引用范围

沿用[465](465-centered-high-square-joint-fourth-budget.md)的原
\(X=T/(2\pi),\mathcal L=\log X,d=\lfloor X\mathcal L\rfloor\)、
interval carrier \(E\)、\(P=EE^*\)、\(Q=1-P\)、原even taper、
sharp prime coefficients、normalizer和全部实高度。
矩阵\(H=C_H,L=C_L\)都是原同维Hermitian有限矩阵；
high为\(\sqrt X<p\le X\)，low为\(p\le\sqrt X\)。
不改变原所有内部P、labels和signs。

定义原high/low同素数乘法diagonal
\[
 w_{\mathcal L}=d_{H,\mathcal L},\qquad
 v_{\mathcal L}=d_{L,\mathcal L},\qquad
 W=E^*M_wE,\quad V=E^*M_vE .
 \tag{1}
\]
它们均非负、uniformly bounded；原derivative L1界和圆周泄漏
与465的\(W\)完全相同。
用465(2)的profile记
\[
 S_H=\int d_{H,\psi}^2,\quad S_L=\int d_{L,\psi}^2,\quad
 C=\int d_{H,\psi}d_{L,\psi},\quad
 e_\psi=\mathcal C_L(\psi),\quad \delta_\psi=e_\psi-S_L .
 \tag{2}
\]
下面的非退化渐近Schur结论要求\(\delta_\psi>0\)；
flat情形将准确给\(\delta_\psi=1/20\)。

输入为[454](454-original-background-and-weighted-prime-mixed-traces.md)原
全log-range weighted二矩、[462](462-original-low-prime-fourth-path-constant.md)
完整low4及[461](461-original-one-high-three-low-fourth-trace.md)的
\(\eta_T=\operatorname{Tr}HL^3/d=o(1)\)。
最后一项使用461明列conductor-one固定gap \(\theta<9/10\) 的[R]；
原7/8足够。本稿不重证底层[R]全链。
[466](466-high-square-variance-commutator-obstruction.md)的实际lower bound
用于排除旧目标，未提供任何新的q上界或high/low commutator下界。

本稿所用最终canonical LF全文为：
465的SHA-256为
`a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464`；
466含sharp \(4M\) 的§5，SHA-256为
`0b955bdc26b4bf950ce457dec7bf18f635f702d85a73d73c8d6263df969cbbbe`。

## 2. 全部bounded-weight准入及两个真实平方残差

465的middle-P比较和同窗bilinear极化给
\[
 \begin{gathered}
 d^{-1}\operatorname{Tr}W^2\to S_H,\quad
 d^{-1}\operatorname{Tr}WH^2\to S_H,\quad
 d^{-1}\operatorname{Tr}WL^2\to C,\quad
 d^{-1}\operatorname{Tr}WHL\to0,\\
 d^{-1}\operatorname{Tr}V^2\to S_L,\quad
 d^{-1}\operatorname{Tr}VL^2\to S_L,\quad
 d^{-1}\operatorname{Tr}VH^2\to C,\quad
 d^{-1}\operatorname{Tr}VHL\to0,\quad
 d^{-1}\operatorname{Tr}WV\to C .
 \end{gathered}
 \tag{3}
\]
后五项不是新的four-word估计。前四个交换high/low weight即可。
最后一项的multiplication/Toeplitz乘积误差由
\(\|QM_wE\|_{\rm HS}\|QM_vE\|_{\rm HS}=O(\log(2+\mathcal L))=o(d)\)
支付。所有物理二矩保留454的差频Hilbert、和频与alias付款；
没有在带末端P的physical词上使用循环迹。

令
\[
 \Gamma=H^2-W,\qquad \Delta=L^2-V,\qquad Z=(HL+LH)/2 ,
 \tag{4}
\]
这些都selfadjoint。使用normalized real HS内积
\(\langle A,B\rangle=d^{-1}\operatorname{Tr}(AB)\)。
记
\[
 \begin{aligned}
 q_T&=\|\Gamma\|_{\rm HS}^2/d,&
 \delta_T&=\|\Delta\|_{\rm HS}^2/d,&
 a_T&=\operatorname{Tr}H^4/d,& e_T&=\operatorname{Tr}L^4/d,\\
 c_T&=\operatorname{Tr}H^2L^2/d=\|HL\|_{\rm HS}^2/d,&
 b_T&=\operatorname{Tr}H^3L/d,&
 k_T&=\|[H,L]\|_{\rm HS}^2/d .
 \end{aligned}
 \tag{5}
\]
从(3)、精确平方展开及462得到
\[
 a_T=S_H+q_T+o(1),\qquad
 e_T\to e_\psi,\qquad \delta_T\to\delta_\psi\ge0 .
 \tag{6}
\]
这三项误差不乘未知q增长因子，不先假设high4 bounded。

## 3. 严格有限Gram式：不删除centering errors

定义准确有限量
\[
 \begin{aligned}
 \chi_T&=d^{-1}\operatorname{Tr}(VH^2+WL^2-WV),&
 p_T&=\langle\Gamma,\Delta\rangle=c_T-\chi_T,\\
 \tau_T&=\operatorname{Re}\operatorname{Tr}(WHL)/d,&
 \beta_T&=\langle\Gamma,Z\rangle=b_T-\tau_T,\\
 \epsilon_T&=\langle\Delta,Z\rangle
    =\eta_T-\operatorname{Re}\operatorname{Tr}(VHL)/d,&
 z_T&=\|Z\|_{\rm HS}^2/d=c_T-k_T/4 .
 \end{aligned}
 \tag{7}
\]
有限循环迹支付每个恒等式；\(HL\)本身无需selfadjoint。
由(3)及461，
\[
 \chi_T\to C,\qquad \tau_T=o(1),\qquad\epsilon_T=o(1).
 \tag{8}
\]
且\(0\le k_T\le4c_T\)，所以\(z_T\ge0\)。

三个真实HS向量的Gram矩阵为
\[
 \begin{pmatrix}
 q_T&p_T&\beta_T\\ p_T&\delta_T&\epsilon_T\\
 \beta_T&\epsilon_T&z_T
 \end{pmatrix}\succeq0 .
 \tag{9}
\]
若\(\delta_T>0\)，从\(\Delta\)方向投影给准确Schur式
\[
 \boxed{\left|\beta_T-\frac{p_T\epsilon_T}{\delta_T}\right|^2
 \le\left(q_T-\frac{p_T^2}{\delta_T}\right)
      \left(z_T-\frac{\epsilon_T^2}{\delta_T}\right).}
 \tag{10}
\]
两个右因子分别非负。若\(\delta_T=0\)，则\(\Delta=0\)、
\(p_T=\epsilon_T=0\)，直接使用\(|\beta_T|^2\le q_Tz_T\)；
不除以0。flat及任何\(\delta_\psi>0\)的固定窗最终为非退化情况。

原整个prime fourth准确展开为
\[
 F_T=\operatorname{Tr}(H+L)^4/d
 =a_T+e_T+6c_T-k_T+4b_T+4\eta_T .
 \tag{11}
\]
因此每个非退化finite T都有
\[
 \boxed{\begin{aligned}
 F_T\le {}&a_T+e_T+6c_T-k_T+4|\tau_T|+4|\eta_T|
       +\frac{4|p_T\epsilon_T|}{\delta_T}\\
 &+4\sqrt{\left(q_T-\frac{p_T^2}{\delta_T}\right)
             \left(c_T-\frac{k_T}{4}
                         -\frac{\epsilon_T^2}{\delta_T}\right)} .
 \end{aligned}}
 \tag{12}
\]
无需q bounded。只知\(\epsilon_T=o(1)\)时，不能把
\(|p_T\epsilon_T|/\delta_T\)免费写成\(o(1)\)。
此式包含entire31、entire22的全部原signs、repeated/distinct labels。

## 4. Bounded-q极限：保留整个22的负项

现在另外假设\(\limsup q_T\le Q_0<\infty\)，且\(\delta_\psi>0\)。
(6)及\(c_T^2\le a_Te_T\)使\(c_T,k_T\)有界；
\(|p_T|\le\sqrt{q_T\delta_T}\)使(12)的centering error趋零。
在有界可行域中，平方根的连续性包括其0端点，故
\[
 b_T^2\le
 \left(q_T-\frac{(c_T-C)^2}{\delta_\psi}\right)
       \left(c_T-\frac{k_T}{4}\right)+o(1) .
 \tag{13}
\]
可以对finite表达的第一个近似因子取positive part后写统一上界；
任何达到极限的可行子列已自动满足它非负，不引入moving端点假设。

若另有\(\liminf k_T\ge\kappa_0\ge0\)，严格得到
\[
 \limsup F_T\le
 \max_{\mathcal D}
 \left[S_H+q+e_\psi+6c-k+
 4\sqrt{\left(q-\frac{(c-C)^2}{\delta_\psi}\right)(c-k/4)}\right],
 \tag{14}
\]
其中紧可行域可以取
\[
 \mathcal D:\quad
 0\le q\le Q_0,\quad c\ge0,\quad
 \kappa_0\le k\le4c,\quad
 (c-C)^2\le q\delta_\psi,\quad c^2\le(S_H+q)e_\psi .
 \tag{15}
\]
若该域为空，前件互不相容；不宣称其在原算术对象上可达到。
未付\(\kappa_0\)时只能用0。
fixed \(q,c\)下objective随\(k\)增大而减小，
所以把\(k\)免费设为0会丢掉真正可能的收益。
保留此项不是已经证明actual commutator有某个正下界。

## 5. Flat常数及只有q上界时仍不足的有理证书

取原flat profile及endpoint taper。由465(14)独立积分，
\[
 S_H=19/480,\quad C=23/960,\quad
 S_L=7/240,\quad e_1=19/240,\quad \delta_1=1/20 .
 \tag{16}
\]
466已经证明实际
\[
 \liminf q_T\ge\underline q=41/15120>1/400>1/1600 .
 \tag{17}
\]
不能继续把465反事实的旧小q门槛当作付款目标。

即使改用本稿更强Gram而舍去\(k\)，其保守envelope在
\(q=\underline q,c=1/30,k=0\)处仍大于\(1/3\)。
这些数属于(15)的代数可行域：
\(c-C=3/320\)、\(q-20(c-C)^2=q-9/5120>0\)，
且\(c^2<(S_H+q)e_1\)。
置
\[
 R=c\,[q-20(c-C)^2]=923/29030400,\qquad
 h=1/3-(S_H+q+e_1+6c)=359/30240>0 .
 \tag{18}
\]
纯有理计算给
\[
 16R-h^2=336311/914457600>0 .
 \tag{19}
\]
因此该objective的\(4\sqrt R\)超过剩余预算\(h\)。
这只证明该松弛不能单靠q上界认证\(1/3\)上界；
不是actual matrix等号模型，也没有证明所有joint方法不可能。

## 6. 一个未被(17)标量下界排除的联合候选

以下是明确、尚未证明的原算术前件：
\[
 \boxed{\limsup q_T\le Q_0=1/350,\qquad
        \liminf k_T\ge\kappa_0=1/40.}
 \tag{20}
\]
\(1/350-\underline q=11/75600>0\)，所以它仅未被466这条标量下界数值排除；
不代表实际可达到，更不代表两个合同已经支付。

对(15)中每个可行极限点，q替换为\(Q_0\)、k替换为\(\kappa_0\)
增加(14)的objective。又
\[
 c\le C+\sqrt{Q_0\delta_1}<C+3/250=863/24000 .
 \tag{21}
\]
记\(B=81/250\)，并定义
\[
 \begin{aligned}
 R(c)&=B-(S_H+Q_0+e_1-\kappa_0)-6c
       =6367/28000-6c,\\
 P(c)&=R(c)^2-16\bigl(Q_0-20(c-C)^2\bigr)\bigl(c-\kappa_0/4\bigr)\\
 &=320c^3+\frac{56}{3}c^2-\frac{1257437}{504000}c
       +\frac{717527777}{14112000000}.
 \end{aligned}
 \tag{22}
\]
在整个\([0,863/24000]\)，\(R(c)\ge163/14000>0\)。
对可行域radicand非负，只需证明\(P(c)>0\)。

这是全连续域的精确有理证书。把该区间分32等份；
第\(j\)份端点\(a_j=j(863/24000)/32\)、
\(b_j=(j+1)(863/24000)/32\)，\(h_j=b_j-a_j\)。
三次Bernstein四个系数准确为
\[
 P(a_j),\quad P(a_j)+h_jP'(a_j)/3,\quad
 P(b_j)-h_jP'(b_j)/3,\quad P(b_j).
 \tag{23}
\]
全部128个有理系数为正，最小值为
\[
 665078890949/6502809600000000>0 .
 \tag{24}
\]
Bernstein基在每段非负、总和1，所以\(P\)在整个区间严格正。
本稿作者已独立以内存有理多项式计算复算(22)–(24)；
不是从网格最大值推断连续域。
由(22)正R与平方比较，(14)的整个joint objective严格小于\(81/250\)。

在(20)及原已付输入下，whole prime fourth因而bounded。
455的proper-power S4-small和454的flat背景预算才在此之后适用；
原完整centered response的limsup也不超过\(81/250\)。
452支付同一对象的zero-side padding；
197/228在原首迹、二矩及完整有限误差下给条件蕴含
\[
 \liminf\frac{s(T)}{N(T)}
 \ge\frac{(1-1/3)^2}{1-2/3+81/250}
 =\frac{1000}{1479}>\frac{27}{40}.
 \tag{25}
\]
分母为正，辅助参数\((1/3-81/250)/(2/3)=7/500\)
位于\((0,3/4)\)，一侧中心四矩接口无需三阶矩极限。

## 7. 实际剩余付款

新增的是完整finite Schur式和一个通过连续有理证书的条件joint预算。
原\(q_T\)上界与\(k_T\)下界仍都未支付；
不能将(25)称作67.5%以上的实际比例，也不登记新无零边界。
这些量保留实际projection leakage，不能由物理ratio正子和或
repeated主项替换。下一真实算术任务是同一原矩阵的signed
covariance与commutator能量，或能进一步收紧(15)的实际联合结构。
底层[R]、全high四词及实际零点feature可见性没有在本稿得到独立认证。

[本轮精确审计脚本](../scripts/hybrid_original_residual_exact_audit.py)
重现flat积分、有理反事实阻断及32段的全部Bernstein系数。
有限执行结果不支付(20)，不认证分析[R]或原实际四素数算术。
