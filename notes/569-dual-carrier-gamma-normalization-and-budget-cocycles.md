# 569. 双载体的Γ规范、奇偶过滤与预算cocycle

2026-10-20，C032；同G20261014、0c4f≤538基线。用户要求执行568留下的双对偶载体来源门，
并检验determinant line／局部cocycle。本文和三原稿统一一完整数学迭代；来源/逆审/同步不另计。

**结论：原双conormal的全部jet链，加共同flow character，并不恢复经典实Γ核。
加入额外的normal奇偶投影能精确恢复穿孔核；完整接触项则可由指定Tate/Fourier/Haar规范恢复。
预算片的matched cocycle也能明确构造，连全纯phase一起抵消。但这两项均未独立给RR容量或Weil正性。**

新增的是固定来源的精确运输判定、有界且变号的修复费用，以及真实compact关系上的协同构造。
不将旧563连续纯性、567曲线RR、568 signed载体或405的1/8再计为新正性。

## 1. 输入和来源范围

完整源先固定为实偶Hermitian分布W，B(r,s)=W(r*s*)，第一变量线性，s*(u)=overline{s(−u)}。
compact复源D=Cc∞是正性目标；405 Gaussian关系另在physical S_exp及其扩张商测试，
不能把非compact h放入D。一般非自对偶pair仍须另给预定权/完成化/左右配对，本文不替其选中心。

