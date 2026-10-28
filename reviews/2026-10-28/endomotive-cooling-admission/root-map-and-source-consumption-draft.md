# Root：cooling map、cyclic coker及两源责任（待当前fresh）

2026-10-28；G20261027/runtime1793085111/原0c4f。此稿只按已实际读取的固定v2 §4.2–4.3作来源/类型消费草稿，不是已通过的根结算或数学合同。当前oldscope稿已全文读；当前source支持稿及不同fresh仍须匹配当前任务/版本后消费。

## 1. 实际原件与命题依赖

PDF747528b/SHA68f9c8ea…，58实际页；本次root实际正文/视觉读22–29，并按页界勘误读30上方Definition4.13/Remark4.14/(4.32)，止4.4。目录/引言locator为1–3。首crop误露整p30的4.4开头/Prop4.15已在gate记载，不消费其中HC0/character命题；修正后只用顶540px图。原全文/提取/图均ignored local。固定arXiv v2 landing page仅核作者/版本2007-03-10；comments52页和本地actual58差别保留，不替换原件或假称全文认证。

§4.2的假设：state modular action保持A；β足够大时regular extremal KMSβ为type I∞。Lemma4.3给irreducible π_ε及自伴H、Trace(e^-βH)<∞；H只差实常数。(4.8)表示Â=A⋊σR，(4.9)S(R,A)为finite-dimensional coefficient subspaces的direct limit，乘法为twisted convolution(4.10)。(4.12) dual scaling θ_λ令H平移logλ。

Âβ的输入为在闭strip Iβ边界Schwartz的analytic A-valued函数，不是任意C*或原du source的自动等价完成。Prop4.4给traceclass输出；Cor4.6/(4.24)在连续fixed-Hilbert realization/lift(4.23)假设下给等变代数态射

    π: Âβ → C(Ω̃β,L¹),   x ↦ [(ε,H) ↦ π_(ε,H)(x)].

每ε的正KMS密度/traceclass并不直接给完整经典Weil型正号或source-du范数比较。

## 2. Trace的实际角色与余核

Prop4.7是**Λ-module map**。在unital B的tensor模型，各degree的式为

    (b0⊗t0)⊗…⊗(bn⊗tn) ↦ (b0⊗…⊗bn) Trace(t0…tn).

trace使用同一个算子乘积，证明靠cyclicity与faces/degeneracies相容；不是把Trace(t0…tn)替换为∏Trace(tj)，也不是宣称degree0 Trace是algebra homomorphism。p27对nonunital对象先unitize/augmentation-kernel，并保compactification cyclic module。不能把algebra object、degreewise tensor和Λ-module quotient混成ordinary quotient algebra。

因此原文**确实有两/多输入的上游公式**。在common-Hilbert lifting的可表达tensor模型中，degree1读作含Trace(π_(z0)(x0)π_(z1)(x1))的函数；其身份是δ的cyclic-chain像，进入coker时作为relation被商去，不是已经从D的两个类构造的internal product。非平凡higher chain/derived pairing仍须按其不同target单独给出，不能因这份image检查否定。

BC标量示例p28的H-spectrum为log n，trace为Σ_(n≥1)g(logn+c)。这是实际theta/Pan型关系来源的标量说明，非独立positive target。Lemma4.8的c→+∞ trace估计证明已在范围内；Lemma4.9/(4.26)的c→−∞主项e^-cτ(x)+O_N(|c|^-N)证明明确延后到Lemma4.17之后，本次**未核**。一般非BC情形Remark4.14还明确可能不满足(4.26)。不以该陈述作新的proved尾估计。

Lemma4.10把Âβ变成Hol(Iβ)-module，F◦Trace◦π为module map；这是external multiplier / 经dual scaling积分的作用。Cor4.11只在BC、x∈Âβ∩kerτ及上述衰减前提下给C(Ωβ,S(Iβ))范围。Prop4.12明确assuming(4.26)，定义δ: Â^natural_(β,0)→S^natural(Ω̃β)。这里0下标引用(5.1)，本次未读；不得把所有degree替成degree0 kerτ或声称任意physical r自动在domain。Def4.13定义D(A,φ)=coker_Λ δ；按408已核p9通用约定理解closed-image coker，而非本定义另证像已闭。

Remark4.14若连续Hilbert lift/Morita triviality失效，Dixmier–Douady twist可能迫目标用continuous elementary-C*algebra field sections；(4.32)仍是等变algebra homomorphism。它保留另一合法对象，未给physical-source范数、非零primitive或mixed正号；不把twist出现冒已解决更强源问题。

## 3. 最便宜两源/源位置test

旧scope稿给的下降条件按实际δ填写：若R_j=closure Ranδ_j，拟lift B~到目标关系R_l，则要同时有B~(R_j,Z_k)⊂R_l、B~(Z_j,R_k)⊂R_l，并有拓扑/continuity以过closure。当前指定段落提供cyclic operations和external Hol action，没有给该internal two-source lift的定理；也没有给R在目标ordinary乘法下为双侧ideal的证明。这里只消费**原段落未提供**，不证明实际ideal不成立、所有product不可能或整篇无这类定理。generic2×2 trace例不作为actualimage反例。

最直接source角色检查是：对任何**已合法**x_r∈δ_0的domain，若拟令q_r=[δ_0(x_r)]∈D_0，则q_r=0按coker定义成立，closure只扩大被杀关系。这不是D=0或全部r类=0；不是未读(5.1)域的保证；只是source-through-image不能当新非零primitive。真实物理源若放在target的别处，仍须给q_r的公式、405全部非compact Pan/translate消去、537非根可见性及norm费用，不能由该零化推断不存在。

同理，external convolution算子Φ_rΦ_s=Φ_(r*s)、continuous dual evaluation与nuclear character均不能直接替代q_r×q_s→mixed。405/518–520及Meyer§5/Th5.8已付更强谱module/zerojets/trace设施，先扣；本门没有重核未付的不同cyclic-degree拓扑比较。Canonical closed-ideal inclusion cone exact0/6L1与此δ无实际比较map，故不搬其结果；10-27§6的ordinary-cycle冻结也不扩到此处。

## 4. 拟结算（待fresh/root final）

此指定段落核清π→partial trace→cyclic δ→coker的类型及source-through-image零化；未取得独立physical nonzero primitive、可下降内部两源操作、principal/整截面乘法/mixed RR/完整Weil身份或signed corecross净量。只是来源/强旧角色0，不建C053/590，不加数学轮；cadence3/history53/latest589/formal17保持。强旧542+555→557 whole4/5负惯性UPPER未改，原Γ/contact/allpp/双pole、原du/zeroextension Dlog/ALLcomplex覆盖费用未付项仍未付。

若当前source稿/fresh确认，停止本门，不顺读4.4/§5/§7、(5.1)或4.26后置证明，不据未付产品重排另个来源。重准入必须有实际不同q_r/B~或新primary精确命题，能改变上述下降/非零test；不以“余核非零/谱实现”换名。Different twisted/higher/derived/有费强源与joint signed保留，其合法性不构成新输入。Goal同实例active/open/noteligible；实际核心瓶颈未变，只有此cooling候选的晋级选择被判定。
