# 原 AF 的 22 全异素数：二步乘积付款与真实有限剩余

2026-10-07。作者：`mixed_path_check`。只新增本报告；不改旧稿、notes、
script、output、formal/math、Goal 或 Git。起点为权威提交
`502463775b1ba2a7d4aab65e1b55f3fbe775d7de`，开始时工作区干净。

本轮研究实际 exactly-two-high/two-low 四词，不重做已固定的 repeated union。
得到的新前向付款是：**真实物理二步同号块的整个全异非对角部分为 o(N)**。
其原因是原支撑强制 `pq<=X`，一个 high prime、一个 low prime 的乘积有
唯一分解，weighted finite Hilbert energy 为 `O(X/L)`。同时给出整个物理
二步量和实际有限矩阵的准确差额，两个未付 correlation 和真实 P crossing
均明确列出。还得到未达目标的粗上界

\[
 M_{22}\ll X^{3/2}/L,
 \qquad M_{22}/d\ll \sqrt X/L^2.
 \tag{1}
\]

这个右边仍趋于无穷，**不是净 O(N) 或新的完整四阶常数**。下面的物理
同号付款不能被免费登记为实际压缩全异四词的付款；对应 finite crossing
是本报告保留的明确剩余，而非被省略的 o(N)。没有比例、无零边界或 RH 结论。

## 1. 固定输入和原对象

