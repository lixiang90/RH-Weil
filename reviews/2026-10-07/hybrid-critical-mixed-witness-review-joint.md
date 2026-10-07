# Critical mixed witness：joint 独立全文审核

2026-10-07。审查人：joint。只写本审查；不修改被审研究报告、冻结论文、450/451、原审计、脚本、输出或只读 math。

**结论：PASS。共同 presentation/zero、实际 mixed plain 合同、连续有理邻域、双 t core 和真实 mixed 系数均通过独立核查。本轮新 draft 的两处范围歧义及联合 stratum 明示已经在审查过程中修订。报告未证明新的 χ、covariance saving 或零自由边界。**

## 1. 内容绑定与验证范围

被审对象是 [实际 critical 研究报告](hybrid-critical-neighborhood-mixed-witness-research.md)。首次完整审读版本 canonical LF SHA-256 为 cb05874517ff2eb9f676db610df3b5ff7e6e94610e1f0d263bb76c891bc9f605，313 行；本审查回读全部新 draft 修订后的最终 freeze 版本为：

**ef85a5e5fd5aef3543aef6eb4b6adff6a1ecd39791575a89704e4b08e04e8983，313 行，canonical UTF-8 19827 bytes。**

canonical hashing 仅作 CRLF→LF、孤立 CR→LF。以下绑定本轮由文件内容重算：

| 对象 | canonical LF SHA-256 |
| --- | --- |
| papers/kappa-feedback-cubic-boundary-paper.tex | 16c0ba50a2917f2ead56843eabf55b62fbbe214e162cff373b4d8554f84315ee |
| notes/450-plain-kappa-extension-and-actual-capacity.md | f16807e0f80461e3005b3173e313218b00f5f86abfa860a4ead79e425dd6bee5 |
| notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |
| scripts/hybrid_kappa_feedback_exact_audit.py | e03d6536378fff4b51625ab71fa5eace9fcbf4fe1156ccb6ae048f03bf96bc68 |
| output/hybrid-kappa-feedback-exact-audit.json | 309f275701a1d96c245eb067d49b00598df4af8e380d220944de250fd2e9d7ba |
| 实际只读 source paper.tex | 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 |

Source 完整路径为 E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex。被审报告引用的 commit 为 adc7f1241b42e322a6451854ab7e4b4c146bf78a；本审查直接认证所读内容 hash，不把 commit 字符串或 JSON metadata 当作内容认证。

本次独立完整审读新报告，直接读取 source 的 row presentation、buffered bins、pointwise dyads、detector、plain/marked 条件、原 amplification 与 physical prime selection。未把别人的 PASS 或有限模型作为连续证明。

另外在内存执行 Fraction 与 SymPy：连续 box 的有理端点及 strict margins；optimizer 三条 affine count 交点；critical 恒等式模 p(e) 的精确余式；方向小数核对。无新脚本、任意矩阵或数值模型，未重跑无变更的原 149 项审计。

## 2. 同一 ψ/zero 的有限多 t：PASS

Source buffered bin 先在有限 Xu 中选取达到 M_i(u) 的真实零点。Nonfloor bin 可固定一个 presentation ψ 和 ρ=σ+iγ，满足 a≤σ<a+e、|γ|≤3iT1。Deleted Euler factors 在该区域无新增零，该零点可以进入 L_orig(ρ,ψ)=0 的 detector 构造。

Detector proof 的顺序是先固定 zero，再令 D*=U^t。Gamma contour、Y*=U^20、terminal U^21 和 shifted-line bound 对 1≤t≤3/2 一致。因此对有限多个预先固定的 t_j，可分别执行同一 proof，保留同一 ψ、ρ。这依据 proof 内部的选择顺序，不能仅从 proposition 的“每个 t 存在”交换量词。

每次保留准确的
\[
 W_{M,j}(y)=W_1(y)V_{\le}(D_jy/U^{t_j})
 y^{-\sigma-i(\gamma-\nu_j)},\qquad
 W_{S,j}(y)=W_2(y)y^{-\sigma-i(\gamma-\nu_j)}.
\]
支持、truncated cutoff 与自然零没有改写。D_j/U^t_j≪1，必要 untwisted annular seminorms 一致有界；这个 cutoff 不产生第二 separating frequency。

