# Relative Green construction: strongest-old and admission audit

2026-11-01；独占审查。SAME G20261027/runtime1793085111，冻结0c4f基线；
实际STATE动作是ONE显式构造准入，C069/606已spent。本稿不修改状态或计数，
不建立C070，不消费其它章节、参数、外部原文或数值。

**裁定：所给配方的实际405 principal首门失败；分类为标准／强旧直接准入
INPUT0，而非一项新的实质数学合同。** 这不靠移植574–575的不同载体结论：
下面在固定A1_Z自己的Hermitian Picard等价关系内重新核对。新写出一个候选
公式和失败记录，并不自动构成新独立输入；同样，不达RH完成门本身也不是
判0的理由。573–575虽未完成RH，仍因各自新增实际ideal、精确核／normal
分类等而计过数学轮；本次不存在相应新增责任。

## 1. 本对象及最短依赖链

依赖仅为：本准入卡的显式F与已有BC72 native对象定义；405实际非零关系
及其准确Mellin约定；标准segment单叶检验、正则单位和Schwarz唯一性。
不使用冻结BC(7.2.19)系数或(6.2.13)极值符号，不将native正性标签当Weil号。

源为REAL rho∈S_exp，rho=e^(u/2)f。卡中
N2=∫(1+|u|)|rho(u)|e^(2|u|)du，H(z)=∫rho(u)e^(uz)du，
eps=1/[16(1+N2)]，F(z)=z+eps z²H(z)。
S_exp付逐源全部指数矩，故H整、实系数且N2有限。对|z|≤2，

    |F'(z)-1|
    ≤eps∫(4+4|u|)|rho(u)|e^(2|u|)du
    =4eps N2<1/4.

在凸圆盘沿线段积分，得到
|F(z)-F(w)-(z-w)|<|z-w|/4；这是标准局部可逆性的一次直接充分检验，
给D(0,2)单叶。F(0)=0、F'(0)=1，实对称且不依赖未知ζ零点。

据此取formal Spf Z[[T]]、analytic闭单位盘及逆formal germ psi=F^-1。
到同一X=A1_Z的alpha_hat(T)=T、alpha_an=F满足
alpha_hat=alpha_an∘psi。formal映射本身整系数；实／复arch gluing无需
偷加“psi整系数”。此处源随rho变，目标不变；目标上的类才可相互比较。
Q=(T=0)固定，formal pullback Q=P，e=1、R=0，所以本配方没有移动有限
overflow。它的变动确实只在arch metric；BC72的整个全局设施本身并非
arch-only。源的bordered紧性也不使仿射A1_Z成为proper截面容量对象。

Omega=F(D)有解析Jordan边界。g_F(w)在Omega内为log(1/|F^-1(w)|)，
外延0；g_0=log^+(1/|w|)。在0附近，写w=F(z)，则

    g_F(w)-g_0(w)=log|F(z)/z|,    F(z)/z→1.

奇点消去后phi=g_F-g_0在0调和且phi(0)=0；其余处连续、紧支、共轭不变，
分布Laplace是两条解析边界的有限测度之差，故属这里所需C^(bDelta)。
这是标准Green函数的direct-image闭包／局部边界计算，不是新Green
正则性定理或更强拓扑估计。实际类为

    Phi(rho)=[O_X(0,phi)]；Phi(0)=0.

此处relative指同一目标上减去零源metric，不冒称574的双frame范畴。
也不把alpha_*(P,g_eq)的绝对自交替换为Phi的零类检验。

## 2. 在这个carrier重新闭合的principal首检

Z[T]的全局正则单位恰为±1。若纯metric平凡线O_X(0,phi)与单位metric
平凡线等距同构，同构是一个此类单位，其模恒1；无论metric采用e^-phi
还是e^(-phi/2)约定，均迫phi=0。若使用算术divisor语言，div(a)=0仍先迫
a为本正常仿射整对象上的单位，不能用任意Q(T)^*抹掉phi而保有限除子0。

继而g_F=g_0；两者正值域分别为Omega与D，故Omega=D。F:D→D满足F(0)=0、
F'(0)=1，Schwarz等号情形迫F=id。因此eps z²H(z)=0，H整函数恒0。

405的约定实际是M_f(s)=∫e^(su)f(u)du。它给真实像J中的实源

    p=(D²+D)h=E eta_0，c(p)=d(p)=0，
    M_p(2)=pi/6≠0，p∈P_an。

故rho_Pan=e^(u/2)p∈S_exp，且本构造实际有

    H_rhoPan(3/2)=M_p(2)=pi/6.

若Phi(rho_Pan)=0，上述链已迫H恒0，与此确切旧值矛盾。结论为

    Phi(rho_Pan)≠0.

无需重算theta源、引入新Pan、证明新一般Fourier定理或展开全源kernel。
若只作结构解释，H≡0的标准Fourier唯一性确实给rho=0，即这种编码具有
零核；本次反测本身只消费具体Mellin值。eps>0的非线性归一化不会将此
非零源变成F=id。

