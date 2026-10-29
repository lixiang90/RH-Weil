# 同源 telescoping：独立 fresh 范围与最强旧审查

2026-10-29；G20261027/runtime1793085111，冻结0c4f。本分工只审 STATE 指定的零数学同源累积准入，不重开 C059，不建 C060/597，不启动 prime-sum 估计、来源或参数。独占输出为本文件，STATE/cadence/Goal/Git 均未修改。

**结论：限定 PASS，直接相加596的准入应停止。** 有限算子求和、共同源的严格迹域和旧的累计端点上费都合法；未付的是把596的各自共振测试换成同一终点测试后的实际算术相关及有符号净比较。两原稿没有将这一缺口扩大成全部 Sonin 或 signed 累积路线失败，也没有把旧共同源上界藏成新待证命题。596本身及其有限 Gram／收缩阈值计数保持已付。

## 1. 实际恢复、独立推导和原稿消费

实际读 goals/README、STATE，运行 research_state.py check 后 show；读同一 Goal、已完成 C059、D20261029Y、macro frontier、596结算和596全文。其后独立重导：共同区间上的有限 telescoping；一般终点源的 HS 因子及精确投影更新；J_q 的 Fourier 乘法值域反测；正压缩次序给共同源端点上费；不同正方向不能相加的有限维负对照。

得到两作者冻结通知后，实际全文读当前文件并现场重算原始字节：

* source-and-update-coverage.md，12084bytes，SHA256 `22921e747890d05d3ff4975a2e004ae27e8becc461da2a51c2bd4bd6ba4d111a`。
* strongest-old-and-whole-consequence.md，11861bytes，SHA256 `695398d0e2efd46ee5dc03bdfbdae7dceace2ab8eb1a2ddf88fb32e649463441`。

两份均为 UTF-8/LF。没有用作者消息、终态标签或文件存在代替原稿。另读560§1、585全文、587§1/§5–6、589必要上界及其 fixed-pair 范围、591定理入口、555完整原型/row norm入口及557的强旧消费纠正；596域稿§5–6用于核严格迹更新的原消费边界。没有读新外部原件或596已排除的6.4、§7、备注指数优化。以下判断使用已有证明，不重验整部历史。

## 2. 对象、norm 和共同空间

首固定 complex h∈C_c∞(R)，终点P为素数，L_P=logP，g_P=J_Ph=h+U_(L_P)h。物理源在原 du 范数及 zero-extension Dlog 域；receiver 取实际 Sonin Π_F 的反射 Mellin 表示，measure 为 dt/(2pi)，不能把 raw 整函数评价向量当作源。

每个终点使用同一 I_P 包含 g_P 两个支集。对所有 q≤P，在 H_P=L²(I_P,du) 上定义 ΔK_(q,I_P)=K_(F_≤q,I_P)−K_(F_<q,I_P)。560的实际 K 是同一全线有界 C0 乘子 ε_F 的区间压缩，所以不同区间之间的零延拓和压缩兼容。特别 I_q⊂I_P 时，596第q步的测试完全可以合法放入同一个 H_P；问题并不是“这些算子不能放在同一空间”。

实际缺口是作用方向和余补空间：596给 ΔK_q 在 J_qh 或先固定有限族 J_qh_i 上的型值，求和需要在同一个 J_Ph 上的型值。整个 source domain、投影、乘子和系数都不因共用 I_P 而改变。没有新 arithmetic class、principal 映射或关系／商的全源覆盖被引入。

## 3. 有限 telescoping 与一般源严格迹域

首固定P后，只有有限多项，无无穷求和或换极限费用：

    K_(F_≤P,I_P)−K_(empty,I_P)=Σ_(q≤P)ΔK_(q,I_P),
    Σ_(q≤P)Δt_q[g_P]=t_≤P[g_P]−t_empty[g_P],
    <g_P,ΔK_(q,I_P)g_P>=Δt_q[g_P]+P_q[g_P].             (1)

