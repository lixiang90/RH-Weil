# 332. 完整带符号节点组的Cauchy Gram与精确对偶

2026-09-07。周期7第1、2动作。[T，已通过独立逆审]，见[报告](../reviews/2026-09-07/332-cauchy-dual-review.md)。
这是有限Gram及经典插值的自含应用；实际节点组与覆盖仍[C/O]。
不宣称Cauchy行列式、对偶构造本身原创或形成新的算术Weil结构。

## 1. 同一对象与定量命题

使用同一实际前缀0<gamma<=T、L=log T、半窗A=L/2，
实型Hilbert空间f(-u)=bar(f(u))及其真实实内积。
记b=1/sqrt(2)、sinc b=sin(b)/b，
eta_A²(u)=cos(bu/A)/(2A sinc b)，|u|<=A。
对于K个互异节点w_j=d_j+i x_j，d0<=d_j<=1/2，d0>0固定，令
\[
 g_j=\eta_A e^{-ix_ju}\cosh(d_ju),\quad
 h_j=-i\eta_A e^{-ix_ju}\sinh(d_ju),\quad
 H_j=\|h_j\|^2,\quad G_j=1+H_j.
\]
同一非实对只列一次，原始重数m_j>=1另放权重2m_j。
形式分析允许端点1/2；实际非平凡零点深度严格小于1/2。

F为按(g_1/sqrt(H_1),h_1/sqrt(H_1),...,g_K/sqrt(H_K),h_K/sqrt(H_K))
排列的实合成算子，Gamma=F*F。两个列共用H归一化，正列范数不是1。
令复Hermitian矩阵
\[
 {\cal K}_{ij}={2\sqrt{d_i d_j}\over w_i+\bar w_j},\qquad
 B_j=\prod_{k\ne j}\left|{w_j-w_k\over w_j+\bar w_k}\right|,
 \quad \Theta=\sum_{j=1}^K B_j^{-2}.                         \tag{1}
\]
空乘积为1。存在c,C>0和A_*，只依赖d0与窗，使所有有限K、
所有互异w_j及A>=A_*同时满足
\[
 \boxed{\Gamma\ \ge
   \{c\,\lambda_{\min}({\cal K})-CK e^{-2d_0A}\}I_{2K}
 \ \ge\{c/\Theta-CK e^{-2d_0A}\}I_{2K}.}                  \tag{2}
\]
高度相位可任意，常数不依赖K或高度直径。
特别地K Theta T^-d0<=c/(2C)时可取gamma=c/(2Theta)>0作为Gram下界。
这不保证实际全体深点满足该数值条件。

## 2. 精确半窗分解与正权比较

对实系数a_j,b_j，写z_j=a_j-i b_j，则sum|z_j|²=||(a,b)||²，
负半窗由实型对称给相同范数，故
\[
 \|F(a,b)\|^2
 =2\int_0^A\eta_A(u)^2
 \left|\sum_j{e^{-ix_ju}\over2\sqrt{H_j}}
       (z_j e^{d_ju}+\bar z_j e^{-d_ju})\right|^2du.       \tag{3}
\]
以下只有精确分解，不对高度相位作平均。
记式(3)中增长部分为M，衰减部分为S，范数使用测度2 eta_A² du。
令t=A-u，
\[
 f_j(t)=\sqrt{2d_j}e^{-(d_j-i x_j)t},\quad
 v_j={e^{d_jA}\over\sqrt{8d_jAH_j}},\quad
 \zeta_j=e^{-ix_jA}z_j.
\]
则增长部分的范数精确等于
\[
 \|M\|^2=\int_0^A{\cos(b-bt/A)\over\sinc b}
       \left|\sum_j v_j\zeta_j f_j(t)\right|^2dt.          \tag{4}
\]
在0<=t<=A，权函数在cos b/sinc b与1/sinc b之间，均为固定正常数。
端点积分或327精确式给统一估计
H_j asymp_{d0} e^(2d_jA)/(d_j A)，因此0<v_-<=v_j<=v_+。
这个对角因子保留在式(4)，没有以渐近主项替换后付O(1/A)算子误差。

在复L²(0,infinity)用共轭第一槽内积，有
integral conj(f_i)f_j=K_ij，故全半轴二次型至少
lambda_min(K) v_-² sum|z_j|²。
尾部以Cauchy–Schwarz估计为
\[
 \int_A^\infty\left|\sum_jv_j\zeta_j f_j\right|^2
 \le v_+^2\sum_j|z_j|^2\sum_j e^{-2d_jA}
 \le C K e^{-2d_0A}\sum_j|z_j|^2.                         \tag{5}
\]
由(4)的正权下界得||M||²>=c lambda_min(K)||z||²
-C K e^-2d0A||z||²。

