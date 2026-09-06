# 322. 允许近深点后的完整共同日程与质量损失

2026-09-06，持续GOAL周期4第2轮。[T，已通过独立内部复核] 条件性完整预算。
没有验证实际廉价近点条件，因此不满足第十节C的较远期显著进展标准。

## 1. 已知量与新增成本

使用321全部定义；固定k=max{s,1/4+Phi_s(theta)/2}<d0。
保留320的Wj=sum_{Cj}2mw Hw、Wmax和Wtotal；
P=P_R+P_s+P_C+P_B+P_F包含全部正项，mathsf A=P-N含全部负项。
令
\[
 \tau=c+L/D,\quad
 q_B={K_B\over W_{\max}},\quad
 e_B={V_\Sigma\over W_{\rm total}}.                        \tag{1}
\]
两个比值分别控制共同逆变换和总正泄漏，不可互相混淆。
只讨论M>=1，因此Wmax、Wtotal>0。

## 2. 完整逐方向响应和合法求和

相对目标j，其他所选簇、其他B_l和F均在D/4之外。
所以314的逐方向实际远尾适用于
P_far,j=P_F+sum_{l!=j}(P_Cl+P_Bl)，不遗漏其他巨大簇。
本簇负列由316给a_s Wj响应，正簇泄漏<=2c² Wj；
本块未选中近深正项由321-(5)控制，其负项只在下界中合法舍去。
因此
\[
 -\langle\mathsf A u_j,u_j\rangle
 \ge(a_s-\rho_T)W_j-C_s^2V_j,                              \tag{2}
\]
rho_T可取317同样阶的统一上界，D/4只改变固定常数：
C{c²+L²T^-d0+L²T^(s-d0)+L⁴T^(Phi-d0)}。
求和得到(a_s-rho_T-C_s²e_B)Wtotal，而不是M倍最坏簇误差。

## 3. 一个共同lambda与R

沿320的P_C共同界以及319对D/4远集的共同界，再加321-(4)，
\[
 \|PQ\|\le C\{LT^s+L^{5/2}T^{1/4+\Phi/2}
                 +W_{\max}\tau+K_B\}.                   \tag{3}
\]
选择由节点权重决定的日程
\[
 \boxed{\lambda=L^4T^k+\sqrt{\tau}\,W_{\max}
                       +\sqrt{K_BW_{\max}},\quad
        R=\lambda(P+\lambda I)^{-1}.}                    \tag{4}
\]
B为空或K_B=0时最后一项为0，不除以K_B。
令delta=||PQ||/lambda，则
\[
 \delta\le C(L^{-3/2}+\sqrt{\tau}+\sqrt{q_B}).               \tag{5}
\]
Q*Q-I=O(L/D)，所以V=R^-1 Q满足
||V||<=sqrt(1+epsilon_T)+delta=:C_T，
||V*V-I||<=epsilon_T+2 sqrt(1+epsilon_T)delta+delta²。
以VV*/C_T²为共同正收缩并用RV=Q，得有限层证书
\[
 \boxed{\operatorname{tr}(R\mathsf A R)_-
 \ge { (a_s-\rho_T-C_s^2e_B)_+\over C_T^2}\,W_{\rm total}.} \tag{6}
\]
正部符号来自负迹本身非负，不是假设各方向的右侧均正。
没有不同Rj之间拼接，也没有从负谱选lambda。

所选最大簇自身仍给||P||>=b_s Wmax，
Wmax>=c_d0 T^d0/L。因此
\[
 {\lambda\over\|P\|}
 \le C\{L^5T^{k-d0}+\sqrt{\tau}+\sqrt{q_B}\}.               \tag{7}
\]
若q_B->0且e_B->0，则同一R保留(a_s-o(1))Wtotal并满足lambda/||P||->0。
e_B为固定小量时(6)保留相应损失，不能宣称系数仍趋a_s。

## 4. 明确的非空B充分条件与保留范围

一个容易检查但不一定由算术获得的条件是：
存在eps_T->0，使每个原始块S_j<=eps_T Wj。
因为Vj<=Sj，这给e_B<=eps_T、S_B<=eps_T Wmax，
K_B<=S_B(1+delta_M)，从而q_B<=eps_T(1+delta_M)。
它允许B非空且节点距目标并不必趋零，但实际是否满足仍需验证。

另一种可能是近相位小，使V_B远小于S_B；
此时仍必须同时检查跨块S_B delta_M、总泄漏V_Sigma与各自归一化，
不能只看一个有利的局部正交条目。
同高度点可并入对应选中簇而不增加高度直径；只有并簇后其余深点满足320的外部分离条件，
才能直接退回320。若全部B_j都由同高度点组成，可在充分大T时用D/8等固定倍数尺度重用320，
幂指数不变；仍有其他近深点时须继续使用本篇完整预算。不把这一特例冒充实质突破。

本篇当前价值是完整计价的条件性推广，不是无条件算术结论。
若无法独立验证这些节点预算，继续换写它们没有较远期意义。
下一数学动作须检验实际计数／相位信息或剔除损失，并与真正可用的负迹上界比较。

复核范围及异议处理见[321–323报告](../reviews/2026-09-06/321-323-near-deep-review.md)。
