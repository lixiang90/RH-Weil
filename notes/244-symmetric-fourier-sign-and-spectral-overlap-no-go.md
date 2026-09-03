# 244. Symmetric Fourier 符号定理与 spectral-overlap gap 障碍

日期：2026-09-03

分支：NCE-8 / 路线 B1；接口：two-sided explicit formula / Brownian physical
prime--continuum Gram

状态：two-sided sign-pure components经过任意 common multiplier 后的精确负相关
与 positive spectral-overlap 表示为 [T]；仅由对称性、符号和共同 multiplier
不能得到 scale-uniform gain 的显式族为 [N]；actual response-weighted ratio
capture 为 [O]。本笔记不更新 PDF，不声称 RH/GRH、负指标可和或新的零点比例。

## 1. 本轮闭合与剩余缺口

笔记 243 证明：仅从 physical-space 中两个 base primitives逐点反号，不能把符号
穿过一般 common signed convolution；甚至整体内积也可能由负翻正。真实 zeta
finite data却始终保持负 prime--continuum correlation，说明还存在一个未使用的
结构。

该结构是 **two-sided evenness**。对称正 prime atoms精确居中后，其 Fourier
symbol为非正；对称负 continuum atoms精确居中后，其 Fourier symbol为非负。
common multiplier在 Hermitian inner product中只留下 `|R-hat|^2`，故整体 cross
必非正。这给出一个不依赖 PNT cancellation 的无条件符号定理。

然而符号不产生 uniform angle：本轮给出一个全有理、偶对称的 family，使负 cross
恒为 `-1`，而 prime energy线性增至 `N-1/2`。因此笔记 242 的 B1a 不能由
“two-sided + opposite coefficient signs + common response”自动推出；唯一剩余量是
实际 multiplier 权下 prime 与 continuum symbols 的定量 spectral overlap。

## 2. Two-sided sign-pure setup

取有限、紧支撑、非负且 even 的 measures `a,b` 于实 lag line，记

\[
 A=a(\mathbb R),\qquad B=b(\mathbb R).
\tag{1}
\]

定义 exact centered opposite components

\[
 p=a-A\delta_0,
 \qquad
 c=B\delta_0-b.
\tag{2}
\]

于是 `p(R)=c(R)=0`。使用 Fourier convention

\[
 \widehat\mu(\xi)=\int e^{-i\xi x}\,d\mu(x),
\tag{3}
\]

并定义非负 centered symbols

\[
 W_p(\xi)=\int(1-\cos(\xi x))\,da(x),
 \qquad
 W_c(\xi)=\int(1-\cos(\xi x))\,db(x).
\tag{4}
\]

evenness消去 sine parts，故

\[
 \widehat p=-W_p\le0,
 \qquad
 \widehat c=W_c\ge0.
\tag{5}
\]

令 `R` 为任意有限紧支撑 complex measure。对笔记 243 的 primitive记号，置

\[
 u_p=F_{p*R},\qquad u_c=F_{c*R}.
\tag{6}
\]

因为 `p,c` 零质量，两个 primitives均紧支撑且属于 `L^2(R)`。

## 3. Common-multiplier spectral sign theorem

### 定理 244-A（opposite symmetric cones have nonpositive response cross）[T]

在第 2 节公理下，定义 positive response measure

\[
d\omega_R(\xi)=
\frac{|\widehat R(\xi)|^2}{2\pi\xi^2}\,d\xi,
\tag{7}
\]

定义在 `R minus {0}` 上。该 density本身在原点未必可去，但式 (8) 中乘上
`W_p,W_c` 后的全部 integrands均有可去极限。则

\[
\boxed{
 \begin{aligned}
 P:=\|u_p\|_2^2&=\int W_p^2\,d\omega_R,\\
 C:=\|u_c\|_2^2&=\int W_c^2\,d\omega_R,\\
 z:=\langle u_p,u_c\rangle&=-\int W_pW_c\,d\omega_R\le0,\\
 E:=\|u_p+u_c\|_2^2
 &=\int(W_p-W_c)^2\,d\omega_R.
 \end{aligned}}
\tag{8}
\]

