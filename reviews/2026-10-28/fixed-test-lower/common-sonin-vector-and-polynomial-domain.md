# Th6.2 lower：共同 Sonin 向量、Gevrey 平滑与全部多项式定义域

2026-10-28；unit_height 独占原件/定义域稿，供 fresh/root 消费。恢复 G20261027、STATE、D20261028F、唯一 next-fixed-test-lower-proof-gate，check/show 通过。只核固定作者 v2 的 Theorem6.2 lower 所需共同 \(H_0\) 支链；不消费同定理 upper、6.4、6.5 或后章，不改 STATE/cadence/Git，不预 C048/585 或计轮。

## 1. 判定及精确交付

**共同向量前件可闭合。** 可以固定单个 raw Mellin 向量 \(H_0\)，使

\[
 H_0\in S_0\mathcal H,\qquad H_0(0)>0,\qquad
 |H_0(t)|\le C e^{-c\sqrt{|t|}},\qquad
 t^jH_0\in S_0\mathcal H\quad\text{对每个 }j\ge0. \tag{H}
\]

这里空间是原物理范数经酉 log/Mellin 变换得到的 \(L^2(\mathbb R,dt/(2\pi))\)，不是 completed Mellin 的加权范数。\(S_0\) 是 gap1 的真实 archimedean Sonin 正交投影。\(H_0,C,c\) 可先于 \(X,n,p\) 及测试源选择，且不随它们变化。多项式不是只有每个单项形式合法：对**全部有限次数的 complex 多项式**均得到实际同空间元素。

本稿不把作者所说的未平滑 raw kernel section 为 \(O(1/|t|)\) 作为已核输入。较弱、已付的 \(O(\sqrt{\log(2+|t|)})\) 界已足，经同一个合法平滑直接推出 (H)。这不改变 trial/source、Euler 乘子或空间；只移除一条不必要的更强渐近依赖。加权 polynomial 集中及 Lemma6.1 的 cofinal 算术费用由其他独占稿/root 核，不由 (H) 单独宣布完整 lower 已证。

## 2. 固定原件与实际必要来源

作者原 Markdown：`literature/local/2026-10-28-core-source-location/bramble-trace-rstation-2-v2.md`，61862 raw bytes，SHA-256
`541098314b2ddc5f8645babf82086e87d16c46188268cbc7ed6cfc1f98720058`。
本次只读 §6 的同空间定义、Theorem6.2 lower 的 \(H_0\)/poly 段及必要 references9/10；不借后章支付前件。

既有实际原件范围见 C005-flux trace-source-audit、532/533。旧 Burnol0208121v1 原 PDF 当前缺失，故本次必要下载另存新目录，不覆写旧路径，也不把恢复字节算新数学。两份 primary 原件通过固定 arXiv 版本取得：

| 原件 | 新本地文件 | 现场 raw 身份 |
|---|---|---|
| J.-F. Burnol, *Two complete and minimal systems associated with the zeros of the Riemann zeta function*, math/0203120v7，最后修订2004-02-25 | literature/local/2026-10-28-fixed-test-lower/burnol-two-complete-0203120v7.pdf | 25 PDF页；321788 bytes；SHA `cff449f51fe65cb8ae72f64b17e3dd4d9f5fb903776f9b825be77bfd75606039` |
| J.-F. Burnol, *Sur les espaces de Sonine associés par de Branges à la transformation de Fourier*, math/0208121v1，提交2002-08-15/首页内文2002-08-14 | literature/local/2026-10-28-fixed-test-lower/burnol-sonine-0208121v1.pdf | 7 PDF页；117262 bytes；SHA `1890a3867e745c342be3a70eeb2948c673bfb644fc4f392f9302d0b9c96acc3b`，与旧缺失原件SHA完全一致 |

