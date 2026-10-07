# 原 actual31 的非交替符号大小 gate：双向 crossing 与完整高度恢复

2026-10-07。作者 twisted_research。状态：新完整推导，待独立全文审查。
仅新增本报告；不修改既有笔记、论文、审查、math、脚本、output、Goal 或 Git。

本次付清一个具体的 **actual finite 31 子扇区**：三个 high 步中只要有
相邻同号，物理四词准确为空；在下述大小 gate 内，原有限 carrier 的
三个内部投影也可完整付款，所以该实际有限词为 o(d)。包含全部原
genuine-prime 标签，不先剔重复标签，不假定未知 high 第四矩有界。
它没有支付交替符号、整个31、distinct22或467的实际 q/k 前件。

## 1. 原对象、输入与精确范围

沿用 [461](../../notes/461-original-one-high-three-low-fourth-trace.md)
的原 AF frame，记

\[
 X=T/(2\pi),\quad L=\log X,\quad Z=\sqrt X,\quad
 d=\lfloor XL\rfloor,\quad I=[-L/2,L/2],\qquad
 Ee_k=L^{-1/2}1_Ie^{i\tau_ku},\quad \tau_k=T+2\pi k/L,
 \quad P=EE^*,\quad Q=1-P.                              \tag{1}
\]

原 even C² taper 是 phi，支撑 I，0<=phi<=1；其二阶导数的 L¹
界一致，a_L=L^{-1}||phi||²有固定正下界。平移先零延拓到实线，
R_sf(u)=f(u+s)。这里 P 是 interval 上的原 finite-carrier 投影；
它不是全实线连续频带投影，不能与下面的高度截断交换。

对真实 prime range R 和 epsilon=+1 或 -1，定义单向部分

\[
 b_p=\frac{\log p}{a_LL\sqrt p},\qquad
 B_R^\varepsilon=-\sum_{p\in R}b_pM_\phi
                    R_{\varepsilon\log p}M_\phi,
 \quad C_R^\varepsilon=E^*B_R^\varepsilon E.
                                                               \tag{2}
\]

因此 (B_R^epsilon)*=B_R^{-epsilon}，而原 real cosine channel为
B_R=B_R^++B_R^-。单向部分通常不自伴，以下 crossing proof保留双方。

固定 alpha_i in (1/2,1]（i=1,2,3）与 gamma in (0,1/2]。
每个 R_i 是 (X^{beta_i},X^{alpha_i}] 内的 primes，
1/2<=beta_i<alpha_i；R_4 是 (X^{beta_4},X^gamma] 内的 primes，
0<=beta_4<gamma，也允许完整低前缀 p<=X^gamma。
固定有限个这样的 intervals之并亦可，常数依赖其固定个数。
**不准入任意 prime mask 或随 T 增长的区间分割。**

只使用 [446](../../notes/446-uniform-prime-twists-on-the-original-gabor-frame.md)
的 conductor-one sharp-prime 后果：固定 [R] zero-free theta 和
fixed-gap logarithmic-control，先固定 theta<a<1、a>1/2，再令 T趋于无穷。
本次具体例仅需旧 theta=7/8。没有重新认证整个外部原稿，亦没有将
canonical prefix输入施加到任意 moving coefficients。

| 冻结输入 | canonical SHA256（CRLF及lone CR转LF，不trim） |
|---|---|
| [446](../../notes/446-uniform-prime-twists-on-the-original-gabor-frame.md) | `08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf` |
| [461](../../notes/461-original-one-high-three-low-fourth-trace.md) | `f9fdf0b721c76a5cc4c4e4821748007e62975286417e6bec9700e39b6778170b` |
| [463双侧高度](../../notes/463-two-sided-height-stability-for-original-fourth-words.md) | `6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90` |
| [原有限频带桥](hybrid-one-three-finite-band-admission-research.md) | `bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f` |

已读 highGram 与 wholecompression 的实际 signed/positive 结构；本次不以
其中增长上界或未知 whole fourth有界作为前件，也不从正方差分解推得
本次不同符号路径相消。

## 2. 单向 canonical 带内界与双方泄漏

unitary Fourier取 Ff(t)=(2pi)^(-1/2)int f(u)e^(-itu)du。准确乘子是

\[
 D_R^\varepsilon(t)=-\sum_{p\in R}b_pp^{i\varepsilon t},
 \qquad B_R^\varepsilon=M_\phi\mathcal F^{-1}
                       M_{D_R^\varepsilon}\mathcal F M_\phi.
                                                               \tag{3}
\]

置 J=[T/2,3T]，D_i^g=D_{R_i}^{epsilon_i}1_J，
B_i^g=M_phi F^{-1}D_i^g F M_phi，C_i^g=E*B_i^gE。
sharp prefix由446 (4)、principal项及prime-power difference给，在±J上

