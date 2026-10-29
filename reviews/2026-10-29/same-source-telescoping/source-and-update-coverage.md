# 596 后的同源 telescoping 首检：有限身份合法，测试方向不自动共同化

2026-10-29；G20261027/runtime1793085111、冻结基线0c4f不变。本稿是 STATE 指定的一次零数学准入分工，供 root 消费；不重审Th6.5、不登记C060/597、不改STATE/cadence/Goal/Git，不启动prime-sum、来源或参数预算。

**结论：停止“直接把596逐prime相加”的准入。** 有限telescoping及每步一般源的严格trace身份都成立；596控制的第q步源是J_qh，终点比较所需源是同一个J_Ph。精确重写成J_qh_(q,P)一般连L²值域都不满足；有限极化和整体平移不改变这一问题。与此同时，旧589已经免费给T_X[J_Ph]≤4T_X[h]的共同上界，不能把所有移动源trace控制都称为未知。未付的是能改变整体signed比较的共同源／cross净估计，不是有限恒等式本身。

## 1. 恢复与消费范围

实际读goals/README和STATE，执行research_state.py check后show，读同一Goal、C059、D20261029Y、当前macro frontier及596结算。当前主合同C059已完成且预算耗尽，cadence为2/history60/latest596/formal19；本分工不消费计数。实际工作树只见root正在推进STATE，不将旧completed合同当新执行预算。

实际读取560第一节、596全文，以及其domain原稿第5–8节的strict trace/update/transport。另读585和589用于确认已有whole/fixed-source资产；本稿不读新的外部原文、不调用6.5后的备注、6.4或§7。原raw-source与过去证明版本不修改。下面的额外计算都是旧560身份、已付strict update和标准Fourier乘法值域的首门比对，不作为新研究轮或实质方法类边界。

## 2. 固定终点、同一物理空间上的有限 telescoping

用大写P表示终点素数，ell_P=logP，先固定complex h∈C_c∞，g_P=J_Ph=h+U_ellP h。取同一个I_P包含其全部支撑；例如supph⊂(−1,1)时I_P=(−ell_P−2,ell_P+2)。每个q≤P都在同一个H_P=L²(I_P,du)上定义

    ΔK_(q,I_P)=K_(F_≤q,I_P)−K_(F_<q,I_P).

每项是560的实际自伴紧算子。按素数顺序只有有限多项，故无任何极限或求和换序问题：

    K_(F_≤P,I_P)−K_(empty,I_P)=Σ_(q≤P) ΔK_(q,I_P),          (A)
    <g_P,[K_(F_≤P,I_P)−K_(empty,I_P)]g_P>
        =Σ_(q≤P)<g_P,ΔK_(q,I_P)g_P>.                       (B)

560的实际身份t_F[g]=qΓ[g]−P_F[g]+<g,K_(F,I_P)g>给每项

    <g_P,ΔK_(q,I_P)g_P>=Δt_q[g_P]+P_q[g_P],               (C)
    P_q[g]=Σ_(k≥1)(logq)q^(−k/2)
                     [R_g(klogq)+R_g(−klogq)].

相加时Δt也有限telescoping，因此(B)只是同一旧身份在两个端点之间相减；它没有自行产生新的估计。Γ=2θ′及FP/contact不改，在同源差分中消去。完整pole若写回Weil型，其值也因同源相减而消去；不是删去pole。

这里F_≤P仍是一个partial finite-prime集合。g_P两脉冲支撑直径略大于logP，全部可见相关可以涉及P以上的素数／素数幂；不能因终点叫P就把(C)或其和直接叫完整Q。560的full-window式仍要求覆盖所有可见properpowers。任何全Q消费都须另保未选项。

## 3. 一般终点源的严格 trace update 确实合法

在第q步反射receiver上，令S_q为实际Π_<q，a_q=q^(−1/2)，V_q为e^(itlogq)乘子，D_q=I−a_qV_q，B_q=2I+V_q+V_q*，

    G_q=(S_q D_q*D_q S_q)|_(S_qH)
       =(1+a_q)²I−a_q S_qB_qS_q ≥(1−a_q)²I.

取任意compact smooth源g，包括固定终点后的g_P，W_g=|hatg(−t)|²。已付560给τ_g=Tr_(S_qH)(S_q W_g S_q)=||√W_g S_q||HS²<∞；不假设bare W_gS_q∈S1。W_g与B_q、D_q交换。一般covariance numerator

    X_q(g)=S_q W_g(I−S_q)B_qS_q
          =(S_q√W_g)[√W_g B_qS_q−√W_g S_qB_qS_q]

