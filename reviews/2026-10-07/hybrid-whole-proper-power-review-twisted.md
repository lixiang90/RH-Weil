# 455 完整 proper-power 四范数与 prime-only 等价：独立全文审查

2026-10-07。审查人：`twisted_research`。只读核验455全文、原AF frame/
Poisson约定、square-base mean value和新精确脚本；未改正文、输出或旧稿。

结论：**限定 PASS**。原全部 proper powers的同一finite compression满足
`||E_pp||S4/N^(1/4)=O(1/L)`，无需full prime fourth前件；因此whole Λ与
whole genuine-prime问题在normalized fourth-root层面等价。
总fourth差无条件o(1)没有被证明，正文(21)正确保留bounded-budget条件。
没有新比例、零自由区、RH或kernel认证。

## 1. 最终文件绑定和精确核验

文本SHA按UTF-8、CRLF→LF、lone CR→LF，不删末尾换行或trim。

| 文件 | SHA256 / canonical LF bytes / raw bytes |
|---|---|
| [455正文](../../notes/455-whole-proper-power-fourth-norm-and-prime-equivalence.md) | `6bf2025dcc8f56d7b35d9c8b764ac2ff3b911a6e054bf9c496042c7f3e11ce41` / 9135 / 9135 |
| [精确脚本](../../scripts/hybrid_proper_power_exact_audit.py) | `2b05fca4d29848965b581bb32220dd90f42f58aeaba765e9365ba01c2a65119e` / 3875 / 3875 |
| [JSON](../../output/hybrid-proper-power-exact-audit.json) | `af7bc4c541f591fee0eb7b5d56c1315cccd8caddfc544ed418ad846104ce399b` / 5617 / 5884 |

只读 `runpy.run_path` 导入，执行 `certify()`，逐字段等于磁盘JSON；
10个weighted prime-product模型和48个scalar checks与输出一致。
没有执行写输出入口。脚本的proof范围限于有限系数和scalar多项式代数，
其 `not_certified` 明确保留MV、Jensen、尾、Schatten和whole-budget算术。

最终编辑修订已只读核对：scalar Jensen的eigenvector对象由未定义的
`C_pp`改为已定义的`E_pp`，开头两处状态文字同步为已完成独审。
这些修改没有改变(1)–(21)数学推导或精确脚本。根节点已重跑输出，
JSON从磁盘读取并绑定最终455正文SHA；我随后再次只读执行`certify()`，
逐字段等于本表最终JSON。10个coefficient models、48个scalar checks
不变。此次确已重跑有限核验，不沿用旧输出绑定。

## 2. 全部 powers与正确的 square-base frequency

原sharp powers的系数确为 `Lambda(p^j)=logp`，不是j logp。
`j>=3` 的几何和由 `sum logn/n^(3/2)<infinity` 控制，uniform于X和整条
real height轴；平方项的全height绝对O(L)保留t≈0 coherent peak。

S2²的base product m=pq<=X，frequency为2logm。
唯一分解使非对角系数2c_pc_q，平方系数c_p²；两种weighted identities
`2S²−sum c_p⁴`和`2W²−sum p²c_p⁴`正确。
S有限、W=O(L²)，因此energy为O(L⁴)。
局部spacing满足 `|2logm−2logn|>=1/m` 对最近相邻整数也成立，
所以delta_m^-1<=m；不是将频率log(m²)误判为length X²的任意多项式。
[Montgomery–Vaughan Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
展开两个time endpoints给任意interval均值O(|J|+L⁴)。
变换t'=2t的Jacobian也给同一尺度。
再加全height bounded R3，正文(12)的O(T)成立，不需zero-free输入。

## 3. 原 finite scalar Jensen、单位傅里叶常数和外尾

[AF v2 §2](https://arxiv.org/html/2608.13637v2#S2) 原unitary约定中，
`f_k=mathscrF phi(t−alpha_k)`、`Fe_k=f_k/sqrtL`，F是contraction。
对完整finite eigenbasis逐个添加0处缺少的measure质量，应用scalar x⁴
Jensen，确得正文(13)。它不依赖x⁴ operator convex，也没有删内部P。

归一化独立复算：`(2pi/(a_L L))⁴`、`P_pp=-pi^-1 ReQ_pp` 和frame的
L^-1相乘，prefactor准确为 `16/(a_L⁴ L⁵)`。
unitary infinite-grid diagonal是 `a_L L²/(2pi)`，而非未归一化的a_L L²。
两者相容；J上的positive scalar费用为O(T/L³)=O(d/L⁴)。

J外二阶C² Fourier尾给sum_k integral O(dT^-3)，这里每个中心均在[T,2T)，
故距离至少T/2；negative heights和t≈0也确被覆盖。
只能在这一步使用全height O(L) pp bound，所得O(d/(L T³))小于d/L⁴。
这在一个positive scalar majorant上分区，不把matrix第四次幂拆成无cross
terms的两个矩阵幂。正文范围准确。

## 4. Schatten传递及完整预算条件

E_pp实际为同一个sharp Λ channel减同一个prime-only channel，Hermitian。
S4 Minkowski和reverse triangle给每个T的fourth-root差≤epsilon_T，
无需任一full F有界；给两边加**完全相同**的Hermitian background后仍成立。
因此(19)、(20)可在原A上直接用，不必先替换background，也容许A大norm。

连续单调的第四次幂使两个limsup相同，包括+infinity，并使boundedness
等价；有限liminf的表述亦正确。对于未必bounded的大小，
`|a⁴−b⁴|<=4epsilon(b+epsilon)³`明确控制增长，(21)没有偷换成无条件o(1)。
只有将来独立支付一个whole prime/Λ/centered fourth预算，才能将全部
proper-power mixed words的**总差额**视作o(N)。此不等于逐词o(N)。

454的条件bridge保持其未付F和实际AC³；452的zero-tail传递另保留明列[R]。
455的(1)–(21)仅依赖原AF frame、经典MV/Chebyshev和norm定理，不需要[R]。
没有发现实质缺口；本PASS不覆盖high/low distinct或完整比例主预算。
