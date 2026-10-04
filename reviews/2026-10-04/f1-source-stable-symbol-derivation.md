# 原源稳定域的交叉Gram、实际新商及周期核扩大

2026-10-04。继续[427](../../notes/427-f1-corner-product-algebra-and-unavoidable-trace-cocycle.md)、
[428](../../notes/428-f1-corner-essential-symbol-and-complete-readout-freedom.md)与
[429](../../notes/429-f1-original-unitary-crosses-the-fixed-corner-domain.md)。
本报告计算真源与原采样的精确交叉Gram，证明最小真实源理想的Calkin商已非交换，
并核准一个具体的源双侧稳定平滑核域。后者尚未证明等于最小源理想；这里不据此冒认完整相对Chern或算术主关系。

## 1. 源箭头保持x的完整纤维计算

仍取414原源c、\(d_p=c\)及原\(d_q\)，
\(\sum_jc(t-jL)^2=\sum_kd_q(t-kM)^2=1\)。
在425完整波形基中，物理群仍为
\(P_{(a,b)}=\lambda_a\otimes\lambda_b\otimes\mathsf T_{aL+bM}\)。
记427去共同时间酉元后的采样为V，\(A(h)=VU(h)V^*\)。

作全Hilbert空间的变量变换
\[
 x=t-jL-kM.
\]
这是在波形基坐标中的酉直积分重写，不是取角点字符、径向环面评价或选择单一x纤维来替代原表示。
原每个源箭头保持x；其系数在\((j,k,x)\)处为\(c(x+jL+kM)\)。
定义
\[
 c_k(x)=\sum_{j\in\mathbb Z}c(x+jL+kM)e_j\in\ell^2(\mathbb Z),
 \qquad \|c_k(x)\|=1.
\]
原e在每个q次数k上是\(P_{c_k(x)}\)，而源v把
\(c_k(x)\otimes e_k\)送至\(c_{k+1}(x)\otimes e_{k+1}\)，在e的正交补为零。

对全部整数r令
\[
 v_r=\sum_aM_{c(t)c(t-aL-rM)}P_{(a,r)}.                     \tag{1}
\]
每个固定r的非零a有限。上述纤维秩一箭头直接给
\(v_rv_s=v_{r+s}\)、\(v_r^*=v_{-r}\)、\(v_0=e\)；
因此
\[
                         u^r=1-e+v_r\quad(r\in\mathbb Z). \tag{2}
\]
这个公式包括r=0；所用平方分割及右平移均来自原源。

V在此直积分中是标量时间空间到径向纤维的向量乘法：
\[
 (V\phi)(x)=\zeta(x)\phi(x),\qquad
 \zeta(x)=\sum_{j<0}c(x+jL)e_j\otimes e_0
            +\sum_{k<0}d_q(x+kM)e_0\otimes e_k.             \tag{3}
\]
这里\(e_j,e_k\)记波形标签的标准坐标。两大和在每个x处有限，互相正交。

## 2. 精确交叉Gram函数

置
\[
 \begin{split}
 m_p(x)&=\sum_{j<0}c(x+jL)^2,\qquad
 m_q(x)=\sum_{k<0}d_q(x+kM)^2,\\
 b(x)&=c(x)d_q(x),\qquad b_k(x)=b(x+kM),\\
 \alpha_-(x)&=\sum_{k<0}b_k(x)^2,\\
 a_k(x)&=m_p(x)\mathbf1_{k=0}+b_k(x)\mathbf1_{k<0}.
 \end{split}                                               \tag{4}
\]
e投影后的第0个q块系数是\(m_p(x)\)，负q块系数是\(b_k(x)\)；
因此
\[
 \langle\zeta,e\zeta\rangle=m_p^2+\alpha_-,
 \qquad
 \langle\zeta,v_r\zeta\rangle=\sum_k a_{k+r}a_k.
 \]
