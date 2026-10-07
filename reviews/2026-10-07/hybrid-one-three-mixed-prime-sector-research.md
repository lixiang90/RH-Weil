# 原有限 AF 矩阵的 13/31 混合项：全部重复指标小量与 distinct 余额

2026-10-07。作者：`twisted_research`。只读确认起点为已推送提交
`502463775b1ba2a7d4aab65e1b55f3fbe775d7de`，开始时工作区干净。
只新增本报告；旧论文、notes、脚本、output、既有报告和 math 未修改。
本轮未派子代理，也未操作 Goal 或 Git。

本次真实付款为：原 finite matrix 的 `4Tr C_H C_L³` 和 `4Tr C_H³ C_L`
中，三个同范围 genuine-prime 指标只要出现重复，其**整个有符号子族**
均为 `o(N)`，包含全部排列、内部 P、carrier 和远端 alias。
不是只在某个 near-composite 区间得到形式估计。
因此这两个完整 sector 可准确约化到三个同范围指标彼此不同的 sum：

\[
 \boxed{M_{13}=4D_{13}+o(d),\qquad M_{31}=4D_{31}+o(d).}
 \tag{1}
\]

下文定义实际有限对象 `D_13,D_31`，给出其保持所有 P 的 Fourier-walk
精确表示及可检验的投影余额。**两个 distinct sum 尚未支付为 O(d) 或 o(d)**。
没有完整四迹常数、新零点比例、零自由区或 RH 结论。

## 1. 原模型和输入绑定

