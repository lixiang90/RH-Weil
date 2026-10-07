# 原 central error slots 与可变槽 high saving

2026-10-07。状态：**相对下列明确通用 [R] 输入，same-source central 联合估计和全部 moderate d 区间的严格 high saving 已支付。** 本报告给出可用于下一主稿的实际证明接口，不以 nominal R 替代实际 row count，不引用固定几何的 `lem:high-bin` 数值结论。未构建 Lean；不独立认证原 recursive moments 的全部证明，也不在此单独宣布新的无零半平面或 RH。

## 1. 来源、已支付接口与参数

只读来源：OpenAI/math 提交 `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`。
canonical LF SHA256：

`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。

直接读原 8700–9195、15520–16480 及其引用的 local table、full tuple、buffered bins、central accounting、physical amplitudes 和 actual count proof。补充原位置：4010–4188、4250–4321、4385–4547、5502–5623、5808–6165、9220–9269、12492–12578、14975–15520。

交叉核验两个已保存接口，但下面 central joint estimate、Mellin exponent 和全 d 比较重新推导：

| 报告 | canonical LF SHA256 | 用途 |
|---|---|---|
| `hybrid-shared-contour-extension-derivation.md` | `07b9643b62e9e8e3f8d91150392f7c34f186b3a7546e49df880a0bb70ed68ff1` | 同一 full correction 的 D2*、whole-bin move、principal/outer 接口 |
| `hybrid-effective-kappa-and-capacity-admission.md` | `69c290f7df660b8cefe72c792a63e3ed67de7d4b1756aee8d174a25fbe586c79` | actual witness/moment/slot selection 重放后的实际 R 上界 |

固定

\[
 t_0=1/20000,\quad \ell_1=1/6+t_0=10003/60000,\quad b=1/8,
\]
\[
 l_x=42497/120000,\quad l_y=57497/120000,\quad
 h_1=32503/40000,\quad \sigma_1=69999/80000=7/8-t_0/4.
\]

原 Mellin zeta 留数仍在 z=1/6，故同一 principal signal 的
`C(s)=s+l_x/2-1+h_1/6=s-11/16`。
接受原全 finite-order primitive Hecke 7/8 结论作为明确 [R] bootstrap，反证范围为

\[
 \sigma_1<\beta_*\le7/8,\qquad
 \Delta_1=\beta_*-\sigma_1\in(0,1/80000].                 \tag{1}
\]

取 `kappa_eff=3/4`、`Delta_eff=0`，而不是将负的 `beta_*-7/8` 填进旧 count statement 的正容量损失。每个非 floor bin 的 `delta=2a-1<=2beta_*-1<=3/4`。下面较宽的 `delta<=alpha=5/6` 包络仍可用于数值认证；它不虚构实际达到 alpha 的行。

## 2. 原 full product 和动态 D_i 分解确实保持同源

选定物理槽 prime p 后，原有限操作的准确 selected replacement 是

\[
 \bar\eta(p)Q^{x+z-1}P_p^*-Q^{z-w-1}P_p
 =\frac{1-D}{(1-V)(1-W)}Q^{z-1}G_p,                    \tag{2}
\]

源 8717–8728。它不含固定 ell 数值；每个 selected prime 仅出现一次，因为 underlying windows disjoint。完整 correction 始终是源 8707–8711 的有限 tuple：

\[
 \mathfrak H_{\eta,u,Z}
 =\sum_{\boldsymbol p}
 \prod_i[W_i(q_{p_i}/P_i)q_{p_i}^{z-1}G_{p_i}]
 \prod_{p\notin S,\ p\notin\boldsymbol p}H_p.           \tag{3}
\]

全局 continuation/joins 只用 (3)，不除以 P_p 或 H_p。由原 D1 的 positive Euler majorant，删去任意 selected factors 后的 unselected product 一致为 `O_epsilon(U^epsilon)`；每个 fixed real box 的 full tuple all-height majorant 有固定 Z-degree，后选外尾阶数不能改变该 degree。

在实际 retained dynamic region

\[
 x_r=a+16e,\quad w_r=1-a-6e,\quad z_r=z_0=17/50,
 \qquad 51/100\le a\le1,\quad0<e\le10^{-3},             \tag{4}
\]

source 8908–8922 给 H_p 的离零证明：off-row `H_p-1=O(Q^{-1-10e})`，ramified `O(Q^{-10e})`。固定 e 后扩大 P0，使所有 slot primes 的 `|H_p-1|<1/2`。这是 dynamic region 内允许用 `B_p=G_p/H_p` 的准确理由，不能据此在其他 contour 使用商。

因此本区内的有限恒等式是

\[
 \mathfrak H_{\eta,u,Z}
 =\mathcal H_{\eta,u}
 \sum_{I\subseteq[K]}
 \prod_{i\in I}\mathcal D_i\prod_{i\notin I}\mathcal Q_i,
\]
\[
 \mathcal Q_i=-P_i^{z-1/2}Q_i,\quad
 Q_i=P_i^{-1/2}\sum_{p\in\mathcal P_i(Z)}
 \bar\chi_p(u)W_i(q_p/P_i)(q_p/P_i)^{z-1},\quad
 \mathcal D_i=\mathcal B_i-\mathcal Q_i.                 \tag{5}
\]

每个 `p|u` 的 main 项仍按原 symbol zero extension 为零。等式 (2)–(5) 用原同源有限操作，而不是把一个新 high integral 定义为原物理 I 的替代品。

## 3. 所有 error slots 与一个 numerator 的联合估计

该步原 `prop:probe-errors`（8852–9049）的 statement 没有 ell=1/6 前件。下面逐项确认其证明对 (4) 和任意固定有限新槽系统成立。

### 3.1 Off-row primes

源 8808–8816 的 holomorphic cancellation identity 只留下四个 error powers。令 `theta=(-w_r)_+<=6e`，得到

\[
 |H_p(B_p+\bar\chi_p(u))|
 \ll Q^{-x_r+2\theta}+Q^{-6z_0+2\theta}
 +Q^{4-5x_r-6z_0+2\theta}+Q^{1-w_r-6z_0+\theta}.
\]

四个指数分别至多

\[
 -a-4e,\quad-51/25+12e,\quad49/25-5a-68e,
 \quad a-51/25+12e,
\]

均不超过 -51/100。slot 中 O(P_i) 个 prime ideals 和 `Q^{z-1}` 给 `O(P_i^{z_0-51/100+epsilon})`。它比 central scale `P_i^{z_0-1/2}` 更小。

### 3.2 Ramified boundary terms 与 geometric tails

`p|u` 时 D=W=0，必须保留原 J_j 表，而不能拿 off-row 式代替。把每项乘 `Q^{z-1+x}` 并先分出 Q^z 后，五个 valuations 的 boundary powers 在 e=0 为

\[
 a-2,\quad1/2-2a,\quad(-a,1-3a),\quad
 1/2-2a,\quad2-5a.
\]

相应 e 改动为 `+6e,-32e,(-26e,-48e),-42e,-80e`（原 8947–8953）。整个 a,e 范围均严格小于 -1/2。common R term 的指数是 `49/25-1-5a-80e<-1/2`，后续 valuation pairs 的比值满足 `|R|<=Q^{-11/10}`、`|V|=Q^{-51/25}`，故 geometric tails 保持此界。explicit rescaling 项分出 Q^z 后为 `-1-w_r<-1/2`。

因此除下一严格 ramified 项外，所有 ramified error labels 只花 divisor-many labels 和 `P_i^{z_0-1/2+epsilon}` 的 central scale。它们不产生正 amplitude exponent。

### 3.3 严格 ramified labels 共用一次 conductor deficit

唯一剩余项是 `(e_0,l,k,m)=(1,0,1,0)`、j>=2 的
`-eta(p)(Q-1)Q^{-x-w}`。分出 Q^z 后它仅有 `Q^{-w_r}`，不能逐槽单独声称已小于 Q^{-1/2}。

令 `psi_u^*` 是 numerator `chi_bullet(u)` 的 primitive inducing character。buffered bins 同时包括 numerator 与其 conjugate，`Re(1-w)=a+6e`，高度在同一个 cumulative buffer 内，所以实际 primitive reflected value有任意 U-small-power bound；deleted Euler factors用原 lemma恢复。u=1 外每个 physical row 的 numerator非主：good ramified prime 的局部 order 为 `6/gcd(6,j)>1`；其余 physical rows是 units，原 5502–5514 的分类处理非平凡 units。这里不将 L' 的零当作 L 的零。

functional equation 的 conductor power为

\[
 A_*=1/2-w_r=a-1/2+6e>0.
\]

固定 triangle-expanded error tuple 后，令 J0 恰为其中 distinct strict ramified labels。原 coefficient-level reciprocity 和 CRT 证明（8968–9009）给一次性精确分配

\[
 q_{\mathfrak f_u}\ll_S q_{rad(u)}
 \le q_u\prod_{p\in J0}q_p^{-(j_p-1)}.                 \tag{6}
\]

所有 strict labels distinct 是物理 disjoint slots 的后果。先对整个 J0 使用 (6)，再求和，而不是每个槽重复使用 numerator 的完整 U^{A_*} 预算。恢复其余 deleted factors至多花 `U^{6e+epsilon}`；strict selected prime 本来已经在 primitive conductor 中，其局部恢复因子恰为一。

numerator 与所有 strict slots 因而一起至多为

\[
 U^{A_*+6e+\epsilon}(3+T_1)^C
 \prod_{p\in J0}q_p^{z_0-w_r-(j_p-1)A_*}
 \le U^{a-1/2+12e+\epsilon}(3+T_1)^C
 \prod_{p\in J0}q_p^{z_0-1/2},                         \tag{7}
\]

因为 `j_p>=2` 且 `-w_r-A_*=-1/2`。ramified labels 总数 divisor-many，off-row labels已有更强 saving。把 finite powers按固定 K分配，得到每个 error subset I 的完整原结论

\[
 \boxed{|L^S(w,\chi_\bullet(u))\prod_{i\in I}\mathcal D_i|
 \ll U^{\delta/2+O(e)+\epsilon}(1+T_1)^C
 \prod_{i\in I}P_i^{z_0-1/2+O(e)+\epsilon}.}           \tag{8}
\]

empty I 也是同一个 reflected numerator bound。新 ell 不进入上述 conductor 分配；不会多出一个 numerator power，也不会把 strict labels 误归入 main amplitude。

## 4. Mixed main/error sets、actual counts 与 central g

按原 15064–15090，在固定 dynamic bin、固定 retained physical参数和每个 error subset I 上分幅度：main slots 的 `g_i in[0,delta/2]`、`|Q_i|<=P_i^{g_i+theta_amp}`，error slots恰定义 `g_i=0`，不要求它们有 lower spike。令

\[
 q=\frac{\sum_{i=1}^K\ell_i g_i}{\ell_1}\in[0,\delta/2].
\]

分母包括所有 physical slots；不能改为 main slots 的总长度。由 (8)、main bounds 及 `mathcal H<<U^epsilon`，得到

\[
 |L^S(w,\chi_\bullet(u))\mathfrak H^{(I)}_{\eta,u,Z}|
 \ll U^{\delta/2+O(e)+\epsilon}(1+T_1)^{A_1}
 Z^{\ell_1(z_0-1/2)+q\ell_1+O(e+\theta_{amp}+\epsilon)}. \tag{9}
\]

这证明实际 central-accounting 里的 **g=q ell1**；不是 dq ell1，也不是 error labels 的 conductor长度。即使 I是所有slots、q=0，该步仍成立；count使用 actual witness/no-slot cases，不虚构不存在的 positive main factors。

对应的 actual count proof必须使用原 witnesses、marked/plain moments、sixth-power amplification和 fixed coefficient class。逐源 15110–15446 核对后，与 effective-kappa报告一致：在 `d>=1/2` 的非floor bin，对每个 actual pointwise amplitude/witness set C，有

\[
 \#C\ll U^{R_*(\delta,x)+\epsilon}(1+T_1)^{A_2},
 \quad x=q/\delta,                                   \tag{10}
\]
\[
 D_x=3-17x/9,\quad P_x=(2-8x/9)(1-x),\quad
 J=(5/6-\delta)D_x+\delta P_x,
\]
\[
 T=1+\delta P_x/(2J),\qquad
 R_*=1-\delta+(5/6-\delta)\delta P_x/(2J).              \tag{11}
\]

这里实际 admissible plain parameter是 kappa_eff=3/4，故 (10) 没有正容量替换损失；(10) 不是未支付的 nominal count。选择所需 prime factors时，whole positive main slots 保持相对共同 presentation的 coefficient `bar(nu)1_T`；plain moment对两个 witnesses和全部 selected slots整体共轭。error slots的 g_i=0只降低 spike gain，不改变 primitive family。prime coefficients不能变成 row-dependent；所有 original masks保持。strict inverse第二 width有独立下界9/37，small/zero capacities必须用no-slot moments。

供给和 mesh 来自 actual长度 `ell1/d`；
`ell1/h1-7/37=57659/3607833>0`，并且

\[
 0<\zeta<5\ell_1-h_1=2521/120000
 \quad\Longrightarrow\quad \ell_1/(h_1+\zeta)>1/5>7/37. \tag{12}
\]

fixed decrements之后选有限 K，使 `2ell1/K` 同时小于原 uniform plain mesh、rounding预算和1/185。原 physical disjoint windows和 amplifier pool 分离可照原实际构造。原S-supported exceptional rows是有限集；在 U>=Z^{1/2} 时以 fixed-target阈值排除，仍留在outer/bounded physical rows里处理。

floor无actual witness保证，独立用ideal count R=1。`d_min<=d<=1/2` 的非floor rows用原无slot t=1 actual count `R<=1-2delta/3+epsilon`，没有prime-supply假设。

**whole-bin移动顺序不可颠倒。** 先用 (3) 和 holomorphy移动原固定 bin，再在 retained points按 I、amplitudes、witnesses分点态集合。这里只估计原可积分full row sum，不能分别 continuation或积分一个由contour决定的子集合。所有 auxiliary Mellin/Fourier frequencies 使用同一累计 T1/2 allocation；完整pointwise bounds包括其global/absolute-line discarded pieces。

## 5. 正确参考指数及端点 certificate

新 sigma1版本的原 common accounting 在(9)(10)下给

\[
 E_\sigma(d;R,q)
 =a-\sigma+h(z_0-1/6)-a l_y-\ell/2+q\ell
   +d(R+\delta/2-z_0).                                \tag{13}
\]

原 lemma 陈述写 sigma0>=7/8；其 full-bin proof只用D1、a<=beta_*、buffered reciprocal和all-height correction。逐读5808–5896，没有独立7/8数值障碍。此处重放该证明，而不是直接引用范围外的 statement。测试的 all-height/joins bounds固定degree；(13)是新的同源记账身份。

将 z=1/6的固定留数和变量几何代入，独立得到

\[
 E_\sigma(d)=K_\sigma+(1/2+\ell)\delta+\ell q-h(1-R)
 +(d-h)(R+\delta/2-17/50),
\]
\[
 \boxed{K_\sigma=2/3+\ell+b/6-\sigma.}                 \tag{14}
\]

沿 `sigma(ell)=11/12-ell/4`，故
`K=-1/4+5ell/4+b/6`。ell1时 K=-997/48000。
旧 ell0=1/6、sigma0=7/8、h0=13/16 的完整 algebraic certificate（15994–16072）给

\[
 E_{\sigma_0}(h_0;R_*)\le-c_*,\qquad c_*=49/440640.    \tag{15}
\]

该 certificate是显式多项式身份，仅调用其代数，不调用固定几何 high theorem或其未重放的 actual counts。对同一 delta,q,R*，(14)准确给

\[
 E_{\sigma_1}(h_1)-E_{\sigma_0}(h_0)
 =t_0(-1/4+\delta+q+3R_*/2).                           \tag{16}
\]

`2D_x-3P_x=4x(11-6x)/9>=0`，且J>0，所以 `1-delta<=R*<=1-2delta/3`。由q<=delta/2、delta<=5/6，(16)的系数至多 `5/4+q<=5/3`。因此全部actual endpoint pairs满足

\[
 \boxed{E_{\sigma_1}(h_1;R_*)\le-m_{ad},\qquad
 m_{ad}=c_*-5t_0/3=307/11016000>0.}                   \tag{17}
\]

**signed-gap核对。** (17)已经相对 C(sigma1)，其导数(16)已含 `-sigma'(ell)=1/4`。不能再扣1/80000。若固定旧reference sigma0=7/8，正确变化系数为 `-1/2+delta+q+3R*/2`，然后换至sigma1恰加 t0/4，得到同一(16)。比较principal C(beta*)时只需