由(2)得到完整乘法算子等式
\[
 \boxed{V^*u^rV=M_{g_r},\qquad
  g_r=m_p+m_q-m_p^2-\alpha_-+\sum_k a_{k+r}a_k.}             \tag{5}
\]
这已经包含p←q及q←p交叉Gram，未把它们删去。
特别\(g_0=m_p+m_q=m\)，核准原\(V^*V\)。
对r≠0，最后一项可进一步明确写成
\[
 \sum_{\substack{k<0\\k+r<0}}b_{k+r}b_k
   +m_p b_{-r}\mathbf1_{r>0}+m_p b_r\mathbf1_{r<0}.         \tag{6}
\]
后两项正是两个通道的有限交叉行；它们在x上紧支。
全部\(g_r\)光滑有界，\(\|g_r\|_\infty\le\|V\|^2=2\)，且充分负端为零。

## 3. 右端的实际周期Gram及轨道秩

定义原时间系数的完整M周期化
\[
 \alpha(x)=\sum_{k\in\mathbb Z}b(x+kM)^2,\qquad
 \beta_r(x)=\sum_{k\in\mathbb Z}b(x+(k+r)M)b(x+kM).          \tag{7}
\]
它们光滑、M周期；b紧支给\(\beta_r=0\)当\(|r|M>\operatorname{diam}\operatorname{supp}b\)。
由\(c^2\le1\)及\(d_q\)的平方分割，\(0\le\alpha\le1\)，\(\beta_0=\alpha\)。
对每个固定r，在充分正端，\(m_p=m_q=1\)，所有可见b标签严格负，(6)的交叉项零；
因此(5)精确变为
\[
 \boxed{g_r(x)=R_r(x),\qquad
 R_r(x)=\mathbf1_{r=0}+1-\alpha(x)+\beta_r(x)
 \quad(x\text{充分大}).}                                  \tag{8}
\]
特别\(R_0=2\)；r≠0时p深边贡献0，q深边贡献\(1-\alpha+\beta_r\)。
在充分负端\(g_r=0\)，所以**\(g_r-R_r\)通常并不紧支**：负端仍为\(-R_r\)。
后面的迹类准入必须另付半线局部化，不能把这个差直接称为紧支误差。

尾Gram还具有严格的正性与秩信息。设
\[
 B_x(z)=\sum_k b(x+kM)z^k,\qquad |z|=1.
\]
此为每个x的有限Laurent多项式；\(x\mapsto|B_x|^2\)是M周期。
对任意有限复系数\((z_i)\)，
\[
 \begin{split}
 \sum_{i,j}\overline z_i z_j R_{j-i}(x)
   ={}&\sum_i|z_i|^2+(1-\alpha(x))\left|\sum_i z_i\right|^2\\
 &+\frac1{2\pi}\int_0^{2\pi}|B_x(e^{i\theta})|^2
                         \left|\sum_i z_ie^{ii\theta}\right|^2d\theta\\
 \ge{}&\sum_i|z_i|^2.                                      \tag{9}
 \end{split}
\]
这是实际源轨道的ToeplitzGram不等式；θ积分仅表示这个正定序列的Fourier展开，没有对物理径向环面选字符。
任意有限数量的源轨道frame尾Gram都满秩，不能固定有限个轨道后仍保持所有这些Gram。

还有一个可直接在实际Calkin商观察的结论。若有限系数z不全零、h≠0，
\[
                         \sum_i z_i u^i A(h)\quad\text{非紧}. \tag{10}
\]
证明：令\(W_z=\sum_i z_iu^iV\)。由(5)、(9)，其Gram乘法函数在右端至少\(\sum_i|z_i|^2\)。
选紧支单位ψ使\(U(h)\psi\ne0\)，把ψ平移至足够靠右。
对应\(\xi=V\psi/\sqrt2\)为弱趋零单位向量列，
\((\sum z_iu^iA(h))\xi=\sqrt2W_zU(h)\psi\)有共同正下界。
这排除源左轨道在商中的任何非零有限常系数线性关系；不据此断言全部商已分类。

## 4. 最小真实源理想的商已严格非交换

令\(\mathcal E=\overline{\mathcal D}^{\|\cdot\|}\)为428的原C*域，
\(\mathcal C=C^*(1,u,\mathcal E)\)，J为\(\mathcal C\)中由\(\mathcal E\)生成的闭理想。
\(\mathbb K(\mathcal H)\subset\mathcal E\subset J\)，故其实际Calkin像是\(J/\mathbb K\)。
以下给该最小源理想中的具体非交换元素，而非仅以闭包定义宣称有新结构。

