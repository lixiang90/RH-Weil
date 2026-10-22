# C037 独占证明：实际双位覆盖上的指数 clutch 核、相对 frame 与度量

2026-10-22。root 已据以下明确新对象／可判测试决定准入 C037 一轮；本稿不改 STATE/cadence，
由 root 与其他独占稿、fresh 审核统一消费结算，不另计文件／分支轮。
413 是已付实际几何输入；这里此前未给出的精确 Čech kernel 不是“所有 Pic 为零”，也不以旧 source quotient 为 base。
下列定理只分类一个明确一参数子族；不主张外部首创，不计算整个 Picard 群。

## 1. 实际对象、覆盖、线族与既定 frame

固定不同有限素数 p,q，L=log p、M=log q；L/M 无理。
完全使用 [413](../../../notes/413-f1-two-place-boundaries-and-virtual-class-collapse.md) 的实际半局部紧单位商：

\[
T=\mathbf Z\cup\{\infty\},\quad
Y=T^2\times\mathbf R_t,\quad
\Gamma=\mathbf Z^2,
\quad(a,b)(j,k,t)=(j+a,k+b,t+aL+bM).
\]

O=Y\D，D={(∞,∞)}×R。两个 Γ 不变开片 Wp={k有限}、Wq={j有限} 覆盖 O，
交 B=Z²×R 上有 Γ 不变坐标

\[
x=t-jL-kM.
\]

每一单边为 proper Γ 空间，商为 Z_L 或 Z_M，交商为 R；整个 O 上 Γ 作用非 proper。
Z_L 的负端附加整个圆 `[s]∈R/LZ`，正端无附加点；其拓扑由

\[
x\mapsto(e^x,e^{2\pi ix/L}),\qquad[s]\mapsto(0,e^{2\pi is/L})
\tag{1}
\]

给出，Z_M 同理。这些准确输入已在 413 完整审查，不将整个 O 换成 Hausdorff proper quotient。

对任意 z∈C，在 Wp、Wq 各取一条具有 trivial Γ fiber action 的平凡复线，
在 B 上以 Γ 不变 transition

\[
g_z(x)=e^{zx}
\tag{2}
\]

粘成等变线 \(\mathscr L_z\)。有限 x 上 g_z 无零，故 transition 及逆均为真实连续函数。
在任意参数 base S、连续参数 z:S→C 上同式给 O×S 上的实际线族，普通连续 base change 就是替换 z。
这是一族连续等变线；不把它冒认为 adelic regular／algebraic 线、完整 C* 代数投影或算术截面族。

闭边界 P={∞}×Z×R、Q=Z×{∞}×R 在 O 中不相交。
Wp 的常数 frame 给 \(\mathscr L_z|P\) 一个既定 frame，Wq 的常数 frame 给 \(\mathscr L_z|Q\) 一个既定 frame。
若消费 relative Pic，以下明确要求保持这两个 frame；不能用 absolute Pic 的 gauges 偷换。

## 2. 一个拓扑引理：side unit 的负端是周期 unit 的一致渐近

设 a 是 Z_L 上的连续无零复函数，A(x) 是其边界限制的 L 周期提升。
则

\[
\sup_{x\le-R}|a(x)-A(x)|\longrightarrow0\quad(R\to\infty),
\tag{3}
\]

且充分负端上存在常数 0<c≤|a(x)|≤C<∞。
证明：(1) 中的整个负端加圆是紧集；边界函数连续且无零，在圆上有正最小模。
若 (3) 失败，取 x_n→−∞ 的坏点，圆相位取子列收敛；(1) 给 a(x_n) 与 A(x_n) 趋同一边界值，矛盾。
这只用连续性，不需要 side unit 在正端有界／有极限。

反过来，任何连续 L 周期无零函数 A(x) 由同一周期函数在负端圈上延拓为 Z_L 的 unit。

## 3. 主定理：absolute kernel 精确为 iΛ

记

\[
\Lambda=\frac{2\pi}{L}\mathbf Z+\frac{2\pi}{M}\mathbf Z.
\]

**定理。** 对任意 z,w∈C，

\[
\mathscr L_z\simeq\mathscr L_w
\ \text{作为连续等变线}\quad\Longleftrightarrow\quad
z-w\in i\Lambda.
\tag{4}
\]

证明只需 w=0，因为张量／取对偶分别对应指数相加／相减。
所有等变线同构均覆盖 **固定 O 的恒等映射**，不允许另作 base 自同构重参数。
线平凡，当且仅当存在两个 side unit a∈C(Z_L,C×)、b∈C(Z_M,C×)，使

