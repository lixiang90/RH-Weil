# 552. 真实径向 adelic Green 修复：主关系下降与完整 Weil 比较门

2026-10-14；当前用户要求跨轮总结、完善宏观 Goal 并开始执行。
本稿执行 D20261014Z 保存的唯一来源类别门；C021 不重开，不建 C022。
归类：旧来源/最强旧范围恢复和一个具体修复的准入检验，零数学轮；不是 Goal 3 方法类边界。

## 1. 原对象和两种不能混淆的来源

405/406 的实际映射为 Eη(u)=2Σ(n≥1)η(ne^u)，源是实偶 Schwartz，
η(0)=∫η=0。519 已经证明 E 的像不是一般 Weil 向量，而是完整 ζ-zero-jets
关系理想 I；P_an=I∩ker d∩ker c。这个最强旧事实必须在尝试 Hodge 对象之前消费。
不能把 Fredholm 参数 z 的有效零除子误认成 ζ 商上的非退化 primitive 向量。

物理源与旧源坐标的精确关系是 r(u)=e^(u/2)f(u)，f=e^(-u/2)r。
405 的 sharp f(u)=e^(-u)f(-u) 在这个中心化后变成普通反射，
c(f)=∫e^(-u/2)r(u)du，d(f)=∫e^(u/2)r(u)du。
含恒等元正规化的完整显式公式给实源

    Q_W(r)=2d(f)c(f)−2B(f,f).

复源采用相应 Hermitian 极化，保留 actual Γ=2θ′、全部 prime powers 和双 pole。
这不是只核了无穷位或 spectral inner product 的重新定义。

取非零实偶 ψ∈Cc∞((-17/16,17/16))，r0=(D²−1/4)ψ。
分部积分给两个 pole 矩为零；r0≠0，因为紧支非零函数不能解该齐次常微分方程。
537 给 Q_W(r0)>0，所以 f0=e^(-u/2)r0 不在 I。
任何要求存在合法 Schwartz η、Eη=f0 的普通逆构造，已经被最强旧范围排除。
有限/双矩修正的合法 η 仍然只给 I/P_an 中关系，不能免费改变这个范围。
这只是旧知识恢复，不是新 RH、正性或方法边界。

## 2. 核过的独立 Hodge 原件

