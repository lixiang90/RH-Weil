# 单列径向 finite Taylor residue 与 RH

文档 065 把 RH 等价为 prime-built analytic kernel 在整个 unit disk 的
positive RKHS completion。本笔记把这个二维解析 completion 再压缩成一条
显式有限序列：Taylor degree `R` 与 radial point `r_R=1-1/R` 同时趋向边界。
该序列有界当且仅当 RH，并可无条件截断为 `n<=exp(O(R))` 的有限素数 Gram。

## 1. Taylor Gram 的 binomial moment 分解

令

`E_R(x)=sum_(j=0)^R x^j/j!`,                      (1)

并沿用 normalized Gamma moments `N_q`。对 `0<=r<1` 定义 width-trace
Taylor Gram

`K_R(r)=2sigma_0 int_0^infinity int_(h_0)^(h_1)`

` |E_R(sigma_0rt)b_h(t)|^2dh e^(-2sigma_0t)dt`.   (2)

### 命题 LM（binomial moment decomposition）

有精确恒等式

`K_R(r)=sum_(q=0)^(2R)omega_(q,R)(r)N_q`,         (3)

其中

`omega_(q,R)(r)=r^q 2^(-q)`

` *sum_(max(0,q-R)<=j<=min(R,q))binom(q,j)`.       (4)

所以 `0<=omega_(q,R)(r)<=r^q`。特别地，

`omega_(2R,R)(r)=r^(2R)4^(-R)binom(2R,R)`

`                  =r^(2R)/sqrt(pi R)*(1+o(1))`.  (5)

#### 证明

展开 `E_R(x)^2`，按 `q=j+l` 合并，并使用

`1/(j!l!)=binom(q,j)/q!`。

另一方面，文档 064 的定义给

`N_q=(2sigma_0)^q M_q/q!`。                       (6)

把 `x=sigma_0rt` 代入即得式 (3)–(4)。式 (5) 是 central binomial
coefficient 的 Stirling asymptotic。`□`

等价地，`omega/r^q` 是 `Binomial(q,1/2)` 落在 Taylor square 允许的 index
range 内的 probability。这解释了所有 coefficients 的 positivity。

## 2. 偶数矩不丢失 Laplace 边界

### 引理 LN（even moments have the full root exponent）

设 positive Laplace moment sequence 的 normalized root rate 为 `B`。则

`limsup_(R->infinity)N_(2R)^(1/(2R))=B`.          (7)

对 zeta，

`B=sigma_0/[sigma_0-max(0,Theta-1/2)]`.           (8)

#### 证明

令 `F(z)=sum_(q>=0)N_qz^q`。文档 064 命题 LD 与 positivity 给它的精确
radius `B^(-1)`，实正边界点是 singularity。even part

`F_even(z)=[F(z)+F(-z)]/2=sum_(R>=0)N_(2R)z^(2R)` (9)

在正边界处仍奇异，因为 `F(-z)` 在其邻域属于更深的 Laplace
convergence half-plane，不能消去 `F(z)` 的正边界奇点。因此 even series 的
radius 仍为 `B^(-1)`；Cauchy--Hadamard 给式 (7)，式 (8) 用定理 KS。`□`

所以用 squared Taylor polynomial 只看到偶数最高矩，并不会遗漏 off-center
divisor exponent。

## 3. 一条径向序列判定 RH

对 `R>=2` 令

`r_R=1-1/R`,

`H_R=(1-r_R)K_R(r_R)=K_R(r_R)/R`.                (10)

### 定理 LO（single radial finite-Taylor RH criterion）

以下条件等价：

1. RH；
2. `sup_(R>=2)H_R<infinity`；
3. `H_R=e^(o(R))`。

更精确地，对 `a=max(0,Theta-1/2)` 恒有

`limsup_(R->infinity)H_R^(1/(2R))`

`                          =sigma_0/(sigma_0-a)`.  (11)

#### 证明

因 `E_R(x)<=e^x` 对 `x>=0`，文档 065 的完整 analytic kernel 给

`H_R<=(1-r_R)K(r_R)`

`              =mathfrak G_(sigma_0(1-r_R))`.     (12)

RH 下定理 KN/LI 说明右端趋于 finite critical covariance trace，故 1 推 2，
而 2 显然推 3。

反之，式 (3) 全部项非负，所以

`H_R>=(1-r_R)omega_(2R,R)(r_R)N_(2R)`.           (13)

式 (5) 中 `r_R^(2R)->e^(-2)`；`1-r_R=1/R` 与 polynomial factors 的
`2R` 次根都趋于 `1`。引理 LN 给式 (11) 的 lower inequality。

反向由式 (3)–(4) 的 `omega_(q,R)<=1` 得

`H_R<=R^(-1)sum_(q<=2R)N_q`。

又因 `limsup N_q^(1/q)=sigma_0/(sigma_0-a)`，对每个 `epsilon>0`，右端至多
`e^(o(R))[sigma_0/(sigma_0-a)+epsilon]^(2R)`。令 `epsilon downarrow0` 即得
式 (11) 的 upper inequality。若 `a>0`，式 (11) 严格大于 `1`，与条件 3
矛盾；故 3 推 RH。`□`

定理 LO 把“每个 disk compact 上的所有 Taylor sections”缩成同一个
degree/boundary schedule 上的一列正数，没有 diagonal extraction 的自由度。

## 4. 真正有限的 prime cutoff

