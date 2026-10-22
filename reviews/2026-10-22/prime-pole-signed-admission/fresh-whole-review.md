# C041／578：独立整稿逆审与消费范围

2026-10-22；审查者 `/root/prime_signed_fresh_review_1022`，独立于三个原证明分支。只写本稿，不修改主稿、STATE或cadence。已恢复README／STATE、check/show、G20261014、C041及冻结0c4f、D20261022L／cycle15因果范围；实际HEAD为856688eb87de19eff6aceaef77c290d34048e3f1。本审查不是运行Goal、数学计轮或远程发布操作。

**结论：修后限定PASS。** 578实际证明的是一个列明的候选充分包反测，以及原数据signed重写的费用审计；未证明任何新的经典signed消失预算。它不能消费为经典Γ情形的反例、所有Selberg／joint方法的no-go或长期Goal的完成边界。root可将本次实际执行的完整Selberg／强PNT正负同族联检及原源费用反测统一结算一完整轮；分部积分、来源／旧结果恢复、分支和本fresh不各增轮。

## 1. 同对象端点、Γ和原费用

逐式核了578(1)–(5)及577对应原件。正半轴上

\[
 E=\Psi(e^u)-e^u+1,\quad E(0)=0,\qquad
 (H-P)|_{u>0}=e^{-u/2}du-e^{-u/2}dE.
\]

因此(3)分部积分的窗导数、\(-\phi_R/2\)和\(-t\phi_R\sin(tu)\)三项符号均正确。上端窗全部jets为0，下端E为0；删除+1会改变下端账。两pole及全部\(\Lambda(p^k)=\log p\)已在同一式中，完整Γ／FP／contact从未窗化或重选。\(J_R\)确为\(\phi_Re^{-|u|/2}\)的Fourier变换，独立非负，但不能因而断言Γ＋J非负。

(4)仅是绝对upper，固定t／完整有效高度的费用不能混同。主稿已把294输入修为**某个先固定a>0**，没有向旧来源索取任意a的无条件常数。连续族自身对每个先固定a的更强误差则另有直接证明，两种量词已分开。平方根全局前件的直接Abel运输即使给多项式upper，也不反驳其已知RH等价强度。

源式(5)与Stieltjes式一致。\(\|h'_e\|_\infty\le\|r'\|_2\|r\|_2\)支付H¹费用；固定窗调制的原du不变、Dlog平方只增logT而导数增T，故这里确实没有原du／Dlog全源统一支付。返回TV只是旧555／577绝对预算。(2)的差值费用、全部complex原zero-extension域及D_L的成长依赖均未扩大。层本身du无界与fixed窗层差有界的577范围保持。

## 2. Selberg来源、平方类型及实际方向

