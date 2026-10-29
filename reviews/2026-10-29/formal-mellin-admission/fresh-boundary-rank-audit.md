# Formal Mellin：独立 fresh 的实际边界、Pan 尾部与净值审查

2026-10-29；G20261027/runtime1793085111、原冻结0c4f。本稿只审AB/STATE已经冻结的同一formal Mellin源公式，独占本文件；不改STATE/cadence/Goal/Git/库，不建C060/597，不调Mellin点/frame/degree，不读新来源或Osipov§3/4。Root实际运行Goal观测为依据，本分工不以子代理作用域改变长期Goal。

**结论：限定 PASS。** 两份冻结原稿在原physical/raw约定、actual 01/02 subgroup、普通与完成tensor、formal成员性和完整商Φ上对齐，没有剩余实质未付前件阻止这份候选的必要下降反测。405的一条固定真实关系P，经此合法源编码，在实际Φ中有非零像；任意非零real倍也非零。有限jet不能直接下商，但从原始boundary定义可建立合法的代数尾部读出，不需要Φ=G2、period lattice、A01∩A02的全局识别或主定理proof。

若root实际全文消费并采用此新target结果，建议**统一一个数学迭代**，不是source0；理由和最强旧扣除见§7。源/定义恢复、两原稿、fresh、有限jet排错及同链repair推论不另计。它不通过长期Goal任一完成门，也不提供whole预算或关键正性输入。

## 1. 恢复、独立推导和实际读稿

实际读AGENTS、goals/README和STATE，运行research_state.py check后show，读同一Goal完整完成门、已完成C059、D20261029AB、macro frontier、当前choice总结和2723-byte必要首检。核实际工作树。读取时唯一cadence为6749bytes/SHA a5cfcd0ca0f2a4ad63f6c7b60d55c83024ebb86387f0a12a0b7b167e6f3cf600，2/history60/latest596/formal19；本分工未写它，也不替root提前消费计数。

先独立重构：单分支formal completed-tensor成员性；finite jet的generic-boundary负对照；01有理系数、02普通tensor的有限Q-span；由此得到全Φ上的尾部读出；405 raw导数号/physical半密度、Euler even-values及π超越性的系数反测。Root和作者消息是待核线索，不作证明前件。

收到各自冻结通知后，实际全文读取当前两稿，并现场、末次重算raw bytes/SHA：

* domain-period-and-readout.md：13380bytes，SHA256 96d0346ca071eaf9ae895e6655254d4010cc92b2e6934db80fb799f6c215b5a9。
* pan-moments-and-old-consequence.md：14816bytes，SHA256 a259650e7427965b34cb25e53be81112b97908c8a1467bbeb9b12ced5ead7e18。

两份均UTF-8/LF。没有把消息、文件存在或终态标签代替原稿。另实际读405§2–5、519/520必要源商与Mellin/谱段、584全文及其最强旧compact-real Laplace与same-B范围，读既付source-domain12603稿的原(6)–(8)定义和Φ/G2区别。本分工没有重新打开PDF数学页、proof或新paper；PDF字节只作身份绑定。

## 2. 原对象、frame 与成员性

固定X=P¹_Z、C=∞、U=A¹_Z、F=ω_(X/Z)≃O(−2)，t=1/z、e∞=dt。该rational branch的系数域为Q，故K_C(F)=Q((t))dt、Fhat_C=Q[[t]]dt；dz=−t^(−2)dt。没有按源选择real formal frame。

V∞=A_(X_Q)(F_Q) completed-tensor_Q R是原无穷ambient，actual arithmetic adeles为A_X(F)⊕V∞。其中C∞ local factor为R((t))dt，integral lattice为R[[t]]dt。对real physical r∈S_exp，

    M_r(s)=∫r(u)e^((s−1/2)u)du，
    a_r(t)=Σ_(j≥0)M_r(j+2)t^jdt。

每个moment绝对收敛，所需指数半范数可依j；没有一个原du/Dlog统一尾费被暗中假设。无限正幂是formal合法数据，不要求解析收敛。有限多项式截断以单分支adele及finite real linear combination表示，在每个固定有限jet上最终稳定；formal completion给a_r。其余arch factors为0，restricted-product条件满足，得到v_r∈V∞及合法J(r)=[(0,v_r)]∈Φ。

这用的是ambient的completed tensor。02 subgroup的generic实腿是F_η tensor_Q R的**普通代数tensor**，不能因为ambient有hat就把分母也完成。Φ是原literal加法商，不是已经给R/C-Hilbert范数的源载体。Real必要首检失败足以否定全complex关系下降，不需要先为Φ补出complex标量结构。

## 3. 有限jet断点与真正的代数读出

