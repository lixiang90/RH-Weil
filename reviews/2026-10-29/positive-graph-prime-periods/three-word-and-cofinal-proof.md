# 正edge-additive图：三闭词障碍与cofinal通信费用

2026-10-29；当前独占证明稿。按root指定的实际三词反测独立核算；不改STATE、Goal、cadence或Git，不调用web／新增文献。以下是可核数学证明，尚待不同fresh及root消费／统一结算；不由出稿自称591后新轮已消费。

## 1. 对象、测度与消费域

令G为有限或可数有向multigraph；顶点、边均是可数集合，允许parallel edges。每条实际有向边e有严格正长度l(e)>0、严格正活动权a(e)>0。有限路径的长度相加、活动权相乘；空路径长度0、活动权1。闭词指实际有限closed edge-word，不把不同edge-word仅按长度识别。

对primitive cyclic closed word γ（模cyclic rotation，且不是proper power），记lγ>0、uγ>0。每个非空closed word W都有有限word意义的primitive root，模cyclic rotation唯一；若W=γ^k，则

    l(W)=k lγ，a(W)=uγ^k。

可数性保证primitive cyclic words及全部repeats为可数族。定义非负测度

    ν_G=Σ_(γ primitive)Σ_(k≥1) lγ uγ^k δ_(k lγ)。             (1)

**Admissibility是假设ν_G在(0,∞)为Radon，不是任意可数图自动满足的结论。** 正项可能因无穷多短轨道而使某compact质量无限；那种图不在本次合法逼近对象内。这里不预设transfer operator的有界性、自伴性、ordinary trace或normal determinant极限。所有下界只使用(1)中的有限或正项子和，故不交换条件收敛级数。

目标为中心化正prime-power measure

    ν_ζ=Σ_(p prime)Σ_(k≥1)(log p)p^(-k/2)δ_(k log p)，
    S={k log p:p prime,k≥1}。                                (2)

S在(0,∞)闭且局部有限，最小点log2；ν_ζ是Radon，support恰为S。它只是完整经典Weil分布中正prime项；完整W的Γ/contact、所有proper powers及indefinite双pole不能从(1)免费获得。

## 2. 三个数字不可能同时为素数幂

先固定不同素数p≠q，a=log p、b=log q。对任意c≥0设

    t1=c+a，t2=c+2a，t3=c+a+b。

若三者都在S，则N=e^(c+a)>1、pN、qN均是整数素数幂。由N和pN都为素数幂，N只能是p的正整数次幂；但qN含p、q两个不同素因子，不是素数幂，矛盾。因此至少一个tj不在S。

有一个对所有有界c共同有效的显式距离。先固定C≥0，令

    L=C+max(2a,a+b)，M=ceil[e^C p max(p,q)]，δ=1/(16M)。       (3)

则全部c∈[0,C]都有

    max_j dist(tj,S)>δ。                                    (4)

证明：假设各距离≤δ，选素数幂整数N1,N2,N3≥2使|log Nj−tj|≤δ。因e^tj≤M、δ≤1，且e^δ−1≤2δ，

    |N2−pN1|
       ≤|N2−e^t2|+p|N1−e^t1|
       ≤2e^t2δ+2p e^t1δ≤4Mδ=1/4<1。

同理|N3−qN1|<1。两差是整数，故N2=pN1、N3=qN1，和前段矛盾。所有量是固定p、q、C的显式数，不读取未知零点，不选择moving test。

同一论证也适用于a=m log p、b=n log q（m,n为正整数）：把p、q在(3)中的倍率分别换成P=p^m、Q=q^n。关键是P、Q有不同素数基底，不是只需a≠b；commensurable单素数长度不触此反测。

## 3. Exact support迫每个循环SCC只有一个prime标签

取同一strongly connected component中的两个非空闭词A、B，分别基于v、w，且l(A)=a、l(B)=b。强连通给有限路径S:v→w、T:w→v，置

    c=l(S)+l(T)，z=a(S)a(T)，x=a(A)，y=a(B)。

S/T可以为空；v=w时c=0、z=1。三个确实存在的闭词为

    W1=S T A，W2=S T A A，W3=S B T A，
    lengths (t1,t2,t3)=(c+a,c+2a,c+a+b)，
    activities (w1,w2,w3)=(zx,zx²,zxy)。                       (5)

每个word活动权严格正，无论word是否primitive，它在(1)中对应的atom至少有正贡献lγ a(W)>0。故

    supp ν_G⊂S ⇒ 每个非空closed word的长度属于S。             (6)

