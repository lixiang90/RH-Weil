# 真实算术截面到局部评价：路线B的单一候选准入核查

2026-10-22，承接用户“按新路线图继续研究”。同G20261014及冻结0c4f基线，
没有新建runtime Goal；C035/572保持完成。本次不是573或C036，单cadence仍为1、正式cycle14不变。

**结论：本候选确能独立提供有限位评价、消失核、乘法过滤和有限格上的原高度预算；
它尚未提供解析源到截面的映射，更没有给出平方／对应上的二次容量及完整Weil预算身份。
因此保存这些前端及反测试后停止本入口，不把另一个未知RR条件开成新合同。**

## 1. 为什么选这个具体测试

[新路线图B](2026-10-20-generalized-weil-facilities-roadmap-after-572.md)要求同一个global对象的
section→local restriction、kernel／乘法和独立容量。上轮actual变分门已执行，
旧560足以付安全高层actual误差及原du的高频部件，不能继续优化16/γ作为新容量。
568已给signed非退化评价载体，569已给Γ规范及matched cocycle；重复这些不会推进缺口。

本次只核同一已定位原件 Connes–Consani,
[*On the Jacobian of* \(\overline{\operatorname{Spec}\mathbf Z}\), v1](https://arxiv.org/html/2602.15941v1)，
具体测试是：有限frame能否给实际消失核，arch小截面是否有有限容量，
两者的预算能否接到原源。这个测试可由该原件内部的奇异边界反例否定过强推断，
比再读一篇线性RR或增加jet阶更有决策价值。未预先声称它已具备新的核心数学输入。

所需对象保持原范畴：\(L\subset\mathbf Q\)是秩一无挠阿贝尔群，
\(\xi:L\to\widehat{\mathbf Z}\)、\(\tau:L\to\mathbf R\)是frame；
small sections施加\(\sum|\tau(x_i)|\le1\)，不是复向量空间。
原文“finite type”指\(\tau\ne0\)，不指有限生成或有限容量。
Thms8.5/8.6/8.15的模对象／tensor／frame-root对偶不自动是Mellin反射、正极化或平方RR。

## 2. 原件歧义与不依赖歧义的真实局部前端

原文§5.2把\(\mathcal L(V)\)描述为“属于\(L\)且分母只在\(V^c\)”的元素。
若字面执行，\(L=\mathbf Z\)、\(V=\operatorname{Spec}\mathbf Z\setminus\{p\}\)时得到\(\mathbf Z\)，
却不能承受结构环\(\mathbf Z[1/p]\)的乘法。Prop5.1的norm计算没有解决这个有限处问题。
本次只将以下标准局部化作为**显式补充定义**消费（\(V\)为非空Zariski开集，另置\(\widetilde L_D(\varnothing)=0\)）：

\[
 \widetilde L_D(V)=L_D\otimes\mathbf Z[S^{-1}]
 =\{x\in\mathbf Q:v_p(x)\ge-n_p\ (p\in V)\},\quad S=V^c.
\]

其开集restriction为包含，kernel为零；它与有限闭子概形上的评价kernel是两回事。
旧来源审计有关Prop5.1的直接消费现以本澄清限定；未付容量、路线图停止结论及568/569不受影响。
没有据这一局部表述问题否定其余模分类，也没有默改论文原文。

无需采用上述修补，从§8的生成frame本身已可严格给出有限商。
写\(L=L_D=\{x:v_p(x)\ge-n_p\}\)。若\(n_p<\infty\)，\(v_p(a_p)=n_p\)，则

\[
 e_{p,k}:L\to\mathbf Z/p^k\mathbf Z,\quad x\mapsto a_px\bmod p^k,
 \qquad\ker e_{p,k}=p^kL=L(D-k[p]). \tag{1}
\]

存在达到最小valuation的元素，其frame像是单位；整数倍使(1)满射。
有限多regular位用CRT合并，kernel为\(NL\)，\(N=\prod p^{k_p}\)。
valuation可加又给
\(L(D-k[p])L(D'-\ell[p])\subset L(D+D'-(k+\ell)[p])\)。
这是同一global有理元素的局部消失过滤，不是从零点反定义的正性。

若\(n_p=\infty\)，则\(pL=L\)、\(a_p=0\)、\(L/p^kL=0\)。
尤其原件的Abel–Jacobi边界点\(L=\mathbf Z[1/p]\)在**本素位**恰没有这种非平凡评价。
这不否定该轨道的其他谱实现；它只否定“该frame quotient已给该轨道全部prime-power预算”。

## 3. 同一非零对象的局部消失—原高度预算

在有限支撑、非退化metric层，令

\[
 L=h\mathbf Z,\quad h=\prod p^{-n_p}>0,\quad
 \tau(x)=tx,\ t\ne0,\quad \lambda=|t|h,\quad d=-\log\lambda.
\]

原高度球\(B_R=\{x\in L:|\tau(x)|\le R\}\)满足精确公式

\[
 \#B_R=2\lfloor R/\lambda\rfloor+1,\qquad
 \#(B_R\cap NL)=2\lfloor R/(N\lambda)\rfloor+1. \tag{2}
\]

全群到\(L/NL\)满射不代表球到该商满射。
对原单位球，存在非零消失截面当且仅当

\[
 N\lambda\le1\quad\Longleftrightarrow\quad
 \sum k_p\log p\le d. \tag{3}
\]

证明只需写\(x=hNm\ne0\)，故\(|\tau(x)|=N\lambda|m|\ge N\lambda\)；反向取\(m=1\)。
局部与无穷位确在同一非零对象上计费。主变换同时输运frame和metric，保持\(\lambda\)与(2)–(3)。
这是真实、非循环的高度前端，归valuation／格的直接机制；它不是完整Weil容量。

若**另行**给出秩r整数评价矩阵\(A=(n_{ij})\)、非零\(\Delta=\det A\)，
原列高度\(\sum_i\lambda_i|n_{ij}|\le R_j\)，以及同一\(\Delta\)的整除下界\(v_p(\Delta)\ge\ell_p\)，
则Hadamard和整数非零性给

\[
 \sum_p\ell_p\log p\le\log|\Delta|
 \le\sum_j\log R_j-\sum_i\log\lambda_i. \tag{4}
\]

这是LS“非零行列式＋有限位整除＋无穷位上界”的正确预算方向。
秩r direct sum、真实评价矩阵、高阶整除以及解析源对列高度的费用仍须另给；
单个rank-one群上多列标量并不自动产生rank-r非零minor。
本次不把这一初等扩展冒称原论文给出的平方截面理论。

独立负对照使容量的范围很明确：

| 同一候选内部的对象 | 有限位评价 | 原arch容量 |
|---|---|---|
| \(h\mathbf Z,\ t\ne0\) | regular位商满、kernel如(1) | (2)有限，(3)准确 |
| \(\mathbf Z[1/p],\ t\ne0\) | 本p商为零，异\(\ell\)商仍满 | 每个正半径球含无穷多个\(p^{-j}\) |
| 所有\(n_p=1\)的rank-one群 | 每处有限商都非零且满 | 球含所有\(1/p\)，仍无限 |
| \(h\mathbf Z,\ t=0\) | 有限商不变 | 全群进单位球，无高度上界 |

一般非循环秩一子群有趋零非零元素：先缩放使其含\(\mathbf Z\)，
约分分母无界；Bezout从\(a/b\)产生\(1/b\)。故正半径球有限恰需群循环且metric非零。
这只针对普通有界点数容量，保留连续／相对／正规化容量，不能推广成一般类RH必须离散。

## 4. 为什么线性容量没有闭合Weil正性

tensor powers的原metric为\(\lambda^n\)，所以

\[
 0\le\log\#B_1(L^{\otimes n})-\max\{nd,0\}\le\log3. \tag{5}
\]

这是曲线层的一次增长；零degree方向保持有界。
567的机制需要平方上signed对应\(D\)的\(n^2D^2/2\)下界、真实乘法和独立的\(H^0(2K)\)容量。
其有误差接口对每个固定实compact源给出（保持567的量词，复源覆盖／极化另付）

\[
 d_j\le R_j=
 \frac{2(C_j+a_j+\epsilon_j-\chi_j)+n_j|b_j|}{n_j^2},\qquad
 |d_j+Q_W(r)|\le\eta_j. \tag{6}
\]

该结论以前件中的两条RR不等式、同一乘法、所有误差及源量词为条件；
本候选只给(5)，没有给(6)的数据。允许\(C_j\)增长仍需独立证明\(\limsup R_j\le0\)、\(\eta_j\to0\)。
把未知数据命名为RR，或直接要求全源预算差非负，均未减少Weil等价责任。

另一缺口更靠前：原文没有给
\(r=e^{u/2}f\longmapsto\)实际global sections／correspondence。
因此405的主关系\(e^{u/2}p\)与537的非根\(r_0=(\partial_u^2-1/4)\psi\)双测试目前**缺输入**，
不是通过，也不是已经构成一般几何反例。
完整Q根商、405的B根商和物理原源必须保不同角色。

固定目标的默认裸加性map不能补这条箭头：全复源可除，向固定有限群的加性map为零；
全源加性map若全落固定正metric球也为零；赋秩一群以自然实metric时，连续加性像因连通而为零。
这些只是精确的窄类检查；允许源依赖的除子／metric、非线性、族、tensor、对应、相对载体或复提升。
用568 signed \(J_W\)复合smooth probes可恢复旧关系测试，仍不生成独立算术容量。

## 5. 连续、函数域、数域与完整经典源的检验

| 系统 | 本次实际检验的信息 | 尚未付的责任 |
|---|---|---|
| 连续正反段\(d=\pm1/16\) | 568同一非退化评价／高度设施两段皆有，Gram为\(2|A|^2+2d|B|^2\)；外加同一格不区分两段 | 从连续分布独立产生实际global容量并与物理real-*配对比较；不能强制它先有literal整数格 |
| 连续阈值\(d=0\) | 二维jet可退为一维最小Weil商，trace权仍2 | 不能以商维数替代谱重数，也不能将本格条件作为所有正例的必要条件 |
| 真有限域曲线 | \(H^0(D)\to H^0(\mathcal O(D)|_E)\)有kernel\(H^0(D-E)\)，local jets与乘法来自同一曲线；全局满射还受\(H^1(D-E)\)控制 | 完整Weil号用平方上的有效性／RR／Hodge，不能只消费曲线限制核 |
| 290/568函数域反模型 | 自由local étale、jets与raw正Frobenius并未排反模型 | 要在实际global gluing、signed有效性／容量或primitive比较处独立鉴别；“不是曲线”不是一份证明 |
| 经典ζ／一般数域 | 本次Q上的整数格前端确有意义 | ideal标签、全嵌入metric、判别式／导子、复位、原源norm及完整全位身份均另付 |

经典目标仍是568已校准的全源型：\(M_\pm(r)=\int e^{\pm u/2}r(u)du\)，
\(w(v)=2e^{-v/2}/(1-e^{-2v})\)、\(\Gamma_0=\psi(1/4)-\log\pi\)，有

\[
 \begin{aligned}
 Q_W(r)={}&2\Re(M_+\overline{M_-})+\Gamma_0\|r\|_2^2
 +\tfrac12\int_0^\infty w(v)\|\tau_vr-r\|_2^2\,dv\\
 &-2\sum_{p,k\ge1}\frac{\log p}{p^{k/2}}
       \Re(r*r^*)(k\log p).
 \end{aligned} \tag{7}
\]

本次(1)–(5)没有删减(7)，而是尚未产生到(7)的身份：
实metric的绝对值不决定Fourier/Haar规范、完整Γ finite-part/contact；
\(\log\#(L/p^kL)=k\log p\)不等于(7)中全部\(\log p\,p^{-k/2}\)加权轨道迹；
frame/root对偶不产生两个pole矩的度数配对。
若通过既有局部trace公式补这些片，仍须证明它们与**同一评价det和容量**协同，而不是两套平行实现。
569的matched cocycle允许预算片协同变换，不能代容量上界或自动排除所有完成化核因子B。

## 6. 结算、语义纠正与下一动作

三独占稿为[原件](../../reviews/2026-10-22/global-section-admission/primary-sheaf-and-restriction.md)、
[kernel／高度](../../reviews/2026-10-22/global-section-admission/finite-place-kernel-and-capacity.md)、
[源map／验证](../../reviews/2026-10-22/global-section-admission/source-map-and-validation-audit.md)。
原文定义、本文初等推导、旧568/567比较及开放的核心前件分开保存；
HTML/PDF核读范围各以对应稿为准，未声明重读全部论文或572篇笔记。

本轮真正增加的是该候选的可用局部预算范围、奇异／无限支撑反测试和来源表述纠正。
这些是已有格／valuation机制的展开及准入决策信息，不是新的经典平方容量定理。
source-only一次门收口，0数学轮；不建C036，不计573，不重置cadence。
最强旧542＋555→557 whole leading4/5（issued上预算）、成长危险core／coupling／Ξ及长期完成门均未改变。
actual安全高层直接合成保留，完整低频责任没有被本次几何审查支付。

对旧来源审计中Prop5.1的模层用法，冻结字面版本下游消费；
本次仅以标准局部化修补和独立frame商重新闭合所用restriction，未重开其他结论。
边界点\(\Theta(p)\)的同p商为零须保留在以后原域消费记录中。

唯一下一动作：先验收**一个实际写出的、区别于旧\(J_W\)复合的源→截面／对应map**，
连同至少一项独立局部消失或原高度比较；先过主关系／非根和原norm，再决定是否准入核心合同。
另一可改变排序的证据是同源算术平方的二次容量／完整预算身份，或穿过actual低频和危险core的新signed比较。
目前没有这样的新输入；不自动串下一篇论文、再读线性RR、增加jets或复跑Sonin高频。
这是停止当前候选的无输入延伸，不是排除几何／相对／连续设施，也不是暂停或完成长期Goal。
