# 581：算术衰减的双prime强完成、真实边界与容量缺口

2026-10-23；接[580](580-kry-finite-schwartz-boundary-cocycle-and-level-alias-gap.md)，[C044](../goals/contracts/C044-arithmetic-weighted-two-prime-and-relative-boundary-gate.md)统一一轮。独立fresh限定PASS、root前件闭合，最终版本见[收据](../reviews/2026-10-23/weighted-two-prime/root-consumption-scope.json)。保G20261014／0c4f基线，不创建runtime Goal，不把合同止损当长期目标完成。

有算术来源的衰减权确实解决了580双densegrid的实际范数发散，并可构造保Fourier、乘法及两个边界读出的强完成，完整解析像也全源可见。但它没有保留原Bruhat–Schwartz域；真实S-unit协同在Mellin读出上重新退为scalar，仍失405／537。另添的反向共轭有可付右逆，却吞掉所有源。独立算术primitive与同对象二次容量仍欠。

## 1. 实物、来源与权的算术含义

原件接口仍为[Kudla–Rapoport–Yang1999](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf) §1的Schwartz／section和§4完整Mellin；本轮height、强完成与边界计算由以下原证明给出，不引用原件未证明的一般Schwartz算术推广：[格高度／原域／强完成](../reviews/2026-10-23/weighted-two-prime/arithmetic-height-and-schwartz-domain.md)、[真实S-unit／两方向边界](../reviews/2026-10-23/weighted-two-prime/sunit-relative-boundary-and-principal-test.md)、[原费用／逆与对照](../reviews/2026-10-23/weighted-two-prime/original-costs-controls-and-inverse.md)。

固定k=Q(√−7)、nativeQ／字符／自对偶Haar与Gaussian φ*，ν=||φ*||²；选两split素数2、11（−7≡4 mod11）。其余finite腿固定，norm因子μ保留。physical r=e^(u/2)f为ALLcomplex S_exp，原du及zero-extension Dlog不改。置

\[
 d_{jk}=2^j11^k,\quad a_{jk}=2\log d_{jk},\quad
 c_a(r)=\int r(u)\operatorname{sech}((u-a)/2)du .       \tag{1}
\]

实际fractional ideal I=dO_k及J=I∩O_k给

\[
 H_{jk}=\sqrt{[O_k:J][I:J]}=2^{|j|}11^{|k|},\qquad
 w_{jk}=H_{jk}^{-2},\quad e_{jk}=d_{jk}1_{2^jO_2}1_{11^kO_{11}}.
                                                               \tag{2}
\]

H是原格与fractional格的相对指数，双对偶下对称；不是usual projective height max(分子,分母)的误记。权不读Q或零点，指数2是明示安全选择，尚未被唯一强迫。仅有g-integer实数分布通常没有这些局部格／place数据；它们是本算术候选的额外设施，不能假定由一般分布及其对偶自动恢复。

## 2. 原du费用、全源可见性与原域的精确门

先固定arch Gaussian，定义实际finite函数

\[
 F_w(r)=\sum_{j,k}z_{jk}(r)e_{jk},\quad
 z_{jk}=w_{jk}c_{a_{jk}}(r),\qquad J_wr=\phi_*\otimes F_w(r).
                                                               \tag{3}
\]

全部mixed项由真实Gram G_nm=2^-|j−j′|11^-|k−k′|控制，Riesz常数γ_-=5/18、γ_+=18/5。令W_2=Σw²=(17/15)(14642/14640)，则

\[
 \|J_wr\|^2\le4\nu\mu\gamma_+W_2\|r\|_{du}^2.       \tag{4}
\]

原Dlog亦支付。采样算子为Hilbert–Schmidt，且因a_jk稠密、c=r*sech连续、sech的Fourier乘子无实零，它在全L²乃至全S_exp上注入。于是537每个非根、580单格盲源都保留；没有统一frame lower。

但任何非零源的(3)都不属原Bruhat域。其两位annulus值的双差分为