若同一循环SCC出现不同prime标签的闭词（长度m log p、n log q，p≠q），(5)及§2给一条长度不在S的正闭词，违反(6)。因此：

**Exact SCC定理。** 在(1)合法且support包含于S的正edge-additive图中，每个包含闭路的SCC都存在一个素数p，使该SCC全部非空closed word的长度均属于{m log p:m≥1}。

这不要求图有限、局部有限、活动权有上界或normal transfer operator；也不说整个图无连接。不同SCC之间仍可有one-way edges，孤立的acyclic部分也可保留。正周期测度按循环SCC分解，因为任何closed word都在一个SCC内；这里不推断某个未定义的无穷transfer operator在Hilbert空间上block diagonal。

若进一步ν_G=ν_ζ，则每个prime p必有primitive word γ满足lγ=log p：logp的正atom必须由某γ及k≥1贡献；(6)给lγ=m log r，故p=r^(mk)，唯一分解迫r=p、m=k=1。于是不同prime的这些primitive words位于不同SCC。每个prime可以有多个同标签SCC或多个primitive words，不从atom总质量擅自推出唯一orbit。

特别地，exact ν_ζ不可能由单一强连通的正edge-additive图实现。它可以由各prime独立circle的正图实现，因此本定理不是说正周期measure本身不存在，也不是说其全局解析延拓不可能有非平凡零点。

## 4. 高repeat的primitive系数补偿

不能将一个based word W在ν_G中的贡献写成l(W)a(W)：若W=γ^k，真实项是lγ uγ^k=lγ a(W)。以下引理使高重复和任意edge subdivision不成为漏项。

固定p、q、C及(3)，置

    d=log2/8，I=[d,2d]，
    F={t∈[a,L]:dist(t,S)≥δ}。

I是固定prime-free区间，F是与S分离的compact集。可选一个**只依p、q、C**的函数h_C∈C_c^∞((0,∞))，满足

    0≤h_C≤1，h_C=1于I∪F，supp h_C∩S=∅。                   (7)

例如先取包含I∪F且closure与S分离的有界开集，再作有限光滑bump分割；S在有界范围只有有限点，故不存在隐藏的不可分离问题。ν_ζ(h_C)=0。

**Primitive阶梯引理。** 若某closed word W满足t=l(W)∈[a,L]、dist(t,S)≥δ，w=a(W)>0，则

    ν_G(h_C)≥(d/4)min(1,w)。                                 (8)

写W=γ^k，ℓ=lγ、u=uγ，故t=kℓ、w=u^k。

若ℓ≥d/4，则h_C(t)=1，(1)中的对应repeat项给ν_G(h_C)≥ℓw≥(d/4)min(1,w)。

若ℓ<d/4，整数集合J={j≥1:d≤jℓ≤2d}有

    #J=floor(2d/ℓ)−ceil(d/ℓ)+1
       ≥d/ℓ−1≥d/(2ℓ)。

又t≥a≥log2=8d，所以这些j都小于k。对0<u≤1有u^j≥u^k=w，对u≥1有u^j≥1；因此全部j∈J都满足u^j≥min(1,w)。由于h_C=1于I，

    ν_G(h_C)≥Σ_(j∈J)ℓu^j≥(d/2)min(1,w)，

更强于(8)。这只消耗同一primitive orbit的正repeat项，无ordinary trace或总mass假设。辅助agent另独立核了本段系数／计数；它不代总稿fresh或root消费。

## 5. 线性通信费与全部短返回路径的sup

仍固定p、q、C，并假设marked闭词A、B的活动权满足

    x≥η0，y≥η0，0<η0≤1。                                   (9)

连接路径活动积z>0无需下界或上界。三个活动权(5)都至少zη0²；由(4)选中一个off-S word，再用(8)，得到共同固定测试下界

    ν_G(h_C)≥(log2/32)min(1,zη0²)
             ≥(log2/32)η0² min(1,z)。                        (10)

因此原初稿同时假x、y、z≥η的版本是(10)的较弱直接后果；无需为增强线性费用再计一轮。

可以在同一层对所有返回路径选择取sup。给marked base vertices v、w定义

    Z_(G,C)=sup{a(S)a(T):S:v→w，T:w→v，l(S)+l(T)≤C}，        (11)

空集合取0，允许值+∞。这是**最佳单条roundtrip的activity product之sup**，不是所有路径activity之sum、容量或graph norm。因为(7)的h_C对每一pair相同，(10)逐pair成立，故

    ν_G(h_C)≥(log2/32)η0² min(1,Z_(G,C))。                   (12)

