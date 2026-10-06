# 436. 源平均范数极限的真实物理迹与两次极限不交换

2026-10-06。接续[433](433-f1-source-cesaro-limit-and-noncompact-fixed-sector.md)、
[434](434-f1-haar-physical-cutoff-on-the-source-domain.md)和[435](435-f1-haar-trace-of-all-source-conjugates.md)。
本稿在同一原Haar物理截止上计算完成源平均，给出无单位项干扰的原素数周期不连续见证。
另支付固定物理截止的迹范数收敛，故两次标量极限的差异是实际计算，而非形式交换。

## 1. 真实完成平均的行及端质量

仍取原c、d、L、M、rho、V、u。置F=(1-e)V、Z=eV，并记
\[
 X(h)=FU(h)F^*,\quad A_r(h)=u^rA(h)u^{-r},\quad
 C_N(h)=\frac1N\sum_{r=1}^N A_r(h).                       \tag{1}
\]
433已证明C_N(h)在算子范数中趋于X(h)，误差O_h(N^(-1/2))；
X(h)属于真实最小源理想J。这里继续计算其实际原球压缩。

F的原波形行准确为
\[
 (F\phi)_{j,k}(t)=
 \left[c(t)\delta_{k,0}\{\mathbf1_{j<0}-a_p(t-jL)\}
       +\mathbf1_{k<0}d_j^F(t)\right]\phi(t-jL-kM),       \tag{2}
\]
其中
\[
 d_j^F(t)=\delta_{j,0}d(t)-c(t)f(t-jL),\qquad f=cd.      \tag{3}
\]
第一项仅有有限个p标签；第二项是有限p宽、无限负q条带。输出t始终在固定紧集。
平方展开及原平方分割给
\[
 \sum_j d_j^F(y+jL)^2=d(y)^2-f(y)^2,\qquad
 \sum_j\int d_j^F(t)^2dt=W=M-\int f^2.                   \tag{4}
\]
有限p残边的总时间能量为
\[
 J_p=\sum_j\int c(t)^2\{\mathbf1_{j<0}-a_p(t-jL)\}^2dt
     =\int a_p(x)(1-a_p(x))dx.                           \tag{5}
\]
该积分有限；a_p在两端分别为0、1。残边与q条带的径向支撑分别在k=0、k<0。

## 2. 原球压缩的精确迹

由(2)–(3)的有限p支撑和q球ell¹尾，434的紧支光滑时间核证明同样支付
P_K X(h)P_K in S₁。这里也可用F=V-eV及原e的有限物理Γ箭头展开；不以范数极限推断迹类。
对充分深K_p、K_q，有限p支撑全部可见，p逃逸球和双球均取不到F。
可见波形矩形给(K_q W+J_p)h(0)。q逃逸球由(4)及原几何自相关给完整q轴周期。
因此准确有
\[
 \boxed{\operatorname{Tr}(P_KX(h)P_K)
       =K_qW h(0)+J_p h(0)
        +W\sum_{b\in\mathbb Z}\rho_q^{|b|}h(-bM).}       \tag{6}
\]
全部源混合已在(3)–(4)计算；没有p周期项。
若扣掉该算子实际具有的K_qW体积，有限部为
(J_p+W)h(0)+W sum_(b!=0) rho_q^|b| h(-bM)。
原A的(K_pL+K_qM)体积不能原样扣到X上；本稿未将另一体积扣除指定为规范算术读出。

## 3. 固定物理截止的更强迹范数收敛

