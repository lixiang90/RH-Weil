# 单一 SU₂ 张量候选：最强旧与目标谱角色准入

2026-10-31；独立支持 `/root/su2_strong_old_admission`。同 G20261027、冻结 0c4f 与 runtime1793085111；仅本稿，未改 Goal、STATE、唯一 cadence、文献库或 Git。本稿是有限来源准入的独立角色比较，不是新数学合同，不替 root 消费或独立原文核查。

**结论：真实全阶对称幂自守性可以支付这一个非 CM 模形式的局部 tensor L 函数族及条件极点上界；它不自行支付经典 ζ 全局零点的 Deligne 放大。** 这不是旧 C₂ 有限因子重复定理的直接实例：此处确有越来越多的新 cuspidal 因子。准入停止依据是原 002／073／567 已付的局部参数与目标全局谱角色区别，而不是否认新来源或仅凭 Γ 费用宣布方法不可能。

## 输入、便宜测试与净后果

1. 输入是固定 level1 非 CM holomorphic form Δ 所给的正规化二维局部对象 V；det V=1。Root 报告已核 Newton–Thorne 1912.11261v3 引言的局部 functoriality 定义与 Theorem A：regular algebraic、cuspidal、level1 的 GL₂ 对每个 ν≥2 有 cuspidal GLν 的 Sym^(ν−1) lift。作者证明与本文其余章节不由本稿消费。
2. 最便宜测试是先对每个有限 n 完整分解 V^(⊗2n)，再问对应 L 函数中的 ζ 因子究竟移动零点、增加零点重数，还是给目标零点所对应的算子取幂。不得仅因“非平凡 tensor＋全阶极点”两个标签就认定通过。
3. 若得到目标全局谱的独立全阶控制，或某个完整 tensor L 函数的独立零点线／正型并有忠实因子传递，才可能改变经典 RH 责任。实际所见只有局部 tensor 和自守性；标准因子身份继承目标零点，但不定位它们。扣旧后无新经典全源、成长 core／coupling 或 whole4/5 后果。

## 1. 精确对象、量词和来源等级

这里 V 是同一个模形式在各素数的二维局部 Langlands／Galois 数据。有限素数的正规化 Satake 特征值记 α_p、β_p，满足 α_pβ_p=1，幂迹 α_p^k+β_p^k 为实数。若使用 SU₂ 术语，已纯化情形有 β_p=conj(α_p)、|α_p|=1；以下有限表示恒等式也可在 det1 的代数表示环中使用，不应把“SU₂”这个名称本身当成局部纯性的独立证明。

V 在此是局部／unitary 正规化的记号，不无声声称一个半 Tate twist 的实际全局 motive。Δ 的未正规化对象 M 权为11；若另引用其标准 motive／Galois realization，偶 tensor 的 weight0 正规化可写成 M^(⊗2n)(11n)，只用整数 Tate twist。本文本身仅用实际自守局部参数及有限表示恒等式，不把这个可用解释当成已审的新全局零点 realization。

每个 n≥1 单独给一个维数 4^n 的对象，允许 n 无界，但先固定 n 再定义 Euler 乘积和延拓。Theorem A 的“对每个阶存在”不含自动可消费的 n 一致解析范数、零点位置或 Γ 误差估计。本文也不取无限 tensor、无限 direct sum 或未经证明的极限。

原文 statement 由 root 的独立来源腿核实并经任务消息传入。本稿未打开、抽取或视觉读取新 PDF，因而不将该消息升级为本人的 primary-source 审核。以下算术后果以该 statement 的正确适用及所标标准解析输入为前提；原作者证明、标准自守 L 函数解析定理的证明均未在此重审。无新 web、下载、引用链或数值实验。

## 2. 全阶有限分解：新因子存在，目标参数没有被替换

det1 二维表示的标准 Clebsch–Gordan 分解给

    V^(⊗2n) = ⊕_(j=0)^n m_(n,j) Sym^(2j)V,
    m_(n,j) = binom(2n,n−j) − binom(2n,n−j−1).

