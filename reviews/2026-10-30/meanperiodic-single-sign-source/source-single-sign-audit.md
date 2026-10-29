# FRS §4.3：single-sign 原文的独立限定来源核查

2026-10-30；独立任务 `/root/frs_single_sign_source`。同 G20261027/runtime1793085111，原冻结0c4f。只写本文件，不改共同STATE、cadence、Goal、文献或Git，不登记C066/603，不计数学轮。原文为固定 arXiv:0803.2821v2；下述读取及有限纠正不等于整篇或其经典ζ应用已经复核。

## 1. 来源裁决

**所核原文给出一个条件式 Mellin–Carleman 极点定位准则，没有在本范围内给出经典ζ的独立 single-sign 证明。** Proposition4.10明确把 eventual constant sign 列为前提；同时还假设变换在一个右侧实区间无极点。结论是该变换的全部极点位于条带，δ=0时位于临界线。它不直接声称ζ的全部零点已经在临界线上。

这一单侧sign准则可能是有用的实际解析入口，不能仅因它没有先构造几何principal/sections便说无用。若一个明确经典ζ输入的全部非平凡零点都能无抵消地进入此变换的极点，且 eventual sign 与必要实极点排除被独立证明，确实可能影响Goal核心门。但指定页没有支付这些具体前件。当前应按限定来源门停止，不把新符号或一般条件定理当已构造的经典正性输入，也不自动顺读后章或引用链。

## 2. 实际阅读、视觉核对与曝光范围

恢复时读AGENTS、README/STATE，执行research_state.py check后show；读Goal、耗尽C065、AQ、formal21及当前frontier。STATE的唯一新动作是这一FRS章门，非C065续算。运行Goal与旧发布观察沿parent现场，不冒称本子任务另做远端API。

固定PDF共45页，651244bytes，SHA256为89d9e01f290a9f8018240ec79c526d9ab1eb3db0e3abf47a1d6d06ae9f009c0f。未新下载副本，未调用web。实际文本/Poppler图像分别核PDF19、20、23、24及必要PDF15，公式与版面可读。

消费范围如下：

- PDF19：§4.1 Definition4.1、增长条件(4.1)–(4.3)、Laurent主部(4.4)、逆Mellin定义(4.5)及自变量角色。页首§3尾为曝光，不以其替代完整前章审查。
- PDF20：必要h12/h21定义(4.6)/(4.7)、互反关系(4.8)及作为输入的Z1/Z2函数方程(4.9)；Theorem4.2的statement可作背景，未审其后续整段proof。图/提取返回的Remark4.3–4.5及proof开头如实记为曝光，不将其当完整mean-periodicity证明。
- PDF23：§4.3 Proposition4.10全部statement。依parent随后明确的范围补充，同页Remark4.9作为“极点与零除子不可混同”的限定负对照消费；Theorem4.7 proof及Remark4.8为同页曝光，不据此宣称已审其完整前提或定理。
- PDF24：§4.3的proof段、Lemma4.11 statement，直到§5标题之前。整页图确实曝光下半§5.1及其两个ζ式，但这些后章内容不消费、不用于本裁决。未读Remark5.11、Proposition6.1/6.9或对应proof。
- PDF15：parent为核PDF24可疑函数方程而明确准入的必要Proposition2.16 statement及图像；其proof由作者省略。定位只在PDF7–18搜索“2.16”所在行，返回PDF15及PDF17的引用行；未消费对应全章。PDF15整页图/提取另曝光Proposition2.15/2.17及§3.1开头，除必要2.16外不把这些扩成新定理消费。

没有阅读[43]的原始Laplace定理、其他引用、§5/6应用、作者后续版本或整个§2/§3证明。没有数值实验。临时渲染在独占tmp/pdfs/frs-single-sign-source-audit目录，不改原PDF。

## 3. 实际对象：Z、f与h，不是原physical源r

Definition4.1先给一类已在全平面亚纯的Z(s)=γ(s)D(s)，并要求全部Z极点落于某有限竖直条带、γ在竖直带快速下降、D在右侧有多项式增长及在指定高度序列上有带内增长控制。这里是作者定理的输入；不能把“Z本来亚纯”默读成本文刚刚独立证明了未知ζ解析性质。

