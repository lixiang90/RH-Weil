# Parity-breaker convolution 与 degree-two exact sector evacuation

文档 188 把 canonical degree-two soft response分成 exact、near、far。有限审计中
exact bucket稳定为正且不可忽略。本笔记对它给出一个无条件算术机制：formal lag
group具有自然的 parity character；continuum 单节点与奇数次 prime powers位于
odd sector，只有 zero lag和偶数次 prime powers破坏对称性。纯 odd symbol的所有
奇数 exact moments严格为零。

对 parity breakers作 convolution telescoping，再用 `ell^2` Cauchy--Schwarz，
得到接近有限实际值的 exact-response upper bound。进一步只保留 coefficient
`L1/L2` norms，可证明 Abel scale上 degree-two exact bucket为 `o(1)`。因此 exact
products不是 NCE-8 的剩余 RH 障碍；困难被严格压到 signed near products与高
degree soft approximation。

## 1. Formal parity character

沿文档 188，formal lag group为

`G=Q_(>0)^times direct-sum Z^m`.                 (1)

对 reduced rational `r=a/b` 定义 `Omega(r)=Omega(a)+Omega(b)`，其中 `Omega`
计 prime factors with multiplicity。定义 character

`chi(r,k)=(-1)^[Omega(r)+sum_jk_j]`.             (2)

它确为 group homomorphism `G->{+-1}`。formal zero的 character为 `+1`。

将 Hermitian coefficient map写成

`d=o+e`,                                        (3)

其中 `o` 支撑在 `chi=-1`，`e` 支撑在 `chi=+1`。称 `e` 为 parity breaker。

对 prime--continuum symbol：

- `log(p^k)` 的 character为 `(-1)^k`；
- 每个 nonzero continuum quadrature basis lag的 character为 `-1`；
- zero lag的 character为 `+1`。

所以 `e` 精确由 even prime powers、zero-lag compressed continuum mass，以及任何
其它显式 zero/even correction组成。

### 定理 AGH（odd-sector exact-moment vanishing）[U]

对每个 `r>=0`，

`(o^(*(2r+1)))(0)=0`.                            (4)

#### 证明

`2r+1` 个 `chi=-1` support elements之和的 character仍为 `-1`，不可能等于
character为 `+1` 的 formal zero。故 identity coefficient为空。`square`

这个 vanishing 是 exact product combinatorics，不是数值 cancellation，也不使用
zeta zeros。

## 2. Breaker perturbation bounds

记 convolution power为 `d^(*k)`，identity coefficient为

`E_k(d)=(d^(*k))(0)`.                            (5)

令

`B=||d||_1`, `S=||d||_2`, `R=||e||_2`.          (6)

### 定理 AGI（telescoping convolution-L2 odd bound）[U]

对 odd `k>=1`，

`|E_k(d)|`

` <=sum_(j=0)^(k-1)||d^(*j)||_2`

`       *||e*o^(*(k-1-j))||_2`,                 (7)

并有较粗但 scale-explicit 的

`|E_k(d)|<=k R S B^(k-2)`                       (8)

（`k=1` 按直接式解释）。此外

`E_4(d)=||d*d||_2^2<=B^2S^2`.                   (9)

#### 证明

commutative telescoping identity给

`d^(*k)-o^(*k)`

` =sum_(j=0)^(k-1)d^(*j)*e*o^(*(k-1-j))`.       (10)

定理 AGH使左侧 identity coefficient等于 `E_k(d)`。对每项的 zero coefficient
应用 `ell^2` Cauchy--Schwarz得到式 (7)。式 (8)中，把 breaker保留为 `ell^2`
factor，把其余 `k-1` factors中的一个保留为 `S`，其余用 convolution Young
inequality的 `L1` bound `B`。式 (9)来自 Hermitian symmetry：
`E_4=<d*d,d*d>_(ell2)`，再用 Young。`square`

式 (7)可完全由 finite arithmetic convolutions计算；式 (8)较松，但适合做共尾
scale analysis。

## 3. Degree-two exact-response bound

沿文档 188，令 `a=sqrt(3)/2`，degree-two interpolant为

`p_2(x)=c x(x-aB)`,                              (11)

其中 `c=2A/(3B^2)` 且 `0<=A<=1`。exact response为

`R_exact=c^2[2aB E_4-E_5-a^2B^2E_3]`.          (12)

### 推论 AGJ（norm-controlled exact bucket）[U]

有

`R_exact`

` <=c^2[2aB E_4+|E_5|+a^2B^2|E_3|]`           (13)

并因此

`R_exact <=(8a/9) S^2/B +(29/9) RS/B`.          (14)

更精细地，可把式 (13)中的 `|E_3|,|E_5|` 分别替换为式 (7)的 finite
convolution bounds。

#### 证明

式 (13)取 odd terms绝对值。由式 (8)--(9)，

`E_4<=B^2S^2`, `|E_3|<=3RSB`,

`|E_5|<=5RSB^3`.                                (15)

再用 `c^2<=4/(9B^4)` 与 `a^2=3/4`，整理得到式 (14)。`square`

