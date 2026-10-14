# C020：MR 短窗抵消到原 du 范数及 actual Γ 的运输

2026-10-14，`/root/c017_gamma_cross`。依 AGENTS 恢复 README/STATE/check/show、
当前 Goal/frontier/C020/D20261014U、164/167、548 及冻结 MR v3 原件相应 Cor1.4。
实际初读 HEAD bc2a891e885f5cb4412c44c5f10df049cfc9127f，root STATE 已在运行态修改；
latest数学546/cadence0，子 get_goal=null 不代替 root active Goal。
仅编辑本稿，不编辑 STATE/cadence/Git，不单独计数学轮。

本文负责 **从已合法的 MR 输入到原 physical norm 的完整解析运输**。
MR 原证明/μ非pretentious依赖由来源代理另审；root 消费前须合并核准下述精确前件 (M)。
本文没有将来源名字或未核依赖当成已付定理，也没有假设 RH。

## 1. 精确来源前件、对象和结果

需要消费的字符平均短区间输入是

    epsilon(D):=sup_(sqrt D/6≤H≤4sqrt D)
      (DH)^−1 ∫_D^(2D) sup_(|tau|≤6sqrt D)
         |Σ_(x<d≤x+H) μ(d)d^(−i tau)|dx →0。            (M)

sup 字符在 centre 积分内；不改成每centre结论，不改成所有 tau。
这里 sup_H 只是参数统一性，不与 centre 积分交换。
冻结 [MR arXiv2007.15644v3](https://arxiv.org/abs/2007.15644v3) 的 Cor1.4 为 inverse statement。
取 k=1、theta=1/4、一个固定正 epsilon0，H 上述范围最终在 [D^theta,D^(1−theta)] 内，
且 epsilon0 D²/H²≥epsilon0 D/16>6sqrt D 对 D 足够大成立。
若 (M) 在任何 H_D 序列上失败，Cor1.4 给固定 C,Q 的 bounded pretentious distance，
与来源代理支付的 M(μ;CD,Q)→∞矛盾，故是对这整个 compact H-range 统一的输入。
这段只说明准确消费量词，μ的 nonpretentious 原证明仍由来源审查负责。
原字符 d^(it) 与本文 d^(−i tau) 的 sign 由对称 sup 无影响。

令 D→∞（D 可为正实数），冻结

    sqrt D≤T≤6sqrt D，h=1/T，|tau|≤T，Y0≥D，
    a_d=μ(d)d^(−1/2−i tau)e^(−d/Y0)，D<d≤2D，
    V(u)=Σ a_d 1_[log d−h,log d](u)。

原 Hilbert norm 是 L²(R,du)，所有 coefficients 与原 complex phases 保留。
本文在 (M) 下证明

    sup_(T,tau,Y0) ||V||²_(du)=o(1)。                  (1)

还令 actual Γ(t)=Reψ(1/4+it/2)−logπ=2θ′(t)，Γ₀=Γ(0)，
G 为全线 Γ multiplier，Fourier hat V(t)=∫V(u)e^(−itu)du。
对任何 barrier beta≥c log(e+T)，固定 c>0，有

    sup JΓ(V)/beta=o(1)，JΓ=qΓ−Γ₀||V||²≥0，
    sup (2π)^−1∫[1+log(2+|t|)]|hat V(t)|²dt /beta=o(1)，
    sup ||GV||²/beta²=o(1)。                           (2)

并且 a.e. full Γ absolute form integral /beta=o(1)。
这里 operator square 使用 beta²；没有声称 ||GV||²/beta=o(1)，
qualitative (M) 不自动提供那一阶更强 rate。
不由 (1)/(2) 推完整 Q 正性、whole II、sum over growing labels 或 macro Goal 完成。

## 2. exact multiplicative窗口与两个 dyadic边界

置 x=e^u，du=dx/x，c_h=e^h−1。除了有限零测 endpoints，

    V(log x)=Σ_(D<d≤2D, x<d≤e^h x) μ(d)d^(−i tau)w(d)，
    w(s)=s^−1/2 e^(−s/Y0)，H(x)=c_h x。

支撑恰包含于 [D e^−h,2D]；dyadic cutoffs 两端必须保。
对 D≥4，h≤1/2，h≤c_h≤2h；在 x∈[D e^−h,2D] 窗口整数数目≤4sqrt D+2，
|a_d|≤D^−1/2，故 |V(log x)|≤6（D 足够大，常数统一）。
左 strip [D e^−h,D] 和右 strip [2D e^−h,2D] 的各自 du 长度都是 h。
不需要任何 MR 输入，其总 squared norm≤72h=O(D^−1/2)。
strip 外的 interior x∈[D,2D e^−h] 是完整未截窗口 (x,x+H(x)]；
原 cutoff D<d≤2D 没有丢失任何 positive-measure overlap。
open/closed integer endpoints 只改变有限 x，norm 不受影响。

## 3. monotone amplitude付款，不用免费maximal部分和

对 s≥D、Y0≥D，w 为 real positive decreasing amplitude，

    |w′(s)|=(1/(2s)+1/Y0)s^−1/2e^−s/Y0≤(3/2)D^−3/2。

interior 的 H(x)≤4sqrt D，故将 w(d) 冻结在 leftpoint x 后，

    |Σ_(x<d≤x+H(x)) μ(d)d^−i tau[w(d)−w(x)]|
    ≤(3/2)D^−3/2 H(x)[H(x)+2]=O(D^−1/2)。            (3)

误差原 du squared norm 是 O(D^−1)，对 T、tau、Y0 统一。
phase d^−i tau 完整保留在 MR sum，未用 derivative 或局部常相位假设替代。
此方法直接付 local monotone/BV weight variation，不需要 Abel 后的 supremum partial sum 输入。

## 4. variable H的固定网格：D极限先于网格极限

固定任意整数 K≥1，不随 D 增长。
把 [D,2D] 分成 K 个 centre 子段 J_i=[x_i,x_(i+1)]，x_i=D(1+i/K)。
冻结各段长度 H_i=c_h x_i。对 x∈J_i，

    sqrt D/6≤H_i≤4sqrt D，
    |H(x)−H_i|≤2sqrt D/K。

因此两个 sum 的不同整数数目≤2sqrt D/K+2；乘 |w(x)|≤D^−1/2 后，
窗口替换的 pointwise physical 误差≤2/K+2D^−1/2。
其 squared du norm≤C/K²+C/D。没有把任意 partial-window maximum 免费加进 (M)。

记 S_i(x,tau)=Σ_(x<d≤x+H_i)μ(d)d^−i tau。
H_i→∞统一，trivial |S_i|≤H_i+2≤2H_i，故

    |S_i|²≤2H_i |S_i|。

用 (M) 与 positivity，仅把 J_i 积分上界为整个 [D,2D]：

    ∫_(J_i) sup_tau |S_i|²dx
    ≤2H_i ∫_D^(2D) sup_tau|S_i|dx
    ≤2H_i²D epsilon(D)≤32D² epsilon(D)。

又 |w(x)|²dx/x≤dx/D²。所以 fixed K 的 interior main contribution≤32K epsilon(D)。
联边界、(3)与固定网格误差，得到 absolute C 的原norm门

    sup_(T,tau,Y0)||V||²
    ≤C[K epsilon(D)+K^−2+D^−1/2]。                    (4)

先固定 K，D→∞；再 K→∞，即得 (1) 的严格 uniform o(1)。
不是选未付 K(D) rate；MR 的 qualitative statement 已够。
不以 finite grid sample 代 theorem，所有 centre x、变量 T/窗长度和复杂 phase 已解析覆盖。

## 5. Fourier identity、实际domain与既有尾mean-value

chi_h(u)=1_[-h,0](u)，原 source 有 exact Fourier factorization

    hat V(t)=hat chi_h(t)P(t)，
    hat chi_h(t)=(e^(ith)−1)/(it)，
    P(t)=Σ_(D<d≤2D) μ(d)d^−1/2e^−d/Y0 d^(−i(tau+t))，
    |hat chi_h(t)|≤min(h,2/|t|)。                     (5)

每个 fixed D 是 finite BV compact source，所以属于 Dlog；
甚至 Γ²(t)=O(log²(2+|t|)) 与 |hat V(t)|=O_(D)(1/|t|) 给 V∈Dom G。
以下再付 uniform Γ费用，而非只凭 fixed-D domain 标签。

系数 square mass≤Σ_(D<d≤2D)1/d≤2，不受 tau 或 Y0 影响。
消费旧 133 引理 XY / 150(14) 的 elementary mean-value bound（强 Montgomery–Vaughan 不必）：
对任何 basepoint、任何长度 X 的频区间，degree≤floor(2D)+1 的原 Dirichlet polynomial 有

    ∫_interval |P(t)|²dt
    ≤[X+4N_poly H_(N_poly)]Σ|a_d|²
    ≤C[X+D log(2D)]。                               (6)

该 elementary proof 仅展开积分、用 cross integral≤2/|log(n/m)|、
|log(n/m)|≥|n−m|/N_poly，再 quadratic Cauchy/调和sum；
对 arbitrary initial phase、正负shells和所有 tau 成立。
不是对 old prime coefficients 的专用结论，也没有请求新的ζ零点信息。

## 6. Γ/Dlog归一化全频付款

冻结 frequency division R_D=D²，完全不是数值 cutoff。
已有 actual Γ全轴界 |Γ(t)|≤10[1+log(2+|t|)]，两端归一化仍是 (2π)^−1。
对 p∈{0,1,2}，在 dyadic positive/negative shells |t|∈[X,2X]、X≥D²，
(5),(6) 给

    (2π)^−1∫_shell [1+log(2+|t|)]^p |hat V(t)|²dt
       ≤C_p [1+log(2X)]^p/X。

求和所有 shells（含负轴）得到

    (2π)^−1∫_(|t|≥D²) [1+log(2+|t|)]^p|hat V(t)|²dt
       ≤C_p [1+log D]^p/D²。                         (7)

tail 全部付清，没有把 sampled band 或 finite matrix 当误差。
在 |t|≤D²，log weight≤C log(e+D)，所以由 Plancherel 和 (1)，

    absolute Γ form integral≤C log(e+D)||V||²+C log(e+D)/D²，
    Dlog graph energy≤C log(e+D)||V||²+C log(e+D)/D²，
    ||GV||²≤C log²(e+D)||V||²+C log²(e+D)/D²。          (8)

sqrt D≤T≤6sqrt D 使 log(e+D)/log(e+T) uniformly bounded。
除以 beta 或 beta²，(8) 严格证明 (2)。JΓ 由 |Γ|+|Γ₀| 的同源 integral付款。
MR **只**用于原 tau 范围的 physical cancellation；
(5)中的 tau+t 在全轴可很大，但 (6)是既有 generic tailmeanvalue，不是假定 MR覆盖所有tau+t。

若把 V 平移并零延拓嵌入一个原Weil区间 I，global Γ norm不因平移改变，
Γ_I 的 operator norm由压缩只下降，form值仍按原zeroextension fullΓ计算。
这不运输全部prime或pole的费用；它们的 signed/core耦合必须另付。

## 7. scope、净值及仍未付责任

来源贡献是 MR 平均 μ 的独立 signed cancellation；generic尾meanvalue/Γ/BV都是旧工具。
本稿提供的是其新的原du变量短窗 transport，在原complexsource、aspect[1,6]、
|tau|≤T、Y0≥D 的统一范围内，及 (2) 的实际Γ/Dlog费用。
不声称 pointwise centre、所有字符height、任意非乘法 coefficient、b_U或fullII的MR结论。

冻结finite κ≤8 mask若由独立原164同源审核确认，则 (1)/(2)可按固定有限Cauchy/Gram运输，
其全exactproduct collisions仍在shared u中；不删除 cross 或把 coefficients norm 换掉。
本文不负责把这一 finite head 升为完整cofactor范围。
fullκ≈Y/U处 Hκ≈1/log²Y，MR polynomial窗口不覆盖；
qualitativeepsilon→0也不支付 growing-label sum、TypeI/continuum或wholeΓ/双pole比较。
单 L² 小或 normalized Γ费用小都不推出完整 Qpositive、nearPSD、wholecount或宏观Goal完成。

问题：合法 MR 前件能否在 actual physical source 付窗范数及 Γ费用？
已付运输：(4)、(5)–(8)，原 Jacobian、variableH、dyadic端点、monotoneweight与全频/domain均保留。
前件：root尚须消费来源代理的 MR/μ非pretentious原证明与 uniformH量词；本稿不代来源审。
未付：全部cofactor/growing-label共同费用、wholecore/complement/coupling、TypeI/continuum与Ξ。
瓶颈：该 finite-aspect rawμ source费用可消，但主要core责任另由 coverage审确定。
轮数/Goal：本代理不结算；root只有在来源与实际mask/net范围核准后才统一计本合同一次。
仅有限head成功不能继续小head循环，也不能完成完整Goal。

## 8. 同轮直接 corollary：任意先固定的 finite aspect

2026-10-14，root 请求为每固定 cofactor 的 dominated-convergence 核验补充此直接推论。
原冻结 aspect6 的首门不变；没有开第二轮、扫描κ或声明所有height结论。
对任意 **先固定** 常数 B≥1，把参数范围写为

    sqrt D≤T≤B sqrt D，h=1/T，|tau|≤T，Y0≥D。

原 source 输入只需对应的

    epsilon_B(D):=sup_(sqrt D/B≤H≤4sqrt D)
      (DH)^−1∫_D^(2D) sup_(|tau|≤B sqrt D)
         |Σ_(x<d≤x+H)μ(d)d^−i tau|dx→0。              (M_B)

Cor1.4 固定 k=1、theta=1/4 和 epsilon0 的 allowed time≥epsilon0 D/16
最终包含 Bsqrt D，而 D²/H²∈[D/16,B²D]。
source nonpretentious lemma针对任意先固定 C,Q，故对这整个 fixed-B compact aspect统一；
若任何 H_D 序列失败，inverse constants仅依赖 fixed-B/threshold结构参数，得到同一矛盾。
这里没有利用错误的 M 关于 cutoff 的单调性，也不让 B 随 D 增长。

Sections 2–6 的 norm/domain/weight/endpoint/Fourier证明完全保留，
只把 H_i 的下界 sqrt D/6 替为 sqrt D/B、phase bound替为 Bsqrt D。
H(x)≤4sqrt D、dyadic boundary h≤D^−1/2、coefficient square mass≤2、generic尾meanvalue均不变。
所以对每 fixed B，

    sup_(sqrtD≤T≤BsqrtD, |tau|≤T, Y0≥D)||V||²=o_B(1)，
    sup JΓ(V)/beta=o_B(1)，
    sup Dlog_graph_energy(V)/beta=o_B(1)，
    sup ||GV||²/beta²=o_B(1)，beta≥c log(e+T)。         (9)

依旧先 fixed centre K，D→∞，再 K→∞。
没有 effective rate、uniform-B claim、B(D)准入或MR fullheight扩张。

例如每固定 κ≥2，D=Y/κ、sqrtY≤T≤2sqrtY 给 finite Bκ=2sqrtκ。
shift u↦u−logκ 不改 full Γ 或原du norm；固定 scalar logκ κ^−1/2−i tau 也无 growing-label费。
(9) 因而支付每一个先固定的 κ 源；root/macro 审可另用已证明的 source-free summable trace tail，
在先 Y→∞、再有限labelcutoff→∞的次序消费这些 fixed-label极限。
本稿没有支付该 full tail、fullcofactor Γ trace、operator synthesis质量或TypeI/continuum/completeQ。
归一化Γ仍区分 form/beta与operator平方/beta²，不作未核强费用扩张。
