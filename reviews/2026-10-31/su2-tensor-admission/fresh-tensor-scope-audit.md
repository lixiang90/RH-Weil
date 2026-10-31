# 不同组织逆审：实际 SU₂ tensor 的来源、谱角色和有限停止范围

2026-10-31；`/root/su2_fresh_scope`。同G20261027、原0c4f基线；只写本稿，不修改STATE／Goal／cadence／库／其它原件，不创建Goal或新数学合同。当前root原稿9757bytes和独立old-role终稿14227bytes均已逐段阅读；后者在收到**当前任务终稿**消息并核其实际字节/hash后才消费，不借旧agent状态替代本任务。

**裁决：限定PASS，没有阻止本门source0／标准旧推论0结算的问题。** 新读的Theorem A确实给这个非平凡局部tensor族全部对称幂的cuspidal automorphy；不能继续笼统说“没有任何真实全阶pole族”，也不能把本族套入旧C₂两个固定因子的封闭分类。它尚未提供目标ζ全球零点的谱放大／独立定位或完整型的新符号控制。停止的是当前直接消费，不是证明整个functoriality或Deligne类比不可能；Goal三个完成门仍open。

## 1. 本人实际来源核验与曝光

我对本地固定PDF重新核了签名、101页、1249898bytes、SHA256 `6d50b558a6182a8d1515a6715529a33079807bf405c8db775e4ed252f5a2f379`；实际抽取并阅读仅PDF1–2，且分别视核已有Poppler图像PDF1、PDF2。首标记为arXiv:1912.11261v3、27 Sep 2021，作者James Newton与Jack A. Thorne。本人未重新下载、检索、打开外链，也未读PDF3–101、作者证明、参考文献或II。PDF文件继续本地ignored，source-receipt核的是下载实际对象，不把它视为公开再分发许可。

PDF1 context所定义的R(π)匹配是每个place的**local Langlands parameter**经过R；不是全球非平凡零点空间的tensor函子。PDF2 Theorem A明确以regular algebraic、cuspidal、level1的GL₂(A_Q)为输入，对每个d≥2给regular algebraic **cuspidal** GLd的Sym^(d−1)π。必要的前置段说明weight≥2 holomorphic forms属于此范围。对Δ用此结论是合法的；level1只说全部finite places不分歧，不把π∞的离散系列误称spherical unramified。

Theorem A被作为已发表深结果的**cited statement**使用。本人没有审其证明。整页抽取和图像使相邻Theorem B、Corollary C、历史／Strategy段及脚注曝光；它们不作为Δ额外解析结论的证据。PDF1的TOC和背景历史也不等于相应章节已消费。期刊版116页与这里arXiv固定101页须分开；本门没有混用两版页码。

完成化的尖点L整性／FE以及s=1非零，均为root**另行标明的标准外部解析输入**，不是从Theorem A原文当页读出了证明。本稿按该标准背景核消费方向，未新审其作者证明或参考文献。更弱的条件消费也足够停止：即使暂把这些解析性质全部授予，缺的全球目标定位仍不随之出现。

## 2. 对象与规范：不预用局部纯性、不制造half-Tate motive

固定Δ的unitary GL₂规范，central character为1，故每个finite p的α_pβ_p=1，t_(p,k)=α_p^k+β_p^k实。这一实数性质来自实Hecke系数和det1的递推，不需要先假|α_p|=1。实二次多项式的根在未纯化时可为实互逆或单位圆共轭，因此偶幂t_(p,k)^(2n)非负并非循环借用待提取的local temperedness。“SU₂”只在已纯化时可按紧群字面理解；标准SL₂表示环恒等式在此前已经可用。

原稿明确V是**局部unitary参数**，未把Δ的weight11 motive作不存在的half-Tate对象。若另用标准Δ motive／Galois背景M，则M^(⊗2n)(11n)的整数twist将weight22n归零；分解项Sym^(2j)M(11j)同样只用整数twist。此说明避免规范偷换，但不升级为本页已经证明某个global zero realization。

这里采用的标准自守背景还包括：π及本次偶对称幂lift的central character为unitary（在本规范实际为1），cuspidal realization因此可按unitary标准L的解析定理消费。没有凭Theorem A的“regular algebraic”四字普遍授权任意非unitary twist的中心规范。这个背景与作者本次statement证明范围仍分开。

## 3. 全有限阶因子、pole与zero三个方向

