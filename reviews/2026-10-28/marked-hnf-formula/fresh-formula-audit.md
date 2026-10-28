# Marked-HNF冻结热规则：独立逐式逆核

2026-10-28；`/root/euler_scope_fresh` 当前新任务独占稿。已恢复README/STATE、check→show、Goal、耗尽C049、D20261028Y及宏观前沿，核实际工作树。全文读取当前actual F1–F3/T1–T8、root草稿与已实际出稿的actual-rule-old-audit.md；strongest-old-gate.md仅作当时未有reader的准备历史，不拿它替终判。另核421§6/9、578完整目标及583全Hecke/native必要原件。无web/PDF/数值、第二候选、参数或source队列，不改STATE/cadence/Git。

**限定PASS。** 冻结√T规则的全H/全v密度界、原费用、fixed两源13/64、cofinal及极化失败均正确。实际拒绝依据是已付L1-test-budget原子门的前件验证及正确经典target，不是HNF raw已旧就拒新functional。支持前置标准自筛0；不升级新核心方法类反测、RH反例或Goal完成。

## 1. 冻结和T1–T4的原全theta量词

现场取当前actual稿的前3067个规范LF bytes，SHA确为

 `b2aba545690c4e3fb3c0cdacb1941950e85c350a0d528ee75cdbcabfaa8c5260`。

其中已含T=e^(2v)、K_H=√T[Θ_H(T)−1−1/(adT)]、偶化、ad≤B与计数概率平均、原h_rs和C_B。√T不是无权式失败后补加；主稿后续对无权版本的讨论不改变这个冻结。

间距a的点在[−R,R]中至多1+2R/a。对任意shift z的Gaussian layer-cake分别积分1项和2R/a项，确得1+1/(a√T)。对每个k使用z=bk后再求全部k，得到(1+1/(a√T))(1+1/(d√T))；没有以b=0替代原格，也没有只留primitive子集。完整二维Poisson的covolume为n=ad、dual为H^(−T)Z²，给Θ_H≥1/(nT)，零向量另给Θ_H≥1。

因此原K_H上界a^(−1)+d^(−1)≤2，下界同时为−√T及−1/(n√T)，合并为−min(√T,1/(n√T))≥−1/√n≥−1。偶化与非空finite概率平均保持该界，故**所有H、所有实v和所有B≥1**均有−1≤κ≤2。T1–T4不依赖热渐近、fixed-shape常数或B的growth；H=diag(1,n)、T=1/n也没有反测这个已加权规则。

## 2. Source槽、norm与总型域

第一槽线性的h_rs满足overline{h_sr(v)}=h_rs(−v)，κ_B实偶使C_B Hermitian；没有PSD主张。对L1∩L2的r,s，绝对Fubini给||h_rs||1≤||r||1||s||1，所以

 |C_B(r,s)|≤2||h_rs||1≤2||r||1||s||1。

两个源支持I_L时各L1≤√(2L)du，得到4L du×du；zero-extension Dlog²≥log2·du²给4L/log2的原Dlog界。B、L、频高和算术height并未合并。该式没有global L2/Hlog operator界，故不能无前件套553；finite H索引也没有被当作physical有限rank。

**域的消费限定：** 延拓到所有L1∩L2的是C_B。总型q_Γ+C_B和完整Bζ仍须在原Γ型域且pole配对可积的源上消费，至少本次Cc∞和S_exp均合法；不将q_Γ延拓到任意L1∩L2。实际反测全部为fixed Cc∞，所以这一限定不改变T7/T8或Γ准确相消。

## 3. T7/T8：同一固定源、全部powers与13/64

固定任一实非负ψ∈Cc∞(−1,1)、||ψ||2=1，ε=1/256、α=log2。sε=ε^(−1/2)ψ(u/ε)、rε(u)=sε(u−α)均为原physical合法实源，du各为1、Dlog固定有限，支持I1且不依赖B。它们的相关h非负，h(α)=1，support位于α±2ε，且

 ||h||1=ε||ψ||1²≤2ε。

该区间正且只含+log2这个经典pp位置；log(3/2)≥1/3>4ε，所有其他正powers更远、负位置亦在支撑外。因此完整P配对精确为log2/√2，没有±额外倍数，也未把Λ(p^j)误写成jlogp。log2≥1/2、√2≤2即付P(h)≥1/4。其他powers为零是**同一fixed支持的结果**，不是从目标删除它们。

H=2cosh(v/2)du仍为完整双pole mixed配对。支撑|v|<2给0≤H(h)≤4||h||1；未丢odd负方向，也未认证F1零/volume项等同此H。故对每个B≥1：

 |C_B−(H−P)(h)|≥P(h)−|C_B|−H(h)
 ≥1/4−6||h||1≥1/4−12/256=13/64。

