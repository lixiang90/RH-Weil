# 540 最终同对象、参数与消费范围审查

2026-10-14；独立只读复核 root 的完整 540，不改主 note、STATE、cadence、Goal 或 Git。
审查 snapshot：notes/540-growing-constant-tail-gaussian-reward-cost.md，raw SHA256
`b23e24ddf7982399fd990f2687bab238971209a4541eb8b98938650dba2ae81d`。
初始 Git HEAD `d092aa73183f05c42d9e2433a4f4dd5371607d80`；540 和本轮 reviews 为 untracked。
按 AGENTS 重读入口、check/show、当前 Goal、MACRO_FRONTIER、C011、D20261014L 与策略。
root 已现场核 Goal active；子代理的隔离 get_goal=null 无终态推论。
此补审与 C012 入口准备均不另计研究轮；由 root 按唯一 cadence 结算 C011 第二轮。

## 1. 结论及范围

540 的连续数学推导与声明范围通过本次复核；无需实质修补。
准确消费是：同一全源 constant exterior supplier，允许每个 L 任意 β/Ω/a/τ、
任意非负 compact U 的 rank/norm，若其 bounded R 全源非负，则

    0≤τ≤8 exp(−A_L−1)/A_L，A_L=L exp(C_L)，L≥3/2。

该式没有判 whole Q 的符号，也不排全部逐窗证法、分块机制或 source adaptation。
它是严格全参数费用，不是新独立算术正性；不足以完成本版宏观 Goal。

## 2. 对象、norm 与 full-source 前件

540 始终保 I_L=(-L,L)、Lebesgue L²、zero-extension 与
Ff(t)=∫f(u)e^(−itu)du，Plancherel 因子 1/(2π)。
实际 Γ=Reψ(1/4+it/2)−logπ=2θ′；未误用 θ′。
完整 dual pole 含 odd 负项，prime 序列为全部 p^k<exp(2L)，系数
2log p/√(p^k)、位移 log(p^k)，并由 539 的 C_L 消费。
边界 p^k=exp(2L) 的相关为零，不改变 strict inventory。

对每个 fixed L/finite Ω，有限 Γ-band continuous kernel 为 Hilbert–Schmidt，
pole 有限秩，所以 K compact。主式 T 保所有 |t|>Ω 的实际非恒定 Γ 权。
whole-source 的 T≥a(I−B)≥τI+U 才运输 Q≥R；R≥0 只在指定证明类内作为前件。
额外修复须 compact 才可沿 539 的 weak-null prime carrier 消失；
单独 τ≤aδ 只需 U bounded 且非负。这两项责任在 540 没有混淆。

539 的 β+τ≥C_L 是 bounded R 非负的必要条件，不是 whole Q 非负的必要条件。
540 明确说明这点，并未把 R 不足运输为 Q 负。

## 3. V1–V3：全参数、norm 误差、等号

**V1 / 540(3)。** 对有限 positive L/Ω，B positive compact contraction，
非零且无 eigenvalue 1（finite-support Fourier entire identity theorem），所以
δ=1−||B||∈(0,1)。由 U≥0，τ≤aδ。再用 β≥C_L−τ 与
a≤Γ(Ω)−β，直接得

    (1−δ)τ≤δ(Γ(Ω)−C_L)。

因此 Γ(Ω)≥C_L，且 τ≤δ/(1−δ)(Γ(Ω)−C_L)。未错误删除 τ，也未假设 β≥0。
若 Γ(Ω)=C_L，τ=0，随后 β=C_L、a=0；型门 0≥U 与 U≥0 给 U=0。
这些等号不证明 R≥0。Ω=0 / δ=1 是明确排除的退化情况。

**V2 / 540(1)。** 冻结 α=Ω/L，两个 exponent αL²、Ω²/α 恰相等于 q=LΩ，
并最大化它们的较小值。h=(α/π)^(1/4)exp(−αu²/2) 全线 norm1，
g=1_Ih 的 accurate norm² 为 1−r，r=erfc√q；完整 h 的双侧外频 norm² 也等于 r。
projection contraction / triangle 得外频 g norm≤2√r，故
δ≤4r/(1−r)。截断、正负频率、norm 分母均付，不能把 g 的 norm 当 1。
erfc x<exp(−x²) 对 x>0 的 shifted-integral 证明正确，给
δ<4/(e^q−1)；分 q≤log5 / q>log5 得 δ<min(1,5e^−q)，覆盖全部 q>0。
g 的 boundary jump 不逃逸：bounded I−B/U 的型门由 Cc∞ 稠密延拓，
strict-support smooth 逼近连 norm 一并支付；实际 Dlog 的 O(1/t) 事实未用于计算 Q。

**V3 / 540(4)。** 令 z=e^−q。当 q≥log10，z≤1/10，
δ≤4z/(1−z)<1。单调函数 x/(1−x) 给

    δ/(1−δ)≤4z/(1−5z)≤8z。

