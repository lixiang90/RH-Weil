# C011 第二轮：zero-extended Gaussian 的完整 time-band 泄漏上界

2026-10-14；独立解析交付，固定新基线 0c4f3a3 / 全部≤538。
本件只写显式源与全参数费用，未修改 STATE/cadence/Goal，也未计另一研究轮。
恢复已读 AGENTS、README、STATE，check/show、当前 Goal、MACRO_FRONTIER、
C011、最新策略与 D20261014L、539 原推导；现场 Git HEAD 为 d092aa73183f05c42d9e2433a4f4dd5371607d80。
子代理 get_goal 返回 null，不能解释为主线程 Goal 已停止；root 须自行核实际线程运行态。

## 1. 实际规范与冻结解析参数

令 L>0、Ω>0，I_L=(-L,L)，H_L=L²(I_L,du)，原源零延拓到实线。
Fourier 规范为

    Ff(t)=∫_R f(u)e^(−itu)du，
    ||f||²=(2π)^−1∫_R |Ff(t)|²dt。

记 P_L 为时窗正交投影，P_Ω 为 Fourier 侧频窗 [-Ω,Ω] 正交投影。
用上述规范的 unitary Fourier transform 𝓕=(2π)^−1/2 F 定义

    B_(L,Ω)=P_L 𝓕^−1 P_Ω 𝓕 P_L |_(H_L)。

其核为 sin(Ω(u−v))/(π(u−v))，对角值 Ω/π；没有多乘 L 或 2π。
0≤B≤I 且每个 fixed L/Ω 上核连续、Hilbert–Schmidt。因此

    δ(L,Ω)=inf_(f∈H_L, ||f||=1)<f,(I−B)f>
          =1−||B||。

证明 δ>0：若 ||B||=1，compact 正算子取得该最大本征值，于是存在非零 f
同时严格时限于 I_L 且 Fourier 限于 [-Ω,Ω]。时限 L² 源亦属 L¹，其 Fourier
延拓为 entire 函数；频窗外连续值为零，identity theorem 迫使 Ff≡0，矛盾。
同样 B≠0，故 0<δ<1。此处没有宣称任何成长 L 上的统一正下界。

先冻结解析族

    h_α(u)=(α/π)^(1/4) exp(−αu²/2)，α>0。

理由是其时域 norm tail 与频域 norm tail 的指数分别为 αL² 和 Ω²/α。
使较小指数最大化、且两费用恰相等的唯一 α 是 Ω/L：
min(αL²,Ω²/α)≤ΩL，两者等价当且仅当 α=Ω/L。
以下始终采用此参数；这不是拟合零点、数值选择或再运行旧矩阵 producer。
令 q=ΩL，无量纲且可取任何正数。

## 2. 完整 norm、截断与频尾费用

由 Gaussian integral，||h_α||=1，且

    Fh_α(t)=(α/π)^(1/4) sqrt(2π/α) exp(−t²/(2α))。

因此，以 erfc(x)=(2/√π)∫_x^∞ exp(−v²)dv 记两个准确 tail：

    r=||(I−P_L)h_α||²=erfc(√α L)，
    s=||(I−P_Ω)𝓕h_α||²=erfc(Ω/√α)。

冻定 α=Ω/L 后 r=s=erfc(√q)，0<r<1。取原时窗内零延拓截断源

    g=P_Lh_α，||g||²=1−r，f=g/√(1−r)。

用 Fourier 投影的 contraction 和 norm 三角不等式，完整支付截断造成的频域变动：

    ||(I−P_Ω)𝓕g||
       ≤||(I−P_Ω)𝓕h_α||+||(I−P_Ω)𝓕(h_α−g)||
       ≤√s+√r=2√r。

所以原归一化源的完整频窗外 norm 为

    <f,(I−B)f>=(2π)^−1∫_(|t|>Ω)|Ff(t)|²dt
                 ≤4r/(1−r)。                                      (1)

分母 1−r 是精确截断 norm；没有用未经支付的 full-line norm=1 替换它。
此推导不忽略正负频率，不隐藏 L-dependent 常数，不使用有限矩阵或 ζ 数据。

## 3. 所有 q>0 的严格上界

对 x>0，令 v=x+w，便有

    erfc(x)=(2/√π)e^(−x²)∫_0^∞ e^(−w²−2xw)dw < e^(−x²)。

因此由 (1)，对每个 q>0，

    δ(L,Ω)≤4 erfc(√q)/(1−erfc(√q)) < 4/(e^q−1)。       (2)

再合并独立已付的 δ<1：若 q≤log 5，δ<1≤5e^−q；若 q>log 5，
4/(e^q−1)<5e^−q。于是全 q 范围严格成立

    0<δ(L,Ω)<min{1,5e^(−ΩL)}。                         (3)

常数 5 为绝对数；没有“q 足够大”的隐含阈值，也没有 L-dependent 前件。
(2) 的 erfc 形式可更紧，但 (3) 已足以承担下面的成长必要费用。
若 Ω=0，B=0、δ=1；α=0 的 Gaussian 不可使用，(3) 的严格式不适用这一退化端点。
没有 L=0 的非零归一化时窗 Hilbert 源。

截断 Gaussian 不是 Cc∞，但不构成 domain 逃逸：I−B 有界，Cc∞(I_L) 在 H_L
稠密。因此用 strict-support smooth 源 g_j→g 的 L² 逼近，并分别按准确 norm
归一化，即得同一 infimum 与以上上界；任何 strict margin 均在足够大 j 后保留。
若需要实际 Q 的 Dlog 域，该截断源有限端点 jump 给 Fg(t)=O(1/|t|)，
故 ∫log(2+|t|)|Fg(t)|²dt<∞；本件仅消费有界 time-band 型，毋须用此附加事实。

