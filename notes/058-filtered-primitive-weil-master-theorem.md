# Filtered primitive Weil package：统一结构定理与 zeta 存在性审计

文档 001 的 PLF 代数给出带额外相容极化的形式纯性蕴含；
2026-09-06 已修正其奇次星算子，有限域模型须另行验证，不能自动视为一般 Weil 证明的实例；文档 045–057 则从素数侧
逐步构造了数域的 finite Gram、primitive Tate 消元、酉 dilation、Sobolev
filtration 与 logarithmic-moment Hodge core。本笔记把这些结果合并成一个
单一结构定义和主定理，并逐项回答：

1. 什么样的广义代数/分析结构足以迫使 zeta divisor 位于中心线？
2. 经典 zeta 对该结构已经无条件存在到哪一步？
3. 尚缺的条件是否比 RH 弱，还是恰与 RH 等价？

审计修订后的结论是：finite Euler--Tate complex、正 polarizations、定性
trace/divisor visibility 和全部 tail control 都有无条件模型；但从定性可见性
推出 Hodge norm 的幂次下界还需要一个定量 dual/Riesz separation 公理。对一般
Gram realization，该公理与 actual arithmetic cycle 的 critical subpower
Hodge norm 都尚未建立。rank-one annular 模型因有独立 exponent theorem 而是特例。

## 1. Filtered primitive Weil package

固定函数方程中心 `c/2`。一个 **filtered primitive Weil package**（FPW）
由以下数据组成。

### FPW1：Euler--Tate finite fibers

对 cofinal scales `X->infinity`，有有限维复空间 `V_X`、由有限 Euler
coefficients 构造的 distinguished cycle `v_X in V_X`，以及 exact Tate
centering operator `Pi_X`。这些对象的定义不能使用 divisor 的实部。

### FPW2：正 Hodge polarizations

每个 `V_X` 上有显式 Hermitian positive semidefinite form

`Q_X(v)=<H_Xv,v>>=0`,                              (1)

并有 arithmetic feature/Gram realization。允许 `rank(H_X)=X^(o(1))`，也
允许在保持 subpower 双侧等价的范围内随 `X` 改变 polarization。

### FPW3：primitive dilation covariance

存在 normalized dilation action 或其 finite filtered model，使 Tate class
被一个 polynomial `P_X` 消去；在每个 fixed critical spectral compact 上，

`P_X(U)=X^(o(1))` 双侧可逆。                       (2)

uniform bounded invertibility 是 strong FPW；式 (2) 是 tempered FPW。

### FPW4：trace/divisor compatibility 与定量分离

**FPW4a（定性兼容）**：Euler realization 与完成 zeta/L 函数的显式公式相容。
对每个 fixed divisor point `rho`，其 normalized formal mode 为

`X^(rho-c/2)m_X(rho)`，                            (3)

其中在某个 fixed spectral compact 上

`|m_X(rho)|=X^(o(1))` 双侧成立。                   (4)

并且没有 `Re rho!=c/2` 的 divisor point 对全部 fibers 恒不可见。这个条件只
排除恒等消失；它本身不能给 Hodge norm 的幂次下界。

**FPW4b（quantitative dual separation）**：在 `V_X/ker Q_X` 上，对每个 fixed
`rho` 存在 dual functional `ell_(X,rho)` 和一条 cofinal subsequence，使

`||ell_(X,rho)||_(Q_X^*)=X^(o(1))`,                (4a)

`|ell_(X,rho)(v_X)|>=X^(Re rho-c/2-o(1))`.         (4b)

这里 dual norm 为

`sup_(Q_X(v)>0)|ell(v)|/sqrt(Q_X(v))`，            (4c)

并要求 `ell` 消灭 `ker Q_X`。式 (4b) 只要求证明所需的 lower bound，不要求
抽取器排除所有更右侧模态。它是一个 Riesz/frame lower-bound 公理；不能由
Mellin 唯一性或“非恒为零”自动推出。strong spectral/GNS realization若已有
bounded spectral projections，可由投影坐标产生 FPW4b；一般 filtered Gram 尚需
单独证明。文档 163 证明：若 fibers 来自同一个 centered Dirichlet series 的
fixed-annulus Sobolev realization，则 Mellin pole 与 compact-frequency dual
自动给出 FPW4b；这一结论依赖跨尺度 coherence，不适用于任意 Gram。

### FPW5：tempered tails and finite-order upper bound

高频、Taylor、sampling、boundary 与 finite-completion tails 的总 Hodge norm
为 `X^(o(1))`。若

`Theta=sup_(rho)Re rho`，                           (5)

则 finite-order explicit formula 给

