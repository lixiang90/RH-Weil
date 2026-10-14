# C017：actual Γ 的 cell 自能与全 complex 交叉费用

2026-10-14；独立审查，仅编辑本文件，不编辑 STATE、cadence 或 Git。
恢复时 STATE 为 C017 ready / latest 545 / cadence 3；实际 HEAD
25d856b7b15f1b7dec6fb971c53f15d7f5ec174b，初读工作树 clean。
子代理 get_goal 返回 null，不据此判断 root 的 runtime Goal。
本审查证明 Γ 准入门，不认证整除费用、双 pole、whole Q 或宏观完成。

## 1. 实际对象、原件与系数

冻结任意整数 N≥4，M=N−1，L=(log N)/2，

    h=1/[8N(log(2N))²]，x_n=−L+log n，I_n=(x_n,x_n+h)，
    Ω_N=union_(1≤n≤M) I_n。

原 physical Hilbert space 为 L²((-L,L),du)，零延拓到 R，Fourier 约定

    hat f(t)=∫_R f(u)e^(−itu)du，||f||²=(2π)^−1∫_R|hat f(t)|²dt。

actual multiplier 与自然闭型域为

    Γ(t)=Re ψ(1/4+it/2)−log π=2θ′(t)，
    Γ₀=−γ−π/2−3log 2−log π，
    Dlog={f∈L²(R): ∫_R log(2+|t|)|hat f(t)|²dt<∞}。

