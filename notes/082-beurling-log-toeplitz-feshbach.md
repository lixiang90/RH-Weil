# Nyman--Beurling log-Toeplitz Gram、whitening 与 Feshbach 障碍

文档 081 把 RH 化为 finite positive Schur distances `d_N->0`。本节分析这些
Gram matrices 的精确谱结构。主要结论是：归一化 features 构成非均匀
log-lattice 上的 stationary positive kernel；Gram 的最小特征值无条件趋零，
所以任何依赖 uniform coercivity 的证明路线必然失败。真正要控制的是 target
对低谱方向的对齐，即 Schur/Feshbach margin。

## 1. Equal-norm dilation orbit

仍令

`r_n(x)={1/(nx)}`,  `phi_n=sqrt(n)r_n`.                 (1)

由缩放可见 `phi_n` 是 `phi_1` 的 unitary dilation orbit 在参数
`log n` 上的取样。定义

`w(t)=|zeta(1/2+it)|^2/(1/4+t^2)`,                     (2)

`kappa(u)=(1/(2pi))int_R w(t)e^(itu)dt`.               (3)

### 定理 PH（multiplicative Toeplitz Gram）

`w in L^1(R)`，`kappa` 是连续 positive-definite function，且

`<phi_m,phi_n>=kappa(log(m/n))`.                        (4)

特别地 normalized Gram

`K_N=(kappa(log(m/n)))_(m,n<=N)`                       (5)

是 log-lattice `{log n}` 上的 Toeplitz-type restriction，所有 diagonal
entries 相同。

#### 证明

文档 081 的 Mellin identity 给临界线上

`M phi_n(1/2+it)=-n^(-it)zeta(1/2+it)/(1/2+it)`.       (6)

Mellin Plancherel 立即给式 (4)。`r_1 in L^2` 说明 `int w<infinity`；
也可由 zeta 的 classical second moment 加 `t^(-2)` weight 看出。Fourier
transform of an `L^1` nonnegative function 连续且 positive definite。`□`

这里的 “Toeplitz” 指 kernel 只依赖 log-ratio，而非 integer difference；
节点间距 `log(n+1)-log n` 趋零，所以它是越来越稠密的非均匀取样。

## 2. 对角与 target coupling 的闭式

### 定理 PI（two exact constants）

对每个 `n>=1`，

`||r_n||_2^2=[log(2pi)-gamma]/n`,                      (7)

`<r_n,chi>=[log n+1-gamma]/n`.                         (8)

因此

`kappa(0)=log(2pi)-gamma`,                             (9)

`g_n:=<phi_n,chi>=[log n+1-gamma]/sqrt(n)`.            (10)

#### 证明

变量替换 `y=1/(nx)` 给

`||r_n||^2=(1/n)int_0^infinity {y}^2 y^(-2)dy`.        (11)

在 intervals `[k,k+1]` 分段积分并用 Stirling formula，右侧常数为
`log(2pi)-gamma`。同理

`<r_n,chi>=(1/n)int_(1/n)^infinity {y}y^(-2)dy`.       (12)

`[1/n,1]` 部分为 `log n`；而

`sum_(k>=1)int_k^(k+1)(y-k)y^(-2)dy`

` =lim_K[log(K+1)-H_(K+1)+1]=1-gamma`.                (13)

合并即得。`□`

所以无需数值 quadrature 即可精确得到 Gram diagonal 和 target vector。

## 3. Whitening 不改变 Hodge distance

令原始 feature Gram 为 `G_N`、coupling 为 `h_N`，并令

`D_N=diag(n^(-1/2))`.                                  (14)

由 `r_n=phi_n/sqrt(n)`，

`G_N=D_N K_N D_N`,  `h_N=D_N g_N`.                     (15)

### 定理 PJ（whitened normal equations）

若 matrices 可逆，则

`d_N^2=1-h_N^*G_N^(-1)h_N`

`     =1-g_N^*K_N^(-1)g_N`.                            (16)

原 coefficients `c` 的 normal equation `G_Nc=h_N` 等价于

`K_N z=g_N`,  `z=D_N c`.                               (17)

#### 证明

把式 (15) 及 `G_N^(-1)=D_N^(-1)K_N^(-1)D_N^(-1)` 代入。
`□`

这移除了 `||r_n||~n^(-1/2)` 的平凡尺度衰减；剩下的 conditioning 完全来自
log-lattice correlations 与 spectral density `w`。

## 4. Exact Feshbach formula for target distance

把 index set 分成 core `I` 与 complement `J`：

`K=[[A,B],[B^*,C]]`,  `g=(a,b)^T`.                     (18)

### 定理 PK（Gram--Feshbach distance）

若 `C>0`，定义

`A_eff=A-BC^(-1)B^*`,

`a_eff=a-BC^(-1)b`,

`q_eff=1-b^*C^(-1)b`.                                 (19)

则

`d_N^2=q_eff-a_eff^*A_eff^(-1)a_eff`.                  (20)

#### 证明

最小化 quadratic residual

`R(z)=1-2Re(g^*z)+z^*Kz`.                             (21)

