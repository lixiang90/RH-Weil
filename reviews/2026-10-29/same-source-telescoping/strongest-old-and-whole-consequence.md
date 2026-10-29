# 同源 telescoping 准入：最强旧共同源控制与整体净后果

2026-10-29；本分工只执行 STATE 指定的零数学准入检查，不重开 C059，不建 C060/597，不读新章节或证明 prime-sum 估计。固定 Goal/原冻结0c4f及596为既有输入。结论是：**596不能直接相加给新的 whole-K 或完整 Q 后果；但共同源控制并非全未知，560＋589已经给累计 trace 端点上费，587已经给成长大窗 whole-K 更强正谱后果。** 不得把这些旧付款改名为新进展，也不得以缺逐项速率判定全部 signed 累积路线失败。

## 1. 恢复、阅读和角色

实际读 goals/README、STATE，执行 research_state.py check 后 show，再读当前 Goal、已完成 C059、决策 D20261029Y、宏观前沿入口和596结算。工作树仅观察到 root 正在更新 STATE，没有据此改判数学或发布已完成。子代理 get_goal 返回本子代理作用域 null；这不推翻 root 已现场核验的 active1793085111，也不授权新建运行 Goal。

实际读取560§1、585全文、587§1及§5–6、589全文、591§1–4、555§4–6、557§5–6、596全文，并读596域稿的严格 projection/trace update 必要段。这里不重审已消费的 Th6.5，也不从 platform 状态认证原文。物理源、receiver、finite-F投影、紧误差和关系/商角色保持原消费：没有新增算术类、principal map或全源覆盖。

以下首固定非零 h∈C_c∞(R)，终点 P 为素数，L_P=logP，f_P=J_Ph=h+U_(L_P)h。用同一 I_P 包含其两个支集；所有 q≤P 的 K 差分都在这个 I_P 上定义。每步 q 的前驱集仍是全体 primes<q，而不是只选一列独立投影。

## 2. 真正的共同源恒等式

定义 Δ_q K_I=K_(F_≤q,I)−K_(F_<q,I)，Δ_q t[f]=t_≤q[f]−t_<q[f]。560给每个有限F及共同I上的 exact identity，有限相加合法：

    K_(F_≤P,I_P)−K_(empty,I_P)=Σ_(q≤P) Δ_q K_(I_P),
    Σ_(q≤P) Δ_q t[f_P]=t_≤P[f_P]−t_empty[f_P],
    Δ_q K[f_P]=Δ_q t[f_P]+P_q[f_P].                    (A)

P_q[f]保全部 k≥1 的 (logq)q^(−k/2)[R_f(klogq)+R_f(−klogq)]。Γ=2θ′及FP/contact在同源差分精确消去；pole也只能在正确的同源分解比较中取消，不能删后把部分式叫full Q。紧算子的有限和是同一物理 L²(I_P,du) 上的普通自伴紧算子等式，尚不需要任何无穷求和或极限交换。

每个 Δ_q t 在固定终点源上也有合法 strict trace update。反射 receiver 上置 S=Π_<q，a_q=q^(−1/2)，D_q=I−a_q V_q，B_q=2I+V_q+V_q*，G_q=S D_q*D_q S|SH。源乘子是

    W_P=|hat h(−t)|² B_P(t),

不是 W0 B_q。它与 D_q、B_q 交换，0≤W_P≤4W0，因此正压缩 τ=Tr_SH(S W_P S)<∞。X=S W_P(I−S)B_q S 为S1，直接沿已付HS因子法：

    X=(S√W_P)[√W_P B_q S−√W_P S B_q S],
    ||X||S1≤8τ.

两方括号项均HS且各至多4√τ，G_q逆统一有界。因而 exact Δ_q t[f_P]=−a_q Tr_SH(XG_q^(−1)) 继续合法。这里仅重用旧 strict positive-compression/HS 论证，既不接收 bare W_PS∈S1，也没有给 W_P、B_q 双尺度协方差的新速率。

