# 函数域同源设施的下一门：真实幂图与实际 torsion 线的廉价容量检验

2026-10-23。独占分支稿；不修改 STATE、不建合同、不计数学轮。
同 G20261014／0c4f 冻结基线，最新数学仍为578。本文仅消费既有资产的直接推论，
不重开已经停止的 Γ／twist／Pick、指数 clutch、flat primitive 或径向 Green 参数入口。

**结论：没有发现已可准入的新 physical-source→同对象 primitive RR 映射。**
可以完整写出的最便宜候选，是实际算术模型上的幂映射图及其规范主除子提升；
该 map 的 primitive 类恒零，既消405也杀537。另一个便宜检验表明，574的实际 unitary
二阶 absolute 线不可能由实双线性 absolute height 承担非零 Weil 值。
二者分别是既有 genus-zero／Picard 分类的具体直接推论，不应重计新数学进展。
它们保留真正 boundary-sensitive relative 容量、非平凡 Jacobian 型对象及有费无限传递等逃逸。

## 1. 恢复的最强输入与没有重复执行的门

本支读过 goals/README、STATE，执行 research_state check/show，并读567、574、575、
最新 Γ/twist 来源结算、573后路线图及 actual moving/DGA、source-dependent family、
adelic relative square 的已执行门。另核552、307和375中有直接影响的原范围。

* [567](../../../notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md)
  已付：曲线平方的真实截面、有效degree、乘法和 surface RR 给 Hodge 负号；
  全 Frobenius 图交重数再识别完整 Weil Gram。形式正交点、transpose、composition 和 trace 不够。
* [真实 moving 门](../../../goals/reviews/2026-10-22-function-field-evaluation-moving-source-gate.md)
  已付：genus2 上的 ordinary、thick-point、special、excess 区别。
  “找一个处处非零 raw minor”不是仍待执行的任务；相对 Picard、base change 和 chart 移动仍须来自同一几何。
* [574](../../../notes/574-actual-adelic-cover-relative-picard-and-source-transport.md)
  已给真实非平凡相对等变线及 absolute kernel；[575](../../../notes/575-regular-cartier-cover-flat-source-and-capacity-gap.md)
  已给真实 Cartier 理想与 nonflat normal 门。不能再以“尚无线或局部消失结构”开预算。
* [actual DGA 门](../../../goals/reviews/2026-10-22-actual-dga-line-moving-and-basechange-admission.md)
  已执行 free/graph/Koszul、标记、scalar base change。它们未给新的 Pic 移动或容量，已停止。
* [source-dependent 门](../../../goals/reviews/2026-10-22-source-dependent-divisor-families-and-relative-sections.md)
  已给完整谱商上的实际 marked section，以及不经谱商但失败全部 principal 平移的 metric/probe 族。
  不能重用“未知 map”的名字当新候选。
* [relative square 门](../../../goals/reviews/2026-10-22-adelic-restriction-relative-square-and-quadratic-capacity.md)
  已给原源 DGA、Pan 同伦、真实 site 复合及 P¹_Z 的真实 n² 小截面容量。
  “算术一维完全没有二次容量”已经不成立；缺的是同源 primitive 系数比较。

强旧实际ζ后果仍为542＋555→557的 whole leading4/5负惯性上预算，非负谱 lower。
下面两项不改善这个后果，不支付577的实际补偿 q_R，也不改变 core/coupling/Ξ 责任。

## 2. 可写出的非谱算术候选：P¹_Z 的真实幂映射图

取实际整模型

\[
 \mathfrak S=\mathbf P^1_{\mathbf Z}\times_{\mathbf Z}\mathbf P^1_{\mathbf Z}.
\]

它相对 Z 为曲面，总 Krull 维数为3；**不能把它叫算术曲面**。
generic fibre S=P¹_Q×P¹_Q 则是普通曲面。对整数 n≥1 取真实 morphism

\[
 [X:Z]\longmapsto[X^n:Z^n],\qquad
 \Gamma_n:\;YZ^n-WX^n=0.
\]

