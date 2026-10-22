# Γ保留近似：历史去重与实际素数幂／双极点预算

2026-10-22；独占分支，供 root 消费。固定 G20261014／0c4f 基线。本文不给总体计轮结算；历史恢复和下列标准乘窗／修补接口本身不冒称新的独立 RH 输入。当前可支付的具体费用与仍等价 RH 的费用严格分开。

## 1. 固定对象、窗口和规范

Fourier 约定为 \(\widehat r(t)=\int r(u)e^{-itu}du\)，\(r^*(u)=\overline{r(-u)}\)。始终固定经典完整分布

\[
 W=W_\Gamma+H-P,\qquad H=2\cosh(u/2)du,
 \quad P=\sum_{n=p^k\ge2}\frac{\Lambda(n)}{\sqrt n}
                       (\delta_{\log n}+\delta_{-\log n}),                 \tag{1}
\]

\(\widehat W_\Gamma(t)=\Gamma(t)=\Re\psi(1/4+it/2)-\log\pi\)，包括既定 finite part／contact。所有 proper powers 和两个极点保留，源是原物理 \(r=e^{u/2}f\)。compact 全 complex 源先定义 \(Q_V(r)=V(r*r^*)\)；405 的实际非compact关系另在 \(S_{\exp}\) 消费。

取实非负 \(\eta\in C_c^\infty((-1/2,1/2))\)，令

\[
 \phi(u)=\frac{(\eta*\eta^*)(u)}{\|\eta\|_2^2},\quad
 \phi_R(u)=\phi(u/R),\quad R\ge1.                              \tag{2}
\]

则 \(\phi\) 实偶、\(0\le\phi\le1\)、正型、支持 \([-1,1]\)、\(\phi(0)=1\)。有可计算常数 \(C_\phi\) 使
\(0\le1-\phi_R(u)\le C_\phi\min(u^2/R^2,1)\)。光滑性是必要选择；三角 Fejér 窗只有一阶原点消失，以下 \(R^{-2}\) 随之变为 \(R^{-1}\)。

定义完全由有限 prime／pole 数据给出的 signed 层

\[
 G_R=W_\Gamma+\phi_R(H-P),\quad
 g_R(t)=\Gamma(t)+\widehat{\phi_RH}(t)
       -2\sum_{n\le e^R}\frac{\Lambda(n)}{\sqrt n}
                         \phi(\log n/R)\cos(t\log n).             \tag{3}
\]

有限求和仍包括每个 \(p^k\le e^R\) 的真实 \(\log p\) 权。窗外项是已明确记录的截断误差；不是把完整目标的高幂或两 pole 删掉。

## 2. 真Γ保留所新增的明确费用接口

569(7) 给完整 Γ 分布

\[
 W_\Gamma(h)=\Gamma_0h(0)+\int_0^\infty 2a(v)
        [h(0)-(h(v)+h(-v))/2]dv,
 \quad a(v)=\frac{e^{-v/2}}{1-e^{-2v}},\quad\Gamma_0=\Gamma(0).       \tag{4}
\]

因此差分不留任何未知 contact：

\[
 E_R:=(1-\phi_R)W_\Gamma
       =-(1-\phi_R(u))a(|u|)du,
 \qquad G_R=\phi_RW+E_R.                                       \tag{5}
\]

右侧是有限负测度。虽然 \(W_\Gamma\) 自身非 Radon，\(1-\phi_R\) 在0的二阶消失付清有限部分。令

\[
 d_R=\|E_R\|_{TV}=2\int_0^\infty(1-\phi(v/R))a(v)dv
       \le\frac{2C_\phi}{R^2}\int_0^\infty v^2a(v)dv.             \tag{6}
\]

原点 \(v^2a(v)=O(v)\)，无穷端指数衰减；故 (6) 无未付尾。其 Fourier 函数 \(e_R\) 满足

