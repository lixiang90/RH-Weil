# 同一595方向：实际physical Llow的独立重放与范围

2026-10-29。限定结论：**同一映射源的真实Llow Rayleigh商严格大于2^-62，而本次P0在对应方向严格为负。** 这是新点态诊断，不是whole Llow PSD、9/8全窗coercivity或独立inverse损失归因。本fresh没有调用root脚本的calculate/transport，没有重跑source、trial、compiler、Gram或更改参数，没有改STATE/cadence/Git。Root仍须消费本原件与独立JSON后结算准入门。

## 1. 实际对象、恢复及字节

已恢复README/STATE、check后show、G20261027、停止的C058、D20261029T、宏观前沿和工作树；当前仅为595发布后的同v准入test，cadence1/history59/latest595/formal19。逐段读root physical-map/error、strongest-old9121、codefresh7699、冻结next admission及595原root的对象/误差/符号链。Goal原冻结0c4f与主primitive/principal/mixed、成长core/Ξ责任保持。

实际主输入：

| 对象 | bytes | SHA256 |
|---|---:|---|
| root actual physical-lower-scalar.json | 116531 | 310ed2f88057da1067cf3bd33ba133425300741163e94bb47599feb9aa7646a7 |
| root scalar程序 | 8953 | 322756691b82f70a0866bd6da28ff4f60a35020126f8deb55c495127bc930671 |
| 595 root消费 | 11597 | 7333762b917efbd8fd92b95a177576eea92a7a6f231d8ff7236dca7cdf93a7c3 |
| 595 compact negative witness | 101277 | 81bf3deaee393796bdf8b5a165904e188c657ff16176eaa9cb5eab1c22a0bab9 |

对root结果内全部48个input pins逐文件重新核bytes/SHA，计算后再次核SHA，全部匹配。它们覆盖595已付root/source/core/public metadata及实际source/trial/compile输入链；本fresh不以这些hash本身冒充重证oracle。actual a/b/j、tail columns、Z均直接从已生成packets读取，未从root结果反推这些算术输入。

本独立重放保存于[JSON原件](independent-physical-replay.json)：29118 bytes，SHA256为00b7349582c200b35a9b2c57be45a1d4e41127d760a078d3b5faf52252d669ec。它保存exact E0/N0、physical norm、完整有理区间、P0同源值、combined gap、48pins与12项数学/程序绑定。15项实际检查均通过，不使用Decimal决定符号。

## 2. 从raw Wr重算全部224个physical系数

读三个完整source数组的所有50400个upper parity entries，独立按(i,j)记录构造even224块；native degrees为0,2,…,446，q_i=8(4i+1)，Γ=18Qd^-1。Raw中心a,b,j的分母S=2^257，尾列midTwice分母2^641，raw U系数36。Z来自同一even trial，native Frobenius numerator重算匹配且不超过2^518，故actual y=8。没有用sector内部degree代原Legendre degree。

与root脚本的integer F/transport不同，本fresh直接从raw inverse expression作用于p=Qd v。设R=2^256，Y=Qd Z/R，Araw=a/S、Braw=b/S，Δ=(9y²+16y)2^-220，则

    Wr=ΓY+Y*Γ−Y*ArawY
       +8(Γ−ArawY−Y*Araw+Y*BrawY)+ΔΓ，
    u=Cw Qd Wr Qd v，Cw=2^769。

实际用Fraction向量分别计算上述八项及adjoint作用，不构造或调用F公式；Z不假自伴。得到的224个坐标分母全部为1，逐项与root保存的u整数完全相等，且全部224项非零。Actual source因此不是仅前14个physical modes：稀疏性只属于Kcert的合同坐标v。

595保存的方向是v/2^512，本次使用整数v；两者是同一physical ray，能量和norm平方同乘2^1024。由Γ^-1/2 Bc=Vint/(18Cw)，当前raw source为x=u/(18Cw)。没有省略一侧的尺度，也没有多乘L²。有限Legendre多项式zero extension是compact BV，Fourier尾O(1/|t|)，属于原Dlog；实际Llow在原L²(du;C)上有界，统一operator误差允许source依赖已生成数据。

## 3. 独立能量、原du norm与严格正区间

能量用完整even矩阵的对角加严格上三角累计，而非root的matrix-vector能量顺序：

    E0=[Σ_i(a_ii+j_ii)u_i²+2Σ_(i<j)(a_ij+j_ij)u_i u_j]/S
       +36Σ_s|t_s*u|²/2^1282，
    N0=18Σ_i u_i²/q_i。

