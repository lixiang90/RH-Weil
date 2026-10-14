# C018：原 weighted core、完整 mixed 型与 Γ-relative 准入审查

2026-10-14；代理 `/root/c017_gamma_cross` 独立审查。
先恢复 AGENTS/README/STATE/check/show、当前 Goal/frontier、C018/D20261014S、
546 及 cycle11-source-entry 原件。初读实际 HEAD
3cebe129e1785eeaaff8f76b82152e1cbe334264，工作树 clean；STATE ready、latest546、cadence0。
子 get_goal=null 不代替 root 的 active 运行态。
只编辑本稿，不编辑 STATE/cadence/Git，也不推算研究轮。

裁定：原 source/core/carry 接口成立；真实 detail 双pole费用可一致支付。
但 signed Γ-relative prime 候选仍未获得证明或合法反例，不能标成 independent 输入。
本稿单独不产生新的 whole 惯性或正性后果，按合同属于入口 0 轮范围。

## 1. 实际对象和 weighted 投影

任意整数 N≥4，L=(log N)/2，M=N−1。令 x=e^(u+L)，则

    U_N f(x)=f(log x−L)，du=dx/x，
    H_N=L²((1,N),dx/x)。

这是原 Lebesgue-u norm 的等距运输，不把 norm 换成 dx 或带 arithmetic coefficient 的 ℓ²。
所有源先零延拓到 R_u，Fourier hat f(t)=∫f(u)e^(−itu)du。

    Γ(t)=Re ψ(1/4+it/2)−log π=actual 2θ′(t)，
    Γ₀=−γ−π/2−3log2−logπ，
    JΓ(f)=(2π)^−1∫[Γ(t)−Γ₀]|hat f(t)|²dt≥0，
    Dlog={f∈L²:∫log(2+|t|)|hat f(t)|²dt<∞}。

原 543 的 actual jump identity 是

    JΓ(f)=∫_0^∞ K(a)||τ_af−f||²da，
    K(a)=e^(−a/2)/(1−e^(−2a))。

不是 regional/periodic 型，不消费 016/017/023 的旧 half normalization。
完整自然 cells J_n=(n,n+1)、ell_n=log((n+1)/n) 分割整个 (1,N)。
原 norm 正交投影为

    (P_NF)|_(J_n)=ell_n^−1∫_(J_n)F(x)dx/x，R_N=I−P_N。

其 normalized basis e_n=1_(J_n)/sqrt(ell_n)，rankP_N=M。
R_N 的条件是各格 ∫F dx/x=0，不能换成 ∫F dx=0。
各 e_n 在 u 上是有限 BV step，hat e_n(t)=O_N(min(1,1/|t|))，
故既在 Dlog，也在 actual multiplier 的 operator domain（log² Fourier weight 可积）。
对每个 fixed N，P_N:L²→Dlog 有界，R_N 保 Dlog；没有得到 uniform-N 的 Dlog projection norm。

step head 本身一般不是 smooth 源。它可在原 Dlog 由 Cc∞((-L,L)) 逼近；
这些 smooth approximants 一般不留在 piecewise-constant P_N 中。
不把一个只含有限 step basis 的 head 宣称为含非零 smooth basis。

## 2. fixed-source 的真实 form-core 逼近

令 g∈Cc∞((-A,A)) 固定。对 N 足够大，所有与 supp g 相交的 u-cells
位于该 compact 的 O_A(N^−1/2) 邻域，数目 O_A(sqrt N)，最大宽度

    epsilon_N≤C_A N^−1/2。

P_N 在 u 上就是每个该格的 du 平均。令 r_N=P_Ng−g（全线零延拓）。
由 g 的 Lipschitz 性，||r_N||∞≤C_g epsilon_N，支撑长 O_A(1)，
故 ||r_N||_1≤C_A,g epsilon_N。
每格内部 variation 来自 −g′；相邻平均的 jump≤C_g(ell_n+ell_(n+1))。
相关 cells 的总长度 O_A(1)，所以 Var(r_N)≤C_A,g，与 N 无关。
有限 BV 的全轴 Fourier 估计给

    |hat r_N(t)|≤C_A,g min(epsilon_N,1/|t|)。

分别在 |t|≤1/epsilon_N 和其外积分 log(2+|t|)，得到

    ||P_Ng−g||Dlog²
    ≤C_A,g epsilon_N[1+log(1/epsilon_N)]
    =O_A,g(log N/sqrt N)→0。                            (1)

这是真实 fixed form-core 捕获，强于仅 L² 密度；接口准备是对的。
但 (1) 不对 arbitrary N-dependent/growing core 一致，也不支付其 Q 的符号或 P/R coupling。

## 3. strict 全primepowers 的 carry 和 adjoint

所有整数 q≥2 的 partial translation 是

    T_qF(x)=1_(1,N)(qx)F(qx)，
    T_q*F(x)=1_(1,N)(x/q)F(x/q)。