\[
 |e_R(t)|\le d_R,\qquad
 e_R(t)+d_R=2\int_0^\infty(1-\phi(v/R))a(v)(1-\cos(tv))dv\ge0.    \tag{7}
\]

并且由 dominated convergence
\(R^2d_R\to-\phi''(0)\int_0^\infty v^2a(v)dv\)，其中
\(-\phi''(0)=\|\eta'\|_2^2/\|\eta\|_2^2>0\)。该精确差分及 \(du\) 费用绕过576对逐层 Radon 近似的高频门：每层 \(G_R\) 都真正保留完整 Γ 奇性，不再是 Radon 物理分布。

## 3. 非零点系数规则：有限层可构造，消失费用未付

因 \(\phi_R(H-P)\) 是紧支有限测度，\(g_R\) 实偶连续；由已付的 \(\Gamma(t)=\log|t|+O(1)\)，其在无穷端趋 \(+\infty\)。故

\[
 c_R=\max\{0,-\min_{t\in\mathbb R}g_R(t)\},\qquad
 V_R=G_R+c_R\delta_0                                      \tag{8}
\]

给一个不读取未知 ζ 零点的正型分布。谱密度是 \((g_R+c_R)dt/(2\pi)\ge0\)；每个 \(c_R\) 是由有限 prime powers、光滑 pole 窗和完整 digamma 明确定义的一维最优化。可用 \(\Gamma(t)\ge\log(2+|t|)-C_\Gamma\) 和下面 (9) 将最优化限制到有效紧区间，再作有认证误差的函数界；本文没有将数值采样当作全谱非负证明。

最粗无条件上界确实可付。置

\[
 M_R=8\sinh(R/2)+2\sum_{n\le e^R}\frac{\Lambda(n)}{\sqrt n}
                                     \phi(\log n/R),
 \qquad0\le c_R\le[-\Gamma_0]_++M_R.                       \tag{9}
\]

这里使用 \(\Gamma\ge\Gamma_0\)、\(|\widehat{\phi_R(H-P)}|\le M_R\)。Chebyshev \(\psi(x)\le C_\psi x\) 加 partial summation 给
\(\sum_{n\le x}\Lambda(n)/\sqrt n\le2C_\psi\sqrt x\)，故 \(c_R=O(e^{R/2})\) 的有效上界。所有幂已经计入 \(\psi\)，没有只拿 primes 代替。这个指数上界只保证每个修补有限，完全不支付目标逼近。

**规范限制。** (8) 每层含原封不动的 \(W_\Gamma\)，但总 contact 多出显式 \(c_R\delta_0\)。因此它是“保真 Γ 奇性、contact 缺陷单独记账”的正证书，不能称为同一 canonical completed g-system。若要求总 contact 每层也精确固定，必须禁止该缺陷，或换用 Fourier 上的非负光滑紧支 majorant \(k_R\ge(g_R)_-\)；其 inverse Fourier 是 smooth 项而非 contact。后一修补的趋零费用同样仍需独立证明，并未由名称解决。

## 4. 唯一未付的 \(c_R\to0\) 是完整正性责任

若完整 \(W\) 正型，则 \(\phi_RW\) 正型（源 Gram 的 Schur 乘积，或正谱卷积）。其 Fourier 为非负光滑函数；(5)–(7) 给

\[
                 0\le c_R\le d_R=O(R^{-2}).                \tag{10}
\]

此推导不选择 ζ 零点，但其前件正是完整 Weil 正性，不能反向说 (10) 已无条件付清。

反之 \(G_R\to W\) 于 \(D'\)。若任一 cofinal 子列有 \(c_R\to0\)，则正型 \(V_R\to W\) 于 \(D'\)，对每个 compact \(r\) 取卷积平方即得完整 \(Q_W(r)\ge0\)。所以在本固定窗口族中

\[
 W\text{正型}\iff \liminf_{R\to\infty}c_R=0
 \iff c_R\to0
 \iff c_R\le d_R\ (\forall R\ge1).                          \tag{11}
\]

前后均保完整目标；用于经典 ζ 时是 RH 等价判据。等价本身不禁止独立 prime／pole 证明，却说明不得把“取最小非负修补”当作其费用趋零的证明。与174的投影／分离、576 smoothing 分支的全负部裁剪责任同类，未减少独立正性输入。

若存在一个真正 compact 负源 \(r\)，则 (8) 的实际原源费用满足

\[
 \liminf_{R\to\infty}c_R\ge
           \frac{-Q_W(r)}{\|r\|_2^2}>0.                    \tag{12}
\]

这是固定实际源反测，不是某个辅助全空间 norm lower。它也说明大而有限的 \(c_R\) 从来不是 RH 失败证据；只有错误地把它丢掉才会产生假证明。

## 5. 原 \(du/D_{\log}\) 与成长预算

对所有 \(\operatorname{supp}r\subset[-L,L]\) 的 complex 源，autocorrelation 满足
\(|(r*r^*)(u)|\le\|r\|_2^2\)、支持 \([-2L,2L]\)。直接从 (1)、(3)、(8) 得

\[
 |Q_{V_R}(r)-Q_W(r)|
 \le\left[c_R+\frac{C_\phi A_L}{R^2}\right]\|r\|_2^2,
 \quad
 A_L=\int_{|u|\le2L}u^2d(H+P)(u).                          \tag{13}
\]

\(A_L\) 是完整实际 pole／power 数据：

\[
 A_L=4\int_0^{2L}u^2\cosh(u/2)du
       +2\sum_{n\le e^{2L}}\frac{\Lambda(n)}{\sqrt n}(\log n)^2
       =O((1+L^2)e^L).                                     \tag{14}
\]

这是可付而粗的 upper，不是必要费用。对固定 \(L\)，除 \(c_R\) 外的一切误差为原 \(du\) 统一 \(O_L(R^{-2})\)；以
\(\|r\|_{H_{\log}}^2=(2\pi)^{-1}\int[1+\log(2+|t|)]|\widehat r(t)|^2dt\)
或原 \(D_{\log}\) 下界转换，不产生新的未知费。通过 fixed-window core，式 (13) 延至整个原 zero-extension 域。

若 \(L=L_R\) 成长，只能消费显式条件 \(A_{L_R}/R^2\to0\) 与 \(c_R\to0\)；不能把 fixed \(L\) 常数吞掉。当 \(L\) 无界时，(13) 不给全线全部源的同一小 \(du\) 常数，更不自动传405非compact尾。全源统一规范、逐源 \(D'\) 极限、固定窗全源规范是三个不同量词。

### 5.1 405全关系与537非根的实际首门

每个固定 \(R\)，\(g_R+c_R>0\) 在充分高的 \(|t|\) 上成立。对任何非零 \(r\in S_{\exp}\)，\(\widehat r\) 是非零整函数，不能在一个实开区间恒零；其快速衰减也付清积分。因此
\[
                   Q_{V_R}(r)>0\quad(0\ne r\in S_{\exp}).        \tag{15}
\]
特别，每层必定不消405任何非零实际 Pan 关系；不是只缺一项 vanishing 证明。它同时看见537的非根，但这只是一个忠实 raw-source 正范数，不是正确的关系商。允许分布近似的路线不要求逐层消 Pan；若要声称真实源商映射，(15) 已明确拒绝该层。

由 \(g_R+c_R=\Gamma+\text{bounded}\)，每层还有全线 \(Q_{V_R}(r)\le C_R\|r\|_{H_{\log}}^2\)，而原 \(du\) 上因高频 logarithm 无统一有界常数。即使未来付 \(c_R\to0\)，也不能将 \(C_R\) 取为全 \(R\) 一致常数：否则 compact 极限型会延成原全线 \(H_{\log}\) 有界型，并由405／553的 Pan 稠密性及真实关系连续性成为零型，矛盾于537非根。该强旧结论只排全线原范数的一致 bounded transport，完全不排 (13) 的 fixed-window 范数极限、\(D'\) 极限、强 topology 或有费成长。

## 6. 连续与函数域负对照

1. 对562正连续模型 \(W_c=2\cos(\tau u)du\)、模型 Γ=0，\(\phi_RW_c\) 正型，(8) 的最小 \(c_R=0\)；全部连续 primitive／power／双pole 已由562精确相消。
2. 对562负段 \(W_c=2\cosh(\kappa u)du\)，\(0<\kappa<1/2\)，可取奇 \(h\in C_c^\infty\)、\(r=(D^2-1/4)h\)，使 \(\mu_\pm r=0\) 而 \(Q_{W_c}(r)<0\)。由 (12) 得 \(\liminf c_R>0\)。双pole-zero 不使负费用自动消失；模型全 prime powers 和 pole 恒等式均保留。
3. 对563／566已经独立证明正型的真实曲线完整 \(W_C\)，模型 Γ=0；正窗乘法仍正，最小 \(c_R=0\)，保全部原周期／aliases，而不是先假设未知纯性。这是窗口工具的正确对照，不能把 Γ=0 的成功外推为经典 budget (10) 的独立证明。

这些都是旧正反模型的具体消费，不能重复称为新的连续 RH 或新的函数域纯性。

## 7. 历史强旧对照与停止范围

| 必要原件 | 已付内容／本门不能重复领取的责任 |
|---|---|
| 016、022、028 | 完整型正背景减势、compact Hodge／负迹预算；加足够质量修补 positivity 不是新 RH 机制 |
| 174 §§1–2 | 最近正锥点／分离自动给安全证书，统一距离仍是独立输入；“裸不可行”的措辞只应读成未减少问题，不能读成禁止等价存在性有独立证明 |
| 177 §§1–3 | 正 Fejér／随机格只是已给 Gram，固定凸锥中的平均不能凭空降低缺陷 |
| 529 | 标准逐点锥 semigroup 失效不等于完整 Q 失正；本门不能以 \(H-P\) 点态符号推 PSD |
| 537 | 实际固定17/16窗 all-complex、完整 Γ／powers／pole 与非有限秩尾正性；它不控制 (3) 全频密度的 \(R\to\infty\) 最小值 |
| 560 | 真 Sonin 全逆／全returns 给每个先固定 finite-S 的正迹减 compact 完整桥；其成长全源误差仍未付，不能代入 (10) |
| 562–563 | 全compact正型闭锥／广义 Weil 等价与热 CM；未知正谱不能用来选经典系数 |
| 569(7)、576 §8 | 既定 Γ FP/contact、Γ正修补及逐层 Radon 统一 Hlog 门；(5) 的精确有限负测度差是这两项已付公式的直接组合 |
| 576 smoothing分支 §7 | Fourier 负部截断能制造正分布，负部消失仍需完整独立误差；(8) 将它具体化为一个固定真Γ层的最小 contact 费用 |

最强 actual whole 后果仍为542＋555→557 leading4/5负惯性 upper，不由本分支变成 lower、core 控制或 RH。当前确有可复用的具体接口：真Γ层、有限 prime／pole 非零点规则、\(O(R^{-2})\) 原Γ差与固定窗原费用。未付瓶颈被集中到 (10)／(11) 的 signed 最小缺陷，但没有被消除。

本分支在此停止，不续数值网格／窗口参数、未知零谱拟合或把 \(c_R\to0\) 改名容量。能改变决定的实际输入是来自 prime／pole 数据的独立 joint 下界，支付 \(g_R\ge-o(1)\)，或一个同对象几何／RR 恒等式付此符号；非局部／源适应／不同强拓扑及明确有费修补均未被排除。
