# 568 独立终审：评价载体、局部 jets 与完整 Weil 容量差

2026-10-20。结论：**PASS（限下述实际构造、恒等式和反测范围）**。
这不是经典 RH、完整 Weil 正性或宏观 Goal 完成的认证。主稿及三原稿的主要公式、对象角色、
范数与量词相容；一处 compact/S_exp 域作用的潜在越界已在出稿期指出并修复，最终版本重新核对。

本审查独立推导关键符号，并以 Python 整数/Fraction 重算有限表；不是仅核 hash 或链接。
没有复证全部外部 RR/Deligne/显式公式定理；本轮所需旧结果按下列绑定原件和其明确前件消费。
原始全度数 closed-point 正性仍来自290/563，有限表不承担外推。

## 1. 已修复的问题与版本界限

405 的 h=Eη 及 p=Eη₀ 是 S_exp 中非compact的真实源。主稿§2的载体先定义于
D=Cc∞，不能直接将它们称作该商的零类。最终568§5.1与classic原稿§5已明确：
这两个关系测试在物理 A_exp=e^(u/2)S_exp=S_exp、V_W^exp=A_exp/kerJ_W 中进行。
完整Γ/pp/poles表达在该域有绝对收敛、可微及连续延拓；kerJ_exp∩D=kerJ_D，
因此只有自然线性单射 V_D→V_exp，不追加拓扑嵌入结论。其余 compact 复源正性量词未变。
主稿(15)的标量也已限定实 t；复杂标量须写 |t|²。

这些修复发生于draft阶段，尚无已结算下游需要撤回；终审绑定的是修复后版本。

## 2. J_W 商与评价 minor：真实，但配对非退化不是正性

对实偶W，直接换元计算：

    ∫(W*r)(t) overline{s(t)} dt = W(r*s*)。

因此 kerJ_W恰为完整B_W的配对根；D′与Cc∞卷积给平滑输出及连续局部导数。
B_W(a*r,s)=B_W(r,s*a*)，以及
W(r* * s*)=overline{W(r*s)}，给根的卷积与*稳定；微分/平移稳定也成立。
这建立闭根理想和Hausdorff局部凸商。它没有证明商拓扑等于C∞像的子空间拓扑，
也没有规范Hilbert/Krein完成、正范数或谱自伴性结论。

有限维U中若点评价不能张满U*，存在非零类v被所有点评价消去，则J_Wv恒0，矛盾。
故主稿(4)确有非零评价minor。它不是Weil Gram的minor；即便总空间的配对非退化，
其任意有限子空间的限制也可能退化/不定，更不能由evaldet≠0读出PSD。
J_W像的逐点乘法并不等于源卷积，普通D在卷积上也不满足截面乘法所需Leibniz和式。
LS的同余乘积整除不能仅从这一载体移植。

一般Hermitian非偶分布需改反射；最一般双对象Mellin对偶未自动给共同中心或Hermitian正型。
主稿明确限定本轮实偶目标，保564–565的completion/weights/B(s)责任，范围准确。

## 3. 连续族的独立符号复算

在A_d=C[D]/(D²+d)、D*=-D中，v=A+BD有

    τ(v*v)=2|A|²+2d|B|²。

这是因为D²=-d使常数项为|A|²+d|B|²；cross D项regular trace为0。
C_d(u-v)=C_d(u)C_d(v)+dS_d(u)S_d(v)，故该式确为完整W_d的二次型，
不是人为正metric的替身。矩映射满射由C_d、S_d的分布线性独立性成立。

Wronskian C_dS_d'−S_dC_d'=C_d²+dS_d²=1。
同一两点评价det=S_d(1)在−1/4<d≤1/4中≥23/24，而Weil点Gram为

    E diag(2,2d) E^T，det=4d S_d(1)²。

因此真实jet非退化、维数容量2和所给统一整函数上界确实两段共享，目标惯性却相反。
compact bump与平移的source Gram为2a²[[1,C_d(h)],[C_d(h),1]]；其det符号同d，
所以反例不依赖δ不是测试函数的问题。独立精确重算d=±1/16,0给metric diag(2,1/8)、diag(2,−1/8)、diag(2,0)
及det 1/4、−1/4、0，与记录相符。

