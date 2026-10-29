# Signed Euler pencil：有限实物与准入前首检

2026-10-29；同G20261027/runtime1793085111，原0c4f，cadence3/latest593/formal18。上一自导子old0已审结发布；本次恢复实际8d2ec62/tree999c207/parent8daf37e与clean，独立GitHub ref/commit/tree匹配，不重推。529的Doob/保正半群旧边界已自筛，不另领预算。

本门只检一个具体finite pencil，不续C055正图连接长度/容量或C056短窗参数，也不据“signed尚未排除”自动准入数学。尚无C057/594。

## 1. 实际对象和两素数源

在任意有限维正Hilbert空间取normal矩阵A_p（可有signed/complex entries，normal性相对于同一个内积），定义

    T_F(z)=Σ_(p∈F) z_p A_p，D_F(z)=det(I−T_F(z))。

实际two-prime signed例为A=diag(1,0)、B=(1/2)[[1,−1],[−1,1]]；二者是rank1 orthogonal projections，但不彼此正交。直接det给

    det(I−uA−vB)=(1−u)(1−v)−uv/2。

所以负entry并没有消掉这项mixed primitive。592的实际扩散family A=P_0、B=J_M/M同样给−uv/M；后者仍允许cofinal fullsigned逼近，不能用本首检反过来否定旧逃逸。

候选假设为先付每prime的完整pure local Euler identity det(I−zA_p)=1−z，再要求全pencil的trace对实际primepower测度精确或在原完整fixed源上逼近。不是把任意graph、unitary flow、companion、cohomology或完成后operator都叫这个pencil。

## 2. Root已执行的exact代数比较

Normal性与pure determinant恰给一个eigenvalue1、其余0，故A_p=P_p为rank1 orthogonal projection。全det若等于∏(1−z_p)，logdet的uv系数即Tr(P_pP_q)=0。又

    Tr(P_pP_q)=||P_pP_q||_HS²≥0，

故所有distinctprime的P_pP_q=0；空间只剩互相正交的prime lines及common zero。它不假已知primeblock分裂，而是从这个具体pencil的pure/wholetrace条件推出。Positive commonmetric换坐标不改trace/det，但原norm运输需给metric比较；不免费称Euclidean费一致。

此simple finite algebra可能已被最强旧直接覆盖；两稿正核actualdomain与old079/565/592准确范围，不能凭signed标签报新结论。

## 3. Cofinal精确源接口：待逆审的不同门

对有限F_j，若pure local factors始终精确且A_p normal，定义原half-density time measure

    ν_j=Σ_(n≥1)Σ_(p1,...,pn∈F_j)
         [log(p1...pn)/n] (p1...pn)^(−1/2)
         Tr(P_p1...P_pn) δ_log(p1...pn)。

在positive compact time上仅有限words，故为实际Radon signed/complex measure；反向word的trace为共轭，故总系数实。全部proper powers保留。设每fixed p最终在F_j，背景精确为WΓ+H，origin可有任意contact；W_j=WΓ+H−ν_j−ν_j^−在off0成立。不要求W_j PSD，不要求ν_j≥0。

在log(pq)、p≠q处，唯一words为pq/qp，实际系数恰为

    ν_j{log(pq)}=log(pq)/sqrt(pq) · Tr(P_pP_q)。

所有其它wordtimes在{log n:n≥2}，故可用一个fixed smooth bump隔离这个atom；不受cutoff、dimension、matrixentries或source-adaptive选择影响。

如果全部fixed compact complex r满足Q_j(r)→Q_W(r)，四平方极化先给全部fixed双槽B_j(r,s)收敛。不能直接搬592依正性得到局部TV的证明。独立math核提出更便宜且root已复核的直接源：令a=log(pq)，取小ε使(a−2ε,a+2ε)仅含一个log整数a且避开0；非负非零η∈Cc∞((−ε,ε))，f=τ_(a/2)η、g=τ_(−a/2)η。则h=f*g#仅在a附近，h(a)=||η||²>0。每层background Γ/H精确相同，origin contact与negative measure在这个mixed源上exact0，直接得到

    (W_j−Wζ)(h)=−log(pq)/sqrt(pq) · Tr(P_pP_q) ||η||²。

因此无需局部TV、signed Dprime重建或uniform source半范数前件，就有

    ||P_(p,j)P_(q,j)||_HS²→0，∀fixed p≠q。

