# C005：真实半局部正交投影运输、迹级数及截断 Fourier 正则性

2026-10-13；独立数学审查，只写本文件，不消费 cadence。
已恢复 AGENTS、README、STATE、check/show、Goal、C005 与 D20261013F；
起始 HEAD `7281079`。核读 [2310.18423v2](https://arxiv.org/html/2310.18423v2)
§4.1、4.4–4.8，重点 (57)–(59) 与 Theorem 4.6。
以下新证明不冒充该文已有正迹比较定理。

## 结论

真正半局部 Sonin 正迹存在于同一紧支光滑 source，且可以精确运输；
其正交投影包含一个不可删掉的压缩 Gram 逆算子。
运输给可重放的 Neumann 迹级数及 Gamma/Sonin 范数相对误差，
但尚未证明 C004 源 L² 上的 signed 主项或 compact remainder。

另独立核得真实半局部截断 Fourier 是 compact **但不是 Hilbert–Schmidt**。
这严格阻止照搬实位快速 prolate 特征值／绝对 epsilon 级数证明。
此结论对象为实际 ambient truncated Fourier，不能升级为源迹差额非紧。

## 普通同构、酉坐标与真实正交投影

令 H_inf=L²(R)_ev，H_2=L²(X_{infty,2})^K。
用真正的酉坐标 U_inf=F_mu w_inf、U_2=F_mu w_2 识别到同一 L²(R,ds)，
而不将 theta_2 本身当作酉映射。
原文给 theta_2 的乘子 `b(s)=1-q exp(-ias)`，其中 q=1/sqrt2、a=log2。
于是共同物理坐标中的 theta_2 是

    B=I-q U_a,
    (U_t f)(x)=exp(-t/2)f(exp(-t)x).

它可逆，`m||f|| <= ||Bf|| <= M||f||`，m=1-q，M=1+q。
这里 B*B=(1+q²)I-q(U_a+U_a*) 不是 I，正交性不能由普通同构保持。

取实位 Sonin 正交投影 P，M_0=Ran P；同 cutoff 的半局部 Sonin 是 B M_0。
Sonin cutoff 此处先固定为1，以便比较 C004 的 S1 trace；
它不是冻结实际 Weil 支持参数 sqrt(mu)。
以下运输公式同样适用于任意正 Sonin cutoff。
令

    C=P(U_a+U_a*)P|M_0,
    G=P B*B P|M_0=(1+q²)I-q C.

则 `m²I <= G <= M²I`。映射 `V=B P G^(-1/2):M_0 -> B M_0`
等距且满射到 B M_0，故运输后的真正正交投影为

    Q=V V*=B P G^(-1) P B*.

直接有 Q*=Q、Q²=Q 和 Ran Q=B M_0。
`B P B^(-1)`只是通常非自伴的相似 idempotent，不能用于免费正性。
`B P B*`也是通常不幂等的正算子，不能替换 Q。
原文 theta_2 与 eta_2 的对偶配对不授权把任一映射称为酉。

## 同源 scaling、迹类与完整 Gram

对 g∈Cc∞(R) 令 A(g)=integral g(t)U_t dt。
共同酉识别保持 scaling，因此半局部表示使用同一个 A(g)，且 A(g) 与 B 交换。
2021 archimedean Sonin 定理给 A(g)P 为 HS。
由于 B、G^(-1/2) 有界，A(g)V=B A(g)P G^(-1/2) 也为 HS。
故真正半局部正迹

    T_2(g)=Tr(A(g)Q A(g)*)
          =||B A(g)P G^(-1/2)||_HS²

合法、有限且非负。不需要另假设 g 保持 Sonin 空间。
这支付 compact smooth 同源正迹存在，不支付它与 Weil 型的符号比较。
任意 g_i,g_j 的 Gram 为

    T_2,ij=Tr_M0[G^(-1) (A(g_j)P)* B*B (A(g_i)P)].

括号内由 HS 乘积为 trace class，交叉由极化成立。
对冻结两移位 g_1,g_2，A_i=U_{c_i}A，c_1=-a/2,c_2=a/2；
正 Gram 的两个对角相同，off-diagonal 是相应 scaling 交叉迹。
这仍不意味着 U_a 保持 Sonin 空间，也不意味着 off-diagonal 有算术符号。

有粗但真实的相对界

    (m/M)² T_1(g) <= T_2(g) <= (M/m)² T_1(g).

该界不支付 C004 固定质量首素数差：T_1 的高频 Gamma 能量可增长。

## 可重放的 Neumann 级数及精确 boundary flux

记 alpha=1+q²=3/2，r=q/alpha=sqrt2/3，rho=2r=2sqrt2/3<1。
因为 ||C||<=2，

    G^(-1)=alpha^(-1) sum_{k>=0} r^k C^k

在算子范数收敛。以 D_N 为截至 N 的部分和，则

    ||G^(-1)-D_N|| <= alpha^(-1) rho^(N+1)/(1-rho).

逐项代入上述 Gram 给一个精确可消费的有限压缩移位级数。
对角迹余项满足

    |T_2(g)-T_2,N(g)| <= kappa rho^(N+1) T_1(g),
    kappa=M²/[alpha(1-rho)]=(M/m)².

交叉余项相应不超过 `kappa rho^(N+1) sqrt(T_1(g_i)T_1(g_j))`。
这些是 Sonin/Gamma 相对估计，不是源 L² 质量估计，不证明紧差额。
固定 N 下右端随高频 source 能量增长；不能将其误读为弱零族上趋0。

令 F=A(g)*A(g)，W=U_a+U_a*。由于 F 与 W 交换，另有准确差额式

    T_2(g)-T_1(g)
       =-q Tr_M0[G^(-1) P W (I-P) F P].

合法性可由差的两个 trace-class 组织核准：P F W P=(AP)* W(AP)，
P W P F P=P W P (AP)*(AP)。因此不用给整块(I-P)F单独宣告 trace class。
此式把未付的 signed source 输入定位为 off-Sonin boundary flux，
不是一个可因普通同构或正投影存在而删掉的项。
本审查尚未给它在 C004 全合法源空间上的有界/紧延拓或精确符号。

## 真实半局部截断 Fourier：compact 但非 HS

此部分使用原文 Fourier intertwining 加上实际 B 乘子独立推导。
在共同物理偶空间中

    F_2=B F_inf B^(-1),
    B^(-1)=sum_{n>=0} q^n U_{na},
    F_inf U_t=U_{-t} F_inf.

因此，适用于 p>1、q=p^(-1/2)、a=log p 的通式为

    F_p=(1-q²)sum_{n>=0}q^n U_{-na}F_inf -q U_a F_inf.

设 L 为物理低支持(0,1)的乘法投影（偶函数以正半轴表示）。
每个 `L U_{-na}F_inf L` 有光滑 cos 核，故为 HS。
级数在算子范数收敛，余项范数至多
`(1-q²) q^(N+1)/(1-q)`。于是 `L F_p L` compact。

实偶正半轴的 F_inf 核为2cos(2pi xy)，上述实际核作为分布恰为

    K_p(x,y)=2[(1-1/p) sum_{n>=0}cos(2pi p^n xy)
                       -(1/p)cos(2pi xy/p)],   0<x,y<1.

核级数没有衰减系数；算子范数中的 q^n 被核尺度 p^(n/2) 抵消。
不能从算子范数几何收敛推核 L² 收敛。

以下证明甚至在远离坐标零点的每个非空矩形中都不为 L²。
取非零 chi≥0 在该矩形紧支光滑，令

    phi_N(x,y)=chi(x,y) sum_{n=0}^N cos(2pi p^n xy).

在该支集 y 离0，反复对 x 分部积分给，对 m≠n，

    integral chi cos(2pi p^nxy)cos(2pi p^mxy)
       =O_k(|p^n-p^m|^(-k)+(p^n+p^m)^(-k)).

全部非对角双和有统一有限绝对界，因为最大指标 j 的频差至少
const p^j，而同指标配对数只有 O(j)。同指标项是
`(1/2)integral chi + O_k(p^(-kn))`。
同样将 chi 改为 chi²，得 `||phi_N||_2=O(sqrt(N+1))`。
核分布与 phi_N 的配对则为

    <K_p,phi_N>=(1-1/p)(integral chi)(N+1)+O(1).

最低频率修正项与所有非对角项均只给 O(1)。如果 K_p 是 L²，
Cauchy–Schwarz 将该配对限制为 O(sqrt(N+1))，矛盾。
因此真正 `L F_p L` 不是 Hilbert–Schmidt；非 HS 不是数值观察。
分布级数在所用远离0的测试上绝对收敛；整体核由算子范数极限确定。

甚至有 ||L F_p L||<1。原文 eta_p 的共同物理表达是

    eta_p=(B*)^(-1)=sum_{n>=0}q^n U_{-na}.

eta_p 与 eta_p^(-1)=I-qU_{-a} 都保持低支持 L，且
F_p eta_p=eta_p F_inf。
若非零 f 与 F_p f 都在低支持，则 g=eta_p^(-1)f 与 F_inf g 均低支持；
这违反实位紧支/Fourier 紧支不确定性。
compact contraction 若有范数1，便达到等号，产生这种非零 f；故范数严格小于1。
其 compact 自伴特征值 lambda_n 因非 HS 满足

    sum |lambda_n|²=infinity,
    sum |lambda_n|=infinity,
    sup |lambda_n|<1.

因此2021实位 epsilon 连续性证明中的快速特征值／绝对可和系数
`lambda_n/sqrt(1-lambda_n²)` 不能免费移植到真实半局部截断对象。
可能存在额外 signed 抵消；本证明没有排除它，也没有证明半局部 epsilon 不连续。

## 冻结弱零族上的实际消费与精确 open 项

取 C004 的 h_m=D(D+1/2)[chi cos(my)] / norm，严格两矩零且弱趋0。
两 patch 等号／反号组合记 G_m^+、G_m^-，源范数平方都是2。
已证完整 prime 账本及实位 epsilon 紧性给

    (QW-T_1)(G_m^+) -> -2w2,
    (QW-T_1)(G_m^-) -> +2w2,
    w2=log2/sqrt2.

令 d_m^±=(T_2-T_1)(G_m^±)。本审查的实际目标恰为估计这两个量；
如果真实半局部正迹以紧剩项消费完整首素数型，必须有
`d_m^+ -> -2w2`、`d_m^- -> +2w2`。
仅要全域 QW≥T_2，则至少需要 `limsup d_m^+ <= -2w2`。
上述投影公式和 Neumann relative tail 尚未支付这些条件。

**已支付：**same-source 真正正投影与 compact smooth 正迹、精确 Gram/flux/级数；
真实半局部 truncated Fourier 的 compact/non-HS 边界及严格 contraction。
**未支付：**flux 在固定源 L² 上的 signed kernel、弱零高频主项、连续误差；
Γ剩项与全低域符号、增长 S/支持预算及完整 Weil 正性。

不能凭 ambient truncated Fourier 非 HS 推断 induced source trace 差非紧，
也不能凭其 compact 推断 arch epsilon proof 延续。
下一唯一可执行动作是主代理把这份实际正则性证明与另份来源审查对账，
再决定有无可独立支付 flux 的原始 signed 定理；没有则保留 open 并按 C005 止损。
本审查无待处理进程，不将旧同构或泛范数界计为新的完整研究轮。
