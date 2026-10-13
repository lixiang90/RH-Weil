# C005：实际 Sonin Mellin 密度的首素数主项独立推导

2026-10-14（客户端日期）；工作目录按合同保留2026-10-13。
恢复 AGENTS、README、STATE、check/show、Goal、C005、D20261013G 与531。
起始 HEAD `6968df3`。本文件只写独立证明，不改 STATE/cadence、不单独计轮。

## 结论与尚未支付的符号

对真实 p=2（以下同时对任何固定素数p），同源正交 Sonin 迹的密度满足

    rho_p(s)-rho_inf(s)
       =-(log p)/pi sum_{n>=1}p^(-n/2) cos(n s log p)+o(1),
       |s| -> infinity.

这里不是把实际P替换成定义的窗口：下文从实际 cosine Fourier 的 Mellin 相位、
实际两 cutoff 投影及真实压缩 Gram 逆给出统一误差。
在任何固定有限源支持U上，`T_p-T_inf` 等于实际p及其全部幂的 signed prime 型
加一个源 L² 紧二次型。冻结 C004 两 patch 因只含p=2，得到

    QW-T_2 = compact quadratic form,
    (T_2-T_inf)(U(h_R,+h_R)) -> -2 log2/sqrt2,
    (T_2-T_inf)(U(h_R,-h_R)) -> +2 log2/sqrt2.

这是首素数非紧账本的独立支付；没有证明剩余紧型非负，
更没有证明 QW≥T_2、完整 Weil 正性、最低态或成长支持预算。

## 真实对象及归一化

共同物理空间用 H=L²((0,infinity),dx)，实 cosine Fourier 核为2cos(2pi xy)。
经 unitary `f(x) -> e^(y/2)f(e^y)` 到 L²(R,dy)，记实际 Fourier 为 F。
源 scaling U_t 成为 shift `f(y)->f(y-t)`；频率 Fourier 用单位归一化。
原文真实 theta_p 对应 `B=I-qU_a`，a=log p、q=p^(-1/2)。
531 已支付真正半局部投影

    Q_p=B P G^(-1)P B*,
    G=(1+q²)I-q C, C=P(U_a+U_a*)P|RanP.

P 为实际实位 Sonin cutoff1正交投影。
源正迹 `T_p(g)=||A_g Q_p||_HS²`，A_g 的频率乘子为
`g_hat(s)=integral g(t)exp(-ist)dt`（此处没有额外1/sqrt(2pi)）。

令k_s为 RanP 中裸 unitary Mellin 求值的 Riesz 向量：
`(U_inf f)(s)=<k_s,f>`。因此

    rho_inf(s)=||k_s||²,
    rho_p(s)=|1-q exp(-ias)|² <k_s,G^(-1)k_s>,
    T_p(g)=integral |g_hat(s)|² rho_p(s)ds.

最后一个公式由任意 Sonin ONB 的 Tonelli 求和给出；不把裸求值密度与
Gamma-completed de Branges 求值混同。整个证明保持 actual K=2theta'。

## 1. 实际 Fourier 对任何有限 Mellin 区间的统一运输

实际 F 的频率表达是

    (F f)_hat(s)=m(s) f_hat(-s),
    m(s)=pi^(is) Gamma(1/4-is/2)/Gamma(1/4+is/2).

取连续实相位m=exp(i phi)，则
`phi'(s)=-K(s)`，`K(s)=2theta'(s)`为偶函数，
`K(R)=log(R/(2pi))+O(R^(-2))`，`K'(s)=O(1/|s|)`。
这些由真实 Gamma 比及标准 Stirling/psi 展开直接成立，不涉及ζ零点。

固定R大且正，记 `T=K(R)>0`，`p_R(y)=exp(iRy)`。
对**任意有限区间J**，有

    ||F(p_R 1_J)-m(-R)p_-R 1_(T-J)||₂ <= c R^(-1/4).
                                                        (A)

常数c不依赖J长度、位置或端点。证明全部在 L² 内：
`|1_J_hat(xi)| <= c/|xi|`，对xi≠0统一有效。
以s=-R+xi为中心，|xi|≤sqrt R时，Taylor 余项给

    |m(-R+xi)-m(-R)exp(-iTxi)| <= c xi²/R.

相位乘子有模1，外区差至多2。因此 Plancherel 误差平方不超过

    c integral_(|xi|<=sqrt R) xi²/R² dxi
      +c integral_(|xi|>sqrt R) xi^(-2)dxi <= c R^(-1/2).