作者 [Yuan–Zhang 原件](https://web.math.princeton.edu/~shouwu/publications/hodge-I-version2.pdf)
标明 2013-05-21；缓存版本及 SHA、读取页范围见本轮 source-metadata.json。
root 已视觉核 PDF pp.4、13–14 和 16；代理不同组织独核。
Theorem 1.3 要求 number field 上 normal/geometrically connected/projective X，
integrable adelic M，nef 且 generic big 的 Li，以及 generic intersection primitive 条件。
等号的 base-pullback 判据另需 arithmetically positive / Li-bounded 条件。
度量须在所有 places coherent；只有一个复解析 strip 的 Fredholm 除子不满足这些前件。
这些都是旧 cited 输入，本轮不因重读定理计独立新增。

这里实际使用 curve 的 vertical 模型公式及其 equality；不假借高维 Hodge 标签。
范数与因子用 PDF p.16 的 ||1||=exp(−φ)、M·N=∫φ c1(M)，
及 dd^c=(i/π)∂bar∂ 固定。PDF p.14 的 Green 字母不能未经核对换成 −log||1||²。

## 3. 一个真正存在、由源定义的非 literal 修复

取 405 明确 η0，p=Eη0，已有 p≠0、c(p)=d(p)=0、B(p,g)=0 对所有 g。
定义 X=P1_Q，底层线丛 O_X；所有有限位用标准 trivial metric；
无穷位用

    ||1||∞(ξ)=exp(−p(log|ξ|)), ξ∈C×（另一个几何坐标，不是Fredholm参数z）.

p 是 Gaussian 多项式的 E 和。正端的 Gaussian 衰减和负端的 Poisson 恒等式
p(u)=e^(−u)E(hatη0)(−u) 使 p(log|ξ|) 在 ξ=0 与 ∞ 都 C∞ flat。
于是该式扩成 conjugation-invariant smooth metric。
有限位来自 P1_Z/O，只有一个 arch 位被改，coherence 已付。
它完全按实际源 p 定义，未按 Q 值或未知零点位置反造度量。

这个 smooth vertical 对象也是 integrable。取 FS 的 O(1)，加充分大的 base constant
使它 arithmetically positive；在紧 P1(C) 上 dd^c p/ω_FS 有界。
取整数 k 足够大，使 kL±M 的曲率非负、全部 horizontal 点的高度非负，
vertical degree 非负，并使 top self-intersection 的 k² 主项压过 k 混合项和固定能量。
故 kL±M 都 nef，M=(kL+M)−kL integrable，且 L-bounded。
这里 k 依赖该源的 curvature/sup/energy；没有统一 all-source/growth k 的声明。

源的“可构造一个合法 adelic 对象”因而是真；停止理由不能再写成所有对象都不存在。

## 4. 它为何不能承担原主关系与配对

对 φ(z)=p(log|z|)，各有限位 vertical contribution 为零，
上述 norm 约定与分部积分直接给

    M_p² = ∫P1(C) φ dd^c φ
         = −(1/(2π))∫C |∇φ|² dA
         = −∫R |p′(u)|² du < 0.

p 非零而两端趋零，所以不是常数，严格不等号已付。
M_p 不是 base pullback，且不能把完整 principal pair 的零类说成这个纯 smooth metric 类。
原 p∈P_an 应作为零主类/根关系下降，B(p,g)=0；此特定 radial Green map 却送它到
非零 Hodge energy 类。因此它不经 S_exp/P_an 下降，也不保持完整 B/Q 的根空间。
这否定的是明确定义的 naive radial repair；不是非 literal/derived/全 place 几何都不存在。
principal pair (div f,−log|f|²) 仍作为一个整体；从未要求其 Green 分量单独为零。

## 5. 频率误差不能免费转成 actual Γ

同一径向 metric 构造对任何实 f∈Cc∞ 给 −M_f²=||f′||²。
复源只能先明确用 Re/Im 两个实 metric 的 energy 和，不能凭 real polarization
自动取得全部复杂几何构造和 principal compatibility。

在固定 I 内取 r_t=ψe^(itu)，或先以两个固定光滑 dual templates 消去两个 pole 矩。
后者的修正系数由反复分部积分为 O_A(t^(−A))，对任意 A，且原 norm/Dlog 保持合法。
f_t=e^(−u/2)r_t，则

    ||r_t||²→||ψ||²>0， ||f_t′||²=t²||e^(−u/2)ψ||²+O(t),
    Q_W(r_t)=log|t|·||ψ||²+O_I(1).

最后一式由实际 Γ 的 digamma 渐近、全部有限 prime-shift 的 bounded correlation
及完整 pole 的快速衰减给出；没有删 pole/pp，fixed I 不把 N-limit 当 growth。
所以对任何在该 fixed 窗与源频率无关的 a>0，Q_W(r_t)/(a||f_t′||²)→0。
一个带严格余量的比较 Q_W≥(1−δ)a(−M_f²)−C||r||²、δ<1、C fixed，不成立。
按此 metric 差值计算的费用不能宣称是可吸收的 actual Γ 误差。
允许非局部平滑、频率适应、额外各 place 数据或完全不同 source class 时，本检验不排除。

## 6. 有限截断与 degree 归一化的合法范围

406 原无限零点不能 literal 装入 fixed projective finite Cartier，是旧直接后果，零轮。
F_R=Π(n≤R)(1−zη(ne^u))² 的 degree 是 2R（非零/碰撞按重数），
其未归一化一级 trace 在固定 u compact 逼近 Eη，有 Gaussian 尾界。
除以 degree 的 trace 却为 R^(−1)Σ(n≤R)η(ne^u)→0；保留非零 trace 需要恢复 R 因子，
费用须重新支付。固定 compact 的超快尾不提供 u→−∞ 或成长支持的统一逼近。
对本稿 η0，finite Fubini 和其 Mellin Aη0(0)=Aη0(1)=0 实际给 c(p_R)=d(p_R)=0；
不能把这个合法逃逸错误地否定。它仍不保持原 Poisson 双端：
p_R(u)=−18π(Σ(n≤R)n²)e^(2u)+O_R(e^(4u)) 于负端，故不在 S_exp，
其 Mellin 是 2H_R(s)Aη0(s)，而非 2ζ(s)Aη0(s)，完整 zero-jets 关系也不能继承。
source 端 η 截断/双矩修正是另一操作，须按 519 的真实四项条件核，
不将两个不同“截断”混用。

还有精确的 compactification 边界层费：选 fixed s>0 小到 η0(st)<0，0<t≤1，
在几何点 |z_R|=s/R 有 p_R(log(s/R))/R→2∫0¹η0(st)dt<0，而 p(log(s/R))→0。
因此未归一化 logmetric 的 sup 误差至少 c_sR。
对任意实 scalars a_R，a_R p_R(log|z|) 在 compactified P1 上 uniform 收敛
当且仅当 a_R R→0，唯一极限是零。必要性先在 p≠0 的 fixed 点逼 a_R 收敛，
再用 z_R→0、连续 uniform limit 逼 a_RR→0；充分性由 ||p_R||∞≤2R||η0||∞。
degree 归一化到 1/R 虽 pointwise 为零，却仍不 uniform。
这排的是整个指定 finite-n radial trace scalar 修复类，不排别的 Green/非局部/全 place 数据。
完整构造/定量尾/normalized fee 的独立稿另存，root 只消费已核量词。

## 7. 前件闭合和止损

对象：旧 E/actual Q 精确中心化；实际 P1_Q trivial adelic radial metric，finite place 标准。
域/量词：全部指定 smooth compact f 及 Gaussian p 的 metric 合法；已核每源 integrability。
已付：旧来源范围与非根坐标、p 的严格 energy 与不下降、fixed-window carrier 的准确误差门。
未付：源商上的非退化 canonical 几何映射；uniform source/growth integrability/费用；
完整 Γ/pp/pole 配对、有效性/对应与 Ξ 识别。
相对固定基线和 latest frontier：仅具体修复的决策信息与旧强范围恢复；无新的 whole forcing。

来源门到此停止，零数学轮；没有“缺附件等待”，没有 C022。
不继续通过调整 scalar/finite R 重复此同一反例，不把本稿扩成 Goal 3。
真正重新准入须给一个在非关系 quotient 方向有值、消去 P_an、由实际算术源定义且具有
完整 source/growth comparison 费用的对象；仅 Hodge 定理、局部 effective divisor 或零主类不足。
宏观 Goal 保持 active，瓶颈仍是同对象独立 signed/正性与成长 core/Ξ。
