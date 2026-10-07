# 三列共同反射稿的独立全文审查（mixed）

2026-10-07。结论：**全文限定 PASS；未发现 P1/P2 数学错误。** 通过范围是实际三变量 meromorphic identity、two-plain natural reflection、inverse negative-line identity与显式 residue / joins归约，以及临界固定邻域的定量 replacement。没有通过新的 strict mixed saving、`χ>0`、`γ<1/3`、新无零边界或整个 generic joint energy theorem。

仅新增本审查文件。被审稿、冻结稿、外部 `math/paper.tex`、Goal、Git 均未修改。没有派 subagent。

## 1. 实读对象与哈希绑定

canonical LF 规则仅为 CRLF→LF、孤立 CR→LF，再 UTF-8 SHA-256。本轮实际重算：

| 实读对象 | canonical LF SHA-256 | bytes |
|---|---|---:|
| `reviews/2026-10-07/hybrid-three-column-reflection-research.md` | `30929e068a6b1610a1ea64aea4e5a0d46623b9fd2f7e41c18f77044d7b209878` | 27422 |
| `reviews/2026-10-07/hybrid-amplified-mixed-column-research.md` | `5f07dc2626ef0fa5ec20f0a56ab113b3ed55679ad066bb93174e1ee98d843752` | 20777 |
| `reviews/2026-10-07/hybrid-critical-neighborhood-mixed-witness-research.md` | `ef85a5e5fd5aef3543aef6eb4b6adff6a1ecd39791575a89704e4b08e04e8983` | 19827 |
| 外部固定 `paper.tex` | `42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3` | 766316 |

外部源路径为 `E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，固定 commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`。重读的相关源段包括 705–726、1425–1453、1602–1640、4221–4268、4390–4479、4510–4680、12343–12360、12511–12531、12677–12773、14997–15047；另重读 1676–1723、1793–1845、7934–7967、11603–11665 核 generic cubic / marked 的实际输入。

