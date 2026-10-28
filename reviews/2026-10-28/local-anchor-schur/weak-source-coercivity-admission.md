# 固定支撑弱源强制性：587 proof的合法运输与锚定正分解准入

2026-10-28；/root/rational_old_admission 独占准入/前件比较。已恢复README/STATE、check后show、Goal/C050、AG、frontier/summary与587根结算；当前C050已耗尽，cadence1/history51/latest587/formal17保持。本稿不新web/source、数学编号/合同，不改STATE/Git/cadence，也不将此准入稿代作C051的根消费。

**判定：题定弱源路线可闭合，且不需smooth或uniform Dlog范数；每个源属于原Dlog、common fixed compact support、du有界和非零L2弱极限已经足够。** 新使用的是587 proof中对全部complex多项式的实际frame/全尾/Jacobi gap，加一次针对非零弱极限的解析因子化；不是把585逐fixed源定理直接套moving源。587已发行的fixed-degree源组及source-rank结论没有直接写出或消费这个弱源命题。它能处理明确的fixed-coercive-anchor正分解中的任意成长rank/源适应修正，但不能扩大成全部成长anchor或全部signed修复的边界。

## 1. 精确待核命题、旧scope和原域

设X_n→∞，所有f_n都是**physical log源**，零延拓后有共同fixed compact支撑J，f_n∈原zero-extension Dlog(J)。假设

 sup_n ||f_n||_du≤M，f_n ⇀ f≠0 于L2(J)。                    (A)

不假设sup ||f_n||_Dlog有限，也不要求弱极限f仍在Dlog。待核结论为actual t_(X_n)[f_n]→+∞。若限定f_n∈Cc∞当然也是其子类。

587正文§1只对固定r_0的每先fixed有限阶导数空间给全部moving coefficients共同lower；§5随后排固定上限source-rank，并保留成长rank非空。正文及所绑定proof/fresh/root记录的定点检查没有Rouché/Montel/弱源局部一致收敛的已消费段。不能只从正文定理把任意f_n认作某个固定E_(d+1)的元素。

可复用的更强原件是587§§2–4及其两proof：ALLpoly全线norm/tail、Gaussian Jacobi的fixed-degree多项式gap、实际向量D_E H_0p_j及全Gram逆。它们比已发行的scalar结论更强，不能遗漏；下面逐项接上新增的解析前件，既不据“未写出”直接判新颖，也不把所需弱源命题假装旧定理已有。

原Dlog的必要作用很具体：560§4已以fixed-window Fourier core把finite-X ordinary trace/HS域运输到全部原zero-extension Dlog源，所以每个t_(X_n)[f_n]是真实有限正迹。du有界、fixed支撑则保证A_(f_n)有界，||A_(f_n)||≤||f_n||_1≤sqrt(meas J)M。只用L2支撑时也可谈非负扩展trace，但不能免费宣布普通迹有限；本命题保Dlog以免换域。

## 2. Weak L2到整函数的局部一致收敛

令F_n(z)=∫_J f_n(u)e^(−izu)du，F为f的同一Fourier变换。由于J有界、f_n∈L1，F_n和F均为整函数。若J⊂[−R_J,R_J]，则对每个fixed complex compact K，

 sup_(z∈K)abs(F_n(z))≤sqrt(meas J) M exp[R_J sup_K abs(Im z)]。

所有z导数也有同样类型的界，只添fixed R_J的幂。对每个fixed complex z，核e^(−izu)给L2(J)的连续线性泛函，故弱收敛使F_n(z)→F(z)。局部一致有界/等度连续，加有限网格或normal-family唯一极限，给

 **F_n→F locally uniformly于C。**                         (B)

这是同一commoncompact/du费用的结果，不依高阶导数或Dlog一致界。f≠0及Fourier单射给F不恒零，因此k=ord_(z=0)F有限。f可以不光滑；此整性及有限零阶仍成立。

## 3. Rouché分解必须保留移动零点，不能直接误差相减

取一次fixed complex disk abs(z)≤R，使F在盘中除0以外无零，0的重数为k，且边界无零。缩R时也使H_0在相应real core上非零。若k=0，直接取P_n=1，以下论证退化为F_n的uniform正模lower。

当k>0，(B)及边界min abs(F)>0使Rouché适用：大n时F_n在盘中恰有k个零点，按重数记ζ_(n,1),…,ζ_(n,k)。对每个fixed小ε>0，F在ε≤abs(z)≤R上无零，局部一致收敛又保证F_n在该annulus无零；故全部ζ_(n,j)→0。定义

 P_n(z)=∏_(j=1)^k(z−ζ_(n,j))，U_n(z)=F_n(z)/P_n(z)。

