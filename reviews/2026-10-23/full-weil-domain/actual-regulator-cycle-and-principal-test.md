# 实际arch右运输的额外物理源、native循环／Green读出与principal首门

2026-10-23。独占分支；不改STATE／cadence。接581的full-local／extra-source问题；以下是明确公式的原件，不把出稿当root消费。保同G20261014／冻结0c4f。新增只限一种不经native c(r)的实际几何读出及其首门计算；尚不是成功的算术regulator、relative primitive或独立二次RR。

## 1. 已定位的原件及本次延拓边界

使用[Kudla–Rapoport–Yang1999作者版](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)：§1(1.4)–(1.6)给Schwartz到诱导section及standard延拓；Theorem3／§5给native正指标循环的degree；§6(6.16)–(6.19)给native负指标的arch Arakelov divisor。§6开头将一般Schwartz算术解释列作待扩展事项，不能当已证full-Weil循环functor。本分支不串2011或其他paper以填未给比较。

固定k=Q(√−7)、原Q／字符／Haar和native Gaussian φ*，有限腿原样。令

\[
 D_u\phi(x)=e^{u/2}\phi(e^{u/2}x),\quad
 T_*r=\int r(u)D_u\phi_*du,\qquad
 M_r(z)=\int r(u)e^{zu}du.                              \tag{1}
\]

ALLcomplex r∈S_exp，原du及zero-extension Dlog；579已付T*:S_exp→Schwartz、实际Hilbert原费≤2πν||r||²及sourcewise强半范数，ν=||φ*||²固定。这里保留整个T*r，不投weight1的c(r)φ*。固定finiteSchwartz已经是581的A1及拟扩full-local域的合法子域；本构造不是在有限位无限完成上偷用一般cycle theorem。

下列目标是native Arakelov divisors的实／复线性化、按(n,v)组织的实际family。它们有有限支撑的原循环或有限维arch分量，不是整cycle；也不是已给unit／K-theory regulator或算术section乘法。

## 2. 必须选全s右运输，不能把standard导数免费当等变

设Φ₀(g,s)为原native全s section，a_u=e^{u/2}，只在arch位作用m(a_u)。选

\[
 \Phi_u^{tr}(g,s)=\Phi_0(gm(a_u),s),\quad
 \Phi_r^{tr}(g,s)=\int r(u)\Phi_u^{tr}(g,s)du.            \tag{2}
\]

在s=0，其Schwartz输入恰是T*r；这是实际右运输，不读取Q或零点。它通常不是λ(T*r)的standard s-extension。若后者记std，则两者导数差的实际section为

\[
 \delta_u(g)=\lambda(D_u\phi_*)(g)
  \{\log|a(g)|-\log|a(gm(a_u))|\}.                     \tag{3}
\]

相应全Eisenstein导数差是E*(g,0,δ_u)，不是可以删除的常数。按φ=−v^{-1/2}E*′规范，classical差带−v^{-1/2}。对arch Iwasawa高度，右m(a_u)只把底行两坐标分别乘a_u及a_u^{-1}，故(3)中log差绝对值≤|u|/2；强域积分的此项可按S_exp指数矩支付，但不因此取得原du的全g统一费用或循环等变性。

这里有一处决定性的坐标区别。若g_τ=n(x)m(√v)，则

\[
 g_\tau m(a_u)=n(x)m(\sqrt{v e^u}),\qquad
 \phi_r^{tr}(x+iv)=\int r(u)e^{u/2}\phi(x+i v e^u)du.   \tag{4}
\]

**x没有缩放**。这不是φ(e^uτ)，不产生非整数Fourier频率；变化的是每个native整数频率的v依赖幅度。公式(4)可先直接以原native Fourier级数定义，强衰减付逐项及全部fixed compact (x,v)微分；这不需要声称一般非native Gaussian的算术定理已证。其正指标系数至多多项式增长，负指标β₁尾指数衰减；v e^u→0时各级导数至多指数于|u|增长，所以S_exp确实足够。

## 3. 具体的native循环与Green源积分

记原正循环Z(n)，deg Z(n)=a_n；原负arch divisor为Z(−m,y)，其λ分量为2N_λ(m)β₁(4πmy)，其中N_λ是原§6的实际整数计数。对n,m>0及v>0设

