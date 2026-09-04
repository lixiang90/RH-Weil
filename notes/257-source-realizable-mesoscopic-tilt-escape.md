# 257. Source-realizable mesoscopic tilt escape 与 triple-convolution ledger

日期：2026-09-04

分支：NCE-8 / 路线 B1；接口：B1o quartic discrepancy budget / actual
degree-two tilt tightness

状态：quartic discrepancy moment 的 exact triple-convolution Brownian identity 与两个
一般 upper bounds 为 [T]；构造满足 positive sources、mass matching、relative lag
concentration、universal raw limit、fixed-physical-frequency extinction 的显式 source
family，但其 `J_4/mu^4` 发散且 actual `q_kappa^2` tilt 完全逃逸，为 [N]。该模型不是
von Mangoldt source，不反驳真实 zeta 的 B1o-q4 [O]；它证明所有现有 soft inputs 仍不足，
下一输入必须利用 prime-specific mesoscopic arithmetic。Gamma residual 未并入。

## 1. Quartic moment 的 real-space exact form

令 `a,b` 是 compactly supported even finite positive measures，总质量分别为 `A,B`，
并定义 centered signed measures

\[
 p=a-A\delta_0,\qquad c=B\delta_0-b,\qquad r=p+c.
\tag{1}
\]

令

\[
 W_p=A-\widehat a,\qquad W_c=B-\widehat b.
\]

于是

\[
 \widehat p=-W_p,\qquad \widehat c=W_c,\qquad
 \widehat r=-(W_p-W_c).
\tag{2}
\]

对零总质量 signed measure `eta`，记 `F_eta(x)=eta((-infty,x])`。Brownian
Plancherel identity 为

\[
 \|F_\eta\|_2^2=
 \int_{\mathbb R}\frac{|\widehat\eta(\xi)|^2}{2\pi\xi^2}\,d\xi.
\]

### 定理 257-A（exact triple-convolution identity）[T]

有精确恒等式

\[
 \boxed{
 \int_{\mathbb R}
 \frac{(W_p-W_c)^4(W_p^2+W_c^2)}{2\pi\xi^2}\,d\xi
 =\|F_{r*r*p}\|_2^2+\|F_{r*r*c}\|_2^2.}
\tag{3}
\]

因此，若 `S=A+B`、`D_raw=||F_p||_2^2+||F_c||_2^2>0`，则笔记 256 的
quartic discrepancy moment 恰为

\[
 \boxed{
 J_4=
 \frac{\|F_{r*r*p}\|_2^2+\|F_{r*r*c}\|_2^2}
 {S^4D_{\rm raw}}.}
\tag{4}
\]

#### 证明

卷积的 Fourier transform 相乘。由式 (2)，

\[
 |\widehat{r*r*p}|^2=(W_p-W_c)^4W_p^2,
 \qquad
 |\widehat{r*r*c}|^2=(W_p-W_c)^4W_c^2.
\]

分别应用 Brownian Plancherel identity并相加，得到式 (3)；再除以
`S^4D_raw` 即得式 (4)。`square`

式 (4) 把 frequency-side 的六阶非负积分变成两个 actual physical triple
convolutions；没有引入任意 Bessel coefficients。

### 推论 257-B（primitive-convolution upper bounds）[T]

有

\[
 \boxed{
 J_4\le
 \min\left\{
 16\frac{A^2+B^2}{S^2}\frac{\|F_r\|_2^2}{D_{\rm raw}},
 \left(\frac{\|r\|_{\rm TV}}S\right)^4
 \right\}.}
\tag{5}
\]

#### 证明

若 `eta` 总质量为零，则 primitive 与 convolution 交换：
`F_(eta*s)=F_eta*s`。Young inequality 给

\[
 \|F_{r*r*p}\|_2
 \le\|F_r\|_2\|r\|_{\rm TV}\|p\|_{\rm TV},
\]

对 `c` 同理。又

\[
 \|p\|_{\rm TV}\le2A,\qquad \|c\|_{\rm TV}\le2B,
 \qquad \|r\|_{\rm TV}\le2S.
\]

代入式 (4) 给第一个 upper。另一方面也可把 primitive 放在最后一个 factor：

\[
 \|F_{r*r*p}\|_2\le\|F_p\|_2\|r\|_{\rm TV}^2,
\]

