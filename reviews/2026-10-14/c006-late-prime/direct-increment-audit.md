# C006：晚素数的固定光滑源增量与边界平方

2026-10-14；独立数学推导，只写本文件，不改 STATE/cadence、不单独计轮。
恢复了 AGENTS、README、STATE、check/show、Goal、C006、D20261014A 与532。
起始 HEAD `7b6652d`。来源接口为2021实际Sonin trace、531真实projection及532裸Mellin求值。

## 结论与必要的对象限定

下面推导适用于**固定紧支光滑源g**，特别是C006冻结两patch、两矩零的全部固定g。
g不随p改变。对实际整数素数p趋∞，有

    T_p(g)-T_inf(g)=p^(-2) L(g)+O_g(p^(-5/2)),
    L(g)=1/(2pi²) integral |g_hat(s)|²
                              |k_s(1)-gamma_s conjugate(k_s(1))|² ds.

其中k_s是实际实位Sonin cutoff1的裸unitary Mellin求值向量，
`gamma_s=m(-s)`，`m(s)=pi^(is)Gamma(1/4-is/2)/Gamma(1/4+is/2)`。
L(g)≥0，且每个非零紧支光滑g有L(g)>0。
所以晚素数在每个固定非零光滑g上最终给严格正增量；真实prime项在冻结域严格为0。

首项L是有界源L²二次型。余项可在固定支持、足够高的固定Sobolev有界集上统一，
但本审查**没有证明whole源L²单位球上uniform p^(-2)或p^(-5/2)费用**。
本结论也只属于single-p相对arch的family，不是逐次添加到一般finiteS的预算。
低域完整Weil符号与many-prime相互作用均未支付。

## 1. 真实域及其source-prime账本

物理H=L²((0,infinity),dx)，F核为2cos(2pi xy)，P为实际Sonin projection。
真实首尾接口保持

    B=I-qU_a, q=p^(-1/2), a=logp,
    G=(1+q²)I-qC_a, C_a=P(U_a+U_a*)P|RanP,
    P_p=BP G^(-1)PB*.

Mellin裸求值归一化为 `U_inf f(s)=(2pi)^(-1/2)integral f(x)x^(-1/2-is)dx`。
因此 `rho_inf=||k_s||²`、
`rho_p=|1-qe^(-ias)|²<k_s,G^(-1)k_s>`，并且
`T_p(g)=integral |g_hat(s)|²rho_p(s)ds`。
这里g_hat=integral g(t)e^(-ist)dt，不另乘unitary因子。

冻结source跨度小于log3，p≥3的所有±nlogp相关严格0。
因此上述晚prime增量属于actual Sonin overlap，不是隐藏的prime functional。
两矩零保持pole准入；以下fixed-g推导不依赖偷偷更换此条件。

## 2. 裸evaluation的真实边界与尾展开

令 `z_s=k_s(1+)`。实际Sonin vector在x<1为0，在x≥1有光滑右侧表达。
这里边界值由实位cosine cutoff resolvent取得，不是一般L²函数的点值。
实际Fourier关系给

    F k_s=gamma_s conjugate(k_s),  |gamma_s|=1.

其physical大x尾为

    k_s(x)=-(F k_s)(1+) sin(2pi x)/(pi x)
               -(F k_s)'(1+) cos(2pi x)/(2pi² x²)
               +O_s(x^(-3)).                            (1)

所以首系数 `t_s=(F k_s)(1+)=gamma_s conjugate(z_s)`。
逆审纠正了显式第二cos项的负号：外部cosine积分两次分部积分给此符号；
下文M1首项只用sin项，第二项再付一次非驻相，因此最终边界平方不变。
所需任意有限阶尾/导数误差常数随s至多多项式增长。

域与正则性支付：从actual两cutoff公式，先把formal Mellin forcing改写为
有限低区间cosine积分及其 `(I-C_0²)^(-1)` 修正，C_0=1_(0,1)F1_(0,1)。
完整Mellin cosine积分给unit模Gamma系数；从(0,1)积分中减去它后，
剩余(1,infinity) Mellin振荡积分按x分部积分。
其第N阶forcing导数为多项式(s)乘y^(-1/2-N)，N≥1后可积。
有限低区间resolvent修正光滑至端点，按同样次数分部积分，
得到(1)以及每个有限阶的多项式常数。Fourier boundary jump确定首系数为−t_s/pi。
不能将(1)套给一般未具边界正则性的Sonin L²向量。