若两个 response channels还共同乘一个 scalar `gamma`，只需把
`d omega_R` 替换为 `|gamma|^2 d omega_R`。

#### 证明

分布导数给 `D F_mu=mu`。在 Fourier侧，除可去的原点外，

\[
 \widehat{F_{p*R}}(\xi)
 =\frac{\widehat p(\xi)\widehat R(\xi)}{i\xi},
 \qquad
 \widehat{F_{c*R}}(\xi)
 =\frac{\widehat c(\xi)\widehat R(\xi)}{i\xi}.
\tag{9}
\]

由式 (5)、Plancherel及式 (7)，

\[
 \langle u_p,u_c\rangle
 =\int\widehat p\,\overline{\widehat c}\,d\omega_R
 =-\int W_pW_c\,d\omega_R.
\tag{10}
\]

同理得到两个 diagonal identities。最后展开
`P+C+2z`，得到式 (8) 最后一行。所有 integrals有限，因为零质量使
`W_p,W_c=O(xi^2)` 于原点，而 compact support使 primitives属于 `L^2`。
`square`

### 推论 244-B（finite zeta prime--continuum sign）[T]

在 `scripts/audit_soft_zeta_orbit.py` 的 finite shared-lag quadrature中，先合并
physical prime channel `d_p=d_I+d_II`。则存在非负 even atomic measures `a,b`
使

\[
 d_p-d_p(\mathbb R)\delta_0=a-a(\mathbb R)\delta_0,
\tag{11}
\]

而 centered continuum channel等于

\[
 b(\mathbb R)\delta_0-b.
\tag{12}
\]

degree-two channel map对二者使用同一 divided-difference multiplier和同一 real
scalar。因此对每个 finite cutoff、每个允许的 Vaughan decomposition与每个
degree-two parameter，

\[
 \boxed{\Re\langle u_p,u_c\rangle\le0.}
\tag{13}
\]

#### 证明

每个 von Mangoldt atom在 `+log n,-log n` 成对出现且 coefficient非负，给式
(11)。每个 continuum cell在 `+lambda,-lambda` 成对出现且 coefficient非正；
lag-zero coefficient在 exact centering中抵消，给式 (12)。笔记 242-B 允许先合并
Type I/II 为 physical prime channel。最后应用定理 244-A。`square`

该推论把笔记 242、243 中仅由四个 finite scales观察到的“总体 cross为负”升级为
完整 finite algebra theorem。它不包含 Gamma residual 或其他 sign-indefinite
Archimedean channels；将这些项并入同一结论需要新的桥梁。

## 4. Uniform gain 不由 symmetric sign 自动产生

### 障碍定理 244-C（symmetric spectral-overlap gap can vanish）[N]

存在满足定理 244-A 全部公理的零质量 components `p,c` 与一列零质量 real common
multipliers `R_N`，使对每个 even `N>=4`，

\[
 P_N=N-\frac12,
 \qquad
 C_N=1,
 \qquad
 z_N=-1.
\tag{14}
\]

因此

\[
 \boxed{
 \frac{-z_N}{P_N+C_N}=\frac1{N+1/2}\longrightarrow0.}
\tag{15}
\]

特别地，不存在只依赖“even + sign-pure + exact centering + common multiplier”的
`delta>0` 使笔记 242-(25) 对所有配置成立。

#### 显式构造

取

\[
 a=\frac12(\delta_{-1}+\delta_1),
 \qquad
 b=\frac12(\delta_{-2}+\delta_2),
\tag{16}
\]

故

\[
 p=\frac12(\delta_{-1}+\delta_1)-\delta_0,
 \qquad
 c=\delta_0-\frac12(\delta_{-2}+\delta_2).
\tag{17}
\]

对 even `N>=4` 置

\[
 R_N=\sum_{k=0}^{N-1}(-1)^k\delta_k.
\tag{18}
\]

因为 `N` 为偶数，`R_N(\mathbb R)=0`。令

\[
 A_N=F_{p*R_N},\qquad B_N=F_{c*R_N}.
\tag{19}
\]

