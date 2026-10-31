# 单一 global relative-K 源公式准入：指数单位有实际lift，普通boundary不承载primitive

2026-10-31；`/root/global_core_formula_admission` 独占原稿。同G20261027、冻结0c4f与runtime1793085111。本稿没有创建Goal、数学合同、source队列或轮数，没有修改STATE／cadence／文献库／Git；只写这一文件。父已核前轮最终4eadfba，本稿不把父API观察说成本人重新核远端。

**裁决：未构造出可准入的新独立core输入。** 本次实际选择并检验一个不同于Sym／Clark／FRS的global relative-K公式：把完整Mellin源指数化为quotient单位，再以普通K-theory连接映射产生relative primitive类。该单位本来就有全局指数lift；其连接像对全部源严格为零。这个首检在原生unitized卷积代数中已经成立，不依赖把native源商误认成任意无约束jet乘积。

下述对象、源公式、cheap test和显式lift均实际写出；但属于519／520源商设施加标准单位／relative-K exactness的直接旧角色检验，不能因换成K1／K0记号重领新的RH数学轮。它不证明所有relative K、Hermitian／metric或global cohomology都失败。

## 1. 输入、测试与条件净值先冻结

输入是全部physical复源 `r∈S_exp,C`，以及405实际Gaussian给出的整完成函数 `H0(s)=ξ(s)/2`。物理与raw的关系仍为 `f(u)=e^(−u/2)r(u)`，不改源的du或zero-extension Dlog。定义

    F_r(s)=∫_R exp[(s−1/2)u] r(u)du,
    µ_−(r)=F_r(0),  µ_+(r)=F_r(1),
    H(s)=s(s−1)H0(s).

选择H而不是仅H0，是为了保留两个endpoint／degree坐标；不能把405的h0（两个degree均1/4）和全部principal一并删掉。H的零除子含所有真实ζ非平凡零点及其完整重数，加0、1各一阶；不假RH、simple zeros或spacing。

最便宜测试是在源定义的单位 `U_r=exp(F_r mod H)` 上检查普通连接类

    J_r=∂[U_r]∈K0(A,(H)),
    K1(A) → K1(A/(H)) --∂--> K0(A,(H)).

若这个类非零、能消全部405实际Pan却保537非根，且另有原范数和mixed容量，才有可能超出旧谱商。实际结果更早停止：`exp(F_r)` 已是A里的可逆全局lift，故J_r=0，连537非根也消失。没有把未知正性或未构造principal当成输入。

这是一条global coherent algebra的实际规则，不是仅造一个finite toy；但其失败责任也仅限该已指定普通boundary消费，不扩大为长期Goal的完整方法类边界。

## 2. Native源代数已有显式指数lift

先不扩大到全部整函数。令

    A_nat=Cδ0 ⊕ S_exp,C

为原physical log线卷积代数的unitization，单位δ0，源仍为同一个r。Pan理想取 `P_phys=C(P_an)`，即旧519的完整jets条件再加µ±=0；它是闭卷积理想，不把它声称为A_nat中由单个H对应源生成的principal ideal。令 `B_nat=A_nat/P_phys`。

每个r都有实际卷积指数

    V_r=exp_*(r)=δ0+E_r,
    E_r=Σ_(n≥1) r^(*n)/n!,
    V_r^(-1)=V_(−r).

这是原生代数里的单位，不是只在形式幂级数或Mellin quotient中定义。具体地，记

    a_A(r)=∫e^(A|u|)|r(u)|du,
    p_(A,j)(r)=sup_u e^(A|u|)|D^j r(u)|,

其中A≥0，j≥0。加权Young不等式和把j阶导数放在一个卷积factor上给

    a_A(r^(*n))≤a_A(r)^n,
    p_(A,j)(r^(*n))≤p_(A,j)(r)a_A(r)^(n−1).

