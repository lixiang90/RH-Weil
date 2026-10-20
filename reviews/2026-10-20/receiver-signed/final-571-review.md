# 571 fresh 独立终审：真实 receiver、双边界与成长归一平均

2026-10-20；独占终审，不改 STATE、cadence 或 Git，不代 root 消费或宏观结算。
审查人 `/root/review_receiver_571`。按 README/STATE/check/show 恢复 C034、同
G20261014／0c4f≤538 固定基线、D20261020N、前沿、570 结算及 560 §§2–6。
本文审的是最终主 571、三份独立原稿及其闭合前件，不由 producer 的完成状态认证结果。

**结论：PASS，限下列对象和量词；没有阻断数学问题。**
真实 receiver 的完整双边界身份、正向一侧费用、单 prime 的 Γ 锁定两号序列，
以及 cofinal 的 m² 归一同步高度平均均成立。它们不推出实际 Sonin ε 的新符号、
原范数成长小费、独立 RR 容量或完整 Weil 正性；strong-old whole leading4/5 未改。

## 1. 原对象、归一及完整 inverse 审核

物理空间是原酉 log 范数的 L²(R,dy)，B 是 normal、有界可逆的 causal 卷积，
D=B⁻¹；没有把 B 当酉。整线酉的是 all-pass BD*=B(B*)⁻¹。
P、L、H 分别为窗 (0,T)、低半线与高半线；G_T=PWP 是 window Gram，
不同于 Sonin 子空间上的 G_F。w、k_R、原 Weil 源 r 三种角色保留。

独立检查因果关系 LD=LDL、DH=HDH，得

    LZL=D_LD_L*，HZH=D_H*D_H，
    LZH=D_L(LD*H)=(LD*H)D_H，
    K=D_L⁻¹(LZH)D_H⁻¹=LBD*H=LD*BH。

半线 D_L、D_H 的逆为相应 B 的压缩；原 Hilbert 域上均合法。
取 A=D_L⊕D_H*、J=[[I,K],[K*,I]]，逐 block 核得

    QZQ=AJA*，QZPw=A(v,u)，v=LD*Pw，u=HDPw。

因此 Schur 补确实消费同一真实 receiver pair，并给

    δ(w)=||v||²+||u||²−〈(v,u),J⁻¹(v,u)〉。

正平方根归一稿的 C 与 K 不是字面相同的 map。显式令
U_L=(LZL)⁻¹/²D_L、U_H=(HZH)⁻¹/²D_H*，二者为相应半线酉算子；则
C=U_L K U_H*、α=U_Lv、β=U_Hu。故两个稿的二次型、norm 和 κ 一致。
主稿已经说明这个坐标运输，未把 α=v、β=u 偷作同一对象。

由 QZQ≥M⁻²I、||A||≤m⁻¹ 得 J≥(m/M)²I，故 κ≤1−(m/M)²<1。
这是每先 fixed F 的完整 inverse gap；并非 growing-F 一致 gap。
原 residual 的两项与 Schur scalar 完全一致，没有截掉全 G_T⁻¹ 或 returns。

## 2. signed 方向与实际 carrier 反射

逐项反算 J⁻¹，cross 是
2Re〈v,K(1−K*K)⁻¹u〉，两个 self-return 带负号。
完成平方严格为

    δ(w)=||u||²−||(1−K*K)⁻¹/²(u−K*v)||²。

交换左右亦成立，故 δ≤min(||u||²,||v||²)。J 的两端谱界给

    −κ/(1−κ)·B ≤ δ ≤ κ/(1+κ)·B，B=||u||²+||v||²。

正向 upper 确无坏 gap 分母；不能因此宣称 δ 非负、非正或 receiver norm 很小。
去掉首个 cross 后，全部余项合计费用 κ²B/(1−κ)，原式仍保留完整 returns。
J 正属于被减的 Gram；一般 causal filter 同样拥有它，不自动支付 Weil 的正号。

对实际 carrier w=e^(iRy)1_(0,T)/√(2π)，实系数反射
R_Tf(y)=overline(f(T−y)) 给 u=e^(iRT)R_Tv，||u||=||v||。
相位始终由同一 R、T=完整 Γ(R) 决定，没有把两个 receiver 自由配准。
receiver 原 norm 的 coherent 双和以
ℓ_T(x,z)=min(min(x,z),(T−|x−z|)_+) 为实 overlap 长度，式子正确。
Σc_xc_z min(x,z)≤D0J0 支付绝对换序；这仅给旧第一矩 upper，未升为 lower。
κ≤MΣ_(x>T)c_x 的 tail bound 也由真实 all-pass block 得到。
fixed-F 的 O(e⁻γT) 是旧 exact/第一矩的直接合成，不能作为新 whole 容量重计。

## 3. 单 prime full inverse 与严格 Γ 锁定的两号

