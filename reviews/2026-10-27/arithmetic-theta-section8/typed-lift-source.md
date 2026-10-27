# Kudla作者稿§8：算术theta lift的准确类型与消费边界

2026-10-27；/root/theta8_source 独占来源稿。只执行STATE指定的§8来源门，不改STATE/cadence/Git，不预建C048/585。出稿不代root消费。结论分类为**来源陈述/类型核查0数学轮**；本章没有提供本项目physical源桥或完整经典Weil身份。

## 1. 实际原件、目视范围和依赖等级

原件是Stephen S. Kudla，*Modular forms and arithmetic geometry*，作者CDM.revised.pdf。本地文件56页、887943字节，原SHA256为47ff2ff6f5151081dd029a1df680377b88d58fc09d6629f3a2b2c3b78bab0f54；没有更换版本或下载其他文献。

已完整目视PDF31的§8标题以后及PDF32的§9标题以前；(8.1)–(8.6)全部核读。必要定义定位：PDF7 §2(2.1)–(2.5)，PDF24–25的(7.1)–(7.4)/Prop7.1；必要依赖陈述定位：Th6.3在PDF23，跨页解释到PDF24；Th7.2在PDF26；Th7.4在PDF30。另目视了PDF7、26、30的相关定义/陈述和脚注。未读这些定理的证明、§9–11、参考文献原证明或整个模形式理论。

以下外部modularity、Arakelov分解、index/stack及orthogonality责任均为**cited，原证明未审**。本次不把作者综述的陈述升级为本项目重证。

## 2. 输入与Petersson方向

固定文中quaternion B及其D(B)，Γ′=Γ0(4D(B))。§8将S_(3/2)描述为这个群的weight3/2 cusp forms。它没有在本章另列Nebentypus、Kohnen-plus条件或一个新multiplier定义；须沿文中半整数权自动因子和theta核的匹配，不能把它改成普通weight2/trivial-character函数。

更需保留原文量词：(8.4)/(8.5)额外明确要求f holomorphic。通常holomorphic cusp子空间在fixed level有限维；但不能因此把一切潜在smooth/Maass延拓都当作该有限维子空间，也不能仅由(8.1)擅自给任意smooth automorphic输入授权。该更大域的增长、收敛和输出前提需单独给出。

令τ=u+iv。式(8.1)的准确方向为

\[
 \widehat\theta(f)
 =\langle f,\widehat\theta\rangle_{\rm Pet}
 =\int_{\Gamma'\backslash\mathfrak H}
       f(\tau)\,\overline{\widehat\theta(\tau)}\,
       v^{3/2}\frac{du\,dv}{v^2}
 \ \in\widehat{\mathrm{CH}}^1(\mathcal M).
\]

这里bar确在整个theta值上；不能被PDF文本提取漏掉。因而输入f为第一变量，lift按f线性。u,v是上半平面积分坐标，不是本项目物理r(x)=e^(x/2)f_phys(x)的log-time；它们没有在本章被识别。

目标由§2(2.2)定义为实系数算术Chow的复化。高度配对在实空间上对称双线性，复化后第一变量线性、第二变量反线性。§8的伴随计算先用于实测试类1、hatω及实均值零函数的a(φ)；零性可再按sesquilinearity扩展。不能将其改成无共轭的复双线性Gram。

## 3. 本章实际所得与未所得

在引用Th7.2的前提下，(8.2)/(8.3)给

\[
 \langle\widehat\theta(f),\mathbf1\rangle=0,\qquad
 \langle\widehat\theta(f),\widehat\omega\rangle=0.
\]

Th7.2的实际标量身份是

\[
 2\langle\widehat\theta(\tau),\mathbf1\rangle
       =\mathcal E(\tau,\tfrac12;B),\qquad
 \langle\widehat\theta(\tau),\widehat\omega\rangle
       =\mathcal E'(\tau,\tfrac12;B).
\]

本次只核陈述，不重审Eisenstein展开、正则化或其全局证明。

若f holomorphic，(8.4)再由Th7.4得其与a(C∞_0)正交。因此(8.5)/(8.6)是

\[
 \widehat\theta(f)\in\widetilde{\rm MW}\oplus{\rm Vert}^0,
 \qquad {\rm Vert}^0={\rm Vert}\cap\ker\langle\,\cdot,\widehat\omega\rangle.
\]

C∞_0是相对于双曲体积μ**均值零**的实光滑函数空间，绝非compact-support函数空间。a(φ)=(0,φ)是arithCH类。Vert由特殊纤维分量类生成；tildeMW按Prop7.1是Rhatω、Vert和a(C∞_0)之和的正交补，其generic restriction与MW=Jac(M)(Q)⊗R等距，高度符号为负Néron–Tate。此分解是外部Arakelov陈述，未在本次重证。

所以本章确实定位一个比裸cusp-residue不同的算术输出设施；但它**没有**在§8证明给定f的lift非零、消去Vert^0、每个B的MW非零、所选输入的实际height严格负，或经典ζ Weil配对与此height相等。结尾将MW/Vert各分量的进一步描述留待后文，本门在此停止。

## 4. 归一化与index/stack的未审前件

Th7.4的PDF30陈述实际有系数

\[
 \langle\widehat\theta(\tau),a(\phi_\lambda)\rangle
       =\tfrac12\,\theta(\tau;\phi_\lambda),
\]

其中右边是weight0 Maass函数在M(C)的经典theta lift。§8(8.4)以theta(φ)简记并只用与holomorphic cusp的零配对；这里的零性不依赖这个非零常系数，不能据其简记领取一个新的无1/2的精确norm身份。若运输数值常数，须回到上述实际标量陈述及原变量/实结构。

§2(2.5)引index theorem给高度signature，并在脚注3提示stack情形对称性仍须按其[49]§4核查。当前仅携带这项cited依赖，未追[49]，不把该脚注省掉后宣布新的无条件stack正极化定理。此前图像中的C∞分量、本章holomorphic正交，以及MW负height的外部事实须各按其前提消费。

## 5. 本项目消费门与停止

此处没有r∈S_exp→合法f的实际公式、全noncompact Pan及平移的消去、537同源非根、原du/zero-extension Dlog或强源费用、同一Green全尾、mixed/RR及完整Γ/contact/properpowers/双pole的经典signed身份。故不能把旧Faber/oldform raw坐标代入“arithmetic theta lift”名称就领取这些箭头。

holomorphic子类的analytic分量消失也不排除另有实际smooth/Maass源；同样，fixed level的finite输入不排除所有单边lower、连续family、非线性或D′方法。底层线性map可以通过旧解析商，只要真正新增独立算术结构/费用/符号，不能以“不factor旧商”作为必要条件。

本次来源门只将上述准确类型及依赖保存为可检验设施，未给经典新输入。建议0轮并止§8直接移植；不自动续§9–11、挑B/level、找unknown插值或新建数学合同。下一实际行动由root依据三句准入和宏观前沿决定。
