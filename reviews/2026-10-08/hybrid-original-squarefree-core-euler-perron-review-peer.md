# 原平方自由核心 Euler–Perron 新源：不同作者全文独审

2026-10-08，checkpoint_audit。审查作者与研究源作者 perron_reviewer 不同。
只新增本审查文件；原研究源及既有依赖保持冻结。

**结论：限定范围 PASS。** 全文读取395行新源，独立逐式重推得到：
原完整 proper-prime-power 外因子，以及 genuine-prime 外因子的
全部 2≤r(k)≤V² 子族，各自可以用 Euler 身份和正高度 Perron
直接支付。完整 P_H−R_sf 的 normalized fourth 为
O(X^(1/2+ε))，这一误差界无条件；接受476原合同之后，完整第四矩
加性传递的指数为37/56。没有发现阻断这两个结论的数学缺口。

## 1. 精确绑定与阅读范围

审查对象为
[395行新源](hybrid-original-squarefree-core-euler-perron-research-perron.md)，
canonical UTF-8 LF SHA256：
2f25a678b0c38c95a40469c41a757506c6f1fe64343bed327c7effe298e980c0。
本轮实读395行、16715 LF字节，未以摘要、有限样本或 root 的 PASS
代替独立阅读。源内行号均指此固定版本。
亦 FULL READ 最终488全部114行、5235 LF字节，绑定下表最终版本。

已在连续研究轮全文读取下列依赖，本轮重读了所需推导；
特别重新全文读取324行原 Vaughan 源、476全部96行，并逐段核读
505源的 ζ 四矩/Cauchy、Euler无限尾及 Type I 完整付款：

