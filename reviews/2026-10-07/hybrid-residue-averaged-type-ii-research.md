# 联合频率壳中的 moving mask 准入：整数比值重编码、全高度 reciprocal 与弱 Type-II 付款

2026-10-07。type_ii_joint。状态：[T/R]，R 仅为既有全 Dirichlet family 的
fixed-gap uniform reciprocal control。本文证明原 balanced cell 的真实
log-frequency shells、有限 masks、six-window 和所有 k 的 moving-weight
联合 Möbius 估计，补齐前一报告只证明 fixed W 准入的有限范围；§5.1另
无条件支付 fixed-cell 基线此前没有自动覆盖的 common-centering 项。
canonical 界弱于这里补齐的无条件 centered Schur 界，没有取得新的
o((log X)^4)、有限四矩常数或简单临界线零点比例。

不更改此前 joint 报告、脚本、math 源码或论文。本报告不是单个 h fiber
的 prime-pair 渐近；不将绝对 determinant interval 的 curved 边界套入下面
straight log-ratio 编码。

## 1. 实际对象和需要估计的联合壳权重

使用此前报告(1)–(9)：Y=X^(3/4)、L=log X、Q=XL，
所选实际整数 D=XL+O(1)，τ_k=2πX+2πk/L。
同一个 canonical completion

\[
 B_V(A)=\sum_{\substack{v\mid A\\v>V}}\Lambda(v),\qquad
 U=V=Y^{1/4},
 \tag{1}
\]

以及此前预先固定的 natural mask

\[
 m(a,b)=\mathbf1_{(a,b)=1}m_0(a,b).
 \tag{2}
\]

本报告使用原 Type-I 已明确准入的 m_0：fixed rectangular/factor/aperture
cuts，固定 b 时 a-slice 有固定有限个 interval 边界。除了这些 cuts，
原 window 是 real C²、0≤φ≤1、||φ''||_1 有 uniform bound。不能扩大为
任意 ghost-point mask。令 H=L²(R/LZ,dz/L)，保留

\[
 F_{a,b}(z)=\phi(z+\log(a/b))\phi(z)\phi(\log b-z)^2,
 \quad W_{a,b;c,d}=\langle F_{a,b},F_{c,d}\rangle_H.
 \tag{3}
\]

对一个原共同 frequency shell J，置

\[
 \Xi_J(t)=\mathbf1_{\{|t|\in J\}},\qquad
 K_J(t)=\Xi_J(t)\{K_{Q,D}(t)-\kappa_J\},
 \quad t=X\log(ad/bc).
 \tag{4}
\]

κ_J 为同一个有限 K 在 J 上的实际平均，准确 |κ_J|≤1；其数值和原
shell endpoints 不更改。端点 convention 取原 partition 的一致约定。
centering 仍是共同线性投影，而非各 channel 独立选择 density。

令 ℛ、𝒮 为实际 Möbius divisor 的 dyadic intervals，
ℛ⊂[R_0,2R_0)、𝒮⊂[S_0,2S_0)，可附加 r≤U/r>U 等真实 cutoff。
定义

\[
 f_{\mathcal R}(a)=\sum_{\substack{r\mid a\\r\in\mathcal R}}
 \mu(r)B_V(a/r),
 \quad
 f_{\mathcal S}(c)=\sum_{\substack{s\mid c\\s\in\mathcal S}}
 \mu(s)B_V(c/s),
 \tag{5}
\]
\[
 \begin{split}
 {\cal Q}_{\mathcal R,\mathcal S}(J)
 =\sum_{\substack{a,b,c,d\ {\rm in\ actual\ cell}\\(a,b)\ne(c,d)}}
 &\frac{m(a,b)m(c,d)\Lambda(b)\Lambda(d)
 f_{\mathcal R}(a)f_{\mathcal S}(c)}
 {(4\pi^2)^2\sqrt{abcd}}\\
 &{}\times W_{a,b;c,d}\,
 K_J\!\left(X\log(ad/bc)\right).
 \end{split}
 \tag{6}
\]

