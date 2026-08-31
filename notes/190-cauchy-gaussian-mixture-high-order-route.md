# NCE-8：Cauchy--Gaussian 尺度混合与高阶消失路线

文档 188--189 把 degree-two soft response 的 exact products 无条件撤离，剩余
困难是 signed near products。一个自然想法是把 Cauchy trace 换成 Gaussian
trace，再对平衡素数测度反复分部积分。本笔记证明：直接换核会破坏 bounded-defect
normality 的尾部接口；但 Cauchy state 本身是 Gaussian states 的精确
Gamma mixture。因此可以同时保留 Cauchy 的全高度检测能力和 Gaussian 的高阶
平滑性。

所得分解把未解的 near sector 缩成两个定量对象：

1. 非尖 Gaussian scales 上的 repeated-primitive discrepancy powers；
2. 尖尺度上的 multiplicative heat small-ball energy。

前者可由经典 PNT 累积误差驱动；后者是新的、比 hard near bucket 更窄的算术
目标。另一个非构造结果说明，soft negative effect 可由具有任意指定高阶零点的
多项式逼近，使 Gaussian response 从任意高 convolution order 开始。代价是
coefficient conditioning，不能省略。

## 1. 为什么不能直接把 Cauchy trace 换成 Gaussian trace

令

$$P_a(t)=\frac{a}{\pi(a^2+t^2)},\qquad a>0,$$       (1)

是右半平面的 Poisson kernel。文档 145 的 normality proof 需要：对每个固定
interior compact set，任意 nonnegative boundary defect $W$ 的 Poisson integral
由一个 trace weight $w$ 控制。抽象成一个点即要求

$$\int P_a(t)W(t)\,dt\le C_a\int w(t)W(t)\,dt$$    (2)

对所有 $W\ge0$ 成立。

### 定理 AGL（Poisson-tail / Fourier-cusp obstruction）[U]

若式 (2) 对所有 nonnegative measurable $W$ 成立，则

$$P_a(t)\le C_aw(t)\quad\text{a.e.},$$             (3)

所以 $w(t)\ge c/(1+t^2)$ 在大 $|t|$ 上成立。若 $w$ 还是 even probability
density，characteristic function

$$K(x)=\int\cos(tx)w(t)\,dt$$                      (4)

在 $x=0$ 不可微；更精确地，

$$\liminf_{x\to0}\frac{1-K(x)}{|x|}>0.$$           (5)

#### 证明

式 (3) 是正锥 $L^1$ duality：若它在正测度集合上失败，取该集合的 indicator
作为 $W$ 即与式 (2) 矛盾。Poisson tail 给 $w(t)\ge c/t^2$。

对充分小的 $x>0$，限制积分到 $1/x\le t\le2/x$。在该区间
$1-\cos(tx)\ge\min_{1\le s\le2}(1-\cos s)>0$，故

$$1-K(x)\ge c\int_{1/x}^{2/x}t^{-2}\,dt\ge c'x.$$ (6)

even characteristic function 若在零点可微，其导数只能为零，从而
$1-K(x)=o(|x|)$，与式 (6) 矛盾。$\square$

因此 Gaussian weight 的快速高度衰减不能通过同一个 universal boundary-defect
argument 推出文档 145 的 normality。Cauchy characteristic
$K_C(x)=e^{-|x|}$ 的 cusp 不是偶然选型，而是 Poisson tail 的 Fourier 影子。

这个 no-go 只针对“由一个固定 trace weight 对任意 boundary negative part 作
Poisson domination”的证明；它不排除使用额外 arithmetic information 的其它
normality argument。

## 2. Cauchy state 的精确 Gaussian mixture

对 $u>0$，令 normalized Gaussian state 为

$$d\mu_u(t)=\sqrt{u/\pi}\,e^{-ut^2}dt,$$            (7)

其 lag characteristic 为

$$K_u(x)=e^{-x^2/(4u)}.$$                           (8)

令

$$m(u)=\frac{e^{-u}}{\sqrt{\pi u}}.$$               (9)

### 定理 AGM（Gamma-mixture identity）[U]

有 probability-state identity

$$\frac{dt}{\pi(1+t^2)}
  =\int_0^\infty m(u)d\mu_u(t)\,du,$$              (10)

以及

