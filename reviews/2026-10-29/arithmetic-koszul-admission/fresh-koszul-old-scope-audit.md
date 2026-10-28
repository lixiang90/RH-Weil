# 独立限定 fresh：Koszul 闭域、源谱与 strongest-old 消费范围

2026-10-29。结论：**PASS，无必须修项**。本次只审当前 canonical 算术 Koszul prototype 的闭域、实际 source、净后果与 standard old0 分类；本文是待 root 消费的独立复核，不是 root 已消费、研究轮、对外发布或长期 Goal 完成。只写本文件，不改 STATE、cadence、Git 或 runtime Goal；未扩文献、web、数值或 helper。

## 1. 闭复形与同调：结论在指定完成中成立

取正整数 n、有限外标签 A⊂F 的正交基 e_(n,A)，d 把外标签 p 移入 n。总整数 m=n∏_(p∈A)p 保持不变。令 r_F(m)=#(F∩Prime(m))，则 m 纤维是有限维 ΛC^r，d=ι_v、d*=v∧，v=(1,…,1)，故 d²=(d*)²=0、dd*+d*d=rI。r>0 时 ||d_m||=√r；这直接给出闭包所需的有限纤维控制，无需借另一 incidence 或两方向模型的 inverse。

有限支撑核的 direct-sum 闭包满足

- D(d)={x:Σ_m||d_mx_m||²<∞}，d 闭，d* 是实际 Hilbert adjoint；
- D=d+d* 在 D(d)∩D(d*) 自伴，D(D)={x:Σ_m r_F(m)||x_m||²<∞}；
- Δ=D² 在 D(Δ)={x:Σ_m r_F(m)²||x_m||²<∞} 上成立。

有限 F 时相关算子有界；全 prime 时一般无界。没有把无界项形式抵消当作域的证明。P_F 是 r=0 纤维投影，Δ 在其正交补 gap≥1。G=Δ^−1(I−P_F) 有界并映入 D(Δ)；h=d*G 的范数≤1，映入 D(d)∩D(d*)。dh 为全 H 上有界算子；hd 起初只在 D(d) 定义，随后作有界延拓。因此 dh+hd=I−P_F 的裸复合身份先在 D(d) 使用，不能宣称每个无界复合原已对全 H 定义。

由该身份，Ran d=ker d∩P_F^⊥，Ran d*=(ker d)^⊥，值域闭；本 canonical Hilbert 完成的 ordinary 与 reduced 同调一致。有限 F、full 整数 carrier 的 H0=ℓ²{n:(n,∏_(p∈F)p)=1}，higher 为 0，通常不是一维。全 prime 才仅余 n=1 vacuum。h 的费用只在这里的 Hilbert norm 支付，不能消费为原 physical du、任意 Dlog 完成或 arithmetic principal primitive 的费用。

## 2. 共用空间、fixed-source 强后果与合法 trace

不同 F 的 P_F 必须先在共同 degree-0 ℓ²(N)，或按外标签零延拓进 K_all 后比较。Cofinal F_j 意为每个有限 prime 集最终包含，不必单调。每个固定 n>1 最终被移出，有限支撑稠密性给 P_Fj→P_vac 强收敛；P 本身不获 operator-norm 收敛。

应消费更强的实际 fixed-source 结论：A_r=rhat(L)，L=log n，r 为原 physical 的固定 compact smooth 源，第一槽 linear。若 a_j 为最小遗漏 prime 的 log，则

    ||A_r P_Fj − rhat(0)P_vac|| ≤ sup_{|t|≥a_j}|rhat(t)| → 0。

这是每个 fixed r 的 operator-norm 结论，足以覆盖 Hilbert norm 一致有界的 moving seeds。用 ||r^(N)||_1 可给 a_j^−N 率；不能把它改称 du-only 或 moving-source unit-ball 的共同率，也不能控制无界 rank、HS norm 或 traceweight。它仍是固定源滤波的标准后果，不是新算术输入。

