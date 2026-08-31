# 边界 Mellin 显式公式与 RH 的有界能量判据

文档 030 只用素数定理证明边界层 Weil form 为 `o(lambda)`。本笔记提取
被该粗渐近隐藏的全部次主项：prime--pole 主项消去后，边界能量恰由
`x^(rho-1/2)` 的零点模态控制。这给出一个新的等价刻画：RH 当且仅当
每个固定光滑左右边界通道的 Weil 能量随截断一致有界。

这个判据不是 RH 的证明，因为所需有界性仍等价于零点位于中心线；它的
价值在于把文档 016–030 的 endpoint Hodge core 与经典显式公式精确接合，
并给出适用于一般 Euler 数据的抽象“边界结构定理”。

## 1. 光滑端点素数和的 Mellin 公式

取 `h in C_c^infinity((0,B))`，延拓为实线上的零函数，并定义

`H(s)=int_0^infinity h(v)e^(-sv)dv`,                  (1)

`A_h(x)=sum_(n>=1) Lambda(n)n^(-1/2)h(log(x/n))`.    (2)

由于 `h(v)=0` 对 `v<0`，式 (2) 实际只含 `n<=x`。`H` 是整函数，且在
任意固定竖直带上沿虚方向快降。

### 定理 DV（smoothed endpoint explicit formula）

若 `x>e^B`，则

`A_h(x)=x^(1/2)H(1/2)`

` -sum_rho H(rho-1/2)x^(rho-1/2)`

` -sum_(m>=1)H(-2m-1/2)x^(-2m-1/2)`,                (3)

其中第一和遍历 zeta 的全部非平凡零点并计重数。非平凡零点和绝对收敛，
平凡零点和也因 `x>e^B` 绝对收敛。

#### 证明

Laplace 反演和 `-zeta'/zeta` 的绝对收敛 Dirichlet 级数在 `c>1/2`
给出

`A_h(x)=(1/(2pi i))int_(c-i infinity)^(c+i infinity)`

` H(s)(-zeta'/zeta(s+1/2))x^s ds`.                  (4)

把积分线向左移动。`-zeta'/zeta(s+1/2)` 在 `s=1/2` 的留数为 `+1`，
在 `s=rho-1/2` 和 `s=-2m-1/2` 的留数为 `-1`。这给出式 (3) 的三个
符号。`H` 的竖直快降与标准零点计数保证水平边消失和非平凡零点和绝对
收敛。若积分线移至 `Re s=-R`，紧支撑给
`|H(-R+it)|<=C_N e^(BR)(1+|t|)^(-N)`；因 `x>e^B`，剩余竖线在
`R->infinity` 时消失，同时得到平凡零点和的绝对收敛。`□`

式 (3) 中无需假设 RH；每个零点的实增长指数正是 `Re rho-1/2`。

## 2. 边界卷积的因子化

沿用文档 030 的 `f_L,f_R in C_c^infinity((0,B))`，令

`h(v)=int_0^v conjugate(f_L(u))f_R(v-u)du`.           (5)

定义整函数

`L(s)=int f_L(u)e^(-su)du`,

`R(s)=int f_R(u)e^(-su)du`,

`L^sharp(s)=conjugate(L(conjugate(s)))`.              (6)

### 命题 DW（boundary Mellin channel factorization）

式 (5) 的 Laplace 变换满足

`H(s)=L^sharp(s)R(s)`.                               (7)

特别地

`H(1/2)=conjugate(L_0)R_0`,                          (8)

正是文档 030 命题 DS/DT 中的有向秩一通道。

#### 证明

在式 (1)、(5) 中令 `v=u+z`，Fubini 定理把二重积分分成

`[int conjugate(f_L(u))e^(-su)du]`

`[int f_R(z)e^(-sz)dz]=L^sharp(s)R(s)`.              (9)

取 `s=1/2` 得式 (8)。`□`

## 3. 完整边界 Weil form 的零点展开

令 `f_lambda` 是文档 030 式 (8) 的左右边界层，`x=lambda^2`。当
`2log lambda>3B` 时，全部 prime correlations 精确分成：

- 大平移的左右相关 `A_h(x)`；
- 只涉及 `log n<=B` 的两个固定边界内部相关 `J(f_L,f_R)`。

后者与 `lambda` 无关。再令

`L_+=int f_L(u)e^(u/2)du`,

`R_+=int f_R(u)e^(u/2)du`.                           (10)

极点 form 可精确展开为

`Q_(0,2)(f_lambda)=2lambda Re(conjugate(L_0)R_0)`

` +2Re(R_0 conjugate(R_+)+L_+ conjugate(L_0))`

` +2lambda^(-1)Re(L_+ conjugate(R_+))`.              (11)

### 命题 DX（boundary Weil form is a zero-mode expansion）

存在显式余项 `E_(f_L,f_R)(lambda)`，在 `lambda->infinity` 时一致有界，
使

`QW_lambda(f_lambda,f_lambda)`

`=2Re sum_rho H(rho-1/2)x^(rho-1/2)`

` +E_(f_L,f_R)(lambda)`.                             (12)

其中 `E` 恰由以下四部分组成：一致有界的 archimedean form、固定的
边界内部 prime correlations、式 (11) 去掉第一行后的极点余项，以及
式 (3) 的平凡零点和的 `2Re`。

#### 证明

完整 form 是

`QW=K_infinity-2Re(A_h+J)+Q_(0,2)`.                  (13)

