# Matrix-valued Bessel--Weil 判据与 component-channel 压缩

文档 152--155 把 prime--continuum Hodge vector分成四个 Vaughan channels，并逐步
消除了 continuum与 cutoff gauges的任意性。它们仍用

`||sum_rv_r||^2<=Rsum_r||v_r||^2`                 (1)

把完整 Gram压成对角预算。本节保留 component-index matrix，证明 matrix-valued
Bessel--Weil center-line theorem，并给 finite vector errors到 Loewner majorant的
严格传递。数值审计显示当前四通道 Gram近似 rank two；这为下一步 bilinear估计
指定了比四个独立 scalar bounds更窄的目标。

## 1. 物理方向与 matrix Bessel bound

在一个 vertical block中令 `v_1,...,v_R in H`，component Gram为

`G_(r,s)=<v_r,v_s>>=0`.                            (2)

令 physical synthesis vector `e=(1,...,1)^T`。完整 modulated energy为

`mathcal E=e^*Ge=||sum_rv_r||^2`.                 (3)

### 定理 ABI（matrix-valued Bessel--Weil criterion）

在文档 151 定理 AAO的 analytic/barrier hypotheses下，若每个 core block有一个
Hermitian matrix `M_k` 满足

`G_k<=M_k` in Loewner order,                       (4)

且

`sup_Y sum_(k in square-root core)e^*M_(Y,k)e/beta_(Y,k)<infinity`, (5)

则相应 divisor的全部 zeros位于中心线。

若只知道 component bounds `||v_r||^2<=B_r`，则

`G<=R diag(B_1,...,B_R)`,                          (6)

故文档 152 的 scalar Type I/II criterion是本定理的 diagonal特例。

#### 证明

式 (4)给 `mathcal E_k<=e^*M_ke`；式 (5)就是文档 151 所需的 block
modulated-energy budget，core exterior由文档 150 定理 AAK处理，再应用定理
AAO。为证式 (6)，对任意 `z in C^R`，

`z^*Gz=||sum_rz_rv_r||^2`

` <=(sum_r|z_r|sqrt(B_r))^2<=Rsum_rB_r|z_r|^2`.   (7)

这正是式 (6)。`□`

式 (5)只沿 physical direction读取 matrix majorant。`M` 在 cancellation channels
上可以很大，只要其 physical compression可和；这比 operator-norm或逐对角控制
更接近 Weil pairing只评估 actual arithmetic cycle的机制。

## 2. Finite approximants 的 Loewner error transfer

设 exact vectors `v_r` 有 approximants `v_tilde_r`，满足

`||v_r-v_tilde_r||<=eta_r`,

`||v_tilde_r||=a_r`.                               (8)

记 exact/approximate Grams为 `G,G_tilde`。定义 nonnegative symmetric matrix

`E_(r,s)=eta_ra_s+eta_sa_r+eta_reta_s`,            (9)

以及

`rho=max_rsum_sE_(r,s)`.                           (10)

### 定理 ABJ（error-stable Gram Loewner enclosure）

有

`G<=G_tilde+rho I_R`.                              (11)

因此 exact physical energy满足

`e^*Ge<=e^*G_tilde e+rho R`.                      (12)

另有常常更锐的 direct-vector bound

`sqrt(e^*Ge)<=sqrt(e^*G_tilde e)+sum_reta_r`.      (13)

#### 证明

写 `d_r=v_r-v_tilde_r`。Gram entry之差是

`<d_r,v_tilde_s>+<v_tilde_r,d_s>+<d_r,d_s>`,      (14)

故 modulus至多式 (9)。Hermitian difference `Delta=G-G_tilde` 的 spectral norm
由 symmetric row-sum Schur bound至多为 `rho`，所以 `Delta<=rho I`，得到式
(11)--(12)。式 (13)对 `sum_rv_r=sum_rv_tilde_r+sum_rd_r` 使用 triangle
inequality。`□`

实现 `component_gram_vector_error_majorant` 返回式 (9)--(11)；
`matrix_bessel_loewner_certificate` 数值检查 `M-G>=0` 的 spectrum及 physical
compression。这样文档 154--155 的 continuum localization、prime tail及 gauge
errors可以先在 vector norm层认证，再进入 matrix criterion。

## 3. Canonical eigenchannels

令

`G=sum_(j=1)^R lambda_j q_jq_j^*`,

`lambda_1>=...>=lambda_R>=0`.                      (15)

### 定理 ABK（physical channel decomposition）

完整 energy精确分解为

`e^*Ge=sum_jlambda_j|q_j^*e|^2`.                  (16)

令 `G_[q]` 保留前 `q` 个 eigenchannels，则

`G<=G_[q]+lambda_(q+1)I`,                         (17)

并且遗漏 physical energy精确为

`sum_(j>q)lambda_j|q_j^*e|^2`

` <=lambda_(q+1)||e||^2`.                         (18)

#### 证明

