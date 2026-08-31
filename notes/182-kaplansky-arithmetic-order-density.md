# Kaplansky arithmetic order-density 与非构造 Hodge positivity

本文研究一个不要求显式构造负谱投影的存在性路线。核心观察是：对 finite
tracial algebra 中的有符号 current `X`，负谱迹是全部 positive contractions
对 `X` 的最大负响应。若一个由算术 correspondences 生成的 unital `*`-algebra
在 strong operator topology 下稠密，则 Kaplansky density 自动把这个上确界
缩小到“算术平方”而不改变其值。

因此，数域上的“类 Weil 结构存在性”可以被拆成两个彼此独立的命题：

1. algebraic density：局部算术生成元的双交换子是目标 von Neumann algebra；
2. local square positivity：每个有限字 `a` 都满足 current 对 `a^*a` 的
   下界，并且缺陷预算可和。

第一步是非构造的、可能可由 commutant/irreducibility 证明；第二步仍是实质性
算术内容。这个分解不会凭空证明 RH，但它把“构造未知 cohomology”替换成了一个
明确的生成性定理和一个有限字 sum-of-squares 问题。

## 1. Arithmetic square-test theorem

令 `(M,tau)` 是 finite von Neumann algebra，`A subset M` 是 unital
`*`-subalgebra，并假设 `A` 的 strong closure 为 `M`。令
`X=X^* in L^1(M,tau)`。

### 定理 AFI（Kaplansky square-test identity）[U]

有精确恒等式

`tau(X_-)=sup{-tau(Xa^*a): a in A, ||a||<=1}`.   (1)

特别地，若

`tau(Xa^*a)>=-epsilon`                           (2)

对所有 `a in A`、`||a||<=1` 成立，则

`tau(X_-)<=epsilon`.                             (3)

取 `epsilon=0` 得 `X>=0`。

#### 证明

任意 `a` 满足 `||a||<=1` 时，`0<=a^*a<=I`。negative-part variational
formula 因而给

`-tau(Xa^*a)<=tau(X_-)`.                         (4)

反向令 `p_-=1_(-infinity,0)(X)`。Kaplansky density 与 `A` 在其
C-star closure 中的 norm density 给出 `a_i in A`、`||a_i||<=1`，使

`a_i -> p_-` strongly.                           (5)

于是 `a_i^*a_i -> p_-` strongly，且全体一致有界。finite trace 下，一致有界
strong convergence 蕴含 `L^2` convergence。对一般 `X in L^1`，先把 `X`
作有界 spectral truncation，再用 Cauchy--Schwarz 控制截断部分、用
`L^1` tail 控制余项，得到

`tau(Xa_i^*a_i)->tau(Xp_-)=-tau(X_-)`.           (6)

与式 (4) 合并即得式 (1)。`square`

这个证明只保证存在一个逼近负谱投影的 arithmetic net；完全不需要把该投影写成
闭式公式。

## 2. Finite-word falsification witness

设 `A=alg^*(g_1,g_2,...)` 由明确算术生成元生成；按定义，`A` 的每个元素只含
有限多个生成元和有限 word length。

### 推论 AFJ（finite arithmetic word witness）[U]

若 `A` strong-dense 且 `tau(X_-)>0`，则存在一个 finite noncommutative
polynomial `a=P(g_1,...,g_m,g_1^*,...,g_m^*)`，满足

`tau(Xa^*a)<0`.                                  (7)

更定量地，对任意 `0<delta<tau(X_-)`，可选 `||a||<=1` 使

`-tau(Xa^*a)>tau(X_-)-delta`.                    (8)

因此，若 RH 失败而候选 arithmetic algebra 确实 strong-dense，则失败必有一个
有限字平方证书；它不会只能藏在不可达的无限极限中。这给计算搜索提供了半可判定
方向，但没有给出 witness word length 的先验界。

## 3. Bicommutant / irreducibility interface

记 `A'` 为 commutant。von Neumann bicommutant theorem 给出

`closure_strong(A)=A''`.                         (9)

### 推论 AFK（commutant density criterion）[U]

若 `A'=M'`，则 `A''=M`，定理 AFI 适用。特别地，在有限维
`M=B(H)` 中，只要 arithmetic generators 的共同 commutant 为
`C I`，它们生成全部 matrix algebra。

这说明非交换性不是装饰。若生成元全都交换，则 `A''` 至多是相应的 abelian
algebra，只能检测 conditional expectation `E_(A'')(X)`。例如

`X=[[0,-1],[-1,0]]`                              (10)

