# 566 原件：经典完整热源、物理可闭性与有限／无限图检验

2026-10-20；独占 classic 分支。对象始终是563的完成化经典 Weil 分布，
不是558／559的 fixed-window Weil 算子再取热迹。本文没有构造出经典 RH 算子。
新检验是：直接闭包物理 Q 的域障碍；完整热源排除普通有限紧图；无限缩边图的合法逃逸及实际系数失配。

## 1. 固定完整源及其无零点输入的紫外系数

采用 Fourier \(\widehat h(y)=\int e^{-iyu}h(u)du\)、Gaussian
\(k_t(u)=(4\pi t)^{-1/2}e^{-u^2/(4t)}\)。实际无穷位 multiplier 是

\[
 \Gamma_\infty(y)=\Re\psi(1/4+iy/2)-\log\pi=2\theta'(y).
\]

沿用563已付的完整源身份，不作原子／极点删除：

\[
 \Theta_\zeta(t)=2e^{t/4}+\frac1{2\pi}\int_\mathbb R
 e^{-ty^2}\Gamma_\infty(y)dy
 -\frac2{\sqrt{4\pi t}}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/(4t)}.                                      \tag{1}
\]

Gamma 积分等价于563(13a)中保原点接触项的 finite-part 差分积分；它不是把
穿孔奇核当通常可积函数。求和包括所有 \(p^m\)，双 pole 完整给 \(2e^{t/4}\)。
Gamma 的竖直 Stirling 公式给

\[
 r(y)=\Gamma_\infty(y)-\log|y|+\log(2\pi)\in L^1(\mathbb R).
\]

理由：大端误差 \(O(y^{-2})\)，小端 \(\Gamma_\infty\) 光滑而 \(\log|y|\) 可积。
于是 Gamma 积分替换对数的误差统一 \(O(1)\)。利用

\[
 \int_\mathbb R e^{-ty^2}\log|y|dy
 =\frac{\sqrt\pi}{2\sqrt t}\bigl(\psi(1/2)-\log t\bigr),
 \quad\psi(1/2)=-\gamma_E-2\log2,
\]

得到

\[
 \boxed{\Theta_\zeta(t)=\frac{\log(1/t)-\gamma_E-\log(16\pi^2)}
 {4\sqrt{\pi t}}+O(1)\qquad(t\downarrow0).}                 \tag{2}
\]

