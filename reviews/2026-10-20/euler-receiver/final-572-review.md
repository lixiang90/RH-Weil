# 572 fresh 独立终审：Euler 后真实 receiver 的原域与完整尾费

2026-10-20。结论：**PASS，严格限于下列模型、权、平均与成长范围。**
本终审重新恢复 README/STATE、check/show、G20261014、C035、D20261020O、
cycle14 和 MACRO_FRONTIER；不修改公共 STATE/cadence/Git，不自行结算研究轮。
冻结基线仍为 0c4f/≤538，最强旧 whole 后果仍是 542+555→557 leading 4/5。
审查对象是最终主572、三份最终 producer 原证明、来源记录及明确继承的571前件；
producer 的结论或退出状态不代替下面的独立推导检查。

## 1. 实际映射、相位与原域：通过

原对象是 H=L²(R,dy)、完整 D=B⁻¹、P_T=1_(0,T)，同一实际载波
w=e^(iRy)1_(0,T)/√(2π) 产生 v=L_-D*P_Tw、u=H_+DP_Tw。
先对全部 T>0 写代数身份，再于成长消费中锁定 T=完整Γ(R)。
它们不是任意低半线输入，也不是 Sonin 裸求值 k_R 或 Weil 原源 r。

直接由 D*=Σ_(n F-smooth)n⁻¹/²U_(-log n)，在 t=−y>0 得到负半线真实 receiver。
实际 bar b(R) 的 divisor 多项式乘入后，以最终 n=dm 合并，系数恰为

    a_(n,T)(t)=n⁻¹/² Σ_(d|rad(n)) μ(d)1_(t<log(n/d)<t+T)。

μ(d) 前不再出现 d⁻¹/²；原 d 权已同 (n/d)⁻¹/² 合并。
用 b 代替 bar b 不会给这个系数。普通唯一分解使不同 n 对应不同实际频率，
一般 g 的碰撞必须另行合并，不能继承 free-label diagonal。

每个 fixed finite F 下 Σ||a_n,T||_(L²(t>0)) 有界于
√T Z_(2,F)(1/2)<∞，因此有限 Euler 乘法、全部重排及等延迟合并在原 receiver
范数内合法。外面的 e^(-iRt) 是这一范数等式中的酉调制，不能借此删除实际频率相位。
各 interval 限制在 (0,log n) 给 ||a_n||≤n⁻¹/²2^ω(n)√min(T,log n)。
两边界支撑公式以及半线交叠
ℓ_T(x,z)=min{min(x,z),(T−|x−z|)_+} 均重新核算无误。

## 2. 完整 diagonal 与无限 MV 域的失败范围：通过

对 S=supp(n)，先作 S 中最小 prime p 的 interval 差分，整线范数平方恰为
2min(T,log p)，其余差分各至多乘4；限制到半线只降低范数。
再用 Σ_(supp(n)=S)1/n=∏_(p∈S)(p−1)⁻¹，得到主稿(7)的完整 support 分组。
Mertens product 比值给 ∏_(p<q<X)(1+4/(q−1))≤C(log X/log p)^4，
而 Σ_p[(p−1)(log p)^3]⁻¹ 收敛，所以 uniform ALL T 的完整 diagonal 是 O(L⁴)。
没有 hidden m⁻²、M²/m²，亦没有将不同 divisor 的平方分别求和。
尾稿保留的粗 O(L⁵) 只是对照，最终定理引用已付 O(L⁴)，不另计一项改进。

单 prime 幂 n=p^k 在两 interval 都离开原点后，严格有
n||a_n,T||²=2min(T,log p)>0。因此 Σ n||a_n||²=∞，不能直接使用粗整数
log-gap 所给的无限 Corollary 3 充分域。这个失败不是 receiver 能量下界。
单 prime 的真实 gap=log p 已给合法无限 Corollary 2 逃逸。

更一般的 first-fixed F，BMS/Matveev 给真实 log gap 的 polynomial(log n) 下界。
已独立重开原刊 Thm9.4 的 modified-height 定义、实域陈述及其短证明；
在 Q、d=|F|、A_j=log p 下，M_D=1.4·30^(d+3)d^(9/2)∏log p 正确。
原定理的 B=max 指数范数无需人为 B≥3。局部 |log(m/n)|≤1 时的 exponent
height bound 与 |e^x−1|≤e|x| 支付尾稿(7)；随后 elementary exponential
majorant 支付(10)的 Σδ⁻¹||a_n||² 有限，uniform T。
该 fixed-F 修复合法，但其巨大上证书不支付 cofinal 高度，也不提供实际费用 lower。

本轮另独立重读 MV 原刊 printed74–75、82 页，核 Theorem2、Cor2/3 与§4
推导，未声称重证其全部 Theorem1。有限 Hilbert-valued 版本由有限系数 span
逐坐标求和获得，常数不依赖维数。无限版本只在实际 gap 加权平方和已付后取极限；
本轮 cofinal 证明只对有限 head 用 MV，并不依赖上述巨大的 Diophantine 常数。

