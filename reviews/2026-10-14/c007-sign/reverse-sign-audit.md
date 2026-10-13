# C007：实际光滑夹心迹域、首素数共振与无限符号的逆审

2026-10-14。恢复AGENTS、README、STATE/check/show、Goal、C007、D20261014C；
HEAD核实为bbbd54c26e1f335c4238877a7954edd02146dab8。
核对direct-sign-audit.md、source-sign-audit.md及主代理提出的实际smoothing引理。
只写本文件，不改STATE/cadence，不新增研究轮。优先证明实际trace域，
然后消费kernel符号；不沿用C006未付的无限角trace分离。

## 1. 独立Plancherel/Sobolev组织的实际S1引理

physical H=L²((0,infinity),dx)，L=1_(0,1)，
`F_r(x,y)=2cos(2pi rxy)`。固定g∈Cc∞(R)，令
`B_r=A_g L F_r L`，r≥1。选择W0使suppg⊂[-W0,W0]。
output unitary log坐标u=logx下，input仍为physical y∈(0,1)，准确kernel是

    b_r(u,y)=2 integral_0^1 g(u-logz) z^-1/2 cos(2pi rzy)dz.

partial_u仅作用于g；低cut z=1并没有移动，故无遗漏cutoff endpoint导数。
对每个u置 `f_u(z)=g(u-logz)z^-1/2 1_(0,1)`。
cosine Fourier Plancherel在input y>0上给

    integral_0^infinity |b_r(u,y)|²dy
      =r^-1 integral_0^1 |g(u-logz)|² dz/z
      <=r^-1 ||g||².

g'代替g得到同一导数界；限制input到(0,1)只减小范数。
output u>W0自动为0。取中段
`J_r=[-logr-W0,W0]`，长度ell=logr+2W0。
从input L²到natural H1(J_r)的算子是HS，范数≤C_g sqrt(ell/r)。
natural H1(J_r)→L²(J_r)的嵌入也是HS：Neumann cosine基给平方奇异值和
`sum_(k>=0)[1+(k pi/ell)²]^-1≤C(1+ell)`。
它不要求端点函数值为0，不把sharp output区间延零后的分布导数误当H1导数。
两个HS因子相乘，认证中段S1 bound `C_g(1+logr)/sqrt(r)`。
此证明不需要另作近边界非驻相估计，也覆盖所有中段cutL端点。

剩余deep physical output `0<x<exp(-W0)/r` 必须另控，不能粗乘无限log长度。
这时source积分覆盖全g，cosine Taylor给准确rank-one级数

    B_r(x,y)=2 sum_(j>=0) (-1)^j(2pi r)^(2j)x^(2j)y^(2j)/(2j)!
                           · integral g(t)exp(-(2j+1/2)t)dt.

output x^(2j)与input y^(2j)的L²范数、以及source固定支持界，给每项nuclear范数
不超过 `2||g||_1 r^-1/2 (2pi)^(2j)/[(2j)!(4j+1)]`。
其绝对和有限，故deep段为S1并有O_g(r^-1/2)费用。
中段与deep段相加，最终严格得到

    ||A_g L F_r L||_1 <= C_g (1+logr)/sqrt(r), r≥1.

任何fixed positive r<1项也由同一分段/Taylor方法给有限S1费用；
其常数可依赖r。这足够处理每个fixed-prime Fourier的有限反向低scale项。
本引理保留g的固定smooth前件，未证明whole source-L² uniform S1费用。

## 2. 真正共同source trace域和bounded block identity

对fixed p，实际Fourier及低cutoff为

    F_p=2(1-p^-1) sum_(n>=0)cos(2pi p^nxy)-2p^-1 cos(2pi xy/p),
    K=L F_p L, R=(I-K²)^-1, h(K)=KR.

算子表达是531原operator-norm收敛展开，kernel不是逐点定义。
上节引理使 `A_g L K` 的high-scale和在S1范数中绝对收敛，
因为 `sum_(n>=0)(1+n logp)p^-n/2<infinity`。
有限反向项亦为S1；于是 `A_g L h(K)=A_g L K R`为S1。
反映源g(-t)同样满足引理。

按low/high写 `F_p=[[K,T*],[T,D]]`，则T*T=I-K²、DT=-TK。
对与K交换的selfadjoint f(K)，定义

    X_f=L f(K)L F_p H,
    Phi(f)=X_f+F_p X_f F_p, H=I-L.

