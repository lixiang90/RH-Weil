# 任意正 Euler 增量：独立准入首检

2026-10-28；G20261027/runtime1793085111/原0c4f。本稿接收 root 本次明确提出的更强候选，原 rational-euler-surgery/first-gate.md 保持原字节。只作准入咨询，不批准 C050/587，不发完整证明，不改 STATE/cadence/Git。已按 README/STATE/check→show 恢复 Goal/C049/D20261028U/宏观前沿；读取旧261-B、405§4、561§1–2、565与128–130相关严格范围，并对 notes/reviews 的正增量、monotone Euler、刚性词作限定去重。

**首检结论：候选成立的逻辑链可闭，未发现反例或隐藏的有限阶假设；它比有限 rational(s) 手术有实质更大的准确范围。** 它应称为“经典完成背景中的 global Euler-log 正增量刚性”，不是一般正 Beurling 系统唯一性、全 signed 修复边界或经典 Weil 正性。旧 Landau 机制是明确依赖，不冒称新的外部定理；目前未在所核旧件发现同等范围的实际结论。

## 1. 冻结的输入／可判门／净后果

1. **实际输入：** (0,∞) 上正 Borel 测度 Δ，某实 σ0 的 ∫exp(−σ0u)dΔ<∞。在其右半面令 Z=ζ exp(LΔ)、E=ξ_Riemann exp(LΔ)。E 由该真实 germ 全平面 entire 延拓，并满足 E(s)=E(1−s)。不预设有限／离散支撑、rational ratio、整函数有限阶、未知根位置、生成规则局部性或源无关性。
2. **最便宜可判门：** 令 F=E/ξ 为全域 meromorphic ratio、ν=uΔ。核 H=−F′/F 的正 Laplace 表示能否穿过每个实点；若 ν 的收敛横坐标有限，旧261-B所迫的实奇点是否可能由 F 实零点承担；若横坐标为−∞，midpoint 的合法 FE 导数是否迫非负积分为0。
3. **扣旧后的实际净值：** 若严格证明，全部这样的 Δ 必为0。因而在 exact classical Γ、无额外 completed poles 与同一 FE 下，向原 Πζ 单调加入任意全局正 Euler-log 测度，不能形成非平凡新完成对象。含任意变尺度／源适应／非局部的构造规则，只要其每个最终输出仍满足这些 global 条件；并无对整个规则族的 uniform 增长费用主张。

它不再局限有限 divisor，也不要求新序列 finite-order 或固定 degree；这与有限有理候选的范围不同。它会改变“只加正 Euler 数据来修补完成对象”的路线选择；不会给 actual ζ 的原全 Weil 型增加一个正号。

## 2. 首门必须支付的解析责任

**uΔ 的域。** 原右半面的有限指数权使 Δ 在0附近已有有限质量。故 ν=uΔ 在0附近有限；对任意 ε>0，u exp(−εu) 有界，给 ν 在稍右半面的可积性和 H(s)=Lν(s)。不用假全实 Laplace 收敛。令 c 为 ν 的收敛横坐标；已知 c<+∞，而 c=−∞ 须经下门证明，不可先用 midpoint 积分。

支撑限定 (0,∞) 也支付归一化：沿实 σ→+∞，支配收敛给 LΔ(σ)→0，故 F(σ)→1。若允许0处的正原子，ν 会丢掉它，F≡exp(Δ{0}) 就是保 entire/FE 的常数反例；因此结论不能无声改成允许 δ0。

**全域 ratio 与实点。** E 不恒零，因为其右半面 germ 非零；E 的实型由这个 germ 的 Schwarz 对称与延拓唯一性推出。旧405的 h>0 和 M_h(s)=ξ(s)/2 给每个实 s 的 ξ(s)>0，因此 F 在整个实轴全纯、无实极点，但此刻仍允许 F 的实零点。不能直接说 F 在实轴正、也不能在 F 可能为0的点取 log。

**有限 c 的两个分支。** H 在 Re s>c 与 Lν 的身份由 meromorphic 恒等定理从原 germ 延伸，后者在该半面全纯。若有限 c 处 F 非零，H 在 c 全纯，违反旧261-B经 Y=e^u得到的正 Laplace 实边界奇点。若 F 在 c 有 m 阶零点，H 的主部是 −m/(s−c)，从实右侧趋于负无穷，违反 Lν(σ)≥0。F 不能在 c 有极点，正是实 ξ>0 和 E entire 所付的关键输入。这一负残数检查不可省。

