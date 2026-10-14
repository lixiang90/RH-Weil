# C021 G2：完整有符号 nondivisible carry 的独立准入逆审

2026-10-14；只编辑本稿，不编辑 STATE/cadence/Git，不独立消费研究轮。
已按 AGENTS 恢复 README/STATE、check/show、G20261014、frontier、C021、D20261014W、
550/changed-head 原矩阵和实际 Γ 接口。check 通过只认证结构。
入口现场 HEAD=8a4a53647e34f07ed962efa657057fa94d3991a9、工作树 clean；
子 get_goal=null，不代替 root 的同一 active 宏观 Goal。
固定基线仍为0c4f3a3/≤538，最新结算数学仍549。

**裁定：G2 open。** 单 q 与 full signed carry 非紧性并不反驳 actual Γ-relative 门。
下面准确核 compressed adjoint 的低 m/高 q 抑制、一个真正同源 full-sum 正配对的
完整 Γ 价，以及全部 q 的有限 cell-frequency 费用；均不提供全源 uniform-N G2。
没有证明或合法核心反例，不以粗 upper 宣称必要增长，不延长合同预算。
G1 的独立付款由另稿/root消费，不能据它闭合 G2/wholecount。

## 1. 实际对象、norm、全部源与严格算术范围

ALL整数 N≥4，L=(logN)/2、x=e^(u+L)∈(1,N)，du=dx/x。
写 r=a_Nφ、a_N=e^(u/2)=N^(-1/4)sqrt x，则

    ||r||²_(du)=N^(-1/2)||φ||²_(dx)。                         (1)

新 Π^a 为 span{a_Nχ_(j,j+1):j=1,…,N−1} 的原 norm 正交 head。
R_a detail 恰为每 unitcell ∫φ dx=0；不是547旧 weighted-mean R。
每格 φ_j(v)=Σ_(k≠0)f_(j,k)e^(2πikv)，所有 complex profiles 完全独立。
实际 zeroextension 域为 R_a∩Dlog，不限制共同 profile 或 Fourier 阶。

actual U_qφ(x)=sqrt q φ(qx) 是 contraction、保每 cell mean0，strict q<N。
P_q 在每格选 q|m 的 output Fourier 模式；D_q=P_qU_q、C_q=(I−P_q)U_q。
本审全程保

    B_C(r)=2N^(-1/2)Σ_(2≤q<N)Λ(q)/sqrt q Re〈C_qφ,φ〉。        (2)

Λ(q) 在全部 actual proper prime powers 取 log p；不换成仅 primes。
内积对第一变量线性，(2) 的各 q、正反方向及 signed cross 都来自同一个 φ。
detail pole=0 不支付 prime carry；Γ/prime/head mixed 仍有另一个责任。

来源矩阵和 occupation 原件见
[550 changed-head 原审](../physical-row-gy/next-full-detail-fourier-occupation-source-audit.md)。
欲付的是全部 N/全部 r 的

    B_C(r)≤δJΓ(r)+C_δ log²N ||r||²，固定0<δ<1。              (G2)

或另一个经过强旧净值核验的 polylog fee；当前不预付。

## 2. compressed adjoint：真实低 m/高 q 抑制

因为 C_q:R_a→R_a，其 detail adjoint 是

    C_q^*=R_flat U_q^*(I−P_q)，
    U_q^*φ(y)=q^(-1/2)φ(y/q)1_(q,N)(y)。                     (3)

不能漏掉 (3) 的 child flat-mean projection。
取单 parent cell j 的单位模式 e_(j,m)，m≠0。若 q|m，则 C_q^*e_(j,m)=0。
若 q∤m，child n=qj+s、0≤s<q、n≤N−1 上精确为

    q^(-1/2)e^(2πims/q)[e^(2πimv/q)−I(m/q)]，
    I(t)=∫_0^1e^(2πitv)dv。                                  (4)

所有实际 children 数 c_j(q)=max(0,min(q,N−qj))，故

    ||C_q^*e_(j,m)||²
       =(c_j(q)/q)[1−|I(m/q)|²]
       =(c_j(q)/q)[1−sinc²(πm/q)]
       ≤min(1,π²m²/(3q²))。                                (5)

最后一步由双积分恒等式
1−|I(t)|²=∫∫[1−cos(2πt(v−w))]dvdw≤π²t²/3 支付。
负 m 同样成立；截尾只删完整 child，不产生 fractional cell 误差。
因此 m 固定、q 大时有真实 O(|m|/q) norm 衰减。
把每个 adjoint 都估为 contraction 后求和，只是粗 upper，不能宣称必要 sqrtN 费。

(5) 也不能逐模式对全 profile 无声对角求和：不同 m 的 child restriction 并不总正交。
例如全部 q children 存在时，q∤m,n 的单-parent Gram 为

    〈C_q^*e_m,C_q^*e_n〉
       =δ_(m,n)−1_(m≡n mod q) I(m/q)overline(I(n/q))。         (6)

截尾则保有限 geometric phase sum；不同 q 的 child 支撑也会相交。
这些 alias/cell/q signed cross 正是全源 joint 费用，不能据 (5) 免费删除。

## 3. 完整算术和的有限 profile-band bound

下列只是有信息的方向测试，不把有限矩阵或 band 通过升级为 G2。
令 V_K 为所有 cell 模式 1≤|m|≤K 的完整 complex 子空间，K≥1整数。
对 φ∈V_K，f=(I−P_q)φ 仍在 V_K，||f'_cell||≤2πK||φ||。
每 child 用 unitcell mean projection 的 Poincaré inequality（cosine Parseval）及 (3)，

    ||C_q^*φ||≤min(1,2K/q)||φ||。                            (7)

