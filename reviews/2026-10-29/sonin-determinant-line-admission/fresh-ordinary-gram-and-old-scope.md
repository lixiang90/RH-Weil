# Sonin Gram行列式：不同组织的限定逆审

2026-10-29；同G20261027/runtime1793085111、原0c4f。按README/STATE/check→show、Goal/C057/D20261029Q/formal19及前沿恢复。本稿只审当前候选，不改状态、计轮、Git或来源。结构check不认证数学或实际运行Goal。

**结论：PASS，按最强旧直接推论归old0。** Ordinary sandwich域、真正Gram kernel、原点mixed Levi与591的同一V_R链闭合；无必须修复的主链缺口。消费范围限自然source及保相同一阶tangent的holomorphic Gram pullback。原domain稿§5的C²句只按中心化scalar链式法则解释，不能外推为任意nonholomorphic Gram重参数也不改曲率；第5节明确该限义。不需改动三个冻结原件。

## 1. 实际输入版本

下列三稿完整读取并逐一核规范UTF-8/LF字节与SHA256；不以旧handle完成替代当前版本。

| 同目录输入 | LF字节 | SHA256 |
|---|---:|---|
| root-gram-source-and-curvature-test.md | 5406 | cb306b01f8a2635afcc20a16c3d70400e941ae096a747686d2210062b643e0d4 |
| fredholm-domain-and-mixed-curvature.md | 8158 | 9f524c45c65f58112a39023de2d1cc4738883dbc7cf8aafe76d13cf2f2cb0929 |
| strongest-old-and-principal-role-scope.md | 7948 | 24458e0b82ad7951f050096b046bfa1c66e781f5f10295bdd07f1a4f7e05874d |

另直接核560 §§1、4，591全文及trace-domain澄清，406 §2及§4.1，410 §§4–6、569 §§5–6的相关角色。只读子核独立复查C²链式法则与Gram PD，无文件写入；该子核已终结，不另计轮。本审未打开外部PDF/网页或进行query、下载、数值。

## 2. 实际密度、强源域与ordinary S₁

P=Π_F是含完整G_F逆的真实Sonin正交投影，receiver为H=L²(dt/(2π))。560给Lebesgue迹密度ρ_F连续且O_F(log(2+|t|))，receiver核对角κ_P=2πρ_F；因此迹积分为∫φρ_Fdt=∫φκ_Pdμ，不是∫φρ_Fdμ。

原physical r的f=rhat，compact smooth或S_exp给f∈B_F=L∞∩L¹(ρ_Fdt)。分|t|≤1和外部，以||r||₁和t²f=−r″hat支付weighted-L¹费用≤C_F(||r||₁+||r″||₁)。这不是du/Dlog统一费；τ不能据此自动扩到全部weighted-L²(log)源。所有C_F先fixed，不交换成cofinal常数。

对0≤R≤P及有界φ∈L¹(ρ_Fdt)，A=M_sqrt|φ| R^(1/2)为HS，||A||HS²≤∫|φ|ρ_Fdt。令u=φ/|φ|、零处0，则

    R^(1/2)M_φR^(1/2)=A* M_u A∈S₁。

故φ=f及e^f−1均合法，后者的weighted-L¹费≤e^||f||∞∫|f|ρ_F。普通Fredholm τ_R(f)=det[I+R^(1/2)M_(e^f−1)R^(1/2)]有定义且在B_F整全纯。R=P时等于PH上的压缩行列式；R无需trace-class、finite rank或projection。此证明只付夹心，不解冻bare R M_φ的S₁断言。

共同op界e^||f||∞−1在||f||∞<log2给零自由log branch；trace-series的S₁收敛依旧含ρ_F费用。共同op半径不等于uniform trace-norm、三阶余项或cofinal C²控制。

## 3. Holomorphic scalar与真正Gram metric

τ_R(zf)非零处的log|τ_R(zf)|²确为pluriharmonic。正Levi候选必须另写

    G_R(z,w)=τ_R(zf+barw barf)。

J_R:x↦(√Rx,√(I−R)x)是H→H⊕H的isometry，D_z=diag(e^(zM_f),I)。其Gram压缩为

    J_R*D_w*D_zJ_R=I+√R M_(e^(zf+barwbarf)−1)√R。

