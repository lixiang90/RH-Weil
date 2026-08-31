# Abel analytic RKHS、边界留数与 Weil 谱结构

文档 063–064 把 annular Abel filtration 编码为单点 moments 和 Gamma 随机
finite Euler Grams。本笔记把全部 moments 重新组装成一个 prime-built
positive holomorphic kernel。其实际 Gram domain 的右边界精确读取最右零点，
而临界边界留数恢复文档 062 的 Hilbert--Pólya covariance。

这给出一个更接近有限域上上同调证明的结构：有限 Taylor fibers 无条件正；
中心线等价于这些 fibers 完备化为临界解析 RKHS；边界 residue 承载纯点
“Frobenius”谱。

## 1. Prime-built analytic-vector kernel

固定 `sigma_0>1/2`。沿用文档 063 的

`v_h(t)=sqrt(2sigma_0)e^(-sigma_0t)b_h(t)`,

`(Txi)(t)=t xi(t)`.                                (1)

在有定义处令

`V_h(z)=e^(sigma_0zT)v_h`.                         (2)

### 定理 LF（Abel analytic-vector Gram kernel）

vectors (2) 的 kernel 为

`mathcal K(h,z;k,w)=<V_h(z),V_k(w)>`

` =2sigma_0 int_0^infinity b_h(t)conjugate(b_k(t))`

`             *e^(-sigma_0(2-z-conjugate(w))t)dt`. (3)

对 finite Euler truncations，它有 exact pair expansion

`mathcal K=sum_(m,n)a_ma_n/sqrt(mn)`

`                         *R_(z,w)^(h,k)(m,n)`,    (4)

其中沿用 intersection endpoints `L,U`，令

`alpha=sigma_0(2-z-conjugate(w))`，则

`R_(z,w)^(h,k)(m,n)`

` =1_(U>L) 2sigma_0[e^(-alpha L)-e^(-alpha U)]/alpha`. (5)

`alpha=0` 时取连续值 `2sigma_0(U-L)`。在实际 integral convergence domain
中，`mathcal K` 是 Hermitian positive-definite、holomorphic in `z` 且
anti-holomorphic in `w`。

#### 证明

把式 (1)–(2) 展开即得式 (3)。两个 Euler indicators 的交集为 `[L,U)`，
对 exponential weight 积分给式 (5)。任意有限线性组合的 quadratic form 是
对应 `V_h(z)` 组合的 squared norm，故 positivity；holomorphy 由 dominated
convergence。`□`

式 (5) 对每个 finite Euler truncation 是 entire，但无限素数极限的 actual
Gram domain 才包含零点信息。

## 2. Taylor--Hankel finite fibers

令文档 063 的 moments 为 `M_q(h,k)`。形式展开式 (3) 得

`mathcal K(h,z;k,w)`

` =sum_(j,l>=0)(sigma_0z)^j(sigma_0conjugate(w))^l`

`                    *M_(j+l)(h,k)/(j!l!)`.       (6)

### 命题 LG（unconditional positive Taylor sections）

对每个 degree `R`，截面

`mathcal K_R=sum_(0<=j,l<=R)` 式 (6) 的相应项  (7)

无条件存在并 positive semidefinite。更精确地，它是 polynomial vectors

`V_(h,R)(z)=sum_(j=0)^R(sigma_0zT)^jv_h/j!`       (8)

的 Gram；再取文档 064 的 cofinal finite Euler cutoff，可把每个 entry 以
exponentially small error 实现成真正有限 prime matrix。

#### 证明

`sigma_0>1/2` 保证所有 moments 有限。式 (8) 的内积展开恰是式 (7)，所以
positive semidefinite。finite Euler approximation 用命题 KQ 与定理 LB。`□`

因此 finite algebraic/Taylor positivity 已无条件建立；开放问题只在无限
degree completion 的 domain。

## 3. Disk existence 精确等价于 RH

令

`sigma_c=max(0,Theta-1/2)`.                        (9)

