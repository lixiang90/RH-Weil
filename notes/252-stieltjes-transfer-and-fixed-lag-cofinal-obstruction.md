# 252. Stieltjes transfer 与 fixed-lag cofinal obstruction

日期：2026-09-04

分支：NCE-8 / 路线 B1；接口：B1j cofinal schedule / normalized
prime--continuum ratio

状态：prime symbol 与 matched continuum symbol之间的 exact `d(psi-x)` Stieltjes
分解为 [T]；固定 continuum lag endpoint不能支撑任意 cofinal dyadic ratio core，以及
`L_m/log Y_m` 的必要下界为 [T/N]，其唯一外部输入是无条件素数定理 [R]。有限数值
回归为 [E]。本笔记不更新 PDF，不声称 RH/GRH、零点比例改进或完整 Weil 正性。

## 1. 必须加入 cofinal schedule 的漏失参数

前两尺度使用

\[
 (Y,N,L)=(8,10,2),\qquad(16,15,2),
\tag{1}
\]

其中 `L` 是 continuum lag endpoint。笔记 251 只在 cofinal tuple 中列出
`(Y_m,N_m,J_m,h_m,Xi_m)`，遗漏了 `L_m`。这不是无害记号：prime lags延伸到
`log N_m`，而 continuum lags只延伸到 `L_m`。本笔记证明任何 `N_m>=Y_m` 的
cofinal Abel schedule若保持 `L_m` 有界，固定 normalized ratio core必然消失。

正确的 schedule至少应写为

\[
 (Y_m,N_m,L_m,J_m,h_m,\Xi_m).
\tag{2}
\]

## 2. Prime 与 continuum symbols

固定 `0<sigma<1`。对 `Y>0,N>=2` 定义

\[
 F_{Y,\xi}(x)
 =x^{-\sigma}e^{-x/Y}
  \bigl(1-\cos(\xi\log x)\bigr),
\qquad x\ge1,
\tag{3}
\]

以及 finite prime symbol

\[
 P_{Y,N}(\xi)
 =\sum_{2\le n\le N}\Lambda(n)F_{Y,\xi}(n).
\tag{4}
\]

lag endpoint `L` 对应的 exact continuum symbol为

\[
 C_{Y,L}(\xi)
 =\int_0^L e^{(1-\sigma)\lambda-e^\lambda/Y}
   \bigl(1-\cos(\xi\lambda)\bigr)d\lambda.
\tag{5}
\]

令

\[
 \psi(x)=\sum_{n\le x}\Lambda(n),
 \qquad E(x)=\psi(x)-x.
\tag{6}
\]

## 3. Exact Stieltjes discrepancy identity

### 定理 252-A（matched arithmetic--continuum decomposition）[T]

对任意上述参数，

\[
 P_{Y,N}(\xi)-\int_1^N F_{Y,\xi}(x)dx
 =F_{Y,\xi}(N)E(N)
  -\int_1^N E(x)F'_{Y,\xi}(x)dx,
\tag{7}
\]

其中

\[
\begin{aligned}
 F'_{Y,\xi}(x)
 ={}&x^{-\sigma}e^{-x/Y}\Bigg[
 \frac{\xi}{x}\sin(\xi\log x)\\
 &-\left(\frac{\sigma}{x}+\frac1Y\right)
 (1-\cos(\xi\log x))\Bigg].
\end{aligned}
\tag{8}
\]

而变量代换 `x=e^lambda` 精确给出

\[
 C_{Y,L}(\xi)=\int_1^{e^L}F_{Y,\xi}(x)dx.
\tag{9}
\]

若 `C^(J)_(Y,L)` 是任意 finite continuum quadrature，并定义

\[
 Q_{Y,L,J}(\xi)=C_{Y,L}(\xi)-C^{(J)}_{Y,L}(\xi),
\tag{10}
\]

则

\[
\boxed{
 P_{Y,N}-C^{(J)}_{Y,L}
 =R_{Y,N}+\int_{e^L}^{N}F_{Y,\xi}(x)dx+Q_{Y,L,J},}
\tag{11}
\]

