# Euler pencil：最强旧扣除与自伴 cofinal 新门

2026-10-29；仅本次具体准入审，不修改 STATE、cadence、合同或 Git。恢复 G20261027、C056 耗尽、D20261029N 和宏观前沿；初始 cadence3/history57/latest593/formal18。Root 后续给出同一 pencil 的自伴／ordinary-S₁ 分支，纳入本稿审查。数学预算与最终结算由 root 裁决。

**判定须分层：** 两投影 signed 例与 exact-pure normal 分类不足以构成新净输入；但“共同自伴、逐层不要求 pure 因子精确、只给完整 fixed-source 收敛”到实际 Hilbert–Schmidt 退耦的分支，有旧记录未付的局部范数后果，可准入一次限定证明门。不能因证明使用标准谱论就把它抹为旧0，也不能把它提前升级为原 Goal 的实质核心方法类完成。

## 1. 最强旧真正已经覆盖什么

已全文核 [078](../../../notes/078-ihara-ramanujan-hodge-structure.md)、[079](../../../notes/079-prime-orbit-schatten-normal-limit-no-go.md)、[592](../../../notes/592-positive-graph-prime-period-separation-and-communication-cost.md)，并核 [565 §§4–5](../../../notes/565-canonical-completion-graded-identifiability-and-independent-energy.md)、[566 §§1–2](../../../notes/566-source-closed-forms-and-full-weil-heat-trace-tests.md)的具体范围。

| 旧资产 | 最强已付后果 | 不能偷渡的结论 |
|---|---|---|
| 078 | 同 q 有限图、selfadjoint Hecke、companion／Hodge 惯性、含边界的 tempered 等价 | 未给独立 log p 多变量 pencil 的交叉生成元退耦 |
| 079 OO–OQ | 实际 prime-block Hilbert 载体、精确 Schatten 阈值与 regularized determinant 缺低迹 | 其载体从一开始已 block-diagonal，未证明一般生成元被迫分块 |
| 079 OR–OS | exact 有限 Euler 函数经无零 counterterms 的全纯局部一致极限仍无零；Sₖ 正常极限同理 | normal-limit 是正常／局部一致收敛，不是矩阵的 AA*=A*A；cofinal trace-source 不自动给 Sₖ 或 determinant 正常收敛 |
| 565 | 超迹虚消及 Jordan 非识别；正 metric／unitarity 要独立付；有限双向 Markov 太窄 | 未给 moving 自伴 prime 生成元的 Hilbert–Schmidt 近投影／混合退耦 |
| 566 | 正闭 jump／ordinary heat-trace 域分开，完整源身份另付 | 未给本次 trace-word coefficients 或矩阵族范数结论 |
| 592 | 正 edge-additive 图的 SCC 素数分离、fixed-C 最佳 individual 返回活动度 sup→0，完整 fixed-source→vague 桥及 long/diffuse 逃逸 | 明确保留 signed；返回 sup 不是整个 sector 的容量、operator norm 或 HS norm；没有 Hilbert block-diagonal 结论 |

因而不能说“079/592 已逐字证明任意 signed Hilbert family 分块”。反之，任何**本来 exactdet 就是有限 Euler 乘积**的方案，若再走079 OR规定的无零正常 renormalization，旧 OR 已直接控制整个目标函数；仅补一个矩阵表示分类不会产生新的 global zero 结论。

## 2. 便宜 exact-pure 门及 signed 玩具去重

有限 pencil T(z)=Σz_p A_p，A_p 在共同正 Hilbert 内积中 normal。若 det(I−zA_p)=1−z，则 normal 谱定理给 A_p=P_p 为 rank1 orthogonal projection。若 full det=∏(1−z_p)，−logdet 的 z_pz_q 系数为 Tr(P_pP_q)，故

    Tr(P_pP_q)=||P_pP_q||₂²=0，p≠q。

这确实从 pure／mixed 条件推出互相正交的 prime lines，而非预设分块；但余下仅为标准有限谱论和二阶系数读取。Root 的 signed 例 A=diag(1,0)、B=½[[1,−1],[−1,1]] 是592 M=2例 P₀、J₂/2 经 diag(1,−1) 同时酉换基，det=(1−u)(1−v)−uv/2 原样不变。仅负 entry 不是新独立实物。

Exact-pure normal 的 cofinal 槽位也只需 fixed log(pq) 系数；不需要592的一般正测度→vague 论证。此 rank1 版本可明确保存为直接准入比较，不据此单开新数学轮。

## 3. 新自伴分支真正少了哪个前件

每层有有限 F_j 及同一个实际 Hilbert 空间上的 A_(p,j)=A_(p,j)*；有限维是子类，也可为 ordinary S₁ 的无限 Hilbert 空间。每层均使用 ordinary trace，不假 uniform S₁、HS、operator norm、维数／rank 上界。未列入的 p 记 A_p=0。整个共同矩阵族可逐层选择；不能逐源另选而没有共同 W_j。

**不要求** det(I−zA_p)=1−z 或 Tr A_p^k=1 在每层精确成立。用同一真实时间分布

    ν_j=Σ_(m≥1)Σ_(p₁,…,p_m∈F_j)
        [log(p₁⋯p_m)/m] (p₁⋯p_m)^(-1/2)
        Tr(A_p₁⋯A_p_m) δ_log(p₁⋯p_m)。

