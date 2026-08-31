# Cofinal stationary discretization 与完全有限充分判据

文档 142 把 finite capped problem化成 boundary symbol的 Cauchy negative part，
但 numerical audit仍包含两类分辨率误差：shared lag quadrature与 height
integration。本节证明可以给出一个完全显式、虽极保守的 polynomial cofinal
schedule，使这些误差 **无条件** 趋零。

所以经典 RH 的剩余项不再包括“是否能有限化”：有限化已经有确定日程。本节
先以 negative Cauchy mass趋零给出 passive sufficient criterion；文档 145随后
证明，仅需该质量沿一条 cofinal schedule一致有界就已足以推出中心线。

## 1. 显式日程

令 `Y->infinity`，写 `ell=logY`，并取

`delta_Y=1/(4+sqrt(ell))`,                          (1)

`N_Y=ceil(Yell^2)`,                                (2)

`tau_Y=Y^(-4)`, `L_Y=3ell`,                        (3)

`M_Y=ceil(Y^4ell^2)` shared geometric lag cells， (4)

以及 height参数

`T_Y=Y^4`, `h_Y=Y^(-4)`,                           (5)

即约 `2Y^8` 个 height cells。

该日程远大于实际 audit需要，不是计算建议；它只用于证明 finite approximation
不是逻辑障碍。注意

`delta_Y->0`, `delta_YlogY~sqrt(logY)->infinity`.  (6)

后一条件也与文档 132 的 Abel zero-wave damping方向一致。

## 2. Lag mesh error 无条件消失

对文档 142 shared weight，total variation有初等 majorant

`int_(tau_Y)^infinity|w_(Y,sigma)(lambda)|dlambda`

` <=Y^(1-sigma)Gamma(1-sigma)`

` +(1/2)log(1/tau_Y)+C`                            (7)

` =O(Y^(1/2)+logY)`.                               (8)

这里 continuum取 full mass；residual Gamma在 `[tau,1]` 用
`1-e^(-2lambda)>=2lambda e^(-2lambda)`，故至多 `1/(2lambda)`，在
`[1,infinity)` 指数可积。

geometric mesh的最大 cell width满足

`Delta_Y<=L_Y log(L_Y/tau_Y)/M_Y=O(Y^(-4))`.       (9)

文档 141 定理 ZD 给

`omega(Delta_Y/2)=O(Y^(-4)logY)`.                 (10)

故全部 shared cells误差至多

`O((Y^(1/2)+logY)Y^(-4)logY)=o(1)`.               (11)

### 定理 ZL（unconditional vanishing shared-discretization error）

沿式 (1)--(4)，文档 142 定理 ZH 的：

- shared cell error；
- Gamma origin error；
- pole/continuum origin error；
- Gamma、continuum与prime tails

全部趋零。

#### 证明

cell error由式 (7)--(11)。Gamma origin为
`O(sqrt(tau_Y))=O(Y^(-2))`；其它 origin mass为 `O(tau_Y)` 再乘
`omega(tau_Y)`。在 `L_Y=3logY`：Gamma tails为 `O(Y^(-6))` 或更小；
continuum incomplete-gamma参数 `e^L/Y=Y^2`，故 superexponential小。
prime cutoff满足 `N_Y/Y=log^2Y`，用 `Lambda(n)<=logn` 的 integral
majorant给 `Y^O(1)e^(-log^2Y)=o(1)`。`□`

## 3. Height symbol ledger 也无条件消失

finite symbol写成

`P_Y(t)=Re sum_jc_(Y,j)e^(-itlambda_(Y,j))`.       (12)

由 `Lambda(n)<=logn`、式 (7)及 `lambda_j<=O(logY)`，有粗界

`C_Y=sum_j|c_(Y,j)|=O(Y^(1/2)logY)`,               (13)

`D_Y=sum_j|c_(Y,j)||lambda_(Y,j)|`

` =O(Y^(1/2)log^2Y)`.                              (14)

文档 142 定理 ZK在式 (5) 下给 grid error

