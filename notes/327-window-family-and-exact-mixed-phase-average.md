# 327. 窄范围变窗的统一二阶公式与近混合相位平均

2026-09-06。NEXT.cycle4的候选推导，[T，待独立逆审]，不声称实际覆盖。
新信息是窗口相位真正变化；变窗后的每个算子都保留同一实际前缀的全部原始零点及重数。
本篇不把不同窗口的R当成320中的一个R。

## 1. 统一算术接口与质量成本

L=log T，0<=y<=H(T)，H->infinity、H=o(L)，A_y=(L-y)/2，q=1-y/L。
对每个y使用原sharp MT密度eta_A²(u)=cos(bu/A)/(2A sinc b)，b=1/sqrt2。
实际算子记mathsf A_y=P_y-N_y，tr mathsf A_y=N(T)、rank<=N(T)。

在v=u/L坐标，密度f_q(v)=q^(-1)f0(v/q)，Q_q=f_q*f_q=q^(-1)Q0(v/q)。
其支撑为[-q,q]；D²Q_q是总变差q^(-2)||D²Q0||TV的有限测度。
对最终q>=1/2，324的去权恒等式、Lipschitz界、原始BGST公式均对q一致；支撑没有超过[-1,1]。
因此令B0=Q0(0)、B1=integral |v|Q0(v)dv，得到
\[
 \operatorname{tr}\mathsf A_y^2
 =\left(q^{-1}B_0+qB_1+O(L^{-1/2})\right)N(T),              \tag{1}
\]
误差对0<=y<=H一致。这里D²Q_q中的所有原子照常保留。
B0+B1=C_MT，所以右端系数为C_MT+O(H/L+L^(-1/2))。
任何正收缩R_y仍有||R_y mathsf A_y R_y||HS<=||mathsf A_y||HS<<sqrt(TL)。

令kappa=cos b/(2 sinc b)>0，固定d in [s,1/2]，s>0。
同一端点Laplace估计一致给负向量范数
\[
 \mathcal H_{d,y}=\|h_{d,y}\|^2
 ={ \kappa\over 4d A_y}e^{2dA_y}(1+O_s(A_y^{-1}))
 ={ \kappa\over 2d(L-y)}T^d e^{-dy}(1+O_s(L^{-1})).         \tag{2}
\]
变窗质量最坏损失为e^{-dH}=T^{-o(1)}，可以保留T幂比较；
它一般不是1-o(1)，不能用于声称固定比例质量无损。
本节是324算术接口的统一参数推论，非新的高阶算术估计。

## 2. 从原积分求精确混合核

忽略共同高度平移。取深度e、d的g和h，中心差Delta为g中心减h中心。
内积约定先线性于g；实型内积为以下实数。定义
\[
 I_A(z)=\int_{-A}^{A}\eta_A(u)^2 e^{zu}\,du
 ={z\sinh(zA)\cos b+(b/A)\cosh(zA)\sin b
       \over A\,\operatorname{sinc}b\,\{z^2+(b/A)^2\}}.      \tag{3}
\]
右端在可去奇点处按左端连续延拓，I_A(0)=1。则
\[
 G_{e,A}={I_A(2e)+1\over2},\qquad
 \mathcal H_{d,A}={I_A(2d)-1\over2},
\]
\[
 \langle g_{e,\Delta},h_{d,0}\rangle
 ={1\over2}\Im\{I_A(e+d+i\Delta)+I_A(d-e+i\Delta)\}.         \tag{4}
\]
(4)由cosh(eu)sinh(du)=[sinh((e+d)u)+sinh((d-e)u)]/2得到；
高度调制的正弦号随内积约定可整体变号，以下平方结论不受影响。
Delta=0时混合内积严格为0，不能用非零频率平均覆盖它。

