# CCM §6 来源门：独立 fresh 审查

2026-10-27；审查者 `/root/ccm_fresh_review`。只编辑本稿，不修改 STATE、cadence、合同、看板或文献库。已恢复 README／STATE、check→show、G20261027、已结算C046、D20261027D与宏观前沿；本次限定为保存的来源0动作，不新建数学合同或研究轮。

**最终结论：限定PASS。** 已核两份原稿、root主稿及实际前件消费记录，支持按其精确范围来源0停止；不支持新增C047／584、数学轮或长期Goal完成。

## 1. 实际阅读与原件定位

全文核读 `source-domain-composition.md`、`roles-principal-relative-and-coverage.md` 的已落盘版本，并实际目视既存固定PDF的44、45、46页和47页顶部§6.3图。原件为CCM math/0512138v2，2007-03-10，本地 `literature/f1/ccm-endomotives-math-0512138v2.pdf`；消费止于§7标题。未追读[15]／[16]／[24]／[44]，也不以页图中可见的§5末段或§7正文作为本门前件。

原排版确认：p45(6.6)是pull Y／push X的方向；(6.7)确印了不typed的pullback base；(6.8)前确有pull–push identity措辞。p46(6.10)明确为algebraic-cycle intersection及proper push，(6.11)却与对应的KK product认同；这些并非OCR造成的疑点。

## 2. 方向、degree与最小修补

以KK(X,Y)作用在K*(X)上的惯例，(6.1)依次为f_X pullback、E twist、g_Y K-oriented push，目标是K*(Y)。p45(6.6)按sheaf formula则从Y到X；两者可用transpose／opposite convention组织，但必须同时交换两腿并检查proper／K-oriented条件，不能只改标签。

KK的degree按2周期读取；在复几何中实维差为偶并不保留完整Chow codimension／Tate grading。GRR需要Todd项和characteristic realization的系数域，不能将Chern equality反用作整性、effective／nef或metric正号。

Z可能奇异，而§6.1要求smooth Z。smooth ambient中O_Z能由perfect resolution处理，合法修补是明确方向的perfect kernel及derived convolution；它不是证明原Z已是smooth correspondence。ordinary p_*对coherent sheaf的存在也不保证它在K0中exact，涉及GRR和复合时须保higher direct images、derived pullback／tensor及Tor。修补后的正确理论保持合法；本审查不否定一般KK或motivic比较。

## 3. 两个有限反测已独立核算

### pull–push identity

取f:P¹_C→pt、β=[O(−1)]。其rank为1，故K⁰类非零；complex index χ(P¹,O(−1))=0，所以f* f!β=0≠β。adjunction只有unit／counit，不能给原字面的inverse identity。此例没有用未知ζ信息或数值实验。

### 同维、同codimension、光滑横截的cycle／Kpush差别

取X=Y=W=P¹，Z1={x}×Y，Z2=Y×{w}。两者都是smooth codimension1 cycles；在X×Y×W中两拉回的normal方向分别为第一和第三坐标，故transverse，交为V={x}×Y×{w}≅P¹。所有proper／complex K-orientation条件成立。

ordinary cycle push (π13)_*[V]为0，因为image只有点(x,w)，比V少一维。另一方面，perfect-kernel convolution是

\[
 R(\pi_{13})_*\mathcal O_V
 =R\Gamma(\mathbf P^1,\mathcal O)\otimes\mathcal O_{(x,w)}
 =\mathcal O_{(x,w)}\ne0.
\]

其KK作用也直接检出非零：第一kernel送1_X到1_Y，第二送1_Y到[O_w]，而χ(O_w)=1。因此原(6.11)不能作为未经修正的ordinary-cycle→structure-sheaf functor消费。此例三个空间同维、两cycle同codimension，不能靠Tate-degree不匹配、补smoothness或Tor修正回避；在本例Tor本已消失。

若将(6.13)理解为derived K0 push，那么保留的是K-kernel复合兼容；若要回到ordinary Chow cycles，须明确graded／Todd realization。两原稿保留了这一准确范围，没有把有限反测升级为所有KK路线的不可能性或新的RH方法边界。它是本来源0门的标准接口校正，不单计研究轮。

## 4. 旧relative资产与principal角色

已查旧410的boundary K0类及ambient零像、411的共同轴trace与2a log p权、432的HH1 commutator charge、573的relative Hochschild cone和首腿闭性。两原稿的角色区分成立：

