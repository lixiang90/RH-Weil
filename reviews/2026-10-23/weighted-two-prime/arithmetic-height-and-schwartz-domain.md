# 双 split 素数的算术衰减权、真实强完成与原域门

2026-10-23；独立分支 `/root/weighted_sunit_arithmetic_581`，独占原件，供 root 与 fresh 核查，不改 STATE／cadence。接 [580](../../../notes/580-kry-finite-schwartz-boundary-cocycle-and-level-alias-gap.md)。以下有实际 ideal-index 权、有全源注入、有原 du/Dlog 强完成费用；这些结果不构成 arithmetic principal 同构、Weil 正性或平方 RR 容量。

## 1. 冻结对象、来源与新门

固定 \(k=\mathbb Q(\sqrt{-7})\)、native Haar／Gaussian \(\phi_*\)，\(\nu=\|\phi_*\|^2\)。选 \(p=2,q=11\)。2 已在580核为 split；\(-7\equiv4\pmod {11}\)，故11也 split。二者的局部空间均为二维，原格 \(O_{k,p},O_{k,q}\) 自对偶、体积1；其他有限位不变，记其固定平方范数为 \(\mu\)。不读 Q 或未知零点选位、权、源或完成化。

唯一外部原件仍是 [Kudla–Rapoport–Yang1999作者版](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)：§1给 \(\lambda\) 与 standard section，§4给完整 Mellin 式，§5给 integral special-endomorphism cycles。本文的双位权与强完成为下列直接构造；不引用原件未证明的任意 Schwartz 算术推广。

物理源为全 complex \(r=e^{u/2}f\in S_{\exp}\)，原范数为 du 与 zero-extension Dlog。令

\[
 s(u)=\operatorname{sech}(u/2),\quad
 c_a(r)=\int r(u)s(u-a)du,\quad
 a_{jk}=2j\log2+2k\log11,\quad d_{jk}=2^j11^k.
 \tag{1}
\]

\(\|s\|_2=2\)，所以全线 \( |c_a(r)|\le2\|r\|_2\)。580无权 dense family 对实际源发散不排衰减权；本轮具体新门是：ideal-index 权能否给真正 Fourier／乘法闭的强完成、全源可见性及包括 origin/integral 的实际费用。完成后的正 Gram 不自动是 arithmetic height。

## 2. 权来自真实 fractional S-ideal 的两个指数

取真实 fractional ideal \(I_{jk}=d_{jk}O_k\)，\(J_{jk}=I_{jk}\cap O_k\)。两个有限指数都合法：

\[
 [O_k:J_{jk}]=2^{2j_+}11^{2k_+},\quad
 [I_{jk}:J_{jk}]=2^{2j_-}11^{2k_-}.
\]

因而相对于 native integral model 的 commensurability height 为

\[
 H_{jk}:=\sqrt{[O_k:J_{jk}][I_{jk}:J_{jk}]}
       =2^{|j|}11^{|k|}.
 \tag{2}
\]

这里 \(j_+=\max(j,0),j_-=\max(-j,0)\)。它同时记录原格与 fractional 格，不是仅取 covolume 比 \(d_{jk}^2\)：后者在 dense cancellation 方向不 proper。H 在 \((j,k)\mapsto(-j,-k)\) 下不变，与这两个 unramified 位的 lattice duality 相容。式(2)是实际有限群指数恒等式，不是尚未定义的 height norm。

对先固定 \(\sigma>0\) 取幅度权

\[
 w_{jk}=H_{jk}^{-\sigma}>0,\quad
 S_\alpha:=\sum_{j,k}H_{jk}^{-\alpha}
  ={1+2^{-\alpha}\over1-2^{-\alpha}}
   {1+11^{-\alpha}\over1-11^{-\alpha}}<\infty\quad(\alpha>0).
 \tag{3}
\]

H 的算术来源不唯一决定 \(\sigma\)，亦不声称它是经典 ζ 的 canonical 正极化。固定 \(\sigma\) 是可核预算／resolvent 型阻尼选择；它没有用未知谱。

## 3. 实际 Hilbert 源：全 du 支付并在全 S_exp 注入

在两个有限位取单位化球

