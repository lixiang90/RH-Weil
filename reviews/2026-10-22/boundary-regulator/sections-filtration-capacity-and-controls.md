# Boundary regulator 到算术截面：连接障碍、局部过滤与真实容量的控制

2026-10-22。独占子稿，仅审本轮指定的 sections/filtration/capacity 箭头；不改 STATE、Goal、cadence 或 Git。
恢复同 G20261014/0c4f 冻结基线，C035 已完成，最新 D20261022C。以下是旧设施的具体检验和标准正控制，
不是新 classic 正性定理，也不是对所有 relative regulator 的不可能性证明。

## 1. 本门结论与最强旧扣除

**非零 boundary 类并不自动给一个全局截面。** 在真正曲线上，连接映射通常首先给“不能拼成截面”的障碍；
障碍消失后，截面 lift 仍是一个全局截面空间的 torsor。实际整性、局部消失过滤和原 metric 必须随该 lift 一起构造。
determinant line 可以在完整算术 RR 中记录真实容量，但单独一个 line、其 trivialization 或一串 valuations 不会生成这些对象。

405/519 已给 actual E、全 Pan、两 degree；537 给真实非根；553 已给全线原 du/Dlog 上消全部关系的连续读出退化；
上轮已给 source-defined 相对 DGA 及全 Pan 零同伦，并明确其 quasiiso 仍是旧解析商。
本稿不把这些重复记成新输入，也不由“所有同调读出都会经过该商”推断 regulator 不可能有新算术内容：
**新的内容可以是独立定义的目标整格、局部过滤、有效性、metric 和 RR 比较，纵使其底层向量空间读出经过同一个商。**

最强实际 ζ 后果仍为 542+555→557 的 whole leading 4/5 负惯性上预算；这里没有改善该预算、危险 core、coupling 或 Ξ。

## 2. Actual DGA 的真实准入，不可只消一个 p

记物理源 F_c=e^(u/2)S_exp,C，S 为 η(0)=∫η=0 的偶 Schwartz 源，

    E_cη(u)=e^(u/2) 2Σ_(n≥1)η(ne^u),
    μ±(r)=∫ e^(±u/2)r(u)du,
    C=[S --∂--> F_c⊕C²],
    ∂η=(E_cη,−μ+(E_cη),−μ−(E_cη)).

源 map 为 j₀(r)=(r,0,0)。上轮 explicit degree cocycle 给真正非 unital DGA；其 H⁰ 为 F_c/(C P_an)。
每个 q=Eη_q∈P_an 有实际源 homotopy K_q(g,a,b)=U_gη_q，

    U_rη(x)=∫e^(−t/2)r(t)η(e^(−t)x)dt,
    T_(Cq)=∂K_q+K_q∂.

所以 regulator 若为 homotopy-invariant 的 chain/category readout，就必须说明实际消去这个完整族；
只使所选 p=(D²+D)h 或其一个 minor 为零不够，所有其平移/缩放也必须相容。
若只在紧支 C_c∞ 源上定义 map，P_an∩C_c∞=0，关系测试在该域是空条件；
须再给扩张到 F_c，或兼容 crop/尾误差与真正 cofinal 极限。

537 的 r₀=(D²−1/4)ψ、0≠ψ∈C_c∞((-17/16,17/16)) 满足 μ±=0、Q_W(r₀)>0。
目标必须能保留 j(r₀) 的 primitive 信息，不能只读 μ±。
405 的 h=Eη_h 有两 degree (1/4,1/4)，Q_W(Ch)=0；因此保双 degree 与正 primitive 能量是不同责任。
裸 H⁰(F_c/E_cS) 会丢 h；给 h 任意忠实正能量则又换了 Q。

## 3. 真曲线上的 boundary-to-sections 正控制

取光滑 proper 曲线 C/k，函数域 K，各闭点的完备局部域 K_x、整数环 O_x。对 divisor D，置

    O(D)_x=t_x^(−D_x) O_x,
    A(D)=∏_x O(D)_x ⊂ A_C.

