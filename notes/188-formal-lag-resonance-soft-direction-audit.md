# Formal lag resonance 分解与 canonical soft direction 审计

文档 187 把 negative Hodge index 化成一个 canonical Chebyshev orbit response。
本笔记把该 response 接到 actual finite Abel prime--continuum quadrature，并解决
两个实现/逻辑问题：

1. `log n` 的 exact product relations必须用有理 products形式判定，不能靠
   floating tolerance；
2. continuum quadrature lags必须保留独立 formal coordinates，只有形式向量
   真正相消时才进入 exact bucket。

在这个 formal lag algebra 中，soft response精确分成 exact、near、far 三部分。
far 部分有直接 exponential variation bound；真正开放核心是一个指定
Chebyshev direction 上的 signed near-product sum。小尺度审计显示 degree two
发生很强的 signed cancellation，但相对于同支撑 arbitrary direction尚未显示
随尺度改善，因此该路线保持观察而不能升级为 RH 证据。

## 1. Product--continuum formal lag group

固定 continuum quadrature nodes `lambda_1,...,lambda_m`。定义 abelian group

`G=Q_(>0)^times direct-sum Z^m`,                 (1)

并把 `(r,k_1,...,k_m)` 的 numerical lag定义为

`ell(r,k)=log r+sum_jk_jlambda_j`.               (2)

integer atom `log n` 表示为 `(n,0)`，第 `j` 个 continuum node表示为
`(1,e_j)`。加法对应 rational products相乘及 continuum coordinates相加；取负
对应 ratio求逆和 coordinates变号。

### 定理 AGE（formal exactness is product exactness）[U]

对只含 integer log atoms的 lag word，formal sum为零当且仅当正号一侧 integer
product 与负号一侧 product精确相等。对包含 continuum nodes的 word，formal
sum为零当且仅当 rational product为一且每个 quadrature coordinate总系数为零。

因此 formal zero不会把一个很小但非零的 near product误判为 exact，也不会把两个
数值接近的 continuum cells合并。

#### 证明

`Q_(>0)^times` 中 equality就是 reduced rational equality；unique factorization
给 integer product陈述。direct-sum coordinates逐坐标为零给 continuum陈述。
`square`

这个 formal group描述的是 finite quadrature model。物理 continuum integral中
不同 cells之间的极限关系仍由 quadrature error ledger控制，不能由形式独立性
冒充正交性。

## 2. Exact--near--far response ledger

令 real stationary symbol与 Chebyshev effect分别为

`P(t)=sum_(omega in G)d_omega e^(-i ell(omega)t)`, (3)

`b(t)=sum_(u in G)beta_u e^(-i ell(u)t)`.        (4)

定义 residual `r=omega+u-v`。Cauchy response为

`R(P,b)=-int P(t)|b(t)|^2dmu(t)`

` =-sum_(omega,u,v)d_omega beta_u conjugate(beta_v)`

`       *e^(-|ell(omega+u-v)|)`.                 (5)

固定 threshold `h>0`，按

- exact: `r=0 in G`；
- near: `r ne 0` 且 `|ell(r)|<=h`；
- far: `|ell(r)|>h`

分成 `R_exact,R_near,R_far`。

### 定理 AGF（three-zone identity and far bound）[U]

精确地

`R=R_exact+R_near+R_far`,                        (6)

且

`|R_far|<=e^(-h)||d||_1||beta||_1^2`.           (7)

此外 `R_exact` 正是 formal frequency product
`-P|b|^2` 的 identity coefficient。

#### 证明

式 (6)只是 disjoint partition。far triples均满足 Cauchy factor至多 `e^(-h)`；
对其余 coefficients取绝对值并扩张到所有 triples即得式 (7)。当 residual为
formal zero时 Cauchy factor为一，求和正是 identity coefficient。`square`

式 (7)仍可能因 `||beta||_1` 增长而无效；它只说明 far sector 的正确 ledger，
不宣称已控制共尾极限。

## 3. Degree-two canonical factorization

在 symmetric interval `[-B,B]` 上，用 degree-two Chebyshev interpolation逼近

`a_rho(x)=(-x)_+/((-x)_++rho)`.                  (8)

三个 interpolation nodes为 `-aB,0,aB`，其中 `a=sqrt(3)/2`。因为
`a_rho(0)=a_rho(aB)=0`，插值 polynomial必有因子

`p_2(x)=c x(x-aB)`,                              (9)

其中

`c=2A/(3B^2)`, `A=aB/(aB+rho)`.                 (10)

### 定理 AGG（degree-two shifted-moment identity）[U]

未作 contraction rescaling 时，canonical response为

`R_2=-c^2 int P(t)^3(P(t)-aB)^2dmu(t)`

`   =-c^2[m_5-2aB m_4+a^2B^2m_3]`.             (11)

所以 degree two自动消去 zeroth、first、second shifted moments，只读取一个指定的
`m_3,m_4,m_5` combination。形式 lag版本由 Chebyshev convolution recurrence
逐字给出。