对 complement variable 先完成平方，得到式 (19) 的 effective quadratic；
再对 core variable 最小化即得式 (20)。`□`

这正是文档 024 的 residual--Feshbach 方法在 Nyman--Beurling Hodge block 上
的精确版本。要证明 RH，必须随 `N` 同时控制 `C^(-1)`、renormalized target
`a_eff` 和 margin `q_eff`；仅控制一个 matrix norm 不够。

## 5. Uniform Gram gap 无条件不可能

### 定理 PL（log-lattice collision no-go）

`lambda_min(K_N)->0`。更精确地，

`lambda_min(K_N)`

` <=kappa(0)-Re kappa(log(N/(N-1))) ->0`.              (22)

#### 证明

在 coordinates `N-1,N` 取 unit vector `(1,-1)/sqrt(2)`，其 Rayleigh
quotient 是式 (22) 右侧。`log(N/(N-1))->0`，而 `kappa` 连续。`□`

因此不能通过证明 `K_N>=delta I`、`delta>0` uniform 来推出 RH；该命题甚至
与无条件 dilation geometry 冲突。用 `||K_N^(-1)||` 粗估 Schur term也会
丢失全部 target alignment。

注意此 no-go 与 zeta zeros 无关：越来越近的 dilation nodes 已足够产生小
奇值。另一方面，`w(t)` 在每个 critical-line zero 还会形成额外的低权
frequency well。故允许的中心零点本身也反对 global coercivity。

## 6. Boundary low spectrum 与 off-line cokernel 是两种障碍

### 定理 PM（two-obstruction separation）

1. critical-line zero `1/2+i gamma` 使 boundary density `w(gamma)=0`；它影响
   Gram conditioning，但与 RH 相容；
2. off-line zero `rho` 不必使 boundary density 在 real frequency 上为零，
   而是通过 analytic point evaluation 消灭整个 synthesis range、却不消灭
   target，从而使 `d_infinity>0`；
3. 因此 finite smallest singular values 不能区分“允许的 critical radical”与
   “错误的 off-line cokernel”；distinguished Schur distance 可以。

#### 证明

1 来自式 (2)。2 是文档 081 定理 PA 的 evaluation obstruction。3 由定理
PL 说明最小奇值无条件趋零，而 Nyman--Beurling theorem 说明只有 target
distance 的极限才等价于 RH。`□`

这与 Weil/Hodge 语言完全一致：primitive intersection form 可以有 growing
near-radical；所需结论不是排除 radical，而是证明 arithmetic target 落进正确
的 radical closure，且没有错误-weight cokernel。

## 7. Sharp rate barrier from critical zeros

Burnol 对 Nyman--Beurling distance 证明了 lower bound

`liminf_(N->infinity) d_N^2 log N`

` >=sum_(Re(rho)=1/2) m_rho^2/|rho|^2`.                (23)

### 结论 PN（rate calibration）

1. 即使 RH 成立，`d_N^2` 也不能比 `1/log N` 更快地趋零；预期的 sharp
   scale 正是 `1/log N`，不能期待 polynomial decay；
2. 若 RH 且 critical zeros simple，则右侧为

   `C=2+gamma-log(4pi)`;                               (24)

3. Bettin--Conrey--Farmer 在 RH 加 reciprocal derivative moment hypothesis
   下构造达到这一 constant 的 mollifier；
4. 因而一个可行的无条件上界目标应是 `d_N^2<=C'/log N+o(1/log N)`，而非
   uniform Gram gap 或指数 residual。

Burnol bound 由 critical zero evaluation/jet vectors 的 almost-orthogonality
给出；multiplicity 出现为 `m_rho^2`，与文档 076--077 的 matrix/tracial
multiplicity 审计吻合。

## 8. 对 RH 存在性路线的更新

现在可以排除两条看似自然但错误的策略：

- 证明 normalized Beurling Gram 有 uniform spectral gap；
- 用 coefficientwise Möbius cancellation 加最小特征值粗界控制 inverse。

剩下的正确 finite target 是：构造 arithmetic trial vector `z_N`，证明

`R_N(z_N)=1-2Re(g_N^*z_N)+z_N^*K_Nz_N ->0`,           (25)

最好达到 `O(1/log N)`；或对 resonance core 使用定理 PK，并证明 complement
elimination 后的 effective Schur margin 趋零。任何证明都必须保留 `g_N` 与
low-spectrum eigenvectors 的相位/对齐信息。

这比“估计 Gram condition number”严格得多，也更接近 Weil 猜想证明中的
Hodge--Riemann target positivity：不是 form everywhere coercive，而是特定
primitive/cohomological class 的 norm 被正确控制。

## 9. 计算实现

`scripts/qw_matrix.py` 新增：

- `beurling_target_coupling`；
- `beurling_feature_norm_squared`；
- `normalize_beurling_gram_data`；
- `positive_gram_feshbach_distance`。

回归测试核对 whitening 前后 Schur distance 不变、任意 core/complement
Feshbach elimination 与直接 distance 相同，并核对式 (7)--(8) 的 constants。
采样 Gram 仍只用于有限线性代数回归，不代替 continuous kernel 的严格公式。
