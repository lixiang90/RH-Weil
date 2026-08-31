# Cotangent DFT、Kloosterman-fraction 接口与黑箱适用性审计

文档 091 证明 coprime determinant kernel 虽由两个可能很大的 cotangent
组成，其和却一致有界。本节把每个 cotangent 精确作有限 Fourier 变换，因而
把 modular inverse 明确变成 Kloosterman-fraction phase；同时证明一个必须
保留的限制：若把两个 reciprocal terms 分开取绝对值，恰会丢掉产生一致界的
reciprocity cancellation。现有 DFI 与 Bettin--Chandee 估计提供了正确的
局部工具，但其定理陈述本身尚不自动推出所需的全 dyadic budget。

以下记 `e(x)=exp(2 pi i x)`。

## 1. Cotangent 的精确有限 DFT

### 定理 RZ（finite cotangent transform）

对整数 `q>=2` 及 `1<=k<q`，

`sum_(j=1)^(q-1) cot(pi j/q)e(jk/q)=i(q-2k)`.        (1)

因此 Fourier inversion 给

`cot(pi k/q)`

` =i/q sum_(j=1)^(q-1)(q-2j)e(-jk/q)`.              (2)

而且变换系数与 cotangent grid 的精确平方质量分别为

`sum_(j=1)^(q-1)|(q-2j)/q|^2`

`                 =(q-1)(q-2)/(3q)`,                (3)

`sum_(k=1)^(q-1)cot^2(pi k/q)`

`                 =(q-1)(q-2)/3`.                   (4)

#### 证明

令 `zeta_q=e(1/q)`，并把式 (1) 左侧记作 `F(k)`。由

`cot(pi j/q)=i(zeta_q^j+1)/(zeta_q^j-1)`            (5)

可得

`F(k+1)-F(k)`

` =i sum_(j=1)^(q-1)[zeta_q^((k+1)j)+zeta_q^(kj)]`. (6)

`F(0)=0`；从 `k=0` 到 `1`，式 (6) 等于 `i(q-2)`；以后每一步两项
geometric sums 都等于 `-1`，故差为 `-2i`。这证明式 (1)，有限 Fourier
反演给式 (2)。对 arithmetic progression `q-2j` 直接求平方和给式 (3)，
Parseval 再给式 (4)。`□`

式 (3) 是后续估计的 conditioning audit：单个 modulus `q` 的 Fourier
coefficient norm 是 `asymp sqrt(q)`，并不是 uniform constant。

## 2. Farey kernel 成为成对 Kloosterman fractions

设 `(a,b)=1`、`a,b>1`、`(delta,ab)=1`，并令 `bar a`、`bar b` 分别是
`a mod b`、`b mod a` 的逆元。文档 091 给出

`U_(a,b)(delta)`

` =-pi/delta[cot(pi delta bar a/b)`

`                    +cot(pi delta bar b/a)]`.       (7)

### 定理 SA（paired Kloosterman-fraction expansion）

有精确有限公式

`U_(a,b)(delta)=-pi i/delta * {`

`  1/b sum_(j=1)^(b-1)(b-2j)e(-j delta bar a/b)`

` +1/a sum_(k=1)^(a-1)(a-2k)e(-k delta bar b/a)}`.  (8)

式 (8) 中每一相位都是标准 Kloosterman fraction。两个 braces terms 必须
作为一个 reciprocity pair 处理；其和满足

`|U_(a,b)(delta)|<=pi^2/4`,                          (9)

但任何逐项 pointwise bound 都不可能一致于 `a,b`。

#### 证明

把定理 RZ 分别以 `(q,k)=(b,delta bar a)` 与
`(a,delta bar b)` 代入式 (7)，即得式 (8)。式 (9) 是定理 RS。最后取
`a=b+1`、`delta=1`：第一个 cotangent 是 `cot(pi/b) asymp b/pi`，第二个
是 `-cot(pi/(b+1)) asymp -(b+1)/pi`。各项线性增长，而和有界。`□`

这还解释了 dyadic bookkeeping 的正确单位：`(a,b)` block 必须与 transpose
`(b,a)` block 配对。若先对每个有向 block 或每个 cotangent 取绝对值，式
(9) 的相消就不可恢复。

## 3. 共同模数上的 reciprocity-preserving DFT

式 (8) 仍把两个 cotangents 写在不同模数上。inverse reciprocity 允许把它们
先合成一个共同模数 `q=ab` 的 finite difference。

### 定理 SB（product-modulus paired transform）

置

`q=ab`,  `n=delta a bar a (mod q)`.                  (10)

则

`cot(pi delta bar a/b)+cot(pi delta bar b/a)`

` =cot(pi n/q)-cot(pi(n-delta)/q)`,                  (11)

从而

`U_(a,b)(delta)=-pi i/delta *sum_(j=1)^(q-1)`

` [(q-2j)/q][1-e(jdelta/q)]e(-jn/q)`.                (12)

这是单一 product-modulus Kloosterman transform。difference multiplier 满足

