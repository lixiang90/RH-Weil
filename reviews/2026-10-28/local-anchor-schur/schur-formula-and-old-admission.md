# Fixed-anchor T-Schur正form：实际公式、旧覆盖与唯一首门

2026-10-28；`/root/rational_first_gate` 当前独占准入稿。已恢复 README／STATE、check→show、同G20261027／runtime1793085111／原0c4f、AG、frontier／summary及已耗尽C050。587已结算一轮，cadence1/history51/latest587/formal17；本稿不是继续degree／rank或log优化，不预C051／588，不改STATE／Git／cadence，不web／新增source。本稿只审这份已给actual正form及固定test，未证明下列moving-source关键lemma。

**裁决：有限T-Gram Schur族实际可定义、非空且为全complex正form；不是按未知K反定义的谱截断。537付的是原du coercivity。旧553和587的已印定理不能直接决定所要求的fixed-anchor／growing-range test。** 可具体冻结的唯一证明首门是下文(L)及其在同一fixed平移源上的消费；成功只排共同fixed-anchor的这类正分解，不能泛排成长rank／无限秩或所有正form逼近。若root恢复更强旧链已直接给(L)，则按强旧消费0止，不以新名称重复计功。

## 1. 已付anchor及实际源projection

anchor固定为 `I₀=(−17/16,17/16)`。核[537 §2 (1)](../../../notes/537-source-exact-weil-window-positive-tail-admission.md)，其实际陈述是

\[
 Q_W[q]\ge\kappa\|q\|_{L^2(du)}^2,\qquad
 \kappa=2^{-49162},\quad
 \forall q\in C_c^\infty(I_0;\mathbb C).
 \tag{1}
\]

这里是Lebesgue／physical du norm，**不是仅有Dlog下界**。全complex、odd负pole、原Γ/FP-contact及所有可见properpowers都在原定理内；本稿不重新验收其正性。对于另行声称合法的infinite anchor range，必须使Q及(1)在其实际form domain上合法延拓；不能从“支持在I₀”单独给任意L²向量定义Q。

令r₀为[587 §1](../../../notes/587-actual-sonin-moment-spread-and-growing-source-rank-necessity.md)的literal bump：`c exp[−1/(1−u²)]` 于|u|<1、外零，du norm1。置

\[
 m_X=\lfloor\log X\rfloor,\qquad
 E_X=\operatorname{span}_{\mathbb C}\{e_0,\ldots,e_{m_X}\},\quad
 e_j=r_0^{(j)}.
\]

每个finite-X的E_X均由真实smooth compact physical源组成，support⊂[−1,1]⊂I₀。此处允许源rank成长，不把587的每先fixed d估计外推为d_X=m_X的uniform估计。

保560／585同一个

\[
 T_X[r,s]=\operatorname{Tr}(A_r\Pi_XA_s^*)
 =\int\widehat r(t)\overline{\widehat s(t)}\rho_X(t)dt.
\]

第一槽线性、第二槽共轭。有限X的ordinary trace／HS域与完整Gram inverse／returns均已付；ρ_X没有重新归一化。它对compact非零源严格正：固定X的高频ρ_X与原正log阶相当，而非零compact源Fourier entire不能在一个实区间恒零。e_j亦线性独立，因Fourier侧是非零F₀乘各阶(it)^j。因此E_X的T-Gram可逆；不依赖587对growing m的下界。

为避免共轭槽混用，定义

\[
 H_{X,jk}=T_X[e_k,e_j],\quad b_{X,j}(r)=T_X[r,e_j],\qquad
 \boxed{P_Xr=\sum_{k=0}^{m_X}e_k\,(H_X^{-1}b_X(r))_k.}
 \tag{2}
\]

H_X为正定Hermitian矩阵，(2)为complex-linear源projection，满足 `T_X[r−P_Xr,e_j]=0`。这是 **T-orthogonal source projection**，不是receiver空间Π_X的子projection，不省H_X⁻¹，也不以普通du投影替代。

对每个fixed源窗J，560给finite-X的 `T_X[r]≤C_(X,J)||r||²_Dlog`。在finite E_X，Q/T的最大Rayleigh quotient有限，故(2)及下列W在同一local Dlog domain连续，常数可依X／m_X。这里没有任何global／cofinal统一du或Dlog界，Gram条件数与各阶源费也不免费。

## 2. 正form及准确的匹配范围

冻结题定公式

\[
 \boxed{W_X[r,s]=T_X[(I-P_X)r,(I-P_X)s]
                    +Q_W[P_Xr,P_Xs].}\tag{3}
\]

