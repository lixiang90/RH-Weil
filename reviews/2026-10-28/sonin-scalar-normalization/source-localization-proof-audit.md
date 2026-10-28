# 固定v2 Th6.3：localization至zero-mean upper的独立核证

2026-10-28；`/root/rational_first_gate` 当前独占sourceproof腿，区别于本目录已终态的规则／类型咨询。已恢复README／STATE、check→show、同G20261027/runtime1793085111/原0c4f、AJ、Goal／frontier／summary和原2490-byte source gate；随后读root新建C052合同。C052承接AJ这一**同次**来源证明首门，不重启C051／C050、不额外计轮。本稿不web／下载／修proof／读sharp或追paper，不改STATE／Git／cadence。

**限定PASS：817–869的必要localization链闭合；终稿前已全文读取并绑定当前upper/tail终稿，U7／U8／UT与本腿实际规范匹配，联合必要链无未付技术接口。** 不能只用raw arch bound加m_X⁻¹冒作U7；该差别会直接破坏原Taylor余项。最初对上游保持的conditional已由第9节当前版本对齐解除，root／fresh总体消费仍另核，不凭source标签认证。

## 1. 固定原件、实际阅读与责任边界

原件为本地 `literature/local/2026-10-28-core-source-location/bramble-trace-rstation-2-v2.md`，rStation v2，61862 bytes，raw及LF SHA256均为

`541098314b2ddc5f8645babf82086e87d16c46188268cbc7ed6cfc1f98720058`。

实际逐段核：784–809的必要陈述／规范，817–869的evaluation-localization proof；必要接口667–720、738–764，及565–575的已定位upper陈述。未审871以后的moving translation／receiver strong-limit证明，未审6.4／6.5／§7。一次定点关键词定位曾显示后文命中行，未消费其推导或作为任何证明前件。Burnol旧Th8的primary具体核读由当前upper腿承担，本腿只核同章给出的raw/completed接口及其对localization的准确责任。

同一实际空间沿560：固定arch Sonin M，finite Euler乘子D_X，`G_X=P|D_X|²P|_M`，weighted norm `||h||²_X=||D_Xh||²_(L²(dt/(2π)))`。actual range为D_XM，正交化用完整G_X⁻¹，不把乘子当酉。

固定 `L=logX、A=√X/L`。source f是原physical log源，F(t)=∫f(u)e^(−itu)du；f先fixed、complex、compact smooth。当前只需F(0)=0的upper，不再审已付lower。

## 2. 上游接口明列：raw entire不等于weighted统一

先明列调用当前upper腿的三项结论；本腿最初按conditional审查，终稿实际版本对齐见第9节：

\[
 \tag{U7}
 \sup_{\|h\|_X\le1,\ |z|\le R}|h(z)|
 \le C_R=\exp(CR\log(R+2)),\quad R\ge2,
\]

C不依X／finite prime set，并且h是raw arch evaluator所定义的**entire**函数。

\[
 \tag{U8}
 \limsup_{X\to\infty}\frac{L^2}{\sqrt X}
 \operatorname{Tr}(1_{[-L,L]}S_X1_{[-L,L]})\le4,
\]

S_X为actual projection到D_XM，kernel按dt/(2π)定义。

\[
 \tag{UT}
 \int_{|t|>L}|F(t)|^2 k_X(t,t)\frac{dt}{2\pi}
 =o_f(\sqrt X/L^2).
\]

UT限每先fixed smooth compact f，不偷换ALLmoving源／Schwartz seminorm一致。

raw entire／growth的同章接口为667–696：Burnol combined E entire；其bilinear completed kernel在 `s+z−1=0` 的分子消去，故quotient可去；除以γ(s)γ(z)时使用entire的reciprocal gamma，不引入新的poles。对任意complex disk先在更大disk做Cauchy derivative，再取Hermitian conjugate diagonal，可将E的 `exp(CRlog(R+2))` 界运输为raw evaluator的original unit-ball界。mere“各函数entire”不足以替代这份unit-ball uniform bound。

尤其，raw界单独只给

\[
 \|h\|_0\le m_X^{-1}\|h\|_X,\qquad
 m_X=\prod_{p\le X}(1-p^{-1/2}),\quad
 \log m_X^{-1}=(2+o(1))A.
\]

因此它会在weighted unit球的complexdisk界多付约2A。原698–720的Hardy／C₀反射／strip argument必须真的将此prefactor移除，才是U7：D_X⁺在Imz≥1有统一正lower，h⁺及C₀h⁺边界weighted norm相同；下侧u_∞解析、y=−1增长仅O(1+|t|)；`h⁺/(z+2i)` 在strip两侧有统一界。乘 `exp[−εcosh(az)]` 后，对每个fixed X先让rectangle长度趋∞再ε↓0，原raw finite-order增长足使vertical边消失，故可去掉依X的prefactor。这段角色／极限次序与U7一致；其primary前件由upper腿最终核证。

