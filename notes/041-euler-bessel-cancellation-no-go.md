# Euler--Bessel 高模态相消与绝对值 no-go

文档 038 命题 FI 把每个 Hodge 坐标写成安全半平面中的 Euler 值级数。
本笔记审计能否对该级数逐项估计。结论是否定的：去掉交替符号会把
Bessel `J` 变成 modified Bessel `I`，产生指数级伪增长；而 centered
Euler remainder 及其离散采样也不具有完全单调性，不能由正测度自动恢复
交替相消。任何成功的高模态估计必须保留 signed prime--continuum measure
或等价的整体 Hankel 结构。

## 1. Euler--Bessel 级数

固定 `sigma>0`，令

`q=1+2sigma`, `nu=1/(2sigma)`, `a=nu+1`,

`j=j_(nu,n)`, `C=sqrt(2sigma)/|J_a(j)|`.             (1)

定义 centered real Euler remainder

`R(s)=(-zeta'/zeta)(s)-1/(s-1)`, `s>1`.             (2)

文档 038 的坐标为

`A_(n,sigma)=-e_(n,sigma)(1)`

` +C sum_(m>=0)(-1)^m a_m(j)R(q+2sigma m)`,          (3)

其中

`a_m(j)=(j/2)^(2m+a)/[m!Gamma(m+a+1)]>0`.           (4)

### 命题 FU（absolute Euler majorant is a modified-Bessel sum）

若 `M_sigma=sup_(s>=q)|R(s)|`，则对式 (3) 逐项取绝对值得

`|A_(n,sigma)|<=|e_(n,sigma)(1)|`

`                       +C M_sigma I_a(j)`,          (5)

因为

`I_a(j)=sum_(m>=0)a_m(j)`.                           (6)

#### 证明

式 (6) 是 modified Bessel 函数的定义幂级数；三角不等式直接给式
(5)。`R` 在 `[q,infinity)` 连续且趋零，故 `M_sigma<infinity`。`□`

## 2. 指数伪损失

### 定理 FV（coefficientwise absolute estimates cannot prove Hodge summability）

式 (3) 的实际逐项绝对 majorant

`M_(n,sigma)=|e_n(1)|`

` +C sum_m a_m(j)|R(q+2sigma m)|`                    (7)

满足

`M_(n,sigma)>=c_sigma e^j/j`                         (8)

对所有充分大的 `n`；另一方面

`lambda_(n,sigma) asymp_sigma j^2`.                  (9)

因此

`sum_n M_(n,sigma)^2/lambda_(n,sigma)=infinity`     (10)

以指数速度失败。任何只保留每个 Euler remainder 绝对值的证明都不可能
建立文档 038 式 (14)。

#### 证明

当 `s->infinity` 时

`(-zeta'/zeta)(s)=O(2^(-s))`，所以

`|R(s)|=1/(s-1)+O(2^(-s))`.                          (11)

`I_a(j)` 幂级数的 saddle 位于 `m=j/2+O_a(1)`，宽度为 `O(sqrt j)`；该
窗口承载总和的固定正比例。在此窗口
`|R(q+2sigma m)|asymp_sigma 1/j`，故式 (7) 的级数部分至少为
`c_sigma C I_a(j)/j`。标准渐近

`I_a(j)~e^j/sqrt(2pi j)`,

`|J_a(j_(nu,n))|asymp sqrt(2/(pi j))`                (12)

给 `C I_a(j)asymp_sigma e^j`，证明式 (8)。Bessel 零点
`j_(nu,n)asymp pi n` 与文档 038 式 (3) 给式 (9)–(10)。`□`

FV 解释了为何安全 Euler 半平面虽解决“单坐标可定义性”，却不能通过朴素
absolute convergence 解决联合高模态问题。

## 3. 完全单调性捷径也不存在

令

`F(s)=1/(s-1)-(-zeta'/zeta)(s)=-R(s)`.              (13)

形式上

`F(s)=int_0^infinity e^(-st)dmu(t)`,                 (14)

其中 signed measure

`dmu(t)=e^t dt-sum_(n>=2)Lambda(n)delta_(log n)`.    (15)

### 定理 FW（centered Euler remainder is not completely monotone）

