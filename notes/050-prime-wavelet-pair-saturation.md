# Prime-wavelet pair Gram 与 diagonal saturation

文档 048–049 把中心线问题压到 local prime-wavelet 的临界 `L^2`
tightness，并无条件解决了其 endpoint-core/translation operator 的正性与
可逆性。本笔记把剩余 `L^2` 量完全展开成有限 prime-pair Gram。

结果显示一个精确障碍：von Mangoldt diagonal 单独贡献

`(6-8log2)log2 * log X+O(1)`.                      (1)

RH 蕴含非对角 prime correlations 与连续背景把这个正对数主项抵消到
`O(1)`，且这一精确 saturation 与 RH 等价。要**直接构造临界 GNS**确实
需要这种 `O(1)`；但只为推出 RH，任意 `X^o(1)` upper bound 已足够。

## 1. Compact local prime kernel

定义非负 compact kernel

`phi(r)=0`,                              `r<=1/2`,

`phi(r)=2-r^(-1)`,                 `1/2<r<=1`,

`phi(r)=2r^(-1)-1`,                   `1<r<=2`,

`phi(r)=0`,                                `r>2`.   (2)

### 命题 HS（finite local prime-wavelet formula）

文档 048 的 merged charge 满足

`z(L)=sum_n Lambda(n)phi(n/L)-Llog2`.                (3)

和只涉及 `L/2<n<=2L`。kernel 的两个基本 moments 为

`int_0^infinity phi(r)dr=log2`,                     (4)

`A_phi=int_0^infinity phi(r)^2dr=6-8log2`.         (5)

#### 证明

由式 (22) 交换 `psi(Ly)=sum_(n<=Ly)Lambda(n)` 与有限积分。固定 `n` 的
feature 是

`int_(max(1/2,n/L))^2 w(y)dy`;                     (6)

在 `n/L` 的四个区间直接积分文档 048 的 `w`，得到式 (2)。continuum
项为

`-L int_(1/2)^2 w(y)y dy=-Llog2`.                  (7)

式 (4)–(5) 对两个 elementary rational pieces 积分；特别地

`A_phi=6-log256=6-8log2>0`.                        (8)

`□`

式 (3) 是完全局部、正权的 smoothed prime count 减其 continuum mean。

## 2. 每个 log block 的有限 pair Gram

定义一个固定长度的 log-block energy

`C(X)=int_X^(2X)|z(L)|^2 L^(-2)dL`

`    =int_(logX)^(log2X)|y(t)|^2dt`.                (9)

对正整数 `m,n`，令

`K_X(m,n)=int_X^(2X)L^(-2)phi(m/L)phi(n/L)dL`,     (10)

`J_X(n)=int_X^(2X)L^(-1)phi(n/L)dL`.               (11)

### 定理 HT（exact finite prime-pair expansion）

有精确恒等式

`C(X)=sum_(m,n)Lambda(m)Lambda(n)K_X(m,n)`

` -2log2 sum_n Lambda(n)J_X(n)+(log2)^2X`.          (12)

所有 sums 都有限：只有 `X/2<m,n<=4X` 可能贡献。`K_X` 是正 Gram
kernel，并满足 scaling

`K_X(m,n)=X^(-1)mathcal K(m/X,n/X)`.               (13)

若 `m/n` 不在 `(1/4,4)`，则 `K_X(m,n)=0`。

#### 证明

把式 (3) 平方后逐项在 `[X,2X]` 积分，得到式 (12)。正性来自 features
`L^(-1)phi(n/L)` 的 Gram。support 与有限范围来自式 (2)；令 `L=Xu`
得到式 (13)。`□`

所以所需 arithmetic input 只涉及 factor `4` 内的 prime pairs，不涉及
任意远距离 additive/multiplicative correlations。

## 3. Universal diagonal logarithm

把式 (12) 的 prime-prime diagonal 记为

`D(X)=sum_n Lambda(n)^2K_X(n,n)`.                  (14)

### 定理 HU（diagonal asymptotic）

当 `X->infinity`，

`D(X)=A_phi log2 logX+O(1)`                        (15)

`=(6-8log2)log2 logX+O(1)`.                       (16)

数值系数为

`(6-8log2)log2=0.315258972014...`.                 (17)

#### 证明

PNT 与 partial summation 给标准二阶 Mangoldt law

`sum_(n<=x)Lambda(n)^2=xlogx-x+O(x exp(-c sqrt(logx)))`. (18)

对 compact piecewise `C^0` 权 `phi^2` 再作 partial summation，一致得到

`sum_n Lambda(n)^2phi(n/L)^2`

`=LlogL int phi(r)^2dr+O(L)`.                      (19)

代入式 (14) 的 integral 形式：

`D(X)=int_X^(2X)L^(-2)`

`                 sum_n Lambda(n)^2phi(n/L)^2dL`. (20)

主项为

`A_phi int_X^(2X)(logL)/L dL`

`=A_phi log2 logX+O(1)`；误差积分为 `O(1)`。`□`

diagonal 本身严格发散，即使所有有限 Gram matrices 都为正。

## 4. RH 等价于 anti-Poisson saturation

令

`R_pair(X)=C(X)-D(X)`                              (21)

为式 (12) 中“非对角 prime pairs + prime--continuum cross + continuum
square”的总和。

### 定理 HV（pair-saturation criterion for RH）

下列条件等价：

