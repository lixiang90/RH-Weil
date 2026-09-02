# 226. Archimedean 背景的零频 Toeplitz 主部与四迹稳定归约

日期：2026-09-02

分支：MOM-1 / 路线 A1e；接口：显式公式型部分 Weil 配置

状态：显式公式中的 \(\mu,\Pi_X\) 分解为 [R]；背景矩阵的零频 Toeplitz
主部、算子范数余项和第四迹稳定归约为 [T]；deterministic mixed-diagonal
window functional 的有限代数为 [T]；把所有非零 mixed frequencies 压到
\(o(N)\) 为 [O]；Montgomery--Taylor 候选常数为 [E]。

## 1. 结论

笔记 225 把四矩主线的开放部分缩到中心化背景 \(A\) 至少出现一次的 mixed
words。本轮证明该背景不是一个需要任意 continuum Bessel bound 的大通道。
在 Alpöge--Furman 的显式公式中

\[
 \nu_X(\tau)=\mu(\tau)+\Pi_X(\tau)+P_X(\tau),
\tag{1}
\]

\[
 \mu(\tau)=\frac1{2\pi}\operatorname{Re}
 \frac{\Gamma'}{\Gamma}\!\left(\frac14+\frac{i\tau}{2}\right)
 -\frac{\log\pi}{2\pi},
 \qquad
 \Pi_X(\tau)=\frac1\pi\operatorname{Re}
 \frac{X^{1/2+i\tau}}{1/2+i\tau}.
\tag{2}
\]

令 \(L=\log X\)，冻结 \(t\asymp X\) 的 Gabor 格点和维数
\(d\asymp XL\)。把 \(\mu+\Pi_X\) 产生的有限矩阵记为 \(B_{\rm ar}(t)\)。
则

\[
 \boxed{
 B_{\rm ar}(t)
 =\frac1aT_d(\phi^2)+E_{\rm ar}(t),
 \qquad
 \|E_{\rm ar}(t)\|\ll\frac1L,}
\tag{3}
\]

一致于长度 \(X/\sqrt L\) 的冻结高度区间。中心化以后

\[
 A(t):=B_{\rm ar}(t)-I
 =S_L+E_{\rm ar}(t),
 \qquad
 S_L:=T_d\!\left(\frac{\phi^2}{a}-1\right).
\tag{4}
\]

因此 Gamma 与 pole-absorption 背景的真正主部只是一个确定性的**零频
Toeplitz window symbol**。若 \(P(t)\) 是 pure-prime Hermitian response，
则在笔记 225 的共同高度上

\[
 \boxed{
 \operatorname{tr}(A(t)+P(t))^4
 =\operatorname{tr}(S_L+P(t))^4+o(N).}
\tag{5}
\]

式 (5) 无条件消去了 \(\mu-L/(2\pi)\) 与 \(\Pi_X\) 的 fourth-trace 影响；
没有分别对 mixed words 取绝对值，也没有假设全局 Weil positivity。

剩余 mixed problem 因而从“Gamma/continuum 任意响应 Gram”严格缩为

\[
 \operatorname{tr}(S_L+P)^4,
\tag{6}
\]

其中 \(S_L\) 已知、无高度相位、算子范数一致有界。尚未证明的是式 (6) 中
非零 prime frequencies 全部为 \(o(N)\)，以及 surviving two-prime diagonal
的极限常数。

## 2. 有限 Archimedean 矩阵

沿用笔记 204、225。令

\[
 f_k(\tau)=\widehat\phi(\tau-\alpha_k),
 \qquad
 \alpha_k=t+\frac{2\pi k}{L},
 \qquad 0\le k<d,
\tag{7}
\]

并定义

\[
 (B_{\rm ar}(t))_{jk}
 =\frac1{aL^2}\int_{\mathbb R}
 f_j(\tau)f_k(\tau)
 [\mu(\tau)+\Pi_X(\tau)]\,d\tau.
\tag{8}
\]

笔记 204 的零频响应恒等式给

\[
 R_t(0)=\frac1{aL^2}\int_{\mathbb R}
 \mathbf f(\tau)\mathbf f(\tau)^*d\tau
 =\beta_LT_d(\phi^2),
 \qquad \beta_L=\frac{2\pi}{aL}.
\tag{9}
\]

取

\[
 c_X=\frac{L}{2\pi}.
\]

则 \(c_XR_t(0)=a^{-1}T_d(\phi^2)\) 精确成立。于是式 (3) 等价于估计

\[
 E_{\rm ar}(t)
 =\frac1{aL^2}\int_{\mathbb R}
 \mathbf f(\tau)\mathbf f(\tau)^*
 r_X(\tau)\,d\tau,
\tag{10}
\]

其中

\[
 r_X(\tau)=\mu(\tau)+\Pi_X(\tau)-\frac{L}{2\pi}.
\tag{11}
\]

## 3. Archimedean remainder 的算子范数 [T]

### 定理 226-A（zero-frequency background approximation）

设 \(t\asymp X\)，格点区间包含于 \([cX,CX]\)，窗口满足笔记 204 的
uniform \(C^2\) 假设。则式 (3) 成立，隐含常数只依赖固定的
\(c,C,\phi\) 正则性。

#### 证明

对 \(z\in\mathbb C^d\)，置

\[
 g_z(\tau)=\sum_{k=0}^{d-1}z_kf_k(\tau).
\]

临界 Gabor 正交性给

\[
 \int_{\mathbb R}|g_z(\tau)|^2d\tau
 \le2\pi L\|z\|^2.
\tag{12}
\]

取一个固定扩大的正区间

\[
 J=[cX/2,2CX].
\]

由 Stirling 公式和式 (2)，在 \(J\) 上一致有

\[
 |\mu(\tau)-L/(2\pi)|\ll1,
 \qquad
 |\Pi_X(\tau)|\ll X^{-1/2}.
\tag{13}
\]

所以 \(J\) 内对式 (10) 的二次型贡献由式 (12) 控制为

\[
 \frac1{aL^2}\int_J|r_X(\tau)||g_z(\tau)|^2d\tau
 \ll L^{-1}\|z\|^2.
\tag{14}
\]

对 \(J^c\)，窗口 Fourier envelope 为

\[
 |f_k(\tau)|\le
 \vartheta(\tau-\alpha_k),
 \qquad
 \vartheta(u)\ll\min(L,|u|^{-1},|u|^{-2}).
\tag{15}
\]

且 \(|\tau-\alpha_k|\gg X+|\tau|\) 在远端分块后成立。Cauchy--Schwarz 给

\[
 |g_z(\tau)|^2
 \le\|z\|^2\sum_{k<d}\vartheta(\tau-\alpha_k)^2.
\tag{16}
\]

Stirling 与式 (2) 还给

\[
 |r_X(\tau)|
 \ll L+\log^+(|\tau|/X)+\frac{\sqrt X}{1+|\tau|}.
\tag{17}
\]

把 \(J^c\) 分成 \(|\tau|\le O(X)\) 与 dyadic far tails，使用
\(\vartheta(u)^2\ll|u|^{-4}\)，逐个 \(k\) 积分后得到

\[
 \int_{J^c}|r_X(\tau)|
 \vartheta(\tau-\alpha_k)^2d\tau
 \ll \frac L{X^3}+\frac{L}{X^{7/2}}.
\tag{18}
\]

由于 \(d\asymp XL\)，式 (16)--(18) 的总和除以 \(aL^2\) 为
\(O(X^{-2})\|z\|^2\)。与式 (14) 合并，

\[
 |\langle E_{\rm ar}(t)z,z\rangle|
 \ll L^{-1}\|z\|^2.
\]

\(E_{\rm ar}(t)\) 为 Hermitian，故式 (3) 成立。\(\square\)

这里没有把 \(\Pi_X\) 的全局 supremum \(O(\sqrt X)\) 用在整个实线上；
它只在靠近原点时大，而该区域与所有正高度 Gabor centers 相距 \(\asymp X\)，
式 (15) 支付这一距离。删除该 localization 会退回笔记 200 的过粗
\(B_0=L+4\sqrt X\) 算子范数。

## 4. 第四迹稳定 [T]

### 定理 226-B（Archimedean fourth-trace evacuation）

假设某高度 \(t\) 满足

\[
 \operatorname{tr}P(t)^4=O(N).
\tag{19}
\]

则式 (5) 成立，一致于笔记 225 的共同高度集合。

#### 证明

令 \(H_0=S_L+P(t)\)、\(E=E_{\rm ar}(t)\)。因为

\[
 \|S_L\|\le\left\|\frac{\phi^2}{a}-1\right\|_\infty=O(1),
 \qquad d\asymp N,
\]

所以 \(\|S_L\|_4=O(N^{1/4})\)。式 (19) 与 \(P=P^*\) 给
\(\|P\|_4=O(N^{1/4})\)，故

\[
 \|H_0\|_4=O(N^{1/4}).
\tag{20}
\]

定理 226-A 给

\[
 \|E\|_4\le d^{1/4}\|E\|=O(N^{1/4}/L).
\tag{21}
\]

非交换 telescoping 与 Schatten Hölder 因而给

\[
 |\operatorname{tr}(H_0+E)^4-\operatorname{tr}H_0^4|
 \ll \|E\|_4(\|H_0\|_4+\|E\|_4)^3
 \ll \frac NL=o(N).
\]

这证明式 (5)。\(\square\)

定理 226-B 使用的是笔记 225 已证明的 pure-prime \(P^4=O(N)\)，不是先
假设完整 centered fourth moment。因而没有把待证 mixed estimate 循环放入前提。

## 5. Deterministic mixed-diagonal functional [T/C]

令 scaled window \(v\in[-1/2,1/2]\)，并置

\[
 s(v)=\frac{\psi(v)}a-1,
 \qquad
 Q_r(v)=\psi(v)\psi(r-v),
\tag{22}
\]

所有函数零延拓。定义

\[
 D_0(\psi)=\int_{-1/2}^{1/2}s(v)^4dv,
\tag{23}
\]

\[
 C_1(r)=\int_{\mathbb R}s(v)^2Q_r(v)dv,
 \qquad
 C_2(r)=\int_{\mathbb R}s(v)s(v-r)Q_r(v)dv,
\tag{24}
\]

以及

\[
 \boxed{
 D_{\rm mix}(\psi)
 =\frac1{a^2}\int_0^1r[8C_1(r)+4C_2(r)]dr.}
\tag{25}
\]

式 (25) 的系数来自精确 cyclic ledger

\[
 4\operatorname{tr}(S_L^2P^2)
 +2\operatorname{tr}(S_LPS_LP).
\tag{26}
\]

在两个 prime signs 相反且 prime powers 相同的 diagonal 上，前一项的两个
orientations 给 \(2C_1\)，后一项的两个 orientations 给 \(2C_2\)。再用

\[
 L^{-2}\sum_{n\le e^L}\frac{\Lambda(n)^2}{n}
 \delta_{\log n/L}\Longrightarrow r\,dr
\tag{27}
\]

和 \(\beta_L^2d/(4\pi^2)\sim N/(a^2L^2)\)，得到式 (25)。这是 surviving
two-prime diagonal 的确定性候选极限；有限 Toeplitz crossing 对该 diagonal
只有 \(O(1+\log L)=o(N)\)。

若进一步证明所有含 \(S_L\) 的非零 prime-frequency words 总和为 \(o(N)\)，
则得到条件性归约

\[
 \boxed{
 b_4
 =D_0(\psi)+D_{\rm mix}(\psi)+D_{22}(\psi)+o(1).}
\tag{28}
\]

式 (28) 当前标记为 [C]，因为 mixed one-/three-prime words 与 two-prime
off-diagonal 尚未完成统一短高度证明；不能用下面的数值把它升级为定理。

## 6. 数值尺度 [E]

对平窗 \(\psi=1\)，有 \(a=1,s=0\)，所以

\[
 D_0=D_{\rm mix}=0,
 \qquad D_{22}=4/15.
\]

对 Montgomery--Taylor 窗
\(\psi(v)=\cos(\sqrt2v)\)，Gauss--Legendre quadrature 给

\[
 \begin{aligned}
 a&=0.918725369866\ldots,\\
 D_0&=0.0000787874\ldots,\\
 D_{\rm mix}&=0.0078407992\ldots,\\
 D_0+D_{\rm mix}+D_{22}&=0.2525089687\ldots.
 \end{aligned}
\tag{29}
\]

这个数值接近 sine-kernel 的 \(1/4\)，但只是式 (28) 条件下的候选常数，
不是无条件第四矩，也不是新的零点比例。特别地，本项目仍遵守：\(13/18\)
只作为四矩匹配假设下的条件性目标；\(16/21\) 的 rank--inertia 界也不能在
算术 mixed ledger 完成前套用。

## 7. 最小公理与删除审计

1. **Stirling local flatness**：把 \(\mu\) 的主部识别为 \(L/(2\pi)\)。删除后
   背景不能化为零频 Toeplitz symbol。
2. **positive-height localization**：使 \(\Pi_X\) 的 \(O(\sqrt X)\) 峰值与 Gabor
   centers 相距 \(\asymp X\)。若只用全局 supremum，式 (3) 失败。
3. **critical Gabor Plancherel**：给式 (12) 的 dimension-free local bound。
4. **window \(C^2\) decay**：负责式 (18) 的远端可积性。sharp cutoff 只有
   \(1/|u|\) decay，必须另做边缘账本。
5. **pure-prime fourth bound**：只在定理 226-B 中提供
   \(\|P\|_4=O(N^{1/4})\)；它已由笔记 225 的 prime-side 共同高度定理给出。
6. **mixed-frequency cancellation**：不在本轮公理中偷偷假设；它明确保留为
   式 (28) 的开放输入。

结论不是 RH 的改写。式 (3) 只使用 Archimedean 显式公式、Stirling、窗口
Fourier decay 和有限矩阵范数；式 (5) 只使用已独立证明的 pure-prime fourth
budget。没有读取任何零点的实部。

## 8. 模型范围与 Weil 接口

- Riemann zeta：式 (1)--(5) 直接适用。
- 固定本原 Dirichlet \(L\)：Gamma shift 与 conductor 常数只改变
  \(c_X\) 的 \(O(1)\) 部分，仍进入 \(E_{\rm ar}=O(1/L)\)；pole term 消失。
- Dedekind/automorphic \(L\)：有限 degree Gamma factors 的主部仍为
  \(c_L L\)，但 \(c_L\) 与中心化单位需要按 analytic conductor 重标。
- 函数域：没有 Archimedean Gamma 背景；对应 \(S_L\) 来自离散 Frobenius
  sampling normalization，不能直接引用本定理。
- 类 RH 失败但有函数方程的模型：Archimedean reduction 仍可能成立；它本身
  不蕴含任何中心线结论。

本轮属于显式公式型 Weil 配置的 finite-background bridge。它没有构造
Frobenius、极化或 Hard Lefschetz，也没有建立上同调型与显式公式型结构的等价。

## 9. 下一最小引理 [O]

证明 **deterministic-background mixed-frequency evacuation**：在每个长度
\(X/\sqrt L\) interval 上，把含 \(S_L\) 的所有 mixed words 分成：

1. zero-prime main \(D_0N\)；
2. balanced two-prime diagonal \(D_{\rm mix}N\)；
3. one-prime、two-prime off-diagonal、three-prime signed remainder \(o(N)\)。

最小独立算术输入应是 one-prime/two-prime shifted upper bound

\[
 \sum_{R<n\le2R}\Lambda(n)(\Lambda*\Lambda)(n+h)
 \ll \Delta(h)R\log R(\log\log R)^3+R\log R,
\tag{30}
\]

加 one-prime/one-prime analog。它可望由笔记 224 的 Henriot 双参数方法以
\(\Omega=1,2\) 重证；在完成前不得把式 (28)--(29) 写入无条件结论链。

## 10. 可复现检查 [E]

脚本 `scripts/archimedean_background_audit.py` 检查：

1. zero-frequency coefficient \(c_X\beta_L=1/a\)；
2. Schatten--4 perturbation 的 \(N/L\) 尺度；
3. 式 (25) 的 orientation coefficients；
4. 平窗与 Montgomery--Taylor 窗的 \(D_0,D_{\rm mix}\) 收敛；
5. 条件候选常数只标记为 [E]/[C]。

脚本不证明式 (18)、mixed-frequency evacuation 或任何零点比例。
## 11. 后续推进（笔记 227）

笔记 227 已用 Omega=1,2 的 Henriot shifted sieve 闭合本笔记第 9 节留下的 one-prime、two-prime off-diagonal 与 three-prime mixed frequencies，并证明 finite Toeplitz crossing 总量同样为 o(N)。共同高度选择不能先固定 pure-prime good point；正确做法是先平均整个非负 tr(S_L+P)^4，只选一次高度，再从选中的 whole trace 反推 Schatten--4 控制并消去 E_ar。MT centered fourth constant 因而成为 0.2525089687，但到全局零点比例的 relative-dense 量词接口仍为开放审计。

## 12. 后续逆审计（笔记 230）

笔记 230 从四个 cyclic slots 中直接选择两个 prime positions：四个 adjacent
placements 与两个 alternating placements，各乘两种 opposite-sign orientation，
独立恢复本笔记式 (25) 的 `8C_1+4C_2`。其独立 quadrature 同时重算
`D_0=0.000078787511...`、`D_mix=0.007840799168...`；未发现 mixed-diagonal
orientation 或 normalization 错误。
