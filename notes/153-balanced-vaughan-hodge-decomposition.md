# 配平 Vaughan 恒等式与完整 component Hodge Gram

文档 152 把 Dirichlet convolution 实现为 logarithmic translations，并把经典
RH 的剩余输入压成 balanced Type I/II Bessel budget。本节完成其中的第一项：
选定一条逐系数精确、连续主项不被静默丢弃的 Vaughan 分解，并把它提升为
triangular Hodge vectors 的完整 component Gram。

结果不是 RH 的证明。新的无条件内容是：

1. `Lambda-1` 被四个显式 Vaughan components 精确重构；
2. `d[psi(u)-u]` 被这四个 atomic components 与一个规范 unit-cell remainder
   精确重构；
3. 每个卷积 component 都进入文档 152 的 translation tensor realization；
4. 所有跨 component 相消由一个有限 Hermitian Gram 精确保留；
5. 尚缺的 RH-strength 输入被进一步定位为这个 Gram（或其 Bessel majorant）与
   unit-cell remainder 的 dyadic Cauchy-capacity预算。

## 1. 逐系数精确的 centered Vaughan identity

在 Dirichlet convolution algebra 中记 `1(n)=1`，卷积单位为 `epsilon`。令

`mu_1(n)=mu(n)1_(n<=U)`,    `mu_2=mu-mu_1`,

`Lambda_1(n)=Lambda(n)1_(n<=V)`,

`Lambda_2=Lambda-Lambda_1`.                         (1)

定义四个 centered coefficients

`A_U=mu_1*log-1`,

`B_(U,V)=-mu_1*Lambda_1*1`,

`C_(U,V)=mu_2*Lambda_2*1`,

`D_V=Lambda_1`.                                    (2)

### 定理 AAV（exact balanced Vaughan identity）

对任意正整数 `U,V,n`，

`Lambda(n)-1=A_U(n)+B_(U,V)(n)+C_(U,V)(n)+D_V(n)`. (3)

此外：

- `B` 只含 `d<=U,m<=V` 的三因子项 `dmr=n`；
- `C` 只含 `d>U,m>V` 的三因子项，故在
  `n<(U+1)(V+1)` 时严格为零；
- `D` 只支撑在 `n<=V`。

#### 证明

由 `log=Lambda*1` 与 `mu*1=epsilon`，

`mu_1*log-mu_1*Lambda_1*1+mu_2*Lambda_2*1+Lambda_1`

`=mu_1*Lambda_2*1+mu_2*Lambda_2*1+Lambda_1`

`=mu*Lambda_2*1+Lambda_1`

`=Lambda_2*(mu*1)+Lambda_1=Lambda`.                (4)

两边减去 `1` 得式 (3)。support assertions 直接来自式 (1)--(2)。`□`

这是 Vaughan identity 的全整数版本；只在 `n>V` 使用时，最后的 low term
`D_V(n)` 自动消失。`-1` 被放进 `A_U` 而不是单独成为一个大向量，这是随后
prime--continuum 配平的关键。经典来源与 Type I/II 语境见文献 34；本文所需
形式已由式 (4)独立证明。

## 2. 连续项的规范 unit-cell remainder

令 `q:[1,X+1]->C` 为连续权，并在 logarithmic lag line 上记

`e_u=e_(logu)=1_[logu-h,logu] in H_h`.             (5)

考虑截断 prime--continuum Hodge vector

`V_X=sum_(n<=X)Lambda(n)q(n)e_n`

`                  -int_1^(X+1)q(u)e_u du`.        (6)

定义 unit-cell remainder

`epsilon_X=sum_(n<=X){q(n)e_n-int_n^(n+1)q(u)e_u du}`. (7)

### 定理 AAW（exact prime--continuum measure split）

若 `A,B,C,D` 如定理 AAV，则

`V_X=V_A+V_B+V_C+V_D+epsilon_X`,                  (8)

其中

`V_R=sum_(n<=X)R(n)q(n)e_n`.                      (9)

