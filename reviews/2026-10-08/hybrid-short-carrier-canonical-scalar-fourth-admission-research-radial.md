# 原 short-carrier 比值方差的 canonical scalar 四矩准入

2026-10-08。radial_review。基线为已提交
2681813154243e10cf4602f4e88514355060d379。
只新增本研究源；全部旧笔记、研究、论文、输出、math与Git冻结。
[T] 下述原对象准入与cutoff-completion恒等式；
[O] 同一正高度窗口上的canonical scalar四矩有效上界。
本稿尚待其他作者独立全文审查。

新增付款不是另给一个小Q合同：原R_+的共享空间窗口可以用两个
真实t-Fourier乘子处理，一个是L² contraction，另一个的L⁴
norm由原窗口的总变差统一控制。因此可把完整short-carrier
ratio upper合法归约到**一个原系数的、未移位的scalar high
Dirichlet polynomial四矩**，没有额外增长的loglog窗口费用。
这使未移位Λ*Λ的Möbius完成成为确切的充分算术接口，
但没有自动支付该接口的正高度mean-square。

## 1. 固定原对象与输入绑定

保留X=T/(2pi)、ell=log X、d=floor(X ell)、I=[−ell/2,ell/2]，
原even C² taper phi、a_ell=ell^−1||phi||₂²及真实zero extension。
0≤phi≤1，原uniform bounds为
\[
 \|\phi'\|_1+\|\phi''\|_1=O_\phi(1),\quad
 \|\phi\|_1=O(\ell),\quad a_\ell\ge c_\phi>0.
\]
由||phi'||∞≤||phi''||₁，还得
\[
 V_\ell:=\|(\phi^2)'\|_1=O_\phi(1),\qquad
 \|(\phi^2)''\|_1=O_\phi(1).                       \tag{1}
\]
两端的零延拓仍保留；所有频率乘子在实线上定义。

| 冻结输入及实际使用范围 | canonical LF SHA-256 |
| --- | --- |
| [472全部四阶P准入](../../notes/472-original-short-carrier-fourth-compression-and-ratio-variance.md) | 9856885e932a892cf7c33ece82f430c2ec13004555eb52da2f1e8b1ec6bb2683 |
| [完整half-ratio及uniform cross](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md) | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 |
| [原half-Gram及Möbius identity](../2026-10-07/hybrid-high-parity-gram-and-mobius-completion-research-radial.md) | 3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2 |
| [239既有one-factor Vaughan范围](../../notes/239-vaughan-quotient-first-centering-and-divisor-kernel.md) | b35398ecdfbe65ce2ea04856a5e66f6676d61cc109b3de48e855b514db0cfa20 |
| [240既有adjacent divisor范围](../../notes/240-mobius-pullback-adjacent-divisor-dispersion.md) | 1867e490fed07598e4f6c44952352d2c3a7a0dc4b066b6c1720e8a96d3a0ed8a |

以下不是重写239/240的Vaughan合成或另一个abstract Gram模型。
新的步骤在更前面：实际shared-profile ratio列到canonical
未移位scalar四矩的Lp准入。它只是一侧upper归约，不能把两个
观测量称为精确相等，不能从反方向推断算术难度相同。

定义
\[
 b_p=\frac{\log p}{a_\ell\ell\sqrt p},\quad
 P_H(t)=\sum_{\sqrt X<p\le X}b_p e^{it\log p},\quad
 \mathfrak m_T=\sum_{\sqrt X<p\le X}b_p\ll\sqrt X/\ell.       \tag{2}
\]
这些仍是原genuine sharp primes，没有重选phase或系数。

