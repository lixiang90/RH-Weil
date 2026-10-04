# 430. 真源保持的实际周期平滑核代数

2026-10-04。接续[429](429-f1-original-unitary-crosses-the-fixed-corner-domain.md)。
本稿构造一个保留原u、原时间及原采样V的实际星代数，支付u及u*的双侧准入和有限词乘法。
关键不是抽象取闭包，而是计算交叉Gram的真实周期尾，并证明所有替换误差迹类。
它是明确的解析扩大候选；不声称它恰为C*(1,u,E)中E生成的最小闭理想。

## 1. 原不变坐标中的精确纤维

保留429的完整波形基、原c=d_p及d_q，L=log p、M=log q。
在原Hilbert空间作忠实酉坐标变换
\[
 (G\psi)_{j,k}(x)=\psi_{j,k}(x+jL+kM),\qquad
 x=t-jL-kM.                                                   \tag{1}
\]
每个原物理箭头P_(a,b)保持x；额外物理时间平移仍把x平移同一实数。
这不是对源取字符评价，也未替换原时间作用。

令H_0=ell²(Z²)。原V在此表示中是向量值乘法
\[
 (GV\phi)(x)=z(x)\phi(x),\qquad
 z(x)=\sum_{j<0}c(x+jL)e_{j,0}
       +\sum_{k<0}d_q(x+kM)e_{0,k}.                          \tag{2}
\]
两行族正交，局部只有有限个非零项。其范数平方为427的m=m_p+m_q，
充分左端z=0，充分右端m=2。记一个共同左端为a，使V=V1_[a,infinity)。

原源在每个x纤维中仍是u(x)=1-e(x)+v(x)。具体地，
e(x)在每个k块投影到单位向量
\[
 c_k(x)=\sum_j c(x+jL+kM)e_{j,k},
\]
v(x)c_k(x)=c_(k+1)(x)，在e的正交补上u为单位。
平方分割给||c_k(x)||=1，这直接核准原u的酉性与箭头，而非另造一个移位。
对所有整数r，有限系数计算给
\[
 u^r=1-e+v_r,\qquad
 v_r=\sum_n M_{c(t)c(t-nL-rM)}P_{(n,r)},\qquad v_0=e.        \tag{3}
\]
例如v_r v_s=v_(r+s)中的中间和恰为sum_n c(t-nL-rM)²=1；负r由伴随处理。

## 2. 全部交叉Gram及其周期尾

由(1)–(3)，交叉Gram准确为纯乘法：
\[
 V^*u^rV=M_{g_r},\qquad
 g_r(x)=\langle z(x),u(x)^r z(x)\rangle.                    \tag{4}
\]
以下内积在第二变量线性。定义
\[
 f=c d_q,\quad
 a_p(x)=\sum_{j<0}c(x+jL)^2,\quad
 a_q(x)=\sum_{k<0}d_q(x+kM)^2,
\]
\[
 z_r(x)=\sum_{k<0,\ k-r<0}f(x+kM)f(x+(k-r)M),\qquad
 \nu(x)=a_p+a_q-a_p^2-z_0.                                 \tag{5}
\]
于是
\[
 g_0=a_p+a_q,\qquad
 g_r=\nu+z_r+a_p(x)f(x-|r|M)\quad(r\ne0).                  \tag{6}
\]
最后一项是真实p/q混合项：r>0时来自负q输入到q=0的p输出，r<0时来自伴随方向。
不能在计算前删除它；它在x紧支，所以不进入右端符号。
z_(-r)=z_r，全部系数实值。核算(6)的完整有限行报告见
[源轨道推导](../reviews/2026-10-04/f1-source-orbit-edge-derivation.md)。

令
\[
 \alpha(x)=\sum_{k\in\mathbb Z}f(x+kM)^2,\qquad
 \beta_r(x)=\sum_{k\in\mathbb Z}f(x+kM)f(x+(k-r)M),
\]
\[
 \gamma_r(x)=\delta_{r,0}+1-\alpha(x)+\beta_r(x).             \tag{7}
\]
这些都是光滑M周期函数，0<=alpha<=1，因为c²<=1、sum_k d_q(x+kM)²=1。
对每个固定r，存在b_r，使
\[
 g_r(x)=\gamma_r(x)\ (x\ge b_r),\qquad g_r(x)=0\ (x\le a).
                                                                    \tag{8}
\]
特别gamma_0=2；r非零时通常是周期系数，不应预先换成常数。
g_r-gamma_r在负端一般仍非零，不能直接叫作紧支函数。

