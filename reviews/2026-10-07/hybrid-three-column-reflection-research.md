# 实际三列的共同反射、natural Euler 零与 inverse-residue covariance

2026-10-07。新研究。**支付了 independent-height 三变量 completed identity、两个 plain 的 exact natural reflection、inverse 列的绝对收敛负线 dual series及其定量小界；把实际临界 mixed mean 归约为具体 inverse 零点残数和 horizontal joins 的加权 covariance。未支付新的 \(\gamma<1/3\) 或 \(\chi>0\)，没有新边界。** 这里没有要求两个 detector 的 Fourier heights 相同。

本轮从 main 502463775b1ba2a7d4aab65e1b55f3fbe775d7de 继续。仅新增本文件；旧论文、笔记、审查、脚本/output与外部 math 源只读，不修改 Goal/Git，没有派子 agent。

## 1. 固定输入与实际 infinity type

只读 source 为 E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex，固定 commit adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical LF SHA256：

~~~text
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
~~~

两个冻结接口的 canonical LF SHA256：

| 对象 | SHA256 |
| --- | --- |
| [whole \(ua^6\) transfer](hybrid-amplified-mixed-column-research.md) | 5f07dc2626ef0fa5ec20f0a56ab113b3ed55679ad066bb93174e1ee98d843752 |
| [actual critical mixed witnesses](hybrid-critical-neighborhood-mixed-witness-research.md) | ef85a5e5fd5aef3543aef6eb4b6adff6a1ecd39791575a89704e4b08e04e8983 |

本次重读的 source 前件：

- 705–726：\(M,S\) 的中央归一化、完整 common character与所有 masks。
- 1425–1453：primitive finite-order Hecke functional equation及 strip growth。
- 1602–1640：positive-half-plane deleted products及导数。
- 4221–4268：\(\Theta\)、primitive presentation、natural redundant radical与非 principal资格。
- 4390–4479、4510–4680：height预算、actual Gamma/truncated inverse profiles及各自 Fourier extraction。
- 12677–12773：原 natural plain reflection、\(C_kq_R\) bound、\(W^\sharp\)与全 geometric restoration。
- 1676–1723、1793–1845、7663–7795、7934–7967：generic cubic reflection的实际 source series、Gauss phases、dual masks和独立性。
- 11603–11742：marked inverse的 squarefree overlap initialization；其 squarefree/Gauss class不是任意 composite coefficient。
- 14997–15039：原 physical once-prime slots的准确系数及 bin upper bound。

实际 \(\psi(n)=\nu_{\rm ray}(n)\chi_n(v)^\varsigma\) 中，\(\nu_{\rm ray}\in\Theta\)是 finite-order ray character：4224–4242、9220和12511均明确这一点。1437证明有限阶在 \(\mathbb C^\times\) 的 infinity type trivial。因此本报告的 completed archimedean factor确为 \(\Gamma(s)\)。没有把实际 norm/height twist并入 \(\psi^*\)。

为防止同一符号的歧义，写实际 tests为
\[
 f_j(y)=V_j(y)y^{-\sigma_j-i\omega_j},\qquad
 \widehat f_j(s)=\int_0^\infty f_j(y)y^s\frac{dy}{y}.
 \tag{1}
\]
\(V_0\)保留 \(V_{\le}(Dy/D_*)\)；两个 \(V_j\)保留各自 annular/原 Gamma-derived profile。三条 \(\omega_j\)可以不同。尤其 long和short detector的 \(\nu_+,\nu_-\) 是这些 \(\omega_j=\gamma-\nu_j\)的来源，不是新的 Hecke infinity type。若另扩展到非有限阶/angular Hecke characters，下面 \(\Gamma(s)\)及 \(J_0\)公式必须重算；本报告没有作该扩展。

以下 fixed presentation均非 principal，写
\[
 L_\psi(s)=L(s,\psi^*)D_R(s),\quad
 D_R(s)=\prod_{p\mid R}(1-a_pq_p^{-s}),\quad
 a_p=\psi^*(p),\quad |a_p|=1,
\]
\[
 C=\frac{3Q_{\psi^*}}{(2\pi)^2},\qquad
 L(s,\psi^*)=\varepsilon_\psi C^{1/2-s}
 \frac{\Gamma(1-s)}{\Gamma(s)}L(1-s,\overline{\psi^*}).
 \tag{2}
\]
\(R\)只含 primitive conductor以外的 redundant natural zero primes。原 fixed exclusions和 \(ua^6\)新增的零都在 \(R\)或 primitive zeros 中，不能漏掉。

## 2. independent-coordinate共同 completed identity

