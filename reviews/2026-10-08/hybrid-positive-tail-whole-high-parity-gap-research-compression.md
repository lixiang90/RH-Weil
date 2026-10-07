# whole high平方残差的正尾项：无fourth增长前件的parity gap

2026-10-08。作者 compression_bridge。新完整推导，待独立全文审查。
root提出直接展开 τ(ΓUΓU) 保留PSD尾的路线；本稿进一步保留其正成本，
用一个scalar clip平方恒等式消元tail，去掉此前bounded-q或a=o(L²)前件。
只新增本文件；旧source、notes、审查、math、Goal与Git未改。

新whole实际结论（flat原profile，仍保留原endpoint taper）是

\[
 \boxed{\liminf_{T\to\infty}(q_T^{\mathrm e}-q_T^{\mathrm o})
          \ge \frac{41}{15120}.}                        \tag{1}
\]

这里 q_T=q_T^e+q_T^o是整个原finite高素数平方残差，无先验第四矩上限。
这是真正整个unknown的必要联合界；没有给q_T一个上界或新的零点比例。

## 1. 原对象与已付输入

原 X=T/(2π)、L=logX、d=floor(XL)、interval carrier E及P=EE*保持。
H=E*B_HE为整个原genuine high primes sqrtX<p≤X的Hermitian channel，
W=E*M_wE为同素数diagonal，J=M_sign(u)、S=E*JE、U=sgn(S)，
零特征值选+1，因此U*=U、U²=I。置

\[
 \Gamma=H^2-W,\quad \tau(A)=\operatorname{Tr}(A)/d,
 \mathcal E(A)=(A+UAU)/2,\quad\mathcal O(A)=(A-UAU)/2,
 \quad q=\tau\Gamma^2=q^{\mathrm e}+r,
 \quad q^{\mathrm e}=\|\mathcal E\Gamma\|_{2,d}^2,
 \quad r=q^{\mathrm o}=\|\mathcal O\Gamma\|_{2,d}^2.       \tag{2}
\]

所有S2 norms采用 ||A||_(2,d)=d^(-1/2)||A||HS。新的推导只对这些
actual finite matrices操作；未删除middle P或把U改成物理J。

| 完整冻结输入 | canonical UTF-8 LF SHA-256 |
|---|---|
| [actual high parity/Gram](../2026-10-07/hybrid-high-parity-gram-and-mobius-completion-research-radial.md) | 3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2 |
| [466 sharp finite commutator](../../notes/466-high-square-variance-commutator-obstruction.md) | 0b955bdc26b4bf950ce457dec7bf18f635f702d85a73d73c8d6263df969cbbbe |
| [原parity residual来源](../2026-10-07/hybrid-parity-resolved-residual-necessary-constraints-radial.md) | 6a5fb7db8467e80682d7351ee37a940af8d39de50fffe2f16b0b3a48d5dfc6f6 |
| [468基线](../../notes/468-original-mixed-cubic-and-parity-resolved-fourth-reduction.md) | ad4cf9f8bb4c77e24487b32434dc64d28162745adf3b1e0555b230be3953baf7 |

canonical只将CRLF及lone CR转LF，不trim。以上原输入已付

\[
 0\le W\le M_T I,\quad M_T\to3/8,\qquad
 K_T:=\|[H,W]\|_{2,d}^2\to41/10080,
 \quad\alpha_T:=\|H+UHU\|_{2,d}=O(L^{-1}),
 \quad\omega_T:=\|\mathcal OW\|_{2,d}
          =O(\sqrt{\log(2d)/d}).                         \tag{3}
\]

ω的费保持原有限投影：由J与M_w交换、原QJE泄漏、U−S缺陷，
||[U,W]||HS=O(sqrt(log(2d)))。没有将H二范数parity升级成H⁴的小量。
这些已付输入与下面finite代数不需要新的[R]合同。

## 2. fixed clip与通用finite commutator

任取R²>M，h_R(x)=max(−R,min(x,R))，H_R=h_R(H)，
Γ_R=H_R²−W、q_R=τΓ_R²、D_R=H²−H_R²≥0，t_R=τD_R。
R在本节是任意辅助数；不会改变原observable。

clip odd且1-Lipschitz，HS谱投影公式给
||H_R+UH_RU||_(2,d)≤α。谱投影重叠Tr(P_iQ_j)≥0保证此公式，
不用operator-norm Lipschitz黑箱。因此

\[
 e_R:=\|\mathcal O\Gamma_R\|_{2,d}\le R\alpha+\omega,
 \qquad \tau(\Gamma_R U\Gamma_R U)=q_R-2e_R^2.          \tag{4}
\]

同时466的finite估计对H_R,W直接适用：

\[
 q_R\ge K_R/(4M),\quad K_R=\|[H_R,W]\|_{2,d}^2,
 \qquad \sqrt{K_R}\ge(\sqrt K-2M\sqrt{t_R})_+.          \tag{5}
\]

第一式无需迹条件或第四矩上限。简核：H_R特征基中δ_i=λ_i²−w_i，
ρ_i=Σ_(j≠i)|W_ij|²≤w_i(M−w_i)。Young给δ_iρ_i≤Mδ_i²/4+ρ_i²/M，
而w_iρ_i+ρ_i²/M≤Mρ_i，故K_R≤M qdiag+4M qoff≤4M q_R。
第二式用commutator三角界与
||H−H_R||_(2,d)²≤t_R，因为(|λ|−R)_+²≤(λ²−R²)_+。
保留t_R是关键；不以a_T/R²的粗界替换它。

## 3. scalar平方恒等式保留PSD尾的正成本

