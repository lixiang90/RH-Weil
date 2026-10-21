# 路线B单一截面候选：独立逆审

2026-10-22。独立核主稿与三独占稿；不改共同STATE、cadence、合同或Git。
本稿是版本绑定的审查意见，不是root消费收据，也不代长期Goal验收。

**结论：修正后PASS，范围仅为本候选的来源澄清、有限商／原高度前端与不晋级的准入判断。**
没有证明一般g系统或经典ζ的独立平方容量、完整Weil正性或成长core结论。

## 1. 版本与实际核查范围

以UTF-8、LF规范化计算四稿SHA-256：

| 文件 | SHA-256（LF） |
|---|---|
| `goals/reviews/2026-10-22-global-sections-local-evaluation-admission.md` | `96692c9821fecf1daea9590a133b52a3f04736e958079514d1019c088f2d8d47` |
| `reviews/2026-10-22/global-section-admission/primary-sheaf-and-restriction.md` | `164f5a74824b8924dd63b0d49b26d8c6fcd7228b8c1d76ca0c0bee4f8050896c` |
| `reviews/2026-10-22/global-section-admission/finite-place-kernel-and-capacity.md` | `f926481b907b357abb9e8db24c09fffaa844d5ac4f16ba181a00c63e61ed958c` |
| `reviews/2026-10-22/global-section-admission/source-map-and-validation-audit.md` | `911a33a3b014a74fe77610ad1fa62fc9320387748e21cb8ac165b1e7313b3383` |

