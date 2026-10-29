# Formal Mellin 准入：实际 Pan 源、超越系数与最强旧扣除

2026-10-29；G20261027/runtime1793085111、冻结0c4f。本分工只执行STATE/AB的固定必要首检，独占本稿；不改STATE、cadence、Goal、Git或库，不开C060/597、来源、参数或数值。Root现场运行Goal观察为依据。本稿不预定统一计轮，由root比较实际新净值后结算。

**结论。** 405给出的一个固定、真实、非compact、双次数零关系，经正确半密度变换成为合法physical源R。在本候选的偶数formal系数中，出现无穷多个非零有理数乘π的不同正整数幂，因此这些系数的Q-rank无穷。实际01/02边界在固定∞ frame上的系数只能张成有限维Q空间；由此得到这份raw source pair的真实类J(λR)≠0（每个real λ≠0）。必要的Pan下降失败。这个判断不依赖Φ=G2、period lattice、A01∩A02的全局识别或未审§3/4。

这只停止指定formal Mellin编码的principal准入，不排全部二维adelic、relative/higher、其它源或有费完成化，也不证明完整Weil型正负或RH。有限Mellin评值不杀Pan是强旧；实际新商中还须闭合下述boundary系数lemma，不能仅凭旧评值非零跳到J(Pan)非零。

## 1. 实际恢复、读取和范围

实际读goals/README、STATE，执行research_state.py check后show，再读同一Goal、已完成C059、D20261029AB、当前macro frontier及2723-byte next-formal-mellin-source-admission。实际工作树只观察root推进STATE，不复用C059预算，不以子代理状态替代Root active Goal。

实际读405§1–5及源/配对范围、519全文、520§1–3、582§1–2及§5–7必要源域、537的源域和已核固定窗结论入口；另读已冻结source-gate-location-and-domain-audit.md恢复实际(6)–(8)的group/标量类型。未重新核全部旧证明，未打开新PDF页、外部paper、web或Osipov§3/4/Example2.3。一次520误记路径读取失败后按真实519链接读取520-f1-source-quotient-spectrum-and-centered-growth.md，未把失败路径冒充已读。

下文用Euler的ζ(2m)恒等式、π超越性、Stirling公式作为标准独立数学事实；没有新文献检索或重证这些经典定理，不使用未知ζ零点位置。主要source/domain原始定义由已消费的12603-byte审稿绑定，本稿在该实际类型中作自含系数计算。

## 2. Raw源、physical源与导数号不能混用

用u表示log尺度，D=d/du。405的raw实Fréchet空间为

    S_exp={f smooth real : sup_u e^(N|u|)|f^(k)(u)|<∞，∀N,k}.

对raw f，M_f(s)=∫f(u)e^(su)du。Physical源r=e^(u/2)f，因此本门约定

    𝓜_r(s)=∫r(u)e^((s−1/2)u)du=M_f(s).                 (1)

所有这些积分在每个fixed复s绝对收敛，带权分部积分无边界项。Raw M_(Df)(s)=−sM_f(s)，所以本处生成双矩零关系的raw算子是D²+D，不是D²−D。乘以e^(u/2)保持S_exp这个函数集合，并只将所需指数半范数阶数作固定平移；没有把这种强拓扑等同du/Dlog单位球。

405的具体偶Schwartz源和其实际像是

    η(x)=πx²(πx²−3/2)e^(−πx²)，
    h(u)=Eη(u)=2Σ_(n≥1)η(ne^u)>0.

η(0)=0、∫η=0、Fourier自对偶；Poisson给两端所有指数权的快速衰减。405已经支付真实源映射、交换关系及精确常数

    M_h(s)=ξ_R(s)/2
          =s(s−1)π^(−s/2)Γ(s/2)ζ(s)/4.                  (2)

这里ξ_R是通常整完成函数，不是critical-line变量t中的Ξ命名。令

    p=(D²+D)h，  H=e^(u/2)h，  R=e^(u/2)p
      =(D²−1/4)H.                                    (3)