| 实际依赖 | canonical LF SHA256 |
| --- | --- |
| [505行长因子源](hybrid-original-extended-inner-zeta-fourth-perron-research-perron.md) | 54d39f22b370be40a780fac6fe80968e24c014fc48d1156ab87248d5310a2549 |
| [486](../../notes/486-original-padded-perron-fourth-mean-remainder.md) | 5e98058d6d47545aedb98b6e70f66f4e11a904b623351903e3846e01bbe7eaf7 |
| [401行平方丰满尾源](hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md) | 66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab |
| [481](../../notes/481-original-type-ii-squarefull-tail-and-optimized-moment-transfer.md) | 4ce3ea2ac087d734142c8788607c1c54fc6887bcf535c806c88097447afdc63e |
| [324行原 Vaughan 源](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 |
| [实际最大 prefix 源](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 |
| [476](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |
| [488最终汇总](../../notes/488-original-squarefree-core-and-half-power-error.md) | 0e2f1cf88d4de1a804c1b9e6ce21febe85c8c5856726fd66c2d778cce29b5825 |
| [451原边界及全部前件](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |

本新误差证明没有消费短 Möbius 的无零输入，source表中该输入仅用于
既有路线背景；不能把它误记成无条件误差的前件。
本审查为无限解析推导审查。有限系数/有理数检查器的执行不是下列
Perron、平均值及∞尾的证明证据。

## 2. 原系数分区与 Euler 恒等式

核源69—117行。原 C4 确实保留 -Λ(m)b_V(k)、m>U、k>V、
共同 Y<mk≤X。r(k)=k/∏_(v_p(k)=1)p 是真正 squarefull 部分；
它与 odd-exponent kernel 不同。s squarefree、r squarefull、
(s,r)=1 是唯一分解；m 可以与 s 或 r 共享素因子。

对 fixed squarefull r，将 d|sr、d≤V 的 Möbius divisor 唯一写为
d=ae，其中 e|rad(r)、a|s、(a,r)=1，ae≤V。
由于非 squarefree d 的 μ(d)=0，a、e 的 squarefree 条件准确。
写 s=aℓ 时，ℓ squarefree 且 (ℓ,ar)=1。绝对初线上的完整 Euler
乘积给

\[
 \sum_{\ell\ {\rm sf},(\ell,ar)=1}\ell^{-w}
   =\frac{\zeta(w)}{\zeta(2w)}
       \prod_{p\mid ar}(1+p^{-w})^{-1}.
\]

所以源(6)—(7)准确包含真实 ae≤V，不能换成两个独立 cutoffs。
对 r≥2，k=sr 永不等于1，而 2≤k≤V 时
b_V(k)=Σ_(d|k)μ(d)=0。因此
B_≥2=ζ C_≥2/ζ(2w) 的 k>V cut 精确无需 -1。
相反 r=1 仍有 k=1 项，故 B_sf=ζ F_(V,1)/ζ(2w)−1。
这一差异是本次 cancellation 的实际算术原因。

核源120—152行。对 Re w≥1/2+c，有限 local factors 以
∏_(p|n)(1−p^(-1/2))^(-1)≪_ηn^η 控制。
每个 r 的 e 数≤τ(r)，a 总质量≤V^(1/2+η)，故
F_(V,r)≪r^ητ(r)V^(1/2+η)。squarefull 计数来自唯一 a²b³ 表示，
每个 r dyad 的 Σr^(-1/2)≪1。因 H≤X，先给定最终 ε，再分配
divisor 与 local factor 的 η，完整 C_≥2≪√V X^ε L^C。
这是全部 r 和 a,e 的实际绝对界，对虚部统一。
有限 denominators 的零点实部是0，所以在本次轮廓内解析。

## 3. 两个完整子族的消极点身份

核源154—199行。真正 prime 大因子与 proper powers 的定义不重叠：

\[
 A_U=-\zeta'/\zeta-Q_{\rm pp}-F_U^{\rm prime},\quad
 Q_{>U}=\sum_{p^j>U,j\ge2}(\log p)p^{-jw}.
\]

F_U^{prime} 只扣 m≤U 的 genuine primes；Q_pp 扣全部 proper
powers，从而 A_U 准确剩全部 genuine prime m>U。
Q_>U 则给全部 m>U 的 proper powers，未将 p>U 误作 p^j>U。
故原 -A_U B_≥2 精确等于
[ζ′+(Q_pp+F_U^{prime})ζ]C_≥2/(a_LLζ(2w))。
即使 ζ 零点重数>1，右边仍解析，未遗漏其留数。

全 k>V 的真实系列是 ζG_V−1：k=1 的扣除保留，2≤k≤V 的
系数准确为0。因此原 proper-power 全子族正是
-Q_>U(ζG_V−1)/(a_LL)。两式首先在 Re w>1 是实际系数身份，
之后才续延。没有给 m,k 新增互素条件；m|r 或 m|s 的项均在。

Q_pp 在每个 Re w>1/2 局部一致绝对收敛。逐 prime-power geometric
sum 后放大至整数，所用 σ≥1/2+c 上 Q_pp≪c^(-2)。
同样 |ζ(2w)^(-1)|≤ζ(2σ)≪c^(-1)，
|F_U^{prime}|≪√U L，|G_V|≪√V。这些输入不需要零点前件。

## 4. 无限初线、半整数端点和完整远尾

核源201—245行。s0=1/2−it，κ=1/2+c，初线
Re(s0+z)=1+c 真正绝对收敛。x^sharp=floor X+1/2、
y^sharp=floor Y+1/2 精确保留两套整数集合。原 h_n 系数
满足 |h_n|≪log(2n)τ3(n)/L；这里允许全部 n≥1。

近端 x/2<n<2x 可用 fixed divisor n^η，因为此时 n≪X。
半整数与整数的距离≥1/2，原 Perron tail 的 harmonic sum 为
O(X^η√x/K·L^C)，K=T/8≍X，两端都≤X^(-1/2+η)L^C。

远端必须保留准确幂：n^(-1/2)(x/n)^κ
=x^κ n^(-1-c)，不是 n^(-3/2-c)。
|log(x/n)|≥log2 后，完整∞尾使用

\[
 \sum_{n\ge1}\tau_3(n)\log(2n)n^{-1-c}
 =-(\zeta^3)'(1+c)+\log2\,\zeta(1+c)^3\ll c^{-4}.
\]

故远尾为 x^κ/K·L^C≪X^(-1/2)L^C。fixed n^η divisor
bound 没有用到∞远端，避免 c<η 的发散错误。
源(21)保持 n>X 的整个初线尾，未把 infinite series 偷换成有限积。

## 5. 真实移线、水平线与统一第四均值

核源247—305行。轮廓左线 z=c，全部 t−Im z∈[T/8,33T/8]。
ζ、ζ′在1的极点位于零高度；原正 guard 排除它。
ζ(2w)^(-1)、Q 的绝对级数、有限 local factors 在所见矩形解析。
z=0 未跨过；源(16)中的 ordinary ζ 零点已经代数取消，
不是依靠 [Rθ] 或免费删除零点留数。

505源 Euler/Abel∞尾证明在 fixed compact σ∈[1/2,5/4]仍成立：
逐 h 的 nonstationary 积分给1/|h|，ψ Fourier 再给1/|h|，
Σh^(-2) 可绝对求和，且 N=floor(10T) 的常数统一。
因此水平线上 ζ≪T^max(1−σ,0)L；半径 c/2 的 Cauchy 给
ζ′≪T^max(1−σ,0)L²，T^(c/2)=O(1)。
乘 Perron kernel X^(σ−1/2)/T 后整个水平线付
X^(-1/2+v+ε)L^C，固定 v<1/4 时是负幂。

第四均值采用已核读的
[Montgomery–Vaughan Vol III Theorem26.23](https://personal.science.psu.edu/rcv4/Vol3/Vol3.pdf)，
印刷143页/PDF151页。取 U0=5T，充分大 X 时
3/(2log X)≤2/log(5T)，故真实 σ=1/2+c 及 c/2 Cauchy 圈
全部在其 uniform 域。所有移位后的正高度仍在(0,5T)。
负虚部由 ζ 的共轭性质准确返回，normalized 时间尺度只变固定常数。
于是 ζ 的 L4 norm≪L，ζ′的 L4 norm≪L²。
没有将 |ζζ′|² 的均值误用作 ζ′的第四矩。

其余因子使用同一实际移位点的上界，得到
||H_≥2||4≪√(UV)X^ε L^C、||H_pp||4≪√V X^ε L^C。
外两 sharp endpoints 共用同一个 ω，kernel 的 L1 质量≪L；
一次 L4 Minkowski 给源(26)的4v及(27)的2v。
任意最终 ε 先分配到 local/divisor、四次幂及日志，量词成立。

## 6. 完整重建 P_H−R_sf 与费用优化

核源327—367行及原 Vaughan 源(8)—(10)。
所有高段 n>Y>U 上有原精确 I2+I3+C4。原 C4 的外 Λ 支撑
精确分成 genuine primes 与 proper powers，genuine-prime 部分
再按 r>H、2≤r≤H、r=1 不交覆盖。这给源(28)，没有双扣。

401源完整 squarefull r>H 尾对 M0=U 仍统一：
c_r(n) 的上界只需 τ(r)τ3(n)，与 M0 大小无关，
共同 Y/r<n≤X/r 是两个 moving prefix 的差。包括 s=1，
包括 m与r共享prime，仍付 X^ε(1+X/H²)。
505源的完整 Type I 4v 费用可用于当前 v=1/8，
finite padding 的所有额外 n>X 已由该源支付。
低段将实际有限平方作时间 L2，付 X^ε(1+Y²/X)。
Λ scalar 返回 genuine P_H 的 proper powers，即使仅用完整绝对和
Σ_(p^j≤X,j≥2)log p/√(p^j)≪L²，也只有 polylog。

因此对同一完整 E_sf=P_H−R_sf，费用表确为
max{2y−1,4v,2v,1−4v,0}。v=1/8、y=3/4 时为
(1/2,1/2,1/4,1/2,0)。V≥X^(1/8)/2、H=V²≥X^(1/4)/4
支付 tail floors；V≤X^(1/8) 支付正向 local factors。
max{4v,1−4v}≥1/2 是这张费用表内的下限。
这些付款自身无条件，未将旧 signed 余项范数移到新的子族。

## 7. 完整传递、保留留数和完成范围

核源369—395行。只有加性第四矩传递接受476原 [R_7/8] 及
同一 P_H 的完整5/7增长。Minkowski 先给 R_sf 同幂上界，
再以 ||E||4(||P_H||4+||R_sf||4)^3 控制完整两矩差。
指数 (3·5/7+1/2)/4=37/56；距5/7为3/56。
9/17−1/2=1/34，159/238−37/56=1/136，均准确。
结论为加性 upper，未推出未知主项的相对渐近。

在 Re ρ>1/2 的 ordinary ζ 零点上，F_(V,1)、1/ζ(2w)解析，
B_sf(ρ)=−1，A_U 留数为−m_ρ。因此未归一化 -A_U B_sf
仍有原留数−m_ρ，两端 Perron kernel 和 normalizer 保留。
本次确实支付了全部 r≥2 子域，尚未支付原 prime/squarefree
核心的完整 joint mixed4，也未改变整个 P_H 的5/7基线。

审查通过的范围是原 scalar、positive J_T、sharp product cuts、
真实 Möbius divisor 系数和全部 genuine/proper masks 下的
无条件完整误差1/2，以及476前件下的完整传递37/56。
无限解析的证据是上述推导；有限算术一致性只能另作有限检查。
没有新的常数中心第四矩、实际零点比例、κ、无零边界或纪录论文认证。

## 8. 488汇总与θ*代数应用的独立核对

最终488的函数、参数、负号、complete-error表、ordinary ζ 极点
范围与395源逐项相符。其51行 local C 定义的排版损坏已由root
修复为完整 squarefull 条件，最终版本没有额外控制字符。
本审查范围包含其无条件1/2和条件37/56总结。

488的106—109行仅在接受451既有全部前件后作代数应用。
以451的严格 e 区间和 θ*=11/12−e*/4，独立 Fraction 算得

\[
 \theta_L=\frac{262487105826029}{300000000000000},\qquad
 \theta_H=\frac{1049948423304119}{1200000000000000},
 \quad\theta_L<\theta_*<\theta_H.
\]

B_I(t)=4t−3+3(1−t)/(2t) 在此区间递增；
γ_half(t)=(3B_I(t)+1/2)/4 也严格递增。直接 exact Fraction
比较两端给
0.6606485022147674<γ_half(θ_L)<γ_half(θ_H)<0.6606485022147714。
该只读内存计算 exit0，同时重算1/2、37/56、1/34、1/136。
此处只认证显示有理区间的代数消费，没有重新认证451全部外部
分析前件，也没有降低其中任一引用依赖或产生新边界。