\[
e^{zx}=a(x)/b(x).
\tag{5}
\]

这是本实际两片平凡化的 Čech coboundary 判据；任一全局等变 frame 的两个系数必为 Γ 不变函数，所以不遗漏可用 gauges。
由 §2，右侧在充分负端的模有正上下界。若 Re z≠0，左侧在负端趋 0 或 ∞，矛盾。
故 z=iλ，λ实。

令 A、B 为 a、b 的负端周期 limits。由 (3)、正下界以及 (5)，

\[
e^{i\lambda x}-A(x)/B(x)\longrightarrow0\quad(x\to-\infty).
\tag{6}
\]

以下说明这个渐近恒等式实际处处成立。存在 t_n→+∞ 使

\[
e^{-i\lambda t_n}\to1,\quad
e^{-2\pi i t_n/L}\to1,\quad
e^{-2\pi i t_n/M}\to1.
\tag{7}
\]

可仅取 t_n 为整数：在紧三维环面上把整数轨道分成小网格，pigeonhole 给接近单位元的正差；
若得到的近回归整数无界，取子列即得；若有界子列反复满足任意精度，则某个正整数为精确周期，取其倍数即可。
这是有限维紧性／Dirichlet 同时逼近，不用任何 RH、谱纯性或素数零点信息。

对固定 x，把 (6) 用于 x−t_n。连续周期 A、B 的一致连续性以及 (7) 给

\[
e^{i\lambda x}=A(x)/B(x)\qquad\text{每个 }x\in\mathbf R.
\tag{8}
\]

取 A、B 的绕数 m、n，周期单位的标准 lift 给

\[
A(x)=e^{2\pi imx/L}e^{a_0(x)},\quad
B(x)=e^{2\pi inx/M}e^{b_0(x)},
\]

a0、b0 为有界连续周期复函数。由 (8)，

\[
i(\lambda-2\pi m/L+2\pi n/M)x-a_0(x)+b_0(x)\in2\pi i\mathbf Z.
\]

左边连续，故为一个常数；a0、b0 有界，迫线性系数为零。
因此 λ∈Λ，必要性闭合。

反之，若 λ=2πm/L+2πn/M，两个周期单位分别延拓到两侧，
用其中一个或其逆选 a、b 便满足 (5)。充分性闭合。

**具体非平凡见证。** z0=iπ/L 不在 iΛ：若 `1/2=m+nL/M`，L/M 无理迫 n=0，又迫整数 m=1/2，矛盾。
故 \(\mathscr L_{i\pi/L}\) 是真实非平凡线，且同样可在保留实际 source 的群胚上叙述。

## 4. 保两边界 frame 的 relative kernel 为零

保持 §1 两个既定 frame 的相对平凡化，在 (5) 中还要求 a|P=1、b|Q=1。
§2 此时给 a(x)→1、b(x)→1，故 `e^(zx)→1` 当 x→−∞。
这当且仅当 z=0：Re z≠0 的模不符；纯虚非零 λ 有振荡序列，不能收敛到 1。
因此

\[
(\mathscr L_z,\mathrm{fr}_P,\mathrm{fr}_Q)
\simeq(\mathscr L_w,\mathrm{fr}_P,\mathrm{fr}_Q)
\iff z=w.
\tag{9}
\]

这是真实的 C 参数相对线子族。absolute 中杀掉 iΛ 的周期 gauges 会改变边界 frame，故不能用于 (9)。
本处“relative Pic”明确指 **带所选边界 trivializations 且同构保持它们**；
仅要求边界限制可平凡而不固定 frames 的 `ker(Pic(O)→Pic(P⊔Q))` 仍使用 (4)，不获得 kernel0。
保留 frame 不是免费恢复目标：它增加了明确刚性数据，物理全 Pan 必须在这种更强相对意义下另验。
不能把 arbitrary z(r) 标记本身当作独立 RR／Weil 正性。

## 5. Γ 不变连续正 Hermitian metric 的准确门

若 \(\mathscr L_z\) 有全局 **Γ 不变** 连续正 Hermitian metric，在两边既有等变平凡化里分别为 Γ 不变正连续 h_p、h_q，因而下降到 Z_L、Z_M。
每个负端圆紧，且 metric 在边界正，故 h_p、h_q 在充分负端各有正上下界。
transition compatibility 按 frame 方向给 `h_p/h_q=|g_z|^2` 或其逆；两种约定均迫 Re z=0。
因 Re z非零时该比例趋0或∞，不可能。

