# Macro21 支持：全源费用的成长范围与下一投入

2026-10-29；独立恢复任务 `/root/macro21_scope_recovery`，只写本文件，不改共同STATE、cadence、Goal、既存证明或13412-byte策略支持。旧三个handle在父现场确认已不存在；缺失的本支持文件由此次新任务实际重建，不能把旧handle的计划当作完成。

本稿开始时C065尚在review；定稿前已实际全文读取602的4966-byte笔记、9138-byte root记录、2164-byte结算合同和唯一cadence，确认数学已由root统一结算602：原3→4/history65→66/latest602，formal20保持。**正式macro21及4→0尚未执行。** 本稿是待root及不同macro fresh消费的支持材料，不自行归零，不把宽度常数整理另计数学轮。

## 1. 当前已闭合的实际责任

恢复时读README/STATE，运行research_state.py check后show；读完整G20261027、C065、AL、当前frontier和formal20。随后全文读16385/13097两数学稿、16049不同审查、1964最强方向、更正3417、重新准入3499及既存13412策略支持。旧585/587全文读取，589读取相关实际上界/量词段；不声称重审它们全部nested原始证明。版本表只认证本次消费材料，不替代数学论证。

602的对象是同一个actual Sonin投影、完整Gram逆与原源空间S_I=L²(I,du)。原物理H_x=L²((0,∞),dx)经酉log变换后源系数仍为r，无第二次半密度运输。低cutoff压缩C_p=LF_pL与source紧误差𝒦_{p,I}必须分名。已经root闭合的最强结论是

    ∀固定有界I，∀p≥pκ，
    ||𝒦_{p,I}−𝒦_{0,I}|| ≤ C_I(1+logp)/p，
    ||𝒦_≤1(X,I)||、||𝒦_{F_X,I}−𝒦_J(X,I)|| ≤ C_I(1+logX)。

pκ仅由固定实位谱隙选定，独立I。量词覆盖整个复L²单位球、任意频高和在该I内随p/X移动的源，常数不含源导数。证明直接控制overlap E_p−E_0，即source紧误差之差；不是先要求p>e^(diam I)才有定理。

实际ordinary trace在smooth/Dlog域仍满足

    t_p−t_0=−𝒫_p+(𝒦_{p,I}−𝒦_{0,I})。

𝒫_p保全部proper powers/原权，仅logp>diam I时其全部相关才exact为0。可见p也在紧误差定理中，不能被误列成指数多个未付head。全L²上消费的是source有界型的连续延拓，不能把两项可能无穷的positive trace相减。完整Γ/contact、proper powers及双pole按560原身份保持；这个分解没有删除目标的任何一项。

## 2. 同证明可读出的宽度充分费用

以下不是新的独立数学合同；它只检查602证明实际带入成长窗会付多少费用。记W=diam I、R²=||r||du²，κ=||C_0||<1。取本来证明中的固定pκ，固定arch resolvent及有限p<pκ的常数都可吸收进C_*，不依W、r、p、X。

源整体平移到[0,W]不改A_r*A_r。新输入为

    T_r=L A_r*A_r H_+=(E A_r L)*(E A_r H_+)，
    ||T_r||S₁≤W R²。

完整h(C_p) Taylor的全返回二阶余项由此为C_*W R²/p。这个费用只用traceclass×bounded，不含角截断/源导数。

物理T核为χ_r(log(x/y))/√(xy)，|χ_r|≤R²。除了矩形e^-W≤x≤1≤y≤e^W，还必须保留其真实三角支撑

    1≤y≤e^W x。

若把矩形内所有点都当有效支撑会不必要地再损失一个宽度因子。令B_r=T_r F L，输入为z∈[0,1]。利用上述支撑，直接得到

    |B_r(x,z)| ≤ (2R²/√x)∫₁^(e^W x)y^-1/2dy ≤4e^(W/2)R²，
    |∂_z B_r(x,z)| ≤(4πR²/√x)∫₁^(e^W x)y^1/2dy
                   ≤(8π/3)e^(3W/2)R²。

右侧在空积分区取零；x→0无需给χ求导。固定R_σ=1+S_σ的smooth核与其输入导数有仅依arch的界。左右dressing R_σ B_r R_σ在单位方形上只添固定积分费用，因此第一variation的输入C¹振幅可取C_*e^(3W/2)R²。原轴条带/一次IBP仍给(1+logλ)/λ；低scale项可用无导数的C_*e^(W/2)R²/p。

第二variation记V_r=h(C_0)T_r。h(C_0)的输出x导数是固定smooth核。对输入y∈[1,e^W]，j=0,1均有

    |∂_x^j V_r(x,y)|
      ≤ C_*R² y^-1/2∫_(y e^-W)^1 z^-1/2 dz
      ≤2C_*R² y^-1/2。

