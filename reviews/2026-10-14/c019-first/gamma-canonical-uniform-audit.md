# C019：canonical head 的 actual Γ 全频统一算子费用

2026-10-14，`/root/c017_gamma_cross` 独立证明。
恢复 AGENTS/README/STATE/check/show、当前 Goal/frontier/C019/D20261014T，
读 547 §4、原 canonical 短审、543 的 actual Γ 尾与旧 023 的规范纠正。
初读 HEAD 812d76d7af702ea815c2376aa228f6ba8990543b、工作树 clean，
STATE C019 ready/latest数学546/cadence0。子 get_goal=null 不代替 root active Goal。
仅编辑本稿，不编辑 STATE/cadence/Git；不自行计研究轮。

## 1. 所证量词、原norm与算子

对所有整数 N≥4，L=(log N)/2、I=(-L,L)、M=N−1，
原 complex H=L²(I,du)，源在 I 外零延拓。令

    a_N(u)=e^(u/2)1_I(u)，x=e^(u+L)，du=dx/x，
    a_N(x)=N^−1/4 sqrt x，
    P_N 为完整整数 cells (n,n+1) 的 dx/x 均值正交投影，
    p_N=P_Na_N，r_N=R_Na_N=a_N−p_N，R_N=I−P_N。

Fourier 为 hat f(t)=∫f(u)e^(−itu)du、Plancherel 因子 (2π)^−1。
用 G 表示全线 actual multiplier operator

    Γ(t)=Re ψ(1/4+it/2)−logπ=2θ′(t)，
    Dom G={f∈L²(R):∫Γ(t)²|hat f(t)|²dt<∞}，
    ||Gf||²=(2π)^−1∫Γ(t)²|hat f(t)|²dt。

本稿严格证明

    a_N,r_N,p_N∈Dom G，
    ||Gp_N||/||p_N||<100，所有整数 N≥4。                (1)

而且

    ||Gr_N||/||p_N||=O(logN/N^1/4)=o(1)。              (2)

这是 actual operator norm，包含完整 Γ、两频尾与原零延拓边界；不是 half form bound。
区间 Γ_I 是原零延拓闭型的 killed/compressed realization。
对 p_N∈Dom G，原 form pairing 的代表是 Γ_Ip_N=1_I Gp_N：
对任意 g∈Dlog、supp g⊂I，qΓ(p_N,g)=〈Gp_N,g〉=〈1_I Gp_N,g〉。
因此 p_N 也属 Dom Γ_I，且

    ||Γ_Ip_N||≤||Gp_N||，||R_NΓ_Ip_N||≤||Gp_N||。        (3)

没有假设 R 与 Γ 交换，也没有把 periodic/regional realization 换进来。

## 2. actual Γ 的显式全轴费用

