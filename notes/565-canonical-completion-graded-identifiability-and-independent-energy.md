# 565. 选定完成化以后：分次识别、独立能量与纯性的剩余责任

2026-10-20，C028；固定G20261014／0c4f≤538。用户续问能否由g-integer分布与对偶，
非循环恢复自然完成化／分次权并推出正极化。结论分三步：
**限制可允许的局部因子，可以无RH选定完成化；单一未分次分布仍未给出唯一分次实现；
正极化需要额外、同源且可核的能量身份。** 第一步在经典对象已知，不能代替第三步。

## 1. 哪些数据实际已由分布决定

正primitive P给Π=Σ k⁻¹(T_k)_*P及M=exp_*Π，在收敛右半平面定义Z(s)。
在已指定全域延拓存在时，解析延拓唯一；此处没有重新选择裸Z的自由。
但Hilberdink–Lapidus的Ψ=GZ另包含核G。564在同一普通整数分布上给出
positive self-Fourier gB，满足全部theta对偶和同一极点位置，却得到B(s)ξ(s)的额外离线根。
除以B(0)可同时固定核的pointvalue／mass与两个pole residues，依然排不掉B的根。
所以bare P、宽Mellin对偶、归一化不足以唯一指定completed divisor；这是564旧资产。

本次不再要求抽象“自然”二字，而检验两类可独立核验的额外条件。

## 2. 标准Gamma类中，完成化唯一性本来可以非循环证明

限制允许的archimedean因子为

\[
 \gamma(s)=C Q^s\prod_{j=1}^r\Gamma(\lambda_js+\mu_j),
 \quad Q>0,\quad\lambda_j>0,\quad\Re\mu_j\ge0.       \tag{1}
\]

