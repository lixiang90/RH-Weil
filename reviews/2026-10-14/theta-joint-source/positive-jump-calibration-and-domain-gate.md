# Theta joint source：完整正跳校准、实际定义域与允许的正源适应

2026-10-14；独立第一来源对象/费用审查，仅写本稿，不改公共 STATE/cadence/Git。
恢复 AGENTS→README/STATE→check/show→同 G20261014 Goal/frontier/C021 stopped/D20261014AA，
入口 HEAD `1d48bd538cd176091dbec90eeca46253a1473d70`；公共工作树已有 root 编辑。
现场 collaboration inventory 为 root、principal_final_reverse、theta_joint_source、theta_macro_scope running。
子 get_goal=null，不能替代 root 实际 active Goal 观察。
固定基线 0c4f/≤538，唯一 cadence 不消费。此稿没有 C022 或新数学合同。

必要原件：405 的 Gaussian/Poisson/Mellin 常数与 principal；552 的 real→physical 坐标；
543 的 actual Γ jump；529 的标准锥边界；523 与本日 principal-quotient-norm 三审的强旧扣除。
下文只在这些原量词上推导，不用未知零点位置/低谱/间距，不按 Q 值反造正权。

## 1. 实际正权、完整对象和符号

固定 physical Fourier `hat r(t)=∫r(u)e^(−itu)du`，Plancherel 因子 1/(2π)。
actual Γ(t)=Re ψ(1/4+it/2)−logπ=2θ′，Γ0=−γ−π/2−3log2−logπ。
原全线测试域为中心化 S_exp,C，尤其包含所有 complex Cc∞；fixed window 零延拓型域是 Dlog。
对合法 r，保留全部 proper prime powers q≥2：

    Q(r)=qΓ(r)−2Σq≥2 [Λ(q)/sqrtq] Re∫r(u+logq)bar r(u)du
                 +2Re[A+(r)bar A−(r)],
    A±(r)=∫e^(±u/2)r(u)du.

compact r 时 prime autocorrelation 只有有限项；S_exp 中由全部指数半范数支付尾。
这里没有删除双 pole，或把 negative odd pole 当无穷位项。

405 给 η(r)=z(z−3/2)e^(−z)，z=πr²；h=Eη=2Σn≥1η(ne^u)。
η(0)=∫η=0、hatη=η，h^sharp=h，h>0，c(h)=d(h)=1/4。
实际 positive physical ground 为

    g(u)=e^(u/2)h(u)>0，g(−u)=g(u)，A+(g)=A−(g)=1/4.

g 及全部导数属于 S_exp。由 405 完整显式公式、552 同对象中心化，
Q(g,r)=0 对全部 centered S_exp,C。g 是 T 的源关系；它不是 P_an 中双 pole 零的主关系。
原 p=(D²+D)h∈P_an，r_p=e^(u/2)p=(D²−1/4)g；r_p≠0、real-even、A±(r_p)=0，Q(r_p,r)=0。
不得把 h/g 的非零 pole 矩与 p/r_p 的零 pole 矩混用。

## 2. ALL complex compact profiles 的完整正跳恒等式

543 的 actual Γ 核是 ν(a)=e^(−|a|/2)/(1−e^(−2|a|))，

    qΓ(r)=Γ0||r||²+(1/2)∫R∫R ν(v−u)|r(v)−r(u)|²du dv.

令 f∈Cc∞(R;C)、r=gf。定义真正非负的 joint jump energy

    EΓ,g(f)=(1/2)∫∫ν(v−u)g(u)g(v)|f(v)−f(u)|²du dv,
    Eq,g(f)=∫g(u+logq)g(u)|f(u+logq)−f(u)|²du,
    E_g(f)=EΓ,g(f)+Σq≥2 [Λ(q)/sqrtq] Eq,g(f).

