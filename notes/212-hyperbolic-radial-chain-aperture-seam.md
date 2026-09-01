# 212. Hyperbolic radial-chain closure 与 aperture seam compression

日期：2026-09-02

分支：MOM-1 / 路线 A2，接口 NCE-8 / response-specific aperture Gram

状态：双曲 ratio 实频间距、固定 aperture 的 \(L^3\) symbol budget 与
\(\sqrt X\) mass budget、整条 radial chain 的 \(O(N/L)\) finite bound、
非 seam aperture cross terms 的绝对可和 evacuation、有限维 seam compression
为 [T]；bounded-degree PSD seam no-go 为 [N]；actual aperture seam response
预算为 [O]；有限审计为 [E]。

## 1. 本轮结论

笔记 211 把同一 ratio aperture 内的 radial chain 行和留作 [O]。本轮发现该
绝对行和条件过强：双曲限制 \(ab\le X\) 已经给足够的真实频率分离，使整条
radial chain 可直接用 signed Montgomery--Vaughan mean square 闭合。

主要结论如下。

1. 若

   \[
    ab\le X,\qquad cd\le X,
   \]

   且 \(a/b\ne c/d\)，则

   \[
    |\log(a/b)-\log(c/d)|\gg X^{-1}.
   \tag{1}
   \]

2. 固定宽度 \(O(1)\) 的 real log-ratio aperture 后，所有 primitive
   prime-power pairs 的 symbol energy 与 coefficient mass 分别满足

   \[
    \mathscr S_\nu\ll L^3,
    \qquad \mathscr M_\nu\ll\sqrt X.
   \tag{2}
   \]

3. 该 aperture 内全部 radial scales 的真实 finite aggregate \(H_\nu\) 满足

   \[
    \boxed{\|H_\nu\|_{HS}^2\ll N/L=o(N).}
   \tag{3}
   \]

   因此开放引理 211-I 不再是必要输入。
4. 把 real log-ratio 轴分成 \(O(L)\) 个 fixed-width apertures。除下列
   **seam pairs** 外，所有 aperture cross terms 的绝对值总和为 \(o(N)\)：

   - 普通相邻 apertures，\(s_\nu-s_\mu\approx0\)；
   - Gabor circular aliases，\(s_\nu-s_\mu\approx\pm L,\pm2L\)。

5. seam graph 只有 \(O(L)\) 条边，但 local norm 与 bounded degree 仍不足以闭合：
   存在 PSD path Gram，每个 block 的能量为 \(N/L\)，每条 seam edge 为
   \(N/(4L)=o(N)\)，全部 seam excess 却趋于 \(N/2\)。

因此 primitive hyperbolic alternating hard input 已从约 \(X^2\) 个 ratio atoms
压缩成一个 \(O(L)\)-vertex、\(O(L)\)-edge 的 **actual aperture seam Gram**。

## 2. Hyperbolic ratio spacing

### 引理 212-A（global real-log spacing under product cutoff）[T]

设 \(a,b,c,d\in\mathbb N\)，\(ab,cd\le X\)，且 \(a/b\ne c/d\)。则式
(1) 成立；可取 \(1/(2X)\) 作为充分下界。

#### 证明

不妨设

\[
 t=\frac{a/b}{c/d}=\frac{ad}{bc}>1.
\]

若 \(t\ge2\)，则 \(\log t\ge\log2\ge1/(2X)\)。若 \(1<t<2\)，则
\(ad>bc\)，而

\[
 (ad)(bc)=abcd=(ab)(cd)\le X^2.
\]

因此 \(bc\le X\)。又 \(ad-bc\) 是非零整数，所以

\[
 t-1=\frac{ad-bc}{bc}\ge\frac1X.
\]

利用 \(\log t\ge(t-1)/t\) 与 \(t<2\)，得到
\(\log t\ge1/(2X)\)。\(\square\)