## 3. Euler 后完整相干尾与同步高度：通过

关键截断是**有限 Euler 合并后**的 log n≤A。若先截 D 再乘 bar b，最终频率
可到 A+log rad(F)，不能消费同一 head/tail 账目；四稿没有这种换序。
有限 head 的整数 log-gap≥1/(2n) 给误差

    C/H ·Σ_(log n≤A)n||a_n||²
       ≤ C A/H ·e^(A/2) Z_(4,F)(1/2)。

这不是 O(diagonal/H)，也没有把无限 Cor3 放在发散域上。
完整相干 tail 虽可 signed，证明只用充分的原范数三角 upper：

    ||tail||≤√T S2(A),
    S2(A)=Σ_(log n>A)2^ω(n)n⁻¹/²
         ≤e^(-αA)Z_(2,F)(1/2−α)。

所有超 cutoff 项都在这个 bound 中，没有第二个未付无限尾。
我重新核算 moving-exponent PNT：对 s∈[1/4,3/4]，先用普通 PNT 在固定 head
以外的 ALL-t 相对误差包络，再 Abel；head 在该紧 s 区间可一致忽略。
∫t⁻ˢ/log t dt 的端点渐近也在该区间统一，故在 X=e^(2L)、
s=1/2−k/(2L)、fixed k 下，prime sum 主项是 e^(L+k)/(L+k)。
Z2 的 log 以2倍 prime sum 开始，三次余项 uniform O(1)；
Z4 在 s=1/2 的一次系数是4，二次及以后 O(log L)（较粗 O(L) 亦足够）。
因此主稿(13)的常数2、4及所有 fixed-k o(1) 正确，没有 fixed-α 极限偷换。

令 A=c e^L、c>4e、k=log(c/4)>1，完整 tail 满足
S2(A)≤exp{−[d(c)+o(1)]e^L/L}，
d(c)=c/2·[log(c/4)−1]>0。
连同未归一 T0~θe^L 的平方费用仍为 o(1)。有限 MV 费在 c<2βθ 时也为 o(1)。
所以对每个先固定 θ>2e，可再固定 β∈(0,1)、4e<c<2βθ，获得完整原范数账目。
这里的兼容门是所用 l¹-tail/MV **充分证书**的范围，不是 signed tail 的必要阈值，
更不是 θ≤2e 的真实费用 lower 或一般方法类边界。

## 4. 完整Γ端点及原范数费用：通过，范围不可扩大

实际区间是 I_L=[R0,R0+R0^β]，R0=exp(θe^L)，最终 T_R=完整Γ(R)。
冻结 T0=Γ(R0) 只是估计步骤；Γ′(R)=1/R+O(R⁻³) 给
Δ_T≤C R0^(β−1)。原 hard endpoint 的载波范数差平方恰为 Δ_T/(2π)，
经 D* 和实际 b 权后的上界为 (M/m)²Δ_T/(2π)。
log(M²/m²)=(4+o(1))e^L/L，被负的 (1−β)θe^L 支付。
固定 T0 的 mean、全部 tail 和端点 cross 均用三角／Cauchy–Schwarz 加回，得到

    av_(I_L)|b_F(R)|²||v_(R,T_R)||²_dy =O_θ(L⁴)，
    av_(I_L)|b_F(R)|²||v_(R,T_R)||²/||w_(R,T_R)||²
         =O_θ(L⁴e⁻ᴸ)→0。

第一式是实际 |b|² 权的原 dy receiver norm；没有 m² 概率归一。
它不证明 unweighted ||v||² 小费，除以实际 |b|² 可能重新引入 m⁻²；
也不支付 Weil 原 du/zeroextension Dlog 范数，不是 pointwise/ALL-height 或 ALL-source 结论，
更不是 receiver 方向再受另一个算子作用的放大率 bound。

## 5. 两 clean receiver 的协同 Gram 与全 inverse：通过

继承571已审的同一实际 K=L_-BD*H_+ 与 J=[[I,K],[K*,I]]、完整 J⁻¹。
原两边界 identity 是 δwin=||v||²+||u||²−<(v,u),J⁻¹(v,u)>。
定义 V=bar b v、U=b u、η=bar b/b；b 从不为零。
反射 R_T 是 antiunitary，故 U=e^(iRT)R_T V，而共同 scalar bar b(v,u)
等于 C_b(V,U)，C_b=diag(I,η)。因此

    J_b=C_b*JC_b=[[I,ηK],[barηK*,I]]，
    |b|²δwin=||V||²+||U||²−<(V,U),J_b⁻¹(V,U)>。

