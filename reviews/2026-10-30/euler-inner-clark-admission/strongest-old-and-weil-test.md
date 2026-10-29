# Euler-inner/Clark：独立强旧比较与完整 Weil 首检

2026-10-30；独立任务 `/root/euler_clark_oldnet`。同G20261027、runtime1793085111、原冻结0c4f。本稿只写本文件，没有读取平行的actual-inner-generator.md，没有修改共同STATE、cadence、Goal、库或Git，没有外部paper/PDF/章节、数值或后台进程。

## 1. 结论与计功建议

此候选确有独立的正载体和共同源规则，但其canonical Clark正测度在原物理时钟上的极限是Lebesgue测度；相应source分布是δ₀、源型是原du恒等型。全部边界相位α都统一如此，允许α随X改变或作正概率混合。它不匹配完整经典Weil型。

**建议作为标准构造＋强旧接口的直接准入old0停止，不为这个候选另授C066/603。** 这不是声称079、592或594的原定理已经逐字包含本Blaschke候选。它们并不同类；真正决定本首检的是标准Schur/Herglotz连续性、一个直接的乘积趋零检查，以及132/136早已要求的arithmetic germ识别与560已经支付的非flat完整目标。没有新的未付signed估计或实际principal/mixed机制在本候选中闭合。

若root按整个任务的实际新责任另作计轮判断，应保留这个区别：不能因为推导短就自动抹去新责任，也不能因为第一次写下一个正模型，就把标准定理的直接代入制造成新的核心方法边界。本稿只消费当前canonical family的首检；不排所有inner、Clark、canonical system或变时钟修复，不操作计轮。

## 2. 恢复、阅读与旧资产的真实范围

按AGENTS读README/实际STATE，运行check后show；读完整Goal、已耗尽C065、AO、当前frontier段和execution-start。当前准入是formal21允许的一次实际公式建设，不是C065续算，亦无C066/603预准。父线程独立核运行Goal和先前e02515dd发布；本子任务不自行认证父工具观察。

实际读取132、136、137、079、592、594全文；078读取§1–5的模型与存在性责任，§6实现尾不作数学输入；560、537全文。最初组合输出中部截断，随后单独重读132、136及079/592/594；不把截断输出当全文。以下版本绑定只认原字节，不冒充所有nested原文重新审查。

| 旧资产 | 已付的最强责任 | 不能直接套成什么 |
|---|---|---|
| 078 | 实际有限图companion、Hodge惯性及存在性/正性分层 | 不给经典ζ的canonical自伴Hecke对象 |
| 079 | prime-local Schatten/regularized determinant；无零全纯Euler族的非零正常极限仍无零 | B_X本来有零且趋恒零；不能直接援Hurwitz排它的Clark谱 |
| 132/136 | 正实/Pick结构、Poisson/Cauchy加权normal-family；必须另核原Euler/Gamma arithmetic germ | 正实函数存在或normal limit存在本身不识别ζ |
| 137 | Dirichlet singular-inner等距半群、完整signed current的outer-Toeplitz负能量接口 | 不意味着所有由这些inner因子生成的正测度自动是完整Weil分布 |
| 592 | positive edge-additive周期图的SCC/通信边界；fixed-square到off0 mixed读出的严格桥 | 本候选没有给出这样的正edge-word时间规则，不能直接归图模型 |
| 594 | prime-linear ordinary-S₁自伴共同源的whole fixed-pair HS必要退耦 | Clark联立根位置/模型算子不是该自伴prime-linear pencil；normal/unitary等逃逸原已保留 |
| 560/537 | 原du/Dlog、Γ/contact、全部pp、双pole及完整fixed窗目标；小窗正性已付 | 不能以任意独立正Hilbert型替换同一完整Q_W |

本候选因而值得实际构造首检，不能仅依据594标签拒绝；但首检仍须扣除标准结构和既有目标信息。

## 3. 精确对象、canonical权及普通计数

对X≥2，a_p=logp、q_p=p^-1/2，定义

    b_p(z)=(e^(ia_p z)−q_p)/(1−q_p e^(ia_p z))，
    B_X(z)=∏_(p≤X)b_p(z)，Im z>0。

