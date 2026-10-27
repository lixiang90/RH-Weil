# EX 准入：已付 trial family、共同定义域与严格 degree 余量

2026-10-28；unit_height 独占支持稿。恢复 STATE/D20261028I、G20261027、前沿及唯一 [EX强旧准入](../gamma-signed-location/next-trial-common-subtraction-admission.md)，check/show通过。本稿只查585既有证明及root消费的准确参数范围，不重证Perron/H₀、不优化c/δ、不改原稿，不外网/下载/数值，不改STATE/cadence/Git。cadence3／历史49／cycle16原字节保持；不预C049/586。

## 1. 判定

**原已付结果给一个开放的充分参数 family，不是唯一已冻数值算法。** 固定同一实际 \(H_0\)、同一source频率邻域 \(\delta>0\) 和原 unweighted多项式比较常数 \(C_1>0\) 后，weighted稿§4已明确要求

\[
 n_X(c)=\left\lfloor c\frac{A_X}{\ell_X}\right\rfloor,
 \qquad A_X=\frac{\sqrt X}{\ell_X},\quad\ell_X=\log X,
 \qquad C_1c<\frac{\Delta_\delta}{2},
\]
\[
 \Delta_\delta=4-\frac4{\sqrt{1+4\delta^2}}>0. \tag{1}
\]

对**任何先固定且满足原充分条件**的c，原证明同段适用，起点/误差常数可依该选择；不声明在所有c上统一。特别，任一已选合法c都不是这段已付充分范围的右端点。因此可在**不换H₀、不换δ、不改变原费用引理**的情况下，取一个固定比较常数

\[
 c<c_+<\frac{\Delta_\delta}{2C_1}. \tag{2}
\]

\(n_X(c_+)\) 对应的更大空间仍是原来已付款的同family实例。这里c₊只用于核原E_X的strongest-old余量；不是把选定E_X换成新repair、做参数优化或扩原证明。若后续残余迹结论只用此已付更大空间及有限正交HS求和，它是标准旧组织，0数学轮，不应再建合同。

本判定**不**说任意c、边界值、任意成长degree、\(\delta_X\) 或 \(H_{0,X}\) 已经付费；也不把它提升为新净signed／whole／corecross结果。

## 2. 本次消费的原版本与位置

以下是既有root-consumed输入，本次不重新认证原外部论文：

- [585](../../../notes/585-cofinal-sonin-fixed-source-trace-lower-and-core-error-fee.md) §2–3：共同H₀、ALLpoly原域及 \(n\asymp\sqrt X/(\log X)^2\) 的严格权gap选择；§4有限正交基求和。
- [weighted-polynomial-trial-lower](../fixed-test-lower/weighted-polynomial-trial-lower.md) §1(H)、§3(P)/(U)、**§4明确的 \(C_1c_\delta<\Delta_\delta/2\)**、全Tail及(C)，§5维数/trace原域。
- [common-H₀终稿](../fixed-test-lower/common-sonin-vector-and-polynomial-domain.md) §1、§5–7：严格compact bump修正后的共同gap、ALLderivative/ALLpoly域及norm。
- [585 root前件记录](../fixed-test-lower/root-consumption-scope.json)：已消费H₀版本dcdf8e91…、weighted版本12063904…；保same-range、同物理范数、全部inverse/returns及fixedsource量词。root最后消费的严格support版本，而非最初9bbec3…草稿，是本次依据。

本次原证明的Perron、Gevrey存在、Γ规范和trace-class前件只按这些记录消费；没有新取原文、续upper/6.4/6.5或另读proof链。

## 3. H₀实际对象、共同gap和 ALLpoly 域

原空间是 \(\mathcal H=L^2(\mathbb R,dt/(2\pi))\)，与原物理log \(L^2(dy)\) 酉等同。原 \(S_0\) 为gap1实际 archimedean Sonin投影。已付的是**先固定一个**raw Mellin向量

\[
 H_0\in S_0\mathcal H,\quad H_0(0)>0,\quad
 |H_0(t)|\le C_0e^{-c_0\sqrt{|t|}},\quad
 t^jH_0\in S_0\mathcal H\quad(j\ge0). \tag{H}
\]

构造中先fixed larger gap \(a>1\)、fixed平滑宽度 \(\varepsilon<\log a\)，原Gevrey bump严格support在 \(|v|<\varepsilon/2\)，故所有导数向量有同一gap至少 \(b=ae^{-\varepsilon}>1\)。这里的平滑宽度ε与下文source的δ不是一个参数。

