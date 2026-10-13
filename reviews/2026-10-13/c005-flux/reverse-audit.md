# C005 第二轮：完整 Sonin 密度与首素数紧余项的不同组织逆审

核读日期2026-10-14（Asia/Shanghai）；目录沿用父任务指定日期。
恢复 AGENTS、README、STATE、check/show、Goal、C005、D20261013G 和实际工作树。
只写本文件，不改 STATE/cadence，不新增研究轮。核对 trace-source-audit.md
与 direct-symbol-audit.md；先审实际投影与求值向量，再审完整逆算子及有限链，
最后才消费单边界／overlap账本。没有用ζ零点或有限数值样本。

## 1. 实际相位、任意有限区间与半线投影

实际 unitary log Fourier 的相位为

    (Ff)^hat(s)=m(s) fhat(-s),
    m(s)=pi^(is)Gamma(1/4-is/2)/Gamma(1/4+is/2),
    (log m)'=-iK(s), K=2theta', K(s)=K(-s).

对R大、T=K(R)>0，原Gamma展开给 `K(R)=log(R/(2pi))+O(R^-2)`，
在|-R+xi|≥R/2上 `|K'|≤const/R`。
任意有限区间J的 unitary Fourier满足 `|1_Jhat(xi)|≤const/|xi|`，
这个界确实与J的长度和位置无关。故将频率分为|xi|≤sqrtR和外侧，
线性相位余项分别用 const xi²/R 与2控制，误差平方为

    O(integral_0^sqrtR xi²/R² dxi)+O(integral_sqrtR^infinity xi^-2 dxi)
       =O(R^-1/2).

这认证A的统一 `O(R^-1/4)` L²运输。频率中心在-R，包络相位
`m(-R)exp(-iT xi)`对应 `m(-R)exp(-iRy)1_(T-J)(y)`。
没有额外exp(iRT)常数；负载频运输与其复合的常数为m(R)m(-R)=1。
不能只证明固定J，再把常数消费到任意移位及Neumann words。

令L为log低半线投影，H=I-L，C0=LFL，R0=(I-C0²)^-1。
实际Sonin空间是 RanH∩ker(LF)，而X=HFL从低空间到RanH有
`X*X=I_L-C0²`。实位有限cosine cutoff的compact与严格norm<1
使X range闭，真实正交投影准确为

    P=H-H F L R0 L F H.

不是一个投影乘积，也没有未付的半线逆算子。
对carrier_J，H先取J+=J∩(0,infinity)。运输所得低部分r0的第二次F运输
落在 `J+∩(T,infinity)`，因此 `||C0 r0||≤epsilon`。
实际r=LFH carrier满足 `||r-r0||≤epsilon`、`||C0r||≤2epsilon`，
进而 `||(R0-I)r||≤2||R0||||C0||epsilon`。
代回精确P式即可得任意J的统一clipping：

    ||P(carrier_J)-carrier_(J∩[0,T])||≤const_P R^-1/4.

该证明支付的是完整两cutoff Sonin投影，不是单边界近似。

## 2. 求值向量的弱极限、密度归一化及有限频段

裸 unitary Mellin求值使用 `1/sqrt(2pi)`；源群积分A_g的乘子
`ghat(s)=integral g(t)exp(-ist)dt`不含该因子。
对M>T，真实 `P[exp(iRy)1_[-M,M]]/sqrt(2pi)` 在L²中有界，
且与 `w_R=exp(iRy)1_[0,T]/sqrt(2pi)` 的距离至多const R^-1/4。
弱极限不能仅凭有界性任意命名为k_R，必须核实同一裸求值。

其可用稠密核心为物理坐标的 `P Cc∞((0,infinity))`。
给物理紧支smooth ψ，低向量r=LFHψ在[0,1]光滑到端点；
`R0r=r+C0²R0r`也光滑，因为C0是有限cosine光滑核。
把F作用于这个低向量，一次分部积分给物理x→infinity的O(1/x)尾。
Pψ在x<1为0，故log坐标包络在y→infinity为O(exp(-y/2))，属于L¹。
这允许其裸Mellin积分绝对取值，且有限[-M,M]配对趋向该真实值。
核心稠密，因为P为有界正交投影、物理Cc∞在ambient L²稠密。
因此每个弱子极限都在同一稠密核心给同一求值，极限唯一，确为Riesz向量k_R。
弱下半连续性给 `||k_R-w_R||≤const R^-1/4`，不曾对全域plane wave直接应用P。

