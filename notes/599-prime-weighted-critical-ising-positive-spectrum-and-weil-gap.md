# 599：素数权临界铁磁正零谱与完整 Weil 目标的固定源缺陷

2026-10-29；G20261027，同一运行Goal1793085111，冻结基线0c4f。明确生成规则的完整失败研究，统一一个数学迭代。有限正性、HS、整函数分解、ODE、旧Pan、混合及费用推论是同一证明链；不分别计轮，也不声明外部理论首创。

## 1. 实际候选与结论

令F_X为不超过X的素数，w_p=log p，S_k=Σw_p^k。固定实λ于紧集，充分大X时
B=S_2−λ√S_4>0，a=B/S_4^(1/4)。对σ∈{±1}^{F_X}，M=Σw_pσ_p，定义

    Z_X,λ(z)=Σσ exp(M²/(2B)+zM/a) / Σσ exp(M²/(2B))。

它不使用未知ζ零点，也不假设正锥membership。令θ=(λ,b)取任意固定非空紧K⊂R×(0,∞)，H_X,θ(z)=Z_X,λ(bz)。保H_X的全部零点iγ及重数，采用hatφ(t)=∫φ(v)e^(−itv)dv，定义

    W_X,θ(φ)=Σγ hatφ(γ)，
    Q_X,θ(r)=W_X,θ(r*r*)=Σγ |hatr(γ)|²，
    r*(v)=overline(r(−v))。

全部级数合法，W_X,θ为正型温和分布。它对每个Schwartz测试一致于θ收敛到四次临界极限F_λ(bz)的全零谱W_θ，因此也有D′极限。这是一个实际独立正分布族；完整目标匹配仍须另验。

**固定源缺陷。** 任给上述K及m_0>0，存在同一个非零实r_*∈C_c∞、q_K>0及X_0，使两个physical矩∫r_*e^(±v/2)dv精确为0，且

    inf_(θ∈K,X≥X_0) Q_X,θ(r_*)>q_K/2，
    |Q_ζ(r_*)|<m_0 q_K/8。

Q_ζ是原完整Weil型，含全部Γ/FP-contact、proper powers及双pole。没有假设RH。q_K、r_*和X_0在这里为存在性常数，未给其数值或有效零点误差率。

## 2. 有限正零轴：自含经典依赖

M²/(2B)的对角项为常数，pair耦合J_pq=w_pw_q/B≥0，磁场权w_p/a>0。对multiaffine稳定多项式A+Bx+Cy+Dxy，固定其它变量于开圆盘，diagonal二次式无盘内根给|A/D|≥1；故收缩成A+Dz仍稳定，D=0另由A≠0处理。

每边1+t(x+y)+xy，t=e^(−2J)∈(0,1]，由
|1+tx|²−|t+x|²=(1−t²)(1−|x|²)及t=1分解得到bidisk稳定。逐vertex收缩恰保全部一致spin项。代入各fugacity e^(−2c_vz)，c_v>0，得Re z>0无零；spinflip给另一半平面无零。全部零点遂在imaginary轴，Z(0)=1排0。

此证明直接覆盖非等权正磁场，不从uniform-field定理偷换假设。Lieb–Sokal1981只取得书目/摘要，未取得原论文PDF或读作者证明；它不是本证明的未付数学依赖。自含有限原件为3741 bytes。

## 3. 真正的临界极限与尾控制

记q=S_4^(1/4)，δ=maxw/q，L=S_2/√S_4，ε=1/(L−λ)。由Σ(w/q)^4=1得L≥δ^(−2)；Bertrand在dyadic区间给δ⁴=O(1/logX)，故δ→0及ε=O_K(δ²)。

精确HS及合法复移线给

    Z_X,λ(z)=e^(−εz²/2) I_X,λ(z)/I_X,λ(0)，
    I_X,λ(z)=∫exp(Φ_X(u)+λu²/2+zu)du，
    Φ_X(u)=Σ[logcosh(w_pu/q)−w_p²u²/(2q²)]。

负Gaussian前因子不可省略。用D(x)=x²/2−logcoshx，有

    x⁴/[24(1+x²)]≤D(x)≤x⁴/12，
    0≤x⁴/12−D(x)≤x⁶/45（|x|≤1）。

因此Φ_X全轴≤−u⁴/[24(1+δ²u²)]，内区误差≤δ²u⁶/45。在compact λ和complex z上得到共同可积Gaussian majorant，包含全部固定阶导数的多项式权。极限为

    F_λ(z)=∫e^(−u⁴/12+λu²/2+zu)du / ∫e^(−u⁴/12+λu²/2)du，
    sup_(|λ|≤K,|z|≤R) |∂λ^j∂z^k(Z_X,λ−F_λ)|≤C_K,R,j,k δ²。

这是全复局部一致收敛，非formal展开或概率弱极限。准确variance为
Z_X,λ''(0)=I_X,λ''(0)/I_X,λ(0)−ε，紧参数上一致有界并趋于m_2(λ)>0。

有限H_X为even、order≤1的指数和，paired Hadamard给

    H_X,θ(z)=∏_(γ>0)(1+z²/γ²)，
    Σ_allγ γ^(−2)=H_X,θ''(0)=b²Z_X,λ''(0)≤C_K。

有限自旋不意味着有限零点。对任意Schwartz φ，完整绝对tail有

    Σ_(|γ|>T)|hatφ(γ)|
       ≤C_K sup_(|t|>T) t²|hatφ(t)| →0。