405直接给p=Eη₀，η₀(x)=(4z⁴−28z³+41z²−9z)e^(−z)、z=πx²，是真实准入Schwartz源，非按零点或配对事后定义。故

    p∈P_an=I∩ker d∩ker c，
    M_p(s)=s(s−1)M_h(s)， M_p(0)=M_p(1)=0，
    M_p(2)=π/6≠0.                                    (4)

R是本门需要的physical Pan 源。其两个指数矩∫R e^(±u/2)du恰为M_p(1)、M_p(0)，均为零；不能把raw双次数矩和Schwartz源η₀的准入零值/积分混同。R非零且非compact：若R最终为零，则正函数H在某个尾上解H''−H/4=0；S_exp排除该尾的两个指数解，迫H在尾上为零，与H>0矛盾。此例不冒充C_c∞ TestFunction，但首检明确要求全405 noncompact关系，因此适用。

Real λR仍是同一physical关系族；平移也保持：e^(−u/2)τ_bR=e^(−b/2)τ_bp，405的Pan理想保持平移与实缩放。形式源映射所需全Pan消去至少必须消去这一份固定R及其实数缩放。

## 3. 本候选的全部系数与固定实数缩放

固定公式a_r(t)=Σ_(j≥0)𝓜_r(j+2)t^jdt。由(1)–(4)，对R的每项系数为

    c_j:=𝓜_R(j+2)=M_p(j+2)
       =[(j+2)²(j+1)²/4] π^(−(j+2)/2)
          Γ((j+2)/2)ζ(j+2)>0.                          (5)

所有项都来自Re s>1的普通值，未借非平凡零点、重数假设或形式解析延拓。首项c₀=π/6。对任意fixed real λ≠0，候选的系数为λc_j；这是raw源族的缩放，不假定Φ本身具有R-向量空间标量作用。

若r_b=τ_bR，则

    𝓜_(r_b)(s)=e^((s−1/2)b)𝓜_R(s)，
    c_j(b)=e^((j+3/2)b)c_j.                            (6)

下面决定性反测只用b=0和λ≠0，不用改变source/point参数。不能从它无条件宣称所有b都满足同一超越系数证明：偶系数的底数会成为πe^(2b)，某些b使它为代数数。一个合法Pan关系已足以否定全Pan消去，无须此额外全称。

## 4. 偶指标给无穷Q-rank

取j=2m−2（m≥1）。Euler精确恒等式

    ζ(2m)=|B_(2m)|(2π)^(2m)/(2(2m)!)

和Γ(m)=(m−1)!给

    c_(2m−2)=q_m π^m，
    q_m=|B_(2m)| 2^(2m−3)(2m)²(2m−1)²(m−1)!/(2m)!
       ∈Q_(>0).                                      (7)

前几个值为π/6、(2/5)π²、(10/21)π³；首项与405的独立常数一致，系数没有丢失1/2或半密度平移。π超越性意味着，对每个N，前N个偶指标系数c₀,c₂,…,c_(2N−2)在Q上线性独立：任何非零有理线性关系会成为π的非零有理多项式等式。因此

    dim_Q span_Q{c_j:j≥0}=∞.                           (8)

乘以同一个非零实数λ不改变这些Q线性关系，所以λR的系数也有无穷Q-rank。这里不引入m(p)成长率或数值验证；(8)是同一固定真实源的完整formal尾的精确属性。

## 5. 真正boundary的系数约束：不靠有限jet下商

本段是将(8)接到实际Φ所需的domain lemma的独立代数核验，不消费另一未读稿作为已证前件。使用已消费source-domain稿所绑定的Osipov定义(6)–(8)。在固定rational branch C=∞，K_C=Q((t))，F的dt frame定义于Q。实际01 subgroup在此branch的arch坐标属于Q((t))dt，故其全部Laurent系数都在Q。

实际02 subgroup的arch腿是**未完成的**F_η⊗_Q R。每个元素按代数tensor的定义为有限和

    Σ_(k=1)^n α_k ω_k，α_k∈R，ω_k∈F_η=Q(z)dz.

每个ω_k在∞的dt坐标有Q系数的Laurent展开（负幂有限）。故任何01+02 boundary在该branch上的全部系数都落入

    span_Q{1,α₁,…,α_n},                               (9)