原 dx/x Jacobian 为 1；T_q 是 contraction，有限区间上不酉。
actual prime operator 是有限自伴和

    B_N=Σ_(2≤q<N)w_q(T_q+T_q*)，w_q=Λ(q)/sqrt q。

Λ 在全部 proper primepowers 取值，strict q<N；q=N 的平移没有正测度 overlap。
令 F_n(v)=F(n+v)，0<v<1。对每个 q，whole correlation exact 为

    〈T_qF,F〉
    =Σ_(1≤n≤M)Σ_(0≤j<q, qn+j≤M)
       ∫_(j/q)^((j+1)/q)
          F_(qn+j)(qv−j) overline(F_n(v)) dv/(n+v)。      (2)

所有 j carry 都存在，不能删到 only j=0 的 divisibility graph。
换 w=qv−j 后 dv/(n+v)=dw/(qn+j+w)，是 exact 原 target weighted measure。
N 为整数，target 裁尾在完整整数 cell 端点，不留 fractional-target 误差。
(2) 对所有 independent complex L² profiles 成立，无 smooth/scalar 替代。

R 的 weighted 平均给

    ∫_(J_n)T_q(RF)dx/x
    =∫_((qn,q(n+1))∩(1,N)) RF(y)dy/y=0。

所以 whole-source identities 精确是

    P T_q R=0，R T_q R=T_q R，R T_q* P=0。              (3)

反向 R T_q P 与 P T_q* R 一般非零。
例如 N=4，p=e_2，则 T_2p 是 J_1 的前半格 (1,3/2) 上的非零 step；
r=R T_2p≠0 在原 Dlog，〈T_2p,r〉=||r||²>0。
因此 full selfadjoint B_N 不是 P/R block diagonal。
这只核反向 mixed 接口，不重登记成新的 prime 负性结果。

mean block 也必须保 carry：

    〈T_qe_m,e_n〉=sqrt(ell_m/ell_n)
       if qn≤m≤min(q(n+1)−1,M)，otherwise 0。

所以 C017 的 thincomb logM matrix norm 不适用于完整 cells；两对象不可混用。

## 4. actual R Q P：Γ、反向prime、两个pole均保留

采用 inner product linear in first argument。对 p∈P_NH_N、r∈R_NH_N∩Dlog，
运输回 u 后 〈p,r〉=0。完整 mixed sesquilinear form 精确为

    Q_L(p,r)=JΓ(p,r)
              −Σ_(q<N)w_q〈T_qp,r〉
              +A_+(p)overline(A_−(r))
              +A_−(p)overline(A_+(r))，                (4)

因为 (3) 消去的只是 〈T_q*p,r〉。
这里

    JΓ(p,r)=∫_0^∞K(a)〈τ_ap−p,τ_ar−r〉da，
    A_+=N^−1/4∫_1^N F(x)sqrt x dx/x，
    A_−=N^1/4∫_1^N F(x)/sqrt x dx/x。

Γ mixed 在原 Dlog 上由 Cauchy–Schwarz≤sqrt(JΓ(p)JΓ(r)) 合法；
p 在 actual Γ operator domain，故也可写 fixed-N finite-rank RΓP，不能据 finite rank 忽略成长 norm。
zero cell 平均不消去 A±，也不消去 JΓ(p,r)。
例如 p 支撑一格，r 是相邻格 interior 的 smooth 零均值源；
Γ mixed 是 −∫∫K(|u−v|)p(u)overline(r(v))du dv。
对 r 格，积分 p 后所得函数严格单调非恒定，故存在 zero-mean smooth r 使 mixed≠0。
(3) 不是完整 Q 的极化消失定理。

所有 identities 保留 actual Γ、全部 strict pp、原 norm 和两个 dual poles；
误差为 exact 0，没有隐藏 cutoff、临界 inverse 或有限矩阵费用。
Γ/prime 的 mixed 大小尚未被 uniformly paid，这与“接口 exact”是两件事。

## 5. detail 上两个pole的统一同源费用

令原 u 函数 a=e^(u/2)、b=e^(−u/2)，压到 R 后写 a_R=Ra、b_R=Rb。
对 r∈R，A_+(r)=〈r,a_R〉、A_−(r)=〈r,b_R〉，故

    R Pole R=|a_R〉〈b_R|+|b_R〉〈a_R|。

每 cell 的 weighted probability variance≤range²/4（直接展开
E[(X−min)(max−X)]≥0 并完成平方即可证明）。
在 x 上，a=N^−1/4 sqrt x、b=N^1/4 x^−1/2。使用

    ell_n≤1/n，sqrt(n+1)−sqrt n≤1/(2sqrt n)，
    n^−1/2−(n+1)^−1/2≤1/(2n^(3/2))，

逐 cell 给

    ||a_R||²≤(N^−1/2/16)Σ_(n≤M)n^−2≤N^−1/2/8，
    ||b_R||²≤(N^1/2/16)Σ_(n≤M)n^−4≤N^1/2/12。         (5)

