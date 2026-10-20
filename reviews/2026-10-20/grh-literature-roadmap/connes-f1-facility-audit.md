# Connes–Consani／F₁：可移植设施、原件边界与路线图接口

2026-10-20。用户明确请求扩大文献搜索、综合审视并建立路线图；本稿是来源审查，0新数学研究轮。
不续C030、不创建运行Goal、不将来源重读计为新定理。这里只消费下面列出的原件章节，
不声称审完每篇全文或所有参考文献。root需将本稿与Lapidus、Weil原证明及仓库历史的独立原稿合并。

## 1. 最有用的结论

1. **2018 §3.4没有付出567所需的平方RR二次项或Γ误差。** 固定v1 PDF21–22页的五步研究程序，
   第2步要求消除cutoff对角发散，第3步要求平方上的HRR且二次项等于实际显式公式的自交，
   第4步才由错误符号推出实际截面存在。§7解决的是连续Frobenius对应的提升，不是上述HRR。
2. **2007的原始Weil证明组织值得和567的surface RR容量并列。** 它通过曲线RR取得有效对应，
   再以canonical截面的评价行列式限制碰撞次数，将复合对应的迹变为非负。
   可迁移目标因此不只“建立一个平方上的RR”，也可是一套可乘截面、评价及碰撞预算。
3. **2020起有比形式交数更具体的分析桥。** Schwartz核将局部图／对角主值变为真正算子核；
   Sonin压缩迹独立为正，且其与Weil源之差可计算。其全球化欠的是差项的符号／费用，
   不是再声明有一个正空间。560已经在每个fixed finite-S及fixed支撑上推进这条桥。
4. **2026的Jacobian、绝对曲线和twistor设施是真对象，但不是已经正极化的全ζ上同调。**
   它们改善层、模、点、框架、局部动力学的组织；不能由名称直接搬用Rosati或Hodge index。
5. 一般g-integer数据首先给乘法半群／测度和Mellin卷积。它不自动给每个局部域的加法、
   自对偶Fourier变换、Tate主值正规化、product formula、实际层的截面或有效锥。
   从Beurling数据到这些设施的函子／比较本身是额外责任，不能写成普遍自动推广。

## 2. 本轮重新打开的12份一级原件

版本采用arXiv提交历史或固定v1/v2 URL，不采用网页抓取时间或HTML内自动排版日期。
以下每行只报告被核章节的结果，不把整个研究计划升级为定理。

