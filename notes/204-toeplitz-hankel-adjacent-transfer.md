# 204. Toeplitz--Hankel adjacent transfer 与有限 Gabor 边界闭合

日期：2026-09-01

分支：MOM-1 / 路线 A

状态：有限 Gabor 响应的 Toeplitz 表示、Hankel 缺陷恒等式、统一边界能量、
adjacent product clusters 的子集一致 finite-to-bulk transfer 及 \(m>X\)
泄漏估计为 [T]；扩展到 alternating ratio Gram、\(3+1\)、\(4+0\) 与完整
signed-kernel 四矩为 [O]；有限矩阵实验为 [E]。

## 1. 结论与严格边界

笔记 203 证明了理想 translation-invariant bulk 中 adjacent exact-product
edge 的 tightness。本轮把真实有限 Gabor 压缩写成 Toeplitz finite section，
并证明其与 bulk surrogate 的 product-cluster 直和差满足

\[
 \sum_m
 \left\|F_m^{\mathrm{fin}}-F_m^{\mathrm{bulk}}\right\|_{\mathrm{HS}}^2
 \ll 1+\log L.
\tag{1}
\]

由于零点主尺度 \(N\asymp TL\)，式 (1) 给出对任意、甚至依赖于 \(T\) 的
乘积集合 \(\mathcal M_T\) 的子集一致传递：

\[
 \left|
 \sum_{m\in\mathcal M_T}\|F_m^{\mathrm{fin}}\|_{\mathrm{HS}}^2
 -
 \sum_{m\in\mathcal M_T}\|F_m^{\mathrm{bulk}}\|_{\mathrm{HS}}^2
 \right|=o(N).
\tag{2}
\]

直接后果是：

1. \(m>X\) 时 bulk symbol 为零，而真实有限泄漏总能量为
   \(O(\log L)=o(N)\)；
2. \(X^{1-\delta}<m\le X\) 的真实 finite adjacent edge 继承 bulk 的
   \(O(\delta^{2\kappa+2})\) tightness；
3. 笔记 201 式 (28) 与看板 A1 的 edge-localized transfer 闭合；
4. adjacent 的不同乘积 near-resonance、alternating/Farey ratio Gram 及其余
   四矩 words 仍是独立开放输入。

证明只用临界密度 Gabor 格、窗口的统一 \(C^2\) 正则性、von Mangoldt 的
素数幂支撑和无条件 Mertens 二次权估计。它不使用零点、RH、Hardy--Littlewood
猜想或完整 Weil 正性。

## 2. 有限 Gabor datum

令

\[
 L=\log X,\qquad h=\frac{2\pi}{L},\qquad
 \alpha_k=T+kh,\qquad 0\le k<d,
\tag{3}
\]

其中 \(d\asymp TL\)。设

\[
 \phi=\phi_L\in C_c^2([-L/2,L/2])
\]

为实偶函数，\(0\le\phi\le1\)，并假设

\[
 a_L=L^{-1}\|\phi\|_2^2\ge a_0>0,
\tag{4}
\]

\[
 \|\phi'\|_1+\|\phi'\|_2+\|\phi''\|_1\le C_0
\tag{5}
\]

一致成立。Alpöge--Furman 的固定平滑 cutoff 与固定窗口满足这些条件；其一手
定义和正则性估计见 arXiv:2608.13637v2 的式 (2.7)--(2.8)。

记

\[
 f_k(\tau)=\widehat\phi(\tau-\alpha_k),\qquad
 \mathbf f(\tau)=(f_0(\tau),\ldots,f_{d-1}(\tau))^{\mathsf T},
\]

并定义

\[
 R_T(x)=\frac1{a_LL^2}\int_{\mathbb R}
 \mathbf f(\tau)\mathbf f(\tau)^*e^{ix\tau}\,d\tau,
 \qquad 0\le x\le L.
\tag{6}
\]

因为 \(\phi\) 实偶，\(f_k\) 在实轴上为实函数，所以式 (6) 正是笔记 201
采用的显式公式矩阵响应。

## 3. 精确 Toeplitz 表示 [T]

