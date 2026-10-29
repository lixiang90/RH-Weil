# Formal Mellin 准入：实际成员性、有限 jet 断点与全商的有理秩读出

2026-10-29；G20261027/runtime1793085111、冻结0c4f。本稿是AB/STATE唯一必要首检的domain分工，供root实际消费。只写本文件，不改STATE、cadence、Goal、Git或文献库；不建C060/597，不改点/frame/degree，不读Osipov §3/4、Example2.3或新的来源。本稿不预定数学计数；root须扣最强旧并和Pan原稿对齐后统一结算。

**结论。** 固定源公式可形成真实formal无穷元素；但只看一个无穷分支的任意有限jet，不能直接给全商Φ的非平凡读出。可以直接从已核定义(6)–(8)建立一个不同的、作用于完整系数尾的**代数读出**：将所选有理无穷分支的非负Laurent系数序列，模掉“系数值的Q-span有限维”的序列。01/02两个实际boundary subgroup均被该读出杀掉，因此它真正下降到Φ，不经过G2、不假设period lattice，不用A01∩A02等于generic rational sections。405明确Pan源的even Mellin系数给无限Q秩，遂在实际Φ中非零，所提源公式不能消405关系。

## 1. 恢复与实际读取范围

实际读goals/README、STATE，运行research_state.py check后show，读同一Goal的完成门、已完成C059、D20261029AB、宏观入口及next-formal-mellin-source-admission.md。恢复到当前实际源公式的必要检验，不复用C059预算。Root的运行Goal观测为同实例active；本分工没有创建/修改Goal。

实际读405§2–3/§4–5，519§1及§3–4，520§1，上一轮source-gate-location-and-domain-audit.md的真实域/quotient段和必要原定义。为区分hat与非hat tensor，沿PDF skill read-only流程目视原PDF6缓存：原(6)的无穷ambient是completed tensor，而(8)的generic subgroup明确是普通tensor。没有把额外原proof或Example作为前件。这里只用已核定义(6)–(8)及P¹的有理局部坐标，不需要作者主Theorem2.1的exact-sequence proof或§4 H¹/protorus定理。

Parent提出了有限Q-span必要criterion；本分工独立核实际两个subgroup的投影、frame和tensor含义，并将其重写成全商上的读出。另与Pan分工核物理半密度/Mellin点对应；以下Pan系数也从405(7)/(11)及Euler even-value公式独立重算。消息不是原稿消费，root仍须读该分工的冻结原稿。

## 2. 固定对象和成员性

固定

    X=P¹_Z，C=∞，U=A¹_Z，F=ω_(X/Z)≃O(−2)，
    z为U坐标，t=1/z，e∞=dt，dz=−t^(−2)dt。

无穷曲线C的generic residue field为Q，故

    K_C(F)=Q((t))dt，  Fhat_C=Q[[t]]dt。

这是真正定义在Q上的frame，不是按源选择的real formal frame。记

    A=A_X(F)，V∞=A_(X_Q)(F_Q) completed-tensor_Q R，
    A^ar=A⊕V∞，
    B01=A_X,01^ar(F)， B02=A_X,02^ar(F)，
    Φ=A^ar/(B01+B02)。

已核原(6)把V∞识别为各horizontal curve的completed local factors组成的restricted product；C∞的factor为R((t))dt，integral lattice为R[[t]]dt。对real physical r∈S_exp，定义

    M_r(s)=∫_R r(u)e^((s−1/2)u)du，
    a_r(t)=Σ_(j≥0) M_r(j+2)t^j dt。

每个积分绝对收敛：取N>j+3/2，|r(u)|≤p_(N,0)(r)e^(−N|u|)即可；无需统一于所有j的单一指数半范数。正幂formal序列没有解析收敛要求，也没有无限负幂。

令v_r在C∞ factor为a_r、其余horizontal arch factors为0。它属于上述restricted product：每个分量均在相应integral lattice，且除一个分量外全零。等价地，有限多项式截断a_(r,N)给原adelic space algebraic-tensor-R中的元素；对固定有限jet，截断在N充分大后完全相同，故在formal completion中定义a_r。该成员性使用ambient的hat tensor，不能据此把B02中的普通tensor也换为completed tensor。

于是J(r)=[(0,v_r)]∈Φ是合法的additive源公式。它对raw无穷空间是R-linear；Φ本身尚未赋予R或C-vector-space结构，不把J称为complex linear feature map。每一moment的连续性也不支付原du/Dlog到任何Hilbert范数的uniform费用。

