# 2602.15941v1 截面候选：原源映射、关系与验证门审计

2026-10-22。独占子稿；不改公共 STATE、cadence、合同或 Git。按本次用户“按新路线图继续”恢复
G20261014／冻结 0c4f≤538；actual 变分门已在 D20261020Q 停止，不复跑安全高度参数。
本稿只审路线图 B 已点名的 2602.15941v1，不自动启动下一论文。

**结论：原文给真实的秩一算术截面、有限位相容的有理限制及 tensor 乘法；
尚未给出旧测试源到这些截面的映射，亦未给出与完整 Weil 型相连的平方容量。
固定目标上的裸加性运输并不是缺失映射的可用默认构造；但这一窄失败不排 families、
tensor／correspondence、非加性或 relative 实现。现有有限过滤、smooth probes 与正反模型足以定位
所缺前提，不能自行补出它。**

## 1. 恢复和本稿消费范围

已读 goals/README、STATE，运行 research_state.py check 后 show；读本 Goal、前沿有关条目、
D20261020Q、路线图 B/验证矩阵，以及 568、567、405、393、552 的相关原证明。
现场起点 HEAD 为 2e3f42844947dadc8b1abedc322414efd067bc9e；读稿时工作树无旧改动。
该现场观察不是 remote 验证，也不代 runtime Goal 现场记录，由 root 统一处理。

本次本地 PDF 文本核读范围：2602.15941v1 印刷/PDF 同页 17–19、23–24、31–42，
尤其 Defs 3.1/3.5、Thm 3.4、Prop 5.1、Defs 8.1/8.4、Thms 8.5/8.6/8.15。
PDF 页 30–43 已整页提取；另以关键词读取上述前置完整页。未把后附录全部证明或全部 48 页算作重核。
首次系统 MiKTeX pdftotext 因本机初始安装注册表权限失败，随后 pypdf 只读提取成功；无下载、后台进程或 PDF 改写。
细小排版/符号以 root 的原页核对为准，本稿不据提取器猜补新命题。

本稿的比较基线不是“尚无任何载体”：568 已付完整源定义的非退化 signed 商、评价 minor、
局部 étale/jet、连续正反测试及经典完整 J；569 已付 matched cocycle／determinant-line 协同。
567 的曲线 RR→Hodge→全周期 Gram 和 563 的正 H 均属已知／旧资产，不重计。
最强实际 ζ 后果仍 542＋555→557 whole leading 4/5，上预算不是负谱下界。

## 2. 原文提供什么对象，不能改成什么对象

原文的算术除子为 D=(L,||·||)：L 是 torsion-free rank-one **阿贝尔群**，可嵌入 Q；
L⊗R 上半范数为 λ|·|，λ≥0。framed 版本再给 ξ:L→Zhat 和 τ:L→R，
τ 的绝对值恢复半范数。tensor 乘法在 L1⊗Z L2 上定义，frame、metric 也同时相乘。
Thms 8.5/8.6/8.15 将这些原范畴对象与 adelic monoid 精确对应。

Prop 5.1 的 O(D) 是绝对结构层上的 module Γ-set；不是一个预设复向量空间。
不含 ∞ 的开集先取 H L(U)；含 ∞ 时在有限 pointed set X 上施加

\[
 \sum_{x\ne *}\|\varphi(x)\|\le1. \tag{1}
\]

因此 metric ball 不会因被称作“截面”便成为对任意复标量封闭的空间。
有限位的 H L、arch 条件、Picard 参数空间和函数空间上的 spectral carrier 是不同对象。
§9.4 另有 Schwartz cross-product sheaf；它不是 Prop 5.1 的 O(D)，不能凭同一字母 O 合并。
§9 的实际分布迹/局部 Fourier 已有独立来源，但没有在此证明 O(D) 的平方 RR／全源正极化。

这里原文所谓 finite type 指 λ>0，并不等于 L 有限生成。例如 L=Z[1/p] 配非零 metric 时
仍有无限多个满足 ||x||≤1 的元素 p^(−k)。不能以“非奇异 metric”推出普通截面容量有限。

## 3. 已有真实 restriction 与尚缺的复源 map

选择 embedding L⊂Q 后，同一个有理元素在所有合法局部化/完备化的像给 genuine diagonal restriction。
Prop 5.1 前对 L(V) 的字面“属于 L 且分母仅在补集中”写法仍有局部化歧义；
若在非空 Zariski open 上采用标准 L⊗Z[1/S]、另置空集值为零的修复，应明确标作补充定义，不能冒称原文已经逐式给出。
在 framed 版本上，ξ_p(x)∈Z_p 还能逐 p 取模 p^k；有限位 congruence 过滤及其 kernel
都是同一有理元素的条件，不是每个位点另选插值向量。
这是真实有限算术限制原型，与从 closed-point 数任选自由直积有区别。