这是 fixed canonical decomposition 的内部 bilinear piece，不是
gauge-independent physical quantity。完整 physical quotient 准确是先
合并全部 ℛ、𝒮，令 Σ_ℛ f_ℛ=Λ，再对 J 求和。以下绝对界不能作为
241禁止丢掉跨块符号的理由，也不会据此宣称 physical closure。

要完成的真实准入是：(6)含移动 shell、原 sharp integer cuts、全部 composite
ghost atoms 和 finite carrier。它没有一个预先固定、与 labels 无关的 W。

## 2. 有限整数比值上的 sharp endpoint 精确重编码

固定 R,S≥1，整数 u∈[R,2R)、v∈[S,2S)。取所有不同的
x=log(u/R)-log(v/S)。对 x≠x'，整数交叉乘积给

\[
 |x-x'|
 =|\log(uv')-\log(u'v)|
 \ge\frac1{\max(uv',u'v)}
 \ge\frac1{4RS}=:\Delta_{R,S}.
 \tag{7}
\]

重复 rationals 只重复同一个 x，按 distinct values 编码；无需先假定 gcd。
下述编码使用这个完整 integer rectangle，而不依赖 μ、Λ 或较有利的
prime/ghost support。

对任何 sharp threshold α，可在两个相邻 distinct x 之间取其 midpoint α'，
使其 sharp half-line indicator 在所有整数 atoms 上准确等于原 indicator。
若 α 恰好等于某个 x，依原 strict/inclusive convention 选它与左邻或右邻的
midpoint。若原 indicator 在全部 atoms 上为常数，直接使用该常数。
所以编码不会改变任何实际 mask，也不需要原 α 离某个 atom 的下界。

每个非恒定编码 α' 到所有 x 的距离至少 Δ_(R,S)/2。
令 η=(32RS)^(-1)，取一个固定 smooth monotone step h，h(y)=0 当
y≤-1，h(y)=1 当 y≥1。则

\[
 h_\eta(x-\alpha')=h((x-\alpha')/\eta)
 \tag{8}
\]

在所有实际整数 atoms 上与 sharp indicator 完全同值。
有限 interval 用两个这样的 steps 的乘积，或 half-line differences；
shell 的正负两段只增加固定数目的 edges。

取 fixed compact cutoff ψ(x)=1 在 x∈[-log2,log2] 上，支撑在稍大的 fixed
interval，扩展上述编码成 compact function H_(α,R,S)(x)。
它不是 fixed profile，但其 weighted Fourier seminorm 可以明确支付。
对于 0<ν<1，有

\[
 \|H\|_1+\|H'\|_1\ll1,\qquad \|H''\|_1\ll\eta^{-1},
 \tag{9}
\]
\[
 |\widehat H(\lambda)|
 \ll\min\{1,|\lambda|^{-1},\eta^{-1}|\lambda|^{-2}\},
 \tag{10}
\]
\[
 \boxed{
 \int_{\mathbb R}|\widehat H(\lambda)|
 (1+|\lambda|)^\nu\,d\lambda
 \ll_\nu \eta^{-\nu}\log(2/\eta).}
 \tag{11}
\]

证明：(9)来自每个 transition 的 total variation O(1)、二阶 variation
O(η^(-1))；(10)分别不用 integration by parts、用一次和两次；
在 |λ|≤1、1≤|λ|≤η^(-1)、|λ|≥η^(-1) 三段直接积分得(11)。
对 ν>0，log 因子可以去掉，但保留这个较粗统一表达即可。

特别地，moving shell 的 micro scale 没有产生 η^(-1) 费用；
只产生可通过任意小 height exponent 支付的 η^(-ν)。
没有用 continuous prime density 替换稀疏整数。

