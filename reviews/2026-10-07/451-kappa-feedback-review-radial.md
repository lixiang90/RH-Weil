# 451 的实际 κ 反馈、三次边界与全族延拓：独立全文审查

2026-10-07。结论：**限定 PASS [T/R]**。全文核读 451、450 及新精确脚本，并核对实际固定源。未发现阻断该相对命题的代数、参数准入或量词错误。这里的 PASS 是在明确原 [R] 下对新推导的审查；不是外部整篇证明、无限分析底层引理、实际素数、kernel、Lean、RH 或新的简单临界线比例的独立认证。

## 1. 绑定的最终材料与审查方法

所有下列 SHA-256 均对 UTF-8 文本仅作 CRLF→LF、孤立 CR→LF 后计算；不裁剪空白。

| 材料 | canonical LF SHA-256 |
| --- | --- |
| [451](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md)，244 行 | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |
| [450](../../notes/450-plain-kappa-extension-and-actual-capacity.md)，122 行 | f16807e0f80461e3005b3173e313218b00f5f86abfa860a4ead79e425dd6bee5 |
| [新精确脚本](../../scripts/hybrid_kappa_feedback_exact_audit.py)，291 行 | e03d6536378fff4b51625ab71fa5eace9fcbf4fe1156ccb6ae048f03bf96bc68 |
| [新审计输出](../../output/hybrid-kappa-feedback-exact-audit.json) | 309f275701a1d96c245eb067d49b00598df4af8e380d220944de250fd2e9d7ba |
| [逐源 lower-κ 推导](hybrid-critical-count-witness-research.md)，324 行 | a1a6146b8f5e0b82b0e7e642e323398aece00d0a3488cce3d6f146974332dff8 |
| 外部固定 paper.tex | 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 |

外部源为 E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex，固定提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a。本次只读重算其文本哈希，符合 451 §1 与 450 的绑定。

本次不是仅引用此前 plain κ 审查：读取新主稿全部 244 行、450 全部 122 行、脚本全部 291 行；重新执行新脚本而未改写输出，所得解析 JSON 与绑定输出完全相等，149 项 PASS，包括 49 个有限直接模型。又独立用通用符号 e,b,κ,y,δ 核对新二次式、Q0 最优值、三次代入、b 的约化及 κ 导数。未执行旧审计，未编辑 notes、旧论文或 math 源。

## 2. 精确三次根和 general κ 连续证书

451 §1、§3 通过。根隔离区间两端的 p(e) 符号相反；在 (1/6,167/1000) 上 p'(e)<0，故指定根存在且唯一。代换 σ=11/12−e/4 给正文指定的 σ 三次方程。与旧自由 b 正根的有理隔离区间严格分离，故新的 σ* 严格小于旧 σ0；比较不依赖显示小数。

以 c=1/(3κ)、x=1/2−y 独立展开原 R，验证
\[
 -2JE=A(y)\delta^2-B(y)\delta+C(y)
\]
以及正文的每个 A、B、C 公式。此处 E=K+Wδ−h(1−R)，W=1/2+3e/2−ey；原 e q 项保留，q=δx。

独立求 Q0=4A(0)C(0)−B(0)^2 关于 b 的导数，得到正文一般最优 b。二阶导数恰为
\[
 \partial_b^2Q_0
 =-\frac{3312\kappa^2-936\kappa+67}{864\kappa^2}<0.
\]
分子二次式的判别式为 −11520，故所谓“极大点”有严格凹性支持。代入最优 b 后，最大值正好是 451 第101–103行所显示的式子，包含所有 25、162 和 κ 因子，没有使用新参数数值拟合。

再代入 κ=5/6−e/2，方括号严格等于 −p(e)。正文 b 的两个表达式之差的分子模 p(e) 余数为零。故 Q0=0 及闭式 b 均正确。

脚本把 e 的系数表示为有理基底 (1,e,e²)，模 p(e) 精确运算；p 在模7无根且保持三次，因此是有理数域上的不可约三次式，求逆所用三维域合法。脚本的有理区间 Horner 包含指定实根，所有符号断言都使用严格区间下界，而非小数近似。

重新核对 A 的四个系数、C 的两个系数、Q1,…,Q4 全部严格正、Q0 恰零，因而
\[
 A(\delta-B/(2A))^2+\frac{Q}{4A}\ge0
\]
对全部 y≥0、实 δ 成立。在真实矩形 δ∈[1/50,3/4]、x∈[0,1/2] 中 J>0，故 E≤0。等号只可能 y=0，再有 δ=(5−9e)/(6+18e)=B0/(2A0)，它严格位于矩形内部；该点 R=2/3。49 个有限模型仅核查恒等式及实现，没有被用于证明连续域正性。

## 3. 450 的新准入与实际 κ 反馈

450 是在底层 [R] 上重做 generic plain proof，不能被解释为直接援引源仅声明 κ≥3/4 的 lemma。其摘要忠实于逐源推导的完整范围：原 moving residue factors 的完整 radical、相同有限群系数展开、自然零延拓、固定 polynomial-size masks、whole-product conjugation、原 profiles 与全部高度均保留。