## 3. 不能遗漏的强旧：共同源累计 trace 已有上费

由实际非负密度或positive compression直接有，对任意 finite F 和任意终点平移 L_P，

    0≤t_F[J_Ph]≤4t_F[h].                              (B)

这是 |1+exp(−itL_P)|²≤4 的 exact 旧后果，不需要596。令 s_X=√X/(logX)²，589对先fixed h 已给 limsup t_X[h]/s_X≤4|∫h|²；故

    sup_P t_X[J_Ph]=O_h(s_X),
    ∫h=0 时 sup_P t_X[J_Ph]=o_h(s_X).                  (C)

量词准确是 X→∞、sup取任意终点P，而h保持先fixed；不是任意h_P的uniform单位球。特别代X=P，结合(A)以及t_empty[J_Ph]≤4t_empty[h]，已经得到

    |Σ_(q≤P) Δ_q t[f_P]|≤4(t_≤P[h]+t_empty[h])
                           =O_h(s_P+1),              (D)

零均值时可改为o_h(s_P)+O_h(1)。这是真实的共同源、有符号累计端点界。它不等于逐项的o((logq)/√q)，也不控制逐项absolute variation，但不能被重新写成“没有任何共同源累计控制”。因此只是因596不覆盖逐项J_Ph而继续申请一个同名累计上界，并无新输入或净值。

更直接地，qΓ[J_Ph]的绝对值由4∫|Γ(t)||hat h(t)|²dt/(2pi)一致控制；compact smooth确保该固定积分有限。560和(C)已给

    K_(F_≤P,I_P)[f_P]=P_(F_≤P)[f_P]+O_h(s_P+1),       (E)

零均值时余项为o_h(s_P)+O_h(1)。或者由(A)、(D)加上K_empty的C0乘子界得到同一结论。它是旧560＋589＋|1+phase|≤2的立即合成，不是596的新增whole结果。此处的 P_(F_≤P) 必须保留完整实际相关，不能替换为 Σ_q 2(logq)/√q||h||²。

## 4. 596的方向与两重成长量词

596对每份先fixed h 控制的是第q步在 J_qh 方向上的 quadratic form，以及有限fixed族的 J_q-Gram。首固定终点 P 后，(A)要求的却是所有q≤P在同一 J_Ph 上的值。若令测试的基源依赖(q,P)，596的O_h常数、起点和有限半范数并没有相应uniform量词；不能把“每个fixed h”改成“这一整组随终点成长的h_(q,P)”。

更不能只用有限极化修补这一点：同一步q的极化只覆盖已控制的J_qh_i之间，既不比较不同step的投影，也不自动控制 J_Ph 的跨q矩阵。Exact update中W_P与B_q分属两个独立尺度；596付款的W0B_q三段速率并没有在原收据中变成任意 W0B_P 的双尺度速率。这里只核出现有消费范围，不从该缺项推出不能另证。

对f_P，R_fP(v)=2R_h(v)+R_h(v−L_P)+R_h(v+L_P)。仅在q=P且L_P超过diam(supph)时，新增q只有k=1两侧相关等于||h||²、k≥2为零。q<P时，q^k可落入L_P±diam(supph)附近，甚至fixed小q的proper powers也须保留。故将每个P_q[f_P]换成596 terminal共振的2w_q||h||²，会在套用新trace率之前就改变了实际算术对象。

## 5. 正方向和min–max不能直接相加

596的E_q=J_q/√2有限维测试子空间随q移动。已付结论是 Δ_q K 在该份子空间上最终正，并非 Δ_q K≥0；没有控制其补空间或与其它E_r的cross。因而n_+不是本情形下可相加的数量。

最便宜的纯线代负对照即可排除这种推理：在C^(2m)取w1,w2>0，

    A=diag(w1 I_m,−2w2 I_m),
    B=diag(−2w1 I_m,w2 I_m).