其逆Mellin函数为

    f_Z(x)=(1/(2πi))∫_(Re s=c) Z(s)x^(-s) ds，c>1/2+w。

必要边界函数为

    h12(x)=f_Z1(x)−ε x^(-1)f_Z2(x^(-1))，
    h21(x)=f_Z2(x)−ε^(-1)x^(-1)f_Z1(x^(-1))。

一般是两个h的互反关系h12(x^(-1))=−ε x h21(x)，不能无条件改成一个实值自对偶h。Theorem4.2另把Z1(s)=εZ2(1−s)作为所列结论的前提。其同页statement给指数多项式的compact-uniform逼近及C∞poly归属；没有理由只凭该statement就宣称任意h已具有某个非零卷积湮灭子。

在Proposition4.10中，作者进一步直接假设一个real-valued mean-periodic h，并假设它满足单函数互反关系。native对象是正实轴上的多项式增长函数或强Schwartz对偶中的mean-periodic对象；MC是Mellin–Carleman变换，不应无声改成整个Mellin变换、原完整Weil分布或ξ'/ξ。

变量t在H(t)=h(e^(-t))中是对数尺度；它不是旧136里F_n(δ_n+it)的边界频高变量。h也不是本项目任意compact physical r∈L²(I,du)。本节没有给r→算术除子的实际映射、原du/Dlog连续费、全405关系消去、537非根coverage、整数截面乘法或mixed配对。这里未付这些角色不证明它们不可能；只是不能把合法h或解析annihilator重新命名为几何principal后自动消费。

特别地，(4.4)的“principal part”是Z在复极点的Laurent主部系数，不能仅凭这个名称认成整几何principal divisor。

## 4. Proposition4.10的准确逻辑与量词

其三个假设是：

1. h为real-valued、属于所列native函数空间中的mean-periodic对象，并满足h(x^(-1))=−ε xh(x)。
2. 存在t0>0，使H(t)=h(e^(-t))在全部t>t0保持同号。它可以是最终非负或最终非正的条件，不是对所有卷积平方成立的positive-type条件。
3. 存在0≤δ<w，使MC(h)(s)在**实数区间**(1/2+δ,+∞)没有极点。这里不是先假整个复右半平面无极点。

结论才是MC(h)的**全部复极点**满足|Re s−1/2|≤δ；δ=0给临界线上极点。

作者的proof把右半平面MC(h)识别成

    ∫₀¹ h(x)x^s dx/x = ∫₀^∞ h(e^(-t))e^(-st)dt，

再引Lemma4.11的Landau型事实：实函数最终同号且Laplace收敛横坐标σ_c有限，则在该实点σ_c有奇性。原文特意说收敛横坐标，而非绝对收敛横坐标。该Lemma的外部原proof未在本任务复核；只按作者本节引用的条件定理消费，未把它算作新的解析估计。

逻辑上，此事实把右侧可能的复极点通过收敛边界迫向一个右侧实奇点；排除那个实区间的极点后，右侧极点被排除，再用正确互反函数方程反射到左侧。若Laplace变换处处收敛而无有限σ_c，极点为空是平凡分支，不能据此构造一个非零实际primitive。

因此single-sign是关键的**未证明前件**，不是这里的输出；无右侧实极点亦不能忽略。尤其δ=0时，任何尚未移除的实极点s>1/2都会阻止直接应用本结论。选定经典Z时必须逐一处理实极点、其去除操作及其对h符号的影响，不能只看非平凡零点。

## 5. PDF24原印函数方程与有限纠正范围

我独立对照文本和页面图，PDF24的proof原行确实印成

    MC(h)(s)=ε MC(h)(s)。

这是同一自变量s的重复，不是文本提取遗漏。不能把这行当成对称极点条带的充分证明，也不能静默把它改写后称为原印公式。

必要Proposition2.16实际在PDF15。其statement为：若f1(x^(-1))=η f2(x)，则相应变换满足MC(f1)(−s)=−η MC(f2)(s)，另有两函数mean-periodic及右半平面半Mellin存在等前提。

针对4.10的互反关系，可作一个独立的有限移位核对：令g(x)=x^(1/2)h(x)，则g(x^(-1))=−εg(x)。以乘法character的标准可逆作用保持native mean-periodicity，并在共同收敛半平面用半Mellin定义得MC(g)(s)=MC(h)(s+1/2)，再按亚纯唯一性延拓。2.16给出

    MC(h)(1/2−s)=ε MC(h)(1/2+s)，
    即 MC(h)(s)=ε MC(h)(1−s)。