在标准 diagonal algebra 上所有 diagonal positive tests 的响应为零，但
`X` 有一个负特征值。加入一个与 diagonal generator 不交换的 shift 后，有限维
algebra 才可能变成全部 `M_2(C)` 并看见该负方向。

## 4. Conditional nonconstructive Hodge--Weil theorem

对每个 dyadic block `T`，设：

- `(M_T,tau_T)` 是 joint prime--continuum--Gamma current 所在的 finite
  tracial algebra；
- `X_T=X_T^* in L^1(M_T,tau_T)` 是该 block 的 signed current；
- `A_T` 是只由 Euler local correspondences、Gamma boundary operator 与
  threshold incidences 生成的 unital `*`-algebra，不以 zeros 定义；
- `A_T'=M_T'`；
- 存在 `epsilon_T>=0`，对所有 `a in A_T`、`||a||<=1` 有

  `tau_T(X_Ta^*a)>=-epsilon_T`.                  (11)

### 定理 AFL（arithmetic order-dense Hodge criterion）[C]

若

`sum_T epsilon_T<infinity`                       (12)

并满足既有低高度、Gamma 与 approximation ledger，则目标 zeta/L divisor 的
off-center negative index 有限；在 generalized bounded-index Weil theorem
的零预算版本 `epsilon_T=0` 下，全部非平凡 zeros 位于中心线。更一般地，任何
既有 finite-trace Hodge--Weil conclusion 可直接以

`tau_T((X_T)_-)<=epsilon_T`                      (13)

为输入。

#### 证明

由 `A_T'=M_T'` 和推论 AFK，`A_T` strong-dense。定理 AFI 将式 (11)
提升为式 (13)，逐 block 求和后应用 bounded finite-trace Hodge--Weil theorem。
`square`

## 5. 与“直接假设 Weil positivity”的区别和循环性审计

定理 AFL 的条件若不进一步分解，当然可能只是 Weil positivity 的稠密重述。
它只有在以下两步分别由独立机制证明时才产生新内容：

1. `A_T'=M_T'` 由 generators 的 support propagation、connectedness 或
   incidence irreducibility 得到，不使用 zero locations；
2. 式 (11) 由每个 finite word 的 local Euler/Gamma cancellation、sum-of-squares
   factorization 或 contractive transfer identity 得到，不调用 explicit formula
   的完整全测试函数正性。

以下做法仍属循环：

- 把负谱投影本身加入 generators；
- 用“对所有 Weil test functions 已非负”直接证明式 (11)；
- 先假设 uniform negative-index bound，再选择实现该 bound 的代数；
- 用 zeros 构造使 commutant 平凡的 generator。

## 6. 数域路线的下一最小引理

这个非构造分支现在有三个递进、可单独证伪的目标。

### 6.1 Generator theorem

在 finite Type II rectangle / threshold complex 上，选取明确生成元族

`G_T={local prime shifts, face incidences, Gamma boundary transfer}`. (14)

计算或证明其共同 commutant。第一目标不是正性，而是

`G_T'=M_T'`                                      (15)

在除去常数/annihilator sectors 后成立。

### 6.2 Finite-word positivity recursion

寻找 word length 递推，使

`tau_T(X_T(ga)^*(ga))`                           (16)

可由 `tau_T(X_Ta^*a)`、显式 commutators 与可和边界误差控制，其中 `g in G_T`。
若递推对任意有限 word 闭合，式 (11) 即由生成元层面的有限 identity 推出。

### 6.3 Quantitative Kaplansky rate

定理 AFI 不给 word length。若要得到可计算的有限证书，需要证明负谱 effect 在
degree-`L` arithmetic squares 中的 response approximation rate，例如

`tau_T((X_T)_-)`

` <=sup_(deg a<=L, ||a||<=1)-tau_T(X_Ta^*a)+rho_T(L)`, (17)

且 `rho_T(L)->0` 有显式、共尾可和的速率。这个问题连接 noncommutative
polynomial approximation、spectral gap 与 arithmetic propagation。

## 7. 审计结论

本笔记无条件证明了一个一般结构定理：strong-dense arithmetic square tests
精确 norm negative trace，并且任何负方向都有 finite-word witness。它提供了
“不具体构造数域 Weil cohomology”时最清晰的非构造路线之一。

尚未证明的是数域算术生成元的 commutant criterion 和 finite-word positivity
recursion。前者是代数生成性问题，后者是新的解析/算术核心；二者都比笼统要求
“存在一个 Weil 结构”更具体，也都有有限矩阵反例能够及时终止错误方向。

