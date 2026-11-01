# C070：联合Hermite截断的独立数学审查

2026-11-01；/root/c070_independent_math_review。只作当前三份终态数学稿及ROOT工作稿的独立review，不是作者证明、ROOT消费、合同结算或新候选。恢复README/STATE，check后show，读取同一Goal、C070、D20261101S和macro frontier；初审时anchor分工尚在执行，现已实际读取其终态及ROOT工作稿。当前STATE为三稿ROOTread、等待本审查。本稿不改STATE/cadence/Goal/库/Git，无新PDF、web、source、数值或科学代码。

**结论：已检查的数学主链PASS，但须限定一处trace措辞并补扣更强的已付旧localization。** 三稿与ROOT工作稿均未支付实际比值；不能从absolute upper、conditional RC或physical下界通道推出C070通过、反例、zero-denominator结论或方法类边界。

## 1. 当前输入与独立性

已全文读并核实际字节：

* finite-column-and-coherent-cutoff.md：9800bytes，SHA256 c5f2c5c76fcd27d0aeb6e5cf767ca0f7e2bc2c19b841490ee18ab36c20dc5e95。
* independent-three-ratio-analysis.md：12230bytes，SHA256 49a1b8e5f9db4eaadee7d6f9b3c81b70aef6540e1c5d6d630d104ac4b2270da6。
* cofinal-anchor-and-relative-remainder.md：10905bytes，SHA256 8256b79d4eea9c6aac2e9b7bec8f0ff985a9921c2aa93ab191405ebf363357a5。
* root-relative-comparison-attempt.md：3863bytes，SHA256 9bc0c41870f8e674bff4326cdb52916d8c6ad40e12438d3b93cd63ce3134ae8e；此项是待消费的ROOT工作稿，不是第四份独立作者证明。

原稿保持这些字节。另实读formation/spec、560/591相关实际接口、591 actual-gevery-tail-and-premise-closure.md §1–2，以及critical-prime-covariance-proof/localization-and-rate-proof.md §§1–4与其root-consumption-scope.json的LOC/D4。后者是已经root消费的旧C059/596资产，不是新来源。

本review没有参与三稿或ROOT工作稿推导。另委托一个message-only独立核对conditional-gap代数，结果PASS且明确RC未支付；该核对没有文件或新研究输出。其结果与下列本review核验一致，不增加数学轮。另已读ROOT的stronger-old-loc-and-consumption-limits.md，所限旧LOC／positive sandwich／实际下界通道范围与本review独立核验一致；该消费限制不代下面的推导检查。

## 2. 对象、域和kernel核验

actual Pi_j是560/603的全部Euler-Gram inverse投影，A_r=M_rhat，physical r与native e^(-u/2)r分别保留。E_(j²)是在receiver上的log-Hermite投影；Mellin列sqrt(2pi)(-i)^n h_n可逐列重相位成phi_n=sqrt(2pi)h_n，同一个E_N不变。相对dmu=dt/(2pi)，E_N kernel为2pi sum h_n(v)h_n(w)，trace中2pi消掉；未遗漏Plancherel因子。

first-linear公式Tr(E_N D_s*D_r E_N)与有限列积分L_r overline(L_s)一致。每行k_j(t,.)∈L²，row norm²=k_j(t,t)，故bounded f和phi_n给合法的单列积分；不需要裸Pi是S1。三重式保留K_N(v,w)的非局部相干项，不能将其替成K_N(v,v)、frequency weight或591的非负jump权。

对每先fixed j，560的finite-F恒等式给k_j(t,t)≤C_(F_j)log(2+|t|)。用projection列的Cauchy–Schwarz，

    ∫|k_j(t,v)k_j(t,w)|dmu(t)
       ≤sqrt(k_j(v,v)k_j(w,w))。

再用phi_n Schwartz，主稿的绝对Fubini估计正确。此处C_(F_j)只用于fixed-j合法性，没有被冒作共同j费用。CD式的系数sqrt(N/2)、符号和v-w分母正确（N=1也相合）。

