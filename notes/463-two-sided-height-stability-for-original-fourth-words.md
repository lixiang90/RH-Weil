# 463：原 prime 四词的双侧高度稳定性

2026-10-07。无需 [R] 或未知第四矩上界，付清任意原 genuine-prime 四词
的辅助频带替换。它不删除三个内部有限投影。

## 1. 对象与结论

沿用 [461](461-original-one-high-three-low-fourth-trace.md) 的原 \(E,P,\phi\)、
sharp primes 和归一化，令 \(\mathcal F\) 为 unitary Fourier transform，

\[
 V=\mathcal F M_\phi E,\qquad K=\mathcal F M_{\phi^2}\mathcal F^{-1},
 \qquad J=[T/2,3T].
 \tag{1}
\]

对每个真实 prime range \(R_i\)，保留原乘子 \(D_i\)，
\(m_i=\|D_i\|_\infty\)，并取 \(D_i^g=D_i1_J\)、\(D_i^b=D_i1_{J^c}\)。
相应定义 \(B_i=M_\phi\mathcal F^{-1}D_i\mathcal F M_\phi\)、
\(C_i=E^*B_iE\) 及其 good 版本。则

\[
 \boxed{\begin{aligned}
 \|C_1C_2C_3C_4-C_1^gC_2^gC_3^gC_4^g\|_1
 &\ll T^{-2}\prod_i m_i,\\
 \|E^*(B_1B_2B_3B_4-B_1^gB_2^gB_3^gB_4^g)E\|_1
 &\ll T^{-2}\prod_i m_i.
 \end{aligned}}
 \tag{2}
\]

原全 prime 乘子有 \(m\ll\sqrt X/L\)。因此两种全第四迹的
raw/good 差各为 \(O(L^{-4})\)，除以 \(d\asymp XL\) 为
\(O(X^{-1}L^{-5})=o(1)\)。原 \(P\) 始终是 interval finite-carrier 投影，
没有改成连续频率投影，也没有与 \(1_J\) 交换。

完整证明见
[双侧高度研究稿](../reviews/2026-10-07/hybrid-two-sided-height-escape-research.md)，
独审见 [radial](../reviews/2026-10-07/hybrid-two-sided-height-review-radial.md)
及 [compression](../reviews/2026-10-07/hybrid-two-sided-height-review-compression.md)。

## 2. 为什么必须保留两端逃逸

原 \(C^2\) packet 尾和 \(d/L\asymp T\) 给

\[
 \|1_{J^c}V\|_2+\|1_{J_0^c}V\|_2\ll T^{-1},
 \quad J_0=[.9T,2.1T],\quad \|V\|\le1.
 \tag{3}
\]

准确的 \(C_i-C_i^g=(1_{J^c}V)^*D_i^b(1_{J^c}V)\) 因而具有
trace norm \(O(m_i/T^2)\)。有限词逐因子替换直接得 \(2\) 第一行；
其余因子取 op 界，不以未知 full fourth 付款。

对 physical 词，\(K\) 的卷积核是
\((2\pi)^{-1}\widehat{\phi^2}(t-s)\)。按 \( |t-s|\le T/100\) 分 near/far，

\[
 \|K_{\rm far}\|\ll T^{-1},\quad \|K_{\rm near}\|\le2,
 \quad \|K_{\rm far}1_{J'}\|_2\ll T^{-1}
 \tag{4}
\]

对长度 \(O(T)\) 的 interval \(J'\) 一致。
任意至多三个 \(K\) 和 bounded diagonal multipliers \(M_j\) 的交替链
\(\mathcal A\) 都满足

\[
 \|1_{J^c}\mathcal A V\|_2\ll T^{-1}\prod_j\|M_j\|.
 \tag{5}
\]

从 \(1_{J_0}V\) 出发，三个 near jumps 仍在 \(J\) 内，escape 准确为零。
其余词从右取首个 far，其 input 仍支撑在长度 \(O(T)\) 的 interval，
于是使用 \(4\) 的 HS 界，其他算子用 op 界。\(J_0^c\) packet 由 \(3\) 支付。
该论证也适用于反向伴随链。

physical 原词准确为 \(V^*D_1KD_2KD_3KD_4V\)。每个替换项在一个
\(D_i^b\) 处切开，左链须取 prefix 的反向伴随，右链保留 suffix。
两端各至多三个 \(K\)，且因 \(D_i^b\) 支撑于 \(J^c\)，两端都可准确
插入 \(1_{J^c}\)。分别使用 \(5\)，再作 HS–HS traceclass 配对，得到
\(T^{-2}\prod_i m_i\)。四个替换项相加即 \(2\) 第二行。

## 3. 实际推进与限制

这是 full-fourth 前件之外的高度准入接口，覆盖 high/low 的任意四个
有序 ranges。其全 prime 尾付款比 [461](461-original-one-high-three-low-fourth-trace.md)
使用的单侧粗界更强；旧证明与绑定无需改写。

结论只比较同类型的 raw/good 对象：actual 对 actual、physical 对
physical。actual 与 physical 之间的内部 \(P\) crossing 另须证明。
因此它尚不解决31、distinct22、高全异或整个第四矩常数；没有获得
新的零点比例或无零边界。需要 band 上 cancellation 时仍须明确列出 [R]。