设同一非零亚纯F的两个这种完成化，都满足同一中心1/2的共轭函数方程。
则两因子相差常数，指定一次归一化后唯一。这是
[Conrey–Ghosh，Theorem2.1／§2，原PDF pp5–6](https://arxiv.org/pdf/math/9204217)
的来源恢复，不是本次新定理。其证明只用这一步的Gamma形状与FE，不用RH、Euler或整数系数。

关键逻辑值得保留：R=γ1/γ2在Re s>0全纯零自由；FE把它反射到Re s<1，
两半面覆盖C，故R全平面entire且零自由。这是**两个核因子的比**，没有假设F或ξ无零。
1/γ1、1/γ2均是阶≤1 entire且有相同零除子，Hadamard给R=exp(a+bs)。
共轭FE只先给b纯虚，不能直接删掉；标准Gamma的Stirling上下竖直渐近再迫b=0。
若是实型linear自对偶，则R(s)=R(1-s)直接杀掉斜率。

中心与半面重叠有实质作用，不能直接改成任意中心：例如F=1/Γ(s)，
γ1=Γ(s)、γ2=Γ(s+1)给完成化1与s，各自关于s↦−s满足root number不同的FE，
却有非恒定ratio s。一般中心须另外支付零自由半面在反射后严格重叠的前件。

因此564的BG0不能属于同一标准admissible Gamma类：它在Re>0已有B的零，
而(1)在那里无零无极点。这里筛的是可显式识别的核，不是未知ζ零点位置。
Gamma duplication会改变参数写法；唯一的是因子函数到常数，不是每一串参数。
在仅有有限极点的场合，归一化pole-clearing多项式须取实际极点的最小除子；
函数域的周期极点另用其已给有限T=q⁻ˢ有理式处理。任意额外entire乘子不能叫“清极点”。

此结果有两条边界。第一，任意Beurling系统未必存在(1)类的完成化；
唯一性定理不生产membership或positive arithmetic dual。第二，两个不同对象的linear pair
γ1F1(s)=γ2F2(w-s)仍允许γ1乘e^{a+bs}、γ2乘e^{a+bw-bs}，即互补尺度自由；
须由已给local measure／conductor或两个非互补校准值固定，不能照搬单对象共轭唯一性。

## 3. 一个物理侧选择：固定局部二次能量的唯一基态

不预设Gamma乘积，也可先给加法R的Euclidean局部背景和Fourier pairing。
在V=H¹(R)∩{xg∈L²(dx)}，定义

\[
 \mathcal E(g)=\|g'\|_2^2+4\pi^2\|xg\|_2^2,
 \qquad
 \mathcal E(g)-2\pi\|g\|_2^2=\|g'+2\pi xg\|_2^2.     \tag{2}
\]

在Cc∞分部积分，随后按V图范数密度闭包，(2)对全部complex V成立。
等号是一阶D′方程，且仅有g=C exp(−πx²)。正核以g(0)=1归一，便唯一选出g0及G0。
这使用标准harmonic oscillator事实；本次固定检验是它是否真正拒绝564的正核gauge。
取A=2^{1/4}，对实际gB算出

\[
 (\partial+2\pi x)g_B
 =2\pi Ax[-3e^{-4\pi x^2}+(3/8)e^{-\pi x^2/4}],
 \quad
 \mathcal E(g_B)-2\pi\|g_B\|^2
 =\pi\left(\frac94-\frac{36\sqrt2}{17\sqrt{17}}\right)>0. \tag{3}
\]

严格符号归结为4913>512；归一gB/B(0)仍严格正。
所以这个检验可以独立排除B，甚至不必先求B的根。完整域证明与积分在
[root原稿](../reviews/2026-10-20/grh-canonical/gaussian-ground-state-selector.md)。

代价也很明确：local quadratic metric、Fourier pairing及基态选择是额外输入，
不由bare g-integer计数或宽Mellin对偶自动出现。它只选择核；其平方不是完整Weil型的平方。
它不要求所有广义RH系统必须是一维Gaussian，也不排函数域／连续正谱模型。

## 4. 单一ζ／Euler数据看不到什么

完整Z及其对偶最多先给未分次的除子或虚谱；一般不能唯一恢复cohomological grading、
原实现的Jordan结构或正内积。两类非识别测试不能混在一起：

- 相邻奇偶次数各加同一Frobenius包，超行列式相消；再加互补次数的dual包，仍保成对对偶。
  所有点数超迹和Z均不变，分次维数与实现却改变。这是形式分次实现的反例，
  不宣称它仍是某个固定光滑射影几何的cohomology；几何正是额外限制。
- I与非平凡unipotent Jordan块J有同一det(I−TJ)及所有power traces，
  前者可酉而后者不能在任何正定内积下酉。det纯性并不决定原算子可正极化。

如果另给无奇偶消去的分解、几何维数、cohomological functor／Tate twist及精确det身份，
权就由这些结构预定；不能将未知根按实部分组后称“恢复权”。
还须区分：在已经证明的纯、无消去分次类中，可能反过来由谱识别权；
那不是在证明纯性之前从最一般分布无条件恢复权。

## 5. 独立能量条件如何真正推出纯性

设一个实际源递推／对应先构造有限维A_j，先验中心a_j与q>1已给，
并证明原ζ因子恰为det(I−q⁻ˢA_j)，含全部重数／符号及周期副本。
若从同一源构造显式H_j>0并核

\[
 A_j^*H_jA_j=q^{2a_j}H_j,                              \tag{4}
\]

则q⁻ᵃʲA_j酉，A_j半单且全部特征值模qᵃʲ，目标因子逐权纯。
本蕴含是001/002/563旧机制；新信息必须来自H及同源identity的独立构造。
若只提出“存在H>0满足(4)”，有限维中它等价于原A_j半单且pure，比det层RH还可能更强；
所以一句存在性公理没有消除原责任。

另一种可核证书是：给定源内积下，U=q⁻ᵃA及其inverse均contractive。
因||Uv||≤||v||≤||Uv||，即得unitarity；连续时间须真强连续group与skew-adjoint域，
不能仅核formal integration by parts。若双对象由perfect pairing联系，可用dual contraction
与已给positive识别代替inverse contraction；未知识别本身仍是未付输入。
普通Markov／detailed balance只给contraction或reversibility，允许模<1的谱；不强制pure。

更强的有限维条件“U及U⁻¹都是逐项非负的Markov矩阵”又太窄：非负逆迫每行支撑互不交，
行和1继而迫U为permutation。它的迹是整数，已排除真实F5证书的trace(U)=−3/√5。
因此不能将双向保正当作一般函数域／数域纯性的必要机制；这只排该有限Markov版本，
保无限维、允许killing的heat semigroup或一般unitary实现。

对连续ODE Zc，563给C=[[0,1],[-d,0]]、G=diag(d,1)，d=c−1/4。
G的正负直接由c判断，c≥1/4源Weil正型，c<1/4有负compact测试。
c=1/4可有半正定证书，商后丢失multiplicity，原companion非半单；
faithful二重根实现须另保trace重数。这展示正型、原实现极化、det身份的不同层级。

另一个明确可用的分析充分包是：**从源构造正稠密闭形式，且证明其全时间heat trace
恰为同一完整Weil分布的热量。** 若表示算子K≥0自伴、e⁻ᵗᴷ对每个t>0普通trace-class，
并由源独立证明Θ_W(t)=Tr(e⁻ᵗᴷ)，则

\[
 (-1)^n\Theta_W^{(n)}(t)=\operatorname{Tr}(K^n e^{-tK})\ge0
 \quad(n\ge0,t>0).                                  \tag{4a}
\]

λⁿe^{−tλ}≤C_{n,t}e^{−tλ/2}及较小时间trace-class支付逐阶微分；
在563规定的实偶／有限指数阶W域内，(4a)给全部complex compact Weil正性。
若完整显式公式和除子前件已付，就可经Weil判据推出RH；无需另先猜自伴谱等于零点。
要把K或其平方根进一步解释为faithful谱行列式时，才须另保零点重数与det身份。

这种包的真输入是具体闭形式及**从源证明heat-trace身份**。
仅说“存在K”或从未知零点反建K，仍只是等价包装。Gamma的局部heat kernel为正，
也不能独自支付此身份：经典Θ_W含有带负号的全部prime atoms和双pole。
标准正闭形式／Dirichlet接口及有限Markov边界详见
[权与独立能量原稿](../reviews/2026-10-20/grh-canonical/weights-and-independent-energy-audit.md)。

## 6. 连续分布、数域和函数域的检验结果

| 输入 | 完成化／权从何来 | 正性结果及限制 |
|---|---|---|
| Zc=1+c/[s(s−1)]，0<c≤1/2 | 规定Gamma=0，最小pole-clearing，pole中心1/2 | 同一positive P/Π/M、同FE，c≥1/4正而c<1/4负；光有规范和中心不足 |
| 普通整数＋gB | 宽核自由，即使mass／pole归一相同 | BG0被标准Gamma类或(2)基态selector排除；经典ξ不因此获得新正性 |
| Dedekind ζK | local R/C、signature、discriminant给标准Γ；共轭FE固定1/2 | 自然完成化已非RH可得，完整Weil正性仍待独立算术输入 |
| F5曲线y²=x³+x+1 | 已知曲线、cohomological次数0/1/2、q=5及有理性 | 精确N1=9给trace −3，显式H>0与全部递推身份给pure及全周期Weil平方和 |
| 290形式曲线型正Euler反例 | P(T)=1−5T+5T²，最小有理分子、同0/1/2标签与FE | 正闭点Euler、形式对偶仍不pure；相应H不正，不能冒称真实曲线 |

F5证书的关键有理计算可统一写为

\[
 A=\begin{pmatrix}0&-q\\1&t\end{pmatrix},\quad
 H=\begin{pmatrix}1&t/2\\t/2&q\end{pmatrix},\quad
 A^THA=qH,\quad\det H=q-t^2/4.                         \tag{5}
\]

q=5,t=−3时detH=11/4>0；反模型t=5时detH=−5/4。
这是从count／系数直接判符号的有限证书，不先读取根。
但对所有这类genus-one二次分子证明此H>0，就是strict Hasse界的责任；边界|t|=2√q时pure仍可能成立，
companion却有Jordan块，故不能以该strict证书排掉真实边界曲线。
数值count并未自行证明全部递推：F5的all-degree结论另用已知genus-one有理性／FE，
563原证书脚本及全周期lift作为输入，不重新计算成新普遍定理。

数域也有重要的正面辨识结果：若先知属于标准Gamma类，同一ζK的Gamma已经由§2唯一，
不能绝对声称ideal norm series“必定不能确定signature”。未知的是一般P的类membership，
以及即使完成化唯一后如何独立构造完整算术正极化。
函数域的既知权纯性来自更强的几何定理，不能把FE或det已pure倒用为原Frobenius半单的证明。

## 7. 净后果、经典缺口及停线

本次付清的固定检验是：局部二次energy selector严格拒绝同一正gauge；
标准Gamma唯一性提供另一个已知、无RH的规范方案；虚消/Jordan和能量正负对照
则界定了分布可识别性及证书的真正代价。这些不宣称新外部首创。

经典ζ已经有canonical Γ、pole清除、weight1及theta反演。缺少的是

\[
 \text{实际Gamma／全部prime powers／双pole}
 \ \longrightarrow\ \text{全complex compact源的独立正能量身份},
 \tag{6}
\]

并付原域／闭包与完整显式公式；若走谱行列式路线，再付完整trace重数与faithful Ξ。选择g0、完成化唯一、后验GNS、
热量all-order CM或未知H存在，都没有支付(6)。热CM和全Weil正型仍只是563等价字典。
原actualζ强旧542+555→557 whole leading4/5、560成长K/core/coupling未改，宏观门open。

本合同一次检验后停止增加规范／purity公理。下一数学准入须有具体同源能量或有控全源逼近，
可以先核独立、预定的非局部correspondence identity，再比较完整Weil源；
没有实际identity／新signed费用时，只保章节定位的来源审查，不再以未知H/CM命名续轮。