但应保持两个限定：

- 模 p^k 的 congruence 是算术有限厚化/消失过滤；它尚不是所有物理 log 坐标导数 jet，
  更不是未经证明存在的复代数曲面局部参数。
- 有 arch 条件时，应在 (1) 中取这些限制及其 kernel 的交；不能把整个 ball 的 kernel
  直接当普通 C-vector-space 的 H0(D−E)，也不能以其有限 cardinality 或 S-dimension 代普通 h0。

原文没有定义下列尚需的纵向箭头：

\[
 \mathcal D\ni r=e^{u/2}f
 \ \dashrightarrow\ \mathcal V_j(D)
 \ \xrightarrow{\mathrm{restriction}}\ \mathcal J_j(E). \tag{2}
\]

这里 V_j 可以保 Γ-set、模、族、相对对应或复提升，但必须实际写出，且说明源的相加、
卷积、共轭/反演如何在那个范畴实现。把 J_W r 的若干复数值写在模 p^k 的格点上不是定义：
值一般不在 Q，任意 rounding 改了加法和混合项，并引入未经付费的原 norm 误差。
以 Eη 作 (2) 的普通逆构造也不行：552 已核 E 的像是 zero-jet 关系理想 I，
不是全 Weil 源空间。那是已付范围，不是本次新障碍。

## 4. 一个可完成的窄检验：固定目标的裸加性 map

以下仅是检验某种默认运输是否合法，不是所有几何构造必须满足的公理。
设 A 为原测试空间 D 或 S_exp 的**整个**加法群。

1. 固定有限 congruence 目标 G 时，任意加性 map A→G 都为零。
   若 m 杀死 G，对任意 a 可写 a=mb，于是 F(a)=mF(b)=0。此处只用源的可除性，不用连续性。
2. 固定 D、λ>0，若加性 F:A→L 的全部值都在 arch unit ball，则 F=0。
   因所有 nF(a)=F(na) 仍须在该固定 ball，n||F(a)||≤1 对所有 n 成立。
3. 若取消 ball 而把 L 赋予 λL⊂R 的自然 metric 子空间拓扑，则连续加性 map A→L 仍为零：
   A 路径连通，像为 R 的连通子集，却包含于可数 λL，故只能是单点，且 F(0)=0。

不能省略限定。若 L=Q 且不要求连续性，Hamel/Q-linear 非零 map 存在；
λ=0 时半范数不分离，第三条不适用。有限过滤后的 bounded 源片不是可除加法群，第一条也不直接适用。
更不能由此要求任意 source→Picard/family/complex/tensor/correspondence 的 map 都是加性到固定 L。
例如除子随源变化、metric 的指数参数、加法通过 tensor 实现，均不属于以上三类。
这些修复若实际给出，其 relations、mixed pairing 与费用须重新检查。

因此该检验的决策信息很窄而确定：**不能把“秩一 group 和 restriction 已存在”直接消费为
从整个复测试空间到固定 arithmetic jet 的非零连续加性评价。**
它没有证明一般 g-integer 或经典 ζ 不存在几何运输。

## 5. 405 主关系与 537 非根必须同时通过

固定旧 f 与物理 r=e^(u/2)f。405 的

\[
 P_{\rm an}=I\cap\ker d\cap\ker c
\]

只是已经构造的解析 principal 候选；I/P_an 的两个次数方向仍有双曲配对。
在 S_exp 中有非零 p=Eη0∈P_an，而 h=Eη 满足 c(h)=d(h)=1/4。
物理谱 Q 的根含 e^(u/2)I；原 B 商只消 P_an。二者不能混用。

对新几何 (2)，需要先指定其 relation 对应的是哪一个配对：

| 消费角色 | 最低合法测试 | 不能代替它的做法 |
|---|---|---|
| 主关系／principal pair | e^(u/2)p 的完整几何类在相应 quotient 或 matched determinant line 中消失 | 仅让一个 Green 分量为零，或只验证局部 unit |
| degree/codegree | 说明 h 的双次数和 pole 片如何补偿；不要求各 budget 片分别下降 | 直接商掉整个 I 却仍声称保留两个 degree |
| 非根见证 | 对任意非零 ψ∈Cc∞((-17/16,17/16))，r0=(D²−1/4)ψ 的像不被抹掉 | 只在 Eη 关系像里找一个非零几何 divisor |
| 原 norm | 比较保 zero-extension 原 du/Dlog，或列出额外强 norm 和运输费 | 把几何 point evaluation 或 p-adic norm 当作原 norm |

