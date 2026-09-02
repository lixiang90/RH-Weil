# 234. 幂级高乘积 Gabor 带通核与 core--tail 分割障碍

日期：2026-09-03

分支：MOM-1 / 路线 A1m；接口：fixed-power alternating determinant response

状态：exact finite response 的带通表示、局部极限、频谱间隙、正 core 与补偿
tail、response-measure scalarization 及一阶 discrepancy 桥梁为 [T]；把 core
正下界单独解释成完整 response 障碍为 [N]；真实四 von-Mangoldt、six-window
determinant measure 的 mesoscopic discrepancy 为 [O]。本笔记不更新 PDF，也不
改变比例常数的 [C] 状态。

## 1. 本轮结论

笔记 233 把 fixed-power high-product 的下一输入写成 actual signed determinant
response，并建议先分离 coherent core `|ad-bc|<=R/X`。本轮对相位作逆向审计后
发现：core 与 tail 不能被当成两个独立障碍。

令

\[
 t=X\Delta=X\log\frac{ad}{bc},
 \qquad D=d_G,
 \qquad h_0=\frac{2\pi}{L},
 \qquad T=2\pi X.
\tag{1}
\]

归一化 Gabor 响应的实部精确是频率位于约 `[1,2]` 的离散带通平均；当
`D/(XL)->1` 时，它局部一致收敛到

\[
 \boxed{
 K(t)=\int_1^2\cos(2\pi\xi t)\,d\xi
 =\frac{\sin(4\pi t)-\sin(2\pi t)}{2\pi t}
 =\frac{\sin(\pi t)}{\pi t}\cos(3\pi t).}
\tag{2}
\]

该核具有严格频谱间隙：其 Fourier support 是
`[1,2] union [-2,-1]`，所以

\[
 \int_{\mathbb R}K(t)\,dt=0.
\tag{3}
\]

但 resolution core 的质量严格为正：

\[
 \boxed{
 c_0:=\int_{-1}^{1}K(t)\,dt
 =\frac{\operatorname{Si}(4\pi)-\operatorname{Si}(2\pi)}{\pi}
 =0.023558003094\ldots>0.}
\tag{4}
\]

因此外层的条件收敛质量精确为 `-c_0`。一个平坦 determinant density 会在
core 中产生正主项，却由 oscillatory tail 完全抵消。故“core 有正下界就停止
比例路线”不是合法判据；必须先证明真实算术密度破坏了这种 core--tail 补偿。

## 2. Exact finite band-pass kernel

沿用笔记 216 的 Dirichlet factor

\[
 \mathcal D_d(\Delta)=\sum_{k=0}^{d-1}e^{ikh_0\Delta}.
\tag{5}
\]

定义

\[
 K_{X,D}(t)
 :=\frac1D\Re\left(
 e^{iTt/X}\mathcal D_D(t/X)
 \right).
\tag{6}
\]

### 定理 234-A（exact discrete frequency band）[T]

精确地，

\[
 \boxed{
 K_{X,D}(t)
 =\frac1D\sum_{k=0}^{D-1}
 \cos\left(2\pi\left(1+\frac{k}{XL}\right)t\right).}
\tag{7}
\]

若 `lambda_X=D/(XL)->1`，则对每个 fixed `M`，

\[
 \sup_{|t|\le M}|K_{X,D}(t)-K(t)|
 \ll M\left(\frac1D+|\lambda_X-1|\right).
\tag{8}
\]

特别地，标准选择 `D=round(XL)` 给局部一致收敛。

#### 证明

把 `Delta=t/X`、`T=2pi X` 与 `h_0=2pi/L` 代入式 (5)--(6)，立即得到
式 (7)。再写

\[
 \frac{k}{XL}=\lambda_X\frac{k}{D}.
\]

式 (7) 是函数 `s mapsto cos(2pi(1+lambda_X s)t)` 在 `[0,1]` 的左
Riemann sum。该函数对 `s` 的导数在 `|t|<=M` 上为 `O(M)`；把
`lambda_X` 换成 `1` 的误差也为 `O(M|lambda_X-1|)`。所得积分正是式 (2)。
这证明式 (8)。`square`

几何和的 centered form 还给出

\[
 K_{X,D}(t)=
 \frac{\sin(\pi Dt/(XL))}{D\sin(\pi t/(XL))}
 \cos\left(2\pi t+\frac{(D-1)\pi t}{XL}\right),
\tag{9}
\]

这与笔记 216-B 完全一致。式 (7) 比 sinc envelope 多保留了决定符号的
carrier band。

## 3. 频谱间隙与精确 core--tail 补偿

采用 Fourier convention

\[
 \widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i\xi t}\,dt.
\tag{10}
\]

### 定理 234-B（band gap and compensating tail）[T]

在 tempered-distribution 意义下，

\[
 \boxed{
 \widehat K(\xi)
 =\frac12\mathbf 1_{[1,2]}(\xi)
 +\frac12\mathbf 1_{[-2,-1]}(\xi).}
\tag{11}
\]

因而式 (3) 成立。并且式 (4) 为正，且 symmetric improper integral 满足

