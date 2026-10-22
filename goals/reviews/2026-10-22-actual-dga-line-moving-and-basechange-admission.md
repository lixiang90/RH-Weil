# 实际 adelic 相对 DGA 的线对象、换底与拼接：本次准入结论

2026-10-22。执行[新路线图§8](2026-10-22-generalized-weil-roadmap-after-573.md)及用户指定门。
沿同G20261014/冻结0c4f。以下是已有实际DGA的标准模块构造、具体原域费用和函数域来源比较；
不新建C037，不编号574，不把旧商的线对象或Koszul表达重新计数学轮。
当前原cadence2、正式cycle14保持；独立逆审/root消费另留记录。

## 1. 结论先分清三个层次

**具体线对象和物理源映射可以给出；全部405关系、537非根、普通换底和相容拼接也能在准确意义下实现。**
一个非指数的实际候选是自由图线及标记。更强的Koszul候选甚至把主关系实现成严格协同的DG同构。
因此不能继续将缺口泛称为“没有线对象”或“没有任何拼接”。

但这些候选尚未实现函数域的**非平凡degree-zero线丛张量移动**。
图线的Pic类恒定；Koszul复形的行列式线恒定，换到同调代数后仍是旧源商上的标准零点复形。
按用户停止条件，本入口到此收口：没有独立算术容量、经典新Weil正性或whole/core净后果。
这不声称所有非自由模、相对层、derived几何或非仿射增强均不可能。

## 2. 固定实际 DGA 与正确单位化

用[已有构造](2026-10-22-adelic-restriction-relative-square-and-quadratic-capacity.md)：
F=F_c=S_exp,C为物理r=e^(u/2)f的卷积空间，S为η(0)=∫η=0的偶Schwartz源。
E_cη(u)=e^(u/2)2Ση(ne^u)，I_c=E_cS为已付闭像，
P_c=I_c∩kerμ+∩kerμ−为physical 405全主关系。原DGA C有

\[
 C^{-1}=S,\quad C^0=B=F\oplus\mathbf C^2,\quad
 d\eta=(E_c\eta,-\mu_+E_c\eta,-\mu_-E_c\eta).
\]

B使用已给degree-cocycle乘法；Φ(g,a,b)=(g,a+μ+g,b+μ−g)将它送到F×C²。
令A=C^+，明确增加一个unit，不把δ0当F内函数。则

\[
 A^0\simeq F^+\times\mathbf C^2,\qquad
 R=H^0(A)\simeq(F/I_c)^+\times\mathbf C^2,
 \quad H^{<0}(A)=0.
\]

对λ1+(g,a,b)，三个坐标为(λ1+g,λ+a+μ+g,λ+b+μ−g)。
写x_r=(r,0,0)∈A^0，则

\[
 \bar x_r=([r],\mu_+r,\mu_-r),\qquad
 \ker(r\mapsto\bar x_r)=P_c.                         \tag{1}
\]