越界二项式取 0。可直接比较对角元 diag(x,x^−1) 的 character：左边 (x+x^−1)^(2n) 中 x^(2j) 的系数是 binom(2n,n−j)，而 Sym^(2j) 的权依次为 x^(2j),x^(2j−2),…,x^(−2j)。相邻权重系数相减即得 m；故是全部有限 n 的恒等式，不是少数试算。

特别地

    C_n := m_(n,0) = binom(2n,n)/(n+1),
    Σ_(j=0)^n m_(n,j)(2j+1) = 4^n.

C_n 是 trivial summand 的 multiplicity；它既不是全部对象维数，也不是目标零点位置的幂指数。n=1 时是 1⊕Sym²V；一般 n 的 Sym^(2j)V 最高阶趋于无穷。本族不能被描述为始终只重复 ζ 与某个固定第二因子。

若 Theorem A 正确用于 Δ，记 L_(2j)(s)=L(s,Sym^(2j)π)，j≥1；Sym⁰ 的有限 L 函数是 ζ(s)。在共同绝对收敛右半平面，由逐素数的精确分解得

    L_n(s) = ζ(s)^(C_n) ∏_(j=1)^n L_(2j)(s)^(m_(n,j)).        (1)

这不是把一般 tensor L 函数定义成原 L(π,s) 的普通幂。它是这一个已完全分解的 tensor 对象之 direct-sum 乘法；每个 p、每个 proper power 均保留。Level1 的选择没有另外丢掉有限坏素数。恒等式先在收敛域成立，随后用已付的各有限因子延拓；不在临界带交换 Euler 乘积。

## 3. 极点上界、精确极点阶与目标零点忠实性是三笔不同费用

加入标准输入“非平凡 cuspidal GLm 的标准有限 L 函数为 entire”，(1) 的有限 L_n 在全平面除 s=1 外没有极点，在 s=1 的极点阶数**至多** C_n。Entireness 本身不排某个辅助 L_(2j)(1)=0；故不能只凭该输入声称阶数恰好 C_n。

若再另付各辅助 cuspidal L 在 s=1 的非零性，则阶数才恰为 C_n。相应 completed 因子若已付 entire continuation／FE，只有 ζ-completion 带来的 0、1 endpoint poles，阶数至多 C_n；精确阶数仍需非零性。标准 GLm 的 line1 非零性可以作为另行标明的引用输入，但不是 Newton–Thorne Theorem A statement 中“cuspidal”一词的无说明证明。本门不依赖精确阶数，有限上界已足够作角色测试。

对每个实际 ζ 非平凡零点 ρ、0<Reρ<1，若 ord_ρζ=m_ρ>0，则 entire 辅助因子在 ρ 没有 pole，因此

    ord_ρ L_n = C_n m_ρ + Σ_(j=1)^n m_(n,j) ord_ρ L_(2j)
               ≥ C_n m_ρ.                                 (2)

这是完整的**同位置零点保留**：辅助零点可以增加重数，不能用 pole 抵消目标零点。不假辅助零点与 ζ 不相交，也不假目标零点 simple。若使用 completed 形式，只需在该开带核其实际 Γ 因子没有额外 pole；有限 L 版本 (2) 已不需要此附加讨论。

所以不能以“没有目标桥”泛称本族完全看不到 ζ。它确有 (2) 这条忠实因子桥：若独立证明某个 L_n 全部非平凡零点在中心线，即可推出 ζ 的相同结论。但 automorphy、entireness、FE 和 endpoint pole bound 没有证明 L_n 的 RH。证明了 (2) 并不等于证明其前件。

## 4. Deligne／Landau 比较实际约束的是谁

对同一局部对象，

    log L_n(s)
      = Σ_p Σ_(k≥1) (α_p^k+β_p^k)^(2n) p^(−ks)/k          (3)

