# 213. Radial alias seam 的精确支撑间隙与迹类闭合

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 NCE-8 / response-specific aperture Gram

状态：有限 Toeplitz 平移迹恒等式、\(\pm L\) alias 主符号逐原子正间隙、
Hankel 迹类总预算与 \(\pm2L\) seam 排空为 [T]；有限审计为 [E]；ordinary
neighboring aperture seam 为 [O]。

## 1. 本轮结论

笔记 212 把 primitive hyperbolic alternating sector 的开放输入压成普通邻接、
\(\pm L\) 与 \(\pm2L\) 三类 aperture seams。本轮闭合后两类。

核心现象不是 unshifted symbols 的端点小重叠，而是更强的 **translated support
gap**。若

\[
 s=\log(a/b),\qquad t=\log(c/d),\qquad
 \Delta=s-t=L-\varepsilon,
\tag{1}
\]

且 \(|\varepsilon|<\log2\)，则 finite Toeplitz trace 主项使用
\(Q_t(u-\Delta)=Q_t(u+\varepsilon)\)，而非 \(Q_t(u)\)。在
\(ab,cd\le X\) 下，这两个物理支撑之间的间隙恰为

\[
 \boxed{\log b\ge\log2.}
\tag{2}
\]

因此 \(\pm L\) alias 的 bulk-symbol 主项逐原子严格为零；有限截断只留下可由
trace norm 求和的 Hankel 余项。选取足够窄但固定的 aperture 后，bulk alias
seams 总贡献为

\[
 O\!\left(\frac{N\log L}{L^4}\right),
\tag{3}
\]

而加回 finite/bulk transfer 后的真实 finite alias seams 仍为 \(o(N)\)。

另一方面，双曲约束直接给

\[
 |s-t|\le2L-4\log2,
\tag{4}
\]

所以足够窄的 \(\pm2L\) seam 根本没有算术原子。

笔记 212-H 因而严格缩小为唯一的 **ordinary neighboring aperture seam**；
没有使用零点、RH、完整 Weil 正性或任意系数 Bessel 假设。

## 2. 精确 finite Toeplitz 平移迹恒等式

令 \(h_0=2\pi/L\)，

\[
 D_d(x)=\operatorname{diag}_{0\le k<d}(e^{ikh_0x}),
\tag{5}
\]

并令 \(T_d(f)=(\widehat f(j-k))_{0\le j,k<d}\)。沿用笔记 204 的
cross-boundary Hankel 余项

\[
 \mathcal H_d(f,g)
 =P_dL(f)(I-P_d)L(g)P_d,
\tag{6}
\]

故

\[
 T_d(f)T_d(g)=T_d(fg)-\mathcal H_d(f,g).
\tag{7}
\]

定义周期平移

\[
 g^{[x]}(u)=g(u-x).
\tag{8}
\]

### 定理 213-A（translated-symbol finite trace identity）[T]

若 \(f,g\) 为实值周期符号，则

\[
 \begin{aligned}
 &\operatorname{tr}\bigl(T_d(f)D_d(\Delta)T_d(g)\bigr)\\
 &\quad=
 \widehat{f g^{[\Delta]}}(0)
 \sum_{k=0}^{d-1}e^{ikh_0\Delta}
 -\operatorname{tr}\bigl(
 \mathcal H_d(f,g^{[\Delta]})D_d(\Delta)
 \bigr).
 \end{aligned}
\tag{9}
\]

特别地，对 singleton bulk response

\[
 F_s=\beta_L^2 e^{iTs}T_d(Q_s)D_d(s),
\tag{10}
\]

取 Hilbert--Schmidt 内积
\(\langle A,B\rangle=\operatorname{tr}(AB^*)\)，有

\[
 \begin{aligned}
 \langle F_s,F_t\rangle_{HS}
 =\beta_L^4e^{iT\Delta}
 \bigg[&
 \widehat{Q_sQ_t^{[\Delta]}}(0)
 \sum_{k=0}^{d-1}e^{ikh_0\Delta}\\
 &-\operatorname{tr}\bigl(
 \mathcal H_d(Q_s,Q_t^{[\Delta]})D_d(\Delta)
 \bigr)\bigg].
 \end{aligned}
\tag{11}
\]

#### 证明

直接计算 matrix entries 得

\[
 D_d(\Delta)T_d(g)D_d(-\Delta)=T_d(g^{[\Delta]}),
\tag{12}
\]

即

\[
 D_d(\Delta)T_d(g)=T_d(g^{[\Delta]})D_d(\Delta).
\]

将式 (7) 用于 \(f,g^{[\Delta]}\)，再取 trace。Toeplitz matrix
\(T_d(fg^{[\Delta]})\) 的所有 diagonal entries 都等于
\(\widehat{fg^{[\Delta]}}(0)\)，故得到式 (9)。式 (11) 再由
\(T_d(Q_t)^*=T_d(Q_t)\) 得到。\(\square\)

