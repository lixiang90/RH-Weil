# Farey 边界谱、large-sieve 远尾与 mean-zero Hodge 修正

文档 084 把 linear Möbius Nyman residual 的未知部分压缩为

`R_N^bdry=int_N^infinity |F_N(y)|^2dy/y^2`,           (1)

其中在 `y>1`，

`F_N(y)=1+sum_(n<=N)b_n{y/n}`,

`b_n=mu(n)(1-log n/log N)`.                           (2)

本节把这个周期边界层完全 Fourier 化。新结论是：`y>=N^2` 的远尾可用
unconditional large sieve 与经典 Mertens bound 排除；真正未控制的部分只在
`N<=y<=N^2`，并进一步局限于一个 boundary zero mode 和分母
`r>sqrt(y)` 的 Farey 近碰撞扇区。

## 1. Reduced-denominator Fourier expansion

本节先允许任意 finite coefficients `b_1,...,b_N`。定义

`H_N(y)=1+sum_(n<=N)b_n{y/n}`,                         (3)

`mu_N=1+(1/2)sum_(n<=N)b_n`,                          (4)

`S_N(r)=sum_(n<=N,r|n)b_n/n  (1<=r<=N)`.              (5)

### 定理 QB（exact Farey expansion）

在任一共同周期上的 `L^2` 意义下，

`H_N(y)=mu_N-(1/(2pi i))sum_(r<=N) r S_N(r)`

`                 *sum_(h!=0,(h,r)=1)e^(2pi i h y/r)/h`.   (6)

也就是说，非零 Fourier frequencies 恰可按既约有理数 `h/r` 编号，且

`c_(r,h)=-r S_N(r)/(2pi i h)`.                        (7)

#### 证明

使用 sawtooth 的 `L^2(R/Z)` 展开

`{z}=1/2-(1/(2pi i))sum_(ell!=0)e^(2pi i ell z)/ell`.(8)

频率 `ell/n` 的既约写法为 `h/r` 当且仅当 `r|n` 且
`ell=h n/r`。把所有给出同一既约频率的项合并，其系数正是

`-sum_(r|n)b_n/(2pi i(hn/r))=-rS_N(r)/(2pi i h)`.     (9)

常数项给式 (4)。有限个 sawtooth 的 `L^2` 展开允许逐项合并。`□`

对 linear Möbius coefficients，若 `r` 非 squarefree，则 `S_N(r)=0`；若
`r` squarefree，则

`rS_N(r)=mu(r)sum_(m<=N/r,(m,r)=1) mu(m)/m`

`              *(1-(log r+log m)/log N)`.            (10)

因此实际 denominator strata 只由 squarefree divisibility directions 构成。

## 2. 单周期 Parseval Hodge 质量

写

`delta(r)=product_(p|r)(1-p^(-2))`.                   (11)

### 定理 QC（arithmetic Parseval diagonalization）

若 `Q_N=lcm(1,...,N)`，则

`E_N:=(1/Q_N)int_0^Q_N |H_N(y)|^2dy`

` =|mu_N|^2+(1/12)sum_(r<=N)r^2|S_N(r)|^2 delta(r)`.(12)

#### 证明

不同既约有理 frequencies 在一个共同周期上正交。对固定 `r`，式 (7) 的
平方和是

`r^2|S_N(r)|^2/(4pi^2)`

` *sum_(h!=0,(h,r)=1)1/h^2`.                         (13)

Euler product 给

`sum_(h!=0,(h,r)=1)1/h^2`

` =2zeta(2)product_(p|r)(1-p^(-2))`

` =(pi^2/3)delta(r)`.                                (14)

代入 Parseval 即得式 (12)。`□`

这是一个完全有限的 positive arithmetic Hodge norm。不过式 (1) 带有
`y^(-2)` 权；该权破坏不同 Farey frequencies 的正交性，所以只知道 `E_N`
仍不能直接控制边界能量。

## 3. Weighted collision Gram

令 frequency set

`F_N={0} union {h/r:1<=r<=N,h!=0,(h,r)=1}`.          (15)

把式 (6) 的 coefficients 记为 `c_alpha`，并吸收起点相位：

`d_alpha=c_alpha e^(2pi i alpha N)`.                  (16)

定义

`J_N(xi)=int_0^infinity e^(2pi i xi t)dt/(N+t)^2`.   (17)

### 定理 QD（exact boundary collision form）

`R_N^bdry=sum_(alpha,beta in F_N)`

`              d_alpha conjugate(d_beta)J_N(alpha-beta)`. (18)

这个 infinite matrix 是 PSD，并满足

`J_N(0)=1/N`,                                        (19)

`|J_N(xi)|<=min(1/N,1/(pi N^2|xi|))  (xi!=0)`.       (20)

