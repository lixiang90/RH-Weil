# Signed Euler pencil：纯幂、混合系数与固定源首检

2026-10-29；限定准入稿，G20261027/runtime1793085111，原0c4f。已按入口恢复README/STATE、check→show、Goal/C056/D20261029N/前沿，并核079及592原范围。本稿只审同一个有限pencil与原prime时间源；不建合同、不计轮、不改STATE/Git/manifest。strongest-old净值由另审及root统一裁决，不因signed标签宣称新数学或Goal完成。

## 1. 对象和精确normal分支

每层有限维正Hilbert空间H，有限prime集F，

    T(z)=Σ_(p∈F)z_p A_p，D(z)=det(I−T(z))。

ordinary trace/determinant；不是supertrace、非线性transfer或完成后的全局cohomology。矩阵元素可负或复，normal性指相对于同一Hilbert内积；不假共同对角化或已知primeblock分裂。

若每个A_p normal且det(I−zA_p)=1−z，则其非零特征值恰一个1；normal排除0上的Jordan块，所以A_p=P_p是rank1 orthogonal projection。再若D(z)=∏_(p∈F)(1−z_p)，在formal log展开

    −log D(z)=Σ_(k≥1)Tr(T(z)^k)/k

中，z_p z_q（p≠q）系数恰Tr(P_pP_q)，目标为0。又

    Tr(P_pP_q)=||P_pP_q||_HS²≥0，

故P_pP_q=0。结论：这些prime lines彼此正交，其余为共同零空间；dim H≥|F|。反向也成立。不需正entry、图的正edge-word或rank上界；亦不只检查某个basis中offdiagonal entries。

实际signed首检A=diag(1,0)、B=(1/2)[[1,−1],[−1,1]]给D(u,v)=(1−u)(1−v)−uv/2。592的实际diffuse例P_0、J_M/M给−uv/M；负entry不能取消这个两prime trace，但cofinal overlap可以趋零。此处未推翻旧diffuse逃逸。

## 2. 原prime时间与固定atom读取：无正测度桥

有限F_j、任意有限矩阵A_(p,j)先定义实际局部有限测度；§4另允许H_j无限维且各A_(p,j)为selfadjoint trace-class S₁。后一域中每个有限word的ordinary trace同样合法。

    ν_j=Σ_(k≥1)Σ_(p1,…,pk∈F_j)
        [log N/(k√N)] Tr(A_p1⋯A_pk) δ_log N，N=p1⋯pk。

在positive compact time内，k≤T/log2且所有p_i≤e^T，故只有有限words；不需要维数、entries或总变差有统一界。所有层的支撑都在同一个固定离散集合{log n:n≥2}。自伴矩阵时反向word的trace为共轭，合并atom实，但不一定非负。