全部compact smooth complex源都可代入；两项各非负，所以W_X为Hermitian PSD form。`W_X[e,f]=Q_W[e,f]` 对e,f∈E_X **exact**，因为P_X在E_X上为identity。有限E_X时不能说已经在整个 `C_c∞(I₀)` 上匹配Q；也没有由m_X→∞自动得到anchor全部源的收敛。

T-orthogonality还给实际有限式 `W_X=T_X−T_X(P_X·,P_X·)+Q_W(P_X·,P_X·)`。这是定义后可核的恒等式；规则只用actual T、anchor上的完整已知Q及实际有限Gram逆，不读取全局K的spectral截断或按所需全局Q补残差。

本任务准确目标是 **positive FORM approximation**：至少要求每个先fixed compact complex r有 `W_X[r]→Q_W[r]`，再以复极化消费两个独立源。有限层P_X依固定位置anchor，一般未证W_X来自单变量translation-invariant分布；PSD本身不能把它叫正D′分布。若另声称某个D′读出，本节固定源form收敛仍是其必要test；本稿只检这个更弱必要条件。

## 3. 固定a=4的完整目标，不移动测试源

只用一次固定平移

\[
 r_a(u)=r_0(u-4),\qquad \operatorname{supp}r_a=[3,5].
\]

它与共同anchor闭包分离，du norm仍为1。完整Weil型准确translation-invariant：自相关、Γ/contact及全部primepowers只依源差；双pole若写 `μ_±(r)=∫e^(±u/2)r(u)du`，平移乘 `e^(±a/2)`，所以完整 `2Re(μ_+ overline μ_−)` 不变。等价地，cosh／sinh两腿作保持 `|C|²−|S|²` 的Lorentz boost，odd负号没有删除。因此

\[
 Q_W[r_a]=Q_W[r_0]\ge\kappa>0
 \quad\text{为同一个固定有限数。}\tag{4}
\]

不是a_X随X移动，不是把r_a套入537的原anchor；正号先由r₀上的已付537取得，再按完整Q的exact平移不变性运输。

令q_X=P_Xr_a。由(1)、(3)有

\[
 W_X[r_a]=T_X[r_a-q_X]+Q_W[q_X]
 \ge T_X[r_a-q_X]+\kappa\|q_X\|_{du}^2.
 \tag{5}
\]

假如某X_n→∞上W_(X_n)[r_a]有界，两项正性才分别迫 `sup_n||q_(X_n)||du<∞` 与 `sup_n T_(X_n)[r_a−q_(X_n)]<∞`。**不能只因q_X来自anchor就先称其du有界**；有限投影的norm可成长，(5)用的是待反证的bounded W。

在L²的subsequence上令q_(X_n)⇀q。q仍支持anchor闭包；`f_n=r_a−q_(X_n)` 全部支持同一fixed compact J=[−17/16,5]、du有界，且

\[
 f_n\rightharpoonup f=r_a-q\ne0.
\]

非零由disjoint supports保证，甚至 `||f||du≥||r_a||du=1`。以上只是实际弱紧性及(1)的消费，没有应用587于moving f_n。

## 4. 唯一未付lemma与最便宜首门

所需actual结论精确为

\[
 \tag{L}
 \begin{gathered}
 X_n\to\infty,\quad\operatorname{supp}f_n\subset J\text{共同fixed compact},\quad
 \sup_n\|f_n\|_{du}<\infty,\quad f_n\rightharpoonup f\ne0\\
 \Longrightarrow\quad T_{X_n}[f_n]\to+\infty,
 \end{gathered}
\]

其中每个f_n须在原T_(X_n)合法源／form domain。(L)若成立，立即与(5)的bounded subsequence矛盾，故 `W_X[r_a]→+∞`，无法趋于(4)。这是真实rule／完整有限目标的单一可判test，而不是把“所需误差小”改名new input。

587的已印结论只对fixed导数源span／先fixed degree的moving coefficients共同有效；f_n不必落在任一这样的fixed span。585仅each fixed f发散，更不足以直接作用于f_n。(L)因而不能由两句scalar／fixed-degree theorem表面引用取代。

具体可审的证明接口是587已付actual frame及Gaussian全线norm，加上共同compact support／du弱收敛对Fourier entire族的normal-family控制：若limit Fourier在0有有限零阶k，需要实际分离固定k个近0零点、给holomorphic unit在固定core的统一nonzero下界，才能把moving f_n运输到fixed-degree多项式gap。这里尚未将该接口当作已证(L)。尤其若core δ须缩小，须明确旧ALLpoly／normlemma中auxiliary c与δ的依赖，不能沿用较大δ₀下的N常数而漏tail。这些只允许作证明witness；W_X、m_X、r₀、anchor和原norm都不能因此改动。

