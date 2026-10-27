# Goal 启动与 Borcherds 首门：独立 fresh 审查

2026-10-27。审查 `goals/GOAL.20261027.md`、`goals/admissions/A20261027-borcherds-principal-source.md`、STATE／单 cadence、既有看板与文献库保存机制，以及 `borcherds-principal-source-admission.md` 的限定来源消费。本分支只写本稿，不改 Goal／STATE／cadence／他人稿，不执行 Git 写入或同步。

先恢复 AGENTS／README／STATE，执行 check→show，再读新 Goal、唯一准入、最新决策和前沿必要范围。结构脚本通过不等于数学证明或运行实例认证。

## 结论

**限定 PASS，可据此完成启动结算与首批 GitHub 同步。** 新运行目标继承旧完整数学完成门及 0c4f 冻结基线，≤582 全部作为输入；Goal 启动、文献保存、来源审查、看板更新或推送都不完成长期数学 Goal，也不增加完整数学轮。Borcherds 首门没有取得新的经典物理源桥，正确停于指定章节，不准入 C046。

最终结算和实际远端发布仍由 root 完成；本稿不能替代 push／远端 ref、commit、tree 验证。本稿核读时，README／前沿／最新决策仍显示上一来源审视，STATE 已指向启动执行阶段；这属于在途状态。root 在结算前须同步入口、决策、唯一下一动作和新 checkpoint，不能留旧“runtime null／仅本地保存”文字作为最新状态。

## 1. Goal、运行事实及恢复绑定

* 原冻结基线仍为 `0c4f3a3eb609bb1d9564138fa4a35701f05605f2`；原 G20261014 的三类完整完成门在新 Goal 中保留。539–582 与 10-27 复核明确是已知输入，不能再次完成新目标。
* STATE 的 `goal` 为 `goals/GOAL.20261027.md`；实际 LF SHA 与 `macro_control.goal_lf_sha256` 相等，completion_audit 的 Goal／SHA 绑定匹配；mathematical_gate=open，final_execution_gate=not-eligible。
* 根聊天已由 root 实际调用 create_goal／get_goal 并报告同 thread 的 active 实例，createdAt=1793085111。这里消费 root 的实际工具观察记录；不以子代理自己的 Goal 上下文取代根实例，也不把 STATE 的文字当独立运行证据。
* 首门原稿记录该通知后的实际 §13 核读动作，而不是仅登记候选。该动作是来源准入，当前无新数学合同。

## 2. 四项用户要求

1. **持续研究。** Goal 有明确数学完成门、止／转向机制、具体源准入和合法备选；局部停止不等于长期完成。没有自动滚基线、自动恢复暂停比例／零区或用未知接口续轮。
2. **每轮同步。** 文件规定保存原件→root消费→STATE／单 cadence／看板／文献更新→检查→正常 fast-forward push→独立远端验证。来源0和管理启动也同步有价值决策；未成功不得称已同步。公开目标仓库沿既有 lixiang90/RH-Weil/main，当前用户直接请求构成授权，不由文件或附件扩大授权。
3. **文献库与看板。** 复用 literature 与 RESEARCH_BRANCHES.md。已核 literature/.gitignore 对 local/ 的保护；全文再分发许可不明时只本地保存，公开版本／URL／SHA／阅读范围。下载与研究消费分开。看板只反映路线，STATE仍唯一行动权威。
4. **4–8轮审视。** cadence 实际保持 rounds_since_review=5、历史46、formal cycle15；默认下一完整数学轮后审视，最迟8轮，组织／来源／代理／推送不另计。新 Goal 没有重置计数，也没有第二计轮器。

10808 代理只作为用户明确授权的网络故障修复，使用命令级配置；Goal没有设置未请求token预算、另开聊天或定时任务。

## 3. Borcherds 原件与源角色

fresh 独立重开[作者原版](https://math.berkeley.edu/~reb/papers/aut/aut.pdf) §13，核 Theorem13.3、Lemma13.1 及 Example13.5。作者首页日期是1996-09-29／corrected1997-05-29；1998是刊年。原件是64页，本地 PDF SHA、字节数与生产稿记录匹配。PDF本地 pypdf 不在本分支 Python 环境中，本次公式核读使用原作者 PDF 的网络提取文本，而非冒称本地完整重放。

核读的关键点：

* Theorem13.3 输入为指定格表示 ρ_M、weight 1−b−/2 的 weakly holomorphic modular F，并要求 m≤0 系数为整数。
* 输出在 C* bundle 上为亚纯函数，在群商上一般承载 weight c0(0)/2 及 unitary projective character；仅由产品存在不能宣称 base 上的 principal function。
* 原式保持 −4log|Ψ| 与 −2c0(0)(log|Y|+Γ′(1)/2+log√(2π))，不是完整经典 Γ(t) 乘子或 Qζ 的身份。
* 相同 line 和 character 的两个 section 之比可给 principal divisor 差；相同 weight 本身不支付 character。该条件机制不等于已经给出物理 r 的输入 map。
* Example13.5 的 J=j−744=q^−1+196884q+… 与本质为 j(σ)−j(τ) 的产品确认真实 principal 例，但 cusp 奇性和 classic 源比较仍须支付。

正维载体本身不认证承担经典源的非零 primitive 部分。原稿没有从本章自动领取整模型、finite vertical legs、全域费用或 mixed RR，这一限定正确。

## 4. 两个字面输入比较的范围

整值 principal-part 复线性候选中，a_m(ir)=i a_m(r) 与两者均为整数迫 a_m=0。这只拒绝“ALLcomplex r 的输出本身都满足整系数”的字面 recipe；不排先整／有理实现再复化的 divisor/current 或配对。

对 compact smooth r 的 arch-only transport，n=1 模态的 ∂bar 因子为

\[
i\pi\,196884\int r(u)e^{u/2}(1-e^u)e^{-2\pi v e^u}\,du.
\]

这是直接对该 Fourier 项微分；compact height 区间允许逐项微分。全 v 消失后，由既有 Laplace 唯一性得到 r(u)(1−e^u)=0，smooth r 只能为零。全 x 的不同模态不能取消 n=1 系数。因此537 compact非根在该**字面 transport**中未得到合法 weakly holomorphic 输入，不能在无输入时消费产品并宣称保非根。

405 全 Pan 是 noncompact；J 的负模态带 double-exponential 增长，S_exp 的线性指数矩本身不支付其全尾。原稿仅记录合法性未付，没有宣称每个实际Pan积分发散，也没有用空的 compact Pan 交代替真实全族。

上述为指定章节输入与旧582唯一性的标准直接比较。作为来源0消费是可限定接受的：它没有新增独立算术设施、费用或实质全域方法类边界，不否定未知的新 modular intertwiner／relative transgression／非局部或付费修复。若未来扩大为新完整方法类边界，则必须另按真实数学迭代准入和计轮，不能沿用本次source0标签。

## 5. 数学与运行的剩余责任

没有新的 r→合法F、全Pan actualprincipal／537／全源coverage、原du／Dlog费用或完整 Hermitian mixed 身份。strong-old whole4/5继续为负惯性UPPER，fixed17/16不外推成长／Ξ，actualq/core/coupling及独立primitive容量瓶颈未改变。

root仍需实际消费本稿、第一来源稿与文献／看板输出，保存唯一下一动作及真实pending，完成首批同步及远端核验。以上完成后只能报告 Goal 已启动；不得将运行 Goal 标 complete。
