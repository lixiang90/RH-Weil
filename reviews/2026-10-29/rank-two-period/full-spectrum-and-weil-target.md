# 秩二 period 全零谱：全截断参数的温和极限与完整 Weil 反测

2026-10-29；`/root/rank2_spectrum_target`独占原推导。**本腿已闭合：正零轴／phase13204-byte最终原件已实际全文读取/hash并独立核用到的前件；完整无限零谱、全a紧化、真实Pan泄漏、共同compact反测及正修补/必要signed成本均在下文支付。** 本稿不修改STATE、cadence、库、Git、Goal或合同，不计轮、不授C063/600。标准相位、乘积、旧Pan与正混合是同一family责任链，不拆成后继数学轮。

## 1. 对象、恢复与准确依赖

实际读README/STATE并运行`research_state.py check`后`show`，读Goal完成门/基线、停止的C062、AH、macro599及当前rank-two明确准入。当前计数1/history63/latest599/formal20；599已发布且本次新source公式由root另核。本文不冒称自行live核父Goal/远端，亦不创建运行Goal。

设ξ(s)=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/2为通常整函数，a≥0，

    G_a(z)=[e^(az)ξ(1+z)−e^(−az)ξ(z)]/z，
    F_a(z)=G_a(z)/G_a(0)。                              (1)

来源是T=e^(2a)、z=2s−1下的实际积分消pole完成：s(s−1)I(T,s)=−T^(−1/2)G_a(z)。这里z是自然中心谱坐标，不能把HS内部变量、另一个s-clock或native norm代入。来源只取root已核的§1准确公式；本文没有打开新PDF、网页或作者后章/RH/simplezero证明，也不从未读作者定理反推下述前件。

本文实际核405的S_exp、谱和/完整显式公式连续延拓及§§4–5真实双矩零源，553§1的physical Fourier及actual Q角色；537§2全复源固定窗严格正性只作一个已有非零anchor。并读599全零谱稿的原Pan/crop范围，沿用的是旧实际源和连续性，不沿用其quartic ODE或Ising谱结论。原paper/嵌套外部证明未被重新审计。

## 2. 正零轴／phase前件的实际消费

已全文实际读取13204-byte `positive-zero-and-phase.md`，raw SHA256 f840095ae6d271f7a9acc84bde7f259c07d7bbe2ab2f9ec763d4aa7167ea67b2，逐项核其水平反射quartet距离差、Hadamard实常数C=0、相位导数/中心/simple及Tonelli-RvM尾。该稿自含证明实际支付以下命题，不用RH：G_a为real even order≤1整函数，

    G_a(0)=2[aξ(1)+ξ′(1)]=a+2ξ′(1)>0，               (2)

全部零点是简单的±iγ_n(a)，γ_n>0。令φ_0(t)为arg ξ(1+it)从t=0连续选择、φ_0(0)=0，φ_a(t)=at+φ_0(t)，则φ_a严格递增、φ_0(t)→∞，

    φ_a(γ_n(a))=nπ，n=1,2,…，
    0≤φ_0(R)≤C R log(R+2)（R≥1）。                  (3)

正性所用的Hadamard常数/水平反射配对、边界相位导数、中央可去点及简单性已由这个实读前件支付，不是只根据(1)外观假定。以下§3–9仅需(2)–(3)、G_a对(a,z)连续和上述标准ξ事实。

## 3. 全部无限零谱的统一计数、绝对尾和温和分布

定义含全部重数的正测度及物理分布，约定hatφ(t)=∫φ(v)e^(−itv)dv：

    μ_a=Σ_(n≥1)(δ_γn(a)+δ_−γn(a))，
    W_a(φ)=Σ_γ hatφ(γ)， V_a=W_a/(1+a)。              (4)

这里不是有限根表。由(3)，含端点的准确全计数为

    μ_a([−R,R])=2 floor([aR+φ_0(R)]/π)。              (5)

在零点端点采用floor，区间差分的误差至多常数；该误差不随a或区间位置增长。故R≥1时

    μ_a([−R,R])≤C[aR+Rlog(R+2)+1]。

令ν_a=μ_a/(1+a)。|t|≤1用(5)给ν_a质量统一有界；dyadic环[2^k,2^(k+1)]上以计数upper乘(1+2^(2k))^(−1)，得到

    ∫(1+t²)^(−1)dν_a(t)≤C，所有a≥0。                (6)

