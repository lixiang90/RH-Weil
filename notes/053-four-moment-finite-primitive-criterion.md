# Primitive homogeneous Gram 的四矩压缩与有限 RH 判据

文档 052 得到纯素数 primitive kernel `chi`，并证明其 full homogeneous
ratio profile 只有 factor-`8` 支撑。本笔记进一步证明两件事：

1. 每个 ratio chamber 的全部跨尺度 pair coupling 只有四个矩，故双和可
   精确化成一次 prefix scan；
2. 直接截断 `Lambda` 会产生线性大的边界伪能量，但截断
   `Lambda-1` 会精确消去该问题，并给出一个完全有限、无积分窗口的 RH
   等价判据。

因此经典 RH 被压成一个显式有限向量在四矩 semiseparable 正 Gram 中的
subpower Rayleigh bound。

## 1. 三个 ratio chambers

沿用

`K_infty(m,n)=M^(-1)k_chi(q)`,                     (1)

其中 `M=max(m,n)`, `q=min(m,n)/M`。令三个 chambers 为

`J_0=(1/8,1/4]`, `J_1=(1/4,1/2]`,
`J_2=(1/2,1]`.                                     (2)

### 定理 IM（four-term chamber formula）

在每个 `J_j` 上，

`k_chi(q)=a_j+b_j logq+(c_j+d_j logq)/q`,          (3)

其中

| `j` | `a_j` | `b_j` | `c_j` | `d_j` |
|---:|---:|---:|---:|---:|
| 0 | `16-24log2` | `-8` | `-2-3log2` | `-1` |
| 1 | `-56+48log2` | `28` | `16+15log2` | `8` |
| 2 | `76-18log2` | `-38` | `-50-18log2` | `-25` |

且 `k_chi(q)=0` 对 `q<=1/8`。

#### 证明

把命题 IK 的

`k_chi(q)=3k_phi(q)-k_phi(q/2)-2k_phi(2q)`

逐 chamber 代入式 (35)，收集 `1,logq,q^(-1),q^(-1)logq` 四项即得。
`□`

设 `m<n` 且 `q=m/n` 落在某个 chamber。式 (1)、(3) 变成

`K_infty(m,n)`

`=[a+b(logm-logn)]/n`

` +[c+d(logm-logn)]/m`.                            (4)

所以一个 chamber rectangle 上的 oriented cross matrix 至多 rank `4`；
自然的左右 features 分别为

`(1,logm,m^(-1),m^(-1)logm)`,                     (5)

`(n^(-1),n^(-1)logn,1,logn)`.                     (6)

## 2. 双和到四个 prefix moments

令 `(alpha_j,beta_j]` 依次为式 (2) 的三个区间。对任意有限复序列
`x_m`，定义

`S_0(t)=sum_(m<=t)x_m`,

`S_1(t)=sum_(m<=t)x_m logm`,

`S_(-1)(t)=sum_(m<=t)x_m/m`,

`S_(-1,1)(t)=sum_(m<=t)x_m logm/m`.                (7)

以 `Delta_j S(n)=S(beta_j n)-S(alpha_j n)` 记短乘法区间差。

### 定理 IN（exact four-moment semiseparable energy）

令 `A_chi=26-36log2`。有限 homogeneous Gram energy

`E(x)=sum_(m,n)x_m conjugate(x_n)K_infty(m,n)`     (8)

精确等于

`A_chi sum_n |x_n|^2/n`

`+2Re sum_n conjugate(x_n)sum_(j=0)^2 T_j(n)`,    (9)

其中

`T_j(n)=n^(-1){(a_j-b_j logn)Delta_jS_0(n)`

`                         +b_j Delta_jS_1(n)}`

`       +(c_j-d_j logn)Delta_jS_(-1)(n)`

`                         +d_j Delta_jS_(-1,1)(n)`. (10)

因此式 (8) 可在排序后以一次 prefix-moment scan 计算；它不需要枚举全部
prime pairs。

#### 证明

diagonal 为 `K_infty(n,n)=A_chi/n`。对 `m<n` 按三个 chambers 分组，
将式 (4) 对 `alpha_j n<m<=beta_j n` 求和，四项分别正是式 (7) 的四个
interval differences，得到式 (10)。最后加 Hermitian transpose，得到
式 (9)。`□`

这里的 finite rank 是精确代数性质，不是 low-rank approximation。

