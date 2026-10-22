# 575. 实际覆盖的Cartier层、非flat指数门与物理源过滤

2026-10-22。[C038](../goals/contracts/C038-regular-cartier-cover-and-flat-source-admission.md)，同G20261014／冻结0c4f；接574已结算的实际非平凡线族。
本轮直接构造regular／Cartier设施及不使用Q、零点标签的物理源候选，然后检验同一层的units、局部消失与原范数。
局部Cartier对象确实存在；本轮没有建立独立Weil正性或RR容量，不以合同完成代宏观Goal完成。

## 1. 具体层及符号

沿413／574固定p=2、q=3，L=log2、M=log3，Γ=Z²作用于T²×R，去双∞层得O。
Wp={k有限}、Wq={j有限}覆盖O，交的共同bulk坐标x=t−jL−kM；边界为P、Q。
每side proper、全O非proper。两side商分别为螺旋`(ρ,θ_L)=(e^x,e^(2πix/L))`加ρ=0圆，另一侧同理。

明确比较三层：复连续函数层C；由上述ambient圆柱smooth函数限制的S∞；具有实际边界解析germ的更小候选。
各层沿真实两片和相同bulk粘合为等变层。S∞是一个可构造的自然候选，未证明裸g-integer分布唯一选出它。
“Cartier型有效数据”指局部非零因子生成的可逆理想，不把空间直接称scheme／DVR。
[Stacks有效Cartier的scheme定义](https://stacks.math.columbia.edu/tag/01WQ)仅作命名参照，regular性在本对象上直接证明。

固定frame约定e_p=e^(zx)e_q，Cartier理想I=O(−D)的生成元满足h_p/h_q=e^(zx)，故I对应574的L_z。
通常O(D)=I^∨，canonical正则截面的坐标才是h_p、h_q；不把理想嵌入与对偶线的section混用。

## 2. 非平凡Cartier设施可以真实构造

规范不变函数

\[
\rho=e^x=e^t2^{-j}3^{-k}\quad\text{在bulk},\qquad
\rho|_{P\sqcup Q}=0                                             \tag{1}
\]

连续且在bulk严格正。bulk在每个atlas开集稠密，因此乘ρ在连续层及S∞中均单射。
只用全局ρ给principal理想(ρ)，关联线自由；但在Wp用ρ、在Wq用1，得到支撑在P的真实可逆理想I_p。
交换两片得I_q，且

\[
I_p I_q=(\rho),\qquad[I_q]=-[I_p].                              \tag{2}
\]

I_p的指数参数为1，574的kernel只有纯虚部分，故它确实非平凡。这是两边界同一对象上的Cartier关系，不是自由线换frame。
连续层允许任意正实幂ρ^α；指定整数幂合法，却未由此得到DVR。

更强地，每个z∈C在连续层都可取实A>max(0,−Re z)，以两边方程ρ^(A+z)、ρ^A实现574的L_z。
在S∞中也可用

\[
E(\rho)=e^{-1/\rho^2},\quad E(0)=0,
\qquad h_p=E\rho^z,\ h_q=E.                                   \tag{3}
\]

它们bulk无零、边界smooth-flat，均为非零因子；所有参数mixed导数在紧参数集上一致flat，给实际smooth family。
因此非平凡连续／smooth Cartier族都已存在。support仍为固定边界，不自动成为函数域的moving点或degree-zero算术族。

## 3. 新增严格门：哪些指数可由非flat normal方程承载

记Λ=(2π/L)Z+(2π/M)Z。对上面同一S∞层中h_p=e^(zx)h_q的方程对，若至少一侧有非零normal Taylor首项，则两侧都有，且精确要求

\[
\boxed{z\in\mathbb Z+i\Lambda.}                                \tag{4}
\]

反向每个此类z都可用ρ的非负整数幂乘周期unit实现。
[完整证明](../reviews/2026-10-22/regular-cartier-cover/finite-normal-order-and-flatness.md)不预设首项处处非零：
先由uniform Taylor与周期性比较实阶；再用三频近回归把负尾关系变为精确恒等；若首系数有零，无理周期传播使它稠密为零，矛盾；最后绕数给Λ。
这补上了允许首系数在个别角度消失的情况，强于只假设“ρ整数幂乘unit”的574直接推论。
normal jets在本螺旋限制层内良定义；不同ambient延拓的差在螺旋为零，逐阶周期极限迫其全部normal jets为零。

特别：纯虚参数的absolute非平凡类，任何本门内的smooth Cartier定义方程只能**两边同时flat**。
它们依然有(3)的合法有效代表，不能删去flat修补后宣布没有Cartier。
iΛ中的framed非平凡类不在这一排除内，absolute与保两端frames的relative含义仍分开。
共同换normal坐标为τ=ρ^c（每个固定c>0）只把实部格改成cZ；纯虚结论及物理S_exp的flat性保持，不靠调这个指数修复。不同normal方向和源依赖厚化未排。

若把(3)的局部方程送入ρ-adic完备化，每阶像均为0；原非零因子在完成化中变成零，regular截面／Cartier性不可免费运输。
这约束方程与嵌入，不是证明整条线、整个形式Pic群或所有derived修补都为零。

## 4. 两种消失过滤与容量差别

连续层中，令J为在P∪Q上消失的全部函数理想，则

\[
(\rho)\subsetneq J,\qquad J^2=J.                               \tag{5}
\]

严格性由√ρ不能除ρ连续给出；幂等性由f=√|f|·f/√|f|，零处延0给出。
故由底层边界取的J-adic filtration全部塌为同一层，J/J²=0。
指定I=(ρ)的整数幂链则严格，却有C/(ρ)的无限长度：0<β<1的ρ^β类线性无关，逐个最小指数比较即可证明。
ρ^(1/m)模ρ有任意高nilpotence阶，也表明不是曲线点的DVR jets。

S∞排掉某些分数幂，仍有(3)及所有非零flat函数属于∩(ρ)^n；这里的normal filtration不分离。
此外每条线在bulk上有固定compact窗内无限维的平滑紧支截面，所有边界jets都看不见它们。
局部正metric或纯虚子族的不变正metric都不使这个空间成为有限维；单位球也不会仅由窗紧而紧。
这些是指定层的反测，不排实际bandlimit、整格、加权截面或另一regular结构；但它们的乘法、kernel、截断费和容量须另给。

## 5. 不使用Q或零点坐标的实际源映射

对全部物理源r=e^(u/2)f∈S_exp,C，直接取

\[
A_r(x)=\int_{-\infty}^x r(u)du,\qquad g_r(x)=e^{A_r(x)}.          \tag{6}
\]

它满足g_(r+s)=g_rg_s，确实是源加法到clutch tensor的实际公式。
但S_exp衰减给A_r(logρ)在ρ=0 smooth-flat；g_r及逆都是S∞的side units，且两边界值为1。
因此(6)拼接的线对**全部源**都是保两frames的relative coboundary。
以h_p=Eg_r、h_q=E形成Cartier理想时，两片ideal本身都等于(E)，连理想嵌入也不移动。保留g_r仅保raw frame mark。

405实际P=(D²−1/4)H、H=e^(u/2)h>0是非compact全主关系，(6)确实消去它及全部P_c；不是compact交空的伪测试。
同一构造也消去537的r₀=(D²−1/4)ψ，尽管μ±r₀=0且完整Qζ(r₀)>0，故未通过非根覆盖门。
两种结果发生于同一map，不能把不同候选的过门优点合并消费。

actual E／Fourier双lift在其真实来源域内满足r_η(x)=r_hatη(−x)，对应对数时间两端primitive之和只剩∫r_η。这一函数恒等式本身尚未给有限位P、Q的几何反射或regular层比较；把两primitive赋给两片frame只是待验的具体候选。
正规化两边标架后clutch平凡；保留这个mean则仍由∫P=−(1/4)∫H<0失败405。
不假设任意物理r有η-lift，不把仅对relations定义的来源操作冒称全source map。
只用μ±选权会杀r₀；按P_c专门规定允许哪些units则是旧关系商的重编码，尚无独立locality／过滤／容量。

## 6. 原du／Dlog费用与解析修补的准入

原范数固定为||r||²_du=∫|r|²du、||r||²_Dlog=(2π)^−1∫log(2+|t|)|hat r(t)|²dt，后者使用全线zero extension。先fixed supp r⊂[−A,A]，(6)有

\[
\|A_r\|_\infty\le\sqrt{2A}\|r\|_{du}
\le\sqrt{2A/\log2}\|r\|_{D\log}.                               \tag{7}
\]

第一项是sharp operator supremum；第二项是upper。全线没有uniform此费。
对所选θ-independent radial extension，normal一阶导数为ρ^−1 r(logρ)，需要point evaluation，原du和Dlog都不控制。bulk处ambient ∂ρ不是restriction层内在算子，其他延拓可改法向导数；边界normal Taylor jets的独立性不等于bulk法向导数独立。
内在地D_x A_r=r；任一ambient延拓F的切向导数为ρ∂ρF+(2π/L)∂θF，所以固定bulk点的**完整ambient C¹范数**仍须支付该point费用，不能仅从此宣称某个法向分量的必要下界。
固定窗窄bump r_ε=ε^−1/2 φ((u−u₀)/ε)的Dlog平方费仅为||φ||² log(1/ε)+O(1)，正规化后point值仍按ε^−1/2/√log(1/ε)发散。
加两个远离u₀的固定probe可付O(√ε)费消μ±，仍在537固定窗内；这不是只有pole方向的坏例。
这是指定marked primitive／regular representative的费用，**零Pic类本身可取单位代表**，不能当所有source lift的必要lower。

先用固定κ平滑可对指定radial extension在|x|≤B上付k阶normal导数upper C_(κ,k)e^(kB)||r||du，原费修补合法；线与Cartier理想仍全部平凡。
source窗A、cover窗B、导数阶与全S_exp半范数各自保留，fixed窗费不代cofinal容量。

强制边界解析也没有自动修复：(6)对compact源负端恒1，边界解析germ合法且平凡；若要求全部bulk解析，generic compact smooth源本来不在域。
405实际P的primitive则在每个负尾非恒零而normal-flat：若尾部为0，则H在该尾满足(D²−1/4)H=0，超指数衰减迫H=0，与H>0矛盾。
所以仅边界解析的候选也不覆盖这条实际全关系。ambient角度解析不能绕过此点，首个normal系数沿螺旋的全部角度极限已迫为零。
“x-entire”平滑与“ρ解析”不是同一结构；真正不同的analytic／非交换层及其有费transport仍是额外输入。

## 7. 连续正反、函数域与已有正设施

562的真实连续正g测度系统Z_c=1+c/[s(s−1)]，d=c−1/4=±1/16，primitive代数R_d=C[w]/(w²+d)、w†=−w给完整型2|a|²+2d|b|²。
同一奇源r=(D²−1/4)(uφ)，φ非零偶非负且support(−1,1)，有双pole矩和mean为0，而完整Q严格异号。
(6)在两模型均给同一平凡Cartier理想及全部零normal jets，连正模型的primitive方向也漏掉。
没有给一般连续g凭空配经典adeles；模型自身Γ=0、完整continuous prime／pole项均保留。

甚至自由加层R_d[[t]]时，两段普通复代数都为两份C[[t]]，局部jet维数同为2n；†在正段逐支共轭、负段交换两支，完整型的符号仍不同。
这个明确的辅助层反测“regular参数＋有限jets＋正纤维metric”不足，不是自然几何增强的普遍no-go；†与ample极化的独立关系仍待证明。

真函数域闭点的DVR、integer ord、local长度与有限余域来自同一曲线；principal关系来自有理函数与乘积公式，proper性给有限维H⁰，曲面RR／Hodge index控制mixed二次容量。
旧真F₅ genus2 degree-zero twist使h⁰(K)=2、h⁰(K⊗L₀)=1，给真实moving对照；这些已知正输入不重复计功。
[Milne §§1、7.6](https://www.jmilne.org/math/xnotes/JVs.pdf)的base change与Picard校正不是任意连续gauge可替代的。

也不能遗忘已有设施：[CC scaling site](https://arxiv.org/html/1603.03191v1)有integral-slope半环结构、Cartier、周期orbit上的type-II RR；仓库384/387/396已有真perfectoid解析Cartier及pullback，401有下降却非lfg的理想。
它们与574的O之间仍欠实际ringed／semiringed比较和全源原范数运输，单周期RR尚未支付全部位的primitive mixed容量。
本轮核该具体来源范围后停止，不自动串下一篇paper。

## 8. 完整经典预算与独立容量缺口

令μ±r=∫e^(±u/2)r(u)du、r*(u)=conj r(−u)。目标始终为同一物理r：

\[
\begin{aligned}
Q_\zeta(r)={}&2\Re(\mu_+r\,\overline{\mu_-r})
+[\psi(1/4)-\log\pi]\|r\|_2^2\\
&+\int_0^\infty {e^{-v/2}\over1-e^{-2v}}\|\tau_vr-r\|_2^2dv\\
&-2\sum_{p,k\ge1}(\log p)p^{-k/2}\Re(r*r^*)(k\log p).           \tag{8}
\end{aligned}
\]

完整Γ(t)=Reψ(1/4+it/2)−logπ=2θ′(t)，contact、所有p^k、双pole、allcomplex mixed和原zero-extension Dlog均未删。
两位Cartier权不覆盖其余有限位，更没有自行恢复实Γ规范或pole预算。局部方程“有效”不等于(8)的primitive正极化。

尚欠独立输入为：同一自然regular／fraction层上的全405 actual同构与537覆盖；原norm的source→moving section／metric lift；可消费的分离过滤、整格或有限评价kernel；以及不以Q符号定义的primitive有效性／mixed RR容量。
最后须把该容量与(8)在同一对象、全部尺度和全部误差下比较。假设这种比较有要求的号，或定义容量为Q，再称为Weil证明，仍是等价改写。

本轮新增实际Cartier实现、非flat指数门和全源regular过滤／费用检验；停止primitive／smoothing、mean／旧商标签及analytic域缩小recipe，不续阶、probe或核参数。
非标量moving支集、新normal方向、semiring／derived层、强拓扑／变域及有费无限修补未排。
宏观瓶颈未改变；最强实际ζ后果仍542+555→557 whole leading4/5负惯性上预算，不提供负惯性下界，core／coupling／Ξ仍欠。
C038统一一轮，标准来源、旧控制、各文件与推送不另计；不完成宏观Goal。
