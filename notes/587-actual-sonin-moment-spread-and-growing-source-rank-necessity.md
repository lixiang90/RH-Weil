# 587：Actual Sonin源矩量共同下界与补偿秩增长必要性

2026-10-28；C050，同G20261027/runtime1793085111/冻结0c4f。两独占证明及当前fresh终稿已root全文核、对齐前件并限定消费。本轮新增的是同一实际核上对移动源系数同时有效的矩量下界；585逐fixed源lower、Gaussian范数工具和辅助线代不另计轮。

## 1. 结论、实际对象及量词

沿560/585原物理空间 `H=L²(du)`、Sonin投影P及M=RanP，保

\[
 B_X=\prod_{p\le X}(I-p^{-1/2}U_{\log p}),\quad
 \Pi_X=B_XP(PB_X^*B_XP|_M)^{-1}PB_X^*,\quad
 A_r=\int r(u)U_u\,du.
\]

Π_X为实际正交投影，完整Gram inverse/returns不删，B_X不当作酉。原physical `r=e^(u/2)f`、Fourier `rhat(t)=∫r(u)e^(-itu)du`、Plancherel dt/(2π)保持。实际正迹为

\[
 t_X[r]=\operatorname{Tr}(A_r\Pi_XA_r^*)
       =\int|\widehat r(t)|^2\rho_X(t)\,dt;
\]

ρ_X已含原求值规范，最后一式不再添除2π。finite-X普通迹/HS域为560已付输入。

固定 `r₀(u)=c exp[-1/(1-u²)]` 于|u|<1，外零，c使du norm1。support为[-1,1]，全部端点jets为0。对每个**先固定**整数d≥0，令

