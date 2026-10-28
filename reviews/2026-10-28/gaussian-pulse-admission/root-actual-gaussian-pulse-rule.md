# 同一actual密度的Gaussian-pulse正滤波：冻结规则与首检

2026-10-28；G20261027/runtime1793085111/原0c4f，AS。前polyfilter metadata5537f6f已独立核actualHEAD且恢复树干净，不重发旧回执。附件2410.20758原定位已由10-20读过，拟新来源在执行前撤回，没有web/PDF重读或新source预算。本门是不同实际nonpoly/nonlocal规则，不续fixed degree/rank/rate或C050/C052。

固定A=1，枚举(-1,1)中互异有理数a_j，字典e_j(t)=exp(-ia_jt)，节点集合稠密于该区间。沿同一actual full-Euler Sonin密度ρ_X，令μ_X(dt)=exp(-t²)ρ_X(t)dt。Gaussian是output/source-filter，不放进Sonin trial空间。先须核ρ_X>0 a.e.；可用585同一非零raw-entire H₀、finite-Euler实轴无零与full-Gram weighted Cauchy。仅near0正性不能冒全谱coverage。

对一份预定非负smooth compact spectral densityσ，令mσ=∫σ、f_X=sqrt[σ/(exp(-t²)ρ_X)] a.e.。若ρ_X>0 a.e.，则f_X∈L²(μ_X)、norm²=mσ。每fixed X，Gaussian+globalρ上界给所有指数矩；若v正交于全部e_j，则vμ_X的Fourier为entire、在稠密实区间为零，故v=0，得到字典完整。有限字典Gram必须另核正定。

新的有限字典Gram记H，区别于ρ内部Euler G_F。严格采用

    H_jk=∫overline(e_j)e_k dμ_X=∫exp[i(a_j-a_k)t]dμ_X,
    v_j=∫overline(e_j)f_X dμ_X, c=H^-1 v,
    p_(X,M)=Σ_(j≤M)c_j e_j,
    E_(X,M)=mσ-v*H^-1v=||f_X-p_(X,M)||²。

原dispatch曾把H的指数方向与v混搭，已在本冻结前明确纠正；外层Weil源配对第一槽linear不改。取ε_X=1/X，选最小M使E<ε_X²，定义

    ν_X=|p_(X,M)|²μ_X,
    w_X(t)=exp(-t²)|p_(X,M)(t)|²,
    𝔚_X(f)=∫fhat(t)dν_X(t)。

每层正tempered、source-independent。有限M存在若上述完整性核闭；这是由exact residual定义的数学规则，不假称已付可计算积分认证、有效停止复杂度、condition number、M(X)或系数原强范数成长率。实际投影给||p||≤√mσ，故计划首界为||ν_X-σdt||TV≤2√mσ ε_X；TV指signedmeasure总变差norm，不除2。它若核闭便付strong S′/D′，并给每fixed I=(-L,L)所有complex源pair的original-du误差≤2L·TV·||r||₂||s||₂；这是相对所选σ，绝非相对完整Q的Γ统一误差。

唯一预定target test取两旧合法源g/g′的完整q₀,q₁>0，R=q₁/q₀。选even非负smooth compact σ±，使A±=∫|ghat|²σ±>0，r±=∫t²|ghat|²σ±/A±满足r−<R<r+；可在t²<R与t²>R且ghat非零处各选小bump。设

    λ−=q₀(r+−R)/[(r+−r−)A−],
    λ+=q₀(R−r−)/[(r+−r−)A+], σ=λ−σ−+λ+σ+。

此σ明确非负，预期同时匹配g与g′两目标；不靠未知ζ零点，但也没有选择完整经典正谱。Full target首检是旧log2 primeatom：σ有限谱质量给physical boundedcontinuous核；完整W在log2有−log2/√2原子，Γ/pole在该非零邻域smooth。height1窄compact test可分离，不能称Q负源或RH反例。

最强同一运输若对variable预定σ_X成立，可取任意已知正tempered谱measure的常规truncate/mollify σ_X，ε_X=1/[X(1+2√m_X)]，使TV误差≤1/X，从而得到该正谱的S′逼近。它仍是同一Galerkin规则的直接消费，不是第二candidate；不得以选择未知经典正谱为输入证明RH。576已付正锥普适及membership缺口，须优先扣强旧；actualρ运输即使成立也不自动新增独立核心input。两审只核此具体rule/TV/target和old-net，不预C053/590/新数学轮或来源队列。
