# 197. 部分 Weil 配置：比例、四矩与非零区域

日期：2026-09-01

状态：有限维结论为 [T]；近期外部结果重述为 [R]；依赖未证矩渐近的结论为 [C]；
有限数值审计为 [N]；zeta 算术输入为 [O]。

独立论文：[partial-weil-configurations-paper.tex](../papers/partial-weil-configurations-paper.tex)。

## 1. 二阶部分 Weil 配置 [T]

令 \(G=P+Q\)，其中

\[
P\succeq0,\quad \operatorname{rank}P\le s,\quad
\operatorname{tr}P\le s,\quad n_+(Q)\le b,
\]

并有

\[
\operatorname{tr}P+2b\le N+E_0,\quad
s+2b\le N+E_1,\quad D\ge s+b.
\]

rank--trace 不等式推出

\[
s\ge4\operatorname{tr}G-\|G\|_{\rm HS}^2-2N-2E_0,
\]

\[
D\ge\frac{4\operatorname{tr}G-\|G\|_{\rm HS}^2-N-E_1}{2}.
\]

若 \(\operatorname{tr}G\ge\tau N\)、
\(\|G\|_{\rm HS}^2\le RN\)、\(E_j=o(N)\)，则

\[
\frac{s}{N}\ge4\tau-2-R-o(1),\qquad
\frac{D}{N}\ge\frac{4\tau-R-1}{2}-o(1).
\]

在 \(\tau=1\) 时是 \(2-R\) 与 \((3-R)/2\)。模型
\(P=\Pi_1,Q=2\Pi_2,\Pi_1\perp\Pi_2\) 表明只使用这些数据时结论尖锐。

Alpöge--Furman（arXiv:2608.13637v2）已对 zeta 和固定本原 Dirichlet
\(L\) 函数无条件实现该配置。Montgomery--Taylor 窗给

\[
R=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2},
\]

故简单中心线比例为 \(0.6725007\ldots\)，互异比例为
\(0.8362503\ldots\)。

## 2. \(13/18\) 的准确地位 [C]

若压缩 Weil 矩阵的前四矩满足 sine-kernel Gram 预测

\[
(m_1,m_2,m_3,m_4)=\left(1,\frac43,2,\frac{13}{4}\right),
\]

则 Christoffel 函数 \(\Lambda_2(0)=5/36\)，正惯性计数给

\[
\frac{s}{N}\ge1-2\Lambda_2(0)=\frac{13}{18}=0.7222\ldots.
\]

核对结论：

1. \(13/18\) 不在 Connes 1998 论文中，而在 Alpöge--Furman 的四矩条件讨论中。
2. 它只是四矩 Christoffel 层级，不是随机矩阵路线的最终上界；全部矩假设给比例 1。
3. 四矩的 zeta 实现仍是条件性的，包含 Hardy--Littlewood 型
   \(\Lambda*\Lambda\) shifted correlations。

## 3. 同一四矩数据的 \(16/21\) [C/R]

Academia 专题首页列出的 Esther Notik 2026 working paper
“A sharp four-moment inertia bound for the zeros of the Riemann zeta function”
保留了 Christoffel 计数丢掉的 rank 与 trace 信息。

定义中心矩

\[
b_2=m_2-1,\qquad b_4=m_4-4m_3+6m_2-3.
\]

完整 rank--trace--inertia 线性规划给

\[
R(b_2,b_4)=\frac{(1-b_2)^2}{1-2b_2+b_4},
\]

\[
\frac{s}{N}\ge R(b_2,b_4),\qquad
\frac{D}{N}\ge\frac{1+R(b_2,b_4)}2,
\]

前提是分母为正且
\(\sigma_*=(b_2-b_4)/(1-b_2)<3/4\)。

对 \(b_2=1/3,b_4=1/4\)，

\[
\frac{s}{N}\ge\frac{16}{21}=0.761904\ldots,\qquad
\frac{D}{N}\ge\frac{37}{42}=0.880952\ldots.
\]

匹配极端谱测度为

\[
\frac8{21}\delta_{1+1/(2\sqrt2)}
+\frac8{21}\delta_{1-1/(2\sqrt2)}
+\frac5{42}\delta_2+\frac5{42}\delta_0.
\]

它的前四矩恰为 \(1,1,4/3,2,13/4\)，所以 \(16/21\) 对这些矩和账本是尖锐的。
本项目已独立核对 quartic dual、闭式 \(R\)、极端测度和两个比例常数。该材料仍是
近期 working paper；其有限维部分可复核，但 zeta 四矩输入并未因此得到证明。

## 4. 更现实的一侧四矩目标 [O]

记当前无条件常数

\[
\kappa=2-\left(\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}\right).
\]

平窗 \(b_2=1/3\) 下，只要证明

\[
b_4<\frac4{9\kappa}-\frac13
=0.3275499074\ldots,
\]

就能严格改善 \(0.6725007\ldots\)。预测 \(b_4=1/4\)，允许约 \(31\%\) 的
相对超额；不需要完整两侧 Hardy--Littlewood 渐近，也不需要单独证明三阶矩。