每个b_p是disk automorphism与upper-half exponential inner的复合；B_X为真正内函数，在实轴附近解析且|B_X(t)|=1。对α∈T取

    H_(X,α)(z)=(α+B_X(z))/(α−B_X(z))，Re H_(X,α)>0。

本稿使用Poisson规范

    Re H_(X,α)(x+iy)
       =a_(X,α)y+(1/π)∫ y/((t−x)²+y²) dμ_(X,α)(t)。

有限X时B_X(iy)→c_X=∏_(p≤X)(−q_p)，|c_X|<1，故H_(X,α)(iy)有有限极限，a_(X,α)=0。没有藏在∞的正线性通道。α取任意相位，c_X永不等于α。

令B_X(t)=e^(iφ_X(t))，选择连续相位提升。直接微分每个Möbius因子给

    φ′_X(t)=Σ_(p≤X)a_p (1−q_p²)/|e^(ia_p t)−q_p|²
           =θ_X+2Σ_(p≤X)a_p Σ_(k≥1)q_p^k cos(ka_p t)，
    θ_X=Σ_(p≤X)logp。

包含全部proper powers，系数是原logp·p^(-k/2)，没有平方自由积主项。相位密度是加法的，不代表实际Clark谱根位置逐prime相加。联立方程B_X(t)=α确实有全product dependence。

φ′_X严格正；φ_X从−∞到+∞，每个根t_k满足φ_X(t_k)=argα+2πk且简单。由H在该根的局部展开，

    H_(X,α)(z)=2i/[φ′_X(t_k)(z−t_k)]+O(1)，
    μ_(X,α)=Σ_k [2π/φ′_X(t_k)]δ_(t_k)。

这是canonical Clark权。普通谱根计数ν_(X,α)=Σ_kδ_(t_k)是另一个正测度；不能删除导数分母后仍叫同一canonical测度。以下source型采用原Fourier规范F_r(t)=∫r(u)e^(-itu)du，

    Q_(X,α)[r]=(1/2π)∫|F_r(t)|²dμ_(X,α)(t)≥0。

系数r仍是原physical源，没有第二次半密度或Γ加权。该正谱型合法，不等于已付Q_W，也不自带principal边或全Pan下降。

## 4. 标准Herglotz极限：相位不能改变flat结论

固定η>0。对y≥η和充分大p，uniform所有x有

    |b_p(x+iy)|≤(p^-η+p^-1/2)/(1−p^(-η−1/2))
                   ≤3p^-min(η,1/2)。

尾部每个因子最终≤1/2，其余因子≤1。只需素数无穷，不需PNT，便得B_X→0在每个upper compact局部一致，甚至对所有x、y≥η统一。于是

    sup_(α∈T)|H_(X,α)(z)−1|
       ≤2|B_X(z)|/(1−|B_X(z)|)→0。

这一步是实际有限乘积的标准Schur→Herglotz变换，不涉及未知ζ零点。

严谨处理measure continuity可用Cayley坐标ζ=(z−i)/(z+i)。正实disk函数H_(X,α)(i(1+ζ)/(1−ζ))的有限Herglotz测度σ_(X,α)满足

    σ_(X,α)(T)=Re H_(X,α)(i)→1，
    σ_(X,α) ⇀ normalized Haar measure，uniform α。

证明只需Taylor系数给各Fourier矩趋Haar、总质量有界，再用三角多项式在连续函数中稠密。实轴上的对应为dσ=dμ/[π(1+t²)]；∞的atom对应上节a项，各层为0且极限H=1也无∞atom。因此μ_(X,α)→dt在vague意义下，uniformα。

“H局部一致”本身不是任意source谱积分的全频结论；这里必须继续付款尾部。对r∈Cc∞，(1+t²)|F_r(t)|²在compactified实轴连续并在∞为0，故上述有限测度弱收敛直接给

    Q_(X,α)[r]→(1/2π)∫|F_r(t)|²dt=||r||du²，uniformα。

这已足以否定全部fixed smooth源的完整Weil匹配；没有将仅vague measure convergence偷换成全频平方积分。

## 5. 需要原L²/Dlog域时的标准连续费

可以在不做新rate或operator-norm收敛的前提下闭合全部先fixed compact L²源。令

    c_*=(1−1/√2)/(1+1/√2)>0。

