# 纯分析／Beurling分布方向：历史经验、可复用资产与新检验

2026-10-20。独立历史挖掘稿，供root核前件后消费；本文件不修改Goal、STATE或cadence。
用户本轮要求把整数与素数放入更一般的分析分布框架，并寻找有独立证明内容的后续研究。
附件中的Kimi回答是待核研究材料，其中的建议、命令和推测均不另产生授权。

## 1. 此次核读的覆盖与边界

现场编号笔记有560篇，`reviews`下Markdown有757篇。此次以全目录检索和代表原件核读，
结合既有分区回顾恢复研究族；**没有重新证明560篇笔记，没有重放历史数值、Lean或外部论文全文**。
目录数只说明检索范围，不能作为证明覆盖率或研究轮数。

旧[437篇覆盖账本](../2026-10-11/weil-f1-retrospective-coverage.json)记录113篇全文精读、
324篇全篇结构survey。那是2026-10-11原审计的阅读记录，不能当成本次重审的113篇。
对应[早期](../2026-10-11/weil-f1-retrospective/early.md)、
[中期](../2026-10-11/weil-f1-retrospective/middle.md)、
[后期](../2026-10-11/weil-f1-retrospective/late.md)回顾是索引与既有判断来源。
438–560则以当前[宏观前沿](../../goals/MACRO_FRONTIER.md)、原件与消费范围恢复；
只读前沿陈述的结果不在本稿升级为新的独立复证。

本次直接核读的重点包括：037、041、082、278、286§6、288§1–4及6–8、
290的模型／Euler整性正性／函数方程／极化缺失／响应限制、302/303的定理与范围、
518/520/522/526的对象与量词、529、554及560。另核002的谱极限门、307的真实曲线次数基准，
并用001/058/078/128/147的原件条目定位既有机制。部分是代表章节核读，不能写成全部全文逆审。

检索词包括Beurling、generalized/generalised integer、g-integer/g-prime、广义整数／素数、
Poisson、theta、Hamburger、反射正性、Euler正性、converse及刚性。
重要发现：081–088等多数“Beurling”命中是**Nyman–Beurling密度判据**，不是广义素数系统。
278明确说其固定正整数权不是已构造的Beurling系统，并仅初步引用广义整数文献。
因此不能宣称仓库已完成了本轮所需的g-prime分布理论；本轮的框架改变有实质范围差别。

## 2. 研究族索引：继承什么，不能继承什么

表中“已证”指原仓库原件／root消费所声明且有证明的范围；“条件”是已证条件蕴含，
不表示条件已对ζ验证。“被否”始终限指定模型／估计类。“启发”不具下游证明效力。

