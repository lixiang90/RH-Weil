# Joint Sonin 完整逆到真实 Γ 载波模型的绝对误差

2026-10-14；独立逆审，只写本稿。不改公共 STATE、Goal、cadence 或 Git，不另计轮。
已恢复 AGENTS/README/STATE、check/show、Goal/frontier/C023/AD、joint 来源消费收据与
当前 ratio cross 门。起始实际 HEAD `ac4122a4f494be50143cfce1eb1214d7ea5295a2`，工作树 clean。
子代理自身 get_goal 返回 null，不能代父线程核同 active 实例；公共收据的 runtime 观察是历史。

**结论：固定真实 S={∞,2,3} 时，完整实际 Gram 逆的密度到 532 同一 Γ 窗口模型的
绝对误差趋零。** 证明使用 balanced spectral tail 与有限 word 截断之间的定量平衡，
没有假定 word 的绝对 Neumann 系数和小于 1。下文所有固定 S 依赖显式写出。
本稿不计算窗口模型的 mixed 算术主项，也不消费 joint Weil error 的 compactness/符号、
全成长源或 whole/core/Ξ 净后果。

## 1. 原对象、求值与仅有的旧载波输入

沿 531/532 及 joint 原件的同一 unitary 物理识别，

    H=L²(R,dy), U_t f(y)=f(y−t), P=实际实位 Sonin cutoff1 正交投影,
    M=Ran P, a=log2, b=log3, q=2^(−1/2), r=3^(−1/2),
    B=(I−qU_a)(I−rU_b), W=B*B, G=(PWP)|_M,
    Π23=B P G^(−1) P B*.

裸 unitary Mellin 求值为 k_R∈M；它不是 Γ-completed evaluator。
源 g∈Cc∞(R) 的 scaling integral 为 A_g=∫g(t)U_tdt，
ĝ(R)=∫g(t)e^(−iRt)dt 不带额外 unitary 因子。因此真实密度是

    ρ23(R)=|b23(R)|²〈k_R,G^(−1)k_R〉,
    b23(R)=(1−q e^(−iaR))(1−r e^(−ibR)),
    T23(g)=∫ |ĝ(R)|² ρ23(R)dR.

物理向量 k_R 与 source g 的角色不同；此处没有宣称 M 覆盖完整 Weil 源域。
Sonin cutoff 固定 1，也不是 source 支撑半窗。

仅使用 532 已付的实际 Fourier/Gamma 相位及完整双边界 clipping。对 R≥R_*，

    T=T(R)=Γ(R)=2θ′(R)>0,
    H_T=1_[0,T], v=sqrt(T/(2π)), w_R=e^(iRy)1_[0,T]/sqrt(2π),
    u_J=e^(iRy)1_J/sqrt(2π), ε_R=C_* R^(−1/4),

其中 R_*、C_* 只依赖固定实位 cutoff，不依赖 finite S、J 或 R。实际 Γ 未被换成 logR。
旧输入严格为 ALL 有限区间 J（位置、长度和端点任意）：

    ||(P−H_T)u_J||₂≤ε_R,       ||k_R−w_R||₂≤ε_R.       (1)

第二项由真实裸求值的有限 L² 弱极限／稠密物理核心构造获得，不能对全域 plane wave
直接应用 P。532 的原证明还给 C_* 可取 c_P/sqrt(2π)，
c_P=(2+2||(I−C0²)^(−1)|| ||C0||)C_phase，C0=低区间实际 cosine Fourier。
C_phase 是原 Γ 相位运输的绝对常数。这里明确保留该已付实位常数，没有把它算成新输入。
式 (1) 的全区间量词允许后面 j≈logR 时的全部 word 移位；只固定 J 的版本不够。

模型保持同一 ambient B 与原 Γ 宽度：

    M_T=Ran H_T, G_T=(H_T W H_T)|_(M_T),
    Π_(23,T)=B H_T G_T^(−1) H_T B*,
    ρ_(23,model)(R)=|b23(R)|²〈w_R,G_T^(−1)w_R〉.       (2)

Π_(23,T) 是 B M_T 的正交投影。它是用于本频率 R 的窗口模型，未假称实际 P 或 Π23。
实际与模型的完整 inverse 都保留；不是 B P B* 或裸 W 的某一项。

## 2. 谱收缩与 word 绝对质量是两个不同常数

