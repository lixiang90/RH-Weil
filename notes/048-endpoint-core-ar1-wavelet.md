# Endpoint core 的 AR(1) 谱隙与连续 prime wavelet

文档 047 把每个 multiplicative block 的远程信息压到两个 endpoint
charges。相邻 blocks 共享 endpoint；合并以后，整个 core 实际只是一条
geometric grid charge 序列。本笔记证明它的 polarization 是一个显式
Brownian/AR(1) Toeplitz form，并在 zeta 临界参数处有与截断长度无关的
严格谱隙。合并后的 arithmetic charge 又是两个相邻 prime blocks 的局部
Mellin wavelet coefficient。

单个 dyadic grid 会 alias frequencies；对所有 grid offsets 平均后，得到
不漏零点的连续 core criterion。

## 1. Max kernel 的 Brownian transfer factorization

固定 `a>0,q>1`，令

`x_j=q^j`, `r=q^(-a)`, `C_(jk)=max(x_j,x_k)^(-a)`

`                         =r^(max(j,k))`.           (1)

### 命题 HF（prefix-square/Markov factorization）

对 `z_0,...,z_N` 和 prefix charges `Z_l=sum_(j=0)^l z_j`，

`sum_(j,k=0)^N C_(jk)z_j conjugate(z_k)`

`=sum_(l=0)^(N-1)(r^l-r^(l+1))|Z_l|^2`

`                         +r^N|Z_N|^2`.             (2)

所以 `C` 的 inverse/precision matrix 是 tridiagonal：令
`Delta_l=r^l-r^(l+1)`，则 off-diagonal entries 为
`-Delta_l^(-1)`，内部 diagonal 为
`Delta_(l-1)^(-1)+Delta_l^(-1)`，两端采用相应单边项。

#### 证明

写

`r^(max(j,k))=sum_(l>=max(j,k))(r^l-r^(l+1))`.      (3)

交换有限和；固定 `l<N` 收集 `j,k<=l` 得 `Delta_l|Z_l|^2`，所有
`l>=N` 的总系数为 `r^N`。precision 公式由 prefix difference 的
Cholesky factorization 立即得到。`□`

这就是一维 Green/max kernel 的 Markov 性；远程 coupling 已被 scalar
recurrence `Z_l=Z_(l-1)+z_l` 完全编码。

## 2. Endpoint core 是 AR(1) Toeplitz 减 scalar

沿用文档 047 的 profile。记

`R_0=(q-1)(q^(a+1)-1)/[a(a+1)]`,                  (4)

`R_1=R_(a,q)(1)`

`=2[q^(a+2)-(a+2)q+(a+1)]/[a(a+1)(a+2)]`,         (5)

`eta=1-R_1/R_0`, `rho=q^(-a/2)`.                  (6)

设 `T_N(rho)_(jk)=rho^|j-k|`，
`W_N=diag(1,rho,...,rho^N)`。

### 定理 HG（exact endpoint-core Toeplitz model）

把文档 047 的 homogeneous kernel 限制到 grid `{q^j}`。若
`p_0=2sigma q^(-c-2)R_0`、`a=c+2sigma`，则

`K_grid=p_0 W_N[T_N(rho)-eta I]W_N`.               (7)

其 Toeplitz symbol 为

`s_(rho,eta)(theta)`

`=(1-rho^2)/(1-2rho cos(theta)+rho^2)-eta`,         (8)

故所有有限截面满足

`p_0 m_(a,q)||W_Nz||^2<=z*K_grid z`

`<=p_0 M_(a,q)||W_Nz||^2`,                         (9)

其中

`m_(a,q)=(1-rho)/(1+rho)-eta>=0`,                  (10)

`M_(a,q)=(1+rho)/(1-rho)-eta`.                     (11)

#### 证明

不同 grid points 的 ratio 至多 `q^(-1)`，所以定理 GZ 的 profile 等于
`R_0`；diagonal profile 为 `R_1=R_0(1-eta)`。又

`rho^j rho^k rho^|j-k|=r^(max(j,k))`,              (12)

给式 (7)。对任意 polynomial `P(e^(itheta))=sum z_j e^(ijtheta)`，
Toeplitz quadratic form 是 `s` 对 `|P|^2` 的积分；Poisson kernel 的最小
值在 `theta=pi`、最大值在 `0`，得到式 (9)–(11)。`m>=0` 也可直接由
`K_grid>=0` 推出。`□`

## 3. Zeta 临界 core 的严格统一谱隙

取 `c=a=1,q=2`，并把 kernel 除以消失的共同因子 `2sigma` 后令
`sigma downarrow0`。此时

`R_0=3/2`, `R_1=4/3`, `eta=1/9`,

`rho=2^(-1/2)`, `p_crit=2^(-3)R_0=3/16`.           (13)

### 定理 HH（uniform critical endpoint-core coercivity）

