# 固定9/8新逆比较与整数合同变换：独立 fresh 核验

2026-10-29。限定审查结论：**新 μ=1/8 的代数入口成立，没有发现要求沿用旧 μ=29/32 的数学阻断。** 下述结果均以新的原范数 source／column 误差实际成立为前件；没有执行完整 moments、matrix、trial、Gram 或参数搜索，没有证明本次 P0／完整 Q 的符号，也不登记研究轮。

## 1. 审查对象与读取范围

审查绑定原件 `new-inverse-threshold-admission.md`，11349 bytes，SHA256 `e60800f4b36e737d3bd13efa0bd57bcd0d799a79ac81a0e9313f20b73450af42`。没有修改原稿或 root 的其他文件。本独占 fresh 文件之外没有写入；未改 STATE、cadence、Git 或原来源。

实际恢复了当前 Goal、C058、D20261029S、宏观前沿和工作树状态；初次 check/show 遇到 root 同时写入的合同 status 词值不合 schema，已通知 root。Root 修正为 running 后，本次 check/show 均通过；这是执行状态修正，不是数学前件变化。

数学原始对照为恢复的固定 b6cd2183c1e79c6c27a34267812a7b2d73ed1b59 `publication/manuscript.tex`：raw normalization 367–387、inverse identity 391–411、一般 Certification Theorem 与证明 538–682、raw tail 1756–1792、Appendix E 1802–1892；另读原13／14的 q-grid norm、旧 trial 与合同编译函数。没有执行这些外部模块。文献恢复／旧 release 验包、全部 projection／tail 解析迁移仍由 root 的相应来源记录负责，本审查没有代付。

对象始终是同一原 du Hilbert 压缩，Γ=18Q⁻¹ 是 Legendre raw Gram；下面的整数矩阵 V_int 与 theorem 中 bounded operator V=K+U 分开。数学上的 * 是 adjoint；实际实对称 source 数据才用 transpose。没有把 raw 坐标范数换成 physical norm，没有把 B=E*M²E 改成 A²。

## 2. 任意非自伴 trial 的逆上界

令 A=E*ME、B=E*M²E、G=E*M⁻¹E，R_X=E−MEX。对任意 X 直接展开得

    R_X*R_X=I−AX−X*A+X*BX，
    R_X*M⁻¹R_X=G−X−X*+X*AX。

相减就得到原件的

    Uμ(X)−G=R_X*(μ⁻¹I−M⁻¹)R_X。

不要求 X 自伴、不要求 A、B 或 X 交换，也不要求 stationary solve 精确。已先支付 M≥mI、m=15/64，故固定 0<μ=1/8<m 时右边半正定。若还保 M≤bI，则 G≥b⁻¹I>0，因而 W≥G>0 与 W⁻¹≤G⁻¹ 都先于 finite sign 成立；没有循环使用目标正性。

若新正交坐标误差各为 εA=εB=ε，||X||≤y，A 换中心在 −X*AX 中花费 y²ε，在 8(−AX−X*A+X*BX) 中花费 8(2y+y²)ε。因此

    ΔX=(9y²+16y)ε，W=U_(1/8),0(X)+ΔX I≥G。

这是 norm perturbation 上界，actual y 必须从本次全部 Z 重新核；旧 y=8 不能继承。

Stationary equation 是 (8B0−A0)X=8A0−I。函数 t(8t−1) 在 t≥15/64 上递增，故谱计算给

    8B−A=E*M(8M−I)E≥(105/512)I，
    8B0−A0≥(105/512−9ε)I>0。

固定 μ 的 trial 提议因此有合法正矩阵入口。Decimal failed pivot 仍只能是提议／实现 NONPASS，不能据此推出 actual Q<0。29/32 只是旧 trial／integer 模板的选择；旧 q 或 cosh envelope 未付它，不能扩为整个新窗方法失败。

## 3. β 的放大与原误差运输

以 r=2⁻⁸⁵、p=2⁻⁴⁴⁰、m=15/64，e=1389r+p、n=896r²+p、h=11696r²+p，θ=2⁻⁴⁸、χ=1，独立 Fraction 重算确认

    n<m，α=eθ+2e²/(m−n)<2⁻¹²²，
    β=(e/θ+n)/m²+2h²/[m²(m−n)]<2⁻²²。

显示量级 α·2¹²²≈0.6782227147402409、β·2²²≈0.7716666666666666 仅为说明；严格比较由有理交叉乘给出。r/p 与 e/n/h 的解析域运输并非这些布尔值本身的后果。

