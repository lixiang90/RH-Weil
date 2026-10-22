# 574 的 regular／Cartier 增强：函数域、连续正反例与容量控制

2026-10-22。独占 controls 原件，供本轮 root 消费。此稿不创建合同、不改 STATE／cadence、不自行推送。
它把下面的直接计算与标准来源门写清，不声称新的外部定理或经典 Weil 正性。

## 0. 先冻结本章来源门

输入是 [574](../../../notes/574-actual-adelic-cover-relative-picard-and-source-transport.md) 的实际两位覆盖、562 的完整连续正负模型、567 的曲面 RR 证明和已经实际执行的 genus-2 moving 控制。
可判门是：给这个覆盖加一个明确结构层后，Cartier 方程／局部商是否真正产生非平凡线、有限局部消失量、有限全局容量，并且这些设施是否能区分连续正负的完整 Weil 型。
净决策仅是检验这种增强能否支付下一源桥的独立前件；若只剩旧值的标签或自由添一根形式参数，则停止相应 recipe，保留不同 regular 子层及有费修复。

主要原件是 [Stacks 有效 Cartier 定义与局部非零因子条件](https://stacks.math.columbia.edu/tag/01WQ)、[proper 曲线 RR](https://stacks.math.columbia.edu/tag/0B5B)、[Milne JVs §1、§7.6](https://www.jmilne.org/math/xnotes/JVs.pdf)，以及 [Connes–Consani scaling site §§4.3–5.4](https://arxiv.org/html/1603.03191v1)。
Stacks 的 scheme 结论不能直接宣布 574 的空间是 scheme；下面只在明确的连续复值局部环层上使用“由非零因子生成的可逆理想”这一 ringed-space Cartier 数据。

## 1. 连续结构层确实给单边界的非平凡 Cartier 线

沿 574：固定 p=2、q=3，T=Z∪{∞}，Y=T²×R，Γ=Z²，去双 ∞ 层得 O。
Γ 作用为

`(a,b)(j,k,t)=(j+a,k+b,t+a log2+b log3)`。

Wp={k 有限}、Wq={j 有限}，交 B 的轨道坐标为 x=t−j log2−k log3。
各片 quotient 的边界分别是长度 log2、log3 的圆；O 全作用非 proper，不能将整体当成 Hausdorff proper 曲线。
取 Γ 不变连续复值函数层；等价地在这两片 quotient 上作局部环层并沿 B/Γ=R 粘合。

在 bulk 定义 ρ=e^x，向两个边界延成 0。
这是实际连续不变函数：靠近任何一个边界时其有限的相应整数坐标趋 ∞，而 t 及剩余有限坐标在一个局部 chart 内受控，故 x→−∞。
bulk 在每片稠密，ρ 在 bulk 严格正，因而任何局部 germ 上的乘法 `h↦ρh` 都单射。
同理所有 ρ^α，α>0，均为非零因子。

须区分两个构造。

1. 用两片相同方程 ρ^α，得到全局 principal Cartier 数据 `div(ρ^α)`；其关联可逆模全局自由，不产生非平凡 Pic 类。
2. 在 Wp 用方程 ρ^α、在 Wq 用方程 1，交上二者比为实际 regular unit ρ^α。由此得到支撑在单边界的可逆理想 I_p(α)。交换两片得到 I_q(α)。

局部基的换基是 exp(αx)，故 I_p(α) 的线类就是 574 的相应实参数 clutch（若采用关联 O(D) 而非理想 O(−D)，参数反号）。
由 574 的绝对 kernel 只有纯虚参数可知 α≠0 时它确实非平凡。
而

`I_p(α) I_q(α)=(ρ^α)`

为 principal；这是真正的两边界协同，不能从一个全局 principal 方程反推“该覆盖没有非平凡 Cartier 线”。
也不能把 574 的“没有 Γ 不变非退化正 metric”改写成“底层空间没有普通 metric”。

这些正设施的界限是：层 C 本身允许全部正实指数；整数次幂是合法过滤，却没有因此成为 DVR 阶。
给定实际 flow 后可额外指定权一方程 ρ，但这不使层中的 ρ^(1/2) 消失，也不把局部商变成有限长度。
一个更小的解析／regular 层可能排除这些元素；此稿不排这样的结构，也不声称不存在自然选择。

## 2. 实际局部消失商的严格负控制：长度不是有限的

在单边界的一点取连续局部环 A，令 α>0。
在 A/(ρ^α) 中，`ρ^β`，0<β<α，给线性无关的复向量类。

证明只需有限组合。若 β1<⋯<βm<α，且 Σ c_jρ^βj=ρ^α h，在固定边界相位的 bulk 序列 x_n→−∞ 上除以 ρ^β1。
连续性使 h(x_n) 有界，右边趋 0；左边趋 c1，故 c1=0，逐次剔除即得全部系数零。
因此该商复维无限；由于局部环 residue field 为 C，它也不能是有限长度局部模。

ρ^n 给确实的乘法过滤 `I^m I^n=I^(m+n)`，但并非函数域里长度恰为 n 的 DVR jet。
例如 ρ^β 属于何个整数过滤由外加指数格决定，而不是“有 Cartier 数据”就唯一决定。
只保零集或其拓扑支撑会丢掉 α，保理想又得到很多实权厚化。

这项反测限于所写 C 层。若换层后能证明边界 stalk 的离散 valuation、有限长度、base change 与两片 restriction 相容，它就是实质额外输入，必须按原范数运输；不能被本节一并否定。

## 3. 同一非平凡线仍有无限 bulk 截面；正 metric 不等于容量

任取覆盖上由非零 clutch 得到的线 L，取 bulk 一个紧区间 I。
每个 `h∈C_c(I)` 都能以第一片 frame 写作 h，以第二片 frame 写作相应的 g 倍或 g^−1 倍，并在 I 外延 0，给一个实际全局截面。
该空间无限维，且其全部截面在两个边界的任意正消失过滤中都为零。
这同时说明：边界的局部消失量可能完全看不见 primitive bulk 方向。

即使固定 |x|≤B、在该 bulk 窗上固定正 metric（或取 unitary 子族已有的全局不变 metric），C_c(I) 中仍能选无限多个支撑互不相交的 bump，并各自缩放至 sup norm≤1。
它们彼此距离至少一个固定常数；单位球不紧。metric 非零／正性并不提供有限维截面、离散整格或有限高度点数。
如换成 L²，固定窗上的单位球仍无限维；“窗是紧的”不支付 finite capacity。

这不否认可选择有界次数解析截面、有限 rank 近似、整格或别的有控空间。
但其 cutoff、restrict/lift kernel、乘法、坏 chart 切换及误差必须另给，不能把任选有限维子空间的维数称作对象自身 RR 容量。
尤其外 tensor 两个已有线性容量、或 direct integral 再积分一次，并不自动给 primitive 对应的平方 RR 二次系数。

## 4. 函数域为何不落入这个负控制

对真实光滑射影曲线 C/F_q，K=F_q(C) 的每个闭点 P 有实际 DVR O_P、uniformizer π_P 和整数阶 ord_P。
局部 `O_P/(π_P^m)` 的长度为 m；除子 D 的截面是同一个函数域内满足 `ord_P(f)+n_P≥0` 的全局函数，绝非任意连续函数。
restricted product 给

`Div(C)=A_K^× / ∏ O_P^×`，

再除全局 K^× 的像才是 Pic(C)。加权总阶对 principal 为 0 来自乘积公式；两端局部单位与全局 principal 不是任选 frame。
这列举的是标准曲线设施，不给 574 凭空赋一个有理函数域。

proper 性使 H^0 有限维；RR 给曲线上的线性次数预算，C×C 的 RR／Hodge index 再控制 signed primitive 对应的二次交数。
后一步不能由前一步 tensor 形式地替代。
567 §2 的实际证明有一个特别清楚的容量门：若 D·H=0 而 D²>0，RR 迫使 H^0(K±nD) 至少二次增长；非零截面的乘法却把其中一个注入同一个固定有限维 H^0(2K)，矛盾。
其中截面、乘法、degree 约束与 fixed capacity 都在同一曲面上，独立于 ζ 零点。

Milne JVs 的 Picard family 也先有 proper 曲线和上同调 base change，再在非特殊 chart 中选相对有效代表；特殊处用 degree-zero twist 移动，overlap 通过 Picard 类校正。
这说明需要运输的是同一结构的移动与 restriction kernel，不只是一个非平凡连续线类。

旧真 genus-2 控制仍有效：`C/F5:y²=x⁵−x+1`，P=(0,1)、Q=(1,1)，K~2∞。
ω0=dx/y、ω1=x dx/y 在 P,Q 的评价矩阵为 `[[1,1],[0,1]]`，故 H^0(K−P−Q)=0。
于是 L0=O(P+Q−2∞) 非平凡 degree 0，h0(L0)=0，而 h0(K⊗L0)=1，区别于 h0(K)=2。
普通重复点需厚点修复，branch／special 处也可能真降 rank；不能要求固定 raw minor 处处非零。
本轮只消费已经审过的控制，不重跑脚本或重计曲线定理。

## 5. Connes–Consani 已有真 regular 与周期 RR；未付的是比较

[CC 的原文 §§4.3、4.4](https://arxiv.org/html/1603.03191v1#S4.SS3) 已有 fraction sheaf、Cartier 及 order；[§5](https://arxiv.org/html/1603.03191v1#S5) 在实际周期 orbit Cp 上给 divisor、theta 与 type-II RR。
其 Thm 5.6 是 `Div(Cp)/P ≅ R × Z/(p−1)Z`；Thm 5.17 给

`Dim_R H0(D)−Dim_R H0(−D)=deg D`。

这里 Dim_R 是滤过后正规化的拓扑维数极限，并非有限维复向量空间的 dim。
这是严格正设施，不能简化成“算术空间还没有任何 regular 层／任何 RR”。
不过 Cp 上的结果不自动等于 574 的 O 上混合两位线、全部位的对应平方、物理源 map 或完整 Weil mixed 容量。
一个 circle 的 degree 与线性 RR 尚未给出任意 signed 两边界组合的自交项。

仓库也已有真实解析设施：[367](../../../notes/367-f1-periodic-cartier-sections.md)、[380](../../../notes/380-f1-perfectoid-annuli-and-periodic-line-bundles.md)、[384](../../../notes/384-f1-finite-level-cartier-regularity.md)、[387](../../../notes/387-f1-analytic-continuation-and-cartier-regularity.md) 的局部环层／perfectoid 环域／Cartier 正则性；[396](../../../notes/396-f1-flat-line-enhancement-and-cartier-pullback.md) 的平坦线与截面拉回。
[401](../../../notes/401-f1-dual-cartier-ideal-and-reflexive-collapse.md) 对具体 J 则付了不是 locally finitely generated／不可直接可逆化的边界。
这些对象不能与 574 连续 O 无证明地相等；“都有 log p 圆”不产生 regular-unit 层的 pull/push 函子。
本门不另串下一篇 paper：若无从该层到本轮实际覆盖的具体 transport、同源源桥和 mixed 容量，就到此停止消费。

## 6. 连续完整正反模型：即使自由加 DVR jets 仍不选 Weil 号

使用 562 已独立证明的正 primitive／prime-power／g-integer 测度族

`Z_c(s)=1+c/[s(s−1)]`，`d=c−1/4=±1/16`。

模型 Γ=0 是其既定完成化，不是从经典删掉 Γ；原极点 0、1 与完整 Π 都保留。
其 primitive 源代数为 `R_d=C[w]/(w²+d)`，`w†=−w`，

`a_r=∫r(u)e^(uw)du=A_r+B_r w`，

完整型为 `Q_c(r)=2|A_r|²+2d|B_r|²`。

取同一个实偶 φ≥0、非零、支撑 (−1,1)，令 g=uφ、`r=(D²−1/4)g`。
由端点分部积分 μ±r=0。A_g=0；在本支撑和 d=±1/16 上，B_g>0，分别由 sin(u/4)/(1/4) 与 sinh(u/4)/(1/4) 的符号立即给出。
再次分部积分得 `a_r=−c a_g`，故

`Q_c(r)=2d c² B_g²`，

两模型严格异号。源 r、原 du／Dlog 范数、两个 pole 矩的精确零均相同。
没有用数值算零点，也没有给一般连续系统虚构经典 adeles。

一个很便宜的 regular 增强负控制是 `R_d[[t]]`，t†=t。
作为普通复代数，两段 R_d 都同构 C⊕C；该增强都有两个实际 formal DVR 分支、同一个 regular parameter t、可乘的整数消失过滤以及 `dim_C R_d[[t]]/(t^n)=2n`。
用有界 t 次数时，普通截面维数也是相同的 `2(N+1)`。
但源仍经旧 a_r 标签，Q 号不变。正段的 † 是逐分支共轭，负段的 † 交换两分支；正 Hermitian metric 可以任选，不能因此把负段 † 变成正 adjoint。

因此“regular 参数＋有限 jets＋非退化评价＋正纤维 metric”本身不是充分包。
这只反测**自由的 Cartier/DVR 添层**，不是一个关于全部 geometric enhancements 的 no-go：若新的全局几何独立使 † 来自 ample polarization，并给同一源的 RR 自交比较，它正好超出了这个负控制。
它也不能把对 t 的 tensor 容量冒充原模型 primitive RR；形式参数是明确新增的辅助层。

## 7. 405、537 和原费用在容量门中的责任

574 的旧双测试不能因引入 Cartier 方程而跳过：

* 405 的实际全主关系 `P=(D²−1/4)H∈P_c`，H=e^(u/2)h>0，有 μ±P=0，却有 `∫P=−(1/4)∫H<0`。
* 537 的 `r0=(D²−1/4)ψ`，ψ≥0、非零、紧支于已付小窗，有 μ±r0=0、Qζ(r0)>0，且同样 mean 非零。

在实源上若把 mean 当单边界 Cartier 实权 α（负权用 Cartier fraction／逆线），它仍看见 537，却把 405 主关系送到非平凡线；改名为 vanishing order 不修同构失败。复源的任意复权是否可作该层的 Cartier 方程须另核，不能由实权自动延拓。
若只用两 pole 矩选权，则消去这条主关系但也消去 r0。
若用旧谱商的系数／完整 Q 反定义该权，这个 map 可以合法，仍是旧读出；须另外给 independent capacity，不能把“类非平凡”作为正号。
这里不把 source-quotient 因子化本身说成错误：所有消关系映射都须因子化，缺的是区别于旧读出的真实整性与比较。

对原源支撑 [−A,A]，574 已付

`|∫r|≤sqrt(2A)||r||_du≤sqrt(2A/log2)||r||_Dlog`。

第一项是 du 精确 dual norm，后一项只是 upper；A→∞ 不能当统一费用。
覆盖 frame 的 x 窗另记 B，不能与源 A 混同：`||exp(αx)^±1||∞≤exp(B|Re α|)`。
这只是指定代表的费用，不是所有可能 lift 的必要下界，也不等于函数域的原高度。
不变非退化正 metric 的失败或 frame 增长，不能自动化成全方法的 source 成本下界。

旧衰减 clutch 若由 κ*r 构造，在 compact 源时负端恒为 1；在 S_exp 源／compact κ 时，对每个 n 都有 `(κ*r)/ρ^n→0`，故它的差离 1 对整数 ρ 过滤是 flat。
在 C 层里它已有相对 trivial gauge，所有边界 jets 也不恢复失去的 primitive 类。
若更小 regular 层不包含这个 gauge，必须先证明源 map 确实落入该层及其 unit／fraction 域；“排掉坏 gauge”不能代替这项准入。

## 8. 完整目标不随 Cartier 增强变小

经典目标仍是 574 §8 的同一完整 Qζ：arch multiplier

`Γ(t)=Re ψ(1/4+it/2)−logπ=2θ′(t)`，

含完整 contact；有限项为全部 `(log p)p^(−k/2) Re(r*r*)(k log p)`，k≥1；pole 为 `2 Re(μ+r overline(μ−r))`。
双 pole-zero 测试源上的 pole 精确消失，是检验门，不是删去目标定义。
连续例 Γ=0、函数域所有周期 aliases／pole 都按各自规范完成化保留。

只有 p=2,3 的局部 Cartier 权还没有覆盖全部 p^k，更未恢复实位 ψ 的 finite part。
已有 569 的 Fourier/Haar 规范与 matched cocycle 是输入；给任何一个正 line metric 并不重新证明它们与本轮容量的 identity。
需要同一真实层、相同 source cutoff 与 norm 的预算，使 arch、每个 finite place 与 pole 缺陷协同变换，然后证明该预算的 primitive 二次项等于 −Qζ。
假设这个二次项有要求的号，或直接以 Q 定义它，再由 RR 名称推出正性，只回到 Weil 等价写法。

## 9. Root 可消费范围与唯一结论

本分支付的是：C 层上的实际单边 Cartier 正设施；无限局部商／bulk 截面反测；CC 真周期 RR、真曲线 moving 与正负连续完整型的逐项比较。
标准 FF／CC 来源不另计；实际单边 Cartier 与过滤的严格比较若由 root 纳入 C038，只与该合同统一消费一次，不应由本分支重复计轮或称为独立经典新正性。
若 root 的其他分支给出新的 regular 层或源映射，必须按它的实际 domain、405 同构、537、metric 及 cutoff 重新消费，不能由本稿摘要直接验收。

仍欠的最小独立设施是：

1. 一个与实际 adelic cover／对偶相容的 regular-unit 与 fraction 层，不由 Ξ 或完整 Q 标签选出；同一层上有正确的全 principal 来源及可乘局部过滤。
2. 非根可见的物理源→相对移动对象／截面，405 全主关系给实际同构；原 du／Dlog 的 lift、restriction 与成长换 chart 费用可付。
3. 同一对象上的 primitive 有效性／mixed RR 或 ample Rosati 容量，而不是自由 t 方向、单圈次数或任选有限维容量。
4. 该独立容量与完整 Γ、全部 prime powers、pole 以及全 complex 源的精确比较，保全部误差与补空间 coupling。

宏观实际瓶颈未改；最强旧实际 ζ 后果仍 542+555→557 的 whole leading 4/5 负惯性上预算，不提供负惯性 lower，也不是成长 core／Ξ。
本门不宣布 Cartier／relative 方法不可能；只停止已被旧 scalar 标签或自由 regular 添层重复实现的入口，不自动接下一篇来源或同一未付容量的改名。
