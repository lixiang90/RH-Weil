# Gaussian pulse：最强旧、双测试匹配与完整目标的atom门

2026-10-28；`/root/moment_fresh_audit` 当前独占任务，非固定poly／source库存续算。已恢复README／STATE、check→show、Goal／frontier及AR结算；当前执行以root实际AS规则3548-byte版本为准。只读必要项目原件，无web／PDF／下载／数值，不改STATE／Git／cadence，不准新source或第二candidate。

**限定PASS，强旧直接消费0。** 同一actual ρ_X上的Gaussian＋固定稠密平移字典可运输预定正compact谱density；所选σ能同时匹配g与g′两完整旧tests。它没有选择完整经典正谱。对这份fixed finite σ，Galerkin质量≤m_σ已直接给一个fixed窄test的全X atom缺陷，无须先等TV极限。整个允许预定σ_X／质量成长的Gaussian-pulse class不能据此被排除；同一规则对已独立知道为正的tempered谱仍具标准普适运输，未付的是经典target选择／membership和完整signed净控制。

## 1. Actual接口、Galerkin约定与TV范围

585已付同一非零raw-entire receiver向量H₀，H₀(0)>0。有限D_X实轴无零，D_XH₀∈RanΠ_X，真实评价Cauchy给

    2πρ_X(t) ≥ |D_X(t)H₀(t)|² / ||D_XH₀||²_(dt/(2π))。

H₀的实零离散，故ρ_X>0 a.e.，不需未消费的“全部实点无共同零”命题，也不把near0正性冒全谱coverage。H₀是receiver；以下g是physical测试源，f_X则是新L²(μ_X)函数，三者不同。

μ_X=e^(−t²)ρ_Xdt有每fixed-X的全部指数矩，560逐X的log上界已足，甚至不需589的cofinal uniform费用。对v∈L²(μ_X)，complex测度vμ_X的Fourier因Gaussian指数矩为entire；若它在固定互异有理a_j稠密的(−1,1)上消失，则entire唯一性及有限测度Fourier唯一性给v=0。有限互异指数的Vandermonde又给每个有限H严格正定。这是weighted Gaussian空间中的完备性，不是普通无权L²的有限bandwidth稠密断言。

采用冻结版本已纠正的外层matrix约定：

    e_j=e^(−ia_jt)， H_jk=∫overline(e_j)e_k dμ_X，
    v_j=∫overline(e_j)f_Xdμ_X， c=H^−1v， p=Σc_je_j，
    E=||f_X−p||²=m_σ−v*H^−1v， ||p||²=m_σ−E≤m_σ。

H的指数为+i(a_j−a_k)t，不能与负指数和同一v混搭。该H是外层dictionary Gram，非ρ内部Euler G_F；这份conjugate-first matrix记法不改变外层Weil源配对第一槽linear。一般证明不需μ_X偶性。

f_X=√[σ/(e^(−t²)ρ_X)]在零测异常点任意置0，精确满足|f_X|²μ_X=σdt、norm²=m_σ；不用f_X bounded／smooth。字典完备性保证每fixed X有有限最小M使E<X^−2，尽管M、系数和condition number无共同预算。残差是平方norm，故其L²误差<1/X。真实orthogonal projection给

    ν_X=|p_X|²μ_X， ν_X(R)=m_σ−E≤m_σ，
    ||ν_X−σdt||TV ≤ ||p_X−f_X||₂(||p_X||₂+||f_X||₂)
                  ≤2√m_σ/X。

TV为signedmeasure variation质量，不取概率距离的1/2。于是频率侧strong S′成立；physical定义𝔚_X(φ)=∫φhat dν_X，故亦strong S′且D′收敛。没有另添／除2π；若另作标准Fourier变换，保hat𝔚_X=2πcheckν_X，非偶权时反射不能删。

Gaussian只属于外层output/source-filter。Fourier乘子e^(−t²/2)p_X对应有限平移Gaussian卷积，physical上非局部；没有将Gaussian放入Sonin trial域，也不保持原compact source支撑。原compact complex测试的weighted配对均合法；若用其源算子解释，平滑后为Schwartz源，可沿逐X密度界及compact近似运输，不声称原全部Dlog／全L²的未过滤ordinary-trace域自动不变。

本结论是exact Hilbert投影下的数学规则。E的形式值和“取最小M”不是已付有效积分认证、数值稳定算法、计算复杂度或M(X)成长率；TV的误差目标可按定义兑现，不意味着已给这种工程／有效性预算。

## 2. 两个完整旧tests可以真正同时通过

