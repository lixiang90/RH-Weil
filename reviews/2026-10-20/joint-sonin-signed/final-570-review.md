# 570 独立终审：真实 F23、稠密双尺度平均、全部返回与原范数

2026-10-20；独立审阅当前 C033 主稿及三份原证明，不改公共状态、cadence 或 Git。
恢复已读 goals/README、STATE、Goal、C033、前沿及 D20261020M；research_state.py check/show
仅作结构恢复。本文另核数学，不能以脚本通过或版本 hash 代替证明。

**结论：PASS，严格限固定 S={∞,2,3}、Sonin cutoff 1、固定双 patch 原源窗。**
完整 joint 误差在每 patch 双 pole-zero 的实际源上确有

\[
 E_{23}(g_\eta^\pm)=\pm\frac{\log^2(1/\eta)}{9\sqrt6\log2\log3}
                     +O(\log(1/\eta)).
\]

全部 returns 同时为 O(1)，不是被截掉；dense nonexact 只作窄源平滑平均 O(1)，
没有把稠密比例改成单素数的逐点统一 gap。原 L²／Dlog 归一后该误差都趋零，
完整 Q 自身在本族为正。无限两号指数及有限秩边界合法；非有限秩紧、Γ-relative、
source-adapted 或成长实际 receiver 修复均未排除。未给独立容量或 RH 正性。

## 1. 物理对象与完整源身份

这里 B 非酉。独立重算 FBF=B*、BB*=B*B 后，
F23=BFB⁻¹=B(B*)⁻¹F 确实自伴且平方为 I；不能从 B 的相似变换一般保酉推得。
B 及 B⁻¹ 的非负 delay 保持 high，故 Sonin(F23)=B Sonin(F)，其物理正交投影
正是 BP(PB*BP|M)⁻¹PB*。当前双 cutoff 与 560 full-G 没有换对象。

任意中间源的 E 必须先指 overlap／ε23 型，而非无条件 T23−full Q。
主稿及对象稿已明示此点，允许 φη、β 单项并非 pole-zero 而仍进行极化。
最终源的两个 pole 矩通过实际 2×2 方程精确为零，支持直径严格小于 log2，
所以所有 p^k 的源相关均为零，才有 E23=T23−QW。Γ/contact、所有 proper powers
和双 pole 始终保留在定义里。没有把这些特殊取值冒充一般预算身份。

## 2. joint cutoff、真正源迹和所有返回

逐 d|6、n=2^j3^k 的 operator norm 是 (dn)⁻¹/²，低方形核振幅为 2/d，
HS norm ≤2/d。Schatten 插值后各项 S_p 费为
(2/d)^(2/p)(dn)^(-(1−2/p)/2)，p>2，双几何列可和，所以 K∈S3。
它不要求 K 本身 HS，也没有用核点值求迹。

ηop=(B*)⁻¹ 及逆保持 low，F23ηop=ηopF。若 low f 及 F23f 同为 low，
运输后违反普通 Fourier 紧支唯一性。紧 contraction 因而有 κ<1。
更精细的 (m/M_B)²(1−||LFL||²) 下界也成立：
||Hηop v||≥||Hv||/||ηop⁻¹||，且 ||ηop⁻¹f||≥||f||/||ηop||。
这是 fixed S 的实际费用，不给成长统一 gap。

535 的 source-S1 引理在每个 fixed smooth r 上给
||A_r L F_λL||1≤C_r(1+logλ)/√λ；C_r 含导数费。
因此第一 Fourier 因子夹源后 S1 收敛，另一因子 operator norm 收敛，
而不是对 ambient 裸级数逐项取 trace。每个 η 的 ordinary trace 先合法，才取 η→0。

用 F23 的 low/high block [K,A;A*,D] 重算，AA*=1−K²、KA+AD=0，
确有 O=Π+L+FLF−I=Φ(K(1−K²)⁻¹)。对实源 Z=A_r*A_r 与 F23 交换，
得到合法半迹 2Re Tr_L[h(K)LZHFL]。复源用实际 ε 的实偶性分解并作 Hermitian 极化，
不是假设所有实源都偶。

C=K³(1−K²)⁻¹∈S1，||Φ(C)||1≤2||K||S3³/(1−κ²)。
故全部 returns 对 L1=O(1) 的窄源同时 O(1)。这是全逆精确分离，
没有截 return 次数或把有限 Fourier 截断当作 involution。

## 3. 一手定理实际重开与 dense nonexact 的双高度控制

本终审实际重开 [Bugeaud–Mignotte–Siksek, Annals 163 (2006),
pp.988–989, Theorem 9.4](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf)。
原文先定义乘积减一 Λ、绝对对数高度与 modified height，再给 real-field 下界，
证明将其归到 Matveev Corollary 2.3。这里只核已知定理的合法实例，未重证深定理。

