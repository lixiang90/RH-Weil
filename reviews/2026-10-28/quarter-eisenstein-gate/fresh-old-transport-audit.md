# Quarter E* scalar族：独立强旧消费审查

2026-10-28；`/root/scalar_upper_tail` 当前独占fresh，非C052 upper续算。已恢复README／STATE、check→show、G20261027／原0c4f、AK／589结算、frontier及root给定actual packet。已全文核root5758b、domain9226b、oldscope终稿11463b及其必要C016／545／whole-frequency原记录。未web、下载、重审Zagier／Garrett原PDF、开新source／合同或修改共享稿／STATE／Git／cadence。

**限定PASS：可以按强旧exact组合0消费，停止当前quarter-slice E*／保留cusp／source-independent scalar校准的明确族。** Fixed-Y存在和whole-L²运输原本已付；cofinal logY公式虽未逐字印于545，却由同一DIRECT、FE及标准theta恒等式，在本次明确闭合的局部域／尾下直接推出。不是仅凭标题判旧，也不是把未付norm标成已知。此审不代root最终消费／发布，不授C053／590或额外轮次。

## 1. 两个actual旧输入和restriction／truncation区别

545和C016已经固定同一个s_t=1/4+it/2，2s_t=1/2+it；Z(w)=π^(−w/2)Γ(w/2)ζ(w)不是entire ξ。E*=Z(2s)E，几何s=0／1 poles与actual w=0／1双pole不同；s=1/2点值内部相消不是新输入。

旧p(s)=s(s−1)清极点后的completed family F_Y在whole-L²(du)上有fixed-Y absolute Bochner／HS map A_Y。沿real t，p_t=−3/16−t²/4−it/4，|p_t|≥3/16。因此qhat=F_r/p_t是真bounded Fourier输入变换，q通常不compact，但恰在旧whole-L²域内。它给A_Yq=Λ^Y V_r，不需除critical ζ或假设其零点位置。

同一packet的更有用表示是旧FE

    E*(z,s_t)=b(t)E(z,3/4−it/2),   b(t)=Z(3/2−it),
    hhat(t)=F_r(t)b(t).

b为旧bounded／Gamma双尾乘子，h∈whole-L²，F_r b∈L¹；旧direct T_Yh=Λ^Y V_r，原dt/(2π)、complex槽及du norm不变。这里h不是原fixed-L compact源，不能把两种旧域混同。

当前G_Y是𝔽_Y上的**restriction Gram**，旧Λ^Y只删除y>Y的constant x-mode而保留非constant Fourier modes；两种norm相差y>Y非constant能量。固定Y的whole-L² map直接给restriction合法，但fixed-Y compactness／√Y粗界本身不判Y→∞的校准比值。当前两稿和root均明确保留此差异。

## 2. Theta kernel的Fourier、尾和两个不同源矩

Gamma积分在Re w=3/2>1绝对收敛，直接换元v=e^(2u)核得

    k(u)=2e^(3u/2) Σ_(n≥1)e^(−πn²e^(2u)),
    khat(t)=Z(3/2−it)=b(t),    h=r*k.

Jacobi恒等式给

    k(u)=e^(u/2)−e^(3u/2)
              +2e^(u/2)Σ_(n≥1)e^(−πn²e^(−2u)).

故k为Schwartz；r先fixed compact时，h负端为

    h(u)=μ_−(r)e^(u/2)−μ_(−3/2)(r)e^(3u/2)
                  +superexponential remainder,

正端同样superexponential，μ_a(r)=∫e^(au)r(u)du。各余项允许源依赖的常数与指数前因子；没有交换source与cusp成长的一致性量词。

特别地，μ_−≠0时∫e^(−u)|h(u)|²du发散，所以不能由h∈L²偷用旧compact／fixed-L的uniform-Y overlap界。正确旧polar积分却绝对收敛：

    (6/π)∫h(u)e^(u/2)du
        =(6/π)F_r(i/2)b(i/2)=μ_+(r),   b(i/2)=Z(2)=π/6.

μ_−控制threshold／√y主项，μ_+控制DIRECT的几何constant residue；两者不是一个矩，也没有把几何pole直接识别为完整Weil双pole。

若讨论unitary line s=1/2+it/2，其bare spectral coefficient是F_r(t−i/2)Z(1+it)，在零点为μ_−(r)/(it)+O_r(1)。这个**系数**属于ordinary L²的条件正是μ_−=0；pointwise E*(1/2)可去／E(1/2)=0不能免费付款该条件。本消费不依赖一个未经核实的unitary contour／Plancherel定理：实际global cusp结论由下面的DIRECT延拓独立获得。

## 3. 非compact h的局部DIRECT延拓已闭，不预设全cusp L²

取0≤χ_N≤1的compact smooth cutoffs，h_N=χ_Nh。h_N→h于L²；旧545 direct whole-L² fixed-Y bound给T_Yh_N→T_Yh。对h_N，旧exact式是

    T_Yh_N=P_Y[Θg_(h_N)−(6/π)∫h_N e^(u/2)],
    g_h(v)=v^(3/4)h(−logv/2).

极化／packet系数及old residue6/π都已在旧whole-frequency§9.3核定。本次延拓只需每fixed Y，不用常数uniform于N的fixed-support估计。