需要另证固定K时可把r或N极限送入压缩迹。令E_r=u^rZ；则
u^rV=F+E_r。E_r的行由434的(5)减去(2)，准确为
\[
 (E_r\phi)_{j,k}(t)=c(t)
 [\delta_{k,r}a_p(t-jL-rM)+\mathbf1_{k<r}f(t-jL-rM)]
 \phi(t-jL-kM).                                        \tag{7}
\]
所有非零p标签满足j<=-rM/L+C，C只依原紧支；水平边k=r向负p延伸，
q条带具有一致有限p宽、k<r。固定物理K，当r充分大时这些p标签均在-K_p以下，
P_p将它们全压到434的唯一逃逸球。对广义平面波e_xi(x)=exp(i xi x)，
球系数的几何和及条带可见q标签的数目给
\[
 \|P_KE_re_\xi\|\le\epsilon_{K,r}
       :=C_K\sqrt{r+K_q+2}\,e^{-rM/2},\qquad \xi\in\mathbb R.  \tag{8}
\]
详细界如下：p水平边的无限几何和为常数乘
rho_p^(rM/L)=e^(-rM/2)；条带每个有限p行有同阶球系数，
q可见行至多r+K_q+O(1)个，q逃逸球尾的ell¹和一致有界。
对有限个尚未进入深p尾的r，扩大C_K即可。相位模为1、输出时间支撑固定，故界对xi一致。
同样由(2)的有限p支撑、有限q可见行及q球尾，
\[
                  \|P_KFe_\xi\|\le M_K.                \tag{9}
\]
e_xi本身不在L²；(8)–(9)指采样后确实属于物理径向有限维乘紧支时间的L²向量。

取Fourier约定hat h(xi)=int h(s)exp(-i xi s)ds。
hat h绝对可积，卷积核可用平面波作弱Fourier积分；(8)–(9)使压缩后的积分在S₁中绝对收敛。
以秩一算子trace norm=两向量范数乘积，交叉项完整展开后得到
\[
 \|P_K(A_r(h)-X(h))P_K\|_1
 \le\frac{\|\widehat h\|_1}{2\pi}
           (2M_K\epsilon_{K,r}+\epsilon_{K,r}^2).        \tag{10}
\]
右侧对r可求和，因此对每个固定K，
\[
 \|P_K(C_N(h)-X(h))P_K\|_1=O_{K,h}(N^{-1}).             \tag{11}
\]
这个估计的常数依K；不提供随K一致的收敛，也不支付任何任意耦合截止路径。

## 4. 无单位调整的原周期损失和实际极限顺序

选择h in C_c∞，支撑在-L的充分小邻域，h(-L)=1，
并避开0、其余p轴格点和所有q轴格点。L/M无理且q格点局部离散，故可选。
435于是对每个固定r、足够深物理K准确给
\[
           \operatorname{Tr}(P_K A_r(h)P_K)=L\rho_p.     \tag{12}
\]
每个固定有限N的平均同样给L rho_p；而(6)对X(h)给0。
不需任何体积扣除、单位分布、自由有限部常数或数值近似。
由(11)，固定K的内层N极限也已经支付，故沿原两坐标共尾截止严格有
\[
 \boxed{\lim_{N\to\infty}\lim_{K_p,K_q\to\infty}
        \operatorname{Tr}(P_K C_N(h)P_K)=L\rho_p,
 \quad
 \lim_{K_p,K_q\to\infty}\lim_{N\to\infty}
        \operatorname{Tr}(P_K C_N(h)P_K)=0.}             \tag{13}
\]
这是同一真实最小源理想中433范数收敛序列的原物理读出不连续见证，
适用于任意两个不同素数及其原合法分割。无需W>0。
对一般h，每个有限N若沿用原A体积，435的有限部为
Lambda(h)-(N+1)W h(0)/2；p<q、h(0)!=0时另有线性N通量。

## 5. 结论的严格范围

本稿支付完成平均的真实球迹、固定球的迹范数收敛和两次实际极限不交换。
原周期读出不能由源平均的范数完成自动延续；也不能因X是源固定元便称其承载全部原素数周期。
有限源词本身的线性有限部下一稿437再检验。
HH₁闭链、完整相对Chern、规范周期选择及主关系、实位／全素数Weil比较、正性、RR、RH仍开放。