恢复README／STATE／check／show、固定Goal、C035、frontier、D20261020Q及流程；
逐读四稿，定点对照568§5的完整型和567§7的条件预算。
另直接核[v1 HTML](https://arxiv.org/html/2602.15941v1)的§5.1–5.2全文、
§8.1的frame定义和Lem8.3证明、§8.2所需tensor公式；
针对原件稿已报告的问题核§2.2 Prop2.4及其所依赖的Prop2.2分类步骤。
没有重核整篇论文、附录完整Pontryagin对偶或所有历史资产；8.15完整对偶来源依赖仍按原件稿记录。
下列初等等式在明确群模型上独立核算，不依赖把模分类升级为正极化。

## 2. 发现并已落实的一处修正

初稿把标准localization补充式写给一般开集而未单列空集。
若在空集也按“反转所有prime”取值，会得到\(L\otimes\mathbf Q=\mathbf Q\)，
不满足sheaf的空集零对象要求。
现四稿已统一限定该公式用于**非空**Zariski开集，并置\(\widetilde L(\varnothing)=0\)。
原件稿还明确\(H0\)为pointed零对象。此修正不改变任何global群、有限商或高度公式。
按上表最终版本，未发现其他必须修正的问题。

## 3. 来源语义及局部商：PASS范围

§5.2的字面表述确同时要求元素属于\(L\)并限制其分母。
对于\(L=\mathbf Z\)、去掉\(p\)的开集，该字面集合不能承受结构环中\(1/p\)的作用；
故标为“局部化澄清／补充定义”准确，不能倒称论文逐式证明了所补公式。
原件稿没有据这一处表述问题否定rank-one分类，且以缩放到含\(\mathbf Z\)的群修复Prop2.4所需分类，范围适当。

开集restriction是有理元素的包含，kernel为零；闭有限thickening评价才有\(p^kL\)核。
regular位由frame生成性给\(v_p(a_p)=n_p\)：

\[
 \ker(x\mapsto a_px\bmod p^k)
 =\{x\in L:v_p(x)\ge k-n_p\}=p^kL.
\]

最小valuation取到的元素给局部单位，整数倍遍历目标，故满射。
多regular位目标的阶互素，CRT给联合满射及\(NL\)核；不是仅从逐点任意复插值推得。
singular位\(n_p=\infty\)则\(pL=L\)、frame分量零，商为零。
因此\(\mathbf Z[1/p]\)在本p处没有该类有限评价，这与其他谱实现存在并不矛盾。
原ball未被当成加法群，全群满射也未被偷换成ball满射。

## 4. 高度、非零预算和tensor：PASS范围

对\(L=h\mathbf Z\)、\(\lambda=|t|h>0\)，球计数及零纤维计数直接化成整数区间：

\[
 \#B_R=2\lfloor R/\lambda\rfloor+1,\qquad
 \#(B_R\cap NL)=2\lfloor R/(N\lambda)\rfloor+1.
\]

球的有限image大小\(\min\{N,2\lfloor R/\lambda\rfloor+1\}\)也正确。
非零kernel元素存在的条件\(N\lambda\le1\)正反向均由\(hNm\)核算；
是同一非零对象上的有限位消失—原arch高度预算，没有读取零点。
主变化协同运输frame与metric保持\(\lambda\)，未按位更换有利minor。

非循环群的分母无界，Bezout产生趋零非零元素；零seminorm也取消arch约束。
故普通有界点数容量仅在循环底群且metric非零时有限，
但这不是一般正Weil系统必须离散的必要条件。
所有\(n_p=1\)的无限支撑模型保持各有限商非零、ball却无限，确能反测“局部好就全局有限”的错误推断。

rank-r扩展正确标为额外direct sum／评价矩阵输入。
Hadamard用于\(\operatorname{diag}(\lambda_i)A\)的列，给
\(\log|\Delta|\le\sum_j\log R_j-\sum_i\log\lambda_i\)；
同一非零整数\(\Delta\)的整除给相反侧下界。
它没有从rank-one标签自动生成高rank非零minor、Frobenius高阶整除或解析源列高度。

tensor metric相乘且\(\lambda_n=\lambda^n\)；若\(x=\lambda^{-n}\ge1\)，
有\(x\le2\lfloor x\rfloor+1\le3x\)，否则ball只含零。
所以主稿(5)的\(0\le\log\#B_1-\max\{nd,0\}\le\log3\)正确。
这是线性容量，不能直接填入平方RR的\(n^2D^2/2\)项。
主稿(6)与567(14)同方向、同因子；最终版本明确保“每个固定实compact源”，
全复源覆盖／极化没有由这一接口自动取得。

## 5. 源、关系与完整项：PASS范围

四稿保持\(r=e^{u/2}f\)，未把405的B根、完整Q根与物理源混成同一商。
原件未给源到global sections／correspondences的map，
因此主关系与537非根见证的状态正确是“缺输入”，不是通过或已反驳。
原\(du/D_{\log}\)到列高度／局部评价的费用也没有支付。

三个裸map失败均有合法范围：可除全源到固定有限群为零；
固定正metric球内的全加性像为零；自然实metric下连续全加性像因连通性而零。
不连续Hamel像、零seminorm、非群bounded源片，以及families／tensor／非线性／对应／复提升均已保留，
没有以窄失败宣布几何总体不可能。

主稿(7)与568(14)逐项一致：两个pole矩为\(2\Re(M_+\overline{M_-})\)，
contact为\(\psi(1/4)-\log\pi\)，差分项前为\(1/2\)，
所有\(p^k\)项权为\(-2\log p\,p^{-k/2}\Re(r*r^*)(k\log p)\)。
该式只是保留经典目标，并未由当前球容量重新导出。
frame/root对偶不被改称Mellin反射，实metric不被改称完整Γ身份，
\(\log\#(L/p^kL)=k\log p\)不被改称prime-power轨道迹。
同一determinant／容量与这些全位片的身份、误差及协同规范仍open。

连续正反段和函数域真反模型仅用于比较已知前提：
外加同一格／非退化评价对连续两号段均无鉴别力；
真曲线限制核及乘法仍需平方有效性／RR／Hodge才到Weil号。
自由local jets不能代global gluing，数域的ideal标签／全嵌入／判别式等未由Q模型免费取得。
本审查没有新增这些系统的纯性或反纯性定理。

## 6. root可消费的最强结论与停止

可消费的是：该已知候选的有限商、kernel、乘法过滤、原高度预算及确切失效strata；
来源文字修正明确标出，非零minor的高rank扩展另负前件。
这些只是现有valuation／格机制的明确展开和准入信息。
扣旧568非退化carrier／评价、567条件RR，以及542＋555→557最强whole leading4/5后，
没有新的经典平方容量、actual低频／core／coupling／Ξ净后果，也没有长期瓶颈被消除。

因此按一次source-only门收口、0数学轮、无C036／573、cadence保持1的分类是适当的；
这不暂停或完成G20261014，更不允许自动串下一paper／多jet／高频参数。
重准入须有实际写出的非旧\(J_W\)复合map及独立局部order／原高度比较，
或同源算术平方二次容量／完整预算身份，或穿过actual低频和危险core的新signed输入。
这些目前均未给出。此PASS不认证上述open项，不代root的最终前件闭合或远端同步核验。
