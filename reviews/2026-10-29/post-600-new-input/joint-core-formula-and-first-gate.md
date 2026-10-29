# 新实际 Euler gauge-relative Gram：一个已执行的迹域首检

2026-10-29；`/root/new_joint_core_formula`独占稿。**结论：构造了下述具体 source-dependent Euler 共轭和 relative Gram，但其未减 bulk 的 ordinary relative determinant 在任意小非零源参数上已经不满足紧扰动域。** 首检由560已付 carrier 和初等移位代数直接闭合，不能作为新的 dangerous-core 净估计或601。建议只按一个实际新公式的0准入止损消费，不准C064，不派det₂／精度／第三prime／新paper继任。不是所有relative determinant或有符号修补失败。

## 1. 恢复与最强旧基线

实际读AGENTS、goals/README和STATE，执行`research_state.py check`后`show`，读完整G20261027、停止C063、AI、600结算和宏观前沿当前段，并观察工作树。恢复时唯一cadence为2/history64/latest600/formal20；父现场已核同runtime1793085111 active及600最终61d46e9发布，本子稿未自行live核父Goal／远端，也不创建或修改Goal。上一轮600为progress，不把其全a正锥失败拆成后继。

先全文读前轮14149-byte `post-599-input-choice/signed-core-actual-comparison.md`。其中共同endpoint的signed telescope上费、whole-K每fixed正谱发散、safe-high实际运输和595物理正点／gap均是强旧；本稿没有重做库存或再领取较弱scalar后果。当前仍欠560同一源上t−K的独立有利比较，而不是再估计一个大正项。下面尝试的是一个明确不同的算子源变化，并实际执行最便宜的合法性检查。

为避免把旧source Gram改名，另读已有Sonin determinant准入：旧对象在receiver谱坐标使用`M_(hat r)`，weighted-L¹夹源使其ordinary determinant合法，mixed Levi逐层恰591 covariance，已0止。这里故意用**原物理log坐标的pointwise `M_r`**共轭Euler算子；它不等于receiver `M_(hat r)`，因此不能直接援591判同一个curvature，但也不能继承其trace-class域。

## 2. 唯一新公式：共同物理Hilbert空间上的Euler共轭

保560的H=L²(R,dy)、U_ell f(y)=f(y−ell)、arch Sonin投影P及M=RanP。对任意先fixed finite F，

    B_F=product_(p∈F)(I−p^(−1/2)U_logp)，
    G_F=(P B_F*B_F P)|_M。

G_F为严格正、有界可逆，Euler因子不是酉。给实际物理源r∈Cc∞(R;R)，以M_r表示pointwise乘法，定义整个complex参数的明确curve

    B_(F,z)[r]=exp(zM_r) B_F exp(−zM_r)，
    G_(F,z)[r]=(P B_(F,z)[r]*B_(F,z)[r]P)|_M，
    D_(F,z)[r]=G_F^(−1/2) G_(F,z)[r] G_F^(−1/2)。       (1)

M_r有界，z↦B_(F,z)为operator-norm entire；其inverse也有界，故G_(F,z)是M上的真实严格正Gram，而不是形式kernel。其费用先依||r||∞、|z|、finite F；不能由“r∈Cc∞”把它改称原du或zero-extension Dlog单位球的统一费。原物理r与下文receiver测试向量亦为不同角色。

若D_(F,z)−I∈S₁，可以尝试ordinary det_M D_(F,z)，把其相对Gram metric的source Hessian作为joint signed候选；若要取det_p，则至少须D−I∈S_p。这个域是**先决条件**，不因G_(F,z)>0自动成立。此处不声称曲率已经等于完整Weil型，不把logdet的定义当principal／section／mixed RR身份。

本式不是K=t−Q+pole或未知PSD的重命名。它只用已知B_F和源r写成了实际bounded算子curve；最便宜可判门是它是否真正进入拟用的Fredholm determinant域。下面已经执行这一门。

## 3. 在一个固定prime、一个固定合法源上的精确计算

取F={2}，ell=log2、a=2^(−1/2)、B=I−aU_ell，令z=iτ，τ∈R。因r real，E_τ=exp(iτM_r)为实际酉算子，有

    B_τ=E_τ B E_τ*，
    B_τ*B_τ=E_τ B*B E_τ*，
    B*B=(1+a²)I−a(U_ell+U_(−ell))。

