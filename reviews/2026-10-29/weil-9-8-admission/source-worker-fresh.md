# 固定9/8 source-only worker：独立实现审查

2026-10-29。结论：**当前固定字节未发现阻断一次source-only复算的实现问题**。此结论仅涉及准备好的六模块与新worker；不声称新数值oracle已经通过，也不授予inverse/core/Gram或完整Weil正性。root另负责数学准入和实际运行。本审查不执行moments、matrices、tails或core，不改STATE、cadence、Goal、Git、worker或副本。

## 1. 实际对象与版本绑定

已恢复README/STATE、check再show、当前Goal/C057历史主合同、最近R决策及宏观前沿；实际工作树显示新C058准备中。长期Goal的同一冻结基线、完整完成门和暂停路线均保持。当前候选是原du的H=L²((-9/8,9/8);C)，raw基φ_j=P_j(u/L)、Γ_jj=2L/(2j+1)=18/[8(2j+1)]。有限源近似不等于原zero-extension Dlog全型正性。

逐段读新worker全本、六副本全本、designer报告、manifest，读原件对应语义和被删legacy入口；不是只相信patch说明。当前绑定：

| 对象 | SHA256 |
|---|---|
| `scripts/weil_9_8_source_pilot.py` | `7589b854cbcd2f1c2fcdf0ecce60b614af7e1d73992b6f64719e1624a0ad0961` |
| ignored `pilot/source-manifest.json` | `15ae30f087481a40d9c9d6bf3ff517ea1e50aba04b3899fcdd049c55364511e4` |
| canonical configuration | `8e4e59c11469cf35e5ad2e85a433660e6720ebd322d7ffd5c87d805cf2c0d364` |

轻量独立核查实际以`python -I -S -B`加载guarded**新worker**，只调用其`patched`/AST检查与hash函数：重新从六原件构造副本，在内存比较全部副本bytes、原/新SHA、bytes与完整patch列表，六项逐项相等；不调用`prepare`或任何science入口，不写新副本。各原件SHA与worker固定pins、manifest一致，来源同b6cd2183c1e79c6c27a34267812a7b2d73ed1b59。

| 模块 | 原bytes | 副本bytes | patch记录数 | 当前副本SHA256 |
|---|---:|---:|---:|---|
| 01-check.py | 19504 | 13581 | 8 | `8d2e73a49846272f7fadeb037e1efa44daeb84318354f5c53c502c44d28bb288` |
| 02-produce.py | 8633 | 6946 | 5 | `792ee1c93291459ca903b6f4f5e3c4f051f2463a1a020eac756b13fa6b913337` |
| 07-check.py | 26727 | 19517 | 31 | `85fcaaefd2d752a8401b9f7686c1c8779282c2cc21504129aabda7d1e37a83de` |
| 08-produce.py | 13345 | 9863 | 20 | `ae0f487544c203905faecbb78b30f94fb16fe4f2f63c6b9846ca13ea673ba2b7` |
| 11-checker_quotient.py | 8059 | 7899 | 6 | `ea6f8ed0e2780aa2835bb75f1a7e08fd807220ac4eb1b14f8c6aa0834e331af3` |
| 12-raw_column_producer.py | 5581 | 5460 | 3 | `a8a67b4e08d540f51e152fe05bd19d77ae69fc618e4d6c08cb24c730b3afbb9c` |

每个replacement带准确hit count，去legacy片段带hash；没有全局替换17。07移去旧moment路径和读packet helper，08移去旧momentSHA/width==3 helper；01遗留旧PRODUCER_SHA是未被当前纯函数引用的历史常量，新运行实际消费worker/manifest对六**副本**的hash，不从此常量继承旧PASS。

## 2. 新算术范围与原norm运输

07/08的非零字典完整为±log2、±log3、±log4、±log5、±log7、±log8、±log9，加0项权7/2共15项。producer用log9=2log3，checker独立直接log9；两者对9的Mangoldt均取log3，weight是−log3/3。其余4/8保log2，不能以logn代Λ(n)。各有向log10>9/4门足以排全部n≥10；2至9中其它非primepower不列入。n=9的真实center误差仍须运行verify_centers完整验证，并非由本代码阅读先支付。

M²由全部225 ordered pairs及三重交集I∩(I−a)∩(I−b)产生，包含0和空交集，未换成压缩矩阵A²。A由a=0行的全15个shift形成，只取第二个weight正确。B重建保one-sided endpoint与recurrence中的trace乘积，18/8正是新2L的系数。fixture独立要求正确宽5/4，删一约束的错误宽7/4须拒绝；不把旧9/8 fixture当正窗定理。

代码中L_CENTER/LN=18·2^2044=9·2^2045，对2048 grid精确表示9/8；seed积分的18/16、trace的18/8均对应原物理L。完整Σ|w|上费改11，checker在14非零weight的每个±1grid误差上付款，zero weight本身exact；producer多付zero的1grid仍安全。实际全center containment与质量guard尚待运行。

J0闭式系数正确同步为18²=324、(2ΩL)²=576²=331776、midpoint分母2^1153和L²=81/64。1153来自1152-bit interval endpoint和的中点，不是digamma中的s=1025/4；保留source积分内部1025是必要的，不能全局替换。两独立seed结构均更新同一系数，raw L²只乘一次。

raw Γ=18Q_d^−1，Q_d=diag(8(2j+1))。对raw midpoint半径width/2^257，原norm的行费为Σwidth·4(2i+1)/(18·2^256)，与07:371–375及08:280一致。每矩阵50400 stored cells、448全行、100576 expanded cells、99681 updates的域保持，三矩阵总151200。这个算术检查付的是source/matrix rounding上费；kernel全算子误差与analytic source-center Lipschitz费另由root闭合。