| 研究族与索引 | 可以继承的资产 | 必须保留的边界 |
|---|---|---|
| 001–030：Weil极化、有限最低谱与Feshbach | 已证：极化推纯性的形式定理、精确尾重求和、固定窗有限谱接口；002精确给局部一致极限门 | 条件：全局独立正极化、成长最低谱支与指数加权逼近；有限矩阵实谱不识别Ξ |
| 031–078：边界current、Green、filtered primitive、Ihara | 已证：037的正trace-class Green及规范current；058分开可见性与dual稳定；078的真实有限图模型 | 条件：critical membership／tightness。一个自伴Green算子已经存在，并不使实际源有有限能量 |
| 079–130：Euler determinant、Nyman–Beurling、incidence与completion | 已证：正Hilbert载体、精确Schur距离、定向Feshbach、尾迁移；被否：082的uniform全Gram gap及128的无代价acyclic纯化 | 目标对齐及实际period大小仍欠；增加正块不能免费保持同一zeta的determinant |
| 131–162：Pick／passivity、容量迹、Vaughan通道 | 已证：capped正测度锥、单边负指标接口、若干localization；被否：147指定full quadratic能量及162泛Gram core放大捷径 | 条件：actual负迹统一预算。不能惩罚RH允许的正临界尖峰，也不能由tail小推出core小 |
| 163–202：growth、threshold、word、非构造补全 | 已证：局部complex、Haar Gram、实际系数恒等式、word检测完备化及条件compactness | finite PSD与全部finite约束一致付费不同；full word检测不等于负迹改善；bare存在仍可能RH等价 |
| 203–278：Brownian两通道、共同乘子、Abel记录 | 已证：某些实际通道符号、有限增益、响应公式与278固定全局正源障碍 | Γ加入会改变同一响应乘子；相对gain不付绝对账本。278不是g-prime或ζ反例 |
| 279–307：响应非识别、Euler变形、可见性、真几何校准 | 已证：286的指定模型、288有限Euler正性限制、290正闭点＋FE离线模型、302/303硬商可见性边界、307真曲线次数正性 | 多个弱公理和全部相对偶矩仍不强迫中心线。303无Euler；290有Euler却不是经典Γ；不同反例不能静默合并假设 |
| 308–362：正则化、mixed Gram、物理determinant与有限控制 | 已证：若干同域正则化与共同误差接口；可继承的是全mixed／同一physical对象的核算纪律 | 涉比例／零区优化的路线保持暂停；列逐个小不等于全Gram小，有限控制不自动给全连续域 |
| 363–406：F₁、period ring、Cartier、adele源与主关系 | 已证：一批实际局部Cartier与405/406的源、单位、局部determinant资产 | relation／radical／principal／物理商不能混用；非退化global primitive、RR／有效性与完整Weil比较未付 |
| 407–437：局部边界、relative complex与trace读出 | 已证：一些真实边界核、完整有理trace carrier及局部比较 | 合法读出并不唯一确定真实time分布；finite-part线性／循环性／源传递须逐域支付 |
| 438–517：精细算术／比例及进一步F₁源接口 | 已有形式证书和实际算术条件链的分账经验；后期进展须看各原消费范围 | 暂停优化；不能把formal条件链的PASS称无条件完整算术定理，也不能把非紧或辅助corner失败扩大到所有几何 |
| 518–526：完整源商与增长／Hilbert完成 | 已证：实际Mellin除法、closed source image、完整Fréchet谱与Jordan；522识别增长条件的RH等价；526排指定等价Hilbert酉化 | 已有谱识别不同于正Hilbert谱约束。换完成可能灭掉对象；忠实完成又可能保留不可酉缺陷 |
| 527–538：完整Weil锥与Sonin，fixed窗正性 | 已证：529标准锥保正的精确方法边界；535 single-prime无费桥边界；537/538全complex fixed窗正性及simple-even/gap | 标准锥失败不证明Q负；single-prime不排joint／paid修复；fixed半窗17/16不能外推成长 |
| 539–560：成长费用、joint、Γ／pole与强旧比较 | 已证：555完整prime原norm约e^L；542+555已蕴含whole预算leading4/5；560每fixed finite-S全源mod-compact桥 | 危险core仍指数，K_L的sign/norm/growth、完整Ξ识别未付。557的4/5不能再当新增；560不交换fixed-S与cofinal量词 |

这个索引将全部编号区间纳入检索版图，但没有对每一区间的每一命题作新核证。
它的用途是从新问题回溯必要原件，避免重新把旧开放箭头当成新输入。

## 3. 与本轮最直接相关的六项资产

### 3.1 290给出必须保留的正Euler＋自对偶负基准

[290](../../notes/290-positive-euler-duality-model-and-mass-moment-nonidentification.md)固定q≥5，

\[
 Z(t)=\frac{1-qt+qt^2}{(1-t)(1-qt)},\qquad
 \alpha\beta=q,\quad1<\beta<\sqrt q<\alpha<q.
\]

原证明给全n正整数B_n和收敛Euler乘积

\[
 Z(t)=\prod_{n\ge1}(1-t^n)^{-B_n},\quad
 Z(1/(qt))=Z(t).
\]

