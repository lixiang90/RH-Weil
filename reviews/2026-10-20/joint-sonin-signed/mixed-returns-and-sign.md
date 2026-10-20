# 固定 F23 的全部 returns 与真实 mixed 窄源符号

2026-10-20；570 配套独立原稿。固定 S={∞,2,3}、Sonin cutoff 1、原物理范数。
本稿消费 560 的完整同源身份和本轮 `actual-kernel-and-source-trace.md` 的真实夹源迹域；
不把 single-prime 结果相加，不把裸 B*B 的 ratio 系数当实际误差。
新结论限固定源窗上的 actual E23=T23−QW；没有 RH 或成长尺度结论。
为允许中间的 φ_eta、β 单项尚不满足 pole-zero，全文任意源上的 E23 先定义为
560 的 overlap／ε23 型，即 T23−qΓ+P_(2,3)；只有在本次最终双 pole-zero、
全部 prime-power 相关为零的源上，才再识别 E23=T23−完整 QW。

## 1. 对象、合法源与待判系数

令 a=log2、b=log3、d=b−a，固定

    0<δ<min(d,a−d)/2。

取实 φ≥0、φ∈Cc∞(−1,1)、∫φ=1，φ_eta(u)=eta^−1 φ(u/eta)。
在 (−δ,δ) 内固定两个避开 0 且分离有序的实 smooth bumps β1、β2；
其 (∫e^(u/2)βj,∫e^(−u/2)βj) 两列不成比例。
逐 eta 精确解此 2×2 系统得到有界实系数 A_eta、B_eta，使

    h_eta=φ_eta−A_eta β1−B_eta β2，
    ∫e^(±u/2) h_eta(u)du=0。

取

    g_eta^±(u)=[h_eta(u+d/2)±h_eta(u−d/2)]/sqrt2。          (1)

每个 eta 的源均为原 Cc∞，两个 patch 不交，每 patch 的双极点矩严格零；
整个支撑直径 d+2δ<a，所以全部 prime-power 相关严格零。
这里是完整 QW 中相应项精确为零，没有删除 Γ 或截断素数幂。
∥h_eta∥1 及 ∥g_eta^±∥1 一致有界。

结论是

    E23(g_eta^±)=±C23 log²(1/eta)+O(log(1/eta)),
    C23=1/(9 sqrt6 log2 log3)>0。                         (2)

分母 sqrt2 是本次实际源的规范；若不除 sqrt2，主项会大一倍。
以下支付稠密 nonexact ratio 和全部返回，不能仅由 exact 子列读出 (2)。

## 2. 实际 trace 与完整返回的费用先于核解释

配套对象稿给 K=L F23 L∈S3、κ=∥K∥<1，实际正交投影确为
Π23=BP(PB*BP)^−1 PB*，不是 B 当酉后的伪投影。
对每个 fixed smooth source，actual overlap 的普通迹可合法写成

    E23(g)=Tr(A_g Φ(K) A_g*)+Tr(A_g Dret A_g*)，
    Dret=Φ(K³(I−K²)^−1)∈S1，
    ∥Dret∥1≤2∥K∥S3³/(1−κ²)。                            (3)

因此 ∥g∥1=O(1) 时全部 returns 同时为 O(1)，并非只控制首个 return。
对应源核 Tr(Dret U_t) 连续有界，所以不能抵消 (2) 的 log²。
第一 Fourier 因子夹源后在 S1 收敛，第二因子在 operator norm 收敛，
再逐 finite pair 积分给下列裸核；没有对未夹源 ambient 系列逐项取迹。

合并尺度后写 F23(x,y)=Σ_r c_r cos(2πrxy)，其中

    r=2^j3^k, j,k≥0: c_r=2/3；
    r=3^k/2, k≥0: c_r=−2/3；
    r=2^j/3, j≥0: c_r=−1/3；r=1/6: c_r=1/3。

正 t 的 even bare 源核为 e_bare(t)=Σ_(r,s)c_r c_s I_(r,s)(t)，

    I_(r,s)(t)=e^(t/2)∫_(e^−t)^1∫_0^1
             cos(2πrxz) cos(2πs e^t xz) dz dx。           (4)

对实源 R_g(t)=∫g(u+t)g(u)du，E_bare(g)=∫R_g(t)e_bare(t)dt。
式 (4) 的 even 扩张与此积分的两个 cross 各贡献一半，校准了 (2) 的系数。

## 3. 一手独立算术输入：只用有限 log 线性形式

对 t 位于固定紧区间 J⊂(0,∞)，先积分 z，再将 Si 的两个真正端点相减，得

    |I_(r,s)(t)|≤C_J[(1+|r−e^t s|²)^−1
                         +(1+|r+e^t s|²)^−1]。          (5)

大相位的 Si 常数在两端抵消，所以是二阶衰减。
对 t∈[0,t0] 同样有统一常数：积分端点 x∈[e^(−t0),1] 始终离0，
两个 Si 端点的相消不需除以 t；t=0 时原矩形为空。self 的 exact 行还另用§5的更强区间长度界。
因 log2/log3 无理，比例集合稠密；不能称 nonexact 项有统一 pointwise gap。

