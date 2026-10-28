# 算术乘法Koszul：闭纤维、Hodge投影与源角色核验

2026-10-29；独占准入核验。**所给canonical orthonormal模型可严格闭合，无构造性断点；它是标准有限Koszul纤维的Hilbert正交和，不给新的独立算术正性。** 本稿只付闭复形／源role，cofinal全正谱极限和最强旧总判定由另一独占稿及root消费。本稿不创建C056/593，不改STATE、Goal、cadence或Git，不使用web、新文献、数值或辅助代理。

## 1. 实际Hilbert空间及有限整数纤维

令F是有限或可数素数集，固定通常prime顺序。K_F的单位正交基为e_(n,A)，n≥1，A⊂F有限，degree为|A|。代数core C_F取有限基向量线性组合；d_0及L_0按root给出的式子定义：

    d_0 e_(n,A)=Σ_(p∈A)(−1)^(position(p,A)−1)e_(pn,A\{p})，
    L_0 e_(n,A)=log(n∏_(p∈A)p)e_(n,A)。

实际乘法移位与exterior符号给d_0²=0。总整数m=n∏_(p∈A)p不变；记E_F(m)=F∩Prime(m)、r_F(m)=#E_F(m)。每个m的基恰由A⊂E_F(m)给出，n=m/∏_A p，所以

    K_F=⊕_(m≥1) K_(F,m)，K_(F,m)≅Λ C^(r_F(m))，
    dim K_(F,m)=2^(r_F(m))<∞。

此识别保持正交单位基。纤维上d_m=ι_v、d_m*=v∧，v为r个1组成的向量；CAR恒等式给

    d_m²=(d_m*)²=0，d_md_m*+d_m*d_m=r I。

r>0时||d_m||=√r；r=0时该纤维只有degree0的一维基e_(m,∅)，d_m=0。这不依未知ζ零点、任何principal命名或待求正内积。

## 2. 闭包、真实域和有界primitive

取Hilbert直和闭算子

    D(d)={x=(x_m):Σ_m||d_m x_m||²<∞}，d x=(d_mx_m)，
    D(d*)={x:Σ_m||d_m*x_m||²<∞}。

有限m截断同时在Hilbert范数及各graph范数收敛，故C_F是core，d为d_0的闭包，其Hilbert adjoint确为所写直和d_m*。若x∈D(d)，则dx∈D(d)且d(dx)=0；这支付闭Hilbert complex意义的d²=0。

在D(d)∩D(d*)上，D=d+d*为有限self-adjoint矩阵D_m的正交直和，因而self-adjoint，且

    D(D)={x:Σ_m r_F(m)||x_m||²<∞}，
    Δ=D²，D(Δ)={x:Σ_m r_F(m)²||x_m||²<∞}，
    Δx=(r_F(m)x_m)。

这里||d_mx_m||²+||d_m*x_m||²=r_F(m)||x_m||²，故D的域没有由不合法的无界项相消扩大。有限F时d、D有界；无限F时通常无界，不能把finite-F operator norm搬成统一全F范数。

令P_F为r_F(m)=0纤维的正交投影。于是kerΔ=ker d∩ker d*=RanP_F；Δ在P_F⊥上有共同gap1。定义G=Δ^(-1)(I−P_F)，即r>0处乘1/r，r=0处0。||G||≤1，G把K_F送入D(Δ)。取

    h=d*G，h_m=d_m*/r（r>0），h_m=0（r=0）。

有||h||≤1，且hK_F⊂D(d)∩D(d*)。尤其d_mh_m=r^(-1)d_md_m*为正交投影，d_m*h_m=0。**dh是全K_F上的有界算子；hd先在D(d)上定义，再有有界延拓。** 精确链同伦为

    dhx+hdx=(I−P_F)x，x∈D(d)。

若写成全Hilbert恒等式，须将hd理解为该有界延拓，不能把原未定义的无界乘积叫作全域算子。

对x∈ker d，x−P_Fx=dhx，且primitive hx有真实K_F范数费||hx||≤||x||。因此

    Ran d=ker d∩P_F⊥，Ran d*=(ker d)⊥，
    K_F=RanP_F ⊕ Ran d ⊕ Ran d*。

两range均闭。于是本模型的ordinary Hilbert cohomology与reduced cohomology相同，不存在靠取不闭像恢复的隐藏Hilbert同调；这项结论只针对本canonical Hilbert闭包，未推广到其它源Fréchet完成。

## 3. 有限F的H0、共同识别与cofinal支持

