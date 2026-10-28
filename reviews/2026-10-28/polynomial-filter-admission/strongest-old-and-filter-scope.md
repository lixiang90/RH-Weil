# Fixed-degree正filter：最强旧、移动系数与分布消费范围

2026-10-28；`/root/moment_fresh_audit` 当前polyfilter独占任务，非phase库存／quiet／出版一致性复用。已恢复README／STATE、check→show、Goal／AQ／frontier及当前规则，核587实际derivative Gram、589两原proof的uniform接口与quiet原量词恢复。没有新web／PDF／章节／下载／数值，不改STATE／Git／cadence。

**限定PASS，分类为更强旧设施直接消费0。** 对任意先fixed d、所有source-independent且系数可随X任意移动的非负real polynomial w_X、deg≤2d，只要同587的g校准趋完整q₀>0，则ν_X=w_Xρ_Xdt趋[q₀/|∫g|²]δ₀于σ(S′,S)，同一估计还给strong dual S′收敛。Physical正型分布趋同系数constant，g′的完整正目标因此失败。本稿直接核全部Schwartz测试及其有界集一致性，未从C052 fixed-pair结论自动升级拓扑；所需强前件已付，未发现实质断点或需新source／数学合同的输入。

## 1. 原对象、factor和精确系数指数

固定d≥0在X极限前选定；允许实际degree随X变化但始终≤2d。w_X在整条real轴非负；real roots的重数为偶，非real roots共轭成对，非零leading coefficient为正，故可选单个complex polynomial

    h_X(t)=Σ_(j=0)^d a_(X,j)t^j， w_X(t)=|h_X(t)|²， deg h_X≤d。

不要求w_X偶、h_X实、w_X(0)>0或roots固定。低degree补零系数，w=0时取h=0；q₀>0的校准排除cofinal零权。Factor choice的常相位不影响结论，不需选择随X连续。这里只使用一元多项式的普通因式，未输入未知ζ零点或附加spectral factor域。

Fourier为rhat(t)=∫r(u)e^(−itu)du，故实际物理源

    r_(X,h)=Σ_(j=0)^d i^(−j)a_(X,j)g^(j)

满足rhat_(X,h)=h_X ghat。它仍支持[-1,1]、端点jets为0、属于原Cc∞及zero-extension Dlog；有限X ordinary trace合法，并保完整Euler Gram inverse／returns。因此

    ν_X(|ghat|²)=T_X[r_(X,h)]。

587已经给每先fixed d、全部complex系数同时有效的actual lower

    T_X[Σ z_jg^(j)] ≥ c_d √X/ℓ^(3d+2) Σ|z_j|²， ℓ=logX。

这里的exponent确为3d+2，源系数的i相位为酉变换。该下界本来就付coeff Euclidean norm，不需偷换原du；如换成导数基上的du／Dlog norm，只改fixed d常数。它不是Gaussian辅助测度的lower，也不是585逐fixed源下界经compactness猜出的一致性。

校准ν_X(|ghat|²)→q₀使它在充分大X≤B₀，于是

    b_X:=Σ|a_(X,j)|² ≤ C_d ℓ^(3d+2)/√X，             (C)
    w_X(t) ≤ (d+1)b_X(1+|t|)^(2d)。                 (P)

第一句是**平方系数norm**的bound；未平方norm只有其平方根的rate。常数依d及固定g／q₀，起点还可依校准序列达到B₀的时间；没有d_X成长uniformity。全部coefficients／roots移动已在587量词和(P)中覆盖。

## 2. 原域与强旧的两个uniform接口

每fixed-X，ρ_X为560同一actual ordinary Sonin density，k_X=2πρ_X。ρ_X=O_X(log(2+|t|))，故w_Xρ_Xdt是正tempered测度，通常全线总质量无限。对Cc∞或Schwartz源的平方／mixed配对有限；degree>0可提高natural form域，不能把全部原Dlog免费送入weighted域。h_X(−iD)是有限阶微分操作，未声称它在原全L²上bounded，也未把固定degree误当有限source rank。

589 headline只付fixed源little-o与fixed-pair均值极限，不够直接判当前class。足够的是它已根闭合的原proof接口：

