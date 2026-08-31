# Möbius threshold complex、Hodge heat supertrace 与 positive gcd Gram

文档 165 证明 hard Vaughan 两通道之和与 cutoff `V` 无关，并指出完整 cross-Gram
预算在 Hadamard coordinates 中仍等同于原 physical energy。它同时证明 raw
三因子 synthesis 具有无界 exact-product multiplicity，所以 Möbius signs 必须先在
每个 product fiber 内求和。本笔记研究求和后出现的

`a_U=mu_(<=U)*1`, `b_U=epsilon-a_U=mu_(>U)*1`.   (1)

主要结论是：`b_U(q)` 不是任意 signed coefficient，而是一个由 `q` 的素因子除数
格无条件构造的有限 Hodge heat supertrace；其 bulk 由 supersymmetry精确配对，
只余乘法 threshold boundary 的 harmonic classes。另有一个 positive gcd-Gram
控制其二阶平均。

这提供了一个独立于零点的 signed Hodge candidate，但尚未证明它与 logarithmic
interval incidence 的组合具有 RH 所需的 Cauchy finite-trace bound。

## 1. Möbius threshold complex

对 `q>=1`，令 `P(q)` 是 `q` 的不同素因子集合，并定义有限 simplicial complex

`K_U(q)={S subset P(q): product_(p in S)p<=U}`,   (2)

其中空面乘积为一。它确为复形，因为取子集只会减小乘积。记 reduced chain
complex 为 `C_tilde_*(K_U(q);C)`，边界为 `partial`，组合 Hodge Laplacian 为

`Delta_j=partial_(j+1)partial_(j+1)^*`

`        +partial_j^*partial_j`,                  (3)

调和投影为 `P_j^harm=1_{0}(Delta_j)`。

### 定理 ACZ（truncated Möbius defect = finite Hodge supertrace）[U]

对 `q>1`，

`a_U(q)=sum_(d|q,d<=U)mu(d)=-chi_tilde(K_U(q))`, (4)

`b_U(q)=chi_tilde(K_U(q))`

`      =sum_(j>=-1)(-1)^j Tr(P_j^harm)`.          (5)

更强地，对每个 `t>=0` 都有 finite McKean--Singer identity

`b_U(q)=sum_(j>=-1)(-1)^j Tr(exp(-t Delta_j))`.   (6)

#### 证明

`mu(d)` 只在 squarefree divisors 非零，而这些 divisors 恰由 `P(q)` 的 subsets
参数化。因此

`a_U(q)=sum_(S in K_U(q))(-1)^|S|`

`      =-chi_tilde(K_U(q))`.                      (7)

因 `q>1`，`epsilon(q)=0`，所以 `b_U(q)=-a_U(q)`。有限维 simplicial Hodge
decomposition给 `ker Delta_j` 与 reduced homology 同构，Euler--Poincare 给式
(5)。令总 Dirac operator `D=partial+partial^*`；每个非零特征值的 even/odd
eigenspaces由 `D` 成对，故 heat supertrace中逐特征值相消，只余 harmonic
subspaces，得到式 (6)。`□`

结合文档 165 的

`R_II=b_U*Lambda_(>V)`,                           (8)

Type II coefficient 因而有无条件 Hodge 展开

`R_II(n)=sum_(m|n,m>V)Lambda(m)`

`          *Str exp[-t Delta(K_U(n/m))]`,         (9)

其中 `n/m=1` 项为零。式 (9)不引用零点；尚未证明的是这些 harmonic
supertraces在 near-product incidence Gram 中具有所需的全局 capacity bound。

## 2. Boundary-shell localization

### 定理 ADA（one-vertex shell formula）[U]

对 `q>1` 及任意素数 `p|q`，

`a_U(q)=sum_(d|rad(q)/p, U/p<d<=U)mu(d)`,         (10)

`b_U(q)=-sum_(d|rad(q)/p, U/p<d<=U)mu(d)`.        (11)

#### 证明

把 `rad(q)` 的 squarefree divisors按是否含 `p` 配对为 `d,pd`。若
`d<=U/p`，两项都出现且 `mu(d)+mu(pd)=0`；若 `U/p<d<=U`，只有 `d`
出现；若 `d>U`，两项都不出现。剩下的正是式 (10)，式 (11)来自
`b_U(q)=-a_U(q)`。`□`

这是式 (6)的 boundary localization：沿 vertex `p` 的离散 Morse pairing
消去了 complex bulk，未配对 faces 全部位于乘法薄壳 `(U/p,U]`。选择最小素因子
时，壳的 logarithmic width为 `log p_min(q)`；当 `q` 没有小素因子时，未配对
的空面精确记录 `b_U(q)=-1`，不能被静默删除。