## 3. 有限jet为什么不能直接下降

对任意N与任意b_0,…,b_N∈R，取generic rational differential的实线性组合

    g=Σ_(j=0)^N b_j t^jdt ∈ F_η tensor_Q R。

原(8)把它按generic diagonal映入所有arch local factors，并给actual boundary (0,g_diag)∈B02。它在C∞的前N+1个系数恰为任意向量b。

因此，若一个对Φ的读出只依赖C∞的一个有限jet、忽略其它arch/finite legs，则它必须杀掉每个b，因而只能是零。特别，bare coefficient mod Z或mod任何预先选的小period lattice，不自动在Φ上下降。

此论证**不说**仅C∞ branch非零的truncated v_(r,N)本身属于boundary。Generic differential同时有其它arch分支的展开，不能删去它们。它只排除一种不合法的有限jet读出；完整商上的其它读出仍可能存在。也不能由此把Φ等同主Theorem2.1的终端商G2。

## 4. 直接下降到Φ的完整尾读出

令S=R^(N_0)为所有real序列的空间，定义

    B_fin={ (a_j)_(j≥0) : dim_Q span_Q{a_j:j≥0}<∞ }。

这里N_0是非负整数指标集，不表示finite-support direct sum。B_fin是R-linear algebraic subspace：有限和的系数值落入两个有限Q-span之和，实倍λ的系数值落入λV，Q-dimension仍有限。它也恰是有限和Σ_(k=1)^m λ_k q^(k)，其中λ_k∈R、q^(k)∈Q^(N_0)。不要求m有任何统一上界。

用固定C∞ factor及frame dt提取非负系数，得到additive map

    c∞⁺:A^ar → S。

它忽略所有finite adeles及其它horizontal arch factors。两个boundary分别满足：

1. 对B01，原(7)的C∞ arch component来自K_C(F)=Q((t))dt本身，而不是其任意real completion；所有系数为Q，故c∞⁺(B01)⊂Q^(N_0)⊂B_fin。
2. 对B02，finite summand投影为0；其arch generic component来自**普通**F_η tensor_Q R。任一元素是有限和Σ_(k=1)^m λ_k f_k(z)dz，f_k∈Q(z)。在t处，f_k(1/t)(−t^(−2))是Q-rational function，Laurent展开所有系数均为Q：把它写为t^(−n)P(t)/Q(t)，Q(0)≠0，再用有理系数递推展开即可。因此所有系数值落入span_Q{λ_1,…,λ_m}，故c∞⁺(B02)⊂B_fin。

结论不是对whole boundary的finite腿做了不合法循环，而是每一个boundary subgroup的原始定义都已足以给

    c∞⁺(B01+B02)⊂B_fin。

所以真正存在well-defined additive homomorphism

    rho∞: Φ → S/B_fin，
    rho∞([(a,v)])=[c∞⁺(v)]。                              (R)

尤其

    rho∞(J(r))=[(M_r(j+2))_(j≥0)]。                       (M)

如果该完整序列含有无限多个Q-linearly independent的值，则rho∞(J(r))≠0，故J(r)≠0于**实际全商Φ**。此推理完全不需要：Φ=G2；A_C tensor_R；未核natural Phi→G2如何作用于纯arch输入；period lattice；A01∩A02=F_η；未付reciprocity或作者§3/4 proof。Finite legs已经正确保留，因为rho∞直接杀B01和B02而不是先删finite腿。

## 5. 对405实际Pan关系的应用

405给实际raw源h=Eη，其完整Mellin为

    M_h(s)=s(s−1)Λ_Q(s)/4=ξ_Riemann(s)/2，
    p_raw=(D²+D)h ∈P_an，d(p_raw)=c(p_raw)=0。

它是实际Schwartz adele限制像，不是按目标配对反向命名的关系。置physical P(u)=e^(u/2)p_raw(u)，则P仍属real S_exp且

    M_P(s)=M_(p_raw)(s)
          =s²(s−1)² π^(−s/2)Γ(s/2)ζ(s)/4。               (P)

这一步保原半密度，不能把raw和physical Mellin点错移。对m≥1，取本固定公式已有的指标j=2m−2，Euler even-value恒等式给

    M_P(2m)=q_m π^m，
    q_m=(-1)^(m+1)B_(2m) 2^(2m−3)
           (2m)²(2m−1)²(m−1)!/(2m)! ∈Q_(>0)。            (E)