独立用 tridiagonal 乘法核主稿 (11)–(12)，包含两个端点；n=1 退化式也一致。
每 n 点 fibre 的 Δ_n 满足主稿 (13) 的 rank2 表达，n≥2 恰有一正一负。
这仅指每个 fibre；整个连续直积分不是有限秩2。主稿已明确限定。

实际 fibre receiver 直接由 D* 的完整几何和得到

    v_(-ℓ)=e^(iRx)q^ℓ(1−ζⁿ)/(√(2π)(1−ζ))。

平方并按 fibre 的 a−τ、τ 长度积分，主稿 (14) 系数 q²/[2π(1−q²)] 正确。
跨窗 norm 比 q^(n+1)/(1−q²) 亦正确；这里是 norm 比，非 squared norm 比。
固定 p 的加权原 receiver norm² 有非零有限极限，相对 ||w||²=T/(2π) 为 O(1/T)。

再以真实 carrier z=(1,e^(iθ),…,e^(i(n−1)θ)) 代 Δ_n，核得

    |b_p(R)|² d_n(θ)
      =2q^(n+3)cos[(n−1)θ+2arg(1−qe^(iθ))]/(1−q²)
        +O_p(q^(2n+2))。

Γ(R)=log(R/(2π))+O(R⁻²)、Γ′(R)=R⁻¹+O(R⁻³) 只用于估误差，未取代完整定义。
取 Γ(R_N⁰)=Na，在其右长 8π/(Na) 的小区间相位至少走过4π，故有 cos=±1。
τ=O_p(q^(2N)/N)，所付长度扰动 O_p(q^(3N)/N) 严格小于主项。
据此主稿 (15) 系数

    ±a q^(N+3)/[π(1−q²)]

正确，无漏2或2π，且 |b| 有固定正下界，不影响两号存在。
这是 R→∞、T=Γ(R) 的实际 carrier 序列，不是固定 T 后自由选 R。
其量级 R⁻¹/² 被 560 较慢的 carrier/clipping 误差覆盖，不能运输成 actual ε 的符号。
也不由 single prime 宣称 joint{2,3} 的 window 符号；570 的 actual 源定理是另一对象。

## 4. cofinal 同步成长平均：逐笔核原 norm 及极限顺序

固定 θ>1，β∈(0,1)、ε>0 满足 1+ε/2<βθ<θ；先如此固定，再 L→∞。
F_L={p<e^(2L)}，R0=exp(θe^L)、H0=R0^β，R∈[R0,R0+H0]，始终 T_R=Γ(R)。
本审独立重算三笔估计：

1. 为估计截 log n≤A=(2+ε)e^L。在 L²((0,∞),dt) 内，有限系数
   f_n(t)=n⁻¹/²1_(t<logn<t+T0) 的 norm²=n⁻¹min(T0,logn)。
   这是本次提出并由 root 已修正的主稿域小点；若读整线，范数会错误地变为 T0/n。
   log n 的 local real spacing≥1/(2n)，有限 Hilbert-valued MV 给
   mean||v_A||²≤C(L²+AΨ/H0)。Σsmooth(logn)/n=O(L²)，且 Ψ≤e^(A/2)/m。
   原高度起点只给系数乘 unit phase；有限 span 的正交坐标求和不引入维数费。
   乘 m²/T0 后有限和 error≤Cexp[−(βθ−1−ε/2)e^L]，量词正确。
2. 完整 inverse tail 全部加回。其 operator norm≤m⁻¹μ(X>A)，故归一尾费≤μ²。
   560 已付 EX=2e^L+o(e^L)、VarX=O(Le^L)，Chebyshev 给 μ≤C_εLe⁻L。
   没有把无限 smooth 级数套在发散的 Σn||f_n||² 上。
3. 完整 Γ 使 Δ_T≤CH0/R0；hard endpoint 原 carrier 差的 norm² 是 Δ_T/(2π)。
   经 D* 后的 m⁻²费保留，m²/T0 归一后是 O(H0/(R0T0))。
   因此是真正 moving T_R 的结论，不是假装 fixed T 的 Bohr 平均。

由三笔费用及 T_R/T0→1，主稿 (16) 的
mean[m²||v||²/||w||²]=O(L²e⁻L)+O(e⁻ce^L)→0 成立。
它也控制同一归一的 δ_+，但不是逐 R、θ≤1 或 ALL complex 源结论。
当1<θ<2时它与旧 ambient m||H D L||→1 可以同时成立。
特别明确：它不证明 m²||H D L v||²/||v||² 小，也不排 normalized receiver
方向在某些 R 饱和全空间 tail norm。主稿已加入此限制。
本审又针对 root 最后补入的强旧比较重读 555 §§3–4：β_L/e^L→1，而此处
Γ(R)~θe^L、θ>1，确在旧标量比较的有利高频层，未覆盖 Γ 约≤e^L 的危险 core。
这个比较只识别谱高度与旧费用，不将 Fourier 频带投影当作合法 compact 源；
故本轮成长均值也不能以“同步”标签重报已付高频为新的危险核心正性。