共同Sonin压缩P仍固定，不能把E_τ跨P消去。移位方向精确为

    E_τ U_ell E_τ*=M_(exp(iτ[r(y)−r(y−ell)])) U_ell。

故全H上的差L_τ=B_τ*B_τ−B*B确为

    L_τ=−a{ M_(exp(iτ[r(y)−r(y−ell)])−1) U_ell
              +M_(exp(iτ[r(y)−r(y+ell)])−1) U_(−ell) }。  (2)

这里finite bandwidth只属于B*B这一中间Gram，不是在完整投影／Weil字典中删proper powers；G_F inverse仍保全部returns。

选J=(3ell,3ell+ell/10)，三个patch J−ell、J、J+ell两两不交且都在正半线。取一个real r∈Cc∞((0,∞))，使

    r=1 on J+ell，r=0 on J and J−ell。                (3)

若要求Weil的双degree平衡，也可保持(3)并精确取

    mu_±(r)=integral r(y)exp(±y/2)dy=0。              (4)

具体做法是先取满足(3)的cutoff，再在远离上述三个patch的两个positive紧区间各放一个同形平移bump。两个mu矩的比值因平移不同而不同，故2×2矩阵非奇异，唯一real线性组合消去两矩；这些远处修正不改变(3)。r仍fixed、compact smooth、有限原du与Dlog范数。这里没有称r是405的Pan，也不以(4)定义新关系。

令

    f_R(y)=exp(iRy)1_J(y)/sqrt(|J|)， R→+infinity。    (5)

它是辅助H向量，不是把另一类Weil源偷偷换进目标。其norm为1、weak→0。U_ell f_R支撑在J+ell、U_(−ell)f_R支撑在J−ell；代(3)入(2)逐项准确得到

    L_τ f_R=−a(exp(iτ)−1) U_ell f_R。                (6)

Backward项在J−ell上系数恰为0；没有相位平均或symbol近似。

## 4. Actual Sonin压缩后主项仍非紧

只用560 §2已经支付的arch carrier：对每个fixed有限区间K，T_R=Gamma(R)→∞，

    ||(P−1_[0,T_R])exp(iRy)1_K/sqrt(2pi)||
         ≤C_* R^(−1/4)。                            (7)

这里Gamma是原actual2theta′；没有带Euler相位的clipping偷渡。因为J和J+ell都固定在正半线，R充分大时均落在[0,T_R]，所以

    ||P f_R−f_R||=O_J(R^(−1/4))，
    ||P U_ell f_R−U_ell f_R||=O_J(R^(−1/4))。          (8)

第二式只是同一个carrier用于J+ell，保U_ell产生的unit-modulus相位。令g_R=P f_R∈M，则g_R weak→0、||g_R||→1。写C_τ=G_({2},iτ)[r]、G=G_{2}，由(6)及L_τ fixed bounded，

    (C_τ−G)g_R=P L_τ P f_R
       =−a(exp(iτ)−1) U_ell f_R+O_(r,τ,J)(R^(−1/4))，
    ||(C_τ−G)g_R||→a|exp(iτ)−1|。                    (9)

取任意0<|τ|<2pi，右端严格正。因此C_τ−G不是compact；实际上

    ||C_τ−G||_ess≥a|exp(iτ)−1|。                     (10)

尤其τ=pi给2a，但失败已存在于任意小非零τ，不能仅保留“源参数0附近”来修复ordinary定义。

由(1)，

    C_τ−G=G^(1/2)[D_τ−I]G^(1/2)。

G^(±1/2)均为M上bounded inverse，所以D_τ−I compact当且仅当C_τ−G compact。又||G||≤(1+a)²，直接有

    ||D_τ−I||_ess≥a|exp(iτ)−1|/(1+a)²>0。            (11)

于是D_τ−I不在任何有限Schatten类S_p，ordinary det与det₂以及其它有限阶det_p均不能按这个raw式定义。加任意compact／有限rank counterterm亦不改变该essential-norm事实。这里的essential norm是这份辅助Gram算子的norm，不是危险core K_L、source→receiver norm或完整Q的必要费用；不能借相同字母把它运输过去。

## 5. 同一个fixed源也拒绝所有含2的finite-Euler层