\[
 L_{n,v}(r)=\int r(u)e^{u/2}e^{-2\pi n v e^u}du,\qquad
 \mathcal Z^+_{n,r}(v)=L_{n,v}(r)Z(n),                  \tag{5}
\]

\[
 \mathcal Z^-_{m,r}(v)=\int r(u)e^{u/2}
       e^{2\pi m v e^u}Z(-m,v e^u)du.                 \tag{6}
\]

这是Div_R／Div_C中的确实积分：(5)只乘一个固定有限cycle；(6)只积分有限个complex places上的实际β₁函数。负项u→+∞时β₁(4πmv e^u)乘exp(2πmv e^u)仍指数衰减，u→−∞时只有O((1+|u|)e^{u/2})，所以逐源及强拓扑积分成立。

于是(4)的非零Fourier模态，按e^{2πinx}而非e(nτ)展开时，正／负幅度分别正好是deg(5)与deg(6)。若改回e(nτ)，必须再把(5)乘e^{2πnv}、(6)乘e^{-2πmv}；不可混淆这两种cycle系数的费用。因为这些是v依赖的实／复权，它们不是一个v无关的整moduli cycle，也没有声称该积分保持整消失阶／同源局部长度。

这给了一种真实读取额外r信息的几何family，非c(r)标量包装。但它不是full local Weil作用下的arithmetic cycle functor：(3)未取得同对象循环cocycle，高K-type的标准Green身份、finite A1的无限cycle延拓和actual principal homotopy均未由(5)–(6)推出。

## 4. 原du／Dlog费用：fixed v可付，全高度不能隐去

(5)核的原du范数可精确计算：

\[
 \|e^{u/2}e^{-2\pi nve^u}\|_{L^2(du)}^2
     =\frac1{4\pi nv},\qquad
 |L_{n,v}(r)|\le(4\pi nv)^{-1/2}\|r\|_{du}.            \tag{7}
\]

对(6)，把每个N_λ(m)提出后，其完整Fourier幅度核为
g_{m,v}(u)=2e^{u/2}e^{2πmv e^u}β₁(4πmv e^u)。换元y=2πmv e^u给

\[
 \|g_{m,v}\|_{du}^2=\frac\pi{6mv}.                    \tag{8}
\]

独立核算所用恒等式为

\[
 \int_0^\infty e^{2y}\beta_1(2y)^2dy
  =\tfrac12\int_1^\infty\frac{\log t}{t(t-1)}dt
  =\frac{\pi^2}{12}.
\]

前式由β₁双重积分及Tonelli直接得；非数值拟合。Dlog控制du，故同费支付；真实N_λ(m)、a_n及按q展开的exp因子须保留，未付全n高度和或quadratic intersection费用。

这不是全高度统一原费。若固定双pole-zero r且L_{n,v₀}(r)≠0，令r_b(u)=r(u−b)、v_b=v₀e^{-b}，则

\[
 L_{n,v_b}(r_b)=e^{b/2}L_{n,v_0}(r),\quad
 \|r_b\|_{du}=\|r\|_{du},\quad\|r_b\|_{Dlog}=\|r\|_{Dlog}. \tag{9}
\]

双pole-zero保持。b→+∞给实际源费发散；不是拿全空间范数lower代替实际费用。fixed v或fixed source window上的费用合法，S_exp强半范数同样合法；不能升为v↓0／成长尺度统一费用。

## 5. 全源可见，却不消405；537奇非根确已找回

对固定n=1，把(5)视为全部v>0的family。x=e^u变元下

\[
 L_{1,v}(r)=\int_0^\infty r(\log x)x^{-1/2}e^{-2\pi vx}dx.
\]

其密度在0／∞均可积（S_exp），Laplace唯一性给：全部v的L为0当且仅当r=0。因此这一family在全S_exp上注入，不再只看到c(r)，不是581真实S-unit协同的scalar读出。

恢复405真实noncompact关系P=(D²−1/4)H，H>0且H∈S_exp，以及全部平移。对任何双pole-zero r，由支配收敛有v↓0展开

\[
 L_{n,v}(r)=-2\pi nv\,M_r(3/2)+o(v).                  \tag{10}
\]

