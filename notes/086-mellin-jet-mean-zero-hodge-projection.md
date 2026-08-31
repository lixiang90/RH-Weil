# Mellin zero jets 与最小能量 mean-zero Hodge 投影

文档 085 用单一 quadratic direction

`u(1-u),  u=log n/log N`                                (1)

消去 periodic boundary 的 constant mode。该构造需要除以 scalar response
`D_N`。本节证明：`D_N` 与待消去的 constant mode 含有同一个 nontrivial-zero
residue current，因此小规模数值稳定不能推出 uniform stability。正确的抽象
结构不是挑选一个非零 scalar denominator，而是在多方向 correction space 中
作最小 Hodge norm 投影；其稳定量是正的 response capacity Schur complement。

## 1. Weighted-Mertens identities

写

`L=log N`,  `u_n=log n/L`,

`B_N=sum_(n<=N)mu(n)(1-u_n)`,                          (2)

`D_(N,j)=sum_(n<=N)mu(n)u_n^j(1-u_n),  j>=1`.         (3)

### 定理 QJ（endpoint directions as Mertens derivatives）

令 `M(t)=sum_(n<=t)mu(n)`，则

`B_N=(1/L)int_1^N M(t)dt/t`,                          (4)

以及

`D_(N,j)=(1/L)int_1^N M(t)u(t)^(j-1)`

`                    *((j+1)u(t)-j)dt/t`,             (5)

其中 `u(t)=log t/L`。等价的完全离散式为

`D_(N,j)=sum_(k=1)^(N-1)M(k)[w_j(k)-w_j(k+1)]`,       (6)

`w_j(t)=u(t)^j(1-u(t))`。

#### 证明

Abel summation 给

`sum_(n<=N)mu(n)w(n)`

` =M(N)w(N)-int_1^N M(t)w'(t)dt`.                    (7)

式 (2) 的 weight 在 `N` 为零且 derivative 为 `-1/(Lt)`，给式 (4)。对
`w_j=u^j(1-u)`，

`w_j'(t)=u^(j-1)[j-(j+1)u]/(Lt)`,                    (8)

给式 (5)。在每个 `[k,k+1)` 上 `M(t)=M(k)` 作 Stieltjes summation，得到
式 (6)。`□`

所以所有 endpoint-preserving polynomial directions 都有 exact finite
arithmetic response；不需要零点数据来构造它们。

## 2. 为什么单一 quadratic denominator 可能失稳

对 `c>1`，Riesz--Perron inversion 给

`B_N=(1/(2pi i))int_(c-iinfinity)^(c+iinfinity)`

`                 N^s/[L s^2 zeta(s)] ds`,            (9)

并且

`D_(N,1)=(1/(2pi i))int N^s/zeta(s)`

`                 *[1/(Ls^2)-2/(L^2s^3)]ds`.         (10)

令 `f(s)=1/zeta(s)`。已知

`f(0)=-2`,  `f'(0)=2log(2pi)`.                        (11)

### 定理 QK（shared zero-residue current）

把式 (9)--(10) 的 contour 向左移动时，`s=0` 的 residues 分别为

`B_N:  -2+f'(0)/L`,                                  (12)

`D_(N,1): -f'(0)/L-f''(0)/L^2`.                      (13)

每个被越过的 simple nontrivial zero `rho` 分别贡献

`Z_B(rho)=N^rho/[L rho^2 zeta'(rho)]`,                (14)

`Z_D(rho)=N^rho/zeta'(rho)`

`          *[1/(Lrho^2)-2/(L^2rho^3)]`.              (15)

因此 `B_N+2` 与 `D_(N,1)` 的 leading zero contribution 相同，而
archimedean/`s=0` leading terms 的符号相反。单方向参数

`alpha_N=-(B_N+2)/D_(N,1)`                            (16)

在 zero current 很小时趋向 `+1`，在 zero current 主导时形式上趋向 `-1`，
并可能在两部分抵消使 `D_(N,1)` 很小时产生极点。

#### 证明

式 (9) 是 weight `log(N/n)` 的标准 inverse Mellin formula。又因

