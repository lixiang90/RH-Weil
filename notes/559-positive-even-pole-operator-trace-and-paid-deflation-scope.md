# 559. 保正偶极点：原算子、signed trace 与付费 deflation 的消费范围

2026-10-14，root 对四份独立原稿作对象／域／费用／最强旧审查。
同 G20261014、固定 0c4f/≤538；本项是来源和旧后果恢复，0 数学轮。
不登记 C024，不续 C023，whole 对照仍为 557 的 leading 4/5。

## 1. 原对象及完整残差

ALL L≥1，Hspace=L²(I_L,du;C)，I_L=(-L,L)，zeroextension 原 Dlog；
Γ(t)=Reψ(1/4+it/2)−logπ=2θ′。Γ_I 为原闭型的自伴实现。
保 555 全部严格 q<e^(2L) primepowers 的 A_L、exact row F_L，令

    h=cosh(u/2)，c=h/sqrt(L+sinh L)，κ=2(L+sinh L)，s=sinh(u/2)，
    H=Γ_I−A_L，E=H+κ|c><c|，Q=E−2|s><s|。

原稿直接支付 ||c||₁≤4、TV(c)≤4（含两端跳跃），
|hat c(t)|≤4 min(1,1/|t|)。actual Γ 的双尾增长给统一 Γ²-Fourier 费用。
先 whole-line operator domain、再闭型 restriction，得到

    c∈Dom Γ_I=Dom H=Dom Q，||Γ_I c||≤C_Γ，ALL L≥1。
    Qc=Γ_I c+(κ−F_L)c。

这不是只付 form domain 或单个 Rayleigh 值。旧 555 uniform PNT 给
||Qc||≤C_Γ+εe^L+C_ε+C(1+L)，先 fixed ε、L→∞、再 ε 任意，故 ||Qc||=o(e^L)。
没有 absolute o(1)、有效 ε(L)、全 complement gap 或 signed trace 净误差。

## 2. 真正 rank-one response 的符号与迹时间域

使用未归一化 h，N=||h||²=L+sinh L，E_θ=H+2θ|h><h|。
安全 shift b>β_L−Γ0 上，m_θ(b)=m_0(b)/(1+2θm_0(b))；正偶极点分母为 plus。
F_θ(t)=<h,e^(-tE_θ)h> 满足 F_θ=F_0−2θ F_0*F_θ。
完整 Volterra／时间路径系列在每个 fixed L,t 收敛，费用已核；不是成长算术估计。

相对 heat 差在 ALL t>0 trace class，且

    Δ(t)=Tr(e^(-tH)−e^(-tE))=2t∫₀¹F_θ(t)dθ≥0，
    0≤Δ(t)≤e^(-tλ1(H))。

两个 individual global trace 的已付时间域为 t>1；此时 Z_E=Z_H−Δ。
不能将小时间相对迹的合法性写成两个无限 individual 迹已付款。
Schatten 的 full simplex 账本保全部 Γ/prime words，但 generic norm 费用没有胜 4/5。
标量响应仅见 h 的谱测度；整个 odd 空间不受正偶 rank-one 影响。
global signed 差需要独立 J_H−D_* 的同 L,t 完整误差，不能从两项指数 o(e^L) 免费相减。

## 3. 合法 signed finite-rank 修复必须保留

令 P=|c><c|、R=I−P、a=<Hc,c>、w=RHc，σ=||w||。
actual source 定义的修复

    V=−|w><c|−|c><w|，||V||=σ=o(e^L)，rank V≤2

是 bounded selfadjoint；w 只需在 Hspace，不需 Dom H。H'=H+V 保原 Dom H，H'c=ac。
c∈Dom H 使 Pc 保域，selfadjointness 给 R 为 reducing，
D=H'|_R 自伴，Dom D=Dom H∩R，动作 RHR；不是未经核验的 unbounded compression。
Γ/A/c/w even，V 杀 odd，负 odd pole 保留。精确

    E=diag(a+κ,D)−V，
    Q≥diag(a+κ,D)−σI−2|s><s|，
    n_−(Q)≤1+1_{a+κ<σ}+n_−(D−σI)≤2+n_−(D−σI)。

σ 作为 mass shift 已付款，不再按 rank V 重复罚维数。
这是旧 024 接口＋555 row＋原 operator 域的合法直接消费，非新的独立算术 input。
无 pole 热包络或某个未修复分解的失败不能排该逃逸。D 的 gap、whole 费用及 Ξ 仍 open。

## 4. 单 cosh 的补空间固定 gap：实际旧源负对照

旧 405 非零 real-even physical principal r_p=e^(u/2)p∈centered S_exp，
双 pole 矩 exact0，完整 Q(r_p,v)=0。smooth cutoff χ_L crop 到 I_L；
取固定 even b∈Cc∞、C(b)>0，令 z_L=χ_Lr_p−C(χ_Lr_p)b/C(b)。
则 z_L∈Cc∞(I_L)、C=S=0、z_L⊥c，z_L→r_p in 原 S_exp，norm→非零。
消费 405 已付的完整 Γ/全部 pp/pole 联合连续性，给单位化 Q(z_L/||z_L||)→0。
因此一个 cosh channel 不付 cofinal fixed γ>0 complement gap。
这不证 Q 负，不排 γ_L→0、growing core、付费 Γ、signed Schur 或其他 source/domain。
本记录只消费上述单 channel 反例；宏观稿的更强 bounded-rank 推论不另登记新结论。

## 5. Root 前件闭合与宏观决策

对象／原 norm／operator domain／ALL complex／ALL L≥1／全部 properpowers／双 pole 已核。
已付误差为 BV endpoint、actual Γ² 双尾、fixed-time trace class、rank-one norm 及旧 PNT 量词。
actual c residual、scalar response、global trace、complement D 和 whole Q 五个角色不合并。
独立 signed global 费用、core coverage/gap/coupling、成长全域正性及通常 Ξ 识别未付。
扣除 542＋555 已蕴含的 4/5 后，净结果为来源范围恢复与选择信息；瓶颈没有消除。

整门 source0 停止，不优化 c、热时间、rank-word 长度或 η/k。
下一先做一次真正 joint finite-S 投影的 mixed 算术系数门，核 full Gram inverse；
原 primary 只付 Hilbertian 同构，不预授 whole Weil 正性或 C024。
重准入须 actual 全源 joint 费用及扣 4/5 后净 core/whole 后果，不能只给 formal response。

四原稿及依赖版本见 [root 消费收据](../reviews/2026-10-14/even-pole-source/root-consumption-scope.json)。
原稿出稿、root 消费和数学结算分开；hash 与结构 check 不认证证明。