式 (11) 是本轮的关键审计点。仅观察 Dirichlet kernel 在
\(\Delta\equiv0\pmod L\) 变大，会漏掉与它同时出现的 translated-symbol
overlap。

## 3. 单个 radial symbol 的精确支撑

写

\[
 x_n=\log n,
 \qquad s=x_a-x_b,
\]

并沿用笔记 211 的精确符号

\[
 Q_{a/b}(u)
 =b_ab_b\,\phi(u)\phi(u-s)\phi(x_a-u)^2,
\tag{13}
\]

其中 \(\phi\) 支持在 \([-L/2,L/2]\)，并把右端看成长度 \(L\) 的周期。

### 引理 213-B（radial support intervals）[T]

若 \(ab\le X\)，则在基本周期内：

\[
 \operatorname{supp}Q_{a/b}\subset
 \begin{cases}
 [x_a-L/2,L/2],&s\ge0,\\
 [x_a-L/2,L/2+s],&s\le0.
 \end{cases}
\tag{14}
\]

#### 证明

三个 window factors 分别要求

\[
 u\in[-L/2,L/2],\quad
 u\in[s-L/2,s+L/2],\quad
 u\in[x_a-L/2,x_a+L/2].
\]

取三个 intervals 的交。若 \(s\ge0\)，则 \(x_a=s+x_b\ge s\)，故左端为
\(x_a-L/2\)，右端为 \(L/2\)。若 \(s\le0\)，左端仍为
\(x_a-L/2\)，右端为 \(L/2+s\)。\(\square\)

该引理只使用 compact support；不需要端点消失阶。

## 4. \(+L\) alias 的精确正间隙

由 \(a,b\ge2\) 与 \(ab\le X\)，

\[
 -L+2\log2\le \log(a/b)\le L-2\log2.
\tag{15}
\]

### 定理 213-C（atomic \(+L\) translated-support gap）[T]

设 \(ab,cd\le X\)，并满足式 (1) 与
\(|\varepsilon|<\log2\)。则 \(s\ge0\)、\(t\le0\)，且在同一个基本周期内
\(Q_s\) 与 \(Q_t^{[\Delta]}\) 的支撑不绕回并严格不交。更精确地，

\[
 \operatorname{dist}
 \bigl(\operatorname{supp}Q_t^{[\Delta]},
       \operatorname{supp}Q_s\bigr)
 \ge x_b=\log b.
\tag{16}
\]

因此

\[
 \widehat{Q_sQ_t^{[\Delta]}}(0)=0.
\tag{17}
\]

#### 证明

若 \(s<0\)，由式 (15) 有

\[
 \Delta=s-t<L-2\log2<L-\log2,
\]

与 \(\Delta=L-\varepsilon>L-\log2\) 矛盾，故 \(s\ge0\)。同理若
\(t>0\)，则 \(\Delta\le s<L-\log2\)，仍矛盾；所以 \(t\le0\)。

因 \(\Delta=L-\varepsilon\)，周期平移 \(u\mapsto u-\Delta\) 等同于
\(u\mapsto u+\varepsilon\)。由引理 213-B，

\[
 \operatorname{supp}Q_t^{[\Delta]}
 \subset
 [x_c-L/2-\varepsilon,\ L/2+t-\varepsilon].
\tag{18}
\]

当 \(\varepsilon>0\) 时，\(\varepsilon<\log2\le x_c\)；当
\(\varepsilon\le0\) 时更显然。因此式 (18) 的左端不越过 \(-L/2\)。其右端
利用 \(\varepsilon=L-s+t\) 化为

\[
 L/2+t-\varepsilon=-L/2+s\le L/2-2\log2,
\tag{19}
\]

也不越过右端，故没有周期绕回。

另一方面，\(Q_s\) 的支撑左端为

\[
 x_a-L/2=s+x_b-L/2.
\]

它与式 (19) 的差正好是 \(x_b\)。这证明式 (16)--(17)。\(\square\)

交换两原子并取共轭，得到完全相同的 \(-L\) 结论。

## 5. Hankel 余项的 trace-norm 预算

定义 boundary Fourier energy

\[
 \mathfrak b_d(f)
 =\sum_{r\in\mathbb Z}\min(d,|r|)|\widehat f(r)|^2.
\tag{20}
\]

笔记 204 的 uniform window estimate 对式 (13) 给

\[
 \mathfrak b_d(Q_{a/b})
 \ll(1+\log L)|b_ab_b|^2,
\tag{21}
\]

且平移不改变该量。

### 引理 213-D（trace-class finite-section remainder）[T]