是两个HS因子的乘积：第二括号两项的HS范数各≤4√τ_g，故||X_q(g)||S1≤8τ_g。先付实际S1，再由domain稿同一个isometry D_q S_qG_q^(−1/2)、positive compression及有界逆循环，得到

    Δt_q[g]=−a_q Tr_(S_qH)(X_q(g)G_q^(−1)).                (D)

这是已付更新代数的一般源版本，不需要W_g=wB_q，也没有沿bare-product cyclicity。G_q逆在q≥2一致有界，旧成长G_F的所有returns仍包在实际S_q内。

因此本首门不是“没有合法common-source trace”。准确的未付箭头在定量消费：对g_P，

    W_(g_P)=w_h B_P，而不是w_h B_q；
    X_q(g_P)=S_q w_h B_P(I−S_q)B_qS_q.

596闭合的O_h((logq)^.9)恰是B_q两边匹配时的covariance，对应W=w_hB_q和源J_qh。不能将它的第二个q悄悄换成P。若重新推导任意(P,q)上界，必须保logP、logq和源半范数的真实联合依赖，并先比较最强旧whole后果；本门没有准这项新估计。

## 4. 全部 prime powers 的相关也不会逐项照搬

对终点源g_P，精确有

    R_(g_P)(v)=2R_h(v)+R_h(v−ell_P)+R_h(v+ell_P).           (E)

596的q=P、ell_P>diam(supph)时，v=±ell_P给||h||du²，所有k≥2相关严格为零，产生2(logP)/√P||h||du²。

但q<P时，v=klogq不再同ell_P匹配。(E)依赖klogq与0、±ell_P的距离；q<P并不排除klogq接近ell_P，尤其不能统一丢掉k≥2项。这里不是声称每一项必非零，而是原支持论证不再提供其精确消失。P_q[g_P]应按(C)/(E)全部保留；将每步一律写成2(logq)/√q||h||²是错误换源。

## 5. 最便宜的实际 pole-zero 值域反测

独立选任一非零、非负、实偶ψ∈C_c∞((−1/100,1/100))，定义

    h=(D_u²−1/4)ψ.

两指数矩∫h(u)e^(±u/2)du经IBP为零，所有平移保零；h是合法固定physical smooth compact源，非零。Fourier侧

    hat h(t)=−(t²+1/4)hatψ(t).

若|t|≤π/log2，则cos(tu)≥cos(π/(100log2))>0于suppψ，故hatψ(t)>0，从而hat h(t)≠0于该区间。这一步不使用数值、零点假设或新外部来源。

对任意不同素数q<P，设t_q=π/logq。J_q=I+U_logq的Fourier乘子m_q(t)=1+e^(−itlogq)在t_q有简单零点，而

    hat g_P(t_q)=[1+e^(−iπ logP/logq)]hat h(t_q) ≠0.       (F)

若前括号为零，则logP/logq为正奇整数，P=q^(2j+1)，对不同素数矛盾。因此若g_P=J_qv且v∈L²，则几乎处处hatv=hatg_P/m_q；由连续非零分子与分母的简单零点，该商在t_q附近绝对值≥c/|t−t_q|，平方不可积。故这个实际合法双pole-zero测试满足

    g_P ∉ Ran(J_q:L²→L²)，q<P.                            (G)

这比“可能没有uniform h_(q,P)”更早：对这一测试，连exact L²重参数都没有，更不可能免费得到compact smooth h_(q,P)。任何整体平移只添不为零的Fourier相位，仍保留(F)的非零；有限个J_q输入的线性组合仍在J_q值域，所以用有限极化／有限和也不能制造该exact测试。

但(G)不是全部逼近路线失败。m_q只有离散实零点、几乎处处非零，J_q在L²中单射且值域稠密、不闭；可以有有费近似。若近似输入范数始终有界，weak compactness会给exact L²原像，与(G)矛盾，故exact-limit近似不能保持有界输入norm。这里不量化逼近率，更不否定随(q,P)付费、非局部／joint或另一测试设计。要消费这种逼近，必须另付输入norm/半范数、误差的实际ΔK或trace运输、以及两极限次序；596的fixed-h常数没有包办这些费用。

## 6. 极化、平移与最强旧免费上界的准确范围

596的有限极化对先fixed h_i在同一个q下给

    <J_qh_i,ΔK_q J_qh_j>/w_q →2<h_i,h_j>du.

所有槽都经同一个J_q；它不产生<g_P,ΔK_q g_P>或跨q的共同Gram，也不给压缩余补空间／coupling。q变化时正方向子空间E_qV和operator本身一起变化，不能将各自min–max计数相加为同一总算子的惯性结论。

