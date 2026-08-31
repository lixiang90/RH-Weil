# Selberg--Volterra cross-fiber transport 与 multiscale near-product criterion

文档 167 以 profinite divisibility polarization 无条件控制了 hard arithmetic
coefficient diagonals，但 triangular interval Gram 的 `n ne n'` entries 仍未处理。
本笔记不再把这些 entries 当作一个待猜测的矩阵不等式，而是把它们重新写成一个
精确的 prefix-field transport。

**后续状态修订（文档 169）：** 本文的 exact transport 与 conditional implication
保持不变；但式 (14) 在 polylogarithmic lengths 上并非一个低于 RH 的普通
Selberg input。文档 169 证明该 profile 与 RH 等价，并无条件消去
`N<=T^(2-eta)` 的 sub-square-root wedge。故式 (14)应标记为 `[E]`，而不只是
来源未知的 `[C]`。

主要结论是：

1. modulated prime--continuum window current 是 ordinary prefix discrepancy field
   经过一个显式 Volterra/Abel connection 的像；
2. 因而单一 window length 的 ordinary Selberg energy 确实不能替代 modulation，
   但完整的 multiscale Selberg profile 可以严格控制它；
3. 若该 profile 具有 Selberg-order `N s log^p N`，则全部
   `T>=log^K Y`, `K>p+1` 的 arithmetic near-products 对 barrier 的总贡献为
   `o(1)`；
4. profinite coefficient second moment 单独不能推出这一 prefix estimate，故新的
   条件不是文档 167 diagonal bound 的形式推论；
5. Guth--Maynard large-values theorem 是 superlevel input，不是该 `L2` profile
   的直接替代；一个声称能在 log-power intervals 给出所需 almost-all estimate 的
   预印本 `arXiv:1009.6121` 已由作者因关键引理错误撤回，本文不使用它。

这没有证明 RH，但首次给出了真实的 cross-fiber map，并把 off-diagonal 缺口化为
一个经典、可独立审计的 multiscale Selberg--Hardy 范数。

## 1. Logarithmic prefix field

令 signed prime--continuum measure 为

`dA(u)=d[psi(u)-u]`.                              (1)

对 logarithmic base point `y` 与 prefix length `s>=0`，定义

`B_y(s)=int_(e^y)^(e^(y+s)) dA(u)`

`      =psi(e^(y+s))-psi(e^y)-e^y(e^s-1)`.       (2)

对 `sigma>=1/2`, modulation center `tau` 与 Abel scale `Y`，置

`f_y(s)=exp[-(sigma+itau)(y+s)]`

`       *exp[-e^(y+s)/Y]`.                       (3)

长度 `h` 的 actual modulated current 是

`S_y(h)=int_(e^y)^(e^(y+h))`

`        u^(-sigma-itau)e^(-u/Y)dA(u)`.          (4)

### 定理 ADI（exact Selberg--Volterra transport）[U]

对全部上述参数，Stieltjes 意义下精确成立

`S_y(h)=f_y(h)B_y(h)-int_0^h B_y(s)f_y'(s)ds`,   (5)

其中

`f_y'(s)=-[sigma+itau+e^(y+s)/Y]f_y(s)`.         (6)

因此 modulation 没有被删除：它成为 prefix field 上的显式 Volterra connection

`nabla_(tau,Y)=d/ds+sigma+itau+e^(y+s)/Y`.       (7)

#### 证明

式 (2) 给 `B_y(0)=0` 且 `dB_y(s)` 在推前到 `u=e^(y+s)` 后就是式 (1)。
对式 (4)作 Stieltjes integration by parts，得到

`int_0^h f_y(s)dB_y(s)`

` =f_y(h)B_y(h)-f_y(0)B_y(0)`

`   -int_0^h B_y(s)df_y(s)`.                     (8)

中间项为零，且式 (3)求导给式 (6)。`□`

式 (5) 是所需 cross-fiber correspondence：不同 terminal products 不再由一个
ad hoc matrix entry连接，而是先嵌入同一 prefix fiber `s in [0,h]`，再由
`nabla_(tau,Y)` transport 到 terminal current。

## 2. Multiscale Selberg--Hardy majorant

固定 dyadic arithmetic scale `N>=2`，定义 logarithmic Selberg profile

`J_N(s)=int_(log N)^(log 2N)|B_y(s)|^2dy`,       (9)

以及该 scale 的 modulated sliding energy

`G_N(tau,h)=int_(log N)^(log 2N)|S_y(h)|^2dy`.   (10)

### 定理 ADJ（Selberg--Hardy cross-energy bound）[U]

若 `0<h<=log(3/2)`，则

`G_N(tau,h)<=2N^(-2sigma)J_N(h)`

` +2hN^(-2sigma)[sigma+|tau|+3N/Y]^2`

`       *int_0^h J_N(s)ds`.                      (11)

#### 证明

对式 (5)使用 `|a+b|^2<=2|a|^2+2|b|^2`。第二项再以 Cauchy--Schwarz 得

`|int_0^h B_y(s)f_y'(s)ds|^2`

` <=h int_0^h |B_y(s)|^2|f_y'(s)|^2ds`.         (12)

当 `logN<=y<=log2N` 及 `0<=s<=h<=log(3/2)` 时，`e^(y+s)<=3N`；又

`|f_y(s)|<=N^(-sigma)`,

`|f_y'(s)|<=N^(-sigma)[sigma+|tau|+3N/Y]`.       (13)

对 `y` 积分并用 Tonelli 即得式 (11)。`□`

