# Parabolic Farey determinant form 与跨 conductor 唯一障碍

文档 088 把 RH upper certificate 的唯一未知正块定位为

`R_N^par=int_N^(N^2)|F_N(y)|^2dy/y^2`.                (1)

本节进一步证明：对 boundary mean-zero 且 endpoint-Lipschitz 的 polynomial
Möbius filters，low denominators、Fourier diagonal 以及同一 denominator 内的
全部 harmonic interactions 都无条件是 `O((log N)^(-2))`。唯一可能处在
`1/log N` sharp scale 的项，是不同 denominators 间满足小 Farey determinant
条件的 bilinear collision form。

## 1. Endpoint smoothing controls conductor amplitudes

令

`b_n=mu(n)P(log n/log N)`,  `P(1)=0`,                 (2)

并定义 endpoint Lipschitz seminorm

`K(P)=sup_(0<=u<1)|P(u)|/(1-u)`.                      (3)

仍记

`S_N(r)=sum_(n<=N,r|n)b_n/n`,  `X=N/r`.               (4)

### 定理 RD（endpoint-to-conductor bound）

对每个 `1<=r<=N`，

`|rS_N(r)|`

` <=K(P)/log N *[log X+(1/2)(log X)^2]`.              (5)

因此 Farey oscillatory Parseval mass

`E_N^osc=(1/12)sum_(r<=N)r^2|S_N(r)|^2`

`                         *product_(p|r)(1-p^(-2))`  (6)

满足

`E_N^osc<<K(P)^2 N/(log N)^2`.                       (7)

#### 证明

写 `n=rm`。由式 (3)，

`|P(log(rm)/log N)|`

` <=K(P)log(N/(rm))/log N`.                          (8)

所以

`|rS_N(r)|<=K(P)/log N`

`              *sum_(m<=X)log(X/m)/m`.               (9)

函数 `log(X/t)/t` 递减，首项加积分给

`sum_(m<=X)log(X/m)/m`

` <=log X+int_1^X log(X/t)dt/t`

` =log X+(1/2)(log X)^2`,                             (10)

得到式 (5)。最后

`sum_(r<=N)(1+log(N/r))^4<<N`                        (11)

由积分比较成立；代入式 (6) 得式 (7)。`□`

linear filter `P(u)=1-u` 有 `K(P)=1`。固定 degree 且 coefficients bounded
的 endpoint-vanishing filters 也有 bounded `K(P)`；对随 `N` 增长的 jet
projection，`K(P_N)` 则成为必须显式追踪的 stability quantity。

## 2. Diagonal 与 same-conductor blocks 已经可忽略

对 dyadic shell `[Y,2Y] subset [N,N^2]`，令 `R=sqrt(Y)`。式 (6) 中
`r>R` 的部分记为 `E_(>R)`。

### 定理 RE（resolved-sector bound）

1. high-denominator Fourier diagonal 在该 shell 的精确贡献是

   `E_(>R)/(2Y)`；                                    (12)

2. 把固定 denominator `r` 的全部 harmonics 合在一起，其 shell energy
   至多为 `C E_r/Y`；
3. 对所有 dyadic parabolic shells 求和，diagonal 与所有 same-conductor
   energies 总和均为

   `O(K(P)^2/(log N)^2)`；                            (13)

4. denominators `r<=sqrt(Y)` 的完整联合 block 也满足同一总界。

#### 证明

diagonal kernel 是

`int_Y^(2Y)dy/y^2=1/(2Y)`,                            (14)

故第一项来自 Parseval coefficient square sum。固定 `r` 的 harmonics 间距
是 `1/r>=1/Y`；continuous large sieve 给 unweighted interval norm
`O(Y E_r)`，再乘 `Y^(-2)` 得第二项。式 (7) 及

`sum_(Y=N,2N,...)1/Y<<1/N`                            (15)

给第三项。对 `r<=sqrt(Y)`，所有既约 frequencies 的 spacing 至少
`1/Y`，同一个 large-sieve argument 直接作用于其联合 family，给第四项。
`□`

所以 ordinary large sieve 的 `N^2` loss 只来自跨越不同 high denominators
的 dense collisions；它不来自 harmonic tail、diagonal mass 或任何单个
conductor。

## 3. Smooth shell 与 Farey determinant kernel

取 nonnegative `w in C_c^infinity((1,2))`，令

`omega(t)=w(t)/t^2`,

`hat omega(xi)=int_R omega(t)e^(2pi i xi t)dt`.        (16)

定义 smooth shell energy

`R_(Y,w)=(1/Y)int_1^2 omega(t)|F_N(Yt)|^2dt`.         (17)

使用文档 085 的 Fourier coefficients

`c_(r,h)=-rS_N(r)/(2pi i h)`,  `(h,r)=1`.             (18)

### 定理 RF（exact determinant collision formula）

不同 high conductors `r!=r'` 的 cross contribution 精确为

`C_(Y,w)=1/(4pi^2Y) sum_(r,r'>sqrt(Y),r!=r')`

` r r' S_N(r)conjugate(S_N(r'))`

` *sum_((h,r)=1,(h',r')=1,h h'!=0)`

` hat omega(Y(hr'-h'r)/(rr'))/(h h')`.               (19)

对每个 `A>=0`，

`|hat omega(xi)|<=C_(A,w)(1+|xi|)^(-A)`.             (20)

#### 证明