沿用 [AF v2 §2](https://arxiv.org/html/2608.13637v2#S2) 的原 Fourier frame、
窗与 multiplier；唯一 frequency-sum 输入是
[Montgomery–Vaughan Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
的局部间距 Hilbert inequality。已付款的 finite crossing 与 repeated union
引用如下，文本哈希只规范 CRLF、孤立 CR 为 LF：

| 输入 | canonical LF SHA256；bytes |
|---|---|
| [高 prime 报告](hybrid-high-prime-four-word-response-research.md) | `988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666`；19170 |
| [高低 repeated union](hybrid-low-high-mixed-four-word-research.md) | `71f62b2dd931cfda012e7dad9c4efcfece63f5cf1bb8ff5b466d3e2ac1ae89f9`；22126 |
| [根节点限定审查](hybrid-low-high-mixed-four-word-review-root.md) | `e9a748ce81c4779577c21b6c8677c45c043c5113770b9d6ebac088171423faed`；5464 |

准确取

\[
 X=T/(2\pi),\quad L=\log X,\quad Z=\sqrt X,
 \quad d=\lfloor XL\rfloor,\quad I=[-L/2,L/2],
 \quad \tau_k=T+2\pi k/L\quad(0\le k<d),
 \tag{2}
\]
\[
 Ee_k(u)=L^{-1/2}\mathbf1_I(u)e^{i\tau_k u},\quad
 P=EE^*,\quad Q=1-P,
 \quad R_sf(u)=f(u+s).
 \tag{3}
\]

所有 physical translations 都先零延拓。保留原偶、非负、C² taper `phi`，
`0<=phi<=1`，以及

\[
 a_L=L^{-1}\|\phi\|_2^2\to a_\psi>0,\quad
 b_p=\frac{\log p}{a_LL\sqrt p},\quad
 B_p^\sigma=-b_pM_\phi R_{\sigma\log p}M_\phi,
 \quad B_p=B_p^++B_p^-.
 \tag{4}
\]

写 `H={p prime:Z<p<=X}`、`Lpr={q prime:q<=Z}`；后文 `B_L,C_L` 中的
L 下标只指 low 范围。令 `B_R=sum_(p in R)B_p`、`C_R=E*B_RE`。
既有真实 second moment 和 leakage 给，置 `ell_0=log(2+L)`，

\[
 \|B_HP\|_2+\|B_LP\|_2\ll\sqrt d,\quad
 \|B_H\|\ll\sqrt X/L,\quad\|B_L\|\ll\sqrt Z/L,
 \tag{5}
\]
\[
 \|QB_HP\|_2\ll\sqrt{X\ell_0}/L,\quad
 \|QB_LP\|_2\ll\sqrt{Z\ell_0}/L.
 \tag{6}
\]

HS norms 在原 physical Hilbert space 或其有限 rank compression 中取；
只在最后使用 `d/N(T,2T)->1`，不采用 `d=N+O(L)`。

## 2. M22 的实际正量与 commutator

设

\[
 A_{22}=\operatorname{Tr}(C_H^2C_L^2)=\|C_HC_L\|_2^2,
 \quad \mathcal K=[C_H,C_L].
 \tag{7}
\]

实际六个位置选择准确给

\[
 M_{22}=4A_{22}+2\operatorname{Tr}(C_HC_LC_HC_L)
       =6A_{22}-\|\mathcal K\|_2^2.
 \tag{8}
\]

对 Hermitian 两矩阵，`||C_LC_H||_2=||C_HC_L||_2`，故

\[
 0\le\|\mathcal K\|_2^2\le4A_{22},\qquad
 \boxed{2A_{22}\le M_{22}\le6A_{22}.}
 \tag{9}
\]

因此求净 `M22=O(d)` 的量级问题与 `||C_HC_L||_2^2=O(d)` 等价。
commutator 可改变 leading constant，但仅凭它的负号不能将一个远大于 d
的正 product norm 变成 O(d)。

已付款的 repeated union 是

\[
 R_{22,\mathrm{rep}}=(4D_{HL,\psi}+8J_{HL,\psi})d+o(d),
 \quad R_{22,\mathrm{distinct}}=M_{22}-R_{22,\mathrm{rep}}.
 \tag{10}
\]

这里 all-distinct 要求两个 high 标签不同、两个 low 标签不同；两范围本就
不相交。(9)同时给真实 signed 下界
`R22,distinct>=-(4D+8J)d-o(d)`，flat 为 `-13d/120-o(d)`。
下面攻击其 upper budget，未把这个下界当成 upper saving。

## 3. 二步物理块与准确频率

令 `a=log p>L/2`、`b=log q<=L/2`，定义

\[
 f_{p,q}^{\sigma,\eta}(u)=
 \phi(u)\phi(u+\sigma a)^2\phi(u+\sigma a+\eta b),
 \quad c_{p,q}=b_pb_q,
 \tag{11}
\]
\[
 U_{\sigma,\eta}=\sum_{p\in H,q\in Lpr}
 c_{p,q}M_{f_{p,q}^{\sigma,\eta}}R_{\sigma a+\eta b},
 \quad U=B_HB_L=\sum_{\sigma,\eta}U_{\sigma,\eta}.
 \tag{12}
\]

两次负号已准确抵消。固定 high 首步正向后只有两个 blocks：

| block | frequency | 三个位置 span | 支撑强制 |
|---|---|---|---|
| `U++` | `log(pq)` | `a+b` | `pq<X`；相等时积分为零 |
| `U+-` | `log(p/q)` | `a` | 没有 `pq<=X` 的限制 |

负 high 首步由 reflection 给另两个 blocks。不同 high 首步的输出支撑
严格分离：正向输出在 `u<0`，负向输出在 `u>0`。这一点在 physical U
中准确成立；经 P 投影后不再免费成立。

定义准确 finite carrier kernel

\[
 K_d(s)=d^{-1}\sum_{k=0}^{d-1}e^{i\tau_k s}
 =e^{i[T+(d-1)\pi/L]s}\frac{\sin(d\pi s/L)}{d\sin(\pi s/L)}.
 \tag{13}
\]

令 `<g>=L^-1 int_R g`。任何两个同首 high sign 的 blocks 满足

\[
 d^{-1}\langle U_{+,\eta}P,U_{+,\eta'}P\rangle_{HS}
 =\sum_{p,q,p',q'}c_{p,q}c_{p',q'}
 K_d(a+\eta b-a'-\eta'b')
 \langle f_{p,q}^{+,\eta}f_{p',q'}^{+,\eta'}\rangle.
 \tag{14}
\]

本文约定 HS 内积线性于第一个因子；反过来的约定只共轭(14)，所有 real
parts 和 norms 相同。式(13)的 carrier 保留在每一次求和内。

## 4. 同号块：唯一 product 与全异 o(d)

把 `U++` 的非空项按 `n=pq<=X` 分组。因为两个 prime 来自不相交 ranges，
一个 n 恰有一个合法 `(p,q)`。置 `c_n=b_pb_q`、`f_n=f_(p,q)^(+,+)`。
所有 log n 落在 `(log(2Z),log X]`，总跨度小于 `L/2`，没有 grid alias。

Chebyshev–Mertens 给

\[
 E_+(Y):=\sum_{\substack{p\in H,q\in Lpr\\pq\le Y}}
 pq(b_pb_q)^2
 \ll\frac{Y}{L^3}\log^2(2Y/Z)\quad(2Z\le Y\le X),
 \tag{15}
\]
\[
 E_+(X)\ll X/L,\quad
 A_+(Y):=\sum_{pq\le Y}b_pb_q\ll\sqrt Y/L,
 \quad \sum_n c_n^2=O(1).
 \tag{16}
\]

若 `Y<2Z` 则集合为空。证明(15)时，对每个 low q 用
`sum_(p<=Y/q)(log p)^2<<YL/q`，再用
`sum_(q<=Y/Z)(log q)^2/q<<log²(2Y/Z)`；normalizer 是原 `a_L^4 L^4`。
(16)的 l1 bound 用 `sum_(p<=Y/q)b_p<<sqrt(Y/q)/L` 与
`sum_(q<=Z)(log q)/q<<L`。没有用 prime pair PNT。

在固定 u 对 log n 用有限 Hilbert，features 为独立的 `c_n f_n(u)`。
`delta_n>=1/(2n)`，拆开(13)的两个 numerator exponentials 和
`csc(pi s/L)=L/(pi s)+O(|s|/L)`，得到

\[
 \left|\sum_{n\ne n'}c_nc_{n'}f_n(u)f_{n'}(u)
                        K_d(\log n-\log n')\right|
 \ll(L/d)E_+(X)+d^{-1}A_+(X)^2\ll1/L.
 \tag{17}
\]

所有 numerator phases，包括 T，都吸收到两边的单位相位，未删除 carrier。
按 u 积分给

\[
 \boxed{\|U_{++}P\|_2^2=dF_{+,L}+O(d/L),}
 \quad F_{+,L}=\sum_{p,q}b_p^2b_q^2
 \langle\phi(u)^2\phi(u+a)^4\phi(u+a+b)^2\rangle.
 \tag{18}
\]

不仅总非对角和小，真正 all-distinct 的非对角和也小。需说明这个最后一步：
固定 p 的 `q!=q'` 子族有单侧 `q,q'<=X/p`，低 log-prime Hilbert 能量
`O(Z/L)`，再按 `sum_p b_p²=O(1)` 聚合为 o(1)；固定 q 的 `p!=p'`
子族有单侧 `p,p'<=X/q`，高能量 `O(X/L)`，按 `sum_q b_q²=O(1)`
聚合为 `O(1/L)`。从(17)扣除这两个 repeated 子族，没有 double-diagonal。
因此

\[
 \sum_{\substack{p\ne p'\in H\\q\ne q'\in Lpr}}
 c_{p,q}c_{p',q'}K_d(\log(pq/(p'q')))
 \langle f_{p,q}^{++}f_{p',q'}^{++}\rangle=o(1).
 \tag{19}
\]

(19)及镜像是本轮明确支付的物理全异子族。它有原 finite carrier 与真实窗；
尚未删除 actual four-word 的 P。

## 5. 异号块：有理 frequency、真实长度与粗 energy

现在 `t_(p,q)=log(p/q)` 在 `(0,L-log2]`。这些频率互异：若
`pq'=p'q`，unique prime factorization 和不相交 ranges 强制 p=p'、q=q'。
对任意邻频率，整数 determinant

\[
 D_{p,q;p',q'}=pq'-p'q\ne0
 \tag{20}
\]

给统一的局部间距

\[
 \delta_{p,q}\ge\frac1{2pZ}.
 \tag{21}
\]

确证：若 log ratio 差至少 1/2，(21)显然；否则两个交叉整数 `pq'`、`p'q`
相差至少1，且后者小于两倍前者，所以
`|log(pq'/(p'q))|>=1/(2pq')>=1/(2pZ)`。
真实整数交叉 length 是 `XZ=X^(3/2)`，不能沿用同号 n<=X 的 energy。

这一组跨度接近 L，不能直接使用一个固定 `c<1` 的 csc expansion 常数。
但这里可支付真实 alias remainder。写

\[
 \csc(\pi s/L)=L/(\pi s)+h_L(s),\qquad
 |h_L(s)|\ll\begin{cases}1,&|s|\le L/2,\\
 L/(L-|s|),&L/2<|s|<L.
 \end{cases}
 \tag{22}
\]

两个 opposite features 的共同支撑长不超过 `L-max(a,a')`，并且
`|t_(p,q)-t_(p',q')|<=max(a,a')`。所以

\[
 |h_L(t-t')|\langle|f_{p,q}^{+-}f_{p',q'}^{+-}|\rangle\ll1.
 \tag{23}
\]

这里先用 Hilbert 支付(22)的主项，再对已经积分的 remainder 用(23)；
没有对一个 moving pair cut 免费套 Hilbert，也没有删除 endpoint alias。

主项的 weighted energy 在 u 平均后有真正的物理节省：

\[
 \left\langle\sum_{p,q}\delta_{p,q}^{-1}c_{p,q}^2
                         |f_{p,q}^{+-}|^2\right\rangle
 \ll Z\sum_p p b_p^2\frac{L-\log p}{L}\sum_q b_q^2
 \ll XZ/L^2.
 \tag{24}
\]

最后一步由 layer cake：
`sum_(Z<p<=X)(log p)^2(L-log p)<<XL`，除以原 L³。
因此(13)、(21)–(24)给

\[
 \boxed{\|U_{+-}P\|_2^2
 \ll d\{1+Z/L^2+Z/L^5\}\ll d(1+Z/L^2).}
 \tag{25}
\]

其中 alias remainder 为
`d^-1(sum_H b_p sum_L b_q)^2<<XZ/(dL^4)=Z/L^5`。
(25)是一个前向不等式，但远不足 O(d)。

令真实 all-distinct rational 余额为

\[
 \Delta_X=\sum_{\substack{p\ne p'\in H\\q\ne q'\in Lpr}}
 c_{p,q}c_{p',q'}K_d(\log(pq'/(p'q)))
 \langle f_{p,q}^{+-}f_{p',q'}^{+-}\rangle.
 \tag{26}
\]

它是 real signed sum。p=p' 或 q=q' 的非对角子族分别由 low/high
single-prime Hilbert 支付 o(1)，所以

\[
 d^{-1}\|U_{+-}P\|_2^2=F_{-,L}+\Delta_X+o(1),
 \tag{27}
\]
\[
 F_{-,L}=\sum_{p,q}b_p^2b_q^2
 \langle\phi(u)^2\phi(u+a)^4\phi(u+a-b)^2\rangle.
 \tag{28}
\]

新的真正未付 arithmetic 对象是(26)，而非一个抽象的 fourth moment。
需要在 length XZ 的 determinant 相关上利用 signed cancellation，或另给
适用于这些 features 的 mean-square saving；(24)的 elementary local gap
只给 `Delta_X=O(1+Z/L²)`，不能闭合净 O(d)。

## 6. 两种 low sign 的 cross：triple composite 对 prime

剩余同首 high sign 的 cross 频率是

\[
 \log(pq)-\log(p'/q')=\log(pqq'/p').
 \tag{29}
\]

定义只收 all-distinct 的明确余额

\[
 \Gamma_X=\sum_{\substack{p\ne p'\in H\\q\ne q'\in Lpr}}
 c_{p,q}c_{p',q'}K_d(\log(pqq'/p'))
 \langle f_{p,q}^{++}f_{p',q'}^{+-}\rangle.
 \tag{30}
\]

第一侧支撑已限制 n=pq<=X，但 m=nq' 仍可长到 XZ。
没有 zero-frequency diagonal：m 含至少三个 prime factors，另一侧 p' 为 prime。
以下给一个未达 O(1) 的真实前向付款，保留这种长度。

固定 q'。在单侧矩形 `m=nq'<=2X` 上，n-side 是 unique `(p,q)` 的
`c_n f_n(u)`，prime-side 是 `b_p' f_(p',q')^(+,-)(u)`；q' 固定后 features
确实可分。两集合不相交，union log span<=L/2+log2<3L/4。
由(15)，

\[
 E_m=q'E_+(2X/q')
 \ll \frac X{L^3}\log^2(4Z/q'),\quad
 E_{p'}\ll X/L.
 \tag{31}
\]

所以 finite bilinear Hilbert 主项是
`O(log(4Z/q')/L²)`，再乘 b_q'。Chebyshev layer cake 给

\[
 \sum_{q'\le Z}b_{q'}\log(4Z/q')\ll\sqrt Z/L.
 \tag{32}
\]

remainder 由 `A_+(2X/q')<<sqrt(X/q')/L`，
`sum_H b_p'<<sqrtX/L` 和 `sum_(q'<=Z)b_q'/sqrt(q')=O(1)` 支付 O(L^-3)。
因此整个 near rectangle normalized bound 为 `O(sqrtZ/L³)`。

far 的 `m>2X` 使位移 S=log(m/p')>log2；在交叉 features 的共同支撑上
仍有 span>=|S|。原 kernel 与 overlap 直接给
`|K_d(S)|<|f f'|><<1/X`，包括 S 靠近 L 的 alias。
三边 l1 mass 为

\[
 A_+(X)\Big(\sum_H b_{p'}\Big)\Big(\sum_L b_{q'}\Big)
 \ll X\sqrt Z/L^3.
 \tag{33}
\]

far 亦为 `O(sqrtZ/L³)`。这保持的是单侧 cut `nq'<=2X`，不使用
pair-dependent cut 代替 Hilbert。因而

\[
 \boxed{|\Gamma_X|\ll\sqrt Z/L^3+o(1).}
 \tag{34}
\]

仍随 X 增长。若试图把所有 q' 合并到一个 triple m feature，prime-side 的
`phi(u+log p'-log q')` 仍依赖 q'；不能直接把它当作只依赖 p' 的 feature。
这指出拟议一次合并 Hilbert 的具体缺口。

为使(30)确为 all-distinct，还须支付其 repeated 部分：p=p' 时位移
`log(qq')>=log4`，真实 overlap 与 kernel 聚合为 o(1)；q=q' 时
frequency 是 `log(pq²/p')`，固定 q 的 composite–prime `m<=2X`
矩形能量 `O(X/L)`，按 `sum_q b_q²=O(1)` 支付 O(1/L)，far 为 o(1)。
所以 whole cross 与(30)之差为 o(1)。

## 7. 整个物理 product 的准确新分解

偶窗 reflection 和 `K_d(-s)=conj K_d(s)` 使两首 high signs 给相同的 norms
与 real cross。其 physical 输出又严格分离。结合(18)、(27)、(30)有

\[
 \frac1d\|UP\|_2^2=2(F_{+,L}+F_{-,L})
                         +2\Delta_X+4\operatorname{Re}\Gamma_X+o(1).
 \tag{35}
\]

令既有 local symbols 为

\[
 d_{R,L}(u)=\sum_{p\in R}b_p^2\phi(u)^2
          [\phi(u+\log p)^2+\phi(u-\log p)^2],\quad
 D_{HL,L}=\langle d_{H,L}d_{L,L}\rangle.
 \tag{36}
\]

对 diagonal closed paths 做实际 variable translation，准确得到

\[
 2(F_{+,L}+F_{-,L})=D_{HL,L},\qquad
 D_{HL,L}\to D_{HL,\psi}.
 \tag{37}
\]

这不是带末端 P 的免费 physical cyclic rotation；每个 diagonal 的
frequency 正好零，积分全实线，普通变量平移合法。因此

\[
 \boxed{\|B_HB_LP\|_2^2
 =dD_{HL,L}+2d\Delta_X+4d\operatorname{Re}\Gamma_X+o(d).}
 \tag{38}
\]

新的物理剩余精确压缩为(26)的 rational determinant sum 和(30)的
triple-composite/prime sum，包含原 features 与 carrier。
并由(18)、(25)及 Cauchy 得
`||UP||_2²<<d(1+Z/L²)<<XZ/L`。

作为 diagonal 校验，连续主项为

\[
 F_{+,\psi}=a_\psi^{-4}\int_{1/2}^1r\,dr
 \int_0^{1-r}s\,ds\int_{-1/2}^{1/2-r-s}
 \psi(v)\psi(v+r)^2\psi(v+r+s)\,dv,
 \tag{39}
\]
\[
 F_{-,\psi}=a_\psi^{-4}\int_{1/2}^1r\,dr
 \int_0^{1/2}s\,ds\int_{-1/2}^{1/2-r}
 \psi(v)\psi(v+r)^2\psi(v+r-s)\,dv.
 \tag{40}
\]

flat 时 `F+=1/640`、`F-=1/96`，故 `2(F++F-)=23/960`，与已固定
`D_HL` 一致。一般 profile 中 F+ 的 middle ψ²与 square-corner J 不同，
不能因 flat 数值相同而将 F+认作 J。

## 8. 实际有限 P：准确二步 crossing 账

在 physical space 嵌入所有有限 matrices，定义

\[
 V=P B_HB_LP,\quad
 \mathcal E=P B_HQ B_LP,\quad
 \mathcal L=Q B_HB_LP.
 \tag{41}
\]

实际 compressed product 正好是 `P B_HP B_LP=V-E`，而
`||UP||²=||V||²+||L||²`。因此无需任何 P 删除假设的 exact identity 为

\[
 \boxed{A_{22}=\|UP\|_2^2-\|\mathcal L\|_2^2
          -2\operatorname{Re}\langle V,\mathcal E\rangle
          +\|\mathcal E\|_2^2.}
 \tag{42}
\]

这是 actual product 二矩所需的全部 internal/outer projection 费用；
既有 repeated-label deletion 不会将 E 或 L 在这里变成 o(sqrt d)。
由(5)–(6)只有

\[
 \|\mathcal E\|_2\le\|B_H\|\|QB_LP\|_2
          \ll\sqrt{XZ\ell_0}/L^2,
 \tag{43}
\]
\[
 \|\mathcal L\|_2
 \le\|QB_HP\|_2\|B_L\|+\|B_H\|\|QB_LP\|_2
 \ll\sqrt{XZ\ell_0}/L^2.
 \tag{44}
\]

这些平方为 `XZ ell_0/L⁴`，除以 d 为 `Z ell_0/L⁵`，仍非 o(1)。
结合物理 product 的已证粗 norm，真实 cross 费用至多

\[
 |\langle V,\mathcal E\rangle|
 \ll (XZ/L)^{1/2}(XZ\ell_0/L^4)^{1/2}
 =XZ\sqrt{\ell_0}/L^{5/2}.
 \tag{45}
\]

故(42)不能按已有输入得到 sharp O(d) 主项；但(43)–(45)比 `XZ/L`
小一个趋零的 log factor，由(9)得到本报告(1)的实际粗上界。

同号已付款的物理块也须单独保留这个区别：令
`V++=P U++P`、`E++=P B_H+ Q B_L+P`、`L++=Q U++P`，则

\[
 \|P B_H^+P B_L^+P\|_2^2
 =\|U_{++}P\|_2^2-\|\mathcal L_{++}\|_2^2
       -2\operatorname{Re}\langle V_{++},\mathcal E_{++}\rangle
       +\|\mathcal E_{++}\|_2^2.
 \tag{46}
\]

E++包含原 `pq>X` 的 pairs；这些 pairs 的 physical U++为空，actual
product 仍可能经 Q crossing 非零。其系数的 log product length 可达
`log(XZ)=3L/2`，不能从 physical `pq<=X` 的(17)免费获得相同 finite
length 或 alias clearance。(43)–(44)同样适用给
`||P B_H+P B_L+P||²<<d+XZ ell_0/L⁴`，仍不是实际同号全异 o(d)。

## 9. all-distinct 的最终准确剩余与下一可检验任务

令 J_HL,L 是已固定 repeated 报告的真实 four-corner finite sum；其主项为
`R22,rep=(4D_HL,L+8J_HL,L)d+o(d)`。代入(8)、(38)、(42)，得到

\[
 \begin{aligned}
 R_{22,\mathrm{distinct}}
 ={}&(2D_{HL,L}-8J_{HL,L})d
      +12d\Delta_X+24d\operatorname{Re}\Gamma_X\\
 &-\|\mathcal K\|_2^2-6\|\mathcal L\|_2^2
      -12\operatorname{Re}\langle V,\mathcal E\rangle
      +6\|\mathcal E\|_2^2+o(d).
 \end{aligned}
 \tag{47}
\]

所有 `K`、E、L 都是同一个原有限 P 的量。式(47)明示 commutator 的 signed
合并及三种 projection correction；不能各自用任意正 majorant后声称保留
同一 sharp constant。flat 的第一个系数是 `17/480`，但它只是这条 exact
decomposition 中的已知项，**不是全异 sector 的主项或预算**。

本轮新增的实际前向内容为(17)–(19)、(24)–(25)、(31)–(34)、(42)–(47)。
未付的精确工作有三项：

1. 给(26)的原窗 rational determinant sum 净 O(1) 或所需 sharp upper。
   局部 gap、真实 support 已使用完毕，余下 length 是 XZ；不能再把它改为 X。
2. 给(30)保留共享 q' 的 triple-composite/prime features 的 O(1) saving。
   单侧 m<=2X、far alias 都已付款到 O(sqrtZ/L³)，余下是 q'聚合，不能免费
   消去 prime-side 的 q' dependent factor。
3. 在 actual product 上支付(41)的 E、L，或直接利用(42)、(47)作同一个 signed
   估计。现有 crossing 粗 norm 明确超过 sqrt d，不能调用 repeated-label
   的平方可求和 deletion 来宣布这部分 o(d)。

这给出可以逐项验证的真实余额与长度。没有先删 height tails、替换 carrier、
平均 P、改采样或将物理 one-sided 量登记为 actual equality。proper powers、
背景、13/31以及 high four-distinct 不属于本报告的新付款。

## 10. 内存精确核验与状态

在内存中对5组不同的非交换 `3x3` 对称整数矩阵、rank-2 P，以精确整数
逐一核验(8)、(9)、(42)。另以 Fraction 核验
`F+=1/640`、`F-=1/96`、`D=23/960` 与 `2D-8J=17/480`；19个断言通过。
没有写 script 或 output。有限模型只检查代数和有理积分，不认证 infinite
Hilbert、prime 渐近、alias 或 operator norm 的分析付款。

状态：新推导待根节点独立全文审查；没有新 net O(N)、完整 fourth constant
或比例证书。本文只新增一个可评审的数学研究文件。
