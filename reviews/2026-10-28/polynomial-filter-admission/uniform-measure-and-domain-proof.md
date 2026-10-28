# 正多项式滤波：系数一致费、全部Schwartz测试与物理分布域

2026-10-28；`/root/scalar_upper_tail`当前polyfilter独占稿。已恢复README／STATE、check→show、G20261027／原0c4f、AQ及root实际2973-byte规则；实际核587导数源Gram、589必要localization和任意measurable正权接口。不是phase／quiet／C050／C052参数续算。没有web、下载、新PDF、数值、STATE／Git／cadence修改；技术恢复后确认此独占文件尚未存在，沿同一任务继续，未重启旧证明或更换模型。

**结论：该固定degree、任意移动系数的正滤波族确实趋于谱原点质量、物理常数分布；所有uniform尾和原规范均可付。所需输入已经是587／589已根闭合证明中的更强设施，以下是标准直接组合，建议强旧0消费，不预C053／590或新数学轮。** 这里不是仅把fixed-pair极限改称S′：第3–5节直接对任意Schwartz test给出完整证明。

## 1. 真实规则、因式与准确源域

先固定整数d≥0；X→∞前d不再变化。w_X是real polynomial、degree≤2d且在整个real轴非负，系数任意依X而source-independent。沿原actual finite-Euler full-Gram密度ρ_X，定义正tempered测度及源型

    ν_X(dt)=w_X(t)ρ_X(t)dt,
    W_X(r,s)=∫rhat(t)overline(shat(t))dν_X(t)。

Fourier为rhat(t)=∫r(u)e^(−itu)du；ρ_X已含receiver求值归一化，不在此式再次添1/(2π)。每fixed-X有ρ_X=O_X(log(2+|t|))，所以ν_X为tempered正测度。对Cc∞ physical源，Fourier Schwartz，weighted配对有限。degree d>0可以提高form域，**不**将全部原Dlog免费送入这个polyweighted域；原du／原物理r=e^(u/2)bare没有更换。

一元实非负多项式的real roots有偶重数、非real roots共轭成对、非零leading coefficient为正，因此可选complex polynomial h_X，degree≤d，使w_X(t)=|h_X(t)|²于real t。零多项式取h_X=0；低degree补零系数。这里只是有限多项式因式，不输入未知ζ零点。h_X与source无关，choice的常相位不影响以下norm或测度。

写h_X(t)=Σ_(j=0)^d a_(X,j)t^j。令D=d/du，则

    r_(X,h)=h_X(−iD)g=Σa_(X,j)(−i)^j g^(j),
    rhat_(X,h)=h_X·ghat。

每个r_(X,h)仍为同[-1,1]内Cc∞源，原ordinary trace合法；这是核估计所用的actual导数源，不是将Gaussian试探范数代作源norm。对其他Cc∞源也有W_X(r,s)=T_X(h_X(−iD)r,h_X(−iD)s)。

## 2. 校准通过587 actual Gram付所有移动系数

g严格取587的du norm1正flat bump，g₀=ghat(0)=∫g>0，q₀=完整Q_W[g]>0。唯一校准为W_X[g]→q₀；因此W_X[g]在充分大X有一个fixed upper B₀，未要求每X精确相等。

587对于每先fixed d和全部complex移动系数的实际导数Gram lower给

    W_X[g]=T_X[r_(X,h)]
       ≥c_d √X/(logX)^(3d+2) Σ|a_(X,j)|²。

相位(−i)^j是coefficient norm的酉变换，无符号／2π损失。因此记ℓ=logX，有

    b_X:=Σ|a_(X,j)|²≤C_d ℓ^(3d+2)/√X。                (1)

这条是对全部允许h_X同时有效的actual lower反向控制系数，不能只用585各fixed源的lower代替。d先fixed，常数和起点依d、g、q₀；不含d_X成长一致性。

有限维Cauchy给全线点值包络

    w_X(t)≤(d+1)b_X(1+|t|)^(2d)。                     (2)