为核 Bessel 的归一化和初始 Mellin strip，本轮只浏览官方 [DLMF 10.22.43](https://dlmf.nist.gov/10.22.E43) 与 [DLMF 10.2.2](https://dlmf.nist.gov/10.2.E2)。其余判断由实读源和下列独立计算支持，不是接受被审稿自述。

## 2. `μ×1×1` 的三变量 reciprocal FE

源 4224、4232–4242、12511 确定实际 row character为有限阶 ray target乘 sextic symbol；1437–1442 确定 primitive infinity type为0，故 archimedean factor为 `Γ(s)`。不同 detector frequencies属于 tests，不是新的 infinity type。这正当化被审稿的

\[
 L_\psi(s)=L(s,\psi^*)D_R(s),\quad
 C=3Q_{\psi^*}/(2\pi)^2,
\]

\[
 L(s,\psi^*)=\varepsilon_\psi C^{1/2-s}
       \frac{\Gamma(1-s)}{\Gamma(s)}L(1-s,\bar\psi^*).
\]

三个实际 annular sums在 `c_j>1` 的 Mellin integral均绝对收敛。因此 `L(s₁)L(s₂)/L(s₀)` 是真实 `μ×1×1`，而不是同 height的单变量 convolution猜测。逐列作 FE，root number确为 `εψ^(−1)εψ²=εψ`，Gamma quotient为

\[
 \frac{\Gamma(s_0)\Gamma(1-s_1)\Gamma(1-s_2)}
 {\Gamma(1-s_0)\Gamma(s_1)\Gamma(s_2)}.
\]

六个 natural correction factors的 numerator / denominator与被审稿 (5) 一致。若所有 `Re s_j, Re(1−s_j)≥σ₀>0`，deleted-product导数界由有限 product和 logarithmic derivatives直接得到；不能延伸到 `Re s₀≤0`。三个 `z_j=1−s_j` substitution给 normalized scales

\[
                         (CD)^{-1},\quad C/X_1,\quad C/X_2.
\]

第一项的 reciprocal scale不是 `C/D`。被审稿没有把这三个 formal scales当作三个已经可准入的 short polynomials；这项限制正确。

## 3. 两个 plain 的 full natural reflection与 moving phases

源 12733–12754 的 formula直接适用于两个独立 tests，保留 `d_j|R` 和 `h_j|R^∞` 的全部 powers。系数是

\[
 \frac{\mu(d_j)\psi^*(d_j)\bar\psi^*(h_j)}{\sqrt{N d_j N h_j}},
 \qquad Y_j=C N d_j/(X_j N h_j).
\]

其总 absolute mass为 `q_R^ε`，不是额外 cancellation。好 prime的 conductor / redundant radical只占一次，固定坏素数部分有限，因此 `v=ua⁶` 上 `Cq_R≪UA`、`Y_j≪UA/X_j` 正确。第 3 节显示的 reflected plain上端可能比原 `m` 更长，这个费用没有被隐去。

在原 exact complex product中，two-plain共同 `εψ²` 在 rowwise absolute square里抵消；它不抵消 `d,h` 的 moving primitive phases、inverse residue的 orientation或原 once slots。被审稿 (11a) 保留了原 `Qψ`、四个 restored variables和所有 coefficients。对 redundant prime，`ψ*(d)` 可以非零，natural `ψ_v(d)`却为零，因而不能用后者替代前者删除项。

Whole-conjugating `Q` 只是在 norm中合法重写；只 conjugate部分 slot不合法。逐 row coefficient mass并未被当作跨 rows / dual tuples的共同 separating measure。原 source generic energy确需比单个 root phase抵消更强的独立性，被审稿对此限制准确。

## 4. Reciprocal Bessel kernel、subtraction sign与 convergence

独立对被审稿 (13) 作 Mellin计算：

\[
 g(y)=\frac1y\int_0^\infty f(t)J_0(2/\sqrt{ty})\frac{dt}{t}.
\]

令 `x=1/(ty)`，则其 Mellin transform是

\[
 \widehat f(1-z)\int_0^\infty J_0(2\sqrt x)x^{-z}\,dx
          =\widehat f(1-z)\frac{\Gamma(1-z)}{\Gamma(z)}.
\]

初始 absolute Fubini strip可具体取 `3/4<Re z<1`；DLMF 的条件积分公式随后给 wider continuation。常数2正确，没有缺少 `2π`。`J₀` series逐项给 large-`y` coefficients `(-1)^k fhat(−k)/(k!)² y^(k+1)`。非零 compact smooth `f` 不可能有所有这些 moments为零：换元 `x=1/t` 后 polynomial density强迫 `f=0`。故 reciprocal kernel一般只有有限阶 tail，不能自动满足 source 1718–1720 的两端 arbitrary rapid要求。

`z=1` 的 `fhat(1−z)Γ(1−z)/Γ(z)` residue是 `−a₀`。把 inverse Mellin line向右移到 `1<Re z<2` 时，原 kernel等于新 integral加 `a₀/y`；所以

\[
                 f^+(y)=f^\vee(y)-a_0/y
\]

的 Mellin transform确为该 quotient的 continuation。`f⁺` 在零端为 `−a₀/y+O(y^A)`，在无穷端为 `O(y^(−2))`，故 strip `(1,2)` 正好相容。被审稿没有把这个 subtraction当成可直接丢弃的 term；正确。

Small-`y` inverse Mellin left shifts没有 poles，给任意固定 order的 rapid decay和有限 polynomial height费用。这里的 contour / derivative order必须先固定再选 `τ`；它不是可随 external tail order免费增加的 bound。临界 replacement只需 large-`y` 的 absolute estimate，该 estimate不新增 exponential height loss。

## 5. Negative contour与精确 dual coefficient

对 squarefree redundant `R`，逐 Euler factor有

\[
 D_R(s)=\mu(R)\psi^*(R)q_R^{-s}D_{\bar R}(-s).
\]

在 `s=−r+it`，`0<r<1`（实际可取 `r=1/20`），这把 reciprocal deleted product送到 `Re(−s)=r>0`，因此避免了错误的负半平面 reciprocal bound。FE给被审稿 (18) 的 phase与 powers。

写 `z=1−s,Y=(Cq_RD)^(−1)`。尺度 identity为

\[
 D^{s-1/2}C^{s-1/2}q_R^s
                        =\sqrt{q_R}\,Y^{z-1/2}.
\]

`L(z,barψ*)^(−1)` 与 `D_barR(z−1)^(−1)` 在 `Re z=1+r` 均绝对收敛，后者 coefficient是 `barψ*(h) q_h^(1−z)`。因此真实 dual series中的 coefficient确为 `q_h`，outer factor确为 `√q_R`。被审稿 (20) 全部 powers / phase / normalization通过独立推导。

当 `Y≤1`，`f⁺(NnNh/Y)=O((Y/(NnNh))²)`。直接相加得到

\[
 |I_-|\ll \sqrt{q_R}Y^{3/2}
      \sum_n(Nn)^{-2}\sum_{h|R^\infty}(Nh)^{-1}
 \ll C^{-3/2}D^{-3/2}q_R^{-1+\epsilon}.
\]

这是真实绝对界，不是假定 dual Möbius cancellation。`C≫1` 在后续 exponent比较中指固定正下界，足以把 `C^(−3/2)` 作为常数；不需要字面 `C≥1`。临界大 `D` 确保所用 `Y≤1`。

## 6. Zeros、Euler pseudozeros、joins和量词

`1/Lψ` 的所有 poles都在 finite Cauchy rectangle内按实际 multiplicity取 residues；包括 primitive/nontrivial zeros、`s=0` 的 trivial零及 redundant Euler zeros，重合时也不假设 simple。`r<1` 尚未越过 `s=−1`。Euler zeros的 count `O((1+H)log(2q_R))` 只计数，不控制 residue大小。

Counterclockwise rectangle的 top由右到左、bottom由左到右，Cauchy rearrangement给 `M=P_H−horizontal+I_-+vertical-tail-difference`。因此被审稿对 `J_H` 的负号和 (23) 正确。

在右 absolute line，inverse Euler series统一有界。在负线，positive Euler convergence和 Stirling给

\[
 |L_\psi(-r+it)^{-1}|
 \ll C^{-1/2-r}q_R^{-r+\epsilon}(1+|t|)^{-1-2r}.
\]

实际 test `f=V y^(−σ−iω)` 的 Mellin transform是 untwisted transform在 `t−ω` 的 translate。故 external tails只对 `V` 使用高阶 derivative，不索取 `(1+|ω|)^N` 的新 allowance。给定 fixed finite target error `A`，先固定 length / amplifier ranges与 internal height orders，选正 `τ`，再选足够大的 external order `N`，两条 vertical tails可统一为 `O(U^(−A))`。

选择 `H≈T₁` 的无零 boundary只避开离散坏 heights，并没有证明
`sup_{−r≤σ≤c}|Lψ(σ+i(ω±H))^(−1)|` 的 polynomial uniformity。被审稿明确保留 `J_H`，没有用 external `N` 免费消灭它。选择 `H` 可依 row / profile；其点态 error uniform，并且本稿没有对该不光滑选择求导，所以这一选择不破坏 replacement。

P3澄清：被审稿 (24) 后的“numerator恰为 `Vhat₀(iν₊)`”应按 test-transform numerator读取，即
`fhat₀(ρ)=Vhat₀(iν₊)`。完整 residue numerator仍是 `Vhat₀(iν₊)D^(ρ−1/2)`，不可漏掉这个尺度。本稿 (24) 本身已经保留它，所以不是数学错误或 saving。

## 7. 临界 `o(1)` replacement及其 uniform derivative预算

写 `Δ_v=M_v−Z_v`。第 5、6 节给 uniform pointwise `Δ_v=O(U^(−3ℓ/2))+O(U^(−A))`。所有结构 rows至多 `O(U^η)`。对原实际 profiles使用源 bin pointwise bound，`|M_v|²≪U^(δℓ+ε)`，而 two-plain加 prime部分
`|B_v|²≪U^(2δm+δz+ε)`。每个 physical prime的 upper fee是 `δ` 每单位 squared slot length，而不是邻域中免费换成 selected `2q`。

故

\[
 \sum_v|\Delta_vB_v|^2
       \ll U^{\eta-3\ell+2\delta m+\delta z+\epsilon},
\]

\[
 \left|\sum_v|M_vB_v|^2-\sum_v|Z_vB_v|^2\right|
       \ll U^{\eta-3\ell/2+\delta\ell/2+2\delta m+\delta z+\epsilon}.
\]

这也可由 Hilbert triangle / cross term得到；被审稿 (31) 的 exponents正确。

在 reference，`δℓ=(5ℓ−3)/6` 且 `2δm+δz=1/3`，取 `η=ℓ+a` 后 leading exponent独立化简为

\[
                               a-(\ell-1)/12.
\]

`0<a<(ℓ₀−1)/24` 应先在 fixed reference `ℓ₀` 上选择，然后把 live critical neighborhood和所有 adjustable losses缩小到该 strict margin以内；如此得到同一个负 exponent。被审稿第 7 节已按这个顺序叙述；第 10 节列举参数时可按这一 joint选择读取，不能先任取大邻域再免费索取同一个 `a` 的 uniform `o(1)`。

Finite-dimensional derivative预算可具体定位：原 long cutoff是 `W₁(y)V_≤(Dy/D*)`，transition上 argument有界；源 4621–4629和4540给每个实际调用的 untwisted annular seminorm一致有界。多个 extracted heights独立，但数量固定；Sobolev orders和 total added-frequency allowance先共同固定，`τ`随后减小。反射原 plain profiles若需 annular partition，相关 contour / Euler orders作为 internal orders预先固定。新增 reciprocal vertical tail使用原 untwisted Mellin translate，不改变这些 height orders。因此没有把 external `N` 的费用偷偷放回 allowance。

对不光滑 `H` 选择也无需新的 profile derivative theorem：uniform `|Z|≤|M|+|Δ|` 先把 unweighted / maximal `Z` energy支配回已付的 `M` family。`η>ℓ` 留固定正 raw margin，可在 all-element raw theorem取 fixed `c<a/ℓ`；profiles / finite Θ labels的 Sobolev loss由先固定的有限 orders和随后的小 `τ`支付。这只给 `Σ|Z|²≪U^(η+ε)`，没有给 weighted deconcentration。

所以被审稿 (33) 是有效的 bin-wise **定量 replacement**。它的右方还含全部 actual zero residues和 horizontal joins的 weighted covariance；`o(1)` error并不使这个主项小。

## 8. Covariance subtraction与完整 mod-six分支

三个 complex numbers `A=L₁,B=L₂,C=L₀` 的代数 identity
`AB/C=A+B−C+(A−C)(B−C)/C` 正确。前三项的三重 Mellin integral各含两个 unit evaluations；actual annular scales足够大时这些 evaluations为0。最后 covariance integral没有强加 `s₁=s₂=s₀`。

Simple zero附近 `L(ρ+ξ)=ξ∫₀¹L'(ρ+tξ)dt` 给被审稿 (38)。它并未为 actual unequal-height profiles提供 microscopic `ξ`，也未给 `1/L'(ρ)` 下界。Local Euler subtraction (39) 的 common-denominator numerator是 `(a₁−a₀)(a₂−a₀)`，亦正确。

对 good prime的 `j=1,…,5`，source的非平凡 finite residue-field characters均有 `|τ_{p,j}^-|=1`。变量换元给非零 additive numerator分支；zero additive numerator时角色和为0。`j=0` 必须读 unit indicator，于是 Fourier值是 `−1/q_p` 或 `1−1/q_p`。被审稿 (41) 四分支正确，覆盖全部 mod-six exponents且保留 exponent-cancelled primes的 zero mask。

Source generic cubic output真正含
`χ_{k_res}(nb)^3 χ_P(n)^(−2)` 与两个 displayed coprimality masks；还依赖 squarefree Gauss initialization、whole `b³`、固定 cusp classes和 tuple / row coefficient独立性。当前三列的 signed exponents与 (20) 的 geometric inverse weights没有被错误等同于这个 output。Source 7934–7966 的独立性也没有被 rowwise `q_R^ε` coefficient mass取代。

## 9. 已通过内容与下一步的准确限制

通过：actual independent-height三变量 FE；原 once slots保持；two natural plain完整反射；common root number与 moving phases；reciprocal Bessel tail和正确 subtraction；negative-line绝对 series；全部 actual poles / joins；固定临界邻域的 `M mean=Z mean+o(1)`；quotient / local covariance algebra；all-mod-six local Fourier table。

未通过，也未在被审稿中声称已付：restricted energy `Σ_{Eχ}|Z|²≪U^(η−χ+ε)`、horizontal inverse bounds、actual residue deconcentration、joint generic signed energy、新 `χ>0`、新 `γ<1/3`、全域 continuation或σ certificate。用现有 unweighted energy和 pointwise caps无法推出这些新输入。

特别，改变 imaginary quadratic field只会先改变普通 finite-order Hecke FE中的 discriminant / conductor常数；这项三列 `Γ(s)` / `J₀` reflection并没有自己产生 cubic-to-quadratic terminal。任何更强边界仍需同一个 actual probe的 Gauss/theta完成、全部 local masks和 residue / join控制，而不是只改变数域名或 amplification次数。
