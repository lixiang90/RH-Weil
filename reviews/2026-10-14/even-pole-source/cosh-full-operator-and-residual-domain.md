# Canonical cosh：actual Γ operator、完整 residual 与补空间范围

2026-10-14；`/root/principal_final_reverse`。按 root 唯一来源门执行；不 spawn，
只写本 owned 原稿，不改公共 STATE/cadence/Git，不建 C024，不另计研究轮。

恢复 AGENTS/README/STATE、check 后 show、同 G20261014 Goal/frontier、C023 stopped、
D20261014AC/战略与 next-positive-even-pole-source-gate。结构 check 不认证数学。
现场 HEAD `43d4b0af7fe57cbf672d85fc82e7b690fa45e7ed`，root 正在改 STATE。
当前 strongest-old whole 对照是557的4/5，不能只拿555 printed1或543 record2比较。
核必要原件405实际双矩零p/full pairing连续性，543 Γ域/双尾，555 exactcosh row，557/558范围。

## 1. 结论与未付责任

对 ALL L≥1，normalized canonical

    h_L(u)=cosh(u/2)，N_L²=L+sinh L，c_L=h_L/N_L，u∈I_L=(-L,L)，

确在原 zeroextension Γ_I 的 operator domain，且有绝对 finite C_Γ：

    ||Γ_I c_L||₂≤C_Γ，ALL L≥1。

这是原 operator 费用，不只是 form domain。hard endpoints 的跳跃已显式付款。
完整 actual operator residual 精确是

    Q_Lc_L=Γ_Ic_L+[2L+2sinh L−F_L(u)]c_L。                (1)

F_L为555原exactprime row，全部strict primepowers/原du/fullcomplex规范不变。
旧uniform PNT直接给 ||Q_Lc_L||₂=o(exp L)。它不提供小的absolute residual、
全core/complement gap、fullsignedtrace费或扣557后新的whole净值。

另外核出实际fixed-source反例：存在原合法norm1 real-even smooth r_L∈Cc∞(I_L)，
r_L⊥c_L、双pole矩exact0，而 Q_L(r_L)→0。这排除“一个cosh向量residual小便给cofinal
补空间固定正γ”的升级；不证明Q_L负，不排γ_L→0/不同growing core/paid joint修复。
两项为旧资产的domain/范围恢复，本稿 source0，无新独立正性或宏观完成。

## 2. 原 Γ、归一化与 endpoint费用

仍用原 H_L=L²(I_L,du；C)，hat f(t)=∫f(u)exp(−itu)du，Plancherel1/(2π)。
Γ(t)=Reψ(1/4+it/2)−logπ=actual2θ′，Γ0=−γ−π/2−3log2−logπ。
Γ_I是full-line form在zeroextension支持I_L上的Dirichlet realization，非regional/periodic。

直接积分给||h_L||²=L+sinh L=N_L²，所以||c_L||₂=1。
对zeroextension的c_L，

    ||c_L||₁=4sinh(L/2)/N_L，
    TV(c_L)=[4cosh(L/2)−2]/N_L。

第二式包含左右endpoint各cosh(L/2)/N_L的jump，及内部
∫|c'_L|=2[cosh(L/2)−1]/N_L；没有假设zeroextension导数是普通L²函数。
函数cosh²(L/2)−sinh L在L≥0单调下降且起值1，
故L≥1时N_L²≥sinh L+1≥cosh²(L/2)。因此两量都≤4。

L¹/BV Fourier估计在原 convention下给

    |hat c_L(t)|≤4，|hat c_L(t)|≤4/|t|（t≠0），
    |hat c_L(t)|≤4min{1,1/|t|}，ALL L≥1。                 (2)

BV integration by parts以distribution derivative的total variation支付端点；
没有通过忽略boundary term取得此uniform envelope。
若需要直接核符号，exact transform是

    hat c_L(t)=[sinh(L/2)cos(tL)+2t cosh(L/2)sin(tL)]
                 /[N_L(t²+1/4)]。

它在t=0给4sinh(L/2)/N_L，在高频给同一个endpoint1/t尾。

## 3. Uniform full-line operator norm 与原 Γ_I operator domain