其中积分采用 oriented convention，且

\[
 R_{Y,N}=F_{Y,\xi}(N)E(N)-\int_1^NE(x)F'_{Y,\xi}(x)dx.
\tag{12}
\]

#### 证明

式 (4) 是 Stieltjes integral `int_(1-)^N F dpsi`。因 `F(1)=0`，对
`dE=dpsi-dx` 分部积分即得式 (7)；直接微分给式 (8)。式 (9) 中
`d lambda=dx/x`，而
`e^((1-sigma)lambda)d lambda=x^(-sigma)dx`。最后加减
`int_1^N F`、`C_(Y,L)` 与 `C^(J)_(Y,L)` 得式 (11)。`square`

### 推论 252-B（dyadic transfer ledger）[T]

令 `Y_m=2^m, xi=t/m`，并允许 `N_m,L_m,J_m` 随 `m` 变化。则

\[
\begin{aligned}
 &(P_{m+1}-C^{(J_{m+1})}_{m+1})
 -(P_m-C^{(J_m)}_m)\\
 &=(R_{m+1}-R_m)+(H_{m+1}-H_m)+(Q_{m+1}-Q_m),
\end{aligned}
\tag{13}
\]

其中 `H_m=int_(e^(L_m))^(N_m) F_(2^m,t/m)`。因此：

- 唯一 arithmetic term是显式 `E=psi-x` response `R_m`；
- prime cutoff与 continuum endpoint mismatch完全在 `H_m`；
- finite continuum discretization完全在 `Q_m`；
- Abel scale及 phase rescaling已显式包含于相邻 kernels。

若预注册 `L_m=log N_m` 且使用 exact continuum，则 `H_m=Q_m=0`，
prime--continuum mismatch恰为 `R_m`，没有隐藏的 compactness或 Weil positivity。

## 4. General continuum moment bound

令 `nu_m` 是支撑于 `[0,L_m]` 的任意有限正测度，定义

\[
 C_m(t)=\int_0^{L_m}
 \left(1-\cos\frac{t\lambda}{m}\right)d\nu_m(\lambda),
\qquad
 M_{2,m}=\int_0^{L_m}\lambda^2d\nu_m(\lambda).
\tag{14}
\]

由 `1-cos u<=u^2/2`，

\[
 0\le C_m(t)\le\frac{t^2}{2m^2}M_{2,m}.
\tag{15}
\]

式 (15) 对 exact continuum与所有 positive cell quadratures同时成立；它不要求
cell midpoint approximation已经收敛。

## 5. Fixed-lag endpoint no-go

素数定理给

\[
 \psi(x)=x+o(x)
\tag{16}
\]

[R]；这里采用 Davenport, *Multiplicative Number Theory*, 3rd ed.，见来源 45。

### 定理 252-C（pointwise cofinal ratio escape）[T/N]

设

\[
 Y_m=2^m,\qquad N_m\ge Y_m,
\tag{17}
\]

并令 `P_m(t)=P_(Y_m,N_m)(t/m)`。对每个固定 `t!=0`：

1. 若 `t log2` 不是 `2pi` 的整数倍，则存在 `c_t>0`，使

   \[
   P_m(t)\ge c_tY_m^{1-\sigma}
   \tag{18}
   \]

   对所有充分大的 `m` 成立；

2. 若 `t log2 in 2pi Z`，则存在 `c_t>0`，使

   \[
   P_m(t)\ge c_t\frac{Y_m^{1-\sigma}}{m^2}.
   \tag{19}
   \]

因此若 `sup_m M_(2,m)<infinity`，则对任意 `B<infinity`，最终都有

\[
 P_m(t)>B C_m(t).
\tag{20}
\]

特别地，任何固定正长度 normalized interval都不可能在所有充分大 `m` 上逐点属于
一个 fixed ratio band `[a,B]`。

#### 证明

若 `A=t log2 notin 2pi Z`，则对 `Y_m/2<=n<=Y_m`，

\[
 \frac{t\log n}{m}=A+\frac{t}{m}\log(n/Y_m)
\tag{21}
\]