方向、共轭和 inverse 的运输均重新核算无误。独立 clean 后保字面原 K 会改掉 cross，
四稿均明确拒绝。J_b 是酉共轭，全部 returns、两边界和 gap 保留。
由 δwin≤min(||v||²,||u||²) 只支付 weighted 正部的相同 mean upper；
负部、absolute residual 与全源 favorable sign 未付，未借正 J 宣称 δwin 正。

## 6. Root 可消费净后果与未付责任

本轮相对571确实付一个新局部账目：明确 θ>2e 同步高度范围内，实际 b 权的
完整 coherent receiver tail 和原 dy norm mean 已闭合，不只是 fixed-F Bohr diagonal。
PNT/Mertens/MV/BMS 都归已有外部来源；新的是在真实 receiver 上的系数、域及完整费用合成，
不是新的外部深定理或新的经典 Weil 正性。

δwin 仍是 window model，不能改名 actual Sonin ε_F 或570的 E_F。
Sonin k_R→w_R、完整 G_F inverse/cofinal clipping、S_T 的其他 bulk/单边界 trace tails、
原源 transport、低频/core、source coupling 与 ALL complex coverage 都另欠。
旧 word-budget 证书不能用只构成证书缺口，不是实际源费用必要下界。
θ>2e 位于555已知有利高频大小层，未进入 Γ约≤e^L 的危险核心。

完整Γ/contact、所有 proper powers 和双 pole 在主稿(21)/(22)中保持，
没有具体源的额外矩消失条件便不能设零。有限 Euler numerator 的 μ(d)
没有替换完整 −ζ′/ζ 的 prime-power 分布。
一般 g 系统还须独立给真实 causal inverse、碰撞合并、原域、计数/间距及相应成长 tail；
连续系统不能继承离散 MV gap。形式 duality 或正 J 均不支付 primitive 正极化。
直接假设全部完整 Weil Grams PSD 仍是等价要求；独立从同源设施证明其正性才是新容量输入。

因此：局部 high-frequency model fee 的 bottleneck 改变；actual Sonin 成长运输和独立容量的
宏观瓶颈不变，strong-old whole leading4/5/core/coupling/Ξ 及 G20261014 完成门均不变。
保留非有限秩 compact、Γ-relative、source-adapted、不同全 inverse 及几何容量合法修复。
本审阅不准入阈值／幂次／singleprime 优化或 unknown-capacity 新合同。

审核中仅要求主稿把“每个 n>A”改为“每个 log n>A 的项”；现已在绑定前修正。
没有其余 blocking 问题。不存在作为证明依据的数值拟合、截断 inverse 或后台运行。

## 7. 最终 LF 版本绑定

以下 SHA256 按 UTF-8 文件字节仅将 CRLF 规范成 LF 后计算，保证所审版本可识别；
hash 不认证证明，亦不把旧571的继承前件计为本轮新定理。
绑定旧571主稿、actual-pair 原证明与 root 消费范围，消费仅限本文明确列出的前件。

| 文件 | LF SHA256 |
|---|---|
| `notes/572-finite-euler-receiver-coherent-tail-and-original-weighted-cost.md` | `8c283c0af3c297b0a0c826cf8cd6db1924f8bad2327bff32a67951e442756ff6` |
| `reviews/2026-10-20/euler-receiver/coefficients-domain-and-diagonal.md` | `80232d8c7709235ed58f75da246bd00bc171754d4341ce72a4564af938cb3ba0` |
| `reviews/2026-10-20/euler-receiver/weighted-tail-and-height-cost.md` | `b8037aefd5f893967175ecfeecbbb8a74c3202bb6d7d7af6daa6a20fe1054939` |
| `reviews/2026-10-20/euler-receiver/independent-control-and-capacity.md` | `9f263dce9fdb220df1c37834b048934aefb31606cd0b13b4ebf999021ed82525` |
| `reviews/2026-10-20/euler-receiver/source-read-record.json` | `f98466295f8685dba29784b3c1f2f70ddfe0c1475d06d43a365c1ec6e8e50bd0` |
| `goals/contracts/C035-finite-euler-weighted-receiver-and-coherent-tail.md` | `c0c763ae878b1d76e2d82c90adebcbc3555fd7a0725ac71b2450f97fa85ba3b0` |
| `notes/571-actual-receiver-two-boundary-signed-comparison-and-growth.md` | `c7f0cf4712bdbb9429c4356c3974098b9c39b2eba4486b91c800fb7653cf109e` |
| `reviews/2026-10-20/receiver-signed/exact-receiver-and-boundary-sign.md` | `ea55881593c9969ef81e28a7e90d0f730d5d32404a8405b77325eaaedcc77e86` |
| `reviews/2026-10-20/receiver-signed/root-consumption-scope.json` | `ca6134f0e5b402782fcba1c95e635c60d7c850618fefd9fa1d3f5f858bf7ffcc` |
