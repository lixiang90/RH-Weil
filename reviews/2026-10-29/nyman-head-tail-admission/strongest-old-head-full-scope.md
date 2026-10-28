# Nyman physical head／full 比较：最强旧范围与准入审

2026-10-29；限定支持稿，待root消费。不建C056/593、不计轮，不查新source，不改STATE／cadence／Git。对象是081的真实L²(0,∞;dx) fractional-part synthesis，不能把它的范数直接认作完整经典Weil型。

## 1. 实物和两种约束必须分开

令rho_n(x)={1/(nx)}，g_b=Σb_n rho_n，A(b)=Σb_n/n。取y=1/x，则

    g_b(1/y)=A(b)y−Σb_n floor(y/n)。

当A=0时，每个integer cell [m,m+1)上为常数，且x>1时g_b=0；因此

    ∫_(x≥1/(M+1))|g_b|²dx
      =Σ_(m=1)^M |Σb_n floor(m/n)|²/[m(m+1)]。

这里M是physical-cell截止，不等于polynomial degree。083的sawtooth恒等式和088／096／097的exact jump Gram已经付清这种坐标运输。

087的periodic boundary-mean约束另是Σb_n（affine residual中1+(1/2)Σb_n=0），不是A=0。原拟two-term

    g_N=rho_N−((N−1)/N)rho_(N−1)

虽A=0，却Σb=1/N，不属于087固定boundary-mean的homogeneous tangent。不能用它直接反驳该tangent上的Loewner比较。Root后来给出的同门three-term修正消除了这一域缺口：

    h_N=((N−1)/N)rho_(N−1)−2rho_N+((N+1)/N)rho_(N+1)，
    Σb_n=Σb_n/n=0。

本审下文以这个正确three-term为准；two-term只保留为初始all-coefficient检验，不偷渡其tangent归属。

## 2. 正确域的实际渐近反测

对N≥4，令cutoff X=N+2。h_N在0<y<N−1为0；首两个pulse为

    [N−1,N)：值−(N−1)/N；
    [N,N+1)：值+(N+1)/N，

在[N+1,N+2)又为0。因此旧local region y≤X的实际能量精确为

    H_X(h_N)=2/N²。

这不是零点数据或数值拟合。对1≤k≤K=floor((N−2)/2)，第k对pulse互不重叠，其区间为[k(N−1),kN)及[kN,k(N+1))，振幅仍为上述两个常数。逐段积分给每对

    (N−1)/(kN³)+(N+1)/(kN³)=2/(kN²)。

故full真实能量E满足

    E(h_N)≥2 H_K/N²，E/H_X≥H_K=logN+O(1)。

其中H_K是harmonic sum。Root另一证明腿负责full上界／可能更精确首项；本审独立核的这个lower已经足以否定一个与X无关的、对该全系数空间全部方向成立的full≤C·physical-head比较。它也给096的relative-hard η至少H_K−1的必要费用，前提是对应方向确在所消费空间中。

087的实际Möbius endpoint方向在cutoffX处只支撑2≤n<X、mu(n)≠0，且n=1,X为0。故这里必须要求N−1,N,N+1均squarefree，再用087 QT的full Vandermonde exhaustion把h_N放入该空间；fixedR或受限coefficient-size族未因此覆盖。

这个cofinal适用域非空且有elementary正density：限制N≡2(mod4)，三项均不被4整除；对每个odd prime p排除至多3个mod p²类。在这一AP中union bound的渐近坏比例至多3Σ_(p odd)1/p²≤3(π²/8−1)<1，计数余项对p≤sqrt(Y+1)为O(sqrtY)。故存在无界的合法triple-squarefree N，不需要twin-prime／RH／PNT假设。QT用于growing full-rank空间，不给fixed-degree interpolation或其费用。

## 3. 最强旧逐项核对

