# 569 独立终审：固定 Γ 规范、全源 cocycle 与容量责任

2026-10-20；独立审阅当前 C032、主稿 569、三份独占原稿、两份 source 记录和两份 exact 记录。
审阅者只编辑本文件，不修改 STATE、主稿、计轮或 Git。本文是最终版本的数学审阅，
不是 root 消费收据、外部论文全部证明认证或宏观完成审计。

**结论：PASS。** 已独立重算关键式，并重新打开关键 primary 文献。
最终主稿将 Γ 分布与其作用分开写；cocycle 稿与主稿明确有限 Hermitian 坐标矩阵的约定，
这些草稿澄清已重闭。没有未解决且阻止按本文范围消费的数学错误。
通过的是限定载体类的精确比较、合法有费修复和全源协同变换；没有通过经典独立容量或 Weil 正性。

## 1. 恢复的完成门及实际审查方法

已读 goals/README、STATE、C032、当前 Goal 和宏观前沿，并执行 research_state.py check/show。
保持 G20261014 与 0c4f≤538 基线；结构检查不认证数学，旧完成结果不重复完成本 Goal。
568 已有 signed 评价商、nonzero minor 和正反局部载体；本轮不能再把这些存在性算作正性输入。
最强实际旧后果仍是 542+555→557 whole leading 4/5；560 的 growing K/sign/core/coupling/Ξ 未付。

本次独立核查包括直接代数、完整函数/分布计算和 primary 定位：