它允许roots／coefficients任意移动；没有暗设w_X偶或w_X(0)>0。

## 3. 两个实际uniform旧接口及Schwartz无穷尾

调用589已根闭合的实际proof，而非其fixed-f headline：

1. 任意nonnegative measurable输出权的正核／Tonelli支配给
   `ρ_X(t)≤C[√X+log(2+|t|)]` a.e.，C不依source／权／X。
2. 每先fixedδ>0及B=1的真实full-Gram evaluator localization给
   `sup_(δ≤|t|≤ℓ)ρ_X(t)≤C_δ exp(−c_δ√X/ℓ)`。

第一条可直接作用于|φ|w_X的截断并单调取极限，不需要它是某个fixed Fourier平方；第二条固定δ后才令X→∞。没有把auxiliary trial kernel当actualρ，也没有将有限高度界外推到全线。

结合(1)–(2)和第一条，对全部t有可积测试意义下的包络

    w_X(t)ρ_X(t)
       ≤C_d ℓ^(3d+2)(1+|t|)^(2d)[1+log(2+|t|)]。        (3)

此处放宽了1/√X的log项，只为简化tail。令p_N(φ)=sup_t(1+|t|)^N|φ(t)|。对任意φ∈S(R)，取固定N=5d+6，直接积分得

    ∫_(|t|>ℓ)|φ(t)|dν_X(t)
       ≤C_d p_N(φ) ℓ^(3d+2)
          ∫_(|t|>ℓ)(1+|t|)^(2d−N)[1+log(2+|t|)]dt
       ≤C_d p_N(φ) ℓ^(−3)[1+logℓ]→0。                 (4)

所有X依赖系数费已经在ℓ^(3d+2)内，故不是把fixed-f Schwartz常数误作uniform。测试φ任意complex时用其绝对值作measurable权即可，不要求|φ|光滑。

对每先fixedδ>0，在δ≤|t|≤ℓ用第二条和(2)，则

    ∫_(δ≤|t|≤ℓ)|φ(t)|dν_X(t)
       ≤C_(d,δ) p_0(φ) ℓ^(5d+3)/√X
                           ·exp(−c_δ√X/ℓ)→0。        (5)

故对于每δ>0、每φ∈S，ν_X对|t|≥δ的φ加权质量趋0。不能将φ=1代入此句：ν_X通常总质量为∞，这里是tempered测试，不是假概率测度tightness。

## 4. 校准给near0质量，闭合全部S′测试

f₀(t)=|ghat(t)|²∈S，f₀(0)=|g₀|²>0。取一次fixedδ_*>0，使|t|≤δ_*上f₀≥m₀>0。正性与校准给

    ν_X([−δ_*,δ_*])≤W_X[g]/m₀≤C₀。                   (6)

这不需要另一个w_X(0)下界。若ψ∈S且ψ(0)=0，对任意fixed0<δ≤δ_*，(4)–(6)给

    limsup_X |ν_X(ψ)|≤C₀ sup_(|t|≤δ)|ψ(t)|。

先X→∞，再δ↓0，连续性给ν_X(ψ)→0。于是对任意φ∈S，选

    ψ(t)=φ(t)−[φ(0)/|g₀|²] f₀(t)，

便有ψ(0)=0；校准ν_X(f₀)→q₀给

    ν_X(φ)→[q₀/|g₀|²] φ(0)。                         (7)

即ν_X→C·δ_(t=0)于σ(S′,S)，C=q₀/|∫g|²；δ_(t=0)是谱原点Dirac，δ_*仅为选定的小半径。这证明了全部Schwartz测试，而不是从卷积平方配对未经factorization直接升级拓扑。

若采用强对偶S′拓扑，同一证明也足够：对任意S有界集，p_N／p_0和一阶导数seminorm共同有界，near0的sup|ψ|≤C_Bδ，(4)–(5)的误差亦对该集统一；因此(7)在每个S有界集上一致。无需新增谱moment或分布factorization前件。