\[
 \Delta_n\Delta_m F_{nm}=2^n11^m w_{nm}c_{a_{nm}}(r).
                                                               \tag{5}
\]

原Bruhat统一局部常值性使n>N、所有m的右侧零；该半平面的a_nm已稠密，迫r=0。这个门对任何处处非零、使同一球族Hilbert合成合法的权都成立，不是只对σ2，也不只是compact源。它不排不同基、新载体／关系或合法强完成。

## 3. 新的强完成确实存在；不能再泛称边界费用未付

对两个指定finite位，定义实际径向函数代数

\[
 A_\beta=\{F=\sum b_{jk}e_{jk}:\quad
             \|F\|_{A_\beta}=\sum|b_{jk}|H_{jk}^{\beta}<\infty\},
             \quad\beta\ge1 .                       \tag{6}
\]

Riesz保证表示唯一，且Aβ连续进入C₀∩L¹∩L²。**两位partial** selfdual Fourier将e_jk送e_-j,-k，是Aβ等距对合；不声称ramified7的固定腿也被全finite Fourier固定。实际点乘e_j e_l=p^min(j,l)e_max(j,l)给submultiplicative范数，Fourier再给卷积闭性。

若w=H^-σ且σ>β≥1，则

\[
 \|F_\sigma(r)\|_{A_\beta}
       \le2\Big(\sum H^{-(\sigma-\beta)}\Big)\|r\|_{du}.
                                                               \tag{7}
\]

本轮固定σ2、β1，和为18/5。origin与两位Haar积分都连续，费用由

\[
 \sum w_{jk}d_{jk}=\sum w_{jk}d_{jk}^{-1}
       =S_*={15\over7}{732\over665},\quad
 \|F_w(r)\|_\infty,\ \|F_w(r)\|_1\le2S_*\|r\|_{du}
                                                               \tag{8}
\]

支付。这两条实际λ的identity／Fourier读出已付，不能沿用580无权telescoping反例否认它们。

原证明还核出sharp阈值：任意σ>0给Hilbert费，但双读出的全线du／Dlog统一费恰要求σ>1。σ≤1取实际r_T=(D²−1/4)ψ(·−T)、ψ≥0固定compact，原范数固定、双pole矩0；正象限a_jk∈[T,T+2log11]有≳T个项，同号origin值至少T exp((1−σ)T/2)。逐源有限不等于全源统一费。

A1还可扩每个先固定的两位局部g的实际λ(g)读出：Bruhat公式给|λ(e_jk)(g)|≤C_gH_jk，故由A1范数控制。C_g不对g统一，不支付Eisenstein总和或全高度费用。A1是真强完成／实际函数乘法，仍非原Bruhat，亦未证明full local Weil群稳定（unipotent chirp可出径向基）、全部DGA微分、Green／算术cycle或regulator延拓。有限函数乘法不是算术截面乘法或RR容量。

## 4. 固定arch的完整解析像：保Γ、所有powers和常数，仍非Qζ

对每个正负j,k明确选**right-transported** section，而非把standard延拓导数当群等变。580规范给normalized e_jk的classical导数为d φ_0(d²τ)，包含constant、负指标β₁及正系数。有限前缀的去constant Mellin是B_(r,N)(z)ℳ_0(z)，极限为

\[
 B_r(z)=\sum_{j,k}w_{jk}c_{a_{jk}}(r)d_{jk}^{1-2z},\quad
 \mathscr M_0=\Lambda_0\Lambda_\chi
  (\log7+\Lambda'_\chi/\Lambda_\chi-\Lambda'_0/\Lambda_0).
                                                               \tag{9}
\]

由|c_a|≤2||r||₂，B在−1/2<Re z<3/2的紧子带正常收敛并有原du费；每S_exp源可用其指数矩半范数拓到−1<Re z<2，不能把该费用冒称du。先在1<Re z<3/2逐项绝对Mellin积分，再继承亚纯身份。没有擅自改完成化B核；B_r由源和实际格规定，仍是signed/source-dependent，不能假设其正逆。

