# 实际Weil坏频率：MV高矩来源与旧范围审查

2026-10-14；root在C012止损/cycle10复盘中指定的下一候选来源审查。
再次恢复AGENTS、README/STATE、check/show、Goal/MACRO_FRONTIER/C012及D20261014M；
STATE仍为C012 ready、latest540（root尚在结算541），不能把本入口提前计轮。
本文件独立输出，不改STATE/cadence/Git，不数值生成更大矩阵。

## 1. 结论与可准入的准确新增目标

MV、unique-prime高矩以及浓缩算子本身均为旧工具。定向核查未发现旧件已经证明
“任意k且k可随L/T增长、actual Γ=2θ′、全部primepowers、完整dual pole”的
实际Weil坏频率测度与负惯性联合上界。不能仅因关键词无命中认证新颖性；
需在首轮原推导后只消费该不同对象/成长量词的净后果。

这个入口不假定Weil PSD、RH或无零区域；它研究实际算术多项式在长频窗中的
相消大小，然后付whole-source concentration运输。它有望改巨大但显式的负惯性
上界，而非直接排除最后一个负方向。若首轮只重新证明018或150，不结算新轮。

## 2. 旧件已付什么

| 原证据 | 已付范围 | 不能重复登记或范围外消费 |
|---|---|---|
| 018全篇 | 全primepowers相位多项式二矩、强相干density、中心井宽；明确MV可去H_x | 没有任意k factorial估计；其threshold是θP(x)，不是完整Γ(t)−2ReF |
| 019、021 | packing/调制prolate/Taylor block大筛，逐fixed窗有限core；弱层统一尾 | finite core可极巨大，没有成长high-k算术rank界 |
| 022–024、023全篇 | polarization/resolvent及concentration→低谱/index，奇负pole加一维 | 是一般分析桥；Γ规范有2026-10-13纠正，actual必须用2θ′ |
| 027全篇、028§§1–2 | concentration trace→phase-volume惯性及negative-trace；中心井纯测度门已有严格>1障碍 | 第5节是此旧桥的actual规范消费，不是新运输定理；不能期待high-k平均自动消去中心井 |
| 150§§1–5 | 任意p barrier-capacity、MV weighted二矩、Abel Cauchy高尾缩核 | Abel shift δ_Y/soft cutoff/Cauchytrace不同于actual Q_L原norm惯性 |
| 267§§2–3 | actual soft-cutoff primepower四阶乘积碰撞/weighted能量 | k=2及特定σ/Abel对象；不能假装已付任意k actual sharp Q_L |
| 455§§1–3 | properpowers完整四Schatten费、prime-only等价有限frame预算 | 原AF finite matrix/channel，不是本窗high-k scalar badset |
| hybrid-signed-one-three-physical-resonance-research.md §3及其radial逆审 | unique factor k!与k=2,3 product能量，原physical四词共同Hilbert | 仅fixed k=2,3且有其原输入；本候选不用其暂停的比例/无零优化 |

最后一行说明factorial思想已出现，故不能把unique factor重新命名成新来源。
本次没有重审全部≤538全文，以上是对象相关定向审查。

## 3. 一级MV来源及不能省略的量词

