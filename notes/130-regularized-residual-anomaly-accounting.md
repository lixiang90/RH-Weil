# Higher regularized residuals 与 anomaly accounting

文档 129 证明 finite positive primitive completion不能同时非平凡且 ordinary-
determinant neutral。无限维 higher regularized determinant 是一个可能的逃逸口；
文档 079 已证明 zeta prime operator 在临界线属于 `S_3` 而不属于 `S_2`。
本节把两条线接起来。

核心结论是：canonical regularization 本身仍不提供免费 purity。Exact acyclic
spectral pairing在 `det_m` 下继续完全抵消；未配对 positive residual 的 regularized
log determinant具有固定 sign，等于 1 仍迫使 residual 为零。真正可能留下的
anomaly 只能来自被减去的低阶 traces、非乘法 regularization 或边界/全局 trace
renormalization，并且必须逐项匹配原 zeta 数据。

## 1. Canonical higher determinant

对 `K in S_m`，定义

`det_m(I+K)`

` =det[(I+K)exp(sum_(j=1)^(m-1)(-1)^jK^j/j)]`.   (1)

有限秩时

`log det_m(I+K)`

` =Tr[log(I+K)+sum_(j=1)^(m-1)(-1)^jK^j/j].      (2)

右侧 scalar Taylor remainder从 `K^m` 开始，因此对 `S_m` operator有定义。

### 定理 XM（regularized acyclic pairing still cancels）

若 `K_+,K_- in S_m` 具有相同 nonzero eigenvalues（含 algebraic multiplicity），
则

`det_m(I+K_+)/det_m(I+K_-)=1`.                    (3)

特别地，把 finite acyclic completion换成 canonical `det_m` 不会产生 anomaly。

#### 证明

有限秩时式 (2) 是 eigenvalues 的同一 symmetric sum，所以两侧相等。一般
`S_m` 情形用 finite-rank spectral truncations；canonical regularized determinant
对 `S_m` norm连续，取极限得到式 (3)。`□`

## 2. Positive regularized rigidity

对 scalar `lambda>=0` 定义

`r_m(lambda)=log(1+lambda)`

` +sum_(j=1)^(m-1)(-1)^jlambda^j/j`.              (4)

直接求导得

`r_m'(lambda)=(-1)^(m-1)lambda^(m-1)/(1+lambda)`. (5)

### 定理 XN（det_m-positive residual rigidity）

若 `K>=0`, `K in S_m`，则

`(-1)^(m-1)log det_m(I+K)`

` =sum_i int_0^(lambda_i)t^(m-1)/(1+t)dt>=0`,     (6)

其中 `lambda_i` 是 `K` 的 eigenvalues。等号当且仅当 `K=0`。因此

`det_m(I+K)=1 iff K=0`.                           (7)

#### 证明

式 (5) 从 `r_m(0)=0` 积分得到每个 eigenvalue contribution。`K in S_m` 保证
小 eigenvalues 的 `O(lambda_i^m)` remainders可和；有限多个大 eigenvalues无碍。
每个积分非负且只在 `lambda_i=0` 时为零，求和即得式 (6)--(7)。`□`

所以文档 129 的 determinant-one rigidity不仅没有因 higher regularization消失，
反而有一个 exact signed integral proof。对 positive contraction `T` 的
`det_m(I-T)` 同样有固定负 remainder `-sum_(k>=m)Tr(T^k)/k`。

## 3. Zeta 临界线的最小正则化阶

令 prime-orbit operator

`T(s)e_p=p^(-s)e_p`.                              (8)

文档 079 定理 OP 已给

`T(s) in S_m iff m Re(s)>1`.                      (9)

### 定理 XO（critical det_3 and its missing traces）

在 `Re(s)=1/2`，最小可用整数 canonical determinant恰为 `m=3`。其 finite-prime
identity为

`det_(3,X)(I-T(s))`

` *exp[-P_X(s)-P_X(2s)/2]`

` =product_(p<=X)(1-p^(-s)),`                     (10)

其中 `P_X(z)=sum_(p<=X)p^(-z)`。当 cutoff趋于无穷，`det_3` 的 logarithm从
prime powers `k>=3` 开始并在中心线局部绝对收敛；被删除的 `k=1,2` traces正是
恢复 Euler determinant所必需的 counterterms。

