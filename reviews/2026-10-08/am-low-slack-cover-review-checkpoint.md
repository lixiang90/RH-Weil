# 九点低松弛覆盖与相邻拼接：不同作者限定审查

2026-10-08，checkpoint_audit；保持原 AM 窗、权重、压力费及已准入的八点证书。
结论：低松弛覆盖、捕获程序及有限几何/部分付款限定 PASS；统一九点 δ=10⁻⁶ 尚未证明。
本审没有提高 c、零点比例或其他解析边界，也没有将可行闭 cell 当作真实零点配置。

## 1. 冻结身份与实读范围

canonical SHA 为 UTF-8，CRLF/lone CR→LF，保留 EOF。

| 输入 | 行／LF 字节 | SHA-256 |
|---|---|---|
| [持久收集及几何程序](../../scripts/am_nine_point_low_slack_cover.py) | 219／10565 | 0c203ae8d05796f73e5ca5018935067342a65f6a9eac3a800b5d36893cfde629 |
| [捕获及全部拼接报告](../../output/am-nine-point-low-slack-cover.json) | 6752／131270 | 628fdf422495f15f3b5f5ce7e035f8f439d43c0928883509f39034c87b0c64ff |
| [旧有限重放程序](../../scripts/am_pc8_finite_replay.py) | 280／13273 | 2db626d7c3fbcc1f6ced7580d0fe847fff743b1039aa58797392e9e05845600f |
| [旧连续语义审查](hybrid-original-am-eight-point-full-certificate-audit-pc8.md) | 228／17120 | 6cea584276b25cfd58fd353f8281986898833ae0a335c8f9033ba99a8154fb46 |
| [旧数值准入审查](hybrid-original-am-eight-point-numerical-extraction-review-pc8.md) | 141／14583 | 6a2a01e8a2474b29fd567c110575cd01ebe64cdbcc2cd090f17ff14044ce8e49 |
| [九点 lift 及无限尾](am-nine-point-lift-research-high-product.md) | 161／8823 | 88bd93c28ca361a5be70a48504a186378abba57031ac0f149b08eaf5a8acf045 |
| [实际隔离 Lean 副本](../../tmp/pdfs/am-nine-point-low-slack/Low805203.lean) | 11673／1036872 | c35a60cefbf034915af4ef4691ce75e9f491dc87e7876901ce2e5e283fffa455 |
| [实际隔离日志](../../tmp/pdfs/am-nine-point-low-slack/replay-log.txt) | 211／34455 | f983f2bf9467dd4c9f954953a83a8b12f85938ae1187f6be00db4120d0adc684 |

本轮全文实读新 219 行、旧 228/141 行和 scratch 收集器；九点 161 行及旧 280 行已全文审过并重核身份。
全部 70 个 cell 的 14 gap/42 span 整数端点及 70 个 reward 均读回；报告所有元数据、70 记录、289 拼接字段以 compact 形式核对。
隔离副本不另称本轮全文读 11673 行：按已审固定 core 逐字重构并精确核差，所改回调、参数 clone、二分 helper 及全部 41 表达式实读。
原 raw Solution 身份为 012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f；
原 admitted NumericCore raw SHA 为 f21a0d9f141a7807a6524f426b64a0c0b7b2e81e12581d3ec528f467e9bd1be3。

## 2. T 的完整连续外覆盖

令 c=805003/10⁸、θ=4/5、δ=10⁻⁶，并定义
T={h∈[θ,∞)⁷:F₈(h)<c+2δ}；强目标恰为 805203/10⁸。
各平方能量与七项压力费均非负。旧 cl=true COV 的 soundness 给一个相邻对能量≥c，
所以 F₈≥c+θB，其中 θB=8087/2500000>2δ；该分支没有把压力重复计入单对证书。
旧 large-gap 检验给 bᵢhᵢ≥c，其他六费至少 θ(B−bᵢ)；其统一最小值为
5053/1953125>2δ。因此所有 large-gap 分支亦不交 T；small-gap≤1/2 与 h≥θ 不交。
剩余只能位于旧 bad COV 闭区间的全部 32 个 root 域中，端点沿原闭覆盖保留。

在 h₆≥h₀ 的一半，walk 中 u₆<l₀ 的方向叶不可能含该点；已证明空 cell 的叶也不含该点。
原 walk 完整通过，故该点必到一个原 minorant 正值叶。若 strong=true，它整 cell 证明 F₈≥c+2δ，与 T 矛盾。
故 strong=false 且 oldresult>0 的记录完整包含这半个 T。另一半对整个七 gap 反射；F₈、b 和旧 root 家族均反射不变。
因此 70 个记录及其反射覆盖全部 T；无需在已跳过的方向叶上虚构新的 minorant。
反射为 gap r↦6−r、span (i,j)↦(7−j,7−i)，每个下/上端点随相应 span 一起搬运，不能盲目逆序 42 数组。
记录 cell 是 T 的外覆盖，不断言记录中每一点都满足 F₈<c+2δ。

## 3. 收集与已付 reward 的正确语义

