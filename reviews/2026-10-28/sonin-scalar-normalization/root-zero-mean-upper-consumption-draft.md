# (6.11)最短消费链：root独立局部化核对稿

2026-10-28；D20261028AJ唯一来源门。Root已实际读固定v2原件667–782、784–869必要段及两具体准入终稿，未读6.4sharp proof／6.5／后章。本稿不是sourceproof已通过的结算：当前upper/tail与localization两独占审尚在途，以下A/B接口在根最终对齐前conditional。原Γ/contact/pp/双pole仍属完整target，不由这一正迹上界删除。

## 原对象与两个接口

f为先fixed compact smooth complex物理log卷积源，F(t)=∫f(u)e^(-itu)du；actual T_X仍为完整Euler-Gram正交Sonin投影的普通迹。设L=logX、A=√X/L、s_X=√X/L²。源与raw arch evaluator h不同。核k_X按dt/(2π)表示，所以T_X[f]=∫|F|²k_X(t,t)dt/(2π)；它与560的ρ_X仅相差这项归一化，不再多扣2π。

接口A：加权arch源空间h的norm为||D_X h||₂（D_X是此原件finite Euler乘子），其unit ball满足全complex disk统一评价

\[
 \sup_{|z|\le R}|h(z)|\le\exp(CR\log(R+2)),\quad R\ge2,
\]

C独立X。必须实际核raw entire性、Burnol completed/raw Gamma运输和Hardy／conjugation strip论证；若只得逐X常数，后面Taylor预算不能使用。Isometry到实际receiver为M_D G_X^(-1/2)，全Gram没有省略。

接口B：central实际trace mass O(s_X)及每fixed Schwartz F的tail ∫_(|t|>L)|F|²k_X dt/(2π)=o(s_X)。前者由A的Taylor截断singular值和log M_X=(2+o1)A得；后者须实际同S_X的平方支配及weighted commutator，不由trial子投影lower倒转得来。两接口为另一独占腿责任，本稿不把原文引用作付款。

## A＋已付Euler权如何给局部上界

固定小η>0。在一个fixed小区间内，Euler相位接近π的集合E_X有测度下界m_η>0（相位导数L+O(1)）；Lemma6.1的全uniform绝对误差给|D_X|²≥exp[(4−Oη)A]。故weighted unit ball的h在E_X上的L²值≤Cexp[−(2−Oη)A]。

对E⊂[-d,d]、|E|≥m，次数≤n多项式的L² Remez／Lagrange界为

\[
 \sup_{|z|\le T}|P(z)|\le C_m(C(T+d)/m)^n\|P\|_{L^2(E)}.
\]

用Chebyshev选出至少m/2测度的值有界子集，按累积测度quantiles取n+1点；点距≥cm|j−k|/(n+1)，Lagrange分母乘积含j!(n−j)!，故指数是O(n logT)，没有额外n logn损失。集合无需正则。

取R=A/(logA)³，n=ceil[(2+η)A/logA]，T=L^B（B先fixed）。由A的Cauchy余项，h减Taylor多项式在目标盘上的误差为exp[−(2+η+o1)A]；log C_R=o(A)，且n log(R/T)=(2+η+o1)A。在E_X上的误差乘上述插值放大后仍有同一负leading，因为n logT=O(A logL/logA)=o(A)。因此

\[
 \sup_{\|h\|_X\le1,\ |z|\le L^B}|h(z)|
 \le\exp[(-2+O\eta+o(1))A].
\]

先固定η再X→∞，η可按随后fixedδ选得足小。只需要这个upper，不需要(6.9)的lower或无共同零点断言。完整range kernel的对角为|D_X|²乘这个evaluation norm的平方；Lemma6.1中Re(e^(-itL)/(1−2it))的绝对值≤(1+4δ²)^(-1/2)，故每fixedδ>0有c_δ>0使

\[
 \sup_{\delta\le|t|\le L}k_X(t,t)\le e^{-c_\delta A}
\]

最终成立。这里源f不随δ/X变，δ只用于证明分区。

## (6.11)及当前实际规则的条件净后果

以B去掉|t|>L；以刚得exponential upper去掉δ≤|t|≤L，其积分为O_F(L exp(−cδ A))=o(s_X)。|t|<δ上只用sup|F|²乘central mass O(s_X)，所以

\[
 \limsup_X T_X[f]/s_X\le C\sup_{|t|<\delta}|F(t)|^2.
\]

此后令δ↓0，F(0)=0即给T_X[f]=o(s_X)。如果保原mass常数，右侧可取4|F(0)|²；当前fixed r₁首检不需要优化或消费sharp4。没有交换moving-source量词或把局部核指数信息外推全线。

若A/B及对象域由当前独占审／fresh闭合，取唯一r₁=r₀′的zero-mean upper与585已付T_X[r₀]≥c₀s_X组合，才得T_X[r₁]/T_X[r₀]→0。纯scalar规则α_X=q₀/T_X[r₀]于是W_X[r₁]→0而q₁>0。更一般，任何positive scalar β_X只要β_X T_X[r₀]→q₀，也给β_XT_X[r₁]→0；无source参数／新rank／anchor优化。

同一已付lemma的更强直接后果应如实消费：任意先fixed compact smooth complex r写作c_r r₀+z_r，c_r=(∫r)/(∫r₀)，∫z_r=0。由zero-mean upper及T_X[r₀]≥c₀s_X，T_X[z_r]/T_X[r₀]→0；实际正型的Cauchy–Schwarz给所有normalized cross项趋0。因此对全部先fixed源对r,s有

\[
 \frac{T_X(r,s)}{T_X[r_0]}\longrightarrow c_r\overline{c_s},\qquad
 W_X(r,s)\longrightarrow
 \frac{q_0}{|\int r_0|^2}\left(\int r\right)\overline{\left(\int s\right)}.
\]

这是全部fixed smooth源配对的rank1均值极限，不需6.4的sharp lower。没有从它自动升级到全部D′ test的拓扑收敛；本门拒绝完整目标只需固定卷积平方。不将spectral δ₀与physical u侧constant分布混同，且不声称未归一化T_X的exact leading4。

域/upper原proof未闭时上述结论保持conditional。不能将其冒作全signed/成长窗口/其它正D′规则边界；不单独消费receiver S_X strong0或normalized分布的完整D′极限。Goal门仍open，cadence原2/history52/latest588/formal17在root最终结算前不动。