A→R的quasi-isomorphism在普通代数DG模范畴给derived equivalence，
核[Stacks22.37.1](https://stacks.math.columbia.edu/tag/09S5)。
这不是Fréchet完成、正度量、整格或filtered sheaf的等距比较；也不计算或宣称Pic(R)=0。

## 3. 非指数的实际线对象与全主关系

定义

\[
 v_r=(1,x_r),\quad L_r=A v_r\subset A^2,
 \qquad s_r=x_rv_r=(x_r,x_r^2).                      \tag{2}
\]

这是严格自由rank-one DG模：a↦a v_r的逆是第一投影，v_r和s_r均闭。
物理源先进入带frame/标记的图线；未标记L_r的Pic类对所有r均平凡。
若只记抽象pair(L,s)，unit rescaling还会额外识别不同源，例如r与2r。
所以(1)的精确线性kernel属于**保frame的标记同伦类**，不能冒领为所有抽象pair的同构纤维。

对任意q∈P_c，已有实际唯一η_q满足E_cη_q=q，且x_q=dη_q。
令y=x_q，有严格可逆变换

\[
 E_q=\begin{pmatrix}1&0\\y&1\end{pmatrix},
 \quad E_qv_r=v_{r+q},\quad E_qE_p=E_{q+p},
\]
\[
 s_{r+q}-E_qs_r=yv_{r+q}=d(\eta_qv_{r+q}).          \tag{3}
\]

因此线严格同构，标记则相差实际同伦；它们不是字面相等。
这覆盖整个P_c，不止一个405见证或compact域内的空交。
乘法同伦在unit上须补K_q(1)=η_q：
K_q(λ1+(g,a,b))=λη_q+U_gη_q，不能只抄非unital公式。

405的h仍保μ±(Ch)=1/4，而537的r0=(D²−1/4)ψ、支撑于17/16窗、μ±=0，
由旧完整显式公式及537正性给\(\bar x_{r_0}\ne0\)。因此标记保留非根，未使用未知零点位置。
但L_r0未标记仍平凡；“源可见”没有变成“Pic类移动”。

## 4. 合法的更强修复：Koszul对象确实有严格拼接

不能仅凭图线平凡就排掉所有模块操作。实际可另取

\[
 K_r=A[\epsilon_r],\quad |\epsilon_r|=-1,\quad
 \epsilon_r^2=0,\quad d\epsilon_r=x_r.               \tag{4}
\]

其底DG模有限semi-free，是两项perfect/Koszul对象，**不是rank-one线**。
对全q∈P_c，令

\[
 G_q:K_{r+q}\longrightarrow K_r,
 \qquad\epsilon_{r+q}\longmapsto\epsilon_r+\eta_q.   \tag{5}
\]

d(ε_r+η_q)=x_r+x_q，且奇次交换符号及η_q²=0保证平方仍零；逆用−η_q。
E_c单射使η_(q+p)=η_q+η_p，所以这些严格DG同构满足协同复合。
这是一项真实付清的拼接；不存在“第二腿自动闭首腿”那种573误读。

有限semi-free还给任意DG换底A→A′的derived scalar extension。
特别A→R后，(4)就是标准

\[
 [\,R\xrightarrow{\bar x_r}R\,],\qquad
 H^0(K_r)=R/(\bar x_r).                              \tag{6}
\]

537的\(\bar x_{r_0}\ne0\)使该H0与K_0的R作为R模不相同：前者annihilator包含非零x_r0，后者annihilator为0。
但(6)也准确说明它仍是旧源商的derived zero-locus表达；主关系的(5)在R上变为恒等。
det K_r由两个free因子相消，行列式线恒平凡；有源依赖的微分/行列式截面不等于非平凡Pic移动。
新整格、度量、局部过滤与容量未由这个标准复形生成。

## 5. 换底和交叠：实际做到了什么

有限源族r(t)=Σt_i r_i可用A⊗C C[t_1,…,t_m]及x(t)=Σt_i x_(r_i)给出。
(2)、(4)、(3)、(5)均为显式族公式，参数特化相容；没有将无限维Fréchet源空间冒充有限型scheme。

对任意A→A′，L_r⊗A A′≅A′(1,x′_r)，由free frame直接成立，无flat前提。
若在R的任意开覆盖上使用这个frame，transition为1；另换unit frames a_i v_r，
transition a_i/a_j是coboundary，虽合法满足三重交叠，却没有新增Pic类。
任意局部cocycle不一定是coboundary；这里只结算本候选实际给出的cocycle。

模的scalar extension不同于函数域proper曲线上的R q_*与special locus控制。
代数quasi-isomorphism不阻止将来添加有用几何，但不能独自赋予proper pushforward、
局部valuation、Cartier有效性或primitive RR；completed tensor和原norm比较也须另付。

## 6. Cartier与可逆化的具体边界

两个非零degree幂等e±保留在A及R中。双pole-zero的r0满足

\[
 x_{r_0}e_+=x_{r_0}e_-=0.                            \tag{7}
\]

因此s_r0虽非null，却不是**整个保degree base**上的regular Cartier截面。
局部化令x_r0可逆会去掉这两个因子；允许primitive局部处理，但全pole协同及复原不能免费。
局部化principal x_q=dη_q则有1=d(η_q/x_q)，所得DG代数contractible。
这些只描述该指定可逆化，不排source-dependent covers、相对Cartier或另一载体。

另一个非指数候选1+t x_r并不总在原A0中可逆。
取r0=(D²−1/4)ψ、ψ≥0 compact非零，则∫r0=−∫ψ/4；
在t*=4/∫ψ时，原F^+的积分character送1+t*x_r0到0。
所以不能把每个此类元素都称global unit。
**该character未声称下降到R**，这里没有证明同调商中它非unit，更没有给逆的必要费用下界。
旧exp(x_r)可作global unit，但只回旧指数；不继续优化其参数。

## 7. 原du/Dlog费用及同伦的范围

令X=H⊕C²，H为原du或zero-extension Dlog空间，
Dlog²=(2π)^−1∫log(2+|t|)|rhat(t)|²dt。
次数0代表作用为T_r=diag(conv_r,μ+r,μ−r)。supp r⊂[−L,L]时，

\[
 M_r:=\|T_r\|\le\max\{\|r\|_1,|\mu_+r|,|\mu_-r|\}
 \le\sqrt{2\sinh L}\,\|r\|_{du}.                    \tag{8}
\]

Dlog右侧再除√log2；μ±=0时可用√(2L)。
在此表示中，图frame及投影费用≤√(1+M_r²)，mark列费用≤M_r√(1+M_r²)，
E_q及逆费用≤1+M_q。所有这些都是原代表元的充分上界。

**T不是整个DG/H0商的正表示**：Pan的T_q在原H上可非零，同伦使用原Schwartz负次链域。
因而(8)不能下降为正商norm、等距源lift或RR容量。
对该负次链域，仍须付

\[
 q_{ab}(U_r\eta)\le q_{ab}(\eta)
       \int|r(t)|e^{(a-b-1/2)t}dt.                    \tag{9}
\]

固定窗的Cauchy–Schwarz费用见旧DGA原稿；全P_c用逐个η_q的Fréchet半范数，
不声称E_c^−1有全线du/Dlog统一逆。(5)的严格拼接没有消除这项费用。
更具体地，固定一个实际非零q=E_cη_q∈P_c，其全平移q_v=τ_vq的唯一源为
η_(q,v)(x)=e^(−v/2)η_q(e^(−v)x)，故

\[
 \|q_v\|_{du/Dlog}=\|q\|_{du/Dlog},\qquad
 q_{ab}(\eta_{q,v})=e^{(a-b-1/2)v}q_{ab}(\eta_q).
\]

这给本指定实际源lift在原域上的确切费用；可沿一个平移方向增长。
它不构成其他几何lift的必要下界，亦不排固定窗/变域修复。
553的全Pan平移稠密障碍仍适用；Fréchet、固定/变域、非线性族及有费cofinal仍保留。
没有用ambient最坏逆或某个坏minor作实际源必要费用。

## 8. 函数域正控制：真正的twist改变什么

在已核C/F5:y²=x⁵−x+1上，P=(0,1)、Q=(1,1)，M=O(2∞)≅K，取

\[
 L_0=O(P+Q-2\infty),\quad\deg L_0=0.
\]

canonical评价系数矩阵\(\begin{pmatrix}1&1\\0&1\end{pmatrix}\)有det1，
所以H0(K−P−Q)=0，RR给h0(M⊗L0)=1；而h0(M)=2。
因此L0非平凡，global unit无法完成这种twist。
非平凡degree-zero线本身h0=0：若有非零截面，其有效零除子degree0，只能处处生成。
所以必须先加正degree基准M再有效化，不能要求L0本身有非零截面。

在T⊂C×C的finite-point且x(P)≠x(Q)开集上，
N=O(Γ_P+Γ_Q)、L=N⊗p*M^−1是实际相对族。
每个fiber h0(N)=1、h1(N)=0，proper曲线投影q使q_*N为line且任意base change相容；
evaluation给相对degree2 Cartier除子。这里有实际曲线、截面与proper比较，不是单纯scalar extension。

[Milne JVs §7 Thm7.6](https://www.jmilne.org/math/xnotes/JVs.pdf)对一般special fiber换degree-zero L_i，
取good chart后用Picard平移校正；一致的是校正后的J-map。
不同有效除子或sections未必字面相等，具体线丛/metric下降还要记base-line与overlap同构。
本F5正控制原域上存在；一般generic选择的有限扩张/下降责任另保留。
μ±的复字符也不是已识别的整值线丛degree，不能直接混用。

## 9. 连续正反控制：模块设施不能支付符号

用已付真实positive g-distribution族Z_c=1+c/[s(s−1)]，d=c−1/4=±1/16。
完整primitive实现R_d=C[z]/(z²+d)、z†=−z，a_r=∫r(u)e^(uz)du给

\[
 Q_c(r)=\operatorname{Tr}(a_ra_r^\dagger)
       =2|A_r|^2+2d|B_r|^2.
\]

两段的普通复代数均为C⊕C；free graph、Koszul、scalar extension与unitriangular变换均可作。
取g=uφ，φ非负偶compact、支撑|u|<1，r=(D²−1/4)g，仍双μ=0。
源侧积分给A_g=0、B_g>0，且a_r=−(d+1/4)a_g，所以该完整型在两段为相反严格符号。
这是旧完整Π/双pole模型；Γ=0为其指定背景，没有伪造经典adeles或给模型删Γ。

因此即使把关系、源map和形式拼接付清，正号仍需一个两段有实际区分力的独立输入。
保持原实对偶很重要；不能用任意Hilbert正norm替换既定Weil配对。
[精确脚本](../../scripts/dga_line_moving_controls.py)及[输出](../../reviews/2026-10-22/dga-line-moving/exact-controls.json)
核图投影、transport、mark同伦的普遍多项式身份和有限矩阵控制；不认证全局Picard族或经典RH。

## 10. 完整经典预算与独立容量缺口

目标仍是同一physical r的完整式

\[
\begin{aligned}
Q_\zeta(r)={}&2\Re(\mu_+r\,\overline{\mu_-r})+
 [\psi(1/4)-\log\pi]\|r\|_2^2\\
&+\tfrac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}
       \|\tau_vr-r\|_2^2dv\\
&-2\sum_{p,k\ge1}\log p\,p^{-k/2}
       \Re(r*r^*)(k\log p).
\end{aligned}
\]

本门没有新证明：(i)Γ/contact来自同一截面的arch容量；(ii)每个p^k是该对象的整性消失阶；
(iii)双pole是同一RR缺陷；(iv)这三片协同产生目标primitive mixed二次系数及可控成长误差。
形式上已给正metric、trivial determinant、严格gauge或标准Koszul，不支付这些身份。

需要的新输入应是：实际非平凡relative Pic/Cartier/对应族及physical比较；
同一模型的整格、消失过滤和proper或有费用的相对pushforward；
独立有效性/ample mixed交数或有误差RR容量；最后是该二次预算与上式的完整比较。
允许使用旧解析identity做最后比较；不允许按Q定义正metric再宣称独立来源。

## 11. 停止、净后果与下一次准入

本门已给具体line和source，核全Pan/537/原费，并保一项严格coherent Koszul修复。
结果仍回旧framed商/derived zero-locus；按用户要求停止，不调图线、指数、localization或jet参数，
不串下一篇paper、不建未知RR合同。
准入检查改变的是：scalar base change和某些严格拼接确已支付，不能再作为笼统缺口；
真正还欠非平凡可移动几何及独立容量。经典瓶颈未移除。

strong-old542+555→557 whole leading4/5的负惯性上预算保持；它不是实际负谱下界。
core/coupling/Ξ与长期完成门不变。既有573限430扩大A的反测也未扩成所有relative方法失败。
这次是标准模块/旧推论的具体来源门，0新增轮；没有新574/C037或运行Goal。

下一只验收实际新数据：给出区别于本门free/unit/Koszul包装的非平凡relative对象，
以及源到它的map/全关系/原费用和至少一项独立过滤或capacity数据。
没有该数据就不续此入口；独立tensor对象/pole定理或actual危险核心全源signed估计出现时再改排序。
这不是预建未知合同，也不宣称合法source-family、强拓扑、非自由/非仿射及有费无限修复已被排。