归一化Theta_A=inner/sqrt(G_e H_d)，p=e+d。对固定B<infinity，
d,e in [s,1/2]、|Delta|<=B、A->infinity，一致有
\[
 \Theta_A(\Delta;e,d)
 ={2\sqrt{ed}\over p^2+\Delta^2}
       \{p\sin(\Delta A)-\Delta\cos(\Delta A)\}
       +O_{s,B}(A^{-1}).                                  \tag{5}
\]
证明：从(3)的p+iDelta项取右端指数，得到
I_A(p+iDelta)=kappa e^((p+iDelta)A)/(A(p+iDelta))(1+O_s,B(A^-1))。
其余d-e项用原积分绝对值<=exp(|d-e|A)，除以主范数后至多O_s(A exp(-2sA))。
G_e、H_d各取(2)的同类主项；p>=2s使主项分母一致远离0。
这样即使d=e或d-e很小，也没有对次项的可去奇点错误求逆。

## 3. 平方平均产生正的主项

对Delta!=0，由(5)及正弦平方积分，
\[
 {1\over H}\int_0^H|\Theta_{A_y}(\Delta;e,d)|^2\,dy
 ={2ed\over(e+d)^2+\Delta^2}
  +O_{s,B}\left({1\over H|\Delta|}+{1\over L-H}\right).      \tag{6}
\]
该式的有用范围是H|Delta|->infinity；允许Delta随T变动且|Delta|<=B。
此时主项有依s、B的正下界，平方平均不是o(1)。
这是同一实际核的恒等式／一致渐近，不需要假造另一套零点模型。

若|Delta|<=C/L，H=o(L)使整个变窗带的相位变化为o(1)，此时反而有
\[
 {1\over H}\int_0^H|\Theta_{A_y}|^2\,dy
 ={4ed\over(e+d)^2}\sin^2(\Delta L/2)
      +O_{s,C}(H/L+L^{-1}).                               \tag{7}
\]
平均保留原来的微观相位，仍不自动变小。Delta=0单独按严格零处理；
Delta L趋于非零2pi倍数时主项也可趋零，不能由(7)推出所有近点都有正泄漏。
介于两种尺度之间的节点同样须保留具体相位，不能用“平均抵消”跳过。

## 4. 原始节点权重不能省略

对单点目标j，深度d、原始重数m_j，目标负质量W_j(y)=2m_j H_{d,y}。
任一未选中近深节点w深度e、原始重数m_w，对实际正Rayleigh泄漏的贡献精确为
\[
 {2m_w G_{e,y}|\Theta_{A_y}|^2\over W_j(y)}
 ={m_w\over m_j}{G_{e,y}\over H_{d,y}}|\Theta_{A_y}|^2.       \tag{8}
\]
G_e/H_d=(d/e)T^(e-d)exp(-(e-d)y)(1+O_s(L^-1))。
若e>=d、|Delta|<=B且H|Delta|->infinity，由非负性、(6)和区间最小权，
\[
 {1\over H}\int_0^H {2m_w G_{e,y}|\Theta_{A_y}|^2\over W_j(y)}\,dy
 \ \ge c_{s,B}{m_w\over m_j}T^{e-d}e^{-(e-d)H}.             \tag{9}
\]
因此同深度、可比较重数的这样一个实际邻点若存在，就阻止该目标的平均正泄漏为o(1)。
若e-d>=delta>0且m_j<=C L、m_w>=1，右端至少T^(delta-o(1))/O(L)，更不可能小。
没有在这里证明实际存在这样的邻点；结论是精确的必要条件，不能变成实际RH反例。

(9)只否定“以这类正泄漏预算的平均小量作为覆盖证明”的充分条件。
mathsf A_y中的所有负列仍在；可能利用近节点自己的负贡献、选取特殊y、
多方向带符号抵消或新的算术节点信息。平均为正不排除某个y恰好很小，
也不证明完整算子响应不存在。

## 5. 本候选状态

变窗统一二阶接口合法；未经独立逆审前仍保留待审状态。
平方相位的平均并不提供所需小量，微观相位也不会被H=o(L)自动打散。
所以不能凭窗口平均启动免费覆盖推论；实际覆盖仍需独立信息。
这构成当前有限动作的停止证据，未达到GOAL第十节C。
