# 256. Quartic discrepancy capture 与 conditional Schur gain

后续271--274：Littlewood实际误差振荡保证一条新的自由共尾大质量选择；
273独立证明真实乘积逆最近间距预算，274进一步将同一选择的full四阶预算
严格归约到次线性增长频带
\(|\xi|\le Y\sqrt{\log(2\log Y)/\log Y}=o(Y)\)。
这不是本篇预算已经成立，也不是268每dyadic首素数schedule的同序列改进。

日期：2026-09-04

分支：NCE-8 / 路线 B1；接口：B1n normalized actual tilt / sign-pure
prime--continuum Schur gain

状态：actual degree-two multiplier 的全可行域上界、局部/全局 quartic capture
归约为 [T]；由一个明确的 prime--continuum quartic discrepancy budget 推出的 fixed-core
capture 与 uniform Schur gain 为 [C]，该 budget 本身仍为 [O]。本文不并入 Gamma
residual，不声称 RH/GRH、完整 Vaughan gain或 Weil 正性。

## 1. 设置与目标

沿用笔记 254--255。令 `a_m,b_m` 是 even nonnegative prime 与 matched continuum
source measures，

\[
 A_m=a_m(\mathbb R),\qquad B_m=b_m(\mathbb R),\qquad
 S_m=A_m+B_m>0,
\tag{1}
\]

\[
 \mu_m=\frac{A_m-B_m}{S_m},\qquad
 \Delta_m(\xi)=\frac{W_{p,m}(\xi)-W_{c,m}(\xi)}{S_m}.
\tag{2}
\]

这里

\[
 W_{p,m}(\xi)=\int(1-\cos(\xi\lambda))\,da_m(\lambda),\qquad
 W_{c,m}(\xi)=\int(1-\cos(\xi\lambda))\,db_m(\lambda).
\tag{3}
\]

记笔记 255 的 normalized raw Brownian probability 为 `nu_m`，并置

\[
 r_m(t)^2:=\mu_m^2+\Delta_m(t/m)^2,
 \qquad
 h_m(t):=q_\kappa(\mu_m,\Delta_m(t/m))^2,
\tag{4}
\]

其中 `kappa=sqrt(3)/2`，且 `q_kappa` 是笔记 254-(10) 的 actual polynomial。
只要 actual response diagonal 非零，笔记 255-E 给

\[
 \Pi_m(K)=\frac{\int_Kh_m\,d\nu_m}{\int_{\mathbb R}h_m\,d\nu_m}.
\tag{5}
\]

B1n 的直接形式要求估计式 (5) 的 numerator 与 denominator。本笔记先把它归约为
不再含 degree-four polynomial cancellation 的 positive quartic discrepancy energy
`r_m^4`。

## 2. 全可行域的显式 polynomial envelope

正源结构自动给

\[
 0\le W_{p,m}\le2A_m,\qquad 0\le W_{c,m}\le2B_m.
\tag{6}
\]

因此逐频率有

\[
 |\mu_m|\le1,\qquad |\Delta_m|\le2.
\tag{7}
\]

这不是额外算术公理，而是 `1-cos u in [0,2]` 的直接结果。

### 定理 256-A（global feasible-domain quartic envelope）[T]

对每个满足 `|mu|<=1, |Delta|<=2` 的实数对，

\[
 \boxed{
 |q_\kappa(\mu,\Delta)|
 \le C_*\,(\mu^2+\Delta^2),\qquad C_*:=56.}
\tag{8}
\]

特别地，实际 matched source 的每个频率都满足

\[
 h_m(t)\le C_*^2r_m(t)^4.
\tag{9}
\]

常数 `56` 只为给出完全显式、易审计的全局界，没有作最优化。

#### 证明

把笔记 254-(10) 按次数写成 `q=q_2+q_3+q_4`。二次型的最大本征值见
笔记 254-(15)，故

\[
 |q_2|\le\kappa^2\frac{4+\sqrt{13}}2
 (\mu^2+\Delta^2)<3(\mu^2+\Delta^2).
\tag{10}
\]

在式 (7) 的矩形上，