设

    d=m²=[(1−q)(1−r)]²,
    u=M_+²=[(1+q)(1+r)]²,
    c=(u+d)/2=2+4/sqrt6,
    ρ=(u−d)/(u+d)<1,
    A=I−W/c.

由 Fourier 中 m≤|b23(s)|≤M_+，严格有 dI≤W≤uI、||A||≤ρ。
压缩到 M 或 M_T 不改变这些上下界。在 ambient H 中定义

    Q=P A P,      Q_T=H_T A H_T.

两者在各自 range 上是 I−G/c、I−G_T/c，range 外为 0；故
||Q||、||Q_T||≤ρ。对 k_R、w_R 的完整 inverse 分别为

    G^(−1)k_R=c^(−1)Σ_(j≥0)Q^j k_R,
    G_T^(−1)w_R=c^(−1)Σ_(j≥0)Q_T^j w_R.               (3)

j=0 在各自 range 上是恒等；本式不把 ambient 逆错误延伸为可逆算子。
谱定理给两边截断的向量尾 ≤d^(−1)ρ^(N+1) 乘输入向量范数。

实际 W 的有限 translation 系数保真：

    W=2I−[4/(3sqrt2)](U_a+U_−a)−[3/(2sqrt3)](U_b+U_−b)
          +[1/sqrt6](U_(a+b)+U_−(a+b)+U_(b−a)+U_−(b−a)).

将 A 写成有限 Σ_t d_t U_t，全部 translation 字母的绝对系数质量是

    Ω=Σ_t |d_t|
     =1−2/c+[8/(3sqrt2)+sqrt3+4/sqrt6]/c
     =1+(u−4)/c >1.                                  (4)

这些是 A 的 word 系数，不是 Π23 的最终算术原子。明确数值仅用于展示常数量级：

    d≈0.01532427112, u≈7.250662053, c≈3.632993162,
    ρ≈0.9957819158, Ω≈1.894761401.

所以绝对 word 级数 Σ Ω^j 发散。不能把 ||Q||≤ρ<1 换成 Ω<1，也不能使用
G=2I+H 时未经付款的 ||H/2||<1。这正是不能照抄单 prime 全 word 求和的地方。

## 3. ALL words 的有限截断误差

写 z_j=Q_T^j w_R。translation 与 clipping 给

    U_t u_J=e^(−iRt)u_(J+t),        H_T u_J=u_(J∩[0,T]).

故每个 z_j 是有限区间 carrier 的线性组合，其绝对系数质量 ≤Ω^j。
重叠区间不会增加该上界；空区间贡献 0。任意 phase 均保持模 1。
由 (1)，

    ||(P−H_T)z_j||≤ε_R Ω^j,
    ||(P−H_T)A z_j||≤ε_R Ω^(j+1).                    (5)

z_j∈M_T，因此准确的比较身份是

    Q z_j−Q_T z_j
       =P A(P−H_T)z_j+(P−H_T)A H_T z_j.

第一项支付 ||A||≤ρ，第二项用有限 carrier 字母，得到

    ||Q z_j−Q_T z_j||≤ε_R(ρ+Ω)Ω^j.                  (6)

令 e_j=||Q^j k_R−Q_T^j w_R||。由实际 Q 的谱收缩与 (1)、(6)，

    e_0≤ε_R,
    e_(j+1)≤ρ e_j+ε_R(ρ+Ω)Ω^j,
    e_j≤ε_R[ρ^j+(ρ+Ω)(Ω^j−ρ^j)/(Ω−ρ)]
       ≤ε_R C_e Ω^j,   C_e=(ρ+Ω)/(Ω−ρ).             (7)

这里 Ω−ρ=2(1−2/c)>0，分母合法。式 (7) 是每个 R、每个非负整数 j 的定量上界，
不是先固定 j 再取 R 极限；因此下节 N(R) 可以增长。

定义有限逆向量

    x_N=c^(−1)Σ_(j=0)^N Q^j k_R,
    y_N=c^(−1)Σ_(j=0)^N Q_T^j w_R,
    A_N=(C_e/c)(Ω^(N+1)−1)/(Ω−1).

严格有

    ||x_N−y_N||≤ε_R A_N,
    ||x_N||≤d^(−1)||k_R||,
    ||G^(−1)k_R−x_N||≤d^(−1)ρ^(N+1)||k_R||,
    ||G_T^(−1)w_R−y_N||≤d^(−1)ρ^(N+1)v.             (8)