这个 bound 的关键不是 breaker `L1` fraction本身，而是 `R=||e||_2`；稀疏的
even prime-power defects在 `L2` 中远比所有 product representations取绝对值小。

## 4. Abel prime--continuum asymptotics

考虑 `1/2<=sigma<=3/4` 的 Abel coefficient scale `Y`。忽略已单列的 finite
Gamma corrections，prime atoms为

`Lambda(p^k)p^(-ksigma)e^(-p^k/Y)`.             (16)

continuum background的 total variation为

`C_Y=int_1^infinity x^(-sigma)e^(-x/Y)dx`

`   asymp Y^(1-sigma)`.                          (17)

### 定理 AGK（degree-two exact sector evacuation）[U]

对保留 prime atoms与 continuum background provenance 的 cofinal quadratures，
在 quadrature/tail errors另行入账时，

`B_Y>>Y^(1-sigma)`,                              (18)

`S_Y^2<<log^3(2Y)+o_mesh(1)`,                   (19)

`R_Y=O(1)+O(zero-lag continuum mass)`.           (20)

因此当 zero-lag compressed mass一致有界时，

`R_(exact,Y)`

` <<[log^3(2Y)+log^(3/2)(2Y)]/Y^(1-sigma)`

` =o(1)`                                        (21)

uniformly for `1/2<=sigma<=3/4`。

#### 证明

式 (17)在 `x in [Y,2Y]` 上给式 (18)。prime coefficient square sum以
`Lambda(n)<=log n` 粗界为

`sum_(n>=2)(log n)^2n^(-2sigma)e^(-2n/Y)`

` <=sum_(n>=2)(log n)^2n^(-1)e^(-2n/Y)`

` <<log^3(2Y)`.                                  (22)

continuum midpoint masses的 square sum在 mesh refinement下趋零；固定 finite
corrections另计，得到式 (19)。breaker prime square mass只含 `p^(2j)`：

`sum_(p,j>=1)(log p)^2p^(-4jsigma)`

` <=sum_(p,j>=1)(log p)^2p^(-2j)<infinity`.      (23)

加 zero-lag mass给式 (20)。最后代入推论 AGJ。`square`

该 theorem只处理 formal exact bucket。continuum quadrature的 uniform functional
error、prime cutoff tail与 Gamma residual仍须沿文档 141/149/187 的 ledger加入。

## 5. Finite bound audit

在文档 188 的小尺度表上，breaker `L1` fraction约为 `.058--.084`。三种上界的
表现为：

| `Y,N` | actual exact | pure `L1` upper / actual | convolution-`L2` upper / actual | norm upper / actual |
|---:|---:|---:|---:|---:|
| `4,7` | .02722 | 8.46 | 1.32 | 5.29 |
| `8,10` | .03132 | 15.21 | 1.46 | 6.67 |
| `12,12` | .03067 | 19.18 | 1.51 | 7.66 |
| `16,15` | .02876 | 22.89 | 1.54 | 8.55 |

pure `L1` bound快速恶化；式 (7) 的 convolution-`L2` bound始终只松约
`1.3--1.5` 倍，验证了 parity mechanism确实读取实际 exact combinatorics。
式 (14) 的 norm bound在小尺度较松，但它给出定理 AGK 的共尾衰减率。

这些仍是 finite floating diagnostics；定理 AGH--AGK 本身是解析/代数推导，不依赖
该表。

## 6. Consequence for the research map

degree-two soft direction现在有如下严格分工：

- **exact products**：由 parity breaker + convolution `L2` 无条件控制，并在
  Abel cofinal scale趋零；
- **far products**：由文档 188 的 exponential variation bound控制，前提是
  Chebyshev coefficient `L1` growth与 threshold协调；
- **near products**：仍保留 signed prime--continuum correlations，是当前唯一
  未解决的 arithmetic core；
- **soft approximation**：degree two本身没有足够小的 uniform error，高 degree
  仍需稳定 recurrence与误差预算。

所以本结果没有证明 RH，但它排除了 exact multiplicative coincidences作为
canonical degree-two路线的障碍。这比把全部 high moments交给 universal
occupancy bound更精确。

## 7. 下一步

下一最小引理应直接针对 near bucket，而不是继续改进 exact bounds：

1. 把 `0<|log(a/b)+continuum shift|<=h` 写成 balanced short multiplicative
   intervals；
2. 保留 degree-two coefficient combination的 signs，寻找 Volterra
   summation-by-parts或 Möbius shell pairing；
3. 比较所得 signed near norm与文档 169 的 full Selberg profile，审计是否仍等价
   于 RH；
4. 同时研究更高 even Chebyshev degrees是否继承 parity odd-moment suppression。

## 8. 审计结论

product/continuum parity character给出了数域 Hodge candidate中的一个真实结构：
bulk odd exact cycles由 character grading精确消去，只有 even-prime-power与 zero
lag boundary defects留下。通过 convolution `L2` 而非绝对 multiplicity计数，
degree-two exact soft response获得无条件共尾消失。剩余问题已严格局部化为 signed
near-product transport与 polynomial approximation，而不是 exact Euler products。

