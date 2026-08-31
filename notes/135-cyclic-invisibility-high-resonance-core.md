# Arithmetic cyclic invisibility of high resonance cores

文档 134 证明，在 `delta^3logT->infinity` 的日程下，Abel negative core 的
相对 Hodge index与余空间误差同时趋零。但相对 dimension 为零仍允许 core
承载少数异常 divisor。本节向“绝对不可见性”推进一步：固定 arithmetic
cyclic vector 的 frequency profile 会衰减，因此即使高频 core 的绝对维数
巨大，该向量投到 core 的 norm仍趋零。

对 profile `O(|t|^(-r))`, `r>1/2`，结论来自文档 133 的负质量界
`O(delta^(-3)T/logT)` 与 weighted concentration spectral theorem。特别地，
finite-filter resolvent/kernel vector 的 Fourier profile

`q_(z,B)(t)=[1-e^(-(z-it)B)]/(z-it)`                (1)

有 `r=1`；其全部 dyadic high-resonance cores上的 projection norm squared
至多 `O(epsilon_(delta,T)/T)`。这里必须使用有限 `B`：未截断的
`1/(z-it)` 属于 half-line Hardy 模型，并不直接属于文档 133 的
`L^2([-B,B])`。修正后仍无条件消除了高频 cores 对固定 explicit-formula
测试向量的影响，把尚未解决的绝对 obstruction局限到
`|t| lesssim Y polylog Y` 的低—中频区域。

## 1. Cyclic energy on one resonance window

沿用文档 133，令

`W_T(t)=[-Re F_Y(x+it)]_+1_[T,2T](t)`,              (2)

并在 `delta<=x<=M`、window-size condition成立时写

`int_T^(2T)W_T(t)dt`

` <=A_(delta,M)T/logT`.                             (3)

文档 134 给 `A_(delta,M)<=C_M delta^(-3)`。令 `C_(W_T)` 是带限空间
`L^2([-B,B])` 上的 weighted concentration operator，`Q_(T,epsilon)` 是
其 eigenvalues `>epsilon` 的 spectral projection。

设一个 cyclic vector `f` 满足

`|hat f(t)|<=C_f t^(-r)` on `[T,2T]`, `r>1/2`.      (4)

### 定理 YG（single-window cyclic-core leakage）

在上述条件下，

`<C_(W_T)f,f>`

` <=[A_(delta,M)C_f^2/(2pi logT)]T^(1-2r)`,         (5)

且

`||Q_(T,epsilon)f||^2`

` <=[A_(delta,M)C_f^2/(2pi epsilon logT)]`

`                                      *T^(1-2r)`. (6)

#### 证明

由式 (4)，

`<C_(W_T)f,f>`

` =int W_T|hat f|^2dt/(2pi)`

` <=C_f^2T^(-2r)/(2pi) int W_T`.                   (7)

代入式 (3) 得式 (5)。在 `Q=Q_(T,epsilon)` 上
`C_(W_T)>=epsilon Q`，所以

`epsilon||Qf||^2<=<C_(W_T)f,f>`,                   (8)

给式 (6)。`□`

这个 bound控制的是某个固定 vector 的 **absolute projection norm**，而不是
除以 core dimension后的平均量。

## 2. 全部 dyadic 高频井

令

`W_(>=T)=sum_(k>=0)W_(2^kT)`,                      (9)

其中正负高度可分别处理后直和。假设文档 133 的 window condition从 `T`
开始对所有 dyadic windows成立。由 `r>1/2`，

`sum_(k>=0)(2^kT)^(1-2r)`

` =T^(1-2r)/[1-2^(1-2r)]`.                         (10)

### 定理 YH（dyadic high-core cyclic invisibility）

令 `Q_(>=T,epsilon)` 是 `C_(W_(>=T))` 在 `(epsilon,infinity)` 的 spectral
projection。则

`||Q_(>=T,epsilon)f||^2`

` <=A_(delta,M)C_f^2 T^(1-2r)`

`   /[2pi epsilon logT(1-2^(1-2r))]`.              (11)

取文档 134 的 balanced threshold

`epsilon_(delta,T)`

` =sqrt(A_(delta,M)/logT)`，                        (12)

得到

`||Q_(>=T,epsilon_(delta,T))f||^2`

` <=C_f^2 epsilon_(delta,T)T^(1-2r)`

`                  /[2pi(1-2^(1-2r))]`.            (13)

只要 `T->infinity` 且 `epsilon_(delta,T)` 至多 subpolynomial增长，右侧就趋零；
在 `delta^3logT->infinity` 的 cofinal日程下更有
`epsilon_(delta,T)->0`。

#### 证明

对式 (5) 在 dyadic windows求和，使用
`log(2^kT)>=logT` 与式 (10)，得到 global weighted energy bound。
再对 global operator使用式 (8)，给式 (11)；代入式 (12)得到式 (13)。`□`

使用 global spectral projection很重要：不需要假设不同 window cores彼此正交，
也不会遭遇“每个 projection很小但它们的 span ill-conditioned”的问题。

## 3. Resolvent/kernel vectors

取 `f_(z,B)(y)=e^(zy)1_[-B,0](y)`；其 Fourier transform正是式 (1)。
固定 `z in C_+`。若 `t>=T>=2|z|`，则

