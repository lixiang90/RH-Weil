# 454 原背景与完整 Λ 混合迹：第二独立审查

2026-10-07。审查人：`twisted_research`。只读全文审查454、原AF v2 §2、
既有全高度接口及 finite crossing 证明，并只读运行新精确脚本的 `certify()`。
未编辑正文、旧论文、math、旧审查或输出。

结论：**限定 PASS**。454证明的是固定原 AF 窗和原有限 frame 下，实际
Gamma/pole背景 A 与完整 sharp Λ channel C 的四个混合迹主项，以及保留
真实 `Tr AC³` 的准确完整四阶展开。它不证明完整 `Tr C⁴=O(N)`，没有新比例、
新零自由区或 RH 结论；本审查也不是 Lean/kernel 认证。

## 1. 最终输入绑定与可复跑范围

以下文本 hash 按 UTF-8、CRLF→LF；未重写文件。

| 文件 | SHA256 / canonical bytes |
|---|---|
| [454正文](../../notes/454-original-background-and-weighted-prime-mixed-traces.md) | `8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7` / 13284 |
| [新精确脚本](../../scripts/hybrid_background_exact_audit.py) | `dfd8aa390df5a34a3dab27154648bfc6e903894f6b2ff2514156bcfd7b0c2105` / 7086 |
| [当前JSON](../../output/hybrid-background-exact-audit.json) | `cc9cd60b8977a03e577f50804a3f0d811a80f7bc86c728fdb98b4fc27539b974` / 2881 |
| [本轮重复混合推导](hybrid-low-high-mixed-four-word-research.md) | `71f62b2dd931cfda012e7dad9c4efcfece63f5cf1bb8ff5b466d3e2ac1ae89f9` / 22126 |
| [原高素数报告](hybrid-high-prime-four-word-response-research.md) | `988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666` / 19170 |
| [原全高度接口](hybrid-uniform-reciprocal-and-fourth-trace-interface.md) | `25468f8c29dc195d08083dd0fb4b60b5aea48478c9c1ce93053875d5dcc7d83c` / 20998 |

只读 `runpy.run_path` 导入脚本，调用 `certify()`，与磁盘 JSON 逐字段比较为
True。没有执行其 `__main__` 写输出入口。
454、重复混合推导和脚本的磁盘 hash/bytes也与独立计算一致。
最后冻结脚本新增高、低各1–3标签的9个 mixed partition模型；独立读取
`mixed_partition` 完整函数，核其六个位置、union/intersection及普通cyclic
分组，assertions与当前JSON全部一致。这是有限自由字系数核验。
脚本仅核有限 cyclic words、commutator 系数和多项式 profile 积分；
其 `not_certified` 保留 Hilbert、projection、alias、全高度和四迹算术缺口。