一变量的原 sharp factor/aperture cuts 同样可在相邻 integers 的 midpoint
重编码，再在 log(u/R) 上以 η_u≍R^(-1) micro-smooth，所有实际整数值不变。
其 fixed-number weighted Fourier cost 是 R^ν log^C(2R)。
φ(z+log(gARx/b)) 乘 fixed annular x-cutoff 的二阶 log-derivative L¹
有 uniform bound：φ'∞≤||φ''||_1，且只取 fixed-length translated
log interval。φ 本身不需要 micro-smoothing。

因而实际 six-window 与这些 sharp cuts 相乘的 Mellin/Fourier profiles
对每个 fixed z 都有同样任意小 exponent 的 explicit seminorm fee。
normalized dz/L 积分不再引入 L 或 z-dependent 幂费用。

## 3. 原 g,u,v 的 joint average 及 natural zero extensions

在 μ(r)μ(s)≠0 时，用此前唯一分解

\[
 r=gu,\quad s=gv,\quad g=(r,s),\quad
 g,u,v\ {\rm squarefree\ and\ pairwise\ coprime},
 \quad \mu(r)\mu(s)=\mu(u)\mu(v).
 \tag{12}
\]

取 a=guA、c=gvC，固定外层 g,A,C,b,d。原 natural mask 的 outer 前件是

\[
 (gA,b)=(gC,d)=1,
 \tag{13}
\]

而内层剩下的独立 zero extensions 可精确写为

\[
 \chi_1(u)=\mathbf1_{(u,gb)=1},\qquad
 \chi_2(v)=\mathbf1_{(v,gd)=1},\qquad (u,v)=1.
 \tag{14}
\]

它们包括 squarefree r,s 需要的 (g,u)=(g,v)=1；没有把 natural mask
当作 smooth weight。若(13)失败，原项就是0。
这里不用仅在 small core 有效的 (a,c)=1 投影；所以(12)–(14)保持全部
nonzero determinant tails，g 和 denominator gcd 也没有被擅自删为1。

固定外层后，B_V(A)B_V(C) 是真实标量，不再是 μ(u)μ(v) 的 moving
coefficients。原 kernel argument 准确为

\[
 t=X\log\frac{uAd}{vCb}
 =X\left\{\log(u/R)-\log(v/S)+\log(RAd/(SCb))\right\}.
 \tag{15}
\]

因此(4)的 actual shell 正是§2处理的 sharp log-ratio interval。
对 actual integer rectangle 重编码只改变其在 atoms 之间的表示，
不改变 κ_J、J 或任何 atom membership。

对每个原 finite k，carrier 分离为

\[
 e^{i\tau_k\log(ad/bc)}
 =e^{i\tau_k\log(ARd/(CSb))}
 (u/R)^{i\tau_k}(v/S)^{-i\tau_k}.
 \tag{16}
\]

g 在 ratio 中准确消去；F_(guA,b)、F_(gvC,d) 中的原 log a、log c
和全部 square-root weights仍在原值，不声称 W 在缩放后不变。

特别地，精确的可分离式为
\[
 H(\log(u/R)-\log(v/S))
 =\frac1{2\pi}\int_{\mathbb R}\widehat H(\lambda)
 (u/R)^{i\lambda}(v/S)^{-i\lambda}\,d\lambda.
 \tag{16a}
\]

在 z 积分中，(3)的 u-dependent factor 是
φ(z+log(guA/b))，v-dependent factor 是 φ(z+log(gvC/d))；
φ(z)^2 φ(log b-z)^2 φ(log d-z)^2 是 bounded outer factor。
原 two natural masks 加 factor/aperture cuts也依 u、v 分别准入。
故 micro-encoded shell H(log(u/R)-log(v/S)) 经 Fourier inversion 使
全部 moving weight 的内层转成真正 coupled canonical sums，
而非依某个 u-sum error 再对 v 施加一次 PNT。

## 4. 全高度 reciprocal 输入支付真实 moving profile

假定既有 [R]：θ>1/2，固定 θ<σ<1，原 Dirichlet family 的 primitive
reciprocal 及 deleted Euler zero extensions 在 Re s≥σ 的 fixed strip
满足任意小 conductor/height exponent bound。q_eff 记录 finite deletion；
gap、原 φ 的 uniform C² bound、cut数及 seminorm order 先于所有 labels 固定。

