# Tracial polarization、spectral dimension 与 weighted Weil determinant

文档 076 证明 scalar minimal GNS 不能用 ordinary Hilbert dimension 实现重复
零点，但 scalar atom mass 可以恢复重数数值。本笔记给出另一种闭合方式：
不添加 dark eigendirections，而在 spectral algebra 上使用 faithful semifinite
trace，把

`tau(P_rho)=m_rho`                                  (1)

作为 noncommutative/tracial dimension。相应 tracial spectral determinant
自动产生 factor `(s-rho)^(m_rho)`。

因此有两种不同但都严格的 multiplicity realization：

- matrix-valued package：`dim_H P_rhoH=m_rho`；
- tracial package：minimal Hilbert fiber 可一维，但 `tau(P_rho)=m_rho`。

后者已足以恢复 zeta/L-function 的 divisor multiplicities。

## 1. Weighted spectral algebra

令 `Gamma` 是 countable discrete spectral set，`m_gamma` 是 positive integers。
在

`M=ell^infinity(Gamma)`                             (2)

上定义

`tau(a)=sum_gamma m_gamma a(gamma)`, `a>=0`.        (3)

### 定理 OB（trace dimension realizes divisor multiplicity）

`tau` 是 faithful normal semifinite trace。coordinate projection
`P_gamma=1_{gamma}` 满足

`tau(P_gamma)=m_gamma`,                             (4)

即使 `M` 在 minimal Hilbert space `ell^2(Gamma)` 上的 ordinary spectral
fiber dimension 只有 `1`。

#### 证明

commutative algebra 上 trace property automatic。positive weights 给
faithfulness；monotone convergence 给 normality；finite-support projections
有 finite trace且递增到 identity，给 semifiniteness。式 (4) 是定义。`□`

所以 Murray--von Neumann/tracial dimension 与 ambient Hilbert dimension 可以
不同；这里的差异恰好承载 divisor multiplicity。

## 2. Tracial spectral determinant

先考虑 finite spectral set。令 normal diagonal operator

`Theta P_rho=rho P_rho`,                            (5)

并允许 integer signed trace weights `nu_rho`：positive weights 表示 zeros，
negative weights 表示 poles/alternating cohomological degrees。定义

`D_tau(s)=product_rho(s-rho)^(nu_rho)`.             (6)

### 定理 OC（local order and tracial logarithmic derivative）

在 `s` 不属于 spectrum 时，

`D_tau'(s)/D_tau(s)=sum_rho nu_rho/(s-rho)`

`                       =tau_gr((s-Theta)^(-1))`,  (7)

且 `D_tau` 在 `rho` 的 order 恰为 `nu_rho`。

对 infinite locally finite divisor，只要 finite-order/heat-resolvent hypotheses
给出一个固定 Weierstrass regularization，式 (6)–(7) 在减去相应 polynomial
counterterms 后仍成立；local orders 不受 regularization 影响。

#### 证明

finite product 逐 factor 取 logarithmic derivative 得式 (7)，local order
显然。infinite 情形的 canonical factors 只加入 locally holomorphic nonzero
renormalization及 polynomial logarithmic derivative，故不改变 local divisor。
`□`

这里使用的是明确的 **spectral product with tracial exponents**；不把它与只
输出正实数的其他 determinant notions 混同。

## 3. Tracially polarized Weil package

固定 center `c/2`。一个 **tracially polarized Weil package** 包含：

1. semifinite tracial von Neumann algebra `(M,tau)` 与 affiliated normal
   operator `Theta`；
2. positive Hilbert realization满足

   `Theta^*=c-Theta`;                               (8)

3. discrete finite-trace spectral projections；
4. integral trace dimensions `tau(P_rho)=m_rho`；
5. Euler/Lefschetz trace formula与 regularized tracial determinant identity

   `Lambda(s)=E(s)det_tau(s-Theta)`,                (9)

   其中 `E` 的 divisor 已知。

### 定理 OD（tracial polarized Weil centerline theorem）

任意 tracially polarized Weil package 的全部 nontrivial divisor 位于

`Re rho=c/2`,                                      (10)

且 `det_tau` 按 trace dimensions `m_rho` 恢复正确 algebraic multiplicities。

#### 证明

令 `A=Theta-c/2`。式 (8) 给 `A^*=-A`，所以 `Spec(Theta)` 位于中心线。
定理 OC 与公理 4 说明 determinant 在每个 spectral point 的 order 为
`m_rho`；式 (9) 转移到 `Lambda`。`□`