`Q_X(v_X)<=X^(max(0,2Theta-c)+o(1))`.              (6)

### FPW6：critical arithmetic tightness

filtered 版本要求

`Q_X(v_X)=X^(o(1))`.                               (7)

strong 版本要求一个固定/covariant Sobolev family 上

`sup_X Q_X(v_X)<infinity`.                         (8)

FPW1–FPW3、FPW4a 与 FPW5 是载体、定性兼容和 tail control；FPW4b 是定量模式
分离；FPW6 是数域 Hodge--Riemann positivity 对实际 arithmetic cycle 的内容。

## 2. 中心线主定理

### 定理 JO（quantitative filtered primitive Weil center-line theorem）[C]

设非空中心对称 divisor data 满足 FPW1–FPW6，特别是 FPW4b 的定量对偶分离，
并设 `Theta=sup_(rho)Re rho<infinity`。则全部 divisor points 满足

`Re rho=c/2`.                                      (9)

事实上有精确 exponent identity

`limsup_(X->infinity)log(max(1,Q_X(v_X)))/logX`

`=max(0,2Theta-c)`.                                (10)

#### 证明

式 (6) 给式 (10) 的上界。固定任意 divisor point `rho`。由 dual
Cauchy--Schwarz 与 FPW4b，沿相应 cofinal subsequence 有

`|ell_(X,rho)(v_X)|^2`

` <=||ell_(X,rho)||_(Q_X^*)^2 Q_X(v_X)`，          (11)

所以

`Q_X(v_X)>=X^(2Re(rho)-c-o(1))`.                  (12)

给定 `epsilon>0`，选择 `Re rho>Theta-epsilon`，再令 `epsilon->0`，得到式 (10)
的下界。FPW6 使左侧为 `0`，所以 `Theta<=c/2`。中心对称和 divisor 非空给
`Theta>=c/2`，并排除左侧零点。因此式 (9) 成立。`□`

**审计边界。** 删除 FPW4b 后，上述证明在式 (11) 处中断。定性 Mellin
uniqueness 只说明一个 mode 不对所有 `X` 恒为零，不能排除随 `X` 变化的
subpower 相消。因此弱 FPW 应视为研究框架 [R]，不是已证明的 exponent theorem。

这与有限域证明的逻辑完全平行：trace compatibility 给 Frobenius/divisor
modes，正 polarization 把它们变成平方范数，而 Hodge tightness 排除错误
weight。

## 3. Strong package 产生真正 Hilbert--Pólya 算子

### 定理 JP（strong FPW GNS theorem）

若 FPW 的 strong 条件 (8) 对一个 translation-covariant Sobolev Gram family
成立，且 finite fibers 在 dilation 下相容并穷尽，则存在 Hilbert completion
`mathcal H`、强连续酉群

`U_t=e^(itA)`,                                     (12)

其中 `A=A*`。定义

`Theta_op=c/2+iA`，                                (13)

则

`Theta_op*=c-Theta_op`.                            (14)

若 trace compatibility separating，则 divisor 是 `Theta_op` 的谱/共振
determinant divisor，因而位于中心线。

#### 证明

对 finite Gram 的平移 orbit 作 GNS completion；uniform Sobolev tightness
保证平移在 completion 上有界且强连续。Stone theorem 给 selfadjoint `A`，
式 (13) 直接给式 (14)。FPW4 把 spectral coordinates 与 divisor 对应；
定理 E 给中心线。`□`

filtered 定理 JO 比 JP 弱但更灵活：subpower filtration 已足以证明权重，
却不自动给一个不依赖 `X` 的 canonical Hilbert norm。不能把两者混称。

## 4. 稳定性与有限化

### 定理 JQ（dual transfer 与 actual-energy transfer）[U]

必须区分两种稳定性。

1. 若两个 quotient Gram spaces 之间存在 `X^(o(1))`-conditioned 双侧线性同构，
   则 FPW4b 的 dual functional 可与同构逆向复合，dual norm 只改变
   `X^(o(1))`。uniform nonvanishing Laurent correspondence 和真正的双侧
   polarization equivalence 属于此类。
2. 若只知道两个 actual arithmetic energies 相差 `X^(o(1))`，则它们的
   subpower tightness 和 power `limsup` 可转移；但这本身不构造近似 Gram
   全空间上的 FPW4b。Poisson alias、Taylor truncation 和 finite moment
   approximation 在现有证明中属于此类。

#### 证明

第一项是 dual norm 在有条件数控制的同构下的标准变换公式。第二项直接由
`Q'_X(v'_X)=Q_X(v_X)+X^(o(1))`（或相应双侧 additive enclosure）比较
`max(1,Q)` 的 power `limsup`。additive actual-vector identity 没有定义任意
方向上的逆映射，所以不能据此声称 dual 已转移。`□`