\[
 e_{jk}=2^j11^k\mathbf1_{2^jO_{k,2}}\mathbf1_{11^kO_{k,11}}
 \quad(\text{其他有限腿固定}),\quad
 F_\sigma(r)=\sum_{j,k}w_{jk}c_{a_{jk}}(r)e_{jk}.
 \tag{4}
\]

其实际 Gram 除固定 \(\mu\) 外为

\[
 G_{(j,k),(l,m)}=2^{-|j-l|}11^{-|k-m|}.
\]

两个 Poisson symbol 的乘积给 Riesz 常数 \(5/18,18/5\)。保留全部 mixed 项后，

\[
 \|\phi_*\otimes F_\sigma(r)\|^2
 \le {72\over5}\nu\mu S_{2\sigma}\|r\|_{du}^2.
 \tag{5}
\]

故任意先固定 \(\sigma>0\) 都支付实际源 Hilbert 费用，Dlog 亦支付；没有把 ambient inverse norm 当实际源费用。Riesz 下界还保证系数的唯一性。

若 \(F_\sigma(r)=0\)，所有 \(c_{a_{jk}}(r)=0\)。因 \(\log2/\log11\notin\mathbb Q\)，\(\{a_{jk}\}\) 稠密；\(r*s\) 连续，故它恒零。Fourier 乘子 \(2\pi\operatorname{sech}\pi t\) 无实零，给 \(r=0\)。因此全 \(S_{\exp}\)，甚至全 \(L^2(du)\)，采样源注入。580单格的 \(R_A\) 盲源被这条真实非整格公式排除；此处不据此宣称 primitive 商也注入。

## 4. 原 Bruhat 域仍失守：任意非零全源都不能保原域

在两个有限位的球层 \(v_2(x_2)=n,v_{11}(x_{11})=m\) 上，\(F_\sigma(r)\) 的实际函数值为

\[
 F_{nm}=\sum_{j\le n,k\le m}2^j11^k w_{jk}c_{a_{jk}}(r).
 \tag{6}
\]

这对每个有限 n,m 绝对收敛：上界的正 level 有限，负 level 有额外 \(2^j11^k\) 几何衰减。双离散差分精确为

\[
 F_{nm}-F_{n-1,m}-F_{n,m-1}+F_{n-1,m-1}
   =2^n11^m w_{nm}c_{a_{nm}}(r).
 \tag{7}
\]

若(4)属于原 Bruhat–Schwartz 域，统一局部常值性给某 N：在 \(x_2\in2^NO_{k,2}\) 内改变 \(x_2\) 不影响函数，且对全部 \(x_{11}\) 同时成立。因此(7)在所有 \(n>N,m\in\mathbb Z\) 为零。权始终正，故这些半平面样点全部 c=0；集合 \(\{n\ell_2+m\ell_{11}:n>N,m\in\mathbb Z\}\) 已稠密，于是 r=0。

结论是：**对每个非零 r，所有 \(\sigma>0\) 的这条 weighted 球族都不属于原 Bruhat 域。** 这是指定双位源的精确原域门，强于单格仅对 compact 源的结论；不排不同基、额外关系、源适应域或下节实际强完成。衰减再快也不能把全部非零系数变成最终局部常值。

## 5. 真强完成：Fourier、乘法、卷积及两个边界都可付

可直接定义一个具有实际函数身份的有限位径向 Banach 空间，而非把 L² 重命名 Schwartz。对 \(\beta\ge1\)，令

\[
 A_\beta=\left\{\sum a_{jk}e_{jk}:\quad
       \|a\|_{A_\beta}=\sum|a_{jk}|H_{jk}^{\beta}<\infty\right\}.
 \tag{8}
\]

Riesz 唯一性使它是实际函数空间；且 \(\|e_{jk}\|_\infty=d_{jk}\le H_{jk}\)、\(\|e_{jk}\|_1=d_{jk}^{-1}\le H_{jk}\)。所以(8)连续进入这两个位的 C₀∩L¹∩L²，origin 评价和两位全积分均连续。其他固定腿只贡献固定 Haar 常数；不声称ramified7的原格也被 full finite Fourier固定。这里及下文的 Fourier 是2、11这两个自对偶局部位的 partial Fourier，其他 finite 腿固定；它将 \(e_{jk}\) 精确送到 \(e_{-j,-k}\)，故对称 H 使其成为 \(A_\beta\) 的等距对合。