405给M_P(z)=(z²−1/4)M_H(z)，所以M_P(3/2)=2M_H(3/2)>0；全部τ_bP仍有这个严格正的矩，乘e^{3b/2}。故

\[
 L_{1,v}(\tau_bP)=-4\pi v e^{3b/2}M_H(3/2)+o_b(v)<0
 \quad(v>0\text{充分小}),                              \tag{11}
\]

而deg Z(1)=2log7>0。(5)在每个真实Pan平移上都存在非principal的正指标输出；不能通过源双pole-zero宣称degree-zero或principal。这里允许v的small范围依b；未给所有v同号或成长uniform结论。

另一方面，取537窗内φ≥0偶Cc∞(−1,1)，ψ=uφ、r*=(D²−1/4)ψ。其μ±=0、c(r*)=0，但M_ψ(3/2)>0，因此M_r*(3/2)=2M_ψ(3/2)>0；(10)使L_{1,v}(r*)≠0于小v。这一实际source确实找回579／581 scalar漏掉的537非根，且537独立保证Qζ(r*)≥2^-49162||r*||²>0。没有用Q来选择系数。注入保非根的改进，不能掩盖principal首门的独立失败。

## 6. 完整Γ、所有素数幂与两constant腿未被删；对象仍是signed KRY线性预算

原a₀(v)=−h_k(logv+C₀)，C₀=log7+2Λχ′(1)/Λχ(1)。直接积分(4)得实际constant

