# `delta->0` renormalization 与 passive Hodge index

文档 133 在固定横向 compact `delta<=Re z<=M` 上，把 Abel impedance 的
负 resonance 压缩成相对 Shannon dimension与余空间误差同时趋零的
weighted-prolate core；但其中常数在 `delta downarrow0` 时发散。本节显式
计算发散阶，得到一个可同时令 `T->infinity`、`delta->0` 的对角日程。

核心结果是：zeta/von Mangoldt coefficients 的 metric constant 至多
`delta^(-3)`。因此只要

`delta^3 log T -> infinity`,                        (1)

余空间负误差与负惯性指数的相对密度仍同时趋零。对
`delta=(log T)^(-alpha)`，允许任意 `alpha<1/3`。同一结论适用于固定 degree
tempered Euler data，degree只进入常数。

这无条件构造了一个趋向中心轴的 **density-polarized Weil package**；它仍不
证明 RH，因为 density-zero core中可能保留少数 off-center divisor。要得到
真正中心线定理，还必须证明这些 cores 对全部 arithmetic cyclic vectors
消失，或直接认证其有限 Feshbach blocks 非负。

## 1. 横向 metric constant 的显式阶

文档 133 的 Abel coefficient square mass满足

`B_2(Y,x)<=sum_(n>=2)(log n)^2n^(-1-2delta)`,       (2)

其中 `x>=delta>0`。

### 引理 YC（explicit horizontal square-mass majorant）

对每个 `delta>0`，

`sum_(n>=2)(log n)^2n^(-1-2delta)`

` <=(log 2)^2/delta+1/(2delta^3)`.                 (3)

特别地，对 `0<delta<=1`，右侧不超过 `delta^(-3)`。

#### 证明

在区间 `x in[n-1,n]` 上，

`log(x+1)>=log n`, `x^(-1-2delta)>=n^(-1-2delta)`, (4)

故离散和至多

`int_1^infinity log(x+1)^2x^(-1-2delta)dx`.         (5)

使用

`log(x+1)<=log2+logx`,

`(a+b)^2<=2a^2+2b^2`,                              (6)

以及

`int_1^infinity x^(-1-2delta)dx=1/(2delta)`,

`int_1^infinity(log x)^2x^(-1-2delta)dx`

` =2/(2delta)^3=1/(4delta^3)`,                      (7)

得到式 (3)。当 `delta<=1`，
`(log2)^2delta^2+1/2<1`，给最后一项。`□`

指数 `3` 来自 logarithmic derivative coefficient 的一个 `log n`，平方后
形成二阶 log moment。对普通 bounded Dirichlet coefficients，相应指数会更小；
对更高 log weights则按同一 Mellin moment规则增大。

## 2. Balanced cofinal core

把文档 133 定理 XZ 的常数写成显式形状

`int_T^(2T)W_(Y,x,T)(t)dt`

` <=C_M delta^(-3)T/log T`,                         (8)

其中其它 archimedean/window constants吸收到固定 `C_M`。定理 YA 对 tolerance
`epsilon` 给

`dim Q/(BT/pi)<=C_M delta^(-3)/(epsilon log T)`.    (9)

### 定理 YD（renormalized cofinal Abel core）

令 `delta=delta(T) in (0,1]`，并假设文档 133 的 window-size 条件对
`Y=Y(T)` 成立。取

`epsilon_(delta,T)`

` =sqrt(C_M/(delta^3log T))`.                       (10)

则存在 weighted-prolate core `Q_(Y,delta,T)`，使

`dim Q/(BT/pi)<=epsilon_(delta,T)`,                 (11)

且在其正交补上负误差至多

`epsilon_(delta,T)||f||^2`.                         (12)

因此若式 (1) 成立，core相对 dimension与余空间负误差同时趋零。特别地，

`delta(T)=(log T)^(-alpha)`, `0<alpha<1/3`,         (13)

给共同速率

`O((log T)^((3alpha-1)/2))`.                        (14)

#### 证明

把式 (10) 代入式 (9)，右侧恰等于式 (10)；定理 YA 同时给余空间误差
`epsilon`。式 (1)、(13)--(14) 直接计算。`□`

这解决了文档 133 所列的“`delta->0` metric constants必然发散”问题在
**相对秩/余空间**层面的 renormalization：不需要固定 `delta`，只需不能比
`(log T)^(-1/3)` 更快地冲向中心轴。

## 3. Negative inertia is controlled by the same trace

令 `A>=0` 是任意 bounded positive operator，`C_W>=0` 是文档 133 的
weighted concentration operator，并令

`H=A-C_W`.                                          (15)

