# 233. Aperture--depth 坐标、三次对数 collar 与幂级高乘积障碍

日期：2026-09-03

分支：MOM-1 / 路线 A1l；接口：alternating/Farey physical response Gram

状态：aperture--depth 精确坐标、fixed-aperture 支撑嵌套、near-aperture flat
overlap 下界、polylog-uniform determinant incidence 与任意 `K<3` 的 primitive
cutoff closure 为 [T]；纯素数 determinant-2 high--low 样本为 [E]；固定对数
saving 不能闭合幂级高乘积正局部能量为 [N]；signed power-high determinant
response 为 [O]。本笔记不更新 PDF，也不改变记录级比例的 [C] 状态。

## 1. 本轮结论

笔记 232 证明 `ab<=XL^2` 不是 alternating 的完整 physical support，并发现
其外 atomic diagonal 有正主质量。本轮进一步得到：

1. 每个 atom 可用 normalized aperture `q` 与 support depth `delta` 精确参数化，
   且 product exponent 满足

   \[
   \frac{\log(ab)}L=2-2\delta-|q|.
   \tag{1}
   \]

2. 在 fixed aperture 上，高乘积 atom 的 translated support 是低乘积 atom
   support 的子区间，而不是与之分离；所以 high--low cross 不能由 window
   support 自动排空。
3. 笔记 222 的 natural-scale factor-bin incidence proof 对任意固定 polylog
   product band 一致。与 Fejer box ledger、atomic diagonal 和 finite/bulk
   remainder 合并后，对每个 fixed `K<3`，

   \[
   \boxed{ab\le XL^K}
   \tag{2}
   \]

   的全部 primitive distinct-base alternating family 无条件 atomic
   diagonalize。这把旧 cutoff `XL^2` 推进了任意小于一个整对数的 collar。
4. `K=3` 是当前 **positive local-energy + natural incidence + absolute finite
   transfer** 账本的 endpoint。更重要地，在 `ab asymp X^(2 theta)`、
   `theta>1/2` 的幂级高乘积箱中，即使 incidence 比 natural scale 多任意固定
   对数 saving，代入该正账本仍比 `N=XL` 大一个 `X^(2theta-1)` 幂。

所以真正剩余输入不是继续优化固定 log powers，而是幂级 high-product 的 signed
response cancellation、power-saving incidence，或证明该 response 本身形成主尺度
障碍。

## 2. Aperture--depth 精确坐标

令

\[
 \alpha=\frac{\log a}{L},\qquad
 \beta=\frac{\log b}{L},\qquad
 q=\alpha-\beta,
 \qquad
 \delta=1-\max(\alpha,\beta).
\tag{3}
\]

这里 `0<=alpha,beta<=1`，且

\[
 0\le\delta\le1-|q|.
\tag{4}
\]

### 定理 233-A（aperture--depth inversion）[T]

精确地，

\[
 (\alpha,\beta)=
 \begin{cases}
 (1-\delta,1-\delta-q),&q\ge0,\\
 (1-\delta+q,1-\delta),&q\le0,
 \end{cases}
\tag{5}
\]

并且式 (1) 成立。

#### 证明

若 `q>=0`，则 `alpha=max(alpha,beta)=1-delta`，再由
`beta=alpha-q` 得第一式；`q<=0` 同理。两坐标相加即为

\[
 \alpha+\beta=2-2\delta-|q|.
\]

`square`

笔记 215 的 product excess `e=log(ab/X)` 因而满足

\[
 \frac eL=1-2\delta-|q|.
\tag{6}
\]

具体地，

\[
 \begin{aligned}
 ab>XL^2
 &\Longleftrightarrow
 \delta<\frac{1-|q|}{2}-\frac{\log L}{L},\\
 ab<XL^\eta
 &\Longleftrightarrow
 \delta>\frac{1-|q|}{2}-\frac{\eta\log L}{2L}.
 \end{aligned}
\tag{7}
\]

## 3. Translated support 的嵌套

沿用笔记 216 的 coefficient-free physical symbol

\[
 P_{a/b}(u)=\phi(u)\phi(u-\log(a/b))\phi(\log a-u)^2,
\tag{8}
\]

以及笔记 218 的共同 Hilbert realization

