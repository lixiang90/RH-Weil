# 原物理 13 混合项：四 placements 的联合 canonical/Hilbert 小量

2026-10-07。作者 twisted_research。状态：完整推导已落盘，等待另一研究者
全文核验。所有旧论文、notes、脚本、output、math 与 Git 保持冻结。

本次新付款限于**原零延拓物理四词**：在已有 [R] 的 zeta zero-free
`theta<9/10` 与 fixed-gap logarithmic control 下，证明

\[
 \boxed{\sum_{j=0}^3\operatorname{Tr}
 (E^*B_L^jB_HB_L^{3-j}E)=o(d).}                    \tag{1}
\]

更强地，四个 placements 各自的 trace 都为复值的 `o(d)`。原 7/8 输入
已足够，取 `a=89/100`；不需要新 cubic boundary。这里保留四 placements、
全部 16 signs、真实 C² 窗、finite carrier、近共振、far 与 alias。
**(1) 不是 `4Tr C_H C_L³=o(d)`**；内部 P 的准确 signed 余额仍未支付。
31、distinct22、全 prime 四迹常数和零点比例也未闭合。

## 1. 冻结输入、定义与 [R]

沿用 [原 13/31 报告](hybrid-one-three-mixed-prime-sector-research.md) 的
原 AF 模型，不另选 cutoff。其 canonical LF SHA256 为
`5db2c614ab9d009a15a70f4e0639b95df2d59a6b56bd752216537fcf71e2b405`。
[distinct22 报告](hybrid-distinct-two-two-prime-sector-research.md) 的
joint Fourier/Hilbert 准入与 finite-P 限定仍保留，SHA256
`daca79cd62b61b7bd82a3b4fdf5a1a956ac0f2a1f44f7e63c0ff3f3b912cfc0d`。

规范输入使用 [446 §3](../../notes/446-uniform-prime-twists-on-the-original-gabor-frame.md)，
canonical LF SHA256 `08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf`。
它引用同一外部 [R] 的 fixed-gap logarithmic-control，给完整 sharp Λ
前缀、principal pole 和全 height 界。这里只用 conductor 1 的 zeta 情形；
没有将任意 moving coefficients 当作 canonical Λ。
该输入与 [448](../../notes/448-canonical-type-i-admission-finite-gram-and-low-prime-fourth-norm.md)
的 sharp-prefix/ghost 量词一致，448 SHA256 为
`6a7219f929cc50a721227c722fd9553eb7eba1ed9d4dd432bd971b39c2e6eafa`。

\[
 X=T/(2\pi),\quad L=\log X,\quad Z=\sqrt X,\quad d=\lfloor XL\rfloor,
 \quad \tau_k=T+2\pi k/L,\quad I=[-L/2,L/2].             \tag{2}
\]

`E e_k=L^{-1/2}1_I exp(i tau_k u)`，`P=EE*`，`Q=1-P`，
`R_s f(u)=f(u+s)`，每次平移先在实线零延拓。
`phi` 是原偶、非负 C² taper，`a_L=L^{-1}||phi||_2²` 有固定正下界。
对 `k=1,2`，原窗给

\[
 \|\phi^k\|_1\ll L,\quad
 \| (\phi^k)'\|_1+\|(\phi^k)''\|_1\ll1,\qquad
 \|\widehat{\phi^k}\|_1\ll\ell_0:=\log(2+L),
 \quad\int_{|\xi|>R}|\widehat{\phi^k}(\xi)|d\xi\ll R^{-1}.
                                                               \tag{3}
\]

最后两界由 `min(L,C/|xi|,C/xi²)` 分段积分；只需 C²，没有假定原窗
为 Schwartz。Fourier convention 是 `hat f(xi)=int f(u)e^{-i xi u}du`，
其 inversion 的固定 `2pi` 因子吸入常数。

`b_p=(log p)/(a_L L sqrt p)`，`B_p=-b_p M_phi(R_logp+R_-logp)M_phi`。
`B_L=sum_{p<=Z}B_p`，`B_H=sum_{Z<p<=X}B_p`，`C_R=E*B_RE`。
系数只含 genuine primes；没有重付 proper-power 四范数。

## 2. 每个 placement 的准确物理核

固定高素数 h 的位置、三个低素数 p,q,r 与四 signs。记
`s_i=epsilon_i log p_i`，`S_j=sum_{i<=j}s_i`，`S=S_4`。
直接按四次零延拓平移，有

