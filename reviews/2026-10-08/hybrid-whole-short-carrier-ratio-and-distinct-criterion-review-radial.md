# 原短载波比值方差与四全异判据：独立全文审查

2026-10-08。审查者 radial_review。结论：**限定 PASS**。
逐行读取并复算被审稿全部276行，未发现阻断。
本次只新增审查，不修改作者源、冻结笔记、math、脚本、输出或 Git。

被审对象：
[hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md)，
canonical UTF-8 LF SHA-256
**c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53**，
11396 bytes，276行。统一CRLF及lone CR为LF，不trim或重写EOF。
相对此前6bd03版本，最终稿只在输入表添加冻结carrier源；全部数学相同。

通过范围是：原scalar sharp-prime对象、真实有限P、固定原taper和
normalizer下的短起点平均、全部16个有序H/L四词的共同good set、
实际q与完整half-ratio方差的增长统一双向比较，以及将来合法
算术upper的共同选点接口。没有支付完整ratio方差的有效算术upper，
没有新的实际零点比例、无零边界或RH证明。

## 1. 输入绑定与核对范围

| 已实际读取的输入 | canonical LF SHA-256 |
| --- | --- |
| [anchored raw whole-P平均源](hybrid-anchored-carrier-averaged-fourth-projection-gap-research-radial.md) | c0e874ab9061982c8ef4365c8e9313eeac77eeddb756dc0b455cab3349f99dd8 |
| [原finite-band / two-cross源](../2026-10-07/hybrid-one-three-finite-band-admission-research.md) | bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f |
| [half-Gram及diagonal cross源](../2026-10-07/hybrid-high-parity-gram-and-mobius-completion-research-radial.md) | 3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2 |
| [465加权二矩](../../notes/465-centered-high-square-joint-fourth-budget.md) | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 |
| [456重复union](../../notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md) | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 |
| [471完整四全异对象](../../notes/471-original-principal-subtraction-and-signed-four-distinct-target.md) | a66dcc18606b59ac0aa1a879f64f6f7dae4a3278981e5fbc2c94190efa3a3ef6 |

审查对象是twisted的新criterion稿。表中anchored源由本审查者提出，
其独立验收须由其他作者承担；这里逐式复算它作为criterion输入的
具体接口，不把本审查当成对自己源的第二作者审查。