局部一致整函数极限与Rouché保全部重数，再连这一共同tail，即付W_X,θ→W_θ于S′及D′，对θ逐测试一致；θ↦W_θ连续。Fourier约定下W=F^(-1)(2πμ)，公式中没有额外2π。这些是Schwartz半范数与fixed源量词，不是原du/Dlog单位球或成长窗uniform费用。

## 4. 不假RH的实际Pan反测

Laplace原理给logF_λ(x)~κx^(4/3)，κ=3^(4/3)/4>0，紧λ一致；全复上界亦给order恰4/3。故even、order<2的H_θ只有paired product，无遗漏zero-free Gaussian。合法分部积分给

    F_λ'''=3λF_λ'+3zF_λ。

三阶ODE唯一性迫每个零点重数≤2。沿405/553固定真实physical Pan源P∈S_exp，有

    Q_ζ(P)=0， μ_±(P)=0，
    hatP(t)=s(s−1)ξ_Riemann(s)/2，s=1/2−it。

该关系来自全部actual零点的Mellin消失及完整显式公式，不用RH。若H_θ每个γ均使hatP(γ)=0，则它的零谱支持于ξ的critical零集；multiplicity≤2加无条件RvM给N_θ(T)=O(TlogT)。paired product沿实轴遂有logH_θ(x)=O(xlogx)，与x^(4/3)矛盾。故

    q(θ)=Σγ |hatP(γ)|²>0。

共同谱尾保证q连续；紧性给q_K=min_K q>0。选实χ∈C_c∞、χ=1于0附近；固定compact degree-dualsη_±满足μ_σ(η_τ)=δ_στ。可由偶正bump及其τ_1平移的非奇异2×2矩阵构造。设

    r_R=χ(v/R)P−μ_+(χ_RP)η_+−μ_−(χ_RP)η_−。

它精确双矩零，r_R→P于S_exp；一般不是Pan。原Q_ζ在S_exp连续，故Q_ζ(r_R)→0；另一方面共同谱尾给sup_K|Q_θ(r_R)−q(θ)|→0。先依K,m_0选一个固定R，再由统一零谱收敛选X_0，即得§1。没有使support随X成长掩盖缺陷，也没有从noncompact测试直接跳到D′失败。

## 5. 同轮消费最强直接修补范围

对§1选定的同一r_*，允许每stage、甚至每个测试源适应地选任意正混合；components可任意多/连续、使用不同cutoff；不设统一rank、总质量upper或费用限制。结论的准确条件是：最终至少m_0的质量实际落在θ∈K且cutoff≥X_0的components上。全部components统一cofinal是充分条件；仅每个标签分别cofinal、质量逐层追逐低cutoff并不足够。条件是对已经依K,m_0选出的r_*成立；不把逐源只有>0但无这个lower扩成覆盖。

任何额外nonnegative per-source能量A_X(r_*)≥0，包括K外positive components，都使

    E_X(r_*)−Q_ζ(r_*)>3m_0q_K/8>m_0q_K/4。

没有总质量upper、boundedness、locality、quadratic或收敛假设。若每stage给共同线性positive-type分布，这否定D′趋于W_ζ；逐源适应而不给共同线性分布时，仍否定全部fixed源能量匹配。Full complex/mixed匹配包含此对角测试。

任何zero-free整因子逐stage不改零除子，包括无界Gaussian；不能用因子改变后的Z''改写原谱inverse-square恒等式。若允许signed/coherent修补，成功匹配的必要条件为最终

    A_X(r_*)<−m_0q_K/4。

这里只是必要负响应。仅另有实际A_X(r)=<r,T_Xr>且T_X为原du空间上bounded Hermitian算子时，才推出||T_X||>m_0q_K/(4||r_*||du²)。不把一般response擅称operator norm，也不把必要条件称充分构造。

## 6. 强旧、逃逸与停止

565/566的自动正模型、576正锥、577窗口修补、586 theta算子、592 orbit-time prime图、594自伴prime-linear ordinary-trace pencil与GORZ fixed-degree Hermite模型，均未识别成本spin生成规则的全零谱及目标比较。405/553、Hadamard/Rouché、ODE、RvM和正混合是依赖，不分别算新成果。新增净后果为这个明确独立positiveD′族的完整构造和full-target/指定正修补类的严格失败；不声称全网新颖。

仍未排：critical部分质量消失或无固定紧集保留质量；λ/b逃出紧集、b趋0/∞；不满足δ→0的权制度、非critical或非rankone耦合；真正negative/signed cross；不同实际源域、target或额外算术data。它们不是已成功输入，不自动获参数/章节/来源后继预算。本rank-one critical族停止。

**实际瓶颈没有改变。** 无新primitive/principal/整section/mixed RR、dangerous core/cross或成长Ξ付款；542＋555→557 whole leading4/5仍是负惯性UPPER。没有RH证明，也未证明全部Lee–Yang/positiveD′或承担整个核心的方法类失败。原Goal三个完成门保持open，同实例active。

原推导、不同完整fresh及root前件闭合见[消费记录](../reviews/2026-10-29/prime-ising-critical/root-consumption-scope.json)。Cadence统一0→1、history62→63、latest599，formal20保持；不是formal21或重置。文献库138中新增项仅metadata-only，无作者PDF/证明页。