直接四块乘法得

    Phi(f)_LL=K f(K)(I-K²),
    Phi(f)_LH=f(K)(I-K²)T*,
    Phi(f)_HL=T f(K)(I-K²),
    Phi(f)_HH=-T f(K)K T*.

令f=h，正好是实际完整overlap
`O_p=S_p-H-F_p H F_p+I`的四块。
这是exact bounded identity `O_p=Phi(h(K))`，不依赖角谱trace的任何极限。

对每个fixed real smooth g，source Z=A_g*A_g与F_p交换，
`A_gF_p=F_pA_(g(-t))`。上节使
`A_g X_h A_g*`及`A_g F_p X_h F_p A_g*`分别真正S1。
所以Phi身份可直接ordinary source trace，合法循环给

    E_p(g)=Tr(A_g O_p A_g*)=2ReTr_low[h(K)M_p(g)],
    M_p(g)=L Z H F_p L.

右侧整体也真正S1：`h(K)L A_g*=(A_g L h(K))*`为S1，
乘`A_g H F_p L`为有界算子即可。不需将任意强收敛的finite-angle trace
当作此ordinary trace。
这支付C007新域，不将C006绕K0的非交换H3 conditional身份自动复活。

## 3. 完整返回修正及bare共同scale极限

固定p的K属于S3、norm<1，故

    C=h(K)-K=K³R in S1.

C与K交换，Phi(C)是ambient S1，Phi(K)和Phi(C)准确相加为实际O_p。
上节已付两者的smooth source迹，因此bare+return不是定义出来的替代trace。
return的source迹可循环为
`2ReTr(A_g D_C A_g*)`，其中 `D_C=H F_p L C L`为ambient S1。
`d_C(t)=Tr(D_C U_t)`连续有界，范数≤||D_C||1。
所以L1源质量一致有界的窄source family上，完整return值一致O(1)。

另外，任意ambient S1 D诱导的固定finite-measure源算子是S1：
对unit physical向量v，map g↦A_gv的source-to-physical kernel有HS范数平方|U|。
D的绝对rank-one展开遂给source S1范数≤|U|||D||1。
可消费此强范围；但符号主证明只需连续bounded return kernel。

bare的共同两scale截断亦合法：`A_g L K_N→A_g L K`在S1，
完整F_M→F_p在operator norm；循环后的source trace由S1×bounded估计收敛。
每个finite scale组合互换U_t与U_-t，故与real-source Z交换。
有限光滑kernel trace直接给两cosine配对积分。
顺序是先以 **完整F_p** 的ordinary半迹取K_N的source S1极限，
再以F_M的operator极限辨认该同一半迹的finite-kernel表达，最后取2Re。
没有对finite F_M写Phi身份或假设F_M²=I；有限组合通常不是unitary involution。
上述双极限可联合取，因为K_N的source S1范数由绝对scale和统一有界。
本U−U里，共振pair的L1核费用O(p^-n)，nonresonant pair由phase gap绝对可和，
same-scale near0费用也可求和。故double kernel在该source区间的L1极限
与S1/operator共同cutoff的bare迹相同。
这里没有使用不合法的distribution乘积或省略common trace-limit前件。

## 4. 实际p=2的log系数与self channel

令a=log2。实际F2 high cos振幅为1，有限反向振幅为-1。
对positive source lag t，barepair为

    I_(r1,r2)(t)=exp(t/2) integral_(exp(-t))^1 integral_0^1
                           cos(2pi r1xz)cos(2pi r2 exp(t)xz)dzdx.

cos乘积和z积分给direct稿的1/(4pi) Si端点式，常数正确。
在t=a+delta，唯一无限共振family是r1=2^(n+1)、r2=2^n。
其difference-phase的每mode在delta=0为
`exp(a/2)(1-exp(-a))/2=sqrt2/4`。
对2^n|delta|≤1，误差为O(|delta|+(2^n delta)²)；其和一致O(1)。
更高n由两个同号Si端点主项相消，尾O(4^-n delta^-2)，其和O(1)。
mode数是log(1/|delta|)/a+O(1)，因而

    e_bare(a+delta)=c2 log(1/|delta|)+O(1),
    c2=sqrt2/(4log2)>0.

非共振scales在a邻域有uniform ratio gap，绝对sum bounded；
有限反向scale不能改变log系数。bounded余项允许log-periodic波动。
在t=0附近，same-scale族是O(t(1+log(1/t)))，nonresonant族有bounded零极限，
所以self channel没有同强度log发散。
冻结W=log(sqrt6)<2a，其他binary-ratio log共振都不进入此source域。

