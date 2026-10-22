# 实际覆盖上非 Q 物理源桥：primitive、双 lift 与 regular 费用门

2026-10-22；独占分支原件，等待 root／独立复核。只写本文件，不创建合同、不结算轮数。
输入是574的实际覆盖、405完整解析关系、537非根与553原范数范围；不把它们改称已知几何 principal。

## 1. 冻结对象和实际测试

固定两位2、3，沿574记侧商为 Z_L、Z_M，L=log2、M=log3，共同 bulk 坐标 x。
每个侧商有嵌入

\[
x\longmapsto(\rho,\vartheta)=(e^x,e^{2\pi ix/L}),\qquad
\partial Z_L=\{0\}\times S^1.
\]

两片作用各 proper，全覆盖作用不 proper。以下函数在实际侧商上下降／延拓，绝不把整个非proper商当Hausdorff曲线。
“光滑侧层”在本稿仅指从 [0,∞)×S¹ 的光滑函数限制到上述螺旋加边界的函数层；这是可明确构造的一种候选，并非已经由adele对象唯一选出的算术结构层。

物理输入是 r=Cf=e^{u/2}f，f∈S_exp,C。关系是全部 P_c=C(P_an)，不是 P_c∩Cc∞。
405中 I 是实际径向E像的 Fréchet 闭包，P_an=I∩ker c∩ker d；这个定义不提供从任意 r 到 adelic η 的逆 lift。
519／520的完整像识别可作为旧输入使用，但不把其谱／商同构重新标成独立 regular-unit 构造。
具体双测试固定为

\[
P=(D^2-\tfrac14)H\in P_c,\quad H=e^{u/2}E\eta_h>0,
\qquad r_0=(D^2-\tfrac14)\psi,
\]

其中0≠ψ≥0紧支于537的17/16窗。两者均 μ±=0；537给Qζ(r₀)>0，而完整405给P是Qζ根关系。
完整关系还有所有合法平移、复标量及 Fréchet 闭包。

本分支实际执行的三个非Q候选是：对物理源积分作真实侧延拓；用actual E／Fourier双lift对两边界正规化；用侧圆periodization读出交叠。
这些均不是预先读出零点位置。它们也均没有生成所需的新 source→Cartier／capacity 箭头。

## 2. primitive 源桥：真实公式，但全部源都是 relative gauge

定义

\[
A_r(x)=\int_{-\infty}^{x}r(u)\,du,\qquad
a_r(\rho)=A_r(\log\rho),\qquad g_r(x)=e^{A_r(x)}.             \tag{1}
\]

对每个 r∈S_exp，a_r 在ρ=0延拓为0，且是C∞-flat。证明不是只用compact源：任取N>0，x≤0，

\[
|A_r(x)|\le N^{-1}p_{N,0}(r)e^{Nx};\qquad
\partial_\rho^k a_r=\rho^{-k}D(D-1)\cdots(D-k+1)A_r(\log\rho).
\]

k≥1时，右边是ρ^{-k}乘r的至多k−1阶x导数的固定线性组合。因此

\[
|\partial_\rho^k a_r(\rho)|\le C_k\!\sum_{j\le k-1}p_{N,j}(r)\rho^{N-k}
\quad(0<\rho\le1),                                      \tag{2}
\]

N可任取。指数g_r与其逆也光滑延拓，边界值均为1；g_r−1同样flat。
将g_r放在任一侧，另侧取1，便是实际side regular units之比，而且保两端既定boundary frames。
故由g_r拼接的线对**全部S_exp物理源**均相对平凡。405的P消去，但537的r₀也消失。

这是比“所有compact源负端恒1”更完整的全域检查。没有将compact上的空principal条件冒充全405。
任何只在bulk先作固定 S_exp-preserving smoothing，再按(1)积分的版本都得到同一结论；局部线类没有留下新的信息。
保留(g_r,所选frame)作为额外mark当然能记录raw源，但其信息来自被特意保留的自由frame，不来自新的Picard／Cartier类。

### 2.1 ρ-adic 局部过滤看不到这些源

在这个光滑侧层中可写 I=(ρ)，但

\[
a_r,\ g_r-1\in\bigcap_{n\ge1}I^n.
\]