取587同一du norm1实偶正bump g，G=ghat，q₀=完整Q_W[g]>0、q₁=完整Q_W[g′]>0，R=q₁/q₀>0。G是非零entire，实零离散。可选even非负非零σ₋、σ₊∈Cc∞，分别支持在t²<R和t²>R且G非零的小邻域；上侧用±t₊的对称小bump即可。于是

    A_±=∫|G|²σ_±>0，
    r_±=∫t²|G|²σ_±/A_±， r₋<R<r₊。

冻结系数

    λ₋=q₀(r₊−R)/[(r₊−r₋)A₋]，
    λ₊=q₀(R−r₋)/[(r₊−r₋)A₊]

均严格正，σ=λ₋σ₋+λ₊σ₊为明确even正smooth compact density。直接代数给

    λ₋A₋+λ₊A₊=q₀，
    λ₋A₋r₋+λ₊A₊r₊=q₀R=q₁。

没有额外2π，因q₀／q₁与原∫|rhat|²ρdt规范一致。TV收敛作用于bounded Schwartz tests |G|²及t²|G|²，所以实际𝔚_X的g／g′配对分别趋q₀／q₁。这里不是只保证“非constant”，而是真通过先前filter首检；固定degree的均值坍缩不能再机械套用。

σ可取even。若需每层也实偶，actualρ_X的已付实结构给μ_X偶，f_X实偶，于是H、v为实、c为实，p_X(−t)=overline(p_X(t))，ν_X偶；不需字典按±成对。更一般非偶μ_X的运输仍合法，仅不再声称每层实偶。

q₀、q₁使用完整Γ／FP-contact、全部Λ(p^k)=logp及双pole，均可从原固定compact源公式定义，不读取未知ζ零点。g′ mean0不等于polefree。匹配这两个finite数据并不支付其余源、cross或完整D′目标。

## 3. 最便宜且更强的full目标atom首检

采用577的完整physical规范：

    W_ζ=W_Γ+2cosh(u/2)du
          −Σ_(n=p^k≥2) Λ(n)n^(−1/2)(δ_(log n)+δ_(−log n))。

在a=log2的充分小fixed邻域U内，避开0及其余prime-power点，完整Γ／contact与pole的限制都为smooth density，故准确有

    W_ζ|_U=−c₂δ_a+b(u)du， c₂=log2/√2>0， b∈C∞(U)。

contact在0，未在U制造第二个atom；proper powers没有被截掉或改权。这个atom与全部q₀／q₁所用目标相同，不是另选一份简化Weil型。

对fixed σ，每层ν_X总质量由**投影norm contraction**付ν_X(R)≤m_σ。因此physical核K_X(u)=∫e^(−itu)dν_X(t)有||K_X||∞≤m_σ，且

    |𝔚_X(ψ)|≤m_σ||ψ||₁  对所有compact smooth ψ。

这是421§6已有的L¹-test/atom门。这里甚至不需先用TV→σ；也不能把总质量界说成仅由g／g′校准推出，后者在高频及G的零附近不能控制全质量。

具体取0≤η∈Cc∞(−1,1)、η(0)=1，ψ_ε(u)=η((u−a)/ε)，ε小到support⊂U。则

    W_ζ(ψ_ε)=−c₂+O_U(ε||η||₁)，
    |𝔚_X(ψ_ε)|≤m_σε||η||₁。

选**一次fixed ε**使(m_σ+||b||∞)ε||η||₁≤c₂/2，就对所有定义好的X有

    |W_ζ(ψ_ε)−𝔚_X(ψ_ε)|≥c₂/2。

ε不随X缩小；这是一个真正固定D′测试，不是假借moving tests否定分布收敛。TV另给极限K_σ=∫e^(−itu)σdt（甚至为Schwartz函数），但完整身份在取极限前已经被统一L¹界拒绝。

该窄ψ不是声称给了Weil Q负源；正型分布在一般非负线性测试上可以为负。此处证明的是给定finite-target构造的full coverage失败，不是RH反例，也不是经典Weil非正。

## 4. 有限正谱层的最强旧必要预算

同一421门直接给一个更一般但仅属必要性的结论：若任意每层有限正谱测度ν_X所定义的physical分布真趋完整W_ζ于D′，则

    ν_X(R)→∞，不能仅unbounded。

否则有cofinal子列质量≤M，沿该子列用上节ε(M)的同一个fixed窄test便得统一atomgap，矛盾。这没有给质量发散率，也不排质量成长；更不把source校准误当总质量约束。当前fixed σ的ν_X质量≤m_σ，故精确落在该旧障碍类。

