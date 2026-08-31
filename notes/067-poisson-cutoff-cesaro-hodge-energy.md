# Poisson cutoff、Cesàro Hodge 能量与临界 residue 常数

文档 066 的 radial Taylor residue 已把 RH 压缩成一列 finite prime
matrices。本笔记识别该 Taylor weight 的精确概率形态，并证明它等价于最经典
但现在完全 prime/Hodge 化的条件：annular energy 的累计质量至多线性增长。

这也算出 radial Taylor truncation 在临界边界保留的精确谱质量比例
`1-e^(-2)`。

## 1. Taylor exponential 是 Poisson cutoff

沿用

`r_R=1-1/R`,

`E_R(x)=sum_(j=0)^R x^j/j!`.                      (1)

定义 positive sampling weight

`W_R(t)=(2sigma_0/R)e^(-2sigma_0t)`

`                         *E_R(sigma_0r_Rt)^2`.   (2)

于是文档 066 的 residue 是

`H_R=int_0^infinity W_R(t)dmu(t)`,                (3)

其中

`dmu(t)=int_(h_0)^(h_1)|b_h(t)|^2dh dt`.          (4)

### 命题 LS（exact Poisson-cutoff formula）

若 `P_R(lambda)=P(Poisson(lambda)<=R)`，则

`W_R(t)=(2sigma_0/R)e^(-2sigma_0t/R)`

`                       *P_R(sigma_0r_Rt)^2`.     (5)

特别地，`W_R` 关于 `t` 非负且单调递减。

#### 证明

Poisson CDF identity

`E_R(lambda)=e^lambda P_R(lambda)`                (6)

代入式 (2)；因 `2sigma_0t-2sigma_0r_Rt=2sigma_0t/R`，得到式 (5)。
exponential factor 与 `P_R(lambda)` 都随 `t` 递减。`□`

所以 Taylor degree `R` 的作用不是任意 polynomial approximation，而是保留
Poisson count 不超过 `R` 的部分。

## 2. 缩放极限与保留质量

### 定理 LT（Poisson bulk cutoff and mass limit）

对每个 `x>=0, x!=1/sigma_0`，

`lim_(R->infinity)R W_R(Rx)`

` =2sigma_0e^(-2sigma_0x)1_(x<1/sigma_0)`.        (7)

并且

`lim_(R->infinity)int_0^infinity W_R(t)dt`

`                         =1-e^(-2)`.             (8)

更定量地，对每个 fixed `0<eta<1/sigma_0`，存在 `c_eta>0` 使 sufficiently
large `R` 满足

`W_R(t)>=c_eta/R`, `0<=t<=eta R`.                 (9)

#### 证明

在 `t=Rx` 时，Poisson parameter 是
`sigma_0(R-1)x`。大数律/Chernoff bound 给：若 `sigma_0x<1`，其不超过
`R` 的 probability 趋于 `1`；若 `sigma_0x>1`，则趋于 `0` exponentially。
式 (5) 随即给式 (7)。而且有统一可积支配

`R W_R(Rx)<=2sigma_0e^(-2sigma_0x)`，

所以 dominated convergence 给

`int_0^infinity W_R(t)dt`

` =int_0^infinity R W_R(Rx)dx`

趋于 `int_0^(1/sigma_0)2sigma_0e^(-2sigma_0x)dx=1-e^(-2)`。
若 `t<=eta R`，Poisson parameter 至多
`(sigma_0eta+o(1))R<R`，故 CDF uniformly 至少 `1/2`；式 (5) 给式 (9)。`□`

Taylor cutoff 因而保留 critical Abel/Cesàro mass 的固定比例，而不是趋零。

## 3. Radial residues 与线性累计能量完全等价

定义 cumulative width energy

`M(T)=mu([0,T])`

` =int_0^T int_(h_0)^(h_1)|b_h(t)|^2dh dt`.      (10)

### 定理 LU（radial--Cesàro equivalence）

以下条件等价：

1. `sup_(R>=2)H_R<infinity`；
2. `M(T)=O(1+T)`。

#### 证明

由式 (9)，对 fixed `eta<1/sigma_0`，

`H_R>=c_eta M(eta R)/R`.                          (11)

所以 1 推出 `M(eta R)=O(R)`；令 `R=ceil(T/eta)` 给 2。

反之，设 `M(T)<=A(1+T)`。因 `W_R` decreasing，Stieltjes integration by
parts 给

`H_R=int W_RdM`

` <=A[W_R(0)+int_0^infinity(1+t)(-dW_R(t))]`.     (12)

这里 `W_R(0)=2sigma_0/R`，且

`int(-dW_R)=W_R(0)`,

`int t(-dW_R)=int W_Rdt`。                        (13)

定理 LT 说明最后一项 uniformly bounded，故 `sup_R H_R<infinity`。`□`

这是纯正测度结论；不使用显式公式或零点。

## 4. Abel tightness、Cesàro growth 与 RH

### 定理 LV（positive Abel--Cesàro centerline theorem）

对 zeta 的 annular width trace，以下条件等价：

