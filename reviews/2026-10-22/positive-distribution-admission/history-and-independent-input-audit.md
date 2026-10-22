# 正函数域分布逼近：历史去重与独立输入审查

2026-10-22，独占分支。仅写本稿，不改STATE、合同或cadence。实际核读最新结构空间稿、Goal／frontier／决策D20261022J，以及174、177、562、563、566、567和下述回顾原件；对notes／reviews／goals/reviews作关键词定位。没有声称重读全仓几百篇，也没有重新认证旧证明。下述“未找到”是有界检索结论，不是世界优先权判断。

## 1. 本次准入的准确对象

root本轮拟测试的对象不是未知经典零点的正谱，而是同一个真实椭圆曲线

\[
 E/\mathbb F_5:y^2=x^3+x+1,
 \qquad N_1=9,\qquad P(T)=1+3T+5T^2.
\]

其已付数据为

\[
 A=\begin{pmatrix}0&-5\\1&-3\end{pmatrix},\quad
 H=\begin{pmatrix}1&-3/2\\-3/2&5\end{pmatrix}>0,
 \quad A^THA=5H,\quad U=A/\sqrt5.
\]

原件：[563§5](../../../notes/563-distribution-side-weil-certificates-and-heat-complete-monotonicity.md)、[完整点数／递推原稿§1–3](../../2026-10-20/grh-distribution/arithmetic-counts-and-conservative-realizations.md)。全次数trace由有理性与Cayley–Hamilton支付，有限N2、N3枚举只是交叉检验；不得把它们外推为全递推。函数域正号的独立几何来源另见[567§2–3](../../../notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md)，并归属其所核Milne／Weil原证明，不冒称本轮新证明函数域RH。

对基变换到\(\mathbb F_{5^m}\)，写\(L_m=m\log5\)。完整源为

\[
 W_m=L_m\sum_{n\in\mathbb Z}\operatorname{Tr}(U^{mn})\delta_{nL_m}.
 \tag{1}
\]

对任意\(a>0\)必须把**整个**源作centered dilation：

\[
 W_{m,a}=a(\mathrm{dil}_a)_*W_m
 =h\sum_{n\in\mathbb Z}\operatorname{Tr}(U^{mn})\delta_{nh},
 \qquad h=aL_m.
 \tag{2}
\]

这不是只移动prime atoms。若原completed对象的中心变量是w，则相应对象为E_m(aw)，原degree-zero／two的极点中心变为\(\pm1/(2a)\)。全部pole、closed places及proper powers在(1)的精确平衡身份中保留。不同分片可能很大，但本稿不把它们分别有界或可分别极限列为已付。

## 2. 旧资产已经付了什么

| 旧原件 | 最强已付内容 | 不能再算本轮新增 |
|---|---|---|
| [174§2、§4、LONG-2](../../../notes/174-nonconstructive-existence-and-branch-map.md) | 正锥投影／分离及有前件的非构造接口；函数域到数域完整正分布极限是条件计划 | GNS、compactness本身造正号；把q-to-1命名为独立算术输入 |
| [177§1–3](../../../notes/177-random-log-grid-fejer-no-free-lunch.md) | 随机grid平均恰为Fejér；同一闭凸锥的随机混合不能改善均方距离 | 随机混合或平均自身是新增能量 |
| [562§2、§6](../../../notes/562-generalized-rh-continuous-g-integers-and-spectral-multiplicity.md) | 真正continuous正P／Π／M给\(W=2\cos(\tau u)\)；正型锥D′闭 | 闭锥传正性；已有cos正段平方和 |
| [563§5–6](../../../notes/563-distribution-side-weil-certificates-and-heat-complete-monotonicity.md) | (1)的全周期身份／正H证书；经典完整源不在直接有限ODE或有限TV类 | 把有限数据重写为unitary／Gram，或重复Gamma不是Radon测度 |
| [566§4、§7](../../../notes/566-source-closed-forms-and-full-weil-heat-trace-tests.md) | 全returns圆周bundle普通heat；有限compact图UV首项失败；一个合法无限图首项匹配、次项失配 | 更多固定图／低谱／Weyl首项拟合 |
| [567§2–3](../../../notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md) | 同一曲面实际RR／截面乘法容量先给负交数，再得全部mixed Gram | 将formal graph／trace／transpose视为独立正号 |
| [10-20六笔记回顾§5C](../../../goals/reviews/2026-10-20-notes-561-566-analytical-rh-lessons.md)及[来源门](../../2026-10-20/grh-six-note-review/next-direction-admission-audit.md) | unscaled真实曲线在\(0<|u|<\log2\)没有非零comb点，经典有Gamma／pole背景；明确保变尺度／背景修复 | 再以同一个fixed-normalization support gap排所有多尺度逼近 |
| [最新结构空间稿§9](../../../goals/reviews/2026-10-22-weil-structures-and-existence-space.md) | 固定经典目标纤维；独立正对象的完整分布像逼近是合法策略，不必产生几何极限 | 以“存在性等价”为理由一概否定独立存在性证明 |

