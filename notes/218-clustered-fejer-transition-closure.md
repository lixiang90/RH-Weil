# 218. Clustered Fejér 大筛闭合 transition oscillatory tail

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 NCE-8 / alternating transition Gram

状态：six-window cone Gram identity、clustered vector-valued Fejér large-sieve
inequality、完整 transition layer closure 与全局
`ab <= X log^(2-eta) X` primitive atomic diagonalization 为 [T]；有限归一化审计为
[E]；临界 `ab asymp X log^2 X` 局部箱能量为 [O]。本笔记不更新 PDF。

## 1. 本轮结论

令

\[
 L=\log X,\qquad N=XL,
\tag{1}
\]

并固定 `0 < delta < 1`。笔记 217 已把 transition band

\[
 \mathcal T_\delta
 =\{(a,b):XL^{1-\delta}\le ab\le XL^{1+\delta}\}
\tag{2}
\]

中 determinant resolution core 的绝对主项压到 `o(N)`，但留下了
oscillatory tail。本轮证明 tail 不需要新的 shifted-prime cancellation。

关键是：translated six-window overlap 不是任意 pair weight，而是一个由
**非负向量**生成的 Hilbert Gram。对连续 Gabor height block 使用一个比原 block
宽两倍的 Fejér majorant，再把 ratio frequencies 按 `O(1/d_G)` 的圆周小箱聚类，
得到

\[
 \text{全部高度能量}
 \ \ll\ d_G\times\text{同箱正 Gram 能量}.
\tag{3}
\]

在 `h_0=2 pi/L`、`d_G asymp XL` 下，同箱意味着

\[
 \operatorname{dist}(s_i-s_j,L\mathbb Z)\ll X^{-1}.
\tag{4}
\]

普通分支正是笔记 217 已闭合的 determinant core；`+/- L` 分支的 translated
overlap 由笔记 215-F 的支撑间隙严格为零。由此得到：

### 定理 218-A（完整 transition layer closure）[T]

对每个固定 `0 < delta < 1`，Riemann zeta 的 primitive distinct-base
transition response 满足

\[
 \boxed{
 \left\|\sum_{(a,b)\in\mathcal T_\delta}
 F_{a/b}^{\rm fin}\right\|_{HS}^{2}=o(N).}
\tag{5}
\]

这包含 atomic diagonal、resolution core、oscillatory tail、Toeplitz--Hankel
remainder 与 aggregate finite/bulk transfer。特别地，笔记 217-G 的 tail
输入已经闭合。

与笔记 215-I 拼接后还有更强的全局推论。

### 推论 218-B（全局 logarithmic square-root cutoff）[T]

对每个固定 `0 < eta < 1`，令

\[
 \mathcal P_{2-\eta}(X)
 =\{(a,b):2\le a,b\le X,
 \operatorname{base}(a)\ne\operatorname{base}(b),
 ab\le XL^{2-\eta}\}.
\tag{6}
\]

则

\[
 \boxed{
 \left\|\sum_{(a,b)\in\mathcal P_{2-\eta}(X)}F_{a/b}^{\rm fin}\right\|_{HS}^{2}
 =
 \sum_{(a,b)\in\mathcal P_{2-\eta}(X)}
 \|F_{a/b}^{\rm fin}\|_{HS}^{2}+o(N).}
\tag{7}
\]

所以此前只对单个 dyadic box 已知的 `AB <= XL^(2-epsilon)` 阈值，现在对整个
primitive hyperbolic union 成立。尚未覆盖的是临界 `ab asymp XL^2` 顶层，而不再
是 `ab asymp XL` 的振荡尾。

## 2. Six-window overlap 的 cone Gram identity

把 transition atoms 编号为 `i=(a,b)`，并写

\[
 s_i=\log(a/b),\qquad c_i=b_ab_b,
\tag{8}
\]

以及笔记 216 的非负 physical symbol

\[
 P_i(u)=\phi(u)\phi(u-s_i)\phi(x_a-u)^2.
\tag{9}
\]

在长度 `L` 的圆周 `mathbb T_L` 上定义

\[
 g_i(v)=P_i(v+s_i).
\tag{10}
\]

取 normalized inner product

\[
 \langle f,g\rangle_H
 =\frac1L\int_{\mathbb T_L}f(v)\overline{g(v)}\,dv.
\tag{11}
\]

### 引理 218-C（translated overlap is a nonnegative cone Gram）[T]

对任意两个 atoms `i,j`，有

