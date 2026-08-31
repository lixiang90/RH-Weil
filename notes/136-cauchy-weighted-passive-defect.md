# Cauchy-weighted passive defect 与 resolvent-core 消失

文档 135 把 Abel resonance 的高频 core 对固定测试向量的影响压到零，但把
低—中频目标留成一个 growing spectral projection 的 Gram。本节证明不必显式
求这个 projection：spectral calculus 直接把全部 resolvent Gram 压到一个标量

`J(F,delta)=int_R [-Re F(delta+it)]_+/(1+t^2)dt`.   (1)

若一列 arithmetic holomorphic candidates 满足 `delta_Y->0` 与 `J_Y->0`，
则其负 core 在每个有限过滤、每个固定 resolvent family 上消失；再加一个已知
收敛的 Euler half-plane 基点与 Poisson admissibility，就得到全右半平面的
normal passive limit。由文档 131 的 positive-real Weil theorem，中心线结论
随即成立。

这给出一个比“所有 Pick matrices 逐点控制”更紧凑的广义结构定理。对 zeta
的 Abel 候选，Poisson admissibility 与 (1) 的高频尾都已无条件成立；尚缺项
精确缩成低—中频 Cauchy-weighted negative mass 的消失。

## 1. 有限过滤 resolvent 的修正

令 `H_B=L^2([-B,0])`，Fourier convention 与文档 133 相同。对 `z=x+iy in
C_+`，取

`f_(z,B)(u)=e^(zu)1_[-B,0](u)`.                    (2)

则

`hat f_(z,B)(t)=[1-e^(-(z-it)B)]/(z-it)`.          (3)

文档 135 旧版本直接使用的 `1/(z-it)` 是 `B=infinity` 的 half-line Hardy
profile，不属于任一 finite `H_B`。式 (3) 是与 weighted-prolate core 相容的
正确向量；文档 135 已据此修正高频常数。

### 引理 YJ（sharp Cauchy resolvent weight）

写 `z=x+iy`, `x>0`，并令

`tau_z=1+|z|^2`,

`c(z)=[tau_z+sqrt(tau_z^2-4x^2)]/(2x^2)`.          (4)

则

`sup_(t in R)(1+t^2)/|z-it|^2=c(z)`.               (5)

因此

`(1+t^2)|hat f_(z,B)(t)|^2`

` <=c_B(z):=(1+e^(-xB))^2c(z)`.                   (6)

#### 证明

把 `v=(t,1)^T`。分母为

`|z-it|^2=v^T[[1,-y],[-y,x^2+y^2]]v`,             (7)

分子为 `v^TIv`。式 (5) 是 positive matrix (7) 的最小 eigenvalue之倒数；
其 trace 为 `tau_z`、determinant 为 `x^2`，解二次式即得 (4)。式 (3) 的
分子至多 `1+e^(-xB)`，给式 (6)。`□`

## 2. 不求 core 的 Gram 支配

令 `W>=0`, `W in L^1(R)`，并令文档 133 的

`C_W=(2pi)^(-1)F^*M_WF`                            (8)

作用在 `H_B`。对 `epsilon>0` 写

`Q_epsilon=1_(epsilon,infinity)(C_W)`.             (9)

### 定理 YK（Cauchy-weighted core Gram domination）

记

`J_W=int_R W(t)/(1+t^2)dt`.                        (10)

则对任意 `z,w in C_+`，

`|<Q_epsilon f_(z,B),Q_epsilon f_(w,B)>|`

` <=J_W sqrt(c_B(z)c_B(w))/(2pi epsilon)`.         (11)

特别地，若 `J_W->0` 并取

`epsilon_W=sqrt(J_W)`,                             (12)

则余空间上的 negative multiplier error 至多 `sqrt(J_W)`，同时式 (11) 在
每个 compact `z,w` 上局部一致趋零。

#### 证明

对 `C_W` 作 spectral calculus：在 eigenvalue `lambda` 上，
`1_(epsilon,infinity)(lambda)<=lambda/epsilon`，所以

`0<=Q_epsilon<=C_W/epsilon`.                       (13)

先在 `Q_epsilon` 的正半内积中用 Cauchy--Schwarz，再用式 (13)：

`|<Qf,Qg>|<=<Qf,f>^(1/2)<Qg,g>^(1/2)`

` <=epsilon^(-1)<C_Wf,f>^(1/2)<C_Wg,g>^(1/2)`.    (14)

式 (6)、(8)、(10) 给

