# 245. Scalarized response spectrum、宽 ratio band 与 one-sided arc certificate

日期：2026-09-03

分支：NCE-8 / 路线 B1；接口：degree-two common multiplier / symmetric
prime--continuum spectral overlap

状态：divided-difference Fourier scalarization、绝对高频尾界及有限好弧的一侧
capture principle 为 [T]；真实 finite zeta ratio-band quadrature为 [E]；固定参数
good-arc certificate 与其 dyadic arithmetic propagation为 [O]。本笔记不更新 PDF，
不声称 RH/GRH、uniform B1a 或新的零点比例。

## 1. 研究结论

笔记 244 将 physical prime--continuum correlation精确写成

\[
 P=\int W_p^2d\omega_R,
 \qquad
 C=\int W_c^2d\omega_R,
 \qquad
 z=-\int W_pW_cd\omega_R.
\tag{1}
\]

B1 的剩余目标是证明实际 response weight下 `W_p,W_c` 有统一定量 overlap。本轮
得到三项进展：

1. common divided-difference multiplier无需展开四次 formal convolution；每个
   Fourier character上它精确等于一个 scalar polynomial `Q(d-hat)`；
2. 总变差给出完全显式的高频尾界，但真实 finite 数据中该界比 exact diagonal大
   `37--41` 倍，不能认证观察到的 `98%--99%` 数值覆盖；
3. 由于 ratio-band energy非负且 exact total diagonal已由 Brownian Gram给出，
   证明 capture不需要控制整个尾：只需在有限多个已验证 good arcs上给出足够大的
   **one-sided lower bound**。

finite quadrature显示宽 band `1/4<=W_p/W_c<=4` 对 exact diagonal捕获约
`0.51--0.70`，continuum mesh从 2 格细化到 4 格后没有消失；相反，窄 band
`3/4<=W_p/W_c<=4/3` 在 `scale=16` 只捕获约 `0.0065`。因此停止追求
`W_p/W_c approximately 1`，保留宽 ratio-band路线。

## 2. Degree-two multiplier 的 Fourier scalarization

令 `d` 为 finite lag algebra中的完整 symbol，

\[
 M=d(\mathbb R),
 \qquad
 \ell=\frac{\sqrt3}{2}B,
\tag{2}
\]

其中 `B` 是 spectral bound。笔记 242 的 common divided difference为

\[
\begin{aligned}
 R_{M,\ell}(d)
 ={}&d^{*4}+(M-2\ell)d^{*3}+(M-\ell)^2d^{*2}\\
 &+M(M-\ell)^2d+M^2(M-\ell)^2\delta_0.
\end{aligned}
\tag{3}
\]

定义 scalar polynomial

\[
 Q_{M,\ell}(X)=X^4+(M-2\ell)X^3+(M-\ell)^2X^2
 +M(M-\ell)^2X+M^2(M-\ell)^2.
\tag{4}
\]

### 定理 245-A（characterwise scalarization）[T]

对每个 Fourier character `chi_xi(x)=exp(-i xi x)`，

\[
 \boxed{
 \widehat{R_{M,\ell}(d)}(\xi)
 =Q_{M,\ell}(\widehat d(\xi)).}
\tag{5}
\]

因此 degree-two response weight为

\[
 d\omega_R(\xi)=
 \frac{|\gamma|^2
 |Q_{M,\ell}(\widehat d(\xi))|^2}
 {2\pi\xi^2}\,d\xi,
\tag{6}
\]

其中 `gamma` 是 common response scalar。

#### 证明

Fourier character是 convolution algebra homomorphism：

\[
 \widehat{d^{*j}}(\xi)=\widehat d(\xi)^j,
 \qquad \widehat{\delta_0}(\xi)=1.
\]

逐项作用于式 (3)即得式 (5)，再代入笔记 244-(7)。`square`

这不是近似。计算式 (6)只需评价 base symbol `d-hat`，复杂度关于 base atoms线性，
不需要物化 `d^{*4}` 的组合支持。exact Brownian Gram仍可在小模型中独立验证
normalization；大模型应以式 (5)为主计算路径。

## 3. 一个严格但过粗的 absolute tail bound

设

\[
 S=\|d\|_{TV},
\tag{7}
\]

并令 `A_*`,`B_*` 分别为产生 `W_p,W_c` 的非零 lag正 measures的总质量。因此

\[
 0\le W_p\le2A_*,
 \qquad
 0\le W_c\le2B_*.
\tag{8}
\]

置

\[
\begin{aligned}
 Q_*={}&S^4+|M-2\ell|S^3+|M-\ell|^2S^2\\
 &+|M||M-\ell|^2S+|M|^2|M-\ell|^2.
\end{aligned}
\tag{9}
\]

### 定理 245-B（supremum high-frequency tail）[T]

对任意 `T>0`，

\[
\boxed{
 \int_{|\xi|>T}(W_p^2+W_c^2)d\omega_R
 \le
 \frac{4|\gamma|^2Q_*^2(A_*^2+B_*^2)}{\pi T}.}
\tag{10}
\]