\[
 E_{\beta_*}(d)=E_{\sigma_1}(d)-\Delta_1,\quad\Delta_1>0. \tag{18}
\]

这消除了“为稳妥再扣一次旧边界变化”的参考幂错误。

## 6. 全部 moderate d、floor 与上端扩展

取 d_min=1/100。以下是 actual pair的uniform包络，不是假设同一pair一定在h1对应的实际dyad出现。

### 6.1 Selected range：1/2<=d<=h1

替actual count exponent为(10)的R*上界，requested losses另记。频率slope满足

\[
 R_*+\delta/2-17/50\ge33/50-\delta/2>0.
\]

因此每个delta,q下(13)随d增加，h1的uniform certificate (17)控制整个区间。R*也不依赖d或ell；新ell只负责确保actualslots供给。

### 6.2 Floor：a=51/100

令delta0=1/50、R=1、q<=delta0/2。直接代(14)给

\[
 E_{\sigma_1}(h_1)\le-7/1200+(32/25)t_0
 =-4327/750000<0.                                    \tag{19}
\]

slope为67/100>0，所以覆盖所有d<=h1。floor使用actualidealcount，不套有witness前件的R* theorem。

### 6.3 无selectedslots的中间范围：d_min<=d<=1/2

采用覆盖floor和非floor的共同actualupper count
`R=76/75-2delta/3`、q<=delta/2。其slope是 `101/150-delta/6>0`，所以只需查d=1/2。沿sigma(ell)且d固定时，(13)变化系数准确为

