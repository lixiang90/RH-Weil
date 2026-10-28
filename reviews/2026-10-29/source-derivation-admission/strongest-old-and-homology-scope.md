# 源商自导子：最强旧后果与同调范围审计

2026-10-29。只审实际候选，不引入新文献、载体、完成或预算。恢复依据为 G20261027、C056 已耗尽、D20261029M 和 macro frontier；结算前唯一 cadence 仍为 3/history57/latest593/formal18，manifest132。本稿为支持审计，未消费数学轮、未修改 STATE。

**判定：old0。** 下述全代数自导子范围未在 405/516/519/520 中逐字作为定理陈述，但它由这些最强旧资产与有限 Hermite 归一化、特征零有限局部代数的标准计算直接推出。无 continuity/lift/有限包稠密假设的广度确实成立；它没有新付独立算术、成长估计、源的几何实现或 signed 比较，不能凭 HH¹ 命名启动 C057/594，也不恢复已停止的旧谱商载体。

## 1. 精确旧输入及不可缩减的职责

令 F=𝒮_exp,ℂ，M_f(s)=∫e^{su}f(u)du，d=M_f(1)、c=M_f(0)，I 为实际源像的复化，P=P_an,ℂ，本稿 A=F/P，乘法为卷积。

| 旧记录 | 已支付的准确后果 | 本候选使用的职责 |
|---|---|---|
| [405 §5–6](../../../notes/405-f1-adelic-restriction-moments-and-radical.md) | P=I∩ker d∩ker c 是实际闭卷积理想；A≅ℂ²×(F/I) 为代数同构；实际 u_d,u_c 在 A 中给正交次数幂等元 | 保留两个 degree，不把裸 F/I 当完整对象；已有乘法，不再“补建乘法” |
| [516 §1–3、7–8](../../../notes/516-f1-global-mixed-radical-and-mellin-jets.md) | 完整 B 的根空间 R_val=ker d∩ker c∩{M_f(ρ)=0 全ρ}；它只测零阶值，高重数 jets 可存留 | 从 δ 的值坐标为零得到全部 mixed B 为零 |
| [519 §1、3–4](../../../notes/519-f1-closed-source-image-and-degree-moments.md) | 实际 I=R_jet，所有 0≤j<m_ρ 的 jets 恰为核；P=R_jet∩ker d∩ker c；已付实际逆及强空间闭性 | joint degree/full-jet 坐标分离 A，不能把缺乘法、闭像或实际源准入称为本轮新问题 |
| [520 §2–3](../../../notes/520-f1-source-quotient-spectrum-and-centered-growth.md) | 对每个真实 ρ，实际 u_j∈F 满足 M_{u_j}=H₀/(s−ρ)^j，j≤m_ρ；在其他零点保全部 jets；H₀=ξ/2，端点为1/4 | 给每个有限局部块的实际支撑元素；无需无约束 jet 乘积、谱基或有限包稠密 |

405/516 的完整公式为 2B(f,g)=d(f)c(g)+c(f)d(g)−T(f,g)，T=Σ_ρm_ρM_f(ρ)M_g(1−ρ)。该公式包括 Γ、contact、全部 prime powers 及双 pole 的原正规化。它下降到 A，但 B 不是 T；两个 degree 方向仍有双曲项。

## 2. 旧资产的直接标准组合

固定真实零点 ρ，m=m_ρ。520 的 u_m 先乘 Mellin 因子 s(s−1)，得到实际 F 元素 v，其端点为零、其他零点全部 jets 为零、在 ρ 处值非零。对 v 的 ρ-Taylor 级数取次数<m 的逆多项式 q(s)，以 q(−D)v 得 e_ρ。有限次 D 运算保 F。这不是对无限全部零点作插值。

由 519 的准确核，e_ρ²=e_ρ，e_ρe_σ=0（ρ≠σ）；且

    e_ρA ≅ R_ρ=ℂ[t]/(t^m),       t=s−ρ。