逐源核对的关键依赖是源第12492–14974行：

- global prime estimate 使用 sκ=(1+κ)/2≥β*，平方槽费用 Z^(κz+ε)；κ≥37/50 使 sκ≥87/100，未跨入新 principal residue。
- 第12932行旧 z≤2M/9 只是展示的粗界；终端真正使用的是 κz≤M/6。新 z≤25M/111 足够，后续没有把 2M/9 偷用于别的递归。
- 第12949–12980行的 comparison 需要 z<M/20。现在 6κ−1≥86/25 给 z<25M/516<M/20；两个更精确指数为 197M/258+ξ 与 40M/43+ξ，分别严格小于 23M/30+ξ 与 14M/15+ξ，因此原 M/15 的共同 margin 保留。
- two transforms、whole support、Möbius indicators、pool p⁶、child exceptions、sixth-power amplification 不要求 κ≥3/4。后续 child affine budget 只需 6κ−1≥0，greedy removal 费用 κd_z≤F_act/6+η，最终数值 Lipschitz 只需 0≤6κ−1≤5。
- 所有 zero-slot case 先于 positive-slot induction，有限深度、strict drop、共同 uncentered/centered 顺序保留；mesh 在固定区间和损失后、slot count 前取，内部 seminorm/height 阶在实际槽数据固定后取，外部 tail order 不得倒改内部阶。

实际 crossing 的 Dκ、Pκ、Jκ、r*、tκ、Rκ 由同一个 inverse/plain witness 的 counts 相交所得，两份 plain witness 的四次 spike 未删除。未假定 physical 和 detector 的不同 witness heights 有相同 phase。

451 第124–142行尤其正确区分 reference κ* 与 analytic κ_act：反证 β*>σ* 时实际调用 κ_act=2β*−1，满足 β*=(1+κ_act)/2；由旧 whole-family 7/8 输入它位于 (κ*,3/4]⊂[37/50,1]。κ* 仅用于前节代数证书，不能直接喂给 positive-slot theorem。

独立微分得到
\[
 \partial_\kappa R
 =\frac{(\alpha-\delta)^2\delta x(1-x)^2}
 {3\kappa^2J^2}\ge0.
\]
利用 J≥(α−δ)D、D≥2、δ≤3/4、x(1−x)²≤4/27，得上界 1/(108κ²)≤625/36963<1/50。由于 κ_act−κ*=2Δ，反馈费用小于 Δ/25。h<1，且 C_b(β*) 比 C_b(σ*) 增加 Δ，所以 high endpoint ≤−24Δ/25。没有参数循环或未成立的 reference zero-free 假设。

## 4. 完整低侧、物理范围和 strict slots

451 §2、§4–§5 的新参数准入通过，不能从旧数值 margin 直接照搬。e∈(1/6,1/5)、b>0，M−2d_J≥1−3e>0，lx−d_J、ly−d_J>0；full-J Gram gap >2/25。原 compensated subset、q_(p_J)^(-3/2)、shared windows、rays、有限补偿及同一 normalizer 保留。原 low reflected energy 的完整第三项已包含：
\[
 F(d)=-d+\tfrac12(11b/6-l_y+d)_+
                 +\tfrac18(5e-1+d)_+ .
\]
每个分段斜率≤−3/8，最大在 d=0；两项正部在 d=0 为零，故完整 low exponent =(1−e)/4−b/6=C_b(σ*)。这一步不依赖 plain κ，也未省略第三项。

selected d∈[1/2,h] 的完整 high expression 在 451 第146–148行正确；斜率 R+δ/2−17/50≥57/200，故 endpoint 的上界控制全部此范围。ζ=Δ/32 的延长费用≤Δ/16，留下 359Δ/400；没有把 fixed reference E=0 当作已有严格 margin。

用代数根的有理区间重新核对：
\[
 l_y-e-11b/6>2/25,\quad 5e-h-\zeta>1/50,\quad h+\zeta<1,
\]
\[
 E_{\rm floor}<-1/200,\quad
 E_{\rm middle}<-1/50,\quad E_{\rm small}<-2/25.
\]
floor 是原 δ=1/50、R=1 的无槽端点；middle 是原 R=76/75−2δ/3 配合 q≤δ/2，不是额外 witness。small 已相对 C_b(β*) 支付，不能再误减一个 Δ。ζ≤(e−1/6)/128<1/384000 由 Δ≤7/8−σ* 导出。

D≥2、P≥3/4、J≥35/48 给 crossing 的合法 t。完整 crossing 还给 r*(1)≥8/13>3/5、r*(3/2)=1、1/3≤m=t−r*≤1/2。因而 inverse zM≤5/26<1/5，plain zP≤1/(18κ)≤25/333<1/5。e/(h+ζ)>1/5 为严格共同供槽余量，450 的保守表述充分。