`<C_Wf_(z,B),f_(z,B)><=c_B(z)J_W/(2pi)`.          (15)

代入即得式 (11)。式 (12) 同时使 complement error 与 Gram bound 为
`O(sqrt(J_W))`。`□`

这比文档 135 的 high-tail decay 强：只要 full-line 标量 (10) 消失，就无需
分井、无需知道 core rank，也无需处理不同窗口 projection span 的条件数。

## 3. Poisson-filtered passive 结构定理

令 `{F_n}` 是 `C_+` 上 holomorphic、real-type 的 arithmetic candidates，
`delta_n>0`, `delta_n->0`。定义

`W_n(t)=[-Re F_n(delta_n+it)]_+`,

`J_n=int_R W_n(t)/(1+t^2)dt`.                      (16)

称该族 **Poisson admissible**，若对 `x>delta_n` 有

`Re F_n(x+iy)`

` >=-(1/pi)int_R (x-delta_n)W_n(t)`

`              /[(x-delta_n)^2+(y-t)^2]dt`.       (17)

式 (17) 允许在 infinity 有非负 harmonic term，但不允许一条在 boundary
不可见的负线性通道。

### 定理 YL（Cauchy-filtered passive Weil structure theorem）

设：

1. `{F_n}` Poisson admissible；
2. 存在非空开集 `U subset C_+`，`F_n` 在 `U` locally uniformly 收敛到某个
   arithmetic germ `F_ar`；
3. `J_n->0`。

则 `{F_n}` 在整个 `C_+` locally uniformly 收敛到唯一 holomorphic
positive-real continuation `F` of `F_ar`。若 `F_ar=Phi'/Phi`，其中 `Phi`
满足文档 131 定理 XQ 的 real self-dual order-one hypotheses，则 `Phi` 的全部
非零 zeros 位于中心轴。

#### 证明

固定 compact `K subset C_+`。当 `n` 足够大时，
`a=x-delta_n` 在 `K` 上有正下界。引理 YJ 对 Poisson kernel给

`(x-delta_n)/[(x-delta_n)^2+(y-t)^2]`

` <=C_K/(1+t^2)`,                                  (18)

故式 (17) 推出

`inf_(z in K)Re F_n(z)>=-C_KJ_n/pi=o(1)`.          (19)

取一个连接 `U` 内基点与 `K` 的 relatively compact disk chain。把式 (19)
加上统一小常数后，每个 disk 上得到 positive-real function；Carathéodory
estimate 沿 disk chain、配合基点处 `F_n` 的有界性，给 `{F_n}` 在 `K` 上
一致有界。因此 Montel 给 normal family。

任意 subsequential limit 在 `U` 上都等于 `F_ar`，identity theorem说明所有
subsequences 极限相同，故整个序列 locally uniformly 收敛。令式 (19) 中
`n->infinity` 得 `Re F>=0`。最后应用定理 XQ。`□`

这是一条足够广的“广义结构定理”：对象只需有 self-dual entire divisor、
Euler/Gamma arithmetic germ、holomorphic regularizations、Poisson boundary
control 与一个 Cauchy-weighted defect。有限域 Hodge--Riemann 的 exact
positivity对应 `J_n=0`；数域只需 filtered `J_n->0`。

## 4. Abel--zeta 的 Poisson admissibility

对文档 132 的

`F_Y(z)=1/s-(1/2)logpi+(1/2)psi(s/2)+I_Y(s)-S_Y(s)`,

`s=1/2+z`,                                         (20)

固定 `Y,delta>0`。在闭半平面 `Re z>=delta`：

- finite/exponentially convergent prime current `S_Y` 有有限 uniform absolute
  bound；
- `|I_Y(s)|<=int_1^infinity u^(-1/2-delta)e^(-u/Y)du`；
- `Re psi(s/2)=log|s/2|+o(1)` 沿大半圆一致。

所以 `Re F_Y(z)->+infinity` 沿该半平面的大半圆。令 boundary negative part
为 `W_(Y,delta)`；Poisson integral `P[W]` 的 boundary value为 `W`，且趋于零。
对 `Re F_Y+P[W]` 在半圆使用 minimum principle，再令半径趋于无穷，得到
式 (17)。因此 Abel candidates 无条件满足定理 YL 的第一项；在
`Re z>1/2` 的 Euler absolute-convergence开集也满足第二项。

于是得到 zeta 的具体充分条件：若存在 `Y_n->infinity`, `delta_n->0` 使

