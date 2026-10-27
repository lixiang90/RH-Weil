# 完整 Γ／signed 原命题定位：本地去重及候选验收差

2026-10-28；unit_height 独占本地支持稿。恢复 G20261027、STATE/D20261028H、Goal、前沿和唯一 [有限定位门](../post-lower-causal/next-complete-gamma-signed-source-location.md)，check/show通过。本稿不查网、不下载、不读新paper或推进数学，不改STATE/cadence/Git；root独占本轮最多两批各三query的外网定位。来源/排重0数学轮，cadence3／历史49／cycle16不动。

## 1. 不能混同的靶对象

[577](../../../notes/577-full-gamma-positive-repairs-and-independent-budget-gap.md)已经固定

\[
 W_\zeta=W_\Gamma+H-P,\quad H=2\cosh(u/2)du,
\quad P=\sum_{n=p^k\ge2}\Lambda(n)n^{-1/2}
 (\delta_{\log n}+\delta_{-\log n}),
\]
\[
 G_R=W_\Gamma+\phi_R(H-P),\quad g_R=\widehat G_R,
 \quad q_R=(-g_R)_+,\quad c_R=\|q_R\|_\infty,
 \quad m_R=\|q_R\|_1/(2\pi).
\]

原Γ为 \(\Re\psi(1/4+it/2)-\log\pi=2\theta'(t)\)，指定FP/contact保留；\(\phi_R\)是已固定的非负正型自相关窗，R为算术截断，物理半窗L、频高T另记。所有proper powers仍用 \(\Lambda(p^k)=\log p\)，不把 \(\phi(k\log p/R)\)冒当某一primitive权的k次幂。

[578(3)](../../../notes/578-prime-pole-signed-budget-and-selberg-control-gap.md)给实际同源重写

\[
 E(u)=\Psi(e^u)-e^u+1,\quad A(u)=e^{-u/2}E(u),\quad E(0)=0,
\]
\[
 g_R(t)=\Gamma(t)+J_R(t)+S_R(t),
\quad J_R(t)=2\int_0^R\phi_R(u)e^{-u/2}\cos(tu)du\ge0,
\]
\[
 S_R(t)=2\int_0^R A(u)
 \left[(\phi'(u/R)/R-\phi(u/R)/2)\cos(tu)
 -t\phi(u/R)\sin(tu)\right]du.
\]

目标是这份**完整线性量**的signed信息，或能独立运输到同一负部/逐compact卷积平方的净误差。\(J_R\ge0\)不使 \(\Gamma+J_R\) 自动非负；去掉E定义的+1会改变下端项。source为原physical \(r=e^{u/2}f\)，Fourier未归一、Plancherel为 \(1/(2\pi)\)，原du及zero-extension Dlog角色保持。

特别区分：577的 \(K_R=\mathcal F^{-1}q_R\) 是连续正修补；560/585的 \(K_L\) 是actual Sonin比较误差。585的 \(K_L[r]\to+\infty\)及 \(K_L[r]/t_L(r)\to1\)不运输为 \(q_R\) 的lower，不能用它排本门的正D′路线。

## 2. 最强已付与真正未付

577已有每层正证书 \(V_R=G_R+K_R(u)du\)，无新增δ/contact；裸层 \(G_R\to W_\zeta\) 于D′无条件。Γ窗化差
\((1-\phi_R)W_\Gamma=-\mu_Rdu\) 的du与Fourier-L¹均为匹配 \(O(R^{-2})\)，这是独立已付费用，不是 \(q_R\) 小量。

fixedL全complex原源已有

\[
 |Q_{V_R}(r)-Q_\zeta(r)|
 \le[D_L/R^2+\min(c_R,2Lm_R)]\|r\|_{du}^2,
 \quad D_L\ll(1+L^2)e^L.
\]

实际 \(q_R\) 的独立消失预算仍未付；对这个**特定family**，577已核
RH ⇔ \(c_R\to0\) ⇔ \(m_R\to0\) ⇔ \(K_R\to0\)于D′，包括cofinal子列版本。这个等价不禁止独立证明，但“负部趋零/正型锥membership/临界domination”本身不是新输入。目标也可按每个compact complex卷积平方的实际修补值来验收；不应无故强加逐层消noncompact405、ordinary trace或全线uniform原norm。

578已付PNT/普通Selberg/Euler平方的准确类型与具体粗包反测。old 542＋555→557 whole4/5仍仅负惯性UPPER；新585 actual Sonin必要费也不是本 \(q_R\) 的预算。不能将这几项互相换名作为候选来源的新后果。

## 3. 本地原陈述/章节去重表

以下仅恢复既有 source-audit/manifest 的实际已审范围，**不称本轮再次读原PDF、目视或认证全文**。部分历史PDF缺失与已审状态分开；现场状态沿本日 core-source-location/local-source-dedup及fixed-test-lower来源记录，不在本门重下载修复。

| 原来源/版本与本地证据 | 已实际审到的原陈述/章节 | 为什么不自动成为本门新 Γ-signed 输入 |
|---|---|---|
| Selberg，*An Elementary Proof of the Prime-Number Theorem*，Annals50(1949),305–313；[578历史来源稿](../../2026-10-22/prime-pole-signed-admission/history-and-source-admission.md) | §2／印页307–310，特别309页(2.8)/(2.9)：有序prime产品总量；补幂后 \(\sum\Lambda(n)\log n+\sum_{mn\le X}\Lambda(m)\Lambda(n)=2X\log X+O(X)\) | 控制和频/乘法卷积，非原 \(g_R\) 的Hermitian负部；完整O(X)总量＋PNT/positive primitive/FE已被578具体nativeΓ=0正负两族联检区分。只排该粗包，不排新twist或经典Γ协同 |
| Saffari–Vaughan，*On the fractional parts of x/n and related sequences. II*，AIF27(2)(1977),1–30；notes003 source35/169来源范围 | Lemma5 的(6.4) uniform multiplicative Selberg variance采用RH前件；另有zero-density条件下long-interval版本 | 不能把conditional平方根/polylog profile写成无条件临界signed费；169/299在本项目指定匹配截断中另核了相关RH强度，截断不同不得无声搬定理 |
| 标准PNT包络；[578累计误差稿](../../2026-10-22/prime-pole-signed-admission/cumulative-error-and-original-cost.md)及同历史来源稿的294/299对照 | 先fixeda的 \(\Psi(x)-x\ll x e^{-a\sqrt{\log x}}\)与端点匹配Abel运输；未以本轮优化新常数 | 对S_R取绝对值只付增长upper及额外 \(|t|\)/H¹费，未付同一负部消失。全局平方根误差本来有RH强度；不能误报“它不能推出RH”，也不恢复暂停的零自由区优化 |
| Connes，*Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*，math/9811068v1；manifest中Connes-1998-trace | 既有404–421审查：finite-S cutoff/普通迹域、AppendixII主值正规化、PDF69–74、76–78 Th6完整显式公式；固定FP/contact已反复核 | 完整身份与其RH/正性判据属于已付接口，不能由“explicit formula”标题取得独立好号；须指出新命题对本S_R或q_R多付的signed方向 |
| Connes–Consani，*Weil positivity and Trace formula, the archimedean place*，2006.13771v1，与55页Selecta作者稿分开；[C004原审](../../2026-10-13/c004-sonin/source-audit.md) | 55页作者稿Th1/Th4.6/Th6.11、AppendixB；v1 trace编号为4.7。全测试trace身份可用，差的有利号有小支持/消失条件 | 不删这些条件扩成完整Γ＋全部prime全源正性。旧535/560已核真实prime比较；Sonin正trace不是577负部修补的同一对象 |
| Burnol，math/9901051v2；[C015原审](../../2026-10-14/c015-admission/original-scattering-and-grade-audit.md) | 17页非arch地方scattering；VII/VIII/IX/X，positive time-delay \(T_p\)、conductor \(H_p=\log p-T_p\)、graded local trace明确区分 | 单地方正号不付经典实位Γ、两pole及共同跨prime signed预算；正Euler/Poisson平方本身已扣旧 |
| Connes–Consani–Moscovici，2310.18423v2；本日core-source-location本地排重及旧C005来源稿 | Th4.6/Prop4.7/4.8及§4.8：finiteS同构、mixed pairing、entire空间，范数依S；真实投影保Gram逆 | 不把Hilbert同构当酉或Weil正性。585已消费的actual fixedsource trace lower是另一费用结果，不能据此获得577的q_R小量或续sharp/后章 |
| Connes–van Suijlekom，2511.23257v1／CMP406:312；CCM，2511.22755v1；[10-12逐版本审计](../../../literature/supplements/2026-10-12-connes-recent-paper-audit.md) | 前者§4–6、Th6.1/Rem4.3；后者§3–5/7–8、Th3.6/5.10与Lemma7.3 | 原最低值单重/孤立/偶与实际结构是输入；减最低值的正商型不是原Q非负；实际最低态与prolate/Ξ强逼近仍欠。不能靠全实零点/positive quotient标题重开 |
| Connes，2602.04022v1／JOMP2026；同10-12审计 | §6.6、§7.2/7.4/7.5：最低态缺口、小支持实位正性、半局部算子非自动正投影、heat展开的RH前件 | 是已审策略/条件接口，不是本门未审新估计；不把RH条件heat式反用为无条件Γ协同定理 |
| Barner，*On A. Weil's explicit formula*，JRAM323(1981),139起；ALKL2402.06671v2；[569固定来源记录](../../2026-10-20/dual-gamma-cocycle/dual-conormal-source-record.json) | Barner只有publisher metadata和p146损坏OCR，精确finite-part原式未消费；ALKL特定normal/dual/b-trace页已读；DLMF5.9.E12/E16供独立Γ校准 | Barner是实在的未审规范点，但尚无已定位的本g_R signed小量命题。569已有实际L¹修补，不能把待核规范说成新的负部estimate，也不能静默指定隐藏约定 |
| Zhu，2608.24827v2，2026-09-02；[C008来源范围](../../../literature/supplements/2026-10-14-zhu-compact-window-entry.md) | 摘要/§1.2/14/17及后续原PDF/source包准入；所需matrix/errorbook/frame/trial/verifier原附件未取得 | compact-window数字/simple排序仍cited/open，C008止损；标题中的positivity/Landau–Widom不付本R→∞负部预算。537独立已消费的fixed窗证书也不升级成长 |

与表中原命题相连的**本项目标准/旧组织**还须扣除：

- [578平方审查](../../2026-10-22/prime-pole-signed-admission/square-identities-and-controls.md)已明确 \(U^2\) 与 \(|U|^2\)、和频与ratio差频、contact增量的区别。正Euler/Toeplitz只给 \(|P_R(t)|\le P_R(0)\)等保留指数大项的不等式；没有和完整Γ/pole的独立相消。
- 576有限FF正原料的D′闭包、174正锥/存在性组织、577取负部规则，均不提供经典membership。真实函数域的全Gram正性来自已付同对象RR/极化，不能只搬点数总量或删period aliases。
- 553的global原norm关系根门与每fixed强源/D′量词不同。不能因为577各层不exact消noncompact405，就泛排不逐层下降的正逼近；也不能用compact交集空洞检验全Pan。

## 4. 若root新命中候选，必须多核的差

本地去重不是按题名判失败。即使命中已知作者/主题，只要出现此前未审的实际signed命题，仍按下列最短字典核是否有净新输入：

1. **实际目标与系数方向。** 原命题究竟控制 \(S_R\)、\(g_R\)、\((-g_R)_+\)，还是另一正核/谱算子的负部？需要的是本 \(P_R-\Gamma-H_R\) 的超额或逐source修补费用，不能把正迹/正 \(J_R\) 当成该方向。
2. **完整规范。** 原Γ是否真为2θ′及指定FP/contact，全部 \(\log p\,p^{-k/2}\) 权与双pole/端点是否保留？Γ窗化μ_R的O(R⁻²)已经付清，不能当作新q_R estimate。另一L函数/局部Γ或更换contact须实际运输。
3. **源、norm和量词。** 区分每fixedcompact complex源、fixed窗ALL源、L(R)成长、全t/负部积分和height平均。直接Abel导数费是H¹，不免费变du/Dlog；一个固定frequency区间、离散网格或平均二阶矩，若无完整补区/尾，不能当c_R或m_R。
4. **独立前件。** 原结论是否假设RH/临界线零点、未知正型membership、已足强的negative-part控制或原最低态识别？等价性不妨碍未来独立证明，但原命题只重述等价条件时，没有新已付款的输入。
5. **净后果和许可范围。** 至少说明相对577/578已付部分多控制了哪个actual signed量，如何进入fixedsource净误差或某个真实成长范围。不强求原命题一步解决RH，但没有具体运输/误差的新箭头就只存定位，不准数学。不能用585的另一个K、whole4/5UPPER或新的正Gram填此空。

如果新命题只给全 \(q_R\) 小量的条件刻画、普通Selberg/PNT、全纯Euler平方、已审最低态或半局部正迹，本地排重应在此止；不去其引用链寻找替代章。若确给原规范下新的twisted/Γsigned信息，就保一份固定原文和一个具体待审命题，不因摘要/平台评价先消费证明。

## 5. root本轮唯一近邻：Nakamura固定v1的本地排重

root通知本轮全部外网预算已经执行：两批共六query；有效的其他命中回到既有Scaling Hamiltonian1910.14368和CC2006.13771，数值零点或conditional/无关来源不入型。此处只记录root报告，不把它算成本分支执行的外网检索，也不追加query。

唯一待核近邻为 Takashi Nakamura，*A complete Riemann zeta distribution and the Riemann hypothesis*，arXiv1504.03438v1。root本轮固定的原HTML在
`literature/local/2026-10-28-gamma-signed-location/nakamura-1504.03438v1.html`，422428 raw bytes，SHA-256
`8f7227f22d1c3c849b7ec6fa3c8a0ee1bcbdee53fb5482d3b0bb27074de46f0d`。

本分支对 `1504.03438`、作者、完整题名、`pretended-infinitely`、`quasi-infinitely/quasi-ID` 的本地精确检索，未命中此前 notes/goals/literature/reviews 的来源消费记录。检索当时只出现本轮另一支持稿的Nakamura locator及这个刚保存的HTML；二者不能反算为历史已审。root亦独立报告其全仓指定关键词检索无旧命中。故它是**本地未审的新定位近邻**，不是又一份旧Connes来源；不据此主张世界新颖性。

本稿不自行打开该HTML数学正文或§2 proof。root明确报告其实际已读范围仅为§1.2定义和§1.3 Theorems1.1–1.4陈述；相关 characteristic-function 正性、log-Lévy signed结构和临界带RH等价性质已经区分，尚无独立q_R消失命题。该根本区别与本地旧资产吻合：

- \(\xi(\sigma-it)/\xi(\sigma)\) 的概率特征函数正性，不能只凭“positive definite”就等同 \(W_\Gamma+H-P\) 的原source平方正性；要先核究竟是ξ本身的变换还是其log/导数所携带的prime／Γ／pole量。
- infinitely-divisible、quasi-infinitely-divisible、pretended-infinitely-divisible不能互换；若原陈述用RH等价的临界性质，仍不能将该性质当成独立算术预算。
- 即使得到明确signed Lévy公式，它与577/578的完整固定窗/Γ/contact/powers/poles身份之间仍需实际字典和误差方向；一个新exact identity并不自动给负部的小质量、逐source修补消失或原du/Dlog净费。

因此本地“无旧同篇消费”不等于“已获得入型新estimate”。root当前准备按无合格命中停止本次有限定位；本稿只提供去重与靶式差异，**不**为此指定§2下一proof门、另找paper或扩搜索。source0止不表示Nakamura结果为假，也不证明Γsigned路线不可能。

## 6. 实际搜索范围、当前结论和交还

本轮本地用rg定位 literature现有索引/manifest相关标题、既有supplement与578三分支来源记录；重点实读577/578靶式、Selberg历史稿/平方稿、10-12 Connes版本边界及569来源记录。notes003仅核所列原来源条目与conditional status，未恢复早期暂停的比例/零自由区研究。没有全仓重推理论，没有新PDF页/网页/下载/渲染或数值进程。

在这些本地记录及root本轮交付的唯一近邻陈述范围内，尚无独立新命题已经支付完整Γsigned负部或正修补消失。它是有限库存/定位判断，不是全球无定理或路线不可能性的结论。§5仅补本轮Nakamura的local novelty及必要运输差，不外网代root扩大检索。当前不指定新章，不预C049/586、不续C048/作者后章/二维trial建议。无pending process。
