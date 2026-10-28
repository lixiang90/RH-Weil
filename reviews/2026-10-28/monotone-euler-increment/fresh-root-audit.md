# Euler修改准入：独立逆核与消费范围

2026-10-28；`/root/euler_scope_fresh` 当前独占审稿。已恢复README/STATE、check→show、Goal、耗尽C049、D20261028U及宏观前沿，核实际工作树。本稿不改STATE、合同、单cadence或Git，不发新数学合同，不作外部文献新颖性声明。根原稿增加正Borel测度版说明及正primitive全repeats子类后，已重新全文核对并绑定下列最新版本。

**限定PASS。** 有限有理(s)分类、任意正Euler-log增量分类及正primitive增量的无FE子类，均有正确的旧依赖短链。未发现RH前件、有限阶偷设、实零点漏项或符号反转。支持root按旧机制应用0保存，不准C050/587；两类不能合成一般正Π唯一性，核心瓶颈和Goal完成门均未改变。

## 1. 有限F：测度差、实零点与横坐标

先固定一个约分的非零F∈R(s)，F(σ)→1迫分子/分母同次数且首项比1。零点a、极点b的重数给

 k(u)=Σ_b n_b e^(bu)−Σ_a m_a e^(au)， −F′/F(s)=∫e^(−su)k(u)du。

正负号正确；k(0)=0支付k/u在0附近有界，有限指数和支付充分右半面的总变差。Euler-log微分后是在同一右半面比较uΠ_F、uΠ_ζ和k(u)du。选更右的固定实权使这些signed测度有限，沿整条竖线的Fourier唯一性给其相等；再在(0,∞)除以u，得到root所写的Π_F−Π_ζ=(k/u)du。不仅是形式逆Laplace，也没有隐藏δ0，因为测度域排0。

Π_ζ=Σ_(p,j≥1)j^(−1)δ_(jlogp)纯原子。Π_F≥0迫它的Lebesgue连续部分k/u≥0几乎处处；k连续给全部u>0的k≥0。这一步不能推广成“任意两个正测度的差正”，root已显式限制。

旧405§4中h>0、h∈S_exp与M_h(s)=ξ(s)/2，使全部实s的Mellin积分收敛且严格正，故ξ在实轴无零。ξF entire只排F实极点，**不排F实零点**。若正k的有限收敛横坐标c处F有m阶零点，−F′/F的留数是−m，实右侧趋−∞，确与正Laplace变换非负矛盾；若F非零，则该变换在c全纯，冲突旧Landau边界性质。若横坐标为−∞，其变换整个、同时等于有理函数−F′/F，故为多项式；实右端趋0使其恒0。于是k=0、F常数并归一为1，未借用FE或非实ξ零点位置。

有限F的原先“minimal s(s−1)”短语已在admission末段冻结纠正。ξF entire允许F(0)=0或F(1)=0；严格保原Λ双pole的子类另加F(0)F(1)≠0。保pole位置/阶数又不自动保原残数数值，root当前未声称后者。

## 2. 任意正Δ：真实边界的局部log与全域反射

这里只假Δ≥0于(0,∞)、一个右半面中LΔ有限，E=ξexp(LΔ)的真实germ延成entire并满足E(s)=E(1−s)。F=E/ξ是亚纯函数，因旧ξ实轴正性而在每个实点附近全纯。这个事实仍不先排F实零点。

Root最新版本已显式支付**任意正Borel测度版**Landau步骤：假LΔ延过有限实横坐标c，在b>c取半径>b−c的Taylor圆盘，再取b−c<h<半径。各阶导数先由稍小实权支付，正矩/Tonelli使Taylor和等于∫e^(−(b−h)u)dΔ<∞，与b−h<c矛盾。旧261-B原述为函数密度，283-C证明内为同一机制，063§2 KR已经是正测度形式；这一核查没有偷加绝对连续性或有限阶。

在Re s>c上，meromorphic恒等定理把F=exp(LΔ)从原germ推到整个半面。故实σ>c有F(σ)≥1。F在c附近全纯有限，连续性给F(c)≥1；选取与实右侧值一致的解析logF便延过c，正是上述不可能情形。局部log是在真实边界排零之后才使用，没有循环假设全实轴F>0。

于是c=−∞；每个紧集均能由更左实权支付积分和导数，LΔ为entire，F=exp(LΔ)全域成立。此后才在实0、1消费FE得到F(0)=F(1)，并以实指数函数的单射性得

 ∫_(0,∞)(1−e^(−u))dΔ=0。

被积权严格正，故Δ=0。没有finite/rational/阶数/离散支撑假设。若允许0原子则会有常数gauge，当前(0,∞)域明确排除。无FE的Δ=cδ_a负对照正确：ξexp(c e^(−as))整个且Euler-log正，却不反射；它不自动是正primitive全repeats。

## 3. 正primitive增量子类不需要FE

按本对象域P≥0于(0,∞)，且Δ=Σ_(j≥1)j^(−1)(T_j)_*P；给定右半面可积性保证相关紧区间质量有限。若P非零，(0,∞)的可数紧区间覆盖给某[a,b]、0<a≤b<∞的P([a,b])>0。

对σ≤0，Tonelli给

 LΔ(σ)≥P([a,b])Σ_(j≥1)e^(|σ|ja)/j=∞。