故在S_exp的每个实际半范数中绝对收敛，且

    a_A(E_r)≤exp(a_A(r))−1,
    p_(A,j)(E_r)≤p_(A,j)(r)·[exp(a_A(r))−1]/a_A(r),

零源时按连续值解释。逆元由同样绝对收敛的Cauchy乘积成立。由于S_exp控制任意指数权，a_A有限；这里无需额外假设全source共用某个增长率。Mellin变换合法换序后给 `F_(E_r)=exp(F_r)−1`。

取quotient单位 `U_r=q(V_r)∈B_nat^×`，则 `[U_r]` 已在 `K1(A_nat)→K1(B_nat)` 的像中。因此普通relative-K exactness立即给

    ∂[U_r]=0  对每个r∈S_exp,C。

此等式是精确代数等式，不靠boundary像闭、Hilbert范数、连续readout或极限。每个P∈P_phys在quotient中为0，所以U_P=1、所有实际Pan和平移均消；但相同公式也杀掉每个非根源，无法把“通过关系门”和“保primitive”拼在一起。

这里使用underlying unital ring的ordinary algebraic K；没有因为存在指数path就声称`[V_r]=0∈K1(A_nat)`。所需事实只是它在上游K1里有代表，连接映射因此消去；两种论证不能混为一谈。

若把标量r换成任意有限矩阵R∈M_N(S_exp)，使用矩阵卷积和submultiplicative矩阵范数，相同逐seminorm指数收敛也给原生矩阵指数lift。这个说法只覆盖实际指数形式，不声称B_nat的所有可逆矩阵都具有原生matrix log或lift；也没有给N无界的共同norm费用。

## 3. 原du／Dlog费用与537非根负对照

先固定supp r⊂[−L,L]，则

    a_A(r)≤√(2L)e^(AL)||r||_du
           ≤√(2L/log2)e^(AL)||r||_Dlog.

这里Dlog采用全线zero extension，`||r||_Dlog²=(2π)^−1∫log(2+|t|)|rhat(t)|²dt`。这些是原r的真实充分费用；derivative半范数仍需对应的p_(A,j)(r)，不能从du免费领取point／高导数控制。E_r一般已非compact，不能仍叫它支撑在原窗。以上只认证lift存在及其指定representative费用，不将它们冒称所有可能lift的必要lower。

取旧537实际非零 `r0=(D²−1/4)ψ`，ψ为17/16窗内非零compact smooth实源；µ±r0=0且完整Qζ(r0)>0。无需重放证书，当前边界公式已经给J_r0=0。故任何**只经J_r的class-factor mixed读出**都不能还原这个非零Q值；即使readout非连续、有无界gain或逐源选择，只要它确实是该零类上的well-defined读出，仍不能把0变成该目标值。

此处不否定raw lift／secondary metric／额外leg携带信息。若保留整个U_(tr)的framed family，其t=0导数仍是旧F_r mod P；这只是旧完整jets＋endpoint源像，不是普通K0 boundary类。固定t的指数还可能有周期alias，不能无说明宣称单个U_r对全部S_exp源忠实。

完整目标Q始终保Γ=2θ′及FP-contact、全部proper powers、两pole、allcomplex mixed与原du/Dlog。没有从一个可逆单位的模、纤维正metric或K0名称取得这个完整Q的新正号，也没有进行n／rank／L参数优化。

## 4. 额外entire ambient：所有有限可逆jet矩阵可lift，但不是native结论

若另选

    A_ent=O(C), I_ent=(H), B_ent=A_ent/I_ent,

则这是一个实际**扩大后的ambient ring**。对原源的map是 `cδ0+r↦c+F_r`；它不是519／520已证的native源商拓扑同构，更不是保持原du或强半范数的逆。原F_r在每个fixed竖带的虚方向快速衰减；任意wild jet序列未必来自native源。520明确没有把native Fréchet商认成全部无约束jet乘积。