式 (1) 是 **real** log-frequency 下界。对整个 \([-L,L]\) 直接模 \(L\)
后会出现差接近 \(\pm L,\pm2L\) 的 circular aliases；只有在 fixed-width real
aperture 内才能无条件转成圆周间距。后文将 alias pairs 显式保留在 seam graph，
而不是忽略 wrap-around。

## 3. Fixed-aperture arithmetic budgets

沿用

\[
 b_n=-\frac1{2\pi}\frac{\Lambda(n)}{\sqrt n}.
\]

固定 \(\omega>0\)，并令

\[
 \mathcal A_\nu
 =\left\{(a,b):
 \Lambda(a)\Lambda(b)\ne0,
 \operatorname{base}(a)\ne\operatorname{base}(b),
 ab\le X,
 \nu\le\log(a/b)<\nu+\omega
 \right\}.
\tag{4}
\]

定义

\[
 \mathscr S_\nu
 =\sum_{(a,b)\in\mathcal A_\nu}
 \sum_r|\widehat Q_{a/b}(r)|^2,
\tag{5}
\]

\[
 \mathscr M_\nu
 =\sum_{(a,b)\in\mathcal A_\nu}|b_ab_b|.
\tag{6}
\]

### 定理 212-B（one-log radial budget saving）[T]

对 fixed \(\omega\)，一致地有式 (2)。

#### 证明

按

\[
 2^p\le a<2^{p+1},
 \qquad 2^q\le b<2^{q+1}
\]

作 dyadic 分解。aperture 条件把 \(p-q\) 限制在只依赖 \(\omega\) 的有限个
整数中；乘积条件给 \(p+q\le\log_2X+O(1)\)。故 admissible dyadic
rectangles 只有 \(O_\omega(L)\) 个。

在每个 rectangle 上，笔记 210-A、210-C 给

\[
 \sum_{a,b}|b_a|^2|b_b|^2\ll L^2.
\]

Parseval 与 singleton classification 因而给
\(\mathscr S_\nu\ll L^3\)。另一方面，同一 rectangle 的 \(\ell^1\) mass
至多

\[
 W_1(2^p)W_1(2^q)\ll2^{(p+q)/2}.
\]

当固定 \(p-q\) 并增加 radial scale 时，该上界构成几何级数，最后一项由
\(2^{p+q}\ll X\) 控制。因此总和为 \(O_\omega(\sqrt X)\)，证明式
(2)。\(\square\)

这里的一个 log saving 来自 fixed aperture 把二维 \((p,q)\) dyadic lattice
压成一条 radial chain；没有使用素数对相关或零点信息。

## 4. Entire radial chain closure

定义

\[
 H_\nu^{fin}
 =\sum_{(a,b)\in\mathcal A_\nu}F_{a/b}^{fin},
 \qquad
 H_\nu^{bulk}
 =\sum_{(a,b)\in\mathcal A_\nu}F_{a/b}^{bulk}.
\tag{7}
\]

### 定理 212-C（fixed-aperture radial-chain bound）[T]

在 \(T\asymp X\)、\(N\asymp XL\) 下，式 (3) 成立。

#### 证明：bulk

同一 aperture 内 real log differences 小于 \(\omega\)。当 \(L>2\omega\) 时
不存在 circular wrap。引理 212-A 因而给 frequencies
\(s_{a/b}/L\pmod1\) 的间距

\[
 \Delta_\nu\gg\frac1{LX}.
\tag{8}
\]

在 exact diagonal-fibre identity 上应用定理 205-B，再用定理 212-B：

\[
 \begin{aligned}
 \|H_\nu^{bulk}\|_{HS}^2
 &\ll
 \beta_L^4(d+LX)\mathscr S_\nu\\
 &\ll L^{-4}(N+LX)L^3
 \ll N/L.
 \end{aligned}
\tag{9}
\]

这里同时控制 diagonal 与 within-aperture off-diagonal；没有把任意 matrix
coefficients 代入 Bessel 界。

#### 证明：finite transfer

由 uniform Hankel estimate 与三角不等式，

