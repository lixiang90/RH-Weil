# 255. Universal raw Brownian limit 与 discrepancy-tilt reduction

日期：2026-09-04

分支：NCE-8 / 路线 B1；接口：B1m raw Brownian denominator / actual
degree-two response tilt

状态：matched Abel source 的 raw Brownian energy尺度、normalized-frequency universal
probability limit及 actual response 的 exact tilt reduction 为 [T]；仅由 raw tightness
与 local multiplier extinction不能决定 tilted tightness 的 underdetermination 为 [N]；
18-component core 的 limit mass数值为 [E]。本笔记只处理 sign-pure
prime--continuum subsystem，不并入 Gamma residual，不声称 RH/GRH 或 uniform physical
Schur gain。

## 1. Matched one-sided sources 与 even centering

固定 `0<sigma<1`，置 `a=1-sigma`，并令

\[
 Y_m=2^m,\qquad N_m\ge Y_m,\qquad L_m=\log Y_m=m\log2.
\tag{1}
\]

在 nonnegative lag half-line定义 prime 与 exact continuum source measures

\[
 da_m^+(\lambda)=
 \sum_{2\le n\le N_m}
 \Lambda(n)n^{-\sigma}e^{-n/Y_m}\delta_{\log n}(d\lambda),
\tag{2}
\]

\[
 db_m^+(\lambda)=
 \mathbf1_{[0,\log N_m]}(\lambda)
 e^{a\lambda-e^\lambda/Y_m}\,d\lambda.
\tag{3}
\]

记其总质量为 `A_m,B_m`。令 `a_m,b_m` 是分别把一半质量反射到负半轴所得的
even measures，并定义 centered components

\[
 p_m=a_m-A_m\delta_0,
 \qquad c_m=B_m\delta_0-b_m.
\tag{4}
\]

对应 symbols为