令
\[
 {\cal F}_\psi(s_0,s_1,s_2)
 =\frac{L_\psi(s_1)L_\psi(s_2)}{L_\psi(s_0)}.
 \tag{3}
\]
原实际三列为
\[
 M_\psi(D;f_0)S_\psi(X_1;f_1)S_\psi(X_2;f_2)
 =\frac1{(2\pi i)^3}\int_{(c_0,c_1,c_2)}
 \prod_{j=0}^2\widehat f_j(s_j)\,
 D^{s_0-1/2}X_1^{s_1-1/2}X_2^{s_2-1/2}
 {\cal F}_\psi(\boldsymbol s)\,d\boldsymbol s ,
 \tag{4}
\]
其中 \(c_j>1\)。这是绝对收敛的实际三变量 Mellin representation；外面的原 \(Q_\psi\)不变。各 tests独立积分，没有对角化 heights。

逐列用(2)给精确 meromorphic identity
\[
\begin{split}
 {\cal F}_\psi(\boldsymbol s)
 ={}&\varepsilon_\psi C^{1/2+s_0-s_1-s_2}
 \frac{\Gamma(s_0)\Gamma(1-s_1)\Gamma(1-s_2)}
 {\Gamma(1-s_0)\Gamma(s_1)\Gamma(s_2)}\\
 &\times{\cal E}_R(\boldsymbol s)
 {\cal F}_{\bar\psi}(1-s_0,1-s_1,1-s_2),
 \tag{5}\\
 {\cal E}_R(\boldsymbol s)
 ={}&\frac{D_R(s_1)D_R(s_2)D_{\bar R}(1-s_0)}
 {D_R(s_0)D_{\bar R}(1-s_1)D_{\bar R}(1-s_2)} .
\end{split}
\]
这里 \(D_{\bar R}(s)=\prod_{p\mid R}(1-\bar a_pq_p^{-s})\)，\(\bar\psi\)指同一 full presentation的 conjugate。root number恰为 \(\varepsilon_\psi^{-1}\varepsilon_\psi^2=\varepsilon_\psi\)，不是三个独立 random phases。

若每个 \(\Re s_j\in[\sigma_0,1-\sigma_0]\)，\(\sigma_0>0\)固定，则六个 deleted factors均在 positive半平面。Source deleted-product lemma给
\[
 |\partial^{\boldsymbol\alpha}{\cal E}_R|
 \ll_{\boldsymbol\alpha,\sigma_0,\epsilon}q_R^\epsilon
 (1+\log q_R)^{|\boldsymbol\alpha|}.
 \tag{6}
\]
有限阶导数由逐个 logarithmic derivative或其高阶导数直接得到，所有 heights统一。这个界不延伸到 \(\Re s_0\le0\)的 reciprocal deleted factor；那里的 Euler poles必须另行处理。

仅作 primitive形式 substitution \(z_j=1-s_j\)，三个 central dual scales分别为
\[
 Y_0^{\rm prim}=\frac1{CD},\qquad
 Y_1^{\rm prim}=\frac C{X_1},\qquad
 Y_2^{\rm prim}=\frac C{X_2}.
 \tag{7}
\]
reciprocal是 \(1/(CD)\)，不是 \(C/D\)。但(5)本身不允许免费移动 \(s_0\)跨过 \(L_\psi\)的零点；(7)不是三个已准入 short polynomials。

## 3. 两条 plain 列的完整 natural反射与原 prime slots

Source 12733–12754可对两个独立 profiles分别应用，得到
\[
\begin{split}
 S_\psi(X_j;f_j)
 =\varepsilon_\psi
 \sum_{\substack{d_j\mid R\\h_j\mid R^\infty}}
 \frac{\mu(d_j)\psi^*(d_j)\overline{\psi^*(h_j)}}
 {\sqrt{q_{d_j}q_{h_j}}}\,
 S_{\bar\psi}\left(\frac{Cq_{d_j}}{X_jq_{h_j}};f_j^\sharp\right),
 \tag{8}\\
 \widehat f_j^\sharp(z)
 =\widehat f_j(1-z)\frac{\Gamma(z)}{\Gamma(1-z)} .
\end{split}
\]
两条 \(\omega_j\)独立传入各自 transform。它们不产生同 height断言。两个 coefficient sums合计 \(q_R^\epsilon\) mass；没有遗漏 \(h_j\)的 full geometric powers。