任意 positive compact time 内只有有限 word，所有 product 的 ordinary trace 合法；反向 word 配对使总系数实。只假 off0 的同源身份 W_j=WΓ+H−ν_j−ν_j⁻，完整 Γ/contact、所有 proper powers、indefinite 双 pole 保留；origin contact 可变。不要求 ν_j≥0 或 Q_j≥0。

若全部 fixed compact complex 源的 Q_j(r)→Qζ(r)，四平方极化先给 fixed mixed pair 收敛。所有 wordtimes 位于固定局部有限集合 {log n:n≥2}。对 a=log n 取 fixed 小 η，令 f=τ_(a/2)η、g=τ_(−a/2)η；h=f*g# 在 a 附近且 h(a)>0，避开全部其它 log n、负半轴和0。每层同一 Γ/H 精确扣除，origin contacts exact0，故直接读取唯一 atom；不需 signed TV bound 或一般 D′ 重建。

特别地，对每个 fixed p，纯原子 k log p 只有全 p word，系数为 log p·p^(−k/2)Tr A_p^k；对 p≠q，log(pq)系数为 log(pq)/√(pq)·Tr A_pA_q。因此源假设给

    Tr A_p^k→1（k=2,3,4），Tr A_pA_q→0（p≠q）。

普通 S₁ 足够，不扩到 S₂-only 的未定义一次 trace、无界生成元、regularized/supertrace 或无限 prime 和的未核域。

## 4. 原先未付的 rank-free 范数消费

Selfadjoint 性使本源矩组合为真正的非负平方：

    δ_p²:=||A_p²−A_p||₂²
         =Tr A_p⁴−2Tr A_p³+Tr A_p²→0。

令 P_p=1_[1/2,∞)(A_p)。标量不等式 dist(x,{0,1})≤2|x²−x|（x实）给

    ||A_p−P_p||₂≤2δ_p→0。

S₁ selfadjoint 算子紧，P_p 是有限秩；有限维当然同样。由 ||A_p||₂²=Tr A_p²→1，反三角不等式给 √rank(P_p)→1，故 P_p 最终恰 rank1。这是由实际源二至四矩取得的 HS 舍入，不是先假 exact-pure 或从 normal 特征值 trace 恢复 singular values。

记 η_p=||A_p−P_p||₂、s_p=||A_p||₂→1。有

    |Tr(P_pP_q)−Tr(A_pA_q)|≤η_p+s_pη_q→0，
    ||P_pP_q||₂²=Tr(P_pP_q)→0，
    ||A_pA_q−P_pP_q||₂≤η_p s_q+η_q→0。

因此对每 fixed p≠q，||A_(p,j)A_(q,j)||₂→0，operator norm 亦趋0。没有统一 dim／rank／norm 前件；这是原592 individual-path-sup没有给出的 whole-sector Hilbert norm 必要退耦。若 metric 随层变，范数属于该层实际共同 Hilbert 空间；未付 condition-number／源映射比较时不运回任意 Euclidean norm、原 du 或 Dlog norm。

079 的 exact有限Euler／正常det极限不覆盖这个仅 source-cofinal 的 family；592 的一般 positive graph 也没有上述 moment→HS 舍入。标准谱论是本次证明工具，不能据此把新增的 actual cofinal norm 量词说成已经付过。此分支支持 root 准入一次限定数学门；并非已经新增算术 primitive 或全局 signed 正号。

## 5. 必须保留的实际 normal 逃逸

自伴不能无声放宽成一般 normal。取 j-cycle unitary U_j，H_j=ℂ²⊕ℂ^j，

    A_p=diag(1,0,U_j)，A_q=diag(0,1,U_j)。
    det(I−uA_p−vA_q)=(1−u)(1−v)[1−(u+v)^j]。

各 A 均 normal，任意 fixed worddegree<j 的 pure/mixed traces 已 exact 匹配两素数 Euler；hidden block 的 word trace 只有 j|m 时非零。因最短 hidden wordtime≥j log min(p,q)，任意 fixed compact 源最终看不到它。可另用其余 primes 的正交 lines 补全 ζ 的 cofinal prime 背景。但 ||A_pA_q||₂²=j、operator norm=1，完全不退耦。

这个反例不驳第4节：U_j 通常不是 selfadjoint，且逐层 purelocal determinant 不精确。它是592 long-cycle逃逸的 normal 矩阵写法，非新的反 RH 模型或独立净结果；也不满足079所需 Schatten正常极限。它防止把 fixed trace 看不见的高阶 clock 偷换为消失的 HS norm。

## 6. 准入范围与停止

原两投影 signed 标签去重为旧；新自伴 source-cofinal 分支的具体净增量是二至四矩强迫 rank1 HS 舍入，以及每 fixed prime-pair 的 whole-sector HS 退耦，含合法 infinite-H ordinary S₁／moving rank／共同源适应。若其全链经不同 fresh 和 root 成立，可结算一个完整数学迭代；本支持审计不自行计轮或建合同。

未给 all-growing F 的统一速率、集体 prime 总通信、Ξ、不同背景消去、非 linear pencils、normal 非自伴／Jordan／unbounded／supertrace／cohomological quotient 或 singular limit 的总边界。没有证明 Q_j PSD，也未产生 same nonzero primitive、principal、整截面／mixed RR 或危险 signed core 净估计。Whole542＋555→557 leading4/5负惯性 UPPER 及原 Goal 完成门不因此改变。停止范围须按实际新自伴分支写，不能把仍合法的 normal clock 或其它机制一起排除。
