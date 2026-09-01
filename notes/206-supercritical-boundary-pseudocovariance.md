# 206. Supercritical boundary 的伪协方差归约与 covariance-blind no-go

日期：2026-09-02

分支：MOM-1 / 路线 A，接口到 NCE-8 / 路线 B

状态：实际 Gabor 响应的复对称性、supercritical aggregate 与 boundary
pseudocovariance 的渐近等价、单因子 boundary energy 上界、physical prime
fibres 公式以及 covariance-blindness 障碍为 [T]/[N]；phase-sensitive
Vaughan 估计和 canonical quarter-turn 为 [O]；有限矩阵检查为 [E]。

## 1. 本轮结论

笔记 205 把 adjacent 通道的唯一剩余有限边界输入写成

\[
 \left\|\sum_{m>X}F_m^{\mathrm{fin}}\right\|_{\mathrm{HS}}^2=o(N).
\tag{1}
\]

该笔记还给出总 product boundary

\[
 -\beta_L^2P_d\mathcal A_X(I-P_d)\mathcal A_XP_d.
\tag{2}
\]

本轮证明式 (2) 不只是式 (1) 的一个较强充分目标。因为笔记 205 已经把
\(m\le X\) defects 的 aggregate 控制为 \(o(\sqrt N)\)，式 (1) 与式
(2) 的 \(o(\sqrt N)\) 控制实际上渐近等价。

更关键的是，实际窗口满足中心反射恒等式

\[
 q_x(x-u)=q_x(u),
\tag{3}
\]

它使无限响应算子 \(\mathcal A_X\) 成为 **complex symmetric**，不是
self-adjoint。令

\[
 P=P_d,\qquad Q=I-P,\qquad B_X=P\mathcal A_XQ.
\tag{4}
\]

则

\[
 P\mathcal A_XQ\mathcal A_XP=B_XB_X^{\mathsf T}.
\tag{5}
\]

所以真正需要消失的对象是 boundary rows 的无共轭伪协方差
\(B_XB_X^{\mathsf T}\)，而不是普通正协方差 \(B_XB_X^*\)。本轮得到

\[
 \boxed{
 \left\|\sum_{m>X}F_m^{\mathrm{fin}}\right\|_{\mathrm{HS}}^2=o(N)
 \iff
 \beta_L^4\|B_XB_X^{\mathsf T}\|_{\mathrm{HS}}^2=o(N).}
\tag{6}
\]

同时无条件证明单因子能量只有主尺度：

\[
 \boxed{
 \beta_L^2\|B_X\|_{\mathrm{HS}}^2\ll N.}
\tag{7}
\]

式 (7) 本身不能推出式 (6)。事实上存在具有完全相同
\(BB^*\)、相同全部奇异值和相同所有 Schatten norms 的矩阵族，其中一族
满足 \(BB^{\mathsf T}=0\)，另一族达到最大 coherent
\(BB^{\mathsf T}\)。因此：

> 若 one-factor block 保持自然非消失尺度，则只读取 covariance、Bessel
> energy 或固定 singular data 不能产生所需 phase cancellation。该 no-go
> 不排除直接证明 \(\beta_L\|B_X\|_{\mathrm{op}}=o(1)\)；笔记 207 证明后者
> 与已知 HS energy bound 合并后足以闭合 supercritical boundary。

缺失输入必须读取无共轭 phase。式 (6) 的 entries 可精确写成两个实际 prime
Dirichlet responses 的乘积，而不是任意长度 \(X^2\) 的 product coefficients；
这给出了与 Vaughan--Brownian 路线的明确接口。

## 2. 实际无限响应与 transpose symmetry

沿用笔记 204--205 的记号：

\[
 L=\log X,\qquad h=\frac{2\pi}{L},\qquad
 \beta_L=\frac{2\pi}{a_LL},\qquad d\asymp TL,
\tag{8}
\]

\[
 b_n=-\frac1{2\pi}\frac{\Lambda(n)}{\sqrt n},
 \qquad x_n=\log n,
\tag{9}
\]

\[
 \mathcal A_X
 =\sum_{n\le X}b_ne^{iTx_n}
 \mathcal L(q_{x_n})D_\infty(x_n).
\tag{10}
\]

这里

\[
 q_x(u)=\phi(u)\phi(x-u)
\tag{11}
\]

先零延拓再按长度 \(L\) 周期化，且

