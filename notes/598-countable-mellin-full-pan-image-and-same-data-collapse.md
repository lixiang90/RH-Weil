# 598. 可数 Mellin 完整像与同数据处理的退化

2026-10-29；G20261027/runtime1793085111，原冻结0c4f。597后的2559-byte明确准入已实际执行；三角原稿12702、强旧审查13068、不同fresh12070均冻结，root全文读并独立重导后消费。C061只登记这个不同full-image责任的一次结算，不续C060、不倒填597前件。不主张外部首创，不导入一般矩问题存在定理。[前件记录](../reviews/2026-10-29/full-image-moment/root-consumption-scope.json)。

## 固定对象与完整结论

源为405同一real physical Fréchet空间F=S_exp，p_(N,k)(r)=sup_u e^(N|u|)|D^k r(u)|，所有整数N,k≥0均有限。U f=e^(u/2)f运输raw→physical；raw实际像J=E(S_even,0)，P_an=closure(J)∩ker c∩ker d。固定数据

    α_n=n+3/2，ℓ_n(r)=∫r(u)e^(α_n u)du=M_r(n+2)，
    B(r)=(ℓ_n(r))_(n≥0)。

B是可数数据，不是Weil配对。目标为所有实序列，未附增长约束。新结论为

    B(F)=B(U(J∩ker c∩ker d))=R^(N_0)。                    (1)

所以全部physical Pan像已经覆盖全部源像。这里实际J而非仅闭包已有代表；不是finite jets、product-density或一条非零关系。复化两边直接得C^(N_0)，但不赋597 actualΦ新的复结构。

## 自含三角插值

固定非零非负ψ∈C_c∞((0,1))，L_n=∏_(k<n)(D+α_k)ψ。紧支分部积分给

    ℓ_j(L_n)=∏_(k<n)(α_k−α_j)ℓ_j(ψ)，
    A_n=ℓ_n(L_n)=(-1)^n n!ℓ_n(ψ)≠0。

给任意实序列b，递归令δ_n=b_n−Σ_(i<n)ℓ_n(g_i)，并取

    g_n=(δ_n/A_n)e^(-α_n a_n)τ_(a_n)L_n，τ_a f(u)=f(u−a)。

每个δ_n有限。选a_n≥n+1、a_n≥a_(n−1)+2，并足够大。对N,k≤n，

    p_(N,k)(g_n)≤C_n e^(-3a_n/2)≤2^(-n)，
    C_n=|δ_n/A_n|max_(N,k≤n)e^N||D^k L_n||∞。

关键是α_n−N≥3/2，无须C_n或b的增长界。支集局部有限；G=Σg_n是实际光滑函数。任意先固定N,k的半范数绝对尾可求和，所以G∈同一F且级数在全部原半范数中收敛。

固定j后取整数N>α_j，有

    ∫|f|e^(α_j u)du≤[1/(N−α_j)+1/(N+α_j)]p_(N,0)(f)。

因此moment与级数的交换绝对合法；n>j的每项严格为零，第j项补齐残差。于是ℓ_j(G)=b_j对全部j同时成立，一个G实现整个序列。所需源费用随数据与j变化，不是原du/Dlog的统一控制。

## 同一序列的实际 Pan 代表

405/597固定raw p=(D²+D)h=Eη_0∈J，c(p)=d(p)=0，physical P=Up。给G∈F，置raw g=U^(-1)G。实际源

    η_g(x)=∫g(t)η_0(e^(-t)x)dt

满足q_(a,b)(η_g)≤q_(a,b)(η_0)∫|g(t)|e^((a−b)t)dt；η_g偶Schwartz、η_g(0)=∫η_g=0。E求和换序由Σ_m|η_0(mλ)|≤C/λ及∫|g|e^t<∞支配。因此g*p=Eη_g确在实际J中，raw双矩仍零。

U(f*g)=(Uf)*(Ug)，故Q=P*G=U(p*g)是真实physical Pan。两个physical零矩为指数±1/2。带权绝对Fubini给M_Q(s)=M_P(s)M_G(s)，参数没有半密度错位。已付公式

    M_P(s)=s²(s−1)²π^(-s/2)Γ(s/2)ζ(s)/4

在s=n+2≥2严格正，不用RH或π超越性。把前节插值用于b_n/M_P(n+2)，所得Q即有B(Q)=b，完成(1)。完整原像、换序和源界见[三角原稿](../reviews/2026-10-29/full-image-moment/triangular-interpolation-and-pan-ideal.md)。

## 一并消费的最强后果

对每个fixed r∈F，有一个fixed Q_r∈U(J∩ker c∩ker d)，全部B(Q_r)=B(r)。因此：

* 任意仅依B的set postmap，若把全部Pan送到同一base，就在全部源上常值；无需连续、线性、局部、有限秩、范数或Hausdorff假设。仅依B选择的自适应参数仍在范围内。
* 597的J_formal=ι∘B满足J_formal(Pan)=J_formal(F)。进一步actualΦ商或同数据处理无法同时消全部Pan并保537非根。
* 配对H(B(r),B(s))若对全部Pan第一槽及全部源第二槽为零，就在全源上为零，不能恢复537严格正值的完整Weil配对。
* 任意indexed族F_κ(B(.))对r与同一个Q_r逐阶段完全相等。因此只要求每个fixed Pan点态渐近归base，也迫每个fixed源归base；mixed版本同样成立。纯同B、同全局域的点态渐近不再是逃逸。

若每阶段exact杀全部Pan，则每阶段全源常值，连joint成长源也不能保信息。若仅逐fixed Pan点态消失，则没有成长源一致率，不能外推uniform费用。597的形式截断渐近消所有fixed源，和本结论一致；它并未保住537。

## 强旧扣除、合法逃逸与停止

405真实ideal、519/520完整零点jets及谱商是依赖；finite-cover旧稿已付finite projections同像与infinite product-density。当前有限δ_(α_j)虽非L1，α_j避开pole，405平移的有限指数独立性也已给有限满像，不能重领。584一维same-data与compact-real唯一性同样是强旧。新增仅在**同一S_exp的exact无限序列及实际Pan全像**；标准后处理/mixed/渐近推论均并入同一轮。

真正未排的是B外额外实际源/finite/arch/relative数据、不同encoder或实际源域使Q_r不准入、只测较小关系类，以及不在全局F上承担全部Pan点态消去的独立正D′比较。费用任意大不救同数据集合障碍，但集合满射不付原du/zero-extension Dlog、连续线性选择、成长窗/Ξ、独立primitive/principal/截面/mixed RR或危险core/cross的有利净号。

C061统一一个数学迭代，原cadence仅一次3→4/history61→62/latest598，formal19先保持。随后允许在4及时正式宏观审视，复盘本身0数学，不先归零。固定编码的完整同数据边界不是长期Goal第三门的自动验收；whole542+555→557 leading4/5负惯性UPPER及关键瓶颈不变，同Goal active/open。停止本编码及其exact/pointwise后处理续造，不调采样/frame/degree或自动读旧来源后章。