\[
 A_{0,r}(v)=-h_k\{(\log v+C_0)\mu_+(r)+M'_r(1/2)\}.
                                                               \tag{12}
\]

即使μ±=0，M′_r(1/2)项也不能删。405对全部τ_bP有M′_{τ_bP}(1/2)=e^{b/2}M_H(1/2)>0，constant也不为0。它不是经典Weil双pole二次型的同名替代。

对Re s>1，以全部(4)减(12)作Mellin，绝对换序由S_exp指数矩及原native非constant模态的绝对积分支付，得到

\[
 \mathscr M_r(s)=M_r(1/2-s)\,\mathscr M_0(s),\qquad
 \mathscr M_0(s)=\Lambda_0(s)\Lambda_\chi(s)
  \{\log7+\Lambda'_\chi/\Lambda_\chi-\Lambda'_0/\Lambda_0\}(s).
                                                               \tag{13}
\]

之后继承原亚纯身份。全Γ(s/2)与Γ((s+1)/2)来自原正／负项的同一β₁积分，所有proper prime powers留在完整L Euler因子，两个端点／constant腿由(12)及(13)保留。μ±=0只使M_r(1/2−s)在s=0,1为0；原KRY的double-pole行为可能仍留下由M′_r(±1/2)确定的simple部分，不能把它与经典Qζ的双pole矩混同。

在s=1/2+it，新增因子恰是rhat(t)，并非c(r)或零点标签。固定ℳ₀在这条线有Γ给的指数尾及标准L多项式界，故完整Mellin像的L²费用≤sup_t|ℳ₀(1/2+it)|²||r||du²；其解析像也全源可见。这是解析输出费用，不是读回cycle／height的有界逆。

405的因子明确是s(s−1)M_H(1/2−s)，实s>1非零；ℳ₀(s)>0亦可直接由positive native模态或完整Euler／Gamma式核查，所以principal失败也可在完整预算中看见。任何以“把此非零像定义为边界”作修复，都还须一个实际算术同伦；按定义取其商只回旧商包装。

经典目标仍是Qζ=Γ/FP/contact−全部Λ(p^k)相关+双pole、ALLcomplex与原du/Dlog；(13)不是Qζ，更不是其平方和。将(13)乘formal signed逆以抽出−Λ₀′/Λ₀，仍欠同一cycle/Green上的实际解卷积、cross terms、原费用及同对象mixed二次身份；这里不重复579有限Euler旧费作新容量。

## 7. 局部过滤、函数域和连续对照；准确止门

(5)保原Z(n)的实际有限支撑与native局部长度，但只乘一个signed／complex实数，未给source的整section及消失过滤；(6)是真实arch-current线性积分，却没有把(3)实现为算术principal cocycle。primitive化若只是事后把全部405像商掉，其存在性为旧源商，不能付款RR。要有独立平方RR，还须同一整模型上的实际source section、local vanishing／boundary principal同构、截面乘法、Green与mixed pairing的signed比较；这些不能从线性degree或positive Gaussian Gram推出。

固定q=7的native coarse载体还可作一个更准确的实物计算，范围不能升级。原Corollary5.4／§6取M=Spec O_H，H为Hilbert class field。对O_k=Z[(1+√−7)/2]，在任意z∈C先选最邻近的虚行，再选该行最邻近实格点，余项的实部≤1/2、虚部≤√7/4，故norm≤11/16<1。该norm-Euclidean除法给O_k为PID，h_k=1，因而H=k。

M仅一个complex place∞。采用degree(∞)=1及principal约定

\[
 \operatorname{div}(a)=\sum_{\mathfrak p}v_{\mathfrak p}(a)\mathfrak p
                      -\log|a|^2\,\infty,
\]

每个prime ideal(π)给[𝔭]=log N𝔭[∞]。因此这个**固定coarse M的native Arakelov divisor实／复线性化，模同系数principal span**，degree诱导同构到R／C；degree-zero类全零。普通整数finite-divisor版本也由PID直接约化为唯一arch实系数，单位只有±1没有额外log关系。此处不借stack的高阶K群、不同整模型或family的相对Picard来增强结论。

这说明不能把一份已经定义在该native CH¹中的degree-zero输出称为隐藏的非平凡primitive方向；若保持family全部degree则仍有丰富(n,v)读出，但不是同一固定CH¹的非平凡primitive交数空间。它不排framed／relative／higher regulator、不同高维载体、新算术曲面、改变field／level后的对应；更不证明full finite-Weil的所有λ核都无几何解释。

连续d=±1/16控制可使用同一个537奇r*。本次Laplace／Green输入与r的原norm均相同、全可见性也相同，但各自native完整Weil值异号；这拒绝“全源可见+局部Weil正Hilbert实现⇒native正性”的自动推论。没有continuous→CM几何运输，不称其反驳KRY。

真函数域567／576的正号来自同一C×C的primitive correspondences、实际截面乘法和RR／Hodge mixed容量，含全部returns／aliases与H⁰/H²项。CM的Spec O_H native degree在此是线性预算，不能充当该曲线平方mixed自交。把函数域source先做任意Laplace平滑再套RR，会改变实际source Gram与预算；必须另付同对象运输，不能将本次注入当成已付该箭头。

因此止本具体arch-only right-transport／native-cycle-integral入口：额外物理源与原du的fixed-height费用、full native Γ及所有powers/constant均有实物；537恢复而405全主关系明确失败，未到primitive二次容量。新边界若读取其他原源信息并有真实principal与Green cocycle，仍未被排除；full-local有限域、不同算术载体、无界／强拓扑height和有费相对设施保留。strong-old whole4/5负惯性UPPER、actualq／core／coupling／Ξ未改变。本分支不自行计研究轮。

## 8. Root消费记录

- 对象/域：S_exp原physical r，经T*r与arch全s右运输；目标是Div_C(M)按整数n和v>0的family，正指标有限cycle线性化、负指标有限arch currents。不是unit/K regulator、整截面或generic full-Weil cycle theorem。
- Paid：579原Schwartz/Hilbert接口；原native KRY cycle/β₁；本次实际(4)–(13)、fixed-height原du/Dlog、fullS_exp注入与405全部平移／537具体源测试；强费用用S_exp半范数明示。
- 方向/误差：等式而非未知小余项；small-v o_b(v)仅逐固定b，(9)是实际源的高度费。std/tr差为(3)，未删除。positive index native length非负不使signed源系数或mixed交数非负。
- Coverage/耦合：完整解析像与Green family全源可见，principal不下降；没有同对象整过滤/截面乘法、signed ζ运输或primitive RR容量。不能并上full finite-domain设施自动升级。
- 强旧净后果：经典Weil正性/容量和whole4/5/core均无新后果；本次准确的额外source readout及方法首门可作为局部新输入，是否准入本轮统一合同由root决定。
