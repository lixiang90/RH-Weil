# 232. Alternating 高乘积尾的支撑障碍与全局 atom ledger 修正

日期：2026-09-03

分支：MOM-1 / 路线 A1k，接口 alternating/Farey ratio Gram

状态：全局 atom-ID 四区分割、`ab<=XL^2` 非物理支撑上界、平窗高乘积
对角常数与一般正窗的高乘积正质量为 [T]；Montgomery--Taylor 数值为 [E]；
高乘积 primitive off-diagonal response bound 为 [O]。本笔记不更新 PDF。

## 1. 逆审计结论

令

\[
 L=\log X,\qquad r=\frac{\log a}{L},\qquad s=\frac{\log b}{L}.
\tag{1}
\]

笔记 218--222 实际只闭合了

\[
 ab\le XL^2.
\tag{2}
\]

笔记 222-B 随后把式 (2) 称为完整 physical product support。这一短语是错误的。
笔记 201 已经明确证明：alternating path support 不推出 product cutoff；笔记
209-(9) 的 singleton symbol 在任意 `a,b<X` 时都可非零。更强地，式 (2) 之外的
atomic diagonal 不是 `o(N)`，而具有严格正的主尺度极限。

因此此前的正确结论是：

1. 笔记 218 闭合 subcritical/transition union；
2. 笔记 222-A 闭合 logarithmic-square critical shell；
3. 笔记 231 独立闭合 central--noncentral signed cross；
4. **尚未闭合**的是 primitive atoms 的高乘积区 `ab>XL^2` 的 off-diagonal
   aggregate。

这不改变笔记 199、230 已独立算出的 paired diagonal 常数；它只撤销把整个
alternating remainder 说成已闭合的旧拼接。

## 2. Exact physical support 没有 product cutoff

沿用笔记 215 的 product excess 与 ratio 坐标

\[
 e=\log\frac{ab}{X},\qquad \sigma=\log\frac ab.
\tag{3}
\]

singleton alternating bulk symbol 为

\[
 Q_{a/b}(u)=b_ab_b\phi(u)\phi(u-\sigma)\phi(\log a-u)^2.
\tag{4}
\]

笔记 215-A 给其一个基本周期内的支撑长度

\[
 \lambda(e,\sigma)=\frac{L-e-|\sigma|}{2}.
\tag{5}
\]

### 定理 232-A（exact support depth）[T]

在式 (1) 坐标中，

\[
 \boxed{\lambda(e,\sigma)=L\bigl(1-\max(r,s)\bigr).}
\tag{6}
\]

特别地，只要 `a<X`、`b<X`，右端严格为正；`r+s>1` 或
`ab>XL^2` 都不使 symbol 自动消失。

#### 证明

由

\[
 e=L(r+s-1),\qquad |\sigma|=L|r-s|
\]

代入式 (5)，并使用

\[
 r+s+|r-s|=2\max(r,s),
\]

立即得到式 (6)。`square`

删除审计：adjacent word 的累计 path 含 `r+s`，所以 compact support 强制
`r+s<=1`；alternating word 的累计 path 是 `0,r,r-s,...`，只控制各坐标与
ratio。把 adjacent cutoff 搬到 alternating family 正是旧拼接的失效位置。

## 3. 高乘积 atomic diagonal 有正主质量

设 `psi` 是支撑于 `[-1/2,1/2]` 的非负偶窗，

\[
 a_\psi=\int_{-1/2}^{1/2}\psi(u)\,du,
\]

并沿用笔记 199 的 alternating overlap

\[
 A_+(r,s)=\int\psi(u)^2\psi(u+r)\psi(u+s)\,du.
\tag{7}
\]

定义高乘积 paired-diagonal 泛函

\[
 D_{\rm alt}^{>}(\psi)
 =\frac4{a_\psi^4}
 \iint_{\substack{0<r,s<1\\r+s>1}}
 rsA_+(r,s)\,dr\,ds.
\tag{8}
\]

### 定理 232-B（moving logarithmic-square cutoff limit）[T]