Γ_n 是实际有效 Cartier 图，且在每个 p 上给同一个方程的 base change。
当 n=p^k 时，其 p-fibre 正是 P¹_Fp 的第 k 次绝对 Frobenius 图；
不可分性及局部交重数没有被用“形式对应”替代。
因此这个候选确有真实 finite-place 算术、局部方程和乘法；它比自由标签强，
但接下来的 primitive 检验立即终止它作为全目标源载体的用途。

令 F₁={y=∞}、F₂={x=∞}，与567的约定一致，则

\[
 \Gamma_n F_1=n,\qquad \Gamma_n F_2=1,\qquad
 D_n=\Gamma_n-F_1-nF_2.
\]

在整个整模型上有显式函数级见证

\[
 \boxed{D_n=\operatorname{div}(y-x^n).} \tag{1}
\]

分子 YZ^n−WX^n 与分母 WZ^n 给出所列全部水平除子；分子 primitive，
没有任何整个 p-fibre 成为额外除子分量。某个 special fibre 上图的不可分性不改变(1)。
transpose 图有同样结论。于是这些 primitive 图在 Pic 和数值商中全部为零；
这也是 relative-square 旧门所指出 genus-zero primitive 空间为0的具体函数级实现。

若取 arithmetic principal pair，必须把有限除子与同一函数的 arch logarithmic Green 项一起取：
依所选规范写为 \(\widehat{\operatorname{div}}(y-x^n)\)，其 arithmetic class 仍为零。
本文不固定一套未使用的 dd^c／log² 归一化，也不将 Green 分量单独说成零。
若另给非principal metric，所得差可以非零；那是新的 arch 数据，并不由(1)自动得到。

### 2.1 一个不读取零点、原域可判的实际 source map

固定有限 N，取节点0、±log2、…、±logN在整条实线的 Voronoi cells V_ν；
两个外侧 cell 可以无界。正节点配 Γ_n，负节点配其 transpose，0配 Δ=Γ₁。
对全部实物理源 r∈S_exp 定义

\[
 a_\nu(r)=\int_{V_\nu}r(u)\,du,
 \qquad \mathcal D_N(r)=\sum_\nu a_\nu(r)D_\nu. \tag{2}
\]

这是实际有限 Cartier cycles 的实系数线性组合；复源采用复化，
不宣称任意复权本身是一个整数 Cartier 除子。
规范 arithmetic principal pair 的相同有限和也定义。由(1)，无条件

\[
 [\mathcal D_N(r)]=0 \quad\text{对每个 }r\in S_{\exp}. \tag{3}
\]

故全部405主关系确被消去，但537的实际双pole矩为零非根 r₀ 也被消去，
而 Qζ(r₀)>0。不是缺一个 positivity 证明，而是这个 class-valued map 已经失败覆盖。
保留原始函数或 marked cycle 可以保源，却改变了 target；此时必须另给对这些标记的
principal 不变配对及容量，不能从(3)抽出它。

### 2.2 原 du／Dlog 费用的准确范围

先固定 supp r⊂[-L,L]，记 J_ν=V_ν∩[-L,L]。由于 cells 两两不交，(2)的系数域有

\[
 \sum_\nu|a_\nu(r)|\le\|r\|_1
 \le\sqrt{2L}\|r\|_{du}
 \le\sqrt{2L/\log2}\|r\|_{D\log}. \tag{4}
\]

每个系数在这个固定窗的 du dual squared norm 为 |J_ν|。
对全 S_exp 则只报 ||a(r)||₁≤||r||₁的强源费用；无界外侧 cell 没有全线 du dual bound。
这只是 **实际系数 map 的费用**；
不是 Green 代表、算术高度或所有局部读出的共同 operator norm。
primitive class map 恒零，其商范数当然也零，不能以这个零费用冒充非根运输。
若用 n 加权的 raw 图degree，有限 N 有粗 upper N√(2L)||r||₂；
这不是必要费用，更不是 full Γ 的 logarithmic 原 Dlog 费用。

