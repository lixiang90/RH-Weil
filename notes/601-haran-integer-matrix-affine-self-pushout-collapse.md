# Haran 2007：整数矩阵仿射自配对的折叠同构

2026-10-29。G20261027/C064。结论限于作者2007版实际F-ring公理下的ordinary affine对象；不是紧化算术平方整体、其它版本F1几何或RH路线的否定。

## 1. 结论和来源

记M=F(Z)，其X→Y态射为全部Y×X整数矩阵，直和与张量为分块和及Kronecker积。在Haran 2007 Definition2.1/2.9的F-Rings中，对每个目标C，

    #Hom(M,C) ≤ 1。

这里是从M出发，覆盖全部矩阵，不仅是标量整数。于是M连同两个id本身满足M←F→M的pushout；若写B=M⊚_F M、结构映射i0,i1:M→B和fold d:B→M，则i0=i1=:i，d与i互逆。

谱反变后，projection Spec(i):Spec(B)→Spec(M)与diagonal Spec(d):Spec(M)→Spec(B)互逆。§7.2中这个ordinary dense affine open不能借两份整数拷贝获得独立横向方向。未判紧化边界的交叉容量。

来源为[Haran, Non-additive geometry](https://doi.org/10.1112/S0010437X06002624)，Compositio143(2007)618–688。原PDF 1032382 bytes/71页，SHA256 `1befc0e1fa8465d29a452d75bbcf02ded93a50b12c179a0b48303570ca60570f`；全文仅本地ignored。实际消费印刷627–628的公理、632 Example1、671–675的§7.1/7.2；附带曝光及未读范围见[准确记录](../literature/supplements/2026-10-29-haran-fibred-sum-source-scope.md)。这是本项目从有限公理推得的命题，不把作者后章标为已审。

## 2. 全矩阵唯一性的有限证明

给定f0,f1:M→C，作者的完整tensor双函子允许任意C态射的mixed interchange；两f均固定F且保⊕、⊗与composition。不先假设C可加。

在M中取σ=[1 1]:2→1、δ=[1;1]:1→2。取F中的部分双射j:2→2⊗2，两个点送到(1,1)、(2,2)，及其部分逆π；不需要C有transpose。写σk=fk(σ)、δk=fk(δ)。源整数矩阵中有

    (id2⊗σ)j=id2=(σ⊗id2)j，
    π(id2⊗δ)=id2=π(δ⊗id2)。

经各fk保留后，mixed interchange给

    (σ0⊗σ1)j=σ0(id2⊗σ1)j=σ0
              =σ1(σ0⊗id2)j=σ1，
    π(δ0⊗δ1)=δ0=δ1。

固定F中的unitors、排列与分配同构省写，所有箭头仍有原有限集类型。因此得到共同Σ、Δ。在End_C(1)定义a+b=Σ(a⊕b)Δ。结合、交换、零单位分别来自源fold/diagonal的有限三项字词和F中的swap/zero，给交换幺半群。两份(-1)都是1的逆元，逆元唯一使它们相同。迭代共同fold/diagonal得所有非负整数相同，再由(-1)及composition得全部整数相同。

不能止于标量层。对任意非空有限X、Y及A=(a_yx):X→Y，源中有准确typed word

    A=(id_Y⊗σ_X) D_A (δ_Y⊗id_X)，
    D_A=⊕_(y,x)[a_yx]，作用于Y⊗X。

右项复制X到Y×X，中间乘各标量，左项对x求和。所有因子在两f下相同，故f0(A)=f1(A)。空X或Y由零对象唯一性处理，完成全矩阵证明。

独立反向证明由任一M→C产生所有Hom上的加法；完整tensor自然性使composition双线性，源矩阵恒等式使规范包含/投影分解id，故⊕为真正biproduct。第二整数拷贝的fold/diagonal由双积泛性质唯一，再得整数及全部矩阵唯一。此证明核了任意C箭头的自然性，不把仅在源像内成立的性质偷渡给目标。

## 3. 自余积不依赖一般存在性

F是初对象。对每个C，相容的两条M→C必相等，因此Hom(M,C)到其两份在Hom(F,C)上的纤维积为对角双射；若无映射，两边都空。M的id余锥合法且直接实现所需泛性质，无须一般Theorem7.1的任意输入存在性。

若另选B，则Hom唯一性先给i0=i1。fold有d∘i=id_M；i∘d与id_B在两结构映射后均相同，余积唯一性给i∘d=id_B，故两map互逆。M不是初对象；准确说初始箭头F→M为epi，不能把Hom(M,C)方向换成Hom(C,M)。

## 4. 严格忠实零约定的有限问题

Definition2.1要求F→C忠实，因而0_(1,1)≠id1。Example1的Mat(F2)、Mat(F3)均为合法非退化输入。若它们有共同C余锥，两条整数约化复合M→C由上文必同。但整数3经F2给1、经F3给0，矛盾。

因此字面非退化类别中该pair无共同余锥，不能无说明地消费“一般所有pair均有fibred sum”；须明确退化零范畴的忠实性例外或适用输入的限制。没有查遍作者其它章约定，不能据此宣称整篇错误。selfpair已有id余锥且直接证明不受影响；具体有共同F(Q)目标的紧化图表也不能一起排除。允许退化零对象的修复仍不改变本自配对证明。

原定位误用module tensor⊗，已冻结并更正为F-ring余积⊚；Remark7.1.9明确前者到后者一般非同构。Root另一个草稿的Spec projection标签曾写反，原文保留、追加正确方向并经fresh重闭，见[语义更正](../reviews/2026-10-29/post-600-new-input/haran-faithful-zero-and-selfcase-scope-closure.md)。本稿只用正确方向。

## 5. 强旧、责任和停止

363的标准Λ-ring中Z为初对象、自余积为Z，属于Borger的另一类别，不能抵扣本次Haran公理下的wholematrix命题；这里F才是初对象。Paid短链为actual mixed interchange→共同fold/diagonal→全部整数→全部矩阵→自pushout同构。无近似、范数费用或成长参数，不能由这个有限链免费获得physical源或谱覆盖。

本门完整否定的是该ordinary affine构造中“两份整数结构独立”这一可证伪前提。没有构造r→D_r，没有405全Pan消去/537非根/全源coverage、整截面/mixedRR或完整Γ/contact/properpowers/双pole身份。关键primitive/principal/mixed、dangerous signed corecross、成长Ξ及whole4/5负惯性UPPER未改，长期Goal三门open。

前置秩三连接的必要中央系数exact等于已付holonomy Green系数，0重复撤销；新pointwise Euler gauge Gram未减bulk时在每个先fixed finite F含2的层非紧，直接由旧560 carrier给det域0止。它们不分拆为601。Haran这个此前未付实际类别的完整有限准入反例统一计一次：原cadence2→3/history64→65/latest601，formal20保持，非macro21。两原证明、零约定直接推论、审查/来源/发布均不另计轮。

停止本fold、frames/rank/det2/参数及作者后章/其它年份/ref的续批。其它类别、紧化边界、额外actualdata、不同正则化和独立正D′机制仍未排除，亦无自动预算。下一研究需不同的实际principal/mixed或完整signedcore公式及可改变选择的测试，不能把未付桥改名重授。

完整原稿12921/11645、不同fresh16122均冻结并由root全文核对。实际前件、raw哈希、计轮和未付箭头见[root消费记录](../reviews/2026-10-29/post-600-new-input/root-consumption-scope.json)。
