# 函数域正性的来源重审：有效化、相对评价与真正的极化

2026-10-22。独占来源原稿；同 G20261014／0c4f，供本次路线图 root 消费。
读过 563、566、567、568 与 307 的原证明，并重新浏览下列作者原件。
本稿没有新函数域 RH 定理，没有新数学轮，也不将标准几何的具体重建编号为 574。

## 1. 三条证明组织及其不可省的独立输入

**曲面组织。** 567 的实际链已经完整：在同一 C×C 上的截面乘法、有效性的 ample degree、
surface RR 与固定 h⁰(2K) 容量，推出 Hodge index；Frobenius 图交数再给全部混合 Weil Gram。
这个负号先于零点位置。重读 [Milne, The Riemann Hypothesis, Thm 1.2](https://jmilne.org/math/xnotes/pRH.pdf)
没有发现一个可以脱离真实截面和有效性、直接适用于一般正 g-prime 测度的新 RR 定理。
567 的有限预算版本仍是条件接口；其未知 ε、η 和二次系数身份没有由本次文献阅读支付。

**Jacobian 组织。** 实际 ample 线丛 L 给 λ 及 Rosati 对合 α†=λ⁻¹α∨λ；
正号由几何交数而来，不由对偶的形式公理而来：

\[
 \operatorname{Tr}(\alpha\alpha^\dagger)
 =\frac{2\dim A}{(D^{\dim A})}
       (D^{\dim A-1}\cdot\alpha^*D)>0\quad(\alpha\ne0).
\]

另一个独立身份是 F†F=q：它由实际 Weil pairing 与 Frobenius 在 Tate twist 上的作用给出。
二者同属同一 Jacobian，再与点数 trace 比较，才得到曲线纯性。
[Milne, Abelian Varieties, §17 Thm 17.3 与证明、§19](https://www.jmilne.org/math/xnotes/AVs.pdf)
明确把 pairing/交数比较列入证明。以“某个正 H 使 F*HF=qH”代替 ample 几何，
在有限递推类虽可成为有限证书，仍没有增加独立几何来源。
307 已具体重建椭圆 degree 二次型；563 已有精确 H 证书；566 已有全时间 ordinary heat lift，均不能再算新输入。

**Weil 原对应／评价组织。**
[CCM 2007 §2.3, (2.35)–(2.46)](https://arxiv.org/html/math/0703392v1)
从 degree 调整、RR 有效化，转向 canonical 截面在对应像点上的评价行列式，
用碰撞消失量与极点 degree 比较而给正迹。这条链要求选择合适代表并处理非退化及交重数；
“每个 fiber 存在某个有效 divisor”本身不保证展示的 determinant 是非零有理函数。
这正是本次唯一实际来源首门，下面用真曲线检验；不是重新证明 567 的全 Gram。

## 2. 真 genus-2 曲线的三种长度二评价：实际执行首门

在 \(k=\overline{\mathbb F}_5\) 上取光滑射影模型

\[
 C:\quad y^2=x^5-x+1.
\]

右端导数为 −1，故平方自由；char≠2 的 degree-five hyperelliptic 模型只有一个 infinity，genus 2。
下列计算是固定曲线上的局部代数，不使用点数估计、Frobenius 根或 Hasse–Weil 界。
令 ι(x,y)=(x,−y)，取 canonical basis

\[
 \omega_0=dx/y,\qquad \omega_1=x\,dx/y.
\]

在 infinity，ω₀ 的消失阶为 2，所以 K∼2∞；ω₁ 在 infinity 正则且非零。
每个 finite 点上 ω₀ 都是 canonical line 的非零 frame：nonbranch 点显然，branch 点由
\(2y\,dy=-dx\) 得 \(\omega_0=-2dy\)。因此可以直接评价系数 1、x。

### 2.1 非分歧点的 2P：普通重复列失败，真正 jet 成功

设 P=(a,b)、b≠0，局部参数 t=x−a。长度二子概形 2P 的 ring 为 k[t]/t²。
在上述 canonical frame 下，评价

\[
 H^0(C,K)\longrightarrow H^0(2P,K|_{2P})
\]

的矩阵（列对应 1,t 的系数，行对应 ω₀、ω₁）是

\[
 \begin{pmatrix}1&0\\a&1\end{pmatrix},\qquad\det=1.
\]

若把同一个非约化 divisor 错作两份 ordinary point evaluation，两列相同，det=0。
这是表示退化而非真实 jet 退化；用 dx 作局部 frame 会得到等价的 unit 因子 det=1/b²，
不得把 frame 变化错当符号或费用。

### 2.2 分歧点的 2P：真实特殊性，任何换基都不能补秩

设 P=(a,0)，其中 a⁵−a+1=0。t=y 是 uniformizer。写 δ=x−a，则

\[
 t^2=\delta^5-\delta,
 \qquad \delta=-t^2+O(t^{10}).
\]

因此 x=a mod t²，同一真实长度二评价矩阵为

\[
 \begin{pmatrix}1&0\\a&0\end{pmatrix},\qquad\operatorname{rank}=1.
\]

div(x−a)=2P−2∞，故 2P∼K，h⁰(2P)=2、h⁰(K−2P)=1。
这是 intrinsic rank drop；改 local frame 或把普通值换成 jet 不会消除。

### 2.3 P+ιP：约化且有效，也可始终 special

b≠0 时 P≠ιP，但两点 x 坐标同为 a；分别用 ω₀ 作 frame，评价矩阵为

\[
 \begin{pmatrix}1&1\\a&a\end{pmatrix}.
\]

它 rank 1，并有 div(x−a)=P+ιP−2∞，所以此 divisor 一直属于 canonical pencil。
这排除“只要 reduced/effective 就有所需 nonzero determinant”的推断。
对应 Δ+Γι 在 Jacobian 上作用为 id+(−id)=0，是 Pic correspondence 的零类控制，
不能把其 determinant 退化称为对 Weil 非平凡正性的反例。

## 3. 2Δ 的真实 self-intersection：碰撞数不是任意有效交数

取实际有效对应 Z=2Δ。它有 d(Z)=d′(Z)=g=2，ordinary 评价列恒重复。
但 Z 在 correspondence quotient 中非零；其作用是 Jacobian 上 [2]。
transpose 不变，复合 Z⋆Z′=4Δ。由于 genus 2 的 Δ²=2−2g=−2，

\[
 \operatorname{Tr}(Z\star Z')=4+4-(4\Delta\cdot\Delta)=16>0.
\]

若形式拆成 d′(Z)Δ+Y，则 Y=2Δ，与 Δ 共有分量，Y·Δ=−4。
所以这里不能把 Y·Δ 解释成一个有限集合的非负 ordinary collision count。
评价 determinant 的恒零也不给一个可数零 divisor 的 degree。
这不否定 Weil 正性、其交数公式或原证明；它否定的是未经 moving/proper-intersection
检查就对任意 effective 代表套压缩行列式论证。真正 jet 可以修复 §2.1 的非约化评价，
但没有单独支付这份 global excess-intersection 及 collision 预算。

对于 Δ+Γι，Y=2Γι，与 Δ 的 tame 固定点交数为 2(2g+2)=12；其 primitive trace 为零。
这又提醒必须保留“非平凡 quotient 类及合适代表”责任，不能对特殊零类套声称严格正的下界。

## 4. 原证明如何实际取得合适族，而非逐点任意选择

[Milne, Jacobian Varieties, §5 Thm 5.1/Lemma 5.2；§7 Lemma 7.1、Prop 7.2、Thm 7.6](https://www.jmilne.org/math/xnotes/JVs.pdf)
给出所需 independent geometric 设施：SymᵍC→Picᵍ 是 birational，generic degree-g divisor 的 h⁰=1；
相对 effective divisor 可在 constant-h⁰ open 上由 pushforward line bundle 的 canonical evaluation 构造。
特殊 fiber 由 degree-zero twist 移入这样的 open，再用真实 Picard translation 和 overlap glue。
这不是任意逐点挑解，且没有使用 RH。有限域上未必有原域 rational 的 generic 选择，
几何 base extension／descent 也须保留；没有因此获得经典源的 uniform 解析费用。

本次具体首门结论：**RR 的存在断言、真实 jet、generic 非退化、特殊 locus 的 patch/moving、
proper collision 与全局 degree 预算，是不同设施。**
“取一个非零 minor”并不同时取得它们；本稿也不拿某个坏 minor 的逆发散当必要的 physical 源费用。
族或 determinant line 可以合法跨图册工作，须另外证明最终 pairing、过滤及费用的协同变换。

## 5. 对一般 g-integer 迁移的具体研究准入

本次没有把“Picard functor／极化存在”定成新公理后声称完成证明。
下一门若继续此路线，实际输入应当是一个**不以 Ξ 零 divisor 为 base、并已有乘法／对偶的候选族**；
输出至少须有：

1. 对 source r 及 405 全 principal 同伦，给相容的 relative line object／有效化族，而非各 r 任意 probe；
2. degree-zero 移动保持既定 quotient/双 degree，并使 537 非根仍可见；
3. 真实 base-change、special fiber 的 gluing/jet/excess 项和局部消失过滤；
4. 在同一整模型上独立证明 primitive capacity，再把其 coefficient 识别为完整 Weil 型。

每一步保 r=e^{u/2}f、原 du/Dlog 与成长量词；几何有非零 determinant 不代这些 norm transport。
563 的有限 H、566 的 heat identity、567 的全 Gram 都可作正控制，但不能填入未知经典 RHS 当新输入。
568 的自由 local jet、569 的 matched cocycle、573 的 actual relative pair 已有合法对象；
它们分别尚缺 global effective source family、positive curvature/capacity 或 full-source 闭链，不能相加就算完成。

continuous 正反例在这里仍是必要的负控制：它们都可有 ODE Wronskian 1、自由 jet、formal graph／dual trace，
却不能都成为满足上述同对象 positivity budget 的几何 family。首门只要求候选指出**它到底在哪一条失败**，
不要求先假设所有 Weil Gram 正。一般 g-integer 的最大推广必然是带额外真实结构的子类，而非全部正分布。

## 6. 高维 Weil 猜想的范围

曲线上述几何证明不能等同于“所有高维标准 Hodge 正性均已证明”。
[Deligne, Weil I, §3 Thm 3.2 与 Lemmas 3.3–3.6，§§4–7](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)
实际使用 symplectic monodromy、rational local characteristic polynomials、even tensor 正系数和
cohomological pole control；Lefschetz-pencil 等再接到一般高维纯性。
单有 Euler 正系数或局部参数的纯性没有支付全球零点。
“所有 tensor 幂均正”若未构造对象及其 global pole budget，也只是把未付 purity 输入换一种语言。

## 7. 消费与停止

本稿首门实际付出的是 genus-2 普通／confluent／special 三种评价与 2Δ excess 的精确检查，
以及定位到相对 Picard 的原件章节。它是标准来源的具体准入测试，归来源0；
不新增实际 ζ positivity、独立平方容量、全 source 几何映射或 whole 4/5/core/coupling/Ξ 后果。
若当前候选只有已构造 relative pair/DGA 名称而没有上述新族/映射，本门即止，
不自动串下一个 paper、不调 genus/jet/minor 参数，也不抹掉合法 source-dependent/强拓扑/无限维修复。
