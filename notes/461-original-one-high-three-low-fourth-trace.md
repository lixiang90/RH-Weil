# 461：原有限矩阵的一高三低混合四迹为小量

2026-10-07。相对于项目明列的 [R]，完成原 actual13 sector；没有得到
完整第四矩常数、新零点比例或新无零边界。

本结果把无零输入真正用于原零点检测矩阵：不只估计零延拓物理词，还
控制其三个内部有限投影。原 7/8 输入已足够，不依赖更新的三次边界。

## 1. 对象与定理

沿用 AF 的原采样、原 C² 窗和归一化，见
[原 13/31 定义](../reviews/2026-10-07/hybrid-one-three-mixed-prime-sector-research.md)。
置

\[
 X=T/(2\pi),\quad L=\log X,\quad Z=\sqrt X,\quad
 d=\lfloor XL\rfloor,\quad I=[-L/2,L/2],
 \qquad \tau_k=T+2\pi k/L.
 \tag{1}
\]

\(E e_k=L^{-1/2}1_I e^{i\tau_k u}\)，\(0\le k<d\)，是实线
\(L^2\) 中的等距嵌入；\(P=EE^*\)，\(Q=1-P\)。
原实偶窗 \(0\le\phi\le1\) 支撑于 \(I\)，
\(a_L=L^{-1}\|\phi\|_2^2\) 有固定正下界，\(\phi,\phi^2\) 的
一、二阶导数 \(L^1\) 范数一致有界。这包括此前采用的 flat 和
Montgomery–Taylor 窗配原固定宽度 taper。

对 genuine primes 定义

\[
 B_R=-\sum_{p\in R}\frac{\log p}{a_LL\sqrt p}
 M_\phi(R_{\log p}+R_{-\log p})M_\phi,
 \qquad C_R=E^*B_RE,
 \tag{2}
\]

其中 \(R=L\) 表示 \(p\le Z\)，\(R=H\) 表示 \(Z<p\le X\)。
\(R_s f(u)=f(u+s)\) 每次均按实线零延拓。所有原符号和三个内部
\(P\) 保留。

**定理。** 假设 [446](446-uniform-prime-twists-on-the-original-gabor-frame.md)
明列的 zeta 无零输入及 fixed-gap logarithmic-control 在
\(\theta<9/10\) 时成立。则

\[
 \boxed{\operatorname{Tr}(C_HC_L^3)=o(d)=o(N(T,2T)).}
 \tag{3}
\]

这里只使用 conductor-one zeta 的该输入。原 \(\theta=7/8\) 可取
\(a=89/100\)；一般 \(\theta<9/10\) 先固定 \(\theta<a<9/10\)。
定理覆盖 entire13：重复和全异素数、全部十六个
符号及四个高素数位置，不以未知的完整第四矩为前件。
\(d/N(T,2T)\to1\) 足够；不声称二者相差 \(O(L)\)。

## 2. 先付真实物理词

[物理 13 完整推导](../reviews/2026-10-07/hybrid-signed-one-three-physical-resonance-research.md)
证明四个 placements 各自满足

\[
 \operatorname{Tr}(E^*B_L^jB_HB_L^{3-j}E)=o(d),
 \qquad 0\le j\le3.
 \tag{4}
\]

其重要付款如下：

- 原 finite carrier 是 \(K_d(S)=d^{-1}\sum_k e^{i\tau_kS}\)。
  原路径窗保留所有累计位移；其 endpoint overlap 同时处理
  \(S\approx\pm L\) 的 alias。
- 近共振先联合分离四个共享窗，再把三个低素数乘积与高素数、或
  两低乘积与高低乘积，聚合成真实整数系数。联合 Hilbert 界给
  \(O((\log(2+L))^4/L)\)，不用未知素数相关。
- Far 保留三个独立的原 sharp low prefixes，包括真实存在的
  \(pqr>2X\)。联合 Fourier 分离后才应用 446 的 canonical 界；
  全部五个 C² Fourier ghosts 与 principal-height 峰另行付款。

Middle-far 的关键幂为
\(X^{(5/2)a-9/4}\)，所以 \(a=89/100\) 给 \(X^{-1/40}\)。
这些论证保留四个物理 placements，未在带末端 \(P\) 的物理词中
免费循环或删除内部投影。

## 3. 频带内的真实投影交叉界

[有限频带完整推导](../reviews/2026-10-07/hybrid-one-three-finite-band-admission-research.md)
补上 (4) 到 (3) 的接口。令 \(\mathcal F\) 为 unitary Fourier transform，
并写原实乘子

\[
 D_R(t)=-\frac1{a_LL}\sum_{p\in R}
 \frac{\log p}{\sqrt p}(p^{it}+p^{-it}),\quad
 B_R=M_\phi\mathcal F^{-1}M_{D_R}\mathcal F M_\phi.
 \tag{5}
\]

