# Heegner采样候选的物理接口与最强旧消费

2026-10-29。独占项目侧审查；不是BO论文来源证明的替代。已恢复README/STATE、Goal、C058停止范围、D20261029U、宏观前沿及唯一固定章节准入。开始时并行STATE缺pending观察字段导致check/show失败，已告知root；root补后本任务实际重新check再show通过。没有改STATE/cadence/Git、联网、数值运行或建数学合同。当前1/history59/latest595/formal19，长期Goal同实例active/open。

## 1. 本次实际对象和已付输入

唯一候选固定M37、Delta1、r0=1及预定cutoff/T_X，不调level、Delta、权或窗。论文中的合法标签、稳定子、degree-zero y、Maass域及Delta1附加条件由独立来源原件负责；本稿不把root/agent消息当已核原文。本稿只在“这些y确为原文定义的合法degree-zero除子”条件下审物理映射。没有自行读取BO新章节或搜索后继来源。

项目源是复S_exp中的物理r=e^(u/2)f。405原f坐标的p_f=(D²+D)h，对应物理

    H(u)=e^(u/2)h(u)>0， p(u)=(D²−1/4)H(u)=e^(u/2)p_f(u)。

405 §4–5的实际Gaussian/Poisson源与579 §2–3、584 §3已付：H和p在S_exp，p非零，全部实平移p_b(u)=p(u−b)及其有限复线性组合均属实际Pan。这里只用这一个明确子空间，不假设Pan与全部谱根相等，也不把Pan按名称视为几何principal。两端全指数衰减保证p、H及导数可积，分部积分合法。

537已付所有compact complex源在半窗17/16的完整Q严格正性。沿583/584的明确控制族，任意非零偶非负smooth phi、足够小支集，r_phi=(D²−1/4)(u phi)非零、双pole矩零、完整Q(r_phi)>0。537没有唯一数值测试源；当前应保同一个实际选择，不可另造一个消失样本后冒认其全源可见性。原du、zero-extension Dlog与强S_exp半范数为不同费用。

## 2. 四个角色及rounding

对fixed integer X，合法标签有限。合并同s=|m|后的distinct实节点为u_j=log(s_j/X)，j=1,…,k_X；同一节点的所有h/标签共享同一个r(u_j)。先保未舍入式R_X(r)=sum a_(r,X)(m,h)y(m,h)，它在合法复化除子空间中是复线性的有限点求值映射。聚合同节点可能导致cycle自身抵消，不预判其非零。

提出的D_X把Re/Im a分别按floor(T_X a+1/2)舍入再除T_X。它一般不是实线性或复线性，半整数tie处甚至不能免费使用奇性。共同分母和稳定子分母清除，只给两个实的整数除子multiple；“有理系数cycle”还不等于定义域为Q的Galois不变cycle。复数加权除子不自动是一个整线丛或单个亚纯函数的主除子。

应分别记录：原始Div^0对象；其Pic/Jacobian类；被选择的principal函数或canonical differential；带归一化的Green/relative数据。Divisor class为零并不意味着选出的principal函数/Green记录是零；度零也远弱于principal。BO principal/torsion判据若有额外Maass条件，不能仅从整数系数获得。图中“relation被消去”必须指定在哪一角色、哪个群/base与哪个实际等式中发生。

## 3. fixed-X有限点的强旧首检：全Pan的采样像已满

这一标准结论从上节实际p重新证明，**没有把584另一份B的像集结论直接套到本新采样**。令V为全部p_b的有限复span，E_X(r)=(r(u_1),…,r(u_k))。则

    E_X(V)=C^k=E_X(S_exp)。                         (A)

证明：若有限维像不是全空间，存在非零alpha=(alpha_j)使sum alpha_j p(u_j−b)=0对所有b。采用原物理Fourier约定hat p(t)=int p(u)e^(−itu)du，取b变量Fourier变换，得

    hat p(−t) sum alpha_j e^(−it u_j)=0， t∈R。