\[
 \boxed{W_{ij}=\langle g_i,g_j\rangle_H,}
\tag{12}
\]

并且 `g_i >= 0`，故 `W_ij >= 0`。

#### 证明

令 `Delta=s_i-s_j`。笔记 216-(9) 给

\[
 W_{ij}=\frac1L\int_{\mathbb T_L}P_i(u)P_j(u-\Delta)\,du.
\]

置 `u=v+s_i`，则

\[
 P_i(u)=P_i(v+s_i)=g_i(v),
\]

且

\[
 P_j(u-\Delta)=P_j(v+s_j)=g_j(v).
\]

圆周平移保持 measure，故得到式 (12)。非负性来自式 (9)。`square`

令

\[
 \theta_i=h_0s_i\pmod {2\pi},
 \qquad
 v_i=c_i e^{iTs_i}g_i.
\tag{13}
\]

笔记 216-A 因而立即给出：

### 推论 218-D（whole main symbol is one vector-valued sampled norm）[T]

对任意 transition atom subset `mathcal A`，其全部 translated-symbol main term 为

\[
 \boxed{
 K_{\mathcal A}^{\rm main}
 =\beta_L^4\sum_{k=0}^{d_G-1}
 \left\|\sum_{i\in\mathcal A}v_i e^{ik\theta_i}\right\|_H^2.}
\tag{14}
\]

因此式 (14) 非负。这个表示保留全部 atoms、physical windows、carrier height
phase 与 Gabor samples；它没有把 tail phase 删除或换成一个任意系数 Bessel
假设。

## 3. Clustered vector-valued Fejér large sieve

下面的有限维 harmonic lemma 是本轮的解析核心。它属于 classical analytic
large-sieve/Fejér majorant 的一个带 cone coefficients 的局部密度版本；为避免
引用范围歧义，这里给完整证明。历史背景可参见 Montgomery--Vaughan,
*The large sieve*, Mathematika 20 (1973), 119--134，
<https://doi.org/10.1112/S0025579300004708>。

### 定理 218-E（clustered cone large sieve）[T]

令 `H` 为 Hilbert space，`g_1,...,g_J in H` 满足

\[
 \langle g_i,g_j\rangle_H\ge0
\tag{15}
\]

且该 inner product 为实数。令 `a_i >= 0`、`|zeta_i|=1`、
`theta_i in mathbb T`。固定常数 `A>0`，置 `M=2d`，并把圆周等分成

\[
 K=\left\lceil\frac{2\pi M}{A}\right\rceil
\tag{16}
\]

个 arcs `I_p`。若 `d` 足够大，则

\[
 \boxed{
 \sum_{k=0}^{d-1}
 \left\|\sum_i zeta_i a_i g_i e^{ik\theta_i}\right\|_H^2
 \le C_A d\sum_{p=0}^{K-1}
 \left\|\sum_{\theta_i\in I_p}a_i g_i\right\|_H^2.}
\tag{17}
\]

常数 `C_A` 只依赖固定的 arc multiplier `A`，与 `d,J`、频率 multiplicities
及 carrier phases 无关。

#### 证明

记

\[
 V_k=\sum_i zeta_i a_i g_i e^{ik\theta_i}.
\tag{18}
\]

Fejér kernel

\[
 \mathcal F_M(x)
 =\sum_{|k|<M}\left(1-\frac{|k|}{M}\right)e^{ikx}
 =\frac1M\left|\sum_{r=0}^{M-1}e^{irx}\right|^2
\tag{19}
\]

逐点非负。因 `M=2d`，对 `0<=k<d` 有

\[
 1-\frac{k}{M}\ge\frac12.
\]

所以

\[
 \sum_{k=0}^{d-1}\|V_k\|_H^2
 \le2\sum_{|k|<M}\left(1-\frac{|k|}{M}\right)\|V_k\|_H^2.
\tag{20}
\]

展开右端，并用 `mathcal F_M >= 0`，得到

\[
 \begin{aligned}
 \text{式 (20) 右端}/2
 &\le
 \sum_{i,j}a_i a_j
 |\langle g_i,g_j\rangle_H|
 \mathcal F_M(\theta_i-\theta_j).
 \end{aligned}
\tag{21}
\]

对每个 arc 定义正 cone aggregate

\[
 G_p=\sum_{\theta_i\in I_p}a_i g_i,
 \qquad E_p=\|G_p\|_H^2.
\tag{22}
\]

由式 (15)，对任意两个 arcs，