因此每个Schwartz φ的完整和绝对收敛，并有

    |V_a(φ)|≤C p(φ)， p(φ)=sup_t(1+t²)|hatφ(t)|，
    Σ_(|γ|>R)|hatφ(γ)|/(1+a)
       ≤C sup_(|t|>R)(1+t²)|hatφ(t)|→0，              (7)

最后极限对全部a≥0一致。也可由同一dyadic求和得(6)的高频积分尾O(log(R+2)/R)。这里使用(1+t²)权，不用会随a²增长的逆平方矩来冒称a统一。低零点γ_1(a)→0不破坏(6)；它是μ_a/归一化的计数质量控制，不要求γ统一离0。

对所有compact complex r，r*(v)=overline(r(−v))，

    Q_a(r)=W_a(r*r*)=Σ_γ |hatr(γ)|²≥0，
    Qbar_a(r)=Q_a(r)/(1+a)=V_a(r*r*)。                (8)

W_a、V_a为正型温和分布，Fourier规范是W_a=F^(−1)(2πμ_a)。全零谱两符号均计入，(4)–(8)没有另加2π。以上只付Schwartz半范数和fixed物理源，不是全线du或zero-extension Dlog单位球的bounded读出。

## 4. a→∞的真实极限与紧化连续性

对固定0≤u<v，(5)差分给

    ν_a((u,v])=[a(v−u)+φ_0(v)−φ_0(u)]/[π(1+a)]
                 +O((1+a)^(−1))。

负轴由偶性得到同样结论；穿0的区间由(5)直接处理，无遗失δ_0原子。于是a→∞时ν_a在每个有限频率区间vague趋dt/π。先在有限频率用此极限，再用(7)同时丢掉两侧尾，支付全部Schwartz测试：

    V_a(φ)→(1/π)∫hatφ(t)dt=2φ(0)，
    V_a→V_∞:=2δ_0于S′，从而D′；
    Qbar_a(r)→2||r||²_du。                            (9)

因而极端a并非目标谱的未分析孔洞：相应归一化极限是明确的flat spectral measure／物理2δ_0。它不等于原Weil型。

对每个有限a_*，(1)或相位反函数给γ_n(a)在a_*附近连续；每个有限区间只有一致有限个零点。局部计数/重数配合(7)给a↦V_a(φ)连续。连(9)，它在紧化参数空间A=[0,∞]（例如a/(1+a)∈[0,1]）上连续，且满足统一(7)。本文S′收敛均指每个Schwartz测试；共同半范数界另给所有需要的尾/源极限交换，不把它变成成长窗du一致率。

同一个尾还付全部有限频率截谱V_a^R(φ)=Σ_(|γ|≤R)hatφ(γ)/(1+a)在R→∞时对a逐Schwartz测试一致趋V_a。若混合components各有不同频率cutoff，后续lower只能消费实际落在足够大cutoff部分的保留质量；不能用“每标签分别cofinal”替代共同质量/阈值条件。

## 5. 无RH的完整目标反测：余零点乘积

沿405/553固定同一个真实非compact Pan源

    p=(D²+D)h=Eη_0，P(v)=e^(v/2)p(v)∈S_exp，
    μ_±(P)=∫P(v)e^(±v/2)dv=0，Q_ζ(P)=0，
    hatP(t)=s(s−1)ξ(s)/2，s=1/2−it。                 (10)

Q_ζ仍是含完整Γ=2θ′/FP-contact、proper powers和双pole的actual型；它在S_exp连续。(10)由实际源在全部ξ零点的Mellin消失与正确partner给出，不是假设RH后将Q_ζ写成PSD和。

设H(z)=ξ(1/2+z)/ξ(1/2)。它real even order1、H(0)=1，零点w=ρ−1/2位于|Rew|<1/2，不假设它们在imag轴。通常ξ在实轴无零。由RvM，Σ_w |w|^(−2)<∞，标准Hadamard按±w配对给正常收敛乘积。F_a也even order≤1、F_a(0)=1，故

    H(z)=∏_(±w pairs)(1−z²/w²)，
    F_a(z)=∏_(γ>0)(1+z²/γ²)。                       (11)

evenness消一次指数、归一化消常数；order≤1不容额外Gaussian。不能只用“两个函数order都1”判断它们的零除子。

