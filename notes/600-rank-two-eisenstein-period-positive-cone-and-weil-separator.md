# 600：秩二算术 period 的全截断正零谱与完整 Weil 分离

2026-10-29；同G20261027/runtime1793085111、冻结0c4f。一次完整的实际来源研究：该Eisenstein积分确给正型全零谱，但其自然clock下整个共同正混合锥均被同一个紧支测试与经典Weil目标严格分离。全参数、无界截断、正归一化、混合和同链signed必要成本统一消费；不按定义、旧passivity或标准引理分轮，不声明外部理论首创。

## 1. 实际来源与准确完成

Lagarias–Suzuki math/0412039v4的§1给PSL2(Z)模曲面上的截断积分，T≥1：

    I(T,s)=−Λ(2s)T^(s−1)/(s−1)+Λ(2−2s)T^(−s)/s，
    Λ(s)=π^(−s/2)Γ(s/2)ζ(s)。

Λ有pole；usual entire ξ(s)=s(s−1)Λ(s)/2不能与它混同。令a=(logT)/2≥0、z=2s−1，则

    s(s−1)I(T,s)=−T^(−1/2)G_a(z)，
    G_a(z)=[e^(az)ξ(1+z)−e^(−az)ξ(z)]/z，
    F_a(z)=G_a(z)/G_a(0)。

z=0取可去值。自然physical频率是G_a(iγ)=0的γ，原s的高度是γ/2。本稿全谱和比较均保这个因子；不以更换clock暗拟合目标。

该对象来自实际算术period，并可由已知ζ算术定义构造，不根据未知中心线零点选择参数。这里只读/目视核原文PDF1–4的必要公式及Thm1–2 statement，未审作者后章RH/简单性proof、附录或引用。下面所用特殊情形由项目自含重导，旧132的outer passivity明确为依赖。545/quarter的source packet范数不是这个先积分后的整函数零除子。

## 2. 无RH的全零轴、简单性和相位

设U(w)=ξ(1/2+w)、c=1/2。无条件ξ为order1、real even，其零点η=α+iγ满足|α|<c。Hadamard按±η及共轭组块正常收敛，无剩余线性指数。对z=x+iy、x>0，一个同高水平对称pair±α+iγ的距离平方积是

    F(t)=t⁴+2(d²−α²)t²+(α²+d²)²，d=y−γ，
    F(x+c)−F(x−c)=8xc[x²+c²+d²−α²]>0。

critical pair亦逐项严格增。因此|ξ(1+z)|>|ξ(1−z)|，没有假设α=0。E_a(z)=e^(az)ξ(1+z)满足|E_a(z)|>|E_a(−z)|；G_a=(E_a(z)−E_a(−z))/z遂无离轴零点。

精确处理Hadamard实常数：在s=1/2由FE和水平配对消去，得到

    φ_0'(t)=Re ξ′/ξ(1+it)
       =Σ_ρ (1−β)/[(1−β)²+(t−γ)²]>0，
    φ_0(0)=0，φ_a(t)=at+φ_0(t)。

这是已付外层正性机制的准确消费，不是新RH前件。由此

    G_a(0)=a+2ξ′(1)>0，
    G_a(±1)=e^aπ/6−e^(−a)/2>0，
    G_a(it)=2|ξ(1+it)|sinφ_a(t)/t。

中央分子零已约去，消两pole没有添加端点零。全部非零根由φ_a(γ_n)=nπ枚举，φ_a′>0给简单性。Tonelli积分与无条件RvM给φ_0(R)≤CRlog(R+2)，且φ_0(R)→∞，所以

    μ_a([−R,R])=2 floor([aR+φ_0(R)]/π)
       ≤CR[a+log(R+2)]。

每个有限a的G_a为even order1整函数，归一化全乘积为F_a(z)=∏_(γ>0)(1+z²/γ²)。全重数和两符号均保留。

## 3. 全a的完整正分布与无界截断极限