各自都有m个正本征值高于对应w_i/2，但A+B=diag(−w1 I_m,−w2 I_m)严格负。连算子彼此交换也不足以修补。此例只否定“若干signed increment各有正方向⇒sum有相应正方向”的逻辑蕴含，不是actual Sonin反模型或596反例。

若有人想把596转成大窗whole-K“正方向数→∞”，还须扣更强旧。587已在固定I0=(-17/16,17/16)给每个先fixed j：

    λ_j^+(K_(F_≤P,I0))
       ≥c_j√P/(logP)^(3j−1)−C_j →∞.                  (F)

K_(F,I)是同一ε_F乘子的空间压缩，I0⊂I_P时零延拓的compression恰等于旧K_(F,I0)。故min–max直接把(F)运输到K_(F_≤P,I_P)。旧结论已经提供该whole-K的每fixed正特征值发散，强于在同一whole对象上仅报收缩阈值计数无穷。它不蕴含596关于相邻ΔK的新结论；两对象方向分别保留，不能把whole的弱新叙述重领一次数学轮。

## 6. 部分素数集不等于完整 Q

F_≤P对每个f_P当然给合法560部分式，但不能自动给全部Weil型。f_P的两簇相关有lag约L_P±diam(supph)；其中logq>L_P的prime也可能可见。因此只选q≤P不保证支持外所有相关为零。要接full Q，必须把所有实际可见Λ(q^k)及完整pole纳入，或者有已经证明的精确消去；不能只保q=P共振。

即使使用覆盖全部相关的终点集合，旧恒等式也只是 Q=t_F−K_F+pole，仍要付同一对象的净比较。K正方向在其中是不利误差；K或ΔK有正谱不证明Q负。585已经给fixed源whole-K必要正费用；587给共同有限族和秩增长必要费；589给scalar规则的fixed-pair均值极限；591另给共同occupation全类的三测试障碍与正gain必要费。这些准确范围不能互相换成对本joint signed余项的有利控制。

whole负惯性最强旧仍是542＋555→557的leading4/5 **UPPER**。555的issued leading1不是当前可用的最强对照；557已把4/5列作旧资产直接推论。没有新的full-source坏集、原norm算子净费或同对象惯性比较，本次准入不改该上预算；既不报PSD，也不报实际负谱比例或lower。

## 7. 准入决定、可推翻条件和已有test

本门应以**标准旧后果/范围核对0轮停止**：不准把596的各自共振主项/finiteGram/min–max直接求和，不晋级C060/597，不启动参数或prime-sum证明。局部596结果仍为新已付资产；本次未得新算术输入、新净号或更强whole后果。长期数学瓶颈及Goal完成门保持open，cadence2/history60/latest596/formal19原字节不动。

能推翻此次停止的最短实际条件须区别于(D)/(E)：提供一个明确作用于共同终点源族的signed/mixed比较，具备P、q和源半范数的真实量词、覆盖全部可见prime powers及coupling，并在扣除(D)/(E)/(F)后确实给full Q或危险core费用的新净后果。仅重新命名“共同源累计trace上界”并不满足，因为(D)已由旧端点给出。其它独立算术principal/Green两槽或positive-D′完整缺陷输入仍可按长Goal另行竞争；本分工没有形成这种实物。

现有旧资产能当场执行的最便宜test就是已经完成的(A)–(F)：先exact telescope、以(B)恢复终点trace、以589给(D)/(E)、以587嵌入排重，再检查全可见primepowers。它们已经足以阻止错误晋级；本分工没有另一个尚未执行且可改变准入选择的旧test，也不为持续研究虚造后继。没有新源位置、下载、数值或后台进程；唯一新文件是本稿，STATE/cadence/Goal/Git均未修改。

## 8. 实际输入指纹

下表是现场读取原字节的身份绑定，不以哈希替代证明或root消费。读取范围已在§1限定；未声称重验全部历史证明。

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
| goals/review-cadence.json | 6749 | `a5cfcd0ca0f2a4ad63f6c7b60d55c83024ebb86387f0a12a0b7b167e6f3cf600` |