假设某a的每个model γ均使hatP(γ)=0。因s(s−1)=−1/4−γ²≠0，model全部零点属ξ的critical零集。model简单性使每个±iγ可从H中消去一次，且不超过ξ重数。Σ|w|^(−2)绝对收敛允许按这一子集消去和任意对称重组；因此

    R_a(z):=H(z)/F_a(z)

恰为**剩余ξ零点**的normalized paired product，不含未定zero-free因子。剩余集保持±与共轭对称，允许ξ重根和离线零点；并没有先用RH。

在实x>0，剩余critical pair给1+x²/γ²。一个离线quartet w=±α±iγ给

    1+2(γ²−α²)x²/(α²+γ²)²+x⁴/(α²+γ²)²。          (12)

全部|γ|≥|α|的quartet因子≥1；因|α|<1/2，违反此条件的低频quartet只有有限个，每个为复模平方并最终≥1。这些有限例外不得先删去，但不会提供x→∞的负补偿。于是R_a(x)最终≥1；若余集非空，任取一个pair/quartet，其余因子最终≥1，被选因子给

    R_a(x)≥c x²，x充分大。                            (13)

若余集为空则R_a≡1。有限非空余集是even整数degree多项式；无限余集更可任选任意多有限因子，推出比任意先固定多项式更大的最终lower。实际只需(13)，故不依赖稀疏余零点的未知计数。

另一方面，实轴Stirling与ζ(x+c)→1直接给

    ξ(x+1)/ξ(x+1/2)~(x/(2π))^(1/4)，
    ξ(x)/ξ(x+1)=O(x^(−1/2))，
    H(x)/F_a(x)~C_a e^(−ax)x^(3/4)，
    C_a=G_a(0)(2π)^(1/4)/ξ(1/2)>0。                 (14)

第二项在(1)中相对第一项至多O(x^(−1/2))，含a=0；没有漏掉两个移位项之间的主消去。若a>0，(14)趋0，违反R_a最终≥1；若a=0，其x^(3/4)既不等于余集空时的1，也不容非空余集的(13)。故假设不成立，且

    q(a):=Q_a(P)=Σ_γ |hatP(γ)|²>0，所有有限a≥0。      (15)

这就是同一实际Pan上的严格泄漏，不是仅“辅助函数不同”。

## 6. 全a同一个合法compact、精确双pole-zero反测

由(7)–(9)及P∈S_exp⊂S，qbar(a)=q(a)/(1+a)在A连续，

    qbar(∞)=2||P||²_du>0。

结合(15)与紧性，有

    q_*:=min_(a∈A) qbar(a)>0。                         (16)

没有数值q_*或有效最小化/零点误差率的声明。它是一个全截断参数的严格正minimum，非仅固定紧a集。

取实χ∈Cc∞、χ=1于0附近，固定compact degree-dualsη_±，μ_σ(η_τ)=δ_στ。可由非负偶bumpρ及τ_1ρ构造：矩阵m[[1,e^(1/2)],[1,e^(−1/2)]]非奇异。令

    r_R=χ(v/R)P−μ_+(χ_RP)η_+−μ_−(χ_RP)η_−。        (17)

r_R为real compact smooth源，μ_±精确为0，且r_R→P于S_exp。它一般不是Pan，也不是新的关系定义。两种连续性分开支付：原Q_ζ在S_exp给Q_ζ(r_R)→0；统一(7)和Schwartz卷积连续性给

    sup_(a∈A)|Qbar_a(r_R)−qbar(a)|→0。                  (18)

因此任给m_0>0及0<ε<1/3，可先选一个R并固定r=r_R，使

    inf_(a∈A)Qbar_a(r)>(1−ε)q_*，
    |Q_ζ(r)|<εm_0q_*。                               (19)

没有使R与a或stage同时成长来藏缺陷。双pole只是在(17)这个合法源上精确为0，未从W_ζ定义中删除。有限频率截谱若也使用，只需再选一个R_freq共同阈值使其归一化能量lower>(1−2ε)q_*，全部a同时成立。

## 7. 正混合、任意归一化和非负添加：最强直接量词

为清楚容纳a→∞，直接使用normalized V_a，a∈A，包括已付极限V_∞=2δ_0。任意原W_a的正混合/缩放ω等价于V_a的正混合ν=(1+a)ω。其真实总质量为

    m=ν(A)=∫_(a<∞)(1+a)dω(a)，                       (20)

另可在a=∞赋任意非负质量。这里不设rank、组件数、连续/离散、费用、总质量upper、locality或boundedness限制。无穷能量不能匹配有限target。