原 543 §4 从 [NIST Binet 积分](https://dlmf.nist.gov/5.9#E15)和 recurrence 已核

    Γ(t)=log(|t|/(2π))+epsilon(t)，
    |epsilon(t)|≤7/|t|，|t|≥1。                        (4)

原 023 的 digamma 差分正级数在乘回 actual 因子后给 Γ 对 |t| 单调。
Γ₀=−γ−π/2−3log2−logπ，既有 elementary 常数给 |Γ₀|<6。
由 (4) 在 t=1 的上界，|Γ(t)|≤7（|t|≤1）。
ln(2π)<2（π<22/7、e>8/3 已足够），故 |t|≥1 时

    |Γ(t)|<log|t|+9。

因此对所有 t，有一个可用的统一界

    |Γ(t)|≤10[1+log(2+|t|)]。                         (5)

明确固定常数

    IΓ=(2π)^−1∫_R Γ(t)²/(1/4+t²)dt

是有限的。双频尾与 head 的完整付款为

    IΓ≤(49/π)∫_0^1 dt/(1/4+t²)
         +(1/π)∫_1^∞(log t+9)²dt/t²
       <49+101/π<83。                                (6)

尾 integral 精确为 2+18+81=101；没有频率 cutoff remainder 未付。
这是对已经核准 actual Γ 工具的显式消费，不是新的算术正性来源。

## 3. 原 a_N 的 exact Fourier 与统一算子norm

直接积分，不近似 source 或端点：

    hat a_N(t)
    =[e^((1/2−it)L)−e^(−(1/2−it)L)]/(1/2−it)，
    ||a_N||²=e^L−e^−L=N^−1/2 M。

两端 triangle 给

    |hat a_N(t)|²
    ≤(e^(L/2)+e^(−L/2))²/(1/4+t²)
    ≤3||a_N||²/(1/4+t²)，                            (7)

因为 s=e^L=sqrt N≥2 时 numerator/||a_N||²=(s+1)/(s−1)≤3。
从 (6)–(7)，

    ||Ga_N||²≤3IΓ||a_N||²<249||a_N||²，
    ||Ga_N||<16||a_N||。                              (8)

这也证明 a_N 的 global multiplier operator domain，虽有两端 zeroextension jumps。

## 4. Ra_N 的 L¹、全线BV与 log² 全频误差

置 ell_n=log(1+1/n)，d_n=sqrt(n+1)−sqrt n。
p_N 每格的原 weighted 平均 c_n=N^−1/4·2d_n/ell_n 随 n 严格递增，
且位于该格 a_N 的两端值之间。
逐格 range 直接给

    ||r_N||_1≤N^−1/4 Σ_(n≤M)ell_n d_n
              ≤(N^−1/4/2)Σ n^−3/2
              ≤(3/2)N^−1/4=:A_N。                    (9)

原 du measure 保留；这里只用 ell_n≤1/n、d_n≤1/(2sqrt n)及 integral sum≤3。
BV 必须包含 I 两端的零延拓跳跃。每格内部 r_N′=a_N′=a_N/2；
内部 step jumps 为 c_(n−1)−c_n，绝对值总和 c_M−c_1；
两端 jumps 绝对值为 c_1−a_N(−L)、a_N(L)−c_M。
所以 full-line variation 恰为

    Var_R(r_N)=2[a_N(L)−a_N(−L)]
               =2(N^1/4−N^−1/4)≤2N^1/4=:V_N^BV。       (10)

若遗漏两端，便少付了一项。本证明没有遗漏。
有限 BV 的 distributional integration by parts 给完整频轴

    |hat r_N(t)|≤min(A_N,V_N^BV/|t|)。                  (11)

令 T_N=V_N^BV/A_N=(4/3)sqrt N>1、W_N=1+log(2+T_N)。
对 |t|≤T_N，以 A_N 界积分；对 |t|≥T_N，以 V_N^BV/|t| 界积分。
前段 ∫_0^T [1+log(2+t)]²dt≤T[1+log(2+T)]²。
后段令 c=1+log3+logT，使用 log(2+t)≤log(3t)，得到

    ∫_T^∞[1+log(2+t)]²dt/t²
    ≤[c²+2c+2]/T≤10[1+log(2+T)]²/T。                 (12)

最后因 c≤2[1+log(2+T)]、后者≥1。
使用 (5)、双轴 Plancherel、A_NV_N^BV=3，给显式全频 operator 误差

    ||Gr_N||²
    ≤(100/π)[A_N²T_N+10(V_N^BV)²/T_N]W_N²
    =(3300/π)W_N²。                                  (13)

故 r_N∈Dom G，p_N=a_N−r_N∈Dom G，且 ||Gr_N||=O(logN)。
没有将 Dlog 的 log-weight form 域误当作 log²-weight operator 域；这里额外证明了后者。

## 5. 显式 ALL-N norm与归一化

已核 exact ||Ra_N||²=N^−1/2 U_M、0<U_M≤1/8，故

    ||p_N||²=N^−1/2(M−U_M)≥(23/32)sqrt N，N≥4，
    ||a_N||²/||p_N||²=M/(M−U_M)≤24/23。               (14)

sqrt N≥2 时 2+(4/3)sqrt N≤(7/3)sqrt N，所以

    W_N<2+(logN)/2。

令 z=N^1/4≥sqrt2，2(1+logz)/z 随 z>1 递减，
在 sqrt2 处也小于 2（log2<7/10、sqrt2>7/5）。于是

    W_N/N^1/4<2，所有 N≥4。

(13)–(14) 得

    ||Gr_N||²/||p_N||²
    <3300·128/(23π)<6400，
    ||Gr_N||/||p_N||<80。                              (15)

(8),(14) 给 ||Ga_N||/||p_N||<16sqrt(24/23)<17。
Triangle 不要求 G 与 P commute，故

    ||Gp_N||/||p_N||<17+80<100。

这证明 (1)；(13),(14) 同时严格给 (2) 的 o(1) 误差。
全零延拓 global bound 比所需的 compressed interval/R bound 更强，(3) 完整支付实际用途。
源 p_N 非零、每个整数 N≥4 均合法，未扫描 N 或拟合 ζ 零点。

## 6. 支付范围、旧工具与仍未付的算术输入

uniform 结论仅为固定 canonical p_N=Pa_N 及其 complex scalar multiples，
不是全部 P_N head 的 uniform Γ operator norm。
事实上最后 cell 的 normalized step e_M∈P_N∩Dom G，支撑宽 ell_M≤1/M；
已核 actual singlecell lower 给

    qΓ(e_M)≥log(1/ell_M)−CΓ≥logM−CΓ。

因此 ||Γ_Ie_M||≥|qΓ(e_M)| 对 N 大时发散，不能将 (1) 扩为 ||Γ_IP_N||≤100。
这项范围负对照是既有 cell 工具的直接消费，不另造研究轮。

本稿支付 547 canonical joint式中 Γp_N/||p_N|| 的 absolute fee，
没有支付 projected native E_<(N/x) 响应，critical/polylog rate、whole head/detail coupling、
R 上 Γ-relative 算术输入、惯性净后果、Ξ识别或 RH。
generic Fourier/BV/actualΓ工具和单分量 norm不能独立计作宏观数学轮。
本轮是否有完整新 joint consequence，须由 root 与算术/critical 独立审查消费后统一裁定。
固定≤538基线、原唯一cadence、暂停约束及 Goal 的完整门保持。