固定 \(J=[T/2,3T]\)，令 \(D_R^g=D_R1_J\)，并相应定义
\(B_R^g,C_R^g\)。446 给真正 global operator bounds

\[
 \|B_H^g\|\le q_H\ll X^{a-1/2}L,
 \qquad \|B_L^g\|\le q_L\ll Z^{a-1/2}L.
 \tag{6}
\]

这里没有把原全高度乘子改称 canonical 小量。\(P\) 仍是 interval
内有限 carrier；它不与 \(D_R^g\) 交换。

由于 \(B_R^g\) 的输出支撑于 \(I\)，可在 \(I\) 上全部整数 carrier
\(j\in\mathbf Z\) 中准确计算 \(QB_R^gP\)。差值 \(n=j-k\) 对应的
outside pairs 数量是 \(\min(d,|n|)\)。其 shifted-grid bound 为

\[
 L^{-2}\sum_n\min(d,|n|)
 |\widehat\phi(2\pi n/L-\xi)|^2
 \ll\log(2+L)+L|\xi|.
 \tag{7}
\]

Minkowski、\(\|\widehat\phi\|_1\ll\log(2+L)\) 和
\(\int|\xi|^{1/2}|\widehat\phi(\xi)|\,d\xi\ll1\) 随即给

\[
 \ell_R^g:=\|QB_R^gP\|_{\rm HS}\ll\sqrt L\,q_R.
 \tag{8}
\]

这是原投影的交叉界，未换成连续 Fourier 频率投影。

## 4. 两次交叉与坏高度的付款

对于任意四个 selfadjoint bounded \(V_i\)，逐个插入三个 \(P\)，
令 \(y_i=\|V_i\|\)、\(\ell_i=\|QV_iP\|_{\rm HS}\)。
精确 telescoping 与 HS–HS 配对给

\[
 \left|\operatorname{Tr}(PV_1V_2V_3V_4P)
 -\operatorname{Tr}(PV_1PV_2PV_3PV_4P)\right|
 \ll\sum_{i<j}\ell_i\ell_j\prod_{k\ne i,j}y_k.
 \tag{9}
\]

每项包含两次 crossing。对一高三低的 good operators，(6)–(9)
给差值 \(O(Lq_Hq_L^3)\)，除以 \(d\) 后为
\(O(X^{(5/2)a-9/4}L^4)=o(1)\)。原 \(7/8\) 输入取
\(a=89/100\) 时，这项为 \(O(X^{-1/40}L^4)\)。

最后回到原全高度对象。记
\(m_H\ll\sqrt X/L\)、\(m_L\ll\sqrt Z/L\) 为 absolute multiplier
上界。原 packet 的带外 HS 尾为 \(O(T^{-1})\)，故
\(\|C_R-C_R^g\|_{\rm HS}\ll m_R/T\)。
物理四词的三次 \(\phi^2\) 卷积按首个大于固定 \(cT\) 的频率跳跃
分解；该卷积在长度 \(O(T)\) input band 上的 HS 尾也是
\(O(T^{-1})\)。右 packet 保留归一化 \(1/L\)，左 packet 的 HS
范数至多 \(\sqrt d\)。两种替换费用均为

\[
 \frac{\sqrt d}{T}m_Hm_L^3,
 \qquad d^{-1}\frac{\sqrt d}{T}m_Hm_L^3
 \ll X^{-1/4}L^{-9/2}=o(1).
 \tag{10}
\]

因此原物理词、good 物理词、good finite 词、原 finite 词之间的
每一步差值都为 \(o(d)\)。结合 (4) 得到定理 (3)。

## 5. 对完整比例预算的实际推进

有限矩阵中的循环迹允许准确写

\[
 \begin{aligned}
 \operatorname{Tr}(C_H+C_L)^4={}&
 \operatorname{Tr}C_H^4+\operatorname{Tr}C_L^4
 +4\operatorname{Tr}(C_H^3C_L)\\
 &+6\|C_HC_L\|_{\rm HS}^2
 -\|[C_H,C_L]\|_{\rm HS}^2+o(d).
 \end{aligned}
 \tag{11}
\]

本次真正移除了整个一高三低项。三高一低、22 的联合 product norm
和 commutator、high 全异四词仍待同对象预算；原背景
\(\operatorname{Tr}(AC^3)\) 也仍开放。
不能将各 repeated 子常数、low 一侧上界与 (3) 相加成完整四矩常数。

无零方向另有 [459](459-natural-inverse-and-primitive-zero-joint-reduction.md)
的有限 primitive 恢复，把下一严格 mixed saving 定位于同对象的
primitive residues/joins 联合能量。它不由 (3) 自动获得 saving。

本轮是结合研究的实质进展，Goal 保持完整目标和 active 状态。
既有引用输入下 \(\sigma_*\approx0.874957019420099\) 保持；
没有确认新的全边界，因此未另写正式边界论文。
