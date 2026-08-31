# 三路线汇合：harmonic synthesis capacity 与 logarithmic occupancy 障碍

文档 175--177 分别得到 rank-one separators、Hodge transgression和 random-grid
Fejér identity。回到文档 167 的 authoritative threshold-complex接口后，需要作
一个关键区分：

- 对真实 Type II fiber `(m,q)`，external feature在 `K_U(q)` 上按 scalar
  identity作用，所以它与 threshold Dirac精确交换；内部 non-harmonic bulk
  已由 McKean--Singer完全消去；
- 未决困难发生在 fiber collapse之后：harmonic scalars `b_U(q)` 经
  logarithmic interval synthesis进入同一 physical Hilbert space，产生跨
  `(m,q)` 的 Gram。

本笔记把这个 external synthesis gap定量化。主要结论是：triangular/Fejér
Gram的 arbitrary-coefficient Bessel constant与长度 `h` 的 logarithmic local
occupancy在常数因子内等价。对 dyadic integers `n asymp N`，它必为
`Theta(1+Nh)`；因此在 square-root wedge、`h asymp1/T` 时，任何只结合
profinite diagonal与 arbitrary-coefficient Bessel bound的证明都会支付
`N/T` 的不可忽略放大。

## 1. 从内部 Hodge 到外部 synthesis

沿文档 167，令有限 index `j=(m,q)` 带 threshold complex `C_j`、Euler/Hodge
supertrace

`chi_j=b_U(q)`,                                  (1)

以及 external interval feature `xi_j in H_h`。因 `xi_j` 在 `C_j` 上为 scalar，

`sum_j Str_(H_h)[xi_j tensor exp(-tDelta_j)]`

` =sum_j chi_j xi_j`                             (2)

对全部 `t>=0` 精确成立。故文档 176 的 transgression在这个 canonical
fiber-constant realization中为零；它只在进一步引入 face-dependent weights时
出现。

定义 external synthesis

`T:c=(c_j) -> sum_j c_j xi_j`,                   (3)

Gram为 `G=T^*T`。则 harmonic current energy是

`||T chi||^2=chi^*Gchi`.                         (4)

local Laplacians的 positive spectra不出现在式 (4)中。文档 167 的 profinite
Gram控制 `chi` 的 weighted diagonal；要推出式 (4)，还需要 `G` 相对于该
diagonal weight的 Bessel/Loewner bound。

## 2. Random cells 给 exact capacity

先研究 canonical triangular carrier。给定有限 points `x_1,...,x_M in R` 与
`h>0`，定义

`K_h(alpha,beta)`

` =(1-|x_alpha-x_beta|/h)_+`.                   (5)

令 local occupancy为

`M_h=sup_(a in R)# {alpha:x_alpha in [a,a+h)}`. (6)

### 定理 AEU（Fejér capacity versus local occupancy）[U]

有 Loewner bound

`0<=K_h<=M_h I`,                                (7)

并且

`1/2 M_(h/2)<=lambda_max(K_h)<=M_h`.            (8)

因此 triangular Gram的最优 arbitrary-coefficient Bessel constant在 local
occupancy的常数因子内。

#### 证明

用文档 177 的随机平移 cells `I_(k,theta)`。令 `P_theta` 把 coefficient vector
送到各 cell sum，则

`K_h=E_theta[P_theta^*P_theta]`.                 (9)

固定 `theta` 时，`P_theta^*P_theta` 是按 cells分块的 all-ones matrices；每块
唯一非零 eigenvalue等于该 cell的 occupancy，故

`P_theta^*P_theta<=M_h I`.                      (10)

取期望得式 (7)及上界。

再取一个长度 `h/2` 区间，含 `M_(h/2)` 个 points，令 `u` 在这些坐标上等于
`M_(h/2)^(-1/2)`、其余为零。任意两点距离小于 `h/2`，故相应
`K_h(alpha,beta)>=1/2`。于是

`u^*K_hu>=M_(h/2)/2`,                           (11)

给出下界。`□`

定理 AEU同时识别文档 175 的 dominant rank-one separator：它可取为 densest
logarithmic interval上的近常数 packet。随机 partition不会消除该 packet，因为
它正是 random cell Gram的最大 singular direction。

## 3. Dyadic integer logarithms 的 sharp scale

取

`X_N={log n:N<=n<2N}`, `N>=2`,                  (12)

并记相应 occupancy为 `M_h(N)`。

### 定理 AEV（dyadic logarithmic occupancy）[U]

对 `0<h<=1`，

`M_h(N)<=1+2N(e^h-1)<=1+4Nh`,                  (13)

且

`M_(h/2)(N)>=max{1,Nh/2-1}`.                   (14)

所以

`max{1/2,Nh/4-1/2}`

` <=lambda_max(K_h)`

