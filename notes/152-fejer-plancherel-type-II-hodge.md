# Fejér--Plancherel 精确对偶与 Type I/II Hodge tensor 接口

文档 151 用 frequency-shifted Gallagher lemma把 modulated short-interval energy
接到 Cauchy negative trace。本节证明该接口本身有一个 exact Plancherel identity，
并把 multiplicative convolution通过 `log(dm)=logd+logm` 表示成 unitary
translations。这样 Vaughan/Heath--Brown identity不再只是“可能使用的解析工具”，
而成为 generalized Hodge structure中的 tensor factorization。

## 1. Triangular kernel 与 Fejér weight 的 exact identity

沿文档 151，令 `nu_tau=e^(-itaulambda)nu`，`h>0`，并定义 sliding vector

`g_(tau,h)(x)=nu_tau([x,x+h])`.                    (1)

令

`D(t)=int e^(-itlambda)dnu(lambda)`.               (2)

### 定理 AAR（exact Fejér--Gallagher Plancherel identity）

有

`int_R|g_(tau,h)(x)|^2dx`

` =(1/(2pi))int_R |D(tau+s)|^2 W_h(s)ds`,         (3)

其中

`W_h(s)=|int_0^h e^(-isu)du|^2`

` =4sin^2(sh/2)/s^2`,                             (4)

并在 `s=0` 连续取值 `W_h(0)=h^2`。

#### 证明

把式 (1)写成

`g(x)=int 1_[lambda-h,lambda](x)dnu_tau(lambda)`. (5)

对 `x` 作 Fourier transform，Fubini给

`g_hat(s)=D(tau+s)int_0^h e^(isu)du`,             (6)

若改用相反 interval orientation只会多一个 unit phase，不影响 modulus。
Plancherel theorem立即给式 (3)--(4)。对 finite measures先作 compact truncation及 smooth
approximation，再以 monotone/Fatou passage；zeta Abel measure因 exponential
weight本身已有 finite total variation。`□`

所以文档 151 的 triangular Gram是 physical-lag side，Fejér-localized Fourier
energy是 spectral side；二者不是估计，而是同一个 Hodge norm。

## 2. 显式 frequency-band constant

取 `h=theta/B`, `0<theta<pi`。对 `|s|<=B`，

`|sh/2|<=theta/2`,                                (7)

故

`W_h(s)>=h^2 sinc(theta/2)^2`,                    (8)

其中 `sinc(u)=sin(u)/u`。

### 推论 AAS（explicit shifted-Gallagher constant）

`int_(tau-B)^(tau+B)|D(t)|^2dt`

` <=C_theta B^2 int_R|g_(tau,h)(x)|^2dx`,         (9)

其中可取

`C_theta=2pi/[theta^2sinc(theta/2)^2]`.           (10)

#### 证明

在式 (3)中只保留 `|s|<=B`，使用式 (8)并整理。`□`

实现 `gallagher_fejer_band_constant` 返回式 (7)--(10)的 `h`、minimum Fejér
weight、dimensionless `C_theta` 与完整 `C_theta B^2` multiplier。因此文档 151
定理 AAM中的隐常数现已完全显式。

## 3. Interval-incidence Hilbert representation

令

`H_h=L^2(R,dx)`,

`e_lambda=1_[lambda-h,lambda] in H_h`.             (11)

定义 unitary translation

`(U_a f)(x)=f(x-a)`.                              (12)

则

`e_(lambda+a)=U_a e_lambda`.                      (13)

对 finite measure `nu` 定义 Hodge vector

`V_(nu,tau)=int e^(-itaulambda)e_lambda dnu(lambda)`. (14)

### 定理 AAT（multiplicative-length translation realization）

有

`||V_(nu,tau)||_(H_h)^2=G_nu(tau,B;theta)`,       (15)

且对 positive integers `d,m`，

`e_(log(dm))=U_(logd)e_(logm)`.                   (16)

因此任何 Dirichlet convolution `c=a*b` 的 atomic vector精确写成

`V_c=sum_d a_d d^(-itau)U_(logd)W_d`,             (17)

其中若另有 nonseparable weight `w_(dm)`，则

`W_d=sum_m b_m w_(dm)m^(-itau)e_(logm)`.          (18)

#### 证明

式 (15)展开 inner product并使用

`<e_lambda,e_mu>=(h-|lambda-mu|)_+`,              (19)

即文档 151 定理 AAQ。式 (16)来自 logarithm additivity与式 (13)。把
`c_n=sum_(dm=n)a_db_m` 代入式 (14)，按 `d,m` 重排，得到式 (17)--(18)。`□`

