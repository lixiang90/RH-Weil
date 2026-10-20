# 双 conormal 的固定权、有限部分与经典 Γ：原件审计

2026-10-20；本稿独占来源／局部核比较，不修改 STATE、计轮或 Git。
固定 G20261014／0c4f≤538，消费 563、565、567、568 已付完整源和反测试。
没有证明经典 Weil 正性；下文明确区分原论文设施、本轮自己的直接计算、仍未付比较。

## 1. 原件与实际阅读范围

主要原件为 Álvarez López–Kordyukov–Leichtnam，
[*A trace formula for foliated flows*, arXiv:2402.06671v2](https://arxiv.org/pdf/2402.06671v2)，
版本日期 2024-02-13，176 页。本轮核 §1.3.1–1.3.6（印刷 pp2–8），
§2.3.4–2.3.5、§2.5.28–2.5.30（印刷 pp46–48），
§5.3（pp119–120）、§5.8（pp128–129）、§6.1/6.3（pp131–135）、§6.7（p139）。
其中印刷 p7、pp46–48 已以下载原 PDF 渲染图目视检查；未重审全书证明。
原 PDF SHA256、精确阅读及访问记录见同目录 `dual-conormal-source-record.json`。
只读使用 pdf 技能作原版排印 QA，原 PDF/PNG 是临时源文件，不作为研究产物入 Git。

§1.3.6 回指 Barner，[*On A. Weil's explicit formula*](https://doi.org/10.1515/crll.1981.323.139)，
JRAM 323 (1981), 139–152。原出版入口无全文权限，GDZ 原扫描 p146 的 OCR 可访问，
但数学字符严重损坏，未取得足以确认该显示式意图的原始清晰公式。
因此没有把“作者本意是某个隐藏 finite part”作为已支付前件。
完整 Γ 的校准改从已核 [NIST DLMF 5.9.12](https://dlmf.nist.gov/5.9.E12) 独立计算；
这是标准 Γ 的既有输入，不是从 conormal 几何推出算术规范。

## 2. 固定权从哪里来

原件 §5.3/§5.8 给 conormal 的第 k 层法向密度次数 −k−1，
§6.3/§6.7 给 density-dual 第 k 层次数 k，k≥0。
若法向定义函数满足 φ_t^*ρ=e^{κt}ρ，则对应作用权为

\[
 K_k:e^{-(k+1)\kappa t},\qquad K'_k:e^{k\kappa t}.             \tag{1}
\]

局部验证无需谱位置：对 x↦e^{κt}x，δ^(k) 的分布拉回含 Jacobian 一次，
得到 −(k+1)κ；Taylor jet x^k 给 kκ。两者相差的一单位正是密度责任，不能任删。
原件把 density-bundle 版本转置，再用叶内对偶；这不是可任意分别调整两半轴的规则。

为简洁，固定一片 preserved leaf，Euler 系数先省略。原文在不同收敛半轴分别取

\[
 \sum_{k\ge0}e^{-(k+1)\kappa t}\quad(\kappa t>0),\qquad
 \sum_{k\ge0}e^{k\kappa t}\quad(\kappa t<0).
\]

组合的穿孔核是

\[
 K_\kappa(t)=|e^{\kappa t}-1|^{-1},\qquad
 K_\kappa(-v)=e^{\kappa v}K_\kappa(v).                       \tag{2}
\]

这仍是由两种载体拼合的分布迹，不能解释为同一正 Hilbert 算子的普通迹。
叶内平坦系数、非平凡 equivariant bundle、多个叶及其真实 Euler 系数是合法扩充，
但须独立给出，不能从本次单叶标量计算排除它们。

## 3. 共同 character 的精确边界与 parity 逃逸

以下命题只限“一个非零 κ、一条完整 k≥0 标量链、同一个实 flow character”的直接翻译。
共同乘 e^{at} 后欲使 (2) 偶，必要且充分为 a=κ/2。于是

\[
 H_\kappa(t)=e^{\kappa t/2}K_\kappa(t)
 =\frac{e^{-|\kappa||t|/2}}{1-e^{-|\kappa||t|}}
 =\frac1{2\sinh(|\kappa||t|/2)}.                            \tag{3}
\]

在同一对偶配对中这正是将两组次数移至 ±(k+1/2)κ 的 half-density 居中。
普通法向密度的固定幂在该线性模型中只产生一个共同 character，已包括在上述比较。
一般 equivariant 系数的作用不是因此全部归入这个类。

经典物理 log 坐标中的完整 Γ 穿孔核是 −a(|t|)，其中

\[
 a(v)=\frac{e^{-v/2}}{1-e^{-2v}}=\sum_{m\ge0}e^{-(2m+1/2)v},\quad v>0. \tag{4}
\]

任何非零常数倍的 (3) 都不能等于 (4)。例如比较 v→∞：首指数迫使 |κ|=1，
首系数也随之固定；但 (3) 的下一指数为 3/2，(4) 为 5/2，矛盾。
若从算术步长 2 开始比较，则 |κ|=2 时 (3) 的首指数是 1，同样不对。
δ0 或其任何局部补偿不能改变这一穿孔差。
因此前轮仅核 κ=−2、一个试选 character 的失败，可加强为上述整个单叶标量共同 character 类失败。
这不是一般几何模型的否定。

一个明确合法但尚未由所审原文供给的逃逸是 normal reflection/parity。
令 κ=1，在 half-density 居中的两链只保留偶 k=2m，便得到 ±(2m+1/2)，
两半轴求和恰为 (4)。在局部实法线 x↦−x 上，δ^(k) 和 x^k 的标量 parity 同为 (−1)^k，
|dx|^{1/2} 的反射因子为 1，因此两侧偶投影可以局部相容。
但这要求真实 involution、与全局微分／flow／pairing 相容的投影及相应迹定理，
原文 all-k 的式子没有自动给出这些数据。
Tate 实位的偶函数部门提示这种选择的算术来源；裸 g-integer 分布与抽象 Mellin 对偶本身
没有指明一个实位、法线反射或该部门。只保留想要的偶 k 不算独立构造。
这一局部比较也只匹配核的形状：真实 Euler 系数、Γ 的负号与 trace multiplicity 仍须支付。
例如三维情形的可定向闭二维叶有 χ=2−2g，不能为配 Γ 直接取 χ=−1；
twisted/super coefficients 或 orbifold 权重可以另行提出，但不在此原文标量设施的已付范围。

## 4. 有限部分显示式的两个独立问题

已目视确认，原文印刷 p7 在普通 ∫_0^∞ 中写

\[
 \frac{f(t)+f(-t)}{|e^{\kappa t}-1|}-\frac{2f(0)}{|\kappa|t}, \tag{5}
\]

其积分号没有有限部分标记、尾部 cutoff 或衰减减项。
对 compact f 且 f(0)≠0，足够大的 t 上只剩 −2f(0)/(|κ|t)，所以普通积分在无穷端发散。
此外 (2) 通常不偶：取 f 支撑在负半轴且离开 0，(5) 用 Kκ(v) 读取 f(−v)，
真实穿孔核却要 Kκ(−v)。这不是只靠改变原点 contact 能修的差。
这两个可直接检验的问题均不归因于 OCR。

可行的数学修复是固定真正的穿孔核与一个 reference scale，定义

\[
 T_\kappa(f)=\lim_{\epsilon\downarrow0}
 \left[\int_{|u|>\epsilon}K_\kappa(u)f(u)du
       +\frac{2}{|\kappa|}f(0)\log\epsilon\right].            \tag{6}
\]

近 0 的有限部分存在，因为 Kκ(u)=1/(|κ||u|)+O(1)，f(u)=f(0)+O(u)；
尾部由 f compact 保证。改变 reference scale 只产生 cδ0。
在保留 scaling degree≤1 的扩张类中，这也是全部原点歧义：更高 δ 导数会增加 scaling degree。
这只是一个独立合法修复，不是替作者宣称原文已固定某个 arithmetic contact。
论文的一般 trace 设施与 (5) 的逐字消费范围必须分开。

## 5. 标准 Γ 输入给出明确 contact，但不能由此倒推 conormal membership

对 h∈Cc∞，本仓完整 Γ 源为

\[
 A_\Gamma(h)=\Gamma_0h(0)+\int_0^\infty2a(v)
 \left[h(0)-\frac{h(v)+h(-v)}2\right]dv,
 \qquad\Gamma_0=\psi(1/4)-\log\pi.                          \tag{7}
\]

DLMF 5.9.12 的积分式令 y=2v，直接得到另一收敛表达

\[
 A_\Gamma(h)=-\log\pi\,h(0)+\int_0^\infty
 \left[\frac{e^{-2v}}v h(0)-a(v)(h(v)+h(-v))\right]dv.        \tag{8}
\]

减项 e^{-2v}/v 同时保 UV 抵消和尾部收敛，与 (5) 全程 1/v 有实质差别。
再由同一 ψ 积分式（或令 z=1 先校准，再取差）

\[
 \int_\epsilon^\infty2a(v)dv
 =-\log(2\epsilon)-\gamma-\psi(1/4)+o(1).
\]

故若固定 physical-log cutoff

\[
 T_a(h)=\lim_{\epsilon\downarrow0}
 [\int_{|u|>\epsilon}a(|u|)h(u)du+h(0)\log\epsilon],
\]

则完整身份为

\[
 \boxed{A_\Gamma=-T_a-(\gamma+\log(2\pi))\delta_0.}          \tag{9}
\]

这是不使用零点位置的明确全 Γ 规范。它保留完整 contact，
但归属为已固定实位标准 Γ/π 的输入；不能说 g-prime 分布单独给出 π 的物理尺度。
本轮并未由 foliation 的 ν、Euler 项或其可调 η/g 独立推出 (9)。

## 6. 一个可计算的合法补偿及其 signed 边界

将 |κ|=2 的 (3) 记 b(v)=e^{-v}/(1-e^{-2v})，令

\[
 D(u)=a(|u|)-b(|u|)>0\quad(u\ne0).
\]

两核具有相同 1/(2|u|) 奇性，所以差延拓为 L1 连续函数，D(0)=1/4。精确质量为

\[
 M=\|D\|_1=\int_0^\infty
 \frac{e^{-y/4}-e^{-y/2}}{1-e^{-y}}dy
 =\psi(1/2)-\psi(1/4)=\frac\pi2+\log2.                      \tag{10}
\]

若 b 用同 physical-log finite part，并取对应 ψ(1/2)−logπ 的规范，
(9) 的 contact 常数仍为 −γ−log(2π)。因此两完整 arch 源之差恰为 −D，
没有额外手调 δ0。L2 卷积算子 norm 为 M：Young 给上界，连续 Fourier multiplier 在 0 取 M 给下界。
这提供一个真实、有限且已核的局部修复费用；不等于原几何自动拥有该修复源。

更不能把 D≥0 当作正型。直接展开

\[
 D(u)=\tfrac14+\tfrac1{16}|u|-\tfrac1{32}u^2+O(|u|^3).
\]

其一阶导数在 0 跳跃 1/8，分片二阶导数可积，故在 Fourier 约定
\(\widehat D(\xi)=\int D(u)e^{-i\xi u}du\) 下

\[
 \widehat D(0)=M>0,\qquad
 \widehat D(\xi)=-\frac1{8\xi^2}+o(\xi^{-2})\quad(|\xi|\to\infty). \tag{11}
\]

因此 −D 的二次型贡献会变号；有限 norm 不代表有利的 signed Weil 输入。
本轮 sympy 只核 Taylor 系数，(10) 与 (11) 的证明是上述积分／分布分部积分，不依赖数值拟合。

## 7. 原论文确有 anomaly/cocycle 设施，但算术比较未付

§2.5.29 的 b-integral 是由边界 cutoff 和 log counterterm 定义的；
§2.5.30 的 (2.5.65) 明确给出

\[
 b\operatorname{Tr}[A,B]=-
 \frac1{2\pi i}\int_{\mathbb R}
 \operatorname{Tr}(\partial_\lambda I_\nu(A,\lambda)I_\nu(B,\lambda))d\lambda. \tag{12}
\]

原件在 smoothing b-calculus 给出该式，并允许一个因子为 b-differential operator。
这是一种具体 boundary trace defect，不是普通正 trace；其 indicial family 来自同一真实算子的边界核。
它确实适合作为预算片协同变换的设施来源；要用于经典，还须构造实际 A/B 和
同一 arithmetic comparison map，把该 anomaly 逐项识别为 Γ、素数幂和 pole 预算的匹配变化。
不能只宣称存在某个 cocycle 就把它与完整 Weil 配对相等。

为避免法向与定义函数的反向缩放混淆，本稿只消费下列从 cutoff 直接推导的方向：
对 b-density u=A(x,y)|dx/x\,dy|，若 x'=e^{\omega(y)}x+O(x^2)，则

\[
 FP_{x'}(u)-FP_x(u)=\int_{\partial M}\omega(y)A(0,y)dy.      \tag{13}
\]

证明为两 cutoff 边界分别是 x≈εe^{−ω} 与 x=ε，其差积分趋于 ωA(0,y)。
这给 log-scale 的加性 cocycle。若改用 d x(ν)=1 的 normal trivialization，则 ν 的缩放方向相反。
原 PDF 印刷 p47 又显示 μ=aν 时 b-integral 差为 +∫log a·u|∂M，
与前一页 cutoff 条件的直接单边换算有符号/记号相容性疑点；已视觉确认，不把这个方向作为新定理消费。
消费 (13) 无需解决该印刷问题，也不影响 (12) 的准确定位。

§1.3.9 及 §2.9.7 允许改变 η/g 调整原点项；能选零 anomaly 是几何选择，
不等于该选择恰好匹配 (9) 的算术常数。
此外 preserved leaves 的情形一般不是 Riemannian foliation，
不能把 2002 Kähler/Riemannian 正性定理和这里的 b-supertrace 直接拼成经典正性。

## 8. 可消费净后果与仍缺的独立输入

本轮比前轮更强的已闭合内容是：整个单叶标量共同-character 类的穿孔比较边界，
标准 Γ 的 physical-cutoff contact 校准，有限 L1 修复的精确 norm 与 signed 变号，
以及真实 b-trace defect 的原件位置和坐标变换方向。
parity 是具体合法修复候选，不是已取得的 global carrier；(12) 是实际设施，不是 Γ 身份。

连续正反族与函数域 568 检验仍有效：局部双载体／完美 pairing／非零 evaluation minor 不判别 primitive 符号。
函数域还需要同一 global source 的 principal gluing、evaluation kernel、乘法、RR 下界和限制容量上界；
一般 g-integer 要另给相应设施。经典尤其要保全部 prime powers、双 pole、
正确物理 r=e^{u/2}f 坐标、原 norm 与全 complex mixed 方向。
完整预算身份及足够的 signed 容量不等式仍未构造。

要求“所有 cocycle 补偿后的完整 Gram 正定”仍是 Weil 正性的改写；
本轮没有给它独立来源，也没有改善 strongest-old 542+555→557 whole leading4/5、
560 growing K/sign/core/coupling 或 Ξ 识别。实际宏观瓶颈未变。
应停止把所审 all-k 标量 foliation 直接翻译成经典 Γ；
只有真实 parity/source comparison 或同一算术 indicial family/capacity 数据出现时才重新准入。
