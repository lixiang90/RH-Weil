# 原 mixed 目标不能由独立边际预算推出：一个自包含 sharpness 引理

2026-10-10。纯有限族不等式；不是 Hecke 角色族，不是实际零点或算术矩的反例。
它说明必须取得新的原算术相关性，不能把现有独立 upper 相乘后登记 saving。

## 引理

所有指数均以同一个 row 基数 U 计；在物理探测器中 `U=Z^d`。
`rLong` 是 long inverse polynomial 的长度 `D_long=U^rLong`，
**不是**以 Z 计的物理总槽长 `eStar≈0.1668385889863`。

固定 `R in (0,1)`、`delta>0`、`rLong>0`。给每个足够大的实数 U 一个有限集合
E_U 及两个复值函数 M_U、P_U。以下四个预算本身不蕴含任何固定 chi>0 的
mixed saving：

\[
\#E_U\le U^R,
\qquad \sup_{u\in E_U}|M_U(u)|^2\le U^{\delta r_L},
\]
\[
\sum_{u\in E_U}|P_U(u)|^2\le U,
\qquad \sum_{u\in E_U}|M_U(u)|^2\le U^{R+\delta r_L}.
\tag{1}
\]

具体而言，有一组满足全部 (1)、常数均为 1 的有限族，使

\[
\sum_{u\in E_U}|M_U(u)P_U(u)|^2
\ge \tfrac12 U^{1+\delta r_L}.
\tag{2}
\]

所以不可能从 (1) 推出对所有这些有限族一致成立的

\[
\sum_{E_U}|M_UP_U|^2\le C U^{1+\delta r_L-\chi}
\tag{3}
\]

其中 chi>0、C有限并且独立于U。

**证明。** 令 `N=floor(U^R)`，当 `U^R>=2` 时，
`U^R/2 <= N <= U^R`。取 `E_U={1,...,N}`，在全部行上定义

\[
M_U(u)=U^{\delta r_L/2},\qquad
P_U(u)=U^{(1-R)/2}.
\]

它们是非负实数，也可视为复数。逐项计算给

\[
\sup |M_U|^2=U^{\delta r_L},\quad
\sum |M_U|^2=N U^{\delta r_L}\le U^{R+\delta r_L},
\]
\[
\sum |P_U|^2=N U^{1-R}\le U,
\quad
\sum |M_UP_U|^2=N U^{1-R+\delta r_L}
\ge\tfrac12 U^{1+\delta r_L}.
\]

若 (3) 成立，则 `U^chi<=2C` 对所有大U成立，矛盾。证毕。

## 与真实临界预算的准确关系

原 normalized 列是

\[
M_{r_L}(u)=U^{-r_L/2}\sum_n\mu(n)\psi_u(n)W_L(q_n/U^{r_L}),
\quad
S_m(u)=U^{-m/2}\sum_n\psi_u(n)W_S(q_n/U^m).
\]

selected physical Q 的每槽 norm scale 为 `P_i=Z^ell_i=U^w_i`，
并含对应 `P_i^(-1/2)` 归一化；其总 U-length 是 z，spike 为 `U^(qz)`。
以下的 scalar budgets 与这些 normalized 列的指数对应，未拿 raw sums
替换 normalized sums。toy 中的函数仅以 M_U/P_U 命名，并不宣称有这些
原算术系数表示。

现有原路线的临界点有 `R=2/3`，令 `alpha=5/6` 且

\[
1/3<\delta<1/2,\qquad
r_L=\frac{3}{5-6\delta}=\frac{1}{2(\alpha-\delta)}\in(1,3/2).
\]

于是精确有

\[
R=1-\alpha+(\alpha-\delta)r_L,
\qquad R+\delta r_L=\frac{1+5r_L}{6}.
\tag{4}
\]

在三次临界点，`deltaStar≈0.388583354266`、
`rLong=tStar≈1.1242271467861`，两边指数均约 `1.1035226223218`。
物理 total slot `eStar≈0.1668385889863` 不参与这个等式。
因此引理中的最后一个预算正好具有既有 sixth-power amplified inverse
二阶指数，未遗漏一个已经可由该独立合同获得的 saving。
真实 plain 目标是 `P=S_short²*Q_selected`。其临界 spike 关系为

\[
2\delta m+2qz=1-R.
\tag{5}
\]

只要非负 m、q、z 满足 (5)，有限模型还可精确拆成
`S_U=U^(delta*m/2)`、`Q_U=U^(q*z)`，令 `P_U=S_U² Q_U`。
这样既有 `sum |S|⁴ |Q|² <= U`、所有对应 lower spikes 与 mixed 下界
同时成立。这是相同边际数值预算的 sharpness，不是把这些数值函数
冒充原 annular Hecke polynomials。

原三次根处的真实 `deltaStar,tStar,mStar,zStar` 满足 (4)–(5)。
因此，若新证明只使用 (1)、原 plain moment、long inverse pointwise
上界及 amplified mean bound，它不能强制一个正 chi。
这里将高度固定在 `T1=1`。既有上界中的 `(1+T1)^A` 是固定常数，
允许的 `U^epsilon` 只放宽 (1)，所以不会排除已经用常数1满足较强
无损 scalar bounds 的有限模型。实际不等式的 epsilon 量词仍是
对每个 epsilon>0 分别有固定常数；若试图推出 chi>0，取
epsilon<chi/2，(2) 仍与它矛盾。这不模拟实际 profile 或height。
实际不同 Fourier heights、Möbius/prime 系数、自然零掩码、共同角色
或函数方程可能禁止这里的完全重合峰；这正是必须前向证明的新信息。

## 可验收的新预算引理

在原实际 core 上，若额外证明

\[
\sum_{u\in C}|M_{r_L}(u)|^2|S_m(u)|^4|Q_P(u)|^2
\ll U^{1+\delta r_L-\chi+\epsilon}(1+T_1)^A,
\quad \chi>0,
\tag{6}
\]

并保留 (5) 的真实尖峰、严格容量、共同presentation、一次selected prime
product、全部自然零掩码及 external tail order 前固定的有限A，
那么除以原 lower spike 给

\[
\#C\ll U^{R-\chi+O(\epsilon)}(1+T_1)^A.
\]

这一步是直接的 Markov/非负求和，不需要额外独立性假设。
先将 epsilon、bin/rounding losses 小于 chi 的固定份额，再按原
height closure 选择tau，才可获得真实固定 count decrement。
(6) 本轮尚未证明；引理没有登记新的无零边界。
