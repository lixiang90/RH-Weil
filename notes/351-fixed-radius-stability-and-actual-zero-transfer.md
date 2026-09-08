# 351. 固定邻点半径的稳定性与实际零点传递

2026-09-08。[T/R]候选，待独立复核。
本篇将349的有限全域证书接入同一组实际简单临界线零点；
所需算术输入仅是已核读的固定平滑全谱二阶公式。
没有给出新的全域alpha、eta证书，因此尚无新的实际零点比例。
不将本篇有限稳定性或已知二阶接口的扩展登记为整个GOAL完成。

## 1. 目标定理与固定参数

固定整数R>=1、有限组实偶L²概率密度p_j（支撑I=[-1/2,1/2]）、
非负权theta_j且sum theta_j=1。令Q和P_mix如348，
核k_j(x)=integral_I p_j(u)exp(ixu)du。
若有0<=alpha<1、eta>=0及有界h，使349式(3)对所有非负gap成立，
则对实际zeta零点，无RH假设地有
\[
 \liminf_{T\to\infty}{s(T)\over N(T)}
 \ge p_*:={P_{\rm mix}-\eta\over1-\alpha},\qquad
 \liminf_{T\to\infty}{D(T)\over N(T)}\ge{1+p_*\over2}.          \tag{1}
\]
N是0<Im rho<=T的总重数，s只计简单且在临界线的零点，D计不同零点。
R、窗口数、权重、alpha、eta、h均固定，不随T增长。
这是有限几何证书的条件接口，不要求新增RH或高矩条件；
有限全域证书本身还需证明，不能仅由周期必要条件获得。

## 2. 用L⁴逼近制造合法平滑窗口

对每个p_j，sqrt(p_j)为I上的实偶L⁴函数。
取实偶eta_(j,delta)∈C_c^infty((-1/2,1/2))在L⁴中逼近sqrt(p_j)，
再归一化其L²范数为1。紧支撑光滑函数的稠密性及偶对称平均保证可取；
归一化因子趋于1。令p_(j,delta)=eta_(j,delta)²，则
\[
 \|p_{j,\delta}-p_j\|_2\to0,\qquad
 \epsilon_{j,\delta}:=\|p_{j,\delta}-p_j\|_1\to0.
\]
由有限支撑、Hölder及平方差恒等式得到以上收敛；不要求p_j光滑或处处正。
于是Q(p_(j,delta))趋于Q(p_j)，
P_delta:=2-sum_j theta_j Q(p_(j,delta))趋于P_mix。
实轴上全域一致有|k_(j,delta)(x)-k_j(x)|<=epsilon_(j,delta)，
两核的模均<=1；不对增长复带声称同一误差。

## 3. 逐边误差仅为O_R(s epsilon)

对d,e>=1，c(d,e)=2/sqrt(de)-1/(de)，有0<=c<=1。
置t=(de)^(-1/2)，直接求导得
\[
 |\partial_dc|={t(1-t)\over d}\le1/4,\qquad
 |\partial_ec|\le1/4.                                        \tag{2}
\]
对同一条完整有限R邻点图，若两个核实轴相差至多epsilon，
每个度相差至多2R epsilon，因为绝对值及max(1,.)都是1-Lipschitz。
每条无序边的贡献2|k|²c的差因此至多
\[
 2\{2\epsilon+(1/4)(4R\epsilon)\}
                =(4+2R)\epsilon .
\]
全图无序边数至多Rs。令
\[
 L_R=4R+2R^2,\qquad e_\delta=L_R\sum_j\theta_j\epsilon_{j,\delta},
\]
则完整图下界的混合误差至多e_delta s，且e_delta趋于0。
无gap上界、最小间距或矩阵阶数误差假设；重复节点也被此界覆盖。