`|1-e(jdelta/q)|<=2pi min_(ell in Z)|jdelta/q-ell|`; (13)

特别在 `|jdelta|<=q/2` 时，式 (12) 的 `1/delta` 被精确抵消，effective
coefficient 至多为 `2pi j/q`。

#### 证明

inverse reciprocity 给

`delta bar b/a=delta+delta/q-delta bar a/b`.         (14)

cotangent 的 period 为 `pi` 且是 odd function，故第二项等于
`-cot(pi[delta bar a/b-delta/q])`，得到式 (11)。对两个共同模数 `q` 的
cotangents 同时使用定理 RZ；两个 exponentials 的差提出 multiplier
`1-e(jdelta/q)`，得到式 (12)。式 (13) 来自
`|1-e(x)|=2|sin(pi x)|`。`□`

这是比式 (8) 更合适的 analytic normal form：reciprocity cancellation 不再
依赖最后把两个大数相减，而已编码在每个 Fourier mode 的差分乘子中。高频
部分仍可能有 `sqrt(q)` coefficient mass，所以它尚不是最终 bound；但低频
不再支付虚假的 cotangent singularity。

## 4. 线性 conductor amplitude 的 Mellin 分解

在线性 filter `P(u)=1-u` 下，记

`A_N(r)=rS_N(r)`.                                    (15)

若 `r` squarefree，置 `X=N/r`，则文档 090 式 (25) 化为

`A_N(r)=mu(r)/log N * T_r(X)`,                       (16)

`T_r(X)=sum_(m<=X,(m,r)=1)mu(m)/m log(X/m)`.         (17)

### 定理 SC（exact Mellin integral and zero residue）

对任意 `c>0`，

`T_r(X)=1/(2pi i) int_((c)) X^z/[z^2 zeta(1+z)]`

`                    *product_(p|r)(1-p^(-1-z))^(-1) dz`. (18)

`z=0` 是 simple pole，residue 为

`Res_(z=0)=product_(p|r)(1-p^(-1))^(-1)=r/phi(r)`.  (19)

所以形式上的主留数是

`mu(r)r/[phi(r)log N]`.                              (20)

但是式 (20) 不是 hard conductor range 上的 uniform asymptotic。事实上若
`N/2<r<=N`，则式 (17) 只有 `m=1` 一项，故精确地

`A_N(r)=mu(r)log(N/r)/log N`;                        (21)

当 `r=N` 时它为零，而式 (20) 通常非零。

#### 证明

使用 Perron 的 logarithmic kernel

`1_(m<=X)log(X/m)=1/(2pi i)int_((c))(X/m)^z dz/z^2` (22)

及绝对收敛恒等式

`sum_((m,r)=1)mu(m)m^(-1-z)`

` =1/zeta(1+z) product_(p|r)(1-p^(-1-z))^(-1)`      (23)

得到式 (18)。因 `1/zeta(1+z)=z+O(z^2)`，式 (19) 成立。式 (21) 直接由
`1<=X<2` 得到。`□`

若把 contour 左移，`1/zeta(1+z)` 在 `z=rho-1` 处产生 poles；因此要把式
(20) 变成所需 uniform remainder bound，会重新遇到 zeta zeros。端点公式
(21) 更直接地表明：最难区间内必须保留 exact short Möbius sum，不能用
zero-residue main term 替换。

## 5. 现有 Kloosterman-fraction 定理能提供什么

Duke--Friedlander--Iwaniec 研究任意系数的 dyadic bilinear form

`B_a(M,N)=sum_((m,n)=1)alpha_m beta_n e(a bar m/n)`. (24)

其两个无条件界（略去只依赖 `epsilon` 的常数）为

`|B_a|/(||alpha||_2||beta||_2)`

` <<[(M+N)^(1/2)+(1+a/(MN))^(1/2)min(M,N)](MN)^epsilon`, (25)

以及

` <<(a+MN)^(3/8)(M+N)^(11/48+epsilon)`.              (26)

Bettin--Chandee 对任意系数的三线性 form

`B_vartheta(M,N,A)`

` =sum_(a,m,n)nu_a alpha_m beta_n e(vartheta a bar m/n)` (27)

证明

`|B_vartheta| <<||alpha||_2||beta||_2||nu||_2`

` *(1+|vartheta|A/(MN))^(1/2)`

` *[(AMN)^(7/20+epsilon)(M+N)^(1/4)`

`   +(AMN)^(3/8+epsilon)(AN+AM)^(1/8)]`.             (28)

这些定理与式 (8) 的相位完全同型，并且允许 arbitrary coefficients；后者还
明确应用于 determinant equations。因此它们可无条件控制经过 smooth
dyadic separation 的许多单相位 subblocks。

## 6. 为什么不能直接宣布 parabolic block 已闭合

固定式 (8) 的 Fourier index `j` 时，第一项可把

`m=a`, `n=b`, `a_(BC)=delta`, `vartheta=-j`          (29)

代入式 (27)。但随后还必须处理：