sup不必达到：对z逼近sup后利用min(1,z)的连续单调性即可；若sup=∞，右端仍有界。非局部选择路径、随graph/model改变、任意长edge-word或细分均已包含在(11)内。

**Cofinal通信定理。** 设G_j为以上合法正图，每层有marked闭词A_j、B_j，长度固定为logp、logq且activities共同满足(9)。若

    ν_(G_j)→ν_ζ 于D′((0,∞))，或正测度vague拓扑，             (13)

则每个first-fixed C<∞都有

    Z_(G_j,C)→0。                                           (14)

证明仅用同一h_C：由(13)及ν_ζ(h_C)=0有ν_(G_j)(h_C)→0，(12)迫min(1,Z_j,C)→0，等价于Z_j,C→0。

等价的路径消费是：若某roundtrip序列的activity product保持≥z0>0，则其总delay必须趋∞；更准确，任何有界delay subsequence都不能保非零activity lower。反向不成立，长或稀薄连接只解除本必要反测，不保证全Weil身份。

定理不要求每个G_j已经有exact support S，也不要求每层ν_j=ν_ζ。它直接控制approximation中bounded-delay、nonvanishing communication，避免把exact SCC结论误套成“每层必须prime分块”。

### 5.1 同一有限测试的近似长度稳健性

若marked lengths a_j→a=logp、b_j→b=logq，结论(14)仍成立。取δ0为(3)，当|a_j−a|、|b_j−b|≤δ0/4时，三个实际word lengths与c+a、c+2a、c+a+b分别相差至多δ0/2。因此至少一个实际length距S>δ0/2。

取固定区间[a_min,L+1]，其中a_min=log2/2=4d；所有大j的三个length均落其中。以δ0/2替换(7)中的δ、以此区间替换[a,L]构造同一个新的fixed h_C。§4计数只需t>2d，故仍有相同常数d/4；其余(10)–(14)原样。这是同一proof的有限裕量消费，不使用moving test或新图参数优化。

## 6. Full fixed-source接口：任意origin接触修复仍不能消去障碍

本节采用root提出、在这里独立核闭的off-origin运输桥。它不声称任意正图已经给出完整Weil分布。原ν_j=ν_(G_j)只假Radon(0,∞)，不据此假设它在0附近质量有限或自动有全R分布延拓。

设每层有一个共同分布W_j∈D′(R)，满足在R\{0}上的实际身份

    W_j = W_Γ+H−(ν_j+ν_j^−)，
    H(u)=2cosh(u/2)du；                                      (15)

W_Γ为原569/577完整Γ的同一off-origin限制，双pole背景H也固定。W_j在0的延拓可依j任意改变：允许任意origin-supported接触修复，不要求其系数uniform，也不要求正measure原积分在0有限。存在全R分布W_j及其全源型本身是本接口的假设，不能由ν_j Radon(0,∞)反推。所有源保原physical du、zero-extension Dlog的compact core、第一槽linear及r#(u)=overline(r(−u))。

