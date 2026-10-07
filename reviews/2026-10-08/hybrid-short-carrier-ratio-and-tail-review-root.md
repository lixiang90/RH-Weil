# 原短载波压缩、完整比值方差与二阶谱尾：root 独立全文审查

2026-10-08。基线 2d5621dbc999e0cf313ea224b825d6d56547c45c。
本审查针对三篇新源及其继承接口；不修改冻结的既有研究或论文。

| 全文实读的新源 | canonical UTF-8 LF SHA256 |
|---|---|
| [完整原 P 的短载波平均付款](hybrid-anchored-carrier-averaged-fourth-projection-gap-research-radial.md) | c0e874ab9061982c8ef4365c8e9313eeac77eeddb756dc0b455cab3349f99dd8 |
| [half-ratio / 完整四全异双向归约](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md) | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 |
| [同加二阶谱尾与条带量纲](hybrid-second-order-tail-coupling-and-strip-geometry-research-compression.md) | e5c21e3a8bb0cb52e9e3131259a52dbb42051d7eb514ca8a65b083128b88d444 |

canonical 只将 CRLF/lone CR 转成 LF，不 trim 或改 EOF。
结论为上述明确范围内 PASS；不是对新的实际比例、无零边界或完整
算术四矩 upper 的 PASS。未运行原 math 的 Lean 工程。

## 1. 短窗口付款的完整核对

原 X、ell、d、taper、b_p 在平均前冻结，E_sigma 只作共同 modulation。
输出支撑在 I，所以 Q 的相关部分确为全 interval Fourier basis 的
outside j；不需补一个 I 外的未知范数。每个 n=j-k 的 outside k
计数为 min(d,|n|)，包括负 n 与 |n|>d 的饱和区。

原 C² 尾给 min(ell,C/|xi|,C/xi²)。围绕任意实 nu=xi/h 的 lattice
分段得到 W_ell(xi)≪log(2+ell)+ell|xi|；没有把 xi 取整。
在 xi=1/ell 与 1 处分段，可积的 sqrt(|xi|) 权重给
∫|hatφ|sqrt(W_ell)≪sqrt ell。若换成 |xi| 权重，仅凭此粗 C² 尾
不能保证可积；新源没有作该错误替换。

经典 finite weighted MV 是对所有起点区间的一致二矩界。
两侧 p^(±it) 可分开支付，无需假设 prime signs 之间的独立性。
Σb_p²≪1、Σp p b_p²≪X/ell 均由 Chebyshev/partial summation 支持。
先在联合 L²(sigma,j,k) 中用 Minkowski，才用这个一致界，准确得到
avg(lambda_R²)≪ell+X/s。积分/无穷 entry 的极限有上述可积
majorant；没有交换未控制的绝对值和 signed mean。

四阶正差是准确的块恒等式：

\[
 \Tr(E^*B^4E)-\Tr((E^*BE)^4)
 =\|QB^2E\|_{\rm HS}^2+2\Tr(A^2K)+\Tr K^2,\quad
 K=(QBE)^*(QBE),\quad A=E^*BE.
\]

每项非负，且总和≤7||B||² lambda²。以 raw
||B_H||²≪X/ell²、d∼Xell 代入，费用为
ell^(-2)+X/(s ell³)。s=T/sqrt ell 时第二项为 O(ell^(-5/2))。
这是实际平均 gap 的付款；没有借 [R] 或未知 high fourth bounded。
一般 x⁴ 并非 operator-convex，不是本证明的前件。

三个内部 P 的完整展开有七个含 Q 的闭合路径，每条至少两次
crossing；其余两因子仅用 raw op。Cauchy 支付 avg(lambda_i lambda_j)。
因此所有 16 个 ordered H/L 四词的 mean absolute 差均 O(ell^(-2))。
以 lambda_H²+lambda_L² 一次 Markov，也可在同一个 ≥1/2 的 good set
上取得同阶误差。总 channel 四词包括全部 prime signs 和标签；
不是逐 tuple 的 P 删除，也不使各 physical placements 自由循环。

q_sq 与 actual q 的准确差为
2τ(A²K)−2τ(WK)+τK²，介于 −2MτK 与正四阶 gap 之间。
它们均不同于 full physical residual；新源没有混同这三个量。

[228](../../notes/228-relative-dense-zero-block-transfer.md) 的合法端点
接口单独实读：s=o(T) 给零点块对称差 O((s+1)log T)=o(N)。
只继承其移动零块与 uniform second/Archimedean 合同，不继承旧未付
fourth arithmetic 常数。固定 sigma=T 的逐点小 gap 没有被证明。

