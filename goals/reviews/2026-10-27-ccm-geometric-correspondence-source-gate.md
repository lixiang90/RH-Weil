# CCM §6 来源门：有向复合、低次数项与 principal 下降

2026-10-27；G20261027／原0c4f基线。执行STATE保存的唯一来源门：既库CCM math/0512138v2的§6.1–6.3／PDF44–47，止于§7。原C046预算已耗尽，583为输入，不建C047／584。本文是root对两原稿与原页的消费记录；fresh结论／最终阶段见同目录审查与STATE。

结论是**来源0停止**。该章能帮助组织已有几何对应的KK实现，但本轮核读发现，若把其普通cycle与结构层K-kernel措辞按字面无条件消费，会漏掉方向、推前及Todd／低次数项。修补后的兼容性仍没有提供新的physical源、有效算术lift或primitive mixed RR。它不构成KK／motivic路线的一般不可能定理。

## 1. 实际原件和本轮授权范围

[Connes–Consani–Marcolli，固定v2](https://arxiv.org/pdf/math/0512138v2)，2007-03-10，*Noncommutative geometry and motives: the thermodynamics of endomotives*。既存 `literature/f1/ccm-endomotives-math-0512138v2.pdf`，58页、747528字节，SHA256 `68f9c8eaa5e9b46790e5adad0e8cd910da43566e7bc339ea5ecc81ab1f3fe601`，本轮现场一致。

root实际目视PDF44–47页，逐式核§6及47顶部exact diagram；提取、页图均在忽略的本地库路径。页面中可见§5末段／§7正文不作本门前件；没有消费§7、追引[15]/[16]/[24]/[44]或声称重证原一般理论。两独占原稿为[域与复合](../../reviews/2026-10-27/ccm-correspondence/source-domain-composition.md)及[对象角色](../../reviews/2026-10-27/ccm-correspondence/roles-principal-relative-and-coverage.md)。

## 2. 实际可消费的有向对象

| 原件 | 实际前件／方向 | 本轮消费限制 |
|---|---|---|
| (6.1)，§6.1 | smooth Z、E复向量丛，f_X proper、g_Y K-oriented；得到k∈KK(X,Y)，按右Kasparov乘积作用K(X)→K(Y) | KK次数为dim_R Z−dim_R Y mod2；复结构只保证even，不自动保Chow整数grading。没有逆向有效cycle选择 |
| (6.2)–(6.4) | K-oriented index／Gysin的GRR；smooth transverse fiber product及tensor twist对应Kasparov product | Todd／Chern实现和signed virtual类不提供nef、正极化、原norm或small-section容量 |
| (6.5)–(6.7) | sheaf公式先pull Y、tensor、push X，方向为K(Y)→K(X) | 须transpose／opposite convention并交换所需proper/K-orientation腿；不能与(6.1)同时按同一有向作用读 |
| (6.10)–(6.14) | ordinary intersection/push与K0／geometric复合的比较，非横截有alternating Tor | raw cycle→O_Z不是无修正的CH复合函子；下节给同维光滑横截反测。derived perfect-kernel是另一个明确、合法入口 |
| §6.3 | K_alg→K_top的comparison fiber及HH/HC的degree／regulator图 | 不能把图的存在当作本项目代数／拓扑／degree已匹配；原引文的适用代数类别、低degree等未在本门重付 |

最小合法修补保留为：对指定smooth proper complex ambient及perfect kernel K，明确方向后使用 R p_Y*(L p_X* a⊗^L K)，以proper derived convolution组织K-kernel复合；若走几何模型，则另核smooth Z、K定向及横截smooth fiber product。singular Z上的O_Z可以是ambient perfect对象，但这不使Z自身成为smooth manifold。ordinary cycle／Chow实现另须说明grading、Todd及系数域。

## 3. 两个标准有限反测，不能按原字面跳过

原p45在(6.8)前将推前／拉回的伴随叙述接成 f* f!=id。伴随给unit／counit，不给这个等式。取 f:P¹→pt、β=[O(−1)]；rank β=1而χ(O(−1))=0，故 f* f!β=0≠β。这里没有把1−O(−1)误当index0。GRR／projection formula可保留，推拉消去不予消费。

对Prop6.1的raw ordinary-cycle措辞，即使补足smoothness仍不够。令

\[
 X=Y=W=\mathbf P^1,\quad Z_1=\{x\}\times Y,\quad
 Z_2=Y\times\{w\}.
\]

两者都是同维曲线间codimension1光滑对应。三重积中两个拉回的法向分别是第一／第三坐标，真正横截；交为V={x}×P¹×{w}。ordinary CH1 push沿π13因image dimension从1降到0而为零。但

\[
 R\pi_{13*}\mathcal O_V
 =R\Gamma(\mathbf P^1,\mathcal O)\otimes\mathcal O_{(x,w)}
 =\mathcal O_{(x,w)}\ne0.
\]

相应KK action把1_X送到[O_w]，其Euler index为1，故非零。这个差别不来自Tor非横截、奇异cycle或Tate次数不匹配，而是ordinary dimension-preserving cycle push与K-push之间确有较低filtration／Todd分量。若(6.13)解释为K0-derived push，则得到的是明确的K-kernel命题，不是无修正的ordinary-cycle (6.10)命题。正确的完整KK／GRR比较理论没有因此被否定。

这两个例子是原章节标准接口的直接校正，0数学轮；不把原文措辞问题升级为经典RH方法类边界。

## 4. 用同一583对象检验“非零K0读数”的角色

在P¹×P¹上记x=1−O(−1,0)、y=1−O(0,−1)，有x²=y²=0、xy=[O_point]，后者Euler index为1。有效Cartier divisor T的bidegree为(D,D)时，**whole Cartier结构层约定**给

\[
 [\mathcal O_T]=1-(1-x)^D(1-y)^D=D(x+y)-D^2xy.
\]

决定性例只需583中m=1：T1为不可约diagonal，R1=X−Y，正确principal divisor为T1−B1−B2。它在CH1中为零；若把各不可约cycle分量线性送结构层，得到

\[
 [\mathcal O_{T_1}]-[\mathcal O_{B_1}]-[\mathcal O_{B_2}]
 =-xy\ne0.
\]

native尺度2只把该值乘2，不能修下降。这说明这样的非零point腿不能冒称是“从583的principal商里恢复了primitive类”；赋值本身尚未杀掉principal relation。对一般m，T_m可能可约，whole O_(T_m)与按每个不可约分量线性求和不同；本轮不将上面的D公式当全m free-cycle函子，更不从中编造全源reader或经典Γ预算。

合法的“零映零”只适用于已经定义、逐个尊重正确关系且对所需completion连续的functor。CCM§6没有给583的Green/current→KK这样的map，故既不能免费在KK里保零，也不能免费把上述非零当新primitive。583本身的L1／mass、raw注入和指定连续principal类商全零证明没有用CCM§6作前件，保持有效。

## 5. 既有relative资产及完整Weil责任不合并

410／411的非零类是特定C* ideal-extension的boundary K0，含参数圆、Morita／axis检测器及ambient忘却零像；432是具体代数商HH1上的commutator-trace电荷；573是Q→Q_J的Hochschild链锥与−4反测。§6.3的relative K则是K_alg→K_top的comparison fiber。三种relative不能只凭名称同一化，HH1也不能直接当even K0 algebraic-cycle像。

原文特定scaling设置下的primary Chern vanishing不撤销这些已付非零电荷；本章也没有把它们的实际代数、degree、regulator和physical源接起来。不能说没有非零K类，也不能用已有非零K类代替同源primitive RR。Dn/n!、B/n等normalization及适用代数类别必须保留；本门不追引文补足。

完整经典Bζ的Γ/contact、全部properpowers、双pole、ALLcomplex物理源及原du／zero-extension Dlog／强源和成长费用，均未被该章节映射匹配。没有同一算术整模型的sections／消失阶／metric乘法、small-section log#容量、mixed正号或signed误差身份。单个K向量、virtual复合及GRR兼容本身都不是这些前件。

## 6. root消费、冻结范围与净值

本轮根前件是指定smooth/proper/K-oriented几何数据或修正后的perfect kernel，不是经典物理源；无r范数／全S_exp／成长量词费用，无数值误差或新Hermitian正号。普通cycle、关系商、physical和KK核的角色按上述区分，不能把多处标准正确接口合成未证的逆向算术lift。

原准入稿对Prop6.1的定位只是待审来源；现追加语义纠正，冻结其无条件ordinary-cycle／principal下降消费。只在明确修补前件下保留K-kernel／GRR接口；未受影响的583及410–437资产不回滚。两原稿和最终fresh须由root实际核读后才结算，不以出稿代消费。

strongest-old仍是542＋555→557 whole leading4/5负惯性UPPER；537／538 fixed17/16、560 fixed-window positiveTrace−compact+pole、583实际全尾均为输入。独立primitive容量、完整signedζ、actualq/core/coupling/Ξ主瓶颈未改。本章没有可应用的新input，故来源0止、不建C047／584、不续§7／引用／下一paper。原cadence1／历史47／cycle16保持，来源审查不加轮、不归零，Goal完成门仍open。

下一必须先有新的独立实物或能改变选择的具体比较/test/net，不能另找范畴名称替代同一未付箭头。后续准入审计与准确唯一动作见STATE；本来源停止不完成长期Goal。