一个依boundary而定、但确实有限维的Q空间。Finite legs的相等条件只进一步限制boundaries，不会使(9)失效。无需先识别A01∩A02，无需Φ=G2或period lattice；把02 ordinary tensor误作completed tensor将破坏此论证，必须保原定义。

另一方面，各fixed r∈real S_exp的𝓜_r(j+2)有限，正幂formal尾a_r属于R[[t]]dt。Source定义把V∞写成沿horizontal branches、相对于completed integral lattice的restricted product；只在∞放这份integral formal尾、其余branch为0，给合法v_r∈V∞。dt与dz的过渡为dz=−t^(−2)dt，保持同一relative canonical F及bounded negative Laurent tail；不要求a_r解析收敛。

若J(λR)=[(0,v_(λR))]=0 in actual Φ，就有(0,v_(λR))为某个01+02 boundary。取∞坐标，(9)强迫其系数Q-rank有限，与(8)及λ≠0矛盾。故

    J(λR)≠0 in Φ，∀real λ≠0.                         (10)

这是作用于实际全Φ的必要障碍，不是仅在G2看见一个系数非零后跳到全商。它只否定这份明确raw encoding对405关系的消去。是否把此结果计为新研究轮仍由root按最强旧与实际完整研究门统一判断。

最强直接消费应一并保留。令L_fin⊂R((t))为全部系数的Q-span有限维的Laurent series；它对加法及每个固定real scalar封闭。由(9)，取实际无穷组件的固定C∞坐标再模L_fin，给合法的**加法代数读出**

    ρ: Φ -> R((t))dt / L_fin dt，
    [(a_finite,v∞)] |-> [v∞|_(C∞)].                    (10a)

因此任意实际有限位adelic腿、任意其它horizontal arch branches的改动，都不会改变这个读出。即使在C∞上另加逐源选择的finite-Q-rank纠正，其rank无需uniform、规则可以nonlinear或source-adaptive，ρ也保持不变；不声称该纠正本身一定是Φ-boundary或Φ中的类保持不变。对每个λ≠0，λR的无穷Q-rank不能被这种纠正抵消，故这一整个同链修补范围仍有非零像；不应在未来把其中更弱的“加一项generic/有限rank修补仍失败”重计成果。

ρ只作algebraic尾部读出，不声称continuous、Hausdorff、正Hilbert或有原du/Dlog费。L_fin含任意有限Laurent polynomial，故在通常逐系数/有界负幂的formal拓扑下稠密，不能凭这个代数商论证closure或completion后的分离性。具有infinite-Q-rank的真正不同∞纠正、改变actual target/完成化或其它relative/higher源仍是未排的不同机制；它们不自动继承本门预算。

## 6. 两个不能混用的较弱论证

**有限评值的强旧。** 仅从c₀(R)=π/6≠0，已知bare coefficient functional不杀Pan。更一般，任意先fixed有限线性组合L(r)=Σ_(j=0)^N a_j𝓜_r(j+2)若杀全部Pan平移τ_bR，则由(6)和不同实指数的线性独立，所有a_j=0。这是405真实关系与519/520的off-zero Mellin机制的直接旧消费。

但有限∞jet本身并不是Φ上已定义的读出。任何有限指定Laurent/Taylor jet可由一个generic real rational differentialΣβ_jt^jdt在∞匹配；它属于02的generic real腿，其它horizontal branches同时有自然展开。因此忽略其它legs的bare finite coefficient/modZ规则不能自动下Φ。这里也**不**声称“仅∞ branch非零的truncated source本身就是02 boundary”；generic differential在其它branches上的数据不能丢。

**零解析半径不是formal非法。** 由(5)及Stirling，log c_j=((j+2)/2)log((j+2)/(2πe))+O(logj)，所以c_j^(1/j)→∞，a_R作为普通幂级数的解析半径为0。这不妨碍R[[t]] formal合法性；01本身也可有解析半径0的Q系数formal尾。故“非解析⇒不在V∞/非boundary”是错误捷径。决定性区别是(8)与(9)的Q-rank，而不是收敛半径。

## 7. 源费、最强旧净值与停止范围

