# 240. Möbius pullback、相邻 divisor columns 与带符号 dyadic dispersion

日期：2026-09-03

分支：MOM-1 / 路线 A1t -> A1u；接口：quotient-first centered Vaughan response / fixed-power four-moment closure

状态：Vaughan synthesis pullback、二维离散 Abel 分解、dyadic Mertens-response blocks
与 algebra-only no-free-lunch 为 [T]/[N]；finite centered pullback/variation ratios 为
[E]；actual adjacent-divisor dyadic mean-square 为 [O]。本笔记不更新 PDF，不改变
零点比例的 [C] 状态。

## 1. 本轮结论

笔记 239 把剩余 physical response 写成

\[
 \sum_{r,s}\mu(r)\mu(s){\mathcal K}_X(r,s).
\tag{1}
\]

只写成式 (1) 仍有循环风险。本轮证明这个 kernel 是 numerator response matrix
沿 Vaughan divisor synthesis 的精确 pullback：

\[
 \boxed{{\mathcal K}_X=T_X^*B_X^{\rm cent}T_X,\qquad T_X\mu=\Lambda.}
\tag{2}
\]

所以式 (1) 本身与 original centered prime response 完全相同，不因出现
`mu` 字样自动获得 Mertens saving。真正的新坐标来自二维 Abel：若
`M(r)=sum_(n<=r)mu(n)`，则

\[
 \mu^*{\mathcal K}_X\mu
 =\sum_{r,s}M(r)M(s)
 \langle U_r,B_X^{\rm cent}U_s\rangle,
 \qquad U_r=T_r-T_{r+1}.
\tag{3}
\]

这里 `U_r` 是相邻 divisor-incidence columns 的差；它在 `r` 上并不光滑。
因此逐 entry 取绝对值的 ordinary variation 路线被降级。保留 block 内符号后，
下一最小算术输入变成一个明确的 dyadic adjacent-divisor response mean-square。

## 2. Vaughan synthesis operator

固定 finite numerator cell `A_X`，其每个 `a>V`。令 active divisor set 为
`R_X={1,...,R}`，其中 `R` 至少覆盖所有可能满足 `rvw=a`、`v>V` 的 `r`。
定义实矩阵

\[
 T_{a,r}
 =\sum_{\substack{v>V,\ w\ge1\\rvw=a}}\Lambda(v).
\tag{4}
\]

把第 `r` 列记为 `T_r`。对任意 divisor coefficients `x=(x_r)`，其合成的
numerator coefficient 为

\[
 (Tx)(a)=\sum_r x_rT_{a,r}.
\tag{5}
\]

### 定理 240-A（exact Möbius synthesis）[T]

逐个 `a in A_X` 有

\[
 \boxed{(T\mu)(a)=\Lambda(a).}
\tag{6}
\]

#### 证明

由 Dirichlet convolution 的结合律与交换律，

\[
 \begin{aligned}
 (T\mu)(a)
 &=\sum_{rvw=a}\mu(r)\Lambda_{>V}(v)\\
 &=(\mu*1*\Lambda_{>V})(a)
 =(\varepsilon*\Lambda_{>V})(a)
 =\Lambda_{>V}(a).
 \end{aligned}
\tag{7}
\]

cell 中 `a>V`，故最后一项是 `Lambda(a)`。`square`

这一定理也解释 composite ghost atoms：单列 `T_r` 可在 composite rows 上非零，
但 actual Möbius combination 在这些 rows 上精确消去。

## 3. Centered response 的 pullback

令 `B_X^cent` 是 numerator coefficient space 上的 Hermitian bilinear response
matrix。其 `(a,c)` entry 已经求和：

1. denominator variables `b,d` 及其 von Mangoldt weights；
2. fixed integer-pair masks 与四个平方根归一化；
3. exact six-window overlap；
4. exact consecutive Gabor kernel；
5. 笔记 239-E 在 physical quotient 后施加的共同 linear shell centering。

因此对 numerator coefficients `f,g`，笔记 239 的 centered form可写为

\[
 {\mathfrak R}_X^{\rm cent}[f,g]=f^*B_X^{\rm cent}g.
\tag{8}
\]

### 定理 240-B（divisor kernel is an exact pullback）[T]

笔记 239-(23) 的 kernel 满足

\[
 \boxed{{\mathcal K}_X(r,s)
 =T_r^*B_X^{\rm cent}T_s,}
\qquad
\boxed{{\mathcal K}_X=T^*B_X^{\rm cent}T.}
\tag{9}
\]

特别地，

