# 固定可数 Mellin 数据的三角插值与真实 Pan 像

2026-10-29。独占原推导；任务为已冻结 `formal-mellin-admission/next-full-image-moment-admission.md` 的一次必要检验，不续 C060，不改采样点、frame、F、C，不登记 C061/598、计轮或 Goal 完成。下述自含构造闭合；项目最强旧的去重与最终消费另由 root 核对。未检索或主张世界首创，未导入抽象矩问题定理。

输入原件：

| 原件 | bytes | SHA256 |
| --- | ---: | --- |
| `reviews/2026-10-29/formal-mellin-admission/next-full-image-moment-admission.md` | 2559 | `51c90b825f563424db54e8ab8d946fc5baa0855c1aa65cfcb069c8199a3357f0` |
| `notes/405-f1-adelic-restriction-moments-and-radical.md` | 14633 | `fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d` |
| `notes/597-formal-mellin-source-boundary-rank-obstruction.md` | 7886 | `51f2e19bb06515d248a310430f0b612ba844c4f7bf9fddf784c0d0dab6251c75` |

## 1. 对象、角色与结论

固定实 Fréchet 空间

    S_exp={r∈C∞(R,R): p_(N,k)(r)=sup_u e^(N|u|)|r^(k)(u)|<∞,
                              对所有整数 N,k≥0}。

本稿中的 r 始终是 physical 源。令 U f(u)=e^(u/2)f(u)，raw 源是 U^(-1)r。取

    α_n=n+3/2，
    ℓ_n(r)=∫_R r(u)e^(α_n u)du=M_r(n+2)，
    B(r)=(ℓ_n(r))_(n≥0)。

这里 B 是本门固定的完整可数数据，不是 405 中同名字的 Weil 双线性配对。目标赋集合/逐坐标 product 结构，不附加增长约束。

405 的 raw J=E(S_even,0) 是实际 adele 限制像，I=closure_(S_exp)J，P_an=I∩ker c∩ker d。写 physical 关系空间为 P_phys=U(P_an)。下文证明更强的实际像版本：

    B(S_exp)=R^(N_0)，
    B(U(J∩ker c∩ker d))=R^(N_0)。                         (A)

因此 B(P_phys)=B(S_exp)=R^(N_0)。不仅 finite jets；每个任意实序列的所有坐标由同一个 S_exp 源实现，而且可由一个实际 J 中的双矩零关系实现，不以闭包极限冒充实际像。

集合满射不付 du/Dlog/Hilbert 范数的统一代价、不付目标正性、不证明 full Weil 容量。本稿最后将同数据精确和 pointwise 渐近处理的最强直接后果一并列明，不能另轮重计。

## 2. 每个固定 moment 的合法域与连续性

对固定 α>0，取整数 N>α。任意 f∈S_exp 满足

    ∫|f(u)|e^(αu)du
      ≤p_(N,0)(f)[1/(N−α)+1/(N+α)]。                     (1)

按正负半轴分开积分即得。因此 ℓ_n 对 S_exp 连续，所需 N 随 n 增长。这不是一个固定 p_(N,0) 对全部 n 的统一估计，也没有对 du 单位球作声明。

固定一个非零、非负实 ψ∈C_c∞((0,1))。例如在 (1/4,3/4) 内取 exp(−1/[(u−1/4)(3/4−u)])、外取零。对 n≥0，令

    L_n=∏_(0≤k<n)(D+α_k)ψ，D=d/du；L_0=ψ。

L_n 是实紧支光滑函数，其支集包含于 [0,1]。紧支分部积分没有端点项，对每 j≥0 有

    ℓ_j(L_n)=∏_(k<n)(α_k−α_j)ℓ_j(ψ)。                    (2)

若 j<n，乘积含 k=j，值恰为零。若 j=n，则

    A_n:=ℓ_n(L_n)=(−1)^n n!ℓ_n(ψ)≠0，                   (3)