ALLj由同一actual dilation-Bochner卷积的 \(\psi^{(j)}\) 给出，已付

\[
 \|t^jH_0\|_{\mathcal H}\le A_0B_0^j(j!)^2\|g\|,
\quad
 \int_{\mathbb R}|t|^{2j}|H_0(t)|^2dt
 \le\frac{4C_0^2\Gamma(4j+2)}{(2c_0)^{4j+2}}.
\]

因此所有**有限**complex polynomial倍在同一 \(S_0\mathcal H\) 中；常数先fixed，不随X、degree、多项式或测试源变化。费用随j增长，不能称uniform-in-j的小费。raw未平滑kernel的 \(O(1/t)\) 不在root消费；旧√log评价界已足，不在这里重开该更强渐近。

每个finiteX的

\[
 D_X(t)=\prod_{p\le X}(1-p^{-1/2-it})
\]

及逆在实轴有界；原range身份为 \(\operatorname{Ran}\Pi_X=D_X S_0\mathcal H\)。故对每个有限整数N，

\[
 \mathcal V_X[N]=\{D_XpH_0:\deg p<N\}
 \subset\operatorname{Ran}\Pi_X,
 \qquad\dim\mathcal V_X[N]=N. \tag{3}
\]

(3)的**合法域/维数**对任意finiteN已付，因D_X无实零且H₀在J_X非零。它不等于相同N范围的quantitative concentration已经付清。后一个结论必须使用(1)的原degree费用。

## 4. 全部多项式使用的是同一实际加权范数

固定X时，trial原norm是

\[
 \|D_XpH_0\|_{\mathcal H}^2
 =\frac1{2\pi}\int_{\mathbb R}w_X(t)|p(t)H_0(t)|^2dt,
 \qquad w_X=|D_X|^2.
\]

不是将D_X当等距，不是completed Gamma norm，也不是只在J_X局部正规化。所有degree的trial都放在这一个空间；物理正交投影与基必须按这个norm构造。finite monomial Gram矩阵由同一积分给出，moments有限且正定，没有未经付款的无限Gram逆。

原weighted§3的(P)/(U)同时对**ALL realt、ALL complex p、ALL finite degree<N**成立，常数 \(C_1\) 可在固定H₀后选定，并不依赖X、N、p、c或sourceδ：

\[
 I_p=\int_{J_X}|pH_0|^2,
 \quad J_X=[\pi/\ell_X-\ell_X^{-2},\pi/\ell_X+\ell_X^{-2}],
\]
\[
 \int|pH_0|^2
 \le e^{C_1N\log(N+\ell_X)}I_p. \tag{4}
\]

H₀在J_X的fixed lower、Gevrey moments和 \(\ell_X^{4N}\) 已包含在C₁账本中。扩大N时不允许重新选择一个依p或N的H₀、重写C₁或换局部norm；(4)的原量词使这种操作根本没有必要。

## 5. 严格开放范围逐项核账

先fixed非零compact complex源r，再选一个fixedδ>0，使
\(|\widehat r(t)|\ge b_r|t|^{k_r}\) 于 \(|t|\le\delta\)。这是source下界邻域，不是取X→∞时再缩的δ_X。原权比较在同一δ上给：J_X exponent \(4-o(1)\)、δ外至X² exponent \(4-\Delta_\delta+o(1)\)、小中心 exponent o(1)。

将 \(N=n_X(c)\) 代(4)，所有充分大X有 \(\log(N+\ell_X)\le\ell_X\)，entropy成本至多 \(e^{C_1cA_X}\)。原稿选择“成本小于固定权gap的一半”的**严格**条件就是(1)。因此

\[
 m(c):=\Delta_\delta/2-C_1c>0. \tag{5}
\]

这个m(c)是已声明充分条件的余量，不是最佳degree常数。对于(2)中的固定c₊，同理有 \(m(c_+)>0\)，而且原其他环节仍在原范围：

