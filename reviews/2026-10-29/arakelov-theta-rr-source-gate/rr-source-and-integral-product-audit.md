# Theta-h0、真实整数乘法与本章来源门

2026-10-29；限定来源审查，待root消费，不建C056/593、不计数学轮。原件固定math/9802121v3，1999-06-29版本；本地PDF21页、405773bytes、SHA256 `39ddc65d010a2f568f46de7e5418ea0be3f995f6eb98dca2a850a0ac8ed52111`，实际字节已独立核。文本读取PDF2–8；整页视觉核PDF5、6、7；PDF8只消费Q例子续段及Fig.2，不认证其余数域例子。未读后续zeta／估计／高维章节或引用文献。

## 1. 实际对象、principal与度数

PDF2–3的对象是数域F上的Arakelov divisor

    D=Σ_P x_P P+Σ_σ x_σ σ，x_P∈Z有限支撑，x_σ∈R；
    I_D=∏_P P^(-x_P)，degD=Σ_P x_P logNP+Σ_σ x_σ，N(D)=e^(degD)。

实位局部metric平方为e^(-2x_σ)|z|²，复位为2e^(-x_σ)|z|²；总Euclidean平方求和。其格体积=√|Δ|/N(D)。对a∈F×，principal系数是ord_P(a)、实位−log|σa|、复位−2log|σa|；积公式给degree0。I_(D+(a))=a^(-1)I_D，乘a给到I_D的真实等距OF-linear同构。因而下述theta量沿真实principal关系不变。这是本身的算术principal证书，不能自动替换成405的源关系证书。

## 2. h0在原文中发生了明确替换

PDF5先介绍通常的有限小截面集合及log#，接着明确换定义。PDF6采用的H0(D)是整个无限加法群I_D，非零section赋Gaussian weight；记本审为

    Θ(D)=Σ_(f∈I_D) exp(−π||f||_D²)，hθ0(D)=logΘ(D)。

零section计一次、weight为1。hθ0是加权格和的log，不是Z-module维数，也不是有限小截面log#。由principal等距它下降到Pic(F)。这个真实算术解释应保留，不能因为功能由Poisson支付便称对象不存在。

## 3. RR规范及原文下标的有限纠正

PDF7 Proposition1给

    hθ0(D)−hθ0(κ−D)=degD−(1/2)log|Δ|，
    I_κ=𝔡_F^(-1)，κ的无限系数0，degκ=log|Δ|。

按定义I_(κ−D)=𝔡_F^(-1)I_D^(-1)，即trace-dual ideal；在复坐标用共轭等距识别Euclidean dual。Poisson因子严格为N(D)/√|Δ|，取log得到上述RR，不缺1/2或判别式。

**原件literal下标不能照抄消费。** 本版PDF7打印Poisson右侧和的下标为`f∈∂ I^(-1)`，但同页∂是different、κ的ideal是其inverse；PDF4也以∂^(-1)=Hom_Z(A,Z)固定trace-dual方向。故该literal下标与定义不一致，正确应为`f∈∂^(-1) I^(-1)`。本审冻结那个general-F字面下标，不改PDF；以上RR仅按正确canonical／trace-dual方向重闭。对Q有∂=1，这处不影响Q例子。不能把本版排印错误升级成新数学障碍或带错下标继续推导。

本章证明用Hecke theta／Poisson；其h1在此依对偶定义，没有在这一页给独立cohomology。这里的RR确实存在，但不因此成为surface上的signed mixed RR。

## 4. Q的真实rank1模型与有限小截面

PDF7–8 Example1：Pic(Q)经degree同构R，Pic⁰(Q)=0。令L_x代表I=Z、无限坐标x，则

    ||n||_x=e^(-x)|n|，L_x⊗L_y=L_(x+y)，
    Φ(x):=hθ0(L_x)=log Σ_(n∈Z)e^(−πn²e^(−2x))，
    Φ(x)−Φ(−x)=x。