以hatφ(t)=∫φ(v)e^(−itv)dv定义

    μ_a=Σ_allγ δ_γ， W_a(φ)=Σ_allγ hatφ(γ)，
    V_a=W_a/(1+a)， Qbar_a(r)=V_a(r*r*)≥0，
    r*(v)=overline(r(−v))。

全部无限和绝对收敛。上节计数经dyadic求和给

    ∫(1+t²)^(−1)d[μ_a/(1+a)]≤C，
    |V_a(φ)|≤C sup_t(1+t²)|hatφ(t)|，

且对应高频尾对所有a≥0统一趋0。这避免了用增长为a²的逆平方矩冒称全参数统一界。Fourier规范为W_a=F^(−1)(2πμ_a)，没有多乘一个2π。

相位计数的区间差分给μ_a/(1+a)在a→∞时vague趋dt/π；连同统一尾，

    V_a→V_∞:=2δ_0于S′，从而D′，
    Qbar_a(r)→2||r||²_du。

有限a连续，故V_a在紧化A=[0,∞]上逐Schwartz测试连续并统一有界。无界T已经被纳入，极限不是未分析的逃逸。该结论是fixed源/Schwartz半范数，不是成长窗或du/Dlog单位球费用。

## 4. 实际Pan泄漏：相同order仍可反测

沿405/553固定真实physical P∈S_exp，有

    μ_±(P)=0，Q_ζ(P)=0，
    hatP(t)=s(s−1)ξ(s)/2，s=1/2−it。

Q_ζ是原完整Weil型，Γ/FP-contact、全部proper powers和双pole均保留；该0不用RH。令H(z)=ξ(1/2+z)/ξ(1/2)。

若某a的model γ全部使hatP(γ)=0，则G_a的简单零点是H的critical子除子。两者even order1的正常paired product可直接消去；R_a=H/F_a恰为剩余ξ零点的乘积，无未定zero-free因子。剩余critical pair沿实x给1+x²/γ²；离线quartet给

    1+2(γ²−α²)x²/(α²+γ²)²+x⁴/(α²+γ²)²。

所有高零因子≥1；低频例外有限，亦最终≥1。余集空则R_a=1，非空则任取一个pair/quartet得到R_a(x)≥cx²最终成立，不需未知余零点密度。

但Stirling对实际差商给

    H(x)/F_a(x)~C_a e^(−ax)x^(3/4)，
    C_a=G_a(0)(2π)^(1/4)/ξ(1/2)>0。

a>0时趋0；a=0时为介于常数与x²间的增长，两者均与余乘积矛盾。因此Q_a(P)>0对每个有限a成立。连a=∞的2||P||²>0及紧化连续性，

    q_*:=min_(a∈A) Qbar_a(P)>0。

这里没有数值q_*、有效最小化或零点收敛速率声明。

## 5. 同一个compact源与整个共同正锥的线性分离

取实cutoff χ_R及固定compact degree-dualsη_±，使μ_σ(η_τ)=δ_στ。设

    r_R=χ_RP−μ_+(χ_RP)η_+−μ_−(χ_RP)η_−。

r_R∈Cc∞、两个physical矩精确为0，并在S_exp趋P；它一般不是Pan。原Q_ζ的S_exp连续性给Q_ζ(r_R)→0，统一model谱尾另给sup_A|Qbar_a(r_R)−Qbar_a(P)|→0。两种连续性分别支付，没有直接以noncompact P测试D′。

取537固定小窗内实非零h，c_h=Q_ζ(h)>0，C_h≥sup_A Qbar_a(h)>0。令δ=q_*/(2C_h)，选一个固定r=r_R使inf_A Qbar_a(r)>q_*/2且|Q_ζ(r)|<δc_h/2。定义

    Φ=r*r*−δh*h*∈Cc∞，
    η=inf_A Qbar_a(r)−q_*/2>0，
    ε_Φ=δc_h/2>0。

于是

    V_a(Φ)≥η>0（全部a∈A），
    W_ζ(Φ)<−ε_Φ<0。

