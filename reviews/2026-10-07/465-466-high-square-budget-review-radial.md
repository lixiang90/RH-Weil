# 465–466 高平方残差预算与实际交换子阻断的独立全文审查

2026-10-07。radial_review。结论：联合限定 PASS。
465的有限预算正确；466的实际正下界排除了465保留的反事实小残差门槛。
最终稿已明确二者的差别，没有实际比例提高。
本次只新增本审查，不修改被审notes、已冻结旧稿、math或Git。

## 1. 最终全文与输入

canonical LF按CRLF/lone CR统一为LF、不trim计算：

| 被审全文 | SHA-256 | UTF-8 bytes / 行 |
| --- | --- | --- |
| [465](../../notes/465-centered-high-square-joint-fourth-budget.md) | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 | 10069 / 272 |
| [466](../../notes/466-high-square-variance-commutator-obstruction.md) | 0b955bdc26b4bf950ce457dec7bf18f635f702d85a73d73c8d6263df969cbbbe | 8013 / 243 |

全文另核454、455、461、462、452及197/228的实际接口。
454原weighted二矩与462low4无需新的无零输入；
461整个13小量依赖其明列conductor-one fixed-gap [R]；
452的短padding引用已交付全族条带及明确[R]，未在本次重证分析内核。
197/228只作同配置的一侧中心偶矩蕴含，不调用旧开放prime-side链。
未修改math或将另一数域合同搬入。

## 2. 465的原加权二矩：middle投影与极化

\(w_{\mathcal L}\)为非负原high同素数diagonal，
\(\sum_Hb_p^2=O(1)\)给sup界；
乘法求导的L1界均由原taper及该正质量支付。
函数及导数在两端为0，原圆周Fourier泄漏计算适用。

令\(G_R=QB_RE\)。物理middle-weight二矩的展开为
\[
 (B_RE)^*M_w(B_SE)
 =C_RW C_S+C_RE^*M_wG_S+G_R^*M_wEC_S+G_R^*M_wG_S .
\]
因\(G_R,G_S\)落在原\(Q\)中，前两个crossing准确含
\(QM_wE\)，并由两HS因子与一个bounded op因子给作者(6)。
HH费用\(O(X\log(2+\mathcal L)/\mathcal L^2)=o(d)\)；
HL、LL更小。没有把未知H4有界用于此比较。

物理对角中的weight最初位于中间点\(u+s\)；
变量代换及两个sign的重排把它写成
\(\langle w\,d_R\rangle\)，因此HH、LL常数分别为\(S_\psi,C_\psi\)。
全部cross primes用454原差频Hilbert、remainder与和频alias付款。
对同一\(B_H+zB_L\)取\(z=1,i\)的bilinear极化合法，
没有新系数或新窗。HL没有同素数对角。
有限\(\operatorname{Tr}WHL\)与\(\operatorname{Tr}HWL\)互为共轭，
所以两个都为\(o(d)\)。\(W^2\)与multiplication-square的差为
\(\ell_w^2=o(d)\)。465(4)全部成立。

## 3. 465有限预算与条件极限

\(\Gamma=H^2-W\)是真实selfadjoint残差。
精确平方展开与已付bounded-weight二矩给
\(a_T=S_\psi+q_T+o(1)\)，该误差没有乘未知增长因子。
作者(10)来自HS Cauchy，对非selfadjoint\(HL\)仍合法；
\(s_T=\operatorname{Tr}WL^2/d\ge0\)，故\(u_T\ge0\)。

finite fourth展开保留原全部31、22、signs和labels。
\(|\operatorname{Tr}HLHL|\le\operatorname{Tr}H^2L^2\)
给作者(12)，包括准确的\(t_T,\eta_T\)绝对误差。
该式逐T成立，未先假定q bounded。
仅在明列\(\limsup q_T\le Q<\infty\)后，
紧域连续性才支付(13)的固定常数预算。

flat的\(d_H,d_L,S,C,e\)独立积分一致：
\(S=19/480,C=23/960,e=19/240\)。
455的S4-small与454 flat背景误差只在whole prime fourth已bounded后使用。
因此centered response、原zero-side padding及197/228一侧LP接口的顺序正确。
反事实有理根号界与\(32000/47301>27/40\)也都正确，
但最终465明确这些前件已经被466排除；没有将其登记为实际比例。

## 4. 466严格PSD不等式与finite误差

在H特征基中，\(\Gamma\)对角为
\(\Delta_i=\lambda_i^2-W_{ii}\)，offdiagonal为\(-W_{ij}\)。
所以qdiag/qoff分解准确。
\(W^2\le MW\)给
\(r_i\le w_i(M-w_i)\le M^2/4\)；
未假设\(\Gamma\)为PSD。
对称求和及\((\lambda_i-\lambda_j)^2\le2(\lambda_i^2+\lambda_j^2)\)
给
\[
 K\le4Mq_{\rm off}+M^2\,\mathbb E\Delta^+
 \le4Mq_{\rm off}+\frac{M^2}{2}\sqrt{q_{\rm diag}}+\frac{M^2\mu}{2}.
\]
完成平方的顶点为\(\sqrt{q_{\rm diag}}=M/16\)，
常数正是\(M^3/64\)。466(4)逐finite矩阵正确，不含未知增长误差。