反之 Re z=0 时 `|g_z|=1`，在两片取 h_p=h_q=1 即为实际全局 Γ 不变连续 unitary metric，且两个边界 frame 均 unit length。
所以

\[
\mathscr L_z\text{ 有全局 Γ 不变连续正 Hermitian metric}\quad\Longleftrightarrow\quad\Re z=0.
\tag{10}
\]

这是一条关于 **本实际非 proper 覆盖上等变 metric** 的新准确限制；不是所有 adelic 几何的无度量定理。
底层 O 是局部紧第二可数 Hausdorff 空间，允许 partition of unity 的非不变 metric 不在此排除范围。
需要的是作用等距／metric 下降这一明确前件；不能略掉它再声称连底层正 metric 都不存在。
它也不是 Weil 正性：即使纯虚子族的 fiber metric正，也没有同源 global sections／RR 容量或完整 Weil budget identity。

## 6. 非 Hausdorff、同伦及 K/Pic 范围

因 L/M 无理，Λ 在 R 稠密。故纯虚 absolute character 子族的自然参数商 iR/iΛ 为 indiscrete；
复子族自然商 C/iΛ 的 Hausdorff 可分辨方向只有 Re z。
这只描述本子族的参数 quotient topology，不宣称整个 Picard stack 的拓扑／完整分类。
若保边界 frame，则 (9) 的参数 C 本身保留，但必须负担相对数据的来源和范数。

`s↦𝓛_(s z0)`，s∈[0,1]，由 O×[0,1] 上同一个 transition `exp(s z0 x)` 给实际连续族；
起点平凡而终点可非平凡。因此这里不能自动使用 paracompact Hausdorff base 上的线丛同伦不变性。
原因不是公式失效，而是当前 equivariant／非 proper base 的对象类别不同。
本线并非 C0(O) 中的有限支投影，亦不提供 413 projectionless 稳定理想中的非零投影；
它与 410/420 的 K 检测线是不同对象，不能用本族推翻旧 K 计算。

## 7. 物理源接口及真实停止范围

从 r=e^(u/2)f、r∈S_exp,C 选一个实际复线性 scalar ℓ(r)，便可给
`r↦𝓛_(ℓ(r))` 的实际线族。
若要求消全部 physical Pan，利用 (4) 及所有 t q∈Pan（t复），
线性 ℓ 必须精确消 Pan：因为 `C·ℓ(q)⊂iΛ` 仅在 ℓ(q)=0 时可能。
保边界 frame 时由 (9) 得相同必要条件。
因此选 scalar **不是**已经给 nonroot-faithful source bridge；它必须独立通过全关系、r0 和原费用。

边界／双 degree 的现成候选 ℓ=µ+ 或 µ− 精确消全 Pan，却杀双 moment零的 537 r0。
裸 mean ℓ=∫r 固定窗有费，却由405 `P=(D²−1/4)H` 的严格负 mean 失败全 Pan。
Mellin／zero-jet 标量泛函可以读旧 quotient 坐标；足够全部必要 jets 的忠实 joint 读出归519/520，不能称单 scalar 忠实整个商。
按本次用户停止条件，这种重新标记不升级为独立算术移动。
非线性 `z(r)=i c Qζ(r)` 更能通过全 Pan 和 537 非根：取 `c=π/(LQζ(r0))`，正好送到 iπ/L 非平凡线。
其 fixed 窗 Dlog 坐标费用来自旧完整 form bound；它明确只是把欲证明正性的原 Q 装入 Pic 参数，
不是独立容量。不能据此声称不存在任何实际源 map，也不能把 unitary fiber metric 当作 Q≥0。
Q-marker 并非 addition→tensor 同态；伴随稿给 `r0/√2` 的实际 absolute 反例，
并保连续两号系统的 `Q_c` 标签都具有 unitary metric。完整 Γ 的 fixed 窗原费用只能报 Dlog form bound，不能改报纯 du bound。
完整 source／norm 测试、全 Γ／prime powers／pole 目标和函数域对照见[伴随消费稿](boundary-cover-and-existing-lines.md)。

本次新几何净输入是 (4)、(9)、(10) 的实际子族精确 kernel 与 metric 门；
它改善“没有非平凡 relative Pic 数据”的不准确描述，但不消除 source scalar 的全 Pan／nonroot／费用耦合、整性过滤或 RR 容量。
本族尚无从独立算术几何得到的 degree 函数；纯虚 transition 和 unitary fiber metric 不自动成为函数域意义的 `Pic0` 或正极化。
不因 contract 一轮结算而完成宏观 Goal，也不延长为单 scalar、固定线 tensor 或 old quotient 调参。
