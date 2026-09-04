# 254. Balanced-core multiplier degeneracy 与 energy reweighting obstruction

日期：2026-09-04

分支：NCE-8 / 路线 B1；接口：B1l degree-two Brownian multiplier / matched
prime--continuum core

状态：degree-two actual multiplier 的 normalized discrepancy normal form、局部显式
二侧估计及 matched PNT core 上的 quadratic extinction 为 [T/N]；有限尺度表为 [E]。
这是一条结构性障碍：笔记 253 的 ratio core 不能继续被视为带 scale-neutral
multiplier 的能量 core。本文只处理笔记 244 的 sign-pure prime--continuum Brownian
subsystem；Gamma residual 尚未并入，不声称 RH/GRH、完整 Schur gain或 Weil 正性。

## 1. Actual two-channel multiplier 的尺度参数

取笔记 244 的 even nonnegative prime 与 continuum source measures `a,b`，记

\[
 A=a(\mathbb R),\qquad B=b(\mathbb R),\qquad
 S=A+B>0,\qquad M=A-B.
\tag{1}
\]

其 centered nonnegative symbols为

\[
 W_p=A-\widehat a,\qquad W_c=B-\widehat b.
\tag{2}
\]

完整 signed base symbol `d=a-b` 因而满足 exact identity

\[
 \widehat d=M-W_p+W_c.
\tag{3}
\]

当前 degree-two construction固定

\[
 \kappa=\frac{\sqrt3}{2},\qquad
 \ell=\kappa S,\qquad \rho=\frac S3,
\tag{4}
\]

以及

\[
 \alpha=\frac{\kappa}{\kappa+1/3},
 \qquad
 \gamma=-\frac{4\alpha^2}{9S^4}.
\tag{5}
\]

这里 `gamma` 正是实现中 `-(polynomial_factor)^2`；它不是可自由调节的外部权。
divided difference polynomial为

\[
\begin{aligned}
 Q_{M,\ell}(X)={}&X^4+(M-2\ell)X^3+(M-\ell)^2X^2\\
 &+M(M-\ell)^2X+M^2(M-\ell)^2.
\end{aligned}
\tag{6}
\]

故 actual response measure为

\[
 d\omega_{\rm resp}(\xi)=
 \frac{|\gamma Q_{M,\ell}(\widehat d(\xi))|^2}
 {2\pi\xi^2}\,d\xi.
\tag{7}
\]

prime--continuum diagonal则是

\[
 D=\int_{\mathbb R}(W_p^2+W_c^2)\,d\omega_{\rm resp}.
\tag{8}
\]

## 2. Exact normalized discrepancy normal form

定义两个无量纲 discrepancy coordinates

\[
 \mu=\frac MS,qquad
 \Delta(\xi)=\frac{W_p(\xi)-W_c(\xi)}S,
 \qquad x(\xi)=\frac{\widehat d(\xi)}S=\mu-\Delta(\xi).
\tag{9}
\]

### 定理 254-A（exact response normal form）[T]

定义

\[
\begin{aligned}
 q_\kappa(\mu,\Delta)={}&
 \kappa^2(\Delta^2-3\mu\Delta+3\mu^2)\\
 &+2\kappa(\Delta^3-4\mu\Delta^2
        +6\mu^2\Delta-4\mu^3)\\
 &+(\Delta^4-5\mu\Delta^3+10\mu^2\Delta^2
        -10\mu^3\Delta+5\mu^4).
\end{aligned}
\tag{10}
\]

则逐频率精确有

\[
 \boxed{
 Q_{M,\ell}(\widehat d)=S^4q_\kappa(\mu,\Delta),
 \qquad
 \gamma Q_{M,\ell}(\widehat d)
 =-\frac{4\alpha^2}{9}q_\kappa(\mu,\Delta).}
\tag{11}
\]

特别地，

\[
 q_\kappa(\mu,0)
 =\mu^2(\kappa-\mu)(3\kappa-5\mu),
 \qquad
 q_\kappa(0,\Delta)=\Delta^2(\kappa+\Delta)^2.
\tag{12}
\]

#### 证明

式 (3) 给 `widehat d=S(mu-Delta)`；式 (4) 给 `ell=kappa S`。把它们代入式
(6)，提出齐次因子 `S^4`，得到

\[
\begin{aligned}
 q={}&x^4+(\mu-2\kappa)x^3+(\mu-\kappa)^2x^2\\
 &+\mu(\mu-\kappa)^2x+\mu^2(\mu-\kappa)^2,
 \qquad x=\mu-\Delta.
\end{aligned}
\tag{13}
\]

展开式 (13) 即为式 (10)；再乘式 (5) 得式 (11)。分别令 `Delta=0`、`mu=0`
并因式分解，得到式 (12)。`square`

