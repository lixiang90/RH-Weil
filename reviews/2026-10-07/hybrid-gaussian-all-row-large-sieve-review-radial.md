# 458 独立全文逆审：Gaussian 全实际行四次/二次大筛

2026-10-07。作者：radial_review。只新增本报告；被审笔记、已冻结的
研究稿、论文、math、脚本、输出和 Git 状态均未修改。本报告实读 458
全文，核对 BGL、GL 的原定理及 family 定义，并以 DDHL v5 的显式
Gaussian 二次矩阵交叉核验。

**限定 PASS。**458 的全实际元素行上界、逐箱方向选择、固定 profile
的 row-scale supremum，以及纯此大筛 envelope 的放大比较，在所声明
的范围内通过。它包括 powerful rows、四个 units 和任意 lambda
valuation；所有自然零保留。它没有支付任意一次 prime slots、任意
profile/height 的完整 raw 合同、Gaussian completed reflection，或新的
无零边界。原底层大筛定理作为确切外部 [R] 输入，未在这里重证。

## 1. 最终证据对象与引用范围

本轮绑定 canonical LF（CRLF、lone CR 均转 LF，再作 UTF-8 SHA256）：

- [458](../../notes/458-gaussian-all-row-large-sieve-comparison.md)：
  `3ee821601d6e1d5da38c8235586981b28d7ebee5a5f28691a98d869834dcc8ac`，
  9964 UTF-8 bytes，246 行。
- [457](../../notes/457-number-field-choice-and-relative-amplification.md)：
  `75079970955602644a9290709f66e2be331ad6116d2a637ed8fc97fb0dde5791`。
  本轮重新核其 §4 的源行范围、自然零、缩放与注入转移；不重审其余
  已冻结的完成/数域结果。
- [Gaussian probe 研究稿](hybrid-gaussian-root-weight-probe-research.md)：
  `4a6b33cae1944bc904216c202a62f04d48d2f47b0ff5a852f13a3af5a063bc3d`。
  此处只比较已经明确的 elementary additive 宽度与 probe 的未付项。

外部 primary inputs：

