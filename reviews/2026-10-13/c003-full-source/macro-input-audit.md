# 四轮前的独立宏观输入审查

2026-10-13；仅修改本文件，不改 STATE、cadence 或主稿。
重新读取 AGENTS、README、STATE、check/show、Goal、C003、D20261013C，
并读529、normalization-erratum及旧Goal第十节。核查时STATE仍是C003 ready、
cadence=3，主代理待结算；529/reviews为未提交新增文件，无本子任务后台进程。
以下是路线筛选，不登记新增研究轮。

## 1. 529不宜触发整个Goal完成

529是完整实际连续型的结果，已给精确支持阈值、无限反例族、
scalar/local势/有界正锥相似类和不同组织审查；它有独立非重复价值。
不能把它降成单个H矩阵反例。但原始标准锥保正虽是一大通用技巧类，
其在当前核心问题中的作用仍只是一条取得最低态排序的shortcut。

旧Goal第十节B末行要求与核心目标有关且有“实质规模”方法类、
精确可行性分界或不同可推进机制；C.2要求净关键输入，C.3禁止
多份小障碍累积冒充核心瓶颈解决。529已付精确分界，但没有给
低奇态的完整signed joint domination、prime/pole全域比较、
prolate与真实最低态的桥或新的独立几何极化。
signed方法、新非局部锥、非保正自伴算子的一般最低态比较均未被排除。

基线004已经明确原型不能直接套Perron且须处理三源；529把这一警告
严格量化并确定全部支持阈值，是实质澄清，仍不足以据“完整核”三个字
自动升级为整个核心方法类边界。建议Goal保持active。
若将来要以障碍终止，至少须说明当前主要可行完成策略为何不可绕过
被排除结构，并检查剩余非局部／有符号来源；现在没有该证据。
不要求证明所有方法都不可能，但不能倒填较容易的终止尺度。

## 2. 因子2后哪些输入不能消费

normalization-erratum给actual K(t)=2theta'(t)，
m_actual=-gamma-pi/2-3log2-logpi=2m_half。
其对象检查是actual `-w_real` 和原文(3.8),(3.19),(4.4)。

- 023的half digamma最低点、单函数界本身保留；不能原数直接作actual
  arch下界、bad-frequency threshold、quadratic curvature或gap预算。
- `archimedean_multiplier`、`dirichlet_archimedean_multiplier(t,0,1)`
  及其谱底helper目前按half约定解释。不能因为函数名叫archimedean，
  就与真实矩阵`-w_real`互换。
- `build_polarization_defect_matrices`使用actual矩阵却默认m_half。
  P−V代数消去仍正确，但不能消费“arch−m_half是已知非负块”。
  022/023以及涉及该正块的compact Hodge/threshold下游若重新准入，
  都须先核准确实际入口、底常数和完整预算；不能只乘2后宣告历史认证恢复。
- 004、005等显式尾／multiplier预算若把half符号实例化到actual，
  需逐条重新实例化；004的abstract minmax和其直接矩阵数据不因此失效。
- 016/017的graph完成平方、degree线性损失和P−V代数保留；actual正块
  成立需用actual m，不能仍用旧半谱底。
- 030的PNT边界lambda主阶、031/033的prime/pole显式来源不靠half修正获得
  新算术输入；arch O(1)性质仍成立，但涉及数值常数须核实际归一化。
- C001冻结矩阵、527/528和529是从q_nm/actual rho原空间推导；不因helper
  错误自动重跑或抹掉。它们不提供上述半谱底正块。

当前审查只定位这些消费接口，不声称已遍查所有脚本／历史预算。
归一化纠错是防错误消费的前件变化，不是新正性瓶颈被解决。

## 3. 主代理选择：真实Sonin正来源的同源trace差准入

唯一下一合同应从独立已证正来源开始，而非继续核侧shortcut。
主代理选择重新消费Connes–Consani的archimedean positivity原文，
核准确支持、Mellin消失、projection定义及trace/error，再同actual QW
建立**此前未付的**同源差比较。这不是新文献发现。
10月12日supplement已核来源摘要；现在必须回到原定理／证明，
重复摘要没有数学轮价值。

