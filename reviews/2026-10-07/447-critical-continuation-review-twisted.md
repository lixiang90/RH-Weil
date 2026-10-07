# 447 临界参数与全族 continuation 第二独立全文审查

2026-10-07。审查人 twisted_research。**限定 PASS。** 直接读取447全文，并重新读取
原 source 的 common-signal continuation、same S、联合 error、principal、参数顺序和
late-height 原文；另从原 Mellin 核重算参考指数及判别式。这里审查 root 的主稿，
不以本代理先前优化报告的结论代替核验。

绑定 `notes/447-larger-slot-discriminant-and-critical-strip.md`，canonical LF SHA256
（CRLF及单独CR换为LF后UTF-8）：

`35d0f11bd822bdf7862dc821f2b02628b3a41778ff9633cb27a9bcbf5d3431b1`。

本版本已修 §4 的严格号：由 Delta<=t_c/4 得到的是 zeta<=t_c/128；之后
t_c/128<1/(5800·128) 仍严格。此修正不改变供应或最终结论。
其余未见实质缺口。PASS 限于447列明的确切外部[R]与441–445已经支付的
同源接口，支持稿中 strict sigma_c 的引用推导；不替代整篇原稿的独立验收，
没有执行 Lean 构建或生成 kernel/Comparator 证书，也不是 RH 证明。

## 1. 固定源和准确依赖范围

源为 OpenAI/math 提交 `adc7f1241b42e322a6451854ab7e4b4c146bf78a` 的
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，
canonical LF SHA256：

