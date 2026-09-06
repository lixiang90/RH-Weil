# 333. 多个完整节点组的共同对偶与条件性计数

2026-09-07。周期7第3动作。[T，依332，已通过独立逆审并采用修订]，见[报告](../reviews/2026-09-07/333-joint-packet-review.md)。
使用同一实际原算子，不引入不同窗口／不同正则化压缩的求和。
真实分组与外部分离仍[C/O]，本篇没有新的无条件密度结果。

## 1. 准确几何与原始输入

同一0<gamma<=T前缀、sharp MT窗A=L/2、L=log T。
固定0<s<d0<1/2、0<theta<1、K0正整数、B>0、delta>0，D=T^theta。
选M个互不相交、非空完整非实节点组C_r，满足：

- 每组至多K0个互异节点，深度>=d0；原始重数不计入组大小。
- 组内高度在长度B的区间，复节点w=d+i x两两距离>=delta。
- 每组指定一个成员高度X_r为中心；中心之间距离>=D。
- 每个未选中深度e>s节点，与所有中心距离>=D。

最后一条是显式前提；不能把其余近深点删掉。允许组数及重数增长，
原始单位高度含重数计数O(L)保持。每组可以是任意不连续的实际子集，
但必须验证未选中深点的最后一条条件。
记n=sum_r |C_r|，全体所选节点按332组成2n列F，Gamma=F*F。

实际输入仅引用已复核的313浅背景、319远深Schur与324二阶：
\[
 \|P_{\le s}\|\ll L T^s,\qquad
 \|\mathsf A\|_{\rm HS}^2\ll TL.                           \tag{1}
\]
P_{\le s}包含全部临界线正列和深度<=s的正列。
它不是A的正谱部分；其余所有未选中深点属于下面P_F。

## 2. 增长组数的共同Gram

由332固定K0、B、delta结论，充分大T时每个对角块Gamma_r>=g_* I，
其中g_*>0仅依固定参数。
不同组成员高度距离>=D|r-r'|-2B，按中心顺序编号。
对大T，317归一化gg、gh、hh远界，加上G/H有界，给
\[
 |\Gamma_{ij}|\le C/(D|r-r'|)\quad(i\in C_r,\ j\in C_{r'}).
\]
每个节点的两条列分别计数，固定行的块外绝对值和<=C K0(1+log M)/D。
中心在(0,T]，M<=1+T/D，因此
\[
 \|\Gamma-\operatorname{diag}(\Gamma_r)\|\ll L/D=o(1).
\]
选择固定gamma=g_*/2，最终Gamma>=gamma I。M=1时块外项为0。
不是对全体n节点套用332的n T^-d0误差；局部误差先在有界组内控制，
组间用真实有限窗核界，因而不额外要求n T^-d0小量。

## 3. 远深背景对全部2n列的一致界

令P_F=B_F B_F*包含全部未选中深度>s节点，
列权omega_w=2m_w G_w，列向量sqrt(omega_w) g_w/sqrt(G_w)。
这些点与每个所选节点距离至少D-B>=D/2。
记Psi_s(theta)=max_{s<=v<=1/2}[v+min(0,nu(v)-theta)]=Phi_s(theta)+theta。
对每列F_i，由319-(4)的第一逆幂分层，
\[
 \sum_w{\omega_w\over |y_w-x_i|}\ll L^3 T^{\Psi_s(\theta)}.
\]
对固定w，组中心D分离，每组至多2K0列，故
\[
 \sum_i |y_w-x_i|^{-1}\ll K_0 L/D.
\]
这包括所有正、负测试列，远核界对g/sqrt(H)也成立，因为G/H统一有界。
使用319两权Schur得到
\[
 \boxed{\|B_F^*F\|^2\ll L^4T^{\Phi_s(\theta)},}             \tag{2}
\]
其中nu(v)=3(1/2-v)/(3/2-v)，r_theta=3(1-theta)/(2(3-theta))，
\[
 \Phi_s(\theta)=
 \begin{cases}r_\theta-\theta,&s\le r_\theta,\\
 s+\nu(s)-2\theta,&s>r_\theta.\end{cases}
\]
常数可依K0等固定参数，不依n、M或重数分布。
距离D/2只改正常数；原始密度、单位高度计数及完整正权保持。

