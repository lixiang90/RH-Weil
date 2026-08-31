# Möbius log-mollifier、almost-prime filtration 与 sawtooth Hodge current

文档 082 把可行目标校准为构造 arithmetic trial vector，使 Nyman--Beurling
residual 达到 `O(1/log N)`。本节分析最自然的 Möbius log-polynomial
mollifiers。新结构是：degree `R` 的 log smoothing 在完整低除数区
`m<=N` 只产生至多含 `R` 个不同素因子的 charges；线性 smoothing 的 defect
精确就是 von Mangoldt prime-power current。所有困难被隔离到 `m>N` 的
truncated-divisor tail。

## 1. Polynomially filtered formal inverse

令 `P(u)=sum_(j=0)^R p_j u^j` 且 `P(0)=p_0=1`。定义

`b_(N,P)(n)=mu(n)P(log n/log N) 1_(n<=N)`,             (1)

`A_(N,P)(s)=sum_(n<=N)b_(N,P)(n)n^(-s)`.              (2)

`zeta A_(N,P)` 的 Dirichlet coefficient 是

`c_(N,P)(m)=sum_(d|m,d<=N)b_(N,P)(d)`.                (3)

再定义 Möbius logarithmic moments

`M_j(m)=sum_(d|m)mu(d)(log d)^j`.                       (4)

### 定理 PO（complete low-convolution formula）

对 `m<=N`，

`c_(N,P)(m)=delta_(m,1)`

`             +sum_(j=1)^R p_j M_j(m)/(log N)^j`.      (5)

因此

`1-zeta(s)A_(N,P)(s)`                                 (6)

在 indices `2<=m<=N` 的 coefficients 是式 (5) 右侧非平凡部分的负值；
所有 `m>N` coefficients 则构成 truncated-divisor tail。

#### 证明

当 `m<=N` 时，每个 divisor `d|m` 自动满足 `d<=N`。把 polynomial 展开，
constant term 给 `sum_(d|m)mu(d)=delta_(m,1)`，其余逐项就是式 (4)。`□`

hard Möbius cutoff `P=1` 精确消去前 `N` 个非平凡 coefficients；但这并不
控制 critical norm。加入 log smoothing 会牺牲这种低阶完全相消，换来 cutoff
边界的正则性和可解析的 local defect。

## 2. Almost-prime support theorem

令 `omega(m)` 是 `m` 的不同素因子个数。

### 定理 PP（log-moment support filtration）

对每个 `j>=0`，

`M_j(m)=0  whenever omega(m)>j`.                        (7)

若 `omega(m)=j`，写 distinct prime divisors 为 `p_1,...,p_j`，则

`M_j(m)=(-1)^j j! product_(r=1)^j log p_r`.             (8)

因此 degree-`R` polynomial mollifier 的完整低 residual 只支撑在
`omega(m)<=R` 的 almost-prime strata 上；prime powers 属于第一层。

#### 证明

只有 squarefree divisors 对式 (4) 有贡献。令 `x_r=log p_r`，则

`M_j(m)=sum_(S subset {1,...,omega(m)})`

`             (-1)^|S| (sum_(r in S)x_r)^j`.           (9)

这是 polynomial `u^j` 的 `omega(m)` 阶 finite difference。阶数大于 degree
时为零；阶数等于 degree 时只剩 mixed monomial，给式 (8)。`□`

这给出一个 multiplicative Lefschetz-like filtration：polynomial degree 是
arithmetic codimension，`j`-th graded defect 由至多 `j` 个 prime directions
组成。

## 3. Linear smoothing gives the von Mangoldt current

取

`P_1(u)=1-u`.                                           (10)

经典 convolution identity 为

`M_1(m)=sum_(d|m)mu(d)log d=-Lambda(m)`.               (11)

### 推论 PQ（exact prime-power defect）

令

`V_N(s)=sum_(n<=N)mu(n)(1-log n/log N)n^(-s)`.          (12)

则对 `2<=m<=N`，

`[zeta V_N](m)=Lambda(m)/log N`,                        (13)

即

`zeta(s)V_N(s)`

` =1+(1/log N)sum_(2<=m<=N)Lambda(m)m^(-s)`

`   +sum_(m>N)c_N(m)m^(-s)`.                           (14)

#### 证明

在式 (5) 取 `p_1=-1`，再用式 (11)。`□`

因此 BCF/Báez-Duarte 型 linear mollifier 的低阶误差不是未知噪声，而是规范
von Mangoldt current，尺度恰为 `1/log N`。这解释了 Burnol lower bound 所
要求的自然 rate。

## 4. Real-space sawtooth flow

令 `b_n=b_(N,P)(n)`，并在 reciprocal coordinate `y=1/x` 定义

`F_(N,P)(y)=1_(y>=1)+sum_(n<=N)b_n {y/n}`.             (15)

Nyman trial residual 是

`f_(N,P)(x)=chi_(0,1)(x)+sum_(n<=N)b_n {1/(nx)}`

`            =F_(N,P)(1/x)`.                          (16)

### 定理 PR（prime-charge jump equation）

