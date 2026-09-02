# 235. Exact finite dyadic band discrepancy 与幂级高乘积的 `L^4` 门槛

日期：2026-09-03

分支：MOM-1 / 路线 A1n；接口：fixed-power alternating response measure

状态：exact finite Gabor kernel 的 pre-alias envelope/variation、dyadic
response-discrepancy bridge 与 raw `L^4` closure normalization 为 [T]；
`theta=3/4` flat-window prime-power measure 为 [E]；全 factor-cell dyadic
discrepancy budget为 [O]。本笔记修正“只需 signed `o(B)`”这一过弱目标，不更新
PDF，也不改变零点比例的 [C] 状态。

## 1. 本轮结论

笔记 234 证明 fixed-power Gabor response 是有零频谱间隙的带通核，并给出一个
global first-discrepancy criterion。本轮解决两个遗留问题。

第一，不能在整个有效 ratio range 上只用 limiting kernel：虽然
`K_(X,D)->K` 局部一致，但粗略 uniform replacement 会损失一个相对 `1/L`，这
不足以抵消 `theta=3/4` positive ledger 中的 `X^(1/2)`。本轮直接对 exact finite
kernel证明 dyadic Abel bound，不发生该损失。

第二，power-high closure 的正确 raw 目标不是 signed response 为 `o(B)`。由

\[
 \beta_L^4D\asymp\frac X{L^3},
 \qquad N=XL,
\tag{1}
\]

exact response-measure integral必须满足