1. `1<=j<b` 的 variable-length transform 及权重 `1-2j/b`；
2. determinant length `D roughly gab/Y` 与 moduli 同时变化；
3. shared `g` 的 principal density 与 nonprincipal additive modes；
4. amplitudes 内部的 `m,m'<=N/(ga),N/(gb)` Möbius sums；
5. 所有 dyadic blocks 的 `1/Y` normalization 与总和；
6. 式 (8) 两个 reciprocal transforms 的 cancellation。

也可把 `ell=j delta` 合并成一个频率变量，但 divisor multiplicity、`j<b`
cutoff 及 `1-2j/b` 使 resulting coefficient 依赖 modulus `b`，不再直接是式
(27) 的 product coefficient `nu_ell alpha_a beta_b`。需先作额外 Mellin/Fourier
separation，并逐项追踪其 total variation。

### 命题 SD（black-box loss audit）

只把式 (8) 拆成单模 DFT、对两个 terms 取三角不等式，再把式 (25)--(28)
作为 arbitrary-coefficient black boxes，并不足以从定理陈述本身推出文档
089 所需的 `O(1/log N)` 总界。

#### 证明

定理 RZ 给每个 modulus `q` 的输入 coefficient norm 精确为
`sqrt((q-1)(q-2)/(3q)) asymp sqrt(q)`；定理 SA 的例子又证明两个单项的
pointwise size 可为 `asymp q`，而 paired kernel 一致有界。DFI/BC 的 RHS
分别乘 coefficient `L2` norms，却不含连接两个 reciprocal transforms 的
负相关。除此以外，式 (25)--(28) 只控制一个已分离 block；它们没有替使用者
完成上述六项 coupled summation。故还需一个完整 dyadic budget 或保持
reciprocity pairing 的加强估计。`□`

这不是说 DFI/BC 太弱；它只排除了“看到 Kloosterman phase 后逐项引用定理”
这一不完整论证。它们很可能仍是 amplification/dispersion 证明的核心输入。

共同模数公式 (12) 改善了这一审计：它允许直接分析 paired low modes；但其
modulus 是乘积 `ab`，且 multiplier 同时依赖 `a,b,delta`，仍需新的 separation
或 dispersion argument，不能不经估算便代入式 (25)--(28)。

## 7. Reciprocity-preserving sufficient certificate

### 定理 SE（paired Kloosterman budget implies RH）

取文档 088--091 的 mean-zero、endpoint-bounded candidates。对每个
`N<=Y<=N^(3/2)`，将 principal shared-GCD term 用共同模数公式 (12) 展开
（或等价地将完整 brace (8) 与 transpose dyadic block 一起求和）；
nonprincipal modes 使用同一 paired convention。若经 smooth separation 后：

1. 所有 paired principal Kloosterman blocks 的 normalized dyadic total 为
   `O(1/log N)`；
2. 所有 paired nonprincipal sieve-mode blocks 的 normalized dyadic total
   为 `O(1/log N)`；
3. separation coefficients 的 `L1` cost 是 `N^o(1)`，且已包含在上述
   bounds 中；

则 classical RH 成立。

#### 证明

定理 SB 是文档 091 principal kernel 的 exact identity，不产生 remainder。
定理 RV 对 nonprincipal modes 也是 exact finite Fourier split。两项假设给
定理 RX 的两个 estimates；定理 RO 处理 `Y>=N^(3/2)`，定理 RE 处理所有
resolved sectors，最后定理 RA 推出 Nyman distance 趋零，从而推出 RH。
`□`

相较文档 091 的 criterion，这里的新增内容是把开放估计放进了可直接与
DFI/BC 比较的 exponential normal form，并明确规定必须保留的 transpose/
reciprocity pairing。

## 8. 广义 Euler 数据与下一步

### 结论 SF（the remaining input is a paired dispersion theorem）

本节无条件完成了三件事：

- cotangent determinant kernel 已精确变换为有限 Kloosterman fractions；
- transform 的 conditioning 与 reciprocity cancellation 均被精确量化；
- linear conductor amplitude 的 Mellin 主留数及其端点非一致性已分离。

下一步不是再寻找 pointwise cotangent bound，而是证明一个
reciprocity-preserving dispersion theorem：它应把 `(a,b)` 与 `(b,a)` blocks
联合放大，同时容纳 short determinant、shared-GCD sieve modes 与 Möbius
hyperbola coefficients。对一般 reciprocal Euler 数据，几何 DFT 部分原样
成立；需要替换的仅是 outer coefficient theorem。这正给出“广义 Weil
结构存在性”中一个可移植而又诚实的 analytic axiom。

## 9. 计算实现

`scripts/qw_matrix.py` 新增：

- `finite_cotangent_dft`；
- `coprime_farey_cotangent_dft`；
- `coprime_farey_product_modulus_dft`；
- `euler_totient`；
- `linear_conductor_mellin_data`。

回归测试核对式 (2)--(4)、双模及共同模数 paired DFT 与 reciprocity closed form、线性
conductor finite sum 与原 Fourier amplitude，并显式检查 `N/2<r<N` 的
one-term endpoint regime。
