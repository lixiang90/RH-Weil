# Primitive principal inverse 延伸独审：compression_bridge

2026-10-07。结论：**PASS，限于原 inverse 恢复、负线余项及其量词**。
只新增本独审，不改 459、既有独审、论文、math、Goal 或 Git。

核对对象为
[root 的 principal 接口延伸](hybrid-natural-primitive-joint-review-root.md)
§2，canonical LF SHA256
`90ae81d09b28ca8a314404d0efda2b7339730788e6aaed33353794c045319d0a`，
4109 bytes / 81 lines。其所绑定的
[459](../../notes/459-natural-inverse-and-primitive-zero-joint-reduction.md)
canonical LF SHA256 为
`fe6046154965fb8e833e0a96adf0801f9aa4fd4b2ea8b27397748c79193477b6`，
8861 bytes / 230 lines。459 正文本来明确 nonprincipal，本延伸是另列前件
的附加推导，不能由其 whole-row 字样自动取得。

## 1. Meromorphic FE 与负线的实际 series

当前固定虚二次域的 primitive principal L 为 zeta_K，root number 为 1。
沿用相同 C 与 Gamma normalization，其 ordinary meromorphic FE 给

\[
 \zeta_K(s)^{-1}
 =C^{s-1/2}\frac{\Gamma(s)}{\Gamma(1-s)}
       \zeta_K(1-s)^{-1}.
\]

取原固定 0<r<1，例如 r=1/20。令
`f(y)=V(y)y^(-sigma-i omega)`，保持原 annulus/profile，不在 D/h 重定义。
负线 integral

\[
 I_-(X;f)=\frac1{2\pi i}\int_{(-r)}
         \widehat f(s)X^{s-1/2}\zeta_K(s)^{-1}\,ds
\]

变元 z=1-s 后就在绝对收敛线 Re z=1+r。原 Bessel kernel

\[
 f^\vee(y)=\frac1y\int f(t)J_0(2/\sqrt{ty})\frac{dt}{t},
 \qquad f_+(y)=f^\vee(y)-\widehat f(0)/y
\]

在 1<Re z<2 的 Mellin transform 是
`fhat(1-z)Gamma(1-z)/Gamma(z)`。因此可直接展开
`1/zeta_K(z)=sum_n mu(n)q_n^-z` 并交换绝对收敛 integral/series，得到

\[
 Y=(CX)^{-1},\qquad
 I_-(X;f)=Y^{-1/2}\sum_n\mu(n)f_+(q_n/Y).
\]

这条计算没有把 z contour 左移穿过 z=1，也没有删除其中 residue。
`f_+` 的定义是已固定的 Bessel Mellin continuation，不依 principal
inverse 是否有极点。故 principal 的 meromorphic FE 可使用同一 kernel。

原固定 annulus 上的 J_0 大 y 展开给 `|f_+(y)|<<_f y^-2`，y>=1。
因为 |y^(-i omega)|=1，这个 bound 对独立 omega 统一。
当 X 大到 Y<=1 时，所有 q_n/Y>=1，故

\[
 |I_-(X;f)|\ll_f Y^{3/2}\sum_nq_n^{-2}
 \ll_f C^{-3/2}X^{-3/2}.
\]

所以 root 所写 principal negative-line bound 正确。无需 principal
L 的 nonvanishing 于 critical strip、L' 下界或新的 Mobius cancellation。

## 2. 极点、joins 与 height 量词

原 inverse contour integrand 是 `fhat(s)X^(s-1/2)/zeta_K(s)`。
zeta_K 在 s=1 的简单 pole 成为 reciprocal zero，不能列入 inverse residues。
在 s=0，FE 的 Gamma(s) 简单 pole 与 `1/zeta_K(1-s)` 的简单 zero
抵消；不会产生虚假的 reciprocal pole。其他真正 reciprocal poles
依实际 primitive zeros 和 multiplicities 保留，不能由本延伸删除。
原 rectangle/joins 的 Cauchy identity 继续成立。

负线上 Euler convergence、Stirling 给
`|1/zeta_K(-r+it)|<<_r C^(-1/2-r)(1+|t|)^(-1-2r)`，
bounded t 由同一 FE 与 continuity 支付。原 right-line inverse series
也绝对收敛。因此两条 vertical tails 与 459/三列报告的 translated
Mellin decay 同型：先固定 profiles、contour/internal orders 与尺度范围，
再选 H 的固定幂长度，最后选 external tail order。
独立 omega 仍只作为 Mellin center，不能把 external order 转成 omega^N。
horizontal joins 始终是未付的实际量，并未由 boundary 无零推出小量。

## 3. 恢复到 principal natural presentation

自然呈现的 redundant Euler radical R 与全部 zero masks 仍按 459 (3)–(4)
逐 coefficient 精确恢复。上述 primitive bound 在所有 retained 尺度 D/q_h
上使用同一 f；C 的固定正下界足够，principal conductor 为固定量也无碍。
原 finite G(s)、geometric tail、negative-error sum 和加权 Hilbert triangle
都不依赖 nonprincipal 条件。所以 459 (3)–(14) 的 inverse 接口可延伸至
principal，所需误差与固定量词保持。

这是 inverse 接口的明确附加接受范围。若后续另行反射 principal 的 plain
L-columns，其 L 本身在 s=1 的 pole 必须在相应 contour 中另行保留；
本 inverse 延伸没有支付那类 plain residues，也没有给实际 mixed strict saving。
459 与原 nonprincipal 独审的绑定版本保持冻结。
