# KRY 实际源接入：正实 dilation 的 Schwartz 映射与关系门

2026-10-23；独占分支，供 root 消费。没有更改 STATE、cadence 或合同。输入为405、537、552–553及上轮KRY原件门；下列直接计算不借未知零点、Q值或零点作标签。

## 1. 原件支持哪一个实际入口

唯一外部原件为[Kudla–Rapoport–Yang 1999](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)，§1 (1.4)给实际局部Weil表示在0评价的线性映射

\[
 \lambda_{\mathcal C}(\varphi)(g)=(\omega(g)\varphi)(0)\in I(0,\chi).
\]

固定q=7，有限Schwartz函数保持\(1_{\widehat{O_k}}\)。§2采用正定无穷位及Gaussian；§1允许一般Schwartz section。Theorem3的固定循环degree身份不能据此自动推广为一般Schwartz输入的primitive循环自交。§6对一般情形的修改是建议，不能当成已经付款的全Schwartz算术theta定理。

下文分清三个对象：实际Schwartz向量、其诱导表示section、尚待构造的relative primitive算术循环。前两者存在不等于第三者已有。

## 2. 全源的明确非标签映射

### 2.1 与原件native最低weight向量对齐

为进入原件固定weight1输入，实际候选应优先采用KRY Lemma2.1确定的最低weight1 Gaussian向量\(\varphi_*\)，保留原件的共同additive character、quadratic form和self-dual Haar。令\(D_u=\omega_\infty(m(e^{u/2}))\)，并定义

\[
 T_*r=\int_{\mathbb R}r(u)D_u\varphi_*\,du,
 \qquad \nu=\|\varphi_*\|^2_{L^2(d\mu_*)}>0.            \tag{A0}
\]

这是实际native向量的unitary伸缩轨道，不是调Haar或Gaussian宽度来选新Γ规范。\(\nu\)由这个固定输入决定，不自由归一化成1。Gaussian积分在原件共同坐标中给

\[
 \langle D_u\varphi_*,D_v\varphi_*\rangle
   =\nu\operatorname{sech}((u-v)/2),\qquad
 \|T_*r\|^2=\frac1{2\pi}\int
   2\pi\nu\operatorname{sech}(\pi t)|\widehat r(t)|^2dt. \tag{A0a}
\]

最低radial K线投影准确为

\[
 P_1T_*r=c(r)\varphi_*,\qquad
 c(r)=\int r(u)\operatorname{sech}(u/2)du.              \tag{A0b}
\]

因此\(\|T_*r\|^2\le2\pi\nu\|r\|_{du}^2\)，且处处严格正的乘子保证注入。405全部平移的非零性、radial \(\lambda_{\mathcal C}\)注入性、537非根及(A10)–(A11)的主关系反测全部对齐成立；(A11)在本native选择取c=0即可。双pole矩到原点值/积分仍分别乘原件确定的非零常数，不改变消失条件。

下列(A1)是\(d\mu_*=dx\)、\(\varphi_*(x)=e^{-\pi|x|^2}\)的明确模型，此时\(\nu=1/2\)，(A0a)恢复乘子\(\pi\operatorname{sech}(\pi t)\)。不声称这个模型数值无条件就是KRY所有印刷坐标的native Haar；实际CM输入按(A0)对齐。后面的不同Gaussian宽度投影(A9)保留为raw模型的对照公式，不再承担native固定weight的规范选择。

### 2.2 明确Euclidean模型及全源合法性

先固定\(\mathbb C\simeq\mathbb R^2\)的Lebesgue测度dx及Euclidean坐标。令

\[
 g_u(x)=e^{u/2}\exp(-\pi e^u|x|^2),\qquad
 (Tr)(x)=\int_{\mathbb R}r(u)g_u(x)\,du.                 \tag{A1}
\]

在二维Weil表示中，正实\(a\)的作用是\(\omega(m(a))\varphi(x)=a\varphi(ax)\)，因为\(\chi_\infty(a)=1\)。所以(A1)是\(\omega(m(e^{u/2}))g_0\)的真实Bochner积分；无额外算术参数，也没有读取Q或零点。