同一模型还满足非退化Poincaré对偶、代数Hard Lefschetz及其自己的超迹／determinant公式；
所有cutoff、任意正概率频率测度的质量相对偶矩界和共同乘子Schur增益均真。
但Z(q^{-s})在Re s=log_qα及1−log_qα有两列离线零点。
缺失的是**与实际F相容的独立正极化**，不是再加一个任意正内积。

有一项对本轮有用的合法重读：取B_n个带标签的广义素数，数值范数都为q^n。
它们自由乘法生成的广义整数按重数计，Beurling Euler乘积恰为Z(q^{-s})。
数值相同的范数不能合并成“没有重数的集合”；形式自由生成元的不同分解是不同广义整数标签。
原290未把它登记为Beurling定理，本稿只说明这个直接解释，不宣称新外部结果。

它仍不是本轮最强负基准的全部：广义整数范数只在q^k上，区间(q^k,q^{k+1})有固定比例空隙，
故N(x)/x不可能趋于A>0。它不反驳“加上N(x)=Ax+o(x)后”的更小类。
完成化也是函数域周期型，不是Riemann的真实Γ因子。

### 3.2 288要求分别记账三种“正性”

[288](../../notes/288-finite-euler-deformation-positivity-obstruction.md)的定理范围是
Z=ζ^m乘有限个局部**多项式**P_p(p^{-s})，不是任意有理或无限Euler扰动。
若全部对数导数系数Λ_Z(n)≥0，则每个局部参数|α_{p,j}|≤1，不能新增Re s>0的零点。
额外weight-1 reciprocal的非平凡局部多项式也被排除。

该稿同时给普通Dirichlet系数全正、反射FE和中心线上乘子点态正的离线模型，
但其Λ_Z(4)<0，故不是非负prime分布的反例。
这三项不能混写：a_Z≥0、Λ_Z≥0、完整Weil型PSD分别是不同责任。
也不能从有限多项式无变形定理排除连续分布、无限Euler或joint修复。

### 3.3 278／286说明正源和良好计数信息仍会漏掉识别力

[278](../../notes/278-fixed-positive-integer-source-record-envelope-obstruction.md)给同一个固定全局
λ(n)∈[1/2,3/2]，保平方根级全局误差、历史guard和soft范数，仍产生真实中频峰。
它明确未付primepower支撑、Euler乘积或Beurling自由乘法结构。
[286§6](../../notes/286-attained-spectral-edge-and-response-nonidentification.md)另付单值亚纯、
整数零点重数和正Dirichlet系数，但仍不付完成FE或标准Euler。

可复用的是模型的“一次性全局源＋全尺度/指定共尾量词＋真正物理响应”组织方式；
不能将278的计数、286的亚纯和290的FE拼接为一个并不存在的共同反例。

### 3.4 037／041已经把“自伴机器存在”与“ζ源准入”分开

[037](../../notes/037-sturm-liouville-hodge-current.md)中L_σ及正trace-class Green算子无条件存在。
RH责任是实际discrepancy current在每个临界权的负Sobolev空间有有限能量，
不是弱方程可解或算子自伴。
[041](../../notes/041-euler-bessel-cancellation-no-go.md)进一步证明centered Euler remainder
不是完全单调函数，任意等差安全采样也不是Hausdorff完全单调序列；
逐项绝对值把Bessel J变成I并造成指数伪损失。

新g-prime分布可从这些一般Green／Laplace／Mellin接口借载体和估计方式，
但须重新证明目标current的growth、极点与全域准入。
“本构造不显式输入零点”只保证定义的一种独立性，不能使未知能量上界变为已知。

### 3.5 518–526说明先查商是否可见，再谈酉化

