# Restriction square 的二次容量、原范数与正反检验

2026-10-22。独占审稿；不改公共状态、Goal、cadence或Git。本文是一个具体候选的准入检验，未提出新的数学合同。

## 1. 判断与最强旧扣除

实际 adelic restriction 是一个不以 Ξ 零除子为定义的合法起点；但把其两项复形作 external square 或 balanced derived tensor，本身不生产函数域证明所需的 primitive 平方 RR。应区分：

1. 真实 restriction 的 kernel 与非零 section/evaluation minor；
2. 对两个旧曲线容量作张量后出现的二次维数；
3. 同一算术平方上全部 signed 对应的交数二次项、独立有效化/乘法与固定容量。

只有第三项接上完整 Weil 型，才能支付当前容量责任。第一、二项确有具体计算，不应称不存在；二次维数也不应自动称作第三项。

旧扣除：405 给实际 Eη、P_an=I∩ker(c,d) 和两 degree；519 给完整 zero-jets 的像识别；553 已给 physical P_an 在原全线 du/Dlog 的平移闭包稠密与 cofinal 费用；407–408 已给非零相对完美对象、逐 idele 零化及指定完成的真实边界行为；567 已恢复真函数域平方 RR；568 已给连续正反载体及有限局部 jets。本文不重新计这些资产。

## 2. 一个 exact finite-stage calculation：restriction 外平方的真实含义

在任意域 k 上，取有限维两项复形 C=[U --E--> V]，置于次数 0、1。记

    u=dim U, v=dim V, rank E=a,
    K=ker E, Cok=coker E, k0=u−a, c0=v−a.

在域上所有向量空间平坦，故 external derived tensor 就由普通总复形计算：

    C⊠C : U⊗U → (V⊗U)⊕(U⊗V) → V⊗V,
    d0=(E⊗1,1⊗E),   d1=(−1⊗E,E⊗1).

Künneth（也可选基将 E 化为 diag(I_a,0) 直接证明）给

    H0=K⊗K,
    H1=(Cok⊗K)⊕(K⊗Cok),
    H2=Cok⊗Cok,
    χ(C⊠C)=(u−v)^2.

因此出现 k0² 或 χ² 并不需要算术、对偶或正性；它首先是两份线性数据的乘法。χ(C⊠C)≥0 也不给任意 primitive signed 对应的负自交；它只是平方后的一个数。

### 2.1 真曲面与抽象平方的准确比较

取真曲线 P¹_k，E={0,1} 为两个不同 k 点，U_n=H⁰(P¹,O(n))、V=k²，n≥0，限制矩阵是

    E_n = [(1,0,…,0); (1,1,…,1)].

对 n=0，rank E_n=1；对 n≥1，rank=2，且 kernel 为 x(x−1)H⁰(O(n−2))。乘法有真实来源：kernel 的零点次数会相加，不能随意把某个小子空间当所有截面。

由 exact sheaf sequence，C_n=[U_n→k²] 计算 RΓ(P¹,O(n−2))。在真实 P¹×P¹ 上，其外平方确实计算 RΓ(O(n−2,n−2))。于是得到真正的几何容量及 χ=(n−1)²；这不是假 RR。但其额外来源是已经存在的 proper product surface、线丛、限制序列与 coherent cohomology，而非单凭某个 E_n 的矩阵名义。

本次实际用 Fraction 精确行消元计算 d0、d1，并逐项核 d1d0=0，得到：

| n | 总复形维数 | rank d0, rank d1 | dim H0,H1,H2 | χ |
|---|---|---|---|---:|
| 0 | 1,4,4 | 1,3 | 0,0,1 | 1 |
| 1 | 4,8,4 | 4,4 | 0,0,0 | 0 |
| 2 | 9,12,4 | 8,4 | 1,0,0 | 1 |
| 3 | 16,16,4 | 12,4 | 4,0,0 | 4 |
| 4 | 25,20,4 | 16,4 | 9,0,0 | 9 |

此表是上面一般恒等式的 exact finite check，不代一般证明。该真例还说明为何必须保留高阶上同调：n=0 的 χ=1 全来自 H²，并非有一个非零全局小截面。