取 n=2、L=Q、D=1、α1=2、α2=3，两个 modified-height 上界可取 a=log2、b=log3；
它们均超过 0.16。唯一分解付乘积非零，实数域系数是
M0=1.4·30^5·2^(9/2)ab。故 |2^m3^n−1|≥e^(−M0)B^(−M0)，
B 取实际指数最大值的更大上界 ≥3 合法。随后在有界 log 范围用均值定理，
才得到 |ma+nb| 的多项式指数高度下界。没有遗漏乘积到 additive log 的转换。

本终审另从积分式重算 Si 界。令 q=r−e^t s 或 r+e^t s，
先积 z 后的一项是

\[
 \frac{\operatorname{Si}(2\pi q)-\operatorname{Si}(2\pi qe^{-t})}{2\pi q}.
\]

两个端点在大相位时常数相消，故为 O(q⁻²)；小相位直接有界。
端点 x∈[e^(−t0),1] 离零，故对 t∈[0,t0] 亦可取统一界，不需除以 t。
这点足以覆盖 self 中心，不能只引用 J⊂(0,∞) 的未付端点外推。

尺度写 2^J3^K/6，以 H=max(J+K,J'+K') 为高度，每层 pair O((1+H)³)。
可比 pair 的两尺度至少 ce^(aH)。在 d 的 nonexact 中心，Matveev 付
c(1+H)^(-M0) 的 log separation。取固定 εM0<1，H≤η^(−ε) 时 η 位移
保留一半 gap，费用被 Σ_H(1+H)^(3+2M0)e^(−2aH) 控制。
高高度完全放弃 gap，改用窄源 L∞≤C/η 及单调相位换元，逐 pair 费 C/(ηs)，
全尾 η⁻¹Σ_(H>η^(−ε))(1+H)³e^(−aH)=o(1)。不可比部分直接求和。
这闭合了全部 dense nonexact 平滑平均 O(1)，没有任何逐点 uniform-gap 前提。
同一无 η 区间积分界还付 pair 核局部绝对 L1 和，与真实 source trace 极限一致。

## 4. 双 cos 系数、self 边界及 exact 计数

实际核振幅从 operator norm 级数合并所得：内部 2/3，两边界 −2/3、−1/3，corner 1/3。
没有再添 r⁻¹/²。重算源半迹时 L U_t H 在 t>0 为零，负时间有真实矩形；
外部 2Re 与最终 even 延拓共同给主稿的 I(r,s)(t)，不多也不少一个 2。

内部 exact family 为 s=2^j3^k、j≥1，r=(3/2)s。其振幅乘积 4/9，
双 cos 差相位的常数项恰为
e^(d/2)(1−e^(−d))/2=sinh(d/2)=1/(2√6)。
二维计数 L²/(2ab)+O(L)，乘得 C23=1/(9√6ab)。
数值只作因子核对 C23≈0.05956785363365116，非拟合证据。
低 scale 的 O(η+(ηs)²) 总费 O(L)，高 scale 的 1/(ηs) 尾亦 O(L)，
边界行只有一个自由指数，仍 O(L)。

self exact r=s 要另付 t→0 的区间收缩，直接 |I(r,r)(t)|≤Cmin(t,1/r)。
低／高 scale 平均给 O(ηL²) 与 O(ηL)，nonexact 用上节中心零的分裂为 O(1)。
固定 β 的混合项由 ε 有界与 βhat∈L1 支付 O(1)，其系数有界。
最终 g± 的 1/√2 使两个正负 cross 各权 1/2，正好得到上面的 ±C23L²。

## 5. 任意有限 Gram、无限指数和允许修复

取任意先 fixed N，稠密群 <log2,log3> 可把
x_i=log(5^i2^(m_i)3^(n_i)) 放入同一小 patch。
不同 i 的 5-adic valuation 区别，保证中心差及加减 d 后都不落在 <log2,log3>。
此处 5 只是选源中心的数论标签，算子 S 始终 {∞,2,3}，没有加第三有限位。

2,3,5 的同一 Thm9.4 实例有 D=1、A=(a,b,log5)，第三指数 i−j 为 fixed 非零。
所有 offdiagonal 为 O_N(1)，diagonal 为同号 C23L²+O_N(L)，故任意 N 维严格两号空间成立。
每个源仍在同一固定支持窗、每 patch 双 pole-zero；这些矩条件在 L² 有限窗为闭条件。
与任意有限余维闭条件或有限秩自伴修复的 kernel 相交只损失有限维，故无限两号仍在。
该推论没有排除无限秩 compact 修复，不从有限 Gram 冒称全域 PSD。

## 6. 原 norm／Γ 价格及 strongest-old 扣除

原 du L² 范数平方为 Cφ/η+O(1)。对 log(2+|ξ|) 的 Dlog，直接缩放产生
η⁻¹(CφL+Cφ,log)+O(L)；低频差不能默写为 O(1)。分离 patch 的该范数交叉有界，
窄源与 fixed β 的交叉由快降 Fourier 支付。这与主稿归一渐近一致。