arXiv [v7版本页](https://arxiv.org/abs/math/0203120v7)及 [v1版本页](https://arxiv.org/abs/math/0208121v1)只用于版本元数据核对；数学消费来自本地固定原 PDF。前者不混 JNTB16(2004),65–94 的期刊排版，后者不混四页 C.R. 排版。

必要原文范围如下：

- [9] PDF5：\(K_a\) 的双 gap 定义、Theorem2.1 的 completed entire/连续评价；PDF7 的 bare Mellin/\(dt/(2\pi)\) 区分；PDF8 的 Proposition4.3、Note9；PDF18 的 Lemma7.4 及紧随的有限评价独立说明。只消费这些必要前件，不输入该文其他 ζ 零点完备性定理。
- [10] PDF2–3：双 gap 非零 Sonine 空间及 positive-halfline cosine 约定；PDF5 的实际 projection/Cor5；PDF6 Theorem8 和必要结构定义，PDF7 的 evaluator/jump文本仅作定位，未输入其完整结构 proof。Theorem8 是 completed structure-function 公式，不直接等于一个已显示的 raw section \(O(1/t)\) 定理。
- [532](../../../notes/532-actual-sonin-prime-symbol-and-compact-weil-bridge.md) §2–3 的 bare evaluator、实际 arch 密度/clipping/连续性及 \(\Gamma(t)=2\theta'(t)\) 增长；raw SHA `dc9ff79c622ed692edfd393c2851e5cc7fcab0a7f5fe41cce82ba69b45a82f09`，沿原 root 已付范围消费，不重证。

## 3. 大 gap 中的原点评价确实非零

在 \(\mathscr H=L^2((0,\infty),dx)\) 中，令

\[
 (\mathcal Cg)(x)=2\int_0^\infty\cos(2\pi xy)g(y)dy,
\quad K_a=\{g:g|_{(0,a)}=(\mathcal Cg)|_{(0,a)}=0\}.
\]

这里 \(a>1\) 是**先固定**的常数，不是 cofinal 参数。Burnol 的偶函数实现可按其 positive-halfline cosine 公式与此同一化；不把全实线偶函数范数和 positive-halfline 范数无声混用。

必要已知输入为 \(K_a\ne0\)、raw Mellin 的解析延拓/连续评价，以及 [9] Prop4.3 的合法除零性质。其非零性在 [10] PDF2–3 给出；不能只从“评价连续”推出“评价非零”。以下补齐这一步：

取 \(0\ne g\in K_a\)，写
\(G(s)=\int_0^\infty g(x)x^{-s}dx\)，在需要处按解析延拓解释。completed 变换
\(\pi^{-s/2}\Gamma(s/2)G(s)\) 为非零 entire 函数。在 \(s_*=1/2\) 处 Gamma 因子有限且非零。若 \(G(s_*)=0\)，其零阶有限；Prop4.3 可逐次将 \(G(s)\) 除以 \(s-s_*\)，每次仍为同一个 \(K_a\) 的 raw Mellin 变换。有限次后得到同空间函数在 \(s_*\) 非零。因此

\[
 E_{a,0}:g\longmapsto\mathcal Mg(0),\qquad
 (\mathcal Mg)(t)=\int_0^\infty g(x)x^{-1/2-it}dx
\]

是 \(K_a\) 上非零有界线性泛函。[9] Note9 和 Lemma7.4 后的说明与这个原点评价结论一致。此处的“原点”是 raw 临界线坐标 \(t=0\)，不是 completed Mellin 的 \(s=0\) pole/端点。

按第一变量线性的 Hermitian 约定，令其实际 Riesz 向量为 \(k_{a,0}\in K_a\)：

\[
 E_{a,0}(g)=\langle g,k_{a,0}\rangle,\qquad
 E_{a,0}(k_{a,0})=\|k_{a,0}\|^2>0. \tag{1}
\]

Burnol 为保持参数解析而使用的 bilinear evaluator不能无声代此 Hermitian 向量；在实点 \(s_*=1/2\)，经相应共轭/非零 Gamma 标量即可得到 (1)。本稿从有界泛函直接定义 Riesz 向量，避免该记号混同。

## 4. raw kernel 的足够增长：无需 \(O(1/t)\)

设 \(G_a(t)=\mathcal M k_{a,0}(t)\)。因 \(a>1\)，有实际闭子空间包含 \(K_a\subset K_1\)。若 \(k_{a,t}\)、\(k_{1,t}\) 分别是同一 bare 评价在两空间的 Riesz 向量，则

\[
 k_{a,t}=P_{K_a}k_{1,t},\qquad
 \|k_{a,t}\|\le\|k_{1,t}\|. \tag{2}
\]

旧532的 arch bare密度与 \(\Gamma\) 高载波比较，以及 compact频段上的连续评价，给

\[
 \|k_{1,t}\|^2\le C_1\log(2+|t|)\qquad(t\in\mathbb R). \tag{3}
\]

若532将 bare evaluator附了 \((2\pi)^{-1/2}\)，这里只在 \(C_1\) 中计入固定 \(2\pi\)，不改变所需阶，不引入新规范。Cauchy–Schwarz 与 (1)–(3) 给

\[
 |G_a(t)|=|\langle k_{a,0},k_{a,t}\rangle|
 \le\|k_{a,0}\|\sqrt{C_1\log(2+|t|)}. \tag{4}
\]

这足够且非循环：用的是**固定 gap1、无 finite Euler 的旧 arch evaluator**，不使用待证的 cofinal Sonin trace lower、Theorem6.2 upper或Theorem6.4。也不从 completed Gamma 的指数大小直接猜 raw section 的衰减。

原稿较强的 \(G_a(t)=O(1/|t|)\) 此处保持**未消费**；本稿未判其为假。Theorem8 的引用本身没有替代这项更强 raw 渐近的单独推导。由于 (4) 经下一步已经推出原稿真正使用的 (H)，它不是本 lower 支链的关键未付前件。

## 5. 固定 Gevrey 卷积确实保两侧 gap

定义实际酉 log map 及 dilation：

\[
 (Wg)(y)=e^{y/2}g(e^y),\qquad
 U_vg(x)=e^{-v/2}g(e^{-v}x),\qquad
 WU_vg(y)=Wg(y-v).
\]

取固定 \(0<\delta<\log a\)，选实偶、非负、积分1的
\(\psi\in C_c^\infty((-\delta,\delta))\)，Gevrey order2，满足

\[
 \|\psi^{(j)}\|_1\le A B^j(j!)^2\quad(j\ge0). \tag{5}
\]

这样的选择可由归一化 \(\exp[-1/((\delta/2)^2-v^2)]\) 于 \(|v|<\delta/2\)、外部置0得到，使支撑严格包含于 \((-\delta,\delta)\)。局部 Cauchy 导数估计结合到 bump 边界距离的 \(e^{-c/(\delta/2-|v|)}\) 衰减给 (5)：取复圆半径为到边界距离的固定小倍数，优化该距离得到第二个 factorial。\(A,B\) 只依这一固定 bump与\(\delta\)。无需由 \(X\) 或测试源选择平滑器。

定义 actual Bochner 积分

\[
 g_0=\int\psi(v)U_v k_{a,0}\,dv\in\mathscr H,
 \qquad H_0(t)=\mathcal M g_0(t)
              =\widehat\psi(t)G_a(t). \tag{6}
\]

积分在原 \(\mathscr H\) 内合法，\(\|g_0\|\le\|\psi\|_1\|k_{a,0}\|\)。每个 \(U_v k_{a,0}\) 的物理 gap至少为 \(ae^{-\delta}\)；而
\(\mathcal C U_v=U_{-v}\mathcal C\)，其 Fourier gap同样至少为 \(ae^{-\delta}\)。故

\[
 g_0\in K_b,\qquad b=ae^{-\delta}>1,\qquad
 H_0\in\mathcal M K_b\subset\mathcal M K_1=S_0\mathcal H. \tag{7}
\]

没有假设 dilation 对 fixed Sonin空间给酉表示；用的是它对两个实际 gaps 的反向缩放，以及固定留出的余量。把更大 gap直接当 gap1不损范数，是闭子空间包含，不是改对象。

原点评价连续，故可移过 Bochner 积分；等价地用 (6) 的 raw Mellin乘子恒等式延拓到实点，得到

\[
 H_0(0)=\widehat\psi(0)G_a(0)=\|k_{a,0}\|^2>0. \tag{8}
\]

由 (5) 分部积分任意次，
\(|\widehat\psi(t)|\le A(B/|t|)^N(N!)^2\)。选择 \(N\) 为固定小倍数 \(\sqrt{|t|/B}\) 的整数，得
\(|\widehat\psi(t)|\le C e^{-c\sqrt{|t|}}\)。与 (4) 相乘后，\(\sqrt{\log(2+|t|)}\) 可由减小固定 \(c\) 吸收，故

\[
 |H_0(t)|\le C_0e^{-c_0\sqrt{|t|}}. \tag{9}
\]

\(H_0\) 解析且在0非零，所以存在固定邻域 \(|t|<\varepsilon_0\) 上的正 lower。特别对 \(J_X=[\pi/\log X-(\log X)^{-2},\pi/\log X+(\log X)^{-2}]\)，当 \(X\) 充分大时 \(\inf_{J_X}|H_0|>c_*>0\)。这项阈值只依固定 \(H_0\)，不依所选多项式。

## 6. ALL log derivatives 和所有 polynomial 倍的实际定义域

不能直接对未平滑 evaluator 的 cutoff jump施任意阶 Euler导数。这里先作 (6)，然后令

\[
 g_j=\int\psi^{(j)}(v)U_v k_{a,0}\,dv\qquad(j\ge0). \tag{10}
\]

每个积分是原 \(L^2\) 向量，且由与 (7) 相同的逐腿 gap准入，**每个 \(g_j\) 均属于同一个 \(K_b\)**。log坐标中
\(Wg_j=\partial_y^j(\psi*Wk_{a,0})\)，这是 \(L^2\) 弱导数，且由所有阶卷积平滑实际为光滑函数。因此

\[
 \mathcal M g_j(t)=(it)^jH_0(t),\qquad
 \|t^jH_0\|_{L^2(dt/(2\pi))}
 =\|g_j\|_{\mathscr H}
 \le A B^j(j!)^2\|k_{a,0}\|. \tag{11}
\]

这同时核了乘 \(t\) 的全部 selfadjoint-multiplier domain，而不只核形式导数。对应 physical Euler算子是
\(x\partial_x+1/2\)，并非裸 \(x\partial_x\)。Fourier后的导数也保 gap，因为 (10) 中 \(\mathcal C\) 可作为有界酉算子移过 Bochner积分，然后用 \(U_{-v}\) 的支持。这样不需要对未知边界行为强行作无界算子交换，也不遗留 cutoff delta。

故对于任意有限 complex 多项式 \(p(t)=\sum_{j<n}a_jt^j\)，

\[
 pH_0\in\mathcal M K_b\subset S_0\mathcal H,
\quad
 \|pH_0\|\le A\|k_{a,0}\|
        \sum_{j<n}|a_j|B^j(j!)^2. \tag{12}
\]

(11) 允许 \(j\) 随 \(n\) 成长，费用显式增长；没有承诺导数费 uniform-in-j。另一方面，(9) 给所有实线矩的统一组织

\[
 \int_{\mathbb R}|t|^{2j}|H_0(t)|^2dt
 \le\frac{4C_0^2\Gamma(4j+2)}{(2c_0)^{4j+2}}. \tag{13}
\]

该式由 \(u=\sqrt{|t|}\) 直接得到，足以向另一独占稿交付其 \(e^{C n\log(n+L)}\) 矩费用所需的固定常数；本稿不代为验证其 Legendre/global weighted 比较。

## 7. finite Euler 后的全 cofinal trial 是合法元素

对每个 finite \(X\)，原稿的 \(D_X(t)=\prod_{p\le X}(1-p^{-1/2-it})\) 是实际有限Euler乘子，

\[
 0<\prod_{p\le X}(1-p^{-1/2})
 \le |D_X(t)|\le\prod_{p\le X}(1+p^{-1/2})<\infty.
\]

用本门已经固定的原 finite-S range equality（按旧 CCM 实际同构/Gram规范消费），得到

\[
 \mathcal V_{X,n}=\{D_XpH_0:\deg p<n\}\subset S_X\mathcal H.
\]

每个元素在原物理范数下有限，\(n\) 是任意有限整数，可随 \(X\) 增长。\(H_0\not\equiv0\)、\(D_X\) 实轴无零，故乘子映射在多项式空间上单射，\(\dim\mathcal V_{X,n}=n\)。没有把 \(D_X\) 当酉、没有删 \(G^{-1}\)，也没有用裸 Hardy trial或 completed norm替代实际 Sonin空间。

这里证明的是全部 cofinal trial 的 **domain/dimension**；其 weighted norms 集中、目标源 \(|\widehat r|^2\) 在相关 annulus 的 lower、n的可用规模及真实 trace求和仍须对应独占证明。不能以本稿的合法性替那些费用付款。

## 8. 前件状态、合法修补与净值

| 前件 | 本稿状态 | 实际支付/范围 |
|---|---|---|
| 任意先fixed a>1 的非零双gap空间、bare评价连续 | 已付原件/旧设施 | [9] Th2.1、[10] PDF2–3；completed→bare在s=1/2只除非零固定Gamma标量 |
| 原点评价非零 | 已闭 | Prop4.3有限次除零；不用未知ζ零点、一般“连续”标签或自由向量坐标 |
| 未平滑 raw section \(O(1/t)\) | 未消费，未判假 | 原稿较强断言非必要；(2)–(4) 用旧532评价界严格替代 |
| Gevrey2平滑、固定双gap余量、原点不消 | 已闭 | 固定a/δ/ψ、actual dilation Bochner积分、\(b=ae^{-δ}>1\)、intψ=1 |
| ALL \(t^jH_0\) 同空间及原norm | 已闭 | (10)–(13)，费用显式；不把未平滑jump施强导数 |
| full weightedpoly concentration/prime uniform error | 不在本稿消费 | H0给所需原域与固定常数；另稿/fresh/root闭合 |
| 全Th6.2 lower/actualK成长数学分类 | 待root综合 | 本稿不预报告proved、不计数学轮，不借upper/sharp续门 |

采用 (4) 替代未核 \(O(1/t)\) 是合法的必要前件弱化：构造仍为“fixed larger-gap原点评价＋同一个compactGevrey2 log卷积”，最后交付与原lower完全相同的 (H)，没有改变目标、正负方向或缺陷项。无需保留未付更强渐近来阻止一个已经实际闭合的 H0 门。

这段大gap/evaluation/Gevrey/poly-domain 机制属于已知 Sonin设施和标准原范数推导；本身不构成新的cofinal trace lower。若整体 lower 的 weighted算术链通过，其 actual cofinal净值另按最强旧比较，不能因本稿是来源支链就把新成长费用藏为0，也不能因补齐这个支链就先报新数学。whole4/5仍为负惯性UPPER，primitive/mixedRR/corecoupling/Ξ及有费非有限秩/source-adapted修复范围未改变。

## 9. 实际下载、提取、目视与未审范围

默认 sandbox 中通过10808的首次curl连接失败，未取到字节；随后在已授权下载范围经工具升级以同一命令级 `127.0.0.1:10808` proxy 下载成功，无全局代理改动。两原PDF按上表 raw身份固定。只读操作未运行PDF authoring标记；未改写原PDF。

使用PDF技能、bundled pypdf提取文本（仅本地ignored诊断），Poppler `pdftoppm -scale-to 1600 -png -singlefile` 渲染，并实际 view_image 完整目视：

| 本地 PNG（tmp/pdfs/fixed-test-lower/） | 目视内容 | SHA-256 |
|---|---|---|
| h0-two-p5.png | [9] K_a与Th2.1、completed/bilinear evaluator约定 | 49b88341577a6f0f32ce12764751b8ef1e760c01f19433a381b20c4d1e405b49 |
| h0-two-p8.png | [9] Prop4.3 proof/Note9的临界线合法除零 | 957129fa99ba29230ca476d3561f8b97bb18df91896c4387d0f2d888c9f2af6e |
| h0-two-p18.png | [9] Lem7.4及随后finite evaluator独立说明 | cfcaef27bfdbbffc1ddb8efe67b5791e5514171c4afb1a882a0e72e2cc59444c |
| h0-sonine-p2.png | [10] dt/(2π)、双cutoff空间闭且proper | 304bf17051f793a44d913b3b8f059ca1fadc4da1aa4d91e8c3efabe79b0bf2fb |
| h0-sonine-p3.png | [10] 非零/任意大gap、cosine空间定义 | 2eeb01025b51f006156124517b91a8a32b9e4229ce5a1e968a226b6b57774826 |
| h0-sonine-p5.png | [10] Th4真实正交投影与Cor5 | 7e70d383f9b2026abdc89bda1771d33345cb386c172f8b7660ad46e075ccea09 |
| h0-sonine-p6.png | [10] Th8为Gamma-completed结构函数陈述 | b87bcc807a53fa08f2eeca80008ebfbe13f22c98b39d757f92c911eb3cc6dd4c |

[9] PDF7和[10] PDF1/7亦读必要文本/版本或locator，没有将其称为已完整目视。新v7 PDF的其余页只作locator扫描，不输入零点完备性论证；[10]不声称本轮重新认证全部7页所有 proof。未读后续引用，不下载第三篇论文。

无pending process。独占稿为实际前件证明与原件记录，出稿不代root消费；交付给 weightedpoly 分支的就是 (H)、(11)–(13) 及其固定量词，稿后不自行续 upper/6.4/6.5。