有限频段的局部有界／连续性还需独立依据，不能仅用高频式或弱连续性推出。
重新核 [CCM v2 §4.8](https://arxiv.org/html/2310.18423v2)：
(60)–(61)将实位Sonin接到completed Mellin de Branges空间，
§4.8.3的求值公理是每个复点的连续求值。
这给实际物理范数中的局部统一有界求值：对每个compact复集合，
每个函数的整函数值有界，uniform boundedness principle使求值算子范数统一有界；
Cauchy估计再给局部算子范数连续性。实轴上的Gamma completion权光滑、非零，
除去它得到裸k_s的范数连续性、有限频段局部有界。
这里不把Gamma-completed kernel的数值对角当作裸密度。

可用Sonin ONB逐项并作Tonelli，得到

    rho_inf(s)=||k_s||²,
    rho_p(s)=|b(s)|² <k_s,G^-1 k_s>,
    T_p(g)=integral |ghat(s)|² rho_p(s)ds,
    b(s)=1-q exp(-ias), a=logp, q=p^-1/2.

第二式来自实际等距运输 `B|RanP G^-1/2`，不能删去G。
归一化因此是 `rho_inf,model=T/(2pi)`；prime密度系数随后为-a/pi。

## 3. 完整压缩 Gram 逆的统一误差

在ambient延拓实际 `C=P(U_a+U_a*)P`，模型
`C_T=Pi_T(U_a+U_a*)Pi_T`；两者范数≤2。
对每个±shift word，模型载波始终是同频率、同绝对幅度的有限区间carrier，
clipping估计对所有这些区间统一成立。
一个长度j word的实际／模型差至多const(j+1)epsilon；
将2^j个words相加得

    ||C^j k_R-C_T^j w_R||≤const(j+1)2^j epsilon.

初始k_R-w_R误差也计入，不是假定两者相等。
令alpha=1+q²、r=q/alpha、rho=2r<1，则实际及模型G逆均在其range上为
`alpha^-1 sum_(j>=0)r^j C^j`。
上述误差乘r^j后由 `sum(j+1)rho^j<infinity` 支付全部级数，给

    ||G^-1 k_R-G_T^-1 w_R||=O_p(R^-1/4).

这是真正完整inverse，不是把未控的relativeGamma截断尾送R→infinity。
由于||w_R||=sqrt(T/(2pi))，实际／模型标量密度的差是
`O_p(R^-1/4 sqrt(logR))`，而不是未经核验的O(epsilon)标量误差。
常数允许依赖固定prime及固定实位cutoff；没有成长S的一致预算。

## 4. 有限链模型的准确边界与全部 primepowers

按y=theta+ja分解，theta∈[0,a)。Pi_T每fiber有n连续格点；B的range
由 `e_j-qe_(j+1)` 张成，在n+1个格点中的正交补满足v_j=qv_(j+1)，
故可取v_j=q^(n-j)，j=0,...,n。这个方向与单个高半线B*模型不同，
不可混用其递增／递减几何向量；二者最终绝对平方相同。

plane evaluation在该fiber的投影密度差确为

    1/(2pi) [1-|sum_(k=0)^n q^k exp(-iRa k)|²/sum_(k=0)^n q^(2k)].

theta总体积分给a因子；n至少floor(T/a)，相位几何尾统一O_p(q^floor(T/a))。
因此

    rho_p,model(R)-T/(2pi)
      =a/(2pi)[1-(1-q²)/|1-q exp(-iRa)|²]+O_p(exp(-T/2))
      =-a/pi sum_(k>=1)q^k cos(kRa)+O_p(R^-1/2).

Poisson级数绝对收敛，n=0的质量项精确抵消。
全部p幂原权a q^k均保留；不是只提取first-prime交叉后猜剩余项。
结合上一节，实际密度差满足

    rho_p(R)-rho_inf(R)
      =-a/pi sum_(k>=1)q^k cos(kRa)
         +O_p(R^-1/4 sqrt(logR))+O_p(R^-1/2).

P与B在log坐标都是实算子，k_-R=conj(k_R)，实际密度是偶函数，
因此同一结论覆盖两端 |R|→infinity。

## 5. 单边界和 overlap 的合法 trace 范围

trace-source-audit 的单边界证明独立核准。
B、B^-1保持高半线，实际F_p=BFB^-1；F共轭将第二高空间的projection差
变成 `P_(B*H+)-P_H+`。fiber上的正交补是
`sqrt(1-q²)q^(j+1), j≥-1`，所以D为额外长度a区间projection减去该fiber等距像projection。
两个source夹心分别positive TC，范数由Poisson核支付，故没有∞−∞。
其trace是

    -a/pi sum_(k>=1)q^k integral |ghat(s)|² cos(kas)ds
       =-a sum_(k>=1)q^k[R_g(ka)+R_g(-ka)].

F共轭只反射源；实偶correlation对保持原数值。
这对冻结实源每个R就精确给∓2w2，但仅是单边界账本。

完整Sonin差还有真实overlap `R_p-R_inf`。
`R_v=S_v+C+F_vCF_v-I`在每个generic角平面有特征值±nu_j；
实位R_inf ambient TC，半局部R_p ambient compact但nonHS。
由531分别合法的Sonin source TC及上述单边界TC可推出整体source overlap TC，
但不能从ambient compact直接推出它的trace趋零。
source-audit 对实位epsilon的角平面trace合并
`nu_j/sqrt(1-nu_j²)`系数及正负方向计数也正确；只在有已付整体TC时消费。

当前direct-symbol全投影／完整G逆证明另行支付了这个最后缺口；
不是把单边界结果升级成完整T_p-T_inf。

## 6. C0剩余、源域 compact 与冻结消费

定义

    r_p(s)=2pi[rho_p(s)-rho_inf(s)]
                  +2a sum_(k>=1)q^k cos(kas).

第2节认证有限频段连续／局部有界，第4节认证两端趋零，故r_p∈C0(R)。
实际上compact结论只需有界measurable乘子与两端essential sup趋零，
不依赖额外的半局部epsilon点值级数。

对任意固定有限测度source支持U，将r_p截在[-N,N]：
其逆Fourier核为 `(2pi)^-1 integral r_p(s)exp(is(y-z))ds`，有界；
U×U有限测度，压缩为HS。余项operator norm不超过
`sup_(|s|>N)|r_p(s)|→0`，所以压缩是compact。
因此对所有原合法smooth同源测试，而非仅弱零族，有

    T_p-T_inf=-prime_p+compact_U.

再以有界型唯一延拓与极化消费到固定source L²；
这不把单个T_p或Gamma本身称为L²有界型。
裸source Parseval因子是1/(2pi)，故实际shift原权正好a q^k，没有多一个2pi。
实位E_inf在此固定U也compact。冻结pole0、onlyp2的同一真实域得到

    T_2-T_inf=-w2 Swap+compact_U,
    QW-T_2=compact_U,
    d_R^+=-2w2+o(1), d_R^-=+2w2+o(1).

h_R严格零矩、单位范数、weakly null；两个移位组合范数平方2，
所以最后极限及归一化一致。负diff不推QW负，compact diff也不推其非负。

## 7. 判定、宏观瓶颈和未付输入

主要候选通过不同组织逆审：统一carrier运输、实际P clipping、真实弱极限求值域、
局部频段连续性、完整inverse误差、finite-chain密度和固定source compact均已付。
新增结果不同于旧511有限S相位以及514source平滑边界绝对尾：
它接上实际正Sonin来源并支付此前未付的非紧首prime／全部单prime幂账本。
未证明多个prime的联合G逆／成长S统一性，不能把single-prime证明扩到finite-S任意集合。

实际瓶颈改变为：首prime的非紧消费缺口已消除，剩下真实compact overlap的全低域符号／费用。
其正性或质量下界、完整更大域的outside-p贡献、成长S与支持预算、
真正最低态／prolate连接仍未付；不按C005结算宣告长期Goal完成。
531的nonHS断点保留；本证明绕过绝对prolate系数方法，
不声称half-local kernel变HS或所有epsilon连续。

唯一下一动作是主代理按此范围消费并审已定位的compact signed low remainder；
不再重算已付prime主项，也不复活暂停路线。
本审查无后台进程；未改STATE/cadence。