* 对每个nonnegative measurable W，正差商核／Tonelli及actual投影平方支配给∫Wρ_X≤C∫W[√X+log(2+|t|)]，C独立W／X／source；
* 每先fixed δ>0、B=1，actual full-Gram kernel在δ≤|t|≤ℓ指数小：ρ_X≤C_δexp(−c_δ√X/ℓ)。

第一句先对bounded compact-support W付清，再单调逼近，不要求W是fixed源Fourier平方。proper powers全保原logp权，没有额外k；Γ/contact和原2π规范也保留。第二句只在所给高度内用，δ在X极限前固定。不能拿trial lower或只限fixed-f的tail常数替代它们。

## 3. 全部Schwartz测试：实际补上的拓扑论证

令K=3d+2，p_N(φ)=sup_t(1+|t|)^N|φ(t)|。由(C)、(P)和全局majorant，X≥3时可放宽为

    w_X(t)ρ_X(t) ≤ C_d ℓ^K(1+|t|)^(2d)[1+log(2+|t|)]。

对任意先fixed complex φ∈S，取N=5d+6。显式积分给

    ∫_(|t|>ℓ)|φ|dν_X
       ≤C_d p_N(φ) ℓ^(−3)(1+logℓ) →0。              (T)

这控制所有移动系数，不是将fixed-f Schwartz常数当作family一致性。对于任意先fixedδ>0，中段由actual localization和(P)给

    ∫_(δ≤|t|≤ℓ)|φ|dν_X
       ≤C_(d,δ)p_0(φ) ℓ^(5d+3)/√X
                              ·exp(−c_δ√X/ℓ) →0。 (M)

因而每个φ∈S的δ外加权质量趋0。不能在这里代φ=1并声称ν_X为概率测度或全质量tightness。

Near0不由(C)配central mass硬猜一个bounded量：那种粗乘积还可能带ℓ的正幂。应使用实际校准。令f₀=|ghat|²∈S、m=|ghat(0)|²=|∫g|²>0。选一次fixedδ₀>0使f₀≥m₀>0于|t|≤δ₀，正性给

    ν_X([−δ₀,δ₀]) ≤ ν_X(f₀)/m₀ ≤ B₀/m₀。           (B)

对任意ψ∈S且ψ(0)=0，由(T)、(M)、(B)，对fixed0<δ≤δ₀有

    limsup_X |ν_X(ψ)| ≤ (B₀/m₀) sup_(|t|≤δ)|ψ(t)|。

先X→∞再δ↓0，得到ν_X(ψ)→0。对任意φ∈S，具体选

    ψ=φ−[φ(0)/m]f₀，

便得到

    ν_X(φ)→[q₀/m]φ(0)，即ν_X→[q₀/m]δ₀于σ(S′,S)。  (L)

谱Dirac的下标0是原点，和上述小半径δ₀不是一个角色。此处确实检验了全部Schwartz函数，不需要从卷积平方到一般test的未付factorization。没有moving δ_X、degree_X或改变source的隐藏极限交换。

最强同链拓扑也能明确消费：对任意S有界集𝔅，φ↦ψ=φ−φ(0)f₀/m是连续linear算子，故对应ψ的p_N、p_0及sup|ψ′|共同有界。(T)、(M)的误差于是对φ∈𝔅一致；core由sup_|t|≤δ|ψ|≤δ sup|ψ′|及(B)控制，校准误差乘sup_(φ∈𝔅)|φ(0)|亦趋0。先X∞后δ↓0得到sup_(φ∈𝔅)|ν_X(φ)−q₀φ(0)/m|→0。这正是strong dual S′拓扑，不是凭弱收敛自动贴标签；Fourier也把此有界集一致性运输到physical侧。

## 4. Physical分布、完整目标和最强旧净后果

按冻结规范定义physical分布

    𝓦_X(f)=∫ fhat(t)dν_X(t)， f∈S。

它对r*s*给原W_X(r,s)，其中s*(u)=overline(s(−u))，所以每层是stationary Hermitian正型tempered分布。非偶w也允许；如果另谈它的Fourier测度，应保2π反射，不能把ν_X直接叫物理Dirac。由(L)和Fourier在S上的连续性，

    𝓦_X(f)→[q₀/m]fhat(0)=[q₀/m]∫f(u)du。