允许stage j甚至每个物理源分别选择正ν_(j,r)，并加任意per-source A_j(r)≥0。对先按m_0,ε选好的同一r，只要最终m_j(r)=ν_(j,r)(A)≥m_0，则

    E_j(r)=∫Qbar_a(r)dν_(j,r)(a)+A_j(r)
           >(1−ε)q_*m_j(r)，
    E_j(r)−Q_ζ(r)>(1−2ε)m_0q_*>0。                 (21)

这不要求修补为quadratic、linear、bounded或收敛。共同线性positive-type分布的D′匹配由φ=r*r*即被否定；源适应若破坏共同线性分布，只排其在这个质量条件下的全部fixed源能量匹配，不冒称它已定义D′对象。全部mixed/complex匹配包含该对角必要条件。若组件频谱各截断，(21)相应只用实际位于足够大frequency cutoff部分的≥m_0质量；其余正量可放入A_j，不能偷换为各标签分别cofinal。

**共同混合的更强必要结果。** 若ν_j对源共同且添加A_j对全部源非负，完整fixed源目标匹配迫m_j→0。否则有子列m_j≥m_0，选(19)同一个r，(21)与该子列收敛矛盾。由统一(7)，m_j→0又使period基部∫V_a dν_j→0于S′。因此任何成功非负添加规则必须让整个period部分消失，再由添加部分承担全部目标；不是period留下非零份额的修补。

**无添加的共同正混合完全不能逼近。** 取537固定小窗内一个非零compact complex h，c_h=Q_ζ(h)>0。由(7)有sup_a Qbar_a(h)≤C_h<∞。若共同混合在h上匹配，

    m_j≥c_h/(2C_h)>0，最终成立，                      (22)

与前段必要m_j→0矛盾。这覆盖任意a_j→∞、任意positive scalar normalizations和任意正参数混合；不必预设保留质量。即使μ的总原始质量趋0而∫(1+a)dω仍非零，(21)仍探测到；归一化至2δ_0没有逃过。

不能把(22)跨源借给逐源适应ν_(j,r)，因为h与r的权重可不同。源适应情形只按(21)在已选r的实际质量条件消费；不声称所有逐源非线性规则失败。频谱截断没有共同cofinal阈值/质量时，也不由(22)自动闭合。

**同一个compact线性separator。** 上述完整正锥失败还可一次收口为固定测试。保持上述h、c_h、C_h，令δ=q_*/(2C_h)>0，再选一个固定Pan-crop r使inf_a Qbar_a(r)>q_*/2且Q_ζ(r)<δ c_h/2。则

    Φ=r*r*−δ h*h*∈Cc∞，
    V_a(Φ)=Qbar_a(r)−δ Qbar_a(h)≥0，所有a∈A，
    W_ζ(Φ)<−δ c_h/2<0。                             (22a)

故所有共同正混合在同一个compact linear测试上均≥0，而目标严格<0；无需先假设混合质量lower。这是difference of squares，非single卷积平方或pointwise正测试。r精确双pole-zero；h按537任取非零小窗源，没有额外宣称h或Φ的双pole矩为0，完整Q_ζ(h)仍保全部pole。源适应在r与h使用不同权重时不能把它们拼成共同V(Φ)。任意额外positive-type A可在Φ取负值，因此(22a)不直接排所有正添加；其准确必要结论仍是上一段period加权质量必须趋0。该separator、anchor推论与(21)同一链，不再另领弱后继。

## 8. Signed必要负响应与原norm

保留(19)及m_j(r)≥m_0，但允许signed/coherent总修补A_j(r)。成功target匹配时最终误差<εm_0q_*，必要

    A_j(r)<2εm_0q_*−(1−ε)q_*m_j(r)
           ≤−(1−3ε)q_*m_j(r)
           ≤−(1−3ε)m_0q_*<0。                       (23)

这是同一个fixed源上的必要负响应，不是signed机制不可能或充分构造；若m_j增长，第一行还保留了相应线性增长的负费用。仅另有实际实现A_j(r)=<r,T_jr>、T_j是原du Hilbert空间上的bounded Hermitian算子时，才可推出

    ||T_j||>(1−3ε)q_*m_j(r)/||r||²_du。

没有该实现、不同native metric、非线性源适应或无界形式时，只能称(23)负响应。Schwartz tail与period内部变量没有支付全线du/Dlog无费norm运输。

## 9. 其它clock、zero-free因子与准确逃逸