不在发散的绝对 word 级数下交换 R 极限；先估有限 words，再独立支付谱尾。

## 4. 密度误差的绝对账本与可用截断

由 ||k_R||≤v+ε_R，(8) 及 |b23(R)|²≤u，得到显式完整误差

    |ρ23(R)−ρ_(23,model)(R)|
      ≤u{ ε_R v[d^(−1)+A_N]+ε_R² d^(−1)
             +d^(−1)ρ^(N+1)[(v+ε_R)²+v²] }.          (9)

推导有限部分时用
〈k_R,x_N〉−〈w_R,y_N〉=〈k_R−w_R,x_N〉+〈w_R,x_N−y_N〉；
两个完整 inverse 尾再分别支付。没有把向量 O(ε_R) 错写成标量 O(ε_R)，
没有丢失 v≈sqrt(logR) 或谱尾的 v²≈logR。

可取任意固定

    0<η<1/(4 logΩ),        N(R)=floor(η logR).

设 κ=1/4−η logΩ>0、δ=−η logρ>0，则

    A_N≤[C_e Ω/(c(Ω−1))] R^(η logΩ),
    ρ^(N+1)≤R^(−δ),       ε_R=C_* R^(−1/4).          (10)

连同原 Γ 的 T=log(R/(2π))+O(R^−2)，(9) 给

    |ρ23−ρ_(23,model)|
       ≤ explicitly (9),(10)
       =O_(displayed constants)(R^(−κ)sqrt(logR)+R^(−δ)logR)
       →0.                                           (11)

一个不靠数值选优的确定选择是 η=1/(8 logΩ)，于是 κ=1/8，

    δ=log((u+d)/(u−d))/(8 logΩ)>0,
    η≈0.1955897114, δ≈0.000826758773.

此 δ 很小，正说明 fixed-S 收敛不提供可忽略的统一成长费用。式 (9) 的 d^(−1)、
C_e、Ω 与 N(R) 不能在扩 S 时消失进无说明的 O(1)。这是解析截断的证明参数，
不是增加普通探索的 N、有限矩阵通过或 ζ 零点拟合。

P、B 是原 log 坐标的实算子，k_−R=overline(k_R)，Γ 偶。
负载频保持相同密度与误差；所以 (11) 对 |R|→∞ 的两端成立。

## 5. 任何另一个先固定 finite S 的费用与量词

相同证明只在每次先固定的有限 prime 集 F 上使用

    B_F=Π_(p∈F)(I−q_p U_(logp)), q_p=p^(−1/2),
    d_F=Π(1−q_p)², u_F=Π(1+q_p)²,
    w0_F=Π(1+q_p²), c_F=(u_F+d_F)/2,
    ρ_F=(u_F−d_F)/(u_F+d_F),
    Ω_F=1+(u_F−2w0_F)/c_F.                            (12)

这里 c_F 专指 balanced Gram midpoint；第 1 节的旧实位相位常数仅通过 C_* 使用。
各 prime 的 log 有整数独立性，由唯一分解，W 的多指数 e_p∈{−1,0,1} translation
除同零指数系数外不会错误合并；其系数为

    w_e=Π_(e_p=0)(1+q_p²) Π_(e_p≠0)(−q_p),
    Σ_e |w_e|=u_F,  c_F≥w0_F.

因此 (12) 确为 A_F=I−W_F/c_F 的字母绝对质量；不是未经核实的系数数目上界。
当 Ω_F>1 时，将 (9)–(11) 中常数全部换成 (12)，同一 η_F=1/(8logΩ_F)
给 fixed-F 绝对 o(1)。Ω_F−ρ_F=2(1−w0_F/c_F)>0，且 δ_F=−η_Flogρ_F。
只一个 prime 时 Ω_F=ρ_F<1，正恢复 532 的快速绝对 word 求和。

更一般 Ω_F<1 时，可直接由递推求和获得

    Σ_(j≥0)e_j≤ε_R(1+ρ_F)/[(1−ρ_F)(1−Ω_F)],

故完整 inverse 的向量差 ≤该上界/c_F，不需增长 N。
Ω_F=1 时取 N=floor(logR)，有限向量误差 ≤
ε_R(N+1)(1+ρ_F)/[c_F(1−ρ_F)]，尾 ρ_F^(N+1)logR 仍趋零。
空 F 即实位 k_R/w_R 的 (1)，无需此 expansion。