同一真曲面可进一步比较 signed primitive D=F1−F2：D²=−2，O(n,−n) 在 n≥2 有 h⁰=h²=0、h¹=n²−1、χ=1−n²；而正方向 O(n,n) 的 h⁰=(n+1)²。将两份 positive section count 相乘，并不能自动产生这个 signed 方向的交数及其全部 graph mixed terms。

不得过强地说“一维曲线永无 n²”：P¹_Z 是绝对维数2的 arithmetic surface，确有实际二次小截面计数，无须仅作形式命名。取 O(1) 的标准 toric metric，再作 arch constant twist a>0；对 n 次的整系数多项式 P=Σ_(j=0)^n a_j z^j，小截面条件为

    sup_(z∈C) |P(z)|/max(1,|z|)^n ≤ e^(an).

Cauchy 的 unit-circle coefficient bound 与 triangle inequality 给

    max_j |a_j| ≤ ||P||sup ≤ Σ_j|a_j|.

故小截面数介于

    (2 floor(e^(an)/(n+1))+1)^(n+1)
    与 (2 floor(e^(an))+1)^(n+1)

之间，从而 log#=a n(n+1)+O_a(n log n)。这是同一真实 arithmetic surface 上 n² 的独立 elementary 容量，finite-place 整性及 arch metric 都明确。它仍不提供源 r→这个线丛/截面的关系相容 map、signed primitive 系数或 full Weil identity；a 是外加 twist，不能按 Q(r) 选择后称作证明。552 的真 adelic metric 另有实际 self-intersection；其问题是原主关系与 full Weil 比较失败，而非没有任何 n²。当前需要的是特定同对象、正确方向和全源身份的二次项。

### 2.2 Balanced tensor 必须先给类型与 Tor

407 的 K=[R --L_v--> R] 是右 R 模复形，R 为非交换 crossed product 的单位化。不能直接写 K⊗_R K：第二因子所需的左作用/双模结构尚须指定，且须和实际 restriction、对应复合相容。

即使在交换环上 balanced tensor 可定义，也不能丢 Tor。例如 K_p=[Z --p--> Z]（次数 −1、0）有 H⁰=Z/p，非零；其 derived self-tensor 有 H⁰=Z/p、H⁻¹=Z/p。两个有限群的 alternating log order 为 0，而不是新增的 2log p 或 (log p)² 容量。普通 tensor 只留 H⁰ 会多算预算。这是 exact elementary model，未冒称 K_p 就是405或407的算术对象。

## 3. Actual prime-arrow control：逐纤维可缩，外平方不能恢复被该函子抹掉的信息

沿407的真实对象

    R=(S(A_Q)⋊_alg Q×)^+,
    a=1_Zhat⊗η, η(r)=πr²(πr²−3/2)e^(−πr²),
    v=1−z aU_q, q prime,
    K=[R --L_v--> R].

K 在源 Perf(R) 非零，且本例两侧无零因子、v 非单位，这些都已付。每个 idele restriction ρ_b(v) 可逆，故基变换后的复形有实际 contracting homotopy ρ_b(v)⁻¹。任何合法的 external tensor square 仍可缩：对一个可缩因子取 h⊗1，Koszul 符号使交叉项相消。这里不需要把普通 tensor 误称 source Tor，也不需要 RH。

一个最便宜的真实 finite cut-off：沿 q^j 轨道取前 N 个坐标，单向 A_N 为严格三角 weighted shift，V_N=I−zA_N。则

    det V_N=1,
    V_N⁻¹=Σ_{j=0}^{N−1}z^j A_N^j.

每个 N 的两项复形及其 external square 都可缩、同调维数全0。逆的 norm 及 N→∞ 的共同费用需另外核；det=1 不等于 uniformly cheap inverse。407 在完整 idele fibre 用迹类理论已付 invertibility，408 对指定 ℓ¹ 完成给 η(0) 控制；这些已有范围不可混为同一个全局目标拓扑。

结论仅是：在这些 idele fibres 内平方无法检测该已知非零 source relative object。绝不能反推源对象/相对范畴本身为零；真实 boundary category、relative K/regulator、全局 gluing 与 external C_Q action 仍是合法逃逸。

加入反向箭头已有407的 actual mixed trace

    C_q(x)=2Σ_{n≥1}η(qne^x)η(ne^x),