原始 Green 函数有图上的对数奇性；仅由(4)不能报 smooth vertical Dirichlet energy 或 uniform sup 上界。
all n 的无限和也不再是一个普通有限 Cartier cycle，须另核完成、尾费、乘法及源域。
本文只用有限模型判定(3)，不以任何无限交换极限制造新的 no-go。

## 3. 函数域与连续双符号控制：候选为何不能承载目标

### 真函数域

在 P¹/Fp 上，同一 n=p^k 图就是实际 Frobenius；(1)在函数域 base change 后仍成立。
这与 H¹(P¹)=0 完全吻合：保 H⁰/H² 全部周期 pole/aliases 后，其 primitive Weil源为0。
因此该候选在 genus-zero 正控制上正确，却不能因此承载经典537的非零 primitive 方向。

正亏格曲线额外拥有非平凡 Jacobian 与 same-object 极化。
[307](../../../notes/307-odd-polarization-and-elliptic-degree-benchmark.md)的真实椭圆模型已经展示：
非零同态的正次数、次数二次律、所有扩域可分核计数先给正号，再给纯性。
不能把 P¹ 的图存在或 arithmetic n² 小截面容量当成这份输入。
本文没有构造新的正亏格算术对象，也没有把307的已知正号重算成新输入。

### 连续正反模型

在562/574的真实连续系统中，固定 d=±1/16，各自保 native Γ=0、双pole及完整 Π。
取非零非负偶 φ∈C_c^∞((-1,1))，g=uφ，r=(D²−1/4)g。则双pole矩为零，而

\[
 Q_d(r)=2d(d+\tfrac14)^2 B_g^2,
 \qquad B_g>0, \tag{5}
\]

这里沿574的 \(e^{uw}\)、\(w^2=-d\) 规范，\(a_g=\int g(u)e^{uw}du=B_gw\)，明确有

\[
 B_g=\begin{cases}
 2\displaystyle\int_0^1 u\phi(u)\frac{\sin(\sqrt d\,u)}{\sqrt d}\,du,&d>0,\\[3pt]
 2\displaystyle\int_0^1 u\phi(u)\frac{\sinh(\sqrt{-d}\,u)}{\sqrt{-d}}\,du,&d<0.
 \end{cases}
\]

分部积分给 \(a_r=-(d+1/4)a_g\)；再用 \(Q_d(A+Bw)=2|A|^2+2d|B|^2\) 得(5)，
故上述定义没有额外的2因子。

两号都非零且异号。把相同物理源送入(2)的外加幂图模型，class 在两号都为0。
它既不能恢复正例的非零值，也不能识别负例的负号；问题是比较 identity 失败，
不是一个已付 identity 被负例反驳。
这些连续 g 系统并未被声称天然带有经典 adeles 或这个算术模型；这里只检验通用附加模型能否保持目标。

## 4. 574实际 unitary 线的 absolute height 首测

这项直接检验使用已经构造的真实覆盖，不引入另一 unknown map。
记 L=log2、M=log3，574的线由 e^(zx) 拼接，absolute kernel 为

\[
 i\Lambda=i\big((2\pi/L)\mathbf Z+(2\pi/M)\mathbf Z\big).
\]

取 z₀=iπ/L，则 𝓛_z₀ 是非平凡 absolute 二阶类。
两side框架范数均为1给其 Γ不变 unitary metric；
平方 transition e^(2πix/L) 可用 p-side 的周期 unitary gauge 平凡化。
所以在**absolute unitary-isomorphism class**上确有

\[
 2[\mathscr L_{z_0}]=0. \tag{6}
\]

因此任何以 tensor 为加法、消去 isometrically trivial 类的实双线性 pairing b 都满足

\[
 b([\mathscr L_{z_0}],A)=0\quad\text{对每个 }A. \tag{7}
\]

这是 bilinearity 与 R 无2-torsion 的直接结论，不需要未知 arithmetic Hodge 定理。
相应的 quadratic height 若由这种 pairing 极化，也在这个类上为0。

