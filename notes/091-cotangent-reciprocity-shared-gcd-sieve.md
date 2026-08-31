# Cotangent reciprocity、shared-GCD 二残基筛与 additive modes

文档 090 把 primitive harmonic kernel 写成 finite Möbius--cotangent sieve。
本节进一步对 reduced determinant kernel 作 reciprocity：当 denominators 互素
时，所有 modulus-sized cotangent terms 精确相消，kernel 一致有界。shared
gcd 只引入一个“每个素数排除两个 residues”的周期筛；其 principal mode
显式可控，非主 additive modes 才是需要与 outer Möbius sums 配合的部分。

## 1. Inverse reciprocity identity

设 `(a,b)=1`、`a,b>1`，令

`bar a in {1,...,b-1}`,  `a bar a=1 (mod b)`,

`bar b in {1,...,a-1}`,  `b bar b=1 (mod a)`.         (1)

则 elementary inverse reciprocity 为

`bar a/b+bar b/a=1+1/(ab)`.                          (2)

考虑 reduced equation

`b h-a h'=delta`,  `(delta,ab)=1`.                   (3)

文档 090 定理 RL 的 particular residues 可取

`h=delta bar b (mod a)`,

`h'=-delta bar a (mod b)`.                           (4)

### 定理 RS（cotangent reciprocity and uniform kernel bound）

unrestricted solution-line correlation 满足

`U_(a,b)(delta)`

` =(-1)^(delta+1) pi/delta`

`   *sin(pi delta/(ab))`

`    /[sin(pi delta bar a/b)sin(pi delta bar b/a)]`. (5)

并且对所有允许的 nonzero `delta`，

`|U_(a,b)(delta)|<=pi^2/4`.                           (6)

特别地，`delta=1` 与 `delta=-1` 给同一个正 kernel。

#### 证明

定理 RL 给

`U=-pi/delta[cot(pi delta bar a/b)`

`                    +cot(pi delta bar b/a)]`.        (7)

用 `cot x+cot y=sin(x+y)/(sin x sin y)` 和式 (2)，

`sin(pi delta[bar a/b+bar b/a])`

` =(-1)^delta sin(pi delta/(ab))`,                    (8)

得到式 (5)。因 `(delta,b)=1`，第一个 denominator sine 至少为
`sin(pi/b)>=2/b`；另一个至少为 `2/a`。若 `|delta|<=ab`，numerator 至多
`pi|delta|/(ab)`，给式 (6)；若 `|delta|>ab`，直接用 numerator `<=1`
得到更小的 `pi ab/(4|delta|)`。变量 `(h,h')->(-h,-h')` 证明 `+/-1`
correlations 相等，式 (5) 又显示其为正。`□`

这是一次真正的 reciprocity cancellation：式 (7) 中两个 cotangents 各自可随
modulus 增长，但它们的和一致有界。对它们分别取绝对值会人为制造不存在的
conductor loss。

## 2. Shared gcd 上的 primitive conditions

回到

`r=ga`,  `r'=gb`,                                    (9)

并假设 `g,a,b` pairwise coprime squarefree。由 `(delta,ab)=1`，式 (3) 的
所有 solutions 自动满足 `(h,a)=(h',b)=1`。取一个 particular solution，写

`h_t=h_0+at`,  `h'_t=h'_0+bt`.                       (10)

剩余 primitive conditions 仅为

`(h_t,g)=(h'_t,g)=1`.                                (11)

### 定理 RT（two-forbidden-residue sieve）

对每个 prime `p|g`，式 (11) 在 `t mod p` 中恰排除两个不同 residues。因此

1. 若 `2|g`，没有 primitive solutions；
2. 若 `g` 为 odd squarefree，allowed residue set `T_g subset Z/gZ` 的大小为

   `|T_g|=product_(p|g)(p-2)`.                        (12)

#### 证明

因 `p` 不整除 `a,b`，两个 linear functions `h_t,h'_t` 各有唯一 zero
residue。若两 residues 相同，则该 `t` 使 equation (3) 左侧被 `p` 整除，
从而 `p|delta`；但 nonzero amplitudes 的 squarefree factorization 与 primitive
condition 排除这一点。所以 residues 不同。Chinese remainder theorem 给
式 (12)；`p=2` 时两个 residues 已覆盖全部 classes。`□`

这给出一个新的 exact vanishing：所有 shared gcd 为偶数的 determinant
strata 在 primitive Farey spectrum 中根本不存在。

## 3. Finite cotangent formula for the shared sieve

对每个 `tau in T_g`，把 `t=tau+gk` 代入式 (10)。

### 定理 RU（shared-GCD primitive cotangent formula）

`H_(ga,gb)(gdelta)`

` =pi/(gdelta)sum_(tau in T_g)`

`  [cot(pi(h'_0+b tau)/(bg))`

`   -cot(pi(h_0+a tau)/(ag))]`.                       (13)

#### 证明

在 progression `t=tau+gk` 上，仍有

`1/(h_th'_t)=(b/h'_t-a/h_t)/delta`.                  (14)

而

`b/(h'_0+b tau+bgk)`

` =(1/g)/(k+(h'_0+b tau)/(bg))`,                     (15)

`a/h_t` 同理。对 `k` 使用 cotangent principal-value identity，再对 allowed
residues 求和即得。`□`

