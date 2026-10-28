# HNF原数据：同族强旧与标记前置咨询

2026-10-28；`/root/rational_old_admission` 本轮另行短咨询。原 geometry-and-actual-input.md 不改。本稿只核root拟定raw数据的类型及旧覆盖，不形成r,s reader，不执行数学合同／计轮，不web／新来源／STATE／Git。

## 1. 直接命中：这族raw矩阵已经在583实际使用

拟定column HNF为

 H=[[a,b],[0,d]]，a,d≥1，0≤b<a，ad≤B，L_H=HZ²。

对固定marked ambient Z²，每个有限指数子格确有唯一这种column HNF，指数ad；b<a是本column约定，不能与row约定b<d混用。它是合法有限算术对象，但**不是本库此前没有的raw族**。

[583 §2(4)–(5)](../../../notes/583-completed-modular-faber-source-and-native-green-transport.md)已经逐个整数m使用全部Hecke/isogeny矩阵

 R_m(j(z₁),j(z₂))=∏_(a'd'=m)∏_(0≤b'<d')[j(z₁)−j((a'z₂+b')/d')]，
 D_m=σ₁(m)，T_m=Σ_(k²|m)T_prim(m/k²)。

两者的明确字典是(a',b',d')=(d,b,a)。将ambient basis(e₁,e₂)识别为complex basis(1,z₂)，L_H由a与b+d z₂生成，其参数正是(d z₂+b)/a。因而不是仅因“都rank2”而猜相似，而是同一det=m有限索引集合的逐项重标记。gcd(a,b,d)=gcd(a',b',d')也相同。旧native原稿已按matrix entries gcd分解，保所有noncyclic重复及square-divisor aliases，不能把Smith content或“全矩阵而非primitive矩阵”当作首次补齐。

本次实际核读[583原稿§2相关段](../../2026-10-27/cusp-transport/native-products-and-green-tail.md)及其[fresh范围](../../2026-10-27/cusp-transport/fresh-review.md)：旧结论并非只数σ₁(m)，还有逐m真实norm多项式、全部边界、principal／Green及全源全尾的同对象运输。只比一个粗计数会漏掉这条更强旧链。

所以：det/content统计若回到σ₁、square-divisor primitive分解及其ζ(s)ζ(s−1)（初始Re s>2），应立即按旧0；若reader只经旧j／Hecke／principal-current数据因子化，应扣583的完整transport与closed-base停止，而非再领取一个“子格carrier”输入。

## 2. Gram、Smith及ambient标记要各保原角色

 G=HᵀH=[[a²,ab],[ab,b²+d²]]，detG=(ad)²；
 g=gcd(a,b,d)，Smith invariants为(g,ad/g)，且g²|ad。

这些公式相容，但G的det不是格指数ad；G的entry gcd也不一定是g²。比如(a,b,d)=(2,1,1)时g=1，而G=[[4,2],[2,2]]的entry gcd为2，不能从Gram content偷换Smith content。

G是本HNF基下的Euclidean Gram。它依赖marked ambient坐标／flag及本基的选择，不是GL₂(Z)-invariant数值矩阵。右换格基V给G→VᵀGV；一般ambient U又改变HᵀH为HᵀUᵀUH，重新HNF还要右换基。即使固定ambient欧氏度量，Gram的条目仍是chosen basis坐标。不能把root的flag称作canonical算术极化或已经下降到unmarked lattice moduli。

对当前a,d>0及b≥0的规范，G反而能恢复H：a=√G₁₁，b=G₁₂/a，d=√(G₂₂−b²)。因此“另保G”并没有在H之外增加独立raw信息。它可能使一个**不同于旧j-quotient**的marked reader可写，但这需要实际公式；目前不等于已产生新relative data／非零primitive或mixed身份。全prime valuations也是同一整数矩阵的函数，不自行带来独立约束。

b=0属于原族且不可删；若将allprime valuations作为reader输入，须约定v_p(0)=+∞并处理相关权／log项，不能把这项当有限height或直接用log b。B是整数index上界，与physical源u、支持L、频高及算术height费用分开。

## 3. 553／537能决定reader，尚不能决定未形成的raw数据

目前没有r,s公式，故没有可核的norm、principal或完整目标身份。不能仅凭有限B或Gram正定，就说整族被553排空；也不能据此宣称它躲过553。

实际reader若由有限个global连续线性源坐标组成，且精确消全405关系，则先用553的真实原域／有限norm门；若只在同一有限坐标后取非线性／quotient，仍应核Pan像与全源像，不因改标签免责。若进一步声称有限rank source读出精确因子化全部fixed窗Qζ，旧537＋finite-rank bump机制已拒绝。

这里“有限HNF索引集”**并不自动意味着physical有限rank**：一个H项也可能包含连续u积分或shift型双线性算子。所以必须先看实际source生成公式，不从有限数据条数推rank。同样，若规则仅作为正D′中间层，不要求逐层杀noncompact Pan；fixed测试收敛和global Hlog统一极限不同。完整Γ/contact、properpowers、双pole与未付signed缺陷不能留在公式外。

若只生成PSD Gram而没有到同一完整Bζ的identity／净比较，已有576–577／formal17的停止理由直接适用。若其实际r,s部分只是μ*log、prime-shift或old ratio/cofactor读出，就按原精确去重0止；raw格的几何名称不会改变这些系数。

## 4. 与既有T_B／rank2 holonomy的停止域

HNF约束是ad≤B、0≤b<a；不是旧T_B的a+b=c、gcd(a,b)=1以及固定log-linear／c^(-2)中心化reader。也不是原rank2连续ODE全z holonomy。**三参数／rank2这两个字本身不构成停止域包含关系。** 因此不应仅由它们的失败泛排所有HNF reader。

但若新公式事实上退回同一T_B经验−均匀核、只用det/count或原holonomy的同一source係数，则旧停止立即承接；不许调HNF权／cutoff／norm／level续参数。当前更直接的同族对照是583的全Hecke matrix数据，不能绕开它只和较弱T_B比较。

## 5. 前置结论与可判信息差

目前**没有新input**：只有已经同族的有限原矩阵、完整标记及明确的输出任务；尚无r,s reader或扣旧净量。它本身不比未知relative carrier多支付principal／mixed，也不比q_R接口多支付signed正号。

若root保留一次**原创公式形成**作为下一动作，其现实价值只在首门便可判定新reader是否确实使用marked shape／coupling且不经旧Hecke／det/content／primeleg数据因子化；这种明确finite索引可使系数／fiber核对较便宜，优于先设unknown RR／height。这个优势是可筛选性，不是新算术信息的证明。HNF族已旧这一事实应写入准入，不宜称“选择了一份新实际算术数据”。

一次形成最多交一份sameobject全complex两源signed reader、原domain/norm／全部量词与同目标字典，立即做normalization／fiber／target检查。只剩旧583数据重编码、σ₁/ζ乘积、μ反演、无identity的PSD Gram或未付Γ/pole即0止；无公式也如实未形成。不因为第一次失败再改HNF权、cutoff、norm或level。没有C050／587／证明预算。

本稿不假定这种新reader能形成，也不把未被旧规则排除的marked信息当作有效primitive。原Goal完成门、whole4/5UPPER及cadence0／历史50／formal17不动。
