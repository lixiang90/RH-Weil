# entire-high 正尾与两个 parity Gram 的独立核验

2026-10-08。审查者 root；只审其他作者的完整新推导。
结论：下列准确对象及前件范围内限定 PASS。
这不是独立认证既定 [R] 分析内核，也不是证明新的实际比例或无零区域。

| 全文审查对象 | canonical UTF-8 LF SHA-256 |
| --- | --- |
| [compression 的 whole 正尾 gap](hybrid-positive-tail-whole-high-parity-gap-research-compression.md) | 568f2c80d9773db7c13bc3605e7d56ed032e3fba7f5d4dc7c34bbea5ac7cb611 |
| [radial 的 split Gram 与真实 even tail](hybrid-parity-split-schur-and-even-anticommutator-research-radial.md) | b9fff88ede3374b488dccddf9cfea3f92f386e98594c385dda51ce210b784d20 |

canonical 只将 CRLF、lone CR 转 LF，保留其他全部字节与 EOF。
两份均全文读完；radial 最终纯文字修正点名两份旧13输入，
避免新增两个无 [R] 的源被“最后两项”误指。其余数学与先前全文版本相同。
root 自己的 whole-low 源不计为本审查的独立对象。

## 1. whole 正尾 gap

逐域独立代数核验 u=|x|、v=|y|：
两者≤R 时 clip 差及 tail 都为零，余项 R²(u−v)²；
一者≥R 时准确余项 (uv−R²)²；两者≥R 也为同一平方。
边界两式一致。使用 (x+y)²≥(u−v)²的方向正确。

H 特征基中 |U_ij|²为双随机矩阵；
两 scalar tails 各求和为 τD_R，最后平方项准确为
||H+UHU||2,d²。没有把 U 换成 J。
Γ gap 扣除的准确 cross 是 −2τ(WUD_RU)；
D_R≥0、0≤W≤MI给其下界 −2MτD_R，无需 W,H 交换。

sharp finite commutator 界 q_R≥K_R/(4M) 是冻结 466 的通用 finite
代数，适用于 clip_R(H)。三角 inequality 付
sqrt K_R≥(sqrt K−2M sqrt(τD_R))_+，scalar distance-square≤tail 正确。

令 c=2(R²−M)>0、z=sqrt(τD_R)。
在 z≤sqrt K/(2M) 区间，一元 quadratic 的极小点
z=sqrt K/[2(M+c)]，值 Kc/[4M(M+c)]；
其余半轴 cz²的最小值更大。K=0 单独直接成立。
此消元保留正 tail 成本，因而完全不需要 τH⁴或 q 增长前件。

最终 finite 式每个 R 常数显式，R²=ell 时
alpha=O(1/ell)、omega=O(sqrt(log d/d))使全部误差趋零。
fixed R、T、最后 R 的替代极限也合法，未知 tail 已被代数消元。
所以 liminf(q_e−q_o)≥41/15120 是整个实际矩阵的新必要约束，
无 [R]、无 q 有界、无 a=o(ell²) 前件。

独立重算 conditional Q=1/350 时的 r≤11/151200、
covariance root sum A=4631/72576000、B=143/72576000；
h=47/5000 的两正余量分别
365807/16200000000、155910001/22325625000000000000。
原 q 上界本身仍未付款。

## 2. marked13 的完整分析域与 sharp 恢复

先固定 C² marks 时，physical prime translations 仍恰 four；
节点并窗的 joint Fourier 只增加固定 log 因子，
近共振的实际 composite energies、spacing、exact-label multiplicities不变。
entire far 的真实 overlap及 ±ell alias payment保留。
canonical middle-far 主幂是 (5/2)a−9/4，固定 a<9/10足够。
坏 ghost 用真实 C² tail O(1/T)，原 raw mass X^(5/4)、
归一化 endpoint kernel 1/d，费用为 X^−3/4 times log powers。

