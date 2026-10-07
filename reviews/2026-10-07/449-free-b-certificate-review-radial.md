# 449 自由 b 连续证书独立审查（radial）

2026-10-07。状态：限定 PASS [T/R]。未发现未修复的数学阻断。本审查只对注明的通用外部输入成立时的参数推导负责，不认证这些原输入自身、实际素数算例、无穷分析的机器 kernel、RH 或边界线上无零。

## 1. 最终版本与输入绑定

审查对象：notes/449-free-b-compensated-geometry-and-optimal-relative-boundary.md。全文370行，canonical UTF-8长度15509 bytes，canonical LF SHA-256：

2d4b37628d6f68229fd687d6ac84c2ba03cb7223c412df5e00c07a0ff5e1a3bd。

canonical LF仅把CRLF和lone CR变成LF。初次全文读取与终审核对时hash一致；未修改该note。

外部来源：OpenAI September-30-2026 build/paper.tex，commit adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical LF SHA-256：

42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。

使用的是445已列明的确切[R]：generic smooth/Gaussian/reflection/Gram、same physical/Poisson/local identities、global/buffered reciprocal、functional equation与增长、actual detector与marked/plain/inverse moments、uniform mesh、fixed-ray prime asymptotic及全Hecke7/8 bootstrap。原固定b的441结论和sigma_0>=7/8的shared接口不被直接换参数。

新输入文件绑定：

- reviews/2026-10-07/hybrid-free-b-geometry-optimization.md：17430 bytes，SHA 35dac7399af8507be7c39c0e3e69c37d47adf83ebda9125d2a5f62e663037f67。
- scripts/hybrid_free_b_geometry_exact_audit.py：10708 bytes，SHA 5a366da5e8114d158cb76b3a94060155786a0ca637a914b662ba17cd66afa63f。

报告与脚本已去掉多余EOF空行。脚本在Q与Q(sqrt(921))中精确841项通过；其中189个finite direct endpoint evaluations只检查实现，连续结论由符号恒等式和正系数证明。此次未运行或覆盖旧审计。独审针对root重新组织的449逐式检查，而非把输入推导报告本身当作证明授权。

## 2. General-b low与真实准入（§1–2，45–117行）

(3)正确给lx、ly、M、h和同一双留数的C_b(s)=s−2/3−b/6。physical completed cn^3、masks、Gaussian、selected-prime compensation、S/T/xi/ray及A_T不因改变b被重新定义。

全rescaled subsets的(4)与原q_(p_J)^(-3/2)系数一致。M'+ell'−1=−3d_J保持generic reflected-energy的实际dyad推导；这一关系不含b。正文(5)保留正row loss、powerful部分只计一次、empty marks、原S/shared-prime masks与common profile/kernel顺序。原source7663–7804允许固定实bounded lengths，不要求ell=1/6或b=1/8。

对1/6<=ell<=1/5及0<b<=3(1−ell)/8：

- M'_min=1−3ell>0。
- lx−ell=(1−3ell−b)/2>0；由b上限及ell<=1/5，最低仍有1/20。
- ly−ell>0。
- Pa=q_b*^(-1) Z^b>=1最终成立，所需阈值可依固定target arithmetic data。

所以source8340–8360的actual ray/Gauss additive Gram前件齐备。原Gram的完整1+Pa^(1/6)+Pa²/Y'保留，没有无声删除第三项。

(7)的Cauchy归一化与固定compact r_J允许的常数正确；tuple数、原rescaling coefficient和X'缩短准确合为−d_J。相对lx/2+b/12的(8)正部函数每段斜率分别在−1、−1/2、−7/8、−3/8中，故max在d=0，而不是只验证端点grid。

由5ell−1<=0得
L_low=max{(1−ell)/4−b/6,b/2}。
所取b域使第一分支占优，(10)交点sigma=11/12−ell/4合法；交点不含b是同一normalizer的代数结果。