`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。

本次直接重读的关键位置：

| 原source行号 | 核验事项 |
|---|---|
| 373–398 | 全primitive finite-order Hecke族 beta_*、poles excluded、有限删因子 |
| 400–502 | sigma0∈(1/2,1)的通用 continuation；共同 saving、小Z、Mellin识别、supremum非attainment |
| 3327–3368 | T先于目标；最终同一S、目标presentation、零延拓与ray数据 |
| 6180–6200、6250–6301 | principal实际tuple、三个余项、唯一主signal与只向右移线 |
| 6520–6580 | late-height的完整合同和量词；A_eta、B_eta先于外部N |
| 6715–6780 | primitive/imprimitive及quadratic Dirichlet transfer、s=1例外 |
| 8707–8765 | 完整无商 selected tuple、精确局部操作和全高度majorant |
| 8980–9049 | numerator primitive ramification、全部strict labels的一次conductor预算 |
| 16191–16453 | 原预算允许依赖全族Delta；mesh→K→principal余量→目标→internal orders→tau→N |

明确的[R]仍含原 coefficientwise probe/Poisson与finite compensation、ray/Gauss
校准、局部算术表、固定角色族 reciprocal/growth/functional equation、smooth calculus、
Gaussian/row sectors、通用 reflected energy/additive Gram、detector witnesses、
marked/inverse/plain/recursive moments、sixth-power amplification、fixed-ray prime asymptotic，
以及原全Hecke7/8结论。441–445支付的是这些通用结果的新参数准入与合并。
未把原仅陈述固定几何的 low/high theorem 当作本次扩域输入；未加入AF比例假设。

本次复核的链绑定：441 `dffcaa1899358d581fe3d6438ee87d075588e5e7e8f41ccd8a629fe5c31be0dd`；
442 `87abb4dd86ccae9b8209e030606413ef2b8682631f9c4d9195afdd808ad1b6b7`；
443 `79bfb7f8770eb3865ccdfe0da416388b2182383bd425fd57b39f520b3fd59bc6`；
444 `47686e9b6b28239562e83e9ab5199349458fd19bf9abbe45cca67df8c876957c`；
445 `99ac005976c7c22934b5597c25b0d6fc6d7f3f4d9be604f8cbd53e130eae0f2e`。

## 2. 独立重算参考幂和连续临界证书

原核的几何幂为 l_x/2+s−1+(1−l_x)z+l_y(w−1)。Actual joint error/main
tuple 加 ell(z−1/2)+qell，row sum 加 d(R+delta/2−z)。以 h=1−l_x+ell 合并，
在 s=a、w=1−a、z=17/50 上，减去主留数 C(sigma)=l_x/2+sigma−1+h/6，
准确得到447的 E_sigma(d)。这从物理核直接核实参考指数，而非仅照抄端点公式。

可变几何满足 l_x/2−1+h/6=−11/16；C(s)始终斜率一。因此

\[
 E_{\beta_*}(d)=E_{\sigma_c}(d)-(\beta_*-\sigma_c)
              =E_{\sigma_c}(d)-\Delta.
\]

减 Delta 正确且仅减一次。原 beta_*−7/8 的signed量没有混入实际count；
fixed kappa=3/4合法，Delta_eff=0。

直接将 R_*、q=(1/2−y)delta 代入上述物理指数，再清分母，得到447(7)的三个
多项式。独立卷积计算 4AC−B²，五个显示系数逐项一致；不是靠浮点图或网格。
q0的有理夹逼为1/5842<t_c<1/5841；其余q_i在更大的t<=1/5000区间严格正。
所以critical时 Q(y)>=0、A(y)>0、p>=0。因Q(y)=0只在y=0，唯一等号点为

\[
 \delta_c=\frac{1896-11520t_c}{4896+12096t_c},
 \qquad1/3<\delta_c<2/5.
\]

这位于真实1/50<delta<=3/4范围。清分母后的J在真实矩形内严格正，因此E_sigma<=0。
等号是actual count包络的等号，不证明physical rows真能达到该点。

有理t=1/5900的额外margin亦核：447先用逐系数
A0Q_N−Q0A_N>=0取得Q_N/A_N>=Q0/A0，再使用J<=5/2；得到
42523/38362753440>10^-6。没有误以A(0)作为A(y)上界。

## 3. 全部physical行及critical gap预算

原全族7/8 bootstrap与反证给0<Delta<=t_c/4；它是一个全族数，在目标eta前固定。
Critical selected endpoint相对C(beta_*)至多−Delta，而非仅有零saving。
Selected非floor区间1/2<=d<=h的斜率至少33/50−delta/2>=57/200>0，
所以全区间受端点控制。所有main/error subsets保留原系数、masks，q以全部槽长度加权，
error gain为0；whole-bin先移线，随后才pointwise分箱。

Floor单独R=1，无需actualwitness；no-slot中间的R=76/75−2delta/3合法覆盖floor
和非floor。独立有理核验t=1/5800的保守上界分别为

\[
 E_{floor}\le-4883/870000<-1/200,
 \quad E_{middle}\le-8483/2610000<-2/625.
\]

Outer小行按完整tuple而非quotient估计，相对C(beta_*)的上界为
−12479/145000<−2/25。它包括bounded nontrivial units及d<d_min，
不由actual witness count冒充覆盖。u=1另由principal处理。

Zeta=Delta/32<=t_c/128；由5ell−h>1/48得到供给ell/(h+zeta)>1/5>7/37，
且h+zeta<1。选prime仅在d>=1/2，故w_i<=2ell_i；d_min不缩小供应。
上端成本<=Delta/16，selected余量>=15Delta/16；central损失<Delta/4后
余量>11Delta/16>Delta/2。Floor的独立余量远大于此上端成本，统一m0仍合法。
大行先固定zeta再选足够大的固定z_infty，达到至少Delta节省；不随Z或row改变。

Actual count的fixed Theta coefficients、positive/negative orientation、整体共轭、
inducing-family exceptions、zero-capacity no-slot branches、严格width与内池支持分离
均保留443条件。Delta仅改变固定loss大小和后续有限K，不更换primitive family。
444的联合error proof确实只对整个distinct strict-label集合使用一个numerator
conductor deficit；原source8980–9049直接支持这一步。

## 4. 共享解析、sameS与normalizer

Critical sigma>7/8−1/23200>5/6、401/600；因此D1(1/3)外小行和新D2*均有正域余量。
Good/ramified的c_b=sigma−3/50>81/100、c_r=sigma−1/20>82/100。
Principal局部正确衰减为sigma，不沿用未付的旧7/8 exponent。
完整无商tuple用于一般行及joins，商分解仅用于已经近1非零的dynamic域。

原T及windows在目标前固定；P0由同一positive tail majorant先选。目标后扩大S
仅删去majorant因子，维持同一H_eta在Re s>sigma_c近1、非零。每个目标的low、
high、c_S、A_T和f都使用一个最终S。不能以原旧校正H或不同S拼接。

Fixed-ray渐近使原正窗A_T最终非零，inverse为任意subpower；later finite
excluded primes只改threshold。Principal余项分别由l_y/20、h/600、mu支付，
主留数仍为同一个line2信号。Critical t的代数无理性不违反这些条款：通用log-length
与poly-range前件允许固定实数，实际annular offsets在strict widths后由threshold吸收。

## 5. 参数顺序、actual high合同及Mellin反证

原source16220–16324显式允许预算依赖全局Delta。447依次先选Delta预算、count/moment
losses、capacity decrements、mesh与rounding，再选K/disjointwindows，再定mu及小e。
mu依赖K；它没有被倒用于选择mesh。原plain的mesh独立于槽数，固定K后其height/
seminorm阶可以增大，均在有限target datum后固定。Principal三项损失可以再缩，不破坏
之前的central预算。统一m0取全部正margin的最小值，m=m0/4在目标前固定。

对目标固定最终S与internal orders后，A_eta、B_eta和literal detector ceiling固定。
它们不依赖以后externalN；所有变量使用同一个cumulative T1/2 allocation。
实际函数J=I_modified/(c_S A_T)与f没有T1；以它们得447(13)，不是以截断函数替代。
以source6520–6580的原顺序先选tau，再选N，再增threshold，得到共同
sigma_hi=m0/8>0。Constant、tau、N及threshold可依赖target，saving不能依赖target。

Low和inverse-normalizer成本可合计取omega=Delta/2；二者均有任意小幂接口。
epsilon_*=min(Delta/2,m0/8)>0在target前固定，并严格小于Delta。
原continuation命题允许任意sigma0∈(1/2,1)，没有隐藏7/8下界。
小Z控制来自原f向右移到任意B>2；Gaussian及bounded reciprocal保证joins消失。
大Z两幂界和小Z快速衰减使Mellin在Re s>beta_*−epsilon_*局部一致全纯；
ordinary Fourier inversion在line2识别同一H_eta/L_F^S。
H_eta非零使其给全纯reciprocal延拓。Supremum定义随后选一个实际zero，
无需beta_*被任何target达到；principal pole给reciprocal zero，不妨碍反证。

Primitive/imprimitive finite factors在Re s>0非零。原quadratic norm factorization
转到Dirichlet时，两因子在0<Re s<1全纯；s=1的唯一可能pole/zero抵消由
L(1,chi_-3)=pi/(3sqrt3)>0排除。故447声明的strict半平面及principal例外准确。

## 6. 核验结论及未认证范围

本次32条独立整数/有理断言覆盖全部判别式系数、critical夹逼、等号delta范围、
floor/middle/small的strict上界、解析域与Euler衰减、供应和central预算。
无限连续正性由完成平方证明承担，有限断言不是其替代。

447把t_c准确限定为固定b、原R_*与amplitude矩形中E_sigma严格负的极限，
并允许critical用共同Delta支付。t=1/5800的正包络只说明任意小Delta不能统一
吸收该包络，不声称真实bad rows达到它或存在L-zero。该scope正确。

限定PASS：在上列[R]与同源接口前提下，critical参数的全physical高界、参数
顺序、late-height及全族Mellin反证闭合。没有认证外部原算术/分析整链、Lean elaboration、
kernel/Comparator或RH；AF固定函数比例也没有被转换成Hecke row-count节省。
