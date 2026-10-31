# GS 零项缩放波包：实际 current 坐标，类型／强旧0止

2026-10-31；同 G20261027/runtime1793085111、冻结0c4f。本稿只做一个源公式的准入比较，不建 C066/603，不增数学轮。恢复时两个 pending 项的结构检查一度失败，已告 root；root 随后修正共享状态。本稿不修改状态、cadence、看板或文献库。

## 1. 独立来源与精确对象

实际重读并视核作者更新版 PDF4 的 (1.1.12) 及其紧邻限制。原件为 `literature/local/2026-10-31-garcia-sankaran/garcia-sankaran-gfasw-author-corrected-20261031.pdf`，838416 bytes，SHA256 `27b36f4de90f66a9bd28dae2054f43ec5f89ad62cee27e767653c69b39434625`。未读 §2/4/5、κ 定义、证明或引用。

公式明确要求 **V anisotropic**。固定合法 orthogonal GS datum、一个复分支与有限 K-invariant Schwartz 输入；只取论文整数 cycle index R=1，此时 tautological bundle rank=1，c₀=1、Ω⁰=1。写 a=φ_f(0)、y>0 为该实嵌入的标量参数，公式在此特化为

    g(0,y,φ_f) = -a log y · 1_X。

这是具体的常数 (0,0)-current。若 a=0，它恒零；以下取一个 a≠0 的合法固定输入。此无歧义特化不解除一般退化指标的次数运输冻结。尤其没有核 modified cycle 的积分模型、算术类或高度。

对原 physical complex F=S_exp，直接定义而非假定 Weil 右平移规范：

    M_j(r)=∫u^j r(u)du，
    J_y(r)=∫r(u)g(0,e^u y,φ_f)du
          =-a[(log y)M₀(r)+M₁(r)] · 1_X。                 (A)

不加未核实的 e^(βu)，不对全生成级数声称收敛或模性。(A) 的值域只是固定 X 上常数 current 的一维复空间；不是已构造的 physical→算术 divisor/Chow/relative-principal functor。

## 2. 全源存在与原费用

所有 r∈F 的两个矩绝对收敛，积分在常数 current 的每个 C^k 拓扑存在。对 p_(N,0)(r)=sup e^(N|u|)|r(u)|、N>0，

    |J_y(r)| ≤ 2|a|[|log y|/N+1/N²] p_(N,0)(r)。

先 fixed supp r⊂[-L,L] 时，原 du squared operator fee 精确为

    |a|² ∫[-L,L](log y+u)²du
      = |a|²[2L(log y)²+2L³/3]。                         (B)

原 zero-extension Dlog 给相同 squared fee 除以 log2 的充分 upper；不称其精确 Dlog dual norm。不识别此 representative 费用为算术高度或所有 lift 的必要 lower。L、y、几何数据独立；没有无界成长下统一小费。

## 3. 实际 Pan 首检：只是旧矩公式的代入

用405已付的真正非 compact physical 关系 P=(D²−1/4)H，H=e^(u/2)h>0，及全部实平移 P_b(u)=P(u−b)。这些是实际源关系的合法标量／平移，双 pole 矩保持零，不是 compact 交的空检验。S_exp 端点使分部积分成立，故

    M₀(P)=−M₀(H)/4≠0，  M₁(P)=−M₁(H)/4，
    J_y(P_b)=a[(log y+b)M₀(H)+M₁(H)]/4 · 1_X。          (C)

对每个 fixed y，至多一个 b 使 (C) 为零。复线性关系空间包含任意复数倍，所以 **J_y(P_an)=J_y(F)=C·1_X**。若同时保留全部 y，这不过是两个矩的 affine-log-y family；两个不同 b 的矩向量行列式非零，Pan 的两个矩像亦是全部 C²。这没有提供新谱／几何分类。

同一 P_b 的 du 与 Dlog norm 不随 b 变，(C) 随 b 线性增大，因此不存在该固定 y 坐标的全线有限 du 或 Dlog bound。无需错用553的全局 bounded-reader 前件，也不把 source-Fréchet 连续误当全局 du 连续。

固定 sesquilinear 配对若只经 J_y（或上述两矩 family）读出，并要求全部实际 Pan 为 mixed radical，则其整个 pullback 必零：Pan 的像已等于全源像。这个 exact-image 观察只在该 **current-only、同数据** 读出上成立；逐源额外数据或真正不同 target 不在此论证中。

## 4. 最强旧比较与不能消费的结论

405 原关系已给 (C)；574 §4–5 已测试 mean 标签 M₀(P)≠0，并保 Mellin 标签的完整关系公式；575 §5 已区分丢掉 mean 的全源平凡化与保 mean 的关系失败。582 §6 已保缩放 constant 项的 Mellin 导数，不能只删 degree 矩。因而 (A)–(C) 是新引用零项的一次明确代入，**旧矩／有限像机制直接合成，0数学**，不把 source-name 改变当新后果。

553给的是原完成中的全 Pan cyclic 密度及有界读出退化；本候选全局不 bounded，不能直接借它排除。旧 raw-theta-mean root 收据另已区分 strong、原 du／Dlog 与 joint 闭包，并明确未宣称常数 arithmetic Chow 类为零。这里甚至只需有限矩的 exact image；不把 raw-theta 的特定 ±3/4 系数、整体算术 Theta 或冻结的 7.4 身份运输到 GS。

最关键的类型止点是：**J_y(P)≠0 的 current 响应不等于“非 principal”，J_y(P_an) 满像也不证明 GS 算术 mixed 高度全零。** 当前未构造相伴 modified cycles、完整 Green pair、其 principal 同构、算术 quotient 或实际 mixed 高度；合法 principal relation 也不必逐坐标 current 为零。不得借582的 q7 degree 非零／primitive=0，把新高维载体按名称判死。

零项只读两个矩，不能承担全部 physical source 的可见性与经典完整 Weil 身份；537 单个非根即使被看到也不能替全源覆盖。新的非零 primitive carrier、非零 Fourier 模式与有限处协同、actual relative/cocycle、独立 mixed 身份或有费非逐层 Pan D′ 路线均未被本稿排除，也未被准入。

## 5. 裁决与止点

这是一个合法的全部 S_exp→常数 current 源公式，消除了“连一个 literal GS current packet 都没写出”的小信息差；但它没有支付原 principal／mixed 箭头，其全部可判响应又是405/574/575/582的强旧直接后果。停止本零项／矩标签建设，不开非退化渐近、权重 β、R/y 调参、作者后章或另一来源队列。

实际瓶颈、whole542+555→557 leading4/5负惯性 UPPER、危险 core/cross／成长Ξ与三个 Goal 门均未改变。同一 Goal active；本稿不构成全 GS／高维 Green 的严格方法类边界。下一数学准入必须带不同实际 source／principal-mixed 或独立 signed 输入及可改变选择的最便宜测试；未有该实物即不授合同预算。
