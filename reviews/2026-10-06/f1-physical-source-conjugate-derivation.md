# 原物理下截止的真源共轭迹、单位通量与平均极限障碍

2026-10-06。独立计算[425](../../notes/425-f1-recentered-geometric-corner-and-source-period-finite-part.md)的同一固定 \(A(h)=VU(h)V^*\)、[429](../../notes/429-f1-original-unitary-crosses-the-fixed-corner-domain.md)/[430](../../notes/430-f1-source-stable-periodic-smoothing-algebra.md)的原u，以及**原物理径向e基**下截止
\[
 P_K=\mathbf1_{j\ge-K_p,\ k\ge-K_q}\otimes1_t.
\]
保留Haar球尾、原 \(c=d_p,d=d_q\)、\(\mathsf T_s\phi(t)=\phi(t-s)\) 及完整平滑混合项。本报告只写新推导，不改笔记或索引。

主结论：对每个固定整数r及足够深的两个原物理截止，压缩确为S₁，且
\[
 \boxed{\operatorname{Tr}(P_Ku^rA(h)u^{-r}P_K)
 =(K_pL+K_qM)h(0)+\Lambda(h)-rW h(0),\qquad
 W=M-\int_{\mathbb R}c^2d^2=\int_0^M w.}                   \tag{1}
\]
这里Λ正是425的原两位周期有限部，不是重新指定的目标分布。非零周期权重保留；真源的缺陷只在单位时间项。433的原平均极限还改变物理体积与保留的周期通道，给实际的连续传递障碍。

## 1. 原Haar下截止在完整波形基中的精确投影

对 \(s=p,q\)，\(\rho_s=s^{-1/2}\)、\(c_s=\sqrt{1-\rho_s^2}\)，仍用425的完整正交波形 \(w_n\)。令
\[
 D_{K,s}=\sum_{n\ge-K}P_{w_n},\qquad
 a_{K,s}=c_s\sum_{n<-K}\rho_s^{-K-n-1}w_n .                 \tag{2}
\]
\(a_{K,s}\) 与 \(b_{-K,s}\) 只差整体负号，故投影相同。原物理下截止精确为
\[
 Q_{K,s}:=\mathbf1_{e\text{ 基次数}\ge-K}
                   =D_{K,s}+P_{a_{K,s}}.                   \tag{3}
\]
证明：对n≥−K，w_n的物理支集全在次数≥−K；n<−K时其物理上尾是 \(-c_s\rho_s^{-K-n-1}b_{-K,s}\)。正端波形与该球正交，球／波形递推及完整性给(3)。它是原Haar球，没有按读出加原子。

因此P_K是四个正交投影通道之和：
\[
 D_p\otimes D_q,quad P_{a_p}\otimes D_q,quad
 D_p\otimes P_{a_q},\quad P_{a_p}\otimes P_{a_q}.             \tag{4}
\]
本文不能用一个x半线替代(3)：后面的两条逃逸球通道会产生全部非零周期权重。

## 2. 原源幂的完整时间采样行

为区分源与物理e基，暂称Green源投影为 \(e_G\)。原源的有限系数为
\[
 u^r=1-e_G+v_r,\qquad
 v_r=\sum_aM_{c(t)c(t-aL-rM)}P_{(a,r)}.                     \tag{5}
\]
固定r时有限个a非零；负r同样由伴随成立。设
\[
 a(x)=\sum_{j<0}c(x+jL)^2,\qquad f(x)=c(x)d(x).
\]
从原(5)直接作用425的两采样通道，得到 \(V_r=u^rV\) 在波形(j,k)行的准确公式
\[
 (V_r\phi)_{j,k}(t)=\eta_{j,k}^{(r)}(t)\phi(t-jL-kM),       \tag{6}
\]
\[
\begin{split}
 \eta_{j,k}^{(r)}(t)={}&\delta_{k0}c(t)[\mathbf1_{j<0}-a(t-jL)]
 +\delta_{kr}c(t)a(t-jL-rM)\\
 &+\delta_{j0}\mathbf1_{k<0}d(t)
 +c(t)[\mathbf1_{k<r}f(t-jL-rM)-\mathbf1_{k<0}f(t-jL)].
\end{split}                                                \tag{7}
\]
所有外侧时间支集在原c、d的共同紧集内。r=0还原原V；源p/q混合项在(7)最后一行完整保留。