并对 `c` 相加，给第二个 upper。`square`

第一个 bound 表明 `||F_r||^2=O(mu^4D_raw)` 足以推出 B1o-q4，但这是更强的
二阶 Brownian discrepancy input，并未由 qualitative PNT 得到。第二个 bound 只有在
centered discrepancy 的 total variation 真正小时才有用；prime--continuum cancellation
一般不会使其 TV 小。

## 2. Positive source family

对整数 `m>=2`，固定

\[
 \ell=\log2,qquad L_m=m\ell,qquad d_m=\sqrt{L_m},
\tag{6}
\]

以及

\[
 u_m=m^{-1},\qquad \varepsilon_m=m^{-1/8},\qquad
 B_m=1,qquad A_m=\frac{1+u_m}{1-u_m}.
\tag{7}
\]

对 `x>0` 记 `s_x=(delta_x+delta_(-x))/2`。定义 even positive measures

\[
 b_m=s_{L_m},\qquad
 a_m=A_m\big((1-\varepsilon_m)s_{L_m}
                 +\varepsilon_m s_{L_m+d_m}\big).
\tag{8}
\]

若需要任意 prescribed common mass scale，可同时把 `a_m,b_m` 乘同一个正数；下文
所有 normalized quantities均不变。

置 `v_x(xi)=1-cos(x xi)`。则

\[
 W_{c,m}=v_{L_m},\qquad
 W_{p,m}=A_m\big((1-\varepsilon_m)v_{L_m}
                    +\varepsilon_m v_{L_m+d_m}\big).
\]

由于 `(A_m-B_m)/(A_m+B_m)=u_m`，并记
`alpha_m=A_m/(A_m+B_m)=(1+u_m)/2`，有 exact formula

\[
 \boxed{
 \mu_m=u_m,qquad
 \Delta_m(\xi)=u_mv_{L_m}(\xi)
 +\alpha_m\varepsilon_m
   \big(v_{L_m+d_m}(\xi)-v_{L_m}(\xi)\big).}
\tag{9}
\]

## 3. 该 family 满足全部现有 soft inputs

### 引理 257-C（mass、lag、raw law 与 local matching）[T]

上述 family 满足：

1. `A_m/B_m->1` 且 `mu_m->0`；
2. 两个 one-sided lag laws 都在 `L_m` 相对集中，并有一致有界 normalized second
   moments；
3. raw Brownian denominator精确为

   \[
   D_m^{\rm raw}
   =\frac12\left[A_m^2(L_m+\varepsilon_m^2d_m)+L_m\right]
   \sim L_m;
   \tag{10}
   \]

4. 在 `t=mxi` 下，raw probabilities `nu_m` 弱收敛到笔记 255-(14) 的同一个
   universal law

   \[
   d\nu(t)=\frac{(1-\cos(t\log2))^2}{\pi\log2\,t^2}\,dt;
   \tag{11}
   \]

5. 对每个 fixed physical window `T<infinity`，

   \[
   \sup_{|\xi|\le T}(|\mu_m|+|\Delta_m(\xi)|)\longrightarrow0.
   \tag{12}
   \]

#### 证明

前两点由式 (6)--(8) 直接得到，因为 `d_m/L_m->0`。对 continuum atom，笔记
255-B 给 `||F_c||^2=L_m/2`。prime one-sided lag的两个独立 copies 的 minimum 为
`L_m+d_m` 当且仅当二者都选到 shifted atom，其概率为 `epsilon_m^2`；所以

\[
 \|F_p\|_2^2=\frac{A_m^2}{2}(L_m+\varepsilon_m^2d_m),
\]

证明式 (10)。relative lag concentration、`A_m/B_m->1` 及同一 Brownian argument
给式 (11)。最后由式 (9) 与 `0<=v_x<=2`，

\[
 \sup_\xi|\Delta_m(\xi)|
 \le2u_m+2\varepsilon_m\longrightarrow0,
\]

这甚至强于式 (12)。`square`

所以该 family 不只是笔记 255-F 的 arbitrary abstract tilt；它来自两个真实 positive
source measures，并自动使用笔记 254 的 actual polynomial normal form。

## 4. Mesoscopic band 上的 quartic lower