这一结论不排允许m_X成长的Gaussian-pulse class。只排finite-target或boundedmass子类，不能将它写成所有Gaussian滤波、非局部正D′或source-adaptive机制的no-go。

## 5. 同一rule的强覆盖与经典membership仍未付

若预定σ_X≥0的smooth compact density、m_X=∫σ_X可随X成长，对同一μ_X／固定字典重复Galerkin，取L²误差门

    ε_X=1/[X(1+2√m_X)]

仍给||ν_X−σ_Xdt||TV≤1/X。无需uniform M或coefficient费，但也没有这些有效费用。这里改变的是同一规则已允许的预定target数据，不另造candidate。

对一份**已独立知道为正且tempered**的谱Radon测度η，可按标准positive cutoff／mollifier先取σ_Xdt→η于strong S′，再加上述TV误差，得到ν_X→η于strong S′。注意：atomic η或无限质量η通常不能由smooth σ_X直接在TV中逼近；正确链是σ_X→η于S′、ν_X−σ_Xdt在TV中趋0，不能混成TV→η。

该standard步骤的必要前件已明：positive tempered η有某N使∫(1+|t|)^−N dη有限；χ(t/R_X)截断与compact正单位核j_(h_X)给σ_X=(χ_Rη)*j_h。S有界集的截断误差由p_(N+1)/R_X控制，mollification误差由h_X p_N(φ′)控制，均统一；故不偷用有限质量或未付拓扑。完整目标只要求D′，这里也没有据positive-tempered输入的运输擅自覆盖所有non-tempered D′目标。

对经典所需的实偶positive cone，576早已付固定真实椭圆曲线／尺度／正混合的D′普适及原Dlog alias费，且明确target membership承担完整Weil正型／RH责任。563的独立能量／热证书也要求完整分布身份，不是匹配两个moment；不能因p_X有限项就把当前含ρ_X的physical核误作有限常系数ODE。577更已给逐层保完整Γ的实际正修补，但其算术修补消失／净预算尚未付。将任何一份已知正层再运输到同一ρ_X，不会使那份未知缺陷自动消失。

当前same-actual-ρ实现确有内容：ρ_X a.e.正、Gaussian exponent moments、有限Hilbert projection把预设正谱送入具体nonpoly／nonlocal filters。这是560／585＋标准Fourier/Hilbert旧设施的直接组合；589的更强global bound甚至非必要。它不添加独立经典算术输入，不提供完整signed core/cross或同一非零primitive／principal／mixed／Ξ，不改善whole4/5负惯性UPPER。应准确旧0保存其运输与finite-target阻断，而不是把正锥普适或两tests通过报成经典突破。

## 6. 当前版本、停止范围

本核全文读取当前root规则及另一独占terminal的实际接口，未以旧任务终态代入：

| 原件 | LF bytes | SHA256 |
|---|---:|---|
| `root-actual-gaussian-pulse-rule.md` | 3548 | `963e55eaa5a4ea943e847c61199f964d7c4250eb50fdf86a82fa972387266387` |
| `actual-galerkin-and-tv-proof.md` | 15246 | `6d6102832a6942165de6df27ddb56b91f155741fff973195ce69ab7811e52920` |
| 585 | 7857 | `5dca916d978eef599587ff4c6ce34144f814ddec0567a4c1b2314dcd71cd01af` |
| 576 | 15924 | `cbf32034c1e63518ef124ba89e1a46093b55da1086868532d8e5a1e0576595bd` |
| 577 | 13925 | `cf80354ab3bb3c7ca2a2bae7e2aa4083adc47d01da5c984146fb285d7551f55f` |
| 563 | 11777 | `094c11cb5909eecc7f4e17468f00b43281b9fc6299042565aa792046807a5f4c` |
| 421 | 17570 | `4ae64e67058560106af2879679cd75975fcfc7e509e8b844a47c40faafc5603b` |

首两行均在本目录。实际主要消费为585非零entire／560逐X密度、576正锥与预算范围、577完整Γpp双pole、563证书／atom限制及421§6；没有重审它们引用的外部论文。

只停止当前fixed σ作为完整Weil目标的尝试；运输定理和允许m_X成长的同一class保合法范围，但不是已准后继／复杂度优化／目标选择预算。Root仍须实际对齐fresh再消费，本稿不结算或发布。原cadence3/history53/latest589/formal17保持，Goal同实例active／open，不因正模型或局部反测完成长期门。