rho_Pan在这里是几何桥必须消去的**已知解析关系**；405并未先证明它在
未知目标上是几何主除子。本结果说明候选不能实现所要求的principal
下降，不宣称发现一个已证几何主除子却无故有非零算术类。

## 3. 扣除573–575的最强结果，而非较弱旧标签

| 旧资产的实际范围 | 已付最强后果 | 本次可消费与不可移植部分 |
| --- | --- | --- |
| 573：指定扩大源代数A_src、I=S1、F_r及delta F | 一个537真非根生成的ideal含Tr[T,T*]=-4见证；普通迹／旧Omega不能下降；C*闭ideal为全部raw源闭包 | 它已有非零relative charge及共同ideal修补的实质边界；本A1_Z无此A、ideal或regulator，不能借用其no-go |
| 574：两素数非proper等变连续cover、exp(zx)线族 | absolute核iLambda、双frame零核；不变正metric iff Re z=0；mean源看见537却失败同一405实关系 | 已有“非平凡实际线仍未杀非零关系”的准确先例；本carrier零核由上一节重证，不将iLambda或Re z门移植 |
| 574最强合法控制：z(r)=ic Q_zeta(r) | 能同时消全部Pan、看见537并有unitary纤维metric，且fixed窗Dlog费可付 | 这些门同时过也未给独立容量；本Phi连405首门都未过，不能声称优于这个已付控制 |
| 575：同cover的实际regular/Cartier层 | 非flat normal首项精确格Z+iLambda；flat Cartier合法；J²=J及指定整数过滤不分离／无限容量；实际primitive g_r=e^(∫_-∞^x r)对全源relative平凡 | 该map消Pan也杀537，且有原norm／导数费用审计；不将其全平凡结论套到本Phi，也不把两候选优点拼起来 |

574的线性全线原du／Dlog连续标签消Pan即零，用了标签可数核及553密度。
这里rho→Phi既无源加法到tensor公式，也非complex-linear；不能套该线性
密度结论，更不能由它排除所有非线性／有费／变域修复。本次只需一个
旧非零关系，失败机制反而更短：保真编码未实现指定商下降。

573新增的是“哪一个实际ideal含何种charge、闭包多大”的非形式结论；
574新增的是指定非proper载体的精确同构分类；575新增的是允许首项有零
时的严格normal-order分类及过滤费用。本次未闭这些类型的新缺口：
segment估计、Green边界延拓、±1单位与Schwarz等号全部是本显式公式
上的标准自包含核验，旧非零p及pi/6已经支付。不能因为证明写在新文件、
target换成A1_Z或失败称作“新反例”便重复计轮。

## 4. 费用、符号、coverage和实际净后果

强源费N2不是原L² fee。对先fixed supp rho⊂[-L,L]，

    N2≤sqrt(2L)(1+L)e^(2L)||rho||_2.

读成native f须再付e^(L/2)。原physical rho的du范数与native f的du范数
不可混同；已有Dlog≥sqrt(log2)||rho||_2只给同一固定窗的相应upper。
不从此授全非compact原norm、C^(bDelta)连续性、逆germ或cofinal成长费。
N2不受全线L²统一控制，也不自动证明Phi没有任何其它合法有费控制；
首门已败，无需新增norm反测或norm变体。

合法输入目前是全部REAL S_exp，不是全部complex物理源的同一个
conjugation-compatible divisor rule；即使只要求real子域，本次已失败。
标准Laplace唯一性表明编码没有把非零537源自动抹去，但“能看见非根”
与“对实际Pan同构下降”必须在同一map同时满足。后者当前明确不满足。

正的纤维metric e^-phi仅是Hermitian line的定义；phi为signed Green差，
没有已付曲率／mixed Weil号。没有给任意两源的Hermitian极化身份、
源加法／tensor兼容、整过滤／section乘法、RR small-section计数或Rosati
容量，更没有完整Gamma=2theta'、contact、全部proper powers、双pole及
ALLcomplex原du／zero-extension Dlog的同对象消费。固定formal部分的零
finite overflow也不能免费支付这些全局量。

所以净后果仅是**停止这个具体F／relative-metric配方**，没有新的经典
Weil不等式、成长谱约束或方法类边界。既有whole17/16与fixed9/8有限头
资产、542+555→557的whole leading4/5负惯性UPPER全部保持；后者仍非
负谱下界或RH正性。actual principal／sections／mixed、成长core/coupling
及Xi关键瓶颈未变，三个长期完成门仍open。

按该卡的预先停止规则，本审查建议INPUT0／0数学轮；不创建C070、607，
不重开BC后章、来源队列、替代F、半径、metric subtraction或额外norm/
whole测试。其它relative/higher载体、真正协同principal metric、ramification、
额外finite数据及source-adaptive修复未被本首检排除，也未因此自动准入。
