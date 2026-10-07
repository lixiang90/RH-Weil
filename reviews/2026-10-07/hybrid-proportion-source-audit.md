# 7/8无零输入与简单临界线比例：来源审计及实际截止接口

日期：2026-10-07。独立审计：progress_audit。范围：只读核查原始来源，阅读197、305和literature/README；只新增本报告，不更新旧稿、文献索引、Goal或Git。本报告的截止估计是条件于明确输入Hθ的纸面推导，不是新的零点比例纪录、Lean验收或RH证明。

## 1. 当前原始来源与计数口径

写N为全部非平凡零点计数，含重数；S=N₀ˢ为简单且在临界线的零点；Nₛ为全部简单零点；N₀为临界线零点，含重数；D=N_d为不同零点；Nₛ∪₀为简单或在临界线的并集，按原零点重数计。简单点自身重数为1。

| 原始来源与本次所见版本 | 主张/定理范围 | 本次核查范围 |
|---|---|---|
| [Alpöge–Furman 2608.13637v2](https://arxiv.org/abs/2608.13637v2)，2026-08-19；目前未见v3 | S/N≥C₀=0.672500703679…，D/N≥C₁=(1+C₀)/2=0.836250351839…；无RH假设 | 核读实际零侧和素数侧接口，未重新构建其Lean |
| [Lamzouri 2609.02882v2](https://arxiv.org/abs/2609.02882v2)，2026-09-08 | 相同C₀、C₁；新增并集≥C₂=0.887620008173…及(Nₛ+N₀)/(2N)≥C₁ | v2比本地归档v1多两项计数结果；核读§2–3及Appendix A |
| [BGST 2501.14545v3](https://arxiv.org/abs/2501.14545v3)，2026-09-01 | 其窄箱比例要求所有高程零点满足宽度b/logT的箱假设 | 核读箱定义与定理；无条件配对相关公式与条件计数结论必须分开 |
| [Biao Wang 2609.24167v1](https://arxiv.org/abs/2609.24167v1)，2026-09-21 | 声称S/N≥C₀+δ₀，D/N≥C₁+δ₀/2，δ₀=6.6662458…×10⁻⁸ | 核读实际算子、谱余项、三点步骤及常数组装；没有完成全文独立认证 |
| [Wang 2609.07918v1](https://arxiv.org/abs/2609.07918v1)，2026-09-07 | 将Lamzouri方法用于短区间 | 核对摘要与范围，未导入短区间常数 |
| [ainta当前README](https://github.com/ainta/zeta-simple-zeros) | 67.3008528…%研究稿；七点区间证书 | 仍自述研究草稿、欢迎独立验证；本次未重跑全域证书 |
| [Shi当前README](https://raw.githubusercontent.com/yuhangshi888/zeta-simple-zeros-673316977/main/README.md) | 67.3316977142%候选；局部Lean两证书推导 | README明确上游解析、Gram极限、谱包络等仍在形式化范围之外 |
| [Devine Zenodo 22066689](https://zenodo.org/records/22066689)，v1.0.3，2026-08-23 | 作者声称无条件67.3399%；另有条件67.92%及增益 | 本次复核记录说明，未重跑243个过渡域与完整账本 |

C₂表示并集，不表示简单临界线交集。平均界只推出max(Nₛ,N₀)/N≥C₁，不能推出两者各自≥C₁。不同零点的C₁界来自完整账本；对任意集合，S/N≥c本身不能推出D/N≥(1+c)/2。

最新Wang稿的数值约为67.2500770342%，低于已发现的67.3%候选；日期较新不等于数值纪录。其Δ_K=TrΨ(G_simple)与三点余项使项目304一类机制的新颖性还须谨慎。作者在致谢披露模型协助并承担正文责任，本报告不据来源身份判断数学真伪。Wang正文的三点与谱余项见[§2–4](https://arxiv.org/html/2609.24167v1)。

Lamzouri附录区分有限Hilbert不等式的无条件形式证书，以及依赖BGST配对相关和Riemann–von Mangoldt渐近的主定理证书。两项解析输入是已引用的数学定理；这不构成新的数学猜想，但也不是本次重跑的全依赖Lean验收。[Lamzouri Appendix A](https://arxiv.org/html/2609.02882v2)。

## 2. 7/8输入的准确范围

本报告以

\[
(H_\theta)\qquad\zeta(s)\ne0\quad(\Re s>\theta),\qquad
1/2<\theta<1
\]

作为明确输入。OpenAI公开[003形式化范围说明](https://raw.githubusercontent.com/openai/math/main/lean/docs/003.md)列出θ=7/8，覆盖ζ、全部正模数Dirichlet角色及指定Hecke函数；[实际Nonvanishing.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean)调用unconditional final assembly。这里承继前次只读源码审计结论：有完整Lean源码/目录声明，本次未重建kernel或Comparator验收。公开9月30日[7/8稿](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/README.md)与10月5日11/12替代证明并列；后者不是对7/8的撤回。

函数方程把非平凡零点的实部限制为

\[
1-\theta\le\beta\le\theta,\qquad
d:=\theta-\tfrac12,\qquad|\beta-\tfrac12|\le d. \tag{1}
\]

θ=7/8时d=3/8，边界β=1/8、7/8尚可包含零点。Hθ本身不规定重数，也不禁止β−1/2=O(1/logT)的小深度离线零点。

Lamzouri的缩放为

\[
z_\rho=i(\rho-\tfrac12)\frac{\log T}{2\pi},\qquad
|\Im z_\rho|\le\frac{d\log T}{2\pi}. \tag{2}
\]

BGST窄箱要求|β−1/2|<b/(2logT)，等价于缩放后固定宽度；(2)的宽度仍随logT增长。把7/8固定条带代入该窄箱定理是不合法的。

## 3. Lamzouri核的实际增长接口 [T | Hθ]

令η为固定实偶函数，supportη⊂(−λ,λ)，∫η²=1，
\(K=\widehat{\eta^2}\)，Fourier约定e^(−2πizu)。对
f_z(u)=η(u)e^(−2πizu)，直接积分给

\[
\|f_z\|_2^2\le e^{4\pi\lambda|\Im z|},\qquad
|K(z)|\le e^{2\pi\lambda|\Im z|}. \tag{3}
\]

由(2)，对实际零点及差点，

\[
\|f_{z_\rho}\|_2^2\le T^{2\lambda d},\qquad
|K(z_\rho-z_{\rho'})|^2\le T^{4\lambda d}. \tag{4}
\]

λ=1/2、θ=7/8时，指数分别为3/8、3/4。只用原临界条带0≤β≤1时分别为1/2、1；7/8给予单向量1/8幂、双点核1/4幂节省。这里是绝对值控制，不宣称单项K(z−w)²非负；只有完整共轭配对和才由实际自伴算子产生非负HS平方。

若η∈C_c^∞，任意整数m≥1，对u积分分部得

\[
|K(x+iy)|\le C_{\eta,m}
 e^{2\pi\lambda|y|}(1+|y|)^m(1+|x|)^{-m}. \tag{5}
\]

这给一个可交付的尾部预算。用单位高度计数N(t,t+1)≪log(t+3)，对同一0<γ≤T窗口、实际高程差≥H≥2，

\[
\sum_{\substack{\rho,\rho'\\|\gamma-\gamma'|\ge H}}
 |K(z_\rho-z_{\rho'})|^2
 \ll_{\eta,m}N(T)\,T^{4\lambda d}\log T\,H^{1-2m}. \tag{6}
\]

证明：在此区间|x|=|γ−γ'|logT/(2π)，|y|≪logT，(5)中的对数幂互相抵消到常数；固定ρ后按整数高程壳求和∑_{j≥H}j^(−2m)，再乘单位高度O(logT)与N(T)。令H=T^ε并取ε(2m−1)>4λd，右侧为o(N)。常数依赖固定η及m；不能允许η随T变化却沿用此固定常数。

这是有效截断/复杂核稳定性的接口；即使更粗条带也能在取更大m后获得o(N)，所以(6)单独不改变渐近比例主常数。

## 4. AF实际有限矩阵的一般padding定理 [T | Hθ]

此处完全保留AF的光滑窗口、全物理零点和实际采样，未以sharp窗口替代。记L=log(T/(2π))，X=e^L，I=[T,2T)，
α_k=T+2πk/L，0≤k<D_T=floor(LT/(2π))，
γ_ρ=−i(ρ−1/2)。令φ_L为AF的C²偶窗口，suppφ_L⊂[−L/2,L/2]，归一化q_L=a_LL²≍L²。保留其Poisson恒等式

\[
\sum_{k\in\mathbb Z}
 \widehat\phi_L(z-\alpha_k)^2=q_L. \tag{7}
\]

该恒等式对复z成立，平方不是绝对平方。φ_L的统一C²平滑给

\[
|\widehat\phi_L(r+iy)|
 \le C_\phi e^{L|y|/2}\min(L,|r|^{-1},|r|^{-2}). \tag{8}
\]

定义padding1≤P≤T/2及I_P=[T−P,2T+P)。v_ρ是D_T维实际采样向量。记

\[
G_P=q_L^{-1}\sum_{\gamma\in I_P}m_\rho v_\rho v_\rho^{\mathsf T},
\quad H=q_L^{-1}\sum_{\rho\ {\rm all}}m_\rho v_\rho v_\rho^{\mathsf T},
\quad E_P=H-G_P. \tag{9}
\]

“all”包括原显式公式中的全部非平凡零点，高程两方向均包含。对于固定T，(8)和单位高度计数保证绝对迹范数收敛。共轭对使H、G_P为自伴矩阵。参数d是深度上界，D_T是矩阵维数，两者勿混淆。

**结论：** 对固定φ窗口和θ，有

\[
\boxed{\ \|E_P\|_1\ll_\phi T^dP^{-2}\ }, \tag{10}
\]

以及较AF原述更细的

\[
\boxed{\ |\operatorname{Tr}G_P-N(I)|\ll_\phi T^dL,\quad
 |\operatorname{Tr}G_P-N(I_P)|\ll_\phi T^dL+PL\ }. \tag{11}
\]

若只沿用AF宽松的日志账本，可将T^dL弱化为T^dL²；两种版本的幂指数及padding门槛相同。原来源为[AF v2 Proposition 4.2–4.3及(2.8)](https://arxiv.org/html/2608.13637v2)。以下证明专门付清一般P与外侧零点的账。

### 4.1 网格与单点界

由|Imγ_ρ|≤d，(8)平方中指数≤X^d≍T^d。网格步长h=2π/L。对任意实中心s，

\[
\sum_{k\in\mathbb Z}
 \min(L^2,|s-\alpha_k|^{-2},|s-\alpha_k|^{-4})
 \ll L^2. \tag{12}
\]

理由：距中心≤h的O(1)项各O(L²)；距离为jh的其余近项的j⁻²和为O(L²)；|s−α_k|≥1后的j⁻⁴尾更小。故∑allgrid|widehatφ_L(γ_ρ−α_k)|²≪T^dL²。

若所求半侧网格距s至少R≥1，则积分比较给

\[
\sum_{\rm separated\ grid}
 |\widehat\phi_L(\gamma_\rho-\alpha_k)|^2
 \ll_\phi T^d\big(R^{-4}+LR^{-3}\big)
 \ll_\phi T^dLR^{-3}. \tag{13}
\]

实际右端α_{D_T}距2T为O(h)，对R≥1只改变常数；距端点≤1的所有零点归入下面的坏端点集。

### 4.2 尾部迹范数

rank-one复转置矩阵仍满足
||v vᵀ||₁=||v||₂²。I_P外的零点到I距离R≥P；由(13)除以q_L≍L²，

\[
q_L^{-1}\|v_\rho\|_2^2\ll_\phi T^d L^{-1}R^{-3}.
\]

对|γ|≤3T按单位高度计数求和给O(L/P²)；更远的两尾由∫_{3T}^∞log t/t³ dt≪L/T²控制。因P≤T/2，这一额外项也被L/P²吸收，遂得(10)。没有把P设为sqrtT后才应用估计。

### 4.3 首迹与外侧padding

对γ∈I且距两端≥1，由(7)“1减掉外网格尾”，使用(13)。坏端点集仅O(L)个零点，单点截断迹绝对值O(T^d)，因此总误差O(T^dL)。其余内侧尾的单位高度求和为O(T^d)，更小。

对γ∈I_P\I，必须估计**内网格**贡献，不能错误地说其所有外网格点都距γ至少R：γ本来就在外侧网格附近。距I≥1时(13)适用于内网格，累加贡献O(T^d)；距I≤1的贡献O(T^dL)。因此这些padding零点对Tr G_P的贡献也是O(T^dL)，uniform inP。合并即得Tr G_P=N(I)+O(T^dL)。最后N(I_P)−N(I)≪PL，得到(11)。

这也说明AF原来sqrtT情形的声明可成立，而直接逐行替换其内侧距离论证时必须补外侧账本；本报告未将此局部证明细节上升为对AF主定理的否定。

### 4.4 7/8给出的真实padding改善

设P=T^α。迹范数尾部o(1)的充分条件是

\[
d-2\alpha<0,\quad\alpha<1. \tag{14}
\]

旧条带d=1/2要求α>1/4；7/8的d=3/8只需α>3/16。端点账本PL=o(N)要求α<1，首迹T^dL=o(N)只需d<1。

例如**P=T^(1/4)**在7/8输入下给

\[
\|E_P\|_1\ll T^{-1/8}=o(1),\qquad
|\operatorname{Tr}G_P-N(I_P)|\ll T^{3/8}L+T^{1/4}L. \tag{15}
\]

原AF用P=sqrtT；(15)把实际padding缩短为T^(1/4)，同时保留其光滑测试与零点侧惯性结构。P=T^(3/16+ε)还可更短，任何固定0<ε<13/16均足以使两项所需误差消失。

## 5. 哪个误差真正主导固定比例

令N=N(I)≍TL，使用AF素数侧对全矩阵H的结果
||H||HS²=R(ψ)N+Oφ(N/L)，故||H||HS≪√N。不能先假定G_P的二矩近似再用它证明自身。源式见[AF v2 Theorem 5.7的proof中全矩阵H=G+E计算](https://arxiv.org/html/2608.13637v2)。

由H=G_P+E_P，

\[
\frac{|\|G_P\|_{\rm HS}^2-\|H\|_{\rm HS}^2|}{N}
 \ll_\phi
 \frac{T^{d-1/2}}{P^2\sqrt L}
 +\frac{T^{2d-1}}{P^4L}. \tag{16}
\]

rank–trace–inertia的简单零点账本给

\[
\frac{S(I)}N\ge2-R(\psi)
-O_\phi\left(
 \frac1L+T^{d-1}+\frac PT
 +\frac{T^{d-1/2}}{P^2\sqrt L}
 +\frac{T^{2d-1}}{P^4L}\right). \tag{17}
\]

不同零点用其相应完整账本，得到(3−R(ψ))/2和同量级误差。此处仅估计有限截止误差，不重新宣称C₀的来源。

d=3/8、P=T^(1/4)时，零点侧(17)的主导量不超过T^(−5/8)，素数侧1/L更大。AF Remark6.1另给保守的logL/L率；无论采用其较强二矩表述还是保守最终比例率，当前瓶颈都是对数误差，不是padding。Lamzouri固定平滑η路线公开估计为O_η(1/√logT)，也明显大于(6)/(15)在合适截止下的幂次误差。

仅为归一化二矩时甚至不必||E_P||₁=o(1)。Hθ下取固定P≥1，(16)也趋零；7/8给T^(−1/8)/√L，旧d=1/2则仅1/√L。此弱要求不能冒称迹范数尾趋零：固定P时(10)允许||E_P||₁增长。若要继续复用需要小迹范数的其它步骤，须保留(14)。

最优MT主项R_MT=1.327499296320…已由固定带宽的配对公式确定。把o(N)误差变得更小不会把它改成R_MT−δ。平滑η逼近MT的误差ε须固定后先取T→∞，再ε→0；本报告不偷偷使用η_T而忽略其导数常数。

## 6. 更高比例所需的新算术接口

### 6.1 扩大带宽：零側已经改善，素数側仍未付清

将实际光滑窗支持扩大到[−bL/2,bL/2]，固定b>0，用相应Nyquist网格。上述零侧指数换为bd，normalizer仍≍L²；(10)–(11)相应为

\[
\|E_P^{(b)}\|_1\ll_{b,\phi}T^{bd}P^{-2},\qquad
|\operatorname{Tr}G_P^{(b)}-N(I_P)|\ll_{b,\phi}T^{bd}L+PL. \tag{18}
\]

例如仍取P=sqrtT，零侧这两项要求bd<1：7/8给b<8/3，旧条带给b<2。这是**仅零侧**的准入范围。

实际素数多项式长度却变为X=T^b。AF Prop5.4的非对角误差是Oφ(L²X)；除以二矩主尺度TL³后为O(T^(b−1)/L)。b>1时失控，Hθ不能直接消去这一误差。需要新证明的具体接口是同一实际窗口下

\[
\mathcal O_1(T,T^b)+\mathcal O_2(T,T^b)=o(TL^3), \tag{19}
\]

连同扩大窗口后采样、Gamma与pole交叉项的合法误差。不能只证明(19)便忽略这些其它项。AF中mathcal O₁是n≠m项，含Λ(n)Λ(m)/sqrt(nm)、log(n/m)分母及T、2T端点相位；mathcal O₂来自同号(nm)相位。[AF v2 §5.3的实际分解](https://arxiv.org/html/2608.13637v2)。

Hθ可用于其原证明中离线深度、某些移线及一点评价；但ζ单函数固定无零区不自动提供所需长素数对相关。改善PNT对角余项，仍不会解除(19)。

### 6.2 一侧四阶预算：明确新比例门槛

承继[197](E:/codex-build/RH-Weil/notes/197-partial-weil-proportions-regions-four-moments.md:134)与[305](E:/codex-build/RH-Weil/notes/305-post-6725-literature-baseline-audit.md:109)的真实算子账本，若中心二矩v及中心四矩上界B₄确能在同一实际算子上成立，则超过目标p所需为

\[
B_4<\frac{(1-v)^2}{p}-1+2v. \tag{20}
\]

对待审p=0.673399，平窗v=1/3给0.326668306770742…；实际MT窗v=1−C₀给0.326602198303353…。这两个值不可互换。

所缺输入不是抽象四矩优化，而是实际四点算术和。素数侧出现长度约T²、系数(Λ*Λ)(n)/sqrt n的均方及shifted convolution；Hθ提供的实部上界本身并不估计这些相关项。将Lamzouri的二阶Hilbert算子与项目Gabor四阶迹相等也未被证明。必须先写出具体矩阵、参数及四点展开，再寻找7/8能进入的移线或短区间项；不能以形式上同为Weil配置替代比较。

### 6.3 固定有限块不能只因7/8而获新几何增益

令Z为任意固定、共轭封闭的有限局部缩放配置，max|Im z|=B<∞。用
ρ=1/2−2πiz/logT+i(3T/2)反缩放并统一平移高程，则充分大T时所有点落在(T,2T)内，并有
|β−1/2|≤2πB/logT≤3/8
对充分大T成立。因此7/8不排除任何这种固定局部复配置；它未删除局部Gram/惯性证书的潜在等号配置。

另一个常见误接法是缩小η带宽，让(2)的全部复差点落入某个核固定正性区域。若靠λ_T d logT=O(1)实现，则λ_T=O(1/logT)。归一化∫η_T²=1由Cauchy–Schwarz给
Q_T(0)=∫η_T⁴≥1/(2λ_T)≳logT。相应二阶主预算的Q(0)已经发散，2−R失去用处。此处只否定这种直接缩放策略，不宣称否定所有可能利用Hθ的正性核。

## 7. 可交付结论与推进顺序

本轮已经得到实际而可严格复核的接口：在原AF光滑采样矩阵上，H7/8把迹范数截止尾中的T^(1/2)换成T^(3/8)，一般padding为T^(3/8)/P²；P=T^(1/4)足以使尾部o(1)，最短幂次充分条件为α>3/16。该改进包括真实外侧padding计数，没有把x截止或抽象源读出冒充物理零点结果。

下一步应先把(10)–(17)作为实际矩阵的独立接口定理复核，随后选择一项尚未付清的新算术估计：(19)的大带宽均方，或(20)的实际一侧四阶预算。后续67.3%有限块证书已提供更高比较基线；重复三点几何或提高纯二阶误差速度均不能自动产生新的常数纪录。

本轮未修改305/literature归档版本，未下载替换旧PDF，未重跑任何外部大证书或Lean构建。源论文的解析定理、作者形式化声明、本报告纸面新估计和未证的新比例输入，以上均分别标明。