\[
\begin{aligned}
 |q_3|
 &\le2\kappa(2\Delta^2+4\Delta^2+12\mu^2+4\mu^2)\\
 &\le32\kappa(\mu^2+\Delta^2)<28(\mu^2+\Delta^2),
\end{aligned}
\tag{11}
\]

这里分别用了 `|Delta|^3<=2Delta^2`、`|mu|<=1`、
`|Delta|<=2` 与 `|mu|^3<=mu^2`。同理，

\[
\begin{aligned}
 |q_4|
 &\le4\Delta^2+10\Delta^2+10\Delta^2
       +20\mu^2+5\mu^2\\
 &\le25(\mu^2+\Delta^2).
\end{aligned}
\tag{12}
\]

三式相加给 `|q|<56(mu^2+Delta^2)`，因而也给所陈述的非严格界。

平方即得式 (9)。`square`

## 3. Local lower 与 global denominator 的夹逼

令 `epsilon_0=10^{-3}`，并记笔记 254-B 的显式常数

\[
 c_-:=\kappa^2\frac{4-\sqrt{13}}2
 -2(30\kappa\epsilon_0+31\epsilon_0^2)
 >0.09589.
\tag{13}
\]

若 `|mu|+|Delta|<=epsilon_0`，则

\[
 q_\kappa(\mu,\Delta)\ge c_-(\mu^2+\Delta^2).
\tag{14}
\]

### 定理 256-B（quartic capture reduction）[T]

令 `K subset R` 可测，并假设在 `K` 上逐点有

\[
 |\mu_m|+|\Delta_m(t/m)|\le\epsilon_0.
\tag{15}
\]

若 actual response diagonal 非零，则

\[
 \boxed{
 \Pi_m(K)\ge
 \frac{c_-^2}{C_*^2}
 \frac{\displaystyle\int_Kr_m(t)^4\,d\nu_m(t)}
 {\displaystyle\int_{\mathbb R}r_m(t)^4\,d\nu_m(t)}.}
\tag{16}
\]

对任意 fixed compact `K`，matched PNT hypotheses 保证式 (15) 对充分大 `m`
成立。因此 B1n 的一个充分而非必要的下一输入是 positive quartic measure
`r_m^4dnu_m` 在某个 fixed core 上的 tight capture。

#### 证明

式 (14) 在 `K` 上给 `h_m>=c_-^2r_m^4`；定理 256-A 在全实轴给
`h_m<=C_*^2r_m^4`。分别代入式 (5) 的 numerator 与 denominator即得式 (16)。
fixed compact 上式 (15) 最终成立，来自笔记 254-D 的
`mu_m,Delta_m(t/m)->0` 局部一致收敛。`square`

式 (16) 只有一侧。在 local positive neighborhood 之外（仍在真实可行域内），
`q_kappa` 可能具有零点；在未证明 global polynomial lower 之前，不能反向声称
`Pi_m(K)` 与 quartic capture 等价。

## 4. 一个完全算术化的充分输入

定义 raw probability 下的 quartic discrepancy moment

\[
 J_{4,m}:=\int_{\mathbb R}\Delta_m(t/m)^4\,d\nu_m(t).
\tag{17}
\]

由于 `nu_m` 是 probability，逐点初等不等式给

\[
 \mu_m^4+J_{4,m}
 \le\int r_m^4\,d\nu_m
 \le2(\mu_m^4+J_{4,m}).
\tag{18}
\]

左边甚至可把混合正项 `2mu_m^2Delta_m^2` 保留；这里故意只用最小账本。

### 开放算术输入 B1o-q4 [O]

是否存在与 `m` 无关的有限常数 `C_4`，使沿某条 cofinal matched schedule，

\[
 \boxed{J_{4,m}\le C_4\mu_m^4}
\tag{19}
\]

对充分大且 `mu_m !=0` 的 `m` 成立？

式 (19) 不涉及零点。把笔记 255-(13) 定义的 `nu_m` 展开，它等价于 prime--continuum
symbols 的显式非负积分估计

\[
 \int_{\mathbb R}
 \frac{(W_{p,m}-W_{c,m})^4(W_{p,m}^2+W_{c,m}^2)}
 {2\pi\xi^2}\,d\xi
 \le C_4\mu_m^4S_m^4D_m^{\rm raw}.
\tag{20}
\]