带内 operators 双向 crossing 是 O(sqrt ell q_i)；
standalone smooth mark 端点不同，真实 round-circle leakage可能
O(sqrt log d)，稿中保留该项。closed finite word 至少两 crossing，
费用 ell q_H q_L³/d 与 physical 主幂相同。
raw/good 恢复保持 first-large-jump HS 与外 packet tails，
新增固定数 marks 只改变固定 guards 和 log powers。
不能从这些参数推广至移动 arithmetic coefficient 或自由两侧 joint cancellation。

sharp 只恢复稿中两个目标 six-factor词。
每个 U−S_epsilon 都直接邻接一个 L；DL 的 S4 小量通过
Tr D²L²D²L²≤Tr D⁴L⁴与已付 whole-low strip 得到。
其余三个 Schatten factors 是 H,L,L。
只有这一步明确需要 q=O(1)，使 H4 bounded；原低四矩无此前件。
先 epsilon 固定、T、最后 epsilon 的量词完整。
V 标记用 UVU−V 的 HS 小量及 HL 的 bounded HS；
因此 Δ⊥UZU 确实新付款，两个 parity 分量正交不能只由总正交拆分。
这一13付款仍相对于既定 conductor-one [R]，未将其假设改成已证明事实。

## 3. finite 双 Gram、high even 尾与 Z_even

两份 3×3 Gram PSD 的 Schur 补包含全部 finite centering errors。
delta_j=0 的退化分支列明。共同有界子列后才删除 errors；
p_e+p_o=c−C、z_e+z_o=c−k/4 与原 finite algebra一致。
F=τ(H+L)⁴ 的 6c−k 系数由循环展开核准。

新增 even-tail proof 保留 T_R=H−H_R：
本节 finite 域明确 R²>M_T；渐近时先固定 T0、R，
使 R²>sup_(T≥T0)M_T，再按正文两级极限。最终补域不改变推导。
parity Jensen (E T_R)²≤E(T_R²)≤E D_R；
PSD trace-square monotonicity无需两个矩阵交换。
core/tail cross≥−e_R sqrt q，因为总 TrΓ_RD_R≥0，
odd cross才允许负。有限 q_e展开故给
||E T_R||4,d⁴≤q_e−q_R+e_R²+2e_R sqrt q。
fixed clip 的 even S4→0及 bounded-q后 R→∞，
推出 ||H_e||4,d⁴ limsup≤q_e−41/15120。
这保留未知高四阶尾，没有将二阶 smallness 升级为免费四阶 smallness。

L_o²准确 U-even，Tr H_e²L_o²≥0；
mixed even/odd H 交项迹准确零。因此主要的 odd-odd anticommutator
HS norm 可用 τH²L_o²控制。
原 root 的完整 low source supplies 1/60、19/1920、1/120；
centered Γ 的 V_o 测试已付。由 parity HS Cauchy及 even-even S4
费用得稿中 (23)。此项不是零，也不是仅取重复 prime 主项。

## 4. 全连续 certificate 及结果范围

逐个重算 (24)–(28) 的纯有理余量：
两个 root upper 给 z_e<13/500。
取 t_e=16/3、t_o=31，将两个 b_j 各做 Young；
z_o=c−k/4−z_e 后 z_e系数为正，r系数也为正。
扩大到旧未付 Q、rbar、z_e cap 的方向均正确。
两个 real p_j 完成平方覆盖整个连续可行域，无有限网格替代。

精确总常数 U=25710335933/77218272000，
1/3−U=29088067/77218272000>0；
k 系数 63/62 正确。
复用旧 k≥1/40 时 U−63/2480<77/250 的余量
34485043/77218272000>0。
这份证书不证明 Q 上界，也不保证所有实际 transition 条件可行。
Q-only 证书只条件地超过 flat 2/3，不自动超过当前 .672509329。

本轮有真正 whole 必要约束及完整 analytic reductions；
仍未得到新的实际比例、无零边界或 RH 结论。
本轮随后 470 用已付中心化严格排除 Q=1/350。
这里已核的 Q-forward 公式因而仅为该不可达前件下的反事实蕴含。
