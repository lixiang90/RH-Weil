# 固定9/8 core worker：独立代码逆审

2026-10-29。结论：**当前修正并冻结的字节，未发现阻断一次既定 finite-comparison 尝试的实现问题**。本记录不执行448/224维trial、compiler、Gram或source数值，不证明finite sign或完整Q。Root另负责源/解析前件消费与实际运行；source-only成功不能自动付款。本子任务只写本审查，未改worker、副本、STATE、cadence、Goal或Git。

## 1. 当前版本与实际读取

恢复README/STATE、check再show、G20261027、当前C058、D20261029S和macro frontier，实际工作树/当前pending均核。逐段核 `scripts/weil_9_8_core_pilot.py` 全本、新inverse原件和设计稿；另核source 08的实际upper-triangle输出循环、tail packet的原列/index/640-bit对象。没有import原driver或第三方core模块。

最终消费的固定身份：

| 对象 | SHA256 |
|---|---|
| 当前core worker，29732 bytes | `d9ac746c3d56199ea65385f9883390c19a64b06ba8397f52ad96201d20485961` |
| `core-run-02/manifest.json` | `5974885eba88831106d3395adf908f73a8c3180671457a7233aff3e44d2b239f` |
| canonical core configuration | `c315a040c3412694f7010f81131d76c4ac808cef9e19a7b0214bcc9d3c86d290` |
| 新inverse数学原件 | `e60800f4b36e737d3bd13efa0bd57bcd0d799a79ac81a0e9313f20b73450af42` |
| source worker | `7589b854cbcd2f1c2fcdf0ecce60b614af7e1d73992b6f64719e1624a0ad0961` |
| source manifest | `15ae30f087481a40d9c9d6bf3ff517ea1e50aba04b3899fcdd049c55364511e4` |
| source configuration | `8e4e59c11469cf35e5ad2e85a433660e6720ebd322d7ffd5c87d805cf2c0d364` |

实现纠正已经发生在任何core科学stage之前：旧877f67e4版本把raw source存储误按lower-triangle读，会在order guard返回非必要NONPASS。实际07/08是 `i=0..447,j=i..447 step2` 的upper rows；当前reader已改为同一顺序，并对称填满原448矩阵。CORE改用core-run-02；core-run-01仅旧prepare metadata保存，不能当已执行失败或数学边界。当前审查不消费旧版本；上述两处改动与最终SHA均重核。

## 2. 源与stage链的绑定

每个科学stage读三份source receipts及对应packets：必须为同source worker/manifest/config SHA、SOURCE_ONLY_NOT_FULL_Q、output SHA及fullQ=false。Moments要求1024项/4controls/完整oracle，matrix要求151200/15centers/225pairs/9controls和完整oracle，tail要求896/4controls。True-moment1152/radius1098及Binet-once、新9/8/raw256-bit/tail640-bit、matrix→moment SHA链另核。

完整三矩阵各50400个canonical upper rows转为raw endpoint sums，分母S=2^257；异parity置零，两个224-sector的q_i使用**原Legendre degree** 8(2i+1)，不是sector内部重新编号。Tail按column-major完整896条读取midTwice=lo+hi，分母2^641；exact parity zeros、非synthetic及caps保留。Raw U系数36和平方分母2^1282与数学原件一致。

Core后继stage用前一stage receipt绑定packet SHA、同core worker/config和前一stage所有输入hash；当前允许输入集合包含这些前件，compile与gram的跨stage链不丢trial/source来源。每stage开始及完成再核input pins。Core manifest与worker显式两个SHA pins防止把旧prepared配置当当前运行。固定MATH SHA绑定所审代数记录，未导入旧μ/target/residual packet。

这里没有声称能对抗任意伪造receipt：其算术信任前件是**已审固定source worker实际产生并由root核过的hash链**。本worker不重跑source oracle，也不单靠receipt计数重新证明解析费用；这与其finite-only输出范围相符。

## 3. Trial、native norm与先于sign的inverse

Trial固定110digits，解新 `Q(8b−a)Q·(Z/R)=8Qa−18S I`，R=2^256；scale同时用于system和rhs，返回Z的量化正确。Cholesky只提议，不支付正号。Raw metricΓ=18Q^-1给X=Q^1/2 ZQ^1/2/R，完整Frobenius numeratorΣq_iq_jZij²及分母2^512正确。

y从同一实际Z的完整ν确定为最小2^k，k从0开始，故y≥1且整数，k≤37；这是一次已产生trial的有向上包围，不是参数搜索或旧y=8。Compile还独立重算ν及normPower一致性。源码Z cap、F/V cap均实际guard，未关闭旧assert来放宽含义。

