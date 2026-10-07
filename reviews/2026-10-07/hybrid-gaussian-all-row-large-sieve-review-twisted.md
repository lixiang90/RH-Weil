# 458：Gaussian 全元素行大筛的独立审查

2026-10-07。结论：**限定 PASS**。全文重核被审稿的实际矩阵、外部
角色族前件、全部元素行分解、两个大筛方向、尺度 supremum 及放大
比较，没有发现阻断其未加 marks 结论的数学缺口。本审查不是 Gaussian
完整反射、原 marked/plain 递归或新无零区域的认证。

## 1. 文件与引用范围

被审稿：[notes/458](../../notes/458-gaussian-all-row-large-sieve-comparison.md)。
读取版本的 canonical LF SHA256 为
`3ee821601d6e1d5da38c8235586981b28d7ebee5a5f28691a98d869834dcc8ac`，
9964 UTF-8 bytes，246 行。规范化仅把 CRLF、lone CR 转为 LF，不 trim。

同步核读已冻结的 [Gaussian probe](hybrid-gaussian-root-weight-probe-research.md)
（`4a6b33cae1944bc904216c202a62f04d48d2f47b0ff5a852f13a3af5a063bc3d`）
及 [457](../../notes/457-number-field-choice-and-relative-amplification.md)
（`75079970955602644a9290709f66e2be331ad6116d2a637ed8fc97fb0dde5791`）。
原来源是只读的
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，
canonical LF SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。
其 12343–12360 行是全实际元素行的 raw 合同，12362–12465 行是
sixth-power-free 放大与 profile/height 量词；没有把 October-5 的不同
paper2 路线作为同一输入。

外部文献已经浏览原文：

