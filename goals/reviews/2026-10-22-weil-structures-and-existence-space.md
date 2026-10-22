# Weil结构与固定目标纤维：把正性问题变成存在性问题

2026-10-22。用户新方向的结构／来源审查；同G20261014、固定0c4f／≤538输入。C038／575已结算，不续其预算。本稿组织001、405、537、553、562–567及574–575，不登记576或新的数学轮。没有证明经典ζ的正结构存在。

## 1. 采用这个方向，但把存在量词放在正确位置

可以先定义Weil结构，再证明存在；存在性与RH等价，并不使一个独立的存在性证明循环。几何学经常把无穷多不等式转换成某种对象的存在。需要防止的是：定义之后，存在性证明仍然借用了待证正性。

正确目标应写成
\[
 \pi:\mathfrak W\longrightarrow\mathfrak D,
 \qquad \mathfrak W(\mathcal D_\zeta)
       =\pi^{-1}(\mathcal D_\zeta)\ne\varnothing.                 \tag{1}
\]
这里\(\mathfrak D\)是**已经固定完整分析数据**的目标空间，\(\mathfrak W\)是带目标标记的结构空间。函数域、连续正例给总空间有点；经典ζ需要自己的纤维有点。

本轮最有用的区分是：最小正Hilbert实现若存在，已由完整源配对唯一确定到保源酉同构；真正可供构造的自由度在几何载体、截面、局部过滤、乘法和容量证书中。因此不宜只把所有正内积排列成空间，再希望空间本身制造正号。

“独立构造”是证明的来源责任，不能作为一个自动生效的形式公理。同一个对象可能通过未知RH存在，也可能通过独立RR定理存在；必须检查后一条证明的前件，而不是只检查对象名称。

## 2. 底空间：固定什么，以及一般g-system未必拥有什么

目标数据至少为
\[
 \mathcal D=(P,\Pi,M;\mathcal C,w,\vee;
       \mathcal A,\mathcal H;\mathscr F,\mathscr P,\mu_\pm;
       \text{域、增长、范数和规范}).                               \tag{2}
\]
P是primitive分布，Π保所有幂，M是g-integers；\(\mathcal C\)是完成化、w为分次权，\(\vee\)是指定对偶；\(\mathcal A\)包括archimedean有限部分及contact，\(\mathcal H\)保全部极点缺陷。裸g分布未必提供规范完成化、亚纯延拓或这样的增长域，本稿不假装已经从裸P解决了565的识别问题。

一般情形先保\(\mathcal D\leftrightarrow\mathcal D^\vee\)及各权。只有给定自对偶实结构，或已说明成对／分级归一化后，才定义下述Hermitian块；高维各权不能全部强塞到1/2。

在log变量中固定
\[
 r^*(u)=\overline{r(-u)},\quad
 B_{\mathcal D}(r,s)=W_{\mathcal D}(r*s^*),\quad
 Q_{\mathcal D}(r)=B_{\mathcal D}(r,r).                         \tag{3}
\]
第一变量线性。一般先取\(C_c^\infty\)，延到更大域另付增长；经典已有\(\mathscr F=\mathcal S_{\exp,\mathbb C}\)、物理\(r=e^{u/2}f\)。\(\mathscr P=P_c\)为405实际解析关系的物理像，已付\(P_c\subset\operatorname{Rad}B_\zeta\)，不是预先认证的几何主除子。

经典目标不能在存在量词内改变：
\[
\begin{aligned}
Q_\zeta(r)={}&2\Re(\mu_+r\,\overline{\mu_-r})
 +[\psi(1/4)-\log\pi]\|r\|_2^2\\
&+\frac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}
             \|\tau_vr-r\|_2^2\,dv\\
&-2\sum_{p,k\ge1}(\log p)p^{-k/2}
                   \Re(r*r^*)(k\log p),
