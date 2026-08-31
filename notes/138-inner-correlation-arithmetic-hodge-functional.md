# Inner-shift correlation cone 与显式 arithmetic Hodge functional

文档 137 把 Cauchy negative defect精确写成 contractive outer vectors上的
Toeplitz最大负能量，并把 Dirichlet phases识别为 singular inner semigroup
`Theta_lambda`。本节再作两个抽离：

1. Paley--Wiener transform把 `Theta_lambda` 变成单侧平移，因此所有测试方向
   只通过一个 positive-definite autocorrelation `r(lambda)` 出现；
2. 不仅 prime 与 continuum，连 `1/s`、digamma/Gamma current也都能精确写成
   同一个 `r` 上的线性 functional。

所以经典 RH 的剩余结构不再是一个未指定的 Hilbert space：它是一条明确的
**arithmetic orbit measure 对 correlation cone 的 accretivity inequality**。

## 1. Paley--Wiener shift model

沿用 Cayley map `p=(1+q)/(1-q)`。取标准 unitary

`U:H^2(D)->H^2(C_+)->L^2(R_+)`,                    (1)

其中第二箭头是 Laplace/Paley--Wiener transform。multiplication by
`Theta_lambda(q)=e^(-lambda p)` 在 `L^2(R_+)` 上成为 right-shift isometry

`(S_lambda phi)(v)=1_(v>=lambda)phi(v-lambda)`.     (2)

### 定理 YS（inner correlations are one-sided autocorrelations）

若 `phi=Uh`，则

`r_h(lambda):=<Theta_lambda h,h>`

` =int_0^infinity phi(u)conjugate(phi(u+lambda))du`. (3)

将其扩张为 `r_h(-lambda)=conjugate(r_h(lambda))` 后，`r_h` 是 `R` 上
continuous positive-definite function，且

`r_h(0)=||h||_2^2<=1`, `|r_h(lambda)|<=r_h(0)`,    (4)

并有 `r_h(lambda)->0` as `lambda->infinity`。

#### 证明

式 (2) 给

`<S_lambda phi,phi>`

` =int_lambda^infinity phi(v-lambda)conjugate(phi(v))dv`，

换元即为式 (3)。把 `phi` 零延拓到 `R`，式 (3) 是普通 translation
autocorrelation；所以任意矩阵
`[r_h(lambda_j-lambda_k)]` 是 translated vectors的 Gram，得到 positive
definiteness。式 (4) 来自 Cauchy--Schwarz；translation weakly趋零给最后一项。
`□`

contractive outer条件 `||h||_infinity<=1` 选出 positive-definite cone 的一个
真子集；把它放宽为全部 `||phi||_2<=1` 可给 sufficient 但更强的证书。文档
137 的 exact defect必须保留原 cone，不能无说明地把放宽后的失败当成原问题
失败。

## 2. Archimedean data 也属于同一个 semigroup

写

`sigma_0=1/2+delta`, `s(q)=sigma_0+p`,              (5)

并令 `r(lambda)=<Theta_lambda h,h>`, `r_0=r(0)`。

首先，

`1/s(q)=int_0^infinity e^(-sigma_0u)Theta_u(q)du`, (6)

所以

`<s^(-1)h,h>=int_0^infinity e^(-sigma_0u)r(u)du`. (7)

其次使用对 `Re z>0` 有效的 digamma identity

`psi(z)=-gamma+int_0^infinity`

`             [e^(-t)-e^(-zt)]/(1-e^(-t))dt`.     (8)

代入 `z=s(q)/2` 得

`<(1/2)psi(s/2)h,h>`

` =-(gamma/2)r_0`

` +(1/2)int_0^infinity [e^(-t)r_0`

`       -e^(-sigma_0t/2)r(t/2)]/(1-e^(-t))dt`.    (9)

式 (9) 在 `t=0` 的 cancellation必须整体保留；把两项分别积分会制造假
divergence。这正是 Gamma regularization 在 orbit-semigroup语言中的形式。

## 3. Prime--continuum orbit functional

Abel continuum current作 `x=e^lambda` 换元：

`I_Y(s(q))=int_0^infinity e^((1-sigma_0)lambda)`

`              e^(-e^lambda/Y)Theta_lambda(q)dlambda`. (10)

prime current为

`S_Y(s(q))=sum_(n>=2)Lambda(n)n^(-sigma_0)e^(-n/Y)`

`                         Theta_(log n)(q)`.       (11)

因此定义完整 scalar Hodge functional

`H_(Y,delta)[r]=-(logpi+gamma)r_0/2`

` +int_0^infinity e^(-sigma_0u)r(u)du`

