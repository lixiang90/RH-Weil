# 更大固定槽几何的连续端点证书与精确包络极限

2026-10-07。独立推导。范围为 441–445 已逐前件准入的原同源 physical
finite compensated probe，及这些稿明确列出的外部通用 [R] 输入和全 Hecke
7/8 bootstrap。这里只新增推导报告，不改 441–446、原 math 或索引。

**结论：固定 t=1/5900 的连续端点证书严格成立，且 floor、middle、supply、
共享轮廓、principal 与外行均保留正余量。候选边界为
sigma=20649/23600=7/8−1/23600。** 这是在已经列明的 [R] 条款成立前提下
对 445 证明接口的再次参数支付；不是外部原稿的完整验收、Lean 证明或 RH 证明。
AF 的简单临界线比例未进入此优化。

## 1. 来源和固定参数

源为 OpenAI/math 提交 `adc7f1241b42e322a6451854ab7e4b4c146bf78a` 的
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，
canonical LF SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。
本次直接重读 441–445；延续此前独立读源的准确通用前件，不引用原固定几何的
low/count/high 结论来覆盖新参数。绑定的 canonical LF 哈希为：

| 稿件 | SHA256 |
|---|---|
| 441 variable low | `dffcaa1899358d581fe3d6438ee87d075588e5e7e8f41ccd8a629fe5c31be0dd` |
| 442 shared contours | `87abb4dd86ccae9b8209e030606413ef2b8682631f9c4d9195afdd808ad1b6b7` |
| 443 actual capacity | `79bfb7f8770eb3865ccdfe0da416388b2182383bd425fd57b39f520b3fd59bc6` |
| 444 joint central high | `47686e9b6b28239562e83e9ab5199349458fd19bf9abbe45cca67df8c876957c` |
| 445 continuation | `99ac005976c7c22934b5597c25b0d6fc6d7f3f4d9be604f8cbd53e130eae0f2e` |

取 b=1/8，并固定

\[
 \ell=1/6+t,\quad l_x=17/48-t/2,\quad l_y=23/48-t/2,
 \quad h=13/16+3t/2,\quad \sigma=7/8-t/4.                 \tag{1}
\]

主留数仍为 w=1、z=1/6；准确地
\(l_x/2-1+h/6=-11/16\)，所以 \(C(s)=s-11/16\) 不变。
原全族 bootstrap 给 beta_*<=7/8；反证 beta_*>sigma 时
Delta_new=beta_*−sigma>0。合法 fixed kappa=3/4、Delta_eff=0；
真实非 floor bin 满足 1/50<delta=2a−1<=3/4。
不能把负的 beta_*−7/8 代入原非负 detector loss。

保持 alpha=5/6、实际全部槽长度加权的 q，并令

\[
 x=q/\delta\in[0,1/2],\quad y=1/2-x\in[0,1/2],
\]
\[
 D=(37+34y)/18,\quad P=(7+18y+8y^2)/9,
 \quad J=(\alpha-\delta)D+\delta P,
\]
\[
 R_*=1-\delta+\frac{(\alpha-\delta)\delta P}{2J}.
                                                               \tag{2}
\]

这些是 443 已支付的 actual count，而非另设 nominal rows。
Main slots 使用原 physical 系数和 masks；error slots 的 g_i 恰为零。
在真实矩形上 0<J<=5/2，且 1−delta<=R_*<=1−2delta/3。

## 2. 把连续问题化为二次判别式

444 的任意物理行指数是

\[
 E_\sigma(d)=K_\sigma+(1/2+\ell)\delta+\ell q-h(1-R_*)
 +(d-h)(R_*+\delta/2-17/50),
\]
\[
 K_\sigma=2/3+\ell+b/6-\sigma=-1/48+5t/4.
                                                               \tag{3}
\]

将 (2) 代入 (3) 的 d=h 端点，直接得

\[
 E_t=-1/48+5t/4-(1/16+y/6+ty)\delta
 +(13/32+3t/4)(\alpha-\delta)\delta P/J.                 \tag{4}
\]

这里的指数已相对 C(sigma)。比较 C(beta_*) 仅需再减 Delta_new；
不能再扣 t/4。变化式中的 5t/4 已包含 −sigma′ 的贡献。

令 \(p_t=10368J(-E_t)=A_t(y)\delta^2+B_t(y)\delta+C_t(y)\)。
完全展开得到：