已读 016/017 的 2026-10-13 normalization errata、023 §7 和 543 §2；
旧 half multiplier 不可消费。本次现场核
[NIST DLMF 5.9.16](https://dlmf.nist.gov/5.9#E16)：对 Re z>0 的 digamma
积分减去 z=1/4，取实部，再以原积分变量 r=2a，恰给

    Φ(t):=Γ(t)−Γ₀=2∫_0^∞ K(a)(1−cos(ta))da，
    K(a)=e^(−a/2)/(1−e^(−2a))，a>0。

因此 Plancherel/Tonelli 的精确系数为

    qΓ(f)=Γ₀||f||²+J(f)，
    J(f)=∫_0^∞ K(a)||τ_a f−f||²da
        =(1/2)∫_(R×R)K(|u−v|)|f(u)−f(v)|²du dv
        =(2π)^−1∫_R Φ(t)|hat f(t)|²dt。                    (1)

这里 τ_a f(u)=f(u+a)；正跳型是全线零延拓后的 killed 型，不能换 regional 或周期型。
Φ 与 log(2+|t|) 的 form norm 等价已经由 543 的实际 Γ 尾证明支付；
也可直接由 K(a)=1/(2a)+O(1)（a↓0）及指数可积尾推出。
NIST 原式是旧输入；以下 comb 的整个交叉算子支付才是本审查要检验的门。

## 2. spacing、每格独立 profile 与密度

对 m>n，

    log(m/n)≥(m−n)/m≥(m−n)/M。

hM<1/8，故所有 cells 不相交，任意两格距离至少
log(m/n)−h>0。末格仍在原 I_L 内，因为

    log(N/M)≥1/N>h。

第一格左端恰为 −L，开放端点不影响 L²。定义

    H_Ω={f∈L²(R): f=0 a.e. off Ω_N}，D_Ω=Dlog∩H_Ω。

每个源的各格 profile 完全独立：f(x_n+v)=f_n(v)，0<v<h。
分解是原 norm 等距的有限直和，||f||²=Σ_n||f_n||²；绝不假设 f_n 是同一个 g 的 scalar 倍。

原域确实按格分解。用光滑有界 χ_n，在 I_n 上等于 1、其余 cells 上等于 0，
则 f_n 的零延拓为 χ_n f。由 (1) 与

    ||τ_a(χf)−χf||²
    ≤2||χ||_∞²||τ_a f−f||²+2||τ_aχ−χ||_∞²||f||²，

以及 ||τ_aχ−χ||_∞≤min(a||χ′||_∞,2||χ||_∞)，得到乘 χ 保 Dlog：
核在 0 为 O(1/a)，在 ∞ 指数衰减，所以第二项可积。
反向用有限和的线性域即可。故 f∈D_Ω iff 各零延拓 f_n∈Dlog。

Cc∞(Ω_N) 是 D_Ω 的 form core，不是另换合法域：逐格围绕中点把支撑缩至内部，
再 mollify。收缩在 weighted Fourier norm 强连续：频率变量缩放后
log(2+|t|)/log(2+(1−ε)|t|) 对 ε≤1/2 一致有界；先在频率紧支撑函数验证，
再用 weighted L² 密度。平移只乘 unit-modulus phase。
mollification 的 Fourier multiplier 有界且逐点趋 1，dominated convergence 给 form 收敛。
格数有限，逐格加总。所有证明先在这个 smooth core 上做，也可由 (1) 直接扩张到 D_Ω。
任意 L² profile 不必有有限 Γ 能量；域外 J=+∞ 只能按 extended positive form 理解。

## 3. 各格零延拓自能的统一显式下界

任意 g 支撑长度 h 的格，a≥h 时 g 与 τ_a g 的支撑 a.e. 不相交，故

    ||τ_a g−g||²=2||g||²。

从 (1) 舍去 0<a<h 的非负项：

    J(g)≥2∫_h^∞ K(a)da ||g||²。

h<1。对 h≤a≤1，用 1−e^(−2a)≤2a 与 e^(−a/2)≥1−a/2，得

    2K(a)≥e^(−a/2)/a≥1/a−1/2。

因此，对所有合法 complex profile，

    qΓ(g)≥[log(1/h)−CΓ]||g||²，
    CΓ:=−Γ₀+1/2=γ+π/2+3log 2+log π+1/2。             (2)

这是同一个 actual Γ，全源、无频率截断、无数值误差；没有少一因子。
常数只是可用显式界，不声称最优。Γ 单独的下界具有真实非空 eventual 范围：
例如任何整数 N≥ceil(exp(CΓ+1))，第 5 节 whole Γ 下界严格大于 0。
whole Q 的 eventual threshold 还必须由另外两个算术/pole费用同对象支付，不能由此句代替。

## 4. 所有跨格项的精确算子与 norm

令 C_N 是 H_Ω 上的 off-diagonal integral operator：

    (C_N f)(u)=Σ_(m≠n) ∫_(I_m)K(|u−v|)f(v)dv，u∈I_n。

它是有界自伴实核算子，不是一个已证正半定的 quadratic form。
从 (1) 的 polarization，格间支撑不相交时 Γ₀ 项为 0，且

    qΓ(f_n,f_m)=−∫_(I_n×I_m)K(|u−v|)f_n(u)overline(f_m(v))du dv。

故完整 mixed identity 是

    qΓ(f)=Σ_n qΓ(f_n)−〈C_N f,f〉。                    (3)

如担心 0 点奇核，先将 K 截断到 ε<a<R，展开等式，随后取 ε↓0、R↑∞：
各自能由 Tonelli 单调收敛；格间有正距离，且以下统一 row 积分可支配，
所以 crossed term dominated convergence 合法。D_Ω 内所有自能有限。

写 d_nm=|log n−log m|。u∈I_n,v∈I_m 时

    |u−v|≥d_nm−h≥(7/8)d_nm，d_nm≥|n−m|/M。

使用对所有 a>0 的 elementary bound

    K(a)≤1/(1−e^(−2a))=1+1/(e^(2a)−1)≤1+1/(2a)，

得到任意 u∈I_n 的 row 积分

    Σ_(m≠n)∫_(I_m)K(|u−v|)dv
    ≤h[(M−1)+(4M/7)(H_(n−1)+H_(M−n))]
    ≤h[(M−1)+(8M/7)H_(M−1)]
    ≤2hM log(2M)，M≥3。                               (4)

最后一步由 H_(M−1)≤1+log M，以及
1+(8/7)(1+log M)≤2log(2M)（M≥3）给出。
例如差为 (6/7)log M+2log2−15/7，递增且 M=3 已为正；
只需 log3>1、log2>2/3 即可验证，无浮点计算。
核对称，column 同界。对 arbitrary complex f，Cauchy–Schwarz/Schur 积分估计给

    ||C_N||_(H_Ω→H_Ω)≤2hM log(2M)，
    |〈C_N f,f〉|≤2hM log(2M)||f||²。                  (5)

这是整个 ℓ²({1,…,M})⊗L²(0,h) operator bound；用每个独立 profile 的 norm 即可。
没有用 finite scalar matrix PASS、同 g 假设、频窗样本或 ζ 零点。

## 5. Γ 门、反例与对数费用的真实大小

联 (2)–(5) 的已证结论为

    qΓ(f)≥[log(1/h)−CΓ−2hM log(2M)]||f||²，f∈D_Ω。   (6)

冻结 h 下，cross fee≤1/[4log(2N)]，趋于 0。
第 3 节的显式 Γ-only threshold 成立，因为 log N≥CΓ+1，
log(1/h)=log N+log8+2log log(2N)，且 cross fee<1/4；
这些附加正项使 (6) 严格为正。它不是 whole Q 的认证范围。

跨格项不可无声删除。取任意非零非负 g∈Cc∞(0,h)，只用格 1、2：
profile 为 (g,g) 时，(3) 的 cross 为严格负数，qΓ(f)<qΓ(f_1)+qΓ(f_2)；
改为 (g,−g) 时严格反向。两源都在原 Cc∞((-L,L))。
故“Γ 自能可直接相加”的等式/下界组织错误；同时 C_N 也有正、负 quadratic directions。
这些反例不推 whole Γ 负，更不推 whole Q 负。

log M 因子也不是只由粗 proof 人工制造。取

    g_h(v)=sqrt(2/h)sin(πv/h)，0<v<h，
    J_M={ceil(M/2),…,M}，j=|J_M|，
    f_n=g_h/sqrt j for n∈J_M，f_n=0 otherwise。

这给 ||f||=1；g_h 零延拓属于 H¹(R)⊂Dlog，是实际合法源，
也可在原 form norm 用 Cc∞ profile 逼近。
各 active 格比值≤2，距离 a≤log2+h<1。
若 k=|n−m|≥1，则 a≤2k/M+h≤(17/8)k/M，因而

    K(a)≥e^(−1/2)/(2a)≥(4e^(−1/2)/17) M/k。

又 (∫g_h)²=8h/π²，得到

    〈C_N f,f〉
    ≥[64e^(−1/2)/(17π²)]hM[H_(j−1)−(j−1)/j]。

M≥32 时，括号≥log(M/2)−1≥(1/2)log M，故

    ||C_N||≥[32e^(−1/2)/(17π²)]hM log M，M≥32。       (7)

因此全 profile 的一般跨格费用阶确为 hM log M；宣称 uniformly O(hM) 的
Γ cross bound 会被这个合法族否定。若要求 smooth 源，可先保留略小常数再用密度逼近。
冻结 h 使此真费用趋 0；不靠把真实 cross 改成 0 取得净余。

## 6. 消费范围、旧资产扣除与下一责任

023 的 abstract concentration/minmax、不确定性和 actual 谱底是旧工具；
543 的 Γ jump representation 也是旧输入。本文件不能孤立命名一个 generic Γ 工具为创新。
本审查新支付的是冻结实际算术 comb 上任意 independent complex profiles 的精确 Γ block
组织、统一 crossing norm 和域；须由 root 同 exact 全 pp weighted divisibility 与
同源 signed dual-pole 合并、对最强旧 016/028/543 后果逆审，才能判断是否有新 joint 净值。
069/080 的 finite incidence/RH-equivalent functional 及 167 的 hard diagonal 不能
直接替代本 common physical source 的 complete Γ cross；是否已有更强 whole comb 结果，
仍由负责旧资产的独立审查确认。

本文件无 prime 或 pole estimate，不声称 Ω_N 正性、全源成长正性、spectral count 改进、Ξ识别或 RH。
Ω_N 总 measure=Mh→0，core/补空间与耦合责任仍未付；self 增长不证明覆盖性。
本门通过后，唯一消费动作是核整除/pole 费用并在同域拼 whole Q；失败的 O(hM)
反例仅防止少付 log M，不改变本轮冻结参数。宏观 Goal 不因本文件或合同通过完成。