完整 Γ 高频为 log|ξ|−log(2π)+O(ξ⁻²)，与该主项的差在 L1，故
qΓ(hη)=η⁻¹[CφL+Cφ,log−log(2π)Cφ]+O(1)。
穿孔核为 −e^(−|t|/2)/(1−e^(−2|t|))；两个 patch 分离，只移除该 mixed 中
contact 的支持贡献，不是删掉完整 Γ 的 contact。一般 mixed 有有限 CΓ；
偶 φ／镜像 β 的可选子族以绝对收敛 Laplace 平方和给 CΓ<0，不能推广到任意形状。

Γ 价格 η⁻¹L 远大于 signed 误差 L²，所以 QW(g±)>0。按原 L² 规范化 E 为
±(C23/Cφ)ηL²+O(ηL)，按 Dlog 为 ±(C23/Cφ)ηL+O(η)，均趋零。
本族也在 537 的旧 fixed-window 全源正性内。没有 QW 负值，没有新经典正性。

norm 稿从 560 账本平衡 N(R) 得 ν=a0/[4(a0+b0)]、p0=1−2ν，
a0=−logρ、b0=logΩ。两项 R⁻¹/⁴Ω^N√logR 与 ρ^NlogR 的指数及 log 次数
独立重算相等；其精细幂率只是旧全逆估计的可消费后果，不重复计新 whole 输入。
它允许 log² 的离点可积奇性，与本轮实际符号结论一致。

最强旧 542+555→557 whole leading 4/5 不变；560 的 fixed-S compact 桥保留。
本轮真正新增的是 fixed double-prime actual 比较的两号及无限指数，消除了此局部未知号，
而非改善成长容量。cofinal S_L 的 κ、S3／returns、对数型常数、actual receiver 像、
source coverage、core／coupling 和通常 Ξ 均未付。不能从 fixed 2,3 的深算术估计
推广所有 g-integer 群，也不能要求所有同源 Gram PSD 后再称作独立容量。

## 7. 可消费范围与版本

root 可消费：同一 full-G 物理投影、每 fixed smooth 源 ordinary trace、全部 returns O(1)、
dense nonexact 平均 O(1)、exact 系数／两号、固定窗无限指数、原 norm 和完整 Γ 价格。
消费链为 535 source-S1＋560 同源 identity＋本轮 joint-S3/gap＋独立 BMS 实例，
再到同一实际源的 mixed；没有先假定零点位置或全源 Weil 正性。

尚不能消费：一般 g 分布的真实评价／全局截面容量、成长 S 的统一费用、全域有利比较、
whole 4/5 改善或宏观 Goal 完成。合同统一一轮由 root 另结算，本审阅不消费 cadence。
以下 LF SHA-256 仅冻结已经完成上述数学核查的版本，不承担证明功能。

| 最终已核文件 | LF SHA-256 |
|---|---|
| notes/570-actual-joint-sonin-signed-mixed-and-narrow-source-cost.md | `6c787848770f78a9f535e381ba512352d46e84eb365f49b29d10097c00ff3315` |
| reviews/2026-10-20/joint-sonin-signed/actual-kernel-and-source-trace.md | `bc9c59754e94bea69889790c28999ffaf76beb34dcd59c5b2dc59753ad7ac953` |
| reviews/2026-10-20/joint-sonin-signed/mixed-returns-and-sign.md | `51aada5556479b911bc9217cd76a2dc0613d490b0ee17644781a5d2981fd6720` |
| reviews/2026-10-20/joint-sonin-signed/narrow-source-norm-and-capacity.md | `ba36398ccc3b54ac119e57bfffaf558b3762a882b4004563e2a3b78c000b4743` |
| notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md | `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3` |
| notes/535-actual-first-prime-sonin-log-resonance-and-indefinite-error.md | `e83c3e080d19c2534425fb3c0e469367012f6c566a470b3baba703fb6def146f` |
| goals/contracts/C033-actual-joint-sonin-signed-mixed.md | `93d8f25daf610367f9eb61f1903565e862a0aa0b0db28117a5aa9f4c1105e2ad` |

最终 root 排版／语义补明已重新核读：intermediate overlap 与最终 full Q 的区分、
复源由实际 ε 实偶处理、Si 界在 [0,t0] 无 1/t 费用，以及 5 只标记源中心不扩算子 S。
这些修复均在 root 消费前，未撤销旧已结算前件。以上最终版本继续 PASS。

提交前 whitespacecheck 另删 kernel §7 的 `actual joint` 后一个行尾空格。
已用恢复该单一空格后 SHA 恰等前审 d9563536… 的方式核实仅此排版 diff，
更新上表绑定；数学内容和 PASS 范围不变。
