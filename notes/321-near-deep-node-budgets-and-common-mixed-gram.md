# 321. 未选中近深点：由原始节点权重控制共同混合Gram

2026-09-06，持续GOAL周期4第1轮。[T，已通过独立内部复核] 有限矩阵／节点预算。
实际满足廉价预算的选择仍[C/O]；本篇不满足GOAL第十节C的较远期显著进展标准。

## 1. 放开外部分离而保留原始对象

沿320的实际前缀、sharp MT窗A=L/2、L=log T，固定0<s<d0<1/2。
选M>=1个互不相交深簇Cj，每簇直径<=r、包含一个深度>=d0的目标xj+i dj，
簇内深度>s，目标中心两两D=T^theta分离，0<theta<1，c=Ar->0。
**不再要求未选中深点与选中簇相距D。**
所有原始正负列与单点重数保留，Q=[hj/sqrt(Hj)]。

记B_j为所有未选中且深度>s、|yw-xj|<D/4的点；
B为其并，F为其余未选中深点。B_j互不相交，因为中心D分离。
每个F点距全部目标>=D/4；319的共同远尾仍适用，常数因4变化，幂指数不变。
所选簇在大T时r<=D/4，其他C_l和B_l对目标j均在D/4以外。

用omega_w=2mw Gw，Gw=||gw||²，定义
\[
 S_j=\sum_{w\in B_j}\omega_w,\quad S_B=\max_j S_j .
\]
若B为空，下面所有B预算为0。它们是原始正列质量，不是负谱量。

## 2. 近相位与远核合用的显式权重

对a=|yw-xj|，令
\[
 p_A(a)=\begin{cases}
 0,&a=0,\\
 \min\{Aa,\,1,\,a^{-1}\},&a>0 .
 \end{cases}
\]
由gh内积的sin相位及Cauchy–Schwarz，
|<g_w/sqrt(Gw),uj>|<=min{Aa,1}。
当a>=1时317远核界另给<=C_s/a；
当a<1时a^-1>=1。因此所有a>=0有
\[
 |\langle\widehat g_w,u_j\rangle|\le C_s p_A(a).            \tag{1}
\]
常数统一于深度e属于(s,1/2)、dj>=d0，s固定。
同高度a=0时gh精确正交；不通过极限除零定义。

令
\[
 V_j=\sum_{w\in B_j}\omega_w p_A(|yw-xj|)^2,\quad
 V_B=\max_jV_j,\quad V_\Sigma=\sum_jV_j.                  \tag{2}
\]
这是明确的节点距离和正列质量，不把未知||P_B Q||直接命名为新输入。
特别地0<=Vj<=Sj。

## 3. 共同矩阵估计

令B_B的列为sqrt(omega_w) ghat_w，P_B=B_B B_B*。
中心排序后，w属于B_l、w'属于B_j、l!=j时
|yw-yw'|>=D|l-j|-D/2>=D|l-j|/2。
同块gg相关至多1；跨块用317核界及sqrt(omega)双侧Schur权。
定义
\[
 \delta_M=\begin{cases}0,&M=1,\\(1+\log M)/D,&M\ge2.\end{cases}
\]
于是
\[
 \|P_B\|\le S_B(1+C_s\delta_M).                            \tag{3}
\]
分解B_B*Q为本块条目K0和跨块条目K1。
K0的各列非零行互不相交，(1)给||K0||<=C_s sqrt(V_B)。
跨块距离及319的两权Schur给
||K1||<=C_s sqrt(S_B) delta_M。故大T时
\[
 \boxed{\|P_B Q\|\le C_s\{\sqrt{S_BV_B}+S_B\delta_M\}
       =:C_s K_B.}                                      \tag{4}
\]
M=1时不存在跨块条目，delta_M=0精确处理；
M增长时delta_M=O(L/D)，没有sqrt(M)因子。
若B为空，(3)–(4)为零算子结论，不对不存在的行指定正权。

此外，对每个j，本块正泄漏满足
\[
 \langle P_{B_j}u_j,u_j\rangle\le C_s^2 V_j.               \tag{5}
\]
其他B_l是相对j的远深正项，可在完整逐方向响应中由314计入；
不能从(5)误认为P_B只产生本块条目。

## 4. 这一预算解决了什么

它消除了“B为空”对有限矩阵分解的必要性，并提供真正可计算的充分预算。
但没有证明实际B的V_Sigma或K_B足够小；一般含重数计数不是这种结论。
本轮只是当前进度。下一轮把(4)–(5)与全部正项、同一R及总负响应拼接，
再检验新增条件是否有无条件算术验证，而不是凭条件性引理结束整个GOAL。

复核范围及异议处理见[321–323报告](../reviews/2026-09-06/321-323-near-deep-review.md)。
