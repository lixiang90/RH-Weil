# 001–149：Weil / F1 路线早期历史审计

审计日期：2026-10-11。当前 HEAD：`331107b2ba0716d2fb78ec1f605f05fe57393274`。范围为当前工作树 `notes/001-*.md` 至 `notes/149-*.md` 的全部 149 篇，共 36,050 行。未改旧笔记、正式成果或 Git；未运行新的 AM、无零区域或零点比例计算；未联网作泛泛综述。

## 阅读覆盖与结论强度

每篇均作实质的全篇结构化 survey：读取开头目的、各节主题、主要定理陈述、结论/限制与下一输入，以及结尾审计。完整非空文本精读 28 篇：001、002、010、031–041、045、046、073、074、105、121–129；其余 121 篇的证明未全部逐行深读。058 的正文19–357行已完整深读，开头1–18行按survey读取；为避免将部分深读冒充全文深读，统计在结构survey中。`coverage.json` 每篇记录当前 SHA-256、行数、阅读范围和判断。此报告不是 149 篇全部证明的独立形式核验，更不是外部文献的新颖性审查。当前旧笔记含指向 163、307 等后期纠正的更新，故以下阶段是依存链的回顾，并非逐 commit 复原当时的认识。

最重要的结果是：早期项目确实建立了不少有用的有限线性代数、正核、尾界与功能分析接口，也越来越准确地暴露了真正的数域输入；但没有在 001–149 中获得无循环的经典 ζ 正极化。多数完成的是“若实际算术能量/dual norm/normality 满足某统一估计，则中心线成立”。F1 在此段主要是数域 Weil 结构的动机和类比，尚没有一个独立于 RH 的 F1 上同调构造。

## 路线阶段：什么推进了，什么没有推进

### 1. 001–030：先抽象 Weil 极化，再尝试有限谱证书