543已付|t|≥1时|Γ(t)−log(|t|/(2π))|≤7/|t|。
head亦可显式付：digamma difference正级数为

    Γ(t)−Γ0=Σ_(n≥0)(t/2)²/
       [(n+1/4)((n+1/4)²+(t/2)²)]。

|t|≤1时至多(1/4)[64+Σ_(n≥1)n^−3]≤(1/4)(64+3/2)<17。
令M_Γ=max{|Γ0|+17,log(2π)+7}，则head |Γ|≤M_Γ，tail |Γ|≤log|t|+M_Γ。
(2)给

    (2π)^−1∫Γ(t)²|hat c_L(t)|²dt
      ≤(16/π)[M_Γ²+∫_1∞(logt+M_Γ)²t^−2dt]
      =(16/π)(2M_Γ²+2M_Γ+2)=:C_Γ²。                     (3)

所以zeroextension c_L属于whole-line multiplier Γ_R 的operator domain，
而不只是weighted-log form domain。对任意原supported Dlog test v，

    qΓ,I(c_L,v)=〈Γ_R c_L,v〉_(L²R)
               =〈1_IΓ_Rc_L,v〉_(H_L)。

闭型representation theorem于是给c_L∈Dom Γ_I，Γ_Ic_L=1_IΓ_Rc_L，
operator norm≤(3)。这是先whole-line强domain再restriction的合法路径，
不是从form membership直接推operator membership。
Γ_Ic_L一般不能被误写为未付boundary的Γ(t)乘原physical c_L；其boundary log behavior
全部由(2)/(3)编码。无须c_L在classicalH¹的zero-trace域。

## 4. 全prime action、signedpole与真实residual

555保原 A_L=Σ_(q<exp(2L))Λ(q)/sqrt q(T_logq^I+T_−logq^I)。
令x_−=exp(L−u)、x_+=exp(L+u)，Ψ_<(x)=Σ_(q<x)Λ(q)、B_<(x)=Σ_(q<x)Λ(q)/q。
exact a.e. row为

    F_L(u)=[e^(u/2)(Ψ_<(x_−)+B_<(x_+))
           +e^(−u/2)(B_<(x_−)+Ψ_<(x_+))]
                 /[e^(u/2)+e^(−u/2)]。

点态A_Lh_L=F_Lh_L，故A_Lc_L=F_Lc_L，全部proper powers已在两个Ψ/B中。
F_L finite-L bounded；其step boundaries不授权删掉source cross，但乘法本身合法L²。

Pole_even=2|h_L〉〈h_L|。由于〈c_L,h_L〉=N_L，

    Pole_even c_L=2N_L² c_L=(2L+2sinh L)c_L。

Odd vector sinh(u/2)与even c_L exact正交，负oddpole action为0。
完整Q的域与Γ_I相同，因为A/pole是H_L-bounded；因此上述都是operator-level等式，
其和给(1)，不是只有diagonal expectation相消。
true one-vector residual用于024时应再project P_(c⊥)Q c；其norm至多||(1)||，
但这仍不提供024所需complementγ或fullresidual Gram的其他方向。

旧uniform PNT/555原行付任意先fixedε>0的ALLu界

    (1−ε)exp L−C_ε≤F_L(u)
       ≤(1+ε)exp L+C_ε+4log2(1+2L)。

2L+2sinh L=exp L+2L−exp(−L)，故

    ||Q_Lc_L||≤C_Γ+εexp L+C_ε+C(1+L)，
    ||Q_Lc_L||/exp L→0。                                 (4)

这是先fixedε、再L→∞、最后ε任意的旧直接费用；没有effectiveε(L)或统一absolute小费。
“只得到o(exp L)”描述本稿可消费的已付强度，不是证明更强费用在数学上不可能。
不能将(4)的o项在heat exponential/Schur division中免费删掉，
也不能拿它替代root未知γ或解出signed全trace。

## 5. 实际fixed-source补空间检验：canonical单向量不付uniform gap

旧405指定非零source p=(D²+D)h=Eη₀，M_p(2)=π/6≠0，p∈P_an、双矩0。
在真实physical坐标取r_p(u)=e^(u/2)p(u)=(D²−1/4)g(u)，g=e^(u/2)h。
r_p real-even、nonzero、属于centeredS_exp；old405完整配对/physical运输给

    Q(r_p,v)=0（全部centeredS_exp v），
    C(r_p)=S_pole(r_p)=0。