固定 raw Solution 经旧 extract 加两份已审桥重建 core，hash 严格等于原 admitted core。
程序保留原 mcheckP、cN=805003、全部旧 root 和原返回 cursor；只 clone mcheckStrongP(cTarget)。
该 block 中仅一处 cN，被替换为 cTarget；其余值表、导数表、切线、Farkas 及 guard 字节不改。
因此沿旧连续 minorant/Farkas 证明，只将最终奖励比较换成新目标，适用于整个真实闭 cell，而非网格点。
oldresult>0 给原奖励已付；八次二分从 805003 开始，仅在实际 test=true 时提高 lo。
唯一奖励比较对 cTarget 单调；无论是否声称最优，返回 lo 始终有实际 true 检验或原 oldpass 作依据。
strong=false 只是原 minorant 未支付更高目标，不是 F₈ 的反例。

根线程实际 --replay exit 0；本审只读核其完整日志，41 标签严格为 large-gap7、adjacent7、cover-0…6、root-0…31，全部 true。
每个 LOWCELL 紧接一个 LOWPAID，共 70/70；与早先捕获顺序及最终 JSON 完全一致，无 error/sorry/panic/中断记录。
30 个旧桥的 axioms 输出仍为 [propext]；runtime 整数计算信任边界保持，不能称 41 个 native 结果都已 Lean kernel decide。
新 41 项复用此前准入的所有值/导数表检查，不重跑或冒充原 240 项全覆盖。

## 4. 相邻两帧与全部 sharp span 的精确拼接

对九点八 gap g，左帧是 (g₀,…,g₆)，右帧是 (g₁,…,g₇)。
六个共同 gap 为左 i=1…6 对右 i−1；十五个共同长 span 为左 (i,j)、1≤i<j≤7、j−i≥2，对右 (i−1,j−1)。
两帧 42 个长 span 去重后共 27 个；九点全部 28 个长 span 中仅总 span (0,8) 没有直接叶约束。
不能只比较六个 gap，必须保留全部 27 个真实 span；本程序正是如此。
以九个 prefix t₀,…,t₈ 表示约束 L≤tⱼ−tᵢ≤U，并额外加入全部 gᵢ≥θ。
使用 5SC=163840 的整数单位，θ 的下界恰为 131072，没有 ceil/floor 丢失连续边界。
每条区间对应两个 directed difference edges；负 cycle 证明空，反之最短路 prefix potential 给真实可行点。
Floyd closure 与本审独立边列表 Bellman–Ford 的全有序配对结果、总 span 精确端点逐字段完全相同。
总 span 位于 [−d₈₀,d₀₈]/(5SC)。本次所有可行区间上端≤已证明压力尾 Sδ=2870483/72245；
此为事后精确检查，未把 Sδ 舍入或以未验证筛选删 cell。可行仅是连续几何可行，不是零点配置存在。

## 5. 实际部分付款与未付范围

70 原始 cell 互异；加入反射后有 140 个来源标签、132 个互异几何 cell。
全部 19600 个有序标签对：六 gap 过滤后 422，十五共同 span 过滤后 289，完整差分闭包仍 289。
独立 Bellman–Ford 不导入根几何程序，实际 exit 0；所有 289 span/reward 字段与报告精确相同。
已捕获 reward 范围为 [805003,805201]。
九点准确恒等式是 F₉−c=(F₈左−c+F₈右−c)/2+2K(S)²。
若任一八点余量≥2δ，则九点目标已付；否则两帧均由 T-cover 捕获。
289 标签对中 78 对 reward 和≥1610206，即两帧平均≥805103/10⁸，已足以证明该整拼接域 F₉≥c+δ。
另 211 对仅凭这两个已付常数不足。最低 reward 和=1610006，发生于 left=112、right=42，
对应 S∈[97507/8192,101377/8192]；它仅证明所用 minorant 没有正平均余量，不能断言真实九点余量为零。
78/211 是带来源标签的闭域描述数量，不是不相交/互异真实域的计数；重叠点可使用多个合法证书中较强者。
剩余付款须在全部未付拼接域证明实际连续局部式，例如
(paid左+paid右)/(2·10⁸)−c+2inf K(S)²≥δ，或证明更紧的真实联合 minorant。
当前程序未认证此项；它也没有从普通 7/8 无零前件推出 δ。

## 6. 实际有限重放及结论

本审实际运行 C:\Python312\python.exe -B -X utf8 scripts/am_nine_point_low_slack_cover.py --check，exit 0：
`PASS captured data only; 289 compatible pairs, 78 average-paid, 211 unpaid; no uniform gain`。
同一命令加 -O 实际 exit 1，由所导入旧程序先拒绝：`PC8 replay requires assertions enabled; do not use Python -O`。
--check 只重新消费 committed captured data，核 script 身份、admitted-core 身份记录及精确几何，不实际重哈希 core、生成叶 minorant 或运行 Lean。
--replay 才重建隔离副本并实际执行固定 Lean v4.34.1；已核根线程这次真实重放与全部数据一致，本审未重复 heavy Lean。
JSON 的 uniform_nine_point_gain_proved 与 new_actual_zero_proportion 均为 false，lean_runtime_trust_required 为 true，范围正确。
限定 PASS：完整低松弛连续外覆盖、原 cursor 不变的实际捕获、全部几何拼接、78 标签域部分付款。
统一 δ 的唯一剩余任务是支付全部未付真实拼接域；此前比例和其他原目标均保持。
