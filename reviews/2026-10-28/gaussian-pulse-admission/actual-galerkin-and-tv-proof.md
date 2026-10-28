# Gaussian＋有限平移正滤波：actual Galerkin 与总变差证明

2026-10-28；`/root/scalar_upper_tail` 当前独占稿。已恢复 goals/README、STATE、check→show、G20261027／原0c4f、AR／cycle17、已耗尽C052及宏观前沿；随后全文核root冻结的AS规则3548b／963e55ea，本次执行以该新Gaussian-pulse准入为准，不恢复poly degree／quiet频带或C052预算。开始时本输出不存在。本稿只核同一actual ρ_X的正性、外层有限Galerkin构造与误差；不审新PDF、web或数值，不改Git／STATE／cadence，不预C053／590。草稿／root消费状态分别由原件和根收据记录。

**限定通过，属强旧直接后果0。** 对每个预先固定的非负 σ∈Cc∞(R)，下面规则以固定Gaussian e^(−t²)及固定稠密平移字典产生正谱ν_X，并有总变差ν_X→σ(t)dt，继而谱和physical两侧均strong S′收敛。全实轴a.e.正性可由已付的单个非零entire Sonin向量推出，不必把σ收缩到原点附近。该结论不构造完整Weil目标的未知正谱，也不提供M_X、条件数或积分认证的有效算法／速率。

## 1. 对象、域、原规范与已付输入

保560／585实际物理投影

\[
 \Pi_X=B_XP(PB_X^*B_XP|_M)^{-1}PB_X^*,\quad
 D_X(t)=\prod_{p\le X}(1-p^{-1/2-it}),\quad
 \operatorname{Ran}\Pi_X=D_XM.
\]

range等式不是未加权等距。receiver Hilbert仍为L²(dt/(2π))，完整Euler Gram逆与全部returns在Π_X和ρ_X内。physical源是r=e^(u/2)f，rhat(t)=∫r(u)e^(−itu)du；原ordinary正迹T_X[r]=∫|rhat|²ρ_Xdt。记同一投影在dt/(2π)下的评价核对角为κ_X(t)，则

\[
 \kappa_X(t)=2\pi\rho_X(t).                                      \tag{1}
\]

这是本稿用于评价Cauchy的归一化。560有附1/√(2π)的裸evaluator时，其范数平方直接等于ρ_X；二者不能混用。

已付560§4给每个fixed finite X的连续密度和ρ_X(t)≤C_X log(2+|t|)。589上游更强的arbitrary-measurable权证明还给ρ_X(t)≤C(√X+log(2+|t|)) a.e.；本构造只须逐X的前一个上界，完全不需要C_X统一或589的cofinal局部化速率。Gaussian指数矩因此没有遗漏cofinal系数费。

源先取全部complex Cc∞。下述每层ν_X为有限正测度，故新配对事实上也能作用于compact L²源（由||r||₁²ν_X(ℝ)控制），但不用它替换原Sonin／Weil Dlog型域或更改physical du。

## 2. ρ_X在全线几乎处处严格为正

585§2及其已付共同向量稿固定同一H₀∈M，H₀(0)>0。其raw Mellin变换是entire：已付completed Mellin为entire，除去Gamma因子等于乘entire reciprocal Gamma及指数因子；再乘compact Gevrey平滑核的entire Fourier变换仍为entire。这里只使用已核entire／非零属性，不借未消费的raw O(1/t)或任意common-zero断言。

因此H₀在实轴的零点局部有限，测度为0。有限D_X在实轴处处非零，因为每个因子绝对值≥1−p^(−1/2)>0；v_X=D_XH₀是实际RanΠ_X内非零向量。真实评价Cauchy在原weighted运输后给

\[
 2\pi\rho_X(t)=\kappa_X(t)
 \ge\frac{|D_X(t)H_0(t)|^2}
             {\|D_XH_0\|_{L^2(dt/(2\pi))}^2}.                    \tag{2}
\]

分母对每fixed X有限且正。若直接用原arch evaluator，则(2)正是完整Gram逆的变分Cauchy式，而不是把B_X当酉或把Gaussian当Sonin trial。于是

\[
 \rho_X(t)>0\quad\text{对Lebesgue几乎处处 }t\in\mathbb R.        \tag{3}
\]

这里不必证明每个实点无共同零；a.e.已经足够。ρ_X可能的零点均包含在H₀的离散实零集中。全线(3)已付，所以任意compact σ的支持都合法，不限near0。

## 3. 固定Gaussian测度与指数字典的完备性

固定A=1，不优化或移动它。置

\[
 d\mu_X(t)=e^{-t^2}\rho_X(t)dt.
\]

