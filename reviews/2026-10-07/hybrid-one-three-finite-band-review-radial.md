# 原 actual13 有限频带准入：独立全文逆审

2026-10-07。审查者 radial_review。

结论：**限定 PASS**。本稿的全高度 finite-word 替换、
physical first-large-jump HS 替换、原离散 P crossing 以及 two-crossing
telescoping 均成立。与已审 physical13 推导结合，严格得到

\[
 \operatorname{Tr}(C_HC_L^3)=o(d),\qquad
 4\operatorname{Tr}(C_HC_L^3)=o(d).
\]

这是实际原 finite matrix 的 whole13 sector，包括所有重复及全异
genuine-prime 标签、所有 signs、四 placements 和原 carrier。
没有得到31、distinct22、完整四阶常数、更高零点比例或新的无零界。

## 1. 被审版本与引用范围

SHA-256 均对 UTF-8 内容作 CRLF/lone CR→LF 规范化后计算。

| 证据对象 | canonical LF SHA-256 |
|---|---|
| hybrid-one-three-finite-band-admission-research.md | bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f |
| hybrid-signed-one-three-physical-resonance-research.md | 0f7c0146e984c49d84fc057394aed1ab9ace658ae5b775b931bfd359a4c47bac |
| hybrid-signed-one-three-physical-review-radial.md | 222dafcd9bfefcb8dc6934208e866407a1173700ff96d97995a4ce5c658b71e6 |
| notes/446-uniform-prime-twists-on-the-original-gabor-frame.md | 08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf |
| pinned OpenAI/math September-30-2026/build/paper.tex | 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 |

被审稿 10,800 canonical bytes、274 行，与本报告在同一 reviews 目录。
本次从头完整逆审这个新证据对象，未以此前 physical13 审查代替。
物理稿的 near、long triples、全部 alias 和 joint Fourier ghost 证明
已经在表中所列独审逐项核准；本次核对它与新桥接的准确衔接。

分析输入 [R] 仅为446所用的固定 θ<9/10 的 zeta 无零输入、
fixed-gap logarithmic control 和相应 uniform sharp Λ Perron；
取 θ=7/8、a=89/100 已充分。其来源仍是固定提交
adc7f1241b42e322a6451854ab7e4b4c146bf78a。
没有独立认证外部原 math 全稿，也没有假定 unknown full prime fourth norm。
不使用任意 moving coefficients 的 canonical cancellation。

没有修改被审稿、旧文件、math、脚本、输出或 Git；本次不是有限
数值模型审计。

## 2. 乘子正规化与 good band

unitary Fourier 下，R_s 的乘子是 e^{its}。
所以原 -b_pM_φ(R_{log p}+R_{−log p})M_φ 精确对应

\[
 D_R(t)=-[Q_R(t)+Q_R(-t)]/(a_LL).
\]

没有遗漏2π、a_L或L。D_R 实、偶；截为 J=[T/2,3T] 后虽不再偶，
D_R^g 仍实，因此 B_R^g selfadjoint，后文两次 crossing 可使用。

Chebyshev 在全 height 给 m_H≪√X/L、m_L≪√Z/L。
sharp Perron 仅在 J 和 −J 上调用；其 principal residue仍保留，
pointwise proper-power difference也仍保留。故
q_H≪X^{a−1/2}L、q_L≪Z^{a−1/2}L。
∥M_φ∥≤1 给 ∥B_R^g∥≤q_R，这是全 Hilbert space 的 op 界，
不是仅有限 matrix 上的界。

J 是用于估计的 Fourier multiplier band。它不是原离散 P，
也没有在后续把 P 换成连续频率投影。

## 3. 全高度 finite matrix 的替换

F_0=F M_φ E 的列为 (2πL)^{-1/2}hatφ(t−τ_k)。
unitary F、∥M_φ∥≤1、E isometry 给 ∥F_0∥≤1、
∥F_0∥_2≤√d。

所有 τ_k∈[T,2T)，距 J^c 至少T/2。原二阶 Fourier 尾给

\[
 \|1_{J^c}F_0\|_2^2
 \ll (d/L)T^{-3}\ll T^{-2}.
\]

1/L 必须来自原 E 正规化；本文保留了它。
所以 C_R−C_R^g=F_0^*D_R1_{J^c}F_0 的 HS 范数≤Cm_R/T。

对 finite 四词逐个替换，误差因子用这个 HS 界，
剩余三因子用一个 finite-dimensional HS 界和 op 界，
费用≤C√d m_Hm_L³/T。每个 placement 同样成立。
normalized 费用恰为 X^{-1/4}L^{-9/2}，趋于0。
本步对 bad heights 只用 m_R，不错误延用高 height 的 q_R。

## 4. physical 全高度替换：first-large-jump 准入

