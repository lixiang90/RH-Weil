# 冻结整数 Vaughan 通道、principal-angle 稳定性与 out-of-sample 审计

文档 157 的公共二维 basis由四个被审计 blocks共同拟合，因而仍可能存在 data
leakage。本节完成两个更严格的检查：

1. basis只由两个小训练 blocks生成，再用于未见过的高度和更大 Abel scales；
2. 把 basis完全冻结成两个整数种子，经 Gram--Schmidt 后不再重新拟合。

同时证明 fixed projector与每块 leading spectral projector之间的 principal angle
如何控制 tail edge和 core--tail coupling。这把“basis稳定”变成可进入文档 157
Feshbach capacity的定量输入。

## 1. Fixed projector 的 tail bound

令 `G>=0` 在 `R` 维 component space上有 eigenvalues

`lambda_1>=...>=lambda_R>=0`.                     (1)

令 `P_*` 为前 `q` 个 eigenvectors的 spectral projector，`P` 为任意 fixed rank-`q`
projector，并记

`s=||P-P_*||=sin(theta_max)`.                      (2)

置 `Q=I-P`，相对 `P+Q` 写

`G=[[A,B],[B^*,C]]`.                               (3)

### 定理 ABQ（principal-angle tail and coupling bounds）

有

`||C||<=lambda_(q+1)`

`       +(lambda_1-lambda_(q+1))s^2`,             (4)

以及

`||B||<=2lambda_1s`.                               (5)

#### 证明

对 unit `x in Ran Q`，因为 `Px=0`，

`||P_*x||=||(P_*-P)x||<=s`.                       (6)

在 `P_*+Q_*` spectral decomposition中，

`<Gx,x><=lambda_1||P_*x||^2`

`             +lambda_(q+1)(1-||P_*x||^2)`,      (7)

取 supremum并用式 (6)得到式 (4)。又因 `P_*GQ_*=0`，

`PGQ=(P-P_*)GQ+P_*G(Q-Q_*)`,                     (8)

两项 norm各至多 `lambda_1s`，得到式 (5)。`□`

式 (4)对 angle是二阶稳定，式 (5)对 angle是一阶稳定。实际 Feshbach correction
是 coupling的平方，所以最终仍是 `s^2` 量级。

## 2. Frozen-projector Feshbach criterion

取

`c_angle=lambda_(q+1)`

`       +(lambda_1-lambda_(q+1))s^2`,             (9)

并选 `epsilon>c_angle`。文档 157 的 core correction满足

`||B(epsilon I-C)^(-1)B^*||`

` <=4lambda_1^2s^2/(epsilon-c_angle)`.            (10)

### 定理 ABR（angle-stable frozen-channel Weil theorem）

在文档 157 定理 ABP的 Gamma--Euler hypotheses下，若存在一个 fixed rank-`q`
projector `P`，使每个 core block可选 `epsilon_(Y,k)>c_angle(Y,k)`，且

`sup_Y sum_k 1/beta_(Y,k) {`

` x^*A x`

` +[4lambda_1^2s^2/(epsilon-c_angle)]||x||^2`

`                         +epsilon||y||^2}<infinity`, (11)

则全部 zeros位于中心线。

#### 证明

式 (4)给 `epsilon I-C>0`；式 (5)与 resolvent norm
`<=(epsilon-c_angle)^(-1)` 给式 (10)。因此式 (11) majorize文档 157 式 (12)，
应用定理 ABP。`□`

ABR 把 fixed-channel存在性问题分成四个可辨认量：leading core energy、spectral
tail `lambda_(q+1)`、principal angle `s` 与 chosen threshold。它不要求逐块 basis
恰好对角化 `G`。

## 3. Algebraic seed realization

给 component label space `K^R` 中 `q` 个 linearly independent seeds

`a_1,...,a_q in K^R`,                             (12)

其中 `K` 可取 `Q`、number field或 coefficient involution固定域。对 seeds按固定
顺序作 Gram--Schmidt，并以标准坐标依次完成 orthonormal basis。

### 定理 ABS（seeded component-channel structure）

式 (12)规范产生 rank-`q` projector `P_a` 与 unitary completion；它只依赖 component
labels和 seeds，不依赖 zeros、height或 Abel scale。若 `P_a` 满足定理 ABR式 (11)，
则对应 zeta function满足中心线结论。

对每个 finite Euler/Abel section，`P_a`、Feshbach blocks、principal angle与式
(4)--(5)全部可由 finite positive Grams计算。因此 seeded structure的有限层存在性
是无条件的；开放部分仅是 uniform capacity bounds。