P_n为monic degree k，P_n→z^k；所有盘中零点按重数被除净，U_n是该盘的无零holomorphic函数，不是只在避开零点的real轴上作形式除法。边界上

 U_n→U:=F/z^k uniformly，U是闭盘中的无零holomorphic unit。

U_n−U在盘内holomorphic，最大模原理将边界一致收敛传入闭盘。因此选fixed 0<δ<R，有fixed u_*>0，使对所有大n和abs(t)≤δ，

 abs(U_n(t))≥u_*，故 **abs(F_n(t))≥u_*abs(P_n(t))**。       (C)

此处不要求F_n的零点实、成对、简单或以已知速率趋0。monic保证coefficients的Euclidean范数至少1；即使F_n(0)为0或非常小，(C)仍有效。直接写abs(F_n)≥abs(F)−o(1)再乘一个可能巨大trace质量会留下孔洞，当前exact因子化避免该步骤。

## 4. 接入587 actual frame：δ/c仅作一次fixed证明见证

需要明确复用587 proof的参数量词。选出的δ可以小于587原r_0所用core；原Gaussian范数稿§§1–4使用的是任意fixed δ，只要H_0在core有fixed正lower，再一次选c_δ>0足小，使ALLpoly矩费小于δ外Euler exponent gap。现在沿同一(W)/(P)/Gaussian/Gevrey全尾推导，取

 ℓ_n=log X_n，A_n=sqrt(X_n)/ℓ_n，N_n=floor(c_δ A_n/ℓ_n)。

δ、c_δ及阈值允许依非零weak limit F，但选定后不随n改变。这只是从587已付参数家族选一个receiver trial witness；没有改变W_X、候选m_X、H_0、物理源规则或anchor，也不是继续优化C050。不能拿原较大core的固定c直接省去较小δ所需的gap条件。

μ_G=w_Xe^(−t²)dt/(2π)仍仅辅助norm。对应Gaussian正交p_j及真实v_j=D_E H_0p_j的frame Gram满足fixed c_H I≤mathsf H≤C_H I，实际投影V mathsf H^(-1)V*≤Π_X，完整inverse不删。旧全线tail对全部complex多项式deg≤N_n+2同时有效。

令j取ceil(N_n/2)≤j<N_n−k。则q=P_np_j的degree<N_n；由core(C)、core上μ_H/μ_G的正下界及ALLpoly尾，

 ||A_(f_n)v_j||²
 =∫abs(F_n p_j)²dμ_H
 ≥c∫_(abs(t)≤δ)abs(P_np_j)²dμ_G
 ≥c′||P_np_j||²_G，                                     (D)

常数对n统一。core外actual积分是非负项，丢弃它不需F_n与某fixed Fourier函数的全线相对误差，也不要求F_n是一个多项式乘fixed bump。

原finite-frame ordinary trace比较及587的**先fixed degree k** Jacobi gap于是给

 t_(X_n)[f_n]
 ≥c Σ_j||P_np_j||²_G
 ≥c_k N_n(N_n/Λ_(X_n))^k ||coeff P_n||²
 ≥c′_k sqrt(X_n)/(log X_n)^(3k+2) →∞。                    (E)

Λ_X≤C sqrt(X)logX为同一原Euler曲率费用；coeff P_n可随n移动，monic使其norm≥1。所有path indices和degree保持587已经付过的N+2范围，k先fixed，不调用d_X→∞。k=0时同式给N_n量级。定性发散是本门目标；(E)中的常数、k/core/c及起点均可依该非零weak limit和序列，不声称整个du单位球的统一率。

这条检查没有把μ_G当ρ或Sonin向量：真实向量始终为D_EH_0p_j。dt/(2π)只在trial/Plancherel norm中保原规范，actual t_X=∫abs(F_n)²ρ_Xdt不另添除2π。源f_n每次处在同一fixed J的原Dlog域，560 ordinarytrace可用；不存在把moving源起点代入585 scalar定理的步骤。

## 5. 固定coercive anchor正分解：成长rank及源适应均不救固定平移测试

精确范围是下面的正分解，而不是仅有“q_X落在正区”这个标签。令I_0=(−17/16,17/16)，对每个q∈原Dlog(I_0)，537给

 Qζ(q)≥κ||q||_du²，κ=2^(−49162)>0。

对Dlog的使用可沿原560的Cc∞ core及完整固定窗Weil型连续性延拓537；不能只用一条不明拓扑的闭包。实际finite source-Schur例的q_X是Cc∞组合，连这个延拓都无需另假。