## 3. Moment精度与Binet对象没有偷换

01/02严格参数均为output1152、radius1098、producer6144/checker6400；1024个q不变。输出转换和896 magnitude guard均更换到1152，两处控制用相同单位。width≤2^55在2^1152输出格上的midpoint radius≤2^−1098。canonical decimal cap400足够覆盖1152-bit grid乘896；没有旧hi−lo==3的捷径。

01的checker用逆Horner端点series、独立Bernoulli三角法及理性复幂，02使用不同组织的正向series/递推，互不import。真实Binet remainder仍在02:202–203的`m.sym(theta,delta)`和01:229–235的积分remainder中分别作为各自oracle的一部分付一次：新packet的对象是**true θ_q**，不是finite D_q。当前1152 oracle若通过，后续kernel预算消费true-moment radius即可，不应再追加Binet。

新worker先实际生成rows，再运行complete_oracle/check_rows及四个mutation controls；同宽shift2^224输出单位远大于允许radius，仍在新magnitude域内，并要求具体落入完整containment拒绝。所有1024个独立包含和width仍须实际通过；读码没有预付working precision足够。

matrix入口不再仅取rows：它核同worker、manifest、configuration digest和moment输出SHA/complete checker receipt，严格核新packet键/参数类型和值/output1152、Binet-once和fullQ=false，再加载07/08。因而旧1024 packet或只改L标签不能合法喂入新576系数。每次源/输入开始、完成的hash复核将字节变化判失败。

## 4. 两个有限checker的覆盖与控制

矩阵generator完成A/B/J0后，checker独立log/root/centers、全pair seeds/closed kernel seeds、expanded oracle和每项containment。它通过`verify_packet`核新schema、完整parameters/sources、identities、error和conventions，完整调用九个原mutation controls。缺row、错parity、缺center、删pair、非零prime置0、错overlap、删/缩error和同宽shift均保留；最后一项必须具体触发`matrix interval fails complete independent containment`。调用路径没有跳过第三矩阵或另一parity。

tail两模块按实际参数L9/8计算argument576和ΩL²=324：producer是directed seed recurrence，checker从whole-factorial quotient独立计算896个coordinates，448 parity zeros必须exact零；δ原位保留。输出640/working2048不直接当精度证明，每项都核raw radius2^−524和完整包含。新增四控制为缺coordinate、改mid、非零parity和同宽shift；后者保持width/mid关系并须具体触发`INDEPENDENT_ENCLOSURE_NOT_CONTAINED`。这些控制与science本体在本审查中均未执行。

tail replay的normalized column/rank-two标签改null，声明仅raw列。全band sinc Taylor、Machin、normalization以及新81/27 rank-two和σ须随后按root已审公式与实际raw精度消费；不能以source replay原名声称fullQ。

## 5. 实际隔离记录与执行范围

worker只有prepare/isolation-test/moments/matrices/tails入口；没有core、inverse、congruence或Gram。强制-I -S -B、assertions，所有副本移去legacy main，compile optimize=0并以非__main__模块名加载；不import原run/stage/scalar/reproduce。AST限制是结构门，实际安全判断还依赖本次读过的固定代码；不是对任意Assign表达式的形式纯性证明。

科学stage必须显式worker/manifest pin、固定configuration，并核六副本当前bytes/shape。文件在固定root内，无符号链接；运行后只允许精确source/当前input读取及stage独占packet/receipt/failure/access写入，未知descriptor、网络/process/ctypes拒绝，标准库受限范围允许，输出用exclusive xb。当前代码没有删除、覆盖或执行外部命令的science调用。失败保NONPASS和原有部分产物，重跑遇既有输出拒绝，不自动提升精度；preflight失败在算术前发生，需root launcher保存终端错误。

实际读取root已经执行的isolation-test receipt/access：worker/manifest/config/source六hash全部匹配本审查；startedAt为2026-10-29T01:39:19.870221+00:00，elapsed约0.0244秒，numericExecution=false。outside-read、socket.__new__、subprocess.Popen三项均按预期拒绝，access明确只这三条expected violations；没有科学数值产物。未重复执行它。此证据只是已审Python程序的audit-hook检查，非OS syscall sandbox。designer稿中“receipts为空”是prepare检查时的历史，不是现在的实时状态。

`git check-ignore`实际确认manifest和source副本被literature/local规则忽略；没有stage这些原文。当前成功标签一律SOURCE_ONLY_NOT_FULL_Q，analyticErrorFeesPaid=false、fullQCertified=false、coreStageAdmitted=false。若原source局部checker字段为PASS，含义限该有限算术子检查，外层未继承旧Theorem B或RH的PASS。

## 6. Root消费时必须保留的边界

本审查支持一次**既定参数**source-only尝试的实现准入；不证明该尝试必成功。有效新结果须依次有当前science输出/完整containment与controls、root对fulloperator误差/原norm/domain的消费、新μ inverse order、新正congruence、全部finite Gram residual和full complement/cross。三个source stages通过也不等于finite target正号，更不等于ALLDlog完整Q。

源恢复/新wrapper/同一般定理的scalar代入不独立计数学轮；成功全证书若日后严格扩大17/16固定窗仍须与strongest-old比较，并单独报告算术primitive/principal/mixed及成长core/Ξ瓶颈没有因此移除。尚未消费旧μ29/32、旧target系数、retained sign packet或任意新有限正性。无本子任务pending进程。