\[
\begin{aligned}
 A_t(y)&=2448+6288y+4512y^2+1536y^3
             +t(6048+2304y+8064y^2+9216y^3),\\
 B_t(y)&=-1896-3016y-208y^2+t(11520+3360y-960y^2),\\
 C_t(y)&=370+340y-t(22200+20400y).                       \tag{5}
\end{aligned}
\]

这与原完成平方证书的 t=0 版本逐系数一致。其判别式的相反数为

\[
 Q_t(y)=4A_t(y)C_t(y)-B_t(y)^2=\sum_{i=0}^4 Q_i(t)y^i,
                                                               \tag{6}
\]

| i | Q_i(t) |
|---|---|
| 0 | 28224−164747520t−669772800t² |
| 1 | 1198848−664266240t−775526400t² |
| 2 | 5344448−877278720t−893260800t² |
| 3 | 7154944−484362240t−1469952000t² |
| 4 | 2045696−113203200t−752947200t² |

每个 i>=1 的系数在 0<=t<=1/5000 上递减，并分别严格大于
1000000、5000000、7000000、2000000。故只要 Q_0(t)>0，
Q_t(y)>0 对全部 y>=0 成立。又 A_t(y)>0，完成平方给

\[
 p_t=A_t\left(\delta+\frac{B_t}{2A_t}\right)^2
                      +\frac{Q_t}{4A_t}>0.             \tag{7}
\]

这证明真实矩形的连续正性，实际还覆盖全部 delta∈R；没有网格到连续的推断。

## 3. 一个精确固定证书：t=1/5900

为使所有数为整数，写 A_N=N A_t、B_N=N B_t、C_N=N C_t，N=5900。
令 Q_N=4A_N C_N−B_N²。相应系数是：

| y 次数 | A_N | Q_N |
|---|---:|---:|
| 0 | 14449248 | 9797299200 |
| 1 | 37101504 | 37811952537600 |
| 2 | 26628864 | 180863397171200 |
| 3 | 9071616 | 246204393472000 |
| 4 | 0 | 70542025932800 |

特别 A_1<=3A_0、A_2<=2A_0、A_3<=A_0，而
Q_1>=3Q_0、Q_2>=2Q_0、Q_3>=Q_0、Q_4>0。
因此 \(A_0Q_N(y)-Q_0A_N(y)\) 的全部系数非负，得

\[
 p_t\ge\frac{Q_N(0)}{4N A_N(0)}
        =\frac{85046}{2960089}.
                                                               \tag{8}
\]

等号在 y=0、delta=116405/301026 时成立；这个 delta 在真实允许区间内。
用 J<=5/2 推出完整统一 margin

\[
 \boxed{-E_t\ge\frac{42523}{38362753440}
                  >\frac1{1000000}=:m_{ad}.}            \tag{9}
\]

该界没有将真实 bad rows 改为任意名义集。仅使用实际 count 的 uniform 包络；
不要求包络极小点真在某个物理 dyad 出现。

此几何准确为

\[
 \ell=2953/17700,\quad l_x=25069/70800,\quad l_y=33919/70800,
 \quad h=19181/23600,\quad \sigma=20649/23600,
 \quad C(\sigma)=553/2950.                              \tag{10}
\]

## 4. 端点之外的全部实际行

Selected 非 floor 的 d∈[1/2,h] 上，(3) 的 d 斜率满足
R_*+delta/2−17/50>=33/50−delta/2>=57/200>0。
故 (9) 控制整个区间，而非只控制 d=h。

Floor 单独取 delta0=1/50、R=1、q<=1/100，斜率为67/100；
直接由物理幂得

\[
 E_t(h)\le-7/1200+(32/25)t=-9941/1770000<0.              \tag{11}
\]

对于 d_min=1/100<=d<=1/2，保持原 no-slot count；共同包络
R=76/75−2delta/3 覆盖 floor 与非 floor。斜率
101/150−delta/6>0。原 endpoint 为至多 −49/14400，固定 d 的
几何导数为 13/50+delta/4+q<=177/200，于是

\[
 E_t(d)\le-49/14400+(177/200)t=-1171/360000<0.            \tag{12}
\]

此处甚至用了较大 delta<=5/6；强 bootstrap 的 delta<=3/4 无需进一步收紧。
No-slot 仅指未把 prime factor 用于 moment，完整 tuple 的槽仍全部存在。