在其合法绝对收敛域成立。所有系数非负；指数化也给非负 Dirichlet 系数。这里的正号来自同一个实局部幂迹的偶次方，不是完成经典 Weil 型对任意 compact complex source 的正号。

使用非负 Dirichlet 级数的收敛／实奇性原理，以及 L_n 除指定 endpoint 外的 pole 控制，可以限制 (3) 所含**局部** α_p、β_p 的大小。这正是 567§6 所恢复的 Deligne 类型机制。若未预用局部纯性，拥有全部 n 的相应合法解析输入可以用来逼近并证明这种局部 tempered bound；若已用 Δ 的纯性，则是重获已知局部事实。两种读法都没有把目标换成 ζ 的全局非平凡零点。

(3) 中的幂是 (α_p^k+β_p^k)^(2n)。与之相对，(2) 中的 ρ 仍是原来的 s 平面位置，重数乘了 C_n。没有出现一个已识别的全局零点算子 Θ_ζ 的 tensor、其 eigenvalues 的乘积，或中心化生成元的相应 tensor-sum。也没有独立同源公式把局部半径比较对象变成 ρ 的实部。这一识别不能由 n→∞ 的符号自动补上。

567§6 的 all-tensor pole 机制本身不是错误；问题是使用者必须对同一 α 消费其结论。073§4 已明确区分 number-field local Satake tensor 与 global zero-space tensor，002§2 的单位局部参数1／ζ例子是更便宜的负对照。当前新自守来源支付更多局部 tensor 解析设施，却没有改变这条谱角色责任。

## 5. Γ、维数与重数：必须保留，但不足以单独宣布 no-go

整 tensor 的标准 completed L degree 为

    D_n = 4^n,
    D_n/C_n = 4^n(n+1)/binom(2n,n)
             ~ sqrt(π) n^(3/2).

此处 degree 按真实 Γ_R degree（一个 Γ_C 计2）计；不是数一数不可约 summand 就得到 Γ 费用。各对称幂的 shifts、端点、导子与规范常数仍必须在任何显式公式／成长窗比较中真实合成。本稿不靠一个总 degree 代替完整 Γ 核，也未独立审查具体无穷参数公式。

因此把完整 tensor 的一般 degree 型误差除以目标的 C_n 重数，不会**仅凭这两个数**自动成为小误差；其比例反而增长。这是对“重数放大免费压掉 Γ”这一未经付款推理的负对照。它不是实际费用的必要下界，不证明某个 signed 抵消、专用源、联合尺度或非局部比较不能做到更好。

同样，C_n 大或 pole order 增长本身不否定每一种 Deligne 弱界；若有与 n 相关的有利合并误差，可以另行比较。当前没有那种新估计，不能把这句合法可能性当已付输入。本门不优化零点比例或无零区域，也不沿 n、weight、level 或另一模型自动续预算。

## 6. 完整目标型、源域与允许修复

(1) 的 log derivative 和任何合法的完整显式公式是加性的。若统一完成化、符号及测试规范，tensor 公式包含 C_n 份目标 ζ 项及全部辅助项；全部 proper powers、Γ/contact、双 endpoint 和剩余误差都不能删除。素数侧 (3) 非负不等于其中任一完整 Weil 二次型非负。

即使日后得到完整 Q_n≥0，也不能从

    Q_n = C_n Q_ζ + Σ_(j≥1) m_(n,j) Q_(2j)

直接通过“减去辅助项”推出 Q_ζ≥0；需要对辅助项的实际符号／比较负责。另一方面，若得到的是 tensor **零点全部在中心线**，则可以直接用 (2)，不必先满足几何 principal/Pan 路线。这两种逻辑不应混淆。

当前 V 不是 physical r 的商，不是 principal class、primitive divisor 或全局零点空间。本稿未构造 r→D_r、未付 405 全 noncompact Pan、537 非根／全源 coverage 或 du／zero-extension Dlog norm 运输。但这些未付几何项不是额外否定一个独立全局零点证明的理由；它们只在声称提供该几何／Weil 实现时重新成为必要责任。