## 5. 实际正负合法窄源与无限指数：更少前件的证明

取fixed phi≥0、integral phi=1、phi∈Cc∞(-1,1)。
取两fixed normalized smooth校正bumps psi±，其ell_(1/2)值不同；
可放在patch内两端并避开下面的有限点集。
对任意fixed中心x_i∈(-b,b)，令

    h_(i,eta)(y)=eta^-1 phi((y-x_i)/eta)-c_(i,-)(eta)psi_-(y)
                                         -c_(i,+)(eta)psi_+(y).

解两乘两矩阵，严格使ell_0=ell_(1/2)=0；系数在eta→0时一致bounded。
每个eta都是原patch合法smooth源，L1质量一致bounded。
其两个patch组合 `g_(i,eta)^sigma=h_(i,eta)(t+a/2)+sigma h_(i,eta)(t-a/2)`。
actual pole为0，actual primepower只有2；没有更换原完整Weil型。

同中心narrow/narrow cross的log配对为log(1/eta)+O(1)，
finite phi自相关log积分可积。narrow/fixed与fixed/fixed的log卷积一致bounded；
self channel bounded，完整return也由第3节一致bounded。
上节共同trace身份因此给 **actual**

    E2(g_(i,eta)^sigma)=sigma·2c2 log(1/eta)+O(1).

正号给严格E2>0，负号给严格E2<0；不是只认证裸功能。
其L²norm随eta增长，归一化后的Rayleigh趋0，与532 compact性相容。
该结论只否定QW≥T2的无费用桥，不使QW本身为负。

任给N，选择N个distinct x_i避开校正bumps。
不同中心的narrow/narrow差离log中心delta=0有正距离，故off-diagonal配对O_N(1)。
所有包含fixed correction的项及return仍O_N(1)。
actual E2在这N个sources上的Gram矩阵准确为

    sigma·2c2 log(1/eta) I_N+O_N(1).

eta充分小给N维严格正／负定空间。
函数独立性可在各自narrow支撑、避开fixed corrections处直接核验。
因此actual E2在原矩零smooth类以及闭域V有无限正、负指数。
再加任意有限个连续source约束，只对任意大的严格±空间施有限余维限制，
仍保留任意大的严格±子空间。无需证明bounded log余项S1、
无需carrier o(1/R)，也无需source稿额外对角H1/S1前件。

source稿的更强备选组织亦未发现错误：same-scale diagonal核在H1的
O(r^-1/4)导数费用由t=r^-1/2两区估计支付，nonresonant H1 dyadic和可求和；
Fejer positive finite-rank采样positive log cross给非S1。
但主符号定理可优先使用上述N窄源矩阵，减少消费前件。

## 6. 每个fixed single-prime和source阈值的同证明扩展

同一实际域引理对每个fixed p≥2成立，常数可依赖p。
F_p high cos振幅为2(1-1/p)，在t=a=logp共振pair的unweighted cos振幅为
`sqrt(p)(1-1/p)/2`。相乘得每mode
`2sqrt(p)(1-1/p)^3`，mode数除以a，所以

    c_p=2sqrt(p)(1-1/p)^3/logp>0.

p=2时正好回到c2，不遗漏两kernel振幅或cos乘积的1/2。
对任意lambda>sqrt(p)，可取两patch中心±logp/2及足够小b>0，
使source支撑在(-loglambda,loglambda)、2b<log2，
并使logp±2b不含任何其他integer（因此不含其他primepower）log。
例如b同时小于support余量及最近p±1的两个正log间距之半即可。
这样actual selfprime=0、onlycrossprime=p、pole两矩零。

actual `QW-T_p=-E_p`、bare+return共同trace及narrowN机制都保留，给
`E_p(g_eta^sigma)=sigma·2c_p log(1/eta)+O_p(1)`和无限±指数。
这是每个fixed single-prime来源的全lambda>sqrt(p)方法边界，
不证明joint finite-S、成长p/source预算或连续添加到其他base-S。
general-p源域随p改变，不把它消费为C006原fixed U的晚prime反例。

## 7. 消费判定与宏观范围

