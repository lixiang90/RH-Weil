# 589：实际Sonin零均值上界与标量归一化的秩一极限

2026-10-28；C052，G20261027／原冻结0c4f。两个终态证明审稿、current fresh及root全文核后统一消费一轮。原作者输入是bramble_trace固定v2的[Theorem6.3中(6.11)](https://rstation.ai/problems/riemann_hypothesis/papers/2)，只核其必要upper链；作者平台标签不是认证。未审6.4的sharp lower或6.5／后章，不主张外部首创。准确前件／版本／root消费见[根收据](../reviews/2026-10-28/sonin-scalar-normalization/root-consumption-scope.json)。

## 1. 同一实际迹的新上界

沿560／585的实际Sonin正交投影Π_X、有限Euler乘子和完整Gram逆／returns。源为物理log源r，原裸源为e^(-u/2)r；rhat(t)=∫r(u)e^(-itu)du。每个先fixed compact smooth complex源都有原ordinary trace

\[
 T_X[r]=\operatorname{Tr}(A_r\Pi_XA_r^*)
       =\int|\widehat r(t)|^2\rho_X(t)\,dt\ge0.
\]

ρ_X已含归一化，trial／Mellin Hilbert norm用dt/(2π)。置ℓ=logX、A=√X/ℓ、s_X=√X/ℓ²；ℓ不是物理源窗。新核证的结论为

\[
 \boxed{\limsup_{X\to\infty}\frac{T_X[r]}{s_X}
        \le4|\widehat r(0)|^2.}\tag{1}
\]

特别地，若∫r=0，则T_X[r]=o(s_X)。量词是每个先fixed r，不给moving-source统一速率或任意Dlog源的同阶upper。585的每fixed非零源发散仍成立；零均值源可以在更小尺度上发散，二者不冲突。

## 2. 必要证明链及真实范数

原件的D_X是有限Euler乘子，M为固定arch Sonin空间。用weighted norm ||h||_X=||D_Xh||₂，映射h↦D_Xh才是到实际receiver range的等距；以原arch坐标写作M_D G_X^(-1/2)。这里的h是raw求值向量，不是物理卷积源r。

固定gap1的Burnol结构函数及completed/raw kernel给entire unit-ball增长exp(CRlog(R+2))。反射后的h⁺与arch conjugate有相同weighted boundary norm，而D_X⁺在Imz≥1有统一正下界ζ(3/2)^(-1)。Hardy评价和gamma反射控制strip两边；对每fixed X先用barrier令矩形长度趋∞、再令barrier参数趋零，确实去掉粗Gram条件数。得到整个complex disk的

\[
 \sup_{|z|\le R}|h(z)|\le e^{CR\log(R+2)}\|h\|_X,
 \qquad C\text{独立于 }X.\tag{2}
\]

只用逐X norm等价会多付约exp(2A)，不足以完成后续Taylor预算。这个区别已由独占上游稿及fresh逐项核清。

由(2)的Taylor rank近似，经真实等距运输，actual localized singular values同时受投影contraction和M_X倍restriction singular values控制，logM_X=(2+o(1))A。取T=ℓ、R=√X/ℓ⁴、n=ceil((4+ε)s_X)，首n项平方和≤n，余项为exponential小量，得到

\[
 \limsup_X\frac{\operatorname{Tr}(1_{[-\ell,\ell]}\Pi_X1_{[-\ell,\ell]})}{s_X}
 \le4.\tag{3}
\]

Π_X在本式表示其Mellin酉共轭。全线tail另用实际Sonin子空间对自伴compression的reducing性质，Π_X≤(P𝓕_XP)²。weighted Hardy commutator的非负差商核及Tonelli允许measurable cutoff，不需要signed trace-difference公式。完整Γ及全部prime powers给phase导数粗界C(√X+log(2+|t|))，从而

\[
 \int_{|t|>\ell}|\widehat r(t)|^2\rho_X(t)dt=o_r(s_X).
\]

这不是把trial子投影lower反转成整个Π_X的upper。

局部化再由Euler权在固定正测度集合上的exp[(4−Oη)A]大值，迫weighted unit球中的h在该集合小。Quantile Lagrange插值的阶乘因子消去nlogn费用；取R=A/log³A、n=ceil((2+η)A/logA)，统一complexdisk Cauchy余项与插值费用合起来给evaluation norm平方≤exp[(-4+o(1))A]。实际kernel是|D_X|²乘这份norm平方，保完整Gram逆。对每fixedδ>0，故有

\[
 \sup_{\delta\le|t|\le\ell} k_X(t,t)\le e^{-c_\delta A},
 \qquad k_X=2\pi\rho_X.
\]

以tail去掉|t|>ℓ，以此式去掉δ≤|t|≤ℓ，core只用sup_(|t|<δ)|rhat|²乘(3)。先X→∞、后δ↓0即得(1)。完整证明责任分别见[上游稿](../reviews/2026-10-28/sonin-scalar-normalization/source-upper-and-tail-proof-audit.md)、[局部化稿](../reviews/2026-10-28/sonin-scalar-normalization/source-localization-proof-audit.md)与[独立逆审](../reviews/2026-10-28/sonin-scalar-normalization/fresh-zero-mean-upper-audit.md)。

## 3. 最强直接后果：全部固定源配对只剩均值

固定587的du norm1实偶bump r₀，support[-1,1]，h₀=∫r₀≠0，q₀=Q_W[r₀]≥κ>0。585已付T_X[r₀]≥c₀s_X，故实际规则

\[
 \alpha_X=\frac{q_0}{T_X[r_0]}\to0,\qquad W_X(r,s)=\alpha_XT_X(r,s)
\]

合法、非空，给stationary正型tempered分布，并精确匹配r₀。

任意先fixed compact smooth complex源r写成r=c_r r₀+z_r，c_r=(∫r)/h₀，∫z_r=0。(1)和旧r₀ lower给T_X[z_r]/T_X[r₀]→0；实际正型Cauchy–Schwarz控制全部cross项。因此对全部先fixed源对r,s，

\[
 \boxed{\frac{T_X(r,s)}{T_X[r_0]}\to c_r\overline{c_s},\qquad
 W_X(r,s)\to
 \frac{q_0}{|h_0|^2}\left(\int r\right)\overline{\left(\int s\right)}.}\tag{4}
\]

无需T_X[r₀]的exact leading或6.4的sharp lower。这里证明的是全部fixed smooth源配对的秩一均值极限；未另付从这些卷积配对到所有D′ test的factorization／拓扑论证，故不自动声称完整D′收敛。physical侧constant分布与spectral δ₀也不混同。

## 4. 完整Weil目标上的固定非零缺陷

取唯一不同test r₁=r₀′，仍支持[-1,1]且非零、mean0。537原完整型在I₀=(-17/16,17/16)上的κ=2^-49162给

\[
 q_1=Q_W[r_1]\ge\kappa\|r_1\|_{du}^2>0.
\]

q₀／q₁保完整Γ／FP-contact、所有Λ(p^k)=logp及两个pole。mean0不等于polefree，尤其不能删除r₁的odd负pole。

由(4)，W_X[r₁]→0，所以

\[
 |W_X[r_1]-Q_W[r_1]|\to q_1
 \ge\kappa\|r_1\|_{du}^2.
\]

这严格排除本规则的完整Weil逼近，当然也排除D′逼近所必需的这个固定卷积平方test。更一般，任意source-independent正scalar β_X，只要β_XT_X[r₀]→q₀∈(0,∞)，同一Cauchy链就给β_XT_X(r,s)趋(4)，故同样失败。允许β_X任意依X变化及cofinal子序列；未覆盖依源选择的非线性规则或frequency-dependent／signed／joint修复。

## 5. 净增量、结算与核心缺口

585／587的lower与588弱源发散不能决定两个发散量的比值；Gaussian trial的t² upper也不能当作actual upper。新增是同一实际投影的zero-mean相对浓缩信息及其完整fixed-pair秩一后果，来自本次核证的原作者upper链，不是两个lower相除。553所需全Pan精确消去／全域统一界没有免费套用。

此结果改变纯scalar消失迹权的可行性，没有证明完整Q正性／负源或排除不同正D′、成长anchor、非局部有符号补偿及primitive主线。完整signed/corecoupling、同一非零primitive／principal／截面乘法／mixed RR与Ξ仍欠，whole542＋555→557 leading4/5仍仅负惯性UPPER。

C052预算耗尽，统一一数学轮，cadence2→3／历史52→53／latest589，formal17不重置。没有新web、下载或数值，文献仍130项，仅更新既有原件的实际阅读范围。Goal同实例1793085111保持active／open；下一先完成本轮授权main同步及独立核验，后继仍须新actual输入或不同可改变选择的具体比较，不续sharp／rate／归一化参数。