局部一位乘法为 \(e_j e_l=p^{\min(j,l)}e_{\max(j,l)}\)。分正负号直接验证

\[
 p^{\min(j,l)}p^{\beta|\max(j,l)|}
       \le p^{\beta|j|}p^{\beta|l|}\qquad(\beta\ge1).
\]

两位相乘给 \(\|FG\|_{A_\beta}\le\|F\|_{A_\beta}\|G\|_{A_\beta}\)。Fourier 对合再给卷积闭性及同一费用。有限 level 平移也连续：其费用由固定平移的 H 次幂支付。这是独立构造的强完成、实际乘法和实际双边界，不用 Q，也不止正 Hilbert Gram。

当 \(\sigma>\beta\ge1\)，实际源有

\[
 \|F_\sigma(r)\|_{A_\beta}
       \le2 S_{\sigma-\beta}\|r\|_{du}.
 \tag{9}
\]

该费用保原 du/Dlog、全源注入和全部 mixed 乘法连续性。还有实际的 fixed-g λ 读出：在一个选定位，\(g=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\) 若 c=0，Weil 公式的 origin 读出为常数倍 \(e_j(0)\)；若 c≠0，则为常数倍 \(\int e_j(x)\psi(Q_g(x))dx\)。两者分别由 \(\|e_j\|_\infty\)、\(\|e_j\|_1\) 控制，所以 \(|\lambda e_{jk}(g_2,g_{11})|\le C_{g_2,g_{11}}H_{jk}\)。因此每个先固定 local g 的真实 λ 评价在 Aβ 连续，且由(9)支付原 du 费。该常数依赖 g；没有把它外推成整个 adelic g／Eisenstein求和的统一控制。

它没有恢复原 Bruhat 域；也没有证明 full local Weil group、所有 restriction／DGA differential、Eisenstein functional 或 arithmetic Green／cycle／regulator 在此新域连续。特别是 unipotent chirp 一般离开这个径向球基，不能从 Fourier＋dilation 断言 full Weil 稳定。真正相对边界须逐条核扩张，不能因(8)是 Banach 代数就免费运输。

## 6. Origin／integral 的 sharp 实际源费用阈值为 σ>1

记

\[
 B_{\sigma,p}=1+{p^{1-\sigma}\over1-p^{1-\sigma}}
                    +{p^{-1-\sigma}\over1-p^{-1-\sigma}}
       \quad(\sigma>1).
\]

因为 \(\sum w_{jk}d_{jk}=B_{\sigma,2}B_{\sigma,11}\)，并且反演后相同，

\[
 |F_\sigma(r)(0)|+\left|\int F_\sigma(r)\right|
       \le4B_{\sigma,2}B_{\sigma,11}\|r\|_{du}.
 \tag{10}
\]

式(10)按这两个位的 Haar 写出；若把其他固定腿一并积分，右侧乘其已固定体积。origin 是原 λ 的 identity 读出 \(\lambda\varphi(1)=\varphi(0)\) 与其 Fourier 对偶读出，不是任意选择的抽象边界。σ>1 支付二者的实际全线源费用；对固定 σ 可取 \(1\le\beta<\sigma\) 与(9)相容。

反向不是粗上界。对 \(0<\sigma\le1\) 取固定非负 \(\psi\in C_c^\infty\)、非零，令

\[
 r_T=(D^2-\tfrac14)\psi(\cdot-T).
\]

它有双 pole 矩0，du 和全线 Dlog 范数均与 T 无关。分部积分保全部 terms 给

\[
 F_\sigma(r_T)(0)=-\tfrac12\sum_{j,k}w_{jk}d_{jk}
          \int\psi(u-T)s^3(u-a_{jk})du.             \tag{11}
\]

所有项同为负，故没有 mixed cancellation 漏项。对每个 \(0\le j\le T/(2\ell_2)\)，取 \(k=\lceil(T-j\ell_2)/\ell_{11}\rceil\ge0\)；有 \(\asymp T\) 个不同正象限点落在 \([T,T+\ell_{11}]\)。在这些点上 \(w d=e^{(1-\sigma)a/2}\)，积分有固定正下界。因此