原件为[Montgomery–Vaughan1974, Hilbert's Inequality](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)，
核对Theorem2、Corollaries2–3与§4。Theorem2处理distinct real frequencies及其最小/局部间距；
Corollary2给有限指数和的均值，Corollary3给Σn|a_n|²付款。它不假定素数或ζ零点。
本文只用finite最小间距版本，不假设作者定理给新的prime high-moment结果。

对有限A(t)=Σ_(n≤N)a_n n^(it)，log n间距≥1/N，所以端点Hilbert式准确给

    ∫_[T,2T]|A(t)|²dt ≤ (T+2πN)Σ|a_n|².

起点T不影响常数，因为其相位只乘到coeff上。π/δ的Hilbert界支付两个endpoint，
所以不把2π漏掉；也不要求T≥N才允许用定理。T≥N只是使误差不大于固定主量级。

## 4. actual高矩、properpowers和Γ threshold

令x=e^(2L)，所有sum严格n<x（边界改变不影响下列上界）。定义

    P_x(t)=Σ_(p<x)(logp)/√p ·p^(it),
    V_x=Σ_(p<x)(logp)²/p,
    R_pp(x)=Σ_(p^j<x,j≥2)(logp)/p^(j/2),
    F_x=P_x+P_pp,
    b_L(t)=Γ(t)−2Re F_x(t).

全部primepowers用真实Λ(p^j)=logp；actual pole仍为2(|C|²−|S|²)，
并非藏进b_L，也没有做pole moment zero假设。

将P_x^k按整数乘积聚合。unique factor给每个prime指数向量α（Σα=k）的系数
(k!/∏α_p!)∏a_p^α_p。因为k!/∏α_p!≤k!，逐项平方求和得到

    Σ_n |coeff(P_x^k;n)|² ≤ k! V_x^k
    ∫_[T,2T]|P_x(t)|^(2k)dt ≤ (T+2π⌈x^k⌉) k! V_x^k.

这里k可为任意正整数，常数2π独立于k/L/T；适用于x^k≤T的短多项式区，
即k≤logT/(2L)。prime重复亦在multinomial中，不能假设squarefree。

properpowers不应叫O(1)：j=2的ℓ¹质量为Σ_(p<√x)logp/p=O(logx)，
j≥3由Σp logp p^(-3/2)/(1−p^(-1/2))<∞支付常数。因此

    |P_pp(t)|≤R_pp(x)=O(1+L),    V_x=O((1+L)²).

这两式可只用Chebyshev及partial summation，不需要PNT误差、RH或暂停路线。
若要显式常数，首轮必须独立付款或保留真实有限R_pp、V_x，不能拟合其数字。

对δ>0、T>0，actualΓ单调给γ_T=Γ(T)。若

    u_T=(γ_T−δ)/2−R_pp(x)>0,

则E_(T,δ)={t∈[T,2T]:b_L(t)<δ}包含于{|P_x(t)|>u_T}，从而

    |E_(T,δ)| ≤ min{T,(T+2π⌈x^k⌉)k!V_x^k/u_T^(2k)}.

此处threshold为完整Γ，不是冻结Ω常数，亦不把P_pp按四矩可忽略错用于高矩。
若u_T≤0，必须付整块T，不能写同一Chebyshev分母。负频率因b_L偶对称可精确乘2。

## 5. 必须支付whole-source运输，density不能直接当型下界

取A_x=Σ_(n<x)Λ(n)/√n、D_x=2A_x−Γ(0)>0，则b_L≥−D_x且b_L(t)→∞。
E_δ={t:b_L(t)<δ}是bounded open/measurable集，closure compact，故measure有限。浓缩算子

    B_E=P_L F^(-1)1_E F P_L

为positive compact contraction，Tr B_E=L|E|/π（原Fourier∫e^(-itu)、原L²）。
令θ=δ/(D_x+δ)∈(0,1)，取B_E本征值>θ的全部vectors作为core；
正交补上<b_E>≤θN，所以完整multiplier型≥δN−(D_x+δ)<B_E>≥0。
再加入唯一odd pole锚sinh(u/2)以消除负pole，positive even pole保留。
于是paid一般桥给

    n_-(Q_L) ≤ floor[(D_x+δ)L|E_δ|/(πδ)]+1.

这不是finite matrix通过；它是全部complex闭型域的惯性上界，也是旧027的准确规范消费。
但只有在实际|E_δ|上界已付后才有新信息，Tr/rank非常大也允许至少一个负方向。
若只给相对density，不能省掉T从density到absolute measure的乘数。

全E_δ还需付低频head，并在Γ(t)≥2A_x+δ后的全部tail精确为空；
中间dyadic块才可逐个用第4节。head、terminal cutoff和每块k都须明确。
低频core、source-adaptive carrier及重数均不能因高频平均自动消失。

## 6. 净后果、反事实与首轮停止门

若k随r=logT/(2L)增长，第4节可把旧二矩多项式density换成factorial tail；
这是真实多prime相消来源，而不是免费lower供应器。但结合终止频率
Γ≈log|t|与A_x≈2e^L，所得absolute badset仍可能巨大，不能据density趋零推出RH。
本文件不声称已有最优成长rate或新负index定理已结算。
旧027中心井pure phase-volume门的>1障碍继续有效；actual规范修正需逐式运输，
不能凭half版本数字当新actual认证，也不能用本候选高频均值消除该低频几何责任。

建议首轮只付款一个明确新对象：实际全primepower/Γ/pole的dyadic high-k测度账本，
再经第5节给新成长负惯性上界，并与018–024/150在同一L/Γ规范逐项比较。
若不能取得严格比旧二矩更强的实际成长上界，或只是换对象重证旧capacity命题，
停止这个primary，不以k↑/数值扫描维持。若成功，也只结算新joint upper，
不宣称完整正性、Ξ识别或宏观Goal完成。

这项准入可以改变“完整signed arithmetic仍完全未付款”的局部箭头，
但不能把未知finite core PSD或最后负方向重新包装为已付来源。
无producer、无pending session；本source审查自身零数学轮。
