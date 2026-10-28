# C051域腿：闭源form、最优anchor能量与强resolvent极限

2026-10-28；`/root/rational_first_gate` 当前独占证明稿。已恢复README／STATE、check→show、同G20261027/runtime1793085111/原0c4f、C051、AG、frontier／summary，并全文读[root主证明](root-weak-source-and-anchor-proof.md)。本稿不重证主弱源lemma；将其(L)明确作为conditional输入，独立核源form的域与自然后果。C050／587已完成，不重启；无web／source／新合同／STATE／Git／cadence操作。根对齐／fresh消费前不自授新编号或轮数。

## 1. 三个Hilbert角色与唯一conditional输入

固定一个bounded open interval J，使 `overline I₀∪[3,5]⊂J`，其中 `I₀=(−17/16,17/16)`。源Hilbert空间为

\[
 H=L^2(J,du),\qquad H_0=L^2(I_0,du),
 \quad i:H_0\hookrightarrow H
\]

（i为零延拓等距嵌入，i*为restriction／anchor正交投影后识别到H₀）。这两者是**源**空间；560的receiver Hilbert空间、Sonin Π_X和A_r卷积算子仍在原实际表示内，不能把本稿的源operator谱冒作receiver谱。

记w(t)=log(2+|t|)，对零延拓源定义

\[
 V_J=D_{\log}(J)
 =\{r\in H:\|r\|_{V_J}^2:=\frac1{2\pi}\int w(t)|\widehat r(t)|^2dt<\infty\},
 \qquad V_0=D_{\log}(I_0).
\]

`||r||²_V≥log2 ||r||²_du`。V₀零延拓到V_J后norm不变，`iV₀⊂V_J`。这是全线Fourier／zero-extension域，非regional／periodic norm。560 §4的缩支撑再mollify core论证给 `C_c∞(J)` 在V_J稠密，anchor同理；故两域也分别在H／H₀稠密。

唯一新conditional输入是[root已给(L)](root-weak-source-and-anchor-proof.md)：对任意X_n→∞，若f_n∈V_J、du有界且在H弱收敛到非零f，则实际 `T_(X_n)[f_n]→∞`；弱limit不必在V_J。以下只消费(L)，不重复normal-family／Rouché／frame证明，也不从旧587 printed theorem直接假设它。

## 2. Finite-X实际T_X的闭性、域、compact embedding与无核

[560 §§1、4](../../../notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md)给fixed finite F_X的实际密度

\[
 2\pi\rho_X(t)=\Gamma(t)
 -2\sum_{p\le X}\log p\sum_{k\ge1}p^{-k/2}\cos(kt\log p)
 +\epsilon_X(t),\qquad \epsilon_X\in C_0(\mathbb R).
\]

Γ为完整 `Reψ(1/4+it/2)−logπ`，其与w之差全线有界；finite-prime Fourier级数绝对一致收敛。因此对每fixed X有实bounded函数b_X，使 `2πρ_X=w+b_X≥0`。于是源form

\[
 T_X[r,s]=\int\widehat r\,\overline{\widehat s}\,\rho_Xdt
 =\langle r,s\rangle_{V_J}+\langle B_X^{\rm src}r,s\rangle_H,
 \quad r,s\in V_J,
 \tag{1}
\]

其中B_X^src为bounded self-adjoint源operator，norm允许依X；不是Euler乘子B_X。高频 `2πρ_X≈w`，低频有界，故natural form domain准确是V_J。560已经将该closure运输到ALLcomplex V_J的ordinary trace／HS源域，所以(1)仍等于actual `Tr(A_rΠ_XA_s*)`，未把仅L²源免费当HS。

`T_X+C_X||·||²_H` 与 `||·||²_V` 等价。若r_n在 `T_X+||·||²_H` norm下Cauchy，则它先在H Cauchy，而
`||r_n−r_m||²_V≤T_X[r_n−r_m]+||B_X^src||||r_n−r_m||²_H`，所以也在V_J Cauchy；完整性及(1)使极限仍在域且form收敛。因此T_X为densely defined、nonnegative、closed form，不能仅由点态ρ≥0省略域闭合。