\[
 W(u)=\phi(u)\phi(u+S)\prod_{j=1}^3\phi(u+S_j)^2,
 \qquad\langle W\rangle=L^{-1}\int_{\mathbb R}W(u)du,             \tag{4}
\]
\[
 d^{-1}\operatorname{Tr}(E^*B_{p_1}^{\epsilon_1}\cdots
 B_{p_4}^{\epsilon_4}E)
 =\Big(\prod_i b_{p_i}\Big)K_d(S)\langle W\rangle,               \tag{5}
\]
\[
 K_d(S)=\frac{
 e^{i[T+(2d-1)\pi/L]S}-e^{i[T-\pi/L]S}}
 {2i d\sin(\pi S/L)}.                                        \tag{6}
\]

四个负号的总乘积为正，全部 finite carrier 保留。(4) 的所有累计位置
必须在 I；特别 `|S|>=L` 时 W 为零。Endpoint overlap 给

\[
 \langle|W|\rangle\le (L-|S|)_+/L,
 \qquad |S|\ge c>0\Longrightarrow
 |K_d(S)|\langle|W|\rangle\ll_c X^{-1}.                       \tag{7}
\]

(7) 只在真实物理支持上使用，准确包含接近 ±L 的 grid alias。
它与高素数位置无关，但不能用来删除原 finite matrix 的内部 P。
因 phi 偶、`K_d(-S)=conj K_d(S)`，同时反转全部 signs 后的路径是共轭。
故下文可固定 high sign 为负，按 low positive signs 的个数 k=0,1,2,3
处理全部路径；high positive 的另八 signs 随后由反射得到。

## 3. 两个 joint near-resonance 估计

选择固定 C∞ 函数 `chi(S)`，0<=chi<=1，`chi=1` 于 `|S|<=log(3/2)`，
`chi=0` 于 `|S|>=log2`。其 Fourier L¹ 为固定常数。
Near 部分始终保留 chi，不把 sharp product cut 当作单变量 canonical 系数。

### 3.1 按乘积聚合的真实系数能量

Chebyshev 与迭代 harmonic sum 给，k=2,3，

\[
 \sum_{p_1\cdots p_k\le Y}\prod_i\log p_i
 \ll_k Y\log^{k-1}(2Y).                                    \tag{8}
\]

素数有重复亦包含在内。每个整数乘积的有序素数表示至多 k! 个。
于是任何模至多 1 的 tuple phases 都满足

\[
 E_3(2X):=\sum_{n\le2X}n\left|\sum_{pqr=n}\prod b_p\,\eta_{pqr}
 \right|^2\ll X/L,
 \quad A_3(2X):=\sum_{pqr\le2X}\prod b_p\ll\sqrt X/L.          \tag{9}
\]

证明 E_3 时，用 multiplicity<=6 和 `prod log²p<=log³(2Y) prod logp`
再应用 (8)，得到 `Y log^5(2Y)/L^6`。A_3 由 (8) 的 partial summation。
单高素数同样 `E_H<<X/L`、`A_H<<sqrt X/L`。

低两素数的完整长为 Z²=X，故更强地

\[
 E_{LL}\ll L^{-4}\Big(\sum_{p\le Z}\log^2p\Big)^2\ll X/L^2,
 \quad A_{LL}\ll\Big(\sum_{p\le Z}b_p\Big)^2\ll\sqrt X/L^2.    \tag{10}
\]

高低乘积 `m=hr<=2X` 因 h>Z>=r 有唯一分解；(8) 给
`E_HL(2X)<<X/L`、`A_HL(2X)<<sqrt X/L`。这些界不需要素数相关定理。

### 3.2 先分离共享窗，再整体 Hilbert

将 (4) 中三项 `phi²(u+S_j)` 与一项 `phi(u+S)` **一同 Fourier 分离**。
对每个固定 u 和 Fourier coordinates，每个 prime 只携自身的 unit phase。
同乘积的这些 phases先合成真实有限系数；其能量受 (9)–(10) 控制。
这一步对每个 high placement 都成立，Fourier L¹ 费用至多 `O(ell_0^4)`。
另对 chi(S) Fourier 分离，费用 O(1)。不先逐 negative low prime 求和。