直接 prefix summation给：

- `A_N=1/2` 于 `[-1,0)` 和 `[N-1,N)`；
- `A_N=(-1)^(j+1)` 于 `[j,j+1)`，`0<=j<=N-2`；
- `B_N=-1/2` 于 `[-2,-1)` 和 `[N,N+1)`；
- `B_N=1/2` 于 `[0,1)` 和 `[N-2,N-1)`；
- 其余处二者按上述列表为零。

所以

\[
 \|A_N\|_2^2=\frac14+(N-1)+\frac14=N-\frac12,
\tag{20}
\]

\[
 \|B_N\|_2^2=4\cdot\frac14=1,
\tag{21}
\]

且只有 `[0,1)`、`[N-2,N-1)` 两个 overlap intervals贡献非零 cross；每个贡献
`-1/2`。故

\[
 \langle A_N,B_N\rangle=-1.
\tag{22}
\]

式 (14)--(15)随即成立。`square`

Fourier解释同样透明：

\[
 W_p(\xi)=1-\cos\xi,
 \qquad
 W_c(\xi)=1-\cos2\xi
 =2(1+\cos\xi)W_p(\xi).
\tag{23}
\]

`R_N-hat` 是集中于 odd multiples of `pi` 的 alternating Dirichlet kernel；恰在
这些频率上 `W_p=2` 而 `W_c=0`。因此 response weight主要看见 prime energy，
只在边界留下固定 cross和 continuum energy。

## 5. Ratio capture 是精确的下一接口

定理 244-A 将 B1a 写成纯非负 spectral overlap问题：证明

\[
 \int W_pW_c\,d\omega_R
 \ge\delta\int(W_p^2+W_c^2)\,d\omega_R.
\tag{24}
\]

这仍与目标 correlation bound等价，不能仅因 integrand非负就称为算术进展。
但可把它进一步拆成一个可证伪的 ratio-capture certificate。

### 定理 244-D（response-weighted ratio capture）[T]

固定 `0<m<=M<infinity`，令

\[
 G_{m,M}=\{\xi:m\le W_p(\xi)/W_c(\xi)\le M\},
\tag{25}
\]

其中 `W_c=0<W_p` 的点置于 complement；`W_p=W_c=0` 的点可任意归类，因为其
energy density为零。若某个 `0<=epsilon<1`
满足

\[
 \int_{G_{m,M}}(W_p^2+W_c^2)d\omega_R
 \ge(1-\epsilon)(P+C),
\tag{26}
\]

则式 (24)成立，且可取

\[
 \boxed{
 \delta=(1-\epsilon)
 \min\left\{\frac{m}{1+m^2},\frac{M}{1+M^2}\right\}.}
\tag{27}
\]

#### 证明

在 `G_(m,M)` 上置 `r=W_p/W_c`。逐点有

\[
 \frac{W_pW_c}{W_p^2+W_c^2}=\frac r{1+r^2}
 \ge
 \min\left\{\frac{m}{1+m^2},\frac{M}{1+M^2}\right\}.
\tag{28}
\]

在 complement 上 `W_pW_c>=0`。积分并用式 (26)即得式 (27)。`square`

式 (26)不是 RH 的隐式改写：它指定了一个固定 ratio band，且坏集只按
**actual response energy**计量。不过它仍是未证的 quantitative arithmetic
input；若允许 `m->0`、`M->infinity` 或 `epsilon->1`，定理变成空话。

## 6. 下一最小引理 B1c [O]

对 zeta 的真实 finite symbol与 degree-two divided-difference multiplier，寻找固定
constants

\[
 0<m<1<M<\infty,\qquad 0\le\epsilon<1,
\tag{29}
\]

并证明式 (26)在目标 square-root response blocks上一致成立。优先分两步：

1. 写出 `d omega_R` 在 dyadic frequency arcs上的 exact mass ledger；
2. 在承载固定比例 `(P+C)` 的 arcs上，用 prime/continuum quadrature误差证明
   `W_p/W_c` 落在固定 compact subinterval of `(0,infinity)`。