#### 证明

把式 (9)代入 `-int P p_2(P)^2dmu` 并展开。`square`

式 (11)解释为何 degree two与 degree one的 cancellation可能显著不同；但它没有
自动给出符号，因为 odd/even moments仍含全部 near-product correlations。

## 4. Three-zone soft Hodge criterion

结合文档 187 的 polynomial approximation error，得到：若 cofinal symbols
`P_n`、canonical contractions `b_n` 与 thresholds `h_n` 满足

`sup_n {R_(exact,n)+R_(near,n)`

`       +e^(-h_n)||d_n||_1||beta_n||_1^2`

`       +2rho_n+5epsilon_n tau_n(|P_n|)+eta_n}<infinity, (12)

则 `sup_n tau_n((P_n)_-)<infinity`，由 bounded finite-trace Hodge--Weil
theorem推出中心线结论。

该 criterion 比 absolute occupancy bound更窄：exact 与 near sectors保留
canonical coefficient signs；只有 far sector取绝对值。尚未证明的是式 (12)的
arithmetic bound。

## 5. Finite prime--continuum audit

脚本 `scripts/audit_soft_zeta_orbit.py` 使用：

- `sigma=0.6`；
- Abel scales `Y=4,8,12`；
- integer cutoffs `7,10,12`；
- 两个 continuum lag cells；
- `rho=B/3`；
- near threshold `h=0.5`。

prime atoms与 continuum cells由 shared-lag quadrature分别返回，再在 formal
group (1) 中合成。以下均为 double-precision finite diagnostics：

表中使用 raw Chebyshev interpolant；若按文档 187 除以 `1+epsilon` 变成严格
contraction，三个 signed buckets与 absolute variation同时乘同一正因子，
cancellation ratio和 Rayleigh depth ratios不变。

| `Y,N,L` | support | signed response | absolute variation | cancellation ratio | canonical/arbitrary depth |
|---:|---:|---:|---:|---:|---:|
| `4,7,1` | 15 | .06781 | .5785 | .1172 | .9031 |
| `4,7,2` | 109 | .004942 | .5353 | .009232 | .4134 |
| `8,10,1` | 19 | .07433 | .8419 | .08828 | .6655 |
| `8,10,2` | 165 | .004495 | .7527 | .005972 | .3879 |
| `12,12,1` | 21 | .08044 | .9750 | .08250 | .5835 |
| `12,12,2` | 205 | .005632 | .8719 | .006459 | .3859 |

这里 cancellation ratio是 `|signed response|/sum|triple terms|`；最后一列把
canonical negative Rayleigh depth与同一 formal support上的 optimal arbitrary
direction比较。

在 frozen `Y=8,N=10,L=2` 例中，

`R_exact=.03132`, `R_near=-.04089`, `R_far=.01407`. (13)

absolute variations分别约 `.03247,.2796,.4406`。prime 与 continuum outer
components 都呈相同的 `positive exact / negative near / positive far` pattern。

## 6. What the finite data does and does not show

### 支持继续研究的现象

degree two的 signed-to-variation ratio在三个小尺度均约 `0.006--0.009`，比
degree one低约一个数量级以上。说明 canonical shifted-moment combination保留了
逐项绝对值会完全丢失的 cancellation。

### 尚未显示的现象

degree-two canonical/arbitrary depth ratio稳定在约 `.39--.41`，没有在这些尺度
趋零。canonical direction仍读取同支撑相当一部分负方向，不能声称它绕开了
arbitrary-direction resonance barrier。

### 不能作的外推

support size从 `109` 增至 `205` 已快速增长；当前数据既非 interval arithmetic，
也非 cofinal schedule。`rho=B/3` 的 additive soft error也很大。表格只验证
formal decomposition与发现 response-specific cancellation，不构成 RH 数值证据。

## 7. 下一最小引理

下一任务不再扩大 brute-force degree，而是直接处理式 (11)：

1. 用 balanced prime--continuum coefficients写出 `m_3,m_4,m_5` 的 common
   exact-product convolution；
2. 证明 continuum centering是否使式 (11)的 leading diagonal/exact terms
   cancellation，而非只在小尺度出现；
3. 对 signed near sector寻找 response-specific large-sieve bound，禁止逐项绝对值；
4. 用式 (7)选择随 scale增长的 `h`，同时控制 `||beta||_1`；
5. 若上述 combination化简后仍等价于文档 169 的完整 Selberg profile，就把
   NCE-8 标记为等价重述。

## 8. 审计结论

本笔记首次把 canonical soft Hodge effect接到 actual finite balanced
prime--continuum orbit，并用 formal products严格区分 exact与near resonances。
degree-two方向显示强 signed cancellation，提供了比 universal Bessel bound更窄的
新目标；但 arbitrary-direction比例没有改善趋势。当前最有价值的开放对象是
`m_5-2aBm_4+a^2B^2m_3` 的 arithmetic factorization，而不是更多无结构 moments。
