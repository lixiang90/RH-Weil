# Landau–Siegel评价行列式向一般Weil设施的运输审计

2026-10-20，独立设施比较稿。核读对象为用户三页Barreto截图、当前路线图、567的实际交数／RR原件、562–563连续族及290正整数Euler负例；并逐段审核本轮root主稿§§4–7。外部成果的出版／版本／接受状态由另份来源审计负责，本稿不以署名或传播代替证明审核。0新数学轮，不改STATE，不开新合同。

## 1. 同一个整数minor承担三项不能拆开的责任

截图的真实载体是O=Z[√d]中的加法格及其带权多项式评价，不是g-integer乘法半群本身。每个O-valued ordinary jet在{1,√d}基中拆成两个整数坐标，才得到整数矩阵及非零minor D。

1. 特征0的次数／重数论证给评价行满秩。Wronskian将一个可能的多项式关系压成一元多项式零数与次数的矛盾，因此实际D≠0，不先使用零点位置或待证正内积。
2. 对χ(p)=−1的同一组有限位，α^p≡α′ mod pO。带权空间对z^p→w操作封闭，unitriangular行变换保持同一个D；ordinary derivatives与乘积法则保留高次p整除。各p可以换不同的行基，却不能换minor列或换目标D后相加。
3. 两个嵌入的高度、jet阶数及det展开的阶乘费用给同一个D的无穷位上界。p-adic阶数之和与log|D|通过整数分解相接。一般数域须用norm和全部嵌入，不能只取一个复绝对值。

因此起作用的是“独立非零性＋真实局部消失＋全局容量”三者的共同对象。任意正Gram、任意正测度或另选一个determinant都不能替代这项共同身份。

从证明设计看，平衡共轭高度的矩形与对Frobenius替换封闭的带权三角形同样重要：它们使局部操作不越界，也使导数及阶乘的代价留在O(U)误差内。不能将收益归结成省略误差或只更换Wronskian术语。

## 2. 与Weil评价det／RR的关系

当前路线图A已将实际截面、评价det、碰撞重数与全局零极预算列为独立正性的前端。截图给这组责任一个已成功作用于真实L函数问题的有限尺度算术原型：局部Frobenius条件产生高阶消失，全位预算限制可承受的消失总量。

Weil曲线证明的局部碰撞／零除子与主除子degree守恒，和这里的valuation／product formula有共同结构。567的另一条RR证明则将错误自交号导致的二次截面增长注入固定有限容量空间；其矛盾也是“过多独立条件或截面无法进入过小容量”。

这些是责任上的类比，不是定理之间的等价。截图的高度界不是曲面RR公式；Wronskian满秩也不推出Hodge index。这里可以不先构造自伴零点算子，确实说明完整上同调并非所有问题唯一可行入口；但它没有构造算术site平方的有效性／HRR，也没有给经典完整Weil源新的符号定理。

特别地，D≠0、logdet或volume的某个正下界不决定原Hermitian型的惯性：例如−I₂的det为正，矩阵仍为负定。即使评价矩阵自身产生一个正的Gram，也须另付其与目标Q_W的mixed项身份。普通det非零性、Gram正性和Weil源身份是三项责任。

## 3. 各类g-integer的检验边界

| 验证对象 | 可以使用的真实设施 | 运输必须另付的部分 |
|---|---|---|
| 数域 | 加法整数格、全部嵌入、prime ideals／residue fields、norm与product formula | 保留ideal标签、residue degree、ramification、导子及无穷位权；某个quadratic Frobenius类的标量界不覆盖Dedekind ζ全Weil型 |
| 真实函数域曲线 | 主除子Σ ord_v(Δ)deg v=0；截面、Frobenius交数、RR与有效性有独立来源 | pole预算代替arch高度；不可照搬特征0普通Wronskian非零性。特征p下1、z^p独立而Wronskian为0，须在具体载体重付separable／Hasse jet理论及局部阶数 |
| 连续Z_c正段 | 562–563直接由完整分布ODE／正能量矩阵给全部Weil平方和 | literal整数格与模p并非这些类RH对象的必要设施；不能用“无整数jet格”把真实正例排出一般环境 |
| 同族连续负段 | 同样有positive P、Π、M及精确对偶，却完整Weil失正 | 正分布／对偶不能恢复截图所用加法、模p作用及全位兼容性；若候选分析capacity条件两段都自动成立，则该条件不足 |
| 290正整数Euler负例 | 全部闭点正整数、Euler乘积、对偶、形式PD／HL及trace相容 | “整数重数”不等于可评价的整数环／局部Frobenius格。其primitive正自交方向正是候选有效性／RR／碰撞预算应拒绝的方向 |