取 growing normalized-frequency band 对应的 physical interval

\[
 I_m=\left[d_m^{-1},2d_m^{-1}\right],
 \qquad mI_m=\left[m/d_m,2m/d_m\right].
\tag{13}
\]

后者以 `asymp sqrt(m)` 逃向无穷。令 `R_m=L_m/d_m=sqrt(L_m)`，并在
`xi=y/d_m` 下定义

\[
 G_m(y)=\varepsilon_m^{-4}\Delta_m(y/d_m)^4
 \big(W_{p,m}(y/d_m)^2+W_{c,m}(y/d_m)^2\big).
\tag{14}
\]

### 引理 257-D（fast-phase positive average）[T]

存在 absolute constant `c_0>0`，使

\[
 \frac1{d_m\varepsilon_m^4}
 \int_{I_m}\frac{\Delta_m(\xi)^4(W_{p,m}^2+W_{c,m}^2)}
 {2\pi\xi^2}\,d\xi
 \longrightarrow c_0.
\tag{15}
\]

#### 证明

在 `xi=y/d_m` 下，

\[
 v_{L_m}=1-\cos(R_my),\qquad
 v_{L_m+d_m}=1-\cos((R_m+1)y).
\]

又 `u_m/epsilon_m=m^(-7/8)->0`、`alpha_m->1/2`、`A_m->1` 及
`epsilon_m->0`。把 `G_m(y)` 展开成 fast phase `theta=R_my` 的有限三角多项式，
其 coefficients在 `y in [1,2]` 上一致收敛到

\[
 G(\theta,y)=\frac18
 \big(\cos\theta-\cos(\theta+y)\big)^4
 (1-\cos\theta)^2.
\tag{16}
\]

对所有非零 Fourier modes应用 Riemann--Lebesgue lemma，得到

\[
 c_0=\frac1{4\pi^2}
 \int_1^2\int_0^{2\pi}
 \frac{G(\theta,y)}{y^2}\,d\theta\,dy.
\tag{17}
\]

这里已使用 `dξ/ξ^2=d_m dy/y^2`。integrand非负；对每个 `y in [1,2]`，两个
trigonometric factors 的乘积不恒为零，故其 theta-average严格为正。连续性与 compact
`y`-interval 给 `c_0>0`。`square`

### 推论 257-E（mass-relative quartic budget fails）[N]

存在 `c_1>0`，使充分大 `m` 时

\[
 \boxed{J_{4,m}\ge\frac{c_1}{m}.}
\tag{18}
\]

因此

\[
 \boxed{\frac{J_{4,m}}{\mu_m^4}\ge c_1m^3\longrightarrow\infty.}
\tag{19}
\]

#### 证明

式 (15) 给 full nonnegative numerator至少为 fixed positive multiple of
`d_m epsilon_m^4`。由式 (10)，`D_raw asymp L_m`。而

\[
 \frac{d_m\varepsilon_m^4}{L_m}
 =\frac{\sqrt{m\log2}\,m^{-1/2}}{m\log2}
 =\frac1{m\sqrt{\log2}}.
\]

这给式 (18)。再用 `mu_m^4=m^(-4)` 得式 (19)。`square`

## 5. Actual degree-two response 的 complete escape

定义笔记 255-E 的 actual tilt

\[
 h_m(t)=q_\kappa(\mu_m,\Delta_m(t/m))^2,
 \qquad
 d\Pi_m=\frac{h_m\,d\nu_m}{\int h_m\,d\nu_m}.
\tag{20}
\]

### 障碍定理 257-F（source-realizable actual-tilt escape）[N]

对每个 fixed `T<infinity`，

\[
 \boxed{\Pi_m([-T,T])\longrightarrow0.}
\tag{21}
\]

换言之，`Pi_m` 不 tight，且其全部 normalized mass逃离每个 fixed compact，尽管
`nu_m` tight并收敛到式 (11)，且 multiplier在每个 fixed physical-frequency window
一致消失。

#### 证明

由引理 257-C，`|mu_m|+sup|Delta_m|->0`，所以充分大 `m` 时笔记 254-B 的
local lower 实际上在所有频率上一致成立：

\[
 h_m(t)\ge c_-^2(\mu_m^2+\Delta_m(t/m)^2)^2
 \ge c_-^2\Delta_m(t/m)^4.
\tag{22}
\]

