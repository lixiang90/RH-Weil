# 一个非阿贝尔 principal 构思的首门：精确退回已付 holonomy 系数

2026-10-29；`/root/new_principal_formula`独占稿。**本支未得到可准入的新 actual principal／mixed 输入。** 构思中的秩三、双端定标幂零连接虽有完整公式，却在最便宜首门精确读回10-28已经root／fresh消费的二阶Poisson–Green系数。故在授C064／601或新来源章前撤销“新候选”身份，只保准确对应和0准入结论。不重做旧库存，不另算新严格方法边界，也不以这个失败完成长期Goal。

## 1. 实际恢复和这次尝试的问题

已读README／STATE，执行`research_state.py check`后`show`，读完整G20261027、停止的C063、AI、600结算和宏观前沿当前段；前轮13733-byte `post-599-input-choice/principal-actual-input.md`全文实读。当前唯一计数为2/history64/latest600/formal20。父任务已经现场恢复同Goal active与600发布；本子稿未自行调用父Goal API／GitHub，不创建实例、不改轮数。STATE初读时的publication条件不被当新授权或新数学证据。

本次没有再抄573–584清单。尝试针对其最短缺口：旧标量primitive与flat unit容易把全部双degree零源一并消掉；能否用一个**真正有序、非交换的二层扩张**保存两源mixed信息，同时把两个physical endpoint矩放入第一层？这要求先验证405真实Pan及其全平移在实际相对类别中消去，并保537同域非根，而不是给一个新Gram取名primitive。

下述构思采用最小step-two上三角群，是实际连接／标架对象；但目前仅在physical实log线，不是已经构造的算术层、Cartier divisor、整数cycle或height。尤其不将它冒认成575两prime覆盖的relative对象：那里两side／边界和此处正负无穷标架不相同，尚无支付该运输的map。这个区别本身已经阻止它成为独立算术输入；仍可便宜检查其解析必要关系门。

## 2. 冻结构思的实际公式、范数和标架

取原physical复空间S_exp，不换成raw f。令E_ij为3×3矩阵单位，对z∈C设

    A_(r,z)(u)=z[e^(u/2)r(u)E_12+e^(−u/2)r(u)E_23]，
    F_r′(u,z)=F_r(u,z)A_(r,z)(u)，F_r(−∞,z)=I。

这是**右乘**演化。记

    a_r=e^(u/2)r，b_r=e^(−u/2)r，
    A_+(u)=∫_(−∞)^u a_r(v)dv，A_−(u)=∫_(−∞)^u b_r(v)dv，
    C_−(u)=∫_(x<y<u) a_r(x)b_r(y)dxdy。

因为E_12E_23=E_13、所有三重乘积为0，解及双端运输准确为

    F_r=I+zA_+E_12+zA_−E_23+z²C_−E_13，
    H_r(z)=F_r(+∞,z)
      =I+zμ_+(r)E_12+zμ_−(r)E_23+z²C(r)E_13，
    C(r)=∫_(x<y) r(x)r(y)e^(-(y−x)/2)dxdy。

这不是只保留未控高阶的formal series，且z=0与r=0均给I。双端标架固定，允许的直接frame改变g(u,z)在±∞均趋I；右乘frame F→Fg的连接为g^(-1)Ag+g^(-1)g′，双端H不变。这里没有非酉A0背景，不能将旧稿中background-only g→I的更宽类偷渡为同一规范。忘掉端标架允许任意右端g会改变类别；不能这么消掉H再说通过原门。

对N>1/2，p_(N,0)(r)=sup e^(N|u|)|r(u)|给

    ||a_r||_1,||b_r||_1
      ≤[1/(N−1/2)+1/(N+1/2)]p_(N,0)(r)。

故全S_exp上各项绝对收敛并在z紧集连续。先fixed支集[-L,L]时各||a_r||_1、||b_r||_1≤e^(L/2)√(2L)||r||_du；它是明确的成长费用，绝非全线du／Dlog单位球对whole map的免费界。另一方面**必要中心系数本身**有全线du界，正是下面旧过滤器的关键。

## 3. 首门发现的是 exact 强旧，不是一个新 rank 参数

