# Weil结构、固定数据纤维与存在性：公理和可实现性分层

2026-10-22。独占分支原件；供root审查消费，不单独开合同、计轮、改STATE或创建运行Goal。
恢复G20261014／0c4f、C038／575、001／405／537／562／565–567后的标准设施审查。
本稿肯定用户提出的存在性方向；没有证明经典ζ的正结构纤维非空。

## 1. 存在性可以是真正突破，逻辑等价不等于循环

可以先定义“某种Weil结构”，再证明固定经典数据上的结构存在。这样可能将无穷多个不等式压缩为一个几何存在性定理。
但必须区分两句话：

1. 完整Weil正性等价于某种结构存在。
2. 已由独立算术／几何构造证明该结构存在。

第一句提供正确目标；第二句才支付未知正号。即使第一句是等价，第二句仍可能成为非循环RH证明。
循环只发生在存在性证明再次借用目标正性、目标零点位置或未经证明的等强极化，而不是发生在“存在性”这一表述本身。
001已经给有限维极化及无限维adjoint充分接口，562给GNS及完整谱识别，567给有效性／RR来源；本稿组织它们的责任，不将其重计新正性。

“由原分布构造”也不是一个足以排循环的形式公理：完整Q本来就是原分布的函数。
需要在每个存在性证明中列明原始输入、实际构造公式、正性来源和最后的完整预算识别；仅改称“自然”无法完成这项审查。

## 2. 先固定底数据；不能让存在量词顺便选择目标

在log变量u中，固定一个已定义的g-system数据包

\[
 \mathcal D=(P,\Pi,M;\,\mathcal C,\mathcal A,\mathcal H;
      \mathscr F,\mathscr P,\mu_\pm;\text{growth/domain conventions}).
 \tag{1}
\]

其中P给primitive分布，Π保全部proper powers，M给g-integers；\(\mathcal C\)是事先固定的完成化／权，\(\mathcal A\)为全部archimedean有限部分和contact，\(\mathcal H\)为完整已知极点背景。
一般对偶是\(\mathcal D\leftrightarrow\mathcal D^\vee\)，不是自动自对偶；有多权时先分级。只有在固定自对偶实结构或适当成对后，才谈下面的Hermitian正性。
裸P未必有亚纯延拓、规范完成化或有限指数阶W；不声称所有g-system都自动属于这个底空间。

令\(\mathscr F=C_c^\infty(\mathbb R;\mathbb C)\)至少在域内；经典关系测试另用405的\(\mathcal S_{\exp,\mathbb C}\)，物理源为\(r=e^{u/2}f\)。
若一般W只是分布，先只在compact测试定义；延到S_exp须独立给增长和连续性。
本稿相应经典底数据全部采用现有已付延拓。

固定完整线性平衡\(W_\mathcal D\)，置

\[
 r^*(u)=\overline{r(-u)},\quad
 B_\mathcal D(r,s)=W_\mathcal D(r*s^*),\quad
 Q_\mathcal D(r)=B_\mathcal D(r,r).
 \tag{2}
\]

\(B\)的第一变量取线性。\(\mathscr P\)是来源端**预先指定并证明**落入rad B的关系，不是将rad B重新命名为主关系。
经典\(\mathscr P=P_c=e^{u/2}P_{an}\)包括405全部非compact实际关系；只测compact交空没有意义。
双degree \(\mu_\pm r=\int e^{\pm u/2}r\)作为单独数据保留，不强迫它们从primitive Hilbert空间恢复。

经典固定目标为

\[
\begin{aligned}
Q_\zeta(r)={}&2\Re(\mu_+r\,\overline{\mu_-r})
 +[\psi(1/4)-\log\pi]\|r\|_2^2\\
&+\frac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}
            \|\tau_vr-r\|_2^2\,dv\\
&-2\sum_{p,k\ge1}(\log p)p^{-k/2}
                  \Re(r*r^*)(k\log p).
\end{aligned}\tag{3}
\]

