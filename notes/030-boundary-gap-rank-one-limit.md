# 加权素数端点间隙、秩一极限与 prime--pole 相消

文档 016 发现 prime degree 势与极点锚在端点都有 `lambda` 量级，因而
不能逐项控制。本笔记证明更精确的事实：固定宽度的左右边界层上，靠近
截断端点 `lambda^2` 的素数幂相关在主阶收敛到一个有向秩一通道；`0,1`
两个极点给出的正是同一通道的 Hermitian 化。由于二者在 Weil form 中
符号相反，全部
`lambda` 主阶严格相消。

这给出一个无条件的边界 near-radical 机制，但不是 RH 的证明：结论只把
Weil form 除以 `lambda` 后送到零，并不控制未正规化余项的符号或大小。

## 1. 加权素数端点间隙的指数极限

令

`x=lambda^2`, `L=log x=2log lambda`,

`P(x)=sum_(n<=x) Lambda(n)/sqrt(n)`,                   (1)

并把每个素数幂放在距右端点的对数间隙

`v_n=log(x/n)=L-log n`。                              (2)

定义概率测度

`mu_x=P(x)^(-1) sum_(n<=x) Lambda(n)/sqrt(n) delta_(v_n)`. (3)

### 定理 DR（weighted prime-gap exponential limit）

当 `x->infinity` 时，`mu_x` 弱收敛到 `[0,infinity)` 上的概率测度

`dmu(v)=(1/2)e^(-v/2)dv`.                             (4)

即对每个 `g in C_c([0,infinity))`，

`int g dmu_x -> (1/2)int_0^infinity g(v)e^(-v/2)dv`. (5)

#### 证明

记 `psi(u)=sum_(n<=u)Lambda(n)`。素数定理给出 `psi(u)=u+o(u)`。
对支撑包含在 `[0,B]` 的 `C^1` 函数，Stieltjes 分部积分（或先对阶梯
函数证明再一致逼近）给出

`sum_(n<=x) Lambda(n)n^(-1/2)g(log(x/n))`

`=int_1^x u^(-1/2)g(log(x/u))dpsi(u)`

`=sqrt(x)int_0^B e^(-v/2)g(v)dv+o(sqrt(x))`.          (6)

这里在固定乘法窗口 `[xe^(-B),x]` 上，`psi(u)=u+o(x)` 一致成立；边界项
也由同一估计控制。连续紧支撑函数再由 `C^1` 函数一致逼近得到式 (6)。
取 `g=1` 的截断逼近，或直接对式 (1) 分部求和，得到

`P(x)=2sqrt(x)+o(sqrt(x))`.                           (7)

式 (6) 除以式 (7) 即为式 (5)。尾部紧性可由
`mu_x([B,infinity))<=P(xe^(-B))/P(x)` 与式 (7) 得到，其上极限不超过
`e^(-B/2)`，故局部结论升级为概率测度的弱收敛。`□`

这个极限不是通常的相邻素数间隙分布；它是显式公式权重
`Lambda(n)/sqrt(n)` 在移动乘法端点下的确定性 PNT 极限。

## 2. 左右边界相关的秩一极限

固定 `B>0` 与 `f_L,f_R in C_c^1((0,B))`。在
`[-ell,ell]`, `ell=log lambda=L/2` 上定义

`f_lambda(-ell+u)=f_L(u)`,

`f_lambda(ell-z)=f_R(z)`,                             (8)

其余位置为零。定义两个带权边界矩

`L_0=int_0^B f_L(u)e^(-u/2)du`,

`R_0=int_0^B f_R(z)e^(-z/2)dz`.                      (9)

对 `a>=0` 令零延拓平移相关为

`C_a(f)=int_(-ell)^(ell-a) conjugate(f(y))f(y+a)dy`. (10)

### 命题 DS（boundary prime correlation has a rank-one limit）

有

`P(x)^(-1) sum_(n<=x) Lambda(n)/sqrt(n) C_(log n)(f_lambda)`

`-> (1/2) conjugate(L_0)R_0`.                         (11)

因此文档 016 的 prime correlation form

`W_P,lambda(f,f)=2 sum_(n<=x) Lambda(n)/sqrt(n)`

`                         Re C_(log n)(f)`            (12)

满足

`lambda^(-1)W_P,lambda(f_lambda,f_lambda)`

`->2Re(conjugate(L_0)R_0)`.                          (13)

#### 证明

写 `v=L-log n`。当 `v<=2B` 且 `L>3B` 时，平移 `log n=L-v`
只能把左边界层送到右边界层，并且直接换元 `y=-ell+u` 得

`C_(L-v)(f_lambda)=g(v)`，

`g(v)=int_0^v conjugate(f_L(u))f_R(v-u)du`.           (14)

