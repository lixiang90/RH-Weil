# Th6.5 actual covariance：独立 fresh 证明审计

2026-10-29；同 G20261027/runtime createdAt 1793085111，冻结基线 0c4f3a3eb609bb1d9564138fa4a35701f05605f2。本稿由独立 fresh 分工完成，终态仅供 root 消费；不修改 STATE、唯一 cadence、Goal、原论文或 Git，不领取新合同/编号，不启动后继。

**结论：限定 PASS。** 两份已冻结原稿已实际全文读取并重算 SHA；shrinking localization、真实未加权 Toeplitz 投影的统一交换子、严格 HS/S1 迹域、完整 G 逆及 560 的原物理范数运输能够合并闭合。原文 bare Tr(uS)、Tr(WS) 必须按下文 positive compression/HS 定义重证；不保留字面 bare-product S1 主张。实际 K 增量由旧 560 直接重导，不依赖论文未展开的 q 符号。没有发现本范围内必须支付的新实质依赖。

新可消费后果是原 du 范数上、随 p 移动的双脉冲测试的有符号前驱增量，以及同链有限极化所得的 shrinking-threshold 正特征值计数。它强于旧 585/587/589/591 已付内容，但方向是 Q=t-K+pole 中的不利 K 增量。长期 Goal 的关键瓶颈没有消除，不能报完整 Q 负例、算术正性或 whole 预算改进。若 root 合并消费，建议统一结算一个数学迭代；来源核查、两 proof、fresh、极化和 min–max 均不另计。

## 1. 恢复、实际读稿与版本绑定

本分工实际恢复 goals/README.md、STATE、同一 active Goal、D20261029X、macro summary/必要 frontier 与唯一 4739-byte proof gate；实际执行 research_state.py check 后 show，检查工作树/实际输出。执行位置是当前 Th6.5 proof，不是重启已停止的 C058。唯一 cadence 在恢复及本次指纹时为 6681 bytes/SHA 73ef5152185e3213a7b076a76a656c0a5a0acf9ace994c612def2de270584f4b；本分工未写它。

先独立读固定 v2 的 statement 959–989、proof 991–1100，再核必要的约定 21–57、6.1 525–563、已付 6.3 的 667–782。旧 C052 localization 审稿与 root closure、560/585/587/589/591 已实际读作消费前件/最强旧比较。1102–1119 曾在上下文中曝光，但其备注不作证明前件，也不消费其指数优化；没有阅读/消费 6.4 sharp 或 §7，未开新 source、查询、数值或参数搜索。

两独占原稿是在各自作者报告冻结后，实际全文读取当前文件并现场重 hash；不是以作者消息、文件存在或已终态标签代稿。下表为实际消费版本，均为 UTF-8/LF 原始字节。

| 输入 | bytes | SHA256 |
|---|---:|---|
| 固定 bramble_trace v2 原件 | 61862 | `541098314b2ddc5f8645babf82086e87d16c46188268cbc7ed6cfc1f98720058` |
| 唯一 proof gate | 4739 | `ede94f14a3430afbd100d907ca3649929aaef1138cd065dc896513311b616f33` |
| localization-and-rate-proof.md | 14467 | `3a5c61a0aacdd6aa7815387e666939d086d0f4da01d939d9df7b52b5d1a2bf36` |
| toeplitz-trace-and-transport.md | 24003 | `3946f4d843f86e7d2991b39db8ba4acf31ab1d9bb666c0a57b2e4eabddd6a977` |
| 560 原范数 finite-F 桥 | 9263 | `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3` |
| 585 fixed-source lower | 7857 | `5dca916d978eef599587ff4c6ce34144f814ddec0567a4c1b2314dcd71cd01af` |
| 587 moment/common-rank 下界 | 8681 | `e4d30cfb6d07299386014cb4c4e3e3979ab5111264355dfb37b24629f121ac82` |
| 589 zero-mean/rank-one 极限 | 7185 | `c491012226713baf0eecff045338563d4e440c6a1bde9eea0d9ccf661b958bc5` |
| 591 三 fixed-test occupation 障碍 | 5974 | `5a6d6e221369a1a9bce668d56c9fe574aeca0a295fdb7d0ccd31e4fcd03eaa7c` |
| C052 root-consumption-scope.json | 9076 | `75612a326db9c1144e43fd56fa5922d408425e891a25b2f7930812b3b068c54e` |
| C052 source-localization-proof-audit.md | 11459 | `809bc7ffc6f1fbf4dd24af0d710af05fb7ca1bc259992430c3fd6760912ffcb1` |