同时读取[Montgomery–Vaughan原文](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
的Theorem 2及Corollaries 2–3，核对所需实线局部间距加权均值。
该输入对有限Dirichlet和适用；平移积分区间只改变系数单位相位。
没有由此引入原zero-free [R]或新的character family。

## 2. (2)–(6)：真实P、全高度MV及共同16词

平均时X、ell、d、phi、a_ell、prime cutoff及所有b_p共同冻结，
只改变sigma。E_sigma在原实区间I上仍为真实isometry。
输出支撑于I，所以outside entries确为全interval Fourier基中
j不在0至d−1；I之外的物理分量没有被错误删除。

对任意实xi，准确outside pair count为min(d,|j−k|)。
以nu=xi ell/(2pi)分解|n|≤|n−nu|+|nu|，使用原C² Fourier界，
得到W_ell(xi)≪log(2+ell)+ell|xi|。这个计算允许nu贴近整数，
不要求xi属于carrier网格。

对每个channel的正、负log p频率，局部间距均至少常数乘p^−1。
weighted MV因此给
\[
 \sup_\alpha\frac1h\int_T^{T+h}|D_R(\sigma+\alpha)|^2d\sigma
 \ll\sum b_p^2+\frac1h\sum p b_p^2
 \ll1+\frac{Y_R}{h\ell}.
\]
这里Y_H=X、Y_L=sqrt X，normalizer中两次ell完整保留。
也可先分别处理两符号再用二项平方界；没有漏掉t近0的相干峰。

原entry的积分在联合
L²(dsigma/h;ell²(outside j,k))中用Minkowski。
每个k、xi引出的实平移均由同一MV supremum控制。
\[
 \int|\widehat\phi(\xi)|\sqrt{W_\ell(\xi)}d\xi\ll\sqrt\ell
\]
使用sqrt|xi|加权L¹；不能误用只有C²粗界时可能发散的
|xi|加权L¹。于是(4)确给
\[
 \langle l_R^2\rangle\ll\ell+Y_R/h=O(\ell),
 \qquad h=T/\sqrt\ell .
\]
这包括整个实高度轴，不要求good Fourier band、P与guard交换，
或高四矩的任何有界前件。

三个内部P的闭合trace差有六个two-crossing pair。
共同sigma上的Cauchy及raw m_H²≪X/ell²给
\[
 \left\langle\sum_{w\in\{H,L\}^4}|\epsilon_w|\right\rangle
 \ll m_H^2\ell/d=O(\ell^{-2}).
\]
这是mean absolute；没有从signed mean推出它。
Markov施于这一个非负总defect，得到相对measure为1−o(1)的
同一G_T，全部16个有序词的absolute差同时o(1)。

这个G_T与anchored源中measure至少1/2、强O(ell^−2)逐点费用的
集合是两种合法选择。criterion使用自己的高相对measure集合，
无需将两个集合相交，也不声称该集合上仍有后者更强速率。

## 3. (7)–(9)：465与456在冻结短窗口上的uniform性

W_sigma=E_sigma* M_wT E_sigma不依赖共同carrier modulation。
准确的乘法压缩平方为
\[
 \tau W_\sigma^2=\ell^{-1}\int w_T^2-
                \|Q_\sigma M_{w_T}E_\sigma\|_{\rm HS}^2/d.
\]
故(7)的S_T和小leakage都不随sigma变化。

465中实际middle-weight HH与物理weighted second的差，
由真实QP两方向crossing付款，为
O(m_H² log(2+ell))/d=o(1)。此费用没有未知H4或q乘子。
差频Hilbert主项的carrier因子可分别吸收到两个prime端点；
csc numerator两项也分别作同样处理。和频及endpoint-alias项
用绝对质量和实际共同overlap，常数与sigma无关。
因此被审稿(8)所需的
\[
 \tau(W_\sigma H_\sigma^2)=S_T+o(1),\qquad
 q_\sigma=\tau H_\sigma^4-S_T+o(1)
\]
均为整个短窗口的uniform additive式。没有将可能增长的
q或H4乘到o(1)中。

456的原three-P repeated helper按平方权重sum b_p²聚合；
其所需second及raw op费用同样uniform。
物理Topp只使用|K_d|及原endpoint overlap。near二根计数和
far预算不取carrier相位符号，故仍uniform；其他重复主项的
Hilbert费用也可吸收单位相位。
由完整exact partition得到
\[
 D_\sigma=\tau H_\sigma^4-2S_\psi+o(1).
\]
D在这里仍是保留全部P、signs、near/far和genuine labels的
actual四全异union。没有把一个重复子族当成全四矩。

## 4. (10)–(12)：half/full factor2的反线性证明

采用原R_s f(u)=f(u+s)的实线零延拓。
每个high步长大于ell/2，严格有
A=Pi_- A Pi_+，故A²=(A*)²=0。
此nilpotence属于物理算子；没有错误地赋给有限E*A E。

J为反射、C为复共轭、K=CJ。even phi和real b_p给
K A K=A*，而对每个原正频carrier向量
\[
 K(E_\sigma e_k)=E_\sigma e_k
\]
准确成立。仅用J则不成立。
因此A*A和AA*的两个HS column范数相等，输出在两半区间正交，
从而
\[
 \Phi_\sigma:=\tau(E_\sigma^*B_H^4E_\sigma)
       =2\|A^*A E_\sigma\|_{\rm HS}^2/d.
\]

D_+=sum A_p*A_p是正半区间的实际same-prime multiplication，
R_+=A*A−D_+。原shared-profile变量替换把D_+R_+ cross
准确分离为p-only与q-only端点；原有限csc Hilbert界给O(ell^−1)，
并统一于sigma。两半same-prime profile正好组成w_T，
所以2||D_+E_sigma||HS²/d=S_T。于是
\[
 \Phi_\sigma=S_T+2r_\sigma+O(\ell^{-1}),\qquad
 r_\sigma=\|R_+E_\sigma\|_{\rm HS}^2/d\ge0 .
\]
系数2已完整付款。R_full=R_++K R_+ K=B_H²−M_wT的两个
输出半块也正交，故其完整实线column范数准确等于2r_sigma。
没有在带末端P的physical trace中作自由循环。

需要严格区别：q_actual是有限H_sigma²−W_sigma的平方；
q_sq是先压缩physical B_H²再平方，仍保留two-step之间的P；
本稿r是完整实线half-ratio norm，2r才是full ratio norm。
Phi是未扣W的physical fourth。本稿从weighted centering及Phi
比较得到q与2r等价，没有将q_sq误当完整实线残差。

## 5. (13)–(14)：增长统一L¹与共同选点

令epsilon_HHHH=Phi_sigma−tau H_sigma4。该量非负，
由全部16词平均桥有其L¹=o(1)。
把(8)、(9)、(12)直接相减，存在sigma-uniform rho_T→0，使
\[
 |q_\sigma-2r_\sigma|\le|\epsilon_{\rm HHHH}(\sigma)|+\rho_T,
\]
\[
 |D_\sigma-(2r_\sigma-S_\psi)|
        \le|\epsilon_{\rm HHHH}(\sigma)|+\rho_T.
\]
因而(13)成立，不需要r、q、H4有界。
它不是所有sigma的逐点small；在同一G_T上才得到逐点o(1)。

若将来实际证明nonnegative r的窗口均值不超过B_T，
则在relative measure至少1−eta_T的G_T上
\[
 \inf_{G_T}r_\sigma\le B_T/(1-\eta_T).
\]
允许另加任意趋零选点误差，即得(14)的一同sigma_T。
全部16词及uniform中心化沿这同一点继续成立。
若B_T增长，不能把除数费用免费吸收到additive o(1)；
稿件已明确保留该因子。若B_T有界，才可这样吸收。

原Jensen早已给q_sigma≤2r_sigma+o(1)的一侧蕴含。
被审稿正确承认这不是新成果；此次新付款是双向L¹、
增长统一及全部mixed words的共同载波桥。
自然短窗口的r upper本身仍是实际待付项。

## 6. (15)–(16)：实际列长度与sinc诊断

(15)由原R_+的准确作用公式直接代入E_sigma e_k：
共同e^{i tau_k u}模为1，留下log(q/p)相位。
外层phi(u)²、p-dependent phi(u−log p)²与moving terminal
phi(u+log(q/p))均保留。没有把共享窗口改为独立profile。

ratio p/q的唯一性不使频距大于X^−2，
square的产品长度仍能到X²。sigma窗口与d个carrier k合起来
只覆盖O(X)高度尺度；不能免费使用length X²的linear均值预算。

对固定参数和四distinct labels，所有实际有限矩阵因子关于sigma
只含e^{±i sigma log p}。唯一分解排除零频率。
在2+/2−情形，两个不同正整数A、B均不超过X²，因此
\[
 |\log(A/B)|\ge |A-B|/\max(A,B)\ge X^{-2}.
\]
3+/1−因所有p>sqrt X而有更大gap；全同号也无零频率。
真实内部P及grid alias不改变这个关于sigma的准确factorization。

显示的概率密度
w_A(t)=(2pi A)^−1 sinc²(t/(2A))
积分为1，其Fourier特征函数为(1−A|S|)_+。
故A≥X²确将整个finite D指数和的long average精确消为零。
这只是一项固定cutoff下的宽平均诊断。其宽度与原h=T/sqrt ell
不同，不能替代短窗口的ratio upper或228零块合同。
自然短窗对|S|≲1/X没有显著抑制，稿件的保留范围正确。

## 7. 最终作用域

新增P与ratio桥的分析及有限代数无需新的zero-free [R]。
用于原零点计数时仍须原228同配置moving-block、normalization、
padding、norm和inertia输入；本审查不重新认证AF分析内核。
本稿没有证明未知的自然短窗r upper，没有把已排除的小Q
条件改名后重新当作算术目标，也没有把long mean0登记为新比例。

最终判定：**限定 PASS，原对象桥与完整判据已付；完整算术upper未付。**