即使 r 的 prime autocorrelation finite，E_g 的 degree terms 仍含全部 q，不能用 compact support 删掉它们。
全部 q 求和合法：f 的支持紧，另端 g 以任意指数衰减，Λ(q)≤logq；近对角 Γ 项用 f 光滑及 ν(a)=O(1/|a|)。
对 Γ 先用 symmetric cutoff ε<|a|<R，prime 先有限和；展开平方后再取这些合法极限。

对 real g，复平方恒等式逐点为

    |g(v)f(v)−g(u)f(u)|²−g(u)g(v)|f(v)−f(u)|²
     =(g(v)−g(u))[g(v)|f(v)|²−g(u)|f(u)|²].

因此 Γ 残余是 ∫g Γg |f|²，prime 残余是
−∫g(u)Σq wq[g(u+logq)+g(u−logq)]|f(u)|²du，wq=Λ(q)/sqrtq。
Q(g,r)=0 测全部 compact r 给 distribution、继而 continuous pointwise identity

    Γg(u)−Σq wq[g(u+logq)+g(u−logq)]
      =−P g(u),
    P g(u)=A−(g)e^(u/2)+A+(g)e^(−u/2)
          =(1/4)(e^(u/2)+e^(−u/2)).

prime sum 在每个 compact u 集正常收敛；Γg 用 symmetric small-jump integral 定义。
故 exact same-object calibration 是

    Q(gf)=E_g(f)−∫μ_g(u)|f(u)|²du+2Re[A+(gf)bar A−(gf)],       (1)
    μ_g(u)=g(u)P g(u)=(1/4)(e^(u/2)+e^(−u/2))g(u).

Γ0、全部 prime powers、原 2θ′ 与 complex cross 均已保留；没有未定 δ0 常数。
乘 g 在每个 compact 支持上是 Cc∞ 的双射，因 g>0 smooth。
因此 (1) 并不缩小全 compact physical source 类，但也没有因此给出未知正性。

## 3. μ 几何与自然 Doob 范数不是同一件事

physical 原 norm 是 ||gf||²=∫g²|f|²du；自然 positive multiplication/Doob 运输采用 g²du。
另一个 source-defined positive finite measure 是 μ_g du，且 ∫μ_g=1/8。
两者在 fixed compact 上等价，global 运输权

    κ_g=μ_g/g²=(1/4)(e^(u/2)+e^(−u/2))/g

无界；不能默默把 μ 范数称原 norm。
μ 不是从未知 Q 正值反造的，它是已知 positive g 与真实双 pole residual 给出的精确权。
它也不是已构造的 adelic intersection/Green；没有 all-place/Hodge label。

以 probability dm=8μ_g du、b(u)=tanh(u/2)，有

    A±(gf)=(1/4)[E_m f±E_m(bf)],  E_m b=0,
    Q(gf)=E_g(f)−(1/8)[Var_m(f)+|E_m(bf)|²].                 (2)

complex variance 是 E|f|²−|Ef|²。任何宣称

    8E_g(f)≥Var_m(f)+|E_m(bf)|²，ALL complex Cc∞             (3)

都恰好重新要求原全 compact Weil 正性；没有独立来源时不能把 (3) 当 Poincaré 输入。
若双 pole 矩零，E_m f=E_m(bf)=0，所需是 E_g(f)≥||f||²_μ。
正 Γ/prime jump 本身没有付清这个谱价。
E_g 的 Markov positivity 也不把完整 Q 半群变为标准锥保正；rank-two signed pole 仍在，529 的范围照旧。
此稿不复活忠实 Hilbert 酉化/临界源修正，也不把 μ 能量空间等同旧商的忠实 Hilbert 完成。

## 4. 原单 theta ground 的 sharp principal-shift 域

405 Gaussian 明确求和给 u→+∞，z=πe^(2u)：

    g(u)=2π² e^(9u/2)e^(−πe^(2u))[1−3/(2z)+O(e^(−3z))],
    r_p(u)=8π⁴ e^(17u/2)e^(−πe^(2u))[1−7/z+O(z^(−2))].