\[
 13/50+\delta/4+q\le177/200.
\]

原中间代数上界 `-49/14400` 因而变为

\[
 \boxed{E_{\sigma_1}(d)\le-49/14400+(177/200)t_0
 =-120907/36000000<0.}                                \tag{20}
\]

每个physical slot仍留在full high correction中；“无selectedslots”只说没有把其额外因子用于rowmoment，不是删掉correction。

### 6.4 h1<d<=h1+zeta

所取 R*=uppercount时，slope至多33/50；floor为67/100。统一以2为上界即可。取

\[
 0<\zeta<\min\{2521/120000,\ m_{ad}/16,\ 1-h_1\}.      \tag{21}
\]

则supply保持(12)，所有endpointexponents最多增加2zeta<m_ad/8。故全moderate范围在adjustablelosses之前有统一正saving，至少 `7m_ad/8`；floor/intermediate余量更大。可明确选择 `zeta=m_ad/32=307/352512000`，此时upperextension还留 `15m_ad/16=307/11750400`。

## 7. Uniform losses、outer/principal接口及物理 high 合同

central-accounting的显式real losses仍为

\[
 (16-6l_y)e+(1+d)\epsilon_c+d\epsilon_d+\epsilon_p,
\]

其中epsilon_c包括joint-errorbound、amplitudewidth、实际countloss，且d在固定compact range。全部系数对target一致有界；K固定后，2^K error subsets和finite amplitude bins是固定乘数，witness/dyadic choices仅有固定logarithmic multiplicity。

