# 原 MT 六邻域谱对偶与全链简单零点比例

2026-10-08。基线 main 030576085955927fcb63742c770b5cd171cb925f。

回到原路线后，本轮得到一个可接入实际零点计数的增量：沿用已经完整重放的七点证书，把有限邻域谱对偶直接用于整条简单零点链，避免每个固定长分块的端点费用。严格比例表达式为

\[
 p_6=\frac{65025C_0-130}{64778}
   =0.673058110110743497\ldots,
 \qquad C_0=\frac32-\frac1{\sqrt2}\cot(1/\sqrt2).
\]

这里的比例计简单临界线零点，分母按重数计所有非平凡零点。它是引用解析输入与计算机辅助有限证书支持的渐近下界。当前无零边界仍为引用输入下的 σ*≈0.874957019420099；本轮未确认新无零条带，也没有据此撰写新边界论文。

## 1. 原对象与新的全链费用 [T/E]

保留 [477](477-original-vaughan-reduction-and-replayed-multipoint-proportion.md) 的原 MT 核

\[
 f_0(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}1_{[-1/2,1/2]}(u),
 \qquad k_0(x)=\widehat f_0(x),\qquad w(x)=k_0(x)^2.
\]

令 j(t)=(t−1)²（0≤t≤2）、j(t)=2t−3（t≥2），J(G)=tr j(G)。对任意有序实点 x₁≤⋯≤x_s，令 G 的条目为 k₀(xᵢ−xⱼ)。本轮证明

\[
 J(G)\ge\alpha s-\eta(x_s-x_1)-6\alpha,
 \qquad \alpha=\frac{247}{65025},\quad\eta=\frac{26}{13005}.
 \tag{1}
\]

空点列按 J=span=0 处理。完整作者证明与实际计数传递见
[研究源](../reviews/2026-10-08/hybrid-mt-six-neighbor-spectral-dual-and-actual-counting-research-compression.md)。下面说明关键费用为何闭合。

## 2. 有限邻域对偶，不要求全 Gram 范数至多2 [T]

任意正 Gram G，置 D=G−I。若 Hermitian B≤I，则

\[
 J(G)\ge2\operatorname{tr}(BD)-\operatorname{tr}(B^2).
 \tag{2}
\]

这是同一谱余项的变分下界：J(G)=tr D²−tr(D−I)₊²，而 D−B≥D−I。最小最大原理给 ‖D−B‖²_HS≥‖(D−I)₊‖²_HS，配方即得(2)。B不必正定。

取 δ₀=3809/4000。新全实轴证书给

\[
 \sup_{x\ge r\delta_0}|k_0(x)|\le M_r,
 \quad(M_1,\ldots,M_6)=\frac{(1805,1064,757,588,480,406)}{10000}.
 \tag{3}
\]

因此 ΣMᵣ=51/100。对相邻间距至少 δ₀ 的任意点列，构造仅保留前六个邻居的矩阵 B：当 1≤|i−j|≤6 时 Bᵢⱼ=u k₀(xᵢ−xⱼ)，其余为0，u=50/51。Schur行和给 ‖B‖≤2uΣMᵣ=1，故(2)合法。所有保留边的效率相同：

\[
 J(G)\ge cE_6,\qquad c=2u-u^2=\frac{2600}{2601},
 \quad E_6=2\sum_{r=1}^6\sum_{i=1}^{n-r}w(x_{i+r}-x_i).
 \tag{4}
\]

这是有限邻域试探矩阵的范数界，未声称任意分离全 Gram 的最大特征值至多2。

原七点 F₆≥19/5000 的全域证书已在477重放。将它在连续七点窗口上求和，每gap至多计6次，每r邻居边至多计7−r次，得到

\[
 E_6+\frac{\mathrm{span}}{500}\ge\frac{19}{5000}(n-6).
 \tag{5}
\]

n≤6时右端非正，仍成立。(4)与(5)直接给 J≥αn−ηspan−6α。没有按280点分块，也没有新增连续subaction假设。

## 3. 密集小簇与全部实点 [T/E]

沿原点列，以gap<δ₀分成连续簇。所有单点簇组成的点列至少δ₀分离；其跨度至多原总跨度。

新证书同时给 k₀(δ₀)>1/10。f₀为正且支撑于[−1/2,1/2]，积分导数显示 k₀在[0,1]单调递减，故gap<δ₀的相邻点有 k₀(gap)>1/10。