对固定r，可选有限的深端阈值，使以下都是准确等式：

* p波形次数j充分负时，\(\eta_{j,k}^{(r)}=\delta_{kr}c(t)\)；
* q波形次数k充分负时，\(\eta_{j,k}^{(r)}=d_j^{(r)}(t)\)，其中
\[
 d_j^{(r)}(t)=\delta_{j0}d(t)+c(t)[f(t-jL-rM)-f(t-jL)];       \tag{8}
\]
* (8)仅有限个j非零，且除上述水平负p边、有限p宽度负q条带外，(7)只剩有限角点行。

选K_p使其低于所有有限p条带并进入p深端，选K_q使其进入q深端且r≥−K_q。以后的“足够深”都指这个固定r的实际有限条件；不要求两截止比例，但不宣称阈值对所有r统一。

一个后面需要的精确能量等式是
\[
 \sum_j[d_j^{(r)}(y+jL)]^2
 =d(y)^2-f(y)^2+f(y-rM)^2=:D_r(y),\qquad
 \sum_j\int[d_j^{(r)}]^2=M.                                \tag{9}
\]
展开(8)，交叉项为 \(2f(y)(f(y-rM)-f(y))\)，末项平方和用 \(\sum_jc(y+jL)^2=1\)，即得(9)。这支付q通道总迹权重，未由预期周期值规定它。

## 3. 先证明整个实际压缩为迹类

按(4)、(6)压缩 \(V_r\)。D_p⊗D_q通道只剩有限个(j,k)波形行；每个时间系数为光滑紧支 \(\eta_{j,k}^{(r)}\)。p逃逸球通道的深端行只在q=r，其有限径向像为 \(a_{K_p,p}\otimes w_{r,q}\)。q逃逸球通道的径向像为有限个 \(w_{j,p}\otimes a_{K_q,q}\)。双逃逸球通道为零，因为在双深负区(7)恒零。

为避免仅凭“有限径向像”宣称时间也迹类，直接构造Fourier核向量 \(v_{K,r}(\xi)\in\mathcal H\)。其上述有限正交径向通道中的时间分量为：
\[
 \eta_{j,k}^{(r)}(t)e^{i\xi(t-jL-kM)}                        \tag{10}
\]
于D_p⊗D_q各行；p球行是
\[
 \frac{c_p e^{i\xi((K_p+1)L-rM)}}{1-\rho_p e^{i\xi L}}
                         c(t)e^{i\xi t};                  \tag{11}
\]
q球的第j行是
\[
 \frac{c_q e^{i\xi((K_q+1)M-jL)}}{1-\rho_q e^{i\xi M}}
                         d_j^{(r)}(t)e^{i\xi t}.           \tag{12}
\]
这些式子来自(2)的实际几何尾求和，不把平面波当L²向量输入。所有时间函数紧支，有限径向行加两个有界几何分母使 \(\sup_\xi\|v_{K,r}(\xi)\|<\infty\)。对 \(h\in C_c^\infty\)，\(\widehat h\in L^1\)，于是
\[
 \frac1{2\pi}\int\widehat h(\xi)
          |v_{K,r}(\xi)\rangle\langle v_{K,r}(\xi)|\,d\xi   \tag{13}
\]
在迹范数中绝对收敛。先对Schwartz输入比较明确Fourier核与(6)的有界采样，再延拓，可知(13)正是 \(P_KV_rU(h)V_r^*P_K\)。因此整个实际物理压缩S₁。

秩一积分中p球、q球、有限角点之间的全部交叉算子都被保留；其时间位移可能含完整混合 \(aL+bM\)。不能在准入前删去这些块。准入后(4)径向通道正交，完整交叉块的普通迹才为零。

## 4. 两个原Haar球给完整轴周期，含单位

