# GY physical-row 原核、完整混合运输与未付槽逆审

2026-10-14；独立审查，来源准备 **零数学轮**，不建立 C021。
恢复 AGENTS/README/STATE、check/show、同 G20261014 Goal/frontier、C020 与
D20261014V；结构检查通过不认证数学。恢复时 HEAD 为
`5e65cc4637fc2d89edd83a85a4e492a5a6cd3608`。现场 root 正在修改
STATE/git 属性和本审查目录，不能把此前 clean 快照当作当前事实。
子代理 get_goal 为 null，不代替 root 的 runtime Goal 观察。
以下只审原 du 对象和来源消费范围，不改 STATE/cadence/Git。

## 1. 对象、精确 cutoffs 与完整三通道

固定 Y→∞、sqrtY≤T≤2sqrtY、h=1/T、|τ|≤T，先取
U=U₂=floor(T/log²(e+T))；后面明确区分 U_B=floor(T/log^B(e+T))，B 先固定。
所有整数源严格截于 Y<n≤2Y，定义

    s(x)=x^(−1/2−iτ)e^(−x/Y)，E_x(u)=1_[logx−h,logx](u)，
    p(b)=Σ_(Y<n≤2Y)b(n)s(n)E_n，
    c(u)=∫_Y^(2Y)s(x)E_x(u)dx。

Hilbert norm 是 L²(R,du)，不是 coefficient diagonal、label norm 或 dx。
按 164 的 Vcut=1 精确恒等式，Λ(1)=0，

    I_U(n)=Σ_(d|n,d≤U)μ(d)log(n/d)
          =Λ_U(n)+log(n/U)a_U(n)，
    Λ_U(n)=Σ_(d|n,d≤U)μ(d)log(U/d)，a_U(n)=Σ_(d|n,d≤U)μ(d)，
    II_U=Λ−I_U=μ_(d>U)*Λ_(m>1)*1_r。

Λ 包含全部实际 proper prime powers。改变 U 时 I 与 II 同时改变；目标不变。
用 linear-first 内积，令 z=(p(I_U),p(II_U),c)、G_ab=〈z_a,z_b〉。
实际 Hodge 方向是 v=(1,1,−1)，完整原型为

    H=||p(Λ)−c||²=vGv*
     =G_11+G_22+G_33+2ReG_12−2ReG_13−2ReG_23。        (1)

不能省掉任一 companion 或 continuum cross。消去 II=Λ−I 后，(1) 恰等于

    H=G_(Λ,Λ)−2ReG_(Λ,c)+G_(c,c)。                   (2)

因此仅付款 Λ/I 或 I/I，不自动付款 (2) 的 Λ/Λ。

## 2. 所有 lag 的 triangular 核与 phase/BV 费用

精确原核为 K_h(x,y)=(h−|log(x/y)|)_+。
对整数 j，令 J_j=(max(Y,Y−j),min(2Y,2Y−j)]，

    w_j(x)=[x(x+j)]^(−1/2)e^(−(2x+j)/Y)
       ·exp[−iτ log(x/(x+j))]·(h−|log(x/(x+j))|)_+。

对任何实际系数 b,d，

    〈p(b),p(d)〉=Σ_(j∈Z)Σ_(n∈J_j∩Z)b(n)overline(d(n+j))w_j(n)。  (3)

j=0、负 j、端点全部保留；w_(−j)(x+j)=overline(w_j(x)) 给 Hermitian 对称。
非零核要求 |j|≤2Y(e^h−1)≤4Y/T，故是全部成长 lag，绝非 fixed-shift 外推。
以 zeroextension 在 J_j 上计算总变差，有绝对常数

    ||w_j||∞+Var(w_j)≤C h/Y。                        (4)

理由：amplitude 导数 O(Y^−2)；log-ratio 导数 j/[x(x+j)]；
|τ j|/Y²≤C/Y，故 native complex phase 只消耗常数；positive-part 核导数
≤C|j|/Y²≤Ch/Y，其长度 Y 上的变差 O(h)。两端跳变和核的 kink 包含在 (4)。
乘 log((x+j)/U) 的 sup+BV 至多再消耗 C logY；乘两项 log(x/d)log((x+j)/e)
至多消耗 C log²Y。这里没有删 τ、再用无相位结果顶替 (3)。

若 E_j^L(z)、E_j^a(z) 分别是 Λ(n)Λ_U(n+j)、Λ(n)a_U(n+j) 的实际 block-prefix
误差，则 Abel 运输给

    total error ≤ C(h/Y)Σ_(|j|≤4Y/T)
                    [sup_z|E_j^L(z)|+logY·sup_z|E_j^a(z)|]。 (5)