\[
 \begin{aligned}
 \|H_\nu^{fin}-H_\nu^{bulk}\|_{HS}^2
 &\ll
 \beta_L^4(1+\log L)\mathscr M_\nu^2\\
 &\ll \frac{X(1+\log L)}{L^4}
 =o(N/L).
 \end{aligned}
\tag{10}
\]

式 (9)--(10) 给式 (3)。\(\square\)

### 推论 212-D（note 211-I is unnecessary）[T]

对笔记 211 的任一 dyadic radial chain \(A_jB_j\le X\)，不需要证明 absolute
coherence row sum 211-(20)；包含该 chain 的 fixed aperture aggregate 已由定理
212-C 直接满足 \(O(N/L)\)。\(\square\)

这不证明 absolute row sum 本身为 \(o(L)\)；它证明 signed physical response
可由更弱、更贴近目标的 Montgomery--Vaughan 结构闭合。

## 5. Far-aperture evacuation

把 real interval \([-L,L]\) 分成长度 \(\omega\) 的 apertures
\(I_\nu\)，总数 \(J=O(L)\)。对两个 intervals 定义 circular separation

\[
 \delta_{\nu\mu}
 =\inf_{s\in I_\nu,t\in I_\mu}
 \operatorname{dist}(s-t,L\mathbb Z).
\tag{11}
\]

若 \(\delta_{\nu\mu}>0\)，finite geometric sums 满足

\[
 \left|\sum_{k\in I_r}e^{ikh_0(s-t)}\right|
 \ll\frac{L}{\delta_{\nu\mu}}.
\tag{12}
\]

### 定理 212-E（non-seam aperture cross evacuation）[T]