标准SL₂ character比较给，对所有有限n≥1，

    V^(⊗2n) = ⊕_(j=0)^n m_(n,j) Sym^(2j)V,
    m_(n,j) = binom(2n,n−j) − binom(2n,n−j−1),
    c_n = m_(n,0) = binom(2n,n)/(n+1),
    Σ_j m_(n,j)(2j+1) = 4^n.

可直接以(x+x^−1)^(2n)中相邻权重系数相减核全n，不必从n=1、2的样本外推。n=1为1⊕Sym²，n=2为2·1⊕3·Sym²⊕Sym⁴，与维数4、16一致。Det非1时的GL₂式要留det幂；原稿只在已固定det1后消去，方向正确。

逐finite place同一identity在共同右收敛域给

    L_n = ζ^c_n ∏_(j=1)^n L(Sym^(2j)π)^(m_(n,j)).

这是实际已分解tensor的direct-sum L乘法，不是把一般tensor错误定义成L(π)的普通幂。没有漏掉bad primes；level1在这里确实全部finite places不分歧。先固定n、在合法收敛域辨认Euler因子、再以各有限因子的延拓继续；不在临界带交换无限Euler乘积。

必须保三种不同前提／方向：

* 只授予辅助cuspidal **completed L整性**，completed Λ_n除0、1外无pole，在端点至多c_n阶。不能仅凭整性说阶数恰好c_n。
* 精确端点阶使用各辅助finite L(1)≠0的**另行标准非零输入**及FE。原稿已明确支付这一引用条件，没有偷把整性当非零性。此首检其实只需上界。
* 对任意非平凡ζ零点ρ、任何重数mρ，所有辅助整因子在ρ没有pole，故ord_ρΛ_n≥c_n mρ。Γ参数在0<Re s<1没有额外pole，completed ζ与ζ的零阶相同。辅助零点若重合只会加重数；无需假“互不相交”。

因此本族**看得见并保留**目标零点，不能笼统称没有任何目标桥。但它保留的是同一s平面位置ρ并增加重数；没有把ρ送到1/2+n(ρ−1/2)，没有Θ_ζ的已识别tensor-sum／乘积，也没有target global Künneth或迹定理。Automorphy／整性／FE／端点pole信息没有给这个新L_n的RH。

如果后来独立证明某个L_n全体非平凡零点都在中心线，保留关系即可传递RH，不必强迫该证明先走405几何Pan路线；如果只得到Q_n≥0，则也须准确支付Weil判据或辅助型的消费责任。原稿和独立稿均保留了这种合法直接global入口。

## 4. Landau消费仍是同一个局部α

右侧合法域中

    log L_n(s) = Σ_p Σ_(k≥1) t_(p,k)^(2n)/(k p^(ks))

有非负系数，指数化给L_n的非负Dirichlet系数。粗polynomial Hecke界提供一个可依n的初始有限收敛横坐标；并未先用|α_p|=1。对每个fixed n，若收敛横坐标σ_c>1，Landau非负级数实奇性会在σ_c产生奇点，与有限L_n在实s>1全纯冲突，故σ_c≤1。没有把完成化Γ的pole当普通Dirichlet级数pole。

若某个fixed p有|α_p|=a>1，则两个根实互逆，|α_p^k+β_p^k|=a^k+a^−k，局部非负级数至少具有2n log a/log p的横坐标。因而2n log a/log p≤1。先保持p、n有限并合法比较，再用全部n令n→∞，得到a≤1；det1与对偶夹出local纯性。若根一开始非实，则实系数det1已使其在单位圆，不存在遗漏分支。

这是一个真实的标准Deligne／Landau提纯代入；其被放大的参数是**α_p**。全球ζ零点ρ不是L_n的奇点，不能按pole套Landau；它在该族中的重数增长也没有使其s位置改变。即使全阶pole控制完全无误，也不能把这两个不同结论拼成RH。002§2、073§4、567§6已先付这条谱角色区别；当前没有新目标谱识别。

## 5. Γ parity、degree和原源域

我独立以real Weil参数核原稿公式。Δ∞的二维参数为I_11；在Sym^(2j)中，中间单项式e₁^j e₂^j在J下的号为(−1)^j，因此给sgn^j与Γ_R(s+ε_j)，ε_j=j mod2。其余成对权±22a给I_(22a)，L因子为Γ_C(s+11a)，a=1,…,j。于是

    L_∞(Sym^(2j)π,s) = Γ_R(s+ε_j) ∏_(a=1)^j Γ_C(s+11a)

