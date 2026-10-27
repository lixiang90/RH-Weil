# CCM §6：实际映射方向、K 定向及复合前件审查

2026-10-27；独占来源稿，供 root 消费。恢复已核 README／STATE、check→show、G20261027、D20261027D、宏观前沿和上一轮的单门准入稿。C046／583 为既有输入；本稿不重开其预算，不建 C047，不改 STATE／cadence／文献库／看板。下列有限例只校正原件的标准接口，0 数学轮，不提供经典 ζ 的新后果。

## 1. 固定版本与实际阅读

原件是 Connes–Consani–Marcolli，[*Noncommutative geometry and motives: the thermodynamics of endomotives*](https://arxiv.org/pdf/math/0512138v2)，arXiv math/0512138v2，2007-03-10。本地 `literature/f1/ccm-endomotives-math-0512138v2.pdf`：747528字节、58页，现场 SHA256 为 `68f9c8eaa5e9b46790e5adad0e8cd910da43566e7bc339ea5ecc81ab1f3fe601`。

实际核 PDF／正文44–46页的§6.1–6.3及第47页顶部的 exact-sequence 图，止于§7标题；没有消费§7或追[15]、[16]、[24]、[44]。pdftotext 后又目视四页 render，以下问题确在原排版中，不是 OCR 错字。局部提取和页图只存 `literature/local/2026-10-27-ccm/`，不入 Git。

## 2. 逐项实际 domain／range 与可消费范围

| 原件位置 | 实际数据与量词 | 可消费结论／限制 |
|---|---|---|
| p44 §6.1、(6.1) | 光滑 Z，X／Y 为光滑流形（原讨论允许 X 仅 locally compact）；f_X:Z→X continuous proper，g_Y:Z→Y continuous K-oriented；E 为 Z 上复向量丛 | 在这些实际前件下给 k(Z,E,f_X,g_Y)∈KK(X,Y)。不要求 Z 嵌入 X×Y，但并未构造任意物理源的 Z 或 E。 |
| p44–45 (6.2)–(6.3) | f:X1→X2 K-oriented，F∈K*(X1)，Td(f)=Td(TX1)/Td(f*TX2) | 以 Chern character 表达 f! 的 GRR；这是有理 characteristic-class realization，不能倒推整性／有效性或范数。K! 的 parity 是相应虚切丛实维差 mod2；复代数情形该差为偶，仍不自动保留 Chow 的整数 codimension／Tate grading。 |
| p45 (6.4) | 两 smooth correspondences 的 g_Y、f_Y 横截，纤维积 smooth，E 为拉回丛的 tensor product，proper／K-orientation 在复合下按原条件运输 | 给 geometric KK correspondence 的 Kasparov product。图中文字 tensor-like 记号应按向量丛张量解释，不能当作新的有效代数cycle乘法。 |
| p45 §6.2、(6.5)–(6.7) | X、Y smooth projective algebraic varieties，Z 先取自由 cycle 群中的一个 irreducible subvariety；p_X、p_Y proper | (6.6)字面的 sheaf 公式将 O_T（T⊂Y）送到 X 上 coherent sheaf，即 Y→X 的 kernel action；与 (6.1)∈KK(X,Y) 的惯用 K(X)→K(Y) action 方向相反。必须选 transpose／opposite convention；不能同时按字面认作同一个有向 action。 |
| p46 (6.10)–(6.11)、Prop6.1 | X、Y、W smooth projective，Z1、Z2 单个 irreducible correspondence，π12*Z1、π23*Z2 general position | 该段意在比较 composition，但其 raw ordinary-cycle 与 structure-sheaf K-push 的字面认同过强；下节给 smooth transverse same-degree 有限反测。只能在修正后的 K-kernel 或 graded／Todd realization 中消费兼容性。 |
| p46 (6.14) | 非 general-position intersection | 明列 derived tensor 的 alternating Tor classes；修正是 signed virtual K-class，非有效 cycle 的正分解。General position、smoothness、Tor-independence也不是完全相同的前件。 |
| p46–47 §6.3 | algebraic／topological／relative K 及 cyclic／Hochschild 的比较图 | 图含 K_top(n+1)→K_rel(n)→K_alg(n)→K_top(n) 与下面 HC(n+1)→HC(n−1)→HH(n)→HC(n)，以及 D_n/n!、B/n 等 normalization。它是引文支持的比较框架，不是物理源／有效lift构造；不能抹掉 degree、denominators、适用代数类别和边界 maps。 |

KK(X,Y) 的 action 方向在本文采用 K_j(X)=KK_j(C,C0(X))，对右侧 Kasparov 乘积给 K_j(X)→K_(j+deg k)(Y)。因此 (6.1)可写成 f_X^*、乘E、g_Y! 的连续 action；而 (6.6)先 pullback Y 再 push X，方向明确相反。可以合法换约定，不可以不说明就消费。

更明确地，(6.1)的 parity 为 dim_R Z−dim_R Y mod2；取transpose要同时交换proper／K-oriented两腿，并重新检查前件，而非仅把KK(X,Y)标签反写。在complex geometric情形这些实维差虽为偶，Chow的整数codimension／Tate grading仍未被完整携带。

## 3. 不能按字面消费的三处，及最小合法修补

### 3.1 p45 的 pull–push identity 不是 adjunction

原文在(6.8)前把 f! 的 right-adjoint 叙述与 f* f!=id 联系。Adjunction 给 unit／counit，不给这个 identity。对 K-oriented proper f，GRR 的 f! 是 index／Gysin push；一般也不能把它直接称为普通 pullback 的 right-adjoint 并由此消去。

最短标准反测：f:P¹_C→pt，β=[O(−1)]∈K⁰(P¹)。β 的 rank 为1，故非零；complex-oriented index χ(P¹,O(−1))=0，故 f* f!β=0≠β。这里 χ(O)=1，而 χ(O(−1))=0；不能错误地把 1−O(−1) 当作 index0 的例子。

因此 (6.9) 后那段用 pull–push cancellation 连接 sheaf intersection 与 KK 的字面推导不予消费。正确的 GRR／projection formula 可另使用，但它们不包含这个 cancellation。

### 3.2 typed sheaf／derived／smoothness 前件

p45 (6.7) 的 tensor base 字面写成 p_Y^−1 O_X，但 O_X 在 X 上而 p_Y 的靶是 Y；应为 p_Y^−1 O_Y。下一段把 O_T（在Y上）与 O_X 上的对象直接 tensor，也必须先支付 pullback／ambient base，不能按符号略写完成 typed comparison。

(6.6)只说 coherent direct image，在 proper 情形 coherent 是对的，但 ordinary pushforward 不是一般 exact functor；若要对 Grothendieck K0、复合及 GRR 消费，应使用 R p_* 的 alternating higher direct images，并使用 L p*／derived tensor。Smooth ambient 的 coherent O_Z 可用 perfect resolution，所以可修为 ambient perfect kernel；并不因此使 singular Z 成为§6.1要求的 smooth correspondence。原文 Prop6.1只要求 ambient smooth 和 general position，未明列每个 Z smooth，不能把所有 raw Z 都直接当 smooth manifold 送入(6.1)。

本稿只接受最小修补：固定 smooth proper complex ambient，令 kernel K∈Perf(X×Y)，明确方向后以 R p_Y*(L p_X* a⊗^L K) 定义正向 K action；复合由 derived convolution 付款。若改回几何 correspondence，则另要求 Z smooth／适当 K-oriented maps 和 transverse smooth fiber product。二者是不同的合法入口，不免费互换。

### 3.3 即使全光滑横截，ordinary cycle composition 仍不等于 K-kernel composition

这个反测排除了只补 smoothness 就无声恢复原字面(6.11)的做法。取

\[
 X=Y=W=\mathbf P^1_{\mathbf C},\qquad
 Z_1=\{x\}\times Y,\qquad Z_2=Y\times\{w\}.
\]

两者都是光滑 codimension1 cycles；三个曲面上的两个拉回，分别由第一坐标=x与第三坐标=w给出，normal方向独立，故 genuinely transverse／general position。交为

\[
 V=\{x\}\times Y\times\{w\}\simeq\mathbf P^1.
\]

按 ordinary Chow-cycle proper push，V的image在 X×W 只是点(x,w)，dimension从1下降到0，因此

\[
 (\pi_{13})_*[V]=0\quad\text{in }CH_1(X\times W).
\]

但对应的 ambient perfect kernels 满足

\[
 R(\pi_{13})_*\mathcal O_V
 =R\Gamma(\mathbf P^1,\mathcal O)\otimes\mathcal O_{(x,w)}
 =\mathcal O_{(x,w)}\ne0\quad\text{in }K_0(X\times W).
\]

非零性也可直接在 action 检查：第一 kernel 送1_X到1_Y，第二送1_Y到[O_w]；χ(O_w)=1，故 [O_w]≠0。这个例子三条曲线同维、两个原 correspondence 均 codimension1，且 smooth／proper／complex K-oriented／横截前件齐全，不能靠 parity 或笼统“补 smooth”回避。

差异是 structure-sheaf realization 的较低 filtration／Todd 腿被 ordinary dimension-preserving cycle push 丢掉。原文若将(6.13)实际解释为 K0-derived push，就已换成 K-kernel convolution，而不是(6.10)所写 ordinary algebraic-cycle composition。正确兼容可以保留为这个更明确的 K-kernel statement；若用 Chow/cohomology，则须给相应 GRR／Todd factors、grading 和系数域，不能把 [Z]↦[O_Z] 当作无修正的所有 ordinary-cycle push／composition functor。本稿未追引文，不重证该完整一般理论，也不把这一有限标准例当作新的 RH 方法边界。

## 4. 整性、正号与 secondary 图不能额外提供什么

原 cycle 的整数系数只给自由 abelian cycle data；E 的 K-class、Tor alternating sum和KK群都允许 virtual differences。Exact／Chern diagrams保 functorial operations，不给 effective cone、nef／primitive条件、positive Hermitian pairing或两独立源的 mixed inequality。Todd／Chern character要有理系数及显式normalization；不能从cohomological equality反推integral section lift。

§6.3说明需要 secondary／relative invariants的方向，并把特定 scaling 设置中的 primary vanishing 归入后续[15]。本章没有证明所有 continuous group actions 的全部 primary Chern characters都零；也没有由这幅图构造本项目的 r→K_rel 源或其范数。已知410／411／432／573的非零relative／cyclic资产不因此消失；它们能否处于此图相同 degree／代数类别并与 physical source 比较，须由另一实际map付款，不能通过命名完成。

图的存在在本章引用[16]；本次没有检查该引文适用的具体代数类别、topology／completion、低degree约定及regulator域，故不对任意本项目代数A宣称整幅exact diagram已适用。D_n/n!和B/n仅按图给出的相应degree读取，不将n=0等未说明项强行套用。

本章没有算术整模型、arch metric、small-section log#、消失阶／截面乘法的定量费用，亦无405全noncompact关系的actual边界公式或537非根的geometric image。完整Γ/contact、properpowers、双pole和ALLcomplex原费用未被此兼容框架替换。

## 5. root 可消费的前件／净值记录

* object/domain-range：指定 smooth／proper／K-oriented geometric correspondence 到 KK；修正后也可为 smooth proper complex ambient 的 perfect K-kernel action。不是任意 classical physical source 到 effective algebraic correspondence 的反向lift。
* norms／growth：本章没有支付 r 的 du／zero-extension Dlog、全S_exp强半范数、成长源窗／arith height或任何全尾；不声称输出原范数连续。
* paid dependencies/errors：固定v2实际§6原页；(6.1)／(6.4)只在已写前件下消费，(6.11)不按raw ordinary-cycle字面消费。两个P¹有限校正为标准直接计算，无数值误差。原[15]/[16]/[24]/[44]本体未重读，无代为背书。
* coefficient/sign：Kpush和Tor允许signed virtual classes；GRR的Todd腿及mod2 KK degree与Chow grading不合并。无positive/mixed身份。
* relation/quotient/physical：583的连续principal零类不能通过一个适用的additive兼容functor变成非零；不同目标／非continuous／relative来源尚需实际定义。本章既不提供正确消405并保537的primitive载体，也不否定其他合法来源。
* strongest-old net：583已付global native尾、410–437已有非零relative电荷、567已有RR机制均为输入；本章只厘清方向和字面兼容的范围。542＋555→557 whole leading4/5负惯性UPPER、actualq/core/coupling/Ξ及独立primitive容量未变。

按单门停止规则，**来源0结束，不建C047，不续§7或追下一paper**。没有可应用的新physical／primitive／signed输入，不能把修补后的兼容理论当作已经取得的新算术源。最终root消费、计数、战略和同步由root负责。
