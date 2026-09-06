# Mellin 横坐标、compact-frequency 对偶抽取与 FPW4b

审计报告指出：对任意随尺度变化的正 Gram，定性 divisor visibility 或
Mellin 唯一性并不足以推出 Hodge 范数的幂次下界。本笔记不撤销这个判断，
而是识别出文档 051--057 的 adaptive Sobolev carrier 所具有的额外结构：
它们由同一个 centered Dirichlet series 在全部尺度上相干地产生。这个
Mellin coherence 允许为每个假设的 divisor point 显式构造一个
compact-frequency dual functional；其 dual norm 只有 `exp(O(r_X))`，而其
算术取值的 Mellin transform 在该 divisor point 有真正的 pole。

因此当正整数列 `r_X>=1` 满足 `r_X=o(logX)` 时，zeta adaptive Sobolev Gram 的 FPW4b 可无条件
建立。仍未证明的是 actual arithmetic tightness；所以这里修复的是结构
定理的 separation 步骤，不是 RH。

2026-09-06 有限性补充：以下所有 Sobolev 阶数均为正整数，变化阶数也保持 `r_X>=1`。仅有 `r_X=o(logX)` 会容许 `r_X=0`，此时非零有限指数和的全轴平方积分发散；原先的 dual 估计不能把该无穷量称为有限 Gram 能量。

## 1. Mellin pole 强迫点值幂次增长

### 引理 ACK（Mellin abscissa lower bound）[U]

设 `A:(0,infinity)->C` 局部可积，并在某个原点邻域恒为零。假设

`M_A(z)=int_0^infinity A(X)X^(-z-1)dX`             (1)

在某个右半平面绝对收敛，并从那里亚纯延拓到含 `z_0` 的连通区域。若
`z_0` 是该延拓的真正 pole，则

`limsup_(X->infinity)`

` log(max(1,|A(X)|))/logX >= Re z_0`.              (2)

等价地，存在 `X_j->infinity` 使

`|A(X_j)|>=X_j^(Re z_0-o(1))`.                    (3)

#### 证明

若式 (2) 失败，可取实数 `sigma<Re z_0`，使充分大的 `X` 上
`|A(X)|<=X^sigma`。于是式 (1) 在 `Re z>sigma` 绝对且在紧集上一致收敛，
从而在该半平面全纯。它与原来的 Mellin transform 在初始收敛半平面相等；
恒等定理迫使亚纯延拓在 `z_0` 也全纯，与真正 pole 矛盾。`□`

还有一个将用于文档 051 的固定窗口 `L^2` 版本。若 `f in L^2_loc([0,infinity))`
的 Laplace transform在 `lambda_0` 有真正 pole，则对每个 fixed `H>0`，

`limsup_(T->infinity) (1/T)log max(1,`

`             int_T^(T+H)|f(t)|^2dt)>=2Re lambda_0`. (3a)

确实，若左侧小于 `2sigma<2Re lambda_0`，把半轴分成长度 `H` 的块并用
Cauchy--Schwarz，就有

`int_(kH)^((k+1)H)|f(t)|e^(-eta t)dt`

` <=sqrt(H)e^(-eta kH)`

`   *(int_(kH)^((k+1)H)|f(t)|^2dt)^(1/2)`,         (3b)

对任意 `eta>sigma` 构成几何可和级数。Laplace transform 因而在
`Re z>sigma` 全纯，再次与 pole 矛盾。

这个引理是定量结论，不只是“变换不恒为零”：一个 pole 明确给出点值或
固定窗口能量的横向指数。

## 2. Coherent annular Sobolev carrier

固定中心 `c/2`、annular factor `A_0>1`，记 `B=log A_0`。对尺度 `X` 的
有限系数向量 `x=(x_n)`，其支撑包含于

`X/A_0<n<=A_0X`,                                  (4)

定义去掉无关 global phase 的 exponential polynomial

`F_(X,x)(tau)=sum_n x_n n^(-c/2)`

`                         *exp[-itau log(n/X)]`,   (5)

以及 order-`r` 正 Hodge form，其中统一要求整数 `r>=1`

`Q_(X,r)(x)=(1/(2pi))int_R |F_(X,x)(tau)|^2`

`                              /(tau^2+kappa^2)^r dtau`, (6)

其中 `kappa>0`。有限个 `log n` 互异，而式 (6) 的 weight 几乎处处为正，
所以这是正定 Gram，而不只是半正定 form。

固定 `z_0 in C`。任取有界、紧支撑、非负且满足 `int chi>0` 的 `chi`，令