σ=0是调和级数，σ<0更强。已知某右侧收敛，所以横坐标确为有限且≥0，直接冲突上一节只用entire与实ξ无零的边界论证；无须等到FE。u=0不能作为primitive的隐藏例外：若把它纳入全repeats，非零0原子本身即使在右半面也产生发散质量，违反原可积前件。此结论仅是附加全repeats假设的严格子类，不反过来将任意正Π叫作正primitive。

## 4. 双源去重、两类不拼接及实际净值

对实际D_N逐项取v=u−logm，积分成为h_rs(log(dm))，有限product cutoff的μ*log=Λ给全部proper powers的原权logp。第一变量线性的伴随满足overline{h_sr(a)}=h_rs(−a)，故Hermitian化后恰是原±prime腿，进入完整型的方向为减项。与同日prime-candidate§1–2确属同规则；finite N的du/Dlog上界没有产生cofinal统一界。550§2–5的raw II₂ O(1)与normalized完整Q接近仅属于其指定samephysical方窗源族，root没有套给任意smooth r,s。

有限F分类的假设允许一般正Π_F，但其结论只针对F(s)有理；任意Δ分类取消有理/有限限制，却增加了**Π_F−Π_ζ≥0**。两者并集不是“全部Π_F≥0且同Γ/entire/FE”。删除/重排ζ原有Euler原子后仍保总Π正、一般signed增量、只在极限有身份的正D′层和joint signed修复都仍有未覆盖范围。578的Γ0模型不能移称经典Γ反例；当前也没有补成578所缺的一般经典Γ模型。

这里支付的是Euler log坐标的指数加权测度与亚纯germ，没有新的physical源→principal/Green/mixedRR映射，没有原全du/zero-extension Dlog的成长费用或完整Weil净号。全Γ/contact、全部pp和双pole仍是原目标责任。Whole4/5仅负惯性UPPER；实际primitive/mixed、危险core/coupling/Ξ门保持open。两个“局部已闭”结果不能组合为Goal完成。

## 5. 分类与下一动作

两份有限F咨询在预算措辞上曾有初步分歧；old-admission§5已撤回自动辅助数学预算，新的任意Δ首检§5仍建议可准一次。那是投入建议，非数学矛盾或已经启动的合同。Root选择更短的405＋旧正Laplace机制＋FE链，按工作流“旧推论0”保存是合理的：新消费范围有用，但没有新独立算术signed输入或实际ζ核心净比较。Top层Cesàro候选没有进入本次root消费，不应由本审稿升级为已证新数学轮。

下一文档仅冻结一次三query primary定位和一个实际locator的准入标准，未列未知paper章节或执行结果。对reviews/goals作逐字搜索，三条完整查询串均只出现在该新文档；本审查未执行web、下载、数值或后台proof，不把将来定位写成已经研究。无合格locator即停止本批，不能延长来源队列或宣称全类不存在。该门的作用是寻找当前两条短链之外的signed替换实物；它本身不是RH等价接口获准。

## 6. 版本绑定

以下均为规范LF SHA-256；这里只绑定所读版本，不由hash认证数学。

| 原件 | raw bytes | LF SHA-256 |
|---|---:|---|
| monotone-euler-increment/root-old-consequences.md | 6659 | 227a20f5226458e2744932e93658054ee5209e5c0c57a9cb8ca7da9062d82161 |
| monotone-euler-increment/next-signed-replacement-source-location.md | 1663 | 54bcb34029785bd3bb118553eb3de1d7248811e898cfd514a008d7ab0be6d5ed |
| monotone-euler-increment/first-gate.md | 7965 | 6cd3276dbf4b2eba1f6473d700ada338c066688b662c89058c0a3319f67d7f12 |
| rational-euler-surgery/admission.md | 2879 | eb58f7a96f0ca83cc44e097a37cc072d93f106b1bc5f14b5c6fa360e52432263 |
| rational-euler-surgery/first-gate.md | 6829 | 331acfea97b2fe8068f7572b7196b745cc00465c45760df47ec1dc3e839db7cc |
| rational-euler-surgery/old-admission.md | 11195 | 43fb59b81b3a0e3d74b90d5c913b21fe2b0ff868104c33ea30f482fcf4eb84dc |
| new-mixed-input/actual-coupled-candidate.md | 3532 | 878dc312bed286b1676630ae199d080b10e16cac7a79d6a7c6312d7001473b12 |
| new-mixed-input/old-net-and-admission-boundary.md | 4785 | 33489cac68d3cf4224ffa76141ac407cde02c6ddd38378e1c7cc90eaba077d55 |
| arithmetic-input-construction/prime-candidate.md | 7946 | 6f2384fae7a5bc266c0bd39a8f0d28c89e2ebfc89addfc9359a09e751c711c2a |

核心旧依赖的LF版本：405 `fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d`；561 `2494d9b2305979836670d32f3a7558f058e57be361c27edb948ec2ed037571e7`；261 `7d4b530804839120a39651ea539d68dbfa152b3a63141e9b389e9a85c95d262f`；283 `00c96923a98f1052157c5e1f5e93d1678a1147af5293a0e8c615b4b2a4189f0a`；063 `c38ce029f6fa4a26f177e452f13ae324d5fc2045df86c0883aa5dcc75fb0fb1a`；550 `9c7615fc8c923b77b3f6d5cb3a121f738c32897bf4e2651d3843152345bb6aa6`。阅读范围是本稿明确列出的段落；不冒称重审其全部历史证明。