`u(1-u)=v/L-v^2/L^2`,  `v=log(N/n)`,                 (17)

而 `v^k` 的 Mellin kernel 是 `k!/s^(k+1)`，得到式 (10)。展开
`N^sf(s)` 到二阶并取 `s=0` residue，`f(0)` 项在式 (10) 中抵消，给
式 (12)--(13)。在 simple zero 处 `1/zeta(s)` 的 residue 是
`1/zeta'(rho)`，代入两个 kernels 即得式 (14)--(15)。`□`

严格的 explicit formula 应以 symmetric finite-height contour 加 remainder
理解；这里的结论只使用每个 crossed pole 的局部 residue，不假定 zero sum
绝对收敛，也不假定 zeros simple。multiple zeros 时把式 (14)--(15) 换成相应
higher residues。

在 `N=10,...,20000` 的探索计算中 `alpha_N` 大致位于 `1.0--2.5`，但这只说明
该范围仍主要看见式 (12)--(13) 的低阶结构；它不是 uniform nonvanishing
证据。若把这种有限数值稳定直接外推，就等于忽略式 (14)--(15)。

## 3. 多方向 response jets

取 directions

`q_j(n)=mu(n)u_n^j(1-u_n),  1<=j<=R`.                (18)

由 `v=log(N/n)`，

`u^j(1-u)=sum_(k=1)^(j+1)`

`          (-1)^(k-1)binom(j,k-1)v^k/L^k`.           (19)

所以 `D_(N,j)` 的 exact Mellin kernel 是

`K_(j,L)(s)=sum_(k=1)^(j+1)(-1)^(k-1)binom(j,k-1)`

`                         *k!/(L^k s^(k+1))`.         (20)

在 simple zero `rho` 的 response 为

`N^rho K_(j,L)(rho)/zeta'(rho)`.                      (21)

随着 `j` 改变，式 (20) 给 `1/(Lrho)` 的不同 polynomial jets。多方向空间
因此不是重复同一个 scalar test，而是对 zero residue current 作有限 jet
separation；这与文档 075/076 的 exterior/multiplicity channels 是同一设计
原则在 boundary gauge 上的版本。

## 4. Minimum-energy mean-zero projection

令 `g_j` 是 Hilbert space `H` 中与 coefficient direction `q_j` 对应的
correction vectors，令

`W_(jk)=<g_j,g_k>`                                    (22)

为 positive-definite Hodge Gram。记 response vector

`D=(D_(N,1),...,D_(N,R))^T`,                          (23)

以及 target response

`t_N=-(B_N+2)`.                                      (24)

约束 `D^*alpha=t_N` 恰好使 corrected periodic mean 为零。

### 定理 QL（response-capacity Hodge projection）

若 `W>0` 且 `D!=0`，则满足 mean-zero constraint 的唯一 minimum-`W`-norm
correction 是

`alpha_min=t_N W^(-1)D/(D^*W^(-1)D)`.                (25)

定义 positive response capacity

`C_(N,R)=D^*W^(-1)D>0`.                              (26)

则最小 correction energy 为

`||g_(alpha_min)||^2=|t_N|^2/C_(N,R)`.                (27)

#### 证明

在 inner product `<x,y>_W=x^*Wy` 中，constraint functional 的 Riesz
representer 是 `W^(-1)D`。Cauchy--Schwarz 给

`|D^*alpha|^2<=C_(N,R) alpha^*Walpha`,                (28)

且等号当且仅当 `alpha` 与 `W^(-1)D` 成比例。用 constraint 确定比例即得
式 (25)--(27)。`□`

这消除了“任选一个 `D_(N,j)` 并假定它不小”的非规范性。真正需要证明的量
变成 invariant positive scalar `C_(N,R)`；它就是 boundary response map 的
rank-one Schur complement/capacity。如果取 `W` 为真实 Nyman correction
vectors 的 Gram，式 (27) 是实际 Hilbert energy；也可先取简化 positive
metric 作 finite algebraic exploration。

## 5. Low convolution remains filtered

由式 (18)，corrected polynomial 是

