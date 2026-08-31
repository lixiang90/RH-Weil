# Sturm--Liouville Green 极化与算术 Hodge current

文档 036 的 `max` 核不是偶然的积分技巧：它是一个规范加权
Sturm--Liouville 算子的 Green 核。本笔记由此构造一维 Hodge complex。
正极化算子和 trace-class Green 算子对每个 `sigma>0` 无条件存在；经典
RH 的存在性问题精确变成 von Mangoldt discrepancy current 是否在所有
这些负 Sobolev/Hodge 空间中具有有限能量。

## 1. Green 核

固定 `sigma>0`，令

`q=2sigma+1`, `p_sigma(x)=x^(q+1)/(2sigma)`，         (1)

并在 `[1,infinity)` 上考虑形式

`a_sigma(phi)=int_1^infinity p_sigma(x)|phi'(x)|^2dx`. (2)

相应微分表达式是

`L_sigma=-d/dx p_sigma(x)d/dx`.                      (3)

在左端取自然 Neumann 条件，在无穷远取衰减条件。定义

`K_sigma(u,v)=[2sigma/q]max(u,v)^(-q)`.              (4)

### 定理 EZ（max-kernel is the Sturm--Liouville Green kernel）

对内部源 `v>1`，函数 `u mapsto K_sigma(u,v)` 满足

`L_sigma K_sigma(.,v)=delta_v`,                      (5)

`partial_u K_sigma(1,v)=0`, `K_sigma(u,v)->0` as `u->infinity`. (6)

因此式 (4) 是 `L_sigma^(-1)` 的积分核。

#### 证明

当 `u<v` 时式 (4) 为常数；当 `u>v` 时

`partial_u K_sigma(u,v)=-2sigma u^(-q-1)`.           (7)

所以在两侧 `(p_sigma K')'=0`，且左端导数为零、无穷远值为零。在 `u=v`
处通量跳跃为

`-p_sigma(v)[K'(v+)-K'(v-)]`

`=-[v^(q+1)/(2sigma)][-2sigma v^(-q-1)]=1`,          (8)

即式 (5)。`□`

## 2. Trace-class Hodge Green 算子

定义 feature operator 的 kernel

`b_sigma(x,u)=sqrt(2sigma)x^(-sigma-1)1_(u<=x)`.     (9)

### 命题 FA（Green operator is positive trace class）

`G_sigma=L_sigma^(-1)=B_sigma^*B_sigma` 正且 trace class，并且

`Tr G_sigma=||B_sigma||_(HS)^2=1/(2sigma+1)`.        (10)

#### 证明

直接积分得

`int_1^infinity conjugate(b_sigma(x,u))b_sigma(x,v)dx`

`=2sigma int_(max(u,v))^infinity x^(-2sigma-2)dx`

`=K_sigma(u,v)`.                                     (11)

故 `G=B^*B`。又

`||B||_(HS)^2=int_1^infinity K_sigma(u,u)du`

`=[2sigma/(2sigma+1)]int_1^infinity u^(-2sigma-1)du`

`=1/(2sigma+1)`.                                     (12)

Hilbert--Schmidt 算子的 `B^*B` 为正 trace class，且 trace 等于式
(12)。`□`

所以 `L_sigma` 有紧 resolvent；其离散正谱的倒数之和由式 (10) 精确给出。
这与文档 029 的 compact Hodge operator 平行，但这里的 Green 极化完全
独立于素数，算术只进入 source current。

## 3. Von Mangoldt discrepancy 的规范势

定义闭半线上的 signed current

`nu=-delta_1+sum_(n>=2)Lambda(n)delta_n-dx`.          (13)

其累积分布为

`nu([1,x])=psi(x)-x=:E(x)`.                          (14)

形式上令

`phi_sigma=G_sigma nu`.                              (15)

### 定理 FB（arithmetic potential and Dirichlet-energy identity）

只要文档 035 的 `I_sigma` 有限，式 (15) 在 energy space 中良定义，并且

`-p_sigma(x)phi_sigma'(x)=E(x)` almost everywhere,  (16)

`L_sigma phi_sigma=nu`,                              (17)

以及精确 Hodge 恒等式

`a_sigma(phi_sigma)`

`=<nu,G_sigma nu>=I_sigma`.                          (18)

反之，若 current `nu` 具有满足式 (17) 的有限能量势，则 `I_sigma` 有限。

#### 证明

对式 (4) 关于第一变量微分。只有 `v<=x` 的 sources 贡献，故

`phi_sigma'(x)=-2sigma x^(-2sigma-2)nu([1,x])`.      (19)

与式 (1) 相乘得到式 (16)，再分布微分得到式 (17)。最后

`a_sigma(phi_sigma)=int p_sigma|phi_sigma'|^2`

`=2sigma int_1^infinity |E(x)|^2x^(-2sigma-2)dx`

`=I_sigma`.                                          (20)

Green 恒等式给中间 pairing。反向由式 (16) 与同一计算得到。边界 atom
`-delta_1` 被编码为右通量 `p_sigma(1)phi_sigma'(1+)=1`；对纯内部
`L^2` sources 则恢复定理 EZ 的自然 Neumann 条件。`□`