当 k=3 时 `S=log(pqr/h)`；near 强制 `n=pqr<=2h<=2X`。
因此 low 侧可准确限为 n<=2X，但 **far 中 n 最大仍是 X^{3/2}**。
composite n 与 high prime h 无共同整数，联合 log frequencies 的跨度
至多 `log(2X)-log8<L-log4`。

当 k=2 时 `S=log(pq/(hr))`；near 强制 `m=hr<=2pq<=2X`。
low-pair 整数 n 与 high-low 整数 m 无共同值，联合跨度至多
`log(2X)-log4=L-log2`。这是 joint high-low 对 low-low，不能逐 r
应用 Hilbert 后再取正和，否则会损失幂次。

在上述两个整数频率并集中，各 log n 的局部分离至少 `c/n`。
把 (6) 的 csc 写为

\[
 \frac1{\sin(\pi s/L)}=\frac L{\pi s}+h_L(s),
 \qquad |h_L(s)|\ll L\quad(|s|\le L-c),                    \tag{11}
\]

使用 generalized Hilbert inequality 的 bilinear 形式，两个 carrier
endpoint 只给 unit phases，normalized principal 与 remainder 各为

\[
 \ll \frac Ld\sqrt{E_AE_B},\qquad
 \ll \frac Ld A_AA_B.                                     \tag{12}
\]

这是已有 distinct22 的同一 Hilbert 输入，支持与 union spacing 已逐项
重新检查。可参考 [Montgomery–Vaughan 原文](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)。
对 (9)、(10) 分别得到本项目真实 near 费用

\[
 k=3:\quad O(\ell_0^4/L),\qquad
 k=2:\quad O(\ell_0^4/L^{3/2}).                            \tag{13}
\]

两个费用均趋零；窗口所在的四 placements 与每个 low sign 的顺序都
仅改变已聚合的 unit phases。k=0,1 无 near：若 k=1，则
`p/(hqr)<1/4`，若 k=0，则终位移绝对值至少 `log(8h)`。

## 4. Endpoint alias 与两个直接绝对小量

选择固定 C∞ `zeta(t)`，`zeta=1` 于 t<=1，`zeta=0` 于 t>=2，
0<=zeta<=1。Alias 指 multiplier `zeta(L-|S|)`；它也覆盖 |S|>=L，
但该外侧原物理 W 为零。下面全部先用 (7)，再作 positive majorant。

### 4.1 k=0,1 的整个 far 都可直接付

k=0 的支持强制 `hpqr<X`。Chebyshev 的 high prefix给
`sum_{h<=Y}b_h<<sqrt Y/L`，扩大或截为 h<=X 都合法。因此系数质量至多

\[
 \sum_{p,q,r\le Z}\prod b_p\frac{\sqrt{X/(pqr)}}L
 \ll\frac{\sqrt X}{L^4}\Big(\sum_{p\le Z}\frac{\log p}{p}\Big)^3
 \ll\sqrt X/L.                                           \tag{14}
\]

乘 (7) 后 normalized 费用 `O(X^{-1/2}/L)`。
k=1 时写 `S=log(p/(hqr))`；支持给 `h<Xp/(qr)`，系数质量至多

\[
 \frac{\sqrt X}{L^4}\Big(\sum_{p\le Z}\log p\Big)
 \Big(\sum_{q\le Z}\frac{\log q}{q}\Big)^2\ll X/L^2.      \tag{15}
\]

因 `|S|>=log4`，整个 k=1 费用 `O(L^{-2})`，包括任何 placements 的 alias。

### 4.2 k=2 的 alias

`S=log(pq/(hr))` 的 positive alias 要求 `pq>=e^{-2}Xhr`，与
`pq<=X`、`h>Z`、`r>=2` 矛盾（X 充分大）。negative alias 则由 h<=X 给
`pq<=e² r`；物理支持还给 `h<=Xpq/r`。系数质量至多

\[
 \frac{\sqrt X}{L^4}\sum_{r\le Z}\frac{\log r}{r}
       \sum_{pq\le e^2r}\log p\log q
 \ll\frac{\sqrt X}{L^4}\sum_{r\le Z}\log^2r
 \ll X/L^3.                                               \tag{16}
\]

乘 (7) 后为 `O(L^{-3})`。式 (16) 是实际 prime-product 范围计数，
不是全部四词 ℓ¹ mass，也没有删掉 high/low 重复标签。

### 4.3 k=3 的 alias，包括 middle placement 的长 triple