有限输入ONB截断的det是有限外积向量的Gram kernel，因而PD。K(z,w)在参数紧集上为连续S₁族，有限截断的S₁逼近及det连续性局部一致，PD传到G_R。Diagonal算子≥e^(−2|z|||f||∞)I且为I+S₁，故其det严格正；未假ambient有限trace。

这给实际解析Hermitian metric，但不是新的算术principal functor。若norm²为G(z,z)，通常Chern号是−∂bar∂logG；取dual metric G^(-1)才对应正Levi。本文只比较明确的正标量系数，不靠line/dual名称改变目标符号。Local holomorphic frame归一化不改Levi；标量τ的zero divisor不独自生成它。

## 4. Mixed计算、迹域与591的精确消费

记A_R(φ)=√R M_φ√R、L_R=logτ_R、F_R=L_R−TrA_R(f)。普通trace-det展开给

    DF_R(0)=0，
    D²F_R(0)[f,g]=Tr[A_R(fg)−A_R(f)A_R(g)]。

每项由上述sandwich或HS乘积付S₁，循环仅在此合法域内。代g=bar(shat)，交换两个已合法compression因子的trace后得到

    D²F_R(0)[rhat,bar(shat)]
      =〈(I−R)^(1/2)M_rhat R^(1/2),
          (I−R)^(1/2)M_shat R^(1/2)〉HS
      =V_R(r,s)。

第一槽linear，正对角无factor2；一般R保jump与killing两部分。故∂z∂barz logG_R(z,z)|0逐层精确等V_R(r,r)，不是只在cofinal极限相似。

591已对全部共同0≤R_X≤Π_X、含无限rank/非局部/整组三源适应给g、τ_(1/2)g、g′的统一gap。其目标q0,q0,q1含完整Γ/contact、全部proper powers与indefinite双pole。这里可直接代入curvature族，无须先交换导数极限。失败索引可随X/R改变，不能误报某固定索引恒失败。

整数tensor或合法正curvature组合只给外部β_XV_R或总权W_X；原591仅迫必要β/W≥c exp[b(logX)²]，非充分、sharp或du→HS算子norm lower。βV_R不是V_(βR)。达到该增长、signed virtual tensor、relative ratio及新features仍未排。

## 5. C²重参数与极限的消费限义

中心化scalar F_R的DF_R(0)=0，确使实C²链式法则中的DF_R·D²Φ项消失，其second jet只读DΦ。这不等于原Gram metric L_R(Φ+barΦ)对任意C²映射有同一Levi。令Φ(z)=zf+a|z|²h，h实、ℓ_R(h)=TrA_R(h)≠0；同一个complex-linear一阶tangent下，raw Gram的Levi变为

    V_R(f)+2Re(a)ℓ_R(h)。

Holomorphic Φ才使该额外mixed导数为0，且线性中心化是pluriharmonic frame项。本次old0结论仅消费自然holomorphic source/同tangent holomorphic pullback；不把domain稿§5的C²句用作任意nonholomorphic metric不变定理。该明确收窄不影响原候选主链，也不把此反对照当新候选或数学轮。

同理，fixedF Taylor remainder不是uniform cofinal余项。要从非线性scalar/kernel极限推出其Hessian/Levi极限，须另付相应局部一致解析或C²控制；pointwise height收敛本身不足。新nonholomorphic metric、不同tangent或signed补偿未获本证，也未被本证排除。

## 6. Principal角色、最强旧与停止

406§4.1已保算术principal pair(div a,−log|a|²)的正则单位可有非零arch Green分量。因此本τ的辅助复参数zero divisor或非零log值都不能单独认证/否定405关系的算术principal下降。410的非平凡relative determinant/K类与569的matched cocycles也是真旧资产，但各自尚缺完整source/principal/section/mixed容量；Gram正性不补这些职责。

最短依赖链是560 actualρ/强源域→普通sandwich S₁与标准det→Gram Levi精确V_R→591全occupation三测试及正权必要费。没有新算术数据、源方向、全域费用或独立signed净号。相对τ只把Q_W−V_R的(T_Π−T_R)+C_R−K_Π+P_pole责任重新写出，一般R未占据正项不丢，也不由未付预算自动准入后继。

故old0恰当：不建C058/595，不推进cadence0/history58/latest594/formal19或manifest132。关键primitive/principal/sections/mixed、dangerous core/cross/Ξ及whole leading4/5负惯性UPPER未改；此局部自然metric停止不完成原Goal，也不排全部行列式线/相对几何。最终根消费、看板/库和发布由root按实际状态办理。
