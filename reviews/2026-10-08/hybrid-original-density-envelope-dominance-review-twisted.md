# 原坏行密度与最终联合包络：独立全文审查

2026-10-08。结论：限定 PASS。独立实读被审稿全部 151 行，以及冻结
450 的 actual crossing 和 451 的实际 κ 反馈；没有发现阻断。审查
比较的是现有包络和候选密度指数，不认证全 sixth-power-free 密度的
新准入，也不把不能直接改善边界说成新密度没有其他价值。

## 1. 最终字节绑定

canonical LF 只作 CRLF/lone CR→LF，不 trim、删 EOF 或尾空白。

| 文件 | canonical LF SHA-256 | canonical bytes / 行 |
|---|---|---:|
| [被审完整源](hybrid-original-density-envelope-dominance-research-root.md) | 6e1352c0f4660239c13f02bad622384c51e2df0035a5739743cb2bc78f76961e | 6103 /151 |
| [450](../../notes/450-plain-kappa-extension-and-actual-capacity.md) | f16807e0f80461e3005b3173e313218b00f5f86abfa860a4ead79e425dd6bee5 | 5431 /122 |
| [451](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 | 10207 /244 |

另独立浏览一手 [BGL 原文](https://arxiv.org/pdf/1112.1650)，核了
Corollary 1.6 的 squarefree family、两段指数及 §2 的 primitive
约定。该文原结论没有自动覆盖本项目所有 sixth-power-free
presentations；本审查没有把它当作这项尚待重证的实际行输入。

## 2. 被比较的 actual 对象与前提

450 的包络是同一个零点产生的 inverse/plain witnesses，以及其实际
positive slots 和合法 amplification 的最终联合指数。这里的
$a$ 是 buffered row bin，$\delta=2a-1$，$x=q/\delta$ 是原全部
槽的加权 mean amplitude；并非把全族 $\beta_*$ 填成每行的 $a$。

分析使用 $R_{*,\kappa}$ 仍限于同一 [R]、原 finite coefficients、
masks、strict widths、height allowance，以及
$\beta_*\le(1+\kappa)/2$ 的实际前提。代数证明可在
$37/50\le\kappa\le1$、$0\le x\le1/2$ 全域进行。above-floor
实际应用为 $1/50<\delta\le3/4$；闭端点 $1/50$ 仅延拓代数，
实际 floor 没有 guaranteed witness，仍单独付 $\#\mathrm{rows}\ll U$。
被审稿已明确这一差别。

## 3. 全域包络 upper 的独立复算

写 $c=(3\kappa)^{-1}$、$\alpha=5/6$。直接展开得到

\[
 2D-3P=2x(2+c-3cx).
\]

在 $c\in[1/3,50/111]$、$x\le1/2$ 上，括号至少
$2-c/2>0$，故 $P/D\le2/3$，且 $D,P>0$。
又 $\alpha-\delta\ge1/12>0$。函数

\[
 t\longmapsto
 \frac{(\alpha-\delta)\delta t}
 {2(\alpha-\delta+\delta t)}
\]

在 $t\ge0$ 上递增；取 $t=2/3$ 后原 $R_*$ 准确化为

\[
 R_{*,\kappa}\le r_0(\delta)
 =\frac{15-16\delta}{15-6\delta}.
\]

$x=0$ 取等仅说明这个 worst-$x$ upper 尖锐，不能把高指数中
带有 $q=\delta x$ 的实际优化角落改成 $x=0$。
该推导没有冻结错误的 κ，没有调用任何新增算术估计。

## 4. 两段差及显式 margin

独立 Sympy 有理约分重新核了三个恒等式：
$2D-3P$、低段差、高段差；检查未改任何源文件。
低段准确为

\[
 g-r_0=\frac{\delta(25-24\delta)}
 {(4-3\delta)(15-6\delta)}.
\]

对 $[1/50,2/3]$，分子至少 $(1/50)9$，正分母至多
$4\cdot15=60$，因此差至少 $3/1000$。

高段准确为

\[
 g-r_0=
 \frac{-\delta(18\delta^2-24\delta+5)}
 {3(2\delta-5)(3\delta^2-6\delta+2)}.
\]

分母等于
$(15-6\delta)(6\delta-3\delta^2-2)>0$。二次式的导数
$36\delta-24\ge0$，其区间最大值为 $-23/8$。
分母的两个因子分别不超过 $11$、$13/16$，于是

\[
 g-r_0\ge
 \frac{(2/3)(23/8)}{11(13/16)}=\frac{92}{429}.
\]

两段在 $\delta=2/3$ 均为 $g=2/3$。全部符号、分母和 margin
在显示连续域内成立，没有用有限采样代替全域证明。

## 5. 含义及尚未认证的接口

由 $g>r_0\ge R_*$，即使全原始行族以后完整得到精确 BGL 指数，
在同一数据、高度和 masks 下直接取 $\min\{g,R_*\}$ 仍是
$R_*$。正高度幂、正小损失无法反转严格大小。
在 $\delta=3/4$ 处，$r_0=2/7<7/13$；在唯一边界等号行
$a_*\approx0.694291677133$ 处，$g(a_*)\approx0.862897>2/3$。
两处数值和全域结论相容，均未把 row bin 与最高零点实部混同。

本稿足以排除“仅更换无槽 raw 密度指数便改善现有边界”的直接
优化方案。它不排除新的 marked density、density 与原 amplification
的联合估计，也不排除改 detector；这些必须从实际同角色/同高度/
同掩码重新证明，不能机械取幂。472 的共同短载波 P 桥作用于标量
prime response，不提供这种角色族 joint moment。

审查没有证明新行族 AFE/密度估计、原 [R] 全包、外部整篇论文、
新的简单临界线比例、Lean 或 RH。被审源的范围准确；限定 PASS。
