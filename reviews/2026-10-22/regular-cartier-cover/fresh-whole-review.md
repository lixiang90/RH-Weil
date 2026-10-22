# C038／575 的独立整稿复核

2026-10-22。独占 fresh 原件；不修改主稿、STATE、合同、cadence 或发布状态。恢复了 G20261014、当前 C038、574 结算及宏观前沿，执行研究状态 check/show，并逐读575、finite-normal、natural-sheaves、actual-source、controls 五份当前原件。本稿判断依据是下面的数学比较，不以结构检查、文件存在或版本 hash 代替证明。

**结论：两处费用／域的范围修正已由 root 纳入后，局部数学结论限定 PASS。独立源到 mixed 容量、完整 Weil 正性与长期 Goal 完成仍 BLOCK／open。** 本审查没有找到可反驳有限 normal-order 指数门的方程对；没有把未找到反例当作证明，而是重新核了其必要性和充分性。

## 1. 固定对象与新增结论的准确层级

本稿只消费574的实际 O、Γ=Z²、两片 Wp/Wq 和共同 bulk 坐标 x，固定 L=log2、M=log3、ρ=e^x；全 O 仍非 proper。S∞ 是在两片螺旋加边界圆上由 ambient cylinder C∞ 函数限制得到的指定候选层。它不是裸一般 g-integer 分布已唯一决定的 regular 层，也不是已证明的 scheme／DVR／proper 模型。

574的绝对参数核 iΛ、保两端 frames 的核零，以及不变正 metric 恰 Re z=0，是本轮输入。575新增的是该实际模型上的 Cartier 实现、finite-normal 代表的更强精确门、具体全源 primitive 的 units／过滤与费用比较；不是重算全 Pic，也不是已有410／420、perfectoid Cartier或函数域定理的新发现。

## 2. 对有限 normal-order 门的反例尝试与证明闭合

先检验 normal jets 是否依赖 ambient 延拓。若 F 在螺旋上为零，沿 x=x₀−nL 的序列逐阶除ρ并取极限，依次迫 F 在整个边界圆上的全部 normal Taylor 系数为零。紧边界可把局部延拓通过 ambient partition of unity统一；故边界 normal jets 确实良定义。相反，并未证明整个 ambient 延拓唯一。

对 h_p=e^(zx)h_q，令两侧首个**不恒零**的边界 normal Taylor 系数分别为 A、B，阶为 m、n。审查时特意允许 A、B 有零，未先假设 unit-leading：

1. 任一侧 flat 等价于限制值对每个 N 为 O(ρ^N)。固定有限 Re z 的乘幂保持这项性质，所以不存在一侧 flat、另一侧 finite-order 的反例。
2. 统一 Taylor 余项给 A+O(ρ)=e^((Re z+n−m)x)e^(i Im z x)(B+O(ρ))。正实指数迫周期 A 恒零，负实指数迫周期 B 恒零；故 Re z=m−n。
3. 三频紧环面负向近回归把渐近关系提升为 A(x)=e^(i Im z x)B(x) 的精确恒等。若 B 有零，其 M 周期轨道把 A 的零传播到 L 圆上的稠密集，迫 A 恒零；无理比 M/L 正是本步责任。因此首系数的零点不能提供额外参数逃逸。
4. 两首系数无零后才使用绕数与有界周期 log，得到 Im z∈Λ。反向 ρ^mθ_L^u、ρ^nθ_M^(−v) 给全部 Z+iΛ 参数的实际 bulk 非零方程。

由此，本门的精确条件 z∈Z+iΛ 成立，且强于预先假设“整数幂乘边界 unit”的旧574推论。限制条件必须保留：固定ρ-normal结构、固定两片、精确 scalar 指数 clutch；不是任意 moving 除子、额外 normal 方向或全 Pic 的分类。

反向检查也重要：E=e^(−1/ρ²) 使 Eρ^z、E 对每个 z 都给合法 smooth-flat regular 方程；其参数 mixed 导数在紧参数集上一致 flat。故纯虚 absolute 非平凡类的定义方程必须双 flat，并不等于没有 Cartier 代表。iΛ 内仍有保 frame 的 relative 非平凡类，不能由绝对平凡替代相对结论。