因此high-scale一次x分部后，y积分为∫₁^(e^W)y^-3/2dy≤2，费用甚至可取C_*R²/λ；low/reverse核在有限带上的费用≤C_*e^(W/2)R²/p。这里两个variation用的是不同坐标的C¹，不能把粗糙χ的导数隐含进去。

最后，固定p<pκ和empty项的完整overlap直接由

    |E_p[r]|≤2||h(C_p)|| ||T_r||₁

付C_head W R²。各个C_p严格gap及有限head是既有实际对象；head的个数独立W。对smooth身份先估计，再作source紧型延拓即可，不假各裸L²正迹有限。

由此，602同一证明足以选择一个很粗的共同上费

    C(W) ≤ C_* (1+W+e^(3W/2))，
    ||𝒦_≤1(X,I)|| ≤ C_* (1+W+e^(3W/2))(1+logX)。

这是**可用的充分upper**，非最佳常数、非必要lower，也没有证明actual norm和不可求和或发散。它补清证明的成长依赖诊断，不生成另一轮“成长定理”，更不支付长期Goal所需的有利signed净比较。

## 3. 自然共同成长时，这个上费证明了什么

取I_L=(-L,L)，W=2L，实际可见素数范围X≈e^(2L)。上节充分上费给至多

    ||𝒦_≤1(X,I_L)|| ≤ O(L e^(3L))。

该估计对pκ以上的可见p同样合法；不能说“因为logp≤W，所以定理不覆盖全部自然素数”。真正未付的是可用于目标比较的费用/符号，而不是该覆盖事实。

另一方面，585对固定r₀早有joint实际迹及完整紧误差至少c e^L/L²，589给相应fixed mean-nonzero量级upper；587给每先固定有限导数源空间的共同lower。上面L e^(3L)的粗upper并没有小到能在自然coupled尺度中与这些项作有利相减。两个方向不同：一个大充分upper不能证明实际onebody至少那么大，也不能据此否定成长窗上可能更好的取消。

尤其对嵌入I_L的同一个固定smooth r₀，533实际onebody响应已经绝对可和/有界。让包含它的环境窗变大，不会把它本人的旧有界费用变成e^(3L)。本支持只显示当前**整个成长单位球**预算还不足以付款，不混淆固定源和moving-source量词。

同样，602的fixed-I全算子差O_I(logX)确实统一两源配对与随X变化的方向；这是whole-unitball新后果。𝒦_J的符号及t_X−𝒦_J的独立实现没有由此付清。正迹和大正compact误差之间的核心相消问题仍在，不能把一个小组件剥离后就称剩余项有利。

## 4. 必须先扣的最强旧，及本周期机会成本

533属于冻结旧资产：同一physical源r=g、每个fixed compact smooth源已有p^-2 A[r]+O_r(p^-5/2)及single-p绝对可和，常数含Sobolev费用。534仅保whole-L²完整范数缺口，不能回滚533。故533＋585/589的j_X=t_X+O_r(1)、ratio1，以及极化533＋587的整个fixed finite-E共同lower/正谱/秩后果都是old0。4340准入、post601 root/fresh及AK相应“fixed-source强化率未付/归因可能新”必须继续冻结；更正不倒改原件或回滚两公式old0和601。

602新付的是无导数T自身S₁、完整resolvent余项和正确C¹方向合成后的全固定窗算子范数；不能因其p-rate弱于533就误判为同一个量词，也不能因叫whole就跳过Goal完成门。

四数学轮599–602的新增应按各自责任保存：599与600对两个实际positive谱模型完成目标反测，601关闭Haran2007 ordinary affine两整数槽独立性，602闭fixed-I onebody统一绝对费用。没有任何一步给同一actual非零primitive的principal/截面乘法/mixed RR；前三个候选的失败范围也不能合并成所有几何或positive D′失败。

因此四轮后及时macro21比再串两个single-p/rank/window变体更有价值。原whole leading4/5仍是542＋555→557的**负惯性UPPER**，537/538只fixed17/16，安全高频运输的既有量词照旧。长期关键principal/mixed、危险signed core/cross、通常Ξ均未移除。局部统一onebody费用确实改变；长期关键瓶颈和三个Goal完成门都未改变。

## 5. 主线、现实备选与唯一下一动作

建议保持同一个非零primitive的算术principal/sections/mixed作为长期主责任，不自动准入继任数学/source合同。当前策略支持13412的条件应由root依实际602记录解除，原历史条件稿保持原字节。