独立重开了[Selberg1949原扫描](https://www.math.lsu.edu/~mahlburg/teaching/handouts/2014-7230/Selberg-ElemPNT1949.pdf)§2／印页307–310，核(2.6)、(2.8)、(2.9)及前页prime/power展开。其有序prime产品和允许p=q的解释与主稿(6)一致。线性补幂\(O(\sqrt X\log^3(2X))=O(X)\)，卷积差以
\(2\sum_{p^k,k\ge2}\log p\,\Psi(X/p^k)\ll X\sum\log p/p^k\)
支付；全部端点原子全权，故(7)合法。

在安全半平面\(-U'+U^2=\zeta''/\zeta\)符号正确。U²为和频／乘积，Hermitian平方为差频／ratio；后者的二次权和contact不属于同一线性Weil预算。原Toeplitz／三角不等式(9)方向正确，却留下\(P_R(0)\ll e^{R/2}\)。平方分支完整二阶矩(7)的diagonal、ordered off-diagonal及sum-frequency系数4均正确，其粗upper只付平均／绝对账，未推出完整高度负部质量或全t的c_R。没有将其他正对象的费用当实际q_R费用。

## 3. 连续全Euler正反联检及实际负源

核读562§2的positive primitive构造及全repeats／卷积指数，不只由\(v_c\ge0\)推primitive。固定c的\(v=e^u+d\)、\(|d|\le C_ce^{bu},b<1\)给

\[
 uv+v*v=2ue^u+2e^u\int_0^ue^{-v}d(v)dv+ud+d*d
          =2ue^u+O_c(e^u)+O_c(ue^{bu}).
\]

积分即(12)，主项\(2X\log X\)与全部X≥1的O_c(X)正确；两个被积块各自非负。精确Ψ公式(10)、强PNT量词及重根只添多项式的边界也正确。此计算不是任意Beurling系统自动继承经典Möbius除数身份，而是这两个具体全Euler模型确实满足同型总量。

平移现明确\(\tau_hr(u)=r(u-h)\)。\(r_1=(D^2-1/4)\eta_0\)的两pole矩为0，平移差仍为0。对a=1/4，两个指数矩分别是\(A_0(1-e^{\pm ah})\)，因此(13)严格负。正修补给
\(\liminf Q_{K_R}(r_-)\ge-Q_-(r_-)>0\)，而
\(Q_K\le c_R\|r_-\|_2^2\)、\(Q_K\le m_R\|r_-\|_1^2\)，故主稿两个liminf lower方向正确。

这是真实compact物理源，不是辅助全空间norm lower；固定窗Dlog费用亦有限。它是本模型双polezero测试，不能充作经典405主关系。Γ=0模型中负部L¹合法，但未误报为经典Γ所给的有限高度支撑。正段hard修补为0，负段不消；只有列明的positive primitive／对偶／PNT／ordinary fullΛ Selberg粗package被排除，没有伪造“同一经典Γ反例”。

另派 `/root/prime_signed_fresh_review_1022/continuous_selberg_subcheck_1022` 独立代数子核；该子核未写文件或STATE，已完成并对(10)/(12)/(13)与c/m方向报PASS。上述公式由本审查自行复核后消费，不以其摘要代证明。

## 4. 函数域、405／537与不同极限

主稿已补\(a_0=2g\)，保原contact。563／567的同对象H／RR及primitive对应全Gram给(14)；E_j按567的负交数半正定商解释，j0统一将有限源指标移至非负，不能将cyclic Gram商冒充普通trace重数。分段积分保全部complex源和全部returns／pole aliases，compact支撑只使本源求和有限；fixed窗L²／Dlog延拓无需换norm。不能强加连续无周期PNT给native latticeFF，也未外加经典Γ改目标。hard q=0来自独立几何正号及完整trace身份，不归功于非负closed-place数据或Selberg总量。

405仍消费实际noncompact Pan及全部固定平移，在S_exp上\(B_\zeta(p,s)=0\)。577正层高频严格正及非零整Fourier给\(Q_{V_R}(p)>0\)，exact层商失败。固定强源裸尾O(R⁻²)与实际修补费用分开，未以compact交集空洞过关。537固定17/16窗由裸误差＋正修补无条件最终保非根，不先要求修补消失，也未扩大为成长窗。

\(G_R\to W_\zeta\)于D′无条件；V的同目标极限仍须付K。特定577family的c→0、m→0、K在D′消失各自⇔Weil／RH是旧完整身份的结论，不是一般D′控制norm。fixed窗(2)、强源有界集尾费、成长共同预算及全线Hlog operator范围明确分开；553稠密性障碍及每层完整目标差全线无界未被新重写消除。

## 5. 新旧净值、计轮及停止审查

直接对照036§4–5、169§1–3、294§1–2、299§1、562§2、577：乘积/max核区别、临界全尺度预算RH强度、旧PNT运输、连续族本身、Γ误差与正部修补均扣旧。本次新增消费只能是**完整Selberg＋强PNT正负同族联检及其实际双polezero补偿费用反测**和准确选择信息。以这个已执行的具体准入检验统一记一轮可接受；不将独立经典signed输入缺失藏在“来源0”下，也不把标准重写本身作新定理。

strong-old542＋555→557 whole leading4/5仍为负惯性上预算，非负谱lower。没有新classic正号、成长源范围、whole/core/coupling/Ξ后果；宏观容量瓶颈未变。局部粗充分包被反测不等于长期实质方法类边界。主稿停止普通PNT绝对包络／Selberg总量／Toeplitz／二阶矩参数的当前入口，并保更精细Γ-signed、joint、非局部、源适应／强拓扑／变域和有费无限修复，范围准确。

审查中曾发现来源首门旧草稿仍写“进行中／未建C041”，已告root；root随后报告已改为实际“先来源门，取得实物后准入一轮”的转换，fresh后再统一结算。本fresh不改这项状态，也不认证尚未发生的root消费、cadence或GitHub同步；其数学内容已由本稿所绑定的578覆盖。

## 6. 最终版本绑定（UTF-8、CRLF正规化为LF）

下列SHA256只标识实际读到的版本，不代替上面的数学前件闭合。

| 文件 | LF SHA256 |
|---|---|
| notes/578-prime-pole-signed-budget-and-selberg-control-gap.md | d600adfc0fa857623f585af2ec809840296659b737afbcf5cb745eba740e0901 |
| goals/contracts/C041-prime-pole-signed-budget-and-selberg-controls.md | 9110a5e11abcf54d05ed4e9aa7fb9dbdf6b700d6aee8dca3e7144ff537018969 |
| reviews/2026-10-22/prime-pole-signed-admission/cumulative-error-and-original-cost.md | ef53a31cdbc25ead41e3878174e1cd28ab117bc51062cb8412c91fdf759af2a9 |
| reviews/2026-10-22/prime-pole-signed-admission/square-identities-and-controls.md | cba3131c3efce44159187ee4269daa4fe8b8ec949e708c8a57aed880edd9f933 |
| reviews/2026-10-22/prime-pole-signed-admission/history-and-source-admission.md | a3c07e2235c39f08ea79457534c6ad53d9ec5e2f6830b0bb60c48c6a0cd4110c |
| notes/577-full-gamma-positive-repairs-and-independent-budget-gap.md | cf80354ab3bb3c7ca2a2bae7e2aa4083adc47d01da5c984146fb285d7551f55f |
| notes/562-generalized-rh-continuous-g-integers-and-spectral-multiplicity.md | e3e42480b967115accabd741cdbbb220865407396908b74b25bba0c213f60c10 |
| notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md | 96c0c5a62e4175705696a29ed28d890eb11cec6f7351dc763641b65f3fcaec8a |
| notes/036-max-kernel-prime-square.md | 3a7f691437b4a6219867b615766c9ef50231cadd6ef92a3a0a10bf988987c946 |
| notes/169-selberg-profile-rh-equivalence-resonance-wedge.md | a916cbb67c1205fdcca365483ccb78d976067726ba84fb1e4ff95776f0be4a1b |
| notes/294-pnt-envelope-gain-and-fixed-source-saturation.md | b7dcac042e667804d59c098581f4c58cfda516778348745614ac02652bbedb40 |
| notes/299-local-one-sided-budget-mellin-strength-audit.md | 3aa3f4b7e7a04215a70efa70a825e66a1a7f5b84f0cc8f85d8a4a254c1eeaae7 |

最终判定：以上版本限定PASS；无待修数学阻断。root结算仍须自行保存对象／norm／量词／paid与open／强旧净值收据并核实现场进程及Git，不由本稿自动完成。