对m≥2的簇，取floor(m/2)个互不交叠的相邻两点块，每块的j迹为2k₀(gap)²。标量凸函数的trace pinching给

\[
 J(G_{\rm cluster})\ge2\lfloor m/2\rfloor/100
 \ge m/150>\alpha m.
 \tag{6}
\]

先pinch成所有单点簇的一个主块和各非平凡簇，再用(4)–(6)，即可得到全域(1)。每个坐标仅支付一次；没有把重叠窗口的j迹直接相加。

## 4. 同一实际零点算子与比例闭合 [T/R]

使用 [304 §5](304-mt-triple-geometry-and-second-moment-stability.md) 与 [477完整实际桥](../reviews/2026-10-08/hybrid-original-multipoint-envelope-and-actual-counting-research-compression.md) 的固定平滑接口。先固定光滑单位profile f_ε→f₀，再取高度T→∞，最后令profile误差趋于0。简单临界线点的实际列精确单位，Gram为k_ε(xᵢ−xⱼ)；其余全部复零点仍保留在同一自伴算子A中。

在全轴 |k_ε−k₀|≤ε 下，仍以原k₀造B，所以 ‖B‖≤1 精确保留。对偶线性项总误差至多2εΣᵢⱼ|Bᵢⱼ|≤2εn；密集簇的两点费用仍有严格富余。于是实际Gram满足

\[
 J_\varepsilon\ge(\alpha-2\varepsilon)s-\eta X_T-6\alpha,
 \qquad X_T=\frac{T\log T}{2\pi}\sim N(T).
 \tag{7}
\]

引用的完整去权二阶合同给 tr A=N、‖A‖²_HS=(R_ε+o_ε(1))N，R_ε→2−C₀。原重数与惯性账本给

\[
 s\ge(2-R_\varepsilon)N+J_\varepsilon-o_\varepsilon(N),
 \qquad D\ge\frac{(3-R_\varepsilon)N+J_\varepsilon}{2}-o_\varepsilon(N).
 \tag{8}
\]

联立并按固定profile、高度、profile极限的顺序，得到

\[
 \liminf\frac{N_0^s(T)}{N(T)}\ge p_6,
 \qquad\liminf\frac{D(T)}{N(T)}\ge\frac{1+p_6}{2}
 =0.836529055055371748\ldots .
 \tag{9}
\]

不同零点结论使用(8)的同一完整预算；没有假定一般配置都满足D≥(N+s)/2。比例装配本身不需要7/8条带。

## 5. 严格证书、增量与当前目标

[新runner](../scripts/hybrid_mt_six_neighbor_geometry_certificate.py)使用128bit Arb，完整覆盖[3809/4000,7]的241910个闭cells，mesh1/40000。每格严格余量大于10⁻⁸；x≥7由递减有理包络141125/3619653<203/5000支付。强radius界递减，覆盖的是每个x≥rδ₀的完整半轴。没有以浮点采样验收。

[新执行报告](../output/hybrid-mt-six-neighbor-geometry-certificate.json)绑定最终源码与原七点记录；--check完整复跑全部闭cells与无穷尾。严格比例区间及文档绑定由[本轮检查点](../output/hybrid-mt-six-neighbor-proportion-checkpoint.json)核验。脚本验证有限核与代数，不自动认证外部解析定理。新增证明另经不同作者全文审查。

项目实际下界从477的67.3009652279…%提高到67.3058110110…%；不同点下界为83.6529055055…%。这仍低于[305](305-post-6725-literature-baseline-audit.md)登记的更高公开候选，不作世界纪录声明。已知MT算术合同、ainta七点证书及[351谱对偶](351-fixed-radius-stability-and-actual-zero-transfer.md)、[355短簇支付](355-short-cluster-payment-and-separated-five-gap-reduction.md)保留先行来源，本轮完成的是原核六邻域与全链装配的具体支付。

原四矩whole界仍为[476](476-original-fourth-growth-five-sevenths-with-ivic-density.md)的T^(5/7+ε)。完整Type II和保留四份素数权、共同相位的signed near预算尚未得到新费用，不能把本次二阶比例增益当作四阶常数或κ参数。后续继续研究原联合四矩与近共振，Goal active。