`P_alpha(u)=1-u+sum_(j=1)^R alpha_j u^j(1-u)`

`            =sum_(k=0)^(R+1)p_k u^k`,               (29)

其中

`p_0=1`,  `p_1=-1+alpha_1`,

`p_k=alpha_k-alpha_(k-1)  (2<=k<=R)`,

`p_(R+1)=-alpha_R`.                                  (30)

### 定理 QM（projected almost-prime filtration）

对 `m<=N`，

`[zeta A_(N,alpha)](m)`

` =delta_(m,1)+sum_(k=1)^(R+1)p_k M_k(m)/(log N)^k`. (31)

因此 minimum-energy mean-zero projection 的完整低 defect 仍只支撑在

`omega(m)<=R+1`.                                     (32)

#### 证明

式 (30) 是 telescoping polynomial identity；把它代入文档 083 定理 PO，
再用定理 PP 的 support filtration，得到式 (31)--(32)。`□`

所以增加 correction directions 不会破坏 arithmetic可解释性；它只按可控
阶数逐层加入 prime-power、semiprime、three-almost-prime 等 currents。

## 6. General reciprocal-algebra version

设 `L(s)=sum a(n)n^(-s)`，其 Dirichlet inverse coefficients 为 `beta(n)`。
把式 (18) 中 `mu(n)` 换成 `beta(n)`，定义

`M_(L,k)(m)=sum_(d|m)a(m/d)beta(d)(log d)^k`.          (33)

### 定理 QN（metric boundary projection for reciprocal systems）

对任意 finite endpoint-direction space 和任意 positive metric `W`：

1. mean-response map 仍由一个 finite vector `D` 表示；
2. 若 `D!=0`，定理 QL 无改变地给 canonical minimum-energy mean-zero
   correction；
3. 完整低 convolution 为

   `delta_(m,1)+sum_k p_k M_(L,k)(m)/(log N)^k`;       (34)

4. `M_(L,k)` 是 Dirichlet series
   `L(s)(d/ds)^k(1/L(s))` 的 coefficient，差一个显式 sign `(-1)^k`。

#### 证明

前两项纯属 finite Hilbert linear algebra。第三项展开 polynomial cutoff 并用
`a*beta=delta`。最后

`(d/ds)^k(1/L(s))=sum beta(d)(-log d)^k d^(-s)`，    (35)

与 `L(s)` 相乘并比较 coefficients 即得。`□`

这给出一个比 zeta fractional-part model 更广的 algebraic Hodge gauge：只要
另有一个 synthesis Hilbert space 实现这些 reciprocal directions，便能对
一般 Euler/Dirichlet 数据作同一个 capacity projection。

## 7. 存在性审计

### 结论 QO（finite existence versus uniform existence）

对每个固定 `N,R`，只要 response vector 非零，minimum-metric mean-zero
structure 无条件存在，且其 coefficients、positive capacity、energy 与完整低
almost-prime current 都可有限计算。相对于单一 quadratic gauge，这已经移除
了非规范的 scalar-denominator 选择。

尚未证明的是一列 `R=R(N)` 与真实 Hodge metrics `W_N`，使

`|B_N+2|^2/C_(N,R)=O(1/log N)`                       (36)

并同时控制文档 085 的 parabolic Farey sector。式 (9)--(21) 表明 capacity
必须吸收 nontrivial-zero residue jets；若直接假定其 uniform lower bound，可能
再次把 RH 强度藏进假设。下一步应构造 actual correction Gram 的 finite
Feshbach formula，并研究增加 jet directions 时 capacity 的 monotonicity 与
high-denominator leakage。

## 8. 计算实现

`scripts/qw_matrix.py` 新增：

- `mobius_endpoint_direction_response_via_mertens`；
- `minimum_metric_mean_zero_mobius_mollifier`。

回归测试对 `j=1,2,3` 比较 direct coefficient sum 与 exact Abel--Mertens
formula；验证三方向投影的 zero mean、两个 endpoint、minimum-metric 性质，
并逐项核对 degree four polynomial 的完整低 convolution formula。
