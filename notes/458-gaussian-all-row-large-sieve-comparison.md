# 458：高斯域全实际行的大筛界与换域的定量限制

2026-10-07。回应辅助域选择问题；这是未加 prime slots 的均方比较，
不构成新的无零区域。已提交的 [457](457-number-field-choice-and-relative-amplification.md)
及 [Gaussian probe](../reviews/2026-10-07/hybrid-gaussian-root-weight-probe-research.md)
保持原版。本笔记补充普通四次大筛与二次大筛组合后能实际支付的范围。

## 1. 结论及引用输入

令 O=Z[i]，lambda=1+i，奇理想使用唯一 primary generator。
对任意同一个有限阶目标 eta（在其坏素数处零延拓），固定光滑
W 支撑于 [1,2]，固定 epsilon_chi=+1 或 -1，定义

\[
 M_u(D)=\sum_{n\ {\rm odd,sf}}
 \frac{\mu(n)\eta(n)}{\sqrt{Nn}}W(Nn/D)
 \left(\frac{u}{n}\right)_4^{\epsilon_\chi}.
 \tag{1}
\]

剩余角色在非单位处始终取零。D,U>=1。这里没有一次素数列、混合
符号列或新 theta 完成的假设。由下列已发表大筛，可以推导

\[
 \boxed{\sum_{0<Nu\le U}|M_u(D)|^2
 \ll_{\varepsilon,W}
 \{U+(UD)^{2/3}+D U^{1/3}\}(UD)^\varepsilon.}
 \tag{2}
\]

隐含常数依赖固定 Gaussian residue/ray 归一化，不依赖 eta 的值或
导子；eta 只作为绝对值不超过 1 的列系数，其附加零掩码保留。
固定的 norm imaginary twist 同样可作为列系数。这不是关于任意
finite target 的 completed functional equation 的结论。