固定 seed v 的 harmonic 源是 A_rP_Fv，其平方型谱系数为 |v_n|²，支持在 log(coprime_F n)；若 v 为 cycle，hA_rv 给 exact 部分的 Hilbert primitive，费用≤||r||_1||v||。对有界正 harmonic 权 R，只有在 A_rR^(1/2) 为 HS 等明确合法条件下，Tr(A_rRA_s*) 才是两个 HS 的 trace pairing。即使 R 不与 L commute，该 ordinary trace 只读取 R_nn 的非负谱权；不能将 bare R 或 bare sandwich 自动写成 S1。

这与单一向量的 metric Gram ⟨RA_rv,A_sv⟩ 不同：后者一般保留真实 off-diagonal，未必 stationary，不归入上述共同正谱 trace。非有界权、无穷正混合须各自满足合法正测度/HS 域。paired ±L 只对称化支持，不能免费改变 Fourier 的反射、2π 或目标系数。

## 3. Cofinal 谱坍缩：旧桥覆盖的量词

10-28 positive-Dprime-and-local-gain-admission §§1–4 已处理一般 positive tempered 谱：physical D′ 收敛通过 UBP 给共同 polynomial spectral moment，继而唯一 S′ 延拓和正谱 vague 极限。该桥不预设绝对连续密度、有限总质量或 bounded gain；后续 actual ρ 的费用不能反向缩窄前面一般命题。旧 root-consumption-scope 的相关字段确认此桥已有根消费，不只是孤立草稿。

E_Fj 的每个远离 0 的频率 compact 最终为空，故以上极限谱只可为 cδ0，physical 分布为 cdu，平方型为 c|∫r|²；去 vacuum 则为 0。537 的固定非零 mean-zero ψ′ 有完整 Q_W(ψ′)>0，排除完整 Weil 目标。这里 ψ′ 不 polefree；完整 Γ/contact/proper powers/indefinite 双 pole 仍在目标里，未被正谱消去。

当前全 fixed-source pointwise 版本也成立，但必须保留原证明的代价。设每个 σ_j 为正 Radon 测度，每个 compact smooth r 的 ∫|rhat|²dσ_j 有限且收敛。固定非空内点的 compact K 后，T_j:C_K∞→L²(σ_j) 图闭：源收敛给 Fourier 逐点收敛，L² 收敛子列给 σ_j-a.e. 收敛，二者一致。因而 T_j 连续；把不同 codomain 嵌入共同 Hilbert 直和，pointwise boundedness 与 Fréchet UBP 给共同有限阶 seminorm。

再调制一个 Fourier 在 0 邻域有正下界的固定 φ，得到 σ_j([y−δ,y+δ])≤C(1+|y|)^(2M)。覆盖区间后有共同 ∫(1+|t|)^−L dσ_j 界，取 L>2M+1 即可。于是每个固定 r 的 Schwartz 尾一致消失；结合 cofinal compact 支持消失，Q_j(r)−α_j|∫r|²→0。用一个非零 mean 的 φ 校准得 α_j→c。故合法增长的 seed、任意 gain、rank/traceweight 或正混合，只要满足此共同正谱与全源前件，仍不能逃出 mean rank-one 极限。

这条结论来自正谱 UBP/闭图/Schwartz 尾，不来自 P 的 strong 收敛或几次有限源校准；获得的是较强源 seminorm，不是原 du/Dlog 的共同 operator norm。它是旧一般桥的标准首步接口替换，未支付新的 arithmetic/core 前提。当前审的是既定 cofinal sequence/量词，不扩成任意 directed net 定理。

## 4. Thermal、旧模型与分类边界

实 σ>1 时合法 thermal trace 为

    Tr e^(−σL) = ζ(σ) ∏_(p∈F)(1+p^(−σ)),
    STr e^(−σL) = ζ(σ) ∏_(p∈F)(1−p^(−σ))
                  = Σ_(n coprime to F) n^(−σ)。

有限 F 的 supertrace 不是 1；全 prime 时才为 1。全 prime 的绝对 trace 由 Σ_m2^ω(m)m^−σ=ζ(σ)²/ζ(2σ)<∞ 控制，故这里无 ∞−∞。反之 bare Tr e^(−tΔ)=∞：固定 prime 的无限 prime powers 有同一 r=0 或 1。不能借形式偶奇抵消定义其 ordinary supertrace，也不由 thermal index 导出 completed ζ/Weil identity。

