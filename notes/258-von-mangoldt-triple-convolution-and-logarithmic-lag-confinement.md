# 258. Von Mangoldt triple convolution 与 logarithmic lag confinement

日期：2026-09-04

分支：NCE-8 / 路线 B1；接口：B1p actual prime coefficients / mesoscopic
escape exclusion

状态：actual matched Abel sources 的 centered-kernel triple-convolution coefficient
ledger、weighted PNT tail primitive identity、exponential lag-tail bound，以及任意
polynomial accuracy 的 `O(log log Y)` lag-window response truncation为 [T]。由此严格排除
笔记 257 的 `sqrt(log Y)` coherent shifted-packet mechanism在真实 Abel sources 中出现，
为 [T/N]；但 absolute truncation error 尚无 actual response denominator lower，不能
升级为 normalized tilt tightness。Gamma residual仍独立，本文不声称 RH/GRH。

## 1. Actual one-sided sources

固定 `0<sigma<1`，置 `a=1-sigma`。令

\[
 Y_m=2^m,\qquad L_m=\log Y_m=m\log2,
 \qquad N_m\ge Y_m,\qquad U_m=\log N_m.
\tag{1}
\]

在 nonnegative lag half-line定义

\[
 d\alpha_m(\lambda)=
 \sum_{2\le n\le N_m}
 \Lambda(n)n^{-\sigma}e^{-n/Y_m}
 \delta_{\log n}(d\lambda),
\tag{2}
\]

\[
 d\beta_m(\lambda)=
 \mathbf1_{[0,U_m]}(\lambda)
 e^{a\lambda-e^\lambda/Y_m}\,d\lambda.
\tag{3}
\]

其 masses 为 `A_m,B_m`，并置
`S_m=A_m+B_m`、`mu_m=(A_m-B_m)/S_m`。令
`s_lambda=(delta_lambda+delta_(-lambda))/2`，并定义 zero-mass centered atom

\[
 k_\lambda=s_\lambda-\delta_0.
\tag{4}
\]

笔记 255 的 even centered measures可精确写成

\[
 p_m=\int k_\lambda\,d\alpha_m(\lambda),\qquad
 c_m=-\int k_\lambda\,d\beta_m(\lambda).
\tag{5}
\]

以下统一记

\[
 D_m^{\rm raw}=\|F_{p_m}\|_2^2+\|F_{c_m}\|_2^2.
\]

若 `mathfrak d_m:=alpha_m-beta_m` 表示 one-sided signed discrepancy measure，则

\[
 r_m:=p_m+c_m=\int k_\lambda\,d\mathfrak d_m(\lambda).
\tag{6}
\]

这里 `mathfrak d_m` 与笔记 254 的 uncentered even divisor `d` 不同；本笔记只用它
表示 positive-half prime minus continuum coefficient measure。

## 2. Triple kernel 的全部系数

对 `lambda=(lambda_1,lambda_2,lambda_3)` 定义

\[
 K_\lambda=k_{\lambda_1}*k_{\lambda_2}*k_{\lambda_3}.
\tag{7}
\]

### 定理 258-A（exact centered triple-coefficient ledger）[T]

逐 measure 精确有

\[
\begin{aligned}
 K_\lambda={}&s_{\lambda_1}*s_{\lambda_2}*s_{\lambda_3}
 -s_{\lambda_1}*s_{\lambda_2}
 -s_{\lambda_1}*s_{\lambda_3}
 -s_{\lambda_2}*s_{\lambda_3}\\
 &+s_{\lambda_1}+s_{\lambda_2}+s_{\lambda_3}-\delta_0,
\end{aligned}
\tag{8}
\]

其中

\[
 s_x*s_y*s_z=\frac18
 \sum_{\epsilon\in\{-1,1\}^3}
 \delta_{\epsilon_1x+\epsilon_2y+\epsilon_3z},
 \qquad
 s_x*s_y=\frac14
 \sum_{\epsilon\in\{-1,1\}^2}
 \delta_{\epsilon_1x+\epsilon_2y}.
\tag{9}
\]

actual triple responses 因而是

\[
 \boxed{
 r_m*r_m*p_m
 =\iiint K_\lambda\,
 d\mathfrak d_m(\lambda_1)d\mathfrak d_m(\lambda_2)
 d\alpha_m(\lambda_3),}
\tag{10}
\]

\[
 \boxed{
 r_m*r_m*c_m
 =-\iiint K_\lambda\,
 d\mathfrak d_m(\lambda_1)d\mathfrak d_m(\lambda_2)
 d\beta_m(\lambda_3).}
\tag{11}
\]

#### 证明