下面付 `V_J↪H` compact。令K_R为zero-extension Fourier截到|t|≤R后再restriction到J的operator。它在H上的kernel为

\[
 k_R(u,v)=\frac1{2\pi}\int_{-R}^{R}e^{it(u-v)}dt,
 \quad(u,v)\in J\times J,
\]

bounded且J有限测度，故K_R为Hilbert–Schmidt／compact。另一方面

\[
 \|r-K_Rr\|_H^2
 \le\frac{\|r\|_{V_J}^2}{\log(2+R)}.
\]

所以V_J的unit ball由compact K_R像一致逼近，embedding compact。anchor V₀同理。

T_X无kernel：若T_X[r]=0，高频ρ_X严格正迫rhat在一个高频实区间几乎处处为零。r支持bounded J且属L²，故也属L¹，其Fourier entire；连续性及解析唯一性给r=0。

进一步，对每fixed X存在λ_X>0，使 `T_X[r]≥λ_X||r||²_H`。否则有unit-H源r_n使T_X[r_n]→0；(1)给V_J有界，compact embedding给strong-H子列到unit r，而closed positive form的lower semicontinuity给T_X[r]=0，与无kernel矛盾。也可先抽V_J弱子列，再以(1)的bounded perturbation及strong-H极限核该lsc，不需uniform-X前件。

故对每fixed X有常数a_X,b_X>0，

\[
 a_X\|r\|_{V_J}^2\le T_X[r]\le b_X\|r\|_{V_J}^2.
 \tag{2}
\]

λ_X／a_X不声称在X一致。由closed form定义源self-adjoint正operator `𝒜_X`：u∈Dom𝒜_X当且仅当存在h∈H使T_X(u,v)=⟨h,v⟩对全部v∈V_J成立，𝒜_Xu=h。紧embedding给每fixed-X的compact resolvent；这是源form的结论，不是新的RH谱实现。

## 3. Anchor完整Q的closed coercive form

在I₀上，完整Γ与w差为bounded Fourier multiplier，所有自相关可见primepowers有限且相应shift型在L²有界，两pole的cosh／sinh线性读出亦在bounded I₀上有界。因此原完整型在core上为

\[
 Q_W[q,s]=\langle q,s\rangle_{V_0}
                +\langle C_0q,s\rangle_{H_0},
 \quad C_0=C_0^*\text{ bounded}.
 \tag{3}
\]

没有删除Γ／FP-contact、properpowers或odd负pole；它们在C₀及log主form中按原符号保留。**这里只在anchor用正性，未假设全局Q_W PSD。**

[537 §2](../../../notes/537-source-exact-weil-window-positive-tail-admission.md)给core上 `Q_W[q]≥κ||q||²_H₀`、κ=2^-49162。以560原V₀ core延拓(3)，该不等式传到全部V₀。又

\[
 \|q\|_{V_0}^2
 \le Q_W[q]+\|C_0\|\|q\|_{H_0}^2
 \le(1+\|C_0\|/\kappa)Q_W[q],
\]

上界也由(3)和 `||q||²_H₀≤||q||²_V₀/log2` 给出。因此存在fixed a₀,b₀>0，

\[
 a_0\|q\|_{V_0}^2\le Q_W[q]\le b_0\|q\|_{V_0}^2.
 \tag{4}
\]

Q_W由此是H₀上domain V₀的densely defined positive closed form。记其associated positive self-adjoint operator为𝒜_Q。这里也给了“合法infinite anchor range”所需的实际Q域／du coercivity，非抽象completion随意读出。

## 4. 原trace源resolvent强趋0：只用energy与(L)

固定g∈H，令 `u_X=(𝒜_X+1)⁻¹g`。variational identity给

\[
 T_X[u_X]+\|u_X\|_H^2=\operatorname{Re}\langle g,u_X\rangle,
 \quad\|u_X\|_H\le\|g\|_H,
 \quad T_X[u_X]\le\|g\|_H^2.
 \tag{5}
\]

对任意cofinal序列X_n→∞抽H弱cluster u；若u≠0，u_Xn在共同J且du有界，(L)使T_Xn[u_Xn]→∞，反(5)。所以全部weak cluster均为0，即u_X⇀0。再由(5)，`||u_X||²_H≤Re⟨g,u_X⟩→0`。因此