其Fourier multiplier为\(\Gamma(t)=\Re\psi(1/4+it/2)-\log\pi=2\theta'(t)\)。
允许结构空间选择正度量、截面和局部模型，却不允许它选择另一个Gamma、删去p^k、忽略双pole或乘入含额外零点的B(s)。
这正是固定纤维\(\mathfrak W(\mathcal D_\zeta)\)与“全体某些正系统有成员”的差别。

## 3. 三个层次；只有第三层承担独立几何来源

### W0：弱Weil实现

一个弱实现由带连续源映射\(j:\mathscr F\to V\)的复向量空间、Hermitian型b、平移／对偶操作以及保留的degree块组成，满足

\[
 j(\mathscr P)=0,\qquad b(jr,js)=B_\mathcal D(r,s),
 \tag{4}
\]

并保持指定源的操作和原域。**不要求b正。**
标准成员为\(V=\mathscr F/\mathscr P\)，b为B的下降，带商拓扑；这证明弱纤维非空，但正是旧源商实现。
可以更进一步把V换成实际覆盖的线、对应或DGA的实现；它们是弱纤维中带额外设施的候选，不是自动正的成员。
574非平凡相对线和575真实Cartier结构说明额外设施不必全平凡；它们也说明正纤维metric不等于(4)的Weil正性。

### W1：正源实现

正源实现为\((\mathscr K,J,U)\)：K是Hilbert空间，\(J:\mathscr F\to\mathscr K\)线性连续，J(F)稠密，U是强连续酉平移，且

\[
 \langle Jr,Js\rangle=B_\mathcal D(r,s),\qquad
 J\tau_t=U_tJ. \tag{5}
\]

\(J(\mathscr P)=0\)须由已证明的关系责任得到；还须通过537非根测试。
**不要求ker J恰为P_c。**最小正实现的核恰为rad B，而405只给P_c包含其中。
405的h有非零两个degree而谱迹为零，因此degree信息必须另存；multiple-zero jets及自然动力学的Jordan也不由GNS商自动保存。

**标准命题。**在本稿固定的连续、平移不变域内，正源实现存在，当且仅当\(Q_\mathcal D(r)\ge0\)对全部r成立。

证明：正实现直接给Q=\|Jr\|²。反向，半正定Hermitian型满足Cauchy–Schwarz，令N={r:Q(r)=0}=rad B，取F/N的Hilbert完成。
平移保持autocorrelation，故下降为等距映射，并以逆平移给酉性。源拓扑中\(\tau_t r\to r\)及B连续给\(Q(\tau_t r-r)\to0\)，从稠密域延出强连续U。
这就是最小GNS源实现，不先用零点；但其存在的未付前件正是完整Q非负。证毕。

因此W1空间给正确且有用的存在性目标，却不额外制造正号。
从U可得Stone自伴生成元，但不能自动声称其普通trace或determinant具有目标零点重数。
562在双重中心零点处的GNS rank1与ordinary multiplicity2已经是具体反测。
具体说，\(L^2(\sum m_\gamma\delta_\gamma)\)的每个atom仍只有一个Hilbert维数，ordinary projection trace是1，不能从测度权m直接读成维数m。
需要普通谱行列式时，另给multiplicity纤维\(\mathbb C^{m_\gamma}\)及完整识别；此时源的平移cyclic子空间一般不再稠密，不能原封不动保留W1的minimal条件。
另一合法实现是给半有限／tracial代数和\(\tau(P_\gamma)=m_\gamma\)，完整核对该trace的行列式身份。
连续谱类允许state／半有限trace时，应另立相应对象，不能硬套通常entire零除子。

### W2：独立有效性／RR结构

这是W0上额外的几何证书空间，而不是把“b正”另写一个名称。其基本设施可为：

- 同一个实际ringed／semiringed／其他已定义载体上的整除子格与主关系；可逆线、局部正则单位及可分离的消失过滤。
- 实际截面与乘法，base change和交叠相容；适当性或有控截断保证有限容量。
- 由局部长度／Euler特征独立定义的交数I与RR公式，degree／有效性约束和一个固定截面容量。
- 物理源到该载体的对应或moving线丛映射。全P_c须成为实际主同构或指定合法等价，537非根须仍可见，原费用另计。
- 将primitive交数与**完整**B对应的源身份，含Gamma/contact、all p^k与pole。身份可以含B作为待核目标，但不得以Q数值定义源的标签或以未知正号定义容量。

积分源通常不是整Cartier除子。应先在真实整格上证明RR／Hodge符号，再经有费用的线性延拓、平滑与完备化接全部complex源；不能把\(\sum c_jD_j\)的任意complex系数直接宣称为实际线丛。
线丛moving、数值对应的primitive投影和Hilbert实现是三个角色，不必强迫它们成为同一种对象。

W2是充分设施的一类，未证明它是RH或一般Weil正性的必要条件。连续正例可有完整平方和而无曲线式DVR／proper有限截面。
其他可能的独立证书包括566的正闭能量＋同源all-time heat identity，或Deligne式tensor全阶正性＋全局pole控制。
“全部Weil结构”适合取这些**带证书类型的并类**，而不是把某一曲面RR模型强制为所有正系统的唯一机制。

## 4. RR怎样真正给正号：有限容量命题

下面是567来源机制的明确充分接口，不是本轮新的RH定理。
设实际整曲面型设施给除子D、K、ample H及非负整数\(l(A)\)，满足：

1. \(I(D,H)=0\)时，\(l(\pm nD)\le1\)。
2. 对某个选择的n，RR／对偶及误差控制独立给
   \[
   l(K\pm nD)\ge\tfrac12n^2 I(D,D)-nB-A,
   \quad A,B\ge0. \tag{6}
   \]
3. 任一非零实际截面的乘法是单射；\(C=l(2K)<\infty\)。

则

\[
 I(D,D)\le\frac{2(C+A)}{n^2}+\frac{2B}{n}. \tag{7}
\]

证明：若I大于右侧，则(6)使两空间的维数均大于C≥0，故都有非零截面。
取K+nD的非零截面，乘法将\(H^0(K-nD)\)注入固定\(H^0(2K)\)，与前者维数>C矛盾。
这一步的单射使用**同一对象上的实际乘法**，不是两个形式维数的比较。证毕。

若对固定物理r有cutoff j与真实D_j(r)，独立付

\[
 I_j(D_j,D_j)=-Q_\mathcal D(r)+e_j(r),\quad
 |e_j(r)|\to0,
\]

并可选n_j使\((C_j+A_j)/n_j^2+B_j/n_j\to0\)，即得Q(r)≥0。
C_j可以成长，不能只看n_j→∞；所有mixed／源费用、关系同构、全部背景的误差均须包含在e_j、A_j、B_j。
只假设“存在某些l_j使(6)成立”没有支付存在性，尤其不能按Q的符号事后制造这些维数。

真实函数域在\(C\times C\)上由有限截面、Serre对偶、RR和degree有效性提供(6)，与Frobenius graph的交数身份接到完整周期Weil型。
这里的独立有限容量是[Milne §1的曲线／曲面RR论证](https://jmilne.org/math/xnotes/pRH.pdf)的关键；567已逐项恢复。
高维[Deligne Weil I](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)使用其相应全局几何与tensor/pole设施，不能被改述为一般Hodge标准猜想或半单性都已证明。

## 5. 一个实际“全体结构空间”：固定规模的presentation groupoid

不用“所有范畴”的proper class。为当前目标先固定一个可编码的模型类：

1. F取S_exp或相应LF测试域。选一个可数稠密\(\mathbb Q(i)\)线性子集E，闭于star、卷积、D及有理平移；再纳入可数稠密实际405源和double-moment修正。
   可以先从稠密种子出发作可数次这些操作。原S_exp的可分性由其可数加权smooth seminorm模型得到；截断／光滑可给显式稠密种子。
2. 固定可数atlas、关系符号、线／截面／评价对象的可数presentation，以及每个fixed窗、阶、cutoff的有界常数序列。Hilbert实现用\(\ell^2(\mathbb N)\)及其闭子空间编码；只讨论可分实现。
3. 分别记录：ring/module运算、gluing cocycle及其相容、局部过滤、mark、完整trace身份、费用。它们都编码成固定集合上的函数／关系，故形成一个集合。
4. 以保源、degree、trace、filtration和mark的实际同构作箭头，形成\(\mathbf{Pres}_\kappa(\mathcal D)\)；先用固定大小上界κ或固定编码载体，不声称覆盖任意大小的所有潜在宇宙。

W0、W1、W2分别为这个groupoid中的子问题；forgetful map到固定底数据的**纤维**才是研究对象。
源与系数补全需要预定连续性界，不能仅在一个任意不稠密可数集上“验证”后宣布全源。
若以后出现非可分的必要载体，应扩大规模和trace类型；当前模型类的空纤维不能否定所有可能Weil结构。

该groupoid不是已经构造的代数stack或具proper性的moduli空间。574 absolute Pic中的dense iΛ核使其粗类商沿虚方向非Hausdorff；575又给非分离normal过滤。
所以不能直接从“Pic族存在”推出一个可用的compact／proper结构空间。
存在性定理可在保frames和实际gluing系数的presentation空间中先做，再对gauge取商；gauge紧性及费用须明确，而不是预先当作已证。

## 6. 两种有限存在性；只有一种可能引入新内容

### 6.1 精确Gram因子的有限可行性只是完整正性的穷尽

在E的前N个源上固定

\[
 G_N=(B(r_i,r_j))_{i,j\le N}.
\]

存在向量\(v_1,\ldots,v_N\)使\(\langle v_i,v_j\rangle=(G_N)_{ij}\)，当且仅当G_N半正定。
所有N可行，借稠密性和费用延拓，当且仅当完整Weil正性。
这给一个准确的存在空间和反例探测器；逐步令N增大或对这些Gram块用compactness并不独立证明它们可行。
同样，声明“一切有限一致条件都可解”若这些条件已经包括全部目标Gram PSD，仍承担全部RH责任。

### 6.2 实际几何presentation的有界延拓才是值得证明的下一定理

一个合法的条件性存在原理是：有非空compact Hausdorff presentation空间K_n、连续总restriction \(K_{n+1}\to K_n\)，每个需要的实际关系／gluing／过滤／比较在某一层进入，并且在极限拓扑下闭；源费用对每个fixed窗一致。
则\(\varprojlim K_n\ne\varnothing\)：任意有限段从最后一层选成员并向下限制，故乘积空间中的有限交性质成立。
若此外全部闭的结构条件和同源预算在极限保留，得到相应全局结构。

这只是standard compactness接口。真正新输入将是：K_n来自实际截面与局部单位，而非按G_N定义；证明其非空、限制可延拓、真实容量界和所需紧性。
finite-object存在不自动给这样的K_n。除子degree／rank／height可能无界，gluing gauge非紧，正定度量的严格下界可能退化。

保537尤其不能只写\(\|J_nr_0\|\ge\delta\)后在弱拓扑取极限；\(e_n\rightharpoonup0\)且\(\|e_n\|=1\)是反例。
需要strong相对紧性、一个固定连续评价坐标不消失，或其他实际闭的非退化见证。
同样，strict positive／Cartier nonzero-divisor通常不是随便选拓扑就闭；必须独立证明极限不会flat塌缩或丢掉有效截面。

## 7. 四类控制；不把几种候选的优点拼成一个已存在对象

| 控制 | 弱实现 | 正源实现 | RR／独立几何设施的作用 |
|---|---|---|---|
| 连续c=1/4+d，d=+1/16 | 已有，Γ=0且双pole／全部Π保留 | 562显式平方和存在 | 无须虚构经典adeles或DVR；说明曲面RR不是所有正型的必要形式 |
| 同族d=−1/16 | 同样已有正P/Π/M、对偶和形式对应 | 因已有compact负源，纤维空 | 若拟议公理仍允许它且强制完整预算，则公理不可能独立推出正性 |
| 真曲线／函数域 | graph、transpose、trace及periodic pole全部可核 | 存在，566还有带重数热lift | C×C的有效性、截面乘法和RR给独立正号；需要同一对象而非只模仿数列 |
| 经典ζ | 405商、已有adelic/DGA、574/575局部设施确有弱成员 | 非空性仍为完整Weil正性责任 | 原缺口是非标签源桥＋分离过滤／mixed容量＋完整身份，不再是“没有线／Cartier对象” |

连续反例的代数\(R_d=\mathbb C[z]/(z^2+d)\)、\(z^\dagger=-z\)给源\(a_r=A_r+B_rz\)，完整Q为\(2|A_r|^2+2d|B_r|^2\)。
这说明即使底层复代数同为\(\mathbb C\oplus\mathbb C\)，正确†的正实现纤维仍会一边非空、一边空；只找抽象ring或fiber metric不足。
可使用既有双pole-zero奇源，同时排掉只看degree、mean或575 primitive unit的候选。

405具体关系\(P=(D^2-1/4)H\in P_c\)、H>0必须在同一个候选中成为实际等价；537的\(r_0=(D^2-1/4)\psi\)、\(\psi\ge0\)compact、\(r_0\ne0\)又必须保留。
不允许一个候选消关系、另一个候选见r0，再宣称二者合在一起已经存在。

原du／Dlog费用的门仍在：固定源窗A时，经典完整Γ form加有限prime／pole扰动已有\(|Q(r)|\le C_A\|r\|_{Dlog}^2\)。
在已证明Q≥0的假设下，这给GNS的fixed窗upper；它不是独立正号，更不是全线uniform du或Dlog控制。
553的P_c全线原norm稠密性表明，若J在全线该norm连续且消P_c，则J=0，与537矛盾。
因此结构空间必须允许非uniform cofinal费用、较强源拓扑或不同物理完成，不能把unpaid norm transportation藏进存在性量词。
566还排除把fullQ直接视为原du上的可闭form：即便正，孤立谱原子也会阻闭；另Hilbert载体／GNS是合法选择。

## 8. 推荐的下一门与准确停止条件

应先冻结底数据纤维与结构类型；下面只是下一轮可准入的有限目标，尚无新局部层时不把它启动成未知容量合同：

> 在575同一实际覆盖上，给一个未以Q／零点作标签的局部层及其截面presentation；对405一个实际非compact关系P及其平移、537 r0和它们的mixed线性组合，构造同时可延拓的gluing／局部过滤／评价kernel。证明关系同构、非根评价见证及原fixed窗费用，且至少给一个由实际截面乘法得出的容量上界。

这仍是准入测试，不是全关系或全Weil正性；有限成功后只有带全P_c及cofinal费用的延拓定理才能晋级。
最便宜反控制是同一continuous d±与真函数域实例：实际正号机制须允许正者并在一个明确facility上排负者，不能仅在末端把负者的Q标签否掉。
若presentation只取旧F/P_c、完整Gram分解，或线／Cartier上额外mark等于Q，则作为W0/W1标准实现保存，停止该recipe，不报独立容量。
若能证明实际K_n的非空／紧性和相容，或直接构造RR/energy/tensor证书，则是应单独准入的真正新输入；即使其最终存在性与RH等强，也绝不因“等价”而否定其证明价值。

本稿的净后果是公理责任和存在空间的整理，扣除001／562／565–567及574／575后没有新增经典正号、whole4/5／成长core／coupling／Ξ后果。
宏观瓶颈未变；它被更准确地定位为固定经典纤维中**独立可构造、原费用可运输、完整预算忠实**的证书非空性。