\[
 \boxed{
 \lim_{M\to\infty}\int_{1<|t|\le M}K(t)\,dt=-c_0.}
\tag{12}
\]

#### 证明

式 (2) 的第一种表示逐频率 Fourier transform 后直接给式 (11)。零频率不在
support 中，所以 `widehat K(0)=0`，即式 (3)；积分由 Dirichlet test 收敛。

对式 (4)，由偶性及变量替换得到

\[
 \int_{-1}^{1}K(t)\,dt
 =\frac1\pi\int_{2\pi}^{4\pi}\frac{\sin u}{u}\,du.
\tag{13}
\]

把 `[2pi,4pi]` 的两半配对，右端的未除 `pi` 积分为

\[
 \int_0^\pi \sin s
 \left(\frac1{2\pi+s}-\frac1{3\pi+s}\right)ds>0.
\tag{14}
\]

故 `c_0>0`。最后由全积分为零减去 core 即得式 (12)。`square`

### 障碍推论 234-C（core-only lower-bound criterion fails）[N]

仅证明 `|t|<=1` 的 response 对一个 asymptotically flat positive determinant
density 有正主项，不能推出完整 signed response 有正主项。常密度模型已经同时
满足：core 主项为 `c_0>0`，tail 主项为 `-c_0`，总和为零。

这不是实际素数 response 的反例；它严格排除的是把 coherent core 从真实
Gabor carrier 中割裂、再把 core 正性直接升级为四矩障碍的 proof schema。

## 4. 实际 response 的正测度 scalarization

固定任意 factor/product/aperture cells。对两个不同 ordered atoms
`i=(a,b)`、`j=(c,d)`，置

\[
 t_{ij}=X\log\frac{ad}{bc},
 \qquad
 w_{ij}=b_ab_bb_cb_dW_{a,b;c,d}\ge0,
\tag{15}
\]

其中 `W` 是笔记 216-(9) 的 exact translated six-window overlap。定义有限正
测度

\[
 \mu_X=\sum_{i\ne j}w_{ij}\delta_{t_{ij}}.
\tag{16}
\]

### 定理 234-D（exact response-measure identity）[T]

笔记 216-(11) 的 off-diagonal bulk main real part 精确等于

\[
 \boxed{
 \beta_L^4D\int_{\mathbb R}K_{X,D}(t)\,d\mu_X(t).}
\tag{17}
\]

等价地，若

\[
 \widehat\mu_X(\xi)=\int e^{2\pi i\xi t}\,d\mu_X(t),
\tag{18}
\]

则式 (17) 中除去 `beta_L^4 D` 的量为

\[
 \boxed{
 \frac1D\sum_{k=0}^{D-1}
 \Re\widehat\mu_X\left(1+\frac{k}{XL}\right).}
\tag{19}
\]

#### 证明

式 (17) 是把式 (6) 逐 atom pair 代入笔记 216-(11)；式 (19) 再由式 (7)
逐项交换有限求和与积分得到。`square`

这一步保留四个 von Mangoldt weights、cells、six-window overlap、carrier 与全部
consecutive Gabor samples。缺失输入被定位在正算术测度 `mu_X` 的固定非零频带
discrepancy，而不是任意系数的 Farey/Bessel bound。

## 5. 从区间 discrepancy 到带通 response

### 定理 234-E（first-discrepancy band-pass bridge）[T]

令 `M>=2`，`mu` 为 `[-M,M]` 上有限正测度，`c>=0`，并置

\[
 E(\mu,c;M)
 :=\sup_{-M\le u\le M}
 \left|\mu([-M,u])-c(u+M)\right|.
\tag{20}
\]

则

\[
 \boxed{
 \left|\int_{-M}^{M}K(t)\,d\mu(t)\right|
 \ll \frac cM+E(\mu,c;M)\log(2+M).}
\tag{21}
\]

若 `B=mu([-M,M])`，则 exact finite response 还满足

\[
 \boxed{
 \left|\int K_{X,D}\,d\mu\right|
 \ll \frac cM+E\log(2+M)
 +BM\left(\frac1D+\left|\frac D{XL}-1\right|\right).}
\tag{22}
\]

#### 证明

由式 (2) 及一次分部积分，

\[
 \left|\int_{-M}^{M}K(t)dt\right|\ll M^{-1},
 \qquad
 |K(M)|+\int_{-M}^{M}|K'(t)|dt\ll\log(2+M).
\tag{23}
\]

对 signed measure `nu=mu-cdt` 置
`F(u)=nu([-M,u])`。Stieltjes integration by parts 给