### 定理 LH（critical analytic-RKHS existence theorem）

`V_h(z)` 的 collective width-trace norm 有限的最大 half-plane 是

`Re z<1-sigma_c/sigma_0`.                         (10)

因此以下条件等价：

1. RH；
2. 式 (3) 作为实际 prime Gram 在整个 half-plane `Re z<1` 上存在，并有
   locally bounded width trace；
3. 式 (3) 在整个 unit disk `|z|<1` 上产生具有 locally bounded width trace
   的 positive holomorphic RKHS；
4. finite Taylor--Hankel sections (7) 在每个 compact subset of the unit disk
   上以 width-trace topology 收敛到 locally bounded positive kernel。

#### 证明

由式 (3)，

`int_(h_0)^(h_1)||V_h(z)||^2dh`

` =2sigma_0 int e^(-2sigma_0(1-Re z)t)dmu(t)`.    (11)

文档 062/063 给 `mu` 的 Laplace abscissa `2sigma_c`，故式 (10) 精确成立。
RH 即 `sigma_c=0`，给 1 与 2。half-plane 包含 unit disk，故 2 推 3；若
`sigma_c>0`，取 real
`1-sigma_c/sigma_0<z<1`，它位于 unit disk 但式 (11) 发散，所以 3 推 1。
式 (6) 的 positive Taylor sections 在实际 domain 内由 analytic-vector series
局部收敛。反之，固定任意 real `0<r<1`，式 (8) 的 scalar polynomial
`sum_(j<=R)(sigma_0rt)^j/j!` 对每个 `t>=0` 单调增到
`e^(sigma_0rt)`；条件 4 的 diagonal local bound 与 monotone convergence
迫使式 (11) 有限。于是每个 real `r<1` 的 actual exponential vector 存在，
再由 Cauchy--Schwarz 与 spectral calculus 得到整个 disk 的 actual kernel，
故 4 推 3。`□`

这里要求的是 actual locally bounded Gram kernel。把式 (5) 或显式公式作
meromorphic continuation，而不证明无限 prime Gram 的 norm convergence，
不能满足条件 3–4。

## 4. 临界边界 residue 恢复零点谱

### 定理 LI（radial residue equals critical divisor covariance）

假设 RH。对 real `0<r<1`，有精确恒等式

`(1-r)mathcal K(h,r;k,r)`

`                 =G_(sigma_0(1-r))(h,k)`.        (12)

因此

`lim_(r->1-)(1-r)mathcal K(h,r;k,r)`

` =sum_gamma c_gamma(h)conjugate(c_gamma(k))`.    (13)

极限在 compact width rectangles 上以 Gram/Hilbert--Schmidt 意义成立。

#### 证明

式 (3) 在 `z=w=r` 时的 weight 是
`2sigma_0e^(-2sigma_0(1-r)t)`；乘 `1-r` 正好变成文档 062 定义的
`G_sigma`，其中 `sigma=sigma_0(1-r)`，给式 (12)。定理 KN 给式 (13)。`□`

所以临界零点谱不是另外附加到 RKHS 上的数据，而是 prime-built analytic
kernel 在边界点 `1` 的 positive Abel residue。

## 5. 两层 GNS 与 Hilbert--Pólya generator

### 推论 LJ（RKHS boundary Hilbert--Pólya structure）

RH 下，式 (3) 的 RKHS 有两层 canonical dynamics：

1. interior vertical translations

   `V_h(z+iy)=e^(isigma_0yT)V_h(z)`，             (14)

   由 positive time operator `T` 生成；
2. boundary residue (13) 的最小 Kolmogorov/GNS decomposition 产生

   `(U_sxi)_gamma=e^(igamma s)xi_gamma`，          (15)

   其 selfadjoint generator `A` 给

   `Theta_op=1/2+iA`, `Theta_op*=1-Theta_op`.      (16)

