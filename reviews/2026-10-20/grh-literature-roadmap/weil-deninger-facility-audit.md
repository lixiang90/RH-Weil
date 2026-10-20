# Weil 原证明、Deligne 与 Deninger：可迁移设施的来源审查

2026-10-20；独立文献／路线图原稿。范围为来源核读与准入比较，0 数学轮；不新建合同、不改 STATE、不宣称经典 ζ 有新增正性。以下依赖笔记 001/002/073/290/307/363/562–567，主线冻结基线仍为 0c4f/≤538。

## 1. 本审查改变什么选择

应保留两条独立机制，不能把它们都缩成“存在一个正内积”：

1. **曲线的有效性—限制映射—RR 机制**：先构造真实截面和有限容量，再得到对应代数的负指数／正迹。
2. **叶间 Kähler—Hodge 机制**：先有独立的正局部度量、微分复形与可下降的 Hodge 分解，再把极化送到上同调。

Deligne 的 tensor—全局极点机制是第三个来源；单个 g-prime 计数的偶次幂并不提供其全局极点输入。

文献带来的一个更具体候选是含 preserved leaves 的双 conormal 迹公式：它同时处理闭轨道和类似 Γ 的对角奇性。但它使用 b-supertrace，不是正算子的普通热迹；原稿中有限部分的显示式还须校正／明确规范。它值得一次严格的来源规范比较，尚不值得直接开启未知极化的数学合同。

## 2. 原证明过程：不能把 1940 年公告当成已经写完的设施

本次核读强度如下；没有访问到的原书不能写成已审完整原证明。