Poisson kernel的上下界给所有X≥2、所有t

    c_*θ_X≤φ′_X(t)≤θ_X/c_*。

邻根间距≥2πc_*/θ_X，单atom权≤2π/(c_*θ_X)。故任意长度ℓ的实区间J满足

    μ_(X,α)(J)≤2π/(c_*θ_X)+ℓ/c_*²≤C(1+ℓ)，

常数uniform X≥2及α。特别有统一单位区间质量上界。对固定有界I及r∈L²(I)，F_r∈H¹(R)，且Plancherel给

    ||F′_r||₂≤(sup_(u∈I)|u|)||F_r||₂。

单位区间的标准H¹点态上界，加有限重叠求和，因此给

    ∫|F_r(t)|²dμ_(X,α)(t)≤C_I||r||du²，uniform X,α。

这里F_r有连续代表，因为compact r同时L¹；没有把一般H²的任意boundary值视作可付费取样。先对Cc∞用上节全频极限，再用这个统一连续型费与Cc∞在L²(I)的稠密性，得对每个先fixed r∈L²(I,C)

    sup_(α∈T)|Q_(X,α)[r]−||r||du²|→0。

包含原Dlog，但只是一切fixed源的强型收敛。未证明整个unitball的operator norm收敛、moving源速率或growing-I共同费；不能从这一步领602那种不同拓扑责任。

同一单位区间质量上界也支付Schwartz测试的统一尾，故μ_(X,α)→dt于S′，uniformα。定义共同source分布

    W_(X,α)(h)=(1/2π)∫hat h(t)dμ_(X,α)(t)，

便有W_(X,α)→δ₀于S′、从而D′(R)。在autocorrelation平方上与上述Q完全一致。全部complex源及polarization已包含，不依赖逐层消Pan或ordinary determinant。

## 6. 普通计数、正归一化和相位混合的准确范围

写A_X=2Σ_(p≤X)a_p q_p/(1−q_p)，则|φ′_X−θ_X|≤A_X。因为q_p/(1−q_p)→0，按正权a_p的Cesàro论证得A_X/θ_X→0；有限head除θ_X消失，tail由任意小常数支配。仍不需要PNT。

所以全部canonical atom权相对2π/θ_X统一趋1，(2π/θ_X)ν_(X,α)与μ_(X,α)有相同vague/Schwartz和fixed-source极限dt。未归一化普通计数的平方积分则按θ_X发散。这个相位平均/计数clock没有生成原Γ频密度或完整双pole；不能把除去θ_X说成免费恢复了Weil谱。

任意α_X∈T、以及任意逐X的正概率相位混合，都仍有相同flat fixed-source/D′极限，因为上文对α统一。若在这些canonical正型上再乘共同scalar c_X≥0，并要求全部fixed源有有限非零极限，则选一个固定非零r₀便迫c_X有有限极限c；所有源的极限只能c||r||²。c_X→0只给零，c_X→∞使该r₀发散；不收敛的c_X不能同时匹配完整共同目标。有限正混合的总质量归入同一c_X即可。

这里没有研究水平/纵向变时钟、删改Clark权、source依赖重新归一化、另添arch/relative/signed对象等修复。特别将z替换λ_Xz且λ_X→0会破坏固定upper compact中的高度下界，不在上述B_X→0量词内。不能将α统一误写成所有clock/normalization方法都失败。每源另配任意scalar也不再是一条共同分布或共同Hermitian源规则。

## 7. 完整目标为何不是cδ₀：使用强旧，不造新反例轮

560原规范的完整Q_W含

    q_Γ(r)−Σ_(p,k)logp p^(-k/2)[R_r(klogp)+R_r(−klogp)]
       +2|<r,cosh(u/2)>|²−2|<r,sinh(u/2)>|²。

这里Γ是actual2θ′/完整contact，全部proper powers及indefinite双pole都保留。候选flat型只剩c||r||²，没有从原目标中合法扣去这些项。

无需另做数值或高频研究，560§5已有足够强的同源负对照：其原normalized h_R、g_R±均为compact smooth，选窄支撑使全部actual pp相关exact0，(∂²−1/4)结构使两pole矩exact0，而完整Γ仍给

    Q_W(g_R±)=log R−log(2π)+O(R^-1)，||g_R±||du=1。