## 3. 退化阶恰为二次

式 (10) 的 homogeneous quadratic part为

\[
 q_2(\mu,\Delta)
 =\kappa^2(\Delta^2-3\mu\Delta+3\mu^2).
\tag{14}
\]

其矩阵本征值为

\[
 \lambda_\pm=\frac{4\pm\sqrt{13}}2,
\tag{15}
\]

均严格为正。故 balanced point `(mu,Delta)=(0,0)` 不是更高阶或不定退化。

### 定理 254-B（explicit quadratic two-sided bound）[T/N]

置

\[
 \varepsilon_0=10^{-3},qquad
 R_0=2(30\kappa\varepsilon_0+31\varepsilon_0^2),
\tag{16}
\]

\[
 c_-:=\kappa^2\lambda_- -R_0>0,
 \qquad
 c_+:=\kappa^2\lambda_+ +R_0.
\tag{17}
\]

数值上

\[
 c_->0.09589,qquad c_+<2.905.
\tag{18}
\]

只要 `|mu|+|Delta|<=epsilon_0`，就有

\[
 \boxed{
 c_-(\mu^2+\Delta^2)
 \le q_\kappa(\mu,\Delta)
 \le c_+(\mu^2+\Delta^2).}
\tag{19}
\]

因此 actual multiplier满足

\[
 \frac{4\alpha^2c_-}{9}(\mu^2+\Delta^2)
 \le |\gamma Q_{M,\ell}(\widehat d)|
 \le\frac{4\alpha^2c_+}{9}(\mu^2+\Delta^2).
\tag{20}
\]

#### 证明

由式 (15)，

\[
 \kappa^2\lambda_-(\mu^2+\Delta^2)
 \le q_2\le
 \kappa^2\lambda_+(\mu^2+\Delta^2).
\tag{21}
\]

置 `s=|mu|+|Delta|`。式 (10) 的 cubic coefficients绝对值和为 `30kappa`，
quartic coefficients绝对值和为 `31`，所以

\[
 |q_\kappa-q_2|\le30\kappa s^3+31s^4
 \le(30\kappa\varepsilon_0+31\varepsilon_0^2)s^2.
\tag{22}
\]

又 `s^2<=2(mu^2+Delta^2)`，故 remainder至多
`R_0(mu^2+Delta^2)`。直接计算

\[
 \kappa^2\lambda_- -R_0
 =0.0958947474\ldots>0
\tag{23}
\]

给式 (19)；式 (11)给式 (20)。`square`

`[N]` 的内容是：任何要求 `|gamma Q|>=q_0>0` 的 scale-neutral balanced-core
certificate 都不可能成立；actual multiplier必随 `(mu,Delta)->(0,0)` 二次消失。

## 4. Matched PNT core 被 multiplier extinguish

回到笔记 252--253 的 exact matched zeta model：

\[
 Y_m=2^m,qquad N_m\ge Y_m,qquad L_m=\log N_m.
\tag{24}
\]

令 `A_m` 为 prime source总质量，`B_m` 为 matched continuum source总质量，
`S_m=A_m+B_m`。定性 PNT与 Abel partial summation给

\[
 A_m-B_m=o(Y_m^{1-\sigma}),qquad
 S_m\asymp Y_m^{1-\sigma},qquad
 \mu_m\longrightarrow0.
\tag{25}
\]

另一方面，笔记 253-A 对任何 fixed nonresonant compact `K` 给

\[
 \sup_{t\in K}
 \left|W_{p,m}(t/m)-W_{c,m}(t/m)\right|
 =o(Y_m^{1-\sigma}).
\tag{26}
\]

所以

\[
 \sup_{t\in K}|\Delta_m(t/m)|\longrightarrow0.
\tag{27}
\]

### 推论 254-C（balanced-core multiplier extinction）[T/N]

在上述 hypotheses 下，并假设 `K` 有正 Lebesgue 测度，

\[
 \boxed{
 \sup_{t\in K}
 \left|\gamma_mQ_{M_m,\ell_m}
 (\widehat d_m(t/m))\right|\longrightarrow0.}
\tag{28}
\]

定义 raw Brownian diagonal measure

\[
 d\mathcal E_m^{\rm raw}(\xi)
 =\frac{W_{p,m}(\xi)^2+W_{c,m}(\xi)^2}
 {2\pi\xi^2}\,d\xi
\tag{29}
\]

以及 actual degree-two response diagonal

\[
 d\mathcal E_m^{\rm resp}
 =|\gamma_mQ_m(\widehat d_m)|^2
 d\mathcal E_m^{\rm raw}.
\tag{30}
\]

若 `K_m={t/m:t in K}`，则

\[
 \boxed{
 \mathcal E_m^{\rm resp}(K_m)
 =o\!\left(\mathcal E_m^{\rm raw}(K_m)\right).}
\tag{31}
\]