这里 prime 尾为 \(O(t^{-1/2}e^{-c/t})\)：固定 \(t_0>0\)，把每项 Gaussian 拆成两个
\(e^{-(\log n)^2/(8t)}\)，第一个用 \(n\ge2\)，第二个用 \(t\le t_0\) 与
\(\Lambda(n)\le\log n\) 求和。pole 为 \(2+O(t)\)，不改变(2)的两个发散系数。
(2)完全来自已定 Gamma／prime／pole，未使用 RH、零点数值或把零点预设为实数。
Stirling 的一手标准来源是 [DLMF 5.11](https://dlmf.nist.gov/5.11)。

## 2. 直接把正 Weil Q 在物理 L²(R,du) 上闭包，方向本身不正确

**原子障碍。** 设正 tempered 测度 \(\sigma\) 有孤立原子 \(\gamma_0\)（质量 \(m>0\)），
定义 \(q_\sigma(g)=\int|\widehat g(\gamma)|^2d\sigma(\gamma)\)，域含
\(C_c^\infty(\mathbb R)\)。则此正形式在原 \(L^2(du)\) 上不可闭。

证明：取 \(\phi\in C_c^\infty\)、\(\int\phi=1\)，令

\[
 g_R(u)=R^{-1}e^{i\gamma_0u}\phi(u/R),\qquad
 \widehat g_R(\gamma)=\widehat\phi(R(\gamma-\gamma_0)).
\]

有 \(\|g_R\|_2^2=R^{-1}\|\phi\|_2^2\to0\)。孤立性与 \(\widehat\phi\) 的快速下降，
结合 \(\sigma\) 的多项式增长，给
\(\widehat g_R\to1_{\{\gamma_0\}}\) 于 \(L^2(\sigma)\)。因而
\(q_\sigma(g_R-g_S)\to0\)，但 \(q_\sigma(g_R)\to m>0\)，违反可闭性定义。证毕。
这不是新的一般可闭性定理；相应更广的绝对连续性标准已有
[Alpay–Jorgensen, Theorem 4.2, pp.11–13](https://arxiv.org/pdf/1109.5273)，
半线 Wiener–Hopf 版本见 [Yafaev, §4.2, Theorem 4.2](https://arxiv.org/pdf/1711.02614)。
上述原子列独立给出本研究实际需要的 Cc∞／全线范围，未把半线定理直接偷换到全线。

**连续正例已能检验。** 562／563的 \(c>1/4\) 正段给
\(q_c(g)=|\widehat g(\tau)|^2+|\widehat g(-\tau)|^2\)，\(\tau^2=c-1/4\)。
它全源正而在物理 \(L^2(du)\) 不可闭。阈值 \(c=1/4\) 的 \(2|\int g|^2\) 同样不可闭。
所以“正闭形式”要求不能误加为所有类 RH 系统的 physical-Q 必要条件。

**经典逻辑范围。** 假若直接的经典 \(Q_W\) 是物理 L² 上可闭的正形式，
Weil 判据先给 RH，显式公式随后识别 \(\sigma=\sum_\gamma m_\gamma\delta_\gamma\)。
零点是孤立的，测度有多项式增长且非空，原子障碍随即矛盾。因此这条**直接 positive
physical-Q closure** 路径不能成立；这不取决于 RH 的真假。
不是否定由别的 Hilbert 空间与别的闭能量实现 \(\Theta_\zeta\)。

边界务必保留：\(g_R\) 的支撑增长到无穷，故此证明不排 fixed-window 的闭形式。
旧559的 \(\Gamma_I-A_I+\text{poles}\) 在每个固定 I 的自伴／闭型实现仍有效。
也不排增强的 weighted/Sobolev/source 范数；例如把 Fourier 取值纳入 graph norm 可使其连续，
但这种换范数不是原 L² 可闭，更不自动给 ordinary heat identity。
在 GNS 范数或已知纯点 trace 空间构造闭能量是合法逃逸，其正性与忠实重数必须独立给出。

## 3. 普通有限紧 metric graph 的正闭 Laplace 形式不能给(1)

具体候选：有限条有限长边，Hilbert 空间为边上 Lebesgue L² 的有限直和，
能量为 \(\sum_e\int|f'_e|^2\)，加有界实势／固定自伴局部 vertex 条件，且算子非负。
普通热迹的首项是

\[
 \operatorname{Tr}e^{-tK}=\frac{\mathcal L}{\sqrt{4\pi t}}+O(1),
 \qquad \mathcal L=\sum_e\ell_e<\infty.                    \tag{3}
\]

Dirichlet／Neumann 边分离的计数 bracketing 已给首项；有限顶点条件不改 Weyl 首项。
完整 finite-graph 公式可核
[Harrison–Kirsten, *Zeta functions of quantum graphs*, §8, (120)–(123), pp.27–28](https://arxiv.org/pdf/0911.2509)。
因此(3)不可能等于(2)，任何有限个新增正态、有限秩谱修复或常数能量平移也不能补出
\(t^{-1/2}\log(1/t)\) 首项。它们只改 \(O(1)\) 或更低项。

这项可判门并不排“所有局部算子”：不规则奇性、无限边／无限体积但紧 resolvent、
非紧 confinement、cusp／relative heat、非通常 trace 都在范围外。
regularized 或 relative trace 必须另外证明它是正测度的 Laplace 变换；
正算子的两个 heat traces 相减，或超迹，通常没有完全单调保证。
例如一维正算子1和2的相对热量 \(e^{-t}-e^{-2t}>0\)，但在 \(t\downarrow0\) 递增，非 CM。
所以 relative 版本不能无条件继承565的 ordinary positive-heat 充分定理。

## 4. 严格支付一种逃逸：无限缩边 Dirichlet 图有正确 log 主项，却非完整经典源

取独立区间 \(I_n=(0,1/n)\)，

\[
 \mathcal H=\bigoplus_{n\ge1}L^2(I_n),\quad
 \mathfrak e(f)=\sum_n\int_{I_n}|f'_n|^2,
\quad D(\mathfrak e)=\{f_n\in H_0^1(I_n):
 \sum_n(\|f_n\|_2^2+\|f'_n\|_2^2)<\infty\}.               \tag{4}
\]

这是稠密正闭 Dirichlet 形式；由每段的 \(\pi^2n^2\) 最低能量，尾部的嵌入范数
趋0，故 compact resolvent。谱可直接分离变量，不读 ζ 零点：

\[
 \lambda_{n,k}=\pi^2n^2k^2,\qquad
 \operatorname{Tr}e^{-tK}=\sum_{m\ge1}d(m)e^{-\pi^2m^2t}<\infty.
                                                               \tag{5}
\]

这就是 [Egger–Steiner, arXiv:1104.1364, §§2–4、§10](https://arxiv.org/pdf/1104.1364)
的 Dirichlet 图经缩放后的显式版本；该文更研究有限正 δ coupling 的闭形式，
并不是只靠形式谱猜测。此处只消费(4)–(5)直接可核的极限对象。

对 \(\Re s>1/2\)，(5)的 Mellin 变换精确为
\(\Gamma(s)\pi^{-2s}\zeta(2s)^2\)。在 \(s=1/2\) 的二阶极点算出

\[
 \operatorname{Tr}e^{-tK}=\frac{\log(1/t)+3\gamma_E-2\log(2\pi)}
 {4\sqrt{\pi t}}+O_\epsilon(t^{-\epsilon}),
 \quad0<\epsilon<1/2.                                    \tag{6}
\]

取 Mellin 线移至 \(\Re s=\epsilon\) 即可，Gamma 竖直指数衰减支付尾部，
不需穿过0或承诺全部热展开。两发散系数已足以比较。
(6)确实逃过有限图(3)并匹配经典的 log 首项；但其第二个发散系数相对(2)多
\(4\gamma_E+\log4>0\)。故这个**具体**正闭形式的 ordinary heat 绝不等于完整经典热量。
不能只凭 \(T\log T\) Weyl 律就声称已建立同源 identity。

更基本地，(5)的结构是 divisor multiplicities \(d(m)\) 与 additive 频率 \(\pi m\)，
而(1)有全部 \(\log p^k\) 长度、\(\log p/p^{k/2}\) 权、Gamma 接触项与双 pole。
这些实际身份都未由(4)提供。下一步若修改无限图，准入须给 **所有时间的源端迹公式**，
不是调几项 Weyl 系数或拟合已知零点。

## 5. 消费记录与最强旧扣除

* 对象／norm／域：原完整 W 的 Gaussian 热量；physical Q 域为全成长 Cc∞ 且 ambient L²du；
  图能量改用明确 edge L²／H₀¹ 域。(2)的参数为全部充分小 t；(1)本身为所有 t>0。
* paid：563完整 Γ／全部 pp／双 pole 身份；原子缩频列及图闭性、trace-class、紫外系数在上文证明；
  标准 Fourier 可闭性与量子图来源准确归旧，非外部新定理。
* 方向／误差：(2)是实际 Θ 的无条件等式渐近，非上下包络；(6)与(2)的次主系数严格不等。
  finite graph 失败不排无限正能量；positive physical-Q closure 失败不排不同 norm／载体。
* strongest-old：016／017早已给 prime 图平方减 degree，563全源 ODE／热CM和565闭形式充分接口已付；
  558／559讨论的是窗 Q 的热迹，不是零点热量，不能靠混同对象支付(1)。
* 本轮净信息：把“直接闭包Q”和“在有限紧图上造K”两个具体实现排到正确范围，
  并用真正 closed、trace-class 的无限图验证可逃逸而不付 actual identity。
  没有新增独立经典正性；whole leading4/5、成长 core/coupling／Ξ仍未改。
* 经典最小未付箭头仍是：由同一 canonical 源构造另一明确 Hilbert 空间中的正闭能量，
  再从算术源证明其 ordinary heat trace 对每个 t>0精确等于(1)。
  若只定义未知K、按未知实零点反造谱，或要求 Θ 全CM，就仍是 RH 等价责任改名。
