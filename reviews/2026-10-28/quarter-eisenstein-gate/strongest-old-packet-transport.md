# Quarter E* packet：最强旧运输、threshold域及校准test

2026-10-28；`/root/rational_first_gate` 当前独占最强旧准入。已恢复README／STATE、check→show、同G20261027/runtime1793085111/原0c4f、AK、Goal／frontier／589结算，读[root具体packet](root-quarter-packet-and-old-admission.md)。C052／589 completed且耗尽；本稿不续其证明、不web／重读原PDF／开新source或合同，不改STATE／Git／cadence，不预C053／590。只审当前actual规则到已付C016／545的运输与cofinal test。

**裁决：当前quarter参数和fixed-Y域本来已在C016／545内；scalar校准的cofinal test也可由同一旧DIRECT、Z功能方程／Gamma-theta恒等式及明确的局部域延拓直接决定，宜强旧合成0止。** 不能只因“Eisenstein”标题判旧，也不能把旧compact-source uniform-Y界套到threshold非compact源。下面将旧已付范围、真实变换及当前短运输分开；cofinal主项并非545原文逐字印出的结论。

## 1. 旧对象确实已经是quarter-line

[C016](../../../goals/contracts/C016-modular-cusp-gram-and-actual-weil-transport.md)／[545 §§1–4](../../../notes/545-modular-packet-norm-cusp-blindness-and-weil-transport-gate.md)和[whole-frequency原稿§2](../../2026-10-14/c016-first/whole-frequency-packet-and-object-gate.md)明确固定

\[
 s_t=\tfrac14+it/2,\quad 2s_t=\tfrac12+it,\quad
 Z(w)=\pi^{-w/2}\Gamma(w/2)\zeta(w),\quad
 E^*(z,s)=Z(2s)E(z,s).
\]

它们已经区分Z的0／1 poles、E*的s=1/2假pole相消和几何s=0／1 poles；并未将E*冒作entire ξ。RH的quarter resonance不是unitary Eisenstein line上的L²特征值，此责任早已写入旧记录，不能因当前文字强调critical ζ变量再次晋级。

旧completed family是 `F(z,s)=p(s)E*(z,s)`、`p(s)=s(s−1)`，旧truncation是仅在y>Y删除完整constant mode的Λ^Y，**不是**几何restriction到𝔽_Y。旧direct family则是

\[
 U_Y(t)=\frac{F_Y(s_t)}{\beta(t)}
       =\Lambda^Y E(\cdot,1-s_t),\qquad
 \beta(t)=p(s_t)Z(3/2-it).
\]

原Haar是dxdy/y²，cusp宽度1；source是complex physical du，Fourier为∫r(u)e^(−itu)du，packet为dt/(2π)，Dlog是同一zero-extension域。

## 2. 当前literal packet的两份精确旧输入变换

记 `p_t=p(s_t)=−3/16−t²/4−it/4`，所以 `|p_t|≥3/16`。令

\[
 \widehat f_c(t)=F_r(t)/p_t.
\]

`1/p_t`为bounded real-axis Fourier multiplier，故 `||f_c||du≤(16/3)||r||du`。旧completed A_Y已在**整个L²(R)**输入上付absolute Bochner／HS，而不限compact source。因此

\[
 A_Yf_c=\frac1{2\pi}\int F_r(t)\Lambda^YE^*(\cdot,s_t)dt
       =\Lambda^Y V_r.\tag{1}
\]

这不需要除critical ζ、未知zero位置或指数增长inverseGamma。f_c一般不保compact support；使用的是whole-L²旧域，不是把它假装成原compact源。

另一份对threshold更有用的同对象变换来自旧FE：

\[
 E^*(z,s_t)=b(t)E(z,3/4-it/2),\qquad b(t)=Z(3/2-it),
 \quad\widehat h_r(t)=F_r(t)b(t).
\]

旧545已付b的Gamma双尾，b全轴bounded且无零，所以h_r∈L²(R)，且Fr·b∈L¹。于是旧direct T_Y给同一packet

\[
 T_Yh_r=\Lambda^YV_r=A_Yf_c.\tag{2}
\]

两式不是两个候选，是同一V_r的exact reencoding。原factor dt/(2π)、所有complex槽和双频polarization保持。

旧completed `||A_Y||²_HS≤C√Y`使r↦Λ^YV_r在每fixed Y也是原du上的HS map；direct旧式对whole L²给

\[
 \|T_Yh\|^2\le2[\sqrt Y+Y^{-1/2}M^2+M]\|h\|_{du}^2,
 \quad M=\sup|\alpha/\beta|<\infty.
\]

所以literal fixed-Y packet至少在L²(𝔽_Y)意义完全合法。**fixed-Y存在／norm不是新未知。**

不过当前G_Y是几何cutoff，准确关系为