001 给出有限维正 similitude 和 primitive HR 推出纯性的形式机制；它也直接指出从零点搭空间的存在命题可以与 RH 等价。尤其旧版奇次 primitive 使用 `J=I` 会在真实曲线奇次中使正性失败，现改为 `J_a`，并指向 307 校准。应把这次纠正视为必须用真实有限域正基准检验类比的经验。[001:33](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/001-polarized-weil-structure.md?plain=1#L33)、[001:55](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/001-polarized-weil-structure.md?plain=1#L55)、[001:194](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/001-polarized-weil-structure.md?plain=1#L194)

002 的 G1–G4 分开了载体、全局 determinant、prime closed-orbit trace 和正 adjoint。这个拆分是可长期复用的研究规格，能阻止“局部 Satake 纯性已经提供全局 RH”的跳跃。[002:7](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/002-global-existence-audit.md?plain=1#L7)、[002:25](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/002-global-existence-audit.md?plain=1#L25)

004–014 的真实进展是：端点修复、保留 prime/pole/archimedean 相消的高阶尾，再到 011 的精确 resolvent 全阶重求和，消除了固定有限候选的一个无限尾瓶颈。010 的四阶局部绝对值和约 `9.77e-2`，合并后仅 `3.41e-5`，显示先合并再取绝对值是结构要求。可它没有解决候选随尺度的统一最低谱支、gap 与指数加权 Xi 逼近；buffer 小和 near-radical Rayleigh 小主要是上界信息。[010:185](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/010-fourth-order-finite-phase-tail.md?plain=1#L185)、[010:204](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/010-fourth-order-finite-phase-tail.md?plain=1#L204)、[002:123](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/002-global-existence-audit.md?plain=1#L123)

015–030 把目标转向共尾 form 的绝对下界、compact defect 和 Feshbach core。固定尺度的 complement 控制是真结果，core 的统一 positivity/coupling 才是未获输入；degree-only、independent-well、phase-volume 等反例淘汰的是指定估计策略。相对 `o(lambda)` 并非中心线所需绝对 `O(1)` 或 `o(1)`。[015:195](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/015-filtered-asymptotic-polarization.md?plain=1#L195)、[021:235](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/021-block-large-sieve-proof.md?plain=1#L235)、[030:205](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/030-boundary-gap-rank-one-limit.md?plain=1#L205)

### 2. 031–044：把困难集中成真实 boundary current 的 membership

显式公式给 boundary/Mellin detector；Chebyshev error、Abel energy、Sturm–Liouville Green current、Bessel ell2 与 Fourier–Bessel Parseval 将同一 global tightness 分别写成具体算术条件。它们改善了载体的自然性和输入的可定位性，没有证明该 tightness。

最清楚的两个反例是：037 的 operator 可以无条件自伴、positive、traceclass，弱解也能存在，但 prime current 的有限 action 仍是 RH 级条件；039 的有限 Parseval partial sum 只能给能量下界，不能排除压到 `z=0` 的无限尾。[037:137](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/037-sturm-liouville-hodge-current.md?plain=1#L137)、[037:154](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/037-sturm-liouville-hodge-current.md?plain=1#L154)、[039:150](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/039-fourier-bessel-arithmetic-field.md?plain=1#L150)

041 排除绝对 Bessel/Hausdorff 完全单调路线，不能读成“Euler–Bessel 或 ζ 不能有结构”。真正未解决的是带符号的 joint resummation。[041:112](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/041-euler-bessel-cancellation-no-go.md?plain=1#L112)、[041:188](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/041-euler-bessel-cancellation-no-go.md?plain=1#L188)

### 3. 045–078：最完整的早期 filtered primitive Weil 规格

稳定 dilation resolvent、arithmetic de Rham square、Tate zero-mass primitive、annular detectors、prefix Hodge flow 等对象可从 primes 构造。058 明确区分：finite positive Gram、primitive inverse、形式 Mellin visibility、具有 `X^{o(1)}` dual norm 的检测泛函、tail upper，以及 actual-cycle growth。关键 FPW4b 不能由“核不为零”或有限 approximation 代替。[045:120](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/045-dilation-resolvent-cyclic-weil.md?plain=1#L120)、[046:94](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/046-dilation-de-rham-weil-complex.md?plain=1#L94)、[058:62](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/058-filtered-primitive-weil-master-theorem.md?plain=1#L62)

063、065 的指数增长反模型表明所有有限 Hankel/Taylor Gram 正并不会免费给临界 completion。073 又精确分开 tempered、uniform bounded 与 exact polarization：前者可允许 Jordan，后者在有限维要求半单。076–077 把 scalar 原子质量、Hilbert 维数、tracial multiplicity 分开。[065:204](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/065-abel-rkhs-boundary-weil-structure.md?plain=1#L204)、[073:61](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/073-tempered-polarization-tensor-category.md?plain=1#L61)、[076:19](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/076-matrix-valued-multiplicity-weil-package.md?plain=1#L19)

078 的 Ihara/Ramanujan companion 是这段最有价值的真实闭模型：operator 与 determinant 独立存在，Ramanujan closed band 恰对应 tempered，strict band 对应 positive polarization，而 band endpoint 的 Jordan block说明更强极化不能无差别要求。ζ 尚缺独立的 global companion/cohomology 与谱界。[078:88](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/078-ihara-ramanujan-hodge-structure.md?plain=1#L88)、[078:160](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/078-ihara-ramanujan-hodge-structure.md?plain=1#L160)、[078:187](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/078-ihara-ramanujan-hodge-structure.md?plain=1#L187)

### 4. 079–120：从直接 Euler determinant 到实际 response 的非局部几何

079 淘汰直接 prime-block Schatten operator 加非零 normal counterterm 的模型；它支持寻找非局部 divisor/determinant geometry，而不否定 F1。080–082 的 divisibility incidence 与 Nyman–Beurling 给真正无条件 Hilbert carrier，但相邻 log nodes 令 Gram 最小特征值本来就趋零。因此追全空间谱隙是错目标；要追 response 定向的 Schur distance、canonical representative 和 leverage。[079:206](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/079-prime-orbit-schatten-normal-limit-no-go.md?plain=1#L206)、[082:150](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/082-beurling-log-toeplitz-feshbach.md?plain=1#L150)

083–094 将实际 arithmetic residual 分到 almost-prime、Farey、cotangent、shared-gcd/Kloosterman 部件，一些 far tails、principal 与 fixed-small-determinant 项获无条件控制。这些是真的缩小“剩余在哪一项”的工作，不能据此套用不匹配范围的通用 large sieve。

095–120 建立目标定向的短化、cell wedge、susceptibility、charge kernel、Padé 与 determinant certifier。111–112 的 uniform `O(1/M)` relative tail transfer尤其说明无限 cell tail可先冻结，留下 finite head。104–105 的 sparse coercivity ceiling仅限制有界节点数 recovery，不限制 collective cells。工具变精确与实际 canonical response 得到 uniform arithmetic 界是两回事。[104:237](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/104-incidence-vandermonde-polylog-coercivity.md?plain=1#L237)、[105:121](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/105-sparse-recovery-ceiling-collective-frame.md?plain=1#L121)、[111:86](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/111-uniform-unit-cell-tail-reduction.md?plain=1#L86)、[119:160](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/119-positive-only-transversal-susceptibility.md?plain=1#L160)

### 5. 121–130：实际 signed period 与 no-free-purity 刚性

121–122 的 Mertens–Abel regression 与 sparse dual cycles是自然的 arithmetic 构造；但 period 守恒不提供其大小。123 给 fixed capacity 下 period 可任意大的抽象反模型；124 的 toy counterexamples淘汰 positivity 自动逼出交错/实根的希望；125 改为 positive capacity loss仍没有弱化 leverage 阈值。[121:156](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/121-mertens-abel-canonical-regression.md?plain=1#L156)、[123:150](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/123-squarefree-interpolation-period-no-go.md?plain=1#L150)、[124:177](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/124-alternating-external-period-defect.md?plain=1#L177)

126–127 区分真正 weight separation、角度与相位相消。Periodic conductor blocks 更接近分权，但现有 natural far completion只有 `N^{-2}` 幅度，不能传给 actual spatial representative；这是此 transfer certificate 的 gap，且 far upper bound不得冒充 actual equality。[126:198](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/126-block-weight-purity-overlap.md?plain=1#L198)、[127:163](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/127-conductor-purity-completion-gap.md?plain=1#L163)

128–130 给出清楚的 model no-go：exact acyclic pairing 保持全部 graded determinant variations，even gain由odd charge精确恢复；finite positive unpaired primitive必留下新det factor；canonical higher `det_m`也不自动制造 anomaly。数域几何必须解释实际已有 Euler/Gamma/boundary factor或真实 low-trace anomaly，不能任意加正定 metric后只宣称 same-zeta。[128:114](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/128-acyclic-completion-no-free-purity.md?plain=1#L114)、[129:67](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/129-primitive-residual-rigidity.md?plain=1#L67)、[130:120](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/130-regularized-residual-anomaly-accounting.md?plain=1#L120)

### 6. 131–149：passivity 规格的两次有效纠偏与两次淘汰

131–136 完成 positive-real/Pick 与 centerline 的条件接口，把高频负井的影响压到 Cauchy capacity；133–135 确有无条件 high-frequency localization，但 relative core density趋零仍允许全部异常 divisor留在少数方向。137–143 将 outer cone 精确识别为 `0<=theta<=1` 的 Cauchy-capped spectral measure，淘汰 uncapped PD character relaxation、非stationary Loewner optimizer，并给全部离散误差趋零的显式 cofinal schedule。[134:219](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/134-renormalized-passivity-hodge-index.md?plain=1#L219)、[139:101](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/139-capped-bochner-correlation-cone.md?plain=1#L101)、[142:229](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/142-shared-lag-stationary-cap.md?plain=1#L229)、[143:126](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/143-cofinal-stationary-discretization.md?plain=1#L126)

145 的实质优化是只需 negative depth一致有界便给 normality；仍是RH强度，并未获 actual bound。146 尝试 full quadratic energy `O(1)`，147 则证明此 ζ candidate 沿所述日程无论 RH 真伪都会发散：正的临界 Poisson spikes也被平方惩罚。148 full-character Loewner domination同样偏强，149 正确退到 finite-trace negative Hodge index。这个阶段最应复用的是容量迹和单边性，而不是新跑网格或全二次方差。[145:62](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/145-bounded-defect-normality.md?plain=1#L62)、[147:171](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/147-ratio-tail-square-quadratic-no-go.md?plain=1#L171)、[149:116](https://github.com/lixiang90/RH-Weil/blob/331107b2ba0716d2fb78ec1f605f05fe57393274/notes/149-finite-trace-hodge-index-structure.md?plain=1#L116)

## 八条跨笔记经验

1. **先锁定全局规格再类比。** Carrier、det、trace、positive pairing、closed adjoint domain分别检查；function equation、local purity、Euler positive edges不能代替其中任何一项。001/002/078 是正面规格，128/129 是负面规格。
2. **每个极限带全量词。** Fixed candidate的无限尾认证不等于尺度统一；relative small不等于absolute small；finite PSD不等于tightness；fixed-rank不等于growing-rank。004–015、031–039、063–065持续暴露这一点。
3. **先精确合并有符号局部项。** 高阶residual、prime–pole current、cotangent reciprocity、shared Gamma/pole lag都靠联合相消。各项取绝对值或total degree只会证明错误量过大。
4. **不要要求多余正性。** Tempered不必半单，trace multiplicity不必Hilbert dimension，target response不必全Gram gap，bounded capacity trace不必最小character统一界。073、076–077、082、145/149提供正确定级。
5. **形式可见必须附dual稳定性。** Nonzero Mellin multiplier只说模式未消失；进入actual positive Gram后的lower bound需FPW4b。Sampling/finite reconstruction若不迁移整个dual norm，就不能做purity证明。
6. **把有限工具与算术定理分账。** 111的统一tail reduction、Padé/charge/determinant认证都能反复用；但把大上界高精度认证到几十位不会使其达到RH阈值。119/120给直接实例。
7. **所有no-go都标模型。** 027/041/060/079/105/123/128/147分别限定估计、坐标、固定宽度、直接Euler块、有界节点、抽象公理、acyclic pairing、指定quadratic candidate。不能合成“ζ/F1/Weil路线不可能”。
8. **反模型要成为规格的一部分。** 真有限域奇次极化与Ihara endpoint必须过；指数Hankel、fixed-capacity unbounded period、uncapped character、critical positive spike必须失败。每条新主定理若把这些也一并推出不可能结论，应先纠正公理。

## 六个可证伪的后续命题与排序

这里的“可证伪”是有明确对象、命题与否证条件；不表示已经知道它们成立。前四项优先服务真正的 Weil/F1 构造。后两项仅保留早期接口，不建议恢复 AM、无零计算或大网格扩展。后期 150–437 的进一步反例应由全局报告覆盖后再选择。

### P1：独立极化的双基准协议（优先）

命题：一套拟议数域/F1极化公理在真实曲线奇次primitive和Ihara companion上，能仅由intersection/graph数据产生正确权、det和trace；同时允许 band-endpoint tempered Jordan，且不能对一般 reciprocal off-center pair强行推出正性。可证伪条件是任一真实正基准失败、或reciprocal负基准被错误认证。交付应是公理、有限精确证明和positive/negative实例，并明确G1–G4哪一项还没建成；不是再构造zero-indexed Hilbert space。支撑：001:33–55；002:7–21；078:88–123、160–195。

### P2：同ζ boundary/primitive trace 的逐项模型（最高价值，最难）

命题：从prime divisibility/closed-orbit数据出发，在一个独立构造的relative complex中，产生一项非acyclic boundary/primitive trace，其低阶贡献精确恢复critical prime `det_3`删除的 `P_X(s)+P_X(2s)/2`；并给Gamma/pole修正的现有因子解释、cutoff兼容及test variation账本。先在function-field或Ihara模型完成同构任务，再谈ζ。可证伪条件是贡献完全contractible、primitive因子不匹配原det、或counterterm通过未知ζ zeros定义。成功只建立全局几何规格，尚需独立HR inequality。支撑：079:206–211；128:114–140；129:147–154；130:89–102、120–154；131:179–210。

### P3：重复根的独立cycle与trace一致性（可先完成有限成果）

命题：在有重复primitive root的有限closed model中，构造不只是同一scalar current的linear filters的arithmetic cycles，使matrix atom rank恰为divisor multiplicity；并验证tracial determinant和matrix determinant给同一divisor。否证条件：所有cycles仍生成rank-one atom，或通过任意dark amplification人为补重数。它解决multiplicity和functoriality，不解决RH。支撑：076:19–63、185–214；077:190–211；078:160–173。

### P4：actual collective frame 与 sparse ceiling 的分界（次优先）

命题：固定R，针对actual incidence/cell-wedge frame，证明全部cells的shorted block比任何有界数量squarefree nodes获得更好的定向forcing susceptibility，且误差用111/112的统一relative tail迁移；必须同时报告normalized forcing moment，不能只比较裸 `lambda_min`。可证伪条件：增长cells仍受同一log负2R尺度、或改善的null spectrum对实际forcing没有增益。第一阶段只证明fixed-R渐近，第二阶段另提出growing-R常数控制；不把前者升级为RH。支撑：104:237–249；105:121–181；108的directional Green接口；111/112统一tail；123:150–182的抽象反例。

### P5：signed arithmetic period 的独立相消定理（有算术风险）

命题：先固定R=2或3，给canonical Möbius representative的external signed period `-F'(2)` 与alternation defect的实际渐近式或有效上界，保留Mertens–Abel signed regression和同一actual Gram。必须指出比123反模型多用了哪条Möbius/prime恒等式；然后才讨论达到124阈值的growing rank。否证条件：只得到capacity/positivity、依赖pointwise RH-Mertens bound、或优化代表不是actual canonical代表。Fixed-R结果即使成功也只是新算术输入的局部定位，不能自动RH。支撑：121:156–160；122:153–168；123:150–182；124:112–128；125:112–134。

### P6：容量迹的单边几何估计，而非全能量界（保留接口）

命题：对一个新且由primes/Gamma独立构造的actual Hodge current，识别非负background并证明剩余negative finite trace有统一界；positive critical spikes必须留在background，不能使residual平方反而惩罚它们。严格目标为149的 `tau((H_n)_-)` 加functional error `O(1)`，它仍有RH强度，不能写成已有定理。否证条件：background通过未知spectral positive part/zeros定义、full energy取代negative trace、或finite-trace norm只是任意选来稀释异常谱。支撑：145:62–110；147:123–185、197–235；149:59–70、191–199。应先在P1/P2的真闭模型建立这种HR关系，再决定是否能迁移到数域。

## 对根报告的建议

把真正的长期方向定为 **独立算术上同调 + 精确全局trace/determinant + 不循环的polarization**。058可作为工程式规格，078与真实有限域为正基准，128–130为completion负基准。暂不把已有能量等价条件的再平滑、再有限化、再高精度认证称为下一突破。早期最可信的可积累成果是证明载体/函子/相消/尾迁移的新有限定理，以及给出明确反模型；真正的经典ζ纯性仍需要一条当前记录未提供的global arithmetic HR输入。