\[
 W_{p,m}(\xi)=\int(1-\cos(\xi\lambda))da_m,
 \qquad
 W_{c,m}(\xi)=\int(1-\cos(\xi\lambda))db_m.
\tag{5}

本笔记的 raw diagonal是尚未乘 degree-two divided difference的量

\[
 D_m^{\rm raw}
 =\int_{\mathbb R}
 \frac{W_{p,m}(\xi)^2+W_{c,m}(\xi)^2}
 {2\pi\xi^2}\,d\xi.
\tag{6}

## 2. Lag concentration lemma

### 引理 255-A（source lags concentrate at `log Y`）[T]

令 `X_{p,m},X_{c,m}` 分别服从 normalized one-sided measures
`a_m^+/A_m,b_m^+/B_m`。使用 qualitative PNT [R]，有

\[
 \frac{A_m}{B_m}\longrightarrow1,
 \qquad
 A_m\asymp B_m\asymp Y_m^a,
\tag{7}
\]

以及

\[
 \mathbb E\left|\frac{X_{p,m}}{L_m}-1\right|
 +\mathbb E\left|\frac{X_{c,m}}{L_m}-1\right|
 \longrightarrow0.
\tag{8}
\]

两族 normalized second moments还一致有界。

#### 证明

变量代换 `x=e^lambda=Y_mu` 把 continuum masses写成

\[
 B_m=Y_m^a\int_{1/Y_m}^{N_m/Y_m}
 u^{a-1}e^{-u}\,du.
\tag{9}
\]

因 upper endpoint至少为 `1`，式 (9) 上下夹住固定正倍数的 `Y_m^a`。而
`lambda/L_m=1+(log u)/L_m`；函数
`|log u|^j u^(a-1)e^(-u)` 对 `j=1,2` 在 `(0,infinity)` 可积，故 dominated
convergence给 continuum部分的式 (8)及二阶矩界。

对 prime mass，kernel `x^(-sigma)e^(-x/Y_m)` 的 Stieltjes partial summation与
`psi(x)=x+o(x)` 给 `A_m-B_m=o(Y_m^a)`，即式 (7)。对 lag deviation，使用
`Lambda(n)<=log n`，把 `n/Y_m` 分成 `(0,1)` 与 `[1,infinity)`，由积分比较得到

\[
 \sum_{n\le N_m}\Lambda(n)n^{-\sigma}e^{-n/Y_m}
 \left|\log\frac n{Y_m}\right|^2
 =O(Y_m^a\log Y_m).
\tag{10}
\]

除以 `A_mL_m^2 asymp Y_m^a(logY_m)^2`，normalized squared deviation为
`O(1/logY_m)`；Cauchy--Schwarz给式 (8) 的 prime部分。`square`

式 (10) 不是 prime-pair或 RH 型估计；其额外 `log Y` 损失仍足够证明 lag 的相对
位置集中。所用 qualitative PNT 的权威出处见来源表 45。

## 3. Raw Brownian energy 的精确概率表示

### 引理 255-B（minimum-of-two identity）[T]

令 `eta^+` 是 `[0,infinity)` 上总质量 `H>0` 的有限正测度，`eta` 是其 even
symmetrization，且 `r=eta-H delta_0`。若 `X,X'` 独立服从 `eta^+/H`，则

\[
 \boxed{
 \|F_r\|_2^2
 =\frac{H^2}{2}\,\mathbb E\min(X,X').}
\tag{11}
\]

#### 证明

在正半轴，centered primitive为

\[
 F_r(x)=-\frac H2\,\mathbb P(X>x),
\]

负半轴由 evenness给相同平方。故

\[
 \|F_r\|_2^2
 =\frac{H^2}{2}\int_0^\infty\mathbb P(X>x)^2dx.
\]

而 `P(X>x)^2=P(min(X,X')>x)`；layer cake给式 (11)。`square`

### 定理 255-C（raw denominator scale）[T]

在式 (1)--(8) 下，

\[
 \boxed{
 D_m^{\rm raw}
 \sim\frac{L_m}{2}(A_m^2+B_m^2)
 \sim L_mB_m^2.}
\tag{12}
\]

#### 证明

由式 (8)，若 `X,X'` 是任一 source的两个独立 normalized lags，则

\[
 \frac{\min(X,X')}{L_m}\longrightarrow1
\]

于 `L^1`；可用
`|min(x,y)-1|<=|x-1|+|y-1|` 及引理中的 uniform integrability。引理 255-B
分别应用于 `p_m` 与 `-c_m`，得到

\[
 \|F_{p_m}\|_2^2\sim\frac{A_m^2L_m}{2},
 \qquad
 \|F_{c_m}\|_2^2\sim\frac{B_m^2L_m}{2}.
\]

Plancherel正是式 (6)，再用 `A_m/B_m->1` 得式 (12)。`square`

## 4. Universal normalized-frequency law

把 raw energy推到 normalized frequency `t=m xi`，定义概率测度

\[
 \nu_m(E)=\frac1{D_m^{\rm raw}}
 \int_{\{\xi:m\xi\in E\}}
 \frac{W_{p,m}(\xi)^2+W_{c,m}(\xi)^2}
 {2\pi\xi^2}\,d\xi.
\tag{13}
\]

### 定理 255-D（universal raw Brownian limit）[T]

测度 `nu_m` 弱收敛到 probability measure

\[
 \boxed{
 d\nu(t)=
 \frac{(1-\cos(t\log2))^2}
 {\pi\log2\,t^2}\,dt,}
\tag{14}
\]

其中 `t=0` 取连续延拓值 `0`。这个极限与 cutoff ratio `N_m/Y_m>=1` 的变化无关。

#### 证明

由引理 255-A，对每个 fixed compact `t`-set一致有

\[
 \frac{W_{p,m}(t/m)}{A_m},\quad
 \frac{W_{c,m}(t/m)}{B_m}
 \longrightarrow1-\cos(t\log2).
\tag{15}
\]

这是因为 `tX/m=t(log2)(X/L_m)`，而 `1-cos` 在 compact arguments上一致
Lipschitz。引理 255-A 的二阶矩界与 `1-cos u<=u^2/2` 还给原点附近统一可积
majorant。

变量代换 `xi=t/m` 后，式 (13) 的 local density为

\[
 \frac{m}{2\pi D_m^{\rm raw}}
 \frac{W_{p,m}(t/m)^2+W_{c,m}(t/m)^2}{t^2}.
\tag{16}
\]

用式 (7)、(12)、(15)得到式 (14) 的 local `L^1` convergence。最后

\[
 (1-\cos u)^2
 =2(1-\cos u)-\frac12(1-\cos2u)
\tag{17}
\]

与经典积分

\[
 \int_{\mathbb R}\frac{1-\cos(bt)}{t^2}dt=\pi|b|
\tag{18}
\]

给

\[
 \int_{\mathbb R}
 \frac{(1-\cos(t\log2))^2}{\pi\log2\,t^2}dt=1.
\tag{19}
\]

local convergence与式 (19) 的 full mass结合，排除 loss at infinity，故得到 weak
convergence及 tightness。`square`

为使式 (18) 可独立审计：对 `epsilon>0,b>=0`，先在正半轴加入
`e^(-epsilon t)` 并对 `b` 微分，得到
`int_0^infinity e^(-epsilon t)sin(bt)/t dt=arctan(b/epsilon)`；从 `0` 积到 `b`
后令 `epsilon downarrow0`，得到正半轴值 `pi b/2`。偶性给式 (18)；`b<0` 由
cosine偶性处理。

定理 255-D 说明 Brownian geometry本身支持 fixed normalized cores；笔记 254-D 的
fixed physical-frequency multiplier extinction不能被误读为 raw energy escape。

## 5. Existing common core 的 raw limit mass [E]

令 `K_0` 为笔记 251 的 positive-frequency 18-component common core。对式 (14)
数值积分得到

\[
 \nu(K_0)\approx0.18173991227509219,
 \qquad
 \nu(K_0\cup(-K_0))\approx0.36347982455018438.
\tag{20}
\]

其中第一 component `[732/200,1239/200]` 已贡献约 `0.181604370067805`；其余远端
components的 raw limit mass很小。`scripts/b1m_raw_brownian_limit_audit.py` 重算这些
数值。式 (20) 为 [E]，不是 actual response capture，因为尚未乘 `q_kappa^2`。

## 6. Actual response 是一个 exact discrepancy tilt

沿用笔记 254 的

\[
 \mu_m=\frac{M_m}{S_m},qquad
 \Delta_m(\xi)=\frac{W_{p,m}(\xi)-W_{c,m}(\xi)}{S_m},
\]

并定义

\[
 h_m(t)=q_\kappa\!\left(\mu_m,\Delta_m(t/m)\right)^2.
\tag{21}
\]

### 定理 255-E（exact tilt reduction）[T]

若 actual degree-two response diagonal非零，则其 normalized frequency probability
`Pi_m` 精确满足

\[
 \boxed{
 d\Pi_m(t)=
 \frac{h_m(t)\,d\nu_m(t)}
 {\int_{\mathbb R}h_m\,d\nu_m}.}
\tag{22}
\]

故任意 measurable core `K` 的 actual capture恰为

\[
 \Pi_m(K)=
 \frac{\int_Kh_m\,d\nu_m}
 {\int_{\mathbb R}h_m\,d\nu_m}.
\tag{23}
\]

#### 证明

笔记 254-(11) 给

\[
 |\gamma_mQ_m|^2
 =\left(\frac{4\alpha^2}{9}\right)^2h_m.
\]

把它代入 actual response measure，再用式 (13)；common constant与
`D_m^(raw)` 在 normalization中约去，即得式 (22)--(23)。`square`

这把 B1m 的未知量严格缩成一个对象：已知且 tight 的 `nu_m` 被 actual arithmetic
discrepancy polynomial `h_m` 如何倾斜。Brownian kernel、ratio coordinate与 response
polynomial不再混在同一个未解释的“energy measure”中。

## 7. Raw tightness 与 local extinction 仍不足

笔记 254 证明 `h_m->0` locally uniformly；定理 255-D 又证明 `nu_m` tight。两者
仍不能单独决定式 (22) 是否 tight。

### 障碍定理 255-F（vanishing-tilt underdetermination）[N]

存在同一个 probability measure `nu`（可取式 (14)），以及两列 uniformly bounded
continuous nonnegative functions `h_m^(tight),h_m^(escape)`，使两列都 locally
uniformly趋于 `0`，但：

\[
 \frac{h_m^{\rm tight}d\nu}{\int h_m^{\rm tight}d\nu}=d\nu
\tag{24}
\]

恒成立，而

\[
 \frac{h_m^{\rm escape}d\nu}{\int h_m^{\rm escape}d\nu}
\tag{25}
\]

的全部质量逃向 `|t|->infinity`。

#### 证明

取任意 `epsilon_m downarrow0` 并令 `h_m^(tight)=epsilon_m`，则式 (24)显然。
另一方面，取固定非零 continuous bump `phi` 支撑于 `[0,1]`，令
`h_m^(escape)(t)=phi(t-m)`。它在每个 fixed compact上最终恒为零，且一致有界；
normalized tilted measure支撑于 `[m,m+1]`，故式 (25)逃逸。式 (14) 的 density除
离散零点外为正，所以 denominator非零。`square`

该反例不声称 zeta 的 `h_m` 可任意选择；它严格证明“raw weak limit + local
multiplier extinction”这两个已知输入在逻辑上不足。任何实际结论必须加入
`h_m` 的 arithmetic tail或profile估计。

## 8. 最小公理、删除与循环性审计

最小输入：

1. `[T]` positive one-sided Abel sources与 even symmetrization；作用是引理 255-B；
2. `[R]` qualitative PNT；只用于 `A_m/B_m->1` 与 prime mass normalization；
3. `[T]` elementary `Lambda(n)<=log n` 与 exponential cutoff；用于 lag uniform
   integrability；
4. `[T]` Brownian Plancherel kernel `1/(2pi xi^2)`；作用是式 (6)、(13)；
5. `[T]` actual degree-two normal form；只在式 (21)--(23)加入 arithmetic tilt。

删除审计：

- 删除 even centering，minimum-of-two factor `1/2` 与 limit density normalization改变；
- 删除 lag concentration，式 (15)不产生 universal `1-cos(tlog2)`；
- 删除 exact raw denominator scale，只得 local density而不能排除 mass escape；
- 把式 (20) 当 actual capture，遗漏 `h_m`，被定理 255-E纠正；
- 从 local `h_m->0` 推 actual escape，被定理 255-F反驳；
- 从 raw tightness推 actual tightness，同样被 255-F反驳；
- 把 Gamma residual并入 `nu_m` 或 `h_m`，需要尚未建立的第三通道 bridge。

非同义反复：limit probability (14) 从 lag concentration与 exact Brownian energy
scale导出，并有可检验的 universal density；它没有把 tightness写入公理。式 (22)
虽是 exact reweighting identity，但其价值在于与定理 255-D 结合后把唯一未知输入
隔离成 `h_m`，而不是声称它本身证明 Schur gain。

循环性审计：全部 [T]/[N] 只用 qualitative PNT、正测度概率恒等式、Plancherel、
dominated convergence及显式 polynomial identity；不使用 zeros、RH/GRH、PNT
平方根误差、Weil positivity、bounded negative index、四矩猜想或非构造完备化。

## 9. 模型与论文接口

- Riemann zeta：式 (1)--(23) 直接适用于 matched exact sign-pure subsystem；
- Dedekind zeta：ideal PNT与相同 Abel lag concentration成立时，raw limit仍为式
  (14)，residue常数在 normalization中消去；
- Dirichlet/automorphic L：coefficients带相位，positive-source minimum identity失效；
  需 packet/family averaged positive matrix measure；
- 函数域：degree集中于 top degree时得到 circle/lattice analogue，而不是连续
  density (14)；
- 一般 Brownian spectral models：引理 255-B及由 relative lag concentration推出的
  limit law独立于 zeta；
- 论文归属：与笔记 242--254 同属 response论文；定理 255-D--F 是 finite-to-bulk
  审计的核心分离结果。

## 10. 下一最小引理 B1n [O]

定义 normalized discrepancy profile

\[
 g_m(t)=\frac{q_\kappa(\mu_m,\Delta_m(t/m))}
 {\left(\int q_\kappa(\mu_m,\Delta_m(s/m))^2d\nu_m(s)\right)^{1/2}}.
\tag{26}
\]

则 actual response probability恰为 `g_m(t)^2dnu_m(t)`。下一步必须在下列二者中
完成一个：

1. **tightness route**：证明对每个 `epsilon>0` 存在 fixed `T`，

   \[
   \limsup_m\int_{|t|>T}g_m(t)^2d\nu_m(t)<\epsilon;
   \tag{27}
   \]

2. **escape route**：构造 `T_m->infinity` 与 fixed `c>0`，证明

   \[
   \limsup_m\int_{|t|\le T_m}g_m(t)^2d\nu_m(t)\le1-c.
   \tag{28}
   \]

最先需要的独立 arithmetic estimate 是 `q_kappa(mu_m,Delta_m)` 的 global
`L^2(nu_m)` denominator 与 growing-`t` tail；仅有 pointwise PNT不够。若 tightness
成立，再选择式 (14) 下质量正且避开 resonances的 fixed core应用笔记 253 的
Schur factor；若 escape成立，则停止 fixed-core路线并形成 actual response no-go。