若采用另一个共同Gaussian宽度\(\alpha>0\)，将指数改为\(-\pi\alpha e^u|x|^2\)即可。相应Haar常数与Gaussian宽度应显式保留；它们不是允许自由选择的完成化B因子。下面所有原范数常数均注明为(A1)的dx规范。

令\(q_{\beta,\nu}(\phi)=\sup_x|x^\beta\partial^\nu\phi(x)|\)。微分和缩放给

\[
 q_{\beta,\nu}(Tr)
 \le C_{\beta,\nu}\int_{\mathbb R}|r(u)|
       e^{(1+|\nu|-|\beta|)u/2}\,du.                    \tag{A2}
\]

于是\(T:\mathcal S_{\exp}(\mathbb R;\mathbb C)\to\mathcal S(\mathbb R^2)\)是连续复线性映射，积分在每个Schwartz半范数中绝对收敛。在\(\operatorname{supp}r\subset[-L,L]\)上，右侧至多

\[
 C_{\beta,\nu}\sqrt{2L}\,
 e^{|1+|\nu|-|\beta||L/2}\|r\|_{du}.                    \tag{A3}
\]

这里是fixed窗到Schwartz半范数的费用，不是成长窗统一有界结论。

两个物理pole矩有直接的、尚不含primitive几何的解释：

\[
 Tr(0)=\int e^{u/2}r(u)du,\qquad
 \int_{\mathbb R^2}Tr(x)dx=\int e^{-u/2}r(u)du.         \tag{A4}
\]

因此双pole-zero源恰使Schwartz值和积分均为零。405的完整主关系远强于这两个矩；(A4)没有付清它。

## 3. 真实原du／Dlog费用及其精确缺口

二维Gaussian积分给

\[
 \langle g_u,g_v\rangle_{L^2(dx)}
 =\frac{e^{(u+v)/2}}{e^u+e^v}
 =\frac1{2\cosh((u-v)/2)}=:K(u-v).                     \tag{A5}
\]

用\(\widehat r(t)=\int r(u)e^{-itu}du\)及
\(\widehat K(t)=\pi/\cosh(\pi t)\)，得到对全部\(r\in L^2(du)\)

\[
 \|Tr\|_{L^2(dx)}^2
 =\frac1{2\pi}\int_{\mathbb R}
    \frac{\pi}{\cosh(\pi t)}|\widehat r(t)|^2dt
 \le\pi\|r\|_{du}^2.                                  \tag{A6}
\]

初始在紧支光滑源上Fubini/Plancherel，随后由有界性延到L²；这与(A2)的Schwartz定义一致。乘子处处严格正，故T注入。全部复mixed项亦由(A5)极化给出。若\(D_{\log}\)用原zero-extension的\(\log(2+|t|)\)权，(A6)当然给其到L²(dx)的上界，未引入导数或替代原费用。

反向费用没有统一付款。对固定非零\(\eta\in C_c^\infty((-L,L))\)，令\(r_n(u)=\eta(u)e^{inu}\)。则原du范数不变，(A6)及dominated convergence给\(\|Tr_n\|_2\to0\)；而Dlog范数平方为\((\log n+o(\log n))\|\eta\|_2^2\)。若要强制双pole-zero，可按552用两个固定dual模板消掉两矩，修正为任意阶\(O(n^{-A})\)，结论不变。

仅在全线Fourier频带\(|t|\le B\)上有

\[
 \|r\|_{du}^2\le\frac{\cosh(\pi B)}\pi\|Tr\|_2^2,       \tag{A7}
\]

不能把这个指数B费用当成紧支全源或成长尺度的已付费用。非零源不可能同时严格紧支和严格频带。

(A6)也不支付section全部点值：\(Tr(0)\)在全线du或Dlog平移下不有界；(A4)及\(r_a(u)=r(u-a)\)使它乘\(e^{a/2}\)，而源norm不变。fixed窗才有\(|Tr(0)|\le\sqrt{2\sinh L}\|r\|_2\)。双pole-zero使这一个值为零，却不自动支付所有section/Green/height半范数。