P_q[g]始终是全部 k≥1 的原权 (logq)q^(−k/2) 乘两侧 R_g(±klogq)。Γ=2θ′及 FP/contact 在同源差分消去；完整 pole 也只在正确的同源分解相减时取消，不是被删去。

一般 compact smooth g 的第q步更新在原范数下也确实成立。令 S=Π_<q 的反射，D_q=I−a_qV_q，a_q=q^(−1/2)，B_q=2I+V_q+V_q*，G_q=S D_q*D_q S|SH≥(1−a_q)²I。对 W_g=|hatg(−t)|²，560已付

    τ_g=Tr_SH(S W_g S)=||√W_g S||HS²<∞.

由 W_g 与 B_q 交换，

    X=S W_g(I−S)B_q S
      =(S√W_g)[√W_g B_q S−√W_g S B_q S]

是 HS×HS，括号每项范数≤4√τ_g，故 ||X||S1≤8τ_g。随后使用 D_q S G_q^(−1/2) 的实际等距及有界 G_q 逆，合法得到

    Δt_q[g]=−a_q Tr_SH(XG_q^(−1)).                       (2)

没有默认 bare W_gS∈S1；每次循环都在明确的 S1×bounded 域中。(2)不要求 g=J_qh。源 g_P 对应 W_P=w_h B_P，故其 numerator 是 S w_h B_P(I−S)B_q S；596支付的共振情形则是 W=w_h B_q。精确一般式合法不等于已支付任意(P,q)的协方差速率。两原稿准确保留了这个区别。

## 4. 免费换源的实际反测与允许的有费逃逸

独立检查 source 稿的具体例子：非零、非负、实偶 ψ∈C_c∞((−1/100,1/100))，h=(D_u²−1/4)ψ。IBP使两个指数矩为零，平移仍为零；ODE唯一性保证h非零。对 |t|≤π/log2，cos(tu)在 suppψ 上有统一正下界，所以 hatψ(t)>0，而 hat h(t)=−(t²+1/4)hatψ(t)≠0。

对任意不同素数 q<P，在 t_q=π/logq 处，J_q 的乘子 1+e^(−itlogq) 有简单零点；g_P 的 Fourier 值却非零。否则 logP/logq 是正奇整数，迫 P=q^(2j+1)，与不同素数矛盾。故形式原像 hatg_P/(1+e^(−itlogq)) 在 t_q 附近有不可平方积分的简单极点：g_P不在 J_q:L²→L² 的实际值域，更不在 J_q(C_c∞) 中。

整体平移只添非零相位，不修补这个零点；同一个q下有限个 J_q 输入的线性组合仍在其值域，有限极化不能制造该 exact 测试。即使特别选择了有原像的另一源，若原像依赖(q,P)，596的逐 fixed-h 常数与起点也没有覆盖整个三角参数族。先fixed P后q→∞不能覆盖有限和q≤P，而P→∞时确实是两尺度问题。

这只否定免费 exact 重参数。J_q 在 L² 中单射、稠密值域且不闭，允许有费近似；对本固定(q,P)的非值域例子，近似原像若始终 norm 有界，弱紧性和 bounded J_q 的弱连续性会推出 exact 原像，矛盾。因此 exact-limit 近似不能维持有界原像 norm。未量化其费用，也不排付费强源、非局部或 joint 比较。任何这种修补仍须付原像半范数、同一 ΔK 的误差运输及极限顺序。

本例的双 pole-zero 不等于 mean-zero：∫h=−(1/4)∫ψ≠0。因此不能对这一个例子直接用589的零均值 o(s_P)；一般的 mean-zero 子族才有该更强费。两原稿没有误认这两种条件。

## 5. 最强旧共同源控制必须先扣除

对所有有限F和所有终点P，positive compression 直接给

    0≤W_P=w_hB_P≤4w_h，  0≤t_F[J_Ph]≤4t_F[h].          (3)