**必须保留的trace限定。** independent稿§3文字“trace of P_j 1_S1 is legitimate”不能按裸乘积P_j1_S1∈S1消费。实际论证只需、且正确给出

    ||P_j1_S1||HS²=Tr(1_S1 P_j1_S1)
                 =∫_S1 k_j(t,t)dmu(t)。

这是positive compression/HS身份；不证明裸P_j1_S1 trace class。主稿已明确positive sandwich，因此限定这句消费即可，联合upper不受影响，无需改旧原稿或重证。

## 3. 两种Hermite估计和fixed-eta联合upper

主稿Mehler式正确。z=e^(-1/N)给H_N(t,t)≤c_H sqrtN，c_H=e/sqrt(pi(1-e^-2))；z=1/2配partial-sum因子2^(N-1)给2^N/sqrt(3pi) exp(-t²/3)。两侧Gaussian tail系数sqrt(3/pi)2^(j²)j^-2 exp(-j^4/3)正确。

独立稿的oscillator/Sobolev证明也闭合：对first-N unit vector，||v'||²≤2N-1，积分(|v|²)'得sup_t sum_(n<N)|h_n(t)|²≤2sqrt(2N)。t乘法把first N送到first N+1，故每个||t²h_n||²≤(2N-1)(2N+1)，并得到tail≤4N(N+1)²/T^4。N=T=j²给tail≤16/j²。它提供不依赖Mehler的自含备份。

两稿的INPUT三域分割正确：core用Pi contraction和Hermite diagonal trace，annulus用Pi1_S的HS及M_f E_N的bounded norm，far用Pi contraction与Hermite tail。没有把Pi E_N的OUTPUT也假定局部化，也没有移动E_N或丢cross terms。

对每先fixed eta>0，已付actual full-Gram kernel localization在eta≤|t|≤j²给指数小middle；先j→∞再eta↓0，确实证明

    b_j²=o(j)，
    b_j=sup_(||f||∞≤1)||Pi_(e^j)M_f E_(j²)||HS，
    C_j(r)≤4b_j²||r||1²。

sup可在所有bounded measurable receiver multipliers上取，不意味着它们全是physical Fourier源。因该sup在取极限之前已受共同界控制，L¹源（包括changing complex源）有同一费用；fixed source窗[-L,L]的du-unit ball随之有一致upper。没有付全线du、growing L或无界校准后的uniform费用。

## 4. 更强的已付旧资产：不得只拿O(j²)作对照

强旧核查发现，除了两稿引用的C052固定eta接口，C059/596已经支付实际moving-core bound。准确来源为

    reviews/2026-10-29/critical-prime-covariance-proof/
      localization-and-rate-proof.md §§1、4 (Loc)，

以及同目录root-consumption-scope.json的status=root-consumed-limited-proved、LOC/D4闭合。原稿的issue-time pending文字由该root收据支配。

§1明确F可以是全部q≤X，最后才令X=p；§4先证明FULL版本：对每fixed b，所有real X≥X0(b)，L=logX、A=sqrtX/L、delta=L^(-2/5)，

    sup_(delta≤|t|≤L^b) k_≤X(t,t)≤exp(-c A delta²)。       (OLD-Loc)

随后另给omit-p的(Loc<)。因此当前Pi_(e^j)可用FULL (Loc)，不是把prime-omission结果免费搬来；actual k包含完整G逆，亦非bare Q或Euler权。取已付b=2，没有新增band或指数优化。

同一HermiteINPUT三分直接给更强的旧后果：delta_j^old=j^(-2/5)、T=N=j²时

    b_j≤sqrt(4sqrt2 j^(3/5))
          +(j/sqrtpi) exp[-c e^(j/2)/(2j^(9/5))]+4/j，
    b_j²=O(j^(3/5))，
    C_j(r)≤O(j^(3/5))||r||1²。

这里delta_j^old只是旧证明的频率cut，别与合同的ratio-error delta_j混同；candidate路径和三个测试都没有改动。该应用只组合旧OLD-Loc与本稿已核的标准Hermite界，不是新moving-eta证明。系数对bounded multipliers共同有效，fixed-L du源的相应量词保持。

故原两稿的o(j)证明数学上正确，但它不是最强已蕴含upper。其“fixed-eta接口本身不支付eta_j”应仅限那个接口；不能泛化为项目所有旧资产都没有moving localization。旧C059已经闭合指定的j^(-2/5)。不需进一步选a、优化指数或开启参数队列。