g_h(v)在v↓0有C_r exp(−c_r/v)上界（固定幂可吸收），在每个bounded height interval也有界。每个𝔽_Y的coset heights满足1/v≥c_Y(c²+d²)，并且|g_(h_N)(v)|≤|g_h(v)|。于是存在与N无关、在该几何compact域统一可求和的Gaussian majorant。Domination使Θg_(h_N)在每fixed Y局部一致／L²趋Θg_h；polar积分也由绝对收敛取极限。

因此同一actual V_r在全部finite-height域上有

    V_r(z)=Θg_h(z)−μ_+(r).

这不是先假设V_r在整个未截断cusp属于L²：μ_−≠0时它事实上不属于。这里支付的是旧全L²输入连续性与coset局部domination，两个空间角色不能互换。

## 4. Coset尾给精确logY系数，非只用预期主项

Identity coset的seed为

    g_h(y)=μ_−(r)√y−μ_(−3/2)(r)+O_r(poly(y)e^(−c_r y)).

对非identity项c≥1，v=y/[(cx+d)²+c²y²]，所以1/v=c²y+(cx+d)²/y。用small-v指数界放宽到全部整数d，先求Gaussian d-sum，再求c-sum，统一x∈[−1/2,1/2]得到

    Σ_(c≥1,d∈Z)e^(−c_r[c²y+(cx+d)²/y])
                     ≤C_r√y e^(−c'_r y).

因此没有第二份√y主项，actual未截断packet的cusp为

    V_r(x+iy)=μ_−(r)√y−μ_(−3/2)(r)−μ_+(r)
                              +O_r(poly(y)e^(−c'_r y)).

原cusp宽度1、measure dxdy/y²给全部先fixed complex源对

    G_Y(r,s)=μ_−(r)overline(μ_−(s)) logY+O_(r,s)(1).

只有√y×√y项产生log，sqrt／constant mixed项和余项都绝对可积。误差不须对moving源一致。当前root／两具体稿把这一步实际展开，不能在恢复时只留下“cusp应为rank1”的希望；若去掉第3节延拓或本节coset尾，只能保fixed-Y合法，不能消费这条cofinal式。

## 5. 完整fixed test及准确旧0范围

r₀为原正bump，μ_−(r₀)>0，所以G_Y[r₀]>0最终成立。α_Y=q₀/G_Y[r₀]给全部先fixed源对极限

    α_Y G_Y(r,s)→q₀ μ_−(r)overline(μ_−(s))/|μ_−(r₀)|².

任意source-independent positive β_Y若β_YG_Y[r₀]→q₀，也同样。它是pole-coordinate rank1，区别于589的mean rank1；不是把589套到几何新源。有限Y的Gram一般不stationary，该极限也不自动是一变量positive D′或全D′拓扑极限。

取r_*=(D²−1/4)r₀。Compact非零r₀不可能解r₀″=r₀/4，故r_*非零；分部积分精确给μ_±(r_*)=0。它仍为537同小窗／原zero-extension Dlog的合法complex源，并不必mean0。上式给G_Y[r_*]=O(1)，故校准值趋0；而完整Q_W[r_*]≥2^(−49162)||r_*||du²>0。Γ／FP-contact、全部properpowers和双pole都保留在完整target；这里只是这个fixed test的actual双pole项确为0。

Quarter参数／完成化／真实Gram／direct whole-L²和DIRECT exact式在545已经存在。当前去p仅bounded输入，去completion后的非compact tail及cusp展开是旧FE、Re>1 Gamma积分、Jacobi及旧连续性的普通直接组合。545文字未逐字给出这个literal threshold packet的logY公式，不能伪称“原文已有同一句”；但完整短依赖链现在已付，未引入新算术估计、独立正性或source机制，按强旧合成0消费准确。

仅停止当前E* quarter-slice、保留cusp、原几何cutoff及scalar校准的族。不泛排paid signed cusp、不同seed／base／source域、新非紧或joint nonlocal修复、其他正D′及primitive主线。原C016的扣完整cusp后blindband是不同用途，不被拿来直接判本GY；也不因本次失败新授cusp subtraction或下一来源预算。whole4/5负惯性UPPER、完整signed/corecoupling、primitive/principal/mixed／Ξ及Goal完成门未改。cadence3/history53/latest589/formal17保持，0数学轮。

## 6. 当前终态与版本绑定

下列current原件已实际读完并核范围。Oldscope先读11453-byte版，随后唯一变更为C016实际文件链接修正；终态11463-byte版本已现场核新hash／正确链接，数学内容保持。该链接修正不是semantic dependency变动。

- root-quarter-packet-and-old-admission.md：3051bytes，LF SHA256 `b778a43ace0eee08e2c520ebc4a1b054013a16a4841a32aa345c334520df2270`。
- root-old-theta-transport-draft.md：5758bytes，LF SHA256 `f208961bf830ccdca713a6cf9c39fdb7df5ba6ec83521577422182ccd90e94ab`。
- quarter-slice-domain-and-cusp-test.md：9226bytes，LF SHA256 `2ce9b414503627dfbc6bfcd5828c60e13314c460f92d88c612f4644d817ca276`。
- strongest-old-packet-transport.md：11463bytes，LF SHA256 `002c9ceb86d5f8e7c355bdfe32f36b41846cfe89540bab6cabab09520f6cc26b`。

旧必要原件为545全文、实际 `goals/contracts/C016-modular-cusp-gram-and-actual-weil-transport.md`，whole-frequency §§8–9.3及原cusp-completion必要DIRECT接口；没有重审外部PDF。该审仅写本独占文件，待root统一前件消费／决定／发布；不会因文件存在自行增加轮数或完成Goal。