采用 [AF v2 §2](https://arxiv.org/html/2608.13637v2#S2) 的原窗、carrier、
grid 和完整物理零延拓。令

\[
 X=T/(2\pi),\quad L=\log X,\quad Z=\sqrt X,\quad d=\lfloor XL\rfloor,
 \quad \tau_k=T+2\pi k/L\ (0\le k<d),\quad I=[-L/2,L/2].
 \tag{2}
\]
\[
 Ee_k(u)=L^{-1/2}\mathbf1_I(u)e^{i\tau_ku},\quad P=EE^*,\quad Q=1-P,
 \quad R_sf(u)=f(u+s).
 \tag{3}
\]

每次平移均先将函数零延拓到实线。真实偶 C² taper为

\[
 \phi(u)=\chi(L/2+u)\chi(L/2-u)\sqrt{\psi(u/L)},\quad
 a_L=L^{-1}\|\phi\|_2^2\to a_\psi>0,
 \tag{4}
\]
\[
 b_p=\frac{\log p}{a_LL\sqrt p},\quad
 B_p=-b_pM_\phi(R_{\log p}+R_{-\log p})M_\phi,\quad C_p=E^*B_pE.
 \tag{5}
\]

H指 `Z<p<=X`，L指 `p<=Z`；这里只讨论 genuine primes。
`B_R=sum_(p in R)B_p`、`C_R=E*B_RE`、`mathcalD_R=sum_(p in R)C_p²`。
unitary Fourier下仍是原 `2pi/(a_L L)` 乘子压缩；未改变 normalization。
仅在最后使用 `d/N(T,2T)→1`。

| 本地前置证据 | SHA256，文本按 CRLF→LF |
|---|---|
| [原高素数报告](hybrid-high-prime-four-word-response-research.md) | `988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666` |
| [22重复混合报告](hybrid-low-high-mixed-four-word-research.md) | `71f62b2dd931cfda012e7dad9c4efcfece63f5cf1bb8ff5b466d3e2ac1ae89f9` |
| [454](../../notes/454-original-background-and-weighted-prime-mixed-traces.md) | `8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7` |
| [AF v2 PDF](../../literature/baseline/2026-alpoge-furman-6725-v2.pdf) | `6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444`，二进制 |

本次新增 near-square estimate 只用素数模数下二次同余每个非零值至多有2个根，
及整数 harmonic sum；这是域中二次多项式根数的初等证明，不借新的分布定理。
其余沿用明确 Chebyshev–Mertens 与已支付的 finite crossing、二矩。
不需要零自由包 [R]、素数对相关、平均比例或 full fourth 前件。

## 2. 完整 mixed sector 的 finite partition

对三个标签范围R、另一个标签范围S（R,S为L,H中的相反两个），定义

\[
 A_{R,S}=\operatorname{Tr}(\mathcal D_R C_R C_S),\quad
 O_{R,S}=\sum_{p\in R}\operatorname{Tr}(C_p C_R C_p C_S),\quad
 T_{R,S}=\sum_{p\in R}\operatorname{Tr}(C_p^3C_S).
 \tag{6}
\]

三个R标签的重复子族在 `Tr C_R³ C_S` 中是准确的 pair inclusion–exclusion：

\[
 U_{R,S}=2\operatorname{Re}A_{R,S}+O_{R,S}-2T_{R,S}.
 \tag{7}
\]

前两个 adjacent equalities分别给 A和其共轭；opposite equality给O。
三个 pair intersections全是T，所以系数 `-3+1=-2`。
O、T均为实数，因为 `C_p C_R C_p`、`C_p³` 和 C_S为Hermitian。
在实际有限矩阵中普通迹循环合法，四个S位置故给 `4U_R,S`。

准确 distinct sum为

\[
 D_{R,S}=\sum_{\substack{p,q,r\in R,\ p\ne q,\ q\ne r,\ r\ne p}}
          \ \sum_{s\in S}\operatorname{Tr}(C_pC_qC_rC_s),\quad
 D_{13}=D_{L,H},\quad D_{31}=D_{H,L}.
 \tag{8}
\]

这里 (8) 要求三个R标签两两不同；四个标签自然全部不同。
`Tr C_R³C_S=D_R,S+U_R,S`。本报告将证明

\[
 |U_{L,H}|+|U_{H,L}|
 \ll_{\chi,\psi}d\left\{
       \frac{\sqrt{\log(2+L)}}{L^{3/2}}
       +X^{-1/4}L^2+L^{-3}\right\}=o(d).
 \tag{9}
\]

从而(1)是关于 whole actual sectors 的准确约化，不声称D已支付。

## 3. 共同 finite estimates 与 Y≠Z 的重复投影引理

令 `ell_0=log(2+L)`。原报告和22报告给

\[
 \sum_{p\in R}b_p^2=O(1),\quad
 \sum_{p\in H}b_p\ll\sqrt X/L,\quad
 \sum_{p\in L}b_p\ll\sqrt Z/L,
 \tag{10}
\]
\[
 \|B_H\|\ll\sqrt X/L,\quad\|B_L\|\ll\sqrt Z/L,\quad
 \|QB_pP\|_2\ll b_p\sqrt{\ell_0},
 \tag{11}
\]
\[
 l_H:=\|QB_HP\|_2\ll\sqrt{X\ell_0}/L,\quad
 l_L:=\|QB_LP\|_2\ll\sqrt{Z\ell_0}/L,\quad
 \|B_HP\|_2+\|B_LP\|_2=O(\sqrt d).
 \tag{12}
\]

最后一个二矩已独立支付，不从未知四矩推回。低B_p norm≤2b_p、高≤b_p。
以下只需吸收这一绝对因子2。

令 repeated `A_i=A_i*` 满足 `a_i=||A_i||<<b_i`、
`l_i=||QA_iP||_2<<b_i sqrt ell_0`、`sum b_i²=O(1)`。
Y、Z为B_H、B_L中的相反两个；写 `y=||Y||,z=||Z||`、
`Y_2=||YP||_2,Z_2=||ZP||_2`。准确逐次删除三个 internal P给

\[
 \left|\sum_i\operatorname{Tr}(PA_iPYP A_iPZP)
       -\sum_i\operatorname{Tr}(PA_iYA_iZP)\right|
 \ll Z_2l_Y+yZ_2\sqrt{\ell_0}+Y_2l_Z+yl_Z\sqrt{\ell_0}=o(d).
 \tag{13}
\]

三个差额依次有单项 bounds
`a_i² Z_2 l_Y`、`a_i y Z_2 l_i`、
`l_Z(a_i²Y_2+a_i y l_i)`。
最后使用 `YA_iP=YP A_iP+YQ A_iP`；右P和右伴随均保留。
按平方重复权重聚合得到(13)，最大费用
`O(X sqrt(ell_0/L)+X^(3/4)ell_0/L²)=o(d)`。
这里Y≠Z，不将22报告中两个相同Y直接替换而省略证明。

adjacent引理也保留这两个不同因子。令 `D_phy=sum A_i²`，
`||D_phy||=O(1)`、`||QD_phyP||_2=O(sqrt ell_0)`；
`E*D_phyE−sum(E*A_iE)²` 为positive、trace O(ell_0)。则

\[
 \operatorname{Tr}\big[(\sum_i(E^*A_iE)^2)(E^*YE)(E^*ZE)\big]
 =\operatorname{Tr}(E^*D_{\rm phy}YZE)+o(d).
 \tag{14}
\]

误差分别为 `yz ell_0`、`z l_Y sqrt ell_0`、
`l_Z(l_Y+y sqrt ell_0)`；其和
`O(X^(3/4)ell_0/L²)=o(d)`。
这一证明先以positive trace换D，再删 D–Y 和Y–Z之间的P，
不在带末端P的物理迹中免费循环。

## 4. 全部 physical carrier 与 near/far cutoff

准确核仍是

\[
 K_d(t)=d^{-1}\sum_{k=0}^{d-1}e^{i\tau_kt}
 =e^{i[T+(d-1)\pi/L]t}\frac{\sin(d\pi t/L)}{d\sin(\pi t/L)}.
 \tag{15}
\]

每个真实四词在P删除后为
`d product b_i sum_sign K_d(S) <W>`，
`W=phi(u)phi(u+S) product_(j=1..3)phi(u+S_j)²`。
所有累计位置都须在I；最终位移S的 endpoint overlap至多 `L−|S|`。
因此统一有

\[
 \langle|W|\rangle\le(L-|S|)_+/L,\qquad
 \log2\le|S|\le L\ \Longrightarrow\
 |K_d(S)|\langle|W|\rangle\ll1/X.
 \tag{16}
\]

`|S|>=L` 时为空（端点等号权重为0）。(16)明确支付接近 ±L 的 alias；
没有把它误套成小差频率。所有以下 far sums都使用已积分的物理权重。
乘一个 uniformly bounded local symbol不改变这个结论。

near 指 `|log(m/n)|<=log2`。此时无grid alias，准确有限核有

\[
 |K_d(\log(m/n))|\ll
       \min\{1,\max(m,n)/(X|m-n|)\}\quad(m\ne n).
 \tag{17}
\]

这是绝对bound，carrier保留在(15)而未被删除。
只在near使用(17)，其余部分统一按(16)求和。

## 5. 三个新 near arithmetic estimates

### 5.1 高低单素数差频率

near `q<=Z<r`、`r/q<=2` 时，`q>=Z/2,r<=2Z`，
`b_qb_r |K_d(log(q/r))|<<1/[X|r-q|]`。
全部整数majorant给

\[
 \sum_{Z/2\le q\le Z<r\le2Z}\frac1{r-q}\ll ZL.
 \tag{18}
\]

故乘任意 `sum b_p²=O(1)` 的 repeated label后，费用 O(X^-1/2 L)。
far差频和正负sum频都用(16)；其平方重复权重聚合为

\[
 X^{-1}(\sum b_p^2)(\sum_Hb_q)(\sum_Lb_r)
 \ll X^{-1/4}/L^2=o(1).
 \tag{19}
\]

### 5.2 低平方乘低素数与高素数：p²q versus r

near `p,q<=Z<r<=X`、`r~p²q` 中，m=p²q复合，故r≠m。
原重复权重准确给

\[
 b_p^2b_qb_r|K_d(\log(p^2q/r))|
 \ll\frac1{X|p^2q-r|}.
 \tag{20}
\]

near强制 `p²q<=2X`。对每个p,q，全部整数r的harmonic sum为 O(L)，
而整数hyperbola计数

\[
 \#\{p,q\le Z:p^2q\le2X\}
 \le\sum_{1\le p\le Z}\min(Z,2X/p^2)
 \ll X^{3/4}.
 \tag{21}
\]

于p≈X^1/4分开求和即可。故near normalized费用 O(X^-1/4 L)。
无需对moving feature应用素数定理或composite–prime Hilbert。
far仍由(19)支付，不丢掉m>2X或alias。

### 5.3 平方与高低素数乘积：p² versus qr

令r为low prime、q为high prime（在13表中可交换这两个算术dummy labels；
这里只majorize absolute weights，不更改任何operator顺序）。重复p可在low或high范围。
near `qr~p²` 给

\[
 b_p^2b_qb_r |K_d(\log(p^2/(qr)))|
 \ll\frac1{X|p^2-qr|}.
 \tag{22}
\]

等号 `p²=qr` 因genuine primes及相反范围不可能；所有近零原子仍非零。
若p为low，则p<=Y=Z；若p为high，near q<=X、r<=Z强制
`p<=Y=sqrt(2XZ)=sqrt2 X^3/4`。

固定r和p，若r不整除p，记
`delta_r(p)=dist(p²,r Z)>=1`。沿q整数arithmetic progression直接求和得

\[
 \sum_{1\le q\le X}\frac1{|p^2-qr|}
 \ll\frac Lr+\frac1{\delta_r(p)}.
 \tag{23}
\]

对prime模数r，每个非零值的平方根至多2个（r=2同样满足此上界）。
将1<=p<=Y分成完整residue blocks及一个残块；残块也不超过整个block的
正harmonic sum。于是

\[
 \sum_{\substack{1\le p\le Y,\ r\nmid p}}\frac1{\delta_r(p)}
 \ll (Y/r+1)\log(2r).
 \tag{24}
\]

重要的是残块费用为 O(logr)，不是 O(rlogr)：对每个residue至多2个根，
`sum_(a=1..r-1)1/min(a,r-a)=O(logr)`。
actual p也为prime，r|p只可能p=r。这仅在low重复时出现；单独有
`sum_(q>Z)1/|r²-qr|<<L/r`，按r求和为 O(L²)。
使用Chebyshev–Mertens `sum_(r<=Z,prime)logr/r<<L`、
`sum_(r<=Z,prime)logr<<Z` 和保守 `sum_(r<=Z)1/r<<L`，(23)–(24)给

\[
 \frac1X\sum_{\substack{p\le Y,\ p\mathrm{\ prime},\ r\le Z,\ r\mathrm{\ prime},\ q\le X}}
                   \frac{\mathbf1_{p^2\ne qr}}{|p^2-qr|}
 \ll\frac{YL^2+Z+L^2}{X}.
 \tag{25}
\]

在(25)中p=r的项按前述prime exception解释，未将整数p中所有倍数r混入。
实际q可限制high和near，放大到所有整数只用于这个positive upper bound。
两个重复范围分别得到 O(X^-1/2 L²)和O(X^-1/4 L²)。
远端ratio仍按(19)；(25)不用于far，故不会遗漏csc alias。

## 6. Actual adjacent A：low非local及所有远端

由(14)，`A_R,S` 与 `Tr E*D_phy,R B_R B_S E` 的误差o(d)。
high的 `D_phy,H=sum_H B_p²`准确为bounded multiplication M_dH。
low则是local M_dL加上same-sign的 `±2log p` shifts；不能认作只有local。
两个d符号norm有界、finite crossing已在§3支付。

local项只有一high、一low的两个shifts。其差频用(18)，sum频及far difference
用(16)、(19)（local symbol norm仅乘绝对常数），全部o(d)。
这直接计算带endpoint的物理迹，未将P与B免费交换，也无需迁移到一个
不同顺序的weighted norm。

low nonlocal中固定p的两步同向；以 `++` 表示，随后low q和high r两符号有

| signs `(p,p,q,r)` | displacement | near费用 | far费用 |
|---|---|---|---|
| `++++` | `log(p²qr)`，至少high长度 | 无near | (19)，空路径也保留为空 |
| `+++-` | `log(p²q/r)` | (20)–(21) | (19)，包括m>2X及alias |
| `++-+` | `log(p²r/q)>log4` | 无near | (19) |
| `++--` | `log(p²/(qr))` | (22)–(25)，p为low | (19) |

`--`通过偶窗reflection给另外四模式。每项都有相同平方重复权重
`b_p² b_q b_r`，其far mass只有 O(X^3/4/L²)，不是全部四词的 ℓ¹ mass。
因此完整low非local也o(d)。得到

\[
 A_{L,H}=o(d),\qquad A_{H,L}=o(d).
 \tag{26}
\]

## 7. Actual opposite O：low与high全部16模式

由混合重复引理(13)，`O_R,S` 可合法换为
`sum_(p in R)Tr E*B_p B_R B_p B_S E`，误差o(d)。
以下表覆盖全部signs，未只处理near。

### 7.1 重复low，另一个low q，high r

固定第一步p+，其余8模式如下，reflection给另外8模式。

| `(p,q,p,r)` signs | displacement | 付款 |
|---|---|---|
| `++--`,`+--+` | `±log(q/r)` | near (18)，far (19) |
| `++-+`,`+---` | `±log(qr)` | (19)；endpoint alias由(16)消去 |
| `++++` | `log(p²qr)` | far (19) |
| `+++-` | `log(p²q/r)` | near (20)–(21)，far (19) |
| `+-++` | `log(p²r/q)>log4` | far (19) |
| `+-+-` | `log(p²/(qr))` | near (22)–(25)，p low；far (19) |

所有near均以 |W|<=1 majorize，所有far均先用物理overlap，故joint moving
features与phase没有被当成独立weights。p=q造成triple重复亦涵盖在(20)
及(25)的prime exception中；不需提前从physical sum免费删掉。
所以 `O_L,H=o(d)`。

### 7.2 重复high p，另一个high q，low r

前三步均为high shifts。相邻同号使两位置距离>L，所以必须交替。
固定第一步p+，只剩第三步p+、第二步q−两个模式；其余6个为空。
加上reflection，全部16signs只有以下4个可能非零：

| sign | displacement | 付款 |
|---|---|---|
| `+-++` 及其反射 | `±log(p²r/q)`；p²>X、q<=X、r>=2使绝对值>log2 | far (19) |
| `+-+-` 及其反射 | `±log(p²/(qr))` | near (22)–(25)，Y=sqrt2 X^3/4；far (19) |

这次near平方–半素数需要模low prime r的真实residue计数；粗称两组products
没有diagonal并不能给出它。反之全high的模数范围不同，不能在本报告免费
认作同样的power-small bound。此处Y/X=X^-1/4是high/low范围的关键。
因此 `O_H,L=o(d)`。和§6、下面triple费用共同证明(9)。

## 8. Triple标签与完成的实际范围

`sum_(p prime)(logp)³/p^(3/2)<infinity`，故
`sum_p ||C_p||³<<L^-3`。已付各范围二矩给 `Tr|C_S|=O(d)`，所以

\[
 |T_{R,S}|\le\Big\|\sum_{p\in R}C_p^3\Big\|\operatorname{Tr}|C_S|
              \ll d/L^3.
 \tag{27}
\]

(26)、§7、(27)及所有列出的projection/arithmetic rates给(9)。
这是全部13/31重复指标**actual finite**的o(d)，不是scalar Jensen的替代物。
它精确收掉全部intersection重复收费；也没有把22的13/120移用到本子族。
fixed-profile量词：chi、psi先固定；对每个epsilon>0，存在X0，使所有X>=X0
的 |U_L,H|+|U_H,L|<=epsilon d。无需target、零自由边界或未知full fourth。

## 9. Distinct余额的准确 finite Fourier-walk 表示

这节不是新的saving，给仍待支付对象的明确聚合等式与可复核费用。
令 `a_s(u)=phi(u)phi(u+s)`，其periodic coefficient为
`a_hat_s(n)=L^-1 int_I a_s(u)exp(-2pi inu/L)du`。
真实zero-extension的wrap处a_s=0，所以原matrix entry准确为

\[
 (E^*M_{a_s}R_sE)_{jk}=e^{i\tau_k s}\widehat a_s(j-k).
 \tag{28}
\]

在某个四词中，固定signs和s_i=eps_i logp_i。
取n_1+...+n_4=0，置
`r_0=0,r_1=n_1,r_2=n_1+n_2,r_3=n_1+n_2+n_3`，
`r_max=max r_j,r_min=min r_j`，m=d−r_max+r_min。
定义准确walk carrier核

\[
 \Gamma_{d,r}(S)=\begin{cases}
 d^{-1}\displaystyle\sum_{k=r_{\max}}^{d-1+r_{\min}}e^{i\tau_kS},&m>0,\\
 0,&m\le0,
 \end{cases}\qquad S=\sum_i s_i.
 \tag{29}
\]

其length为m，start也由r确定；不能换成长度d或删除carrier。
直接展开四个有限indices、令k为第一index，得到

\[
 \frac1d\operatorname{Tr}(C_{p_1}C_{p_2}C_{p_3}C_{p_4})
 =\prod_i b_{p_i}\sum_{\varepsilon}\sum_{n_1+\cdots+n_4=0}
  \Gamma_{d,r}(S)
  e^{-\frac{2\pi i}{L}(r_1s_1+r_2s_2+r_3s_3)}
  \prod_i\widehat a_{s_i}(n_i).
 \tag{30}
\]

只有m>0才有项，等价于保持全部四个indices在[0,d−1]。因此(30)可以直接
用于(8)，没有遗漏任何P、sign、crossing、重复排除或alias。
将Gamma替换为K_d，仅得到相应**一个顺序的**physical trace；两者差是
完整的projection余额，不能宣称它小。

为明确其规模，已有C² bounds给

\[
 \sum_n|\widehat a_s(n)|\ll\ell_0,\qquad
 \sum_n\min(1,|n|/d)|\widehat a_s(n)|
       \ll L(1+\log(d/L))/d\ll L^2/d.
 \tag{31}
\]

且 `|Gamma−K_d|<=min(1,(r_max−r_min)/d)`，所有m<=0也满足这个界。
利用 span<=sum|n_i|，在正majorant中放大到四个独立n sums，得到

\[
 |\mathcal E_{13}|/d\ll X^{1/4}\ell_0^3/L^3,\qquad
 |\mathcal E_{31}|/d\ll X^{3/4}\ell_0^3/L^3.
 \tag{32}
\]

这里E是(8)的distinct finite trace与相应physical顺序trace之差，按全部signs
和prime labels聚合。真频率a_s coefficients的ℓ¹ bound已支付，未假设
different primes leakage正交。这些bounds仍增长，**不足以删除distinct P**。
相较只说投影未知，(29)–(32)给出准确要估计的walk sum及当前自然费用。

## 10. 实际长度、系数及新的可检验闭合条件

distinct physical13的一个顺序为low q、low r、low s、high p；终位移
`eps_q logq+eps_r logr+eps_s logs+eps_p logp`。
可能的整数分组包括low三素数product（最大X^3/2）对high prime（最大X），
以及low两素数product（最大X）对high×low（最大X^3/2）。
distinct31则包含high两素数product（最大X²）对high×low（最大X^3/2），
或high三素数product（最大X³）对low prime；后者的某些linear sign paths
为空，但(30)中的finite edges不能据此免费删除。

产品系数是原 `product(logp)/(a_L L)^4 sqrt(productp)`，带原physical
intermediate窗或(30)的Fourier coefficients。
只说两个product集合无exact equality不能控制长度超过X的near differences。
比如high²与high×low的local integer spacing可到X^-3/2，而finite时间长度
仅X；一般Hilbert weighted-energy账本会出现正幂损失。
更不能把三个同范围labels彼此不同的条件静默移掉后得到虚假的diagonal。

可检验的actual闭合条件现在有两个明确对象：

1. 对(8)的distinct标签及全部signs，支付按其原物理顺序计算的carrier sum
   `K_d(S)<W>` **实部**的signed O(1) normalized upper budget（13/31各一个；
   一个physical顺序的trace本身可以是complex，不能默认它为实数）；
2. 对完全相同标签和signs，支付(30)中把K_d换为Gamma所产生的
   `(Gamma−K_d) product a_hat` sum为o(1)，或与第一项合法联合支付。

第二条件正是internal-P余额，不是abstract“假设有投影控制”。(29)可直接
给有限整数测试及原taper计算；(32)表明现有绝对ℓ¹方法没有付出它。
若两个条件确实成立，(1)与这些明确费用才给完整actual M13/M31上界。
本报告未把它们登记为已证明前件。

另一条合法充分路线是对selfadjoint B=B_H+B_L使用
`Tr(E*BE)^4<=Tr(E*B^4E)` 的scalar spectral Jensen。
但后者one-high/three-low coefficient是
`sum_(j=0..3)Tr E*B_L^j B_H B_L^(3−j)E`，并非可在物理迹中免费循环的
`4Tr E*B_H B_L³E`。不同放置会改变首尾窗及support；三步同号长度cut也
依放置不同。其one-sided whole-fourth budget必须保留这四个placements，
不能用本报告的actual finite循环去更改physical polynomial。

## 11. 范围、有限检查与下一步

本次不重复消费low四矩、proper powers、padding或background小量；
原Fourier/physical轴完整保留，没有先丢掉height tails。
证明(9)所需的唯一finite-P付款是平方重复指标可求和的(13)–(14)。
对distinct全部词，没有声称相同付款仍可用。

未解决的是(30)中三个同范围labels不同的真实signed响应，特别finite walk
和product ratio之间的相消。可继续尝试sum over walks后的Fourier separation、
moving residue/dispersion，或whole physical Jensen的四placement合并；
新的结果必须实际支付(29)及(32)所显示的余额。

在内存以exact Counter验证高低标签数各1–3的9个cyclic partition模型；
以Fraction和整数奇偶相位验证d=2、3、4、5的4个有限Fourier-feature模型，
直接matrix trace与(29)–(30)的Gamma walk完全相等，共13个断言通过。
后者features为任意有限rational coefficients，只检查walk代数，不代替真实
AF窗、prime sums或渐近分析。没有写新script/output。

当前推导完成，等待根节点独立全文审查。未用小模型冒充无限分析证明；
后续near residue计数有限审计也不会自动认证distinct signed预算或比例。