\[
 \sum_{\substack{\theta_i\in I_p\\\theta_j\in I_q}}
 a_i a_j|\langle g_i,g_j\rangle_H|
 =\langle G_p,G_q\rangle_H
 \le\sqrt{E_pE_q}.
\tag{23}
\]

令 `rho(p,q)` 为圆周上的 bin distance。由式 (16)，arc length 与 `A/M`
可比。再用

\[
 \mathcal F_M(x)
 \le\min\left(M,\frac1{M\sin^2(x/2)}\right)
\tag{24}
\]

及 `sin(x/2) >= x/pi`（`0<=x<=pi`），得到

\[
 \sup_{\theta\in I_p,\varphi\in I_q}
 \mathcal F_M(\theta-\varphi)
 \le \frac{C_A M}{1+\rho(p,q)^2}.
\tag{25}
\]

式 (25) 的每一行和为 `O_A(M)`。把式 (23) 代入式 (21)，再用 Schur test
或 `2sqrt(E_pE_q)<=E_p+E_q`，得到

\[
 \sum_{|k|<M}\left(1-\frac{|k|}{M}\right)\|V_k\|_H^2
 \le C_A M\sum_pE_p.
\tag{26}
\]

结合式 (20) 与 `M=2d` 即得式 (17)。`square`

这里允许单个 arc 含任意多频率。传统 separated-frequency large sieve 会被最小
gap 控制；式 (17) 则把 multiplicity 的全部代价精确留在同箱正 Gram `E_p` 中。

## 4. Local circle boxes 恰落入 determinant core

对式 (14) 取定理 218-E 的 `A=8`。令 `I_p` 是式 (16) 的圆周 arcs，并记

\[
 E_p
 =\left\|\sum_{\theta_i\in I_p}|c_i|g_i\right\|_H^2.
\tag{27}
\]

同一 arc 内的两点满足

\[
 \operatorname{dist}(h_0(s_i-s_j),2\pi\mathbb Z)
 \le\frac{A}{M},
\]

故

\[
 \operatorname{dist}(s_i-s_j,L\mathbb Z)
 \le\frac{AL}{2\pi M}
 =\frac{AL}{4\pi d_G}ll X^{-1}.
\tag{28}
\]

因 `2<=a,b<=X`，每个 ratio log 位于
`[-L+log 2,L-log 2]`。所以式 (28) 只可能靠近 `0,+/-L`；`+/-2L` 与更远 aliases
被 ratio diameter 排除。

若靠近 `+/-L`，笔记 215-F 给

\[
 W_{ij}=0
\tag{29}
\]

的逐原子 translated-support gap。若靠近 `0`，置

\[
 m=ad,\qquad n=bc,\qquad \Delta=s_i-s_j=\log(m/n).
\tag{30}
\]

对充分大 `X`，式 (28) 与 mean-value theorem 给

\[
 |m-n|\le C_A\frac{\min(m,n)}X.
\tag{31}
\]

因此所有对式 (27) 有非零贡献的 off-diagonal pairs 都属于笔记 217-D 的
resolution core。

笔记 217-D 的证明实际控制了在取 `|D_d|<=d_G` 后的更强正 majorant；于是

\[
 \begin{aligned}
 \beta_L^4d_G\sum_pE_p
 \ll_\delta{}&
 N\frac{\log L}{L}
 +N L^{-(1-\delta)/2}(\log L)^5
 +N L^{\delta-1}\notag\\
 ={}&o(N).
\end{aligned}
\tag{32}
\]

第一项是笔记 216-D 的 atomic diagonal，后两项是笔记 217-(29) 的 core
majorant。式 (32) 不是把完整 Gram positivity当成公理；其 arithmetic 部分正是
Henriot--Holowinsky discriminant-uniform upper-bound sieve 已证明的局部质量。

## 5. Transition bulk 与 finite closure

把式 (13) 代入定理 218-E，并用式 (32)，得到

\[
 K_{\mathcal T_\delta}^{\rm main}
 \le C\beta_L^4d_G\sum_pE_p=o(N).
\tag{33}
\]

所以 entire translated-symbol main Gram 已闭合。这个论证不是逐 tail shift 的
一阶导数估计；tail cancellation 由 Fejér majorant 把全部高度 samples 重新组织成
resolution-scale 的 local density 后自动包含。

还需审计 Toeplitz--Hankel 与 finite-section errors。令

\[
 Z=XL^{1+\delta}.
\tag{34}
\]

笔记 215-D 给 transition subset 的 coefficient mass