式 (8) 是 `(s_1-delta_0)*(s_2-delta_0)*(s_3-delta_0)` 的逐项展开；式 (9)
来自三个 independent signs 的 convolution。把式 (5)--(7)代入并用 Fubini，即得
式 (10)--(11)。全部 measures compactly supported，故没有交换积分问题。`square`

定义 six-lag Brownian kernel

\[
 \mathcal B(\lambda,\mu)
 :=\langle F_{K_\lambda},F_{K_\mu}\rangle
 =-\frac12\iint_{\mathbb R^2}|x-y|\,
 dK_\lambda(x)dK_\mu(y).
\tag{12}
\]

第二个等号是 zero-mass Brownian distance identity。若

\[
 d\Gamma_{p,m}(\lambda)
 =d\mathfrak d_m(\lambda_1)d\mathfrak d_m(\lambda_2)d\alpha_m(\lambda_3),
\]

并以 `beta_m` 替换最后一项定义 `Gamma_(c,m)`，则笔记 257-A 变成完全显式的

\[
\begin{aligned}
 S_m^4D_m^{\rm raw}J_{4,m}
 ={}&\iint\mathcal B(\lambda,\mu)
 d\Gamma_{p,m}(\lambda)d\Gamma_{p,m}(\mu)\\
 &+\iint\mathcal B(\lambda,\mu)
 d\Gamma_{c,m}(\lambda)d\Gamma_{c,m}(\mu).
\end{aligned}
\tag{13}
\]

式 (13) 保留两个 discrepancy factors 的 signs；对 `mathfrak d_m` 逐项取 absolute
value 会删除真正需要的 prime--continuum cancellation。

## 3. Centered discrepancy primitive 是 weighted PNT tail

定义 prime、continuum 与 signed tail functions（endpoint convention只影响零测集）

\[
\begin{aligned}
 P_m(u)&=\alpha_m((u,U_m]),\\
 C_m(u)&=\beta_m((u,U_m]),\\
 R_m(u)&=P_m(u)-C_m(u),
 \qquad 0\le u\le U_m.
\end{aligned}
\tag{14}
\]

### 定理 258-B（exact weighted-PNT primitive identity）[T]

对 `x>0`，几乎处处有

\[
 F_{p_m}(x)=-\frac12P_m(x),\qquad
 F_{c_m}(x)=\frac12C_m(x),\qquad
 F_{r_m}(x)=-\frac12R_m(x).
\tag{15}
\]

由 evenness，负半轴给相同平方，故

\[
 \boxed{
 \|F_{r_m}\|_2^2=\frac12\int_0^{U_m}|R_m(u)|^2du,}
\tag{16}
\]

以及

\[
 D_m^{\rm raw}
 =\frac12\int_0^{U_m}(P_m(u)^2+C_m(u)^2)du.
\tag{17}
\]

#### 证明

在正半轴，even source 的全部 negative mass先贡献其总质量的一半。越过 `0` 后，
center atom再减去相应总质量；因此 centered cumulative等于负的一半 positive tail。
对 `c_m` 的 overall minus sign给相反号。平方后在两个半轴积分，得到式 (16)--(17)。
`square`

结合笔记 257-B，式

\[
 \int_0^{U_m}|R_m(u)|^2du
 =O(\mu_m^4D_m^{\rm raw})
\tag{18}
\]

是足以推出 B1o-q4 的明确 weighted-PNT tail-square input；它比 B1o-q4 本身更强，
当前保持 [O]，不能从 `psi(x)=x+o(x)` 推出。

## 4. Actual Abel source 的 exponential lag tails

令 source tail mass

\[
 \mathcal T_m(d)=
 \alpha_m(\{|\lambda-L_m|\ge d\})
 +\beta_m(\{|\lambda-L_m|\ge d\}).
\tag{19}
\]

### 定理 258-C（uniform exponential/superexponential lag envelope）[T]

存在只依赖 `sigma` 的 `C_sigma<infinity`，使对充分大 `m` 及
`1<=d<=L_m-log2`，

\[
 \boxed{
 \frac{\mathcal T_m(d)}{S_m}
 \le C_\sigma\left[
 L_m e^{-ad}+(L_m+e^d)e^{-e^d/2}
 \right].}
\tag{20}
\]

该 bound 对所有 cutoff schedules `N_m>=Y_m` 一致。

#### 证明

低 lag 区对应 `n<=Y_me^(-d)`。由 `Lambda(n)<=log n` 与积分比较，若右端点至少
为 `2`，

\[
 \sum_{n\le Y_me^{-d}}\Lambda(n)n^{-\sigma}e^{-n/Y_m}
 \le C_\sigma(Y_me^{-d})^aL_m.
\tag{21}
\]

若右端点小于 `2`，左端为零。continuum low tail则至多
`a^(-1)Y_m^ae^(-ad)`。