本审查核读 [2026综述§7.2](https://arxiv.org/html/2602.04022v1#S7.SS2)：
所用S是真Sonin orthogonal projection；列出的g支持窗为
[2^-1/2,2^1/2]，有两个transform消失条件，控制的是实位型，
不直接控制加入prime后的完整Weil型。这些限制是准入前件。
§7.4的另一trace算子不能沿用S的正投影解释。

**一轮可执行任务与最便宜负对照：** 冻结一个实光滑对数源
g(y)=D(D+1/2)eta(y)，eta in C_c^infinity((-log2/2,log2/2))。
积分分部直接给hat g(0)=hat g(i/2)=0，源非空且不使用ζ零点。
先按原定理精确确认这一Fourier/Mellin约定，不用消失条件的字面相似
替代源函数识别。若源对象一致，则取两个真实multiplicative translates
g_0(y)=g(y)、g_a(y)=g(y-a)，先a=log2；平移保留两个消失条件。
每个单源的自相关仍在原窄窗，跨源相关可触及实际p=2原子。

构造同一个2×2账本：actualGamma来源、pole来源、全部prime来源、
Tr(theta(g_i) S theta(g_j)^*)及来源差；先解析核q_(log2)交叉和所有
trace域／traceclass条件，不做大N或扩大pilot。
这一账本的目的仅是检验能否产生新的signed trace差恒等式／估计。
每条单源正性不能自动极化成跨两个远移源的positive matrix：
它们的线性组合不再满足窄支持条件。必须为该差matrix另给独立来源。

可以把negative control严格缩成只有p=2的实际域：令eta支撑(-b,b)，
2b<log(3/2)，两源中心置于±log2/2，选择

    log2+2b<L<log3.

则2<mu<3，完整actual prime只有k=2。每个单源的support宽2b<log2，
故prime diagonal精确零；两源同形相隔log2，prime off-diagonal精确
为−w_2||g||²。双方hatg(i/2)=0使pole矩阵全部精确零。
actualGamma与真实Sonin trace的cross及difference仍须原件算清。
这不是假想prime模型，也不是改变原子位置；已经给非空完整prime域。
若最终只借Gamma的高频uncertainty粗下界盖住一个有限w_2，
则属于旧预算准入检查，不应宣称找到新的Sonin算术桥。

**负对照要求：** 把上述两个源移至同一支持窗边界外，或只改变两源
相对平移使实际p=2重叠发生，而保持单源正trace及消失条件。
如果“单源正trace→完整2×2正性”的步骤不给这条prime交叉任何费用，
它已失败于对象／量词，不能靠再写Schur条件挽救。
合格的新增输入必须给完整同源difference的确定符号／定量费用，
并说明可消费域非空；若只是原实位正性或条件matrix inequality，
一轮后停止，不自动打开更多Sonin字段、RR或λ增长预算。

原窄窗下卷积支持至多log2，prime只有零长度边界，所以“不含prime”
结果不能宣称非空的完整prime适用域。两源移位是最便宜真正prime
准入门槛；即便这个二维门槛通过，完整补空间与增长支持费用仍未付。

去极点B保正、rank-two secular条件和TP2背景顺序均不选为新主线。
我初提B的短时ordered minor检验仅能继续排kernel-side shortcut；
Gamma-only可能已失败，且没有独立算术正输入。撤回它作为下一合同
的建议，不消费为研究轮，也不制造一个容易完成的新宏观Goal。

## 4. 两个看似新方向已经不合格

精确指数锚的prime漂移可以写得非常具体。令e_+(y)=e^(y/2)在I外零，
d_+=ell−y,d_-=ell+y，则几乎处处

    (prime e_+)(y)/e_+(y)
      =sum_(k<exp(d_+)) Lambda(k)
        +sum_(k<exp(d_-)) Lambda(k)/k.

actualGamma作用则由同一rho的零延拓jump integral给

    (K e_+)(y)/e_+(y)
      =m_actual+int_0^infinity rho(a)
          [2−e^(a/2)1_(a<d_+)−e^(−a/2)1_(a<d_-)]da.

e_-交换两侧。这可以作来源复核，但靠PNT提取主阶只重复030，
把居中误差压到所有边界剖面的O(1)则重返031/033的RH等价核心。
因此不把“hyperbolic anchor漂移”单独推荐为新的1–2轮主攻。

prime删除的cheap模型对照也说明B一般保正不够：固定非负光滑bump g，
把它放在±(ell−1)，取实奇f_ell。K_actual能量因平移不变和
K_actual−m_actual非负，可用固定常数统一界；而|S(f_ell)|²为
正常数乘lambda+低阶，故去prime后的W奇能量趋向−infinity。
这只是去prime模型反证，不能作为actual W反例。实际prime边界主项
恢复的必要相消已在030，不能再次计算并记新成果。

## 5. 下一动作与未付条件

唯一下一动作：按第3节读取原始archimedean positivity定理的准确源，
冻结一个真正Sonin trace/actual QW同源账本与p=2两源负对照，
检验是否有新的signed trace差桥；一轮没有新桥即停止。
不用未知最低态，不扩大冻结样本，不以条件matrix改名替代来源输入。

宏观瓶颈保持：没有独立来源控制同一完整Weil型的关键signed联合能量。
529真正改变的是标准锥路线；归一化纠错改变的是旧“正输入”的可消费性。
这两个变化都须进入宏观复盘，但不等于长期Goal完成。无pending processes。
