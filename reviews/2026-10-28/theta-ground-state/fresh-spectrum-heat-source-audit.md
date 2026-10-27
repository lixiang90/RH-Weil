# C049独立数学逆审：实际谱、热缺陷与fixed源见证

2026-10-28；unit_fresh独占。**限定PASS，无需数学修补。** 两份实际终稿合并闭合固定半线Dirichlet Aθ的两项计数、热迹归一化缺陷和真正compact卷积平方见证；并非消费准入时的WKB问号。扣除最强旧后，这是该实际谱规则的新完整反测，按工作流应统一一数学轮；本稿不自行更新计数／合同／STATE，也不将它升级为经典负源、whole改善、core突破或普遍方法边界。

## 1. 实际恢复、阅读与终版

恢复README／STATE、同G20261027／1793085111、C049与D20261028P、Goal完成门及宏观前沿；check后show通过，核工作树和原cadence。全文读以下两份最终原稿；此前对heat初版只核条件链，没有把未闭(C)消费为结果。回核旧566(13)/(15)、10-14同H/r_p尾及本轮实际定义／准入，按已读563／553／565／577范围去重。没有web、PDF、下载、数值、参数修补、锐化或后继测试；只写本稿。

| 实际LF绑定 | bytes | SHA-256 |
|---|---:|---|
| spectral-domain-and-two-term-count.md | 9724 | 2a233e8b26962158d3fc7f035787c4b9a27d534919986fec398c1524d9bd879d |
| heat-source-and-gaussian-transport.md | 12414 | 0bc229396da45f449be8e0e298ee907db2c2eb34388514364c9f3ea7ec064303 |
| goals/contracts/C049-theta-ground-state-full-gamma-heat-gate.md | 3194 | a792986a9ab25436cf492834d08ae18c29f1996fe9f0d070166b5fe3c2723e21 |
| reviews/2026-10-28/arithmetic-input-construction/theta-ground-state-candidate-admission.md | 5206 | a88149480173e119e429db60024f13fc9860afd78746097ccff8758efc29867c |
| notes/566-source-closed-forms-and-full-weil-heat-trace-tests.md | 10582 | 004f5438c918373e0ead73c0011ffb3883ef872c4977e356911dd910da177053 |

10-14原尾稿仍按LF 55b67be3e867452cb00254dd30953ec430649fc743c97fc15b1a4af3f29c452e消费。准入审查LF 05251a4c…只给执行范围，不证明本次(C)或预定轮数。

## 2. 全n势、准确域与正谱

Hθ使用405全整数求和，不把n=1近似当实际算子。谱稿(3)的R_n有准确有理表达；对D_x=2zD_z、j≤3的同一可和majorant，确能支付全n逐项导数及ρ的O(z^j e^(−3z))尾。分母1+ρ≥1，因此log导数、V及V′的误差链成立。

已独立核代数：w₁=9/2−2z+3/(z−3/2)，V₁=4z²−22z+33/4+3/(z−3/2)，V₁′=16z²−44z−6z/(z−3/2)²。全势由此终严格递增、为正，且全局与4π²e^(4x)相差O(e^(2x))。旧H尾／V leading已扣，新增前件是实际计数所需的全n导数控制及终单调；未依赖早期非正式常数81/4。

core分部积分确给q=∫(|f′|²+V|f|²)，下上势界使q加固定L²项与H¹及e^(4x)加权范数等价；q≥0又允许换为q+||f||²。因此准确闭型域为H₀¹(0,∞)∩L²(e^(4x)dx)，端点是算子x=0的Dirichlet。尾cutoff、有限区间内部光滑逼近与反向Cauchy闭合均在同一范数内；没有偷偷取maximal一阶域。

表示算子域的分布写法与该闭形式一致，局部H²正则性足够，未误称全局H²。紧嵌入由有限区间H¹紧性与统一weighted尾闭合。q[f]=0迫f=cHθ，而Hθ(0)>0和Dirichlet迫c=0；compact resolvent再排0谱聚点，故λ₁>0。全线Hθ没有被当作本Dirichlet域零模。

## 3. 严格计数：分割的是Schrödinger能量

关键分割在∫(|f′|²+V|f|²)上完成。人工切口DD／NN是该能量的标准域包含关系；若切原平方会带Robin项，原稿明确没有这样做。Neumann尾仍有V→∞的紧性，V>E几乎处处排除≤E谱；转折点恰落切口不赠零态。

常势DD／NN的floor计数在E=v时也保≤1误差；每格只付一次。有限初始区间上下计数为x₀T/π+O(1)，它的相位积分为x₀T+O(T⁻¹)，没有丢失head的线性T贡献。终单调段取δ=T⁻¹/²，格数O(√T(1+logT))；左右Riemann和差≤δT，转折点导数无界也不影响此估计。故谱稿(14)的严格余项成立，而非引用WKB。

全势与纯指数相位积分的差用|sqrt(A_+)−sqrt(B_+)|≤sqrt|A−B|及实际支撑并集，付到O(√T)。纯指数积分的准确换元与有余项展开给T[log(T/π)−1]/2+O(T⁻¹)。因此本次原谱计数确为

