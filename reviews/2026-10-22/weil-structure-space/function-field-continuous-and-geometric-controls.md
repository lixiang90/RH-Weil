# Weil结构空间的函数域、连续正反例与几何来源控制

2026-10-22；独占分支稿。输入为001、290、563、567、574–575及本轮primary-source核读。本文不改STATE、Goal或cadence，不宣称经典ζ的目标纤维已有点。以下是结构空间路线的验收控制与来源区分，不是新RH定理。

## 1. 应取目标数据上的纤维，不是只问某个总空间非空

先固定输入包

\[
\mathfrak d=(P,\Pi,M,\mathcal A,\mathrm{pole},c,w,
\mathcal F,\mathcal P,\|\cdot\|_{du},\|\cdot\|_{D\log}).
\]

这里Π保全部prime powers；完成化、archimedean finite-part/contact、极点缺陷与预定分次权先指定，不能随正性需要改变。一般双对象还须指定对偶函子及相互比较，而不是只写自对偶。经典输入为物理r=e^{u/2}f、完整405关系P_c、537非根及575§8的完整Qζ。只固定裸P而不固定这些规范会重开565已排的B(s)/分次虚消自由度。

把所有目标的结构组成总群胚\(\mathscr W\to\mathscr D\)是合法组织；所需命题是**经典目标纤维**\(\mathscr W_{\mathfrak d_\zeta}\ne\varnothing\)。函数域给另一个纤维有点，或连续正段给无穷多个点，不能支付此命题。若不保marking，甚至可以把一个固定正对象复制给所有目标，却没有恢复任何目标trace。

建议区分四层，不混称“已得到Weil结构”：

1. **弱比较层**：实际ringed/semiringed/对应载体、duality、degree、trace、source map及关系同构；不预先给primitive正号。
2. **有限Gram证书层**：每个有限测试族有同源矩阵及可核正半定分解；必须说明只是一族有限集合，还是所有有限族。
3. **正极化层**：完整primitive配对正，且同一源mixed配对精确等于完整Weil型；或由独立设施推得这种性质。
4. **几何来源层**：正号由有效截面、乘法、proper容量、RR二次项/ample Rosati等独立结构给出；该层不是“任意有正内积的线丛”。

第三层的非空在最低GNS自由度下就是完整Weil正性存在性重述。第四层更强，必须有实际构造或新的存在性定理；不能把“自然”二字作为可证明性公理。第四层也不应只准普通scheme，否则已知连续正例被定义排掉，无法声称覆盖最一般g系统。

## 2. 函数域：有点的几何实例及独立箭头

对真实光滑射影几何连通曲线C/Fq，取C×C上的除子、实际线丛及其截面、两个fiber类F1/F2、Frobenius图Γn和transpose/复合。这是由曲线方程和射影几何指定的弱载体；不以零点为base，也不以Q值选线。

567§§2–3已恢复其关键独立箭头：proper性使H0有限；有效截面能相乘；surface RR和Serre对偶给n²D²/2的二次增长。如果D与ample fiber和正交而D²>0，±nD的RR下界和截面乘法把越来越大的空间注入固定H0(2K)，矛盾。由此先取得Hodge负号，再用同一图交数身份把它运输为全部源的Weil正性。这里“同一对象、相同mixed系数、所有n”的要求不可删。

已知具体有点实例可用E/F5: y²=x³+x+1。直接点数N1=9、有理性和genus-one FE给P(T)=1+3T+5T²；563§5的精确矩阵

\[
A=\begin{pmatrix}0&-5\\1&-3\end{pmatrix},\quad
H=\begin{pmatrix}1&-3/2\\-3/2&5\end{pmatrix},\quad
A^THA=5H,\quad\det H=11/4>0
\]

为此纤维的有限能量证书，不需要先读根。对全部compact complex源，L=log5、U=A/√5、\(B_y=\sum_jr(y+jL)U^j\)给

\[
Q_E(r)=L\int_0^L\mathrm{Tr}(B_yB_y^{*_H})\,dy\ge0.
\]

这里全部周期副本、原点质量和周期极点已由完整trace身份保留；不能仅取一个fundamental strip的零点。矩阵证书是已知函数域资产的精确实例，几何层的有点性来自实际曲线，不把复矩阵代替其DVR、有效性或源关系。

若要额外测试Picard移动，可使用已结算的genus2曲线y²=x⁵−x+1/F5及L0=O(P+Q−2∞)，P=(0,1)、Q=(1,1)。其degree-zero线真实非平凡，h0(K)=2而h0(K⊗L0)=1。它说明Picard移动、截面lift与base change确有同一对象的实现；它没有自动提供经典物理源到该Picard族的map。

## 3. 裸Weil cohomology与正极化必须分开

已有术语可以帮助精确定义，但不能代替本轮存在性。