`h_(z_0)(tau)=int_(-B)^B exp[(z_0-itau)u]du`,      (7)

`q_(z_0)(tau)=chi(tau)h_(z_0)(tau)`.              (8)

定义线性泛函

`ell_(X,z_0)(x)=(1/(2pi))int_R F_(X,x)(tau)`

`                                  *conjugate(q_(z_0)(tau))dtau`. (9)

### 定理 ACL（compact-frequency dual extractor）[U]

若 `supp chi subset [-T,T]`，则

`||ell_(X,z_0)||_(Q_(X,r)^*)^2`

` <=C_(z_0,chi) R^(2r)`,                           (10)

其中 `R=max(1,sqrt(T^2+kappa^2))`，常数与 `X,r` 无关。特别地，若
`r_X=o(logX)`，则

`||ell_(X,z_0)||_(Q_(X,r_X)^*)=X^(o(1))`.         (11)

#### 证明

对式 (9) 在 measure `dtau/(2pi)` 下使用带权 Cauchy--Schwarz：

`|ell(x)|^2<=Q_(X,r)(x)`

` *(1/(2pi))int |q_(z_0)(tau)|^2`

`                         *(tau^2+kappa^2)^r dtau`. (12)

最后一个积分至多为 `C_(z_0,chi)R^(2r)`。当
`r_X=o(logX)` 时，其对数是 `o(logX)`，得到式 (11)。`□`

## 3. 与 centered Dirichlet series 的精确 Mellin compatibility

令 `a(n)` 是固定算术系数，并设

`L_a(s)=sum_(n>=1)a(n)n^(-s)`                     (13)

在某个右半平面绝对收敛。取式 (4) 中的实际向量

`x_(X,n)=a(n)1_(X/A_0<n<=A_0X)`.                 (14)

记 `A_(z_0)(X)=ell_(X,z_0)(x_X)`。再定义

`k_(z_0)(u)=(1/(2pi))int_R`

`             conjugate(q_(z_0)(tau))e^(-itau u)dtau`, (15)

`K_(z_0)(z)=int_(-B)^B k_(z_0)(u)e^(zu)du`.       (16)

逐个 `n` 作变量代换 `u=log(n/X)`，得到初始收敛半平面上的精确恒等式

`int_0^infinity A_(z_0)(X)X^(-z-1)dX`

`=K_(z_0)(z)L_a(c/2+z)`.                          (17)

而由式 (7)--(8) 和 Fubini，

`K_(z_0)(z_0)=(1/(2pi))int_R`

`                   chi(tau)|h_(z_0)(tau)|^2dtau>0`. (18)

严格正性来自 `h_(z_0)` 是非零 entire function，不可能在 `chi` 非零的
正测度集合上恒为零。

### 定理 ACM（Mellin-coherent quantitative separation）[U]

假设 `L_a(s)` 亚纯延拓到含 divisor point `rho` 的区域，并在 `rho` 有真正
pole。令 `z_rho=rho-c/2`，在式 (7)--(9) 取 `z_0=z_rho`。若
`r_X=o(logX)`，则存在 `X_j->infinity` 使

`||ell_(X_j,z_rho)||_(Q_(X_j,r_(X_j))^*)=X_j^(o(1))`, (19)

并且

`|ell_(X_j,z_rho)(x_(X_j))|`

` >=X_j^(Re rho-c/2-o(1))`.                       (20)

因此

`Q_(X_j,r_(X_j))(x_(X_j))`

` >=X_j^(2Re rho-c-o(1))`.                        (21)

#### 证明

式 (18) 保证式 (17) 在 `z_rho` 保留 `L_a` 的真正 pole。引理 ACK 给
式 (20)，定理 ACL 给式 (19)，最后把二者代入式 (12) 得式 (21)。`□`

这里的 dual functional 可以依赖在反证中固定的 `rho`，但 carrier、Hodge
form 和实际算术向量都不依赖零点。这与从零点位置反向制造正内积不同，
没有把 RH 放进结构的定义中。

## 4. 对 zeta adaptive Sobolev Gram 的应用

取 `c=1`、`A_0=4`、`kappa=1/2`，并令

`a(n)=Lambda(n)-1`.                               (22)

其 centered Dirichlet series 是

`L_a(s)=-zeta'(s)/zeta(s)-zeta(s)`.               (23)

在 `s=1`，`-zeta'/zeta` 与 `zeta` 的 residue 都为 `+1`，故在式 (23) 的差中相消；在任一 multiplicity 为
`m_rho` 的非平凡零点 `rho`，式 (23) 的 residue 为 `-m_rho`，所以是真正
pole。式 (6) 正是文档 055 的 `mathcal H_(r_X)(X)`（global phase 不改变
模方）。