将P先固定再让q→∞不符合有限和q≤P的覆盖要求；让P→∞则是三角参数域，需要联合控制。即使个别重参数h_(q,P)存在，逐fixed h的O_h与起点也不能当作该三角族的uniform常数。平移不改变两脉冲的间距logq，不能把logq换成logP。

另一方面，旧positive trace已经给非常实用且无需新合同的whole上界：对所有finite F和所有P，

    0≤W_(g_P)=w_h B_P≤4w_h,
    0≤t_F[g_P]≤4t_F[h].                                  (H)

这是正压缩的算子次序，所有迹都用HS／positive compression。589给先fixed h的t_X[h]=O_h(√X/(logX)²)，故(H)对所有P同时给t_X[g_P]≤C_h√X/(logX)²；若∫h=0，旧589更给统一于P的o_h(√X/(logX)²)。它不要求g_P先fixed、没有source-width费用，是现成最强旧whole资产，必须在任何新联合估计前扣除。

(H)及有限telescoping还给|Σ_(q≤P)Δt_q[g_P]|≤4t_P[h]+4t_empty[h]（粗但已付）。所以“完全不知道common-source trace sum有多大”不准确。未付的是在完整Γ/pp/pole与实际K同对象比较中，对共同源的有利净signed后果／cross，而不是又一个比(H)弱的正trace上界。新596的邻接signed比较仍是新结果；本首门并未推翻它，也不重领它的数学轮。

## 7. 准入判定、停止与可改变选择的证据

有限exact身份(A)–(D)与全部norm/domain合法，故不因“源不匹配”否认telescoping本身。直接应用596把第q步主项相加的推理则在测试源、pp相关和联合常数三处不成立；(F)–(G)给一个实际双pole-zero反测，排除免费exact重参数修补。

因此本门零数学止，不自动启动prime-sum证明、C060/597、另一paper/章节、δ或指数优化，也不宣称一般Sonin／signed／resummation路线数学上失败。能改变这项停止的具体输入可以是：在同一个g_P和共同I_P上的实际两尺度covariance／cross身份及量化净预算；有费逼近连同同对象误差运输足以胜过(H)的whole后果；或新的算术primitive/principal/mixed、独立正D′完整缺陷规则。只给另一个O_h(logq)^α而仍只作用J_qh不能付款。

原du、zero-extension Dlog、全部Γ/contact、properpowers和pole范围保持；safe-high实际运输仍是旧付。长期关键primitive/principal/sections/mixed、危险core/cross和成长Ξ未改，whole542+555→557仍仅leading4/5负惯性UPPER。同一长期Goal继续active/open；root统一审查、保存状态与发布，本稿不代其完成。

## 8. 实际输入指纹

下表由本分工现场对原始UTF-8/LF字节计算，冻结读取版本，不代替证明或root消费；当前STATE因root正在执行不绑定为不变输入。

| 输入 | bytes | SHA256 |
|---|---:|---|
| goals/GOAL.20261027.md | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| goals/contracts/C059-critical-prime-sonin-covariance.md | 2011 | `376a3bc8f3504e2d071d8c30ad81579c78c7488cb2d2b93c80d7dee008972be8` |
| goals/reviews/2026-10-29-critical-prime-596-settlement.md | 3721 | `811b56c38cb38061c8831aaff8f06aeeabebfe8fae1628a00c0e032ef70b2130` |
| notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md | 9263 | `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3` |
| notes/585-cofinal-sonin-fixed-source-trace-lower-and-core-error-fee.md | 7857 | `5dca916d978eef599587ff4c6ce34144f814ddec0567a4c1b2314dcd71cd01af` |
| notes/589-sonin-zero-mean-upper-and-scalar-rank-one-limit.md | 7185 | `c491012226713baf0eecff045338563d4e440c6a1bde9eea0d9ccf661b958bc5` |
| notes/596-critical-prime-sonin-covariance-and-signed-increment.md | 9094 | `b609b8e5a820ca259c1a02fce134ca5b788d4c3373b933b6e1d2c3094cc4a782` |
| reviews/2026-10-29/critical-prime-covariance-proof/toeplitz-trace-and-transport.md | 24003 | `3946f4d843f86e7d2991b39db8ba4acf31ab1d9bb666c0a57b2e4eabddd6a977` |
| reviews/2026-10-29/critical-prime-covariance-proof/root-consumption-scope.json | 12083 | `80d5ec2ddc9d6e134640e581cbd8123d723f252708f163678b3d0daac9bb3f63` |
| goals/review-cadence.json | 6749 | `a5cfcd0ca0f2a4ad63f6c7b60d55c83024ebb86387f0a12a0b7b167e6f3cf600` |

本分工终态：只写本稿，无STATE/cadence/Goal/Git修改，无后台或自动后继。原稿冻结后交root按实际字节消费。