| 已核原件 | 可直接消费的最强结论 | 与本比较的实际区别 |
|---|---|---|
| 081 §§3–5 | critical Mellin实现、finite positive Gram／distinguished distance及NB等价；formal inverse不控制critical norm | 本test不是新的carrier／RH等价，也不是d_N lower或upper |
| 082 PH／PL／PM及PI | normalized log-Toeplitz核；相邻log节点迫系数Euclidean-normalized最小谱→0；target coupling闭式 | PL没有将physical first-X cells作为comparison norm，也未给full/head相对下界；标准小谱不是本quotient的定理 |
| 083 §§4–6 | actual sawtooth jump和weighted full norm；low charges不控制local-tail cross及tail self-energy | 已有“不足”的责任分割；未给本两约束空间中uniform domination constant的log lower |
| 087 QP／QQ／QS／QT | 真full Gram的affine projection、capacity／gain公式；full-rank Möbius-support穷尽 | 这些保留target/base coupling，并未证明local Gram替代full；约束Σb与A不能混；本lower不否定finite existence |
| 088 QW／QX／QY／QZ | complete local formula，local/parabolic/far PSD分解，actual easy-optimizer leakage上证书，periodic far majorant | QY允许选择同一candidate并实际估leakage，不要求全方向uniform C；本test不反驳它 |
| 096 SU／SW／§5 | exact local jet Gram正定；若relative η已知，则leverage有条件上界；local-only endpoint数值退化 | §5明确说是finite diagnostics，非渐近定理。没有已付同域η_N≳logN的actual必要下界 |
| 097 SY／SZ／TA | 任意integer window的exact finite Gram、periodic Gram和far completion | 公式允许计算新vector，但并未给它的growing-index pulse计数／harmonic渐近；本lower并非更强已出渐近的弱改写 |
| 099 TH | full夹在全部y≤X² spatial Gram加O(X^-2)periodic Gram之间 | 保留全部parabolic区，故不把本first-X head失败当反例；其结论不以first-X head取代spatial Gram |
| 104 UA／UC | unit-cell恢复divisor charges／incidence inverse；每fixedR、fixed squarefree nodes的polylog coercivity | nodes／rank量词不同，不能借fixed-node bound覆盖moving adjacent triple或反向推出full/head uniform性 |
| 111 VB／VC | 保留全部y≤X²的cell means，只截断远端cell variances，并得rank-independent O(1/M) relative error | 不是physical y-window截成M。新pulse能量仍留在其all-means中，不否定111的uniform approximation |

检索08x–111的相关exact／adjacent／local-only段，除082的log节点碰撞与096的有限诊断，未找到已出同对象的log physical-head/full失真定理。此为限定实际检索和上述原件逐读结论，不是全项目／全世界优先权断言。

因此本审不将“097有一般exact formula，可事后代入”自动等同于“旧定理已消费这个uniform渐近界”。这里还需actual moving-vector的pulse算术、两约束域及growing Möbius空间归属才能得到新的必要费用。可将其作为一个具体量化比较交root决定数学准入；不应称新增独立算术正性／源桥或whole改进。

## 4. 必须反扣的target／response信息

最强旧082 PI给z_n=<rho_n,chi>=(logn+1−gamma)/n。对同一three-term有精确

    <h_N,chi>=(1/N)log(1−1/N²)=O(N^-3)。

并且Σb=0是boundary response zero。故这个full/head坏方向与裸target的耦合很小；不能仅凭它证明d_N不趋0、canonical affine optimizer失败、实际mean-zero optimum有log误差，或整个local/Feshbach方法失败。若用full范数归一化，其target coupling最多O(N^-2/sqrt(logN))。另一方面，真实affine coupling是Q*(z+G b_base)，还含base cross；本计算也不证明坏方向对所有actual optimizer无害。

这个test准确改变的选择是：不能把physical head对全部合法方向的uniform Loewner比较当成免费设施；应继续保留095／098已要求的response／target alignment或实际hard leakage。它不把这些既有正确方向冒作本轮首次发现，更不说明uniform log损失单独就能决定SP阈值。

## 5. 当前消费等级与边界

本审支持“已形成、可证伪且有明确实际域的head/full比较”，并确认所核最强旧未给同域渐近lower；若root数学合同要求这一必要费用，可以限定准入。最终是否按一数学轮结算仍由root的合同／独立proof／fresh消费决定，本稿本身不计轮。

有限系数／fixedR、non-squarefree三点、actualtarget optimizer、含全parabolic／allmeans的metric、source-adaptive或其它有费修复必须各保原量词。不以generic norm坏方向代替actual目标反例，不复活091错误一般δ或其093／094-SP下游冻结。

这个Hilbert norm不是原physical r=e^(u/2)f的完整Weil型；未支付新principal、整过滤／mixed RR、Γ/contact／properpowers／双pole身份、dangerous corecross或成长Ξ。Whole542+555→557 leading4/5仍只是既有负惯性UPPER，长期Goal完成门未通过。

本审实际只写本独占文件，无外部query／PDF／下载／数值实验；STATE、cadence、manifest与Git未改。新完整三点估计和其净后果须root与另一证明腿对齐，不能凭此支持稿存在就完成消费。