使用此前报告(20c)–(20d)已经证明的准确 Dirichlet series

\[
 \sum_{(u,v)=1}\frac{\mu(u)\mu(v)\chi_1(u)\chi_2(v)}{u^zv^w}
 =\frac{{\cal H}_{\chi_1,\chi_2}(z,w)}
 {L(z,\chi_1)L(w,\chi_2)}.
 \tag{17}
\]

H 在 Re z,Re w≥σ>1/2 上 absolutely convergent 且 uniformly bounded；
只使用 H，不使用其 reciprocal。q_eff≤O(gb),O(gd)，本 cell 中是
X 的固定幂；不删掉 deleted-prime fees。

对 fixed z 以及 Fourier λ，原 inner weight 分离为两个 annular profiles，
加两个 pure twists τ_k+λ、-τ_k-λ（τ=0 时支付 κ_J 项）。
二维 Mellin inversion 分别移两线到 σ，乘 u^(-1/2)v^(-1/2) 后给

\[
 |\mathcal I_{g,A,C,b,d;J,k}|
 \ll_{\sigma,\epsilon}
 (RS)^{\sigma-1/2}
 (q_{1,\mathrm{eff}}q_{2,\mathrm{eff}})^\epsilon
 \times\text{实际 weighted Mellin/Fourier seminorm}.
 \tag{18}
\]

水平线可先对每个 finite X/encoded profile 移动后送高度到∞；
原 C² Fourier decay 加足够小 reciprocal height exponent使其消失。
没有 principal residue，因为 principal 1/L 在s=1是零。

在实际 seminorm 中，twist 的 height 因子满足

\[
 (3+|\tau+\lambda+t_1|)^{2\epsilon}
 (3+|-\tau-\lambda+t_2|)^{2\epsilon}
 \ll
 (3+|\tau|)^{4\epsilon}(1+|\lambda|)^{4\epsilon}
 (1+|t_1|)^{2\epsilon}(1+|t_2|)^{2\epsilon}.
 \tag{19}
\]

§2的 encoded interval 的(11)支付 λ，one-variable sharp cuts 的同类
估计支付 t_1,t_2，φ 的 uniform C² profile支付剩余 Mellin weights。
η≈(RS)^(-1)，R,S≤O(Y)、q_eff和τ_k均为X的固定幂。
给定最终 ε>0，可以先取输入 reciprocal exponent 充分小，
将这些 explicit seminorm fees 和 logs 全部吸收进 X^ε。
由于输入是全高度，|λ|远大于原 |τ_k| 的 tails 也已付款；没有截掉它们。
归纳得到

\[
 \boxed{
 |\mathcal I_{g,A,C,b,d;J,k}|
 \ll_{\sigma,\epsilon}
 (RS)^{\sigma-1/2}X^\epsilon.}
 \tag{20}
\]

这是实际 sharp log-shell、natural masks、six-window 和 canonical
μ⊗μ 的 uniform moving-weight bound。不是一个尚未支付 seminorm 的
fixed-W 估计。取 finite k 的准确平均不增加 D；减 κ_J 项只增加固定常数。
z 积分的 normalized measure 也已保留。

## 5. 真实外层账本、diagonal 删除及全部 tails

对于固定 g，u≈R_0/g、v≈S_0/g，补齐其若干 dyadic annuli，只需固定
数目的 intervals；当 quotient接近1时用R,S≥1的首个 annulus。
记 R≈R_0/g、S≈S_0/g，其中 comparability 常数固定，
nonempty 时 g≤O(min(R_0,S_0))。原 completion ranges是

\[
 A\asymp Y/(gR),\qquad C\asymp Y/(gS).
 \tag{21}
\]

保留原 square-root weights，使用 B_V(n)≤log n 和 Chebyshev，给