分部积分使 r0 的两个 pole 矩恰为零，537 给 Q_W(r0)>0，故它确为 Q 的非根；
f0=e^(−u/2)r0 不在 I。该正号来自旧 fixed-window 资产，不是本次 O(D) 的新贡献。
552 已给合法 radial adelic metric 仍把 p 送到非零 energy 类的具体失败；
其二阶高频费用也不等于 actual Γ 的 log 阶。不能重复调同一个 radial scalar 来修复 (2)。
非局部、全位、族、source-adapted 或不同 Green 方案仍未排。

在当前候选中纵箭头尚未定义，故两项测试状态是 **未具备输入，不能通过也不能判反例**；
不是证明原文 O(D) 本身错误。若用 568 signed J 复合 probes 来补纵箭头，关系/非根可通过，
但只恢复旧源定义 map，不能把它当独立 principal 几何或容量来源。

## 6. finite filtered 与 smooth 测试能否改变当前选择

可执行的有限任务必须先有实际 source map，再核同一 map 的 kernel、乘法和 capacity；
不能先选任意 finite image，随后把其 dimension 命名 RR。

393 已付单 p 实际截面的轮廓满射和目标 CC 一致拓扑下的过滤维数 max(w,0)。
它同时证明解析 Banach 商拓扑在非零轮廓上离散；轮廓不是通常线性 map，
正权时解析 H0 普通 K-维数无穷。故它并不直接给当前源过滤、同一乘法单射下的单调容量，
也不提供算术平方上的二次项。仅在现 O(D) 上再读一次线性/周期 RR 不改变核心选择。

568 的 smooth probes 是合法的原 norm 修复：对 fixed I,J，

\[
 e_\psi(r)=B_W(r,\psi),\qquad
 |e_\psi(r)|\le C_{I,J}\|r\|_D\|\psi\|_D. \tag{3}
\]

所有 compact probes 分离 J 像；它们可代 point/jet，不能免费取 δ 极限，
后者一般付 ||ψε||²_D~ε^−1 log(1/ε)。但 (3) 只有复数读出，不定义其到 rank-one arithmetic section 的 map。
有限个 probe 的所有 PSD Grams 也只检有限子空间；全 probe／全 cutoff 极限的 PSD 与原 Weil 正性等价，
不是独立新输入。有限验证若要改变选择，应检一个已写出的非旧 J 复合映射，至少能够：

- 在同一原 norm 可控片上消 p、保 r0；
- 用真实 restriction/乘法给可核的局部 order，而非用目标 Q 的符号反定义；
- 给与该 source 片同尺度的独立 capacity/height 上界，并说明错误完成化 B 或负段在哪项前提失败。

当前原文和已付资产没有交出这样的新纵向 map，因此没有一个适合继续扫 jet 阶、prime 数或过滤维数的
具体数值实验；有限平滑 Gram 只能恢复旧信息，不能替候选的准入。

## 7. 正反验证：真正要鉴别的是前提，不是重新计算 H

| 系统 | 既有真实可用输入 | 当前 O(D) 推广必须支付的差别 |
|---|---|---|
| 连续 Z_c，d=c−1/4=±1/16 | 同一个二阶 solution/jet carrier、Wronskian=1、固定0/1评价非零、统一高度界两段均通过；完整配对为 2|A|²+2d|B|² | 不以 literal Q/有限 residue 作为所有类 RH 的必要条件；若作连续 capacity，须给物理 real-* 与同源 budget 的独立比较。非零评价、正 metric、单线性维数不能区分两段 |
| 连续阈值 d=0 | jet carrier 仍二维；最小 Weil 商一维且 trace 权2 | 不能要求 faithful positive jet action 而错误排正例；不能按 quotient rank 静默删重数 |
| 真 E/F5 | 实际 H0(C,O(D))→H0(E,O(D)|E)，kernel=H0(C,O(D−E))；乘法、有效 degree、RR 来自同一个函数域 | 这些是来源原型；完整 Weil 号还经过 C×C 的 signed 对应/容量，不能将曲线级 restrictions 直接当平方正性 |
| 290/568 F5 Euler 反模型 | 所有 finite closed-point étale、local jets、raw positive Frob 同样存在 | 必须在实际 global gluing、signed effective/RR 或 primitive 比较处失败；不能以“不是曲线”略过前提检查 |
| 经典 ζ／一般数域 | 原源包含完整 Γ_R/Γ_C、所有 prime powers、contact、pole，数域保 ideal 标签和判别式 | 原论文 Q 的有理整性/frame 是额外算术输入；尚无从任意 g 数据取得这些结构的函子，更无由本载体支付 classic 全源 mixed budget |

