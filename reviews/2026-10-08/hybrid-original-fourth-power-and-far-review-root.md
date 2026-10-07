# 原四阶增长幂、完整远共振与主质量扣除：root 全文独审

2026-10-08。基线 46106dc449ac7e6d91a3646b09e63b0b0e272cc1。
本稿是不同作者的完整数学审查，不是有限脚本输出代替解析证明。
canonical UTF-8 LF 只统一 CRLF/lone CR，不 trim 或改变 EOF。

| 全文读取的冻结作者源 | canonical LF SHA256 |
|---|---|
| [零点包四阶幂源](hybrid-positive-height-zero-packet-fourth-upper-research-radial.md) | 8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481 |
| [完整远共振源](hybrid-whole-ratio-smooth-carrier-far-resonance-research-twisted.md) | 9b8c6064731f65eb4449a3e9da353077baa856a4cb27f93fd5063b6f6a578054 |
| [原半素数主质量源](hybrid-canonical-semiprime-smooth-subtraction-and-variance-obstruction-research-compression.md) | 7fcb097ad17d77b7281acd1f7c7d0f1580c5519c015437e104823cdfabd52645 |

审查结论：三源在其明确范围内通过。实际新结果是有条件的四阶增长幂改进、
合法短载体平均下的完整远共振小量，以及连续主质量的 additive 扣除。
没有得到有用的常数四阶预算、实际新零点比例或无零边界。

## 1. combined twisted Perron 的端点、极点和全部尾

根节点逐行读取 radial 的 332 行源，另核 Guth–Maynard 原研究论文
(1.2)–(1.3) 的 Ingham/Huxley 密度公式，以及 Fesenko–Ricotta–Suzuki
Appendix A 的 local logarithmic derivative 证明。正文所用均是 ζ 本身，
不涉及把 sextic Hecke rows 映成原 n^(it) 列。

半整数 x=floor X+1/2、y=floor sqrt X+1/2 保持原整数 cutoffs：
无论 X 的小数部分多少，二者的整数前缀均与原集合相同。
F=(x^z−y^z)/z 在 z=0 整个，故两 prefix 必须在移线前合并。
这只消除了 Perron 核的人造极点；若 s0=1/2−it 本身为 ζ 零点，
D(s0+z) 的真实 pole 仍给 −mρ F(0)。作者准确保留了该项。

原 t∈[T/4,4T] 的每行可各选 H_t∈[10T,11T]，同时避开两横边的
零点 ordinates。全部不良 H 的 O(T log T) 个小区间，总长度为
O(c1 T)，先固定足够小 c1 即可。没有要求一个固定 H 适用于所有 t。
横边 ζ 高度均为常数倍 T，local partial fraction 给 O(log² T)。
左线 Re(s0+z)=−1 无零，且不跨越 trivial zeros −2,−4,…。
直接 twisted 截断误差的系数模与 t 无关；端点 harmonic sum 给
O(sqrt X log² X/H_t)，在 H_t≈T≈X 时为 O(X^(−1/2)log² X)。
这里没有 Abel 分部积分带来的另一个 t 因子。

左边完整积分付 O(X^(−3/4)log² X)，横边付 O(X^(−1/2)log² X)。
ζ 的 s=1 residue F(1/2+it) 在原正高度窗亦为 O(X^(−1/2))。
跨越的所有非平凡零点均在 |γ|≤16T，包括正负高度及重数。
扩大到该全集发生在取绝对值之后，故不需要 H_t 的可测选择。

## 2. 零点包 Jensen 的 log 费用与连续实部

由 F 的积分表达式与分式表达式同时得
|F(a+iv)|≪X^(a_+) ell/(1+ell|v|)。这是在 a=v=0 仍合法的界。
unit 零点个数 O(ell)，故 near |v|≤1 的权和 O(ell²)，其余
harmonic tails 亦 O(ell²)。单个权在整个 J2 上的积分 O(ell)。
加权 Jensen 的三次权和花 ell^6，单个积分花 ell，再除以原
(a_ell ell)^4，准确留下 ell³/T 乘零点实部权和。
这核对了作者的 log³，而不是遗漏 harmonic tail 后误报的幂。
若用较粗 normalized 核 1/(1+|v|)，会留下 log^7；不能混用两核。

低实部层的指数为
4σ−3+3(1−σ)/(2−σ)，高层为
4σ−3+3(1−σ)/(3σ−1)。前者在 [1/2,3/4]、后者在 [3/4,θ]
严格增加，两者接点为 3/5。固定有限 σ 网格后才令 T 增大，
避免假设 moving σ 的密度常数一致。最大值恰为

\[
 B(\theta)=4\theta-3+\frac{3(1-\theta)}{3\theta-1}.
\]

θ=7/8 给 19/26，较 446 的 3/4 严格省 1/52；一般 gap 为
(1−θ)(6θ−5)/(3θ−1)，在 5/6<θ≤7/8 为正。
474 已付 proper-power L4 norm 差后，用 Minkowski 传回 genuine primes。
没有在未知四阶增长时声称两个四矩相差 additive o(1)。
结论相对明确的 ζ strip [Rθ]；它没有独立验证原 strip 证明本身。