令 α0=2⁻¹²²、β0=2⁻²²，ε=2⁻²²⁰，b=433/64。独立精确核得

    εD=ε+(2b+ε)ε=(465/32)2⁻²²⁰+2⁻⁴⁴⁰，
    λ0=εH+σ+α0+β0εD
      =2⁻¹²²+2⁻²⁰⁴+2⁻²²⁰+465·2⁻²⁴⁷+2⁻⁴⁶²+9·2⁻⁵¹²。

这里 εH=2⁻²⁰⁴+2⁻²²⁰、σ=9·2⁻⁵¹² 依然要求本次全 source／column 误差闭合。正确的正号消费链是

    D_M=B−A²≤D0+εD I，D0=B0−A0²，
    D0+εD I≥D_M≥0，
    P0≥0 ⇒ G⁻¹+J≥α0I+β0(D0+εD I)≥αI+βD_M。

因此同时放大 β 与其 εD 付款合法。不能仅对可能不正的裸 D0 放大系数。一般 theorem 随后才可给 M+K+U≥0；δ/16 与原合法 smooth／Dlog 型回代另由 root 闭合。这条链没有把本次有限 sign 当作已知事实。

## 4. raw norm 与 V_int 的独立重导

保原 Legendre degree i，q_i=8(2i+1)，Q=diag(q_i)、g=18、Γ=gQ⁻¹、S=2²⁵⁷、R=2²⁵⁶。Raw centers 为 a/S、b/S、j/S。取整数 Z、Y=QZ/R，则

    X=Γ¹ᐟ²YΓ⁻¹ᐟ²=Q¹ᐟ²ZQ¹ᐟ²/R，
    ||X||F²=Σ_(i,j)q_iq_j|Zij|²/R²。

g 精确消掉；这正是 physical 正交坐标里的 Frobenius 上界，并非 raw Euclidean Z 范数。Stationary equation 同样严格运输为

    Q(8b−a)Q·(Z/R)=8Qa−18S I。

为直接避免平方根，本 fresh 用 Γ、Y 写出

    Wr=ΓY+Y*Γ−Y*(a/S)Y
       +8[Γ−(a/S)Y−Y*(a/S)+Y*(b/S)Y]+ΔXΓ。

把 Y=QZ/R 逐项代入，恰得到原件的 Cw=SR²=2⁷⁶⁹、

    c=8Cw+(9y²+16y)2⁵⁴⁹，
    F=18SR(Z+Z*)−Z*QaQZ+8Z*QbQZ−8R(aQZ+Z*Qa)，
    V_int=QFQ+18cQ，Wr=Cw⁻¹Q⁻¹V_intQ⁻¹。

V_int 的正定来自先前 W>0，而非目标 K。对称性与每列 q_j 整除性须实际执行 exact check；它们也是把 V_int Q⁻¹ V_int 当整数矩阵的依据。

实现精确条件：y 应按本次 Frobenius 和取 y=2^k、k≥0 的整数二进制上界，或直接检查 c 为整数。旧13／14本身就把 k 限在非负范围。把“任意 dyadic 上界”宽读成可任意负幂再无检查地称 V_int 整数不合适；选 k≥0 没有新增数学前件或搜索，且不削弱合法 inverse upper identity。

新 raw tail 的 midpoint t_s 分母2⁶⁴¹，故平方分母2¹²⁸²；81/Γ00=27/Γ11=36，得到 Ûraw=36Σt_st_s*/2¹²⁸²。这里没有再乘 L²，也没有沿旧648/17系数。

## 5. 正合同变换、清分母与两个完整公式

令 C0 为原件第6节 raw matrix，Bc=Q⁻¹ᐟ²V_int/(√18 Cw)。独立代回 Γ⁻¹ᐟ² 的公式，得

    18²Cw² Bc*P0Bc=V_int C0V_int+18²CwV_int。

Bc 的非奇异来自 V_int>0；标量18²Cw²和 T0=9·2¹²⁸²均正。由于 Γ 的平方根在右边消去，最后是完全有理的同一个有限型，不是另一个坐标中近似比较。

本 fresh 从 T0/S、36T0/2¹²⁸²、18T0λ0、T0β0/S、T0β0/(18S²)、18²CwT0 分别重算六个系数，全部分母为1，并与原件逐项一致：