这将文档 001 的 Hilbert-dimension Weil theorem严格推广到 tracial dimension。

## 4. Grading and tensor operations

### 定理 OE（tracial Weil category closure）

tracial packages 对以下操作封闭：

1. direct sum：trace与 divisor multiplicities相加；
2. tensor product：使用 `tau_1 tensor tau_2`，pure weights相加，spectral
   projection trace dimensions相乘；
3. dual/contragredient：谱点取 `c-rho` 或 reciprocal，trace dimensions不变；
4. finite group invariants/idempotent summands：用 restricted trace；
5. `Z/2`-graded complexes：以 supertrace

   `tau_gr=tau_even-tau_odd`                       (11)

   定义 alternating tracial determinant。

#### 证明

normal semifinite traces 在 direct sums/tensor products 上分别相加/相乘。
tensor spectral projection `P_rho tensor P_sigma` 的 trace 是
`m_rho m_sigma`。dual 不改变 projection dimension。idempotent reduction 与
grading是 trace additivity。定理 073 的 polarization/tensor calculation 保持
adjoint center relation。`□`

因此 tracial multiplicities 与 PLF cohomological multiplicities具有相同的
formal calculus，而无需把 minimal scalar GNS 非自然地放大。

与文档 073 相同，这里的 tensor statement 只描述已经拥有 global spectral
trace packages 的对象。它不从两个 number-field L-functions 的零点空间
朴素构造 Rankin--Selberg 零点空间；后者仍需独立 global trace/determinant
compatibility。

## 5. Scalar covariance canonically induces a trace

设 critical scalar/vector-channel covariance 的 distinct atom `gamma` 是

`M_gamma=m_gamma^2 q_gamma q_gamma^*`,             (12)

其中 universal feature vector `q_gamma!=0` 已知。

### 定理 OF（atom-mass to tracial-dimension reconstruction）

rank-one atom 的唯一 nonzero eigenvalue/trace为

`w_gamma=m_gamma^2||q_gamma||^2`.                  (13)

若 normalized ratio

`w_gamma/||q_gamma||^2`                            (14)

是 positive integer square，则其 positive square root规范定义
`m_gamma`，从而在 minimal spectral algebra 上定义唯一 weighted coordinate
trace `tau(P_gamma)=m_gamma`。

所得 tracial determinant按 multiplicity `m_gamma` 计数，而 minimal GNS
eigenspace仍是一维。

#### 证明

outer product (12) 的 nonzero eigenvalue 是式 (13)。positive square root给
`m_gamma`。commutative atomic algebra 上，一旦所有 coordinate projection
weights指定，normal trace唯一；定理 OB–OC 给 determinant statement。`□`

integrality/perfect-square condition 是 divisor trace compatibility 的可检验
部分；对 arbitrary positive kernel 它不会自动成立。

## 6. Zeta and Gamma--Euler existence audit

### 定理 OG（conditional tracial zeta completion）

对 classical zeta，以下条件等价：

1. RH；
2. 文档 062 的 prime-built Abel Grams 有 critical tight completion；
3. 该 completion 产生 minimal scalar GNS、自伴 translation generator及由
   atom weights重建的 trace `tau(P_gamma)=m_gamma`；
4. 存在满足文档 062 trace formula的 tracially polarized Weil package，其
   determinant divisor是 completed zeta divisor。

在这些条件下，不需 nonminimal dark amplification，tracial determinant
已经按正确零点重数恢复 completed zeta。paired Gamma--Euler data 在文档
062/067 的 square-summability、frame 与 finite-order hypotheses 下同理。

#### 证明

1 与 2 是文档 062 定理 KL–KO。RH 下 critical covariance 正是式 (12)，
continuous width frame 保证 `q_gamma!=0`；定理 OF 从 atom weight恢复解析函数
本来就具有的 integer multiplicity，给 3。Hadamard/explicit-formula
regularization给式 (9)，故 4。4 经定理 OD 反推 RH。`□`

对 zeta，integrality 本身不是新增猜想：零点 order 已由 meromorphic function
定义为正整数。真正未证的仍是 critical tightness；tracial construction只在
这一步成立后，以 minimal 且无 dark directions 的方式闭合 multiplicity。

因此三层结构现在区分完整：

- scalar FPW：足以证明 centerline；
- scalar GNS + weighted trace：足以恢复 divisor multiplicities；
- matrix-valued multiplicity-complete GNS：进一步让 ordinary Hilbert
  eigenspace dimensions 等于 multiplicities。

第三层最强但不是 RH 所需；第二层是当前 prime covariance最自然的 determinant
接口。
