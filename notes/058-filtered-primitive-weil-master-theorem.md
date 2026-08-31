# Filtered primitive Weil package：统一结构定理与 zeta 存在性审计

文档 001 的 PLF 代数抽象了有限域 Weil 证明；文档 045–057 则从素数侧
逐步构造了数域的 finite Gram、primitive Tate 消元、酉 dilation、Sobolev
filtration 与 logarithmic-moment Hodge core。本笔记把这些结果合并成一个
单一结构定义和主定理，并逐项回答：

1. 什么样的广义代数/分析结构足以迫使 zeta divisor 位于中心线？
2. 经典 zeta 对该结构已经无条件存在到哪一步？
3. 尚缺的条件是否比 RH 弱，还是恰与 RH 等价？

结论是：finite Euler--Tate complex、正 polarizations、trace compatibility、
divisor visibility 和全部 tail control 都已无条件存在；唯一未证公理是
actual arithmetic cycle 的 critical subpower Hodge norm，而它与 RH 等价。

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

### FPW4：trace/divisor compatibility

Euler realization 与完成 zeta/L 函数的显式公式相容。对每个 fixed divisor
point `rho`，其 normalized mode 为

`X^(rho-c/2)m_X(rho)`，                            (3)

其中在某个 fixed spectral compact 上

`|m_X(rho)|=X^(o(1))` 双侧成立。                   (4)

filtered center-line 版本只要求 **off-center separating**：没有
`Re rho!=c/2` 的 divisor point 对全部 fibers 不可见。strong spectral/GNS
版本若要恢复完整 divisor，则要求所有 divisor points separating。

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

FPW1–FPW5 是结构与兼容性；FPW6 是数域 Hodge--Riemann positivity 对实际
arithmetic cycle 的内容。

## 2. 中心线主定理

### 定理 JO（filtered primitive Weil center-line theorem）

设中心对称 divisor data 拥有满足 FPW1–FPW6 的 filtered primitive Weil
package，则全部 divisor points 满足

`Re rho=c/2`.                                      (9)

事实上有精确 exponent identity

`limsup_(X->infinity)log(max(1,Q_X(v_X)))/logX`

`=max(0,2Theta-c)`.                                (10)

#### 证明

式 (6) 给式 (10) 的上界。固定任意 divisor point `rho`。FPW4 在一个 fixed
compact spectral channel 中给 mode (3)，其 polarization weight 由式 (2)、
(4) 最多改变 `X^(o(1))`。Mellin singularity/finite-order uniqueness 防止
该 fixed pole 被其他指数完全消去，故沿某子列

`Q_X(v_X)>=X^(2Re(rho)-c-o(1))`.                  (11)

对所有 `rho` 取 supremum 得式 (10) 的下界。FPW6 使左侧为 `0`，所以
`Theta<=c/2`。divisor 在 `rho->c-conjugate(rho)` 下中心对称；若有
`Re rho<c/2`，其对偶点实部大于 `c/2`，矛盾。因此式 (9) 成立。`□`

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

### 定理 JQ（equivalent-polarization invariance）

以下操作保持定理 JO 的全部假设与结论：

1. 乘以在 critical unitary spectrum 上 uniform nonvanishing 的 Laurent
   correspondence；
2. 以 `X^(o(1))` 双侧改变每个 fixed spectral compact 上的 polarization；
3. 删除总 norm 为 subpower 的高频或 boundary tail；
4. 用 alias 为 subpower 的 sampled Gram 替换 continuous Gram；
5. 用 uniform energy error 为 subpower 的 finite moment Gram 替换 sampled
   或 continuous core。

#### 证明

五种操作都把每个 fixed divisor mode 的 squared norm乘以
`X^(o(1))`，并只加入 subpower remainder。因此不改变式 (10) 的 power
`limsup`。`□`

JQ 是 filtered Weil category 的同构概念：对象不按逐项公式相等，而按
critical spectral weights 的 tempered equivalence 分类。

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

### 定理 JS（unconditional finite zeta FPW structure）

经典 zeta 无条件满足 FPW1–FPW5：