174早期“循环性”字样的数学有效部分是“等价包本身没有新增输入”。等价性不证明任何独立存在性论证必然循环；本轮须服从最新结构稿的精确修正。

## 3. 基变换相位递近：未在上述历史中找到的同强合成

全仓定向检索组合了base change／扩域／基变换／phase／相位与approx／逼近／dilation／缩放／dense，并检查cos通用性、曲线正分布闭包；没有定位到下述完整构造。

由已付H，U是二维正能量空间上的orientation-preserving rotation，写\(\operatorname{Tr}U^n=2\cos(n\theta)\)。\(\theta/(2\pi)\)无理：若U有限阶，则\(2\cos\theta=-3/\sqrt5\)为代数整数；其在\(\mathbb Q(\sqrt5)\)中的norm为\(-9/5\)，矛盾。这里使用标准“root of unity和为代数整数”，不使用经典ζ零点，也不先用一般Weil RH。

标准圆旋转逼近可选\(m_j\to\infty\)，使

\[
 \delta_j=\operatorname{dist}(m_j\theta,2\pi\mathbb Z)\downarrow0,
 \qquad\delta_j>0.
\]

对固定\(\gamma>0\)，取\(h_j=\delta_j/\gamma\)、\(a_j=h_j/L_{m_j}\)。则完整(2)成为

\[
 W_{m_j,a_j}=h_j\sum_{n\in\mathbb Z}2\cos(\gamma nh_j)\delta_{nh_j}
 \longrightarrow 2\cos(\gamma u)\,du
 \quad\text{于D′}.
 \tag{3}
\]

这是保留**全部returns**的黎曼和，不是只留下首return或有限谱拟合。对\(\gamma=0\)，可取\(h_j=\sqrt{\delta_j}\)，此时有效频率\(\delta_j/h_j\to0\)，极限为\(2\,du\)。

最便宜的全对象误差检验是：对任意\(\phi\in C_c^1\)，固定γ时

