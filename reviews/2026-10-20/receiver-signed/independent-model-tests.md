# 571 独立模型门：真实 receiver、双边界 Schur 耦合与单 prime 精确反测

2026-10-20；独占审查原稿，不改 STATE/cadence/Git，不代 root 消费。
已读 README/STATE、运行 research_state check/show，并恢复同 G20261014、0c4f≤538、
570 结算和 560 §3 两份原模型。strong-old 为 542+555→557 leading4/5。
本稿的对象是 **有限窗模型残差**，不是 570 的 actual Sonin error E，也不是原 Weil 源。

## 1. 准入的具体 input / test / net

已有输入为 560 的 exact D、两个半线 inverse 和完整 G_T inverse。
新的可判测试：在真实 carrier w_(R,T)，严格锁定 T=Γ(R)，计算双边界残差

    δ_(F,T)(R)=<w_(R,T),(G_T^(-1)−S_T)w_(R,T)>。

单 prime 的 delay fibres 可给完整 inverse 的闭式，故可独立核查符号、实际 receiver 像和原 norm。
结果是：固定单 prime 时 δ 在实际 Γ 载波的趋∞序列上两号，大小为 R^(−1/2)；
真实 receiver 的跨窗输出也为 R^(−1/2) 阶，绝非任意负半线向量的费用。
这为“无条件同号双边界修正”提供具体反测，但不支付 joint {2,3} 或 cofinal F_L、
不付 Sonin clipping 的成长费，不产生完整 Q_W 的正/负结论。
是否晋级数学合同由 root 按其他稿的 joint/growth 结果判断，不能以此自动结算新轮。

## 2. 一般有限 F：完整 Schur 表示保两边界及全部 returns

用互相正交的 P=1_(0,T)、L=1_(-∞,0)、H=1_(T,∞)，W=B*B，Z=W^(-1)=DD*。
Z 的各对角压缩有严格正下界，故以下 inverse 均为原 Hilbert norm 的有界完整 inverse。
设

    A=Z_PL Z_LL^(-1/2), B_r=Z_PH Z_HH^(-1/2),
    C=Z_LL^(-1/2) Z_LH Z_HH^(-1/2),
    M_C=[[I,C],[C*,I]]。

由 bounded Schur complement 精确得到

    G_T^(-1)=Z_PP−[A B_r] M_C^(-1) [A*;B_r*]，
    S_T=Z_PP−AA*−B_r B_r*，
    Δ_T=G_T^(-1)−S_T=[A B_r](I−M_C^(-1))[A*;B_r*]。       (2.1)

第二式来自 560 已付的半线因果 inverse，因而 AA*=P D L D*P、
B_r B_r*=P D* H D P；它不是另造的单边界模型。
若 m=∏(1−p^(−1/2))、M_+=∏(1+p^(−1/2))，则

    M_C ≥ (m/M_+)² I，且 ||C||≤1−(m/M_+)²<1。             (2.2)

证明：(m/M_+)² 是 Z_(L⊕H)≥M_+^(−2)I 与
Z_LL,Z_HH≤m^(−2)I 经 block congruence 的直接下界；
M_C 的谱对称地落在 1±singular(C)，遂得 norm bound。
它是 fixed-F gap，不是成长一致 gap。
展开 block inverse只是代数身份，保留完整 (I−CC*)^(-1) 与 (I−C*C)^(-1)：

    Δ_T = −A CC*(I−CC*)^(-1) A*
          −B_r C*C(I−C*C)^(-1) B_r*
          +A C(I−C*C)^(-1) B_r*
          +B_r C*(I−CC*)^(-1) A*。                    (2.3)

两个 diagonal returns 非正，但 cross 没有固定号；删其中任何一项都会改变 signed 比较。
对真实 w 只允许 α=A*w、β=B_r*w，其原 norm 严格为

    ||α||²=||L D*P w||²，qquad ||β||²=||H D P w||²。     (2.4)

不能以任意 α,β 或任意负半线 bump 代替这个受限像。
式 (2.1) 本身只是 exact representation；若直接假设该 quadratic form 有利，
尚未得到独立 capacity，不把表示当新正性。

## 3. 单 prime 的真正 fibres 和 exact full inverse