而hat p(0)=int p=−(1/4)int H非零；连续性给某个0附近开区间hat p(−t)不为零。因此有限exponential polynomial在开区间为零，整延拓恒零。对t=0求0至k−1阶导数得到distinct节点的Vandermonde系统，迫全部alpha_j=0，矛盾。k=0时两像都是单点，结论平凡。所有变换都只用Schwartz/可积和有限和，不借ζ零点位置或未知几何。V包含于实际Pan，所以(A)成立。

每个fixedX的R_X、D_X均只依赖E_X。即使后者含非线性rounding，也逐个匹配整个节点向量，故**准确有像集相等**

    R_X(Pan)=R_X(S_exp)， D_X(Pan)=D_X(S_exp)。       (B)

这不需要y独立、非零，目标也不必赋范。于是若某fixedX的class读出C_X(D_X(r))仅以这份D_X为输入，并要求全部Pan都送到同一zero/base值，则它在整个source像上恒值，连同537控制源的类也被杀掉。特别地，“每fixedX全部Pan actual principal，同时某source的Jacobian类非零”不能由这个有限采样rule同时实现。这里对principal函数/Green原始数据、relative/higher数据不作零结论；它们可能还有独立记录，已经不是仅靠D_X的类读出。

这是405已付actualGaussian与标准Fourier/有限维对偶的直接消费，不是新的成长核心边界或新增数学轮。若把(B)另包装成普遍Heegner失败，会超出量词。

## 4. 原norm与cofinal逃逸不能省略

固定X的点求值不是原L2(du)或Dlog上的有界算子。如果某个聚合节点方向产生非零输出，取smooth窄bump在该节点取固定值、避开其他有限节点；缩宽epsilon而保持所有采样值不动，则输出固定，而L2范数趋零。对同一bump，Fourier缩放给

    ||r_epsilon||_Dlog^2=O(epsilon log(1/epsilon)) ->0。

因此也没有原Dlog有界运输。这里条件性的“输出非零”不能省略；若聚合后所有cycle/类都零，当然只是零映射。没有反驳强S_exp拓扑上的有限求值连续性；fixed强半范数或必要导数费必须实际支付。

有限采样也可漏掉一个fixedX的compact正窗源：有限节点之外可放小smooth支集。但不同X可能用不同漏源，这个标准有限rank事实**不否定cofinal全部fixed源可见性**，不假装已经评价原选定phi的所有X。

同样，(B)为每fixedX逐层全Pan精确消去的限制。为给某r匹配节点而选的p_(X,r)一般随X改变，强半范数/系数可能成长；本稿没有对其费用给uniform上界。因此若只要求每一个先fixed Pan源在X→∞时渐近principal，不能用(B)交换量词而宣布全部fixed源极限类零。非闭base的极限尤其须连同583的closed-base补正消费；连续性只保证落closure(base)，非Hausdorff目标不能自动升级为零。

原候选T_X=X²只控制形式系数rounding。对任何已经定义的复化target seminorm q，逐项误差上界至多

    q(D_X−R_X) <= (sqrt(2)/(2T_X)) sum_labels q(y_label)。

这不是原文已付height界。没有q(y)的成长及mixed/Gram运输，不能从系数l2或T_X的次数推出Jacobian、Green、Neron–Tate或完整Weil误差消失。标签网格、稳定子、关系尾、cutoff sqrtX至X^(3/2)、整数multiple与实际harmonic Maass lift的全部费用仍须另核。

## 5. 与强旧资产比较及本章可判门

旧BY门是原II2,2/k0/trivialrho下shadow target为零和arch CM Green评价，且原essential j主部不在有限principal-part域。它不决定本次M37真实Heegner/Jacobian的全部输入；也不授予新sampler一个harmonic lift。旧583给actualFaber/native Green全尾，但其raw像保Pan、合适closed-base principal完成商杀全部源。旧584是另外的markedg11 signed-cut/Pan增长及同B后处理全退化；本稿没有把其核、1728号或其necessary费用套到Heegner采样。这里只复用真实Pan/537角色及标准有限测量首检。

