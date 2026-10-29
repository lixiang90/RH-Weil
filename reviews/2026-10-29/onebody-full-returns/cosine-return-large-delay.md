# 单素数全返回：最强旧恢复与固定源窗的全 L² 预算

2026-10-29；`/root/onebody_full_returns` 独占原稿。父任务为已保存4340-byte admission 的 actual large-prime/fullreturn 首检；不是恢复C064预算。本文没有修改STATE/cadence/Goal/Git/文献库，没有新web/PDF/章节、数值或样本选择。

**必须先更正新颖性前件：533早已支付每个fixed compact smooth源的p⁻²渐近及single-p绝对可求和。** 因此原准入声称fixed-r强化率未付过弱，且j_X[r0]的同量级增长已由533＋585/589直接包含，不能再领602。

本稿另从完整cosine-return公式独立得到一个不同拓扑的预算：对每个固定有界源窗I，存在C_I及p_I，使实际single-p差额在全原complex L²(I)上的有界延拓满足

    ||D_(p,I)|| ≤ C_I (1+log p)/p，p≥p_I，
    D_(p,I)[r]=t_p[r]−t_empty[r]  （原ordinary trace先在Dlog成立）。       (A)

这个预算不需要源导数，允许源、频率和全部complex系数随p变化；p-rate弱于533的fixed-smooth p⁻²，但其全du单位球量词不同。它**没有**给∑p||D_p||<∞，也没有给p²D_p的norm渐近。由(A)可付所有empty-base onebody源算子之和O_I(log X)，从而完整≥2 connected source算子与actual K_X的差在全du单位球上O_I(log X)。其定理证明在下文闭合，是否相对最强旧有真正净增仍交root/fresh消费；这里不把旧fixed-r manybody后果冒充新结果，不预授C065/602或Goal完成。

## 1. 恢复、最强旧与实际范畴

已读AGENTS、README/实际STATE，运行check后show，读完整G20261027、停止C064、AK、macro frontier当前摘要和4340-byte admission。恢复基线0c4f、same runtime1793085111、cadence3/history65/latest601/formal20、Goal三门open。父现场已核运行Goal及73228ef实际远端；本子任务没有自行认证父API或改运行状态。

先实读535和其trace-domain proof，随后全文核531/532/533/534及c006 direct-increment原稿。533 §1写出

    t_p[g]−t_empty[g]=p⁻² A[g]+O_g(p⁻⁵ᐟ²)，
    Σ_p |t_p[g]−t_empty[g]| <∞，

且direct稿开头及§5/§6明确适用于**每个fixed compact smooth g**，特别而非仅限冻结两patch/矩零源；余项在固定支持的足够高Sobolev有界集统一。534的降级针对whole-L²单位球的低cycle/角迹消费，不撤销fixed-smooth定理。故当前admission未恢复最强旧，需冻结其fixed-r“未付/新归因”读法。

另一方面，533 §5的紧性只排除p²D_p在whole-L²上的norm首项渐近；534明确把uniform绝对上界/可求和norm留open。本稿(A)不与其矛盾，也不自动支付更强可求和norm。

## 2. 同一物理对象、普通迹与overlap身份

用531的共同物理空间H=L²((0,∞),dx)，unitary log坐标使U_a成为平移；physical dilation为U_a f(x)=e⁻ᵃᐟ² f(e⁻ᵃx)。F是核2cos(2πxy)的自伴unitary cosine Fourier。L=1_(0,1)，H_+=I−L，P是真实实位Sonin投影。对prime p，q=p⁻¹ᐟ²、a=logp，

    B_p=I−qU_a，G_p=(P B_p*B_p P)|RanP，
    Π_p=B_p P G_p⁻¹ P B_p*，Π_empty=P，
    F_p=B_p F B_p⁻¹，K_p=L F_p L。

F_p是自伴unitary involution；全部G_p及K_p的实际返回都保留。源是560原physical r（原raw f=e⁻ᵘᐟ²r），A_r=∫r(u)U_u du，t_p[r]=Tr(A_rΠ_pA_r*)。没有额外半密度或1/(2π)更换。

