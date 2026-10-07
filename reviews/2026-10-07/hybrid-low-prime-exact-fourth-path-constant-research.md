# Actual low-prime 四迹的完整路径常数：flat 19/240

2026-10-07。作者 twisted_research。状态：完整新推导，等待另一研究者全文
独立核验。只新增本报告；旧 notes、三篇论文、审查、脚本、output、math
和 Git 保持冻结。

本次对原 finite matrix 证明 **genuine primes p<=sqrt X 的整个四迹极限**。
所有重复、distinct、四 signs、carrier、alias及内部 P 都包含在同一对象。
仅用既有原 AF window/crossing、Chebyshev–Mertens 与 generalized Hilbert
输入，**无新增 [R] zero-free 前件、无 unknown full-fourth 前件**。

\[
 \boxed{d^{-1}\operatorname{Tr}C_L^4\longrightarrow\mathcal C_L(\psi),
 \qquad\psi\equiv1\Longrightarrow\mathcal C_L=19/240.}     \tag{1}
\]

这里 d/N(T,2T)→1 时可把分母换 N。此结果比
[453 的 scalar Jensen 上界](../../notes/453-explicit-low-prime-fourth-moment-budget.md)
更具体：453 未计算 actual path主项，而本次证明 offdiagonal 小量并保留
路径 overlap。它仍不能和已付高素数、mixed22常数直接相加成全四迹；
distinct22、31和高 all-distinct 项尚未闭合，未宣布新比例或 RH。

## 1. 原对象与冻结输入

\[
 X=T/(2\pi),\quad L=\log X,\quad Z=\sqrt X,\quad d=\lfloor XL\rfloor,
 \tau_k=T+2\pi k/L,\quad I=[-L/2,L/2].                     \tag{2}
\]

`E e_k=L^{-1/2}1_I exp(i tau_k u)`，`P=EE*`，`Q=1-P`，
`R_s f(u)=f(u+s)`，每次在实线作真实零延拓。
原 even taper `phi(u)=chi(L/2+u)chi(L/2-u)sqrt(psi(u/L))`；
原 fixed edge chi在宽度O(1)后恒1，phi与phi²均C²，导数 L¹ uniformly
bounded，0<=phi<=1，`a_L=||phi||_2²/L→a_psi>0`。

\[
 b_p=\frac{\log p}{a_LL\sqrt p},\qquad
 B_p=-b_pM_\phi(R_{\log p}+R_{-\log p})M_\phi,
 \quad B_L=\sum_{p\le Z}B_p,\quad C_L=E^*B_LE.             \tag{3}
\]

本报告 L 作长度，B_L、C_L 下标作 low range，不混用。
genuine primes的所有符号项均保留，proper-power 项不在本对象内。

| 输入 | canonical LF SHA256 |
|---|---|
| [原13/31的实际 low crossing](hybrid-one-three-mixed-prime-sector-research.md) | `5db2c614ab9d009a15a70f4e0639b95df2d59a6b56bd752216537fcf71e2b405` |
| [四 placements 的 joint Fourier/Hilbert](hybrid-signed-one-three-physical-resonance-research.md) | `0f7c0146e984c49d84fc057394aed1ab9ace658ae5b775b931bfd359a4c47bac` |
| [一般 two-crossing 引理](hybrid-one-three-finite-band-admission-research.md) | `bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f` |
| [453](../../notes/453-explicit-low-prime-fourth-moment-budget.md) | `0df65e79b5875fc0e5f7110ceaa05723e4db0cca0b3cc443551c7005a700ddf6` |