任意不同 `alpha,beta in F_N` 还满足 sharp Farey spacing

`|alpha-beta|>=1/N^2`.                               (21)

#### 证明

把式 (6) 代入式 (1)，令 `y=N+t`，得到式 (18)。它是 functions
`e^(2pi i alpha t)` 在正 measure `dt/(N+t)^2` 下的 Gram form，故 PSD。
式 (19) 直接积分。式 (20) 的第一界来自绝对值；第二界对式 (17) 分部积分，
boundary term 与 derivative integral 各贡献 `1/(2pi N^2|xi|)`。两个不同
既约分数之差的分子是非零整数，分母至多 `N^2`，故式 (21)。`□`

式 (18) 明确说明困难在哪里：diagonal part 是 `E_N/N`，off-diagonal part
编码所有 Farey near collisions，且可以与 diagonal 大幅相消。逐项取绝对值
会恰好丢掉所需结构。

## 4. `N^2` 之后的 large-sieve 对角化

Montgomery--Vaughan Hilbert inequality 给以下连续 large-sieve 形式：若实
frequencies 的 separation 至少为 `Delta`，则对任意 interval `I`，

`int_I |sum c_alpha e^(2pi i alpha y)|^2dy`

` <=C(|I|+Delta^(-1))sum|c_alpha|^2`,                 (22)

其中 `C` 是 absolute constant。由有限部分逼近，该式也适用于本节的
square-summable countable frequency family。

### 定理 QE（unconditional far-tail reduction）

对任意 finite coefficients `b_n`，

`int_(N^2)^infinity |H_N(y)|^2dy/y^2`

` <=C E_N/N^2`.                                      (23)

#### 证明

式 (21) 允许在 dyadic interval `[Y,2Y]` 对式 (6) 使用式 (22)，得到

`int_Y^(2Y)|H_N(y)|^2dy<=C(Y+N^2)E_N`.               (24)

乘以 `Y^(-2)`，再对 `Y=2^jN^2` 求和：

`sum_(j>=0)(Y^(-1)+N^2Y^(-2))<=C'/N^2`.             (25)

即得式 (23)。`□`

所以 `N^2` 不是人为 cutoff，而是 denominator-`N` Farey spectrum 的自然
Heisenberg/large-sieve 分辨尺度。

## 5. Linear Möbius spectrum 的无条件远尾界

在线性情形，`|b_n|<=1`，故

`|S_N(r)|<=(1/r)(1+log(N/r))`.                        (26)

另一方面 Abel summation 给 boundary zero mode 的精确公式

`mu_N=1+(1/(2log N))int_1^N M(t)dt/t`,                (27)

其中 `M(t)=sum_(n<=t)mu(n)`。

### 定理 QF（far boundary is not the RH obstruction）

有无条件估计

`E_N<<N+(1+(1/log N)int_1^N |M(t)|dt/t)^2`.          (28)

使用经典 Korobov--Vinogradov/Walfisz 型 Mertens bound

`M(t)<<t exp(-c(log t)^(3/5)(loglog t)^(-1/5))`,      (29)

得到

`E_N/N^2=o(1/log N)`.                                (30)

因此

`int_(N^2)^infinity |F_N(y)|^2dy/y^2=o(1/log N)`     (31)

无条件成立。

#### 证明

式 (26) 代入定理 QC；dyadic summation 给

`sum_(r<=N)(1+log(N/r))^2<<N`.                       (32)

式 (27) 控制 constant mode，得到式 (28)。在式 (27) 的积分中把
`[1,N]` 分成 `[1,sqrt N]` 与 `[sqrt N,N]`，再用式 (29)，可把式 (28) 的
第二项除以 `N^2` 后界成一个负 stretched exponential。于是式 (30) 成立，
再用定理 QE 得式 (31)。`□`

注意式 (31) 并不控制 constant mode 在 `[N,N^2]` 上的贡献；在那里它约为
`|mu_N|^2/N`，经典 zero-free bound 远不足以达到 sharp scale。

## 6. Parabolic Farey sector

对 `R<=N`，令 `H_(>R)` 是式 (6) 中仅保留 denominators `r>R` 的
oscillatory part，不含 `mu_N`。取 dyadic scales

`Y_j=2^jN<N^2`,  `R_j=floor(sqrt(Y_j))`,              (33)

并定义

`P_N=sum_j int_(Y_j)^min(2Y_j,N^2)`

`                 |H_(>R_j)(y)|^2dy/y^2`.            (34)

### 定理 QG（parabolic localization certificate）

低分母部分无条件满足

`sum_j int_(Y_j)^min(2Y_j,N^2)`

`       |H_(<=R_j)(y)|^2dy/y^2`