对任意符号 \(f,g\)，

\[
 \|\mathcal H_d(f,g)\|_{S_1}
 \le \mathfrak b_d(f)^{1/2}\mathfrak b_d(g)^{1/2}.
\tag{22}
\]

因此

\[
 \left|
 \operatorname{tr}(\mathcal H_d(f,g)D_d(\Delta))
 \right|
 \le \mathfrak b_d(f)^{1/2}\mathfrak b_d(g)^{1/2}.
\tag{23}
\]

#### 证明

把式 (6) 写成 \(AB\)，其中

\[
 A=P_dL(f)(I-P_d),\qquad
 B=(I-P_d)L(g)P_d.
\]

Schatten Hölder 给 \(\|AB\|_{S_1}\le\|A\|_{S_2}\|B\|_{S_2}\)。
crossing-pair 恒等式给
\(\|A\|_{S_2}^2=\mathfrak b_d(f)\)、
\(\|B\|_{S_2}^2=\mathfrak b_d(g)\)，证明式 (22)。式 (23) 由
\(D_d(\Delta)\) 酉及 trace duality 得到。\(\square\)

这里必须用 trace norm；若只用
\(|\operatorname{tr}(HD)|\le\sqrt d\|H\|_{HS}\)，会人为引入不可接受的
\(\sqrt d\) 损失。

## 6. 全部 \(\pm L\) aperture seams 闭合

把 real ratio 轴分成长度 \(\omega\) 的 intervals，并固定

\[
 0<4\omega<\log2.
\tag{24}
\]

若两个 aperture intervals 与 \(+L\) diagonal 的距离至多 \(2\omega\)，则其中
任意原子对都满足

\[
 |(s-t)-L|<4\omega<\log2.
\tag{25}
\]

### 定理 213-E（global \(\pm L\) alias seam evacuation）[T]

令 \(\mathcal E_{\pm L}\) 为上述 \(\pm L\) aperture seam edges。对笔记 212
的 primitive hyperbolic blocks，bulk 版本有

\[
 \boxed{
 \sum_{(\nu,\mu)\in\mathcal E_{\pm L}}
 |K^{bulk}_{\nu\mu}|
 \ll \frac{N(1+\log L)}{L^4}.}
\tag{26}
\]

对真实 finite blocks 则有

\[
 \sum_{(\nu,\mu)\in\mathcal E_{\pm L}}
 |K^{fin}_{\nu\mu}|
 \ll \frac{N\sqrt{1+\log L}}{L^2}=o(N).
\tag{26a}
\]

#### 证明

先考虑 bulk blocks。由定理 213-C，式 (11) 的 symbol-overlap 主项对每个
alias atom pair 都严格为零。式 (21)、引理 213-D 于是把单对余项控制为

\[
 \ll \beta_L^4(1+\log L)
 |b_ab_bb_cb_d|.
\tag{27}
\]

定理 212-B 给每个 aperture 的 coefficient mass
\(\mathscr M_\nu\ll\sqrt X\)。alias graph 有 \(O(L)\) 条边，因此把式 (27)
按 atom pairs 与 aperture edges 绝对求和得到

\[
 \beta_L^4(1+\log L)
 \sum_{(\nu,\mu)\in\mathcal E_{\pm L}}
 \mathscr M_\nu\mathscr M_\mu
 \ll
 \frac{LX(1+\log L)}{L^4}
 =\frac{N(1+\log L)}{L^4}.
\tag{28}
\]

最后用笔记 212-(16c) 的 bounded-degree absolute finite/bulk transfer bound，
将式 (26) 与逐边差的绝对值求和，得到式 (26a)。因此真实 finite blocks 的
\(\pm L\) seam 总贡献为 \(o(N)\)。\(\square\)

注意：式 (26) 对 bulk alias blocks 给出显示的 \(L^{-4}\) 相对增益；finite
transfer 只承诺总体 \(o(N)\)，不应把更强的 bulk rate 未经证明地赋给 finite
blocks。

## 7. \(\pm2L\) seam 排空

### 定理 213-F（hyperbolic ratio diameter excludes \(\pm2L\) aliases）[T]

在 \(ab,cd\le X\)、\(a,b,c,d\ge2\) 下，

\[
 |s-t|\le2L-4\log2.
\tag{29}
\]

因此在式 (24) 的 aperture partition 中，不存在距离 \(\pm2L\) diagonal 至多
\(2\omega\) 的算术 seam edge。

#### 证明

式 (29) 由式 (15) 立即得到。任一候选 aperture edge 内的原子差与
\(\pm2L\) 的距离小于 \(4\omega<\log2\)，但式 (29) 说明该距离至少
\(4\log2\)，矛盾。\(\square\)