它保 q 且 x≥0 为正；Poisson端点给 μ_q≠0，须 L=D²+D 及双矩修正。辅助 Fredholm t 平面的零除子不是算术平方，C_q>0 也不是 full mixed Weil Gram。单向 det 的 acyclicity 与反向 mixed trace 的存在两者都须保留；本稿不重开其旧参数。

## 4. 原 du/Dlog 费用：source map 与 evaluation inverse 必须同域核算

固定 physical r=e^(u/2)f。原 physical du norm 是 ∫|r|²du=∫e^u|f|²du，不能用 ∫|f|²du 无费替代；fixed |u|≤L 只给有 e^L 费用的比较。原零延拓 Hlog 可取

    ||r||²_Hlog=(2π)^−1∫[1+log(2+|t|)]|rhat(t)|²dt.

对 finite window 和 finite local readouts，可给真正 matrix Gram。比如 ℓ_(α+iγ,j)(r)=∫u^j e^((α+iγ)u)r(u)du 的 du squared norm 为 ∫_(−L)^L u^(2j)e^(2αu)du；joint map 的费用由整个 Gram 最大特征值给出，不是把各对角界当精确费用。

553 已付：critical Hlog 费用 ≍_j L^(2j+1)/(1+log(2+|γ|))，每个先 fixed offcritical α≠0 的费用 ≍_(α,γ,j)L^(2j)e^(2|α|L)。这里没有新的谱坐标构造；只是原范数下的准入责任。

若局部值 y 要经 E:U→V 提升为截面，最小 Hilbert 费用为

    min_(Eu=y)||u||² = <y,(EE*)†y>,   y∈ran E.

这使用已指定的 section metric；还须比较该 metric 和原源 norm。一个 exact danger model 是 E_ε=[[1,0],[1,ε]]、y=(1,−1)，则最小 preimage=(1,−2/ε)，费用1+4/ε²。它证明 uniform right-inverse bound 可能失败，不能拿 det≠0 当有费闭合。

但这不是实际 source 的必要下界。若已有真实 bounded map A_L:r→u 且 y=E A_L r，则 E†E 是 orthogonal projection，最小提升费用≤||A_Lr||²；小 singular value 不额外强迫实际源费。只有已经证明实际 y_r 在危险方向、且所用原/截面 norm 正确，才可消费方向费用。完整截面库有其他好 minor 时，也不能固定坏 minor 制造假损失。全空间 worst-case lower 不能替 actual source cost。

405/519/553 的更早门仍须先过：任何原全线 du/Hlog 连续、消去全部 physical P_an、值于 Hausdorff正能量商的线性 map 必零；非线性 principal-coset 不变 map 也常值。故非根 r0 保留的实际 relative map 必须使用 Fréchet/有限窗/cofinal/domain变化或未闭正能量等合法前件，且列出其费用。只消单 p 不足，须消 τ_a r_p 全族；r0=(D²−1/4)ψ 保 Q_W(r0)>0 的537测试不能遗漏。

## 5. Continuous +/- controls：相同 restriction square 看不到 Weil sign

沿568的真正 positive g-integer 连续族，d=c−1/4，完整 Q 为

    R_d=C[z]/(z²+d), z†=−z,
    Q_d(A+Bz)=2|A|²+2d|B|².

d=±1/16 都有真二维 solution/jet carrier、Wronskian1、相同 finite capacity 与非零两点评价 E_1，det E_1=S_d(1)≥23/24。其 external square dimensions 都相同；若仅使用 det(E_1⊗E_1)=(det E_1)^4，更完全失去 sign。

保 actual involution/trace 时，tensor Hermitian matrix 为

    diag(4,4d,4d,4d²),

d>0 为正，d<0 有两个负方向。Sym² 仍留一个负方向；Λ² 的权为4d。若改用 Hilbert–Schmidt 正 metric，则换了要比较的 form，须重新证明同源 full Weil identity。该控制不否定带独立实极化或有效性的新 square；它精准排除“非零评价＋ordinary tensor counts自动给正性”。

d=0 时 trace nilradical 亦须保留：真实 full jet length2 与最小 trace quotient dimension1 不同，平方后把 faithful正metric强加所有nilpotent方向会额外排除已知正例。

## 6. Function-field controls：什么独立设施确实能够通过