式 (11)中的第二项是一个 Hardy cost；它要求全部 `0<s<h` prefixes，而不是只要求
terminal variance `J_N(h)`。这正是文档 151 命题 AAP 的 no-go 没有排除的额外
结构。

## 3. Selberg-order profile 推出 full near-product evacuation

取文档 151 的 dyadic heights `tau_T asymp B_T asymp T`、
`h_T=theta/B_T asymp1/T`，barrier `beta_T>=c log(e+T)`。Abel truncation只需
`N<=C Y logY`；更长 arithmetic scales 已由 exponential tail 控制。

### 推论 ADK（conditional full arithmetic near-product evacuation）[C]

假设存在 fixed `p>=0,C_0`，使对所有相关 `N,T,Y` 与 `0<s<=h_T`，

`J_N(s)<=C_0 N s log^p(2N)`.                    (14)

则对任意 fixed `K>p+1`，全部 arithmetic dyadic scales 上有

`sum_(T>=log^K(2Y)) G_(Y,delta)(tau_T,B_T)/beta_T`

` <<log^(p+1-K)(2Y)/loglog(3Y)=o(1)`,           (15)

其中只计 prime--continuum arithmetic current；Gamma 与其它显式 smooth
corrections 仍须按原 barrier ledger 加入。

特别地，经典 Selberg-order profile `J_N(s)<<Nslog^2(2N)` 会把 full arithmetic
near-products 的高区间阈值降到任意 `K>3`，而不只控制 coefficient diagonal。

#### 证明

在高区间 `T>=log^K(2Y)`、`K>1`，对 `N<=CYlogY` 有

`sigma+|tau_T|+3N/Y<<T`                          (16)

（有限个初始 `Y` 吸收到常数）。把式 (14)代入式 (11)，使用
`N^(1-2sigma)<=1` 与 `h_T asymp1/T`，得到每个 arithmetic dyadic scale

`G_N(tau_T,h_T)<<log^p(2N)/T`.                  (17)

相关 `N` 至多 `O(logY)` 个，所以每个 height block

`G_T<<log^(p+1)(2Y)/T`.                          (18)

除以 barrier 后对 dyadic `T>=T_*=log^K(2Y)` 求和，几何级数由首块支配：

`sum G_T/beta_T`

` <<log^(p+1)(2Y)/[T_*logT_*]`,                 (19)

即式 (15)。`□`

推论 ADK 是比“控制 cross Gram”更可审计的存在性条件：式 (14)只读取
prime--continuum prefix discrepancies，不引用 zeros 的位置；但目前本文没有无条件
证明它。

## 4. 为什么 profinite diagonal 不能自动给 prefix profile

### 命题 ADL（scalar second moment does not control Volterra prefixes）[U]

不存在仅依赖 coefficient square mass

`M=sum_(j=1)^H|a_j|^2`                           (20)

的 universal 常数 `C`，使所有 terminal prefixes满足

`|sum_(j=1)^H a_j|^2<=CM`.                       (21)

事实上取 `a_j=1`，左端为 `H^2`，右端的 mass 为 `H`，所需常数至少为 `H`。

因此文档 167 的 profinite `L2` coefficient bound 即使是 polylogarithmic，也不能
独自产生式 (14)；必须使用 prime--continuum centering、Möbius boundary signs 或
其它真正的 prefix cancellation。

该反例不否定 profinite polarization：它说明后者是 diagonal input，而
Selberg--Volterra field 是独立的 cross-fiber input。两者在广义 Weil package 中
应当并列，而非互相冒充。

## 5. Large-values 与文献审计

Guth--Maynard 的已发表 large-values theorem 对 `|b_n|<=1` 的 dyadic Dirichlet
polynomial及一组 `1`-separated large-value points给出 superlevel cardinality bound。
它适合与文档 150 的 layer-cake identity组合，但它本身不是式 (14)的 continuous
`L2` prefix estimate；还需要完成 coefficient normalization、continuous-to-discrete
maximal transfer、prime--continuum balancing及 threshold integration。

检索还发现 `arXiv:1009.6121` 的摘要曾声称
`I_Lambda(N,h)<<Nhlog^5N+Nh^(21/20)log^2N`，并推出 log-power length 的
almost-all prime theorem。然而该稿已由作者撤回；其说明指向
`arXiv:1103.4451v2`，后者明确写明 Lemma 2 因错误的 Lemma A 而有关键错误。
故这一 claim 不能用来验证式 (14)，也不进入本文参考输入。

## 6. 有限实现与下一步

脚本 `scripts/selberg_volterra.py` 实现式 (5)的离散版本。若

`B_j=sum_(k<=j)a_k`,                              (22)

则 exact summation by parts 为

`sum_(j=1)^H f_ja_j`

` =f_HB_H+sum_(j=1)^(H-1)(f_j-f_(j+1))B_j`.     (23)

回归测试同时验证两项 Cauchy majorant，并以 constant block检查命题 ADL 的线性
amplification。

下一步不应再搜索仅有 coefficient diagonal 的 Bessel bound，而应二选一：

1. 对 centered Vaughan/threshold decomposition直接证明式 (14)或一个足以使
   式 (11) barrier-summable 的较弱 nonuniform profile；
2. 保留 layer-cake threshold，建立 Guth--Maynard 型 superlevel capacity 的
   continuous balanced版本，从而绕过 full `L2` profile。

无论选择哪一路，目标都已从模糊的 cross Gram 变成了可逐参数核验的 prefix-field
估计。