固定 p，a=log p、q=p^(−1/2)，B=I−qU_a。
写 y=x+ka，x∈[0,a)，k∈Z。原 L²(dy) 酉分解为
∫_[0,a)^⊕ ℓ²(Z) dx；无变 norm。
若 T=Na+τ，N=floor(T/a)、0≤τ<a，则 x<τ 的 window 有 N+1 点，x≥τ 有 N 点。
以下 n 指某一 fibre 的实际点数，i,j=0,...,n−1。

    (G_n)_(ij)=(1+q²)δ_ij−q δ_(|i−j|,1)，
    (S_n)_(ij)=[q^|i−j|−q^(i+j+2)−q^(2n−i−j)]/(1−q²)，
    (G_n^(-1))_(ij)=
      [q^|i−j|−q^(i+j+2)−q^(2n−i−j)+q^(2n+2−|i−j|)]
      /[(1−q²)(1−q^(2n+2))]。                         (3.1)

这些式直接乘 tridiagonal G_n 可验证，包括两个端点；无截断 inverse/returns。
置 u_i=q^(i+1)、v_i=q^(n−i)、c=q^(n+1)，则

    Δ_n=G_n^(-1)−S_n
       =[c(uv*+vu*)−c²(uu*+vv*)]/[(1−q²)(1−c²)]。       (3.2)

n≥2 时 u,v 线性独立，中间 2×2 矩阵 [[−c,1],[1,−c]] 两号，
故 Δ_n 恰有一个正和一个负 eigenvalue，其余为0。
所以 S_T 并无统一 Loewner 侧；但这一算子不定性还须下一节认证 actual carrier。

## 4. 真实 receiver 的原 norm：不是任意负半线测试

θ=aR、ζ=q exp(iθ)、C_n(θ)=(1−ζ^n)/(1−ζ)，
w_(R,T)(x+ka)=exp(iRx)exp(ikθ)/√(2π)，0≤k<n。
在负 fibre k=−ℓ，ℓ≥1，**actual receiver** 精确为

    (L D*P w)_(-ℓ)=exp(iRx) q^ℓ C_n(θ)/√(2π)。         (4.1)

这是沿负半线的同一 geometric tail，不是自由 bump；由 D* 的完整几何级数逐项求和。
原 fibre norm 与跨到右边界的 norm 精确为

    ||L D*P w||_fibre²=q²|C_n|²/[2π(1−q²)]，
    ||H D L D*P w||_fibre²=q^(2n+4)|C_n|²/[2π(1−q²)³]，
    ||H D L D*P w||_fibre / ||L D*P w||_fibre
       =q^(n+1)/(1−q²)。                              (4.2)

跨窗输出在 k≥n 为 exp(iRx) C_n q^(k+2)/[√(2π)(1−q²)]，直接付第二式。
若 C_n=0 则两个输出同零；对 q<1 实际 C_n 从不为0。
整个原 L² norm 按长度 (a−τ) 的 n=N fibres 与长度 τ 的 n=N+1 fibres 相加。
乘上 |b_p(R)|²=|1−ζ|² 后，receiver norm² 为

    q²/[2π(1−q²)] { (a−τ)|1−ζ^N|²+τ|1−ζ^(N+1)|² }。 (4.3)

右跨窗 norm²同样按 (4.2) 两块加，不发生任意 phase 配准。
特别固定 p，T→∞ 时加权 receiver norm²→a q²/[2π(1−q²)]，
而 ||w||²=T/(2π)。其相对 carrier norm²为 O(1/T)，跨窗 receiver 输出相对自身 O(exp(−T/2))。
这些是这一个 actual receiver 的原 norm；不声称是全部 Weil source 或成长 F_L 的必要费用。

## 5. Carrier signed 闭式和严格锁定 T=Γ(R) 的两号序列

令 z_θ=(1,exp(iθ),...,exp(i(n−1)θ))，
A_n(θ)=∑_(i=0)^(n−1)q^(i+1)exp(iiθ)=q C_n(θ)。
因 v*z_θ=exp(i(n−1)θ)overline(A_n)，由 (3.2)

    d_n(θ)=z_θ* Δ_n z_θ
      =2c { Re[exp(i(n−1)θ)overline(A_n)²]−c|A_n|² }
          /[(1−q²)(1−c²)]。                           (5.1)

完整实际 Γ-window 模型误差精确为

    δ_p(R)=[(a−τ)d_N(aR)+τ d_(N+1)(aR)]/(2π)，
    T=Γ(R)=Re ψ(1/4+iR/2)−logπ=Na+τ。                 (5.2)