\[
 |F_\sigma(r_T)(0)|\gtrsim T e^{(1-\sigma)T/2}\to\infty.
 \tag{12}
\]

integral 由 \((j,k,u,T)\mapsto(-j,-k,-u,-T)\) 给相同反测。这是先固定真实 compact 双 pole-zero 源形状后平移的实际费用，非 ambient operator norm 冒充源费。它区分 fixed window 与全线：每个先固定窗／源费用仍有限；没有成长窗统一费。全 \(S_{\exp}\) 源凭 \(|c_a(r)|\le2M_r e^{-|a|/2}\)，\(M_r=\max\int |r|e^{\pm u/2}du\)，使(11)的读出对每个 r、每个 σ>0 都有绝对意义；这不支付全线原 du 统一控制。

## 7. 完整 KRY 解析像与实际有限 quasi-cycle 身份

取 \(d=2^j11^k>0\)，有限 adelic \(t_d\) 在2、11位为 \(m(d^{-1})\)，其余为1。两个位都 split，Weil 公式给

\[
 \omega(t_d)\psi_0=d\psi_{jk}=e_{jk}.
\]

bare 球的 right-transported family 必须定义为

\[
 \Phi^{tr}_{\psi_{jk}}(g,s)=d^{-1}\Phi_0(gt_d,s).
 \tag{13}
\]

它在 s0 等于 \(\lambda\psi_{jk}\)。由 rational \(m(d^{-1})\) 的左不变性，

\[
 E^{*,tr}_{\psi_{jk}}(g_\tau,s)
       =d^{-1}E^*_0(g_{d^2\tau},s).
\]

注意 \(v^{-1/2}d^{-1}=(d^2v)^{-1/2}\)，所以 classical 导数为 \(\phi_0(d^2\tau)\)；normalized \(e_{jk}\) 的导数为 \(d\phi_0(d^2\tau)\)。这是任意正负 j,k 的实际 analytic identity，不把 standard extension 与 right transport 的导数误认相同。

finite 截断的 constant、负指标 β₁、所有正系数同时保留，完整去 constant Mellin 为

\[
 \mathscr M_{\sigma,N}(z;r)=B_{\sigma,N}(z;r)\mathscr M_0(z),\quad
 B_{\sigma,N}=\sum_{|j|,|k|\le N}w_{jk}c_{a_{jk}}(r)d_{jk}^{1-2z},
 \tag{14}
\]

\[
 \mathscr M_0=\Lambda_0\Lambda_\chi
      (\log7+\Lambda'_\chi/\Lambda_\chi-\Lambda'_0/\Lambda_0).
\]

完整 Γ／全部 prime powers／原极点及 constant FP 规范都在继承的 \(\mathscr M_0\) 中；没有以未定 B 重定义完成化。这里 \(B_{\sigma,N}\) 的每项由 source／格／权实际给出，仍是 signed/source-dependent，不能把它当成 positive inverse。

当 \(|1-2\Re z|<\sigma\) 时，(14)的极限 B 在紧子带正常收敛，且有原 du 一致上界。特别 σ>1 覆盖闭带 \(0\le\Re z\le1\)。每个 \(r\in S_{\exp}\) 的上述真实 c 尾把 normal convergence 拓到

\[
             -\sigma/2<\Re z<1+\sigma/2,           \tag{15}
\]

但扩大的费用用 \(M_r\)，不伪报全线 du。这里先在真正的绝对 Mellin 区间 \(1<\Re z<1+\sigma/2\) 核函数身份：native 去 constant 函数 G(v) 的全部正／负指标在 imaginary axis 非负，且 \(\int_0^\infty G(v)v^{x-1}dv<\infty\) 对 x>1；换元后全部项的绝对积分恰有额外因子 \(\sum|wc|d^{1-2x}\)。所以可先逐项绝对积分，得到实际加权去 constant 函数的 Mellin 为 Bℳ₀；随后才把该已识别函数作继承的亚纯延拓到(15)。不是声称 ℳ₀ 的原始积分在整个(15)收敛，也不是仅形式级数。若只用原 du 统一费，则初始绝对区间缩为 \(1<x<(1+\sigma)/2\)，故这里须 σ>1。