$$e^{-|x|}
  =\int_0^\infty m(u)e^{-x^2/(4u)}\,du.$$          (11)

因此对任意 finite signed lag measure $q$，

$$\langle K_C,q\rangle
  =\int_0^\infty m(u)\langle K_u,q\rangle\,du.$$   (12)

#### 证明

式 (10) 的右侧 density 为

$$\frac1\pi\int_0^\infty e^{-u(1+t^2)}\,du
  =\frac1{\pi(1+t^2)}.$$                           (13)

取 Fourier transform 得到式 (11)--(12)。有限 $q$ 时 Fubini 直接适用。
$\square$

截断 mixture 的 exact closed form 是

$$F_U(x)=\int_0^U m(u)e^{-x^2/(4u)}\,du$$

$$=\frac12\left\{
e^{-|x|}\operatorname{erfc}\!\left(\frac{|x|}{2\sqrt U}-\sqrt U\right)
-e^{|x|}\operatorname{erfc}\!\left(\frac{|x|}{2\sqrt U}+\sqrt U\right)
\right\}.$$                                       (14)

特别地 $F_U(0)=\operatorname{erf}(\sqrt U)$，且
$F_\infty(x)=e^{-|x|}$。

## 3. 平衡测度的 repeated-primitive Gaussian bound

令 $\nu$ 是 compactly supported finite real signed measure，且
$\nu(\mathbb R)=0$。定义 cumulative primitive

$$A(x)=\nu((-\infty,x]),\qquad E=\|A\|_1.$$        (15)

### 定理 AGN（Gaussian discrepancy-power bound）[U]

对每个 integer $k\ge0$，

$$|\langle K_u,\nu^{*k}\rangle|
\le
\frac{\Gamma((k+1)/2)}{\sqrt\pi\,u^{k/2}}E^k.$$   (16)

若一般 signed measure 写成

$$d=M\delta_0+\nu,\qquad \nu(\mathbb R)=0,$$       (17)

则

$$|\langle K_u,d^{*k}\rangle|
\le\sum_{j=0}^k {k\choose j}|M|^{k-j}
\frac{\Gamma((j+1)/2)E^j}{\sqrt\pi\,u^{j/2}}.$$  (18)

#### 证明

distribution 意义下 $\nu=DA$，所以

$$\nu^{*k}=D^k(A^{*k}).$$                          (19)

反复分部积分并用 Young inequality 给

$$|\langle K_u,\nu^{*k}\rangle|
\le\|K_u^{(k)}\|_\infty\|A^{*k}\|_1
\le\|K_u^{(k)}\|_\infty E^k.$$                   (20)

由式 (7)--(8)，

$$\|K_u^{(k)}\|_\infty
\le\int |t|^k\,d\mu_u(t)
=\frac{\Gamma((k+1)/2)}{\sqrt\pi\,u^{k/2}}.$$    (21)

展开式 (17) 的 convolution power 得式 (18)。$\square$

这个 theorem 与逐 product absolute counting 不同：每个 centered prime--
continuum discrepancy factor 都真正贡献一个 cumulative PNT error $E$。

## 4. Degree-two broad-scale bound 与 fixed-degree barrier

沿文档 188，degree-two response frequency measure 为

$$q_2=-c^2d^{*3}*(d-aB\delta_0)^{*2},$$           (22)

其中 $a=\sqrt3/2$。这是

$$-c^2[d^{*5}-2aB d^{*4}+a^2B^2d^{*3}]$$         (23)

的 factorized 版本。

把式 (18) 的右侧记为 $G_k(u;M,E)$，则

$$|\langle K_u,q_2\rangle|
\le c^2[G_5+2aB G_4+a^2B^2G_3].$$               (24)

若在固定 $u\ge u_0>0$ 上

$$|M|+E/\sqrt{u_0}\le B\delta,\qquad\delta\le1,$$ (25)

则式 (24) 给

$$|\langle K_u,q_2\rangle|\le C_{u_0}B\delta^3.$$ (26)

对 Abel prime--continuum discrepancy，经典 PNT zero-free region 无条件给某个
$\delta_Y\to0$ 的 weighted cumulative discrepancy estimate；但
$B_Y\asymp Y^{1-\sigma}$。固定 degree two 的

$$B_Y\delta_Y^3$$                                  (27)