| 公理 | zeta 中的实现 | 状态 |
|---|---|---|
| FPW1 | `chi=phi-2phi(2·)`，`u(L)=sum Lambda(n)chi(n/L)`，再以 `Lambda-1` finite completion | 无条件精确 |
| FPW2 | pure-prime Gram、biharmonic/Sobolev Green Gram、sampled/moment 矩阵或 annular-width frame | 无条件正半定 |
| FPW3 | `I-sqrt2 U_(-log2)`，unit-circle gap `sqrt2-1`；adaptive order `r=o(logX)` | 无条件 tempered 可逆 |
| FPW4 | zeta 显式公式；primitive multiplier off-center 无零，连续 annular widths 对完整 critical spectrum 有 frame gap | 无条件 separating |
| FPW5 | BV boundary bound、Hilbert large-sieve tail、Poisson alias、Taylor remainder | 无条件 subpower |

而 FPW6 的下列实现彼此等价，并各自等价于 RH：

1. primitive block `C_prim(X)=X^(o(1))`；
2. centered full homogeneous Gram `mathcal E_4(X)=X^(o(1))`；
3. two-moment biharmonic norm `mathcal H_2(X)=X^(o(1))`；
4. adaptive Sobolev norm `mathcal H_(r_X)(X)=X^(o(1))`；
5. polylog sampled Euler core 为 subpower；
6. `O(logX/loglogX)` logarithmic-moment Hodge form 为 subpower。
7. rank-one annular coordinate `|B_A(X)|^2=X^(o(1))`。
8. continuous annular-width mean Gram uniformly tight。

#### 证明

FPW1–FPW5 分别是命题 IE、定理 IH/IT/IY、定理 IF/JB、定理 IG、命题
HY 与定理 IW/JG/JK。前六个 FPW6 版本的等价性依次由定理 IG、IP、IV、
JB、JI、JM；第七个由定理 JX，第八个由定理 KC。`□`

### 推论 JT（exact zeta existence boundary）

对 zeta：

- finite filtered Weil structure 已无条件存在，且仅作 off-center detection 时
  可压到 rank `1`；
- strong/critical arithmetic polarization 的存在性等价于 RH；
- continuous annular-width frame 已无条件解决 full-spectrum alias 与 uniform
  reconstruction，故 strong package 的剩余缺口也仅是 arithmetic tightness；
- 因而本仓库没有证明 RH，也没有把 RH 隐藏在 finite positivity 中；
- 唯一开放项是 distinguished arithmetic cycle 在已构造正 polarizations
  中的 uniform/subpower norm，而不是空间、kernel、dilation 或 trace formula
  的存在。

这是非循环存在性审计：所有 finite forms 对任意 coefficient vector 都正，
但只有实际 `Lambda-1` vector 的临界大小仍未知。

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
   为 `X^(mu+o(1))`。

则 FPW1–FPW5 存在，并可选成 rank

`O_mu(logX/loglogX)`                               (17)

的 finite logarithmic-moment fibers。若这些 fibers 上的 actual arithmetic
cycle 满足 FPW6，则全部 paired divisor 位于 `Re rho=c/2`。

#### 证明

Tate centering与 primitive multiplier 用定理 II；piecewise Mellin finite
Gram 用 IQ；adaptive polarization/tail 用 JE；Poisson 与 Taylor finite-rank
reduction 用 JJ/JN。定理 JO 给中心线。`□`

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

主结构问题现已闭合到一条公理：对 zeta 证明任一 FPW6 版本。最小 finite
版本是定理 JM 的 moment form

`M(X)^*H_XM(X)=X^(o(1))`,                          (18)

其中 `dim H_X=O(logX/loglogX)`，所有 entries 和 moments 均由有限素数数据
显式计算。

下一步不应再通过可逆 smoothing 改写同一 norm；应直接攻击式 (18)：

1. 分析 `H_X` 的正交多项式/有效谱基；
2. 对对应 moment combinations 建立 twisted Selberg symmetry；
3. 利用 residue/character dispersion 控制 actual `Lambda-1` vector；
4. 或构造独立几何，使式 (18) 成为显然的 intersection-norm bound。

任何成功的 subpower bound 都会证明 RH。当前结果是结构定理、完整有限化和
非循环存在性审计，而不是该最终算术估计。

文档 073 给 FPW 一个 operator-theoretic 解释：FPW6 是 normalized arithmetic
orbit 的 cyclic temperedness；strong covariant tightness 则通过 Cesaro
unitarization 重建 exact polarization。它也证明这些 tempered Weil objects
在标准 tensor-category operations 下封闭，但不把 global Rankin--Selberg
zero space误认成局部 Satake tensor 的朴素 global tensor product。
