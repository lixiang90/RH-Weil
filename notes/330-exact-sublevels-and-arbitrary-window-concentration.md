# 330. 精确混合核的次水平集与任意增长的选窗集中度

2026-09-07。周期6第1–4个数学动作；完整证明候选，独立复核待完成。
本篇是核分析，实际邻点的存在与全体覆盖仍为[C/O]，不是RH或新密度结果。

## 1. 量词与结论

沿用[327](327-window-family-and-exact-mixed-phase-average.md)的全部列和实内积。
固定0<s<=1/2、0<delta0<=B<infinity，取
s<=d,e<=1/2、delta0<=|Delta|<=B。允许这些节点参数随T变化，
但在下面每个A或y导数、积分中固定。L=log T，
A_y=(L-y)/2，0<=y<=H，H->infinity、H=o(L)。

令Theta_A为同一对归一化g、h列的实内积。对每个实数C>=1，记
W_C={w:[0,H]->[0,infinity)可测，integral w=1，w<=C/H a.e.}。
存在只依赖s、delta0、B的c_1,c_2>0以及A_*,H_*，使
只要(L-H)/2>=A_*且H>=H_*，同时对所有C>=1有
\[
 \boxed{c_1 C^{-2}\le
       \inf_{w\in W_C}\int_0^H w(y)|\Theta_{A_y}|^2\,dy
       \le c_2 C^{-2}.}                                  \tag{1}
\]
因此C可以增长得任意快，充分大T的门槛不再依赖C。
这里只求统一的最优阶，不声称329的精确常数J(C)在所有联合极限下仍给相对渐近。

## 2. 精确一阶相位形式

设b=1/sqrt(2)、k=b/A、p=e+d、z=p+iDelta。原始积分为
\[
 I_A(z)=\int_{-1}^1{\cos(bv)\over2\sinc b}e^{zAv}\,dv
 ={z\sinh(zA)\cos b+k\cosh(zA)\sin b
       \over A\sinc b(z^2+k^2)}.
\]
在本节z上分母不为零。定义
\[
 C_A(z)={z\cos b+k\sin b\over2A\sinc b(z^2+k^2)},\quad
 D_A(z)={-z\cos b+k\sin b\over2A\sinc b(z^2+k^2)}.
\]
它们满足精确恒等式I_A(z)=e^{zA}C_A(z)+e^{-zA}D_A(z)。
为避免与密度上限C混淆，带下标C_A始终指上述有理函数。

G_e=(I_A(2e)+1)/2，H_d=(I_A(2d)-1)/2，n_A=sqrt(G_e H_d)>0。
由327的原始内积（Delta方向保持）有
\[
 \Theta_A={\Im\{I_A(p+i\Delta)+I_A(d-e+i\Delta)\}\over2n_A}.
\]
C_A(z)在充分大A时不为零，取连续辐角，令
\[
 B_A={e^{pA}|C_A(z)|\over2n_A},\qquad
 \psi_A=\Delta A+\arg C_A(z).
\]
便得到精确而非渐近定义
\[
 \Theta_A=B_A\sin\psi_A+r_A,\quad
 r_A={\Im\{e^{-zA}D_A(z)+I_A(d-e+i\Delta)\}\over2n_A}. \tag{2}
\]
以下界均对所列紧参数范围一致：
\[
 0<b_-\le B_A\le b_+,\quad |B_A'|=O(A^{-2}),\quad
 \psi_A'=\Delta+O(A^{-2}),\quad
 |r_A|+|r_A'|=O(Ae^{-2sA}).                              \tag{3}
\]

这里必须直接验证导数，不能对327的裸O(A^-1)误差微分。
对t在[2s,1]，正实公式给
\[
 I_A(t)=e^{tA}{t\cos b+k\sin b\over
               2A\sinc b(t^2+k^2)}
        +e^{-tA}{-t\cos b+k\sin b\over
               2A\sinc b(t^2+k^2)}.
\]
两个有理系数及其导数按k=b/A直接求导。于是
\[
 (\log G_e)'=2e-A^{-1}+O(A^{-2}),\quad
 (\log H_d)'=2d-A^{-1}+O(A^{-2}),\quad
 n_A\asymp {e^{pA}\over A}.
\]
加减的常数1只贡献O(Ae^-2sA)的对数导数误差，已吸收进O(A^-2)。
同时
C_A'/C_A=-A^-1+O(A^-2)，故
(\log B_A)'=p+Re(C_A'/C_A)-(\log n_A)'=O(A^-2)，
(\arg C_A)'=Im(C_A'/C_A)=O(A^-2)。
B_A趋向2sqrt(ed)/sqrt(p²+Delta²)，该量在参数范围有统一正下界。

余项需要独立控制。对q=d-e，原积分及其A导数给
|I_A(q+iDelta)|<=exp(|q|A)、
|partial_A I_A(q+iDelta)|<=|q+iDelta|exp(|q|A)。
这是因积分权非负且总质量为1。p-|q|=2min(d,e)>=2s；
除以n_A并使用n_A'/n_A=O(1)，得到次指数项的(3)。
e^-zA D_A(z)/(2n_A)及其导数更小。此处也覆盖q=0。

换为y导数后，最终psi(y)=psi_{A_y}严格单调，
delta0/4<=|psi'(y)|<=K_0，B(y)>=b_-，
|B'(y)|+|r(y)|+|r'(y)|可统一小于任意预定正常数。
所有这些门槛均与密度上限C无关。

