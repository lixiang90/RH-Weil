# Actual inverse-Euler滤波：强旧、域与相对test准入

2026-10-28；`/root/moment_fresh_audit` 当前独占任务，非cooling／Gaussian／fixed-poly续算。已恢复README／STATE、check→show、Goal／AV／frontier，实际读root本轮3617-byte规则及必要560／585／587／589和已消费filter范围。没有新web／PDF／章节／下载／数值，不改STATE／Git／cadence，不续C052原proof或gain优化。

**准入结论：actual规则合法，完整G_X逆没有被取消；现有强旧能直接付未归一化ν_X→0于strong S′、两个raw moments→0及β_X→∞，但本次未恢复到决定校准后g′/g相对量的已付链。** 这些合法性／exact重写／未校准极限是直接旧后果0；不能把它们称为首检已通过或已拒绝，也不能因ratio尚未判就自动授新数学／source预算。

## 1. 先统一D与actual frame

若用complex变量记d_X(s)=∏_(p≤X)(1−p^(−s))，则

    D_X(t):=d_X(1/2+it)=∏_(p≤X)(1−p^(−1/2)e^(−it logp))

正是560／585在physical Fourier坐标的B_X乘子；U_a r(u)=r(u−a)，rhat=∫r(u)e^(−itu)du。root文件已经把D_X写成real-frequency函数，不可再向它重复代1/2+it。没有改ζ模型、Γ、原du或Euler约定。

令M=RanP为固定arch Sonin，G_X=PB_X*B_XP|_M，Π_X=B_XP G_X^−1P B_X*。记K₀(t,t)为P按dt/(2π)的raw evaluation kernel对角，

    Q_X(t)=<k₀(·,t),G_X^−1k₀(·,t)>
           =sup_(||D_Xh||₂≤1)|h(t)|²。

同一actual kernel为k_X(t,t)=|D_X(t)|²Q_X(t)=2πρ_X(t)，所以当前measure准确是

    dν_X(t)=Q_X(t)dt/(2π)。                              (E)

只取消了外层|D_X|²。完整G_X^−1／returns仍在；ν_X不是固定arch density K₀dt/(2π)。在receiver上对应的exact positive operator为

    L_X=B_X^−1 Π_X(B_X*)^−1=P G_X^−1P。

它是weighted dual-frame operator，通常不是projection；B_X可逆不等于酉。把L_X换成P会直接改变本test对象。

## 2. Fixed-X合法性与非compact源解释

为免与空间维数混名，记a_X=∏_(p≤X)(1−p^−1/2)、b_X=∏_(p≤X)(1+p^−1/2)。每fixed X有0<a_X≤|D_X(t)|≤b_X，故

    a_X² I_M≤G_X≤b_X² I_M，
    b_X^−2 I_M≤G_X^−1≤a_X^−2 I_M。

560的逐X log密度界给ν_X为positive tempered measure；乘任意finite β_X>0仍然合法。原fixed-window自然型域仍为zero-extension Dlog：新旧density各以逐X正有限常数互相控制，其high-frequency log阶不变；这些常数不对X一致。

对原Cc∞测试，ordinary positive trace可直接写为Tr(A_r L_X A_r*)，由L_X与P的上述比较付TC／HS域；无需先把非compact源塞入完整Q恒等式。585非零entire Sonin向量也给ρ_X>0 a.e.，故ν_X>0 a.e.；非零g使0<S_X[g]<∞，β_X=q₀/S_X[g]确实定义。这里S_X是root命名的源配对，不与receiver Sonin投影混同。

若改用source deconvolution解释，有限X确有

    B_X^−1=Σ_(n为F_X-smooth)n^−1/2 U_(log n)，
    B_X^−1r=Σ n^−1/2 τ_(log n)r。

系数总和a_X^−1有限，固定X的全部log-moments也有限；因此compact smooth r被送到Schwartz／L¹／全线Hlog源，但一般不再compact，也不在全部指数强源S_exp。其原L¹／du／Hlog费用至多携a_X^−1等逐X因子，没有免费cofinal norm等距。

完整pole矩尤其不能省：对本题正g，Tonelli给

    μ₊(B_X^−1g)=μ₊(g) Σ_(n为F_X-smooth)1=∞  （X≥2）。

所以不能把560仅对原compact／指定强域付的full Q=T−K+P直接用到filtered g。这个域差并不使本规则非法：构造本来是在原compact源上定义stationary positive spectral distribution；filtered source无需另有完整Q。其目标q₀、q₁仍是原g、g′的完整合法值，g′ mean0不是polefree。

## 3. 不能漏掉的更强旧rawnorm极限

除了粗a_X^−2条件数界，C052上游终稿§3的strip证明实际已经支付real轴的

    |h(t)|≤C(1+|t|)||D_Xh||₂， C独立X。

这是h⁺/(z+2i)的两边界Hardy／Gamma界经strip PL去掉X prefactor后的直接real-axis限制。因此(E)中的weighted raw evaluator满足

    0≤Q_X(t)≤C(1+t²)  对全部real t／全部X。             (U)

不能把这一步缩回仅有m_X^−1 norm等价。另一方面，已根闭合的localization终稿6.12对每个first-fixed B给

    Q_X(t)≤exp[(-4+o(1))A]， |t|≤(logX)^B，
    A=√X/logX。

特别地，在每fixed compact上Q_X→0统一。配(U)，对S的任一有界集先用共同Schwartz seminorm去掉|t|>R，再固定R令X∞，得到

    ν_X→0 于strong S′。

这项是原uniform proof已经直接蕴含的强旧消费，不是新读6.4／6.5或新cofinal估计。对每个fixed compact smooth r、全部fixed源对也有S_X(r,s)→0；特别记G=ghat，

    J₀(X)=∫|G|²dν_X→0，
    J₁(X)=∫t²|G|²dν_X→0， β_X=q₀/J₀(X)→∞。           (Z)

