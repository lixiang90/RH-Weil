# 实际 prime boundary、物理源 readout 与局部消失过滤的范围

2026-10-22；本轮独占来源／具体候选核查稿，待 root 与 fresh 审阅。
沿 G20261014、冻结 0c4f；不改公共 STATE、cadence 或 Git，不以本稿创建新数学合同。
本稿核查原件已有的边界设施和三个直接候选，严格扣除 404–437 的更强旧资产。

## 1. 恢复后的问题与来源

上一门已经给出不以 Ξ 零除子作定义底空间的实际 relative DGA，
其 H⁰ 仍为 405/519 的保两 degree 解析商。
这次问能否由真实 adelic 边界，把物理源送进有局部消失过滤和平方 RR 的算术截面；
不能把一个旧 local trace、普通指数或任意圆周读出重新命名为 regulator。
当前最强 whole 后果仍为 542+555→557 的 leading 4/5 负惯性**上预算**，不是负谱下界。

本稿现场核读 [CCM2007 固定 v1](https://arxiv.org/html/math/0703392v1) 的
Definition 8.2、§8.2、Proposition 8.13、Proposition 8.21 及 Theorem 6.1、§6.2。
实际输入是 (a_v=0) 闭边界上的逐系数限制及边界动力学；
它不自行给 connecting regulator、算术截面或 RR。以下公式反测为本稿在旧原件上的直接计算。

必须先扣除的旧设施包括：

- [408](../../../notes/408-f1-orbit-completion-and-prime-boundaries.md)：有限箭头源与明确 ℓ¹ 完成的差别；finite boundary 与 real origin 的差别。
- [409](../../../notes/409-f1-boundary-prime-power-kernels-and-heat-defects.md)、[410](../../../notes/410-f1-boundary-kernel-bundles-and-relative-k-classes.md)、[411](../../../notes/411-f1-full-rational-relative-classes-and-logarithmic-trace.md)：实际 prime-power 选择、核丛、相对 K 与 logarithmic 读出；不再声称没有非零边界对象。
- [412](../../../notes/412-f1-transverse-compression-and-periodic-traces.md)：实际横向 \(L^2(\mathbf Q_p)\) 压缩、悬挂、全部 prime-power 权重及指定 Fourier 截止的精确有限部分。
- [420](../../../notes/420-f1-source-hardy-index-and-dual-action.md)、[421](../../../notes/421-f1-weighted-hardy-trace-and-atomic-obstruction.md)：原源 Hardy 族确有约化指数/Chern 数据；带时间权重一般不闭，固定／有界迹范数或共同 BV 预算不能恢复周期原子。
- [425](../../../notes/425-f1-recentered-geometric-corner-and-source-period-finite-part.md)、[430](../../../notes/430-f1-source-stable-periodic-smoothing-algebra.md)、[437](../../../notes/437-f1-finite-source-word-without-a-linear-physical-finite-part.md)：原采样到指定物理球有限部确实已有，真源稳定周期核代数也已有；但实际有限源词可无共尾线性有限部，故不能任意扩大其定义域。

本稿不重证上述全部上游；主原件与旧证明可消费范围不能由一个摘要或 hash 代替。

## 2. 真实 \(\rho_v\) 的定义域，及 acyclicity 没有支付的箭头

取有限箭头代数

\[
 A=\mathscr S(\mathbb A_{\mathbf Q})\rtimes_{\rm alg}\mathbf Q^\times,
 \qquad A_v=\mathscr S(\mathbb A_{\mathbf Q}^{(v)})\rtimes_{\rm alg}\mathbf Q^\times,
 \quad\mathbb A_{\mathbf Q}^{(v)}=\{a:a_v=0\}.
\]

实际边界 map 是

\[
 \rho_v\Big(\sum_q a_qU_q\Big)=\sum_q(a_q|_{a_v=0})U_q. \tag{1}
\]

这是由闭不变子集给出的代数 map。它与 405 的 idele trace

\[
 E\eta(u)=2\sum_{n\ge1}\eta(ne^u),\qquad E_c\eta=e^{u/2}E\eta
\]

有不同 target；不能对任意物理函数 (r) 直接写 \(\rho_v(r)\)。
在 (r=E_c\eta) 上，已有实际 source lift \(1_{\widehat{\mathbf Z}}\otimes\eta\)；
但 537 的 primitive 非根 (r_0) 不在 \(E_c\mathscr S_{\rm even,0}\) 内。
否则完整 (Q_W(r_0)=0)，与 537 的严格正性矛盾。
因此“先取 (E_c^{-1}r)，再限制到边界”既没有覆盖 (r_0)，
也不能因 519 在实际像上的 Fréchet 反演合法，就声明其在全物理源上存在。

408 的精确测试仍有效。对 \(a=1_{\widehat{\mathbf Z}}\otimes\eta\)、
单向箭头 (aU_q)，若 \(\eta(0)=0\)，
则 (1-z aU_q) 在每个有限 (p) 的有限箭头边界源可非单位，
却在指定 \(B_{1,p}=(\ell^1(\mathbf Q^\times,C_0(\mathbb A^{(p)})))^+\) 中可逆。
在 real boundary，源限制已为零。若改用 \(\eta_+(x)=e^{-\pi x^2}\)，
完成后确可由全原点字符检测非零，但该字符为所有边界共有，
并未自动变成只支撑某个 (p) 的除子。

这些不是整条路线的不存在性定理：409–412 已用更细的原点/横向/局部动力数据获得真 prime 选择及周期权。
相反，正确任务是构造穿过这些表示共同核的**相对传递**，
并证明它与物理 DGA 的全关系、两 degree 和原时间测试相容。
对一个在 idele fibre 可缩的复形取 fibre 同调，当然读到零；
不能把这个 fibre 函子的非保守性冒称源 relative 类不存在。

## 3. 直接圆周 periodization：费用可付，但失败全 principal

令 \(\ell_p=\log p\)，取确实存在的周期轨道圆
\(C_p=\mathbf R/\ell_p\mathbf Z\)。物理卷积代数上最直接的读出为

\[
 (\mathcal P_pr)(t)=\sum_{n\in\mathbf Z}r(t+n\ell_p),
 \qquad \rho_p^{\rm orb}(r)=\int_{\mathbf R}r(s)U_s\,ds,
 \quad(U_s\xi)(t)=\xi(t-s). \tag{2}
\]

这在 (\mathscr S_{\exp}) 上定义，compact 源时局部有限。
它尊重**物理**卷积及普通 adjoint \(r^*(u)=\overline{r(-u)}\)；
未中心化函数须先用 \(r=e^{u/2}f\)，因为 \(C(f^\sharp)=(Cf)^*\)。
裸用 (f) 配普通圆周 adjoint 会改变仓库的 sharp。
式(2)是最便宜的 orbit 候选，不把它宣称为原 \(\rho_p\) 的已证 regulator。

对 \(\operatorname{supp}r\subset[-L,L]\)，置 \(N_{L,p}=1+\lceil2L/\ell_p\rceil\)。
逐 fibre 的 Cauchy–Schwarz 给

\[
 \|\mathcal P_pr\|_{L^2(C_p)}^2\le N_{L,p}\|r\|_{du}^2
 \le\frac{N_{L,p}}{\log2}\|r\|_{D_{\log}}^2. \tag{3}
\]

这里 \(\|r\|_{D_{\log}}^2=(2\pi)^{-1}\int\log(2+|t|)|\widehat r(t)|^2dt\)。
这是实际源到目标 (L^2) 的 upper fee；不是 target 高阶 jets 或商正 norm 的费用。
若 \(\ell_p>2L\)，平移支撑互不相交，实际等式为 \(\|\mathcal P_pr\|_2=\|r\|_2\)。
故 (r_0) 在所有充分大 (p) 的这个读出中都可见。
同时，这说明未经配重的 \(\sum_p\|\mathcal P_pr\|_2^2\) 对任何非零 compact 源发散；
它不是局部消失支撑有限的算术 divisor 预算。

两个 pole degree 也不能单靠这个圆周 target 读回。取 compact \(a\) 且
\(\mu_\pm(a)\ne0\)，则 \(\mathcal P_p(\tau_{\ell_p}a-a)=0\)，但
\[
 \mu_\pm(\tau_{\ell_p}a-a)
  =(e^{\pm\ell_p/2}-1)\mu_\pm(a)\ne0.
\]
所以若使用 (2)，须像原 DGA 一样另保两字符；
405 的 \(h\) 应仍给 \((\mu_+(H),\mu_-(H))=(1/4,1/4)\)。
这种直接增广合法，但不修复下面的 principal 失败。

405 给 \(h=E\eta_h>0\)、
\(p_0=(D^2+D)h=E\eta_0\in P_{\rm an}\)，
\(c(p_0)=d(p_0)=0\)。令 \(H=e^{u/2}h\)、\(P=e^{u/2}p_0\)，则

\[
 P=(D^2-\tfrac14)H,
 \qquad\int_{C_p}\mathcal P_pP(t)dt
   =\int_{\mathbf R}P(u)du=-\tfrac14\int H(u)du<0. \tag{4}
\]

全部积分由 (\mathscr S_{\exp}) 衰减合法。于是 (2) 对**每个**有限素数均不消这个实际主关系，
尚未到容量门就失败。只加两 degree 的线性补偿也无效，因为 P 的两个 pole moments 已为零。
这不排除更丰富的 chain-level/transgression 补偿，但不再允许把 raw periodization 当作所需 H⁰-map。
式(4)是旧 405 与周期读出的直接反测，不是新谱结论，也不改旧 412 的完整横向构造。

## 4. 加上真实横向权后：所有 pp 可以恢复，但逐位仍不降商

对未中心化线性测试 (k\in\mathscr S_{\exp})，指定 Tate/Fourier/Haar 规范下的有限位局部量为

\[
 L_p(k)=\ell_p\sum_{m\ge1}\{k(m\ell_p)+p^{-m}k(-m\ell_p)\}. \tag{5}
\]

404 给局部固定点的 \(|1-w|_p^{-1}\) 横向 Jacobian；
更强的 412 已从真 \(L^2(\mathbf Q_p)\) 投影及悬挂得到

\[
 \operatorname{Tr}T_{N,h}
 =\ell_p\big[(2N+1)h(0)+\sum_{m\ne0}p^{-|m|/2}h(m\ell_p)\big],
 \quad h(s)=e^{s/2}k(s). \tag{6}
\]

扣 \((2N+1)\ell_pk(0)\) 而非 \(2N\ell_pk(0)\)，正好得到 (5)。
单位壳层有限部为零是所选加法字符和 Fourier 双截止的已付结果，不能再留自由 \(\delta_0\)。
普通圆周没有负时间的非对称权；真实横向设施已经修复这一点，不应重复报告为未付问题。

但 (5) 本身仍非消关系的 regulator。405 的明确源为

\[
 \eta_0(x)=(4z^4-28z^3+41z^2-9z)e^{-z},\quad z=\pi x^2.
\]

当 \(x\ge2\)，(z\ge4\pi>7)，且

\[
 4z^4-28z^3+41z^2-9z=z\{4z^2(z-7)+41z-9\}>0.
\]

所以 \(p_0(u)=2\sum_{n\ge1}\eta_0(ne^u)>0\) 对 \(u\ge\log2\) 成立。
由 \(p_0^\sharp=p_0\)，每个有限素数 (p\ge2) 都满足

\[
 \boxed{L_p(p_0)=2\ell_p\sum_{m\ge1}p_0(m\ell_p)>0.} \tag{7}
\]

物理写法是 \(2\ell_p\sum_{m\ge1}p^{-m/2}P(m\ell_p)>0\)，中心权没有消失。
这是实际全 pp 的反测，不是只截一阶 prime。用物理偶的 compact 近似恒等元卷积 p₀，
亦得合法局部 mixed 检验趋于 (7)，故不能以“线性而非二次型”避开这个关系问题。

完整显式公式却给

\[
 L_\infty(p_0)+\sum_pL_p(p_0)=0, \tag{8}
\]

因为两 pole moments 与所有非平凡零点上的 \(M_{p_0}\) 均为零。
此处由旧 405 的完整解析恒等式消费 (8)，未预设零点位置。
Σp 绝对收敛；因此 \(L_\infty(p_0)<0\) 是全位补偿的实际必要部分。

结论只是否定“逐位 local trace 加 degree-only counterterm 便降到原商”的候选。
真正 principal divisor 的各地 order 本来可非零；
所以 (7) 不排除允许局部变换、determinant line 与边界 transgression 协同的全球 regulator。
但那必须显式给同一链对象及补偿恒等式，不能把 (8) 的旧谱 trace 直接宣布为正容量。

## 5. 原 norm 费用：point trace 与 quadratic correlation 必须分开

线性 (5) 含 point evaluation，它在原 du 或 Dlog 上没有统一连续界。
取 \(a=\ell_p\)，固定 \(\phi\in C_c^\infty((-1,1)),\phi(0)=1\)，
\(r_\varepsilon(u)=\phi((u-a)/\varepsilon)\)，支撑足够窄以避开其他 \(m\ell_p\)。
则

\[
 r_\varepsilon(a)=1,\quad
 \|r_\varepsilon\|_{du}^2=\varepsilon\|\phi\|_2^2,
 \quad\|r_\varepsilon\|_{D_{\log}}^2
   =O_\phi(\varepsilon\log(1/\varepsilon))\longrightarrow0. \tag{9}
\]

最后一步直接由 \(\widehat r_\varepsilon(t)=\varepsilon e^{-iat}\widehat\phi(\varepsilon t)\) 换元得到。
原 \(\mathscr S_{\exp}\) 的强半范数可控制这些评价；(9) 不排 Fréchet/cofinal/源适应传递。
它也不把任意全空间 inverse 坏 singular value 代作实际源下界。

另一方面，完整 Weil 所需的是二次 correlation \(C_r(s)=(r*r^*)(s)\)，
其 \(|C_r(s)|\le\|r\|_2^2\)。所以固定 (p) 的全部 pp 项确有

\[
 \Big|2\ell_p\sum_{m\ge1}p^{-m/2}\Re C_r(m\ell_p)\Big|
 \le\frac{2\ell_p}{\sqrt p-1}\|r\|_{du}^2. \tag{10}
\]

compact 源时再用真实支撑令 (m\ell_p>2L) 的 correlation 精确为零。
不能将线性 point readout 的不连续，错推为原完整二次 prime form 没有 fixed-window 原费用。
也不能从一个固定 (p) 的 (10) 推所有 p 的成长小费或 primitive positivity。
全线消 Pan 的原 norm 连续 Hausdorff quotient 仍受 553 的强旧稠密结论约束；本稿不重计它。

## 6. 局部消失阶：Schwartz boundary 不自动产生 arithmetic jets

在 p 坐标的 \(C_c^{\rm lc}(\mathbf Q_p)\) 内，令 \(J_0=\{\varphi:\varphi(0)=0\}\)。
每个 \(\varphi\in J_0\) 在某个小球上为零；选紧开集合 K 包含其支撑，
取足够小 (p^N\mathbf Z_p\subset K)，置 \(e=1_K-1_{p^N\mathbf Z_p}\)。
则 \(e^2=e,\ e(0)=0,\ e\varphi=\varphi\)，从而

\[
 J_0^m=J_0\quad(m\ge1),\qquad J_0^m/J_0^{m+1}=0. \tag{11}
\]

这是**局部 test-function factor** 的断言，不无证明地升级为整个非交换完成理想的 equality。
它说明 (a_p=0) 的 ordinary I-adic thickening 在此系数类别不含非平凡 formal normal jets。
vanishing-neighborhood 尺度过滤仍可用，例如 \(\varphi|_{p^N\mathbf Z_p}=0\)；
但它不等于 discrete valuation ring 的 \(\mathfrak m^m/\mathfrak m^{m+1}\)，
也未证明其“阶”对源乘法可加、对 rational principal 有 product formula、与同一截面有限评价兼容。
函数域真 \(\mathcal O_{C,v}\) 的 \(\mathfrak m_v^m\) 与有限长 jets 是另一层算术输入。

因此不能把 408 的有限边界非零性、409 的动力学选择或 (6) 的 pp repeat index 直接叫作截面的消失阶。
若使用 arithmetic subalgebra、analytic germ 或 relative cyclic chains 修复，
要给从实际物理 DGA 到该新系数/过滤的 map；其原 norm、relation 和乘法比较均为待付前件。

## 7. 更强旧来源的约束，及连续/函数域检查

420 已有原源的 rank-zero、非平凡 Chern \([\mathscr L]-[1]\) 族；
不能再把“构造一个边界 index bundle”列作从零开始的任务。
421 已证明在其全 \(\mathcal A_2\) 上带非标量时间权重一般不闭，
并以原子测试量化固定/有界预算 Hardy 读出不能等于原周期分布。
这个结论保留不同小源域、真实 singular 输入、测试后 trace 与相对传递的逃逸。
425/430 更进一步已有源稳定的周期 readout 域，而 437 的 actual 有限词说明
“所有源词＋任意线性体积扣除＋共尾有限部”已不能自动成立。
所以新 regulator 要支付明确 chain/boundary 补偿和其合法域；不能仅换源 bundle 或自由补原子。

连续正反控制很直接：periodization (2)、local evaluation 及其费用不使用 g-prime 分布，
故对旧 \(R_d=\mathbf C[z]/(z^2+d)\)、\(z^\dagger=-z\) 的 (d=\pm1/16) 都原样可设，
而其 primitive trace 型 \(2|A|^2+2d|B|^2\) 号不同。
这只表明这些线性/局部设施不足以识别 Weil 号；不声称连续系统已天然有经典加法 adeles。

函数域模数／次数方向的周期 quotient 为 \(\mathbf Z/\deg(v)\mathbf Z\)，
闭点 Frobenius orbit 的周期同其 degree；不将整个 \(C_K/K_v^\times\) 等同这个有限商，
其 compact/Pic 成分仍须保留。与各闭点 orbit 的对应需选 orbit 中一个点；
这仍不是截面/RR 的比较。
最低成本负测为 \(C=\mathbf P^1/\mathbf F_q\)：其 primitive (H^1=0)，
但 raw orbit periodization 将有限序列 \(\delta_0\) 送至每个 cycle 上的非零元素。
所以 raw local orbit 不能直接等同全球 primitive cohomology。
真函数域另有 \(C\times C\) 上有效对应、局部 intersection orders、principal product formula、
截面乘法与 signed RR，再以全部 Frobenius iterates 识别 Weil Gram。
H⁰/H² 和所有 period aliases 均须保留；不能以一个周期圆的正 (L^2) norm 代替这段几何。

## 8. 完整 Γ、全 pp、双 pole 的同源责任及本稿消费边界

物理坐标的完整规范继续是

\[
\begin{aligned}
Q_W(r)={}&2\Re(\mu_+(r)\overline{\mu_-(r)})+
[\psi(1/4)-\log\pi]\|r\|_{du}^2\\
&+\frac12\int_0^\infty\frac{2e^{-v/2}}{1-e^{-2v}}
\|\tau_vr-r\|_{du}^2dv
-2\sum_{p,m\ge1}(\log p)p^{-m/2}\Re C_r(m\log p).
\end{aligned} \tag{12}
\]

(12) 是 405/568 的已付完整解析身份，(5)–(8) 没有添加独立正性。
real boundary 的 \(\eta(0)=0\) 不意味着其 complete Γ/contact 为零；
Γ 来自选定局部 Fourier/normal action 的整体分布，不能用全原点 evaluation 取代。
有限位 return/valuation 权已有实际算子设施，但尚无同一个 arithmetic section 的 order 身份。
两个 pole characters 在 DGA 中已被保留，但仍未证明它们是该截面平方 RR 的唯一 defect。

本稿付的是候选的实际定义域、直接 principal 反测、fixed-window 原费用和 old-source 范围恢复；
不新增 classic 独立容量或 whole/core/Ξ 后果。
下一真正能改变选择的输入为：**相对 chain/regulator 的一个实际公式**，
其边界在原源全 Pan 上为相容的 exact/principal 变换，保 537 非根及 h 双 degree，
并把某个独立 arithmetic germ/valuation filtration 与同一截面的 height/平方 RR 比较。
若只取 (H^0\simeq F_c/P_{\rm an}) 后读完整 spectral trace，仍是旧商包装；
若只公设 (12) 是非负 RR 系数，仍是 Weil 正性的等价/充分包。
本稿未排合法的 relative、非交换、Fréchet、cofinal 或源依赖修复。