## 3. 精确次水平集，没有加性误差下限

存在K只依赖范围常数，使每个epsilon>0满足
\[
 \left|\{0\le y\le H:|\Theta_{A_y}|\le\epsilon\}\right|
 \le K(H+1)\epsilon.                                    \tag{4}
\]

取epsilon_0=b_-/8，并增大A_*使|r|<=b_-/8。
当epsilon<=epsilon_0时，次水平集必在|sin psi|<=1/4内。
把它放入较大的相位区间U={|sin psi|<=1/2}。
在每个U的连通分量内，cos psi符号不变且绝对值至少sqrt(3)/2，
而
\[
 {d\over dy}\Theta=B'\sin\psi+B\psi'\cos\psi+r'
\]
与B psi' cos psi同号，且绝对值至少某固定c_*>0。
因为psi单调且总变差O(H)，U在[0,H]只有O(H+1)个分量。
每一分量内Theta严格单调，其epsilon次水平部分长度最多2epsilon/c_*。
相加即得(4)；epsilon>epsilon_0时用H<=(H+1)epsilon/epsilon_0补齐。

关键是小阈值围绕精确零点，而不是用
|sin psi|<=epsilon+O(1/L)估计长度后留下不可消除的O(1/L)。
导数一致非零使(4)适用于任意小epsilon。

## 4. 密度上限的匹配上下界

**下界。** 对任意w in W_C，(4)给
\[
 \int_{|\Theta|\le\epsilon}w\le KC(1+H^{-1})\epsilon.
\]
取epsilon=[2KC(1+H^-1)]^-1，则至少一半质量在其补集上，
故integral w Theta²>=epsilon²/2>=c_1 C^-2（H>=1）。
没有交换C与T极限，也不要求C相对于L或H增长缓慢。

**上界。** 先从(2)–(3)确定精确零点。
每个完整相位区间[k pi-pi/6,k pi+pi/6]的两端，Theta符号相反；
区间内导数绝对值>=c_*，所以有唯一简单零点。
相位速度上下界说明，在[1,H-1]内可选n>=aH个这样的零点（充分大H），
其中a>0固定；相邻所选零点有统一正间隔，均距[0,H]端点至少1。
这些断言由完整区间数>=delta0(H-2)/(4pi)-O(1)及相位分量间的正间隔得到。
此外(2)–(3)给|dTheta/dy|<=M，M固定。

取固定C_0充分大，使任意C>=C_0时，围绕这n个零点、
每段长度ell=H/(nC)的对称区间彼此不交且仍在[0,H]。
其并集E恰有长度H/C。令w=(C/H)1_E，则w in W_C，
每一点|Theta|<=M ell/2<=M/(2aC)，故积分<=c_2 C^-2。
对1<=C<C_0，均匀密度1/H属于W_C，且归一化内积|Theta|<=1，
扩大c_2至至少C_0²即可。这样所有C同时成立，证明(1)。

此构造可以跟随精确零点，允许任意精细的可测选择。
它是单对节点的数学可达性，不是数值定位精度保证，也不是多对共同选择。

## 5. 原始重数与深度差的成本

对327、329定义的Z(y)=2m_wG_{e,y}Theta²、
W(y)=2m_jH_{d,y}，若e>=d，则
\[
 {G_{e,y}\over H_{d,y}}
 ={d\over e}T^{e-d}e^{-(e-d)y}(1+O_s(L^{-1})).
\]
由区间最小值与(1)，对任何w in W_C，
\[
 \boxed{\int_0^H w(y){Z(y)\over W(y)}\,dy
 \ge c\,{m_w\over m_j}
       {T^{e-d}e^{-(e-d)H}\over C^2}.}                   \tag{5}
\]
单对构造也给相应上界
inf_w integral w Z/W <= C' (m_w/m_j) T^(e-d)/C²；
上下界只相差exp((e-d)H)=T^o(1)及固定常数。

若深度差eta=e-d>0固定，C=T^{kappa+o(1)}，
实际单零点原始重数满足1<=m_j,m_w<<log T，H=o(log T)，
则(5)为T^{eta-2kappa-o(1)}的下界。
kappa<eta/2时该单项正预算必发散；要取得o(1)，必要条件至少是
liminf(log C/log T)>=eta/2。
相反kappa>eta/2时，单对的上界构造确给o(1)。
等号边界仍依次幂因子，不能仅看指数判定。
这里的重数上界只使用已采用的实际单位高度计数，不另假设简单性。

e=d且重数可比较时，G_d/H_d=1+o(1)一致，
inf_w integral w Z/W与(m_w/m_j)C^-2同阶。
故C->infinity确能消去单对预算；不能把增长集中度一概称为失败。

## 6. 研究边界

新增输入是精确C¹核在所有小尺度的次水平集控制，填补329固定C证明的误差缺口。
固定非零高度间隔的较深邻点会要求至少T^{(e-d)/2-o(1)}的集中度；
这是在实际原始权重下的条件性单对成本，没有验证这种实际节点配置存在。

全部正负列仍保留；(5)只约束单项正泄漏，不下界完整有符号响应，
也不能将单目标W换成簇总质量。所有窗口各有自己的算子和正则化。
|Delta|->0、多个节点共同优化、限制窗口可计算性或新的算术筛选均未被本篇覆盖。
本篇若通过独立复核，也只结算有限核引理，不满足GOAL第十节C。
