# 三次 κ 反馈正式论文：独立全文数学与量词审查

2026-10-07。**最终限定 PASS [T/R]。** 本报告将独立新论文作为证据对象，全文读取最终 990 行 TeX，核对 extended plain proof、actual counts 与 strict widths、完整 low、连续证书、实际 κ 反馈、全部 physical 范围、同一 principal tuple、Mellin 和全族反证。修订后的逐槽 mesh 前件明确且已在实际 K 选择中支付。最终稿未发现阻断相对定理的问题。

本结论依赖论文 Definition 1.1 明列的固定外部输入包 R；不是外部整篇证明、全部分析引理、实际素数、kernel、Lean 或 RH 的独立认证。PDF 编译与逐页视觉验收由独立 build manifest 记录，本报告审核数学源与量词。

## 1. 最终绑定与新证据对象

canonical LF SHA-256 仅把 CRLF 和孤立 CR 转为 LF，不去除首尾空白。

| 最终材料 | canonical LF SHA-256 |
| --- | --- |
| [新论文 TeX](../../papers/kappa-feedback-cubic-boundary-paper.tex)，39181 字节、990 行 | 16c0ba50a2917f2ead56843eabf55b62fbbe214e162cff373b4d8554f84315ee |
| [451](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |
| [450](../../notes/450-plain-kappa-extension-and-actual-capacity.md) | f16807e0f80461e3005b3173e313218b00f5f86abfa860a4ead79e425dd6bee5 |
| [精确脚本](../../scripts/hybrid_kappa_feedback_exact_audit.py) | e03d6536378fff4b51625ab71fa5eace9fcbf4fe1156ccb6ae048f03bf96bc68 |
| [审计输出](../../output/hybrid-kappa-feedback-exact-audit.json) | 309f275701a1d96c245eb067d49b00598df4af8e380d220944de250fd2e9d7ba |
| 固定外部 paper.tex | 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 |

固定源为 E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex，提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a。实际源哈希已独立只读重算；它不是由审计 JSON 的 metadata 推定。

阅读先覆盖初版完整 978 行，再覆盖最终 990 行全部内容，包括本轮必要的逐槽 mesh 条件、审计计数与 metadata 范围澄清。此报告只绑定上表最终 TeX，不把初版或 451 的通过替代正式论文通过。未修改 TeX、notes、旧论文、math 或既有审计输出。

## 2. R、主命题与 extended plain proof

第73–140行明确 R 的完整系数、masks、自然零延拓、反射/Gram、global log、moments/detector、prime asymptotics、whole-family 7/8 及 quadratic transfer 等接口。新 κ 区间的 plain 结论不是作为 R 直接假设。β* 在第92–101行包含 1/2、排除 principal pole；唯一 bootstrap 是 β*≤7/8，旧自由 b 边界只用于比较，没有循环引用新数值。

Extended plain proposition 的最终前件第189–217行通过，尤其包括
\[
 \max_i z_i\le\eta_{\rm mesh},\quad
 n_1+n_2+6\kappa z\le M,\quad
 \beta_*\le(1+\kappa)/2\quad(\kappa<1).
\]
mesh 在固定有界长度范围及 ε 后、slot count 前选择，一致于 κ∈[37/50,1]。完整 moving radical、固定 polynomial-size puncture mask、Θ 系数组合、disjoint underlying supports、inducing-family exclusions 和原 seminorm/height 费用全部保留。仅总长度满足 affine budget 不足以调用该命题；最终正文明确增加的逐槽条件是必要范围。

第219–306行是底层 R 上的 proof replay，数值依赖与源第12492–14974行相符：

- Prime contour 真正使用 sκ=(1+κ)/2≥β* 的右侧 displaced line，且 sκ≥87/100；自然零、nonprincipal exclusions、weighted Fourier heights 保留，κ=1 使用 absolute count。
- Terminal 使用 κz≤M/6，不依赖旧展示粗界 z≤2M/9；新 z≤25M/111 足够。
- Comparison 中 6κ−1≥86/25 给 z<25M/516<M/20，差为 1/645；两个 exponent 确实不超过 23M/30+ξ 和 14M/15+ξ，保留 M/15 margin。
- Two transforms、complete support、Möbius indicators、p⁶ pool、第二相关、child decrease、exceptions 和 sixth-power counts 无旧 κ 下限依赖。Clipping 只需 6κ−1≥0，whole-slot greedy removal 费用 κd_z≤F_act/6+η_pool；末段 Lipschitz 只需 0≤6κ−1≤5。
- Zero-slot 优先、同带 uncentered 后 centered、有限深度与 strict drop 的顺序保留；内部高度阶固定后才选 external tail order。

该重证扩大的是数值参数域，底层无限分析 identities/estimates 仍为 R。有限有理审计不证明这段 induction。

## 3. 实际 crossing、严格宽度与 mesh 准入

第313–376行的原 inverse/plain 两支 count 通过。q 是全部 physical slots 的 length-weighted mean，error/zero slots 以零 gain 保留；plain witness 使用两份，未删除第四次 spike。D、P、J、r*(t)、tκ、Rκ 的交点和 long/short 公式一致，保持同一 presentation。不同 physical/witness heights 没有被当成相同 phase。

在 κ∈[37/50,1]、δ∈[1/50,3/4]、x∈[0,1/2] 上，独立核验
\[
 D\ge455/222,\quad P\ge86/111,\quad
 35/48\le J\le5/2,\quad1<t_\kappa<3/2.
\]
写 m=t−r*(t)，在 t=1 有 m=(1−cx)/D≥1/3，t=3/2 时 m=1/2。m 在 t 递增；r*(1)≥8/13，给 inverse zM≤5/26<1/5。Plain zP≤1/(18κ)≤25/333<1/5。并非只用一个不支付 strict widths 的 nominal R。

先减固定 ν0 后两条 marked width 分别为
\[
 1-r-2z\ge2\nu_0,\qquad
 3-2r-8z=4(1-r-2z)+(2r-1)
 \ge8\nu_0+1/5-o(1);
\]
plain width 为 1−2m−6κz≥6κν0。Zero capacity、r≥1、m≥1/2 使用原 no-slot/amplified endpoints，没有强求 shrinking capacity 的固定 marked margin。

最终第683–701行把这些条件应用于实际物理素数：仅 d≥1/2 选择 primes，w_i=e/(Kd)≤2e/K。先固定 count/moment losses、decrement、uniform mesh 和 rounding，再取足够大 even K，故同时满足 max_i w_i≤η_mesh 及 whole-slot rounding margin。之后才取 amplitude/bin widths。原 masks、自然 zeros、Θ 分解、whole conjugation、内部 pool 的 disjointness、S-supported finite exceptional rows 和 cumulative T1/2 均保留。

## 4. 同一 physical probe、完整 low 与 normalizer

第378–488行的补偿表达式保留原 divisibility、q_(p_J)^(-3/2)、同一重标度、shared windows 与 ray data。cn³ completed sums 是无限绝对收敛的和，只有 subsets 有限。Surviving marked slots 先并入 row norm，冻结 J 的 tuple count 配合 q_J 权重与 shortened X' 给 −d_J，避免重复计数。

独立核对 reflected branches 的 s_hyb、actual T_d 及 frozen saving identity：由 H+2A0≤M' 和 z_a≤e' 得 T_d≤H−3d_J+小量；另 2A0−N0+B0+4S0≥0。完整 row energy 为 M'+(5e−1+d_J)_+/4，far annuli 由完整 absolute input 支付。它不依赖 κ，也包含 empty-slot endpoint。

Gram 第三项 P_a²/Y' 被完整保留。P_a∼Z^b≥1，M'≥1−3e>0，lx−d_J、ly−d_J>0。最后
\[
 F_{\rm low}(d)=-d+\tfrac12(11b/6-l_y+d)_+
                   +\tfrac18(5e-1+d)_+
\]
每个 slope≤−3/8；全 J gap ly−e−11b/6>2/25 给最大值在 d=0。完整 low exponent =(1−e)/4−b/6。

第403–409行的 normalizer 核对通过：
\[
 C_b(s)=s+l_x/2-1+h/6=s-2/3-b/6.
\]
Raw z coefficient 为 h−e；exact tuple 在 residue 加 e/6 后合并为 h/6，没有再加第二个 e/6。独立符号验证 C_b 恒等式和 low exponent=C_b(σ*)。

## 5. 新三次证书与全文附录

第144–157、490–587行的根区间、σ/κ/b 参数、A/B/C、Q0 极大点和三次代换通过。独立 general e,b,κ 符号展开验证 −2JE；Q0 的二阶 b 导数恰为
\[
 -\frac{3312\kappa^2-936\kappa+67}{864\kappa^2}.
\]
分子判别式 −11520，故严格凹。极大点、极大值因式均与正文一致；κ=5/6−e/2 后 braces=−p(e)，b 的两个表达式模 p 同余，Q0=0 恰成立。p 的区间端点异号且 p'<0，指定根唯一；与旧 e0 的隔离区间严格分离，得到新边界严格改善，旧边界未被用作 bootstrap。

本次针对新论文增加的表格和附录，独立按其第917–930行公式求 A0,…,A3、B0,…,B2、C0,C1，与 general A/B/C 恒等。使用有理多项式求逆、模 p 约化及 Fraction 区间 Horner，再次核验第554–559行每一个打印的严格 enclosure：
A 在 (47,48)、(121,122)、(86,87)、(29,30) 除以100，C 在 (7,8)、(6,7) 除以100，Q1–Q4 在 (4,5)、(19,20)、(26,27)、(7,8) 除以100。全部严格成立，Q0 精确为零。

第518–519、575–581行的范围区分正确：cleared polynomial F 对任意实 δ 定义且在全部 y≥0 满足 square completion F≥0；E 的有理表达式只在 J≠0 定义，E≤0 仅在真实 J>0 矩形推出。没有将任意 δ 的 F 正性误扩张为任意 δ 的 E 符号。唯一 equality y=0、δ=(5−9e)/(6+18e)、R=2/3 在真实矩形内部；它是 envelope 的等号，不是已构造的坏 witness 或零点。

## 6. κ_act 反馈及所有 physical ranges

第589–653行明确 analytic calls 取 κ_act=2β*−1，不取 κ*。在反证 β*>σ* 下，κ_act∈(κ*,3/4]、差 2Δ；实际满足 β*=(1+κ_act)/2。独立微分 R 给显示正导数，利用 J≥(α−δ)D、D≥2、δ≤3/4、x(1−x)²≤4/27 得 625/36963<1/50。费用小于 Δ/25，h<1，使与实际 C_b(β*) 比较的 endpoint≤−24Δ/25。Reference E 允许等号而不用额外 margin，global Δ 真实支付 losses。

Full selected expression 第631–640行从原 expression 正确展开，conductor deficit 只消费一次，仍保留 eq。在 d∈[1/2,h] 的 slope≥57/200；ζ=Δ/32 延长至 h+ζ 的费用≤Δ/16，留下 359Δ/400。δ、q 的原 bound、protected labels 与 real losses 仍适用。

第657–681行重新核对全部 physical floor/middle/small：floor<-1/200，middle<-1/50，small<-2/25。Floor 为 δ=1/50、R=1、q≤1/100 的无 witness 界；middle 的 δ coefficient 为正，δ=3/4 给上界，不制造新 detector；small 已相对 C_b(β*)，没有再减 Δ。ζ≤(e−1/6)/128<1/384000。5e−h−ζ>1/50 给 e/(h+ζ)>1/5，严格超过 actual inverse/plain requests。

## 7. 无商 tuple、principal 和 outer

第705–787行仍用原 raw kernel、完整 G_p selected sum 和 unselected normal correction，一般域没有误除 H_p。Quotient 只用于已付 near-one principal/dynamic 域；先 global whole-bin move，后 buffered local partitions。

Principal box 的 good/ramified exponents 最弱分别 σ*−3/50>81/100、σ*−1/20>82/100；general 4−6s−6z 项保留 θ=(−Re w)_+。D1 的 εH=min(ε0,1/50) 与 full height/domain 侧条件保留。Small rows 用 D1(1/3) 及 σ*+1/2>4/3，未偷用旧 D1(3/8) 数值结论。

Principal 明确等于同一 Hη(s)=∏_(p∉S)Hp(s,1,1/6)，并保留同一 cS AT；fixed-ray asymptotic 给 AT∼log^-K、最终非零和 subpower inverse。目标前 positive majorant 选 P0 保证 |Hη−1|≤1/2，目标后同一 S 扩大只改善该界。w=19/20、z=33/200、double residue s 线右移至2给 mw、mz、μ 正余量，1/6 residue 未随 e 改变。

Outer 在完整绝对 tuple 的 (2,2,z∞) 支付 B0=7/4−3e/4+b/4；先 ζ 后 target-independent z∞，再小 losses 与固定 height 阶。未把 completed sums 换成 finite sums，未随 row、Z 或 external N 重选 order。

## 8. 共同量词、实际 cutoff 和全族 Mellin

第789–875行量词通过：geometry、whole-family β*、Δ、κ_act 先于 target；losses/decrement/mesh 先于 K；随后 μ=σ*e/(2K)、amplitudes 与 buffers。总 central real costs<Δ/4；各固定物理 margin 和 principal margins 留半或指定份额。m0=min{Δ,mw,mz,μ,1/200,1/50,2/25}、m=m0/4 共同于 target。

目标后固定 arithmetic data、最终同一 S 和 finite internal orders，得到 Aη、Bη 与 actual ceiling τ0η；external N 最后选且不改变内部阶。τ≤m/[4(Aη+1)] 支付 principal/high height loss，N 使 Bη−Nτ<C_b(β*)−m/2，得到共同 σhi=m0/8。Z threshold 可以依赖 target，但共同 ε* 不依赖它。

Jη、fη 本身不含 auxiliary T1。Jη 仅大 Z 定义和归一化，small Z 只使用同一 whole-positive-axis Gaussian fη。Low 总 loss ω=Δ/2，配合 high contract 得 Mellin 在 Re s>β*−ε* 局部一致，其中 ε*=min{Δ/2,m0/8}>0。斜率1与初始 line2 identification 保证延拓的是同一 e^(s−5/6)²Hη/Lη；不需要为目标 zero 跨越 contour。β*−ε*>σ* 与同一 S 的 Hη nonvanishing 排除 numerator cancellation。

β* 不需 attained：supremum 给实部>β*−ε* 的 target zero，所有共同选择已先固定，遂矛盾。有限 Euler deletions 在 Re s>0 不生零，quadratic factorization 在 R 下完成 Dirichlet/zeta transfer，principal pole 允许而边界线排除。该反证没有额外 target-dependent exponent 被当成共同 margin。

## 9. 有限审计的准确范围及最终判定

审计重新执行所得解析输出与上表绑定 JSON 一致；149 是 counted checks，其中98项是49个有限模型的两种 identity 检查，另有未计数 internal arithmetic asserts。Continuous theorem 由 coefficient positivity 和 square completion 支付，不由49样本外推。脚本的 source-hash 字段只是固定 metadata；它不读取或认证外部源、451 或正式论文。本文的实际 source/note/paper binding 由独立读取和 canonical 哈希完成。

最终论文第940–951行已准确写明这些区别。本次额外的 independent symbolic/rational 核查验证 general Q0、κ derivative、打印 rational enclosures 与附录全部 A/B/C coefficients，没有改变脚本或输出。

**最终限定 PASS [T/R]**：在 Definition 1.1 明确 R 下，extended plain admissible slots、actual counts、三次参考证书、κ_act feedback、完整 physical estimates 与同一函数的 family continuation 衔接。未发现尚未支付的新接口。此通过不表示原无限分析输入或外部整篇论文已被重新证明，也不产生 RH 或更高临界线比例。
