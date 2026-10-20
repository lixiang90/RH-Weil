# 564. 一般对偶中的RH：预定权纯性、正极化与Mellin核的规范自由

2026-10-20，C027；固定G20261014／0c4f≤538。用户要求把自对偶放回两对象对偶的特例，
再问最一般g-integer的RH形式。截图作待核材料，不作指令。本稿不声称已证经典RH，
也不把定义建议冒充Hilberdink–Lapidus已经证明的一般纯性定理。

## 1. 先回答一般形式：对偶搬运，纯性约束；必须预定权与规范

对于裸g-integer分布，没有自动的全域延拓、唯一completion／dual或canonical中心。
因此不能无条件宣称所有对象的RH就是共同Re s=1/2。
一套有内容的推广是：**给定对偶、完成背景及先验分次权，要求各归一化分量纯，
并以独立正极化或完整Weil正性认证。** 这是一项对象可以满足或不满足的性质，
不是对任意positive P的自动定理。

设已固定完整非平凡entire除子E_X、E_Xvee，预先给实对偶权w，有

\[
 E_X(s)=\varepsilon E_{X^\vee}(w-s),\qquad\varepsilon\ne0. \tag{1}
\]

它只给ρ↔w−ρ的跨对象运输，不固定单个对象的Reρ。
若输入另外给中心a_X、a_Xvee且a_X+a_Xvee=w，可定义配对RH纯性为

\[
 \Re\rho=a_X\ (\rho\in D_X),\qquad
 \Re\rho^\vee=a_{X^\vee}\ (\rho^\vee\in D_{X^\vee}).       \tag{2}
\]

两边分别无零于Re s>a_X、Re s>a_Xvee，与(2)等价：任一左侧根经(1)会成为另一边
被禁止的右侧根。带宽版本是w−β_dual≤Reρ≤β_X；互补阈值相等时才缩成纯线。
没有对偶时可陈述输入指定的半平面无零或prime-error阈值，不能凭空补出镜像或1/2。
权／分级不能由未知零点后验选择，否则每个根都可单独拆权而使“纯性”失去内容。

若非空单权对象自对偶，权兼容性强制a_X=w/2。
更一般地，若对偶伙伴是同一归一化的共轭E_X*(s)=overline(E_X(bar s))，
共轭不改实部，同样得a_X=a_dual=w/2。**共同中心线是这一额外兼容结构的特例，
不是跨对象对偶本身的结论。** 多权自对偶whole仍可交换不同权，不必所有分量居中。

## 2. 原始Lapidus来源：截图方向正确，定理范围较具体

