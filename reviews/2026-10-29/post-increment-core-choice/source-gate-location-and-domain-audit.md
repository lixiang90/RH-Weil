# Osipov来源门：章节定位修正与实际域/商映射审查

2026-10-29；本稿是/root/core_choice_fresh的新限定任务，独占输出。此前13057-byte fresh-core-choice-audit.md原字节保持，本稿另核root追加1853-byte章节定位修正。G20261027/runtime1793085111、冻结0c4f、0数学及formal19/原cadence均不变；不建C060/597，不读源proof或第二paper。

**结论：定位修正成立；限定来源门应以source0停止。** 原目标一直包含主exact sequence，只是把它错放在Introduction。原件明确把Theorem2.1放§2、proof放§3；在独立定位、追加修正先冻结后，仅读同一原件的必要§2定义/主statement可以纠正这一位置错误。本次实际内容确有自然的∞组件→全adelic商映射，不能把它也称不存在；没有形成的是physical r→该∞组件的合法源公式及405 compatible chain。原statement的商群计算尚未给项目所欠principal/Green或mixed输入，不能从carrier继续向proof索要同一缺口。

## 1. 恢复与严格读取顺序

新任务到达后重新读goals/README和STATE，执行research_state.py check后show，恢复同一Goal/C059/Z与当前source阶段。旧choice稿只审过旧2649-byte门，不被拿来认证修正后的新内容。本分工不修改STATE、cadence、Goal、Git或任何旧稿。

先只读取旧门允许的PDF3及PDF4在§2前的intro。PDF3正文明确说明主Theorem2.1不在intro陈述；PDF4 outline明确把statement置于§2、proof置于§3。已实际目视PDF3原页，定位不是从parent消息推定。本文未把intro的数域(2)或surface-over-k的(3)类比当成算术主定理。

当修正稿osipov-source-location-correction.md实际落盘后，本分工全文读并现场核1853bytes/SHA745c9abe…ccb68，确认它先冻结、仍同一v2/P¹_Z/F/C基准、只许PDF4–8内的立即必要定义与Theorem2.1，任何proof/Example2.3/§3前停。随后才实际读PDF4从§2开始的tail、PDF5–6、PDF7必要定义与完整Theorem2.1 statement。

PDF7的statement已经完整结束；提取程序在Example2.3 heading前截断，所以未读取PDF8。PDF7的Remark2.2在一次文本prefix中曝光，仅作读取边界说明，不消费其compactness/§4指向来扩预算。另用pdfplumber只定位heading坐标，Theorem2.1始于PDF7 y≈245pt、Remark2.2始于y≈482pt、Example2.3始于y≈535pt；据此render并目视只至statement末的上部crop。没有打开Example2.3正文、任何proof、§3/4或引用。

另实际读root的osipov-source-read-record.json作scope对照。该记录如实注明root一次过宽返回曝光了PDF7末Remark/Example/§3heading及PDF8首1000字符preliminaries，并明确不消费它们为前件。本文不把root的曝光改写成完全未见；本分工自己的截断/裁切没有读取这些正文，root与fresh的实际读取范围分别保留。未审的主proof/§4分析不因此变成已付。

本次沿PDF技能作read-only提取与裁切渲染，不改写PDF；原件267569bytes/21页、SHA8491958e…100cc再次匹配。渲染缓存处于ignored literature/local，唯一研究稿修改为本文件，没有新query/下载/重跑Jensen或旧17件。

## 2. 同一门的位置修正为何不是新来源队列

原2649-byte门的数学目标是主exact sequence及必要定义，同时硬限§1/PDF1–4。实际位置证明两个定位条件不能同时实现。修正保留原稿、实际旧读取范围及未执行的目标，公开追加“§2必要defs/statement、PDF4–8上限、proof前止”，没有扩大到证明或另一个命题；新source域审查也单独输出。因此这是一项可核的locator纠正，不是以旧scope的PASS覆盖新scope，不是凭引言citation自动读后章。

如果只是希望从给定商群的存在进一步索要完整positive配对，那不属于这次修正；也不能以statement引用§3/4为由继续。此判断只允许现在已经执行的同一statement定位修复，不授以后一般扩章权限。

## 3. 固定基准符合本节列出的scheme前件

PDF4的§2定义X为二维integral normal scheme，X→SpecZ projective且surjective（由此flat）。C为reduced水平一维子scheme，其各integral component支配SpecZ，U=X\C为affine；F为locally free O_X-module。