把式 (18) 代入式 (17)，交换 `L^2`-convergent Fourier sums 与 smooth
integral。频率差

`h/r-h'/r'=(hr'-h'r)/(rr')`                          (21)

给式 (19)。对 compactly supported smooth `omega` 反复分部积分，得到式
(20)。`□`

因此 cross-conductor interaction 被 microlocally 集中到整数 determinant

`Delta=hr'-h'r`                                      (22)

满足

`|Delta| roughly <= rr'/Y`.                          (23)

这不是启发式“频率接近”，而是 smooth Hodge kernel 中出现的精确整数窗口。

## 4. Parabolic block 的最终归约

取一组 nonnegative smooth dyadic partition，使其在 `[N,N^2]` 上和为一。
令 `C_N^cross` 是对应式 (19) 的 cross-conductor forms 之和。

### 定理 RG（cross-conductor reduction）

若 periodic boundary mean 为零，则

`R_N^par<=C|C_N^cross|_sum`

`          +O(K(P)^2/(log N)^2)`,                    (24)

其中 `|.|_sum` 表示逐 shell cross form 的 absolute values 之和。更准确地，
不取绝对值时，各 shell energy 等于 low-denominator block、high
same-conductor block 与式 (19) 的和。

#### 证明

mean-zero 消去 zero frequency。对每个 shell，把 field 分成
`r<=sqrt(Y)` 与 `r>sqrt(Y)`；用 `|a+b|^2<=2|a|^2+2|b|^2`。定理 RE 控制
low block。展开 high block，所有 `r=r'` 项之和由定理 RE 控制，剩余恰是
式 (19)。对 partition 求和即得。`□`

式 (24) 保留了 `S_N(r)conjugate(S_N(r'))` 的 Möbius signs 与 harmonic
kernel 的 signs；若在式 (19) 内逐项绝对值化，仍会退回 large-sieve
`N^2/Y` loss。

## 5. Sharp collision criterion

### 定理 RH（编号 RH：parabolic determinant certificate）

设 `P_N(0)=1`、`P_N(1)=0`，相应 periodic boundary means 为零，并且

`K(P_N)=O(1)`.                                       (25)

若

`sum_(dyadic Y) |C_(Y,w)|=O(1/log N)`,                (26)

则

`R_N^par=O(1/log N)`.                                (27)

若同时文档 088 定理 RA 的 local 与 periodic conditions 成立，则 RH 成立，
并达到 sharp Nyman upper scale。

#### 证明

式 (25) 使定理 RG 的 error 成为 `O((log N)^(-2))`；式 (26) 给主项。
再调用定理 RA。`□`

这里编号“RH”只是本仓库连续定理编号；式 (26) 仍是尚未证明的 bilinear
arithmetic estimate，不是黎曼猜想的重命名。

## 6. Reciprocal Euler systems 的 determinant template

对一般 reciprocal coefficients `beta(n)` 与 endpoint filter `P`，定义

`S_(L,N)(r)=sum_(r|n,n<=N)beta(n)P(log n/log N)/n`.   (28)

### 定理 RI（universal parabolic collision structure）

只要相应 real/adelic synthesis features 的 periodic frequencies 仍按 rational
denominators `h/r` 分层，则：

1. conductor amplitudes 是 `rS_(L,N)(r)`；
2. smooth parabolic Gram 的 cross terms 都具有式 (19) 的 determinant kernel；
3. endpoint bounds 控制 diagonal/self-conductor sectors；
4. generalized RH existence problem 被归约为带 `beta` amplitudes 的
   cross-conductor determinant inequality。

#### 证明

前三项只使用 sawtooth Fourier expansion、endpoint vanishing 与 smooth
Fourier decay；与 `mu` 的特殊乘法性无关。第四项结合文档 088 的 localized
Hodge theorem。`□`

一般 `L` 是否具有这种 rational-periodic synthesis 是额外结构假设；文档 084
只无条件给了 coefficient-side reciprocal current，不能自动推出这一假设。

## 7. 存在性审计

### 结论 RJ（the remaining theorem is genuinely bilinear）

现在对 bounded endpoint norm、mean-zero polynomial Möbius candidates：

- local almost-prime potential 已完全显式；
- far block 已由 periodic Loewner majorant 控制；
- parabolic low denominators、diagonal、harmonic tail 与 same-conductor blocks
  均为 `O((log N)^(-2))`；
- 唯一开放项是式 (19) 中 `r!=r'`、小 determinant 的 signed bilinear sum。

所以接下来的有效工具应针对

`hr'-h'r=Delta`,  `|Delta|<=rr'/Y`,                  (29)

并同时保留 Möbius hyperbola amplitudes

`rS_N(r)=mu(r)sum_(m<=N/r,(m,r)=1)`

` mu(m)P(log(rm)/log N)/m`.                          (30)

这已经是一个具体的 Type-I/II--Farey determinant 问题。普通 large sieve、
单周期 Parseval 或对 `S_N(r)` 的逐项上界都无法证明所需 signed estimate。

## 8. 计算实现

`scripts/qw_matrix.py` 新增：

- `mollifier_conductor_amplitude`；
- `linear_mollifier_conductor_amplitude_majorant`；
- `parabolic_shell_diagonal_energy`。

回归测试逐 denominator 核对 `rS_N(r)` 与 divisor-sum Fourier data，验证
定理 RD 的 endpoint majorant，并从 conductor masses 独立重建式 (12) 的
shell diagonal energy。
