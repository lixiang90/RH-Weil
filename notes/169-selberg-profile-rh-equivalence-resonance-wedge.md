# Multiplicative Selberg profile 的 RH 等价性与平方根共振楔

文档 168 把 modulated near-product energy 精确传输到 ordinary prefix field

`B_y(s)=psi(e^(y+s))-psi(e^y)-e^y(e^s-1)`

的 multiscale profile

`J_N(s)=int_(log N)^(log 2N)|B_y(s)|^2dy`.       (1)

本笔记修正一个重要的逻辑边界：所需的 Selberg-order profile 并不是可直接从
经典无条件 short-interval theorem 调入的较弱输入。在 polylogarithmic
multiplicative lengths 上，它本身已经与 RH 等价。另一方面，在真正进入这一
RH-strength 区域之前，仍有一个可无条件删除的两参数楔：全部
`N<=T^(2-eta)` 的 arithmetic scales。

主要结论是：

1. 对任意 primes/integers，不使用 cancellation 就有
   `J_N(s)<<Ns(Ns+1)log(3N)`；
2. 结合 Selberg--Volterra Hardy majorant，这无条件消去
   `N<=T^(2-eta)` 的全部高 dyadic heights；
3. 若对某个 `K,p` 在 `s<=log^(-K)N` 上有
   `J_N(s)<<Nslog^pN`，则 RH 成立；
4. RH 下 Saffari--Vaughan/Selberg 的 multiplicative variance 加上一个
   elementary prime-power estimate 反过来给该 profile（可取 `p=2`）；
5. 因而文档 168 的 `(SP)` 是 zeros-independent 的 prime-side formulation，
   但不是低于 RH 的已知输入。真正未决区域被压到
   `N>T^(2-eta)` 的 square-root resonance wedge。

## 1. Elementary microscopic profile

记

`P_y(s)=psi(e^(y+s))-psi(e^y)`,

`L_y(s)=e^y(e^s-1)`, `B_y(s)=P_y(s)-L_y(s)`.     (2)

### 定理 ADM（elementary multiplicative-prefix bound）[U]

存在 absolute constant `C`，使对全部 `N>=2` 与
`0<s<=log(3/2)`，

`J_N(s)<=C Ns(Ns+1)log(3N)`.                    (3)

特别地，当 `Ns<=1` 时，

`J_N(s)<<Nslog(3N)`.                            (4)

#### 证明

对固定 `n`，条件 `e^y<n<=e^(y+s)` 等价于

`log n-s<=y<log n`,                              (5)

故该 atom 对 `y`-积分的 incidence length 至多为 `s`。由 Tonelli 与
Chebyshev bound `psi(x)<<x`，

`int_(logN)^(log2N)P_y(s)dy`

` <=s psi(3N)<<sN`.                              (6)

另一方面，每个窗口所含整数至多 `3Ns+1` 个，所以

`sup_y P_y(s)<=(3Ns+1)log(3N)`.                  (7)

因 `P_y(s)>=0`，式 (6)--(7) 给

`int P_y(s)^2dy<=sup_yP_y(s) int P_y(s)dy`

` <<Ns(Ns+1)log(3N)`.                           (8)

又 `e^s-1<<s`，所以

`int_(logN)^(log2N)L_y(s)^2dy<<N^2s^2`,          (9)

它被式 (3)右端吸收。最后用
`|P-L|^2<=2P^2+2L^2` 即得。`□`

这个 bound 不使用 prime-pair cancellation。其大窗口部分为
`N^2s^2` 量级，不能越过平方根共振区；但微观 incidence factor `s` 会消除
pointwise `+1` 所造成的假常数损失。

## 2. Unconditional sub-square-root wedge evacuation

沿文档 168，取 `tau_T asymp T`、`h_T asymp 1/T`、
`beta_T>>log(e+T)`，并只计 Abel-relevant `N<=CYlogY`。当
`T>=log^K(2Y)`, `K>=1` 时，

`sigma+|tau_T|+3N/Y<<T`.                         (10)

### 定理 ADN（unconditional resonance-wedge localization）[U]

固定 `eta in (0,1)`。对全部充分大的 `Y`，

`sum_(T>=T_*) 1/beta_T`

` *sum_(N dyadic, N<=min(CYlogY,T^(2-eta)))`

`   G_N(tau_T,h_T)`

` <<T_*^(-eta)+log(2T_*)/T_*`,                  (11)

其中外和取 dyadic heights。特别地，若
`T_*=log^K(2Y)`，则式 (11)为 `o(1)`。

#### 证明

把式 (3)代入文档 168 的 Selberg--Hardy majorant。由
`N^(-2sigma)<=N^(-1)`、式 (10)及 `h_T asymp 1/T`，

`G_N(tau_T,h_T)`

` <<log(3N)[N/T^2+1/T]`.                        (12)

这里 Hardy 项使用

`int_0^h Ns(Ns+1)ds=N^2h^3/3+Nh^2/2`.          (13)

对 `N<=T^(2-eta)` 的 dyadic scales 求和，并除以
`beta_T>>logT`，得到每个 height block 至多

`O(T^(-eta)+log(2T)/T)`.                         (14)

再对 dyadic `T>=T_*` 求和，几何级数由首块支配，给式 (11)。`□`

所以未决的 arithmetic near-products 可进一步限制为

`N>T^(2-eta)`,                                   (15)

即 `T<N^(1/(2-eta))`。对应 additive interval length
`H=N/T` 位于平方根尺度附近或以上；这正是 generic Hilbert spacing term不再
可和的 resonance wedge。

## 3. Polylogarithmic profile implies RH

