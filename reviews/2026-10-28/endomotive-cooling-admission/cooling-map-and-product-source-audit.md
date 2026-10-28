# CCM cooling：实际π／Trace／cyclic coker与两源产品的来源类型审

2026-10-28；`/root/rational_first_gate`当前独占source任务，非Gaussian／poly旧任务续算。已恢复README／STATE、check→show、AU／同G20261027／原0c4f及当前gate。最初check因pending字段报结构错误，root随后修正，本稿末次check已PASS；本稿没有改共享STATE。使用PDF技能，实际逐文及逐页图核固定v2 **PDF22–29完整页**，再按root追加页边界勘误只核**PDF30在§4.4标题之前的Def4.13／Remark4.14前缀**。未读§4.4正文、§5／§6／§7或引用串；没有web／下载／数值／新数学／Git／cadence操作。

**来源类型结论：实际cooling algebra map、partial-trace cyclic morphism及distilled Λ-module的coker均已准确定位；本范围没有给该coker的内部乘法／正Hermitian两源型、trace-image为理想或同一非零primitive的物理源映射。** 原文确有多输入trace公式，不能误报“没有双输入”；它们是cyclic chain态射的分量，不能免费变成商上的mixed交数。当前按限定来源0止，不判整个endomotive／higher路线失败，不授后章或数学合同。

## 1. 原件、旧页重叠和本次精确边界

固定原件为Connes–Consani–Marcolli，*Noncommutative geometry and motives: the thermodynamics of endomotives*，arXiv math/0512138v2，2007-03-10；本地
`literature/f1/ccm-endomotives-math-0512138v2.pdf`，58页／747528 bytes，原SHA256
`68f9c8eaa5e9b46790e5adad0e8cd910da43566e7bc339ea5ecc81ab1f3fe601`，现场重核一致。

仅读[root gate](root-source-gate.md)、[当前old-scope稿](old-scope-and-type-test.md)及上述PDF窗口。408已读23–24／26／29等内页不能被“以前只看首页”替代；其topological tensor／continuous dual／closed-image coker资产保留。本次新核的是这些实际π／δ与产品下降的类型责任，不重验收全篇拓扑完成或谱实现。

PDF29页尾实际止Prop4.12／(4.31)，未有D的Definition。root据此明确补准PDF30的§4.4前缀，本稿只读缓存`page-30-before-4.4.txt/.png`。root gate另如实记其首轮crop错误曾意外暴露整p30含4.4开头；该暴露已隔离，不在本稿证明范围，不能写成root完全未见4.4。**本稿自身没有读取full page-30.png或4.4正文。** PDF30前缀也不能补齐p29所引(5.1)或Lemma4.9延后的证明。

## 2. π：上游确是代数表示，不是physical→primitive映射

**PDF22–23，Lemma4.3及(4.4)–(4.8)。** 先有(A,ϕ)、保持A的modular action σ_t及低温regular extremal type-I∞ KMS_β态ε。原文在该前提下给irreducible π_ε、H及trace-class e^(−βH)，满足

\[
 \epsilon(a)=\frac{\operatorname{Tr}(\pi_\epsilon(a)e^{-\beta H})}
                        {\operatorname{Tr}(e^{-\beta H})},\quad
 e^{itH}\pi_\epsilon(a)e^{-itH}=\pi_\epsilon(\sigma_t(a)).
\]

H只确定到加常数。π扩成crossed-product表示

\[
 \pi_{\epsilon,H}\!\left(\int x(t)U_tdt\right)
       =\int\pi_\epsilon(x(t))e^{itH}dt.                 \tag{P}
\]

这是真实operator／algebra层。KMS式(4.3)也确有两个上游代数元素的correlation，但没有把它认证为distilled商上的配对或项目physical源的mixed型。

**PDF23–24，(4.9)–(4.18)。** 精确domain为

\[
 \widehat A=S(\mathbb R,A)=\bigcup_{V\subset A,\ \dim V<\infty}
 S(\mathbb R,V),\qquad
 (x\star y)(s)=\int x(t)\sigma_t(y(s-t))dt.
\]

