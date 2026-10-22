# 实际相对 DGA 的 line/module 门：具体图线、主关系与移动责任

2026-10-22。独占审查稿，供 root/fresh 消费；不改 STATE/cadence，不开574或C037。
本稿恢复同G20261014／0c4f及D20261022F；只消费已给实际径向相对DGA，
不把它称为整个adelic cyclic结构层。以下是旧DGA与405/519/553的标准模块推论及具体候选核查，
归来源0；它没有独立经典极化、RR容量或whole/core净后果。

## 1. 对象与正确的 unitization

沿[实际限制原稿](../adelic-relative-square/actual-restriction-and-chain-carrier.md)，
F=F_c=S_exp,C 是物理r=e^(u/2)f的卷积代数，S为偶Schwartz源且η(0)=∫η=0。
实际E_c:S→F连续单射、闭像I_c；P_c=I_c∩kerμ+∩kerμ−。
原DGA记C，C^(−1)=S，C^0=B=F⊕C²，负次数相乘为0，

\[
d\eta=(E_c\eta,-\mu_+E_c\eta,-\mu_-E_c\eta),\qquad
x_r=j_0(r)=(r,0,0),\qquad
\mu_\pm r=\int e^{\pm u/2}r(u)du.
\]

B的乘法是原稿的degree cocycle，不是裸逐分量乘法。
Φ(g,a,b)=(g,a+μ+g,b+μ−g)将B送到F×C²，并将dS送到I_c×0×0。
F不含卷积unit；δ0不属于F。现在明确添一个共同的unit，令A=C^+。
若λ1+(g,a,b)∈A^0，则

\[
\Phi^+(\lambda1+(g,a,b))=
 (\lambda1+g,\lambda+a+\mu_+g,\lambda+b+\mu_-g)
 \in F^+\times\mathbf C^2. \tag{1}
\]

这是unital代数同构；附加的λ在三个因子中共同出现。
因此

\[
H^0(A)=R=(F/I_c)^+\times\mathbf C^2,
\quad H^{<0}(A)=0,
\quad [x_r]=(\bar r,\mu_+r,\mu_-r). \tag{2}
\]

