# Actual full-prime weighted Schur 与 whole inertia：独立逆审

2026-10-14；`/root/principal_final_reverse`。本稿只编辑当前 owned 路径，不改 STATE、
Goal、cadence 或 Git，不改之前的 principal reverse 原件。
按 AGENTS 再读 README/STATE、check 后 show，恢复同 G20261014、0c4f/≤538 基线、
Goal/frontier、C021 stopped、D20261014AA/current gate。现场 HEAD
`1d48bd538cd176091dbec90eeca46253a1473d70`，公共工作树有 root 与其他代理正在保存的文件。
本次任务由 root 明确派发；不据 stopped C021 的旧预算推断重新准入。

必要原件为 016 的原 prime graph identity（其 half-Γ 常数依纠正不消费）、
028 的 phase negative-trace 证明、543 的 actual Γ/domain/双频尾与最强旧 whole budget，
以及本目录 positive-jump 来源稿。该 Schur 推导独立于其 unknown Poincaré inequality，
也不需要未知 ζ 位置、间距、简单性、任何 matrix PASS 或 ζ 拟合。

## 1. 审查结论

root 提出的精确 row、full-source operator bound、odd-pole rank-one 处理和
actual Γ 惯性常数均成立。对全部 L→∞，同一个真实完整 prime adjacency 有

    ||A_L||=(1+o(1))exp L。

以如下 exact Schur certificate β_L≥||A_L|| 计，完整实际 Weil 负惯性满足

    n_−(Q_L)≤1+(L/π)∫[β_L+1−Γ(t)]_+dt
            =1+(4e+o(1))L exp(β_L)。

这里最后等号指右侧预算的渐近；不声称实际 n_− 达到它。
β_L=(1+o(1))exp L，因此该 certified upper budget 的 log/exp L 上限为 1。
旧 543 的已结算 record 预算 Cexp S_L 有 S_L∼2exp L，log/exp L 极限为 2。
所以相对该最强已明示 whole 预算有严格 leading-exponent 改善，且新界适用 ALL L。
全库最强旧/新颖性审查由另一组织核对；本稿不以定向搜索认证全部旧文献没有同结果。

这改善 whole 惯性预算，仍保指数危险 core。它不证明 actual negative eigenvalues 存在，
不证明 near-PSD/PSD/RH、G2、principal-compatible geometry 或通常 Ξ 识别。
本逆审本身不另外计轮；root 若消费一个新 whole 数学结果，需一次统一结算和最强旧收据。

## 2. 原对象、全源域、strict q 与 adjoint

取 I_L=(-L,L)、H=L²(I_L,du；C)，源全部 complex，零延拓到全线。
设 X=exp(2L)、a_q=log q、w_q=Λ(q)/sqrt q；q 遍历全部 q≥2、q<X，
Λ 自动只留下真实 prime powers，包括所有 proper powers。定义

    (A_L r)(u)=Σ_(q<X)w_q[
        1_(u+a_q∈I_L)r(u+a_q)+1_(u−a_q∈I_L)r(u−a_q)]。

每个 partial translation 是 H 上 contraction；两项互为 adjoint，有限和给
bounded selfadjoint operator。它在 usual positive-function cone 上保正，
并非声称其 quadratic form PSD；这两个意思必须区分。

内积第一变量线性，准确有

    〈A_L r,r〉=2Σ_(q<X)w_q Re∫_(−L)^(L−a_q)r(u+a_q)bar r(u)du。

actual complete Weil form 在原 zeroextension Dlog 上是

    Q_L(r)=q_(Γ,I_L)(r)−〈A_L r,r〉+2|C_L(r)|²−2|S_L(r)|²，
    C_L(r)=∫r(u)cosh(u/2)du，S_L(r)=∫r(u)sinh(u/2)du，
    Γ(t)=Reψ(1/4+it/2)−logπ=actual 2θ′。

没有删除 prime cross、pole 或改变 2π/half-window convention。
若 q=X，则 shift overlap 为零长度；本定义保 strict cutoff，边界 singletons 不改变型。
fixed L 的 A_L 与两 pole 均是 H-bounded perturbations；不要求 A_L 保 Dom Γ，
也不偷换 regional/periodic Γ。完整型闭、半有界，域仍是原 Dlog，Cc∞ 为原 form core。

## 3. Exact weighted row：辅助权不改变物理 norm