先减固定 ν0，再取 whole slots，使
\[
 1-r-2z\ge2\nu_0,\qquad
 3-2r-8z=4(1-r-2z)+(2r-1)
 \ge8\nu_0+1/5-o(1),
\]
\[
 1-2m-6\kappa z\ge6\kappa\nu_0>0.
\]
r≥1、m≥1/2 与零容量仍用原 no-slot endpoints；没有对 shrinking width 强行索取固定 marked margin。Θ exceptions、原 finite-ray coefficients、underlying disjointness、natural zeros、whole conjugation、同一累计 T1/2 及全部 height/profile 费用均在准入范围中。

## 5. 完整 tuple、principal、outer 和全族闭合

451 §6 在新参数上重新满足先前已推导的一般域，未偷用只按旧参数命名的结论。D2* 的 good/ramified margins 分别满足 σ*−3/50>81/100、σ*−1/20>82/100，含 4−6s−6z 项的 θ=(−Re w)_+ 没有遗漏。一般 tuple 保留 G_p 的无商系数式，quotient 仅在近1域使用；先 global contour 后 buffered local partitions，whole-bin 的统一性保留。

small rows 改用 D1(1/3)，其 σ*+1/2>4/3 已核；不沿用写成 D1(3/8) 的旧 small lemma。large rows 的绝对 tuple 在 (2,2,z∞) 支付原 B0=7/4−3e/4+b/4；先 ζ 后目标前的 z∞、real exponents 与 height 阶，completed c n³ sums 是真正完成的和而非有限和。

双 principal 留数仍是同一 c_S A_T，Euler 因子严格绑定
\[
 H_\eta=\prod_{p\notin S}H_p(s,1,1/6).
\]
目标前 positive majorant 固定 P0 并保证 |Hη−1|≤1/2；最终同一 S 只扩大。原 fixed-ray asymptotic 给 AT 最终非零与 subpower inverse。w=19/20、z=33/200、主 s 线仅右移到2及 buffered shifts 的准入，给 mw=ly/20、mz=h/600 与正 μ。这里没有因 e 改变而移动 1/6 principal 留数。

451 §7 的量词顺序通过：全族 β*、Δ、κ_act 和几何先于 target；count/moment losses、capacity decrement、mesh 和 rounding 先于 even K；再取 μ=σ*e/(2K) 及 amplitude/prime/buffer losses。中央其他总费用<Δ/4，加上已支付的 ζ 后仍充分大于 m0/4；floor/middle/small 保留各一半固定 margin。

m0=min{Δ,mw,mz,μ,1/200,1/50,2/25} 与 m=m0/4 都共同于 target。目标之后只固定 arithmetic data、最终同一 S、内部有限高度阶和 Aη、Bη、τ0η；外部 N 后选且不改内部阶。先 τ≤m/[4(Aη+1)] 再大 N，两个合同项均可压至共同 σhi=m0/8。Jη、fη 不含 cutoff T1，因而没有通过选择 T1 改变 principal function。

完整 low 与 AT inverse 的总 loss 取 ω=Δ/2，在全族 bootstrap 后而非目标后任意调 Δ。于是 low 斜率与 high error 给 ε*=min{Δ/2,m0/8}>0，共同于 target。Jη 只需在大 Z 定义；Mellin 作用于由同一 Gaussian principal integral 在整个正轴定义的 fη，其小 Z 衰减来自原右移。原初始识别线2和 C_b 斜率1保证 Fourier/Mellin 识别不换函数。延拓在 Re s>β*−ε* 局部一致，且同一 S 上 |Hη|≥1/2 排除 numerator 抵消目标零点。supremum 无需取得：存在实部超过 β*−ε* 的目标零点即可矛盾。

## 6. 审计与 [R] 的准确边界

新脚本的代数域、求逆、根隔离、区间符号、连续系数、几何不等式和反馈分数均可核验。原样执行得到与绑定 JSON 相同的 149 项，49 个直接模型不承担无限域证明。独立通用符号检查还覆盖脚本没有单独输出的 general Q0 极大点、严格凹性、极大值因式、三次代入和 reduced b。没有以运行成功替代数学准入。

限定 PASS 的底层 [R] 包含 445/449 明确继承的原 complete-probe estimates、generic marked/inverse 和 plain induction 的分析组件、adaptive detector、global prime bounds、Euler coefficient tables、反射能量/完整 Gram 与 smooth/Gaussian calculus、shared-contour 与 principal Mellin identification、whole-family 7/8 输入和 quadratic factorization。450 的 lower-κ 重证是在这些底层输入上推广原 proof 的数值区间；本审查没有独立重新证明这些所有无限分析引理，也未审核外部整篇 paper.tex 的每一行。

在这些准确输入下，451 的新相对边界、实际 κ 反馈及同一函数族 continuation 没有未支付的新接口。它不推出 RH、不提供绝对认证的 kernel theorem，不计算新的简单临界线比例，也不改变已交付的 69999 或自由 b 论文。