上一节已足够拒绝“对任意finite F”的raw定义。为不把跳过早期层误留成cofinal修复，这里收齐同一代数的直接范围：**r可以固定，不随F变；只有用于证明非紧的receiver小patch依F选择。**

取上节同一个r，其support紧含于正半线，r=0在开区间I₀内、r=1在I₀+log2内，并已用远处bump作双矩平衡。对任意先fixed finite F包含2，准确有

    W_F=B_F*B_F
       =product_(q∈F)[(1+a_q²)I−a_q(U_logq+U_(−logq))]，
    a_q=q^(−1/2)。

其有限delay集合D_F由sum ε_q logq、ε_q∈{−1,0,1}给出；prime factorization使这些delay互异。尤其delay log2的系数准确为

    c_F(log2)=−2^(−1/2) product_(q∈F,q≠2)(1+1/q)≠0。   (11a)

选J_F⊂I₀足够窄，使全部J_F+d（d∈D_F）两两不交。这总能在每个先fixed F做到，不声明最小spacing的cofinal lower。令f_R=exp(iRy)1_(J_F)/sqrt(|J_F|)。unitary共轭的全Gram差在每个delay d的输出上为

    c_F(d)[exp(iτr(y))−1] U_d f_R，                 (11b)

因为输入patch上r=0。凡非零输出都支撑于fixed positive compact supp r；其中log2输出在r=1的plateau上，系数为c_F(log2)(exp(iτ)−1)。输出patch互不相交，故没有其它mixed delay可抵消它。即使d<0，r=0的负半轴也不留下非零amplitude。

对任意fixed positive compact支撑的L² amplitude v，(7)先用于step函数再用其L²逼近，结合||P−I||≤2，给

    ||P(exp(iRy)v)−exp(iRy)v||→0。                  (11c)

把(11c)用于(11b)的有限个amplitude，unit-modulus delay相位不影响误差，便得全finite F压缩差的同样noncompact见证：

    ||G_(F,iτ)[r]−G_F||_ess
          ≥|c_F(log2)| |exp(iτ)−1|>0，               (11d)

只要τ∉2piZ。对relative D用G_F有界可逆夹乘再得非紧；若写数值lower，可除||G_F||≤product_(q∈F)(1+a_q)²。这里准确量词为每个先fixed finite F有其J_F、R阈值和o_F(1)，没有uniform F渐近、危险core／K费用或primitive谱结论。

因此不能仅删去F={2}、从较大X开始来建立同一raw determinant：同一个合法fixed r在每个finite F含2的层都拒绝其compact／S_p域。源没有随X移动；receiver见证随finite F缩支撑是证明中允许的算子norm测试，未被冒称全Weil source-family的覆盖。

## 6. 完整目标保留，但本式没有到达其比较门

560的原字典保持

    t_F(r)=Tr(A_r Pi_F A_r*)
       =q_Gamma(r)−P_F(r)+<r,K_(F,I)r>，
    A_r=integral r(u)U_u du，
    P_F(r)=sum_(p∈F,k≥1)logp p^(−k/2)
                         [R_r(klogp)+R_r(−klogp)]。

F_L覆盖所有actual可见base primes后，完整目标仍

    Q_W(r)=t_(F_L)(r)−<r,K_(F_L,I)r>
               +2|<r,cosh(u/2)>|²−2|<r,sinh(u/2)>|²。  (12)

全部Gamma/FP-contact、原1/(2pi)、所有proper powers和双pole均在同一actual对象里，没有为拟合新Gram而删去。对(4)源，pole只是本源上精确为0，不从目标定义中消失。(1)的pointwise M_r与(12)的group integral A_r不同，尚无新同源Hessian身份；trace-domain首门已经失败，不能把合法bounded curve等同于合法Fredholm metric或完整Weil比较。

原已停Sonin determinant用的是receiver M_(hat r)，其weighted-L¹源衰减实际支付S₁，因此合法但Levi等于591旧covariance。本候选改tangent后确实不落进那个逐层相等，但也正因此丢掉了原trace-class付款。直接换用det₂不是修复：它也要求compact，而(11)否定了这一必要条件。

## 7. 净后果、计轮和准确停止

