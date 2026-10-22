# 独立逆审：源依赖除子族与相对截面

2026-10-22。独占复核稿；不修改共同STATE/cadence、Goal、合同或Git。
复核者未参与三份构造稿的撰写。结论为**限定范围PASS**：实际解析截面与相对评价已构造；
没有取得独立经典算术容量或完整Weil正性的证明，不准入C036/573，不改变长期完成门。
本收据的hash仅绑定版本，不充当数学证明。

## 1. 实际核读与独立检查

完整核读本轮主报告和三份构造稿。为复原前件，另读405 §§1–6、519全稿、553全稿、
568 §§5–6，537的原源定理/常数、552 §§1–5，以及567 §§2–3的曲面RR到全周期源Gram。
独立重新检查以下关键代数、算子范数与对象角色；未重跑537的computer-assisted证书，
未重证518/Meyer闭像或函数域Hodge定理；这些依赖按已经结算的准确范围消费。

外文仅核[Stacks 31.15](https://stacks.math.columbia.edu/tag/0C4S)的regular-section定义与
[Lemma 31.15.10](https://stacks.math.columbia.edu/tag/01X0)，以及
[30.8 Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XS)的单项式/Cech论证。
Stacks的scheme表述没有直接替复解析空间支付定理；本例的非零因子、图和restriction均已局部直接检查。
未打开新的论文链。

## 2. H-base上的实际section与正确商

固定物理源r=e^(u/2)f及A_r(z)=M_f(1/2+z)。405原式给A_h=Xi/2、
A_p=(z²−1/4)Xi/2；这里h、p均须在physical S_exp扩张域消费，不能冒充compact输入。
H=(z²−1/4)Xi的闭解析子空间以V(H)为底空间、限制的商sheaf为结构层。
这保留重数/nilpotents；不用RH或简单性，也不要求底空间有限。

对a=[A_r]_H，sigma_r=−aY确为O(1)的global section，复线性依赖r。
它可能为零或零因子，不能一般称为regular section；s_r=X−aY在Y≠0图上为monic x−a，
其零空间与base同构并且flat，在另一图上也无零因子问题。因此marked section、
regular graph以及相对Picard类是不同目标。div(s_r/X)=Gamma_r−Gamma_0，
故仅取Picard类会把r0一并丢掉，不能用它兼领marked-section的非根可见性。

kernel=physical P_an的论证依赖519(1)的实际像=完整zero-jets，再加两个degree矩；
不是任意entire除法自动得到Schwartz源。去掉degree的Xi商承载Q，但保留全jets，
在重根时不等于最小trace根商。普通局部multiplication trace只读m倍常数项，
nilpotent方向仍为trace radical。四稿均保留了这一区别。

Xi(±1/2)=1/2使H-base分为primitive部分和两个degree点，h的degree值为(1/4,1/4)。
537的r0=(D²−1/4)psi非零、双矩零且Q(r0)>0，因而其primitive值不能全零。
这合法地通过405与537测试，却用旧completed-divisor谱商作为base，不是独立算术来源。
raw A_r/H在p上等于1/2；必须模去entire sections才消关系。
literal H w=A_r的纤维会从空变为整条仿射线，其projective closure也有整条P1纤维；
它不能替代上述flat graph。源乘法是卷积，O(1)乘积在O(2)，也未被无费混同。

## 3. 原du/Dlog费用与全部关系量词

固定(-L,L)的k阶读出具有精确L² squared fee

    integral_(−L)^L u^(2k) exp(2 alpha u) du。

以光滑函数逼近极向量取得上确界，精确性成立；它不是Dlog的同一个精确Gram。
Dlog原范数使用全线zero extension，四稿正确保留restricted dual上界、固定窗/固定k费用，
不把对角控制冒充全部高度、全部重数jets的共同operatornorm。
553的critical fee对ALL gamma、L≥1；offcritical指数渐近仅对先fixed alpha≠0、gamma、k。
principal-part坐标还含H局部leading derivative倒数，不能偷用高度/间距一致常数。

553已给全部r_p平移span在全线L²/Dlog稠密；全线原norm连续、全部principal-coset不变的
Hausdorff值map，即使非线性也常值。这是旧结论，本轮没有升级或重新计功。
原Fréchet/解析局部拓扑、compact输入窗口收费、varying domain和matched cocycle仍是合法逃逸，
不能用上述旧结论否定所有family。

## 4. 不用谱商的具体候选及其失败范围

加权正交投影probe确可同时杀指定p/h并保r0：h、p实解析且在任一开区间线性独立；
compact r0不能在含其支撑的较大开区间等于该解析线性组合。相应Gram正定，
残差平方严格正。该smooth probe的原du/Dlog费用和FS sup范数均可付。
但全部平移被杀会由Fourier唯一性迫probe为零，故确有实际principal平移失败。
complex参数纤维也不能凭Z[t]普适式免费取得每个p-adic specialization。

投影Gaussian族中A_P为原L²正交投影，C_a=||kappa_a||₂的常数及
||phi'_r||²≤(ae)^−1||r||²来自sup_t t² exp(−a t²)=1/(ae)，均正确。
S_exp/Gaussian衰减足以在0、infinity光滑flat延拓；逐源integrability按552原比较闭合。
compactified曲率费用仍允许O_a(e^(2L))，未从sup高度小费中删掉。
P被严格消去、r0保留非零vertical能量，但任意非零平移tau_b P不与P共线，故仍不下降全部关系。
有限位标准frame下小截面的N消失预算log N≤inf Phi_r正确；它未从源生成prime-power阶。
pole-only族消全部指定关系却丢掉r0；主pair族的代表跳跃也没有同对象预算净增益。
这些结论仅限定给出的候选，没有排除全部relative/adelic/source-adapted构造。

## 5. 同对象flat评价、连续反测试与函数域

E_t:x(x−t)=0的代数在Z[t]上以{1,x}自由，长度2且flat。
m≥1时O(m)完整restriction满射，其kernel通过乘x(x−t)与H0(O(m−2))同构。
在该flat基中x^m余式为t^(m−1)x，所以选列{1,x^m}的minor确为t^(m−1)；
裸双点评价的t^m多含一个collision/frame因子。完整截面空间一直有{1,x}的minor 1。
因此坏minor对数发散只拒固定坏选列/无费frame，不是所有载体或实际源的necessary lower。
这里确有同对象消失order/global degree/线性容量比较，未产生曲面signed平方RR。

对R_d=C[z]/(z²+d)、z dagger=−z及系数共轭，独立展开给

    tau((A+Bz)(A+Bz)^dagger)=2|A|²+2d|B|²。

两个非零号的底层C代数都为C⊕C，但正d的dagger分别固定两个idempotents，负d交换二者；
普通复截面容量不足以看见实极化。d=0时length和trace重数仍为2，nilpotent方向是根，
不能从同样的local jets强制其Weil可见。换d为|d|是在换原目标配对。

函数域对照准确：先有C×C上的独立有效性/乘法/RR/Hodge，再把交数延拓到全复源。
567(4)的E_r(y)对每个compact源只有有限指标，并保全部period aliases、proper powers和a0；
这里不需要每个任意复组合先是integer Cartier divisor。有限分子商不是全连续时间源。

## 6. 完整Weil责任、旧强扣除与PASS边界

主稿(9)逐项等于568(14)：双pole mixed项、Gamma0=psi(1/4)−log pi、
w(v)=2 exp(−v/2)/(1−exp(−2v))、全部p^k及log p/p^(k/2)系数均未删除。
旧显式公式把它识别为primitive Xi trace，但本轮没有证明它是同一算术section/determinant
的arch原容量减finite位消失预算。sigma_h非零而Q(h)=0，已拒全H-base忠实正norm直接等于Q；
重根时还必须保trace nilradical。要求Gram恰为Q且全部PSD仍是Weil等价条件。
有额外零点的B改变base，entire unit不改base却可改principal-part frame；本构造未独立选规范。

PASS仅覆盖：给定旧源/growth的真实analytic global-section map；
具体probe/adelic metric族的原范数成功与关系失败；flat restriction修复及同对象曲线容量；
连续/函数域控制的上述准确量词；完整Gamma/pp/pole目标的保留及独立容量缺口。
不覆盖：新经典正性、独立平方容量、有限位specialization、全源joint成长费用或所有family no-go。
本轮是旧谱商/范数门和初等相对几何的具体准入组合，0数学轮，无C036/573。
strong-old542+555→557 whole leading4/5仍只是issued上预算；actual低频/core/coupling/Xi、
Goal冻结基线/版本、原cadence1及正式cycle14均不改变。

## 7. 审阅版本绑定（UTF-8、统一LF）

| 文件 | LF SHA-256 |
| --- | --- |
| goals/reviews/2026-10-22-source-dependent-divisor-families-and-relative-sections.md | 7a534cc04313a7f08d333036849e6117b050d27fa7ffc6642425f7b4fdb66ad8 |
| reviews/2026-10-22/source-dependent-family/relative-divisor-construction.md | 7cba0c8d021c3df3d9868dbbaba158a5db6a41df62077cc06a9f53c6eae15bad |
| reviews/2026-10-22/source-dependent-family/relation-nonroot-and-original-norm.md | b1d42fdf88b186436f52cb3b0834933ae030851eebfd75106f4c0ef4f1bd81d9 |
| reviews/2026-10-22/source-dependent-family/local-global-relative-budget.md | 5155d5f1dda74810e5ffbbf1014b34c3c509f0e96006e51c69220017431cf955 |

若以上数学正文修改，须重新核相应依赖后更新绑定；组织性状态/同步回执不自动更改本PASS范围。