另一方面eta_A²<=C/A，有限和Cauchy–Schwarz给
\[
 \|S\|^2
 \le\sum_j|z_j|^2
       \sum_j{1\over2H_j}\int_0^A\eta_A(u)^2 e^{-2d_ju}du
 \le C K e^{-2d_0A}\sum_j|z_j|^2.                         \tag{6}
\]
使用||M+S||²>=||M||²/2-||S||²并重命名常数，得到(2)的第一步。
复坐标z_j及相位zeta_j分别是实2K维等距变换；不漏掉任何实方向，
也没有把两个独立实列错误合成一个实列。

## 3. 有限Cauchy公式与精确退化量

函数f_j线性无关：若其有限线性组合在正半轴为零，
解析性及在0处的前K阶导数给不同指数的Vandermonde系统。因此K严格正定。
经典Cauchy行列式在本记号给
\[
 \det{\cal K}
 =\prod_{i<j}{|w_i-w_j|^2\over|w_i+\bar w_j|^2}.           \tag{7}
\]
可直接验证：乘上全部分母后，行、列交换的交错性给相应Vandermonde因子；
两边总次数相同，取逐个简单极点的留数，归纳由K=1定出常数1。
对角缩放sqrt(2d_i)消掉对角分母2d_i；
非对角分母以共轭成对，因而得到(7)的正实表达式。
主余子式除行列式即
\[
 ({\cal K}^{-1})_{jj}=B_j^{-2},\qquad
 \lambda_{\min}({\cal K})
 ={1\over\|{\cal K}^{-1}\|}
 \ge{1\over\operatorname{tr}{\cal K}^{-1}}={1\over\Theta}. \tag{8}
\]
因为|w_j+bar(w_k)|²-|w_j-w_k|²=4d_jd_k>0，0<B_j<=1。
式(8)是有限矩阵恒等式，不依赖无限插值定理。

例如K<=K0、所有高度在长度B的区间内、|w_j-w_k|>=delta>0时，
每个分母<=sqrt(1+B²)，令q=min(1,delta/sqrt(1+B²))，则
\[
 \lambda_{\min}({\cal K})\ge K^{-1}q^{2K-2}
 \ge K_0^{-1}q^{2K_0-2}.                                 \tag{9}
\]
固定K0、B、delta之后，取足够大的A给Gamma统一正下界；无需内部间隔随1/L缩小或选择特殊相位。
若K或内部最小距离变化，不能继续使用固定常数，须回到Theta。
重数合并为权重；不把同一节点的m个重复列用于可逆性。

## 4. 完整正负列的精确对偶效应

设Gamma>=gamma I>0。J_-:R^K->R^(2K)选择每对的第二坐标，
令U=F Gamma^-1 J_-，E=gamma U U*。则
\[
 U^*F=J_-^*,\qquad
 U^*U=J_-^*\Gamma^{-1}J_-\le\gamma^{-1}I,\qquad
 0\le E\le I,\quad\operatorname{rank}E\le K.               \tag{10}
\]
令omega_j=2m_jH_j，所选完整节点组的原算子贡献精确为
\[
 {\mathsf A}_{\rm sel}
 =\sum_j\omega_j\{(g_j/\sqrt{H_j})\otimes(g_j/\sqrt{H_j})
                 -(h_j/\sqrt{H_j})\otimes(h_j/\sqrt{H_j})\}.
\]
因此
\[
 \boxed{-\operatorname{tr}(E{\mathsf A}_{\rm sel})
          =\gamma\sum_j2m_jH_j.}                          \tag{11}
\]
全部选中正列被对偶精确消去；每条选中负列与U的内积坐标恰为相应单位向量。
没有假设gh小量、没有删组内正项，也没有把P当作正谱部分。

完整算子仍是A=A_sel+P_ext-N_ext。若P_ext=B_ext B_ext*，
其精确下界为
\[
 -\operatorname{tr}(E{\mathsf A})
 \ge\gamma\sum_j2m_jH_j
       -\gamma\|B_{\rm ext}^*U\|_{\rm HS}^2.              \tag{12}
\]
这里只在下界中合法丢弃N_ext的非负贡献。外部所有正列必须控制，
不因所选组可逆就断言全算子有大负响应。

## 5. 与旧条件的关系和实际缺口

331限制同一组原始h方向的混合预算；U是由全部g/h重新组合的对偶方向，
所以(11)与其三点必要条件没有冲突。
固定有限组可含O(1)高度差，而316相干小簇允许多节点且直径o(1/L)。
这两类假设不自动互相蕴含；不宣称本篇已经验证严格更弱且非空的实际输入。

下一动作：多个内部非退化组的共同Gram、浅／远外部正项、实际sharp二阶及计数后果，
再审计真实分组、近碰撞与覆盖成本。
经典插值背景[Clark原件](../literature/background/clark-generalized-interpolation-1968.pdf)
已归档；仅核读其开头范围介绍，本证明未调用该文完整定理。
即使本篇通过复核，仍只是条件性工具，不能完成持续GOAL。