本轮实际核读[ALKL 2402.06671v2](https://arxiv.org/pdf/2402.06671v2)
§§1.3.6、2.5.29–30、5.8、6.1、6.7及指定显示式，未重审176页证明。
原文给conormal与density-dual两条序列、固定作用和b-supertrace；不是普通正迹。
[Burnol 9902080v1](https://arxiv.org/pdf/math/9902080v1)的实位/乘法分解及Fourier恒等式
提供另一个已有局部来源；两者尚未被识别为同一个算术几何载体。
Barner1981只定位到出版信息，正文未取得，不用其名支付原文有限部分疑点。

## 2. 双半轴共同权的门：先比较离开原点的核

原文§5.8 Prop5.8.1与§6.7 Prop6.7.1的normal阶k≥0分别有作用

\[
 e^{-(k+1)\kappa t},\qquad e^{k\kappa t}.                 \tag{1}
\]

一单位κ的差来自density transpose，不是自由参数。按各自收敛半轴组合，
单叶穿孔核为Kκ(t)=|e^(κt)−1|⁻¹，κ≠0；叶Euler系数/轨道符号来自实际几何，不能任取。
对v>0有Kκ(v)/Kκ(−v)=e^(−κv)。所以同一个实flow character e^(at)使其成为偶核，当且仅当

\[
 a=\kappa/2,\qquad
 H_\kappa(t)=e^{\kappa t/2}K_\kappa(t)
 =\frac1{2\sinh(|\kappa||t|/2)}.                         \tag{2}
\]

该character比较独立于未知ζ零点；只消费单叶、共同权、时间重标和常系数的这一个明确类。
经典ζ完整Γ分布离开原点的密度则为

\[
 -a(v),\qquad a(v)=\frac{e^{-v/2}}{1-e^{-2v}},\quad v=|t|>0. \tag{3}
\]

没有常数A与κ使AHκ=a：大v的指数与首系数迫|κ|=1、A=1，
小v时AHκ~1/v，而a~1/(2v)，矛盾。若先取|κ|=2以匹配小端系数，
得到b(v)=e^(−v)/(1−e^(−2v))，大端指数仍不同。任何cδ0均不能修改穿孔差。

这不排多叶、额外系数、奇偶sector或奇异/非局部几何，也不证明Γ无法几何实现。
对两个半轴独立选twist需要新的pairing及source，不能冒称由(1)自动得到。
2002 Kähler/Riemann正性与本篇preserved-leaf b-trace也没有免费共同载体。

### 2.1 合法有费修复：穿孔差不是不可控制

令D(u)=a(|u|)−b(|u|)，u≠0，连续延拓到0。直接展开并积分得

\[
 D(0)=1/4,\quad D(u)=1/4+|u|/16+O(u^2),\quad D\ge0,
 \qquad \|D\|_1=\psi(1/2)-\psi(1/4)=\pi/2+\log2=:M.      \tag{4}
\]

积分证明：y=2v把2∫(a−b)dv化为∫(e^(−y/4)−e^(−y/2))/(1−e^(−y))dy。
因此在同一个physical-log有限部分与相同接触反项下，两Γ型分布差恰为−D，
其全L²卷积operator norm等于M：|hatD|≤M且hatD(0)=M。fixed窗也有同一上界，
若转原Dlog须保||r||²_D≥log2 ||r||²_2，不漏norm费用。

但D的点态正不等于positive type：它在0附近反而上升。
更精确地，半轴分部积分给hatD(ξ)=−1/(8ξ²)+O(ξ⁻⁴)，而hatD(0)=M>0。
故这个有界修正本身变号，不能当有利正迹或无费预算。它是可用的解析修复，
原conormal几何没有因此自动产生这笔D源；没有证明所有允许修复失败。

### 2.2 奇偶过滤确能修复穿孔形状，但它是额外输入

取|κ|=1的半密度链，单半轴的全部normal rates为k+1/2。
若另有真实反射P，P在第k阶上作用(−1)^k、与flow/dual pairing兼容，则(1+P)/2选偶阶，

\[
 \sum_{m\ge0}e^{-(2m+1/2)v}
 =\frac{e^{-v/2}}{1-e^{-2v}}=a(v).                       \tag{5}
\]

两半轴使用同一sector时给正确偶核，而非手乘e^(−|t|/2)。
若无P，(5)只是一条清楚的条件构造；必须另给反射、sector乘数、Euler系数及其全局延伸。
它只匹配核形状，Γ负号和trace重数仍欠；三维可定向闭二维叶的χ=2−2g不能手取为−1。
原论文计算all k，未替一般g分布选择这一投影。裸g-prime的正测度/乘法对偶不提供normal parity。
这保留一个可精确描述的合法修复，没有把原单链不匹配升级为所有几何失败。

## 3. 有限部分、接触常数与已有局部Fourier来源

定义physical-log cutoff下的最小对数有限部分

\[
 T_a(h)=\lim_{\epsilon\downarrow0}
 \left\{\int_{|u|>\epsilon}a(|u|)h(u)du+h(0)\log\epsilon\right\}.
                                                               \tag{6}
\]

对任意h∈D，近0的偶化差O(v²)，大端指数可积。digamma积分给
∫ε∞2a(v)dv=−log(2ε)−γ−ψ(1/4)+o(1)，因此完整Γ分布精确为

\[
 A_\Gamma(h)=-T_a(h)-[\gamma+\log(2\pi)]h(0)
 =\Gamma_0h(0)+
 \int_0^\infty 2a(v)\left[h(0)-\frac{h(v)+h(-v)}2\right]dv,
 \quad\Gamma_0=\psi(1/4)-\log\pi.                        \tag{7}
\]

等价地AΓ=−T_a−[γ+log(2π)]δ0。该规范含563/568的完整Γ，非只高频log或穿孔核。
用aα(v)=e^(−2αv)/(1−e^(−2v))、Γα0=ψ(α)−logπ时，(7)相同δ反项适用所有α>0，
故α=1/4与1/2的比较确为(4)的−D，不藏未付δ。

在只减零阶Taylor项的最小对数FP类中，换cutoff的差为cδ0；
不限制延拓阶时，不能声称任意point-supported ambiguity都只有δ。
模型稿式(13)–(15)给所有有限cutoff的精确相对变换，其cocycle不选择绝对Γ0。

原文intro印刷p7的显示式在普通积分意义下有无穷端1/t减项问题，
对非偶Kκ还不能将正负测试放入同一个正时间分母。已用PDF技能视觉核原版，非OCR猜测。
这仅限制该显示式的消费，不否定正文trace定理。Barner正文未核，不能声称它已修复该处。
正文§2.5.29的b-integral明确依赖boundary defining data；这种依赖并不自动给算术接触常数。

实际已有的非循环锚点是实局部域及其加法Fourier结构。
指定字符exp(−2πixy)、自对偶Haar与trivial sign sector后，Tate/Burnol的局部Gamma phase具有

\[
 \gamma_+(s)=\pi^{1/2-s}\frac{\Gamma(s/2)}{\Gamma((1-s)/2)},\quad
 \left.\frac{d}{ds}\log\gamma_+(s)\right|_{s=1/2+i\xi}
 =\Re\psi(1/4+i\xi/2)-\log\pi.                         \tag{8}
\]

Fourier约定换相位时须同步反转相应约定；这里固定(8)。
它精确恢复(7)的乘子，而不预设RH；odd sign sector给3/4，说明parity确有实际局部来源。
Burnol conductor operator log|x|+Flog|x|F⁻¹在指定域实现该乘子，
但Γ0本来可负，不是完整Weil正性的正算子证明。
这条局部设施已有文献来源，不是本轮新的RH输入；一般g分布也不自动携带R及加法角色。

## 4. b-renormalization确有局部变换律，尚未识别为算术预算

对边界x≥0、b-density u=a(x,y)dx/x dy，以
FP_x(u)=limε[∫_(x>ε)u+logε∫a(0,y)dy]定义有限部分。
若x'=e^(ω(y))x+O(x²)，直接移动小下限得

\[
 FP_{x'}(u)-FP_x(u)=\int_{\partial M}\omega\,\operatorname{Res}u. \tag{9}
\]

这是坐标规范明确的方向；不把它与法向trivialization aν的反向缩放混淆。
原件§2.5.29相关ν公式的记号方向在源稿保留为未解决消费风险，不拿它代(9)的证明。
对本篇定义类中的smoothing b-operators，§2.5.30式(2.5.65)另给

\[
 {}^b\!\operatorname{Tr}[A,B]
 =-\frac1{2\pi i}\int_{\mathbb R}
 \operatorname{Tr}\{\partial_\lambda I(A,\lambda)I(B,\lambda)\}\,d\lambda.
                                                               \tag{10}
\]

这是真实独立的边界trace-defect设施，(9)和它给local anomaly的候选来源。
本轮不重证b-calculus整章，也不将其延到所有unbounded operator。
必须另给同一算术indicial families、全轨道powers及pole/cohomology比较，
才能说(10)就是所需Weil预算的cocycle。b-trace不消commutator，也不能当正普通trace。

## 5. 完整预算的matched cocycle可以明确实现

设复局部凸A上有连续Hermitian各片b_j，符号吸入各片，b=Σb_j、Q=Σq_j。
令R=rad b，不能只取Q(h)=0的isotropic向量。对箭头r→r+h、h∈R定义

\[
 c_j(r,h)=q_j(r+h)-q_j(r)=2\Re b_j(r,h)+q_j(h).
 \quad c_j(r,h+k)=c_j(r,h)+c_j(r+h,k),\quad\sum_jc_j=0.   \tag{11}
\]

取线L_j=A×C，metric e^(−q_j(r))|z|²和transport z→e^(c_j/2)z，
就是严格的Hermitian isometry作用；各c_j是显式coboundary。
总tensor metric为e^(−Q)，总transport=1，故完整预算代表无关。
它对不定Q同样存在，纤维范数为正不表示Q≥0。

若固定有限维复切片并要求transport全纯，取

\[
 g_{j,h}(r)=e^{b_j(r,h)+q_j(h)/2},\qquad
 g_{j,k}(r+h)g_{j,h}(r)=e^{i\Im b_j(h,k)}g_{j,h+k}(r).    \tag{12}
\]

单片一般只是projective作用；中心2-cocycle的tensor乘积仍为1，连phase都抵消。
不能把单片实transport称为全纯，或把任意指数metric命名为cohomology determinant。
总线的固定holomorphic frame metric e^(−Q)在每个复直线上的Chern曲率系数恰Q(v)。
要求这条线半正曲率因此仍等价完整Weil正性，不是新容量定理。

### 5.1 连续正反例：真实compact关系也通过

在旧完整族Z_c=1+c/[s(s−1)]、d=c−1/4中，W''+dW=0。
对任意非零φ∈D，k=(∂²+d)φ是真实非零compact关系，B_W(k,r)=0对全部r成立。
pole矩M±(k)=cM±(φ)，故P(k)=c²P(φ)，全部prime-power片R(k)=P(k)，没有删项。
实偶φ可归一化到M±(k)=1/4，得到P(k)=R(k)=1/8。
这在d=±1/16、0全部成立，而且任意complex r的mixed变换(11)准确匹配。
关系k与ik给单片phase e^(−i/8)，完整tensor相消。

另一构造用C_d、S_d、e±u/2在任意开窗线性独立的四矩Gram，直接造相同compact关系。
因此本轮协同修复不是人为添一个形式根方向；它确实作用于原positive primitive/fullΠ模型。
这些模型Γ=0、源原点光滑，不应强加经典Γ或preserved leaves为类RH必要条件。
负段也通过全部协同检验，原563符号阈值不重计；仅改contact可被非零k立即检测，仍不筛纯性。

### 5.2 函数域：全周期pole、正确总权与cocycle仍不足

q=5、L=logq、g=1，真曲线trace t=−3，290反模型t=5。
全递推S0=2,S1=t,S_(n+2)=tS_(n+1)−qS_n给a_n=q^(−n/2)S_n并偶延拓。
完整源和完整pole均为log-comb：

\[
 W=L\sum_{n\in Z}a_n\delta_{nL},\quad
 P=L\sum_{n\in Z}(q^{n/2}+q^{-n/2})\delta_{nL},\quad R=P-W.
                                                               \tag{13}
\]

R的非零格点系数q^(−|n|/2)N_|n|包含全部powers；原点为2−2g=0，W0=P0=2。
定义T_Lr(u)=r(u−L)、p(z)=z²−(t/√q)z+1，则k=p(T_L)φ为compact完整根关系。
以y∈[0,L)的periodized M±(r;y)=Σ_j q^(±j/2)r(y+jL)计算全部aliases，得

\[
 P(k)=p(\sqrt q)p(q^{-1/2})P(\phi)=\frac{N_1^2}{q}P(\phi)=R(k).
                                                               \tag{14}
\]

真/反例倍率分别81/5、1/5，两边都可归一化为1/8；不能以单个cosh pole矩冒充(13)。
同源矩阵A_t=[[0,−q],[1,t]]同时满足det A=q及AᵀJA=qJ；归一化top determinant均1。
它们的源trace form H_t=[[2,t],[t,2q]]却分别有det11、−5。
因此正确权、determinant line总权、symplectic对偶与matched cocycle一起仍不提供primitive正号。
这不重证567的失正反例，而是检验新设施在原反例上是否有额外区分力：没有。

真实曲线另给0→O(D−E)→O(D)→O(D)|E→0、真实kernel H0(D−E)、RR和平方几何。
它的determinant cohomology确能协调principal changes；自由局部jet与二次型指数线没有这些输入。

## 6. 真正determinant容量与等价改写的分界

若实际给定有限评价E:S→J，两项复形[S→J]的行列式线才是
det J⊗(det S)⁻¹≅det coker E⊗(det ker E)⁻¹。
平衡维数时det E是规范截面；线存在不保证截面非零，更不保证目标Weil Gram正。
已有独立正metric时，按列坐标q(x)=x*Hx定义H（第一变量线性时H_ij=b(s_j,s_i)），
||det E||²=|det[E]|² detH_J/detH_S，换基协同抵消。
这些有限事实见[Stacks 0FJ9](https://stacks.math.columbia.edu/tag/0FJ9)、
[0FJI](https://stacks.math.columbia.edu/tag/0FJI)，不从名字引入未知经典perfect complex或Quillen定理。

仍需独立输入：

1. 同一global source的乘法、restriction/kernel、局部消失过滤与principal映射；
2. 同一非零det截面的全位结构，局部order/碰撞下界及匹配的Γ/contact规范；
3. 从实际source证明的RR/height/容量上界；不能由Q反定义容量；
4. 同一scale下预算差趋完整Q的all-complex身份，含全部powers、周期/双pole及误差/覆盖。

本轮(5)/(7)/(9)–(12)没有支付这些容量。要求e^(−Q)曲率半正、要求所有评价Gram PSD，
或将未知Weil Gram先当正metric再作determinant，均为等价/循环组织。
反之，Tate实局部域数据、真实曲线RR、独立boundary indicial family是可识别的额外输入；
它们各自承担的箭头必须保留，不能从一项局部Γ身份跳到全球正性。

## 7. 净后果与停止

已闭合：指定双conormal单链的两侧共同权门；明确parity合法修复与其额外结构；
同log FP的完整Γ校准及有界变号差；预算片的实/全纯cocycle；连续与全周期函数域关系检验。
来源风险按原件范围保留，未将b-trace认成普通正迹。旧405/563/567/568资产均扣除。

没有经典独立global容量，没有完整Weil正性，也没有最强旧542+555→557 whole leading4/5的改善。
560的成长K/sign/core/coupling及通常Ξ仍未付，宏观瓶颈没有改变。
C032一轮后停止调κ/sector/contact或构造未知detline；不再用新来源名延长同一缺口。
下一动作回到560 actualreceiver的joint signed责任，先固定实际算子/输入像及全源比较，
检查是否存在一个可改变强旧结论的具体mixed门；没有实际input则保存未准入，不能预建新数学合同。
若取得真实global evaluation complex＋独立容量，或同实际receiver的有利signed新估计，才改变选择。

三原稿：[源核查](../reviews/2026-10-20/dual-gamma-cocycle/dual-conormal-source-audit.md)、
[cocycle](../reviews/2026-10-20/dual-gamma-cocycle/budget-cocycle-and-determinant-line.md)、
[模型](../reviews/2026-10-20/dual-gamma-cocycle/continuous-function-field-tests.md)。
有限/符号记录只核已证式，不替代全源证明；最终消费见本目录独立审阅及root收据。