若U7只能换成含m_X⁻¹的较弱界，则下节原n的Cauchy余项只有 `exp[−(η+o(1))A]`，**不足**推出6.12。这里不能以“norm等价”略掉该条件数，也不在本稿改n修proof。

## 3. E_X的正测度与weighted小值：6.13准确

固定充分小η>0（例如η<1/10），选fixed d>0使 `1/√(1+4t²)≥1−η` 于[−d,d]。phase `tL−arctan(2t)` 的导数为L+O(1)，所以条件cos≤−(1−η)所占的Lebesgue measure最终≥某fixed m_η>0；不要求E_X为interval或光滑。

旧Lemma6.1的uniform absolute o(A)给该E_X上的

\[
 \log|D_X(t)|^2
 \ge4(1-\eta)^2A+o(A)\ge(4-9\eta)A.
\]

所以对weighted unit球，按原dt/(2π) norm准确有

\[
 \|h\|_{L^2(E_X,dt)}
 \le\sqrt{2\pi}\,e^{-(2-9\eta/2)A}.\tag{1}
\]

2π在这里来自将weighted norm换成dt的L²，不是actual trace再多一份归一化。

## 4. Quantile／Lagrange费用：没有遗漏nlogn

给定E⊂[−d,d]、|E|≥m>0，degree≤n的complex polynomial P，先在measure≥m/2的子集取 `|P|≤√(2/m)||P||_(L²E)`。可取n+1个quantile nodes，其距离至少 `c|j−k|m/(n+1)`；Lebesgue measure≤interval长度保证这点，节点允许取子集closure，continuity保值界。

Lagrange第j个denominator因此≥ `[cm/(n+1)]^n j!(n−j)!`。对|z|≤T，numerator≤(T+d)^n。求和使用

\[
 \sum_{j=0}^n\frac1{j!(n-j)!}=\frac{2^n}{n!},
 \qquad\frac{(n+1)^n}{n!}\le C e^{Cn},
\]

得到原式

\[
 \sup_{|z|\le T}|P(z)|
 \le C_m\left(\frac{C(T+d)}m\right)^n\|P\|_{L^2(E)}.
 \tag{2}
\]

complex coefficients无额外限制；没有剩下一个 `exp(Cnlogn)` 的未付费用。m=m_η只依先fixedη，所以后面interpolation factor的常数不随X变化。

## 5. Cauchy／Taylor至6.12：全部complex disk与unit球统一

按原文选

\[
 R=\frac A{(\log A)^3},\quad
 n=\left\lceil\frac{(2+\eta)A}{\log A}\right\rceil,
 \quad T=L^B
\]

（B>0先fixed）。最终R>T、R≥2，且

\[
 \log C_R=O(A/(\log A)^2)=o(A),\qquad
 n\log(R/T)=(2+\eta+o(1))A.
\]

U7使h在|z|≤R的sup对整个weighted unit球同时≤C_R。若P_n是其degree-n Taylor截断，则

\[
 \sup_{|z|\le T}|h-P_n|
 \le C_R\frac{(T/R)^{n+1}}{1-T/R}
 =\exp[-(2+\eta+o(1))A].\tag{3}
\]

E_X上的余项以T换成fixed d，仍至少有该负指数；其L²费再乘√(2d)只是fixed常数。将(2)用于P_n，其interpolation factor的log为

\[
 O_{\eta,B}(n\log L)=o(A).
\]

故由(1)、(3)，`||P_n||_(L²E_X)` 的小值和两处余项都足以给

\[
 \sup_{\|h\|_X\le1,\ |z|\le L^B}|h(z)|
 \le\exp[-(2-9\eta/2+o(1))A].
\]

先X→∞后η↓0：对每ε>0先选fixedη，再选X起点，便得6.12的 `exp[(-2+o(1))A]`。m_η／d及阈值可依η；没有η_X、B_X或遗漏moving unit-vector费用。这个步骤明确依U7而非raw norm加m_X⁻¹。

## 6. Actual kernel及6.10：Gram没有被换成trial模型

weighted evaluator的norm平方准确为

\[
 Q_X(z)=\sup_{\|h\|_X\le1}|h(z)|^2
 =\langle G_X^{-1}k_0(\cdot,z),k_0(\cdot,z)\rangle.
\]

因此6.12给 `Q_X(t)≤exp[(-4+o(1))A]`，uniform于|t|≤L^B。actual projection range D_XM 的kernel是

\[
 k_X(t,t)=|D_X(t)|^2Q_X(t),\qquad
 \rho_X(t)=\frac{k_X(t,t)}{2\pi}.\tag{4}
\]

它来自真实isometry `M_(D_X)G_X^(-1/2)`／完整inverse，非只取585／587的positive trial kernel。k按dt/(2π)定义，所以ordinary source trace是 `∫|F|²k dt/(2π)=∫|F|²ρdt`，不可再添除一份2π。