- [BGL, Theorem 1.3 与 §2](https://arxiv.org/html/1112.1650v1)：
  squarefree 理想四次矩阵宽度 (A+D+(AD)^{2/3})，任意复列系数；
  使用其实际 Fisher–Friedberg Hecke family 和固定有限 ray data。
- [GL, Definition 1、Remark 3、Theorem 1.1、Corollary 1.2、§2](https://arxiv.org/html/1112.1642v2)：
  四次 family 的平方二次方向宽度 (B+D)。
- [DDHL v5, §3 与 Theorem 5.1](https://arxiv.org/html/2306.11875v5)：
  primary convention、互反/补充律、零扩张和显式 Gaussian squarefree
  quadratic large sieve。

这些输入并不包括任意目标 eta 的 FE；没有读取某个 completed
functional equation 并把它当作本证明的必要条件。没有运行有限
脚本、修改 JSON、构建 math，或借有限计算认证上述无限大筛。

## 2. 实际 quartic 矩阵确实匹配 BGL

不能只说角色阶数为四，便调用一个名字相近的 Hecke-family 定理。
这里有具体匹配。

Gaussian 奇理想有唯一 primary generator，primary 乘法保持 primary。
对 squarefree 奇 (n)，每个奇 (pi\mid n) 的局部角色

\[
 x\longmapsto (x/\pi)_4
\]

在循环群 ((\mathcal O/\pi)^\times) 上为真正四次角色：

\[
 N\pi\equiv1\pmod4.
\]

因而奇 conductor 正是 (n)，非互素输入取零；包括 norm 为 rational
prime 平方的 inert prime。无限型为零，可能的 2-part conductor
处于固定有限 ray data 中。

还可直接按 GL §2 的构造说明 numerator family。取 (S) 只含复位
及 lambda 位；Gaussian class number one 已足够。取固定

\[
 \mathfrak c=(\lambda^k),\qquad k\ge3
\]

满足该构造的局部条件，所有代表理想 (E) 的 (m_E) 选为其 primary
generator。若

\[
 (a)=(x)E\mathfrak g^4,\qquad x\equiv1\pmod{\mathfrak c},
\]

把奇 fractional ideal (mathfrak g) 也取 primary fractional generator
(g)。两侧的 primary 归一化给

\[
 a=xm_E g^4.
\]

Fisher–Friedberg 的 numerator (m_{(a)}=xm_E) 与 (a) 相差一个四次幂。
在其选定的、与 evaluation ideal (n) 互素的 (g) 上，故有

\[
 \chi_{(a)}((n))=(a/n)_4.
 \tag{R1}
\]

这给出了可用的 family 选择；其它固定归一化可经有限 ray 分拆处理。
squarefree (a) 时奇 conductor 含每个 (pi\mid a)，故 (R1) 在不互素
处的 primitive/zero extension 与真实矩阵也相同。

若改用 denominator-indexed convention，DDHL 的 primary reciprocity
给

\[
 (a/n)_4=(n/a)_4
 (-1)^{((Na-1)/4)((Nn-1)/4)}.
 \tag{R2}
\]

cross factor 只依赖有限 sectors。先固定行 sector，再将列分成有限
sectors，Cauchy 的损失为固定常数。单位与 lambda 的补充律也只有
固定有限 residue data，不引入随 (D)、(U) 或 eta conductor
增长的参数。

所以 458 的四次方向使用同一个真实剩余矩阵。对
(\epsilon_\chi=-1)，零处仍定义为零；共轭整个和并共轭列系数即可。
这个步骤不需对 eta 作 functional equation，也不要求 eta 属于
上述四次 family。

## 3. 平方方向不是非法降阶

真实局部恒等式是

\[
 (b/n)_4^2=(b/n)_2,
 \tag{R3}
\]

包括非互素处的零值。每个奇 prime 的四次局部角色平方仍为非平凡
二次角色，奇 conductor 不消失。GL Remark 3 和 Corollary 1.2
明确覆盖 (n=4) 的平方 family，因此可以把这一方向的宽度换成
(B+D)。

还有一个不依赖抽象 family 名称的交叉核验：DDHL v5 Theorem 5.1
直接给 odd squarefree Gaussian 元素的矩阵 ((n/b)_2) 宽度 (B+D)。
primary 元素属于该定理的 odd 行/列；将 (R2) 平方，reciprocity
sign 消失，所以

\[
 (b/n)_2=(n/b)_2.
\]

unit 情形单独为 1。限制到唯一 primary generators、排除任意指定
column masks，只减少非负行和或改动任意列系数。这与 458 所用的
平方方向是同一个矩阵，不是把四次 general row 当作二次角色。

## 4. 元素行分解、计数与自然零

458 (4) 的唯一分解通过逐 prime valuation 的 Euclidean division

\[
 v_\pi(u)=4t+e,\qquad 0\le e\le3
\]

得到。(e=1,2,3) 分别放入 squarefree、两两互素的 (a,b,c)；
(t) 放入任意 (r)。(r) 可与 (a,b,c) 重叠，这一点必要且正确。
单独保留 (lambda^v) 和四个 units 后，全部非零实际 Gaussian 元素
恰出现一次。

逐 column 的等式

\[
 \chi_n(r)^4=1_{(n,r)=1}
\]

是 zero-extended 等式。若 (n) 与 (a,b,c) 或 (r) 相交，固定
角色/显式 mask 保留原值零。扩大 (a) 或 (b) 的 squarefree 行
集合时没有删除这些 column zeros。

固定其余因子后，pairwise 行互素限制与 (Nu\le U) 是 row subsets；
外部求和非负，故可扩大。列系数仍为固定因子的角色乘原系数，不
依赖正在求和的 (a) 或 (b)。其能量为

\[
 \sum_n |t_n|^2
 \le \|W\|_\infty^2
 \sum_{D\le Nn\le2D}\frac1{Nn}
 \ll_W1.
 \tag{R4}
\]

eta 的 finite-order 值绝对值为 1、坏 prime 处为零，因而不改变
(R4) 的常数，也不需 conductor 费用。固定 norm imaginary twist
同样成立。

Gaussian ideal/primary 元素的 norm 箱计数为 (O(B),O(C),O(R))，
不是 (O(B^2)) 等错误格点长度。于是 458 (7)、(8) 的两个每箱
预算以及其因子 (BCR)、(ACR) 正确。

## 5. 两方向选择与全行上界

令

\[
 V_0=AB^2C^3R^4\le V=U/2^v.
\]

无论选哪一方向，行数项 (ABCR\le V_0)。当 (B\le A) 选四次
方向，否则选平方方向，所选 (D) 项为

\[
 D\min(A,B)CR\le D V_0^{1/3},
\]

因为 (min(A,B)^3\le AB^2) 且 (R^3\le R^4)。四次方向额外项
精确等于

\[
 (AD)^{2/3}BCR
 =(DV_0)^{2/3}B^{-1/3}C^{-1}R^{-5/3}
 \le(DV)^{2/3}.
\]

这里所有箱参数至少为 1，故没有忽略小参数的反向不等式。
dyadic 箱数为 (O(\log(2V)^4))，可吸收入预先任意缩小的 epsilon。
对 lambda valuation 求和时，(V,V^{2/3},V^{1/3}) 均几何可和；
四个 units 只有固定倍数。458 (2) 因而覆盖全部实际行。

若 (U\ge D)，有

\[
 DU^{1/3}\le(UD)^{2/3},
\]

所以 (3) 正确。若 (U=D^{1+c})、(0<c<1)，四次额外项相对 (U)
仍为 (D^{(1-c)/3})。这是当前上界未支付近线性合同的定量缺口；
并不证明真实均方必定达到这一上界，也不排除另有 Möbius saving。

## 6. 固定 profile supremum 的准入

逐 (D') 上界本身不足以交换 supremum 和行和；458 §5 使用了
必要的额外 argument。对每个 dyadic (D_j)，写 (D'=tD_j)、
(1\le t\le2)。有限区间 Sobolev 将 supremum 归约到 (f) 与
(\partial_t f) 的两个平方积分。后者的 column profile 是

\[
 -\frac{Nn}{t^2D_j}
 W'\!\left(\frac{Nn}{tD_j}\right).
\]

两类 columns 都支撑于固定倍数的 (D_j) 区间，其能量、所需固定
seminorm 对 (t\in[1,2]) 一致。逐 (t) 应用 §4 的实际矩阵大筛并
积分合法。

对全部 (D_j\le D) 求和：(U) 项只有 logarithmic multiplicity；
含 (D_j^{2/3})、(D_j) 的项几何可和。小到无 column 的尺度为零，
剩余 bounded scales 可用大筛参数 1 处理。因此同一个固定 (W) 的
supremum 上界通过。

没有由此得到任意 row-dependent profiles、任意高度导数或 Gaussian
FE 的统一合同。增加这类参数时须重新明确能量/seminorm 的费用；
458 最终版未越过这一范围。

## 7. 放大域、envelope 比较与原目标

本轮建议的唯一必要域澄清已经纳入 458 §6：启动平均是 457 的
**fourth-power-free 源行**；终端 (B(H,D)) 才使用 458 的全行界和
同 profile supremum。若起始 (u) 任意，则 ((u,a)\mapsto ua^4)
不再注入，例如 ((p^4,1))、((1,p)) 同像；不能直接把任意全行
均方也除以 multiplier 个数。

在正确源域内，令 (H=UP^4)，457 的 deleted-column identity
保留自然零与缩放。将本轮终端宽度代入其平均，忽略可任意缩小的
幂损失，确有

\[
 \frac{B(H,D)}P
 =U^{1/4}\bigl(H^{3/4}+D^{2/3}H^{5/12}+DH^{1/12}\bigr).
\]

三个 (H) 指数均正，因此纯这一 envelope 在 (H\ge U) 上的最小值
位于 (H=U)。这不是对其它预算组合、真实 cancellation 或反射
机制的不可能性结论。

当 (D=U^r,r>1)，三项最大指数为 (r+1/3)。458 引用的 critical
(r\approx1.1242271468) 给 (1.4575604801)，与已有 cubic raw
合同的 (e_6\approx1.1035226223) 及假设理想 quartic raw 后的
(e_4\approx1.0931703601) 比较一致。后者仍是条件数，没有把当前
Gaussian 大筛读成理想 raw 合同。

一次 prime slots 会使展开 columns 不再 squarefree，特别 overlap
会改变 primitive character 与 zero masks；本次两类大筛没有支付
这些原 detector columns。也未支付完整 marked/plain 递归、同源
principal signal、Mellin 全族 continuation，或 RR/RH。458 的结论
止于新的未加 slots 全行二矩及其定量限制，限定 PASS。
