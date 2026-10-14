# Adelic primitive 来源门：Hodge原域、实际metric逃逸与未付比较

2026-10-14，独立来源类别审查，**零数学轮**；不重开C021、不建C022。
按AGENTS恢复README/STATE/check-show、同Goal/frontier、D20261014Z、下一adelic门、
406及C015末节。结构check通过不认证数学。
入口现场HEAD `56270972893773289738ad258151bb4174cb742a`；root的git属性/ignore与来源目录
有进行中改动。子get_goal=null，不代root同G20261014运行观察。
只写本稿，不改公共状态/Goal/cadence/Git。冻结基线仍0c4f/≤538。

## 1. 原独立定理实际要求什么

一级[Yuan–Zhang作者PDF](https://web.math.princeton.edu/~shouwu/publications/hodge-I-version2.pdf)，
版本May21,2013，*The arithmetic Hodge index theorem for adelic line bundles I: number fields*。
root缓存48页/695199 bytes，本代理现场复核PDF SHA256
`954f560c65324f5ca1adb130c86f566eeaf66464ec2391cff00d036eecda25e2`，
text SHA256 `67061ff98b55a80ee8d347831bf6af76514e3ec481828f9c16b5b96d4367011b`。
PDF技能视觉核印刷4/10/13/14/16页；web截图失败后改读root已渲染原页。
以下是旧定理的正确消费条件，不称新算术Hodge theorem。

Theorem1.3（印刷4页）：K number field；X/K normal、geometrically connected、projective，
dimX=n≥1；M̄ integrable；L̄₁,…,L̄_(n−1) nef、其底层L_i big；
**generic algebraic** primitive条件M·L₁…L_(n−1)=0给
M̄²·L̄₁…L̄_(n−1)≤0。等号判据另要求L̄_i arithmetically positive、
M̄ L̄_i-bounded，才等价于rM̄=π*M̄₀、r>0。若M底层numerically trivial，
原文允许相应弱化；不能因此删掉integrability或模型条件。

nef指由nef Hermitian模型度量的一致极限；integrable是两个nef adelic bundles之差。
L̄-bounded要求某integerk>0使kL̄±M̄均nef。度量覆盖**所有places**、连续/Galois invariant，
且除有限places外来自同一个integral model（Def1.2、2.1/2.2，印刷3/10/11页）。
这不是只给一个complex Green function或generic度数零即可调用的规则。
等号只给来自base（或相应torsionmultiple）的类，不把每个非零source标签强制为非零class。

曲线n=1没有L_i；generic primitive条件就是deg M=0。
原Prop2.4（印刷13–14页）对regular、geometrically connected arithmetic surface的
smooth vertical model给非正自交与base-constant等号判据。它正可用于下面P¹_Z模型。

## 2. 406给了哪些真实数据；literal停止不是全类别停止

406真实Gaussian族为

    F_η(z,w)=Π_(n≥1)(1−zη(ne^w))²，F_η(0,w)=1，|Imw|<π/4。

它在C_z×该strip上全纯，非空局部principal Cartier divisor与标准倒数零点读出已经旧有。
非零值η(ne^w)对应z=1/η(ne^w)，重数含±n；标准线性铅笔的trace为

    −∂_zlog F_η(0,w)=Eη(w)=2Σ_(n≥1)η(ne^w)。

指数单位改变任意代表的一级log导数，却不改其analytic零divisor；
只有按406固定标准乘积/倒数根读出，才能继续称规范trace。
F中的z是auxiliary determinant坐标，w是analytic continuation参数；
complex w不能未经证明当actual idèle，更不是已给的number-field algebraic参数。

固定Gaussian w的无限零点阻literal finite projective fibre divisor，是406的旧直接后果，
本稿不重计边界。另一些确切finite障碍也须分清：

- 有限F_R(z,w)=Π_(n≤R)(1−zη(ne^w))²在固定w是degree≤2R的complex polynomial，
  可以进入complex P¹。但其coeff属于某number field，406未证明；本稿不声称具体η₀(n)
  的transcendence已知。让所有real w的非常数analytic coefficients同属fixed K不可能，
  因K countable；这不排逐w另选模型或只用archmetric。
- 若coeff确在K，zeros给O(D)正degree；减degree·[∞]得到principal div(F_R)，
  完整principal arithmetic pair商掉是零class。primitive化不能一边删degree，一边保
  原Green/energy不变。P¹上的底层degree-zero line bundle本来trivial，metric仍可非trivial。
- analytic determinant line/复杂流形Cartier已经合法，但不是number-field projective adelic
  M̄。有限参数、rational approximation、analytic/nonliteral metric仍是允许修复，不能因上条排除。

下一节展示**实际source-defined的合法nonliteral model**，因此“任何actualmodel不存在”是不正确结论。

## 3. 径向trace metric：确有合法P¹_Q primitive adelic对象

取405/406的实际

    η₀(r)=(4z⁴−28z³+41z²−9z)e^−z，z=πr²，
    p(u)=Eη₀(u)，p≠0，d(p)=c(p)=0，B(p,g)=0，ALL g∈S_exp。

p由原source及标准Fredholm读出定义，未使用Q值反造metric。
在另一个几何坐标ξ∈P¹(C)上定义ϕ(ξ)=p(log|ξ|)，ϕ(0)=ϕ(∞)=0。
这里新增的radial坐标选择必须记录；它不是F的auxiliary z divisor本身。

**实际smoothness。** η₀(0)=∫η₀=0、Gaussian polynomial的Fourier transform仍是Gaussian polynomial。
λ=|ξ|→∞时所有Eη₀的Euler derivatives有polynomial×e^(−cλ²)界。
λ→0时Poisson给

    Eη₀(logλ)=λ^−1·2Σ_(n≥1)hatη₀(n/λ)，

并有所有Euler derivatives的polynomial×e^(−c/λ²)界。
转成任意Cartesian derivatives只再乘λ的有限负powers，因此在ξ=0及1/ξ=0都C∞flat。
ϕ为全P¹(C)的real smooth、conjugation invariant、nonconstant函数。

取K=Q、X=P¹_Q、integral model Xcal=P¹_Z；底层M=O_X。
每finite place取model trivial norm||1||_v=1，arch取

    ||1||_∞=exp(−ϕ)。                                (3)

这是all-place coherent、continuous/Galois-invariant的真实Hermitian model，
底层generic degree0，故primitive条件确实成立。finite place为零并非省略未知place。
但它只实现了这个指定radial repair，没有自动实现全部prime arithmetic pairing。

**Integrable与bounded的付款。** 固定FS O(1)模型，加一个base常数B>0，得L̄：
curvatureω_FS>0，所有normalized algebraic-point heights≥B，L̄²>0（B足够大）。
ϕ smooth compact给P=sup|ϕ|<∞及H=sup|ddᶜϕ|/ω_FS<∞。
取integerk大到k≥H、kB≥P，并使

    k²L̄²−2k|L̄·M̄|−|M̄²|≥0。

smooth model intersection在此定义良好，不循环使用integrability。
于是kL̄±M̄：curvature≥0，所有horizontal-point heights≥0，
vertical fibres上degree=k>0，total arithmetic-surface selfintersection≥0。
这些是P¹_Z全部维数的nef测试；故kL̄±M̄为nef Hermitian models。
M̄=(kL̄+M̄)−kL̄ integrable，且M̄ L̄-bounded。
在曲线theorem没有额外L_i，但这一domination独立验证了所需integrability。
没有uniform全部η/f/growth的k或费用结论，不能从这个单source存在性继承它。

## 4. Exact radial energy及等号；Green名称不代norm规范

原PDF印刷16页视觉明确：若N̄ finite metrics trivial、||1||∞=e^−φ，则
M̄·N̄=∫φ c₁(M̄)。结合原Chern convention，固定

    ddᶜ=(i/π)∂bar∂，c₁(M̄)=ddᶜϕ，

(3)的自交精确为

    M̄²=∫_(P¹(C))ϕ ddᶜϕ
        =−(1/(2π))∫_C|∇ϕ|²dA
        =−∫_R|p′(u)|²du<0。                        (4)

最后一步由ϕ=p(logr)，polar面积2πrdr及d/dr=p′/r，所有端点flat故无boundary费。
有限places贡献严格零，原Q只有一个arch place，未漏place倍率。
若改用Green=−log||1||²，需同步其intersection convention；
不能把该Green名直接代原Prop2.4中的g而制造factor2/4。
(4)也可仅按strict negative使用；其exact factor由metric/Chern/p16公式固定。

等号只在p constant时成立。p两端0且非零，故不constant，M̄不是base pullback，
更不能是principal arithmetic零class。这与原Prop2.4/Theorem1.3一致。

但是**这个repair不保405/406的principal/radical下降**：旧B(p,p)=0，
而−M̄²=∫|p′|²>0。若目标要求pairing-preserving primitive realization，
两者不能同时作为同一source配对。正确地把η₀主关系送零class完全允许，
没有要求其非零label必须保非零class；(3)偏偏不是这种零class实现。
这只排指定radial trace metric的faithful下降，不排另一个canonical construction。
尤其不据此把p直接认成物理Q_L的非零根；406-source与physical变量的桥尚未付。

## 5. finite-n与normalized-degree修复的实际边界层费用

对同η₀的标准finite determinant，trace是

    p_R(u)=2Σ_(1≤n≤R)η₀(ne^u)。

在每个fixed compact u，它与所有derivatives趋p，来自406的Gaussian尾。
每fixedR的p_R(log|ξ|)仍在0/∞ smooth（0处为even Taylor，∞Gaussian），
因此也给单个合法model metric；不能误称finite修复在域上根本不存在。

但**它不uniform adelic收敛到(3)**。选fixed s>0充分小，使η₀(st)<0、0<t≤1，
因η₀(r)=−9πr²+O(r⁴)。在ξ_R=s/R有Riemann-sum精确极限

    p_R(log(s/R))/R→2∫_0¹η₀(st)dt<0，
    p(log(s/R))→0。

所以logmetric sup误差≥c_sR；这不是仅infinite literal零点的重复。
degree normalization p_R/R在每fixedξ趋0，但在ξ_R处仍保持非零极限，
仍不uniform收敛至trivial metric。

更完整的封口对**任意real scalars a_R**成立：

    a_R p_R(log|ξ|)在compactified P¹上uniform收敛
       iff a_R R→0；此时唯一limit是0。                (5)

必要性：取fixedξ₀使p(log|ξ₀|)≠0；uniform收敛到continuous G与p_R(ξ₀)→p(ξ₀)
先迫a_R→a。全部fixedξ∈C×再给G(ξ)=a p(log|ξ|)，两端G(0)=G(∞)=0。
移动ξ_R=s/R→0时，uniform与continuity给a_Rp_R(ξ_R)→0；
p_R(ξ_R)/R→c_s≠0遂逼a_RR→0，故a=0、G=0。
充分性由sup|p_R|≤2Rsup|η₀|直接成立。
这是完整compactified/Sup-logmetric范数的结论，不用pointwise冒充uniform。
例如R^(1+ε)归一化确得trivial metric极限，R归一化仍失败；
整个指定finite-n trace scalarrepair类均不能保非退化uniform极限。

finite-n本身没有必须丢掉dual moments：本η₀满足
∫₀∞η₀(t)dt/t=0、∫₀∞η₀(t)dt=0（由405 Euler/Mellin公式），
故finite sum的M_(p_R)(0)、M_(p_R)(1)也各为0。
所以(5)的费用不能归咎于“finite截断必破degree/moment”；真正障碍是compactification boundary layer。
双矩零仍不自动给B-radical：finite Mellin式用Σ_(n≤R)n^−s代替全ζ(s)，
本稿不把p_R免费列入旧B的根空间。

这只核**finite-n trace radial metrics与任意scalar normalization**。
有限η_R可另用compact cutoff加双矩补偿来保η(0)=∫η=0；
但其Fredholm rank随λ→0仍增长，不能称整个w族固定finite degree。
更不同的Green正则化、algebraic/rational截面近似、nonliteral模型允许继续存在；
必须另给同一对象的all-place uniform limit、primitive/quotient及完整费用。

## 6. 其余合法修复及明确未付链

有限w/有限F_R若经一个已指定rational approximation进入K[z]，可在P¹_K给
实际algebraic divisor及标准all-place model；degree≥0与primitive化的principal零类责任仍在。
arch-only smooth修复也可用cutoff·log(1+|F_R|²)定义trivial vertical metric，
再FS/base domination给integrable model。它不会因coeff不是algebraic而自动失败，
但cutoff/regularization/auxiliary坐标和zero-divisor损失必须收费，不称canonicalFredholm实现。
本稿不按已知Q或谱内积反造这些metrics。

完全principal pair(div f,−log|f|²)的表示与其arithChow/Pic零class不同；
local unit的Green分量可非零，不能独立强制其为零。analytic F不是已认证的K(X)^×，
合法principal-pair规则也不能因此自动施于它。

尚未付的最小闭合记录是：

- 同一actual source到normal/projective number-field X、底层M及全部places的canonical构造，
  保原source乘法、标准Fredholm/单位规范、principal quotient；(3)仅一个不同radial metric。
- 全complex源、原L²/Dlog及成长统一性；real smoothmetric的polarization不自动给实际sesquilinear Weilkern。
- generic primitive degree与dual moments的准确对应，以及nef/integrable的uniform模型/metric费用。
- actualΓ=2θ′、全部properpowers、双pole与arithintersection的same-source比较；finite trivial metrics
  不能无证明表示全部prime贡献，(4)只是原Dirichlet能量。
- principal/radical范围保非退化实际probe：η₀送零class允许；
  已付actual r₀=(∂ᵤ²−1/4)ψ、Q(r₀)>0只提供旧非根probe，尚无406→physical r₀的坐标/配对构造。

结论：原Hodge定理独立且可用，**真实合法primitive adelic metric model确存在**；
指定radial trace repair却不保旧principal/radical配对，指定finite-n trace修复有已量化uniform费用。
因此当前没有新全Weil/成长净后果或input/test/net三句准入；来源类别审入口零轮停止。
不排finite截断、complex-analytic、nonliteral或付费metric的所有可能方案，
不以旧literal∞障碍、η₀零类或单个模型/Hodge负自交完成宏观Goal。