需要一个已经独立证明、且不涉及 ζ 零点的量化输入。直接来源是
[Bugeaud–Mignotte–Siksek, Annals 163 (2006), Theorem 9.4, pp.988–989](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf)，
原文从 Matveev Corollary 2.3 推出正实代数数的乘积减 1 下界。
本次已实际核读原刊该定理；历史 507 的来源审查此前消费的是 2,5，本稿另核 2,3 参数。
取 α1=2、α2=3、K=Q、D=1、A1=a、A2=b、B≥max(3,|m|,|n|)。
若 2^m3^n≠1，原定理给 |2^m3^n−1|≥c B^−M，M 固定有限。
当 ma+nb 在固定紧区间时，用实均值定理转换到

    |ma+nb|≥c'(1+|m|+|n|)^−M。                          (6)

非零性由不同素数的唯一分解给出。没有把乘积下界未经转换写成对数下界。
这里不优化常数；例如实数域公式可取 M=1.4·30^5·2^(9/2)ab。
它是很深但既有的独立数论输入；一般 g-integer 的稠密 log 群没有自动的 (6)。

## 4. 稠密余共振：只证明平滑平均，不宣称 punctured 邻域 O(1)

令 ψ_eta(t−d) 的支撑宽 O(eta)、L1=O(1)、L∞=O(eta^−1)。
实际取 ψ_eta=φ_eta*checkφ_eta，故还非负且总质量 1。
尺度写成 r=2^J3^K/6，J,K≥0，以
H=max(J+K,J'+K') 为 pair height；每个整数高度最多 O((1+H)^3) 个 pair。
在 r/s 位于固定可比区间时，r、s≥c exp(aH)。不可比部分由 (5) 直接绝对可和。

中心 t=d 的 exact 条件是 j−j'=−1、k−k'=1。
对其余 pair，(6) 给

    |(j−j'+1)a+(k−k'−1)b|≥c(1+H)^−M。                (7)

选择固定 ε>0 满足 εM<1，切 H_eta=eta^−ε。
当 H≤H_eta、|t−d|≤C eta 时，充分小 eta 保留一半的 (7) gap，故

    |r−e^t s|≥c s(1+H)^−M。

于是全部 low-height nonexact 项的绝对平均费用不超过

    C Σ_(H≥0)(1+H)^(3+2M) exp(−2aH)<∞。              (8)

对 H>H_eta，不声称 gap；对每个 pair 改用 t→r−e^t s 的单调换元及 (5)：

    ∫|ψ_eta(t−d) I_(r,s)(t)|dt≤C/(eta s)。            (9)

全部 high-height comparable 尾至多

    C eta^−1 Σ_(H>H_eta)(1+H)^3 exp(−aH)=o(1)。       (10)

因此所有 nonexact pair 的窄源平均共同为 O(1)，而非只固定一个 pair 取极限。
以上 (8) 的常数极大但 fixed；不会变成 cofinal 素数集的统一费用。
同一估计表明在任意紧 t 区间内 pair 核可绝对 L1 求和，因 (9) 无 eta 的
区间积分费用 O(1/s)，与指数高度衰减相乘可和；其分布核与 §2 实际 trace 一致。
其他 exact ratios 稠密，每一点都可能有尖峰，所以 pointwise uniform O(1) 是错误命题。

## 5. Exact 二维列与主项系数

在内部 exact family，s=2^j3^k 且 j≥1,k≥0，r=(3/2)s；两振幅乘积为 4/9。
t=d 时 cos difference 的平均项是

    e^(d/2)(1−e^−d)/2=sinh(d/2)=1/(2sqrt6)。          (11)

设 L=log(1/eta)。内部 exact 尺度的计数是

    #{(j,k):j≥1,k≥0, ja+kb≤L}=L²/(2ab)+O(L)。      (12)

这是有界斜三角的逐行 floor 计数，不需要任何 ζ 假设。
当 s≤eta^−1 时，(4) 相对 (11) 的平均误差为 O(eta+(eta s)²)，
对二维尺度求和为 O(L)（eta L² 亦吸收在内）。
当 s>eta^−1，(5) 与 v=t−d 换元给每项 O((eta s)^−1)，
其全尾同样 O(L)。sum-phase 全列绝对可和。
exact 边界行只有一个自由指数，至多 O(L)；有限 corner 为 O(1)。
因此

    ∫ψ_eta(t−d)e_bare(t)dt
      =(4/9) sinh(d/2) L²/(2ab)+O(L)
      =C23 L²+O(L)。                                 (13)

在 self 中心 t=0，exact 条件是 r=s。
积分区间长度 O(t)，对 difference phase 先积分 z 有

    |I_(r,r)(t)|≤C min(t,1/r), 0<t≤t0。

低尺度 r≤eta^−1 的总平均为 O(eta L²)，高尺度 Σ_(r>eta^−1)1/r=O(eta L)。
nonexact 项沿 §4 在中心 0 的同一两高度分裂给 O(1)。故 self 窄源 E(φ_eta)=O(1)。