531/560已给r∈Cc∞及原zero-extension Dlog的A_rΠ_p∈S2，故两源夹乘为S1。532 §5已在一般smooth源上识别

    t_p[r]=q_Γ[r]−P_p[r]+E_p[r]，
    E_p[r]=Tr(A_r O_p A_r*)，
    O_p=Π_p+L+F_p L F_p−I。

其中P_p含所有logp·p⁻ⁿᐟ²真实proper powers，Γ为actual2θ′/完整FP-contact。这个身份不是仅在535冻结moment源上才成立。双pole属于完整Q而不在t_p中；共同相减时保其相同值而消去，不把pole删出目标。

对于real smooth r，Z_r=A_r*A_r与F_p交换，535 trace-domain proof给完整普通overlap迹

    E_p[r]=2 Re Tr_L[h(K_p) T_r F_p L]，
    h(K)=K(I−K²)⁻¹，T_r=L Z_r H_+。                         (1)

以下独立支付T_r自身S1，故(1)可直接按bounded×S1消费全部返回，不拆尚未付的角级数。若logp大于源相关跨度W，则所有P_p项exact0，故

    t_p[r]−t_empty[r]=E_p[r]−E_empty[r]。                     (2)

这一步保同一个r，不是把r换成p依赖的receiver或新patch。

## 3. 关键无导数引理：T_r本身是uniform S1

固定I长度至多W>0，r∈L²(I)。在unitary log空间，平移r的源参数不改变Z_r；可在证明中把r移到[0,W]，记所得源为h。A_h=U_cA_r，故A_h*A_h=Z_r，||h||2=||r||2。此为相同Z的代数表达，不换actual trace比较的测试源。

令E=1_[0,W]为log空间投影。因h支持[0,W]，A_h H_+的输出在正半线，而A_h L与它可能相交的输出只在[0,W]。因此精确有

    T_r=L A_h* E A_h H_+
       =(E A_h L)* (E A_h H_+)。

两因子是普通convolution的真正HS算子，并可直接核

    ||E A_h L||HS²=∫₀ᵂ t |h(t)|²dt，
    ||E A_h H_+||HS²=∫₀ᵂ (W−t)|h(t)|²dt。

于是

    ||T_r||S1 ≤ W ||r||2²。                                  (3)

没有使用源导数、H¹源范数或whole-HS的错误断言。这也支付硬L/H边界；不需在源/边界上施加Dirichlet条件。

在physical x坐标，χ_r(t)=∫r(u+t)overline(r(u))du连续、support⊂[−W,W]、||χ_r||∞≤||r||2²。T_r的核为

    T_r(x,y)=χ_r(log(x/y))/sqrt(xy)，0<x<1<y。

它只连接矩形x∈[α,1]、y∈[1,β]，α=e⁻ᵂ、β=eᵂ。该核在矩形上连续且幅度≤C_W||r||2²；它不必有源导数。本稿后面只在cosine dressing造成的那一坐标上求导。

## 4. 固定实位全resolvent与真正二阶trace余项

记K=K_empty=LFL，κ=||K||<1。K为光滑核紧算子，严格gap由旧530/531的Fourier整延拓唯一性支付。令D=F_p−F、N=L D L。由F_p=(B_p/B_p*)F，

    ||D||≤2q/(1−q)，||N||≤||D||。                              (4)

选p≥p_κ，使||D||≤(1−κ)/2，则||K+N||≤κ₁=(1+κ)/2<1。两个完整resolvent

    R_ε=(I−εK)⁻¹，R_(ε,p)=(I−ε(K+N))⁻¹，ε=±1，

都有与p无关的共同bound。h=.5(R_+−R_−)，其真正非交换first variation为

    Dh_K[N]=.5(R_+ N R_+ +R_− N R_−)。

由两次resolvent identity，而非形式截角，

    ||h(K+N)−h(K)−Dh_K[N]||≤C_κ||N||²，
    ||h(K+N)−h(K)||≤C_κ||N||。