\[
 g_{a/b}(v)=P_{a/b}(v+\log(a/b)).
\tag{9}
\]

把 `v` 除以 `L`。由笔记 215-A 的支撑区间平移得到：

### 定理 233-B（translated aperture--depth interval）[T]

`g_(a/b)` 的 normalized support 包含于

\[
 \boxed{
 J(q,\delta)
 =\left[\frac12-q_+-\delta,\frac12-q_+\right],
 \qquad q_+=\max(q,0).}
\tag{10}
\]

对 flat window，该区间就是 support，且 `g=1` 于其内部。若标准 smooth window
在支撑内部严格为正，则 `g` 在式 (10) 内部严格为正。

#### 证明

笔记 215-A 在未平移变量中的区间为：`q>=0` 时

\[
 [L(\alpha-1/2),L/2],
\]

`q<=0` 时

\[
 [L(\alpha-1/2),L(1/2+q)].
\]

式 (9) 再减去 `Lq`。代入式 (5)，两种情形分别得到

\[
 [1/2-q-\delta,1/2-q],
 \qquad
 [1/2-\delta,1/2].
\]

这正是式 (10)。flat/strictly-positive 陈述来自各 window factors 的逐点性质。
`square`

### 推论 233-C（high--low support nesting）[T/N]

固定 aperture `q`。若 `delta_h<delta_l`，则

\[
 \boxed{J(q,\delta_h)\subset J(q,\delta_l).}
\tag{11}
\]

特别地，满足式 (7) 的 fixed-aperture high atom 与 low atom 具有完整的 high
support overlap。对 flat window，normalized overlap 精确等于 `delta_h`。

更一般地，对两个 apertures `q,q'`，flat overlap 满足