谱定理给式 (16)。tail operator
`sum_(j>q)lambda_jq_jq_j^*` 在其支撑上的 norm为 `lambda_(q+1)`，故式
(17)--(18)。`□`

式 (16)建议区分两个 rank概念：

- ordinary stable rank `(trG)^2/||G||_F^2`；
- physical participation ratio
  `(e^*Ge)^2/sum_j[lambda_j|q_j^*e|^2]^2`。

后者直接测量 arithmetic total direction实际使用多少 eigenchannels。
`component_gram_channel_spectrum` 计算两者、每个 physical contribution及累计比例。

## 4. Rank-compressed generalized structure theorem

### 定理 ABL（rank-`q` matrix Hodge center-line theorem）

设一般 Gamma--Euler data满足文档 151 的显式公式与 barrier hypotheses，并在每个
core block有 canonical `R`-component Hodge Gram `G_k`。若可构造 positive
rank-`q` matrices `M_(q,k)` 与 tail bounds `epsilon_k>=0`，使

`G_k<=M_(q,k)+epsilon_k I_R`,                      (19)

并满足

`sup_Y sum_k[e^*M_(q,Y,k)e+R epsilon_(Y,k)]`

`                         /beta_(Y,k)<infinity`,   (20)

则全部 zeros位于中心线。

对 zeta，文档 153--155 的 Vaughan/continuum/simplex constructions无条件给每个
finite block的 `R=4` Gram及其 exact spectral compression。未证的存在性输入是：
从 Type I/II arithmetic无循环构造 fixed或缓慢增长 rank的 `M_q`，并证明式
(20)沿 cofinal Abel schedule一致成立。

#### 证明

式 (19)是定理 ABI的 majorant，且
`e^*(epsilon I)e=epsilon||e||^2=R epsilon`。应用定理 ABI。`□`

ABL 抽离出的结构比 scalar Bessel budget更广：允许多个 weight channels形成一个
matrix polarization，只需其 physical compression和 tail capacity可和。这与有限域
Weil证明中“先按 weights分解，再用 Hodge--Riemann form控制 actual cycle”形式对应。

## 5. Vaughan simplex Gram 的 finite channel audit

沿文档 155 的四组 `(N,Y,T)`，对 stable simplex gauge的 `4 x 4` Gram作式
(15)--(16)分解：

下表的 top-`q` capture按单个 channel的 **physical contribution**
`lambda_j|q_j^*e|^2` 排序，用来测量 actual arithmetic direction；定理 ABK式
(17)的 operator tail则按 eigenvalue排序。两种排序一般不应混同，尽管在部分
finite samples中会一致。

| `N,Y,T` | stable rank | physical participation | top-1 capture | top-2 capture | diagonal loss |
|---:|---:|---:|---:|---:|---:|
| `80,30,2` | `1.999` | `1.983` | `56.69%` | `99.46%` | `2.686` |
| `80,30,8` | `2.019` | `1.843` | `64.69%` | `99.91%` | `2.321` |
| `160,60,2` | `2.038` | `1.314` | `86.15%` | `99.95%` | `1.862` |
| `160,60,8` | `1.991` | `1.179` | `91.73%` | `99.98%` | `1.715` |

这里 diagonal loss是式 (6)给出的 `R trG/(e^*Ge)`。所以 scalar criterion在这些
finite blocks上损失 factor `1.7--2.7`；前两个 spectral channels却已经捕获至少
`99.45%` 的 physical energy。

在 `N=160,Y=60,T=8`，component order为

`(Type-I log, Type-I correction, Type-II, low prime power)`. (21)

最大 physical channel的 eigenvector（忽略约 `10^(-3)` 的 phases与整体符号）约为

`(-.768,-.199,-.347,-.501)`,                      (22)

第二 channel约为

`(.423,-.800,-.423,-.037)`.                       (23)

第一 channel同时使用全部四类，第二 channel混合 Type-I correction与 Type-II；它们
都不是单独的 classical Type I或 Type II方向。这正说明需要 matrix-valued bilinear
estimate，而不是继续分别缩紧四个 scalar diagonals。

这些是 midpoint/truncated finite diagnostics。Eigenchannels依赖 `Y,T` 与 cutoff
family，尚未证明 uniform convergence、固定 rank-two model或式 (20)。数值只改变
下一步优先级，不是 RH evidence。

## 6. 下一步

1. 在 dyadic multiplicative rectangles上直接构造 `2 x 2` channel majorant；
2. 用 Type I mean-term channel与 Type II bilinear channel作 Schur/Feshbach组合，
   而不是四项独立 Young inequality；
3. 证明其余两个 cancellation channels的 operator tail `epsilon_k`可和；
4. 用定理 ABJ把 continuum quadrature与 prime truncation误差加入 Loewner enclosure；
5. 审计 eigenvectors在 `Y,T` 增长下是否稳定到由 convolution algebra决定的固定
   channel basis。