假设对全部fixed r∈C_c^∞(R;C)，

    Q_j(r)=W_j(r*r#)→Q_W(r)。                                (16)

**无需每层Q_j PSD。** 四个复平方的polarization给每对fixed r,s上W_j(r*s#)→W_ζ(r*s#)。同一W_j必须共同用于全部源，不能逐源选择不同图或非线性source-map。

先支付任意K=[u,v]⊂(0,∞)上的uniform mass。取实非负φ∈C_c^∞(R)，support为[-1,1]，并在(-1,1)严格正。置B=v/4、A=(u+v)/2、φ_B(x)=φ(x/B)，令r=τ_Aφ_B、s=φ_B。则

    h0=r*s#=τ_A(φ_B*φ_B#)≥0，
    supp h0⊂[u/2,v+u/2]⊂(0,∞)，h0>0于K。                   (17)

因为K位于该支撑区间的内部，c_K=min_K h0>0。全部origin-supported修复在h0上exact0；反射measure也不贡献。由(15)、polarization及目标同一off-origin身份，

    ν_j(h0)=(W_Γ+H)(h0)−W_j(h0)→ν_ζ(h0)，
    ν_j(K)≤c_K^(-1)ν_j(h0)，故sup_j ν_j(K)<∞。               (18)

不必先证明μ_j=ν_j+ν_j^−在0的mass界。有限个初始j的值由原Radon合法性给出，收敛控制尾部，故sup包含全部j。

对任意h∈C_c^∞((0,∞))，取实偶正approximate identity k_ε∈C_c^∞，∫k_ε=1；只取ε充分小，使h*k_ε的support仍在同一个positive compact K。fixed ε时h*k_ε=r*s#（r=h、s=k_ε），故polarization与(15)给ν_j(h*k_ε)→ν_ζ(h*k_ε)。再用(18)及||h*k_ε−h||∞→0，

    limsup_j |ν_j(h)−ν_ζ(h)|
       ≤[sup_j ν_j(K)+ν_ζ(K)]||h*k_ε−h||∞→0。               (19)

于是得到(13)的D′((0,∞))收敛；同一positive compact质量界与光滑一致逼近也给vague收敛。这里没有新的factorization/source定理或近0正measure积分假设。

因此任何以(15)同一off-origin Γ/H/prime拆分、经(16)逐fixed complex平方逼近完整经典Weil型的正图族，都必须支付(14)的通信费。任意只在origin改变contact或有限部分延拓不能消除该固定off-origin反测。完整Γ/contact/pp/双pole的最终身份仍由(16)承担；不能把prime-side正measure叫作Weil正型。

未覆盖的是改变off-origin Γ或pole背景、非局部signed修补、不同source-map或非共同逐源图等机制；它们须另付同目标运输。若声称全部Dlog源身份，比(16)更强；这里只消费必要compact core，不免费给du→graph map范数、算术principal下降或Hodge配对。

## 7. 非空commensurable对照与合法逃逸

令q>1为一个素数幂，统一edge delay为ℓ=logq，两个顶点间四条有向边都存在，edge activity矩阵

    B=q^(-1/2)J，J=(1/2)[[1,1],[1,1]]。

这是强连通正图；J²=J、TrJ=1，故TrB^k=q^(-k/2)。有限closed-word计数给kℓ处(1)的系数为ℓ TrB^k：primitive length m-edge的cyclic class在k-edge based trace中恰贡献m个不同起点，要求m|k，与(1)完全一致。因此

    ν_G=Σ_(k≥1)(logq)q^(-k/2)δ_(klogq)。                    (18)

这是非空的强连通positive mixing单q Euler-factor对照；所有length在同一prime基底上，故不触§2不同素数反测。它不是非平凡曲线完整ζ、不是F5曲线的全Hodge实现，也不证明RH；有限域全周期均nlogq的情况不因本定理被错误排除。

尚未排的机制包括：cofinal返回delay→∞；activities消失；prime atom由越来越多微小orbit分摊而没有单个marked activity lower；signed/supertrace cancellation；非edge-additive或依无限past的roof；一般smooth/singular/pro-/higher flow与Hodge载体；不同source-map或off-origin重整；非normal的global analytic continuation。Origin接触修复在§6的共同全源身份类内已被反测覆盖，不再作为该类的逃逸。Exact measure的prime-labelled SCC分解本身不限制全部外部解析耦合。

当前最强消费只是正edge-additive周期图的exact SCC分类及marked prime通信必要费，附(15)类型下的fullfixed-Weil接口。它不支付独立arithmetic primitive、405全部关系下降、537非根/全源coverage、principal/整截面/mixed RR、危险signed core/cross或Ξ；whole542+555→557 leading4/5负惯性UPPER不变，Goal完成门未闭。

## 8. 前件与交付范围

* 输入：有限closed-word拼接、严格正activity、edge-additive delay、素数唯一分解、ν_G的Radon合法性；没有读取未知零点。
* 量词：p≠q、C、η0先fixed；图可随j任意改变、可数/非局部/path选择无uniform上界；h_C是固定C_c^∞测试，不随图、word或j改变。
* 系数方向：始终使用primitive period lγ而非word period；nonnegative子和给lower，(12)只约束最佳单条return product的sup，不约束总sum/capacity。
* 覆盖：exact支持门和cofinal marked-loop门分别陈述；从ν=ν_ζ存在prime primitive词，不推出cofinal统一marked activity lower。近似length稳健性已由同一δ裕量单独支付。
* Full-source接口：共同W_j∈D′(R)的off-origin限制为同Γ/H减正反prime measure，并有全部fixed complex平方收敛；允许任意origin-supported接触修复，不要求near0 measure质量界。普通trace/positive graph measure/Weil型/Hodge能量不混同。

外部文献/网页/下载/数值0；本稿未重证旧078/079/565/566，强旧净值及是否准入由另独占审查与root消费决定。本文自身不创建合同、计轮或完成Goal。
