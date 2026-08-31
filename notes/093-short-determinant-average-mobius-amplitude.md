# 短 determinant 逆元平均与 Möbius conductor 的一致界

文档 092 把 parabolic collision 写成 reciprocity-preserving Kloosterman
transform，但现有黑箱估计尚未覆盖全部 coupled ranges。本节先直接处理最短
determinant strata。两个新的无条件输入恰好配合：logarithmic Möbius Riesz
sum 在全半轴一致有界，而 positive `delta=+/-1` kernel 沿完整 inverse-residue
systems 的总质量只有常数量级。结果是每个固定的 reduced determinant sector
对线性 Möbius filter 的 principal shared-GCD mode 总计为 `o(1)`；真正障碍
必须来自随 `N` 增长的 determinant range 或 nonprincipal sieve modes。

## 1. Logarithmic Möbius Riesz sum 一致有界

定义

`G(X)=sum_(n<=X)mu(n)/n log(X/n)`,                    (1)

`m(X)=sum_(n<=X)mu(n)/n`.                            (2)

### 定理 SG（uniform logarithmic Riesz bound）

存在 absolute constant `C_mu` 使

`sup_(X>=1)|G(X)|<=C_mu`.                            (3)

#### 证明

交换有限和与积分给

`G(X)=int_1^X m(t)dt/t`.                             (4)

经典 zeta zero-free region 与 Perron/partial summation 给某个 `c>0` 下的

`m(t)<<exp(-c(log t)^(3/5)(loglog t)^(-1/5))`        (5)

（改变小 `t` 区间只改变常数）。式 (5) 对 measure `dt/t` 可积，故式 (4)
的 partial integrals 一致有界。`□`

这里只用了无条件 PNT 级 zero-free region，而没有使用 RH；文档 085 已引用的
Lee--Leong 显式估计可作为式 (5) 的现代有效版本。

## 2. 去掉有限 Euler factors 不破坏一致性

对整数 `r>=1` 置

`T_r(X)=sum_(m<=X,(m,r)=1)mu(m)/m log(X/m)`.         (6)

令 `D(r)` 是所有 prime factors 都整除 `r` 的正整数集合，允许任意次幂。

### 定理 SH（local-smooth convolution and conductor bound）

有 exact identity

`T_r(X)=sum_(d in D(r),d<=X)G(X/d)/d`.              (7)

因此

`|T_r(X)|<=C_mu product_(p|r)(1-p^(-1))^(-1)`

`          =C_mu r/phi(r)`.                          (8)

在线性 filter 下，对所有 `1<=r<=N`，

`|rS_N(r)|<=C_mu/[log N] * r/phi(r)`                (9)

当 `r` squarefree；非 squarefree `r` 的左侧为零。

#### 证明

Dirichlet series identity

`sum_((m,r)=1)mu(m)m^(-s)`

` =1/zeta(s) product_(p|r)(1-p^(-s))^(-1)`          (10)

说明 restricted Möbius coefficients 是 `mu` 与 `1_(d in D(r))` 的 Dirichlet
convolution。把 convolution 代入 logarithmic Riesz sum并交换有限和，得到
式 (7)。定理 SG 与 geometric Euler products 给式 (8)。文档 092 式 (16)
再给式 (9)。若 `r` 非 squarefree，则每个 multiple `n` 都有 `mu(n)=0`。`□`

式 (9) 比文档 089 的 endpoint absolute majorant 强约两个 logarithmic
powers；它保留了 base Möbius cancellation，但不需要对随 `r` 变化的局部
Euler factors建立新的 zero-free region。

## 3. 最短 Farey kernel 的 inverse-residue 平均

固定 `b>1`。对 `(a,b)=1`，令 `c=bar a mod b` 为 `1,...,b-1` 中的逆元，
并置

`k=(ac-1)/b`.                                       (11)

文档 091 对 `delta=1` 的公式成为

`U_(a,b)(1)=pi sin(pi/(ab))`

`              /[sin(pi c/b)sin(pi k/a)]>0`.        (12)

### 定理 SI（uniform dyadic row mass）

对 `A>=2`，

`sum_(A<a<=2A,(a,b)=1)U_(a,b)(1)`

` <=2pi^2 b/(3A)(floor(A/b)+1)`

`       *product_(p|b)(1-p^(-2)).`                  (13)

特别地，若 `A>=b/2`，则该 row sum 为 `O(1)`，常数与 `A,b` 无关。

#### 证明

由 `k/a=c/b-1/(ab)`。若 `c/b<=1/2`，sine 在 `[0,pi/2]` 的 concavity 与
`1/(ac)<=1/2` 给

`sin(pi k/a)>=(1/2)sin(pi c/b)`.                    (14)

若 `c/b>1/2`，左移 `1/(ab)` 要么使 sine 增大，要么只跨过其最大点；同一
`1/2` 下界仍成立。因此

`U_(a,b)(1)<=2pi^2/(ab)csc^2(pi c/b)`.              (15)

当 `a` 跑过长度 `A` 的区间，每个 reduced residue、因而每个 inverse `c`
至多出现 `floor(A/b)+1` 次。另一方面 Möbius inclusion--exclusion 与

`sum_(c=1)^(q-1)csc^2(pi c/q)=(q^2-1)/3`            (16)

给 exact reduced-residue identity

`sum_((c,b)=1)csc^2(pi c/b)`