#### 证明

Gram--Schmidt在 seeds线性独立时给 orthonormal `q`-frame；依预定标准坐标完成后
得到 unitary basis。projector显然与 analytic divisor无关。最后应用定理 ABR。
`□`

实现 `orthonormal_channel_basis_from_seeds` 完成该构造；
`channel_projector_stability_certificate` 返回式 (2)、actual/bounded tail edge及
actual/bounded coupling norm。

## 4. Zeta 的冻结整数候选

在 component order

`(Type-I log, Type-I correction, Type-II, low prime power)` (13)

下，取整数 seeds

`a_1=(17,-1,4,10)`,

`a_2=(3,-17,-10,-2)`.                              (14)

它们是文档 157 finite common basis的粗整数化，线性独立，故定理 ABS无条件给一个
固定实二维 projector。必须强调：式 (14)目前是 data-suggested candidate，不是从
Vaughan convolution algebra推导出的 canonical weights。

### 定理 ABT（frozen integer-channel conditional RH criterion）

若式 (14)产生的 fixed projector对 zeta Vaughan simplex Grams满足定理 ABR式
(11)，则 RH成立。

式 (14)的 projector、每个 finite Feshbach majorant及其 Loewner positivity均不使用
zeros，故 finite结构无条件存在；未证的是 cofinal uniform bound。

#### 证明

这是定理 ABS与 ABR对 zeta四 component identity的 specialization。`□`

ABT 与“抽象地假设某个二维 basis存在”不同：basis已被两个整数 vectors完全固定。
它也不是 RH证明，因为式 (11)尚未建立。

## 5. Out-of-sample 设计

训练 basis只使用

`(N,Y,T)=(80,30,2),(80,30,8)`,                    (15)

并固定为

`u_1 approximately(.829,-.067,.219,.510)`,

`u_2 approximately(.131,-.855,-.487,-.116)`.      (16)

测试 blocks没有参与式 (16)的 PCA。对每个测试 block分别计算：

- training-PCA basis的 strict Feshbach upper；
- integer seeds式 (14)的 strict Feshbach upper；
- 与该 block leading rank-two projector的 principal sine；
- 定理 ABQ的 tail/coupling bounds。

| test `(N,Y,T)` | PCA excess | integer excess | PCA `sin theta` | integer `sin theta` |
|---:|---:|---:|---:|---:|
| `(80,30,4)` | `.0034%` | `.0202%` | `.0173` | `.0303` |
| `(80,30,16)` | `.0384%` | `.0294%` | `.0399` | `.0383` |
| `(160,60,4)` | `.1188%` | `.0213%` | `.1071` | `.0975` |
| `(160,60,16)` | `.0033%` | `.0079%` | `.1223` | `.1110` |
| `(240,90,8)` | `.0003%` | `.0042%` | `.0272` | `.0583` |

所有 Feshbach majorants都直接验证 `M-G>=0`。训练 basis的最大 excess低于 `.12%`；
完全冻结整数 basis的最大 excess低于 `.03%`，且在较大的 `N=160` tests上反而更
稳定。这降低了“文档 157效果完全来自同样本拟合”的可能性。

定理 ABQ的 tail bound也相当接近实际值。例如 PCA basis在五块上的

`actual tail / angle upper`

依次约为

`.024540/.024573`, `.006092/.006133`,

`.039624/.042292`, `.009816/.010744`,

`.023835/.023838`.                                 (17)

coupling bound `2lambda_1s` 较实际 coupling松约数倍，但全部方向正确并足以形成
严格证书。

## 6. 证据边界与下一步

Out-of-sample tests仍是有限 diagnostics：

- training与 integer seeds都源自同一早期数据探索；
- 测试只有五个 blocks，不覆盖全部 dyadic heights；
- midpoint continuum、finite prime cutoff及其 tails尚未共同做 interval enclosure；
- principal sine在 `N=160` 可达 `.12`，尚未证明趋零或保持统一小量。

下一步是从恒等式而非拟合解释式 (14)：

1. 对四个 Vaughan components计算连续主项的 coefficient matrix；
2. 检查式 (14)是否近似该 matrix的 image/kernel singular vectors；
3. 若是，解析证明 fixed projector的 angle bound；
4. 若否，扩大 out-of-sample blocks并寻找反例，而不继续美化候选；
5. 将 prime/continuum vector error经文档 156 定理 ABJ加入整数-basis Feshbach
   certificate。