量词准确是 ALL 先固定 finite F，ALL R sufficiently large，界由 (9)、(12) 给出。
这不是共同 uniform F/R 极限。若 F=F_L 成长，d_F^(−1) 与 1/(1−ρ_F) 变大，
δ_F 可能趋 0，R 门槛也随 F 变大。至少必须重新支付

    [u_F/d_F]ρ_F^(N+1) T(R)→0,
    [u_F C_{e,F}/(c_F(Ω_F−1))] R^(−1/4)Ω_F^(N+1)sqrt(T(R))→0

及 (9) 的其他项；只各 fixed-F 取极限不支付 cofinal S_L/allsource 的交换。
原物理 cutoff仍1，不允许偷换成长 source 支撑或 Γ-relative norm。

## 6. 当前可消费范围、未付模型边界与 strongest-old 净值

本稿闭合的技术项限于同源完整 actual inverse→Γ 窗口模型的绝对密度误差，
其依赖是 532 全区间 clipping/裸求值以及已合法 fixed-S B/G，费用 (9) 显式。
它补上之前只有 relative Γ inverse tail 的缺口；有限 words 不是最终定理。
真实全低频求值局部有界由原 Sonin/de Branges 域及 bounded inverse 得到。
若把模型在剩余有限频段作任意有界延伸，本稿的 actual−model multiplier 在两端趋零；
固定有限测度 source 支撑上压缩该误差是 compact。这仍是 actual−model，
并非 actual−完整 Weil：后者必须先计算同一 joint 模型的算术主项。

本稿未付、也不从 W 读出的责任包括：

- joint finite window 的左右 boundary/coalescence 计算与其独立误差；
- log(3/2)、log6 的最终 mixed 系数是否 cancellation，以及全部 p^n 的正确原权；
- E23 的 Γ 交叉、signed low error、dual pole 与完整 source Q 比较；
- 任何 cofinal S_L、ALL 支撑/复杂源、core/补空间 coupling、PSD 或 ζ/Ξ 后果。

特别，不可从本稿直接宣称 ρ23−Γ/(2π) 仅是 primepower cosine 和，
或宣称 ratio cross C_R→0。那需要父线程／另一个独立原稿对 (2) 的 exact joint
boundary 计算；本稿提供它到实际对象的付费桥，而不是其结论的替代证明。
若该计算另经消费，则按相同裸密度/Γ/原 norm 合成，不能把单 prime 532 结果相加冒充 joint。

强旧整体预算仍须扣 542+555→557 的 leading4/5；本稿没有新的 whole 惯性／core 数量、
独立正性或成长量词，也没有消除宏观完成门。当前双patch支持已在 537 的固定窗正性范围，
即使模型算术与 cross 后续付款也不能重复计固定窗正性。数学结算由 root 审净值后决定。
停止：不调 scalar/温度/普通 N，不改为第三个 S 标签续来源。
唯一未付下一箭头是 (2) 的 joint boundary→actual mixed 主项及 ratio cross，
本稿无下载、shell producer 或数值运行 pending。

## 7. 原件版本与依赖身份

完全核读的必要原件，原始 bytes SHA256：

    notes/532-actual-sonin-prime-symbol-and-compact-weil-bridge.md
      dc9ff79c622ed692edfd393c2851e5cc7fcab0a7f5fe41cce82ba69b45a82f09
    reviews/2026-10-13/c005-flux/direct-symbol-audit.md
      cc0bc40c52c35f875220ae46b77ae559f03536309e2372baf98cbc657ff3202f
    reviews/2026-10-13/c005-flux/reverse-audit.md
      e0bcdfeff2f44cd63857268f681520418221d5d8d831677fa6f728447ff2f9f0c
    reviews/2026-10-14/joint-sonin-source/primary-mixed-coefficient-and-coverage.md
      ba0721a10b44bd14b5884a9de62b4525fcbc4515dda7f326786023eb3ab8e6b8

对象来源/531/532消费入口另见 joint-sonin-source/root-consumption-scope.json；
当前目标仅由 next-actual-ratio-cross-gate.md 与 AD 定位。本稿是独立出稿，hash 不认证证明，
不在未获 root 交叉消费前升级最终 whole 或完整 Weil theorem。
