# 406独立来源审计：Boole

2026-09-20。审查者01a0bf01-058e-7ae2-a9b4-6a38a286c729，以下为返回的完整原文。

以下为可整体归档的独立来源报告，已对照405、任务单及406。范围仅为原始文献的命题、适用条件和几何准入界限；源代数构造、Gaussian具体计算与双矩检算仍由主线程及Hubble负责。

**1．普通trace-class Fredholm determinant：条件、指数公式及零点**

主要原始来源是Barry Simon，*Notes on Infinite Determinants of Hilbert Space Operators*，**Advances in Mathematics 24 (1977), 244–273**。[作者官网PDF](https://math.caltech.edu/SimonPapers/74.pdf)。

| 所需命题 | 原文精确位置 |
|---|---|
| Fredholm行列式的定义与收敛 | §3，Definition、Theorem 3.2，印刷p.254／PDF11 |
| 迹类值全纯族的行列式全纯 | Theorem 3.3，p.254／PDF11 |
| 迹范数逼近下的连续性 | Theorem 3.5，p.255／PDF12 |
| 乘法性 \(\det((I+A)(I+B))=\det(I+A)\det(I+B)\) | Theorem 3.8，p.256／PDF13 |
| \(\det(I+A)\ne0\iff I+A\)可逆 | Theorem 3.9，p.256／PDF13 |
| 线性参数族零点的代数重数 | Theorem 3.10，pp.256–257／PDF13–14 |
| 特征值乘积与Lidskii迹公式 | Theorem 4.2、Corollary 4.3，p.258／PDF15 |
| \(\det(e^T)=e^{\operatorname{Tr}T}\) | **Theorem 6.2证明中的明确公式**，p.262／PDF19 |

这些命题的标准对象是复可分Hilbert空间 \(H\)及迹类理想 \(\mathcal S_1(H)\)。若 \(T\in\mathcal S_1(H)\)，则
\[
e^T-I\in\mathcal S_1(H),\qquad
\det_F(e^T):=\det_F\!\bigl(I+(e^T-I)\bigr)
=e^{\operatorname{Tr}T}.
\]
不要求 \(T\)自伴、正规或范数小。这里采用普通Fredholm行列式；其他正则化行列式及无界生成元需要另外的条件。[Simon，p.262](https://math.caltech.edu/SimonPapers/74.pdf#page=19)。

直接推论：固定 \(T\)时，\(z\mapsto\det_F(e^{zT})\)是无零整函数，复平面上的零极除子为零。更一般地，若 \(T(s)\)按**迹范数全纯**，则
\[
\det_F(e^{T(s)})=e^{\operatorname{Tr}T(s)},\qquad
d\log\det_F(e^{T(s)})=d\operatorname{Tr}T(s).
\]
它具有全局全纯对数；对数导数可以非零。仅逐点属于迹类，不能替代参数全纯性假设。

对406的另一族，固定 \(A\in\mathcal S_1(H)\)，
\[
F_A(z)=\det_F(I-zA)
=\prod_j(1-z\lambda_j(A)).
\]
非零特征值按代数重数列出；在 \(z_0=1/\lambda\)处，零点阶数恰为 \(\lambda\)的代数重数。这支持406的真正Fredholm零除子，但不证明辅助参数除子已成为算术除子。[Simon，Theorems 3.10、4.2](https://math.caltech.edu/SimonPapers/74.pdf#page=13)。

还应区分：**行列式零点阶数与普通Fredholm指数不同。** \(I-zA\)即使不可逆，指数仍为零；有限维退化块的核与余核维数相等。一般参数族的零点阶数也不能直接替换为某个纤维的核维数。

**2．Gaussian条带延拓及“一级迹不能由零除子决定”的准确范围**

406的条带
\[
\Sigma=\{w:|\operatorname{Im}w|<\pi/4\}
\]
来自所选Gaussian多项式的具体估计，属于**稿内解析引理**。Simon提供的是完成该引理之后的行列式全纯性接口，而不是这条带本身。

最小待验证输入是：对每个 \(K\Subset\Sigma\)，存在 \(c_K>0,C_K,N\)，使全纯对角项满足
\[
\inf_{w\in K}\operatorname{Re}(e^{2w})>0,\qquad
\sup_{w\in K}|\eta(ne^w)|
\le C_K n^N e^{-c_Kn^2}.
\]
由迹范数中的局部正规收敛得到 \(w\mapsto A_w\)全纯，再用 **Simon Theorem 3.3，p.254**得到
\[
(z,w)\longmapsto\det_F(I-zA_w)
\]
联合全纯。[准确引用](https://math.caltech.edu/SimonPapers/74.pdf#page=11)。一般Schwartz函数不能自动获得这个复延拓；复 \(w\)也不因此成为实际idele。

“一级迹不可由零除子读出”须保留类别限定。对于允许全纯单位倍乘的类别，
\[
\widetilde F(z,w)=e^{zg(w)}F(z,w)
\]
保持零除子及 \(F(0,w)=1\)，但
\[
-\partial_z\log\widetilde F(0,w)
=-\partial_z\log F(0,w)-g(w).
\]
这是406障碍所需的准确表述。

另一方面，若始终限定于规范线性族 \(F_A(z)=\det(I-zA)\)，完整的带重数零点决定上述规范乘积，并由Lidskii公式决定 \(\operatorname{Tr}A\)。**Simon Theorem 3.4，p.254**给出任意 \(\varepsilon>0\)的增长界 \(C_\varepsilon e^{\varepsilon|z|}\)，**Theorems 4.1–4.2，pp.257–258**给出对应的乘积唯一性。非平凡指数倍乘一般离开此规范类别。[原文](https://math.caltech.edu/SimonPapers/74.pdf#page=14)。

**3．普通Cartier除子：商层、全局商与单位消失**

Stacks **Definition 111.49.1(6)–(7)，Tag 02AR**明确规定：
\[
1\longrightarrow\mathcal O_X^\times
\longrightarrow\mathcal K_X^\times
\longrightarrow\mathcal K_X^\times/\mathcal O_X^\times
\longrightarrow1,
\]
其中右端是**商层**，并且
\[
\operatorname{CaDiv}(X)
=\Gamma(X,\mathcal K_X^\times/\mathcal O_X^\times).
\]
[Stacks准确定义](https://stacks.math.columbia.edu/tag/02AR)。

必须区分三个对象：
\[
\operatorname{Prin}(X)
=\operatorname{im}\!\left[
\Gamma(X,\mathcal K_X^\times)\to\operatorname{CaDiv}(X)
\right]
\cong
\frac{\Gamma(X,\mathcal K_X^\times)}
{\Gamma(X,\mathcal O_X^\times)},
\]
而一般
\[
\operatorname{Prin}(X)\ne\operatorname{CaDiv}(X).
\]
全局商只描述主Cartier除子；一般Cartier除子允许局部代表 \(f_i\)，其比值在交叠处为正则单位，却不必来自一个全局亚纯函数。

此外，\(\mathcal K_X\)是将处处非零因子局部化后再层化所得。一般概形不能直接把它替换为单一函数域；具体定义另见 **Definition 31.24.1，Tag 01X1**。[Stacks亚纯函数层](https://stacks.math.columbia.edu/tag/01X1)。

因此普通主除子映射确实满足
\[
\operatorname{div}(fu)=\operatorname{div}(f)
\quad(u\in\mathcal O_X^\times).
\]
406可用的结论是：**若拟议结构层已将指定指数单位识别为局部正则单位，则其非零logdet函数值不能直接作为普通Cartier主除子标签。**

这项识别不能仅由“它在非交换源代数中可逆”推出。商层论证也不授权将整个交叉积代数当作交换scheme的结构环。

**4．相对K理论：何时真正产生非零边界**

Charles Weibel，*The K-book*，作者官网公开稿 **IV.1.11.1，章内p.8／PDF8**：对含幺环同态 \(f:R\to B\)，以同伦纤维定义相对K群，有
\[
K_1(R)\longrightarrow K_1(B)
\xrightarrow{\partial}K_0(f)\longrightarrow K_0(R).
\]
[作者官网第四章](https://www.math.rutgers.edu/~weibel/Kbook/Kbook.IV.pdf#page=8)。

正合性给出精确判据：
\[
\partial\beta\ne0
\iff
\beta\notin\operatorname{im}\bigl(K_1(R)\to K_1(B)\bigr).
\]
因此来自原环实际单位的像，其边界必为零。某个矩阵代表不能在原环中求逆，并不足以证明其 \(K_1\)类没有提升。

这条定义及消失结论允许非交换环。但是，要把 \(K_0(f)\)进一步解释为支撑模、有限长度缺陷或除子群，必须核实相应局部化定理。Weibel **V.6.1，章内p.38**讨论Noetherian环及中心乘法集时，首先得到的是 **G理论**局部化；不能未经验证便把它当作任意非交换代数的K理论模模型。[作者官网第五章](https://www.math.rutgers.edu/~weibel/Kbook/Kbook.V.pdf#page=38)。

最小可靠局部模型是DVR \(R\)，分式域 \(K\)，剩余域 \(k\)：
\[
K_1(R)\to K_1(K)
\xrightarrow{\partial}K_0(k)\cong\mathbb Z,\qquad
\partial[f]=v_R(f).
\]
原文位置为 **V.§6，式(6.6)，章内p.41**；具体边界见 **V.Exercise 5.1，pp.37–38**及 **Example 6.1.2，p.38**。该书采用
\[
\partial[\alpha]=[\operatorname{coker}\alpha]-[\ker\alpha]
\]
的符号；与通常分析指数的“核减余核”须注意符号差异。[DVR／Dedekind局部化原文](https://www.math.rutgers.edu/~weibel/Kbook/Kbook.V.pdf#page=41)。

对 \(L=R^n\subset K^n\)、\(g\in GL_n(K)\)，其格解释为
\[
v_R(\det g)=
\ell_R\!\left(L/(L\cap gL)\right)
-\ell_R\!\left(gL/(L\cap gL)\right).
\]
所以ambient可逆的算子可以相对指定格产生非零指数；若 \(g\in GL_n(R)\)，则它保持格且指数为零。移动格仍不是非零指数的充分条件，两项长度可能抵消。

**5．行列式线：线、截面、退化与除子须分别提供**

Stacks **§15.124开头及Lemma 15.124.4，Tag 0FJI**，对两项有限投射复形
\[
C=[E^{-1}\xrightarrow d E^0]
\]
构造
\[
\det C=\det E^0\otimes(\det E^{-1})^{-1}.
\]
两项等秩时有典范截面 \(\delta(C)=\det d\)，它是处处可逆的平凡化当且仅当 \(C\)无上同调。[局部行列式构造](https://stacks.math.columbia.edu/tag/0FJI)。

概形上的粘合与典范截面见 **Lemma 36.39.1，Tag 0FJW**。[全局构造](https://stacks.math.columbia.edu/tag/0FJW)。

得到**非零有效Cartier除子**的最小附加条件是：

- \(\delta(C)\)局部为非零因子，即是正则截面；
- 它在某处不是单位，即零集非空。

仅有行列式线，或仅知道某个映射不可逆，均不足够。对应的精确准入是 **Definition 31.15.6、Lemma 31.15.10，Tag 0C4S**。[正则截面与有效Cartier除子的对应](https://stacks.math.columbia.edu/tag/0C4S)。

真正的无限维相对位置模型可引用Segal–Wilson，*Loop groups and equations of KdV type*，**Publ. Math. IHÉS 61 (1985), 5–65**：

- **§2，pp.10–11／PDF7–8**：先指定极化 \(H=H_+\oplus H_-\)，要求 \(W\to H_+\)为Fredholm、\(W\to H_-\)为紧算子；投影指数记录相对位置。
- **§3，pp.17–20／PDF14–17**：在指数零分支构造行列式线。
- **p.20，Proposition 3.3及此前段落**：典范行列式截面在投影失去可逆性、即 \(W\)不与 \(H_-\)横截时消失，并给出相应Fredholm行列式表达式。[原论文](https://www.numdam.org/item/PMIHES_1985__61__5_0.pdf#page=17)。

这里产生零点的是指定投影的退化；ambient变换本身仍可逆。对RH-Weil采用此机制，需要另行交付极化或格、允许的变换群、行列式线及其截面和粘合数据。

**6．Arakelov／Green数据：普通单位障碍不能覆盖的范围**

Henri Gillet–Christophe Soulé，*Arithmetic intersection theory*，**Publ. Math. IHÉS 72 (1990), 93–174**，原始论文：

| 内容 | 精确位置 |
|---|---|
| 算术循环对及Green条件 | §3.3.3，pp.126–127／PDF35–36 |
| 主算术循环及算术Chow商 | §3.3.3、Definition 3.3.4，p.127／PDF36 |
| 整数环单位的无穷位对数映射 | §3.4.3，p.131／PDF40 |

[原始PDF](https://numdam.org/item/PMIHES_1990__72__93_0.pdf)。

在余维一，主算术除子为
\[
\widehat{\operatorname{div}}(f)
=\bigl(\operatorname{div}(f),-\log|f|^2\bigr).
\]
若 \(u\)是底层正则单位，则有限部分为零，但
\[
\widehat{\operatorname{div}}(u)
=(0,-\log|u|^2)
\]
仍可能是非零算术除子对；它在模主算术关系的 \(\widehat{\mathrm{CH}}^1\)中为零。[定义所在p.127](https://numdam.org/item/PMIHES_1990__72__93_0.pdf#page=36)。数域整数环情形的单位对数映射在p.131直接呈现。[具体位置](https://numdam.org/item/PMIHES_1990__72__93_0.pdf#page=40)。

因此406应保留：

> 单位消失障碍仅适用于普通Cartier标签，或明确要求消去的单位子群 \(U\)。它不排除G1允许的带Green数据等替代除子理论；这些理论可能保留底层正则单位的非零无穷位分量。

采用该替代路线仍需实际的算术循环对、Green条件与主算术关系；来源没有把任意光滑logdet自动认证为主算术除子。

**7．对405之后工作的最小准入结论**

下一步可以据此选择并明确交付：

| 路线 | 必须明确的最小数据 |
|---|---|
| 普通Cartier | 交换局部结构层、亚纯对象、商层粘合，以及指定正则单位确实被消去 |
| 相对K理论 | 实际环／范畴映射、可用的局部化模型，以及非零类不来自原端 \(K_1\) 的证据 |
| 行列式线／局部格 | 格或极化、有限缺陷、线及截面；产生除子时还需正则性与实际零点 |
| Arakelov等替代理论 | 有限部分与arch／Green数据、单位作用及主关系的完整定义 |

之后仍须证明同一对象与405的双矩、完整Weil配对及算术对应兼容。当前文献支持指数族、真正Fredholm零除子及上述准入机制，尚未认证 \(P_{\mathrm{an}}\)为几何主除子像。

本次报告未写入、修改或归档文件，未启动Lean，未使用git。