所有finite j的t^(2j)|G|²也为Schwartz，未归一化对应矩同样趋0。这里不做rate／gain优化。裸零极限不能乘发散β后沿用，也不能把J₁、J₀两个趋零量相除报ratio→0。

## 4. 已付比较为何仍不决定唯一相对首检

令T_∞为固定arch P的普通trace，R_∞=T_∞[g′]/T_∞[g]∈(0,∞)。frame算子比较给对j=0、1分别

    b_X^−2 T_∞[g^(j)]≤J_j(X)≤a_X^−2 T_∞[g^(j)]。

因此仅有

    (a_X/b_X)²R_∞≤J₁/J₀≤(b_X/a_X)²R_∞。

这个cofinal条件数区间不收口。585还给J_j≥b_X^−2T_X[g^(j)]及各fixed源lower；587亦可给相应fixed derivative Gram的lower比较，但仍是分别下界，不是相对upper。589原T_X[g′]/T_X[g]→0针对未过滤ρ_X，不能穿过移动的|D_X|^−2后原样使用。

最便宜的实际未付量可以无歧义写成probability measure

    dπ_X(t)=|G(t)|²dν_X(t)/J₀(X)，
    J₁(X)/J₀(X)=∫t²dπ_X(t)。                            (R)

这里π_X才有总质量1；ν_X本身一般总质量∞。当前唯一target要求(R)→q₁/q₀>0。所读已付资产没有给π_X的相对tightness、t²统一可积性、normalized raw-kernel形状或直接的relative矩界；没有一个可消费的旧结论把其值固定为q₁/q₀，也没有把它严格排开。

具体缺口不是“再证明finite-X inverse存在”或“再付一遍ordinary trace”，而是原完整G_X^−1下的J₁相对J₀估计。若后续要判0、∞、另一个常数或无极限，都须付这条actual relative责任；把未知ratio改名input、只写两个lower或裸(Z)不够。本准入没有执行这样的新proof，也不授权它。

## 5. 与先前filter／anchor／gain停止范围的区别

当前|D_X|^−2是source-independent的真实有限Euler inverse，通常有无限Fourier delay列；不是fixed-degree polynomial，也不是fixed finite Gaussian-pulse target。587对fixed degree移动系数的控制不能免费用于这一非compact moving source；588共同支撑／弱非零和fixed-coercive anchor也不覆盖B_X^−1g的支撑与norm。它不是改ζ模型或使用σ/ρ来选择预定谱。

Gaussian旧exact σ/ρ可达性与576正锥只说明已给正target可另选权实现，不决定这份canonical weight输出什么；有限目标的uniformmass／atom门也不能套到ν_X。事实上固定X由arch log尾及frame lower即知ν_X(R)=∞，不存在那份finite总质量上界。Normalized β_Xν_X仍可作为positive tempered measure逐层合法；完整D′逼近和全部目标覆盖尚未付。

AS／AT的full positive D′→谱vague及必要局部指数gain门只给必要条件。对本规则必须保**总权**β_X|D_X|^−2；不能把β_X删去后用raw gain最大值判不可能，也不能以最大值够大判充分。Raw max出现在t=0，不是fixed away0 band的有效lower。由旧raw compact exponent，在假设一个fixed away0 band有非零目标谱质量时会要求logβ_X/A≥4−o(1)；已有frame校准upper的leading指数与之兼容，仍未判(R)。这里只恢复原必要性方向，不续gain／sharp参数。

同理，553的global bounded读出还须精确消去全部Pan等前提，不能由有限X可逆／正谱合法性套用；逐层positive D′并不被要求先是几何principal商。Source／receiver／完整Weil型的符号与域均不互换。

## 6. 当前分类、版本与停止

本稿已经闭合的旧0内容为actual D约定、L_X=P G_X^−1P、fixed-X原域／tempered性、裸ν_X strong S′零极限及β∞；未闭的是校准后唯一g′/g相对test。因此准确结论为“合法而首检未判”，不是候选失败／通过，也不是已经有经典独立signed输入。Root若选择后续责任，仍须另按真实可判量准入，不能自动续C052原sourceproof或创建数学轮。

| 已实际读取的版本 | LF bytes | SHA256 |
|---|---:|---|
| `root-actual-rule-and-admission.md` | 3617 | `eb76e65ac56c4efcee24ed312e9f72f8c256d9433112aaa702ea465dfdcffcf6` |
| 560 | 9263 | `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3` |
| 585 | 7857 | `5dca916d978eef599587ff4c6ce34144f814ddec0567a4c1b2314dcd71cd01af` |
| 587 | 8681 | `e4d30cfb6d07299386014cb4c4e3e3979ab5111264355dfb37b24629f121ac82` |
| 589 | 7185 | `c491012226713baf0eecff045338563d4e440c6a1bde9eea0d9ccf661b958bc5` |
| C052 upper/tail终稿 | 10211 | `bab769113b4ce8c858dfd4b7a83dea6abd8808436a599d2206ea9a9bf0915fff` |
| C052 localization终稿 | 11459 | `809bc7ffc6f1fbf4dd24af0d710af05fb7ca1bc259992430c3fd6760912ffcb1` |

原完整Γ／FP-contact、所有proper powers与双pole在q₀／q₁和最终目标中保持。Whole4/5仍仅负惯性UPPER，signedcorecross／非零primitive／principal／mixed／Ξ未改。无新source／数学迭代或counter，原cadence3/history53/latest589/formal17保持，Goal同实例active／open。当前仅交old-scope准入意见，非root已消费或新后继预算。