因为 α_k−α_n=k−n，且 ψ 非负非零。符号为 (−1)^n；不能误用 D−α_k。

平移约定 τ_a f(u)=f(u−a) 给 ℓ_j(τ_a f)=e^(α_j a)ℓ_j(f)。这一符号与分母 e^(α_n a) 一致。

## 3. 任意完整序列的同空间插值

给任意 b=(b_n)_(n≥0)∈R^(N_0)，不要求任何增长界。递归定义实紧支 g_n。

已有 g_0,…,g_(n−1) 时，令

    δ_n=b_n−Σ_(i<n)ℓ_n(g_i)，
    g_n=δ_n e^(−α_n a_n) A_n^(-1) τ_(a_n)L_n。            (4)

δ_n 是有限实数，A_n 非零，因此此式合法。即使 b_n 增长任意快，下一步仍可再选择有限但足够大的 a_n；不要求事先的 uniform bound。

选择 a_n>0 且 a_n≥a_(n−1)+2（n=0 时以前值略去）、a_n≥n+1。于是 support(g_n)⊂[a_n,a_n+1]，这些支集局部有限且互不相交。对 0≤N,k≤n，直接估计得

    p_(N,k)(g_n)
      ≤|δ_n/A_n| e^N ||L_n^(k)||∞ e^(−(α_n−N)a_n)
      ≤C_n e^(−3a_n/2)，                                 (5)

其中 C_n=|δ_n/A_n|max_(0≤N,k≤n)e^N||L_n^(k)||∞<∞。这是对每个实际 n 的有限最大值，不声称 C_n 一致有界。

进一步选择

    a_n≥(2/3)log(max{1,2^n C_n})                          (6)

即可保证 max_(N,k≤n)p_(N,k)(g_n)≤2^(−n)。若 δ_n=0 则 g_n=0，任取满足前述支集条件的 a_n 即可；式(6)也仍合法。

现在令 G=Σ_(n≥0)g_n。由支集局部有限，G 为实际光滑函数，不是形式级数。对任意先固定 N,k，除有限前项外 n≥max(N,k)，故

    Σ_n p_(N,k)(g_n)<∞。

因此 G∈S_exp，且 Σg_n 在每个 p_(N,k) 中收敛到 G：

    p_(N,k)(Σ_(n≥m)g_n)≤Σ_(n≥m)p_(N,k)(g_n)→0。

这给同一明确 Fréchet 空间中的收敛；无需将逐坐标收敛误称函数空间收敛，也无需另加完成化。构造甚至可令 G 的支集位于一个正半轴中；G 仍一般有符号，未声称非负。

对每个先固定 j，取 N>α_j。由(1)及上面的半范数绝对求和，

    Σ_n∫|g_n(u)|e^(α_j u)du<∞。

因此 moment 与级数可作绝对换序。由(2)，n>j 的每一项在 ℓ_j 下严格为零；由(4)，第 j 项把此前有限和精确补成 b_j。于是

    ℓ_j(G)=Σ_(n≤j)ℓ_j(g_n)=b_j，∀j≥0。                  (7)

(7) 完成 B(S_exp)=R^(N_0)。并非先对不同长度取不同插值源，亦非只付各有限截断的稠密性。

## 4. Physical 卷积与实际 adele 限制像

必须保 raw/physical 的角色。乘 U、U^(-1) 都是 S_exp 的连续线性自同构：Leibniz 展开给

    p_(N,k)(e^(±u/2)f)
      ≤Σ_(l≤k) binom(k,l)(1/2)^(k−l)p_(N+1,l)(f)。

普通加法卷积在 S_exp 中合法，且有 405 同一估计

    p_(N,k)(f*g)≤2p_(N,k)(f)p_(N+1,0)(g)。               (8)

利用 |u|≤|v|+|u−v|，把一项多出的 e^(−|u−v|) 积掉即得。导数下移同样有绝对支配。半密度满足真正的代数等式

    U(f*g)=(Uf)*(Ug)。                                   (9)

