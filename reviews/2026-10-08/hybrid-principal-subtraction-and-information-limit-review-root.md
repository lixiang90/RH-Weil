# 完整主密度消去与整族矩信息限制：root 全文独审

2026-10-08。审查者 root，与两份来源作者不同。完整读取最终规范化文本；
结论是在下述准确作用域中 PASS，未发现数学阻断。此结论不表示外部同行评审
或形式证明，也不证明未知的原高素数第四矩上界。

| 审查来源 | canonical UTF-8 LF SHA-256 |
| --- | --- |
| [principal source](hybrid-whole-prime-principal-subtraction-and-product-length-research.md) | 87b98f4f1d176b72c66f07258dfb3c7499ac53844ce076c900d3d8ca9036a02f |
| [tensor information source](hybrid-whole-joint-moment-information-amplification-research-radial.md) | f9e3ffa1aa8c0be583b1c11fc952f8f09bd6deeee9f7bdfa31f3abda1523863e |

canonical 仅 CRLF/lone CR→LF，不 trim，不改 EOF。本报告不独审 root 自己
编写的471汇总。下面对两份新完整推导逐项复核，底层冻结分析只在其已审范围使用。

## 1. Principal source：同一个原有限算子

1. 来源的连续积分确实是逐向量 L² Bochner integral 定义的 strong
   operator integral。翻译族不要求 B(L²) 范数连续；其总变差有限给有界性。
   初稿的 operator-valued Bochner 表述已被纠正，最终文本没有该前件。
2. Fourier multiplier (3)是准确原函数积分：
   ∫_{sqrt X}^{X}x^{-1/2+it}dx
   =(X^{1/2+it}−X^{1/4+it/2})/(1/2+it)。
   sign、两个方向、a_ell 和 ell 因子与原 high channel 一致。
   交叉审查发现初稿下端错写 it；我初次核验也遗漏了这一点。
   最终源和本报告已修为 it/2，界只用两端模长，后续费用不变。
3. good height 的 sup 为 O(X^{-1/2}/ell)。bad multiplier 两侧准确
   同为 1_{J^c}F，HS²=O(T^{-2})，得到实际 C0 operator norm 小量。
   这里确实付了 t≈0 的峰；没有把原 P 与 frequency cutoff 交换。
4. 整个 four-word 比较不从 S4 距离小直接推出未知第四迹连续。
   实际用 infinity、infinity、S2,d、S2,d 的 Schatten Hölder：
   rho*m_H=O(ell^{-2})。原完整 high/low、任意 placement 及原 P 保留。
   多个 C0 的词也有同界，因其 S2,d≤rho、op≤rho。
5. bar Γ−Γ 的 S2,d norm 为 O(rho)，原 Γ 可有 O(m_H) 增长。
   因此 q 差的交费仍是 O(rho*m_H)=O(ell^{-2})；
   没有偷偷用 q 有界或将该交费删除。parity 投影为 HS contraction。
6. 我另读原有限 band admission 中 (13)–(16) 的 entry/shifted-grid
   crossing 证明及463的完整双侧 height 证明。它们对这里的 bounded
   continuous multiplier 有效，不需要其离散素数性质。
   good 差词的 closed crossing 费用为 ell*rho0*m_H³/d=O(ell^{-4})；
   raw/good 的两侧 escape 费用为 T^{-2}m0*m_H³/d
   =O(X^{-1}ell^{-5})。这些只支付含主密度的差词。
7. finite walk 的 signed measure 表达保留原 n_j、span、载波和 Γ_{d,r}。
   每个有限 T 的 Fourier ℓ¹ bound 与有限总变差允许 Fubini。
   高 physical 的 alternating/nilpotent 结构没有错误传给压缩后矩阵。

## 2. Principal source：真实乘积尺度与签名

素数原子的系数没有变化。两个不同素数的同一 product 有两个有序表示，
而 p² 只有一个，所以 ∑n n|c_H(n)|²准确等于
2(∑p p b_p²)²−∑p p²b_p⁴。其 X²/ell² 量级及 product 可达 X²
是原 atomic 类的标准误差成本；它不是整个 signed response 的下界。

source 明确 restricted 正 nearcore 不可当作全量正下界，也不从连续
部分的全量 o(1)推出每个 moving determinant shell 的替换合法。
31 的 near-product bound X^{3/2} 与真正 high4 的 X² 不能混淆。

最后的 (13)使用456已付完整 repeated union=19/240+o(1)，465已付
τWH²、τW²→19/480。因此 τH⁴=19/240+D_T+o(1)、
q=19/480+D_T+o(1)，无需未知 high4 bounded。
接近470必要下界的小 q upper 必须付四全异净负相消，D_T=o(1)不够。
这是条件目标解释；source 没有宣称已证明该负相消或新数值 Q。

## 3. Tensor source：有限 word 与全部方向

固定 m 的 normalized auxiliary trace 给 σA=σA³=0、
σA²=1、σA⁴=m/2。任何非交换 base word 保留原次序，其 trace
只乘 σ(A^j)。含0/2H的数据精确保留，已付 odd-H 零目标也仍成立。
U-parity、rowweights、whole low16词及两分量 covariance 均逐词满足此规则。

新增 D=A²−I 的辅助均值为零，且 σDA=0、σD²=γ−1。
所以 Γ̃=Γ⊗I+H²⊗D 与各 row-test/low residual/Z mode 的关系准确；
q̃=q+(γ−1)a，两 parity q_j 同理。
整个 gap 增量为 (γ−1)τ(H²UH²U)≥0，因为两个矩阵均 PSD。
这不是假设完整 Weil 矩阵 PSD，也不是交换 H 与 U。

signed fourth 展开给 F̃=γa+e+6c−k；
||HL−LH||2,d≤2||HL||2,d 使 k≤4c，
故 F̃≥γa≥γ(τH²)²。这一放大与470的两个下界相容。
完整 residual 的三个 auxiliary mode 正交，来源的 (20)也准确。

所有极限先固定 m 再 T。若 base a 无界，low S4 有界使 F 同样无界；
若有 bounded-a 子列，每个固定 m 模型仍 bounded-q，但 finite F 常数
随 m 任意增大。结论只针对列明 trace/Gram 信息类。
positive auxiliary variant 也保留0/2H数据，以反三角得相同有限信息限制，
没有将其未付 odd-H 项冒充原 exact zeros。

## 4. 作用域结论

tensor source 明确 W⊗I 是为保留 row-test 信息选择的 center，而真正
每prime tensor 后的 same-prime operator 会是 W⊗A²。该差异不被当作小量。
新 dm 维表示不保持原 scalar carrier，未证明原 prime coefficients、
raw/tail rates 或零侧 partial-Weil 账本。反模型不是实际素数或零点配置。

因此通过的是：原算子的合法连续主密度约化，以及所列整族矩数据没有统一
finite fourth upper 的信息限制。没有通过、亦没有被来源宣称通过的是：
可达 q upper、整个 mixed fourth 的有用常数、新比例、新无零边界或 RH。
现有 [R] 的 conductor-one 假设不会因这份有限审查而独立获得认证。
