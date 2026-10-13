# C005：半局部 Fourier、物理投影与截断正则性的不同组织逆审

2026-10-13。已恢复 AGENTS、README、STATE、check/show、现 Goal、C005、
D20261013F 及工作树。只写本文件，不改 STATE/cadence，不另计研究轮。
核对对象为531、source-audit.md、projection-transport-audit.md；
采用“原乘子→极分解确认物理 Fourier→标量 Fourier 测试判核→HS夹心判迹”的顺序。

## 1. 一级来源、表示和 Fourier 方向

核读 [Connes–Consani–Moscovici, 2310.18423v2](https://arxiv.org/html/2310.18423v2)
§4.1、4.2、4.5–4.8，特别 (42)、(47)、(57)–(59)、Proposition4.7 与 Theorem4.6。
本地 PDF SHA256 为
`8bc197642ee9ca4f2393b6cbfd3db292be6a315ce76ad61bfb845d9fedb47f2e`，
与来源审查记录一致。HTML 的部分 proposition 标题失真，编号按 PDF 审查定位。
此原文给 Sonin Hilbert 同构及 Fourier 交织，没有本次新正迹／非HS定理。

固定真实单素数 S={∞,p}。将两个物理空间分别通过原件 unitary w/F_mu
识别到同一谱 L²，再识别回实位偶空间。记此真正 unitary 识别为 J_p。
原 (57) 的乘子是 `b(s)=1-p^(-1/2)exp(-is log p)`，
故在共同物理坐标里

    J_p theta_p = B = I-q U_a,
    q=p^(-1/2), a=log p,
    U_a f(x)=p^(-1/2)f(x/p).

(47) 给 `J_p eta_p=(B*)^(-1)`；不是 B^(-1)。
因此 theta*eta=I 的 mixed 配对与原件一致，theta*theta=B*B≠I。
原低 module 支持 |x|<L 经 w 的乘法权运输仍对应实位正半轴(0,L)；
这个支持运输不使用 theta 本身的非酉性。

Proposition4.7 的真实 Fourier 交织给

    F_p = B F B^(-1),          F U_a=U_a* F.

这条等式是在原全部物理空间上，不能只因 Sonin 子空间映射存在而定义一个假 Fourier。
为独立确认它的自伴／酉性，写

    W=B*B=(1+q²)I-q(U_a+U_a*),
    B=V W^(1/2),              V=B W^(-1/2).

B是可逆normal算子，V unitary；W与F交换，故
`F_p=V F V*`。因此 F_p 确为自伴 unitary involution，
不以一般非酉相似“自动保自伴”这一错误理由消费。
此极分解不能把 Sonin 的 BM 改成 VM，因为 W^(1/2) 未证明保持 M。

## 2. 精确算子展开及所有 p、所有 L 的紧性

几何级数 `B^(-1)=sum_(n>=0)q^n U_(na)` 在 operator norm 收敛。
先将 Fourier 移到最右，再合并第一项和偏移尾，得

    F_p=(1-q²)sum_(n>=0)q^n U_(-na)F-q U_a F.

这里正向 dilation 单独留下，符号和系数不可改变。
在 H=L²((0,∞),dx) 的 unitary 偶空间坐标下，F 的核为 `2cos(2pi xy)`。
各项核为

    q^n U_(-na)F : 2 cos(2pi p^n xy),
    -q U_a F    : -(2/p) cos(2pi xy/p).

所以 F_p 的分布核正是

    k_p(x,y)=2[(1-1/p)sum_(n>=0)cos(2pi p^nxy)
                       -(1/p)cos(2pi xy/p)].

核中 p^(n/2) 与 q^n 完全抵消；无遗漏权重、sqrt p 或偶实位因子2。
不能把它读成逐点收敛或 L² 收敛的级数。

取任意固定真实素数 p 和任意固定 L>0，C_L为(0,L)投影，
`K_(p,L)=C_L F_p C_L`。每个有限展开项的双端截断是有光滑有界核的 HS 算子。
截至 n=N 的算子范数尾至多

    (1-q²)q^(N+1)/(1-q)=(1+q)q^(N+1).

故 K_(p,L) 是紧自伴 contraction。尾界不要求 L 的数值下界或上界。
这仅是 operator norm 界，不是 HS／trace norm 界。
结论对每个 p、每个 L 成立，后面的测试 O(1) 可依赖固定 p、L、测试函数；
本定理没有声称 p、L 统一的 HS、gap 或核常数。

## 3. 独立标量 Fourier 组织的 non-HS 证明

给(0,L)²任意非空内部矩形，取非零非负 chi∈Cc∞，紧支于该矩形。
所有坐标都离0有正距离。对 chi 和 chi² 分别定义乘积变量推前密度

    m_chi(z)=integral chi(x,z/x) dx/x,
    m_(chi²)(z)=integral chi(x,z/x)^2 dx/x.

它们都在正 z 上紧支光滑，且总积分分别为 ∫chi、∫chi²。
采用 scalar Fourier `mhat(omega)=integral m(z)exp(-2pi i omega z)dz`。
令 `c_n=cos(2pi p^nxy)`，则任意 m≠n 有精确关系

    integral chi c_m c_n
       = (1/2) Re[mhat_chi(p^m-p^n)+mhat_chi(p^m+p^n)].

由于 scalar Fourier 任意阶快速下降，且
`|p^m-p^n| >= (1-p^(-1))p^max(m,n)`，这些非对角积分的绝对双和有限。
最大指标为 j 的配对数仅 O(j)，故一阶下降已经由 `sum j p^(-j)<∞` 支付；
无需选择依赖 N 的积分常数。
对角项为

    integral chi c_n² = (1/2)integral chi
                         +(1/2)Re mhat_chi(2p^n),

其误差总和有限。低频修正 cos(2pi xy/p) 与 c_n 的交叉和也绝对可和，
因为 `|p^n-p^(-1)| >= (1-p^(-1))p^n`，包括 n=0。

定义合法测试 `phi_N=chi sum_(n=0)^N c_n`。对 chi² 重复上述公式给

    ||phi_N||_2²=(N+1)/2 · integral chi²+O(1).

对 k_p 配对，全部非对角无限／有限双和只是统一 O(1)，对角贡献给

    <k_p,phi_N>=(1-1/p)(N+1)integral chi+O(1).

leading coefficient严格正；没有把单个cos²的1/2遗漏到核因子2之外。
每个 phi_N 是固定内部支撑的 smooth 测试；对该测试核级数绝对分布收敛。
算子范数极限的 Schwartz 分布核与此级数核一致：先对 smooth tensor 测试核验，
再利用测试空间连续性／smooth 核的有限秩分解延拓，不从点值求和辨认算子。

若该内部核是 L²，Cauchy–Schwarz 将后一配对约束为 O(sqrt(N+1))，
与准确线性主项矛盾。因此 k_p 在每个这种内部矩形都不是 L²。
HS 算子在(0,L)²上必有唯一 L² 积分核，其分布限制应等于 k_p；
故 K_(p,L) 不属 HS。该反证没有利用 x=0、cutoff边界或非光滑测试，
也没有把“不绝对点值收敛”当 non-HS 的证明。

## 4. 严格 contraction、谱系数和成长 cutoff 的量词

从 W与F交换另得

    B* F_p = F B*,
    eta=(B*)^(-1)=sum_(n>=0)q^n U_(-na).

B*=I-qU_(-a) 及其 inverse 都保持低支持 C_LH，因为 U_(-na) 将其压缩到(0,L/p^n)。
若非零 f 及 F_p f 同时低支持，则 g=B*f 非零，
而 g 与 Fg=B*F_p f 都低支持。g是紧支L²，因而L¹；其通常偶 Fourier
有 entire 延拓且在外侧开实区间为零，解析唯一性给g=0，矛盾。

K_(p,L) 若范数1，紧性保证存在低支持unit向量达到该范数。
unitary F_p 与投影范数等号使 F_p f 也低支持，正好违反上述结论。
所以 `||K_(p,L)||<1`，但没有未经计算的数值gap。
紧自伴谱定理按 multiplicity 计其特征值 nu_j，non-HS 给

    sum_j |nu_j|²=∞,
    sum_j |nu_j|=∞,
    sum_j |nu_j|/sqrt(1-nu_j²)=∞.

最后一步只用 |nu_j|≤1 和每个分母在(0,1]。
故实位 epsilon 连续性证明所用的绝对可和 prolate 系数前件，
在这个真实半局部截断对象上实际失败；严格gap不能恢复可和性。
但未证明某个半局部 epsilon 系数公式存在，更不证明 epsilon_p 不连续。
额外有符号抵消或其他 trace regularization 仍可能，不能从谱绝对和失败排除它们。

主代理提出的同轮附属成长结论也成立：对固定 p，
`||K_(p,L)||` 随 L 不减，因为自伴压缩范数等于低支持unit向量的绝对Rayleigh上确界，
允许的向量空间随L嵌套。且 C_L→I 强，故对任意unit f，
`C_LF_pC_L f→F_p f`、其范数趋1。于是

    lim_(L→∞)||K_(p,L)||=1.

所以每个有限 L 的严格gap并无增长L的统一正gap。
这个 L 是 ambient module/Fourier cutoff，不是当前冻结的 source 支持参数 lambda_source。
此附属压缩事实不提供 source flux、低谱排序或新的完整正性。

## 5. 正投影、同源 trace 与 flux 的独立 HS 夹心核验

固定 Sonin cutoff1，P为实位正交投影，M=RanP。
原稳定性给真正半局部Sonin在共同物理空间恰为BM。
B可逆且 `(1-q)||f||≤||Bf||≤(1+q)||f||`，所以BM闭。
令 `G=PWP|_M`，则 `(1-q)²I≤G≤(1+q)²I`。
`V_M=B|_M G^(-1/2)` 满足 V_M*V_M=I_M，其 range为BM；
因此实际正交投影是

    P_p=B P G^(-1) P B*.

所有 inverse只在M定义；环境式由P嵌入。它不是BPB*或BPB^(-1)。

对原 smooth compact 同源 h，`A=integral h(t)U_t dt` 有界且与B、W交换。
旧实位正trace使Y=AP为HS。于是 AV_M=BY G^(-1/2)为HS，
真实半局部正迹为其平方范数；任意两个源交叉由HS乘积为TC。
这不要求A或dilation保持M，也不声称所有 source L² 均有有限trace。

将全部循环trace只在这些TC组织里进行，得

    T_p=Tr_M[G^(-1)Y*WY]=Tr_M[G^(-1)P W Z P],
    T_inf=Tr_M[Y*Y]=Tr_M[P Z P],        Z=A*A.

这里 Y*WY 是TC；PWPZP=G(PZP)也是TC。
二者之差作为完整块是 `PW(I-P)ZP`，故其trace合法：

    T_p-T_inf=Tr_M[G^(-1)PW(I-P)ZP]
             =-q Tr_M[G^(-1)P(U_a+U_a*)(I-P)ZP].

scalar identity部分恰因P(I-P)=0消去。无需断言每个未经HS夹心的 ambient 块TC。
交叉Gram按同一HS夹心极化；main note的符号与来源审查一致。

粗范数界以及 Neumann relative trace tail亦正确。
写alpha=1+q²、C=P(U_a+U_a*)P|M，||C||≤2，
`G^(-1)=alpha^(-1)sum_(m>=0)(qC/alpha)^m`，
rho=2q/alpha<1，故截至N的inverse误差≤`rho^(N+1)/[alpha(1-rho)]`。
以Y*WY夹心，trace余项≤
`(1+q)²rho^(N+1)T_inf/[alpha(1-rho)]`，
与两份审查一致；p=2时rho=2sqrt2/3。
由于 `alpha(1-rho)=(1-q)²`，该系数就是粗transport比值κ²。
这份费用仍随原Gamma/Sonin能量，不能误称固定source L²质量费、紧误差或弱零趋零证书。

## 6. 与实际 prime、基线及宏观瓶颈的关系

冻结p=2两patch中，完整pole与其他primepower均严格零。
真实已付恒等式仅是

    QW-T_2 = -E_inf-w2 Swap-(T_2-T_inf),    w2=log2/sqrt2.

若欲取得 C004 所需的紧剩项桥，必须实际证明最后 flux 在两个弱零组合上
分别趋 -2w2、+2w2；只求全域 QW≥T2 的必要条件更弱而仍未付。
当前正投影／正trace／non-HS theorem 均没有付这些量。
不得从 ambient K_(p,L) non-HS 推断 source E2 或 T2−Tinf 非紧，
也不得从其 compact 推断实位 epsilon 的绝对收敛证明延续。

基线511已给真实有限S共同 Fourier及Euler相位；本次不将 B/F_p 相位重记新。
514的对象是有 smooth源卷积的单prime边界 `[Pi,V_p]A V_p*`，
其HS费用和全素数绝对trace尾与本次无source平滑的 `C_LF_pC_L`不同。
本次 every-p/every-L ambient cutoff non-HS、strictgap和真实投影trace消费
没有在这两篇基线中出现，也不与其TC/HS结论冲突。
这只是相对已核基线的非重复判断，不认证世界优先权或外部同行评议。

审查判定：531目前的主要候选及两份审查在常数、表示方向、域和全参数量词上通过。
新接口是完整物理正交化后的有限正trace／flux；新的严格regularity断点
阻止免费照搬实位快速谱和绝对prolate误差证明。
完整signed联合正性、真正最低态／prolate与增长支持费用仍未付，Goal不应据此complete。
停止／重准入条件与531一致：必须直接支付实际signed flux或可验证source误差，
不能以normtransport、固定gap或新增条件名晋级。
唯一下一动作是主代理消费本限定逆审并继续C005最后一轮的真实通量估计。
本审查无待处理下载／计算进程，不修改计数。
