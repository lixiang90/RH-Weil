# 原六次幂自由行密度：root 独立全文审查

2026-10-08。基线 2681813154243e10cf4602f4e88514355060d379。
限定 PASS：相对明确的原 sextic squarefree sieve 与标准 primitive
Hecke AFE，认可被审源的全行 raw 计数推导及其范围。
没有认证新的最终行包络、无零边界或简单临界线比例。

全文实读最终
[研究源](hybrid-original-sextic-primitive-zero-density-research-compression.md)，
canonical UTF-8 LF SHA256
74ea809c6aef75638dc2bc115af2b592ff4feb999cd15e35adcfa4319235d52b，
20750 bytes / 407 lines。canonical 仅统一 CRLF/lone CR，不 trim。

root 直接实读只读原 math 的 presentation/ramification、
buffered bins 与 sextic sieve/row-envelope 段落，并核
[BGL 的一手 Corollary 1.6、Lemma 2.1、§5](https://arxiv.org/pdf/1112.1650)。
本审查不把 BGL 的 squarefree corollary 原样应用于全部 sixthfree 行，
不改原 math 或运行其 Lean 工程。

## 1. 实际零点、原行和有限分层

原 X_u 的 above-floor buffered bin 按实际 primitive zero 定义，
所以 bad row 可计入 C(U;a,3I T_1)。这里不需要证明
“large inverse ⇒ zero”；反过来先有 zero，才由原 detector 给 witness。
floor 无该前件，独立保留 #rows≪U。

(u)=s w k 是原唯一理想分解；w 的指数为 2,…,5，k squarefree，
(k,w)=1。固定 w 后 ν(n)χ_n(v)^(±1) 是 fixed column coefficient，
χ_n(k)^(±1) 是实际 varying-row matrix，非单位仍取零。
原 norm annulus 给 q_k≈U/V，powerful w 总数≪V^(1/2)，
实际层 cardinality 为 U V^(−1/2)；都在优化中保留。

S 外每个原局部非平凡 sextic character tame，导子恰含该素理想一次，
fixed ν 不能抵消。故 primitive conductor 的 moving 部分是
q_k rad(w)，而 rad(w)≤V^(1/2)。S 内只作 fixed local types 的有限
分层；root numbers 不被错误称为有限值。原 primitive/natural
coefficient 的差只在 fixed S 内，可用有限分解支付。
physical row multiplicity 的声明也与 fixed orientation 的 j mod 6
局部数据相符，但正文 proof 实际按行求和，不靠错误的去重下界。

## 2. 非 squarefree 列及 uniform AFE

每个 n 唯一为 c d²，c squarefree，允许 c,d 共享素因子。
固定 d 后 ψ_vk(d²) 是模≤1 的 row multiplier。取绝对平方时
保留其自然零值，成为固定 (k,d)=1 restriction；没有把它放进
依赖 k 的 c_n 再调用大筛。大筛作用于 c 的 fixed support 与 coefficient。

未加临界权时三份平方根费用为
sqrt(MB)/q_d、B/q_d²、M^(1/3)B^(5/6)/q_d^(5/3)；
加 q_n^(−1/2) 时为
sqrt M/q_d、sqrt B/q_d²、(MB)^(1/3)/q_d^(5/3)。
fixed-domain ideal count 给第一份仅 logarithm，后两份收敛。
Minkowski 平方后分别得到正文 (6)、(7)，无 moving-mask 额外假设。

AFE 长度 B≈(M rad(w))^(1/2)(1+H)^(d_F/2)，
故第三项 (MB)^(2/3)=M rad(w)^(1/3)(1+H)^(d_F/3)；
原先消息中的 (M²rad(w))^(1/3) 笔误没有进入最终正文。
moving q_k 的 Mellin factor 在每个 fixed Mellin ordinate 下模为
q_k^(eps/2)，其单位相位可提出 row square。dual root number 同样
逐行模1提出。fixed S-supported coefficients 的和用收敛几何级数
Minkowski；其余为原 presentation。gamma-ratio/rapid-tail 的标准
AFE 前件被明确保留，未以大筛单独证明 AFE。

因此 critical second 的三项
M+(M rad(w))^(1/2)+M rad(w)^(1/3)
对 frozen w 一致成立，height power 可统一取 d_F/2。
小临界 mollifier 的列本来 squarefree，系数的 n^(−it) 为 fixed
column phase，所以其大筛界对全实 t 一致，不需 height 截断。

## 3. classical zero-row detector 与全部高度

非 principal 的 L_orig M_X 系数 c_n 在 1<q_n≤X 为零；
Mellin Γ 移线从实部 2 到 1/2−β。z=0 residue 因实际 L_orig(ρ)=0
消失。允许 β=1 时新线仍在 [−1/2,0)，不跨 Γ 的 −1 pole。
原自然 Euler factors 在正实部没有零；没有引入其他 pole 角色。

root 与另一审查者共同指出的 fixed-H Γ 尾现已付清：
最终稿在全实 t 积分，majorant 用距 [−H,H] 的指数衰减，
critical second 用 H'=1+|t| 的任意高度版本。
积分准确付 H(1+H)^(d_F/4+eps)，固定 H=1 也不漏 conductor 尾。
没有假设 fixed C 的 |t|>CH 部分可随 U 消失。

dyadic-polynomial 的 row β 权用 partial summation，row γ 用一维
Sobolev；partial sums 用 binary blocks。每个真正大筛输入都先固定
列 support、coefficient 与 common t，log derivatives 只付小幂。
第一项用 row Cauchy，其余项用正平方计数。于是 (12) 的五项及
高度选择 Y 的显示指数正确。d_F/4−(σ−1/2)d_F/(6−4σ)
=d_F(1−σ)/(3−2σ)，与最后 Y term 的 height exponent 相同。

该新 auxiliary X,Y 仅用于 actual zero count，不作为原 canonical
probe slots，也不改变原 simultaneous witness 的长度。

## 4. 逐层指数的连续核对

设 x=log_U M，原三项的 ℓ(x) 为
max{x,(1+x)/4,(1+5x)/6}，交界 1/7 准确。
加 powerful w 数量后必须再加 (1−x)/2，与实际 cardinality 取 min。

低 σ 的选择 h=x/2、y=(1+3x)/(12r)，r=7/6−σ，
在 x≥1/5 与 r∈[1/3,2/3] 上有 h≤y≤2x。
Type I 与 Y-cross 相等；X-cross、X-first、Y-plain 均不超过该值。
E−g_low x=(5/3−2σ)(1−x)/(12r)≥0，
g_low−(3/2−σ)=−6(σ−1/2)(σ−5/6)/(7−6σ)≥0。
总层 exponent 随 x 增，x=1 给 g_low；x≤1/5 由 cardinality 支付。
这个 proof 覆盖连续 σ,x，不是数值网格推断。

σ=7/8 的三行表含第三段 h 的两支。逐段的 ℓ、max{x,h,2(x+h)/3}
及四项 affine difference 都可在各端点严格核验；
这些是 affine inequalities 的全域证明，而非一般函数抽样。
在 x≤1/15 用 cardinality，在 x≥1/15 用优化层指数；
共同最大为 7/13，height p=6/5。
固定 h,y 的 σ-slope≤2 max y=56/13，因此高 σ safe 界有效，
但没有证明全部高 σ 的最优 BGL g。

## 5. 已付 raw 计数与最终边界的区分

实际 payoff 为原 all-sixthfree raw count：
σ≤5/6 的 g_low，以及 σ>5/6 的 G_safe，
尤其 7/8 处 7/13 优于原 raw 5/8。其分析地位为 [T/R]；
原 sextic sieve、standard AFE、fixed arithmetic data 仍是准确前件。

2D−3P≥0 给原 final R≤(15−16δ)/(15−6δ)。
低段和实际 safe 高段的差均严格为正；高段分子最低 69/2。
所以新 raw 上界直接和原 final bound 取 min，全 above-floor actual
域均不改善。闭 delta=1/50 只作代数比较，floor 的实际 count 保持 U。
这里不同于比较文献 exact g 的另一完整源；实际已付 safe 也已单独核算。

原 row-bin a_*≈0.694 与最高零族 β_* 两层变量始终区分。
再联合 slots/amplification 需要新的 actual moment 或 count，不能相乘
两个独立 upper、机械取幂、删除 masks 或沿不同高度拼数据。
原 472 的 scalar-carrier 桥没有提供这种角色族接口。

没有发现最终正文的数学阻断；限定 PASS。
没有新 final residual upper、simple proportion、无零 boundary、
新论文或原 [R] 整体认证。