| 原环节 | 对同H₀/δ的固定c₊为何仍已付 |
|---|---|
| \(\log(N+\ell_X)\le\ell_X\) | \(N=O(\sqrt X/\ell_X^2)\)，每个fixed finitec₊都满足；起点可依c₊ |
| δ外坏区 | exponent费用 \(C_1c_+<\Delta_\delta/2\)，原strictgap仍正；无需新的prime-sum或频高定理 |
| 小中心坏区 | 同一 \(C_1c_+<\Delta_\delta/2<2\)，原中心与J_X的4阶gap仍有严格余量 |
| \(|t|>X^2\) 完整尾 | 原要求只有 \(N=O(\sqrt X/\ell_X^2)\) 且常数fixed；已付Gevrey tail吸收照用，未将compact-frequency权界外推 |
| ALLpoly concentration | 原证明先给整个degree空间的统一坏区费；没有对p单独选c，故更大V中ALL向量仍按同原估计消费 |
| 实际域与finiteHS求和 | (H)/(3)的ALLpoly域与原finiteX正迹已付，不因degree的另一固定合法选择而变域 |

据此，原weighted(C)对 \(V_X(c_+)\) 同样成立：所有v在
\(\pi/(2\ell_X)\le|t|\le\delta\) 上有 \(1-o(1)\) 质量，误差不依v；同一个sourceF在这段的模下界也不变。这里没有重证原估计，只核它们的已付款量词和c的出现位置。

若首测使用两份fixed源，必须先有一个共同fixedδ使二者各自的有限零阶模下界成立。有限两源可沿原解析非零前件取共同邻域，但一经本门冻结，不能在选c₊后改δ或各用一套E。没有把“所有先fixedr分别可选δ”升级成“全source都有一个共同δ和共同常数”。

## 6. c₊的用途与不得扩大的范围

对一个已选合法c，(2)保证同family的嵌套

\[
 V_X(c)\subset V_X(c_+)\subset\operatorname{Ran}\Pi_X,
\]
\[
 n_X(c_+)-n_X(c)
 =(c_+-c)\frac{A_X}{\ell_X}+O(1)\to\infty. \tag{6}
\]

所以当要检查原 \(E_X(c)\) 的剩余迹时，不能只读585最终打印的单个lower常数：同一旧family已经提供一个更大、维差仍为 \(\sqrt X/(\log X)^2\) 阶的actual comparison空间。该大空间不是用来替换原E或宣布新repair，而是strongest-old核账的现成比较物；其正交补仍须按同一物理weightednorm使用。此后的有限正交HS后果由root/另一独占稿核，不能把它们再称一轮新residual数学。

准确边界是：

- 原资料**没有**指定数值a/ψ/H₀/C₁/c/δ及实现它们的唯一算法；给的是固定合法对象/常数的存在与充分范围。固定一次选择后其空间/投影当然确定，但不因此成为“该证明只付一个不可比较的数值E”。
- 有权选择c₊来自原**严格**不等式，不来自笼统“c很小”。若没有一个c满足原strict条件的见证，就不能随意捏造c₊；本次是原§4已经把所需不等式明确写出。
- 不声称右端 \(\Delta_\delta/(2C_1)\) 已可取、不声称optimal c、所有大c或更快N成长均已付；也不声称一套误差在全开放参数域上uniform。
- (3)的任意finiteN域合法性不授予该N的集中/trace lower；δ_X→0、c_X逼边、另一个H₀或新的weightednorm均不在本次消费范围。
- 对fixedsource得到的后果不变成ALL changing-source/corecoupling或whole正性；537控制源的净Q早已正，不能用其二维复验制造新净后果。

## 7. 强旧分类与交还

本稿所核的核心事实是：**同一actualH₀／fixedδ／原norm下，已消费的degree充分域具有严格可用余量，故大于当前c的同family comparison空间已经付费。** 这来自585及weighted原稿ALLpoly/strictgap量词的直接消费，不是新Perron、Gevrey、最佳degree或独立signed输入。

因此，若EX共同扣项的拟议结论仅由 \(V_X(c_+)\ominus V_X(c)\) 的有限正交组织及原HS正项求和得到，分类应为 **strongest-old／标准推论0**，不是重新准C049/586。不能以“原稿没打印这份residual公式”回避已付大空间。

本稿不单独宣布全部residual估计或所有修复失败；要排的是当前原参数family下一个具体free/O(1)共同扣项主张。更大收费投影、不同非局部/source-adapted/Γ-relative修复及独立primitive/signed输入仍按实物重新准入。whole4/5UPPER、完整核心cross/primitiveRR/Ξ未变，长期Goal门保持open。

无pending process。独占支持稿待fresh/root消费，不改原证明、管理文件或轮次。
