# 原 high 半区间 Gram 与有限 parity：独立全文审查

2026-10-07。审查人 twisted_research。限定 PASS。
本报告独立核验实际算子、有限迹、原载波和每个比较步骤；
没有修改被审稿、冻结笔记、math、脚本、输出或 Git。

## 1. 最终被审对象与范围

被审稿：[radial 原稿](hybrid-high-parity-gram-and-mobius-completion-research-radial.md)。
canonical LF SHA-256：
3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2。
磁盘 UTF-8 原字节 11380，283 行。归一化只把 CRLF 和 lone CR 改为 LF，
不删尾空白或最后换行。

全文七节均重新核验。另实读原 high 四词报告的泄漏与 T0 推导、
[454](../../notes/454-original-background-and-weighted-prime-mixed-traces.md)
加权物理二矩、
[462](../../notes/462-original-low-prime-fourth-path-constant.md)、
[463](../../notes/463-two-sided-height-stability-for-original-fourth-words.md)。
结论只覆盖原稿明确声称的 Gram、cross trace、有限谱对称和卷积恒等式。
不认证完整 high 四矩有界、比例改进、独立于 [R] 的新无零区域或 Lean。

## 2. 半区间结构与 physical Gram

R_s f(u)=f(u+s) 且区间外零延拓。每个 high 步长严格大于 L/2，
所以正平移的 output 在负半区、input 在正半区。
因此 physical A=Π_- A Π_+，A²=(A*)²=0；这一步没有作用于
E*AE 的平方。由原偶 φ 和实系数，空间反射把 A 变成 A*。

反射把每个 Ee_k 变成其复共轭，而 G=A*A 为 real selfadjoint。
因而两个 physical block 的有限压缩迹相等，严格得到
Φ_H=2||GE||HS²。这里是作用于有限 d 个向量的范数，
没有把 E*B_H⁴E 的迹当成 whole Hilbert trace。

原稿 (7) 中右平移 log(q/p)、两个 endpoint φ 及共享
φ(u−log p)² 全部正确。令 z=u−log p 后，(8) 的 p-only、
q-only 两因子准确恢复；未把未分离的端点窗免费送入 Hilbert。

## 3. Signed cross 的 O(1/L) 付款

high log frequencies 跨度小于 L/2。因此原 finite csc 几何核没有
±L 的 alias，两个 numerator exponentials 的相位均可保留在系数中。
局部间距 δ_p≥1/(2p)，weighted Hilbert 的双线性版本可由复极化获得。
uniform 于 z 的两向量系数范数给

L/d Σ_p p b_p² + d⁻¹(Σ_p b_p)² = O(1/L)。

两因子不必相同。共享 φ(z)² 的积分除以 L 有界，因此这个预算
确实支付复 cross trace，而非仅估计对角或丢 carrier 的无限 sinc。
D_L 支撑正半区，两个反射 diagonal 不交，故 (10) 的因子 2 正确。
展开 Gram 后 (11) 是 Sψ+2||RE||HS²/d+o(1)，error 不含未知第四矩。

flat 的 S1=19/480 与旧 repeated union 2S1=19/240 是不同对象。
原稿明确没有把 repeated union 当 whole fourth limit，范围正确。

## 4. Actual Γ 与内部 P

令 K=(QB_HE)*(QB_HE)，则
C_H²−Dhat=E*(R+J_ref R J_ref)E−K。
K≥0 且 TrK=o(d)，但 TrK² 未付；原稿保留了这个区别。

原 high 报告的 T0 比较确实先只用：
bounded multiplication 泄漏 O(log(2L))、
||B_H||op≪√X/L、
||QB_HE||HS²≪X log(2L)/L²=o(d)。
将 Σ C_p² 换成 Dhat，以及把有限 weighted two-word 换成 physical
weighted two-word，误差均为 O(X log(2L)/L²)=o(d)。
不需 TrC_H⁴=O(d)。Dhat² 的有限 Toeplitz 比较只花 O(log(2L))。

因此 (15) 两个极限成立，有限平方展开严格推出

TrC_H⁴/d=Sψ+||C_H²−Dhat||HS²/d+o(1)。

这里是 actual 正 residual 恒等式。不能由 K≥0 推出两个不交换
平方的排序，也不能从 actual residual bounded 倒推 physical R bounded。
原稿没有作这两项非法推论。

## 5. 原有限载波上的 parity

sign(u) 的 Fourier 系数在 odd n 为 2/(π|n|)，其余为零。
跨有限 carrier 的计数是 min(d,|n|)，因此 Tr(I−S²)=O(log(2d))。
内部 P 给出的 anticommutator 恰是 (18) 的两个 Q crossing。

U=sgn S 在零特征值选 +1 时仍为 Hermitian involution，
||U−S||HS²≤Tr(I−S²)。由 raw high op 界，
||C_H+UC_HU||HS²/d=O(L⁻²) 正确；它不是 P 与 sign 相交换的模型。
Hoffman–Wielandt 应用于 C_H 和 −UC_HU，给排序谱反射的二范数界。
该界不控制第四次方稀疏 tails，原稿明确保留未付范围。

## 6. Möbius completion 与确切导数符号

实读磁盘 (21) 是

(-ζ'/ζ)²=ζ''/ζ−(ζ'/ζ)'，

括号内没有额外负号。这等于 ζ''/ζ−ΣΛ(n)log n·n⁻s。
逐系数给 Λ*Λ=μ*log²−Λ log，distinct pq 的系数为
2log p log q，prime-power 分支也保留。

本审查过程中曾误读为 −(−ζ'/ζ)'；逐字重读后已撤回。
被审稿无需修改，当前绑定版本数学符号正确。

原 factor-conditioned high sum、路径窗和 absolute heights 没有由该
恒等式变成已准入的 residue-character inverse/plain 行族。
长度 X²、观测 height 长度 O(X) 的 MV 加权误差为 O(X²L²)，
不能用相同名称或单行 reciprocal 界消去这一未付 joint 费用。

## 7. 最终结论与剩余实质缺口

限定 PASS。physical ratio 方差 (11)、actual residual (16)、
finite parity (19) 和 completion (20)–(21) 的定义与证明相容。
正文明确标出以下仍未付：

- ||RE||HS²=O(d) 或 actual ||C_H²−Dhat||HS²=O(d)；
- factor-conditioned semiprime completion 的同 profile/height 行准入；
- full high fourth 的有限常数和 whole response 的 sharp 合并预算。

低四矩、bounded background 和 proper powers 只使 whole boundedness
与 actual high boundedness 互相蕴含；不产生 sharp 常数自由相加。
本 PASS 不把这些开放前件改成结果。