## 3. 四矩其实由一个 Chebyshev current 决定

对 zeta 取 `x_m=Lambda(m)-1`。令

`A(t)=sum_(m<=t)[Lambda(m)-1]=psi(t)-floor(t)`.     (11)

### 命题 IO（one-current reduction）

式 (7) 的四个 moments 都是 `A` 的 Stieltjes transforms：

`S_f(t)=A(t)f(t)-int_1^t A(v)f'(v)dv`,             (12)

其中 `f=1,logv,v^(-1),v^(-1)logv`。所以定理 IN 的全部 arithmetic
输入仅是同一个 centered Chebyshev current `A` 在三个相邻乘法 annuli
上的四个 endpoint/integral coordinates。

对未中心化信号还有更短的公式。若

`H_(-1)(t)=sum_(n<=t)Lambda(n)/n`，则

`u(L)=4psi(L/4)-8psi(L/2)+5psi(L)-psi(2L)`

` +L[-H_(-1)(L/4)+4H_(-1)(L/2)`

`                         -5H_(-1)(L)+2H_(-1)(2L)]`. (13)

等价地，若 `E(t)=psi(t)-t`，

`u(L)/L=int_(L/4)^(L/2)E(t)t^(-2)dt`

`       -3int_(L/2)^L E(t)t^(-2)dt`

`       +2int_L^(2L)E(t)t^(-2)dt`.                (14)

#### 证明

式 (12) 是 Abel/Stieltjes partial summation。将命题 IE 的三段 `chi`
分别求和得到式 (13)；再用
`H_(-1)(x)=psi(x)/x+int_1^x psi(t)t^(-2)dt`，主项相消后得到式 (14)。
`□`

式 (14) 也显示 primitive charge 是三个相邻 annuli 上系数 `(1,-3,2)`
的二阶尺度 coboundary。

## 4. 为什么必须先中心化

给定 `X`，若直接取有限向量

`x_n=Lambda(n)1_(X/4<n<=4X)`,                     (15)

其 full homogeneous energy 一般含 `asymp X` 的截断边界项。事实上，把
`Lambda(n)` 换成 continuum model `1`，令 `L=Xs`，Riemann sum 主项为

`X s int_(1/(4s))^(4/s)chi(r)dr`.                 (16)

它在 `1<=s<=2` 因 `int chi=0` 消失，却在外侧一组正测度的 `s` 上非零；
平方乘 `dL/L^2` 后正好是一个正的 constant times `X`。

所以不能用未中心化 full norm 粗暴支配目标 block：这会重新引入刚被
Tate 消元移除的边界 class。

## 5. 有限 centered homogeneous RH 判据

定义有限向量

`a_X(n)=[Lambda(n)-1]1_(X/4<n<=4X)`               (17)

以及完全有限的正数

`mathcal E_4(X)=sum_(m,n)a_X(m)a_X(n)K_infty(m,n)`. (18)

定理 IN 把它精确化成四 prefix moments 的单和。其 diagonal 为

`mathcal D_4(X)=A_chi sum_(X/4<n<=4X)`

`                              [Lambda(n)-1]^2/n`. (19)

### 定理 IP（finite four-moment criterion for RH）

以下条件等价：

1. RH；
2. `mathcal E_4(X)=X^(o(1))`；
3. `mathcal E_4(X)=O(log(X)^A)` 对某个固定 `A` 成立；
4. `mathcal E_4(X)/mathcal D_4(X)=X^(o(1))`。

而且

`mathcal D_4(X)=4(26-36log2)log2 logX+O(1)`.       (20)

RH 下可取无条件于本构造的经典上界

`mathcal E_4(X)=O(log(X)^4)`.                      (21)

#### 证明

先证 `2 => 1`。在 `X<=L<=2X`，`chi(n/L)` 的支撑保证所有出现的 `n`
都位于 `(X/4,4X]`。故

`u(L)=sum_n a_X(n)chi(n/L)+R_chi(L)`,              (22)

其中 `R_chi(L)=sum_n chi(n/L)`。由于 `int chi=0`、`Var(chi)=6`，BV
Riemann-sum inequality 给

`|R_chi(L)|<=6`.                                   (23)

因此

`sqrt(C_prim(X))<=sqrt(mathcal E_4(X))+6/sqrt(2X)`. (24)

式 (2) 给 `C_prim(X)=X^(o(1))`，定理 IG 推出 RH。