[518](../../notes/518-f1-quantitative-mellin-division-and-mobius-source.md)消全部零点jets，
[520](../../notes/520-f1-source-quotient-spectrum-and-centered-growth.md)在同一实际Fréchet商上
识别全部非平凡零点和完整Jordan重数；这些是已付的谱接口。
[522](../../notes/522-f1-optimal-centered-growth-and-rh-equivalence.md)证明指定次指数增长条件与RH等价，
并未证明条件成立。
[526](../../notes/526-f1-faithful-two-weight-hilbert-quotient-and-defect.md)的双权完成忠实保留原商，
但用已知中心线近频率对就能证明自然商群不uniform有界，任何等价Hilbert内积都不能使其酉。

因此新路线不能重复“先换一个正norm，自伴性自然成立”。可允许新的非等价norm或不同实现，
但需独立来源、原源连续嵌入、全重数和谱识别；这些是新前件，不受旧边界统一排除。

### 3.6 554／560给一般分布研究可直接比较的真joint对象

[554](../../notes/554-theta-joint-positive-jump-and-adaptive-domain-scope.md)的theta关系使
Q(gf)=正跳能量−μ项＋双pole成为完整恒等式；所需modified Poincaré不等式仍是whole正性责任。
源／窗口适应确能修复旧单g域失配，其原norm运输平方费可做到order e^L，
所以single-g巨费不能用于排除所有适应修复。

[560](../../notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md)则付了
每先fixed finite-S的真实正trace与原Weil型之间的自伴紧误差K；全primepower和actualΓ=2θ′均保留。
可借鉴的是完整inverse、两真实boundary与bulk先联合再取界，非把single-place trace相加。
未付的是cofinal S_L的K_L符号／norm／Γrelative费用与core。
任意一般分布版本还必须重新证明B、压缩逆及源域的合法性，不能由形式替换p→实变量继承。

## 4. 哪些循环最容易在“纯分析化”后重现

1. **把识别与约束混成一件事。** 从Mellin理想得到ζ谱已经付过；新增自对偶结构若只重现
   ρ↔1−ρ，就只付对称性。真正新增必须是一个对该谱有效的单边界／正性／耗散不等式。
2. **把Weil正性直接当公理。** 这可定义正确的一般类并证明一般定理，但对经典ζ的成员资格
   仍可能恰为RH。每次须注明哪一项对ζ无条件、哪一项是未付membership。
3. **把所有有限正性当成极限正性。** 固定cutoff的正Gram可以逃质量、灭目标或改变norm。
   002要求局部一致非零整函数极限，058要求定量dual分离，037要求统一能量；不能只用compactness名词。
4. **追错误的全空间gap。** 082已由相邻log节点碰撞排除uniform Gram gap。
   critical-line零点允许near-radical；目标应是实际源的定向Schur margin或负部，而非全部奇值远离0。
5. **忘记正临界谱可以很大。** 147的指定平方能量在RH真时也发散。
   “涨落小”若同时惩罚合法正谱，可能是一个比RH更强甚至已假的目标。
6. **静默删Γ／pole／proper powers。** 529的真实交叉核、554的正跳和560的紧差都依靠完整项。
   558还已拒绝丢正even pole的热包络；所谓纯分析模型不能靠删这些项变简单再移回ζ。
7. **把符号相似当对象相同。** Brownian四阶、矩阵trace四阶、prime正measure与谱正measure，
   以及乘法卷积和加法反射都是不同对象；没有公式和norm运输就不能互相付款。
8. **用弱旧子界报告新whole结果。** 当前最强whole旧后果是542+555→557的leading4/5，
   不是555打印的1，更不是543的2。新分布反模型也须与290的共同假设交集对照。

附件另有一个坐标误会须立即避免：物理加法变量x上的整数Dirac梳受Poisson对偶，
不等于log n在对数变量中是等距格点。log(n+1)−log n→0；log-prime支撑也不因整数来源而形成自对偶格。
由Gaussian theta反演得到的是带变量和权的明确Mellin关系，不能把它压缩成“log整数梳自对偶”。
分类“只有经典有限扰动或motivic系统”仍是附件推测，不是旧仓已证明的rigidity theorem。