080 的 Dirichlet incidence/Green/Mertens 响应、581 的 weighted rational carrier 和两方向共轭 differential、旧 inclusion cone 是不同 actual pair/degree/map。本复核不称这些稿子已写出此 exact d，不借它们的 primitive；也不从本模型 acyclicity 断言所有 Green、secondary 或 Hodge 路线无效。old0 的理由是本 recipe 的最强可消费输出，已由标准 finite-fiber Koszul 分辨率、旧一般正谱桥和 537 完整正测试推出；闭包、索引和 pointwise 首步的补齐没有新独立算术输入。这是项目内部 standard-old 分类，不是文献优先权主张。

Canonical gap1 已排本完成内部的 nonclosed-range 借口；Fréchet/non-Hausdorff 或别的完成只有改域/模型后才属未覆盖情形。Moving clock/能量 recenter、不同 differential 或 cohomological action、nonstationary Gram、真实 secondary/Green/filling source 等仍未排；本 PASS 不给它们自动开预算或新队列。

## 5. 净后果与版本冻结

**同意 standard old0 停止；不建立 C056，不计 593。** 当前 strongest whole 后果仍是原 542+555→557 的 leading 4/5 负惯性 UPPER，不能改称 PSD、零点比例或 lower；primitive/principal/mixed/signed-core cross/Ξ 的 unpaid 输入未减。Whole-budget 改善和移除核心瓶颈都未由本原型获得。长期 Goal 的 completion gate 保持 open；本 fresh 不独立核 runtime Goal，也不执行 root 消费或发布。

开始与核验时观察的唯一 cadence 为 2/history56/latest592/formal18，LF 6559 bytes、SHA256 ea44d838ee01c575b03fab5a1aa3986134ee5f8e55e7fd55d7b5cbbe2eef714d。本文件不消费或复制计轮权；这些数值是本次观察，后续状态归 root。

本次全文核前四个当前稿及旧桥 §§1–4；080 只核 §§1–3 的 actual differential，537 核固定完整正测试，S-unit 稿核 relevant §5 与 §6 开头，581 只核末尾角色/net，旧 root-consumption-scope 只核相关结构字段。未声称重证所有历史 cone/077/079 或全部 source。下表冻结实际消费的 UTF-8/LF 版本；缩写路径均相对仓库，前三个当前稿与 root 草稿均在本目录。

| 文件 | LF bytes | SHA256 |
|---|---:|---|
| root-fiber-and-source-test.md | 4978 | 917cf314af6574c91f518ceba3bead3d624444c11048192c84cd2434eeb1dacd |
| closed-fiber-and-source-audit.md | 11229 | 13b5125b9f2ebce2b151ad7912403d71a48fda8858f43b3bd4501e9b4b80b8ae |
| strongest-old-and-cofinal-spectral-test.md | 11962 | 44ec28d24fd3e488551f2580559661b548ab1895aa2a27110f6084b7e86794f4 |
| root-domain-and-old-consumption-draft.md | 4281 | c174b6e40841a1762b4cafa12d0fd8a65ff0b0b84e6dc01c50f8f7251d24645c |
| reviews/2026-10-28/gaussian-pulse-admission/positive-Dprime-and-local-gain-admission.md | 11371 | e6fc43de0e72174f6f90c67c4a7dd4e09c093487d96906ba11d522e576bbc1a1 |
| notes/080-divisibility-incidence-green-hodge.md | 8320 | d0e5fd6956f95d462116a84ece12e323c1ebedf3fcbb45e74a27c00125f3f249 |
| notes/537-source-exact-weil-window-positive-tail-admission.md | 8155 | 269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8 |
| reviews/2026-10-23/weighted-two-prime/sunit-relative-boundary-and-principal-test.md | 13390 | e501ae9ea855da3b23ca9d99e7a736d667ba8ab0a2f42f061ff6d565277aff2b |
| goals/GOAL.20261027.md | 9679 | b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de |

最终结论：上述版本下 PASS，无必须修项；待 root 连同对象、域、norm、源量词及剩余逃逸范围一并消费，再由 root checkpoint/发布。