\[
 \sum_A\frac{B_V(A)}{\sqrt A}\ll
 \sqrt{Y/(gR)}\log(2Y),\quad
 \sum_C\frac{B_V(C)}{\sqrt C}\ll
 \sqrt{Y/(gS)}\log(2Y),
 \tag{22}
\]
\[
 \sum_{b\asymp Y}\frac{\Lambda(b)}{\sqrt b}\ll\sqrt Y,\qquad
 \sum_{d\asymp Y}\frac{\Lambda(d)}{\sqrt d}\ll\sqrt Y.
 \tag{23}
\]

外层用了 absolute sums；不称它们来自新的 b,d 联合相消。
1/sqrt(ac)=1/(g sqrt(uvAC))的 g^(-1) 不能遗漏。
把(20)–(23)合并，每个 g 的实际全部 outer payment 为

\[
 Y^2g^{-2}(RS)^{\sigma-1}X^\epsilon
 \asymp
 Y^2(R_0S_0)^{\sigma-1}g^{-2\sigma}X^\epsilon.
 \tag{24}
\]

Σ_g g^(-2σ) 有界，σ>1/2；这是共同 Möbius sign 平方消失后的真正费用，
不是假定 μ(g)仍可相消。所有 g包括 h可能共享的大 divisor 都保留。

同 atom reference必须准确删除。所有两侧 masks primitive，所以 h=0
当且仅当(a,b)=(c,d)。先在 all-atoms 版本证明(24)，再减原 reference。
对 fixed g,A,C、b=d，coprime u,v 的 uA=vC 准确只有
u=C/(A,C)、v=A/(A,C) 一对；没有隐藏的零 determinant families。
更直接地，原 dyadic f_ℛ(a)、f_𝒮(a) 满足
|f_ℛ(a)|,|f_𝒮(a)|≤d(a)log a，因而该同 atom reference绝对值

\[
 \sum_{a,b}
 \frac{|f_{\mathcal R}(a)f_{\mathcal S}(a)|\Lambda(b)^2}
 {(4\pi^2)^2ab}\,m(a,b)^2 W_{a,b;a,b}
 \ll_\epsilon X^\epsilon.
 \tag{25}
\]

在 shell J 中按其实际 Xi_J(0)(1-κ_J)乘这个 reference再减；
该系数至多2。如果 shell不含0则reference为0。没有在 joint canonical
sum 中删掉 composite ghosts 后再猜测 diagonal compensation。

所以得到真正的实际弱界

\[
 \boxed{
 |{\cal Q}_{\mathcal R,\mathcal S}(J)|
 \ll_{\sigma,\epsilon}
 Y^2(R_0S_0)^{\sigma-1}X^\epsilon+X^\epsilon.}
 \tag{26}
\]

共同 central-plus-dyadic shells覆盖所有实际 t，数目O(log X)，因此同界
可经有限求和（吸收logs）覆盖完整 K^(cent)；没有仅保留resolution core。
原 affine formula逐个 h的ℓ集合仍只有它原来的整数点数，每次重新联合 h
只是有限求和交换。式(15)不是对每个稀疏 fiber 做 continuous replacement。

对 r>U、s>U 的真实 large-divisor tail，O(L²)个dyadic rectangles给

\[
 |{\cal Q}_{>U,>U}^{\rm cent}|
 \ll_\epsilon
 Y^2 U^{-2(1-\theta)}X^\epsilon+X^\epsilon.
 \tag{27}
\]

这里先取σ-θ充分小、固定在所有 labels 之前，将(R_0S_0)^(σ-θ)吸入
最终ε。θ=7/8、U=Y^(1/4)、Y=X^(3/4)时主幂为

\[
 Y^{31/16}=X^{93/64}.
 \tag{28}
\]