联合 dyadic choices 为 O((log U)^(2J))。Presentation labels 有限，可先 subdivision；共享 presentation 的有限-ray character 固定于 rowsum，和 Fourier extraction ν_j 是不同对象。

缩小 |ν_j|≤c_JT1 仍可 extraction：Fourier L1 mass 一致有界，外部 tail 有任意固定阶衰减。先固定 c_J>0、长度和 height orders，再用 T1=Z^τ 与足够大的 external N 吸收固定 arithmetic power。全部 separating variables 分摊同一个 T1/2，不能在不同 shifts 重复领取。

有限参数 Sobolev 产生固定 (1+T1)^A_J，order 先于 external N 固定，然后选择小 τ。共同 γ 不意味着 ν1=ν2；报告没有这种错误约束，也没有断言连续 t 的 maximizer 相容性。

## 3. 实际 mixed plain 与 count：PASS

两个 S 使用同一完整 zero-extended ψ。对两个 S 和一次 Q_I 作 whole conjugation后，physical prime coefficients 正是 source 固定有限 Θ expansion。Underlying supports 在 masks 前仍 disjoint；原自然零和 deleted radical 全部保留。

固定 presentation label后，额外 moving radical为零、row norm为U，effective width 为1。报告“共同 ν 在Θ”是有限-ray presentation label，不能读成两个 Fourier extraction parameters 相等。不同 profile heights 使用原 smooth/Sobolev allowance。

Source 原 lemma 显示 κ≥3/4；此报告在 [37/50,3/4] 使用的是已经独立审核的 extended plain contract，没有声称原 lemma 的文字覆盖该区间。实际条件仍为 κ_act=2β*−1，reference κ 不提供新的 zero-free input。

令 s=m1+m2、q=δx、c=(3κ)^−1。原 moment 与实际 spikes给
\[
 G(s)=1-\delta s-\frac{q}{3\kappa}(1-s)
     =1-\delta\{cx+(1-cx)s\}.
\]
因此
\[
 G(m_1+m_2)=\tfrac12\{G(2m_1)+G(2m_2)\},\qquad
 G'(s)=-\delta(1-cx)<0.
\]
cx<1 有固定裕量。较大 actual m 的 double-copy plain pair 合法，capacity request 更小。重复 S 不构成重复 prime slot。固定供给截断后的 G_Λ 在每段也严格下降，转折处连续。

Source 明确允许 z=0 时全部 bounded n1,n2，不要求 n1+n2≤1。所以 m≥1/2 的 zero-slot branch 合法，不能将 positive-slot 条件延伸到此处。Strictness、whole-slot rounding 和 mesh 只付小误差，不产生固定 power gain。Hölder 组合既有 moments 只给这些 rates 的 convex combination；报告未把这点升级为任意未证 mixed theorem 的最优性。

## 4. 原 coefficient class 与本轮 draft 修订

Reused Q_i 破坏 pre-mask support disjointness并包含 p=p 的 prime-pair diagonal。若把 ψ(p)^2 硬折为一次 ψ(p)，coefficient 含 row-dependent ψ(p)，不属固定 Θ list。改变 numerical length 不能修复合同；此检查通过。

M_r1 M_r2 的 coefficient 是 weighted truncated μ⊗μ convolution。n=p²ab 的两个 squarefree factors各含一次p时，非零 μ-products的符号由总 prime multiplicity确定；positive untwisted profiles 可使 coefficient非零，而 μ(n)=0。这是 class identity 的反例，不是 constructed saturated bad row。

M_r S_m 的单-divisor例需要 m<r<2m，且 a squarefree、与p互素。q_p∼U^m、q_a∼U^(r−m) 时，1,p,a低于inverse annulus，p²,p²a高于它，只有pa留下，所以 coefficient非零而 μ(p²a)=0。