任意finite real jet b_0,…,b_N可由generic differential g=Σb_j t^jdt∈F_η tensor_Q R给出。其global generic diagonal是actual02 boundary，虽然在其它arch branches也同时有展开。故一个忽略其它legs、只依C∞某finite jet的Φ读出必须为零；bare coefficient modZ不是合法捷径。不能由此说单branch截断本身是boundary，也不能把finite-jet证明路线的失败直接当作J失败。

令

    FinQ={a(t)∈R((t)): 全部Laurent系数值的Q-span有限维}。

它是R-linear algebraic subspace，并且

    FinQ = image(Q((t)) tensor_Q R -> R((t)))。

一个方向来自代数tensor是finite sum；反向选全部系数值的有限Q-basis，将各系数的有理坐标逐项排成Q((t))中的series。负幂有限使这些series同样是Laurent series。有限negative part对是否属于FinQ无影响，所以它与domain稿的非负序列商S/B_fin自然对应。

原(7)给01在C∞的arch component来自Q((t))dt本身，系数全Q。原(8)给02的arch component是finite sum Σα_kω_k，α_k∈R、ω_k∈Q(z)dz；在rational frame dt中，每个ω_k的Laurent系数全Q。因此每个actual boundary在这个branch的系数都在span_Q{1,α_1,…,α_m}中。这个m可逐boundary任意大，只需每个实际元素有限。

于是忽略finite legs和其它arch branches、取C∞投影再模FinQ，直接杀掉两个原始boundary subgroups，真正诱导

    ρ:Φ -> T=R((t))dt/FinQ dt。

这不要求finite legs先独立取消，更不要求intersection等于global rational sections。Φ≠G2、A_C不被tensor_R、任何unpaid reciprocity/period lemma都未被使用。它给充分的nonboundary判据：ρ(J(r))≠0即J(r)≠0在实际全Φ中。

## 4. 405实际关系的正确常数与超越尾

405的raw源h=Eη，η(x)=πx²(πx²−3/2)e^(−πx²)，已付M_h(s)=ξ_R(s)/2=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/4。Raw D=d/du满足M_(Df)(s)=−sM_f(s)，所以p=(D²+D)h，不能误成D²−D。

405已给p=Eη₀的真实Schwartz原像、c(p)=d(p)=0、p≠0且noncompact。令physical P=e^(u/2)p；乘半密度保持S_exp，并使本门M_P(s)=M_p(s)。两个physical exponential moments为0，不能与mean0或原像η₀的两项准入条件混同。

具体有

    M_P(s)=s²(s−1)² π^(−s/2)Γ(s/2)ζ(s)/4。

本固定编码的even indices j=2m−2给

    M_P(2m)=q_m π^m，
    q_m=|B_(2m)| 2^(2m−3)(2m)²(2m−1)²(m−1)!/(2m)!
        ∈Q_(>0)。

前项π/6、(2/5)π²、(10/21)π³与405独立常数一致。Euler even-zeta公式和π超越性为标准独立数学事实，不用未知零点位置。任何有限有理线性关系都给π的非零有理多项式，故整个even子列Q-linearly independent。非零real倍λ不改变Q线性关系，因此

    ρ(J(λP))≠0，J(λP)≠0，∀λ∈R\{0}。

特别J在这个固定Pan实直线上作为加法映射是单射。一个实际Pan关系的非零像已否定所需全Pan消去；无需再用537非根测试挽救已失败的necessary gate。

这里只用b=0与实缩放。一般translation的even底数变为πe^(2b)，不能未经证明把π超越性原封套到所有b。解析半径0也不是nonboundary理由：formal空间容许零解析半径的有理系数尾，决定性条件是Q-rank。

## 5. 同一结果的最强修补边界与真实渐近逃逸

ρ忽略任意finite adelic腿及其它arch branches。对每个r，凡合法修补d_r在C∞的系数值Q-span有限，就有ρ(J(r)+[d_r])=ρ(J(r))。规则可以source-adaptive/nonlinear、带任意auxiliary参数，rank无uniform上界，只要每个实际元素仍有限。这些修补不必本身为Φ-boundary；它们属于ρ看不见的更大允许类。

因此每个λ≠0的λP在上述修补的每个实际stage仍有非零像。这与任意有限腿、有限generic或finite-Q-rank∞修补不能**精确**消关系，是同一读出的直接最强后果，应与本结果一次消费，不在后轮领取其较弱子类。