若共同校准匹配q0，只能从O(j^(3/5))直接推出liminf c_j j^(3/5)>0（常数依该upper与g），继而c_jj→∞。不能把这个O界改读为c_jj^(3/5)→∞，也不能推出c_j本身发散。更强旧upper仍没有anchor lower或actual ratio。

## 5. 列递推、平移和条件gap

主稿(F)合法：t phi_n属于L²且只涉及邻列；H=tG是bounded multiplier。B_n=M_G Pi(t phi_n)-M_H Pi phi_n不需要未付的Pi phi_n∈Dom(M_t)。因此该identity没有隐藏unbounded-domain运输。边界L_N只是同一有限递推的endpoint，不是另选N路径。

主稿(T)的product commutator、1/2因子和real cross正确；反射平均对应shift±a，故它保留的交叉项没有591的免费有利号。

独立稿§5条件引理PASS。v_a的Fourier符号为-i sin(at)G，而g′是itG，所以v_a+a g′是正确的三阶余项。反射平均产生exact even/odd正交。若最终A_j=sqrt(C_j(g))>0且实际RC

    e_j+o_j=o(A_j+B_j)， B_j=sqrt(C_j(g′))

成立，任一bounded-ratio-error子序列上B_j/A_j有界，故e_j/A_j、o_j/A_j→0。再取B_j²/A_j²→r≥0，平移比趋1+a²r，

    max(a²r,|r-k|)≥a²k/(1+a²)=k/5， k=q1/q0>0。

这严格给conditional liminf ratio-error≥k/5。无界error子序列不能降低liminf。第一槽、符号及2因子均无问题。条件RC是额外的实际相对coherence/anchor责任，不是已付localization或upper的结论。

## 6. 尚未支付的实际责任

两稿没有证明最终C_j(g)>0、无限零分母、实际RC或actual ratio-error的通过/失败。绝对upper即使加强到旧O(j^(3/5))，也不给A_j+B_j的同尺度lower，任意共同c_j仍可能放大所有余项。Pointwise Taylor不付非局部E_N后的相对feature比较；固定X穷尽不付joint path。

591共同occupation、603不同输出投影及594 trace-word仍须原前件，不能按名称套用。反过来，本review也不证明它们未来绝不可能适用。没有全mixed/D′、principal、sections、mixed容量或growing core/coupling/Ξ结论；Γ/contact、proper powers、双pole和odd源保持。

## 7. 对完整当前attempt的分类建议

建议将合法kernel/列identity、absolute joint upper及必要校准条件作为**old-derived、标准短链推论**消费；将k/5作为**通用PSD/反射代数的conditional reduction**消费。它们是严格且可复用的数学记录，不是“没有做证明”；但在最强旧OLD-Loc及标准Hermite扣除后，没有新增独立算术输入、actual ratio裁决、whole classical净后果或核心瓶颈移除。

不能只比较weak O(j²)与o(j)而登记新的whole-object净改善；更强O(j^(3/5))已经是同一旧链可消费后果。下面§8–9核完第三稿与ROOT工作稿后，完整受审attempt仍只有旧算子结构的标准短链support／Poincare代数、absolute upper及generic conditional reduction，没有另一个独立严格净结果存留。本review建议按合同旧推论门记0新增数学、不建607；本次ONE证明预算按实际已完成attempt停止，不重置或自动排后继。实际比值、anchor lower和零分母分支须原样OPEN，不能把未知结算成通过或反例。最终ROOT消费、合同状态和统一记账归ROOT，本review不修改共享执行状态。

同一长期Goal的最强whole17/16、fixed9/8 head、same605唯一头+ALL complement正完成及whole4/5负惯性UPPER保持；三完成门open。未改任何共享执行文件或cadence，也未创建607或后继任务。

## 8. 第三稿：actual物理边界通道的核验

第三稿区分physical receiver y与Mellin频率t正确。M=Ran P包含于y≥0，B_j是finite forward-shift Euler乘积，非identity项的最小shift为log2。Xi_j=P B_j* I_N的有限Mobius和使用负shift U_(-log d)，T_j=G_j^(-1)Xi_j属于M；Pi_j I_N=B_jT_j保完整Gram逆。未把有限Mobius和升成1/zeta或把合法列升成定量coercivity。