选择顺序可重放原16191–16453，必须保留以下具体前件：

1. 指定count/rounding/moment losses小于m_ad的固定小份；先选capacitydecrements和plainuniformmesh，再选fixed even K与actualdisjointwindows。actualannularoffsets仅在正strictmargins之后由threshold吸收。
2. K及positive min ell_i固定后，再选amplitudewidth、prime-bin preliminarypowers和e。由原15064–15070的 `d/ell_i` 有界，U-small-powers可吸收到各P_i的bin allowance。原detector-dyads的e0只依赖prescribedloss及boundedactual lengths（4398–4400），可在target前取；pre-saturation ranges也须保留。
3. centralreal总损失和logarithmic/normalizerallowance选在m_ad/4内。principal预先选择 `0<mu<sigma1 min ell_i`；它是新的正确localdecayσ1，不静默沿用7/8。其e/principal-loss小于 `min(l_y/20,h1/600,mu)/4`。
4. fixedtarget后才固定arithmetic datum、allinternalmoments/seminormorders和统一有限height exponent A_eta。每个primitive/bufferedargument使用同一cumulativefrequency矩阵与T1/2预算，不能在下一估计更新预算。
5. 取tau>0同时小于d_min/100、原detectorheightceiling和已留highmargin除以固定A_eta。于是T1=Z^tau满足所有literal U-small-powerheightconditions。最后选择外尾orderN和threshold；提高N仅增加externaltestseminorms，不改变internalA_eta、fullarithmeticdegreeB_eta或slotmesh。

