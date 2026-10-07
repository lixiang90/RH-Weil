# 临界邻域的多 t 实际 witnesses、合法 mixed plain 与联合核

2026-10-07。新研究，结论限定于准确原 [R] 和已审 extended plain contract。**支付了有限多 t 的共同 presentation/zero 构造、合法 mixed plain 的完整准入及其不改善 count 的结论，以及一个连续临界邻域的短/长 witness 联合核归约。没有支付新的 mixed inverse–plain moment，未取得新边界。** 此处没有再单独扩大 κ contract，也不证明所有 mixed 方法不可能。

仅写本新报告；冻结论文、450/451、既有审计、旧稿和 math 均未修改。不存在从有限模型到实际素数或无限分析的认证声称。

## 1. 固定对象与 source 接口

canonical LF SHA-256 对文本仅作 CRLF→LF、孤立 CR→LF：

| 既有对象 | SHA-256 |
| --- | --- |
| [κ 正式论文](../../papers/kappa-feedback-cubic-boundary-paper.tex) | 16c0ba50a2917f2ead56843eabf55b62fbbe214e162cff373b4d8554f84315ee |
| [450](../../notes/450-plain-kappa-extension-and-actual-capacity.md) | f16807e0f80461e3005b3173e313218b00f5f86abfa860a4ead79e425dd6bee5 |
| [451](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |
| [既有精确脚本](../../scripts/hybrid_kappa_feedback_exact_audit.py) | e03d6536378fff4b51625ab71fa5eace9fcbf4fe1156ccb6ae048f03bf96bc68 |
| [既有精确输出](../../output/hybrid-kappa-feedback-exact-audit.json) | 309f275701a1d96c245eb067d49b00598df4af8e380d220944de250fd2e9d7ba |
| 实际只读 source paper.tex | 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 |

source 是 E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex，commit adc7f1241b42e322a6451854ab7e4b4c146bf78a。以上哈希本轮只读重算，非 JSON metadata 认证。

关键 source 行：

- 705–726：Sψ(n;W)=U^(-n/2)Σψ(l)W(q_l/U^n)，Mψ(r;W)=U^(-r/2)Σμ(l)ψ(l)W(q_l/U^r)，全部 masks 保留；two plain factors 需同一完整 row character。
- 4221–4268：Xu 的有限 presentation νχ•(u)^±，primitive conductor 与 deleted radical 均 ≪A q_u；S-supported sixth-power-free inducing exceptions 有限。
- 4385–4497：pointwise dyads、profile 和 cumulative frequency 条件，fixed internal height orders 先于 external tail order。
- 4510–4685：实际 saturated witnesses 与完整 Gamma/truncated-inverse/profile 构造。
- 9220–9269：marked inverse 的 μ coefficient、一次 product-form prime list、disjoint underlying supports、bounded row-independent coefficients、两个 strict widths。
- 12362–12442：sixth-power amplification，特别已经支付的 scale supremum 和 ua⁶ 的准确 column identity。
- 12492–12578：plain 的 common τ、完整 displayed moving radical、共用 polynomial-size mask、Θ finite-ray coefficient lists、逐槽 mesh 和 n1+n2+6κz≤M。
- 14997–15170：原 physical Qi、幅度 bins、whole-slot selection、whole conjugation、不同 witness/physical heights 的 Sobolev 费用。

## 2. 有限多个 t 可以共享同一 ψ 和零点

**命题 [T/R]。** 固定一个非 floor dynamic bin，固定任意有限个 t_j∈[1,3/2]。可对每个 row 先选同一个 bin 给出的 presentation ψ∈Xu 和 zero ρ=σ+iγ，再分别执行 source detector proof，得到所有 t_j 的 saturated pairs
\[
 (M_{r_j}(W_{M,j}),S_{m_j}(W_{S,j})),
\quad r_j\le t_j+o(1),\quad r_j+m_j\ge t_j-o(1),
\]
\[
 0\le m_j\le1/2+O(\epsilon),\quad
 |M_{r_j}|^2\gg U^{\delta r_j-\epsilon},\quad
 |S_{m_j}|^2\gg U^{\delta m_j-\epsilon}.
 \tag{1}
\]
各 pair 共享 ψ、ρ，但 Fourier extraction 的 ν_j 可以不同；不能要求其 profiles 或 heights 相同。

**证明与准入。** Source 4554 先选择 bin zero，t 只进入 D*=U^t；Y*=U^20、Gamma shift 和新线的 −189/100 上界一致于全部 t。对每个 t_j 都有 tail size 1+o(1)，而后才选 dyad 和 ν_j（4609–4655）。因此不需要在各 t_j 间更换 presentation 或 zero。先固定同一个 zero 的选择再执行有限次 proof，保留每次完整 truncated cutoff。

联合 dyadic subdivisions 数为 O((log U)^(2J))；presentation labels 仍有限。每个 W_M,j 是 W1(y)V≤(D_j y/U^t_j)y^(-σ-i(γ−ν_j))，W_S,j 是 W2(y)y^(-σ-i(γ−ν_j))。Untwisted profiles 的全部所需 annular seminorms 一致有界，cutoff transition 不产生第二 frequency。

先为有限 J、physical Mellin coordinates 和所有 separating variables 分配同一个 cumulative T1/2，令各 |ν_j|≤c_J T1；Fourier L1 mass 和任意外部 tail decay 保证缩小 c_J 后仍可 extraction。没有反复重领 T1/2。Finite-dimensional parameter Sobolev 付 (1+T1)^A_J，A_J 在 external N 前固定；τ 在其后缩小。Primitive conductor、原 row-dependent deleted radical 和自然零没有变化。没有新增随 row 选择的 prime coefficient 或 puncture。

这比只读 proposition 的“每个 t 存在”更强，但它只构造有限 tuple，不给连续 t 的选中 dyads/profile 的单调性、同 height 或相关性。Source proof 的 Fourier maximizer ν_j 可能不同，不能把它们放到对角 ν_1=ν_2。

## 3. 合法 mixed plain 及其准确 count

令两个实际 pairs 使用第2节固定的同一个 ψ，选一次原 physical prime subcollection I，写 Q_I=∏_(i∈I)Qi。把整个 product 按 source 15136–15161 一并 conjugate 到 positive row orientation。两个 S 的 profiles 可以不同、twist heights 也可以不同；source plain 接受它们，参数 Sobolev 支付 joint height cost。

**命题 [T/R]。** 若
\[
 s=m_1+m_2,\quad s+6\kappa z\le1,\quad
 \max_{i\in I}w_i\le\eta_{\rm mesh},
 \tag{2}
\]
所有 Θ coefficients、underlying disjointness、自然 zeros 与 inducing exclusions 保留，且真正取 κ_act=2β*−1，则 extended plain 给
\[
 \sum_{u\in\mathcal B}|S_{m_1}S_{m_2}Q_I|^2
 \ll U^{1+\epsilon}(1+T_1)^A.
\]
同一幅度 bin 的 whole positive slot selection 给 spike
\[
 |S_{m_1}S_{m_2}Q_I|^2
 \gg U^{\delta(m_1+m_2)+2qz-\epsilon-\delta\max_iw_i}.
 \tag{3}
\]
Effective width 真正为1：共同 ν 在 Θ，fixed within row sum，没有新 moving twist。Masks 为原 ones，不以 primitive inducing character 偷换 polynomials。

在 positive-capacity 区，z=(1−s)/(6κ) 先减 ν0，所得理想 count 是
\[
 G(s)=1-\delta s-\frac{q}{3\kappa}(1-s)
     =1-\delta\{cx+(1-cx)s\},\qquad c=(3\kappa)^{-1}.
 \tag{4}
\]
所以
\[
 G(m_1+m_2)
 =\frac{G(2m_1)+G(2m_2)}2,\qquad
 G'(s)=-\delta+q/(3\kappa)<0.
 \tag{5}
\]
因此 mixed plain 不能优于把较大的 actual m 重复两次。临界邻域的 prime supply 对这些全部 requests 充足，(5) 是实际合法 moments 的 count 比较，不是假定 witnesses 的 abstract LP。

即使 available supply Λ 先截断 capacity，
\[
 G_\Lambda(s)=1-\delta s
 -2q\min\{\Lambda,(1-s)_+/(6\kappa)\}
\]
仍在 s∈[0,1] 严格下降；较大 m 的 double-copy request 容量较小，因此若 mixed request 可付，它也可付。Whole-slot rounding 只引入可预先任意缩小的 mesh loss，不产生固定正 power gain。Empty Q 的 count 1−δs 也满足同样比较。多个 S factors 经 Hölder 组合已有第四 moments，所得 bound 至多是已有 counts 的 convex average。

## 4. 不能直接调用的 product 及实际系数原因

### 4.1 同一 physical Qi 不能重复作为两个新 slots

每个 lemma 要求 underlying prime supports 在 masks 之前 disjoint（source 6941–6942、9235、12536）。将两个 witnesses 各自乘同一个 Q_I 后再乘，会得到 Qi²。它包括 diagonal prime-pair p=p 的 ψ(p²)，不是 source 定义的 prime polynomial；若硬折为原 prime p，其相对 ψ(p) 的 coefficient 含 varying row ψ(p)，不在固定 Θ list 中。

增加 numerical length 2w_i 不会修复 support 或 coefficient class。可以把 I 分成 disjoint I1,I2 再用一次 union product，回到第3节。Hölder 对非负 factors 可以处理重叠，却只产生已有 rate 的 weighted average，不给新 correlation saving。

### 4.2 M×M 和 M×S 不封闭于标准 M/S

相同 row character 确实 multiplicative，包括自然零：
\[
 \psi(a)\psi(b)=\psi(ab).
\]
但 inverse product 的 coefficient 是
\[
 \sum_{ab=n}\mu(a)\mu(b)
 W_1(q_a/U^{r_1})W_2(q_b/U^{r_2}),
 \tag{6}
\]
而非 μ(n)W(q_n/U^(r1+r2))。例如 n=p²ab、a,b squarefree 且彼此与 p coprime，取 admissible positive untwisted profiles 支持 a p、b p；支持内 μ(ap)μ(bp) 同号而非零，μ(n)=0。这是 coefficient-class 的直接反例，适用于不等长度，不只是形式上的 μ*μ 符号。它不是 constructed saturated bad row，但足以否定把这个 product 原样当作 source M 的 class identity。

M×S 的 coefficient 是 truncated weighted μ*1。所用临界参数满足 m<r<2m，可取 n=p²a，q_p∼U^m、q_a∼U^(r−m)，其中 a 是另一与 p 互素的 prime ideal。Inverse annulus 内只有 divisor pa，plain quotient 为 p；unit、p、a、p²、n 均在 inverse annulus 之外。因此该 n 的 coefficient 非零，虽然 μ(n)=0。Full unweighted μ*1=unit identity 不能用于 annular truncation。

也不能把 arithmetic divisor weight 仅以 d(n)≪n^ε 就称为 annular plain profile；它依赖 divisors 而非只依赖 norm，原 theorem 没有 arbitrary bounded ideal-column coefficient 的该结论。求和中的 signed cancellation 不能用逐项绝对 majorant 替换后保留原 plain moment。

已有 inverse amplification 实际已控制 scales D'≤D 的 supremum（12394–12408），不因更多 t 带来一个独立 second-moment gain。用另一 factor 的 pointwise bound 再乘这个 supremum，会取消它自己的 saturation spike，回到原 count。

这些都是现有 R 合同不能直接接入新 mixed polynomial 的具体原因；不排除从完整 correlations 重证新的 theorem。

## 5. 连续 critical neighborhood 的实际短/长联合核

下面不假设存在最坏实际 row，结论对所有符合 source witnesses 的 rows 作 partition。定义
\[
 \mathcal N:\quad
 \delta\in[3/8,2/5],\quad x\in[49/100,1/2],\quad
 \kappa\in[37/50,3/4].
 \tag{7}
\]
这是包括已付 critical point 的真实有理邻域。只在合法 κ_act 和 nonfloor bins 上应用；κ 在此处不是可偷用的 reference zero-free input。

记
\[
 t_0=t_\kappa,\quad r_0=r_*(t_0),\quad
 m_0=t_0-r_0,\quad R_0=R_{*,\kappa},
\]
\[
 s_I=\delta(1-x),\quad s_P=\delta(2-2cx),\quad
 s_L=\alpha-\delta.
\]
由实际 counts，
\[
 A_I(r_0)=P_{\rm count}(m_0)=L(t_0)=R_0,
\]
\[
 A_I(r)=R_0-s_I(r-r_0),\quad
 P_{\rm count}(m)=R_0-s_P(m-m_0),\quad
 L(r)=R_0+s_L(r-t_0).
 \tag{8}
\]

### 5.1 显式连续有理 bounds

在 (7) 上可直接用
\[
 c\in[4/9,50/111],\ D\in[455/222,1867/900],
 \ P\in[86/111,1496/1875],
\]
\[
 J_{\min}=(13/30)(455/222)+(3/8)(86/111),\quad
 J_{\max}=(11/24)(1867/900)+(2/5)(1496/1875).
\]
代入 δP/(2J) 的端点给
\[
 111/100<t_0<114/100,\quad
 2/3<r_0<3/4,\quad 3/8<m_0<9/20,
 \quad R_0-(1-\delta)>1/25.
 \tag{9}
\]
例如 r0 下界使用 (172/111)t_min−(5/9)(1/2) 除 D_max，上界使用 (352/225)t_max−(61/111)(49/100) 除 D_min；m0 用 ((1−x)t+(1−c)x)/D 两侧 bounds。这里全部 Fraction 检查严格成立，没有网格外推。

并且
\[
 s_I\ge3/16,\quad s_P\ge43/74,\quad s_L\ge13/30,\qquad
 s_I^{-1}+s_P^{-1}\le910/129.
 \tag{10}
\]

### 5.2 双 t core 命题

固定 0<v≤1/100，令 θ=v/100，t_-=t0−v、t_+=t0+v。先将 witness/moment/rounding losses 取足够小于 θ 和 v，再选 mesh、K、实际 profiles/height order，最后 τ/external tails。由 (9)，两个 t 均严格在 [1,3/2] 内。用第2节取共同 ψ、ρ 的两个 actual pairs。

**命题 [T/R]。** 每个 bin 可分成 exceptional set E 和 core C，使
\[
 \#E\ll U^{R_0-\theta}(1+T_1)^A,
 \tag{11}
\]
而 C 同时带有 t_- 的 short witnesses r_s,m_s 以及 t_+ 的 long inverse length ℓ，满足
\[
 r_0-v-\frac{4\theta}{s_P}-o(v)
 \le r_s\le r_0+\frac{4\theta}{s_I},
\]
\[
 m_0-v-\frac{4\theta}{s_I}-o(v)
 \le m_s\le m_0+\frac{4\theta}{s_P},
 \tag{12}
\]
\[
 t_0-\frac{4\theta}{s_L}\le\ell\le t_0+v+o(v).
 \tag{13}
\]
All factors 保留同一 ψ/ρ、原 zero mask、同一 amplitude bin 和 physical Qi。Constants 与有限 height order 一致于 (7)。

**证明。** 在 t_-，若 r≥1，则 amplified count≤L(t_-) =R0−s_L v<R0−4θ。若 short inverse r≥r0+4θ/sI 或 plain m≥m0+4θ/sP，(8) 给 count≤R0−4θ；按 source positive-capacity moments 支付 strict widths，m≥1/2 用 zero-slot plain。将这些 rows 加入 E。其余 short pairs 的上界就是 (12) 的上两侧，support r_s+m_s≥t0−v−小量给两个下界。

在 t_+，plain improvement 对全部对应 plain branch 检查；同样的 short inverse improvement 只在 r<1 的短支除去 rows，不能把 A_I(r) 套到 r≥1。长 inverse branch 留给下面的 amplified L(r) 判定。若剩下 pair 仍 r<1，则
\[
 r+m\le t_0+4\theta(s_I^{-1}+s_P^{-1})
 <t_0+v/2,
\]
因为 4(910/129)/100<1/2。这与 r+m≥t0+v−小量矛盾，所以余核的 r=ℓ≥1。若 ℓ<t0−4θ/sL，amplified count 更好，把这些 rows 也加入 E；其余由 r≤t_++小量给 (13)。

每个 removal 使用实际 source moments，而非只排除一个数值方案。有限 subdivisions 和所有 real/height losses 可在 4θ 至 θ 的预留份额中支付。Short inverse thresholds >2/3，故第二 marked width 固定正；r 趋近1的固定 zero-capacity neighborhood 用原 amplified/no-slot bound，少选 primes 的差≤2qν0，在同一预留份额支付，不索取 shrinking marked margin。Short plain thresholds <1/2，capacity 正；m≥1/2 用原 zero-slot plain。所需 inverse/plain prime requests <1/5，被冻结几何 e/d>1/5 的严格 supply 支付。每槽 mesh、whole-slot decrement、Θ exceptions 和 bounded S-supported rows 均按原方式处理。高度费用先保留为 (1+T1)^A；应用于 physical proof 时还须用 actual ceiling 选择 τ，不能省略它。

本命题把潜在 critical obstruction 定位为一个实际共同 witness core。没有断言 C 非空、规模恰为 U^R0 或这些 parameter bounds 能由 actual prime sums 同时饱和。

## 6. 当前 critical root 下的明确长度与一个新 mixed 目标

令 e 为 p(e)=657e³−954e²+21e+20 的已付根，κ*=5/6−e/2，δ*=(5−9e)/(6+18e)、x*=1/2。在 reference critical point R0=2/3，
\[
 t_0=\frac{3}{5-6\delta_*}
     =\frac{1+3e}{8e},\qquad
 r_0=\frac{2}{3\delta_*}-1,\qquad m_0=t_0-r_0 .
 \tag{14}
\]
方向数值为
\[
 \delta_*=0.3885833542660\ldots,\quad
 t_0=1.1242271467861\ldots,\quad
 r_0=0.7156336197825\ldots,\quad m_0=0.4085935270036\ldots .
\]
选一次 short-plain capacity
\[
 z_0=\frac{1-2m_0}{6\kappa_*}
     =0.0406297558841\ldots .
\]
同一个 R0=2/3 identity 给
\[
 2\delta_*m_0+\delta_*z_0=1/3.
 \tag{15}
\]
这里 κ* 只用于显示 reference numbers；实际证明中的 moments 始终用 κ_act，general (8) 取代 (15)。

### 6.1 精确需要的新估计

先固定联合 dyadic stratum 的 ℓ、m_s 和一次所选的原 prime-slot subcollection I_P 及 total z，再对其实际 core rows 求和；最后合并前文已付的 polylogarithmic 有限 subdivisions。I_P 满足 2m_s+6κ_act z≤1 的严格小量预算、每槽 mesh 和全 Θ coefficient/height/zero 条件，Q_P 仅使用一次。考虑真实对象
\[
 H_{\rm mix}=
 \sum_{u\in C}
 |M_{\ell}(W_L)|^2\,|S_{m_s}(W_s)|^4\,|Q_P(u)|^2.
 \tag{16}
\]
这是一个 inverse 加两个 plain factors 和一次 prime product 的 absolute square，不是现有 plain/marked theorem 的 integrand。

现有合法计算只有
\[
 H_{\rm mix}
 \le\sup_C|M_\ell|^2
       \sum_C|S_{m_s}|^4|Q_P|^2
 \ll U^{1+\delta\ell+\epsilon}(1+T_1)^A.
 \tag{17}
\]
At the core，spike 是 U^(δℓ+2δm_s+2qz−ε)。临界 (15) 使它为 U^(δt0+1/3−ε)，因此 (17) 给 count 正好 2/3，没有未用余量。General neighborhood 同样由
2δm0+2qzP(m0)=1−R0 给 count R0。

**条件桥梁。** 若能对 (16) 的确切共同 ψ、Γ-derived rowwise profiles、实际 κ、selected physical Qi 和 full natural zeros，证明一致的某 χ>0
\[
 H_{\rm mix}\ll
 U^{1+\delta\ell-\chi+\epsilon}(1+T_1)^A,
 \tag{18}
\]
且同一有限高度阶独立于 external N，那么先 v、ν0、mesh losses≪χ，(11)–(13) 与 spikes 给 critical neighborhood 的 count 至少减少 min{θ,χ/2}。这只是一条准确的新接口；(18) 尚未证明，未因此声明新边界。Reference critical 指数 1+δ*t0≈1.4368559556551；full raw length ℓ+2m_s+z≈1.9820439566773，不可把它隐藏成 width1 的标准 polynomial。

### 6.2 原系数、mask 和 height：下一机制不能略过的内容

展开 (16) 前的 polynomial，
\[
 M_\ell S_{m_s}^2Q_P
 =U^{-(\ell+2m_s+z)/2}
 \sum_{a,b,c,(p_i)}
 \mu(a)\psi(abc\prod p_i)
 W_L(q_a/U^\ell)W_s(q_b/U^{m_s})W_s(q_c/U^{m_s})
 \prod_i a_i(p_i)W_i^{\rm phys}(q_{p_i}/P_i).
 \tag{19}
\]
这是 source 的实际 μ×1×1、固定 Θ prime coefficients 与 dyadic profiles；未凭目标定义一个新读出。Primitive conductor 仍来自同一 ψ≪q_u，全部原 deleted primes/natural zeros保留。重复 factors 不会抹掉任何 mask。

Full unweighted ideal convolution μ*1*1=1，提供一个具体 completion 方向。但实际 W_L 有 truncated inverse cutoff，W_s 处于短 annulus，且 long/short Fourier heights 分别 γ−ν_+、γ−ν_-，一般 ν_+≠ν_-。剥去共同 γ 后，coefficient 仍有 divisor-ratio norm twists；它不是仅依赖 q_n 的 smooth profile。即便把 ν 差暂设为0，补成 full convolution 的其他 dyads 也可能带 signed cancellation，不能从 completed coefficient1 推回某个 saturated block 的 moment。

若展开 |S|⁴ 并冻结 b1,b2,b3,b4，row weight 含 ψ_u(b1b2)\overline{ψ_u(b3b4)}。它不是固定 Θ inverse-column coefficient。将这些 primes 当作辅助 moving residue data，须保留 displayed supports 及 zero masks，generic norm上界达 U^(4m_s)，不能在 cancellation 后把 effective conductor 假称仍为1。若只用 |row weight|≤1 后去掉它，就丢掉需要的 correlation，又回到 (17)。

因此下一具体可研究机制是：对 (19) 的 profile-resolved shifted μ*1*1 completion，或其完整 Möbius–divisor/row correlation，证明 (18) 的严格 covariance saving。必须允许实际不同 ν_j，但把所有新增 Fourier frequencies放在原 cumulative allowance内；保留一次原 Qi、所有 common zeros、displayed moving radicals、rowwise σ/γ 与 fixed polynomial height order。仅把新 composite coefficient 称为 plain polynomial，或把两个 ψ 的 primitive character相同称为同 phase，不能支付该接口。

## 7. 已支付与未支付的结论

本轮支付了四个可审结果：

1. Source 构造允许同一 row 的有限多个 t 共享 ψ 和 zero，全部 profiles、height 和自然零准入已明确；没有要求同 ν。
2. Mixed plain S_(m1)S_(m2)Q 的原 coefficients 与 length/conductor/mesh/height 合法；其理想 count 是两个原 plain counts 的平均，不能更强。
3. Reused Qi、inverse products 和 partial μ convolutions的 class 障碍有具体原系数例子；只限制既有 theorem 的直接调用。
4. 整个有理 neighborhood (7) 上，actual moments 将未获严格 saving 的 rows 归约成 (12)–(13) 的共同 short/plain 与 long/inverse core，且定位了 (16)–(19) 的准确新 mixed 接口。

未支付 (18)、actual covariance deficit、连续 t dyad/maximizer 的新相容性、完整 high/low 改参及全域 continuation。亦未证明方法不可能、RH、RR、新零自由边界或更高简单临界线比例。冻结稿和其两审保持原哈希；任何新边界仍需完整全域证明与独立两审。