记 `N_(-infinity,-epsilon)(H)` 为 `H` 小于 `-epsilon` 的 eigenvalue数目，
按 multiplicity计。

### 定理 YE（passive Hodge-index bound）

对每个 `epsilon>0`，

`N_(-infinity,-epsilon)(H)`

` <=N_(epsilon,infinity)(C_W)`

` <=Tr(C_W)/epsilon`

` =B/(pi epsilon)int W(t)dt`.                       (16)

#### 证明

令 `Q` 是 `C_W` 的 spectral projection `1_(epsilon,infinity)(C_W)`。
在 `Q^perp` 上 `C_W<=epsilon I`，而 `A>=0`，所以

`H|_(Q^perp)>=-epsilon I`.                          (17)

min--max principle说明 `H` 在 `-epsilon` 以下的 dimension不超过 `dim Q`。
positive eigenvalues of `C_W` 的和是 trace，所以
`epsilon dim Q<=Tr C_W`。文档 133 式 (26) 给最后一个等号。`□`

### 推论 YF（cofinal negative-index density）

在定理 YD 的日程下，

`N_(-infinity,-epsilon_(delta,T))(H)/(BT/pi)`

` <=epsilon_(delta,T)`.                             (18)

所以当 `delta^3logT->infinity` 时，显著负 eigenvalues的相对 Hodge index与
其允许阈值同时趋零。

这比“负井测度趋零”严格得多：它直接控制 bandlimited Hodge operator 的
negative inertia。然而它仍允许每个 scale保留有限或 density-zero 的负方向；
RH 需要最终一个也不剩。

## 4. Fixed-degree tempered Gamma--Euler extension

设 completed self-dual degree-`d` Euler data 的 logarithmic coefficients满足

`|b(n)|<=d Lambda(n)`                               (19)

（unitary/tempered local parameters的固定 degree分解给出这一粗界）。则

`sum_n|b(n)|^2n^(-1-2delta)e^(-2n/Y)`

` <=d^2delta^(-3)`.                                 (20)

所以定理 XZ、YD、YE逐字成立，只需把 `C_M` 换成 `d^2C_(M,d)`；balanced
scale成为

`epsilon_(d,delta,T)=O_d((delta^3logT)^(-1/2))`.     (21)

因此对任何固定 degree 的 primitive Dirichlet/tempered automorphic
Gamma--Euler package，只要已知 pole continuum正确减去，均得到相同的
cofinal density-polarized structure。non-tempered或 degree随 conductor增长的
family需要另行追踪式 (19) 的常数，不能自动套用固定 `d` 结论。

## 5. 计算账本

新增：

- `abel_coefficient_square_mass_majorant`：式 (3) 与 `delta^3` normalization；
- `abel_cofinal_scaling_ledger`：给定 window mass prefactor，计算式 (10)--(12)
  的 balanced scale；
- `weighted_hodge_inertia_density_bound`：定理 YE 的 negative-index、Shannon
  dimension 与相对密度账本；
- `weighted_prolate_core_rank_bound` 现在同时返回 significant negative
  inertia bound。

例如 `delta=0.1`, `log T=10^6`，式 (3) 给 square-mass majorant约
`504.80`。若 window prefactor取 `2`，balanced tolerance与相对 core bound
均约 `0.0318`，而 `delta^3logT=1000`。这只是 scaling ledger；实际 theorem
应用必须把解析证明中的真实 prefactor传入，不能默认为 `1`。

## 6. 逻辑边界：density polarization 不是 purity

目前无条件存在的结构已经达到：

`a=1/2 outer exact passivity`

` + Abel arithmetic continuation toward a=0`

` + delta(T)->0 renormalization`

` + complement error ->0`

` + relative negative Hodge index ->0`.            (22)

但 Weil 猜想的 RH 机制要求 exact positive polarization，不是“几乎所有方向
为正”。一个 density-zero primitive sector仍可承载全部 off-center zeros；
determinant-line residue对少数方向也不会稀释。因此不能从式 (18) 宣称 RH。

下一步必须把相对指标升级为 **cyclic invisibility或absolute index zero**：

1. 证明每个 fixed arithmetic kernel vector投到 negative core 的 norm趋零；
2. 或证明 core residual Gram trace本身为 `o(1)`，而非除以 Shannon dimension
   后才趋零；
3. 或在 core 上构造新的 positive intersection form并用 Feshbach shorting
   认证最小 eigenvalue非负。

其中第 1 项最接近文档 015 filtered Weil theorem：若一个 separating cyclic
test family对全部 negative cores渐近不可见，再结合余空间误差 `o(1)`，即可
把极限 form提升为精确正性并由文档 131 定理 XQ推出 RH。
