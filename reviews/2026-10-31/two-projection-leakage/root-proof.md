# C066：相位倍增的全trial与实际交叉泄漏证明

2026-10-31，root原推导稿；不是root最终消费。唯一输出尺度Y=X²，同G20261027/runtime1793085111/冻结0c4f。一轮责任；不授其它指数、rank、source或作者章节后继。

## 1. 域、结论与已付输入

沿560的physical H与全部finite-Euler Gram逆，Mellin酉坐标H=L²(dt/(2π))中B_Z=M_(D_Z)，

    D_Z(t)=∏_(p≤Z)(1−p^(−1/2−it)), w_Z=|D_Z|²,
    Π_Z=B_Z P(PB_Z*B_ZP|RanP)^−1 PB_Z*, A_r=M_f, f=rhat.

源仍r=e^(u/2)bare，原du/zero-extension Dlog。每fixed complex Cc∞源的A_rΠ_Z∈S₂由560支付。因此

    E_X(r,s)=〈(I−Π_Y)A_rΠ_X,(I−Π_Y)A_sΠ_X〉HS,
    C_X(r,s)=〈Π_Y A_rΠ_X,Π_Y A_sΠ_X〉HS,
    E_X=t_X−C_X, 0≤E_X(r)≤t_X(r).                         (1)

第一槽linear，mixed全域是严格HS×HS；不称Π_Z或未夹源乘积S₁。逐层E一般非stationary，不先称W_X正分布。将证明：每个先fixed非零r，k=ord₀ f有限，存在c_r>0、X_r，使

    E_X(r)≥c_r sqrtX/(logX)^(2k+2)→∞.                    (2)

记ell=logX、a_Z=sqrtZ/logZ、s_X=a_X/ell。以下只消费旧585/589已闭的准确资产：

* Uniform Euler式：logw_Z(t)=−4a_Z h_Z(t)+o(a_Z)，h_Z=Re[e^(−it logZ)/(1−2it)]，uniform |t|≤Z²；全线另有w_Z≤exp[(4+o(1))a_Z]，由2Σp^−1/2 upper。
* 585固定真实H₀：H₀(0)≠0、|H₀(t)|≤C exp(−c sqrt|t|)，全部有限多项式倍在同一arch Sonin域。J_X=[π/ell−ell^−2,π/ell+ell^−2]上w_X≥exp[(4−o(1))a_X]。
* 对全部complex polynomials deg q<n，I(q)=∫_(J_X)|qH₀|²dt>0，旧Legendre/Gevrey账本给∫|qH₀|²dt≤exp[C n log(n+ell)]I(q)，以及pointwise |q(t)|²≤C n²ell²[C ell²(1+|t|)]^(2n)I(q)。
* 589/C052的whole weighted evaluator：Q_Z(t)≤exp[(-4+o(1))a_Z]，uniform |t|≤(logZ)^B，B先fixed；**actual** diagonal为k_Z(t,t)=w_Z(t)Q_Z(t)，相对dt/(2π)。不是仅away-zero界，也不偷用bare Q为actualρ。

这些是旧root消费输入，不重审所有嵌套证明；新责任是相位集合上的whole-growing-trial集中与不同输出的capture。

## 2. 相位峰谷反配

先fixed 0<ε≤1/100，设S_X={t:h_X(t)≤−1+ε}。令a=(1−2it)^−1、z=e^(−it ell)、v=az=x+iy。x≤−1+ε、|v|≤1，故|t|≤sqrtε、|y|≤sqrt(2ε)。Y=X²时

    h_Y=Re(v²/a)=x²−y²+4txy
        ≥1−4ε+2ε²−4sqrt(2)ε≥1−10ε≥.9.                 (3)

|t|界来自|a|≥1−ε及[(1−ε)^−2−1]/4≤ε。若|t|≤π/(2ell)，则cos(tell)和2t sin(tell)均非负，h_X=(cos(tell)+2t sin(tell))/(1+4t²)≥0。所以

    S_X⊂{π/(2ell)<|t|≤sqrtε}.                          (4)

在此同一集合，输出uniform Euler式与whole Q_Y相乘给

    sup_(S_X) k_Y(t,t)≤exp[−7a_Y]                     (5)

对充分大X成立；因为logk_Y≤−4a_Y h_Y−4a_Y+o(a_Y)≤−7.6a_Y+o(a_Y)。S_X虽随X变，始终在固定小区间，故两个输入的uniform量词都覆盖它。没有固定Y后换对角极限。

## 3. 增长维trial在S_X的统一集中

取n=floor(c_ε a_X/ell)，c_ε>0足小。对所有deg q<n，置v=D_X qH₀，按真实H范数归一。J_X⊂S_X最终成立，因为其上h_X=−1+O(ell^−2)。因此

    ||D_XqH₀||²≥(2π)^−1 exp[(4−o(1))a_X] I(q).         (6)

在S_X补集且|t|≤X²，Euler式给w_X≤exp[(4−4ε+o(1))a_X]。利用全线unweighted多项式账本，除以(6)，这部分质量至多

    exp[−4εa_X+o(a_X)+C n log(n+ell)]≤exp[−2εa_X]       (7)

