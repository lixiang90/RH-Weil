# C012 native Chebyshev variation：独立核心逆审

2026-10-14，独立核验入口原件 S1–S8。本文仅归本代理所有，
不编辑 root STATE/cadence/Goal，不自行结算研究轮、提交或宣告宏观完成。

恢复次序已完成 AGENTS→README/STATE→research_state.py check/show→
GOAL.20261014/MACRO_FRONTIER/C012/D20261014M→所需原件；结构检查通过不认证数学。
现场 Git HEAD 为 6309e116e20e886b55a09e0674638b39e4edf349，恢复时工作树干净。
STATE 为 C012 ready、原 cadence 3，前两轮 C011 已止损；本代理不拿子代理 runtime
查询替代 root 的现场 Goal 身份。新基线仍 0c4f3a3/≤538，完整成长 signed 费用未付。

核验对象为
[入口](../c011-second/full-gamma-signed-bridge-entry.md)，
actual 定义交叉核对 [016](../../../notes/016-prime-graph-hodge-inequality.md)
顶部 2026-10-13 归一化纠错。S1–S4 是原规范恢复，不是新增独立正性。
本审查给出 S5–S8 的独立证明及准确修复量词；历史重复分类另由 root 消费原件审查。

## 1. actual Γ 核、原 norm 和整个闭型

固定 L>0，I=(-L,L)，complex f∈Cc∞(I)，零延拓到 R。使用

    F(t)=∫_R f(u)e^(-itu)du，N=||f||²，
    h(a)=∫_R f(u+a)conjugate(f(u))du，k(a)=Re h(a)。

Plancherel 精确给 ∫|F|²dt/(2π)=N 和
∫cos(ta)|F(t)|²dt/(2π)=k(a)。h(-a)=conjugate(h(a))，故 k 偶实；
positive-definite 不等于 k 逐点非负。