常数 8 使用较紧的 4/(e^q−1)，不是误从 5e^−q 得 8e^−q。
所有分母均严格正，方向正确。

## 4. actual Γ 与 V4 的全 Ω 优化

本次现场打开 [NIST DLMF 5.7.6](https://dlmf.nist.gov/5.7#E6) 核原 digamma partial fraction。
对 z=1/4+it/2，取实部后的 n 项为 1/(n+1)−x_n/(x_n²+t²/4)，x_n=n+1/4。
compact t 上原项 O(n^−2)、导数 O(n^−3) 一致可和，因此逐项微分合法，
得到 540 的 Γ′(t)=(t/2)Σx_n/(x_n²+t²/4)²>0。
539 的 C_L>4>Γ(256) 与 Γ(Ω)≥C_L 因此确实强制 Ω>256。

Binet bound 不只按旧 PASS 消费：本次亦核 538 原 geometric-source 与 full-inertia
§7.2，并由 [NIST DLMF 5.9.15](https://dlmf.nist.gov/5.9#E15) 同规范复算。
令 z=5/4+it/2、z₀=1/4+it/2。digamma recurrence 的两 reciprocal real 项非正，
而 |u²+z²|≥|Im z²|=5t/4，故 Binet remainder 的绝对值

    ≤[8/(5t)]∫_0^∞ u/(exp(2πu)−1)du=1/(15t)。

Re logz≤log(t/2)+25/(8t²)，所以实际 Γ 上界为
log(t/(2π))+1/(15t)+25/(8t²)。π>3、log(2π)>1 与 t≥256 上 fee 和<1，
严格给 Γ(t)<log t；没有额外 1/2、漏 π 或改变 Γ。

**V4 / 540(5)。** Γ(Ω)≥C_L 与 Γ(Ω)<logΩ 给 Ω>exp C_L；
主文用弱些的 Ω≥exp C_L 合法。置 A=L exp C_L、x=LΩ，则 x≥A，
L≥3/2、C_L>4 保 A>(3/2)e^4>log10，V3 自动可用。于是每个可行 Ω 上

    τ≤8e^−x(Γ(Ω)−C_L)≤8e^−x log(x/A)
      ≤(8/A)e^−x(x−A)。

令 y=x−A≥0，由 ye^−y≤e^−1 即得 8 exp(−A−1)/A。
这一上界优化的是 scalar 表达式，并未为不同测试源更换 Ω；全部 Ω 同时覆盖。
Γ(Ω)=C_L 的 τ=0 情况也满足该统一 bound。
539 自含 C_L→∞ 给 A/L=exp C_L→∞，因而对每个固定 c>0，
[8e^(−A−1)/A]/e^(−cL)→0；540 的 τ(L)=o(e^−cL) 声明正确。
未借 PNT 或补填 C_L 渐近，没有证明常数或 exponent 最优。

## 5. 量词逃逸与宏观净值

每个 fixed L 的 539 carrier 和 Gaussian test 均针对同一个完整 H_L supplier；
无需它们为同一源，也无需 uniform compactness。L-dependent compact rank/norm 可任意大。
但 finite source 条件后的 Gaussian 门没有已付：从 B compact 可删有限个 eigenvalues>1/2，
使补空间 B≤I/2、restricted δ≥1/2。Gaussian 可能不满足该条件。
因此 539 对 finite 条件仍真，不能与本轮 unrestricted Gaussian 门拼成条件后的 V4。
540 对此限制的具体例子和警戒均正确。

若仅 U_f 按源变化、始终非负且 a/τ 仍统一，丢 U_f 后 scalar 门仍真；
若 β/a 按源变化，或不存在单个 compact U 的 whole R，539 的 single supplier 门未付。
540 没有把前一种有限扩展升级为排除全部 source adaptation。
signed/noncompact 修复、完整 nonconstant Γ 与 prime/pole 的 joint 比较、
有限 head/complement 全预算与实际新几何都明确未排。

所以通过的是全源恒定尾机制的 reward 成本；uniform τ₀>0 被排，
但逐窗极小 τ、匹配的新 exact error、真实 full Γ tail 均未排。
540 保留完整 Q 高频能量，没有宣称它 weak-null/compact 消失。
新 Goal 要求 source/joint 核心责任的更强净后果，这次不能验收宏观完成。
停止 C011 的继续扩窗/扫描、转保完整 Γ-tail 的 C012 准入，符合二轮止损与宏观约束。

## 6. 修改建议与终态

无需实质修改。可选的可读性改进只有：在 540 §2 直接并列
δ=inf_(||f||=1)<f,(I−B)f>=1−||B||，使 §3 的取 infimum 更容易核对；
现文已由算子性质与前后定义充分支持此等式。
本审查未执行有限诊断、扩精度/参数测试或 C012 首轮；没有 pending scientific process。
root 若仅添加本 audit 引用而改变 raw hash，属于引用变动；实质修改仍应核依赖范围。