令K(u)=e^(−|u|/2)。交换积分变量、对称化后，对所有复r∈S_exp有

    C(r)=1/2∬r(x)r(y)K(x−y)dxdy，
    |C(r)|≤2||r||²_du，
    |C(r)−C(s)|≤2||r−s||_du(||r||_du+||s||_du)。

这里是**复双线性二次式，没有conjugate**；不能把它宣称为全complex Hermitian Weil型。仅在实r时它也是普通正Poisson–Green能量。此识别无需继续任何高阶计算。

定向关键词随后实际找到10-28的已闭原族：

    A0=diag(1/4,−1/4)，B=[[a,c],[cbar,−a]]，
    Y′=zr e^(−uA0)B e^(uA0)Y，H_B(r)(z)=Y(+∞,z)。

其冻结原稿及后续root／fresh记录已经给出，在a=0、|c|=1时

    V_2(r)_(11)=1/2∬r(x)r(y)e^(−|x−y|/2)dxdy=C(r)。

**相同的是本构思必须为零的这个读出，不是把整个秩三对象等同于旧秩二对象。** 新矩阵表示只是将旧全z运输的第二Taylor系数放成一个exact中央entry；它没有改变source、kernel、原范数、关系或方向，因此不能据rank不同再授数学门。

旧553已付physical Pan在原real／complex L²的线性span稠密。若本相对framed类别把全部Pan当principal平凡类，则H_p(z)≡I必使C(p)=0对全Pan成立；上述单个必要系数的L²连续性已经迫C全零，与旧非零实compact bump的C>0矛盾。这个逻辑不要求whole H_r global-du有界，也不要求carrier有限维或完整coset相容。它正是10-28 root已准确重闭的系数级旧链，而不是本稿新证明一种更大方法类失败。

## 4. 全真实平移关系的已付见证与537角色

405的raw p_raw=(D²+D)h对应physical

    H=e^(u/2)h>0，P=(D²−1/4)H∈S_exp，
    P_b=τ_bP，H_b=τ_bH。

全部P_b及其fixed倍数是真实Pan，μ_±(P_b)=0，不能compact crop替代。旧closure原件已经准确支付

    (D²−1/4)K=−δ_0，K*P_b=−H_b，
    C(P_b)=1/2∫[(H′)²+H²/4]>0。

该值不依b，没有额外2π。因此本构思在每个真实平移上有

    H_(εP_b)(z)=I+ε²z²C(P)E_13≠I（εz≠0）。

这不是要求raw connection字面为0，而是它在**已指定双端framed gauge quotient中**仍非平凡。若只改用central coefficient的极化作mixed读出，实对角B_C(P_b,P_b)=2C(P_b)>0亦不为根；原完整B_ζ(P_b,·)=0则是旧405已付事实。故不能绕过quotient首门，只把该ordinary Green energy称Weil mixed交数。

同域非根可取553已明确的r0=(D²−1/4)ψ、0≠ψ∈Cc∞((-17/16,17/16);R)，则r0≠0、μ_±(r0)=0，537严格正性给Q_ζ(r0)>0。这个构思确会读取其central data，但同时读取应消的P；“保非根”不能修复“关系未消”。未重新运行537数值或寻找新probe。

若忘掉端框架使所有这些平坦连接全局可平凡化，又会同时丢掉这个非根；更宽gauge、额外数据或不同mixed配对是另一对象，并未被本次构思构造或排除。尤其没有给同对象算术principal／sections／RR或Γ/contact／全部p^k／双pole身份。

## 5. 裁决、净后果与精确停止

这个尝试触及的是“scalar units之外能否保存非阿贝尔mixed信息”的真实首箭头，但它的首个有信息读出与旧已闭C(r) exact相同。因而本支撤销它作为**真正不同新输入**的资格，**0准入／无C064或601**。0的理由是明确strongest-old包含，而不是公式简单、只是一条反例或尚未证明RH。没有新增whole后果、primitive／mixed／dangerous corecross／成长Ξ付款；whole542+555→557仍仅leading4/5负惯性UPPER。