\[
 \boxed{(\mathcal A_X+1)^{-1}\xrightarrow{\rm strong}0\quad\text{on }L^2(J).}
 \tag{6}
\]

没有uniform-X compactness／monotonicity假设；也没有证明operator-norm convergence、λ_X→∞或全source单位球lower。这里只称这族bounded resolvent的strong极限为0，不制造H上一个普通“无穷operator”。

## 5. 同正分解类的最佳能量：minimum、唯一性与closed form

在H上以extended form定义

\[
 \mathcal F_X[r]=\inf_{q\in V_0}\{T_X[r-iq]+Q_W[q]\}.
 \tag{7}
\]

要求r−iq∈V_J；由于iV₀⊂V_J，有限值的domain准确为V_J，r∉V_J时置∞。它是同一fixed-anchor正分解的最优值，未新增正模型或改残差系数1。

对r∈V_J，在V₀中考虑

\[
 a_X(q,v)=T_X(iq,iv)+Q_W(q,v),\qquad
 \ell_r(v)=T_X(r,iv).
\]

该sesquilinear form bounded，且由(4)满足 `a_X(q,q)≥a₀||q||²_V₀`；ℓ_r为continuous anti-linear functional。Lax–Milgram／完成平方的Hilbert论证给唯一q_X(r)∈V₀，使

\[
 T_X(iq_X,iv)+Q_W(q_X,v)=T_X(r,iv)
 \quad(\forall v\in V_0).
 \tag{8}
\]

它对r complex-linear、V_J→V₀ bounded。对任意h∈V₀，(8)消cross，原目标在q_X+h处等于其minimum加 `T_X[ih]+Q_W[h]`，所以minimum确实取得且唯一，不把infimum免费当closed。该q_X由 `T_X+Q_anchor` 的能量方程决定，**不是**任意infinite T_X-orthprojection；本构造没有声称后者均已存在或具有physical／Q域。

以此定义polarization

\[
 \mathcal F_X(r,s)
 =T_X(r-iq_X(r),s-iq_X(s))+Q_W(q_X(r),q_X(s)).
\]

它是Hermitian positive quadratic form。由(2)、(4)及 `||r||²_V≤2(||r−iq||²_V+||q||²_V₀)`，

\[
 \tfrac12\min(a_X,a_0)\|r\|_{V_J}^2
 \le\mathcal F_X[r]\le T_X[r]\le b_X\|r\|_{V_J}^2.
 \tag{9}
\]

故F_X的norm与complete V_J norm等价，domain V_J，positive且closed／densely defined。记其associated source-operator为𝓑_X，区别于Euler乘子与receiver Π_X。每fixed X其resolvent也compact；这些fixed-X常数不作cofinal uniform费用。

## 6. Extended limit与Mosco两条实际验证

定义extended closed form

\[
 \mathcal F_\infty[r]=
 \begin{cases}
 Q_W[q],&r=iq,\ q\in V_0,\\
 +\infty,&\text{otherwise in }H.
 \end{cases}\tag{10}
\]

其finite domain为iV₀，closure为iH₀，通常不在H稠密；不能把它当整个J上的通常densely-defined Q_W。

**Weak liminf。** 任取X_n→∞、r_n⇀r于H；若liminf F_Xn[r_n]<∞，取达到该liminf且energies bounded的子列，并用第5节minimum q_n（近似minimum亦够）。Q_W[q_n] bounded，由(4)抽V₀弱子列q_n⇀q∈V₀。r_n du有界；残差 `e_n=r_n−iq_n∈V_J` 仍du有界、共同支持J，weak limit为r−iq。T_Xn[e_n]被同一energy控制；(L)迫r=iq。Q_W在V₀是Hilbert norm平方，weak lsc给

\[
 \mathcal F_\infty[r]=Q_W[q]
 \le\liminf Q_W[q_n]
 \le\liminf\mathcal F_{X_n}[r_n].\tag{11}
\]