式 (8) 是精确向量恒等式，不使用 PNT、零点或极限过程。

#### 证明

由式 (3)，前四项之和为

`sum_(n<=X)[Lambda(n)-1]q(n)e_n`.                 (10)

式 (7) 是

`sum_(n<=X)q(n)e_n-int_1^(X+1)q(u)e_u du`.        (11)

相加即式 (6)。`□`

这个余项不能写成“`O(1)`”后丢弃；它必须进入最终 Hodge budget。另一方面它有
完全初等的确定性上界。因为

`||e_u||=sqrt(h)`,

`||e_n-e_u||^2=2min(h,log(u/n))` for `n<=u<=n+1`, (12)

逐 cell 使用 Minkowski 给

`||epsilon_X|| <=sum_(n<=X)int_n^(n+1)`

` [sqrt(h)|q(n)-q(u)|`

` +sqrt(2min(h,log(u/n)))|q(u)|]du`.               (13)

式 (13) 是可认证的 finite bound，但对 Abel weight
`q(u)=u^(-1/2-delta)e^(-u/Y)` 直接求和通常只给 logarithmic 量级；它尚未自动
满足文档 152 式 (22)所需的全 dyadic summability。需要 bounded-overlap、
Euler--Maclaurin cancellation或把 cells与 Type I vector进一步联合短化。

## 3. Vaughan terms 的 translation tensor realization

加入 vertical modulation 后，把

`e_n` 替换为 `n^(-itau)e_n`.                     (14)

文档 152 定理 AAT 给

`e_(dm)=U_(logd)e_m`.                             (15)

### 定理 AAX（balanced Vaughan translation tensor）

式 (8)中的四个 atomic vectors 都有有限 translation synthesis：

- `A` 是 `d<=U` 的 `mu(d)U_(logd)` 作用于 logarithmic inner vectors，再减
  同一个 component 内的 counting vector；
- `B` 是 `d<=U,m<=V` 的 Type I 三因子 synthesis；
- `C` 是 `d>U,m>V` 的 Type II 三因子 synthesis；
- `D` 是 `n<=V` 的有限 low-prime-power vector。

任意 nonseparable Abel weight `q(dmr)` 只使 inner vector依赖 outer indices，
不破坏式 (15)或分解的精确性。

#### 证明

把式 (2)展开为 divisor sums，并对每个乘积 `n=dm` 或 `n=dmr` 使用
`logn=logd+logm(+logr)` 与式 (15)。有限截断允许任意重排。`A` 中的
counting subtraction与 `mu_1*log` 保持在同一个 vector，正是式 (8)的配平。
`□`

这里已经无条件构造了“代数结构”：Dirichlet convolution、unitary length
translations、positive interval-incidence polarization及 arithmetic vector都显式
存在。没有无条件构造的是这些 translated vectors 的统一 Bessel bound。

## 4. 完整 component Gram 与相消守恒

记式 (8)的五个向量为 `v_A,v_B,v_C,v_D,v_epsilon`，定义

`mathcal G_(r,s)=<v_r,v_s>_(H_h)`.                 (16)

### 定理 AAY（component Gram conservation）

矩阵 `mathcal G` 为 positive semidefinite Hermitian Gram，且完整
modulated triangular energy精确为

`G_X=||sum_rv_r||^2=1^*mathcal G1`.               (17)

特别地，

`G_X=sum_r||v_r||^2+2Re sum_(r<s)<v_r,v_s>`.      (18)

因此只报告 component diagonals 不是恒等重构；负的 cross entries可以携带主要
prime--Tate cancellation。安全但可能有损的估计是

`G_X<=5sum_r||v_r||^2`,                           (19)

而 sharper 证明应尽量直接控制式 (17)或在 Schur complement 后再 majorize。

#### 证明

式 (16)是向量族的 Gram，故 Hermitian positive semidefinite。展开式 (8)的
norm square得到式 (17)--(18)；Cauchy--Schwarz给式 (19)。`□`