频率线性相位精确对应反射区间T-J，常数为m(-R)，没有剩余R T相位。
负载频同理；因K偶，反射中心仍T，常数改为m(R)。
这里p_R仅与有限J相乘时使用，未把全域 plane wave 当 L² 向量。

## 2. 实际 Sonin 投影的统一 clipping 估计

记 L=1_(y<0)、H=I-L、C_0=LFL。
实位实际 cutoff满足 `||C_0||<1`，来自 compact finite cosine Fourier
及紧支/Fourier紧支不确定性。设 R_0=(I-C_0²)^(-1)。
实际 Sonin 投影的合法 L² 公式为

    P=H-H F L R_0 L F H.                                 (B)

这是 RanH 内去掉HF RanL的正交投影：
`(HFL)*(HFL)=I_L-C_0²`；不以投影乘积假称正交。

由(A)、(B)，对任何有限J，

    ||P(p_R1_J)-p_R1_(J intersection [0,T])||₂
       <= c_P R^(-1/4).                                 (C)

常数仍与J无关。完整证明如下。
H先将J换成J_+=J∩(0,infinity)。令r=LFH(p_R1_J)。
(A)给r与 `r_0=m(-R)p_-R1_((T-J_+) intersection (-infinity,0))`
的距离至多epsilon=c R^(-1/4)。对r_0再用(A)，其反射区间在(T,infinity)，
所以 `||C_0 r_0|| <= epsilon`，`||C_0 r|| <=2epsilon`。
于是

    ||(R_0-I)r||=||R_0 C_0²r|| <=2||R_0||||C_0||epsilon.

而F r_0与 `p_R1_(J_+ intersection (T,infinity))` 的距离至多epsilon，
因为m(R)m(-R)=1。代入(B)得到(C)，可取
`c_P=(2+2||R_0||||C_0||)c`。
这一步使用实际P和实际two-cutoff resolvent，不只做单 boundary模型。

## 3. 裸 Mellin 求值向量由有限 L² 测试恢复

取J_M=[-M,M]、M>T，(C)给

    P(p_R1_JM)/sqrt(2pi)
        =w_R+error_M,
    w_R=p_R1_[0,T]/sqrt(2pi),
    ||error_M|| <= c_P R^(-1/4)/sqrt(2pi).

这族在实际Hilbert空间有界。其弱极限恰为k_R；因此

    ||k_R-w_R|| <= c_P R^(-1/4)/sqrt(2pi).                 (D)

为避免formal Mellin plane遗漏域，这里说明唯一性。
稠密核心为 `P C_c^infty((0,infinity))` 的物理向量。
对这样的ψ，(B)中低支持 resolvent 向量光滑至端点：
`R_0r=r+C_0²R_0r`，C_0是光滑有限 cosine 核。
对其有限区间 Fourier 分部积分，Pψ在物理x趋∞为O(1/x)，且x<1为0。
故裸 Mellin 积分对每个Pψ绝对收敛。
当M趋∞，上述有限 L² 向量与Pψ的配对收敛到其真实 Mellin 求值。
任何弱子极限都给同一稠密核心上的求值；连续 Riesz 向量唯一。
这也与原件 Sonin/de Branges 的连续求值一致。
弱下半连续性给(D)，没有对全域 plane直接应用P。

## 4. 完整压缩 Gram 逆与长区间模型的误差

记Π_T=1_[0,T]，V_a=U_a+U_a*，
`C=P V_a P`（在ambient延伸）、`C_T=Π_T V_a Π_T`。
两者范数均≤2。令alpha=1+q²、r=q/alpha、rho=2r<1。
实际与窗口 Gram 逆都具有算子范数收敛级数

    G^(-1)k_R=alpha^(-1)sum_(j>=0) r^j C^j k_R,
    G_T^(-1)w_R=alpha^(-1)sum_(j>=0) r^j C_T^j w_R.

C_T^j w_R是至多2^j个“同carrier、有限区间”的组合；
所有移位相位绝对值1。由(C)，在每一组合上
`(P-Π_T)`及其移位后的误差至多const·2^j R^(-1/4)。
具体用

    P V_a P e-Π_T V_a Π_T e
      =P V_a(P-Π_T)e+(P-Π_T)V_aΠ_T e

逐项核准。递推结合(D)得

    ||C^j k_R-C_T^j w_R|| <= c(j+1)2^j R^(-1/4).

所以完整级数的差满足

    ||G^(-1)k_R-G_T^(-1)w_R||
       <= c_q R^(-1/4) sum_(j>=0)(j+1)rho^j
       =O_q(R^(-1/4)).                                  (E)