在 \(z=1/2+it\)，B 是有限复原子测度 \(\sum w_{jk}c_{a_{jk}}\delta_{a_{jk}}\) 的 Fourier 变换。若完整解析输出恒零，ℳ₀不恒零给 B恒零；有限测度 Fourier 唯一性及各 a 不同给所有 c=0，再给 r=0。因此这条**完整解析 KRY 像**也全源可见。不能据此断言其 primitive image、某一固定 Fourier 系数或实际相对 cycle 商全源可见。

对先固定 finite j,k，可直接在同一 CM stack 定义准循环：对象 \((E,\iota,z)\)，z integral special endomorphism，\(Q(z)=n/d^2\)，标记 \(y=dz\in\operatorname{End}(E)\otimes\mathbb Z[1/22]\)。当 \(n/d^2\) 非正整数时为空，否则这就是实际已知 \(\mathbf Z(n/d^2)\) 的原模态问题；没有制造新的 scheme thickness。positive levels 还具有580的 étale 可除性身份，negative levels 的 y 为 quasi-endomorphism。其指数 n 可为 rational；q-expansion 的 cusp width 随 finite family 变，**没有共同 fixed-level automorphy**。finite complex 线性组合合法不证明无限 weighted cycle／Green 的强收敛、integral lattice 或 principal 同构；不调用 general Schwartz-cycle theorem。

若坚持 standard extension，必须保留

\[
 \delta_{jk}(g)=\lambda\psi_{jk}(g)
       \log {|a(g)|\over|a(gt_d)|}                 \tag{16}
\]

的完整导数／constant 修正。log 因子由 \(h_{jk}=\log H_{jk}\) 控制；衰减可支付诸如 \(\sum H^{-\alpha}(1+h)^m\) 的固定 m 预算。它不自动证明 Eisenstein／arithmetic boundary 在新 \(A_\beta\) 域上的延拓。本文通过明确选择(13)保留全式，未删掉(16)来换正号。

## 8. 405、537、控制例及尚欠容量

405实际 \(P=(D^2-1/4)H\)、H>0 及全部平移仍满足

\[
 c_{a_{jk}}(\tau_bP)=-\tfrac12\int H(v)s^3(v+b-a_{jk})dv<0.
\]

权始终正，Fσ和完整解析 B 都保留该关系的非零像。所以它们不是 arithmetic principal 商；(11)的 origin 同号更排除“衰减后它自然成为边界零”的说法。真正协同边界可以读取额外原源，但须实给相对链与 homotopy。若把 Pan 像按定义作 boundary，仍是旧 quotient 包装；553旧有全线 bounded-Pan 消灭障碍也不因强完成自动消失。

537的每个非零 compact 原源被 Fσ 看见，原 du/Dlog 费由(5)/(9)支付；这是实际 coverage 改善。没有在 Fσ 的 positive norm 与完整 Qζ 之间付同对象二次等式，因此不能将该正 norm 用作537之外的新正性。连续 d=±1/16 对照对同一源、同样权／Gram 给不同 Weil 符号，故新 Banach／Hilbert 设施本身不能识别分布敏感的有符号型；无 continuous→CM 运输，不称其为 KRY 反例。

函数域的 degree-zero primitive Frobenius 对应在同一 \(C\times C\) 上有真实 mixed 交数、截面乘法与 RR/Hodge 来源；这里的乘法虽真实连续，仍仅是有限位函数乘法，不是那些 arithmetic sections 的乘法，也未产生 squared RR 容量。完整原Γ／全部 powers／双 pole 的解析继承不支付 signed 解卷积、local-vanishing filtration 或 height 正极化。finite/strong-topology、fixed-window/full-line/growth、源注入/primitive可见性严格分开。

本分支新增：实际 ideal-index 权，Fourier/乘法/卷积与双边界可付的具体强完成，du/Dlog 的 sharp σ=1 阈值，全部非零源的原 Bruhat 门，及具有全源注入的完整解析 Mellin 像。它没有给出 Weil/RH 新正号、同对象 primitive 容量或 whole4/5 负惯性 UPPER 以外新后果。
