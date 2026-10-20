# 567. 函数域Weil正性的来源：RR容量、全源交数与一般g-integer反测试

2026-10-20，C030；同G20261014／0c4f≤538。本轮按用户要求深入正性来源。
结论是：**曲线的正性来自独立的截面／交数理论，完整点数公式把它接到Weil源；
一般正g-integer分布确能模仿对应及其对偶，却不能自动继承该交数的符号。**
本次新检验给连续全Π的形式graph模型：正反两段均有正的不同图交数、正degree、
精确反射与同源配对，primitive signature仍不同。经典ζ的独立正性尚未取得。

## 1. 先分清三种“函数域正性”

对光滑射影几何连通曲线C/F_q，RH等价于其规范完成化的完整Weil正型。
曲线可以用C×C上的Hodge index，或Jac(C)上的Rosati正性证明，均有独立几何来源。
阿贝尔簇也有ample polarization与Rosati机制。一般高维光滑射影簇的分次纯性由
Deligne证明；这不等于一般标准Hodge正性或原Frobenius半单性均已证明。
技术来源分别核[Milne §1、§3](https://jmilne.org/math/xnotes/pRH.pdf)及
[Deligne Weil I §3、§§4–7](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf)。

001/002早有“正极化＋同源迹⇒纯性”；307有实际椭圆degree基准；563/566已付
有限证书和heat实现。更强的RR迁移责任在[363§5](363-f1-arithmetic-geometry-and-existence-audit.md)
已核Connes–Consani策略，不能把重读这些机制计为经典新输入。
本轮只将其向来源前端展开，并用新的全Π模型检验能够推广哪一部分。

## 2. 正性之前：一个固定截面空间排除错误二次增长

设S是代数闭域k上的光滑射影整曲面（因而H0(O_S)=k），K为canonical divisor，H为hyperplane class，
l(D)=dim H0(S,O(D))。独立于任何ζ零点，几何给：

1. 所有l(D)有限；非零截面s的乘法单射H0(E)→H0(E+div(s))。
   等价地，l(A)>0时l(A+B)≥l(B)。
2. l(D)>1意味着D有非零有效代表，因此D·H>0。
3. surface RR、Serre对偶和h1≥0给

\[
 l(nD)+l(K-nD)\ge\chi(O_S)+\tfrac12(n^2D^2-nD\cdot K). \tag{1}
\]

若D·H=0，则l(±nD)≤1。反设D²>0，分别将n、−n代入(1)，得到
l(K±nD)≥cn²−O_D(n)，c>0。两者最终非零；选一个非零截面乘法，即得

\[
 H^0(K-nD)\hookrightarrow H^0(2K).
\]

左边趋于无限维，右边是同一固定有限维空间，矛盾，故D²≤0。
这恢复Hodge index的关键负号，无须先读纯谱、给未知正H或选光滑H。
来源核[Milne Thm1.2，印刷8页](https://jmilne.org/math/xnotes/pRH.pdf)。
真实输入包括RR的二次系数、有效性的degree约束、可相乘的实际截面和固定容量；
只有形式Euler等式不能代替它们。

## 3. 同一交数怎样精确变成完整Weil正性

在C×C上固定F1=C×pt，F2=pt×C。F1²=F2²=0，F1F2=1。
Γ_n=graph(Frob_q^n)，n≥0，满足Γ_nF1=q^n、Γ_nF2=1。
其primitive部分和全部交数为

\[
 D_n=\Gamma_n-F_1-q^nF_2,\quad D_nF_i=0,
\]
\[
 \Gamma_n^2=(2-2g)q^n,\qquad
 \Gamma_m\Gamma_n=q^{\min(m,n)}N_{|m-n|}\quad(m\ne n). \tag{2}
\]

自交来自adjunction；N_r=#C(F_{q^r})。第二式必须保留纯不可分交重数q^min：
固定点的局部交重数先为1，共同复合Frobenius再将局部方程提升为q^min次幂。
这不是有限点数拟合。置E_n=q^{-n/2}D_n，直接展开得

\[
 -E_mE_n=a_{n-m},\qquad a_0=2g,\quad
 a_r=q^{-r/2}(q^r+1-N_r),\quad a_{-r}=a_r.             \tag{3}
\]

Hodge index作用于(F1+F2)^⊥，先对整数divisor再作有理／实／复系数延拓，
给所有有限Toeplitz Gram正性。归一化系数非有理不意味着它本身必须是Cartier divisor。
任意有限整数指标整体平移到n≥0，不改变(3)。

令L=logq。563已核全部周期极点／原点项后的完整源是
W_C=LΣ_{n∈Z}a_nδ_{nL}。对每个g∈Cc∞(R;C)，分段换元严格给

\[
 Q_{W_C}(g)=L\int_0^L
 \left\|\sum_jg(y+jL)E_{j+j_0}\right\|^2dy\ge0.        \tag{4}
\]

支撑保证统一有限和，j0使下标非负。全部proper powers、周期与a0均在式内。
这直接给完整Weil正性，并没有先假设RH或563的正H。
之后可作GNS完成，但cyclic Gram商的rank不能冒充2g的普通trace重数；
566的heat实现仍须使用原全递推／带重数Tate trace，保留其独立责任。

Rosati是另一实现：ample divisor先定义†并独立给Tr(AA†)>0；
Frobenius与Weil pairing另给F†F=q。两笔费用接到同一Jacobian／点数trace后才推出纯性。
反射配对本身不提供第一笔正号。

## 4. 新检验：连续完整Π可造正交点，却不自动有Hodge index

取562已证的真实正primitive族

\[
 Z_c(s)=1+\frac{c}{s(s-1)},\quad0<c\le\tfrac12,
 \quad d=c-\tfrac14.
\]

P、Π和M的正性由562的全级数／卷积证明支付，不能从下面n_c≥0倒推。
这里Γ=0、极点0与1、自然完成化已经指定。完整源及全部prime-power密度是

\[
 W_c(u)=\begin{cases}2\cos(\sqrt d\,u),&d\ge0,\\
 2\cosh(\sqrt{-d}\,u),&d<0,\end{cases}
\]
\[
 d\Pi_c(u)=\frac{n_c(u)}u\,du,\qquad
 n_c(u)=e^u+1-e^{u/2}W_c(u),\quad u>0.                 \tag{5}
\]

n_c是u倍完整Π密度，**不是累计g-integer计数N，也不是primitive P密度**。
正段用cos≤1，负段用0<√(−d)<1/2，均得所有u>0的n_c(u)>0。

在实自由空间中取F1、F2及Γ_t，先t≥0，定义

\[
 F_1^2=F_2^2=0,\ F_1F_2=1,\quad
 \Gamma_tF_1=e^t,\ \Gamma_tF_2=1,\quad
 \Gamma_s\Gamma_t=e^{\min(s,t)}n_c(|s-t|),              \tag{6}
\]

其中n_c(0)=0，所以Γ_t²=0。它是完全由同一源决定的对称配对，
不是已构造的scheme、同态次数或真实有效除子范畴。置
D_t=Γ_t−F1−e^tF2，E_t=e^{-t/2}D_t，计算即得

\[
 \boxed{-E_sE_t=W_c(t-s).}                             \tag{7}
\]

正反两段的所有不同图交数均正，双degree和pole背景也相同；primitive符号却不同。
负段令r=√(−d)，任意h>0给

\[
 \det\begin{pmatrix}2&W_c(h)\\W_c(h)&2\end{pmatrix}
 =-4\sinh^2(rh)<0.                                    \tag{8}
\]

因此primitive部分已有正的交数方向，加上fiber双曲平面，整体正index至少2；
真正曲面Hodge index只允许1。正段由cos加法直接给全部Gram半正定，
阈值rank1只说明cyclic商退化，不把二重零点的ordinary trace变为1。

这也有合法平滑测试，毋须用δ：取非零非负实偶φ∈Cc∞，
g(u)=φ(u−h/2)−φ(u+h/2)，则负段完整源精确给

\[
 Q_{W_c}(g)=-8\sinh^2(rh/2)
 \left(\int\phi(u)\cosh(ru)du\right)^2<0.             \tag{9}
\]

形式关系还可以完整保留：将(6)扩到t∈R，transpose取Γ_t↦e^tΓ_{−t}、F1↔F2，
保持交数；shift Γ_t↦Γ_{t+r}、F1↦F1、F2↦e^rF2使交数缩放e^r。
在形式group algebra上定义Γ_t∘Γ_s=Γ_{t+s}及Γ_t*=e^tΓ_{−t}，
σ(Γ_t)=e^{t/2}W_c(t)，直接得σ(Γ_t∘Γ_s*)=−D_tD_s。
单位化u_t=e^{-t/2}Γ_t后，σ(u_tu_s*)=W_c(t−s)，平滑积分便是完整Q。
这些身份两段均成立，负段σ并非正state；形式复合不制造几何section或有效锥。
因此“正的prime计数＋正的不同graph交数＋对偶／复合／迹”仍不能生产Hodge负性。
本轮新增的是这个全Π同源对应反测试；连续RH相变本身归562/563旧资产。

## 5. 真曲线与正整数Euler负例：RR必须排除什么

563的F5真曲线y²=x³+x+1，g=1、N1=9，以及290的q=5、g=1、N1=1模型，分别给

\[
 -(D_iD_j)_{i,j=0,1}=\begin{pmatrix}2&-3\\-3&10\end{pmatrix},
 \qquad\begin{pmatrix}2&5\\5&10\end{pmatrix}.           \tag{10}
\]

行列式分别11和−5。290已证明其全部primitive closed-point数为正整数、
Euler乘积、精确FE、形式PD/HL和全递推均成立，不能把它当成“无算术”的负例。
整数primitive symbol D=2D0−D1在负例中满足D²=2，在真例中为−30。
前者若有第2节同源截面理论，RR迫使l(K±nD)≥n²−O(n)，注入固定H0(2K)即矛盾。
因而所缺的不只是degree计数的正性，而是作用于任意signed对应组合的真实有效性／RR。
全次数性来自290与实际几何，不从这两个有限Gram外推。

## 6. 高维还提示另一种推广：全部tensor正性必须配pole预算

Deligne Weil I Thm3.2的具体输入包含：P1有限去点开集上的lisse sheaf、非退化
交替配对、足够大的symplectic monodromy和有理局部特征多项式。
even tensor幂的局部幂迹为(Tr F_x^n)^{2k}≥0；monodromy另行识别tensor coinvariants，
cohomological公式控制全部tensor L函数的全局极点。非负级数半径比较给
|α_x|≤q_x^{β/2+1/(2k)}，再令k→∞并用对偶夹成纯性。
这是原文§3的机制恢复，后续Lefschetz pencils／rationality才接到一般高维对象。

可迁移的组合是“全tensor阶正性＋同源全局极点控制”。仅把正Euler系数取偶次幂
没有支付第二项；把所需极点位置作为未证假设，也没有减去纯性责任。
更不能将经典ζ的局部参数1的纯性，当作其全球非平凡零点的纯性，002早已排除此混淆。
此路线值得保留，但本轮没有得到经典所需tensor对象及其极点定理。

## 7. 最大合法推广及经典Γ对角的具体难点

一般化可以允许连续、非lattice、无限维与分次系统，不必先恢复普通整数梳。
但bare正P＋Mellin对偶不能使全体对象pure，(8)及290已经否定这一断言。
能够成立的充分框架要求：先固定完成化／预定权；再由源构造对应／截面载体，
独立证明第2节的有效性、乘法与RR预算；最后证明primitive交数等于−Q_W。
对实偶W，在足够稠密的实compact测试上证明后可按连续性与复化恢复全部复杂测试。
若只定义I(D_g,D_g)=−Q_W(g)再假设I负，仍是等价改写。
若裸假设“有满足这些性质的截面空间”，未给独立来源，责任也仍未支付。

经典ζ尤其不能原样用(6)的point-graphs。由563完整源直接恢复，u>0、离开原点时

\[
 W_\zeta=2\cosh(u/2)\,du-
 \frac{e^{-u/2}}{1-e^{-2u}}\,du-
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}. \tag{11}
\]

pole背景减W再乘e^{u/2}给正的raw coincidence测度

\[
 d\mathcal N_\zeta(u)=\frac{du}{1-e^{-2u}}
             +\sum_{n\ge2}\Lambda(n)\delta_{\log n}.   \tag{12}
\]

这只是完整旧公式的推论，不是新经典正性。不同测试支撑正距离分离时，
该交点项确为正；但Γ在原点约1/(2u)，质量无限。point自交没有有限值，
必须用平滑D_g并保留Γ finite-part/contact、全部素数幂和双pole。
这些局部有效性不能决定正规化后的primitive自交符号，正如连续反测试所示。
数域还须保理想标签重数、判别式和全部无穷处，不能仅用数值范数集替代。

经典真正还缺两项相连的新输入：一个有实际截面／乘法／有效性的载体，
以及该载体的Euler二次项与完整Weil源的精确比较。单条周期轨道RR、
局部复提升或形式主关系不等于这个平方上的RR；363、405/406、552已有准确边界。
566还表明不能把全线physical Weil型直接当作可闭正能量，须核另载体与norm运输。

### 无限／正规化情形：固定容量可以放宽为一个有误差的有限预算

无需要求一般系统有有限genus或一个有限维的全局H0(2K)。对每个固定实compact测试g，
若能独立构造cutoff j的实际截面空间l_j、K_j、D_j及乘法，令
C_j=l_j(2K_j)≥0，并在某个整数n=n_j≥1证明

\[
 l_j(\pm nD_j)\le a_j,\qquad
 l_j(\pm nD_j)+l_j(K_j\mp nD_j)
 \ge\chi_j+\tfrac12n^2d_j\mp\tfrac12nb_j-\epsilon_j,  \tag{13}
\]

其中d_j是该cutoff的自交二次系数，b_j是canonical线性系数，ε_j≥0包含所有RR误差。
维数非负和乘法直接给min{l_j(K_j−nD_j),l_j(K_j+nD_j)}≤C_j：
若一个为0即成立；若两者非零，用任一非零截面乘法分别注入H0(2K_j)。
因此仅在这个n_j的两条不等式就给可审计预算

\[
 d_j\le R_j:=\frac{2(C_j+a_j+\epsilon_j-\chi_j)+n_j|b_j|}{n_j^2}. \tag{14}
\]

若同源身份给|d_j+Q_W(g)|≤η_j，η_j→0，且limsup R_j≤0，便有Q_W(g)≥0。
这允许C_j发散，只须其相对n_j²与其他误差共同受控；不能先取掉cutoff再用固定容量。
必须对每个compact g支付(13)、同源η_j和该尺度选择，或在足够稠密的测试代数上付并核连续性；
有限若干g、无误差Euler符号或单条周期轨道RR不满足此量词。
若目标Q_W(g)<0，(14)反而强迫一个正的预算下限：这些维数／误差不能同时小。

(14)是本轮将经典RR论证量化的条件接口，未生成经典的sections、ε_j或η_j；
只假设存在满足R_j→0的未知数据仍有RH强度，不能列为已取得的独立算术输入。
它的用途是让候选构造能被具体否决，并保留有限容量论证无法直接覆盖的无限载体。

## 8. 消费、纠正与下一门

073 §7旧句把一般有限域纯性与普遍正极化混写，本次原位缩回已证类并追加范围纠正。
NB/NC等条件定理未变；562–566已经明确保留purity、半单性、正H的区别，
未用旧句作强消费。因此没有需要撤回的经典正性或heat身份。

C030在两独立原稿、root逐式核验和独立逆审后统一结算本次源模型检验1轮；
来源重建、标准RR/Deligne定理、旧反例、组织与推送不另计。
actual强旧542＋555→557的whole leading4/5、560成长K/core/coupling与Ξ仍未变，
长期Goal不因此完成。实际瓶颈没有消除；本次明确了可独立付款的来源和假实现的拒绝点。

下一唯一准入：对363已归档Connes–Consani2018 §3.4作一次与(11)的具体比较门，
只核其**平方的相对指数二次项与Γ对角finite-part**是否已有可用身份／误差。
保原canonical scalar/双degree／原norm；有新同源输入才新建合同。
若仍只给策略、周期轨道RR或未构造H1，则来源0立即停，不续本合同、不调continuous参数，
返回560已有actualreceiver joint signed门，不另串几何文献。

独立原稿：[函数域来源](../reviews/2026-10-20/grh-geometric-origin/function-field-source-audit.md)、
[一般源模型与负测](../reviews/2026-10-20/grh-geometric-origin/generalization-admission-audit.md)。
正式root收据和独立终审在同目录；文件hash只绑定版本，不认证数学。