这里r_p是已知全线主关系，非紧支；不把它直接冒充fixed-window合法源。
构造真正window smooth源：对L充分大，χ_L是even smooth cutoff，1 on |u|≤L−1，
support inside |u|<L−1/2，0≤χ≤1，各阶derivative uniform。
固定real-even nonnegative nonzero b∈Cc∞(−1/4,1/4)，m_b=C(b)>0。
令

    f_L=χ_L r_p，d_L=C(f_L)/m_b，z_L=f_L−d_Lb。

那么z_L∈Cc∞(I_L)、real-even、C(z_L)=0 exact；evenness还给oddpole0。
所以z_L⊥c_L且双poleexact0，不是只small moments或formalprojection。

centeredS_exp两端比任意指数快，使χ_Lr_p→r_p in同一Fréchet拓扑。
C(r_p)=0给C(f_L)=−C((1−χ_L)r_p)，其absolute tail对每个fixed N都有
O_N(exp[−(N−1/2)(L−1)])；因而d_L→0 faster than any fixed exponential。
于是z_L→r_p in centeredS_exp，norm||z_L||₂→||r_p||₂>0。
old405已付fullB/Mellin/全部pp/Γ与pole在该拓扑的continuity；physicalC坐标同构，故

    Q_L(z_L)=Q(z_L)→Q(r_p)=0。

每个z_L在window中，Q_L与全式Q值相同；这里没有将增长prime inventory的误差
从pointwise convergence偷补，所用是已付的完整S_exp连续性。
归一化w_L=z_L/||z_L||，得到实际norm1 smooth complement源：

    w_L⊥c_L，C(w_L)=S_pole(w_L)=0，Q_L(w_L)→0。            (5)

所以不可能由单c_L小residual推出某fixedγ>0对所有充分大L的
Q_L|_(c_L⊥)≥γI。若该gap成立，(5)会违反它。
这不证明任一fixedL上Q_L负，不排γ_L→0或actualgrowingcore/商域/paidΓ/residual修复。
与537固定窗严格正性相容；该源族的L确实增长，gap可随L消失。
它也不认证nonroot商覆盖，所用globalinput本来是principal关系。

另一个范围检验可直接消费old539/556：fixedL对c_L作全prime返回调制，
再删fixed cosh core，得到bounded prime/evenpole部分在c⊥仍有negative direction，
但actualΓ价格log|t|随t增长。它只阻止免费删除该bounded部分，不能给fullQ负。
本稿不把这旧noncompact机制重复计成新边界。

## 6. 最强旧/net与source止损

域与endpoint费成立；保正evenpole后的完整one-vectoroperator相消为旧555 row/PNT直接后果。
uniformΓ规范常数与实际(5)闭合缺少的消费细节，均不提供新的独立算术符号。
当前strongest-old557全source预算leading4/5仍在，未被(4)或diagonal-only状态改进。

仍open：保正pole的fullsignedtrace/arithmetic共同费用、actualcore/complementcoverage、
growinggap/residual及通常Ξ/PSD。只one-vectoro(exp L)不能登记C024，
本来源分项0停止；root统一整门/唯一下一动作及Goal运行，宏观门保持open。

前件闭合：ALL L≥1/operator Γdomain原zeroextension；unitc_L/原du/actual2θ′；
全部strictpp、receiverrow与signedpole exact；BV endpoint/Γ²全tail/complex域已付；
residual是actualQ c，不是freeR或Hilbert改造；counter是旧fixedprincipal的actualCc∞截断，
norm及exactmoments明确；fullcore/trace净费open，强旧4/5先扣、0计轮。

现场raw依赖SHA256：

- 405：`d4dd4f2934f57946e381b345f7e50fe385e6c5e65531cdce854aa0f49be3174a`。
- 543：`ce4d2d3271573e0f70df44dce7974fb8c0958557102542c149a77402b94d77e8`。
- 555：`55a3745ab8160738e2a2dde15e84290e99205df68f3b59b357d26127846a31c5`。
- 557：`5abfd13af9c955b27c5a2ea8f01d2555fa05b1df450adbedbcfe20f62d327166`。

hash固定消费版本，不代root核operator/domain、fixed-sourcecutoff或fullcore/net前件。