首次版本仅写“临界 r>m>0”，一般不足以排除 p²。根节点本轮已将新 draft 修订为明确 m<r<2m、a取另一互素prime ideal，并列出所有其他 divisors；本审查已直接回读修订句。第5节的增强 bounds 还保证所用 short core 的 r_s<2m_s 有统一正裕量。

Full μ*1 的 unit identity 不能用于这些截断 annuli。仅凭 d(n)≪n^ε，arithmetic divisor coefficient也不成为只依赖norm的annular smooth profile。原 scale-supremum amplification已付；再乘pointwise bound会取消相应 saturation spike。全部结论只限制既有 theorem 的直接调用，不排除新 correlations。

## 5. 连续 box：精确有理证明通过

独立使用
\[
 \alpha=5/6,\quad B=2-2cx,\quad D=3-(1+2c)x,\quad
 P=B(1-x),\quad J=(\alpha-\delta)D+\delta P.
\]
整个 box 的单调性直接给
\[
 c\in[4/9,50/111],\quad B\in[172/111,352/225],
 \quad D\in[455/222,1867/900],\quad
 P\in[86/111,1496/1875].
\]
无 finite grid。正数端点比较给
\[
 J_{\min}=785/666,\qquad J_{\max}=3428821/2700000.
\]
由 δP/(2J) 可统一使用更强的
\[
 t_{\min}=\frac{141378877}{126866377},\qquad
 t_{\max}=\frac{2785237}{2453125}.
\]
独立代入报告给的 numerator bounds得到
\[
 r_{\min}=\frac{6121636065950}{8763802456783},
 \quad r_{\max}=\frac{17586076411}{23917968750},
\]
\[
 m_{\min}=\frac{94366732557}{236859525859},
 \quad m_{\max}=\frac{69993086221}{167425781250}.
\]
r使用 Bt−(1−c)x 的端点，m使用 ((1−x)t+(1−c)x)/D；不假定各端点可同时达到真正 extremum。

严格有理比较蕴含报告的
\[
 1.11<t_0<1.14,\quad 2/3<r_0<3/4,\quad
 3/8<m_0<9/20,
\]
并给
\[
 R_0-(1-\delta)\ge\frac{6288750}{126866377}>1/25.
\]
Symbolic rational algebra还独立给
\[
 A_I(r_0)=P_{\rm count}(m_0)=L(t_0)=R_0,\qquad
 m_0=\frac{(1-x)t_0+(1-c)x}{D}.
\]
三条 slopes满足
\[
 s_I\ge3/16,\quad s_P\ge43/74,\quad
 s_L\ge13/30,\quad s_I^{-1}+s_P^{-1}\le910/129.
\]
因此4(910/129)/100<1/2是连续严格裕量，不依赖取样或小数。

以v≤1/100、θ=v/100为界，增强端点给
\[
 r_s\le r_{\max}+\frac{4}{10000\,s_{I,\min}},\qquad
 m_s\ge m_{\min}-\frac1{100}
 -\frac4{10000\,s_{I,\min}}-o(v).
\]
这蕴含 r_s−2m_s<−0.035 加可预先缩小的 witness loss，确证第4节的 critical class example适用。

## 6. 双 t core 的实际 branch：PASS

在t_-，r≥1使用原sixth-power amplification的active L(r)分支。r≤t_-+o(1)给 count≤R0−s_Lv+o(1)，有超过4θ的improvement。

其余r<1中，inverse threshold r0+4θ/sI>2/3合法使用positive-capacity marked moment；第二width有固定margin。r接近1的预先固定小邻域，用 R0−(1−δ)>1/25 的 no-slot/amplified bound，避免索取shrinking marked margin。Strict ν0减量和whole-slot mesh可预先控制。

Plain threshold在整个box低于1/2，之后用原zero-slot plain。所有requests<1/5，由冻结几何 e/d>1/5支付。Short upper bounds与actual support给(12)的lower bounds。固定正v、θ后可按原顺序取small losses、profile/height orders和τ、N。

首次版本在t_+写“再次除去满足同样 inverse/plain improvements”，字面未限定inverse为r<1。A_I(r)不能用于r≥1，否则会错误用短marked合同删掉长core。根节点本轮已修订新draft，显式仅对r<1作short inverse removal，长branch留给L(r)；本审查已回读。