每次除以ρⁿ仍由(2)光滑延拓。对非零源这些函数不必为零，所以这个消失过滤不分离；它不是DVR的离散valuation。
此外，Iⁿ/Iⁿ⁺¹至少仍含整个边界圆上的光滑系数空间，未自动产生有限维评价空间或有限整格。
不能把“任意高阶消失”直接解释为获得任意大的有限位整除预算：这种非分离过滤缺少函数域局部环的Krull／valuation设施。
对g_r本身则更简单：它是side unit，Cartier消失阶始终0；若改记录g_r−1，得到的又是上述flat现象。

## 3. 原 du／Dlog 费用：C0可付，normal jets 另欠

若实际源支撑于[−A,A]，有

\[
\|A_r\|_\infty\le\sqrt{2A}\,\|r\|_{du}
\le\sqrt{2A/\log2}\,\|r\|_{D\log}.                      \tag{3}
\]

第一常数作为Cc∞到C0的operator norm是sharp supremum；以光滑近常数源逼近端点。第二常数只是旧Dlog≥(log2)du给出的upper。
由此g_r和g_r^{-1}的所选representative C0费用均不超过 exp(√(2A)||r||du)。
没有固定支撑时，(1)的C0读出对全线du／Dlog无统一常数；长窗近常数源已给√A增长。

下列normal微分先固定所选θ-independent radial extension；bulk处ambient ∂ρ不是restriction层内在算子，另一个延拓可以改变其法向导数。边界Taylor jets的独立性与bulk导数的这项区别必须保留。
normal regular 费用并非由(3)支付。对这个指定radial extension，ρ=e^x下

\[
\partial_\rho a_r(\rho)=\rho^{-1}r(\log\rho),
\]

因此哪怕先固定一个bulk点，控制这个指定radial derivative就需要point evaluation。
内在补强可用D_x A_r=r：若F是任一ambient延拓，沿螺旋有D_x(F|Z_L)=ρ∂ρF+(2π/L)∂θF。固定bulk点上系数有界，故完整ambient C¹ norm仍须控制该切向导数；单个法向分量则不能由此推出必要下界。
原du和Dlog均不控制该点值；568§5.2已给原Dlog point／jet的严格费用反测。不能由raw源属于C∞便声称这种lift在原范数中连续。
具体可固定bulk点x₀、取φ∈Cc∞、φ(0)≠0，并令r_ε(x)=ε^{-1/2}φ((x−x₀)/ε)。其du norm恒定，而
`||r_ε||²_Dlog=||φ||²_2 log(1/ε)+O_φ(1)`；故正规化为Dlog norm1后，点值仍按
`ε^{-1/2}/sqrt(log(1/ε))`发散。这是在一个固定compact源窗内的raw代表费用，不必先构造principal或pole-zero反测。
若额外要双矩零，可用固定两个光滑probe消去μ±；原r_ε的μ±=O(√ε)，修正项所有固定norm均O(√ε)，点值发散保留。
若另加强Sobolev／weighted S_exp半范数则可付，但必须单列：在ρ≥e^{-B}的覆盖窗，k阶normal微分带e^{kB}，另需要r至多k−1阶的相应点值控制；负端flat全seminorm由(2)的p_{N,j}支付。
覆盖窗B、源支撑A和实际高阶regular norm是三个不同参数，不能只留一个“fixed窗常数”。

合法修补是先固定κ∈Cc∞，令rκ=κ*r，再取A_{rκ}。
在每个|x|≤B上，k≥1时可用Cauchy–Schwarz得

\[
\sup|\partial_\rho^k A_{\kappa*r}|
\le C_{\kappa,k}e^{kB}\|r\|_{du},                       \tag{4}
\]

其中C_{κ,k}只含κ至多k−1阶导数的L² norm。若源支撑[−A,A]且κ支撑[−a,a]，C0还可用
||κ*r||₁≤||κ||₁√(2A)||r||du。
这是指定radial extension的原范数regular representative upper；它不是restriction层任意延拓的内在∂ρ估计，所构造的线仍对所有源相对平凡。
不能把(2)、(4)的坏增长说成**所有同构类lift**的必要lower：当前Pic类为零，本来可以直接选零／单位代表。
若保原mark以区分源，则该mark的费用与额外regularity必须保留。

## 4. 强制解析regularity没有自动修复全源域

需要分开“边界解析germ”和“整个side解析”。

- compact r 的g_r在充分负端恒1，所以边界解析germ合法，却仍是relative gauge。
- 对一般noncompact S_exp，g_r−1为flat但可能在每个负尾非零；这时它不能是非零的ρ-解析germ。
- 若要求整个bulk也实解析，则generic compact smooth r的primitive本来就不在域；不能用这种域缩小直接略掉537或全405。