取 405/597 固定的 raw 实际像元素

    p=(D²+D)h=Eη_0∈J，c(p)=d(p)=0，
    η_0(x)=(4z^4−28z^3+41z²−9z)e^(−z)，z=πx²，
    P=Up。

对任意 physical G∈S_exp，令 g=U^(-1)G∈S_exp。为避免只借 ideal 的名称，实际构造

    η_g(x)=∫_R g(t)η_0(e^(−t)x)dt。                      (10)

记 q_(a,b)(η)=sup_x|x^a η^(b)(x)|，a,b 为非负整数。可微及 Schwartz 估计为

    q_(a,b)(η_g)
      ≤q_(a,b)(η_0)∫|g(t)|e^((a−b)t)dt<∞。              (11)

所有所需指数权绝对可积，因为 g∈S_exp。η_g 实偶，η_g(0)=0。又

    ∫|g(t)|∫|η_0(e^(−t)x)|dx dt
      =||η_0||_1∫|g(t)|e^t dt<∞，

故一次合法换序给 ∫η_g=(∫g(t)e^t dt)(∫η_0)=0。于是 η_g∈S_even,0，是实际可用的 Schwartz adele 因子。

还须核 E 的求和换序。由 |η_0(x)|≤C(1+x)^(-2)（x≥0），

    Σ_(m≥1)|η_0(mλ)|≤C/λ，λ>0。

因此对每先固定 u，

    ∫|g(t)|Σ_(m≥1)|η_0(m e^(u−t))|dt
      ≤C e^(−u)∫|g(t)|e^t dt<∞。

故用 405 的 Eη(u)=2Σ_(m≥1)η(me^u) 可得实际等式

    g*p=Eη_g∈J。                                        (12)

这是实际像，不需要先在 J 中作逼近再落入 I。由 raw Mellin 卷积的绝对 Fubini，c(g*p)=c(g)c(p)=0，d(g*p)=d(g)d(p)=0。结合(9)，

    P*G=U(p*g)∈U(J∩ker c∩ker d)⊂P_phys。                (13)

两个 physical 次数是 ∫(P*G)e^(−u/2)du、∫(P*G)e^(u/2)du，分别为上述 raw c、d；不把它们说成 ordinary mean 的两个条件。

## 5. 每个可数数据已由真实 Pan 实现

固定 s>1，physical Mellin 卷积也满足

    M_(P*G)(s)=M_P(s)M_G(s)。                             (14)

原因是两个指数加权绝对 L¹ 范数有限；用 exponent s−1/2 作一次 Fubini 即得。(9)同时验证了它与 raw M_(p*g)(s) 的一致性，没有错位成 s±1/2。

405/597 已付的固定公式为

    M_P(s)=s²(s−1)²π^(−s/2)Γ(s/2)ζ(s)/4。

所以 μ_n:=M_P(n+2)>0，对所有 n≥0。这里只有 s≥2 的实 Dirichlet 级数正性、Gamma 正性与固定源公式；不用 RH、π 超越性或任何未知 ζ 零点位置。

给任意 b∈R^(N_0)，把(7)应用于序列 (b_n/μ_n) 得到一个 G∈S_exp。令 Q_b=P*G。由(13)，Q_b 是 physical 真 Pan 关系，raw 代表实际上在 J∩ker c∩ker d；由(14)，

    B(Q_b)=b。

这证明(A)。即使 μ_n 或 b_n 的增长很大，构造只逐 n 需要有限 δ_n 与更远平移；没有免费 uniform norm 逆。

直接 complexification 同轮可得：S_exp,C=S_exp+iS_exp、P_phys,C=P_phys+iP_phys，分别对 b 的实部、虚部作上述构造，因此

    B(S_exp,C)=B(P_phys,C)=C^(N_0)。                       (15)

这仅是同源公式的复线性延拓。597 原 actual Φ 是实加法商；(15)不自动给它复标量结构或 complex arithmetic carrier。实源结论本身已足否定全实源关系下降后仍保非根的同数据尝试。