#### 证明

式 (9) 在 `Re(s)=1/2` 给 `m>2`，故最小整数为 3。对每个有限 prime set，

`log det_3(I-T)`

` =sum_p[log(1-p^(-s))+p^(-s)+p^(-2s)/2]`.       (11)

移项并 exponentiate 得式 (10)。`k>=3` 部分由
`sum_p p^(-3/2)` 控制。`□`

`det_3` 本身在 `Re(s)>1/3` 是 zero-free canonical local object；global zeta zeros
不在其中，而必须由低阶 counterterms的 singular/global continuation进入。

## 4. Regularization-anomaly accountability theorem

### 定理 XP（same-zeta regularized completion dichotomy）

设一个 infinite-dimensional completion使用 canonical `det_m`：

1. exact even/odd `S_m` pairing仍由定理 XM完全抵消；
2. unpaired positive primitive residual由定理 XN产生非平凡 fixed-sign factor；
3. 若最终 determinant仍要等于原 zeta factor，则该 residual必须由显式 low-trace
   counterterm、multiplicative anomaly或已有 boundary/Euler/gamma factor补偿。

所以“使用 regularized determinant”不是结构存在性证明。必须额外构造并验证
anomaly，使其：

- 不预先使用待证 zeta zeros；
- 与原 Euler/Tate/archimedean explicit formula逐项匹配；
- 在 test-function variations下保留所需 polarized positivity；
- cutoff极限可控而非仅形式相消。

在 zeta prime carrier 的临界线上，最小 anomaly data至少包含式 (10) 的
`P_X(s)+P_X(2s)/2`。若用

`P(s)=sum_(r>=1)mu(r)log zeta(rs)/r`               (12)

定义其 continuation，就已经把 global zeta divisor放回构造，不能作为无循环 RH
证明。

#### 证明

前两项分别是定理 XM、XN。若 unpaired residual非零而 final determinant不变，
乘法恒等式迫使另一个 factor为其 inverse；canonical definition中唯一未包含的数据
是低阶 trace subtraction/其它 anomaly，故必须显式给出第三项。zeta specialization
由定理 XO；式 (12) 是 Euler logarithm的 Möbius inversion，因显式依赖 zeta而有
所述循环边界。`□`

这把文档 129 所列“infinite regularization”出口从一个名词变成可审计 deliverable：
需要构造的正是低阶 global trace geometry。

## 5. Finite critical-line audit

取 `s=1/2`。`S_2` 是 Hilbert--Schmidt partial sum `sum_p1/p`，`S_3` 是
`sum_pp^(-3/2)`；`P_1,P_2/2` 是两个 missing traces。

| prime cutoff | primes | `S_2` | `S_3` | `P_1` | `P_2/2` | `|det_3|` | counterterm magnitude |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 100 | 25 | 1.803 | 0.8177 | 5.54 | 0.901 | 0.6001 | `1.60e-3` |
| 1,000 | 168 | 2.198 | 0.8422 | 12.65 | 1.099 | 0.5949 | `1.06e-6` |
| 10,000 | 1,229 | 2.483 | 0.8477 | 29.14 | 1.242 | 0.5938 | `6.37e-14` |
| 100,000 | 9,592 | 2.705 | 0.8491 | 70.05 | 1.353 | 0.5935 | `9.77e-32` |

`S_3` 与 `det_3` 快速稳定，而 low traces继续增长，counterterm趋于零；有限 Euler
inverse正由二者的 singular compensation重建。这正是需要全局 geometry解释的
anomaly，而不是数值误差。

## 6. 计算实现

新增：

- `regularized_positive_residual_certificate`：对任意 finite PSD kernel计算
  `det_m(I+K)`、低阶 trace counterterms、scalar/integral remainders与 fixed-sign
  rigidity；
- `prime_critical_regularization_certificate`：在 `Re(s)=1/2` 计算 finite `det_3`、
  两个 missing traces、`S_2/S_3` sums、counterterm与 Euler reconstruction。

回归核对 remainder integral identity、positive rigidity、exact pairing ratio及
critical-line finite Euler identity，tolerance 为 `1e-49`。
