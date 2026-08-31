# Local--parabolic--far Hodge 分块与唯一 leakage 证书

文档 087 给出了真实 Nyman Gram 上的 constrained optimizer，但 total Gram
仍混合所有空间尺度。本节把 reciprocal coordinate `y=1/x` 分成

`(0,N)`,  `[N,N^2]`,  `(N^2,infinity)`.                (1)

每段产生一个 PSD Hodge block。local block 对任意 finite mollifier 都能由
低卷积 jumps 精确求出；far block 被单周期 Farey Parseval form 以 `N^(-2)`
控制；因此只剩中间 parabolic block 需要新的 Möbius--Farey 相消。

## 1. 任意 finite mollifier 的 exact local energy

给定 coefficients `b_1,...,b_N`，令

`A=sum_(n<=N)b_n/n`,                                  (2)

`c(m)=sum_(d|m)b_d`,                                  (3)

`C(k)=sum_(m<=k)c(m)`.                                (4)

在 `m<=N` 时式 (3) 已包含全部 divisors，不涉及 truncated tail。定义

`F_b(y)=1_(y>=1)+sum_(n<=N)b_n{y/n}`.                 (5)

### 定理 QW（complete finite local-potential energy）

对 `0<y<1`，

`F_b(y)=Ay`.                                          (6)

对 `k<=y<k+1`、`1<=k<N`，

`F_b(y)=Ay+1-C(k)`.                                   (7)

因此

`R_b^loc:=int_0^N |F_b(y)|^2dy/y^2`

` =|A|^2+sum_(k=1)^(N-1){|A|^2`

`   +2Re[A conjugate(1-C(k))]log((k+1)/k)`

`   +|1-C(k)|^2(1/k-1/(k+1))}`.                      (8)

#### 证明

每个 sawtooth 的连续斜率为 `1/n`，在 integer `m` 的总 downward jump 是
`c(m)`。从 `F_b(0+)=0` 积分到第 `k` 个 interval，得到式 (6)--(7)。对
`|A+(1-C(k))/y|^2` 在 `[k,k+1]` 积分即得式 (8)。`□`

文档 084 的 linear Chebyshev decomposition 是式 (8) 在
`c(m)=Lambda(m)/log N` 下的进一步正交化。式 (8) 则适用于文档 086/087 的
任意 polynomial jet correction；由定理 QM，其 `C(k)` 仍由有限
almost-prime currents 完全确定。

## 2. 三个 spatial Hodge blocks

在原变量 `x` 中定义 disjoint regions

`Omega_loc=[1/N,infinity)`,

`Omega_par=[1/N^2,1/N]`,

`Omega_far=(0,1/N^2]`.                                (9)

端点是零测集。对 Nyman features `rho_n` 及 target `chi`，定义 restricted
data

`G^a_(mn)=int_(Omega_a)rho_m conjugate(rho_n)dx`,

`z^a_n=int_(Omega_a)rho_n chi dx`,

`e^a=int_(Omega_a)|chi|^2dx`,                         (10)

其中 `a in {loc,par,far}`。

### 定理 QX（PSD spatial Hodge resolution）

每个 augmented block

`H^a=[[e^a,(z^a)^*],[z^a,G^a]]`                      (11)

均为 PSD，且

`H=H^loc+H^par+H^far`.                                (12)

对任意 coefficient vector `b`，

`||chi+sum b_nrho_n||^2=R_b^loc+R_b^par+R_b^far`,    (13)

三个 summands 均非负。`R_b^loc` 就是定理 QW 的式 (8)。

#### 证明

式 (11) 是 restricted functions `(chi,rho_1,...,rho_N)` 的 Gram matrix，
故 PSD。Lebesgue measure 在三个 disjoint regions 上可加，给式 (12)--(13)。
变量替换 `y=1/x` 把第一块变成 `y<=N`，故定理 QW 适用。`□`

这是真正的 Hodge direct-sum decomposition：困难不能在不同 blocks 间相消，
因为每一块本身都是一个正范数。