对于 \(v=ua^6\)，primitive character、conductor及 root number与 \(u\)相同。好 primes的 tame conductor至多一次，新增 redundant primes只来自 \(\operatorname{rad}a\)。由 source 4260–4263、12689–12698，
\[
 Cq_R\ll_{\mathcal A}q_{\operatorname{rad}u}q_{\operatorname{rad}a}
 \ll_{\mathcal A}UA,\qquad A=U^{(\eta-1)/6}.
 \tag{9}
\]
这比用 output row norm \(UA^6=U^\eta\)强。因此每个 retained plain dual main scale满足
\[
 Y_j=\frac{Cq_{d_j}}{X_jq_{h_j}}
 \ll \frac{UA}{X_j}.
 \tag{10}
\]
在 reference \(\eta\downarrow\ell\)、\(m=0.408593527\ldots\)，上端 exponent为
\[
 1+\frac{\ell-1}{6}-m=0.612111\ldots.
\]
这些可能超过 \(1/2\)。不能把它们自动记成更短于原 \(m\)的 plain factors。

原一次 slots保持
\[
 Q_{\psi,i}=P_i^{-1/2}\sum_{p\in{\cal P}_i}
 c_i(p)\psi(p)W_i(q_p/P_i),\qquad Q_\psi=\prod_iQ_{\psi,i}.
 \tag{11}
\]
在 exact complex product中不反射或复制这些 finite factors。两个 plain反射的共同 \(\varepsilon_\psi^2\)在每个 row的 absolute square中抵消；没有因此产生 mean saving。

在 norm上可以 whole-conjugate \(Q_\psi\)，改用 \(\bar\psi\)及全部 conjugate coefficients以调用 plain theorem；这保持 \(|Q_\psi|\)及 underlying lists。不能只 conjugate一部分 slots。这个合法 norm选择仍不把 M和两条 reflected plain同时变成一个原 canonical inverse class。

为明确 whole composite没有被拆后遗忘，令 \(\alpha_j(d_j,h_j)\)为(8)的 coefficient。结合下面(20)、(23)，整个原 once-slot complex column准确为
\[
\begin{split}
 M_\psi S_{\psi,1}S_{\psi,2}Q_\psi
 ={}&\varepsilon_\psi^2 Q_\psi
 \sum_{d_1,h_1,d_2,h_2}\alpha_1(d_1,h_1)\alpha_2(d_2,h_2)\\
 &\times S_{\bar\psi}(Y_1;f_1^\sharp)
 S_{\bar\psi}(Y_2;f_2^\sharp)
 \bigl(Z_\psi+I_{-,\psi}+E_{H,\psi}^{\rm vert}\bigr).
 \tag{11a}
\end{split}
\]
只有 \(I_-\)项合成 root phase \(\varepsilon_\psi\mu(R)\bar\psi^*(R)\sqrt{q_R}\)及(20)的实际 series；\(Z_\psi\)残数/joins仍在原 orientation，不能赋予三个 independent Gauss factors或删除。四个 restored ideal variables、两条 dual profiles、原 \(Q_\psi\)和所有 natural coefficients均留在同一式中。

尤其(8)的 \(\psi^*(d_j),\bar\psi^*(h_j)\)在 redundant primes上可以非零，原 \(\psi_v(d_j)\)却为零。不能把这些 outer primitive phases写成 natural \(\chi_{d_j}(v)\)并因此删除。逐 row coefficient mass \(q_R^\epsilon\)也不证明一个跨所有 rows和 current dual tuples的共同 separating measure；generic reflected-energy要求的独立性仍须另算。

## 4. inverse kernel的新 exact integral及不可删除的尾