这不需要596。589的 t_X[h]=O_h(s_X)，s_X=√X/(logX)²，立即使(3)同时统一于任意P；若∫h=0则为o_h(s_X)。再用有限 telescoping，

    |Σ_(q≤P)Δt_q[g_P]|
      ≤4(t_≤P[h]+t_empty[h])=O_h(s_P+1),               (4)

mean-zero 时为o_h(s_P)+O_h(1)。这是绝对值放在和外的 signed 累计端点界，不是 Σ|Δt_q| 的 total variation，也不包含各项的 leading sign。

560加上 |qΓ[J_Ph]|≤4∫|Γ(t)||hat h(t)|²dt/(2pi)<∞ 又给更直接的旧合成：

    <g_P,K_(F_≤P,I_P)g_P>
       =P_(F_≤P)[g_P]+O_h(s_P+1),                     (5)

mean-zero 时同样可用o_h(s_P)+O_h(1)。由 ε_empty∈C0 的原 bounded 乘子与(4)也能重导它。若只把“共同源累计 trace 上费”重新挂牌为未知，就会漏掉(4)/(5)；本次两个原稿已恢复并明确消费这些最强旧资产。

whole-K 的正方向也已有比收缩阈值更强的旧结论。587在 fixed I0 上给每 fixed j 的正本征值 lower c_j√P/(logP)^(3j−1)−C_j→∞。由 ε_F 压缩兼容及 I0⊂I_P，零延拓后 min–max 将同一 lower 运输到 K_(F_≤P,I_P)。因此在这个 whole-K 对象上仅报正方向数趋∞或收缩阈值计数，不能算新净后果。它不蕴含596的相邻 ΔK 新结果；两个对象不能互换。

## 6. 正方向、proper powers 与 full Q 的剩余责任

596的有限 Gram 给同一步q的 J_qh_i 两槽；子空间和 ΔK_q 随q一起变化，不控制负余补空间或与其它步骤的 cross。纯线代对照 A=diag(w1 I_m,−2w2 I_m)、B=diag(−2w1 I_m,w2 I_m) 各有m个高于对应 w_i/2 的正本征值，但 A+B=diag(−w1 I_m,−w2 I_m) 为负，连相互交换都不够。它只否定一种不合法的逻辑相加，不是 actual Sonin 反例、whole方法类边界或596反例。

算术腿亦不能换源。R_(g_P)(v)=2R_h(v)+R_h(v−L_P)+R_h(v+L_P)。只在q=P且两簇分离时，k=1两侧相关给 ||h||du²、k≥2为零。对q<P，klogq可接近L_P，原证明不能统一删除proper powers或把每项都换成2(logq)/√q||h||²。

F_≤P是合法 finite-prime 部分集合，却未必覆盖 g_P 的全部可见相关。单个双脉冲的支撑直径略大于logP，可涉及q>P的相关；若要求整个 H_P 的完整型，还须覆盖整个区间相应的更大可见集合。全Q消费必须保留未选prime powers和两个pole，或另证它们精确消去。(5)不付这些尾与净比较。

K正增量在 Q=t−K+pole 中是不利误差。K、ΔK 有正方向并不证明Q负；正trace的共同端点上费也不证明Q正。强旧542＋555→557的leading4/5负惯性UPPER保持，不能只拿555 issued leading1作弱对照；安全高频的实际原du运输继续作为已付输入。Primitive/principal/整sections/mixed、危险core/cross和成长Ξ仍未解决。

## 7. 准入、计数和停止边界

两原稿经此独立推导与现场版本核对后，限定 PASS，无需要阻止本门结算的实质缺陷。本门应按标准旧身份、正压缩次序、Fourier值域及线代负对照的**准入范围核对0数学轮**停止。596仍是原来的一次新数学资产；不重领其增量、极化或min–max，也不因本首检生成C060/597。

唯一cadence实际原字节仍为6749bytes/SHA a5cfcd0ca0f2a4ad63f6c7b60d55c83024ebb86387f0a12a0b7b167e6f3cf600，即2/history60/latest596/formal19；不归零，不是formal20。文献135条不增，无新原件下载。Root仍须按既有授权保存证据、更新当前状态／看板／文献范围并执行真实GitHub同步；本稿不认证尚待发布的远端。