\qquad \mu_\pm r=\int e^{\pm u/2}r(u)du .                    \tag{4}
\end{aligned}
\]
对应完整乘子\(\Gamma(t)=\Re\psi(1/4+it/2)-\log\pi=2\theta'(t)\)。不能删proper powers、双pole、contact，或乘B(s)找到另一个正目标。对经典已固定的完整显式公式，Weil判据把全Q正性与RH联系；一般g系统若要从正型分布读出零除子，仍须其完整公式、解析域及分离性假设。

## 3. 四种结构层：把自由度和责任拆开

| 层 | 定义／存在性责任 | 已付及未付 |
|---|---|---|
| \(\mathfrak W_0\)：弱源比较 | 向量／对应／线对象带j，Hermitian b可不定，\(b(jr,js)=B(r,s)\)，消实际关系；degree另存 | F/P的signed下降总给标准成员，是诊断用旧商 |
| \(\mathfrak W_+\)：正源实现 | Hilbert H、连续线性J、强连续酉U；\(\langle Jr,Js\rangle=B(r,s)\)，J像稠密、\(J\tau_t=U_tJ\) | 非空恰为全Q≥0；最小实现唯一 |
| \(\mathfrak W_{\rm tr}\)：谱／迹实现 | 指定谱代数、trace类型、重数、全热量／行列式身份和增长域 | 不由最小GNS自动提供 |
| \(\mathfrak W_{\rm cert}\)：带设施证书 | 实际几何RR、独立能量＋完整热身份，或tensor＋全局pole等指定证书 | 应由独立定理得到到正层的映射；经典非空未知 |

**标准GNS命题。**在固定连续、平移不变源域内，\(\mathfrak W_+(\mathcal D)\ne\varnothing\iff Q_{\mathcal D}\ge0\)。正向显然；反向由Cauchy–Schwarz取\(F/\operatorname{Rad}B\)完成。共同平移保持B，逆平移给酉性，源平移连续给U强连续。两个最小实现以\(J_1r\mapsto J_2r\)延成保源酉同构。

所以正层在固定完整Gram之后基本是一个点或空集，增加基底坐标只增加表示自由度。若存在性证明能先从实际截面构造J，再核对(4)，它仍是有效证明；若只说“由GNS存在”，就遗漏了其正性前件。

**核和degree不能误合。**不要求\(\ker J=P_c\)。405的H=Ch有两个degree各1/4，却为Weil trace根；H不属于P_c，因为P_c的两个degree为0。primitive正商会消H，分次0/2必须另保。multiple-zero jets、给定realization的Jordan也不能从净trace恢复。537的明确compact双pole-zero非根r0必须可见，但这不意味着所有旧关系商元素都应在正范数中非零。

**迹和重数不能误合。**\(L^2(\sum m_\gamma\delta_\gamma)\)的每个atom仍为一维，普通投影trace是1而非\(m_\gamma\)。可加\(\mathbb C^{m_\gamma}\)谱纤维，但单源cyclic像不再稠密；或在交换代数上给\(\tau(P_\gamma)=m_\gamma\)。nonatomic谱可允许state／半有限trace，其普通Hilbert heat trace通常无限；一般连续正型不应被“通常整个谱行列式”公理无故排除。

证书层适合是**带类型的并类**。曲面RR是充分来源之一，不是所有连续正例的必要几何。001已有有限维PLF／adjoint接口；本轮不把它重新命名为新定理。

## 4. 一个可编码的结构空间，而非无边界的“所有对象”

固定可数稠密\(\mathbb Q(i)\)源代数E，闭于star、卷积、D和有理平移。从固定compact mollifier的有理平移／缩放出发作可数闭包即可；其在compact smooth拓扑稠密，截断用更强指数半范数给\(C_c^\infty\)在S_exp稠密。加入实际405测试和r0；全P_c的几何消去还须关系稠密子集及连续闭延拓，不能用553的Hlog-cyclic稠密替代F拓扑。

然后固定可数atlas／对象与操作符号、presentation大小上界κ、每个源窗／阶／cutoff的费用序列。运算、gluing、过滤、mark和评价编码为固定集合上的函数／关系；可分Hilbert载体可嵌在\(\ell^2\)。这给一个真正为集合的presentation群胚\(\mathbf{Pres}_\kappa(\mathcal D)\)，再选上述结构子问题。

这不是已经证明存在的代数stack，更没有自动proper性。先保frames和实际gluing系数，再处理gauge；574的dense iΛ粗类商非Hausdorff，575的smooth normal过滤不分离，说明不能先对gauge取商再假设紧。固定κ只是当前模型类；空纤维不能排除所有更大／不同类型的Weil结构。

纯first-order紧致性也不免费保原实数、原分析域、范数费用和ordinary trace。需要在指定拓扑中做真正的解析存在性证明。

## 5. 紧性确实能完成拼接；它不支付有限层正号

枚举E为\(r_i\)，写\(w_{ij}=B(r_i,r_j)\)，独立选有限\(M_i\ge|w_{ii}|\)、\(\varepsilon_N\downarrow0\)。定义
\[
 K_N=\{G\in\operatorname{Herm}_N:G\succeq0,
 G_{ii}\le M_i,\ |G_{ij}-w_{ij}|\le\varepsilon_N\}.           \tag{5}
\]
PSD给\(|G_{ij}|\le\sqrt{M_iM_j}\)，故K_N紧；主子矩阵限制是连续\(K_{N+1}\to K_N\)。若每层非空，compact乘积的有限交性质给逆极限非空：任意有限段从最高层选点并向下限制即可。**不要求限制满射。**取极限误差0，所有有限W块PSD，源稠密／连续性给全Q≥0。

这证明了一个准确的存在性接口，也表明(5)全层非空本身等价于目标正性。彼此孤立的局部问题各有解，若还没有共同限制系统，才不能套此定理；不能反过来说真实非空紧逆系统仍缺surjectivity。

实际有限源空间的原Hlog Gram记H_N。要求候选因子A_N满足
\[
 G_N=A_N^*A_N,\quad 0\preceq G_N\preceq B_NH_N,\quad
 -\delta_NH_N\preceq W_N-G_N\preceq\delta_NH_N.                \tag{6}
\]
在实际零源商上、固定\(B_N,\delta_N\ge0\)时，这可行恰为
\[
 -\delta_NH_N\preceq W_N\preceq(B_N+\delta_N)H_N.              \tag{7}
\]
规范化H_N后把W_N谱clip到[0,B_N]即证充分，必要由(6)。原H_N核代表真实零函数，故W_N在核上相容；一般抽象数据不能省此责任。若允许B_N预先取到已知upper加δ，才只剩下侧门。δ→0且覆盖全源便给正性；此时任意Cholesky因子并未增加几何内容。

真正值得证的是：从**非Q标签**的实际截面／评价det构造A_N，并独立给(6)、共同有限可行和原费，而不是由W_N正性选择A_N。无限Hilbert弱球虽紧，Gram等式不弱闭（\(e_n\rightharpoonup0\)但norm1）；应先用Gram坐标，重建Hilbert不等于重建原几何。Cartier性、非退化metric、乘法单射也都要另核极限保留。

## 6. 费用与域：存在性量词不能偷偷换源

对经典固定\(\operatorname{supp}r,s\subset[-L,L]\)，令
\[
 \|r\|_{H_{\log}}^2=(2\pi)^{-1}\int
 (1+\log(2+|t|))|\widehat r(t)|^2dt,
\quad C_\infty=\sup_t\frac{|\Gamma(t)|}{1+\log(2+|t|)},
\]
则旧完整公式直接给
\[
 |B_\zeta(r,s)|\le C_L\|r\|_{H_{\log}}\|s\|_{H_{\log}},\quad
 C_L=C_\infty+2\sum_{n\le e^{2L}}\frac{\Lambda(n)}{\sqrt n}
                  +4\sinh L.                              \tag{8}
\]
Hlog与原全线zero-extension Dlog等价。sum包含全部proper powers，窗外相关实际为0；pole项是粗upper。Γ高频log费不能由du alone替代。C_L可以成长，不能把有界性冒充小容量。

若全域J以同一个有限常数在原du／Hlog连续且杀全P_c，553的全线密度逼J=0，违反r0。这并不否定Fréchet连续GNS或支撑相关／变域有费的实现；即使每个全域映射各用不同有限常数，也不能逃开密度。

566已显示正Q本身也未必在原全线L²可闭；结构可在另一个载体上有正闭能量。strong-resolvent极限亦不保heat trace：\(Ke_j=je_j\)，K_n只把第n个特征值改0，则K_n→K strong resolvent，却
\[
 \operatorname{Tr}e^{-tK_n}\longrightarrow
 \operatorname{Tr}e^{-tK}+1.                                \tag{9}
\]
每个固定t甚至有统一trace upper。完整热／行列式层需要尾部tightness或trace-norm运输；不能用Gram紧性代付。

## 7. 函数域的独立来源：先有同对象容量，再得符号

真实光滑射影曲线C/Fq在\(C\times C\)上有Frobenius graphs、transpose／复合、实际除子、截面和乘法。proper性保证有限维，RR和Serre对偶给二次增长，degree有效性给primitive约束。它们先推出Hodge负号，再由图交数身份得到全部mixed Weil正性。可核来源见[Milne §1](https://www.jmilne.org/math/xnotes/pRH.pdf)及567；这条链的关键是同一个对象上的乘法和有限容量。

明确的旧充分接口为：实际D、K及\(l(A)=\dim H^0(A)\)，由primitive degree、RR及全部误差独立给
\[
 l(K\pm nD)\ge\tfrac12n^2I(D,D)-nB-A,
 \quad C=l(2K)<\infty,\quad A,B\ge0.                         \tag{10}
\]
非零截面的乘法单射推出
\[
 I(D,D)\le2(C+A)/n^2+2B/n.                                \tag{11}
\]
若反之，两截面空间都大于C；取一边非零截面把另一边注入固定H0(2K)，矛盾。由原RR取得(10)仍是独立前件；(11)不从形式维数命名产生。

对固定物理源的实际cutoff若付
\[
 I_j(D_j(r),D_j(r))=-Q(r)+e_j(r),\quad e_j\to0,
 \quad(C_j+A_j)/n_j^2+B_j/n_j\to0,                           \tag{12}
\]
即得Q≥0。C_j允许成长，但必须和n_j同步付款。先在真实整格／实对应证明，再带mixed比较及原费延到complex源；任意复系数积分不能直接当实际Cartier线丛。

不能把“存在Weil cohomology”当作正号已付。[Milne §§2–3](https://www.jmilne.org/math/xnotes/pRH.pdf)区分trace／对偶与标准正性，并给超奇异椭圆的quaternion系数障碍：不存在覆盖整个char-p几何宇宙的R-valued有限维Weil cohomology。这不妨碍单个对象的复能量证书。

[Deligne–Milne §4](https://www.jmilne.org/math/xnotes/tc.pdf)的technical Weil forms／polarizations已有adjoint-trace正性及tensor／dual兼容；分类以初始正form存在为前件，不能用分类证明任意范畴非空。[Deligne Weil I §§3、6–7](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)另有tensor／monodromy与全局极点机制；不应将其改述为一般Hodge标准猜想或全部半单性已证。证书类因此保留RR、energy-heat和tensor-pole三种类型。

## 8. 三组具体控制及一个退化边界

**真函数域。**旧563／566的\(E/\mathbb F_5:y^2=x^3+x+1\)有N1=9，\(P(T)=1+3T+5T^2\)。直接可核
\[
 F=\begin{pmatrix}0&-5\\1&-3\end{pmatrix},\quad
 H=\begin{pmatrix}1&-3/2\\-3/2&5\end{pmatrix}>0,
 \quad F^THF=5H.                                           \tag{13}
\]
全点数递推和有限证书而非未知根给全部n；L=log5、U=F/√5、\(B_y=\sum_jr(y+jL)U^j\)给完整全周期
\[
 Q_E(r)=L\int_0^L\operatorname{Tr}(B_yB_y^{*_H})dy\ge0.      \tag{14}
\]
period aliases和周期极点均保留。矩阵是已付有限实例；其真实几何来源不能由任意矩阵装饰替代。

**连续正反例。**562族\(Z_c(s)=1+c/[s(s-1)]\)、\(c=1/4+d\)、\(d=\pm1/16\)均有真正正P／Π／M和精确对偶，各自指定Γ=0并保0/1双pole。负段完整\(W_-(u)=2\cosh(u/4)\)。取非零偶\(\eta\ge0\)compact，\(r_1=(D^2-1/4)\eta\)、\(r_2=\tau_hr_1\)，两pole矩0。A=\(\int\eta\cosh(u/4)>0\)，全Gram为
\[
 2(3/16)^2A^2
 \begin{pmatrix}1&\cosh(h/4)\\\cosh(h/4)&1\end{pmatrix}.       \tag{15}
\]
h≠0时det负，尽管两对角均正。故最早2×2有限joint门就空。正段改为cos(h/4)及相应A_+、c_+，全部有限Gram由两个显式Fourier评价给平方和；ODE正能量独立证书在563已付。不是只验证有限N后外推。

**575实际层。**真实非平凡Cartier与clutch线保留；但是其primitive源g=exp∫r在同层是边界1单位，405消掉时r0也消掉。smooth过滤有非零flat交，bulk截面无限维，尚无预算(10)／(12)。它是合法局部设施，却不能进入带完整source marking的正证书纤维；换名不修coverage。

**正定退化与Jordan。**对实a、q>0，
\[
 F_a=\begin{pmatrix}0&-q\\1&a\end{pmatrix},\quad
 H_a=\begin{pmatrix}1&a/2\\a/2&q\end{pmatrix},\quad
 F_a^TH_aF_a=qH_a,\quad H_a>0\iff a^2<4q.                   \tag{16}
\]
端点companion有非平凡Jordan，不能正定酉化，特征根却仍模√q；其半单化可正。给定realization的正定极化严格强于只看行列式RH。由连通deformation不能越过退化自动传正；允许半单化时要付source／norm／trace身份。此为565责任的标准二维演示，不算新研究轮。

## 9. 两条真正可用的存在性路线

**A：实际有限几何设施的有界存在性。**选一个非Q／零点标签的具体presentation类X_N；共同约束含真实关系同构、r0见证、gluing、局部过滤、乘法和同源预算。独立证明各有限批共同可行、包络紧、条件闭、fixed源窗费用一致，再用§5拼接。若这些有限空间按完整PSD定义，仍只做了GNS；若按实际几何定义并由RR或有效性保证可解，才是潜在新输入。

**B：独立正对象的完整分布像闭包。**设\(\mathfrak G_+\)由独立几何／energy／tensor定义，已证每个对象的完整正分布\(\Phi(G)\)。若独立证明
\[
 W_\zeta\in\overline{\Phi(\mathfrak G_+)}^{\mathcal D'},       \tag{17}
\]
则沿实现该闭包的序列或一般网，对每个compact r有
\(Q_\zeta(r)=\lim\Phi(G_j)(r*r^*)\ge0\)。正型分布锥闭，不必使原几何对象本身在naive Pic空间收敛。这比“必须构造一个极限scheme”宽松，是值得保留的独立存在性策略。

未付的正是(17)的同源近似，不能用Euler右半平面收敛或prime数列收敛替代。Γ/contact、all powers、全部pole及所有signed重整化必须在同一完整W_j中收敛；若还要求几何source lift或普通行列式，另付原norm和trace tightness。仅因目标位于正锥的闭包而构造近似会循环；由独立正几何逼近则不循环。

两条路线都比继续给575 primitive乘光滑因子更有价值，但本轮尚无可供启动的真实X_N非空输入或(17)近似族。A保留函数域容量机制，B免去几何极限存在；前者局部层难，后者完整Γ同源极限难。若有具体有限对象与原费，优先A；若有完整正分布逼近定理，优先B。不在没有实物时把未知非空命名成C039。

## 10. 本轮结算、停止与下一验收

本轮交付了固定目标纤维、分层公理、可编码presentation群胚、准确紧性命题及控制。新增的是路线清晰度；GNS、紧性、二维模型和RR充分接口均为标准或旧资产组织，没有新增经典独立正号、容量或whole净后果。

下一只验收一个具体独立候选，至少同时给：

1. 实际对象／操作／源公式，不按完整Q或Ξ零点命名。
2. 同一对象保持405全关系及平移、r0非根和原du／zero-extension Dlog费用；有限测试成功不冒充全域。
3. 独立的实际乘法／过滤／容量，或完整正分布逼近来源；精确指出哪一条前件排掉连续负例。
4. 完整mixed Γ/contact／prime powers／pole预算、成长和尾部误差及强旧对照。

若只返回F/P、任意Gram分解或以Q选metric，保存为弱／正层标准表示后停止；不再串一个未知存在性合同。合法的新层、不同证书类型、强拓扑／变域和有费无限修补均未排除。

最强实际旧后果仍542＋555→557的whole leading4/5负惯性**上预算**，不是实际负谱lower；成长core／coupling／Ξ未付。宏观独立正性／容量瓶颈未改变。统一cadence保持4、历史Weil轮39、正式cycle14不归零；数学Goal门仍open，runtime Goal现场null且未新建。

分支原件：[公理与实现](../../reviews/2026-10-22/weil-structure-space/axioms-and-realizations.md)；[紧性与有限可行](../../reviews/2026-10-22/weil-structure-space/compactness-and-finite-feasibility.md)；[函数域／连续／几何控制](../../reviews/2026-10-22/weil-structure-space/function-field-continuous-and-geometric-controls.md)。