困难项是有效长度约 \(T^2\) 的正半定均值

\[
\frac1T\int_T^{2T}\left|\sum_m c_m m^{it}\right|^2dt,\qquad
c_m\sim\frac{(\Lambda*\Lambda)(m)}{\sqrt m}.
\]

普通 Montgomery--Vaughan error 在此长度上大于 diagonal 约一个 \(T\) 因子，
所以必须保留 shifted-convolution 的算术相消。这是下一轮最优先的具体目标。

## 5. 非零区域需要深度可见性 [T/O]

只知道每个离线对有一个负方向并不控制其谱深度。令 \(B_\eta\) 为
\(|\operatorname{Re}\rho-1/2|\ge\eta\) 的离线对数。若有子空间

\[
\dim U_\eta\ge B_\eta-E_\eta,\qquad
G|_{U_\eta}\preceq-v(\eta)I,
\]

则

\[
B_\eta\le E_\eta+\frac{\operatorname{tr}G_-}{v(\eta)}.
\]

所以负谱迹的相对小量给深离线零点密度零；若
\(E_\eta=0,\operatorname{tr}G_-<v(\eta)\)，则窗口内没有这种零点。

构造性接口是 \(G=CC^*-BB^*\)。若在 \(r\) 维子空间上

\[
BB^*\succeq\alpha^2I,\qquad CC^*\preceq\beta^2I,\qquad \alpha>\beta,
\]

则 \(v=\alpha^2-\beta^2\)。这就是定量 divisor-mode separation。

2026-09-06补充：[302](302-positive-background-quotient-collapse.md)证明一种
明确硬商不能免费给出该可见性：在窄的原始高度窗口中，商掉有限指数分解
的全部正秩一项张成后，实际zeta前缀的负秩仍精确保留，
但压缩负迹无条件指数趋零。该压缩不保原迹，也不是Schur补；
不反驳上面的条件性结构蕴含，只表明其下框架必须另证。

## 6. Connes 附件提供的结构 [R]

附件 9811068.pdf 是 Alain Connes 的
“Trace formula in noncommutative Geometry and the zeros of the Riemann zeta function”
（arXiv:math/9811068）。它研究 \(X=\mathbb A/k^*\) 上的 idele 类群作用，把
临界零点作为 absorption spectrum，把离线零点作为相对中心线的 resonances。

论文证明 \(S\)-local trace formula；提出全局 cutoff trace formula；并在正特征
全局域中证明该全局公式与全部 Grössencharakter \(L\) 函数的 RH 等价。数域
Archimedean cutoff 使用 prolate spheroidal 投影几何。

它不提供 \(13/18\)，但给出另一个非交换几何 carrier。可研究的放宽问题是：

1. 不证明 RH 等价的完整全局 trace formula；
2. 只对有限 Gabor/prolate 压缩证明 trace 与前几矩；
3. 从 resonance harmonic measure 提取惯性或深度可见性；
4. 接入二阶、四阶或非零区域结构定理。

## 7. Academia 专题的使用原则

该专题目前列出 42 篇材料，质量高度不均。它适合作为线索源，不适合作为可信度
背书。只有能回溯原文、列出明确假设，并能还原为有限维恒等式、可执行证书或明确
算术输入的内容才进入主路线。本轮真正有价值的新线索是四矩 exact LP；其余大量
物理类比或声称证明 RH 的材料暂不作为研究依赖。

## 8. 下一步

1. 推导 tapered/Gabor window 下 \(b_4\) 的完整 prime/Gamma/continuum 分解。
2. 分离 fourth moment 的 \(2+2\)、\(3+1\)、\(4+0\) resonance families。
3. 针对一侧阈值设计 Vaughan/Brownian response。
4. 联合优化窗口的 \(b_2,b_4\)，而不是只优化二阶 \(R\)。
5. 研究 Connes cutoff 的有限四矩是否有更自然的局部几何控制。
6. 建立单个离线 resonance 的 prolate/Gabor 商空间 lower frame 模型。

审计脚本 scripts/partial_weil_audit.py 已覆盖二阶尖锐模型、Montgomery--Taylor
常数、\(13/18\)、\(16/21\)、\(37/42\)、匹配四点谱测度、\(b_4\) 阈值与深度
可见性账本。它只验证有限维恒等式，不构成 zeta 四矩估计或 RH 证据。
## 9. 后续更新（笔记 228）

当前 prime-side 路线控制的是中心二矩与中心四矩，而不是完整 raw moments 到四阶。
笔记 228 证明：relative-dense moving blocks 足以应用本笔记的 quartic
rank--trace--inertia 证书；若中心二矩为 `v`、中心四矩上界为 `B4`，则 simple
比例为 `(1-v)^2/(1-2v+B4)`。MT 数值形式上给 `0.7569026657...`。另一方面，
笔记 228 构造两组均值一、同中心二/四矩但不同三阶矩的显式谱测度，严格说明
当前数据不能代入需要完整 `m0,...,m4` 的 `13/18` Christoffel 数值。记录级实例
在笔记 203--227 的 prime-side 链独立复核完成前保持 `[C]`。