所以它在 sources 中是六阶的 arithmetic response moment；“四阶”只指 normalized
discrepancy `Delta` 的幂次。它可能很强，当前没有证明，也不得由有限数值拟合升级。

### 推论 256-C（mass-relative quartic criterion）[C]

假设开放输入 (19) 成立。令 `K` 是 fixed compact `nu`-continuity set，且
`nu(K)>0`，其中 `nu` 是笔记 255-D 的 universal raw limit。再假设 `mu_m!=0`
eventually。则

\[
 \boxed{
 \liminf_{m\to\infty}\Pi_m(K)
 \ge\frac{c_-^2\nu(K)}{2C_*^2(1+C_4)}>0.}
\tag{21}
\]

#### 证明

由 `r_m^4>=mu_m^4`，

\[
 \int_Kr_m^4\,d\nu_m\ge\mu_m^4\nu_m(K).
\]

式 (18)--(19) 给

\[
 \int_{\mathbb R}r_m^4\,d\nu_m
 \le2(1+C_4)\mu_m^4.
\]

约去非零的 `mu_m^4`，再应用定理 256-B。由 `nu_m weakly to nu` 且
`nu(partial K)=0`，有 `nu_m(K)->nu(K)`，得到式 (21)。`square`

`nu` 具有连续密度，因此任意有限个闭区间的并只要端点有限，就是 continuity set。
条件 `mu_m!=0` 不能静默删除。式 (19) 本身不约束零质量点；若额外要求
同一不等式也在 `mu_m=0` 处成立，则它强迫 `Delta_m=0`，`nu_m`-a.e.，
从而 actual response diagonal为零，式 (5) 本身不再定义。
此处量词由笔记261的非零质量扰动审计修正。

## 5. 与 physical Schur gain 的接口

令 `P_m,C_m,z_m` 是笔记 244 的 actual sign-pure prime--continuum Gram entries，
并置 `D_m=P_m+C_m>0`。其 exact sign theorem 给

\[
 -\frac{z_m}{D_m}
 =\int_{\mathbb R}
 \frac{W_{p,m}(t/m)W_{c,m}(t/m)}
 {W_{p,m}(t/m)^2+W_{c,m}(t/m)^2}\,d\Pi_m(t),
\tag{22}
\]

其中 `0/0` 处 integrand 取 `0`，且 integrand处处非负。

### 推论 256-D（conditional uniform sign-pure Schur gain）[C]

除推论 256-C 的 hypotheses 外，设 `K` 避开 matched continuum resonances，并满足
笔记 253-B 的 fixed-core ratio conclusion。则充分大 `m` 时 core 上式 (22) 的
integrand至少为 `2/5`，并且

\[
 \boxed{
 \liminf_{m\to\infty}\left(-\frac{z_m}{D_m}\right)
 \ge\frac{c_-^2\nu(K)}{5C_*^2(1+C_4)}>0.}
\tag{23}
\]

#### 证明

笔记 253-B 给 core 上的 scalar Schur factor一致趋于 `1/2`，故最终至少为
`2/5`。式 (22) 的 complement integrand非负，所以

\[
 -\frac{z_m}{D_m}\ge\frac25\Pi_m(K).
\]

代入式 (21)即得式 (23)。`square`

式 (23) 只闭合 sign-pure two-channel subsystem。Gamma residual 是第三个可能不定号
channel；未建立 block Schur bridge 之前，不能把 (23) 称为完整 zeta response gain。

## 6. 最小公理、删除与循环性审计

最小输入：

1. `[T]` even nonnegative source representation；给式 (6)--(7) 与全局常数 `C_*`；
2. `[T]` actual degree-two normal form；给 `q_kappa`，而非任意外生 multiplier；
3. `[T]` local positive quadratic jet；只用于 fixed core numerator lower；
4. `[R]` qualitative PNT；只用于 fixed compact 上 `mu_m,Delta_m->0` 与
   `nu_m weakly to nu`；
5. `[O]` arithmetic budget (19)；只用于 total quartic denominator upper；
6. `[T]` sign-pure Fourier sign theorem及 matched ratio；只用于把 capture转成式 (23)。