\[
 \widehat q_x(r)=\frac1L\int_{-L/2}^{L/2}
 q_x(u)e^{irhu}\,du.
\tag{12}
\]

### 引理 206-A（centered Fourier reality）[T]

对每个 \(0\le x\le L\)，

\[
 \widehat q_x(-r)=e^{-irhx}\widehat q_x(r).
\tag{13}
\]

因此

\[
 c_x(r):=e^{-irhx/2}\widehat q_x(r)
\tag{14}
\]

为实偶序列：

\[
 c_x(-r)=c_x(r)\in\mathbb R.
\tag{15}
\]

#### 证明

式 (11) 在圆上满足式 (3)。在式 (12) 中作反射
\(u\mapsto x-u\pmod L\)，得到式 (13)。另一方面 \(q_x\) 为实函数，故
\(\widehat q_x(-r)=\overline{\widehat q_x(r)}\)。两式代入式 (14) 即得
式 (15)。\(\square\)

### 定理 206-B（complex-symmetric prime response）[T]

令

\[
 M_x=\mathcal L(q_x)D_\infty(x).
\tag{16}
\]

则

\[
 M_x^{\mathsf T}=M_x,
 \qquad \mathcal A_X^{\mathsf T}=\mathcal A_X.
\tag{17}
\]

并且逐 entries 有精确 physical-response 公式

\[
 (\mathcal A_X)_{j\ell}
 =\sum_{n\le X}b_nc_{x_n}(j-\ell)
 \exp\!\left(
 i\left[T+\frac h2(j+\ell)\right]x_n
 \right).
\tag{18}
\]

#### 证明

若 \(r=j-\ell\)，则由式 (13)

\[
 \begin{aligned}
 (M_x^{\mathsf T})_{j\ell}
 &=(M_x)_{\ell j}
 =\widehat q_x(-r)e^{ijhx}\\
 &=e^{-irhx}\widehat q_x(r)e^{ijhx}
 =\widehat q_x(r)e^{i\ell hx}
 =(M_x)_{j\ell}.
 \end{aligned}
\]

式 (10) 是这些 complex-symmetric 算子的标量线性组合，所以仍为
complex symmetric。再把
\(\widehat q_x(r)=e^{irhx/2}c_x(r)\) 代入
\((M_x)_{j\ell}=\widehat q_x(j-\ell)e^{i\ell hx}\)，即得式
(18)。\(\square\)

这里的 transpose 不带共轭。将它误换成 adjoint 会把问题错误地变成一个正的
boundary covariance，并丢掉需要证明的 phase cancellation。

## 3. Supercritical aggregate 的 exact pseudocovariance equivalence

令

\[
 E_{\le X}
 =\sum_{m\le X}
 \left(F_m^{\mathrm{fin}}-F_m^{\mathrm{bulk}}\right),
 \qquad
 G_{>X}=\sum_{m>X}F_m^{\mathrm{fin}}.
\tag{19}
\]

笔记 205 的式 (25) 已证明

\[
 \|E_{\le X}\|_{\mathrm{HS}}^2=o(N).
\tag{20}
\]

### 定理 206-C（supercritical--circularity equivalence）[T]

取 \(B_X=P\mathcal A_XQ\)。则精确地

\[
 E_{\le X}+G_{>X}
 =-\beta_L^2B_XB_X^{\mathsf T}.
\tag{21}
\]

从而式 (6) 成立。

#### 证明

全部 finite products 等于

\[
 \beta_L^2P\mathcal A_XP\mathcal A_XP,
\]

而全部 Laurent/bulk products 等于

\[
 \beta_L^2P\mathcal A_X^2P.
\]

两者之差为

\[
 -\beta_L^2P\mathcal A_XQ\mathcal A_XP.
\]

由式 (17)，

\[
 Q\mathcal A_XP=(P\mathcal A_XQ)^{\mathsf T}=B_X^{\mathsf T},
\]

故得到式 (21)。再由式 (20) 和三角不等式，

\[
 \|G_{>X}\|_{\mathrm{HS}}=o(\sqrt N)
 \iff
 \beta_L^2\|B_XB_X^{\mathsf T}\|_{\mathrm{HS}}=o(\sqrt N).
\]

平方即为式 (6)。\(\square\)

因此笔记 205 的式 (34) 应读作与 supercritical lemma 渐近等价的
one-factor boundary reformulation，而不是一个未知强度更高的充分条件。

