# 473：原零点行密度与最终联合包络的独立全文审查

2026-10-08。结论：限定 PASS。完整实读最终笔记、三份数学来源和新检查器，
另回核固定数学源的原 sextic sieve 与 450 的实际 count 公式。
原全行 raw 密度是相对明确 [R]/AFE 前件的新推导；
它在原完整 above-floor 域处处弱于已付最终联合包络。
没有发现阻断，不能据此宣称新无零边界或实际比例。

## 1. 最终证据绑定

canonical UTF-8 LF 只把 CRLF/lone CR 换成 LF，不 trim 或改变 EOF。

| 完整实读对象 | canonical LF SHA-256 | bytes /行 |
|---|---|---:|
| [473](../../notes/473-original-sextic-zero-density-and-final-envelope-comparison.md) | 1b864a1e3891a2d53ad0e7019e91041fb1ec3911ed7c8ec23d43769d594bf8a1 | 5982 /119 |
| [原全行 density 源](hybrid-original-sextic-primitive-zero-density-research-compression.md) | 74ea809c6aef75638dc2bc115af2b592ff4feb999cd15e35adcfa4319235d52b | 20750 /407 |
| [最终包络全域比较源](hybrid-original-density-envelope-dominance-research-root.md) | 6e1352c0f4660239c13f02bad622384c51e2df0035a5739743cb2bc78f76961e | 6103 /151 |
| [高行连续严格证书源](hybrid-high-bin-strict-certificate-research-twisted.md) | f33ace9d5600e5875ea05aa2ae32c0d70cd02610b6637cabcb53633965421138 | 6428 /215 |
| [新检查器](../../scripts/hybrid_detector_density_checkpoint.py) | 48f3823dfd12959e670a4b19e55638f8ef12c3b871522a45f3409036dfcdd3a9 | 12740 /242 |
| [450 actual capacity](../../notes/450-plain-kappa-extension-and-actual-capacity.md) | f16807e0f80461e3005b3173e313218b00f5f86abfa860a4ead79e425dd6bee5 | 来源依其冻结记录 |
| [451 actual feedback](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 | 来源依其冻结记录 |
| [冻结 Cubic 代数模块](../../scripts/hybrid_kappa_feedback_exact_audit.py) | e03d6536378fff4b51625ab71fa5eace9fcbf4fe1156ccb6ae048f03bf96bc68 | 来源依其冻结记录 |

固定数学输入的 canonical LF SHA 为
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
回读其 4701–4724，原 [R] 确切是理想 squarefree、原自然零值的
sextic sieve；系数先于行求和固定，允许 fixed row/support restrictions。
本审查没有重证这个无限分析大筛、标准 primitive Hecke AFE 或整个
原 [R] package。笔记的 [T/R] 范围准确保留这些前件。

## 2. 实际行、primitive zeros 与 powerful 冻结

473 §2 与 density 源 §§1–5 的对象一致：

- 原 sixth-power-free element rows，按理想作 squarefree/powerful 分解；
- 原 presentation、有限 Θ、两个 orientation、固定 S 和 natural zero masks；
- a>51/100 的 bin 已有实际 primitive 零点，才可使用 C(U;a,H)；
- floor 没有该见证，继续使用独立的 O(U) 行数。

deleted Euler factors 的零点位于 Re s=0；正实部的原零点由 primitive
inducing L 给出。principal inducing exception 先按固定 ramification
范围排除。没有把 inverse 大值本身当成已存在的零点。

固定 powerful w 后，M≈U/Nw，R_w=N rad(w)≤(Nw)^(1/2)。
S 外估值 1,…,5 都给非平凡 tame local character，primitive conductor
指数为一；固定 S 内的有限类型先分层，所以导子≈M R_w 的比较
常数对 moving w 一致。powerful parts 的数目 O((Nw)^(1/2))
在最终层计数中恢复，未把原全行换成 BGL 星号 squarefree-row 族。

对任意列 n=c d²，固定 d 后其字符值是模≤1的 row factor；
natural zero 值留下 fixed row restriction，非 squarefree 列由
Minkowski 汇总。三项分母指数 1、2、5/3 的和分别付 log、收敛、
收敛费用。没有把 moving row factors 放进任意列系数大筛。

## 3. 临界二矩、高度尾与零点 detector

AFE 两侧长度约为 (M R_w)^(1/2)(1+H)^(d_F/2)。
Mellin 分离后的导子虚幂、dual root number 都是每个 fixed Mellin
频率下的模一 row factor；固定 finite types 与 S-supported
primitive coefficient 的几何和先分开。因此 sieve 第三项准确为

\[
 (M(MR_w)^{1/2})^{2/3}=M R_w^{1/3},
\]

不是丢失一个 M 的式子。统一临界二矩为
M+(M R_w)^(1/2)+M R_w^(1/3)，全高度上可逐点取 H'=1+|t|。

辅助 M_X 仅是计数用 classical mollifier。没有重设原 M_r、槽、
profiles、physical amplitudes 或 normalizer。Gamma detector 在实际
ρ 上移至 Re z=1/2−β∈[−1/2,0)，只跨过 z=0，而其 residue 因
L_orig(ρ)=0 消失；未跨负整数 Gamma poles。

critical integral 保留全实轴，H=1 的尾也用任意高度临界二矩支付。
rowwise γ 的 sup 用 Sobolev，partial maxima 用 fixed binary intervals；
logarithmic derivatives 只改变先于行求和固定的系数。
这些与 density 源 (12) 的完整五项费用一致。

选择 Y 的高度幂 d_F/(6−4a)，Type I 与 Y-plain 的额外幂均为

\[
 p(a)-1=\frac{d_F(1-a)}{3-2a}.
\]

其他 Y-cross 的高度幂不更大。原域 d_F=2，
p(7/8)=6/5；没有把正高度费用当作 U 的负指数节省。
应用到原 bins 时 H=3I T_1，仍须按原顺序先固定 a 范围与 ε，
再选小 τ。密度本身不免费给每行 reciprocal bound。

## 4. 连续 powerful 层和实际安全指数

密度源 (14) 的三项上界为
max{x,(1+x)/4,(1+5x)/6}，分界 x=1/7 正确。
最终层要取 actual cardinality 与“powerful 数目＋detector”之 min。

在 1/2<a≤5/6，x≤1/5 先以 cardinality 付款；
x≥1/5 时 h=x/2、y=(1+3x)/(12(7/6−a))，
h≤y≤2x 的 bilinear rectangle 端点保证完整连续范围。
五项最大值及计回 w 后的 affine 上界给

\[
 G(a)=\frac{8(1-a)}{7-6a}.
\]

7/8 的高、中、小分段需要把小段按 x=1/15 再切开，
以区分 h=0 的 cardinality 与 h=x−1/15 的 optimized 分支。
四段实际 h、y、Type I、X-first/cross、Y-plain 的所有 dominance
均是整区间仿射不等式，而非有限 x 样本。所得 7/13、
5/8−7/13=9/104 与最大 2y=56/13 正确。

固定该参数后对 a 的单调/斜率上界给 G_safe。
其 cap 1 是合法 cardinality，不能把该安全延伸说成全部高 a 最优 LP。
在 5/6 的拼接处可采用不同安全 upper；这不会影响全域支配。
473 正确区别已证 G_safe 与条件的文献最优高段 g。

## 5. 最终 envelope 严格支配 raw

回核 450 的 actual

\[
 R_{*,\kappa}
 =1-\delta+\frac{(5/6-\delta)\delta P}
 {2[(5/6-\delta)D+\delta P]},
\]

它已结合同一 inverse/plain witness 与原 slots/amplification，
不能拿最初 raw R 来代替。κ 的原分析前件仍保留；
本次代数比较不使 κ_* 变成合法 actual plain 输入。

在 c∈[1/3,50/111]、x∈[0,1/2]，
2D−3P=2x(2+c−3cx)≥0，D,P>0、5/6−δ≥1/12。
单调代入 P/D≤2/3 得 r_0=(15−16δ)/(15−6δ)。

重新相减后，低段差的分子 δ(25−24δ)>0；
安全高段差的分子 225−380δ+168δ² 在 [2/3,3/4]
递减，最小为 69/2>0。因此实际两段 raw 在整个
δ∈(1/50,3/4] 上都严格大于 r_0≥R_*。

条件的文献高段差式也正确：其正分母可写成
(15−6δ)(6δ−3δ²−2)，18δ²−24δ+5 在该段最大值
−23/8。这里的条件比较未把未付 family extension 作为已证输入。

δ=1/50 只作代数闭延拓。floor 无 actual zero witness，
不可由这些差式升级。a_*≈0.694291677 是 moving row bin，
不是全族 β_*；7/8 raw 的改善也不作用于唯一等号角落。

## 6. 高行 strict certificate 与实际反馈

完整实读双 Bernstein 来源。代换 δ=l+(r−l)u、y=v/2
使次数至多 (2,3)，其 power-to-Bernstein 公式及 12 个系数正确。
指定 Cubic 实嵌入的有理 interval Horner 下端均严格大于
表中整数/1000，而这些下界都大于 1/25。
非负、和为一的 Bernstein 基因此给全矩形 F>1/25。

30/43≤δ≤3/4 与 a≥73/86 等价，J≤5/2 且 J>0，
故 E_*<−1/125。随后使用真正 κ_act=2β_*−1 的
451 derivative feedback，得到 −1/125−24Δ/25；
ζ=Δ/32 的延伸费用给 −1/125−359Δ/400。
这限于原 450/451 [R]、全部物理前件和参数顺序；
没有在 κ_* 处偷用尚未成立的无零假设。

## 7. 检查器独立执行与 metadata 范围

已在 Python -B 中 import 新检查器并只调用 finite()，
不运行 build/main、不写 JSON、不执行旧脚本的 main、不改旧输出。
返回 count=81，全部 assertions 通过。

其中连续认证实际包括：

- low-σ 的 two-variable bilinear 四角证书；
- 7/8 四个 affine whole-interval 分支及三项 sieve domination；
- 三个完整 rational raw-minus-final 恒等式与全区间符号；
- 冻结 Cubic 模块 hash 核验、指定实嵌入和 12 个双 Bernstein 下界。

检查器确实形成 symbolic expressions 后核等、在区间端点核 affine
符号；不是只打印硬编码的 7/13 或把网格 PASS 当连续证明。
Cubic 模块 import 有重定向输出，无文件写入。

build() 的 source/review pairs 核查 source hash 出现在独审正文；
各文件自身 canonical hash、Markdown source-table hash、相对链接
也逐一计算。预定 JSON 自链接的存在检查延后交给 main 写/读，
避免首生成时自输出尚未存在的循环。--check 以完整计算结果对比 JSON。
本次 JSON 尚待父代理在全部 review 落盘后生成，因此没有预称
完整 build()/--check 已通过。

有限证书不认证 sextic sieve、primitive AFE、Gamma detector 无限
分析、原 [R] 全包、RH、实际比例或新无零边界。
它也没有证明 density 与同一 prime slots 的新联合 amplification，
或者 472/474 正高度标量四次均值的有效 upper。

限定 PASS 的实际结论是：473 忠实汇总相对明确底层输入的原全行 raw
密度，以及不改善现有最终包络的全域连续比较。剩余算术接口仍为 [O]。