在笔记 199 的 von Mangoldt square-measure 渐近下，把 alternating primitive
atomic diagonal 限制到

\[
 ab>XL^2
 \quad\Longleftrightarrow\quad
 r+s>1+\frac{2\log L}{L},
\tag{9}
\]

其归一化 paired-diagonal 极限为式 (8)。若 `psi` 在支撑内部严格为正，则

\[
 \boxed{D_{\rm alt}^{>}(\psi)>0.}
\tag{10}
\]

同素数底、proper-power 与 pairing 退化项在 `L^{-4}` 归一化下消失，所以式
(8) 也属于 distinct-base primitive atoms，而不是 central 或 chain 主项。

#### 证明

笔记 199-(17) 给

\[
 L^{-2}\sum_{n\le X}\frac{\Lambda(n)^2}{n}
 \delta_{\log n/L}\Longrightarrow r\,dr.
\tag{11}
\]

对两个变量取乘积测度，并在 paired alternating path 上保留式 (7)，得到带
indicator

\[
 \mathbf1_{r+s>1+2\log L/L}
\]

的双积分。边界 `r+s=1` 对极限测度为零，overlap 有界，故 bounded convergence
给式 (8)。笔记 199 对退化 pairings 的估计同样适用于该子区域。

若 `psi` 在内部严格为正，取任意小矩形

\[
 r,s\in(1/2+\epsilon,1/2+2\epsilon)
\]

且 `epsilon<1/6`。该矩形满足 `r+s>1`，四个窗在一个正长度内部区间上同时正，
所以 integrand 在正测度集合上严格为正，得到式 (10)。`square`

### 推论 232-C（flat-window exact obstruction）[T]

对平窗 `psi=1_[-1/2,1/2]`，

\[
 A_+(r,s)=1-\max(r,s),
\]

并且

\[
 \boxed{
 \iint_{r+s>1}rsA_+(r,s)\,dr\,ds=\frac1{32},
 \qquad D_{\rm alt}^{>}=\frac18.}
\tag{12}
\]

由于完整 flat alternating diagonal 为 `1/5`，式 (2) 之外的极限份额为

\[
 \boxed{\frac{(1/8)}{(1/5)}=\frac58.}
\tag{13}
\]

#### 证明

按 `r>=s` 对称分半，

\[
 2\int_{1/2}^1\int_{1-r}^r rs(1-r)\,ds\,dr
 =\int_{1/2}^1r(1-r)(2r-1)\,dr
 =\frac1{32}.
\]

乘以式 (8) 的 factor `4` 即得。`square`

对 Montgomery--Taylor 窗，独立 Gauss--Legendre 审计给

\[
 D_{\rm alt}=0.178157229928\ldots,
 \qquad
 D_{\rm alt}^{>}=0.101342668158\ldots.
\]

所以高乘积极限份额约为 `0.568838369338`。[E] 该数值只审计窗口积分；
正性本身已由定理 232-B 严格证明。

## 4. 全局 atom-ID ledger

固定 `0<eta<1`，采用 half-open convention。每个 primitive ordered pair
`(a,b)` 恰落入以下一个区域：

\[
\begin{array}{ll}
\mathcal A_{\rm low}:&ab<XL^\eta,\\
\mathcal A_{\rm trans}:&XL^\eta\le ab<XL^{2-\eta},\\
\mathcal A_{\rm crit}:&XL^{2-\eta}\le ab\le XL^2,\\
\mathcal A_{\rm high}:&ab>XL^2.
\end{array}
\tag{14}
\]

这是穷尽且互斥的纯集合恒等式。现有证明覆盖为：

- low：笔记 215；
- transition：笔记 218；
- critical：笔记 220--222；
- high：atomic diagonal 有式 (8) 的主质量，off-diagonal 尚无闭合定理。