`J_(Y_n,delta_n)=int_R[-Re F_(Y_n)(delta_n+it)]_+/(1+t^2)dt->0`, (21)

则 RH 成立。注意式 (21) 是尚未证明的 RH-strength estimate，不能由数值趋势
代替。

## 5. 高频尾已无条件消失

文档 133--134 给，在

`T>=C_(delta,M)Ylog^3(YT)`                          (22)

之后的每个正或负 dyadic window，

`int_[T,2T]W_(Y,delta)(t)dt`

` <=C_M delta^(-3)T/logT`.                         (23)

### 推论 YM（Cauchy defect 的 high-tail bound）

在式 (22) 下，

`int_(|t|>=T)W_(Y,delta)(t)/(1+t^2)dt`

` <=4C_M delta^(-3)/(TlogT)`.                      (24)

#### 证明

在 `[2^kT,2^(k+1)T]` 上 Cauchy weight至多 `(2^kT)^(-2)`；式 (23)
给该窗口至多

`C_Mdelta^(-3)/[2^kT log(2^kT)]`。

对 `k>=0` 求和至多首项的两倍，再对正负高度乘二。`□`

所以只要 `delta^3TlogT->infinity`，式 (21) 的 high tail无条件趋零。经典 RH
存在性问题最终缩成

`int_(|t|<T_Y)[-Re F_Y(delta_Y+it)]_+/(1+t^2)dt->0`, (25)

其中 `T_Y` 可取满足式 (22) 的起始高度。这比未加权负质量或 core rank严格更
接近 arithmetic cyclic family：移动到高度 `T` 的负质量会自动受到 `T^-2`
惩罚。

## 6. 数值 audit 与分辨率边界

新增实现：

- `cauchy_resolvent_weight_constant`：引理 YJ 的 exact constant；
- `cauchy_weighted_core_gram_bound`：定理 YK 的 finite Gram majorant；
- `abel_cauchy_high_tail_bound`：推论 YM 的 two-sided dyadic账本；
- `zeta_abel_cauchy_negative_mass_audit`：在 `[0,H]` 扫描后利用 real type
  作 symmetric composite trapezoid，并输出式 (1) 与指定 resolvent 的
  diagonal negative energies。

所有 sampled integral 都是非区间网格诊断。

固定 `delta=.1`, cutoff `N=40Y`, `H=2Y`，得到：

| `Y` | step | sampled full-line `J_Y(H)` | sampled positive-half negative mass |
|---:|---:|---:|---:|
| 10 | .25 | `1.8226e-1` | `2.1132e-1` |
| 30 | .25 | `5.6303e-2` | `2.3983e-1` |
| 100 | .25 | `1.1606e-2` | `2.7079` |
| 300 | .50 | `3.7581e-3` | `10.249` |

未加权负质量随 `Y` 增大，Cauchy-weighted defect却明显下降，符合“负井向高频
逃逸”的机制。对 `Y=100,step=.25`，把 `H` 从 `Y,2Y,4Y,8Y` 扩大时，
`J_Y(H)` 为

`0.0114845, 0.0116056, 0.0116421, 0.0116537`.       (26)

在 `H=2Y` 把 step从 `.25` 减至 `.125` 得 `0.0116723`，说明该尺度上的趋势
对网格已有一定稳定性，但仍不是 rigorous quadrature enclosure。尤其不能从
表格外推式 (21)，也不能由有限已验证 zero高度替代全频估计。

## 7. 下一解析输入

新的逻辑边界为

`Abel arithmetic candidates`

` + Poisson minimum principle`

` + high-tail Cauchy defect ->0`

` + low/intermediate weighted defect (25) ->0`

` => normal passive limit => Pick positivity => RH`.                (27)

下一步应直接研究式 (25)，而不是再估 core dimension。可能的严格入口有：

1. 对 `[-T_Y,T_Y]` 使用 smooth Cauchy kernel的 Fourier transform
   `pi e^(-|u|)`，把 weighted second moments变成 log-frequency 上的正
   exponential kernel；
2. 对 negative part使用 convex dual
   `v_- = sup_(0<=theta<=1)(-theta v)`，寻找由 primes定义且可被
   large-sieve/Poisson控制的 dual density；
3. 证明负井中心随 `Y` 至少线性逃向 infinity，并对固定低高度建立 uniform
   Abel convergence；二者与式 (24) 拼接。

任一路线若给出 (25)，定理 YL 已完成从该估计到广义 Weil 结构与中心线的
全部 functional-analytic 桥接。
