# 线性 Möbius mollifier、Chebyshev 方差与周期边界层

文档 083 已证明线性 log mollifier 的完整低 Dirichlet defect 是
`Lambda/log N`，但还没有把这一离散 jump current 的 Green potential 求出来。
本节完成这一步。结果是一个精确的三通道 Hodge 分解：局部能量由 Möbius
斜率、Chebyshev 比率的常数正交补、以及二者的标量匹配误差组成；剩余困难
恰是 `x<1/N` 的周期边界层。

## 1. Complete-low potential identity

固定 `N>=2`，写

`L=log N`,

`b_n=mu(n)(1-log n/L) 1_(n<=N)`,

`A_N=sum_(n<=N)b_n/n`,  `a_N=L A_N`,                 (1)

以及

`F_N(y)=1_(y>=1)+sum_(n<=N)b_n {y/n}`.               (2)

令 `psi(y)=sum_(m<=y)Lambda(m)`。

### 定理 PV（exact Chebyshev local potential）

对 `0<y<1`，

`F_N(y)=y A_N`.                                       (3)

对 `1<=y<=N`，

`F_N(y)=y A_N-psi(y)/L`

`      =(y/L)(a_N-psi(y)/y)`.                         (4)

#### 证明

文档 083 的 jump equation 给 `F_N` 的连续斜率 `A_N`。令

`c_N(m)=sum_(d|m,d<=N)b_d`。

从零出发积分 jump current，得到

`F_N(y)=1_(y>=1)+y A_N-sum_(m<=y)c_N(m)`.             (5)

当 `y<=N` 时，推论 PQ 给

`c_N(1)=1`,  `c_N(m)=Lambda(m)/L  (2<=m<=N)`.

把它代入式 (5)；`y>=1` 的两个常数 `1` 精确消去，即得式 (4)。在
`0<y<1` 没有 jump，直接得式 (3)。`□`

这里没有使用素数定理或 RH；式 (4) 是有限除数卷积恒等式的完整势论版本。

## 2. Scalar--variance Hodge decomposition

定义局部能量

`R_N^loc=int_0^N |F_N(y)|^2 dy/y^2`

`       =int_(1/N)^infinity |f_N(x)|^2 dx`,            (6)

其中 `f_N(x)=F_N(1/x)`。再令

`u(y)=psi(y)/y`,

`ubar_N=(1/(N-1))int_1^N u(y)dy`,                     (7)

`V_N=int_1^N |u(y)-ubar_N|^2dy`.                      (8)

### 定理 PW（three-channel local Hodge split）

有精确正交分解

`R_N^loc=(1/L^2)[a_N^2+V_N+(N-1)|a_N-ubar_N|^2]`.    (9)

#### 证明

式 (3) 在 `(0,1)` 的贡献是 `A_N^2=a_N^2/L^2`。式 (4) 给

`int_1^N |F_N(y)|^2dy/y^2`

` =(1/L^2)int_1^N |a_N-u(y)|^2dy`.                   (10)

在 `L^2([1,N])` 中把 `u` 正交投影到常数函数；Pythagoras 恒等式正是

`int_1^N |a_N-u|^2=V_N+(N-1)|a_N-ubar_N|^2`.         (11)

与 `(0,1)` 项合并即得式 (9)。`□`

所以局部问题不是一个模糊的 cancellation：三个非负量分别检测 Tate/斜率
通道、primitive Chebyshev 波动通道和两通道的 scalar compatibility。

## 3. 三个量的有限算术公式

令 `M(t)=sum_(n<=t)mu(n)`。Abel summation 给出

### 定理 PX（Möbius slope and Chebyshev moments）

`a_N=sum_(n<=N) mu(n)log(N/n)/n`

`   =int_1^N M(t)(1+log(N/t))dt/t^2`,                 (12)

并且

`ubar_N=(1/(N-1))sum_(m<=N)Lambda(m)log(N/m)`.        (13)

若 `psi(k)=sum_(m<=k)Lambda(m)`，则

`int_1^N u(y)^2dy`

` =sum_(k=1)^(N-1)psi(k)^2(1/k-1/(k+1))`,            (14)

从而

`V_N=sum_(k=1)^(N-1)psi(k)^2(1/k-1/(k+1))`

`    -(N-1)ubar_N^2`.                                (15)

#### 证明

式 (12) 对权 `log(N/t)/t` 作 Stieltjes 分部积分；其连续导数的负值为
`(1+log(N/t))/t^2`，而端点权在 `t=N` 为零。对式 (13) 交换
`int_1^N sum_(m<=y)Lambda(m)dy/y` 的求和与积分。最后 `psi(y)` 在每个
`[k,k+1)` 上等于 `psi(k)`，逐区间积分 `y^(-2)` 得式 (14)，再减去常数
投影的平方范数即得式 (15)。`□`