固定X=P¹_Z、C=∞截面、U=A¹_Z、F=O_X(−2)满足这些列明条件：P¹_Z为正则从而normal的integral二维scheme，其结构态射projective/surjective/flat；∞为reduced integral SpecZ截面，补A¹_Z affine；O(−2)为invertible。这里是普通scheme/locally-free前件，没有把F假设为nef、positive Hermitian或已给Arakelov metric。不能因F degree为负而错误判它不在作者定理域，也不能因这些前件通过就认证任何physical-source/higher-intersection结论。

本节没有要求先给Weil型、Schwartz源或Π_F；也没有把本项目的physical窗口/谱高/算术height识别为F/C的twist。这些角色仍不同。

## 4. 真实无穷组件和两个商的准确类型

为避免pypdf丢hat的风险，下式已与PDF7 statement crop核对。PDF5–6定义的completed tensor是局部线性紧向量空间的limit构造；例如

    Q((t)) completed-tensor_Q R = R((t)).

它是formal Laurent域（负次幂只有有限项），不是任意C∞函数空间，不是收敛Laurent函数/Green current或已付physical L²。可有无限formal正幂尾，不能将essential负幂尾免费塞入。

记A=A_X(F)，A∞=A_(X_Q)(F_Q) completed-tensor_Q R，则原件(6)给

    A_X^ar(F)=A ⊕ A∞.

A_X,01^ar(F)按(7)由同一个A_X,01(F)对角映入finite/∞两腿；A_X,02^ar(F)=A_X,02(F) ⊕ (F_η tensor_Q R)，η为X的generic point，绝非405的Schwartz原像η。第二项按自然对角嵌入∞组件。定义

    Φ = A_X^ar(F)/(A_X,01^ar(F)+A_X,02^ar(F)).

因此一个**真实而合法**的arch-to-quotient箭头已经由定义给出：

    i∞: A∞ -> Φ，v |-> [(0,v)].

不能因为尚无r↦v_r，就把i∞也标作缺失。另一方面，因01关系同时动两腿，i∞的kernel/像不能任意用arch-only正则germ或一个未核子商替代；finite legs与对角关系必须保留。

PDF7在主statement前还定义A_C(F)，它由局部compatible kernel投影得到，并有

    A_C(F) ≅ direct-limit_n inverse-limit_(m<n)
                 H⁰(X, F tensor (O_X(nC)/O_X(mC))).

同时A_(U_Q)(F)=H⁰(U_Q,F_Q|U_Q)。Theorem2.1声明短exact sequence 0→G1→Φ→G2→0，其中

    G1 = [ restricted-product_(x∈D,D not⊂C) O_(Kx,D)(F)
           ⊕ product_(D not⊂C, f(D)=SpecZ)(Fhat_D completed-tensor_Q R) ]
         / [ product_(D not⊂C) Fhat_D + product_(x∈U) Fhat_x ],

    G2 = product_i (K_(C_i)(F) completed-tensor_Q R)
         / [ A_C(F) + (A_(U_Q)(F) tensor_Q R) ].

第一组Fhat_D按原(7)的规则映进numerator两腿，Fhat_x只映finite腿。右商的分母是A_C(F)本身的自然像，**没有**把它也tensor_R；丢掉这个区别会改变整/实关系与商。Φ是全adelic商，G2只是它的终端商；即便某个元素在G2为零，也不能未经G1控制就判它在Φ为零。

这都是给定sheaf的additive adelic group结构。01/02为加法子群，并非已经识别为本项目arithmetic divisors的multiplicative principal/Green pairs。由global sections或rational data给这些子群中的元素，不自动证明405完整Schwartz像为这些boundaries。

## 5. 本项目入口依然没有形成

在这份实际§2 definitions/Theorem2.1 statement范围内，未给出

    physical r=e^(u/2)f in all-complex S_exp -> v_r in A∞

的公式、finite legs或从一维Schwartz adele限制复形诱导的compatible map。原文输入是scheme/sheaf/adelic elements，不能把其中generic point η、formal参数t或section系数换名为physical源、u=logλ或receiver Fourier变量。

例如按r的Mellin矩任意组成formal Taylor序列，只有在所需真实系数域、局部/受限乘积条件及quotient maps均检查后才是一个元素；即使可编码，也没有付款使它消405全noncompact Pan/平移、保537非根及原du-Dlog费用。复杂源到实formal组件还需明确realification/complex角色，不能把real protorus当complex Hilbert空间。本文没有提出或认证这种额外编码。