在长度 \(L\) 的圆上采用 Fourier 系数

\[
 \widehat q(n)=\frac1L\int_{-L/2}^{L/2}
 q(u)e^{inhu}\,du,\qquad n\in\mathbb Z.
\tag{7}
\]

令 \(\mathcal L(q)\) 为 \(\ell^2(\mathbb Z)\) 上的 Laurent 算子，

\[
 \mathcal L(q)_{jk}=\widehat q(j-k).
\]

记 \(P_d\) 为到坐标 \(0,\ldots,d-1\) 的投影，并置

\[
 T_d(q)=P_d\mathcal L(q)P_d,\qquad
 D_d(x)=\operatorname{diag}(e^{ikhx})_{0\le k<d}.
\tag{8}
\]

对 \(0\le x\le L\) 定义

\[
 q_x(u)=\phi(u)\phi(x-u),
\tag{9}
\]

先以零延拓到基本区间，再视为长度 \(L\) 的周期函数。

### 定理 AEN（exact Gabor--Toeplitz response）[T]

令

\[
 \beta_L=\frac{2\pi}{a_LL}.
\]

则

\[
 \boxed{
 R_T(x)=\beta_Le^{iTx}T_d(q_x)D_d(x).}
\tag{10}
\]

若 \(q_y^{(x)}\) 表示圆上的周期平移

\[
 q_y^{(x)}(u)=q_y(u-x\pmod L),
\tag{11}
\]

则

\[
 \begin{aligned}
 R_T(x)R_T(y)
 ={}&\beta_L^2e^{iT(x+y)}
 \bigl[
 T_d(q_xq_y^{(x)})
 -\mathcal H_d(q_x,q_y^{(x)})
 \bigr]D_d(x+y),
 \end{aligned}
\tag{12}
\]

其中

\[
 \mathcal H_d(f,g)
 =P_d\mathcal L(f)(I-P_d)\mathcal L(g)P_d
\tag{13}
\]

是精确的 cross-boundary Hankel defect。

#### 证明

由 Fourier 定义与 Fubini，

\[
 \begin{aligned}
 \int_{\mathbb R}f_j(\tau)f_k(\tau)e^{ix\tau}\,d\tau
 &=2\pi\int\phi(u)\phi(x-u)
   e^{i\alpha_ju+i\alpha_k(x-u)}\,du\\
 &=2\pi Le^{iTx}e^{ikhx}\widehat q_x(j-k).
 \end{aligned}
\]

除以 \(a_LL^2\) 得式 (10)。又

\[
 D_d(x)T_d(q_y)D_d(-x)=T_d(q_y^{(x)}).
\]

利用 \(\mathcal L(f)\mathcal L(g)=\mathcal L(fg)\) 和

\[
 P\mathcal L(f)P\mathcal L(g)P
 =
 P\mathcal L(fg)P
 -
 P\mathcal L(f)(I-P)\mathcal L(g)P
\]

即得式 (12)--(13)。\(\square\)

#### 周期 alias 审计

周期平移不能未经检查地换成实线平移。对 \(x,y\ge0\)，

\[
 \operatorname{supp}q_x=[x-L/2,L/2].
\]

当 \(x+y>L\) 时，周期平移后的 \(\operatorname{supp}q_y^{(x)}\) 与
\(\operatorname{supp}q_x\) 至多在端点 \(x-L/2\) 相交；而 \(\phi\) 及其
导数在 cutoff 端点消失。因此

\[
 q_xq_y^{(x)}=0\qquad(x+y>L)
\tag{14}
\]

几乎处处。圆周表示没有把一个 \(L\)-alias 路径偷渡进 bulk。

## 4. Fourier crossing energy [T]

定义

\[
 \mathfrak b_d(q)
 =
 \sum_{n\in\mathbb Z}\min(d,|n|)|\widehat q(n)|^2.
\tag{15}
\]

### 引理 AEO（finite-section boundary energy）[T]

精确地

\[
 \|P_d\mathcal L(q)(I-P_d)\|_{\mathrm{HS}}^2
 =\mathfrak b_d(q).
\tag{16}
\]