不是任意Banach完成或项目原L²(du)。`Â_β`取x在I_β={0≤Im z≤β}解析、两边界为Schwartz的S(I_β,A)所给元素；原文给它的subalgebra资格。对偶作用为`θ_λ(∫x(t)U_tdt)=∫λ^(it)x(t)U_tdt`，把H送成H+logλ。参数空间Ω̃_β是(ε,H)的principal R⁺* bundle，按Tr(e^(−βH))=1有自然截面。

Prop4.4给各π_(ε,H) inequivalent irreducible、equivariance及`π_(ε,H)(Â_β)⊂L¹(H(ε))`。trace-class准入不是mere“算子有trace”标签：scalar x的`g(s)=∫x(t)e^(its)dt`满足g与e^(βs)g均Schwartz，原thermal trace使g(H)为trace class；general A-valued情形在谱投影上同样控制。

**PDF25–26，(4.22)–(4.25)，Cor4.6。** 原文需共同可分Hilbert空间内的continuous lifting，尤其(4.23)在trace-class范数中的连续性，才给

\[
 \pi:\widehat A_\beta\longrightarrow
 C(\widetilde\Omega_\beta,\mathcal L^1),\qquad
 \pi(x)(\epsilon,H)=\pi_{\epsilon,H}(x).               \tag{C}
\]

这是R⁺*等变cooling morphism，保(P)的代数表示；不能把所需lifting当所有system自动已有。BC在β>1时representations独立β，p26声称其continuity可直接核，Ω_β=E_β为compact且各representation用同一Hilbert空间。`Prim Â`在这里是C* primitive-ideal space，不是项目所需Hodge／Lefschetz primitive对象。

## 3. Trace与δ：确有实际多输入，但类型为cyclic morphism

**PDF26，Prop4.7。** 对unital B及trace-class operators，实际公式是

\[
 (B\otimes\mathcal L^1)^\natural\longrightarrow B^\natural,
\quad
 (b_0\otimes T_0)\otimes\cdots\otimes(b_n\otimes T_n)
 \longmapsto
 (b_0\otimes\cdots\otimes b_n)\operatorname{Tr}(T_0\cdots T_n).
                                                               \tag{T}
\]

原文逐一核faces、degeneracies、cyclic permutation；尤其末face／循环置换使用trace循环性。degree1确有Tr(T₀T₁)这一个真实双输入式。**所证是Λ-module态射，不是Trace为algebra homomorphism，也不是余核内部的双线性乘法。** 不用generic 2×2反例代替这里实际类型判断。

**PDF27。** 非unital A用unitization后augmentation kernel定义A^natural；另给essential-ideal compactification的(A,A^comp)^natural及canonical cyclic map。adjoint unit不在L¹，故Prop4.7是通过unitized相对循环模构造的；不能直接在非unital L¹里随意插unit，也不把这些对象等同本项目canonical inclusion-cone。

在共同H的lifting下，(T)应用到B=C(Ω̃_β)，对合法elementary cyclic tensors可把其分量读成

\[
 \delta_n(x_0\otimes\cdots\otimes x_n)(z_0,\ldots,z_n)
 =\operatorname{Tr}\bigl(\pi_{z_0}(x_0)\cdots\pi_{z_n}(x_n)\bigr),
 \quad z_j=(\epsilon_j,H_j).                           \tag{D_n}
\]

unitized项按原相对构造解释。main diagonal z₀=⋯=z_n上是同一representation中operator product的trace；不是两个distilled classes的现成交数。所见多输入image仍属于即将被余核除去的relations。

**PDF27–29，(4.26)–(4.31)。** scalar元的BC位置特别具体：SpecH={log n:n≥1}，于是

\[
 F_x(c):=\operatorname{Tr}(\pi_{\epsilon,H+c}(x))
       =\sum_{n\ge1}g(\log n+c)
\]

（scalar x及其g如上）。Lemma4.8的c→+∞ trace衰减在窗口内有证明。Lemma4.9声明BC对general x∈Â_β有