g/r_p 均 even，故两端只需反射。对 actual centered principal translate r_a(u)=r_p(u−a)，
其 source 是合法 η0 scaling 加准确 centered scalar；全部 a 保 A±=0、Q(r_a,·)=0。
自然 Doob f_a=r_a/g 属 L²(g²du) 对 ALL real a，因为其 norm 就 ||r_a||₂。
但 right-tail μ integrand 精确 leading 为

    |f_a(u)|² μ_g(u)
      =8π⁶ e^(13u−17a)
         exp{π[1−2e^(−2a)]e^(2u)}[1+o(1)].                 (4)

left-tail 同式替 u→−u、a→−a。因而

    r_p(·−a)/g ∈ L²(μ_g du)  iff  |a|<(1/2)log2.           (5)

在 a=±(1/2)log2，相应端 leading Gaussian exponent 恰抵消，但 e^(13|u|) 发散，端点不准入。
不是只核 strict 不等式后漏掉 endpoints，也不是 ordinary high-precision 诊断。
域失败只针对这个 fixed g 与 μ norm；不能扩大成全部 principal-compatible/nonlocal/domain repairs。

## 5. 合法非 compact principal profile 的实际 E 费用

为避免只凭 (1) 的 compact identity 偷换 global domain，给可复算 cutoff 费用。
设 d0=1−e^(−2)，M0=sup g，M2=sup|g''|；它们有限、由指定 Gaussian 求和独立确定。
用 symmetric small Γ 跳积分及全部 pole identity 得

    |Γg(u)|≤B+(1/(4d0))(e^(u/2)+e^(−u/2)),
    B=|Γ0|M0+M2/(2d0)+4M0 e^(−1/2)/d0.

这里 small |a|≤1 的 second difference ≤M2 a²；large ν≤e^(−|a|/2)/d0，
两真实 moments 1/4 支付 convolution 尾。于是 actual nonnegative prime degree

    Dpp(u)=Σq wq[g(u+logq)+g(u−logq)]
          =Γg(u)+P g(u)
          ≤[B/2+1/(4d0)+1/4](e^(u/2)+e^(−u/2)).

又 ∫ν(a)min(1,a²)g(u+a)da
≤[M0/(2d0)+1/(4d0)](e^(u/2)+e^(−u/2))。
合并 constant

    Cg=B/2+M0/(2d0)+1/(2d0)+1/4

给全部 joint weighted jump 的 cutoff-control density D≤Cg(e^(u/2)+e^(−u/2))。
从而 cutoff χ_R（bounded、Lip uniform，χ_R→1）的乘法 error 满足

    ∫ |f(u)|² g(u) ∫g(v)|χ_R(v)−χ_R(u)|² K0(u,dv) du
      ≤4 Cg ||f||²_μ,

并对 f∈L²(μ) 以 dominated convergence 趋零。
K0(u,dv)=ν(v−u)dv+Σq wq[δ_(u+logq)+δ_(u−logq)](dv)，
故 E_g=(1/2)∫g(u)g(v)|Δf|²du K0(u,dv)；没有漏 receiver/complex cross 或另乘 ground。
若 f∈L²(μ) 且 E_g(f)<∞，则 χ_R f→f in E_g+μ norm；用 |Δ(χf)|² 展开即可。

对 (5) 内 f_a，先 (1) 核 f_aχ_R：r_aχ_R→r_a in centered S_exp，Q→0、A±→0，
μ term→||f_a||²_μ。Fatou 先给 E_g(f_a)≤||f_a||²_μ，故 finite；
上面的 actual cutoff-control 再给 E_g(χ_Rf_a)→E_g(f_a)，从而精确

    E_g(f_a)=||f_a||²_μ， |a|<(1/2)log2.                     (6)

这些 nonzero 原主关系是 modified pole-zero energy 的合法 equality profiles。
对于 (5) 外的平移，其 compact cutoff μ norms 与 E_g(χ_R f_a) 都发散；
此句不以 cutoff 发散单独声称未截 f_a 的每一种定义域都失败。

若要完全数值独立地限定 M0/M2，令

    S0=e^(−π/2)/(1−e^(−3π/2)),
    C_v=(2v)^v e^(−v),
    M0≤2π^(−1/4) C_(9/4) S0,
    M2≤M0/4+164π^(−1/4) C_(17/4) S0.