同一个低区间表达还给

    z_s=1/sqrt(2pi)+O(1/|s|),  |s| -> infinity,            (2)

并给所有实s的连续有界z_s。因为积分
`integral_0^1 x^(-1/2+is) h(x)dx` 对光滑h在log坐标一次分部积分为O(1/|s|)，
而低resolvent保持其L²及光滑端点控制。Gamma系数只有unit模。

## 3. q与logp联合：actual压缩移位的端点计算

对每个固定s，写k=k_s、z=z_s、t=gamma_s conjugate(z)。
内积采用第一变量反线性。actual dilation为U_a k(x)=p^(-1/2)k(x/p)，故

    <k,U_a k>=sqrt(p) integral_1^infinity conjugate(k(py))k(y)dy.

将(1)代入，在y=1端点分部积分。由于实际p是整数，
`sin(2pi p)=0`、`cos(2pi p)=1`。于是

    <k,U_a k>=-p^(-3/2) conjugate(t)z/(2pi²)+O_s(p^(-5/2)),
    c_1(s,a):=<k,C_a k>
       =-q³ Re(gamma_s conjugate(z)²)/pi²+O_s(q^5).        (3)

积分中的k(y)/y及其所需导数可积，保证端点计算合法。
这一步同时保留q=p^(-1/2)和physical scale p=e^a，没有只作固定a的小q展开。

再令u=1_(x≥1)U_a* k。尾展开给

    u(x)=-q t sin(2pi p x)/(pi x)+O_s(q³x^(-2)),
    ||u||²=q²|z|²/(2pi²)+o_s(q²).                       (4)

low Fourier泄露 `1_(0,1)F u` 为O_s(q³)：
主振荡的p±y频率在y∈(0,1)离0，端点积分是O(1/p)；
更高尾亦满足同样或更好的界。actual Sonin投影公式因此给

    P U_a* k=u+O_s(q³),
    P U_a k=gamma_s F conjugate(u)+O_s(q³).               (5)

两branch交叉是o_s(q²)，而不先假设它们正交。
可定量取O_s(q³)+O_s(q⁴ logp)：在x≤p/2时Fu的nonstationary界O_s(q³)，
而integral_1^(p/2)|u|≤O_s(q logp)；在x≥p/2时||u||≤O_s(q²)、||Fu||≤O_s(q)。
于是(4)、(5)给

    c_2(s,a):=<k,C_a²k>=||C_a k||²
       =q²|z|²/pi²+O_s(q³).                            (6)

所有这些误差可用同一有限次多项式(s)常数控制；
一旦固定源g光滑，乘|g_hat(s)|²后可积分。

## 4. 真正首阶：正交化质量项相消，而不是q²T_inf

记alpha=1+q²、r=q/alpha、d=2cos(as)，
`G^(-1)=alpha^(-1)sum_(j>=0)r^j C_a^j`。
因此密度增量的准确组织为

    rho_p-rho_inf
       =-r d rho_inf
          +sum_(j>=1)r^j c_j-d sum_(j>=1)r^(j+1)c_j.    (7)

显式q²质量项因alpha在分子/Gram逆中**精确相消**。
不能把q²rho_inf单独消费为晚prime费用。
对j≥2，`|c_j|≤2^(j-2)||C_a k||²`；(5)又给||C_a k||=O_s(q)。
所以(3)、(6)及完整几何尾给

    rho_p-rho_inf
      =-2r cos(as)rho_inf
        +q⁴/pi²[|z_s|²-Re(gamma_s conjugate(z_s)²)]
        +O_s(q^5).                                     (8)

不是只有形式的前两项展开：p≥3保证全部尾的2r<1有统一gap。

## 5. fixed smooth source的大移位迹实际抵消

(8)的第一项不能pointwise删除。需要单独支付

    J_g(a)=integral |g_hat(s)|²rho_inf(s)e^(ias)ds
          =Tr(U_a A_g P A_g*).

对固定g∈Cc∞及a=logp超过其相关跨度，实际有

    J_g(logp)=O_(g,N)(p^(-N))  for every fixed N.         (9)