一致趋于 `A`，所以 `1-cos(t log n/m)>=c'_t>0`。又
`n^(-sigma)>=Y_m^(-sigma)`、`e^(-n/Y_m)>=e^(-1)`，而式 (16) 给

\[
 \sum_{Y_m/2<n\le Y_m}\Lambda(n)=Y_m/2+o(Y_m).
\tag{22}
\]

这证明式 (18)。

若 `A=2pi k` 且 `t!=0`，限制到 `Y_m/2<=n<=3Y_m/4`。此时

\[
 \left|\frac{t}{m}\log(n/Y_m)\right|
 \in\left[
 \frac{|t|\log(4/3)}m,\frac{|t|\log2}m
 \right].
\tag{23}
\]

充分大时 `|u|<=1`，故 `1-cos u>=u^2/4`。再由 PNT 得该 interval上的
Mangoldt mass为 `Y_m/4+o(Y_m)`，证明式 (19)。式 (15) 与有界 `M_(2,m)`
随即给式 (20)。任一正长度 interval含某个 `t!=0`，所以不能整体永久留在 ratio
band。这里要求正长度；单点集 `{0}` 不在该结论的量词内。`square`

## 6. Quantitative moment 与 endpoint necessity

### 定理 252-D（continuum second-moment tax）[T/N]

设 `K` 是固定正长度 normalized interval。若存在 `B<infinity`，使充分大 `m` 对所有
`t in K` 都有

\[
 P_m(t)\le B C_m(t),
\tag{24}
\]

则可选一个 `t_0 in K` 满足 `t_0 log2 notin2pi Z`，并有

\[
 \boxed{M_{2,m}\ge c_{K,B}m^2Y_m^{1-\sigma}.}
\tag{25}
\]

#### 证明

resonant points组成离散集，所以 `K` 含 nonresonant `t_0`。把式 (18)、(24)与
(15)串联：

\[
 c_{t_0}Y_m^{1-\sigma}
 \le P_m(t_0)\le B C_m(t_0)
 \le\frac{Bt_0^2}{2m^2}M_{2,m}.
\tag{26}
\]

整理即得式 (25)。`square`

对标准 exact continuum measure

\[
 d\nu_m(\lambda)=
 e^{(1-\sigma)\lambda-e^\lambda/Y_m}d\lambda
 \quad(0\le\lambda\le L_m),
\tag{27}
\]

有

\[
 M_{2,m}\le
 \int_0^{L_m}\lambda^2e^{(1-\sigma)\lambda}d\lambda
 \le\frac{L_m^2}{1-\sigma}e^{(1-\sigma)L_m}.
\tag{28}
\]

### 推论 252-E（lag endpoint must track `log Y`）[T/N]

在定理 252-D 的 hypotheses与标准 continuum (27) 下，

\[
 \boxed{\liminf_{m\to\infty}\frac{L_m}{\log Y_m}\ge1.}
\tag{29}
\]

#### 证明

若某个 `epsilon>0` 与无限子列满足 `L_m<=(1-epsilon)log Y_m`，则式 (28) 为

\[
 M_{2,m}=O\bigl((\log Y_m)^2
 Y_m^{(1-\sigma)(1-\epsilon)}\bigr),
\tag{30}
\]

而式 (25) 因 `m=(log Y_m)/(log2)` 要求
`M_(2,m)>=c(log Y_m)^2Y_m^(1-sigma)`，矛盾。`square`

推论 252-E 比“`L_m` 不能固定”更强：任何 first-order 小于 `log Y_m` 的 endpoint
都不够。自然 matched choice `L_m=log N_m` 因而不是方便性假设，而是正确数量级的
必要条件。

## 7. 有限回归与状态纪律

`scripts/b1j_stieltjes_fixed_lag_audit.py` 在
`(Y,N,m,t)=(16,15,4,1.375)` 检查式 (7)、(9)，误差分别约
`4.86e-63`、`3.89e-62`。这些只是高精度回归；定理 252-A 的证明不依赖数值容差。