令u=QZ，代码的u*au、u*bu和au+(au)*逐项正是数学F中的Z*QaQZ、Z*QbQZ、aQZ+Z*Qa。c=8Cw+(9y²+16y)2^549及V=QFQ+18cQ正确，Cw=2^769；V全对称和每列除q_j的整性实际核。W≥G>0来自已付M下界、μ1/8、实际norm和source误差的一般inverse恒等式，代码不以目标sign反推W的正号。

## 4. 两个compiler与小型独立实核

`coefficients()`精确清分母λ0后给六coeff，bit lengths为1029/9/1168/1007/746/2063，与数学原件相符。Direct的av_q是(aV)*Q，故其contraction确为(aV)*Q(aV)，没有把非对称av误作自伴。VQ^-1V的除法先有列整性；两套tail contraction都保两列完整贡献。

Combined另以k-major loops构造aQa及Yv Hinner Yv*；不调用direct的matrix multiply或intermediates。Direct采用dot-product顺序，目标在两个sector必须逐个比较224²个entries，再核对称及3200-bit cap。共同六scalar coefficients仍需数学语义审查；双实现相等不能单独支付正congruence。

本fresh另外实际运行**仅3×3**的精确fixture：加载guarded新worker，先核当前SHA；只在该内存module把` symmetric`的224维硬约束改成通用小维对称断言，其余被测数学函数未改、生产源码未动。取

    q=(8,24,40), S=2^257,
    a/S=[[3,1,0],[1,4,1],[0,1,5]],
    b/S=[[20,0,1],[0,30,2],[1,2,40]],
    j/S=[[-2,1,0],[1,0,2],[0,2,3]],
    Z=[[1,2,0],[-3,4,1],[2,0,-1]],
    tails=[(2,-1,3),(-1,1,0)], y=1.

该非对称Z下，实际inverse_integer的V对称/列整性通过，direct与combined全部9 entries精确相等。另用独立Fraction表达式从Γ=18Q^-1、C0=j/S+Uraw−λΓ−β0[b/S−aΓ^-1a/S²]计算 `T0(VC0V+18²CwV)`，T0=9·2^1282，其全部entries与程序目标精确相等且为整数。还在该小SPD system执行一次3×3 trial函数以核输出/非负normPower；未执行真实224维trial。

## 5. Gram与失败方向的符号范围

Actual K的max-bit-length只作一次确定归一化b，固定256digits提议K/2^b−2^-480 I的Cholesky，再量化到2^-512格。它不继承3353-bit观测值、不搜索精度或shift。

Exact残差实现逐entry计算

    Rcert=2^1024 K−2^b FF*−2^(b+544)I。

544=1024−480，故diagonal payment与proposal相符。真实checker总是核完整224行；仅mutation反测允许在第一失败行早止。全部row sums严格小于d=2^(b+544)才给该sector整数sign；real Gram同样支付complex向量正号。Factor F00加2^600的反测须实际拒绝。程序若首sector失败立即停止，不把另一sector叫已执行。

Failed-pivot向量由leading Cholesky的转置三角系统提议，原K上的v*Kv用exact整数重算；只有实际负数才标`actualFiniteTargetNegative`。非负方向不算PSD，负方向也只是这个**充分比较目标K**，绝不是full-Q负test。代码packet和failure均保这项限定。

本fresh的小3×3 K=2^600 I实际经过Gram proposal及完整3行残差，strict PASS；F00 mutation实际拒绝。另以2×2 diag(-1,2)实际核failed-pivot路径，exact direction给负K值。它们仅检查实现公式/分支，不能代实际两224-sector sign。

## 6. 执行/隔离与未付边界

新程序无上游模块import、任意source dispatch或外部进程调用入口；只有prepare/isolation-test/trial/compile/gram。强制-I -S -B、assertions与显式hash；所有输出exclusive xb，碰撞拒绝；失败保存NONPASS/部分产物/access，不删改重试，不自动改数学配置。运行audit精确allowlist/标准库范围，拒绝socket/process/ctypes及未知fd。它是已读Python程序的audit hook，不是OS syscall sandbox或任意AST纯性证明。

本审查没有执行新的core isolation-test，不能把source worker已有三项拒绝当core实际结果；root运行前仍应执行当前core-run-02隔离门并核actual receipt。Source packets的完整source费用、root analytic closure、当前core完整trial/compile/Gram均不是本fresh的新成果。数学原件/SHA绑定不自动证明原du/Dlog、完整Γ/contact/pp/双pole、δ/rank-two、576核和全cross/complement前件；这些必须由root原消费记录闭合。

当前可给的是一次既定配置finite-comparison执行的代码准入。成功输出仍是FINITE_STAGE_PASS_NOT_FULL_Q、fullQCertified=false并要求root闭合解析前件。没有完整9/8正窗结论、没有595或数学轮结算，也没有primitive/mixed或成长core/Ξ关键瓶颈变化。所有长期Goal完成门保持原责任。