\[
 E_{d+1}=\operatorname{span}_{\mathbb C}\{r_0,r_0',\ldots,r_0^{(d)}\}.
\]

则存在依d及固定数据的c_d>0、X_d，使对所有X≥X_d及**全部complex系数**z（允许随X变）有

\[
 \boxed{t_X\!\left[\sum_{j=0}^dz_jr_0^{(j)}\right]
 \ge c_d\frac{\sqrt X}{(\log X)^{3d+2}}\sum_{j=0}^d|z_j|^2.}\tag{1}
\]

各固定源组的du/zero-extension Dlog基Gram固定正定，故(1)换成E_(d+1)原范数只改固定常数。没有d_X成长uniformity，也没有全源单位球lower。

三源的actual moment `m_j=∫t^(2j)|rhat₀|²ρ_Xdt` 给

\[
 G_X=\begin{pmatrix}m_0&0&-m_1\\0&m_1&0\\-m_1&0&m_2\end{pmatrix}
 \succeq c\frac{\sqrt X}{(\log X)^8}I_3,
 \quad
 \boxed{\mathfrak D_X:=\frac{m_0m_2-m_1^2}{m_0+m_2}
 \ge c'\frac{\sqrt X}{(\log X)^8}\to\infty.}\tag{2}
\]

偶性来自原P/B及其逆的实结构，非“正密度所以偶”；导数Fourier因子it给02项的负号。偶块小特征值λ_-满足𝔇≤λ_-≤2𝔇。

## 2. 辅助Gaussian范数与真实trial的全线比较

记ℓ=logX、A=√X/ℓ，`D_E(t)=∏_(p≤X)(1-p^(-1/2-it))`、w_X=|D_E|²。复用585已付H₀：H₀(0)≠0、Gevrey全尾，全部有限complex polynomial倍都在同一真实Sonin域。真实trial向量始终为D_E pH₀。

仅作辅助多项式范数的测度是

\[
 d\mu_G=w_Xe^{-t^2}\frac{dt}{2\pi},\qquad
 d\mu_H=w_X|H_0|^2\frac{dt}{2\pi}.
\]

Gaussian没有被放进Sonin空间，两测度也不是actualρ_Xdt。选固定δ>0使H₀及h=rhat₀在|t|≤δ有正模lower；固定c>0足小，N=⌊c A/ℓ⌋。Gaussian腿证明：对deg q≤N+2的全部complex多项式，

\[
 c_H\|q\|_G^2\le\|q\|_H^2\le C_H\|q\|_G^2,
 \qquad
 \int_{|t|>\delta}t^2|q|^2d\mu_G\le\varepsilon_X\|q\|_G^2,
 \quad\varepsilon_X\to0.\tag{3}
\]

费用链是旧Legendre(P)分别积分Gevrey/Gaussian全线矩，再用J_X上Euler权lower与δ外固定exponent gap；中段t²付X⁴因子，由logX=o(A)吸收。|t|>X²分别以e^(-t²)和H₀的e^(-c√|t|)吸收全部degree/Euler前因子，未外推只在|t|≤X²有效的算术渐近。最后结合core权比才得全线norm等价。详独占Gaussian稿§§2–4；(3)不由未加权概率集中省略得来。

## 3. 曲率与finite核Jacobi lower

在μ_G中取real正交规范多项式p_n。even权给

\[
 tp_n=a_{n+1}p_{n+1}+a_np_{n-1},\quad a_n>0,\ a_0=0.
\]

V=t²−logw_X的全实线曲率由exact有限Euler级数控制：

\[
 |V''|\le2+2\sum_{p\le X}(\log p)^2
 \frac{p^{-1/2}}{(1-p^{-1/2})^2}
 \le\Lambda_X:=C\sqrt X\log X=C A\ell^2.\tag{4}
\]

这里只需Chebyshev θ(y)≤Cy及分部求和，未优化零自由区。Gaussian全矩与V′至多线性加逐fixed-X有界项保证IBP边项及下述finite-rank核的HS域。对到degree<n的投影P_n，

\[
 \langle V'p_n,p_{n-1}\rangle=n/a_n,
 \quad
 \|[V',P_n]\|_{HS}^2\le\Lambda_X^2\|[t,P_n]\|_{HS}^2
 =2\Lambda_X^2a_n^2.
\]

不调用抽象operator-Lipschitz定理：commutator的实际finite核为 `(f(t)-f(s))Σ_(j<n)p_j(t)p_j(s)`，点态Lip界足够。左侧两个矩阵元的平方和至少2n²/a_n²，所以

\[
 a_n^2\ge n/\Lambda_X.\tag{5}
\]

另一方面(3)给对n≤N+1的a_n²≤C₀，常数固定；这付了另一方向的tail费用。

## 4. Fixed-degree三角路径与实际运输

先fixed d，取ceil(N/2)≤j<N−d及P(t)=Σ_(ℓ≤d)c_ℓt^ℓ。t^ℓp_j投到p_(j+k)的每条有效Jacobi路径都含a_(j+1)…a_(j+k)。提出这些mandatory edges后没有小分母；其余有限路径因子由C₀控制。因此投影系数矩阵为diag(A_(j,k))乘一个diag1的upper triangular矩阵U_j；U_j及inverse由fixed d控制，且(5)给A_(j,k)≥[N/(2Λ_X)]^(k/2)。

由此

\[
 \sum_j\|Pp_j\|_G^2
 \ge c_dN(N/\Lambda_X)^d\sum|c_\ell|^2
 \ge c'_d\frac{\sqrt X}{\ell^{3d+2}}\sum|c_\ell|^2.\tag{6}
\]

所用j数≥N/3，且deg(Pp_j)<N；**原N+2范围已经足够**，不另加成长degree前件。源导数的因子i^ℓ只改coeff unitary相位。

令v_j=D_E H₀p_j，真实frame Gram H满足c_HI≤H≤C_HI。到其span的真实投影为 `Q=V H⁻¹V*≤Π_X`，不能省逆。普通正迹比较、h在core的lower与(3)给

\[
 t_X[r]\ge\operatorname{Tr}(H^{-1}B_r)
 \ge C_H^{-1}\sum_j\|A_rv_j\|^2
 \ge c_T\sum_j\|Pp_j\|_G^2.
\]

所有求和有限，A_r的ordinary trace/HS准入是原物理域，非Gaussian基的形式迹。合并(6)得(1)，d=2得(2)。这是actual源系数共同下界，没有将585逐fixed源起点用compactness偷换。

## 5. 完整K与固定秩补偿的准确边界

所有X用fixed I=(-17/16,17/16)，大X覆盖全部可见prime后，完整mixed式给

\[
 K_X^{E_{d+1}}=G_X^{E_{d+1}}-Q_W^{E_{d+1}}+P_{pole}^{E_{d+1}}.
\]

Q/P是fixed有限矩阵，完整Γ=2θ′/FP-contact、全部Λ(p^k)=logp和双pole的正负号均保；不施pole-zero条件。故原du或Dlog的压缩最小特征值至少

\[
 c_d\sqrt X/(\log X)^{3d+2}-C_d.\tag{7}
\]

对任意共同Hermitian**源型**补偿R_X，若rank R_X≤d，压缩到E_(d+1)仍有kernel单位向量，因而残差压缩operatornorm至少(7)。允许系数/norm成长、range移动/非局部、有符号；receiver-trial projection的rank与源型rank不同，不混用。

若所有先fixed源都有 `(K_X−R_X)[r]=O_r(1)`，预先固定的(d+1)²个复极化测试已迫整个压缩矩阵有界，矛盾。更强的同链必要条件是：对每X有限秩的这种共同补偿，**其秩必须趋于无穷**，不能仅在一条子列上保持有界；否则沿该子列用相应fixed d仍矛盾。没有给秩增长率，也没有排除成长秩。

由同一压缩和min–max，对每个先fixed j≥1，K_X的第j个正本征值也有c_j√X/(logX)^(3j−1)−C_j的充分lower；j=1、2另保585/偶奇旧链中已有的更强scalar rate，不将此较弱特例冒作改进。

成长秩逃逸确非空：560已付每fixed-X、fixed-I的K_X自伴紧，按|λ|>1保留其有限谱项得到有限秩R_X，且||K_X−R_X||≤1。它的rank由本结论必趋∞。这只是旧谱截断的合法性/范围对照；依赖完整K本身，不提供独立算术正性或有利signed净差，不作为新研究输入。

另一个不能混用的rank角色是receiver投影：即使receiver E=|v〉〈v|只有rank1，其诱导的源型是C_E(r,s)=∫rhat·conj(shat)|vhat|²dt/(2π)。非零L²向量的权在正测度集非零，固定bump的Fourier零集离散，所以每个有限导数源Gram都正定；该源型rank为无穷。故本结果不按receiver rank排除旧EX/fullgap机制，它们只受各自原停门约束。

## 6. 强旧、瓶颈与结算

旧585给每个fixed非零源的scalar lower；旧EX反测给特定扣项两对角成长。它们未支付moving source coefficients的共同moment-spread。弱前件even双原子模型虽使全部fixed测试发散，却给𝔇有界，说明不能仅凭这些scalar结论报本结果；该模型不满足actual Sonin完整字典，也不否定旧ALLpoly设施。

本轮新增是Gaussian全线比较/finite核Jacobi lower/实际frame运输合成后的actual共同费用。局部瓶颈改变：固定上限源秩的修补已不能留下全部fixed源的有界残差。仍欠成长秩/有费无限秩中的独立完整signed净号，以及primitive/principal/整过滤/截面乘法/mixed、全corecross与Ξ；whole542+555→557 leading4/5仍仅负惯性UPPER。

C050统一一数学轮，预算耗尽；辅助lemma、fixed-degree同链推论、准入/审稿不另计。Goal同实例active/open/noteligible，本结果不完成长期Goal或提供RH证明。原证明、当前fresh、root前件闭合及版本绑定见 `reviews/2026-10-28/sonin-moment-proof/`。