固定 `L=2,N=Y,sigma=3/5` 的诊断为 [E]：

| `Y` | ratio at `t=1` | ratio at resonant `t=2pi/log2` |
|---:|---:|---:|
| 16 | 2.4162 | 1.0780 |
| 64 | 11.4868 | 2.5494 |
| 256 | 42.1950 | 6.7379 |
| 1024 | 133.8125 | 16.8048 |
| 4096 | 375.8280 | 39.0185 |

表只用于显示定理 252-C 的两个相位 regime；它不升级为渐近证明。

## 8. 删除、非同义反复与循环性审计

删除审计：

- 删除 `x=e^lambda` 的 Jacobian，continuum density会错误地多一个 `x` 次幂；
- 删除 endpoint mismatch `H_m`，固定 `L` 与增长 `N` 会被伪装成 arithmetic
  discrepancy；
- 删除 quadrature error `Q_m`，finite cells不能替代 exact continuum；
- 删除 PNT，只剩 exact identity，不能推出 cofinal lower (18)--(19)；
- 删除 positivity of `nu_m`，式 (15)不成立；
- 删除 second-moment growth，fixed-lag no-go不能转成 endpoint necessity；
- 把 `N_m>=Y_m` 偷换成当前两个 finite cutoffs的事实，量词错误；定理 252-C只针对
  明确的 cofinal schedules。

非同义反复审计：公理中没有包含 ratio divergence或 `L_m/logY_m>=1`；两者来自
PNT interval mass、phase two-case lower及 continuum moment upper。若 prime coefficients
不是 von Mangoldt weights，或 continuum second moment按式 (25)增长，no-go可失效。

循环性审计：PNT是无条件定理，不使用 RH；本证明没有调用 zero-free region的定量
误差、Mertens平方根界、Weil positivity、谱酉性或 bounded negative index。式 (11)
把唯一进一步所需的 arithmetic input明确写成 `E=psi-x` response，而不是用紧性产生。

## 9. 模型范围

- Riemann zeta：式 (3)--(12)直接适用，推论 252-E排除 fixed-lag cofinalization；
- Dedekind zeta：将 `psi` 换成 ideal von Mangoldt summatory function；需相应 ideal PNT
  才能复制 no-go；
- Dirichlet/automorphic L：coefficients带复相位，prime lower positivity失效；exact
  Stieltjes identity保留，但定理 252-C不能直接引用；
- 函数域：sum/integral variable离散化，endpoint matching对应 degree cutoff；可建立
  analogous finite identity；
- 本结果仍属显式公式型 Weil response，不建立上同调型 polarization bridge。

## 10. B1k 问题及其后续闭合 [T]

B1j 已关闭 fixed `L` 路线，并确定 natural cofinal normalization

\[
 Y_m=2^m,\qquad L_m=\log N_m,
\tag{31}
\]

或至少 `L_m=(1-o(1))logY_m`。本笔记提出的下一最小引理 B1k 不计算第三 finite point，而是在
一个避开 `t log2 in2pi Z` 的 compact normalized subcore上证明：

\[
 \sup_{t\in K}
 \frac{|R_{Y_m,N_m}(t/m)|}{C_{Y_m,\log N_m}(t/m)}=o(1)
\tag{32}
\]

所需的最弱 unconditional `psi-x` 输入，并把 finite quadrature、frequency cutoff与
degree-two multiplier的 response-density normalization分别加入。若普通 PNT已足以证明
(32)，下一障碍将唯一落在 response energy不能由该 compact core捕获；若不够，则式
(12)明确给出所需 smoothed discrepancy norm。无论哪种情况，都不得恢复 fixed `L=2`
或用更多 finite samples替代 cofinal proof。

后续：笔记 253 已证明，在 matched endpoint 与任何 fixed nonresonant compact core
上，普通 qualitative PNT 足以给式 (32) [T]，且 scalar Schur factor一致趋于 `1/2`。
因此 B1k 已关闭；当前 B1l 只剩 actual Brownian/Gamma response-energy capture，或其
严格 energy-escape obstruction。