由上一节，μ_X与Lebesgue测度等价。由逐X的log上界，对每个R≥0和每个整数n≥0，

\[
 \mu_X(\mathbb R)<\infty,\qquad
 \int |t|^n e^{R|t|}\,d\mu_X(t)<\infty.                         \tag{4}
\]

常数允许任意依X／R／n；后面的M_X也允许无界，故不需要先付uniform费用。所有操作均在新外层L²(μ_X)中；e^(−t²/2)或字典元素没有被声称属于原Sonin trial空间。

先固定一列**互异**有理数(a_j)稠密于(−1,1)，固定次序先于X和σ，令e_j(t)=e^(−ia_jt)。每个e_j∈L²(μ_X)。对任一M和c≠0，指数多项式p=Σ_(j≤M)c_je_j是非零entire函数：在0取0至M−1阶导数的Vandermonde矩阵可逆。其实零集测度0；结合(3)，

\[
 \int|p|^2d\mu_X>0.                                            \tag{5}
\]

因此每个有限字典的Gram严格正定；不允许重复a_j造成奇异。

再核全部字典的稠密性。若v∈L²(μ_X)正交于每个e_j，定义有限complex测度dη=v dμ_X及

\[
 F(z)=\int e^{izt}v(t)d\mu_X(t).
\]

Cauchy–Schwarz和(4)给∫|v|e^(R|t|)dμ_X<∞，连同带任意t幂的同界，支付compact z集合上的支配与逐次求导，所以F为entire。正交性给F(a_j)=0。互异a_j在有限区间有聚点，identity theorem给F≡0。有限complex测度的Fourier唯一性给η=0：也可直接将η与Gaussian approximate identity卷积，Fourier反演先得每个卷积为0，再令Gaussian宽度趋0。故v=0 μ_X-a.e.，即

\[
 \overline{\operatorname{span}\{e_j:j\ge1\}}^{L^2(\mu_X)}
       =L^2(\mu_X).                                            \tag{6}
\]

参数只在固定(−1,1)中仍可完备，所付前件是Gaussian给entire Fourier，不是普通无权L²上的band-limited稠密断言。巨大或病态的系数不受本存在性证明约束。

## 4. 有限Galerkin规则：修正后的H／v约定

先固定σ≥0、σ∈Cc∞，m=m_σ=∫σ(t)dt。m=0时σ=0，以下f=p=0、ν_X=0为平凡情形。m>0时在(3)的满测集合定义

\[
 f_X(t)=\sqrt{\frac{\sigma(t)}{e^{-t^2}\rho_X(t)}}\ge0.
\]

零测异常点任意置0；不要求f_X有界或光滑。μ_X与Lebesgue等价及(3)保证精确

\[
 |f_X|^2d\mu_X=\sigma(t)dt,\qquad\|f_X\|_2^2=m.                \tag{7}
\]

使用conjugate-first的标准外层矩阵记法

\[
 H^{(M)}_{jk}=\int\overline{e_j(t)}e_k(t)d\mu_X(t)
             =\int e^{i(a_j-a_k)t}d\mu_X(t),\qquad
 v^{(M)}_j=\int\overline{e_j(t)}f_X(t)d\mu_X(t).                  \tag{8}
\]

所有积分有限，v_j由Cauchy–Schwarz支付。H是**外层dictionary Gram**，不同于ρ_X内部的Euler G_F。保留root已纠正的正指数／v约定；不以even μ偶然掩盖下标混搭。令

\[
 c^{(M)}=(H^{(M)})^{-1}v^{(M)},\qquad
 p_{X,M}=\sum_{j\le M}c_j^{(M)}e_j,
\]

这是f_X在该有限span上的真正正交投影，正规方程Hc=v逐项成立，且

\[
 E_{X,M}=\|f_X-p_{X,M}\|_2^2
   =m-(v^{(M)})^*(H^{(M)})^{-1}v^{(M)}\ge0,
\]
\[
 \|p_{X,M}\|_2^2=m-E_{X,M}\le m.                                \tag{9}
\]

E随M非增，(6)给对每fixed X有E_(X,M)→0。取ε_X=1/X，定义

\[
 M_X=\min\{M\ge1:E_{X,M}<\varepsilon_X^2\}.                  \tag{10}
\]

集合非空，所以最小M是确定的有限整数；本式采用冻结规则的严格门E<ε_X²，原先≤版本也同样有有限最小M。不需任何对X一致的收敛速率。X变化时所需M、coefficients和条件数可任意成长。