输入是
[Blomer–Goldmakher–Louvel Theorem 1.3](https://arxiv.org/html/1112.1650v1)
的 squarefree 四次宽度 A+D+(AD)^(2/3)，以及
[Goldmakher–Louvel Corollary 1.2](https://arxiv.org/html/1112.1642v2)
在 n=4 时给出的平方角色宽度 B+D。两者均允许任意列系数；
不能把前者的 squarefree 行直接当成全部 u。

在 U>=D 时 (2) 简化为

\[
 \sum_{0<Nu\le U}|M_u(D)|^2
 \ll \{U+(UD)^{2/3}\}(UD)^\varepsilon.
 \tag{3}
\]

这改善已提交 elementary additive bound U+D^2 在中间尺度的上界，
但仍只在 U>=D^2 支付任意小幂损失的线性 raw 界。若
U=D^(1+c)，0<c<1，额外项除以 U 为 D^((1-c)/3)，是正的幂次损失。
因此原证明所需“每个 c>0、U>=D^(1+c) 即线性”的合同仍未支付。

## 2. 实际角色与两类大筛的匹配

对每个奇 squarefree n，a -> (a/n)_4 是 primary generator 上的
剩余角色。把它读作奇理想上的角色时，单位补充律归入固定的
2-part ray data。奇 prime 的局部 conductor 正是该 prime，且
squarefree n 的 CRT 乘积在奇部 primitive。

具体地，对互素奇 primary a,n，四次互反律是

\[
 \left(\frac a n\right)_4
 =\left(\frac n a\right)_4
 (-1)^{((Na-1)/4)((Nn-1)/4)}.
\]

此式及单位/lambda 的补充律采用
[DDHL v5 §3](https://arxiv.org/html/2306.11875v5) 的 primary convention。
四次互反律的 cross factor只依赖固定有限 primary ray sectors。
按行 sector、列 sector 分拆，再用有限次 Cauchy，可将该真实剩余
矩阵与 BGL 的四次 Hecke-family 大筛匹配。非互素处两侧都为零；
固定的 2-part 不作为新的增长参数。epsilon_chi=-1 的情形将整个
和共轭，列系数随之共轭，故具有同一范数界。

平方 (a/n)_4^2 是二次剩余角色，在每个奇 good prime 仍 primitive。
GL Remark 3 与 Corollary 1.2 明确允许将四次 Hecke family平方为
二次 family，给出 B+D。亦可直接用 Gaussian quadratic Hecke
family及二次补充律处理同一有限 2-part。这里使用的是同一
真实矩阵的平方角色，不是把任意四次行宣称为二次行。

一个无需抽象 family 识别的交叉核对是 DDHL v5 Theorem 5.1：其
Gaussian squarefree 二次符号矩阵直接有 M+N 宽度。primary 元素
属于该定理的 odd 行/列，且 primary quadratic reciprocity 将
(b/n)_2=(n/b)_2；故可直接用于本笔记的平方方向。

上述有限 sector 分拆仅改变固定常数。eta 及下面固定因子的
角色/零掩码全部进入列系数，不需要 eta 属于四次 family。

## 3. 全部元素行的精确分解

每个非零 u 唯一写成

\[
 u=\zeta\lambda^v a b^2 c^3 r^4,\qquad
 \zeta\in\{1,i,-1,-i\},\quad v\ge0,
 \tag{4}
\]

其中 a,b,c,r 为奇 primary；a,b,c squarefree且两两互素，r 任意，
r 允许与 a,b,c 重叠。逐奇 prime 将 valuation 写成 4t+e，
e=0,1,2,3，即分别确定 r,a,b,c。primary generator 的乘法精确，
剩余单位归入 zeta。因此没有漏掉 powerful rows或增加单位重复。

其角色精确满足

\[
 \chi_n(u)^{\epsilon_\chi}
 =\chi_n(\zeta\lambda^v)^{\epsilon_\chi}
  \chi_n(a)^{\epsilon_\chi}
  \chi_n(b)^{2\epsilon_\chi}
  \chi_n(c)^{3\epsilon_\chi}1_{(n,r)=1}.
 \tag{5}
\]

这是 zero-extended 等式：即使 n 与 r 或 a,b,c 相交，等式仍保留
真实零值。尤其不能将 r^4 行看成无条件 principal 而删除其 mask。

先固定 zeta,v，令 V=U/2^v>=1。对 (4) 的其余四项作 dyadic 分箱，
各 norm 在 [A,2A)、[B,2B)、[C,2C)、[R,2R)，A,B,C,R>=1。
非空箱必有

\[
 A B^2 C^3 R^4\le V.                                    \tag{6}
\]

每个固定因子对应的奇理想数 O(B)、O(C)、O(R)，来自二维 Gaussian
格点计数。a,b,c 的 pairwise restrictions及最后 Nu<=U restriction
可在每个固定因子的非负行和中扩大为全部相应 squarefree 行。
这一步是 upper bound；(5) 的列零掩码不随之删除。

## 4. 每箱选择四次或二次方向

先固定 b,c,r，对 a 求和。实际列系数为

\[
 t_n=\frac{\mu(n)\eta(n)}{\sqrt{Nn}}W(Nn/D)
 \chi_n(\zeta\lambda^v b^2c^3)^{\epsilon_\chi}1_{(n,r)=1}.
\]

它们仍在 squarefree n 上，且 sum |t_n|^2=O_W(1)，因为
sum_(D<=Nn<=2D) 1/Nn=O(1)。BGL 给每箱

\[
 \ll B C R\{A+D+(AD)^{2/3}\}(VD)^\varepsilon.              \tag{7}
\]

另固定 a,c,r，对 b 求和；其角色是 chi_n(b)^(2 epsilon_chi)，
epsilon_chi 两种符号给同一二次角色。GL 给每箱

\[
 \ll A C R\{B+D\}(VD)^\varepsilon.                        \tag{8}
\]

若 B<=A 选 (7)，否则选 (8)。两界的行数项均为 ABCR<=V。
所选 D 项最多

\[
 D\min(A,B)CR\le D V^{1/3},                              \tag{9}
\]

因为 min(A,B)^3<=AB^2，且 C^3R^3<=C^3R^4。若选 (7)，
它唯一额外的四次项也有

\[
 (AD)^{2/3}BCR
 =(D AB^2C^3R^4)^{2/3}B^{-1/3}C^{-1}R^{-5/3}
 \le(VD)^{2/3}.                                          \tag{10}
\]

故每箱由 V+(VD)^(2/3)+DV^(1/3) 控制。O(log(2V)^4) 个箱的
损失吸进任意小幂。最后对 v 求和，V=U/2^v 的三个幂次分别为
1、2/3、1/3，均构成几何级数；四个 units只增加固定因子。
这证明 (2)，包括所有 ramified valuations及全部非零实际元素行。

## 5. 固定 profile 的 row-scale supremum

对同一个 W，还可将左侧换成
sum_(0<Nu<=U) sup_(0<D'<=D) |M_u(D')|^2，右侧不变至任意小幂。
证明不能只从逐 D' 界直接交换 supremum 与求和：先按 D' dyadic 分箱，
写 D'=tD_j、1<=t<=2。有限 t 区间的 Sobolev 界

\[
 \sup_{1\le t\le2}|f(t)|^2
 \ll\int_1^2(|f(t)|^2+|f'(t)|^2)\,dt
\]

将 M 的最大值归约为 W(Nn/(tD_j)) 及其 t 导数的两个二矩。
两者均有固定 seminorm和 O(1) 列能量，support在固定倍数的 D_j
区间；(7)–(10)的证明逐一适用。将所有 D_j<=D 相加，第一项多
O(log(2D))，其它两项几何可和。D'小到 support无非零 n 时和为零；
剩余常数尺度并入同一界。没有新增 contour、finite-target FE或高度合同。

## 6. 四次放大不能消去此上界的额外费用

沿 [457](457-number-field-choice-and-relative-amplification.md) 的精确
u -> u a^4 转移，起始 u 限为 fourth-power-free rows，令 H=UP^4，
平均 multiplier 给上界 B(H,D)/P。起始行的限制保证 (u,a)->u a^4
注入；任意全 u 不能直接沿此映射除以 P。终端 B(H,D) 则确实由
本笔记的全行界支付，且同 profile supremum 由第 5 节支付。
这里 B(H,D)=H+(HD)^(2/3)+D H^(1/3)。忽略可任意
缩小的 epsilon 损失，得到

\[
 \frac{B(H,D)}P
 =U^{1/4}\{H^{3/4}+D^{2/3}H^{5/12}+D H^{1/12}\}.          \tag{11}
\]

固定 U,D 时三个 H 指数都为正。因此这种纯大筛 envelope在 H>=U
中的最小值位于 H=U；增加四次 multiplier不能从该预算得到收益。
这只评价 (2) 的上界，不是对实际 Möbius cancellation 的不可能性定理。

当 D=U^r、r>1，本界的指数为

\[
 e_{\rm LS}(r)=\max\{1,2(1+r)/3,r+1/3\}=r+1/3.            \tag{12}
\]

取既有 critical r=ell≈1.1242271468，本界是约 1.4575604801。
相比之下，原 cubic raw 合同支撑的 order-six amplification为
e6(ell)≈1.1035226223；只有另行证明理想 quartic raw合同后，才能用
e4(ell)≈1.0931703601。三者都是同一类未加 marks 的均方指数，
不是 sigma 改变量，且不包含原 marked/plain 整套递归。

## 7. 对换域问题的解释

Q(sqrt(-3)) 的实际优势是 cubic signal + sextic reflection给出
quadratic terminal；判别式、格密度、有限单位数主要改变固定常数。
另一个虚二次域不能原封保留 primitive cubic root；Q(i)则允许重新
设计 quartic signal、反射及四次放大。

现在 Gaussian 的真实 signal、保留 eta 的 unit-dual identity，以及
未加 slots 的全行估计 (2) 都有具体输入/证明。但普通四次加二次大筛
仍留下 (UD)^(2/3) 或 D U^(1/3) 费用，没有支付每个 c>0 的近线性
raw合同。一次 prime slots的 overlap会使 expanded columns不再
squarefree，本笔记不直接推广 (2) 给那些列。

优先研究应是同一个 sign-adapted Gaussian probe的 completed反射、
实际 quadratic terminal及近临界 cancellation，而非只减小域的
判别式或把原式中的 6 改成 4。其他虚二次域需要新的闭合 signal；
高次 CM 域还需单位商、多个 archimedean profiles及高度预算。
当前既有引用输入 [R] 下 sigma*≈0.874957019420099保持；未确认
新边界，不触发新的正式边界论文。
