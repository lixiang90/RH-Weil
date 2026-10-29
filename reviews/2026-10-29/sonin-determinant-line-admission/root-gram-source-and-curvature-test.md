# Sonin行列式线候选：实际源、Gram metric与mixed首检

2026-10-29；同G20261027/runtime1793085111、原0c4f。按README/STATE/check→show/Goal/C057/D20261029Q/formal19前沿恢复，初始实际main b27ee71b1117f1943bd4b7710d2bcefd3f3b3988、tree4c62e4c、parent1454fdd独立GitHub ref/commit/tree已核且clean，前次发布条件通过，不重推。

上一轮594＋formal19是真数学/宏观进展；原核心未付。本门不续C057矩/metric参数，也不新读旧Segal–Wilson/Simon章或派空泛形成任务。具体实物是原actual Sonin投影上的压缩指数乘子，核它给的是不是新的同源mixed几何。尚未准C058/595，不计轮。

## 1. 同一实际算子和ordinary determinant域

先fixed finiteF（cofinal时F={p≤X}），P=Π_F为560的真实正交Sonin投影，receiver H=L²(dt/(2π))，完整G_F逆不删。其正迹Lebesgue密度ρ_F满足2πρ_F=Γ−bounded_F+ε_F、ε_F∈C₀，故连续且0≤ρ_F≤C_F(1+log(2+|t|))。Receiver核对角κ_F=2πρ_F，两种测度不混。

物理源r∈Cc∞(R;C)或S_exp，f=hat r；f∈B_F=L∞∩L¹(ρ_F dt)。实际weighted-L¹费可由C_F(||r||L¹+||r''||L¹)支付，不是免费原du/Dlog范数费。对0≤R≤P及φ∈B_F，

    K_R(φ)=√R M_φ √R ∈S₁，
    ||K_R(φ)||₁≤∫|φ|ρ_R dt≤∫|φ|ρ_F dt。

Factorization用M_sqrt|φ|√R的HS范数；只消费夹心S1，不升级已冻结的bare R M_φ S1。由|e^f−1|≤e^||f||∞|f|，定义实际ordinary Fredholm determinant

    τ_R(f)=det_H[I+K_R(e^f−1)]。

R=P时等于PH上的压缩Pe^(M_f)P determinant，P⊥块是恒等。有限维参数中的f↦τ_R(f)全纯，0附近取logτ(0)=0。Domain只付上述强源，不把τ无条件扩到全部Dlog源。没有取未知ζ零点、normaldet极限或numerics。

## 2. 标量、Gram metric和Chern符号须分清

τ_R(zf)本身是holomorphic scalar；非零处log|τ_R(zf)|²是pluriharmonic，不能将它直接称为有正曲率的行列式线。真正候选为

    G_R(z,w)=τ_R(zf+bar(w)bar(f))。

P的pure情形来自e^(zM_f)作用的Gram。一般R可用isometry J_R:h↦(√Rh,√(I−R)h)到H⊕H，取diag(e^(zM_f),I)作用；其Gram压缩为I+√R(M_exp(zf+barwbarf)−I)√R。有限输入维截断给真实Gram determinant，TC连续性传到上述kernel。Diagonal G_R(z,z)>0，给实际Hermitian metric；任意有限源方向可同样多变量化。

本文把**正Levi系数**定义为∂z∂barz logG_R(z,z)|0。若采用通常Chern约定，det tautological line与其dual符号相反；取dual Gram line才对应+(i/(2π))∂bar∂logG。该选择不凭名称提供算术principal、整截面或mixed RR。Holomorphic frame中心化不改Levi。

## 3. 根已执行的mixed计算与old591消费门

令L_R(f)=logτ_R(f)−Tr K_R(f)，一阶为0。逐层ordinary trace-det微分给对任意f,g

    D²L_R(0)[f,g]=Tr[K_R(fg)−K_R(f)K_R(g)]。

代g=barh，合法S1/HS循环后得

    C_R(r,s)=Tr[√R M_(f barh)√R−√R M_f R M_barh√R]，
    C_R(r,r)=||(I−R)^(1/2)M_f R^(1/2)||HS²=V_R(r)。

无额外factor2，receiver2π按原ρ/μ记；R=P退回connected projection variance。裸holomorphic τ的双全纯导数与这个Gram Levi有关，但二者不是同一个几何类型。

591已付共同0≤R_X≤Π_X的全部rank/合法无限维/非局部/按整组三源适应。其固定g、τ_(1/2)g、g'均在537正窗，原完整Q目标q0,q0,q1>0。全Γ/contact/properpowers/indefinite双pole不删。若声称本自然Gram curvature族在全部fixed源上趋完整Q，就精确落入591三测试统一gap；这里不是新的容量/符号定理。

若真实tensor/positive组合的curvature确为β_XV_R或Σw V_R，591只给外部energy系数/总权必要≥c exp[b(logX)²]，非充分、非source→HS operatornorm lower。整数tensorpower是外部系数，不是把R换成βR。Signed virtual tensor/relative ratios、额外principal Green补偿、新source features或非occupation几何仍未排，也不据此自动授预算。

## 4. 非线性极限、principal与完整主线责任

本门直接检验逐层mixed curvature/二阶源配对；不能无前件把X→∞与二阶导数交换。FixedF Taylor remainder O_F与cofinal locallyuniform/C²是不同量词。若有人改研究任意pointwise nonlinear τ/height极限、发散signed组装或奇异frame，当前Hessian旧门不能自动宣判失败；需实际比较与相应极限域。这不是本门的新后继预算。

Fredholm τ的zero divisor在辅助源参数上是principal，不等于405关系的真实算术principal边。算术正则单位的Green分量本可非零，不能单看metric非零就判principal失败。当前候选未提供把裸Gram曲率与arithmeticprincipal/Green协同的独立身份，也未给整过滤/截面乘法/mixedRR。若只把V_R名称换成detline，不越过已知591。

强旧判门：560实际密度/夹源域、标准ordinary determinant/Gram计算及591全occupation比较若已直接蕴含整个后果，就old0止，不新建C058/595。410实际非平凡line/K边界和569matchedcocycle保原角色；不将formal line或fiberpositivity当新primitive。关键sameprimitive/principal/mixed/corecross/Ξ与whole4/5负惯性UPPER未变，Goalactive/open。当前cadence0/history58/latest594/formal19、manifest132不动；两原稿→不同限定fresh→root范围闭合后发布，无新query/PDF/下载/数值。