## 3. Easy optimizer plus hard leakage

在任意 finite correction basis 中，把 constrained quadratic data 分成

`(W,h,E_0)=(W_e,h_e,E_e)+(W_p,h_p,E_p)`,              (14)

其中两个 triples 都来自 restricted Hilbert norms，故其 affine quadratic
forms 非负。令 `alpha_e` 是 easy form 在同一 boundary constraint
`D^*alpha=t` 下的 minimizer。

### 定理 QY（positive leakage upper certificate）

令 `E_full^*` 是 full constrained minimum，`E_e^*` 是 easy minimum，并令

`L_p(alpha_e)=E_p+2Re(h_p^*alpha_e)`

`                 +alpha_e^*W_palpha_e>=0`.           (15)

则

`E_full^*<=E_e^*+L_p(alpha_e)`.                       (16)

更精确地，若 `alpha_*` 是 full minimizer，则

`E_e^*+L_p(alpha_e)-E_full^*`

` =||T_full(alpha_e-alpha_*)||^2>=0`.                 (17)

#### 证明

`alpha_e` 满足 full problem 的同一 affine constraint，所以把它作为 trial
vector 立即得到式 (16)。两个 vectors 的差位于 homogeneous constraint
kernel；full Euler--Lagrange equation 使 linear cross term 消失，展开 full
quadratic form 得式 (17)。`□`

因此不必先控制 full inverse。可以先在 local+far 的可控 metric 中求 canonical
candidate，再只估计它进入 parabolic block 的 leakage。

## 4. Far block 的 periodic Loewner majorant

对任意 constant `a_0` 与 coefficients `b_n`，令

`H_(a_0,b)(y)=a_0+sum_(n<=N)b_n{y/n}`.                (18)

其一个共同周期为 `Q_N=lcm(1,...,N)`。令

`P_N(a_0,b)=(1/Q_N)int_0^Q_N|H_(a_0,b)(y)|^2dy`      (19)

为文档 085 定理 QC 的 augmented Farey Parseval form；显式地只需把其中
constant mode 换成 `a_0+(1/2)sum b_n`。

### 定理 QZ（far Gram domination）

存在 absolute constant `C`，使对所有 `(a_0,b)`，

`int_(N^2)^infinity |H_(a_0,b)(y)|^2dy/y^2`

` <=(C/N^2)P_N(a_0,b)`.                              (20)

等价地，在 augmented coefficient space 上有 Loewner inequality

`H^far<=(C/N^2)H^per`.                               (21)

#### 证明

定理 QB 的 frequencies 仍是 denominator 至多 `N` 的既约 fractions，最小
spacing 至少 `N^(-2)`；constant `a_0` 只是 zero frequency。文档 085 定理
QE 的 dyadic continuous-large-sieve 证明逐字适用，给式 (20)。quadratic
form inequality 对所有 augmented vectors 成立，正是式 (21)。`□`

这比只对 linear Möbius candidate 的渐近估计更强：任何 jet-corrected vector
都可用其完全有限的 periodic Parseval mass 控制 far leakage。

## 5. Localized RH upper certificate

对一列合法 coefficients `b^(N)`，记

`P_N=P_N(1,b^(N))`,                                   (22)

`R_N^par=int_N^(N^2)|F_(b^(N))(y)|^2dy/y^2`.          (23)

### 定理 RA（three-block sufficient criterion）

若沿某个 cofinal sequence，

`R_N^loc ->0`,  `R_N^par->0`,  `P_N/N^2->0`,          (24)

则 RH 成立。若三个量分别满足

`R_N^loc=O(1/log N)`,

`R_N^par=O(1/log N)`,

`P_N/N^2=O(1/log N)`,                                (25)

则达到 sharp `R_N=O(1/log N)` scale。

#### 证明

定理 QX 与 QZ 给

`R_N<=R_N^loc+R_N^par+(C/N^2)P_N`.                   (26)