固定原件位于 literature/local/2026-10-28-core-source-location/bramble-trace-rstation-2-v2.md。本文不把作者、平台或可读版本当数学认证，也不主张本仓世界优先权。

## 2. 原对象、范数和量词

实际物理空间是 H=L2(R,dy)，U_a v(y)=v(y-a)，P 是 gap-one arch Sonin 正交投影，M=Ran P。对每个有限素数集 F，

    B_F=product_(q in F)(I-q^(-1/2)U_logq),
    Pi_F=B_F P (P B_F*B_F P|M)^(-1) P B_F*.

Pi_F 是原物理正交投影；B_F 仅为逐 finite-F 有界可逆同构。完整 Gram inverse/returns 均保留。原 physical source h 与 raw arch Mellin 向量 v 不同。Fourier H(t)=integral h(u)exp(-itu)du，receiver measure dt/(2pi)，source norm 是 du；裸乘法源为 exp(-u/2)h(u)。

先固定任意 complex h in C_c-infinity(R)，p 沿素数趋无穷，L=log p、r=p^(-1/2)、A=sqrt(p)/L、f_p=h+U_Lh。O_h 常数只依这一份固定 h、固定 cutoff 及所用有限 Schwartz 半范数，不依 p。没有 all-moving-h_p 或整个扩张 Dlog 单位球的 uniform rate。

在相同 Mellin 反射后，S 为 Pi_<p 的实际未加权正交投影，V 的乘子为 exp(itL)，D=I-rV，B=2I+V+V*，W0=|H(-t)|^2，W=W0B。若不反射则所有乘子同步反射，数值不变。0<=B<=4，W>=0；不能假定 S 与它们交换。

已付 C052 的统一整个复盘评价界是

    sup_(|z|<=R)|v(z)| <= exp(C R log(R+2)) ||D_F v||_2,

C 对所有有限 F 一致。其 Hardy/arch-conjugation/strip 去 prefactor 的角色不可用逐 F norm 等价代替；后者多付 exp((2+o(1))A)，会破坏 Taylor 预算。实际 diagonal 为 k_F(t,t)=|D_F(t)|^2 Q_F(t)，Q_F 为这个 weighted unit ball 的评价范数平方。k_F=2pi rho_F，没有额外 2pi。

## 3. 独立核 shrinking localization 与三段速率

原 6.1 proof 的 VK/Perron 误差是 y exp(-c_B (log y)^(1/3)/(loglog y)^(1/3))。在 y>=sqrt(X) 用固定 2B 覆盖 twist，分部积分的微分只打 y^(-1/2)/log y；不生 |t| 费用。低 y、去高 powers 的误差均 o(A/L)，主积分端点以 |1/2-it|^(-1)<=2 得 O_B(A/L)。因此全固定 B 的绝对一致 O_B(A/L) 升级确实来自已写 proof，非将 statement 的 o(A) 直接改字。

Euler log 的 k>=2 总费 O(log L)=o(A/L)。在 J_X=[pi/L-L^(-2),pi/L+L^(-2)] 上权 exponent >=4A-C A/L，weighted unit v 的 L2(J_X,dt) <=sqrt(2pi)exp(-2A+C A/L)。

缩集插值是本次必须量化的地方。对 measure m 的集合，先取半测度 good set，再选等测度 quantile nodes。Lagrange 分母含 (m/(C(n+1)))^n j!(n-j)!；求和的 2^n/n! 消去 n^n。故真实因子是 C m^(-1/2)[C(T+1)/m]^n，没有遗留 n log n。此证明允许 m=2L^(-2) 及 complex polynomial。