对任意 `N` 与 grid charges `z_0,...,z_N`，临界 core form 满足

`Q_core,N(z)>=p_crit m_crit sum_(j=0)^N2^(-j)|z_j|^2`, (14)

其中

`m_crit=3-2sqrt(2)-1/9=26/9-2sqrt(2)>0`.           (15)

上界同样统一，其常数为

`p_crit[3+2sqrt(2)-1/9]`.                           (16)

#### 证明

把式 (13) 代入定理 HG。Poisson symbol 的底为
`(1-rho)/(1+rho)=3-2sqrt2`，减去 `eta=1/9` 仍严格为正。`□`

所以 endpoint core 内部绝不是临界负方向；它有显式 uniform Hodge gap。
剩余困难只能来自实际 core charges 的总 norm，以及它们与 centered
nearest-neighbor remainder 的 Schur coupling。

## 4. 合并 core charge 的局部 prime 公式

现在固定 zeta critical moments `a=1,q=2`。令

`E(x)=psi(x)-x`,

`H(L)=int_L^(2L)E(x)x^(-2)dx`, `L>=1`.             (17)

对 block `(L,2L]`，记

`beta(L)=int_(L,2L]dnu=E(2L)-E(L)`,

`alpha(L)=int_(L,2L]x^(-1)dnu`.                    (18)

文档 047 的两个 endpoint weights 为

`A(L)=2L alpha(L)-beta(L)`,

`B(L)=2beta(L)-2L alpha(L)`.                        (19)

### 命题 HI（merged endpoint charge is a local Mellin wavelet）

在 interior endpoint `L=2^j,j>=1`，相邻 blocks 合并后的 charge 为

`z(L)=B(L/2)+A(L)=L[2H(L)-H(L/2)]`.                (20)

它只使用 `[L/2,2L]` 的 prime discrepancy。更明确地，整数 `L` 时

`H(L)=psi(L)/(2L)`

` +sum_(L<n<=2L)Lambda(n)[1/n-1/(2L)]-log2`.       (21)

等价地，

`z(L)=int_(1/2)^2 w(y)E(Ly)dy`,                    (22)

其中

`w(y)=-y^(-2)` on `[1/2,1]`,

`w(y)=2y^(-2)` on `[1,2]`.                         (23)

对 divisor mode `E(x)=x^rho`，

`z(L)=W(rho)L^rho`,

`W(rho)=[2^rho+2^(1-rho)-3]/(rho-1)`               (24)

`=[2^(rho-1)-1][2-2^(1-rho)]/(rho-1)`.             (25)

`W` 在开条带 `0<Re rho<1` 无零。

#### 证明

Stieltjes 分部积分给

`alpha(L)=E(2L)/(2L)-E(L)/L+H(L)`.                 (26)

代入式 (19)，得

`A(L)=-E(L)+2LH(L)`,

`B(L)=E(2L)-2LH(L)`.                               (27)

相邻 endpoint 的 `E(L)` 项相消，证明式 (20)。交换 `psi` 的 finite sum
与积分得到式 (21)；`x=Ly` 给式 (22)–(23)。对 `x^rho` 积分并化简得到
式 (24)–(25)。令 `x=2^(rho-1)`，numerator 为
`(x-1)(2x-1)/x`；其零点分别在 `Re rho=1` 与 `Re rho=0`。在 `rho=1`
分母消去实零点，结论仍成立。`□`

## 5. 所有 shifted grids 消除 phase alias

单看 `L=2^j` 会把 ordinates modulo `2pi/log2` 混合。定义连续信号

`y(t)=e^(-t/2)z(e^t)`, `t>=log2`.                  (28)

对 `tau in[0,log2)`，shifted grid 是 `L_(tau,j)=e^tau2^j`。有精确分解

`int_(log2)^infinity |y(t)|^2e^(-2sigma t)dt`

`=int_0^(log2)sum_(j>=1)`

` e^(-(1+2sigma)(tau+jlog2))`

` |z(e^tau2^j)|^2dtau`.                            (29)

### 定理 HJ（shift-averaged core energy is a complete detector）

令

`mathcal W_sigma=2sigma int_(log2)^infinity`

`                    |y(t)|^2e^(-2sigma t)dt`.     (30)

则下列条件等价：

1. RH 成立；
2. `mathcal W_sigma<infinity` 对每个 `sigma>0`；
3. `sup_(0<sigma<=1)mathcal W_sigma<infinity`。

在每个 fixed `tau` grid 上，定理 HH 的同一个 gap 控制式 (29) 中的
weighted charge norm；对 `tau` 积分不会损失该 gap。

#### 证明

由式 (22)，`z(e^t)` 是 normalized prime error 的 compactly supported
log-convolution。其 Laplace/Mellin multiplier 是式 (24)，在临界条带内
无零。若条件 2 成立，加权 Cauchy--Schwarz 使其 Laplace transform 在
`Re s>0` 解析；任何 `Re rho>1/2` 的零点都会在
`s=rho-1/2` 产生未被 `W(rho)` 消去的 pole，矛盾。函数方程排除左侧。