这里的同构是有限局部代数的实际同构：满射由 e_ρ 的有限多项式乘子给出；单射由 degree/full-jet 核给出。405 的两个 degree 幂等块同样为 ℂ。不声称这些块的代数直和等于 A，或 A 是无约束无限乘积；全局单位也未被假定。520 的 −D 是卷积乘子，中心化平移是线性/module 作用，二者不能被误称为这里的 Leibniz 导子或卷积代数自同构。

现在令 δ:A→A 为任意 ℂ-linear Leibniz 导子。任何幂等元 e 都有 δe=2eδe；即使 A 无单位，线性算子 (Id−2L_e)²=Id 也迫使 δe=0。因此 δ(ea)=eδa，导子保持每个上述有限块。局部有

    0=δ(t^m)=m t^(m−1)δt，故 δt∈tR_ρ。

于是每个 ρ 的常数项均为零，两个 ℂ-degree 块也被 δ 杀掉。更准确的逐块后果是

    j_ρ(δa)=v_ρ ∂_t j_ρ(a)，       v_ρ∈tR_ρ。

该式仅给每个已有 δ 的必要局部形式，不声称任意 v_ρ 族都能胶合为 A→A。它还表明自导子不能把不同零点或 degree 相互运输。joint 坐标分离使此逐块论证足够，不需连续性或有限谱包近似。

故标准组合的最强直接后果为

    δ(A) ⊂ R_val/P = rad(B_A)，
    B_A(δa,b)=0 对所有 a,b∈A，且 d(δa)=c(δa)=0。

高阶 jets 不一定消失。此理想在每个有限局部块为 nilpotent；实际重数未有全体统一上界，不把 R_val/P 叫作全局 nilpotent ideal、nilradical 或已知统一 nilpotence 指数。

若全部零点简单，则所有局部块均为 ℂ，joint degree/values 分离 A，所以 δ=0。若某个 m≥2，投影 a↦e_ρa 后在该块取 t∂_t，再嵌回 A，给实际非零自导子；它仍落在 full B-radical。于是

    Der_ℂ(A,A)=0 ⇔ 全部非平凡 ζ 零点简单。

这不是 RH 等价，更不证明简单性。其“若存在重零点则有非零导子”不要求实际存在重零点，也不将该导子的非零性换成 Weil 非根性。

## 3. 原物理源及完整目标的消费

候选严格为 J_δ(r)=δ([f])，f(u)=e^(−u/2)r(u)，输入至少满足 f∈F。输出是 A 中类；本论证没有把它命名为几何除子、实际 HH 链或原 Green pair。它按定义消去 P，不因此满足独立 principal 来源或非根准入。

[552 §1](../../../notes/552-radial-adelic-green-principal-and-comparison-gate.md)记录原物理恒等式 Q_W(r)=2d(f)c(f)−2B(f,f)=T(f,f)（实源；复源用相应 Hermitian 极化）。自导子的 degree 和所有零点值均零，所以它的完整 pullback 恒为零；与任意其他 A 元素的 mixed B、T 也零。若另加 degree 修补，B 可出现双曲项，但那些 degree 方向仍无 T，故完整 Q_W 仍为零。不能把恢复 endpoint 的裸 B 值误报为独立 Weil 正性。

[537](../../../notes/537-source-exact-weil-window-positive-tail-admission.md)已给 fixed17/16 内每个非零 complex 物理源 Q_W>0。这一真实非根见证不能被 J_δ 保持。因此该候选不能承担主线要求的同一非零 primitive、实际非根的完整 Weil 比较；不是先证明其几何 principal/截面/RR 就能补救的遗漏。

逐源选择不同的合法 δ、有限和或再乘 A 中因子仍在该 radical；若采用 A 原强商拓扑的合法极限，radical 闭性也保零。此范围不含改变值域、另添非根源项、换 pairing/metric、非 Leibniz 映射或没有该拓扑收敛的无界过程。