取 R=A/(log A)^3、n=ceil(3A/log A)、T=L^b，b 首先固定。Cauchy remainder <=exp(-3A+O_b(A log L/L))，插值费 log M=O_b(A log L/L)。由 weighted smallness 得

    log Q_X(t)<=-4A+C_b A log L/L, |t|<=L^b.

再乘 uniform prime envelope exp(4A/sqrt(1+4t^2)+C A/L)，对 delta=L^(-2/5) 有 delta^2=L^(-4/5)>>log L/L，于是

    sup_(delta<=|t|<=L^b) k_<p(t,t)<=exp(-c A delta^2).

省略最后素数 p 只改变 log 权 O(p^(-1/2))=o(A/L)；对 predecessor weighted norm 重跑同一评价/插值，而非猜 inverse Gram 单调方向。C052 评价已对所有有限 F 一致，故 omit-p 无新费用。

固定 chi 后三非负权分别为 w chi(t/delta)、w[chi(t/L)-chi(t/delta)]、w[1-chi(t/L)]。中段实际延至 2L，取固定 b=2 覆盖。central Cayley 尺度 delta 上二阶 circle derivative 只费 (1+Ldelta)^2，因此交换子为 O_h((1+Ldelta)^(3/2))=O_h(L^(9/10))。中段 positive-compression trace <=C_h L exp(-c A delta^2)。尾在固定 Cayley 尺度1上以 Schwartz 衰减支付，固定 N=4 给 O_h(L^(-2))。没有使用 sharp lower 或重新优化指数。

## 4. 独立核 actual unweighted Toeplitz kernel 与统一 rank bound

域稿不是仅说“de Branges/Toeplitz 类相似”。按 raw Mellin 和反射，g、Cg 都消失于 (0,1) 的两物理支持条件给

    K0={f in H2_+ : u_infinity overline f in H2_+}
      =ker T_(overline{u_infinity}),
    u_infinity(t)=gamma(1/2+it)/gamma(1/2-it).

域稿由 cosine Mellin multiplier 和 C 与物理复共轭 J 交换核出相位；第二条件用 CJg 支持得到，两向 membership 都成立。此处核在原 unweighted full-boundary L2 中。有限 D_F^+ 与 inverse 都属 H-infinity，但 norm 可依 F 很大；只用于代数双射：

    D_F^+ K0=ker T_(overline{u_infinity}/D_F^+).

所以实际 S 正是此未加权空间的正交投影。没有以 D_F^+ 当 unitary，没有消费 uniform inverse angle。可选的 unimodular symbol 变换也只用 invertible coanalytic Toeplitz 左乘，不进常数。

对 disk K=ker T_phi，full-boundary Z=M_z：forward block (I-S)ZS 落 H2 intersect K-perp，T_phi 在此 injective，rank(T_phi Z-ZT_phi)<=1 故该 block rank<=1。若 f(0)=0，完整 bar z f 仍在 K，因此 backward off-diagonal block 只依一个评价，rank<=1；可能的 negative-Hardy 分量没有丢。两个 block norm<=1，遂 rank[S,Z]<=2、S1 norm<=2。这里的常数与 phi 大小、F、range angle 均无关。

每个 Cayley 尺度 d 使用真实 boundary unitary sqrt(2d)/(t+id) times composition with b_d(t)=(t-id)/(t+id)，Jacobian 与 dt/(2pi)、dtheta/(2pi) 正好匹配。它保 Hardy 分解及 Toeplitz kernel，绝非 Euler weighted-range 的等距假设。整数 powers telescoping 后 trace-norm 极限给

    ||[S,M_(v(b_d))]||_S1<=2 sum |n||vhat(n)|.

Fourier 在 N 分割得到 N^(3/2)||v||2+N^(-1/2)||v''||2，N>=1 优化合法，恰付上一节中央/尾段预算。独立核未发现 [11] 新来源或未付定理依赖。

## 5. 严格 S1/HS 域与 exact projection/trace identity

此处必须保留域稿对原文的修补。对所用 bounded nonnegative u，定义

    tau_u=Tr_(SH)(S u S)=||sqrt(u)S||_HS^2.

560 的实际 compact-smooth trace 支付 tau_w<infinity；0<=u<=w 付各段。RKHS 正交基加 Tonelli 给 tau_u=integral u k_F dt/(2pi)。不声称 bare uS 或 WS 为 S1。