## 2. 完整比值归约的核对

实读 [465](../../notes/465-centered-high-square-joint-fourth-budget.md)
与[原 high half-Gram 源](../2026-10-07/hybrid-high-parity-gram-and-mobius-completion-research-radial.md)。
W 是同一个 prime diagonal 的有限乘法压缩；共同 modulation 不改变
其矩阵。原加权二矩的 leakage/cross 费用仅用 raw op 与二矩，
Hilbert 主项中 sigma 只是可吸收的单位模相位。因此 uniform
q_sigma=a_sigma−S_T+o(1) 不以 q 或 a 有界为前件。
完整 repeated union 的删除 helper 也不乘未知全四矩；其原 scope
与短窗口相容。没有把 2S 与 whole high fourth 等同。

A=Π_-AΠ_+ 给 physical A²=(A*)²=0；不会推出 (E*AE)²=0。
必须用 K=CJ 而非单独反射 J：K 固定每个原 E_sigma e_k。
于是两个半块的 ||G E_sigma||HS 相等，full Φ=2||G E_sigma||HS²。
原 D_+R_+ cross 的变量代换保持共享窗，Hilbert 费用 O(1/ell)
对 sigma 一致。因此 Φ/d=S_T+2r_sigma+O(1/ell)，其中 r 是
明确 half-ratio 范数。full ratio 的平方范数是其两倍，非同名混用。

结合已付 mean absolute gap，q−2r 与 D−(2r−S_psi) 都在 L¹ 中趋零。
uniform o(1) 不乘增长的 r、q；共同 good set 保留全部 16 词。
若另证 avg r≤B_T，则在这个集合内选择必须支付
B_T/(1−eta_T)，只有 B_T=O(1) 才能把损失改写为 additive o(1)。
旧 Jensen 已给 r upper⇒q upper 的单侧充分路线；
新增结果是双向增长一致的归约和同一 good set，源已正确区分。

long sinc² 平均的归一化与 Fourier 三角窗正确。四 distinct primes
无零频率，最小对数差仅可按 X^(-2) 支付，宽度 X² 可消去有限 D。
该宽度不属 [228] 的 o(T) 端点范围；不能推出现有短窗口的 r upper。

## 3. 二阶谱尾与条带几何的核对

对 n_+(Q)≤b 的 A=P+Q，Weyl 给 lambda_(i+b)≤p_i。
F(t)+kappa_2(t) 在负轴为 0，在 [0,2] 为 4t−t²，超过 2 为 4。
故前 b 槽≤4，后 s 槽≤2p_i+1−j(p_i)，其余槽≤0。
同一个槽位证明允许 tr j(G) 与完整负尾/正尾同加，
而不允许把针对同一 j 的多个下界重复相加。

p 不必等于 s；原账本恢复 simple/distinct 的式 (4)–(5) 正确。
两份 PSD square 及一份 contraction 的变分式独立优化，非对角
效果只增加 square 成本，谱基标量完成平方即得精确对偶。
Hoffman–Wielandt 与二次增长导数界给式 (11)，仅需二矩恢复。
这不是整个 Weil 算子半正定，也不需要 full fourth upper。

root 要求并已核改两处文字：j 仅在 [0,∞) 上 2-Lipschitz；
e^(dL)/L packet 下界只属随 L 的原 AF taper，不能套给固定 η_delta。
在原标准化零坐标中固定 7/8 条带宽度为 3log T/(16π)，
不会随 T 收缩。单对未压缩负特征值不是多对有限配置的尾下界。
low-only 实际效果的两份二次型分别正、负定，Schur gap=5/6；
没有给出正的 normalized tail 收益。原三点常数也没有因此变大。

## 4. 精确有限复核与保留的开放项

[新检查器](../../scripts/hybrid_short_carrier_checkpoint.py) 的 finite()
独立执行通过 32 项恒等式/不等式检查，包括非交换复数 Hermitian
块的正 gap、same-W 夹界、全部 16 词的七路径展开、
固定载波的反线性 half-ratio factor2、两端谱尾 dual 及指数账本。
这些是有限代数检查，不能认证 prime 渐近。

本轮实际付清的是合法短窗口中的 whole fourth projection correction。
同一窗口完整 ratio 方差的有用 upper，以及实际 kappa_2/N 的正
lower，仍没有付款；没有得到新的零点比例、无零边界或论文结果。
既有 [R] 分析内核仍须按原 source 的范围继承。