`D_Yh_Y/2=O(Y^(-7/2)log^2Y)=o(1)`,                (15)

而 Cauchy tail mass `O(T_Y^(-1))`，所以 tail error

`C_Y/T_Y=O(Y^(-7/2)logY)=o(1)`.                   (16)

### 定理 ZM（fully finite stationary sufficient criterion）

沿式 (1)--(5)，令 `v_Y^sample` 是 exact Cauchy cell masses乘
`min(P_Y(mid),0)` 的有限和。若

`v_Y^sample>=-epsilon_Y`, `epsilon_Y->0`,          (17)

则 RH成立。

同样地，对满足文档 138--142 hypotheses的一般 fixed-degree self-dual
Gamma--Euler/Selberg orbit data，只要 coefficient total mass与最大 length至多
polynomial增长，就可加大式 (4)--(5) 的 powers取得同一 fully finite criterion。

#### 证明

定理 ZL与式 (15)--(16)说明 arithmetic quadrature、height grid和所有 tails
总误差为 `o(1)`。式 (17)故推出完整 Hodge functional在 Cauchy-capped cone上
`>=-o(1)`；应用文档 139 定理 YY与文档 131 positive-real Weil theorem。`□`

定理 ZM 不假定 RH，但其条件 (17) 仍有 RH强度；新增内容是把它变成一列完全
有限、只使用 primes/Gamma 与 elementary error bounds的判据。文档 145 定理
ZV把式 (17)进一步放宽为 `inf_Y v_Y^sample> -infinity`。

## 4. 固定分辨率 audit 的含义

实现 `zeta_abel_shared_stationary_certificate` 组合 shared arithmetic quadrature
与 stationary symbol lower ledger；`abel_shared_cofinal_discretization_schedule`
生成式 (1)--(5) 及 mesh/tail scaling账本。height symbol计算已分块，避免
prime nodes增长时构造完整 height-by-lag外积。

固定 `delta=.1`、`N=40Y`、128 lag cells、height cutoff `8Y` 与固定 height
step `.05`，得到：

| `Y` | sampled stationary minimum | stationary error | arithmetic error |
|---:|---:|---:|---:|
| 2 | `-.2328` | `.2355` | `.0986` |
| 5 | `-.1112` | `.2164` | `.2492` |
| 10 | `-.0580` | `.3075` | `.4920` |
| 30 | `-.0217` | `.7077` | `1.2554` |

sampled negative mass稳定下降，和文档 136 的直接 boundary audit一致；errors
增长是因为分辨率固定。对 `Y=30` 把 lag cells从 128增到 1024，arithmetic
error从 `1.255` 降到 `.273`，验证了 mesh refinement方向，但尚未进入式
(4) 的保守渐近区。

这些非区间数字只用于确认 scaling机制，不能验证式 (17)。

## 5. 剩余数学输入

经过文档 131--143，结构链已经达到：

`self-dual divisor + Euler/Gamma germ`

` -> Abel holomorphic candidates`

` -> inner orbit semigroup + Cauchy spectral cap`

` -> exact stationary negative-part variational problem`

` -> explicit fully finite cofinal tests`

` -> positive-real continuation -> center-line zeros`.             (18)

全部 functional-analytic、operator、outer-factor、finite-discretization箭头都已
证明。本节的 passive版本剩余输入是式 (17)；对仅需中心线的最弱当前版本，
文档 145说明只需一个 arithmetic inequality给 finite symbols的 Cauchy negative
mass统一 `O(1)`。

下一步不应再继续加大 brute-force grids；应研究 finite symbol本身的结构，例如：

1. 用 explicit Mellin/zero-wave expansion识别 off-line zero会在式 (17) 中留下
   何种稳定 lower obstruction；
2. 在不引用 zeros的情况下，用 prime-continuum discrepancy对 negative set作
   one-sided large-sieve或 entropy bound；
3. 对 fixed-degree L-functions追踪 conductor与Satake coefficient对式
   (13)--(14) 的影响，形成 GRH uniform family版本。