在z=1/2+it，B是有限复测度Σw c δ_a的Fourier；原子a各异。完整解析输出恒零迫B恒零、全部c=0、r=0，故它也全源可见。每个finite前缀可用z integral、y=dz quasi-endomorphism标记原Z(n/d²)模态问题；负level不等于已付一般整cycle定理，没有共同fixed-level automorphy，无限cycle／Green强收敛另欠。

本节只延拓完整central-derivative／Mellin输出，未声称无限输入的所有s Eisenstein泛函已在A1自动延拓。若坚持standard，原δ=λψ log(|a(g)|/|a(gt_d)|)和其constant修正必须保留。

## 5. 真实S-unit协同：不同对象、完整预算又成scalar

真正global rational m(d^-1)同时移动arch与finite，其实际轨道为

\[
 \Omega_{jk}=D_{-a_{jk}}\phi_*\otimes e_{jk},\qquad
 V_w(r)=\sum z_{jk}(r)\Omega_{jk}.                    \tag{10}
\]

它与(3)不同，不能借用固定arch的全部半范数。对每个finite轨道采用全s transported Φ_n(g,s)=Φ_0(gm(d^-1),s)。在g_v=m(√v)上，两个diagonal交换，rational左automorphy及constant-term的b→d²b换元给

\[
 E_n^{*,tr}(g_v,s)=E_0^*(g_v,s),\qquad
 \mathscr M_{V_w}(z)=C_w(r)\mathscr M_0(z),\quad
 C_w(r)=\sum w_{jk}c_{a_{jk}}(r).                    \tag{11}
\]

两条constant腿、完整Γ、全部素数幂和极点一同保留。无限**输出**由Σ|z|收敛，不反推输入Schwartz或cycle延拓；一般τ不宣称同值。这个真实协同读出又退为一个scalar，|C_w|≤61||r||du/18。

405 P=(D²−1/4)H、H>0及全部平移满足c_a(τ_bP)=−(1/2)∫H(v)sech³((v+b−a)/2)dv<0，故C_w(τ_bP)<0；原(3)、origin与integral也非零，没有principal取消。另一方面w在(j,k)↔(−j,−k)下对称，C_w的源核为偶函数；选537窗内非零奇ψ，r_*=(D²−1/4)ψ，则双polezero、C_w(r_*)=0而Qζ(r_*)≥2^-49162||r_*||²>0。丢失发生在(11)的Mellin读出，不在(3)的全源注入。

实际原域还有贴近首门的反测：ψ≥0非零compact于537窗，r=(D²−1/4)ψ，全部c_a<0。finite origin处(10)的arch函数是Σw c_a φ_*(y/d)。沿k0、d=2^j→∞，c_a∼−4(∫ψe^{3u/2})d^-3，故取y=d时其绝对值至少常数d^-5；所有项同号无抵消。这个双polezero、537正非根的补偿轨道像仍不archSchwartz。有限位读出费不能代付它的全部arch半范数。

## 6. 边界方向与实际费用：不能借另一个复形的右逆

物理轨道系数是z=w c。真实S-unit的label shift为T，因此physical差分为I−T；换用衰减frame w_nΩ_n、坐标c时是

\[
 \partial^{frame}=M_w^{-1}(I-T)M_w .                 \tag{12}
\]

不是反向共轭。对本实际z，沿整格两坐标路径可显式路由

\[
 (I-T_p)b_p+(I-T_q)b_q=z-C_w(r)\delta_{00},\quad
 \|b_p\|_1+\|b_q\|_1\le{805\over432}\|r\|_{du}.     \tag{13}
\]

Σw=61/36、Σ(|j|+|k|)w=805/864使完整边链和尾费均已付。剩余charge C_w对全部405严格非零；直接补掉δ00将连537都杀。ℓ² Hausdorff coinvariants丢charge，不能同时保(11)非零读出。

