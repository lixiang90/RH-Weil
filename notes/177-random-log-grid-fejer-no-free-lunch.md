# NCE-3：随机 logarithmic grids、Fejér 恒等式与凸性 no-free-lunch

文档 174 把随机 dyadic/log partitions列为第三条探索路线。本笔记给出两个互补的
严格结果：

1. 随机平移等长 log-grid的平均 cell Gram恰好是 triangular/Fejér Gram；
2. 若随机 predictors全在同一个 closed convex arithmetic cone中，随机化的
   expected squared loss不可能优于确定性 barycenter。

所以概率方法不是新的能量来源。它能做的是非构造地选择一个好分区，或利用
boundary crossing的稀疏概率；若没有额外 boundary arithmetic，随机化只是文档
151--152 的 Fejér polarization的另一种表示。

## 1. 随机平移网格

固定 `h>0`。对 `theta` 在 `[0,h)` 上均匀分布，定义 cells

`I_(k,theta)=[theta+kh,theta+(k+1)h)`, `k in Z`. (1)

### 定理 AER（random-grid Fejér identity）[U]

对任意 `x,y in R`，

`P_theta{x,y lie in the same cell}`

` =(1-|x-y|/h)_+`.                              (2)

因此对有限 points `x_alpha` 与 coefficients `c_alpha in C`，

`E_theta sum_k`

` |sum_(x_alpha in I_(k,theta))c_alpha|^2`

` =sum_(alpha,beta)c_alpha conj(c_beta)`

`   (1-|x_alpha-x_beta|/h)_+`.                  (3)

右端是 positive semidefinite triangular/Fejér Gram。

#### 证明

若 `|x-y|>=h`，两点不可能同格。若 `0<=d=|x-y|<h`，一个长度 `h` 的随机
平移 cell同时包含两点，当且仅当 boundary没有落入它们之间长度为 `d` 的区间；
概率为 `1-d/h`，得式 (2)。展开 cell sums的平方、交换有限求和与期望，再应用
式 (2)得式 (3)。`□`

同样，

`P_theta{x,y are separated}`

` =min{1,|x-y|/h}`.                             (4)

取 `x_alpha=log q_alpha`，式 (3)正是 multiplicative near-product kernel

`(1-|log(q_alpha/q_beta)|/h)_+`.                (5)

因此随机 log-grid自动保持 Type II product collisions与全部 cross terms。

## 2. 非构造选择一个好网格

令

`E(theta)=sum_k`

` |sum_(x_alpha in I_(k,theta))c_alpha|^2`.      (6)

### 推论 AES（probabilistic grid selection）[U]

至少存在一个 `theta_* in [0,h)` 使

`E(theta_*)`

` <=sum_(alpha,beta)c_alpha conj(c_beta)`

`    (1-|x_alpha-x_beta|/h)_+`.                 (7)

#### 证明

非负函数不可能处处严格大于其平均值；结合定理 AER。`□`

这是一个真正的非构造选择：无需写出 `theta_*`。但右端就是 canonical Fejér
energy，所以式 (7)本身没有降低文档 152 的 physical Gram。它只允许把平均
polarization实现为一个确定 partition，便于随后使用 cellwise arithmetic。

## 3. 同一凸锥中的随机化不能改善平方损失

令 `H` 是实 Hilbert space，`K subset H` 是 nonempty closed convex set，
`X in H` 固定。设 `E_omega in K` 是 square-integrable随机变量，Bochner均值为

`Ebar=mathbb E_omega[E_omega] in K`.             (8)

### 定理 AET（convex randomization no-gain theorem）[U]

有精确 bias--variance decomposition

`E_omega ||X-E_omega||^2`

` =||X-Ebar||^2`

`  +E_omega||E_omega-Ebar||^2`,                 (9)

故

`E_omega ||X-E_omega||^2`

` >=dist(X,K)^2`

`   +E_omega||E_omega-Ebar||^2`.                (10)

除非随机 predictor几乎处处等于其均值，否则其 expected loss严格大于
deterministic barycenter的 loss。

#### 证明

写 `X-E_omega=(X-Ebar)-(E_omega-Ebar)`，展开平方并用
`E(E_omega-Ebar)=0` 消去 cross term，即得式 (9)。因 `K` convex且closed，
Bochner均值 `Ebar in K`，再得式 (10)。`□`

对文档 174 的 positive arithmetic cone `K_T`，式 (9)直接适用。这严格排除：

- 在不改变 cone或 carrier时，仅随机混合安全 predictors；
- 期待 convex clipped residual因随机符号或随机 basis自行下降；
- 把“存在一个 realization”误当成对平均 arithmetic energy的新估计。

## 4. 概率法何时仍可能有用

随机 partition只有在下列至少一项发生时才可能带来实质收益：

1. `K_(T,omega)` 随网格改变，而每个 realization有更稀疏的 boundary incidence；
2. arithmetic proof能使用式 (4)的 crossing probability，而不先取绝对值丢掉
   joint prime/continuum/Gamma cancellation；
3. 选出的 realization同时控制多个 blocks，而非每块任意换 gauge后再把
   incompatible predictors拼接；
4. random grid把文档 175 的 rank-one packet压到文档 176 的 commutator shell。

一个可证伪的目标是：对固定或 product probability space上的 shifts，

`E_omega sum_T K_T(epsilon,omega)`

` <=sum_T [GCD_T+Bdry_T]`,                      (11)

其中 `GCD_T` 由文档 166--167 的 profinite Gram控制，而 `Bdry_T` 使用式 (4)
得到可和 crossing probability。若右端有限，Tonelli给几乎处处总 residual有限，
再由 AEG推出中心线。

## 5. 与前两条路线的组合

文档 175把 finite polar obstruction约化为 rank-one product packet `u u^*`。
对 packet positions `x_alpha=log(d_alpha m_alpha)` 应用式 (3)，得到

`E_theta sum_k`

` |sum_(alpha in I_(k,theta))u_alpha|^2`

` =u^*K_hu`.                                    (12)

文档 176又把 diagonal cell/face insertion的失败量写成
`||[D,A_theta]||_HS^2`。随机化后，某条 face被 boundary切断的概率由式 (4)
给出。因此三条路线形成一个具体链条：

`rank-one separator`

` -> random cell packet`

` -> expected boundary crossing`

` -> incidence--Dirac commutator`

` -> harmonic/transgression residual`.          (13)

链条中仍缺的是对真实 Möbius/prime coefficients证明式 (11)，但每一步现在都有
有限、零点无关的定义。

## 6. 审计结论

本笔记无条件证明：

- random shifted log-grid与 Fejér Gram的精确等价；
- 一个好 grid realization的非构造存在；
- 同一 convex arithmetic cone内随机化的严格 no-gain；
- boundary crossing probability的精确公式。

下一步只应研究“随机网格是否降低 threshold commutator shell capacity”，不应再
把随机化本身视为能量估计。若 expected shell capacity仍等于 full near-product
Gram，NCE-3应降级为 Fejér polarization的表示定理。
