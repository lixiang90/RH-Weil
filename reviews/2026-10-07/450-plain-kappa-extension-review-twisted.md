# 原 plain 矩证明的独立 κ 扩域复核

2026-10-07。审查人：twisted_research。状态：**限定 PASS [T/R]**。
本报告独立逐行逆审原证明，而不是将原来只写明
`κ∈[3/4,1]` 的 lemma 直接调用到区间外。保留该证明明确使用的通用
算术、解析和有限阶连续性输入 [R]，原证明可重证成
`κ∈[37/50,1]` 上的一致 plain lemma。没有修改原 math 源、已提交笔记或论文，
没有构建 Lean，也没有在本报告中推出新的无零边界或零点比例。

## 1. 固定源及实际审查范围

只读源为
[paper.tex](E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex:12492)。
CRLF 和孤立 CR 均转 LF 后的 UTF-8 SHA256：

```text
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
```

canonical UTF-8 长度为 766316 bytes。逐行阅读的主体为12492–15015；另独立阅读
1123–1286 的 smooth calculus、1347–1413 的 kernel seminorms、
1425–1450 的 Hecke strip-growth 接口和1531–1600的 logarithmic control。
此前固定 `κ≥3/4` 的准入报告不能充当本次区间外结论的输入。

本报告的 [R] 是以下原输入：有限 Gauss/CRT/reciprocity 恒等式及其全部 zero
extensions、完整局部 correlation、primitive Hecke entireness/functional equation、
固定域素理想定理、理想/除子计数及 polynomial-size Euler-product bounds。
smooth calculus、Euler-kernel continuity和global logarithmic-control保持源中的
完整统一版本。没有重新认证外部文献或整个 math 项目。

## 2. 必须保留的 lemma 前件

沿源12492–12578，行仍是 `k∈O`、`0<q_k≪Z^m`，固定 twist 为
`ψ_k(n)=τ(n)χ_n(k)`，宽度 `M=m+q`。全部 displayed moving residue factors
的素数 support 在消去相位或模六约化之前计入 `q`；冗余零不变成常数1。
额外 puncture 只能在精确保留剩余相位后表示成一个 common squarefree mask，
且该 mask 对两个 plain factors 和全部 slots 相同，在当前行和内层 live labels
之前固定，范数最多是一个固定幂 `Z^B`。

`Θ` 是包含 fixed twists、reciprocity phases及 supplementary `χ_n(-1)` 的
固定有限群。资格条件按 **primitive inducing character** 判定：无 slot 时排除
principal，存在正长度 slot 时排除整个 `Θ`。不能以某个带零 presentation
是否等于 fixed presentation 代替此条件。

slots 的 underlying prime supports 在 imposed masks 之前两两不交；每个
coefficient 是 `Θ` 的固定有限线性组合，独立于 Z、当前行和移动 modulus。
令 `z=Σz_i`、`A=n_1+n_2+z`。扩域后的正长度条件仍准确为

\[
 n_1+n_2+6\kappa z=A+(6\kappa-1)z\le M.
 \tag{1}
\]

若 `κ<1`，仍必须假设

\[
 \beta_*\le\frac{1+\kappa}{2}.
 \tag{2}
\]

`κ` 在一次 lemma invocation 中是同一个参数，不能按当前行选择。
`κ=1` 的 endpoint 仍用 absolute counting，不需要(2)。所有零长度 slots 在
bounded scales 处先吸收到常数；`z=0` 分支仍允许任意 bounded plain lengths，
没有 conductor 下界。所有 length ranges 在 mesh 之前固定。

## 3. 全部 κ 数值使用点及新的精确余量

独立搜索并检查主体全部 `κ` 出现位置，没有在 local `F_2`、Gauss evaluation、
exceptional character counting 或 centered-lattice cancellation 中发现另一个
隐含 `κ≥3/4` 的数值使用。需改写和保持的地方如下。