## 5. 本轮连续反模型与最强旧结果的比较

root本轮提出待独立闭合的连续分布候选

\[
 Z_a(s)=\frac{(s-a)(s-(1-a))}{s(s-1)},\qquad0<a<\tfrac12.
\]

若新原件确实证明：primitive g-prime分布非负、乘法卷积指数给非负g-integer分布、
N(x)=1+a(1-a)(x−1−log x)、精确Z_a(s)=Z_a(1−s)，则它的净新范围应如此登记：

| 旧资产 | 已排除／已保留 | 不能覆盖新候选的原因 |
|---|---|---|
| 278 | 正固定整数源＋全局平方根信息不足以控制指定中频 | 未构造primitive g-prime／Euler／完成FE |
| 286 | 正整数对数导数源＋正Dirichlet系数＋亚纯模型可有离线零点 | 未付完成FE，也没有新候选的g-integer计数结论 |
| 288 | 普通系数正＋FE可离线；有限多项式扰动若再保Λ正则不能新增右半平面零点 | 新候选是连续分布，超出有限局部多项式类；不能用其Λ负例代替 |
| 290 | 正离散Beurling多重集＋FE＋对偶/HL/全部相对偶矩仍可离线 | q-lattice使N(x)/x无极限，不含Ax+O(log x)；未给nonlattice连续primitive密度 |

所以若成立，新候选不能被宣传为首次说明“自对偶＋Euler正性不蕴含RH”；290已给更丰富的旧负例。
它真正补上的检验交集是：**连续primitive正性、非lattice、极强N正则与精确FE同时仍不足**。
这能修正附件关于“计数光滑／nonlattice／完成化”的候选筛选，提供新的准入负基准。
它仍不触及具有Riemann真实Γ、真实高斯Poisson源和T log T完整谱的子类；
不能据此称已排除“纯分析方法”或消除实际ζ的成长core瓶颈。

本次对notes/reviews精确检索候选因子与计数式未找到同型原件；这只是本地去重，
不是文献新颖性证明。本节候选的最后数学状态以root的新原件与独立审查为准，
本历史稿不自行把收到的agent叙述升级为已消费定理。

## 6. 可消费短链与能改变选择的下一检验

**短链A：用负基准筛选一般分析公理。** 290原件的全n Euler正性／FE／失极化
→按重数的离散Beurling解释→排除“只靠Euler正＋自对偶”的候选；
若本轮连续候选闭合，再加“强N正则＋nonlattice仍不足”的交集。
这条链不使用未知ζ零点，不证明ζ负性，也不代经典Γ子类的分类。

**短链B：用真正基准校准独立正性的来源。**
[307](../../notes/307-odd-polarization-and-elliptic-degree-benchmark.md)的具体曲线次数正性
→同一对应代数上的FᵀHF=5H→正similitude→全扩域trace及zeta识别。
关键次序是先有独立有效次数，再得正Gram和谱界；把次序反过来便成反造。
其功能是验证新抽象公理有没有独立来源，不能把有限域几何输入称为数域已付。

**短链C：保留实际ζ的比较对象。** 405/518/519给原源和jets
→520给同一商完整谱
→560给每fixedL实际完整Q=正trace−compact＋signed双pole。
新g-prime理论若能产生对这个K_L的独立signed／Γrelative估计，才开始支付实际ζ的核心箭头。
只在广义类另造一台自伴算子，不会自动沿此链回到ζ。

建议按以下可判门选择后续，不再单纯增加等价描述：