6.26 的严格因子为

    S u B(I-S)B S
      =(S sqrt(u))[sqrt(u)B^2S-sqrt(u)BSBS].

第一因子 HS norm=sqrt(tau_u)。后两项因 u 与 B 交换，分别写 B^2 sqrt(u)S、B sqrt(u)S B S，各 HS norm<=16sqrt(tau_u)。两 HS 乘积是真 S1，得到 <=32tau_u。先对全部 u=w 应用可先行证 covariance numerator X=S W(I-S)B S 为 S1，不依尚未证明的速率。

另若 [S,a] 为 S1，S a(I-S)=[S,a](I-S) 为 S1，6.25 的 ordinary trace norm 界由 bounded BS/G inverse 直接给出。G=S D*D S|SH=(1+r)^2I-rSBS，G>=(1-r)^2I；p>=2 时 inverse 有同一数值界。这里是新一步的 exact G，不是省略旧成长 G_F inverse。

D 映 predecessor range onto 新 range，J_D=D S G^(-1/2):SH->H 是 onto 新 range 的真实 isometry，故 S'=D S G^(-1) S D*。令 A0=SWS|SH 为 positive S1。由 W 与 D 交换，

    S D* W D S=A0 G-rX,
    X=S W(I-S)B S in S1.

新 localized trace 正确定义为 Tr_(SH)(G^(-1/2) S D* W D S G^(-1/2))；旧迹为 Tr A0。所有换序都是 S1 times bounded，得到 exact

    Delta t_p[f_p]=-r Tr_(SH)(X G^(-1))=-r C_p.

C_p 现实性由两个有限实正迹的差推出，无需对 formal non-S1 skew commutator 取迹。与第3/4节相接，实际得到 |C_p|<=C_h L^(9/10)、|Delta t_p[f_p]|<=C_h rL^(9/10)。两独占稿的条件在同一对象/measure/量词下互相补齐，不存在循环依赖。

## 6. 560 运输：全部 pp、原 du/2pi、pole-zero

不把原文未充分展开的 q_(infinity,F) 整体搬进仓库。实际从 560 已付式

    t_F[f]=q_Gamma[f]-P_F[f]+<f,K_(F,I)f>

相减。两个 F 在每个 p 用同一个含 f_p 支撑的 I_p，Gamma=2theta'、FP/contact 不动，全部 Lambda(p^k)=log p 保持。对 L>diam(supp h)，

    ||f_p||_du^2=2||h||_du^2,
    R_fp(+-L)=||h||_du^2,
    R_fp(+-kL)=0 (k>=2).

所以不是丢高 powers，而是其相关严格为零；新增 prime form P_p[f_p]=2Lr||h||_du^2。于是令 Delta K_p=K_(F_<=p,I_p)-K_(F_<p,I_p)，

    <f_p,Delta K_p f_p>
      =2Lr||h||_du^2+O_h(rL^(9/10)).                         (K)

系数2来自两侧相关；没有 2pi 遗失，因为相关与 source norm 均在 du。Rayleigh R_p=<f_p,Delta K_p f_p>/||f_p||_du^2 满足 R_p/(Lr)->1。这是 scalar statement，不是 operator convergence。

Pole 在同源差分中精确消去；不能把未选 primes 的 partial form 叫 full Q。若须显式双 pole-zero 子族，先固定非零 psi compact smooth，h=(D_u^2-1/4)psi。两 exponential moments 经 IBP 为零，平移继续为零；h 非零由 compact-support homogeneous ODE uniqueness 保证。所有 f_p 属原 zero-extension Dlog，且 ||f_p||Dlog<=2||h||Dlog；du norm 精确固定。未声称更强指数加权源半范数不成长。

## 7. 最强直接消费：有限 fixed Gram 与 shrinking-threshold count

本节独立检验 root 提出的直接推论；root 消息不作证明前件。证明仅用已闭合的 (K) 对 all fixed complex h 成立、J_p h=h+U_Lh 线性及 compact selfadjoint Delta K_p，不额开数学/来源预算。

