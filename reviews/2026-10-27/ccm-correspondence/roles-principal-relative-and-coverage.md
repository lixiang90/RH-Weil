# CCM §6 的对象角色：principal 零类、既有相对电荷与未付覆盖

2026-10-27；G20261027／原0c4f基线。独占角色比较稿，交 root 消费；不改 STATE、cadence、文献库或看板，不开数学合同。已恢复 README／STATE、check→show、Goal、C046结算、D20261027D、宏观前沿及583后唯一准入稿。C046预算已耗尽，本文只执行保存的来源0门。

原件为既库 CCM *Noncommutative geometry and motives: the thermodynamics of endomotives*，固定 math/0512138v2，2007-03-10，[原PDF](https://arxiv.org/pdf/math/0512138v2)，本地 `literature/f1/ccm-endomotives-math-0512138v2.pdf`，SHA256 `68f9c8eaa5e9b46790e5adad0e8cd910da43566e7bc339ea5ecc81ab1f3fe601`。本分支实际读 §6.1–6.3、printed/PDF44–47，并目视四页公式及第47页上部exact diagram；消费止于§7标题。缓存所含的§5末段或§7文字不作此门的数学前件，没有追读引文或下一章。

## 1. 章节付的是已有几何数据的运输，不是物理源的逆向 lift

§6.1的实物输入是 smooth correspondence `(Z,E,f_X,g_Y)`：f_X proper，g_Y K-oriented，E为复向量丛；Z不必嵌入X×Y。其(6.1)构造 k(Z,E,f_X,g_Y)∈KK(X,Y)。以通常KK惯例，其对K理论的作用为

\[
 K^j(X)\longrightarrow K^{j+\dim_\mathbb R Y-\dim_\mathbb R Z}(Y),
 \qquad \alpha\longmapsto (g_Y)_!\bigl(f_X^*\alpha\otimes E\bigr),
\]

次数按2周期理解。K定向保证 pushforward 合法，并不选择有效代数cycle、Hermitian metric、nef类、small sections或正极化。若所有空间为复流形，相关实维差为偶；这只给even parity，不等于完整codimension／Hodge grading已内在恢复。

§6.2的(6.6)却按 `pull p_Y → tensor O_Z → push p_X` 写 sheaf action，所以是从Y到X。在适当derived/perfect-kernel条件下，其安全K理论版本是

\[
 K^0(Y)\longrightarrow K^0(X),\qquad
 \beta\longmapsto (p_X)_!\bigl([\mathcal O_Z]\otimes^{\mathbf L}p_Y^*\beta\bigr).
\]

若要与§6.1的k∈KK(X,Y)比较，必须明确采用transpose convention或交换输入／输出两腿；不能把原文相近的符号当作方向相同。若Z为codimension c且d_Y=dim_CY，Chow的对应分量从CH^p(Y)到CH^(p+c−d_Y)(X)；K0作用包含不同cohomological degree的Todd／Chern分量，不能省掉grading再把任何K0读数称为primitive交数。

原文还把一般irreducible algebraic Z直接当smooth correspondence的Z，并以O_Z作bundle。X×Y光滑时，O_Z可作为ambient perfect K0 kernel处理；Z自身却可能奇异，O_Z在ambient中也不是普通向量丛。要使用§6.1的smooth model，须另付合法smooth representative／resolution及其K定向、pushforward和误差。当前章节没有给本项目源所需的这种具体模型。

## 2. 复合与principal下降须分别核，不能由“functor”名称代付

PDF45原文在(6.8)前将f!说成f*的right adjoint并接f*f!=id；后者不是一般adjunction的推论。GRR只给Chern character与pushforward的兼容式，不能证明任意对象有逆向代数lift。本文不消费该literal identity，也不据此搬运本项目relative类。

Prop6.1／(6.11)的general-position假设与(6.14)的Tor修正是实际需要的前件；derived tensor加proper derived pushforward是合法perfect-kernel复合的安全组织。此处不将该命题的cycle措辞升级为任意Chow类、奇异cycle和coherent K0之间已构造的无条件函子。

特别是，按不可约分量线性指定Z↦[O_Z]，不自动成为CH ring homomorphism或尊重所有rational equivalence的映射。一个标准角色提示是：有效Cartier divisor D有 `[O_D]=1−[O(−D)]`，但按分量相加的Σn_i[O_(D_i)]一般不能替成[O_(Σn_iD_i)]；后者带scheme structure及较低degree信息。这只是防止误消费的标准K0事实，不在本门另计数学结果。

因此，583的full principal Green pair在指定连续principal quotient中为零，并不等于“把其cycle分量逐个送[O_Z]，就在KK里也为零”。合法说法仅为：**若某个已定义functor确实从该quotient下降，或先证明它逐个杀掉正确principal relations并对已付completion连续，则零类必映到零。** §6没有给这个Green/current到KK的具体映射、relation／boundary验证或L1×mass连续性。它不能免费把旧零类变成新非零primitive，也不能免费以KK=0否定raw记录或另一relative目标。

这有一个与583同对象的标准负对照，无需新源或新合同。固定X=P¹×P¹，写

\[
 x=1-[\mathcal O(-1,0)],\quad y=1-[\mathcal O(0,-1)],
 \qquad K^0(X)=\mathbb Z[x,y]/(x^2,y^2).
\]

在m=1时，R_1=X−Y，零除子为diagonal Δ，完整principal divisor为Δ−B1−B2。真正CH¹类为零，O(divR_1)为平凡line。可是按irreducible cycle各自取structure sheaf并线性相加，得到

\[
 [\mathcal O_\Delta]-[\mathcal O_{B_1}]-[\mathcal O_{B_2}]
 =(x+y-xy)-x-y=-xy=-[\mathcal O_{\rm point}]\ne0.
\]

最后非零可由Euler characteristic为−1检测。这是同一个principal relation未被该naive赋值杀掉的明确反测；若用native的2倍cycle尺度，残余也同步为−2[O_point]，不能忽略尺度。它不是principal quotient的像“重新非零”，而是该赋值根本没有沿正确关系下降。point项在较低filtration中，取codimension1／Chern首项才消失；不能把这个低degree项叫作新的primitive容量。

对一般bidegree(D,D)的**whole effective Cartier divisor** T，其structure sheaf满足[O_T]=D(x+y)−D²xy，若再扣D[O_B1]+D[O_B2]便残留−D²xy。这里须保whole-divisor convention；composite m的T_m可reducible，对整个O_(T_m)的公式不等于按每个irreducible component线性求和的同一赋值。m=1的irreducible对照已经足够，本门不以一般m误认来扩张结论，也不建立新的full source→K映射或费用下界。

## 3. 已有资产的真实degree／目标表

| 资产 | 原件实际对象与读数 | 与CCM §6不能默同的角色 |
|---|---|---|
| 583 balanced principal完成化 | 整数基先lift再复化的 `(2Z(r),G(r))`；fixed复粗P¹×P¹上global L1×current-mass尾；在杀finite principal span的指定连续商中全像零。raw analytic/current仍注入全部源，保Pan与537。a0Φ0另保line标签 | 不是已给smooth manifold correspondence，也不是ordinary locally finite divisor或CH类。没有本章KK输入或对该拓扑连续的descent；不能直接指定其KK像或forget Green/boundary后仍称同一类 |
| 410的Ξ_a | p^Z紧支箭头经实际C*扩张boundary map `δ_J[1−zU^a]∈K0(C(S¹)⊗I_J)`；Morita核丛[L_a]检测非零；进入ambient B_J/C*(G(p))后像零 | 是ideal-extension的boundary K0，带参数圆及特定Morita比较；不是凭名称就等于X×Y中的codimension0/1cycle。忘却的零像不撤销relative非零 |
| 411的Ω_(p,a)／k_p | `K0(C(S¹)⊗I_p)`的真实全Q×相容相对类；共同axis quotient中trace检测 `2a log p`，k_p的trace为`2 log p`；ambient忘却仍零 | 共同轴将finite坐标置零，仅是合法非零检测器。`a log p`与显式公式`Λ(p^a)=log p`不同，不能删a或把trace看作完整Weil型。C* K0不自动有代数cycle lift、metric或RR过滤 |
| 432的Ω | 具体有界代数 `A_src=alg(1,u,u*,D_src)`、代数商 `Q_src=A_src/S1`；实际closed one-cycle上的ordinary commutator trace定义 `Ω:HH1(Q_src)→C`，角点读数为`−4∫s h(s)k(−s)ds` | 这是HH degree1、trace-class ideal准入与闭链数据；原weighted source链一般不闭。不是K0 algebraic correspondence，也不能由“Chern character”一词认成任意KK像 |
| 573的ideal反测与relative pair | 指定解析扩大域中以δF_(r*)生成J_*；有finite-rank commutator trace−4，使旧Ω不能沿HH1(Q)→HH1(Q_J)下降；norm closure杀raw源。真实两层Hochschild cone保(ζ,0)的−4 | relative complex是Q→Q_J的链锥，既不是C* ideal K0本身，也不是CCM algebraic/topological comparison fiber。首腿仍须闭，第二腿不自动修复c_r。未给整模型／filtered sections |

上述非零K／relative／循环电荷是真实既有资产；不能把本门的“未给可用lift”改写为“项目一直没有非零K类”。反方向也不成立：这些资产的非零性不自动给同一primitive代数cycle或mixed pairing。若未来真有比较，必须指定同一个代数／pair、degree、map方向、relation、topology、regulator与原费用，不能只做标签对齐。

## 4. §6.3 的relative comparison不是上述相对对象的自动同一化

PDF46–47介绍的K_n^rel(A)来自K^alg(A)→K^top(A)的classifying-space比较，其exact sequence与HH／HC通过Chern character和regulator相连。图中的次数是

\[
 K_{n+1}^{top}\to K_n^{rel}\to K_n^{alg}\to K_n^{top},\qquad
 HC_{n+1}\to HC_{n-1}\to HH_n\to HC_n.
\]

这与410／411的ideal-extension boundary、573的Q→Q_J Hochschild cone是三种不同的relative构造。exact diagram并没有自动给它们之间的比较图、excision或本项目源的map。HH1若欲来自图中middle Chern项，需实际K1^alg元素及其Dn map，而不能把even K0、任意trace或HH1循环自由互认。图中的Dn/n!、B/n等归一化也不能用来声称已保持全部integral filtration；本门仅记图示的rational characteristic transport。

原文关于continuous scaling下primary invariants为零的叙述，是其相应action与Chern character的结论定位，不是“每个continuous action或每个relative电荷都为零”的定理。本章没有将432的具体Ω与那个primary map同一化，所以不能用此句使已付Ω消失；同样不能把secondary invariants存在的框架当成已选出物理source与正确regulator。

## 5. 付／未付与本门停止

| 责任 | 本章能消费的内容 | 当前仍未付 |
|---|---|---|
| 已有对象的运输 | smooth／K-oriented／proper correspondence到KK、GRR的characteristic兼容；general-position复合及非横截Tor责任；algebraic/topological relative comparison的方向 | 本项目实际r↦algebraic/perfect kernel，及其transpose／degree／连续completion和relations；不存在可直接应用的新physical输入 |
| 405与537 | 可作为未来具体map的检验职责；583和573提供已付负／非零对照 | 章节没有给任意全S_exp源map，故本门既未通过这些关系门，也未据此证明所有新map失败；不能拿compact构造代全部noncompact Pan |
| 整性与有效性 | 原cycles可带整数multiplicities；K0及virtual correspondences合法存在 | K0差类不保证effective／nef／primitive；Chern／Todd的有理分量不自动给整数sections、tensor乘法、normal vanishing或metric容量 |
| mixed RR／符号 | GRR与composition是匹配映射后的结构兼容 | 不给同一算术整对象上small-section log#、mixed交数正号、Rosati/Hodge或正确两degree端点；不是Qζ的Hermitian身份 |
| 完整经典预算与原norm | 本章不以删项改变目标 | 完整Γ/contact、properpowers、双pole、ALLcomplex源及原du／zero-extension Dlog、强源／height尾均仍待实际比较；不能以generalized GRR支付数值误差 |

本门的实际净值是修正或冻结若干会误导后续消费的方向、degree和functor假设，并确认§6提供的是**给定对应的兼容组织**，没有现成的逆向有效算术source／primitive输入。本章的literal漏洞只收紧本次可消费范围，不是证明KK／motivic路线不可能；derived/perfect kernel、真正secondary／relative对象和不同metric路线仍合法，但当前章没有给本项目所缺的具体箭头。

按已冻结停止条件，建议root将本章作为**来源0结束**：不建C047、不作584，不读§7、不追引文／future paper，不把本轮角色澄清计成新的经典正性或方法类严格边界。C046／583的一数学轮不重计，单cadence保持；strongest-old542＋555→557 whole leading4/5仍是负惯性UPPER，actualq/core/coupling/Ξ与独立primitive mixedRR主瓶颈未改变。下一数学合同仍必须有可应用的新input/test/net consequence；本稿不另设下一行动权威。