每个fixed系数有真实强源界。令α=j+3/2，取整数N>α，则

    |𝓜_r(j+2)|≤p_(N,0)(r)
       [1/(N−α)+1/(N+α)].                              (11)

这支付单个moment的绝对收敛/强域连续性，N随j增长；不是原du/Dlog的全formal尾统一费。平移时du/Dlog保持而(6)增长，不能偷渡原norm有界运输。此次Pan必要门已经失败，故不以此费用另开参数或norm优化。

519识别真实像I为完整ζ零点jets空间，P_an=I∩ker c∩ker d；520给所有非零点处的实际预解。它们早已支付实s≥2的Mellin求值不杀Pan，以及(6)的有限评值非蕴含。没有必要重新证明这些旧谱设施。新目标Φ则是加法adelic商，不是原Fréchet源商或另一个已知Hilbert商；不能仅凭旧求值非零就宣称J(Pan)非零。将两者接通所需的短依赖链是：

    405真实p与精确Mellin常数
      -> (7)/(8) Euler-even-zeta + π transcendence
      -> (9) actual01/02普通tensor系数lemma
      -> (10) actualΦ中的必要下降失败.

无新独立positive输入、主关系桥、mixed容量或whole预算获得付款；本结果是指定source pair的反测。Real subset失败已足阻止allcomplex延伸；不需再用537非根测试挽救已失败的全Pan门。537 fixed窗正性和582合法full-source Green资产保持，不升级为成长正性。Raw target Φ的topology/complexification、allcomplex/du费用和全source coverage仍未付，也不由本稿否定。

全部Γ/contact、properpowers及双pole的经典目标保持原范围；此源反测没有删改或重算它们。Whole542+555→557 leading4/5仍仅负惯性UPPER；算术primitive/principal/整sections/mixed、危险core/cross和成长Ξ未解决。Stop仅此固定Mellin点/frame/F/C的编码；不同finite legs、真正不同source/relative/higher或有费完成化需另有实物，不由本稿授予后继。

## 8. 实际输入版本与终态

以下均现场核原始UTF-8/LF字节，身份绑定不代数学认证；STATE是root可变记录，不冻结为输入。外部PDF只通过已核source-domain定义消费，本分工未重新读PDF或proof。

| 输入 | bytes | SHA256 |
|---|---:|---|
| goals/GOAL.20261027.md | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| goals/contracts/C059-critical-prime-sonin-covariance.md | 2011 | `376a3bc8f3504e2d071d8c30ad81579c78c7488cb2d2b93c80d7dee008972be8` |
| goals/review-cadence.json | 6749 | `a5cfcd0ca0f2a4ad63f6c7b60d55c83024ebb86387f0a12a0b7b167e6f3cf600` |
| reviews/2026-10-29/post-increment-core-choice/next-formal-mellin-source-admission.md | 2723 | `4bd4483a700f1ab67c784d92f0723fd8cd1f76028be5674b78aa63163094b21f` |
| reviews/2026-10-29/post-increment-core-choice/source-gate-location-and-domain-audit.md | 12603 | `82d2231ceb82b2a90cf07bf25bba068f1bb1efcea79ad3c2ec59e7d7ed76027b` |
| notes/405-f1-adelic-restriction-moments-and-radical.md | 14633 | `fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d` |
| notes/519-f1-closed-source-image-and-degree-moments.md | 5766 | `93d39e6d932c9913f5feb77bed4d1ad096c9d984ed571e894576fce6c53b124c` |
| notes/520-f1-source-quotient-spectrum-and-centered-growth.md | 6311 | `81a05708dfd2139d374d9fac7f631e66ea4449d502cf9fb0c52f53b900dc9651` |
| notes/537-source-exact-weil-window-positive-tail-admission.md | 8155 | `269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8` |
| notes/582-full-local-weil-strong-domain-and-actual-green-source-gates.md | 14027 | `6d5e5711e44fad0aec44e6d95233b7898370430bc9b7b1cc8281b7d4304fdcc8` |

本分工终态：只写本稿，无STATE/cadence/Goal/Git/库修改，无query、下载、数值、后台或自动后继。两腿会合及计轮由root按实际冻结稿消费，不能用本消息或终态标签代稿。