最后用 elementary integral bounds Σn^−2≤2、Σn^−4≤4/3，不需数值。
所以所有 N≥4、所有 complex detail 源都有

    ||R Pole R||≤2||a_R||||b_R||≤1/sqrt24，
    Pole(r)≥−(1/sqrt24)||r||²。                        (6)

这是同源 payment，保两个 signed poles，未加 parity/moment 假设。
若要精确而非 norm 费用，可按 rank-two Gram 计算：

    c_R=〈a_R,b_R〉，P_R=||a_R||||b_R||，
    eigenvalues=c_R±P_R。

c_R 为同一格上递增 a 与递减 b 的 covariance 总和，严格负；detail pole 不是正型。
zero-mean 不能删除它。

(6) 不支付 R Pole P：该 mixed 块还含 b_R 对 Pa 等。
full ||a||、||b|| 都是 O(N^1/4)，b_R 的 norm 亦允许 O(N^1/4)；
从 (5) 只能给其中一项 O(sqrt N) 的 upper bound，不能称必要费或已经有反例下界。
本 detail 费用只减少一个单独 ledger，未与 prime/Γ 产生新 whole 谱后果。

## 6. Γ-relative 候选为何仍 open

当前候选是固定 0<eta<1、absolute C，使所有整数 N≥4、全部 r∈R_N∩Dlog 满足

    〈B_Nr,r〉≤eta JΓ(r)+C log N||r||²。                 (7)

保 whole signed sum 后，它精确等价于

    (2π)^−1∫_[R] [b_N(t)−eta Φ(t)]|hat r(t)|²dt
       ≤C log N||r||²，
    b_N(t)=2Σ_(q<N)w_q cos(t log q)，Φ=Γ−Γ₀。          (8)

(8) 仍有所有 cell weighted moments 的原 source 约束。
逐点 symbol bound 是足够条件，但不是 source quadratic statement 的必要条件；
单个 symbol 大值亦不能直接变成合法 R 源反例。

对每个 fixed N，bounded B_N 当然给 (7) 的一个 N-dependent C_N，
例如 〈B_Nr,r〉≤2S_N||r||²、S_N=Σ_(q<N)w_q。
旧 016/543 已知该裸费用是 sqrt N 尺度，不能当 absolute C log N。
这是仍缺的 **uniform-N signed Γ-weighted source estimate**，不是域、norm 或 carry 的 unknown。

旧 539 的 finite continuous cell-moment/carrier 反例已排 free logarithmic norm shortcut；
本稿不重新证明/计轮。那些 carriers 的 JΓ 随 log|omega| 增长，
旧反例没有对 N 的 uniform phase-return height upper bound。
因此它不能否定 (7)，也不能给 R Q R 负值。
反过来，forward invariant、P fixed-core 捕获和 (6) 都未提供 (8) 的 arithmetic concentration 付款。

常见省费尝试的准确失败范围是：

- 按每 q contraction 相加，仍为 2S_N，丢失需要的 joint signed 信息。
- 只用 local zero-mean，即便核清 carry，也不能将 forward invariance 换成 B 的正性或小 norm。
- 用已有高矩坏集 measure，仍须对所有合法 R 源的 |hat r|² 支付 concentration；
  measure 本身不是同源 inequality。
- 用 high-frequency simultaneous return，只在给出 joint-N 的 Γ 返回费后才能成为 (7) 反例；
  当前没有这个可消费量，不凭“可以返回”声明 eta<1 失败。

本代理未得到 (7) 的新证明或反例，保留为 open，而不是假装 partial 图或 pole 单独能付它。

## 7. 净后果、结算及唯一责任

如果 (7) 真付清，R 上

    Q_L(r)≥(1−eta)JΓ(r)+(Γ₀−C log N)||r||²
                    +2|C_even(r)|²−2|S_odd(r)|²。

finite head rank M 和 odd pole rank 1，再用旧 028/actualΓ负迹桥，
确可给 polynomial whole count（指数 C/(1−eta)、logN 因子，常数另含 Γ₀/eta）。
这条后果是 conditional；不把表示/投影/triangularity/本 pole norm 提升为已证 polynomial count。
PSD、P_N 最低值、真实 mixed Schur 及 Ξ 识别仍另付。

问题：density-compatible detail 能否取得完整 signed Γ-relative arithmetic 费用？
已核：原 weighted P/R、Dlog fixed-source approximation、全部 carry/方向、exact mixed式，
及 detail 两pole的统一费用 (6)。
未付：(7)/(8) 的 uniform arithmetic source inequality；reverse prime/Γ mixed 的净费用。
瓶颈：source/core 接口已清楚，但主 Γ-relative 算术输入没有改变。
范围裁定：本稿 alone 是准入准备/单账本 payment，入口 0 轮；不扩为完整方法失败或新 whole 谱后果。
下一唯一责任：用真实 signed concentration/near-product 原定理付款 (8)，
或给合法 R 源、joint-N 与 Γ cost 的完整反例；仅另写 unknown domination 不构成新输入。
宏观 Goal 保持 open，原≤538基线和暂停路线不变，是否另有本轮新结果由 root 复核后统一结算。
