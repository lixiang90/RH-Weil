# 444. 同源联合 error slots 与全物理频率的 central high 节省

2026-10-07。状态 [T/R]：相对于明确的原局部算术、L函数反射/reciprocal、
witness与通用moments，以及原全Hecke 7/8 bootstrap，证明新几何的实际中央联合界。
442支付完整轮廓和外行，443支付实际count；本稿不以nominal R代替实际rows。
最后的continuation与对来源本身的独立验收须区分。

## 1. 固定对象、来源和共同参考幂

固定[OpenAI/math原稿](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
提交adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical LF SHA256
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
精确前件为原8707–9049的full tuple、dynamic local表、error proposition，
primitive numerator反射/删因子与buffered reciprocal，
以及443已逐前件重放的actual counts。核心原算术和通用分析为[R]。

使用441–443的同一个physical finite compensated probe及所有原masks、ray data、windows：

\[
 \ell_1=1/6+t_0=10003/60000,\quad t_0=1/20000,\quad b=1/8,
 \quad l_x=42497/120000,\quad l_y=57497/120000,
 \quad h_1=32503/40000,\quad \sigma_1=69999/80000.
\]

原全Hecke7/8结论给bootstrap sigma1<beta_*<=7/8，设Delta1=beta_*-sigma1>0。
取kappa_eff=3/4、Delta_eff=0。每个非floor bin有delta=2a-1<=3/4；
下面在更大的0<=delta<=alpha=5/6代数范围作uniform包络。
主留数始终z=1/6，故C(s)=s-11/16。

## 2. Dynamic decomposition及离零域

Whole-bin轮廓先按442完成；只在retained points作dynamic有限分解。
此处

\[
 \Re s=a+16e,\quad\Re w=1-a-6e,\quad\Re z=z_0=17/50,
 \quad51/100\le a\le1,\quad0<e<10^{-3}.
 \tag{1}
\]

Full correction是442(6)的无商tuple。原局部表在(1)给
H_p-1=O(Q^{-1-10e})于p不整除u，及O(Q^{-10e})于p|u。
固定e后选P0使所有slot primes的|H_p-1|<1/2，故仅在此dynamic域可令B_p=G_p/H_p。
原同源身份给有限分解

\[
 \mathfrak H_{\eta,u,Z}=\mathcal H_{\eta,u}
 \sum_{I\subseteq[K]}\prod_{i\in I}\mathcal D_i
                        \prod_{i\notin I}\mathcal Q_i,
 \qquad\mathcal Q_i=-P_i^{z-1/2}Q_i,
 \tag{2}
\]

Q_i为443(8)原physical slot，mathcal D_i为同slot B_i减去mathcal Q_i。
p|u时main项仍为0。此商分解不用于contour joins或global continuation。
Unselected正majorant使mathcal H<<U^epsilon，独立于selected labels。

## 3. 一个numerator与全部error slots的联合账本

Off-row原抵消只留四个幂。令theta=(-Re w)_+<=6e，在(1)的上界分别为
-a-4e、-51/25+12e、49/25-5a-68e、a-51/25+12e，均<=-51/100。
每槽O(P_i)个prime ideals给O(P_i^{z0-51/100+epsilon})，
强于所需central scale P_i^{z0-1/2}。

Ramified D=W=0后，原j=1,…,5的boundary项分出Q^{z0}，e=0时幂分别为
a-2、1/2-2a、(-a,1-3a)、1/2-2a、2-5a；
e改动分别+6e、-32e、(-26e,-48e)、-42e、-80e。
这些均<-1/2。Common R与V geometric tails有固定负ratio，
explicit rescaling也给-1-Re w<-1/2。Ramified labels divisor-many，
所以除下述strict项外，每个error slot仅花central scale，没有正amplitude gain。

唯一strict ramified项来自j>=2、(e0,l,k,m)=(1,0,1,0)，
分出Q^{z0}后只有Q^{-Re w}；不能逐槽单独声称Q^{-1/2}。
Triangle展开固定error tuple后，令J0恰为其中distinct strict labels，
psi_u^*为numerator的primitive inducing character。原CRT/reciprocity给

\[
 q_{\mathfrak f_u}\ll_S q_{\mathrm{rad}(u)}
 \le q_u\prod_{p\in J0}Q_p^{-(j_p-1)}.
 \tag{3}
\]

J0无重复是physical disjoint supports的后果。
Functional equation的conductor幂A_*=1/2-Re w=a-1/2+6e>0。
Numerator及conjugate都在buffered bin中；反射值Re(1-w)=a+6e
满足同一个cumulative height buffer。原primitive reflected reciprocal/growth接口
与删因子恢复共同花U^{6e+epsilon}乘固定height幂。
Strict selected primes本来在primitive conductor中，恢复因子为1。
一次性将(3)应用到整个J0后，numerator×strict factors一起至多为

\[
 U^{a-1/2+12e+\epsilon}(1+T_1)^A
 \prod_{p\in J0}Q_p^{z_0-\Re w-(j_p-1)A_*}
 \le U^{a-1/2+12e+\epsilon}(1+T_1)^A
 \prod_{p\in J0}Q_p^{z_0-1/2}.
 \tag{4}
\]

最后一步由j_p>=2及-Re w-A_*=-1/2。
这只使用一次numerator conductor，不为每个error slot重复赋予U^{A_*}。
剩余labels divisor-many，所有finite powers按固定K分配，故每个I均有

\[
 \boxed{|L^S(w,\chi_\bullet(u))\prod_{i\in I}\mathcal D_i|
 \ll U^{\delta/2+O(e)+\epsilon}(1+T_1)^A
       \prod_{i\in I}P_i^{z_0-1/2+O(e)+\epsilon}.}
 \tag{5}
\]

Empty I是同一numerator bound。u=1外numerator非主用原unit分类与
good ramification证明；bounded nontrivial units仍由442外小行处理。
此处不以L′的零替代L的零。

## 4. Mixed main/error amplitudes与实际行数

在retained point每个error subset I上，main gains g_i∈[0,delta/2]，
error slots恰取g_i=0。令q=sum_i ell_i g_i/ell1∈[0,delta/2]。
分母是所有physical slots总长度，不只main slots。
Main上界与(2)(5)给

\[
 |L^S(w,\chi_\bullet(u))\mathfrak H^{(I)}_{\eta,u,Z}|
 \ll U^{\delta/2+O(e)+\epsilon}(1+T_1)^{A_1}
 Z^{\ell_1(z_0-1/2)+q\ell_1+O(e+\theta_{amp}+\epsilon)}.
 \tag{6}
\]

因此central-accounting的实际gain是g=q ell1。
443给d>=1/2非floor actual pointwise set的count
#C<<U^{R_*(delta,x)+epsilon}(1+T1)^{A_2}，x=q/delta，且

\[
 R_*=1-\delta+\frac{(\alpha-\delta)\delta P_x}{2J},\quad
 D_x=3-17x/9,\quad P_x=(2-8x/9)(1-x),\quad
 J=(\alpha-\delta)D_x+\delta P_x.
 \tag{7}
\]

这是经过same-source witnesses、whole-slot spikes、原Theta系数和strict widths的实际count。
All-error I、q=0也可用，不虚构positive prime factor。
Floor独立取R=1；d_min<=d<=1/2非floor用actual no-slot count1-2delta/3。
这些pointwise partitions仅在whole-bin move后使用；不分别延拓contour-dependent sets。

## 5. 连续端点certificate及正确参考幂

442原Mellin记账给

\[
 E_\sigma(d)=a-\sigma+h(z_0-1/6)-a l_y-\ell/2+q\ell
    +d(R+\delta/2-z_0).
\]

准确改写为

\[
 E_\sigma(d)=K_\sigma+(1/2+\ell)\delta+\ell q-h(1-R)
 +(d-h)(R+\delta/2-z_0),\quad
 K_\sigma=2/3+\ell+b/6-\sigma.
 \tag{8}
\]

沿sigma(ell)=11/12-ell/4，有K=-1/4+5ell/4+b/6。
旧ell0=1/6、sigma0=7/8、h0=13/16的纯代数endpoint证书可直接验证：
令y=1/2-x、v=51+41y，则

\[
 10368vJ(-E_0)=
 (3+5y)\{(4v\delta-79)^2+49\}
 +4y\{4v\delta[(1+3y)(15+32y)\delta+9-13y]+265+3485y\}.
 \tag{9}
\]

y∈[0,1/2]、delta>=0使各显示项非负，9-13y>=5/2，
v<=17(3+5y)、0<J<=5/2，因此-E0>=49/440640。
这是连续区间的完成平方证明，不是网格实验。
另2D_x-3P_x=4x(11-6x)/9>=0给
1-delta<=R_*<=1-2delta/3。
对同一delta,q,R_*，新endpoint精确差为

\[
 E_{\sigma_1}(h_1)-E_{7/8}(h_0)
 =t_0(-1/4+\delta+q+3R_*/2)\le(5/3)t_0.
\]

故实际pairs统一满足

\[
 \boxed{E_{\sigma_1}(h_1;R_*)\le-m_{ad},\quad
 m_{ad}=49/440640-5t_0/3=307/11016000>0.}
 \tag{10}
\]

该margin已相对C(sigma1)。变化式包含-sigma′=1/4，不能再扣1/80000。
比较C(beta_*)只需E_beta=E_sigma1-Delta1，得到更强余量。
固定旧sigma0的导数则是-1/2+delta+q+3R*/2；换reference恰补t0/4，结果相同。

## 6. 全moderate d的实际包络

d_min=1/100。
Selected nonfloor范围1/2<=d<=h1中，(8)的slope
R_*+delta/2-z0>=33/50-delta/2>0，故endpoint(10)控制全部d。
这个uniform包络不要求同一个pair实际出现在h1 dyad。
Floor delta0=1/50、R=1、q<=delta0/2的slope为67/100，直接得

\[
 E_{\sigma_1}(h_1)\le-7/1200+(32/25)t_0=-4327/750000.
 \tag{11}
\]

No-slot中间d_min<=d<=1/2取共同R=76/75-2delta/3，涵盖floor。
Slope101/150-delta/6>0，故只查d=1/2。
固定d时沿sigma(ell)的导数为13/50+delta/4+q<=177/200。
旧中间纯代数界-49/14400因此变为

\[
 E_{\sigma_1}(d)\le-49/14400+(177/200)t_0
 =-120907/36000000<0.
 \tag{12}
\]

每个physical slot仍在full correction中；no-slot只说未将prime factor用于row moment。
向h1+zeta扩时所有slope可保守界为2。固定

\[
 \zeta=m_{ad}/32=307/352512000
 <\min\{2521/120000,1-h_1\}.
 \tag{13}
\]

443的actualsupply保留，增加成本<=2zeta=m_ad/16。
于是全部d∈[d_min,h1+zeta]在real损失之前至少有
15m_ad/16=307/11750400的统一saving，相对C(sigma1)，
floor与中间余量更大。外d<d_min和d>h1+zeta分别由442(16)(17)支付。

## 7. 统一合同与剩余continuation

固定K后，有限2^K subsets为常数，amplitude/witness/physical dyad multiplicities
按原条款只花任意小幂；所有变量共用一个cumulative T1/2 allocation。
Central附加real损失为
(16-6l_y)e+(1+d)epsilon_c+d epsilon_d+epsilon_p，
其系数在上述compact range有target-independent界。
先选count/rounding/moment loss与capacity decrement，再选uniform mesh、fixed K/windows；
再选amplitude宽度、prime preliminary powers、e及detector-dyads的pre-saturation参数。
可将所有central real损失、multiplicity与逆normalizer成本总和压到m_ad/4以下。
不能在K之后反过来缩需要先确定的moment mesh；固定K后才选依赖min ell_i的幅度小loss。

442的small-row margin为172249/2000000，large rows可预定更大margin。
于是固定预留某个m_np>0，在target确定及固定internal orders之后，存在有限A_eta、B_eta，
对原physical nonprincipal sum有

\[
 \left|\frac{I_{modified}-\mathscr P_\eta}{c_S A_T}\right|
 \ll_{\eta,N}Z^{C(\beta_*)-m_{np}}(1+T_1)^{A_\eta}
                 +Z^{B_\eta}T_1^{-N}.
 \tag{14}
\]

A_eta、B_eta不随后选external N改变。Detector literal height条件须先固定ceiling，
再选tau；principal合同另由442(13)合并。Physical函数不含T1，
最后late-height closure与continuation在445给出。

完整独立读源推导见[central联合误差报告](../reviews/2026-10-07/hybrid-central-error-slots-and-high-saving.md)。
这里的actualhigh新推导仍相对于列出的[R]；没有调用AF比例来减少坏行数，
也没有把 finite rational audit 当成无限分析或Lean证明。