### 推论 ACN（adaptive Sobolev FPW4b for zeta）[U]

对任意正整数列 `r_X>=1` 且 `r_X=o(logX)` 和任意非平凡零点 `rho=beta+igamma`，存在
显式 compact-frequency dual functionals 满足式 (19)--(21)，特别是

`limsup_(X->infinity)`

` log(max(1,mathcal H_(r_X)(X)))/logX>=2beta-1`.  (24)

若 `Theta=sup_rho Re rho`，则

`limsup_(X->infinity)`

` log(max(1,mathcal H_(r_X)(X)))/logX`

` >=max(0,2Theta-1)`.                              (25)

结合文档 054--055 已有的 Abel-summation upper bound，得到等号。因此文档
051 的 wavelet exponent、文档 054 的 fixed-order criterion 和文档 055 的
adaptive detector 在这个具体 coherent carrier 上都有严格的定量 separation
证明，不再依赖“单个 mode 自动贡献正能量”的非严格说法。

## 5. 有限 Gram 的 Schur 补证书

在式 (4) 的有限 index set 上，把式 (6) 写成 `x^*G_(X,r)x`，并把
`ell_(X,z_0)(x)` 写成 `d_(X,z_0)^*x`。由于 `G_(X,r)>0`，有精确公式

`||ell_(X,z_0)||_(Q_(X,r)^*)^2`

`=d_(X,z_0)^*G_(X,r)^(-1)d_(X,z_0)`.              (26)

### 命题 ACO（dual norm = Schur margin）[U]

对任意 `eta>=0`，

`[[G_(X,r),d_(X,z_0)],`

`  [d_(X,z_0)^*,eta]]>=0`                         (27)

当且仅当

`eta>=d_(X,z_0)^*G_(X,r)^(-1)d_(X,z_0)`.          (28)

特别地，定理 ACL 给出完全解析的有限证书

`eta=C_(z_0,chi)R^(2r)`.                          (29)

#### 证明

式 (26) 是有限维 Riesz representation；式 (27)--(28) 是对正定块
`G_(X,r)` 的标准 Schur complement。式 (29) 来自式 (10)。`□`

这把 FPW4b 从抽象“可见性”变成了一个可审计的 augmented Gram inequality。
数值上可以计算式 (26)，但证明并不依赖浮点 condition number。

## 6. 对一般 Gamma--Euler 数据的结构定理

定理 ACM 不使用 zeta 的特殊零点分布，只使用：

1. centered Euler coefficients 给一个在右半平面绝对收敛的 Dirichlet series；
2. 该 series 亚纯延拓后在目标 divisor point 有真正 pole；
3. fixed-width annular truncation；
4. translation-invariant Sobolev Hodge weight，且 `r_X=o(logX)`。

因此对任何满足这些条件、中心为 `c/2` 的 paired Gamma--Euler datum，
subpower actual-cycle bound

`Q_(X,r_X)(x_X)=X^(o(1))`                         (30)

都会排除 `Re rho>c/2`；中心对称再排除左侧，故全部 divisor 位于中心线。
这是一个比任意 scale-varying FPW 更窄、但 separation 已自动证明的广义结构
定理。

## 7. 审计边界与下一步

本笔记完成的是：

- 为 zeta adaptive Sobolev carrier 显式构造 FPW4b dual extractor；
- 用 Mellin pole 而不是定性 visibility 证明其算术取值的幂次 lower limsup；
- 给 dual norm 的解析 `exp(O(r_X))` bound 和有限 Schur certificate；
- 对任意固定零点逐点工作，因而不需要对无限零点族作统一 height frame bound。

本笔记没有完成的是：

- 证明 `mathcal H_(r_X)(X)=X^(o(1))`；这仍与 RH 等价；
- 为不具备共同 Dirichlet/Mellin realization 的任意 FPW Gram 自动构造 dual；
- 证明 sampled/moment approximants 自身的全空间 Riesz lower bound。它们的
  中心线蕴含可由与 Sobolev energy 的 subpower additive equivalence转移，
  但这不等于每个近似 Gram 都已有独立 FPW4b；
- 给式 (26) 做 interval-certified cofinal 数值 enclosure。

下一步不再寻找新的 detector。应直接攻击式 (30) 的算术内容：对
`r_X~logX/loglogX` 的平方根/polylog core，证明 centered prime--continuum
向量的 uniform Type I/II matrix Bessel bound，或得到足以使 dyadic negative
trace 可和的 weaker bound。