定理 DV 中 `A_h` 的第一项为
`lambda H(1/2)=lambda conjugate(L_0)R_0`；它在式 (13) 中产生
`-2lambda Re H(1/2)`，与式 (11) 第一行精确抵消。非平凡零点项因
式 (13) 的负号变成式 (12) 的正号。文档 030 定理 DU 的 Fourier-tail
论证给出 archimedean form 的一致有界性；其余三部分显然或由定理 DV
一致有界。`□`

所以文档 030 的 `o(lambda)` 结论只是式 (12) 与经典零点零自由区域的粗略
后果；式 (12) 保留了所有被 PNT 压扁的谱信息。

## 4. 一个新的 RH 等价判据

### 定理 DY（boundary-energy criterion for RH）

下列命题等价：

1. Riemann 猜想成立；
2. 对每个 `B>0` 和每对 `f_L,f_R in C_c^infinity((0,B))`，有

   `sup_(lambda>=lambda_0)|QW_lambda(f_lambda,f_lambda)|<infinity`. (14)

#### 证明：RH 推出有界性

若 RH 成立，`rho-1/2=i gamma`，故式 (12) 中每个指数因子的模为一。
`H` 在竖直带快降，而零点数为 `O(Tlog T)`，所以

`sum_rho |H(i gamma)|<infinity`.                     (15)

式 (12) 与 `E=O(1)` 给出式 (14)。

#### 证明：有界性推出 RH

先记

`R_h(x)=A_h(x)-x^(1/2)H(1/2)`.                       (16)

式 (11)、(13) 与其余项的一致有界性说明：若式 (14) 对所有复剖面成立，
则 `Re R_h(x)=O(1)`。把 `f_R` 依次乘以 `1` 和 `i`，式 (5)–(8) 也依次
乘以 `1` 和 `i`，从而分别控制实部和虚部，得到

`R_h(x)=O(1)`.                                       (17)

对 `Re w>1/2` 直接交换和与积分可得

`int_1^infinity R_h(x)x^(-w-1)dx`

`=H(w)(-zeta'/zeta(w+1/2))-H(1/2)/(w-1/2)`.          (18)

由式 (17)，左边解析延拓到整个 `Re w>0`。若存在零点
`rho_0` 满足 `Re rho_0>1/2`，则右边在 `w_0=rho_0-1/2` 有极点，除非
`H(w_0)=0`。但可选择支撑在任意小区间内的非负实 bump
`f_L=f_R`，使 `L(w_0)` 不为零；由式 (7)，相应 `H(w_0)` 也不为零，
矛盾。因此没有中心线右侧零点。函数方程的对称性又排除左侧零点，故 RH
成立。`□`

这里的“对所有剖面”可以缩小到任意 Laplace 变换在每个 `Re w>0` 点都能
取非零值的可数稠密 bump 族。定理 DY 与 Weil 全局正性判据不同：它只
要求移动边界族的双边有界，而不要求非负；代价是这个有界性本身已经携带
全部 RH 零点信息。

## 5. 广义 Gamma--Euler 边界结构

设 `Z(s)` 是有限阶 meromorphic Euler 函数，

`-Z'/Z(s)=sum_(n>=1)b(n)n^(-s)`                      (19)

在某右半平面绝对收敛；其完备 divisor 关于 `Re s=c/2` 对称。设中心线
右侧的已知 poles 为 `p`，阶数为 `m_p`。定义

`A_(Z,h)(x)=sum_n b(n)n^(-c/2)h(log(x/n))`,           (20)

`R_(Z,h)(x)=A_(Z,h)(x)`

` -sum_p m_p H(p-c/2)x^(p-c/2)`.                    (21)

### 定理 DZ（general boundary-divisor structure theorem）

假设 `Z` 满足使 contour shift 合法的标准有限阶、零点计数和 Gamma-factor
增长条件。若一个 separating 测试族的每个 `R_(Z,h)(x)` 都是 `O(1)`，则
`Z` 没有中心线右侧的非平凡零点；结合 divisor 对称性，全部非平凡零点
位于 `Re s=c/2`。

反之，若全部非平凡零点位于中心线，且测试函数的 `H` 具有足够竖直快降，
则每个 `R_(Z,h)` 都是 `O(1)`。

#### 证明

式 (4) 原封不动变为

`H(w)(-Z'/Z(c/2+w))`.                                (22)

移动 contour 后，右侧 poles 给出式 (21) 中被减去的增长项；非平凡零点
给 `-H(rho-c/2)x^(rho-c/2)`。若余项有界，其 Mellin 变换在
`Re w>0` 解析；separating 性排除 `-Z'/Z` 在该半平面的任何未减极点，
特别排除右侧零点。反向蕴含与定理 DY 的绝对收敛论证相同。`□`

DZ 是一个足够广的显式公式结构定理：所需“代数结构”被压缩为 Euler
对数导数、中心对称 divisor，以及一族有界的边界 translation matrix
coefficients。对 zeta，这个结构的局部卷积因子化与 pole 主项相消已由
DW/DX 无条件构造；尚未证明的恰是 DY 的一致 `O(1)`，即 RH 强度的全球
存在性条件。

## 6. 数值转录审计

脚本使用

`h(v)=v^4(2-v)^4 1_[0,2](v)`                        (23)

检查式 (3)。在 `x=1009` 时，直接素数幂和为

`A_h(x)=15.8371955043591833`，

主项为 `15.8364784083107561`；加入前 50 对数值 zeta 零点与平凡零点后为

`15.8371955059648341`，误差约 `1.61*10^(-9)`。这只检查常数、符号与
`rho-1/2` 平移的转录，不是 RH 的数值证据。