因此 sampled/moment 判据可以从已经验证 separation 的 coherent Sobolev
energy 继承中心线蕴含；除非另有全空间同构证书，不应说它们自动继承 FPW4b。

### 推论 JR（finite-rank FPW suffices）

若经 JQ 的操作后，每个 scale 的 Hodge core 是

`Q_X(v_X)=sum_(j=1)^(R_X)|ell_(X,j)(v_X)|^2`

`                         +X^(o(1))`,              (15)

其中 `R_X=X^(o(1))`，则只要

`max_(j<=R_X)|ell_(X,j)(v_X)|^2=X^(o(1))`,        (16)

中心线结论成立。

#### 证明

有限个非负项的 maximum 与 sum 在 `R_X=X^(o(1))` 下具有相同 power
exponent；应用定理 JO。`□`

## 5. 经典 zeta 的逐项存在性

### 命题 JS（finite zeta FPW carrier audit）[U/R]

经典 zeta 无条件满足 FPW1–FPW3、FPW4a 与 FPW5；FPW4b 必须按具体 realization
单独审计：

| 公理 | zeta 中的实现 | 状态 |
|---|---|---|
| FPW1 | `chi=phi-2phi(2·)`，`u(L)=sum Lambda(n)chi(n/L)`，再以 `Lambda-1` finite completion | [U] 精确 |
| FPW2 | pure-prime Gram、biharmonic/Sobolev Green Gram、sampled/moment 矩阵或 annular-width frame | [U] 正半定 |
| FPW3 | `I-sqrt2 U_(-log2)`，unit-circle gap `sqrt2-1`；adaptive order `r=o(logX)` | [U] tempered 可逆 |
| FPW4a | zeta 显式公式；primitive multiplier off-center 无零 | [U] 定性 separating |
| FPW4b | 对偶泛函的 `X^(o(1))` norm 与 mode 下界 | [U] adaptive Sobolev/annular coherent carrier 由文档 163；[U] rank-one annular 由 JX；[R] 任意 Gram 未证 |
| FPW5 | BV boundary bound、Hilbert large-sieve tail、Poisson alias、Taylor remainder | [U] subpower |

下列 actual-cycle tightness 判据分别由其原始定理直接证明与 RH 等价；不能再把它们
统称为“由弱 FPW + 定性 visibility 自动推出”：

1. primitive block `C_prim(X)=X^(o(1))`；
2. centered full homogeneous Gram `mathcal E_4(X)=X^(o(1))`；
3. two-moment biharmonic norm `mathcal H_2(X)=X^(o(1))`；
4. adaptive Sobolev norm `mathcal H_(r_X)(X)=X^(o(1))`；
5. polylog sampled Euler core 为 subpower；
6. `O(logX/loglogX)` logarithmic-moment Hodge form为 subpower；
7. rank-one annular coordinate `|B_A(X)|^2=X^(o(1))`；
8. continuous annular-width mean Gram uniformly tight。

#### 证明边界

载体结论分别来自命题 IE、定理 IH/IT/IY、定理 IF/JB、定理 IG、命题 HY 与
定理 IW/JG/JK。文档 163 现在为 adaptive Sobolev carrier 严格验证 FPW4b；
sampled/moment 判据再按定理 JQ 的 actual-energy transfer 继承其中心线蕴含。
rank-one annular 仍由 JX 独立处理，strong width frame 由 KC 处理。对除此之外的
任意 Gram，仍必须另行验证 FPW4b。`□`

### 推论 JT（revised zeta existence boundary）

对 zeta：

- finite filtered carrier、定性 explicit-formula visibility 与 positive Grams 已无条件存在；
- rank-one annular detector 因定理 JX 的独立 exponent 计算具备定量 separation；
- adaptive Sobolev carrier 因文档 163 的 compact-frequency Mellin dual 具备 FPW4b；
- sampled/moment actual energies 可由 subpower approximation 转移中心线蕴含，但任意 Gram 的全空间 FPW4b 仍未自动建立；
- strong/critical arithmetic polarization 的 tightness 仍等价于 RH；
- 因而本仓库没有证明 RH，也没有把 RH 隐藏在 finite positivity 中。

一般 FPW 现在有两个需区分的接口：`(i)` divisor mode 到 Gram norm 的定量分离，
`(ii)` actual `Lambda-1` vector 的 uniform/subpower tightness。某些 Mellin-coherent carriers 已独立
解决 `(i)`，但 `(ii)` 仍有 RH 强度；不能再笼统称“唯一开放项只有 FPW6”。