推论 257-E 因而给

\[
 \int h_m\,d\nu_m\ge c_-^2J_{4,m}\gg m^{-1}.
\tag{23}
\]

另一方面，在 `|t|<=T` 上使用 cosine 的 Lipschitz bound，式 (9) 给

\[
 |\Delta_m(t/m)|
 \le2m^{-1}+\varepsilon_m d_mT/m
 =O_T(m^{-5/8}).
\tag{24}
\]

定理 256-A 的 global bound给

\[
 \sup_{|t|\le T}h_m(t)
 \le56^2\sup_{|t|\le T}
 (\mu_m^2+\Delta_m(t/m)^2)^2
 =O_T(m^{-5/2}).
\tag{25}
\]

因为 `nu_m` 是 probability，fixed core numerator至多为式 (25)；除以式 (23) 得
`Pi_m([-T,T])=O_T(m^(-3/2))->0`。`square`

## 6. 删除、循环性与结论边界

最小输入：

1. `[T]` two positive even sources与 exact centering；产生真实 `Wp,Wc`；
2. `[T]` Brownian Plancherel/primitive identity；产生式 (3)--(5)；
3. `[T]` mesoscopic shifted atom `d_m=sqrt(L_m)`，其 relative lag仍趋于 `1`；
4. `[T]` `epsilon_m=m^(-1/8)` 与更小的 mass mismatch `mu_m=m^(-1)`；分离 shape
   discrepancy与 total-mass discrepancy；
5. `[T]` actual `q_kappa` 的 local positive lower与 global upper；把 `J_4` failure
   转成 actual tilt escape。

删除审计：

- 删除 mesoscopic shift而令两个 source shapes完全相同，则 `Delta=mu v_L`，式 (19)
  不再成立；
- 强加 `epsilon_m=O(mu_m)`，本构造的 scale separation消失；
- 只检查 fixed normalized `t`，看不到逃逸 band `t asymp sqrt(m)`；
- 只检查 fixed physical `xi` 的 pointwise limit，同样看不到 shrinking physical band
  `xi asymp m^(-1/2)`；
- 删除 actual polynomial lower，只能证明 `J_4` 失败，不能推出 `Pi_m` escape；
- 把该 source family称为 von Mangoldt coefficients，会越过真正开放的 arithmetic
  realization问题。

非同义反复：反例由 explicit positive atomic measures生成；`nu_m,mu_m,Delta_m,h_m`
全部按 actual definitions计算，不是任意指定 tilted functions。逃逸 band、速率
`J_4>=c/m` 与 fixed-core upper `O_T(m^(-5/2))` 都由独立公式推出。

循环性审计：不使用 zeros、RH/GRH、PNT error、Weil positivity、bounded negative
index、四矩猜想或紧性完备化。反例证明 soft axioms 的逻辑不足，不证明真实 primes
满足或违反 B1o-q4。

## 7. 模型范围与下一最小引理 B1p

- Riemann zeta：定理 257-A--B 直接适用于 matched sign-pure subsystem；反例 257-F
  只排除 soft proof，不排除 prime-specific tightness；
- Dedekind zeta：positive prime-ideal source同样适用 triple-convolution ledger；
- Dirichlet/automorphic L：相位 coefficients 需 matrix-valued convolution版本；
- 函数域：可在 degree lattice上测试 mesoscopic shifted shells是否被 purity排除；
- 一般 spectral zeta：257-F 是 actual polynomial、positive-source 类中的严格
  finite-to-bulk no-go；
- 论文归属：与笔记 242--256 同属 Vaughan--Brownian response论文，作为证明
  “PNT-level matching不足”的 source-realizable obstruction section。

B1o 的 soft route 至此应停止。下一最小引理 **B1p** 必须使用真实 von Mangoldt
结构：把式 (4) 的 `r*r*p`、`r*r*c` 展开为 exact prime--continuum triple-convolution
coefficients，并在 mesoscopic lag separations `d=o(logY)` 上证明足以排除 257-F 机制的
response estimate；或者从真实 coefficients 构造相同 escape，从而终止 fixed-core
路线。仅重复 qualitative PNT、fixed-window matching或 raw tightness不再满足晋级条件。