d=0时jet空间/代数仍二维，但τ配对rad=CD、Weil最小商为一维且trace权2；
faithful正Hilbert *作用因skew D且D²=0必令D=0，确会过强排除阈值正例。
这里没有把cyclic维数当普通谱重数，也没有声称所有正谱模型失败。

Wick rotation z→iz保centered disk supnorm/原点jet过滤，只运输到旋转后评价点并保det绝对值；
不保物理实线的*。主稿只拒忘却实对偶后的holomorphic容量，未错误拒全部real joint条件。
Hankel和核给2(|cos矩|²−|sin矩|²)；半轴任何开区间两矩独立，因此存在真正compact负测。
这准确拒过强Hankel必要性，未否其他反射/核构造。

## 4. 函数域局部设施与primitive差：两个载体不可合并

R_B的有限域trace pairing因可分而perfect，即使Tr(1)=d在特征p中为0也无碍。
截断jet配对取最高系数再域trace：对a的最低非零项a_i，乘单项式b t^(r−1−i)，
其余高项模t^r消失，再选b使域trace非零，故非退化。ordinary algebra trace不具此性质。
t→t^q在有非零nilpotent时非自同构；不用特征零Wronskian移植，处理准确。

X_B的复线性化是另一个正载体，d-cycle对V_B^n的trace为d当d|n、否则0。
故raw trace复原截断N_n。但完整primitive系数是

    a_n=q^(n/2)+q^(−n/2)−q^(−n/2)Tr(V_B^n)。

负号方向和a_0=2g contact正确；raw维数M_B发散不代固定primitive trace重数。
F_q上perfect双线性与C点集上的positive内积没有F_q→C标量扩张关系。

独立整数/Fraction复算q=5两组N、b和M_B全表均吻合：
真曲线(9,27,108,675)/(9,9,33,162)，反模型(1,11,76,451)/(1,5,25,110)。
primitive二阶det=4−t²/5分别11/5、−1；完整系数代数基1,X上trace form
[[2,t],[t,10]]的det分别11、−5。前者是归一化Gram，后者不同基/尺度，不混同。

倒数FE令X†=q/X。复化并合并系数共轭后，reduced点由α→q/barα交换；
交换二点块不定，固定点给正的带重数平方和。因此此trace form正恰为该有限类的纯性，
不是独立来源。nilradical商须保原trace权，稿件已保留。

真实曲线的restriction核H⁰(D−E)、degE>degD注入及RR下界作用于同一global source，
与自由局部jet仅有target严格不同。平方上有效化/交数及全period primitive身份仍消费567旧结果；
本轮未从raw点集造出global gluing、RR或primitive positivity。

## 5. 经典完整Γ、powers、pole与实际读出费用

由digamma积分，Γ∞(ξ)−Γ∞(0)=∫w(v)(1−cos ξv)dv，
w=2e^(−v/2)/(1−e^(−2v))、Γ∞(0)=ψ(1/4)−logπ。
故(13)/(14)的contact及二阶差分系数一致：配对后jump恰为
(1/2)∫w||τ_vr−r||²。近零差分O(v²)对w~1/v可积；large-v指数下降。
双pole从2cosh(u/2)卷积给e^(t/2)M_-+e^(−t/2)M_+，配对为2Re(M_+bar M_-)。
有限位由n=p^k给logp/p^(k/2)，没有以logn代logp或删proper powers。
所有项的符号与完整源恒等式相容；正jump不消Γ₀、prime及odd-pole方向的共同符号责任。

fixed I调制r_R=φe^(iRu)下，Fourier移频及Schwartz尾给
||r_R||_D²=logR||φ||²+O(1)。Γ∞=log|ξ|−log(2π)+O(ξ^−2)给
∂^k(G∞*r_R)(0)=(iR)^kφ(0)logR+O(R^k)。
fixed-window prime位移只有有限多，对k阶导数贡献O(R^k)；pole矩由分部积分任意快下降。
所以point/jet对原L²和Dlog确不有界，k=0比值~sqrt(logR)。
同一方向Q_W(r_R)=logR||φ||²+O(1)>0；没有把费用反例错报负惯性。

