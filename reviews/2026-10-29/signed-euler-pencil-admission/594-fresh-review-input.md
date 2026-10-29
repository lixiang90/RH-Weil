# 594：自伴 signed Euler 源的 Hilbert–Schmidt 舍入与素数对退耦

2026-10-29；C057一个限定数学迭代的待审草稿。原冻结0c4f，同G20261027/runtime1793085111。Math8488与strongold9159原件已terminal/root全文核；不同数学fresh及root最终消费尚未完成，不计cadence。完整前件与最终结算以本门root收据为准。不声称RH、世界优先权或全部signed模型边界。

## 1. 实际共同源规则

每层F_j是有限prime集，每fixed p最终属于F_j。H_j为正Hilbert空间，可无限维；共同族A_(p,j)=A_(p,j)*∈S₁(H_j)，无uniform S₁/HS/operator norm、dimension或rank上界。矩阵元素可signed/complex，共同metric可逐层改变。

用ordinary trace的prime-linear pencil T_j(z)=Σz_pA_(p,j)定义其时间数据

    ν_j=Σ_(k≥1)Σ_(p1,…,pk∈Fj)
         [logN/(k sqrtN)] Tr(A_p1⋯A_pk) δ_logN，N=p1⋯pk。

在[0,T]上k≤T/log2、p_i≤e^T，故每层只有有限words；S₁使每个word的ordinary trace合法。合并reverse word后系数实，但ν_j不必非负。三个R² unitvectors两两内积−1/2的projections就在log(pqr)产生−log(pqr)/(4sqrt(pqr))的实际negative atom。

原physical r=e^(u/2)bare及du/zero-extension Dlog保持。每层确有共同W_j∈D′(R)，off0上

    W_j=WΓ+H−ν_j−ν_j^−，H=2cosh(u/2)du。

