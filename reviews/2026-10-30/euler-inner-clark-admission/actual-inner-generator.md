# 单一 Euler-inner 候选：实际正 Clark 载体及最便宜的 germ 首检

2026-10-30；`/root/euler_clark_construct` 独占原稿。同 G20261027/runtime1793085111、原冻结0c4f。按AO执行一次有止点的实际公式建设准入，不修改STATE/cadence/Goal/文献/Git，不预授C066/603。没有新外部primary、PDF、章节、数值或另一候选。

**裁决建议：该明确候选在已付的 arithmetic-germ 必要门直接0止，不是新的RH正性输入。** 有真实的独立正载体；但其规范Herglotz函数对所有边界相位一致趋于常数1，规范Clark测度趋于Lebesgue，原源型趋于du内积。它在132/136早已要求的非恒定Euler/Gamma germ对齐之前就失败。下文把已实际完成的权重/源域/完整目标核对保存，不以这些标准桥接拆出新数学责任或另开修复预算。

## 1. 恢复及原件范围

读README/STATE，运行research_state.py check后show；恢复Goal、已耗尽C065、formal21、AN/AO及宏观frontier当前段。现场STATE已是AO：唯一在执行的是同目录execution-start的候选，不是恢复C065预算；原cadence0/history66/latest602/formal21，所有Goal完成门仍open。旧602发布的独立远端核验由parent完成，本子任务不冒称重新执行它的API。

本次全文读取132、136、137、079、592、594及560；组合输出曾截断，随后单独补读079/137及136后段。它们作为项目既有资产使用，不声称重审全部nested作者证明。尤其：132/136的正实极限必须先在非空Euler开集对齐实际germ；137已给inner Dirichlet流与完整signed Toeplitz目标，不把inner这个名称当新算术正号。079的无零正常determinant类、592的正edge周期类、594的prime-linear自伴S₁类不自动包含下述非线性inner/Clark构造。

## 2. 明确的实际对象和规范权重

令X≥2，F_X={p素数:p≤X}，a_p=logp，q_p=p^-1/2。在上半平面C_+定义

    w_p(z)=exp(i a_p z)，
    b_p(z)=(w_p(z)−q_p)/(1−q_p w_p(z))，
    B_X(z)=∏_(p∈F_X)b_p(z)。                                  (1)

因|w_p|<1且

    |1−q_pw|²−|w−q_p|²=(1−q_p²)(1−|w|²)>0，

每个b_p严格contractive、实边界上模1，故B_X为实际非恒定inner函数。它仅用原素数/原1/2权，没有ζ零点或未标记正锥membership输入。固定边界相位α∈T，定义

    H_(X,α)(z)=(α+B_X(z))/(α−B_X(z))，
    Re H_(X,α)(z)=(1−|B_X(z)|²)/|α−B_X(z)|²>0。              (2)

这是正实函数的规范Cayley变换，不是logarithmic derivative。采用Herglotz测度的明确规范

    Re H_(X,α)(x+iy)
       =(1/π)∫_R y/[(x−t)²+y²] dμ_(X,α)(t)+c_(X,α)y。      (3)

μ≥0，且∫(1+t²)^-1dμ<∞。由于B_X(iy)在y→∞趋于实数∏(-q_p)，模严格小于1，H_(X,α)(iy)有界，故c_(X,α)=0。这里没有无穷远的正线性项被省略。

实轴上选连续phase lift B_X(t)=exp(iφ_X(t))。直接求导给

    D_X(t):=φ'_X(t)
      =Σ_(p≤X) a_p(1−q_p²)/(1−2q_p cos(a_pt)+q_p²)>0，
    D_X(t)=θ(X)+2Σ_(p≤X)a_pΣ_(n≥1)q_p^n cos(n a_p t)，
    θ(X)=Σ_(p≤X)logp。                                      (4)

