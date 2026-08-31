# Farey determinant 的 cotangent 参数化与 Type-I/II 缩窗

文档 089 把唯一开放的 parabolic block 写成跨 conductor determinant form。
本节把 harmonic variables `h,h'` 沿 determinant equation 求和，得到 finite
Möbius sieve of cotangent kernels；同时利用 endpoint-improved Fourier mass，
把尚需研究的 scales 从 `[N,N^2]` 缩到 `[N,N^(3/2)]`。

## 1. GCD--LCM reduction of the determinant equation

固定不同 denominators `r,r'`，考虑

`h r'-h' r=Delta`.                                   (1)

写

`g=(r,r')`,  `r=ga`,  `r'=gb`,  `(a,b)=1`.           (2)

### 定理 RK（determinant divisibility and primitive condition）

若式 (1) 有整数解，则 `g|Delta`。写 `Delta=g delta` 后，方程化为

`b h-a h'=delta`.                                    (3)

若还要求 `(h,r)=(h',r')=1`，则必要地

`(delta,ab)=1`.                                      (4)

此外 smooth shell 的 core collision condition

`|Delta|<=rr'/Y`                                     (5)

等价于

`|delta|<=lcm(r,r')/Y=gab/Y`.                        (6)

因此 `lcm(r,r')<Y` 时没有非零 core determinant；允许的 reduced
determinants 数量至多为 `O(lcm(r,r')/Y)`。

#### 证明

式 (1) 左侧被 `g` 整除。除以 `g` 给式 (3)。模 `a` 看式 (3)，因 `b`
可逆，`(h,a)=(delta,a)`；primitive condition 迫使 `(delta,a)=1`。模
`b` 同理。最后 `rr'/g=gab=lcm(r,r')`，故式 (5) 除以 `g` 即为式 (6)。`□`

式 (4) 还不是 shared factor `g` 上 primitive congruences 的充分条件；那些
条件将在 finite Möbius sieve 中自动编码。

## 2. Solution line 的 cotangent 求和

先考虑一般 equation

`A u-B v=Delta`,                                     (7)

令 `q=(A,B)`，并假设 `q|Delta`。写

`A=qa`,  `B=qb`,  `Delta=qdelta`,  `(a,b)=1`.         (8)

取一个 particular solution `(u_0,v_0)`；全部解为

`u=u_0+bt`,  `v=v_0+at`,  `t in Z`.                  (9)

### 定理 RL（generic cotangent harmonic kernel）

若 `a,b>1` 且 `(delta,ab)=1`，则没有 solution 经过 `u=0` 或 `v=0`，并有

`U(A,B;Delta):=sum_(Au-Bv=Delta)1/(uv)`

` =pi/delta[cot(pi v_0/a)-cot(pi u_0/b)]`.           (10)

该 series 按 symmetric principal value 收敛；事实上两项合并后为
`O(t^(-2))`。

#### 证明

由式 (7)--(8)，

`1/(uv)=(a/v-b/u)/delta`.                             (11)

代入式 (9) 后，

`a/v=1/(t+v_0/a)`,  `b/u=1/(t+u_0/b)`.               (12)

使用

`PV sum_(t in Z)1/(t+x)=pi cot(pi x)`                (13)

即得式 (10)。coprimality assumption 排除 zero denominators。`□`

非 generic cases（`a=1`、`b=1` 或 solution line 穿过坐标轴）可直接删去
`u=0`/`v=0` 项后取极限；它们是有限的 boundary corrections，不改变后续
determinant structure。

## 3. Primitive harmonics 是 finite Möbius sieve

定义真正出现在文档 089 中的 primitive correlation

`H_(r,r')(Delta)=sum_((h,r)=1,(h',r')=1,`

`                         hr'-h'r=Delta)1/(hh')`.    (14)

### 定理 RM（primitive cotangent sieve）

有 exact finite formula

`H_(r,r')(Delta)`

` =sum_(d|r)sum_(e|r')mu(d)mu(e)/(de)`

`                     *U(d r',e r;Delta)`,            (15)

其中 incompatible divisibility terms 取零，degenerate `U` 按定理 RL 后的
删项极限解释。特别地，对 `r!=r'`，

`H_(r,r')(0)=0`.                                     (16)

#### 证明

在式 (14) 插入

`1_((h,r)=1)=sum_(d|r,d|h)mu(d)`                     (17)

及 `r'` 的同型公式。写 `h=du,h'=ev` 后，equation 变成

`d r'u-e rv=Delta`，weight 变成 `1/(deuv)`，得到式 (15)。若
`Delta=0`，两个 primitive fractions `h/r=h'/r'` 相等；既约表示唯一性迫使
`r=r'`，故式 (16)。`□`

因此 harmonic double sum 不再是一个无限黑箱：它是有限 divisor sieve of
explicit modular-inverse cotangents。对 denominators 求和时出现的正是
Estermann/Dedekind-cotangent 型 arithmetic，而非任意 dense frequency matrix。

## 4. Four variables collapse to a determinant sum

文档 089 式 (19) 可重写为

### 定理 RN（determinant-cotangent collapse）

`C_(Y,w)=1/(4pi^2Y)sum_(r!=r'>sqrt(Y))`

` r r'S_N(r)conjugate(S_N(r'))`

` *sum_(Delta!=0)hat omega(YDelta/(rr'))`

`                         H_(r,r')(Delta)`.           (18)

在 core range 中，只有

`Delta=gdelta`,  `(delta,ab)=1`,

`|delta|<=gab/Y`                                     (19)

