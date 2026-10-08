# 原共同乘积 Perron 的长内层 ζ 四矩消费与条件 9/17 完整误差

2026-10-08，perron_reviewer；研究输入为已发布并冻结的 484，身份见 §1。
root 提示同一长内层机制可以进一步支付 Type I，本作者逐式补全其合同。
只新增本研究源，不改已冻结来源、Git、检查器或输出。
**状态：完整条件证明，待不同作者 FULL READ。**

在普通 ζ 全高度 [Rθ] 的同一个引用前件下，将原有限内层和延长到
N=floor(10T)，新增系数全在 n>X，并由共同乘积 Perron 截断支付。
长内层在正 guard 上接近 ζ，因而可消费经典普通 ζ 的第四均值，
不再只使用 Weyl 点值。相同机制给原 Type I 费用 4v。
在 H=V² 的实际费用族内，θ=7/8 得
\[
 \boxed{\mathcal M_E\ll X^{9/17+\epsilon},\qquad P_H=R+E,}
 \qquad
 \boxed{\mathcal M_{P_H}=\mathcal M_R+O(X^{159/238+\epsilon}).}
 \tag{1}
\]
与 484 的完整误差 43/75 和传递 713/1050 比，分别省 56/1275 与 14/1275。
完整 R 仍只继承已有 5/7 上界，没有新的 whole 上界、中心四阶常数、比例或无零边界。

本稿不声称经典 ζ 四矩或长 Dirichlet 截断接口的首次性。
新增付款是它们在原有限乘积、原 Λ/μ 系数、两 sharp endpoints 和完整分区中的消费。
最终真实余项仍有 balanced prime/squarefree signed mixed4。

## 1. 冻结输入、原函数与量词

下列源、原稿及证明在同一连续研究轮已由本作者全文实读；
原 484 source 的最终唯一措辞勘误也已精确核对。
本轮消费其数学合同，不重跑旧检查器、不重新认证其引用的无零输入。