有限X时D_X有正下界和有限上界，φ_X从−∞遍历到+∞。若t_k为B_X(t_k)=α的全部根，则它们离散、simple，并在每个有界区间有限。H在各相邻根之间解析跨越实轴且Re边界为0。在t_k附近，

    H_(X,α)(z)=2i/[D_X(t_k)(z−t_k)]+holomorphic，

故(3)的全部有限谱测度精确为

    μ_(X,α)=Σ_k [2π/D_X(t_k)] δ_(t_k)。                     (5)

无额外连续部分：每个不含这些离散根的紧实区间均有解析跨边界及零Re边界；没有其它可承载singular measure的实点。式(5)同时核了π与导数方向。

规范Clark权是2π/D_X(t_k)，不是1。普通零点计数Σδ_(t_k)、phase导数D_X(t)dt和(5)是三个不同对象。不能先用(2)证明正性，再把测度改为普通计数或中心化phase密度而沿用同一Herglotz/source结论。

## 3. 实际正Hilbert载体和原du源

这里只消费实际谱测度本身：

    𝓗_(X,α)=L²(R,dμ_(X,α)/(2π))，
    J_(X,α)r(t)=hat r(t)=∫_R r(u)exp(−itu)du，
    Q_(X,α)(r,s)=∫ hat r(t)overline{hat s(t)}dμ_(X,α)(t)/(2π)
               =Σ_k hat r(t_k)overline{hat s(t_k)}/D_X(t_k)。 (6)

源空间仍为原physical r=e^(u/2)bare的L²(I,du)，第一槽linear，原Fourier规范及Plancherel1/(2π)保持。正性Q(r,r)≥0由真实Hilbert范数直接给出；不是假设未知Weil正号。

不把(6)无条件认成modelspace K_(B_X)=H²⊖B_XH²的投影范数。一般two-sided原源的Fourier方向、实际Clark restriction域与H²/modelspace角色需要另证，本门没有消费这种识别；谱测度与(6)已经足够作首检。

为明确(6)在原源域确实有限，并排除漏掉weighted tails，给一个不借source导数的统一估计。对z=t+i，p=2这个固定因子满足

    |b_2(t+i)|≤m:=(1/2+1/√2)/(1+1/(2√2))<1。

这是圆盘半径1/2上disk automorphism的最大模；其余inner因子模≤1，故对全部X≥2、t∈R、α∈T，

    Re H_(X,α)(t+i)≤C:=(1+m)/(1−m)。                         (7)

用(3)的Poisson kernel在单位区间上的下界，得到同一个M<∞使

    sup_(j∈Z,X≥2,α∈T) μ_(X,α)([j,j+1])≤M。                 (8)

固定有界源窗I、W=diam I，可把所有源共同平移到[0,W]；其Fourier只乘模1相位，(6)及du内积不变。对r∈L²(I)，hat r连续且属于H¹(R_t)，并有

    ||hat r||²_L²(dt)=2π||r||²_du，
    ||(hat r)'||²_L²(dt)=2π||u r||²_du≤2πW²||r||²_du。