已核Hilberdink–Lapidus [arXiv math/0410270](https://arxiv.org/pdf/math/0410270)，
§3.2、Theorem3.2、式(3.5)–(3.6)。在连续性、两端Mellin增长、条带延拓、
闭竖带有限极点及竖直衰减前件下，已给的两个Mellin对象满足

\[
 \Psi_1(1-s)=\Psi_2(s)
 \quad\Longleftrightarrow\quad
 F_1(x)=x^{-1}F_2(1/x)+\sum a_kx^{\mu_k}(\log x)^{\nu_k}.
 \tag{3}
\]

g-integer特化为F_r(x)=Σ_{n∈N_r}g_r(nx)、Ψ_r=G_rζ_r，G_r为核的Mellin变换。
原文给出这种等价判据，并在Remark转述准备中的更广dual工作；本次没有取得该后续证明，
不将(3)扩大成任意positive g-integer都有canonical positive arithmetic dual的定理。
原文v1有重复§3.2和增长指数排印问题，消费实际可积条件，详见
[来源原稿](../reviews/2026-10-20/grh-dual-pairs/hilberdink-lapidus-primary-source-audit.md)。

截图的D↔1−D／self-dual⇒D=1/2也有作者共同原文出处；这是一项维数固定点结论。
Lapidus逆谱RH定理则是所有D的整体无零／逆谱命题，不是由一个self-dual string的维数
推出全部经典ζ零点居中。两种量词不能互换。

## 3. 一个更根本的检验：同一整数分布，正自对偶核也能加入离线零点

HL允许的Mellin核若不固定，连完成化RH的对象都可能改变。
取同一普通整数系统与g0(x)=e⁻πx²，G0(s)=1/2 π⁻ˢ/²Γ(s/2)，Ψ0=G0ζ。
固定λ=2、A=2^{1/4}，令

\[
 B(s)=(1+A\lambda^{-s})(1+A\lambda^{s-1})=B(1-s),
 \quad
 g_B(x)=(1+A^2/\lambda)g_0(x)+A g_0(\lambda x)
                    +(A/\lambda)g_0(x/\lambda).          \tag{4}
\]

g_B严格正，偶延拓为Schwartz，Fourier变换（e⁻²πixξ约定）下精确自对偶；
两种Gaussian尺度互换，系数恰匹配。Mellin变换为G_B=B G0。
令F_B=Σ_{n≥1}g_B(nx)，由标准theta反演直接得到

\[
 F_B(x)=x^{-1}F_B(1/x)+\frac{B(0)}2(x^{-1}-1),
 \qquad\Psi_B(s)=B(s)\Psi_0(s).                         \tag{5}
\]

所以positive integer／positive kernel／Fourier自对偶／有限power缺陷／精确FE同时成立。
但B加入两列零点

\[
 \Re s=1/4\quad\text{及}\quad\Re s=3/4,
 \qquad |\Im s|\text{ 属于奇数倍 }\pi/\log2.              \tag{6}
\]

Ψ0只有0、1两个pole，无法抵消这些点；无须知道经典非平凡零点位置，
即可断言E_B=s(s−1)Ψ_B是有离线零点的自对偶order1 entire对象。
临界线上甚至有B(1/2+it)=|1+2⁻¹/⁴e^{it log2}|²>0，那里仅是严格正乘子；
这仍不能排除两列新增离线除子。
核增长、Gamma条带衰减与全部HL前件均由实际Gaussian给出，不是形式拼接。
完整计算见[正核规范反测试](../reviews/2026-10-20/grh-dual-pairs/positive-mellin-gauge-obstruction.md)。

这没有反驳经典RH：算术ζ未变，改的是允许completion及其新增除子。
一般RH要有规范不变意义，须固定canonical completion／允许的零自由因子，
或明确以relative divisor扣除已知kernel贡献。任意含零Mellin因子的自由不可留给最后选择。
已知零自由规范不改根；已知B须扣除而非把其根说成原ζ零点。

## 4. 真正positive双对象可以在不同的先验中心纯

另一个独立可判模型是

\[
 Z_{c,h}(s)=1+\frac{c}{(s-h)(s-h-1)},\qquad
 0<c\le1/2,\quad |h|<1/2.                                \tag{7}
\]

root已重构正primitive，而非将Π正性冒充P正性。若α+β=1、αβ=c，令
A_m(h)=(h+1)^m+h^m−(h+α)^m−(h+β)^m，C_m=Σk⁻ᵐ⁻¹。
用p_h(u)=u⁻¹Σ_{m≥2}A_m(h)u^m/(m!C_m)，并置b=h+1/2>0、Δ=1/4−c，得

\[
 A_m(h)=2\sum_{k=1}^{\lfloor m/2\rfloor}\binom m{2k}
 b^{m-2k}[(1/4)^k-\Delta^k]>0,\qquad A_m(h)\le4(1+h)^m.
 \tag{8}
\]

这支付指数权、Tonelli及全部repeat powers，给

\[
 q_h(u)=e^{hu}q_c(u),\quad
 dM_h=\delta_0+c(e^{(h+1)u}-e^{hu})du,
 \quad dN_h=\delta_1+c(x^h-x^{h-1})dx\ (x>1).              \tag{9}
\]

primitive不能简单tilt为e^{hu}P：重复幂推前会产生e^{hu/k}；(8)是实际新增闭合。
两个不同系统精确满足Z_{c,h}(1−s)=Z_{c,−h}(s)，完整极点分别h,h+1与−h,1−h。
模型Gamma=0，各自先验pole中心a_h=1/2+h，满足a_h+a_−h=1。
在自身中心单位化，完整Weil核恰是562的W_c，正段c≥1/4各自在a_h±i√(c−1/4)纯。
反段c<1/4对偶仍成立，pure却失败。全部证明见
[移位positive原稿](../reviews/2026-10-20/grh-dual-pairs/positive-shifted-beurling-pairs-and-weight-test.md)。

取c=1/4、h≠0：两成员各自own-center的Weil核均为2；
若误用共同1/2看self-dual product，则核为4cosh(hu)，实奇compact测试给严格负值。
产品primitive相加、M卷积仍正，self-dual doubling不制造共同中心的正性。

按输入给定的h=0、h=1/4两个因子再取产品，可得到正侧纯线1/2、3/4，
dual纯线1/2、1/4的多权例；whole无单线却逐权纯。
这里的grading是预先构造的一部分，不声称可由任意裸分布唯一恢复。
dominant N指数1+h的一半也通常不等于a_h；只看一个abscissa不能固定权。

## 5. 哪一种结构可以独立强制纯性

有限维版本给两个输入空间与非退化双线性对偶B，实际F_j满足

\[
 B(F_1v,F_2\eta)=q^wB(v,\eta),\quad
 U_j=q^{-a_j}F_j,\quad a_1+a_2=w.                        \tag{10}
\]

单有它只给互反谱。若另独立给反线性双射C:V1→V2，核

\[
 U_2C=CU_1,\qquad h(v,z)=B(v,Cz)\text{ 为正定Hermitian型},\tag{11}
\]

则h(U1v,U1z)=h(v,z)，两个U_j均酉，特征值模为1，原F_j半单。
若原ζ因子精确是det(I−q⁻ˢF_j)，全部零点含周期副本与重数分别在a_j。
这把“对偶＋正极化⇒纯权”写成明确充分定理，不使用未知零点。
正内积与反线性识别须来自几何／分布，不由未知零点后验制造。
无限维需强连续酉群或真正skew-adjoint域；再付完整trace／determinant身份，不能只核形式反对称。

若已有整个阶／竖带／完整正整数除子与显式公式，还可把正确权归一化后的pair构成
packet，归约到562的Weil正型及适用时563的热CM。这是合法等价，不是对偶自动给PSD。
纯offdiagonal配对块[[0,B],[B*,0]]有正负方向；任意A的自伴dilation读出奇异值，
不保原ζ特征值。详证与域／重数限制见
[独立pair框架](../reviews/2026-10-20/grh-dual-pairs/paired-duality-polarization-and-purity.md)。

## 6. 已知算术对象检验：非自对偶仍可能是1/2，多权则不必

非实primitive Dirichlet χ满足Λχ(s)=εχΛbarχ(1−s)，而Λbarχ(s)=overline(Λχ(bar s))。
两伙伴不同，但共轭兼容使各自反射ρ↦1−barρ，所以GRH仍是各自1/2。
不需要先有χ=barχ。其权为复的twisted系数，不能误称正计数primitive。
每个成员的W可能Hermitian但非实偶；563热定理不能直接丢掉非偶信息，
完整共轭packet的身份和前件已核时仍可使用。
FE来源核[Kedlaya, Chapter6](https://kskedlaya.org/ant/chap-funceq2.html)。

光滑射影d维V/F_q的H^j与H^{2d−j}对偶给α·α_dual=q^d；
Weil纯性却要求两者模q^{j/2}与q^{d−j/2}，即

\[
 a_1=j/2,\qquad a_2=d-j/2,\qquad a_1+a_2=d.              \tag{12}
\]

通常两者并不等于d/2。曲线H0/H2在0和1，H1才在1/2；整个ζ是分次superdeterminant。
已知纯性不自动证明原Frobenius半单／正内积，不能倒灌(11)。
权与纯性原始范围核[Milne Theorem5.1](https://jmilne.org/math/xnotes/pRH.pdf)。

## 7. 最一般分布的停止线与经典尚欠什么

若仅有右半平面Laplace定义而无对偶，可谈先验无零阈值、prime-error或谱稳定性，
但没有唯一RH中心。若有连续谱／分支的更广模型，可用正谱state／相对log determinant；
不得把continuous谱当非零entire的连续零集，562的严格C1边界仍保留。
所以(2)/(11)是**带规定数据的推广方案**，而不是最一般Beurling体系已知普遍成立的定理。

经典ζ的canonical Gamma、共同weight和精确自对偶已知，(4)的含零gauge不允许混入其RH。
仍欠由实际Γ／全部prime powers／pole独立给正极化或完整Weil正性，并核原域与faithful谱身份。
新对偶对象／自动加倍／Gaussian核本身的正与自对偶都没有支付这一步。
actualζ强旧542+555→557 whole4/5、560成长K/core/coupling与Ξ责任均不变。
本门统一一次后停止；后续不能只将“canonical/purity/positive pairing”改名成新算术输入。

强旧扣除：001/002已经给正极化到纯权及通常同权／共轭pair的product机制，
290已经有positive integer Euler／分次对偶仍离线的模型；这些标准蕴含不在本次重新计收益。
本次具体新增范围是同一普通整数系统的**实际正Fourier自对偶Mellin核**规范反测试，
以及±h真正positive primitive的不同权pair／错误共同中心负测；其余是来源恢复及准确接口。