本节也没有把Φ或G2送到具备独立positive mixed配对/整截面乘法的primitive类，更没有完整Γ/contact、全部properpowers与双pole的Weil身份。Intro对H¹-related protorus的描述及已曝光Remark2.2的compactness不能替这些箭头付费；其§4分析并未读，不从名称补上。

所以正确停止理由是：**actual arch-to-quotient map存在，但physical-to-arch及405 compatibility未在此门形成；主statement只计算给定sheaf的商。** 这不是“曲面或商不存在”、不是固定F类型错误、不是证明作者定理失败，更不是所有二维adele或relative/higher源都不可能。

## 6. 源门消费与长期边界

本次位置修正和原定义读取都是来源核查，0数学轮；外部Theorem2.1仅cited statement消费，未审proof。该首门依1853修正稿的原stop rule应source0停止，不续Example2.3、§3 proof、§4、2022中央扩张、引用或另一paper，也不调整F/C/field继续试。若以后有真正不同的actualsource chain，需按原长Goal重新准入，不能把今天未付bridge本身改名成输入。

Root另提出next-formal-mellin-source-admission.md的非canonical候选：在同一P¹_Z/ω≃O(−2)/∞对象上，以M_r(j+2)作formal正幂系数，J(r)=[(0,v_r)]。本分工只读取该新proposal的公式/门限作角色对照，未执行其membership、finite-jet period或405必要反测，未消费其正确性。该明确自造公式不归作者定理，也不继承本source-domain审查的PASS；须先独立扣519/520最强旧，再核实际商的读出和finite legs。通过real必要首检也不付allcomplex/du/mixed。它与今天“原章未给canonical physical入口”的结论不矛盾，不能被倒填成作者已经给出的输入。

原choice13057、原门2649均保持原字节，只由本稿对新增scope作独立有限重闭。没有新J_r/量化core后果，不准C060/597，不改变596已付邻接结果或same-source已付endpoint/K=P+O/587whole谱。算术primitive/principal/整sections/mixed、危险core/cross、成长Ξ仍欠；whole542+555→557 leading4/5负惯性UPPER不变，Goal完成门仍open，同实例运行状态由root现场核验。

唯一cadence仍6749bytes/SHA a5cfcd0ca0f2a4ad63f6c7b60d55c83024ebb86387f0a12a0b7b167e6f3cf600，2/history60/latest596/formal19，不重置、不算formal20。文献归档/manifest由root负责，本稿不增改。Root须实际全文消费此新稿后同步STATE执行阶段、准确读取范围及后继；旧choice的PASS不能替它。

## 7. 实际字节绑定与终态

以下只绑定新任务的输入身份，不代证明。PDF与旧稿保持原字节；crop只是read-only查看缓存，不作数学原件。

| 输入 | bytes | SHA256 |
|---|---:|---|
| goals/GOAL.20261027.md | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| goals/review-cadence.json | 6749 | `a5cfcd0ca0f2a4ad63f6c7b60d55c83024ebb86387f0a12a0b7b167e6f3cf600` |
| reviews/2026-10-29/post-increment-core-choice/next-osipov-arithmetic-quotient-source-gate.md | 2649 | `6082558a873052bb568c57326979db645967ee72b2d81b2a142b24044f71ac52` |
| reviews/2026-10-29/post-increment-core-choice/osipov-source-location-correction.md | 1853 | `745c9abe341462a2e6bd1c7ead186bb37302478696d172c6dd726d6a526ccb68` |
| reviews/2026-10-29/post-increment-core-choice/fresh-core-choice-audit.md | 13057 | `b437301c274943306a88cf398e69146e8573d361b8a38b4e168e7c174f1f782c` |
| literature/local/2026-10-29-core-input-choice/osipov-1801.02282v2.pdf | 267569 | `8491958ec6ff552aa1d3915ecb7f29a8a1bed4069292acac76a3b79c7b8100cc` |
| notes/405-f1-adelic-restriction-moments-and-radical.md | 14633 | `fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d` |
| notes/552-radial-adelic-green-principal-and-comparison-gate.md | 9192 | `670c05aac61921a4f36accc89638e2844fe7221df6341e4e7ff27964fb22d887` |
| reviews/2026-10-29/post-increment-core-choice/arithmetic-input-candidate.md | 11154 | `099e07320bce1a8d54d80bbab861b10994b5a5cebfed63a5fe9a8cdd3016ca0e` |

本分工终态：仅新增本审查稿及ignored read-only render缓存，无STATE/cadence/Goal/Git/manifest/旧choice修改，无query/download/数值/后台进程或自动后继。未读取PDF8、Example2.3正文、proof或§3/4；root据实际新稿消费。
