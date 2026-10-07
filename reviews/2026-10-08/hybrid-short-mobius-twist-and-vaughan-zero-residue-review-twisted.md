# 原短 Möbius twist 与 Vaughan 零点留数：独立全文审查

2026-10-08。审查人：twisted_research。结论：**限定 PASS**。
已实读作者稿全部113行，并对照冻结的原 Vaughan 系数及共同 product cutoff；没有改动被审稿、旧稿或数学仓库。

## 1. 最终字节绑定及范围

规范化只作 UTF-8 解码、CRLF→LF、孤立 CR→LF；不 trim，不删除末尾换行。

| 文件 | canonical LF SHA256 | 字节 / 行 |
|---|---|---:|
| [被审作者稿](hybrid-short-mobius-twist-and-vaughan-zero-residue-research-radial.md) | a970366e68b8d3526c0dadac49b8ee8f4a7b6984e763712a851f8b6d353a291d | 6064 / 113 |
| [冻结的原 Vaughan 准入与完整 Type II 剩余](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 | 12260 / 324 |

此次批准两个具体结论：普通 ζ 的固定 buffered 无零输入下，原 sharp 短 Möbius 多项式的正高度统一准入；完整实际 Vaughan 剩余在 ζ 零点处的留数仍为原重数的负值。没有证明完整 Type II 四矩的新上界、比例或无零条带，也没有认证 Lean 形式化。

## 2. Reciprocal buffer 与常数量词

输入严格为普通 ζ 无零于 \(\Re s>\theta\)，其中 \(1/2\le\theta<1\)。先固定 \(\delta>0\)；需要时选更小的正 buffer 来覆盖较大的目标 \(\delta\)。作者的四个半径满足
\[
0<r_0<r<R_1<R_2,\qquad
2-R_2=\theta+\delta/4>\theta.
\]
大高度圆盘不含 pole \(1\)，故可从中心 \(2+iv\) 的 Euler 值选同一解析 \(\log\zeta\) 分支。固定实部带的多项式增长只给 \(\Re\log\zeta\) 的上界，足以与中心的有界 Euler 值一起应用 Borel–Carathéodory；不需要先假设 reciprocal 的次幂界。

小盘在 \(\Re s\ge3/2\)，故 Euler 级数给整个小盘上的有界 \(\log\zeta\)。三圆定理的指数
\[
b_\delta=\frac{\log(r/r_0)}{\log(R_1/r_0)}\in(0,1)
\]
正确。以同一个高度 \(v\) 为中心，实轴方向的半径 \(r\) 覆盖 \(\theta+\delta\le\sigma\le3/2\)；更右侧由 Euler 级数处理。因而
\[
|\zeta(\sigma+iv)^{-1}|
\le C_{\theta,\delta,\eta}(1+|v|)^\eta,
\qquad \sigma\ge\theta+\delta,
\]
对任意固定 \(\eta>0\) 成立。有限高度部分的 \(1/\zeta\) 在该区域解析，ζ 的 pole \(1\) 是 reciprocal 的零，不能列作 reciprocal 极点。

这里得到的是带固定正 buffer 的次幂费用；没有把未知的临界线 reciprocal 当作输入。常数可以依赖固定 \(\theta,\delta,\eta,a\)，不依赖当前 \(W,t,T\)。

## 3. 实际 sharp Perron 与全高度统一性

\(w^\sharp=\lfloor W\rfloor+1/2\) 保留全部原整数 \(n\le W\)，且每个整数距离端点至少 \(1/2\)。初始线的 reciprocal Dirichlet 级数绝对收敛，因为
\[
\Re(1/2-it+z)=1+1/\log w^\sharp.
\]
近端 Perron 误差按 \(|n-w^\sharp|^{-1}\) 的 harmonic sum 付款；远端的绝对级数费用可由原 \(|\mu(n)|\le1\) 支付。因此作者的
\[
O\!\left((w^\sharp)^{1/2}\log^2(2w^\sharp)/T^2\right)
\]
覆盖全部端点和尾，未使用半权或改变 cutoff。

移线后 \(\Re z=\theta-1/2+\delta>0\)，全矩形上的 reciprocal 实部至少 \(\theta+\delta\)。没有跨过 \(z=0\) 或 ζ 零点；ζ 在 \(1\) 的 pole 不产生 reciprocal 留数。实际虚部可以达到 \(O(T^2)\)，所以必须先取上述 \(\eta\) 小到 \(2\eta<\varepsilon/2\)，再取 \(T\) 大；作者的量词允许这样做。

左线的 \(1/|z|\) 积分是 \(O_\delta(\log T)\)。水平线长度有界、\(|z|\asymp T^2\)、\((w^\sharp)^{\Re z}\ll (w^\sharp)^{1/2}\)，给出的水平费用一致。因 \(W\le V\le X^a\)、固定 \(a<1/4\)，水平项与 Perron 误差均可吸收。\(1\le W<2\) 时原整数集合只有 \(n=1\)，直接处理；作者的 \(W=1\) 按其整数 cutoff 约定正是这个情况。故最终
\[
\sup_{t\in[T/4,4T]}|G_W(1/2-it)|
\ll W^{\theta-1/2+\delta}T^\varepsilon
\quad(1\le W\le V)
\]
是原 sharp、原正高度对象的统一结论。

## 4. 完整 \(C_4\) 系数与普通零点留数

逐项核对作者式(4)。\(\zeta G_V\) 的第 \(k\) 个系数是
\[
b_V(k)=\sum_{\substack{d\mid k\\d\le V}}\mu(d).
\]
当 \(1<k\le V\)，全部除数都在范围内，系数为零；当 \(k=1\)，系数为 \(1\)，被 \(1-\zeta G_V\) 的单位项抵消。故 \(1-\zeta G_V\) 在 \(k\le V\) 全零，在 \(k>V\) 为 \(-b_V(k)\)。
\(D_\zeta-F_U\) 正好保留 \(m>U\) 的 \(\Lambda(m)\)。这证明未截断乘积严格给原负号的 \(m>U,k>V\) 系数，只有共同的两端 Perron 差才产生 \(Y<mk\le X\)。没有把斜 product cutoff 改成两个独立的矩形截断。

展开时 \(D_\zeta\zeta=-\zeta'\)，故
\[
(D_\zeta-F_U)(1-\zeta G_V)
=D_\zeta-F_U+\zeta F_UG_V+\zeta'G_V
\]
的符号正确。若普通 ζ 在 \(\rho\) 有重数 \(m_\rho\)，\(D_\zeta\) 的留数为 \(-m_\rho\)，其余三项在 \(\rho\) 解析。因此完整系数的留数仍为 \(-m_\rho\)，包括多重零点。

两端的 half-integer 保留原 \(Y<mk\le X\) 集合。核
\[
K_{X,Y}(z)=\frac{(x^\sharp)^z-(y^\sharp)^z}{z}
\]
在 \(z=0\) 可去，值为 \(\log(x^\sharp/y^\sharp)\)；这不删除 \(\rho=1/2-it\) 的实际零点贡献。采用有限矩形且避开边界零点时，每个跨过的零点贡献正是
\(-m_\rho K_{X,Y}(\rho-(1/2-it))\)。正 \(t\) 对应的负虚部零点仍在同一个普通 ζ 对象内，没有丢掉共轭侧。

## 5. Pole \(1\) 的精确主部与费用

令 \(z=w-1\)。\(\zeta'(w)=-z^{-2}+O(1)\)，所以
\(\zeta'G_V=-G_V(1)z^{-2}-G'_V(1)z^{-1}+O(1)\)；
\(D_\zeta=z^{-1}+O(1)\)，而 \(\zeta F_UG_V\) 的简单 pole 系数是 \(F_U(1)G_V(1)\)。因此作者的 Laurent 主部
\[
-\frac{G_V(1)}{z^2}
+\frac{1-G'_V(1)+F_U(1)G_V(1)}{z}
\]
和相应 \(-G_V(1)K'(1-s)\) 的导数符号都正确；Euler 常数不产生遗漏的简单 pole。

原 \(t\asymp T\asymp X\)、\(Y<X\) 下，
\[
|K(1-s)|\ll X^{-1/2},\qquad
|K'(1-s)|\ll X^{-1/2}\log X.
\]
\(|G_V(1)|\ll\log X\)、\(|G'_V(1)|\ll\log^2X\)，并由基本 Chebyshev 上界和 Abel 求和有 \(F_U(1)\ll\log X\)。故未归一化 pole 项为 \(O(X^{-1/2}\log^2X)\)，除同一 \(a_\ell\ell\) 后是 \(O(X^{-1/2}\log X)\)。这与普通零点项分开，并未宣称抵消 top zero packet。

## 6. 可接受结论与仍未付对象

本稿真实新增的是原短 Möbius 点值准入；不能把它再套入一个已经依赖 \((m,k)\) 的误差，以认领第二次相消。完整 \(C_4\) 的四份系数、全部 aspect ratio、共同 product cutoff 和正高度联合矩仍须实际估计。短 \(G_V\) 在普通零点处没有减幅，故原绝对 zero-packet/density 估计的 top 项也不能仅凭此消失。

这些判断只限制所列具体搬用，不是 actual Möbius/prime 相消不存在的断言。六邻域比例机制与此准入独立。审查没有运行或生成新的数值证书；此处 PASS 来自逐式数学检查和最终源绑定，不宣称新的 whole \(M_{C_4}\) saving。