固定 `D>0`，定义

`H_R^[D]=(1-r_R)2sigma_0 int_0^(DR)int_(h_0)^(h_1)`

` |E_R(sigma_0r_Rt)b_h(t)|^2dh e^(-2sigma_0t)dt`. (14)

### 定理 LP（exponentially accurate finite-prime Taylor residue）

若

`D>2/(2sigma_0-1)` 且

`kappa_D=(2sigma_0-1)D-2-2log(sigma_0D)>0`,       (15)

则

`0<=H_R-H_R^[D]<=e^(-kappa_D R+o(R))`.            (16)

并且 `H_R^[D]` 只使用

`n<=exp(DR+h_1)`                                  (17)

的有限 Euler coefficients。因而 RH 也等价于

`sup_R H_R^[D]<infinity`，                         (18)

或等价于 `H_R^[D]=e^(o(R))`。

#### 证明

在 `t>=DR` 且 `D>2/(2sigma_0-1)` 时，取 `D` 更大若有必要可保证
`sigma_0r_Rt>=R`。于是 Taylor terms 随 degree 增长，且

`E_R(sigma_0r_Rt)<=(R+1)(sigma_0r_Rt)^R/R!`.      (19)

用 zeta 的 absolute bound
`int_(h_0)^(h_1)|b_h(t)|^2dh<<poly(t)e^t`，tail 至多为

`e^(o(R)) int_(DR)^infinity`

` (sigma_0t)^(2R)/(R!)^2 e^(-(2sigma_0-1)t)dt`.   (20)

integrand 从 cutoff 起递减；Stirling 在 `t=DR` 给每 `R` 的 log rate

`2+2log(sigma_0D)-(2sigma_0-1)D=-kappa_D`，

故式 (16)。当 `t<=DR`、`h<=h_1` 时，annulus 只含式 (17) 的整数，故
`H_R^[D]` 是真正 finite prime Gram。指数小于 `1` 的 positive tail 不改变
定理 LO 的 bounded/subexponential dichotomy，给式 (18)。`□`

条件 (15) 对 sufficiently large `D` 总成立。

## 5. 有限矩阵的显式形态

### 命题 LQ（finite radial Hodge matrix）

对 cutoff (14)，令有限 index set

`S_R={n:n<=e^(DR+h_1)}`。                         (21)

存在显式 positive semidefinite matrix `A_R`，其 entries 为

`A_R(m,n)=(1-r_R)2sigma_0 int_0^(DR)`

` int_(h_0)^(h_1)1_(|logm-t|<=h)1_(|logn-t|<=h)`

` *|E_R(sigma_0r_Rt)|^2dh e^(-2sigma_0t)dt`,      (22)

使

`H_R^[D]=sum_(m,n in S_R)`

`       [a_m/sqrtm]A_R(m,n)[a_n/sqrtn]`.          (23)

`A_R` 只由 elementary exponentials、polynomials 与 interval endpoints
组成，不含零点。它也是 functions

`1_(|logn-t|<=h)E_R(sigma_0r_Rt)`                 (24)

在 positive measure
`(1-r_R)2sigma_0e^(-2sigma_0t)dtdh` 中的 Gram。

#### 证明

把 finite signal `b_h(t)=sum_(n in S_R)a_n/sqrtn`
`1_(|logn-t|<=h)` 代入式 (14)，展开平方给式 (22)–(23)；式 (24) 给
positivity。`□`

所以 RH 被压成 actual arithmetic vector `a_n/sqrtn` 在一列完全显式有限
Hodge matrices `A_R` 中的统一 Rayleigh bound。

## 6. Gamma--Euler 径向结构定理

### 定理 LR（general radial finite-Taylor centerline theorem）

考虑定理 LL 的 paired Gamma--Euler data，并假设 absolute current growth

`|b_h(t)|<=e^((omega+o(1))t)`.                    (25)

取 `sigma_0>max(omega,sigma_c)`，其中
`sigma_c=max(0,Theta-c/2)`。若 `D` 足够大使

`2(sigma_0-omega)D-2-2log(sigma_0D)>0`,           (26)

则相应 finite radial residues 满足

`sup_R H_R^[D]<infinity`                          (27)

当且仅当全部 divisor 位于 `Re rho=c/2`。若中心线失败，

`limsup(H_R^[D])^(1/(2R))`

`              =sigma_0/(sigma_0-sigma_c)`.       (28)

#### 证明

定理 KV 给 normalized moments 的 root，Lemma LN 对一般 positive Laplace
trace 同样成立；定理 LO 的最高偶矩论证逐字适用。tail proof 中把
`2sigma_0-1` 换成 `2(sigma_0-omega)`，给式 (26) 与 finite approximation。
`□`

## 7. 存在性进展与剩余缺口

对 zeta，目前所需结构已具体到单列 finite matrices `A_R`：

- matrix entries、positivity、finite support 全部无条件存在；
- cutoff error 有严格 exponential rate；
- off-center divisor 必使 actual arithmetic Rayleigh values 指数爆炸；
- RH 等价于这些 values uniformly bounded，甚至只要求 subexponential。

尚未证明的是式 (23) 对 zeta coefficients `a_n=Lambda(n)-1` 的统一 bound。
generic coefficient vectors 不满足该 bound；可行证明必须利用 prime/pole
centering 与 endpoint cancellation，而不能只用 `A_R` 的 operator norm。
