# 有限覆盖的 whole-cusp 读出：标准运输与强旧扣除

2026-10-27；同 G20261027、runtime createdAt1793085111 和原0c4f基线。本次执行 STATE 唯一准入动作，不恢复 C047 预算、不建立 C048/585。root 实际逐项核两独占稿；最终 fresh／消费范围和绑定版本见[前件收据](../../reviews/2026-10-27/finite-cover-trace/root-consumption-scope.json)。本文件出稿不等于最终消费。

## 1. 实际门与可消费证明

对象是任意有限指数 modular subgroup 的 coarse 紧化曲线 X、实际 j-cover π:X→P¹、全纯复微分 ω 和每个 whole cusp 的固定复权。Γ 不含 −I 时先取 PSL₂ 的像；width 按 coarse cusp 定义。输入仍是全部复 S_exp 物理源 r=e^(u/2)f，读出为 R_c(r)=Res_c(L_r(π)ω)。没有把 essential 奇点当作有限阶除子。

[运输原稿](../../reviews/2026-10-27/finite-cover-trace/orbit-trace-transport.md)中取 t=q_c、x=t^w、z=J(x)，ω=Σ a_n t^(n−1)dt，明确得到

\[
 T_c(J(x))=\sum_{\text{whole orbit}}\frac{\omega}{d\pi}
 =\frac{\sum_{m\ge1}a_{mw}x^m}{xJ'(x)}=O(z^{-2}).
\]

单 sheet 的1/w恰被完整轨道的w项抵消，w∤n 的项消去。Ω=C\[0,1728] 的基本群非平凡，但其∞ monodromy 保持 whole orbit，足够使 T_c 单值。0上的 coarse ramification e∈{1,3}，1728上e∈{1,2}；ω全纯使两端至多2/3、1/2次奇性。故复 jump ν_c=(T_c,+−T_c,−)/(2πi) 属 L¹[0,1728]；对复ω不能改用 Im/π。

Cauchy给 T_c(z)=−∫ν_c(t)/(z−t)dt；正向 cusp 圈映成顺时针基圈完整轨道，第二个负号抵消，准确有

\[
 R_c(r)=\int_0^{1728}L_r(t)\nu_c(t)dt.
\]

端点小圈、∞大圈和全部非compact源尾均已控制；无额外原子、polynomial或1/w。精确局部参数 π=v^(−w) 下的 residue 系数提供独立方向检查。全cusp等权总和为0，是边界线性约束。

## 2. 原范数与量词

每个固定 Γ/ω/mask 有自己的 C=||ν||₁。对 N>1728，费用为 C(1/N+1/(N−1728))p_(N,0)(r)。fixed supp r⊂[−L,L] 的原du费用可取 C√(2L)e^(1728L)，原 zero-extension Dlog 再乘1/√log2。没有跨level统一C，没有全线原norm统一界，也没有把584特有的正端点或 sharp 正增长复制到任意复读出。

## 3. 必须扣除的强旧后果

[405](../../notes/405-f1-adelic-restriction-moments-and-radical.md)的实际正H与全平移 p_b=(D²−1/4)H(·−b)在同 S_exp 中；M_H(t)>0 对实t成立。[584§5](../../notes/584-marked-cusp-borel-kernel-and-pan-residue-collapse.md)已经消费 compact-real Laplace 唯一性：若读出杀全部p_b，则 (t²−1/4)M_H(t)ν(t)=0；L¹无pole原子，遂ν=0。

[强旧原稿](../../reviews/2026-10-27/finite-cover-trace/old-consequence-and-repairs.md)对固定有限组读出 B 给有限维 annihilator 比较，得到

\[
 \operatorname{span}_{\mathbb C}\{B(p_b)\}=B(P_{an})=B(S_{exp}).
\]

因此同B后的任意后处理若将**全部**Pan关系（包括有限复线性组合）送到同一base，便在整个源像常值。多坐标非线性不能只测试孤立的p_b。对于无限坐标这里只得到 product 拓扑的稠密性；连续常值延拓另须 Hausdorff 目标，不能据此宣布更强拓扑的精确商为零。

## 4. 计轮、瓶颈和停止

本次只是584的slit-Cauchy加标准有限覆盖trace，再接已经消费的405唯一性及有限维对偶。没有新的独立算术输入、定量完整Weil界或非标准比较原则，按**旧推论准入审查0数学轮**保存。单cadence保持2／历史48／formal cycle16；最新完整数学仍584。没有C048/585，没有因family量词另计一轮。

停止当前fixed finite whole-cusp residue数据的level/cusp/basis/mask调节及仅依同数据的lift/height包装。保不同实际source-map、额外relative数据、meromorphic额外pole、complex/unbounded谱、强或无限目标拓扑、源适应和未逐层消Pan的D′正逼近；这些是未覆盖范围，不能当作已获的新输入。仅依B的源适应后处理仍受同像结论。

最强经典后果仍542+555→557 whole leading4/5负惯性UPPER。独立非零primitive源、整过滤／截面乘法／mixed RR、完整Γ/contact/properpowers/双pole与全源成长signed、actual core/coupling/Ξ仍欠。实际主瓶颈未变；本小类的标准推论不满足长期Goal完成门。

## 5. 唯一下一动作及为什么有信息差

仅准[完整 oldform tower 的联合数据／583坐标比较](../../reviews/2026-10-27/finite-cover-trace/next-joint-oldform-tower-admission.md)。它有全部d的实际公式，测试有限像结论未覆盖的无限联合及拓扑；不是选新level找一个通过Pan的单腿。先扣583 raw注入和连续principal完成化已知结果，若只是坐标自同构按0旧比较止，不预数学合同。不同时续period/paper/height。

该比较胜过重做finite reader：后者已由本次强旧链直接处理；也胜过给“relative修复”命名，因为尚无那样的新源实物。只有真实不同的合法拓扑／principal数据和同源净后果才会改变决策，单纯保留raw信息或非闭商标签不会。

本次复用405/583/584及其既有来源，无新增外部论文或全文下载；[文献范围记录](../../literature/supplements/2026-10-27-finite-cover-trace-source-scope.md)只记录实际复用，不冒称新原证明审查。当前审查／同步阶段以STATE为准。
