# Prime-orbit Schatten 阈值与 Euler-local normal-limit no-go

文档 078 表明有限图的 closed orbits、Hecke operator、companion Frobenius
与 Hodge form 可以同时存在。本节尝试对 Riemann zeta 作最直接的对应构造：
每个素数给一个长度 `log p` 的周期轨道。结论分两层：Euler/周期轨道载体
确实无条件存在；但任何纯 prime-local、以正常算子理想极限拼接的 determinant
都不可能产生全局 zeta 零点。成功结构必须包含非局部 prime mixing、奇异极限
或先取全局上同调再取 determinant。

## 1. 无条件 prime-orbit transfer carrier

令

`H_pr=direct_sum_p C^d`,                                (1)

`D e_(p,j)=log(p)e_(p,j)`.                              (2)

取一族 unitary local Frobenius `U_p in U(d)`，令

`U=direct_sum_p U_p`,  `T(s)=U exp(-sD)`.               (3)

对 Riemann zeta，`d=1,U_p=1`。一般固定 degree 的 tempered Euler 数据也
具有此形式（有限多个 ramified factors 可另外加入）。

### 定理 OO（prime-orbit trace realization）

在 `Re(s)>1`，`T(s)` 为 trace class，且

`det(I-T(s))^(-1)`

` =product_p det(I-U_p p^(-s))^(-1)`,                  (4)

`log det(I-T(s))^(-1)`

` =sum_(m>=1) Tr(T(s)^m)/m`

` =sum_p sum_(m>=1) tr(U_p^m)p^(-ms)/m`.               (5)

特别地，`U_p=1` 时式 (4) 就是 `zeta(s)`。

#### 证明

`T(s)` 的 singular values 是每个 `p^(-Re(s))` 重复 `d` 次，故
`Re(s)>1` 时绝对可和。有限截断的 determinant 与 trace-log 展开是普通
有限维恒等式；绝对收敛允许依次令 prime cutoff 和 power cutoff 趋于无穷。
`□`

因此“每个素数是一条长度 `log p` 的 closed orbit”不只是比喻：它给出一个
正 Hilbert 空间、正生成元 `D`、unitary local Frobenius 与精确 Euler trace。
这与 Deninger 动力系统纲领的局部周期数据一致。但 `T(s)` 是依赖 `s` 的
transfer family，不是一个以 zeta zeros 为固定谱的全局 Frobenius。

## 2. 临界线是精确 Schatten 边界

### 定理 OP（prime-orbit Schatten threshold）

对任意实数 `r>=1` 和 `sigma=Re(s)>0`，

`T(s) in S_r  iff  r sigma>1`.                          (6)

特别地：

- trace class 的精确区域是 `sigma>1`；
- Hilbert--Schmidt 的精确区域是 `sigma>1/2`；
- 在临界线 `sigma=1/2`，`T(s)` 不属于 `S_2`，但属于每个 `S_r,r>2`，
  因而属于整数 Schatten class `S_3`。

#### 证明

由 singular values 的显式列表，

`||T(s)||_(S_r)^r=d sum_p p^(-r sigma)`.                (7)

prime sum 在 exponent `>1` 收敛；在 `=1` 由 Euler 的
`sum_p 1/p=infinity` 发散；更小 exponent 逐项更大。`□`

这把“Euler product 到不了临界线”细化成算子理想分层：中心线正好是二阶
summability 的边界，而不是 compactness 的边界。事实上 `sigma>0` 时
`T(s)` 仍 compact；丢失的是可取普通 trace/determinant 的强度。

## 3. Higher regularized determinant 删除了什么

对整数 `k>=1` 与有限 prime set，定义

`det_k(I-T)`

` =det(I-T) exp(sum_(j=1)^(k-1)Tr(T^j)/j)`.             (8)

### 定理 OQ（canonical determinant and missing traces）

在 `Re(s)>1/k`，prime cutoff 极限存在、局部一致且无零，并等于

`Delta_k(s)=product_p [(det(I-U_p p^(-s)))`

`             *exp(sum_(j=1)^(k-1)tr(U_p^j)p^(-js)/j)]`.  (9)

在 zeta scalar case，若

`P_X(z)=sum_(p<=X)p^(-z)`,                              (10)

则对每个有限 `X` 有精确恒等式

`product_(p<=X)(1-p^(-s))`

` =Delta_(k,X)(s) exp(-sum_(j=1)^(k-1)P_X(js)/j)`.      (11)

#### 证明

有限维式 (8) 逐 eigenvalue 分解即给式 (9)、(11)。对 `|z|<1`，

`log(1-z)+sum_(j=1)^(k-1)z^j/j=-sum_(j>=k)z^j/j`,      (12)

其局部绝对值为 `O(|z|^k)`。`sum_p p^(-k sigma)` 在
`k sigma>1` 收敛，故 canonical product 局部一致收敛且不降为零。`□`

在 `Re(s)=1/2`，`Delta_3` 已合法，但式 (11) 为恢复 inverse Euler product
必须补回 `P(s)+P(2s)/2`。这些正是被 `det_3` 删除的低 prime-power traces。
所以 higher determinant 可以越过中心线，却只得到一个 **zero-free 的局部
正则化对象**，没有自动得到 `1/zeta` 或 completed zeta。

在 `Re(s)>1` 有 Möbius inversion