这里的导数来自源变量u有界，不是对r求导。每个单位区间J的初等Sobolev估计

    sup_J|f|²≤2∫_J(|f|²+|f'|²)

配合(8)给

    Q_(X,α)(r,r)≤C_0(1+W²)||r||²_du。                       (9)

所以J_(X,α):L²(I,du)→𝓗_(X,α)真实有界，常数独立X/α/频高及源导数。ALLcomplex原zero-extension Dlog源包含于这个L²域，故(6)对它们也有意义。这里不支付任何growth-I目标，也不假ordinary trace/determinant或非compact Pan下降。

## 4. 最便宜的必要门：所有边界相位都得到常数germ

取任何δ>0。对Im z≥δ，

    |b_p(z)|≤(p^-δ+p^-1/2)/(1−p^(-δ−1/2))。

取固定P_δ使右边对p≥P_δ至多1/2。小素数因子仍≤1，因此

    sup_(Im z≥δ)|B_X(z)|≤2^(-#{p:P_δ≤p≤X})→0。             (10)

只用素数无限性，不需PNT、RH或primephase随机性。由(2)，

    sup_(α∈T,Im z≥δ)|H_(X,α)(z)−1|
       ≤2 sup|B_X|/(1−sup|B_X|)→0。                       (11)

所以即使α=α_X任意变化，仍在上半平面局部统一趋于同一常数1。固定compact/germ的量词对α统一；没有把它升级成source单位球上的范数收敛。

132/136早已要求独立positive generator先在非空Euler开集匹配实际arithmetic germ。用z∈C_+、w=−iz、s=1/2+w，在Im z>1/2的绝对收敛区，目标germ已由原数据唯一规定为

    F_ar(w)=1/s+1/(s−1)−(1/2)logπ+(1/2)ψ(s/2)
                    −Σ_(n≥2)Λ(n)n^-s。                  (12)

这是完整ξ'/ξ arithmetic germ；其Euler项含全部prime powers，两个pole、Gamma均保留。沿z=iy、y→∞，s=y+1/2为实，(12)为(1/2)log(y/(2π))+o(1)，故非恒定，也不等于1。这个非恒定性已经在绝对收敛半平面，无需把ζ的未知零点当输入。

(11)因此在最便宜的已付必要门就阻止本规范候选。正型载体无条件存在不等于对齐实际Weil；这里不能以J=0或“每层positive”跳过(12)。这项判定是有限inner标准计算加132/136既有准入要求的直接组合，不据此另领一个方法类定理或数学轮。

## 5. 规范Clark测度及全部fixed原源的真实极限

保存已完成的source核对，以免把(11)误读成无穷远漏质量而仍可能匹配fullfixed源。将上半平面Cayley到圆盘，(3)给有限圆周Herglotz测度ν_(X,α)。实点t对应的测度为

    dν_(X,α)=dμ_(X,α)/[π(1+t²)]；

无穷远点质量由c_(X,α)给出，此处为0。圆周总质量为Re H_(X,α)(i)。由(11)及Herglotz/Poisson的Fourier系数唯一性，ν_(X,α)对全部α统一weak-*趋于Haar；极限在无穷远点无原子。因此

    μ_(X,α) → dt vague，且
    ∫(1+t²)^-1dμ_(X,α)→π。                              (13)

对每个Schwartz函数f，π(1+t²)f(t)在圆周紧化处连续延拓为0，故(13)实际给∫f dμ→∫f dt。取h∈Cc∞(R)，其Fourier为Schwartz，定义

    W_(X,α)(h):=(1/(2π))∫hat h(t)dμ_(X,α)(t)。             (14)

于是每层W_(X,α)是真正正型tempered distribution，且

    W_(X,α)→δ₀于D′(R)，对每个fixed h的收敛对α统一。

特别地，对每个fixed compact smooth complex r,s，(6)趋于原du内积。由(9)及Cc∞(I)在L²(I)的稠密性，得到更准确的全部fixed原源结论

    sup_(α∈T)|Q_(X,α)(r,s)−<r,s>_du|→0，
    ∀先fixed有界I，∀先fixed r,s∈L²(I)。                  (15)

证明只需先用smooth近似r,s，(9)统一控制近似误差，再用Parseval；包括原Dlog。它是逐fixed源/固定pair的强型结论，不是sup全部单位球、moving频高或成长窗的operatornorm收敛。此处已分别付Cauchy加权与source尾，不拿vague本身偷渡|hat r|²测试。

## 6. 完整Weil身份、proper powers与固定源反测

按560/592的同一规范，完整目标在off0为

    Wζ=WΓ+2cosh(u/2)du−νζ−νζ^−，
    νζ=Σ_pΣ_(n≥1)logp p^(-n/2)δ_(nlogp)。                (16)

WΓ保actualΓ/FP-contact；2cosh保两个pole在卷积平方上的原indefinite配对。Γ/contact没有因为本候选只用prime而从目标删除。所有proper powers也仍在(16)，不是只保第一素数项。

δ₀显然不等于(16)：取a=log2的足够小邻域，只含一个positive primepower位置a。WΓ在该off0邻域光滑，pole背景也光滑，而(16)含非零原子−a/√2·δ_a。Contact全在0，此处exact不见。

还可在原源接口内给同一固定反测。取实η∈Cc∞(-1,1)，||η||du=1，η_ε(u)=ε^-1/2η(u/ε)，令

    r=τ_(a/2)η_ε，s=τ_(-a/2)η_ε，
    h_ε=r*s#=τ_a(η_ε*η_ε#)。

取ε>0足够小，使h支撑不碰0/其它primepowers；h(a)=1，||h||L¹=O(ε)。故

    δ₀(h_ε)=0，Wζ(h_ε)=−a/√2+O(ε)。                       (17)

固定一次ε使背景绝对值≤a/(2√2)，即得与δ₀至少a/(2√2)的mixed-pair gap。r,s及其四平方极化源都是fixed compact smooth/原Dlog；若候选对全部fixed complex卷积平方趋于完整Q_W，四平方极化就会迫mixed项也收敛，与(14)/(17)矛盾。此处差测试不被误称为单个positive square；只否定全部fixed-source匹配，未声称actualQ_W负。

式(4)中的phase primepower信息并没有证明候选没有算术信息。准确地说，中心化phase导数的Fourier型

    (1/(2π))∫hat h(t)[D_X(t)−θ(X)]dt
       =Σ_(p≤X,n≥1)logp p^-n/2 [h(nlogp)+h(−nlogp)]      (18)

确实回收全部有限primepower正周期数据。但(18)不是规范Clark测度(5)；它中心化且可signed，目标还需其负号与原Γ/双pole。把(18)代入旧560/137只是保留的完整signed身份，不是本正测度突然已经匹配Weil。普通计数、phase density、Clark权不能在这一步合并。

## 7. 强旧归因、停止及未判范围

本候选不由594的自伴prime-linear域自动判败，也不假它是592的正edge周期测度；079的无零正常determinant前件同样未被强套。有限B_X在上半平面确有零点，且B_X→0正是不能从Hurwitz“非零极限”分支拿结论的情形。这里实际使用的是直接(10)/(11)，以及更早132/136的非恒定germ必要门；137已付inner代数表示并不提供这个缺少的target对齐。

正载体/规范测度是真实存在的，(15)也保原du源。但它们给的是flat source identity，不是新的classicWeil正号、actual primitive、principal/整数sections/mixedRR或危险signedcore比较。这里最强可消费净后果是：**这一明确的未修正规范Euler-inner/Clark候选没有通过现成germ准入**；fixed-source核对解释同一失败，不另立数学责任。最终0/准入及计轮仍由root比较最强旧、different fresh后统一办理，本稿不操作这些状态。

停止本单一建设，不自动续clock、α网格、ordinarycount替换、source权、一般inner函数、arch dressing、Gamma添加、rank、第三prime或作者章节。不同独立生成式、真正coherent signed修复、非正常全局重整或relative/高层几何仍未排除，但此处没有为它们构造实物、赋予预算或提供Goal完成证据。长期关键principal/mixed/corecross/成长Ξ及whole4/5负惯性UPPER未改变，三Goal门仍open。

## 8. 实际执行与版本声明

只写本文件；没有修改共同状态、cadence、Goal、库或Git，没有后台进程。对外部Clark/Herglotz作者定理未新增source消费：所用正实表示、Poisson唯一性是本项目132/136/137已用的标准设施；规范原子及本候选极限的必要计算已自含写出。没有声称世界优先权，也没有用paper名给新输入背书。Hash仅认证版本，不认证命题。

本文终稿，等待parent与独立审查消费；文件存在不代root判轮或发布。