另核 root §3.1 的合法修补：共同改用 τ=ρ^c、每个固定 c>0 重建 normal 层时，首项变为 e^(cmx)A、e^(cnx)B；实部比较给 c(m−n)，同一三频论证仍给虚部Λ。故准确条件改为 cZ+iΛ，纯虚 absolute 非平凡与全部 S_exp primitive 的 flat 结论保持。这里重建了结构层，并非说任意实幂是旧 S∞ 的坐标微分同胚；没有对变化 c 的统一 norm／metric 结论，也没有排不同 normal 方向或源依赖厚化。

## 3. Cartier 理想、对偶与完成化的方向

ρ 在稠密 bulk 无零，直接证明乘ρ在各局部层单射。Wp 上ρ、Wq上1给真实单边界可逆理想；交换两片后乘积为全局 principal (ρ)。Re z=1 不在574绝对核内，因此该单边线非平凡，不能称“仍只有自由线”。

约定 e_p=g_z e_q 时，局部方程比 h_p/h_q=g_z 给的是理想 I=O(−D)=L_z；通常 O(D)=I∨，inclusion I→O 才是其对偶线的 canonical section，局部系数为 h_p、h_q。当前原件已正确分开，不能后续反号消费为有效截面容量。

连续消失理想 J 有 J²=J，而指定 (ρ) 有严格幂链；ρ^β（0<β<1）的有限线性组合按最小指数比较，在 C/(ρ) 中确实线性无关。S∞ 中非零 flat 方程又落入全部 (ρ)^N。将这些方程的**嵌入像**送到ρ-adic完成化后为零；抽象可逆模的完成化仍可自由，不能据此宣称整条线或形式 Pic 群为零。575保留了这个区别。

## 4. 全405、537与同一物理映射

对所有 r∈S_exp,C，A_r=∫_-∞^x r、g_r=e^A_r 的负端衰减估计控制全部 radial 导数，g_r 与逆都在指定 S∞ 内延为边界值1。它们是实际 side units，故该同一映射消去全部 P_c，也同时消去537真非根。用 E g_r、E 作方程时，作为嵌入理想两片仍等于(E)，不是仅 Pic 类碰巧不动。

405实际非compact关系 P=(D²−1/4)H、H>0、H∈S_exp 的确在映射域内；端点分部积分给 ∫P=−∫H/4<0，μ±P=0。537 r₀=(D²−1/4)ψ 的两矩亦零且完整 Qζ(r₀)>0。因此不能把“过关系”和“保非根”分别从 primitive 与 mean 两个不同候选拼成一个成功映射。按照 P_c 专门删选 units 可合法制造旧商，但未支付自然 locality、过滤或独立容量。

actual E／Fourier公式只在405已指定的 η∈S_even,0 与相应实际来源像内消费，不允许由闭像或关系像反推任意物理 r 有 η-lift。另核 root 追加的几何范围修正：这是同一 log-time 中 x 与−x 的反射函数恒等式，本身未给574有限位 P↔Q 几何反射、regular层比较或Cartier同构。将两个primitive赋给两片frame只能作为另一个具体候选检验；在此候选中，primitive的和是mean，双 frame 正规化平凡，保mean则由同一P失败。此项不是全源桥，也不是已经支付的两finite边界协同。

解析修补的停止也有实际反例：A_P 在负端 flat，却不能在任何负尾恒零，否则 H 在该尾满足(D²−1/4)H=0，超指数衰减迫 H=0，与正性矛盾。因此边界解析结构排掉该候选的真实405关系；compact源负端恒1则本来平凡。只要求 x-entire 与要求ρ-analytic不能混同。

## 5. 已修正的原范数与延拓范围

本次 fresh 发现并要求两项范围修正，现已复读 root 修后文本：