目标νζ=Σ_pΣ_(k≥1)logp·p^(−k/2)δ_(klogp)。每个fixed p最终在F_j。原physical r=e^(u/2)bare、du/zero-extension Dlog及完整WΓ/contact/H=2cosh(u/2)du保留。假定共同W_j∈D′(R)在off0满足W_j=WΓ+H−ν_j−ν_j^−；origin可有任意contact。若全部fixed compact complex r有

    W_j(r*r#)→Wζ(r*r#)，

四平方极化直接给每个fixed mixed pair收敛。这里不要求Q_j PSD、ν_j≥0或预付whole-source norm bound；逐r选不同pencil而不存在共同W_j不在假设内。

固定n≥2，a=log n。取ε>0，使[a−2ε,a+2ε]⊂(0,∞)且不含其它log整数，η∈Cc∞(−ε,ε)实非零，令r=τ_aη、s=η。h=r*s#支撑恰在这个小窗，h(a)=||η||²>0。所有origin contact及ν_j^−作用严格零；共同Γ/H在差中精确相消。因此

    (W_j−Wζ)(h)=−[ν_j{a}−νζ{a}]||η||²→0。

这就读取每个fixed atom，无需一般D′重建、UBP、密度或592的positive-TV桥。特别唯一分解给

    ν_j{klogp}=logp·p^(−k/2)Tr(A_p^k)，
    ν_j{log(pq)}=log(pq)/√(pq) Tr(A_pA_q)，p≠q。

前式只能由all-p的k-letter word产生；后式只有pq、qp两个words，没有漏别的prime分解或proper powers。故完整fixed源收敛迫每个fixed p,k有Tr(A_p^k)→1，每个fixed p≠q有Tr(A_pA_q)→0。

例如三个C²实unitvectors两两内积−1/2，其rank1 projections满足Tr(P_1P_2P_3)=−1/8；六个排列在log(pqr)合计给−log(pqr)/(4√pqr)。所以本pencil确可有negative atom，不能把整个ν_j当正测度。以上隔离只读固定atom，未偷付局部TV有界或全分布强收敛。

## 3. Cofinal normal分支：保逐层pure校准

若A_(p,j)逐层normal且每个单prime因子始终exact为1−z，则A_(p,j)=P_(p,j)为rank1 orthogonal projection。§2的mixed atom直接给

    ||P_(p,j)P_(q,j)||_HS²=Tr(P_(p,j)P_(q,j))→0，
    ∀fixed p≠q。

Rank1使此product的HS norm等于operator norm。该结论允许维数、cutoff、共同内积及所有entries随层与已给共同源规则改变；不需谱normal-limit。它是两固定prime sector的实际Hilbert overlap，不是592最佳single path activity sup。

没有统一all-growing-primes的速率、collective mixing norm或fulloperator收敛结论；不能将每fixed pair消失交换成growing F_j的sum/sup消失。尚未付其它来源、principal/整数截面/mixed RR、dangerous core/cross或Ξ。

## 4. 严格自伴分支：pure只须源端极限，不必逐层exact

同一pencil中，若只要求每个A_(p,j)自伴，可取消§3的exact单prime因子假设。这里H_j可为无限维，但此分支每个A_(p,j)必须在ordinary trace-class S₁；没有uniform S₁/HS/operator norm上界。S₁给所有有限words的ordinary trace，fixed time上仍仅有限words；不使用regularized trace或缺失的k=1项。由§2仅用k=2,3,4，固定p有

    m_p=Tr(A_p²)→1，
    d_p=Tr(A_p⁴)−2Tr(A_p³)+Tr(A_p²)
       =||A_p²−A_p||_HS²→0。

取正交谱投影P_p=1_[1/2,∞)(A_p)。在无限维S₁分支，A_p compact，此P_p仍有限秩；非零谱的可数求和及零核均按原Hilbert谱定理处理。逐个real eigenvalue λ有

    |λ−1_[1/2,∞)(λ)|²≤4λ²(λ−1)²，

故dimension-free地

    ||A_p−P_p||_HS≤e_p:=2√d_p，
    |√rank(P_p)−√m_p|≤e_p。

右端→0、m_p→1，所以rank(P_p)最终恰为1。不需要rank/dimension上界或先验uniform operator norm；后者由||A_p||op≤√m_p支付。

令t_pq=Tr(A_pA_q)→0，ε_pq=e_p√m_q+e_q。HS Cauchy给

    |Tr(P_pP_q)−t_pq|≤ε_pq，
    ||A_pA_q−P_pP_q||_HS≤ε_pq。

因为P_p/P_q最终rank1正交谱投影，

    ||A_pA_q||_HS
      ≤√(|t_pq|+ε_pq)+ε_pq→0，∀fixed p≠q。

这是本同对象测试中比§3更弱的pure校准前件：原完整fixed源的几个atom极限即足够。公式给实际moment缺陷下的dimension-free付款；没有另给source收敛的速率，也没有将背景Γ/H或norm费用改写。正交仅是极限近似，不说每层A_p已是projection或每层exact Euler。

## 5. Normal但非自伴时不能免费放宽pure前件

同pencil内的scope反测：F_j递增穷尽primes，H_j=C^(F_j)⊕C^j，令E_p为第一块互相正交的prime line投影，U_j=diag(1,ω_j,…,ω_j^(j−1))，ω_j=e^(2πi/j)，并置

    A_(p,j)=E_p⊕U_j。

这些A_p individually normal，共用同一个Hilbert内积；单prime determinant为(1−z)(1−z^j)，故不满足§3逐层pureexact。任意k-letter word的hidden trace是Tr U_j^k=j·1_(j|k)。对每个fixed time窗[0,T]，j>T/log2后所有hidden word贡献严格零；F_j再包含全部p≤e^T后，ν_j在该窗恰等νζ。因此可取同WΓ/H与零额外contact，使全部fixed compact源的完整signed型最终exact Qζ。

然而p≠q时A_pA_q=0⊕U_j²，HS norm=√j、operator norm=1。故只把pure因子放宽为fixed-moment/source极限时，normal分支的pairwise Hilbert-decoupling会失败。此hidden long-clock escape与592保留的长返回机制一致，不作为新全局反例重复领预算；没有付Q_j PSD或RH。

## 6. 角色、norm及结算边界

上述exact/cofinal均在普通正Hilbert trace的prime-linear pencil上；相对于每层共同正metric G_j的normal/selfadjoint可经G_j^(1/2)共轭使用同一证明，trace/det不变，结论norm是原G_j-Hilbert norm。若另要Euclidean norm，||AB||_(HS,Euclid)≤√κ(G_j)||AB||_(HS,G_j)，成长κ不能省略。各prime分别选不同metric不够。

079的prime-local normal-limit结论以已分块为前件；592的positive-edge SCC/返回sup与此operator overlap不同。exact finite部分用标准谱定理与HS正性；§2只消费已固定prime整数时间，无新的算术或零点输入。是否相对最强旧有净新增，交root/另审，不以此稿的完整性自动计轮。

本门未构造非零算术primitive、principal/Green、整过滤/section乘法或mixed RR；未控制whole4/5负惯性UPPER、dangerous signedcorecross或成长Ξ。非normal、supertrace、nonlinear/singular/globalquotient、新arch边与有独立signed比较的其它机制均未被排除。Goal完整门不能缩为此局部class；本稿无后继参数/来源/图容量预算。