真/反 F5 的已知 primitive Gram det 为 11/5 与 −1，属 567/568 旧资产。
本稿只用其鉴别候选前提，不再算点数、求 H 或把旧符号计新结果。
连续负段也不能从“其零点不纯”反推设施失败；失败条件必须先在同一 source-defined construction 中说出。
若仅提供局部 residue 或 mod-p^k restriction，真/反两边的自由局部设施仍同时通过。

## 8. 容量与完整源仍缺哪些独立输入

即使以后补上 (2)，仍须同一个对象承担：

1. 实际可乘 sections 与 principal 变换，局部 vanishing/collision order 的可加下界；
2. 不以 Q 反定义的 global height/RR 上界，及其过滤单调性、尺度与误差；
3. 同一非零 minor/determinant section 在所有位的协同规范；569 的 cocycle 可用但不能代此上界；
4. 对全部 compact complex r 的完整身份
   (A_j(r)−L_j(r))/c_j→Q_W(r)，c_j>0，或 567 已核的平方 RR budget，全部误差付清。

最后一项须保 Γ 的 finite-part/contact、log p·p^(−k/2) 的全部 proper powers 与双 pole；
不能由 arithmetic jet 的正 residue pairing 推出被减入的 primitive signed 差仍正。
仅有一次线性 RR 或 O(D) tensor 乘法没有生成这个二次系数；
若将所有 Weil Gram PSD、所需正曲率或“预算差非负且等于 Q”放回定义，仍是等价终点。

## 9. 消费记录与停止

对象：2602.15941v1 的 rank-one arithmetic divisor / O(D) module Γ-set / framed finite restriction。
域和量词：原文定义及每固定有限 reduction；原源 D、S_exp 和 fixed-window 非根见证严格分开。
norm：arith metric ball、R 子空间拓扑、原 du/Dlog、393 目标轮廓拓扑各保其角色。
方向：真实 arithmetic restriction 是 global→local；尚无 f/r→global，也无正预算→Q 的完整比较。
误差：本稿基本类型/加性检查为精确；未给任何新 growth、Γ 或 all-place 误差估计。
覆盖：固定 map 类的裸加性失败，不排 family/nonlinear/tensor/correspondence/relative/复提升；
其他路线需要自己的实际构造与费用，不能由本次停止自动准入。

**本门只得到已有几何对象的精确来源位置和 source-map 类型审计，没有新 classic 独立容量，
没有 whole 4/5/core/coupling/Ξ 净后果。** 依路线图入口规则来源止；不建新数学合同，
不自动打开下一 paper，不继续增加有限 primes、jets 或 smooth probe 参数。
唯一可使本候选重新准入的是实际写出的新 (2) 和至少一项独立 restriction/kernel/height 比较，
使 p/r0 与正反模型在具体前提上可判；仅换维数名词或引线性 RR 不足。

## 10. 原件与继承依赖

- 本地固定原件：literature/f1/cc-jacobian-2602.15941v1.pdf；原范畴以本稿 §1 页范围为准。
- goals/reviews/2026-10-20-generalized-weil-facilities-roadmap-after-572.md §5/§7；
  goals/reviews/2026-10-20-actual-variational-sonin-transport-admission.md §7。
- notes/568-source-evaluation-carriers-local-jets-and-weil-capacity-gap.md §§2–6；
  reviews/2026-10-20/evaluation-carrier/{continuous-carrier-and-budget-tests,function-field-evaluation-budget}.md。
- notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md §§2–7；
  notes/405-f1-adelic-restriction-moments-and-radical.md §§4–7；
  notes/552-radial-adelic-green-principal-and-comparison-gate.md §§1、3–7。
- notes/393-f1-profile-surjectivity-and-filtered-dimension.md §§3–6；
  notes/537-source-exact-weil-window-positive-tail-admission.md 的 fixed 17/16 全源正性。

版本绑定、独立审阅和 root 最终消费另行进行；本稿存在不表示其结论已被 root 消费或结算。