` +(1/2)int_0^infinity [e^(-t)r_0`

`       -e^(-sigma_0t/2)r(t/2)]/(1-e^(-t))dt`

` +int_0^infinity e^((1-sigma_0)lambda)e^(-e^lambda/Y)`

`                         r(lambda)dlambda`

` -sum_(n>=2)Lambda(n)n^(-sigma_0)e^(-n/Y)r(log n)`. (12)

### 定理 YT（exact correlation-functional identity）

对每个 contractive outer `h`，

`Re<g_(Y,delta)h,h>=Re H_(Y,delta)[r_h]`.          (13)

因而

`J_(Y,delta)/pi`

` =sup_(h outer, ||h||_infinity<=1)`

`                  [-Re H_(Y,delta)[r_h]]`.        (14)

#### 证明

式 (7)、(9)--(11) 分别代入 Abel candidate
`1/s-(logpi)/2+psi(s/2)/2+I_Y-S_Y`，得到式 (12)--(13)。文档 137
定理 YP再给式 (14)。所有 interchange对固定 `Y,delta>0` 由 exponential
cutoff、`|r(lambda)|<=r_0` 与式 (9) 的 removable cancellation保证。`□`

当 `h=1` 时，`r(lambda)=Theta_lambda(0)=e^(-lambda)`；式 (12)退化为
`F_Y(delta+1)`。这同时解释文档 137 的 Poisson signed mean为何只是 correlation
cone 中的单个 constant-vector probe，而不能控制 worst outer direction。

## 4. 广义 orbit-correlation Weil theorem

令 `Gamma subset R_+` 是 length semigroup，`Theta_lambda` 是 Hilbert space上的
inner/isometric representation。设一个 self-dual arithmetic divisor的
regularized logarithmic derivatives可写成

`H_n[r]=H_(infinity,n)[r]+int_Gamma r(lambda)dnu_n(lambda)`, (15)

其中 `nu_n` 是 discrete orbit measure减去 continuum/pole comparison，
`H_infinity` 是像式 (7)、(9) 那样的 archimedean generator form。

### 定理 YU（orbit-correlation filtered Weil theorem）

在文档 136 定理 YL 的 holomorphy、Poisson admissibility与 Euler-open-set
convergence条件下，若

`inf_(r in C_outer) Re H_n[r]>=-epsilon_n`,

`epsilon_n->0`,                                    (16)

其中 `C_outer={r_h: h outer, ||h||_infinity<=1}`，则 arithmetic germ有
positive-real continuation，相应 self-dual order-one zeta divisor的全部 zeros
位于中心线。

#### 证明

定理 YT/文档 137 定理 YP把式 (16)识别为 `J_n/pi<=epsilon_n`。应用文档
136 定理 YL及文档 131 定理 XQ。`□`

定理 YU 抽出的数据足够广：

- closed-orbit/Euler data只需给 additive length semigroup与 signed orbit
  measures；
- archimedean local factors只需能写成 isometric semigroup generator form；
- exact cohomological intersection positivity可由 `epsilon_n=0` 恢复；
- 数域 filtered package只要求式 (16) 的 uniform `o(1)` accretivity。

## 5. 有限 correlation certificates

实现新增：

- `finite_shift_autocorrelation`：对有限零延拓向量计算式 (3) 的离散版本；
- `autocorrelation_toeplitz_gram`：构造其 Hermitian Toeplitz Gram，并用于检查
  positive-definite correlation constraint；
- `cayley_dirichlet_inner_value`：文档 137 定理 YQ 的 inner semigroup值。

这些工具允许下一步在有限 lag mesh上优化式 (12)，但有限 mesh只有在控制
continuous-lag interpolation与 infinite tail后才是严格证书。

## 6. 新的精确障碍与下一步

经典 RH 现被压成式 (12) 在 `C_outer` 上的 uniform lower bound。三种粗化会
丢失关键结构：

1. 对 prime coefficients取 absolute sum：丢失 signed discrete--continuum
   cancellation；
2. 只保留 `|r(lambda)|<=r_0`：丢失 positive-definite Toeplitz constraints；
3. 把 `C_outer` 换成任意 pointwise bounded functions：丢失 outer/cyclic
   realizability。

文档 139 已执行这项审计：仅保留 positive definiteness会允许 point-mass
characters并塌缩到最深 negative well，因此过度放宽。正确 finite cone还必须
保留 Cauchy spectral cap，等价于双正 Gram约束
`0<=R<=K_C`。文档 140 又把该 Loewner interval上的 linear optimization求成
negative spectral trace闭式；后续应直接构造式 (12) 的带误差 quadrature，
而不再使用 uncapped correlation cone。