fixed smooth probes的Γ加权Cauchy–Schwarz、有限位shift L²界及pole矩界确给
|B_W(r,ψ)|≤C_(I,J)||r||_D||ψ||_D。缩probe的费用为
ε^−1 log(1/ε)||ψ||²主项，或增强H^s、s>k+1/2的费用，均是合法但不免费的修复。
此处先fixed I、R→∞；不支付support成长、所有评价map失败或所有非局部修复失败。
经典carrier无限维由有限维D′子空间闭及log2负原子不可能平滑推出，正确但与563旧障碍同源。

## 6. 关系、各budget下降与PSD字典

405给I⊂rad T，而I∩rad B=P_an；物理r=e^(u/2)f下Q=T。
因此J_Q消整个physical I是正确Q角色，不是把405 B的根从P_an扩大。
旧h有c=d=1/4，故P(r_h)=2cd=1/8，arch−prime=−1/8；实倍数给±t²/8。
它只排Q非退化商上两片无补偿分别下降，未排det line、matched local cocycle、
或405已付保双degree的解析扩张。p的关系被消、r₀的Q>0可见两测试准确，
但在读取完整源前件后成立，不升级独立几何principal/sections。
单独Γ₀→Γ₀+c时J→J+cId且p≠0，已有关系迫c=0；这只校准此一contact自由度。

平滑W_ε Gram恒等式由实偶ρ卷积、平移和反射直接成立。
allε/all finite complex Gram PSD与Q≥0的反向通过共同compact中Riemann sums及D连续性，
再ε→0，合法。它是等价字典，不是新正性。局部lower≤log|D|≤global upper本身只给
预算差非负；其归一化全source→Q身份、全部mixed方向、误差与容量独立性仍须另证。
本轮明确没有该预算。正|det|²或J*J会改变连续负段目标，不能替代完整配对。

## 7. 净后果和未核责任

本轮实际新增是给出源定义signed评价候选及非零minor，真实local étale/jet同时通过正反模型，
并核经典同源map的原norm费用和片段下降责任。商/核线性化是一般既有方法；
563纯性证书、565阈值重数、567 RR/Gram、405关系及552同类高频费用均扣旧归属，
不能声称新经典正性或严格whole预算改善。542+555→557 leading4/5及560 growing signed K/core/coupling保持。

尚未支付：裸g数据的canonical completion/权；可乘global source及与jets兼容的principal gluing；
同一nonzero对象的非负local order及独立height/RR容量；完整Γ/contact/powers/poles的全mixed身份与极限。
真实几何、连续/非局部或norm适应修复未被排除。C031一轮结算及STATE/cadence由root另行负责；
本审查不将settlement draft或hash当成根消费。结算摘要已读，其范围与本文一致，但不是数学输入。

## 8. 输入版本绑定（UTF-8，CRLF正规化为LF后SHA256）

- `notes/568-source-evaluation-carriers-local-jets-and-weil-capacity-gap.md` — `f71ab11661107f5fe0d294ac671421b7aaef0f8860f87c238d8fbe1a15554a4a`
- `reviews/2026-10-20/evaluation-carrier/continuous-carrier-and-budget-tests.md` — `28571c625801e986746db8c52c6ba218c7db049dc8756297042e7922dc774096`
- `reviews/2026-10-20/evaluation-carrier/function-field-evaluation-budget.md` — `a16efa3d6201754ce4d8aa1b8dc7152eb6f14d981b4265de4d6dec4ce672d91e`
- `reviews/2026-10-20/evaluation-carrier/classic-full-source-and-evaluation-audit.md` — `b6cdeaf86818ac822025b15b71818eb65f2db230ca7e47786d98f1a8278cc116`
- `reviews/2026-10-20/evaluation-carrier/exact-algebra-checks.json` — `3d2e567ec07b298c080ab51203eb2c09ab72bb80a4737c6f5e9c8501577e84bd`
- `notes/405-f1-adelic-restriction-moments-and-radical.md` — `fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d`
- `notes/552-radial-adelic-green-principal-and-comparison-gate.md` — `670c05aac61921a4f36accc89638e2844fe7221df6341e4e7ff27964fb22d887`
- `notes/563-distribution-side-weil-certificates-and-heat-complete-monotonicity.md` — `094c11cb5909eecc7f4e17468f00b43281b9fc6299042565aa792046807a5f4c`
- `notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md` — `96c0c5a62e4175705696a29ed28d890eb11cec6f7351dc763641b65f3fcaec8a`

哈希只绑定所审版本，不认证外部来源或未经核查的前件。