令
\[
 A=-\sum_{\sqrt X<p\le X}b_pM_\phi R_{\log p}M_\phi,\quad
 G=A^*A,\quad D_+=\sum_p A_p^*A_p,\quad R_+=G-D_+ .
\]
R_s f(u)=f(u+s)，G、D_+、R_+作用在I_+。
准确有D_+=M_{d_+}，其中
d_+(u)=phi(u)² sum_p b_p² phi(u−log p)²；
保持原w_T(u)=d_+(u)+d_+(−u)和
S_T=ell^−1 int_I w_T²。这是原genuine same-prime中心。
原carrier E_sigma e_k=ell^−1/2 1_I e^{it_k u}，
t_k=sigma+k eta，eta=2pi/ell，sigma∈[T,T+s]，
s=T/sqrt ell，0≤k<d。
定义r_sigma=||R_+E_sigma||HS²/d，保留该完整非负方差。

## 2. 两个准确的t-Fourier乘子：没有拆掉shared window

对有界频率函数m，T_m是关于实变量t的Fourier乘子，
T_m(e^{itxi})=m(xi)e^{itxi}。
对u∈I_+定义
\[
 m_{1,u}(\xi)=\phi(u-\xi)^2,\quad
 m_{0,u}(\xi)=\phi(u+\xi),\quad
 P_u=T_{m_{1,u}}P_H
     =\sum_p b_p\phi(u-\log p)^2 e^{it\log p}.              \tag{3}
\]
这里的P_u不是新的prime family；它是同一个P_H的固定物理窗过滤。

准确令
\[
 z_u(t):=T_{m_{0,u}}\bigl(\overline{P_u}\,P_H\bigr)(t).
\]
逐个有限频率展开即得
\[
 z_u(t)=\sum_{p,q}b_pb_q\phi(u-\log p)^2
        \phi(u+\log(q/p))e^{it\log(q/p)},                  \tag{4}
\]
因而
\[
 (G E_\sigma e_k)(u)
  =\ell^{-1/2}1_{I_+}(u)\phi(u)e^{it_k u}z_u(t_k).          \tag{5}
\]
(4)包含p=q。其diagonal是
phi(u) sum_p b_p² phi(u−log p)²，正好恢复D_+，没有更换中心。
若要R_+列，只需从z_u减去这一个原diagonal。

全局finite polynomial不属于L⁴(R)。下文不会对它直接使用
全实轴Lp norm；只对height-cut后的真正Lp函数使用乘子界，
其余由C² convolution tails严格付款。

## 3. uniform BV到L⁴的自证及C²局部化

记H为Hilbert transform，其Fourier符号为−i sign xi。
先对real Schwartz f，g=f+iHf的Fourier支撑在非负半轴，
四次卷积在零点为零，且g⁴可积，所以int g⁴=0。
其实部给
\[
 \int(Hf)^4=6\int f^2(Hf)^2-\int f^4 .
\]
Cauchy后解二次式，得到
\[
 \|Hf\|_4\le(1+\sqrt2)\|f\|_4.                             \tag{6}
\]
Schwartz情形的Hf在无穷远为O(1/|t|)，上述积分良定义；
Fourier四次卷积的零点只可能来自四个零频率，集合测度为零。
然后用稠密延拓。

对complex f，把real Re(e^{itheta}f)的(6)对theta积分；
int_0^{2pi}|Re(e^{itheta}z)|⁴ dtheta=(3pi/4)|z|⁴，
所以同一个常数仍适用，不需要多乘一个实虚部triangle费用。
半轴projection Pi_+^F=(I+iH)/2的L⁴ norm因此至多
\[
 C_4:=1+1/\sqrt2 .
\]
频率端点平移是物理t的unit modulation，norm不变。

对compact W^{1,1} multiplier m，
m(xi)=int m'(v)1_{xi>=v}dv。强Lp积分给
\[
 \|T_m f\|_4\le C_4\|m'\|_1\|f\|_4.
\]
应用(1)、(3)，得到uniform于u
\[
 \|T_{m_{1,u}}\|_{4\to4}\le N_\ell:=C_4V_\ell=O_\phi(1),
 \qquad \|T_{m_{0,u}}\|_{2\to2}\le1.                       \tag{7}
\]
这是boundedness准入常数，不声称是最优sharp norm。