RH 下 divisor expansion 的 coefficients 因额外的 `1/rho` 来自 `E`
而平方可和，故 `y` 有有限 Besicovitch mean square，得到条件 3。式 (29)
只是把连续 `t` 唯一写成 `tau+jlog2`，并逐 grid 应用定理 HH。`□`

HJ 避免了一个常见漏洞：单个离散 grid 的 multiplier 虽在开条带无零，
仍可能发生不同 ordinates 的 sampling alias；连续 offset average 不会。

## 6. Core-only 连续 Weil 结构

### 定理 HK（prime-wavelet core generates the center-line structure）

若式 (30) 的 finite shifted-grid Grams 在 `sigma downarrow0` tight，并且
一阶 `t` 导数也满足相同 Sobolev tightness，则：

1. 定理 GV 的 GNS construction 直接从 local charges `z(e^t)` 产生强连续
   酉群 `U_t=e^(itA)`；
2. `Theta=1/2+iA` 满足 `Theta*=1-Theta`；
3. zeta 的全部非平凡零点位于中心线；RH 下 `A` 的谱为 ordinates。

因此构造连续 Weil 结构不需要保留每块完整 centered remainder；local
prime-wavelet core 本身已经是 complete spectral detector。remainder 的
价值转而在于尝试用 local variance/large sieve **证明** core tightness，
而不是保证逻辑完备性。

#### 证明

HJ 给中心线结论。Sobolev Gram 到强连续 GNS、selfadjoint generator 与
adjoint identity 完全按定理 GV；式 (24) 的非消失保证所有 divisor modes
可见。`□`

## 7. Gamma--Euler 推广

### 定理 HL（general shifted-grid wavelet core theorem）

对中心 `c/2` 的 Gamma--Euler discrepancy，取任意 `q>1` 并在临界
`a=c` 的 geometric blocks 上抽取文档 HC 的 endpoint moments。合并共享
endpoints 后得到 local compactly supported Mellin-wavelet signal。若其
Mellin multiplier 在标准非平凡条带无零，则所有 shifted-grid Abel
energies 的临界 tightness 迫使 divisor 位于 `Re s=c/2`；Sobolev 版本产生
`Theta=c/2+iA`、`Theta*=c-Theta`。

zeta 的 `c=1,q=2` multiplier 已由式 (24)–(25) 验证无零。一般数据可选
一个或有限多个 `q`，避开离散 multiplier zeros。

#### 证明

Brownian/Toeplitz core 只依赖 `a,q`，命题 HF–定理 HG 原封不动。中心线
论证是定理 HJ 的 Mellin pole argument；连续 offsets 消除 sampling alias。
`□`

## 8. 存在性审计

对 zeta，已经无条件构造：

- 每个 shifted finite grid 的 local prime charges `z(L)`；
- critical endpoint-core 的统一严格 Hodge gap (15)；
- 所有 finite Gram/Sobolev matrices 的正性；
- `sigma>=1/2` 的 infinite weighted energies。

仍未证明的是 `sigma downarrow0` 的 shift-averaged core tightness；定理 HJ
说明它与 RH 等价。新的算术目标是直接证明 uniform Abel estimate

`sup_(0<sigma<=1) 2sigma int_0^(log2)sum_(j>=1)`

` e^(-(1+2sigma)(tau+jlog2))|z(e^tau2^j)|^2dtau`

`<infinity`.                                        (31)

这正是式 (30) 的 shifted-grid 版本。每个 `z(L)` 只涉及 `[L/2,2L]`，且 boundary
Chebyshev values 已在式 (20) 中精确相消；这比原始全局 current norm 更适合
Selberg integral、dispersion 或相邻-block large sieve。

### 有限数值审计

实际 zeta prime data 给出：

| `L` | `z(L)` | `z(L)/sqrt(L)` |
|---:|---:|---:|
| 2 | -0.32694308 | -0.23118367 |
| 4 | -0.10338344 | -0.05169172 |
| 8 | -0.00399210 | -0.00141142 |
| 16 | -0.01744395 | -0.00436099 |
| 32 | -0.00460264 | -0.00081364 |
| 64 | 0.04878754 | 0.00609844 |
| 128 | -0.24187210 | -0.02137868 |

临界 Toeplitz form 的解析 infinite-volume 底为 `0.0604617641`。截断长度
`N=4,8,16` 的归一化最低本征值分别为

`0.08626628, 0.06675947, 0.06204227`,               (32)

从上方逼近该底。脚本独立核对了 prefix-square、Toeplitz 共轭和式 (21) 的
逐区间积分。这些有限数据不控制式 (31)，不是 RH 的数值证据。