| 选择 | 目前实物与缺口 | 改变选择的证据 |
|---|---|---|
| 不同实际relative primitive/Green载体 | 旧源商/fulljets、旧Green设施和Haran ordinary affine均已判定各自范围；尚无新r→D_r/整数principal边 | 明确X/pair及独立源公式，先全405关系/平移、537非根和coverage，原du/Dlog/强尾，再有同对象两源mixed责任 |
| 实际coherent signed核心比较 | 560完整对象、602低阶隔离均可用；但𝒦_J定义本身不是新输入，有限base dressing也不能免费继承固定F的C¹或统一gap | 一个真正不同的同源两源响应/严格身份，有原norm净费，并能改变危险core/cross或自然共同成长比较；须胜过533/585/587/591等强旧 |
| 独立positive D′生成规则 | 证书拓扑合法，599/600只停止具体族；没有新的实际生成式 | 独立规则及全部fixed compact complex卷积平方的完整signed缺陷消失；不强加逐层Pan/ordinary trace，但也不以membership假设代付 |

此刻没有新的实际公式通过这三句input/test/strongest-old-net准入，故**没有已经获准的数学或作者章节继任**。不能把“进一步控制𝒦_J”改名成新合同，也不把C(W)常数优化、single-p rate、一般base、第三prime/rank或另一个source query队列自动列为下一轮。

**唯一已能执行的下一动作**是完成602＋实际formal21的准确范围保存/看板/文献scope/检查点，正常main同步并独立核actual HEAD/ref/commit/tree/soleparent/路径/clean。正式21仍须root及不同macro fresh消费后才归零；本稿不提前认证发布。

发布后的研究恢复须先做一次有止点的**实际公式建设准入**：只保一个候选对象，先产出完整actual family/source map、一个能改变选择的便宜负对照、以及扣强旧后的条件净后果；在这些实物出现前不建合同、不计轮。若一次建设没有给出这样的材料，就准确记“尚无准入继任”，不换名把原未知𝒦_J预算当输入，也不自动串未定位论文/旧章。这是新数学尚未构造的状态，不是用户缺信息或外部网络阻塞，不能据此complete、pause或先标blocked长期Goal。

反事实很明确：上述任一新实物若直接进入同对象principal/mixed或危险core/cross，应立即胜过局部onebody常数工作；若只有逐fixed-r或fixed-E结论，则先按533及585/587强旧归零。不能用没有既成后继作为Goal已经达成的理由。

## 6. 文献、执行与版本

当前仅重用项目已付证明；没有新primary、作者PDF、章节或数值。本稿不改140条manifest，不把已有source proof登记成新外部论文。599 metadata、600 PDF1–4、601有限公理/§7及原额外曝光的历史范围照旧；全文许可不明继续本地ignored。

下面绑定定稿前实际读取的原字节。602/root/合同状态来自实际文件而非仅父消息；cadence读到4/history66/latest602/formal20。本稿自己不更新它。

| 文件 | bytes | raw SHA256 |
|---|---:|---|
| onebody-full-returns/cosine-return-large-delay.md | 16385 | 670c91b0d06bde3255ffb7aa43fa250f2f9c0f6ba728b8e7e78d9f9f8373f9b7 |
| onebody-full-returns/uniform-traceclass-cross-check.md | 13097 | 709df9ed1bad8f08cb71b15d6c63d685ad78c17a9ae86e3bbc1a5815eddcbe7a |
| onebody-full-returns/fresh-uniform-source-budget-audit.md | 16049 | b633ae282ea798533c680a75b8658f3e378730df3fd3f66f36ab0e7e344ab19e |
| onebody-full-returns/compact-error-versus-trace-direction.md | 1964 | 13d70ac72dc578d7987f68829e8a5d801e72a69c55a6a7654656e997189e174f |
| 本目录strategy-and-completion-gates.md | 13412 | 212fd3d54587cc621aad95e3e44fd0fa9b90a3aaf4e651b966fc8b3ca0f2fc18 |
| notes/602-whole-window-sonin-onebody-return-budget.md | 4966 | 09daf7df96092e17a80ded1d5b645715a07608e6f0e0410918209d5f5690a739 |
| onebody-full-returns/root-consumption-scope.json | 9138 | 6b3dae7660438cb79a40232c7d87e648afc15821a0c3ee32645bd9a77fb326a9 |
| goals/contracts/C065-whole-window-onebody-return-budget.md | 2164 | f61a822da11878e951c4307328862f162ff04f26e3150d241b389fc562e46f3e |
| goals/review-cadence.json（数学602后、formal21前） | 7007 | 9b7f56a6b2dfbeba6f9b8e915d2838d9eb1151b958d0be2da0cc36cbce9087ac |

本文件终稿；只写本独占支持，没有后台进程。实际正式macro/root消费、solecadence归零和公开同步均由父线程核证据后办理。