在没有 shell subtraction 的 raw specialization 中，它比既有
canonical whole I/II contour 的 X^(21/16+ε)更弱，
也远弱于同 cell 无条件 finite-ratio Schur 的 X^(1/2+ε)。
旧 finite-ratio 报告未直接证明 individual common-centered channels 有
相同 Schur 界；这项额外付款在下面§5.1完成，不将 raw 基线自动扩大。
因此不能把(27)称为新的算术净 saving 或最佳 Type-II 上界。
其新内容是实际移动的 sharp frequency shell权重获准，
而非 fixed-W 前件，也不是新的四矩常数。

### 5.1. 无条件补齐同 fixed cell 的 common-centering Schur 费用

这里不使用 [R]。取原 usual central J_0=[0,M]、dyadic J_j=[R_j,2R_j]，
M≥1，R_j=2^jM，最后一个 interval可覆盖实际最大 |t|=O(X)。
endpoint常数改变但 length≍R_j 的 intervals同样适用；不扩大到 length
任意趋零而 upper endpoint不受控的 shells。

对每个 ξ_k≥1，原 finite cosine 核逐项积分准确给

\[
 |\kappa_J|
 \le\frac1{D|J|}\sum_k
 \frac{|\sin(2\pi\xi_k B)-\sin(2\pi\xi_k A)|}{2\pi\xi_k}
 \le\frac1{\pi|J|}.
 \tag{29}
\]

原 primitive ratio atoms i=(a,b) 的 s_i=log(a/b) 互异，
不同 s 间距≥c/Y²，且固定 balanced cell 的全部 s_i 落在O(1)区间。
对固定 i，在 central |t|≤M 或 dyadic |t|≤2R_j 中可有的 j-atoms 数量
因此满足

\[
 \#\{j:|X(s_i-s_j)|\le2R_j\}
 \ll1+Y^2R_j/X.
 \tag{30}
\]

central 情形把 R_j 换成 M。故 shell density subtraction matrix 的
绝对 Schur row与column费用为

\[
 \sup_i\sum_j
 |\kappa_J|\mathbf1_{\{|X(s_i-s_j)|\in J\}}
 \ll R_j^{-1}+Y^2/X.
 \tag{31}
\]

Σ_j R_j^(-1)≪1/M，shell数O(log X)，给所有 centering terms 的
共同费用

\[
 B_{\rm density}\ll1+(Y^2/X)\log(2X).
 \tag{32}
\]

raw finite complex kernel保留 carrier，用原精确几何级数
|D^(-1)Σ_ke^(iτ_k(s_i-s_j))|≤min(1,C/(X|s_i-s_j|))，
排序相邻 ratios 得已证
B_raw≪1+(Y²/X)log(2Y)。fixed O(1) log-ratio区间保证
|s_i-s_j|<L/2，故没有偷删grid alias。

上述 Schur estimates 在原 Hilbert features 中保持：
|<F_i,F_j>|≤||F_i||||F_j||。对原 canonical f_ℛ,f_𝒮 记

\[
 A_{\mathcal R}=
 \sum_{a,b}\left|
 m(a,b)\frac{f_{\mathcal R}(a)\Lambda(b)}{4\pi^2\sqrt{ab}}
 \right|^2\|F_{a,b}\|_H^2
 \ll_\epsilon X^\epsilon,
 \tag{33}
\]

用上面(25)相同的 divisor majorant，A_𝒮 同界。
对 mixed coefficient vectors，symmetric absolute kernel的 Schur operator
bound 给 B sqrt(A_ℛ A_𝒮)，不需要 features orthogonal，也不使用
任意 ghost-gauge freedom。原 same atom reference最后准确减去，
其费用仍由(25)支付。因此无条件有

\[
 \boxed{
 \left|\sum_J{\cal Q}_{\mathcal R,\mathcal S}(J)\right|
 \ll_\epsilon X^{1/2+\epsilon}.}
 \tag{34}
\]

每个 J 单独也有相同粗界。完整 I、II、Λ coefficients仍满足同一 divisor
majorant，所以(34)同样适用其固定表示的全部 centered entries，以及
physical quotient的合并表达。它不意味着可以从 physical 小量反推出
channelwise 小量；这是这个固定表示另有独立证明的粗充分上界。