`S=log(n/h)`，n=pqr<=Z³=X^{3/2}。positive alias 给
`n>=e^{-2}Xh`，所以 h<=e²Z。该 high prefix 的质量 `O(sqrt Z/L)`；
low triple 的全部质量 `O(Z^{3/2}/L³)`。故质量 `O(X/L⁴)`，乘 (7)
后为 `O(L^{-4})`。negative alias 给 n<=e²，仅有限小 prime triples
（本宽度下其实 min n=8>e²）；也可保守付 `O(X^{-1/2}/L⁴)`。

**此处没有以 path support 删除 `n>2X`。** high 在 middle 时这些
triples 可真实存在；它们在 positive alias 按上述原质量付款，其余
`n>2X` 留给下一节的 joint canonical 估计。

## 5. Entire middle-far：独立 sharp primes 与全部 Fourier ghosts

定义光滑紧支核

\[
 k_L(S)=\frac{(1-\chi(S))(1-\zeta(L-|S|))}{\sin(\pi S/L)},
                                                               \tag{17}
\]

在 0、±L 的邻域用零延拓定义。其 numerator 在这些 pole 附近恒零，
支持在 `c<=|S|<=L-1`，且 `||hat k_L||_1`、`||k_L''||_1` 为 L 的
固定幂。因而对 R>=1

\[
 \|\widehat k_L\|_1\ll L^{C_0},\qquad
 \int_{|\xi|>R}|\widehat k_L(\xi)|d\xi\ll L^{C_0}/R.       \tag{18}
\]

这一步只处理真实 middle-far，alias 已由 §4 完整付款。分解
`1=chi+(1-chi)zeta+(1-chi)(1-zeta)` 在原物理支持上精确。
对 (17) 及 (4) 的四个 shifted window factors 一同 Fourier 分离。
共有五个固定 Fourier coordinates，所有 prime variables完全独立；
每个角色只是原 sharp prefix的 norm phase。

关键是**不插入 tuple product的独立 canonical cutoff**：三个 low primes
始终各自 p,q,r<=Z，高 prime 为 Z<h<=X。`n>2X` 全保留；其 net-ratio
限制就在 (17) 这个已分离的同一 kernel 内。有限 prime sums可先互换，
Fourier L¹ 绝对收敛，故这是真实观测量的相等变形。

### 5.1 高 height 主区

[R] 与 446 的 shifted sharp Perron 给，对任意固定 theta<a<1，

\[
 \sum_{p\le Y}\frac{\log p}{\sqrt p}p^{it}
 \ll_a Y^{a-1/2}\log^2(2Y(3+|t|))
       +\frac{\sqrt Y}{1+|t|}+\log^2(2Y).                 \tag{19}
\]

完整 Λ 的 principal residue为 `x^{1/2+it}/(1/2+it)`，x=floor Y+1/2；
不能删掉。减去 proper powers 的 pointwise absolute contribution
`O(log²(2Y))` 即得 (19)。这只是 exact prime-prefix 准入，未把既有
proper-power S4预算重新相加。

在五个 Fourier coordinates 均 `|xi|<=T/100` 时，每个 prime height
为 (6) 某个 endpoint 加至多五个 ±xi，故 `|t|asymp T`。
两个 endpoint 分别约 2T 与 T；此断言保留了 finite grid 的实际 floor。
用 (19) 估计一个 high prefix（X 与 Z 两前缀之差）及三个 low prefixes，
并保留每项 b 的 `(a_L L)^{-1}`，得到 normalized main

\[
 \ll_a \frac{X^{a-1/2}Z^{3(a-1/2)}}{dL^4}
           L^{C_1}
 \ll_a X^{(5/2)a-9/4}L^{C_2}.                             \tag{20}
\]

不存在 moving b-dependent error再套 canonical cancellation 的步骤；
四个 prefixes 的共同 separation 在应用 (19) **之前**完成。
theta=7/8 下取 a=89/100 得指数 `-1/40`。更一般 theta<9/10 即可。

### 5.2 Fourier ghost heights 靠 0 的区间

若某个 prime height不在上述高主区，至少一个 coordinate满足
`|xi|>T/100`。不能在该区继续套 |t|asymp T 的 (19)。
使用 (3)、(18) 的真实 C² L¹ tail，五者 union的 Fourier质量
`O(L^{C_3}/T)`。其余因子仅取已经证明的 L¹ norm；全部 prime sums取
原 absolute masses