将其用于(1)，所有迹因(3)单独为S1，得到

    .5(E_p−E_empty)=Re ℒ_r(D)+O_κ(||T_r||1 ||D||²)，
    ℒ_r(D)=Tr_L[Dh_K[N] T_r F L]
                  +Tr_L[h(K) T_r D L]。                       (5)

交叉项(h(K+N)−hK)T_rD的trace亦由(3)付O(||N||||D||)。因此(5)余项为C_W,κ||r||2²/p。这里保持了全部actual inverse，绝非把bare低cycle当fulltrace。

## 5. First variation的一坐标C1核足够

固定K的kernel为2cos(2πxy)，在[0,1]²光滑。由

    R_ε=I+S_ε，S_ε=εK+K R_ε K，

S_ε有光滑核；每个有限端点导数由固定cosine row的L² norm及||R_ε||控制。不需prolate展开或source导数。

令B_r=T_r F L。其核是

    B_r(x,z)=∫₁ᵝ T_r(x,y)·2cos(2πyz)dy，x,z∈[0,1]。

因此B_r在输出x连续、在**输入z**有一阶连续导数，且

    sup|B_r|+sup|∂_z B_r|≤C_W||r||2²。

C_ε=R_ε B_r R_ε也有同样的一坐标C1 bound：展开(I+S)B(I+S)，对输入坐标求导只落到B或右侧S，左侧S仅有界积分。依(3) C_ε仍为S1。合法循环后第一项为

    .5 Σ_(ε=±1) Tr_L[N C_ε]。

其核配对是D(x,y) C_ε(y,x)，正好可对C_ε的**输入x**分部积分，不需要∂χ_r。

第二项h(K)T_r的核在输出x有一阶连续导数，输入y局限[1,β]；因为h(K)=.5(S_+−S_−)本身光滑，所以

    sup|h(K)T_r|+sup|∂_x(h(K)T_r)|≤C_W,κ||r||2²。

这项的trace核配对位于[0,1]×[1,β]。所有有限cosine-scale与这些kernel的trace配对可由HS×HS的普通核乘积验证，未对分布级数逐点求和。

## 6. 真实p所有scales与坐标轴费用

对λ>0记F_λ核为2cos(2πλxy)。实际operator-norm identity为

    D=−p⁻¹F₁ +(1−p⁻¹)Σ_(n≥1)F_(pⁿ) −p⁻¹F_(1/p)。           (6)

注意high-scale核没有额外p⁻ⁿᐟ²幅度；其full operator norm恰λ⁻¹ᐟ²，所以(6)在operator norm绝对收敛。TC test允许与trace换序。

若f在[0,1]²连续、仅对x有连续一阶导数，则λ≥2时

    |∬ f(x,y) cos(2πλxy)dxdy|
       ≤ C (||f||∞+||∂_x f||∞)(1+logλ)/λ。                   (7)

证明：y≤1/λ的strip直接付1/λ；y≥1/λ时对x分部积分，边界及积分余项≤C/(λy)，再积分y给logλ/λ。没有丢去xy=0附近。若y∈[1,β]，同一积分无1/y奇性，仅O_W(1/λ)。

用(7)于第一项的C_ε(y,x)，用无log版本于第二项，得到每个high-scale contribution≤C_W,κ||r||2²(1+logλ)/λ。λ=1及λ=1/p低核在实际有限矩形上幅度≤2，乘p⁻¹均为O_W(||r||2²/p)。因此

    |ℒ_r(D)|≤C_W,κ||r||2² Σ_(n≥1)(1+nlogp)/pⁿ
                       +C_W,κ||r||2²/p
             ≤C_W,κ||r||2²(1+logp)/p。                       (8)

结合(5)的fullreturn二阶余项，(2)给(A)在real smooth源成立。实际560的ρ_p、ρ_empty均实偶，故complex r=a+ib的t差为a与b的t差之和；不能对complex r直接假设Z_r与F_p交换。于是相同bound作用于全complex smooth源，且constant仅依固定I/κ。