在双pole-zero子空间也有实际section费用反测。在本文坐标取

\[
 F_b(r)=\int_{\mathbb R^2}Tr(x)e^{2\pi ib|x|^2}dx
       =\int r(u)\frac{e^{u/2}}{e^u-2ib}du.             \tag{A6a}
\]

若\(0\ne r\in C_c^\infty\)且两个pole矩为零，径向Fourier唯一性给某个\(b_0\ne0\)使\(F_{b_0}(r)\ne0\)。直接换元给

\[
 F_{e^a b_0}(\tau_a r)=e^{-a/2}F_{b_0}(r).             \tag{A6b}
\]

令\(a\to-\infty\)，全部源仍双pole-zero、原du和Dlog不变，而\(b=e^a b_0\to0\)处的读出无界。Weil非零常数和共同坐标缩放不改变此结论。因此在含\(wn(0)=w\)的固定compact上，section的sup费用也没有全线原norm统一上界；这是实际源费用，而不是拿全空间算子norm冒充个别源的必要费用。每先fixed源或fixed窗的Fréchet费用仍合法。

一般Gaussian宽度α与测度\(c\,dx\)将(A5)–(A7)的乘子整体乘\(c/\alpha\)。不能混用KRY self-dual measure与这里dx后，仍声称数字π不变。

## 4. 405全主关系与537非根：已经能作实际判定

令405的\(h=E\eta>0\)，物理\(H_0=e^{u/2}h(u)>0\)，
\(p=(D^2-1/4)H_0\ne0\)。这是明确的noncompact物理Pan，属于\(\mathcal S_{\exp}\)，并保其全部平移。由(A6)，

\[
 \|T(\tau_a p)\|_2^2=\|Tp\|_2^2>0\quad(a\in\mathbb R). \tag{A8}
\]

所以这个正Hilbert能量没有把405主关系送成根；两个零矩并不能修复(A8)。相反，对537窗任取非零\(0\le\eta\in C_c^\infty((-17/16,17/16))\)，令\(r_*=(D^2-1/4)\eta\)。双pole矩为零，537保证\(Q_W(r_*)>0\)，注入性保证\(Tr_*\ne0\)。因此本候选确实保一个非根，但也保全部Pan；它尚不通过关系/非根联合门。

\(\lambda_{\mathcal C}\)不会在此radial像上自动制造所需kernel。在有限g取identity，只需考察\(g_\infty=wn(b)\)。按实际Weil公式，\(\lambda_\infty(\phi)(wn(b))\)是\(\phi(x)\psi_\infty(bQ(x))\)的积分乘一个非零Weil常数。对radial Schwartz \(\phi(x)=F(|x|^2)\)，它是半轴函数F的一维Fourier变换，带固定非零测度/坐标缩放。若全部b的评价为零，Fourier唯一性迫使F=0。所以\(\lambda_{\mathcal C}T\)在此像上仍注入，不能消掉(A8)。这是section向量层的结论，不是断言所有这些向量的未来算术cycle类均非主。

## 5. 固定weight入口与一般Schwartz入口不能互换

正实dilation通常不保固定K∞类型。原1999固定weight循环恒等式不能直接给(A1)的任意混合K类型算术解释。可进一步实际检查投回最低radial K类型，而不是只声称“投影可能有帮助”。

对本candidate可作更强的精确判定。radial L²的酉坐标
\(J\phi(v)=\sqrt\pi e^{v/2}\phi(e^{v/2})\)给

\[
 JTr(v)=\int r(u)G(v+u)du,\quad
 G(v)=\sqrt\pi e^{v/2}e^{-\pi e^v},\quad
 \widehat G(t)=\pi^{it}\Gamma(1/2-it)\ne0.              \tag{A8a}
\]

若\(Tr=cG_{\alpha_0}\)，则\(\widehat r(-t)=c\alpha_0^{-1/2}\alpha_0^{it}\)。右侧除非c=0，否则不属于L²；注入性再给r=0。故没有非零L²物理源能使(A1)恰落在某个Gaussian最低K线；单dilation的Gaussian是delta源而非原L²源。一般Schwartz section入口真实，但不能偷换成原固定weight degree身份。