该付款关闭旧 baseline 中“common shell centering另需支付linear mass项”
在上述 fixed-cell、usual central/dyadic partition 上的局部缺口。
它没有覆盖 log-ratio跨度达到 L 的 all-cells alias，也远不是o(L^4)。
不将它称作新的公开解析纪录或足以付四矩常数的算术saving。

## 6. 对 reciprocal residue average 的准确结论和剩余任务

此前 exact affine formula中的 h/(gq)、modulus vb_0、O(1)个ℓ整数点，
在联合 frequency shell后精确恢复(15)的 log-ratio mask。
本报告利用整数比值间距，证明这种特定 moving weight 可交给
coupled canonical Dirichlet series和 explicit weighted Fourier inequality。
这是一条可核查的真实 transform及准入，不把任意 reciprocal-residue
coefficients都宣布为canonical。

以下范围仍未证明：

- 固定单个 h 的曲线型 arithmetic filter，或额外 sharp h interval：
  在u,v坐标中它是 guAd-gvCb∈[H_1,H_2]，不是固定 log(u/v) interval；
  §2不能直接准入该 curved Mellin boundary。
- 外层 A,C,b,d及不同 divisor blocks 的 joint signed gain。
  (22)(23)取绝对值的费用仍是幂级；这也是(27)弱于已有基线的原因。
- 真正 physical o(L^4)、完整四矩 finite-constant预算、跨cells与alias账本。
  241的 physical-first 原则仍然约束接入比例链的最终估计。

不再将“actual log-frequency moving profile没有weighted Mellin预算”
作为本报告域内的未付前件：该预算已由(7)–(20)显式支付。
同样，上述 fixed-cell usual shell partition 的 linear mass centering
已经由(29)–(34)无条件支付到与 raw Schur 相同的粗幂界。
应该继续攻击的是能避免(22)(23)绝对求和的联合算术估计，
或利用 h-average和实际 prime/denominator结构取得新的净费用；
不重复扩写已完成的canonical准入，也不以(27)宣布目标完成。

## 7. 有限防错证据与依赖范围

在 u=8,…,15、v=16,…,31 的128个完整整数 atoms（110个 distinct ratios）
上，以 Fraction 进行精确 endpoint 编码审计。测试阈值包括全部110个 ratio、
全部109个相邻 arithmetic midpoints以及两个外侧阈值；对 strict/inclusive
两种 lower-half-line convention全部测试。436个 nonconstant编码用相邻
ratios乘积作为 geometric midpoint 的平方，通过 rational square comparison
比较；56576个 atom classification 全部准确同值。该检查不使用浮点log，
不代替(7)–(11)的全量词证明，也不认证 reciprocal 输入或渐近节省。

主要依赖为仓库已固定的以下原件：

- [实际 affine / coprime joint 报告](hybrid-joint-type-ii-fiber-research.md)：
  completion、唯一 g,u,v 分解、稀疏整数 fiber和 coupled Euler product。
- [Type-I原mask准入](hybrid-response-type-i-admission-and-type-ii-gap.md)：
  预先固定 natural ghost extension、fixed finite interval cuts、原 C²窗口。
- [finite-ratio raw基线](hybrid-finite-ratio-gram-baseline.md)：
  actual atom spacing及原 finite geometric kernel的 Schur 付款。
- [446](../../notes/446-uniform-prime-twists-on-the-original-gabor-frame.md)：
  全导子/全高度 uniform reciprocal-control 的明确 [R] 范围。
- [239](../../notes/239-vaughan-quotient-first-centering-and-divisor-kernel.md)
  与 [241](../../notes/241-divisor-scale-separation-no-go.md)：
  original common linear centering 和 physical-fiber-first规则。

新增 moving-profile Fourier inequality、pointwise integer编码以及
common-centering Schur 账本均在本文完整证明。没有导入新的外部
prime-pair、random-sign、Hardy–Littlewood或有限四矩常数假设，
也没有重跑外部 formal kernel。
