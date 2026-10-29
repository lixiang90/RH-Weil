# 597. Formal Mellin 源的实际边界反测：无限有理秩与精确修补范围

2026-10-29；C060，G20261027/runtime1793085111、原冻结0c4f。沿AB预先冻结的2723-byte同一源公式，两独占原稿13380/14816、不同fresh13982与root实际全文核后统一消费。新增是实际加法商Φ中的合法无限级读出及Pan反测，不是首次发现旧Mellin评值非零；不主张外部首创。作者定义/版本及原稿绑定见[root消费](../reviews/2026-10-29/formal-mellin-admission/root-consumption-scope.json)。

## 1. 固定实际对象与结果

固定X=P¹_Z，C=∞，U=A¹_Z，F=ω_(X/Z)≃O(−2)。以z为U坐标，t=1/z，e∞=dt，dz=−t^(−2)dt。Osipov2018v2已经核到的定义(6)–(8)给

    A^ar=A_X(F)⊕V∞，V∞=A_(X_Q)(F_Q) completed-tensor_Q R，
    Φ=A^ar/(B01+B02)。

B01由原A01同时对角映入finite/arch；B02的arch generic腿为普通F_η tensor_Q R，F_η=Q(z)dz。Ambient有hat、generic分母无hat，两者不能互换。Φ不是Theorem2.1的终端商G2，本文不用作者主proof、§4或其H¹/protorus身份。

对real physical r∈S_exp，冻结的源是

    M_r(s)=∫r(u)e^((s−1/2)u)du，
    a_r(t)=Σ_(j≥0)M_r(j+2)t^jdt，
    J(r)=[(0,v_r)]∈Φ，

其中v_r只在C∞ branch取a_r，其余arch factors为0。此为本项目自造公式，不归作者。结论是：它虽为合法formal编码，却不消405实际关系。对下述固定real physical Pan源P，

    J(λP)≠0 in actual Φ，∀λ∈R\{0}。                       (1)

更强同链范围是：任意补充finite adelic腿、任意其它arch分量，或在C∞上增加逐元素finite-Q-rank系数纠正，都不能让(1)逐层精确归零。规则可nonlinear/source-adaptive、带任意auxiliary参数，rank不需uniform。此为固定encoder的exact边界；不排cofinal渐近消失，见§5。

## 2. 成员性与finite-jet首检

每个moment绝对收敛。令α=j+3/2，取整数N>α，则

    |M_r(j+2)|≤p_(N,0)(r)[1/(N−α)+1/(N+α)]。

所需强源半范数随j增加，不是du/Dlog单位球的统一费用。固定branch的completed local factor为R((t))dt，integral lattice为R[[t]]dt。无限正幂formal尾合法，不要求解析收敛；有限多项式截断在每个固定jet上稳定，从ambient的formal completion得到a_r。只放一个integral factor、其余为0满足restricted-product条件。

但bare finite jet不能直接下Φ。任意b_0,…,b_N∈R可取generic real rational differential g=Σb_jt^jdt∈F_η tensor_Q R；其global diagonal是02 boundary，在C∞有任意给定jet。因此只依一个∞分支finite jet并忽略其它legs的Φ读出只能为零。不能凭M_P(2)≠0或coefficient modZ就判Φ类非零；也不能把单branch截断误称generic diagonal boundary。

## 3. 真正下降的代数尾读出

令

    FinQ={a(t)∈R((t)): dim_Q span_Q{全部Laurent系数}<∞}。

它是R-linear algebraic subspace，恰为Q((t)) tensor_Q R在R((t))中的像：有限tensor和的系数值落在有限Q-span；反之以系数值的有限Q-basis逐项展开即得有限和。有限负幂不影响这一条件，故亦可用R^(N_0)/B_fin，B_fin为非负序列的finite-Q-span类。

两个实际boundary subgroup的C∞投影都落FinQ dt：

* B01在该rational branch来自Q((t))dt，所有系数有理。
* B02的arch腿是有限和Σ_(k≤m)α_k f_k(z)dz，α_k∈R、f_k∈Q(z)。每个f_k(1/t)(−t^(−2))的Laurent系数有理，故系数值落span_Q{α_1,…,α_m}。

01+02的系数因而落span_Q{1,α_1,…,α_m}；finite腿的兼容只会进一步限制boundary，不会使此条件失效。忽略finite与其它arch factors后模FinQ，真正诱导

    ρ:Φ→T=R((t))dt/FinQ dt，
    ρ([(a_f,v∞)])=[v∞|_(C∞)]，
    ρ(J(r))=[a_r]。                                      (2)