停止这一再呈现，不调rank、E_ij权、A0、frames、coupling或高阶，不以它串论文／source章。完整源路径可能有不满足旧系数界的别种连接、真曲率／relative算术module、非解析或近似D′规则，这些仅为未排范围，不是本稿已给出的new actual data，不自动授预算。当前缺失仍是一个不同于这个已付ordinary Green系数、能actual消405并保537的算术相对关系或mixed根机制。

本稿未网页、新paper／PDF／作者后章／下载／渲染、数值或大型重放；只写这一独占文件，不改Goal／STATE／cadence／库／Git。原件存在不代root消费。作者论文或文献目录无需新增；计数保持2/history64/latest600/formal20，不将本次恢复旧closure称macro21或重复数学轮。无待续进程。

## 6. 实读范围与版本

最初“rank3可形成新数据”的构思在定向旧记录查验后撤销；未先授合同再补强旧。405实际读§4的η／h公式至§7，553读§§1–3开头，575读§§1–3开头；旧opinion和6654结算全文，Pan closure读§§1–4，domain稿读§§1–3至det段，scope-clarification与root JSON全文。未以JSON的24项hash清单冒称本轮重新读完全部nested原件；以下指纹只认实际版本，不代数学证明。

| 实际输入 | 实读范围 | bytes | raw SHA256 |
| --- | --- | ---: | --- |
| `goals/GOAL.20261027.md` | 全文/完成门与流程 | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| `goals/contracts/C063-rank-two-period-positive-cone.md` | 全文/停止与预算 | 1517 | `e242d79457f2721ac77aa50d9666456e3ea77b6d7597937b4b93f061188271cb` |
| `goals/reviews/2026-10-29-rank-two-period-600-settlement.md` | 全文/最新因果 | 3943 | `6e015edf62a0ad1ade37bdab5cead786f3b26d90095e3ccc4a089462ce07d2b5` |
| `reviews/2026-10-29/post-599-input-choice/principal-actual-input.md` | 全文/强旧摘要，不重做573–584库存 | 13733 | `2370929c97354a86e6d02b11ee689e954723e9501250e5d9d82e9cb0707e848a` |
| `notes/405-f1-adelic-restriction-moments-and-radical.md` | §4 eta/h公式至§7 | 14633 | `fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d` |
| `notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md` | §§1–3开头 | 6613 | `35a40c35d1eaa7fafb462361ddef1bfb9643402b5670f832b9142aeb4b74abce` |
| `notes/575-regular-cartier-cover-flat-source-and-capacity-gap.md` | §§1–3开头 | 13160 | `f70e37cb84d4d705a3a9e6fe57c6f1b72bd8f9b02cb3d9ddeb6ac16bb184fd8e` |
| `reviews/2026-10-28/independent-source-discovery/original-holonomy-next-input-opinion.md` | 全文 | 5813 | `2ac26586491f74da5fb58e579bc55b43f7ecc42e5ad9daf3a104009f965ce359` |
| `goals/reviews/2026-10-28-framed-holonomy-strongest-old-stop.md` | 全文 | 6654 | `2e4d377d05b4a2db6d65e444741172d99fe00d37bf78b2e089fab90c5d280b08` |
| `reviews/2026-10-28/framed-holonomy-closure/pan-coefficients-and-strongest-old-closure.md` | §§1–4 | 8361 | `37b4f87afaa5b18306792633d56d26f933b3fd675bead37ab40fda79cacea284` |
| `reviews/2026-10-28/framed-holonomy-closure/domain-norm-and-gauge-closure.md` | §§1–3至det段 | 10882 | `552ec97a112e87fd89029a2c001f691060cd722f2e927c2ceb8dd3a42f3f10e0` |
| `reviews/2026-10-28/framed-holonomy-closure/coefficient-and-gauge-scope-clarification.md` | 全文 | 2430 | `5078dd43d4458e2a0da7c89ede8c179f149a78f0accf93b1eefee0a355bfae83` |
| `reviews/2026-10-28/framed-holonomy-closure/root-consumption-scope.json` | 全文，nestedhash仅身份 | 8397 | `5f5043bdc3842584e16888c2c7dc38be9ba9abdf946a93d0796a7b591fce1ec0` |