同样有

\[
 \int_{|\xi|>T}W_pW_cd\omega_R
 \le\frac{4|\gamma|^2Q_*^2A_*B_*}{\pi T}.
\tag{11}
\]

#### 证明

由 `|d-hat(xi)|<=S` 与式 (4)的三角不等式，

\[
 |Q_{M,\ell}(\widehat d(\xi))|\le Q_*.
\]

再用式 (8)及

\[
 \int_{|\xi|>T}\frac{d\xi}{2\pi\xi^2}=\frac1{\pi T}
\]

分别得到式 (10)--(11)。`square`

定理 245-B 是真正的解析 upper bound，但它完全丢失 `Q(d-hat)` 的平均相消和
prime/continuum ratio geometry。下文数据表明，在当前 normalization中它不能作为
B1c 的实际证书；这只是对该 finite family 的 [E] 结论，不宣称任何 supremum方法
在所有模型中都必然失败。

## 4. Tail-free 的 one-sided good-arc principle

令 exact Brownian diagonal为

\[
 D=P+C.
\tag{12}
\]

固定 `0<m<=M_0<infinity`，定义 good ratio set

\[
 G=\{\xi:m\le W_p(\xi)/W_c(\xi)\le M_0\}.
\tag{13}
\]

### 定理 245-C（finite good arcs suffice globally）[T]

设 `I_1,...,I_J` 是 `G` 内两两不交的 bounded intervals。若可独立认证

\[
 \sum_{j=1}^J
 \int_{I_j}(W_p^2+W_c^2)d\omega_R
 \ge\kappa D
\tag{14}
\]

for some `kappa>0`，则无需估计 `union I_j` 外的高频或坏 ratio部分，已有

\[
 \int_G(W_p^2+W_c^2)d\omega_R\ge\kappa D.
\tag{15}
\]

进而由笔记 244-D，

\[
 \boxed{
 -z\ge
 \kappa
 \min\left\{\frac m{1+m^2},
 \frac{M_0}{1+M_0^2}\right\}(P+C).}
\tag{16}
\]

#### 证明

式 (6)中所有 energy densities非负，故删除 `G minus union I_j` 只能减小左端；
式 (14)给式 (15)。再应用笔记 244-D。`square`

这个方向绕过了定理 245-B 的大 tail constant。关键不是证明 quadrature覆盖整个
谱，而是用 exact denominator `D` 认证一批有限好弧已经携带固定比例能量。

### 推论 245-D（interval enclosure template）[T]

若每个 interval `I_j=[alpha_j,beta_j]` 上有可核查 bounds

\[
 0<p_j^-\le W_p\le p_j^+,
 \qquad
 0<c_j^-\le W_c\le c_j^+,
 \qquad
 |Q_{M,\ell}(\widehat d)|\ge q_j^-,
\tag{17}
\]

并且

\[
 p_j^-\ge m c_j^+,
 \qquad
 p_j^+\le M_0c_j^-,
\tag{18}
\]

则 `I_j subset G`，且在 positive half-line `0<alpha_j<beta_j` 时

\[
\begin{aligned}
 \int_{I_j}(W_p^2+W_c^2)d\omega_R
 \ge{}&
 \frac{|\gamma|^2(q_j^-)^2}{2\pi\beta_j^2}\\
 &\cdot\bigl((p_j^-)^2+(c_j^-)^2\bigr)
 (\beta_j-\alpha_j).
\end{aligned}
\tag{19}
\]

若 integrand为 even（当前 real two-sided zeta symbol与 multiplier正是如此），同时
加入 reflected interval `-I_j` 后右端乘二。一般 complex multiplier下不得自动
使用该倍增。式 (19)直接来自各因子的 pointwise lower bounds；它给下一轮
interval-arithmetic实现的严格目标。

## 5. Finite zeta ratio-band evidence [E]

`scripts/vaughan_spectral_ratio_capture_audit.py` 使用定理 245-A直接评价
`Q(d-hat)`，以 positive-frequency midpoint quadrature积分到 `T=256`、步长
`0.01`。它同时用 exact Brownian Gram核对 `P+C,z` normalization。

下表的 capture均除以 exact `D=P+C`，不是除以截断积分；`coverage` 是截断
spectral diagonal除以 exact diagonal。

| scale, cutoff | continuum cells | coverage | cross coverage | `[1/4,4]` | `[1/2,2]` | `[3/4,4/3]` | crude tail / `D` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 8, 10 | 2 | 0.9800 | 0.9865 | 0.511 | 0.331 | 0.271 | -- |
| 8, 10 | 4 | 0.9854 | 0.9904 | 0.585 | 0.537 | 0.409 | 37.24 |
| 16, 15 | 2 | 0.9871 | 0.9936 | 0.668 | 0.483 | 0.0069 | -- |
| 16, 15 | 4 | 0.9912 | 0.9953 | 0.702 | 0.576 | 0.0065 | 41.25 |

结论仅为 finite evidence：