更精确地，充分大 `m` 时式 (20)逐点给

\[
 \frac{d\mathcal E_m^{\rm resp}}
 {d\mathcal E_m^{\rm raw}}
 \asymp
 \left(\mu_m^2+\Delta_m(\xi)^2\right)^2
 \quad(\xi\in K_m),
\tag{32}
\]

其中二侧常数完全由式 (20)给出。

#### 证明

式 (25) 的第一式是对 kernel `x^(-sigma)e^(-x/Y_m)` 作与笔记 253 相同的
Stieltjes partial summation；fixed lower endpoint只贡献 `O(1)`。matched continuum
在 `[Y_m/2,Y_m]` 上给 `S_m gg Y_m^(1-sigma)`，而完整 Abel integral给相反 upper，
故其余两式成立。式 (26) 除以 `S_m` 给式 (27)。于是式 (20) eventually uniform
适用，并给式 (28)、(32)。最后由式 (30)

\[
 \mathcal E_m^{\rm resp}(K_m)
 \le\sup_{K_m}|\gamma_mQ_m|^2
 \mathcal E_m^{\rm raw}(K_m),
\]

得到式 (31)。`square`

## 5. 这对 B1 ratio route 的含义

笔记 253-B 证明在 `K_m` 上

\[
 \frac{W_pW_c}{W_p^2+W_c^2}\longrightarrow\frac12.
\tag{33}
\]

但式 (32) 证明同一 core 的 actual energy weight并不 scale-neutral，而是额外乘上
prime--continuum discrepancy 的四次权

\[
 (\mu_m^2+\Delta_m^2)^2.
\tag{34}
\]

因此“ratio趋于 1”与“actual response energy tight”不是两个独立友好的事实：
前者正把 endogenous degree-two multiplier推向其二阶零点。有限尺度证书中对
`|Q(d-hat)|` 的 positive lower不能原样 cofinalize。

这还没有证明

\[
 \frac{\mathcal E_m^{\rm resp}(K_m)}
 {\mathcal E_m^{\rm resp}(\mathbb R)}\to0,
\tag{35}
\]

因为 denominator也可能以同阶或更快退化。把式 (31)误写成式 (35)会再次犯
finite-to-bulk量词错误。真正剩余的 arithmetic input 是 discrepancy-weighted energy
在频率上的相对分布。

### 定理 254-D（fixed physical-frequency multiplier escape）[T/N]

在式 (24) 的 matched schedule 下，对每个 fixed `T<infinity`，

\[
 \sup_{|\xi|\le T}
 \left(|\mu_m|+|\Delta_m(\xi)|\right)\longrightarrow0,
\tag{36}
\]

因而

\[
 \boxed{
 \sup_{|\xi|\le T}
 |\gamma_mQ_m(\widehat d_m(\xi))|\longrightarrow0.}
\tag{37}
\]

若 `T>0`，相应地

\[
 \mathcal E_m^{\rm resp}([-T,T])
 =o\!\left(\mathcal E_m^{\rm raw}([-T,T])\right).
\tag{38}
\]

#### 证明

定义 complex smoothed discrepancy

\[
 H_m(\xi)=
 \sum_{n\le N_m}\Lambda(n)n^{-\sigma-i\xi}e^{-n/Y_m}
 -\int_1^{N_m}x^{-\sigma-i\xi}e^{-x/Y_m}\,dx.
\]

对 `|xi|<=T`，其 kernel derivative满足

\[
 x|G'_{m,\xi}(x)|
 \le x^{-\sigma}e^{-x/Y_m}
 \left(\sigma+T+\frac{x}{Y_m}\right).
\]

把笔记 253 的 `epsilon--X_epsilon` 分割原样应用于这个 uniform majorant，得到
`sup_(|xi|<=T)|H_m(xi)|=o(Y_m^(1-sigma))`。又 `M_m=H_m(0)`，而 exact identity

\[
 W_{p,m}(\xi)-W_{c,m}(\xi)
 =M_m-\Re H_m(\xi),
\]

成立。这证明式 (36)。定理 254-B 给式 (37)，再用
式 (30) 与 supremum bound给式 (38)。`square`

定理 254-D 不证明 actual probability mass 已逃到无穷：若 total response energy
同时更快趋零，normalized mass 仍可能留在有限窗。其严格内容是所有 fixed physical
windows 都失去 scale-neutral multiplier lower；任何 nontrivial denominator lower
必须检查增长频带 `T_m->infinity`。

## 6. 有限诊断 [E]

`scripts/b1l_multiplier_degeneracy_audit.py` 对 `sigma=3/5,N=Y,t=1` 计算 exact
continuum integrals与 finite von Mangoldt sums：