这给出一个真正的 algebraic realization：Dirichlet convolution变成 translation
tensor synthesis，Abel weight `e^(-dm/Y)` 虽不 separable，却只使 inner vector
依赖 outer index `d`，不破坏 identity。

## 4. Balanced Type I/II Hodge criterion

对每个 dyadic spectral block `k`，设完整 prime--continuum signed measure已由
Vaughan、Heath--Brown或其它 exact convolution identity分为固定数量 `R` 的
**balanced components**

`nu_k=sum_(r=1)^R nu_(r,k)+epsilon_k`.             (20)

“balanced”表示 continuum main term必须与产生它的 Type I component放在同一个
`nu_(r,k)` 中，而不是最后用 triangle inequality单独拆掉。假设每个 component的
Hodge vector有式 (17)并满足 Bessel synthesis bound

`||sum_d alpha_dU_(logd)W_d||^2`

` <=B_(r,k)sum_d|alpha_d|^2||W_d||^2`.            (21)

### 定理 AAU（Type I/II Bessel--Hodge center-line criterion）

在文档 151 定理 AAO的 analytic/barrier hypotheses下，若

`sup_n {core_negative_trace`

` +sum_k 1/beta_(n,k) [ Rsum_r B_(r,n,k)`

`       *sum_d|alpha_(r,d)|^2||W_(r,d)||^2`

`       +(R+1)||V_(epsilon_(n,k),tau_(n,k))||^2 ]}<infinity`, (22)

其中 dyadic `B_k^2/(1+T_k^2)` 已吸收到 uniform常数，则相应 divisor全部 zeros
位于中心线。

#### 证明

由式 (20)及 `||sum_(j=1)^(R+1)v_j||^2<=(R+1)sum||v_j||^2`，再对每个
convolutional component应用式 (21)，得到 modulated energy `G_k` 被式 (22)方括号
控制。对 `k` 求和并应用文档 151 定理 AAO。`□`

定理 AAU并未把困难藏在“存在某个 Hilbert space”中：`H_h,U_a,e_lambda` 已全部
canonical，Vaughan/Heath--Brown convolution identity也无条件。唯一新输入精确是
actual balanced Type I/II translated vectors的 Bessel budget式 (22)。

## 5. 为什么 continuum 必须在 component 内配平

若先写

`||V_prime-V_continuum||^2`

` <=2||V_prime||^2+2||V_continuum||^2`,           (23)

就删除了文档 151 finite audit中占主导的 negative off-diagonal cancellation。
例如 `Y=30,T=2` 时 diagonal为 `1.1573`，off-diagonal为 `-.9036`，完整 energy只有
`.2537`。因此式 (20)要求 balanced decomposition不是审美选择，而是保持 Weil
prime--Tate cancellation的必要结构。

一个可行的 exact organization是先对

`d[psi(u)-u]`                                     (24)

应用 combinatorial identity：`du` 与 identity/Type I main term成对，Möbius或
bilinear remainder进入 Type II components。任何 discretization error保留为
`epsilon_k` 并在式 (22)单独计 norm，不能静默丢弃。

## 6. 对 GRH/automorphic data 的存在性

对 fixed-degree tempered Euler data，generalized von Mangoldt coefficients可写为
有限 Satake phases之和。logarithmic length仍满足

`log(dm)=logd+logm`,                               (25)

故 `H_h,U_a` 与定理 AAT不变；local phases只进入 `alpha_d,W_d`。Gamma与 pole
measure进入 balanced archimedean component。于是：

- interval-incidence Hilbert space无条件存在；
- positive triangular/Fejér Hodge norm无条件存在；
- local Euler convolution/tensor factorization在可用 identity下存在；
- 定理 AAU的 global Bessel budget仍是 GRH-strength输入。

对 family版本，degree、conductor及 ramified corrections必须在式 (22)中 uniform；
单个固定 L-function不需要 family uniformity。

## 7. 下一步

现在可以直接在式 (21)上工作：

1. 选一条保持 `d[psi-u]` 配平的 Vaughan identity；
2. 将 `d,m` 限制在 dyadic multiplicative rectangles；
3. 用 overlap条件 `|log(dm/d'm')|<h` 转成 near-product incidence；
4. 对 Type I 用短 interval divisor count，对 Type II 用 bilinear large sieve；
5. 把每个 rectangle的 Bessel budget除以 `beta_k asymp logT_k` 后求和。

若该预算成功，定理 AAU直接给 RH；若失败，finite triangular Gram的 dominant
rectangle会指出是 Type I main-term配平、Type II near-collisions还是 Abel tail造成。