negative/zero-b分支未付Pa>=1；正文117行明确排除直接扩展，这个限制恰当。超过第一分支的b也不延用原交点。两个候选更满足强all-J吸收域b<3(1−3ell)/8，所以它们不依赖broader-envelope边界的细节。

## 3. 每个连续系数、临界根与最优scope（§3，119–205行）

(11)的P(y)=(7+18y+8y²)/9与原P_x完全相同；D=(37+34y)/18也正确。R_*与J来自合法kappa=3/4、alpha=5/6的实际crossing。J>=35/54>0、R>=1−delta及R<=1−2delta/3的使用域是原真实rectangle。

独立展开(13)确认比例为
F=648(−2JE)=A delta²−B delta+C；
(14)的A四项、B三项和C两项系数全部准确。因子648与后续12960分母相容，没有丢失2或J。

(15)常数判别式、b_opt=(2185ell−213)/1228和Q_max(0)=−1631700(1653ell²−66ell−35)/307均成立。(16)正根e=(33+8sqrt(921))/1653与b的两种表达式相同，隔离界1/6<e<167/1000、.123<b<.124正确。

临界关系约简后：

- A_0=(108036−82548e)/307>0；A_1,A_2,A_3也严格正。
- (17)的Q_0=0准确。
- Q_1、Q_2使用e<167/1000给正；Q_3、Q_4使用e>1/6给正。
- Q只有degree4，没有漏掉更高项。

因此Q(y)>=0对所有y>=0成立；y>0严格正。Completing square证明F>=0；在真实rectangle J>0后才推出E_sigma<=0。正文没有把分母符号跨域忽略。

唯一等号为y=0、delta=(49−sqrt(921))/48，且B_0/(2A_0)正是此数；它在[1/50,3/4]内部。

最优性(19)使用这个固定实际rectangle点的R_*=2/3，消掉全部b项。E对ell的斜率3/4+3delta/2>0，因此ell>e会使该点E_sigma>0。这个论证排除保持原R_*、low交点和整个amplitude rectangle的更强非正证书；正文204–205行明确不声称actual坏行达到包络、L零点存在或所有方法最优，范围正确。

## 4. 有理严格比较（§4，207–225行）

有理几何(20)全部准确。A,C,Q正系数与A_0Q−Q_0A非负系数给Q/A>=Q_0/A_0。因J<=5/2，
−E>=Q_0/(12960A_0)=10580567/347281513800000>10^(-8)。
这是真实continuous saving；finite sample未承担证明任务。

note447已有t_c<1/5841，而1/5825>1/5841，故sigma_r=7/8−1/(4·5825)<sigma_c，无小数比较。

独立Fraction复算449新增的根比较：
1653ell_r²−66ell_r−35=−9289/407167500。
ell_r>1/6处二次式递增且小于0，所以正根e在右侧，sigma_circ<sigma_r。最优代数点与稳健有理例均被保留，次序准确。

## 5. 全d、floor/outliers及actualslots（§5–6，227–317行）

(22)由完整unfactored Mellin exponent重写，C_b的常数已计入。与444的joint full numerator接口仍共享同一q；g=qell，error gain为0，不只对positive slots平均，也没有重复扣primitive conductor deficit。

central d斜率至少33/50−delta/2>=57/200>0，故[1/2,h]受endpoint控制。floor用delta=1/50、R=1、q<=1/100；不虚构witness。middle的common无槽R=76/75−2delta/3覆盖floor，斜率101/150−delta/6>0。最坏q和delta给的middle式准确，其delta系数在当前候选为正。

(23)各identity逐项正确：
Gram_allJ=(1347−7133e)/1842>2/25；
5e−h=(6411e−1015)/2456>1/50；
floor=(290401e−49533)/184200<−1/200；
middle=(292151e−84703)/1473600<−1/50。
有理Gram/supply三项也正确。

