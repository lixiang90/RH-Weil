# Constrained Nyman Hodge capacity 与 jet-Feshbach 单调性

文档 086 构造了 minimum-metric mean-zero correction，但尚未把 metric 与
原始 Nyman residual 的交叉项同时纳入。本节使用真实 fractional-part Hilbert
Gram，解出完整的 affine constrained approximation problem。新增一个 jet
direction 时，capacity 增量和 residual energy 降幅都成为显式 Feshbach
平方；这给出了一个可迭代、无条件有限存在的 Hodge filtration。

## 1. Actual correction Gram

令

`rho_n(x)={1/(nx)}`,  `chi=1_(0,1)`,                 (1)

并定义 exact Nyman data

`G_(mn)=<rho_m,rho_n>`,

`z_n=<rho_n,chi>=(log n+1-gamma)/n`.                 (2)

取一个 base coefficient vector `b in C^N`，写

`f_0=chi+sum_n b_n rho_n`,                            (3)

`E_0=||f_0||^2=1+2Re(z^*b)+b^*Gb`.                  (4)

再取 endpoint-preserving correction coefficient columns

`Q=(q_1,...,q_R) in C^(N times R)`,                   (5)

并令 `g_j=sum_n q_j(n)rho_n`。定义

`W=Q^*GQ`,                                            (6)

`h=Q^*(z+Gb)`,                                        (7)

`D=Q^*1_N`,  `t=-2-1_N^*b`.                          (8)

约束 `D^*alpha=t` 恰好使 corrected coefficients

`b+Qalpha`                                            (9)

的周期 boundary mean `1+(1/2)sum coefficients` 为零。

### 定理 QP（unconditional actual Nyman correction structure）

对每个固定 `N`，`G>0`。若 `Q` full column rank，则 `W>0`，并且

`||f_0+sum_j alpha_jg_j||^2`

` =E_0+2Re(h^*alpha)+alpha^*Walpha`.                 (10)

在 critical Mellin line `s=1/2+it` 上，若

`Q_j(s)=sum_n q_j(n)n^(-s)`,                          (11)

则

`W_(jk)=(1/(2pi))int_R |zeta(s)|^2 Q_j(s)`

`                    *conjugate(Q_k(s))dt/|s|^2`.    (12)

因此式 (6) 是真实而非试验性的 positive Hodge Gram，所有 finite data
无条件存在。

#### 证明

若 `sum c_n rho_n=0`，其 Mellin transform 在 `0<Re(s)<1` 是

`-zeta(s)sum c_n n^(-s)/s`.                           (13)

它恒等为零迫使 finite Dirichlet polynomial 恒等为零，从而 `c_n=0`；所以
`G>0`。式 (10) 直接展开平方范数。文档 081 的 Mellin identity

`M rho_n(s)=-zeta(s)n^(-s)/s`                        (14)

与 Plancherel 给式 (12)。`□`

## 2. Complete affine constrained projection

定义 response capacity

`C=D^*W^(-1)D`.                                      (15)

### 定理 QQ（exact constrained Nyman projection）

若 `D!=0`，则式 (10) 在约束 `D^*alpha=t` 下的唯一极小点是

`alpha_*=-W^(-1)h`

` +(t+D^*W^(-1)h)W^(-1)D/C`.                        (16)

其最小能量为

`E_* =E_0-h^*W^(-1)h`

`      +|t+D^*W^(-1)h|^2/C`.                        (17)

#### 证明

先完成平方：unconstrained minimizer 是 `-W^(-1)h`，unconstrained energy
是 `E_0-h^*W^(-1)h`。constraint 在此点的 residual 为
`t+D^*W^(-1)h`。在 `W`-inner product 中，用文档 086 定理 QL 把这个
residual 投影到 response representer `W^(-1)D`，得到式 (16)--(17)。`□`

式 (17) 有两个独立的 Schur terms：第一项衡量 correction span 对原始
residual 的 ordinary approximation；第二项是强制 boundary mean-zero 的
额外代价。只研究 capacity 而忽略 coupling `h` 仍不够。

## 3. Capacity 的一阶 Feshbach 增量

加入一个新 direction，把数据写成

`W_+=[[W,b],[b^*,c]]`,  `D_+=(D,d)^T`.               (18)

令

`sigma=c-b^*W^(-1)b>0`,                              (19)

`d_eff=d-b^*W^(-1)D`.                                (20)

### 定理 QR（capacity monotonicity with exact gain）

`C_+:=D_+^*W_+^(-1)D_+`

` =C+|d_eff|^2/sigma>=C`.                            (21)

#### 证明

对 block matrix `W_+` 使用 Schur inverse formula。由式 (19) 的正性，
新增项非负。`□`

`d_eff` 是新方向在先消去旧 correction space 后留下的 boundary response，
`sigma` 是其正交 Hodge norm。只有 `d_eff!=0` 的方向才严格增加 capacity。

## 4. Constrained residual 的精确边际收益

把 coupling 同样扩张为 `h_+=(h,e)^T`，并定义

`e_eff=e-b^*W^(-1)h`,                                (22)

`r=t+D^*W^(-1)h`.                                    (23)

### 定理 QS（jet-Feshbach energy decrement）

令 `E_*` 与 `E_(+,*)` 分别为扩张前后的 constrained minima，则