physical 四词的 Fourier 形式
F_0^*D_1 K D_2 K D_3 K D_4F_0
精确，其中 K=F M_{φ²}F^{-1}。
三份内部 φ² 的 convolution 与两端 φ packet 均保留。

原 C² 界给 |hatφ²(v)|≪|v|^{-2}。
far convolution |v|>ηT 的 L1 尾≤C/T，故
∥K_far∥≤C/T；同时

\[
 \|K_{\rm far}1_{J'}\|_2^2
 \ll |J'|\int_{|v|>\eta T}|v|^{-4}\,dv
 \ll T^{-2}
\]

对长度O(T)的 J' 一致。其 HS 界为T^{-1}，不能只用 op 尾。
K 本身 op≤1，因此 K_near op≤2。J_0 外侧 F_0 的 HS 同样≤C/T。

从右端 input 1_{J_0}F_0 开始，三个 near jumps 至多扩张3ηT。
J_0=[.9T,2.1T]、η=.01 给所有 multiplier heights在
[.87T,2.13T]⊂J。all-near 子词中 D_R 改成 D_R^g 精确不变。

其余七个子词中，取从右数第一个 far。它右方每个 near convolution
和 diagonal D 都只把 input 保持在某个固定长度O(T)的 J'；
因此可实际插入1_{J'}并使用 K_far1_{J'} 的 HS 界。
右方包括 F_0 的其余 factors 只用 op≤1或相应 m_R；
左端 F_0^* 使用 HS≤√d。每词的 trace 因而
≤C√d T^{-1}∏m_R，正是(12)。

右 input 1_{J_0^c}F_0 用HS≤C/T给同一费用。
raw/good 两组使用同一 decomposition，all-near 子词相消。
没有假定任何 prime phase 独立，也没有删掉远低绝对 height。
每个物理四词都能严格返回同一 good band，normalized 误差为
X^{-1/4}L^{-9/2}；whole fourth moment不是此证明的前件。

## 5. 原离散 P 的准确 crossing

B_R^g 的输出仍支撑I，故 Q B_R^gP 的 relevant 部分完全在L²(I)。
{L^{-1/2}1_Ie^{iτ_ju}}_{j∈Z} 是I上的完整正交基：
共同 carrier e^{iTu} 只是unitary调制。
因此 Q 正是其中 j∉[0,d−1]的补集；I^c分量为0。

用真实基底计算 B_R^g 的 jk 项，得到(13)的
(2πL)^{-1} integral。n=j−k>0 时上侧 outside pairs数为min(d,n)；
n<0时下侧数为min(d,|n|)。两者逐n合计准确为min(d,|n|)，
没有多计两个边界或遗漏 finite floor。

对 ν=Lξ/(2π)，|n|≤|n−ν|+|ν|。
unweighted shifted-grid square sum由 hatφ 的原界控制为O(L²)；
也可由I上 Fourier Parseval直接得到这个界。
加权部分最近格点为O(1)，1至O(L)距离的中间层产生logL，
更远层用二阶尾后可和为O(1)。因此

\[
 W_L(\xi)\ll\ell_0+L|\xi|
\]

uniform 于任意实ξ，包括ν任意接近整数；并未把ξ视为离散频率。

在 jk 向量空间中使用 Minkowski，D_R^g(τ_k+ξ) 虽依赖k，
其模一致≤q_R，所以得到(16)首行。
∫|hatφ|≤C ell_0，且
∫|ξ|^{1/2}|hatφ(ξ)|dξ≤C：
分别在0到1/L、1/L到1、1到∞使用
min(L,C/|ξ|,C/ξ²)即可。
故 l_R^g≤Cq_R√L。sharp J没有引入 derivative fee，
因为这里只使用实际 global sup。

这条估计始终针对原 P=EE^*，没有连续投影替换。

## 6. 两次 crossing 的六对项

selfadjoint V_i 的 off-diagonal 两块互为共轭，故
∥[P,V_i]∥_2=√2 l_i。
product commutator 给(18)，并且每个相关 trace 都因finite-rank P准入。

准确 telescoping的第一项配 l_1 与右 triple的crossing，
得到 (1,2)、(1,3)、(1,4) 三对。
第二项左 HS≤y_1l_2、右为两个因子的 crossing，
得到 (2,3)、(2,4) 两对。
第三项左≤y_1y_2l_3、右 l_4，给 (3,4)。
因此 (19) 确实是六个两次 crossing 项；没有只付一次 crossing 就
以剩余 physical op 填补整个误差。

good operators 的 y_R≤q_R、l_R≤Cq_R√L给
|Δ|≤CLq_Hq_L³。除d并保留各q的L费用，得到

\[
 d^{-1}|\Delta|\ll
 X^{(5/2)a-9/4}L^4.
\]

a=.89时为X^{-1/40}L^4=o(1)。
不需要 commutativity、small op commutator或未知 full fourth。

## 7. 实际 whole13 的闭合及范围

衔接顺序无循环：

1. 已审物理稿独立支付原 full-height physical13 每个 placement 为 o(d)。
2. first-large-jump 比较给 good physical13 同样 o(d)。
3. 两次 crossing 给 good actual compressed 词相差 o(d)。
4. finite packet 尾给原 actual 词再相差 o(d)。

因此原 Tr(C_HC_L³)=o(d)。只有有限 matrix 中才用迹循环，
得到四个placements合计4Tr(C_HC_L³)=o(d)。
N(T,2T)与d仅使用ratio→1，不采用更强且未付的d=N+O(L)。

所有profiles和fixed gap a−θ先固定，height范围、prime labels、
carrier和placement均统一；再令T→∞。quoted [R]没有扩大成
“原math全部kernel已经认证”。

31的相同crossing费用仍是
X^{(7/2)a−11/4}polylog，且其physicalnearproduct可达XZ。
distinct22与高全异signedsector也没有随本桥接自动闭合。
本次限定PASS验收的是实际整个13小量，不形成完整四阶常数，
不登记更高简单临界线比例或新无零区域。

## 8. 461 综合笔记的独立全文审查

2026-10-07 追加。完整从第1行至文末独立读取
notes/461-original-one-high-three-low-fourth-trace.md，并核对其全部定义、
两个 bridge 的衔接、一般 θ 的量词及(11)的四次展开。
本节没有以此前两份研究报告已经通过替代对综合稿的审查。
最终194行稿已经全文复读，**限定 PASS**，canonical LF SHA-256 为
f9fdf0b721c76a5cc4c4e4821748007e62975286417e6bec9700e39b6778170b，
6,799 canonical bytes。原 13/31 矩阵定义来源仍为
hybrid-one-three-mixed-prime-sector-research.md，canonical SHA-256
5db2c614ab9d009a15a70f4e0639b95df2d59a6b56bd752216537fcf71e2b405。

461(1)–(2) 与原 13/31 报告同一 finite matrix 完全一致：
unitary E、d=floor(XL)、原 carrier τ_k、实线零延拓、
genuine-prime sharp low/high split 以及(a_L L)^{-1}正规化均未改变。
phi 和 phi² 的统一 C² 导数前件与已审 physical/band 证明匹配。
quoted [R] 只用 conductor-one zeta 的无零和 fixed-gap control；
没有将整个外部 kernel 重新认证，也没有使用 full fourth moment。

定理一般 θ<9/10 时，应先选择固定 θ<a<9/10。
bridge 的 normalized power 是 X^{(5/2)a−9/4}L^4=o(1)；
X^{-1/40}L^4 是原 θ=7/8 可取 a=89/100 的具体实例。
独审指出的这个量词澄清已在最终§1和§4采纳；
最终稿没有把一般 θ<9/10 都宣称具有这个固定 power。
§2 的 physical coefficients/Hilbert/alias/ghost 范围与已审稿一致。
§3 原离散 crossing 与§4 两次 crossing、first-large-jump HS
保留的是同一个 P；没有连续投影或 free trace cyclicity。

对 §5 最终展开另作完整 finite algebra 核对。
令 H=C_H、L_0=C_L，为原有限 selfadjoint 矩阵，置
A=Tr(H²L_0²)=∥HL_0∥_HS²、B=Tr(HL_0HL_0)。
十六个有限 word 按循环迹准确归并为

\[
 \operatorname{Tr}(H+L_0)^4
 =\operatorname{Tr}H^4+\operatorname{Tr}L_0^4
 +4\operatorname{Tr}(H^3L_0)
 +4\operatorname{Tr}(HL_0^3)+4A+2B .
\]

两高两低的六个 words 中，四个属于 adjacent class A，
两个属于 alternating class B；没有把非交换因子作交换。
commutator skewadjoint 给

\[
 \|[H,L_0]\|_{\rm HS}^2=2A-2B,\qquad
 4A+2B=6A-\|[H,L_0]\|_{\rm HS}^2 .
\]

因此先有不含任何余项的 exact finite identity，
再使用已经支付的4Tr(HL_0³)=o(d)，严格得到461(11)。
其 commutator 负号和 coefficient6 均正确；
displayed o(d)只替代已付13，不是从未知 full C4 upper bound 得来。

剩余31、22 product norm及commutator、高全异、完整背景与
proper powers的同对象预算没有由该展开自动支付。
§5未把 repeated 常数与 low 一侧上界相加成全四矩；
459的另一个无零 mixed-saving合同也未从13自动取得。
有限矩阵 trace 和d/N→1的量词范围保留。