令 \(\mathcal E_{seam}\) 包含 \(\delta_{\nu\mu}\le2\omega\) 的 block pairs。
则 \(\#\mathcal E_{seam}=O(L)\)，且

\[
 \boxed{
 \sum_{\substack{\nu<\mu\\(\nu,\mu)\notin\mathcal E_{seam}}}
 |\langle H_\nu^{bulk},H_\mu^{bulk}\rangle_{HS}|
 \ll \frac{N\log L}{L^3}=o(N).}
\tag{13}
\]

seam pairs 恰位于 real differences 接近 \(0,\pm L,\pm2L\) 的有限宽
diagonals。

#### 证明

对固定 ratio pair，Cauchy--Schwarz in Fourier modes 给

\[
 \sum_r|\widehat Q_{a/b}(r)\widehat Q_{c/d}(r)|
 \le |b_ab_bb_cb_d|.
\tag{14}
\]

式 (12)、(14) 与定理 212-B 因而给

\[
 |\langle H_\nu^{bulk},H_\mu^{bulk}\rangle|
 \ll
 \beta_L^4\frac{L}{\delta_{\nu\mu}}
 \mathscr M_\nu\mathscr M_\mu
 \ll\frac{N}{L^4\delta_{\nu\mu}}.
\tag{15}
\]

对 fixed \(\nu\)，非 seam intervals 的 reciprocal circular distances 之和为
\(O(\log L)\)。再对 \(J=O(L)\) 个 \(\nu\) 求和得到式 (13)。

在长度 \(2L\) 的 real range 中，每个 interval 只在 \(0,\pm L,\pm2L\)
附近有 \(O(1)\) 个 seam partners，故 seam edges 总数为 \(O(L)\)。
\(\square\)

### 引理 212-F（global finite defect evacuation）[T]

所有 apertures 的 finite defects 总和满足

\[
 \left\|\sum_\nu(H_\nu^{fin}-H_\nu^{bulk})\right\|_{HS}^2
 \ll\frac{X(1+\log L)}{L^2}=o(N).
\tag{16}
\]

#### 证明

定理 212-B 给每个 aperture \(\mathscr M_\nu\ll\sqrt X\)，而上述 dyadic
geometric sum 对全部 apertures 合计更精确地给
\(\sum_\nu\mathscr M_\nu\ll L\sqrt X\)。把该 \(\ell^1\) mass 代入 uniform
Hankel triangle bound，得到

\[
 \beta_L^4(1+\log L)L^2X
 \ll X(1+\log L)/L^2.
\]

这证明式 (16)。另一方面，定理 212-C 给

\[
 \sum_\nu\|H_\nu^{bulk}\|_{HS}^2=O(N),
 \qquad J=O(L),
\]

故 Cauchy 给
\(\|\sum_\nu H_\nu^{bulk}\|_{HS}^2=O(NL)\)。式 (16) 与
\(|\|B+E\|^2-\|B\|^2|\le2\|B\|\|E\|+\|E\|^2\) 因而给

\[
 \left|
 \left\|\sum_\nu H_\nu^{fin}\right\|_{HS}^2
 -\left\|\sum_\nu H_\nu^{bulk}\right\|_{HS}^2
 \right|
 \ll \frac{N\sqrt{1+\log L}}{L}=o(N).
\tag{16a}
\]

还需审计 seam 的逐 block transfer。由 \(\mathscr M_\nu\ll\sqrt X\)，每个
\(E_\nu=H_\nu^{fin}-H_\nu^{bulk}\) 满足

\[
 \|E_\nu\|_{HS}^2
 \ll\frac{X(1+\log L)}{L^4}
 =\frac{N(1+\log L)}{L^5}.
\tag{16b}
\]

seam graph 的 degree 为 \(O(1)\)，且定理 212-C 给
\(\|H_\nu^{bulk}\|^2\ll N/L\)。因此逐边 Cauchy--Schwarz 给

\[
 \sum_{(\nu,\mu)\in\mathcal E_{seam}}
 \left|
 \langle H_\nu^{fin},H_\mu^{fin}\rangle
 -\langle H_\nu^{bulk},H_\mu^{bulk}\rangle
 \right|
 \ll\frac{N\sqrt{1+\log L}}{L^2}=o(N).
\tag{16c}
\]

相同估计也给 finite/bulk aperture diagonal sums 相差 \(o(N)\)。所以
finite-to-bulk boundary 不会重新制造被式 (13) 删除的 far-aperture coherence，
也允许在下一节使用真实 finite seam blocks。\(\square\)

## 6. Seam Gram compression

定义 aperture block Gram

\[
 K_{\nu\mu}=\langle H_\nu^{fin},H_\mu^{fin}\rangle_{HS}.
\tag{17}
\]

由定理 212-C，

\[
 K_{\nu\nu}\ll N/L,
 \qquad \sum_\nu K_{\nu\nu}=O(N).
\tag{18}
\]

定理 212-E 与引理 212-F 说明，primitive hyperbolic aggregate 除 \(o(N)\)
外只剩

\[
 \boxed{
 2\operatorname{Re}
 \sum_{(\nu,\mu)\in\mathcal E_{seam},\ \nu<\mu}
 K_{\nu\mu}.}
\tag{19}
\]

这是一个 \(O(L)\)-vertex、\(O(L)\)-edge 的 actual response Gram，而不是
原先的 \(X^2\)-scale arbitrary Farey family。

## 7. Bounded-degree seam is still insufficient

### 障碍定理 212-G（PSD path seam can retain main-scale excess）[N]

对 \(J=\lfloor L\rfloor\)，存在 PSD Gram matrix \(K\)，满足

\[
 K_{jj}=N/L,
 \qquad K_{j,j+1}=K_{j+1,j}=N/(4L),
\tag{20}
\]

其余 off-diagonal entries 为零，但

\[
 2\sum_{j=1}^{J-1}K_{j,j+1}\sim N/2.
\tag{21}
\]

#### 证明

式 (20) 的 matrix 是 diagonal 为 \(N/L\)、相邻 off-diagonal 为
\(N/(4L)\) 的 tridiagonal Toeplitz matrix。其 eigenvalues 为

\[
 \frac NL\left(1+\frac12\cos\frac{k\pi}{J+1}\right),
 \qquad1\le k\le J,
\]

全部为正。式 (21) 直接求和即得。\(\square\)

所以即使 far cross 已清除、seam graph degree 一致有界、每条 edge 都是
\(o(N)\)，仍不能推出 seam excess 为 \(o(N)\)。需要实际响应的一侧平均增益。

## 8. 修正后的下一最小引理 [O]

### 开放引理 212-H（actual aperture seam budget）[O]

对式 (17) 的真实 prime-power Toeplitz blocks，证明

\[
 \boxed{
 2\operatorname{Re}
 \sum_{(\nu,\mu)\in\mathcal E_{seam},\ \nu<\mu}
 K_{\nu\mu}=o(N),}
\tag{22}
\]


或证明满足完整四矩阈值的显式一侧上界。估计必须分别处理：

1. ordinary neighboring apertures；
2. \(\pm L\) circular alias seams；
3. \(\pm2L\) endpoint seam；
4. Type I/II/continuum/Gamma 在同一 seam 上的 actual cross response。

一个更小、可证伪的第一步是证明所有 \(\pm L\) alias seam symbols 的总 overlap
energy 为 \(o(N)\)，利用式 211-(9) 的 endpoint factor，而不是假设圆周频率自动
分离。

## 9. 公理作用、删除审计与循环性

1. **product cutoff \(ab\le X\)**：负责引理 212-A。删除后 \(bc\le X\) 的
   关键推论失效。
2. **fixed real aperture**：把 dyadic lattice 降一维并避免内部 circular wrap；
   删除后 symbol budget 回到 \(L^4\)。
3. **local von Mangoldt budgets**：负责式 (2)，不产生 seam cancellation。
4. **Toeplitz diagonal fibres**：负责定理 212-C 的 scalar Montgomery--Vaughan
   应用。
5. **endpoint/window structure**：尚未用于闭合 alias seams；它是开放引理
   212-H 的候选独立输入，不能被描述为已经产生正性。

删除审计：

- 只保留 block norm 与 bounded seam degree 时，定理 212-G 给主尺度 PSD 反例。
- 忽略 circular alias 会错误地把 real spacing (1) 当成全局圆周 spacing；本笔记
  显式保留 \(\pm L,\pm2L\) seams。
- 式 (22) 是 prime-side finite response budget，不使用 zeros；但它本身仍是 [O]，
  没有被包装成 Weil positivity 或 negative-index axiom。

结论边界：

- 本轮只处理 primitive hyperbolic sector \(ab\le X\)。中心 ratio、同素数
  chains 与 \(ab>X\) sector 仍按笔记 209--211 分开处理。
- 没有证明完整 alternating 四矩或改善零点比例。
- \(13/18\) 与 \(16/21\) 仍为条件性目标。

## 10. 模型范围

- zeta 和固定本原 Dirichlet \(L\) 函数共享 product cutoff、ratio spacing 与
  aperture compression；角色相位必须保留在 seam Gram。
- Dedekind/automorphic coefficients 需要 local Rankin--Selberg energy 与 ratio
  multiplicity 分类，不能自动得到 \(L^3\) budget。
- 函数域有界 degree 可使 aperture 数量不增长，但这不建立 cohomological 与
  explicit-formula Weil structures 的等价桥梁。

## 11. 可复现审计 [E]

脚本 `scripts/aperture_radial_chain_audit.py` 检查：

1. prime-power hyperbola 中 \(X\) times minimum real log gap 的正下界；
2. fixed-width apertures 的 \(\mathscr S_\nu/L^3\)、
   \(\mathscr M_\nu/\sqrt X\) 与 block count；
3. non-seam reciprocal circular distances 的 \(O(L\log L)\) 总预算；
4. tridiagonal PSD seam Gram 保留约 \(N/2\) off-diagonal excess。

有限实验只审计索引、尺度和反例，不证明开放式 (22)。

## 12. 后续更新

笔记 213 已证明：足够窄 aperture 下，\(\pm L\) alias 的 translated-symbol
主项逐原子严格为零，finite Hankel 余项总和为 \(o(N)\)；\(\pm2L\) seams
由 ratio diameter 直接排空。因此本笔记的开放引理 212-H 已缩小为 ordinary
neighboring aperture seam budget 213-G。
