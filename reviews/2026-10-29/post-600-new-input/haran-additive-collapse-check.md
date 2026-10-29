# Haran 2007 的实际 F-ring 公理：整数两槽的有限字词折叠

2026-10-29；`/root/new_principal_formula`的新独占任务，未改此前10689-byte holonomy首门稿。**有限公理门闭合：在Definition2.1／2.9的实际范畴中，对每个目标C，Hom(F(Z),C)至多一元；因此这个self-cospan的F-ring纤维和F(Z)⊚_F F(Z)由F(Z)表示，折叠同构，且两个map在全部矩阵上相等。** 下面不用module tensor替代⊚，不由ordinary embedding的full faithfulness偷推，不假设目标C预先可加。

该结论只消费这一ordinary affine open。没有证明compactified arithmetic square整体塌缩、所有Haran或所有F1路线失败，没有构造physical源→principal／mixed桥、完整Weil身份或新的原范数费用。标准范畴工具及计轮建议见§8，仍待root／不同fresh消费。

## 1. 恢复、source与命题方向

实际恢复README／STATE，运行check后show，读Goal、停止C063、AI、600总结和宏观前沿当前段。新任务来自root明确的finite-axiom准入，不复用C063预算。当前solecadence2/history64/latest600/formal20；parent现场Goal／发布状态由root记录，本子稿未自行调用父Goal API／GitHub或改变其状态。

实读Haran2007本地出版PDF的printed627–628：Definition2.1及(2.3)–(2.8)、Definition2.9；printed627／628已整页目视。root随后明确补准printed632 Example1，本文实读并目视(2.13)–(2.13.4)，确认F(A)为所有有限Y×X的A矩阵，composition／⊕／⊗为通常矩阵乘法、直和、Kronecker积。Example1的fully faithful只比较ordinary F(A)和F(B)，本证明的目标C则任意F-ring，两者不能混为前提。

printed671–674的§7.1及§7.2相关文字已实读，671／674整页目视，printed675只消费§7.2末的affine open公式。真实曝光边界需保留：671页上半§6.3尾随整页返回，675文本取前50行连带返回§8开头三段；632整页目视也使Example2后半可见。上述均只曝光、不作本证明依赖或新章准入。未打开676–678、新论文、作者参考文献或§8后续定义；未用那些段落改变命题。

记M=F(Z)，即Example1的integer-matrix F-ring。要证明的是

    对任意F-ring C，任何两个同态 f0,f1:M→C 都相等。       (A)

这是Hom(M,C)方向，不是Hom(C,M)方向。严格术语是initial箭头F→M为epimorphism，或M在opposite范畴为subterminal；若说“relative subterminal”，应在Spec的反变一侧说。M不是F-Rings的initial object，源中initial object是F。

## 2. 真正使用的公理与有限结构

Definition2.1给：F→C在对象上恒等且faithful，[0]为零对象，⊕、⊗是functor，并有F中的固定coherence和分配同构。特别，(2.5.1)对**任意C morphisms**成立，不只对一个ordinary子环的像成立。

Definition2.9给fi固定F，保composition、⊕、⊗。所以fi不必faithful于整个M，不能假设integer coefficients在C中保持不同；例如允许mod p的普通像。关键只在两map有相同的F部分，且mixed tensor必须服从C的interchange。

写1=[1]、2=1⊕1。M中取

    σ=[1 1]:2→1， δ=[1;1]:1→2， n=[−1]:1→1。

给定fi，写σ_i=fi(σ)、δ_i=fi(δ)。取F中的partial injection

    j:2→2⊗2，j(1)=(1,1)，j(2)=(2,2)，

及其partial inverseπ:2⊗2→2，只在这两个diagonal点有定义。π只是F里的具体partial bijection，**不要求C有transpose involution**。所有unitors／排列均为F中的指定coherence，两fi都固定；下式沿作者惯例省写它们。

在literal integer matrices中有

    (id_2⊗σ)j=id_2=(σ⊗id_2)j，                    (1)
    π(id_2⊗δ)=id_2=π(δ⊗id_2)。                    (2)

每条都是单份M内的有限矩阵恒等式，故分别经fi送入C；这里没有在C上预先定义加法。

## 3. 两份fold与diagonal已由mixed interchange强迫相等

考虑C中的mixed tensor σ_0⊗σ_1:2⊗2→1。由(2.5.1)两种分解及(1)，

    (σ_0⊗σ_1)j
      =σ_0(id_2⊗σ_1)j=σ_0，
    (σ_0⊗σ_1)j
      =σ_1(σ_0⊗id_2)j=σ_1。

所以σ_0=σ_1=:Σ。同样，将π左乘δ_0⊗δ_1，利用(2)和两种factorization，得到

    π(δ_0⊗δ_1)=δ_1=δ_0，