| 原位置 | 实际需要 | `37/50≤κ≤1` 的验收 |
|---|---|---|
|12833–12901，prime bound|`s_κ=(1+κ)/2≥β_*`，fixed positive contour gap|`s_κ∈[87/100,1]`；global logarithmic-control 已对整个 compact `b∈[1/2,1]` 统一|
|12925–12938，terminal|`κz≤M/6`|由(1)及`A≥z`直接成立；旧未继续使用的`z≤2M/9`改成`z≤25M/111`|
|12947–12985，comparison|正 slots 中`z<M/20`，两条同 band comparison 有固定 margin|`6κ−1≥86/25`，故`z<25M/516=M/20−M/645`|
|14219–14285，greedy removal|除以`6κ`且overshoot只付一个slot|`κ>0`、`κ≤1`；`κd_z≤F_act/6+η`，完全保持|
|14818–14832，aggregate perturbation|`0≤6κ−1≤5`|新区间下界为`86/25>0`，上界仍为5|
|14865–14973，uniformity|固定 comparison margin、固定数值 Lipschitz、compact prime lines|以上余量允许沿原顺序一次选 mesh；无需在 moving labels 或 slot count 后重新选 mesh|

terminal 中

\[
 z\le\frac M{6\kappa}\le\frac{25}{111}M,
 \qquad \kappa z\le\frac M6.
 \tag{3}
\]

因此 floor 的额外指数仍是 `ρ/6`，原 terminal budget 不变。
旧 `2M/9` 的数值自身不在新区间成立，但全文没有在 terminal 后再使用它；
不能在重证时原样照抄这条粗界。

若 `A>5M/6`，则(1)给

\[
 z<\frac{M}{6(6\kappa-1)}\le\frac{25}{516}M<\frac M{20}.
 \tag{4}
\]

固定 `L=M/4` 的 comparison 仍有两条 plain lengths 至少 L。
用原 reflection calculation `A_comp≤3M/2−A+2z+ξ`，可保持原粗结果

\[
 A_{\rm comp}\le\frac{23}{30}M+\xi,
 \qquad A_{\rm comp}+(6\kappa-1)z
 \le\frac{14}{15}M+\xi.
 \tag{5}
\]

直接使用(4)则得到更精确且无需额外输入的

\[
 A_{\rm comp}<\frac{197}{258}M+\xi,
 \qquad A_{\rm comp}+(6\kappa-1)z
 <\frac{40}{43}M+\xi.
 \tag{6}
\]

两条所需 boundary 的共同 margin 至少 `3M/43>M/15`。
因此原 `ξ≤ρ/30` 足以让 comparison 调用同 band 已证明的 uncentered range，
不存在新的 same-band cycle。精确有理数核算：
`1/20−25/516=1/645`，
`5/6−197/258=1−40/43=3/43`。

## 4. 完整 transform 与递归并未改变

13125–13303 的 genuine whole-dyad localization 在原 full kernel 上先做，
依赖的是 bounded aggregate support、arbitrary Schwartz decay 和有限计数，
与 κ 无关。不能在 live columns 中插入一个 row-dependent sharp cutoff。
零频率 powerful-ideal count、第一 genuine complete common support 的
`B_c+B_d≤c+d−2p−R` 逐素数不等式均完全保持。

13442–13594 的 row enlargement 和 `hp^6` pool 保留原三项 valuation
`1,6,7` 修正；removal/moving-radical lengths分别是
`(iℓ_p,e_iℓ_p)`，`e_1=e_7=1,e_6=0`。
pool exponent `ℓ_*=σ/3`、`η<σ/6`、归一化 prime average 只用一次。
新 κ 不改变任何 Gauss coefficient 或局部 mask。zero row 仍仅在最后 smooth
ball 加入，不参与 amplification。

13596–14310 的第二 transform 先恢复全部 live slots 后平方，保留两个 inverse
roots、full smooth kernel及每个 shared-prime multiplicity。完整 support extraction
给 nominal

\[
 M'=M+J-g-g_2+t_2\le M-\sigma.
 \tag{7}
\]