固定r_a=τ_4r_0，support=[3,5]，故在I_0外非零。对每个X，允许任意q_X(r_a)∈Dlog(I_0)，但必须实际有

 **W_X[r_a]=t_X[r_a−q_X]+Qζ(q_X)**，                      (F)

两项非负且第一项系数1。q的rank可以成长或无限、range可在anchor内任意变化、系数无预定上界；单源值的论证也容许非线性/source-adapted选择。若声称W是sesquilinear正型，则其线性/共轭槽仍须由实际生成式另付，不能从非线性q这个更宽数值范围自动取得。

假设存在X_n→∞的子列使W_(X_n)[r_a]≤B。**只有在这一假设后**，由(F)和coercivity才推出

 ||q_(X_n)||_du²≤B/κ。

仅有anchor support不能给这个bound。L2(I_0)有弱紧性，抽取子列q_(X_n)⇀q；零延拓后f_n=r_a−q_(X_n)有共同fixed compact支撑J，du有界且f_n⇀r_a−q。弱极限q仍支持于closure(I_0)，虽未必Dlog；在I_0外，残差弱极限等于r_a，故必非零。每个f_n仍在原Dlog(J)。

于是(A)–(E)适用，t_(X_n)[f_n]→∞，与W_(X_n)[r_a]≤B矛盾。因此

 **W_X[r_a]→∞，对(F)类的全部上述q_X选择成立。**             (G)

这不靠固定rank上限，也不是在growing-degree源组上应用587。它确实覆盖题定actual T_X source-Gram投影P_X的q_X=P_Xr_a：只要range位于这个fixed coercive anchor，W_X=T_X((1−P_X)·)+Qζ(P_X·)具有(F)，就受此门约束。具体T-Gram inverse/positive form定义由另一独占稿核，本稿不将T-Schur与Q-Schur混用。

完整Weil目标的物理平移不变性给Qζ(r_a)=Qζ(r_0)，是fixed有限值；在full Γ/contact、全部proper powers和两个pole齐全时成立，不靠删pole或prime。故(G)拒绝本类在全部fixed compact卷积平方上趋完整Qζ的必要条件。若另声称W_X来自一变量正分布，必须先有该分布身份；本固定测试失败不需提前假定W_X具有translation invariance。

## 6. 新信息差、合法逃逸与准入建议

587现有source-rank→∞必要性没有排成长rank；(A)–(G)比较的是**另一个明确强前件类**：common fixed source support、du弱紧且残差weak limit非零，以及固定coercive anchor的两项正分解。新增闭合步骤是normal-family/Rouché保留moving零点，再用已经支付的ALLpoly/Jacobi/actualframe，而非改degree、log指数或C050参数。旧587已述定理不能直接套它；当前定点核读也未见该强结论已root消费。它是可准确冻结的一项新量词/方法范围比较，不是新独立算术数据；是否形成新完整数学结算，须由root对齐实际Schur族和strongest-old净scope统一决定，不能只凭未印出或技术标准标签判0/1。

若正式冻结这一门，可得到完整覆盖**(F)固定anchor正分解类**的source-adaptive/growingrank边界，包含任意rank、任意anchor内range和无预设系数bound；bound由假定有限输出而来。它不能称“所有成长rank修复失败”，更不能直接通过Goal整体核心方法类完成门。587原谱截断按K构造的非空成长rank逃逸、577不同正D′规则与完整t−K+pole相消并未被(F)覆盖。

下列条件不能省略：weak limit允许为0时本解析有限零阶门不适用；common support丢失时du弱收敛不再给整函数局部一致控制；anchor随X扩张/漂移、失去uniform du coercivity、残差前置系数趋0或另有signed cross抵消，都不能由本论证排除。无限维anchor版本还须q_X实际属于原Q/trace formdomain并有同一κ，不凭“闭子空间”免费准入。这里没有给这些逃逸新预算或新候选。

本稿支持root仅按上述具体对象/原norm/正分解与固定平移负控制判一次准入，不写全面新合同、不预发数学编号、也不扩到另一来源或泛形成。C050耗尽、cadence1/history51/latest587/formal17不动；完整signed净号、primitive/principal/mixed、全corecross及Ξ与whole4/5UPPER仍未在此准入稿中支付。

版本绑定：587为8681 bytes/LF SHA256 `e4d30cfb6d07299386014cb4c4e3e3979ab5111264355dfb37b24629f121ac82`；Gaussian实际frame稿12142 bytes/`1ce4ebc02ba8790d21b83642683cf910d8102802af5769f640b6dc1192603ed4`；Jacobi稿13009 bytes/`e76fefa49913f09754a9a68c4a661bc20ef59089bfd375e80563f473eecb187c`。原norm/ordinarytrace及全部目标项按560/537原消费范围保留。