准确同调为

    H_0(d)≅span闭包{e_(n,∅):p∤n对所有p∈F}，
    H_q(d)=0（q≥1）。

有限F作用在**完整整数carrier**上，H0含全部F-coprime整数，并非只留vacuum。例如F={2,3}仍有n=5、25等harmonic基。F包含全部prime时，H0才是C e_(1,∅)。若F遗漏一个prime，则它的所有powers已经给无限维H0。

不同F的K_F不相同，强收敛必须先识别。可在共同degree0空间ℓ²(N)上，把P_F看成对F-coprime整数的对角投影；或在K_all中对所有非零exterior标签补0。这两种识别一致。若F_j cofinal覆盖每个finiteprime集（不必单调），则

    P_Fj → P_vac strongly。

证明是每个n>1固定选p|n，最终p∈F_j使P_Fje_n=0，n=1保留；再用||P_Fj||≤1和finite-support稠密。此处没有比较未经识别的不同Hilbert空间，也没有声明D_Fj的norm或resolvent收敛。

更具体地，对每firstfixed T，最终F_j含全部prime≤e^T，所以n>1且F_j-coprime时必有logn>T。自然harmonic能量L_H e_n=logn e_n的谱，在每个固定[0,T]内最终只可能0；paired ±L_H版本在[−T,T]亦然。**强P收敛本身不支付moving seeds、unbounded gain或无限traceweight下的源极限。** 这些正谱极限必须另消费准确topology桥。

## 4. 明确的physical源与合法正谱

L按m纤维为logm I，self-adjoint，且其unitary群e^(−iuL)强保持D(d)、D(d*)并与d及P_F相容。对r∈Cc∞(R;C)定义

    A_r=∫r(u)e^(−iuL)du=rhat(L)，rhat(t)=∫r(u)e^(−itu)du。

||A_r||≤||r||_1；若supp r⊂I且|I|有限，||A_r||≤√|I|·||r||_du。此为原physical r=e^(u/2)bare及第一槽linear的同一Fourier约定。这里只使用zero-extension Dlog的compact smooth core，不将K_F范数改叫原du，不补任意谱权对应的全部Dlog型域。

此处还有一个比裸P强收敛更强、但仍属标准源滤波的结论。在共同degree0载体上，令a_j为F_j外最小prime的log（没有则∞），则对每个**fixed** r∈Cc∞，

    ||A_rP_Fj−rhat(0)P_vac||
       ≤sup_(|t|≥a_j)|rhat(t)|→0。

故共同有界norm的moving seed也可由这个operator-norm滤波处理；不能只恢复较弱的P强收敛。对任何N，右端还可用a_j^(−N)||r^(N)||_1界住，但这支付的是明确强源半范数，不能升级成moving du-unit源的同费率。它也不是HS norm／无界rank或traceweight的统一控制；任意gain仍需另稿的正谱桥。

对source-independent v∈K_F，harmonic源

    J_(F,v)(r)=P_FA_rv=A_rP_Fv

满足||J(r)||≤||v||√|I|·||r||_du，且

    <J(r),J(s)>=Σ_(n F-coprime)|v_(n,∅)|²
                              rhat(logn)overline(shat(logn))。

这给有限正谱σ_(F,v)=Σ|v_(n,∅)|²δ_logn；moving v_j的范数费不能丢。若v本身为cycle，则A_rv也是cycle，且hA_rv给exact部分的primitive，K_F原费≤||v||||r||_1；不因此称它为实际arithmetic principal／Green primitive。

更一般，对harmonic空间上的bounded R≥0，只在A_rR^(1/2)确为HS的源上定义

    Q_R(r,s)=Tr(A_r R A_s*)。

正确HS sandwich／极化给合法S1，逐harmonic正交基求trace得

    Q_R(r,s)=Σ_(n F-coprime) R_nn rhat(logn)overline(shat(logn))。

R可非对角；其offdiagonal在这个ordinary trace中确实不贡献。**任意R≥0并不自动满足所有compact源的HS条件。** 无界R、非traceclass occupation或无限混合，须先给实际闭HS域／等价非负谱积分的合法性；不能用形式未夹源trace补足。任意正谱权与tempered域的扩展由另一稿处理，此处不预付。

同源positive mixtures及外部gain仍保该谱support；paired ±L只把它扩为{±logn:n F-coprime}，不产生其它有限frequency。σ以上述源积分定义，未额外添除2π；若作标准Fourier分布变换，应沿旧谱桥保反射与2π约定。