从 [NIST digamma 差分积分](https://dlmf.nist.gov/5.9#E16) 对
z=1/4+it/2 和 z=1/4 作差、取实部，再令原积分变量 v=2a，得

    Γ(t)-Γ(0)=∫_0∞ w(a)(1-cos(ta))da，
    w(a)=2e^(-a/2)/(1-e^(-2a))。

这里 Γ(t)=Re ψ_digamma(1/4+it/2)-logπ=actual 2θ′，Jacobian 2 必保留。
旧 half-θ′ 的核系数不能消费到本对象。reflection 和 duplication 给
ψ(1/4)=−γ−π/2−3log2，故 Γ(0)=−γ−π/2−3log2−logπ。

非负 Tonelli、而不是拆两个近零发散积分，给

    Γ-form(f)=Γ(0)N+JΓ(f)，
    JΓ(f)=∫_0∞ w(a)[N-k(a)]da
         =(1/2)∫_0∞ w(a)||T_a f-f||²da。       (A1)

T_a 为全 R 的酉平移；不能换成 overlap 内 partial graph 差。
w(a)=1/a+O(1) 于 0，smooth 源平移差为 O(a²)，远尾 w 指数可积；A1 因而有限。
该非负积分和 Fourier 侧 log-growth 同一闭型定义原 Dlog。
S1 系数、norm、全尾、合法域通过。

## 2. 双 pole、全部 primepowers 与端点

令 C=∫f cosh(u/2)、S=∫f sinh(u/2)。原两 Laplace 矩分别是 C+S 和 C−S，
所以完整 pole 精确为

    pole=2 Re[(C+S)conjugate(C-S)]
        =2|C|²-2|S|²=4∫_0∞cosh(a/2)k(a)da。    (A2)

prime 为 −2∫_(0,∞) z(a)dψ_Cheb(e^a)，z=e^(-a/2)k。
ψ_Cheb 含每个 p^j 的权 Λ(p^j)=log p；超出相关支撑的原 atoms 自动为零。
ψ_Cheb(1)=0，没有 a=0 prime atom；E=ψ_Cheb(e^a)−e^a，E(0)=−1。
因此

    pole+prime=2∫_0∞z(a)da-2∫_(0,∞)z(a)dE(a)，
    ∫_(0,∞)z dE=[zE]_0∞-∫_0∞E z′da
                =N-∫_0∞E z′da。               (A3)

z 在远端为零、原右端点 z(0)=N。对连续 smooth z 与 locally BV E，
Stieltjes 分部积分适用；它精确包含 −2N 质量项，没有忽略 prime atoms。
把 A=E+1 时 ∫A z′=∫E z′−N，故

    Q=(Γ(0)-2)N+JΓ+2∫z+2∫E z′，
    Q= Γ(0)N   +JΓ+2∫z+2∫A z′。              (A4)

S2–S4 通过。Stieltjes 式在固定窗由有限 atoms 和连续项定义；
导数式此次只在 smooth core 使用，不预设全 Dlog 的 h′ 存在或其绝对费可积。

## 3. 任意 fixed L 的真实 prime-free carriers

取长度 b<min(2L,log2) 的小子区间 J⊂I，冻结 real g∈Cc∞(J)、g≥0、
||g||=1，且有非空开区间上严格正。H(a)=h_g(a) 为 smooth、非负、偶，
H(0)=1，H′(0)=0，支撑在 [−b,b]；H 在一些正 a 区间严格正。
对所有 ω>0 使用原合法 complex 源

    f_ω(u)=e^(iωu)g(u)，N=1，k_ω(a)=H(a)cos(ωa)。

全部实际 primepowers 的 a=log(p^j)≥log2>b，故 k_ω(a)=0：
这族原完整 prime 贡献恰好零，不是删去 prime 或近似。
0<a<b 上 ψ_Cheb(e^a)=0，所以 E(a)=−e^a、A(a)=1−e^a 均为真实精确算术值。

令 q(a)=H′(a)−H(a)/2。真实 absolute 费用精确为

    B_E(f_ω)=2∫_0^b e^(a/2)|−ωH sin(ωa)+q cos(ωa)|da，
    B_A(f_ω)=2∫_0^b(e^(a/2)-e^(-a/2))
                         |−ωH sin(ωa)+q cos(ωa)|da。 (A5)

由 ||x+y|−|x||≤|y|，副项分别造成不超过
2∫e^(a/2)|q| 和 2∫(e^(a/2)−e^(-a/2))|q| 的 fixed-g 有界误差。

这里可给比入口 o(ω) 更强但已付证明的 O(1) 余项：
p(x)=|sin x|−2/π 有零均值、有界周期原函数 P。
任何 W^(1,1)(0,b) 权 φ 满足

    ∫_0^b φ(a)p(ωa)da
      =[φ(a)P(ωa)]_0^b/ω−∫_0^bφ′(a)P(ωa)da/ω
      =O_φ(ω^-1)。                               (A6)

分别取 smooth 权 φ_E=e^(a/2)H、φ_A=(e^(a/2)−e^(-a/2))H。
A5/A6 独立给

    B_E(f_ω)=κ_E ω+O_g(1)，
    κ_E=(4/π)∫_0^b e^(a/2)H(a)da>0，
    B_A(f_ω)=κ_A ω+O_g(1)，
    κ_A=(4/π)∫_0^b(e^(a/2)-e^(-a/2))H(a)da>0。    (A7)

每个误差来自 explicit integral 或有界周期原函数，均不靠采样、N 增长或 ζ 零点。
S5/S7 和 A 版通过；E 起点修成 0 不能挽救这个 absolute 全源费用门。

## 4. 完整 Γ 为 log ω：不同组织的全尾证明

不依赖入口的频尾分割，直接从精确全型 A1 证明。
取 0<r<b。w(a)=1/a+O(1)、H(a)=1+O(a²)，所以
w−1/a 和 wH−1/a 在 (0,r) 可积，w 及 wH 在 (r,∞) 可积。
代入 k_ω，得到

    JΓ(f_ω)=∫_0^r(1−cos(ωa))/a da
             +∫_0^r(w−1/a)da+∫_r∞w da
             −∫_0^r(wH−1/a)cos(ωa)da
             −∫_r∞wH cos(ωa)da。               (A8)

后两个项是 L¹ 系数的 Fourier cosine 响应，趋 0。第一个换元 v=ωa 后，
在 v<1 绝对可积，在 1<v<ωr 分离 log(ωr) 和 Dirichlet 收敛的 ∫cos(v)/v，
于是

    JΓ(f_ω)=log ω+O_g(1)。                       (A9)

A8 是完整 jump energy 的精确重排，保留 0<a<∞ 所有位置，
由 A1 同一性已经包含完整谱尾；没有固定 Ω、截尾错误或半规范。
这独立支付入口 S8 所需的原 norm / whole Γ 比较。

若需要 whole Γ 的更精确常数，可以用
[NIST digamma 渐近及复变量余项](https://dlmf.nist.gov/5.11#E2)
给 Γ(t)=log(|t|/(2π))+O(1/|t|)。F_g 为 Schwartz。
按 s=t−ω，在 |s|≤ω/2 上原积分收敛到 log ω−log(2π)，
其差可由 O((1+|s|)/ω) 的可积矩控制；在 |s|>ω/2，
|Γ(ω+s)−log ω|≤C(1+logω+log(2+|s|))，Schwartz 尾的积分趋 0。
故 actual Γ-form=log ω−log(2π)+o_g(1)，无谱尾遗漏。

## 5. actual graph / pole / bounded 修复不能支付

按原 016，a=log n 的 partial graph energy 为

    E_a(f)=∫_(−L)^(L−a)|f(u+a)−f(u)|²du，
    P_L(f)=Σ_(p^j<e^(2L)) Λ(p^j)/√(p^j) E_(log p^j)(f)。

所有权正确且 fixed L 项数有限。每项 E_a≤4N，故 P_L≤M_L N，M_L<∞。
对本 carrier，因为支持与 prime 移位无重叠，交叉项严格 0，
E_a(f_ω) 只有 |g|² 的 degree 积分，甚至与 ω 无关。
原实际图平方与全 R 平移平方不是同一积分，但二者在 fixed L 均 bounded；
不能利用这一名称差异产生 hidden ω 供给。

2|C(f_ω)|²、2|S(f_ω)|² 均为 compact smooth 加权 g 的 Fourier 系数平方，
Schwartz 下降。因此保 actual positive pole 2|C|²，甚至采用更强预算
2|C|²+2|S|²，都只贡献 O_g(1)。任意 fixed-L bounded 自伴修复 K_L 给
|⟨K_L f_ω,f_ω⟩|≤||K_L||；有限 rank 或 compact 为其子类。

所以对于每个 L>0，任意有限常数 c_L,d_L，均不可能在全部 complex smooth 源上
用 c_L JΓ+d_L N 控制 B_E 或 B_A；加入上述原 positive graph、pole 和
任意 fixed-L bounded 修复、各块任意 fixed-L 有限系数仍失败。
左边 κω+O(1)、右边最多 O_L(logω)。系数、rank、norm 可随成长 L 任意变化，
因为反例是逐个 fixed L，先固定其有限值、再令 ω→∞。
按 reference-energy 归一化后，同一费用仍以 ω/logω 无界，
这不是单纯发现 ||f′|| 大，而是原 Dlog relative-form 消费门失败。

源适应若仅改变 bounded 修复而保持一个 whole-source uniform norm M_L，也同样失败。
源适应若只把 |E(a)| 换成逐源 majorant M_(L,f)(a)≥|E(a)|，而仍用
2∫e^(-a/2)M_(L,f)|k′−k/2| 支付，则新费用逐源至少 B_E，故更不能救费；
A 版的 pointwise majorant 同理。
若修复 norm 按 f_ω 无界增长，或改变允许域/删空间而禁止上述探针，
则离开本定理量词；其新增 norm 或域消费桥必须另付。
不声称任何 source adaptation 都失败。

## 6. signed 原量、端点抵消及 whole Q

prime-free 源有真实

    R_E=−2∫z dE=2∫_0^b e^(a/2)H(a)cos(ωa)da→0，
    2∫E z′=2N+R_E→2，
    2∫A z′=R_E→0。                              (A10)

这是 E(0)=−1 的端点责任。A4 中 −2N 与 E 导数项中的 +2N 精确抵消；
改用 A 时两者同时消失，不能只消掉一项。
2∫z+R_E=4∫cosh(a/2)H(a)cos(ωa)da 正是完整 pole，
它是 full-line even smooth compact 函数的 cosine Fourier 系数，Schwartz 趋 0。
全部实际 prime 项严格 0。因此

    Q_L(f_ω)=Γ-form(f_ω)+pole(f_ω)=logω+O_g(1)>0

于充分大 ω；用上述精确 Γ 渐近亦可写 logω−log(2π)+o_g(1)。
绝对费线性爆炸与 actual signed 导数项 bounded 是不同事实，
不能推完整 Q 负、RH 失败、全 signed 来源不存在或宏观 Goal 完成。
S6/S8 的限定方法边界通过，signed 方向负对照亦通过。

## 7. 有限条件和 H¹ 的准确边界

无需任何有限条件才能否定 whole-source inequality；本审查不能直接引用
539 的有限线性条件负指数论证到这个非线性 absolute fee。
但如下较窄增强可独立证明：任意固定有限 **L² 连续** 线性条件仍失败。

在上面 prime-free 小区间 J 的 smooth 子空间 X=Cc∞(J) 上，
把原条件向量映射 T:X→C^m 的 image 取一个 basis v_1,…,v_r，
每个 v_j 选一个固定 smooth 原像 q_j∈X；这就是其 image 上的固定右逆。
受限恒零或线性相关的条件自然包含在这个 image，不能凭空假设各原条件独立。
每个 L² 连续条件可写成 L² 配对；Riemann–Lebesgue 给 ℓ_j(f_ω)→0。
令 r_ω 为该右逆作用在条件向量上的校正，
其有限 image 坐标均 o(1)。tilde f_ω=f_ω−r_ω 满足全部条件，
且 r_ω→0 于所有 fixed smooth 范数，特别 r_ω=o_(H¹)(1)；所有源仍支持在 J。

correlation 双线性 Cauchy–Schwarz 给

    sup_a |k_(tilde f)(a)−k_f(a)|=o(1)，
    sup_a |k′_(tilde f)(a)−k′_f(a)|=o(ω)。

因此 fixed-L 权积分的 Lipschitz 差为 o(ω)，B_E/ω→κ_E、B_A/ω→κ_A；
||tilde f||²→1。由 JΓ 的正型 Cauchy–Schwarz，
|√JΓ(tilde f)−√JΓ(f)|≤√JΓ(r)=o(1)，
因此 JΓ(tilde f)−JΓ(f)=o(√logω)，故 JΓ(tilde f)∼logω。
修正后仍支持在 J、所有实际 prime 相关仍为零，bounded 参考项仍 O(1)。
最后 norm 归一化不改变边界。这一增强有完整单独证明，不消费 generic finite-condition 口号。

没有在本文件证明任意分布/导数条件或任意 Dlog 连续条件的同一范围；
随源或 ω 改动的 finite-codimension complement 也未被这个 fixed-right-inverse 论证覆盖。
无限维更窄域、只选 special sources、signed 重排与非局部来源保持未排。

H¹ 是实质 escape：本 real g 有
||f′_ω||²=ω²+||g′||²。
在任意 fixed-L H¹ 域，|k′|≤||f′|| ||f||、|k|≤N，
令 M=∫_0^(2L)e^(-a/2)|E(a)|da<∞，则

    B_E(f)≤2M||f′|| ||f||+M N。

A 版同理。因此 H¹-strength 预算可以支付这种费用；
此处排除的是原 whole Dlog/logarithmic reference 门，而不是一切 stronger norm。
不能为通向原 Weil/ζ 的目标免费换成 H¹ 或删除 high carriers。

## 8. 审查判定及消费限制

S1–S8 均通过本文独立推导，且 S7 可在 fixed smooth probe 上给 κω+O(1) 余项。
严格新候选边界为：实际 E/A primitive 的 absolute derivative 消费费，
不能由原 full Γ+finite actual primegraph+positive pole+fixed-L bounded 修复全源支付；
它对每个 L>0 已失败，允许成长系数不挽救，但保 signed 和改变源域仍逃逸。

本文不重新证明世界新颖性，旧 016/237 等的对象差异由原件复核后再结算。
也不声称通过本准入轮即完成成长方法类的宏观门：未付的完整 signed 来源、
联合 full-source growth 预算与同对象 Ξ 识别没有在本证明中得到。
本文件无数值输入、无 ζ 零点、无 producer 或 pending process。

## 9. note541 最终版本消费审查（追加，零新轮）

收到 root 的最终 scope 复核任务后再次完成 AGENTS/README/STATE/check/show/
Goal/frontier/C012/D20261014M 恢复。STATE 当时仍为 C012 ready/cadence3，
root 正准备结算541及cycle10；文件写成不自动完成结算。
现场 HEAD 仍 6309e116e20e886b55a09e0674638b39e4edf349；
工作树有新541和本审查目录，无科学 producer。

只读核验 [541](../../../notes/541-native-chebyshev-variation-and-full-gamma-boundary.md)
的现场 SHA256 为
`fdb316427ecd4cb307e43304c2c8b698d780ab4ac02777faa76adc92292160ae`。
本追加只核该版本，不代 root 修改541、STATE、cadence或Git。

**完整 Γ 的更强余项通过。** 541§4使用 z=5/4+it/2 的 Binet 式和 recurrence：
|u²+z²|≥|Im z²|=5|t|/4，故 remainder 的显式上界为
(8/(5|t|))∫u/(e^(2πu)−1)du=1/(15|t|)。recurrence 的 real reciprocal
为 O(t^-2)，Re log z−log(|t|/2)=O(t^-2)。于是原 Γ(t) 的 O(1/|t|)
误差常数已经有实际供应，而不是仅无误差 asymptotic 标签。

对 μ=|Fg|²/(2π) 的整个 R 积分，在 |s|≤ω/2 上完整付
O((1+|s|)/ω)；在补集上 ω≤2|s|，
|Γ(ω+s)−logω+log(2π)|≤C+2log(2+|s|)。Schwartz μ 的该 weighted tail
为 O_g(1/ω)，包括 t=ω+s 接近 0 的区域及被拆分的 mass。
因此541的 Γ-form=logω−log(2π)+O_g(1/ω) 和相应 JΓ 精确常数通过。
它比本文 A9 所需结果强，并与本文完整 time-jump 的不同组织逆证一致。

**§5 signed 系数通过。** 令 I_ω=∫_0^b e^(a/2)H(a)cos(ωa)da，
则 R_E=2I_ω，2∫E z′=2N+2I_ω，2∫A z′=2I_ω。
现场541两式均写为正确的 2I_ω；本代理只消费这一版本。
若写成 2N+I_ω，将与 R_E 及 Stieltjes 端点不符，不能消费。
正确版本的 −2N/+2N cancellation 和 whole Q 最终正均通过；
完整 pole Schwartz 后，Q=logω−log(2π)+O_g(1/ω) 同样合法。

**bounded / 有限条件 / majorant 量词通过。** 541采用 fixed-L、whole-source
统一有限的 bounded 修复，而非任意 unbounded source energy；rank/norm 可以依 L。
其 finite 条件准确限于固定有限 L² 连续 functionals，image 上 fixed smooth
右逆避免线性相关问题，r_ω=o_(H¹)(1)，支持始终在同一 prime-free J。
因 H¹→JΓ 有界，√JΓ(r_ω)=o(1)，Cauchy 给 JΓ 变化 o(√logω)+o(1)；
correlation derivative cross 项为 o(ω)，norm→1，足够保原 ω/logω 无界 ratio。
这一校正后只保 κω+o(ω)，541没有把未付 O(1) 余项错误移植到校正族。
一般 distribution 条件及任意 Dlog 连续条件未由这个证明覆盖。

按 source 选择的 pointwise majorant 只要仍≥|E|，absolute 费用逐源至少 B_E；
因此不能救支付法。此结论不是所有 source-adaptation 或 joint signed 方法失败。
541明确保留非统一新源能量、域改变、source 分块交叉抵消、signed 响应、H¹
及独立几何逃逸，且不以541本身完成宏观 Goal。

最终判定：541该版本的新增费用命题、全尾误差、signed 系数和修复范围通过。
本追加为同一轮最终消费审查，零新数学轮；完整成长 signed 来源与Ξ识别仍未付。