- **bulk normal 导数不是 restriction 层的内在算子。** 在一个远离边界的局部 angular chart，可用 cutoff 乘 θ−(2π/L)logρ，得到在螺旋上为零、bulk ∂ρ 却不为零的 ambient 函数。因此ρ^−1r及高阶 e^(kB) upper 只属于所选 θ-independent radial extension，不能据此声称所有延拓的法向分量有同一下界。边界 jets 独立性不与此矛盾。修后主稿／source明确保留这项范围；同时 D_xA_r=r 与切向公式 ρ∂ρF+(2π/L)∂θF 给出任意**完整 ambient C¹ norm**的真实 point 费用。
- natural分支 §7 的ρ^A在连续层允许 A>0；若作为 S∞ 方程消费，现已明确 A∈Z≥0，或改共同 flat 因子。没有继续把任意实幂默认为 smooth。

固定源窗[−A,A]，C0 primitive费 √(2A)||r||du 是 sharp supremum；Dlog上界借 ||r||du≤(log2)^−1/2||r||Dlog。点值窄 bump 的 Dlog平方费是 ||φ||²log(1/ε)+O(1)，正规化后的点值仍发散；用两个远离该点的固定probe消两矩仅付 O(√ε)。故这不是只在 pole 方向上的反测。

固定κ平滑确实支付所选 radial representative 的每个 fixed-cover-window regular upper；它仍给平凡理想。零 Pic 类本来可取单位代表，所以这些费用不能升级成所有 source-to-class lifts 的必要下界。源窗A、覆盖窗B、导数阶、S_exp半范数和 cofinal量词均须分开。

## 6. 连续正反、函数域与真实已有设施

连续 Z_c、d=±1/16 模型中，同一 odd源 r=(D²−1/4)(uφ) 有两矩和mean零；a_r=−c a_(uφ)且 B_(uφ)>0，完整型 2d c²B² 严格异号。当前 primitive／全部 normal jets 在两者均平凡，连正模型的 primitive方向也未覆盖。模型自己的Γ=0不是从经典目标删Γ，也没有给一般连续g虚构经典adeles。

自由添 R_d[[t]] 时，两段普通复代数均是两个formal DVR分支，有限jet维数同为2n；差异仍在†，正段逐支共轭、负段交换。它只反测“自由regular添层＋任选纤维metric”不足，不能推广为全部自然几何增强的反定理。

真实函数域有同一曲线上的DVR、principal乘积公式、proper H⁰、moving／base change和曲面mixed RR／Hodge；genus2已付控制的 twist 真使 h⁰从2变1。不能用连续层无限bulk截面反驳这个正控制，也不能把曲线线性RR直接当平方容量。

已直接核对[CC原文](https://arxiv.org/html/1603.03191v1) §§4.3–5.4：fraction／order与周期type-II RR确实存在；Thm5.17的维数是经过滤与归一化的拓扑维数极限，不是复h⁰。这与[Stacks有效Cartier](https://stacks.math.columbia.edu/tag/01WQ)的scheme条件和[proper曲线RR](https://stacks.math.columbia.edu/tag/0B5B)的范围均相容。旧384／387／396的真perfectoid Cartier设施不被当前连续层反测否定；欠缺的是到574的实际有费比较与全源mixed预算。

## 7. 可消费与不可消费的结论

可消费的新增结论是：固定actual覆盖上有真实非平凡Cartier理想与全部指数的smooth-flat代表；finite-normal首项门准确为Z+iΛ；当前非Q primitive recipe在同一S∞单位层上对全源平凡，费用和解析域失败明确。三分支、root计算、fresh及来源核查合为C038一个完整数学轮，不按文件另计。

仍不可消费：自然唯一regular层、405保持且537可见的独立moving源桥、同层分离局部整性过滤／有限评价kernel、原norm cofinal容量、primitive ample／mixed RR与完整Q的同源身份。经典Γ=2θ′及contact、全部 p^k、双pole和allcomplex mixed均保留于575(8)，两位局部数据尚不覆盖它们。

故独立容量、Weil正性、成长core／coupling／Ξ仍open。最强实际ζ后果仍542+555→557 whole leading4/5负惯性**上**预算，不是负谱lower；本轮局部设施没有更强actual净后果，不满足宏观Goal完成门。按用户止损停止primitive／smoothing、mean／旧商标签和域缩小recipe，保留新moving支集、额外normal方向、非scalar／semiring／derived层、强拓扑／变域与有费无限修补的合法逃逸。