`P(s)=sum_(r>=1) mu(r) log(zeta(rs))/r`.                (13)

它由 `log zeta(s)=sum_(m>=1)P(ms)/m` 直接反演得到。若以式 (13) 解析延拓
式 (11) 的 counterterm，就已经把 `zeta(rs)` 的 global divisor 放进构造；
这可用于恒等变形，但不能作为无循环证明 RH 的结构存在性论证。

## 4. 正常 Euler 极限不能产生全局零点

令

`Z_X(s)=product_(p<=X)(1-p^(-s))^(-1)`.                (14)

### 定理 OR（Hurwitz normal-limit no-go）

令 `Omega` 是包含于 `Re(s)>0` 的连通开集。设 `R_X` 在 `Omega` 上全纯
无零，并且 `R_X Z_X` 局部一致收敛到非零全纯函数 `Z`。则 `Z` 在
`Omega` 上无零。

因此，在任何包含非平凡 zeta 零点、但不含 `s=1` 的小圆盘上：

1. `Z_X` 不可能局部一致收敛到 `zeta`；
2. 乘以任何无零且保持正常收敛的 archimedean/Tate renormalizer 也不可能
   局部一致收敛到 `xi`；
3. inverse partial products 同样不可能作为有限全纯函数局部一致收敛到在该点
   有 pole 的 `1/zeta`。

#### 证明

若 `Re(s)>0`，方程 `p^(-s)=1` 不成立，故每个 `Z_X` 全纯无零；乘 `R_X`
后仍如此。Hurwitz theorem 说明一列无零全纯函数的局部一致极限要么恒为零，
要么仍无零。假设排除前者。第三点还可直接由局部一致极限保持有限全纯看出。
`□`

这不是说 zeta 没有 Euler product，而是说从绝对收敛半平面到临界带的解析
延拓必然是一个 **非正常的全局过程**。全局零点不能从互不作用的 finite
prime blocks 通过温和的局部一致极限凭空出现。

### 定理 OS（prime-block Schatten no-go）

更一般地，设 `T_X(s)=direct_sum_(p<=X)T_p(s)`，每个 local block 在
`Omega subset {Re(s)>0}` 上使 `I-T_p(s)` 可逆。若对某个 `k`：

1. `T_X(s)` 在 `S_k` 中局部一致收敛；
2. 使用 canonical `det_k`；
3. 只乘局部一致、全纯无零的 counterterms；

则所得极限在 `Omega` 无零，不能是 `xi` 的 spectral determinant。

#### 证明

`S_k` convergence 给 regularized determinant 的局部一致收敛；有限
prime-block determinants 无零。应用定理 OR/Hurwitz 即得。也可直接用式
(12) 的 locally normally convergent logarithm。`□`

所以把各 prime 的局部酉 Frobenius 作 direct sum、tensor-independent Euler
product 或 Schatten completion，即使局部纯性完全成立，也不足以产生全局
RH 谱。

## 5. 成功 Weil 结构所需的最小非局部输入

### 结论 OT（necessary global mixing audit）

任何从 primes 构造 classical zeta Weil package 的成功方案，至少必须发生
以下一项：

1. **nonlocal prime mixing**：determinant 前的 operator 已有连接不同素数的
   off-diagonal blocks，并能在有限阶段产生 global zeros；
2. **global cohomological quotient**：先用一个混合 prime/Tate/archimedean
   数据的 differential 取 cohomology，再对 induced Frobenius 取
   graded determinant；
3. **singular renormalized limit**：prime cutoff 极限在原空间不是 normal
   determinant limit，但经可独立控制的 subtraction/compactification 后在新空间
   收敛；
4. **nonlocal trace formula**：periodic-orbit trace 先与 archimedean 和 Tate
   项整体相消，之后才定义 zero-side spectral object。

纯 prime-local direct sum 已由定理 OS 排除。

本仓库先前的 max-kernel、prefix-flow、Brownian bridge、Weil form 与 Abel--GNS
结构都含有跨整数/跨素数的 Gram coupling，并把 Euler、Tate、archimedean
项在 determinant 之前合并。定理 OS 表明这种 nonlocality 不是计算上的累赘，
而是产生任何 global zero spectrum 的逻辑必要条件。

下一步存在性目标因而可以更明确地写成：从无条件 prime-orbit carrier
`(H_pr,D,U)` 出发，构造一个 **不预先使用 zeta zeros** 的全局 differential
或 Schur/Feshbach quotient，使其 cohomological determinant 是 `xi`；然后在
该 quotient 上证明文档 073 的 two-sided tempered bound。前半步负责产生
zeros，后半步才负责把它们压到中心线。这两步不能再由独立 local Euler blocks
代替。

## 6. 有限恒等式回归

`scripts/qw_matrix.py` 新增：

- `primes_up_to`；
- `prime_orbit_schatten_sum`；
- `finite_prime_euler_inverse`；
- `finite_prime_regularized_determinant`；
- `finite_prime_regularization_counterterm`。

回归测试在 `Re(s)=0.6` 的复点（普通 Euler product 已不处于绝对收敛论证的
安全区域，但有限乘积仍有定义）逐位核对式 (11)，并核对 prime sieve 与有限
Schatten sums。数值部分只检查公式实现；Schatten 阈值和 no-go 来自上述证明。