574的合法反控制 z(r)=ic Qζ(r)，选择 c=π/[LQζ(r₀)]，恰把537非根送入此线。
所以这个 Q-marker 的 absolute line class 与正纤维 metric，不可能再由上述双线性 absolute height
恢复 Qζ(r₀)>0。此处不是对所有 source map 的否定；只是将574旧包装的容量障碍说成一个可判等式。

**relative 两frame情况必须分开。** 574的 framed kernel 为0，平方所需 gauge 在边界不是1，
故该 relative 类不是二阶；(6)–(7)不能用于它。
真正 boundary-sensitive regulator、det-line cocycle 或相对 height 仍可有值，
但其同源有效性、局部过滤、primitive RR 和完整 Γ/prime-power/pole 比较都必须另外构造。
本文没有把 absolute 的零结论偷运到 relative target。

## 5. 为什么经典完整 Γ 仍是新增输入的责任

几何primitive图为 principal 后，若刻意只留下 arch metric 来保存源，
就不能继续消费“同一 principal pair 为零”。必须先写出新的全位 source map。
[552](../../../notes/552-radial-adelic-green-principal-and-comparison-gate.md)已经实际核过一种合法 radial adelic metric：
它在405非零主关系 p 上有严格非零 energy，且 fixed-window 高频阶为 t²，
而完整经典 Γ 为 log|t|。该特定 map 已停，不再调 smoothing 或 scalar。
新的 graph metric 并不被552一概排除，但本文没有给出这样一项新的 metric/finite-place 配合公式。

完整目标仍是同一 physical r 的全部复源二次型

\[
\begin{aligned}
 Q_\zeta(r)={}&2\Re(\mu_+(r)\overline{\mu_-(r)})
  +[\psi(1/4)-\log\pi]\|r\|_2^2\\
 &+\frac12\int_0^\infty
       \frac{2e^{-v/2}}{1-e^{-2v}}\|\tau_vr-r\|_2^2\,dv\\
 &-2\sum_{p,k\ge1}(\log p)p^{-k/2}
       \Re(r*r^*)(k\log p).
\end{aligned} \tag{8}
\]

其中 full FP/contact、所有 proper powers、双pole、全405非compact关系及537非根均是共同责任。
有限幂图真实存在不表明它的局部消失阶等于(8)的全部素数幂预算；
properness、有效性或某个全局 n² 截面数也不自动将 arch 二次系数变为(8)。

## 6. 本支准入判断与停点

本支没有找到不同于旧 completed quotient 或外加 probe/metric 的新非退化算术 source map。
上述两项检验可以立刻拒绝两个廉价候选，但均属旧资产直接具体化，**不能以此另建 C042/579**。
P¹ 幂图已在此停于 primitive coverage=0；574二阶线检验只停 absolute height 的该用法，
不续 graph degree、jet阶、谱点、clutch参数或另一个未给公式的 source 标签。

会真正改变这个判断的最小实物是：

1. 同一非谱算术/relative对象上，实际写出 source map及全部 Pan 的 principal/exact 变换，
   同时给537 primitive 非零值；不以完整 Q 或零点坐标作标签。
2. 该 map 的原 du/Dlog fixed-window费用和实际 growth/strong-source tail，
   以及同一对象的局部消失过滤或可检验的 mixed 容量系数。
3. 至少一个当前负控制在明确、先于目标正号的输入处失败，而不是定义“几何对象”时直接要求 Q≥0。

这些是准入数据，不是假设已成立的完整充分包，更不是新的未知 map 合同。
若没有其中的具体公式，本支不建议自动串下一来源论文；维持一次来源定位后止。

与577的量词比较：本支没有得到 q_R 的 fixed-source费、D′消失或 growing-window统一控制中的任何新项。
577的特定 family 上补偿消失仍有 RH 等价责任；任何未来独立证明当然可以使用旧等价接口，
但(1)、(6)或“存在正 height”本身不构成它。
宏观独立正性／容量、whole4/5上预算／core／coupling／Ξ瓶颈没有改变。