故δ_0=δ_1=:Δ。这是实际mixed word的有限消去，不是因为两个“copy”同名，也不是从scalar整数相等假定整条row／column相等。

此短证已经说明核心axiom的作用范围：(2.5.1)确实可混用不同fi的像；Definition2.9保证(1)／(2)和j、π可在两槽共同使用。它没有向actual公理另加一条跨槽commutativity。原(2.6)也有效，但这里甚至不需先由它推出整个目标的additive enrichment。

## 4. 负元、整数和全部matrix层，不留scalar漏洞

先在C_(1,1)定义

    a+b := Σ(a⊕b)Δ。                                (3)

Σ和Δ均为f0对ordinary fold／diagonal的像，继承commutative monoid／cocommutative comonoid的有限关系，unit／counit是F中0↔1的map。因此(3)为commutative monoid，单位是zero morphism。具体地，三项加法均展开为Σ_3(a⊕b⊕c)Δ_3；交换性来自F中swap，a+0=a来自fold／diagonal的unit／counit关系。这里的“+”不是把原(2.7)的composition误称加法。

令ν_i=fi([−1])。因为Σ、Δ已共同，fi对integer恒等式1+(−1)=0的像给

    1+ν_0=0=1+ν_1。

commutative monoid中1的inverse唯一，显式有

    ν_0=ν_0+(1+ν_1)=(ν_0+1)+ν_1=ν_1。

对任意n≥1，all-ones row σ_n:n→1及column δ_n:1→n由binary σ／δ、⊕、composition和F-coherence有限生成；source中[n]=σ_nδ_n。因此两fi在全部非负integer scalars相同，负整数再由共同ν与composition得到。0、1原本就在F中固定。

现在取任意非空有限X、Y与integer matrixA=(a_yx)∈M_(Y,X)。对有限标号选任意F中的排列，令

    D_A=⊕_((y,x)∈Y×X)[a_yx]，

是Y⊗X上的diagonal scalar matrix。source有准确有限word

    A=(id_Y⊗σ_X) D_A (δ_Y⊗id_X)。                   (4)

δ_Y把每个X-coordinate复制到每个y，D_A逐(y,x)乘a_yx，σ_X再对x求和，故(4)的(y,x) entry正是a_yx。两fi在σ_X、δ_Y、D_A各块、F排列与identity上全同，又保⊕、⊗、composition，所以f0(A)=f1(A)。X或Y为空时只有zero map，也同。至此(A)在**全部finite matrix层**闭合，不只是C_(1,1)中的整数。

## 5. 对root较长additive路线的一致核对

短证不依赖目标已经是Mat(R)。若沿root提出的路线，从任一f:M→C定义Σ_X=σ⊗id_X、Δ_X=δ⊗id_X，并用F的分配coherence识别X⊕X，则(2.5.1)和(2.6)对任意h:X→Y确给

    hΣ_X=Σ_Y(h⊕h)， Δ_Y h=(h⊕h)Δ_X。                (5)

因此α+β=Σ_Y(α⊕β)Δ_X在所有Hom(X,Y)上给abelian group，负元由f(−1)⊗id生成；(5)使composition双线性。这里证明的是作用于**所有C箭头**的自然性，不能只在f(M)内验证后便升级。

canonical inclusions／projections来自F，它们的π_iι_j=δ_ij关系保留；而Σ_iι_iπ_i=id是M中的integer matrix恒等式，经f和上述同一加法送入C。于是⊕确为biproduct，每个对象是有限个1的canonical biproduct。第二f′的fold／diagonal必须是相同biproduct的唯一codiagonal／diagonal，遂与短证一致。若进一步重构C为Mat(End_C1)，还须保composition、⊕和tensor各自的component公式；本题已由(4)完成wholematrix唯一性，不需要借一个未写明的等价来补最后一步。

这也回答“(2.5.1)、(2.6)是否足够”：它们和Definition2.9及source矩阵关系已经足够，未发现需要继续读下一页公理或另加新兼容性的缺口。

## 6. self-fibred sum与折叠的准确结论

先不用一般pair的存在声明，M连同两条id_M就已代表self-cospan M←F→M的pushout：任意C中的兼容pair f0,f1:M→C由(A)必相等，因而只有唯一共同factor M→C；两者都不存在时对应Hom也为空。这个selfcase有id cocone，M中F保持faithful，完全不需要解决没有共同faithful target的一般pair会怎样。

若按§7.1 Theorem7.1写B=M⊚_F M、两map i0,i1以及fold d:B→M，则(A)应用到target B立即给i0=i1=:i。普遍性质给d i=id_M，而i d:B→B与id_B在两条i0,i1后均相等；由同一普遍性质的唯一性，

    i d=id_B， 所以 d:B→M为isomorphism。              (6)