原fulltuple的绝对selectedG bounds也可在新几何保留：小行global线用D1(1/3)，不是原已不自动满足的D1(3/8)；G_p off-row O(1)、ramified O(Q^{1/2})，positive fulltuple `<<U^epsilon Z^{17ell1/50}`。独立数值为

\[
 h_1(17/50-1/6)-l_y/2=-197449/2000000,
\]
\[
 \text{small sum relative to }C(\beta_*)
 \le-172249/2000000+small\quad(d_{min}=1/100).           \tag{22}
\]

这单独覆盖d<d_min以及boundednontrivialunits；中间(20)不用于这些rows。大行 `(s,w,z)=(2,2,z_infty)` 的selected G均O(1)，fulltuple给 `U^epsilon Z^{ell1 z_infty}`。固定(21)后选足够大的fixedz_infty>2，原large sum exponent
`B0+(h1+zeta)(1+epsilon)-zeta z_infty+epsilon`，`B0=132497/80000`，可低于C(sigma1)任意指定saving。

principal部分另有同源normalizer和余留数接口（shared-contour报告已按actualfulltuple付清）：`m_w=l_y/20=57497/2400000`、`m_z=h1/600=32503/24000000`、mu>0，normalizer逆只有subpowerloss。令这些固定余量、m_ad及(22)余量的四分之一之最小为m>0，按上述顺序留height与tail预算，即可获得实际物理合同

