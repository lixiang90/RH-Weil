# 原 E_X 共同扣项：实际残差与强旧净果

2026-10-28；独占支持稿，待 fresh／root 消费。恢复 README／STATE／Goal／D20261028I、宏观当前入口与唯一 next-trial-common-subtraction-admission，运行 research_state.py check／show，通过结构检查。实际核585原weighted稿§4–5的严格参数域、585主稿及root前件收据、560完整型和原EX建议。没有外网／下载／数值，没有改STATE、cadence或其他稿，没有启动新residual研究预算。

**结论：原共同扣项的 fixed-source 残差仍有原阶正增长，完全是585已付family＋有限HS求和＋560完整型的直接后果，分类0。** 比较空间只作旧后果的见证，原E_X及其扣项规则始终不变；不把更大degree实施为修复，不重验537。

## 1. 冻结的实际对象与规范

保585同一物理 \(\mathscr H=L^2(\mathbb R,dy)\)、实位Sonin空间M、实际有限Euler乘子B_X和正交投影

\[
 \Pi_X=B_XP(PB_X^*B_XP|_M)^{-1}PB_X^*.
\]

Mellin酉表示的norm为dt/(2π)，range为D_XM；B_X不是酉，全部Gram逆／returns保留。源为原physical r=e^(u/2)f，A_r为原时间卷积，在此表示乘 \(\widehat r(t)=\int r(u)e^{-itu}du\)。每个fixed finite X的A_rΠ_X是HS，普通迹域由531／560／585既有收据支付。

固定一个非零实非负 \(r_0\in C_c^\infty((-1,1))\)，令r1=∂r0。则F0(0)=∫r0>0，F1(t)=itF0(t)。先固定共同δ>0及m0>0，使

\[
 |F_0(t)|\ge m_0\quad(|t|\le\delta),\qquad
 |F_1(t)|\ge m_0|t|.
\tag{1}
\]

两源的原du／zero-extension Dlog范数固定，不施双pole-zero假设。共同H0使用585已消费的同一向量及全部poly实际域，不能给两源换两套E_X。

写 \(\ell=\log X\)、\(A=\sqrt X/\ell\)、\(b_X=A/\ell=\sqrt X/\ell^2\)。原weighted§4明给

\[
 \Delta_\delta=4-4/\sqrt{1+4\delta^2}>0,
 \quad C_1c<\Delta_\delta/2,
 \quad n_X=\lfloor cb_X\rfloor.
\tag{2}
\]

这里δ、C1、c均先fixed，且c>0。原稿没有给一个唯一数值算法，而是此严格开放参数family。固定本次原c后，

\[
 V_X=\{D_XpH_0:\deg p<n_X\},\qquad
 E_X=\operatorname{proj}_{V_X}
\]

及原共同C_X(r,s)=Tr(A_rE_XA_s*)都保持不变。E_X是物理Hilbert空间的finite-rank投影；C_X是它诱导的源配对，**不据此把C_X叫作源空间上的finite-rank算子**。原trace／rank粗费为 \(|C_X(r,s)|\le n_X\|r\|_1\|s\|_1\)，不是全线du统一小费。

## 2. 更大空间只作585强旧见证

设 \(c_*=\Delta_\delta/(2C_1)>c\)，取一次固定

\[
 c_+=(c+c_*)/2,
 \qquad N_X=\lfloor c_+b_X\rfloor,
 \qquad W_X=\{D_XpH_0:\deg p<N_X\}.
\tag{3}
\]

因为C1c+<Δδ/2，W_X完整落在**相同已付**weighted／全尾证明的参数范围；不需新PNT、Gevrey、频高运输或误差估计。没有重新优化δ或C1，也没有把原扣项E_X换成W_X的投影。

原585对ALL complex poly的统一结论直接适用于W_X：存在ε_X→0，使每个v∈W_X有

\[
 \int_{\pi/(2\ell)\le|t|\le\delta}|v(t)|^2\frac{dt}{2\pi}
 \ge(1-\varepsilon_X)\|v\|_{\mathscr H}^2.
\tag{4}
\]

同H0／D_X的polynomial map是实际单射，故dim V_X=n_X、dim W_X=N_X，且V_X⊂W_X⊂RanΠ_X。设 \(\widetilde E_X=\operatorname{proj}_{W_X}\)，

\[
 R_X=\widetilde E_X-E_X
 =\operatorname{proj}_{W_X\cap V_X^\perp},
 \qquad0\le R_X\le\Pi_X-E_X.
\tag{5}
\]

这是actual嵌套正交投影之差，不是两个非正投影的形式相减。其rank为

\[
 m_X=N_X-n_X\ge(c_+-c)b_X-1
 \asymp\sqrt X/\ell^2.
\tag{6}
\]

R_X、W_X只用于证明原E_X还留下什么，不作为新扣项方案。所有常数固定；不覆盖c_X趋参数边界等moving-degree规则。

## 3. 原剩余迹：域、有限求和与两个固定源

原共同剩余迹是

\[
 T_X^{res}(r,s)=\operatorname{Tr}(A_r(\Pi_X-E_X)A_s^*)
 =t_X(r,s)-C_X(r,s).
\tag{7}
\]