Fejer arcs、factor boxes 与 crossing-Hankel transfer 在前三段都使用同一冻结
`X,L,d`；这只能保证已覆盖区域之间的拼接，不会把第四段变为空集。不同前三段
之间的 cross 可由 transition/critical aggregate `o(N)` 与 low 的 `O(N)` 范数
作 Cauchy 控制；涉及 `A_high` 时该论证没有 small norm 前提。

### 障碍定理 232-D（three-region closure no-go）[N]

下列资料不能推出完整 primitive alternating atomic diagonalization：

1. `A_low,A_trans,A_crit` 各自及相互 cross 已闭合；
2. 全部 atomic diagonal 为 `O(N)`；
3. `ab<=XL^2` 内的 factor-box incidence 为 natural scale。

#### 证明

这些假设没有控制 `A_high` 的 aggregate off-diagonal。式 (12)--(13) 还证明
`A_high` 的 diagonal norm square 不能作为 `o(N)` 删除。抽象 Hilbert 空间中可令
所有 high atoms 平行或正交；两种模型保持相同 atomic diagonals 与前三段资料，
但 high aggregate 分别可产生主尺度 excess 或零 excess。因此结论不由所列资料
逻辑蕴含。`square`

## 5. 对旧结论链的精确影响

1. 笔记 222-A 的 determinant incidence theorem 保持 [T]，但 222-B 只能称为
   critical-shell closure，不能称为 entire primitive support closure。
2. 笔记 225 的 finite four-Toeplitz telescoping 与各已处理 signed boundary
   estimate 保持 [T]；“完整 pure-prime fourth ledger”必须加入 high-product
   primitive off-diagonal 输入。
3. 笔记 227--230 的常数、moving-block transfer 与 quartic inertia implication
   保持 [T]/[E]；把它们实例化为 zeta 的新比例仍为 [C]，且现在有一个明确未闭合
   prime-side sector。
4. 笔记 231 的 central-cross repair 不依赖错误 cutoff，保持 [T]。

本障碍不是 RH 的改写。它完全位于 finite prime-side response support，并给出
显式正质量反证；没有调用零点位置、Weil positivity、酉谱或负指标假设。

## 6. 下一最小引理 232-E [O]

令

\[
 \mathcal H_j=
 \{(a,b):2^jXL^2<ab\le2^{j+1}XL^2,\ a,b\le X\},
\tag{15}
\]

只保留 `Q_(a/b)` 的真实 support-depth factor

\[
 \lambda=L(1-\max(r,s)).
\]

证明以下二者之一：

1. 只要 source 或 target 落入某个 `H_j`（包括 high--low cross），对应的跨
   ratio Fejer/factor-bin local energy 在所有 `j` 上可和为 high atomic
   diagonal 加 `o(N)`；
2. 构造保留 von Mangoldt weights、carrier phase 与 support depth 的主尺度
   lower-bound model，证明现有 determinant upper sieve 即使扩到 `R>>XL^2`
   仍不足。

不得用全区间 `W_2`、任意 Farey coefficient Bessel bound或把式 (8) 的主质量
当作误差。首先应把笔记 220-(20) 的 box estimate加入 exact overlap depth，避免
以 `R<=XL^2` 的旧上界完成一个循环推理。

## 7. 可复现审计 [E]

脚本 `scripts/alternating_high_product_tail_audit.py`：

1. 验证平窗式 (12)--(13)；
2. 对 Montgomery--Taylor 窗独立计算完整与高乘积 alternating diagonal；
3. 检查 moving threshold `1+2 log L/L` 的积分收敛方向；
4. 只审计窗口积分与支撑几何，不证明高乘积 off-diagonal 估计。

## 8. 后续 aperture--depth 推进（笔记 233）

笔记 233 将本笔记的 high region精确写成 aperture--depth 坐标，并证明
fixed-aperture high support 嵌套于 low support；所以 high--low 不能靠支撑排空。
另一方面，原 critical determinant theorem 可一致延伸，使任意
`ab<=XL^K,K<3` 无条件闭合。剩余主质量仍在 fixed-power high-product 区；任何
fixed log saving 对 positive local-energy ledger都不足。