对supp r⊂[-c,c]且c<log2，A_rT_j的support在[-c,infinity)，所有B_j非identity项均移到正半线；同时H_-Pi_j=0。因此Lemma1

    H_-[Pi_j,A_r]I_N=-H_-A_rP T_j=-L_rT_j

是exact有限列identity，所有算子在r∈L¹时bounded。g、g′的b=1/8及两个a=1/2平移源满足最大support a+b=5/8<log2，适用范围准确；没有把输入频率localization改成输出频率localization。

对每列v=T_(j,n)，F=A_gv在[-b,infinity)有support且F(-b)=0，F′=A_(g′)v。FTC加Cauchy–Schwarz并积分给单端Poincare

    ∫_(-b)^0 |F|² ≤ (b²/2) ∫_(-b)^0 |F′|²。

故实际channel B_j(g′)≥2B_j(g)/b²正确。只有B_j(g)≤C_j(g)，不能把此式升级成两个full C_j的同向比较。shift+a通道为0，shift−a通道积分到a，反射平均的1/2正确；所得C_j(tau_a g)≥B_j(g)/2仍不是目标ratio判定。

Full-anchor式(6)的三个项、-2Re cross与最后K_j(r†*r)均正确：分别展开Pi_j A_r I_N、A_r Pi_j I_N的norm与实际cross，并用B_j*B_j在M上的G_j。它保留同一个actual Gram inverse及有限N traces，不免费删除相消。Xi_j总捕获或G_j逆norm控制本身不能支付此差的lower。

refined even symbol R_e的实际compact source是两shift平均减(1+lambda)g；余下lambda I只参与commutator代数，不是送入Weil型的delta-source。物理区间(-a-b,-b)上只有shift−a项存留，系数1/2平方为1/4；平移后(-b,a-b)包含(-b,0)，故

    ||[Pi_j,M_(R_e)]I_N||HS² ≥ B_j(g)/4

成立。relative refined-even remainder为o(sqrt(C_j(g)))仅迫beta_j=B_j(g)/C_j(g)→0；稿中没有支付beta不消失或趋零，更没有实际RC。此项是exact support代数给出的必要条件，不是C070固定路径反例或新增实质方法类边界。第三稿无actual anchor lower、最终分母正、无限零分母或三比值结论；其自述范围正确。

## 9. ROOT工作稿：费用与逻辑负控制的核验

Phi_j的reflection direct sum使even／odd源exact正交。u_a=g+h_c、v_a=-a g′+h_s给两个向量norm分别为sqrt(A+a²B)、sqrt(S)，差的norm为sqrt(R)。反三角不等式因此给完整平方

    R≥[sqrt(A+a²B)-sqrt(S)]²。

不需删除相干cross或换成positive part；若同一c_j匹配三个正目标，其标量连续极限确给稿中严格正的liminf c_jR。此式只是一项必要费用，未给实际R相对小。Taylor refinement的lambda=a²/m2与系数1+lambda正确；g自身commutator从G−1起算，因此二阶vanishing本身不付层级。

phase-blind逻辑控制亦正确，且须严格保其角色。W_b=M_exp(ibt)与所有source multipliers交换；abstract conjugate W_bPi_XW_b*保k对角、|k|²、夹源positive traces与full HS。固定N列W_b*phi_n弱趋0由L¹ Fourier的Riemann–Lebesgue给出，旧560 compact commutator将它们送到强零，有限N／有限三源的右截断能量遂趋0。

这说明仅这些phase-blind数据不能推出一个跨该抽象conjugacy类的positive finite-E anchor lower。该conjugate没有被证明是同一actual B/P/G或满足同一physical边界；故此论证不是C070实际变形、实际ratio反例或actual Pi no-go。原稿已明确此限制，ROOT消费必须保持。

完整受审结果没有支付共同校准后的relative coherence、actual denominator或目标比值。更强旧absolute upper与所有上述标准恒等式均不能改变这点；当前核心瓶颈及长期Goal完成门未变。