Physical极限是同系数constant分布，没有另添／除2π。对全部fixed compact smooth complex源对，因rhat overline(shat)∈S，亦给

    W_X(r,s)→[q₀/m](∫r)overline(∫s)。

取g′，其test t²|ghat|²∈S且在0为0，故W_X[g′]→0；但完整537给q₁=Q_W[g′]≥2^−49162||g′||du²>0。于是该固定卷积平方的缺陷趋q₁，完整Weil D′逼近失败。q₀／q₁含实际Γ／FP-contact、所有Λ(p^k)=logp及双pole；g′ mean0并不polefree。这里只需完整目标的D′固定test，不假设目标属于S′，也不能仅因一个pole项指数增长就断言完整目标整体非tempered。

Class确实非空且包括非constant规则：每fixed 1≤j≤d可取w_X=q₀t^(2j)/T_X[g^(j)]，真实trace正且有限，恰校准g。这个例子在冻结class内，不是另调参数躲失败。d=0则是pure scalar；其full S′后果也已被上述更强uniform旧设施直接支付。C052只明确消费fixed pairs并保留拓扑责任是准确历史；现在显式给出(T)–(B)才恢复这个更强后果，不是凭“automatic D′”修改旧结论。

587 actual moving-coefficient lower、589 actual global／local uniform接口，加普通一元因式／有限维Cauchy／Schwartz尾／正性校准已含全部前件。这里没有新的独立算术／几何来源或未付uniform源估计。不同于scalar的fixed-degree filter class和首次明确的S′结论有实质消费内容，但按最强旧去重应记直接0，而非新C053／590或新一轮。

同链还有一个必要性：若每X允许任意finite-degree非负poly，并假设完整D′逼近，则其degree必须趋∞，不能仅unbounded。否则有cofinal子列degree≤2D，完整逼近在该子列仍给g的q₀校准及g′的q₁>0极限；对先fixed D用上述结论便矛盾。这不支付d_X→∞的uniform估计、成长率或对它的排除；正是保留下来的合法逃逸责任。

## 5. 与其它停门的边界及版本

588排fixed-coercive-anchor的两正项completion；本class是对source-independent谱权作有限阶微分预处理，不是同一anchor projection。553需要global bounded读出及全部Pan消去等准确前提；这里poly可unbounded，且每层正D′本来无须先消Pan，故不用553拒绝它。Phase是旧log-derivative的exact加法分解，quiet是移动源low-energy／K有利负谱；它们不直接替代本任务的全部test收敛论证。Source-degree、source-rank和receiver-rank仍分开。

本判定只限全real轴非负、source-independent、degree有某个先fixed统一上界的规则，允许系数／roots任意移动及任意cofinal子列。非多项式、成长degree、非局部、signed、逐源非线性或不同primitive／mixed机制未被泛排，不据此授其后继预算。K不利正部／T-pole-cross、同一非零primitive／principal／mixed与Ξ仍欠，whole4/5负惯性UPPER未改，Goal原数学门open。

实际版本绑定：当前root规则2973 LF bytes／`32483f5eab0e992e1826cd5c6706bb62f98bba314aa799ef284c4834a0e84076`；587为8681／`e4d30cfb6d07299386014cb4c4e3e3979ab5111264355dfb37b24629f121ac82`；589为7185／`c491012226713baf0eecff045338563d4e440c6a1bde9eea0d9ccf661b958bc5`。C052 upper为10211／`bab769113b4ce8c858dfd4b7a83dea6abd8808436a599d2206ea9a9bf0915fff`，local为11459／`809bc7ffc6f1fbf4dd24af0d710af05fb7ca1bc259992430c3fd6760912ffcb1`。当前另一独占terminal `uniform-measure-and-domain-proof.md` 9735／`275a18e512cd9368e42399ac191c998cfbe44208e3458c89928107bd933fadde`已全文读，系数／tail／near0及原规范与本核一致。

本稿仅交当前准入及最强旧消费意见，不替root结算或发布。原cadence3/history53/latest589/formal17不动；不续C050／C052／phase／quiet参数或来源队列，不结束长期Goal。
