# 原路线的 Vaughan 归约与完整重放多点比例

2026-10-08。基线 main 5b4c99e561ddec59f1818b8471da508036503745。遵循用户“先回到原路线的改进”，本轮不继续更换代数数域。

本轮完成两个不同层次的结果：原素数四矩中的低段和 Type I 部分支付到2/3，完整剩余为实际带符号 Type II；原MT核的七点全域证书完成真实重放，以已知谱包络装配实际简单临界线比例。本项目新增的是完整验证与实际接口的纳入，不将已有多点机制或外部更高数值改称首次发现。无零边界仍为引用输入下的 σ*≈0.874957019420099；没有新边界论文。

## 1. 原完整 scalar 的已付部分 [T]

仍为 X=T/(2π)、ell=logX、J_T=[T/4,4T]，原 high scalar

\[
 P_H(t)=\frac1{a_\ell\ell}
   \sum_{\sqrt X<p\le X}\frac{\log p}{\sqrt p}p^{it},
 \qquad M_T=T^{-1}\int_{J_T}|P_H(t)|^4dt.
\]

取 U=V=floor(X^(1/8))、Y=X^(5/6)，完整实际剩余是

\[
 C_4(t)=-\frac1{a_\ell\ell}
 \sum_{\substack{m>U,\ k>V\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it},
 \quad b_V(k)=\sum_{\substack{d\mid k\\d\le V}}\mu(d).
\]

[完整作者证明](../reviews/2026-10-08/hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md)及[不同作者全文独审](../reviews/2026-10-08/hybrid-original-vaughan-type-i-and-type-ii-reduction-review-twisted.md)支付实际平方长度Y²的均值、sharp高段二阶导数及Type I系数二矩，得到

\[
 M_T\le8M_{C_4}+O_{\phi,\varepsilon}(T^{2/3+\varepsilon}),
 \qquad
 M_{C_4}\le8M_T+O_{\phi,\varepsilon}(T^{2/3+\varepsilon}).
\]

原两端、原正高度、normalizer和proper-power范数迁移全部保留。这不是两第四矩相差o1，也没有证明whole 2/3。当前whole上界仍是[476](476-original-fourth-growth-five-sevenths-with-ivic-density.md)的 T^(5/7+ε)，其中[Rθ]须按原来源阅读。

固定0<a<1/4还能取 U=V=floor(X^a)、Y=X^((2+4a)/3)，已付部分为 T^((1+8a)/3+ε)。a1/8给2/3，a1/7给5/7。a减小时，实际未付因子域扩大；不声称可不付代价地把同一Type II估计搬到新域。

剩余中大素数乘积的 c3 与 c4 系数真实相消。generic Type II 差相位 (mj)^it·overline((mk)^it)=(j/k)^it 与m无关，故 Type I 的二阶导数不能迁移为该联合矩的付款。需要支付的是完整 Λ(m)b_V(k)、共同Y<mk≤X及所有aspect ratios的四矩。

## 2. 实际七点证书完整重放 [E]

使用 ainta 固定040c5e899e658aed7b56a2a87f501798fe10761d的原代码、MT归一化核k0及原局部函数

\[
 F_6(g)=\frac1{3000}\sum_{i=1}^6g_i+
 \sum_{r=1}^6\frac2{7-r}\sum_{i=1}^{7-r}
 k_0(g_i+\cdots+g_{i+r-1})^2\ge\frac{19}{5000}
 \quad(g_i\ge0).
\]

[安全重放程序](../scripts/hybrid_multipoint_cap_replay.py)先验证所有固定原始模块的字节hash，再从Arb构造128bit、mesh1/4000的完整cells和二导数表。未解决terminal cell失败；只在完整stack清空后生成PASS。原cutoff整数45600满足45600/(4000·3000)=19/5000，域外压力判断无浮点舍入缺口。

[七点新执行报告](../output/hybrid-multipoint-seven-primary-replay.json)记录：

| 项目 | 真实结果 |
|---|---|
| complete cover | PASS |
| initial boxes | 729 |
| visited nodes | 707901 |
| pruned / splits | 354315 / 353586 |
| max depth | 37 |
| pressure / interval / tangent pruning | 3087 / 257493 / 93735 |
| normalized k0² table SHA | a9992300d2bf71665aa2b6bd2727e798624cd297103bb200c7f0ca2baea55a2c |
| w'' table SHA | 7913c5511a572c32dd573cd53123d8cf3ddf73d3ec63b1aa823faae2ae83570a |

另以旧固定 RationalKernel 完整重放三点 μ221/10^6，445581 boxes、333733 accepted leaves、453 outside、maxdepth19；[纯有理报告](../output/hybrid-multipoint-three-rational-replay.json)。它是独立有限认证，仍不自动证明分析计数接口。

## 3. 已知谱包络与实际比例装配 [T/R/E]

令 Ψ(t)=(t−1)²（0≤t≤2）、Ψ(t)=2t−3（t≥2）。对 m×m correlation Gram，已知精确谱包络 g_m(E)在 E≤m/(m−1)等于E，其余为 E/m+2sqrt((m−1)E/m)−1。[固定原始来源与独立数学核读](../reviews/2026-10-08/hybrid-multipoint-spectral-envelope-source-read-root.md)明确给先行来源 Schwarz e2453c1，并逐项核对多大特征值、1-Lipschitz、真实有限Gram的近单位对角比较。它不是本项目的新机制。

原七点窗口聚合对m点给 E_m+span/500≥A=(19/5000)(m−6)。选固定 m280，置

\[
 A=\frac{2603}{2500},\qquad
 C=g_{280}(A)=\frac{2603}{700000}
       +2\sqrt{\frac{726237}{700000}}-1.
\]

原Gram pinching及全部280个offset平均保留真实gap长度，给 J≥(C/280)s−279N/140000−o(N)。由真实二阶稳定性和完整惯性账本 s≥C0 N+J−o(N)，其中 C0=3/2−cot(1/sqrt2)/sqrt2，得

\[
 \liminf\frac{N_0^s}{N}\ge
 p=\frac{C_0-279/140000}{1-C/280}
 =0.6730096522791369120137\ldots .
\]

完整分析对象、重数、固定平滑顺序、有限原Gabor与prefix接口由[实际计数作者证明](../reviews/2026-10-08/hybrid-original-multipoint-envelope-and-actual-counting-research-compression.md)逐项给出。脚本只验证有理区间和有限证书，实际ζ计数的分析结论依赖明列[R]而非由程序自动认证。

不同零点计数必须另由完整HS预算及multiplicity/inertia关系推出，可得 liminf D/N≥(1+p)/2≈0.836504826139568456。这里不使用一般不成立的D≥(N+s)/2。

[精确区间代数](../output/hybrid-multipoint-cap-exact-algebra.json)给p上下有理包围，并严格证明它大于原 ainta m269装配及初始m270 cap。选m280足够，无须本稿主张全整数m的全局最优性。

## 4. 增量与尚未完成的目标

304项目三点基准为0.672509329145868939…；本轮完成更强原七点证书及已知包络的实际纳入，比例下界约67.3009652279%。它略高于原ainta的67.3008527928%，但低于[305已登记](305-post-6725-literature-baseline-audit.md)的更高公开候选，包括Shi67.3316977%及Devine声称67.3399%；也未完整重跑Schwarz增强目标382623/10^8。不是世界纪录声明、全Lean证明或外部同行评审结论。

此比例装配不需要7/8条带。条带输入目前用于476原四矩增长估计；新的Type I归约指出增长的实际Type II剩余。二者尚未支付同一物理四阶常数，也未把增长幂当κ反馈参数。

接下来可直接攻完整C4的联合均值，或原所有内部P的signed near共振常数；新增证明须保持真实四份素数权及共同相位。当前无零边界保持，Goal active，公开README继续作为项目介绍。