1. RH 成立；
2. `C(X)=O(1)`；
3. 对每个 `epsilon>0`，`C(X)=O_epsilon(X^epsilon)`；
4. 有精确 saturation

   `R_pair(X)=-(6-8log2)log2 logX+O(1)`.           (22)

#### 证明

RH 下文档 HJ 的 divisor expansion 对 wavelet 多一次 Riesz smoothing，
coefficients 为 `O(|rho|^(-2))`，故 `y(t)` 是 bounded uniform
almost-periodic 主项加衰减项；于是每个长度 `log2` 的积分 `C(X)` 一致
有界。

条件 2 显然给 3。若 3 成立，把 `[1,infinity)` 分成 dyadic log blocks；
对任意 `sigma>0` 取 `epsilon<2sigma`，则

`int |y(t)|^2e^(-2sigma t)dt`

`<=sum_k 2^(-2sigma k)C(2^k)<infinity`.            (23)

定理 HJ 遂给 RH。最后，由定理 HU，条件 2 与式 (22) 等价。`□`

式 (22) 是一个具体的、有限尺度的 prime-pair statement；它不引用零点，
却具有 RH 的全部强度。

## 5. Boundary tightness 与 subpower center-line bridge

### 定理 HW（diagonal scale cannot give critical tightness, but subpower suffices for RH）

1. 任何 certificate 若保留正 diagonal 而不证明式 (22) 的 signed
   cancellation，都不能推出 `C(X)=O(1)`，因其至少含

   `(6-8log2)log2 logX+O(1)`.                      (24)

2. 反之，只要能对**完整 centered form**证明

   `C(X)<=X^(o(1))`，                               (25)

   例如 `C(X)=O(log(X)^A)`，就已经推出 RH。

#### 证明

第一项来自定理 HU。第二项就是定理 HV 的条件 3，因为任意 subpower bound
都被每个固定 `X^epsilon` 最终支配。`□`

所以 logarithmic loss 只妨碍直接到达临界 Hilbert space，不妨碍先证明
中心线。真正有用的 large sieve 必须控制**完整 centered pair form**；把
prime-prime、cross、background 分别取绝对值通常只给多项式尺度，无法
得到式 (25)。

## 6. Centered pair measure 与可攻击接口

把 local prime measure 写成

`dmu_L(r)=sum_n Lambda(n)delta_(n/L)-Ldr`.          (26)

则

`z(L)=int phi(r)dmu_L(r)`,                          (27)

`C(X)=int_X^(2X)|int phi dmu_L|^2L^(-2)dL`.        (28)

因此式 (22) 可由下列任一更强输入推出：

1. centered pair measures 在 test `phi tensor phi` 上的 uniform finite
   total variation/cancellation；
2. factor-`4` multiplicative dispersion estimate，保留 continuum cross；
3. 文档 047 的 block-tridiagonal remainder 与 endpoint AR(1) core 的
   uniform Schur bound；
4. 对 `z(L)` 本身的 Selberg-type mean square `C(X)=O(1)`。

前三项是结构化证明接口；第四项就是最小标量目标。

## 7. Gamma--Euler pair-saturation theorem

### 定理 HX（general local pair-saturation structure）

设 complex Gamma--Euler data 满足定理 HL，并且其 squared Euler
coefficients 有 Rankin--Selberg diagonal law

`sum_(n<=x)|Lambda_Z(n)|^2=kappa_Z xlogx+O(x)`.     (29)

则 local wavelet block energy 的 diagonal 主项为

`kappa_Z(6-8log2)log2 logX+O(1)`.                  (30)

若 centered non-diagonal/background pair form 以其负值抵消式 (30) 到
`O(1)`，则相应 divisor 全部位于中心线；Sobolev 版本产生定理 HQ 的
Laurent-wavelet Weil datum。

#### 证明

定理 HU 的 partial-summation proof 把式 (18) 换成式 (29)，给式 (30)。
抵消后 local block energies 一致有界，定理 HL/HQ 给中心线与结构。`□`

primitive Dirichlet twists 的 `kappa_Z=1`（忽略有限 conductor primes）；
automorphic 情形的 `kappa_Z` 由相应 Rankin--Selberg diagonal 决定。

## 8. 存在性审计

无条件完成的是：

- finite pair Gram (12)；
- factor-`4` support；
- diagonal 的完整 `+0.315257...logX` 主项；
- zeta/Gamma--Euler 的 saturation-implies-center-line 结构定理。

未完成的是式 (22) 的负 correlation 主项。数值检查必须同时报告
`D(X)` 与 `R_pair(X)`；只观察很小的 total `C(X)` 会隐藏两个大项的相消，
也不能外推到所有尺度。

### 有限相消审计

脚本的有限 pair expansion 给出：

| `X` | `C(X)` | `D(X)` | `R_pair(X)` | prime-pair | cross | background |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.001294 | 0.664835 | -0.663541 | 3.795388 | -7.637718 | 3.843624 |
| 16 | 0.001227 | 0.884204 | -0.882977 | 7.753557 | -15.439579 | 7.687248 |
| 32 | 0.001357 | 1.126711 | -1.125354 | 15.309013 | -30.682152 | 15.374496 |

可见很小的 total 是三个 `O(X)` 项先相消、再由 centered remainder 抵消
正 diagonal 的结果。解析 diagonal coefficient 为
`0.315258972014...`；`D(X)/logX` 在 `X=101,1009,10007` 分别为
`0.326243,0.327946,0.326145`。这些有限值验证式 (12) 的 bookkeeping；
它们不证明式 (22) 对所有 `X` 成立。