若只知共同上界 E_L,E_a，即是 C(E_L+logY E_a)/T²。
所谓 E/T² 必须把 a_U 的 logarithmic correction 已纳入 E；不能免费省这一 log。
从 Λ_U 原定理的 big-O 关于 U 求导，并不能获得 a_U 误差定理。

## 3. 直接 AP 的合法变 cutoff 逃逸

原 [GY math/0111212v1](https://arxiv.org/html/math/0111212v1) §4 的
(4.3),(4.7) 是可消费的 finite-divisor/AP 机制；(1.30) 用 x^(1/2−ε)
的弱 BV，Theorem 4.1/(4.6) 的 R 范围不能直接代入 U₂。
不把其已经求成 singular series 的结论移到 physical j≈sqrtY。

保 native finite sums，定义

    A_U(j)=Σ_(d≤U,(d,j)=1) μ(d)/φ(d)，
    B_U(j)=Σ_(d≤U,(d,j)=1) μ(d)log(U/d)/φ(d)，
    Δ(2Y,U)=Σ_(d≤U)max_((a,d)=1)sup_(v≤2Y)
                         |ψ(v;d,a)−v/φ(d)|。

直接 AP 给 Λ/I 的原 mixed main

    Σ_j∫_(J_j) w_j(x)[B_U(j)+log((x+j)/U)A_U(j)]dx。 (6)

每个 physical j 只选择 residue −j mod d，故 Δ 的 residue-max 保全部 j；不需 fixed-j。
coprime block-prefix 的误差至多 2Δ；log multiplier 和 (4) 全部计入。
noncoprime residue 不能按零删除：Λ(n)≠0 时 n=p^k、p|d。
在 (Y,2Y] 每个 p 至多一个 power，故每 d 的此类 Λ 质量≤Σ_(p|d)logp≤logd。
保 proper powers 可直接给总 weighted 误差

    |G_(Λ,I)−(6)|≤C[logY·Δ(2Y,U)+U log²Y]/T²，       (7)

也可安全消费来源审的稍弱 U log³Y 上界。
这是两个原 AP slots 分别证明后相加，不是对 GY error 求导。

经典 log-level BV 若给 Δ(2Y,U)≪Y/log^A Y，在其合法
U≤sqrtY/log^(B_A)Y 范围内，(7) 为 O(log^(1−A)Y)+o(1)。
另一个已原件核验的 Vaughan 显式形式是

    Δ(x,Q)≪_A x/log^A x+sqrtx·Q·log^6(xQ)。          (8)

(8) 来自 R. C. Vaughan 作者一级原件
[The Bombieri–Vinogradov Theorem](https://personal.science.psu.edu/rcv4/Bombieri.pdf)
第 3 页未编号 theorem，sup_(y≤x) 在 modulus/residue 求和内；第 1 页 (1)/(2)
用完整 Λ(p^k)、k≥1 定义 ψ。其字节版本见同目录 native-ap-source-and-log-critical-errors.md，
本审不以 GY 的弱 (1.30) 代替 (8)。取先固定 A=4、B=10、U=U₁₀，
Δ≪Y log^−4Y，(7)≤O(log^−3Y)+O(Y^−1/2 log^−7Y)=o(1)。
U₂ 代入 (8) 所得 total upper fee 含 O(log^5Y)，没有付款 o(1)；
这是该上界未给足节省，非必要发散或反例。
**U₁₀ 是合法 different-cutoff 逃逸**，必须保新的 II₁₀/cofactor shell 与 continuum。
它只支付 (6) 的误差，不支付 native main 与 (2) 的 signed 比较。

## 4. Pure I/I：全部 CRT main 与可核 remainder

对 d,e≤U，n≡0 mod d、n≡−j mod e 可解当且仅当 gcd(d,e)|j；
解集合是一条 mod[d,e] progression。任意 block-prefix 的计数误差 O(1)，
uniform 全 j，包括 j=0。两项 logarithm 原样留在积分，因此

    G_(I,I)=Σ_j Σ_(d,e≤U) μ(d)μ(e)1_(gcd(d,e)|j)/[d,e]
       ·∫_(J_j)w_j(x)log(x/d)log((x+j)/e)dx
       +O(U²log²Y/T²)。                              (9)

(9) 由 CRT count 与 (4) Abel，非 singular-series近似。
U₂ 的 remainder 为 O(log^−2Y)=o(1)；先固定 B>1 的 U_B 则为 O(log^(2−2B)Y)=o(1)。
这付款完整 pure main+误差，**不单凭 CRT positivity 付款 main 的小ness或取消 Λ/Λ**。
若分成 Λ_U/a_U 三个子Gram，log corrections 和其 cross 仍包含在 (9)。

arithmetical diagonal 另可直接核：

    G_(Λ,Λ)^diag=hΣ_(Y<n≤2Y)Λ(n)²e^(−2n/Y)/n=O(logY/T)=o(1)。

用 Λ²≤log(2Y)Λ 与 Chebyshev。对 n=p^k，

    I_U(p^k)=klogp−1_(p≤U)(k−1)logp，

所以 Λ/I 的 diagonal 同样保 proper powers 并是 O(logY/T)。
pure I diagonal 包含非 primepowers，在 (9) 原 CRT 中保留。
以上 diagonal smallness 不付款 Λ/Λ 的全部 near off-diagonal。

## 5. 强旧聚合：Type I/continuum 已能近似，不能重复登记

来源筛选过程中复核出比 549 所列 O(log⁶Y) 更强的旧后果。
此节消费旧 085 的经典 μ-Mertens bound、159 的 m₀,m₁、164 exact synthesis，
结合 elementary grid/Chebyshev/ordinary PNT；不算新增来源或一轮研究。

对固定 u，J(u)=(Y,2Y]∩[e^u,e^(u+h)]。每 d≤U 的整数 d-grid 之和与
(1/d)∫_(J(u))log(x/d)s(x)dx 的 discrepancy ≤sup+TV。
window 长≤CY/T；|τ|h≤1 给

    discrepancy_d ≤ C logY/sqrtY。

所有 clipped endpoint 均是同一合法 grid estimate，无 complete-window 假设。
合并 density 为 m₀(U)logx+m₁(U)，其中

    m₀(U)=Σ_(d≤U)μ(d)/d，m₁(U)=−Σ_(d≤U)μ(d)logd/d。

旧 μ-Mertens stretched-exponential bound 经 Abel 给任意固定 A 的
m₀(U)=O_A(log^−A U)、m₁(U)=1+O_A(log^−A U)；常数 0 与 1 来自
1/ζ(s)=(s−1)+O((s−1)²)，尾收敛由该同一旧 bound 支付。
U_B 的 logU≈(1/2)logY，所以

    ||r||₂≤||r||∞·sqrt(log2+h)
           ≤C_B log^(1−B)Y+O_A(log^−A Y)，r=p(I_U)−c。 (10)

特别 U₂ 给 ||r||₂=O(1/logY)。这付 actual aggregate direction，较 individual-j
main 更直接；不主张对任意 head profiles 的 operator norm。

令 q=p(Λ)−c。窗口 integer-count/Cauchy 与 Chebyshev 给

    ||p(Λ)||²≤C Y logY/T²≤C logY，||c||²≤CY/T²≤C。

故 ||q||²、||p(II₂)||² 都为 O(logY)，且 p(II₂)=q−r 给

    ||p(II₂)||²−||q||²=O(log^−1/2Y)=o(1)。           (11)

这比旧粗 O(log⁶Y) 强，root 应更正最强旧比较；不由改正重新计轮。
即使 qualitative flat-label η(Y)M 真，也须至少胜本节旧 O(logY)，不能只胜粗 log⁶。

Λ/continuum 的 integrated signed cross 也已由 ordinary PNT 付款。
写 linear-first mixed weight

    W(x)=s(x)∫_Y^(2Y)overline(s(v))K_h(x,v)dv
        =∫_{[-h,h]∩[log(Y/x),log(2Y/x)]}
              (h−|t|)e^((1/2+iτ)t)e^(−x(1+e^t)/Y)dt。

原 x-phase 精确消去。||W||∞≤Ch²；内部导数 O(h²/Y)，
两端动态 integration-boundary 的导数 O(h/Y) 仅在宽 O(Yh) 的 strip，
其总 BV≤Ch²；zeroextension 端点跳变同费。因此 sup+TV≤Ch²，uniform τ。
对 ψ(z)−z 的原 prefix o(Y) 做 Abel，全部 actual primepowers 原样保留，得

    〈p(Λ),c〉−||c||²=o(Yh²)=o(1)。                 (12)

(2) 即 ||p(Λ)||²−||c||²+o(1)。PNT 给 (12)，不宣布每个短interval Λ−1 小，
也不支付 Λ/Λ 的原 full-nearproduct norm 节省。

## 6. actual Γ、Dlog 与完整 signed Weil 费用

每个有限 p 源 zeroextension 为 BV。c 连续分段光滑：内部
c′(u)=b s(b)−a s(a)，a=e^u、b=e^(u+h)；边界 strip 只有一个 endpoint，
积分端项一并计入。|τ|≤T 给 Var(c)≤CsqrtY；因此所有本节源属于 Dlog，
并属于 full actual Γ multiplier operator 的域。

Fourier 规范 F(t)=∫f(u)e^(−itu)du；actual Γ(t)=Reψ(1/4+it/2)−logπ=2θ′。
令 Φ=Γ−Γ₀≥0，J_+(f)=(2π)^−1∫(1+Φ(t))|F(t)|²dt，
与 ∫log(2+|t|)|F|²/(2π) 等价。这里是原 full-frequency zeroextension 型，
不是 periodic/regional 核或单有限频带。

Σ_(Y<n≤2Y)|I_U(n)|≤CY log²Y，故 Var(pI)≤CsqrtY log²Y。
Chebyshev 更直接给 Var(pΛ)≤CsqrtY；加 c 后仍可用上述界。
BV Fourier 尾 |F_r(t)|≤CsqrtY log²Y/|t|；取 R=Y²，

    J_+(r)≤C logY||r||²+C log⁵Y/Y=O(1/logY)=o(1)，
    J_+(q)≤C logY||q||²+C logY/Y=O(log²Y)。          (13)

第二行并未推 q 小。r 的 Γoperator平方亦有同样 BV 尾，但不能把
operator平方/β² 的费偷换成 /β 或 J_+。

共同 support [logY−h,log(2Y)] 可平移至 I₁=(−1,1)。平移保 autocorrelation、
Γ 型和 A_+(f)overline(A_−(f))，因为 A_± 的 e^(±a/2) 因子相消。
完整 Weil 型为

    Q(f)=(2π)^−1∫Γ|F|²
        −Σ_(n≥2)Λ(n)/sqrt n·[h_f(logn)+h_f(−logn)]
        +2Re[A_+(f)overline(A_−(f))]，
    h_f(a)=∫f(v+a)overline(f(v))dv，A_±(f)=∫f(u)e^(±u/2)du。

在 I₁ 全部可能的 actual pp 是 2,3,4,5,7；它们及两个 signed pole
是 bounded型。实际较短 common support 上无相关的项按精确 zero overlap 为零，
不是人为截断。尤其没有删除 odd negative pole。
polarized linear-first B_Q 在这些原域满足

    |B_Q(f,g)|≤C sqrt(J_+(f)J_+(g))+C||f||||g||。     (14)

β≥c log(e+T) 时 (13),(14) 与 pII₂=q−r 给

    |Q(pII₂)−Q(q)|/β
       ≤[2|B_Q(q,r)|+|Q(r)|]/β=O(log^−1/2Y)=o(1)。 (15)

这是强旧完整 normalized-Q proximity，非 Q(q) 小、正性或全域符号结论。
单 AP/L² Gram 小本身不能推 (13)：此处 Γ 尾由独立 BV estimate 支付，
不能把 549 flat-label Γ 付款自动赋给 actual growing all-ones direction。

## 7. 尚未付、停止与唯一准入责任

已核 AP 合法 U₁₀ 逃逸、full-j phase/prefix/BV 运输、pure CRT 与旧 aggregate。
GY paper 不提供剩余 Λ(n)Λ(n+j) 全相关；其导言也明确指出该困难。
actual coefficients 的完整 core 责任仍是：

- Λ/Λ 全 off-diagonal triangular kernel 的定量净节省；已付 diagonal 与 O(logY)
  旧 aggregate upper bound 不代替它。
- 完整 physical H=||pΛ−c||² 的 barrier/core summation：本节仅一个
  sqrtY≤T≤2sqrtY、|τ|≤T、σ=1/2 的 finite topband；allheight/cofinal Abel/成长支撑仍未付。
- 需要更细 continuum coupling 时，保原连续 (x,v) 核；(12) 只消费 integrated
  topband cross，不给所有 modulated source/operator matrix 元。
- AP 的 native A_U,B_U 全 j main 与目标 signed 节省的比较仍须独立付款；
  U₁₀ 的 companion/全 cofactor shell 不可删。旧 (10) 已付款 I−c 的该 actual 聚合方向，
  不能将这个旧收益再作为新来源净值。
- 549 全 label 单位球与 actual ακ=1 的成长质量之间仍有 rate/collision 缺口；
  若转换 source/frequency/range，重新支付 Γ/pp/dual pole 及原域，勿交换量词。
- 成长全源/core覆盖、实际 ζ/Ξ 识别和 Goal forcing 均未改。

结论：本来源准备 **入口零轮止损**，没有 C021 准入三句中的新净后果。
所谓 U₂ 原 paper 范围缺失不是全方法反例，因为 U_B 直接 AP 逃逸合法；
另一方面其成功只复原经典 AP/CRT，而且完整 topband aggregate 已由强旧工具给更直接后果。
下一数学准入必须提出独立、非循环、能胜本稿强旧并触 core 的原 physical
Λ/Λ signed 定量输入或合法必要费用门；不能把 unknown whole domination 命名成输入。
本审文件保存结束；无新 producer/数值测试/轮数消费。