必须同时保留反方向的实际例子。令d_N在C∞为−trunc_N(a_P)，其它components为0。每个d_N合法且属于detector kernel；每stage有ρ(J(P)+[d_N])=ρ(J(P))≠0。然而未商掉的formal ambient中a_P−trunc_N(a_P)→0。在任何使自然商映射连续的原商拓扑下，对应Φ-class也趋0。因此本精确代数边界**不排**同一个target中的rank-growing/cofinal渐近消失；不必先更换target或取closure才出现这种逃逸。

这份truncation对所有fixed源都逐系数趋0，未保537非根或有效容量，故不是新的Weil逼近建设。它只说明ρ不能充当分离的定量误差/容量。FinQ含全部finite Laurent polynomials，在formal topology下稠密；T的自然商拓扑非Hausdorff。ρ只作代数读出，不付distance、du/Dlog、positive Hilbert、mixed RR或完整Weil sign。真正改变∞尾的infinite-Q-rank修复、closure/completed generic分母或不同relative源也未被本稿排除，均需另给实物和费用。

## 6. 前件没有被无声强化

本证明只用已核定义(6)–(8)的field/tensor/diagonal角色，不消费作者Theorem2.1主proof、§4 H¹/protorus、G2显式计算或Example2.3。Boundary coefficient lemma即对原whole subgroup成立，无需假设其有限腿可自由选择或原交集为generic。

失败范围固定为这份Mellin编码及§5所述each-stage exact repair类。Allcomplex、原du/Dlog、整sections/mixed与full-source覆盖仍是原责任；real necessary counterexample不缩窄长期目标。Nonzero Φ类是一个不该留下的Pan类，不是得到新的有效primitive或正号；不能把它当成RH推进的独立正性输入。

有限jet首检仍先执行，发现其不能下商后，没有改源公式、Mellin点、frame、F/C或degree。新full-tail读出由同一原始boundary定义自含给出，完成原定“J是否消真实Pan”的检验；这不是以finitejet路线失败冒称source失败，也不是继续调参寻找预定符号。

## 7. 最强旧扣除与计轮建议

405/519/520早付真实Pan源、完整零点jets商和off-zero Mellin评价。仅M_P(2)=π/6非零当然是旧事实；它不能推出actualΦ class非零，因为02 boundary可以有任意finite real jet。必须额外闭合原boundary分母的ordinary/completed tensor差别和full-tail代数读出，才能把这份旧关系运输到新actual arithmetic quotient。

584的compact-real Laplace measure门及same-B一维像集退化也已实际读作强旧：它们不涵盖本unbounded positive-integer完整formal编码，不提供这里的Φ读出。未将有限阶不杀Pan或已有Green合法性重新报新数学。曾考虑countable moment surjectivity可能给更强像集结论，但既有精确关键词检索未见其已付记录；本稿没有导入Eidelheit/Stieltjes/Durán定理、没有证明或假设onto，也不开新source来取得它。

因此这里多于来源恢复或既有finite-evaluation换名：得到一个对**实际新target**合法的infinite-level读出、一个固定真实关系及其整条real倍的nonboundary证明，并关闭同encoder的完整each-stage finite-leg/finite-Q-rank修补类。它完成原已冻结具体source pair的严格失败研究。建议root实际消费后统一计一个数学迭代；不因尚无C060/597标签判0，也不按lemma、原稿、repair或工具分别计轮。Root仍负责最终最强旧/net结算。

该局部决定确实改变：停止此source pair的principal准入，不能仅加finite legs或逐元素finite-Q-rank纠正便得到exact下降。但关键长期瓶颈没有移除，whole542+555→557 leading4/5负惯性UPPER不变；596保持。这里没有全Weil有利sign、primitive/principal/整sections/mixed建设、危险core/cross或成长Ξ新输入；并未覆盖全部arithmetic/relative/higher或cofinal修复。故Goal三个完成门仍open，不能以repair-class标签通过Goal gate3。

## 8. 现场输入版本与终态

下表为本次实际读取的raw版本；只绑定身份，不代数学证明。STATE由root按阶段修改，不冻结为数学输入。Cadence仅表读取时版本，统一更新由root在消费后执行。

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
| reviews/2026-10-29/formal-mellin-admission/domain-period-and-readout.md | 13380 | `96d0346ca071eaf9ae895e6655254d4010cc92b2e6934db80fb799f6c215b5a9` |
| reviews/2026-10-29/formal-mellin-admission/pan-moments-and-old-consequence.md | 14816 | `a259650e7427965b34cb25e53be81112b97908c8a1467bbeb9b12ced5ead7e18` |

本分工终态：只新增本owned审稿，无STATE/cadence/Goal/Git/库修改，无query、下载、数值、PDF新页或后台进程，无自动后继。两原稿末次raw hash再次匹配；本稿供root全文实际消费后结算，文件存在/消息终态不代消费。