\[
 \Big(\sum_H b_h\Big)\Big(\sum_L b_p\Big)^3
 \ll\frac{\sqrt X Z^{3/2}}{L^4}=X^{5/4}/L^4.             \tag{21}
\]

(6) 的 endpoint form还有 `1/d`。故整个 ghost 区费用

\[
 \ll \frac{X^{5/4}}{dT}L^{C_4}=X^{-3/4}L^{C_5}=o(1).    \tag{22}
\]

这包含任一 principal height峰、多个 coordinates 相消、以及所有窗口
Fourier tails，没有依赖未知 low absolute-height canonical小量。
u 的归一化平均只给固定有界因子，不产生额外 T 或 X。

## 6. 得到的真实小量与有限 P 的准确余额

将 §3–5 对四 placements、全部 signs求和，有某个固定 C

\[
 d^{-1}\left|\operatorname{Tr}(E^*B_L^jB_HB_L^{3-j}E)\right|
 \ll \frac{\ell_0^4}{L}+\frac1{L^2}
       +X^{-1/40}L^C+X^{-3/4}L^C+\frac{X^{-1/2}}L=o(1)
 \quad(j=0,1,2,3).                                      \tag{23}
\]

Profile 和 a先固定，再取 X趋∞；常数不依赖当前 prime labels、Fourier
coordinates、carrier index或 placement。该 proof相对于 [R]，不是对
外部无零定理的重新认证。相同论证给 (1)，包括所有重复和 distinct labels。

对任意一个 placement，令其有序 operators为 V_1,...,V_4。定义准确
physical-to-finite差额

\[
 \begin{aligned}
 \Delta(V)={}&\operatorname{Tr}(PV_1QV_2V_3V_4P)\\
 &+\operatorname{Tr}(PV_1PV_2QV_3V_4P)\\
 &+\operatorname{Tr}(PV_1PV_2PV_3QV_4P).
 \end{aligned}                                           \tag{24}
\]

逐个插入 P 的 telescoping严格给

\[
 \operatorname{Tr}(PV_1V_2V_3V_4P)
 -\operatorname{Tr}(PV_1PV_2PV_3PV_4P)=\Delta(V).          \tag{25}
\]

令 Delta_j 对应 low^j–high–low^{3-j}。有限矩阵中循环合法，故新结果
把完整 actual13准确约化为

\[
 \boxed{4\operatorname{Tr}(C_HC_L^3)=-\sum_{j=0}^3\Delta_j+o(d).}
                                                               \tag{26}
\]

右侧 aggregate 为实数到 o(d)，单项未默认实数。旧原报告 (29)–(30)
中同标签的 `(Gamma_{d,r}-K_d) product a_hat` sum，正是 (25) 的相反号。
其已知 absolute bound仍为 `X^{1/4}ell_0³/L³` normalized growth，
不足以声称 (24) 小。平方重复的 P 删除已经支付，但 distinct全词无此免费权利。

因此 (23) 是 scalar spectral Jensen whole-fourth 路线中真实13系数的
一个新已推导小量；它没有给 actual13同样结论。若下一步能付
`-Re sum_j Delta_j<=C d`（或更强 o(d)），才闭合这一 actual sector。
此前的 repeated union结果仍准确保留，未重复付款。

## 7. 31 的具体剩余算术与范围

三个 high、一个 low 的 near alternating路径含
`n=pr` 对 `m=qh`，p,q,r>Z、h<=Z。近共振所需整数范围可达 XZ=X^{3/2}；
它不是 §3的 `n,m<=2X`。有限时间 X 对这两个真实产品的间距不足，
目前 Hilbert能量产生正幂费用，不能免费用本次13的预算。

同一 middle-far canonical四前缀若是 three high + one low，只给指数
`(7/2)a-11/4`，a=89/100 时为正。因此当前输入不付完整31。
这是一条解析账本的缺口，不是实际 prime响应不可能小的断言。
必须另付真实 joint high-product resonance，或在保持 (24)–(25) 的
所有 finite-P terms 后找到 signed联合预算。

本报告未成全 fourth moment、比例记录、无零边界或 RH 证明；没有改 Goal，
未修改旧文档或运行新增渐近数值审计。等待对 (8)–(23) 和实际 scope 的
另一研究者全文审查，尤其检查 shared-window 分离与 ghost/alias payment。