| 原件 | 实际核读位置 | 可消费内容与访问限制 |
|---|---|---|
| Weil，*Sur les fonctions algébriques à corps de constantes fini*，CR 210 (1940), 592–594 | 本次未获得三页原扫描；1941 原文开头明确回指该公告。另核 Weil 致 Cartan 1940-04-08 原信，收于 Audin 编通信集，印刷 p79–80 | 保留公告的历史定位；不把未审 lemma 归为本次已付款原证明。[通信原件](https://audin.pages.math.unistra.fr/livres/smf_doc-math_6.pdf) |
| Weil，*On the Riemann Hypothesis in Function-Fields*，PNAS 27 (1941), 345–347 | 三页全部；尤 p346 的 quotient ring/complementary correspondence，p347 的多项式正性与插值 | 正性前端为实际 complementary correspondence 的不可约性与次数。p347 注2明确说 Severi 的复数理论须重写到特征 p。[原文](https://www.pnas.org/doi/pdf/10.1073/pnas.27.7.345) |
| Weil，*Sur les courbes algébriques et les variétés qui s’en déduisent* (1948) 与 *Variétés abéliennes et courbes algébriques* (1948) | 前书 BnF 扫描入口已定位，工具访问失败；未声称核读全书 | 1941 留下的基础几何／对应责任由后续专著系统实现；精确章节若要再消费，应先获取原件。[BnF 前书](https://gallica.bnf.fr/ark:/12148/bpt6k3372566b) |
| Mattuck–Tate，*On the inequality of Castelnuovo–Severi* (1958), 295–299 | Springer 原版书目与 Manin 俄译 (1960), pp25–28 全文；p26–27 为限制映射，p28 为图／固定点后果 | 实际可构造限制映射的单射性给截面维数上界，而 RR 给同一对象下界。不是只命名 RR。[原版 DOI](https://doi.org/10.1007/BF02941959)，[原论文译本](https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=127&what=fullt) |
| Grothendieck，*Sur une note de Mattuck-Tate* (1958), 208–215 | 作者原文的公开 LaTeX 重排版 §§1–2 全读、§3 定位；PDF p1 署明 2022 重排，不冒称原扫描 | Thm1.1、(1.5)–(1.8) 与 §2 (2.1)–(2.12) 将 RR／Serre 对偶、乘法和容量转成 Hodge index；567 已恢复这一机制。[重排原文](https://denisevellachemla.eu/AG-Mattuck-Tate.pdf) |

### 2.1 Weil 1941：正迹来自 complementary correspondence 的真实效果

设对应群模掉 principal 与两类 fiber 对应得到代数，transpose 为 \(\gamma\mapsto\gamma'\)，迹为次数之和减 coincidence number。p346 的独立几何步骤构造 generic complementary correspondence，其 bidegrees 为 \((g,m)\)，满足

\[
2m=\sigma(\gamma\gamma'),\qquad m\ge0.
\]

随后才利用 Frobenius \(L L'=q\)、全部点数的迹公式，对**每个整数系数多项式** \(F\) 得 \(\sigma(F(L)F(L)')\ge0\)；延到实系数后，用有限多根上的插值排除错误 reciprocal-conjugate 配对。这个顺序不预设纯性。

对应到一般分布时，形式定义 \(\sigma\)、transpose 或乘法很容易；困难是从它们之外构造上述非负 \(m\)。567 连续全 Π 与 290 已证明，正的不同图交数不能替代这一 signed-combination 有效性。

### 2.2 Mattuck–Tate：一个比“造完整上同调”更小的设施目标

原译本 p26–27 对 \(C\times C'\) 的足够大双次数除子 \(D\) 构造

\[
H^0(D)\longrightarrow\bigoplus_{i=1}^{r}H^0(D|_{C_i}),
\qquad r=d+1-g',
\]

通过逐个选择非基点的 fiber，使该限制映射单射，得到
\(h^0(D)\le(d+1-g')(d'+1-g)\)。同一 RR 二次项给 \(D^2\le2dd'\)。

这是可迁移设施的**研究建议**：先找同源截面模块、真实限制／evaluation 映射与单射性、可计算的目标容量；未必先完成全套未知 \(H^1\)。其量化容错可用567(13)–(14)承接。该建议不提供经典的截面，也不复活553中已失败的 global bounded L² evaluation：代数限制单射与全局有界读出不是同一命题，域、norm 和 principal 兼容性必须另核。

### 2.3 Rosati 是独立正性来源的另一种封装

Jacobian 上 ample divisor 给 \(\lambda\)，从而 \(a^\dagger=\lambda^{-1}a^\vee\lambda\)。\(\operatorname{Tr}(aa^\dagger)>0\) 来自实际有效除子的交数；\(\pi\pi^\dagger=q\) 则由 Frobenius/Weil pairing 给出。可核现代原证明为 [Milne §1 Thm1.27–1.30](https://jmilne.org/math/xnotes/pRH.pdf)。这里用 Milne 核 Rosati 技术链，而非用一篇综述代替上述全部历史原件。

001/307 已有这一封装与椭圆曲线 degree 基准；073 已有双向 subexponential growth→纯性、uniform bounded averaging→极化。不应把“未知 H 正定／未知双向温和”重新包装为本轮新来源。

## 3. Deligne：应搬走的是全 tensor 系统及其全局极点预算

核 [*La conjecture de Weil I* §3，Thm3.2、Lemmas3.3–3.6、(3.7)，印刷 pp283–285](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)：lisse sheaf 带交替非退化配对、足够大的 symplectic monodromy，以及有理局部特征多项式。偶 tensor 幂的局部幂迹非负；monodromy 识别 coinvariants，cohomological trace formula 独立限制 tensor L 函数的全局极点。正级数的局部／全局收敛半径比较，最后让 tensor 阶趋于无穷。

设施责任是：同一对象族上的 tensor、对偶、全部局部因子与全局极点定理。一般 g-prime 的 \((\text{positive count})^{2k}\) 只付了非负性，完全未付这个极点定理。更不能把已证纯性写成一般 Hodge standard positivity 或原 Frobenius 半单性均已证明。073 的范围已在567修正；本次没有增强该结论。

优先级：在未出现实际 tensor 载体、可证明的全阶 pole 控制之前，把这条保留为条件机制。不能通过给每个 tensor 次序另选完成化／额外无零因子来假造统一系统。

## 4. Deninger：已有真实的无限维正性设施，但算术 membership 尚欠

### 4.1 1998 纲领必须与后来已证部分分开

[Deninger ICM1998，§3 pp168–174、§4 pp176–183](https://ems.press/content/book-chapter-files/27103?nt=1) 给局部 Γ/Euler 因子的 regularized-determinant 描述；算术全局 cohomology、兼容正 Hodge star 与完整 global determinant 属于期望。cup-product 的 derivation 与 conformal star 关系给中心化生成元的反对称性。对一般非自伴闭算子，仅形式反对称不足以宣布其闭包反自伴；域与谱身份还须支付，见001/002。

本次可消费的是必要设施的组织，不能从局部因子已有 determinant 推全局 RH，也不能从一串已规定零点的 determinant 反向宣布独立几何。

### 4.2 2002 的 Kähler–Riemann foliation 是比未知 H 更实在的模块

[Deninger–Singhof，math/0204111，§§3–4，4.4、Prop4.6，PDF pp8–14](https://arxiv.org/pdf/math/0204111) 从 bundle-like metric、叶间 Kähler identities 和 smooth reduced Hodge decomposition 构造可能无限维的正极化。dense-leaf 假设使顶次空间一维；holomorphic leaf map 若将 Kähler class 乘 \(q\)，则其 degree \(n\) 作用归一化后保持所构造的正内积（原文称 unitary endomorphism）。无限维消费时不从这一等式擅自补出指定 Hilbert completion 上的满射性、反自伴生成元域或全连续谱定位；若用真实可逆 flow，则相应群与闭包须另核。

这确实容纳无限维，说明“类 RH 正性必须有限 genus／离散算术梳”过强。但要用于某个 g-integer 系统，尚需从分布及规范对偶构造该载体、证明源到 cohomology 的 map、trace 与全部 Γ/pp/pole；本论文没有给经典 ζ 的 membership。

反向测试必须保留：[Deninger–Singhof 2001，*A counterexample…*，§1 Prop1.2、§2，pp209–219](https://www.numdam.org/item/10.5802/aif.1821.pdf) 的 Heisenberg nilmanifold 例显示一般 foliation 的 reduced cohomology 可含 harmonic forms 看不到的无限部分；smooth Hodge 分解及某种 naive trace-to-cohomology 传递会失败。不能把“叶上有正 Laplacian”自动消费成目标上同调的完整 trace。

### 4.3 2018–2024 的 arithmetic dynamical space：存在轨道不等于完成载体

[Deninger，1807.06400v4 (2024-02-07)，Introduction pp1–3、§10 pp62–64](https://arxiv.org/pdf/1807.06400v4) 已由 rational Witt vectors 构造算术 schemes 的拓扑 flow；闭点给的是 compact packets of periodic orbits，而非每个闭点恰一个轨道，flow 没有 fixed points。一般“foliation”未必局部平凡。故不能直接套2002 smooth Kähler–Riemann theorem，也不能忽略 packet multiplicity 或没有 Γ 边界的事实。

可迁移的是 multiplicative arithmetic source→flow 的独立构造方式；g-integer 任意实／连续分布没有原 scheme 的 residue-field 和 Frobenius 数据，Witt 构造不能无成本全覆盖。

### 4.4 新具体设施：含 preserved leaves 的双 conormal 迹公式

[Álvarez López–Kordyukov–Leichtnam，2402.06671v2](https://arxiv.org/pdf/2402.06671v2) 本次只核 Introduction Thm1.3.1–1.3.10、§§2.7.1–2.7.7、6.1、5.8、6.7及相应局部显示式；**未审完176页证明**。

已陈述并有论文证明的结构：\(I\) 为 conormal、\(I'\) 为 density-dual conormal，分别有短正合序列；必须合用两个 reduced cohomologies。Thm1.3.7–1.3.10 把 b-supertrace 的短／长 heat-time 极限、preserved-leaf 与 closed-orbit 贡献接起来。一般 metric/\(\eta\) 选择会留下 \(c\delta_0\)；b-trace 不在 commutators 上消失。它不是普通 Hilbert trace，更不自动是正测度。

根消费必须把“已证结构”与以下**我们自己的原件比较／疑点**分开：

1. §5.8 Prop5.8.1 固定 normal-density 权为 \(e^{-(k+1)\kappa_Lt}\)，§6.7 Prop6.7.1 固定对偶 jets 权为 \(e^{k\kappa_Lt}\)。来源为 \(\xi^{t*}\rho=e^{\kappa_Lt}\rho\) 与 density-transpose；这两节未给可自由分别选择两个半轴 twist 的定理，也未给兼容正反线性 Hodge 算子。
2. intro 印刷 p7/PDF13 在 \(\mathbb R^\times\) 的组合写为 \(\sum_L\chi(L)|e^{\kappa_Lt}-1|^{-1}\)。若 \(\kappa=-2,t>0\)，手乘 \(-e^{-t/2}\) 便有 classic off-zero arch profile
   \[
   -\frac{e^{-t/2}}{1-e^{-2t}}.
   \]
   同一个 global scalar twist 在 \(t=-v<0\) 给 \(-e^{-3v/2}/(1-e^{-2v})\)，不是目标 even profile。局部相似不能付款 two-sided identity；选择 \(e^{-|t|/2}\) 本身也不是 flow character。
3. 该 p7 对 \(W_L\) 的 displayed extension，照字面在 \(\int_0^\infty\) 中全程减 \(2f(0)/(|\kappa_L|t)\)。对 \(f\in C_c^\infty,f(0)\ne0\)，无穷端有 logarithmic divergence；且对一般 signed \(\kappa_L\) 的写法与上方非 even kernel 也须核对。已视觉核 PDF，不能归咎 OCR。这里不据此否定整篇迹公式，但**不能消费这条显示式为现成 canonical Γ finite-part**。
4. 合法核比较可先任选 \(\chi\in C_c^\infty,\chi=1\) near0，并用
   \[
   \langle\operatorname{fp}_{\chi}K,f\rangle
   =\int_{\mathbb R}K(t)\,[f(t)-f(0)\chi(t)]\,dt
   \]
   （\(K(t)=|e^{\kappa t}-1|^{-1}\)）定义有限部分。不同 \(\chi\) 相差 \(c\delta_0\)。这是独立的分布定义修复，**不是原文已选定的 arithmetic contact**；其与 \(\psi(1/4)-\log\pi\)、conductor/Haar 规范的关系仍待证明。
5. 叶的 Euler coefficient、轨道符号 \(\epsilon_\gamma(k)\)、pole cohomologies 及 multiplicities 都由真实载体决定，不能为配公式手选。在3维可定向闭叶情形 \(\chi(L)=2-2g_L\) 还有偶整数限制；保留 twisted coefficients/更一般载体，但须另给来源。

**建议的一次来源门**：查既定 density-dual sequence 是否有允许的、相容的权运输，使 K/K′ 两侧共同匹配完整 Γ，且 canonical Mellin Γ 规范能固定 \(\delta_0\)。须先澄清上述 displayed finite-part；若只能手乘绝对值 character、独立调半轴、任调 contact，门即停。这项比较即使成功也只付 arch-source 设施，不付 Weil 正性、RR、全 pp 轨道 identity 或任何 ordinary heat identity。

补充边界：[Álvarez López–Kim–Morishita，2410.20758v1，Introduction (A1)–(A4)、Thm1.8、2.4–2.5](https://arxiv.org/pdf/2410.20758v1) 在指定3维横截/Riemannian flow 类证明 regularized determinant；dense-leaf 分支还用 isometric leafwise homotopy。其类无 preserved leaves/fixed points，不能直接承担经典 Γ 项。真实 determinant 进展应保留，不能倒推当前 arithmetic space 已适用。

## 5. 设施层级与四类模型的验收

| 层级 | 对一般 g-integer 要独立支付什么 | 真曲线 | 290 正整数 Euler 负例／连续负段 | 连续 \(Z_c\) 正段 | 经典／数域 |
|---|---|---|---|---|---|
| 源与规范 | \(P\to\Pi\to M\)、对偶核、权、Γ/contact/poles；不能由 \(B(s)\) 改目标 | 闭点/扩域/权全给 | 能通过 Euler/FE；故尚不识别 pure | 562 给完整连续 Π，Γ=0 模型 | Tate/theta/标准Γ可规范已知对象；任意分布不自动具备 |
| 对应与迹 | composition、transpose、principal quotient、full trace，非只不同图正交点 | 真实 \(C\times C\) | 290/567 通过大量形式设施仍失正 | 567 formal correspondence 可实现 | CC/Meyer 来源有强表示；合法商/全source须逐项核 |
| 正性前端 | complementary effective object，或限制单射+RR预算，或独立 Kähler/Hodge 分解 | 有 | 必须有一项失败；不是靠否定正Euler | 二维独立 ODE energy 可给证书，不要求伪造曲面 | 未造同源 RR/metric+allsource；核心责任在此 |
| 完整实现 | full Weil identity 或全 time 普通 heat trace；普通/relative/b-trace分清 | 563/566 全周期 lift | 566 nonunitary 正闭form 仍 source-heat不等 | \(K=(c-1/4)I_2\) 已付 | Γ有限部分/pp/pole、carrier/norm/domain/limits 未同时付 |
| 扩大类 | 连续谱、无界容量、graded weights；按对象选 ordinary trace/semifinite/分布迹 | 高维须分次 | negative controls 不能被定义删除 | 连续分布不妨碍pure；连续谱混合有分支 | 任意g-integer不会全成立，研究目标是自然可验的额外设施 |

验收时先固定 source 与 duality，再比较极化／指数；不能只在知道纯性后造 Hilbert 载体。数域 ideal-label、archimedean Hodge 数据与全局 product formula 比裸 g-prime measure 多；抹掉这些数据后，不应要求重新唯一恢复全部设施。相反，一般框架应允许这些数据成为独立输入，并验证其在正反例间的判别力。

## 6. 给 root 的路线顺序与止损

1. **一次具体 arch-source 门**：以上双 conormal 的两侧权、FP规范与实际 classic Γ 比较；失败就保留有用 facility、停止该源，不扩图形类模型。它比重读“未知平方RR”更可能改变规范／域判断。
2. **几何长期主责**：从实际 source 候选选一个有限 signed correspondence 系统，造同源 section/restriction map，核是否有 MT 式注入和567预算。必须给具体 map/range/norm/principal 兼容性；没有实际数据就不新开数学合同。
3. **解析备选保持实际输入**：560 的完整 joint 源及 compact error 已付；具体 actualreceiver 的 signed mixed 计算可作为与几何路线互相校准的门。不能被更多 unknownH/CM 名字替代。
4. **tensor 支线的重准入**：须拿出独立全阶 tensor/pole 定理，单独 source positivity 或自己假定的 meromorphic continuation 不够。

本稿新增的是原件定位、可迁移设施的更细分层，以及有实际公式可判的候选／疑点。567 RR budget 与本稿路线建议没有造出经典正性。最强实际 ζ 后果仍 542+555→557 whole leading4/5；成长 core、560 K 的 signed/growth/norm与完整 Ξ 识别均未变。本稿不能用于结算新数学轮或完成长期 Goal。