` =b^2/3 product_(p|b)(1-p^(-2)).`                  (17)

把式 (15)--(17) 合并即得式 (13)。`□`

所以 `U_(a,b)(1)` 的 pointwise positive 性并不意味着 conductor-sized
average：接近 `pi^2/4` 的值只出现在极少数 inverse residues，完整一行的
总质量是常数而不是 `A`。

## 4. Shared gcd density 的精确 totient 抵消

对 odd squarefree `g`，文档 091 principal sieve density 是

`theta(g)=product_(p|g)(1-2/p)`.                    (18)

### 定理 SJ（shared-factor cancellation）

线性 amplitudes 的两个 local-factor losses 与式 (18) 合并后满足

`theta(g)(g/phi(g))^2`

` =product_(p|g)p(p-2)/(p-1)^2`

` =product_(p|g)[1-1/(p-1)^2]<=1`.                 (19)

若 `2|g`，整个 primitive stratum 为零。

#### 证明

逐 prime 化简即可；even case 是定理 RT。`□`

这是此前没有利用到的精确匹配：shared-GCD sieve 的密度恰好吸收了 uniform
conductor bound 中全部 `g/phi(g)` 平方损失。

## 5. 固定 shortest determinant sectors 已无条件消失

令

`L_N=max_(n<=N)n/phi(n)`.                            (20)

Rosser--Schoenfeld 的 classical totient bound 给

`L_N<<loglog(3N)`.                                   (21)

### 定理 SK（principal `delta=+/-1` contribution is `o(1)`）

在线性 Möbius filter 的全部 parabolic shells

`N<=Y<=N^(3/2)`                                     (22)

中，shared-GCD principal modes 的 `delta=+1` 与 `delta=-1` 总贡献绝对值
满足

`|C_N^(principal,|delta|=1)|`

` <<L_N^2/log N`

` <<(loglog(3N))^2/log N=o(1)`.                     (23)

#### 证明

对 `r=ga,r'=gb` 使用定理 SH。定理 SJ 消去全部 shared-`g` totient loss，
剩余 `(a/phi(a))(b/phi(b))<=L_N^2`。在 quotients 的 dyadic blocks
`a~A,b~B` 中，定理 SI 与 symmetry 给

`sum_(a~A,b~B)U_(a,b)(1)<<min(A,B)`.                (24)

对所有 dyadic `A,B<=H`，elementary geometric sum 给

`sum_(A,B<=H)min(A,B)<<H`.                           (25)

取 `H=N/g`，再放宽所有 hard-sector 与 determinant-window constraints，只会
增大正 majorant。因此式 (18) 的 smooth shell normalization 给

`|C_N^(principal,|delta|=1)|`

` <<L_N^2/(log N)^2`

`   *sum_(Y>=N dyadic)1/Y`

`   *sum_(g<=N)N/g`.                                 (26)

两个 sums 分别是 `O(1/N)` 与 `O(N log N)`，得到式 (23)。`delta=-1`
kernel 与 `delta=1` 相同；smooth Fourier weight 一致有界，只改变常数。`□`

式 (23) 已足以用于 Nyman convergence，尽管它比 conjecturally sharp
`O(1/log N)` 多两个 `loglog N` factors。

### 推论 SL（every fixed determinant window is harmless）

对任意固定 `D>=1`，所有 `0<|delta|<=D` 的 principal modes 总贡献仍为

`O_D(L_N^2/log N)=o(1)`.                             (27)

#### 证明

对固定 `delta`，当 dyadic larger quotient `A>=2D` 时，式 (14) 的证明只需
把 `1/(ac)` 换成 `|delta|/(ac)<=1/2`，并令
`c=delta bar a mod b`；乘以 `delta` 仍置换 reduced residues。有限多个
`A<2D` blocks 用定理 RS 的 uniform bound。逐 fixed `delta` 使用定理 SK 的
同一 dyadic summation即可。`□`

## 6. 存在性审计与广义接口

本节没有控制：

- `|delta|` 随 `N` 增长的 principal determinant tail；
- shared-GCD sieve 的 nonprincipal additive modes；
- 为精确 mean-zero Hodge projection 加入的高阶 polynomial directions 的
  uniform conductor stability。

但它排除了最短 positive kernel 作为独立障碍。文档 091 观察到该 kernel
没有 sign cancellation；本节证明它具有更强的 inverse-residue sparsity。

对一般 reciprocal Euler coefficients `beta(n)`，可抽象出一个可移植条件：
若 base logarithmic Riesz sums 一致有界，删除有限 Euler factors 后至多乘
`product_(p|r)(1-p^(-1))^(-1)`，且 shared-factor primitive density 吸收其
平方，则所有固定 determinant strata 同样消失。这给 generalized Weil/Hodge
结构增加了一个明确的“local removal stability”公理，而不是 zeta 特有技巧。

## 7. 计算实现

`scripts/qw_matrix.py` 新增：

- `mobius_logarithmic_riesz_sum`；
- `coprime_mobius_logarithmic_riesz_sum`；
- `local_smooth_convolution_riesz_sum`；
- `reduced_cosecant_square_sum`；
- `shortest_farey_kernel_row_sum`。

回归测试逐项核对式 (7)、式 (17)，并比较实际 shortest-kernel dyadic row
sum 与定理 SI 的显式上界。