flat untapered diagonal的uniform Mertens上界为
\(3/8+o(1)\)；原taper只减少该非负乘法函数，normalizer趋1。
实际\(\mu_T=\operatorname{Tr}\Gamma/d=o(1)\)由原high二矩支付。
这里无需q或high4有界。

## 5. 实际commutator二矩与系数

466(10)准确保留两个原Q-crossings，
HS误差为\(O(m_H\sqrt{\log(2+\mathcal L)})=o(\sqrt d)\)。
新shift coefficient含
\(\phi(u)\phi(u+s)[w(u+s)-w(u)]\)，其sup、C2及零延拓边界
满足454同一有限Fourier/Hilbert估计；
乘积求导所需常数统一于原prime steps。
这也支付\(QC_{\rm phys}E\)的HS泄漏。

物理二矩本身先由全部差频、和频及alias项得到\(O(d)\)，
才把norm-square传给actual；不使用未知high4反证其HS有界。
本次独立核全部sign对角：
对\(x\in[1/2,1]\)、\(t\in[x-1/2,1/2]\)，
\[
 D(t)-D(x-t)=(x+1)(t-x/2).
\]
两个sign乘该中心对称区间的平方积分给
\[
 K_1=\frac16\int_{1/2}^1x(x+1)^2(1-x)^3\,dx
 =\frac{41}{10080}.
\]
这是整个actual commutator的极限，不是受限正子和。

## 6. 实际阻断、粗envelope及最终scope

由严格finite PSD界直接得
\[
 \liminf q_T\ge
 \frac{41/10080-(3/8)^3/64}{4(3/8)}
 =\frac{33479}{15482880}>\frac1{1600}.
\]
若liminf无穷无需另论，否则沿有界达到子列取极限；
不先假设全列bounded。
全部fraction积分、差额及466(16)–(17)的有理根号方向经独立复算一致。
粗465预算在该下界处已经大于\(1/3\)，所以其旧小q付款目标确实不可追求。

最终两稿限定PASS包括有限联合预算、实际结构下界及主动撤回旧目标。
它们没有证明whole fourth足够小；不排除保留low/high残差协方差、
entire13正交及22负commutator后的更精确联合预算。
目前没有新的实际简单零点比例、无零边界或RH/RR结论。

## 7. 最终466新增§5：sharp \(4M\) 界的独立复核

最终全文保留§1–4的正确粗界，并新增无需首迹误差的更强PSD界。
仍在H特征基中，写 \(w_i=W_{ii}\)、
\(r_i=\sum_{j\ne i}|W_{ij}|^2\)、
\(\Delta_i=\lambda_i^2-w_i\)。
对任何实 \(\Delta_i\)，Young不等式准确给
\[
 \Delta_i r_i\le M\Delta_i^2/4+r_i^2/M .
\]
这里M正；M=0时W=0且K=0直接处理。
由 \(0\le W\le MI\) 得 \(r_i\le w_i(M-w_i)\)，故
\[
 w_i r_i+r_i^2/M
 \le(2w_i-w_i^2/M)r_i\le M r_i .
\]
于是对每个finite矩阵，
\[
 K\le4\,\mathbb E[(w_i+\Delta_i)r_i]
 \le Mq_{\rm diag}+4Mq_{\rm off}\le4Mq .
\]
这个推导不用 \(\operatorname{Tr}\Gamma=o(d)\)、q bounded或high4先验。
系数4的sharpness由作者的二阶矩阵直接核准：
\(W=\begin{pmatrix}M-\epsilon&\epsilon\\\epsilon&M-\epsilon\end{pmatrix}\)、
\(H=\operatorname{diag}(\sqrt{M-\epsilon},-\sqrt{M-\epsilon})\)。
取 \(0<\epsilon<M/2\)，W的特征值为M和 \(M-2\epsilon\)，
\(q=\epsilon^2\)、\(K=4(M-\epsilon)\epsilon^2\)，因此比值趋 \(4M\)。

结合§5已付的actual \(K_T\to41/10080\) 与
\(M_T\le3/8+o(1)\)，得到最终更强结论
\[
 \liminf q_T\ge\frac{41/10080}{4(3/8)}
 =\frac{41}{15120}.
\]
它同时排除 \(Q=1/1600\) 与 \(Q=1/400\)，
后者差额为 \(41/15120-1/400=1/4725>0\)。
§6所列旧有理下界仍真，但不再是当前最强actual必要条件。
不能把被排除的 \(Q=1/400\) 当作可追求的实际付款目标。

最终联合限定PASS绑定上表最终全文，包括这项新增强界。
它没有支付新的q上界、high/low交换子下界或实际比例改进；
比 \(41/15120\) 更大的候选Q只是不被本不等式排除，仍须原算术证明。