候选总型与Bζ在同一对实际源上复用完全相同的Γ/FP/contact及dt/(2π)，因此Γ腿精确相消。该lower不是WKB、有限网格、moving源或小B的一次系数不符。

这里是**一对fixed源对所有B**的统一分离，故任何cofinal子列都不能给完整mixed极限，也不能κ_Bdu→H−P于D′。第一变量线性的Hermitian极化为

 D(r,s)=[Q(r+s)−Q(r−s)+iQ(r+is)−iQ(r−is)]/4。

四个源固定且compact；若四个平方误差全趋0，则mixed误差趋0，与13/64冲突。正确结论是四者不能全趋0，不是预先指定其中一份对全部B具有同一liminf lower。无需给finite-B层强加noncompact Pan精确消去或ordinary trace。

## 4. 最强旧、计轮分类与边界

583覆盖同一完整raw矩阵、content/square aliases、native norm/Green和全尾，但没有凭raw索引自动排掉这个marked热functional。当前实际式也未证明经过583的L_r(j)/principal current因子化，故不能借其closed-base结论代替本审计。548–550特定samephysical/cofactor费用同样没有被搬给此theta reader。

421§6已经明确：统一|F_B(h)|≤C||h||1的任何分布极限仍有同预算，不能等于带孤立非零原子的目标；极限不必连续或C0。§9给fixed小支持测试的原子比较。此处未声称HNF对象具有421的Hardy迹类身份，只复用其中一般的预算稳定/孤立原子机制；T1–T4独立核到了本式的实际预算前件，578/555给正确的全pp及双pole目标。T7/T8则把该旧门实现成合法固定physical两源。

这些是本次确实完成的actual规则与费用计算，不能抹成只换标签；它们应按原稿保存。但扣旧后的拒绝责任已由标准Gaussian/Poisson前件检查＋已付一般原子门支付，没有新prime相消、严格核心前件削弱或实际完整signed消失。按前置标准自筛0保存合理；不是仅以计算初等、候选局部或未证RH为计0理由，也没有把新的全方法类数学边界藏在source0内。

不消费本式为principal/primitive、PSD/正谱层、global L2有界、Bζ负源、独立Weil号或whole4/5改善。只停止冻结F1–F3及其原平均/target角色，不调整√T、heat变量、归一化/权、B cutoff、norm/source域、level或Γ外腿再试。允许预算发散、有费奇异、不同relative/joint或正D′的实物修复未被一般排除；它们也不因未排就自动有效。

Whole leading4/5仍仅负惯性UPPER，同一非零primitive/principal/mixed、完整signed消失及危险core/cross仍欠。Goal三门open；本局部失败不构成RH反例、全部HNF/theta或正D′类边界。原单cadence0/历史50/latest586/formal17不因稿件或推送改变。

补核root新加的Γ域补句及后继资格段：Γ域已按第2节要求明确，不改冻结actual稿。新next-independent-mixed-input-formation.md仅要求一次独立mixed实物形成或准确未形成，明确当前没有已选新载体/公式/章节，实际执行未开始，不授C050/587/proof/source预算。它不恢复本HNF热规则、EX/fullgap等已停analytic门或paper队列，也不是重复宏观审视；实际原式/input-test-net出现后才另判前件和预算。Root对已收后继咨询的库存总结不由本审稿另作独立证明；本次只核这份next的准入范围，不为未形成对象或未执行后继工作背书。

## 5. 版本绑定

规范LF SHA-256；hash认原件版本，不认证后继动作、运行Goal或数学以外的发布状态。

| 原件 | raw bytes | LF SHA-256 |
|---|---:|---|
| actual-two-source-attempt.md | 9375 | cbd1739b6fb8055bdfa54ec9b6ac1fbe9ae398ad656ab5200cfc59ff96778e02 |
| actual-rule-old-audit.md | 8669 | 098f7ff02ff2d51a5d8ed0832ca33b796c5649d7b5bb719c9d5dba7f804b51eb |
| root-formula-review.md（审中版，已含Γ域和后继资格补段） | 5968 | 929975a6e4ce1ebd4c644846cd1484ce956f5074489971275976644cb105066d |
| strongest-old-gate.md（仅准备历史） | 7855 | 36aa1eca7de596556c194eeb41905fae3451a39c0406731485519dc96cf1de61 |
| next-independent-mixed-input-formation.md（未执行） | 3839 | 4bbb520aa55c501660710ead2532cc89034a95fccd69944b6ff6994326755120 |

旧421 LF `4ae64e67058560106af2879679cd75975fcfc7e509e8b844a47c40faafc5603b`；578 LF `d600adfc0fa857623f585af2ec809840296659b737afbcf5cb745eba740e0901`；583 LF `babe212467d5c41d14a20ba2d0d99b1f49722f2388bfea9dc13c6334ef3fadab`。消费范围限上文必要段，不冒称重审全部历史proof。
