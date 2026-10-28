# Sonin bare 正迹的 cofinal 概率平均：585 的直接旧后果

2026-10-28；`/root/rational_first_gate` 独占准入稿。已恢复 README／STATE、check→show、同 G20261027／原0c4f、AD、frontier／summary 和已耗尽 C049。STATE 当前实际动作正是本次 fixed-source 凸组合比较，未准新合同／来源。运行实例按 root 最新观察仍为 createdAt1793085111 active；本子任务 get_goal 返回 null，不把它误作 root Goal 终态或另建实例。本稿只读585／560及 post-lower 必要消费范围，不重证原 lower、不做全库存／web／新source／参数候选，不改 STATE／Git／cadence。

**结论：拟比较成立，且是 585 固定源发散加 560 正迹非负性的标准直接旧后果，净分类0。** 任意满足所给 cofinal 条件的有限概率混合，其 bare trace 在每一先固定非零 compact smooth complex 源上趋于 +∞，不能趋向该同一源的有限完整 Q_W。它没有新增 signed/core 信息、改变当前选择或取得后继资格；不能据此复活来源检索／泛形成／旧 lower 预算。

## 1. 对象、域与最强旧短链

沿 [585 §1](../../../notes/585-cofinal-sonin-fixed-source-trace-lower-and-core-error-fee.md)，物理源为 `r=e^(u/2)f`，固定

\[
 0\ne r\in C_c^\infty(\mathbb R;\mathbb C),\qquad
 A_r=\int r(a)U_a\,da,
\]

且 `X≥2`，`F_X={p≤X}`，Π_X 是到真实 B_X M 的物理正交投影，含原完整 Gram 逆／returns。此处 r 是原 du 源，不是 ambient evaluator／receiver；保持 Fourier `dt/(2π)` 与 zero-extension Dlog。

[560 §1、§4](../../../notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md)已支付 finite X 的 ordinary trace／HS 准入及

\[
 t_X(r)=\operatorname{Tr}(A_r\Pi_X A_r^*)\ge0.
\]

585 §1 的**已证输入**是：对每个上述先固定 r，令有限 `k=ord₀ rhat`，存在依 r 的 `c_r>0、X_r`，使

\[
 t_X(r)\ge c_r\frac{\sqrt X}{(\log X)^{2k+2}}
 \quad(X\ge X_r),\qquad t_X(r)\longrightarrow+\infty.
\]

本稿只消费最后这个已经支付的全 cofinal 极限；不重开共同向量、VK／Euler 权、全多项式集中或 tail 证明。它比“存在一个发散子列”强，正是下节尾部一致阈值所需前件。

## 2. 所给概率平均的实际不等式

只审题定规则：每个 j 有有限概率测度

\[
 \mu_j=\sum_i w_{j,i}\delta_{X_{j,i}},\quad
 X_{j,i}\ge2,\quad w_{j,i}\ge0,\quad\sum_iw_{j,i}=1,
 \qquad
 \forall R\ge2:\ \mu_j([2,R])\longrightarrow0.
\]

仍先固定上一节同一个非零 r。任取有限 `M>0`，由585已有极限，选有限 `R≥2` 使全部 `X>R` 都有 `t_X(r)≥M`。小 X 部分仍非负，因此准确有

\[
 \begin{aligned}
 T_j(r)&:=\sum_i w_{j,i}t_{X_{j,i}}(r)\\
 &\ge M\sum_{X_{j,i}>R}w_{j,i}
 =M\bigl(1-\mu_j([2,R])\bigr).
 \end{aligned}
\]

从而 `liminf_j T_j(r)≥M`；因 M 任意，

\[
 \boxed{T_j(r)\longrightarrow+\infty.}
\]

这是同一固定卷积平方 `h_r=r*r*` 的对角值比较，不要求每个支点 X_(j,i) 单独趋无穷，也不要求每个支点超过共同阈值；逃离每个有界区间的**总概率质量**已经够。有限和保证每层值有限，无需交换两个无限积分或调用未付的 uniform integrability。这里没有重新证明585，也没有新算术前件。

对该固定 r，完整 Q_W(r) 为有限常数；compact 自相关只见有限多个 prime-power 位置，Γ／FP-contact 与双 pole 在原光滑源域也有限。所以 T_j(r) 不能在这个**同一先固定** h_r 上趋于完整有限 Q_W(r)。若候选声称对全部 fixed compact complex 卷积平方成立，只此一份非零 r 即可拒绝；事实上上式对585的每个先固定非零 r 分别成立。

## 3. 完整 K 与双 pole 保留：本结论只判 bare trace

取同一个 fixed I=(−L,L) 包含 supp r，并对**所有** X≥2 使用原 `K_X=K_(F_X,I)`；不拿一个可能不容纳 r 的小源窗替代它。记 `R_r=r*r*`，把尚未覆盖的可见 prime-power 缺项保为

\[
 C_X(r)=-\sum_{p>X,\ k\ge1}(\log p)p^{-k/2}
       [R_r(k\log p)+R_r(-k\log p)].
\]

fixed compact 自相关使这份和仅有有限个可见位置，故 `|C_X(r)|≤B_r<∞`，并且全部 `X>e^(2L)` 时 `C_X(r)=0`。560 的原字典对每个合法 X 准确给