## 4. 单因子 boundary energy 无条件闭合

### 定理 206-D（boundary one-factor Montgomery--Vaughan bound）[T]

在笔记 204 的窗口正则性和 \(T\asymp X\) 下，式 (7) 成立。

#### 证明

若 \(j\in I_d=\{0,\ldots,d-1\}\)、\(\ell\notin I_d\)，令
\(r=j-\ell\ne0\)。由式 (10) 的未中心化 entries，

\[
 (B_X)_{j\ell}
 =\sum_{n\le X}b_ne^{iTx_n}\widehat q_{x_n}(r)
 e^{i\ell hx_n}.
\tag{22}
\]

固定 \(r\)。合法的 \(\ell\) 构成一个连续整数区间，长度恰为

\[
 s_r=\min(d,|r|).
\tag{23}
\]

点 \(x_n/L\pmod1\)、\(2\le n\le X\) 的圆周间距为
\(\gg(LX)^{-1}\)：直接距离由相邻整数给出，绕圆距离由最小整数
\(n=2\) 给出 \(\gg L^{-1}\)。对式 (22) 沿该 \(\ell\)-区间应用
Montgomery--Vaughan 圆周 mean square，得到

\[
 \|B_X\|_{\mathrm{HS}}^2
 \ll
 \sum_{n\le X}|b_n|^2\mathfrak b_d(q_{x_n})
 +LX\sum_{n\le X}|b_n|^2
 \sum_{r\in\mathbb Z}|\widehat q_{x_n}(r)|^2.
\tag{24}
\]

笔记 204 已证明一致边界预算

\[
 \mathfrak b_d(q_x)\ll1+\log L.
\tag{25}
\]

Parseval、\(0\le q_x\le1\) 和 Mertens 二次权给

\[
 \sum_{n\le X}|b_n|^2\ll L^2,
\tag{26}
\]

\[
 \begin{aligned}
 \sum_{n\le X}|b_n|^2
 \sum_r|\widehat q_{x_n}(r)|^2
 &=\frac1L\sum_{n\le X}|b_n|^2\int|q_{x_n}(u)|^2du\\
 &\le\sum_{n\le X}|b_n|^2
 \ll L^2.
 \end{aligned}
\tag{27}
\]

所以

\[
 \|B_X\|_{\mathrm{HS}}^2
 \ll L^2(1+\log L)+XL^3
 \ll XL^3.
\tag{28}
\]

由 \(\beta_L\asymp L^{-1}\)、\(N\asymp XL\)，得到式 (7)。
\(\square\)

式 (7) 是 covariance 尺度，而式 (6) 要求 pseudocovariance 的
little-oh。后者不能通过在式 (24) 中改善绝对常数得到。

## 5. Physical prime fibres 与无共轭 Vaughan 接口

定义实际、带响应的 prime Dirichlet polynomial

\[
 \mathcal P_r(t)
 :=\sum_{n\le X}b_nc_{x_n}(r)n^{it}.
\tag{29}
\]

由式 (18)，

\[
 (B_X)_{j\ell}
 =\mathcal P_{j-\ell}
 \left(T+\frac h2(j+\ell)\right).
\tag{30}
\]

### 推论 206-E（exact boundary pseudocovariance fibres）[T]

对 \(j,k\in I_d\)，

\[
 \boxed{
 (B_XB_X^{\mathsf T})_{jk}
 =\sum_{\ell\notin I_d}
 \mathcal P_{j-\ell}\!\left(T+\frac h2(j+\ell)\right)
 \mathcal P_{k-\ell}\!\left(T+\frac h2(k+\ell)\right).}
\tag{31}
\]

该和按 \(\ell\) 由 Cauchy--Schwarz 收敛。式 (31) 的两个 factors **没有
共轭**；这正是 covariance-blind 方法遗漏的 phase。

因此下一条实际算术输入可写为：

### 开放引理 206-F（Vaughan boundary pseudocovariance）[O]

证明

\[
 \beta_L^4
 \sum_{j,k\in I_d}
 \left|
 \sum_{\ell\notin I_d}
 \mathcal P_{j-\ell}\!\left(T+\frac h2(j+\ell)\right)
 \mathcal P_{k-\ell}\!\left(T+\frac h2(k+\ell)\right)
 \right|^2
 =o(N).
\tag{32}
\]