高 lag 区对应 `n>=Y_me^d`。把 integers 分成 dyadic intervals
`[2^jY_me^d,2^(j+1)Y_me^d)`，仍用 `Lambda<=log`；指数权给

\[
 \sum_{n\ge Y_me^d}\Lambda(n)n^{-\sigma}e^{-n/Y_m}
 \le C_\sigma Y_m^a(L_m+e^d)e^{-e^d/2}.
\tag{22}
\]

把上限延到 infinity只会增大该 positive sum，因此 bound 与 `N_m/Y_m` 无关。
变量代换 `x=Y_mu` 对 continuum high tail给同型且更小的 incomplete-Gamma bound。
最后 matched continuum 在 `[Y_m/2,Y_m]` 上的正质量直接给
`S_m>=B_m>=c_sigma Y_m^a`；这里不需要 PNT。除后得到式 (20)。`square`

### 推论 258-D（polynomial mass confinement）[T]

对每个 fixed `K>0`，取

\[
 d_m^{(K)}=\frac{K+2}{a}\log L_m.
\tag{23}
\]

则

\[
 \boxed{
 \mathcal T_m(d_m^{(K)})/S_m=O_{\sigma,K}(L_m^{-K-1}).}
\tag{24}
\]

特别地，任何占 source 总质量至少 `L_m^(-K)` 的 coherent tail packet都不可能位于
`|lambda-L_m|>=d_m^(K)`。

#### 证明

式 (20) 第一项为
`L_m exp(-(K+2)logL_m)=L_m^(-K-1)`；第二项比任意 `L_m` 的负幂更小。
`square`

## 5. Triple response 的 logarithmic-window truncation

令 `I_m^(K)=[L_m-d_m^(K),L_m+d_m^(K)]`，并只截断两个 discrepancy factors：

\[
 r_m^{(K)}=\int_{I_m^{(K)}}k_\lambda\,d\mathfrak d_m(\lambda).
\tag{25}
\]

定义

\[
 \eta_{p,m}=r_m*r_m*p_m,\quad
 \eta_{c,m}=r_m*r_m*c_m,
\]

及

\[
 \eta_{p,m}^{(K)}=r_m^{(K)}*r_m^{(K)}*p_m,\quad
 \eta_{c,m}^{(K)}=r_m^{(K)}*r_m^{(K)}*c_m.
\tag{26}
\]

### 定理 258-E（arbitrary-power central-lag response approximation）[T]

对每个 fixed `K>0`，

\[
 \boxed{
 \frac{
 \left(\|F_{\eta_{p,m}-\eta_{p,m}^{(K)}}\|_2^2
 +\|F_{\eta_{c,m}-\eta_{c,m}^{(K)}}\|_2^2\right)^{1/2}}
 {S_m^2\sqrt{D_m^{\rm raw}}}
 =O_{\sigma,K}(L_m^{-K-1}).}
\tag{27}
\]

若以 `J_(4,m)^(K)` 表示笔记 257-(4) 中把 `r_m` 换成 `r_m^(K)` 所得的 normalized
quartic energy，则

\[
 \boxed{
 \left|\sqrt{J_{4,m}}-\sqrt{J_{4,m}^{(K)}}\right|
 =O_{\sigma,K}(L_m^{-K-1}).}
\tag{28}
\]

#### 证明

记 `e_m=r_m-r_m^(K)`。因为 `||k_lambda||_(TV)<=2`，推论 258-D 给

\[
 \|e_m\|_{\rm TV}
 \le2\mathcal T_m(d_m^{(K)})
 =O(S_mL_m^{-K-1}).
\tag{29}
\]

又 `||r_m||_(TV)<=2S_m`，且 `||r_m^(K)||_(TV)<=||r_m||_(TV)+||e_m||_(TV)`。
利用

\[
 r_m*r_m-r_m^{(K)}*r_m^{(K)}
 =e_m*(r_m+r_m^{(K)}),
\]

并把 primitive放在最后的 `p_m` 或 `c_m` factor，Young inequality 给

\[
 \|F_{\eta_{p,m}-\eta_{p,m}^{(K)}}\|_2
 \le\|F_{p_m}\|_2\|e_m\|_{\rm TV}
 (\|r_m\|_{\rm TV}+\|r_m^{(K)}\|_{\rm TV}),
\tag{30}
\]

对 `c_m` 同理。平方相加并用式 (17)，得到式 (27)。最后在 Hilbert direct sum
`L^2 direct-sum L^2` 中应用 reverse triangle inequality，再除以
`S_m^2sqrt(D_raw)`，得到式 (28)。`square`

## 6. 对 mesoscopic escape 的严格含义 [T/N]