证明在 u≥0 对 z=πn²e^(2u) 用 z^v e^(−z)≤C_v e^(−z/2)、
n²≥1+3(n−1)；η0 的 absolute polynomial ≤82z⁴（z≥π）；另一端由 evenness。
这些粗 explicit constants 只支付 domain/cutoff，不声称优化或新的 Γ-relative main bound。

## 6. single shifted/scaled ground 的必要巨费，只排该族

g_b(u)=g(u−b) 仍 actual positive source relation。
A±(g_b)=e^(±b/2)/4，μ_b(u)=μ_g(u−b)，κ_b=κ_g(u−b)。
乘任意 scalar c>0 同时把 μ 乘 c²、G² 乘 c²，κ 不变。
principal domain 成为 |a−b|<(1/2)log2；选 b=a 就准入该 principal translate。

g 的 tail 给

    κ_g(u)=(1/(8π²))exp{πe^(2|u|)−4|u|}[1+o(1)].

κ even、tail eventually strictly increasing。对 sufficiently large L，

    inf_b sup_|u|<L κ_g(u−b)=κ_g(L)
      ∼(1/(8π²))exp{πe^(2L)−4L}.                         (7)

任一 b 至少一个 endpoint 的 |u−b|≥L，给 lower；b=0 在 tail monotonic 超过 compact head 后给 upper。
范数 operator price 是 sqrt(sup κ)，不是 sup κ。
(7) 是该 single-shift/scalar 范数运输类的必要费用，**不是**完整 Q 费用下界/Goal3。
下面已付的合法 positive mixtures 明确推翻过大的延伸。

## 7. 真实 positive source mixtures 修复域及窗口费用

任一 positive finite sum G=Σ c_j τ_(b_j)g，c_j>0，是 actual E-source/positive T-radical，
finite moment α=A+(G)>0、β=A−(G)>0。同一推导给

    μ_G=G(βe^(u/2)+αe^(−u/2)),
    Q(Gf)=E_G(f)−||f||²_μG+2Re A+(Gf)bar A−(Gf).

它不用 unknown gap，仍保全部 pp、2θ′、原 norm G²。
finite mixture 的 principal-shift μ 域是

    min b_j−(1/2)log2 < a < max b_j+(1/2)log2.

端点仍由相同 e^(13|u|) tail 发散；不能 finite mixture 即覆盖 ALL a。

**一个固定 infinite actual mixture却可覆盖 ALL principal translations。**
取 G=Σn∈Z e^(−n²)τ_n g。每个 S_exp 半范数与全部导数由 Σ e^(−n²+N|n|) 控制，
故在 centered S_exp 收敛、G>0、Q(G,·)=0。
其 actual real-even Schwartz source 是

    η_G(r)=Σn∈Z e^(−n²−n/2) η(e^(−n)r),
    C(Eη_G)=G.

Gaussian coefficients 支付每个 Schwartz 半范数的 scaling e^(linear n)；
η_G(0)=∫η_G=0，经 absolute Schwartz convergence 可换序，故不是抽象命名关系。
令 m0=min_[0,1]g>0，整数 n=floor u 给

    G(u)≥m0 e^(−(|u|+1)²),
    κ_G(u)≤C exp{(|u|+1)²+|u|/2},
    C=2max(α,β)/m0.

actual r_p(u−a)² 的 double-exponential 衰减因而给
τ_a r_p/G∈L²(μ_G) 对 ALL finite real a。
一般 positive G 的 symmetric Γ/degree cutoff-control 同 §5（用 min(α,β)>0）证明
这些 profiles 的 E_G 合法，且 E_G=μ_G norm²。它们仍是关系 equality，非未知非根正性。
此合法 escape 说明“固定 g 只容纳一段 a”不能升级“任何合法 positive ground 均不容纳全部 a”。