定义 primitive reciprocal transform
\[
 \widehat f^\vee(z)=\widehat f(1-z)\frac{\Gamma(1-z)}{\Gamma(z)}.
 \tag{12}
\]
它有以下实际 integral representation：
\[
 f^\vee(y)=\frac1y\int_0^\infty
 f(t)J_0\!\left(\frac2{\sqrt{ty}}\right)\frac{dt}{t}.
 \tag{13}
\]
此处的常数2与 source \(C=3Q/(2\pi)^2\)一致，没有再次添加 \(2\pi\)。由 [DLMF 10.22.43](https://dlmf.nist.gov/10.22.E43) 的 Bessel Mellin integral，令 \(x=r^2/4\)，得到
\[
 \int_0^\infty J_0(2\sqrt x)x^{s-1}\,dx
 =\frac{\Gamma(s)}{\Gamma(1-s)}.
\]
先在一个绝对收敛 strip计算(13)，再由 compact support的 smooth Mellin continuation得到(12)。亦可直接把(12)在 \(\Re z<1\)逆 Mellin并移线验证。

对任意 fixed annular \(f\)，[DLMF 10.2.2](https://dlmf.nist.gov/10.2.E2)的 \(J_0\) power series给
\[
 f^\vee(y)
 =\sum_{k=0}^{K-1}
 \frac{(-1)^k\widehat f(-k)}{(k!)^2\,y^{k+1}}
 +O_{K,f}(y^{-K-1})\qquad(y\ge1).
 \tag{14}
\]
同一界适用于任意先固定数量的 Euler derivatives。特别
\[
 f^\vee(y)=\frac{\widehat f(0)}y+O_f(y^{-2}).
 \tag{15}
\]
在 \(y\downarrow0\)，compact smooth annulus上的 Bessel oscillation对 \(t\)非驻相；或把(12)的 inverse Mellin line任意左移，可得
\[
 (y\partial_y)^jf^\vee(y)
 \ll_{A,j,V,\sigma}(1+|\omega|)^{B_{A,j}}y^A.
 \tag{16}
\]
Stirling和 translated Mellin decay确保有限 \(B_{A,j}\)，在 fixed real ranges统一；不要求 \(\omega_1=\omega_2\)。

这里 \(\Gamma(1-z)\)的 poles在 \(z=1,2,\ldots\)。generic completed-reflection 1718–1720要求输入在零与无穷两端均任意 rapid；非零 compact \(f\)的 \(f^\vee\)不能满足无穷端要求。若所有(14)系数都为零，则 \(\int f(t)t^{-k}dt/t=0\)对所有 \(k\ge0\)。换元 \(x=1/t\)，compact interval上的 polynomial density迫 \(f=0\)。所以有限个 moment cancellation可以加快有限次衰减，不能使这个非零 reciprocal kernel自动进入 generic rapid class。

这不是仅凭 coefficient不合类来拒绝反射：它是实际 gamma quotient的可审尾项。

## 5. 保留 natural zeros的负线 reciprocal dual series

选固定 \(0<r<1\)，例如 \(r=1/20\)，同时处于 source strip-growth范围。移原 inverse contour到 \(\Re s=-r\)。下面只先计算该负线 integral，所有穿越的 poles及 joins随后显式列出。

natural Euler factors有准确 identity
\[
 D_R(s)=\mu(R)\psi^*(R)q_R^{-s}D_{\bar R}(-s).
 \tag{17}
\]
因此(2)给
\[
 \frac1{L_\psi(s)}
 =\varepsilon_\psi^{-1}\mu(R)\bar\psi^*(R)\,
 C^{s-1/2}q_R^s
 \frac{\Gamma(s)}{\Gamma(1-s)}
 \frac1{L(1-s,\bar\psi^*)D_{\bar R}(-s)}.
 \tag{18}
\]
这里的 \(D_{\bar R}(-s)\)在负线为 positive-real-part product，全部 new zeros有保留；不调用 \(\Re s<0\)的免费 reciprocal deleted bound。

设
\[
 a_0=\widehat f(0),\qquad
 f^+(y)=f^\vee(y)-\frac{a_0}{y},\qquad
 Y=\frac1{Cq_RD}.
 \tag{19}
\]
\(f^+\)在 \(1<\Re z<2\)的 Mellin transform正是 meromorphic continuation的(12)。证明是把 inverse Mellin line从 \(0<\Re z<1\)向右移到该 strip；唯一穿越的 \(z=1\) residue为 \(-a_0\)。原 \(s=-1\)及第二个尾项尚未穿越，因为 \(r<1\)。

负线 inverse integral于是**精确等于**
\[
\begin{split}
 I_{-,\psi}(D;f)
 :={}&\frac1{2\pi i}\int_{(-r)}
 \frac{\widehat f(s)D^{s-1/2}}{L_\psi(s)}\,ds\\
 ={}&\varepsilon_\psi^{-1}\mu(R)\bar\psi^*(R)\sqrt{q_R}\,
 {\cal M}_{R,\bar\psi^*}(Y;f^+),\\
 {\cal M}_{R,\bar\psi^*}(Y;f^+)
 ={}&Y^{-1/2}
 \sum_{\substack{n\\h\mid R^\infty}}
 \mu(n)\bar\psi^*(nh)q_h
 f^+\!\left(\frac{q_nq_h}{Y}\right).
 \tag{20}
\end{split}
\]
这不是 natural inverse polynomial。它包含 full \(h\)-powers，且真实 coefficient是 \(q_h\)，不是 \(q_h^{-1/2}\)。推导是在 \(\Re z=1+r\)展开
\[
 L(z,\bar\psi^*)^{-1}
 =\sum_n\mu(n)\bar\psi^*(n)q_n^{-z},\qquad
 D_{\bar R}(z-1)^{-1}
 =\sum_{h\mid R^\infty}\bar\psi^*(h)q_h^{1-z}.
\]
两式在该线绝对收敛。与 \(f^+\)的 Mellin integral交换后即(20)，归一化 \(\sqrt{q_R}\)从 \(q_R^s\)产生，不能漏掉。

尽管有 \(q_h\)，整个 dual series仍绝对可控。\(Y\le1\)时，(14)–(15)给
\[
\begin{split}
 |I_{-,\psi}(D;f)|
 &\ll_f\sqrt{q_R}\,Y^{3/2}
 \sum_nq_n^{-2}\sum_{h\mid R^\infty}q_h^{-1}\\
 &\ll_{\epsilon,f}
 C^{-3/2}D^{-3/2}q_R^{-1+\epsilon}.
 \tag{21}
\end{split}
\]
\(\sum_nq_n^{-2}<\infty\)，且 \(h\)-mass为 \(\prod_{p\mid R}(1-q_p^{-1})^{-1}\ll_\epsilon q_R^\epsilon\)。实际 \(f=V(y)y^{-\sigma-i\omega}\)在 fixed annulus的绝对值统一；故此 \(y\ge1\) bound不产生新的 exponential height loss。涉及 small-\(y\)和 derivatives的有限 polynomial height orders仍按(16)支付。

## 6. actual zeros、Euler pseudozeros与有限 height equality

不能从(21)得出 \(M_\psi(D)\)很小，因为 contour shift穿越的 poles正是其实际 spike渠道。

令 \(c>1\)固定，选 \(H>0\)，使 rectangle
\[
 {\cal R}_H=\{-r\le\Re s\le c,\,
                 \omega-H\le\Im s\le\omega+H\}
\]
的 boundary不含 \(L_\psi\)的零。写
\[
 {\cal P}_{H,\psi}(D;f)
 =\sum_{\zeta\in{\cal R}_H^\circ}
 \operatorname*{Res}_{s=\zeta}
 \frac{\widehat f(s)D^{s-1/2}}{L_\psi(s)}.
 \tag{22}
\]
这里 \(\zeta\)取全部 reciprocal poles及其实际 multiplicities。令 \(J_{H,\psi}\)为 minus \(1/(2\pi i)\)乘 rectangle两条 counterclockwise horizontal integrals，即 top从 \(c+i(\omega+H)\)到 \(-r+i(\omega+H)\)，bottom反向。Cauchy给
\[
 M_\psi(D;f)
 ={\cal P}_{H,\psi}(D;f)+J_{H,\psi}(D;f)
 +I_{-,\psi}(D;f)+E_{H,\psi}^{\rm vert}.
 \tag{23}
\]
\(E^{\rm vert}\)只是两条原/负 vertical tails差，不含任何隐藏 zero或 horizontal join。

simple primitive/nontrivial zero \(\rho\)的 summand为
\[
 \frac{\widehat f(\rho)D^{\rho-1/2}}{L_\psi'(\rho)}.
 \tag{24}
\]
对 actual long witness \(f_0(y)=V_0(y)y^{-\sigma-i(\gamma-\nu_+)}\)、选中零 \(\rho=\sigma+i\gamma\)，其 numerator恰为 \(\widehat V_0(i\nu_+)\)。没有原句迫这个数为零，也没有对 \(1/L_\psi'(\rho)\)的 uniform bound。multiple zeros须保留 higher residues，不假设 simplicity。

新增 natural \(a\)-zeros另外产生
\[
 1-a_pq_p^{-s}=0,\qquad
 \Re s=0,\quad
 \Im s=\frac{\arg a_p+2\pi k}{\log q_p}.
 \tag{25}
\]
这些是 \(L_{\rm orig}\)的 Euler zeros，不能与 primitive L zeros混淆或删掉。它们在 finite rectangle中按 multiplicity合计
\[
 O\bigl((1+H)\log(2q_R)\bigr).
\]
该数目界不是 residue大小界；多个 local zeros可能重合，包括 \(s=0\)与 primitive trivial zero。\(r<1\)没有跨原 \(s=-1\)。

原 absolute right line tails由 translated smooth Mellin decay直接支付。负线的(18)只含 \(\Re z=1+r\)的 absolute Euler functions及 gamma quotient；具体有
\[
 |L_\psi(-r+it)^{-1}|
 \ll_{r,\epsilon}C^{-1/2-r}q_R^{-r+\epsilon}
 (1+|t|)^{-1-2r}.
\]
这里用正线 Euler convergence、\(D_{\bar R}(r-it)^{-1}\ll q_R^\epsilon\)及固定 \(r\)的 Stirling，bounded \(t\)由 continuity支付。对(1)的 pure twist，Mellin尾导数只作用于 untwisted \(V\)，decay变量为 \(t-\omega\)，没有引入随 external \(N\)增大的 \((1+|\omega|)^N\)预算。两条 vertical tails因而由
\[
 \bigl(D^{c-1/2}
 +C^{-1/2-r}q_R^{-r+\epsilon}D^{-r-1/2}\bigr)
 p_{N+2}(V)H^{-N}
\]
控制。先固定所需 internal derivative/contour orders与 bounded length/amplifier ranges，再选 \(\tau>0\)，令 \(H\asymp T_1=U^\tau\)在已分配的 added-frequency allowance内，最后选择 external \(N\)，使
\[
 E^{\rm vert}=O(U^{-A})
 \tag{26}
\]
对任意预先指定有限 \(A\)成立。每条 \(\omega_j\)的 absolute center保留；反射只把相应 center翻为 \(-\omega_j\)，没有反复领取高度预算。可以对每个 row/profile在一个固定 positive-width \(H/T_1\) interval内选择无零 boundary；坏 \(H\)为离散集合。没有声称该选择随 row/profile光滑，更没有从“无零”推出 join bound。后面的误差对任意这些选择统一，不需要对 \(H\)求导。

horizontal integrals则含准确未付量
\[
 \sup_{\substack{-r\le\sigma\le c\\\pm}}
 |L_\psi(\sigma+i(\omega\pm H))^{-1}|.
 \tag{27}
\]
Source buffered rectangle只控制其原 zero-free右部，不控制跨过 actual row zeros后的整条 join。本报告保留 \(J_H\)，不宣称选无零 boundary便自动得到 uniform polynomial inverse bound，也不令(27)随 external tail order免费消失。这是 actual quantifier障碍，而非 kernel代数错误。

## 7. 临界 mixed mean的新 inverse-observable归约

定义由显式零点和 contours构成的 observer
\[
 Z_\psi(D;f)={\cal P}_{H,\psi}(D;f)+J_{H,\psi}(D;f).
 \tag{28}
\]
它不是按所需 mixed值定义的算子；(22)和指定 horizontal integrals给出其独立 analytic formula。(21)、(23)、(26)严格给
\[
 M_\psi(D;f)=Z_\psi(D;f)
 +O(C^{-3/2}D^{-3/2}q_R^{-1+\epsilon})+O(U^{-A}).
 \tag{29}
\]
取 whole amplification的结构 rows，数量 \(\ll U^\eta\)，其 primitive bin、\(\Theta\) exclusion、natural \(v\)-zeros固定，未按 live detector maximizers定义新 row class。对 actual bin中 profiles/高度，先支付原 finite-dimensional Sobolev orders与共同 allowance。写
\[
 B_v=S_{\psi_v}(U^m;f_1)S_{\psi_v}(U^m;f_2)Q_{\psi_v}.
\]
实际 pointwise upper bounds是
\[
 |M_v|^2\ll U^{\delta\ell+\epsilon},\qquad
 |B_v|^2\ll U^{2\delta m+\delta z+\epsilon}.
 \tag{30}
\]
这里 prime upper真正为 \(\delta/2\)每单位 slot长度，来自14997–15024的 \(a-1/2\)；不能在整个邻域免费改为较小 selected amplitude \(q\)。reference \(x=1/2\)才有 \(\delta z=2qz\)。

将(29)乘 \(B_v\)，用 Hilbert norm triangle/cross-term比较，有
\[
\begin{split}
 \sum_v|(M_v-Z_v)B_v|^2
 &\ll U^{\eta-3\ell+2\delta m+\delta z+\epsilon}+O(U^{-A}),\\
 \left|\sum_v|M_vB_v|^2-\sum_v|Z_vB_v|^2\right|
 &\ll U^{\eta-\frac32\ell+\frac12\delta\ell+
                         2\delta m+\delta z+\epsilon}+O(U^{-A}).
 \tag{31}
\end{split}
\]
只用 \(C\gg1,q_R\ge1\)的粗界；没有按 primitivity丢 natural poles。

在冻结451的 reference center，
\[
 E(\ell)-\delta\ell=\frac23,\quad
 2\delta m+\delta z=\frac13,\quad
 E(\ell)=\frac{1+5\ell}{6},\quad \ell=1.124227146\ldots.
\]
因此第二个 exponent在 \(\eta=\ell+a\)时精确为
\[
 a-\frac{\ell-1}{12}.
 \tag{32}
\]
先取 fixed \(0<a<(\ell-1)/24\)，再取 sufficiently small fixed critical neighborhood及全部 adjustable losses，(31)给
\[
 \sum_v|M_vS_{1,v}S_{2,v}Q_v|^2
 =\sum_v|Z_vS_{1,v}S_{2,v}Q_v|^2+o(1).
 \tag{33}
\]
这是真实 bin-wise quantitative reduction，不是 formal dual length猜测。它只在 stated critical neighborhood和 \(\eta\)范围作该强 \(o(1)\)结论；更广域仍有(31)。actual \(\kappa_{\rm act}\)与 all physical slot coefficients不变。

通过(33)，需要的新输入可以定位为 inverse zero-residue/horizontal observable在 plain+prime spike set上的能量去集中。举一个充分条件：固定结构 row family及 tests，设
\[
 {\cal E}_\chi=
 \{v:|B_v|^2>U^{1/3-\chi}\}.
 \tag{34}
\]
若 uniformly有
\[
 \sum_{v\in{\cal E}_\chi}|Z_v|^2
 \ll U^{\eta-\chi+\epsilon},
 \tag{35}
\]
并保留 \(\sum_v|Z_v|^2\ll U^{\eta+\epsilon}\)，则在 reference及相应小邻域，(30)给
\[
 \sum_v|Z_vB_v|^2\ll U^{\eta+1/3-\chi+O(\epsilon+\text{neighborhood})}.
 \tag{36}
\]
后者的 unweighted \(Z\) bound由已付 raw inverse moment及(29)得到。Whole transfer再给原 \(\chi\)目标。这是具体可测试的 restricted covariance条件，不是已经证明的 theorem；也没有声称它在逻辑上严格弱于所有 mixed raw estimates。每个 \({\cal E}_\chi\)来自固定 plain/slot tests，不得按原 target core重新选择 coefficients。

现有 plain fourth只控制 unweighted \({\cal E}_\chi\)个数；没有给(35)。在 reference \(\delta\ell=0.436855955\ldots>1/3\)，用 pointwise inverse upper补权反而损失 \(\delta\ell-1/3=0.103522622\ldots\)。有限数值 array可同时满足 inverse/ plain总能量 \(\le U^\eta\)和这些 pointwise caps，却在 \(U^{\eta-1/3}\) rows上令 \(|Z|^2=|B|^2=U^{1/3}\)，使 mixed为 \(U^{\eta+1/3}\)。这只说明现有 inequalities未支付去集中；它不是实际 sextic character的反例或方法不可能性。

## 8. exact covariance subtraction与 pole局部展开

共同 Mellin quotient另外有不依赖 heights的准确 decomposition：
\[
 {\cal F}_\psi
 =L_\psi(s_1)+L_\psi(s_2)-L_\psi(s_0)
 +\frac{[L_\psi(s_1)-L_\psi(s_0)]
        [L_\psi(s_2)-L_\psi(s_0)]}{L_\psi(s_0)}.
 \tag{37}
\]
若三个 actual annular scales足够大使 \(f_j(1/D_j)=0\)，将前三项代入(4)，每项至少两个 pure Mellin factors给 unit evaluations，故其 integral恰为零。实际 block因此等于最后这个 covariance integral；不是把 \(s_j=s_0\)强加到 profiles上。

在 simple零 \(\rho\)，令 \(s_j=\rho+\xi_j\)。其 reciprocal pole residue准确为
\[
 \frac{L_\psi(\rho+\xi_1)L_\psi(\rho+\xi_2)}{L_\psi'(\rho)}
 =\frac{\xi_1\xi_2}{L_\psi'(\rho)}
 \left(\int_0^1L_\psi'(\rho+t\xi_1)\,dt\right)
 \left(\int_0^1L_\psi'(\rho+t\xi_2)\,dt\right).
 \tag{38}
\]
这给局部 quadratic covariance zero，但 actual independent Mellin frequencies/real coordinates没有 \(\xi_1,\xi_2=O(U^{-c})\)前件，且 reciprocal \(L'\)无uniform下界。它提供未来 shifted-zero covariance机制的实际积分，不给当前 power saving。

good unramified prime的 exact local factor为
\[
 A_p(\boldsymbol s)
 =\frac{1-a_0}{(1-a_1)(1-a_2)},\quad
 a_j=\psi^*(p)q_p^{-s_j}.
\]
局部 subtraction也准确：
\[
 A_p-\frac1{1-a_1}-\frac1{1-a_2}+\frac1{1-a_0}
 =\frac{(a_1-a_0)(a_2-a_0)}
        {(1-a_0)(1-a_1)(1-a_2)}.
 \tag{39}
\]
取 \(a_j=a_0q_p^{-\xi_j}\)，leading covariance coefficient为
\(a_0^2(q_p^{-\xi_1}-1)(q_p^{-\xi_2}-1)\)。对 \(\Re s_j\ge1+\sigma\)、\(|\xi_j|\le h\)，其绝对值由
\[
 \ll_\sigma |a_0|^2|\xi_1\xi_2|(\log q_p)^2
 e^{(|\xi_1|+|\xi_2|)\log q_p}
\]
控制；只有 additional microscopic difference前件才可能形成小量，original extraction不提供它。

## 9. Gauss/CRT相位、signed列与generic low的准确接口

在好 prime上，任何 finite reflected tuple的 signed character exponent为
\[
 j_p=v_p(n)+v_p(P)-v_p(b_1)-v_p(b_2)\pmod6
 \tag{40}
\]
（这里取 exact complex product中的原 \(Q_\psi\) orientation）。whole-conjugate \(Q\)的 norm表示改为 minus \(v_p(P)\)，但不消灭其他分支。所有出现该 prime的 tuples都保留 \(1_{p\nmid v}\)，即使 \(j_p=0\)。

source additive character下的完整 local Fourier table可直接计算：
\[
 q_p^{-1}\sum_{x\bmod p}\chi_p(x)^j e(-ax/p)
 =
 \begin{cases}
 q_p^{-1/2}\tau_{p,j}^{-}\chi_p(a)^{-j},&j\ne0,\ a\ne0,\\
 0,&j\ne0,\ a=0,\\
 -q_p^{-1},&j=0,\ a\ne0,\\
 1-q_p^{-1},&j=0,\ a=0.
 \end{cases}
 \tag{41}
\]
非零 \(j\)的 \(|\tau_{p,j}^{-}|=1\)来自 source prime Gauss identities；\(j=0\)是 Ramanujan zero mask，不是 modulus-one Gauss factor。(41)由 \(y=ax\)换元或完整 additive orthogonality证明，所有 exponents的非单位值均先设为零。

对 coprime primitive conductor pieces \(f_1,f_2\)，同一 additive convention的 CRT Gauss product还保留
\(\psi_1(f_2)\psi_2(f_1)\) cross phases；它们不是独立 local random signs。Functional equation已经把它们合为同一 \(\varepsilon_\psi\)。\(ua^6\)新增 redundant primes不改变该 root number，只产生(17)、(25)、(41)的 zero-mask分支。

例如三条 columns及一次 slot中的 valuation都先取0或1，(40)即可出现 \(j=1,5,4,0\)等分支；full plain powers允许全部 residues。cancelled exponent prime仍在 zero radical。不能只保留 sixth-free signed index而删除其 zero-exponent support。deleted-coefficient外层还带(8)的 primitive phases，不能在 natural零上置零；这使跨 rows的共同 coefficients独立性比单个 root phase更强。

generic low的实际输入不是“有 Gauss phases即可”：1670–1716指定 completed cubic \(T=L_0D\)，\(\gamma_2(n)\bar\alpha(n)\)、squarefree \(n\)、whole \(b^3\)及其真实 cubic normalization；7934–7966在 exact marked-reflection后得到
\[
 \chi_{k_{\rm res}}(nb)^3\chi_P(n)^{-2}
 1_{(P,k_{\rm res})=1}1_{(P,b)=1},
 \tag{42}
\]
并证明 tuple coefficient与 row/dual variables分离。当前 primitive三列 reflection给(20)、(40)、(41)，没有导出(42)；而 reciprocal \(f^\vee\)的尾也不满足1718–1720的两端 rapid前件。以上两个差别都已计算其实际原因，没有仅引用“arbitrary \(\beta\)不可套”。

可以继续沿(33)、(35)、(38)研究 explicit zero-residue energy在 actual unequal-height plain/prime peaks上的去集中，或为 signed sextic tuples的全部(41)分支建立新的 joint energy。必须同时支付 primitive phases、natural Re0 poles、horizontal joins、真实 dual长度及一次 original slots。现有 generic low无需改字，但它还没有提供这些新 bounds。

## 10. 参数顺序与已付/未付范围

先固定有限 arithmetic datum/\(\Theta\)、critical neighborhood、\(0<a<(\ell-1)/24\)、amplifier \(\eta=\ell+a\)范围及 contours \(c,r\)；primitive infinity type此时已明确为0。固定所需 finite derivative、Sobolev、Mellin和 residue comparison orders，分配所有 actual heights及 separating coordinates的同一个 cumulative allowance；这些 orders不依赖 external \(N\)。再选 adjustable real/divisor losses及 \(\tau>0\)，之后选 external tail \(N\)支付(26)，最后取 height threshold。不能用 \(N\)消灭未有uniform bound的(27)。

已付：independent-coordinate completed identity与六个 natural correction factors；双plain full geometric反射及 \(UA/X_j\)真实上端；inverse \(J_0\) integral和全部 tail coefficients；negative-line dual series的精确相位、\(\sqrt{q_R}\)、\(q_h\)及绝对界；original primitive/natural zero residues与 joins保留；critical-neighborhood mixed mean的(33)定量归约；exact quotient/local covariance subtraction和 all-mod-six Gauss zero table。

未付：weighted inverse-residue/horizontal去集中(35)、actual \(\gamma<1/3\)或 \(\chi>0\)、signed composite的generic-energy扩展、全域 high continuation及新 boundary。source通用 Hecke/Gauss/smooth/marked/plain输入仍为明确 [R]；本报告没有重新认证 whole kernel。没有证明 RH、RR、Weil算术桥或比例改进。