真曲线 C/F_q 给真实 diagonal restriction H⁰(C,O(D))→H⁰(E,O(D)|E)、kernel H⁰(C,O(D−E))、局部 valuations、可乘截面；真实 S=C×C 又给 RR

    l(nD)+l(K−nD) ≥ χ(O_S)+(n²D²−nD·K)/2.

固定 ample fibre和primitive交数条件使正自交假设强迫两侧 n² 级截面；非零截面乘法把它们注入固定 H⁰(2K)，产生矛盾。这是567已恢复的同对象 Hodge-index 机制，包含 canonical线性项、H¹≥0、有效性与容量；非只写 dim U_n²。对应 Frobenius graph 的完整 mixed intersection 再识别为所有 n 的 point-count/full Weil Gram，而非只归一某一 scalar trace。

相反，568 的 q=5 真曲线与正整数Euler反模型都可造每个 finite B 的 étale local algebra、free jets、nonzero evaluation、raw Frobenius permutation及它们的外平方；原数据为

    true: N1..4=(9,27,108,675), b1..4=(9,9,33,162);
    false: N1..4=(1,11,76,451), b1..4=(1,5,25,110).

两者 primitive 二阶 Gram det 为11/5与−1。反模型通过 local/tensor facilities，不通过真 square 的同源 RR/Hodge。raw positive点集的大小或其平方随 B 成长，不能冒充固定 genus 的 primitive H¹ 容量；H⁰/H² pole subtraction正是未付 signed 运输之一。

## 7. Full classical Γ/prime powers/poles 的预算不能从复形形式推出

本次始终保留568的完整经典源

    Q_W(r)=2Re(M_+ conjugate(M_-))+Γ0||r||²
      +(1/2)∫_0∞ [2e^(−v/2)/(1−e^(−2v))]||τ_vr−r||²dv
      −2Σ_(p,k≥1)(log p)p^(−k/2)Re(r*r*)(klog p),
    Γ0=ψ(1/4)−logπ.

所有 proper powers、Γ finite-part/contact、双pole及全部 complex mixed terms保留。relative tensor、Euler类、局部 quotient 和单素数箭头没有自动给上述 identity。405 的 h 的 primitive Q 为0而两degree非零，单独 pole 与 arch−prime 分片分别为±1/8；matched cocycle/determinant line合法，但也必须独立说明预算片如何协同，不能各自无补偿下降。

552 已有具体真 arithmetic quadratic metric energy：−M_f²=||f′||²。它送405关系p到非零energy，且高频t时energy~t²而 actual Γ/full Q~log|t|，故并不支付本题比较。不能将一个已知正Hodge metric或 Hilbert tensor norm的存在当作新的 independent capacity。

## 8. 可消费结论与独立新输入清单

本次新增的是 exact finite-stage restriction-square/acyclicity/norm tests，用于选择实际候选；扣旧后没有新的 classic全源不等式、independent square capacity或whole/core净后果，不足开C036或新增数学轮。

下一次可晋级的独立输入至少须实际付下面一条，并接上其余已给设施，而非改名：

- 实际 adelic bimodule/correspondence composition及global gluing，在 Ξ-independent base 上给源map；通过全部405关系/537非根，列原norm与成长域。
- 同一对象的local restriction kernel、filtration与section multiplication，并独立产生 signed primitive D² 的RR二次系数；不能只平方旧曲线rank。
- 当前具体relative category中非零 regulator/index或effective-section量，能从 source relative object穿过 fibre acyclicity，在所需boundary上保留非根；普通source Euler类0不够。
- 由同一restriction/determinant capacity证明完整Γ/pp/pole mixed identity及全部error/coupling费用。若把身份加“预算非负”作为假设，则依然是Weil正性的等价充分包。

合法逃逸包括 noncommutative/relative/derived geometry、不同实际completion、Fréchet/cofinal原域、signed source-adapted families、真实全位cocycle及independent arithmetic surface。本文不以玩具finite complex或全空间norm下界排除这些类。

证据来源：405、407、408、519、552、553、567、568及本轮前一family报告。407–408 primary 的实际引用归原记录（CCM2007 v1 §§4/6/8、Connes1999、Simon）；本文没有另起paper链，也未宣称重读完整上游原证明。二次RR机制归567所核来源，有限复形/表格为本次直接精确推导。