` <<(log N)^3/sqrt(N)=o(1/log N)`.                   (35)

因而

`R_N^bdry<=3|mu_N|^2/N+3P_N+o(1/log N)`.             (36)

特别地，若

`|mu_N|^2/N=O(1/log N)`,  `P_N=O(1/log N)`,           (37)

则文档 084 的 boundary condition 成立。

#### 证明

denominators `r<=R_j` 的 spacing 至少为 `R_j^(-2)>=Y_j^(-1)`，故式
(22) 已在长度 `Y_j` 的 shell 上有效。其 Fourier mass 由式 (26) 粗界为
`O(R_j(log N)^2)`；除以 `Y_j` 后是
`O((log N)^2/sqrt(Y_j))`，对至多 `O(log N)` 个 shells 求和给式 (35)。
在每个 shell 用 `|a+b+c|^2<=3(|a|^2+|b|^2+|c|^2)`，再加入定理 QF 的
far tail，得到式 (36)。`□`

这把开放部分缩成两块：

1. boundary zero mode `mu_N`，即一个 log-smoothed Mertens scalar；
2. `r>sqrt(Y)` 的高分母 Farey sector，其中频率间距小于观测尺度
   `1/Y`，普通 large sieve 尚不能对角化。

## 7. Exact mean-zero quadratic gauge

zero mode 可以在 finite trial-vector level 被精确投影掉。令

`u_n=log n/log N`,

`P_alpha(u)=1-u+alpha u(1-u)`                         (38)

并定义

`B_N=sum_(n<=N)mu(n)(1-u_n)`,

`D_N=sum_(n<=N)mu(n)u_n(1-u_n)`.                     (39)

### 定理 QH（boundary mean-zero Hodge correction）

若 `D_N!=0`，取

`alpha_N=-(B_N+2)/D_N`.                              (40)

则 coefficients `b_n^(2)=mu(n)P_(alpha_N)(u_n)` 同时满足

`P_(alpha_N)(0)=1`,  `P_(alpha_N)(1)=0`,              (41)

以及

`1+(1/2)sum_(n<=N)b_n^(2)=0`.                        (42)

其完整低 convolution 为

`c_N^(2)(m)=delta_(m,1)+(1-alpha_N)Lambda(m)/log N`

`             -alpha_N M_2(m)/(log N)^2  (m<=N)`.    (43)

#### 证明

式 (41) 直接来自式 (38)，式 (40) 代入 periodic mean 给式 (42)。把

`P_alpha(u)=1+(alpha-1)u-alpha u^2`                  (44)

代入文档 083 的定理 PO，并用 `M_1=-Lambda`，即得式 (43)。`□`

这是一项真正的 Hodge projection：它消除了 boundary Tate/constant mode，
但把 linear prime-power current 改成 prime-power 与 two-almost-prime current
的组合。当前不能假定 `D_N` 一致远离零或 `alpha_N` 有界；这些是该修正能否
优于 linear mollifier 的新有限算术问题。

## 8. 结构存在性审计

### 结论 QI（what remains after Farey diagonalization）

现在无条件存在并已求出的结构包括：

- complete-low Chebyshev potential；
- periodic boundary carrier 的完整 Farey spectral resolution；
- 单周期 positive Parseval Hodge norm；
- weighted boundary 的 exact PSD collision Gram；
- `y>=N^2` 的 unconditional negligible tail；
- 可精确消去 boundary zero mode 的 quadratic finite correction。

因此 linear mollifier 路线的未证输入不再是整个 `m>N` tail，而是有限尺度窗
`N<=y<=N^2` 内的 parabolic high-denominator Gram `P_N`，外加选择 linear
filter 时的 smoothed-Mertens zero mode。mean-zero quadratic filter 把后者转移
成显式 semiprime current，但尚未控制前者。

这给下一步一个明确目标：研究 squarefree denominator amplitudes `S_N(r)` 在
`r>sqrt(Y)` 上的 bilinear Farey large sieve，或对 quadratic gauge 的
`alpha_N,D_N` 建立稳定性估计。任何只估计单周期 Parseval mass、或把 collision
Gram 逐项绝对值化的方法，都不会保持证明 RH 所需的相消。

## 9. 计算实现

`scripts/qw_matrix.py` 新增：

- `reduced_denominator_density`；
- `beurling_periodic_fourier_energy`；
- `beurling_periodic_piecewise_energy`；
- `linear_mollifier_periodic_mean_via_mertens`；
- `mean_zero_quadratic_mobius_mollifier`。

测试在 `N=6` 上把定理 QC 的 Fourier divisor formula 与一个共同周期上的逐段
精确积分比较；在 `N=30` 上核对定理 QH 的 zero mean、两个 endpoint 条件和
式 (43) 的全部低 coefficients。