## 3. Möbius defect 的 positive gcd Gram

令

`S_U(X)=sum_(q<=X)|a_U(q)|^2`,                    (12)

并定义

`Q_U=sum_(d,e<=U)mu(d)mu(e)/[d,e]`.              (13)

### 定理 ADB（exact second moment and positive gcd Gram）[U]

有

`S_U(X)=sum_(d,e<=U)mu(d)mu(e)floor(X/[d,e])`,   (14)

`S_U(X)=XQ_U+O(U^2)`,                            (15)

且

`Q_U=sum_(r<=U)phi(r)`

`       *(sum_(d<=U,r|d)mu(d)/d)^2>=0`.          (16)

此外无条件粗界

`S_U(X)<=X sum_(d,e<=U)1/[d,e]`

`       <<X log^3(2U)`.                          (17)

对 `b_U` 的二阶矩只少 `q=1` 的一项。

#### 证明

展开式 (12)并交换有限和得到式 (14)。以
`floor(X/l)=X/l+O(1)` 逐对应用，得到式 (15)。再用

`gcd(d,e)=sum_(r|d,r|e)phi(r)`                   (18)

及 `1/[d,e]=gcd(d,e)/(de)`，交换求和得到式 (16)。对式 (14)取绝对值，

`S_U(X)<=Xsum_(d,e<=U)gcd(d,e)/(de)`.            (19)

再次用式 (18)，并以 harmonic sum估计

`sum_(r<=U)phi(r)/r^2*(sum_(a<=U/r)1/a)^2`

` <<sum_(r<=U)log^2(2U/r)/r<<log^3(2U)`,         (20)

得到式 (17)。`□`

式 (16)是新的 positive arithmetic Gram：尽管 `a_U(q)` 本身是 signed Euler
supertrace，它的平均平方由 divisor-gcd incidence 的正平方和控制。式 (17)还不足以
处理 `Lambda_(>V)*b_U` 的全部 modulated near-product correlations，但它证明
Möbius fiber collapse 后的平均损失只有 polylogarithmic，而 raw factorization
space 的 Bessel constant按文档 165 无界。

## 4. 对广义结构定理的修正

当前数域 hard core 中有三个严格不同层次：

1. **positive physical Gram**：interval/Fejer incidence norm；它给能量，但单独
   不能禁止 physical amplification；
2. **channel primitive coordinate**：Hadamard difference；它只是 gauge
   coordinate，文档 165 说明它不能独立替代目标；
3. **arithmetic signed Hodge complex**：`K_U(q),partial,Delta`；其 heat
   supertrace在所有 `t` 上精确给 Möbius defect，且由 Euler product的 divisor
   combinatorics构造，不依赖零点。

第三层才是有限域 Hodge mechanism 的真实类比候选：non-harmonic faces由
supersymmetry成对消去，只有 harmonic boundary classes进入 Type II。它尚未拥有
有限域中的 Lefschetz polarization/similitude，也尚未给出 Cauchy negative-index
一致界，所以不能宣称 RH 已证。

对 Dirichlet character twists，`mu(d)chi(d)` 给 weighted face supertrace；要把它
提升成 ordinary homology dimension必须引入 compatible local-system/operator
weights。对一般 automorphic inverse coefficients，Boolean threshold complex未必
直接适用，必须逐个 Euler datum验证；不能从函数方程自动推广。

## 5. 下一步

下一阶段不再把“控制完整 hard cross Gram”列作独立目标。更精确的任务是：

1. 将式 (9)的 harmonic projections与 logarithmic interval incidence组成一个
   matrix-valued superconnection current；
2. 利用式 (10)先把每个 `b_U(q)` 局部化到乘法 boundary shell，再按
   `q=n/m` 作 dyadic rectangles；
3. 以式 (16)作为 diagonal gcd-Gram，而不是 raw triple multiplicity，研究
   不同 products 的 modulated cross incidence；
4. 寻找一个由 `partial+partial^*` 与 length translations共同满足的 adjoint或
   finite-index inequality，使 negative spectral trace受 harmonic boundary
   classes控制；
5. 若该 compatibility失败，构造明确反例，判断 threshold Hodge 是否也只是
   coefficient重写。

任何成功结果最终仍须回到文档 149--151 的 Cauchy finite-trace budget；但现在
候选 signed structure 与循环的 positive cross-Gram target已经严格分离。