- [ALKL 2402.06671v2](https://arxiv.org/pdf/2402.06671v2)：重新打开 §§1.3.6、2.5.28–30，
  以及 Proposition 5.8.1、6.7.1 的显示式和假设范围；未重审全书证明。
- [DLMF 5.9.12、5.9.16](https://dlmf.nist.gov/5.9)：核 ψ 积分、差分及 Re z>0 域，
  由此重新计算接触项与 L1 质量。
- [Burnol 9902080v1](https://arxiv.org/pdf/math/9902080v1)：重新打开 §§G–H 的实位 Gamma phase、
  conductor operator 和临界线乘子；只消费该局部身份及其既有来源。
- [Stacks 0FJI](https://stacks.math.columbia.edu/tag/0FJI)：重新核两项有限 projective complex 的
  determinant、canonical section 及 acyclic 判据；有限向量空间的 norm 换基式另直接推导。

web 的原 PDF 文本可读，截图接口 cache miss；本文不声称独立重做 producer 的本地视觉 QA。
原版显示式的具体视觉确认归 source-record 中的既有记录；下文可消费结论另有直接数学检验，
不依赖猜测 Barner 未取得公式的本意。
复算 Taylor、两组 companion 矩阵及非实 cocycle 也均通过；有限计算只验证已证明恒等式。

## 2. single κ 与共同 character：失败类及合法逃逸均准确

原件的两条次数分别为 −(k+1)κ 与 kκ，k≥0，且来自 density-dual 的一次次数差。
相应收敛半轴上的几何级数给 Kκ(t)=|e^(κt)−1|⁻¹。
对 v>0，Kκ(v)/Kκ(−v)=e^(−κv)；故共同实 character e^(at) 偶化的条件为
e^((2a−κ)v)=1 对每个 v>0，严格迫 a=κ/2。κ 可负，最终核只依赖 |κ|，没有遗漏该情形。

偶核 Hκ(v)=1/[2sinh(|κ|v/2)] 的 IR 主项是 e^(−|κ|v/2)，UV 主项是 1/(|κ|v)。
经典 a(v)=e^(−v/2)/(1−e^(−2v)) 的 IR 主项是 e^(−v/2)，UV 为 1/(2v)。
假设 A Hκ=a，IR 迫 |κ|=1、A=1，UV 随即矛盾；非实 A 也不能回避正实核的点值比较。
δ 或任何支撑在原点的修正不改穿孔差。因此该限定类的排除正确，优于只拒一个试选 twist。

范围必须保留：这是一个 κ、完整标量 all-k 链、共同实 character、正时间重标和常倍数类；
不是所有多叶、twisted/super coefficients、非局部或奇异几何的排除。
两半轴分别调权不属于已付同一 pairing。

额外反射在 k 阶给 (−1)^k，投影到 k=2m，确有
Σ_m e^(−(2m+1/2)v)=a(v)。这是精确的条件修复，并非原 all-k 迹自动给出的结构。
主稿最终明确它只匹配 shape，实际 involution、sector/flow/dual 相容、Euler 负号、trace 重数及全局延伸仍欠。
在可定向闭二维叶 χ=2−2g 的普通标量情形不能手取 χ=−1；保留额外系数等合法设施。

## 3. 完整 Γ 有限部分、修复大小及 Fourier 符号

以物理 log cutoff 定义
T_a(h)=lim[∫_|u|>ε a(|u|)h(u)du+h(0)log ε]。
任意 compact smooth complex h 均合法：两侧合并后的 h_e(v)−h(0)=O(v²)，a(v)~1/(2v)。
从 ψ 差分积分，或先令 α=1 校准，独立得到

    ∫_ε^∞ 2a_α(v)dv = −log(2ε)−γ−ψ(α)+o(1),
    a_α(v)=e^(−2αv)/(1−e^(−2v)), α>0。

将 Γ_α0=ψ(α)−logπ 代入收敛差分形式，剩余接触常数严格为 −γ−log(2π)，与 α 无关。
故主稿 (7) 的负号、2、π 和完整 contact 全部正确；没有只匹配高频 log 而漏 Γ0。
最小对数 extension 类只余 δ 歧义，不可扩大为任意阶 point-supported extension 唯余 δ。

令 b=a_(1/2)，D=a_(1/4)−a_(1/2)。v>0 时 D>0；原点 Taylor 的直接复算为

    D(v)=1/4+v/16−v²/32−7v³/768+O(v⁴)。

偶延拓连续且 L1，质量是 ψ(1/2)−ψ(1/4)=π/2+log2=M。
因此同物理 cutoff、同接触反项的两完整 Γ 型源之差确为 −D，不隐藏另一个 δ 费用。
全 L2 卷积 norm≤M 由 Young 得到，反方向由连续乘子 hatD(0)=M 得到；fixed 窗只消费同一上界，
没有声称每个有限窗的 norm 也等于 M。转原 Dlog 时 log2 的范数常数仍须保留。

主稿的较强 Fourier 余项 O(ξ⁻⁴) 也成立，不必缩回 source 稿的 o(ξ⁻²)。
D 在闭正半轴光滑、各阶导数指数下降，特别 D''''∈L1；两次分部积分给

    hatD(ξ)=−2D'(0+)/ξ²−(2/ξ²)∫_0^∞D''(v)cos(ξv)dv。

对末积分再分部两次即可得 −1/(8ξ²)+O(ξ⁻⁴)。所以 hatD 在 0 正、高频负；
−D 的卷积二次型也变号。点态 D≥0 不代表 positive type，有限 norm 不代表有利 signed 项。
这一有费解析修复保留，但几何 membership 和与其他预算联合后的有利号均未由此支付。

Burnol 原件的实偶 γ+ 与主稿 (8) 相符；直接微分给 .5ψ(s/2)+.5ψ((1−s)/2)−logπ，
在 s=1/2+iξ 恰为 Reψ(1/4+iξ/2)−logπ。odd sector 的 3/4 也正确。
这里的实局部域、加法字符、自对偶 Haar 和 sector 是额外、已知的局部结构；
不是 bare g-integer measure 自行选出的设施，也不是完整 Weil 的正算子证明。

## 4. b-cutoff 与原文风险：只消费独立重算的方向

对 u=A(x,y)|dx/x dy| 及 x'=e^ωx+O(x²)，cutoff x'>ε 对应 x>εe^(−ω)+O(ε²)。
额外积分直接趋于 +ωA(0,y)，所以 FP_x'−FP_x=∫ω Res u 的方向正确。
不同定义函数的 O(x²) 部分只给 o(1)，不增 contact。

若同时要求 dx(ν)=1、μ=aν，则与 μ 相容的定义函数是一阶 x'=x/a，故上述方向给 −log a。
原文所显示的 +log a 与这一直接换算存在相容疑问；主稿没有把它当已解决外部定理消费。
source 稿保留风险、消费另证的 defining-function 方向，处理正确。

原件 §1.3.6 的普通积分显示式若照字面作用于 h(0)≠0 的 compact h，尾部全程 1/t 减项发散；
若 h 支撑负半轴且避开 0，同一正时间分母也读不到 Kκ(−v)。两问题彼此独立，且不能靠 δ 改穿孔值。
这只限制该显示式的逐字消费，不推翻正文 trace 设施，更不替未取得的 Barner 公式指定隐藏约定。

原件 (2.5.65) 的负号、导数作用于第一个 indicial family、因子 1/(2πi) 均与主稿相同。
它在指定 smoothing b-calculus（原文另容一个 b-differential 因子）的范围有真实 source；
没有延拓成所有 unbounded operators 的公式，也没有变成普通正 trace。
把它识别为完整算术预算，仍需实际同一个 indicial family、prime powers、pole/cohomology 比较，当前未付。

## 5. 第一变量线性、实 1-cocycle 与全纯 phase

取 b_j 第一变量线性，q_j=b_j(r,r)，R=rad Σb_j。主稿正确使用 full radical；
只有 Q(h)=0 的 isotropic 元素不能替代 R。
c_j(r,h)=2Re b_j(r,h)+q_j(h) 是全代表、全 mixed 的实 coboundary，满足所写复合律。
Σc_j=0 来自 h∈R，对正型与不定型同样成立。

主稿与 cocycle 稿统一用 metric e^(−q_j)|z|²，transport e^(c_j/2)，直接相乘确为 isometry。
全纯候选 g_h(r)=exp[b_j(r,h)+q_j(h)/2] 的复合按先 h 后 k 给

    g_k(r+h)g_h(r)/g_(h+k)(r)
      =exp[b_j(h,k)−Re b_j(h,k)]
      =exp[i Im b_j(h,k)]。

σ 的 2-cocycle 关系由底层实双线性给出，tensor phase 因 Σb_j(h,k)=0 精确抵消。
模型稿 metric 用 e^F、负指数 j，且写的是先 l 后 k；其相位仍是 exp[i Im B(k,l)]。
这两个约定分别正确，不能混用 transport 顺序或只看指数正负判错。
以 q_P(k)=1/8、B_P(k,ik)=−i/8 的非实对再次复算，主稿和模型稿各自公式都给所写 e^(−i/8)。

经典 Gaussian 关系在 physical S_exp 中使用，未冒充 compact。
c_P(r,tr_h)=.5Re{bar t(M_+(r)+M_−(r))}+|t|²/8 的 mixed 常数正确。
I 未被冒称整个 full radical，也未被冒称旧 405 B 的根；双次数方向及 P_an 的区别保持。

审查时要求的有限 Hermitian 坐标补充已经加入：q(sx)=x*Hx，H_ij=b(s_j,s_i)，target 同理。
因此 H' = A*HA 与第一变量线性相容；若按 b(s_i,s_j) 排矩阵则应转置共轭，不能混用。
det norm 比值及换基不变性本来正确，此补充闭合了记号意义。

## 6. 模型检验是真实全域关系，不是有限表外推

连续族：对任意非零 φ∈D，k=(∂²+d)φ 非零且仍 compact。
分部积分给 W*k=0 和 M±(k)=(d+1/4)M±(φ)=cM±(φ)，故 P(k)=c²P(φ)=R(k)。
实偶非负 φ 可归一化至 M±(k)=1/4；d=±1/16、0 的倍率分别 25/256、9/256、1/16。
任意开窗四矩 Gram 的另一构造也成立：两常系数 ODE 的解空间因 d>−1/4 交为零，
乘正 bump 后的四函数 Gram 正定。包括阈值，但未声称全部 jet representation 在阈值正定。
全部 Π 和双 pole 保留；Γ=0 是模型规范，不是删除经典 Γ。

函数域：W 和 P 是完整 log-comb，不能用单个连续 cosh 矩替代周期 aliases。
a_n=q^(−n/2)S_n 的 reciprocal 双向递推，连跨越 n=0 的两处都成立，a0=2g=2。
于是 p(T_L)W=0，k=p(T_L)φ 是对所有 compact complex r 的完整根关系。
固定 φ 时 periodized M± 的和统一有限，按 y∈[0,L) 展开 convolution 可得主稿 P 的全部 aliases 身份。
T_L 作用在 M± 上乘 q^(±1/2)，因此 P(k)=p(√q)p(1/√q)P(φ)=N1²/q P(φ)。
真例 −3 给 81/5，反例 5 给 1/5；取 φ 支撑 (0,L) 时 P(φ)=2L||φ||²>0，归一化都合法。
g=1 的 R contact 为 0，W0=P0=2；一般 genus 的 2−2g 不可因此删去。全文没有这样外推。

q=5 两组 A_t、H_t 的 det、AᵀH A=qH 和 AᵀJA=qJ 都已独立精确复算；
detH 分别 11、−5。top line 的正确总权/归一化 determinant=1 与 primitive 正负确能并存。
模型 finite JSON 的 n≤8 数列只作校验；全 n 后果来自递推，不由有限 counts 外推。
正整数 Euler/primitive 正性按已付 290/562–568 的范围继承，不宣称本轮重新证明全部旧构造。

## 7. determinant 与独立容量的界限

真实有限 map E:S→J 的 det J⊗det S⁻¹、kernel/cokernel 正合列身份及平衡维 canonical det E 均成立。
line 存在不保证截面非零；nonzero evaluation minor 不保证 Weil Gram 正。
已有独立正 H_S,H_J 时 determinant norm 公式成立；若先拿未知 Weil Gram 当正 metric，就把目标放进前提。
负本征值数为偶时 determinant 也能正，故 top line 正号不能代完整 Gram 半正。

主稿 e^(−Q) 的纤维 norm 对任意实 Q 都正；固定 holomorphic frame 后其 Chern 曲率为 i∂bar∂Q。
沿 v 的曲率系数 Q(v)，所以要求半正曲率仍等价完整 Weil 正性。
实平凡化 line 的存在、实 cocycle 消失、projective phase 总抵消本身都不含容量。

真实曲线另有同一个 global function field、restriction exact sequence、kernel H0(D−E)、
principal changes、RR 与平方交数；它们才是独立来源。反模型没有被给出同一真实曲线几何，
所以不能从两者共享的局部 carrier、权和 cocycle 倒推几何，也不能声称所有连续/一般几何必失败。
经典尚缺同一可乘 global source、真实消失过滤、同一非零 determinant section 的全位结构、
独立 RR/height/容量估计及其 all-complex、全 powers/双 pole/Γ/contact 的共同 scale 极限与误差。

## 8. 根消费范围和净后果

| 项目 | 本轮可消费 | 仍欠／不可升级 |
|---|---|---|
| 对象、域 | 固定 real-even full W；compact 全复源；classic 关系另在 physical S_exp | 一般非自对偶对象的预定权/左右 pairing 另给 |
| carrier 门 | single-κ all-k common-character 类的严格失配；明确 parity 逃逸 | 所有几何失败、global parity/Euler/trace membership |
| norm、Γ | full physical-log FP/contact；全 L2 的 M 修复及 Dlog 转换常数 | 新原 norm 容量、修复源自动有利 signed 性 |
| source、误差 | Γ 身份和 cocycle 精确；continuous compact 与 FF 全周期关系，无截断误差 | 经典 all-place 截面预算及成长误差、coverage/coupling |
| map/角色 | full-radical 代表变换、真实有限 evaluation det 的条件接口 | Q 根不代 principal divisors；形式指数 line 不代实际 cohomology complex |
| 实际系数方向 | −D 变号；pole/prime mixed 与 phase 完整抵消 | 从局部 positive metric 推完整 Weil 正号 |
| strongest-old | 405/563/567/568 归旧；542+555→557 whole 4/5 保持 | 560 growing K/sign/core/coupling/Ξ 未改 |

本轮是真实的固定核比较、可计费用修复和协同构造；不是 classic 新独立正性，宏观瓶颈未改变。
一轮后停止调 κ/δ/sector 或未知 line 标签的止损范围合理。
回 560 的实际 receiver mixed 准入是尚未执行的下一动作，不能把结算中的计划当成已付数学结果；
其 fixed-S 测试即使成功，也须另外核 strong-old 净后果和成长门，不能以旧任务换名完成 Goal。

## 9. 最终版本绑定

以下均按 UTF-8 文本去除 BOM 并统一 CRLF/CR 为 LF 后计算 SHA256。
hash 仅固定本次审阅版本，不认证数学或外部论文。review 自身不作循环 hash 绑定。

<!-- FINAL_LF_BINDINGS -->

| 文件 | LF SHA256 |
|---|---|
| notes/569-dual-carrier-gamma-normalization-and-budget-cocycles.md | `5b423e7d023a413f3c3d1fb0f582073015285e84afd38b4761d9d3734f57da45` |
| reviews/2026-10-20/dual-gamma-cocycle/dual-conormal-source-audit.md | `adcc19bae0b9fec1a83d6e8ff636269f846f340b71ff3016fb0e8c87fad1c606` |
| reviews/2026-10-20/dual-gamma-cocycle/budget-cocycle-and-determinant-line.md | `dbfef0dc2d946e6577d36cfe0d57d3ccd211b02a331a2589544821390a7793c8` |
| reviews/2026-10-20/dual-gamma-cocycle/continuous-function-field-tests.md | `d91ffd874047bc63f886b639d470c8b065771d25b2a9475da407b4338da4da3b` |
| reviews/2026-10-20/dual-gamma-cocycle/dual-conormal-source-record.json | `464ee57d88af981d92f60fd0d2354854a6e1b9e9a54bd4806c8d19a1ea0b955e` |
| reviews/2026-10-20/dual-gamma-cocycle/root-source-read-record.json | `a23d47db9cff972d19bac9d5efa6c33f761a888629a8fef7b5c7f7a3e9c03c21` |
| reviews/2026-10-20/dual-gamma-cocycle/model-exact-checks.json | `977fb249a254003efc9821f6b1206e2cac2f831568fb06afde83e978e8aee8dd` |
| reviews/2026-10-20/dual-gamma-cocycle/root-analytic-checks.json | `4e4d5483ba22c3f927fb4dbaa2b2e471bde536cffcda917b92a04478dfed7315` |
| goals/contracts/C032-dual-carrier-gamma-and-budget-cocycles.md | `187cea9b4352f8f65e1979326c705cdae32878ace117437c78e6c242988906dd` |
| goals/reviews/2026-10-20-dual-gamma-cocycle-569-settlement.md | `9ae1a1160369816ef8b6a100a2a952ef24bb15df20900c394e583097e7e8ec15` |
