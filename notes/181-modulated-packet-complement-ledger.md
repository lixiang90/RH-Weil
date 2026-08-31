# Modulated packet compression、补空间 ledger 与余维障碍

文档 180 把 cell cone 的遗漏方向放入 trace-norm remainder。本笔记进一步把
这个 remainder 拆成三个可审计量：packet compression 的负谱、补空间的负谱，
以及 packet--complement coupling。这个拆分揭示一个 sharp obstruction：若有符号
流在 height sample basis 中是对角乘法算子，那么每格只取一个复调制向量并不会
因相位而获得额外捕获；在常值负块上，它只能看见该格总负谱的 `1/M`。

因此“加入 modulation”本身不是修复。构造性路线必须证明补空间近似正，或在每格
加入与格维数同阶的独立模式。与此同时，谱定理总能非构造地选出最优 packet
subspace，但这种选择直接依赖未知负谱，不能充当算术构造。

## 1. Packet--complement block decomposition

令 `H=H^* in M_d(C)`，`P` 为 orthogonal projection，`Q=I-P`。把

`H_P=PHP|_(Ran P)`, `H_Q=QHQ|_(Ran Q)`              (1)

看成两个 compression。记 `Tr(A_-)=sum_lambda (-lambda)_+`。

### 定理 AFE（exact block negative ledger）[U]

有双边估计

`Tr((H_P)_-) <= Tr(H_-)`                         (2)

以及

`Tr(H_-) <= Tr((H_P)_-)+Tr((H_Q)_-)`

`             +2||PHQ||_1`.                     (3)

式 (3) 中的最后一项精确等于 block-off-diagonal remainder 的 trace norm：

`||PHQ+QHP||_1=2||PHQ||_1`.                      (4)

#### 证明

finite-trace variational formula 给

`Tr((H_P)_-)=sup_(0<=A<=P)-Tr(HA)`

`            <=sup_(0<=A<=I)-Tr(HA)=Tr(H_-)`,   (5)

得到式 (2)。令

`E_P(H)=PHP+QHQ`.                                (6)

文档 180 的 negative-part Lipschitz inequality 给

`Tr(H_-)<=Tr((E_PH)_-)+||H-E_PH||_1`.            (7)

第一项是两个对角块的负谱迹之和。相对于
`Ran P direct-sum Ran Q`，余项是

`[[0,PHQ],[QHP,0]]`.                             (8)

它的非零特征值为 `+-s_j(PHQ)`，故其 trace norm 是式 (4)，代入式
(7) 即得式 (3)。`square`

这个定理比只保留 off-cell norm 更适合设计实验：若只计算 packet block，所得量是
完整负谱的下界，而不是上界。要得到 Weil criterion，补块与 coupling 都不能省略。

## 2. 一格一个复调制 packet

令 height 格 `I` 含 `M` 个 samples，

`H_I=diag(h_1,...,h_M)`, `h_j in R`.             (9)

取任意正 weights `w_j`，`sum_j w_j=1`，以及任意 phases `theta_j`，定义

`v_j=sqrt(w_j) exp(i theta_j)`, `P_v=vv^*`.      (10)

记

`mu=sum_j w_jh_j`,

`sigma^2=sum_j w_jh_j^2-mu^2`.                  (11)

### 定理 AFF（phase-blind cell ledger）[U]

对上述 diagonal signed current，

`v^*H_Iv=mu`,                                   (12)

`||P_vH_I(I-P_v)||_1=sigma`.                    (13)

因此 packet response 和 packet--complement coupling 都只依赖
`|v_j|^2=w_j`，与 modulation phases 完全无关。

#### 证明

式 (12) 直接由对角性得到。因为 `P_vH_I(I-P_v)` 的秩至多一，trace norm
等于 Hilbert--Schmidt norm；其平方为

`||(I-P_v)H_Iv||^2`

` =v^*H_I^2v-|v^*H_Iv|^2=sigma^2`.              (14)

这也证明式 (13)。`square`

对不交 cells 取 orthogonal direct sum 后，式 (13) 的 trace norm逐格相加。
所以调节 `n^(-iT)` 相位不能降低 diagonal height-current 的这个 remainder；
必须改变 amplitudes、加入多个独立 cell modes，或使用真正非对角的 joint current。

## 3. Sharp codimension no-go