需要保留；smooth tails 按 `Y|Delta|/(rr')` 任意幂衰减。

#### 证明

在 harmonic pairs 上按 `Delta=hr'-h'r` 分组，再使用定理 RM。定理 RK 给
式 (19)，文档 089 定理 RF 给 smooth decay。`□`

式 (18) 把 `(h,h')` 两个无限 variables 压成一个短 determinant variable
`delta` 与 finite cotangent sieve，为 bilinear estimates 提供了标准算术坐标。

## 5. Upper half of the parabolic window is already harmless

设 boundary mean 为零，并保持文档 089 的 endpoint norm `K(P)`。由定理 RD，

`E_N^osc<<K(P)^2N/(log N)^2`.                         (20)

对任意 shell `[Y,2Y]`，global Farey spacing `N^(-2)` 与 continuous large
sieve 给

`R_(Y)<=C(Y+N^2)E_N^osc/Y^2`.                        (21)

### 定理 RO（`N^(3/2)` large-sieve cutoff）

`sum_(dyadic Y>=N^(3/2)) R_(Y)`

` <<K(P)^2/(log N)^2`.                               (22)

因此 sharp parabolic problem 只需处理

`N<=Y<=N^(3/2)`.                                     (23)

#### 证明

把式 (20) 代入式 (21)。对 dyadic `Y>=Y_0=N^(3/2)`，

`sum 1/Y<<1/Y_0`,  `sum 1/Y^2<<1/Y_0^2`.             (24)

于是两项分别为

`O(K(P)^2/(sqrt(N)(log N)^2))`

和 `O(K(P)^2/(log N)^2)`，给式 (22)。`□`

这比文档 085 的 universal `N^2` 分辨尺度更强；改进来自 Möbius filter 的
endpoint smoothing 把总 coefficient mass 降低了一个 `(log N)^2` 并集中到
可接受的 sharp budget。

## 6. Möbius hyperbola Type-I/II factorization

在线性或一般 polynomial Möbius filter 下，若 `r` squarefree，则

`rS_N(r)=mu(r)sum_(m<=N/r,(m,r)=1)mu(m)/m`

`                  *P((log r+log m)/log N)`.          (25)

非 squarefree `r` 的 amplitude 为零。

在剩余窗口式 (23) 及 hard sector `r>sqrt(Y)` 中，

`m<=N/r<N/sqrt(Y)<=sqrt(N)`.                         (26)

### 定理 RP（squarefree gcd factorization）

若 `r=ga,r'=gb` 且两个 amplitudes 非零，则 `g,a,b` pairwise coprime 且
squarefree，并且

`mu(r)mu(r')=mu(a)mu(b)`.                            (27)

将式 (25) 代入式 (18) 后，剩余 collision form 是 variables

`g,a,b,delta,m,m'`                                   (28)

上的 Type-I/II sum，其中

`gab>=Y`,  `(delta,ab)=1`,  |delta|<=gab/Y,           (29)

`m<=N/(ga)`,  `m'<=N/(gb)`,                           (30)

并带 signs `mu(a)mu(b)mu(m)mu(m')`。shared gcd
direction `g` 的 Möbius sign 精确平方消失。

#### 证明

squarefree `ga` 迫使 `(g,a)=1` 且两者 squarefree；`gb` 同理，而
`(a,b)=1` 来自定义。因此三者 pairwise coprime。乘法性给式 (27)。其余条件
来自定理 RK、RO 与式 (25)--(26)。`□`

这识别了 cancellation 的真正来源：不是 shared gcd `g`，而是 coprime
quotients `a,b` 与短 hyperbola variables `m,m'`。

## 7. Narrowed sufficient theorem

### 定理 RQ（Type-I/II cotangent certificate）

若存在 mean-zero endpoint-bounded filters，使文档 088 的 local/periodic
conditions 成立，并且式 (18) 在

`N<=Y<=N^(3/2)`                                      (31)

内的 Type-I/II expansion (28)--(30) 满足 dyadic total

`O(1/log N)`,                                        (32)

则 RH 成立。

#### 证明

定理 RO 排除上半窗口；文档 089 定理 RE/RG 排除 resolved sectors 并把剩余项
化为式 (18)；式 (32) 给 parabolic sharp bound。最后使用文档 088 定理 RA。
`□`

## 8. 存在性审计

### 结论 RR（precise analytic-number-theory interface）

当前唯一未证命题已成为一个标准形状的解析数论接口：

- outer variables 是 pairwise-coprime squarefree `g,a,b`；
- determinant variable `delta` 是长度 `gab/Y` 的短和；
- harmonic line 已精确求成 finite Möbius--cotangent sieve；
- reciprocal variables `m,m'` 至多为 `sqrt N`；
- 只需 scales `N<=Y<=N^(3/2)`。

可尝试的工具因此缩为：Kloosterman/cotangent spectral reciprocity、dispersion
method、Möbius bilinear estimates 或对 `(a,b)` 的 Kuznetsov 型处理。尚不能
直接调用经典 Weil bound：式 (15) 的 moduli、outer Möbius amplitudes 与短
`delta` ranges 同时变化，必须证明与目标权重匹配的平均估计。

## 9. 计算实现

`scripts/qw_matrix.py` 新增：

- `farey_determinant_reduction`；
- `generic_unrestricted_farey_harmonic_correlation`。

测试核对 `g|Delta`、reduced primitive condition 与 lcm；并把定理 RL 的
cotangent closed form 与 solution line 上四万个直接 terms 的 symmetric sum
比较。
