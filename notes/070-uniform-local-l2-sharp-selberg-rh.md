# Uniform local `L^2`、sharp Selberg blocks 与 RH

文档 042 证明 dyadic Selberg mean square 的 `X^(2+epsilon)` bound 等价于
RH；文档 067–069 则给 anchored Cesàro/line-graph 条件。本笔记补上此前缺失
的 local uniformity：RH 下零点 coefficients 与 unit-window zero count 足以
证明 normalized Chebyshev current 的 uniform Stepanov `L^2` bound。

结果是 epsilon-free 的 sharp block criterion

`int_X^(2X)|psi(x)-x|^2dx=O(X^2)`,                (1)

以及 fixed annular log blocks 的 uniform mean-square criterion。

## 1. 指数级数的 uniform local lemma

设 real frequencies `lambda_j` 与 coefficients `a_j`。对 integer `k` 定义
unit-bin mass

`A_k=sum_(lambda_j in [k,k+1))|a_j|`.             (2)

### 引理 MJ（unit-bin `l^1` decay implies Stepanov `L^2`）

若

`A_k<=C log(2+|k|)^B/(1+|k|)`                    (3)

对某个 fixed `B>=0` 成立，则 exponential series

`F(t)=sum_j a_j e^(ilambda_jt)`                   (4)

在 symmetric finite partial sums 下收敛于 `L^2_loc`，并对每个 fixed
`L>0` 满足

`sup_(T in R)int_T^(T+L)|F(t)|^2dt<infinity`.      (5)

#### 证明

两个 frequencies 的 interval kernel 满足

`|int_T^(T+L)e^(i(lambda-mu)t)dt|`

`                         <=min(L,2/|lambda-mu|)`. (6)

其 modulus 与 `T` 无关。按 unit bins 分组：`|k-l|<=1` 的贡献由
`sum_k A_k^2<infinity` 控制。对同号且 `k<=l<=2k` 的其余项，式 (6) 给

`sum_k [log(2+k)^(2B)/k^2]sum_(d<=k)1/d<infinity`; (7)

对 `l>2k`，使用 `|k-l|asymp l`，贡献至多

`sum_k [log(2+k)^B/k]`

`       *sum_(l>2k)log(2+l)^B/l^2<infinity`.      (8)

异号 bins 的 separation 是 `asymp |k|+|l|`，由同一 far-range estimate
控制。因此式 (4) 的 interval squared norm double series absolute convergent，
且 bound independent of `T`。对 coefficient tails 重复同一估计给 uniform
`L^2` Cauchy convergence，得到式 (5)。`□`

关键是 unit-bin `l^1` mass 的平方可和加一层 harmonic interaction；仅知道
`sum|a_j|^2<infinity` 并不足以自动给 uniform local bound。

## 2. RH 下 Chebyshev current 的 uniform local bound

### 定理 MK（critical Chebyshev current is Stepanov bounded）

假设 RH。令

`f(t)=e^(-t/2)[psi(e^t)-floor(e^t)]`.              (9)

则对每个 fixed `L>0`，

`sup_(T>=0)int_T^(T+L)|f(t)|^2dt<infinity`.       (10)

#### 证明

RH 下 explicit formula 的 nondecaying part 是

`-sum_gamma [m_gamma/(1/2+igamma)]e^(igamma t)`.  (11)

Riemann--von Mangoldt local count 给

`sum_(gamma in [k,k+1))m_gamma=O(log(2+k))`.      (12)

所以式 (11) 的 unit-bin coefficient mass 是
`O(log(2+k)/(1+k))`；负 ordinates相同。引理 MJ（`B=1`）给 uniform local
`L^2`。trivial zeros、archimedean terms 以及 `floor(e^t)` 与 smooth main term
的 interpolation difference 都属于 `L^2(0,infinity)`，且其 fixed-length
local norms uniformly bounded；加入它们得到式 (10)。`□`

这一步提供了文档 060/061 中未从抽象 Besicovitch tightness 自动获得的
Stepanov uniformity；它使用了 zeta zeros 的局部计数这一额外 finite-order
输入。

## 3. Epsilon-free Cramér--Selberg criterion

定义

`V(X)=int_X^(2X)|psi(x)-x|^2dx`.                  (13)

### 定理 ML（sharp multiplicative-block RH criterion）

以下条件等价：

1. RH；
2. `V(X)=O(X^2)` uniformly for `X>=2`；
3. step discrepancy 满足

   `int_X^(2X)|psi(x)-floor(x)|^2x^(-2)dx=O(1)`； (14)

4. 文档 068 的 dyadic line-flow block energies

   `Q_k=sum_(2^k<=n<2^(k+1))`

   `             |psi(n)-n|^2/[n(n+1)]`          (15)

   uniformly bounded。

#### 证明

RH 下式 (14) 由定理 MK 取 `L=log2` 与 `x=e^t`。在 `[X,2X]` 上
`x^(-2)asymp X^(-2)`，故 step variance 为 `O(X^2)`。smooth discrepancy
与 step discrepancy 相差 `x-floorx`，其 squared block norm 是 `O(X)`；
Cauchy--Schwarz 给式 (13) 的 `O(X^2)`，所以 1 推 2–4。

