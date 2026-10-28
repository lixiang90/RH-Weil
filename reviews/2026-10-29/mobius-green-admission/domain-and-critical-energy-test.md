# Möbius causal Green 响应：实际域、临界能量和旧范围核对

2026-10-29。限定支持原稿；不新建数学合同、不计轮、不认证几何 principal。对象采用405／518–520的原映射，复数情形由逐项复化得到。本稿不更改旧原件，不依赖RH、简单零点或零点分离，不作新文献检索。

## 1. 固定对象和源公式

405的bare源空间是 \(\mathcal S_{\exp,\mathbb C}\)，实际像为

\[
 E\eta(u)=2\sum_{m\ge1}\eta(me^u),\qquad
 \eta\in\mathscr S_{e,0,\mathbb C}
 =\{\eta\in\mathscr S(\mathbb R,\mathbb C):
 \eta\text{偶},\ \eta(0)=0,\ \int_\mathbb R\eta=0\}.
\]

519已付 \(I=J=E(\mathscr S_{e,0,\mathbb C})\)，不是只有稠密原像。物理源为
\(r(u)=e^{u/2}f(u)\)。乘以 \(e^{u/2}\) 是该Fréchet空间的自同构，但不会把bare的两个次数条件省去。定义实际响应

\[
 V_r(t)=\sum_{n\ge1}\frac{\mu(n)}{\sqrt n}\,r(\log n-t).
 \tag{1}
\]

这是给定算术Möbius系数的真实算子。518(11)的旧逆为
\(\theta_f(x)=\tfrac12\sum_n\mu(n)f(\log nx)\)，因此准确关系是

\[
 V_{e^{u/2}f}(t)=2e^{-t/2}\theta_f(e^{-t}).                 \tag{2}
\]

故(1)并非新的逆映射；它是518的反射对数坐标及半密度运输。因子2来自原E的正负整数求和，不能删除。

若 \(r\in C_c^\infty\)、\(\operatorname{supp}r\subset[-L,L]\)，每个紧t区间中(1)只有有限项，因而平滑；\(V_r(t)=0\) 对 \(t<-L\)。每阶导数由 \((-1)^jr^{(j)}\) 给出，且

\[
 |V_r^{(j)}(t)|\le C_{r,j,L}e^{t/2}\quad(t\ge-L).         \tag{3}
\]

这里用到的只是 \(\sum_{n\le Y}n^{-1/2}\le2\sqrt Y\)；不使用Möbius cancellation。对一般 \(r\in\mathcal S_{\exp,\mathbb C}\)，记 \(p_{N,j}\) 为原指数半范数。任意整数N≥1给

\[
 \sum_n n^{-1/2}|r^{(j)}(\log n-t)|
 \le\begin{cases}
 p_{N,j}(r)e^{Nt}\zeta(N+1/2),&t\le0,\\
 C_Np_{N,j}(r)e^{t/2},&t\ge0.
 \end{cases}                                             \tag{4}
\]

第二行把n在 \(e^t\) 两侧分开，分别求 \(n^{N-1/2}\) 与 \(n^{-N-1/2}\) 的幂和。紧集上一致绝对收敛允许逐项求导，给连续线性映射 \(V:\mathcal S_{\exp,\mathbb C}\to C^\infty_{\mathrm{loc}}(\mathbb R)\)。负时间端任意指数衰减；正时间仅有(3)这样的粗界，不免费是L²。

“Green”也可用一个实际inverse恒等式解释。令 \(\mathcal C U(t)=\sum_{m\ge1}m^{-1/2}U(t-\log m)\)。对 \(U=V_r\)，上述负端估计支付局部换序，除数分组给

\[
 \mathcal C V_r(t)
 =\sum_k k^{-1/2}r(\log k-t)\sum_{n\mid k}\mu(n)
 =r(-t).                                                \tag{5}
\]

对compact源这一换序在每个t实际上有限；对 \(\mathcal S_{\exp}\) 用足够大的N给 \(\sum_{m,n}(mn)^{-N-1/2}<\infty\)。式(5)证明实际算术线性逆，不是主除子／正则单位商定理。

## 2. 整个真实像及全部平移的响应，含精确norm

对 \(f=E\eta\)，518重建给 \(\theta_f=\eta\)。也可在(1)直接用双和的绝对收敛按nm分组，得到

\[
 \boxed{V_{r_\eta}(t)=2e^{-t/2}\eta(e^{-t}),\qquad
 r_\eta(u)=e^{u/2}E\eta(u).}                              \tag{6}
\]