选 h(u)=cosh(u/2)>0。只将它用于 Schur 的 pairwise arithmetic inequality，
未把 H 换为 L²(h²du) 或 μ norm，因此没有隐藏的 norm-transport 价格。
记 strict sums

    Ψ_<(x)=Σ_(2≤q<x)Λ(q)，B_<(x)=Σ_(2≤q<x)Λ(q)/q，x≥1，
    x_+=exp(L−u)，x_−=exp(L+u)。

由 h(u±logq) 的两个指数项直接展开，exact a.e. row 为

    R_L(u)=(A_Lh)(u)/h(u)
      =[e^(u/2)(Ψ_<(x_+)+B_<(x_−))
        +e^(−u/2)(B_<(x_+)+Ψ_<(x_−))]
          /[e^(u/2)+e^(−u/2)]。

定义 β_L=ess sup_(u∈I_L) R_L(u)，finite、nonnegative。
全部复杂源的 weighted Schur inequality 可不借抽象 kernel 定理直接证明：
对每个 pair v=u+a_q，

    2|r(v)||r(u)|≤[h(v)/h(u)]|r(u)|²+[h(u)/h(v)]|r(v)|²。

在 overlap 上积分、乘 w_q，并对所有 q 求和，receiver 换元后的 coefficient 正好 R_L。
故对全部 r∈H，

    |〈A_L r,r〉|≤∫R_L(u)|r(u)|²du≤β_L||r||²。

selfadjointness 给 ||A_L||≤β_L。全部 phases、source directions 和 growing q 已一起付款，
没有只核 positive r 后漏 complex quadratic directions。

## 4. Uniform PNT 付款与真实 adjacency 的 sharp leading coefficient

只消费原 016 等已有的无条件 PNT Ψ(x)=x+o(x)，以及原 Chebyshev 上界。
strict Ψ_< 与 closed Ψ 的差在一个 atom 至多 log x，所以 PNT 同样成立。
对任意先固定 ε>0，存在 finite C_ε，对全部 x≥1：

    |Ψ_<(x)−x|≤εx+C_ε。

这来自通常 PNT 余项的定义与 finite head，并非新增 zero-free 优化。
Chebyshev 加 Stieltjes partial summation 给某绝对 C_B：

    0≤B_<(x)≤C_B[1+log x]，ALL x≥1。

关键 exact identity 是

    [e^(u/2)x_++e^(−u/2)x_−]/[e^(u/2)+e^(−u/2)]=exp L。

因此 pointwise、uniform in全部 |u|<L：

    (1−ε)exp L−C_ε ≤R_L(u)
      ≤(1+ε)exp L+C_ε+C_B(1+2L)。

令 L→∞ 后 ε 任意，得到 R_L(u)/exp L→1 uniformly，故
β_L/exp L→1。这里不先固定 u 或排 endpoint boundary layers；small cutoff 的
PNT relative error 已由同一个 C_ε 付款。B 的全部 1/q terms 也没有省掉。

此外 h∈H，Rayleigh integral 给

    ||A_L||≥〈A_Lh,h〉/||h||²≥(1−ε)exp L−C_ε。

与上界合并，真实 ||A_L||/exp L→1。h 零延拓为 fixed compact BV，属于原 Dlog；
即使只接受 smooth probes，Cc∞ 的 L² 逼近和 A_L boundedness 也支付同一个 Rayleigh 下界。
这是 adjacency norm 的 sharpness，不能转成 Q 负性，因为正 even pole 和 actual Γ 仍在。
它只说明任何更好的 scalar norm certificate for A_L alone 不能把 leading 1 降低；
full signed Γ/pole/core 或非标量修复没有被排除。

β_L 也是 finite-arithmetic exact certificate，而非一个未给对象的 existence bound。
breakpoints 为 u=L−log q 和 u=log q−L（只保位于窗口者）。在各 open cell 上，
上述四个 strict sums 都是常数，所以 R_L(u)=(e^u a+b)/(e^u+1)，其导数符号固定。
因此 essential supremum 是 finitely many cell endpoints 的 one-sided limits 与窗口端点
limits 的最大值；singletons 的 strict convention 单独保留，不把 point value 当 ess sup。
不需要为该数学证书盲增 N、运行普通矩阵或拟合 ζ 零点。

## 5. Pole rank、原 Γ negative-trace 与 4e 常数