\[
 q_i:=\|D_i^g\|_\infty\ll_a X^{\alpha_i(a-1/2)}L
 \quad(i=1,2,3),\qquad
 q_4\ll_a X^{\gamma(a-1/2)}L.                            \tag{4}
\]

每个 high interval是两个实际前缀之差。负方向由原实系数的共轭同样
成立，不改变角色族。principal项 sqrt(Y)/T及prime-power差 O(log Y)
均包含后才吸收进 (4)。使用原 L归一化，不换成 log Y。
全局 ||B_i^g||<=q_i，且其伴随的 multiplier为 overline(D_i^g)，
支撑仍是 J，不是 -J。

原有限频带桥的 (13)–(16)只用乘子绝对上界和 Minkowski，完全不需要
自伴。因此对每一个单向 factor及其伴随同时有

\[
 \ell_i:=\|QB_i^gP\|_2\ll\sqrt Lq_i,\qquad
 \ell_i^*:=\|Q(B_i^g)^*P\|_2\ll\sqrt Lq_i.               \tag{5}
\]

具体地，在 I上完整 Fourier e_j基中，outside j的每个差 n=j-k有
min(d,|n|)个 k；其实际矩阵核为

\[
 (B_i^g)_{jk}=\frac1{2\pi L}\int
 \overline{\widehat\phi(\xi-2\pi(j-k)/L)}
 D_i^g(\tau_k+\xi)\widehat\phi(\xi)\,d\xi.              \tag{6}
\]

shifted-grid energy W_L(xi)<=C(log L+L|xi|)和
int |xi|^{1/2}|hat phi(xi)| dxi=O(1)给 (5)。
输出始终支撑 I，所以 Q不存在漏掉的实线 I^c部分。
sharp 1_J无需平滑；这里只使用真实 global q_i。

## 3. 非自伴四词的两次 crossing 引理

令 V_i 任意 bounded算子，y_i=||V_i||，ell_i=||QV_iP||_2，
ell_i*=||QV_i*P||_2，P有限rank。则

\[
 \left|\operatorname{Tr}(PV_1V_2V_3V_4P)
 -\operatorname{Tr}(PV_1PV_2PV_3PV_4P)\right|
 \le\sum_{i<j}\ell_i^*\ell_j\prod_{k\ne i,j}y_k.        \tag{7}
\]

证明：逐次插入三个 P，差恰为

\[
 \operatorname{Tr}(PV_1QV_2V_3V_4P)
 +\operatorname{Tr}(PV_1PV_2QV_3V_4P)
 +\operatorname{Tr}(PV_1PV_2PV_3QV_4P).                 \tag{8}
\]

直接在相邻位置插入 P+Q，递归有

\[
 \|QV_2V_3V_4P\|_2
 \le\ell_2y_3y_4+y_2\ell_3y_4+y_2y_3\ell_4,
 \quad\|QV_3V_4P\|_2\le\ell_3y_4+y_3\ell_4.            \tag{9}
\]

第一项左 factor PV_1Q 的 HS norm为ell_1*；第二项左边最多
y_1ell_2*；第三项左边最多y_1y_2ell_3*。分别作HS–HS trace配对，
得到 (7)的六项。没有用 ||[P,V]||_2=sqrt(2)ell这样的自伴恒等式。

对 V_i=B_i^g，令 s=alpha_1+alpha_2+alpha_3+gamma，置

\[
 \eta=1-(a-1/2)s>0.                                   \tag{10}
\]

(4)、(5)、d asymp XL给原 finite 与 physical 的 good比较

\[
 d^{-1}\left|\operatorname{Tr}(C_1^gC_2^gC_3^gC_4^g)
 -\operatorname{Tr}(E^*B_1^gB_2^gB_3^gB_4^gE)\right|
 \ll\frac{L\prod_iq_i}{d}\ll X^{-\eta}L^4=o(1).         \tag{11}
\]

这正是需要支付的三个内部 P。未使用任意别的 four-word均值。

## 4. 原 raw/good 双侧恢复覆盖 complex directions

463的证明虽首先陈述原real prime channels，但其每一步是 bounded
diagonal multiplier的绝对范数与HS–HS配对。下面记录对本次复乘子的
完整适用性，避免从real statement直接跳到单向词。

设 V=F M_phi E、K=F M_phi² F^{-1}，m_i=||D_i||_infty。
全高度 Chebyshev给

\[
 m_i\ll X^{\alpha_i/2}/L\ (i\le3),\qquad
 m_4\ll X^{\gamma/2}/L.                                \tag{12}
\]

有限 factor差是

\[
 C_i-C_i^g=(1_{J^c}V)^*D_i^b(1_{J^c}V),\qquad
 \|C_i-C_i^g\|_1\ll m_i/T^2.                           \tag{13}
\]

这里 D_i^b=D_i1_{J^c}允许 complex；用
||A*DA||_1<=||A||_2²||D||即可。四词逐因子替换且其余
raw/good op<=m_j，得到 finite trace差 O(T^-2 product m_i)。

