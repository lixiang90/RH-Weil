# BC §7.2 原文首门：真实全局交数设施，物理源桥未付

2026-11-01；/root/bc72_primary_reader。SAME G20261027/0c4f 输入；本稿是指定来源审查，非新数学合同或ROOT消费。建议 SOURCE/INPUT0 止，不建C070、不计607，不推断全部formal-analytic方法失败。

原件为Bost--Charles，arXiv:2206.14242v2，修订2022-09-14；本地PDF189页/1907786B，SHA256 fc8eef2982b7e4fbcb14e7a175671afaef0802ad358ba5ce1169a80cab5d2480。不能以2026出版书替代这份字节版本。

## 1. 实际阅读及未消费边界

完整抽取§7.2：PDF130–137及138上段、印刷106–114中7.3标题之前；并目视核父线程生成的bc72-130.png至bc72-138.png，138仅消费上段7.2.22。PDF138下半的7.3开头因整页抽取/渲染被曝光，未作为输入使用，未继续7.3/8/9或参考文献。

仅为对象定义读取6.1.1/PDF108–109、6.2/PDF113–115及7.1/PDF127–129。6.1.2的向量丛定义及7.1.2的章节同页内容有曝光；不据此新增截面/RR定理消费。未追溯第3–5章的证明或Bos20。下述等式标为来源cited；本节内证明读过，不等于所有nested定义、正则性和规范已独立重证。

另有两项定量消费留置：6.2.13的Dirichlet配对符号不在本门另读第3/4章裁决；7.2.19的系数链有下述未闭合处。二者均非本次拒绝物理源晋级所需前件。

## 2. 原对象、系数和态射

K为数域，O_K为整数环。平滑formal-analytic算术曲面Vtilde包含：Noetherian仿射形式概形Vhat，约化定义概形通过结构映射同构于Spec O_K，且形式光滑、相对维数1；每个σ:K→C有连通紧致带非空边界的Riemann曲面Vσ及内点Pσ；复形式芽经ισ与Vhat_σ相配，满足复共轭相容。P:Spec O_K→Vhat是典范截面。

6.2给出的紧支撑Arakelov除子群满足

    Zhat_c^1(Vtilde) ≅ Z ⊕ C^{bΔ}(V_C)_{R,Dir},
    (n,φ) ↦ n(P,g_eq)+(0,φ).

算术部分D=nP，n是整数；Green部分是实值、复共轭相容的C^{bΔ}函数，在外部Vσ^+\interior(Vσ)为0。它不是自由复系数的物理源空间，也不是只有一个标量：Green部分仍无限维。不能用nP一项的有限秩否定全部metric源，亦不能把complex cycle系数视为整线丛。

7.1.1的态射α=(αhat,(ασ))由O_K形式概形态射与各Archimedean解析映射组成，二者在Pσ的形式芽由ισ相合。7.2的目标X是Spec O_K上的整、正规算术曲面，α非恒定。Q=αhat(P)为O_K截面，e(α)>0为generic形式曲线态射的分歧指数。

本稿中的P、Q是几何截面，不是Weil空间上的投影或二次型；残余除子R也不是旧R_tail算子。末尾圆盘例原文用r表示半径，本稿改记ρ，绝非本项目物理源r。

α_*将(D,g)送至(αhat_*D,(ασ_*gσ))，算术部分只是nP→nQ。Prop7.2.1/(7.2.1)给再复合的direct-image相容。Prop7.2.2文字量化(D,g)，显示式(7.2.2)写的是(P,g)：

    α^*Lbar · (P,g) = Lbar · α_*(P,g).

本稿仅消费这个显示的P情形，不自行把排版改成全源mixed/Hermitian身份。Lbar的metric须C^{bΔ}。7.1.2中截面范数结论另假X reduced、proper、flat及体积条件，不能把那些假设或John/L²范数与7.2、物理du-Dlog混用。

## 3. 有限位overflow及证明范围

X正规以外若先假regular，则Q Cartier且

    αhat^*Q = e(α)P + R,                         (7.2.3)
    E_fin := deg-hat(R·P)=Σ_x n_x log|κ(x)| ≥0.   (7.2.5–6)

R有效且与P proper相交，n_x为交局部长度。仅normal时Q为Q-Cartier；选择NQ Cartier后以N^{-1}αhat^*(NQ)定义拉回，R和交0-cycle可为有理系数。勿把regular情形的有限环阶数表达无条件搬到所有normal情形。

Example7.2.3在Vhat=Spf O_K[[T]]、X=A1_{O_K}、αhat=a0+Σ_{i≥e}a_iT^i、a_e≠0下给

    E_fin = log|N_{K/Q}a_e|,

并以a_e为unit刻画其为0。这是实际整数/局部算术资料，不是任意加上的Archimedean常数；但尚未给物理源诱导这些系数的规则。

Prop7.2.5在αhat quasi-finite且ND Cartier时声称N^{-1}deg-hat(αhat^*(ND)·P)=log n，n为正整数，因此非零时≥log2。印刷108页明确说证明只给所需的较弱非零下界，把更精确整性推导留给读者。故强整性仅记CITED statement，不把当前已印证明升级为完整整性重证；本门不补该证明。Quasi-finiteness也不是7.2.13的一般前提。

## 4. 真正的全局公式及其符号