若 \(d\ge L\) 且

\[
 \|q'\|_1\le A_1,\qquad \|q''\|_1\le A_2,
\]

则

\[
 \mathfrak b_d(q)
 \ll A_1^2\log(2+L)+A_2^2.
\tag{17}
\]

在式 (5) 下，\(q_x\)、\(q_y^{(x)}\) 及 \(q_xq_y^{(x)}\) 对所有
\(x,y\in[0,L]\) 都一致满足式 (17)。特别地，

\[
 \boxed{
 \|\mathcal H_d(q_x,q_y^{(x)})\|_{\mathrm{HS}}^2
 \ll_{C_0}1+\log L.}
\tag{18}
\]

#### 证明

固定 Fourier difference \(n=j-k\)。从 \(P_d\) 跨到补空间的 pairs 数恰为
\(\min(d,|n|)\)，所以式 (16) 成立。两次分部积分给

\[
 |\widehat q(n)|
 \le
 \min\left(
 \|q\|_1/L,\,
 \frac{A_1}{2\pi|n|},\,
 \frac{A_2L}{4\pi^2n^2}
 \right).
\tag{19}
\]

在 \(1\le|n|\le L\) 用第一导数界，在 \(|n|>L\) 用第二导数界；对
\(|n|>d\) 把 crossing multiplicity 换成 \(d\)，求和即得式 (17)。

由

\[
 q_x'=\phi'\phi-\phi\phi',
\qquad
 q_x''=\phi''\phi-2\phi'\phi'+\phi\phi''
\]

及式 (5)，Cauchy--Schwarz 给出统一 \(W^{2,1}\) 界；乘积同理。最后

\[
 \begin{aligned}
 \|\mathcal H_d(f,g)\|_{\mathrm{HS}}
 &\le
 \|P_d\mathcal L(f)(I-P_d)\|_{\mathrm{HS}}
 \|\mathcal L(g)P_d\|\\
 &\le \mathfrak b_d(f)^{1/2}\|g\|_\infty,
 \end{aligned}
\]

得到式 (18)。\(\square\)

## 5. Product clusters 的子集一致 transfer [T]

置

\[
 b_n=-\frac1{2\pi}\frac{\Lambda(n)}{\sqrt n},
\qquad x_n=\log n.
\tag{20}
\]

定义真实有限 cluster

\[
 F_m^{\mathrm{fin}}
 =
 \sum_{ab=m}b_ab_bR_T(x_a)R_T(x_b),
\tag{21}
\]

以及 bulk symbol 和 surrogate

\[
 Q_m(u)
 =
 \sum_{ab=m}b_ab_b
 q_{x_a}(u)q_{x_b}^{(x_a)}(u),
\tag{22}
\]

\[
 F_m^{\mathrm{bulk}}
 =
 \beta_L^2e^{iTx_m}T_d(Q_m)D_d(x_m).
\tag{23}
\]

由式 (14)，\(m>X\) 时 \(Q_m=0\)。

### 定理 AEP（subset-uniform adjacent transfer）[T]

在式 (3)--(5) 下，

\[
 \boxed{
 \sum_m
 \|F_m^{\mathrm{fin}}-F_m^{\mathrm{bulk}}\|_{\mathrm{HS}}^2
 \ll_{a_0,C_0}1+\log L.}
\tag{24}
\]

此外，

\[
 \sum_m\|F_m^{\mathrm{bulk}}\|_{\mathrm{HS}}^2=O(N).
\tag{25}
\]

所以对任意乘积集合 \(\mathcal M_T\)，

\[
 \left|
 \sum_{m\in\mathcal M_T}\|F_m^{\mathrm{fin}}\|_{\mathrm{HS}}^2
 -
 \sum_{m\in\mathcal M_T}\|F_m^{\mathrm{bulk}}\|_{\mathrm{HS}}^2
 \right|
 \ll\sqrt{N\log L}+\log L=o(N).
\tag{26}
\]

#### 证明

由式 (12)，单个 ordered factorization 对差矩阵的贡献为