不由经典 PNT 自动一致有界。例如仅用
$\delta_Y=\exp[-c\sqrt{\log Y}]$ 时，式 (27) 仍可发散。

所以 Gaussian smoothing 是实质改进，但它本身没有证明 RH。它精确显示：
fixed-degree route 仍不够，必须增加 convolution vanishing order，或得到比经典
PNT 强得多的 response-specific cancellation。

## 5. 任意高阶零点的非构造 soft-effect approximation

令

$$I_0=\{f\in C([-B,B]):f(0)=0\}.$$                (28)

### 定理 AGO（high-order ideal density）[U]

对任意固定 integer $r\ge1$，ideal

$$x^r\mathbb R[x]$$                                (29)

在 $I_0$ 的 uniform norm 中稠密。特别地，对 soft negative effect
$a_\rho$ 及任意 $\epsilon>0$，存在 polynomial

$$p_{r,\epsilon}(x)=x^rs_{r,\epsilon}(x)$$        (30)

满足

$$\|p_{r,\epsilon}-a_\rho\|_\infty\le\epsilon.$$  (31)

#### 证明

由 $f(0)=0$ 的连续性，选 $\delta>0$ 使 $|f(x)|\le\epsilon/3$ 当
$|x|\le2\delta$。取 continuous cutoff $\chi$，在 $|x|\le\delta$ 为零，在
$|x|\ge2\delta$ 为一。函数

$$g(x)=\chi(x)f(x)/x^r$$                           (32)

在零点定义为零后连续。由 Weierstrass theorem，取 polynomial $s$ 使

$$\|s-g\|_\infty\le\epsilon/(3B^r).$$             (33)

于是 $x^rs$ 与 $\chi f$ 相差至多 $\epsilon/3$，而 $(1-\chi)f$ 至多
$\epsilon/3$；放宽常数即得式 (31)。$\square$

若在定理 AGB 中使用式 (30)，signed response

$$-x p_{r,\epsilon}(x)^2$$

从 degree $2r+1$ 开始。结合定理 AGN，在每个 fixed non-cusp Gaussian scale
上，PNT discrepancy 因而可出现任意高次幂。

这是一个真正的非构造存在性结论：不读取 zeros 或 negative eigenvectors，只用
$a_\rho(0)=0$。但它还不是 RH proof，因为：

- cutoff 变窄时 $s_{r,\epsilon}$ 的 degree 与 coefficient norms 可极大；
- Chebyshev/orbit $L^1/L^2$ conditioning 必须进入 response bound；
- Cauchy mixture 的 $u\to0$ sector 尚未由定理 AGN 一致控制；
- polynomial approximation error $\epsilon\tau(|H|)$ 仍须共尾可和。

## 6. 尖尺度被缩成 heat small-ball energy

由式 (14)，对 $x\ne0$，

$$0\le F_U(x)\le
\operatorname{erf}(\sqrt U)e^{-x^2/(4U)}.$$       (34)

因此对 finite response map $q$，

$$\langle K_C,q\rangle_{0<u<U}
=\operatorname{erf}(\sqrt U)q(\{0\})
 +\sum_{\ell\ne0}q_\ell F_U(\ell),$$              (35)

且 nonexact variation 满足

$$\le\operatorname{erf}(\sqrt U)H_q(U),$$         (36)

其中

$$H_q(U)=\sum_{\ell\ne0}|q_\ell|
                 e^{-\ell^2/(4U)}.$$             (37)

称 $H_q(U)$ 为 multiplicative heat small-ball energy。它只读取
$|\log(\text{product ratio})+\text{continuum shift}|\lesssim\sqrt U$，并对较远
products 作 Gaussian 衰减；这严格窄于文档 188 的 hard near variation。

文档 189 已控制 degree-two 的 formal exact coefficient $q(\{0\})$。所以 NCE-8
现在可表述为：

1. 选 $U_Y$；
2. 用定理 AGN 控制 $u\ge U_Y$ 的 broad Gaussian mixture；
3. 证明 $\operatorname{erf}(\sqrt{U_Y})H_{q_Y}(U_Y)=O(1)$；
4. 同时控制 high-order approximant conditioning 与 explicit-formula errors。

