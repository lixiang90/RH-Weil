# Ivić 原零密度输入与原 scalar 第四矩增长指数

日期：2026-10-08  
作者：twisted_research  
研究基线：已推送 475 bundle，commit 5fe68395d20e9738ecc0ba64e8a762f4d93bd073。  
状态：完整研究推导，待其他作者独立审查。本文只新增证据；不修改 475、旧论文、脚本或既有源。结论是增长上界的加强，尚非有限第四矩常数、临界线比例或无零边界的加强。

## 1. 对象和冻结前件

沿用原对象 \(X=T/(2\pi)\)、\(\ell=\log X\)、\(d=\lfloor X\ell\rfloor\)、\(\eta=2\pi/\ell\)，原 \(C^2\) 窗 \(\phi\) 和 \(a_\ell=\ell^{-1}\int_I\phi^2\ge c>0\)。高素数 scalar 为

\[
 P_H(t)=\frac1{a_\ell\ell}
 \sum_{\sqrt X<p\le X}\frac{\log p}{\sqrt p}p^{it},
 \qquad
 \mathcal M_T=\frac1T\int_{T/4}^{4T}|P_H(t)|^4\,dt. \tag{1}
\]

只假设同一 \([R_\theta]\) 中有关 \(\zeta\) 的结论：每个非平凡零点实部 \(\beta\le\theta\)，其中本报告固定 \(5/6<\theta\le7/8\)，保持原零包源的范围。不把该结论替换为其他 Hecke 家族的密度假设。