radial §7 的 local Nikolskii 推论是一侧上界。零点包 Jensen 不能反向，
所以作者没有据 bounded fourth 免费断言 3/4 无零，有限低高度例外
也不被 diagonal height/length 渐近预算自动排除。此范围准确。

## 3. 固定正光滑载体与完整远区

根节点逐行读取 twisted 的 359 行源。a_n=1/[4n(n+1)] 的总宽 1/4，
中心 1/2 给 support [3/8,5/8]；第一因子长度 1/8 给密度∞范数≤8。
每个固定阶 m 先保留 k>m+1 个 sinc 因子，所得可积 Fourier majorant
对所有 N≥k 成立。Fourier inversion 的 dominated convergence 因此
同时给 C^m 收敛、正性与总积分一，而非只定义一个形式 infinite product。

|z|≥256 时 N0=floor(sqrt|z|/8)≥sqrt|z|/16，n≤N0 的每个参数
|z|/[8n(n+1)]≥4，故每个 sinc≤1/4。所有其余因子≤1，严格得
|Γχ(z)|≤exp(−sqrt|z|/16)。选 Δ=1024ell^(5/2)/X、s=T/sqrt ell
即有 sΔ=2048πell²≥4096ell²，故整个 |S|≥Δ 的核≤X^(−4)。
原全标签系数质量 m_H^4≪X²/ell^4，由此整体远区 O(X^(−2)ell^(−4))。
原 φ 只需 C²；新的光滑性属于合法载体起点的概率密度。

同一个 u 的两个 half-ratio 项输出 v,v' 均在 I_+，真实 S=v−v'
满足 |S|≤ell/2。这里没有 ratio 按 ell 取模，也没有物理周期化。
更强的是 actual atom 的准确调制
C_(p,ε)(σ)=exp(iσεlog p) Ctilde_(p,ε)。四个 actual 压缩相乘时
三个内部 P 原样保留，σ 相位只是 exp(iσΣ εlog p)。归一化 trace
绝对值≤operator norm≤Π b_p，故所有有序 H/L words、signs、
repeated 与 four-distinct 标签的任意 σ-independent 子集均可整体付款。
有限求和的 hard far gate 不需另作 Fourier 展开，没有未付 gate 尾。

χ∞≤8 继承 472 的 whole-word mean absolute P error 和共同 good set，
选择起点仍在 [T,T+s]，与原 moving zero block 合同兼容。
作者在可能增长的预算上保留 good-set probability 分母，这是必要的。
不能把整个 word 的 P 误差逐 tuple 分给 near 标签。

真正 |S|≈1/X 时 sS→0，Γχ→1；因此未付 near 仍保留原 signed phases、
长度 X² 和 determinant 宽度 O(Xell^(5/2))。远区小量本身不给 whole upper。

## 4. 半素数连续主项与真实 centered variance

根节点逐行读取 compression 的 212 行源。两 factor 的普通 dx density
作乘法卷积准确给 triangular ρ_X；Fubini 的 Mellin transform 等于
V_X(t)^2。没有把离散 ρ_X(n) 多项式当成连续积分。
在 J2，V_X²=O(X^(−1))，而 raw Q_X=O(X)。所以减去主项后
| |Q|²−|Q−V²|² |≪1，正规化的四阶差真实为 O(ell^(−4))，
无需任何未知的四阶有界前件。

compact signed measure 的 log 变量连续部分为 e^(y/2)ρ(e^y)dy，
与 x^(−1/2)dx 完全相符。t0=17T/8、B=15T/8 精确覆盖 J2；
triangle kernel 的 transform δ sinc²(vδ/2) 在 |v|≤B 下界为 cδ。
整轴 Plancherel 因而直接证明作者用于 atom-minus-density 的 Gallagher 步骤。

实际 chirp weight 在长度 δ=1/T 的 log 窗中花 t0δ=O(1) 的 variation，
连同 triangle derivative，完整 BV 范数为 O(x^(−1/2))。
Stieltjes 分部积分正确要求所有 prefix 的最大 discrepancy。
得到的 weighted maximal variance ≪ell^4/T 只是充分预算，尚未支付，
不能从 ordinary count 或另一个中心的 Selberg variance 免费推出。
top product scale X² 需要所有大 factor 的联合相消；作者记录的 Cauchy
费用 X^4ell 与目标 X^3ell^4 是方法成本的对比，不是实际方差下界。
其 Coppola 的 real-g、support 和 Wintner-center 范围审计也没有声称
排除其他 signed 方法。弱 unconditional log-saving 比原 strip 上界差，
作者准确避免把它列为新 best upper。

## 5. 结论范围

以上完整解析审查支持各自新付款。待 notes/475 将这些结果合并时，
应把零点包的实际 B(θ) 上界与 fixed-start sampling 的单侧准入连接，
而把 near signed arithmetic 和 maximal centered variance 留为开放输入。
不得宣称新比例、无零边界、常数四阶预算或新边界论文已经完成。