在 base (-1,1) 任取先固定有限族 h_1,...,h_m。对 h_i、h_i+h_j、h_i+i h_j 等有限固定源用 (K) 并极化；常数只需在这有限集合取最大。置 w_p=L/sqrt(p)，同一 I_p 可取 (-L-2,L+2)，则

    <J_p h_i,Delta K_p J_p h_j>/w_p -> 2<h_i,h_j>_du.

这是 finite fixed smooth Gram 收敛，不能跳成全 L2 weak/strong 或 operator-norm 收敛。为得到任意 fixed m 的正方向，可在 (-1,1) 取 m 个互不相交小区间、各自非零 psi_j，再令 h_j=(D_u^2-1/4)psi_j 并 du normalize。其支撑仍互不相交，故 du orthonormal，且所有 h_j pole-zero。

L>2 时 E_p=J_p/sqrt(2) 在这份 fixed m-dimensional span 上是 du isometry。矩阵

    [<E_p h_i,Delta K_p E_p h_j>/w_p]_(i,j<=m) -> I_m.

有限维中 entrywise 等同 operator-norm 收敛，因此最终 compression >=(say 3/4)w_p I_m。560 对每个 p/共同 I_p 给 Delta K_p 自伴紧；min–max 遂给最终至少 m 个 positive eigenvalues >w_p/2。准确量词是

    for every fixed m, exists P_m, for every prime p>=P_m,
    N_+(Delta K_p ; w_p/2)>=m.

故该 shrinking-threshold count 趋于无穷。没有 m=m_p 的量化增长率；没有固定正阈值、全 operator 非消失 norm、Delta K_p>=0 或 complete K/Q 符号。w_p->0，故这个计数与增量 norm 可能趋零并不冲突。它是同一次 bound 的 finite polarization/min–max 后果，不另计研究轮，也不重做旧 587 的 whole-K 正本征值下界。

## 8. 最强旧扣除、剩余范围与结算建议

585 给每个 fixed source 的 whole K_X 正发散/必要费；587 给 fixed finite source basis 的共同 lower 和 whole-K/补偿秩后果；589 给 fixed-pair trace 经 anchor normalization 的 mean rank-one 极限；591 给共同 positive occupation covariance 的三 fixed-test gap 及正 gain 必要费。这些都没有控制相邻 cofinal predecessor 的 signed difference，也未给对移动双脉冲源的 o(Lr) trace 更新。两个成长/发散的 lower、或 fixed-source ratio limit，不能相减推出本次单素数速率。587 的 whole K 正 eigenvalues 也不能相减推出本次 Delta K 的 shrinking-threshold count。

因此新增付款不是旧 560 差分恒等式的换名：新增为真实 predecessor 投影上的定量 covariance 小费，经 exact Gram update 和 560 后获得 (K)，及第7节直接最强后果。这确实改变局部选择：此一 actual increasing-Sonin trace 没有吸收测试上的 leading critical-prime term。若 root 全部消费，统一一个数学迭代合理；不能因门尚未建 C059 就固定为0，也不能将已经完成的新有符号比较藏成 source-only0。

宏观关键瓶颈保持：Lr->0，没有合法 prime 增量累积/cross 费用，没有 whole K 有利号/全原范数小费，没有危险 core/cross、成长窗 full-Q/coercivity、primitive/principal/整过滤/截面乘法/mixed/通常 Xi 的独立算术输入。542+555->557 leading4/5 仍为负惯性 UPPER。已付 safe-high transport 也不因本稿重新变成未知或获得重计。本结果不排除成长源/成长秩/非局部 resummation 或别的 signed 联合机制，不完成长期 Goal。

实质阻断点：在本门实际范围内未发现。修补只限原文 shorthand 的严格 trace 解释和以旧560替代不展开 q 的运输；两项已自含闭合，不改原件。若任何被冻结 input 的语义或 SHA 改变，应冻结依赖本稿的 root 消费并重核 affected chain，不能仅沿状态标签继续。

本分工终态：proof/fresh 审核完成，待 root 作实际合并消费及唯一 cadence/看板/文献范围/Git 结算；本分工没有后台 shell、数值或待续来源进程，没有自动后继。本文本身不把 draft completion 当 root-consumed result。