* 410／411是特定C* ideal extension的boundary K0；ambient忘却为零不撤销relative非零。
* 432是具体商代数上HH1及trace-class准入后的ordinary commutator trace，不凭名称成为KK／algebraic K0 cycle。
* 573的relative cone属于Q→Q_J的链复形，首腿仍须闭；与§6.3比较K^alg→K^top的homotopy fiber不是同一relative构造。

§6.3的primary-vanishing措辞没有识别本项目相同代数／degree／Chern map，不能据此消去上述非零资产。反向也不能由其非零性领取有效代数lift、mixed RR或完整Weil身份。

583的balanced pair只在其指定连续principal quotient中为零。只有实际定义并通过该商下降、或杀principal关系且对已付completion连续的functor，才必然保这个零类。当前章节没有给从583 L1×mass pair到KK的这个map；不能直接宣称583的KK像为零，亦不能逐分量送O_Z后将产生的低filtration读数称为被恢复的primitive类。

## 5. 待root消费的范围

本审查目前支持来源0停止：原件给指定已有对象的运输组织，并无可应用于本项目physical全源的逆向有效算术输入；literal兼容须按上述domain／degree／derived／Todd范围收紧。derived kernels、secondary／relative目标、不同metric或强拓扑修复仍合法，但当前章没有支付它们的实际源公式及费用。

root最终稿仍须保：原du／zero-extension Dlog及全S_exp强半范数、完整Γ/contact／properpowers／双pole、405真实noncompact关系及537非根、同对象整过滤／sections乘法／mixedRR、coverage／coupling。当前章节没有给这些费用或signed身份；strongest-old542＋555→557 whole leading4/5仍为负惯性UPPER。不得建立C047／584、追§7或下一paper，也不据本门完成长期Goal。

## 6. root主稿与实际版本的最终核验

实际全文核读 `goals/reviews/2026-10-27-ccm-geometric-correspondence-source-gate.md` 与 `root-consumption-scope.json`。root对普通cycle、K-kernel、Green/current pair及已定义quotient的角色区分成立；两个P¹有限反测、反向sheaf action、singular Z与ambient perfect object的差别均保留。有限修补未被扩大为原论文一般理论已经重证，也没有用新范畴标签代付物理source、关系、原norm或mixed正号。

root及角色稿补充的同对象m=1检验可独立闭合。在P¹×P¹上，x=1−O(−1,0)、y=1−O(0,−1)满足x²=y²=0，xy为point结构层类且Euler index为1；diagonal Δ有O_Δ=x+y−xy。故逐不可约分量的naive structure-sheaf赋值将principal relation Δ−B1−B2送到−xy≠0。这只证明该赋值未沿principal关系下降，不能称为从583零类中恢复的primitive。

一般bidegree(D,D)的whole effective Cartier T满足[O_T]=D(x+y)−D²xy，但可约T的whole structure sheaf与逐不可约components线性相加不同。root已明确只用m=1作为决定性例，并将一般D公式限于whole-Cartier约定；没有把它误用为全部m的free-cycle reader，也没有从未构造的reader领取全源费用或新预算。这一限定是必要的，当前版本已满足。

既有410／411的boundary K0、432的HH1和573的relative cone都按原degree／pair保留；§6.3 comparison fiber未被当作它们的共同代数模型。583不依赖本章证明，因此本次语义纠正仅冻结CCM原字面(6.11)的无条件消费及自动principal下降，不回滚583或已有relative电荷。

本门不产生经典独立正性、成长预算或实质核心方法类边界；source0计数与cadence保持1／历史47／cycle16一致。尚无可应用的新physical／primitive输入，按原规则止§7、不追引文及下一paper。无剩余必须阻止此精确范围结算的修正项；新的实际输入或可改变选择的具体比较仍可另作准入，但不是本审查已验收的成果。

已核root记录的三个实际LF SHA256，均相符：

| 原件 | SHA256（LF） |
|---|---|
| root主稿 | `ad9e3805b428ef8ba58f15c19e5edd2e8379870a28301be91f9e616320008e4b` |
| 域／复合原稿 | `4f52b2922fdd7a5a707991e4a3e6ac2d7b0f4b4fa3565be6314a826ddc236f4b` |
| 角色原稿 | `482a5eb7b26c75ea3000c763682bca63a819e23a2e8f23654851b85d0e464b36` |

原始PDF SHA亦与root记录一致。哈希只固定审查版本，不代证明；本审查未验收GitHub同步，亦未修改STATE、cadence、合同或文献库。