`|z-it|>=t-|z|>=t/2`,

`|q_(z,B)(t)|<=2(1+e^(-B Re z))/t<=4/t`.           (14)

### 推论 YI（finite-filter resolvent cores are invisible at high frequency）

对式 (1)，定理 YH 可取
`r=1,C_f=2(1+e^(-B Re z))<=4`，故

`||Q_(>=T,epsilon_(delta,T))f_(z,B)||^2`

` <=4(1+e^(-B Re z))^2epsilon_(delta,T)/(pi T)`

` <=16epsilon_(delta,T)/(pi T)`.                   (15)

因此沿任意满足 `T>=2|z|`、`T->infinity`、
`delta^3logT->infinity` 的 cofinal日程，右侧趋零。

同理，任意 finite linear combination of resolvent vectors、以及 Fourier
profile具有更高 polynomial decay 的 smooth compactly supported test vector，
都对 high-resonance core渐近不可见。对后者，任意次 integration by parts给
任意大的 `r`。

式 (15) 是文档 134 逻辑边界中第一个 **absolute cyclic invisibility** 结果：
尽管不能证明整个 negative core消失，但它对每个固定 arithmetic kernel
vector的高频部分确实消失。

## 4. 高频 obstruction 的无条件局域化

选取 `T_Y` 满足

`T_Y>=C_(delta,M)Ylog^3(YT_Y)`                     (16)

及 `T_Y->infinity`。文档 133 定理 XZ从该高度起适用；推论 YI说明所有
`|t|>=T_Y` 的 balanced negative cores 对 fixed finite-filter resolvent test
family不可见。

所以任何仍能阻止 passive limit 的 cyclic obstruction必须来自

`|t|<T_Y`,                                          (17)

即随 `Y` 增长的低—中频 core，而不是此前粗 absolute-mass bound允许的
`exp(O(Y^(1/2-delta)logY))` 极高频区域。式 (17) 不是说后者没有负井，而是
它们不能被任何固定 resolvent/kernel vector以非消失 norm看见。

这把存在性问题进一步拆成两个不对称部分：

- high frequencies：relative index、complement error、cyclic projection都已
  无条件趋零；
- low/intermediate frequencies：仍需证明 growing core 对 separating cyclic
  family 的 projection趋零，或直接证明其 Feshbach block正。

## 5. Fixed-degree extension

对文档 134 的 fixed-degree tempered Gamma--Euler data，
`A_(delta,M)` 至多多一个 `d^2` factor。因此 balanced threshold多一个 `d`，
式 (13)、(15) 仍对固定 `d,B` 趋零。非自对偶数据先与 dual配对，resolvent
profiles取有限向量值；Cauchy--Schwarz只增加固定 matrix dimension常数。

所以 high-core cyclic invisibility属于广义 Gamma--Euler passive package的
稳定性质，而不是 zeta scalar case的偶然现象。

## 6. 实现与 audit

新增：

- `abel_cyclic_core_leakage_bound`：式 (5)--(13) 的单窗口/全 dyadic tail
  energy与 projection norm账本；
- `abel_resolvent_core_leakage_bound`：式 (14)--(15) 的 finite-filter
  resolvent specialization；现在显式要求 `truncation_length=B`。

示例取 `delta=.2,r=1,C_f=3,A=2`：

| `T` | balanced threshold | cyclic energy bound | core projection norm bound |
|---:|---:|---:|---:|
| `10^2` | `5.31` | `8.07e-1` | `3.90e-1` |
| `10^4` | `3.75` | `4.04e-3` | `3.28e-2` |
| `10^6` | `3.07` | `2.69e-5` | `2.96e-3` |

这里固定 `delta` 且高度尚不足以让 balanced threshold小于一，但 polynomial
profile decay已经使 absolute leakage快速消失。对
`z=.4+3i,T=10^4,B=2` 的 resolvent specialization，profile constant约
`2.90`，projection norm bound约 `3.17e-2`。此前未截断 Hardy profile给出的
`2.19e-2` 不能直接作为 finite-filter core 的投影界。这些是解析 scaling
formulas的数值转录，不是 zero evidence。

## 7. 下一步：中频 core 的 cyclic Gram

剩余核心现在是有限频率区 `|t|<T_Y` 上的 growing weighted spectral space。
直接用 rank不够；最相关的新量是 separating resolvent family在该 core上的
Gram：

`R_(Y,B)(z,w)=<Q_(<T_Y)f_(z,B),Q_(<T_Y)f_(w,B)>`.  (18)

若能在每个 compact `z,w in C_+` 上证明

`R_(Y,B)(z,w)->0`,                                  (19)

则高频由推论 YI、低中频由式 (19) 合并，全部 negative cores对 arithmetic
RKHS cyclic family不可见。配合余空间 `o(1)` 与文档 015 filtered positivity，
将得到完整 Pick kernel正性，再由文档 131 定理 XQ推出 RH。

因此下一目标不是 core 的裸 dimension，而是式 (18) 的 resolvent-weighted
trace/Gram。文档 136 直接用 `Q<=C_W/epsilon` 把它压到一个
Cauchy-weighted negative mass，并给出相应 filtered passive结构定理。