p球(11)范数平方用 \(\int c^2=L\)，q球(12)用(9)总和为M。几何分母的精确Poisson展开
\[
 \frac{1-\rho^2}{|1-\rho e^{i\xi D}|^2}
                  =\sum_{a\in\mathbb Z}\rho^{|a|}e^{iaD\xi}
\]
绝对收敛，所以(13)中逐项Fourier反演合法。两个球迹分别为
\[
 T_{p,\rm ball}=L\sum_{a\in\mathbb Z}\rho_p^{|a|}h(-aL),
 \qquad T_{q,\rm ball}=M\sum_{b\in\mathbb Z}\rho_q^{|b|}h(-bM). \tag{14}
\]
对称权重允许把反演得到的h(aD)改名为h(−aD)，未要求h偶。源次数r、截止起点K和p条带j的纯时间相位在自相关中取消；ρ来自原Haar球而未变化。式(14)包括单位 \((L+M)h(0)\)，不是只比较非零群标签。

## 5. 有限波形体积的两条实际源边通量

有限D_p⊗D_q通道的迹为 \(I_r(K)h(0)\)，其中
\[
 I_r(K)=\sum_{j\ge-K_p,k\ge-K_q}\int[\eta_{j,k}^{(r)}(t)]^2dt.
\]
该和实际有限，原r=0给 \(I_0(K)=K_pL+K_qM\)。为了算全部角点变化，使用430的忠实不变坐标x，仅在这个**已由原物理截止分解出的有限波形通道**内换元。其真实纤维向量为 \(z_r(x)=u(x)^rz(x)\)，源酉性给每个x \(\|z_r(x)\|^2=\|z(x)\|^2\)。故有限内部能量差等于两个外边能量差的负值。