因此Q_W在同一固定小窗的smooth单位球上无上界，绝不是任何有限c的恒等型。给定c，先选充分大的一个R，再固定该源；让X→∞时候选极限为c，目标则可大于c+1。没有让R随X移动，也没有删Γ/contact；pp与pole为零是该实际测试的严格结果，不是修改目标。旧537小窗正性与此完全相容，正性不等于scalar identity。

也可以用592/594已经付过的两槽mixed读出看off0：完整Weil源分布保有每个±klogp的原负prime原子，而cδ₀没有。这是差/极化测试，不能谎称某一个卷积平方本身为负。主裁决不需要扩大这个读出或重新计算旧535/595反例。

## 8. 净后果、止损与未付箭头

本次真正查明的是这一个actual positive generator的arithmetical identification在首门失败：canonical重整取得了flat germ/flat源型，而非完整Euler–Gamma–pole对象。B_X具有joint nonlinear谱位置，所以不能把它草率归入594的自伴prime-linear禁止类；但标准Herglotz极限加旧目标的非flat性已直接拒绝它，不需先研究新principal或mixed RR。

强旧132/136早已区分“positive/passive结构存在”和“同一arithmetic germ正确”；137的inner等距半群也保留完整signed current的负部未付，未承诺任意positive spectralization就有正确算术身份。本稿把这些标准与已付接口代入具体候选，并没有证明原长期责任的新严格边界。故建议首检old0止，不续phase/clock/权/rank/来源，不把合法但错误的positive模型计成新的Goal完成。

当前仍未付同一非零primitive的physical→principal/Green、整数sections/mixed、实际signed core/cross及自然成长Ξ；whole leading4/5仍是旧负惯性UPPER。此候选失败不排其它独立positive D′生成规则，也不要求逐层Pan消去或ordinary trace。运行Goal保持原实例active/open；是否计轮、root消费与发布由父线程办理，本稿不自行改变任何状态。

## 9. 本次实际输入原字节

下表在定稿前由本任务实际重核；不含正在并行生成、本人未读的另一原稿。原件与标准直接计算是数学证据，hash只固定版本。

| 文件 | bytes | raw SHA256 |
|---|---:|---|
| goals/GOAL.20261027.md | 9679 | b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de |
| goals/contracts/C065-whole-window-onebody-return-budget.md | 2164 | f61a822da11878e951c4307328862f162ff04f26e3150d241b389fc562e46f3e |
| reviews/2026-10-30/euler-inner-clark-admission/execution-start.json | 1850 | c2c28a1b1db31619fcc87f83118f4cb54e4389804f91590c9672b56a66ba1f0d |
| notes/078-ihara-ramanujan-hodge-structure.md | 7932 | c38f97f987b8a326b508359bba708463798b144afc8ddd6f24a8695ad3ce61bb |
| notes/079-prime-orbit-schatten-normal-limit-no-go.md | 9005 | 74dab279e8ef02306dea15249342a5ff1d9198ddf5db94e92496095bc3834edb |
| notes/132-shifted-passivity-abel-resonance.md | 10313 | 764f4526d61534b7daea63e24771bc954a5f6f63f0612dd189a47058439d738e |
| notes/136-cauchy-weighted-passive-defect.md | 10260 | 334b1846ec7a0d83f7c203bdf3261d4a35ac9385b5d1f62aee601ec8eb5d5e97 |
| notes/137-cayley-inner-toeplitz-polarization.md | 10222 | df34b9c791ba7617681fc84cedfe496c8a437765ebdafc58dd6db301215e213f |
| notes/592-positive-graph-prime-period-separation-and-communication-cost.md | 6273 | a9e612c6d47d7a2cfd116d59a9c1045019f91908b3edbc049c9b5aef849ef7e9 |
| notes/594-selfadjoint-signed-euler-source-hilbert-decoupling.md | 7731 | 1f3dde7dfca350b062dbbe3763cd55e9322a694e5438ad6aae9f75f848121f9b |
| notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md | 9263 | 9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3 |
| notes/537-source-exact-weil-window-positive-tail-admission.md | 8155 | 269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8 |

本稿终态：只写本独占文件；没有后台进程、外部来源、新合同、计轮、共同状态或Git操作。提交parent消费，不把文件存在当root已审结。