| 冻结输入 | canonical UTF-8 LF SHA256 |
|---|---|
| [484](../../notes/484-original-double-perron-conditional-remainder.md) | 38c94314687ccddf1cda08b2d7611c0e1409927b0fb62fdfb0760b32256d1cad |
| [484 双因子 source，427 行](hybrid-original-double-log-derivative-perron-research-checkpoint-audit.md) | 8673c02894a1503a8e4bb9e25bfe1c693347ddfc1f5acb070b55a64b3c275b27 |
| [其不同作者全文审查](hybrid-original-double-log-derivative-perron-review-peer.md) | 1f05daa4c005b8e8363f985d31468188e312b1615fff2f1123bb227646a66f02 |
| [482](../../notes/482-original-conditional-mobius-perron-remainder.md) | c0abff933a180f5591412f82772634091f8db0e2079f846772f8a7047ed4a912 |
| [482 有限 product Perron source](hybrid-original-optimized-type-ii-remainder-research-checkpoint-audit.md) | 2d43aa69d79bde9a3aeac00ff4c9ee79696640f816df28eba051011ab255b25d |
| [481 全参数分区](../../notes/481-original-type-ii-squarefull-tail-and-optimized-moment-transfer.md) | 4ce3ea2ac087d734142c8788607c1c54fc6887bcf535c806c88097447afdc63e |
| [481 全 squarefull tail source](hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md) | 66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab |
| [477 原 Vaughan 恒等式、Type I 和二矩](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 |
| [479 最大 prefix 和疏项付款](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 |
| [原 scalar proper-power 迁移](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [476 条件 whole 增长](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |
| [451 既有边界及其完整相对输入](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |

保持
\[
 X=T/(2\pi),\quad L=\log X,\quad J_T=[T/4,4T],\quad a_L\ge c_\phi>0,
\]
\[
 P_H(t)=\frac1{a_LL}\sum_{\sqrt X<p\le X}\frac{\log p}{\sqrt p}p^{it},
 \quad \mathcal M_F=\frac1T\int_{J_T}|F(t)|^4dt,\quad
 \|F\|_{4,T}=\mathcal M_F^{1/4}.
 \tag{2}
\]
[Rθ] 是普通 ζ 在整个 Re(s)>θ 无零，1/2≤θ<1。
它不是密度估计，本稿不由当前研究重新证明该前件。
任意最终 ε>0 之前先固定更小 δ∈(0,(1−θ)/4)、ρ、η，
α=θ−1/2+δ，β=2θ−1；随后令 T 增大。
所有几何幂、guard 和常数先于 T 固定。外层仍用 c=1/L、H_out=T/8。

## 2. 唯一新增的外部经典输入及真实 +c 域

本轮实际读取了作者原书
[Montgomery–Vaughan，Multiplicative Number Theory III](https://personal.science.psu.edu/rcv4/Vol3/Vol3.pdf)
Theorem 26.23 的陈述和完整证明，PDF 第151页（印刷第143页）。
它给无条件合同
\[
 \int_0^{U}|\zeta(\sigma+it)|^4dt\ll U(\log U)^4,
 \qquad U\ge60,\quad |\sigma-1/2|\le2/\log U,
 \tag{3}
\]
常数在显示实部域统一。这里不是固定 σ>1/2 的渐近公式；
原证明使用平滑 approximate functional equation、有限多项式均值及 divisor 能量。
本稿只引用这一上界，不引用新的 twisted ζ moment 或 character-family theorem。

取 U=5T。对最终充分大 T，
\[
  \frac{3}{2L}\le\frac2{\log(5T)}.
 \tag{4}
\]
因此实际 c=1/L、以及以 1/2+c 为中心、半径 c/2 的全部 Cauchy 圈，
都在 (3) 的统一域。圈上的实部为 [1/2+c/2,1/2+3c/2]。
外层所有 |ω|≤T/8 的 t−ω∈[T/8,33T/8]，再加 c/2 的小虚部偏移，
仍在 (0,5T)。所以 (3) 为所有外层 ω 供应同一 normalized L4 合同。
实际 s 的负虚部由 ζ(\bar s)=\overline{ζ(s)} 处理；Cauchy 圈也映到上述正高度范围。

Cauchy 加 L4 Minkowski 直接给
\[
 \|\zeta'(1/2+c-i(t-\omega))\|_{4,T}
 \le\frac2c\,\frac1{2\pi}\int_0^{2\pi}
 \|\zeta(1/2+c-i(t-\omega)+(c/2)e^{i\vartheta})\|_{4,T}d\vartheta
 \ll L^2.
 \tag{5}
\]
特别是其 normalized fourth 为 O(L^8)，统一于全部 ω。
这里消费的是 ζ 自身四矩；没有把 |ζζ′|² 的均值错当 ζ′ 的四矩。

## 3. 固定长内层：Euler、Abel Fourier 和全部无限尾

令 N=floor(10T)，
\[
 W_N(s)=\sum_{j\le N}j^{-s},\qquad
 W_{\log,N}(s)=\sum_{j\le N}(\log j)j^{-s}.
 \tag{6}
\]
以下 lemma 不使用 [Rθ]。统一于
\[
 1/2\le\sigma\le3/4,\quad T/9\le|\tau|\le5T,\quad s=\sigma+i\tau,
\]
有
\[
 W_N(s)=\zeta(s)+O(T^{-\sigma}).
 \tag{7}
\]
这只用于正高度 guard；同样证明涵盖负 τ，但不包含 τ=0 的相干峰。

对整数 N，Euler 的确切续延式为
\[
 \zeta(s)=W_N(s)+\frac{N^{1-s}}{s-1}
       -\frac12N^{-s}
       -s\int_N^\infty\psi(u)u^{-s-1}du,
 \quad \psi(u)=\{u\}-1/2.
 \tag{8}
\]
先在 Re(s)>1 以计数函数逐式积分证明，再续延到 Re(s)>0、s≠1；
该积分在 σ>0 绝对收敛。原主极点项明确保留，
其正 guard 费用为 O(N^(1−σ)/|s−1|)=O(T^(−σ))。

为避免 Fourier 的不绝对收敛换序，先取 Abel 正则化
\[
 \psi_r(u)=-\sum_{h\ne0}\frac{r^{|h|}}{2\pi ih}e^{2\pi ihu},
 \qquad 0<r<1.
 \tag{9}
\]
这是 ψ 的周期 Poisson 平均，sup≤1/2；
r↑1 时在非整数处趋于 ψ，整数集合对积分无影响。
固定 r 的 Fourier series 绝对收敛，因此可与 (8) 的积分换序；
之后用 u^(−σ−1) 的可积 domination 取 r↑1。

逐非零频率的相位是
\[
 \Phi_h(u)=2\pi hu-\tau\log u,\quad
 |\Phi'_h(u)|\ge2\pi|h|-|\tau|/N\ge\pi|h|,\quad
 |\Phi''_h(u)|\le|\tau|/u^2,
 \tag{10}
\]
其中 T 足够大使 N≥9T。一次真实积分分部给
\[
 \begin{split}
 \left|\int_N^\infty u^{-\sigma-1}e^{i\Phi_h(u)}du\right|
 &\ll \frac{N^{-\sigma-1}}{|h|}
 +\frac1{|h|}\int_N^\infty u^{-\sigma-2}du
 +\frac{|\tau|}{h^2}\int_N^\infty u^{-\sigma-3}du\\
 &\ll\frac{N^{-\sigma-1}}{|h|}.
 \end{split}
 \tag{11}
\]
所有常数统一于上述 σ、τ 域。再乘 (9) 的 1/|h|，
完整 Σh^(-2) 绝对收敛，统一于 r。
故原无限积分为 O(N^(−σ−1))，乘 |s|=O(T) 后为 O(T^(−σ))。
与主极点及端点项合并证明 (7)。
这一步支付了完整无限 u-tail，没有截去一个未知振荡 remainder。

(7) 的差 W_N−ζ 在每个所用 c/2 圈内解析，因为其虚部≈T，
没有 pole 1；N 是同一个固定整数，不在 Cauchy 圈上改变。
圈上 Re(s)≥σ−c/2，且 T^(c/2)=O(1)，故 Cauchy 得
\[
 W_{\log,N}(s)=-\zeta'(s)+O(T^{-\sigma}L)
 \quad \text{在实际 }s=1/2+c-i(t-\omega).
 \tag{12}
\]
结合 (3)、(5) 和 (7)，
\[
 \sup_{|\omega|\le T/8}\|W_N(1/2+c-i(t-\omega))\|_{4,T}\ll L,
 \quad
 \sup_{|\omega|\le T/8}\|W_{\log,N}(1/2+c-i(t-\omega))\|_{4,T}\ll L^2.
 \tag{13}
\]

## 4. 延长有限多项式并不改变原共同 sharp 函数

给定外部有限因子 D(s)=Σ_{m≤M}d_m m^(−s)，
原两端 product cut 为 Y<mj≤X。
把内层 j≤floorX 延长为 j≤N，N>X：
每个新增 j>X 与 m≥1 的 product 均>X，
因此原真实系数 n≤X 完全不变。
对三因子 mdj 同理，m,d≥1 保证新增 j>X 的所有系数也在 n>X。

这不允许直接丢掉这些额外系数。先保留完整有限矩形 product，
再使用 x♯=floorX+1/2、y♯=floorY+1/2，
\[
 K_{X,Y}(w)=\frac{(x^\sharp)^w-(y^\sharp)^w}{w},
 \quad w=c+i\omega,\quad |\omega|\le T/8.
 \tag{14}
\]
对其全部 normalized n 系数，若实际 |γ_n|≤Cφτ3(n)/√n、
product support n≤Z≪X^z、z<2，
冻结有限 Perron 逐项误差证明原样给
\[
 O_{\phi,\eta}\left(
 X^{2\eta}\{\sqrt Z/T+\sqrt X\,T^{-1}\log(2X)\}\right).
 \tag{15}
\]
远端包括所有额外 n>X，近端对两个半整数距离作 harmonic sum。
N/X≈20π 是固定常数，所有 (x/n)^c 因子和日志比较只改变固定常数；
原 proof 不要求 N/X=1。下面逐对象核 coefficient 和 z<2，
而不是把有限 product 換成无限 Dirichlet series。

又
\[
 \int_{-T/8}^{T/8}|K_{X,Y}(c+i\omega)|d\omega\ll L.
 \tag{16}
\]
这是合法外层 L4 Minkowski 的总质量；不能消去这一日志或把共享 ω 改成独立移位。
外层没有跨 ζ 零点：它用的是有限、全纯的 product。

## 5. 原 short Λ/μ 项的长 ζ 四矩付款

取原一般域
\[
 0<v<a,\quad v<1/4,\quad \max(1/2,a+v)<y<1,\quad
 U=V=\lfloor X^v\rfloor,\ A=\lfloor X^a\rfloor,\ Y=X^y.
 \tag{17}
\]
对任意 U≤B<A、q(m)=1 或 1_prime，
\[
 S_{B,A,q}(t)=-\frac1{a_LL}
 \sum_{\substack{B<m\le A,\ k>V\\Y<mk\le X}}
 \frac{\Lambda(m)q(m)b_V(k)}{\sqrt{mk}}(mk)^{it},
 \quad b_V(k)=\sum_{d\mid k,d\le V}\mu(d).
 \tag{18}
\]
AV<Y 强制原 k>V，但共同乘积掩码不换成矩形。
展开原 b_V 后，外层 finite Perron 用
F_(B,A,q)(s)G_V(s)W_N(s)；完整 support Z=AVN≈X^(1+a+v)<X²。
这里 F_(B,A,q)(s)=Σ_(B<m≤A)Λ(m)q(m)m^(−s)，G_V(s)=Σ_(d≤V)μ(d)d^(−s)。
normalized product 系数
\[
 \gamma_n=-\frac1{a_LL\sqrt n}
 \sum_{\substack{mdj=n\\B<m\le A,\ d\le V,\ j\le N}}
 \Lambda(m)q(m)\mu(d)
\]
对所有 n≤Z 有 |γ_n|≤Cφτ3(n)/√n，包括 n>X。
所以 (15) 为真负幂，只需 η 在固定 1−a−v 的余量之前选小。

在同一个实际 s=1/2+c-i(t−ω)，484 已证全 prefix/+c/guard 给
\[
 |F_{B,A,q}(s)|\ll A^\alpha T^\rho+\sqrt A/T
 +\sqrt A\,T^{-2}\{\log^2(2A)+\log T\},\qquad
 |G_V(s)|\ll V^\alpha T^\rho.
 \tag{19}
\]
这些合同含全部 Λ pole、无限 internal tail、prime mask 和端点费用。
先恢复真实 product mask，再以 (13) 和共享 ω 的 L4 Minkowski，
\[
 \|S_{B,A,q}\|_{4,T}
 \ll (AV)^\alpha T^{2\rho}L^C
       +\sqrt A\,T^{-1}V^\alpha T^\rho L^C
       +\text{更小 internal Λ tails}+\text{(15)}.
 \tag{20}
\]
此处没有把 W_N 的四矩和另外两个未知四矩相乘；
只对已证 pointwise F、G 使用 sup，W 用真实正高度均值。
Λ pole 项的 norm 指数 a/2−1+vα+ρ<−1/2+ρ，
所有显示的非主项可保持真负幂。

任意最终 ε 先分配 4δ(a+v)、8ρ 与日志，严格得
\[
 \boxed{\mathcal M_{S_{B,A,q}}
       \ll_{\phi,\theta,v,a,y,\epsilon}X^{2\beta(a+v)+\epsilon}.}
 \tag{21}
\]
不需要把原二矩改成长矩形的二矩；本次直接支付短项 L4。
旧 Weyl 费用 1/3+β(a+v) 仍有效，两者可各按适用费用消费；
(21) 并非在所有 a 下都较小。

## 6. 原 Type I 的完整 4v 付款

原 Vaughan 恒等式保持
\[
 g_{U,V}(d)=-\sum_{\substack{mb=d\\m\le U,\ b\le V}}\Lambda(m)\mu(b),
 \quad D=UV,
\]
\[
 I_2(t)=\frac1{a_LL}\sum_{d\le D}\frac{g_{U,V}(d)}{\sqrt d}d^{it}
                  \sum_{Y/d<j\le X/d}j^{-1/2+it},
\]
\[
 I_3(t)=\frac1{a_LL}\sum_{d\le V}\frac{\mu(d)}{\sqrt d}d^{it}
                  \sum_{Y/d<j\le X/d}(\log j)j^{-1/2+it}.
 \tag{22}
\]
这两式来自原 477 的相同 finite identity，两个对象均保留 Y<dj≤X。

I2 外 Perron product 为 Γ_(U,V)(s)W_N(s)；
这里 Γ_(U,V)(s)=Σ_(d≤UV)g_(U,V)(d)d^(−s)。
其 support Z2=DN≈X^(1+2v)<X²。
Γ 的 normalized product 系数对全部 n≤Z2（包括 n>X）
由 |g(d)|≤τ(d)logU、Σ_(d|n)τ(d)=τ3(n) 给 Cφτ3(n)/√n。
I3 的 product 为 G_V(s)W_log,N(s)，support Z3=VN≈X^(1+v)；
logj≤logN=O(L)，normalized 系数≤Cφτ(n)/√n。
因此两者的全部额外系数分别由 (15) 支付；
主误差指数 v−1/2 与 (v−1)/2 都严格为负，先选 η 足够小。

保持真实 g，而不是换成任意 μ：
\[
 \sum_{d\le UV}\frac{|g_{U,V}(d)|}{d^{1/2+c}}
 \le\left(\sum_{m\le U}\frac{\Lambda(m)}{\sqrt m}\right)
      \left(\sum_{b\le V}\frac{|\mu(b)|}{\sqrt b}\right)
 \ll\sqrt{UV}\log(2U),
 \quad
 \sum_{d\le V}\frac{|\mu(d)|}{d^{1/2+c}}\ll\sqrt V.
 \tag{23}
\]
不在这两项中认领新 μ 相消。
用 (13)、(16) 和原 normalizer 直接得到
\[
 \|I_2\|_{4,T}\ll X^v L^C+\text{负幂误差},\qquad
 \|I_3\|_{4,T}\ll X^{v/2}L^C+\text{负幂误差},
\]
\[
 \boxed{\mathcal M_{I_2+I_3}\ll_{\phi,v,y,\epsilon}X^{4v+\epsilon}.}
 \tag{24}
\]
实际 sharp 下端、上端和共同外移位没有删除。
在本稿最优 v≤1/8 范围，4v 改善旧 1/3+2v 费用；其他 v 须分别比较两条合同。
这不是直接消费抽象 ζ′ moment 到另一 masked 家族。

## 7. H=V² 的新完整费用族

原 lower block、large proper powers 和完整 squarefull r>H tail 保持旧证明，
分别付 2y−1、1−2a、1−4v；本次用 (21)、(24) 替换两个中间付款。
合成误差的费用为
\[
 C=\max\{2y-1,\ 4v,\ 2\beta(a+v),\ 1-2a,\ 1-4v,\ 0\}.
 \tag{25}
\]
原 squarefull-k 的独立 1/2 合同若另消费，也被 max{4v,1−4v}≥1/2 吸收；
本主分区直接使用完整 r>H 尾，未遗漏该费用。
H=V² 不变，a=2v 的主参数给精确 V²≤floorX^(2v)=A。
最终 r≤H 的 pure-squarefull k=r 原 b_V(k)=0；
非零 core 仍有 s(k)≥2、s(k)rad(r(k))>V。
m>A 为 prime 自动 (m,r)=1，不添 (m,s)=1。

从 proper/tail 得 a≥(1−C)/2、v≥(1−C)/4；
4v 与 tail 给 C≥1/2，short 给
\[
 C\ge\frac32\beta(1-C),\qquad
 C\ge\frac{3\beta}{2+3\beta}.
\]
该新费用族的最优值为
\[
 \boxed{c_\theta=\max\left\{\frac12,\frac{6\theta-3}{6\theta-1}\right\}.}
 \tag{26}
\]
当 θ≤5/6，取 v=1/8、a=1/4、y=3/4；
low、Type I、proper、tail 均1/2，short=3β/4≤1/2。
当 θ≥5/6，Dθ=6θ−1，取
\[
 v=\frac1{2D_\theta},\quad a=\frac1{D_\theta}=2v,\quad
 y=\frac{6\theta-2}{D_\theta},\quad c=\frac{6\theta-3}{D_\theta}.
 \tag{27}
\]
low、short、proper、tail 同为 c；Type I=2/Dθ≤c，
差为 (6θ−5)/Dθ≥0。
所有 (17) 前件成立，两个分支在 θ=5/6 接合。
这是所列费用族与 H=V² 的最优性，不是所有算术方法的最优性。

## 8. θ=7/8 的真实余项及完整传递

取
\[
 U=V=\lfloor X^{2/17}\rfloor,\quad A=\lfloor X^{4/17}\rfloor,\quad
 H=V^2,\quad Y=X^{13/17}.
 \tag{28}
\]
(25) 五项依次为 (9/17,8/17,9/17,9/17,9/17)。
原 Vaughan 顺序的实际 finite partition 支付 lower、Type I、
全部 short m、large proper m 和 large prime m 的 r>H 尾。
其余严格为
\[
 R(t)=-\frac1{a_LL}
 \sum_{\substack{m>A,\ m\ {\rm prime}\\k>V,\ r(k)\le H\\Y<mk\le X}}
 \frac{\Lambda(m)b_V(k)}{\sqrt{mk}}(mk)^{it},
 \quad r(k)=\prod_{v_p(k)\ge2}p^{v_p(k)}.
 \tag{29}
\]
保留原 Λ(m)、b_V(k)、负号、normalizer、全部 aspect ratios 和 product masks。
本对象的 V,Y 与 484 不同，不能把它称为旧余项的子族。

scalar proper-power 迁移仍是原同一 sharp 对象的 L4 norm 小量。
先有限次 Minkowski 合成 E=P_H−R，得到 (1) 第一条；
再由 476 的同一 [R7/8] 下 M_PH≪X^(5/7+ε)，
R=P_H−E 继承同幂。
最后严格以
\[
 |\mathcal M_{P_H}-\mathcal M_R|
 \ll \|E\|_{4,T}(\|P_H\|_{4,T}+\|R\|_{4,T})^3
\]
得到
\[
 \frac{3(5/7)+9/17}{4}=\frac{159}{238},\qquad
 \frac57-\frac{159}{238}=\frac{11}{238}.
 \tag{30}
\]
独立有理计算给 43/75−9/17=56/1275、
713/1050−159/238=14/1275。
这只是完整 additive 增长误差；不要求未知主项 lower，
不声称相对主项等价或常数级 o(1)。

## 9. 保持冻结 484、482 对象的真实 prime-band 扩大

保持 484 的 V=floorX^(8/75)、A0=floorX^(16/75)、H=V²、
Y=X^(59/75) 及全部 b_V，不换其实际余项。
取 A2=floorX^(62/225)。
原 R_(Λμ) 内的 A0<m≤A2、m prime、r≤H 带，先对同 m-band 的全部 k 用 (21)：
\[
 2\beta(a_2+v)=\frac32\left(\frac{62}{225}+\frac8{75}\right)=\frac{43}{75}.
\]
再直接对同带的 r>H 消费原 tail proof。
在 c_r(n) 中加入此 m-mask 后，原 τ(r)τ3(n) coefficient majorant 仍成立，
费用 1−4v=43/75；故 full band−tail 的真实 r≤H 带也付43/75。
精确从旧 R 中减去该带，得到旧配置下 m>A2 的 R2，
P_H−R2 仍付43/75，complete transfer仍713/1050。
A2/A0≍X^(14/225)。这是同一个冻结对象的 cutoff 扩大，
没有由全函数 signed norm推任意子族norm。

完全同理，保持 482 的全部 V=floorX^(8/81)、H、Y=X^(65/81)、b_V，
取 A2'=floorX^(74/243)，
\[
 \frac32\left(\frac{74}{243}+\frac8{81}\right)=\frac{49}{81},
 \qquad \frac{74}{243}-\frac{16}{81}=\frac{26}{243}.
\]
全部 k 带和同带 r>H 各付49/81，差后得到真实 core-band。
旧配置下剩余 m>A2' 的误差仍49/81、传递仍779/1134。
Λ prefix 对全部 N≤X 已证，因此 a2,a2'>1/4 不违规；
μ 的 v 仍<1/4，且各自 a+v<y。两种旧配置与 (28) 分别消费。

## 10. 不使用 [Rθ] 的 3/5 完整误差推论

本节的无条件用途由 checkpoint_audit 在同轮独立研究中提示。
不调用 (19) 的无零前件；直接在真实 s=1/2+c-i(t−ω) 上用
\[
 |F_{B,A,q}(s)|\ll\sqrt A\log(2A),\qquad |G_V(s)|\ll\sqrt V.
\]
外层 finite coefficients、两 sharp endpoints、全部额外 n>X 和 (15) 不变。
将这两个 trivial 上界放入同一共享 ω 的 Minkowski，再用无条件 (13)，
得真实短项 M_S≪X^[2(a+v)+ε]。
原 Type I 的 4v、lower、proper-power 及完整 tail 付款均不使用 [Rθ]。

取 U=V=floorX^(1/10)、A=floorX^(1/5)、H=V²、Y=X^(4/5)，
一般域、精确 floor core 和原系数分区仍成立。
五项费用 (2y−1,4v,2(a+v),1−2a,1−4v) 精确为
(3/5,2/5,3/5,3/5,3/5)。
将 (29) 里的参数替换为这一组，定义其同一个原形式的 R0，
再合成完整实际误差 E0=P_H−R0，严格得到
\[
 \boxed{\mathcal M_{E_0}\ll_{\phi,\epsilon}X^{3/5+\epsilon}
        \quad\text{不假设 }[R_\theta].}
 \tag{31a}
\]
与 481 已有无条件 13/21 误差相比，省 13/21−3/5=2/105。
本节没有给 R0 或 whole P_H 新的无条件四矩上界；
不能把条件 476 的增长输入自动用于本节的无条件传递。
这也不提供中心四阶常数、实际零点比例或无零区域。

## 11. 既有 θ* 的新应用与真正未付款范围

对 476 已证明的 5/6<θ≤7/8 域，cθ≤9/17<19/30≤B_I(θ)，
故相同 norm 差先使 R 继承 B_I，再得
\[
 \mathcal M_E\ll X^{c_\theta+\epsilon},\qquad
 \mathcal M_{P_H}=\mathcal M_R+
 O\!\left(X^{[3B_I(\theta)+c_\theta]/4+\epsilon}\right).
 \tag{31}
\]
这里 B_I(θ)=4θ−3+3(1−θ)/(2θ) 是已有 whole 输入。

保留 451 的完整相对输入包及其普通 ζ transfer 后，
可消费既有 θ*=11/12−e*/4；本稿不降低那些依赖或产生新 boundary。
精确
\[
 c_*=\frac{5-3e_*}{9-3e_*},\quad
 v_*=\frac1{9-3e_*},\quad a_*=2v_*,\quad
 y_*=\frac{7-3e_*}{9-3e_*}.
\]
451 的有理根区间、cθ 与 B_I 单调性给
c*∈(.5293832084010138,.5293832084010156)，
[3B_I(θ*)+c*]/4∈(.6679943043150209,.6679943043150252)。
这些是严格外包围的有理十进制端点，有限 Fraction 只核此代数，
不代替本稿的无限估计。

原完整 C4 生成函数仍为 (Dζ−F_U)(1−ζG_V)。
ζ 零点 ρ 的 residue 仍为 −mρ，因为 1−ζ(ρ)G_V(ρ)=1。
长 W_N 的延伸只是有限 product 消费，没有为该零点包添加衰减。
普通 ζ 四矩只支付一个无权长内层；另外两个因子仍靠已证 prefix pointwise，
并没有得到真正 balanced prime/squarefree signed mixed4 的新联合相消。
在较长 a 域，(21) 甚至可能比旧 Weyl 费更差，应保留两条已证合同分别比较。

所以本稿完成的是新 Type I、真实短项、完整误差、传递及固定对象的 band 付款。
原 whole 5/7、中心四阶常数、已知简单零点比例和既有无零边界均未改善。
未执行有限素数实验、旧重型检查或生成输出；没有用数值采样认证无限证明。