双和绝对界在固定t可由 \(|\eta(mne^{-t})|\le C_N(mne^{-t})^{-N}\)、N>1支付，导数同理。\(t\to+\infty\) 时，偶性及 \(\eta(0)=0\) 给 \(\eta(x)=O(x^2)\)，所以(6)为 \(O(e^{-5t/2})\)；负端由Schwartz任意幂衰减支付。实际精确能量是

\[
 \boxed{\|V_{r_\eta}\|_{L^2(dt)}^2
 =4\int_0^\infty|\eta(x)|^2dx
 =2\|\eta\|_{L^2(\mathbb R)}^2.}                          \tag{7}
\]

换元为x=e^{-t}；这没有使用 \(\int\eta=0\) 来偷换目标次数。519的逆连续性使(7)在整个I上由有限个原 \(p_{N,j}(f)\) 控制；也不把原物理 \(\|r\|_{L^2(du)}\) 当作这一Green范数。

因此所有 \(e^{u/2}P_{\rm an}\) 的响应确属L²，且更强地，整个 \(e^{u/2}I\) 都属该域。平移应区别bare与physical：

\[
 \begin{aligned}
 V_{\tau_a r}(t)&=V_r(t+a),\quad \tau_a r(u)=r(u-a),\\
 r_{\tau_af}(u)&=e^{a/2}\tau_ar_f(u),\\
 V_{r_{\tau_af}}(t)&=e^{a/2}V_{r_f}(t+a).
 \end{aligned}                                           \tag{8}
\]

bare \(\tau_af\) 对应真实源 \(\eta_a(x)=\eta(e^{-a}x)\)。所以405全部非compact真实Pan及其全部固定平移都通过L²测试，系数和norm运输明确；不能混同bare平移与物理平移。

## 3. 所有非零compact源的临界L²能量均不有限

**命题。** 对每个非零 \(r\in C_c^\infty(\mathbb R,\mathbb C)\)，由(1)定义的 \(V_r\notin L^2(\mathbb R,dt)\)。这是原始未加权、未截断Green响应的域结论。

取 \(\operatorname{supp}r\subset[-L,L]\)，定义整函数
\(M_r(z)=\int r(u)e^{zu}du\)。对 \(\Re z>1/2\)，绝对Fubini给

\[
 F_r(z):=\int_{-L}^\infty V_r(t)e^{-zt}dt
 =M_r(z)\sum_n\frac{\mu(n)}{n^{z+1/2}}
 =\frac{M_r(z)}{\zeta(1/2+z)}.                            \tag{9}
\]

绝对界是
\(\sum_n n^{-\Re z-1/2}\int|r(u)|e^{\Re z\,u}du<\infty\)。并未在临界线上形式代入Euler逆。

假设 \(V_r\in L^2\)。因其支撑在[-L,∞)，其Laplace积分在 \(\Re z>0\) 全纯，紧子域上的各阶导数由Cauchy–Schwarz及指数衰减支配。并有

\[
 |F_r(\sigma+i\tau)|
 \le \frac{e^{\sigma L}}{\sqrt{2\sigma}}\|V_r\|_2,
 \qquad\sigma>0.                                       \tag{10}
\]

(9)和解析延拓说明：右半面内 \(M_r(z)/\zeta(1/2+z)\) 的每个非平凡零点分母极都须可去。可精确地把 \(\zeta(1/2+z)F_r(z)=M_r(z)\) 作为右半面的亚纯恒等式使用；ζ在z=1/2的极要求F的相应零，不能被当成零点障碍。

右半面边界上的极也不允许。若 \(z_0=i\gamma\)、\(\zeta(1/2+i\gamma)=0\)，而该商在z0有k≥1阶极，则沿 \(z=z_0+\sigma\) 有
\(|F_r(z)|\ge c\sigma^{-k}\) 对足够小的σ>0。这与(10)的 \(O(\sigma^{-1/2})\) 矛盾。因而L²假设迫使 \(M_r\) 在每个 \(z=\rho-1/2\)、\(\Re\rho\ge1/2\) 至少具有mρ阶零。多重零点不能只消一次值。

接下来这些完整消失条件与compact源的整函数增长矛盾。Fourier唯一性保证非零r的 \(M_r\not\equiv0\)。选择 \(M_r(z_*)\ne0\)。由compact支撑，

\[
 \max_{|z-z_*|\le2R}|M_r(z)|
 \le\|r\|_1\exp\{L(|\Re z_*|+2R)\}.
\]

Jensen不等式给（零点计重数）