另添反向共轭B_p=M_w(I−T_p)M_w^-1确为合法解析算子，有明确ℓ²右逆范数≤4/3，实际finite Gram及完整Ω Gram费用≤24/5；相应双向Koszul为H₀=H₁=0、H₂=span_C{w}（权向量张成的复直线，不是charge C_w(r)）。这个修复原费用可付却吞掉H₀全部源；H₂只留预给的一维权，odd537在其通常scalar读出上仍消失。它是另一个复形，尚非算术principal，不能混用(12)方向和(13)费用。

真正常数S-unit d的principal divisor仅支撑2／11及arch；首level特殊循环Z_0(1)−Z_1(1)=Z(1)却有非零char7分量、degree2log7，故常数S-unit principal不能实现所需cycle edge。这个支持反测不排新的isogeny／modular-function对应或真实relative transgression，但它们尚未构造。

## 7. 完整经典预算的实际源费用与合法无界逃逸

580的非compact双polezero Gaussian-trigonometric源R_A满足完整Qζ(R_A)=logA||R_A||²+O(1)>0。本轮同源精确计算为

\[
 (R_A*s)(a)=4\pi e^{-\pi^2-\pi A}e^{-a^2}\sin(Aa),\quad
 0<\|J_wR_A\|^2\le16\pi^2\nu\mu\gamma_+W_2
                         e^{-2\pi^2-2\pi A}.        \tag{14}
\]

Γ(t)=Reψ(1/4+it/2)−logπ及FP/contact先完整进入型；所有Λ(n)按Gaussian自相关给一致可和尾Σ(logn)n^-1/2 exp(−(logn)²/2)，双pole在源上精确0。不存在Qζ≤C||J_wr||²+C₀||r||du²这种有界容量比较。固定537窗另有全部complex双polezero高频源的同类反测；不是成长窗结果。

逐系数除权给Σ|c(a_jk)|²=∞，是每个实际非零源的指定无权恢复费用；合法无界J_w^-1在Ran J_w上仍存在，不必经这个发散向量，未被排除。若能独立构造匹配(14)的无界算术height与完整Γ身份，仍可能有用；按定义将Q拉回其像只得到等价改写。高频平滑机制归552／579旧输入，不另作新经典正号或新预算改善。

## 8. 连续与函数域检验；真正的新设施和缺件

连续d=±1/16族上同一奇compact源、同一J_w及A1费用，native完整Weil型却异号。这拒绝自动识别正Gram与signed Weil型；没有continuous→CM运输，不能称其反驳KRY。

函数域两个places的norm均为Q的整数次幂，步长2deg(P)logQ必相称，不能原样得到本轮densegrid全源注入。真正Weil正号来自同一C×C的primitive mixed交数、实际截面乘法与RR；完整returns／aliases及H⁰,H² poles保留。compact源按统一j₀使用非负Frobenius图，全S_exp另需已证Toeplitz型完成。给source乘w改mixed Gram；给trace乘ρ^|n|则Poisson平滑并改点数预算，二者都不能宣称原RR型不变。A1的函数乘法不是这些截面乘法。

本轮新增：真实指数高度权；可付du/Dlog的Fourier／乘法／卷积／双读出强完成与sharp阈值；全非零源的原域门；全源可见的完整解析像；真实rational协同的scalar预算及两个边界方向、实际routing／Koszul费用。这些是独立局部设施及准确方法边界，尚未提供完整Weil正性或同对象二次容量。

停止这个H^-2球族／S-unit-label-boundary recipe，不调σ／level或串下一paper。下一仅接能扩张**同一**强域中full local作用、实际relative regulator／arithmetic cycles／Green并读取额外原源的具体公式，先405全主同构／537及全源非根／原费，再同对象局部消失过滤、截面lift／乘法／mixed RR。只有未知height或旧源商不得续新数学合同。

局部强完成和费用前沿改变，独立算术容量主瓶颈未变。strong-old542+555→557 whole leading4/5仍为负惯性UPPER；actualq、成长core／coupling／Ξ均未改，长期Goal open。