前几项为π/6、(2/5)π²、(10/21)π³，与405的M_(p_raw)(2)=π/6一致。Euler公式与π的transcendence为标准独立数学输入，不使用未知ζ零点位置；本稿不重证这些经典定理。

若(E)的无限子列有非平凡有限Q线性关系，除去非零rational q_m就给π满足非零Q多项式，矛盾。因此(M)的系数序列Q-span无限，得到

    rho∞(J(P))≠0，因而J(P)≠0∈Φ。                         (F)

对每个λ∈R\{0}，乘λ是R作为Q-vector space的可逆Q-linear map，故λ倍该序列仍无限Q秩；于是所有J(λP)都非零。这里只使用固定b=0的实际Pan关系及其实数缩放，不声称任意平移后的πe^(2b)仍transcendental，也不需要此更强量词。Full-Pan下降已经被一个实际关系否定。

因此这份明确源公式虽是合法raw编码，却不满足主线要求的“405实际关系成为boundary”。无需继续用537测试才判它的principal准入失败；537及allcomplex目标保持原范围，未被删掉。

## 6. 最强同链修补边界

定义actual arithmetic adeles中的detector kernel class

    K_det={d∈A^ar : c∞⁺(d)∈B_fin}。

它包含全部boundary，并允许：任意finite腿；任意其它arch分支；在C∞加任意formal序列，只要该序列的系数值Q-span逐元素有限。这里不要求uniform rank、uniform norm或统一有限标量基。

对任意规则r↦d_r∈K_det，不论它是否linear、是否依源适应、是否另有auxiliary参数，都有

    rho∞(J(r)+[d_r])=rho∞(J(r))。

所以固定Pan P及所有非零real倍在这些修补后仍非零。特别，给finite places添加任意source-dependent corrections也不能修复这一失败。此为同一读出的直接最强消费，不是额外研究轮或“所有非局部/源适应修补失败”的结论。

允许的逃逸必须保持准确：在C∞本身引入具有无限Q秩的不同系数并抵消读出、改变源编码、改变boundary/完成化/分离商或其它primitive，是不同对象/机制，未被本稿否定。No point/frame/degree/weight tuning is authorized by this result.

## 7. 拓扑、最强旧与净后果的边界

B_fin包含所有finite-support real序列，因此在product topology中稠密；S/B_fin的自然quotient topology非Hausdorff。rho∞是一个代数读出，**不是**到separated normed/positive/Hilbert空间的continuous capacity。它不付distance、du/Dlog界、正极化、惯性、mixed RR或完整Γ/pp/pole身份。ρ∞(J(P))≠0足以否定当前**exact algebraic quotient**中的Pan消去，却不自动推广到任何closure/completed/Hausdorff variant。

每个finite truncation的系数序列在B_fin中，所以本readout看不见它们；不能把“各finite段不可见”换成完整formal尾不可见，也不能把ρ∞(truncation)=0换成truncation本身为boundary。这个limit-sensitive区别不需要新增源参数。

519/520已经指出真实Pan是完整零点jets关系，并给off-zero Mellin评价的障碍。它们及405的M_p(2)≠0先作强旧对照：**单一off-zero值非零本身不能证明actual Φ-class非零**，因为§3已证bare finitejet不下降。这里额外闭合的是原boundary定义上的finite-Q-span读出，再用405/Euler/π将同一旧关系运输到actual Φ。是否把这份完整实际候选失败计作新数学或标准旧直接准入，须由root在消费两个原稿、不同fresh及最强旧后统一决定；本分工不按文件/lemma数计轮。

实际长期瓶颈不因这种反测消失：它不提供新的正principal/Green桥、整sections/mixed容量或危险core/cross/成长Ξ输入。596和最强whole542+555→557 leading4/5负惯性UPPER保持。当前source pair应停止principal准入，不继续调Mellin点/frame/field/degree，也不读作者未准proof；不据此完成长期Goal或排除全部二维adelic方法。

## 8. 输入身份与终态

本稿只写此owned路径。以下指纹是实际当前原字节的身份绑定，不代证明；STATE为root可变执行记录不绑定为数学输入。Source PDF仅用既付§2定义/原PDF6目视，未消费新章节或Example。

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
| literature/local/2026-10-29-core-input-choice/osipov-1801.02282v2.pdf | 267569 | `8491958ec6ff552aa1d3915ecb7f29a8a1bed4069292acac76a3b79c7b8100cc` |

本分工终态：没有STATE/cadence/Goal/Git/库修改，没有web/query/download、数值或后台进程，没有自动后继。冻结后交root按实际原稿消费；原稿存在/终态消息不代root结算。