两乘子的convolution kernel
K_m(v)=(2pi)^−1 int m(xi)e^{ivxi}dxi，由(1)二次分部积分给
\[
 |K_m(v)|\le C_\phi/|v|^2,\quad |v|\ge1,                  \tag{8}
\]
uniform于u。它们每个T的kernel确实在L¹中；near v=0可用
O(ell)、middle可用O(1/|v|)，L¹可能有log ell增长，
但(7)没有由这个粗L¹增长推出乘子norm。下一节只对远tail用(8)。

## 4. 仅O(T)正高度的guard：完整局部乘子费用

取
\[
 J_0=[T,\,2T+s],\quad J_1=[T/2,\,3T],\quad
 J_2=[T/4,\,4T],\quad
 \mathcal M_T=\frac1T\int_{J_2}|P_H(t)|^4dt.               \tag{9}
\]
T足够大时s<T/2，J_0至J_1外有至少cT距离，
J_1至J_2外也有至少cT距离。没有跨过原height 0相干峰。

把P_H准确拆为P_H1_J2及其补集。
(8)及||P_H||∞=mathfrak m_T给，对t∈J_1，
\[
 |T_{m_{1,u}}(P_H1_{J_2^c})(t)|
       \le C_\phi\mathfrak m_T/T .
\]
对其余真正L⁴函数使用(7)，故
\[
 \|P_u\|_{L^4(J_1)}
 \le N_\ell T^{1/4}\mathcal M_T^{1/4}
                         +C_\phi\mathfrak m_T T^{-3/4}.   \tag{10}
\]
所有u使用同一个J_2；没有重选profile或逐u选择好高度。

准确拆overline(P_u)P_H在J_1内外。因
||P_u||∞≤mathfrak m_T，(8)给t∈J_0的外部tail
≤C_phi mathfrak m_T²/T。内部用L² contraction和Hölder：
\[
 \begin{split}
 T^{-1/2}\|z_u\|_{L^2(J_0)}
 &\le T^{-1/2}\|P_uP_H\|_{L^2(J_1)}
                       +C_\phi\mathfrak m_T^2/T\\
 &\le N_\ell\mathcal M_T^{1/2}
   +C_\phi\frac{\mathfrak m_T}{T}\mathcal M_T^{1/4}
   +C_\phi\frac{\mathfrak m_T^2}{T}.
 \end{split}                                             \tag{11}
\]
这对每个finite T和全部u成立，无scalar fourth bounded前件。
两个远端费用分别为O(X^−1/2 ell^−1)及O(ell^−2)，
第一项还乘显示的M_T^(1/4)。若M_T增长，不能将所有cross
未经检查改写为additive o(1)。

## 5. sigma+k的准确正密度与完整ratio upper归约

定义真正平均的height density
\[
 \omega_T(t)=\frac1{sd}\sum_{k=0}^{d-1}
                  1_{[T+k\eta,\ T+s+k\eta]}(t).
\]
准确有int omega_T=1，其支撑在J_0，且
\[
 0\le\omega_T(t)\le\frac1{d\eta}(1+\eta/s).                \tag{12}
\]
这是interval overlap count，未把discrete carrier偷偷换成
continuous projection。也不删除two endpoint strips。

由(5)、Fubini的非负性，
\[
 \operatorname{avg}_\sigma\frac{\|GE_\sigma\|_{\rm HS}^2}{d}
  =\frac1\ell\int_{I_+}\phi(u)^2
                      \int\omega_T(t)|z_u(t)|^2dt\,du.    \tag{13}
\]
偶窗给ell^−1 int_I+phi²=a_ell/2。写
\[
 A_T=\frac{a_\ell T}{2d\eta}(1+\eta/s),\quad
 E_T(M)=N_\ell\sqrt M+
 C_\phi\frac{\mathfrak m_T}{T}M^{1/4}
                    +C_\phi\frac{\mathfrak m_T^2}{T}.
\]
(11)–(13)严格给finite、growth-uniform的实际估计
\[
 \operatorname{avg}_\sigma\frac{\|GE_\sigma\|_{\rm HS}^2}{d}
       \le A_T E_T(\mathcal M_T)^2.                       \tag{14}
\]
A_T保持exact floor与overlap损失；若M_T增长，不把它的
o(1) relative变化免费当成additive o(1)。