## 4. 为什么这是 strongest-old 后的 0

这里不是因为“旧 exact 公式可以代入任何新东西”就判 0。所需实际输入全部已在固定旧 F 中：520 已给逐零点局部函数，405 已给代数及 degree 幂等块，519 已给完整 joint 核，516 已给配对恰只测值。剩余有限 Hermite 逆与 δ(t^m) 是标准有限代数步骤，不引入新的算术适用范围、统一高度估计、原物理 norm/growth 控制或未知 signed coupling。

应保存的确切增量是把已有分解的标准推论写明，从而关闭“在同一 A 上另选任意 algebraic 自导子就能产生 primitive 非根”的提案。它不是已有文中逐字宣告的定理，也不是新的独立源方法类净后果；不能用普适量词、HH¹ 标签或重新编号补出数学预算。与 593 的实际 moving-source 渐近 norm loss/candidate 反例不同，此处没有旧资产未蕴含的全对象或成长结论。

原 Goal 所需独立 arithmetic primitive→principal/Green→整过滤/截面乘法→mixed RR→同一完整 Weil 比较均未新增；542+555→557 的 whole leading4/5 负惯性 UPPER 未动，关键瓶颈未变。本局部候选选择应停止，Goal 仍 active/open/noteligible。

## 5. HH¹ 与旧非交换 HH₁ 必须分开

对这个交换 A，通常代数 Hochschild cochain 约定下 HH¹(A,A)=Der_ℂ(A,A)，因为 inner derivations 为零；非单位情形也只需通常 degree1 计算。本稿讨论的是上标¹、值域及双模为 A 的自导子，不是 HH₁，不推出 Ω¹_{A/ℂ}=0、对任意 A-module 的导子为零或更高/relative/cyclic 群消失。

[430](../../../notes/430-f1-source-stable-periodic-smoothing-algebra.md)的实际对象是原 u,V 及周期平滑核生成的指定非交换扩大域；[431 §4、6](../../../notes/431-f1-source-orbit-essential-symbol-and-boundary-injectivity.md)给有限 Γ 扭曲乘法及真正非交换子商，不是本 A 的 Mellin jet 交换代数。
[432 §1–2](../../../notes/432-f1-relative-cycle-charge-and-source-invariant-cutoff.md)定义的是 Q_src=A_src/S₁ 上 HH₁ 的规范电荷 Ω(c)=Tr Σ[A_r,B_r]，前提为商上一循环；旧角点值为 −4∫s h(s)k(−s)ds。自导子零不对该 homology 电荷施加任何消失结论。

[573 §1–6](../../../notes/573-relative-ideal-chain-closure-and-regulator-loss.md)进一步证明：由一个真实 537 非根源的加权边界生成 J_*，其商可令链闭，却有 T,T*∈J_* 且有限秩交换子迹 −4；故原432电荷不能沿相应 HH₁ 商映射下降，闭理想为 overline(D_src)。这是已付的非交换 relative pair 的限定反测，不能归并成“所有 HH 为零”，也不由本 δ 计算重证。其它 regulator、relative/higher 边、不同值域及有独立比较的无限转移仍须各自准入。

[402 §3–5](../../../notes/402-f1-intrinsic-ff-diagonal-conormal-obstruction.md)的普通 Ω_{C/ℚ_p} 及 FF 普通平方是另一个明确 pair：其非连续普通代数微分不有限维。A→A 自导子结论不抵触它，也不给连续/导出几何的免费替代桥。

**停止条件已满足：** 将本候选记为旧分解的显式标准推论，不新开数学合同或改写旧谱商停止决定；下一准入必须有不同的实际 source/pair、537 非根测试及 strongest-old 扣除后的净后果。本文未查询/下载新资料，未触动 cadence、STATE、Git 或文献 manifest。