最后式的kernel恰P_c；不是I_c。A→R是unital quasi-isomorphism。
在**普通代数dg模及导出tensor**的范围内，[Stacks Lemma22.37.1](https://stacks.math.columbia.edu/tag/09S5)
给D(A)与D(R)的等价。这没有断言所有Pic群为零，也没有断言所有derived范畴都无几何。
它只说明：本A的这些代数模块操作本身没有添加超出旧R的新不变量。
带metric、Fréchet完成、整格、局部valuation及指定sheaf/site的比较没有由该定理支付。

## 2. 不用指数的具体 line 对象和源映射

对每个实际r∈F，直接在A²中定义

\[
v_r=(1,x_r),\qquad L_r=A v_r\subset A^2,
\qquad s_r=x_r v_r=(x_r,x_r^2). \tag{3}
\]

v_r闭，ι_r:A→L_r、a↦a v_r是严格dg模同构，逆为第一坐标投影。
所以L_r确为rank-one自由dg模，并非只在K群中的虚类；s_r是实际闭截面。
这给物理源到**嵌入的带标记图线**的明确映射。
若只忘记嵌入/标记而记Pic类，则所有L_r同构于A；源信息在s_r而不在线丛类上。
保嵌入数据可以区分r，但不能把这一点误称为非恒定Picard移动。

有限参数族也实际存在：选r_1,…,r_m，取A_T=A⊗C[t_1,…,t_m]，
x_T=Σt_i x_(r_i)，L_T=A_T(1,x_T)。这是有限自由族的公式，任意参数特化都成立。
没有把整个无限维源Frechet空间偷偷当成有限型scheme，也没有从此推适当pushforward或cohomology base change。

## 3. 405全主关系：严格线同构与标记同伦必须区分

若q∈P_c，则有实际η_q∈S满足E_cη_q=q及μ±q=0，故x_q=dη_q。
记y=x_q。在A²上定义严格可逆的elementary矩阵

\[
E_q=\begin{pmatrix}1&0\\y&1\end{pmatrix},\qquad E_q^{-1}=E_{-q}.
\]

它送v_r到v_(r+q)，因而给严格线同构L_r→L_(r+q)。然而它并不严格保存标记：

\[
s_{r+q}-E_qs_r=yv_{r+q}=d(\eta_qv_{r+q}). \tag{4}
\]

所以**标记之差是实际链同伦**，不是标记字面相等。
若都用全局frameι_r比较，标记正是x_r，差x_q=dη_q；反之差为boundary当且仅当q∈P_c。
在ambient A²中也有明确等式

\[
s_{r+q}-s_r=d\bigl(\eta_q,(2x_r+y)\eta_q\bigr). \tag{5}
\]

这里的精确kernel声明需要保住全局frame／第一投影。若忘掉frame而只记抽象pair(L,s)，
unit rescaling会额外识别源：例如r与2r的pair可由ι_(2r)∘(乘2)∘ι_r^−1同构。
因此未加frame的pair并不忠实参数化F/P_c，不能把它的全部isomorphism fibers说成Pan cosets。
非根结论只要求s_r0非null且不与零标记pair同构，仍然成立。

这里η_q是实际restriction源，不是除以Ξ得到的形式商。
E_q严格满足E_q E_p=E_(q+p)，故这些overlap变换也有真正的cocycle。
但同一个E_q公式对任意q∈F都给图线同构；主关系的区别只由(4)的boundary性质承担。
这正是旧405商的带标记实现，不是新principal rational function/divisor理论。

若把旧乘法同伦扩到unitization，不能漏λ项。对λ1+(g,a,b)应取

\[
K_q(\lambda1+(g,a,b))=\lambda\eta_q+U_g\eta_q,
\qquad U_g\eta(x)=\int e^{-t/2}g(t)\eta(e^{-t}x)dt,
\]

才有m_(x_q)=dK_q+K_qd。若只照抄非unital的U_gη_q，unit1处等式会失败。

## 4. 537非根、两个degree及真正Cartier门

405实际h有μ±(Ch)=1/4；其x_(Ch)在R中的第一因子为0，两个字符因子为1/4，故不是boundary。
完整Q(Ch)=0不与此矛盾：P_c、I_c和Q的trace根不同。
537的r0=(D²−1/4)ψ、0≠ψ∈Cc∞((−17/16,17/16))满足μ±r0=0、完整Q(r0)>0。
旧405恒等式即给[x_r0]≠0。因此(3)的标记在导出同伦类中保留537非根；
L_r0的未标记Pic类仍然平凡。没有用未知ζ零点位置。

还有一个更具体的限制。A中两个非零局部幂等e±在(1)下为(0,1,0)、(0,0,1)，
而

\[
x_{r_0}e_+=x_{r_0}e_-=0. \tag{6}
\]

所以即使[x_r0]非零，标记s_r0在这个**保双degree的整个base**上仍不是非零因子，
不能称为effective Cartier section。加自由graph不会修复(6)。
这是(3)这一具体mark的失败，不排另一个载体上的source-dependent线对象或virtual/relative有效性。

若局部化使x_r0可逆，两个C因子被杀；这是合法primitive处理，但丢失的pole/degree比较须另付。
若局部化一个全principal x_q=dη_q，则

\[
1=d(\eta_q x_q^{-1}),
\]

局部化DGA直接acyclic。可见“将每个源变成可逆twist”不能同时保全主关系与537。
没有断言r0本身非nilpotent或其局部化必非零；本门只用(6)的确定后果。

## 5. Base change、交叠与图线没有付出的那一步

对任意unital dg代数态射A→A′，

\[
L_r\otimes_A A'\simeq A'(1,x'_r)
\]

由自由frame直接成立，不要求flat；derived tensor也相同。
这是**模的scalar extension**，不能代替函数域proper曲线推前p_*L为line bundle的定理。
在A→R的base change后，带标记对象恰为(R,[x_r])。
任意已给开覆盖上的图线均由同一v_r平凡化，真正的线过渡函数为1。
若另换局部framea_i v_r（a_i为unit），overlap是a_i/a_j，当然满足cocycle，
但这是已有平凡线的coboundary；没有因此得到degree-zero Picard平移。

若另加一个非trivial transition cocycle，则可能构造别的line；本稿没有排除它。
但该cocycle、与r的实际比较、全Pan的兼容及原metric费用都是新输入，不能说由现有U_r已经给出。
也不能把graph family的“所有fiber自由”消费成函数域special locus的moving修复。

## 6. 原du/Dlog费用：代表元有上界，商没有免费正norm

令X为原du或zero-extension Dlog空间，Dlog²=(2π)^−1∫log(2+|t|)|rhat(t)|²dt。
实际作用在X⊕C²上由卷积及μ±给出。若supp r⊂[−L,L]，记

\[
c_L=\max\{\sqrt{2L},\sqrt{2\sinh L}\},\qquad
C_r=\max\{\|r\|_1,|\mu_+r|,|\mu_-r|\}.
\]

则||T_r||≤C_r≤c_L||r||du；改用Dlog时再除√log2。
因此图嵌入h↦(h,T_rh)的范数≤√(1+C_r²)，在其像上的第一投影逆norm≤1；
标记乘法x_r v_r的代表元费用≤C_r√(1+C_r²)。elementary E_q及其逆均≤1+C_q。
这些是具体候选在原表示中的充分上界，不是必要实际源费用或RR容量。
没有选择坏minor后把其逆的发散当成源必须支付的费用。
这个Hilbert表示只计算次数0的代表元作用；没有把d:S→B的原Fréchet链域
免费完成为一个positive closed form或全域有界Hilbert differential。

对η源，q_(a,b)(U_rη)≤q_(a,b)(η)∫|r(t)|e^((a−b−1/2)t)dt。
固定窗用Cauchy–Schwarz支付，原稿已给√(sinh(2κL)/κ)；全F要逐个带权L1。
全Pan的q通常并非compact；不能把compact费用冒充(4)所有η_q的统一du费用。
特别E_c^−1虽在原Fréchet闭像中连续，未给一个全线du/Dlog上的统一逆。

553的全principal平移稠密障碍保留：若把标记的homotopy商再赋予Hausdorff正目标且
map在全线原du/Dlog连续、精确消全Pan，就只能退化；不能由自由graph范数免费下降。
原Fréchet、fixed/变域及有费cofinal方案仍合法。本门没有将它们排除。

## 7. 指数unit和cone/determinant的两个旁门

在S_exp的带权卷积Fréchet代数中，逐半范数可核
t_r=exp(x_r)=1+Σ_(n≥1)x_r^n/n!。例如导数加权L1的第n项可由
||∂^k r||_(1,w)||r||_(1,w)^(n−1)/n!控制，故级数收敛且t_r^−1=t_(−r)。
这给严格可逆源作用，但t_r总是unit，作为自由线的mark没有零divisor。
若q=dη_q，则

\[
t_q-1=d\left(\eta_q\sum_{n\ge0}\frac{x_q^n}{(n+1)!}\right).
\]

它提供实际gauge同伦，却只在同一个平凡线中实现旧指数recipe。
指数可能有period alias；不能未经证明就称其单个mark的kernel恰Pan。
只有带标记线性x_r已在§3严格给出这个kernel。

另一个实际对象Cone(m_(x_r):A→A)是两项perfect complex，不是rank-one line。
其determinant line由两个free因子的det相消而平凡；局部化可有torsion trivialization，
但无已给的全局算术metric、局部消失过滤或容量。这也不能靠改名越过本门。

### 7.1 合法的更强修复：Koszul DGA 确实给严格相容拼接

不能由graph mark仅同伦就声称所有实际source gluing都不存在。
对每个r直接给

\[
K_r=A[\varepsilon_r],\qquad |\varepsilon_r|=-1,\quad
\varepsilon_r^2=0,\quad d\varepsilon_r=x_r. \tag{7}
\]

这是交换dg代数：x_r闭且次数0，d(ε²)=x_rε−εx_r=0。
作为A模它是有两个自由分次生成元的semifree对象；不是rank-one line。
若q∈P_c、x_q=dη_q，则有**严格的A-dg代数同构**

\[
\theta_q:K_{r+q}\longrightarrow K_r,\qquad
\varepsilon_{r+q}\longmapsto\varepsilon_r+\eta_q. \tag{8}
\]

右边微分是x_r+x_q，平方是0：两个奇次数交叉项相消，η_q²=0。
逆送ε_r到ε_(r+q)−η_q。E_c单射给η_(p+q)=η_p+η_q，
故(8)在全Pan族上严格满足overlap/cocycle；不只是标记的链同伦。
这份显式合法修复必须在停止时保留，不能把下游容量缺口泛写成“没有任何拼接”。

任意A→A′的derived base change可由普通K_r⊗_A A′计算，因为该A模semifree；
所得仍为dε=x′_r的两项Koszul对象。尤其

\[
K_r\otimes_A^{\mathbf L}R
 =\bigl[R\xrightarrow{[x_r]}R\bigr],\qquad
H^0=R/([x_r]),\quad H^{-1}=\operatorname{ann}_R([x_r]). \tag{9}
\]

这里(9)的两个次数是−1、0；A自身的负次数已由quasi-isomorphism消去。
537给[x_r0]≠0，所以H0(K_r0)=R/([x_r0])与H0(K_0)=R不可能作为R模同构：
前者annihilator是非零ideal([x_r0])，后者annihilator为0。
因此这个严格修复也保留非根见证，并非将全源都变成同一个acyclic对象。
两个degree字符在Koszul基变换下仍在R中，不能与§4的局部化杀pole混淆。

代价与范围也要同时保留。(8)的矩阵含η_q；其原源半范数和全Pan费用仍由§6负责，
semifree的代数base change不支付任何uniform du/Dlog完成。
K_r的determinant line仍由两个rank-one自由因子相消而平凡；
(9)是旧R上的standard derived zero-locus，不是函数域proper Picard twist或其相对有效divisor族。
它没有提供独立整性过滤、局部消失阶、RR/Rosati容量或完整Γ/素数幂/pole预算身份。
所以这是一项实在可行的**strict gluing修复**，但在本准入门仍是标准来源0推论；
不靠禁止该修复来停止，也不由其成立晋级未知正容量合同。

## 8. 函数域正控制、连续反控制的消费

函数域真正degree-zero twist为L↦L⊗M、M∈Pic^0(C)，并保持degree。
MilneJVs§7的非特殊开集上，H0维数恒1使proper pushforward成为line；
evaluation产生相对有效divisor，换twist后由该真实Picard族及base change拼接。
图线候选只有free rank-one scalar extension；§7.1的Koszul修复又确实给严格coherent gluing，
但两者均没有proper曲线、RΓ的special jump、
Picard translation或同一effective family。因此它没有实现上一轮genus2 special/excess的修复来源。
这不是否定module语言能够表达线丛，而是逐项列出这里未构造的对象。

旧连续正反R_d=C[z]/(z²+d)、z†=−z在d=±1/16均可逐字作(3)：
v=(1,x)、L=R_d v，scalar extension与elementary overlap完全同样成立。
但既定目标Tr(a a†)=2|A|²+2d|B|²的符号不同。
因此graph/free/base-change/cocycle这些设施没有区分正反模型；不能把其module范数换成目标Weil型。
这里不宣称这两个连续g分布已有实际经典adeles；它们是本候选的代数充分性反控制。

## 9. 完整目标与停止

经典要比较的始终是同一物理r的

\[
\begin{aligned}
Q_W(r)={}&2\Re(\mu_+r\,\overline{\mu_-r})+
 [\psi(1/4)-\log\pi]\|r\|_2^2\\
&+\tfrac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}
       \|\tau_vr-r\|_2^2dv\\
&-2\sum_{p,k\ge1}(\log p)p^{-k/2}
       \Re(r*r^*)(k\log p),\quad r^*(u)=\overline{r(-u)}.
\end{aligned}
\]

Γ/contact、全部proper powers、双pole及全mixed都未删；但本候选没有把任一片识别为
同一整模型截面的局部消失/高度/RR缺陷，更没有三者协同的signed容量身份。

本来源门给出了具体line、actual source map、全Pan同伦、base change与overlap，
并保留§7.1真正可行的Koszul strict gluing修复；它们仍回到旧marked商／指数／derived zero-locus，
按用户止，不扩成未知RR合同。
仍欠的独立输入是：

1. 不是按[x_r]换名的真实非平凡line/对应族，及物理源到它的保全关系比较；
2. 该同一对象的proper或有费相对pushforward、特殊点moving/descent、局部整性/消失过滤；
3. 相对ample/RR/Rosati的独立mixed容量正号及原du/Dlog/cofinal费用；
4. 该容量的primitive二次系数与上式完整预算的身份和误差。

这些可由新几何／新有费relative增强给出，不能由“某个正metric存在”或“容量等于Q且非负”定义。
本门不排所有Pic、所有derived、所有连续系统或更小原域；也不更新strong-old4/5、core/coupling/Ξ及Goal完成门。