**整个共同正混合锥与目标由同一个紧支线性测试严格分离。** 任意正Borel混合ν（含a=∞、任意正归一化/组件数/费用/阶段变化）只要实际定义分布，均有∫V_a(Φ)dν≥η ν(A)≥0，故不能于D′趋W_ζ；零质量也无法匹配。Φ是差平方，非单个卷积平方或pointwise正函数。r精确双pole-zero；没有额外宣称h或Φ的双pole矩为0，目标仍完整。

## 6. 正添加、源适应和signed必要成本

原W_a正混合ω的真实质量是m=∫(1+a)dω，对应V_a混合ν；还允许ν在∞有质量。全参数统一upper及r上的lower使m=∞时该源能量∞，不是合法有限target逼近。

任给m_0>0、0<ε<1/3，可另选一个之后固定的精确双矩零r，使inf_A Qbar_a(r)>(1−ε)q_*、|Q_ζ(r)|<εm_0q_*。若逐源适应混合在这个r上最终m_j(r)≥m_0，任何逐源非负添加都有

    E_j(r)−Q_ζ(r)>(1−2ε)m_0q_*。

共同混合若加任意全源非负响应且完整匹配，必有m_j→0，否则上述固定源在某子列反测；统一S′界随即使整个period基部趋0。成功者须让添加部分独自承担目标。没有添加时，537正anchor又迫m_j有统一下界，故所有共同混合/归一化失败，亦与§5直接separator一致。

不能把anchor的mass跨源借给逐源适应规则，r与h的参数可不同；这种规则只按选定r上的保留质量条件消费。任意positive-type添加也可在差平方Φ上取负，不能只凭§5排全部正添加。若各组件只取有限频率截谱，须另保实际大cutoff部分的质量/cofinal条件；各标签分别cofinal不自动足够。

若允许signed/coherent总修补，匹配在上述r上的必要负响应为

    A_j(r)<−(1−3ε)q_*m_j(r)，

最终成立。只有另有真实A_j(r)=<r,T_jr>且T_j为原du空间bounded Hermitian算子，才得||T_j||>(1−3ε)q_*m_j(r)/||r||²_du。

共同实signed分布修补D_j还受§5的直接条件：若在Φ上匹配误差<ε_Φ/2，则

    D_j(Φ)<−ε_Φ/2−ηm_j。

这是差平方响应；在同一bounded Hermitian实现下才相应推出
||T_j||>(ε_Φ/2+ηm_j)/(||r||²_du+δ||h||²_du)。差测试的负值不迫T_j有负谱，正型添加也可给这个符号。这些是必要成本，不是signed机制失败或充分构造，不运输内部/native范数。

## 7. 强旧、clock与停止

132外层passivity、545/quarter的Eisenstein packet、565/566正身份、576正锥、577修补、586算子、594ordinary trace及599 Ising均保原最强范围。新净责任是这份实际算术period的全a全零谱/完整目标与整个共同正锥分离；不是“又有一个正模型”，也不重领HB、Pan、crop、标准求积或审计。

对额外固定b>0，F_a(bz)与H若等谱，则even/order1/归一化迫函数相同；实轴xlogx系数迫b=1，线性x迫a=0，logx余3/4仍矛盾。但这不证明全部b-混合、b<1 Pan泄漏或退化joint(a,b)正修补失败。自然clock以外的源适应/变尺度、真正signed负cross、不同源域/target及额外实际data均保留；它们不是已成功输入，也不自动获得后继预算。

本G_a来源族停止，不续T/phase/clock/其它rank/作者后章/附录或引用链。没有新primitive/principal/整section/mixed RR、危险signed core/cross或成长Ξ输入；whole542＋555→557 leading4/5仍仅负惯性UPPER。Goal三个完成门open，同实例active。

[根前件记录](../reviews/2026-10-29/rank-two-period/root-consumption-scope.json)绑定原推导、不同完整fresh、实际来源/强旧及修补量词。统一一个完整失败研究：cadence1→2/history63→64/latest600，formal20保持；非macro21，不归零。文献139，新增PDF仅本地，作者后章proof未审。