本轮重大候选通过：新smooth source S1引理支付真实globalphysical0和cutL端点，
exact boundedPhi身份与ordinaryTC循环支付actual E的bare/完整return分离，
实际首prime正log系数及原严格矩零窄源给严格正负反例，
N维机制和有限约束给无限±指数。
这与C006 conditional非交换角截断不同，不无声复活其未知whole返回预算。

改变的实际瓶颈是：已付true first-prime compact桥的低域符号现在被证为不定，
全源无费用QW≥T_p比较失败，finite continuous constraints无法修复。
完整QW正性、实际lowest/prolate、conditioned base-S和成长S/U仍开放。
positive trace本身不包含未付的signed joint支配；本结果也不构造RH反例。
宏观Goal须按下一节逐项验收实质方法类边界，不能仅凭合同或“无限指数”标签宣告complete；
世界优先权、外部评议和整体形式化未认证。

唯一下一动作：主代理按上述实际对象和量词消费结论并确定无费用桥的停止／重准入条件；
新准入必须支付不同真实signed来源或明确的source费用，不能只增加finite矩约束。
本审查无pending计算／下载进程，不改STATE/cadence。

## 8. 独立宏观完成审计：只以535这一方法边界验收

重新完整读取GOAL.20261013的三个并列完成分支及旧GOAL.20260909§10 B/C/D。
本审计不以535结尾的“Goal active”作为依据，也不将RH证明加为边界分支的隐含条件。
结论是：**535单独已经达到所写“有效机制的严格边界”数学门槛；
当前完整Goal的保存／最终审计步骤尚未完成，不能在未保存核验前调用complete。**

验收的方法类准确是：采用真实canonical单prime Sonin正迹T_p，
在完整actual Weil测试源上取得无费用QW≥T_p，
并允许任意有限个连续源条件及有限秩自伴修复的方法。
这是原有限位Sonin正来源比较程序的一个真实机制类，
不是所有正trace、所有Hilbert实现或所有finite-S方法。
535排除每个实际p、每个lambda>sqrt(p)上整个类的全source比较；
在每个域内存在任意维数的严格反向空间，不能选择有限个例外／矩条件修复。

其规模与核心意义足够，理由来自535自身而非累加529/530：
实际Gamma、极点及全部primepowers账本保留，正来源是真正orthogonal Sonin projection；
新增smooth-source S1域和bounded block身份解除actual trace前件，结论已无conditional；
每个首prime耦合的正log系数c_p明确量化，完整return是连续bounded核，
故符号失败由真实算术尺度共振强制，独立于ζ零点位置、有限矩阵或未知低谱。
support跨过sqrt(p)即出现合法反向域，给出了明确的可行性必要分界和修复责任：
成功机制必须付无限维cross费用、质量支配或不同共同来源，有限补充不能完成该工作。
这正对应旧§10 B末行“实质规模的方法类／更精确可行性分界”，
且不是孤立线代反例或旧计数模型变体。

相对3a72930的复核：baseline在notes/reviews/goals/literature的
Sonin／logarithmic-resonance检索仅有旧literature的有限S空间同构摘要；
此前511的相位及其他辅助边界不含本canonical source比较、actual log系数、
smooth source迹域或无限±修复边界。检索只辅助核对已读基线对象，
不证明世界优先权。535与直接／来源／主迹域／本不同组织逆审的对象和量词一致，
ordinary共同trace域这一主要异议已由新引理明确闭环。

未排除的无限秩紧修正、质量费、多prime联合抵消、独立几何正性和lowest路线，
是必须如实声明的逃逸条件；旧边界分支要求说明这些条件，
并未要求逐一排除它们。不能因为RH、growth-S或这些逃逸仍开放，
无限提高已经满足的严格方法边界门槛。535也没有证明这些逃逸可实现。
若选择RH／新正性证明分支，这些仍是未付数学前件；
若选择用户明确允许的方法边界分支，它们不再是完成该分支的隐藏必需工作。

当前真正缺的完成前件是保存与总体核验，而非C008或另一个数学突破：
535及其新迹域/逆审仍在工作树中，须将最终一致版本、来源版本/范围、
本宏观判定、停止／重准入条件和STATE结算保存，提交推送后核远程SHA，
并逐项确认完整Goal要求没有遗漏。外部评议、世界优先权和形式化只按真实未认证状态陈述；
Goal不要求将这些未声明成果伪装成已完成。完成这些实际D项后，
主代理可以依据方法边界分支正当地完成本Goal；无需人为继续一个新的候选合同。
本审计本身不改STATE/cadence，不调用Goal状态工具，不新增研究轮。