式 (12)--(15) 把局部 Hodge block 完全有限化；它们不需要零点数据。

## 4. 未知部分是周期边界层

定义

`R_N^bdry=int_N^infinity |F_N(y)|^2dy/y^2`

`        =int_0^(1/N)|f_N(x)|^2dx`.                  (16)

### 定理 PY（exact bulk--boundary split）

`R_N=R_N^loc+R_N^bdry`,                               (17)

且对 `y>1`，

`F_N(y)=1+sum_(n<=N)b_n{y/n}`                         (18)

是周期函数，其一个共同周期为

`Q_N=lcm(1,2,...,N)`.                                 (19)

更精确地，若 `psi_1` 是 trigamma 函数，则

`R_N^bdry=Q_N^(-2)int_0^Q_N |F_N(N+t)|^2`

`                         psi_1((N+t)/Q_N)dt`.        (20)

#### 证明

式 (17) 是在 `y=N` 分割文档 083 的能量。每个 `{y/n}` 以 `n` 为周期，
故式 (19) 成立。把 `[N,infinity)` 分成长度 `Q_N` 的区间，利用周期性并交换
非负求和与积分；恒等式

`sum_(j>=0)(N+t+jQ_N)^(-2)`

` =Q_N^(-2)psi_1((N+t)/Q_N)`                          (21)

给出式 (20)。`□`

式 (20) 是一个有限正表达式，但 `Q_N` 巨大，不能被误读为有效估计。
它揭示的重点是：文档 083 的“高 Dirichlet tail”在实空间里正是 cutoff
产生的高频周期边界层，而不是低区 Chebyshev current 的一部分。

## 5. 一个精确的有限 RH 充分证书

### 定理 PZ（local Hodge plus boundary certificate）

若存在 cofinal integers `N_j`，使

`a_N^2+V_N+(N-1)|a_N-ubar_N|^2=O(log N)`             (22)

且

`R_N^bdry=O(1/log N)`,                                (23)

则

`R_N=O(1/log N)`, 因而 `d_N->0`，所以 RH 成立。       (24)

#### 证明

定理 PW 将式 (22) 除以 `(log N)^2`，给
`R_N^loc=O(1/log N)`。与式 (23) 及式 (17) 合并后，文档 083 的
`d_N^2<=R_N` 和文档 081 的 Nyman--Beurling--Báez-Duarte 等价给出 RH。
`□`

这一定理没有降低 RH 的逻辑难度，但把候选结构的存在性拆成三个可独立研究的
正通道。尤其，证明平均意义的 Chebyshev 方差仍不足够：还必须验证 Möbius--
Chebyshev scalar matching，并控制小 `x` 边界层。

## 6. 一般 Euler 数据的系数模板

设

`L(s)=sum a(n)n^(-s)`,  `1/L(s)=sum beta(n)n^(-s)`,

并定义 generalized von Mangoldt coefficients

`-L'(s)/L(s)=sum Lambda_L(m)m^(-s)`.                  (25)

令

`beta_N(n)=beta(n)(1-log n/log N)1_(n<=N)`.           (26)

### 命题 QA（universal linear reciprocal defect）

对 `m<=N`，

`sum_(d|m)a(m/d)beta_N(d)`

` =delta_(m,1)+Lambda_L(m)/log N`.                    (27)

#### 证明

constant part 是 `a*beta=delta`。又因

`L(s)(1/L(s))'=-L'(s)/L(s)`,                          (28)

比较 Dirichlet coefficients 得

`-sum_(d|m)a(m/d)beta(d)log d=Lambda_L(m)`，代回
式 (26) 即得式 (27)。`□`

因此“线性 reciprocal cutoff 产生 logarithmic-derivative current”并非 zeta
偶然，而是广泛 Euler/Dirichlet 代数的结构定理。不过，要把式 (27) 提升为
定理 PV--PZ 那样的实空间 Hilbert 结构，还需为 `a(n)` 构造带正确 jumps 的
广义 synthesis features，并独立证明相应 division/density theorem；不能直接
把 zeta 的 fractional-part 模型移植过去。

## 7. 存在性审计与计算实现

目前无条件存在的对象包括：所有 finite coefficients、局部三项 PSD Hodge
分解、周期边界层及其单周期表达式，以及一般 `L` 的低卷积恒等式。尚未证明
的是式 (22)--(23) 的共同尺度；特别是式 (23) 正承载 Möbius cutoff 的全局
相消，给它作逐项绝对值估计会丢失目标 rate。

`scripts/qw_matrix.py` 新增：

- `linear_mobius_mollifier_slope`；
- `weighted_mertens_normalized_slope`；
- `chebyshev_ratio_mean`；
- `linear_mollifier_local_hodge_decomposition`。

回归测试核对定理 PV 的一个非整数点、定理 PX 的 weighted-Mertens
summation-by-parts 公式，并从独立的逐区间积分重建定理 PW 的三项能量。