以下用primary实际核说明这不是从粗范数推来的结论。
实位2021公式及prolate spectral decomposition精确给

    T_inf = Gamma_actual + D_delta
                      -sum_j lambda_j² <zeta_j,theta(.)zeta_j>.

对rho>1，Gamma off-diagonal核为
`-rho^(-1/2)/(1-rho^(-2))`，而primary的

    delta(rho)=2sqrt(rho)[Si(2pi(1+rho))/(2pi(1+rho))
                         +Si(2pi(rho-1))/(2pi(rho-1))]

把两个Si都替换为pi/2时，恰为相反数
`+rho^(-1/2)/(1-rho^(-2))`。
所有非振荡代数主项在actual归一化下精确相消。
Si的剩余是频率rho±1的端点振荡尾。
将rho=p exp(t)代入固定光滑相关函数，反复t分部积分；
相位导数至少const·p，得到任意所需p负幂。

zeta项也由actual finite Fourier低源取得，不删除它：
`zeta_j(x)=F xi_j(x)/sqrt(1-lambda_j²)`，x≥1。
xi_j在[0,1]光滑、实偶，在0的所有奇导数为0。
对其cosine积分反复分部积分，全部代数尾只来自x=1边界振荡。
在source相关的t积分中，相位p exp(t)x且x≥1，无stationary点。
xi_j任意固定阶导数可用actual smooth C_0 kernel和
`C_0 xi_j=lambda_j xi_j`界为const/|lambda_j|。
乘lambda_j²后至多留下|lambda_j|，primary实位快速谱给sum|lambda_j|<infinity。
因此相位分部积分及j求和可合法绝对控制，得到(9)。
这项费用依赖固定g的有限多个导数；不能据(9)宣布整个L²单位球具有该rate。

## 6. signed首项、source费用和非空范围

将(8)对|g_hat|²积分并用(9)，得到

    T_p(g)-T_inf(g)=p^(-2)L(g)+O_g(p^(-5/2)),
    L(g)=1/(2pi²)integral |g_hat(s)|²
                               |z_s-gamma_s conjugate(z_s)|² ds.

平方恒等式支付符号，没有把unknown低谱压缩定义成正项。
(2)及Gamma相位非恒定表明L的乘子在某个开区间严格正；
非零紧支光滑g的Fourier transform是非零整函数，不能在该区间全零，故L(g)>0。

由于z_s全实线有界，首项有**真实source L²质量界**

    0<=L(g)<=C||g||²,

C只依赖固定archSonin cutoff及此归一化，不依赖p或g。
余项不是已付的source L²质量界：以上有限次尾、端点和phase微分估计给
某个固定有限M与常数，使余项被

    C p^(-5/2) integral (1+|s|)^M |g_hat(s)|² ds
       +C_N p^(-N) [fixed-support finite smooth seminorm of correlation_g]

控制。取N足够大，这在固定支持的足够高Sobolev有界集上是uniform O(p^(-5/2))。
它完整支付每个固定smooth g及这种有界集，但没有删掉导数费用。

于是实际single-p family对每个固定smooth g有
`sum_(p≥3)|T_p(g)-T_inf(g)|<infinity`；在上述Sobolev有界集亦统一。
没有把sum p^(-1/2)粗relativeGamma界的发散作为实际反例。
也没有把该绝对求和升级到连续添加一般finiteS：B_S压缩Gram会产生不同cross。

## 判定与停止／重新准入

新增的是固定实际source的晚prime正p^(-2)边界平方及single-p可求和费用，
而不是旧固定p compact性、generic normtransport或假设的growingS统一范数。
首项支付源L²质量，余项保留固定光滑/Sobolev前件。
冻结source上late prime functional为0，故这个正项是实际overlap净增量。

实际宏观瓶颈没有因此消除：whole L² joint frequencies s~p、低域signed compact余项、
base S={infty,2}或一般finiteS的增量、growth支持与最低态均需另付。
本审查不从pointwise eventualpositive推一个uniform positive operator或uniform p^(-2)界。

唯一下一动作：主代理对(1)真实boundary tail、(3)/(6)cross和(9)actual取消作独立逆审，
再分别决定fixed smooth single-p结果是否消费、whole源L² joint域还有何独立估计。
没有待处理进程，不单独计研究轮；在逆审前该文件不视为最终主笔记定理。