式 (32) 与式 (1) 渐近等价，但它把未知量严格定位到：

1. 两个长度 \(X\) 的 prime responses，而不是一个长度 \(X^2\) 的任意
   product polynomial；
2. 实际 centered window coefficients \(c_{x_n}(r)\)；
3. 共同 exterior Gabor index \(\ell\)；
4. 无共轭 Type I/II cross phase。

可以对式 (29) 使用逐系数 exact Vaughan identity，再联合估计式 (31) 中的
Type I--Type I、Type I--Type II 和 Type II--Type II 项。不得先对两个
\(\mathcal P\) 分别取绝对值或平方均值；那样只恢复式 (7)。

## 6. Covariance-blindness 是 sharp obstacle

### 定理 206-G（same-covariance pseudocovariance no-go）[N]

对任意 \(r\ge1\)，存在两矩阵
\(B_{\mathrm{coh}},B_{\mathrm{circ}}\in\mathbb C^{r\times2r}\)，使

\[
 B_{\mathrm{coh}}B_{\mathrm{coh}}^*
 =B_{\mathrm{circ}}B_{\mathrm{circ}}^*=I_r,
\tag{33}
\]

因而它们具有相同奇异值及全部 unitarily invariant/Schatten data，但

\[
 B_{\mathrm{coh}}B_{\mathrm{coh}}^{\mathsf T}=I_r,
 \qquad
 B_{\mathrm{circ}}B_{\mathrm{circ}}^{\mathsf T}=0.
\tag{34}
\]

#### 证明

取

\[
 B_{\mathrm{coh}}=[I_r\ \ 0],
 \qquad
 B_{\mathrm{circ}}=2^{-1/2}[I_r\ \ iI_r].
\tag{35}
\]

直接相乘即得式 (33)--(34)。更一般地，

\[
 B_\theta=2^{-1/2}[I_r\ \ e^{i\theta}I_r]
\]

保持 covariance 为 \(I_r\)，而

\[
 B_\theta B_\theta^{\mathsf T}
 =\frac{1+e^{2i\theta}}2I_r
\]

连续遍历从零到最大 coherence 的全部尺度。\(\square\)

所以在同一个固定 nonvanishing singular scale 上，即使把式 (7) 提升为
exact covariance identity 或完整 singular-value distribution，也不能从中
读取式 (6) 所需的额外 circular phase cancellation。这比笔记 205 的任意
Hankel-family rank-one 反例更精确：它直接作用于已经 factorized 的
one-boundary block。另一方面，若能证明整个 block 的 operator norm 满足
\(\beta_L\|B_X\|_{\mathrm{op}}=o(1)\)，则笔记 207 的次乘性证书仍可闭合目标。

## 7. 一个非循环但仍开放的 quarter-turn 充分证书

令 \(J\) 是 exterior space \(Q\ell^2(\mathbb Z)\) 上预先指定的实正交
complex structure：

\[
 J^{\mathsf T}=-J,\qquad J^2=-I.
\tag{36}
\]

置

\[
 \mathcal E_J=B_XJ-iB_X.
\tag{37}
\]

### 命题 206-H（quantitative quarter-turn certificate）[T]

精确地

\[
 2B_XB_X^{\mathsf T}
 =iB_X\mathcal E_J^{\mathsf T}
 +i\mathcal E_JB_X^{\mathsf T}
 +\mathcal E_J\mathcal E_J^{\mathsf T}.
\tag{38}
\]

并且

\[
 \|B_XB_X^{\mathsf T}\|_{\mathrm{HS}}
 \le2\|B_X\|_{\mathrm{HS}}\|\mathcal E_J\|_{\mathrm{op}}.
\tag{39}
\]

因此定理 206-D 加上下列 response-specific estimate：

\[
 \boxed{
 \beta_L\|B_XJ-iB_X\|_{\mathrm{op}}=o(1)}
\tag{40}
\]

足以推出式 (1)。

#### 证明

由 \(JJ^{\mathsf T}=I\)，

\[
 B_XB_X^{\mathsf T}=(B_XJ)(B_XJ)^{\mathsf T}.
\]

把 \(B_XJ=iB_X+\mathcal E_J\) 展开并把
\(-B_XB_X^{\mathsf T}\) 移到左侧，得到式 (38)。再用