(10)是在精确ρ_X、精确积分和精确正规方程下的**数学存在／形式certified residual规则**。它没有给ρ_X或这些积分的有效评价程序、误差包络、最小特征值下界、矩阵条件数、M_X上界或实际浮点停止认证。不能把m−v*H^−1v的形式相减称为已执行／稳定的可计算算法。若另行有有效积分／逆的严密误差界，可据严格余量搜索；本稿未支付那项额外工程／有效性输入。

## 5. 实际正谱与总变差误差

令p_X=p_(X,M_X)，定义所给同一族

\[
 w_X(t)=e^{-t^2}|p_X(t)|^2\ge0,\qquad
 d\nu_X(t)=w_X(t)\rho_X(t)dt=|p_X(t)|^2d\mu_X(t).                \tag{11}
\]

每fixed X，p_X是有限指数和，w_X为Schwartz函数，ν_X是有限正测度；质量ν_X(ℝ)=m−E_(X,M_X)≤m。它只依预定σ、固定字典和X／actualρ_X，不依随后测试的源r,s。Gaussian和平移在原physical Fourier坐标下定义外层filter，没有修改源du或ρ内部的Π／Gram。

令TV表示总变差质量|ν−λ|(R)，不取概率距离的1/2约定。由(7)和| |p|−f |≤|p−f|，

\[
 \begin{aligned}
 \|\nu_X-\sigma dt\|_{\rm TV}
 &\le\|p_X-f_X\|_2(\|p_X\|_2+\|f_X\|_2)\\
 &\le2\sqrt m\,\varepsilon_X
 \le(2\sqrt m+\varepsilon_X)\varepsilon_X\longrightarrow0.
 \end{aligned}                                                 \tag{12}
\]

中间更强界使用真实投影的norm contraction；一般仅知L²近似也有最后所拟界。复数p不造成符号或极化问题。

因此ν_X→σdt于strong S′：对任意S中的有界集B，sup_(φ∈B)|ν_X(φ)−∫φσ|≤sup_B||φ||∞·TV→0。这里证明全部Schwartz测试，且有总变差控制，不是fixed-f配对后冒拓扑。

## 6. Physical正型、2π与完整目标的范围

定义physical分布和源配对

\[
 \mathfrak W_X[\varphi]=\int\widehat\varphi(t)d\nu_X(t),\qquad
 W_X(r,s)=\int\widehat r(t)\overline{\widehat s(t)}d\nu_X(t).
\]

仍用外层Weil配对**第一槽linear**。有限维求系数时的conjugate-first矩阵约定不改变它。若s*(u)=overline(s(−u))，则W_X(r,s)=𝔚_X[r*s*]，所以每层是stationary Hermitian正型tempered分布，且对每个complex r∈Cc∞，W_X[r]≥0。

按本定义的physical核为∫e^(−itu)dν_X(t)，因而

\[
 \mathfrak W_X\longrightarrow\mathfrak W_\sigma,\qquad
 \mathfrak W_\sigma[\varphi]=\int\widehat\varphi(t)\sigma(t)dt
 \quad\text{于strong }\mathcal S'.                             \tag{13}
\]

此处不添／除2π；若另将𝔚_X作标准Fourier变换，则hat𝔚_X=2π checkν_X，其中checkν_X(φ)=ν_X(φ(−·))。ν_X不必偶，反射不能删。(13)的strong拓扑由Fourier映射在S连续、S有界集的Fourier supnorm一致有界及(12)支付，也蕴含D′收敛。

所有fixed源对另有明确误差

\[
 |W_X(r,s)-\int\widehat r\,\overline{\widehat s}\,\sigma dt|
 \le\|\widehat r\,\overline{\widehat s}\|_\infty
       \|\nu_X-\sigma dt\|_{\rm TV}.
\]

在每个first-fixed I=(−L,L)上，|rhat|∞≤√(2L)||r||du，故对ALL complex r,s∈L²(I)更有相对**所选σ**的原du统一误差≤2L·TV·||r||du||s||du。此处不是相对完整Q的Γ统一误差，也未把L放入Gaussian参数。

full经典目标只须D′，不假设其tempered。这里的目标是**预定非负compact σ**，不是完整Wζ。完整Γ／FP-contact、全部proper powers及双pole没有被声称等于σdt，也没有删除或重定义；“可逼近任意已给正σ”不提供完整signed缺陷消失。特别不能先假设未知完整Weil正谱再用本构造命名为独立来源。

## 7. 同一规则的conditional正锥运输

冻结规则末段允许σ也预定地随X变化。这不需要新的uniform字典收敛率：每fixed X重复(6)–(10)，令m_X=∫σ_X，取

\[
 \varepsilon_X=\frac1{X(1+2\sqrt{m_X})}.
\]

同一有限Galerkin规则给TV(ν_X−σ_Xdt)≤2√m_X ε_X≤1/X，无论m_X成长多快；条件数和M_X仍未控。σ_X必须先于测试源选定，不能逐源改target。