按此正确范围，剩余r<1满足
\[
 r+m\le t_0+4\theta(s_I^{-1}+s_P^{-1})<t_0+v/2,
\]
与t_+的actual saturation support矛盾。所以余核ℓ≥1；再用真实L(r)删除ℓ<t0−4θ/sL，即得(13)。

4θ至θ的预留margin可支付subdivisions、witness losses、strict decrement、slot mesh及最后small height power。仅从显示式(11)的(1+T1)^A本身不能宣称零height费用；应用时仍须选择τ。报告明确保留此条件，conditional χ的最终count也使用同一reserve。

该命题是实际moments对rows的partition，不是abstract LP。没有推断core非空、达到U^R0或某实际row实现理想同步饱和。

## 7. Critical 等式、mixed 原系数与 χ：PASS

对既有隔离positive small root e，独立计算以下rational differences的分子模p(e)=657e³−954e²+21e+20的余式全部为零：

- t0−(1+3e)/(8e)；
- r0−(2/(3δ*)−1)；
- R0−2/3；
- 2δ*m0+δ*z0−1/3。

分母含e、3e+1、9e−5、153e²−201e−20，均在既有strict隔离区间上非零。不能仅由零模余式略过分母。所有方向小数吻合，包括1+δ*t0≈1.43685595565507、raw length≈1.98204395667734。κ*仅显示reference intersection，实际moments仍需κ_act。

对于(16)–(18)，先固定联合dyadic stratum的ℓ、m_s和一次selected prime tuple/total z，再求和，最后有限subdivisions合并。前文O((log U)^(2J))及有限slot choices已支持此步骤。根节点本轮已在§6.1显示式前明写这个已付步骤，本审查直接回读最终句；它不增加数学input。

在每个固定stratum，pointwise inverse与合法plain fourth确实给
\[
 H_{\rm mix}\ll U^{1+\delta\ell+\epsilon}(1+T_1)^A.
\]
Actual spike是δℓ+2δm_s+2qz，Q只使用一次。临界identity给count恰2/3。一般参数的
\[
 2\delta m_0+2q\frac{1-2m_0}{6\kappa}=1-R_0
\]
也已独立符号核对，没有未付余量。

展开coefficient为准确μ(a)、两条plain columns、一次prime tuple和同一ψ(abc∏p_i)。Normalized scale为U^(-(ℓ+2m_s+z)/2)。固定Θ coefficients、physical profile、原自然零、deleted radical与primitive conductor均保留。

Full μ*1*1=1正确，但实际Gamma/truncated inverse和short annuli不能据此collapse。剥去共同γ、σ后仍有例如q_a^(i(ν_+−ν_-))的divisor-dependent factor及不同cutoffs。即使差频为零，也未支付补齐其他dyads的signed correlation。Frozen plain rows的weight不属固定Θ inverse-column coefficients；其displayed support和mask不能在相位约分后丢失。

因此唯一新增saving条件是(18)的一致正χ，必须作用于确切coefficients、共同row presentation、不同Fourier heights、原physical slots和全自然零，且固定height order先于external N。既有moments没有给这个χ。

未来若真正证明该估计，取固定v、strict decrement、mesh、real losses和height power充分小于χ，可从core与exceptional reserve得到所述正count deficit。这条条件桥梁通过；本报告和被审研究都没有声称条件成立。

## 8. 最终 scope

本轮新draft的两项范围修订及stratum明示明确了原合同范围，没有新增算术假设；冻结论文和既有450/451及149项审计未修改。既有共同centering仍仅是fixed-cell结果，moving-shell准入弱幂界没有被当saving。

四项新增结果通过：有限多t共同ψ/zero；合法mixed plain及affine count；现有coefficient class不封闭的具体原因；实际rows的连续short/plain与long/inverse core。

尚未证明mixed χ、whole physical fourth saving、high/low全域continuation、比例进一步提高或新的零自由边界。封存本审查不认证这些未完成目标。