值得注意的是，粗界 `E(x)=O(x)` 已使点值势

`phi_sigma(x)=2sigma int_x^infinity E(u)u^(-2sigma-2)du` (21)

对每个 `sigma>0` 存在；真正的 RH 强度在有限 Dirichlet action，而不是
弱方程本身的可解性。

## 4. Hodge membership 中心线定理

记 `H_(-1,sigma)` 为 currents 关于 norm

`||eta||_(-1,sigma)^2=<eta,G_sigma eta>`             (22)

的完备空间。

### 定理 FC（negative-Sobolev Hodge criterion for RH）

经典 zeta 的下列条件等价：

1. RH 成立；
2. 对每个 `sigma>0`，规范 current `nu` 属于 `H_(-1,sigma)`；
3. 对每个 `sigma>0`，方程 `L_sigma phi_sigma=nu` 有有限 Dirichlet
   energy 解。

#### 证明

定理 FB 把条件 2、3 都等价于 `I_sigma<infinity`。文档 035 推论 EQ 把
后者对所有 `sigma>0` 的成立等价于 RH。`□`

FC 是一个具体的 Hodge 结构存在性定理：

- differential 与 polarization `a_sigma` 无条件给定；
- Green operator 正、trace class；
- arithmetic cycle/current `nu` 无条件给定；
- 唯一开放条件是该 cycle 在趋向临界权重时仍具有有限 Hodge norm。

它没有把 RH 隐藏在算子的自伴性中；RH 恰好是一个明确 cycle membership
陈述。

## 5. 有限 Hodge currents 与紧性终点

对整数 `X>=2`，在 `[1,X]` 上定义有限 Green 核

`K_sigma^X(u,v)=[2sigma/(2sigma+1)]`

` [max(u,v)^(-2sigma-1)-X^(-2sigma-1)]`.             (23)

它对应左端自然条件、右端 Dirichlet 条件。令 `nu_X` 是式 (13) 在
`[1,X)` 的截断并保留连续背景，使其累计值在 `[1,X]` 上为 `psi(x)-x`。

### 命题 FD（finite Hodge energies and cofinal compactness）

对每个有限 `X`，`K_sigma^X` 正且

`<nu_X,K_sigma^X nu_X>=I_sigma(X)`.                  (24)

此外 `I_sigma(X)` 随 `X` 单调增加，且

`sup_X I_sigma(X)<infinity`                          (25)

当且仅当有限势在 energy norm 中一致有界；此时它们弱紧，并收敛到定理
FB 的全局有限能量势。

#### 证明

把式 (9) 的 feature 空间从 `[1,infinity)` 截到 `[1,X]`，其 Gram 核正是
式 (23)，而 feature 积分仍为
`sqrt(2sigma)x^(-sigma-1)(psi(x)-x)`。故平方 norm 是文档 035 式
(26)，得到式 (24) 与单调性。Hilbert 空间中的一致有界族弱相对紧；有限
区间方程的相容性识别任意弱极限为全局 Green 势。反向显然。`□`

FD 把 RH 路线写成标准 Hodge 紧性问题：所有有限 cycles 与正极化都已经
存在，所缺的是对每个临界权重的 cofinal energy bound。

## 6. 广义 Sturm--Liouville Hodge 结构

对中心为 `c/2` 的 Gamma--Euler 数据，令

`q_(c,sigma)=c+2sigma`,

`L_(c,sigma)=-d/dx [x^(q_(c,sigma)+1)/(2sigma)]d/dx`, (26)

其 Green 核为

`K_(c,sigma)(u,v)=[2sigma/q_(c,sigma)]`

`                         max(u,v)^(-q_(c,sigma))`.   (27)

### 定理 FE（general Sturm--Liouville Hodge structure theorem）

设 `nu_Z=d(Psi_Z-M_Z)` 连同左端边界 current。若对每个
`sigma>sigma_0`，`nu_Z` 属于 `L_(c,sigma)` 的负一阶 energy space，
则全部非平凡零点满足

`|Re rho-c/2|<=sigma_0`.                             (28)

若 membership 对每个 `sigma>0` 成立，则对应广义 RH 成立。

当 `c+2sigma>1` 时，Green 算子 trace class，且

`Tr L_(c,sigma)^(-1)`

`=2sigma/[(c+2sigma)(c+2sigma-1)]`.                  (29)

#### 证明

与定理 FB 相同，负一阶 norm 是

`2sigma int_1^infinity |Psi_Z(x)-M_Z(x)|^2`

`                         x^(-c-2sigma-1)dx`.         (30)

应用文档 035 定理 ES 得式 (28)。trace 由积分式 (27) 的对角线，或
feature operator 的 Hilbert--Schmidt norm 得到。`□`

FE 抽离出的广义结构非常小：一个一维 weighted de Rham differential、
正 Dirichlet polarization、trace-class Green operator，以及一个 Euler
discrepancy current。这个 current 在全 Hodge scale 中的有限能量迫使
divisor 纯权重。