还须保固定矩修正。560 的实际 ε23∈C0，有界；任意 fixed smooth β 满足 hatβ∈L1。
由 |hatφ_eta|≤1，任意 fixed translate 的 cross obey

    |E23(φ_eta(·−x),β)|≤∥ε23∥∞∥hatβ∥1/(2π)=O(1)。

fixed/fixed 项亦 O(1)，有界 A_eta、B_eta 不改变 (13)。
最后按 (1) 极化，两个 even cross 各有 1/2 权重；self 为 O(1)，returns 为 O(1)，得到 (2)。

## 6. 固定窗的无限正负指数与有限修复边界

可在同一固定 patch 中取任意 N 个中心 x_i=log q_i，
q_i=5^i 2^(m_i)3^(n_i)∈Q+，使 x_i 留在更小内区间。
存在性只用 <log2,log3> 在 R 稠密：log2/log3 无理，整数旋转的初等稠密性即可；
m_i、n_i 为允许正负的 fixed 整数。不同 i 的 5-adic valuation 不同，
因此 q_i/q_j 不在 <2,3>。
在每个中心重复窄 bump 和同一固定双矩修正，得到 h_(i,eta)、g_(i,eta)^±。

当 i≠j，self/cross 的窄中心是 x_i−x_j 或 ±d+x_i−x_j，均不属于 <log2,log3>。
本次调用相同 Theorem 9.4 的三个正有理数 2、3、5，D=1，
A1=a、A2=b、A3=log5，第三指数是 fixed 非零 i−j，另外两指数随 pair height 线性增长。
唯一分解付非零，得到依赖这组 fixed 中心的多项式 height gap；§4 对全部 nonexact 项仍适用。
因此 off-diagonal Gram 为 O_N(1)，每个 diagonal 为 (2)：

    [E23(g_(i,eta)^σ,g_(j,eta)^σ)]_(i,j≤N)
      =σ C23 L² I_N+O_N(L)，σ∈{+1,−1}。              (14)

eta 充分小时分别得到 N 维严格正、负空间。故 actual E23 在此固定原源窗、
每 patch 双 pole-zero 的 L2 闭子空间上有无限正、负指数。
每个有限余维闭源条件及每个有限秩自伴源修复都仍保无限正负指数，
因为其 kernel 在每个任意大正/负子空间中只删除有限维。
这是实际 joint 比较的局部边界，不扩为任意 finite S 或 cofinal S_L 的定理。

## 7. 原范数费用与独立容量责任

(2) 的未归一质量为 L1=O(1)，并不是 norm1 发散。
原 L2 norm²=eta^−1∥φ∥2²+O(1)，原 Dlog norm²~eta^−1 L∥φ∥2²。
于是按原 L2 规范化后，signed 项尺度为 ±C23 eta L²/∥φ∥2²+O(eta L)→0；
按 Dlog 能量规范化后为 ±C23 eta L/∥φ∥2²+O(eta)→0。
与 fixed-window compact 完全一致。原 Γ 个体费用仍 ~eta^−1 L，为正且远大于 mixed log²；
本结论不推出 QW 负值，也不改变 537 已知小窗全源正性。

独立新输入是：在 full physical joint 投影上真正支付 dense ratio 平滑费用，
证明 all returns 不抵消可见的 signed log²，并给 fixed two-prime 无限 ± 比较空间。
它把 E23≤0 或 E23≥0 的固定窗未知号问题变成实际不定性，排除无费比较与有限秩补丁。
这仍不提供独立 RR/容量下界；非有限秩 compact 修复、Γ 相对费用、source-adapted 比较合法保留。
若将要求改为完整 QW≥0，或要求所有同源 Gram PSD，仍是 Weil 正性的原责任。
成长窗须另付 S_L 的 gap、S3/returns 费用、Diophantine 常数与实际 receiver/source coverage，
以及相对于最强旧 542+555→557 leading4/5 的 whole 净后果；本稿没有这些量词。

## 8. 消费清单

- 对象/角色：实际 physical F23、Π23/fullG inverse；源为 log 变量 g，非裸求值/辅助 H 向量。
- 域/norm：先每 eta 原 Cc∞ 夹源 ordinary trace；原 du/zero extension Dlog 不改。
- 来源：535 source-S1 机制、560 full same-source identity；本轮对象稿付 joint S3 与 full returns。
  唯一新增外部实例为已核 Theorem 9.4 的 fixed 2,3（有限 Gram 用 2,3,5）；无 RH 前件。
- 系数方向：actual E23=T23−QW 两号皆有，C23 正；不是裸 W 系数，也不是 QW 负。
- 误差：nonexact 平滑 O(1)、边 exact O(L)、全部 returns O(1)；常数仅 fixed S/cutoff/shape。
- coverage：两 patch 双 pole-zero 固定源窗；不付成长 S、完整 all-window 正性或通常 Ξ。
- 强旧扣除：537/538 固定窗正性、560 compact 桥及 whole leading4/5 均保；新后果仅 actual joint signed 边界。