设一格中 `H_I=-aI_M`，`a>0`，而 `P` 是任意 rank-`r` projection。

### 定理 AFG（constant-negative multiplicity obstruction）[U]

精确地

`Tr((PHP)_-)=ar`,                                (15)

`Tr((QHQ)_-)=a(M-r)`,                           (16)

`PHQ=0`.                                        (17)

所以 rank-`r` packets 至多捕获该格负谱质量的 `r/M`。特别地，每格一个
modulated packet 的 capture fraction 恰为 `1/M`，无论怎样选相位。

这个结论排除了如下希望：用固定数目的 random shifts 或 vertical modulations，
在不断增长的 cell dimension 中自动得到完整 negative-index upper bound。若没有
独立的 complement positivity，packet rank 必须与有效负谱 multiplicity 同阶。

## 4. 非构造最优 packet subspace

把 `H` 的特征值按

`lambda_1<=...<=lambda_d`                       (18)

排列。

### 定理 AFH（Ky Fan optimal negative compression）[U]

对 `0<=r<=d`，

`max_(rank P=r) Tr((PHP)_-)`

` =sum_(j=1)^r (-lambda_j)_+`.                  (19)

最优 `P` 可取为最低 `r` 个 eigenvectors 的 span。若
`r>=rank(H_-)`，取 `P=1_(-infinity,0)(H)`，则 coupling 为零、补块半正定，
并完整捕获 `Tr(H_-)`。

#### 证明

由式 (5)，固定 `P` 时

`Tr((PHP)_-)=sup_(0<=A<=P)-Tr(HA)`.             (20)

再对 rank-`r` 的 `P` 取上确界，等价于对所有 rank至多 `r` 的 effects取上
确界。Ky Fan variational principle 选择 `-H` 最大的正特征方向，得到式
(19)。`square`

定理 AFH 说明“好 packet subspace 的存在”在纯算子层面从来不是问题；问题是该
subspace 是由 `H` 的未知负谱投影定义的。若把它直接用于 zeta current，就只是把
RH 所要排除的负方向重新命名。若要有效，必须证明一个由 Euler/Gamma/incidence
数据预先生成的算术代数能在不读取 zeros 的情况下逼近这个谱投影。文档 182
给出这种 order-density 路线的精确定理。

## 5. Constructive block criterion

对 dyadic block `T`，令 `H_T` 是 joint prime--continuum--Gamma current，
`P_T` 是由显式 complex arithmetic packets 生成的 projection，`Q_T=I-P_T`。
定义

`N_T=Tr[((P_TH_TP_T)|_(Ran P_T))_-]`,            (21)

`R_T=Tr[((Q_TH_TQ_T)|_(Ran Q_T))_-]`,            (22)

`C_T=2||P_TH_TQ_T||_1`.                         (23)

由定理 AFE，

`Tr((H_T)_-)<=N_T+R_T+C_T`.                     (24)

因此若

`sum_T(N_T+R_T+C_T)<infinity`                   (25)

连同既有低高度与 approximation ledger，则 bounded finite-trace
Hodge--Weil theorem 推出目标 divisor 的非零 zeros 位于中心线。

这里真正需要的新输入不是 `N_T` 单独很小，而是以下二者之一：

1. 构造 packets 使 complement 上存在独立 arithmetic positivity，从而
   `R_T` 可和；
2. 构造近乎 exhaustive 的 multiscale frame，同时证明 `C_T` 可和。

## 6. 有限可证伪实验

下一阶段对 actual Type II rectangle 不应再审计 PSD component Gram 的“负特征值”。
应先形成 genuine self-adjoint signed compression `H_T`，再记录

`(N_T,R_T,C_T,Tr((H_T)_-))`.                    (26)

式 (24) 必须逐实例成立。对 diagonal height model，还应验证式 (11)--(13) 的
phase invariance；若实验仅改变 phases 却声称改善 capture，应判为 basis artifact。

## 7. 审计结论

本笔记得到四个无条件有限维结论：block negative ledger、phase-blind variance
公式、sharp codimension no-go，以及谱定理给出的非构造最优 compression。
它们把路线分成两个互不混淆的问题：

- 构造性：显式控制 complement negativity 与 packet coupling；
- 非构造性：证明预先给定的 arithmetic algebra 对全部 spectral effects
  order-dense，而不是事后选择负谱投影。