1. scalarized integral重构 exact Gram至约 `1%--2%`，支持 normalization正确；
2. 宽 `[1/4,4]` band在两尺度、两 meshes上保留 substantial energy；
3. 窄 `[3/4,4/3]` band不稳定并在 scale 16近乎消失，故停止该目标；
4. 总变差 supremum tail虽严格，却比 exact diagonal大几十倍，不能认证 coverage；
5. midpoint values不是 interval proof，表中 capture不得升级为定理 245-C 的
   hypothesis。

尝试把 continuum mesh增至 8 或把 integer cutoff显著增大时，旧实现为取得 exact
Gram仍物化四次 formal convolution，支持迅速膨胀。该运行被主动停止；这不是
算术反例。定理 245-A 已给出后续避免组合爆炸的正确实现路径。

## 6. 下一最小引理 B1d [O]

固定宽 band

\[
 m=\frac14,
 \qquad M_0=4.
\tag{20}
\]

在每个目标 finite block上自动生成一族 disjoint good arcs，并以式 (17)--(19)的
interval enclosures认证

\[
 \sum_j\int_{I_j}(W_p^2+W_c^2)d\omega_R
 \ge\kappa(P+C)
\tag{21}
\]

for one fixed experimental `kappa>0`。第一阶段只要求有限、机器可核查的有理/区间
证书；第二阶段才研究 `kappa` 对 scale 的解析一致性。

实现必须：

1. 直接评价 `Q(d-hat)`，不展开 `d^{*4}`；
2. 用导数或 interval arithmetic认证整个 arc，而非采样点；
3. 以 exact Brownian Gram diagonal作 denominator；
4. 只累计已验证落入 `[1/4,4]` 的 arcs；
5. 将 quadrature coefficient误差与 continuum tail单独列账。

晋级条件：在增长的 finite scales上取得非退化 certified `kappa`，并把其唯一未证
uniformity归约到明确的 prime/continuum exponential-sum estimate。止损条件：若
certified `kappa` 随 mesh和 scale一致趋零，或 good arcs系统地向逃逸频率移动，则
用其形成 actual-symbol版本的 spectral escape obstacle，并停止 uniform B1a。

## 7. 公理、删除审计与循环性

定理 245-A 只用 convolution character；245-B 增加 total variation；245-C--D只用
positive spectral density、exact denominator和 interval lower bounds。

删除审计：

- 删除 common multiplier，式 (6)没有单一绝对平方；
- 删除 two-sided sign theorem，ratio-band之外的 cross可为负贡献，245-C不能只靠
  删除坏集；
- 删除 exact denominator，只证明截断能量中的比例不能推出 global capture；
- 用 midpoint samples替代 interval enclosures，式 (14)没有严格证书；
- 只用 `Q_*` 而不利用 actual `Q(d-hat)`，finite证书被表中的 `37--41` 倍损失阻断；
- 将宽 band收缩到 ratio 1附近，finite表给出直接反证证据。

非同义反复审计：245-A 是 exact complexity reduction；245-B 是独立可计算上界；
245-C--D 是 one-sided certification theorem。式 (21)仍是未证输入，明确标为 [O]；
本轮没有把数值 capture当成 uniform positivity。

循环性审计：全部 [T] 只用 finite convolution、Fourier characters、三角不等式与
非负积分；不使用 RH/GRH、Weil positivity、谱酉性、PNT error、Mertens平方根界或
bounded negative index。

## 8. 模型范围与论文接口

- **Riemann zeta**：245-A--D适用于当前 sign-pure finite prime/continuum response；
  B1d 是下一可执行任务。
- **Dirichlet/automorphic L**：若 coefficients带相位，须先建立 matrix-valued或
  family-averaged sign bridge，才能使用 one-sided deletion。
- **Dedekind zeta**：nonnegative ideal von Mangoldt atoms允许同型 scalarization；
  多 Gamma channels需扩成 vector ratio cone。
- **函数域**：finite cyclic degree character使 scalarization更直接，可作为 interval
  certificate的正向基准。
- **负向模型**：若没有 common absolute-square weight，245-C的好弧删除原则失效。
- **论文归属**：245-A--D 与 242--244 属于 Vaughan--Brownian response独立论文；
  不并入四矩比例或上同调 Weil 结构论文。

本轮将 B1c 从“证明整个频谱上的 uniform comparability”缩成了更弱且可独立认证的
有限好弧 lower-bound问题。绝对 tail不够小并不阻止这条 one-sided路线。

后续进展：笔记 246 从 atom first moments导出 `W_p,W_c,d-hat,Q(d-hat)` 的显式
Lipschitz constants，证明 midpoint verified-cell lower sums在 mesh趋零时恢复全部
strict-good energy [T]。浮点网格从 `0.01` 加密到 `0.005` 后，宽 band lower/exact
由 `0.0988/0.0252` 增至 `0.1999/0.1645` [E]。下一 gate是把 coefficients、lags、
trigonometric values与 exact denominator全部 rational interval化。
