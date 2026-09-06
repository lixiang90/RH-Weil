# 310. 正则化可见性：探索准入与完整符号账本

日期：2026-09-06。phase 2 第 1 轮；VIS-REG 主探索。
本轮目标是核清一个可研究的候选，而不是把经典线性代数记为新算术结果。
旧命题重叠及原始文献审计运行中；后续实际估计仍 [O]。

## 1. 精确对象、目标和停止条件

固定 302／304 同一实际有限零点前缀及原始高度规范，在实型 Hilbert 空间 W 上写
\[
A=P-UU^*,\qquad P=BB^*\ge0.
\]
B 的列是所有 \(\sqrt{m_x}f_x\)、\(\sqrt{2m_z}g_z\)，
U 的列是所有 \(\sqrt{2m_z}h_z\)；每个不同非实共轭对只索引一次。
因此没有丢掉其他非实对的正项。先取 sharp MT 半宽 \(A(T)=\log T/2\)，
并保留 302 较窄窗作为对照，不在两种窗之间借用未证明的一致性。

对 \(\lambda>0\)，取 \(R_\lambda=\lambda(P+\lambda I)^{-1}\)。
研究完整压缩 \(C_\lambda=R_\lambda A R_\lambda\) 及其实际负迹，
不能单独把负向量残余当负迹。初始参数 λ 可依赖 T 及独立可核算的正背景界，
不能通过预先计算待证明的完整负谱来指定一个廉价日程。

已有硬商保持负秩却可丢失负迹尺度。所需新输入是：在同一实际对象上，对 λ 的一个非平凡范围，
独立控制正背景泄漏和负响应的差，或证明一个候选统一日程必然支付不可接受的代价。
基础 resolvent 恒等式、惯性不变和旧 Schur 判据仅作工具。
若 4–6 轮只得到这类重写、旧反例或无净改善，则停止 VIS-REG 并切换。

## 2. Tikhonov 残余不等于压缩负迹 [T，经典重建]

对任意 h，配方或正规方程给
\[
\inf_a(\|h-Ba\|^2+\lambda\|a\|^2)
=\langle h,R_\lambda h\rangle,
\quad a_\lambda=B^*(P+\lambda I)^{-1}h,
\quad h-Ba_\lambda=R_\lambda h.
\]
所以最小目标同时包含残余和系数代价；并非 \(\|R_\lambda h\|^2\)。
由 \(P=\lambda(R_\lambda^{-1}-I)\)，完整压缩严格为
\[
C_\lambda=\lambda R_\lambda(I-R_\lambda)
             -(R_\lambda U)(R_\lambda U)^*.
\tag{1}
\]
正背景泄漏的每个特征值不超过 \(\lambda/4\)，但维数增长的总迹仍须支付。
记 \(M(\lambda)=U^*R_\lambda U\)，则
\[
U^*R_\lambda^2U=M(\lambda)-\lambda M'(\lambda).
\tag{2}
\]
这里导数对固定有限配置计算；若 T 与 λ 同时变化，不能据此声称统一极限可交换。

标量反例：\(P=1,U=1\) 时 \(A=C_\lambda=0\)，但
\(\langle U,R_\lambda U\rangle=\lambda/(1+\lambda)>0\)。
故正的 Tikhonov 残余不证明存在负方向。
更一般取 \(P=\operatorname{diag}(1,N+\varepsilon)\)、
\(U=\sqrt{1+\varepsilon}\,e_1\)，则 \(\operatorname{tr}A=N\)、
\(n_-(A)=1\)、\(\operatorname{tr}A_-=\varepsilon\)。
正则化残余可有固定正尺度而负迹任意小。这是抽象接口反例，不是实际 zeta 模型。

## 3. 原始负谱和阈值问题仍在 [T，经典重建]

由于 \(0<R_\lambda\le I\) 可逆，有限维 Sylvester 惯性律给
\(n_-(C_\lambda)=n_-(A)\)。又由负迹的变分式，
\[
\left(\frac{\lambda}{\|P\|+\lambda}\right)^2\operatorname{tr}A_-
\le \operatorname{tr}(C_\lambda)_-\le\operatorname{tr}A_-.
\tag{3}
\]
右界因为正收缩合同不增加负迹；左界对 \(A=R^{-1}CR^{-1}\) 使用相同估计。
\(\lambda_1\le\lambda_2\) 时，\(R_{\lambda_1}R_{\lambda_2}^{-1}\) 是正收缩，
故压缩负迹随 λ 单调不减。对固定 T，λ↓0 回到硬商，λ→∞ 回到 A。
这没有提供独立的 \(\operatorname{tr}A_-\) 估计，不能记为解决其预算。

令 \(K_\lambda=(P+\lambda I)^{-1/2}U\)，则
\[
(P+\lambda I)^{-1/2}(A+\lambda I)(P+\lambda I)^{-1/2}
=I-K_\lambda K_\lambda^*.
\]
因此
\[
n_-(A+\lambda I)=n_+\big(U^*(P+\lambda I)^{-1}U-I\big),
\quad
\operatorname{tr}A_-=
\int_0^\infty n_+\big(U^*(P+\lambda I)^{-1}U-I\big)d\lambda.
\tag{4}
\]
第二式只是逐个负特征值的长度积分。它准确表达所需阈值控制，尚未缩小实际算术输入。
严格大于 1 的特征值被计数，等于 1 对应零特征值，不能混淆。

## 4. 可继续尝试的有代价逼近

若能独立构造 \(U=BC+E\)，且 \(\|C\|\le\kappa<1\)，则对任意 x，
将 \(U^*x=C^*B^*x+E^*x\) 配方给
\[
\langle Ax,x\rangle\ge-\frac{\|E^*x\|^2}{1-\kappa^2},\qquad
\operatorname{tr}A_-\le\frac{\|E\|_{\rm HS}^2}{1-\kappa^2}.
\tag{5}
\]
标量优化依据 \(t^2-(\kappa t+e)^2\ge-e^2/(1-\kappa^2)\)。
完整正项背景不能省略，κ 的缺口也不能吞入不一致常数。
硬投影只给小 E；它不约束实现此逼近的 C。下一轮先审计该条件与既有 capture／shorting 结果的重叠，
并检查实际单个非实对和实背景的系数代价；没有独立的 κ／E 输入时不晋级。

## 5. 本轮状态

以上是有限线性代数的明确账本 [T]，主证明不以实验替代；新颖性不宣称。
它排除了几种错误解释，但本身不满足 phase 2 的“新增实质成果”验收。
[独立重叠及符号审查](../reviews/2026-09-06/310-overlap-and-sign-review.md)已完成；原始文献已按获取状态归档。下一轮见[311日程与系数成本](311-regularization-schedules-and-coefficient-cost.md)。