原始分析输入限于
[AF v2 §2](https://arxiv.org/html/2608.13637v2#S2) 的明确物理定义、
Gamma/pole bounds和窗尾，及
[Montgomery–Vaughan Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
的整数 log-frequency 局部间距 Hilbert inequality，以及经典
Chebyshev–Mertens。此处不用零自由包 [R]；全高度接口中的 reciprocal
部分也没有被带入454的证明。

## 2. 原始定义和全高度静态背景

独立检查了 `d=floor(XL)`、`alpha_k=T+2pi k/L`、unitary Fourier 的 F，
以及 `2pi/(a_L L)` normalization。准确 background 主部是
`A0=E*(phi²/a_L−1)E`，不是把 F 认成等距映射后留下一个 scalar I。
只使用 `d/N→1`，没有使用 AF §2.2 中更强且不相容的差额字样。

AF (2.3) 给 J=[T/2,3T] 上 `mu=L/(2pi)+O(1)`；Bessel 立即支付 Oop(1/L)。
J外每个 Fourier translate 到中心至少 T/2，二阶尾的加 log-weight 积分为
`O(dL/T³)`；乘原归一化后为 O(T^-2)，因此 negative/low heights 被实际支付。
pole 项分别用 J 内 `O(sqrtX/T)` 和 J外原绝对 `O(sqrtX)` 乘同一正尾压缩。
这些费用给 (5)，没有先删 low heights 或 principal peak。

`h_L=phi²/a_L−1` 在区间端点同取 −1，derivatives 相接，所以其圆周计算
合法。真实 translations 仍先零延拓；wrap 处 `phi(u)phi(u+s)=0`，并非
将 physical operator 改为 periodic operator。carrier 共轭只用于计算原 P。

## 3. 完整 log range：Hilbert 与两个 alias 账本

这是454的新实质输入，不能沿用 high-only 的跨度小于 L/2。
我独立核验了正文(11)–(17)的每一账本。

同号差频率的 csc 主项首先在**全部**不同整数 frequencies 上应用 Hilbert；
`delta_n^-1<=2n` 和 `sum Lambda(n)²<<XL` 给 O(1/L)。各 numerator phase
包括 carrier均进入可分的 coefficients，任意 bounded `c_n(u)`不破坏这种
单侧分离。只有 csc remainder 按差频范围分开，避免对截断 Hilbert kernel
作未经证明的应用。

大差频率意味着 n>sqrtX、m<=sqrtX，且 alias gap 至少 logm。
`Lambda(m)/logm<=1` 和整数 `sum_(m<=sqrtX)m^-1/2<<X^1/4` 配合 high
Chebyshev mass，给 O(X^-1/4 L^-2)，与(14)一致。没有省略 n靠近X、m小
这一实际 near-alias 区域。

正负和频率的输出交集长至多 `L−log(nm)`。当 nm=X，真实积分恰为0；
在其附近，这个 overlap 消掉有限核的 `1/(X epsilon)` 极点，留下
`O(1/(XL))`。小和频率另用固定 log4 gap。
`sum_(nm<=Y)Lambda(n)Lambda(m)/sqrt(nm)<<sqrtY log(2Y)` 可先对一侧
Chebyshev partial summation，再用 `sum_(n<=Y)Lambda(n)/n<<logY` 得出；
因此(15)的算术输入足够，两个 normalized 费用分别为
O(X^-3/4/L)、O(X^-1/2/L²)。

(17)允许 arbitrary bounded w（负号以 absolute bound支付）和 bounded c_n。
它是 `B_g* M_w B_g` 的实际 frame norm展开，diagonal中的 c_n²没有丢掉。
其中任意 bounded c_n 不自动获得 projection leakage；正文随后只对
固定 h_L 生成的 C² coefficients 使用泄漏，范围正确。

## 4. A²C²、commutator 与有限 P 迁移

对 A0² 的 positive leakage，trace O(logL) 乘 Cop²，得到
O(XlogL/L²)=o(d)。`B E=E C+QBE` 的 right-adjoint展开将有限
`Tr(C E*Mh²E C)` 和 `Tr(E*B Mh²B E)` 比较，cross项和平方泄漏正是
正文(19)两项，未把 bounded physical multiplication 与 P 免费交换。
R_T 对这一量仅乘已付 `Tr C²=O(d)`，因此不循环用四矩。

直接处理 `Mh B Mh B` 会出现耦合 endpoints。正文采用 D=[Mh,B]，其
真实 shift coefficient为 `a_s(u)(h(u)−h(u+s))`，方向和右平移一致。
(17)给 D 的物理二矩；C² coefficient正则性及 triangle给其独立 leakage。
`[A0,C]−E*DE=-E*Mh QBE+E*BQ MhE` 符号正确，HS error o(sqrt d)。
先从物理二矩取得 O(sqrt d) norm，再比较 squared norms，因此(22)没有
以待证 commutator bound 证明自身。R_T 的 HS error仅用已付二矩。

Hermitian 恒等式
`||[A,C]||HS²=2Tr(A²C²)−2Tr(ACAC)` 的符号和因子2正确。
ACAC的极限不被冒称非负。

## 5. A⁴、A³C 和连续 constants

bounded h multiplication的每个压缩幂差额 trace norm O(logL) 可通过
两次 P↔Q 的 HS crossings 证明；对 j<=4 其余 bounded 因子不改变费用。
乘 Cop及删除 Mh³与B间 internal P 的两个 HS leakages均给
O(sqrtX logL/L)=o(d)。

实际 single-shift trace仍用 K_d(±logn)。小 shift有固定 log2 gap；大 shift
保留 `L−logn` 的 overlap，正好支付 alias。n=X的 term积分准确为0。
R_T 对 A³C只乘已付 Tr|C|=O(d)，没有借完整 prime fourth bound。

完整 Λ²/n 的 proper-power质量总和收敛，归一化 L^-2 后趋零；这是二矩
diagonal极限内的付款，不等于免费删除 proper-power 的未知四阶 mixed words。
(25)的 r积分上限和正负方向正确，(27) retained endpoint difference squared。
pair symmetry与 `(h−h')²<=2h²+2h'²` 给 J<=4Z；flat bulk的V=Z=J=0，
边 taper仍在误差中，而非被点态删掉。

## 6. Whole fourth 精确余额和最终限定

自由 cyclic expansion的各项 multiplicities为
1、4、4、2、4、1。用 commutator identity合并2+2背景项后，确切得到
`F_T+4Y_T+6Z−J+V+o(1)`。`Y_T=Tr AC³/N`保留**实际 A**，所以(28)的
o(1)确不需要 F_T bounded；若先用(5)替换这里的 A 会产生未支付的 C³费用。
正文明确避免了这个错误。

HS Cauchy准确是 `||AC||HS ||C²||HS`，给
`|Y_T|<=sqrt((Tr A²C²/N)F_T)`；不是把 Y_T免费认成0。只有未来独立付出
`limsup F_T<=F<infinity`，才能取得(30)。现有 low upper constant、
high repeated或本轮 repeated mixed 子族均不能代替这一前件。

本次限定 PASS覆盖(1)、(17)、(28)–(30)及其固定原profile量词，
不认证完整 prime fourth、所有 mixed-prime correlation、任何比例改进、
proof kernel或 moving-conductor 的新统一矩阵定理。没有发现阻断性数学缺口。