三句裁决如下：输入是(1)这个实际source-dependent Euler共轭；首检是relative Gram的ordinary／Schatten determinant域；执行后以(2)–(11d)拒绝这个**未减bulk**的具体规则。没有靠未证PSD、K=t−Q+pole、unknown domination或cofinal covariance假设维持候选。

然而(9)–(11d)只是旧560 carrier加初等移位乘法的直接typing结果，发生在已付high-frequency区，未给任何新的dangerouscore有利差、principal／Green关系边、整sections／mixed RR或成长Ξ。它也不改善whole542+555→557 leading4/5负惯性UPPER。因此建议**0准入止损**：不准C064／601，不给一个新数学轮，不拆“det₂也失败／改compact counterterm”再领弱后继。

此拒绝不覆盖另有实际定义和费用的bulk-subtracted determinant、非Schatten正则化、不同polar／Grassmannian线、source smoothing或真正signed/coherent新机制。它们需要独立指定的对象／regularization／源map与完整Gamma/pp/pole和原norm误差；列为合法自由不等于已经构造，也不自动授后继预算。本稿不选择一个未知counterterm继续、不派paper／参数／高频率改进。

实际瓶颈未变，三个Goal完成门仍open，同实例应保持active。这个源域首检优于重复595同v诊断或596累加，因为它实测了一份新公式并在进入未知core前给出确定裁决；它不冒称新的core独立输入已经出现。

## 8. 执行范围与版本

只写本独占文件。无web／新paper／PDF／数值或大型算术重放；不改Goal、STATE、cadence、文献库、看板或Git。一次Windows wildcard目录检索失败后用`rg --files`定位真实Sonin determinant目录，失败不作未发现证据。辅助只读agent核了(2)、(6)–(11d)，并确认任意小非零τ及fixed-r所有finite F含2的范围；两次只读检查均已terminal、无文件；其消息只作交叉检查，不代本稿完整推导，也不另计轮。

实际输入指纹如下。Hash仅认版本；未重审这些旧稿的全部外部证明、未重新认证safe-high大证书。

| 本地输入 | 实读／使用范围 | bytes | raw SHA256 |
| --- | --- | ---: | --- |
| goals/GOAL.20261027.md | 全文/完成门与规则 | 9679 | b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de |
| goals/contracts/C063-rank-two-period-positive-cone.md | 全文/停止与计轮 | 1517 | e242d79457f2721ac77aa50d9666456e3ea77b6d7597937b4b93f061188271cb |
| goals/reviews/2026-10-29-rank-two-period-600-settlement.md | 全文/当前因果范围 | 3943 | 6e015edf62a0ad1ade37bdab5cead786f3b26d90095e3ccc4a089462ce07d2b5 |
| reviews/2026-10-29/post-599-input-choice/signed-core-actual-comparison.md | 全文/strongest-old与准入限制 | 14149 | 839ffe03cf13fe78462a0749f981dd5570b042b33bf466068eadf767fa12ff95 |
| notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md | 全文；使用§§1–2 actual对象及carrier，保全目标字典 | 9263 | 9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3 |
| notes/596-critical-prime-sonin-covariance-and-signed-increment.md | 前120行；仅用§§1–2物理/receiver角色，后续不消费为新前件 | 9094 | b609b8e5a820ca259c1a02fce134ca5b788d4c3373b933b6e1d2c3094cc4a782 |
| reviews/2026-10-29/sonin-determinant-line-admission/fredholm-domain-and-mixed-curvature.md | 前96行，使用ordinary夹源域与§§3–6角色；不重审nested proof | 8158 | 9f524c45c65f58112a39023de2d1cc4738883dbc7cf8aafe76d13cf2f2cb0929 |
| reviews/2026-10-29/sonin-determinant-line-admission/root-gram-source-and-curvature-test.md | 全文/旧source tangent与Levi正号、停止范围 | 5406 | cb306b01f8a2635afcc20a16c3d70400e941ae096a747686d2210062b643e0d4 |
| notes/591-connected-occupation-covariance-three-fixed-test-barrier.md | 前22行，仅读实际receiver/source定义与三源statement；非新审计 | 5974 | 5a6d6e221369a1a9bce668d56c9fe574aeca0a295fdb7d0ccd31e4fcd03eaa7c |

UTF-8/LF；文件冻结后由parent重hash。当前无待续进程；raw稿存在不代root消费、计数或准入。