最终成立；log(n+ell)≤ell最终成立，故可先选c_ε使C c_ε<ε，再取X大吸收o项。此选择独立q及所有complex系数。

频率|t|>X²不能沿用有限高度Euler渐近。改用全线w_X upper及pointwise多项式界/Gevrey尾。令u=sqrt|t|≥X，积分的指数除去固定因子后至多

    C n logell+4n log(2u)−c u.

因为n logX/X=O(a_X/X)→0，sup_(u≥X)n logu/u→0；故全部多项式增长被Gevrey指数吸收，dt=2u du亦可吸收。该tail除以(6)为O(exp[−c'X])。结合(7)，存在κ_ε>0使

    ||1_(S_X^c)v||²≤exp[−κ_ε a_X]                    (8)

对**整个**n维trial T_X=span{D_Xt^jH₀:0≤j<n}的全部unit向量成立。T_X⊂RanΠ_X是实际物理range，不是Gaussian辅助测度；n个函数线性独立，故dim T_X=n。

## 4. 源乘法与真正输出projection运输

固定非零compact complex r，f整个且不恒零，因此k有限。取δ_r,c_r>0使|f(t)|≥c_r|t|^k于|t|≤δ_r；全线|f|≤||r||₁。现在先选ε≤min(1/100,δ_r²/4)，这是证明中的trial选择，**不是改变同一E_X的生成规则**。

由(4)/(8)，每个unit v∈T_X有

    ||M_fv||²≥c'_r ell^(−2k)(1−exp[−κ_ε a_X]).         (9)

由(5)及actual kernel的positive trace，

    ||Π_Y 1_(S_X)||op²≤||Π_Y 1_(S_X)||HS²
      =∫_(S_X)k_Y(t,t)dt/(2π)≤C_ε exp[−7a_Y].           (10)

这是有cutoff的HS算子，不将整个Π_Y宣称trace class。分S_X及补集，用乘f与cutoff可交换、projection contraction及(8)，

    ||Π_Y M_fv||²≤C_r[exp(−7a_Y)+exp(−κ_ε a_X)].        (11)

右侧uniform于全部unit trial向量。输出正交分解、(9)/(11)于是给|| (I−Π_Y)M_fv||²≥c''_r ell^(-2k)。在T_X取真实ON基，正项求和并用HS范数支配有限维restriction，得

    E_X(r)≥n c''_r ell^(-2k)
          ≥c'''_r sqrtX/ell^(2k+2).                    (12)

这才是新crosslower。旧t_X lower本身没有相减C_X的资格；此处只在实际n维trial上证明output capture指数小，没有声称整个C_X/t_X→0。

## 5. 共同正scalar与cofinal正混合

固定587的du-unit even bump r₀，support[-1,1]、h₀=∫r₀≠0。由(12)的k=0和旧589 upper，E_X(r₀)≍s_X。每个fixed mean-zero z有0≤E_X(z)≤t_X(z)=o(s_X)。PSD Cauchy及r=(∫r/h₀)r₀+z，给所有fixed complex源对

    E_X(r,s)/E_X(r₀)→(∫r/h₀)overline(∫s/h₀).          (13)

此归一化结论是新分母lower加旧589的直接后果，归同一责任。若任意共同positive scalar β_X满足β_X E_X(r₀)→q₀=Q_W(r₀)>0，则β_X E_X(r₀′)→0，与537的q₁=Q_W(r₀′)>0冲突。两q保完整Γ/contact、pp及indefinite双pole；mean-zero不等于pole-free。无需exact leading常数。

还可准确消费一种共同修复：在X≥X₀、分母已正后，令F_X=E_X/E_X(r₀)。任意共同probability measuresν_j若ν_j([X₀,M])→0对每fixed M成立，则∫F_X(r,s)dν_j趋(13)。理由是F_X对每fixed pair最终uniform接近极限，且有限cutoff区间仅有限次投影变化、分母正，故locally bounded。等价地，未归一正权的r₀能量质量先归一、其质量cofinal逃逸，且总r₀能量趋q₀，仍不能匹配r₀′。不覆盖逐源不同权、非cofinal剩余、负权或其它输出尺度。

## 6. 完整经典身份、净后果与止点

对任意fixed源窗I，X最终含全部可见pp后，560给Q_W=t_X−K_(X,I)+Pole，故Q_W−E_X=C_X−K_(X,I)+Pole。原Γ=2θ′、FP/contact、所有proper powers和双pole都在此身份中；新证明未判该有符号有限部的有利号，更未构造principal/整sections/mixed RR。

新净值仅为不同实际Π_X→Π_(X²)的同时成长反配与完整fixed源失败，以及已核共同正校准/混合。Y=X的591、固定输出的旧界、固定向量强极限、596单prime增量均不支付(8)–(12)。不以新norm标签或旧ratio1计功。它停止一个此前未核的实际PSD候选，**不是一般Y(X)/source-adaptive/relative/higher/signed方法的边界**。

Whole leading4/5仍负惯性UPPER，危险core/cross/成长Ξ与原三个Goal门open。待独立完整proof、不同组织审查和root消费后才按一个数学迭代结算；本稿不修改cadence、不预宣称Goal完成或完整D′收敛。