还原原 norm 后的 T0m⁻²μ²、m⁻²Δ_T 与有限 MV cutoff 费用全部存在。
现有 upper 不能升为 O(L²)，但“大 upper”亦不是 actual receiver lower。
乘 actual |b(R)|² 的相关费用未付，粗 M²/m² 会耗尽当前小量。
单 prime 的 b 权精确抵消不具有可乘的 multi-prime norm 结构。
所以该平均是受限像的新限定信息，不是 Γ-relative 容量或 actual ε_(F_L) 的平均界。

## 5. 来源、完整 Weil 预算及准入边界

MV 来源记录与原 551 来源审计相符：Thm2 的 local Hilbert 常数3π/2，
Cor2 的 mean-square error3π，finite complex、distinct real-frequency 前件正确。
本终审实际读了仓库原来源审计和当前 source-read-record；root 本轮目视原 PDF
74–75页及读82页的事实由该记录承担，不冒称本审重证作者全套 lemma。
旧 MV、560 概率/第一矩、532/560 Γ 与 clipping 归旧来源，新综合未冒称新外部定理。

完整 Γ/contact、全部 log p·p⁻ᵏ/² 的 prime powers、双 pole 均保在 560 源身份。
本轮没有 pole-zero 源的附加假设，也未把这些项删去。dy carrier norm 不是未经运输的
du/zeroextension Dlog 源费。cofinal word/clipping 与完整 Sonin inverse 的旧证书缺口
仍在；它是证书不能给足够小误差，不是 actual clipping error 的必要下界。

一般 g 情形的 all-pass/Schur 身份要求真实 normal、bounded invertible causal B，
并有相应因果逆和 Hilbert 域；反射另需实系数。ordinary log-spacing、浓缩、diagonal
与计数不从一般对偶自动继承；exact collisions 必须 coherent 合并，连续分布须另给设施。
正 J、正 trace 或自伴有限矩阵均不付独立 RR/evaluation 容量。
直接假定完整 mixed Weil Gram PSD 是等价改写；足够强的有利 domination 若无来源仍是未付输入。

本轮新的是实际 receiver 完整 signed 组织、严格 Γ 锁定 single-prime 两号及上述同步平均。
strongest-old 542+555→557 leading4/5、危险 core、coupling、Ξ 识别和宏观容量瓶颈未改。
非有限秩 compact、Γ-relative、source-adapted、不同全逆组织及真实 global 几何修复均保合法。
不能据本轮通过 Goal 的强方法类失败门，不能自动续开 unknown weighted-tail 合同。
root 须另核下轮新 input/test/net；停止单prime相位、N、m归一参数优化的决定与证据相符。
本 PASS 允许 root 消费此一研究迭代，不结算 cadence、不完成长期 Goal。

## 6. 最终 LF 版本绑定

hash 仅绑定受审前件；数学审查在上文，不由 hash、check 或 agent 状态认证。
规范化只将 CRLF 换为 LF，其余 bytes 不改。实际主稿域修正已复读后取 hash。

| 受审文件 | LF SHA256 |
|---|---|
| notes/571-actual-receiver-two-boundary-signed-comparison-and-growth.md | `c7f0cf4712bdbb9429c4356c3974098b9c39b2eba4486b91c800fb7653cf109e` |
| reviews/2026-10-20/receiver-signed/exact-receiver-and-boundary-sign.md | `ea55881593c9969ef81e28a7e90d0f730d5d32404a8405b77325eaaedcc77e86` |
| reviews/2026-10-20/receiver-signed/receiver-norm-and-growth.md | `e21c72e41ca37f949b81b585147364bc19b3b347a56caf2d764a06a2ec7a0093` |
| reviews/2026-10-20/receiver-signed/independent-model-tests.md | `b3f02e80b60d31b267b28a75d889ad66911da03ecd909df8e2b591ecd2c435d7` |
| goals/contracts/C034-actual-receiver-two-boundary-signed-comparison.md | `59e914c202716af237ce7de8bd57f33740b46c671fbd1b3fe19790d57f80bd63` |
| notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md | `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3` |
| notes/555-actual-prime-weighted-schur-and-growing-weil-inertia.md | `55a3745ab8160738e2a2dde15e84290e99205df68f3b59b357d26127846a31c5` |
| reviews/2026-10-20/receiver-signed/source-read-record.json | `43193639b4cc5a7b4608699bbdd789c3191b895646378d300ffea593bebc3505` |
| goals/GOAL.20261014.md | `cc6046029a8e5c9fe4eae427dfd663f1d851666370637c8fd451042f340fee8b` |