\[
 \sum_i|c_i|\ll L\sqrt Z.
\tag{35}
\]

笔记 213-D 的 trace-class factorization 对全部 atom pairs 绝对求和，给

\[
 |\mathscr H_{\rm tr}|
 \ll \beta_L^4(1+\log L)
 \left(\sum_i|c_i|\right)^2
 \ll \frac{Z(1+\log L)}{L^2}=o(N).
\tag{36}
\]

这里最后一步使用 `delta<1`。同一个 mass budget 对 aggregate finite/bulk defect
`mathcal E_delta` 给

\[
 \|\mathcal E_\delta\|_{HS}^2
 \ll\frac{Z(1+\log L)}{L^2}=o(N).
\tag{37}
\]

式 (33)、(36) 说明 bulk aggregate norm square 为 `o(N)`；再由 triangle
inequality 与式 (37)，finite aggregate norm square 也是 `o(N)`。这证明定理
218-A。

值得强调：笔记 216-I 要求对每个 cell pair 的 tail 先取绝对值，是一个充分但
过强的桥梁。定理 218-A 控制的是物理上实际出现的**整个 aggregate**，允许
Fejér/Hilbert cancellation 跨越人工 product/ratio cell 边界。因此本轮没有证明
216-(34) 那个更强的 cellwise absolute statement，也不需要它。

## 6. 与 collar 拼接

固定 `0<eta<1`，在定理 218-A 中取

\[
 \delta=1-\eta.
\tag{38}
\]

则 transition band 覆盖

\[
 XL^\eta\le ab\le XL^{2-\eta}.
\tag{39}
\]

令 `A` 为 `ab<=XL^eta` 的 primitive aggregate，`B` 为式 (39) 的 aggregate。 位于共同 cutoff 上的原子任意只分配给其中一个集合。
笔记 215-I 给

\[
 \|A\|_{HS}^2=\sum_{i\in A}\|F_i\|_{HS}^2+o(N)=O(N),
\tag{40}
\]

而定理 218-A 与笔记 216-D 给

\[
 \|B\|_{HS}^2=o(N),
 \qquad
 \sum_{i\in B}\|F_i\|_{HS}^2=o(N).
\tag{41}
\]

Cauchy--Schwarz 给 `|<A,B>|=o(N)`。将式 (40)--(41) 相加，即得推论
218-B。

## 7. Finite normalization audit [E]

脚本 `scripts/clustered_fejer_transition_audit.py` 独立检查：

1. 对随机非负 Hilbert-cone vectors、任意 carrier phases 和 clustered
   frequencies，验证式 (17) 的显式宽松常数 `200`；
2. 对实际 prime-power transition atoms、flat compact window 与 exact closed
   Dirichlet kernel，比较完整 sampled main Gram 与同箱 local mass；
3. 验证有非零 overlap 的 alias same-bin pairs 不存在；
4. 验证普通 same-bin pairs 满足 `X|ad-bc|/min(ad,bc)<=1`。

输出为：

| case | sampled main / `(d_G local mass)` | max `X|det|/min` |
|---|---:|---:|
| random, `d=8` | 0.411122 | -- |
| random, `d=16` | 0.442722 | -- |
| random, `d=24` | 0.657220 | -- |
| actual `X=120` | 0.887216 | 0.455408 |
| actual `X=200` | 0.950467 | 0.372787 |
| actual `X=300` | 0.909658 | 0.608828 |

这些数值只检查 normalization、circle bins、carrier phase 与 determinant map；
式 (17)、(32)--(41) 的渐近结论来自解析证明。

## 8. 最小公理、删除审计与循环性

1. **consecutive Gabor height block**：允许用带宽 `2d_G` 的 Fejér kernel
   majorize 所有实际 samples。若采样指标是任意稀疏集合，式 (20) 不再自动成立。
2. **translated six-window covariance**：给式 (12) 的共同 Hilbert realization。
   只知道逐项 `0<=W_ij<=1` 不足以构造 block aggregates `G_p`。
3. **nonnegative cone**：使式 (23) 中 pairwise absolute mass 等于两个正
   aggregates 的 inner product。删除后，局部 signed cancellation可能使 `E_p`
   很小而 cross-bin absolute mass很大。
4. **alias support gap**：把圆周同箱严格还原为 ordinary determinant core。
   删除后还需独立控制 `Delta near +/-L` 的 resonant local energy。
5. **discriminant-uniform core sieve**：给式 (32) 的 arithmetic little-oh。
   Fejér inequality只把全局问题压到 local density，不制造该 density saving。