这里只使用上述文件的实际 algebra/window/crossing 部分，不引用其 conditional
zero-free 步骤。Hilbert 亦是 [Montgomery–Vaughan 原文](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
的已准入经典 inequality；不是关于任意 bounded prime coefficients的输入。

## 2. 原 P 的删除：精确 block identity，完全不需 band

已付个别 prime crossing `||QB_pP||_2<<b_p sqrt(ell_0)`，
`ell_0=log(2+L)`，按真实 low ℓ¹ mass求和，给

\[
 y:=\|B_L\|\ll\sqrt Z/L,\qquad
 l:=\|QB_LP\|_2\ll\sqrt{Z\ell_0}/L.                      \tag{4}
\]

这正是原13/31报告 (11)–(12) 的无条件 low bound；P仍是 interval
finitecarrier，不是连续频率 projection。没有将 (4)改成小量 op。

对任意 selfadjoint B，按 `PH⊕QH` 写 block `B=[[A,C*],[C,D]]`，
`C=QBP`，A=PBP，D=QBQ。直接乘 block，有

\[
 \begin{aligned}
 \operatorname{Tr}(PB^4P)-\operatorname{Tr}A^4
 ={}&2\operatorname{Tr}(A^2C^*C)+\operatorname{Tr}(C^*C)^2\\
 &+\|CA+DC\|_2^2.
 \end{aligned}                                           \tag{5}
\]

P有限rank保证所有 terms可定义；D只需 bounded。(5)各项非负且总量
至多 `7||B||²||QBP||_2²`。这也可由已核 two-crossing 引理得到，
但 (5)显示为什么只一个 leakage 的粗界不足。

对原 B_L 使用 (4)，于是

\[
 0\le\operatorname{Tr}(E^*B_L^4E)-\operatorname{Tr}C_L^4
 \ll y^2l^2\ll X\ell_0/L^4=o(d),                         \tag{6}
\]

normalized 费用 `O(ell_0/L^5)`。因此不需要新频带、[R]或 full fourth
来迁移本次 physical low计算。没有在物理 trace中免费循环 P。

## 3. 原物理四词：所有 net frequencies 与 overlap

固定 signs和有序四低素数，记 `s_i=epsilon_i logp_i`、`S_j=sum_{i<=j}s_i`，
`S=S_4`。准确式为

\[
 d^{-1}\operatorname{Tr}(E^*B_{p_1}^{\epsilon_1}\cdots
 B_{p_4}^{\epsilon_4}E)=\prod_i b_{p_i}\,K_d(S)\langle W\rangle,
                                                               \tag{7}
\]
\[
 W(u)=\phi(u)\phi(u+S)\prod_{j=1}^3\phi(u+S_j)^2,
 \quad\langle W\rangle=L^{-1}\int_{\mathbb R}W(u)du,
                                                               \tag{8}
\]
\[
 K_d(S)=\frac{e^{i[T+(2d-1)\pi/L]S}-e^{i[T-\pi/L]S}}
                 {2i d\sin(\pi S/L)},\qquad K_d(0)=1.    \tag{9}
\]

真实 overlap `|S|>=L⇒W=0`，且

\[
 |S|\ge c>0\Longrightarrow |K_d(S)|\langle|W|\rangle
 \ll_c X^{-1}.                                           \tag{10}
\]

(10)包括接近 ±L 的 alias；在求和之前保留所有物理 intermediate窗。
反转全部 signs使 (7)变为共轭，因此只需讨论 positive signs数 k=2,3,4，
k=1,0由真实偶窗反射给出，有限16项都覆盖。

## 4. Near offdiagonal：共享窗先 joint Fourier

取固定smooth near cutoff chi(S)，1于 `|S|<=log(3/2)`，0于 `|S|>=log2`。
四 shifted窗（3个phi²、一个phi）一同 Fourier 分离；各 L¹ norm为
`O(ell_0)`，费用 `O(ell_0^4)`。chi的 L¹ Fourier norm为固定常数。
这保持各 prime的 unit phases，再按真实产品合成系数；不能逐一个 low
prime先用正和 majorant。

### 4.1 two-plus/two-minus，去掉准确 n=m

`S=log(n/m)`，`n=pq<=Z²=X`、`m=rs<=X`。
每个有序 genuine-prime pair的multiplicity至多2，任意 unit phases的系数
满足

\[
 E_{LL}:=\sum_n n|c_n|^2
 \ll L^{-4}\Big(\sum_{p\le Z}\log^2p\Big)^2\ll X/L^2,
 \qquad\sum_n|c_n|\ll\sqrt X/L^2.                        \tag{11}
\]

联合整数 log frequencies在 `[log4,logX]`，span `L-log4`，
每个局部分离至少 c/n。剔除 n=m 后，即使两侧频率集重叠，Hilbert矩阵
以零 diagonal定义，其 bilinear inequality仍给 weighted energies (11)。
对 (9) 用 `csc(pi s/L)=L/(pi s)+h_L(s)`、`|h_L|<<L`，得 normalized
principal `O((L/d)E_LL)=O(L^{-2})`，remainder `O(L^{-4})`。
Carrier endpoints只改 unit phases。故所有该类 offdiagonal near为

\[
 O(\ell_0^4/L^2)=o(1).                                   \tag{12}
\]

这里 n=m **先准确剔除**，其值在 §6计算，不用 Hilbert 删除它。

### 4.2 three-plus/one-minus，无 n=m

`S=log(pqr/h)`，h<=Z。near强制 `n=pqr<=2h<=2Z`；n复合、h素数，
故无exact zero。Chebyshev卷积与multiplicity<=6给

\[
 E_3(2Z)\ll Z/L,\quad E_1(Z)\ll Z/L,
 \quad A_3(2Z)\ll\sqrt Z/L,\quad A_1(Z)\ll\sqrt Z/L.      \tag{13}
\]

例如 `sum_{pqr<=Y}prod log²p<<Y log^5(2Y)`，除 L^6后用
Y<=2Z且logZ=L/2得到 (13)。频率span至多 `log(2Z)-log2=L/2`。
同一 Hilbert bound给 near normalized `O(X^{-1/2}ell_0^4/L)`。
4same signs的位移至少 log16，没有 near。

## 5. Entire far，包含全部 alias：不用 canonical input

对 complement of chi，`|S|>=log(3/2)`，可先用 (10)。
此处无需把 middle与alias再拆分；以下计数覆盖真实 entirefar。

Chebyshev的迭代卷积对 k=2,3,4给

\[
 \sum_{p_1\cdots p_k\le Y}\prod_i\log p_i
 \ll_k Y\log^{k-1}(2Y),\qquad
 A_k(Y):=\sum_{p_1\cdots p_k\le Y}\prod_i b_{p_i}
 \ll_k\frac{\sqrt Y\log^{k-1}(2Y)}{L^k}.                 \tag{14}
\]

首界由 `sum_{p<=Y}logp/p<<logY` 归纳，次界由 partial summation。
可放大到全部genuine primes，原各low cut仍在真实sum里。

- k=2：全部质量 `(sum_{p<=Z}b_p)^4<<X/L⁴`，乘 (10)为 `O(L^{-4})`。
  这同时付 ±L alias；在其支持上更强的small-product限制亦未必需要。
- k=3：真实支持强制 `pqr<Xh`。对每个h<=Z，(14)给
  `A_3(Xh)<<sqrt(Xh)/L`，因log(Xh)<=3L/2。故总质量
  `sum_h b_h A_3(Xh)<<sqrt X L^{-2} sum_{h<=Z}logh<<X/L²`。
  farnormalized费用 `O(L^{-2})`，保留 middle placement中真实长 triples。
- k=4：支持强制 `pqrs<X`，质量 `A_4(X)<<sqrt X/L`，费用
  `O(X^{-1/2}/L)`。其中接近 L 的alias同样由 (10)支付。

其他 signs由反射给同样费用。这里绝不在 physical support外使用 (10)，
也未把这些有限 product cuts当作 canonical Λ convolution。
所有 nonzero net atoms已整体付成o(d)，不需要 T² pair-correlation。

## 6. Exact zero atoms：三配对及 all-repeat交集

只有two-plus/two-minus可能 S=0。genuine-prime唯一分解说明 positive
pair和negative pair多重集相同；没有不同素数四标签的exact zero。
按有序 p,q与两个 orientations sigma,eta=±1，列三个配对

\[
 A:(p_\sigma,p_{-\sigma},q_\eta,q_{-\eta}),\quad
 A':(p_\sigma,q_\eta,q_{-\eta},p_{-\sigma}),\quad
 O:(p_\sigma,q_\eta,p_{-\sigma},q_{-\eta}).                 \tag{15}
\]

p!=q 时该threepairings×fourorientations×ordered p,q枚举每个zero
word恰一次。p=q 时，每个two-plus/two-minus signword被算两次；
必须减去每个p的六种all-repeat signword各一次。该 correction不等于
随意减3或遗漏配对intersection，且其 absolute量

\[
 \ll d\sum_{p\le Z}b_p^4\ll d/L^4,                       \tag{16}
\]

因为 `sum_p(logp)^4/p²` 收敛。这里K_d(0)=1，全部path权重<=1，
无需假设same-prime与distinct两个域独立。

令x=logp/L,y=logq/L。zero路径的normalized integrals为

\[
 G_{A,L}(x,y)=\sum_{\sigma,\eta}\frac1L\int
      \phi(u)^4\phi(u+\sigma Lx)^2\phi(u+\eta Ly)^2du,    \tag{17}
\]
\[
 G_{O,L}(x,y)=\sum_{\sigma,\eta}\frac1L\int
 \phi(u)^2\phi(u+\sigma Lx)^2\phi(u+\sigma Lx+\eta Ly)^2
 \phi(u+\eta Ly)^2du.                                    \tag{18}
\]

A'对应 `phi(u)^2 phi(u+sigma Lx)^4 phi(u+sigma Lx+eta Ly)^2`。
作普通实线变量平移 `v=u+sigma Lx`、再把sigma重命名为−sigma，
其orientation和准确等于 G_A,L。此处是 S=0 后的实线积分恒等式，
不是在带P的physical trace中免费循环 operators。
因此 full physical diagonal准确为

\[
 d\sum_{p,q\le Z}b_p^2b_q^2
       [2G_{A,L}(x_p,x_q)+G_{O,L}(x_p,x_q)]+O(d/L^4).     \tag{19}
\]

## 7. 原profile极限与 prime measure

令Psi(t)为psi在 `[-1/2,1/2]` 的zero-extension，
`a_psi=int Psi(t)dt`。fixed edge cut宽度O(1)给，uniform于x,y∈[0,1/2]，
`G_A,L=G_A+O(1/L)`、`G_O,L=G_O+O(1/L)`，其中

\[
 G_A(x,y)=\sum_{\sigma,\eta}\int\Psi(t)^2
                    \Psi(t+\sigma x)\Psi(t+\eta y)dt,    \tag{20}
\]
\[
 G_O(x,y)=\sum_{\sigma,\eta}\int\Psi(t)\Psi(t+\sigma x)
              \Psi(t+\sigma x+\eta y)\Psi(t+\eta y)dt.     \tag{21}
\]

证明uniform edge error时，仅需四个translated boundary strips各宽O(1/L)，
乘积有界；不假设Psi在zero-extension边界光滑。translation的L¹连续性
给G_A、G_O连续（flat indicator情形也成立）。

Mertens–partial summation的既有输入给

\[
 \sum_{p\le Y}\frac{\log^2p}{p}
     =\tfrac12\log^2Y+O(\log(2Y)),\qquad
 \nu_X:=\sum_{p\le Z}\frac{\log^2p}{L^2p}\delta_{\log p/L}
       \Longrightarrow x\,dx\big|_{[0,1/2]}.             \tag{22}
\]

总质量趋1/8，固定小primes不形成x=0原子。对有界连续G，可用
`nu_X tensor nu_X` 的弱收敛，a_L→a_psi，以及 (19)，得到

\[
 \mathcal C_L(\psi)=a_\psi^{-4}
 \int_0^{1/2}\!\int_0^{1/2}xy[2G_A(x,y)+G_O(x,y)]dxdy.  \tag{23}
\]

这保留整个原profile；不能用Jensen profile常数倒填 actual path常数。
结合 (6)、(12)–(14)、(16)，证明 (1)。所有profiles先固定，T后趋∞。

## 8. Flat profile的确切常数

Psi=1_[-1/2,1/2]时，x+y<=1。A四 orientations 的支持span分别为
max(x,y)两次、x+y两次；O的四orientations的span全为x+y。因此

\[
 G_A=2(1-\max(x,y))+2(1-x-y),\qquad G_O=4(1-x-y).         \tag{24}
\]

`a_psi=1`，且直接分三角形的polynomial积分给

\[
 \int_0^{1/2}\!\int_0^{1/2}xy(1-\max(x,y))dxdy=3/320,
 \quad\int_0^{1/2}\!\int_0^{1/2}xy(1-x-y)dxdy=1/192.
\]
\[
 \boxed{\mathcal C_L=4(3/320)+8(1/192)=19/240.}            \tag{25}
\]

453的flat `3/16` 是合法scalar Jensen上界；与 (25) 的差为13/120。
这一差来自实际 path overlap，未把 scalar 主项和 actual主项混作相等。

当前完整推导待独审。不把 (25) 与 high repeated或mixed22常数相加宣布
全响应constant，亦不以有限模型认证prime渐近、Hilbert或projection输入。
下一阶段仍要实际支付31、distinct22和高 all-distinct signed响应。