由全L² bound唯一延拓得到D_(p,I)；原Dlog trace身份通过原core密度和Dlog连续性与此延拓一致。不声称两个独立正迹对任意裸L²源都有限。对于有限个p<p_I，532的源compact余项加有限prime-shift型给D_(p,I)有界；head费用并入C_I。

## 7. 新旧拓扑分开及cofinal全算子后果

(A)是whole-du单位球上O_I(logp/p)，不是533fixed-smooth p⁻²的改进；后一更强p-rate仍应先恢复。由533，当前admission的fixed r0 onebody和早已绝对收敛，故

    j_X[r0]=t_X[r0]+O_(r0)(1)，

同585/589两边界均为√X/log²X量级，属于old直接后果。更强地，533对fixed有限组的所有complex极化源给onebody Gram一致有界；587各fixed derivative空间的共同lower减去有界矩阵后仍成立。不能把这些强旧后果拆新轮。

本稿(A)若经root/fresh接受，真正不同后果为**整个fixed-I source operator**预算。记560的K_(p,I)、K_(empty,I)，定义

    K_(≤1,X,I)=K_(empty,I)+Σ_(p≤X)(K_(p,I)−K_(empty,I))。

D_(p,I)=−P_(p,I)+K_(p,I)−K_(empty,I)，其中P_p为所有actual properpower-shift型。对fixed I，仅pⁿ≤eᵂ能有相关，故Σ_pP_(p,I)是X一致有界的有限visible型。由(A)及Chebyshev部分求和Σ_(p≤X)(logp)/p=O(logX)，

    ||K_(≤1,X,I)|| ≤ C_I(1+logX)。                            (9)

精确Möbius身份给full≥2 connected source算子

    K_(J,X,I)=K_(F_X,I)−K_(≤1,X,I)，
    ||K_(F_X,I)−K_(J,X,I)|| ≤ C_I(1+logX)。                   (10)

(10)对全部complex du单位源及随X移动的source/frequency/coupling同时成立，在同一fixed I上是全算子差；比仅fixed smooth测试的有界onebody响应多了uniform拓扑。它不等于新whole K_X上/下界或Weil正性；K_J本身是需与正迹相消的actual compact误差部分。C_I不对I成长统一，不能代I_X/通常Ξ预算。任何对新颖性/实际净增的判定应先核其它旧exact分解，不能只拿本文(9)标签绕过最强旧。

## 8. 终态、来源及计轮边界

任务实际执行并发现了原4340准入遗漏533强旧的问题；应先冻结其“fixed-r统一rate未付/新manybody归因”读法，追加更正，不改原件。本稿给固定窗whole-L² budget的自含fullreturn推导。Root发现并接受旧533范围纠错后，已另写whole-window-onebody-readmission并登记C065，明确这是不同统一norm责任；该登记不回填原4340题，也不预认本稿root消费/602或Goal完成。

长期principal/sections/mixedRR、全成长corecross/Ξ及whole4/5负惯性UPPER未改；三完成门open。无新primary/PDF/作者章，也无数值或后台进程。独立数学原稿存在不代root消费或最终计轮。

实际阅读全文：AGENTS/STATE、Goal/C064、AK/当前frontier摘要、4340 admission；530/531/532/533/534/535、c007 trace-domain、c006 direct-increment；585/587/589全文；560 §1实际字典；最后读取parent明确重准入和C065以核本稿责任范围。没有以旧输入hash表冒称重新审完所有nested source/audit。必要raw指纹列于末。


## 9. 534/535范围与新旧归因的最后核对

534确已支付whole-source的一些lowcycle砖块、M0的S1、Mδ的HS与H3的localized TC乘积；但明确没有完整D_p的uniform norm。535随后在fixed smooth源上支付实际h(Kp) overlap trace及bare/return分离，未把常数去导数后宣告whole du单位球bound。本稿不重新计算这些砖块或把smooth traceclass本身计功：新证明的实质是(3)的无导数HS×HS因子，配合(5)全op二阶余项和(7)所需C1仅由固定cosine/resolvent在一个坐标产生，最终一次合成完整source operator的(A)/(9)/(10)。仅说旧已付fulltrace或已有同一resolvent身份，不等于已付这些uniform全单位球量词；反之若发现旧完整exact估计已蕴含(A)/(9)/(10)，root仍应归old0。