6. **fixed `delta<1` transition ceiling**：使 core majorant、Hankel remainder 与
   finite defect均为 `o(N)`。在 `delta=1`，现有预算不闭合。

删除审计：

- 只使用 ordinary separated-frequency large sieve会付最小 ratio gap
  `asymp1/Z`，在 supercritical union 上过大；定理 218-E 允许频率聚类并把代价
  精确送入已控制的同箱能量。
- 逐 tail shift 取绝对值会恢复 harmonic 主尺度；本轮不这样拆散一个本来完整的
  sampled norm。
- 只知道 core absolute sum 为 `o(N)`，若没有式 (12) 的共同 Gram realization，
  不能推出 tail 小；关键桥梁是独立证明的 harmonic theorem 218-E。
- 本轮没有证明每个 product/ratio cell pair 的 tail 均小；它证明实际 aggregate
  所需且更弱的结论。

循环性审计：所有输入都在 finite prime/Gabor side。证明使用 finite Fejér
identity、Hilbert Cauchy--Schwarz、window support、已发表 upper-bound sieve 与
elementary mass estimates；不使用 RH、GRH、零点比例、Weil 完全正性、谱酉性、
fixed-shift Hardy--Littlewood asymptotic 或 bounded negative index。

## 9. 模型范围与部分 Weil 接口

- **Riemann zeta**：定理 218-A 与推论 218-B 直接适用。
- **primitive Dirichlet L**：character phases 可吸收到式 (17) 的 `zeta_i`；
  analytic closure不变，local core absolute sieve也不受 unit phases影响。
- **Dedekind/automorphic L**：定理 218-E 与 six-window Gram部分保留；式 (32)
  需要相应 coefficient-convolution local sieve，不能由 Rankin--Selberg second
  moment自动替代。
- **函数域**：圆周 frequency lattice 与 Fejér聚类逐字存在；local box energy
  可能由 polynomial large sieve给出 exact degree bound。
- **负向 spectral models**：若 pair kernel没有 nonnegative common-window Gram，
  core小不能通过定理 218-E传播到全高度能量。这给出了结构的真实适用边界。

在部分 Weil 配置中，本轮把一个 response-specific local positive mass预算提升为
完整 finite Gram 的 `o(N)`，但提升定理本身不假设该 Gram正性；正性来自明确的
six-window向量实现。

## 10. 修正后的下一最小引理 218-F [O]

transition tail 已闭合。新的首个未覆盖层是 critical logarithmic-square shell

\[
 XL^{2-\rho}\le ab\le XL^2
\tag{42}
\]

（固定小 `rho>0`）。沿用式 (27) 的 `A=8` circle boxes，证明

\[
 \boxed{
 \beta_L^4d_G\sum_p
 \left\|\sum_{\substack{(a,b)\text{ in (42)}\\\theta_{a/b}\in I_p}}
 |b_ab_b|g_{a/b}\right\|_H^2=o(N),}
\tag{43}
\]

或者构造实际 prime-power family，使式 (43) 的左端 `gg N`。

式 (43) 是有限、正、可证伪的 arithmetic local-density问题。generic
`z^{Omega}` sieve在顶端只给主尺度（并带 `log log` 损失），所以晋级必须利用
factorization restrictions、真实 six-window support 或更精确的局部二素数结构；
不能重新诉诸已经不需要的 oscillatory-tail cancellation。若出现 `gg N` 的实际
下界，则该层必须与 adjacent/continuum/Gamma channels联合处理，并应形成明确
的 response obstruction theorem。

## 11. 后续更新（笔记 219）

笔记 219 对 critical `ab asymp XL^2` local boxes 做有限审计，并构造一个
nonnegative sparse model：它同时满足正确的一阶质量、二阶矩、pointwise bound
及所有 `h<=L^2` 的 natural-size shifted upper bounds，但 critical proxy 仍为
`asymp N`。因此式 (43) 不能仅由这些 scalar budgets 推出；下一轮必须使用
actual factorization restrictions、six-window support、joint local law 或真实跨通道 Gram。

## 11. 后续全局覆盖修正（笔记 232）

定理 218-A 与推论 218-B 保持 [T]；它们的集合范围始终是
`ab<=XL^(2-eta)`。笔记 232 证明“尚未覆盖的只有 critical 顶层”这一文字摘要不
完整：critical 顶层之外还有 `ab>XL^2` 高乘积区，且其 atomic diagonal 为主尺度。