\[
 \left|\int Kd\nu\right|
 \le \|F\|_\infty
 \left(|K(M)|+\int|K'|\right).
\tag{24}
\]

加回 constant-density 项即得式 (21)。式 (22) 再由定理 234-A 的 uniform
误差乘总质量 `B` 得到。`square`

因此若 `M->infinity`、`D/(XL)->1`，并能在实际 response measure 上证明

\[
 E(\mu_X,c_X;M)=o\left(\frac{B_X}{\log M}\right),
 \qquad
 M\left(D^{-1}+|D/(XL)-1|\right)=o(1),
\tag{25}
\]

且 `c_X asymp B_X/M`，则该 packet 的 signed response 为 `o(B_X)`。式 (25)
是充分条件，不被当作新公理；它是下一算术估计的一个可独立证伪版本。

## 6. `theta=3/4` 的 determinant mesh

在 balanced box

\[
 a,b,c,d\asymp X^{3/4},
 \qquad R=bc\asymp X^{3/2},
 \qquad H=R/X\asymp X^{1/2},
\tag{26}
\]

写 `ad=bc+r`。对 fixed `A` 与 `|r|<=AH`，

\[
 t=X\log\left(1+\frac r{bc}\right)
 =\frac rH+O_A(X^{-1}).
\tag{27}
\]

所以相邻 determinant layers 在 `t` 坐标中的 mesh 是

\[
 H^{-1}\asymp X^{-1/2}.
\tag{28}

它趋于零；resolution core 采样的是越来越稠密的 `[-1,1]`，不是有限个孤立
shift。若 weighted layer mass 在这个 mesh 上局部平坦，式 (4) 预测 core 为正，
而式 (12) 同时要求外层补偿。真正可证伪的问题因而是 layer-mass discrepancy，
而不是 support 是否重叠或 core 是否非空。

## 7. 修正后的下一最小引理 234-F [O]

固定 `theta=3/4` 与一个窄 balanced factor/aperture cell。对式 (16) 的实际
四-von-Mangoldt、six-window response measure，证明下列二者之一：

1. **mesoscopic flatness**：在覆盖完整有效 ratio range 的 `t`-packets 上建立
   式 (25)，并给出可对全部 packets 求和的 charge/边界账本；
2. **band obstruction**：在频带 `1<=|xi|<=2` 上证明式 (19) 保持固定符号且
   总量为 `gg N`，其中 lower bound 必须同时包含 core 与 tail。

不得再以 `|t|<=1` 的单独正 lower bound 作为止损条件；也不得用逐 determinant
absolute count、window-only overlap 或任意 Farey coefficients替代 `mu_X`。

第一攻击点可取 determinant block 长度 `H=X^(1/2)`：证明带
`W_{a,b;c,d}` 的 layer cumulative weight 在每个 `H`-block 相对于其局部平均的
discrepancy 小于 block mass 的一个对数因子。若连无权或平窗版本都显示固定比例
discrepancy，再转向 band obstruction。

## 8. 公理作用、删除审计与循环性

1. **实际高度 `T=2pi X`**：把频带从 baseband 移到 `[1,2]`。删除 carrier
   会得到非零总质量的低频 sinc，完全改变 core--tail 结论。
2. **consecutive Gabor samples**：给式 (7) 的均匀 frequency band。任意抽样
   集不自动具有式 (11)。
3. **six-window positivity**：使 `mu_X` 为正测度；它不推出频带 Fourier
   coefficient 为正。
4. **四个 von Mangoldt weights 与 cells**：全部保留在 `mu_X` 中；式 (21)
   没有假装已经证明其 discrepancy。
5. **`D/(XL)->1`**：决定极限 band 恰为 `[1,2]`；其他密度给不同但仍远离零的
   band，须重新归一化。

删除审计：

- 只保留 sinc envelope 会丢掉 `cos(3pi t)`，并把零总质量误读为正总质量；
- 只估 core 会错过式 (12) 的 universal compensating tail；
- 只知道 total incidence 的 natural upper bound 不给式 (20)；
- 把式 (25) 称为已知算术事实会循环地隐藏当前缺口。

循环性审计：全部 [T]/[N] 结论来自有限 Gabor 几何、Fourier transform、
Stieltjes 分部积分与 elementary logarithm expansion；不调用 RH/GRH、零点比例、
Hardy--Littlewood 渐近、Weil positivity、谱酉性或 bounded negative index。

## 9. 模型范围与部分 Weil 接口

- Riemann zeta：式 (17)--(19) 直接作用于当前 alternating response。
- Dirichlet `L`：角色相位会使 `mu_X` 不再为正；exact band identity仍成立，
  discrepancy bridge须改为 signed variation版本。
- Dedekind/automorphic `L`：band geometry不变，算术测度改由局部系数构成。
- 函数域：连续 `t` 变为 degree lattice；若频带与 lattice alias 相交，零质量
  结论必须重新检查，不能形式照搬。
- 无 Euler product 模型：定理 234-A--C 仍是 response geometry，但没有式
  (16) 的 determinant factorization。

在部分 Weil 配置中，定理 234-D 把 finite response Gram 的缺口转成一个明确的
非零频带 arithmetic discrepancy；障碍推论 234-C 防止把局部正性误当成完整
Weil 正性或负迹 lower bound。

## 10. 可复现审计 [E]

脚本 `scripts/power_high_bandpass_audit.py` 检查：

1. exact finite centered formula 与式 (2) 的局部一致收敛；
2. `c_0=0.023558003094...` 及 symmetric tail 的补偿趋势；
3. `theta=3/4` determinant mesh、式 (27) 与平坦 lattice core/tail 模型。

脚本只审计 response geometry 和模型 discrepancy，不计算真实四素数渐近。