\[
 \|\Lambda^YV_r\|^2=G_Y[r]
       +\int_{y>Y}|V_r^{\rm nonconst}(z)|^2d\mu(z).
\]

最后一项非负且finite，但不能未经尾界就把两个norm写成完全相等。固定Y的HS／compact性也不能交换成Y→∞的校准结论；旧上界显含√Y，不给所需ratio。

## 3. 阈值到底在哪里：不能偷用旧unitary／compact域

若尝试把同packet改写到 `s=1/2+iv/2`，原参数必须为 `t=v−i/2`，source factor变为 `F_r(v−i/2)`。以uncompleted E为basis时相应系数为

\[
 a_r(v)=F_r(v-i/2)Z(1+iv)
       =\frac{\mu_-(r)}{iv}+O_r(1),\quad
 \mu_-(r)=\int e^{-u/2}r(u)du.
\]

ordinary L²(dv) threshold要求μ₋=0。E*(z,1/2)的点值可去／E(z,1/2)=0，不能把μ₋≠0的1/v系数投入unitary Plancherel。合法移线也须核边界／residue，不能凭half-point相消绕过source域。

[10-22 twisted gate §5](../../2026-10-22/twisted-gamma-signed-admission/history-and-twisted-source-gate.md)只为 `r↦e^(σu)r` 在supp⊂[−L,L]付 `e^(|σ|L)` 的du费；这里σ=−1/2。它没有支付shifted source后的threshold 1/v为L²，更没有一般cofinal-Y packet定理。因此这一旧twist不是免费unitarity。

等价地，用root给定并在当前domain稿核过的exact Gamma／theta inverse Fourier式

\[
 k(u)=2e^{3u/2}\sum_{n\ge1}e^{-\pi n^2e^{2u}},\qquad
 \widehat k(t)=b(t),\quad h_r=r*k,
\]

Poisson恒等式使u→−∞的h_r为

\[
 h_r(u)=\mu_-(r)e^{u/2}-\mu_{-3/2}(r)e^{3u/2}
                  +\text{superexponential remainder}.
\]

正端superexponential。h_r虽属L²，当μ₋≠0时却有

\[
 \int_{-\infty}e^{-u}|h_r(u)|^2du=\infty.
\]

旧compact-source incomplete seed的norm为 `2∫e^(−u)|h|²du`，而旧fixed-L／all-Y overlap依赖compact h。故r₀的threshold源**不在该cofinal旧bound的前件内**；不能以h∈whole-L²就套它。polefree r_*虽消leading项，也不能仅凭weighted integral有限便免费使用无穷coset的unfolding结论。

## 4. 旧已付范围与当前必要桥：不把“未打印”当新数学

旧记录的精确可消费范围是：

| 原件／scope | 已付强后果 | 不能自动外推的内容 |
|---|---|---|
| C016／545 §2、whole-frequency §§3–6 | quarter-line completed全t Bochner／HS、head、双尾、Dlog及complete constant-mode扣费 | 不是仅有限频窗；但fixed-Y compactness不判cofinal scalar校准 |
| 545 §§3–4、whole-frequency §9.2 | direct E_Y(3/4−it/2)的whole-L² fixed-Y全频界、完整Cauchy／Hilbert mixed kernel、强延拓 | 不能再报source uppernorm未知；B_Y会随Y成长 |
| whole-frequency §9.3、cusp-completion §8.2 | 对compact h的 `T_Yh=P_Y[Θg_h−(6/π)∫h e^(u/2)]`，g_h(y)=y^.75h(−logy/2)；fixed-L all-Y界 | h_r有threshold非compact尾，不能照搬该infinite-Y H界 |
| 545 §5／cusp-completion §8.3 | 完整扣除同一cusp后base2盲带及noncompact对照；任意finiteY／有限条件／compact修复范围 | 当前G_Y保留cusp，未扣该mode，不能用blindband直接拒绝r₀校准 |
| 545 §6、10-22 twisted gate §§2–3 | 几何pole与实际dual-pole不同；完整Q高频logΓ和bounded fixed-Y Gram不同；signed桥未付 | 不能只凭Gram正性报Weil；但也不能将fixed-Y carrier极限代当前fixed-source Y→∞ |

若只停在这张表，判r₀／r_*所需的**最小精确量**仍是

\[
 G_Y[r_0]\ge c\log Y,
 \qquad G_Y[r_*]=o(\log Y).
 \tag{3}
\]

不需要恢复Maass–Selberg原PDF、全部unitary谱或完整Weil身份。不能把(3)当已由旧fixed-Y bound直接给出。

当前[domain／cusp稿](quarter-slice-domain-and-cusp-test.md)恰给了这个同对象的短旧运输，而不是另造packet：取compact cutoffs h_N→h_r；每fixedY的旧whole-L²连续性使T_Yh_N→T_Yh_r。`g_h(v)=v^.75h(−logv/2)` 在v↓0有 `C_r e^(−c_r/v)` 界，令Θg_hN在每个𝔽_Y由同一可求和coset Gaussian majorant控制，故旧DIRECT可在**局部L²**取极限。