\[
N_\theta(T^2)=\frac{T}{2\pi}[\log(T/\pi)-1]
 +O_\theta(\sqrt T(1+\log T)).
\]

这里每个半线本征值按重数计一次，没有±2；常数依固定原H，不依T。全n尾、域、分割、相位误差及线性常数同链闭合，足以兑现heat终稿的实际(C)。

## 4. 热常数、原源费用与共同Gaussian

ν_T按每个√λ_j的正负两原子定义，因此M_T=2Nθ(T²)，hat W_T=2πν_T。热迹应是2Tr e^(−tAθ)=4t∫T e^(−tT²)Nθ(T²)dT，不能再除2。Stieltjes两端、低T有限head与普通trace-class由实际谱计数付清。

独立核Gaussian矩与ψ(3/2)=2−γ_E−2log2后，θ侧为

\[
\Theta_\theta(t)=
\frac{\log(1/t)-\gamma_E-\log(4\pi^2)}{4\sqrt{\pi t}}
 +O_\theta(t^{-1/4}\log(2+1/t)).
\]

余项来自已证O(√T logT)，为o(t⁻¹/²)。完整目标的旧log(16π²)、FP/contact、全部primepowers及2e^(t/4)双pole保持，故

\[
\lim_{t\downarrow0}\sqrt t\,[\Theta_\theta(t)-\Theta_\zeta(t)]
 =\frac{\log2}{2\sqrt\pi}>0.
\]

这个方向是固定规则热量偏多，不是Qζ负号。目标未被换成未知实零点的平方频率和。

物理时间u与算子x分离。每层B_T的L¹费M_T、fixed窗du费2LM_T及原zero-extension Dlog的1/log2运输准确，strong费用按r=e^(u/2)f本身支付。原子evaluation无globaldu统一界；谱多项式增长给fixed complex compact／S_exp源逐一尾T^(1−2m)logT，不是moving／成长窗统一结论，也未强加逐层exact消405。

Gaussian桥没有滥用D′：θ侧按已付正温和测度作用Schwartz，完整Wζ侧按完整Γ multiplier及其L¹／二阶导数界、全部pp的Σ(logn)n⁻³/²与pole指数权作用S_exp。共同χ_Rk_t在每fixed t下于这些域收敛；卷积半范数保证χ_Rk_(t/2)的平方趋k_t。故若D′目标身份成立，固定compact test后共同crop极限确迫热身份，和上式矛盾；没有交换未付的joint R/T/t极限。

更强的实际见证也闭合：先固定足够小t使δ_t>0，再选有限R令r=χ_Rk_(t/2)的极限型差>δ_t/2，最后T足够大给Q_T(r)−Qζ(r)>δ_t/4。此后r及其physical前像e^(−u/2)r均固定compact，不能误说是不断移动源或17/16窗负源。两型可以同时为正。

## 5. 强旧净后果、轮数与精确停止

已扣10-14同H/r_p尾、566完整目标两项及旧具体图失败；未把旧非局部E_g、K_div或565 Gaussian selector认作同一Aθ。旧“自动平方不自动有heat身份”是责任，不能直接决定这次实际谱的定量缺陷。本次确有严格的同对象两项谱估计、归一化热差及fixed原源不消失差，区别于只重复正平方／旧leading／目标公式。

因此建议按RESEARCH_WORKFLOW统一消费**一完整数学轮**，两个原稿／本审／来源恢复／推送不另计。这个判断来自实际终稿闭合的新净反测，非由准入PASS、C049编号或达到cadence4的需要预保证。本审不改原cadence3／历史49／cycle16（LF cc6877d133b9b9fabd57f199b2433fa4d3fea02a5786b61727cd8f8479d4d2db）；实际统一结算由root执行。

停止原半线Dirichlet、原x尺度／H幂／±倍数及常数的谱recipe，不调sector、补偿或再拟合。不同连接、非局部／relative、其他强源或有新输入的修复未被本定理排除，也不自动获准。

局部未知已改变：这个实际theta谱规则的完整Weil身份已被严格排除。独立全局signed/corecross／非零primitive mixed／Ξ仍未付，whole4/5仅负惯性UPPER、585必要费／safehigh保持。本次不是RH反例、所有confining类no-go或Goal完成门；同实例长期Goal仍active、open／noteligible。本审不认证尚待root执行的结算、发布或远端核验。

## 6. 586消费草稿的附核

另全文读notes/586-theta-ground-state-spectrum-and-full-gamma-heat-defect.md的消费草稿，并实际核最终修订6098 bytes／LF 417da8333f9940db9c3b929ae72c493e9beb2ffdcaec7f43112d56cc92537e9a。其短链、固定compact反测、cofinal同一极限和停止范围与两raw一致，首段仍明确pending最终消费／结算。

已提出并核闭两处容易误读的短链措辞：初始compact段保x₀T/π的计数贡献及x₀T相位贡献，只把二者比较误差记O(1)；Neumann尾保V≥T²且几乎处处严格大于，再排≤阈值谱。纯指数积分排版也已修正。这些是消费摘要精确化，原raw证明无须改动。附核绑定的是这个待消费草稿，后续root状态／receipt链接变更不由本稿冒称已完成。