p外边j<−K_p只在q=r。其相对原q=0外边的总能量差为
\[
 a(x-K_pL+rM)-a(x-K_pL).
\]
a从负端0过渡到正端1，差紧支，因此
\[
 \int[a(x-K_pL+rM)-a(x-K_pL)]dx=rM.                        \tag{15}
\]
可由对位移求导 \(\int a'=1\) 直接证明。不能把两个无限外边的积分逐行分开并说每一行积分相等；两者各自无穷，只有半轴总差的紧支积分合法。

q外边k<−K_q的全部p条带已被D_p包含。用(9)，能量差为
\[
 \sum_{k<-K_q}[f(x+(k-r)M)^2-f(x+kM)^2].
\]
它准确化成|r|个有限项的带符号和，积分为 \(-r\int f^2\)。双外边恒零，p、q外边没有重叠能量。于是
\[
 \boxed{I_r(K)-I_0(K)=-rM+r\int f^2=-rW.}                  \tag{16}
\]
这给两条清楚的来源通量：内部p边 \(-rM\)，内部q边 \(+r\int f^2\)，总通量 \(-rW\)。所有有限角点混合修正已由真实纤维酉能量恒等式计入；不需要把它们凭猜测设零。

## 6. 完整压缩迹、r为正负1与相同体积有限部

合并(14)、(16)得到(1)，其中
\[
 \Lambda(h)=(L+M)h(0)
   +L\sum_{a\ne0}\rho_p^{|a|}h(-aL)
   +M\sum_{b\ne0}\rho_q^{|b|}h(-bM).
\]
扣除425同一个原体积 \((K_pL+K_qM)h(0)\) 后，所有足够深截止的值已完全相同，故有联合有限部
\[
 \operatorname{FP}_{\rm phys}(u^rA(h)u^{-r})=\Lambda(h)-rW h(0). \tag{17}
\]
特别
\[
 \operatorname{FP}_{\rm phys}(uA(h)u^*)=\Lambda(h)-W h(0),
 \quad\operatorname{FP}_{\rm phys}(u^*A(h)u)=\Lambda(h)+W h(0). \tag{18}
\]
单位系数分别是 \(L+\int f^2\) 与 \(L+2M-\int f^2\)。非零p、q轴权重始终为原 \(L\rho_p^{|a|}\)、\(M\rho_q^{|b|}\)。

源加权边界 \(A-uAu^*\) 的每个足够深物理压缩确为S₁，普通压缩迹为 \(W h(0)\)。这只是两个已合法S₁压缩之差，**不**把通常非紧的完整源边界称为迹类，也不把裸 \((u^*P_Ku-P_K)A\) 未经准入写普通迹。433的 \(W\ge M-L\) 表明p<q时该单位通量严格正。h(0)=0时压缩通量为零，但不证明原非紧边界是算术主关系。

若改为r依赖的体积 \((K_pL+K_qM-rW)h(0)\)，算式会回到Λ；这只是另一已明确的扣除，尚无几何理由选它为规范读出，本文没有为追求源消失而改原体积。

## 7. 原Cesàro固定算子的实际物理迹

进一步检验[433](../../notes/433-f1-source-cesaro-limit-and-noncompact-fixed-sector.md)的同一个范数极限 \(X(h)=FU(h)F^*\)，\(F=(1-e_G)V\)。它在波形基中分成q=0的有限p行与q<0的有限p宽度条带：
\[
 (F_p\phi)_{j,0}(t)=c(t)[\mathbf1_{j<0}-a(t-jL)]\phi(t-jL),
\]
\[
 (F_q\phi)_{j,k}(t)=\mathbf1_{k<0}
      [\delta_{j0}d(t)-c(t)f(t-jL)]\phi(t-jL-kM).            \tag{19}
\]
所有非零p次数有限，因此足够深P_p在这里恰为单位。原P_q保留q=0波形与其负半轴块的正交性，两个通道交叉迹为零。两类总时间能量分别为
\[
 C_p:=\int_{\mathbb R}a(x)(1-a(x))dx,
 \qquad\sum_j\int[\delta_{j0}d-cf(\cdot-jL)]^2=W.           \tag{20}
\]
前者用全p平方分割展开平方；后者交叉项 \(-2\int f^2\)，末项以全L平方和积分给 \(+\int f^2\)。C_p有限，平滑分割从0过渡到1使其严格正。

相同有限行加q逃逸球的Fourier秩一证明支付 \(P_KX(h)P_K\in\mathcal S_1\)，并精确给
\[
 \boxed{\operatorname{Tr}(P_KX(h)P_K)
   =K_qW h(0)+C_p h(0)
                  +W\sum_{b\in\mathbb Z}\rho_q^{|b|}h(-bM).} \tag{21}
\]
完成域固定部门已失去原p负端体积和p球周期，负q体积也从M降为W。此处不是用期望目标另定义X，X是433同一原源平均的真实算子。

## 8. 范数平均不能传递原物理读出：具体见证

对有限N，令 \(C_N(h)=N^{-1}\sum_{r=1}^Nu^rA(h)u^{-r}\)。固定N后，选择对所有这些r足够深的物理截止，(17)给
\[
 \operatorname{FP}_{\rm phys}(C_N(h))
                   =\Lambda(h)-\frac{N+1}{2}W h(0).        \tag{22}
\]
433却证明 \(C_N(h)\to X(h)\) 在算子范数中收敛。若h(0)非零且p<q，(22)随N线性变化，而(21)显示极限甚至具有不同的负端体积系数。截止深度阈值依赖N，不能交换这两个极限。

还能完全避开单位项：取真实光滑紧支h，只在 \(-L\) 的小邻域非零，\(h(-L)=1\)，避开0和两条轴的其他周期。则
\[
 h(0)=0,\qquad\Lambda(h)=L\rho_p\ne0,
 \qquad h(-bM)=0\text{ 对所有 }b.
\]
每个有限N的实际物理有限部都为 \(L\rho_p\)，但范数极限X的每个足够深物理压缩迹由(21)恒为0。它是同一源平均、同一原物理截止、同一真实时间测试的明确不连续见证，不能靠单位时间常数抵消。

本报告支付实际S₁压缩、完整轴周期、单位源通量及固定部门的原物理迹。未认证这些有限部在源稳定代数上的循环性、相对Chern链、规范截止传递或算术主消失。实位／全素数Weil比较、Weil正性、RR和RH均仍开放；有限有理审计不替代这里的无限维Haar与时间核证明。