## 10. Lamzouri新短证的有限算子接口审计（2026-09-06）

[R] Youness Lamzouri，*A new proof that more than 2/3 of the zeros of the
Riemann zeta function are simple and on the critical line*，
[arXiv:2609.02882v1](https://arxiv.org/html/2609.02882v1)，2026-09-02。
主代理已阅读§§2--3的主要证明：Proposition2.1的Hilbert空间不等式、
两项固定测试函数去除相关权的步骤，以及Theorem1.1的极限次序。
所得约0.6725007与0.8362503仍是原二阶基线，不是本项目的新纪录。
未运行附录链接的Lean工程，不能把作者关于形式证书的说明当作本地验证。

下面给出与本篇第1节的精确有限维接口 [T，外部结果的兼容性核验，
不作新颖性晋级]。采用其固定实偶函数 \(\eta\)，满足
\(\int\eta^2=1\)，紧支撑；\(K=\widehat{\eta^2}\)。
令 \(\mathcal Z\) 为有限共轭封闭多重集，\(N\) 为总重数。
不同实点中简单的有 \(s\) 个，重复的有 \(r\) 个；
不同非实共轭对有 \(k\) 对，每对两点的共同重数记为 \(m_z\)。记
\[
 f_z(u)=\eta(u)e^{-2\pi izu},\quad
 g_z=(f_z+f_{\bar z})/2,\quad h_z=(f_z-f_{\bar z})/(2i).
\]
实点的 \(f_x\)、各 \(g_z,h_z\) 都属于实Hilbert空间
\[
 \mathcal H_{\mathbb R}
   =\{v\in L^2:\overline{v(u)}=v(-u)\},
\]
其中通常复内积限制为实数。其范数恒等式为
\(\|f_x\|^2=1,\ \|g_z\|^2-\|h_z\|^2=1\)。
在这些向量的有限实线性张成上，令 \(v\otimes v\) 表示
\(w\mapsto\langle w,v\rangle v\)，并定义自伴算子
\[
 A=\sum_{\text{实 }x}m_xf_x\otimes f_x
     +2\sum_{\text{非实对 }z,\bar z}
                  m_z(g_z\otimes g_z-h_z\otimes h_z).
\]
直接取迹得到 \(\operatorname{tr}A=N\)。在实正交基上作张量展开，
复化后的同一有限实矩阵具有相同特征值，且
\[
 \|A\|_{\rm HS}^2
 =\left\|\sum_{z\in\mathcal Z}f_z(u)f_z(v)\right\|_{L^2(du\,dv)}^2
 =\sum_{z,w\in\mathcal Z}K(z-w)^2 .
\]
最后一步展开积分并用 \(w\mapsto\bar w\) 重排多重集。
右侧并非逐项非负；是总和等于Hilbert--Schmidt范数平方。

取 \(P=\sum_{\text{简单实 }x}f_x\otimes f_x,\ Q=A-P\)，则
\[
 P\succeq0,\quad\operatorname{rank}P\le s,\quad
 \operatorname{tr}P=s,\quad n_+(Q)\le r+k=:b .
\]
最后一项因为 \(Q\) 的非负部分来自至多 \(r+k\) 个秩一算子，
减去半正定项不会增加正惯性。又
\[
 s+2b\le N,\qquad
 D_{\rm distinct}=s+r+2k\ge s+b .
\]
第1节以 \(G=A,E_0=E_1=0\) 直接给
\[
 s\ge2N-\|A\|_{\rm HS}^2,\qquad
 D_{\rm distinct}\ge(3N-\|A\|_{\rm HS}^2)/2,
\]
恰为Lamzouri的Proposition2.1。没有额外设谱酉性或完整Weil正性。

**审计结论。** 该正式预印本提供清晰的证明路径，
有限不等式确实落在本项目已有二阶部分配置内；不是未知的新结构公理。
这不证明其 \(A\) 与本项目任一Gabor离散化矩阵具有相同四阶迹。
从二阶记录到MOM-1所需一侧四阶预算，仍须独立证明实际四点相关和
有限到整体误差；本接口同定本身不减少这些算术输入。
因此不以改写该短证为由启动新的四矩估计周期。

主代理与carrier_audit独立重建上述接口；gap_exception_audit和
midband_compute对本节最终全文只读复核通过。这里的[T]仅表示完整内部证明，
不表示新颖性、外部同行评审或Lean验证已经完成。

### 10.1 后续：二阶谱余项而非四阶预算

[304](304-mt-triple-geometry-and-second-moment-stability.md)在同一实际算子内
保留 \(\operatorname{tr}j(G_{\rm simple})\)，以不交三点几何给严格余量。
配合已知的固定平滑全谱二阶渐近和完整有理证书，
内部证明得到简单/不同零点下界约0.672509329/0.836254665 [T/R]。
这不推翻本节关于缺失四阶输入的判断：该增益根本不使用四阶矩。
同类Schur--Jensen机制已见公开工作稿，304明确不声称首次发现或世界纪录，
也不将新余项与其他未证明可加的稳定性预算相加。