乘任意逐stage zero-free整因子不改零点/重数，不能修复以上谱目标；但不得再把改变后的二阶导数冒作原谱逆平方矩。本文没有要求这类改后函数自己收敛。

固定b>0时F_(a,b)(z)=F_a(bz)的全部零除子若与经典H完全相同，even/order≤1/归一化将迫函数相同。实轴渐近的xlogx系数先迫b=1，线性x系数再迫a=0，最后logx的余3/4仍矛盾。因此没有一个固定(a,b)能逐点给同一完整零谱身份。这个直接必要比较**不证明**任意b<1的Pan泄漏、b-混合/positiveadd或b退化的joint family失败；不得把singleidentity扩成本文未付的共同反测。

仍未排：实际signed/coherent负响应及其新算术机制；不同源域/target/额外data；自然clock之外的变尺度正混合/适应；来源公式以外的非rank2/不同integrals。共同positive-add成功允许period整体消失，但这恰要求独立添加承担全部W_ζ，不是本period成功逼近。逐源适应无共同保留质量也保其准确范围。未排自由不是已成功输入，不自动取得参数/新rank/作者后章/引用预算。

没有新的primitive/principal/整section/mixed RR、dangerous signed core/cross有利净号或成长Ξ。Whole542+555→557 leading4/5仍仅负惯性UPPER；本文全a及正修补边界不自动通过Goal第3门，长期Goal保持完整强度/open。真正新净值与是否统一一个完整实际失败研究由strongest-old分工、不同fresh及root实际消费；phase/Hadamard/RvM/旧Pan/紧性/正混合不分别计轮。

## 10. 实读输入与终态

本稿只写此独占文件。未新web/PDF/作者proof/refs/数值/Git、无后台进程。§2原件现已实际全文读/hash，本文前件全部闭合；出稿仍须不同fresh/root消费，不代结算。下表仅标实际版本和使用范围，不假称重审全部嵌套外部证明。

| 实际输入 | 实读范围 | bytes | raw SHA256 |
| --- | --- | ---: | --- |

| goals/GOAL.20261027.md | 全文/完成门与流程 | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| goals/contracts/C062-prime-ising-critical-positive-distribution.md | 全文/停止与计轮边界 | 1547 | `16a49214fa90bb0d94477789bf0abc2ba652c9ea6785963e3a2ebabee3678626` |
| goals/reviews/2026-10-29-prime-ising-599-settlement.md | 全文/最新因果范围 | 2983 | `e0117c962f4ed259d8432e5a665917e83a26d563678e8e4121ecc98ff2245679` |
| reviews/2026-10-29/post-599-input-choice/next-rank-two-period-math-admission.md | 全文/本门义务 | 4122 | `35456a67bfa8143c0828242326cf9f36f2ee83fadd039f603b7c43cc5d2ff8fc` |
| reviews/2026-10-29/post-599-input-choice/lagarias-suzuki-source-admission.md | 全文/准确公式和来源范围，未读新PDF | 2185 | `3bd17096bfa34117d9bfb5cf25c6f42d91c1c1e33bb86c2a828b46b895a7b828` |
| reviews/2026-10-29/rank-two-period/positive-zero-and-phase.md | 全文/独立核本文全部phase及simple前件 | 13204 | `f840095ae6d271f7a9acc84bde7f259c07d7bbe2ab2f9ec763d4aa7167ea67b2` |
| notes/405-f1-adelic-restriction-moments-and-radical.md | §§1–5：S_exp/完整连续性/真实Pan | 14633 | `fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d` |
| notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md | §1及§§2–3开头：physical Fourier/actualQ及norm角色 | 6613 | `35a40c35d1eaa7fafb462361ddef1bfb9643402b5670f832b9142aeb4b74abce` |
| notes/537-source-exact-weil-window-positive-tail-admission.md | §§1–2完整源正性statement与完成域；不重放数值 | 8155 | `269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8` |
| reviews/2026-10-29/prime-ising-critical/positive-zero-distribution-and-weil-target.md | §§5–8真实Pan/精确crop/修补量词；不借其Ising/ODE谱 | 15907 | `a81dda0f1f5ab745a689db39ae0c303a6b15efdf037a2e8d7f4bf4c95c8260b7` |

UTF-8/LF原件已冻结。数学净值/是否一个完整实际失败迭代、STATE/唯一cadence/库/发布均由root据不同fresh和最强旧另行结算。