具体缩放为 ||(U_q^*f)'_cell||²≤q^(-2)||f'_cell||²；
截尾只减少积分，ALL N 同一常数。故保 full signed sum 后

    |B_C(r)|≤2Σ_(q<N)Λ(q)/sqrt q·min(1,2K/q)||r||²。

用546已付自含 Chebyshev ψ(X)≤4(log2)X，对 R=2K 分部求和：

    Σ_(q≤R)Λ(q)/sqrt q≤8(log2)sqrt R，
    Σ_(q>R)Λ(q)/q^(3/2)≤12(log2)/sqrt R。

于是有一个安全统一常数

    |B_C(r)|≤48sqrt K ||r||²，ALL N≥4，φ∈V_K。                (8)

这保所有 q/properpowers、所有 cells 和同源 signed pair，并不假设 cross 为零。
例如 K≤log⁴N 时 (8) 的费已≤48log²N；这只是 band 范围，不是 all Dlog。
K 任意增长时 sqrtK 的 upper 未被 actual log-frequency Γ 吸收，
不能反向称 sqrtK 为 necessary，也不能用它关闭或否定 G2。

## 4. 真正同源 full-sum 非紧序列及其 actual Γ 价格

取 k≥1，φ_k 只支撑 parent cell1 与 child cell2：

    (φ_k)_1(v)=2^(-1/2)e^(2πi(2k+1)v)，
    (φ_k)_2(v)=i·2^(-1/2)e^(2πikv)，其余cell=0。              (9)

这是单位 dx norm、每格 mean0 的共同 complex 源，ALL N≥4 合法。
定义原 du 单位源 ρ_(N,k)=N^(1/4)a_Nφ_k=sqrtx φ_k；
它是 fixed-N 有限 BV、全线 zeroextension，属于 Dlog 甚至 Γ operator 域。

exact child→parent 系数在 q=2、m=2k+1 为

    2^(-1/2)∫_0^1e^(−πiv)dv=−i sqrt2/π。

所选 i phase 使 signed pair 为正。D_2 仅输出频率2k，与 parent2k+1 正交。
所有 q≥3 的 actual forward overlap 恰为0，因为 source 支撑 x<3；
reverse 方向是相同配对的共轭，不是被删掉。
因此这里是 full sum 的严格值

    B_C(ρ_(N,k))=log2/π，ALL N≥4，ALL k≥1。                  (10)

它与550的 full signed carry 非compact 事实相容，但还须支付同源 Γ。
按543/547实际规范，

    Φ(t)=Γ(t)−Γ(0)，Γ(t)=Reψ(1/4+it/2)−logπ=actual2θ′，
    JΓ(ρ)=(2π)^(-1)∫_R Φ(t)|hatρ(t)|²dt。

由已付 actual jump ν(a)=e^(−a/2)/(1−e^(−2a))、ν(a)=1/(2a)+O(1)，
Φ(t)=log(e+|t|)+O(1)，保原 factor2/2π。
ρ_(N,k) 在 u 中只是某个固定 x∈(1,3) 源的平移，所以 JΓ 精确不依 N。
每个 piece 的 phase derivative 为2πm x、m∈{k,2k+1}，均在 [c k,C k]。
非驻相分部积分给

    |hatρ(t)|≤C/k，|t|≤c k；
    |hatρ(t)|≤C/|t|，|t|≥C k。

piece endpoints/jumps 包含在这些界中，常数不依 N,k。
两段 Fourier norm 质量 O(1/k)，高频 log 尾 O(logk/k)；Parseval 保中间质量1−O(1/k)。
故完整实际 Γ 能量为

    JΓ(ρ_(N,k))=logk+O(1)，k→∞，uniform ALL N≥4。             (11)

所以对每个固定 δ>0，(10)−δ(11)→−∞。
**这一个实际 full-sum 非紧序列不是 G2 反例。**
free carrier/torus 构造若换 source，必须另付其真实 Γ(logτ)、细胞 mean 条件和全部 q 同源性；
不从539/单q的原norm失败继承 actual Γ-relative 失败。

## 5. 最小未付前件与准确停止范围

原 G1 另稿已证明 E_cell≤4JΓ+56logN||r||²，保 ALL N/ALL Dlog。
它只允许已付 D-occupation 取小 ε，并不支付 (2)。
本审 (5)/(7)/(10)/(11) 说明两种快捷反例均不成立：
low m/high q 的粗 star 费用忽略 child mean；fixed-N 高频非紧性忽略 Γ。
这是真实逃逸核查，不是 G2 已证或所有反例都失败。

剩余最小责任是：对任意 cell/frequency 叠加与 q 成长，控制完整 signed (2) 相对
同一源的 full zeroextension Φ(t) 能量，使减去一个严格 δ<1 的 Γ 后，剩余 norm fee
仅为 uniform polylogN；或给一个准确合法族使这一 fee 必须超所有拟用 polylog。
需要同时核 (6) 的 alias、不同 q 的 common-child overlap、child/cell 位置与实际 Γ。
不允许把逐 q worstnorm、独立 source 的 Γ 和另一个 source 的 arithmetic 最大值相加为必要费。
也不把这个剩余目标命名为新的独立输入/合同。

当前没有这样的 full multi-q bound 或合法核心反例；G2 保持 open。
G1-only/有限 band/表示与非紧性核查按 C021 既有规则入口0停止，
不延长预算、不登记 quasipolynomial wholecount 已证、不形成 Goal 方法类完成声明。
single-q free/finite-rank 删除仅是已排范围；Γ-relative、允许 source适应/联合 signed 费用未排。
原宏观 signed/core/Ξ 瓶颈仍在；新准入动作由 root 从当前战略统一选择，不在本稿另启候选。

本子任务无待跑进程。只保存上述范围与停止理由；root 负责 STATE、唯一 cadence 与授权推送。