` <=1+4Nh`.                                    (15)

特别地，当 `Nh->infinity` 时最佳 Bessel常数为 `Theta(Nh)`。

#### 证明

任意 log interval `[a,a+h)` 对应 ordinary interval
`[e^a,e^(a+h))`。在 `[N,2N)` 内其长度至多 `2N(e^h-1)`，故整数点数至多式
(13)第一项；`e^h-1<=2h` 对 `0<h<=1` 给第二项。

另一方面 `[log N,log N+h/2)` 含所有

`N<=n<Ne^(h/2)`.                                (16)

其数目至少 `N(e^(h/2)-1)-1>=Nh/2-1`，并至少含 `n=N`，得式 (14)。
代入定理 AEU即得式 (15)。`□`

## 4. Harmonic diagonal 到 physical Gram 的代价

设 fiber collapse后 Type II coefficients为 `c_n`，`N<=n<2N`，相应
triangular energy为

`Q_(N,h)(c)=sum_(n,n')c_n conjugate(c_(n'))`

`              (1-|log(n/n')|/h)_+`.           (17)

### 推论 AEW（occupancy-weighted harmonic synthesis）[U]

无条件有

`Q_(N,h)(c)<=(1+4Nh)sum_(N<=n<2N)|c_n|^2`.     (18)

在 `h asymp1/T` 的 spectral block上，任意系数 Bessel route必须允许大小

`B_(N,T) asymp1+N/T`.                           (19)

更精确地，当 `N/T->infinity`，存在 coefficient vectors使

`Q_(N,h)(c)/sum|c_n|^2 >> N/T`.                 (20)

#### 证明

式 (18)由定理 AEV的 operator-norm上界。式 (20)取定理 AEU证明中的 densest
interval常数向量，并用式 (14)。`□`

式 (20)是 arbitrary-coefficient theorem的 sharp no-go，不声称真实
`R_II(n)` 必取最坏向量。它说明：文档 167 的 polylogarithmic coefficient
diagonal若只通过一个对所有 coefficients有效的 Bessel bound进入 physical
Gram，就必须额外支付 `N/T`。在文档 169 剩余的

`N>T^(2-eta)`                                       (21)

区域，该放大至少达到 `T^(1-eta)`，远大于 logarithmic Cauchy barrier。故这条
组合不可能闭合。

## 5. 三路线的正确汇合

定理 AEU--AEW把文档 175--177的关系固定为：

1. **rank-one dual：** 最坏 external obstruction是一个 packet `u`；
2. **random Fejér realization：** packet energy是 random cell sums的平均；
3. **occupancy barrier：** 任意系数 packet在 densest cell上产生 `Theta(Nh)`
   amplification；
4. **internal Hodge exactness：** threshold Laplacian已把 coefficient降到
   harmonic `b_U(q)`，但不控制上述 external amplification。

因此下一步必须使用最坏向量不具备的真实算术性质，而非继续改进 universal
Bessel常数。候选输入只有：

- Möbius boundary signs对 densest rank-one packet的定向 cancellation；
- prime--continuum--Gamma在 cell sum内部先 joint gluing；
- Selberg--Volterra prefix transport的某个比 full profile更单侧的版本；
- 一个跨不同 `q` fibers的 genuine arithmetic correspondence，直接限制
  allowable rank-one packets。

## 6. 新的最小目标

令 `u_I` 是任意长度 `h/2` logarithmic interval上的 normalized constant packet。
一个比 arbitrary-coefficient Bessel严格更弱、又直接命中 sharp obstruction的
目标是

`sum_I |<u_I,c^(arith)>|^2 <= C_T`,             (22)

其中 intervals取 bounded-overlap cover，`c^(arith)` 是已经完成
Möbius fiber collapse及 prime/continuum/Gamma joint centering的真实系数，
而 `C_T` 除以 barrier后可和。

式 (22)只测试 occupancy产生的 dominant packet族，不测试任意 coefficients。
文档 175 的 finite dual说明，如果还可证明 polar extreme rays均被这族与一个
可控 remainder捕获，就能接回 AEJ。若真实算术系数在式 (22)上仍达到
`Nh` worst case，则 NCE-1/3组合应停止，转向 nonlocal correspondence。

## 7. 审计结论

本笔记无条件证明：

- external Fejér synthesis capacity与 local occupancy的双边界；
- dyadic logarithmic carrier上 `Theta(1+Nh)` 的 sharp尺度；
- square-root wedge中 arbitrary-coefficient Bessel路线的 polynomial loss；
- threshold Hodge内部精确性与外部 cross-polarization之间的定量分界。

这不是 RH 证明，但它删除了一个过宽方向：profinite diagonal不能经 universal
Bessel estimate直接升级为所需 physical Gram。下一轮应只估计真实算术
coefficients对 densest-cell rank-one packets的响应。