在vacuum为\(G_{\alpha_0}(x)=e^{-\pi\alpha_0|x|^2}\)的共同oscillator规范中，最低radial K线是\(\mathbb CG_{\alpha_0}\)。其正交投影系数为

\[
 \frac{\langle g_u,G_{\alpha_0}\rangle}{\|G_{\alpha_0}\|^2}
 =\frac{2\alpha_0 e^{u/2}}{e^u+\alpha_0}
 =\sqrt{\alpha_0}\,\operatorname{sech}
         \frac{u-\log\alpha_0}{2}.                     \tag{A9}
\]

当(A1)宽度正是vacuum宽度、二者共同重标坐标时，系数即\(\operatorname{sech}(u/2)\)。若坚持paper印刷Gaussian、quadratic/bilinear form及self-dual坐标，必须先核其共同宽度；本文不以OCR的一处π/2π差异认证数字\(\alpha_0=1\)。结论对每个固定\(\alpha_0>0\)一致。

写\(k_c(u)=\operatorname{sech}((u-c)/2)\)。直接求导

\[
 (D^2-1/4)k_c=-\tfrac12k_c^3.                          \tag{A10}
\]

故405全部平移都满足

\[
 \int(\tau_a p)(u)k_c(u)du
 =-\tfrac12\int H_0(v)k_c(v+a)^3dv<0.                  \tag{A11}
\]

同理\(\int r_*k_c<0\)。投回该固定weight线于是仍不消Pan，同时可保537；它只把全源压成一个已知线性functional，不能取得全Weil mixed容量。该functional的全线du费用有限，因为\(\|k_c\|_2=2\)，但有限费用不修关系错误。选择任意其他固定Gaussian宽度亦受(A11)限制。

## 6. 容量和对照的责任分层

上述T是同一个、不依赖g-system的正Schwartz/Hilbert构造。562/578连续正负系统均可输入相同非零r，所得(A6)一律严格正。因此(A6)本身不可能区分它们的native Weil符号。若主张某个cycle容量等于完整Weil型，必须在连续负例上指出哪个额外独立几何/过滤假设不成立；不能给负例外加CM结构而称已检验通过，也不能据此反驳KRY算术定理。

真函数域中，一个源到Frobenius对应组合的map之所以有用，在于同一C×C上的双degree primitive投影、主除子关系、mixed交数及RR/Hodge负号同时闭合。T的radial L²能量没有这些设施；将其全源正号与函数域的RR正号并列，不构成同对象比较。全returns/aliases与H⁰/H²极点没有因(A1)而消失。

完整经典目标仍为\(W_\Gamma+H-P\)：实际Γ的FP/contact、所有prime powers及两pole均未删减。(A4)只在本次挑选的双pole-zero源上精确为零；并非将目标定义中的pole或Γ除掉。算术Mellin中\(\Lambda_0\Lambda_\chi\)的signed解卷积及Green/primitive自交仍需另付；(A6)的正平滑乘子不是这些费用。

## 7. 消费范围与最强旧扣除

本分支新给这个具体candidate的全部S_exp合法性、精确du核/上界/非逆费用、radial section注入性与405/537联合反测。是否记一数学轮由root和去重审查决定；此处不主张它是新外部定理或实际ζ正性。

552已排一种实际radial adelic Green energy，553已给全线弱norm下降密度障碍；本candidate换为合法KRY输入和smoothing核，其关系失败不推翻这些旧结果，也没有新增whole4/5、core、coupling或Ξ后果。实际primitive循环map尚未构造。将\(\mathcal S_{\exp}/P_{an}\)事后命名为relative cycle不会修复它，亦不能将Q或零除子重引为标签。

停止的是(A1)直接正L²/section或固定最低K线承担完整Weil容量的recipe。没有排除新的relative边界、不同mixed-height、全位协同、强拓扑、源依赖或有费用无限修复；重准入须先有实际cycle/principal身份以及原norm/signed比较实物，不能只给未知bridge。