Rank1使HS=operatornorm。它是原Hilbert sector间的pairwise overlap，不是positivegraph最佳single path的sup；总cofinal所有prime aggregate mixing、非normal/新arch边、非linear pencil、supertrace/relative/singular quotient均未涵盖。Sourceadaptive共同矩阵允许，不能逐r另选而没有共同W_j。速率、全F共同upper与RH无此结论。Root最初考虑过一般Dprime重建的UBP/Fourier桥，现已放弃作为依赖，也没有消费其未审结论。

## 4. 最强旧准入判门

独立input是已有实际two-prime projections/pencil与原prime weights，尚非新算术primitive。便宜可判门是negativeentries能否在mixed trace相消，以及signed full-source极限是否仍迫Hilbert overlap消失。扣079假定primeblocks的normal-limit、565有限Markov、592正edge-word分离/原norm桥后，若整个结果已标准直接蕴含则old0止；若确有不同wholeobject/cofinal signed必要结论才准一个数学轮，不以原型/两agents计轮。主线primitive/principal/mixed、dangerous signedcorecross/Ξ与whole4/5UPPER未付，不能把prime-only局部边界缩成Goal完成。

## 5. 同对象形成的严格自伴分支：去逐层pureexact

两个当前任务独立形成且root已重推：令每层所有A_(p,j)自伴，dimension、rank、matrixentries与共同positive metric可任意移动；不再要求det(I−zA_p)=1−z逐层成立。Fullfixed complex源收敛通过同一离散atom双槽test给

    m_(p,k)=Tr A_p^k→1，k=2,3,4；t_(p,q)=Tr A_pA_q→0，p≠q。

这里log(p^k)只有全p的k-word，其系数为logp·p^(−k/2)m_(p,k)，没有其它prime或word污染。定义

    d_p=m_(p,4)−2m_(p,3)+m_(p,2)=||A_p²−A_p||_HS²≥0。

对real λ，若λ<1/2，|λ|≤2|λ²−λ|；若λ≥1/2，|λ−1|≤2|λ²−λ|。故P_p=1_[1/2,∞)(A_p)满足

    ||A_p−P_p||_HS≤e_p=2sqrt(d_p)，
    |sqrt(rankP_p)−sqrt(m_(p,2))|≤e_p。

由于m2→1、d→0，每fixed p的rankP_p最终恰1，未要求ambient dimension统一。令ε_pq=e_p sqrt(m_(q,2))+e_q，由HS Cauchy和projection范数1给

    ||A_pA_q−P_pP_q||_HS≤ε_pq，
    0≤Tr(P_pP_q)≤|t_pq|+ε_pq，
    ||A_pA_q||_HS≤sqrt(|t_pq|+ε_pq)+ε_pq→0。

这些是dimensionfree实际generator norm后果；不是仅trace小、positivegraph最佳单路径sup或某固定lowrank预设。所有量读自同层原完整source，不借normaldeterminant在临界带收敛。没有给uniform growing F、source逐层变化或originaldu→HS统一映射费；原norm中的固定mixed test只用于读系数。普通positive metric换坐标时HS均指该native metric，不外推到未付Euclidean比较。

同一证明允许H_j无限维而每个A_p为ordinary selfadjoint S₁：全部有限words trace合法，spectral threshold仍finite rank，谱求和/HS估计不变。不扩到S₂-only缺少一次trace、无界或regularized/supertrace。

Normal但非selfadjoint确实不能这样去pureexact。实际H_j=C²⊕C^j，U_j为j-cycle unitary，A_p=diag(1,0,U_j)、A_q=diag(0,1,U_j)，则

    det(I−uA_p−vA_q)=(1−u)(1−v)[1−(u+v)^j]。

所有fixed worddegree<j的pure/mixed traces与Euler完全相同，hidden words time≥jlog2，fixed源最终看不见；但||A_pA_q||_HS²=j。可在F_j的各prime coordinate E_p之外共用同一U_j，F_j cofinal，即全prime fixed-source背景最终精确；不付PSD/RH。它是旧long/delayed逃逸的normal矩阵实物，不把它本身当新算术输入。自伴分支的fixedpair HS结论是否新净后果，须在两完整原稿及root扣079/592后准入，不凭本增补提前计轮。