physical词准确为 V*D_1KD_2KD_3KD_4V。每个替换项在 D_i^b处
切开，D_i^b=1_{J^c}D_i^b1_{J^c}，两边均有bad guard。
左边取反向伴随链，右边取原suffix；各含至多三个 K。
463 (3)–(5) 的双侧逃逸 proof对这两链都给
HS<=T^-1乘对应乘子op之积。共轭改变值而不改变height support、
绝对上界或near-jump support，所以complex方向不产生额外项。
由此两种比较分别满足

\[
 \begin{aligned}
 &|\operatorname{Tr}(C_1C_2C_3C_4)
              -\operatorname{Tr}(C_1^gC_2^gC_3^gC_4^g)|\\
 &\quad+|\operatorname{Tr}(E^*B_1B_2B_3B_4E)
              -\operatorname{Tr}(E^*B_1^gB_2^gB_3^gB_4^gE)|
 &\ll T^{-2}\prod_i m_i.
 \end{aligned}                                          \tag{14}
\]

其normalized费用为

\[
 \ll X^{s/2-3}L^{-5}.                                  \tag{15}
\]

由于s<=7/2，这始终o(1)。特别不能在 raw tau≈0使用 (4)；
那里的principal峰已经由 (12)及两端packet逃逸支付。
也没有假设1_J与P交换。

## 5. 空物理 signs 得到真正 actual 子扇区

若 epsilon_1=epsilon_2，任意两个high标签 p,q满足
log p+log q>L；同向两步要求 u、u+epsilon log p、
u+epsilon(log p+log q)同时在 I内，这是不可能的。
故 B_1^{epsilon_1}B_2^{epsilon_2}=0。
若 epsilon_2=epsilon_3，同样 B_2^{epsilon_2}B_3^{epsilon_3}=0。
其余两 factors及其标签不影响这个准确零。

因此只要三个high方向不是交替的，原physical四词为零。
16个完整signature中12个满足该条件；仅余
(+,-,+,±)及(-,+,-,±)四个交替high signatures。
将 (11)、(14)接回同一raw对象，严格得到

\[
 \boxed{\frac{|\operatorname{Tr}
 (C_{R_1}^{\varepsilon_1}C_{R_2}^{\varepsilon_2}
  C_{R_3}^{\varepsilon_3}C_{R_4}^{\varepsilon_4})|}{d}
 \ll X^{-\eta}L^4+X^{s/2-3}L^{-5}=o(1)}                \tag{16}
\]

前件是 (10)及至少一个相邻high同号。它是原actual词的结论，
包含复carrier、所有内部 P、全部高度和 genuine-prime coefficients。
原factorized range sum里重复与distinct标签同时保留。
本证明不把任意distinct-only删标签后的对象当成另一个canonical prefix。

在原finite矩阵中可以普通迹循环，将四个low placements逐一转成
low在末位的形式后使用 (16)；high的次序随这次实际循环确定。
这一操作只在有限矩阵中做，没有free cyclically rotate物理trace。

## 6. 一个用旧7/8输入的具体 partition

取固定a=22/25，gamma=1/2，并将真实high range划成

\[
 R_t=(X^{1/2},X^{11/20}],\qquad R_b=(X^{11/20},X].      \tag{17}
\]

当三个high标签至多一个落在R_b时，完整range partition恰为
(t,t,t)、(b,t,t)、(t,b,t)、(t,t,b)四个factorized words。
所有这些词可统一取 s<=1+11/20+11/20+1/2=13/5；于是

\[
 \eta\ge1-\frac{19}{50}\frac{13}{5}=\frac3{250},
 \qquad s/2-3\le-\frac{17}{10}.                        \tag{18}
\]

这四个range words的12个非交替signatures（及四个actual low位置）
总贡献由绝对三角不等式为
O(d X^{-3/250}L^4+d X^{-17/10}L^{-5})=o(d)。
有限项数固定，不用把全四词的prime L¹质量作为任何P错误的付款。
这是实际31 partition中有明确标签内容的新增已付块，不是仅说明物理零。

## 7. 尚未付款与量词

本结果仍留开：同一capped范围内的四个交替high signatures；(17)中
至少两个bulk标签的非交替或交替signatures；以及完整31 signed净预算。
交替路径可有真实high²对high×low近共振，物理支持不会自动消失。
对不满足 (10)的块，(11)没有节省，即使其物理词为零，也不能
由此推出实际有限词小量。原entire22及467实际q上界/k下界亦仍未支付。

顺序是先固定原profile、[R] theta、gap a、所有caps及固定区间个数，
再令T趋于无穷；隐常数允许依赖这些固定数据，不依赖当前prime标签、
carrier row或T。没有选择目标后再改变窗、截断prime系数或R族。
这不产生新的whole第四矩常数、临界线比例、无零区域或RH结论。