\[
 -\beta_L^2e^{iTx_m}b_ab_b
 \mathcal H_d(q_{x_a},q_{x_b}^{(x_a)})D_d(x_m).
\tag{27}
\]

若 \(m\) 含两个不同素数底，则 \(\Lambda(a)\Lambda(b)\ne0\) 的 ordered
factorizations 只有两个。由式 (18)、Cauchy--Schwarz 和

\[
 \sum_{n\le X}\frac{\Lambda(n)^2}{n}\ll L^2,
\tag{28}
\]

这部分对式 (24) 的总贡献至多

\[
 \beta_L^4(1+\log L)
 \left(
 \sum_{n\le X}\frac{\Lambda(n)^2}{n}
 \right)^2
 \ll1+\log L,
\tag{29}
\]

因为 \(\beta_L\asymp L^{-1}\)。

若 \(m=p^k\)，则至多有 \(k-1\) 个 ordered factorizations，每个系数绝对值为
\((2\pi)^{-2}(\log p)^2p^{-k/2}\)。这部分由

\[
 \beta_L^4(1+\log L)
 \sum_{p,k\ge2}
 \frac{(k-1)^2(\log p)^4}{p^k}
 \ll L^{-4}(1+\log L)
\tag{30}
\]

控制，因为该双和收敛。式 (24) 得证。

另一方面，

\[
 \|T_d(Q_m)\|_{\mathrm{HS}}^2
 =
 \sum_n(d-|n|)_+|\widehat Q_m(n)|^2
 \le
 \frac dL\int_{-L/2}^{L/2}|Q_m(u)|^2\,du.
\tag{31}
\]

展开右侧后得到笔记 203 的 adjacent exact-product bulk functional。对随 \(L\)
变化的窗口 \(\psi_L(u)=\phi_L(Lu)^2\)，笔记 203 的证明只使用一致的
\(\|\psi_L\|_\infty\) 与端点 envelope，因此其 \(\delta=1\) 上界一致成立。
再用 \(\beta_L^4d\asymp T/L^3\)、式 (28) 及 \(N\asymp TL\)，得到式 (25)。

令

\[
 \mathbf F^{\mathrm{fin}}=(F_m^{\mathrm{fin}})_m,\qquad
 \mathbf F^{\mathrm{bulk}}=(F_m^{\mathrm{bulk}})_m
\]

为 Hilbert 直和中的向量。式 (24)--(25) 给

\[
 \|\mathbf F^{\mathrm{fin}}-\mathbf F^{\mathrm{bulk}}\|
 =O(\sqrt{\log L}),
\qquad
 \|\mathbf F^{\mathrm{fin}}\|
 +\|\mathbf F^{\mathrm{bulk}}\|=O(\sqrt N).
\]

投影到任意坐标集合 \(\mathcal M_T\) 不增范数；对两个投影向量使用
\(|\|u\|^2-\|v\|^2|\le\|u-v\|(\|u\|+\|v\|)\)，得到式 (26)。
\(\square\)

## 6. 推论 [T]

### 推论 AEQ（supercritical product leakage）[T]

\[
 \sum_{m>X}\|F_m^{\mathrm{fin}}\|_{\mathrm{HS}}^2
 \ll1+\log L=o(N).
\tag{32}
\]

这是式 (24) 在 \(Q_m=0\) 的坐标集合上的直接应用。

### 推论 AER（真实 adjacent edge tightness）[T]

若 \(\phi_L(Lu)^2\) 具有笔记 203 式 (4) 的一致端点 envelope，消失阶为
\(\kappa\ge0\)，则

\[
 \limsup_{T\to\infty}\frac1N
 \sum_{X^{1-\delta}<m\le X}
 \|F_m^{\mathrm{fin}}\|_{\mathrm{HS}}^2
 \ll_\phi\delta^{2\kappa+2}.
\tag{33}
\]

因此

\[
 \lim_{\delta\downarrow0}\limsup_{T\to\infty}\frac1N
 \sum_{X^{1-\delta}<m\le X}
 \|F_m^{\mathrm{fin}}\|_{\mathrm{HS}}^2=0.
\tag{34}
\]