| 检验 | 最小实际输入与判据 | 成功／失败怎样改策 |
|---|---|---|
| A：公理逐项负对照 | 对290及本轮连续候选逐项列primitive正性、N、FE、Γ、增长、pole、谱重数、Weil型；明确是哪条新公理排除它 | 若所有新增条件仍被负基准满足，立即拒其充分性；若仅“谱正”排除，仍须独立来源，不能开membership合同 |
| B：theta自对偶与正性的分离 | 固定物理变量及高斯核，写出Mellin双端缺陷、pole和增长的精确公式；先查是否只恢复FE，或得到超出FE的可计算非负分解 | 只恢复FE即止损；新非负分解须同时给原complex全源域与Γ／pole费用，再送560/554比较 |
| C：真正可识别的反射／HB核 | 先固定整函数组合、反射对合、除数与再生核；在307正模型和290负模型验符号；区分全核PSD与单点正 | 若正模型失败，修公理；若负模型被认证，修充分定理；若两者分开，下一门只能是经典ζ核的独立估计 |
| D：逼近与谱可见性 | 在选定positive closed model中先付局部一致的非零determinant极限及全重数；或给实际源的dual下框架 | 只在有限低谱吻合或只得L²，回002/058，不升级RH；真付后才讨论经典ζ适用范围 |
| E：actual joint费用 | 使用560真实K与原du、Dlog、actualΓ及全部pp；给一个可判signed系数／反例，或cofinal Γrelative新界 | fixed-S结果只改局部比较；若给全成长新费用，再扣strong-old4/5检查净值；不复活停止合同的旧预算 |

这里A是便宜筛选，B/C是当前纯分析纲领最值得保留的实质问题，E是返回实际ζ的消费口。
没有某一项独立新输入时，应停在明确章节的来源审查，不能连续把“未知正性”改名为新合同。

## 7. 本稿的瓶颈结论与交接

历史挖掘的主要价值是找到了足够强的旧负基准290、真正正性来源307、
和已付的实际源商／joint比较链518–520／560。
它也确认：纯分析化本身没有绕过正性、覆盖、growth和determinant识别四项责任。

本稿没有改变实际ζ的关键瓶颈。若本轮连续反模型经root闭合，改变的是一般分析公理的
**可行性筛选**，其精确新增交集见§5；不能称完成现有宏观Goal。
STATE旧唯一动作及其现场处理由root维护；本稿不预建合同、不计研究轮、不复活暂停的比例／零区路线。

交付后精确下一步：root核本轮连续候选的primitive反演正性、计数与FE原件及下节正测度刚性，
把它与290作为同一张公理负对照表消费；随后只选择对经典ζ有新独立正性运输证据的一项检验。
若没有这样的输入，保存停止条件，不把C1–C5／反射正性的名称当作证明进展。

## 8. 本轮新刚性原稿的独立审查：分析恢复整数确实可以付清

本节在历史稿主体完成后应root追加审查；被核原件为
[来源稿§5.1–5.2](beurling-primary-source-and-admission-audit.md)。
这不是从旧笔记摘要消费来的命题，本节给独立核算及与旧资产的对照。

### 8.1 对象、归一化与结论

取Fourier变换 \(\widehat f(\xi)=\int f(x)e^{-2\pi ix\xi}dx\)。
若μ是R上的正tempered Radon测度，

\[
 \widehat\mu=\mu,\qquad \mu|_{(-1,1)}=\delta_0,
\]

则μ必为 \(\sum_{n\in\mathbb Z}\delta_n\)。这里输入没有离散性、整数支撑、
乘法自由生成、Delone或算术系数。单位gap和中央原子质量固定Fourier尺度，不能删去规范。
正tempered测度对Schwartz函数的积分合法，μ({0})=1也由限制等式已付。

### 8.2 独立逐步核对

1. 可取实偶 \(h_j\in C_c^\infty(-1/2,1/2)\)，在L¹和L²中趋于单位区间指标。
   令 \(f_j=|\check h_j|^2\ge0\)，则f_j是Schwartz，
   \(\widehat f_j=h_j*\widetilde h_j\) 的紧支撑在(-1,1)，
   \(\widehat f_j(0)=\|h_j\|_2^2\)。对每个j都在合法测试域，未直接测试sinc²。