\[
 \boxed{
 |J(q,\delta)\cap J(q',\delta')|
 \ge
 \bigl(\min(\delta,\delta')-|q-q'|\bigr)_+.}
\tag{12}
\]

因此若 physical log-ratio gap 为 `O(1/X)` 且两个 depths 远离零，则 overlap
为 `min(delta,delta')+o(1)`，不是小量。

#### 证明

式 (11) 因两个 intervals 有相同右端而立即成立。一般情形的右端差为

\[
 |q_+-q'_+|\le|q-q'|.
\]

两个长度分别为 `delta,delta'` 的 intervals 的交长至少为较短长度减去右端差，
得到式 (12)。`square`

这里 `[N]` 的含义是：仅用 compact support 或 support depth 不能排空
high--low cross。它不声称真实算术 aggregate 必为主尺度。

## 4. Prime-side near-collision 不是空模型 [E]

脚本在 genuine primes 中分别搜索 `ab>XL^2` 与 `cd<XL^(1/2)` 的最近 ratios，
得到：

| `X` | high ratio | low ratio | determinant | `X |log rho-log sigma|` | flat overlap / high depth |
|---:|---:|---:|---:|---:|---:|
| 300 | `199/251` | `23/29` | 2 | 0.103950 | 1.000000 |
| 600 | `409/541` | `31/41` | 2 | 0.071556 | 1.000000 |
| 1200 | `883/983` | `53/59` | 2 | 0.046067 | 1.000000 |

四个 entries 都是 odd primes，所以 determinant `2` 正好达到笔记 209-F 的
parity lower bound；它不是 base-2 或 proper-power exceptional channel。

这些有限数据只证明 arithmetic support 非空并审计索引；它们不推出渐近有多少
determinant-2 pairs，也不构成 fourth-moment lower bound。

## 5. Polylog-uniform factor-bin incidence

令 fixed real constants

\[
 0<K_-<K_+<\infty,
\tag{13}
\]

考虑笔记 222 的 ratio-compatible factor boxes，改把 product range 写成

\[
 XL^{K_-}\le AB,CD\le XL^{K_+}.
\tag{14}
\]

仍置

\[
 R=AD\asymp BC\asymp\sqrt{ABCD},
 \qquad H_R\asymp R/X.
\tag{15}
\]

### 定理 233-D（fixed-polylog uniform determinant incidence）[T/R]

在式 (13)--(15) 的全部 boxes 上，一致有

\[
 \boxed{
 \mathfrak D_{A,B;C,D}(H_R)
 \ll_{K_-,K_+}RH_R(\log L)^C.}
\tag{16}
\]

外部输入仍只有笔记 222 已审计的 Bettin--Chandee fixed-determinant formula 与
标准 Selberg upper-bound sieve [R]；没有新增素数相关猜想。

#### 证明

逐项复核笔记 222：

1. product comparability 现在给
   `B/D=L^(O_(K_-,K_+)(1))` 与
   `A/C=L^(O_(K_-,K_+)(1))`，仍只是 fixed polylog factors；
2. moderate aspect 中 proper-power deletion 的相对误差仍为
   `U^(-1/2)L^O(1)` 或 `V^(-1/2)L^O(1)`；
3. Bettin--Chandee remainder 的负 `U`/`V` power 不受 fixed log powers改变，
   只改变隐含 polylog 常数；
4. extreme aspect 中 `K=U/V>U^(1-delta)` 仍给 two-linear-form sieve 的固定
   power saving；
5. gcd ledger 中 affine length 的 `g` 与 shift count 的 `1/g` 仍精确抵消；
6. `H_R` 现在仍为 fixed power of `L`，若某个 box 中 `H_R/g<1`，对应非零
   determinant fiber 为空，反而更容易。

因此笔记 222-C--H 的证明逐字成立，只需把所有 `O_rho(1)` 改为
`O_(K_-,K_+)(1)`。得到式 (16)。`square`

这一步没有把结论当作新公理；它明确检查了原 proof 中 product endpoint 的每个
用途。

## 6. 三次对数以前的完整 primitive closure

### 定理 233-E（`K<3` primitive cutoff closure）[T]

固定任意

\[
 0<K<3.
\tag{17}
\]

令 `P_K(X)` 为全部 distinct-base primitive ordered pairs `(a,b)`，满足

\[
 2\le a,b\le X,\qquad ab\le XL^K.
\tag{18}
\]

则

\[
 \boxed{
 \left\|\sum_{(a,b)\in\mathcal P_K(X)}F_{a/b}^{fin}\right\|_{HS}^2
 =
 \sum_{(a,b)\in\mathcal P_K(X)}
 \|F_{a/b}^{fin}\|_{HS}^2+o(N).}
\tag{19}
\]

#### 证明

`K<=2` 已由笔记 218 与 222（取稍有重叠的 half-open bands）覆盖。以下设
`2<K<3`，并固定足够小 `eta>0`。

**已知低区。** 笔记 218 闭合 `ab<=XL^(2-eta)`。

**扩展 shell 的 atomic diagonal。** 对 fixed multiplicative factor boxes，
引理 210-A 给每个 `(A,B)` box

\[
 \sum_{a\asymp A,b\asymp B}|b_ab_b|^2\ll L^2.
\tag{20}
\]

product coordinate 有 `O(log L)` 层，ratio coordinate 有 `O(L)` 层；故
`XL^(2-eta)<=ab<=XL^K` 的 atomic diagonal 至多

\[
 \beta_L^4d_G\,O(L^2)O(L\log L)
 \ll X\log L=o(N).
\tag{21}
\]

**扩展 shell 的 local positive energy.** 对每个 ratio-compatible ordered
box pair，笔记 220-(20) 与定理 233-D 给

\[
 \frac{\beta_L^4d_G}{R}\mathfrak D(H_R)
 \ll \frac{R}{L^3}(\log L)^C.
\tag{22}
\]

这里 `R<=XL^K`。relevant box pairs 仍只有
`O(L(log L)^2)` 个，所以总量至多

\[
 \boxed{
 N L^{K-3}(\log L)^{C+2}=o(N),}
\tag{23}
\]

因为 `K<3` fixed。笔记 218-E 的 clustered cone Fejer inequality把式 (23)
提升为整个 bulk main Gram 的 `o(N)`；`+/-L` aliases 由笔记 215-F 的全 product
support gap 排空，`+/-2L` 由 ratio diameter 排空。

**finite transfer.** 对 cutoff `Z=XL^K`，引理 215-D 给

\[
 \sum_i|b_ab_b|\ll L\sqrt Z.
\tag{24}
\]

笔记 218-(36)--(37) 的 crossing-Hankel 与 aggregate defect 因而都至多

\[
 \frac{Z(1+\log L)}{L^2}
 =N L^{K-3}(1+\log L)=o(N).
\tag{25}
\]

最后，扩展 shell 的 aggregate norm 与 diagonal 都为 `o(N)`，所以它与已知
低区的 cross 由 Cauchy--Schwarz 为 `o(N)`。合并即得式 (19)。`square`

## 7. `K=3` 与幂级高乘积的正方法天花板

式 (23)、(25) 在 `K=3` 都不再给 little-oh。这不是说 endpoint closure 为假，
而是当前 absolute ledger 的精确推理边界。

更一般地，定义 overlap-weighted incidence

\[
 \mathfrak D_W(H)=
 \sum_{0<|ad-bc|\le H}
 \Lambda(a)\Lambda(b)\Lambda(c)\Lambda(d)W_{a,b;c,d}.
\tag{26}
\]

由笔记 216、220，单个 factor-box pair 的正局部能量上界为

\[
 \mathcal E_{box}
 \ll\frac{\beta_L^4d_G}{R}\mathfrak D_W(H_R).
\tag{27}
\]

要仅靠式 (27) 得到 `o(N)`，至少需要

\[
 \boxed{\mathfrak D_W(H_R)=o(RL^4).}
\tag{28}
\]

natural-scale benchmark（这里不声称 asymptotic）是 `mathfrak D_W(H_R)` 处于 `R H_R` 乘 overlap factor 的尺度。

### 障碍定理 233-F（fixed-log savings do not enter power-high）[N]

固定 `1/2<theta<1`，考虑 balanced interior boxes

\[
 A,B,C,D\asymp X^\theta,
 \qquad R\asymp X^{2\theta},
 \qquad H_R\asymp X^{2\theta-1},
\tag{29}
\]

并限制 aperture 靠近零，使 support depth `delta asymp 1-theta` 为固定正常数。
只使用任意 fixed `A_0>=0` 的 absolute incidence estimate

\[
 \mathfrak D_W(H_R)
 \ll\frac{R H_R}{L^{A_0}}
\tag{30}

以及式 (27)，不能逻辑推出 `mathcal E_box=o(N)`。其直接代入上界相对 `N` 为

\[
 \boxed{
 \frac{\mathcal E_{box}}N
 \ll
 \frac{X^{2\theta-1}}{L^{A_0+4}},}
\tag{31}

右端对每个 fixed `A_0` 都发散。

#### 证明

由 `beta_L^4 d_G asymp X/L^3`、式 (29)--(30)，式 (27) 只给

\[
 \mathcal E_{box}
 \ll
 \frac{X}{L^3R}\frac{RH_R}{L^{A_0}}
 =\frac{X^{2\theta}}{L^{A_0+3}}.
\]

除以 `N=XL` 即为式 (31)。抽象预算
`D_*(H_R)=RH_R/L^(A_0)` 满足式 (30) 且使该 proxy 达到右端尺度，所以这些
上界资料本身不蕴含 little-oh。`square`

该 no-go 只排除 proof schema，不声称真实 prime incidence 有相应 lower bound，
也不声称真实 fourth moment 发散。式 (12) 与纯素数实验说明 window support 和
arithmetic emptiness 都不能充当缺失的 power saving；但真正的渐近 lower bound
仍是开放问题。

## 8. 最小输入、删除审计与循环性

1. **compact translated support**：给式 (10)--(12)。删除 translation 会错误地
   比较不同物理坐标；删除 compact support 则 depth 不再定义。
2. **strict interior positivity / flat window**：只用于把 envelope overlap升级为
   实际正 overlap；式 (10) 的 envelope identity不依赖此项。
3. **von Mangoldt local energy**：给式 (20)--(21)。删除后 atomic diagonal
   可能不再是 `o(N)`。
4. **natural determinant incidence**：定理 233-D 只在 fixed-polylog bands使用；
   不把它外推成幂级 uniform theorem。
5. **Fejer cone Gram**：把 local positive energy提升为 whole sampled bulk Gram。
   删除共同非负 Hilbert realization，式 (23) 不控制 cross-bin energy。
6. **moving-cutoff coefficient mass**：负责式 (25)。它与 main incidence共同给
   同一个 endpoint `K=3`。
7. **frozen `X,L,d_G`**：所有 resolution bins、factor boxes 与 finite transfer
   使用同一尺度；没有通过换 cutoff 隐藏误差。

删除审计：

- 把 high support 当成小量失败于 fixed interior `theta`，此时 depth 为常数；
- 把 high--low 当成 disjoint 失败于式 (11)；
- 继续增加任意 fixed log saving 失败于式 (31)；
- 把式 (31) 读成实际 lower bound 会过度声称；它只是 implication ceiling。

循环性审计：全部结论位于 finite prime/Gabor side。使用的是 compact windows、
Chebyshev/PNT-level local mass、已审计 determinant upper sieve、有限 Fejer identity
与 Hilbert inequalities；没有调用 RH/GRH、零点密度、Hardy--Littlewood
asymptotic、Weil positivity、谱酉性或一致有界负指标。

## 9. 模型范围与部分 Weil 接口

- Riemann zeta：定理 233-E 直接扩大已闭合 primitive cutoff；233-F 精确定位剩余
  response 输入。
- 原始 Dirichlet `L`：unit character phases不影响 absolute theorem 233-E；
  power-high signed lemma必须保留角色相位。
- Dedekind/automorphic `L`：需要相应 local coefficient energy、factor incidence
  与 moving-cutoff mass；现有 Rankin--Selberg second moment不自动给定理 233-D。
- 函数域：aperture--depth 变成 degree aperture/depth，有限域大筛可检验 `K=3`
  endpoint 是否是整数模型特有。
- 无 Euler product 的谱 zeta：没有 determinant factorization，只有支撑定理而无
  233-D/E 的算术接口。

在部分 Weil 配置中，定理 233-E 是 response Gram 的可验证近正/对角化输入；
233-F 则证明 compact support 加 polylogarithmic negative-trace budget不足以处理
幂级深层 atoms，避免把完整 Weil positivity藏进“uniform local energy”公理。

## 10. 下一最小引理 233-G [O]

固定一个 interior exponent `1/2<theta<1` 与窄 balanced factor box

\[
 a,b,c,d\asymp X^\theta.
\]

对笔记 216-(11) 的 **实际 signed** determinant response，证明以下二者之一：

1. 在每个长度 `X/sqrt L` 的 height interval 上，其一侧均值相对 natural positive
   local energy取得 `X^(-epsilon_theta)` power saving；
2. 给出保留四个 von Mangoldt weights、six-window overlap、carrier phase 与
   consecutive Gabor samples 的 `gg N` lower-bound family。

不得以任意 Farey coefficients、逐项 absolute determinant count 或 window-only
support bound替代 actual response。第一轮只取例如 `theta=3/4`，并把 shifts分成
`|ad-bc|<=R/X` 的 coherent core 与其外 oscillatory layers；若 core 已产生不可消
的正 lower bound，应停止比例路线并形成四矩障碍论文。

## 11. 可复现审计 [E]

脚本 `scripts/alternating_aperture_depth_audit.py` 检查：

1. 式 (1)、(5)、(10) 的精确坐标恒等式；
2. fixed-aperture nesting 与式 (12)；
3. genuine-prime high--low determinant-2 near collisions；
4. 式 (31) 的 exponent ledger。

脚本不实现 Bettin--Chandee/Selberg sieve，也不把有限 prime samples升级为渐近
定理。

## 12. 后续修正（笔记 234）

笔记 234 对 actual carrier 作逆向审计，证明在自然变量
`t=X log(ad/bc)` 中，normalized consecutive-Gabor response 的极限是带通核

\[
 K(t)=\frac{\sin(\pi t)}{\pi t}\cos(3\pi t),
 \qquad
 \operatorname{supp}\widehat K=[1,2]\cup[-2,-1].
\]

其全积分为零，但 `|t|<=1` core 积分为严格正常数
`0.023558003094...`，外层 tail 精确给相反质量。因此本笔记 233-G 中“若
core 已产生不可消正 lower bound 就停止”的表述必须加强为：只有在同时保留
core 与 tail 的完整频带 response 后得到 `gg N` lower bound，才能形成障碍。
修正后的下一输入是实际 response measure 的 mesoscopic determinant
discrepancy，或完整 band lower bound；support-only 与 positive ledger 的
no-go 结论不受影响。