| 本地前件 | canonical LF SHA256 |
|---|---|
| [真实正高度零包第四矩源](hybrid-positive-height-zero-packet-fourth-upper-research-radial.md) | 8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481 |
| [原 scalar 准入源](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [固定起点原 half-Gram 采样源](hybrid-fixed-start-half-gram-sampling-research-root.md) | 7ed68a71d4d22d0bf1d90c61cef231534737188131aad9842669cd11f19c82cc |

本文只替换这些源中零点加权求和所用的密度指数；原 cutoff、共同 \(u\)、窗口、正高度 guards、proper powers 和真实有限载波保持相同。

## 2. 已核的一手 Ivić 输入

Ivić 本人的 [*Topics in recent zeta function theory*](https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/86/6d/866d1cf0-a942-4f8a-9d30-7cb3b03e1b1c/i_ivic-66.pdf)，印刷第 182–183 页（PDF 第 187–188 页），从 (9.56)–(9.60) 的 \(k=2\) 选择得到 Theorem 9.3，式 (9.63)：

\[
 N(\sigma,V)\ll_{\varepsilon,\sigma}
 V^{\,n_I(\sigma)+\varepsilon},
 \qquad n_I(\sigma)=\frac{3(1-\sigma)}{2\sigma},
 \qquad \frac{3831}{4791}<\sigma<1. \tag{2}
\]

这里 \(N\) 按重数计 \(\beta\ge\sigma,\ |\gamma|\le V\) 的 \(\zeta\) 零点。Ivić 的 [2001 年本人综述](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/Ivic-Sanutalk.pdf) §3，印刷第 5–6 页（PDF 第 5–6 页），另明确给出相同计数定义、(2) 和范围。因 \(3831/4791<4/5\)，实际使用的整个 \([4/5,\theta]\) 都在前件内。

核验读取了原书相应证明与定理，而非仅依赖数据库表格。原书大 PDF 因超过 web 单页大小上限，另以 Python 仅在内存下载、提取上述页；未在仓库保存副本。该 PDF 共 278 页，10538942 bytes，原二进制 SHA256 为 fafac152db87abe132858fa97d8fe501c61cd261e20732ef701396fba27b61aa。这里采用严格下端，避开原书与后来综述端点表述差异；实际网格从 \(4/5\) 起，故没有影响。本文不要求隐含常数对移动 \(\sigma\) 统一：后文只有先固定的有限网格，所以每个固定 \(\sigma\) 的 (2) 已足够。任意固定幂次日志损失均可吸收入最终的 \(\varepsilon\)。

## 3. 整个实部区间的包络，而非仅替换端点

在 \([1/2,4/5]\) 仍用冻结零包源已采用的经典输入：

\[
 n_0(\sigma)=
 \begin{cases}
 3(1-\sigma)/(2-\sigma),&1/2\le\sigma\le3/4,\\
 3(1-\sigma)/(3\sigma-1),&3/4\le\sigma\le4/5.
 \end{cases} \tag{3}
\]

令 \(f(\sigma)=4\sigma-3+n(\sigma)\)。低段的导数分别为

\[
 f'_0(\sigma)=
 \begin{cases}
 4-3/(2-\sigma)^2,&\sigma\le3/4,\\
 4-6/(3\sigma-1)^2,&\sigma\ge3/4.
 \end{cases}
\]

两者在相应区间均为正，且两段在 \(3/4\) 连续。因此

\[
 \sup_{1/2\le\sigma\le4/5}f_0(\sigma)
 = f_0(4/5)=\frac{22}{35}. \tag{4}
\]

在 \(4/5\le\sigma\le\theta\) 用 (2)，得到

\[
 f_I(\sigma)=4\sigma-3+\frac{3(1-\sigma)}{2\sigma},
 \quad
 f'_I(\sigma)=4-\frac{3}{2\sigma^2}
 \ge \frac{53}{32}>0. \tag{5}
\]

又 \(f_I(5/6)=19/30>22/35\)，两者相差 \(1/210\)，故本报告实际整个区间的最大指数正是

\[
 B_I(\theta)=4\theta-3+\frac{3(1-\theta)}{2\theta},
 \qquad 5/6<\theta\le7/8. \tag{6}
\]

在 \(4/5\) 处采用的两个上界不需拼成连续曲线；(4) 与 \(f_I(5/6)>22/35\) 已检查低区 supremum 不夺取最终最大值。

## 4. 原真实零包到同 cutoff 的迁移

冻结零包源的真实 Perron 核是 \((x^z-y^z)/z\)，其中 \(x=\lfloor X\rfloor+1/2\)、\(y=\lfloor\sqrt X\rfloor+1/2\)。它是 entire，但不删除实际 \(\zeta\) 零点落在 \(z=0\) 的留数。沿用其全部高度尾和避零横边后，原 von Mangoldt scalar 满足

\[
 \widehat{\mathcal M}_T
 \ll \frac{\ell^3}{T}
 \sum_{\substack{\zeta(\beta+i\gamma)=0\\|\gamma|\le16T}}
 X^{4(\beta-1/2)_+}
 +O(X^{-2}\ell^4). \tag{7}
\]

现在固定目标 \(\varepsilon>0\)，再选固定网格宽度 \(\nu>0\) 及固定密度损失 \(\varepsilon_1>0\)，使 \(4\nu+\varepsilon_1\) 与日志吸收总额小于目标损失。分开 \(\beta\le1/2\)（总零数 \(O(T\log T)\)），再以有限网格分割 \((1/2,\theta]\)，并把 \(4/5\) 作为网格端点。对每格下端 \(\sigma_j\)，有

\[
 \sum_{\substack{\sigma_j<\beta\le\sigma_j+\nu\\|\gamma|\le16T}}
 X^{4(\beta-1/2)}
 \le X^{4(\sigma_j+\nu-1/2)}N(\sigma_j,16T). \tag{8}
\]

分别代入 (2)、(3)，然后用 (4)–(6)。网格和损失先固定，最后让 \(T\to\infty\)，有限多个隐含常数取最大即可。因此

\[
 \widehat{\mathcal M}_T\ll_{\theta,\varepsilon}T^{B_I(\theta)+\varepsilon}.
 \tag{9}
\]

首个贴近 \(1/2\) 的格也可直接用总零数界，至多付 \(T^{4\nu}\)；它小于 (6) 的正指数。没有按高度移动 \(\sigma\) 或先取无穷网格的步骤。

冻结源已经证明原 sharp high cutoff 删除 proper powers 的归一化 \(L^4\) 范数误差 \(O(X^{-1/12})\)。仅用三角不等式，(9) 给同 (1) 的

\[
 \boxed{\mathcal M_T\ll_{\theta,\varepsilon}T^{B_I(\theta)+\varepsilon}}.
 \tag{10}
\]

这不是声称两个第四矩本身相差 \(o(1)\)；增长时必须保留四次方展开的交叉项。

## 5. 原 half-Gram 的增长迁移

固定起点采样和原 scalar 准入源中的误差函数为

\[
 E_T(M)=N_\ell\sqrt M
       +C\frac{m_H}{T}M^{1/4}
       +C\frac{m_H^2}{T},
 \qquad N_\ell=O_\phi(1),\quad m_H\ll\frac{\sqrt X}{\ell}. \tag{11}
\]

它们把原同 \(u\) 窗下 \(r_\sigma\) 的上界控制为固定常数倍 \(E_T(\mathcal M_T)^2+O(1/\ell)\)，分别适用于准入源的短载波平均及采样源的每个原允许起点。代入 (10)，并**保留**交叉项，再用 \(B_I(\theta)<1\)，得

\[
 E_T(\mathcal M_T)^2
 \ll_{\theta,\varepsilon}
 T^{B_I(\theta)+\varepsilon}.
 \tag{12}
\]

例如最大的残余交叉项可按
\((m_H^2/T)\sqrt{\mathcal M_T}\ll\ell^{-2}T^{B_I/2+\varepsilon}\)
控制，并非在增长情形直接丢作 \(o(1)\)。这给原实际 half-Gram 增长界，不移除内部 \(P\)，不改变载波或 prime 中心，也不要求未知全第四矩已为 \(O(1)\)。

## 6. 数值与辅助 Theorem 50 的准确范围

在 \(\theta=7/8\)，

\[
 n_I(7/8)=\frac3{14},\quad
 B_I(7/8)=\frac57,\quad
 \frac{19}{26}-\frac57=\frac3{182},\quad
 \frac34-\frac57=\frac1{28}. \tag{13}
\]

在已冻结三次边界数值 \(\theta_* \approx0.874957019420098946\)，仅数值展示 (6) 为 \(B_I(\theta_*)\approx0.7141980029530279\)。

辅助一手核验：[Tao–Trudgian–Yang, arXiv:2501.16779](https://arxiv.org/html/2501.16779v1) Definition 37 与 Theorem 50 给 \(n_{50}(\sigma)=3(1-\sigma)/(10\sigma-7)\)，声明范围 \(7/10<\sigma<1\)。Definition 37 的实际量词为：对每个固定 \(\sigma,\varepsilon\)，存在固定左移 \(\delta>0\)、常数 \(C\)，从 \(V\ge C\) 起控制 \(N(\sigma-\delta,V)\)；取 infimum 的损失可并入 \(\varepsilon\)。单调性即给普通 \(N(\sigma,V)\)，但未给任意随 \(V\) 移动网格的统一常数。

为辅助比较，限制到 \(\sigma\ge6/7\)：其证明取 \(\tau_0=10\sigma-7\)，确有 \(\tau_0\ge3-3\sigma\)。Heath–Brown large-value 项在 \(\tau=\tau_0\) 等号且较小 \(\tau\) 保持所需不等式；zeta 项由 \(\mu(7/10)\le3/40\) 对 \(\tau<4\tau_0/3\) 消除。这里不借“Montgomery 猜想”作为假设，而使用文中的已证 large-value bounds。低至 \(7/10\) 的完整声明不是主迁移 (6) 所需前件。

当 \(6/7\le\theta\le7/8\) 时，用 Theorem 50 与经典输入在 \(6/7\) 拼接，也得完整
\(B_{50}=4\theta-3+3(1-\theta)/(10\theta-7)\)：该顶段导数在 \(6/7\) 为 \(43/121>0\)，此后增加。它在 \(7/8\) 同为 \(5/7\)，但在 \(\theta_*<7/8\) 比 (6) 稍弱，因为 \(2\theta>10\theta-7\)。Guth–Maynard 在 \(7/8\) 给 \(n=15/59>3/13\)，不能作为此处加强；Chen–Debruyne–Vindas 的 \(24(1-\sigma)/(30\sigma-11)\) 有下端 \(279/314>7/8\)，亦不能套到本对象顶段。后者范围已核 [原论文 Theorem 1.2 与 Appendix A](https://ems.press/content/serial-article-files/48886?nt=1)。

## 7. 结论和未付主预算

(10)、(12) 是同一原对象的有效增长加强；在现有 \([R_\theta]\) 下不引入新零点族、角色掩码、平方平均或移位卷积前件。这里并未把旧 \(\theta_*\) 换成新无零区域。

指数 \(5/7\) 仍为正。原完整 signed 四全异 near-resonance、\(O(1)\) 第四矩或可用固定常数上界仍未由该输入支付。因此本报告不给新 simple/critical-line 比例，也不宣布 RH。

在本报告整个参数范围，旧点值增长指数与新增指数之差也严格为正：
\[
 (2\theta-1)-B_I(\theta)
 =\frac{(1-\theta)(4\theta-3)}{2\theta}>0.
\]