对完整405的P，第二点是实际失败，不是仅举一个人为源：若A_P在某个负尾为0，则P在该尾为0，H在那里满足(D²−1/4)H=0。
H在该尾是a e^{x/2}+b e^{-x/2}；S_exp的超指数衰减迫a=b=0，与H>0矛盾。
因此A_P在每个负尾均非恒零，而其全部ρ-jets为0。其指数不具有非平凡解析ρ-germ。
这已经足以阻止“只要求边界解析而允许内部光滑”的候选覆盖全部405实际主关系。

即使允许从环境(ρ,θ)解析函数限制到螺旋也一样：若限制值对ρ为flat，取环境Taylor展开的第一个非零ρ系数F_n(θ)。
沿ρ→0可使θ=e^{2πi logρ/L}趋于任意边界点，flat性迫F_n在整个圆上为0，递归迫全部系数为0。
边界紧性和局部解析性遂使环境函数在一个负端邻域恒零，矛盾。
此论只适用于所说的环境解析层；不排其他尚需构造的noncommutative／overconvergent／带权结构层。

在x变量作Gaussian holomorphic smoothing并不改这一门：卷积后的非零S_exp函数仍在ρ变量flat，一般产生logρ型的非解析边界行为。
“x-entire”与“ρ-Cartier regular”不是同一个条件；选择复厚化／横截方向本身是新输入。

## 5. actual E 与反射primitive：先分清两种边界

405实际径向限制是

\[
E\eta(x)=2\sum_{n\ge1}\eta(ne^x),\qquad
E\eta(x)=e^{-x}E\widehat\eta(-x).
\]

中心化后

\[
r_\eta(x)=e^{x/2}E\eta(x)=r_{\widehat\eta}(-x).          \tag{5}
\]

因此在已有actual lift η 的来源像上，两端primitive满足

\[
A_{r_\eta}(x)+A_{r_{\widehat\eta}}(-x)
=\int_{\mathbb R}r_\eta(u)du.                           \tag{6}
\]

这是actual Poisson双lift的准确函数恒等式，并不需要RH。这里x与−x是同一对数时间的两端；它本身没有给574有限位P、Q之间的几何反射、regular层比较或Cartier同构。
若将这两个primitive作为两片frame的指定候选，以下仅检验该具体赋值，不把Poisson函数恒等式冒称已建两finite边界映射。
若保两端常数frame，把右primitive正规化为B_r(x)−∫r=−A_r(x)，两边exp拼接便为1；537没有被独立捕获。
若不正规化而保留(6)的常数exp(∫r)，得到的是相对frame差的mean标签。
405实际P具有

\[
\int P=-\tfrac14\int H<0,                              \tag{7}
\]

所以它失败全主关系。纯unitary指数也可通过缩放同一P避开指数的2πi核，不能修复。
只用μ±正规化则双pole-zero的537 r₀也被删去。

不能假设任意物理r都有η lift；对η像／闭像／全源域的范围必须如405分别保存。
若宣布“恰把所有actual E principal primitives加入regular units，而不加入其他flat primitives”，这可以定义一个人造quotient层，但须另证其locality、乘法、自然覆盖下降及Cartier有效性。
单以P_c指定允许gauge的做法，只将旧源关系移到层的定义中，不支付独立valuation／capacity。
因式分解经过正确旧商本身没有逻辑错误；当前欠的是从该定义外独立证明的几何过滤与预算。

## 6. periodization／holomorphic jets的准确停止范围

actual侧圆上的自然periodization为

\[
\operatorname{Per}_L r(t)=\sum_{n\in\mathbb Z}r(t+nL),
\qquad\frac1L\int_0^L\operatorname{Per}_Lr=\frac1L\int r.
\]

它对S_exp良定义并在其Fréchet拓扑连续。由(7)，对405实际P的圆均值非零，所以不能直接作为消主关系的边界gauge／section invariant。
若源支撑[−A,A]，令N_A=⌈2A/L⌉+1，每个纤维至多N_A项，故

\[
\|\operatorname{Per}_Lr\|_{L^2(S_L)}^2\le N_A\|r\|_{du}^2.
\]

这是明确fixed窗费用；不推出全线原norm有统一界。平移多个不重叠副本会让圆读出的coherent费用增长。
本稿不声称减去均值后所有higher Fourier modes也已被这个单反例排除；单个非零mode是否失败须另算其实际Mellin值。