固定 ζ=m_ad/32=1/32000000。全部上端斜率可以界为2；扩至
d<=h+ζ 的额外成本至多 m_ad/16，所以 selected 余量至少
15m_ad/16=3/3200000。且

\[
 5\ell-h=1517/70800>\zeta,\quad h+\zeta<1,
 \quad\ell/h-7/37=34243/2129091>0.                      \tag{13}
\]

因此所有原 actual supply 仍满足
ell/(h+ζ)>1/5>7/37；strict widths、whole-slot rounding、内部 pool 与物理
支持不相交的证明按 443 保留。d_min 不缩小 prime supply：只在 d>=1/2
选择 primes，w_i<=2ell_i。

Outer 小行按 442 完整无商 tuple 重放，相对 C(beta_*) 的自由指数为

\[
 h(13/75)-l_y/2+(63/50)d_{\min}
 =-79/800+(51/100)t+63/5000=-20311/236000<0.             \tag{14}
\]

这里相对 C(beta_*)，不可偷改成相对 C(sigma)。若需要后一参考，只增至多
t/4，仍严格负。更粗的 2d_min 计数给 −92823/1180000。
Outer 大行先固定 ζ，再选固定足够大 z_infty，正 ζz_infty 可以支付任何
预定固定 margin；不令 z_infty 随 Z 或 moving row 改变。

## 5. 已准入接口的再次支付与量词

这一步不能只凭 (9) 宣布完成。更大 t 的实际桥分别为：

1. **Low。** (10) 的 ell 仍在 [1/6,1/5]，441 的通用反射能量、实际 Td/H、
   additive Gram 和 tuple 亏损证明直接适用，得到
   \(|I_{modified}|\ll Z^{C(\sigma)+\epsilon}\)。不调用原固定 low theorem。
2. **Actual rows。** 固定 kappa=3/4、Delta_eff=0；(13) 支付供应。
   443 的真实 witness、原 Theta 系数、zero extensions、inducing exceptions
   和 width decrements 无须改变。Alpha 仍为5/6。
3. **Joint errors。** 444 的 dynamic local 域与所有 error-slot × 一个 numerator
   conductor 分配不含 ell=1/6 的固定限制；按固定新 K 分配有限 losses。
   Off-row、strict ramified 与 mixed main/error gain 仍为同一个物理表达式。
4. **共享解析域。** 新 sigma>5/6、sigma>401/600，442 的 D1(1/3) 与 D2*
   重放仍成立。D2* 的 good/ramified 衰减可取
   c_b=19233/23600、c_r=19469/23600，均正；principal B_p+1=O(Q^−sigma)。
   原 H_eta 在 Re s>2/3 全纯，以正 majorant 在目标前重选 P0 保证
   Re s>=sigma 上 |H_eta−1|<=1/2。未用待证的新无零性。
5. **Principal。** 留数误差仍是三个正 margin：
   m_w=l_y/20=33919/1416000、m_z=h/600=19181/14160000，及
   任意 fixed 0<mu<sigma min ell_i。正 ray normalizer 最终非零且逆为任意小幂。

严格顺序：先固定 t、bootstrap、m_ad、count losses、width decrements、uniform
mesh 与 rounding，再选 fixed even K 及原 disjoint windows。K 固定后才选
mu=sigma ell/(2K)、amplitude 宽度、prime preliminary powers 与小 e。
Central 全部 real loss 与 normalizer 成本取小于 m_ad/4；principal 三项分别
取小于其 margin 的1/4。ζ 已固定，外大行的 z_infty 也在目标前固定。
不能先以依赖 K 的 mu 倒选 mesh。

令 m0 为 m_ad、m_w、m_z、mu 与20311/236000的最小值。
所有非principal及principal项留至少 m0/2；随后 m=m0/4。
目标确定后才固定 arithmetic data、最终同一个 S、internal Sobolev/height orders。
先得到固定 A_eta、B_eta 和原 detector height ceiling，之后选 tau_eta，再选外部
tail order N_eta。J_eta、f_eta 都不含 T1，全部 physical rows 共用原 cumulative
height buffer。与445相同的 late-height 关闭给 sigma_hi=m0/8>0，且与目标无关。

反证 beta_*>sigma 时，在目标前取 omega=Delta_new/2，再令
epsilon_*=min(Delta_new/2,m0/8)>0。445 的原 Mellin continuation 和全族
supremum 非 attainment 论证遂可逐式重放；不为新参数假定零自由性。
因此相对于列明的 [R]，(10) 的严格半平面改进可以闭合；有限因子与 quadratic
transfer 仍用同一论证。没有边界线上无零断言。