\[
 F_x(c)=e^{-c}\tau(x)+O(|c|^{-N}),\quad c\to-\infty,\ \forall N,
                                                               \tag{4.26}
\]

并明确将证明放在Lemma4.17后；**本次没有读取那个证明**。不能把页28的scalar Poisson动机当该general lemma已独立证明。后续Cor4.11及Prop4.12在本稿按其明示(4.26)前提消费。

当τ(x)=0，Cor4.11给FTraceπ(x)∈C(Ω_β,S(I_β))。改用λ=e^c，(4.30)定义`S_β(R⁺*)=∩_(α∈[0,β]) μ^(−α)S(R⁺*)`，μ(λ)=λ。S^natural(Ω̃_β)是C(Ω̃_β)^natural中沿main diagonal具有C(Ω_β,S_β)衰减的cyclic submodule。Prop4.12原式为

\[
 \delta:\widehat A_{\beta,0}^{\natural}
          \longrightarrow S^{\natural}(\widetilde\Omega_\beta).
                                                               \tag{4.31}
\]

**下标0在该页明确指向未读(5.1)。** Cor4.11确实处理degree0的x∈Â_β∩Kerτ，但本稿没有据此把所有degrees的0-submodule替换成“tensor逐项在Kerτ”，也不能自行认定任意compact physical r均在δ的完整合法domain。

## 4. D的coker／closure及一般情形：有商，不自动有商代数

**授权PDF30前缀Def4.13：** `D(A,ϕ)`被定义为cyclic morphism δ的cokernel。该定义行本身没有image已闭的证明或closure横线。

结合当前old-scope已恢复的全篇topological coker约定，可在各degree记

\[
 D_n=S_n^{\natural}(\widetilde\Omega_\beta)/N_n,
 \qquad N_n=\overline{\operatorname{Ran}\delta_n},       \tag{Q}
\]

closure在原给定topological cyclic-module目标中取。这里“closed-image quotient”不等于Ranδ_n自身已闭，也不指定一个未给的Banach／Hilbert tensor norm。(Q)使用的是408已核全篇约定与本次Def4.13的结合，不能说closure字样就印在本定义行。

**Remark4.14。** 无共同H lifting时，改用Ω̃_β上的continuous field C_(ε,H)及section algebraC(Ω̃_β,C)。Dixmier–Douady障碍可使之不能Morita等价到scalar函数；原式(4.32)仍给R⁺*等变algebra homomorphism`π:Â_β→C(Ω̃_β,C)`。coker／cyclic cohomology可继续讨论，且general pair的(4.26)通常不成立，须逐情形分析。此处未为一般system补出同一个scalar目标或BC衰减定理。

末段还给rough general definition：把上述S替换为**Traceπ(Kerτ)生成的subalgebra**。这确实提供ambient algebra的生成描述，不能遗漏；但“由image生成一个subalgebra”并不等于“image是该代数的双侧ideal”，更不证明degreewise closed relations在某two-source运算下稳定。该段没有给imageideal或quotient-product下降定理。

## 5. 外部convolution作用已给；内部mixed／非零source没有免费得到

PDF28–29 Lemma4.10定义Hol(I_β)为S(I_β)的multiplier algebra。令分布ĥ满足`∫ĥ(λ)λ^(it)d*λ=h(t)`，则

\[
 \theta(\widehat h)x=\int\widehat h(\lambda)\theta_\lambda(x)d^*\lambda,
 \quad x(t)\mapsto h(t)x(t).
\]

equivariance使target fiber函数作logλ平移的积分；其c-Fourier变换为

\[
 F(g_\epsilon)(u)=h(u)F(f_\epsilon)(u).
\]

这证明FTraceπ是**外部Hol(I_β)-module map**，其image稳定于给定external multipliers。它不是target函数逐点相乘后仍在trace image的定理；也不是D×D内部产品、D与continuous dual的正Hermitian识别或mixed RR。Λ-module的相邻tensor multiplication／cyclic faces同样不等于新增两个商类的乘法。