本章要提供改变选择的实际桥，至少须说明：固定采样principal part是否为合法Maass输入、对应cusp obstruction/orthogonality与canonical lift如何选；所需正系数和Delta1修正是否已付；全405关系在哪个actual principal/Green身份中消去而537仍保非零；该身份的原du/Dlog/强源/cofinal误差与mixed费用如何运输。(B)已表明若它只承诺每finiteX从同D_X取一个杀全Pan的类，就不可能保非根；若走cofinal/relative路线则必须另付新数据/成长量词，未知本身不算输入。

当前项目旧资产既没有给固定sampler principal，也没有给所需cofinal费用；来源合法仍不能补这些缺项。若独立BO来源审查只找到modular输入到真实cycle的typed构造和条件性principal判据，应按**来源0停止**当前门，不建C059，不自动续§6/7/8、引用、level/Delta/权/截断；不能宣称全部Heegner、不同relative/higher或有费cofinal方案失败。若原文确给新实际physical身份，root需对齐其真实量词后重新准入，不能仅按论文标题晋级。

实际关键瓶颈仍为非零arithmeticprimitive/principal/sections/mixed、危险signedcorecross/成长Xi；whole542+555→557仍仅leading4/5负惯性UPPER。当前来源核查和标准旧消费不移除这些瓶颈，不完成长期Goal。输出只本文件，无数值进程或后继任务。

## 实际项目输入字节

下表SHA只绑定所用版本，不把hash当证明。405读全相关源/关系/双矩；537读取全源定理和§4域；579读取物理规范及实际Pan角色；583 §5–6连closed-base补正；584 §3–6、marked-cusp原Pan证明及控制/准入；BY只用已归档scope，不重开PDF。BO原文由独立来源分支承担，未列作本稿已核证明。

| Path | bytes | SHA256 |
|---|---:|---|
| notes/405-f1-adelic-restriction-moments-and-radical.md | 14633 | fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d |
| notes/537-source-exact-weil-window-positive-tail-admission.md | 8155 | 269a500556d37fc04a4e44efd2f0899414787743e529506dbbe7395a34eea9f8 |
| notes/579-kry-physical-gaussian-source-and-native-primitive-obstruction.md | 15730 | 1b4506e2a1dfd311b7816e17622b45ee257295c6716822cfc424b0e93ef306f1 |
| notes/583-completed-modular-faber-source-and-native-green-transport.md | 11644 | babe212467d5c41d14a20ba2d0d99b1f49722f2388bfea9dc13c6334ef3fadab |
| notes/584-marked-cusp-borel-kernel-and-pan-residue-collapse.md | 8856 | 63a2a438666cc859d543503715a16bb7c58c2de80e0a5bd8a22e2a36997c96a0 |
| reviews/2026-10-27/joint-oldform-tower/583-principal-closed-base-correction.md | 1843 | 92f135e0b119487fc1a62b4af1bd8b66ba3112e946f1de7491e437d841cee454 |
| reviews/2026-10-27/marked-cusp/pan-relation-test.md | 12525 | 6a68cf1bfd7861cabb80dd0bdd41e09756293e9071ef870a2ff1715463874367 |
| reviews/2026-10-27/marked-cusp/source-controls.json | 17286 | 8d8495f4aad1b5f6be4a02b27b958a82391e7cf96291b1479306d74679406cf1 |
| reviews/2026-10-27/after-reader/next-marked-cusp-functional-admission.md | 4158 | 91570b2c3b0e6dfd0f08667a8e8c70329923d1e3a07a1c6205f6f5432deeb5d4 |
| literature/supplements/2026-10-27-by-cm-source-scope.md | 1588 | af956e37c4b5baf5bc8d617d6097e4520df34bd62ad61ece6f8f8eaaa95216ed |
| reviews/2026-10-29/weil-9-8-physical-lower-gate/next-heegner-principal-source-admission.md | 4185 | 90ca14ee39c13937173df7651f905ea5dabf5152a19c6ddea1aaff31d35c7394 |