原half-Gram的uniform D_+R_+ cross为O(ell^−1)，故
\[
 \boxed{\operatorname{avg}r_\sigma+\frac{S_T}{2}
       \le A_T E_T(\mathcal M_T)^2+C_\phi/\ell.}           \tag{15}
\]
全部physical窗口、原same-prime center以及原k采样保留。
这里不是把q_sq换成完整实线residual。

若将来实际证明M_T=O(1)，(15)便支付avg r=O(1)，
472同时把真实q及全部16词传至同一个合法short carrier。
若a_ell→a、limsup V_ell≤V，并使用冻结原profile的S_T→S_psi，
则还给具体充分upper
\[
 \limsup\operatorname{avg}r_\sigma
 \le\frac a2(C_4V)^2\limsup\mathcal M_T-\frac{S_\psi}{2}.   \tag{16}
\]
这只是有前件的实际一侧估计。C_4V是安全Lp常数，不是已付
small-r算术目标，也不是已证sharp比例。

可以由(15)继续保留所有显示的growth费用，不能只引用(16)
然后对未证bounded M_T进行优化。
本轮真正新付款是完整shared-profile的canonical scalar准入，
不是单纯给未知r重新命名。

## 6. canonical Λ列：scalar proper powers的L⁴小量

定义原同一normalizer、同一sharp high cutoff的
\[
 \widehat P_H(t)=
 \frac1{a_\ell\ell}\sum_{\sqrt X<n\le X}
          \frac{\Lambda(n)}{\sqrt n}e^{it\log n}.
\]
它与genuine P_H之差只包含实际proper powers。
对平方，写
\[
 P_2(t)=\sum_{X^{1/4}<p\le X^{1/2}}a_p e^{2it\log p},
 \quad a_p=\frac{\log p}{a_\ell\ell p}.
\]
Chebyshev、partial summation给
\[
 \sum a_p^2\ll X^{-1/4}/\ell,\qquad \sum p a_p^2=O(1).
\]
P_2²按base pq展开，primitive prime factorization的重数至多2；
weighted MV因此在J_2给
\[
 \frac1T\int_{J_2}|P_2|^4
 \ll(\sum a_p^2)^2+\frac1T(\sum p a_p^2)^2
 \ll X^{-1/2}\ell^{-2}+X^{-1}.                            \tag{17}
\]
frequency是2log(pq)，仍是base pq≤X的间距；
不错误地按原n=p²q²≤X²支付MV。

对k≥3，每个p^k>sqrt X且p^k≤X。Chebyshev给
sum_{p>X^(1/(2k))} log p p^(-k/2)
≪X^(-(k−2)/(4k))，常数uniform于k≥3。
k≤ell/log2，故
\[
 \sup_t\left|\frac1{a_\ell\ell}
     \sum_{\substack{k\ge3\\\sqrt X<p^k\le X}}
       \log p\,p^{-k/2}e^{ikt\log p}\right|
       \ll X^{-1/12}.                                    \tag{18}
\]
因此在normalized L⁴(J_2,dt/T)中
\[
 \|\widehat P_H-P_H\|_4=O_\phi(X^{-1/12})=o(1).            \tag{19}
\]
这里是norm差，未在未知增长的fourth上展开并声称additive o(1)。
一个实际bounded upper可先对widehat P_H付款，再由(19)迁回
P_H；到那时scalar fourth差才可作additive o(1)。

## 7. 现在合法的未移位Möbius完成：两个cutoff均须保留