另一个模型Q(r,s)=<R A_rv,A_sv>一般含R的offdiagonal，不是上述ordinary trace；非stationary source Gram、逐源选seed及改变cohomological action不能被本式自动涵盖。它们保持准确未排范围。

## 5. 537反测的确切消费

取固定非零ψ∈Cc∞((-1/4,1/4))，令r*=ψ′；它非零、mean0，仍在537窗I0=(-17/16,17/16)。537完整源正性给

    Q_W(r*)≥2^(-49162)||r*||_du²>0。

mean0不等于polefree；原Γ/contact、全部properpowers及indefinite双pole均未从Q_W删去。F=all primes时任何上述harmonic正源型都只读rhat(0)=∫r，故在r*上exact0。这已拒绝该exact fullprime模型的全源coverage；不能把它说成allKoszul／allHodge失效。

对cofinal F_j，只有在另一稿支付**positive谱运输并把极限识别为完整Q_W的谱**后，局部support逃逸才迫目标谱cδ0，从而Q_W只能是c·(∫r)overline(∫s)，与r*冲突。单独vague收敛和强P收敛不够，尤其不能在unbounded gain下省略频率尾或目标谱识别。本文不替另一稿预先证明／消费该桥。

## 6. Thermal character不等于Weil身份

对σ>1，完整整数carrier的绝对thermal trace由基计算给

    Tr exp(−σL)=ζ(σ)∏_(p∈F)(1+p^(−σ))，
    STr exp(−σL)=ζ(σ)∏_(p∈F)(1−p^(−σ))
                     =Σ_(n F-coprime)n^(−σ)。

有限F是coprime Dirichlet series，不是常数1；F=all prime时才得supertrace1。可数F下σ>1的absolute trace由∑_m2^ω(m)m^(−σ)=ζ(σ)²/ζ(2σ)<∞支配，因此此处不是不合法的∞−∞。未经thermal权的Tr exp(−tΔ)却为∞：一个prime的powers已给无穷多相同r=0或r=1纤维。故不能把formal super cancellation或全primeEuler数1当作ordinary full heat trace，更不能叫completed ζ／Weil正性。

## 7. 强旧、准入判定与读取范围

080的finite divisibility incidence矩阵为不同的acyclic微分，其Dirichlet symbol和Mertens Green observable不能与本Koszul harmonic源互换。581反向共轭的Koszul作用在weighted rational-orbit carrier，H0/H1=0、H2一维，亦是不同pair/map；不能仅凭名字相同声称它已给本全部纤维式。但本模型的有限Koszul计算、正交直和闭包、gap1和源角色都是标准可直接验的组合，没有出现独立arithmetic primitive、principal下降、mixed RR或新的正性预算。

本稿只确认**canonical model的具体standard比较**，cofinal正谱运输仍由另一稿完成。若root对齐后确定是旧通用谱桥的直接组合，应准确old0收束，不据闭复形存在、新增notation或源滤波要求数学轮。最终old0和净值由root统一决定。Whole542+555→557 leading4/5负惯性UPPER及关键primitive/principal/mixed/signedcorecross/Ξ未改，Goal完成门不因本模型缩小。

本次恢复README/STATE，check后show；读Goal完成门、当前C055停止域、D20261029H及macro18相关责任段，全文核root当前prototype、080，核581指定§5原费用与源角色、537目标正窗。未重读所引外部论文／全部历史。只写本文件，未改任何状态／计轮、未用运行Goal工具、无新web/source/PDF/download/numerics；未成功派出或消费任何helper。

规范LF版本仅绑定本次读取对象，不证明外部结论，也不冻结未来合法状态更新：

| 文件 | LF bytes | SHA256 |
|---|---:|---|
| root-fiber-and-source-test.md（本目录） | 4978 | 917cf314af6574c91f518ceba3bead3d624444c11048192c84cd2434eeb1dacd |
| notes/080-divisibility-incidence-green-hodge.md | 8320 | d0e5fd6956f95d462116a84ece12e323c1ebedf3fcbb45e74a27c00125f3f249 |
| notes/537-source-exact-weil-window-positive-tail-admission.md | 8155 | 269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8 |
| reviews/2026-10-23/weighted-two-prime/sunit-relative-boundary-and-principal-test.md | 13390 | e501ae9ea855da3b23ca9d99e7a736d667ba8ab0a2f42f061ff6d565277aff2b |
| goals/GOAL.20261027.md | 9679 | b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de |