- Weil cohomology的有限分次、PD、Künneth与cycle map给trace和函数方程；RH仍须增加正性机制。特别不能声称“既有ℓ-adic cohomology，因此已知一般代数cycle的标准Hodge正性”。Deligne的纯性证明也不是一般标准猜想的证明。
- 不宜把整个函数域几何宇宙规定成R-valued有限维Weil cohomology：超奇异椭圆曲线的endomorphism quaternion给真实的系数障碍。可在Qℓ/晶体系数或抽象motive范畴先做几何，再在适当实现与对应代数上讨论正号；这个障碍不禁止单个曲线的复能量证书。

这两点核[Milne，pRH §§2–3，尤其2.2](https://www.jmilne.org/math/xnotes/pRH.pdf)。本轮仅消费这些指定范围，不把所有高维对象装进001的带F相容J的PLF定义。

Tannakian文献已有technical **Weil form**：由非退化形式给adjoint，且对每个非零endomorphism u有Tr(uu†)>0；polarization还要求不同对象间的tensor、dual和compatibility。既已给一个Weil form，同parity的相容forms可由相应totally-positive symmetric automorphisms参数化。此分类以初始正form为前件；不会证明任意带对偶范畴都存在它。核[Deligne–Milne，Tannakian Categories §4，尤其4.5–4.6](https://www.jmilne.org/math/xnotes/tc.pdf)。无限维g系统若不在rigid有限维Tannakian范围内，必须另定trace、domain和完成化，不能直接套用该分类。

Deligne原证明的另一来源不是先猜全局正Hilbert形式，而是全tensor阶的局部迹、monodromy和全局cohomological极点控制，再由估计推出weight；见[Weil I §§3、6–7](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)。因此可以保留“tensor-可实现性＋全局pole预算”作为几何存在性证书的另一种形态；仅偶次幂系数非负仍不够。

## 4. 连续正反例精确校验四层

取562已付positive P/Π/M的真实连续族

\[
Z_c(s)=1+\frac{c}{s(s-1)},\qquad d=c-1/4=\pm1/16.
\]

其自然完成化在本模型中已指定为Γ=0、双pole=0/1；完整源满足W''+dW=0、W(0)=2、W'(0)=0。两段都有正的原始分布、精确对偶、正式对应复合与trace，故通过相应弱解析/形式对应层；这不等于已构造实际adelic几何。

正段有563的独立有限证书C=[[0,1],[-d,0]]、G=diag(d,1)>0、v=√2(0,1)；C*G+GC=0，完整W由ODE唯一性恢复，故得到全部Gram正性。它通过有限能量/正极化层。它未因此取得proper曲面的sections/RR或整值DVR，所以对于**指定的scheme型几何子层**，结论是未构造，而不是自动通过。

负段W(u)=2cosh(u/4)。任意h>0即有

\[
\det\begin{pmatrix}2&W(h)\\W(h)&2\end{pmatrix}
=-4\sinh^2(h/4)<0.
\]

可用567§4的平滑差源给严格负Q，不依赖delta测试。因此它被完整正极化层排除，也被任何具有正确mixed身份的独立正RR层排除。负段仍可添与正段普通复代数同构的R_d[[t]]，有同样有限jets维数、Cartier参数与正纤维metric；差别是†与trace的相容符号。故这类局部设施不能作为正极化空间的充分membership条件。

| 固定目标纤维 | 弱对偶/正式trace | 所有有限Gram PSD | 独立能量证书 | 实际proper/RR几何实例 |
|---|---|---|---|---|
| 连续d=+1/16 | 是 | 是 | 563显式G | 尚未构造，不能强迫有普通曲线 |
| 连续d=−1/16 | 是 | 否，2×2即拒 | 不可能与完整身份同存 | 正RR子层须空；裸几何装饰可有 |
| 真C/Fq | 是 | 是 | 可由几何/已核实例取得 | 是，真实C×C |
| 290正整数Euler模型 | 是，含正式PD/HL | 否 | 无相容正权1极化 | 不能是相应真实曲线 |
| 经典ζ | 完整公式/旧源商已付 | fixed537窗已付；全成长未知 | 未独立取得 | 当前575不足 |

注意“所有有限Gram PSD”已等价于完整Q≥0；将其列入空间定义便使该层非空变成RH强度的存在性问题。它能作无歧义验收，但不是由弱层非空自动升级。

还应保留端点Jordan控制。设q>0，a实，\(F_a=\left(\begin{smallmatrix}0&-q\\1&a\end{smallmatrix}\right)\)、\(H_a=\left(\begin{smallmatrix}1&a/2\\a/2&q\end{smallmatrix}\right)\)，则全a精确有\(F_a^TH_aF_a=qH_a\)，而H_a>0恰为a²<4q。端点a²=4q的给定companion realization有非平凡Jordan块，不能保持正定内积；其特征根仍都在模√q圆上。故“给定realization存在正定similitude”严格强于只问该行列式的RH：半单化可有正metric。只读target zeta不能免费决定Jordan/分次虚消，这归565既有责任。模空间若要求非退化极化，必须说明是在固定实际realization上，还是允许半单化，并证明后者不损失source/trace/norm。

## 5. 575应被哪条结构条件拒绝

574–575的实际cover不是伪对象：有真实非平凡clutch线、Cartier理想和smooth-flat有效代表。不能把旧失败粗写成“没有任何线丛或regular结构”。但是以下具体门必须在结构空间中留下：

1. **源覆盖**：g_r=exp(∫_-∞^x r)对所有物理源都是保双frames的unit。它确实消405全P_c，却也消537非根，故不能作为具有537完整trace比较的source marking。若结构完全忘掉source mark，则它仍是合法弱对象，不能再从其存在推目标正性。
2. **分离过滤**：continuous边界J=J²，指定(ρ)的商无限长度；smooth normal过滤有非零flat交。若公理要求曲线式有限长度、分离消失过滤，这个选定层明确不通过。若允许filtered-regularized/derived修复，须明确新过滤、消失长度和误差，不能只改名称。
3. **容量**：bulk固定窗已有无限维compact截面，局部unit metric不提供proper有限容量。若允许无限容量C_j，必须按567§7证明其相对于n_j²的预算、全部RR误差及与Q的η_j趋零，而不是要求C_j一定有界。
4. **原费**：575 primitive的fixed source窗C0 du/Dlog upper已付；完整regular代表还需额外derivative费。一个新空间若把原费写为自动“连续”，不能把这一费用抹去。成长source窗、cover窗和capacity cutoff须分别量化。

完整Γ/contact、所有p^k、双pole和allcomplex mixed比较是target marking，不宜只是事后另附等式。一旦只恢复删Γ或删pole的预算，所得点在另一个目标纤维。

## 6. deformation、紧致性与obstruction能做什么

**有意义的deformation任务**是先固定弱载体、关系和局部数据，研究其正极化子空间的提升；不是用总空间一条path把函数域正性传到经典。

连续c族已给最便宜反控制：d=0处正能量G退化；d<0时出现上述有限Gram障碍。总族连通，弱对象始终存在，正子空间仍可在边界停止。非退化strict-positive锥通常不闭，半正锥虽闭却可能丢faithfulness、普通trace重数或537覆盖。因此不能仅说“正性锥闭＋经典是极限”就完成存在性；需实际同目标收敛且所有身份、重数、domain及原费稳定。

正分布锥的闭性仍是合法路线：若独立几何构造的完整W_j逐分布趋于Wζ，则每个r的\(W_j(r*r^*)\ge0\)传到\(Q_\zeta(r)\ge0\)。不要求原几何载体在某个naive Pic空间有compact极限，也不要求每个极限realization保持非退化。这里未付的是这样的**同源逼近**及其完整Γ/全部prime powers/双pole/contact身份；若还要产生物理源的几何lift，则原du/Dlog运输另需证明。等价存在性可以被独立方法证明，并非逻辑上因其等价就自动循环；循环发生在用尚未证明的目标正性建立逼近或极化。

**紧致性**可在事先给定的有界模型中把相容有限资料粘成点。例如固定维数矩阵、上界与归一化，闭多项式约束及PSD形成compact候选；若每有限组约束都有共同解且有限交性质成立，则有全解。但是每个finite-Gram块的正确PSD可行性本身已经是该块Weil正性，正反例中的2×2障碍不会被紧致性消掉。

更强几何层的难点是：Cartier regular性、nonzero-divisor、非退化source覆盖、effective乘法单射、同源RR误差等不全是一个现成compact闭条件；平坦性/base change不是正极化的替代。无限维时还需固定拓扑/trace类、紧致性或coercivity的实际upper、共尾source域和Gamma紫外误差。纯first-order compactness至多给形式/可能非Archimedean模型，不能免费得到原实分析的domain和估计。

**obstruction的正确职责**是将拒绝点定位到某个有限可核门：405不保持、537被杀、某finite mixed Gram负、过滤不分离、capacity超预算或Γ contact缺失。有限Gram负能证明正纤维空，却不能在正例中制造RR几何。当前实际ζ已有fixed窗正资产，但尚无全成长正纤维的独立compact候选与有界提升定理。

## 7. 给root的消费建议

用户的“先定结构再问存在性”可以采用，且比继续拼scalar标签更适合组织必要设施；但应把下一任务写成一个**带固定target marking的弱几何模空间及其正子问题**。

本轮可交付的是清楚的分层定义、非空真函数域实例、连续±与575的精确拒绝门、以及紧致性所需的有限joint-feasibility/原费清单。不能把这些设计本身报为新的经典容量输入。真正改变瓶颈的下一原件应给：一个尚未靠Q或zero coordinates命名的候选族；405同构/537可见/原norm运输；一个独立effective-RR或tensor-pole定理；以及恢复完整Weil预算的同对象比较。任一项缺失，目标纤维非空仍是待证命题。