令gσ为Pσ的上述Green函数，Nbar_{P,g}为带相应capacitary metrics的法线丛。Prop7.2.6/(7.2.8)给

    I(α,g):=α_*(P,g)·α_*(P,g)
      = e(α) deg-hat P^*Nbar_{P,g}
        + E_fin(αhat) + Σ_{σ:K→C} Ex(ασ,gσ).

这是同一态射的有限位和全部Archimedean位的真实global arithmetic交数公式。其本节证明经Lemma7.2.7、NQ Cartier化和线丛限制同构，再与Archimedean积分结合；不是只有一个孤立的Green-current方程。所有σ按原文求和，不另插半因子。

g=g_eq为典范equilibrium potentials时，Cor7.2.8/(7.2.13)为

    I(α,g_eq)= e(α) deg-hat P^*Nbar_P Vtilde
               + E_fin(αhat)+Σσ E_arch(ασ),

原文用overflow非负推出Cor7.2.9/(7.2.14)：

    I(α,g_eq) ≥ e(α) deg-hat P^*Nbar_P Vtilde.

不等式右侧法丛算术次数的符号未由此支付。它不是I≥0的无条件结论，更不是全部g或所有mixed除子上的PSD。一般g的Ex(ασ,gσ)不能直接继承equilibrium choice的非负性。第5章overflow非负性在本门只按本节cited依赖使用，未扩读其证明。

Prop7.2.10另假Q落在X的regular locus，选择对角Green g_{Xσ}及其C∞实2-form βσ，配上capacitary normal metric，给(7.2.15)：

    I(α,g_eq)=deg-hat Q^*Nbar_Q^cap X
       +Σσ [2∫_{Vσ} g_{Vσ,Pσ} ασ^*βσ
             −∫_{(∂Vσ)^2} g_{Xσ}(ασ(z1),ασ(z2)) dμσ(z1)dμσ(z2)].

必须保留boundary双积分的减号；βσ在此是实form，不能擅加正性。式(7.2.16)还带负的log jet norm，(7.2.17)以同一e-jet将其与normal degrees及E_fin配对。这些是native Arakelov/capacitary度量，未与本项目fullΓ或du-Dlog建立等距关系。

## 5. 两个圆盘实例：有实物，仍非Weil源

7.2.4.2给ψ∈R^*X+X²R[[X]]，向A1_Z的非恒定态射由αhat∈Z[[T]]及解析αan配合，必须满足

    αhat = αan ∘ ψ.                             (7.2.18)

因此native载体及整性、形式/解析相合是实际条件，不能任意指定一个源函数便获得态射。印刷112页(7.2.19)的字面式是I=2∫_0^1∫_0^1 log|αan(e^{2πit1})−αan(e^{2πit2})|dt1dt2。

**7.2.19的定量消费留置。** 目视确认其显示2；但同节(7.2.15)有负的一份boundary积分，其A1证明给β=0、g_C=log|z1−z2|^{-1}、capacitary tangent norm1，次页又称μ为normalized Haar概率测度。按这些所列数据直接代入会出现一份double-log而非所显示的两份。本门不修补系数，不声明出版版错误、作者erratum或新的数学反例；只冻结该corollary的精确定量消费。主物理源输入门不需解决此处。

7.2.4.3的P1例改取半径ρ的圆盘、非恒定formal/meromorphic资料及同一gluing；Cor7.2.12/(7.2.21)为

    I_ρ=2 ht(α(0))+2 T_{αan}(ρ)−boundary double-Green integral.

源中g_{P1}≥0仅给(7.2.22)的UPPER：I_ρ≤2ht(α(0))+2T_{αan}(ρ)。不许把它消费为Weil正性lower。高度、Nevanlinna characteristic与原Weil频高不是同一变量。第5章所引Green/characteristic定义在本门未重证。

## 6. 最便宜晋级门与根消费范围

本节确比“只有Archimedean Green设施”强：已经把给定formal-analytic态射的finite overflow、capacity法丛次数和Archimedean边界项放在同一global交数中。不能贬成空载体或纯形式口号。

然而，它没有提供本项目全complex S_exp或compact-Dlog物理源到上述integral divisor、αhat/ασ及gσ的实际公式；没有说明405全部真实noncompact关系及其平移如何principal下降、哪个非零primitive仍可见，亦没有给source覆盖/逆费。整数nP和real Green群不自动等于这个复源域；原物理r=e^{u/2}f及原norm必须另运输。

它也没有把native交数的任意两个独立源mixed配对识别为完整经典Weil型。有限交局部长度的log|κ(x)|不是已经付费的全部Λ(p^k)p^{-k/2}系数，更没有fullΓ/FP-contact、双pole及其原符号的同对象matching。原normal degree、Green choice或有界边界资料不能按定义命名为缺失的classical capacity。Height/ramification/radius变化不等于已付uniform source/growing-window量词。

所以第一道“实际物理源→同一全局几何比较”的前提尚无新实物；SOURCE/INPUT0是本明确来源门的停止，不是上述native定理被否定。法丛sign、mixed/full-Weil matching和成长norm不能仅改名成为下一数学合同。最强旧whole17/16、9/8有限头/同605全部补空间正完成、whole4/5负惯性UPPER及长期三个完成门均未改变。

停止本§7.2来源门；不续7.3、8、9或参考文献，不运行科学源/Gram，不提供C070或新计轮授权。ROOT仍须结合独立transport审查、最强旧573–575/GS及实际字节后决定消费；本稿不操作STATE、cadence、文献manifest或Git。
