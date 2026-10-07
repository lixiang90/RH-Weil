# 459 根节点全文审查与 principal 接口澄清

2026-10-07。正文限定 PASS；没有新的 strict joint saving 或边界。
被审 [459](../../notes/459-natural-inverse-and-primitive-zero-joint-reduction.md)
canonical LF SHA256：
`fe6046154965fb8e833e0a96adf0801f9aa4fd4b2ea8b27397748c79193477b6`，
8861 bytes、230 lines。根节点全文复读并重新推导以下接口。

## 1. 同对象恢复及定量误差

两方向恢复恒等式逐 prime 精确成立：primitive inverse 的局部
\(1-a_pt\) 乘 geometric inverse 后恢复 natural inverse 的局部 1。
系数 \(q_h^{-1/2}\) 与缩放 \(X/q_h\) 的 normalizer 相容。
\(f\) 始终保持原尺度的 profile/cutoff，不能随短尺度重新定义。

对任意 fixed \(s,\varepsilon>0\)，
\(\prod_{p\mid R}(1-q_p^{-s})^{-1}\ll (NR)^\varepsilon\)，
由有限小 primes 与大 primes 的 \(\varepsilon\log q_p\) 分拆得到。
因此 weighted scale supremum 的双向比较合法，不需要行权独立。
它不是两个固定尺度观测量的等式或免费的 separating measure。

恢复尾用 \(0<t<1\) 的正幂比较给
\(D^{1/2-\theta+\theta t}(NR)^\varepsilon\)。负线误差求和给
\(C^{-3/2}D^{-3/2+\theta(1+t)}(NR)^\varepsilon\)，比恢复尾更小。
原 \(C\) 的固定正下界足够；不要求其数值大于一。
独立 height 仅以相位出现于绝对界，rectangle/vertical orders 必须
按正文顺序选取，horizontal joins 始终保留。

有限 \(G(s)=\sum_{q_h\le D^\theta}\psi^*(h)q_h^{-s}\) 的幂次准确；
它是 entire polynomial，显式极点仅来自 \(1/L(s,\psi^*)\)。
原自然零掩码、row-dependent phases、redundant radical 和恢复尾
没有删除。simple-zero 例式保留完整 \(D^{\rho-1/2}/L'(\rho)\)，
multiple zeros 与实际 joins 也未假设小。

对 \(\#v\le U^\eta\)、\(D=U^\ell\)、\(|B_v|^2\le U^{b+\varepsilon}\)，
平方误差是 \(U^{\eta+b-\ell(2\theta-1)+\varepsilon}\)。
Hilbert norm triangle 给任意固定 \(0<\chi<\ell(2\theta-1)\)
的严格预算双向等价，也适用于原 nonnegative peak-set weight。
这支付近似误差，不支付等价两边本身的 strict upper bound。

## 2. Principal presentations 的范围

459 §1 明写 nonprincipal presentation。正文审查按这个范围接受，
不能仅凭 §5 的 whole-row 字样把它提升为全部行的 theorem。
无需把可能的 principal rows 宣称已由某个未核验的 source exception
计数付清；下述普通 meromorphic FE 给相同接口的直接延伸。

在当前虚二次域，primitive principal \(L\) 为 \(\zeta_K\)。
它仍有同一普通 FE，在 \(s=-r+it\)、\(r=1/20\) 上给

\[
 \frac1{\zeta_K(s)}
 =C^{s-1/2}\frac{\Gamma(s)}{\Gamma(1-s)}
 \frac1{\zeta_K(1-s)}.
\]

右侧 inverse Dirichlet series 在 \(\Re(1-s)=1+r\) 绝对收敛。
在这条线逐项使用原 Bessel kernel
\(f_+=f^\vee-\widehat f(0)/y\)，仍得到
\(O(C^{-3/2}X^{-3/2})\) 的 negative-line 界。
这个论证不跨越 \(\Re z=1\) 再删除 residue；直接在
\(z=1-s\)、\(\Re z=1+r\) 的收敛线上使用同一 kernel。

\(\zeta_K\) 在 \(s=1\) 的 pole 是 reciprocal 的 zero，不能记作
inverse residue。FE 中 \(s=0\) 的 apparent Gamma pole 与
\(1/\zeta_K(1-s)\) 的 zero 抵消。contour recovery 只收集实际
reciprocal poles；所有 primitive nontrivial/trivial zeros 与 joins
仍按实际集合保留。固定 contour、scale、height 量词不变。

所以 (3)–(14) 的恢复和余项，可在另行采用这项 principal meromorphic
FE 时延伸到 principal presentations。这里记录的是明确的附加
推导，未修改 459、其既有 hashes 或两份独审。
后续 whole mixed saving 若使用该延伸，必须同时列出它的前件。

## 3. 原完整目标

本次 primitive 恢复把待证输入缩小到实际 residues/joins 联合能量，
仍需原 two-plain、once-slots、unequal heights 与所有 natural masks。
不从 zero-free boundary 推出 uniform inverse 或 \(L'\) 下界，
不把有限 \(G\) 的绝对 mass 当作新的跨行 cancellation。
无新零点比例或无零边界，Goal 保持 active。