曲线的 adelic 复形是 [K⊕A(D)→A_C]，差为 (f,a)↦f−a；其 kernel 是 L(D)，
余核是 H¹(C,O(D))。这里局部 valuation、principal functions 和加法拼接来自真正曲线，并非从某个待证 trace 反定义。
由 sheaf 的局部整性可直接核 kernel：全局 rational f 同时满足所有 ord_x(f)+D_x≥0，才是同一线丛的截面。
乘法 L(D)·L(D′)⊂L(D+D′) 也由这些不等式逐点相加而来。

本次仅定点核 [Stacks Project, 53.5 / tag 0B5B](https://stacks.math.columbia.edu/tag/0B5B)：
其 proper 曲线 RR 给 χ(E)=deg(E)+rank(E)χ(O_C)，Gorenstein 时给 canonical/duality 形式。
这确有有限 cohomology 容量，但曲线线性 RR 尚不是 C×C 的 signed 二次 RR；后者沿 567 既有来源消费。
此处不另串原件。下面 P¹ 的连接映射由写出的短正合列直接计算，非借该网页假设新的比较定理。

令 E 有效，真实 restriction 序列为

    0→O(D−E)→O(D)→O(D)|_E→0.

从而有

    0→L(D−E)→L(D)→J_(D,E) --δ--> H¹(O(D−E))→H¹(O(D))→0.

给局部 jets y，存在 global section lift 当且仅当 δ(y)=0；若存在，所有 lift 构成 L(D−E) 的 affine torsor。
因此“boundary regulator 非零”与“获得 section”不能直接同义化。它可能先证明了目标局部数据有障碍。

一个完全计算的例子：C=P¹_k，E={∞}，取

    0→O(−2)→O(−1)→O(−1)|_∞→0.

H⁰O(−2)=H⁰O(−1)=H¹O(−1)=0，而 H¹O(−2)=k；故 δ:k→k 为同构。
非零 boundary jet 确实存在并被 global cohomology 保留，却没有任何 O(−1) 全局截面 lift。
相反 D=n∞、n≥0 时，多项式给许多可 lift 的局部数据；其可解域、kernel、metric 仍须分别给。
各 affine chart 的高阶 cohomology 为零而 global H¹ 可非零，说明 gluing 能恢复被局部 cohomology 漏掉的量；
**这不是 407 中“整个 fibre 对象可缩”的同一命题，不能拿此例直接证明 actual idele boundary 已穿过 acyclicity。**

函数域需要的实际新比较应当将 DGA 类送入这个形态的具体 local data/gluing，并证明相应 δ 消障碍、
同时保住 r₀，再控制一个 actual lift。写出一个目标 H¹ 或一个抽象 connecting morphism，还没有付该箭头。

## 4. 整格、局部过滤、det line：可以同源，但不可互相代定义

真实 P¹_Z 给独立于 Ξ 的正控制。令

    L_n=H⁰(P¹_Z,O(n))=Z[X,Y]_n,   n≥0.

在 z=X/Y 的 0 点，整数多项式系数的 (m,k)-jet restriction（m≤n+1）为

    ev_(m,k): L_n→(Z/p^k)^m,
    Σa_jz^j↦(a₀,…,a_(m−1)) mod p^k.

它是满射，kernel 为 a₀,…,a_(m−1) 全被 p^k 整除的真实 sublattice。
固定 degree 截面中，局部 module ideal (p^k,z^m) 描述该 kernel；乘法过滤则可用

    F_n^(a,m)=p^a z^m Z[z]_(≤n−m),
    F_n^(a,m)·F_(n′)^(b,l) ⊂ F_(n+n′)^(a+b,m+l).

这保留 vertical p-adic 与 horizontal vanishing 两个指数，不错误地把矩形 ideal 的乘积说成 I_(k+k′,m+m′)。
上轮 toric norm 的独立算术容量也在同一 L_n 中成立：固定 a>0，

    ||P||sup=sup_z |P(z)|/max(1,|z|)^n,
    # {P∈L_n: ||P||sup≤e^(an)}

介于两个系数立方盒，故 log#=a n(n+1)+O_a(n log n)。
所以 real filtered sections、非零评价、finite 整性和 n² 容量都存在；缺的是实际 r→该对象的相容比较。
不能将 arch twist a 按 Q_W(r) 选取后宣布容量差已识别为 Weil 型。

det line 本身也不是一个 section functor。对满秩 lattice map E，det E 记录总 p-adic length，
却不保完整 local module：k≥2 时 diag(p^k,1) 与 diag(p^(k−1),p) 的 determinant 同为 p^k，
但 cokernel 分别为 Z/p^k 与 Z/p^(k−1)⊕Z/p，局部 elementary divisors 不同。
因此只有 boundary determinant valuation，而没有实际 module/source map，不能反推出每个局部消失方向或 actual source lift。

这不排 det line 在已有 integral perfect complex、所有局部 lattice、arch metric 及 RR 定理中计算 Euler 容量。
它排除的是由一个现成 analytic determinant/cocycle，跳过这些输入后“自然”得到同一算术截面库的推理。
若 actual regulator 给的是 K₁/K₀ 类或 metrized line，下一步须注明其如何得到 L_n、ev、F 与乘法，而非只把它们命名出来。

甚至可以在同一正控制中直接看到 determinant 的真实二次量：给 L_n⊗R 的 monomial basis 以
各向量长度 e^(−an) 的 orthogonal coefficient metric，则 det L_n 的标准 wedge 长度为
e^(−an(n+1))，其 Arakelov degree 恰为 a n(n+1)。这里 n² 来自**已给的真实 rank n+1**与每个方向的实际 arch twist an；
toric sup 与 coefficient norms 的比较只改 O(n log n) 容量误差。
所以“det line 从来不能出现二次项”也是错误结论。缺口是从 actual r 的 boundary 类得到上述 integral section family、
其 rank/metric/局部过滤以及 primitive 方向的同源比较，不能只要求一个 abstract line 拥有所需 degree。

## 5. 从 complex 源到离散 orders 的连续性：限定障碍及合法逃逸

若 V 为连通的 complex/real topological vector space，Λ 是固定离散格，任何连续 V→Λ map 都常值。
尤其 additive map 若同时连续且在 r=0 为零，就只能为零。此项只适用于 literal fixed lattice/固定离散拓扑。
它不能排除：

- 先把 arithmetic cycle/section module 建好，再对 coefficients 作 complex 线性扩张；
- source-dependent family、Picard/Deligne 连续部分、R-divisors 或 signed cycles；
- valuation chamber 内 orders 恒定，但参数穿过真实 degeneracy locus 时跳跃；
- Fréchet/cofinal/变域且逐层付费用的比较。

这些逃逸必须保留原 finite integer order 的来源。复杂系数扩张后，一般 complex cycle 没有 literal integral effective order；
Weil 证明中是先在真实 integral/rational 对应上用有效性/RR，再以 polarization/连续性扩成全 complex Gram。
若主关系也先 complexified，目标等价关系必须同步扩张，不能同时要求 arbitrary complex r 对应一个单独整数 divisor。
若只给 rational/dense 子族，则还须 denominator、height 与极限误差，稠密性本身不给全源 signed 比较。

乘性/指数 regulator 并不会免费避开这份责任。例如实际构造了某个 finite matrix readout A(r) 后，
exp(tA(r)) 是 GL_N(C[[t]]) 的 unit，det exp(tA(r))=exp(t Tr A(r))，t-adic order 恒零。
其 log|det| 是 arch real quantity，不能由此读出非零 finite 消失阶。
若改用 meromorphic matrix family 得到 det 的真实零阶，则所需 family、degeneracy locus、整性与全关系相容是额外构造；
若直接采用 Ξ 零点定义该 locus，又回旧谱商包装。
这只是 unit-valued exponential 这个具体候选的测试，不排一般 noncommutative/secondary regulator。

## 6. 原 du/Dlog 与 actual lift 费用

553 的强旧结论覆盖任何全线原 du/Dlog 连续、消所有 physical Pan 且值于 Hausdorff target 的 class map：
线性 map 必零；若 nonlinear 且对所有 Pan coset 不变，也常值。
这里应扣旧，而不能再称一个新 regulator obstruction。它不适用于未证 class-invariance 的 raw map，亦不排 Fréchet/变域。

固定窗 |u|≤L 上，actual action 的旧费用为

    ||r*·||_(du→du), ||r*·||_(Dlog→Dlog) ≤ ||r||₁ ≤ √(2L)||r||du,
    ||μ±||_(du-dual)=√(2sinh L),
    q_(a,b)(U_rη) ≤ q_(a,b)(η) [sinh(2κL)/κ]^(1/2)||r||du,
    κ=a−b−1/2.

Dlog 取 log(2+|t|) 版本时，右边可除 √log2。源半范数各有不同 κ，不能收成一个全线 scalar 原范数界。
后续 actual regulator/sections map A_L 的原费用仍未由这些 action bounds 自动给出。

若实际 local value y_r=E A_Lr，已知 A_L 的同 metric bound 时，最小 section lift 范数≤||A_Lr||。
不能用 E 在整个 target 上坏 singular value 的 reciprocal 当 actual source 的必要费用；
同样不能只固定坏 minor 而忽略同一完整 section 库的好 minor。
需核的是每个已定义 source/domain 的 y_r 方向、section metric 与原 du/Dlog 的直接运输，以及 L→∞ 的全部费用。

## 7. 一个更贴近 boundary 的连续正反控制

旧连续正反族保 d=±1/16，R_d=C[z]/(z²+d)，z†=−z。它不只是有相同维数：
有完全显式的 polynomial boundary resolution

    [C[z] --(z²+d)--> C[z]],

在开集 z²+d≠0 上实际可缩，余核是有限 boundary module R_d；两者 divisor 都有效、length=2、局部 multiplicity=1。
因此“在 open part acyclic、boundary 有非零 module、det divisor 有正 local orders”这三项可以同时成立于正反例。
它不是 actual adele 407 的实现，也不是经典候选；其作用是控制这三项本身是否足够给 Weil 符号。

保相同 involution 和 regular trace，

    Q_d(A+Bz)=Tr_reg((A+Bz)(A+Bz)†)=2|A|²+2d|B|².

d>0 正，d<0 有负方向。换一个 positive Hilbert metric 可使目标正，但必须重新证明它是同一完整 Weil 型。
把任意 effective boundary divisor 的次数或其平方称为 primitive RR，也不能区别这对控制。
函数域成功所额外用的是 C×C 上真正 signed correspondence、自交、effective-section 乘法与同对象 RR/Hodge，
然后与所有 Frobenius periods、H⁰/H² pole 项识别；不是 local determinant order 的单独非负性。

## 8. 完整 Weil 项与本门未付输入

全程保 568 的物理规范（r*=overline(r(−u))）

    Q_W(r)=2Re(μ+(r)overline(μ−(r)))+[ψ(1/4)−logπ]||r||du²
      +(1/2)∫₀∞ [2e^(−v/2)/(1−e^(−2v))]||τ_vr−r||du²dv
      −2Σ_(p,k≥1)(log p)p^(−k/2)Re(r*r*)(klog p).

没有删 Γ finite-part/contact、proper powers 或两个 pole，也没有因 r₀ 的双矩为零就更改全源定义。
目前 boundary-to-sections 箭头尚未证明：

1. actual DGA/relative prime object 的具体 boundary class，在所选真实算术 target 上非零并保 r₀，同时消全 Pan；
2. 该类给 local jets 后确实消连接障碍，并有相容 global lift/全源 family、真实整性与局部乘法过滤；
3. 对同一 lift/source，原 du/Dlog 与 arch metric 的 fixed/cofinal 运输有完整费用；
4. 同一 square 的 independent signed RR 系数及容量差，逐项等于 Γ、所有 p^k 与 pole/mixed 项，含全部误差。

第4项若只是定义“容量差:=Q_W，并假定正”，仍是 Weil 正性等价/充分包。
曲线正控制证明了这些设施有真实、可计算的形态；它没有把 actual classic 源接到它们。
本分支的结果是缩清 regulator 到 sections 之间的具体两层责任（gluing 障碍与 integral/metric lift），
并给实际正反测试；没有新的独立 classic 容量输入，不足晋级新数学合同。
在此停止，不继续换 det line 名称或加指数参数。可改变选择的证据必须是上面1–3中的 actual map/非零计算，
或第4中的同源新比较；它们一旦出现，应重新检验而非援引本稿作一般排除。