在这个unrestricted entire ambient内，标准离散Hermite整函数插值定理给

    B_ent ≅ ∏_(z∈Zeros H) C[ε]/(ε^m_z)

的环同构。这里是global ring层面，不把Spec of infinite product误称为仅有这些离散点的代数曲线；也不支付任何插值函数的strip增长或源norm。该标准插值定理在本稿只作常用外部数学输入，不声称重新审完其原始证明，不归给519的源重建。

对任意fixed finite N及M∈GL_N(B_ent)，每个node的matrix jet M_z的constant matrix可逆。选一个holomorphic polynomial代表于该node小邻域；缩小邻域，使谱落在有限个避开0的复小域内，并各取log分支。holomorphic functional calculus给该matrix germ的log L_z，模ε^m_z仍满足exp L_z=M_z。此处只要**逐离散node**的log，无需所有node共用branch或global matrix function已知有log。

再对L_z的N²个entry作离散Hermite整插值，得B(s)∈M_N(O(C))，`G(s)=exp B(s)`是全局可逆entire matrix（逆exp(−B)），且G mod H=M。由此

    GL_N(A_ent)→GL_N(B_ent)  满射， 对每个有限N；
    image[K1(B_ent) --∂--> K0(A_ent,I_ent)] = 0。

若每stage rank有限而随stage增长，仍逐stage为同一精确零像；不需要先有rank一致上界。但插值过程没有给stage共同增长／范数，不能偷偷运输成native arbitrary-unit的结论。对本次source指数U_r，上一节已有更便宜的native lift，根本不用此全GL_N附属事实。

结论仅是**该ordinary连接映射的像为零**。不声称整个relative K0为零、不替其它relative／higher K或HP作计算、不宣布所有metric／Hermitian class或non-entire growth-constrained对象平凡。

## 5. 实际line/module解释与不应合并的角色

仅为核普通clutch的方向，可在entire ambient取代数double ring

    D=A_ent×_(B_ent)A_ent,
    L_U={(a,b)∈A_ent² : a modH = U·(b modH)}。

U的全局unit lift v=exp F_r给显式D-module同构

    D→L_U,  (x,y)↦(v x,y),
    L_U→D,  (a,b)↦(v^(-1)a,b)。

所以其底层rank1 projective module是自由的；relative连接类也因v存在而为零。这是实际代数模，不将SpecO(C)、analytic plane、算术curve和primitive载体混为同一个几何对象。若固定两侧frame而禁止v，framed U仍可非平凡，但那是另一个target／允许同构规则；不能一面用v消Pan，一面又在非根处忽略这个同构。

这与旧post-601 framed Hecke规则的结论方向一致：保frame精确重呈现旧完整jets，忘frame全局gauge连非根也一起平凡化。旧574／575还已有实际非proper覆盖上的非平凡线／Cartier族，以及对所有源可延拓的指数primitive成为relative coboundary的明确首检；因此不得把“原来完全没有relative对象”作为本门的新归因。

两种旧对象并不是本次A_nat或A_ent本身，不能把它们的全部Pic分类、C* ideal factorization、chainnorm或K类计算直接搬来。本稿的零boundary由当前actual lift独立核出；旧资产提供的是更强的已知source角色及去重对照。

## 6. 强旧净值与保留的逃逸

短依赖链为：519完整jets和双degree接口→520真实Fréchet谱／Jordan而非无约束product→553原norm／cofinal费用及实际Q partner责任；574／575和post-601展示global gauge／raw frame／primitive类不能混消费。加上标准卷积指数和relative-K exactness，本候选无需新算术估计已被决定。

源消Pan合法、lift有实际代表、强拓扑和全部端点可保，都不因此得到独立section有效性／mixed RR。其普通boundary全零使537覆盖门失败；与fullζ或自然成长窗的关键比较没有新增正号、signed净费用或whole后果。旧whole542+555→557 leading4/5仍为**负惯性UPPER**，不等于PSD、比例或负谱lower；primitive／principal／sections／mixed、危险corecross与Ξ没有改变。