选非零实偶\(h\in C_c^\infty\)，令
\[
 F=uA(h)\in J,\qquad G=A(h)u^*\in J.
\]
直接乘法及427的迹类乘积余项给
\[
 [F,G]=uA(h)^2u^*-A(h)^2
       =2\{uA(h*h)u^*-A(h*h)\}+\mathcal S_1.                \tag{11}
\]
而\((h*h)(0)=\int h(s)^2ds>0\)。429的q=1深负行给
\[
 (I_n^1)^*\{uA(h*h)u^*-A(h*h)\}I_n^1=B_0(h*h).
\]
该时间块普通迹为\(L(h*h)(0)>0\)，故非零。
迹类余项在正交单位向量列上的范数趋零，不影响共同正下界；
因此(11)非紧，\(\pi(F)\pi(G)\ne\pi(G)\pi(F)\)。
\[
                         \boxed{J/\mathbb K\text{非交换}.} \tag{12}
\]
这对原所有合法c、d_q成立，不需某个分割的\(\alpha\)非恒定。
它严格排除把源稳定后的商继续等同于原标量\(C_0(\mathbb R_\xi)\)的候选，
但未给J全商的完整识别或K边界。

## 5. 允许原来源中的非恒定周期实例

当p<q，即L<M时，选小ε使\(L+2\varepsilon<M\)。
原平方分割构造允许c支撑在长度\(L+2\varepsilon\)的区间：
先取该区间中覆盖一个完整L基本段的正光滑函数，再除以其L平移平方和的平方根。
另选合法d_q在c的某个正区间严格正，则\(b=cd_q\not\equiv0\)，
且\(\operatorname{diam}\operatorname{supp}b<M\)。

于是\(\beta_r=0\)对所有r≠0；\(\alpha=\sum_kb(x+kM)^2\)在一个M周期中有开零弧，
在另一开区间严格正，所以非恒定。因此
\[
                             R_r=1-\alpha\quad(r\ne0)     \tag{13}
\]
是实际来源导出的非恒定周期系数，不是自由加入的目标权重。
此为允许源中的明确实例，**不声称每个原分割的R_r都非恒定**。

源夹心乘积的准确表达为
\[
                       A(h)u^rA(k)=VU(h)M_{g_r}U(k)V^*.    \tag{14}
\]
利用下一节的半线局部化，在迹类商中可把\(g_r\)换成\(R_r\)。
当R_r有非零周期谐波时，\(U(h)M_{R_r}U(k)\)具有真实频率移位，
不能普遍化成标量卷积。
例如非零谐波次数n、\(\nu=2\pi/M\)给输入频率η到η+nν的系数
\((R_r)_n\widehat h(\eta+n\nu)\widehat k(\eta)\)。
选择原合法光滑测试使这两个值非零，得到实际非对角频率耦合；无需环面字符评价。

## 6. 具体周期核域与正确的源乘法准入

定义\(\mathcal G_M\)为L²(\(\mathbb R_x\))上全部光滑核算子B，核满足
\[
 K_B(x+M,y+M)=K_B(x,y),\qquad K_B(x,y)=0\ (|x-y|>R_B),
\]
且各阶导数在基本条带有界。周期与有限传播把有关条带化成紧集；
Schur界给有界性。卷积、伴随及逐项微分积分证明此为非单位化星代数。
\(U(h)\in\mathcal G_M\)，并且
\(BM_{R_r}C\in\mathcal G_M\)对B、C∈\(\mathcal G_M\)成立。
后者核为\(\int K_B(x,z)R_r(z)K_C(z,y)dz\)，平滑、周期、有限传播均保持。