Π_X−E_X是正交投影，A_r(Π_X−E_X)由旧HS乘有界投影仍为HS，故每个夹心普通迹及mixed产品均合法；不对裸Π_X或Π_X−E_X取未夹紧无限迹。其对角为HS norm平方，(5)给

\[
 T_X^{res}(r,r)\ge\operatorname{Tr}(A_rR_XA_r^*)
 =\sum_{j=1}^{m_X}\|\widehat r\,v_j\|^2_{L^2(dt/(2\pi))},
\tag{8}
\]

其中v_j为W_X∩V_X⊥的真实正交基，全部在W_X内，故同一个(4)对其统一适用。有限正项求和没有无限极限／trace交换；2π已在v_j norm里，不再扣一次。

结合(1)、(4)、(6)，对所有大X分别有

\[
 \begin{aligned}
 T_X^{res}(r_0,r_0)&\ge m_0^2m_X(1-\varepsilon_X)
       \ge a_0\sqrt X/\ell^2,\\
 T_X^{res}(r_1,r_1)&\ge m_0^2(\pi/(2\ell))^2m_X(1-\varepsilon_X)
       \ge a_1\sqrt X/\ell^4,
 \end{aligned}
\tag{9}
\]

其中a0、a1>0固定。这是原剩余投影Π_X−E_X上的actual迹下界，而非把原t_X的lower机械重复后忽略C_X。新正交方向已经在扣项之外，故增长确实没有被这份E_X扣掉。

## 4. 560完整型把同阶增长送到原K_res

取原已冻cofinal X_j=j+1/2，L_j=ℓ_j/2，素数集合{p≤X_j}与{p<e^(2L_j)}精确同一。fixed两源及其mixed自相关最终都由这一F覆盖；全Γ／FP-contact、所有proper powers和完整双pole按560保留。

令K_res,X(r,s)=K_L(r,s)−C_X(r,s)。对同一两源的mixed形式，完整身份为

\[
 K_{res,X}(r,s)
 =T_X^{res}(r,s)-Q_W(r,s)+P_{pole}(r,s),
\tag{10}
\]

\[
 P_{pole}(r,s)=2\langle r,\cosh(u/2)\rangle
                   \overline{\langle s,\cosh(u/2)\rangle}
             -2\langle r,\sinh(u/2)\rangle
                   \overline{\langle s,\sinh(u/2)\rangle}.
\]

Q_W与P_pole在这两个fixed源上只是固定有限矩阵，不需重新使用537正号。由(9)得最终

\[
 K_{res,X_j}(r_0,r_0)\ge a'_0e^{L_j}/L_j^2\to+\infty,
 \qquad
 K_{res,X_j}(r_1,r_1)\ge a'_1e^{L_j}/L_j^4\to+\infty.
\tag{11}
\]

这些是充分lower，非sharp渐近。两对角分别还满足K_res/T_res→1，因为(10)中的差固定；不将比值陈述用到changing-source或未估mixed方向。原source du／Dlog norm未随X变，因此原2×2残差矩阵不可能是entrywise O(1)或矩阵norm O(1)：仅r0这一维见证已足停止“此trial已吸收fixed-source大费”的recipe。

## 5. Mixed、矩阵和方法范围不扩大

同一个Π_X−E_X给T_res的Hermitian正Gram，故mixed只自动有Cauchy–Schwarz \(|T_{res}(r_0,r_1)|^2\le T_{res}(r_0,r_0)T_{res}(r_1,r_1)\)。本稿没有计算它的号、phase或渐近；K_res的mixed项还须按(10)保固定Q／pole矩阵。不得从两个对角增长推出全K_res PSD、二维最小特征值同阶、ALLmoving组合的统一下界或全危险core／补空间cross费用。

此下界使用585已付annulus集中，在物理Sonin投影空间上取补空间；不能将它直接叫作ε Fourier cutoff的core／补空间耦合定理。537已给这两源及其span的净Q正性，重复验证它不产生新whole结果。557 whole leading4/5仍为负惯性UPPER；585局部必要费作为已知输入，均不重验收。

停止范围准确为：同H0／共同fixedδ、原严格已付fixed c degreefamily的这份E_X同步扣项，不能把原fixed-source误差费降成O(1)。没有凭“finite rank”标签排除所有growing-rank补偿，亦未排不同有费投影、source-adapted／非局部、Γ-relative或独立正D′／primitive修复。

## 6. 强旧分类与停止

短依赖链为：**585严格开放degree范围 → 同family更大W_X的已付统一集中 → actual正交补及有限HS求和 → 原T_res的(9) → 560完整恒等式 → 原K_res的(11)**。没有新独立算术输入、新费用机制或未付全尾；只是原585足够性估计对其已付family的直接逻辑后果。对照最强旧，应统一归 **标准直接推论0**，不能因这里第一次打印残差lower就另记数学轮或辅助whole改进。

因此这次EX强旧准入已得到停止证据，不启动residual数学合同，不重做积分／数值或调degree／δ／C1，不换成\(\widetilde E_X\)继续修复，也不续lower／sharp／source／paper。原E_X扣项recipe在此止。cadence3／历史49／cycle16不动，无C049／586；完整独立净signed、primitive容量与corecoupling／Ξ仍欠，长期Goal门open。