更一般，若有限jet／regular取值在全线原du或Dlog中有一个有限统一bound，且精确消全部P_c，553的principal cyclic稠密性迫这个读出为0。
这个结论只对给定linear／Hausdorff能量目标及全域有界拓扑成立；不能直接套到574的非Hausdorff Pic参数空间。
有费cofinal变域、Fréchet、infinite jets及非线性relative family仍是合法逃逸。
若靠Mellin取值识别何处应消actualE像，消失条件又回到旧完整Mellin／zero-jet关系；它可为合法旧修补，但没有新的capacity输入。

## 7. 连续正反例和函数域正控制

沿562的真实连续系统Z_c(s)=1+c/[s(s−1)]，d=c−1/4=±1/16，primitive代数
R_d=C[w]/(w²+d)、w†=−w，a_r=A_r+B_rw，完整Q_c=2|A_r|²+2d|B_r|²。
这里本节代数坐标A_r与(1)的primitive函数不是同一对象，避免以同名偷换。
用574已经代入的odd双pole-zerocompact源 r=(D²−1/4)(uφ)，φ偶、非负、非零，两个模型Q严格异号。
上面的smooth-flat primitive构造在两模型都给relative单位／零线类、全部ρ-jets为0；它连正模型的真正primitive方向也不覆盖。
加上单纯positive fiber metric并不改变此结果。
控制只检验候选设施，不为一般连续g凭空配上Q₂、Q₃ adeles。模型自身Γ=0、完整双pole与continuous prime measure不删。

函数域正控制的额外数据不是exp(A)的存在：在真实光滑proper曲线上，每点的O_{C,P}是DVR，局部有理函数给整数ord_P，线丛通过有理／regular units下降。
有理函数的principal divisor给同一对象上的全局关系，properness给有限维H⁰，RR与曲面／对应上的有效性交数再承担mixed容量。
exp(局部积分)若保持regular且无零，只给ord=0的unit；若积分有极点，其指数一般有essential singularity，并非代数有理／meromorphic Cartier函数。
所以它不能替代函数域有理函数到principal除子的设施。

复物理源可加性与整数valuation的角色也不能混：固定位置的、处处定义的additive群同态C→Z为零，因为C可除而Z无非零可除子群。
但这**不排Pic⁰移动族**：代数族中零点位置可移动，单点ord可跳，degree在flat族中不变仍允许Jacobian非平凡。
要用后一逃逸，必须实际给参数base、线对象、moving divisor／sections、base change及原metric lift；不能只将整数权换成复指数或调用离散性排除所有族。

## 8. 保留完整经典目标；独立缺口与停止

所有source测试均以574(7)的完整Qζ为最终比较对象，但不以它定义源标签：完整Γ(t)=Re ψ(1/4+it/2)−logπ=2θ′(t)、contact、每个p^k、双pole和全部complex mixed均不删。
actual E双lift属于Poisson来源，至多解释对偶／关系，不自动生成上述所有局部预算的同源capacity identity。
两位regular-circle设施更不覆盖其他finite places或archparity/contact。

这个候选源门已到明确停止条件：primitive／smoothing虽是真实非scalar物理构造，却在合理smooth单位层中过度消去所有源；边界解析修补不覆盖noncompact405；双lift余项与periodization回到失败mean／旧Mellin关系。
不续调κ、有限jet阶、probe个数或重新用Q标记。

尚欠的独立输入可精确列成同一对象上的五项：

1. 实际regular／meromorphic结构层及其局部整性环，证明由adelic覆盖和dual关系自然决定，且允许全405的实际同构而保537；
2. 不以P_c或Xi零除子定义的source→marked relative line／moving section公式，连同全部principal的actual gauge，不能只给source quotient的别名；
3. 分离的local vanishing／整格过滤、乘法与真实finite evaluation kernel，避免flat层的∩Iⁿ非零和无限圆系数；
4. 原du／Dlog上的合法fixed窗、变域cofinal及regular／metric费用，若加强norm要把价格完整带回；
5. 不由Q符号或旧zero-jet坐标定义的primitive mixed有效性／RR容量，以及与全部Γ、pp、pole的同源预算identity。

当前新增的是具体候选和逐门scope／费用核查，不是独立正性或新actualζ whole后果。最强旧whole leading4/5、成长core／coupling／Xi和宏观瓶颈均未改变。
该稿结论不排新的非标量relative层、真正moving Picard族、较强有费拓扑、非局部regularity或不同完整算术模型。