\[
 \left|\frac{I_{modified}(Z)-\mathscr P_{principal}(Z)}{c_SA_T(Z)}\right|
 \ll_{\eta,N} Z^{C(\beta_*)-m}(1+T_1)^{A_\eta}
             +Z^{B_\eta}T_1^{-N}.                    \tag{23}
\]

这里physicalI、sameS下的A_T、principal signal都不包含analysisheightT1。先定internalA/B，再选tau和N；外尾closure将(23)变为固定正saving的high比较。原441的low估计可另选epsilon<Delta1，low/high使用同一个normalizer。该组合仍明确条件于通用[R]而非AF平均比例；67.25%没有被用来减少坏行数。

## 8. 检查结果与范围

独立BigInt有理计算9项断言通过：K_sigma1、sigma1、m_ad、floor、中间、smallconstant、精确/粗smallsum和supplyextension。具体数值已写(17)、(19)–(22)，不是以浮点margin代替符号证明。

没有发现centralerror-slot、mixedmain/error或全moderate-frequency范围的新实质障碍。关键原范围问题已有具体付款：sigma0<7/8的contour声明按D1证明重放；kappa<3/4不用未声明recursive theorem而取kappa_eff=3/4；实际count采用(10)而非未付nominalR；reference变动已计入(16)，不得再次扣旧边界变化。

本报告的“已支付”限于所列原算术 identities、fixed-familyL bounds、witness、marked/plain/recursive moments、sixth-poweramplification及全Hecke7/8 bootstrap作为[R]输入。它给新的same-sourcehigh推导；不独立验收整篇来源、不声称Lean内核验收，也不在本报告中单独进行continuation结论或Weil/RH几何桥认证。