式 (24) 使右侧趋零。文档 083 的 `d_N^2<=R_N` 与 Nyman--Beurling--
Báez-Duarte criterion 给 RH。式 (25) 同理。`□`

定理 RA 没有把 RH 隐藏进一个 global norm：local 是有限 jump arithmetic，
periodic mass 是有限 divisor sum，唯一仍需 analytic cancellation 的 quantity
明确是 bounded scale window `[N,N^2]` 上的 `R_N^par`。

## 6. Parabolic Farey collision form

沿用文档 085 的 reduced frequencies `alpha,beta` 与相位 coefficients
`d_alpha`。定义 truncated kernel

`J_N^par(xi)=int_0^(N^2-N)`

`                 e^(2pi i xi t)dt/(N+t)^2`.          (27)

则

`R_N^par=sum_(alpha,beta)d_alpha conjugate(d_beta)`

`                              J_N^par(alpha-beta)`.  (28)

式 (28) 是 PSD Gram。对 shell `y~Y`，denominators `r<=sqrt(Y)` 已由普通
large sieve 对角化；所以其真正 dense sector 是

`r>sqrt(Y)`.                                         (29)

这说明 parabolic leakage 同时具有两种等价坐标：空间上是唯一中间 Hodge
block，频率上是高分母 Farey collision block。下一步需要的是针对 amplitudes
`S_N(r)` 的 bilinear arithmetic estimate，而不是再估计 local jumps 或 far
periodic mass。

## 7. Abstract localized Hodge theorem

### 定理 RB（positive localization principle）

设一个 generalized Weil/Hodge synthesis package 的 Hilbert measure 可分成
有限或可数个 disjoint regions，因而 polarization

`W=sum_a W_a`,  `W_a>=0`.                             (30)

则：

1. 每个 `W_a` 是独立 positive Hodge block；
2. 任意 easy-region constrained optimizer 加上其 hard-region leakage 给 full
   energy 的上证书；
3. 任意已知 operator majorant `W_hard<=B` 可直接替换 hard leakage；
4. 若所有 block energies 沿一列 algebraic trial objects 同时趋零，则对应
   Hodge distance radical 化；结合文档 001 的 polarized Weil structure，
   相应 zeta zeros 位于中心线。

#### 证明

第一项来自 restricted Gram positivity；第二项是定理 QY；第三项由 Loewner
order；第四项由正项求和及 generalized structure theorem。`□`

定理 RB 把 Weil 证明机制中的“全局正性”细化成可拼接的局部 polarizations：
结构存在性可以逐块证明，但所有 blocks 必须由同一个 algebraic trial object
同时控制。

## 8. 存在性审计

### 结论 RC（single remaining positive block）

对 zeta 的 polynomial Möbius jet candidates：

- local block 无条件由定理 QW 与 almost-prime moments 精确计算；
- far block 无条件由定理 QZ 控制；
- full finite constrained optimizer 与 jet gains 由文档 087 精确计算；
- 唯一没有 uniform upper estimate 的是 parabolic block (28)。

所以当前路线的存在性问题已压成一个具体的 positive bilinear theorem：构造
同一列 coefficients，使 local jump energy、periodic Farey mass 和
high-denominator parabolic collision energy 同时达到式 (24) 或 (25)。

这仍未证明 RH；但它排除了三个常见伪路线：只控制低 Dirichlet coefficients、
只控制一个周期平均、或只控制全 Gram 的最小特征值，都不足以估计式 (28)。

## 9. 计算实现

`scripts/qw_matrix.py` 新增：

- `beurling_mollifier_local_energy`；
- `quadratic_hodge_energy`；
- `easy_hard_constrained_hodge_certificate`。

测试把一般 local jump formula 专门化回文档 084 的 Chebyshev 三项分解；另用
两个独立 PSD blocks 检查 easy optimizer 的 candidate energy、hard leakage
和 full constrained optimum 之间的严格上证书。