这一步使用了所有 prime powers 至少为 \(2\)。若模型允许趋于 \(1\) 的连续
算术尺度，\(\pm2L\) 排空不再自动成立。

## 8. 修正后的唯一 aperture 最小引理 [O]

### 开放引理 213-G（ordinary neighboring aperture budget）[O]

令 \(\mathcal E_0\) 只包含 real differences 接近 \(0\) 的普通相邻 apertures。
对真实 primitive hyperbolic finite blocks，证明

\[
 \boxed{
 2\operatorname{Re}
 \sum_{(\nu,\mu)\in\mathcal E_0,\ \nu<\mu}
 K_{\nu\mu}=o(N),}
\tag{30}
\]

或给出足以跨越四矩比例阈值的一侧常数。

该问题不能再利用 alias translation 的正支撑间隙：当 \(s-t=O(1)\) 时，
translated symbols 具有主尺度重叠。笔记 212-G 的 PSD path 反例也继续适用，
故 local norm、bounded degree 与逐边 \(o(N)\) 均不充分。下一轮应直接研究
ordinary edge 的 overlap kernel

\[
 \widehat{Q_sQ_t^{[s-t]}}(0)
\tag{31}
\]

是否存在 response-specific telescoping、符号规则或可求和的一侧 Schur gain。

## 9. 公理作用、删除审计与循环性

1. **exact Toeplitz modulation covariance**：负责把 alias Dirichlet resonance
   与 translated overlap 绑定。删除后只能看到一个错误的“大 Dirichlet kernel”。
2. **compactly supported physical window**：负责支撑区间与严格零 overlap。
   若 window 只有快速衰减，结论改成尾重叠估计，不能直接写成零。
3. **product cutoff \(ab,cd\le X\)**：负责 ratio range (15) 与 sign forcing；
   删除后支撑区间可绕回，\(\pm2L\) 也可能真实存在。
4. **算术原子 \(a,b,c,d\ge2\)**：给正间隙 \(\log2\)。若允许尺度趋于 \(1\)，
   统一 gap 消失。
5. **uniform boundary Fourier energy**：只控制 finite Hankel remainder，不产生
   主项消失。
6. **aperture mass budget \(\mathscr M_\nu\ll\sqrt X\)**：负责从逐原子余项到
   全部 alias seams 的一致求和。

删除审计：

- 忽略 translated symbol 会把本轮机制错写为 endpoint smallness；式 (9) 说明这
  不是正确有限代数。
- 主 symbol overlap 为零不等于 finite Toeplitz cross Gram 为零；
  \(\mathcal H_d\) 是必须保留的边界项。
- 若只用 HS norm 控制 trace，会多付 \(\sqrt d\)；引理 213-D 的 trace-class
  factorization 是闭合总预算的必要层。
- 定理 213-E 是 prime-side finite response 估计，不引用 zero-side positivity、
  RH、GRH、简单零点比例或负指数一致有界。

结论不是公理改写：公理只给 modulation covariance、window support、双曲 cutoff
和局部能量；正间隙 \(\log b\) 来自它们的精确几何组合。ordinary seam 仍开放，
所以本轮没有把完整四矩或 RH 隐藏进公理。

## 10. 模型范围

- Riemann zeta 与固定本原 Dirichlet \(L\) 函数：比值支撑和 cutoff 几何相同；
  character phases 只进入 coefficients，不破坏逐原子零 overlap。
- Dedekind/automorphic \(L\) 函数：若局部参数仍由整数 \(n\ge2\) 索引且可取得
  aperture \(\ell^1\) mass budget，则几何部分保留；系数预算需另证。
- 函数域：degree lattice 提供离散端点间隙，但周期长度和最小正 degree 的归一化
  必须重做。
- 只有函数方程而无整数双曲 cutoff 的负向模型：定理 213-C、213-F 通常不适用，
  可作为检验该结果确实是算术结构而非函数方程同义反复的模型。

## 11. 可复现审计 [E]

脚本 `scripts/alias_seam_overlap_audit.py` 检查：

1. 随机有限 Hermitian Toeplitz symbols 的式 (9)，包括平移符号的正负号；
2. \(X=1000,5000,20000\) 的实际 prime-power hyperbola 中，所有抽取到的
   \(|(s-t)-L|<0.5\) alias pairs 的无绕回与支撑间隙；
3. 最小观测间隙为 \(0.693147\ldots=\log2\)；
4. ratio diameter 与 \(2L\) 的距离接近并不小于 \(4\log2\)；
5. Hankel remainder 的 nuclear norm 不超过两个 crossing factors 的
   Hilbert--Schmidt norm 乘积。

这些有限检查只审计恒等式、符号方向、索引和 sharp endpoint geometry；解析结论
来自上面的证明，而不是由有限样本外推。