这一点与“先声称V_r∈L²全cusp”完全不同；r₀实际会有log发散。rank-one residue保持旧6/π，且

\[
 \frac6\pi\int h_r(u)e^{u/2}du
 =\frac6\pi F_r(i/2)b(i/2)
 =\mu_+(r),\qquad b(i/2)=Z(2)=\pi/6.
\]

因此同一actual V_r在每个有限几何域上可合法读为 `Θg_h−μ₊(r)`。本次实际全文核该桥，非依旧compact overlap界的形式外推。

## 5. 最强旧直接推论可判cofinal校准test

本稿不重复另一个完整cusp证明，只记录已核的普通dominated-extension足以运输到的量：identity seed为

\[
 g_h(y)=\mu_-(r)\sqrt y-\mu_{-3/2}(r)
                         +O_r(\sqrt y\,e^{-c_ry}).
\]

nonidentity cosets的smallheight满足 `v≤1/(c²y)`；同一Gaussian majorant的计数给

\[
 \sum_{c\ge1,d\in\mathbb Z}
 e^{-c_r(c^2y+(cx+d)^2/y)}\le C_r\sqrt y\,e^{-c'_ry}.
\]

它不产生第二份√y主项。这两个接口在当前domain稿已完整给出，本稿逐项核其与旧DIRECT／measure／source一致；没有调用新算术估计或新primary source。由此整个packet的cusp为

\[
 V_r(x+iy)=\mu_-(r)\sqrt y-\mu_{-3/2}(r)-\mu_+(r)
                         +O_r(\sqrt y\,e^{-c'_ry}).
\]

宽度1和dxdy/y²使只有√y×√y项产生logY，mixed与constant项可积。故最强可消费的同链fixed-pair结果是

\[
 \boxed{G_Y(r,s)=\mu_-(r)\overline{\mu_-(s)}\log Y+O_{r,s}(1).}\tag{4}
\]

545原文没有逐字声称(4)的threshold packet rank1，但它的actual quarter/direct恒等式、全轴fixed-Y域与经典Gamma／theta输入已经足够，当前局部延拓付清了不能省略的前件。这个普通强旧组合不形成新的独立几何／算术输入，不该为(3)另开新cusp合同。

literal r₀为实正bump，μ₋(r₀)>0；故充分大Y有G_Y[r₀]>0，`α_Y=q₀/G_Y[r₀]` 合法且约为常数/logY。题定 `r_*=(D²−1/4)ψ` 非零并在537小窗，分部积分给μ_±(r_*)=0。它不必mean zero，亦不必使μ_(−3/2)为0；不能借两pole为零把几何constant remainder也删掉。

由(4)，G_Y[r_*]=O(1)，所以

\[
 \alpha_YG_Y[r_*]\longrightarrow0,
 \qquad Q_W[r_*]\ge2^{-49162}\|r_*\|_{du}^2>0.
\]

因此完整fixed test失败。更强地，全部fixed complex源对的normalized极限只为μ₋的rank1配对，不是589的mean rank1；有限层／极限都未自动成为stationary单变量D′。这里仅消费source-form必要test，不凭正Gram宣称完整Weil正性。

## 6. 当前版本、净裁决与停止

本次实际读C016／545、原whole-frequency全文必要packet／domain段、cusp-completion的MS／completion／quarter-frequency／direct段，以及10-22 twisted gate原项目稿；没有重开其外部PDF／后章。又全文核当前 `quarter-slice-domain-and-cusp-test.md` 9226 bytes，LF SHA256 `2ce9b414503627dfbc6bfcd5828c60e13314c460f92d88c612f4644d817ca276`：其fixed-Y cutoff limit及coset bound与本稿旧运输一致。

**净裁决为强旧直接合成0止。** 依据是上列实际source变换和必要threshold域桥，非标题、quarter字样、一般紧性或因“未印公式”而升级。若根消费不保第4–5节的局部domination／cusp主项前件，就只能保fixed-Y合法、(3)未判，不能以希望的logY代证明；当前两稿已将它们具体核闭。

只停止给定quarter E*／原r₀ scalar校准／原几何cutoff族。不排paid cusp的不同signed账本、新seed／base／source域、非局部joint响应、不同positive D′或primitive主线；也不把这次旧运输反测升级整个Eisenstein方法边界。

完整Q的Γ/FP-contact、全部properpowers及双pole从未删除，r_*仅在该fixed test上精确polefree。whole542＋555→557 leading4/5仍只负惯性UPPER，核心signed／primitive-mixed与Goal完成门不变。cadence3/history53/latest589/formal17保持；无C053／590／来源续章、STATE／Git或新计轮。