## 5. Physical正型分布、非偶权的反射与full目标

不假设w_X偶：例如(t−1)²本就允许。按root给定的配对，明确将physical分布定义为

    𝓦_X[φ]=∫φhat(t)dν_X(t),   φ∈S。

则𝓦_X[r*s*]=W_X(r,s)，其中s*(u)=overline(s(−u))；因此各层确为stationary Hermitian正型tempered分布。它的formal physical kernel是∫e^(−itu)dν_X(t)。在标准Fourier=∫e^(−itu)约定下，准确关系为

    hat(𝓦_X)=2π check(ν_X),
    check(ν_X)(φ)=ν_X(φ(−·))。

非偶权时不能省反射；也不能把ρ已有的receiver2π再除一次。由(7)及Fourier在S上的连续性，physical极限为

    𝓦_X[φ]→C φhat(0)=C∫φ(u)du，
    即𝓦_X→C·du（constant distribution）。               (8)

谱原点Dirac与物理常数分布不可互换。对全部先fixed Cc∞源对，(7)也给W_X(r,s)→C(∫r)overline(∫s)。

Full Weil目标只需作为D′分布／compact-source配对，不假设它在全线上tempered：两个pole可带指数growth。由于(8)本来蕴含D′收敛，要拒绝完整目标只需原fixed compact test。取g′，其Fourier为it·ghat，所以g′的Fourier模平方为t²f₀∈S且在0为0。因此

    W_X[g′]→0，
    Q_W[g′]≥2^(−49162)||g′||²_du>0。                  (9)

完整q₀／q₁保Γ／FP-contact、全部Λ(p^k)=logp和双pole；mean0不等于polefree，不能删g′的odd负pole。正滤波family的D′逼近在这一个必要测试已失败，无需先断言目标temperateness。

## 6. 最强旧分类、范围与停止

589只印fixed-source／fixed-pair结论时不足以直接推出本scope；但它的已付arbitrary-measurable global upper及fixedδ localization，加上587已付fixed-degree actual系数共同lower，已完整包含(1)–(9)的前件。非负一元poly因式、有限维Cauchy、Schwartz尾积分和near0校准是标准直接消费，没有新增独立算术／几何输入或未付uniform source估计。应恢复为更强旧后果0，而不是按新打印S′结论或moving coefficients另计数学轮。

所得边界仅限每先fixed有限degree、real轴全局非负、source-independent的这类poly filter；允许coefficients／roots任意随X、任意cofinal子列。它不是C052只scalar的文字重复，但也不是C050 degree优化。d_X成长、非多项式／非局部／signed／逐源非线性规则及primitive主线未被否定，不据此自授其预算。

全局目标正号、K不利正部／T-pole-cross、同一非零primitive／principal／mixed及Ξ仍欠；whole4/5负惯性UPPER未变。原Goalopen，cadence3/history53/latest589/formal17保持，不预C053／590。当前稿仅供root／独立审查消费，不作共享状态或发布操作。

## 7. 必要输入与当前版本

实际阅读root当前规则、587§1 actual derivative Gram、589原localization§6的fixedδ/B接口、C052 upper/tail§5和已根消费quiet稿中任意W的G4量词恢复；537原小窗完整coercivity用于(9)。没有重开这些旧合同或查新paper。

原norm／版本锚：587为8681bytes／LF SHA e4d30cfb6d07299386014cb4c4e3e3979ab5111264355dfb37b24629f121ac82；C052 upper10211bytes／bab769113b4ce8c858dfd4b7a83dea6abd8808436a599d2206ea9a9bf0915fff；local11459bytes／809bc7ffc6f1fbf4dd24af0d710af05fb7ca1bc259992430c3fd6760912ffcb1。当前root规则为2973bytes／LF SHA32483f5eab0e992e1826cd5c6706bb62f98bba314aa799ef284c4834a0e84076；不把此前task终态冒作本次结果。