若r不在iV₀，假定finite liminf导致矛盾，故相应liminf为∞。没有要求r_n的Dlog norm共同有界；Q项单独提供的是q_n的V₀界。

**Strong recovery。** 对r=iq、q∈V₀，取常序列r_n=r且在(7)选同一q，残差为0，所以 `F_Xn[r]≤Q_W[q]=F∞[r]`。对F∞=∞的r，recovery上界条件本来无有限限制。连同(11)即实际验证Mosco两条件，不以名称替证明。特别地，对每个fixed r∈H，

\[
 \boxed{\mathcal F_X[r]\longrightarrow\mathcal F_\infty[r].}\tag{12}
\]

因此anchor的V₀上极限是原完整Q；anchor外（乃至anchor内不在原Q域的L²源）为∞。固定r_a=τ₄r₀在J内、anchor外，所以最佳能量亦趋∞；它是主fixed test的自然加强，而非新的全局Weil正性。

## 7. 自给energy证明的广义resolvent极限

固定g∈H，令 `v_X=(𝓑_X+1)⁻¹g`。它唯一最小化 `F_X[r]+||r−g||²_H`，且

\[
 \mathcal F_X[v_X]+\|v_X\|_H^2
 =\operatorname{Re}\langle g,v_X\rangle.
 \tag{13}
\]

这给v_X du有界及F_X[v_X] bounded。任取weak cluster v，(11)使v=iq∈iV₀。对任意w∈V₀，minimum与anchor recovery给

\[
 \mathcal F_X[v_X]+\|v_X-g\|^2
 \le Q_W[w]+\|iw-g\|^2.
\]

取weak liminf，v唯一最小化 `F∞[r]+||r−g||²`。等价于q在H₀解

\[
 Q_W(q,w)+\langle q,w\rangle_{H_0}
 =\langle i^*g,w\rangle_{H_0},\quad
 q=(\mathcal A_Q+1)^{-1}i^*g.
\]

唯一性使v_X⇀iq。又由(11)、(13)及limit energy identity，

\[
 \limsup\|v_X\|_H^2
 \le\operatorname{Re}\langle g,iq\rangle-Q_W[q]
 =\|iq\|_H^2.
\]

weak lsc给反向liminf，故norm收敛，v_X→iq strongly。于是，不援引未核的Mosco–resolvent定理而直接得到

\[
 \boxed{(\mathcal B_X+1)^{-1}
 \xrightarrow{\rm strong}
 i(\mathcal A_Q+1)^{-1}i^*.}\tag{14}
\]

i*也可记为P_(I₀)，先投影／restriction到anchor H₀。右侧是H上annihilate外部方向的**广义resolvent**，不是domain稠密于全H的有限self-adjoint operator resolvent；不写成通常全空间Q_W的resolvent，也不声称operator-norm convergence。

同一energy还给 `F_X[v_X]→Q_W[q]`。其minimum q_X(v_X)在V₀弱趋q、Qnorm趋Q(q)，故在V₀强趋q，而 `T_X[v_X−iq_X(v_X)]→0`。这只是上述同一最小化身份的直接后果，没有另添source／参数或新预算。

## 8. 条件、原规范与消费限制

第2–3、5节的fixed-X域／minimum／closedness由560原Γ+bounded项、原core、537 anchor κdu及普通Hilbert论证独立闭合。第4、6–7节只额外依主(L)；一旦root／fresh消费(L)，这些自然后果无另一个moving-domain假设。所有源保持原du／zero-extension Dlog与complex槽，finite-X ordinary迹仍是actual Sonin，不把form closure混作receiver projection或source-rank。

完整Γ／FP-contact、全部Λ(p^k)=logp及两个pole在Q／T的bounded perturbation字典中保留，只有anchor Q已知PSD。全局Q正号、漂移／成长anchor、消失迹权或unbounded signed cross均未被本稿解决。strong resolvent0／广义anchor极限不代RH谱识别或全Weil正性，whole4/5UPPER与primitive/principal/mixed／signed核心门不因此完成。

本稿不改STATE／cadence／Git；C051是否闭合、编号及统一一轮由root对齐主(L)、当前fresh及实际版本后消费，同实例Goal保持active/open/noteligible。
