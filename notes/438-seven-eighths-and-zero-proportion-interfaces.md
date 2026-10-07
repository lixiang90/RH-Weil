# 438. OpenAI 7/8 证明的思路及与 67.25% 比例法的接口

2026-10-07。外部预印本和形式化源码为 [R]；明确输入下的截止、核增长及联合预算推导为 [T/R]；
新的比例或无零边界仍为 [O]。math 仓库只读，本稿不宣称已重跑其 Lean kernel。

## 1. 找到的原件及验证范围

本地 `E:/codex-build/math` 的 origin 是 OpenAI/math，核查提交为
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`。
7/8 主稿位于
[September-30/build/paper.tex](</E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex:106>)，
它声明对 F=Q(sqrt(−3)) 的全部有限阶 Hecke L 及全部 Dirichlet L，
Re s>7/8 在所有导子、全部高度均无零；principal 的 s=1 极点允许存在。
[October-5/build/paper2.tex](</E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex:73>)
给另一条 11/12 证明，明确定位为较易阅读的替代途径，不是撤回 7/8。
这里的半平面严格大于边界，不能排除边界线上的零点。

实际形式化入口
[Nonvanishing.lean](</E:/codex-build/math/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean:29>)
调用 `SevenEighths.ProbeFinalAssemblyUnconditional.zeta_nonzero`。
其 unconditional assembly 通过 certified existence、bands 和 detector profile 构造证书。
ComparatorChallenges 中有 sorry 的文件是挑战模板，不能据此判断实际定理含 sorry。
本轮只读重跑实际 OAI import closure 的 2,924 个模块、486,490 行，未找到 sorry/admit/sorryAx
或新增 axiom 声明；这没有扫描外部依赖，也没有执行 kernel、build 或 Comparator。
扫描的逐模块哈希、外部未扫描依赖及范围保存在
`output/openai-math-nonvanishing-static-closure.json`，可由
`scripts/openai_math_source_closure_audit.py` 复跑。
`lean/formalization.yaml` 的全局 review.status 为 unchecked；源码、作者范围说明与本项目独立验收仍须区分。

公开固定来源：
[7/8 原稿](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
[形式化范围 003.md](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/docs/003.md)。

## 2. 先理解 11/12：把一个目标嵌入可平均的六次族

固定目标 nu，考虑光滑 Mobius 理想和 A_1(D)，嵌入

\[
 A_u(D)=\sum_{\mathfrak n}\mu(\mathfrak n)\nu(\mathfrak n)
     \chi_{\mathfrak n}(u)W(N\mathfrak n/D).
\]

对 H=D^{1+theta}，0<theta<=1/10，原替代稿得到
sum_{0<Nu<=H}|A_u(D)|²<<D^{1+epsilon}H。
在 u=p^6 上，六次符号恰为 1_{p不整除n}；所以
A_{p^6}=A_1+O(D/H^{1/6})。
用约 H^{1/6}/log H 个这样的素数行，得到

\[
 |A_1(D)|^2\ll D^{1+\epsilon}H^{5/6}+D^2H^{-1/3},
\]

即 |A_1|<<D^{11/12+5theta/12+epsilon}。对每个要求的 epsilon 固定足够小 theta，
给 11/12+epsilon 的幂；不需要 theta 向零时统一常数。

难点是这个族均方。Poisson 把六次符号转成 Gauss 和；Mobius 系数进入 cubic theta 系数；
theta 的反射将角色指数 −1−2 化为 3 mod 6，即二次角色。
因此最终能用强二次 large sieve，而不是直接接受高次符号的较差交叉项。
theta completion 的完整指标是 n b³，b 可以与 squarefree n 共素因子；所有零延拓必须保留。
作者用准确 Mobius 反演及 double-Poisson 的有限下降递归控制这些 completion 项。
把已付的 Mobius 幂节省代回 Mellin 公式，才能推出 reciprocal L 的解析延拓与无零性。
不能只说“六次族均方强，所以 RH”。

## 3. 7/8 主稿：同一个 probe 的 low、高表示与补偿

主稿使用更精细的有限 physical probe。low 侧来自原几何、反射能量和 additive Gram；
high 侧是同一 probe 的准确 Poisson/Euler 展开，不是另外挑选一个较好估计对象。
短素数槽上作两项补偿：标记原行并减去 rescaled 的 scalar contribution。
有限 inclusion–exclusion 消掉不想要的 principal 局部项，却保留角色放大；
全部槽和两侧保持同一个 ray class、排除集及 zero masks。

原 Part II 的 low 指数为 3/16，principal 的非消失校正信号是

\[
 f_\eta(Z)=\frac1{2\pi i}\int_{(2)}
 Z^{s-11/16}e^{(s-5/6)^2}
 \frac{H_\eta(s)}{L_F^S(s,\eta)}\,ds,
 \quad |H_\eta-1|\le1/2.
\]

high 行若有偏右零点，就必须同时产生 inverse Mobius polynomial 与 plain polynomial 的大值。
相同的 u 行、相同高度和原 masks 使两种 witness 能合并；
标记逆二矩与 plain 四矩提供坏行的数量界，adaptive cutoff 平衡两者。
端点用完成平方的严格有理证书，而非仅检查参数网格。

令 beta_* 是所有 primitive finite-order Hecke 零点实部的全局上确界，不要求它被达到。
若 beta_*>7/8，则 low 比 Z^{beta_*−11/16} 少一个正幂；
high−principal 也有 target-independent 正节省。
两者给 reciprocal Mellin signal 的统一增长节省，迫使 1/L 向 beta_* 左侧延拓，
与全局上确界矛盾。先有 11/12 的第一阶段，才支付第二阶段所用的参数容量。
函数方程最后把 ζ 零点限制在 [1/8,7/8]。

这条路径研究的是“一个零点也不允许存在”的统一探测器。
它与有限 Weil Hermitian form 的 rank–trace 比例法有显式公式、矩和正负惯性的共同语言，
但计数对象和统一量词不同。

## 4. 比例来源必须保持交集口径

[Alpöge–Furman/Claude v2](https://arxiv.org/html/2608.13637v2) 的基线准确为

\[
 C_0=3/2-\frac1{\sqrt2}\cot(1/\sqrt2)
     =0.672500703679\ldots .
\]

分母计全部非平凡零点的重数，分子计简单且在中心线的点；
不是仅仅中心线比例，也不是“每个角色有 67.25% 好行”。
固定 primitive Dirichlet 的推广不等于全 Hecke 行族在导子、高度和 source weights 上的一致性。
[Lamzouri v2](https://arxiv.org/html/2609.02882v2) 同时给简单或在线并集至少 88.762…%，
以及简单比例与在线比例的平均至少 83.625…%；两者都不是提高 C_0 的交集界。
本轮还核到新的三点余项稿与既有 67.3% 研究草稿，所以任何新常数必须另作范围和纪录比较。
详见[来源审计](../reviews/2026-10-07/hybrid-proportion-source-audit.md)，不把未重跑的草稿认证成纪录。

## 5. 实际可支付的混合定理：更短 AF padding

显式以 H_theta: ζ(s)在 Re s>theta 无零作为输入，置 d=theta−1/2。
函数方程给 |beta−1/2|<=d。保留 AF 原 C² 窗口 phi_L、L=log(T/2pi)、
采样步长 2pi/L、归一化 q_L~L² 和全部原物理零点。
令 I=[T,2T)、I_P=[T−P,2T+P)，1<=P<=T/2，
G_P 为 I_P 零点的有限矩阵，H 为完整显式公式矩阵，E_P=H−G_P。

原 C² Fourier 界与准确 Poisson 网格恒等式给

\[
 \boxed{\|E_P\|_1\ll T^dP^{-2},\qquad
 |\operatorname{Tr}G_P-N(I)|\ll T^dL.}
 \tag{1}
\]

因此 |Tr G_P−N(I_P)|<<T^dL+PL。
证明保留复杂平方与共轭配对：网格全和的单点绝对预算 O(T^d L²)，
距端点 R>=1 的单侧尾 O(T^d L R^{−3})；
除以 q_L 并按单位高度计数求和就给 (1)。
距端点不到 1 的零点 O(L)，单列 O(T^d L)；
padding 外侧必须估计内网格贡献，不能套“1减掉外网格”的内侧论证。
自含证明见[来源与截止接口报告 §4](../reviews/2026-10-07/hybrid-proportion-source-audit.md)。

7/8 给 d=3/8，取 P=T^{1/4}，于是

\[
 \|E_P\|_1\ll T^{-1/8}=o(1),\qquad
 |\operatorname{Tr}G_P-N(I_P)|\ll
 T^{3/8}L+T^{1/4}L.
 \tag{2}
\]

迹范数尾为 o(1) 的充分门槛从旧 d=1/2 下 P=T^{alpha}, alpha>1/4，
改成 alpha>3/16；原稿选择的 P=sqrt T 可缩短。
这是同一 AF physical matrix 的真实接口改善。
但全矩阵 prime 二矩仍为 (R(psi)+o(1))N，MT 主常数 R_MT=2−C_0 没变；
prime 的 O(1/log T) 或最终保守 O(loglog T/log T) 误差大于 (2) 的归一化幂次尾。
所以该结果没有提升渐近比例。

Lamzouri 固定窗口 support eta⊂(−lambda,lambda) 的同源界还给
||f_{z_rho}||²<=T^{2lambda d}、|K(z_rho−z_rho′)|²<=T^{4lambda d}。
lambda=1/2 时，双点核最坏增长从 T 改为 T^{3/4}，
可以减轻尾截断预算；微观深度仍是 (beta−1/2)log T，未变成固定宽箱。

## 6. 不能免费获得的高矩与坏行节省

本轮[同窗惯性推导](../reviews/2026-10-07/hybrid-strip-inertia-derivation.md)给两个准确界限。
首先，若 p_off、p_mult 分别为离线与非简单的重数比例，
Lamzouri 联合预算与固定条带合成，对任何固定 k>0 有

\[
 \frac1N\sum|\beta-1/2|^k+(3/8)^k p_{\rm mult}
 \le(3/8)^k(1-C_0)+o(1).
 \tag{3}
\]

这是原尺度横向矩与重数的联合约束，没有改变 C_0。
其次，在同一个固定平滑 Lamzouri characteristic operator 中，
可用稀疏 O(log T) 簇精确匹配其窗口的二阶主常数 R_f，
同时使中心四阶迹/N 发散；把簇以足够小的位移拆开后，全部点都可简单且在线。
它反驳的是“条带+单窗口二阶+局部计数就自动给四矩”的推断，
不是 ζ 的反例，也不满足所有测试函数的完整显式公式。
如果把窗口缩到 1/log T 以控制微观深度，规范二阶常数反而按 log T 增长。

真正的比例增益仍需同一算子的四点算术、谱尾或可抗抵消的高矩余项。
真正的 detector 增益则需全 Hecke 行族的坏行幂节省，不能从单函数的高度比例推出。
[439](439-prime-slot-geometry-and-a-conditional-strip-improvement.md)筛出的
7/8−1/80000 候选来自原补偿几何的改变，仍待完整估计；
[440](440-principal-euler-correction-below-seven-eighths.md)支付了其中的本地 Euler 解析接口。
这三项结果和外部证明的验收范围分别保存，RH、实际新比例及实际新边界没有被标成完成。