反之假设 RH。经典显式公式给

`A(t)=O(t^(1/2)log(t)^2)`.                         (25)

式 (17) 的 signal 仅支撑于 `X/8<L<16X`。对它作 Abel summation；
截断后的 `chi(n/L)` 总变差一致有界，式 (25) 给

`|sum_n a_X(n)chi(n/L)|=O(X^(1/2)log(X)^2)`.       (26)

在支撑区间以 `dL/L^2` 积分，得到式 (21)，从而 `1 => 3 => 2`。

最后，`sum_(t<n<=16t)Lambda(n)^2/n=4log2 logt+O(1)`，而 `-2Lambda+1`
只贡献 `O(1)`，给式 (20)。式 (20) 使条件 2 与 4 等价。`□`

定理 IP 比文档 IB 的 centered window Gram 更有限：没有 continuum、没有
外部积分窗口，也没有双素数枚举；数据只是约 `15X/4` 个显式 coefficients
和四个 prefix arrays。

## 6. Piecewise Mellin 结构的广义版本

### 定理 IQ（finite-moment primitive Weil structure）

设中心为 `c/2` 的 Gamma--Euler 数据满足定理 II，并且 primitive kernel
在有限个 multiplicative annuli 上是有限 Mellin-polynomial：

`chi(r)=sum_(lambda,k)b_(lambda,k)r^lambda(logr)^k`. (27)

假设：

- centered Euler coefficients 的 finite completion 与原 primitive block
  只差一致有界的 BV remainder；
- Rankin--Selberg diagonal 为 subpower；
- primitive Mellin multiplier 在开临界条带无零。

则其 full homogeneous kernel 在每个 ratio chamber 是有限秩
semiseparable kernel；所需 features 是有限多个

`n^lambda(logn)^k`.                                (28)

若实际 centered coefficient vector 的相应 finite homogeneous Gram 为
subpower，则全部 divisor 位于 `Re rho=c/2`。

#### 证明

两个式 (27) pieces 的乘积对尺度积分后仍是有限个
`q^mu(logq)^j`；有界支撑只产生有限多个 ratio chambers。因此每个 chamber
的 cross kernel 分离成有限多个式 (28) 的左右 tensor products。centered
completion、BV remainder 与定理 IP 相同地把 finite Gram bound 传给原
primitive block；定理 II/IG 的非消失与 GNS 论证给中心线。`□`

IQ 给出一类足够广的、真正可有限计算的代数结构：有限 Mellin pieces 取代
有限域 correspondence 的有限维矩阵元，prefix moments 取代 closed-point
trace coordinates，而临界 Gram tightness 扮演 Hodge--Riemann 正性。

## 7. 数值审计与证据边界

用定理 IN 的 prefix 公式计算 zeta centered vectors：

| `X` | `mathcal E_4(X)` | `mathcal D_4(X)` | Rayleigh quotient |
|---:|---:|---:|---:|
| 8   | 0.1515161 | 2.561300 | 0.0591559 |
| 16  | 0.0356864 | 4.334178 | 0.00823372 |
| 32  | 0.0256262 | 6.324025 | 0.00405220 |
| 64  | 0.1669540 | 8.507502 | 0.0196243 |
| 128 | 0.1973547 | 10.644432 | 0.0185407 |

实现同时用 generic complex finite vector 验证了四矩单和与直接双 Gram 在
高精度下相等。这些有限值只审计恒等式；定理 IP 明确说明其 subpower
渐近具有 RH 全部强度。

## 8. 下一步

剩余目标现为对式 (9) 中实际 `a_X=Lambda-1` 证明 subpower cancellation。
最具体的入口是：

1. 把三个 `Delta_j S` 用式 (12) 全部改写为 `A(t)=psi(t)-t`；
2. 检查系数表是否允许 Selberg symmetry formula 对四个 moments 联合完成
   平方，而不逐项取绝对值；
3. 对乘法 annuli 作 residue-class dispersion，目标只剩四个 endpoint
   coordinates，而非任意 pair kernel；
4. 寻找式 (9) 的离散 Hodge decomposition：diagonal 加 chamber cross
   是否能写成少量 endpoint squares 加正 local variance。

任何普通 operator norm 会再次损失 coefficient cancellation；必须针对
`Lambda-1` 的四个联合 moments 证明完整 quadratic form 的 subpower 界。