在 distributions on `(0,infinity)` 中，

`dF_(N,P)=A_(N,P)(1)dy`

`          -sum_(m>=2)c_(N,P)(m)delta_m`.              (17)

`y=1` 处 indicator 的 `+1` jump 与 `b_1{y}` 的 `-1` jump 精确相消。
此外

`R_(N,P):=||f_(N,P)||_(L^2(dx))^2`

`          =int_0^infinity |F_(N,P)(y)|^2dy/y^2`.      (18)

#### 证明

每个 `{y/n}` 在非整数 jump 之间 derivative 为 `1/n`，故总连续 slope 是
`sum b_n/n=A_(N,P)(1)`；在 integer `m` 的 jump 为
`-sum_(n|m,n<=N)b_n=-c_(N,P)(m)`。`m=1` 的 cancellation 来自 `b_1=P(0)=1`。
变量替换 `y=1/x` 给式 (18)。`□`

在线性情形，式 (17) 在 `2<=m<=N` 的 jumps 精确为
`-Lambda(m)/log N`；`m>N` 的 jumps 是唯一尚未简化的 global tail。

## 5. Positive Hodge upper certificate

由文档 081 的 Mellin Plancherel，

`R_(N,P)`

` =(1/(2pi))int_R |1-zeta(s)A_(N,P)(s)|^2/|s|^2dt`,

`s=1/2+it`.                                             (19)

### 定理 PS（mollifier Hodge certificate）

对 optimal Nyman distance，

`0<=d_N^2<=R_(N,P)`.                                   (20)

因此只要存在一列 explicit polynomials `P_N`（degree 可随 `N` 变）满足

`R_(N,P_N)->0`,                                        (21)

就能推出 RH；若进一步

`R_(N,P_N)<=C/log N+o(1/log N)`,                       (22)

则达到文档 082 所校准的 sharp scale。

#### 证明

`A_(N,P)` 是 Nyman minimization 中的一个合法 length-`N` Dirichlet
polynomial，故 optimal distance 不超过其 residual norm。定理 PD 再给
式 (21) `=>RH`。`□`

每个 `R_(N,P)` 本身是无条件 positive finite-feature Hodge norm；困难不是
定义或正性，而是证明 cofinal decay。

## 6. Local almost-prime core 与 global tail

把式 (17) 的 charge 分成

`J_local=sum_(2<=m<=N)c_(N,P)(m)delta_m`,

`J_tail =sum_(m>N)c_(N,P)(m)delta_m`.                  (23)

### 定理 PT（exact obstruction split）

1. `J_local` 由定理 PO/PP 完全显式，且支撑在 `omega(m)<=R`；
2. linear case 的 `J_local` 就是 `Lambda(m)/log N`；
3. `J_tail` 包含 cutoff 与任意大 composite integers 的全部相互作用；
4. 任何仅估计 `J_local` 的证明都不能推出式 (21)，因为 weighted potential
   norm (18) 还含 local--tail cross term 和 tail self-energy。

#### 证明

前三项来自 definitions 与定理 PP/PQ。固定由 jump current 到 potential 的
同一线性 Green normalization 后，式 (18) 对 `F_local+F_tail` 展开给第四项。
`□`

对 `J_tail` 作逐项绝对值估计会丢失 Möbius cancellation；结合文档 079/082
的 no-go，合理工具应是 large-sieve、Mellin contour 或 Feshbach/Gram
alignment，而不是 local Euler product 或粗 inverse norm。

## 7. Degree filtration 的取舍

### 结论 PU（mollifier design audit）

- `P=1`：低 coefficients 完全消失，但 cutoff discontinuity 把全部困难推到
  hard tail；
- `P=1-u`：endpoint vanishing，并把低 defect 变成可识别的 prime-power
  current；
- degree `R`：可匹配更多 cutoff jets，但会引入前 `R` 个 almost-prime
  strata；
- degree 随 `N` 增长：可能逼近 optimal Gram coefficients，但必须同时控制
  almost-prime core 的组合增长和 global tail。

Bettin--Conrey--Farmer 在 RH 与 reciprocal-zero-derivative moment hypothesis
下证明 linear mollifier 达到 Burnol constant。无条件重证其 upper estimate
会证明 RH；其证明中对 zero residues 的控制，正对应式 (23) 的 global tail
而不是 local von Mangoldt identity。

所以本节没有证明式 (21)，但把候选的 arithmetic differential 完整分层：
低阶 Hodge current 已无条件求出，唯一开放输入是 tail potential 及其与 local
almost-prime core 的相消。

## 8. 计算实现

`scripts/qw_matrix.py` 新增：

- `mobius`；
- `mobius_log_divisor_moment`；
- `polynomial_mobius_mollifier_coefficients`；
- `zeta_mollifier_low_convolution`；
- `beurling_mollifier_residual`。

回归测试逐项核对 `N=30` 的式 (13)，并验证 `M_1(6)=0`、
`M_2(6)=2log2log3`、`M_2(30)=0`，从而同时检测 sign、factorial 与
almost-prime support。real-space residual 也与 feature sum 逐点一致。