`E_*-E_(+,*)`

` =|C e_eff-d_eff r|^2`

`   /[C(C sigma+|d_eff|^2)]>=0`.                     (24)

因此 nested jet spaces 的 exact mean-zero Nyman energies 单调不增。新增
方向没有收益当且仅当

`C e_eff=d_eff r`.                                   (25)

#### 证明

Schur elimination 给 enlarged unconstrained energy

`E_uc,+ =E_uc-|e_eff|^2/sigma`,                       (26)

enlarged capacity 是式 (21)，而 enlarged constraint residual 是

`r_+=r+conjugate(d_eff)e_eff/sigma`.                  (27)

把这些量代入式 (17)，通分并完成平方，得到式 (24)。`□`

式 (24) 比一般的“子空间扩大使距离下降”更精确：它把每个 arithmetic jet
的实际贡献分解成 Schur gap、独立 boundary response 与 residual coupling。

## 5. Polynomial jet filtration 的有限穷尽性

回到 Möbius directions

`q_j(n)=mu(n)u_n^j(1-u_n)`,  `j=1,...,R`.             (28)

令

`A_N={n:2<=n<N, mu(n)!=0}`,  `K_N=|A_N|`.             (29)

### 定理 QT（finite Vandermonde exhaustion）

取 `R=K_N` 时，式 (28) 的 columns 张成所有满足以下条件的 coefficient
perturbations：

1. 支撑包含于 `A_N`；
2. 在 `n=1,N` 为零。

因此定理 QQ 在 `R=K_N` 精确给出整个 endpoint-preserving Möbius-support
subspace 内的 mean-zero Nyman optimum。

#### 证明

把 rows 限制到 `A_N`。除去每行非零因子

`mu(n)u_n(1-u_n)`,                                   (30)

剩余 matrix 是 `u_n^(j-1)` 的 square Vandermonde matrix。不同 integers
给不同 `u_n`，故 determinant 非零。`□`

这证明 finite existence 并非 degree 不足的问题：允许 degree 随 `N` 增长后，
reciprocal-support correction space 可被完全穷尽。开放性在于 constrained
minimum 是否以所需速率趋零，而不是 finite linear system 是否可解。

## 6. Abstract constrained Hodge structure theorem

前述证明不依赖 fractional-part functions 的特殊形式。令 `T:V->H` 是 finite
synthesis map，`W=T^*T>0`；令 `f_0 in H`，`h=T^*f_0`；再令
`ell in V^*` 是一个 boundary/Tate functional。

### 定理 QU（affine Hodge projection principle）

对任意 `ell(v)=t`：

1. 唯一 minimum-energy correction 由定理 QQ 的 Riesz projection 给出；
2. obstruction scalar 是 positive capacity `ell W^(-1)ell^*`；
3. 对 nested synthesis spaces，capacity 按定理 QR 单调增加；
4. constrained energy 按定理 QS 单调下降，且每步降幅是显式正平方；
5. 所有结论在 direct sums、matrix-valued coefficients 及任意 reciprocal
   Euler algebra 的 finite jet spaces 中保持成立。

#### 证明

前三项是定理 QQ--QS 的 basis-free 重述。direct sum 与 matrix-valued 情形只
把 scalars 换成 compatible blocks；正 Schur complement 证明逐字不变。`□`

这是从 Weil/Hodge 机制抽离出的又一个普适部件：polarization `W` 把一个
boundary functional 转成正 capacity，而 Feshbach filtration 把结构存在性
化为一列单调 finite certificates。

## 7. RH 存在性审计

令 `E_(N,R)^mz` 表示式 (17) 对 degree-`R` Möbius jet space 的值。

### 结论 QV（what the exact Gram does and does not prove）

对每个固定 `N,R`，actual Gram、capacity、canonical coefficients、energy 与
每步 Feshbach gain 均无条件存在且可由 primes-free fractional-part Hilbert
geometry 定义。若存在 cofinal `(N,R(N))` 使

`E_(N,R(N))^mz ->0`,                                 (31)

则 Nyman--Beurling criterion 推出 RH。

但 RH 本身是否保证存在 exact mean-zero approximants 尚未在这里证明；因此
式 (31) 当前是充分判据，不宣称等价。即使取定理 QT 的 full
Möbius-support space，也仍是 general Nyman coefficient space 的真子空间。

下一步的非循环目标有两种等价表述：

- 证明式 (24) 的正 gains 沿 jet filtration 累积到使式 (31) 成立；或
- 将 Gram 按文档 085 的 local / parabolic Farey / far regions 分块，证明
  optimal constrained vector 的 parabolic leakage 足够小。

任何假设 `W_N` 有 uniform spectral gap 的做法仍被文档 082 的 log-lattice
collision no-go 排除；可行量必须是 target/response-aligned Schur expressions，
而不是粗 `||W_N^(-1)||`。

## 8. 计算实现

`scripts/qw_matrix.py` 新增：

- `constrained_hodge_projection`；
- `nested_response_capacity_update`；
- `nested_constrained_hodge_update`。

回归测试用独立 direct block inversion 检查 capacity increment，用直接二次型
检查 constrained minimum，并核对式 (24) 的 energy decrement 与扩大后的
三维优化结果完全一致。