- [BGL, Theorem 1.3 与 Appendix II](https://arxiv.org/pdf/1112.1650)：
  两侧 squarefree ideals、固定坏处及任意列系数的高阶大筛。
- [GL, Definition 1、Remark 3、Corollary 1.2 与 §2](https://arxiv.org/pdf/1112.1642)：
  将四次 Hecke family 平方为二次 family，及其大筛。
- [DDHL v5, §3 与 Theorem 5.1](https://arxiv.org/html/2306.11875v5)：
  实际 primary 互反律及 Gaussian 二次大筛的直接交叉核对。

它们不是关于任意 target 的 metaplectic completed functional equation。
本次也没有使用 rational Dirichlet quartic 大筛替换 Gaussian ideal 大筛。

## 2. ordinary quartic symbol 与 Hecke family

直接把 `(a/n)_4` 读成一个未处理单位的理想字符确实不充分；本处可以
明确完成这个接口。取 `K=Q(i)`，BGL 的固定坏集只需含 lambda。因为
Gaussian class number 为 1，可在其 Appendix II 的构造中把每个理想
代表 E 的元素 m_E 选为 primary generator e_E。对 primary a，构造中

\[
 (a)=(x)E\mathfrak g^4,\qquad x\equiv1\pmod{\mathfrak c}
\]

的元素 x 也是 primary，且 E 与 g 均取 primary generators。
于是 `a=x e_E g^4`；单位为 1，因为两端 primary。构造的 Kummer
元素 `m_(a)=x e_E` 与 a 相差四次幂。因 g 与待评估理想互素，得到

\[
 \Xi_{(a)}((n))=(a/n)_4
\]

在互素奇理想上准确成立；非互素奇部，两端都是零。平方自由 a 的
奇 conductor 正是 `(a)`，可能另有固定 lambda-part，infinite type
为 trivial。因此实际 a 方向直接是 BGL 的矩阵。若采用反向 family
记号，先固定有限 ray sectors，再用互反律转置，费用也是固定常数。
没有新的 conductor 参数，也没有假设 eta 属于这一 family。

最终正文新增的 primary 互反符号
`(-1)^(((Na-1)/4)((Nn-1)/4))` 与 DDHL §3 相同；平方后消失。
DDHL Theorem 5.1 对实际 squarefree Gaussian 二次符号给出 `M+N`
宽度，primary 行列属于它的 odd 行列，故正文的直接交叉核对也成立。

同一族的平方给
`Xi_(n)((b))^2=(n/b)_2=(b/n)_2`：最后一个等式是 primary Gaussian
二次互反律；亦可先保留有限 sectors。GL Corollary 1.2 的 `n=4`
遂准确覆盖真实 b 方向。平方角色在每个奇 prime 仍 nonprincipal
primitive，不能将 quartic 方向整体称作 quadratic。

epsilon_chi=-1 时先将整个和共轭，再共轭列系数，两个大筛范数不变。
任意 eta、norm imaginary twist 和固定因子的自然零掩码全部保留在
绝对值不超过 1 的列权重中；这一估计无需对 eta 作反射。

## 3. 全部元素行与每箱费用

逐 prime valuation 模 4 分解
`u=zeta lambda^v a b^2 c^3 r^4` 是唯一的。a,b,c 奇 squarefree 两两
互素；r 可与前三者重叠。`chi_n(r)^4=1_(n,r)=1`，所以 r 不能
作为无条件 principal 因子删掉。lambda^v 与四个 units 固定后，均
进入列系数，不删除含 ramified prime 的实际行。

写 `V=U/2^v`，dyadic norms `A,B,C,R>=1`，非空箱满足
`A B^2 C^3 R^4<=V`。固定 b,c,r 的列平方能量是 `O_W(1)`；固定
a,c,r 同样成立。这使用 Gaussian ideal count，含单位理想，不需要
prime number theorem。删去 pairwise 行限制是在非负外和中扩大
行集合；留下的字符仍有非互素零值，固定 r 的列 mask 没有删除。

因而两个准确的箱上界分别为

\[
 BCR\{A+D+(AD)^{2/3}\}(VD)^\epsilon,
 \qquad ACR(B+D)(VD)^\epsilon.
\]

若 B<=A 取第一式，否则第二式。以下是逐箱不等式，非数值网格验证：

\[
 ABCR\le V,\qquad \min(A,B)CR\le V^{1/3},
\]

\[
 BCR(AD)^{2/3}
 =(DAB^2C^3R^4)^{2/3}B^{-1/3}C^{-1}R^{-5/3}
 \le(VD)^{2/3}.
\]

第二个不等式由 `min(A,B)^3<=AB^2` 及 `R^3<=R^4` 得到。
O(log(2V)^4) 个箱先以较小 preliminary epsilon 控制，再吸入目标
epsilon。v 和的三个正指数 1、2/3、1/3 几何可和，四个 units 只
给固定倍数。因此 (2) 真正包括全部非零 u，且常数不随 eta 导子增长。

## 4. scale supremum 与放大的准确范围

§5 不能从点态二矩直接交换 supremum；被审稿实际用了 t 的 Sobolev
不等式。`D'=tD_j,1<=t<=2` 时 profile 与其 t 导数仍支撑在固定倍
D_j 上，列能量均有统一 `O(1)` 界。固定 t 先应用两个二矩，再
积分；加 O(log(2D)) 个尺度。D' 小到没有 norm>=1 的理想时为零，
其余常数尺度可并入。由此证明的是同一个固定 profile 的 supremum；
没有据此省略另需支付的 rowwise height / angular 参数量词。

最终 §6 已显式继承 457 的 **fourth-power-free u** injectivity
前件。任意全元素 u 的乘法映射 `(u,a)->u a^4` 本身并不单射；
全行二矩用来控制放大后的行，而被放大的原行是 fourth-power-free。
因此 `/P` 没有被扩大为所有原行的结论。此次补明已从最终磁盘全文
核验，不是仅在审查中追加解释。

在这一合法范围内，令 `P=(H/U)^(1/4)`，三个上界项除 P 后为

\[
 U^{1/4}\{H^{3/4}+D^{2/3}H^{5/12}+DH^{1/12}\}.
\]

对固定 U,D，三项都随 H 单调增大。故扩大 H 无法改进**这一个
已证明 envelope**；这不是实际 Möbius cancellation 的 no-go。

## 5. 临界账本及未支付步骤

U>=D 时 `DU^(1/3)<=(UD)^(2/3)`。若 `U=D^(1+c),0<c<1`，
交叉项除 U 是 `D^((1-c)/3)`。因此虽然比 elementary `U+D^2`
改善，仍没有证明原来源每个 c>0 的近线性 raw 合同。

当 `D=U^r,r>1`，已证明 envelope 的最大指数是 `r+1/3`：它比
`2(1+r)/3` 大 `(r-1)/3`。在引用的 r≈1.1242271468 处约为
1.4575604801，不能作为 cubic 已付指数约 1.1035226223 的改进。
只有另证理想 quartic raw 合同，才可采用条件指数约 1.0931703601；
三个数字均为未加 marks 二矩账本，不能直接翻译成 sigma 边界。

符号适配 probe 已将两种 incoming signs 的真实 Gauss numerator
统一为 `2h^3u`。它消除了正 incoming 的旧 `u^3` 费用，但没有
把 arbitrary eta 的完成变换或 surviving quartic terminal 变为已付
二次行。实际接入原目标还缺同一 eta、全部 valuations/零掩码、
angular/Mellin profiles 下的 completed reflection 和近临界 cancellation。
once-prime overlap 会使展开列不再 squarefree；本笔记没有付款这些
列，故本次 PASS 严格限于 unmarked 全行 (2)、固定 profile supremum
及其上述比较。没有新无零区，也没有 full RH 结论。