没有先任意选择 T，再把 R 配准。
写

    Φ_N(R)=(N−1)aR+2 arg(1−q exp(iaR))。

arg 取连续周期分支（圆盘中心1半径q不含0）；其导数绝对值≤a q/(1−q)。
由 A_n=q/(1−ζ)+O_p(q^(n+1))，uniform in θ，得

    |b_p(R)|² d_N(aR)
      =2q^(N+3) cos Φ_N(R)/(1−q²)+O_p(q^(2N+2))。      (5.3)

标准完整 Γ 的 asymptotics 为 Γ(R)=log(R/(2π))+O(R^(−2))、
Γ'(R)=1/R+O(R^(−3))。故在大 R 上单调。
对每个充分大的整数 N，唯一取 R_N^0 满足 Γ(R_N^0)=Na，
于是 R_N^0=2π exp(Na)(1+O_p(exp(−2Na)))。
在区间

    J_N=[R_N^0, R_N^0+8π/(Na)]

内，Φ_N'=(N−1)a+O_p(1)，对充分大 N 有 Φ_N'≥Na/2，
故相位总变≥4π。可分别选 R_N^+,R_N^-∈J_N，
cos Φ_N(R_N^+)=1、cos Φ_N(R_N^-)=−1。
这时 **仍严格以原完整 Γ 定义 T_N^±**，且

    τ_N^±=Γ(R_N^±)−Na=O_p(1/(N R_N^0))=O_p(q^(2N)/N)，
    floor(T_N^±/a)=N。

由 (5.1) 有 |d_n|≤C_p q^n，故长度扰动带来的 (5.2) 误差
O_p(τ_N q^N)=O_p(q^(3N)/N)，严格小于 (5.3) 主项。
因而保 full inverse 和两个真实边界的实际 carrier signed 结论为

    |b_p(R_N^±)|² δ_p(R_N^±)
      =± a q^(N+3)/[π(1−q²)] + O_p(q^(2N+2))，          (5.4)

特别两号均在 R→∞ 出现，signed magnitude 为 Θ_p(R^(−1/2))。
除以原 ||w||²=T/(2π) 后为 Θ_p(R^(−1/2)/logR)。
Γ 从未被 log 近似替换定义；asymptotics 只付相位选择导致的窗口扰动。

## 6. 增量、scope 和未付容量

560(5) 已有 fixed-F 模型密度与完整 primepower 主项的 O_F((1+T)e^(−γT))，
570 已有 fixed joint actual E 的两号源及原 norm费用；二者均扣除。
本稿新增的确切信息是另一对象 Δ_T 在 actual w_R、T=Γ(R) 上的两号、
完整 rank2/Schur returns，以及 authentic receiver 原 norm，不把全空间 lower 偷换进来。
单 prime (5.4) 不是 joint {2,3} 的符号定理，且模型差并非 actual Sonin E。
fixed-p 误差变小阶不越过其 Sonin/carrier 运输误差，不宣称经典 ζ 新 density 符号。

保持 Γ、全部 primepowers 与双pole：本稿不改完整 Q_W 的定义，
只检查 560 exact parametrix 的内部残差，故尚无可输入 Q_W 的负例或正容量。
S_T 的统一 Loewner 号被精确反测；付非有限秩、source-adapted、Γ-relative 修复仍合法。
从 (2.1) 假设 actual (α,β) 上的有利号只是未付比较；若进一步假设足够强到逼 full Q≥0，
仍为 Weil 正性承担原责任，不能称独立 RR 容量。

cofinal F_L 时须另付 C 的成长gap、actual α/β协同、T=Γ(R) 与 F_L的同尺度、
原 Sonin k_R→w_R clipping/fullinverse误差及全源积分/危险core。
本固定单prime门不能把 560 的 ambient m||H D L||≈1 下界恢复为这些输入的必要费。
无全对象净预算，strong-old leading4/5、core/coupling/Ξ及宏观完成门均保持原状。

## 7. 可复核性与运行范围

(3.1) 用 tridiagonal 乘法即可精确复核；(3.2) 由
c(u_iv_j+v_iu_j)=q^(2n+2−|i−j|)+q^(2n+2+|i−j|) 逐项核查。
(4.1)–(4.3) 是原物理直接求和，(5.4) 是解析序列而非数值拟合。
草拟时曾运行小 R 的 mpmath 探索；它不作任何命题前件，也不将样本消费为证明。
本报告不依赖数值输出，不另存数值作证书。