令Y=sqrt X，Lambda_H(n)=Lambda(n)1_{Y<n<=X}，
c_H=Lambda_H*Lambda_H。准确有
\[
 \widehat P_H(t)^2=\frac1{(a_\ell\ell)^2}
             \sum_{X<n\le X^2}\frac{c_H(n)}{\sqrt n}n^{it}. \tag{20}
\]
这是一个未移位的canonical coefficient family；
此前shared spatial windows已由(3)–(15)一侧准入付款，
不需要再用多个独立frequency shifts重造character合同。

完整系数identity
Lambda*Lambda=mu*log²−Lambda log
由Re s>1下(−zeta'/zeta)²=zeta''/zeta−(zeta'/zeta)'
逐系数得到。令L=Lambda1_{n<=Y}、U=Lambda1_{n>X}，
Lambda_H=Lambda−L−U。在X<n<=X²，L*L=U*U=0，因而
\[
 \boxed{\ c_H(n)=
 \sum_{d\mid n}\mu(d)\log^2(n/d)-\Lambda(n)\log n
 -2\sum_{\substack{ab=n\\a\le Y}}\Lambda(a)\Lambda(b)
 -2\sum_{\substack{ab=n\\a>X,\ b>Y}}\Lambda(a)\Lambda(b).\ } \tag{21}
\]
最后一项在n<=X^(3/2)为空，却在整个top-product range不可删。
例如X=16、n=95=5·19，full Lambda*Lambda贡献2log5 log19，
low term为0，最后upper-cutoff term恰将它全部删除，
原high<=16的c_H(95)=0。
若只用mu*log²与low correction，就已经改变原sharp列。

因此新的实际充分算术任务可以准确写为
\[
 \frac1T\int_{T/4}^{4T}
  \left|\sum_{X<n\le X^2}\frac{c_H(n)}{\sqrt n}n^{it}\right|^2dt
       \le B_\phi (a_\ell\ell)^4,\quad B_\phi=O(1),         \tag{22}
\]
或证明足够好的explicit有限upper，再通过(15)保留全部费用。
(21)中的Möbius、low及large-factor项必须共同估计，
不能逐项取绝对值后假称完成了net cancellation。
它也不是ordinary Mertens prefix、任意coefficient sieve，
或原character-row amplified合同的免费特例。

本稿在内存中用symbolic prime logarithms，X=16、Y=4，
对17<=n<=256的240个系数逐一复核(21)，全部exact通过。
它只核Dirichlet卷积代数，不认证(22)或任何素数渐近；
没有生成或覆盖旧audit/output。

## 8. 新归约的进展与仍未付算术

(15)给实际原carrier、完整same-profile ratio的一侧upper，
其外部对象是一个原sharp scalar high polynomial四矩。
窗口Lp费用uniform，height guards均为O(T)正高度；
不用放大到X²，不包含height0的正相干峰。
(17)–(21)又完整支付proper-power准入并明确了原两个sharp
factor cutoff在Möbius完成中的实际correction。

这比旧239/240的形式Vaughan lift多付了原shared window至
canonical未移位scalar任务的analytic接口，却没有证明
Möbius-divisor net mean-square的新χ或实际O(1)。

直接weighted MV对genuine P_H²仍只给
M_T≪1+X/ell²：产品长度至X²，
sum_n n|sum_{pq=n}b_pb_q|²≪(sum_p p b_p²)²≪X²/ell²。
这只是已有raw-op/second量级的粗upper，不能称为四矩付款。
已有zero-free prefix幂估计也不能免费提供(22)；
原inverse/marked/plain character合同的对象、导子、height与
实际coef归属仍须逐项证明，本文没有引用它们。

下一真正算术目标已经明确为(21)全部corrections保留后的
正高度canonical mean-square(22)，或在(15)里保留exact费用的
更强一侧预算。该目标目前为[O]。
没有得到新实际比例、无零边界、field变化或RH证明。