对任意实x,y，令u=|x|、v=|y|、d_R(x)=x²−h_R(x)²≥0。
准确有

\[
 \begin{aligned}
 &x^2y^2-h_R(x)^2h_R(y)^2-R^2\{d_R(x)+d_R(y)\}
                     +R^2(u-v)^2\\
 &\qquad=\begin{cases}
 R^2(u-v)^2,&u,v\le R,\\
 (uv-R^2)^2,&\max(u,v)\ge R.
 \end{cases}
\end{aligned}                                          \tag{6}
\]

边界两式一致。又(x+y)²≥(u−v)²，故

\[
 x^2y^2-h_R(x)^2h_R(y)^2
 \ge R^2\{d_R(x)+d_R(y)\}-R^2(x+y)^2.                  \tag{7}
\]

在H特征基中以非负 |U_ij|²/d 求和。U为unitary，|U_ij|²双随机，
所以d_R的两项给2t_R；最后一项准确是α²。因此

\[
 \tau(H^2UH^2U)-\tau(H_R^2UH_R^2U)
       \ge2R^2t_R-R^2\alpha^2.                         \tag{8}
\]

Γ与Γ_R的准确difference只另含−2τ(WUD_RU)。D_R与UD_RU为PSD，
0≤W≤MI给τ(WUD_RU)≤Mt_R。于是(4)、(8)严格给

\[
 \boxed{q-2r\ge q_R+2(R^2-M)t_R-2e_R^2-R^2\alpha^2.}  \tag{9}
\]

没有把Γ_R当PSD，也没有交换W和H。原root提出的直接PSD展开已经保证
τ(D_RUD_RU)≥0；(6)–(8)进一步量化它与两次clip差所提供的正成本。
正成本不能删除后再用较弱growth合同代替本式。

## 4. 消元tail：whole finite必要式与无增长前件极限

令c=2(R²−M)>0、z=sqrt(t_R)。由(5)，

\[
 q_R+ct_R\ge\frac{(\sqrt K-2Mz)_+^2}{4M}+cz^2
       \ge\frac{Kc}{4M(M+c)}.                          \tag{10}
\]

最后一步是精确一元最小化：z≤sqrtK/(2M)时完成平方，极小点
z=sqrtK/[2(M+c)]；其最小值为K/(4M)−K/[4(M+c)]。
z在其余半轴时cz²≥cK/(4M²)，仍不低于同一数。
K=0情形直接成立。故全finite不等式为

\[
 \boxed{q^{\mathrm e}-q^{\mathrm o}=q-2r
 \ge\frac K{4M}\frac{2(R^2-M)}{2R^2-M}
        -2(R\alpha+\omega)^2-R^2\alpha^2.}              \tag{11}
\]

任意H、U、0≤W≤MI均可使用，只要U*=U、U²=I、R²>M。
无先验q_R、q、a上界。也没有将未知fourth tail免费取极限。

对原actual对象，选R_T²=L，最终必大于M_T。由(3)，
2(R_Tα_T+ω_T)²+R_T²α_T²=O(1/L)+o(1)，
factor=1−M_T/(2L−M_T)→1。K_T已有有限极限，故(11)直接给(1)。
这个growing clip合法，因为(4)–(11)对每个R的常数显式且一致；
未使用只对fixed R声称的uniform-o。

亦可保持joint两极限：先任意fixed R²>M_*，T→∞，误差趋零，
得到liminf(q−2r)≥(K_*/4M_*)·2(R²−M_*)/(2R²−M_*)；
再令R→∞即(1)。(10)已经消元t_R，因此这次两极限不需要a_T bounded。
这是与468旧有bounded-q clip步骤的实质区别。

特别地，沿任何共同有界极限(q,r)，

\[
 0\le r\le\tfrac12(q-\underline q),\qquad
 q^{\mathrm e}\ge r+\underline q,\qquad
 \underline q=41/15120.                               \tag{12}
\]

whole q可能增长时，(1)仍成立。因已有liminf q≥underline q>0，
亦有limsup(r/q)≤1/2。它不界定q大小，不能自行支付whole第四矩。

## 5. 尚未付款Q候选的更紧必要covariance区间

这里只接已付δ_e=11/480、δ_o=13/480与χ_T→C=23/960：
|c_T−χ_T|≤sqrt(q_T^e δ_e,T)+sqrt(r_T δ_o,T)。
不将整体Δ⊥Z拆成各parity正交；本节没有使用Z的新付款。

**若未来另证**limsup q_T≤Q=1/350，则(12)给
limsup r_T≤(Q−underline q)/2=11/151200。
共同极限中sqrt((q−r)δ_e)+sqrt(rδ_o)先随q增加，q=Q时随r增加直到
Qδ_o/(δ_e+δ_o)=13/8400；允许的r全在此单调区间。因此

\[
 \limsup|c_T-C|\le\sqrt A+\sqrt B<\frac{47}{5000},
 \quad A=\frac{4631}{72576000},\quad B=\frac{143}{72576000}.\tag{13}
\]

严格比较有纯有理平方证书。h=47/5000时

\[
 h^2-A-B=\frac{365807}{16200000000}>0,
 \qquad(h^2-A-B)^2-4AB
 =\frac{155910001}{22325625000000000000}>0.              \tag{14}
\]

所以该仍未证明的Q候选必须满足更窄外包
1747/120000≤liminf c_T≤limsup c_T≤4003/120000，端点有固定严格余量。
这收紧旧1/100外包，但没有实现或排除整个candidate。

新付款是整个actual平方残差的parity gap；wholehigh固定upper、
whole31/22净upper及新的比例均仍开放。已有无零边界没有改变。