删除审计：

- 删除 source positivity，式 (7) 与全局 envelope 的固定可行域消失；
- 删除 local lower，只剩 denominator upper，不能证明 core capture；
- 删除 (19)，定理 255-F 的 escaping tilt 仍未被排除；
- 删除 `mu_m!=0`，用于 normalize 的 mass scale可能为零；
- 删除 continuity-set 条件，弱收敛一般不给 `nu_m(K)->nu(K)`；
- 删除 ratio conclusion，positive capture不能自动转为 quantitative cross gain；
- 删除 sign-pure complement positivity，core 之外可能抵消 core gain；
- 把 (16) 写成二侧等价，需要未证明的 global lower；
- 把 two-channel式 (23) 直接加上 Gamma，缺少独立 block bridge。

非同义反复：式 (19) 是由 primes、continuum kernel和 raw Brownian weight完全显式
定义的六阶积分估计；它没有把 `Pi_m(K)>0` 或 Schur gain写入假设。定理 256-A--B
说明为什么这一具体 arithmetic moment足够，而不是将 desired capture换名。

循环性审计：已证部分只用正源范围、actual polynomial的有限代数、定性 PNT、弱收敛
与 elementary moment inequalities。条件 (19) 没有使用 zeros作定义，也没有假设 RH、
PNT平方根误差、Weil positivity、谱酉性或 bounded negative index；但它的真实算术强度
尚未确定，后续必须从 prime sums独立证明或以反例否定，不能因其形式不含零点就宣称
弱于 RH。

## 7. 模型范围与下一最小引理 B1o

- Riemann zeta：定理 256-A--B 无条件适用于 matched sign-pure subsystem；
  推论 256-C--D 等待 (19)；
- Dedekind zeta：若 prime-ideal coefficients保持 nonnegative，代数归约保留，但
  `J_4` 预算须重新证明；
- Dirichlet/automorphic L：带相位 coefficients 不满足 scalar式 (6)，需 matrix-valued
  feasible domain；
- 函数域：有限 degree 可直接检查相应离散 `J_4`，可作正向/负向测试；
- 一般 spectral zeta：只要有两个 sign-pure positive sources 与同一 polynomial，
  定理 256-A--B 保留；
- 论文归属：与笔记 242--255 同属 Vaughan--Brownian response论文，作为 B1n 从
  normalized tilt到 explicit arithmetic moment 的归约节。

下一最小引理 **B1o** 是证明或反驳式 (19)。应先把 `J_{4,m}` 展开为 Brownian
minimum kernel下的有限 prime--continuum 六重 signed sum，寻找 exact diagonal与
off-diagonal cancellation；若只能得到 `J_4=o(1)` 而不能相对 `mu_m^4` 控制，则不足以
应用推论 256-C。并行但独立的后续是 Gamma block bridge，不得混入 (19)。

后续：笔记 257 已把 `J_4` 精确写成两个 centered triple convolutions 的 Brownian
primitive energy [T]，并构造满足全部现有 soft inputs 的 positive-source family，使
`J_4/mu^4->infinity` 且 actual `q_kappa^2` tilt 沿 `t asymp sqrt(m)` 完全逃逸 [N]。
因此 B1o 的 soft route 已止损；B1p 必须利用真实 von Mangoldt coefficients 在
mesoscopic lag separations 上的算术结构，不能继续从 qualitative PNT或 raw
tightness推导式 (19)。

2026-09-05后续：对固定 \(0<\sigma<1/2\)，268在实际dyadic整数尺度，以首个素数处两个相邻共同cutoff
选择非零质量，证明 \(|M|\gg Y^{-\sigma}\log Y\)。
结合267的独立加权均值高频界，所选schedule满足
\(J_{4,>Y^2}=O((\log Y)^{-3}\mu^4)\)。
因此本篇(19)沿该schedule严格归约为
\(J_{4,\le Y^2}=O(\mu^4)\)，该增长频带预算仍[O]。
这条选择在255允许的 \(N_m\ge Y_m\) 范围内，但不覆盖原固定
\(N=\lfloor Y\log^2Y\rfloor\) 或无cutoff源；也未补入Gamma。