\[
 \boxed{
 \mu^*{\mathcal K}_X\mu
 =\Lambda^*B_X^{\rm cent}\Lambda.}
\tag{10}
\]

#### 证明

式 (5) 与式 (8) 的双线性给

\[
 {\mathfrak R}_X^{\rm cent}[Tx,Ty]
 =x^*T^*B_X^{\rm cent}Ty.
\tag{11}
\]

逐项展开式 (11) 正是笔记 239-(23) 对除 `r,s` 外全部变量的求和，得到式
(9)。再令 `x=y=mu` 并使用定理 240-A，得到式 (10)。`square`

### 推论 240-C（quotient invariance）[T]

若 `h in ker T`，则

\[
 {\mathcal K}_Xh=0,
 \qquad
 (\mu+h)^*{\mathcal K}_X(\mu+h)
 =\mu^*{\mathcal K}_X\mu.
\tag{12}
\]

所以 divisor coordinates 中只有 quotient `C^R/ker T` 可被 physical response
看见。任何依赖 representative 而不在此 quotient 上不变的 norm 或 partial-sum
预算，都不是 intrinsic physical quantity。

## 4. Algebra-only Möbius gain 不存在

### 障碍定理 240-D（synthesis-pullback no-free-lunch）[N]

固定 `T,mu` 且 `lambda=Tmu ne 0`。若一个 Hermitian response class 在保持
`T,mu` 不变时允许 rank-one family

\[
 B_\tau=\tau\frac{|\lambda\rangle\langle\lambda|}{\|\lambda\|_2^2},
 \qquad \tau>0,
\tag{13}
\]

则不存在只依赖 `T`、`mu`、Mertens partial sums 或 convolution identity 的
uniform upper bound 控制 `mu^*T^*B_tau Tmu`。事实上

\[
 \mu^*T^*B_\tau T\mu=\tau\|\lambda\|_2^2\longrightarrow\infty.
\tag{14}
\]

#### 证明

把 `Tmu=lambda` 代入式 (13) 即得式 (14)。`square`

这不是说 actual Gabor response matrix 可以任意取式 (13)。它精确说明：
Vaughan/Möbius synthesis 代数本身不能产生所需 `o(L^4)`；证明必须使用
`B_X^cent` 的 exact band、determinant、window 或 prime-correlation 结构。

## 5. 二维 Abel 与相邻 divisor columns

置

\[
 M(r)=\sum_{n\le r}\mu(n),\qquad M(0)=0,
\tag{15}
\]

并约定 `T_(R+1)=0`、`K(R+1,s)=K(r,R+1)=0`。定义

\[
 U_r=T_r-T_{r+1},
\tag{16}
\]

以及 mixed forward difference

\[
 \Delta_{12}{\mathcal K}(r,s)
 ={\mathcal K}(r,s)-{\mathcal K}(r+1,s)
 -{\mathcal K}(r,s+1)+{\mathcal K}(r+1,s+1).
\tag{17}
\]

### 定理 240-E（exact two-dimensional Abel pullback）[T]

有三个 exact identities：

\[
 \boxed{
 \sum_{r=1}^R M(r)U_r=T\mu=\Lambda,}
\tag{18}
\]

\[
 \boxed{
 \Delta_{12}{\mathcal K}(r,s)
 =U_r^*B_X^{\rm cent}U_s,}
\tag{19}
\]

以及

\[
 \boxed{
 \mu^*{\mathcal K}\mu
 =\sum_{r,s=1}^RM(r)M(s)
 \Delta_{12}{\mathcal K}(r,s).}
\tag{20}
\]

#### 证明

式 (18) 中 `T_j` 的 coefficient 是 `M(j)-M(j-1)=mu(j)`。式 (19) 把
定理 240-B 的四个 entries展开即可。式 (20) 可对 `r,s` 各作一次有限 Abel
summation，或把式 (18) 代入式 (19) 后求和。`square`

式 (20) 给出严格的 sufficient absolute bound

\[
 |\mu^*{\mathcal K}\mu|
 \le
 \sum_{r,s}|M(r)M(s)\Delta_{12}{\mathcal K}(r,s)|
 \le \|M\|_\infty^2V_{12}({\mathcal K}),
\tag{21}
\]

其中 `V_12(K)=sum_(r,s)|Delta_12 K(r,s)|`。但式 (21) 在每个 adjacent
divisor pair 后立即取绝对值，可能丢失主要 physical cancellation。

### 障碍命题 240-F（divisor columns 没有形式上的 smoothness）[N]