1. RH；
2. `sup_(0<sigma<=sigma_*)mathfrak G_sigma<infinity` 对某个
   `sigma_*>0`；
3. `M(T)=O(1+T)`；
4. `sup_R H_R<infinity`。

并且有精确 exponential identity

`limsup_(T->infinity)log M(T)/(2T)`

`                    =max(0,Theta-1/2)`.          (14)

#### 证明

先证一般 positive Abel--Cesàro comparison。若 `mathfrak G_sigma<=C`，取
`sigma=1/(2T)`，则

`mathfrak G_(1/(2T))`

` =(1/T)int e^(-t/T)dmu(t)>=e^(-1)M(T)/T`.        (15)

反之，若 `M(T)<=A(1+T)`，令 `s=2sigma`，Stieltjes integration by parts 给

`int e^(-st)dmu(t)=sint e^(-st)M(t)dt`，

故 `mathfrak G_sigma<=A(1+2sigma)`。这证明 2 与 3；定理 LU 给 3 与 4。
定理 KL/KN 给 1 与 2。

最后，对任意 positive measure，Laplace convergence abscissa 等于
`limsup_T log M(T)/T`：一个方向由 `M(T)<=e^(alpha T)` 积分，另一个方向
由 `L(s)>=e^(-sT)M(T)`。定理 KL 的 Laplace abscissa 为
`2max(0,Theta-1/2)`，给式 (14)。`□`

式 (14) 说明 linear bound、subexponential bound 与 centerline 在这里都等价；
linear bound 更强的外观来自 RH 下 critical almost-periodic energy 的有限
mean，而不是额外假设。

## 5. RH 下的精确 radial residue limit

令

`C_crit=int_(h_0)^(h_1)G_0(h,h)dh`

` =sum_gamma m_gamma^2/|1/2+igamma|^2`

`                       *m_(h_0,h_1)(gamma)`.     (16)

### 定理 LW（critical Taylor residue constant）

RH 下，

`lim_(T->infinity)M(T)/T=C_crit`,                 (17)

并且

`lim_(R->infinity)H_R=(1-e^(-2))C_crit`.          (18)

#### 证明

定理 KN 的 square-summable Besicovitch expansion 对 Cesàro mean 应用正交
关系，不同 ordinates 的 cross terms 消失，得到式 (17)。

一般地，若 `M(T)=CT+o(T)` 且 `W_R` 是定理 LT 的 decreasing kernels，
Stieltjes integration by parts 把

`int W_RdM-Cint W_Rdt`

写成 `M(T)-CT=o(T)` 对 `-dW_R` 的积分。先截去 fixed initial interval，
再用 `int t(-dW_R)=int W_Rdt=O(1)`，误差趋零。式 (8) 因而给式 (18)。`□`

常数 `1-e^(-2)` 量化了 degree `R` Taylor truncation 在同步边界
`r_R=1-1/R` 上保留的临界谱质量。

## 6. General Gamma--Euler Cesàro--RKHS theorem

### 定理 LX（general positive Cesàro Hodge structure）

对定理 LL/LR 的 paired Gamma--Euler current，令

`sigma_c=max(0,Theta-c/2)`。                       (19)

则

`limsup_(T->infinity)log M(T)/(2T)=sigma_c`.       (20)

以下条件等价：

1. 全部 divisor 位于 `Re rho=c/2`；
2. annular Abel Grams 在 `sigma downarrow0` uniformly tight；
3. cumulative Hodge energy `M(T)=O(T)`；
4. synchronized radial Taylor residues `H_R` uniformly bounded；
5. 定理 LR 的 finite Euler residues `H_R^[D]` uniformly bounded。

若 critical coefficients square summable，则 centerline 情形还有

`H_R->(1-e^(-2))C_crit`,                           (21)

其中 `C_crit` 是 divisor spectral weights 的 width trace。

#### 证明

定理 KP/LL 给 Abel abscissa与 centerline equivalence；定理 LU–LV 是任意
positive width-trace measure 的 Tauberian statements；定理 LP/LR 的
exponentially small finite cutoff 不改变 boundedness；square-summable
critical expansion 与定理 LW 给式 (21)。`□`

## 7. 对证明路线的影响

单列 finite Hodge matrix bound 现在有一个无矩阵术语的完全等价版本：

`int_0^T int_(h_0)^(h_1)|b_h(t)|^2dh dt=O(T)`.    (22)

这避免了 fixed sliding block 的过强要求；它是 anchored Cesàro mean。对
zeta，有限矩阵、RKHS completion、Abel tightness、Cesàro Hodge energy 与
RH 是同一缺口的五种严格等价表述。新的价值是可以在 prime side 选择最适合
筛法、large sieve 或 Hodge inequality 的版本，而不混淆局部与长期平均。

文档 074 将这里的 exponent identity 识别为一般 cyclic
Cesàro–Lyapunov Hodge theorem：exponential growth 检测 weight 偏移，临界
情形的 polynomial growth 检测 Jordan depth，uniform boundedness 则重建
exact polarization。