所以文档 090 的 divisor inclusion--exclusion 可以在 squarefree support 上
改写成更小的 exact residue sieve；它还自动显现 even-`g` vanishing。

## 4. Principal density 与 nonprincipal additive modes

令

`w_g(t)=1_(t mod g in T_g)`.                          (16)

作 normalized finite Fourier expansion

`w_g(t)=sum_(nu mod g) hat w_g(nu)e^(2pi i nu t/g)`, (17)

`hat w_g(nu)=(1/g)sum_(t mod g)w_g(t)e^(-2pi i nu t/g)`.

### 定理 RV（local sieve Fourier decomposition）

zero mode 为

`hat w_g(0)=product_(p|g)(1-2/p)`.                    (18)

在 prime modulus `p|g` 上，若两个 forbidden residues 是 `tau_1,tau_2`，则

`hat w_p(nu)=-(e^(-2pi i nu tau_1/p)`

`                 +e^(-2pi i nu tau_2/p))/p`         (19)

对 `nu!=0`，故 `|hat w_p(nu)|<=2/p`。squarefree `g` 的 coefficients 由
Chinese remainder theorem 乘法分解。

因此 primitive correlation 精确分成

`H_(ga,gb)(gdelta)`

` =hat w_g(0) U_(a,b)(delta)`

`   +sum_(nu!=0)hat w_g(nu)U_(a,b;delta,nu)`,         (20)

其中

`U_(a,b;delta,nu)=sum_(t in Z)`

` e^(2pi i nu t/g)/(h_t h'_t)`                       (21)

是 twisted solution-line kernel。

#### 证明

式 (18) 来自定理 RT。prime modulus 上，全 residue exponential sum 对
`nu!=0` 为零；删去两个 forbidden terms 给式 (19)。CRT 给乘法分解。把
式 (17) 插入 restricted solution-line sum，交换有限 Fourier sum 与
absolutely paired principal-value sum，得到式 (20)。`□`

principal term 由定理 RS 一致有界。所有 shared-gcd 新困难都进入带小 local
Fourier coefficients 的 nonprincipal additive twists；这正是 Kloosterman/
dispersion methods 所需的标准入口。

## 5. Shortest determinant strata

### 定理 RW（structure of `delta=+/-1`）

对 coprime conductors `g=1`，

`H_(a,b)(+/-1)=U_(a,b)(1)`

` =pi sin(pi/(ab))`

`   /[sin(pi bar a/b)sin(pi bar b/a)]`,               (22)

且 `0<H<=pi^2/4`。因此 shortest determinant kernel 本身没有 sign
cancellation；其求和必须依赖 outer amplitudes

`S_N(a)conjugate(S_N(b))`.                            (23)

对 odd shared `g`，principal sieve mode 仍是 positive bounded kernel 乘以
`product_(p|g)(1-2/p)`；可能的额外振荡只来自式 (20) 的 nonprincipal
additive modes。

#### 证明

`g=1` 时 primitive conditions 已由 `(delta,ab)=1` 自动满足，使用定理 RS。
一般 odd `g` 使用定理 RV。`□`

所以不能期待 cotangent reciprocity 单独证明 RH：它消除了虚假的 modulus
growth，却同时表明 `delta=+/-1` principal kernel 是正的。真正所需的负相关
必须来自 Möbius Type-I/II amplitudes 或 nonprincipal additive twists。

## 6. Refined bilinear certificate

### 定理 RX（principal/nonprincipal collision criterion）

在文档 090 的剩余窗口 `N<=Y<=N^(3/2)` 中，把每个 shared-gcd stratum 按
式 (20) 分解。若

1. outer Möbius amplitudes 对 bounded principal kernels 的 dyadic bilinear
   sum 为 `O(1/log N)`；
2. nonprincipal twisted kernels 的总和为 `O(1/log N)`；

并且此前 local/periodic conditions 成立，则 RH 成立。

#### 证明

定理 RS 控制 principal kernel，定理 RV 给 exact split；两项假设控制文档
090 式 (18)。再用定理 RQ。`□`

这把一个 cotangent bilinear estimate 分成两个性质不同的任务：principal
部分是纯 Möbius bilinear cancellation，nonprincipal 部分是带 additive
characters 的 dispersion/Kloosterman cancellation。

## 7. 存在性审计

### 结论 RY（reciprocity removes kernel growth, not Möbius difficulty）

当前已无条件证明：

- coprime reduced harmonic kernels 对所有 determinant strata 一致有界；
- shared even gcd strata 精确消失；
- odd shared gcd 只产生显式 two-residue sieve；
- 该筛的 principal density 和全部 additive Fourier modes 均有限显式。

剩余开放输入因而不再包含 cotangent singularity 或 harmonic summation问题。
它是两个标准但仍很强的平均估计：bounded modular-inverse weights 下的 outer
Möbius bilinear sum，以及小 sieve Fourier coefficients 加权的 twisted sum。

## 8. 计算实现

`scripts/qw_matrix.py` 新增：

- `coprime_farey_harmonic_reciprocity`；
- `squarefree_shared_gcd_allowed_residues`；
- `squarefree_shared_gcd_primitive_correlation`。

测试核对 reciprocity closed form 与 solution-line cotangent formula、统一
`pi^2/4` 界、even-`g` vanishing、`product(p-2)` residue count，并把 shared
`g=5` 的 finite cotangent formula 与六万个 restricted direct terms 比较。