## 6. 严格额外端点余量的精确极限、临界参数与一个反例

令 t_c 为

\[
 28224-164747520t_c-669772800t_c^2=0
\]

的正根，即

\[
 t_c=\frac{56448}
 {164747520+\sqrt{164747520^2+4\cdot669772800\cdot28224}}
 \simeq0.0001711975385049552.                            \tag{15}
\]

对于 0<=t<1/5000，A 的系数逐项满足 A_1<=3A_0、A_2<=2A_0、A_3<=A_0；
当 t<t_c 时 0<Q_0<=28224，而 (6) 的其他系数远大于
3Q_0、2Q_0、Q_0。因此 (7) 的全局下界准确为

\[
 \min_{y\ge0,\delta\in\mathbb R}p_t
 =\frac{Q_0(t)}{4A_t(0)}>0,                             \tag{16}
\]

在 y=0、delta=−B_t(0)/(2A_t(0)) 取得；在 0<=t<1/5000 上准确有
1/3<delta<2/5，故该 delta 在真实矩形内。
故任何固定 rational 0<t<t_c 都有连续统一 margin，并可以按 §5 的同一顺序
重新选择小 losses 和固定 slots。t=1/10000、1/6000、1/5900 全部通过。
严格 E_sigma<0 的这族固定参数证书的边界下确界是
7/8−t_c/4≈0.874957200615374。这里的“极限”只指相对 C(sigma) 的额外严格余量，
并非实际 high/continuation 接口不能启动的极限。

在 t=t_c，准确有 Q_0=0、Q_i>0（i=1,…,4），A_t>0，因此 (7) 给
p_t>=0、E_sigma<=0。Q_t(y)=0 当且仅当 y=0；唯一等号点为
delta=(1896−11520t_c)/(4896+12096t_c)，约为0.38668853。
其范围 1/3<delta<2/5 可由
792−46656t_c>0、312+81792t_c>0 直接证明；在实际参数矩形内。
有理夹逼 1/5842<t_c<1/5841<1/5000 及 §2 的系数下界，严格核实上述所有符号。

反证 beta_*>sigma(t_c) 时，global Delta_new=beta_*−sigma(t_c)>0 仍在目标前固定，
所以 E_beta=E_sigma−Delta_new<=−Delta_new。可先按 Delta_new 的固定小份选择
count losses、capacity decrements、mesh 和 rounding，再选 K/windows，最后选 mu
与小 e；并可取 ζ<=Delta_new/32，同时满足 (13) 的 supply/上端条件。
上端 cost<=Delta_new/16，real loss<Delta_new/4 后，central high 仍可保留
Delta_new/2。Principal 与外行仍各取其原正 margin，共同余量取它们和 Delta_new
的正最小值，继而重放 §5 的 late-height 和 continuation。
因此 critical 参数也可以由反证中的正 Delta_new 支付损失而启动；不能把
相对 C(sigma) 的零额外余量误写成不能进行 uniform saving。

作为准确的失败见证，t=1/5800 时取

\[
 y=0,\quad \delta=57215/147963,\quad q=57215/295926.
\]

这些值满足1/50<delta<3/4及q=delta/2。准确得到

\[
 p_t=-29297/1430309<0,\quad J=2164165/1775556,
 \quad E_t=29297/18075106080>0.                         \tag{17}
\]

所以仅加入 delta<=3/4 不能突破此 endpoint 包络障碍；临界点已经在该矩形内。
(17) 是已准入 count 上界与 amplitude 范围的代数反例，不证明物理坏行真能
同时达到该包络，也不证明任何 L 函数存在相应零。进一步改进须在这个临界
区间获得更强的实际 count/gain 关联或改造 high 估计，不能靠减小误差 ε。

## 7. 有限精确核验范围

本次用整数/有理运算逐项展开 (5)–(6)，核 N=10000、8000、6000、5900、5800
的判别式；核 (8)–(14) 的分数、m_ad 和供应不等式；并核 (17) 位于真实矩形及
正指数。显示的小数只用于定位 t_c，证明全部使用有理系数和 (15) 的闭式。
正性证明来自 (7) 及明确系数不等式，覆盖连续集合；有限运算不是原来源的
形式化验收，也没有承担未被列明的 analytic theorem。