所以本稿建议**单候选强旧／类型0停止，不准数学合同**。不是新的完整核心方法类边界，不满足Goal任何完成门。没有外部paper／作者章节／下载／数值或新文献项；没有加数学轮或重置宏观周期。

保留而未构造的修复包括：native quotient中非指数且不可lift的实际数据；growth-constrained／non-entire允许gauge；额外metric、Hermitian、secondary或真正relative/higher objects；独立的mixed算术有效性／RR身份及原费用。它们当前不是输入，仅指出本门不能排它们。停止本公式，不自动打开这些子题、rank／frame／growth参数或来源门。

本次没有发现可继续执行的新独立core公式；明确缺的是一个**不能被当前允许的global source lift先行平凡化、同时具有实际同源mixed容量或危险signed比较**的输入。把这种未付条件直接命名为“nontrivial K／metric／global realization”不改变选择。Root应消费本首检后再决定全局下一步，不把本稿出稿当新结果或授权。

## 7. 实际阅读和执行限制

本人读当前README／STATE、执行check→show、读Goal／macro21／latestAT及实际工作树；只按父任务进行这一公式准入。实际旧证据读取范围：519全文；520§§1–3（尤其native谱／非product范围）；553§§1–5；574§§1–8；575§§1–8；568§§1–3及匹配cocycle保留语；post-601 principal-actual-formula的公式／Pan／frame／费用与停止范围。Koszul原件和旧inclusioncone只作不同对象的范围负对照，不作为本次K1 lift证明。

早期数次rg使用Windows wildcard path而失败，随后用rg --files定位实际文件；失败locator不构成不存在证据。没有重新审旧nested证书、全部作者证明或整个库。父消息中曾提出“519/520 native A≈全部无约束jet product”的待验想法，本人指出其growth差别；父确认不消费该错误前提，本稿始终将unrestricted entire ambient另列。没有已root消费结论需要由本稿自行回滚。

本稿为terminal原件，root须逐项核实际版本／依赖并与其它当前审查对齐后才消费。没有待运行计算或可继承后台handle。

下列版本只绑定本次实读输入，不认证nested证明或原作者来源：

| 输入 | raw bytes | SHA256 |
|---|---:|---|
| goals/GOAL.20261027.md | 9679 | b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de |
| goals/review-cadence.json | 6813 | 0bd41adf77ca1d22895c9a42e808ef3e627c929bc639cce0f782ceaee4aa2041 |
| literature/manifest.json | 221943 | 8d0e293f87c7828d1d6d733b5c967fd3793b06759a730ce26ab5115ed551aac1 |
| notes/519-f1-closed-source-image-and-degree-moments.md | 5766 | 93d39e6d932c9913f5feb77bed4d1ad096c9d984ed571e894576fce6c53b124c |
| notes/520-f1-source-quotient-spectrum-and-centered-growth.md | 6311 | 81a05708dfd2139d374d9fac7f631e66ea4449d502cf9fb0c52f53b900dc9651 |
| notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md | 6613 | 35a40c35d1eaa7fafb462361ddef1bfb9643402b5670f832b9142aeb4b74abce |
| notes/574-actual-adelic-cover-relative-picard-and-source-transport.md | 11880 | b97aa1619f559e22041f5f46404a5ab09e598722e16287059e8691c555eee45d |
| notes/575-regular-cartier-cover-flat-source-and-capacity-gap.md | 13160 | f70e37cb84d4d705a3a9e6fe57c6f1b72bd8f9b02cb3d9ddeb6ac16bb184fd8e |
| reviews/2026-10-29/post-601-core-input/principal-actual-formula.md | 12821 | 5449ad97e57faea997bb6e05b6ce87dd1b65ab9d7e94fb9be07a348bd4c1744d |
| notes/537-source-exact-weil-window-positive-tail-admission.md | 8155 | 269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8 |