反之，2 与 step/smooth comparison 给 3；3 在 dyadic log blocks 上求和，
得到文档 068 的 prefix energy `P(N)=O(logN)`，定理 MA 推出 RH。式 (14)
与 (15) 的 equivalence 来自 exact interval decomposition 及
`1/[n(n+1)]asymp X^(-2)`。`□`

所以文档 042 定理 GB 中的 `X^epsilon` 可以在 RH 等价陈述中完全移除。
证明 RH 的困难仍未降低：无条件把 exponent 从 `3-o(1)` 降到精确 `2`
仍具有 RH 的全部强度。

## 4. Dyadic direct-sum Hodge structure

### 命题 MM（exact logarithmic-scale direct sum）

对 integer `J>=1`，

`P(2^J)=sum_(k=0)^(J-1)Q_k`.                      (16)

令

`q_star=limsup_(k->infinity)`

`       log(max(1,Q_k))/(klog2)`。                (17)

则

`q_star=max(0,2Theta-1)`.                         (18)

RH 等价于任一以下条件：

- `sup_kQ_k<infinity`；
- `sum_(k<J)Q_k=O(J)`；
- `Q_k=2^(o(k))`。

#### 证明

式 (16) 是式 (15) 按 dyadic edges 对 prefix energy 的精确 partition。定理
ML 给第一个 equivalence，定理 MA 给第二个，文档 042 定理 GA 对
`V(2^k)/2^(2k)` 应用 step/smooth comparison 给式 (18) 与第三个。
`□`

注意这些条件在 zeta 上因 divisor theory 而等价；对 arbitrary nonnegative
sequence，bounded blocks、linear partial sums 与 subexponential blocks 并不
逻辑等价。

## 5. Fixed annular local blocks

固定 `0<h_0<h_1` 与 `L>0`，令

`B_ann(T;L)=int_T^(T+L)int_(h_0)^(h_1)`

`                              |b_h(t)|^2dhdt`.    (19)

### 定理 MN（uniform fixed-annular-block criterion）

RH 当且仅当

`sup_(T>=0)B_ann(T;L)<infinity`。                  (20)

#### 证明

RH 下命题 KA 把 `b_h` 写成 `f(t+-h)` 与 fixed-width integral of `f` 的
有限组合；定理 MK 在稍大的 fixed interval 上给 uniform `L^2` upper bound，
再积分 `h` 得式 (20)。反之，若式 (20) 成立，把 `[0,T]` 分成 `O(T/L)`
个 blocks，得到 cumulative annular energy `O(T)`；文档 067 定理 LV 推出
RH。`□`

这解决 fixed nondegenerate width band 的 local-mean converse。它不声称对
shrinking widths `eta->0` 有文档 061 的 natural normalized uniform bound；
后者仍需要随 `eta` 一致的额外估计。

## 6. General Gamma--Euler sharp block theorem

### 定理 MO（general Stepanov--Selberg centerline theorem）

考虑中心 `c/2` 的 paired Gamma--Euler current，假设：

1. 文档 068 定理 MD 的 visible prefix explicit formula；
2. centerline divisor coefficients 为 `O(m_rho/|rho|)`；
3. local divisor count

   `sum_(gamma in [k,k+1))m_gamma=O(log(2+k)^B)`  (21)

   对某个 fixed `B` 成立。

令 centered counting discrepancy 为 `E_Z(x)`，并定义

`V_Z(X)=int_X^(AX)|E_Z(x)|^2dx`                   (22)

对任意 fixed `A>1`。则全部 divisor 位于 `Re rho=c/2` 当且仅当

`V_Z(X)=O_A(X^(c+1))`.                            (23)

等价地，normalized step current 的每个 fixed log block 有 uniform `L^2`
bound；也等价于 general prefix line-graph blocks

`sum_(X<=n<AX)w_(c,n)|A_n|^2=O_A(1)`.            (24)

#### 证明

centerline 下 assumptions 2–3 给 unit-bin coefficient mass
`O(log(2+k)^B/k)`；引理 MJ 给 uniform local `L^2`。变量替换 `x=e^t`
把它变成式 (23)，因为 normalized energy weight 是 `x^(-c-1)`。
反向对 fixed multiplicative blocks 求和得到 `P_c(N)=O(logN)`，定理 MD
推出中心线。式 (24) 是权重 (6) 的 discrete interval identity。`□`

该定理覆盖 zeta、primitive Dirichlet L-functions 以及具有标准 fixed-degree
local zero count 的 automorphic L-data；若 conductor/degree 随 family 变化，
式 (21) 的 constants 必须单独保持 uniform。

## 7. 存在性审计

sharp block formulations 现在区分清楚：

- anchored Cesàro `O(T)`：由正 Abel Tauberian theory 等价 RH；
- fixed log-block `O(1)`：RH 加 local divisor count 后成立，并反推 RH；
- shrinking-width normalized blocks：仍需 `eta`-uniform input，不能由上述
  fixed-scale theorem 自动推出。

对 zeta，finite block kernels 与 local zero-count mechanism 均已确定；未证的
仍是从 prime side 无条件获得式 (13) 的 `O(X^2)` cancellation。