**窗口适应的 finite lattice。** 取 M=ceil L、G_L=Σn=−M..M τ_n g。
|u|≤L 时 G_L≥m0；α=β≤e^(M/2)/[4(1−e^(−1/2))]。因此

    sup_|u|≤L κ_GL(u)
      ≤ e^(1/2) e^L/[2m0(1−e^(−1/2))].                    (8)

G_L 是明确 finite actual source，ALL window r=G_L f 的 μ 范数费用支付为
||f||²_μ≤C_g e^L||r||²₂；没有把 target norm 当原 norm。

**root 提出的 continuous cosh mixture 的不同组织逆核。**
固定 A>0，even smooth χ_L=1 on [−L−A,L+A]、support in [−R,R]，R=L+A+2，0≤χ≤1。
令 c_L(b)=cosh(b/2)χ_L(b)、G_L(u)=∫c_L(b)g(u−b)db。
compact b integral 的 actual source
η_GL(r)=∫c_L(b)e^(−b/2)η(e^(−b)r)db 满足两源消失条件和 Schwartz 准入。
Γ/T/source swapping 由 compact b 与 S_exp 控制，故也是 positive actual T-radical。
evenness 给 α=β=(1/4)∫cosh²(b/2)χ_L(b)db≤(R+sinhR)/4。
取 |v|≤A，在 window 内 u−v∈χ=1 区间；odd sinh term cancels，故

    G_L(u)≥m_A cosh(u/2),
    m_A=∫_|v|≤A cosh(v/2)g(v)dv>0,
    sup_|u|≤L κ_GL(u)≤(R+sinhR)/(2m_A)=O_A,g(e^L).        (9)

这是按源/窗口变化的 actual positive repair，已付合法性与运输价；
不得继续把 single theta 的 (7) 当全部 source-adapted positive grounds 的下界。
finite/infinite constructions 都没有 canonical adelic map、independent Hodge 或 nonroot quotient coverage 声明。

**root 提出的 ALL centered S_exp source-adaptive 域修复，另付量词。**
对任意 complex r∈centered S_exp，令

    c_n(r)=sup_|u−n|≤1 |r(u)|+e^(−n²)>0,
    G_r=Σn∈Z c_n(r) τ_n g.

c_n 对每个指数 e^(N|n|) 可求和。故 G_r 在 centered S_exp 收敛且 strictly positive；
source η_Gr=Σ c_n(r)e^(−n/2)η(e^(−n)·) 在全部 Schwartz 半范数 absolute 收敛，
仍满足 η(0)=∫η=0，是 actual E-source、Q-radical，不是按 Q 值构造。
取 n=floor u 得 G_r(u)≥m0|r(u)|。α=A+(G_r)、β=A−(G_r) finite positive，所以

    ∫κ_Gr |r|²≤m0^(−1)∫[βe^(u/2)+αe^(−u/2)]|r(u)|du<∞.  (11)

此 domain repair 是 nonlinear/source-adaptive；无 fixed linear quotient map 或 global uniform fee。
不能由 (11) 自动叫 Green/Hodge 对象或令 Q(r)≥0。

若需要 full E 定义域，须单独付以下 cutoff，而不是继承 (11) 标签：
任意 positive actual G∈centered S_exp，令 α=A+(G)、β=A−(G)、m=min(α,β)>0，
M0=sup G、M2=sup|G''|，B=|Γ0|M0+M2/(2d0)+4M0e^(−1/2)/d0。
same-object Q(G,·)=0 给 Dpp=ΓG+PG；long Γ degree ≤PG/d0，small Γ degree≤M0/d0，
且 PG≥2m。因此完整 cutoff-control density（Γ 的 min(1,a²)、prime 的全部 atoms）满足

    D_G≤C_G PG,
    C_G=B/(2m)+M0/(2m d0)+1+2/d0<∞.                      (12)

