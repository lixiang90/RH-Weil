# Landau–Siegel简化证明：评价行列式、全位预算与Weil正性的距离

2026-10-20，按用户提供的Kevin Barreto三页截图及继续核查指令。
本稿是外部证明核查和设施比较，0新增数学轮；不是568，不建C031，不恢复暂停的零区优化。
保G20261014、0c4f/≤538冻结输入、原cadence2。独立原稿与root消费范围见文末。

## 1. 可以确认什么，不能由宣传或署名确认什么

本轮直接核对截图的数学链，并定位以下一手记录：

- [OpenAI 2026-10-01原稿](https://github.com/openai/math/blob/main/preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/paper.pdf)。
- [Banks，arXiv:2610.15483v1](https://arxiv.org/html/2610.15483v1)，2026-10-11；其Theorem1.1给有明确常数的版本。
- [Kerr，arXiv:2610.21099v1](https://arxiv.org/html/2610.21099v1)，2026-10-15；其实现走小高度多项式与Masser非消失路线。
- [Green，hexagon:2610.00311v2](https://hexagonmath.org/2610.00311v2)，记录页区分10月17日初稿与10月18日v2；注意不是同号arXiv论文。
- [Tao，2026-10-19解释](https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/)，解释全位多项式机制，并提及Pescador及Barretto的进一步改进。

Barreto版本的直接审核对象是用户所附完整三页；不因尚未取得稳定原稿地址而否认截图，
也不据Tao提及就代替逐行检查。本文不用“世界最简”作数学结论。
OpenAI另有quasi-RH原稿及形式化项目；它们与这三页的具体证明是不同对象，
不能把另一个定理的形式化声称当作本截图已通过Lean。来源稿另列实际核查范围。

截图的结论是：对所有primitive nonprincipal real Dirichlet χ及其real zeros β∈(0,1)，

\[
 (1-\beta)\log q\ge 1-O\!\left(\frac{\log\log(3q)}{\log q}\right),
 \qquad (1-\beta)\log q\ge c>0.                         \tag{1}
\]

第一式是q→∞的一致渐近下界，第二式由大q及有限小q合并；它不是所有零点实部等于1/2。
小q合并还用L(1,χ)≠0及解析零点孤立性，不能只写“有限个character”便省略端点。
本次对截图链的局部审核未发现实质缺口；这句话不代表已重跑其他形式化或重证所有引用基础。

## 2. 真正的新输入在整数评价格，而不在零点一侧

令d≠1 squarefree、|d|≤q，χ(p)=(d/p)对odd p∤q；工作在O=Z[√d]，无需它等于最大整数环。
此处α'=u−v√d是代数共轭；d>0时不要误读成复共轭。
对x≥max(e³,√q)取

\[
 B=2\sqrt{2x}\,q^{1/4},\quad
 0\le u<B/2,\quad 0\le v<B/(2\sqrt q),\qquad
 T=\{(r,s)\in\mathbb Z_{\ge0}^2:r+ks<x\}.               \tag{2}
\]

矩形面积为2x，取整数点得到至少2x个不同α=u+v√d和不同α'；所有共轭模均小于B。
在T的单项式上作评价

\[
 z^rw^s\longmapsto
 \left(\partial_z^j(z^rw^s)(\alpha_i,\alpha'_i)\right)_{i,\ 0\le j<2x/k}.
                                                               \tag{3}
\]

把O值的每个坐标展开为基{1,√d}下的两个整数，即得一个真正整数矩阵。
不是先用ζ零点定义矩阵，也没有选择未知正内积。

### 2.1 非零性：带重数评价不能吞掉所有行

若行相关，得到非零F(z,w)，deg_zF<x、deg_wF<x/k，所有F(z,α'_i)在α_i有至少
J=ceil(2x/k)阶零。至多deg_wF个specialisations恒为零，其余有超过x个。
这些一元多项式张成的空间维数ℓ≤ceil(x/k)。选不同次数的基g₁,…,gℓ，普通Wronskian满足

\[
 W=\det(g_b^{(a)})_{0\le a<\ell,1\le b\le\ell}\ne0,
 \qquad \deg W<\ell x.                                  \tag{4}
\]

最高项系数是不同degree上falling-factorial多项式的Vandermonde型行列式，特征0下非零。
将任一非零specialisation放入一列，常数换基不改变零重数；该列各导数仍有至少
J−ℓ+1≥ℓ阶零。超过x个不同α_i便迫使deg W>ℓx，矛盾。
因此评价行满秩，存在使用全部行、固定一组列的非零integer minor D。
这支付的是实际评价空间的非退化性，不能拿来宣称完整Weil Gram正定。

### 2.2 有限位：Frobenius的厚邻域给高阶整除

对k≤p≤x、χ(p)=−1，p为odd且不除d，有

\[
 \alpha_i^p\equiv\alpha'_i\pmod{pO}.                    \tag{5}
\]

记h=floor(r/p)，作整系数行变换

\[
 z^rw^s\rightsquigarrow z^{r-ph}(z^p-w)^hw^s
 =z^rw^s+\sum_{j=1}^{h}(-1)^j{h\choose j}z^{r-pj}w^{s+j}.
                                                               \tag{6}
\]

p≥k保证新单项式仍在同一T中，且z次数下降；按r排序这是unitriangular变换，
保持同一个D。更重要的是，z^p−w的每个正阶普通z导数都有p因子（高于p时为0）。
乘积法则因此使(6)的每一个jet坐标都被p^h整除，故

\[
 v_p(D)\ge\sum_{(r,s)\in T}\lfloor r/p\rfloor.
                                                               \tag{7}
\]

这里必须使用普通导数；擅自改为∂^j/j!会改变整除账本。
每个p可使用不同unitriangular变换，但minor的列及原D固定，故各p预算可以相加。

### 2.3 无穷位：同时控制两共轭，支付高度、导数及阶乘费用

两种共轭的entry界同时给整数坐标界，不漏基{1,√d}的运输。
令m=|T|、U=Σ_T r，取k=ceil(log(x²B))，则

\[
 m\ll x^2/k,\quad U\gg x^3/k\gg xm,\quad
 3\le k\le x,\quad \log k=\log\log x+O(1).               \tag{8}
\]

非零entry模至多x^{2x/k}B^{r+s}≤B^r(x²B)^{x/k}≤B^re^x。
行列式展开的m!、导数及s次数费用合计O(xm)=O(U)，因此

\[
 \log|D|\le U\log B+O(U).                              \tag{9}
\]

有限位用floor(r/p)≥r/p−1及Chebyshev，合计损失同为O(U)。
小于k的素数用Mertens付log k+O(1)。同一个非零整数的全位比较最终给

\[
 A_\chi(x):=\sum_{p\le x,\ \chi(p)=-1}\frac{\log p}{p}
 \le\tfrac12\log x+\tfrac14\log q+\log\log(3x)+O(1).
                                                               \tag{10}
\]

x<e³或x<√q的范围由全素数Mertens直接支付。全体O常数不依χ、q、x；
只付fixed q渐近不足以推出(1)。实数x的严格不等号和导数整数端点由ceil处理。

## 3. 分析侧只把一个坏零点转成一种不可持续的局部偏置

对0<η≤1，partial summation将(10)送到

\[
 \sum_{\chi(p)=-1}\frac{\log p}{p^{1+\eta}}
 \le\frac1{2\eta}+\frac14\log q+O(\log(2/\eta)).         \tag{11}
\]

Euler product、全部higher powers的uniform O(1)、以及p|q项的O(log log(3q))给

\[
 \frac{L'}L(1+\eta,\chi)
 \le\tfrac12\log q+O(\log(2/\eta)+\log\log(3q)).        \tag{12}
\]

完成L的Hadamard展开在σ>1有Re(σ−ρ)⁻¹>0，因为已知Reρ≤1；无需假设RH。
保留real β，连同完整conductor/Γ常数得到

\[
 \frac1{1-\beta+\eta}\le\log q+
 O(\log(2/\eta)+\log\log(3q)).                         \tag{13}
\]

取η=(log q)⁻²并正确反演，η log q也趋0，得到(1)。
Γ在此实参数区间有界，prime powers在此高阶尾可绝对付费；
这不等于经典全Weil型中可以舍弃Γ、prime powers或pole。

因果顺序是：独立算术评价预算先给(10)，再由已有解析字典排除特殊坏零点。
不需要先找所有零点的自伴算子。对χ=1没有χ(p)=−1这组局部输入；
也不能把nonsquare quadratic格偷偷退化为平方d来对ζ照搬。

这份简化还有三项具体设计值得学习：平衡u与v√q的矩形使高度只有B≈√x q^(1/4)；
三角形加权T对z^p→w封闭，避免另付w方向越界的截断费用；
按specialisations组成Wronskian，用一元次数预算替代更长的resultant/因子分解组织。
真正收益来自选对保操作的空间和量纲，而非事后省略边界或误差。

## 4. 与Weil有效性、RR容量相同的责任和不同的实现

| 责任 | 本证明真正支付的设施 | 函数域Weil／567的对应角色 | 不能混同 |
|---|---|---|---|
| 有对象可评价 | O中实际加法格、带权多项式、ordinary jets | 真实截面、评价及对应 | 单纯乘法半群或正Euler数据没有这些map |
| 不被关系全部消灭 | Wronskian次数/重数预算给满秩 | 非退化评价det、合法principal商；非零截面仍可见 | D≠0非目标Q的符号定理 |
| 局部约束有效 | α^p≡α'及其厚邻域，给非负v_p(D)下界 | 有效零除子、碰撞/局部交重数、截面乘法 | Frobenius符号来自实际reduction，不由正计数自动恢复 |
| 全局容量有限 | 无穷位高度＋导数＋m!的定量上界 | degree守恒、评价det的零极预算，或RR截面容量 | (9)是特定格的高度界，不是平方RR公式 |
| 同一对象全位结算 | Σ_pv_p(D)log p=log|D| | 主除子degree0、全局product formula | 任意分别选定的正矩阵/测度不能组成它 |

二者共同之处是：实际对象不能同时承受过多独立局部条件和过小的全局容量。
Weil原始评价det路线与此非常接近；RR路线则以二次增长的截面被送入固定有限容量空间取得矛盾。
Wronskian、有效性、RR是不同的可替换证明部件，并非彼此逻辑等价；
本例也没有给arithmetic site平方上的HRR或经典Weil交叉型。

因此上一[路线图](2026-10-20-generalized-weil-facilities-literature-roadmap.md)的评价det路线获得一个
已经成功作用于真实L函数问题的具体原型。新增的是这项外部独立算术输入和准确比较，
不是本仓构造了新的经典正极化。它提醒我们先找小而真实的评价/整除设施，
不必把“完整上同调先建成”当唯一入口。

## 5. 最大g-integer环境必须允许不同的容量机制

### 数域

对非零algebraic integer Δ，有限位ord与全体嵌入的log|σΔ|由norm/product formula相接；
须保prime ideals、residue degrees、ramification、discriminant和所有arch权。
这提供自然推广环境，但本证明只核特定quadratic Frobenius偏置；
它不自动给任意Dedekind ζ的全Weil正性。

分布不能被无条件视作唯一恢复了全局代数对象：
[de Smit–Perlis 1994](https://arxiv.org/pdf/math/9410216)明确构造相同Dedekind ζ而非同构的数域，
甚至class number也可不同。本轮核读该三页原文的定理、例子及证明组织，未重算regulator证书。
因此“由同一ζ/范数计数推出唯一ring/sections”需要额外刚性；
这不排除多个来源共同实现同一Weil型，也不排除一种不追求唯一重建的纯分析证明。

### 函数域

全局函数域主除子的Σ_v ord_v(Δ)deg v=0，允许用所选无穷位的pole预算代替arch高度。
真实曲线上的sections、RR及Frobenius graph另有独立来源，可检验所提局部/全局设施。
但不能直接拷贝(4)：正特征下1和z^p线性独立，ordinary Wronskian却为0。
须用合适separable或Hasse jet理论重新支付非退化性和局部阶数；
数域证明中不能除j!与函数域中需要divided-power工具是两个不同语境。

### 连续g分布及负对照

562的同一positive primitive连续族Z_c(s)=1+c/[s(s−1)]，在c≥1/4有完整Weil平方和，
在0<c<1/4失正。两段都具有正P/Π/M及精确反射，故这些弱数据不能推出本证明所需评价设施。
290又提供正整数Euler/形式对偶非pure对照，说明离散整数重数本身也不够。
另一方面，continuous正段表明literal有限位integer lattice不是所有类RH性质的必要条件。

一般框架可以把“局部vanishing/constraint filtration＋全局capacity”作为候选接口，
让数域以valuation实现、函数域以divisor degree实现、纯分析正例以独立ODE/energy实现。
这只是容纳不同证书的设计，不是从一般分布自动恢复局部域或product formula的定理。

## 6. 从全位预算到完整Weil正性，还欠哪些独立输入

当前D约束特定χ的一个非负实标量prime profile。非零det或正volume本身不控制Hermitian惯性；
即使另造一个处处正的Gram，也必须证明它对应目标Weil型，而不是另一个对象。
完整目标是对每个r∈Cc∞(R;C)证明Q_full(r)=W_full(r*r*)≥0，保Γ、全部powers、双pole及contact。
靠近1的实零点会强迫χ(p)=−1的正质量偏置，正好对应(5)的实际Frobenius类。
一般离线复零点产生的检测带有频率振荡；目前没有把这些任意signed/complex方向
变成同一几何中非负局部阶数的构造。直接乘n^(−it)也不会自动保留原来的整数同余。
这解释了为何“一个极端偏置不能存在”和“全部Weil测试均为正”承担不同强度的责任。

若要借用det机制，至少还欠以下实质比较，而不是给未知条件换名字：

1. **源定义的评价载体。** 从P/Π及固定dual构造可乘的filtered sections/jet格、实际maps和局部作用；
   不用目标零点填矩阵。若采用principal商，须同时消去405的合法关系、保留552/537的非根方向。
   原f与物理r=e^(u/2)f的运输不能丢。
2. **完整源的同一规范。** 有限位filtration准确支付proper powers及labels；arch/capacity项给规范Γ、
   discriminant和pole/contact。任意可调cδ0或B(s)不能用来“校准”最终符号。
3. **所有方向的非退化和比较。** 不是每个basis diagonal或某种正character profile，
   而是任意有限复线性组合的mixed项。integer格若只在有理测试子代数定义，
   必须付清分母/高度并证明其在完整W拓扑中稠密及连续延拓。
4. **有符号的预算身份。** 对每个fixed r，若独立取得非零D_n(r)、有限位下界L_n(r)及arch上界A_n(r)，
   则A_n−L_n≥0；要推出目标，还须证明某个c_n>0下

   \[
    \frac{A_n(r)-L_n(r)}{c_n}=Q_{\rm full}(r)+o(1).       \tag{14}
   \]

   这是尚未构造的same-source比较责任，不是本轮新定理。若反过来按右边定义A_n，
   再假定它是合法上界，正性已经被放入前提。上界过粗而增加任意正费也只给另一泛函。
5. **误差与全域。** 每个fixed complex compact源的误差必须趋0；若还要成长窗定量结论，
   另付该成长量词及core/coupling。有限S、有限频率或少数r不覆盖完整Weil判据。

(14)若真正由独立jet/collision/capacity定理支付，会是有价值的新输入；
仅把它作为存在性条件写下，与旧unknown H/CM/完整正型条件没有兑现上的区别。
走Weil判据本身不必先取得faithful determinant；只有另声称谱实现时再付零点/重数身份。

## 7. 决策、停止范围与下一动作

本轮使评价det路线更具体，尚未构造经典source→jet map，也没有把(10)提升到(14)。
因此不以这一外部结果重开零区优化、不增加一轮玩具det数值、不建立“未知det存在”合同。
actual强旧542＋555→557 leading4/5、560成长K/sign/core/coupling及Ξ识别均保持。

唯一下一动作仍为既定的2402.06671v2双conormal固定权/finite-part对完整Γ来源比较。
理由是：它有可直接判定的实际公式，处理上述第2项；本轮尚无可同等准入的经典评价map。
若原定义只允许手调两半轴权或cδ0，停该翻译并返回560 actualreceiver joint signed准入。
评价det路线保留为几何主干；改变优先级需要一个真实map通过关系/非根测试，
或一个独立same-source局部阶数/容量估计，不能只出现新的“adelic positivity”名称。

本轮瓶颈没有改变；变化的是外部成功原型和设施缺口的精确度。

独立原件：
[截图数学核查](../../reviews/2026-10-20/landau-siegel-inspiration/elementary-proof-audit.md)、
[来源/版本核查](../../reviews/2026-10-20/landau-siegel-inspiration/primary-source-verification.md)、
[设施运输核查](../../reviews/2026-10-20/landau-siegel-inspiration/facility-transfer-audit.md)。