实际E0、N0、N0/(18Cw)^2与root记录逐项Fraction相等，N0>0。Kcompact的j含原Γ带核与完整双pole，U用两条原尾列；没有放入λ、β、D0或W^-1再测一次P0。b只用于选择确切source，不向这次能量重复收εB。

按已付原norm误差，εlow=εA+εH+σ=2^-204+2·2^-220+9·2^-512。Actual source的Llow Rayleigh位于

    [E0/N0−εlow,E0/N0+εlow]。

两端均与root结果exact相等，且本fresh另以有理交叉乘严格核

    2^-62 < E0/N0−εlow < E0/N0+εlow <2^-61。

显示中心约2.716481090907042×10^-19仅说明量级；实际符号和dyadic界不是浮点结果。这只支付一个源。旧已付Q≥Llow+τ、τ=2^-49162可给这个具体r的Q(r)≥(2^-62+τ)||r||²；没有取得所有9/8源的coercivity。

## 4. 同一physical norm中的P0与合并gap

独立从595正合同变换推导规范，而不是用Kcert坐标Euclidean范数作跨对象比较：

    Kcert=T0·18²Cw² Bc*P0Bc，T0=9·2^1282，
    c=Bc v，||c||²=||r||²=N0/(18Cw)^2。

因此这个同一源的P0 Rayleigh恰为

    Nold/(T0 N0)，Nold=v*Kcert v<0。

本fresh实际Fraction核得

    −2^-67 < Nold/(T0 N0) < −2^-68 <0。

显示值约−3.49349682804228×10^-21。Actual Llow与P0在同一physical norm中的gap下界为E0/N0−εlow−Nold/(T0N0)，严格大于2^-62，显示值约2.7514160591874645×10^-19。Stored v/2^512的共同平方尺度在两边完全抵消。

该gap只归属于**合并充分损失**。旧关系C−P0=(A−W^-1)+(J−J0+εJ I)+α0I+β0(D0+εD I)≥0已经保留Schur condensation、inverse upper、source及α/β各腿；单scalar没有分摊这些腿。不能写成“已证明W逆界是唯一问题”，更不能用此正点推whole Llow PSD。595的exact负Kcert仍成立；只是该向量经正确source运输后并不是actual Llow的负源。

## 5. 净后果与计轮建议

这是实际新点态信息，不应称为旧定理直接推论或假装没有数学工作。它改变595负证书的允许扩张范围：不能借该向量宣称当前bounded lower operator本身失败。旧537/538不直接覆盖全窗非零多项式，强旧审计也没有预付此点值。

最强直接局部推论也应保留：同一native finite norm中，任意Hermitian加性修补H若满足本P0+H≥0，则在这个c上必须有〈c,Hc〉/||c||²>2^-68，因而||H||>2^-68；它不要求H正、局部或预先选定。当前实际C−P0又有operator norm>2^-62。这些直接来自上节同源Rayleigh，不是额外计算或另一个研究轮；对象仍只是这个固定有限充分目标及其compression损失，不能改称原完整Q或无界成长路线的必要修补费。

但当前取得的是冻结准入test的**正分支诊断**：没有whole Llow号、完整窗coercivity、whole方法类反例或主core前件削弱。冻结计划要求扣强旧后有足以晋级的净后果才另准合同，workflow§6的“新严格费用／新完整准入反例”不能仅因出现一个point value就自动套用；反过来也不能单凭“尚未建合同”决定0。决定性是本实际结果所承担的责任仅为同源消费诊断，没有支付负分支原拟的whole-operator边界。

建议按**新的点态准入诊断，0新增数学轮**保存，不开C059，不将595再结算一次；cadence1/history59/latest595/formal19保持。这个建议不是把新whole结果藏为source0，也不评价它为旧0。另派只读子核point_scope_audit核冻结plan/workflow口径，意见一致，未写文件/跑数值，已terminal；本段判断由本fresh对原文与实际范围负责，不以子核消息代授权。

当前same-v test已完成，应停止同方向/逐腿损失/参数诊断链，不能以连续0门绕过宏观审视或恢复C058预算。后继数学预算须另有实际独立输入或能改变主primitive／independent signed选择的具体test。Whole4/5负惯性UPPER及primitive/principal/mixed、成长core/cross/Ξ未变；本fresh不完成Goal、不改状态或计轮。

无未结束的子任务或numeric session。本文件与独立JSON之外无写入。
