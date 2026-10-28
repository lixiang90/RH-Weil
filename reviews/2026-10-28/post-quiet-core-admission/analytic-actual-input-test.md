# Post-quiet analytic首检：相位两源式有定义，但独立joint输入未形成

2026-10-28；`/root/scalar_upper_tail`当前独占任务，非quiet／quarter／C052复核续算。已恢复README／STATE、check→show、G20261027／原0c4f、cycle17／AN与当前frontier；只核必要560、577–578和585–589已付角色。无web／下载／新PDF／数值／STATE／Git／cadence操作。

**结论：本次至多尝试的一份actual两源表达可完整写出，最便宜place-mixed test也可精确执行；但它立刻化为560已有完整signed字典，没有形成独立joint signed/core输入。** 不准新数学合同／来源门，不将“尚需的净估计”重命名为输入；下面止于这一个表达，不追加第二候选。

## 1. 唯一尝试：branch-free scattering相位两源型

物理源r=e^(u/2)bare，第一变量线性；先取r,s∈Cc∞(I)，I=(-L,L)，Fourier F_r(t)=∫r(u)e^(−itu)du。对有限素数集F，沿同一实际arch／Euler scattering symbol写

    γ(w)=π^(−w/2)Γ(w/2),
    u_∞(t)=γ(1/2+it)/γ(1/2−it),
    u_p(t)=(1−p^(−1/2+it))/(1−p^(−1/2−it)),
    u_F(t)=u_∞(t)∏_(p∈F)u_p(t)。

这些symbol在real t光滑、无零、模为1。使用u_F′/(i u_F)而非某个arg分支，避免把2π branch跳跃当新contact。唯一候选为

    J_F(r,s)=(1/(2π))∫ F_r(t)overline(F_s(t))
                                    [u_F′(t)/(i u_F(t))]dt
                  +P_pole(r,s),                         (A)

    P_pole(r,s)=μ_+(r)overline(μ_−(s))
                       +μ_−(r)overline(μ_+(s)),
    μ_±(r)=∫e^(±u/2)r(u)du。

两源位置独立、保全部complex配对；pole在对角是2Re(μ_+ overlineμ_−)，恰为完整even正／odd负Lorentz型，不是两个正平方。此式是signed form，未声称positive、普通operator trace或新的几何principal读出。

每fixed F相位导数的绝对值≤C_F+Clog(2+|t|)，所以(A)在原zero-extension Dlog(I)上由weighted Cauchy–Schwarz合法；pole泛函在每fixed I由原du控制。不存在把普通L²免费当Γ域、为新Hardy trace-class公式补未付前件或改变源norm。这里只使用已有实际symbol与完整Γ，不使用未知ζ零点。

## 2. 最强旧必须先扣：该式正是已有目标

直接微分给

    u_F′/(i u_F)=Γ_actual(t)
        −2Σ_(p∈F)logp Σ_(k≥1)p^(−k/2)cos(ktlogp),
    Γ_actual(t)=Reψ(1/4+it/2)−logπ=2θ′(t)。

Gamma系数／常数是原完整FP-contact规范；finite Euler的k在log级数微分时约掉，全部proper powers保权Λ(p^k)=logp，没有多乘k或只留squarefree项。

令R_(r,s)(a)=∫r(u+a)overline(s(u))du。Plancherel给

    J_F(r,s)=q_Γ(r,s)
       −Σ_(p∈F,k≥1)logp·p^(−k/2)
                  [R_(r,s)(klogp)+R_(r,s)(−klogp)]
       +P_pole(r,s)。                                  (B)

这已经是560的exact arithmetic side。F包含p<e^(2L)后，support外相关严格为0，所以对全部同窗Dlog源(B)恰为完整B_(Wζ)(r,s)，不是新的cofinal误差估计。若记实际ordinary Sonin正迹配对T_F，则

    T_F(r,s)−[J_F(r,s)−P_pole(r,s)]
                         =〈r,K_(F,I)s〉                 (C)

仍恰是560已有完整Gram逆／returns误差；没有产生独立于K的signed预算。对fixed源说(C)净差有界或有极限，也只是旧exact恒等式，不是新增有利方向。

## 3. 已执行的最便宜test：两个visible places的connected增量为0

取F中未含的不同素数p、q，定义Δ_pJ_F=J_(F∪{p})−J_F。由实式(B)，逐项精确有

    Δ_pΔ_q J_F(r,s)=0                                   (D)

对全部complex r,s成立。该零不是source pairing为零，而是**加入两个place的connected finite difference**为零：相位log导数已经把它们强制拆成两个已知线性prime-power块。这里没有实际非交换／joint系数留下来承担core比较。

首检不是因为各一阶变化也为0。用587的同一正flat bump r₀，support[-1,1]，R₀(a)>0对0<a<2，取F=∅、p=2、q=3，则

    Δ₂J_∅[r₀]
      =−2log2[2^(−1/2)R₀(log2)+(1/2)R₀(2log2)]<0,
    Δ₃J_∅[r₀]=−2log3·3^(−1/2)R₀(log3)<0,
    Δ₂Δ₃J_∅[r₀]=0。

所有可见proper powers已列全：2³的log>2、3²的log>2，相关为0。Pole／Γ在place增量中精确相消，未从完整目标删除。这个纯符号test不需有限网格、ζ零点、数值或新的参数。

它只否定“本相位重写提供了新增place-joint信息”的说法，不否定Euler结构能够通过其他真实耦合或独立算术估计参与RH；非零Δ_pΔ_q也不是一切成功方法的数学必要条件。

## 4. 577–589与whole最强旧比较

577已经用完整Γ／线性P／双pole造出合法正层，并付Γ协同O(R⁻²)／原Dlog运输；未付的是实际negative-part修补的小预算。578的Stieltjes signed式和ordinary Selberg／Euler平方区别，也已把线性place数据、乘积频率与差频率分清。(A)没有新增一份能付款的二源cofactor，不能拿已有相位导数重新命名该缺口。

585使fixed源T和K共同成长，固定T−K已由560精确固定；587付fixed-degree共同费用，588付weak-nonzero moving源，589付scalar归一化的均值秩一。Quiet旧组合再给真实低能逃逸及有利的K负谱。它们均未给K不利正部与T／pole／cross的完整有利比较，不能从两个反向费用界拼出净正号。

最强whole542+555→557仍是leading4/5负惯性UPPER，(A)–(D)没有改它。特别是K的负谱在Q=T−K+P中有利，不是目标Q的负惯性；本相位等式也没有新Q正号、negative source、primitive／principal／mixed或Ξ后果。

## 5. 准确未形成与最短缺口

已形成的是(A)这一个合法双源**旧重编码**及(D)的精确首检；未形成的是一份相对560／577–578真正独立、能改变不利signed/cross箭头的actual输入。没有合格新数学合同，不把“需要K_+被控制”“需要q_R消失”作为新假设或计划交付。

对这份候选，首个缺口已经明确：scalar scattering log导数只有既知逐place线性信息，所有可能的新Gram非线性仍留在(C)同一旧K里。若未来另有实际耦合对象／恒等式或独立原norm费用，应先给其本体和源位置再准入；当前没有这样的对象。此处只是缺失输入记录，不是另排未知估计／来源章节或要求用户提供机制，也不宣称整个analytic／joint方法不可能。

本task准确止于未形成独立输入，0数学轮；不续相位参数、频带、source-rank、scalar／anchor、quiet或旧source预算，不追加第二候选。原cadence3/history53/latest589/formal17、Goal完成门open及原基线保持。仅写本独占稿，待root消费范围。