## 5. 旧覆盖审查与成功scope

| 最强旧资产 | 本门能继承什么；不能据此直接判什么 |
|---|---|
| [553 §§1–3](../../../notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md) | 其全Pan cyclic closure会使**全域、固定finite global norm、杀全真实Pan**的energy reader退化。当前W_X无这些uniform界／逐层Pan下降前件，且正form逼近本就不要求逐层消noncompact Pan。不能凭positive completion／source-adapted标签套553。 |
| [560 §§1、4](../../../notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md) | 支付实际T域／正性／TGram／finite-X Dlog费用和full Γ/pp/pole字典；没有给共同du-bounded moving弱极限的coercivity。 |
| [585 §§1、4–5](../../../notes/585-cofinal-sonin-fixed-source-trace-lower-and-core-error-fee.md) | 支付每个先fixed源发散。不能把弱limit非零改成某个固定f后无误差地替换f_n。 |
| [587 §§1–5及proof](../../../notes/587-actual-sonin-moment-spread-and-growing-source-rank-necessity.md) | 每先fixed degree的actual coefficient-uniform gap、真实frame inverse、全线norm／tail已付；rank须→∞不排m_X=⌊logX⌋。已有更强frame设施可用于证明(L)，但已消费记录没有把任意du-bounded弱非零族列作定理。本门不继续C050的degree／rank rate。 |
| 587§5的compact-K谱截断／旧正型设施 | 保合法growing-rank逃逸非空；谱截断按K定义，与本(2)–(3)实际local rule不同。仅有PSD、局部匹配、rank成长均不证明complete Q收敛；也不直接否定本rule。 |

本稿没有找到一条可直接消费、已涵盖(L)／共同fixed-anchor强scope的旧定理；这一判断限上述必要原件，不是全库存或文献不存在结论。若另一当前proof恢复出587更强paidlemma已经直接蕴含(L)，应扣最强旧分类，不因“新Schur族”名称另计。

成功后的强scope可只写实际正分解

\[
 W_X[r]=T_X[r-q_X(r)]+Q_W[q_X(r)],\quad
 \operatorname{supp}q_X(r)\subset\overline I_0,
\]

两项均合法且Q项保(1)，residual的系数固定为1。上述fixed r_a反证不使用q为Tprojection、linear／idempotent或finite-rank；故包含本题非空finite Schur族，也覆盖合法infinite Tprojection，甚至逐源非线性选q的scalar必要test。若声称正FORM，则另须共同Hermitian两源规则；不由逐对角选择自动给它。

infinite版本只有在q_X落在明确Q-form domain、保support及coercivity、residual落在T域时才合法；不把抽象T-completion中的vector免费当physical compact源。这份coverage与费用应和(L)同根闭合。

该结论不排residual另缩放、带signed cross的完整共同修复、anchor随X移到无穷／支撑成长、不同非局部range或其它正form族。它不证明完整Weil正性、全部growing-rank方法失败或whole改善；未排的名称也不授后继。

## 6. 冻结input／test／net及停止

**Input：** (2)–(3)的actual TGram源projection与已付537 anchor du coercivity，literal587 r₀、固定m_X规则及完整Q；有限族非空，不先假设全局正号／未知K消失。

**Test：** 只审fixed a=4的r_a，支付(L)的原support／du弱量词与actual frame运输，再按(5)判W_X[r_a]是否发散。不能仅重印587 fixed-degree下界，也不能用未知completion／domination替代(L)。

**Net：** 若成功，排这个共同fixed-anchor正分解的finite／合法infinite range class，允许rank任意成长和源适应q；原因是局部正费用加固定外部源的actual残差，区别于587固定上限source-rank边界。只否定此明确positive FORM approximation机制；全量Γ/contact／properpowers／双pole一直在目标Q与anchor正性内。

**准入意见：** 具有actual formula、明确norm、fixed test及可改变此具体选择的scope，支持只冻结这一项(L)／local-anchor test的有限证明首门。若强旧已给全scope则旧0止；若(L)／domain或norm运输不闭，准确未证止，不调整anchor／a／m_X／source／norm，不预C051／588、重开C050或接source／查询／泛形成队列。准入不等于本次已取得净定理。

此稿不改变cadence1/history51/latest587/formal17，同实例长期Goal保持active/open/noteligible；whole542＋555→557 leading4/5仍只负惯性UPPER，primitive/principal/mixed及完整signed/core/Xi没有由准入完成。