`F` 在 `(1,infinity)` 上不是完全单调函数。更强地，对任意固定
`q>1`,`h>0`，序列

`F(q+hm)`, `m=0,1,...`                               (16)

不是 Hausdorff completely monotone sequence。

#### 证明

若 `F` 完全单调，Bernstein 定理给出 `[0,infinity)` 上正测度，其 Laplace
变换为 `F`。但对任意 `q>1`，式 (15) 乘 `e^(-qt)` 后具有有限总变差，
Laplace 变换唯一性迫使该正测度等于式 (15)；后者在每个 `log n` 有负 atom
`-Lambda(n)`，矛盾。

对离散序列，把 `y=e^(-ht)` 推到 `[0,1]`。式 (16) 是 finite signed
measure `e^(-qt)dmu(t)` 的 moments。若它是 Hausdorff completely
monotone，Hausdorff moment theorem 给出具有相同 moments 的正测度；紧
区间 moment uniqueness 再迫使它等于含负 atoms 的 pushforward，矛盾。
`□`

数值上 `F(s)` 的前若干导数或差分可能具有正确符号；FW 证明这种现象不
可能延续到全部阶数，不能作为全局 positivity 输入。

## 4. 保留相消的精确重求和

式 (14) 代入式 (3) 的交替部分。令 `h=2sigma`。Bessel 幂级数恒等式为

`sum_(m>=0)(-1)^m a_m(j)e^(-hmt)`

`=e^(ha t/2)J_a(je^(-ht/2))`.                       (17)

因 `ha/2=q/2`，得到：

### 命题 FX（cancellation-preserving Euler--Bessel resummation）

有

`sum_m(-1)^m a_m(j)F(q+hm)`

`=int_0^infinity e^(-qt/2)J_a(je^(-sigma t))dmu(t)`. (18)

右边保留 signed continuum-minus-primes measure 与振荡 Bessel `J`；把
`dmu` 换成其 total variation 恰会恢复定理 FV 的 modified-Bessel 指数
损失。

#### 证明

将式 (14) 代入左边，在绝对收敛的有限截断后交换和与积分，再用式 (17)
重求和。由 `q>1` 的指数权及 Bessel 有界性取极限，得到式 (18)。`□`

FX 与文档 039 的 Fourier--Bessel current pairing 是同一个恒等式的
Euler-sampling 版本。它说明高模态相消只能来自：

1. prime atoms 与 continuum background 的 signed cancellation；
2. Bessel oscillation across the whole multiplicative scale。

二者任一被绝对值移除都会失去可用界。

## 5. 高模态证明所需的新输入

### 推论 FY（necessary form of a noncircular high-mode estimate）

要证明 RH 路线所需的

`sum_n |A_(n,sigma)|^2/lambda_(n,sigma)<infinity`    (19)

对 `sigma<1/2` 成立，一个基于式 (3) 的论证必须至少保留以下之一：

- Euler remainder 样本间足以重建式 (18) 的 signed finite differences；
- 对 signed measure `dmu` 的 Hankel/Bessel large-sieve cancellation；
- 等价的 prime--continuum discrepancy `L^2` 控制。

纯 coefficientwise absolute bounds、正 Hausdorff moment 表示、或把 Euler
samples 独立处理都被 FV/FW 排除。

这不是对所有可能证明的 no-go，而是对当前显式 Euler--Bessel 坐标中一大
类局部化策略的严格排除。剩余可行目标是构造保留 signed measure 的 block
估计，而不是继续收紧单个 `|R(s_m)|`。

## 6. 数值审计

脚本 `zeta_bessel_euler_coordinate` 同时计算式 (3) 的交替截断和式 (7) 的
绝对 majorant。取 `sigma=0.75`，模态 `n=1,3,5` 时：

| `n` | signed coordinate | absolute majorant | ratio |
|---:|---:|---:|---:|
| 1 | -1.95455 | 4.67148 | 2.39 |
| 3 | -1.23348 | 1252.61 | 1016 |
| 5 | -1.03390 | 432661 | 418475 |

这只展示定理 FV 已证明的伪损失机制；小模态实际值接近常数不预示其未知
无限渐近。