由 A_L≤β_L I 且 even pole positive：

    Q_L≥Γ_(I_L)−β_L I−2|s_L〉〈s_L|，s_L(u)=sinh(u/2)。

若 V 是严格负的 Q_L 子空间，则 V∩ker S_L 至多少一 complex 维；
其上 Γ−β≤Q_L<0。因此严格 min–max 给

    n_−(Q_L)≤1+n_−(Γ_(I_L)−β_L)。

只加 odd pole 的 rank one；不以 signed rank-two norm 替代，不加两维，
complex multiplicities 也不再乘二。positive even pole 不需要额外排一维。

原 Γ_I compact resolvent 与自然闭域已有 543 原证明；bounded perturbations 保它。
对任意 δ>0，λ<β 的 Γ eigenvalue 在 [Γ−(β+δ)]_- 中贡献>δ，所以

    n_−(Γ_I−β)≤δ^−1 Tr[Γ_I−(β+δ)]_-
      ≤L/(πδ)∫[β+δ−Γ(t)]_+dt。

最后一行正是 028 的 Bessel evaluation-density 证明，在 actual positive multiplier
Φ=Γ−Γ0、threshold β+δ−Γ0 上消费；原 Γ0 的负号与实际量值全部消去。
evaluation vector squared norm 2L，Fourier factor 1/(2π)，故是 L/π，未混旧半窗符号。

543 已原双尾付款：|t|≥1 时 Γ(t)=log(|t|/(2π))+ε(t)，|ε(t)|≤7/|t|。
对应 log model 的 exact integral 是

    ∫_R[a−log(|t|/(2π))]_+dt=4πexp a。

positive part 为 1-Lipschitz；在共同有效 tail support |t|≤2πexp(a+7) 内
∫7/|t|dt=O(a+1)，fixed head 的 log singularity 可积，故

    I(a):=∫[a−Γ(t)]_+dt=4πexp a+O(a+1)，a→∞。

actual 2θ′ 和两条频率尾决定 4π；若误用 half-Γ 会改变指数，不能继承历史常数。
取 δ=1、β=β_L→∞，即得 root 的 exact budget 及

    n_−(Q_L)≤1+(4e+o(1))L exp β_L。

若优化 δ，I(β+δ) 的相对误差对 β+δ≥β 一致趋零，inf_(δ>0)e^δ/δ=e，
所以 scalar-family optimized leading constant 同为 4e；不靠固定 δ 隐藏更强旧优化。

## 6. 严格净值、指数误差与仍未付的核心

记本次 issued budget B_new(L)=1+(L/π)I(β_L+1)。由 β_L∼exp L，

    log B_new(L)/exp L→1，ALL L→∞。

不能写 B_new=(4e+o(1))L exp(exp L)：β_L−exp L 只知道 o(exp L)，
可以在指数中产生无界 multiplicative error。原证明保 exact β_L；
只在 logarithmic leading coefficient 或 exp[(1+o(1))exp L] 意义消费。

旧 543 在同一个 cofinal record family 上已付 B_543≤Cexp S_L，
S_L=Σ_(q<exp(2L))Λ(q)/sqrt q∼2exp L（原 PNT/partial summation）。
它比 old optimized scalar (4e+o(1))Lexp M 强 O(L)，必须用这条更强预算作对照。
而 log(Cexp S_L)/exp L→2，且

    B_new(L)/(Cexp S_L)→0

沿同一 record family 成立。这比较两个 certified upper budgets；不推出 actual n_− 的下界
或真实数目已经按某比例减少。对任意 L，新证书另给 ALL-L leading ≤1；
不误称旧 543 的 record 特殊结论本来已是 ALL L。

新门不消费 theta positive-jump unknown sign，也不需要 source→μ 的 e^L norm 换算。
辅助 Schur h 不是 arithmetic source/quotient/Green map；其职责是原 complete prime
operator 的全源上界。PNT 是独立已知算术输入，新的责任是把它以正确 receiver rows
组合进同一 full Q，保 actual Γ 和 odd-pole rank。

仍未付：Γ-relative/fullcarry quasipoly 费用、PSD 或 o(1) cofinal 下界、危险 core 的
same-source coupling、principal-compatible arithmetic geometry、完整谱支/通常 Ξ。
leading 1 的指数预算改善不支付这些条件，不能按 contract 完成而结束宏观 Goal。
root 需结合另一组织的最强旧扫描决定是否记录一个新 whole 结果；此独审不自行计轮。