对平滑核的实际Gram应用347的合法度归一化对偶，
再把图下界与原核的完整图下界比较。
原核通过349的全域证书给下界，故
\[
 J_\delta:=\sum_j\theta_j\operatorname{tr}\Psi(G_{j,\delta})
 \ge(\alpha-e_\delta)s-{\eta\over2\pi}(x_s-x_1)-C,\quad
 C=3R\alpha+2\|h\|_\infty.                                   \tag{3}
\]
s=0时取跨度零，(3)右侧=-C仍成立。
我们只比较图的至多Rs条边，没有比较全稠密Gram的算子范数。
因此(3)直接适用于任意增长s，只有一个全链端点C；
没有采用分块，所以不产生C ceil(s/b)的额外端点数。
这不取消347–349在采用固定块路线时必须计入该成本的要求。

## 4. 同一实际算子与共同重数账本

对每个固定delta、每个j，按304§5.2或309§1，用实际全部零点构造
自伴有限算子A_(j,T,delta)，有精确迹N及
\[
 H_{j,\delta}:=\|A_{j,T,\delta}\|_{\rm HS}^2
             =(Q(p_{j,\delta})+o_{j,\delta}(1))N.              \tag{4}
\]
简单特征Gram为同一组s个简单临界线零点上的
k_(j,delta)((gamma_a-gamma_b)log T)，故这里x_i=gamma_i log T，
(x_s-x_1)/(2pi)<=T log T/(2pi)=N+o(N)。
这是exp(ixu)坐标；不要与304的gamma log T/(2pi)位置直接混用。

(4)使用固定平滑全谱二阶公式。它取自
[Lamzouri v1 §3 Lemma3.2证明](https://arxiv.org/html/2609.02882v1#S3)，
其中同一个Q_delta与Q_delta''分别应用固定函数的BGST Lemma5以去权。
本轮重读了该一般固定函数步骤及
[BGST 2501.14545v3 §3](https://arxiv.org/html/2501.14545v3#S3)
保留旧Lemma5的勘误脚注和前缀式(3.5)。
没有导入后者窄箱比例假设或直接使用其移动区间式替代前缀。
原PDF已归档，本轮仅补核读范围，不覆盖原件。

若实际不同重复实点有r个、非实共轭对有k对，
共同b=r+k满足N>=s+2b、D>=s+b，且每个A_j去掉简单特征后的正惯性至多b。
304-B逐窗应用后用theta_j加权，得到
\[
 4N-\overline H_\delta\le4b+3s-J_\delta,\qquad
 \overline H_\delta=\sum_j\theta_j H_{j,\delta}.
\]
相同计数只加权一次，算子不必在同一个Hilbert空间里相加。
据共同账本分别得到
\[
 s\ge2N-\overline H_\delta+J_\delta,\qquad
 2D\ge3N-\overline H_\delta+J_\delta.                           \tag{5}
\]
第二式不能仅由第一式和一般计数关系推出。

## 5. 先固定平滑再取极限，含alpha=0边界

联立(3)–(5)，对每个固定delta有
\[
 (1-\alpha+e_\delta)s\ge(P_\delta-\eta)N-C+o_\delta(N).
\]
由于1-alpha>0，先令T趋无穷，再令delta趋0，得到(1)的简单零点结论。
过程中从未取delta=delta(T)，也不需要关于增长平滑导数的统一算术界。

不同点计数满足
\[
 {2D\over N}\ge1+P_\delta-\eta
              +(\alpha-e_\delta){s\over N}-C/N+o_\delta(1).
\]
若alpha>0，充分小delta使alpha-e_delta>=0，代入上述简单比例下界，
再取两极限，右端趋向1+P_mix-eta+alpha p*=1+p*。
若alpha=0，则用0<=s/N<=1处理负系数：
(-e_delta)s/N>=-e_delta。两极限仍给1+P_mix-eta=1+p*。
这完成(1)，没有误用一般不成立的D>=(N+s)/2。

## 6. 当前接口状态

对固定半径及有限偶L²窗口集合，349式(3)若有完整证明，
本篇提供其实际算术传递；因此不应继续把增长矩阵近似作为额外未证预算保留。
真正未解的是能产生净增益的全域势证书，及更新前沿后的新颖性／数值比较。
350的周期二次型上限仍仅限所列方法类，不因本篇接口而变成实际零点上界。
R(T)增长、无限窗口族或不同非稀疏对偶仍需重新证明误差控制。