这是“原2.16＋独立character移位”的有限重闭，支持4.10所需的左右极点反射；它不是PDF24原行本身。它也不支付经典ζ的single-sign、实际MC与ζ零点的完整识别或任何新的算术正号。对省略的2.16 proof及全部native空间理论没有扩大审查。

## 6. 极点、零点与same-source识别

选定范围内没有实际给出一个经典ζ专属的G(s)/h，证明其single-sign并把全部ζ非平凡零点完整、无抵消地送到MC(h)的极点。不能因作者使用ζ类函数便直接作这种识别。若未来使用某个分子/分母比值，至少还须核：Z的分子零点是否抵消目标分母零点、MC保留了哪些主部和重数、哪些实极点须先移除，以及这些步骤如何改变h。

同页Remark4.9正好是一个可消费的typing负对照：作者给含Selberg整个二阶函数的Z_Γ，但其boundary h_Γ仅为c0+c1 x^(-1)，MC(h_Γ)为仅在0/1处有可能极点的有理函数。因而mean-periodicity不自动识别整个Z的全零除子；MC的极点信息可只见边界主部，而漏掉一个很大的entire零点结构。该例用于防止消费方向错误，不用于否定其它实际Z、全部FRS或所有mean-periodic方法。

## 7. 与旧证书和长期Goal的关系

本任务另实读旧136 §3。那里需要一列holomorphic arithmetic F_n的全频Cauchy加权负部J_n=∫[-ReF_n(δ_n+it)]_+/(1+t²)dt趋0，并另付Poisson admissibility及非空Euler开集的正确germ。这与FRS的单个h(e^(-t))在t→+∞同号不是同一对象、变量或量词；没有现成等价可以把其中一个假设免费替换为另一个。

同样不能只凭“Meyer谱商”或598的固定Mellin样本规则，宣布本节涵盖的全部mean-periodic模块失败。当前可得的准确净判断是：这一指定章节没有付清经典ζ的独立sign或同对象零除子识别；它给一个有真实内容但仍带关键假设的极点约束接口。source0停止不等于完成或否定长期研究。

若以后实际给出不同的独立single-sign证明并完整控制目标零点/实极点，这条路线可重新比较核心净后果；在此之前不自动顺读§5/§6应用、追引用、造新数学合同或把缺失sign换名为新输入。主principal/mixed、signed core/cross、自然成长Ξ与whole4/5负惯性UPPER未因本次阅读改变，三个Goal门保持open。计轮、STATE、库记录、root结算与GitHub发布都由parent按当前证据办理。

## 8. 执行及版本

本任务仅写本独占MD；渲染页为read-only来源核对的临时文件，没有后台进程。未改原PDF、共同状态、文献或Git。原文公式错误的修复是有限解释，不把本文或hash当作者全部定理的认证。下列原字节在定稿时实际核对；自身不作自引用hash。

| 文件 | bytes | raw SHA256 |
|---|---:|---|
| literature/local/2026-10-30-frs-mean-periodicity/fesenko-ricotta-suzuki-0803.2821v2.pdf | 651244 | 89d9e01f290a9f8018240ec79c526d9ab1eb3db0e3abf47a1d6d06ae9f009c0f |
| goals/GOAL.20261027.md | 9679 | b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de |
| goals/contracts/C065-whole-window-onebody-return-budget.md | 2164 | f61a822da11878e951c4307328862f162ff04f26e3150d241b389fc562e46f3e |
| goals/reviews/2026-10-29-general-rh-macro-review-cycle-21.md | 7467 | b5ba1da36d2961223911220ce4dc2e21efe07676a172018ebaf3890ba0571382 |
| notes/136-cauchy-weighted-passive-defect.md | 10260 | 334b1846ec7a0d83f7c203bdf3261d4a35ac9385b5d1f62aee601ec8eb5d5e97 |
| reviews/2026-10-30/meanperiodic-single-sign-source/execution-start.json | 2355 | 8028da9516e90b653e14daa082051682ec2f9b36fdb19c6cda5ec83b79dea969 |

本文终稿，提交parent消费；文件存在不等于root已审结、已计轮或已发布。