第三项是当前唯一保留的 ultra-near arithmetic input。它适合用 multiplicative
large sieve、Mellin heat kernel 或 Selberg--Volterra summation-by-parts 研究，
而不再要求全部 hard near tuples 的 absolute bound。

## 7. Frozen finite audit

脚本 scripts/audit_soft_zeta_orbit.py 先把原 outer/effect/effect triple response
精确合并为式 (22)，再按

$$[0,.01],[.01,.04],[.04,.16],[.16,.64],
  [.64,2.56],[2.56,\infty]$$

分解 Gaussian mixture。对 $Y=8,N=10,L=2$：

| Gaussian $u$ band | signed | exact | nonexact | variation | $|signed|/$variation |
|---:|---:|---:|---:|---:|---:|
| $0--.01$ | $.002563$ | $.003522$ | $-.000958$ | $.008590$ | $.2984$ |
| $.01--.04$ | $.000213$ | $.003452$ | $-.003239$ | $.01973$ | $.01079$ |
| $.04--.16$ | $.000380$ | $.006441$ | $-.006061$ | $.07181$ | $.005293$ |
| $.16--.64$ | $.000832$ | $.009824$ | $-.008992$ | $.2082$ | $.003997$ |
| $.64--2.56$ | $.000480$ | $.007336$ | $-.006856$ | $.2617$ | $.001834$ |
| $2.56--\infty$ | $.0000264$ | $.000741$ | $-.000714$ | $.03735$ | $.0007055$ |

六带 signed sum 为 $.00449488$，与原 Cauchy response 在 $2\cdot10^{-10}$ 内
一致。最尖 band 的 nonexact signed contribution 只有 $-.000958$；主要
exact/near cancellation 分布在中尺度，而不是集中在不可分辨的最小 product
gaps。

在单 Gaussian scale 上，式 (24) 的有限上界随 $u$ 变宽而快速改善：冻结模型
中 upper/actual ratio 从 $u=.16$ 的约 $82.8$ 降到 $u=2.56$ 的约 $3.94$，
在 $u=10.24$ 为约 $2.59$。这支持 broad-scale repeated-primitive route，但不
构成 cofinal estimate。

所有数字均为 double-precision diagnostics，不是 interval proof 或 RH evidence。

## 8. 与广义结构定理的接口

定理 AGL--AGO 给 bounded finite-trace Hodge--Weil theorem 增加一个新的
constructive/nonconstructive factorization：

- **global detection**：Cauchy tail 保留 Poisson normality；
- **scale resolution**：Gamma mixture 把 Cauchy trace 分成 Gaussian fibers；
- **arithmetic smoothing**：每个 broad fiber 用 cumulative discrepancy powers；
- **nonconstructive effect existence**：high-order ideal density 自动给任意
  convolution vanishing order；
- **remaining constructive input**：heat small-ball energy 与 coefficient
  conditioning。

它没有假设完整 Weil positivity，也没有使用 zeros。若 heat small-ball bound
最后被证明等价于 full Selberg profile，则该分支必须标记为等价重述；目前式
(37) 是更窄、带 canonical response coefficients 与 Gaussian scale 的对象，
尚未发现这种等价。

## 9. 下一步

1. 为式 (37) 建立 dyadic product-ratio shell identity，保留 $q_Y$ 的 signs；
2. 把文档 184 的 Volterra prefix transport 改写为 Gaussian Mellin heat flow；
3. 构造 constrained Chebyshev approximants $x^rs(x)$，审计 degree、
   coefficient $L^1/L^2$ growth 与 approximation error；
4. 推广文档 189 的 exact parity/$L^2$ bound 到高阶 constrained response；
5. 在 $Y=4--32$ 的 cofinal toy grid 上联合优化 $r,U,\rho$，只把趋势用作
   falsification，不作 RH 外推。

## 10. 审计结论

直接 Gaussian 换核因 Poisson tail/cusp obstruction 不可行；Gaussian 尺度混合
则是 exact 且兼容 normality 的修复。它把 near-resonance 障碍拆成一个可由
经典 PNT 驱动的 broad-scale discrepancy-power 部分，以及一个明确的 ultra-near
heat small-ball energy。high-order ideal density 又提供了不读取谱位置的
非构造 vanishing-order amplification。当前真正需要攻克的对象已从“全部近乘积”
缩小到式 (37) 与其 constrained-polynomial conditioning。