实现 `balanced_vaughan_coefficients` 逐 `n` 计算式 (2)--(4)；
`balanced_vaughan_modulated_gram_audit` 计算四个 atomic components的完整
`4 x 4` Gram及其对角/cross ledger。它刻意返回
`continuum_cell_component_included=False`，防止有限 atomic audit被误读为已经
控制式 (7)。

## 5. 专门化的中心线判据

对文档 150 的 dyadic square-root core，令 `k` 标记 vertical block，
`beta_k asymp logT_k` 为 barrier，`mathcal G_k` 为式 (16)的完整五分量 Gram。

### 定理 AAZ（balanced Vaughan--Hodge center-line criterion）

在文档 151 定理 AAO的 analytic/barrier hypotheses下，若对一条 cofinal Abel
schedule有

`sup_Y sum_(k in core) [1/beta_k]1^*mathcal G_(Y,k)1<infinity`, (20)

则 RH 成立。一个更强、便于 Type I/II 分别估计的充分条件是

`sup_Y sum_(k in core)[1/beta_k]`

` {5(||v_epsilon||^2+sum_(R=A,B,C,D)B_(R,k)E_(R,k))}<infinity`, (21)

其中 `B_(R,k)E_(R,k)` 是文档 152 式 (21)给出的 translation-synthesis Bessel
majorant。core 外部已由文档 150 定理 AAK无条件控制。

#### 证明

式 (20)正是文档 151 的 modulated energy budget，应用定理 AAO。式 (21)经
定理 AAY式 (19)与文档 152 的 component Bessel bounds推出式 (20)。最后与
定理 AAK的 exterior bound合并。`□`

AAZ 比 AAU 更具体：它固定了 zeta 所需的四个 arithmetic components、连续
余项及全部 support restrictions。它也没有循环地宣称式 (20)或式 (21)成立；
证明其中任一式仍具有 RH 强度。

## 6. 有限审计

取 `delta=.1, theta=.25`，权

`q(n)=n^(-1/2-delta)e^(-n/Y)`, `h=theta/T`.        (22)

下表只含四个 centered atomic components，不含式 (7)：

| `N,U,V,Y,T` | full `1*G*1` | diagonal sum | cross sum |
|---:|---:|---:|---:|
| `80,4,5,30,2` | `.170914` | `.377789` | `-.206874` |
| `80,4,5,30,8` | `.0482943` | `.103258` | `-.0549634` |
| `160,6,7,60,2` | `.204585` | `.510553` | `-.305968` |
| `160,6,7,60,8` | `.0633898` | `.141521` | `-.0781316` |

在 40-digit arithmetic 下逐系数最大重构误差约 `10^(-40)`；测试套件在
60-digit precision下要求 `10^(-48)`。表中 cross term持续为负且占 diagonal
的显著比例，说明分解后立即取 triangle inequality确有明显损失。这些数值只审计
恒等式、Hermitian symmetry与 cancellation ledger，不是区间证书，也不证明
式 (20)。

## 7. 下一步

现在真正需要估计的对象已不再含糊：

1. 对 `A,B` 的 dyadic multiplicative rectangles证明带 counting subtraction的
   Type I Bessel bound；
2. 对 `C` 的 `d>U,m>V` near-product incidences应用 bilinear large sieve；
3. 用 bounded overlap处理 `epsilon`，或采用文档 154 的 exact-continuum gauge将
   unit-cell remainder完全移除；
4. 在选择 `U,V` 时同时优化 Type II support gap `(U+1)(V+1)` 与 Type I
   coefficient mass；
5. 优先控制完整 Schur-compressed Gram式 (17)，只有在 cross blocks无法保留时才
   退到式 (19)。

若这些预算可和，定理 AAZ直接推出 RH；若失败，finite Gram会区分失败来自 Type I
main-term配平、Type II near-collisions还是 unit-cell remainder。

文档 154 随后证明 unit-cell remainder并非 intrinsic obstruction：直接把 exact
continuum vector最优分配给四个未中心化 Vaughan components，可在保持完整能量
不变的同时消除该余项，并最小化 component-diagonal安全预算。