这用的是真正F-ring纤维和⊚，未使用module tensor。Remark7.1.9说module tensor→⊚一般非同构，不影响本selfcase由actual axioms得到的(6)，也不能被误读成作者声明每个具体selfcase必非退化。

Spec反变后，已核§7.2公式中的ordinary affine open

    Spec(F(Z)⊚_F F(Z))

与Spec(F(Z))同构，两个projection相同；不能把这份open的两条ordinary integer slots当成已独立的非零transverse arithmetic方向。这里只是这个affine constructor的判定，不推compactification、arch boundary、不同F-ring变体或2022／2024框架的结论；也没有说此open之外不存在primitive／mixed容量。

faithful F确要求0_(1,1)≠id_1，故literal F-Rings排除zero matrix category。上述证明未假设fi在Z上injective，亦未借zero-ring target消去两槽。终点M=F(Z)非zero且有id cocone，faithfulness细节不阻挡selfcase。

## 7. 最强旧与真实未付箭头

本分工只定向扣363的来源地图和§5的Borger段。那里的Z是标准Λ-ring范畴的initial object，所以其self-coproduct等于Z；Lorscheid行提醒的是blueprint tensor／反射范畴不可互换。这些不是Haran2007 Definition2.1的同范畴命题。此处F才initial，而M满足的是Hom(M,C)至多一元，必须由§3的mixed tensor word证明；不能仅凭旧Borger结论的外形相同就替代。

当前paid短链是：actual(2.5.1)+fixed-F morphisms → 两fold／diagonal共同 → integer scalars共同 → (4)所有矩阵共同 → self-pushout fold同构。没有physical源r、Pan、537非根或原du／Dlog被映入这个载体的formula。亦无Γ/contact、proper powers、双pole、整数截面／mixed RR或成长Ξ身份，whole4/5负惯性UPPER未改。因此本有限门不完成Goal的任何全局验收。

## 8. 分类建议与终态

本次不仅核了书目或印刷位置，确有一个source-specific、wholematrix级的代数判定；不能在结算中抹成“只看了定义，没有数学结果”。另一方面，核心证明是标准interchange／commutative monoid／finite matrix generation，不是新一般范畴理论，更不能每个引理各计一轮。

建议root把它作为**一个待different-fresh/root消费的明确有限数学首门**：若按实际新Haran-affine非退化候选取得此前未付的完整准入反例，整门可统一一次结算；若找到同一Haran类别、同一fold命题已由旧资产支付，则归old0。仅见363的Borger／Lorscheid不同类别，还不足以断言本门已paid。这里不预建C064／601、不改cadence，也不因没有RH或使用标准范畴工具先强定0。root须保本门仅affine carrier的范围，不把它升级成所有Haran／F1或直接physical primitive路线终结。

只写本新独占稿；此前10689-byte `principal-formula-and-first-gate.md`保持原字节。没有web、新论文／PDF后章、数值或large replay，没有Goal／STATE／cadence／库／Git变更，也无待续进程。

## 9. 实际输入与阅读边界指纹

源PDF实际原字节及允许页的text／PNG来自同一本地版本。PDF全部71页并不等于读取71页；source消费严格按§1。671§6.3尾、675§8开头、632Example2的额外曝光均未被用作本门前件。未重新审计所有F-scheme、localization或pro-object定义。

| 实际输入 | 实读范围 | bytes | raw SHA256 |
| --- | --- | ---: | --- |
| `goals/GOAL.20261027.md` | 全文/完成门与流程 | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| `goals/contracts/C063-rank-two-period-positive-cone.md` | 全文/停止和计轮边界 | 1517 | `e242d79457f2721ac77aa50d9666456e3ea77b6d7597937b4b93f061188271cb` |
| `reviews/2026-10-29/post-600-new-input/haran-locator-scope-correction.md` | 全文/⊗冻结及⊚更正 | 2463 | `8f577f3e3ddd606d02c1a6ab99d17026c5875baf772c1d425266fa4d1ceb80e3` |
| `reviews/2026-10-29/post-600-new-input/haran-fold-first-gate-admission.md` | 全文/实际finite-axiom门 | 1814 | `9d48d6f60269d6ae80f47f45328bd4faf69c1632b429519dc72e95e3769c67c2` |
| `literature/local/2026-10-29-haran-section72/haran-non-additive-2007.pdf` | raw签名/hash；消费print627–628与632Example1、671–674§7及675§7.2末，真实额外曝光见正文 | 1032382 | `1befc0e1fa8465d29a452d75bbcf02ded93a50b12c179a0b48303570ca60570f` |
| `notes/363-f1-arithmetic-geometry-and-existence-audit.md` | §§1–2及§5末Borger/Lorscheid范围，不续来源库存 | 15561 | `be7d7668a14ba28cdb0c021651ccf019fd284ee67b1d90278bc8557a6b64b18c` |
