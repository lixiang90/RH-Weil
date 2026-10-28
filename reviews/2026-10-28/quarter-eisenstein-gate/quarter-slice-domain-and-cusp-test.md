# Quarter packet：literal域、threshold源矩与最便宜cusp测试

2026-10-28；`/root/moment_fresh_audit` 当前独占准入审，不是C052复核续算。已恢复README／STATE、check→show、同G20261027/runtime1793085111、Goal／frontier、AK和589结算。当前没有C053或新数学／来源预算；仅核给定literal规则。未改共享稿／STATE／Git／cadence，未web、下载、重审Zagier／Garrett全文或追后章。

**结论：literal fixed-Y packet合法；s=1/2点值可去不能代替unitary spectral coefficient的L²域。最便宜cofinal测试确为μ₋阈值：r₀有logY主项，而指定polefree r_*无该主项。把原packet明确接到545的direct式及旧theta恒等式，下面的局部延拓可闭，此测试是强旧组合的直接后果，宜旧0止，不另开cusp估计合同。** 545未原文列出这个rank1极限；此处明列必要输入和延拓，不能只凭标题或“预期”消费。

## 1. 版本与实际范围

按UTF-8 LF核对：root准入稿 `root-quarter-packet-and-old-admission.md` 3051 bytes／SHA256 `b778a43ace0eee08e2c520ebc4a1b054013a16a4841a32aa345c334520df2270`；545原件13140 bytes／`25b778a2c1d1b9360ff2dd553f853a33c0dda7575740ab3aeac6ec46f555acfa`。

旧必要接口为 `reviews/2026-10-14/c016-first/cusp-completion-and-norm-audit.md` 的constant term／half cancellation、whole-L² fixed-Y packet界及DIRECT延拓规范（27094 bytes／`7bc8fe9d148d52804187975774a71e3f194242e8f23a32ac49b22b936f254ae0`），以及同目录 `whole-frequency-packet-and-object-gate.md` 的§9.2–9.3（26409 bytes／`a99a83f01cb27479d74557150b11b34dc6a1893a1f3fa83aa1fb5d99ab0ba46f`）。本次只消费这些具体接口，不重新读取其后其他候选。537为原小窗完整coercivity，8155 bytes／`269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8`。

## 2. Z、参数和fixed-Y定义

Z(w)=π^(−w/2)Γ(w/2)ζ(w)在w=0、1的residue分别为−1、+1；entire ξ(w)=w(w−1)Z(w)/2是另一对象。当前E*=Z(2s)E的常数项准确为

    Z(2s)y^s + Z(2s−1)y^(1−s)。

它在s=1/2的两个constant poles内部相消，E*(z,1/2)有限，其constant mode为√y[log y+γ−log(4π)]。这不是零向量；相反uncompleted E(z,1/2)=0。E*仍在几何s=0、1有简单极点。不能用entire ξ的名字删除这些极点／jets，或把几何s=0、1与actual w=0、1的两pole型混同。

冻结s_t=1/4+it/2使2s_t=1/2+it是经典ζ变量。unitary Eisenstein line却是Re s=1/2，其2s在Re w=1；quarter resonance不自动是自伴Laplace的L²谱点。

令p(t)=s_t(s_t−1)=−3/16−t²/4−it/4，故|p(t)|≥3/16。旧545的entire family为F(z,s)=s(s−1)E*(z,s)，且它的truncated packet map已在全部L²(R)输入上付fixed-Y HS界。以输入Fourier系数F_r(t)/p(t)代入即可得到当前E* packet：该乘子bounded，无未知critical ζ除法。其physical inverse一般不保compact support，因此只能用旧whole-L² fixed-Y界，不能直接套旧fixed-L、全部Y统一的incomplete-seed overlap界。

在𝔽_Y上旧constant-mode truncation没有改变函数，故V_r的积分及G_Y的complex极化合法，原du／Fourier因子1/(2π)不变。有限Y的G_Y是正Gram；它一般是双频kernel，未支付平移不变性，不能自动叫一变量positive-type tempered D′。完整目标仍可用所有fixed源对的必要极限检验，不要求每层先成为stationary分布。

## 3. Unitary改写的threshold条件

把参数移到s=1/2+it/2时，原physical Fourier系数被迫成为F_r(t−i/2)，不是F_r(t)。若以uncompleted E写同一unitary packet，其spectral coefficient为

    a_r(t)=F_r(t−i/2) Z(1+it)。

在t=0，Z(1+it)=1/(it)+O(1)，因此ordinary L²(dt)系数域需要

    F_r(−i/2)=μ₋(r):=∫e^(−u/2)r(u)du=0。

对固定compact smooth r，此条件消去简单阈值pole，余项在0附近有界，双尾由Γ和F的下降可积。若μ₋≠0，a_r不在普通L²；点wise E(z,1/2)=0只使乘积的固定z integrand可去，不能把这个不在L²的系数投入unitary Plancherel后宣告全cusp norm有界。合法contour改写也须保这份threshold账本；s=1/2没有E* pole不表示源矩自动消失。

因此最便宜原始测试是：核μ₋(r₀)≠0的G_Y[r₀]至少clogY，而μ₋(r_*)=0的G_Y[r_*]=o(logY)（bounded已足够）。旧fixed-Y O(√Y)粗norm及逐点half cancellation单独都不支付这两句。下面给出对当前具体规则足够的短旧链，不把unitary L²想象当作证明。

## 4. 实际direct输入与非compact域闭合

旧函数方程给

    E*(z,s_t)=b(t)E(z,3/4−it/2)， b(t)=Z(3/2−it)。