\[
 Q_W(r)=t_X(r)-\langle r,K_Xr\rangle+P_{\rm pole}(r)+C_X(r),
\]

\[
 P_{\rm pole}(r)
 =2|\langle r,\cosh(u/2)\rangle|^2
  -2|\langle r,\sinh(u/2)\rangle|^2.
\]

完整 Γ=`Reψ(1/4+it/2)−logπ`、FP/contact、全部 Λ(p^k)=logp 及两 pole 都在这条旧身份中；支持外相关零是原 exact 运输，并非删去 proper powers。此处没有要求双 pole moments 为零，odd pole 的负号仍保留。

对本题的原概率权定义 `barK_j(r)=Σ_i w_(j,i)⟨r,K_(Xji)r⟩`、`barC_j(r)=Σ_i w_(j,i)C_(Xji)(r)`。取覆盖阈值 `R_cov>e^(2L)` 后，

\[
 |\overline C_j(r)|\le B_r\mu_j([2,R_{\rm cov}])\longrightarrow0,
 \qquad
 \overline K_j(r)=T_j(r)+P_{\rm pole}(r)-Q_W(r)+\overline C_j(r).
\]

因此 `barK_j(r)/T_j(r)→1`。一般 cofinal 概率测度仍可有低层质量，所以 **barC_j 只是趋零，不是每个 j 精确零**。若层用585的 `X_n=n+1/2` 编号，则 C_n 是固定源的有限 prefix 缺项；以上仍须用同一 fixed I 定义全部 K_n，不能让小 L_n 的窗漏掉 r，也不能无声加强为所有支点均已覆盖。

585 §4 已说明固定 r 时实际 K 与 t 同为必要成长大项；本处保留 C 后准确平均了完整字典。**bare trace 的概率平均发散不能判完整 corrected traces 发散或失败**：原 `T_j−barK_j+P_pole=Q_W−barC_j→Q_W`，若连 missing-visible-prime 缺项也计入，则完整等式逐层／平均都保留。这个身份本身没有证明目标正号。固定 pole 是常数，无法把 bare trace 的 +∞ 变成有限值；真正不能略去的是同量级 K 及低层未覆盖时的 C。

本稿不把 t_X≥0 推成 Q_W≥0，不把 K 的最终 fixed-r 正成长推成 K 在每层对所有源 PSD，也不推577的 q_R 不消失。与 [post-lower §2](../../../goals/reviews/2026-10-28-causal-choice-after-sonin-lower.md) 已付的 fixed-r `K/t→1`、固定 fraction 反测相同，这项比较只说明原两腿需要保同量级 signed 相消，不支付相消后的净号。

## 4. 量词、norm 与覆盖限制

* r 必须先固定、非零、compact smooth、complex；常数和阈值依 r。没有证明 changing-source r_j 的平均发散，也没有从585扩到任意 Dlog／全 S_exp 源的 lower。
* 证明用同一原 du 源与 Π_X 的真实正迹。du／Dlog 范数对先固定 r 是有限常数；不产生全线统一 operator bound／lower，也没有平均后的成长速度。质量逃逸可任意慢，不能直接保留585关于 X 的 rate 为一个未经给定的 j-rate。
* 权非负与质量1、全部 X_(j,i)≥2、所述 cofinal 质量条件是本比较的前件。不能泛排 signed 权、非概率质量或不 cofinal 的规则；它们不由本不等式决定，也没有被本稿赋予成功身份。
* 允许混合中保有小 X 支点，只要求其总质量趋零。若规则源适应，只有对被审同一 fixed r 仍实际满足这些前件时，本不等式才适用；不把标签当自动覆盖。
* 只拒绝把这些 bare 正迹平均值指定为完整型对角值的收敛身份。没有判所有非局部／joint signed、有费减法、Γ-relative 修复、非概率归一化或 full corrected traces，也没有证明一个一般正 D′ 策略无效。

## 5. 最强旧去重与后继资格

最短已付链就是

`560 ordinary positive trace` ＋ `585 每先 fixed 非零 r 的 t_X→+∞`
`→ T_j(r)≥M(1−μ_j([2,R])) → T_j(r)→+∞`。

只用正数的有限概率平均和已证尾部阈值，强旧前件已经决定整个题定比较，不是借“计算简单／局部失败”才记0。此刻把结论显式写成概率平均，并没有新增独立 source、principal／primitive、signed 缺陷消失、core/cross 净费或完成门所需的实质方法类边界。

所以它**不改变 AD 后的当前投入选择，也不构成重新准入的真新比较**。本稿完成这一个具体核账即旧0止，不复活 C048 lower／C049、C050／587、来源／搜索／paper／参数或泛形成计划，不以需要 next 为理由续预算；当前没有由本比较产生的已准后继。

whole 542＋555→557 leading4/5 仍只负惯性 UPPER；关键 primitive/principal/mixed、完整 signed 消失及实际危险 core/cross 未改。同实例 Goal 仍 active/open/noteligible；本稿无数学计轮、无 formal18／归零，不改变原 cadence0/history50/latest586/formal17。草稿需 root 消费，不能自行作为总体结果。
