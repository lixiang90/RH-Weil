# 319. 第一逆幂密度尾与远深正背景的共同矩阵界

2026-09-06，phase 3第3轮。[T/R，已通过独立内部复核] 实际筛选子背景的统一矩阵上界。
目标存在及后续簇几何为[C/O]。本篇不假设RH，不产生新的零密度定理。

## 1. 精确范围

同一实际0<gamma<=T前缀、L=log T、sharp MT窗A=L/2。
固定0<s<d0<1/2，0<theta<1，D=T^theta。
Q有M>=1个归一化深目标列uj，目标深度>=d0，高度xj两两D分离。
F是任意实际非实对子集，其深度e>s，且每个w属于F都满足
|yw-xj|>=D，对所有j成立。F不包含未核算的近深点。

记Gw=||gw||^2，omega_w=2mw Gw，
B_F的第w列是sqrt(omega_w) gw/sqrt(Gw)，P_F=B_FB_F*。
局部含重数计数O(L)及314引用的统一Ingham输入均保持原范围。
下述常数只依赖s、d0、theta、窗及计数常数，不依赖M、F或重数分布。
F空时结论按零算子理解。

## 2. 有限加权Schur引理（自证）

若有限矩阵K满足|Kij|<=aij，aij>=0，正权pi,qj满足
\[
 \sum_j a_{ij}q_j\le A_0p_i,\qquad
 \sum_i a_{ij}p_i\le B_0q_j,
\]
则||K||^2<=A0 B0。对任意向量v，以Cauchy–Schwarz得
\[
 \sum_i\Big|\sum_jK_{ij}v_j\Big|^2
 \le\sum_i\Big(\sum_ja_{ij}q_j\Big)
                 \Big(\sum_ja_{ij}|v_j|^2/q_j\Big)
 \le A_0B_0\sum_j|v_j|^2 .
\]
因此应用于绝对值支配矩阵不需正定性，也不依赖行列数。
这是经典Schur检验，不作为新方法。

## 3. 第一逆幂尾的实际计数输入

对任一目标中心x，令
\[
 S_v^{(1)}(x)=
 \sum_{\substack{w\in F,\ e_w\ge v\\ e_w>s}}
 {m_w\over|y_w-x|},\qquad s\le v\le1/2.
\]
所有距离在[D,T]内。若D>T则F空；下文取大T时1<D<T。
单位高度计数配合两侧距离环带，给
S_v^(1)<=C L(1+log(T/D))<=C L^2，统一于x和v。
全局含重数零密度给
\[
 S_v^{(1)}\le C L^3T^{\nu(v)}/D,\quad
 \nu(v)={3(1/2-v)\over3/2-v}.
\]
于是（局部项只放大一个log）
\[
 S_v^{(1)}\le C L^3\min\{1,T^{\nu(v)-\theta}\}.              \tag{1}
\]
外部原始条款为Chourasiya–Simonic v2 Corollary1/Table1与Bellotti–Wong v2
Theorem1.1，核读范围承继314报告；实际右侧零点与深度共轭对一一对应，2倍列权另计。

有限原子分层恒等式为
\[
 \sum_{w\in F}{m_wT^{e_w}\over|y_w-x|}
 =T^sS_s^{(1)}+L\int_s^{1/2}T^vS_v^{(1)}\,dv
 \le C L^4T^{\Psi_s(\theta)},                              \tag{2}
\]
其中
\[
 \Psi_s(\theta)=\max_{s\le v\le1/2}
 [v+\min\{0,\nu(v)-\theta\}]=\Phi_s(\theta)+\theta.           \tag{3}
\]
最大值计算与314同一交点rtheta=3(1-theta)/(2(3-theta))：
在交点左侧导数为1，右侧为1-3/(3/2-v)^2<0。
因此Psi=rtheta（s<=rtheta）或s+nu(s)-theta（s>rtheta）。
端点、严格深度筛选与等号原子的处理同有限分层恒等式，不需要交换无限和。

对所有e属于(s,1/2)，端点积分给Gw<=C_s T^e/L，常数只依赖固定s，故
\[
 \sup_j\sum_{w\in F}{\omega_w\over|y_w-x_j|}
 \le C L^3T^{\Psi_s(\theta)}.                             \tag{4}
\]
这与314的逆平方、逐目标二次型尾不同；先估计第一逆幂是为了另一侧的分离行和。

## 4. 共同矩阵，而非逐列求和

由317-(1)的gh版本，
|(B_F*Q)wj|<=C sqrt(omega_w)/|yw-xj|。
固定yw时，两侧D分离的目标且每个距离>=D给
\[
 \sum_j {|y_w-x_j|}^{-1}\le C(1+\log M)/D\le C L/D.        \tag{5}
\]
对该支配矩阵用pi=sqrt(omega_i)、qj=1，
第一Schur行界来自(5)，第二列界来自(4)，得到
\[
 \boxed{\|B_F^*Q\|^2\le C L^4T^{\Phi_s(\theta)}.}           \tag{6}
\]
再用313-(3)对完整深度<1/2的正子背景给
||B_F||^2=||P_F||<=C L T^(1/2)，于是
\[
 \boxed{\|P_FQ\|\le C L^{5/2}
          T^{1/4+\Phi_s(\theta)/2}.}                      \tag{7}
\]
界对增长的M一致，未出现sqrt(M)或总列质量乘数。
相比314单列beta的L^2，多付L^(1/2)，换取整个合成算子范数。
这不等于宣称最佳log幂，更不等于给未筛选的近深正项免费上界。

## 5. 下一步与证据边界

F的筛选可无条件定义；在完整算子应用时，所有被筛掉的正项必须另行控制。
下一轮分解P为临界线、浅点、选中簇、未选中远深点四部分，
用簇块结构处理选中近项，再选择一个共同lambda。
脚本仅核对Psi-theta=Phi与有理参数；证明依据本篇矩阵与计数推导。
原始依赖／内部287、314比较见[来源报告](../reviews/2026-09-06/phase3-primary-literature-review.md)，
完整证明已通过[独立逆审](../reviews/2026-09-06/317-320-collective-proof-review.md)。
Schur 1911 §2 Satz I是经典绝对行列和背景；本篇现代两权形式由§2自证，
不宣称是原文逐字陈述，不作世界优先权声明。