平窗型窗口给 \(O(\delta^2)\)，形式端点余弦窗给 \(O(\delta^4)\)。证明是
式 (26) 与笔记 203 定理 AEM 的直接组合。

## 7. 公理作用与删除审计

1. **临界密度 \(h=2\pi/L\)**：把 modulations 变成长度 \(L\) 圆上的整数
   Fourier basis。删除后式 (10) 的 exact Laurent factorization 不再成立。
2. **有限区间 \(0\le k<d\)**：没有被忽略；它精确产生式 (13) 的 Hankel
   defect。因此本定理不是先假设无限 Gabor frame 再宣称边界消失。
3. **统一 \(W^{2,1}\) 正则性**：把 boundary energy 压到 \(O(\log L)\)。
   只有 sharp cutoff 时 Fourier \(1/n\) tail 可延伸到
   \(d\asymp e^LL\)，边界能量可达 \(O(L)\)；这对本 adjacent 主尺度仍为
   \(o(N)\)，但不足以替代完整四矩其他通道所需的强边界估计。
4. **von Mangoldt 素数幂支撑**：保证同一两素数乘积只有两个 ordered
   factorizations，单素数退化和可和。对稠密任意系数，增长的 divisor
   multiplicity 可使式 (29) 失效。
5. **Mertens 二次权界**：只把 coefficient 总平方质量压到 \(O(L^4)\)；
   它是无条件 prime-side 输入，不包含零点位置。
6. **endpoint envelope**：只负责式 (33) 的 \(\delta\)-速率，不参与
   Toeplitz--Hankel transfer 本身。

本定理适用于 Riemann zeta 及固定本原 Dirichlet \(L\) 函数的同型 Gabor
显式公式压缩。它属于“显式公式型部分 Weil 配置”的 finite-to-bulk 桥梁；
没有构造上同调分次、Frobenius、极化或 Hard Lefschetz，因而不说明两类
Weil 结构等价。

## 8. 循环性与结论边界

- 式 (24) 是确定性的 finite-section 恒等式加无条件 coefficient bound；
  没有读取零点或假设 Weil form 正定。
- 式 (33) 只控制 pure-prime \(2+2\) adjacent exact-product diagonal clusters。
- 不同乘积 near-resonance 仍需与有限 Toeplitz diagonal 相容的
  vector-valued Montgomery--Vaughan 分解。
- alternating ratio Gram、\(3+1\)、\(4+0\)、Gamma/continuum 背景和完整
  \(J_T-J_{\infty,T}\) Schatten gate 均未由本定理控制。
- 因此本结果不能单独推出新的零点比例，更不能推出 RH；它完成的是此前单独列出
  的 A1 边界桥梁。

## 9. 下一最小引理 [O]

路线 A 的下一主硬点是 A2：对真实 alternating response 子空间证明

\[
 G\preceq(1+\varepsilon_{\mathrm{alt}})D+M,
 \qquad x^*Mx\le\eta_{\mathrm{alt}}N,
\]

其中 \(G,D\) 是 ratio Gram 及其 diagonal，\(x\) 是实际 Vaughan channel
vector。必须保留共同 \(k\)-fiber 的交叉抵消，不能换成任意 ratio coefficients
的 all-direction Bessel bound。

辅助任务是把 adjacent interior 的 vector-valued Montgomery--Vaughan
disintegration 与式 (12) 的 Toeplitz diagonal逐项对接；这只处理不同乘积
near-resonance，不再包含 endpoint tightness。

可复现脚本 scripts/toeplitz_hankel_adjacent_audit.py 检查：

1. Toeplitz product 与 cross-boundary Hankel defect 的精确有限矩阵恒等式；
2. Fourier crossing-pair 计数式 (16)；
3. diagonal modulation 对周期 symbol translation 的方向与 phase；
4. smooth compact windows 的 boundary energy 对 \(\log L\) 的数值尺度。

脚本不证明素数渐近、式 (33) 或任何零点结论。