保留而未排除的修复包括：实际 global／relative／graded cohomology 与 trace，使局部 tensor 控制忠实作用于目标谱；独立完整 Q_n 正性并付清辅助项；某个 tensor L 的独立 RH 经 (2) 传递；有实际原范数与合并费用的 signed、联合成长、源适应或非局部机制。它们当前未被构造，不能由“未排除”授予后继合同。本稿不证明所有自守放大或所有 Deligne 类比不可能。

## 7. 强旧扣除、分类与停止

| 已读旧证据 | 本门可用的准确范围 |
|---|---|
| 002§2 | local pure parameter 不等于经典 ζ global zero-line；单位局部参数1仍有目标责任 |
| 073§4 | 真 global Frobenius tensor determinant 与 number-field local Satake tensor 的区别；仍欠独立 global trace/determinant |
| 567§6 | 全阶正性与 pole budget 的 Deligne 机制约束同一局部 α；不把局部ζ参数1认作全局零点 |
| 10-29 fixed-C₂ root／role稿 | 固定有限两简单对象只改 ζ/Lχ 重数；保 relative/lax/graded/nonfinite 逃逸，未排本次有无限多 Sym factors 的族 |

本门的 Clebsch–Gordan 与因子身份是标准表示代数及所标解析输入的直接消费；本稿对经典目标的停止理由属于强旧角色检验 old0。Root 新取得的 Newton–Thorne statement／PDF 属其来源门的新文献输入，不能因此说“本次没有新来源”，也不能反向把新来源标签当成新 RH 数学轮。

没有新的数学合同、计轮或宏观周期。实际 principal／sections／mixed、危险 signed core／cross、自然成长 Ξ 与 whole leading4/5 负惯性 UPPER 均未改变；本稿不是实质核心方法类的完整边界，不满足 Goal 完成门。停止这一未补 global-target 控制的自动放大推理；不自动打开作者证明、II、后章、引用、另一 level/rank 或参数。

## 8. 实际阅读与版本

已读当前 README／STATE、Goal、C065、AS/AR 与 macro21 的相关范围及宏观入口；执行结构 check→show 时 parent 的进行中 pending 记录一度缺必要 observation/resume 字段，已告知 root、未私改。该结构故障不作为数学证据。旧567第一次按错误文件名读取失败；随后以 `rg --files` 定位到下列实际文件并直接读取§6及相邻限定语，不以失败 locator 推不存在。

下表均为本稿读取时的实际 raw 字节；旧文献 manifest／cadence 在旧 C₂ root 中的绑定属于其历史版本，本文不把它们当当前库／计数值。

| 文件 | bytes | SHA256 |
|---|---:|---|
| notes/002-global-existence-audit.md | 10963 | 65a5bbe1971ea97d5e40c1da53cba9c06001da2362f85153ec77a97da8f8df35 |
| notes/073-tempered-polarization-tensor-category.md | 12906 | 3a0a9ab86a5080c4f8af0e18895ef62f31c0e5be52dfbb6ce4580b51a4a76b93 |
| notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md | 14450 | 96c0c5a62e4175705696a29ed28d890eb11cec6f7351dc763641b65f3fcaec8a |
| reviews/2026-10-29/finite-monodromy-tensor-admission/root-consumption-scope.json | 8038 | 17f675bf71a79db2d21ba6aef509b15b05f789c0f9d9e61cb96fad07ed14903b |
| reviews/2026-10-29/finite-monodromy-tensor-admission/strongest-old-and-spectral-role.md | 7539 | ca7784fc9a076ffa318553ddc0bbe8a48a2e4a951f9a0ea4f79ba805201e652b |

新 primary 的版本、哈希、实际视觉页范围及 Theorem A 逐字核验由 root 来源记录负责，本稿不重复认证。文件哈希只绑定版本，不认证数学。