若欲把D当内部产品载体，当前type-test仍需在实际操作`B~:S_j×S_k→S_l`上证明`B~(N_j,S_k)⊂N_l`及`B~(S_j,N_k)⊂N_l`，并付closure所需连续性。本窗口没有这样的命题。本稿没有反证这些包含式、没有证明image非ideal，更不以trace一般不乘法泛判实际BC失败。

余核tautology须另说清楚：**凡合法x_r∈domain δ₀，若将physical源定义成`q_r=[δ₀(x_r)]∈D₀`，则q_r=0，连未取closure时也如此。** 两输入若只取δ₁(x_r⊗x_s)的class也一样是image relation。这里止的是source-through-image读法；不是D=0、全部HC=0或CCM路线失败。此事实不借canonical C*ideal exact0，也没给两种商的比较同构。

项目physical源可形式代入原scalar公式：设`g_r(u)=e^(−u/2)r(u)`、`x_r(t)=(2π)^−1∫g_r(u)e^(−itu)du`，则其scalartrace是`Σ_n g_r(logn+c)`。这是将项目物理normalization放到原(P)的候选输入位置，**不是本章交付的非零D-source**；凡其满足未完全核定的0-domain条件，上述class恰为0。不能仅凭compact r的strip资格就宣称全部r有τ／所有degree的合法性，亦未核405全部noncompact关系、537非根保留或原du／zero-extension Dlog的商范数费。

至多一个可供以后另准的actual首检是：在BC、某fixed β>1，取满足δ₀-domain的scalar x_r，记`F_r(c)=Σ_n g_r(logn+c)`，并用另一独立compact physical s的`b_s(c)=e^(−c/2)s(c)`作target probe，检验

\[
 F_r(c)\overline{b_s(c)}\ \stackrel{?}{\in}\ N_0.      \tag{Test}
\]

这是原trace relation与实际target pointwise multiplication的一个窄理想稳定性test，第一槽linear、第二conjugate。**本稿未执行(Test)、未找反例／证明、未准其数学预算。** 即使该probe族通过，也不能免费补全所有target／closure／higher-degree产品或完整physical coverage；若只把F_r自身作为商source，前述tautology已经先止。没有第二candidate或后章队列。

## 6. 净来源结论与保存范围

本次实际恢复了π、Tr、δ、D各自domain／range、degree、topology及BC scalar source位置：上游algebra product存在、cyclic多输入trace存在、coker定义存在、external multiplier action存在。**本窗口未给同一非零primitive的physical源与内部mixed下降／正号的新输入**，也未给其完整Γ／FP-contact、全部Λ(p^k)=logp、双pole及原物理norm的运输。BC后续zero-spectrum／HC₀／character／positivity不在本门消费；p29的后文展望不是已读定理。源门0止，不因此否定不同actual relative／derived／有费机制。

old-scope所载405／Meyer谱module及closure资产先扣，本稿未复读其章；canonical cone与10-27 ordinary-cycle／Todd冻结也未被搬作此D的普遍反证。无新数学／C053／590／formal18；cadence3/history53/latest589/formal17保持，whole4/5UPPER与principal／primitive／mixed／signed-core／Ξ瓶颈未改，Goal门open。root／fresh仍须按实际终稿另消费，本稿不代结算。

版本绑定：root gate含页边界及crop勘误，4808 bytes／LF SHA `0f0a393ba35de4e6090c907fad8d1577b0de15a2b3bba02be46b7d23cba4c3ee`；old-scope终稿10046 bytes／LF SHA `7ffb2e3cffe957d7246d6c72f9abf1ea2daa6b711a1b17503e056781f19c7054`。授权p30 prefix文本1660 bytes／raw SHA `ab9b695f0e019e4be970e6c3250e2a72b28e1dc24e9a5324c5053196fc77bd57`。原PDF及22–29／30prefix文本／页图均只在ignored本地库；本稿无复制后章正文或第三方全文到公开工作树。