笔记 257-F 的 positive-source obstruction把相对质量 `epsilon_m=m^(-1/8)` 搬到
lag `L_m+sqrt(L_m)`。对 actual Abel sources，取任意 fixed `K>1/8`；因为
`sqrt(L_m)>>d_m^(K)` 而 `epsilon_m>>L_m^(-K-1)`，推论 258-D 与该 packet要求矛盾。
所以那一个具体 `t asymp sqrt(m)` escape mechanism不能嵌入真实 prime/continuum
Abel tails。

更一般地，任意 polynomial-size coherent tail packet 都被限制到

\[
 |\lambda-L_m|=O_{\sigma,K}(\log L_m).
\tag{31}
\]

若把单一 lag separation `d` 转为其最敏感 physical frequency `xi asymp1/d`，则剩余
polynomial packet mechanism只能在

\[
 |t|=m|\xi|\gtrsim_{\sigma,K}\frac{m}{\log L_m}
\tag{32}
\]

的 normalized frequencies出现。式 (32) 只是 packet geometry；它不是 `Pi_m` 的
tail lower，也没有排除 central window 内许多 signed coefficients 的 collective
oscillation。

同样，式 (28) 是 absolute response-amplitude approximation。若 actual denominator
比 `L_m^(-2K-2)` 更快消失，该误差仍可能主导 normalized probability；因此不能从
式 (28) 直接宣称 tilted tightness。这是本轮 finite-to-bulk 审计的停止位置。

## 7. 最小输入、删除与循环性审计

最小输入：

1. `[T]` exact von Mangoldt/continuum Abel coefficients；给式 (2)--(6)；
2. `[T]` centered atom algebra与 Brownian kernel；给式 (8)--(13)；
3. `[T]` `Lambda(n)<=log n` 与 exponential Abel cutoff；给 lag-tail envelope；
4. `[T]` matched continuum bulk lower `B_m>>Y_m^a`；给 normalized tail bound，
   不需要 PNT；
5. `[T]` Young inequality与 primitive-convolution exchange；给式 (27)--(28)。

删除审计：

- 删除 exponential Abel factor，upper lag 的 superexponential confinement消失；
- 删除 elementary coefficient bound，prime tail不能由 positive majorant控制；
- 删除 matched continuum bulk lower，只剩 unnormalized tail bound，不能除以 `S_m`；
- 对 `mathfrak d_m` 展开后逐项取绝对值，会丢掉式 (13) 的两个 signed discrepancy
  channels；
- 把 absolute approximation (28) 当 relative capture，缺少 denominator lower；
- 把 central window confinement当成 fixed-frequency tightness，忽略式 (32) 的增长频带；
- 把 two-channel result并入 Gamma，缺少第三通道 block bridge。

非同义反复：式 (20) 是由 actual Abel coefficient envelope导出的 source-tail theorem，
并非把 desired response tightness写入假设；式 (27) 再通过 explicit convolution
stability把它传给 actual triple response。笔记 257 的 soft positive-source family不满足
式 (20)，因此确被新增的 arithmetic/weight structure排除。

循环性审计：全部 [T/N] 只用 `Lambda<=log`、positive Abel tails、matched continuum
bulk lower、有限 signed convolution algebra与 Brownian Plancherel；连定性 PNT也不需要，
更不使用 zeros、RH/GRH、PNT平方根误差、Weil
positivity、谱酉性、bounded negative index、四矩猜想或紧性完备化。

## 8. 模型范围与下一最小引理 B1q

- Riemann zeta：式 (1)--(30) 直接适用于 matched sign-pure subsystem；
- Dedekind zeta：用 ideal von Mangoldt bound与 prime-ideal theorem可得到 degree-dependent
  analogue；
- Dirichlet/automorphic L：absolute coefficient majorant可能保留 tail confinement，但
  triple ledger需 matrix/phase-valued版本；
- 函数域：degree cutoff通常给更强的 compact shell confinement，可作为正向基准；
- 一般 spectral models：只有具 exponential lag envelope 的 source class才能引用
  258-C--E；笔记 257 说明 relative concentration本身不够；
- 论文归属：与笔记 242--257 同属 Vaughan--Brownian response论文，作为 actual
  arithmetic coefficients 与 soft no-go 之间的第一道 bridge。

B1p 已完成 coefficient expansion并闭合 far-lag part。下一最小引理 **B1q** 是在
central window `|lambda-L_m|<=C logL_m` 内，把式 (13) 化成 short multiplicative
interval中的 weighted von Mangoldt discrepancy Gram，并证明 response-specific
signed bound；或者证明该 central Gram仍可产生 `t>=m/logL_m` 的 actual escape。
不得退回全 TV、任意系数 Bessel bound或仅 fixed-frequency PNT。
