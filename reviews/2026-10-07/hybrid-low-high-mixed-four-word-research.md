# 原 AF 高低素数重复混合四词的有限压缩主项

2026-10-07。作者：`twisted_research`。起点为权威提交
`1a51f5767f217c3dc02cd97ff2233d25cd8dd186`；开始时只读核实工作区干净。
随后其他代理的新增研究文件不属于本报告的修改范围。本报告只新增本文件，
不改旧论文、notes、审查、脚本或 math。

本次支付的是实际有限矩阵中“恰有两个高素数位置、两个低素数位置，且至少
一个范围内的两个指标相同”的整个有符号四词子族。记此和为
`R_22,rep`，则对固定原 AF 窗有

\[
 \boxed{\frac{R_{22,\mathrm{rep}}}{d}
       \longrightarrow 4D_{HL,\psi}+8J_{HL,\psi}.}
 \tag{1}
\]

下文明确给出两个积分。flat profile 的系数为 `13/120`；它是这一实际重复
混合子族的主项，包含非零有限投影和非对角路径的付款，并非只计算一个参考
diagonal。四个指标分别不同的 `22` 子族、`13` 和 `31` 子族仍未闭合。
本报告没有完整四迹常数、新零点比例、零自由区或 RH 结论。

## 1. 物理定义、原始输入和绑定