\[
 \left|h\sum_n2\cos(\gamma nh)\phi(nh)
 -\int2\cos(\gamma u)\phi(u)du\right|
 \le2h\bigl(\|\phi'\|_1+\gamma\|\phi\|_1\bigr).
 \tag{4}
\]

逐cell用fundamental theorem of calculus即可支付；对γ=0候选另加有效频率趋0的compact误差。root若将此列为新数学设施，应在主稿或审查中独立核(3)–(4)、m_j选择和分片规范，而不能以本稿历史检索代替证明。

**新合成的准确净值：**旧563的一个真实曲线及所有基变换，在允许centered dilation后，不用smearing就能产生任意cos正核的分布极限。旧174只有退化计划，旧563／566只给单曲线全周期实现，10-20的support反测明确没有处理这种合法修复。因此不应将这项真实设施一概归为0来源。

**必须扣除的更强旧分析后果：**562的continuous正段已经直接有cos核，标准dilation给任意频率；再用标准Bochner–Schwartz／正测度离散逼近，解析层的even正型分布由cos正混合生成并不新。本轮若完成相应密度定理，新处在于把**固定真实函数域几何族**接到这个已知解析锥，不能宣称首次证明Bochner型普适性。

## 4. 对闭包定理的消费边界

设\(\mathcal C_E\)为(2)的有限正实权混合。若主稿精确证明

\[
 \overline{\mathcal C_E}^{D′}
 =\{\text{real-even positive-type distributions on }\mathbb R\},
 \tag{5}
\]

其正向包含使用旧全源正性和闭锥，反向使用(3)＋正测度截断／离散化。正型分布自动tempered及其Bochner–Schwartz表示是标准定理；对非compact谱尾仍须给固定多项式增长和足够阶测试导数的误差，不能只在可数测试上逐点收敛后无连续性地断言所有D′收敛。

(5)会给实际的新方法范围信息：允许如此宽的基变换、缩放和正混合后，“存在正函数域逼近”不再给比Weil正型更窄的独立membership条件。它不证明经典目标属于此闭包；将\(W_\zeta\)放进去仍须新的算术逼近输入。它也不排更加刚性的primitive／pole marking、费用受控或同对象RR逼近类可能提供新判别力。

同理，(5)只讲完整线性分布。有限混合及centered dilation未必仍是一个整数重数的通常zeta除子，非整数权还可能产生分支；它们是独立正源证书。不能由(5)自动恢复ordinary determinant、几何source lift、同一Picard族或原算术完整目标的完成化。

对连续正段，(3)能重建已有cos核；对continuous负段\(2\cosh(u/4)\)应由既有compact 2×2负Gram排掉，说明宽闭包仍确实区分正反，不能声称其稠密于所有even分布。经典完整Γ／all prime powers／双pole始终是同一个\(W_\zeta\)，不能因核class普适而省去任何分片。

## 5. 原域／范数与有限部分预算

令\((D_ar)(v)=\sqrt a\,r(av)\)，它在原L²(du)酉。完整(2)有准确关系

\[
 Q_{W_{m,a}}(r)=a\,Q_{W_m}(D_ar).
 \tag{6}
\]

源支撑从[-L,L]变为[-L/a,L/a]；这是成长窗，不是同一个固定函数域窗。Fourier约定\(\widehat r(t)=\int e^{-itu}r(u)du\)下

\[
 \|D_ar\|_{H_{\log}}^2
 =\frac1{2\pi}\int\bigl(1+\log(2+a|t|)\bigr)|\widehat r(t)|^2dt.
 \tag{7}
\]

特别a≤1时此项不增加，但(6)的a与几何窗扩大／截面容量／trace尾费不能混同或删除。对compact卷积平方的(3)–(4)，直接由原\(L²\)及导数付C¹误差是可行的：\(\|r*s^*\|_1\le\|r\|_1\|s\|_1\)，导数同样处理；这不是原全线Dlog上的统一bounded几何map。只得到compact D′逼近时，也不自动有Gaussian heat／ordinary trace的全time尾运输。

若目的仅是以完整D′极限推出compact源的Weil正性，不要求每一个有限函数域近似对象精确消掉**经典**405关系：不同目标的中间源可以有不同关系。在D′中将极限识别为已知完整\(W_\zeta\)之后，可另行引用旧405在\(\mathcal S_{\exp}\)上的恒等式描述该极限的全关系；D′收敛本身不推出\(Q_j(r)\to0\)对noncompact405源成立，更不产生几何lift。537的compact非根保留则由其极限值保证。若另要同一固定目标几何source map，必须逐层给对应关系／degree／原费；这比(5)更强，不能从分布闭包反推。两项命题应分别陈述。

Gamma在0的穿孔核为\(-1/(2|u|)+O(1)\)，故完整\(W_\zeta\)不是局部有限Radon测度（563已付）。对(2)，\(|\operatorname{Tr}U^{mn}|\le2g=2\)给

\[
 |W_{m,a}|([-R,R])\le2g(2R+h).
 \tag{8}
\]

所以正混合若\(\sum c_jg_j\)及\(\sum c_jg_jh_j\)一致有界，其D′极限仍是局部有限测度，不能等于经典完整源。紧支正型mollifier卷积在稍大窗保持相同TV控制。此是563非Radon事实＋标准TV紧性的直接后果，不能将它重计为已经排了所有scaled正近似；发散权预算、无限维谱尾及精确signed finite-part抵消是合法未排修复。(5)若成立正会包含超出统一TV预算的极限。

## 6. 证明来源与本轮停止／晋级建议

本次没有新外部论文定理在手。使用来源分为：函数域几何／点数有理性与RR正性属Weil、Hasse及所核[Milne原讲义](https://www.jmilne.org/math/xnotes/pRH.pdf)；全周期分布身份、具体H及heat lift是仓库563／566已核实现；无理圆旋转、黎曼和和Bochner–Schwartz是标准工具；本轮候选新增合成是固定真实E的基变换＋缩放在完整分布层生成cos及相应闭包范围。没有对世界文献优先权作判断。

建议root据(3)的真实新设施准入一轮明确范围的数学合同，并在同轮核全positive-mixture closure、连续反例、完整规范和误差，随后停当前普适类。若最终只得到(5)，应报告它解决了宽逼近类的**方法范围／设施覆盖**，没有解决经典membership；不靠继续微调phase、grid或mollifier延长合同。

强旧actual净后果仍是542＋555→557的whole leading4/5负惯性上预算，不是负谱lower；此候选没有改善实际ζ的core／coupling／Ξ，也没有给固定目标的独立容量。新局部设施范围与宏观瓶颈改变必须分开结算。