Poisson正好给这个最后恒等式。与之比较，有限小截面是

    B_x={n∈Z:|n|≤e^x}，hhat0(L_x)=log(2 floor(e^x)+1)。

例如每个x<0都有B_x={0}、hhat0=0，但Φ(x)>0（Gaussian和含非零n的正项）。两者明确不同；不能把Prop1对Φ的精确RR无声套到hhat0。

## 5. 有实际乘法，但不直接产生计数／theta mixed容量

在整数module上Z⊗_Z Z→Z、m⊗n↦mn是实际同构；L_x,L_y上的pure-tensor metric满足

    ||mn||_(x+y)=||m||_x||n||_y。

因此B_x×B_y→B_(x+y)合法。不过有限B_x不是Z-module，不能把它的tensor写成module同构；该set map有碰撞，通常也不满射。固定x=y=log2时image为{0,±1,±2,±4}，漏掉target B_(log4)中的±3。x=y=0时#B_0=3而3<3²，已拒绝从此乘法免费推出#target≥#B_x#B_y。

Gaussian加权计数也没有因pure-vector norm乘法而变成section权乘法。在x=y=0，记w(n)=e^(−πn²)：

    w(1·1)=e^(−π)>w(1)w(1)=e^(−2π)，
    w(2·2)=e^(−16π)<w(2)w(2)=e^(−8π)。

这两项用于Gaussian的无限I，不冒充有限B_0的小截面。Θ(L_x)Θ(L_y)是独立(n,m)的直和格求和，而rank1 tensor对象L_(x+y)只对一个整数求和；特别Θ(L_0)>1故Θ(L_0)≠Θ(L_0)²。Direct sum与tensor不能混为Deligne放大。

这些基本比较只否定无费的直接计数／权运输，不否定有额外独立条件、collision费用或其它整过滤的容量估计。几何section乘法本来也不普遍injective；本章所核页没有提供本Goal需付的两独立物理源mixed比较。

## 6. 405／537与最强旧的实际门

本章给了D及其principal等距，但没有构造r↦D_r、实际arith primitive或两槽mixed配对：405全部noncompact P_an及其平移如何映成上述principal未给，537非根如何保留／原du-Dlog与强源费用、全源coverage亦未给。不能把源的complex线性组合直接当成有限位整数系数的D；若需先映到实际对象再线性化，那个映射及费用须另付。Pic⁰(Q)=0只说明这个Q degree0 Pic目标本身不能容纳非零primitive，不排更高／relative／derived或不同源族。

与既有资产对照：573§9已保P¹_Z的真实整数section过滤、metric与log#正控制，且指出没有从其HH源自动得到这些sections；552已给真实径向adelic metric并有principal／完整型反测。Corrected-theta root收据已付scalar Gaussian/Poisson、全物理源费及Pan闭包，未认证整arithmetic theta；它不是此hθ0定理，但不能重读Poisson就重领新source／Green。405/518–520已有真实源商及卷积乘法，本章的arith线module乘法不能无桥替代同源mixed。

故本门结论是**已核经典算术theta-RR与正确角色，来源门停止，不准新数学合同**。不是证明所有Arakelov机制不可能，也不是宣布本文后续章节无机制（未读）。完整Γ/contact、properpowers、双pole及Weil signed身份未由本页RR付清；principal／sections／mixed、signed corecross／成长Ξ仍欠，whole4/5负惯性UPPER无新后果。源量词／范数／coupling尚未闭合，不能用hθ0正值替代它们。

没有额外query、paper或数值计算；只写本稿，不改STATE/cadence/manifest/Git。无同章首次阅读断言，不续本文后章、Q参数、rank或theta recipe；本文原PDF保持本地ignored。当前单cadence2/history56/latest592/formal18保持，来源审查不计数学轮；最终结算由不同fresh与root负责。