\[
 \boxed{\text{global raw band response}=o(L^4).}
\tag{2}

这里 `B` 是 positive response-measure mass，可能比 `L^4` 大一个幂；所以
`o(B)` 本身不闭合四矩。

本轮把式 (2) 归约为：central cumulative discrepancy 加全部 dyadic shells 的
local cumulative discrepancies，总和为 `o(L^4)`，另有显式可审计的 mass/edge
项。

## 2. Exact finite kernel 与 pre-alias 区

沿用笔记 234，置

\[
 D=d_G,\qquad
 \lambda=\frac D{XL},\qquad
 K_{X,D}(t)
 =\frac1D\sum_{k=0}^{D-1}
 \cos\left(2\pi\left(1+\frac{k}{XL}\right)t\right).
\tag{3}
\]

标准选择 `D=round(XL)` 满足

\[
 |\lambda-1|\le\frac1{2XL}.
\tag{4}

几何和形式是

\[
 K_{X,D}(t)=
 \frac{\sin(\pi\lambda t)}
 {D\sin(\pi t/(XL))}
 \cos\left(2\pi t+\frac{(D-1)\pi t}{XL}\right).
\tag{5}

固定 `0<c<1/2`，以下只取

\[
 |t|\le cXL.
\tag{6}

这称为 pre-alias 区。对 fixed-width aperture cells，实际
`|t|=X|log(ad/bc)|=O(X)`，所以充分大 `X` 时自动落在式 (6)。

### 引理 235-A（exact envelope and dyadic variation）[T]

假设 `1/2<=lambda<=2`。在式 (6) 中，

\[
 |K_{X,D}(t)|\ll\min(1,|t|^{-1}),
\tag{7}
\]

并且对 `1<=R<=cXL/2`，

\[
 |K_{X,D}(R)|+|K_{X,D}(2R)|
 +\int_R^{2R}|K'_{X,D}(t)|dt\ll1.
\tag{8}

对 `M>=2`，

\[
 |K_{X,D}(M)|+\int_0^M|K'_{X,D}(t)|dt
 \ll\log(2+M).
\tag{9}

#### 证明

在 `|t|<=cXL` 中，

\[
 |\sin(\pi t/(XL))|\gg |t|/(XL).
\]

代入式 (5)，并用 `D/(XL)=lambda asymp1`，得到式 (7)。对式 (5) 求导：
amplitude 的导数为

\[
 O(|t|^{-1}+|t|^{-2}),
\]

carrier phase 的导数为 `O(1)`；故当 `|t|>=1` 时

\[
 |K'_{X,D}(t)|\ll |t|^{-1}+|t|^{-2}.
\tag{10}

在 `|t|<=1` 上逐项微分式 (3) 给 uniform `O(1)`。分别在 `[R,2R]` 与
`[0,M]` 积分即得式 (8)--(9)。`square`

## 3. Exact constant-density shell cancellation

只有 variation bound 仍会把 constant density 当作误差。带通结构还给每个 shell
的额外 cancellation。

### 引理 235-B（finite shell integral）[T]

在引理 235-A 的范围内，

\[
 \left|\int_0^M K_{X,D}(t)dt\right|
 \ll
 \frac1M,
\tag{11}

且

\[
 \left|\int_R^{2R}K_{X,D}(t)dt\right|
 \ll
 \frac1R.
\tag{12}

#### 证明

对式 (3) 先在 `t` 上积分。以式 (12) 为例，所得 summand 是

\[
 G_R(\xi)
 =\frac{\sin(4\pi\xi R)-\sin(2\pi\xi R)}{2\pi\xi},
 \qquad 1\le\xi\le3,
\tag{13}

且 `||G_R'||_infinity<<R`。因此式 (3) 的离散频率平均与
`int_0^1 G_R(1+s)ds` 相差 `O(R/D+R|lambda-1|)`。该连续平均正是 limiting
band kernel `K` 在 `[R,2R]` 上的积分；由一次分部积分为 `O(1/R)`。这证明
式 (12)。式 (11) 使用

\[
 G_{0,M}(\xi)=\frac{\sin(2\pi\xi M)}{2\pi\xi}
\]

完全相同；limiting kernel 在正半轴的条件积分为零，故 `[0,M]` 积分为
`O(1/M)`。`square`

这里保留的是 exact consecutive samples。若把它们换成任意频率集合，式
(11)--(12) 不自动成立。

## 4. Dyadic discrepancy bridge

令 `mu` 是 even finite positive measure，支撑于 `[-U,U]`，其中

\[
 2\le M\le U\le cXL/2.
\tag{14}

把正半轴分为

\[
 I_0=[0,M],\qquad
 I_j=(R_j,2R_j],\qquad R_j=2^{j-1}M\quad(j\ge1),
\tag{15}

并在 `U` 以外把 `mu` 延拓为零。只保留与 `[0,U]` 相交的有限多个 shells。
写

\[
 b_j=\mu(I_j),\qquad c_j=\frac{b_j}{|I_j|},
\tag{16}

以及 local one-sided cumulative discrepancy

\[
 E_j=
 \sup_{u\in I_j}
 \left|
 \mu(I_j\cap(-\infty,u])-c_j|I_j\cap(-\infty,u]|
 \right|.
\tag{17}

这里 `mu` 表示正半轴限制；even extension 的总质量为

\[
 B=2\sum_j b_j.
\tag{18}

### 定理 235-C（exact dyadic band-discrepancy bridge）[T]

在式 (14)--(18) 下，

\[
 \boxed{
 \begin{aligned}
 \left|\int K_{X,D}(t)d\mu^{even}(t)\right|
 \ll{}&
 \frac{b_0}{M^2}+E_0\log(2+M)\\
 &+\sum_{j\ge1}\left(\frac{b_j}{R_j^2}+E_j\right)
 +B\left(D^{-1}+|\lambda-1|\right).
 \end{aligned}}
\tag{19}

#### 证明

在每个 `I_j` 上写

\[
 d\mu=c_jdt+d\nu_j,
\]

其中 `nu_j` 的 cumulative primitive 由式 (17) 控制。对 constant-density
部分，引理 235-B 给

\[
 \begin{aligned}
 \left|c_0\int_{I_0}K_{X,D}\right|
 &\ll \frac{b_0}{M^2}
 +b_0(D^{-1}+|\lambda-1|),\\
 \left|c_j\int_{I_j}K_{X,D}\right|
 &\ll \frac{b_j}{R_j^2}
 +b_j(D^{-1}+|\lambda-1|).
 \end{aligned}
\tag{20}

对 discrepancy 部分作 Stieltjes integration by parts。引理 235-A 给 central
block

\[
 \left|\int_{I_0}K_{X,D}d\nu_0\right|
 \ll E_0\log(2+M),
\tag{21}

而每个 dyadic shell 给

\[
 \left|\int_{I_j}K_{X,D}d\nu_j\right|\ll E_j.
\tag{22}

对 `j` 求和，再由 evenness 乘固定因子 `2`，即得式 (19)。`square`

最后一个不完整 shell 不产生漏洞：式 (17) 的 reference density仍铺在整个
dyadic interval，`U` 以外的零质量被计入 `E_j`。

## 5. `L^4` closure gate

对每个 factor/aperture cell pair，用笔记 234-(16) 的实际正 response measure
`mu_q`；若原 ordered cell pair 不对称，就用

\[
 \mu_q^{sym}=\frac12(\mu_q+\iota_*\mu_q),
 \qquad \iota(t)=-t,
\tag{23}

替代。因为 `K_(X,D)` 为 even，response integral 不变。

令 `Q(mu_q;M)` 表示式 (19) 右端去掉 absolute constant 后的量。

### 推论 235-D（global raw `L^4` criterion）[T/C]

若对一个不重叠的 fixed-power factor/aperture partition 有

\[
 \boxed{
 \sum_q Q(\mu_q;M_q)=o(L^4),}
\tag{24}

则这些 boxes 的 bulk alternating off-diagonal main response 总和为 `o(N)`。

这里“式 (24) 推出 `o(N)`”是 [T]；对实际 primes 证明式 (24) 是 [O]，故完整
实例仍为 [C]。

#### 证明

定理 234-D 与定理 235-C 给 main response 的绝对值至多

\[
 \beta_L^4D\sum_qQ(\mu_q;M_q).
\]

再用式 (1) 与式 (24)，得到

\[
 \frac X{L^3}o(L^4)=o(XL)=o(N).
\]

`square`

该 criterion 是 global box ledger；不能把“每个 fixed box 为 `o(L^4)`”直接对
增长的 box 数求和。aliases、atomic diagonal、finite boundary 与共同高度选择仍
调用笔记 218、223--225、231、233 已分别审计的接口，本推论只闭合当前缺失的
bulk high-product alternating main response。

## 6. 为什么 `o(B)` 不够 [N]

### 障碍推论 235-E（relative cancellation ceiling）[N]

若已知资料只给

\[
 \left|\int K_{X,D}d\mu\right|=o(B)
\tag{25}

而不控制其相对于 `L^4` 的绝对尺度，则不能逻辑推出该 box response 为 `o(N)`。

#### 证明

在 `theta=3/4` natural positive ledger 中允许

\[
 B\asymp X^{1/2}L^{O(1)}.
\]

例如抽象预算 `|int Kdmu|=B/log X` 满足式 (25)，但仍可大于每个 fixed power
`L^4`。乘式 (1) 后不为 `o(N)`。`square`

该 no-go 只审计 implication；不声称实际 prime response 有此大小。

## 7. Actual prime-power finite diagnostics [E]

脚本 `scripts/power_high_prime_measure_audit.py` 固定

\[
 0.70X^{3/4}\le a,b,c,d\le1.30X^{3/4},
 \qquad M=X^{1/4},
\tag{26}

保留：

1. 四个 prime-power von Mangoldt factors；
2. distinct-base atom restriction；
3. flat translated six-window overlap；
4. exact carrier 与全部 consecutive Gabor samples；
5. symmetric response measure 与 cumulative discrepancy。

输出摘要为：

| `X` | ratio atoms | pairs | core signed / `B` | band signed / `B` | `E log M/B` | det-2 mass / `B` |
|---:|---:|---:|---:|---:|---:|---:|
| 400 | 182 | 310 | +0.03430 | +0.02487 | 0.08966 | 0.05764 |
| 800 | 420 | 1,038 | -0.01029 | -0.01633 | 0.03062 | 0.00972 |
| 1,600 | 812 | 2,778 | -0.00508 | -0.00546 | 0.03282 | 0.00522 |
| 3,200 | 1,806 | 8,084 | +0.00094 | -0.00090 | 0.02002 | 0.00649 |
| 6,400 | 4,556 | 30,576 | -0.00127 | -0.00236 | 0.01052 | 0.00276 |

这些数据与 mesoscopic flattening 相容，也显示 core 的符号不稳定且不决定完整
band。它们不证明式 (24)：

- `M=X^(1/4)` 只覆盖增长但有限的 determinant range；
- finite `B` 尚远小于渐近 power scale；
- 没有审计全部 factor/aperture boxes；
- relative trend 不能替代 absolute `o(L^4)` budget。

## 8. 修正后的下一最小引理 235-F [O]

固定 `theta=3/4`。选择一个增长 central scale `M_X`，并对全部窄 balanced
factor/aperture cells 的实际 response measures证明

\[
 \boxed{
 \sum_q\left[
 E_{q,0}\log(2+M_X)+\sum_{j\ge1}E_{q,j}
 \right]=o(L^4),}
\tag{27}

同时用已知 positive incidence控制

\[
 \sum_q\left[
 \frac{b_{q,0}}{M_X^2}
 +\sum_{j\ge1}\frac{b_{q,j}}{R_j^2}
 +B_q(D^{-1}+|\lambda-1|)
 \right]=o(L^4).
\tag{28}

第一攻击点是 flat window 与 single balanced product cell；若式 (27) 连无权
版本都失败，则构造完整 band 的 lower-bound measure。只有式 (27)--(28) 的
global总量或完整 band lower bound可以晋级；relative `o(B)`、单 core 正性或
有限下降趋势均不可晋级。

## 9. 输入、删除审计与循环性

1. **exact consecutive frequency band**：给式 (3)、(11)--(12)。删除规则抽样会
   丢失 constant-density shell cancellation。
2. **pre-alias restriction**：使 denominator `sin(pi t/(XL))` 远离下一零点。
   fixed aperture cells 自动满足；跨 alias cells必须先用笔记 213 的分离。
3. **positive response measure**：允许 cumulative discrepancy。Dirichlet角色权
   下须改用 signed variation，不能直接照搬。
4. **even symmetrization**：只使用 kernel evenness，不新增算术假设。
5. **global `L^4` normalization**：来自 exact `beta_L^4D` 与 `N`，不是 RH 等价
   的 positivity budget。

删除审计：

- 用 limiting kernel 作全 support uniform replacement只给相对 `1/L`，在
  power-high 区不够；
- 只证明 `E_j=o(b_j)` 不自动给式 (27)；
- per-box little-oh 不经 global ledger不可求和；
- finite table不得升级为四素数渐近。

循环性审计：全部 [T]/[N] 结论来自 finite trigonometric sum、pre-alias
elementary bounds、Riemann-sum error、Stieltjes integration by parts与既有响应
归一化；不调用 RH/GRH、Hardy--Littlewood 四素数渐近、Weil positivity、谱酉性
或 bounded negative index。式 (27) 明列为新的独立算术输入。

## 10. 模型范围与部分 Weil 接口

- Riemann zeta：式 (24) 是 fixed-power alternating bulk 的直接缺口接口。
- 原始 Dirichlet `L`：频带定理保留；正测度 discrepancy须替换为角色加权 signed
  block estimate。
- Dedekind/automorphic `L`：同一 `L^4` normalization未必保持，须由各自 Gabor
  dimension和局部系数重算。
- 函数域：degree lattice可能与 discrete band alias；必须先检查频带是否避开
  lattice dual zero mode。
- 无 Euler product 模型：dyadic bridge仍成立，但不存在 determinant response
  measure 与 factor-cell归约。

在部分 Weil 配置中，定理 235-C--D 把“signed response cancellation”从定性口号
缩成绝对 `L^4` arithmetic discrepancy budget，且没有把完整 Weil 正性隐藏在
增长约束族中。

## 11. Exact Abel 加强：移除 `B/D` 伪损失

上文引理 235-B 通过与 continuous band 比较得到的
`R/D+R|lambda-1|` 是正确但过粗的上界。对 exact consecutive grid 可直接作
离散 Abel 求和，从而完全移除该项。

### 引理 235-G（exact pre-alias shell cancellation）[T]

在引理 235-A 的范围内，uniformly 有

\[
 \left|\int_0^M K_{X,D}(t)dt\right|\ll M^{-1},
 \qquad
 \left|\int_R^{2R}K_{X,D}(t)dt\right|\ll R^{-1}.
\tag{29}

#### 证明

对式 (3) 先在 `t` 上积分，只需控制

\[
 S_D(y)=\frac1D\sum_{k=0}^{D-1}
 \frac{e^{2\pi i(1+\lambda k/D)y}}{1+\lambda k/D},
 \qquad 1\le y\le cD/\lambda.
\tag{30}

令 `z=exp(2pi i lambda y/D)` 与
`a_k=(1+lambda k/D)^(-1)`。pre-alias 条件给

\[
 \left|\sum_{k=0}^m z^k\right|
 \le\frac2{|1-z|}\ll\frac D y.
\tag{31}

序列 `a_k` 单调、`a_0=1`，且 total variation 为 `O(1)`。Abel summation
因此给

\[
 |S_D(y)|\ll y^{-1}.
\tag{32}

而 `int_R^(2R)K_(X,D)` 是 `S_D(2R)-S_D(R)` 的固定虚部倍数，
`int_0^M K_(X,D)` 只含 `S_D(M)`；得到式 (29)。`square`

### 定理 235-H（sharpened dyadic bridge）[T]

在定理 235-C 的 notation 下，式 (19) 可加强为

\[
 \boxed{
 \left|\int K_{X,D}(t)d\mu^{even}(t)\right|
 \ll
 \frac{b_0}{M^2}+E_0\log(2+M)
 +\sum_{j\ge1}\left(\frac{b_j}{R_j^2}+E_j\right).}
\tag{33}

#### 证明

重复定理 235-C 的 Stieltjes 分部积分；只把 constant-density 部分的引理
235-B 换成引理 235-G。central 与 dyadic constant terms 分别成为
`O(b_0/M^2)` 与 `O(b_j/R_j^2)`，不再出现
`B(D^(-1)+|lambda-1|)`。discrepancy terms 不变。`square`

因此推论 235-D 的 sufficient global gate 可把 `Q` 替换为式 (33) 右端；下一
最小引理 235-F 的 mass budget 式 (28) 也应删除
`B_q(D^(-1)+|lambda-1|)`。修正后的剩余项只有

\[
 \sum_q\left[
 \frac{b_{q,0}}{M_X^2}
 +\sum_{j\ge1}\frac{b_{q,j}}{R_j^2}
 \right]
\quad\text{和}\quad
 \sum_q\left[E_{q,0}\log(2+M_X)+\sum_{j\ge1}E_{q,j}\right].
\tag{34}

这不是 asymptotic arithmetic input；它是 exact finite response geometry 的
加强。式 (34) 的第一组可尝试由 positive incidence闭合，第二组仍是唯一的
signed arithmetic discrepancy 缺口。

## 12. 后续 mass-ledger 闭合（笔记 236）

笔记 236 已无条件闭合式 (34) 第一组。对 balanced `Y=X^theta`，置
`H=Y^2/X` 与 `M=max(H,Y/H)`；则 `HM>=Y` 且 `H/M<=1`。初等 interval count
给 `D_Y(S)<<Y^2SL`（`S>=Y`），从而

\[
 \frac{b_0}{M^2}+\sum_{j\ge1}\frac{b_j}{R_j^2}
 \ll (H/M)L\ll L=o(L^4).
\]

所以沿定理 235-H 的充分路线，fixed balanced cell 只剩式 (34) 第二组
cumulative discrepancy。对 `theta=3/4` 的证明尺度应取 `M=X^(1/2)`；笔记 235 的 finite
experiment 使用 `M=X^(1/4)` 只为控制计算量，不能替代该渐近尺度。

## 13. 笔记 237 的 necessity 修正

笔记 237 构造 even positive slow-modulation measures，使 central cumulative
discrepancy 恰按 `sqrt(M)` 增长，而 exact consecutive-band response 仍为
`O(M^(-1))`。因此定理 235-H 与式 (34) 保持为完全有效的 sufficient
certificate，但 cumulative discrepancy 不是 band response 的必要或唯一
算术输入。主看板已改为 actual band-energy Gram / physical-response
Type-I--II estimate；本笔记中较早出现的“唯一缺口”均应按此限定理解。
