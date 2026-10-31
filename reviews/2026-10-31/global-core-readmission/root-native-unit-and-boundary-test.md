# 单一relative-K源公式：先核实际native单位lift

2026-10-31。G20261027/runtime1793085111、冻结0c4f。一个公式准入，不是C065续轮。当前草稿待独立稿、不同范围审查及root结算；不以文件存在代结论。

## 候选与原对象

物理源r=e^(u/2)f∈S_exp,C，采用原du、zero-extension Dlog。定义

    F_r(s)=∫_R e^((s−1/2)u)r(u)du=M_f(s).

519/520支付的是S_exp原拓扑中的实际源像／完整ζ-jets商及预解，不是O(C)/(Ξ)的任意无约束jet乘积。520§3还明确拒绝从谱识别推该全乘积拓扑。Root先前消息提出该识别，已在任何本门消费前由直接原件核读撤销；不能用整函数插值运输native源、范数或增长。

用405/519完整physical关系P_c，包括非compact Pan及两个degree，记

    A_nat=Cδ₀⊕S_exp,C   （卷积单位化）,
    B_nat=A_nat/P_c,   q:A_nat→B_nat.

P_c在中心Mellin侧恰消全部目标ζ重数jets与s=0,1两个degree，所以是闭卷积理想；没有把一般radical的只值条件替代完整jets。取候选

δ₀在此只记单位化的卷积单位，不是du里的物理源或可代入完整Weil型的测试函数；下文q_A和导数估计只作用于S_exp部分，绝不把δ₀的Dlog费用叫有限。

    r ↦ q(U_r),   U_r=exp_*(r),
    r ↦ ∂[q(U_r)]∈K₀(A_nat,P_c).

∂是ordinary relative K-theory连接方向K₁(B_nat)→K₀(A_nat,P_c)。它不是从K₀到K₁的逆，也不是HH₁/HP、hermitian K或metric regulator。用relative triple可直接表述为两个free A模和商上同构q(U_r)。当前尚无其它primitive载体。

最便宜负对照：先问q(U_r)是否已有实际native全局单位lift。若有，ordinary connecting class就是0，全405关系虽消去，同一537正Weil非根也被杀；没有必要继续RR/sections或给它一个正metric。

## Native卷积指数存在，且本来就是全局lift

对A≥0，q_A(g)=∫e^(A|u|)|g(u)|du满足q_A(g*h)≤q_A(g)q_A(h)。这些量与全部导数的q_A(D^kg)共同给S_exp等价Fréchet拓扑；加一阶导数的weighted W^(1,1)估计控制相应上确界半范数，反向多取一个指数权控制积分。

在该原拓扑中

    U_r=δ₀+g_r,   g_r=Σ_(n≥1) r^(*n)/n!

实际收敛。对每个A、k，导数可放在同一个卷积因子，故

    q_A(D^k(r^(*n)))≤q_A(D^kr)q_A(r)^(n−1),
    q_A(g_r)≤e^(q_A(r))−1,
    q_A(D^kg_r)≤q_A(D^kr)(e^(q_A(r))−1)/q_A(r).

比值在q_A(r)=0按连续值1解释（此时r=0）。这没有把强导数费用换成du或Dlog。绝对收敛允许同一weighted卷积代数内相乘，binomial恒等式给U_r*U_(−r)=δ₀；r↦U_r连续，t↦U_(tr)还是一个从δ₀出发的实际单位路径。

中心Mellin字符在每个fixed s连续，且卷积乘法合法，故F_(g_r)=exp(F_r)−1。δ₀的字符是1，因此U_r的Mellin单位确为exp(F_r)。这不是先在更大O(C)证明后反向假设native lift存在。

于是q(U_r)已有单位lift U_r∈A_nat^×。ordinary relative triple通过该free A模自同构即与identity triple同构，故

    ∂[q(U_r)]=0  对全部r∈S_exp,C。

也可直接由ordinary K exactness得到；不需给nonunital ideal的naive Hochschild复形套excision。该结论不要求任何全部native quotient units的log或lifting定理。

不以连续单位路径判定algebraic K₁类本身为零；这里判零的仅是其ordinary connecting image，依据是实际单位lift或relative triple同构。

对P∈P_c，q(P)=0，故q(U_(r+P))=q(U_r)：完整Pan消去确实通过。但同一映射对537源r₀=(D²−1/4)ψ也为0，尽管该旧fixed17/16双矩零源有Qζ(r₀)>0。这里的失败是进入ordinary连接类后全部coverage消失，不是说Mellin谱商本身为零。

## 原费用、标准旧角色和合法范围

若先fixed supp r⊂[−L,L]，

    q_A(r)≤√(2L)e^(AL)||r||du
          ≤√(2L/log2)e^(AL)||r||Dlog.

所以选定native代表的zeroth weighted L1费用可付e^(√(2L)e^(AL)||r||du)−1；全部k阶代表仍需q_A(D^kr)。这只是代表的充分费用，不是K零类的必要下界（零类本可取identity代表），更不是成长窗统一界或算术height。没有从范数合法性取得mixed RR。

此公式只把来源原件中的global lift改写成K边界语言。574/575已付实际source exponential/clutch若是side unit就coboundary并杀537；519/520已有完整Mellin quotient但不授正性。这里的标准卷积指数与relative exactness没有增加独立principal、有效整截面、容量或危险signed core估计。应按标准强旧0扣除，不把一个显式新写的组合计为新研究定理。

额外ambient可另定义A_ent=O(C)、H=s(s−1)ξ(s)/2、B_ent=A_ent/(H)。H来自实际Pan的中心Mellin；普通entire Hermite插值若被采用，只属于这个**额外放大**的对象。即使在该ambient证明所有有限矩阵单位都lift，也不能升级成全部native B_nat units、native强增长/原norm、hermitian或metric版本。当前首检完全不依赖这项更强ambient主张。

停止的是本单一exp源→ordinary连接类recipe。没有证明整个relative K₀为0，没有排除非free/非connecting类、非liftable native quotient单位、graded/derived/hermitian或secondary/metric regulator。更没有把它们仅因未排而准为新合同。任何这种后继须有实际源对象、原费、405/537及扣强旧净后果；不能只把“需要非liftable”改名为输入。

完整经典Q的Γ/contact、全部p^k、双pole与allcomplex测试均未改动；此门不提供Q的新符号。原whole leading4/5负惯性UPPER、principal/sections/mixed、signed core/cross、成长Ξ均未变。Root实际消费待当前两审稿，原cadence与文献manifest原字节保持，不预准C066/603或Goal完成。