完整Γ有限部分及contact规范、所有properpowers和indefinite双pole保留；origin还可有任意逐层contact修复。只假设全部**先fixed compact complex r**满足

    Q_j(r):=W_j(r*r#)→Q_W(r)。                       (1)

不要求Q_j PSD、逐层消noncompact Pan，也不假regularized determinant正常收敛。共同族可随层/所有资料改变，但逐r分别选不同族而没有共同W_j不在(1)内。此规则还不是独立算术primitive/principal源映射。

## 2. 双槽离散原子读取

四平方极化从(1)给所有fixed r,s的mixed收敛。所有wordtimes在同一个固定局部离散集{log n:n≥2}。给n，a=log n，取ε>0使(a−2ε,a+2ε)只含该log整数且位于positive半轴。取非零实η∈Cc∞(−ε,ε)，令r=τ_(a/2)η、s=τ_(−a/2)η。则h=r*s#仅支撑a附近，h(a)=||η||du²>0。

在(W_j−Wζ)(h)中，Γ/H精确相消，origin contacts与negative measure exact0。故

    ν_j{a}−νζ{a}=−(Q_j(r,s)−Q_W(r,s))/||η||²→0。     (2)

无需ν_j≥0、局部TV一致界、UBP或一般signed D′重建。n=p^k时只有全p的k-letter word；n=pq、p≠q时只有pq与qp。因此

    m_(p,k):=Tr A_p^k→1，k=2,3,4；
    t_pq:=Tr A_pA_q→0，p≠q。                         (3)

对应atom的实际权分别为logp·p^(−k/2)及log(pq)/sqrt(pq)。这些fixed two-slot源可精确读出其误差；不将原source收敛升级为moving-source或统一成长窗费用。

## 3. 无维数前件的实际谱舍入

Selfadjoint性使

    d_p:=m_(p,4)−2m_(p,3)+m_(p,2)
        =||A_p²−A_p||HS²≥0，d_p→0。                 (4)

取P_p=1_[1/2,∞)(A_p)。A_p是compact自伴，故P_p有限秩，即使H_j无限维亦然。对每个real λ，

    |λ−1_[1/2,∞)(λ)|²≤4λ²(λ−1)²。

逐谱求和及HS反三角不等式给

    ||A_p−P_p||HS≤e_p:=2sqrt(d_p)，
    |sqrt(rankP_p)−sqrt(m_(p,2))|≤e_p。              (5)

由m2→1、e_p→0，每fixed p的rankP_p最终恰为1。没有先假pure local factor逐层exact，也不由一般normal的特征值trace代替singular-value控制。Operator norm由||A_p||op≤sqrt(m2)取得，无额外uniform前件。

对每fixed p≠q，在Pp/Pq最终rank1后令

    ε_pq=e_p sqrt(m_(q,2))+e_q。

分别展开trace差与product差，HS Cauchy给

    |Tr(PpPq)−t_pq|≤ε_pq，
    ||ApAq−PpPq||HS≤ε_pq。

又Tr(PpPq)=||PpPq||HS²≥0，于是

    ||ApAq||HS≤sqrt(|t_pq|+ε_pq)+ε_pq→0。            (6)

这给整个fixedprime-sector的HS/因而operatornorm必要退耦，允许任意合法无限H、移动rank和共同族适应。它不是592的最佳single返回路径活动度sup。若前件相对共同metric G_j成立，(4)–(6)均为native G_j范数；Euclidean另有sqrt(κ(G_j))运输费用，成长condition-number不能省略。没有du/Dlog→HS统一operator映射估计。

## 4. 非空适用族与真正的normal逃逸

取每prime的正交line E_p，A_(p,j)=E_p、F_j穷尽primes，ν_j为原primepower截断。每个fixed compact源最终只见正确的有限primepowers，所以(1)最终exact；这给非空实际自伴适用族。它并未付Q_j PSD或新经典正性。

另一方面，令U_j为j-cycle unitary或其roots-of-unity对角形式，

    H_j=C^(Fj)⊕C^j，A_(p,j)=E_p⊕U_j。

各A_p normal，TrU_j^k=j·1_(j|k)。每fixed T，j>T/log2后hidden words全部在窗外；F_j又穷尽全部可见primes，故同WΓ/H的Q_j对每fixed源最终exact Q_W。然而对p≠q，

    ||A_pA_q||HS=sqrt(j)，||A_pA_q||op=1。

两prime的det公式为(1−u)(1−v)[1−(u+v)^j]，单prime factor为(1−z)(1−z^j)。所以“fixed moment逼近”不等于“逐层pureexact”，normal也不等于selfadjoint。此normal clock是旧long-delay逃逸的实际域对照，不将其当独立新反RH结果。未排非normal、非linear、supertrace/relative/global quotient、singular极限或另添arch边。

## 5. 最强旧扣除和完整目标

Signed两投影例只是592 M=2例的酉换基；exact-pure normal的rank1正交分类归标准准入旧比较，不重复计轮。真正新增的是(1)在原signed固定源域下迫(4)–(6)，去掉逐层pureexact并允许无uniform维数/rank/norm及ordinary S₁无限H。079预设primeblocks或exact有限Euler的正常det极限，未给这个source-cofinal class；其normal-limit指全纯局部一致收敛，不能混同矩阵normal。592只positive-edge SCC/path-sup，不给signed whole-sector范数。

新局部方法选择改变：在这个prime-linear ordinary-trace自伴类中，不能靠有限或无限rank、signedentries、逐层共同适应而保fixedpair非消失的Hilbert混合，同时匹配完整fixed源。未给all-growing F的sum/sup、集体通信、moving源速率或normal-clock等全部修复的边界；原537非根、405关系和principal/整截面/mixed RR也未由此生成。危险signedcorecross/成长Ξ、whole542＋555→557 leading4/5负惯性UPPER仍未改。

C057仅一个完整数学迭代；待不同fresh与root前件核定后统一cadence3→4/history57→58/latest594，再按连续非核心投入在4轮及时做formal19，正式复盘完成才同counter4→0一次。当前稿未结算，不提前消费counter。不得以这一prime-only局部模型类缩小长期Goal完成门；同Goal保持active/open/noteligible。不续moment阶数、metric/gain参数或来源队列。