最小 boundary GNS 的 spectral atom weights 在已知 normalization 下恢复零点
重数的数值，但每个 distinct ordinate 的 cyclic eigenspace 仍是一维。按文档
062 推论 KO 可用该 recovered integer weight 选择 nonminimal multiplicity
amplification，使 ambient `A` 的 eigenspace dimensions恢复 divisor
multiplicities；新增 orthogonal directions 不由原 scalar boundary vectors
生成。文档 076 给出这一区别的 matrix-valued rank theorem。

#### 证明

式 (14) 来自 `T` 的 spectral calculus。式 (13) 正是文档 062 的 critical
covariance，故其 GNS/Stone construction 给式 (15)–(16)；atom weight 与
nonminimal amplification 给上述受限意义下的重数结论。`□`

interior `T` 测量 prime signal 的 logarithmic time；boundary `A` 测量零点的
vertical frequency。二者不能混同，但由同一个 analytic prime kernel 的
interior action 与 boundary residue 联系。

## 6. Positivity completion 的必要性

### 命题 LK（finite-section positivity does not imply RKHS completion）

文档 063 的模型 `dmu_a(t)=e^(2at)dt`，`0<a<sigma_0`，使每个 finite
Taylor section (7) positive，却只能在

`Re z<1-a/sigma_0`                               (17)

完成为 actual RKHS。故“全部有限阶关系成立”仍不足以推出中心线；必须证明
这些正截面在整个 unit disk 的 locally bounded completion。

#### 证明

所有 finite moments 存在，故命题 LG 适用。式 (11) 变成

`2sigma_0 int_0^infinity`

` e^(-2[sigma_0(1-Re z)-a]t)dt`，

其收敛条件恰为式 (17)。`□`

这与 Weil 猜想证明中的关键差别一致：有限 correspondence identities 不够；
还需要 Hodge--Riemann positivity 在适当 completion 上成立。

## 7. 广义 analytic RKHS--Weil 结构定理

### 定理 LL（Gamma--Euler RKHS--Weil theorem）

设一组 paired finite-order Gamma--Euler data 具有：

1. 中心 `c/2` 与非空、中心对称 divisor；
2. Euler annular finite fibers 及其 cofinal actual current；
3. continuous width divisor-separating frame；
4. 某个 absolute-convergence base point `sigma_0` 的全部 moment Grams；
5. critical coefficients 的 square summability。

令 `sigma_c=max(0,Theta-c/2)`。则：

- base moments 产生全部 unconditional positive Taylor fibers；
- actual analytic-vector Gram 的 maximal half-plane 为

  `Re z<1-sigma_c/sigma_0`;                       (18)

- 它完成为 critical half-plane `Re z<1` 上的 positive RKHS 当且仅当全部
  divisor 位于 `Re rho=c/2`；
- centerline 成立时，boundary residue 产生 selfadjoint `A`，并且

  `Theta_op=c/2+iA`, `Theta_op*=c-Theta_op`.       (19)

#### 证明

定理 KV/LE 给 Abel abscissa与 finite fibers。把式 (1)–(13) 中 `1/2`
替换为 `c/2`，定理 LH 给 maximal domain 与 centerline equivalence；critical
square summability 给 boundary covariance，定理 KP 的 GNS construction 给
式 (19)。非自对偶数据先与 contragredient 配对以取得 Hermitian kernel。`□`

## 8. 对 zeta 存在性的最终审计

对 Riemann zeta，已经无条件构造：

- base point `sigma_0>1/2` 上的 prime-built moment Grams；
- 每个有限 Taylor degree、Euler cutoff 的 positive analytic kernel；
- 精确 pair formula (5) 与 finite Gamma cutoff；
- maximal-domain exponent 与 `Theta` 的等式。

未证且与 RH 等价的是这些 finite positive kernels 在整个 unit disk 上的
locally bounded completion。若完成，边界 residue 自动给文档 062 的完整
Hilbert--Pólya spectrum；仅逐项解析延拓不够。