只由式 (4) 不能推出 `U_r` 随 `r` 作任何 uniform power decay。更精确地，若
`a=rp`，其中 prime power `p>V`，且 `r+1` 不整除 `a`，则

\[
 T_{a,r}\ge\Lambda(p),\qquad T_{a,r+1}=0,
 \qquad |U_r(a)|\ge\Lambda(p).
\tag{22}
\]

#### 证明

在式 (4) 中取 `v=p,w=1` 给第一式。每个贡献到 `T_(a,r+1)` 的 tuple 都要求
`r+1` 整除 `a`，故第二式成立；相减得到第三式。`square`

因此不能把 `r` 当连续 smooth variable，用普通 derivative/Schur variation
直接声称 `Delta_12 K` 很小。任何 saving 必须平均 adjacent divisibility，而非
只估计 kernel envelope。

## 6. Dyadic signed localization

把 `{1,...,R}` 分成 dyadic intervals `I_j`，并定义 numerator-space vectors

\[
 Z_j=\sum_{r\in I_j}M(r)U_r.
\tag{23}
\]

若 `I_j=[A,B]`，一次局部 telescoping 还给

\[
 \boxed{
 Z_j=M(A)T_A+
 \sum_{r=A+1}^{B}\mu(r)T_r-M(B)T_{B+1}.}
\tag{24}
\]

这把每个 block 具体化为 truncated Möbius synthesis 加两个 endpoint columns，
没有 arbitrary coefficients。

定义 block response matrix

\[
 C_{ij}=Z_i^*B_X^{\rm cent}Z_j.
\tag{25}
\]

### 定理 240-G（dyadic Mertens-response reduction）[T/C]

若 dyadic block 数为 `J`，则

\[
 \mu^*{\mathcal K}\mu=\sum_{i,j=1}^JC_{ij},
\tag{26}
\]

且

\[
 \left|\mu^*{\mathcal K}\mu\right|
 \le J\left(\sum_{i,j}|C_{ij}|^2\right)^{1/2}.
\tag{27}
\]

在 fixed-power cell 中 `J=O(L)`。所以 arithmetic mean-square input

\[
 \boxed{
 \sum_{i,j}|C_{ij}|^2=o(L^6)}
\tag{28}
\]

足以推出 required response `o(L^4)`。

式 (26)--(27) 为 [T]；对 actual primes 证明式 (28) 为 [O]，故完整 closure
仍为 [C]。

#### 证明

式 (23) 对 `j` 求和后用定理 240-E-(18)，再代入式 (25)，得到式 (26)。
对 `J^2` 个 entries 用 Cauchy--Schwarz 得式 (27)。因 `R` 是 `X` 的固定幂，
`J<=1+log_2 R=O(L)`；式 (28) 因而给 `O(L)*o(L^3)=o(L^4)`。`square`

式 (28) 严格强于目标，并非目标的改写；其价值在于每个 `C_ij` 有式 (24) 的
actual truncated Möbius coefficients，可尝试 dispersion/large-sieve。若证明过程
把 `Z_j` 换成 arbitrary vector norm，则又回到被笔记 238 排除的 full Bessel
预算。

## 7. Finite centered audit [E]

脚本 `scripts/mobius_divisor_pullback_audit.py` 固定 `theta=3/4`、`kappa=1/4`、
central proof scale `M=X^(1/2)`，并逐项验证：

1. `Tmu=Lambda`；
2. `K=T^*B^cent T` 在 actual Möbius vector 上重构 direct response；
3. 二维 Abel identity (20)；
4. dyadic block identity (26) 与两个 majorants。

输出摘要如下；`retention` 是 actual response 除以 entrywise Abel absolute
budget。

| `X` | active `r` | pairs | response/`L^4` | Abel-abs/`L^4` | retention | dyadic-`l1`/`L^4` | dyadic-Cauchy/`L^4` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 400 | 29 | 28,466 | `+5.44e-8` | `3.30e-6` | `1.65e-2` | `2.58e-7` | `3.57e-7` |
| 800 | 39 | 131,090 | `-3.92e-8` | `5.48e-6` | `7.15e-3` | `5.40e-7` | `9.69e-7` |
| 1,600 | 65 | 526,249 | `-1.42e-8` | `6.12e-6` | `2.32e-3` | `4.85e-7` | `1.06e-6` |
| 3,200 | 92 | 2,346,769 | `-3.09e-9` | `5.61e-6` | `5.51e-4` | `3.26e-7` | `5.68e-7` |

