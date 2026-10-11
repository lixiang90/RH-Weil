# 513. 新增一个素数的实际闭链传递与单位链修正

2026-10-11。[T/R] 继续[511](511-f1-semilocal-fourier-inversion-cycle.md)、
[512](512-f1-finite-place-double-moment-sign-test.md)。
本稿在真实径向角中给单素数Hochschild链传递、显式二边界、独立的时间域迹类证明及全部新增Euler电荷。
有限素数的相容公式不提供无限S链极限、真实主除子或全局负性。

## 1. 先用实际源映射建立同一角

固定有限S、素数 \(\ell\notin S_f\)，\(S'=S\cup\{\ell\}\)。
沿用511的源、加权完成、紧群概率Haar与实际共同Fourier。
512的真实源映射
\[
 F\longmapsto F\otimes\mathbf1_{\mathbb Z_\ell^\times}
\]
给等距 \(j:\mathcal H_S\to\mathcal H_{S'}\)：
新单位壳层使周期化中新的S-unit指数为0，像是在新紧群变量上的常函数。

令 \(P=P_{0,S}\)、\(E=P_{0,S'}\)、\(J_0=jP\)。
紧群平均给 \(Ej=jP\)，全部新径向函数都在j的像内，因此
\[
 J_0^*J_0=P,\qquad J_0J_0^*=E.                           \tag{1}
\]
J₀只在径向块间是满酉；整个空间间是partial isometry。
反演、红外Π以及径向测试卷积均与这条实际映射交织。

先取旧角代数 \(\mathfrak A_{S,0}=P\mathfrak A_SP\)。
其单位是P，迹类理想准确是 \(\mathcal S_1(P\mathcal H_S)\)。
\[
 \alpha(A)=J_0AJ_0^*,\quad A\in\mathfrak A_{S,0}           \tag{2}
\]
是精确星同构到运输后的角代数，保持普通迹与迹类范数，单位映成E。
不直接把整个旧代数的任意A送入J₀AJ₀*并称它为精确代数同态：
J₀*J₀=P，而且旧代数的任意迹类元未必被P reducing。

在实际新径向块上明确取
\[
 \mathfrak B_E=\operatorname{alg}^*
 \bigl(\alpha(\mathfrak A_{S,0}),E\mathcal F_{S'}E,E\mathcal I_{S'}E\bigr),
 \qquad Q_E=\mathfrak B_E/\mathcal S_1(E\mathcal H_{S'}).   \tag{3}
\]
它含全部径向迹类元，单位严格是E。相应的全空间扩大由新原代数与这些运输后的角元生成；
这是由指定源映射支付的扩大，未声称等于旧430代数。

令旧、新Fourier–反演的角算子为
\[
 W=\alpha(P\mathsf S_SP),\quad
 T=E\mathsf S_{S'}E,\quad V=TW^*,\quad
 C=E\Pi_{S'}A_{S',h}E=\alpha(C_{S,h}).                    \tag{4}
\]
W、T、V为角酉，\(T=VW\)。
511在真实稠密源上的Mellin计算给
\[
 W=M_{m_S},\quad T=M_{m_Sm_\ell},\quad V=M_{m_\ell},\quad
 m_\ell(\tau)=\frac{1-ae^{-i\tau L}}{1-ae^{i\tau L}},
 \quad a=\ell^{-1/2},\ L=\log\ell.                       \tag{5}
\]
所以V、W实际上交换。这里的符号识别已定义的来源算子；
不按目标电荷选择相位，也不把它推广到所有非平凡紧群字符。

## 2. 从正向真实缩放得到收敛展开

径向对数坐标中写 \(Z_t v(u)=v(u-t)\)。
\(Z_L=\ell^{-1/2}EU_{S'}((\ell,1,\ldots,1))E\) 来自真实正向实缩放，
频率符号是 \(e^{-i\tau L}\)。于是
\[
 V=(E-aZ_L)(E-aZ_{-L})^{-1}
   =-aZ_L+(1-a^2)\sum_{j\ge0}a^j Z_{-jL}.                \tag{6}
\]
逆级数与最后展开均在算子范数中绝对收敛。
这个有理表达式等于已经在(3)准入的TW*，没有暗中要求原星代数范数闭合。

定义实系数 \(v_1=-a\)、\(v_{-j}=(1-a^2)a^j\)（j≥0），其他为0。
\[
 \sum_n|v_n|=1+2a,\quad
 \sum_n|n|\,|v_n|=\frac{2a}{1-a},\quad
 \sum_{n\ne0}|v_n|=2a+a^2.                              \tag{7}
\]
每个有限阶带权系数和均有限。

## 3. 时间域直接支付新增边界的迹类准入

仍取实 \(h\in C_c^\infty(\mathbb R)\)、\(h^\sharp=h\)，
\(\eta(t)=e^{t/2}h(t)\) 实偶；\(A=A_\eta\)为卷积
\((A\psi)(u)=\int\eta(u-v)\psi(v)\,dv\)，\(C=\Pi A\)、\(\Pi=\mathbf1_{u\le0}\)。
同一径向表示中的新增边界为
\[
 B_\ell=C-VCV^*=[\Pi,V]AV^*.                            \tag{8}
\]

对有限区间I，先支付 \(M_IA_\eta\in\mathcal S_1\)。
在I=[0,1]上，右变量谐振子 \(H=1+v^2-\partial_v^2\) 给
\[
 (M_IA_\eta)H\text{ 的核}=
 \mathbf1_I(u)\bigl((1+v^2)\eta(u-v)-\eta''(u-v)\bigr).
\]
它属于L²，因为 \(1+v^2\le3(1+(u-v)^2)\)。
\(\|H^{-1}\|_2=\pi/\sqrt{24}\)，故
\[
 \|M_{[0,1]}A_\eta\|_1
 \le C_\eta:=\frac{\pi}{\sqrt{24}}
       \bigl(3\|(1+x^2)\eta\|_2+\|\eta''\|_2\bigr).        \tag{9}
\]
恒等式先在Schwartz域上验证，再延伸；不对输出硬截止求导。
分割成至多 \(\lceil |I|\rceil\) 个长度≤1区间，并用平移酉性，给
\(\|M_IA_\eta\|_1\le C_\eta(1+|I|)\)。

对t、s∈R，
\[
 [\Pi,Z_t]AZ_s=
 (\mathbf1_{u\le0}-\mathbf1_{u-t\le0})A Z_{t+s}.           \tag{10}
\]
t≠0时输出位于长度|t|的一个有限区间，故
\[
 \|[\Pi,Z_t]AZ_s\|_1\le C_\eta(1+|t|),                  \tag{11}
\]
独立于s；t=0的项准确为0。
(6)、(7)于是使
\[
 B_\ell=\sum_{n,m}v_n v_m[\Pi,Z_{nL}]AZ_{-mL}             \tag{12}
\]
在迹类范数中绝对收敛，并给显式连续界
\[
 \boxed{\|B_\ell\|_1\le C_\eta(1+2a)
       \left(2a+a^2+\frac{2La}{1-a}\right).}             \tag{13}
\]
这是来源位移级数的准入，未通过相减两个标量迹或强极限付清。

## 4. 时间域普通迹准确给新增Euler电荷

若η支集在[-R,R]，(10)的输入也落在某个有限区间。
用两端有限区间压缩和频率积分，可把卷积核写成迹类Bochner积分：
测试变换明确取 \(\varphi(\tau)=\int\eta(t)e^{-i\tau t}\,dt\in L^1\)，
反变换带 \(1/(2\pi)\)；这与状态空间的酉Fourier归一化分开。两端指数向量均属L²。
因此普通迹准确为核的对角积分，
\[
 \operatorname{Tr}([\Pi,Z_t]AZ_s)=-t\,\eta(-t-s).         \tag{14}
\]
不把未截断的实轴指数向量当作L² rank-one因子。

令 \(d_r=\sum_n n v_n v_{n-r}\)。
绝对几何求和给
\[
 d_0=0,\qquad d_r=-a^{|r|}\quad(r\ne0).                  \tag{15}
\]
例如r≥1，n=1贡献 \(-(1-a^2)a^r\)，负n贡献 \(-a^{r+2}\)；
r≤−1同样求和，r=0正负两项准确抵消。
由(12)的迹类收敛、(14)、(15)，
\[
 \operatorname{Tr}B_\ell
 =-L\sum_r d_r\eta(-rL)
 =L\sum_{r\ge1}a^r(\eta(rL)+\eta(-rL))
 =\boxed{2\log\ell\sum_{r\ge1}h(r\log\ell)}.              \tag{16}
\]
最后算术和因h紧支而实际有限；没有有限位自由δ₀。

算子恒等式
\[
 B_T=C-TCT^*=B_\ell+V(C-WCW^*)V^*                        \tag{17}
\]
把新旧边界接到同一来源中。旧边界由511准入，(13)给新增准入，
所以三条商一链均真实闭合；普通迹保持的运输与酉共轭给完整电荷传递。

## 5. 一链乘法必须保留单位链

在角商中写 \(e=qE\)、\(c(u,C)=u^{-1}\otimes uC\)，
\[
 \widetilde c(u,C)=c(u,C)-e\otimes C.                    \tag{18}
\]
这里“单位修正”明确改变了链；不称 \(e\otimes C\) 的HH₁类为零。
其一次边界及普通电荷均为零，但在普通Hochschild同调中仍可能非零。
例如交换代数C[x]中的 \(1\otimes x\) 经 \(a\otimes b\mapsto a\,db\)
送到dx，后者杀全部二边界。

采用 \(b_2(a,b,c)=ab\otimes c-a\otimes bc+ca\otimes b\)。
任意可逆u、v，令 \(C_v=vCv^{-1}\)，直接展开得
\[
 \widetilde c(uv,C)-\widetilde c(v,C)-\widetilde c(u,C_v)
 =b_2\left(u^{-1}\otimes u\otimes C_v
              -(uv)^{-1}\otimes u\otimes vC\right).      \tag{19}
\]
这个恒等式无需u、v交换。

本轮已证qC与qV、qW交换。取u=qV、v=qW，(19)给同一角商中的
\[
 \boxed{\widetilde c(qT,qC)
       =\widetilde c(qW,qC)+\widetilde c(qV,qC)+b_2H_\ell}, \tag{20}
\]
\[
 H_\ell=q(V^*)\otimes qV\otimes qC
             -q(T^*)\otimes qV\otimes q(WC).
\]
未修正链的公式则是
\[
 c(qT,qC)=c(qW,qC)+c(qV,qC)-e\otimes qC+b_2H_\ell.        \tag{21}
\]
所以(20)远强于仅证明电荷相加；单位项不能因电荷为零就被删掉。

## 6. 全空间链与角链有显式桥接，有限顺序相容

若全空间酉U与径向投影P交换，且C=PCP，
令D=(1−P)U*，则
\[
 c(U,C)-c(PUP,C)=qD\otimes q(UC)
             =-b_2(qD\otimes qP\otimes q(UC)).            \tag{22}
\]
因为DP=0、P(UC)=UC、(UC)D=0。
同样
\[
 1\otimes qC-qP\otimes qC
            =-b_2(q(1-P)\otimes qP\otimes qC).            \tag{23}
\]
(22)、(23)使511原全空间链合法进入角后，再用(2)逐张量运输。
没有凭“非径向测试为零”直接删除张量补块。

两个新增素数的源嵌入按单位壳层张量与基本域常函数扩张实际相容，
径向Vℓ、Vp由同一真实缩放产生并交换。
将各条链运输到最终有限S的同一角，重复(20)得到
\[
 [\widetilde c_{S\cup F,h}]
   =[\widetilde c_{S,h}]+\sum_{\ell\in F}[\widetilde c_{\ell,h}]
 \quad\text{in the common finite target }HH_1.           \tag{24}
\]
F必须有限，所有原素数电荷保留，最终乘积与添加顺序无关。
这是实际源映射下的有限相容性，不是全adele的链极限。

## 7. 下一关口

单素数实际传递、单位修正、二边界与新增Euler费用已经支付。
[514](514-f1-late-prime-tail-and-mixed-charge.md)进一步检验：零电荷的远端新增类是否仍有混合读出，
以及能否绝对迹类累计这些边界。
原主关系仍须满足405的双次数与完整混合根空间；
本稿未认证任何这些新增类为几何主关系，也未将来源Hilbert酉性等同于全部零点的谱识别。