bootstrap只给beta_*<=7/8，并未用新边界。Delta<= (e−1/6)/4；zeta=Delta/32<1/384000使5ell−h−zeta>0、ell/(h+zeta)>1/5>7/37且h+zeta<1。extension费用<=Delta/16；真正参考C_b(beta_*)另减Delta，critical零附加margin后仍有15Delta/16中央预算。

443的actualslots前件确实保留：alpha/kappa固定；inverse/plain branch有原strict widths；whole positive slots只有允许的one-fraction loss；zero capacity用zero-slot版本；mesh先于K；w_i<=2ell_i。内部plain pool与physical slots是分离，非包含。固定Theta系数/full conjugation、outside-S inducing exceptions、原zero masks及finite S-supported units未被随意删除。

解析域由原有限local表逐式重证。sigma_circ>5/6给足够的D2*与small D1(1/3)margin；source原写D1(3/8)的small lemma未被直接应用。good c_b>81/100、ram c_r>82/100，principal四error最弱为sigma_circ。negative-w的theta和D1 epsilon_H=min(epsilon_0,1/50)均保留。

fulltuple一般contour不除H；只有已经近one的principal/dynamic域用quotient。whole-bin全局先移，pointwise partitions后置。small (25)精确负于−2/25，独立覆盖d<d_min及bounded units。large (26)的B_0=7/4−3ell/4+b/4正确，先zeta后固定z_infty，全u绝对尾仍保留；这些只要求既有generic all-height输入，不把completed sums误称有限。

principal正常product、同一S、同一c_S A_T、actualrayprime非零normalizer、m_w=l_y/20、m_z=h/600与mu>0合法。改变b只改变C_b线性常数，未改变双留数和exp((s−5/6)^2)。

## 6. Delta量词与同源continuation（§7，318–357行）

critical E_sigma<=0本身不是正saving，但(24)后真实E_beta<=−Delta。正文先用共同Delta选moment/count losses、capacity decrement、uniformmesh、rounding，再K/windows，再mu；不存在用K-dependent mu回选mesh/K的循环。

central total losses<Delta/4，extension至多Delta/16，足以留下m_0的一半。floor/middle/small保各自独立margin；principal用m_w,m_z,mu的小份额。m_0=min(Delta,m_w,m_z,mu,1/200,1/50,2/25)>0在target前固定。

target后的最终arithdata与same S之后才选internal orders，A_eta/B_eta不随externalN变动；actual detector ceiling在tau之前，tau在externalN之前，threshold最后。原cumulative T1/2只分配一次，没有给witness或prime额外新buffer。(28)使用同一个独立physical normalized J_eta及same principal f_eta，二者不含T1。

由tau<=m/[4(A_eta+1)]及尾N选择，得到sigma_hi=m_0/8；low与inverseA_T损失总omega=Delta/2。二者是全族共同exponents；target-dependent tau/N/常数/阈值不会破坏supremum反证。

C_b(s)斜率1，Gaussian的小Z右移、Fourier识别、Mellin局部一致收敛可逐式重复。H_eta>=1/2排除取消；共同epsilon_*>0使supremum无需attained也可选矛盾target。finite Euler/Dirichlet quadratic transfer与principal s=1例外保留，未扩大为边界线或critical-line比例结论。

twisted另审全族continuation；本审查也核定这里的接口和量词一致，未把其另一份结果当作本报告的替代证据。

## 7. 结论与未付范围

449最终冻结版本限定PASS [T/R]：

- general-b完整low、negative/third项分支准入明确；
- 所有continuous coefficients与最优范围准确；
- 有理严格比较和全部d/outer预算成立；
- actual slots、同一source/normalizer与Delta参数顺序合法。

输入包[R]自身的正确性、原高比例方向的signed arithmetic费用、RH/规范Weil桥和externalformalcert仍未付。本报告不要求修改note；如其后仅增加审查链接或元信息，需重绑定最终hash。