以下结论不使用显式公式逐零点估计，而只使用固定倍增增量的 Mellin transform。

### 定理 ADO（polylog profile criterion is RH-strength）[E]

假设存在 fixed `K>0`, `p>=0`, `C`，使对全部充分大的 `N` 及

`0<s<=log^(-K)(4N)`                              (16)

都有

`J_N(s)<=C Nslog^p(2N)`.                         (17)

则 Riemann hypothesis 成立。

#### 证明：第一步，微增量望远镜化为固定倍增

令 `E(x)=psi(x)-x`，取

`M=ceil[(log2)log^K(8N)]`, `r=(log2)/M`.          (18)

则 `r<=log^(-K)(8N)`，所以同一 `r` 同时落在 scales `N` 与 `2N` 的
允许范围内，而

`E(2x)-E(x)=sum_(j=0)^(M-1)`

` [E(e^r e^(jr)x)-E(e^(jr)x)]`.                 (19)

对式 (19)使用 `|sum z_j|^2<=M sum|z_j|^2`，再对
`x=e^y`, `y in [logN,log2N]` 积分。每个 shifted base interval落在
`[logN,log4N]`，故被 `J_N(r)+J_(2N)(r)` 控制。于是

`int_N^(2N)|E(2x)-E(x)|^2 dx/x`

` <<M^2 Nrlog^p(4N)`

` <<Nlog^(K+p)(4N)`.                             (20)

#### 第二步，Mellin continuation 排除右半平面零点

由式 (20)与 dyadic Cauchy--Schwarz，

`I(z)=int_1^infinity [E(2x)-E(x)]x^(-z-1)dx`     (21)

在 `Re z>1/2` 绝对局部一致收敛，因而全纯。另一方面，在
`Re z>1`，

`M_E(z)=int_1^infinity E(x)x^(-z-1)dx`

` =-(1/z)zeta'(z)/zeta(z)-1/(z-1)`,             (22)

且换元给

`I(z)=(2^z-1)M_E(z)`

` -2^z int_1^2 E(u)u^(-z-1)du`.                 (23)

式 (23)最后一项是 entire function；若 `rho` 是
`Re rho>1/2` 的 nontrivial zero，则式 (22)在 `rho` 有极点，而
`2^rho-1 ne0`（因为 `|2^rho|>1`）。这与式 (21)在该半平面的全纯性矛盾。
故没有 `Re rho>1/2` 的非平凡零点；函数方程的中心反射再排除
`Re rho<1/2`，所以全部非平凡零点位于中心线。`□`

这里 `(SP)` 的定义完全在 primes 一侧，不显式引用 zeros；但定理 ADO 说明，
其 polylog-scale uniformity 已编码 RH 的全部难度。把它称为“经典 Selberg-order
输入”而不标记 `[E]` 会低估其逻辑强度。

## 4. RH gives the profile

Saffari--Vaughan 的 Lemma 5 在 RH 下证明，对 `0<delta<=1`，

`int_N^(2N)|vartheta(x+delta x)-vartheta(x)-delta x|^2dx`

` <<delta N^2 log^2(2/delta)`.                   (24)

这是 conditional theorem；其同文的 unconditional zero-density版本只在较长
区间给相对误差型估计，不能替代式 (24)。

### 定理 ADP（RH equivalence of the multiscale profile）[E]

RH 等价于：存在（等价地，对任意）`K>0` 以及某个 fixed `p`，使对全部充分大
`N` 与 `0<s<=log^(-K)(4N)` 有

`J_N(s)<<Nslog^p(2N)`.                           (25)

在 RH 方向可取 `p=2`。

#### 证明

式 (25)推出 RH 是定理 ADO。反之假设 RH，令
`delta=e^s-1 asymp s`。当 `s>=1/N` 时，把式 (24)除以
`x asymp N`，得到 `vartheta` 对应的 logarithmic profile

`<<Nslog^2(2/s)<<Nslog^2(2N)`.                  (26)

令 `R=psi-vartheta`。由 Chebyshev bound，`R(3N)<<sqrt(N)log(3N)`；
对其非负 prime-power increments重复定理 ADM 的 incidence argument，得到

`int_[logN,log2N]|R(e^(y+s))-R(e^y)|^2dy`

` <<Nslog^2(3N)`.                                (27)

式 (26)--(27)给 `psi` 的式 (25)。当 `s<1/N` 时直接使用定理 ADM，
此时 `Ns+1<=2`，得到更强的 `Nslog(3N)`。`□`

## 5. 对结构计划的修订

现在的严格区域图是

`N<=T^(2-eta)` -- elementary incidence/Hardy --> `o(1)`,

`N>T^(2-eta)`  -- square-root resonance wedge --> RH-strength. (28)

因此下一步不能把目标写成“从经典无条件 Selberg theorem推出 `(SP)`”。可行的
非循环突破必须直接在式 (28)右侧增加结构，例如：

1. 只控制 barrier layer-cake 所读取的负方向，而不是 full positive `L2` profile；
2. 用 threshold-complex harmonic signs构造 signed prefix current，使其固定倍增
   Mellin transform不再逐字等于 `-(zeta'/zeta)/z`；
3. 在 `N>T^(2-eta)` 内证明 prime/Gamma joint Loewner inequality，允许
   continuum 与 archimedean barrier在平方前参与，而不是先孤立 `psi-x`；
4. 对一般 Gamma--Euler 数据，把对应 fixed-dilation Mellin factor列入审计，防止
   将 GRH-equivalent variance误标成普通 local counting input。

本笔记没有证明 RH；它一方面无条件删除了 sub-square-root wedge，另一方面证明
剩余的 full Selberg profile路线已经到达 RH 等价壁垒。