## 7. 原件依赖与前件闭合收据

本次直接付费依赖如下，均只消费其已经证明的适用范围。

| 原件 | 消费的原事实 | 不消费的更强结论 |
|---|---|---|
| 016 §§1、2、5 | exact partial-translation prime graph/degree 与无条件 PNT/partial summation | 历史 half-Γ 正块/旧数值；unknown joint Hodge domination |
| 028 §1 | 原 L²/complex Bessel negative-trace，threshold 可任意平移 | 未给的 cofinal residual Schur sign、prolate 全 core 费用 |
| 543 §§1–4、6 | actual full Q/domain、Γ positive graph、compact resolvent、双尾误差/4π 与 optimized 4e | 将 degree heat profile 自动用于新 adjacency；温度账本当实际 count 下界 |
| 543 §§5–7 | 已结算 record B≤Cexp S、S∼2exp L 及该热账本 leading S | 该 record 界扩成 ALL L；fixed ledger 边界排全部 joint/core 修复 |

现场原件 raw SHA256：

- 016：`56c14fbc3357392a21924bc6a4e7bbe1fa6e10ab3a2809509ae0e080277aa4fd`。
- 028：`3fff3593894a1074601d3874351d5e67bc26e25c3a50c6013040ebc4899aceae`。
- 543：`ce4d2d3271573e0f70df44dce7974fb8c0958557102542c149a77402b94d77e8`。
- 被特指的旧 035：`6488a0344fe45fcd918da8c309746b9473eb0cf050213c07e88f0a293b0d8a91`。

另做了旧 whole 表述定向反审。035 是 Chebyshev Abel-energy 收敛横坐标与 RH 等价，
不是已经付清的 actual Q_L 全源惯性估计；其 critical tail 不从通常 PNT 自动成立。
027 给合法 phase-volume 运输，但其证明本身未给比本次 leading 1 更强的 arithmetic
symbol bound。150 的 square-root Cauchy-core localization、275 的 growing low-frequency
response 和 record path 属于各自 Abel/Brownian 对象；其完整 Weil/core 桥仍有原条件，
不能把已付子系统指标免费改为同对象 n_−Q_L。542 已准确恢复旧 degree/028 强基线，
只降低其较弱 Fourier 对照不能重复计功。537 的 fixed L=17/16 weighted-Schur 及完整
正性有其冻结 source 数据/尾/complement 责任，不自动提供无界成长窗的 same β_L。
本稿主动保留这些强旧事实；若另组织发现同对象更强旧 whole 预算，须撤销本次净增量，
而不是继续使用较弱对照。没有声称文献首创或全文重验所有 ≤538 资产。

前件闭合字段：

- **实际对象/norm/domain：** Q_L、全部 complex L²(I_L,du)、zeroextension Dlog；
  bounded prime/pole perturbation 与原 form core，未换 μ/Doob norm。
- **source/growth 量词：** ALL L>0 exact finite β certificate；ALL r∈Dlog；
  strict q<exp(2L) 全部 primepowers；ALL L→∞ asymptotic，用同一个 PNT head payment。
- **已付误差：** Ψ strict atom≤log x；ALL-x εx+Cε；B upper C_B(1+2L)；
  actual Γ 双尾 |ε(t)|≤7/|t|；I(a) error O(a+1)；保 exact β 在指数内。
- **实际 coefficient direction：** finite full adjacency A_L 本身，receiver 双向/complex
  phases 都保；不是 fixed profile、basis diagonal、flat-label unitball 或人为谱权。
- **pole/rank：** 双 pole exact signed form仍在；只为 upper count 丢正 even rank-one，
  负 odd rank-one 给 +1；其大小不当 o(1)，complex 维数不翻倍。
- **净值：** 在原 543 certified record budget 上 log leading 2→1；
  新证书另为 ALL L，仍 exp[(1+o(1))exp L]，不声称实际 count 减半或已无负谱。
- **剩余/停止：** full signed Γ/pole/core、G2、near-PSD/Ξ/独立 arithmetic sign 未付；
  ||A_L|| sharpness 表明不继续优化纯 scalar Schur leading constant，保真正 joint 修复。

root 后续数学结算/STATE/唯一下一动作和 Goal completion audit由 root 统一办理。
本审查的完成只关闭该 reverse subtask；宏观完成门保持 open。