**midpoint 的合法性。** 有限 c 被排后，Lν 在全 C entire，且等于全域 meromorphic H；于是 H 没有极点，F 不能有任何零或极点。此后才可在1/2消费 F(s)=F(1−s)，得到 H(1/2)=0。正测度的合法积分 ∫u exp(−u/2)dΔ=0 迫 Δ=0，因为权在全部 u>0 严格正。这里不额外假 F 正实，也不用 Hadamard、finite order 或渐近根计数。

以上只是准入阶段确认各责任有直接可核的闭合路径，不替 root 的正式 proof/fresh/root-consumption。

## 3. 两个必要性负对照

* **不要求 FE：** 固定 a,c>0、Δ=cδ_a。F(s)=exp(c exp(−as)) 为非平凡 zero-free entire，E=ξF entire，原 Γ 保持，但 F(s)≠F(1−s)。这是实际任意正 Euler-log 测度类中的反测；不是把该 Δ 免费称为来自正 primitive 的全 repeats。它还说明取消 finite-order 以后，FE 确有责任。
* **不要求 E entire：** 旧561的 Z_c=1+c/[s(s−1)] 在其允许参数内有正的实际 Π_c=q_c(u)du，并满足 Z_c(s)=Z_c(1−s)。取 Δ=Π_c、F=Z_c，则 E=ξZ_c 保同一个经典 Γ 乘法背景和 FE，却在实0、1有额外 pole，因为 ξ(0)=ξ(1)=1/2。旧 Γ=0 模型不是本命题的反例；本例只展示 entire 前件不可删。

严格保原双 pole／minimal s(s−1) 的子类可另要求原 bare Z 在0、1的相应非零残数条件。本命题若结论 Δ=0 成功，本身已恢复原对象；但在准入前不能单凭 E entire 宣称任意候选原 pole 都保留。

## 4. 正 primitive 增量的更窄子类

若另给实际正 P 增量且 Δ=Σ_{k≥1}k^−1(T_k)_*P，非零 P 在某 [a,b]⊂(0,∞) 有正质量。对任意 σ<0，Tonelli 中第 k 项对 ∫u exp(−σu)dΔ 至少为 a·P([a,b])exp(|σ|ka)，故不收敛，ν 的 c≥0；σ=0亦由无穷重复质量发散。这样有限 c 已与 E entire 矛盾，**此严格子类不必再用 FE**。

这不是把正 Π 与正 primitive 混同，而是分别核假设强度；上节无FE的 δ_a 负对照不属于这个正 primitive 全 repeats 子类。仅作为候选分类补注，不自行把正式合同预算扩成另一条路线。

## 5. 最强旧比较与预算建议

261-B 是已付的正 Laplace 实边界引理；405 的全实轴 ξ>0 也已付。561 提供正测度／全 repeats／解析 germ 的准确区别，565只证明固定同一裸函数的标准 Gamma 唯一性。128–129的 positive residual rigidity 是有限正 metric／Schur determinant 中 **先要求 same determinant** 的刚性；130虽含 infinite regularized residual 与 anomaly 责任，也先要求最终 exact same-zeta 的乘法补偿。它们不直接推出本命题这种“先允许改变裸 Z，只保经典 Γ、entireness、FE，最后再迫 Z=ζ”的测度类结论。

因此本门不是另做 Gamma 选择或 unknown norm 包装。与有限 rational 0止不同，它有一个实际全局非局部类上的可判结果，且能排一项明确的修复策略。建议 root 若强旧咨询未发现更强原结论，可准**至多一个完整数学迭代**，只证明这一无finite/order限制的类边界及上述负对照；不用数值、不改参数、不串论文。这里的“可准”不是本代理已经开合同或计轮；root 决定与实际消费仍须分开。

即使证明成功，也保留 signed Euler 增量／删减原 Πζ 原子、改变 Γ／额外 completed poles、非 exact FE、只在极限有 FE/entireness 的正 D′ 层、joint signed／primitive-RR／relative 等未覆盖对象。Π≥Πζ 是全局单调假设，不是所有 Π≥0 的同义词；它不能完成578未给经典 Γ 正 countermodel的一般分类。

原 du/zero-extension Dlog 与全部 Γ/contact、proper powers、双 pole 的经典目标保持。这里使用 full Euler-log 数据而非截掉 k≥2；也不把 Euler-log 增量正性等同于 Weil 卷积正型。Whole4/5 UPPER、actual core/coupling、非零 primitive/mixed 和 Ξ 识别瓶颈未因此解决。长期 Goal 的完成门仍 open；本文只结束一个准入咨询，不消耗数学 cadence。