| 原件、固定版本与定位 | 已证对象／设施 | 本目标可用什么、还欠什么 |
|---|---|---|
| Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, [math/9811068v1](https://arxiv.org/pdf/math/9811068v1)，1998-11-10；§VII Thm4，PDF31–32；§VIII Thm5与后续number-field讨论；Appendix II Thm6，PDF77–78 | 由真实局部域、自对偶加法角色和Haar测度构造semi-local Hilbert空间；cutoff迹恢复局部主值项及明确的对角发散。原Hilbert谱实现与全部零点／共振的区别保留 | 为完成化常数与finite-part提供外部校准；$R_\Lambda=\widehat P_\Lambda P_\Lambda$不是正交投影。semi-local迹公式不能免费变为全球正性；§VIII Thm5在原件首先表述于正特征global field，不应省掉范围 |
| Connes–Consani–Marcolli, *Weil’s proof and the geometry of the adeles class space*, [math/0703392v1](https://arxiv.org/pdf/math/0703392v1)，2007；§2.3，PDF9–11；§2.4 PDF12；§6 Thm6.1/Prop6.2，PDF28–29；§7 | cyclic module／余核给全部零点对应的Lefschetz迹；degree/codegree为两个Mellin矩；曲线RR、评价行列式与有效对应证明真正Weil正性 | 将“源／关系／次数／配对”分别固定。Prop6.2明确是RH等价，不是无条件正性。§2.4的bivariant对应、RR=index、effective=onto module字典部分仍为拟议；原像V不自动是几何主除子 |
| Connes–Consani, *Geometry of the Arithmetic Site*, [1502.05580v1](https://arxiv.org/html/1502.05580v1)，2015；§6 Prop6.21/Def6.22、§7 Thm7.7 | 算术site、unreduced/reduced square及Frobenius对应已构造；连续参数对应有精确复合规则 | “平方不存在”的旧诊断错误；真正欠完整交叉／有效性／RR。两无理参数乘积为有理时出现切向变形，不能把全部复合替成普通群律。一般g-prime标签不自动提供同一范畴 |
| Connes–Consani, *Geometry of the scaling site*, [1603.03191v1](https://arxiv.org/html/1603.03191v1)，2016；§5.4 Thm5.17、Lemmas5.18–5.19，固定PDF约32页 | 周期轨道$C_p=\mathbb R_+^\times/p^\mathbb Z$上的除子、theta与连续维数RR：Dim H0(D)−Dim H0(−D)=degD | 支付真实一维截面存在性，可作局部／周期基准；不是算术平方的二次RR。连续维数的意义和极限须保留，不能套普通有限维l(D)代数 |
| Connes–Consani, *The Riemann–Roch strategy: Complex lift of the Scaling Site*, [1805.10501v1](https://arxiv.org/html/1805.10501v1)，2018-05-26；§3.1–3.4，PDF17–22；Thm4.2；§5、§7 | 真实adelic复提升、适当almost-periodic解析函数的Jessen／tropical下降、连续除子的离散提升以及Witt形式的Frobenius提升 | 对连续源重要：不必先离散化g-prime分布；但Jessen实现有精确兼容条件。§3.4的relative迹→交数、HRR与对角正规化是任务，不提供567(13)–(14)的实际$C_j,\epsilon_j,\eta_j$ |
| Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, [2006.13771v1](https://arxiv.org/html/2006.13771v1)，2020-06-24；Thm1、Thm3/§4 Thm7，§5–6、Appendix E/F | Schwartz核与quantized differential处理真实Γ的主值；全compact源有Sonin positive trace = $W_\infty+\epsilon$；规定支持窗与消失矩下给强domination | 这是独立分析正源与精确余项，不仅是RH等价。Thm1限$\operatorname{supp}g\subset[2^{-1/2},2^{1/2}]$及指定矩；全尺度domination未由该定理给出。$W_\infty$的Fourier密度$2\theta'$、符号、常数与prime项必须按原公式运输 |
| Connes–Consani, *Riemann–Roch for the ring Z*, [2306.00456v1](https://arxiv.org/html/2306.00456v1)，2023-06；Thms1.1/5.1 | 绝对基底$\mathbb S$上的Arakelov divisor与指定S-dimension；整数RR包含修正取整$\lceil\deg_2D\rceil'+1$ | 给可构造的H0/H1与有限／无穷位粘合样板；其RR是算术曲线的一次公式，不能代替平方交数二次项或把取整误差删除。广义实参数源需另证兼容 |
| Connes–Consani–Moscovici, *Zeta zeros and prolate wave operators: Semilocal adelic operators*, [2310.18423v2](https://arxiv.org/html/2310.18423v2)，v1 2023-10-27、v2 2024-05-04；§4.6–4.8 Thm4.6/Prop4.8 | 任意先固定finite-S的Sonin空间稳定性、dual Hardy–Titchmarsh变换与de Branges整函数实现；明确有界可逆映射 | Hilbertian isomorphism不是原L²酉性；整函数载体上的norm仍随S改变。正压缩迹与完整Weil源比较要另证；不能把整函数实现当作目标Ξ行列式身份 |
| Connes–Consani–Moscovici, *Zeta Spectral Triples*, [2511.22755v1](https://arxiv.org/html/2511.22755v1)，2025-11-27；Thm3.6、Thm5.10、Lemma7.3、§8 | 规定最低态假设下，移去最低值的商内积给自伴导数与精确正规化行列式；prolate候选的极限已有具体表达 | §8明确仍缺实际最低态simple/even及候选对最低态足够强的逼近。平移后的正商不证明原Weil型正；固定λ极限不支付λ增长。可作为独立谱识别路线，不应当作RR设施已完成 |
| Connes–Consani, *On the Jacobian of overline Spec Z*, [2602.15941v1](https://arxiv.org/html/2602.15941v1)，2026-02-17；Thm3.4、Prop5.1、Thms8.5/8.6/8.15、§9 | adelic Riemann sector与带半范数秩一群Picard幺半群同构；真正O(D)模层；framed/rooted除子及tensor乘法、Abel–Jacobi纤维 | 为“除子—层—乘法—局部项”提供具体对象。Jacobian不是已正极化的阿贝尔簇；§9的局部trace解释仍不提供全平方RR/Hodge。按一般Beurling数据重造秩一群、局部整性、frame和metric均需新比较 |
| Connes–Consani, *On the Absolute Geometry of Spec Z and the Fargues–Fontaine curve*, [2606.06604v1](https://arxiv.org/html/2606.06604v1)，2026-06-04；Prop2.2、Thms3.9/3.16、§5 | pullback结构层的p茎为F1[T^{Z[1/p]+}]；局部perfectoid点与tilt主单位盘；代数闭假设下的untilt商；复周期轨道得Tate椭圆曲线 | 有真实局部曲线和部分Frobenius，不是只有比喻。一般perfectoid点与代数闭untilt商须区分；局部曲线的正性不能直接控制全球ζ。§5所需的局部到全局下降仍单列 |
| Connes–Consani, *The Absolute Twistor Line and the Geometry of overline Spec Z*, [2609.00299v1](https://arxiv.org/html/2609.00299v1)，首次提交2026-08-31；Thm5.1、Def7.2、Props7.3/7.5 | 绝对twistor对象的复点为P1(C)，实结构$z\mapsto-1/\bar z$；奇整数Frobenius作用与其兼容；全局绝对曲线有真实结构层 | 改善拱位与实结构组织；兼容实结构不等于正Hermitian极化。普通P1图的交数必须和算术平方原源另比较；奇整数动力学不涵盖所有g-prime标签或全ζ的prime-power/Γ项 |

本轮另核题录／现版本、未重新消费全文：[Connes 2602.04022v1](https://arxiv.org/abs/2602.04022)，
2026-02-03，*The Riemann Hypothesis: Past, Present and a Letter Through Time*。
其§6–7的此前已核范围见[2026-10-12来源审查](../../../literature/supplements/2026-10-12-connes-recent-paper-audit.md)。
Borger Λ-descent、Lorscheid blueprints、2024 *Knots and primes*及Meyer的核空间谱实现，
本次只沿旧题录作为结构／历史背景，不冒充本轮逐定理新核读；不能用它们填正性空白。

## 3. 两条几何来源链与一条具体分析链

### 3.1 2007的有效对应—评价行列式链

这段是原文机制恢复，不是新定理。对真实曲线的对应Z，曲线RR与generic-point论证使其在适当
主关系／trivial关系调整后有效且degree g。令$Z(P)=Q_1(P)+\cdots+Q_g(P)$。
复合有真实cycle身份

\[
 Z\star Z'=d'(Z)\Delta+Y.
\]

canonical截面的评价行列式平方为对像点对称的有理函数。
其极点预算和主除子零／极degree守恒限制collision cycle与对角的交数。
原文(2.37)–(2.46)据此得到正迹。新推广不能只复制这个cycle等式；还须给：

- 真正可评价／相乘的截面空间；评价行列式的非退化性以及零／极计数；
- 兼容主关系、双次数及transpose/composition的effectivity；
- collision、ramification及对角自交的同源正规化，且误差保全部源。

若将“存在这些设施”直接作未知假设，仍没有独立新输入。
对经典无限容量情形，还必须使用合法relative determinant或增长截面预算；
有限g、有限维行列式或有限若干点数拟合不能代替它。

### 3.2 2018／567的平方RR—容量链

2018给复提升和下降工具，567把曲面RR推Hodge负性的容量论证写成带cutoff预算。
这条链要求实际Euler二次项而不只是线性RR或局部index。
目标量是每个固定compact测试的

\[
 |d_j+Q_W(g)|\le\eta_j,\qquad
 R_j=\frac{2(C_j+a_j+\epsilon_j-\chi_j)+n_j|b_j|}{n_j^2},
 \quad\eta_j\to0,\quad\limsup R_j\le0.
\]

本轮§3.4来源核查没有生成任一新的经典$C_j,\epsilon_j,\eta_j$。
2023曲线RR和2026真实模层让候选载体更具体，但不自动支付这些数值／源身份。
允许$C_j\to\infty$的567接口保留，不能回退为“没有有限genus所以此路不可能”。

连续维数不能仅凭普通截面乘法单射自动满足567的容量论证。
[393§§3–4](../../../notes/393-f1-profile-surjectivity-and-filtered-dimension.md)已证的是单p的轮廓满射，
并在CC目标一致收敛拓扑上计算过滤轮廓像的覆盖维数；解析H0在正权时的普通K维数无穷，
轮廓的Banach商拓扑却离散，且轮廓映射并非通常线性映射。
若采用这种连续维数，必须另外证明所需乘法／单射的过滤与拓扑相容性及维数单调性，
不能将已证的轮廓维数公式直接代入普通有限维容量预算。

### 3.3 2020–2024／560的正迹—同源余项链

对unitary scaling表示和Sonin正交投影P，$\operatorname{Tr}(A_g P A_g^*)\ge0$有独立Hilbert来源。
关键费用是把它与实际完整$Q_W$比较。
2020在实位给具体核；560进一步付出每个先固定finite-F与fixed支撑上的完整prime-power身份，
在原物理L² norm上写成

\[
 Q_L(r)=T_{F_L}(r)-\langle r,K_{F_L,I}r\rangle
       +2|\langle r,\cosh(u/2)\rangle|^2
       -2|\langle r,\sinh(u/2)\rangle|^2.
\]

这是可运算的正源与误差，不是把零点谱装进正空间。
fixed参数compactness不决定误差符号，也不支付成长uniform费用。
在新的几何载体还没有实际RR／非退化比较时，保留这条有实际输入的备选最合理。

## 4. 对最一般g-integer的可迁移责任

“最一般”应指允许atomic/continuous、lattice/nonlattice、双对象对偶、分次多权、无限容量，
而非断言每个正Euler系统都有RH。562–567的正／负族和290已排除后一断言。

| 设施 | 一般正g-integer裸数据给到哪里 | 独立需要什么 | 最便宜拒绝测试 |
|---|---|---|---|
| 源与完成化 | $P\mapsto\Pi\mapsto M$及右半平面Mellin对象 | 标准完成化类membership、权、Γ/极点项及核校准 | 564同整数positive Mellin gauge $B(s)$ |
| 对偶／对应 | log平移、反演、形式graph／transpose可定义 | 加法局部模型或独立函子、复合异常、实际cycle及双degree | 567 continuous负段仍有全部形式身份 |
| 主关系／层 | 可构造analytic source理想或余核 | 真正局部单位、带度量变换律、restriction/gluing、nonzero quotient可见性 | 405双矩、406单位读出、552零主类／高频norm障碍 |
| 正源 | 额外给Hilbert carrier可得positive trace | 与同一完整W的identity/controlled defect，保原norm及growth | 566非unitary twist正form却heat identity失败 |
| 有效性／RR | 正计数、正的不同graph交点 | 任意signed组合的截面、乘法、独立存在性／collision预算 | 290完整正整数Euler负例、567负continuous Gram |
| 全球谱／trace | Mellin零除子／分次supertrace | 全零点可见性、重数、普通trace或合法relative trace、极限 | 562 atom重数、565隐藏取消/Jordan、566 trace∞／非可闭 |

上表只是可移植设施的责任图，不是“最小公理已独立证明”的宣称。
对于continuous模型，almost-periodic／convex下降给载体灵感，不能先把其PSD或边界增长放回假设。
对于数域，必须保ideal标签、每个实／复无穷位、判别式和全部局部characters；
对于函数域，必须保q周期、proper powers和graded权。

## 5. 已有笔记怎样改变路线排序

| 旧资产 | 此次保留的强后果 | 禁止重复支付／合法逃逸 |
|---|---|---|
| 363 §5及本轮2018原件核查 | 精确列出复提升→relative交数→平方RR→有效化→下降的责任 | 原文不是全平方RR定理；不再以研究计划本身开数学合同 |
| 405 | 真实源映射、两个次数矩、analytic radical及非退化商方向已区分 | 余核向量不是几何section；全部源理想不可直接商掉而保双degree |
| 406 | 普通Cartier下单位的log determinant读出需消去；带度量pair允许补偿 | 没有排全部Arakelov／relative方案；新对象须付完整变换律 |
| 552 | 指定radial Green energy不下降；其二阶高频不能免费比较actual Γ的log阶 | 仍允许非局部、全place、source-adapted修复；不得再调同一scalar |
| 560 | 每fixed有限S和支撑有原norm的完整正trace−compact＋双pole | 可直接研究actual joint signed误差；compact≠小／负，保成长量词 |
| 566 | unitary周期bundle的正闭form与完整heat身份；physical-Q全线闭包路线失败 | 不排另carrier；Hilbert energy和full-source trace identity分开核 |
| 567 | 曲线RR独立正性来源及continuous全Π对应失正测试；增长容量接口 | 不能把positive counts/graphs/duality/trace再当充分正性；新几何须拒负段 |

## 6. 建议并入root路线图的门与停止规则

优先把路线画成依赖图，而非一串待造的名词：

\[
 \text{canonical full source}\longrightarrow
 \text{source-faithful carrier/principal quotient}\longrightarrow
 \begin{cases}
 \text{effective correspondence+evaluation/collision budget},\\
 \text{square RR+controlled capacity},\\
 \text{independent positive trace+signed defect control}
 \end{cases}
 \longrightarrow Q_W\ge0.
\]

前两支是独立几何设施的两种证据组织；第三支已有较强actual analytic输入。
无需先证明它们等价，更不能把最后一个箭头作为第一支的定义。

1. **本轮已完成的来源门：** CC2018 §3.4不给classic实际二次RR／Γ预算；结论为来源止，0轮。
2. **几何重新准入门：** 先交出一个在405非根商方向有值、兼容406完整单位／metric变换的实际载体和明确比较，
   或原件里此前未消费的同源指数／collision界。只有框架、周期点、unknown H1或标题不能开合同。
3. **分析备选的具体门：** 使用560真实receiver、全压缩逆和双边界，比较联合finite-place误差的signed交叉；
   若没有实际输入／新测试，不重跑ratio或只换Hilbert表示。
4. **共同验证顺序：** 连续pure段必须成功，continuous非pure段和290必须在独立设施处失败；
   真F5曲线支付全部n的递推；经典ζ必须保Γ finite-part/contact、全部prime powers与双pole。
   再讨论cofinal cutoff／权／数域／continuous极限，不以低谱或有限点数据外推。

本稿没有改变实际ζ的whole leading4/5、成长core、coupling或Ξ识别瓶颈。
新增的是来源定位、不同Weil证明组织的设施拆分，以及在新论文对象和旧障碍之间的具体责任对应。
不能把此路线图的整理或其条件箭头计为新的独立正性。