正确；j=0回到ζ的Γ_R(s)。本段是标准参数的直接有限代数核验，**不是**从新PDF当页消费的作者公式。一个Γ_C计degree2，故总degree D_n=Σ_j m_(n,j)(2j+1)=4^n，且

    D_n/c_n ~ √π n^(3/2).

这只核计账比值，不构成Γ净误差的必要lower，也不排专用源、signed相消、联合尺度、非局部或relative修复。原稿没有用该ratio单独宣布整体no-go，裁决范围合格。若某条后续方法直接给全球正性而不走谱幂，它应按自己的完整输入审查，不能被“没有谱幂”一句预先排除。

对每个fixed n，同一合法compact复源上的完整显式公式可按direct sum相加，Q_n=c_nQ_ζ+Σm_(n,j)Q_(2j)；不能从正Dirichlet系数偷出任一Q≥0，也不能仅从Q_n≥0减去未知辅助型而得到Q_ζ≥0。原du／zero-extension Dlog、各自Γ/contact、全部proper powers和endpoint的multiplicity都必须留在实际公式中。本门没有对n无界给uniform source-norm或成长窗极限；没有把native automorphic fiber当physical r、principal class、primitive carrier或其norm运输。

## 6. 强旧净值、停止和完成门

002§2已区分local纯性和ζ全球零点；073§4已明确local Satake tensor与global zero-space tensor不同；567§6的全tensor pole机制约束的是原局部特征值。它们是本门停止理由的短依赖链。旧C₂原收据的“两个固定简单对象／两个固定L因子”是更窄范围，**不能**当成本次SU₂无限多对称幂factor的排除定理；原稿与独立稿都正确区分。

Newton–Thorne原文是实际新cited文献输入，不能写成没有新来源；标准代入后没有新经典全源／成长／signed核心净后果，所以此门source0、标准强旧0，而非一个新数学合同或一个新的实质核心方法类边界。全部physical→principal／sections／mixed、危险core／cross、成长Ξ及whole leading4/5负惯性UPPER保持；此UPPER不是正性、比例或负谱lower。

本稿不许可继续作者证明／II／引用链、换level／CM／weight／tensor阶数或追加参数预算。真实不同的global realization／trace／目标谱传递，或直接支付完整目标的新独立符号控制，才可推翻当前选择；现有尚欠的箭头仅改名不算新输入。保留relative／lax／graded／无限结构、joint signed及源适应修复，不因它们未排除就预准入。

本人的实读支持**0新增数学轮、0宏观周期重置、0Goal完成**。唯一cadence实核仍为6813bytes／SHA `0bd41adf77ca1d22895c9a42e808ef3e627c929bc639cce0f782ceaee4aa2041`；0/history66/latest602/formal21。库登记141→142是root待执行的metadata工作，本稿不宣称已登记／发布。Runtime active只按root本轮实际观察记录，child没有重建Goal或用child-local null推状态。

## 7. 核验版本与执行限制

当前原稿和支持终稿是待root消费的原件，不能用本稿PASS替代root对前件和净值的结算。引用的原字节版本：

| 文件 | bytes | SHA256 |
|---|---:|---|
| root-tensor-and-source-comparison.md | 9757 | 74805a9e705f6c0cf32d774110f860b75d92fc6b9922368d601a395a48df587c |
| strongest-old-and-spectral-role.md | 14227 | 08e76e75050a595cca01544ac12ddea17c4935dc0f9a40dfdeccc0c410609ee4 |
| source-receipt.json | 672 | 2c5222282435a57c6706b6e83b6289efd6cfc08a37a3460f343b6affacf9a6c9 |
| goals/GOAL.20261027.md | 9679 | b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de |

已恢复README／STATE、check→show、Goal／C065／macro21／AS和前沿入口，并看实际working tree。旧567第一次按猜测文件名读取失败，随后用rg定位并直接读取实际文件§6及邻近限定语；失败locator不是来源不存在的证据。旧C₂收据当前实读到对象／谱角色／停止范围，未把其中历史cadence／manifest绑定叫当前值。本稿未重新审旧证据的全部证明，也未审原作者后续章。所有hash只绑定本次原件，不认证数学或完成Goal。