这是实际全Φ的加法读出。无需Φ=G2、A_C tensor_R、period lattice、A01∩A02=F_η或额外reciprocity lemma。它不是positive Hilbert特征或已有范数容量。

## 4. 405固定真实关系与超越系数

405给raw源h=Eη，η(x)=πx²(πx²−3/2)e^(−πx²)，M_h(s)=ξ_R(s)/2。令D=d/du，

    p_raw=(D²+D)h=Eη₀∈P_an，
    η₀(x)=(4z⁴−28z³+41z²−9z)e^(−z)，z=πx²，
    P(u)=e^(u/2)p_raw(u)=(D²−1/4)(e^(u/2)h(u))。

Raw M_(Df)(s)=−sM_f(s)，所以是D²+D。p_raw是真实Schwartz adele限制像，两个raw次数为0；P是本门physical源，两个指数矩∫P e^(±u/2)du均为0。P非零、noncompact且属real S_exp，不将它冒充compact TestFunction。旧405已支付这些源条件，不使用RH。

保半密度后的精确值为

    M_P(s)=M_(p_raw)(s)
          =s²(s−1)²π^(−s/2)Γ(s/2)ζ(s)/4。

对m≥1，取本固定公式的even index j=2m−2。Euler even-zeta值给

    M_P(2m)=q_mπ^m，
    q_m=|B_(2m)|2^(2m−3)(2m)²(2m−1)²(m−1)!/(2m)!
       ∈Q_(>0)。                                        (3)

前三项π/6、(2/5)π²、(10/21)π³，首项与405核对。Euler公式及π超越性为标准独立事实，不使用未知ζ零点位置。任何有限有理线性关系都会给π一个非零有理多项式，因此(3)无限Q-linearly independent。非零实倍λ不改变有理线性关系，故a_(λP)∉FinQ。由(2)得到(1)，并且J在这条Pan实直线上为加法单射。

这里只需固定b=0的Pan关系及all λ≠0。一般平移会把even底数换成πe^(2b)，没有证明对所有b使用同一超越论证；一条真实关系已足否定全Pan消去。零解析半径亦不是判据：formal有理系数尾也可不收敛，关键是Q-rank。

## 5. 最强exact修补后果与实际渐近逃逸

对任何合法纠正d_r，只要其C∞ Laurent系数值Q-span逐元素有限，就有

    ρ(J(r)+[d_r])=ρ(J(r))。

此类允许任意finite legs、其它arch分支，以及逐源/非线性/无uniform rank的finite-Q-rank∞纠正；它们不必本身是boundary。所有λP仍有非零读出，因此不能逐层精确消关系。同一读出的较弱generic/有限位修补子类以后不重计成果。

但令d_N只在C∞取−trunc_N a_P、其余为0。每个d_N合法、在detector kernel中，每stage仍有非零ρ；另一方面ambient formal尾a_P−trunc_N a_P→0。若取使自然商映射连续的原商拓扑，对应Φ类也趋零。故本边界不排同一target中的rank-growing/cofinal渐近消失，不需先改变target才有逃逸。

FinQ含全部finite Laurent polynomials，在formal topology中稠密，T的自然商拓扑非Hausdorff。这里没有distance、du/Dlog、分离正范数、inertia、mixed RR或Weil sign后果。上述truncation对所有fixed源都消掉formal尾，也未保537非根；它不是新的正性建设。真正无限Q-rank∞纠正、改变encoder/分母/完成化/relative carrier仍合法未排。

## 6. 最强旧、计轮与停止

405/519/520已有真实关系、完整零点jets商和off-zero Mellin评值；单个数值非零是旧事实，但它不是Φ读出。584的compact-real Laplace/same-B一维像集门也未涵盖本unbounded countable formal编码。本轮额外闭合原01/02 boundary上的无限级代数读出，再把同一405关系运输到actual Φ，完成一个具体新target的严格失败研究，统一一个数学迭代。

有限jet路线失败后采用同一未变source上的合法full-tail读出，是完成原必要检验，不是调整Mellin点/frame/F/C/degree。未证明/导入countable moment-surjectivity；它不是本定理前件。新C060只登记原2723-byte门的本次结算，不能借标签额外计轮。

停止这份formal Mellin source pair及§5的exact修补类，不再用537挽救已失败的Pan门。非零Φ类是一个不应留下的关系，不是新的有效primitive或正号。算术principal/sections/mixed、危险core/cross、成长Ξ及whole542+555→557 leading4/5负惯性UPPER均未改；Goal三个完成门仍open。