`g` 连续且支撑在 `[0,2B]`。小平移还会产生两个边界层各自内部的相关，
但它们只来自 `log n<=B` 的有限多个 `n`，总贡献为 `O(1)=o(P(x))`。
其他平移的相关为零。定理 DR 因而给出式 (11)，因为 Fubini 定理给出

`int_0^infinity e^(-v/2)g(v)dv=conjugate(L_0)R_0`.   (15)

最后使用 `P(x)/lambda->2` 得到式 (13)。`□`

对两个不同的边界数据极化式 (11)，从右边界到左边界的有向极限算子是
秩一的：它只看式 (9) 的两个 Laplace 边界矩。式 (13) 的自伴 Hermitian
化在左右边界直和上一般是秩二，而不是秩一；后文“同一个通道”均指这个
精确意义。

## 3. 极点锚的同一个秩一极限

回忆

`C(f)=int f(y)cosh(y/2)dy`,

`S(f)=int f(y)sinh(y/2)dy`,                           (16)

以及

`Q_(0,2)(f)=2|C(f)|^2-2|S(f)|^2`.                   (17)

### 命题 DT（pole anchors have the same Hermitianized boundary channel）

对式 (8) 的边界层族，

`C(f_lambda)/sqrt(lambda)->(L_0+R_0)/2`,

`S(f_lambda)/sqrt(lambda)->(-L_0+R_0)/2`,             (18)

从而

`lambda^(-1)Q_(0,2)(f_lambda)`

`->2Re(conjugate(L_0)R_0)`.                          (19)

#### 证明

在左边界写 `y=-ell+u`、右边界写 `y=ell-z`，并使用
`sqrt(lambda)=e^(ell/2)`。例如

`lambda^(-1/2)cosh((-ell+u)/2)->(1/2)e^(-u/2)`，

`lambda^(-1/2)sinh((-ell+u)/2)->-(1/2)e^(-u/2)`，    (20)

右端两个极限的符号都为正。紧支撑上的控制收敛给出式 (18)。再用恒等式

`|L_0+R_0|^2-|-L_0+R_0|^2`

`=4Re(conjugate(L_0)R_0)`                            (21)

得到式 (19)。`□`

## 4. Weil form 的主阶相消

完整 zeta Weil form 写成

`QW_lambda=K_infinity-W_P,lambda+Q_(0,2)`,            (22)

其中

`K_infinity(f)=int K_infinity(t)|hat f(t)|^2dt/(2pi)`. (23)

### 定理 DU（boundary-layer prime--pole cancellation）

对任意固定 `f_L,f_R in C_c^1((0,B))`，式 (8) 的族满足

`QW_lambda(f_lambda,f_lambda)=o(lambda)`.             (24)

更准确地，式 (22) 中 prime correlation 与 pole form 除以 `lambda`
都收敛到式 (13)/(19) 的同一个秩一型，故彼此相消；archimedean form
一致为 `O(1)`。

#### 证明

命题 DS、DT 已处理两个 `lambda` 阶项。平移固定剖面只在 Fourier 变换中
乘以模为一的相位。因为剖面是紧支撑 `C^1` 函数，其 Fourier 变换为
`O((1+|t|)^(-1))`；又有

`|K_infinity(t)|<=C+log(2+|t|)`。                    (25)

用 `|a+b|^2<=2|a|^2+2|b|^2` 即得式 (23) 的绝对值一致有界。
式 (13)、(19) 代入式 (22) 后得到式 (24)。`□`

## 5. 对 Hodge 结构路线的含义与限制

1. 文档 016 中 endpoint degree 与 pole anchor 的同阶现象不是偶然尺度匹配；
   它们在完整边界层上具有完全相同的 PNT 秩一主符号。
2. 因此任何把 prime defect 和 pole polarization 分开取 operator norm 的证明
   都会丢掉主阶相消。适合的 core 必须同时携带左右边界 Laplace 矩。
3. 定理 DU 只给 `o(lambda)`，而过滤定理 BA/DO 最终需要绝对误差 `o(1)`
   或精确非负。下一步必须提取式 (11) 的次主项，并把它与 archimedean
   form 及 canonical core 的 Feshbach block 联合起来。
4. 对 twisted Dirichlet/automorphic 数据，式 (11) 会带局部相位；普通 PNT
   不再足够，需要相应扭曲 Chebyshev 和的统一端点渐近。这恰好标记了
   zeta 与一般 GRH 之间新增的算术输入。

脚本 `weighted_prime_gap_average` 直接计算式 (3)；回归测试用
`g(v)=e^(-v)` 检查其平均值趋向极限 `1/3`。该检查用于发现归一化或常数
转录错误，不是定向舍入证明。普通高精度计算给出

| `x` | `int e^(-v)dmu_x(v)` |
|---:|---:|
| 13 | 0.5488391146 |
| 101 | 0.3826729316 |
| 1009 | 0.3469419025 |

与极限 `1/3` 一致。