旧533还有比j_X[r0]更强的即时后果：对587任一先fixed derivative空间E_(d+1)，用533于其固定有限个complex极化测试，onebody Gram逐元素绝对收敛，从而uniform-X有界。因此旧587的整个moving-coefficient lower减有界矩阵后仍给J_X在该E上的同量级lower，且每个fixed正source特征值的发散亦已包含。新定理不能把这些old finite-Gram后果冒称新增。新全source operator差O_I(logX)才涉及不预先固定finite-dimensional源族的统一coupling。

## 10. 实际输入指纹

Raw SHA只认证版本。旧数学作为已经root支付的输入使用，未重审全部nested外部证明；本任务没有取得或阅读新的外部原件。

| 资产 | bytes | SHA256 |
|---|---:|---|
| `goals/GOAL.20261027.md` | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| `goals/contracts/C064-haran-integer-affine-fold.md` | 2047 | `765aa6546b77297a475a0003ce6c4a362736915ae36eb014874d3f3d21971399` |
| `reviews/2026-10-29/post-601-core-input/cofinal-onebody-first-gate-admission.md` | 4340 | `fad417627223fd636047793c182348c08179293d8b50b1c65eb691a458148a8f` |
| `notes/530-archimedean-sonin-prime-compact-repair-boundary.md` | 8695 | `7aba1a289da2f40edbc4ba776b687aa9f80fb5bad39a0374e1bcbf99785d3bbd` |
| `notes/531-semilocal-sonin-positive-trace-and-non-hilbert-schmidt-cutoff.md` | 7870 | `11989cb45e7d72b6b5f9c166ac5d202975bf9127db3d07a6c496e16d8aabba51` |
| `notes/532-actual-sonin-prime-symbol-and-compact-weil-bridge.md` | 8516 | `dc9ff79c622ed692edfd393c2851e5cc7fcab0a7f5fe41cce82ba69b45a82f09` |
| `notes/533-actual-late-prime-sonin-boundary-square.md` | 9978 | `3b15593b57a0b5dab22409df4baac440fc04491fcff1b2f10b6451404b7ca478` |
| `notes/534-actual-uniform-sonin-subterms-and-trace-consumption-gap.md` | 8097 | `19fa13a6fda7d3deaf84c78a2794d759ca784c3e0248fa7f904adca60d554c28` |
| `notes/535-actual-first-prime-sonin-log-resonance-and-indefinite-error.md` | 9910 | `e83c3e080d19c2534425fb3c0e469367012f6c566a470b3baba703fb6def146f` |
| `reviews/2026-10-14/c007-sign/trace-domain-proof.md` | 5507 | `bae082f91a0f01a44fa3e3d1e9e0685bfa28e63a8dca32b822f395ad7b306094` |
| `reviews/2026-10-14/c006-late-prime/direct-increment-audit.md` | 10415 | `8ee99cdcc4bba7d7da565169bfc38bf6d1469192c73db7ea715251d3f6294ee9` |
| `notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md` | 9263 | `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3` |
| `notes/585-cofinal-sonin-fixed-source-trace-lower-and-core-error-fee.md` | 7857 | `5dca916d978eef599587ff4c6ce34144f814ddec0567a4c1b2314dcd71cd01af` |
| `notes/587-actual-sonin-moment-spread-and-growing-source-rank-necessity.md` | 8681 | `e4d30cfb6d07299386014cb4c4e3e3979ab5111264355dfb37b24629f121ac82` |
| `notes/589-sonin-zero-mean-upper-and-scalar-rank-one-limit.md` | 7185 | `c491012226713baf0eecff045338563d4e440c6a1bde9eea0d9ccf661b958bc5` |

本稿终态：只写本文件，无后台进程；原件存在不代root或different fresh的消费，不单独操作计轮。