entrywise absolute Abel 在四个尺度只保留约 `1.6%` 到 `0.055%` 的 signed
response；dyadic blocking恢复约一个数量级，但仍明显损失跨 block cancellation。
这只说明 finite route selection，不证明任何 asymptotic。尤其表中每个量很小不能
替代 uniform global cell ledger。

## 8. 下一最小引理 240-H [O]

固定 `theta=3/4,kappa=1/4` 与一个 balanced factor/aperture cell。使用式 (24)
逐个展开 `C_ij`，保留：

- exact determinant condition `ad-bc`；
- `v,v'>V` 的两个 prime-power variables 与 completions `w,w'`；
- denominator von Mangoldt variables `b,d`；
- common-centered exact Gabor multiplier；
- 两个 endpoint columns，不把它们吸收到 arbitrary norm。

下一轮只攻击一个 dyadic rectangle family（优先 `i`、`j` 相隔至少两层），证明

\[
 \sum_{|i-j|\ge2}|C_{ij}|^2=o(L^6),
\tag{29}
\]

或给出反向 lower-bound evidence。相邻/对角 blocks 留作独立 local problem。
式 (29) 若成功尚不足以完成式 (28)，但它可证伪、保留 actual response direction，
并会把剩余缺口缩到 `|i-j|<=1`。

晋级条件：得到带 uniform constants 的式 (29)，且 endpoint columns与所有 factor
cells 有 global ledger。止损条件：

1. 若估计第一步取式 (21) 的 entrywise absolute variation，停止；
2. 若使用 `||B_X^cent||op` 或 arbitrary coefficient large sieve，停止；
3. 若 dyadic Cauchy bound 相对 actual response 的 finite loss继续幂级增长，则把
   式 (28) 降为观察线，改做直接 determinant-frequency dispersion；
4. 若所谓 proof 只把式 (26) 重新命名而没有独立 mean-square inequality，停止。

## 9. 最小公理、删除审计与循环性

本轮结果只用：

1. **finite Dirichlet convolution**：给 `Tmu=Lambda`；
2. **共同 linear response matrix**：给 pullback `T^*BT`；
3. **同一个 physical centering**：保证 `B_X^cent` 不依 channel representative；
4. **finite Abel summation**：给 adjacent columns 与 Mertens weights；
5. **dyadic partition**：给 `O(L)` 个 actual localization vectors。

删除审计：

- 删除 convolution identity，式 (6) 与 prime response reconstruction失效；
- channelwise 非线性 centering不再产生共同 matrix `B_X^cent`；
- 删除 exact band/determinant arithmetic，定理 240-D 表明 Möbius data不能控制
  arbitrary `B`；
- 把 adjacent differences假设为 smooth，被命题 240-F 反驳；
- 把 block signs取绝对值只给充分上界，不是必要条件。

非同义反复审计：定理 240-B 明确指出式 (1) 单独只是 pullback identity，因此不把
它算作 arithmetic progress；新的、严格更强且可独立否证的输入是式 (28)/(29)。

循环性审计：全部 [T]/[N] 使用有限 convolution、矩阵乘法、rank-one countermodel、
有限 Abel 与 Cauchy--Schwarz；不调用 RH/GRH、Mertens 的 RH 等价点态界、
Hardy--Littlewood 四素数渐近、Weil positivity、谱酉性或 bounded negative index。

## 10. 模型范围与 Weil 接口

- **Riemann zeta**：`Tmu=Lambda` 与式 (24)--(29) 是 actual fixed-power四矩响应的
  arithmetic interface。
- **primitive Dirichlet L**：把 `Lambda` 换成带 character 的 coefficients 后
  synthesis恒等式仍可写，但 `B`、`T` 变成 complex；全部转置改为 adjoint。
- **Dedekind/automorphic L**：只有在先证明相应 coefficient convolution identity
  后才能定义 `T`；不得从 Euler product形式直接假定。
- **函数域**：degree divisor synthesis有离散 lattice alias；pullback/Abel代数保留，
  actual `B^cent` 的 band结构必须重算。
- **一般谱 zeta模型**：若无 Möbius inversion，则本轮 divisor-coordinate结果不适用；
  定理 240-D 仍是任何 synthesis-only argument 的抽象障碍。
- **上同调型 Weil 结构**：本轮完全属于显式公式/响应矩阵侧；没有构造 Frobenius、
  polarization 或 Hard Lefschetz bridge。

本轮把 A1t 的风险点严格定性：quotient 后的 Möbius kernel不是新的 positivity，
而是 original response 的 pullback。可继续的非循环输入只剩 actual
adjacent-divisor dyadic dispersion，而非普通 Mertens bound或 full operator norm。