## 4. 一个共同效应和任意所选子集

对任意所选节点子集J，n_J=|J|，令J_-选择其负坐标，U_J=F Gamma^-1 J_-，
E_J=gamma U_J U_J*。无论J是否整个组，U_J*都消去**全部所选正列**，
也消去所选负列中不属于J的列，而在J的负列上取得单位内积坐标。
因此E_J同样消去前述列，且在J的归一化负列上的内积矩阵为gamma delta_jk。
由332，0<=E_J<=I、rank E_J<=n_J。
令W_J=sum_{j in J}2m_jH_j，完整算子的精确账本给
\[
 -\operatorname{tr}(E_J\mathsf A)
 \ge\gamma W_J-\gamma\operatorname{tr}(U_J^*P_{\le s}U_J)
                   -\gamma\|B_F^*U_J\|_{\rm HS}^2.
\]
U_J*U_J<=gamma^-1 I且||Gamma^-1||<=gamma^-1。特别地
gamma||B_F*U_J||HS²<=gamma||B_F*F||²||Gamma^-1 J_-||HS²
<=(n_J/gamma)||B_F*F||²，故
\[
 \boxed{-\operatorname{tr}(E_J\mathsf A)
 \ge\gamma W_J-C n_J\{LT^s+L^4T^{\Phi_s(\theta)}\}.}       \tag{3}
\]
第二项中gamma^-1的固定损失吸入C；常数统一于J。
关键是外部预算按n_J控制，而不是将全体误差先除以可能很小的W_J。

若
\[
 d_0>\max\{s,\Phi_s(\theta)\},                             \tag{4}
\]
则H_j>=c T^d0/L和m_j>=1给相对误差
O(L²T^(s-d0)+L^5T^(Phi-d0))=o(1)，因此所有非空J一致有
\[
 -\operatorname{tr}(E_J\mathsf A)\ge(\gamma-o(1))W_J.
                                                                    \tag{5}
\]
这里直接测试原算子。没有声称同一个R的范数或负谱压缩满足相同新范围；
317–320曾为后续正则化使用更强参数限制，不能仅由(4)宣称改进了那个定理。

## 5. 同一sharp二阶的条件性计数

由0<=E_J<=I及rank<=n_J，有||E_J||HS<=sqrt(n_J)。
以实际(1)及HS Cauchy–Schwarz得到
\[
 W_J\ll\sqrt{n_J TL}.                                    \tag{6}
\]
对任意固定d>=d0，令J为所选深度>=d的全部节点，
K_sel(d)=sum_{j in J}m_j，保留单个右侧零点的原始重数。
W_J>=c K_sel(d) T^d/L且n_J<=K_sel(d)，故
\[
 \boxed{K_{\rm sel}(d)\ll T^{1-2d}L^3.}                   \tag{7}
\]
空集时显然成立。左侧对称计数等于右侧，合计左右两侧时乘以2，未改计重数口径。
该指数与325相同；新内容只在选中正列处理和明确几何类，
不称为新的全体零密度估计。

例如(s,d0,theta)=(3/20,1/4,2/5)给Phi=-7/130，满足(4)。
若按原始重数计的实际固定比例覆盖被另行证明，d=1/4的指数1/2才有326所列潜在比较价值。
当前没有此覆盖；d=2/5处同一指数仍弱于既有Huxley输入。

## 6. 下一审计

此定理排除了“共同相位gh不能全小，所以所有共同测试都失效”的错误推论。
它并没有证明实际分组成立。组大小K0、复距离delta和外部D间隙均固定在假设中。
仅用单位高度O(L)、全局零密度或贪心D分離选择，不能免费得到这些条件和固定比例覆盖。
下一动作须核算增长大小、碰撞和抽样损失，不能继续把条件性(7)写成实际改进。