定义h=r*k，hat h=F_r b，其中Gamma积分的绝对Re w>1表达给

    k(u)=2e^(3u/2) Σ_(n≥1) exp(−πn²e^(2u))， hat k(t)=b(t)。

这不是对critical ζ作inverse；b是旧545已经付双尾的bounded multiplier。经典theta Poisson恒等式直接给

    k(u)=e^(u/2)−e^(3u/2)
           +2e^(u/2)Σ_(n≥1)exp(−πn²e^(−2u))。

记μ_a(r)=∫e^(au)r(u)du。r固定compact，故u→−∞时

    h(u)=μ_(−1/2)(r)e^(u/2)−μ_(−3/2)(r)e^(3u/2)
           + O_r(exp[−c_r e^(−2u)])

（调整c_r可吸收固定指数前因子）；u→+∞时h及其必要导数有superexponential tail。h∈L²，但μ₋≠0时不在旧compact-source域，也不满足负端weighted overlap积分有限。这正是不能漏掉的threshold，不能用“h∈L²”偷拿全部Y统一旧界。

需要的是旧DIRECT的局部延拓，能够不用那个错误界闭合。取0≤χ_N≤1的smooth compact cutoffs，h_N=χ_Nh。对每fixed Y，545的全L² fixed-Y bound给T_Yh_N→T_Yh。旧compact-source DIRECT给

    T_Yh_N = P_Y[Θg_(h_N)−k(h_N)·1]，
    g_h(v)=v^(3/4)h(−log v/2)，
    k(h)=(6/π)∫h(u)e^(u/2)du。

这里k(h_N)→k(h)绝对成立；g_h(v)在v↓0有C_r exp(−c_r/v)界。每个𝔽_Y内coset height至多O_Y((c²+d²)^−1)，因此Θg_(h_N)有与N无关的可求和Gaussian majorant，局部L²可取极限。由此在每个𝔽_Y上得到同一实际未截断packet

    V_r=Θg_h−k(h)·1。

该步骤使用固定Y全L²连续性与局部domination，没有套非compact h的旧fixed-L uniform-Y界。并且

    k(h)=(6/π)F_r(i/2)Z(2)=μ_(1/2)(r)，

因为Z(2)=π/6。原DIRECT residue 6/π和原packet的2π因此一致。

## 5. Cusp测试的强旧直接结果

上述theta式使identity seed在y→∞准确有

    g_h(y)=μ₋(r)√y−μ_(−3/2)(r)+O_r(√y e^(−c_r y))。

非identity项不添另一个√y主项：height为v=y/[(cx+d)²+c²y²]≤1/(c²y)，小v指数界给

    Σ_(c≥1,d) exp[−c_r(c²y+(cx+d)²/y)]
       ≤ C_r√y e^(−c'_r y)。

允许放宽为全部整数对只增大此absolute upper。于是整个实际packet在标准cusp宽度1上一致为

    V_r(x+iy)=μ₋(r)√y−μ_(−3/2)(r)−μ_(1/2)(r)
                 +O_r(√y e^(−c'_r y))。

固定compact基区的积分已合法。按原dxdy/y²积分，只有√y×√y产生logY；mixed与constant项都可积。因此对全部先fixed compact smooth complex源对，旧链直接给

    G_Y(r,s)=μ₋(r) overline(μ₋(s)) logY+O_(r,s)(1)。

这是cusp主项的实际参数／源运输，不是从半点值或正Gram猜rank1。r₀为固定正bump，μ₋(r₀)>0，故α_Y=q₀/G_Y[r₀]合法且趋0；normalized fixed-pair极限为

    α_Y G_Y(r,s) → q₀ μ₋(r) overline(μ₋(s))/|μ₋(r₀)|²。

它是指数源矩的rank1配对，和589 Sonin规则的均值rank1不是同一输入。此配对通常不平移不变；不能冒作stationary spectral δ或自动的全部D′拓扑收敛。

对题定r_*=(D²−1/4)ψ，分部积分精确给μ_±(r_*)=0；r_*非零（compact支持的ψ不可能满足ψ''=ψ/4而非零），且仍在537原小窗／Dlog合法域。它未必mean0，故不是偷用589或删mean代删pole。G_Y[r_*]=O(1)，从而α_YG_Y[r_*]→0；但完整537给Q_W[r_*]≥2^(−49162)||r_*||²>0。当前literal scalar规则因这个固定完整test失败。

## 6. 准入判定与保留范围

固定Y存在／范数运输本就是545旧输入的bounded重编码；cofinal结论在原545文字中未显式列出，却由上述同一direct恒等式、Gamma／theta及必要局部域延拓直接推出。这里没有新的独立算术输入，也没有理由再开新source或C053付一个被强旧组合覆盖的cusp upper。root若消费，宜记当前具体规则旧0停止；不是重计一数学轮。

若只保“预期cusp主项”而不保第4节非compact局部延拓和第5节coset majorant，则logY rank1不得标proved；本稿明列并核了这两项，避免把conditional单位谱域当结论。全Y fixed-L overlap界仍不适用于h；该限制没有被消除，而是使用正确的局部连续性绕开。

本test仅排给定quarter-slice／原r₀ scalar校准／原𝔽_Y规则，不排不同seed、完整signed或nonlocal响应、其他正D′机制及primitive主线。完整Q的Γ／FP-contact、所有proper powers和双pole仍在target；μ_±=0只使当前固定test的完整pole项为0。whole4/5负惯性UPPER、signed/corecoupling／primitive-mixed与Goal门均未改变。原cadence3/history53/latest589/formal17保持，不由本审、旧链展开或文件数增轮。