## 4. 从非负修复的真实 supplier 提取 scalar：方向不能颠倒

假设某个 fixed L/Ω 上，对原合法全 complex smooth 源有型不等式

    a(I−B_(L,Ω)) ≥ τI+U，a≥0，U≥0。                  (4)

此处 U 可为任意 bounded 正算子；若是 compact，rank 和 norm 可任意随 L 增长。
两侧有界，(4) 由 smooth 密度延拓 H_L。每个 norm-one f 都给

    τ≤a<f,(I−B)f>−<f,Uf>≤a<f,(I−B)f>。

取 infimum 后得到严格必要式

    τ≤aδ(L,Ω)。                                      (5)

结合 (2)–(3)，若 a>0，则

    τ<4a/(e^(ΩL)−1)，τ<5a e^(−ΩL)。                 (6)

若 a=0，则 τ≤0，特别是不能供应正 scalar。U 的非负符号使可用 scalar 更小，
不能把 U 作为“额外供给”丢在左侧后抬高 τ。这里根本不需要 compact 性，
因此允许 rank 随 L 增长也不逃出该必要上限。
反之，若 U 有负部分，(5) 不由 (4) 自动推出；signed 修复属于尚需新来源的不同消费门。
上界是必要限制，不是存在 τ 或 U 的充分条件，也不给 δ 的下界。

## 5. 接 539：变 β/Ω/非负 U 的完整 conditional 费用

此节明确消费 539 的两个已审前件，且只限同一 constant exterior supplier：
此节的 U 及其余 band/pole 修复在每个 fixed L 上必须 compact，
以便合法消费 539 的 prime 必要门；第 4 节单独的 scalar 上限允许更一般的 bounded U≥0。

    C_L≤β+τ，                 （whole prime + compact bounded supplier ≥0 的必要条件）
    β+a≤Γ(Ω)，a≥0，           （Γ(t)−β≥a, |t|≥Ω 的逐点规则）
    a(I−B)≥τI+U，U≥0，τ≥0。   （本节抽取规则）

C_L 是 539 保所有 actual primepowers 的真实费用；Γ=actual2θ′，未换成 θ′。
结合 τ≤aδ，得到

    C_L≤β+aδ≤Γ(Ω)−a(1−δ)，
    a≤[Γ(Ω)−C_L]/(1−δ)，
    0≤τ≤[δ/(1−δ)] [Γ(Ω)−C_L]。                     (7)

若 Γ(Ω)<C_L，仍是 539 已排的失败。若 Γ(Ω)=C_L，必 a=τ=0；不能使用
下面带 strict 正右侧的写法。若 Γ(Ω)>C_L 且 q>log 5，则由 (2)

    0≤τ<4[Γ(Ω)−C_L]/(e^(ΩL)−5)，
    β>C_L−4[Γ(Ω)−C_L]/(e^(ΩL)−5)。                  (8)

β、a 均可任意按 L 调整，(7)–(8) 仍由同一个 full-source 必要门推出。
没有预设 β≥0，也没有把原固定 7/2 代回成长程序。

对任何声称全部无界成长 L 成功的此类程序，539 已付 C_L→∞，因而
Γ(Ω(L))≥C_L 迫使 Ω(L)→∞。在 eventually Ω≥256 上，539 同规范 Binet 上界

    Γ(Ω)≤log(Ω/(2π))+1/(15Ω)+25/(8Ω²)

直接给 Γ(Ω)=O(log Ω)。又 C_L≥0，而 L→∞ 时 eventually L≥1、q=ΩL≥Ω→∞。
故 (7)–(8) 的右侧趋零：例如 q≥log 10 时

    τ≤8 Γ(Ω)e^−q=O((1+log q)e^−q)→0。               (9)

因此此类来源在允许任意变 β(L)/Ω(L)、任意 L-dependent 非负 compact 修复后，
仍不能供应一个与成长 L 无关的严格正 scalar τ₀。若每窗采用 τ(L)>0 并让它迅速趋零，
上述必要条件不排除它；也没有证明这种逐窗机制实际可闭合全部 Schur/算术误差。

## 6. 准确影响、未付前件与不消费项

新增独立输入是显式 Gaussian 的全参数 norm/频尾必要预算，而不是独立算术正性。
539 的 Ω(L)→∞ 逃逸仍合法，但 constant-envelope 抽出的 nonnegative scalar 必须衰减；
这一点在调 β/Ω、增非负 compact rank 后依然成立，不应继续用更多矩阵掩盖该费用。

完整 Q_L 的 nonconstant Γ-tail 为

    T(f)=(2π)^−1∫_(|t|>Ω)[Γ(t)−β]|Ff(t)|²dt。

本件只约束从 constant 下界 a 所得的 a(I−B)。不可用 Gaussian 上界给实际 T 的上界，
更不可说实际 unbounded Γ-tail 因 compact 或弱收敛消失。若 Q≥R 而 R 的 scalar 不足，
也不推出 Q 负、RH 失败或任意 signed/几何方法失败。
growth whole Q 的联合 signed prime/pole/Γ 费用、全部误差与通常 Ξ/ζ 同对象识别仍未付。

本件支持 C011 第二轮止损/转向判断，但不是新 Goal 的完整完成证明。
更有信息价值的下一来源是保留完整 nonconstant Γ-tail 的 whole-source joint signed 估计，
或实际多prime/几何正输入；重新准入 constant supplier 需具体新的 signed 预算或完整尾机制，
不能只重命名 τ(L)、盲增 N/精度或再次引用固定窗证书。