2. 自Fourier等式意味着 \(\langle\mu,f_j\rangle=\langle\mu,\widehat f_j\rangle\)。
   用tempered分布约定也可写 \(\langle\widehat\mu,f_j\rangle=\langle\mu,\widehat f_j\rangle\)；
   这里实偶f_j进一步消除任何F与F^{-1}的反射记号疑问。
   gap遂给 \(\int f_jd\mu=\|h_j\|_2^2\to1\)。
3. 原点贡献 \(f_j(0)\mu(\{0\})=|\int h_j|^2\to1\)，故
   \(\int_{x\ne0}f_jd\mu\to0\)，且每项非负。
   L¹收敛使 \(\check h_j\) 在全实轴一致趋于 \(\sin\pi x/(\pi x)\)。
   Fatou用于正测度，给
   \(\int_{x\ne0}|\sin\pi x/(\pi x)|^2d\mu=0\)。
   因极限函数在R\Z严格正，μ在R\Z无质量；正Radon性质再给supportμ⊂Z。
4. 支撑在Z后μ=Σc_nδ_n，c_n≥0且tempered给至多多项式增长。
   \(e^{2\pi ix}\mu=\mu\) 的Fourier变换说明 \(\widehat\mu\) 作为分布以1为周期。
   自Fourier使μ自己1周期，因而全部c_n=c_0=1。

没有发现符号、分布配对、极限或支撑论证的缺口。结论是**正测度的物理Fourier刚性**，
不是零点侧正谱测度的构造。

### 8.3 固定Gaussian反演的等价准入

若μ额外是偶测度，且对所有t>0满足

\[
 \Theta_\mu(t)=\langle\mu,e^{-\pi t x^2}\rangle
 =t^{-1/2}\Theta_\mu(1/t),
\]

令D=μ−Fμ。Gaussian Fourier公式给D杀掉所有Gaussian；D是偶tempered分布。
Gaussian族在t>0是Schwartz拓扑的C∞映射，所以逐t微分合法，D杀掉
\(x^{2k}e^{-\pi t x^2}\)。在t=1/(2π)，这些函数张成所有偶Hermite函数的有限线性组合；
Hermite展开在Schwartz拓扑稠密，故D=0。再用8.2得到comb。
这一步不是仅用同一Gaussian在单点t的一项积分；需要**所有t>0**，量词不可弱化。

对正g-integer测度dN支撑[1,∞)，
\(\mu=\delta_0+\iota_*dN+(-\iota)_*dN\)自动满足中央gap；N(x)=O(x^A)给tempered。
于是固定Gaussian精确反演可恢复 \(dN=\sum_{n\ge1}\delta_n\)。
这里物理变量为广义整数的范数x，绝非log n格点。消去这一坐标误会后，用户所问
“由一般分析对象恢复整数特殊性”在这个强而明确的条件类中已有完整可审证明。

### 8.4 最强旧对照与剩余责任

本次旧notes的self-Fourier／自对偶／Poisson／刚性检索未找到同型“正tempered测度＋单位gap”分类。
012已有self-Fourier型prolate，405有实际Poisson源，554有theta正跳；它们并未陈述以上全正测度分类。
因此本地范围可登记为新识别命题；没有据此作外部文献优先权声明。

它比“裸FE与计数正则”更强，确实排除本轮连续密度反例；也不由290的周期FE自动得到。
但对经典整数comb，固定Gaussian反演本来已由Poisson给定；再分类为整数并没有替ζ产生
新的Weil正性、负部预算、成长K_L控制或Ξ的自伴determinant极限。
原仓最小未付箭头仍是 **integer-side正性如何向同对象完整Weil/spectral正性运输**。
下一研究门应使用原稿§6所要求的显式remainder/coupling核，并与405／554／560比较；
只再次导出同一FE／principal关系或未知核≥0，仍按来源止损。