## 6. Gamma--Euler 数据的广义存在性定理

### 定理 JU（Gamma--Euler FPW existence theorem）

设完成 Gamma--Euler datum 满足：

1. finite-order meromorphic continuation 与中心 `c/2` 的 paired functional
   equation；
2. Euler logarithmic derivative coefficients 具有 polynomial growth，且有
   continuum/Tate main density；
3. 存在 compact BV primitive Mellin kernel，其 multiplier 在开临界条带
   对 divisor separating；
4. Rankin--Selberg diagonal 为 `X^(o(1))`；
5. normalized Euler frequencies 在 fixed compact annuli，coefficient mass
   为 `X^(mu+o(1))`；
6. 对所选 finite fibers 存在 FPW4b 的受控对偶泛函；或者所选 fibers 是
   文档 163 的 Mellin-coherent fixed-annulus Sobolev carrier，此时 FPW4b
   由定理 ACM 自动给出。

前五项给 FPW1–FPW3、FPW4a、FPW5，并可选成 rank

`O_mu(logX/loglogX)`                               (17)

的 finite logarithmic-moment carriers。若再有第 6 项及 actual arithmetic
cycle 的 FPW6 tightness，则全部 paired divisor 位于 `Re rho=c/2`。

#### 证明

Tate centering与 primitive multiplier 用定理 II；piecewise Mellin finite
Gram 用 IQ；adaptive polarization/tail 用 JE；Poisson 与 Taylor finite-rank
reduction 用 JJ/JN。这些结果给定性 carrier；一般情形仍需把第 6 项作为独立
输入，但 fixed-annulus Sobolev realization 可调用文档 163 的定理 ACM。加入
FPW4b 和 FPW6 后，修订定理 JO 给中心线。`□`

它覆盖 primitive Dirichlet L 函数；对 fixed-degree automorphic L 函数还需
逐例验证 local coefficient/Rankin--Selberg 输入。若 local temperedness 本身
未知，则不能把它偷偷作为无条件结论。

## 7. 与有限域 PLF 的精确字典

| 有限域 PLF/Weil cohomology | Filtered primitive Weil package |
|---|---|
| closed points/Frobenius traces | prime powers/Euler logarithmic coefficients |
| Tate classes | continuum/pole main modes |
| primitive cohomology | zero-mass scale-difference current |
| Lefschetz operator | normalized dilation/translation polynomial |
| Hodge star/Rosati polarization | positive Green, sampled or moment Gram |
| Hard Lefschetz finite decomposition | finite logarithmic dilation descendants |
| Frobenius weight | divisor growth exponent in `X` |
| Hodge–Riemann positivity | FPW6 arithmetic tightness |
| Lefschetz trace formula | global explicit formula |

有限域中 fiber dimension 固定；数域 filtered package 的 rank 缓慢增长。这是
两者最显著的差别，也是为何数域只得到 asymptotic/tempered polarization，
而不是现成的有限维 pure Frobenius module。

## 8. 证据边界与下一步

主结构问题不再表述为“只剩一条公理”。文档 163 已对 Mellin-coherent
adaptive Sobolev carrier 完成第一项；对任意其他 finite Gram 仍需分别检查：

1. 是否有全空间 FPW4b，或是否仅能通过 actual-energy approximation 转移结论；
2. 是否能证明 FPW6 actual-cycle tightness。

最小 finite tightness 候选是定理 JM 的 moment form

`M(X)^*H_XM(X)=X^(o(1))`,                          (18)

其中 `dim H_X=O(logX/loglogX)`，所有 entries 和 moments 均由有限素数数据
显式计算。

下一步不应再通过可逆 smoothing 改写同一 norm；应直接攻击式 (18)：

1. 分析 `H_X` 的正交多项式/有效谱基；
2. 对对应 moment combinations 建立 twisted Selberg symmetry；
3. 利用 residue/character dispersion 控制 actual `Lambda-1` vector；
4. 或构造独立几何，使式 (18) 成为显然的 intersection-norm bound。

在已有独立 exponent theorem 的 realization 中，成功的 subpower bound 会证明
RH；对一般 Gram 还必须先验证 FPW4b。当前结果是条件结构定理、有限化工具和
非循环存在性审计，而不是最终算术估计。

文档 073 给 FPW 一个 operator-theoretic 解释：FPW6 是 normalized arithmetic
orbit 的 cyclic temperedness；strong covariant tightness 则通过 Cesaro
unitarization 重建 exact polarization。它也证明这些 tempered Weil objects
在标准 tensor-category operations 下封闭，但不把 global Rankin--Selberg
zero space误认成局部 Satake tensor 的朴素 global tensor product。