独立算术输入是 response-weighted、two-sided prime--continuum symbol comparability；
不是 arbitrary-vector Bessel bound，也不是未加权 PNT。式 (29)必须独立于 scale，
否则不能产生 B1a 的 uniform `delta`。

晋级条件：闭合式 (26)，或把坏集能量严格归约到一个已有可估计的 Type I/II
short-interval quantity。止损条件：若 actual `d omega_R` 像定理 244-C 一样集中到
`W_c/W_p ->0` 或 `infinity` 的 arcs，且该集中随 scale增强，则停止 uniform-factor
路线，返回笔记 242-D 的 absolute/summable two-defect Schur budget。

## 7. 最小公理、删除审计与非循环性

定理 244-A 使用：

1. **nonnegative source measures**：产生 `1-cos` 非负 symbols；
2. **two-sided evenness**：删除 sine/phase parts；
3. **exact mass centering**：把 symbols变成 `1-cos`；
4. **common multiplier**：cross中产生同一个 `|R-hat|^2`；
5. **translation-invariant Brownian `L^2` metric**：允许 Plancherel除以 `xi^2`。

删除审计：

- 删除 evenness，笔记 243-C 给 base primitives反号而整体 response翻正的反例；
- 删除 source positivity，式 (4)--(5)可变号；
- 删除 exact centering，原点 mass mode不再由 `1-cos` 表示；
- 删除 common multiplier，两个 response phases可任意改变 cross符号；
- 保留全部五条仍不能得到 uniform `delta`，由定理 244-C反驳；
- 删除式 (26)中固定的 `m,M,epsilon`，ratio certificate不提供正下界。

非同义反复审计：式 (13)是从 atom signs、evenness与 common response导出的新有限
结构结论；这些公理均不陈述 correlation sign。式 (24)只是 B1a 的 exact spectral
重写，已明确说明。真正新的障碍是 244-C；新的 arithmetic input是 244-D 中固定
参数的 hypothesis (26)。

循环性审计：全部 [T]/[N] 只用有限 measures、Fourier--Plancherel和有理 prefix
summation；不调用 RH/GRH、Weil positivity、谱酉性、PNT error、Mertens平方根界或
bounded negative index。

## 8. 模型范围与 Weil 接口

- **Riemann zeta**：推论 244-B 无条件适用于 finite sign-pure prime/continuum
  response；B1c 是新的定量缺口。
- **primitive Dirichlet L**：character phases破坏 source positivity/evenness，
  不能引用 244-B；需要 character-paired family average或 matrix-valued替代。
- **Dedekind zeta**：若 ideal von Mangoldt coefficients非负且 two-sided completion
  保留，244-A适用；Archimedean多参数背景须另审计。
- **automorphic L**：一般 coefficients带符号或复相位，244-A通常不适用。
- **函数域 zeta**：degree lattice与非负 prime-divisor coefficients给有限圆周版本；
  但若直接调用已知纯性证明 overlap，则会循环于该模型的 RH。
- **负向测试模型**：即使具有函数方程，只要 Euler coefficients或 background不满足
  sign-pure even setup，就可绕开 244-A，不与已知 RH 类比失败冲突。
- **显式公式型 Weil 配置**：式 (8)给 actual physical Gram的正谱表示；它不构造
  上同调分次、极化、Hard Lefschetz或 Frobenius权重。

本轮把 B1 的“统一负 correlation”分成两层：其**符号**由 two-sided explicit
formula结构无条件给出；其**强度**完全等于 actual common multiplier权下的 spectral
overlap。定理 244-C 证明两层之间没有抽象捷径。

后续进展：笔记 245 将 degree-two multiplier逐 Fourier character精确标量化为
`Q(d-hat)`，并证明只需在有限个 verified good arcs上取得相对于 exact Brownian
diagonal的 one-sided lower bound，无需控制整个高频尾 [T]。finite 数据支持宽
`[1/4,4]` ratio band，而 ratio 1附近的窄 band已停止 [E]；下一引理为 interval
good-arc certificate B1d。