有限源指标集J的右端Gram矩阵
\[
 \Gamma_J(x)=[\gamma_{k-j}(x)]_{j,k\in J}
                                                                    \tag{9}
\]
满足Gamma_J>=I。确实，令f_x(k)=f(x+kM)，则对有限lambda，
\[
 \sum_{j,k}\overline{\lambda_j}\gamma_{k-j}\lambda_k
 =\sum_j|\lambda_j|^2+(1-\alpha)|\sum_j\lambda_j|^2
       +\|\sum_j\lambda_j S^j f_x\|_{\ell^2}^2.
                                                                    \tag{10}
\]
这保留所有源轨道，且给严格下界。只在有限矩阵使用此式；无限常值矩阵
(1-alpha)本身未必定义ell²上的有界算子，不能自动写无限Gamma的平方根。

## 3. 明确的周期平滑核类

令G_M为L²(R_x)上具有以下核的积分算子B：
\[
 K_B\in C^\infty(\mathbb R^2),\quad
 K_B(x+M,y+M)=K_B(x,y),\quad
 K_B(x,y)=0\quad(|x-y|>R_B)                                \tag{11}
\]
其中R_B可依B而变。联合周期和有限传播保证所有核导数在一个基本条带有界。
Schur估计给有界性；伴随取overline(K_B(y,x))，乘积核为integral K_B(x,z)K_C(z,y)dz。
后者的z积分在一致有界长度内，故仍光滑、联合M周期，传播半径至多R_B+R_C。
因此G_M是实际非单位星代数。原U(h)属于G_M，其核h(x-y)甚至联合任意实周期。
若r(x)光滑M周期，则B M_r C也在G_M；裸M_r本身不要求属于G_M。

定义实际有界算子
\[
 F_{i,j}(B)=u^i V B V^*u^{-j},\qquad i,j\in\mathbb Z,
\]
\[
 D_{\rm src}=\operatorname{span}_{\rm finite}
       \{F_{i,j}(B):B\in G_M\}+\mathcal S_1(\mathcal H).     \tag{12}
\]
所有元素是原Hilbert空间中的真实算子；没有通过期望读出定义元素。
它包含原D，因为F_(0,0)(U(h))=A(h)，并包含429的uA、Au及A-uAu*。

## 4. 乘法余项的完整迹类准入

由(4)，精确乘积为
\[
 F_{i,j}(B)F_{k,l}(C)
   =u^i V B M_{g_{k-j}} C V^*u^{-l}.                       \tag{13}
\]
用(8)替换周期尾后，
\[
 F_{i,j}(B)F_{k,l}(C)
 =F_{i,l}(B M_{\gamma_{k-j}} C)+S_{i,j,k,l}(B,C),
 \qquad S_{i,j,k,l}(B,C)\in\mathcal S_1.                   \tag{14}
\]
迹类论证不能省掉左端：V*的输出在[a,infinity)，C有限传播使C V*的输出在
[a-R_C,infinity)。选择光滑chi在该半线恒1、充分左端为0，令
\[
 q=\chi(g_{k-j}-\gamma_{k-j}).                             \tag{15}
\]
由(8)，q光滑紧支，而且(M_g-M_gamma) C V*=M_q C V*。
B M_q C的核光滑，两变量都在supp(q)加相应传播半径的紧区间内。
在严格更大的紧区间作Fourier秩一展开，双变量反复分部积分给绝对可和系数，故该算子迹类。
有界V、V*、u的乘积保留迹类，得到(14)。全部交叉通道都已包含在g_r中。

另外F_(i,j)(B)*=F_(j,i)(B*)，S₁为双侧理想。因此(12)确是星代数。
源双侧准入准确为
\[
 uF_{i,j}(B)=F_{i+1,j}(B),\quad u^*F_{i,j}(B)=F_{i-1,j}(B),
\]
\[
 F_{i,j}(B)u=F_{i,j-1}(B),\quad
 F_{i,j}(B)u^*=F_{i,j+1}(B).                               \tag{16}
\]
故u、u*是真正的双侧乘子，所有含至少一个域元素的有限源词都在该域中。
没有把非紧加权边界硬放进S₁，而是把它作为(12)的合法新元素保留。

## 5. 已支付的条件及剩余问题

本稿支付一个具体扩大域的实际算子准入、乘法、伴随、普通迹理想和真源双侧稳定性。
其周期核选择有原交叉Gram的动机，但允许所有(11)的核是明确的解析扩大；
尚未证明这些核全由原E和u生成，所以不把本域等同于最小源理想。
商的精确本质范数和非紧源边界继续在431计算。

427的原非零交换子迹依旧成立：本域包含原D和S₁，因此在整个新域上
匹配S₁普通迹的标量循环扩张仍不可能。扩大定义域没有消除此反例。
本稿没有选定新的有限部、物理球截止的周期读出或完整相对Chern链。
实位、全素数比较、算术主关系、Weil正性、RR和RH分别保持开放。