考察具体有限和域
\[
 \mathcal D_{\rm src}
  =\operatorname{span}_{\rm finite}
       \{u^iVBV^*u^{-j}:i,j\in\mathbb Z,\ B\in\mathcal G_M\}
       +\mathcal S_1.                                     \tag{15}
\]
定义在完整原Hilbert空间，不是只给抽象闭包。
其两个生成元乘积由(5)为
\[
 (u^iVBV^*u^{-j})(u^kVCV^*u^{-l})
             =u^iVBM_{g_{k-j}}CV^*u^{-l}.                 \tag{16}
\]
V与V*由原m左端为0而满足\(V=V\mathbf1_{[a,\infty)}\)。
C有限传播使\(CV^*\)输出位于\([a-R_C,\infty)\)。
取光滑χ在该半线为1、在充分负端为0。
因为\(g_r-R_r\)在充分正端精确为零，
\[
 f_r=\chi(g_r-R_r)\in C_c^\infty,\qquad
 M_{g_r-R_r}CV^*=M_{f_r}CV^*.
\]
\(BM_{f_r}C\)的中间变量z紧支，有限传播使x、y也紧支；
其完整核光滑紧支，故确为迹类。乘有界V、u幂仍迹类。
因此(16)在同一域中准确成为
\[
 u^iV(BM_{R_{k-j}}C)V^*u^{-l}+\mathcal S_1.                \tag{17}
\]
伴随交换i、j并把B变为B*；左右乘u、u*只改变整数指标。
所以\(\mathcal D_{\rm src}\)是实际星代数，含原D，且由真源u双侧稳定。

**范围：** 任意\(\mathcal G_M\)核形成的是明确的解析扩大。
尚未证明其中每个任意周期核都由原u及A测试族生成，
因此不能未经生成性论证，把(15)称为最小J本身。
它的范数完成是一个源稳定的具体容纳域，包含J；J的全商识别仍待支付。

## 7. 周期核在扩大域中的精确Calkin符号

对任意\(B\in\mathcal G_M\)，取紧支单位ψ并以nM平移至足够靠右。
B与\(\mathsf T_M\)交换，且有限传播保证Bψ的支集也位于m=2端。
于是\(\xi_n=V\mathsf T_{nM}\psi/\sqrt2\)为弱零单位向量列，且
\[
 \|VBV^*\xi_n\|=2\|B\psi\|.
\]
取紧支光滑ψ的上确界，再用\(\|V\|^2=2\)上界，精确得
\[
                 \|VBV^*\|_{\rm ess}=\|VBV^*\|=2\|B\|.     \tag{18}
\]
由(17)在r=0时的\(R_0=2\)，
\[
                 \rho(B)=\tfrac12\pi(VBV^*)               \tag{19}
\]
是等距星同态；乘积误差确为迹类，非仅形式符号。

周期核代数本身也可明确识别。把L²(\(\mathbb R\))按M胞元分成
\(\ell^2(\mathbb Z)\otimes L^2(0,M)\)：
\((\mathscr J\phi)_j(t)=\phi(t+jM)\)。
有限传播使B只有有限个胞元差n；其块
\[
 C_n(t,s)=K_B(t,s+nM),\qquad 0<t,s<M
\]
是Hilbert–Schmidt紧算子。对胞元整数指标作完整Fourier酉变换后，B成为
\[
                         \sum_n e^{in\theta}C_n           \tag{20}
\]
这个连续紧算子值Laurent多项式的乘法算子。
这是保留全θ直积分的Floquet变换，不是偷取某个物理字符。

反向，对\(f,g\in C_c^\infty(0,M)\)延拓为实线紧支函数，实际周期化矩阵单位
\[
 L_n^{f,g}=\sum_{j\in\mathbb Z}
       |\mathsf T_{jM}f\rangle\langle\mathsf T_{(j+n)M}g|
\]
属于\(\mathcal G_M\)，在(20)中给\(e^{in\theta}|f\rangle\langle g|\)。
这些有限秩系数与Laurent多项式一致稠密于连续紧算子值函数。
故
\[
 \boxed{\overline{\mathcal G_M}^{\|\cdot\|}
            \cong C(S^1)\otimes\mathbb K(L^2(0,M)).}        \tag{21}
\]
(19)把这一C*代数等距嵌入(15)范数完成的实际Calkin商。
没有证明这个整个周期核商已经包含在最小J的商中；任意周期核的原源生成性仍缺。

## 8. 本轮完成与尚缺桥梁

已得到原u与V的精确g_r、实际尾R_r、统一轨道Gram下界、最小源理想商非交换，
以及一个经过完整迹类误差准入的u双侧稳定周期核域。
扩大域的周期核符号已有具体胞元／Fourier模型；不是空泛地只定义闭包。

仍缺最小J全商、其K边界、原球截止在扩大域中的传递及规范相对Chern链。
这些公式没有给新边自由指定读出，也没有选出原Λ而排除426的任意时间分布自由度。
完整算术主消失、实位与全素数Weil比较、RR、正性及RH继续开放。