不交换一个未控的R极限和relativeGamma尾；统一窗口误差使全部words都可求和。
由||w_R||=sqrt(T/(2pi))、G逆有界，(D)、(E)给实际密度与窗口密度之差
`O_q(R^(-1/4)sqrt(log R))`。
同样 `rho_inf(R)=T/(2pi)+O(R^(-1/4)sqrt(log R))`。

## 5. 长区间的B范围投影密度精确计算

这一节模型误差已由前四节支付。L²(log time)分解为
θ∈[0,a)与格点θ+ja的 direct integral；[0,T]在每fiber有n=n(θ)个连续格点。
B将标准基e_j送到 `e_j-qe_(j+1)`。B范围在n+1个格点上的正交补
恰由 `v_j=q^(n-j)`，j=0,...,n，生成。
因此该fiber的投影 Mellin 密度减去原n个点的密度，恰为

    (1/(2pi))[1-|sum_(k=0)^n q^k exp(-iRa k)|²
                         /sum_(k=0)^n q^(2k)].

当T趋∞，所有n(θ)至少floor(T/a)，几何尾统一给

    rho_p,model(R)-T/(2pi)
      =a/(2pi)[1-(1-q²)/|1-q exp(-iRa)|²]
          +O_q(q^(floor(T/a))).

Poisson核恒等式

    (1-q²)/|1-q exp(-iRa)|²=1+2sum_(n>=1)q^n cos(nRa)

由绝对几何级数成立。结合(E)，得到真实主项及一个明确趋零误差：

    rho_p(R)-rho_inf(R)
      =-a/pi sum_(n>=1)q^n cos(nRa)
          +O_q(R^(-1/4)sqrt(log R)).                      (F)

q^(floor(T/a))=O_q(R^(-1/2))已吸入较大误差。
物理P、B都是实算子，负载频密度与正载频相同；故(F)适用于|R|趋∞。
它不是只有第一个prime的猜测：所有p幂及原权同时出现。

## 6. 源 L² 的真正 compact remainder 与冻结消费

定义真实剩余乘子

    r_p(s)=2pi[rho_p(s)-rho_inf(s)]
                  +2a sum_(n>=1)q^n cos(nas).

(F)给r_p(s)趋0。原Sonin连续求值及bounded可逆G给密度局部有界、连续；
故r_p为有界连续趋零乘子。
对任何有限测度的固定源支持U，压缩算子
`1_U F_mu^(-1) M_(r_p) F_mu 1_U`是compact：
频率截断到[-N,N]时核有界、在U×U为HS；
截断余项的算子范数≤sup_(|s|>N)|r_p(s)|趋0。

因此同源型有准确分解

    T_p-T_inf
      =-a sum_(n>=1)q^n [source shift_(na)+source shift_(-na)]
         +compact_U.

这里source Fourier的Parseval因子为1/(2pi)，所以实际prime原权就是
`a q^n`，没有再多或少一个2。
冻结源U的跨度小于log3，源内无prime，onlyp2交叉为
`-w2Swap`，pole为0；实位误差E_inf在该U也是compact。
于是完整真实账本确实变为

    T_2-T_inf=-w2Swap+compact_U,
    QW-T_2=compact_U.

合法弱零h_R族使全部compact二次型趋0，得到本文件开头的d_R±极限。
这支付C005要求的非紧首素数主项及源 L² 紧剩余，
不是relativeGamma界或有限数值正样本。

## 宏观范围及下一动作

新增独立分析是实际Mellin sharp-window运输、actualP uniform clipping、
完整G逆误差及真实首素数/全部p幂主项。531的非HS断点仍成立；
本路线通过Gamma phase和actual投影的有符号分析绕过绝对prolate级数，
不无声复活已停止的绝对系数证明。

未支付：compact remainder的全低域符号或可消费质量界、QW≥T_2、
含outside-p素数的更大源域、成长S/支持费用及真正最低态/prolate桥。
固定有限U上compact不意味着全增长U统一compact或符号；
也不证明所有半局部epsilon连续或所有truncatedF变HS。
长期Goal不能仅凭此局部桥完成。

唯一下一动作：主代理以不同组织方式核(A)相位/归一化、(C)实际projection、
(D)真实evaluation域与(E)完整逆级数，再消费(F)及冻结compact结论；
之后要研究的是新已定位的compact signed low remainder，而非继续重算首素数。
本文件没有待处理计算/下载进程；重大结论在独立逆审前不升级最终笔记。