actual enclosing/clipped width 至多增加原 `C_*ξ`，故仍严格降至少 `σ/2`。
残余 coprimality 以完整 squarefree Möbius indicator、完整 factor allocation
处理；不通过一个错用于 noncoprime pairs 的 CRT identity 替换。

actual child defect 包含全部 frequency enclosure、slot ratios、clippings 和 mask
deletion 后，仍有

\[
 F_{\rm act}\le6(w+\ell)+\delta_{{\rm fr},1}+2\theta_N.
 \tag{8}
\]

greedy prefix 只移除整 slots，从(8)直接得

\[
 \kappa d_z\le F_{\rm act}/6+\kappa\eta
 \le\Delta_{\rm child}+\delta_{{\rm fr},1}/6+\theta_N/3+\eta.
 \tag{9}
\]

这里没有用 `κ≥3/4`，也没有把 removed polynomial 的真实 coefficient 改成
新系数。若 slots 全消失，调用先完成的 unrestricted zero-slot child；不试图
把 arbitrary plain lengths 塞进 positive-slot affine range。

14312–14777 的 exceptional branch 用 induced `Θ` membership、完整 retained
zeros 和 local sextic residues 计数。`F_2≥2b_2/3` 的全部 local cases、
valuation-one nonunit 的额外 `f/6`、centered masked lattice leading coefficient
独立于 scale 和 norm twist的事实均 κ 独立。两 rectangle 的 equal product scales
及 common mask/norm power 保留至 main-term cancellation 完成；不能先按行
作不同 supremum。原最终 deficit

\[
 A-5M/6-2v/3-(M/4-v)_+\le(A-M)_+
 \tag{10}
\]

在正 slots 中仍为0，在 padded zero-slot core 中仍最多 δ。

## 5. 量词、mesh 与 height orders

原14779–14973的 finite induction 可完整保持如下顺序。

1. 固定 bounded length ranges 和最终 ε，先选 `ρ,σ,δ`，使原
   `T_term=ρ+δ+ρ/6+3σ+5σ/3<ε/4`。
2. 以原 strict decrease 定 depth D；选与 slot count 独立的 numerical `C_*`。
   再选 `ξ,η,ε_0`，满足原14876–14885，uniform于新区间全部 κ。
3. 此后才固定任意 finite slot count N、arithmetic datum、coefficient lists和
   profiles，形成一个 aggregate `H_N`，最终选 Z threshold 吸收
   `θ_N=H_N/log Z`。所有 removed subsets 共用同一 mesh。
4. small-power shares 可依赖固定 N；prime contour displacement 付的是
   `2ez`，不是 `2eNη`。每阶段只发生一次 normalized pool density和一次
   greedy overshoot；分支上只发生一次 terminal budget。
5. finite kernel/reflection/prime seminorm及 polynomial height orders沿 D
   stages反向固定；提高 external Fourier-tail order只提高外部输入 seminorm，
   不改变已固定的 internal height degree，也不引入 `Z^{Jξ}`。

global logarithmic-control 对 `s_κ≥β_*` 及一个 fixed positive gap 的常数在
`s_κ∈[87/100,1]` 一致。它使用 supremum definition 排除 `Re s>β_*` 的零，
不要求 supremum 被某个 target 达到。不能因此省略(2)，也不能把某个纯优化
reference `κ_*` 当成满足(2)的实际参数。

## 6. 结论和另一个作者报告的实际绑定

结论是重证原 plain estimate 的**参数范围扩展**，相对于§1列出的原 [R]
输入，保留全部 physical eligibility、共同 coefficient/mask、zero extensions、
mesh和height量词。读源证明没有留下新的 κ 数值障碍；本报告未将此结论
自动扩展到 inverse moments、detector witnesses、任何新 high saving 或无零半平面。

随后全文独立复核 radial_review 的
[独立主推导](hybrid-critical-count-witness-research.md)，共324行，canonical LF
SHA256 为

```text
a1a6146b8f5e0b82b0e7e642e323398aece00d0a3488cce3d6f146974332dff8
```