沿用 [AF v2 §2](https://arxiv.org/html/2608.13637v2#S2) 的 frame、窗、
prime multiplier；唯一频率和输入是
[Montgomery–Vaughan 的局部间距 Hilbert inequality，Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)。
以下只引用已证明的物理泄漏和整数频率估计，不需要任何零自由输入。

| 输入 | SHA256；文本按 CRLF→LF |
|---|---|
| [原高素数报告](hybrid-high-prime-four-word-response-research.md) | `988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666`；19170 bytes |
| [453](../../notes/453-explicit-low-prime-fourth-moment-budget.md) | `0df65e79b5875fc0e5f7110ceaa05723e4db0cca0b3cc443551c7005a700ddf6`；10115 bytes |
| [AF v2 PDF](../../literature/baseline/2026-alpoge-furman-6725-v2.pdf) | `6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444`；478663 bytes，二进制 |

准确令

\[
 X=T/(2\pi),\quad L=\log X,\quad Z=\sqrt X,\quad d=\lfloor XL\rfloor,
 \quad \tau_k=T+2\pi k/L\ (0\le k<d),\quad I=[-L/2,L/2].
 \tag{2}
\]

`H=L²(I,du)` 中所有平移先零延拓到整条实线。令

\[
 Ee_k(u)=L^{-1/2}\mathbf1_I(u)e^{i\tau_k u},\quad P=EE^*,\quad Q=1-P,
 \quad R_sf(u)=f(u+s).
 \tag{3}
\]

固定原偶窗 `psi`（indicator 或 MT，或同样满足既有正则性的固定偶 profile），
真实 taper 为

\[
 \phi(u)=\chi(L/2+u)\chi(L/2-u)\sqrt{\psi(u/L)},\quad
 a_L=L^{-1}\|\phi\|_2^2,\quad a_\psi=\int_{-1/2}^{1/2}\psi(v)\,dv>0.
 \tag{4}
\]

归一化 `0<=phi<=1`；`a_L=a_psi+O(1/L)`，且真实 `C²` taper 满足
`||phi'||_1+||phi''||_1=O(1)`。不是用裸 indicator 替代有限 `phi`。
对 genuine primes 定义

\[
 \ell_p=\log p,\quad b_p=\frac{\log p}{a_LL\sqrt p},\quad
 B_p=-b_p M_\phi(R_{\ell_p}+R_{-\ell_p})M_\phi,\quad C_p=E^*B_pE.
 \tag{5}
\]

由 unitary Fourier transform `F=mathscrF M_phi E`，(5)准确对应原
`(2pi/(a_L L))F* M_prime F`，其中
`M_prime(t)=-(1/pi)sum_(p<=X)(log p)/sqrt p cos(t log p)`。
没有删除 carrier、改采样、改物理支撑或重付 proper powers。
下标 `H` 和 `L` 分别指 `Z<p<=X` 与 `p<=Z`。写

\[
 B_R=\sum_{p\in R}B_p,\quad C_R=E^*B_RE,\quad
 \mathcal D_R=\sum_{p\in R}C_p^2\quad(R=H,L).
 \tag{6}
\]

仅在最终解释为零点计数尺度时使用 `d/N(T,2T)→1`，不使用更强的差额估计。

## 2. 实际 cyclic partition 和所需六个量

所有迹首先在准确的 `d` 维矩阵中进行，普通迹循环合法。令

\[
 A_H=\operatorname{Tr}(\mathcal D_H C_L^2),\quad
 A_L=\operatorname{Tr}(\mathcal D_L C_H^2),\quad
 A_{HL}=\operatorname{Tr}(\mathcal D_H\mathcal D_L),
 \tag{7}
\]
\[
 O_H=\sum_{p\in H}\operatorname{Tr}(C_p C_L C_p C_L),\quad
 O_L=\sum_{p\in L}\operatorname{Tr}(C_p C_H C_p C_H),\quad
 O_{HL}=\sum_{p\in H,q\in L}\operatorname{Tr}(C_p C_q C_p C_q).
 \tag{8}
\]

若两个高位置的指标相等，则其全部六个位置选择给
`R_H=4A_H+2O_H`；两个低位置相等同理给 `R_L=4A_L+2O_L`。
同时相等的交集为 `I_HL=4A_HL+2O_HL`。所以准确 inclusion–exclusion 为

\[
 R_{22,\mathrm{rep}}=4(A_H+A_L-A_{HL})
                    +2(O_H+O_L-O_{HL}).
 \tag{9}
\]

本报告分别证明

\[
 A_H/d,A_L/d,A_{HL}/d\longrightarrow D_{HL,\psi},\qquad
 O_H/d,O_L/d,O_{HL}/d\longrightarrow4J_{HL,\psi}.
 \tag{10}
\]

因此高重复和低重复子族各有相同主项，交集也有相同主项，不能将两项主项
直接相加。其 union 仍是(1)。没有把有符号四词视作正的独立费用。

## 3. 有限 carrier 核、端点 alias 及两集合 Hilbert 估计

准确核为

\[
 K_d(s)=d^{-1}\sum_{k=0}^{d-1}e^{i\tau_k s}
 =e^{i[T+(d-1)\pi/L]s}\frac{\sin(d\pi s/L)}{d\sin(\pi s/L)}.
 \tag{11}
\]

对四个 shifts `s_i=eps_i log p_i`，设 `S_j=sum_(i<=j)s_i`、`S_0=0`。
真实物理词的准确 trace 是

\[
 d\prod_i b_{p_i}\sum_{\varepsilon\in\{\pm1\}^4}
 K_d(S_4)\langle W_\varepsilon\rangle,\qquad
 W_\varepsilon(u)=\phi(u)\phi(u+S_4)\prod_{j=1}^3\phi(u+S_j)^2,
 \tag{12}
\]

其中 `<f>=L^-1 int_I f`。负号在四次乘积中准确抵消。
所有五个物理位置必须在 `I`；span 超过 `L` 时该词为空。

以下端点小量直接来自真实支撑，不能忽略：

\[
 \langle|W|\rangle\le (L-|S_4|)_+/L.
 \tag{13}
\]

因 `|sin(pi s/L)|>=2min(|s|,L-|s|)/L`，对任何固定 `s_0>0`，

\[
 s_0\le|s|\le L\ \Longrightarrow\
 |K_d(s)|\langle|W|\rangle\ll_{s_0}L/d\ll1/X.
 \tag{14}
\]

若 `L/2<=|s|<=L`，右端可加强为 `O(1/d)`。在 `|s|=L`，真实权重为零。
此界支付 alias 的是已经积分的物理词；不是对任意点态耦合系数免费套 Hilbert。

需用 Hilbert 时，只在两组可分离 features 上使用。若两组频率都是
`log n`、为不同正整数构成的不相交集合，局部间距至少 `1/(2n)`。
当 union 的频率跨度小于 `cL`（固定 `c<1`），在(11)拆开两个 numerator
exponentials，并用
`csc(pi s/L)=L/(pi s)+O_c(|s|/L)`。Theorem 2、polarization 和尺度优化给

\[
 \left|\sum_{m,n}\alpha_m\overline{\beta_n}K_d(\log m-\log n)\right|
 \ll_c \frac Ld\sqrt{E_\alpha E_\beta}
          +\frac1d\Big(\sum|\alpha_m|\Big)\Big(\sum|\beta_n|\Big),
 \quad E_\alpha=\sum m|\alpha_m|^2.
 \tag{15}
\]

此处 `m!=n`；对一组频率的 diagonal 另行保留。每个 numerator phase，
包括 `T`，分别进入两组 features 的单位相位。(15)不适用于不能分开的
pair-dependent cut。下文的 `m<=X` 或 `m<=2X` 都是单侧矩形 cut。

Chebyshev–Mertens 给

\[
 \sum_{p\in R}b_p^2=O(1),\quad
 \sum_{p\le Y}b_p\ll\sqrt Y/L,\quad
 \sum_{p\le Y}p b_p^2\ll Y\log Y/L^2\quad(Y\le2X).
 \tag{16}
\]

式(16)最后一项在下文只作用于真实 `p<=X` 的系数，延伸到 `2X` 是整数组
上限的方便写法。固定一个低素数 `p` 后，`m=p²q<=2X` 的能量满足
`sum m b_q²=p² sum_(q<=2X/p²)q b_q²<<X/L`。
`m` 为复合数，与另一组 prime frequencies 无交点。因此(15)统一支付
`O(1/L)`，即便 `m` 很接近另一 prime；不假设 prime independence。

## 4. 先支付共同的二矩和有限投影泄漏

记 `ell_0=log(2+L)`。已提交高报告的 Fourier crossing 证明同样适用于
所有 shifts：`phi(u)phi(u+s)` 在 wrap 区准确为零，periodic coefficients
满足 `O(min(1,1/|n|,L/n²))`。故

\[
 \|QB_pP\|_2\ll b_p\sqrt{\ell_0},\quad
 \|QB_HP\|_2\ll\sqrt{X\ell_0}/L,\quad
 \|QB_LP\|_2\ll\sqrt{Z\ell_0}/L.
 \tag{17}
\]

`||.||_2` 为 Hilbert–Schmidt norm。高算子 norm 至多 `b_p`，低算子至多
`2b_p`，所以 `||B_H||<<sqrtX/L`、`||B_L||<<sqrtZ/L`。

定义两范围平方的 local symbol

\[
 d_{R,L}(u)=\sum_{p\in R}b_p^2\phi(u)^2
                     [\phi(u+\ell_p)^2+\phi(u-\ell_p)^2].
 \tag{18}
\]

两者 sup norm 和一、二阶 derivative L¹ norm 都为 `O(1)`；其 multiplication
的投影泄漏为 `O(sqrt ell_0)`。对 high，`sum B_p²=M_dH` 准确成立；
对 low，还有 `±2log p` 的非 local 项，不能丢掉。

对 `Y=B_H` 或 `B_L`，以及任意实 `0<=w<=O(1)`，在固定 `u` 展开
`Y Ee_k`。同方向的不同 primes 差频跨度 `<L/2`，(15)给
`O((L/d)sum p b_p²+d^-1(sum b_p)²)=O(1/L)` 的 normalized off-diagonal。
low 的正负交叉项频率为 `log(qr)>=log4`，其两个输出支撑的交集长度至多
`(L-log(qr))_+`；(14)聚合给 `O((L/d)(sum_(q<=Z)b_q)²)=o(1)`。
high 正负输出支撑严格分离，交叉项为零。于是

\[
 \frac1d\operatorname{Tr}(E^*Y M_w YE)
 =\langle w d_{R,L}\rangle+o(1),\qquad
 \|YP\|_2=O(\sqrt d).
 \tag{19}
\]

`w` 只按 sup norm 进入这个证明，不要求它在求和前吸收耦合系数。
后续取 `w=d_H` 或 `d_L`。这支付的是准确 finite-k sum，不用全高度平均替代。

## 5. 重复指标聚合的 P 删除引理

这节给出本次关键范围：P 删除只在平方可求和的 repeated label 上聚合，
绝不对全部四词使用其 ℓ¹ 系数。

设重复的 selfadjoint `A_i` 满足 `a_i=||A_i||<<b_i`、
`l_i=||QA_iP||_2<<b_i sqrt ell_0`、`sum b_i²=O(1)`。
另设 `Y=Y*`、`y=||Y||`、`l_Y=||QYP||_2`、`Y_2=||YP||_2=O(sqrt d)`。
逐个从左到右删掉 opposite word 的三个 internal P，得到

\[
 \left|\sum_i\operatorname{Tr}(P A_iPYP A_iPYP)
       -\sum_i\operatorname{Tr}(P A_iY A_iYP)\right|
 \ll Y_2l_Y+yY_2\sqrt{\ell_0}+yl_Y\sqrt{\ell_0}=o(d).
 \tag{20}
\]

三个差额逐项界分别是
`a_i²Y_2 l_Y`、`a_i yY_2 l_i`、
`l_Y(a_i²Y_2+a_i y l_i)`。最后一项使用准确分解
`YA_iP=YP A_iP+YQ A_iP`，故
`||YA_iP||_2<=a_iY_2+y l_i`；没有漏掉右 P。
按 `sum a_i²=O(1)`、`sum a_i l_i=O(sqrt ell_0)` 聚合得到(20)。
最大范围 `Y=B_H` 的右端为
`O(X sqrt(ell_0/L)+X ell_0/L²)=o(d)`。

adjacent word 也可合法删除。置 `D_phy=sum A_i²`，其 norm 为 `O(1)`，
`||QD_phyP||_2<<sqrt ell_0`。实际 `sum(E*A_iE)²` 与 `E*D_phyE` 的差
是 positive leakage，迹为 `O(ell_0)`。因此

\[
 \operatorname{Tr}\big[(\sum_i(E^*A_iE)^2)(E^*YE)^2\big]
 =\operatorname{Tr}(E^*D_{\rm phy}Y^2E)+o(d).
 \tag{21}
\]

详细误差为 `O(y²ell_0+l_Y²+y l_Y sqrt ell_0)`：先换 D（positive trace
付款），再把 `(E*YE)²` 换 `E*Y²E`（差 `E*YQYE`），最后付
`P D_phy QY²P`，使用 `||QY²P||_2<=2y l_Y`。
全程保留右伴随和真实 P。相同估计若对 all-distinct 四词使用
`(sum b_p)^4`，并不能得到 `o(d)`。

还须明示 bounded multiplication 的迁移，不能在带末端 P 的 physical trace
中免费循环。若 `M=M_w`、`||M||=O(1)`、`||QMP||_2=O(sqrt ell_0)`，则
`Tr(E*M Y²E)` 和 `Tr(E*Y M YE)` 分别与同一个有限矩阵量
`Tr[(E*M E)(E*YE)²]` 比较。前者由(21)同样的三个泄漏步骤，后者展开
`YE=E(E*YE)+QYE`，各自误差均为
`O(l_Y²+y l_Y sqrt ell_0)=o(d)`。因此可以迁移到(19)，但迁移是付费的
有限投影比较，不是宣称 P 与 Y 交换。§6的两个 local main 都使用此桥。

## 6. 两个相邻主项：low 非 local 部分必须付款

由(21)、(19)、high 的平方乘法性质，立即有

\[
 A_H=d\langle d_{H,L}d_{L,L}\rangle+o(d).
 \tag{22}
\]

`A_L` 中不可直接写 `sum_low B_p²=M_dL`。其非 local 部分包含
`p,p,q,r`，其中 `p<=Z`、`q,r>Z`，两个 low shifts 同向。
以 `b=log p,a=log q,c=log r` 写 `low ++`；`low --` 是其反射。

若最后两个 high shifts 同向，两相邻 high 步合计超过 `L`，支撑为空。
其余两种模式如下，均须实际付款。

| sign | 净位移 / 分離变量 | 聚合费用（除以 d） |
|---|---|---|
| `+++-` | `log(p²q/r)`；支撑强制 `m=p²q<X` | prime–composite (15)：`O(1/L)` |
| `++-+` | `log(p²r/q)`；先固定 `m=p²r<=2X` 的单侧矩形 | prime–composite (15)：`O(1/L)` |
| `++-+` 的 `m>2X` | 净位移 `>log2`，直接用(14) | `O(1/L²)` |

第一种令 `v=u+2b+a`，真实 weight 为

\[
 \phi(v-2b-a)\phi(v-c)\phi(v-b-a)^2\phi(v-a)^2\phi(v)^2.
 \tag{23}
\]

它准确分成 q-side、r-side 和 common v-side；q-side 所有因子 norm≤1。
第二种令 `v=u+2b-a`，weight 为

\[
 \phi(v+a-2b)\phi(v+c)\phi(v+a-b)^2\phi(v+a)^2\phi(v)^2.
 \tag{24}
\]

按 `m=p²r` 写，r-side 是 `b_r phi(v+log m-2b)`；q-side 含
`b_q phi(v+log q-2b)phi(v+log q-b)²phi(v+log q)²`。
最后额外的 `phi(v+log q)²` 保留，不能漏掉。两集合频率跨度最多
`L/2+log2<3L/4`（充分大 X）；均有能量 `O(X/L)`，所以(15)统一给
`O(1/L)`。没有用 moving pair cutoff 替代这个单侧矩形。
far 项用(14)后，`sum_low b_p²=O(1)` 和
`(sum_high b_q)²<<X/L²` 给 `O(L^-2)`。
因此 low 非 local 项整体为 `o(d)`，而 local 项由(19)得到

\[
 A_L=d\langle d_{H,L}d_{L,L}\rangle+o(d).
 \tag{25}
\]

## 7. Opposite high-repeat 的全部16符号模式

由(20)，`O_H` 可换成 `sum_(p high)Tr E*B_p B_L B_p B_L E`，误差 `o(d)`。
置 `a=log p>L/2,b=log q<=L/2,c=log r<=L/2`。
先固定第一步为 `p+`，下表列出其八种；第一步 `p-` 由反射给另外八种。
所有 bounds 保留(11)的 carrier。

| `(p,q,p,r)` sign | 真实支撑 / 净位移 | 付款 |
|---|---|---|
| `++--`, `+--+` | `±(b-c)` | q≠r 用可分 (15)；q=r 保留 square main |
| `++-+`, `+---` | `±(b+c)` | `(14)`，`O((L/d)(sum_high b_p²)(sum_low b_q)²)=o(1)` |
| `++++`, `+++-` | `S_3=2a+b>L` | 准确为空 |
| `+-++` | `S_4=2a-b+c>L/2` | `(13)` 的强 `O(1/d)`；`o(1)` |
| `+-+-` | `S_4=2a-b-c>0`，支撑使 `L-S_4>c>=log2` | 以下 near/far 付款 |

首行 `++--` 令 `v=u+b`，weight 准确为

\[
 \phi(v-b)\phi(v-c)\phi(v-b+a)^2\phi(v+a)^2\phi(v)^2.
 \tag{26}
\]

q/r features 分离；`+--+` 用 `v=u-b` 同理。对 q≠r，low energy
`sum q b_q²<<Z/L` 使 normalized 误差 `O(Z/d)+O(Z/(dL²))=o(1)`，
再按 `sum_high b_p²=O(1)` 求和。q=r 的四个闭合 signs 是 square corners，
不在两个 high-prime alternating words 的旧 `o(d)` 论证里。

最后一行是可能很小的 displacement，不能直接用固定间隔(14)。
`Z<p<Z+1` 最多一个整数，其 `b_p²<<1/Z`；用 `|K|<=1`，费用
`(1/Z)(sum_low b_q)²=O(L^-2)`。其余 `p>=Z+1` 有
`S_4>=2log(p/Z)`，且 alias gap 至少 `log2`，故

\[
 |K_d(S_4)|\ll X^{-1}\{1/\log(p/Z)+1\},\quad
 \sum_{Z+1\le n\le X}\frac1{n\log(n/Z)}\ll L.
 \tag{27}
\]

最后用全部整数 majorant、`b_p²<<1/p`，费用是
`O((Z/L²)L/X)=O(1/(ZL))`。这涵盖任意 real X，未假定 sqrtX 与 primes
有固定间距。合并全部16模式得

\[
 O_H=4dJ_{HL,L}+o(d),
 \tag{28}
\]

其中 `J_HL,L` 是下一节给出的实际四角有限和。

## 8. Opposite low-repeat 的全部16符号模式

由(20)，`O_L` 也可换为物理词，误差 `o(d)`。现在 `b=log p<=L/2`，
`a=log q>L/2,c=log r>L/2`。固定第一步 `p+` 的八种如下；反射补齐。

| sign | 位移 / 准入范围 | 付款 |
|---|---|---|
| `++--`, `+--+` | `±(a-c)` | q≠r 可分 high Hilbert `O(1/L)`；q=r square main |
| `++-+`, `+---` | `±(a+c)`，绝对值 `>L` | 支撑为空 |
| `++++` | `2b+a+c>L` | 支撑为空 |
| `+++-` | `log(p²q/r)`，支撑强制 `m=p²q<X` | 单侧 composite–prime (15)，`O(1/L)` |
| `+-++` | `log(p²r/q)`，先分 `m=p²r<=2X` | (15) 的矩形 `O(1/L)`；far `O(L^-2)` |
| `+-+-` | `S_4=2b-a-c<0`，支撑使 `L-|S_4|>b>=log2` | 以下 near/far 付款 |

首行可按(26)的同一分离方式、互换 high/low ranges 使用(15)。
第四行令 `v=u+2b+a`，真实 weight 为

\[
 \phi(v-2b-a)\phi(v-c)\phi(v-b-a)^2\phi(v-b)^2\phi(v)^2.
 \tag{29}
\]

第五行令 `v=u+2b-a`，weight 为

\[
 \phi(v+a-2b)\phi(v+c)\phi(v+a-b)^2\phi(v-b)^2\phi(v)^2.
 \tag{30}
\]

这两个式子与(23)–(24)有不同 common factors；仍然准确可分。
`m=p²q` 或 `p²r` 复合、另一 frequency prime，两集合不相交；其 union
整数间距和 `O(X/L)` 能量给统一 `O(1/L)`。`m>2X` 时位移大于 `log2`，
用(14)和 high ℓ¹ mass 付 `O(L^-2)`。

最后一行若 `q,r<=2Z`，则

\[
 |S_4|=\log(qr/p^2)\ge\frac{q+r-2p}{2Z},\quad
 |K_d(S_4)|\ll\frac{Z}{X(q+r-2p)}+\frac1X.
 \tag{31}
\]

整数差 `q-p,r-p>=1`，`b_qb_r<<1/Z`，且
`sum_(1<=j,k<=2Z)1/(j+k)<<Z`。故此 near 区聚合为 `O(1/Z)`。
若 q 或 r 超过 `2Z`，则 `|S_4|>=log2`，alias gap 仍 `>=log2`；
`|K|<<1/X` 和 `(sum_high b_q)²<<X/L²` 付 `O(L^-2)`。
再按 `sum_low b_p²=O(1)` 求和。因此

\[
 O_L=4dJ_{HL,L}+o(d).
 \tag{32}
\]

这些是 repeated-low 真正需要的 composite–prime 和 near-boundary 费用。
仅借旧 high-sector 的“同号 high shifts 为空”不足以证明它。

## 9. 两对相等的交集和四角主项

`A_HL` 中分别把 `mathcalD_R` 换为 `E*D_phy,R E`，positive leakage 的
迹 `O(ell_0)` 乘另一个 bounded D，误差 `O(ell_0)`。
两者间 internal P 的删除付 `O(ell_0)`，因为各自泄漏 `O(sqrt ell_0)`。
`D_phy,H=M_dH`；`D_phy,L` 的 local part 为 `M_dL`，非 local 位移
`±2log p` 在 `[log4,L]`，乘 bounded dH 后由(13)–(14)付
`O((L/d)sum_low b_p²)=o(1)`。所以

\[
 A_{HL}=d\langle d_{H,L}d_{L,L}\rangle+o(d).
 \tag{33}
\]

`O_HL` 的三个 internal P 逐对删除，聚合误差
`O(sqrt(d ell_0)(sum_high b_p²)(sum_low b_q²))=o(d)`。
该 pair-weight deletion 合法，因为平方权重可求和。取§7中的 q=r 子族：
所有非零位移模式原本已用绝对 bounds 支付，仍为 `o(d)`；四个闭合 square
模式保留，故

\[
 O_{HL}=4dJ_{HL,L}+o(d),
 \tag{34}
\]
\[
 J_{HL,L}=\sum_{p\in H,q\in L}b_p^2b_q^2\frac1L
 \int_{\mathbb R}\phi(u)^2\phi(u+\ell_p)^2
                         \phi(u+\ell_q)^2\phi(u+\ell_p+\ell_q)^2\,du.
 \tag{35}
\]

闭合路径的 carrier 因 `S_4=0` 准确为1。四个 orientations 通过 translation
与偶窗 reflection 给同一个积分；非闭合路径的 carrier 已在§7–8保留。

## 10. 固定 profile 的连续积分和 flat 常数

elementary Mertens partial summation 给 normalized prime-square measure
`L^-2 sum (log p)²/p delta_(log p/L)→r dr`。
实际 taper 仅在固定厚度物理边带出现；scaled measure 下这部分消失。
全部符号一致有界，所以 dominated convergence 和 partial summation 给

\[
 d_{H,L}(Lv)\longrightarrow
 d_{H,\psi}(v)=\frac{\psi(v)}{a_\psi^2}
                \int_{1/2}^{1/2+|v|}r\psi(r-|v|)\,dr,
 \tag{36}
\]
\[
 d_{L,L}(Lv)\longrightarrow d_{L,\psi}(v)=\frac{\psi(v)}{a_\psi^2}
 \int_0^{1/2}s\{\psi(v+s)\mathbf1_{|v+s|\le1/2}
                  +\psi(v-s)\mathbf1_{|v-s|\le1/2}\}\,ds.
 \tag{37}
\]

于是

\[
 D_{HL,\psi}=\int_{-1/2}^{1/2}d_{H,\psi}(v)d_{L,\psi}(v)\,dv,
 \tag{38}
\]
\[
 J_{HL,\psi}=\frac1{a_\psi^4}\int_{1/2}^1r\,dr
 \int_0^{\min(1/2,1-r)}s\,ds
 \int_{-1/2}^{1/2-r-s}\psi(v)\psi(v+r)\psi(v+s)\psi(v+r+s)\,dv.
 \tag{39}
\]

`min(1/2,1-r)=1-r` 在这一区间，但保留前式表明 low range。
`J_HL,L→J_HL,psi`，`<dH dL>→D_HL,psi`；(22)、(25)、(28)、(32)、
(33)、(34)证明(10)和(1)。这只是 fixed-profile 渐近量词：对固定 chi、psi
和任意 epsilon>0，存在 X0，使所有 X>=X0 的 normalized difference
小于 epsilon。不声称已经给出数值高度阈值，也不把 MT 浮点值当精确证书。

flat profile `psi=1`（有限 phi 仍含原 C² taper）时

\[
 d_H(v)=\frac{|v|+v^2}{2},\qquad
 d_L(v)=\frac14-\frac{|v|}{2}+\frac{v^2}{2},\qquad
 D_{HL}=\frac{23}{960},
 \tag{40}
\]
\[
 J_{HL}=\int_{1/2}^1\frac{r(1-r)^3}{6}\,dr=\frac1{640},\qquad
 \boxed{4D_{HL}+8J_{HL}=\frac{13}{120}.}
 \tag{41}
\]

`8J=1/80` 是两个 high 与两个 low 各重复时真实 square paths 的费用；
不能用 high-only `pqpq=o(d)` 结论删除它。

## 11. 仍未支付的实际余额与下一任务

在相同有限矩阵中，全部 `22` mixed contribution 准确是

\[
 M_{22}=4\operatorname{Tr}(C_H^2C_L^2)
             +2\operatorname{Tr}(C_HC_LC_HC_L)
        =R_{22,\mathrm{rep}}+R_{22,\mathrm{distinct}},
 \tag{42}
\]

最后一个 sum 要求两个 high 指标不同、两个 low 指标不同，仍有原 internal P。
更完整地

\[
 \operatorname{Tr}(C_H+C_L)^4
 =\operatorname{Tr}C_H^4+\operatorname{Tr}C_L^4
   +4\operatorname{Tr}(C_H^3C_L)+4\operatorname{Tr}(C_HC_L^3)+M_{22}.
 \tag{43}
\]

这里 `13`、`31` 以及 `R_22,distinct` 未控制为足够的 signed `O(d)` 常数。
§5的重复指标泄漏付款不能免费用于这些完整子族。因此，既有 high repeated
费用、453的 low scalar Jensen upper bound 和本次13/120不能直接相加成
whole response 四迹预算。453的 scalar upper bound也没有在本报告变成实际
`Tr C_L^4` 的等式主项。

本推导在完整 Fourier/physical轴上准确进行，没有先丢掉 height tails 或按
contour-dependent detector label 切 bins。physical支撑只在证明相应词为空或
支付(13)时使用；跨采样 alias 由真实 overlap 支付。没有另消费低素数、
proper powers 或 padding 的既有 o(N) 误差。共同 centering 和 background
混合仍须在 whole Hermitian response 上合法合并。

下一任务若利用 physical one-sided Jensen upper bound，可直接尝试完整
mixed signed路径，但其值不能认作同 sharp 常数的 finite compression 等式。
若仍研究 actual matrix，须保持 `R_22,distinct` 的原 P，或给新的聚合删除
估计，而不是继续用(20)中仅有重复标签才可求和的平方系数。

## 12. 防错核验和审查范围

在内存中对高、低标签数各取1、2、3，枚举全部非交换四词并按 cyclic rotation
合并，精确验证(9)、其三项定义和 union/intersection，9个模型共36个断言通过。
Fraction独立积分核验 `D_HL=23/960`、`J_HL=1/640`、`4D+8J=13/120`。
这些有限模型仅检查 partition 和有理系数，不认证 prime 渐近、Hilbert input
或全 height 分析。

另一代理 `mixed_path_check` 只读独立核验了全部高/低 repeated 的16 signs、
§5的三个 P 删除差额、composite–prime两集合整数间距与能量、near/far alias
付款，并特别指出(24)必须保留的额外 q-factor；本文已保留。
它未修改任何文件。当前状态：
[根节点独立全文审查限定通过](hybrid-low-high-mixed-four-word-review-root.md)。
此通过只覆盖(1)及明列重复混合子族的付款，不列为完整四迹预算或新的比例证书。