## 6. 最强直接后果：同数据处理不能恢复 primitive

满射比 597 的单条关系非零强：对每个先固定 r∈S_exp，存在一个先固定 Q_r∈U(J∩ker c∩ker d)，使

    B(Q_r)=B(r) 全部坐标精确相同。                        (16)

因此对任意集合 Y、任意 map F:R^(N_0)→Y，若存在 y_0 且

    F(B(Q))=y_0 对所有 Q∈P_phys，

则 F(B(r))=y_0 对所有 r∈S_exp。无需 F 线性、连续、局部、有界或与源无关的有限秩。若 F 的所有自适应参数也只由完整 B(r) 决定，它们已包含于 F；这类仍全部退化。

把 597 的 formal-tail→actual Φ 固定映射记作 ι，J_formal=ι∘B。于是同样有

    J_formal(P_phys)=J_formal(S_exp)。                    (17)

任意实际 Φ 的进一步 quotient 或 set postmap，只要把全部这类 Pan 像送到同一零对象，就同时把全部源像送去，包括 537 的明确非根 compact 源。不是要求 ker J=Pan；这里只使用必须杀 Pan 且要保至少一个非根的必要条件。

此处还包含下列同数据渐近直接后果，不能把它保留作另一轮新定理：任给索引集、任意族 F_κ:R^(N_0)→Y_κ，(16)使

    F_κ(B(r))=F_κ(B(Q_r))，对所有 κ 同时成立。             (18)

Q_r 是与 κ 无关的一个固定真实关系。因此若在同一明定的目标识别/收敛规则下，对每个固定 Pan Q 的输出趋于规定零对象，那么对每个固定源 r 的输出也如此。目标不必 Hausdorff，F_κ 不必连续；结论只传递每一 κ 的相等。597 的 truncation 逃逸仍然存在，(18)准确说明它不能在仅用这份固定 B 数据、且对全部固定 Pan 有同一消失责任时保住 fixed 非根。

这不将 pointwise 限制升级为任何 uniform rate/有界源球估计。额外源数据、依赖 full r 但不经过 B 的自适应规则、只要求另一个较小/成长的关系类消失、不同源域、不同采样数据、源与 κ joint 成长或没有逐固定 Pan 消失责任的 D′ 比较，均未被这个集合论论证排除。特别是不把它泛化为全部正分布逼近失败。

## 7. 费用、覆盖与宏观范围

已付域是所有 real S_exp、以及同公式的 direct complexification；增长量词是每个任意无增长约束的可数序列存在一个实际源。误差是全部 moments 精确匹配，非 o(1)；物理/实际像、双 degree 和绝对换序已分别支付。

未付的是任意选取的序列空间范数到原 du/zero-extension Dlog/Hilbert 范数的统一控制、对 r 的连续线性选择、成长窗/Ξ 的集体覆盖、primitive/principal/截面/mixed RR 的新正输入，以及 full Weil signed core/coupling。构造依赖整个序列的逐步残差与越来越远的平移，不可由集合满射宣称免费 norm transport。

本稿无新论文/源码下载、无新数值，证明为自含三角构造与 405 已有实际 ideal 的重新逐项检查。数学净值须与最强旧（尤其 519/520 的全零点 jets、373 的 profile、584 的不同数据像）对齐后由 root 判定；若已有同强结论，不按本文件/证明长度加轮。

597 的 actual Φ 有理秩反测保持正确，但本稿不再靠有理秩或有限修补参数加强其数值。新责任是固定完整可数 B 的 Pan 像已覆盖全部源像，因而同数据精确/pointwise后处理不能保 primitive。它仍不是经典 RH 的严格方法类总体边界；旧 whole542+555→557 leading4/5 负惯性 UPPER、关键 primitive/mixed/corecross/growing Ξ 均未因此改善。长期 Goal 保持 active，结算/单 cadence/宏观复盘由 root 统一处理。