本门没有形成新的同源 joint 身份或算术／正分布输入。能改变停止的条件必须超过(4)/(5)和587的whole-K下界，作用于明确共同终点源族，保全部实际pp/coupling及原norm，并给full Q或危险core的新净后果。仅换一个共振指数、给另一个更弱累计 upper，或命名未付cross不满足。

关于曾咨询的后继 endpoint-PNT 方向：本分工没有执行该估计，也不把它预先登记为新数学。Partial cutoff 主项与full-visible尾必须放在同一个净量上比较；双pole-zero带来的continuum moment抵消若只是标准旧身份，不构成晋级依据。若没有事前说明可改变选择的实际净后果，不应以半段新系数开启后继合同。本稿没有另一个已形成的可执行研究后继；root依长Goal另择新实物，不能把刚停止的准入重跑一遍。

长期Goal的完整数学门保持open，不完成、不暂停、不替换；本分工没有调用Goal状态工具，也没有后台shell、数值、来源进程或自动后继。最终结果仅供root实际消费。

## 8. 现场输入绑定

下面表格由本分工现场重算原始UTF-8/LF字节；身份绑定不代证明，当前STATE为root的可变执行记录，不作为冻结数学输入。

| 输入 | bytes | SHA256 |
|---|---:|---|
| goals/GOAL.20261027.md | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| goals/contracts/C059-critical-prime-sonin-covariance.md | 2011 | `376a3bc8f3504e2d071d8c30ad81579c78c7488cb2d2b93c80d7dee008972be8` |
| notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md | 9263 | `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3` |
| notes/585-cofinal-sonin-fixed-source-trace-lower-and-core-error-fee.md | 7857 | `5dca916d978eef599587ff4c6ce34144f814ddec0567a4c1b2314dcd71cd01af` |
| notes/587-actual-sonin-moment-spread-and-growing-source-rank-necessity.md | 8681 | `e4d30cfb6d07299386014cb4c4e3e3979ab5111264355dfb37b24629f121ac82` |
| notes/589-sonin-zero-mean-upper-and-scalar-rank-one-limit.md | 7185 | `c491012226713baf0eecff045338563d4e440c6a1bde9eea0d9ccf661b958bc5` |
| notes/591-connected-occupation-covariance-three-fixed-test-barrier.md | 5974 | `5a6d6e221369a1a9bce668d56c9fe574aeca0a295fdb7d0ccd31e4fcd03eaa7c` |
| notes/555-actual-prime-weighted-schur-and-growing-weil-inertia.md | 6167 | `55a3745ab8160738e2a2dde15e84290e99205df68f3b59b357d26127846a31c5` |
| notes/557-joint-row-norm-and-gamma-arithmetic-moment-budget.md | 6491 | `5abfd13af9c955b27c5a2ea8f01d2555fa05b1df450adbedbcfe20f62d327166` |
| notes/596-critical-prime-sonin-covariance-and-signed-increment.md | 9094 | `b609b8e5a820ca259c1a02fce134ca5b788d4c3373b933b6e1d2c3094cc4a782` |
| reviews/2026-10-29/critical-prime-covariance-proof/toeplitz-trace-and-transport.md | 24003 | `3946f4d843f86e7d2991b39db8ba4acf31ab1d9bb666c0a57b2e4eabddd6a977` |
| reviews/2026-10-29/same-source-telescoping/source-and-update-coverage.md | 12084 | `22921e747890d05d3ff4975a2e004ae27e8becc461da2a51c2bd4bd6ba4d111a` |
| reviews/2026-10-29/same-source-telescoping/strongest-old-and-whole-consequence.md | 11861 | `695398d0e2efd46ee5dc03bdfbdae7dceace2ab8eb1a2ddf88fb32e649463441` |
| goals/review-cadence.json | 6749 | `a5cfcd0ca0f2a4ad63f6c7b60d55c83024ebb86387f0a12a0b7b167e6f3cf600` |