固定δ>0，Lemma6.1的absolute uniform error在δ≤|t|≤L^B给

\[
 \log|D_X(t)|^2\le\left(\frac4{\sqrt{1+4\delta^2}}+o(1)\right)A.
\]

与(4)合并，准确得到6.10：

\[
 \sup_{\delta\le|t|\le L^B}k_X(t,t)
 \le\exp[-(c_\delta+o(1))A],
 \quad c_\delta=4-4/\sqrt{1+4\delta^2}>0.
 \tag{5}
\]

固定B的logarithmic heights最终在旧absolute uniform prime range内；未把只在finite height的relative式外推全线。6.11只需这个upper；858–867的反向Q_X lower／common-zero断言及完整6.9 density equality并非其必要前件，本稿不据它们额外消费结论。

## 7. U8／UT对齐后，先X再δ推出6.11

对fixed complex compact smooth f，分成 `|t|>L`、`δ≤|t|≤L` 和 `|t|<δ`。第一段由UT为 `o_f(√X/L²)`；第二段由(5)和长度2L为

\[
 O(\|F\|_\infty^2 L e^{-c_\delta A/2})
 =o_f(\sqrt X/L^2).
\]

第三段以fixed `sup_(|t|<δ)|F(t)|²` 乘U8的actual central trace mass，所以

\[
 \limsup_{X\to\infty}\frac{L^2}{\sqrt X}\,T_X[f]
 \le4\sup_{|t|<\delta}|F(t)|^2.
\]

X先趋∞，δ固定时exponential middle常数合法；随后δ↓0，连续F给

\[
 \boxed{\limsup_{X\to\infty}\frac{L^2}{\sqrt X}\,T_X[f]
       \le4|F(0)|^2.}\tag{6}
\]

T_X≥0，故F(0)=0时即 `T_X[f]=o(√X/L²)`。zero-mean结论实际只需U8中有限limsup常数，不需要6.4sharp下界或再优化4。这里没有ALLchanging-source uniform rate，没有将fixedδ换成δ_X，也不消费source之外receiver strong-limit／movingtranslation断言。

## 8. Paid／conditional／open与实际scalar消费

本腿实际核清：E_X measure／6.13、quantile interpolation的factorial账、完整complex Cauchy/Taylor指数、weighted-unit球量词、Q_X／actual k的Gram和2π、6.10至6.11的fixedδ先X后δ。没有发现这些local steps的实质断点。

上游U7必须包含raw entire unit-ball complexdisk界及weighted strip去m_X⁻¹；U8必须是actual localized projection trace mass，UT必须是原actual trace tail。它们均由当前另一独占腿核，本稿现已全文读最终版本并对齐三接口。若后续root／fresh发现任一项的实质前件失败，应冻结本稿(6)的消费，准确FAIL该必要链并停止原sourceproof，不在本稿改n／window／source修补。

在这三接口的当前联合结论下，r₁=r₀′满足F₁(0)=0；(6)与585已付r₀ lower使 `T_X[r₁]/T_X[r₀]→0`，而完整q₁>0，故当前α_X=q₀/T_X[r₀]规则不能逼近完整Q。相同fixed test也拒绝任何positive scalar β_X若 `β_XT_X[r₀]→q₀∈(0,∞)`；这不是全部消失迹权／signed／nonlocal机制的边界，也不证明所有normalized分布已有rank1极限。

q₀／q₁仍含完整Γ／FP-contact、所有Λ(p^k)=logp及双pole；r₁ mean0不等于polefree。No upper／localization estimate被冒作Weil正性。当前sourceproof的编号／统一轮数／终态仅由root对齐两稿和fresh后消费；本稿无STATE／Git／cadence操作，whole4/5UPPER及primitive/mixed／signed核心门不因draft完成。

## 9. 当前上游终稿的实际对齐

已全文读[当前upper/tail稿](source-upper-and-tail-proof-audit.md)：10211 bytes，LF SHA256 `bab769113b4ce8c858dfd4b7a83dea6abd8808436a599d2206ea9a9bf0915fff`，现场重核一致。

其§2–3给raw／completed entire kernel增长、weighted Hardy反射和strip去prefactor，正是U7；§4在同一actual isometry／Hilbert measure给U8；§5以actual投影比较、weighted commutator非负核／Tonelli及fixed-F Schwartz尾给UT。与本稿的source Fourier、S_X=actualΠ_X、k_X=2πρ_X、X／L／A及fixed-source量词一致，不需要补一个未审sharp lower／receiver limit前件。

本稿不重证上游已给的Burnol PDF6 primary段或其全部tail细节，但已核其最终推导在本腿使用处确实足够；上游也未预消费本腿localization。联合6.11链由这两个不同原件拼接，根前件闭合和current fresh仍须按实际版本独立核。本稿的限定PASS不等于Goal完成或root已结算。