对该实际版本给**限定 PASS [T/R]**，范围是其明确保留底层输入的相对结果。
§3重证和本报告独立读源所得一致；§4 general crossing/strict widths及§5
反馈导数已重新计算，见下节。其§2 correctly保留 actual downward bins、
buffered prime upper bound及不同 witness/physical heights，不能靠这些上界排除
amplitude endpoint。旧 critical envelope 的唯一零点在降低合法 κ 后严格变负，
其 compactness 结论只是存在一个共同负 margin，没有认证新优化 root。

该稿§6新增 amplification 的范围是**固定有限个真实正长度 physical slots**。
在固定 K 和 bounded positive d 范围中，各 `P_i=U^(ℓ_i/d)` 一致趋向无穷，
eligible amplifiers排除 slot support 的费用确为 `o(P)`；若把它改读成任意
可随 U 缩到 bounded scale 的 slots，则此 `o(P)` 不由该证明给出。
在其实际限定下，`Q_(ua^6)=Q_u`、injectivity和marked widths保持，
`B_0=max{1,r+2z,(2r+8z)/3}`给所述相对估计。long branch中`r≥1,2z<1`
蕴含`B_0=r+2z`，附加 slot 斜率`5/3−2q≥11/12`，所以并未降低原长支
`α=5/6`。低幂 amplification 的 phase不自动保持，该稿只排除原 identity
不改便降幂的捷径。这些范围限定不可在引用时删除。

## 7. κ feedback 桥的独立有理计算

令`α=5/6`，`0≤δ≤3/4`、`0≤x≤1/2`。为避免与 width的 c 混淆，本节记
`a=1/(3κ)`，并置

\[
 B=2-2ax,\quad D=3-(1+2a)x,\quad P=B(1-x),
 \quad J=(\alpha-\delta)D+\delta P.
 \tag{11}
\]

两条实际 selected count lines为
`1−δ{x+(1−x)r}`和`1−δ{ax+B(t−r)}`，故直接解交点得

\[
 r_{*,\kappa}(t)=\frac{Bt-(1-a)x}{D},\quad
 t_\kappa=1+\frac{\delta P}{2J},\quad
 R_{*,\kappa}=1-\delta+\frac{(\alpha-\delta)\delta P}{2J}.
 \tag{12}
\]

`δ=0`时最后式仍有连续解释；当前矩形中`J>0`。
直接微分而非有限网格得到

\[
 \partial_\kappa R_{*,\kappa}
 =\frac{\delta(\alpha-\delta)^2x(1-x)^2}{3\kappa^2J^2}
 \ge0.
 \tag{13}
\]

用`J≥(α−δ)D`、`D≥2`、`x(1−x)^2≤4/27`及`κ≥37/50`，得到纯有理统一界

\[
 \partial_\kappa R_{*,\kappa}
 \le\frac{(3/4)(4/27)}{12(37/50)^2}
 =\frac{625}{36963}<\frac1{50}.
 \tag{14}
\]

由此，如果**另有** reference high envelope的连续证书
`E_(σ*,κ*)≤0`，且`κ*=2σ*−1≥37/50`、`h<1`，在反证
`β*>σ*`及已知bootstrap `β*≤7/8` 下，实际参数应取
`κ_act=2β*−1`。它满足positive plain的全族前件，且

\[
 \kappa_{\rm act}-\kappa_*=2\Delta,
 \qquad \Delta=\beta_*-\sigma_*>0.
 \tag{15}
\]

对全部 `0≤d≤h`，新count的反馈费用至多`d·2Δ/50<Δ/25`。
从reference `C_b(σ*)`转到真实`C_b(β*)`本来精确减去Δ，故仍有
`24Δ/25`的central gap可先于target支付real/mesh/rounding losses。
这没有将reference κ*代入实际prime estimate，没有重复扣除Δ。
本节只认证feedback桥；连续critical polynomial、所有physical d、principal、
outer及family continuation仍须在新的主稿中分别验收。