| `m` | `mu_m` | `Delta_m(t/m)`, `t=1` | `|gamma Q|`, `t=1` | `Delta_m(1)` | `|gamma Q|`, `xi=1` |
|---:|---:|---:|---:|---:|---:|
| 4 | -0.103332 | -0.00234463 | 0.00728004 | -0.0234322 | 0.00573923 |
| 6 | -0.0427279 | -0.0000524787 | 0.00107958 | -0.00373541 | 0.000984092 |
| 8 | -0.0230248 | -0.000323294 | 0.000292052 | -0.00255056 | 0.000263757 |
| 10 | -0.0113908 | 0.0000422708 | 0.0000703070 | -0.00110263 | 0.0000633788 |
| 12 | -0.00610602 | 0.0000649761 | 0.0000200199 | -0.000207538 | 0.0000191348 |

该表只显示式 (28) 的有限前兆；推论 254-C 的证明不使用单调性或数值拟合。

## 7. 最小公理、删除与循环性审计

最小输入：

1. `[T]` even sign-pure source representation；作用是式 (2)--(3)；
2. `[T]` actual degree-two polynomial、`rho=S/3` 与 response scalar；作用是式
   (4)--(7)，不可替换为任意 multiplier；
3. `[T]` exact normalization by `S=A+B`；作用是揭示齐次消去；
4. `[R]` qualitative PNT；只在推论 254-C 中给 `mu_m,Delta_m->0`；
5. `[T]` matched endpoint与 nonresonant compact core；作用同笔记 253。

删除审计：

- 删除 actual polynomial而换成外生 bounded-below multiplier，二阶 extinction消失；
- 删除 `M/S->0`，式 (12) 显示 balanced symbol `Delta=0` 处 multiplier一般不为零；
- 删除 `Delta->0`，ratio core不再接近 polynomial的 balanced point；
- 删除 response normalization `S^-4`，齐次尺度账本错误；
- 把 raw energy capture直接当作 response energy capture，被式 (31)反驳；
- 把式 (31)升级成 total fraction (35)，缺少 denominator lower，证明在此明确停止；
- 把当前 two-channel measure称为完整 Gamma response，会越过笔记 244-B 已声明的
  sign-indefinite Archimedean gap。

非同义反复：式 (10) 是 actual degree-two polynomial 的新 normal form；式 (19) 的
positive-definite quadratic lower可被其他 polynomial反驳，并非“连续函数趋零”的改写。
障碍来自 endogenous multiplier的显式二阶零点，而不是把 desired energy escape作为
公理。

循环性审计：未使用 zeros、RH/GRH、RH-strength prime error、Weil positivity、谱酉性、
bounded negative index、四矩猜想或紧性完备化。PNT只证明 normalized discrepancies
趋零；它不提供式 (35) 的 denominator comparison。

## 8. 模型与论文接口

- Riemann zeta：式 (24)--(32) 直接适用于 exact matched sign-pure subsystem；
- Dedekind zeta：若 ideal PNT与同一 degree-two normalization成立，normal form保留；
- Dirichlet/automorphic L：complex source phases先破坏式 (2)，需 matrix-valued normal
  form，不能直接引用 254-C；
- 函数域：若使用同一个 degree-two polynomial，式 (10)--(20) 纯代数保留；PNT
  cofinal limit要换成 degree asymptotic；
- 其他 soft polynomials：退化阶由相应 divided difference在 balanced point的 Taylor
  jet决定，不能默认仍为二次；
- 论文归属：与笔记 242--253 同属 Vaughan--Brownian response论文，且应作为阻止
  finite good-arc certificate直接 cofinalize 的核心障碍节。

## 9. 下一最小引理 B1m [O]

正确的 cofinal capture不再是 unweighted ratio-core tightness，而是 actual
discrepancy-weighted问题：对某个 fixed nonresonant `K`，证明或反驳

\[
 \liminf_m
 \frac{\displaystyle
  \int_{K_m}q_\kappa(\mu_m,\Delta_m(\xi))^2
  (W_{p,m}^2+W_{c,m}^2)\frac{d\xi}{\xi^2}}
 {\displaystyle
  \int_{\mathbb R}q_\kappa(\mu_m,\Delta_m(\xi))^2
  (W_{p,m}^2+W_{c,m}^2)\frac{d\xi}{\xi^2}}>0.
\tag{39}
\]

下一轮先比较 low normalized core 与 escaping physical-frequency bands 的同一
`q^2` 权；必须给 denominator 的独立 lower。若 denominator由 `|xi| asymp1` 或更高
频率主导并使式 (36)趋零，则形成 actual-symbol energy-escape no-go；若 core与 total
同阶，则式 (33)恢复 uniform Schur gain。Gamma residual必须作为独立第三 channel
加入，不能用当前 sign-pure deletion原则暗中吸收。