\[
 \|UV^{\mathsf T}\|_{\mathrm{HS}}
 \le\|U\|_{\mathrm{HS}}\|V\|_{\mathrm{op}},
 \qquad
 \|\mathcal E_J\|_{\mathrm{HS}}\le2\|B_X\|_{\mathrm{HS}},
\]

得到式 (39)。式 (7)、式 (39)--(40) 给

\[
 \beta_L^4\|B_XB_X^{\mathsf T}\|_{\mathrm{HS}}^2
 \ll
 \left(\beta_L^2\|B_X\|_{\mathrm{HS}}^2\right)
 \left(\beta_L^2\|\mathcal E_J\|_{\mathrm{op}}^2\right)
 =o(N).
\]

再用定理 206-C。\(\square\)

式 (40) 不能作为未经解释的“极化公理”。若 \(J\) 是从目标矩阵事后优化而来，
它可能只是把式 (6) 隐藏进定义。可接受的下一最小引理必须：

1. 从 lower/upper Gabor boundary pairing、Vaughan channel incidence 或
   continuum/Gamma response 独立构造 \(J\)；
2. 逐项证明式 (40)，不能读取 zeta zeros；
3. 若 canonical \(J\) 不满足式 (40)，将失败记录为新的 polarization
   obstruction，而不是继续增加自由参数。

## 8. 与 Weil 型配置的接口及公理删除审计

1. **窗口中心反射**只用于定理 206-B 的 transpose symmetry。删除后总
   boundary 是 \(P\mathcal A Q\mathcal A P\)，但未必是单块
   \(BB^{\mathsf T}\)，circularity 归约失效。
2. **有限 Gabor projection**产生真实 exterior block \(B_X\)。它没有被无限
   Toeplitz 极限丢弃。
3. **Montgomery--Vaughan spacing 与 Mertens square budget**只证明式 (7)，
   不制造式 (6) 的 little-oh。
4. **无共轭 phase information**是式 (32) 的新算术输入。删除它后，定理
   206-G 给出 sharp 反例。
5. **quarter-turn \(J\)** 若能由算术 correspondence 构造，可被解释为显式
   公式型有限极化；当前没有这样的构造，所以不得声称已获得 Weil positivity。

适用范围：

- 对 Riemann zeta，定理 206-A--G 无条件适用。
- 对固定本原 Dirichlet \(L\) 函数，若系数相位进入 \(b_n\)，
  \(\mathcal A^{\mathsf T}=\mathcal A\) 仍成立，因为 transpose symmetry 来自
  每个 response matrix；式 (7) 的绝对预算不变。式 (32) 则必须保留角色相位。
- Dedekind/automorphic 情形需要相应 Rankin--Selberg square budget；不能从
  zeta 的式 (26) 自动推广。
- 函数域模型可检查 Frobenius pairing 是否提供一个 canonical \(J\)，这是
  上同调型极化与显式公式 boundary circularity 之间一个具体、尚未证明等价的
  桥梁问题。

## 9. RH/GRH 循环性与结论边界

- 本轮没有证明式 (1)，没有得到完整 adjacent 四矩，也没有改善零点比例。
- 定理 206-C 只把一个 prime-side finite boundary input 改写成结构更强的实际
  response statement；它不等价于 RH 或完整 Weil positivity。
- 定理 206-D 是无条件大 \(O\) 能量界；不能把 \(O(N)\) 升级为 \(o(N)\)。
- 定理 206-G 排除 natural-scale covariance 自动制造 phase cancellation，
  但不排除 Type I/II phase cancellation，也不排除直接证明 vanishing
  one-factor operator norm。
- 式 (40) 是充分条件而非已知事实；在构造 canonical \(J\) 前，它不进入任何
  零点结论链。
- alternating/Farey、\(3+1\)、\(4+0\)、Gamma/continuum cross terms 仍独立
  开放。

## 10. 可复现检查 [E]

脚本

`scripts/supercritical_pseudocovariance_audit.py`

检查：

1. centered Fourier relation 与 finite response 的 transpose symmetry；
2. boundary factorization \(P\mathcal A Q\mathcal A P=BB^{\mathsf T}\)；
3. physical prime-fibre entry formula；
4. same covariance / different pseudocovariance 反例；
5. quarter-turn identity 与范数上界。

有限实验只核对代数、索引与反例，不证明式 (32)、式 (40) 或任何 zeta
渐近。