函数域使用Hasse／divided-power工具不意味着截图中可随意改用∂^j/j!。截图的ordinary derivative所携带的p因子是有限位整除账本的一部分；除以j!会改变它。不同特征下的jet理论须分别证明，不能仅替换记号。

一般环境应容纳valuation、divisor degree、独立ODE／energy等不同容量证书，而不是强迫每个正例具有literal有限位整数格。目前P／Π／M与Mellin对偶本身没有给出这些证书。数域中同Dedekind ζ的非同构field也提醒：分布未必唯一识别全局ring；这只增加重建刚性责任，不否定多来源实现同一Weil型或纯分析证明。

## 4. 从标量偏置到完整Weil正性的未付箭头

截图控制的是固定实非主character的χ(p)=−1标量prime profile。有限位Frobenius替换正好对应这个实际splitting类。近1实零点通过实参数log derivative强迫该profile过大，因而产生矛盾。

χ=1不能替入：χ(p)=−1的集合不复存在，且d为nonsquare的格不可退化为平方d后假装rank／共轭不变。一般离线复零点的检测包含振荡；乘上p^(−it)不会自动保留原整数坐标、Frobenius同余及非负局部阶数。

完整目标要求每个r∈Cc∞(R;C)的Q_full(r)≥0。要将当前机制用于此目标，仍须给出源定义的sections／jets、全Γ／powers／pole／contact的规范预算、任意复线性组合的mixed项、同一norm／domain及每个固定r的极限误差。只有有理测试时还要支付分母高度及向完整W拓扑的稠密连续延拓。成长窗的统一误差、core与coupling是进一步责任。

若独立取得D_n(r)≠0、有限位下界L_n(r)及arch上界A_n(r)，只能先得A_n−L_n≥0。root主稿(14)

\[
 (A_n(r)-L_n(r))/c_n=Q_{\rm full}(r)+o(1),\qquad c_n>0
\]

若在上述同源量词下被独立证明，确是足够的比较接口；但本轮没有这样的D_n／预算身份。按Q_full反定义A_n，或假设此A_n是合法上界，会把正性偷放进前提。增加任意正费用得到的是另一泛函，也不能消费为所需完整Weil正性。

新source→jet map若走principal商，还须通过405／552的双测试：消去旧f空间合法关系p，并在物理坐标r=e^(u/2)f中消去相应e^(u/2)p；同时保留537已知Q_W(r₀)>0的非根方向r₀=(D²−1/4)ψ。通过双测试仅准许后续研究，不认证全部正性。

## 5. root主稿独立范围审核

对 `goals/reviews/2026-10-20-landau-siegel-determinant-and-weil-facilities.md` 当前落盘版本§§4–7的结论：**PASS，未发现须阻断消费的设施范围问题。**

- 容量／有效性类比保持为责任同构，没有把高度界报成平方RR或独立正极化。
- 数域、函数域及连续正反例的范围正确；正特征Wronskian反例和ordinary／divided derivatives的不同职责已明确。
- scalar near-1排除与全complex Weil正型被分开，χ=1及振荡方向的有限位障碍已列。
- (14)明确标为未构造的same-source责任，未计为新定理／经典正性；whole/core／coupling也未升级。
- de Smit–Perlis提醒限于非唯一重建，不扩大为不能从分布证明RH。
- 既定Γ来源门仍有可直接判定的公式，本轮未产出可优先准入的classic source→jet map。因此不以未知det标签启动新合同，不恢复暂停的零区优化，保留原next action有具体依据。

本次没有新数学结果可结算。新增的外部成功原型，使路线图A从抽象责任表转为可参考的实际设计；实际经典瓶颈仍是全源身份与独立全方向容量／符号控制。