设 r∈centered S_exp，f=r/G∈L²(μ_G)，则 χ_Rr→r in centered S_exp。
compact identity 的 E_G(χ_Rf) 因 Q/A± 连续及 μ convergence 有 finite limit。
Fatou 先给 E_G(f) finite；(12) 与 μ-integrability 再给 cutoff E convergence，故 exact
global calibration Q(r)=E_G(r/G)−||r/G||²_μG+2Re A+(r)bar A−(r)。
这支付 (11) 所有 r 的 actual Γ/全部 pp energy 域（非根也可）；constant C_G 依赖所选 source。
仍未支付 balanced sign、统一 source/growth norm、principal-compatible geometry 或 Ξ。
其正跳 energy 已知非负，而它减 μ 加 signed pole的净值仍是原完整 Q；不从某项合法性升级最终效果。

## 8. 所有 positive grounds 的双 pole 必要运输价与准确范围

对任意 strictly positive measurable G，有 finite α=A+(G)>0、β=A−(G)>0，
定义 κ_G=(βe^(u/2)+αe^(−u/2))/G；不必先假设 actual T relation。
设 K²=ess sup_|u|<L κ_G(u)<∞。由 G≥(βe^(u/2)+αe^(−u/2))/K²，
在 I_L 积两个 positive moments，严格保外窗正贡献，得

    K² α≥2L α+2sinhL β,
    K² β≥2sinhL α+2L β.

αβ>0，令 d=K²−2L；两式给 d≥0、d²αβ≥(2sinhL)²αβ，故

    K²≥2L+2sinhL.                                       (10)

physical L² source→μ_G profile norm transport 所有 complex compact window profiles 的最佳 K²
就是此 ess sup（可用 compact bumps逼近高值区），因此 (10) 是该正权运输责任的真必要费用。
(8)/(9) 给实际 source/window-adapted grounds 的同阶 upper，原 single g 的巨费不是不可修复。
这只约束“positive ground + pole residual μ norm/原 L² transport”这个特定步骤；
不约束 signed profile 的 actual Q/Γ-relative 费用、不同 target norm或联合 cancellation。
单靠 e^L norm fee 不能推 actual Q negative，也没有排允许修复后的全部成长核心方法。

## 9. 强旧扣除、未付箭头与来源止损

405 已有 actual Gaussian relation、positive h、全部 Mellin/moments；543 已有完整 Γ jump；
旧 016/529 已给 prime squares/standard cone责任。把它们作 positive ground identity 是 exact old-mechanism recovery，
不是新 independent arithmetic sign。principal density/translation invariance 单线完成已由强旧 523 支付；
此 μ geometry 属另一 global unbounded weight，不能用 density shortcut排它，也不提供忠实正定 quotient。

实际本门付清：complete complex jump calibration、two measure 区分、single-g sharp shift/endpoints、
合法 principal profile 的 full energy cutoff、explicit positive actual mixtures和其 norm fees；
其中修复逃逸改变过大的停止解释，但不付 (3) 或非根 positivity。
全 Cc 的 joint energy inequality仍与原 whole Q/RH责任相同，没有独立 spectral-gap input。
fixed 537 窗正性可运输到 (2)，扣旧后无新窗口/成长 forcing；没有新增 whole count/Ξ后果。

停止：仅 old identity/unknown modified Poincaré 时来源0停，不继续调 lattice/c_L/常数、
不以某一 μ-domain 失败晋级 Goal3，不据 (10) 完成宏观 Goal。
重新准入：actual source-defined independent inequality/geometry，支付完整 E_G−μ_G 与 rank-two pole，
ALL complex/成长原 norm及非根覆盖；或在允许 source/window-adapted、joint signed 修复后仍成立的合法核心反例。
actual fullcarry/physical ΛΛ 真备选仍未付。root 决定唯一下一动作与收据，公共状态不由本稿修改。

前件闭合：domain Cc∞ complex（global principal extensions另逐项支付）；original norm L²du；
source actual Eη/η0、全部 translation/positive mixtures 明确；Γ=2θ′、全部 pp、双 pole、2π因子；
paid cutoff/μ运输与真 counter-role；remaining modifiedPoincaré/nonroot/core/Ξ open；
strong-old net 是对象恢复和修复决策信息，不是新的宏观 forcing；研究轮0。