| 系数 | 精确值 | bit length |
|---|---|---:|
| cJ | 9·2¹⁰²⁵ | 1029 |
| cU | 324 | 9 |
| cΓ | 162·2¹²⁸²λ0 | 1168 |
| cB | 9·2¹⁰⁰³ | 1007 |
| cAA | 2⁷⁴⁵ | 746 |
| cW | 2916·2²⁰⁵¹ | 2063 |

Direct target 因而确为

    cJ VjV+cUΣ(Vt_s)(Vt_s)*−cΓVQ⁻¹V−cBVbV
       +cAA(aV)*Q(aV)+cWV。

另从 Yv=VQ⁻¹ 与独立 combined inner

    Hinner=Q(cJj−cBb+cAAaQa)Q−cΓQ+cUΣ(Qt_s)(Qt_s)*

展开 Yv Hinner Yv*+cWV，得到同一个六项式，未使用交换性，也未把 aV 与 Va 混淆。实际两个实现仍须分别累加并核全部 entries，不得一个调用另一个冒充独立；本文的小 fixture 不能替代实际两224-sector equality。

## 6. 实际执行的精确小对照与条件 caps

除手推外，本 fresh 用即时 stdlib Fraction 程序执行了两种不同的精确对照，没有生成完整 source／Gram 或写入数值 packets。

1. 取3维实对称 M，diagonal=(3,4,5)，相邻 off-diagonal=1/10、1/9，E取前两个坐标，X=[[1/5,2/7],[-3/11,1/13]]。直接算 M⁻¹、A、B、G，逐项验证 U−G=R_X*(8I−M⁻¹)R_X。该 X 非自伴，覆盖了不应偷偷加自伴假设的位置。
2. 取 q=(8,24,40)，a=[[2,1,-1],[1,3,0],[-1,0,5]]，b=[[4,2,1],[2,7,-1],[1,-1,9]]，j=[[5,0,2],[0,1,3],[2,3,7]]，非对称 Z=[[1,2,-1],[0,-1,3],[2,0,1]]，t0=(1,2,-1)、t1=(2,-1,3)、y=1。保持本次真实 S/R/λ0 等巨整数比例，独立算 Wr、V_int、Wr⁻¹与 raw transformed P0。全部3×3 entries 满足：Wr identity、V symmetry／column divisibility、正合同变换右式、six-term direct、combined formula精确全等，且最终 entries 全为整数。这里只检查代数，fixture 不是实际 source 或 positivity witness。

整数 cap 也按原件**条件**重新计算。设 n<256、q<2¹³、|a|/|b|/|j|≤2²⁷³、|Z|≤2²⁷²、|t|≤2⁶⁴¹，则 Frobenius 平方 <2⁷⁴，可选 k≤37。用每次 contraction 的项数、系数绝对值逐项上包围，本次大整数检查确认

    |Fij|<2⁸⁶⁴，|V_int,ij|<2⁸⁹¹，|Kij|<2³²⁰⁰。

在 K 的 cap 中保留了最多两条 tail columns；Γ项用 q≥8，未把减项省掉。这些是运行时实际 source/Z/t caps 已通过后的安全上预算，不能倒过来宣称真实数据已经通过，也不是要求 K 的观测 bit scale 等于某个旧值。任一实际 cap 未过应准确 NONPASS；不关闭 assert 或用旧3353-bit结果替代。

## 7. 可消费结果和未付门

可以消费的只有：在新 m/b 和实际新 source／column 误差前件下，固定 μ=1/8 的 inverse upper、实际 norm付款、新α0/β0连εD运输、同原norm的 raw V_int、两套新整数目标公式与正合同变换。它们给出了可执行有限证书入口，解除旧 μ 模板迁移这一个局部阻断。

尚欠本次15 shifts／225 pairs的完整 oracle、全部 weighted rows、true moment与raw tail误差、全解析 cross／complement 的 root 接入、实际 Z norm、两个完整 compiler equality，以及两个224-sector全部 exact residual rows的 sign。只有这些闭合，才可能经一般 theorem 得本次完整 classical Q下界。单个 Decimal方向、failedpivot或一个正Rayleigh都不够。

新有限 target 可能返回NONPASS；这只停止固定 L9/8、Ω256、N448、μ1/8、θ2⁻⁴⁸ 的充分比较，不推出 Q负性，也不自动授参数继续。即使完整证书后来成功，固定17/16→9/8支持扩大仍不支付 cofinal成长、primitive/principal/mixed RR或长期Goal完成门。本审查不计数学轮，不改变关键瓶颈或whole4/5负惯性UPPER。