具体地，给定一份**已经独立知道为正且tempered**的谱Radon测度η，可以先按标准方式选σ_Xdt→η于strong S′。这里不读取未知经典正谱。为闭合该标准步骤，固定0≤χ≤1、χ∈Cc∞、χ=1于[−1,1]、supportχ⊂[−2,2]，以及support⊂[−1,1]的非负compact smooth单位积分mollifier j。取R_X→∞、h_X↓0、h_X≤1，令

\[
 \sigma_X=(\chi(\cdot/R_X)\eta)*j_{h_X}\ge0.
\]

这是smooth compact非负密度，m_X有限。正tempered测度有某N使C_η=∫(1+|t|)^(−N)dη<∞；这也是其标准多项式质量成长表述的直接后果。对S任一有界集B，截断误差由

\[
 C_\eta(1+R_X)^{-1}\sup_{\varphi\in B}p_{N+1}(\varphi)
\]

控制。卷积误差用mean-value和|shift|≤h_X，控制为

\[
 C_{\eta,j}\,h_X\sup_{\varphi\in B}p_N(\varphi'),
\]

其中p_N(ψ)=sup_t(1+|t|)^N|ψ(t)|；平移后的权至多固定倍，χ≤1使该界独立R_X。两项均趋0，所以确为strong S′逼近。再用同一TV≤1/X与三角不等式，ν_X→η于strong S′，physical亦经原Fourier映射收敛。

这是已给正tempered谱的conditional transport，仍是当前同一Gaussian-pulse规则；没有另开参数候选、经典target选择或signed缺陷证明。它说明**不能**由某一份固定σ的失败推出整个Gaussian-pulse族失败。若要将η取为完整经典Weil谱，首先必须独立支付其正性／合法正谱membership；那正是未付目标，不能在此循环假定。完整目标只要求D′，本正tempered输入运输也不据此覆盖所有可能的非tempered D′目标。

## 8. 最强旧扣除及根消费接口

最短依赖链是：560实际全Gram投影／评价与逐X log界＋585已付非零raw-entire H₀ ⇒ρ_X全线a.e.正；Gaussian指数矩⇒指数字典完备和finite H正定；有限Hilbert投影⇒(9)／(12)／(13)。589更强arbitrary-measurable全线界足够但非必要；不借587 growing-degree Gram或新cofinal算术估计。本稿为标准强旧直接后果0，无独立算术／几何新输入，不建C053／590或计数学轮。

它确实给固定poly边界之外一个非poly／nonlocal、允许无界有限M的实际正规则；不能机械续用固定degree的均值极限去排除它。另一方面，本首门支付可预设正σ及已知正tempered谱的conditional全测试运输，不付完整Weil目标／signed core/cross、同一非零primitive／principal／mixed RR或Ξ，也未改善whole542＋555→557 leading4/5负惯性UPPER。完整目标的具体反测由本次其他独占稿／root另核，不在此复制。Goal原完成门open；所有消费待root／fresh绑定本终稿，子稿不自行结算。

## 已读依赖版本

- reviews/2026-10-28/gaussian-pulse-admission/root-actual-gaussian-pulse-rule.md：3548 bytes；LF SHA256 `963e55eaa5a4ea943e847c61199f964d7c4250eb50fdf86a82fa972387266387`；全文核，保strict residual／修正H约定和同规则conditional正锥运输。
- notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md：9263 bytes；LF SHA256 `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3`。
- notes/585-cofinal-sonin-fixed-source-trace-lower-and-core-error-fee.md：7857 bytes；LF SHA256 `5dca916d978eef599587ff4c6ce34144f814ddec0567a4c1b2314dcd71cd01af`。
- reviews/2026-10-28/fixed-test-lower/common-sonin-vector-and-polynomial-domain.md：16348 bytes；LF SHA256 `dcdf8e91b408423e3647f116f8bd72e040feaf24cf80f9b92db30d776398af85`，只消费已付raw-entire／原norm／共同H₀，不重审所引PDF。
- reviews/2026-10-28/sonin-scalar-normalization/source-upper-and-tail-proof-audit.md：10211 bytes；LF SHA256 `bab769113b4ce8c858dfd4b7a83dea6abd8808436a599d2206ea9a9bf0915fff`，保arbitrary-measurable粗界的准确范围，非本稿必要uniform前件。
- notes/589-sonin-zero-mean-upper-and-scalar-rank-one-limit.md：7185 bytes；LF SHA256 `c491012226713baf0eecff045338563d4e440c6a1bde9eea0d9ccf661b958bc5`，不把其headline fixed-source极限替代本次全S测试证明。