\[
 n_{M_r}(R;z_*)\log2
 \le \log\max_{|z-z_*|\le2R}|M_r(z)|-\log|M_r(z_*)|
 \le 2LR+C_r.                                          \tag{11}
\]

所以 \(M_r\) 在 \(|\Im z|\le T\)、\(0\le\Re z\le1/2\) 中的零数是 \(O_r(T)\)。相反，无条件Riemann–von Mangoldt计数

\[
 N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}
       -\frac{T}{2\pi}+O(\log T)
\]

与保持正高度及重数的函数方程对称 \(\rho\mapsto1-\overline\rho\) 给

\[
 \#\{\rho:0<\Im\rho\le T,\ \Re\rho\ge1/2\}
 \ge\tfrac12N(T)\gg T\log T,                            \tag{12}
\]

仍计重数。因此(11)不可能覆盖(12)的全部必要jets；无条件至少有一个未消极（实际上高度无界地有）。若其在开右半面，违背全纯性；若在边界，违背(10)。矛盾证明命题。

这个论证不需要已知正比例中心线零点，不要求RH或任何零点简单性，也没有把零点逐个距离下界塞进估计。它同时适用于实源、复源、任意给定compact支撑，以及零均值／双矩零的compact子类。

## 4. 裸L²商的实际含义与最便宜反测

裸类 \([V_r]\) 可取于 \(L^2_{\mathrm{loc}}/L^2\) 或ambient \(C^\infty/(C^\infty\cap L^2)\)。它消去Pan并在compact源上单射，尚非Hausdorff primitive或正Hilbert结构。

对任意U取χ_jU截断，分别在局部L²／局部导数拓扑趋于U；故全局L²／平滑L²分母在对应ambient中稠密，**ambient商**非Hausdorff且Hausdorff化为0。不能据此推response-range限制商也非Hausdorff：χ_jV_r未必在V的像。

更早的完整配对反测来自405，甚至无需第三节。取其真实Gaussian \(h=E\eta_0\)，满足

\[
 c(h)=d(h)=1/4,\qquad B(h,h)=1/16.
\]

但 \([V_{e^{u/2}h}]=0\)。因此只用这个L²商就会消去整个I，并丢掉原来两个次数方向；完整B不可能仅经此裸类下降。这里B是405已经核过恒等元contact、无穷位、所有有限素数幂和双次数／双pole的完整配对，不能以polefree目标替换来避开该反测。

外加 \((d(f),c(f))\) 两坐标可以保留这项旧必要信息，但405(14)早已有 \(\mathbb C^2\times(\mathcal S_{\exp,\mathbb C}/I)\) 的实际Hausdorff卷积商；添加旧次数不产生新的principal、整截面或mixed RR。

本文只证 \(e^{u/2}I\subset\{r:V_r\in L^2\}\)，**未证等号**。一般非compact复源的该Laplace论证仅直接约束中心线和右侧jets，不给左侧全部条件或充分性。519已有更完整的全jets源信息。

## 5. strongest-old净后果与未排修复

短依赖链为：405原E及bare／physical约定 → 518(11)、(18)–(19)实际Möbius逆 → 519闭像及逆连续性 → 反射对数半密度恒等式(2)、(6)、精确norm(7)。这些已经是强旧付清的实际解析设施。第三节只另把compact Paley–Wiener／Jensen线性零密度、ζ的无条件 \(T\log T\) 计数和标准L²–Laplace边界界合用，排除给这个未加权原响应套有限L²能量。它是标准输入的直接可核组合，不是新的独立算术正性。

081／082已区分原始Möbius inverse、临界norm和finite Gram Schur距离。本文不付target alignment／Feshbach margin、Nyman–Beurling距离上界或520的忠实酉化／双向次指数增长，亦不把允许的中心线零点误叫RH反例。

本测试仅停止原响应的全局未加权L²全compact metric和裸mod L²承载完整B。截断／加权／renormalized能量、非local度量、付费强完成、relative／higher几何均未排，亦未证成功，不据此续参数。正D′逼近不被强加逐层有限Green能量。

Principal／正则单位真实边、非零primitive、整过滤／截面乘法／mixed RR、signed core／cross和成长Ξ仍欠；完整Γ/contact、proper powers及双pole不由逆ζ自动补出。Whole4/5负惯性UPPER保持，无关键瓶颈移除／Goal完成／新数学轮。

## 6. 本稿实际读取范围

全文读405、518–520；081的package／Gram／Mellin接口及082§§5–8。ζ计数和FE为标准输入，Jensen及L²门已自含写出。无外部query／新primary／PDF／下载／数值，未改manifest或其它文件；本稿待root消费。
