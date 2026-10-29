# Haran 整数副本自余积：独立公理反查

日期：2026-10-29。角色：`/root/haran_fold_countercheck`。这是交给 root 的独立证据原稿；未读取平行证明原稿，未代替 root 消费，也不授权 C064/601。

## 结论与精确对象

在本次实际核对的 Haran 2007 Definition 2.1、2.9 下，令 \(Z_F=F(\mathbb Z)\)，则对每个该类别的目标 \(C\)，

\[
\#\operatorname{Hom}_{F\text{-Rings}}(Z_F,C)\leq 1.
\tag{1}
\]

这里的等同性包括每个有限集对之间的**全部整数矩阵**，不只是 \(1\to1\) 标量。因而 \(Z_F\) 连同两个恒等态射本身就满足 \(Z_F\mathbin{\circledcirc}_F Z_F\) 的泛性质，所问 fold 是同构。未找到有效双映射反模型；下文给出只用已核公理的闭链。

这是该版定义中仿射自余积的局部事实。它没有宣告紧化算术曲面、无穷边界、其它版本的 Haran/F1 几何全部退化，也没有提供物理 Weil 形式的源桥、RR、primitive/principal/mixed 识别或 RH 结论。

## 恢复与来源边界

本任务恢复了 `AGENTS.md`、`goals/README.md`、实际 `goals/STATE.json`；执行过 `python scripts/research_state.py check`、随后 `show`，并读取当前 Goal、停止的 C063、宏观前沿当前摘要与 D20261029AI，以及本门 admission、locator correction。恢复位置为：长期 G20261027 未完成，C063 已停止；第 600 轮已结算，sole cadence 为 2、history 64、formal 20。runtime Goal active 与远端 `61d46e9` 属于 root 已记录观察，本子任务没有另作运行时/远端认证。

唯一数学文献是本地 *Non-additive geometry*, M. J. Shai Haran, Compositio Math. 143 (2007), 618–688，DOI `10.1112/S0010437X06002624`，71 页 PDF：

`literature/local/2026-10-29-haran-section72/haran-non-additive-2007.pdf`。

实际消费范围：

- 印刷页 627–628：Definition 2.1、显式 (2.3)–(2.8)、Definition 2.9。核对文本与这两页 PNG；页 628 下方 ring-category remark 的可见内容不承担额外证明输入。
- 印刷页 632：只消费 Example 1 的 (2.13)–(2.13.4)，确认 \(F(A)\) 是全部 \(A\)-矩阵、分块和 Kronecker 积、普通环映射诱导态射。文本按 `Example 2` 截断；整页 PNG 显示时下方 Example 2 也可见，但没有消费该例或其结论。
- 印刷页 671–675：从 §7.1 开始，至 §7.2 末、§8 标题之前；只作余积/仿射定位与类型核对。没有读取或使用 §8、作者其它论文或参考文献，没有网络检索。

实际余积符号是 \(\circledcirc\)，不是模张量 \(\otimes\)。印刷页 674 Remark 7.1.9 的一般自然映射
\(B^0\otimes_A B^1\to B^0\mathbin{\circledcirc}_A B^1\)
不能一般视为同构；本文只证明上述特殊自余积，沿用 root 对旧 \(\otimes\) 消费的冻结。

## 公理足够迫使任意目标态射自然

若根本不存在 \(J:Z_F\to C\)，(1) 已成立。以下固定一个这样的 \(J\)。用 \(1=[1]\)、\(2=[2]\)，取源整数矩阵

\[
d=\begin{pmatrix}1\\1\end{pmatrix}:1\longrightarrow2,
\qquad s=\begin{pmatrix}1&1\end{pmatrix}:2\longrightarrow1.
\]

对任意有限集对象 \(X\)，通过来自 \(F\) 的指定分配/对称/单位同构识别 \(2\otimes X\simeq X\oplus X\)，定义

\[
\Delta_X=J(d)\otimes1_X:X\longrightarrow X\oplus X,
\qquad
\nabla_X=J(s)\otimes1_X:X\oplus X\longrightarrow X.
\tag{2}
\]

关键检查不是把某个性质从源矩阵泛化，而是利用 Definition 2.1 的**完整**双函子 \(\otimes:C\times C\to C\)。对任意 \(C\)-态射 \(u:X\to Y\)，包括未预先处于 \(J\) 像内者，(2.5.1)、(2.5.5)、(2.6) 及指定对称同构给出

\[
(u\oplus u)\Delta_X=\Delta_Yu,
\qquad
u\nabla_X=\nabla_Y(u\oplus u).
\tag{3}
\]

例如第一式两侧在张量记号下都是 \(J(d)\otimes u\)：
\((1_2\otimes u)(J(d)\otimes1_X)
=(J(d)\otimes1_Y)(1_1\otimes u)\)。
第二式同理，两侧都是 \(J(s)\otimes u\)。这里 \(1_2\otimes u=u\oplus u\) 来自分配律及 \(1_2=1_1\oplus1_1\)；不是额外假设 \(\oplus\) 已为范畴积/余积，也不需要尚未证明的矩阵表示。

## 从该副本建立双积与加法

对 \(u,v\in C(X,Y)\)，定义

\[
u+v=\nabla_Y(u\oplus v)\Delta_X.
\tag{4}
\]

源整数矩阵中行/列的结合、交换、单位恒等式经 \(J\) 保留；再用 (2.4.1) 与 (3)，得到 (4) 为各 Hom 集上的交换幺半群运算，单位是通过 \([0]\) 分解的原零态射。具体而言，三项和的两种括号都化成
\(\nabla_Y^{(3)}(u\oplus v\oplus w)\Delta_X^{(3)}\)；交换由指定交换同构消去；添零由 \(s(1\oplus0)d=1\) 的带类型矩阵恒等式及零态射分解得到。

对任意可复合 \(k,l\)，(3) 直接给出

\[
k(u+v)=ku+kv,
\qquad (u+v)l=ul+vl.
\tag{5}
\]

设 \(n_X=J(-1)\otimes1_X\)。\(J\) 保留源矩阵的 (4)，故
\(1_X+n_X=J(I_X+(-I_X))=0\)。由 (5)，\(n_Yu\) 是 \(u\) 的加法逆元；(2.8.4) 也给出 \(n_Yu=un_X\)。于是 \(C\) 在这套运算下是 preadditive category。这里无需先把所有 \(C\)-态射等同于矩阵。

取 \(X\oplus Y\) 的来自 \(F\) 的包含与投影 \(\iota_X,\iota_Y,\pi_X,\pi_Y\)。它们满足

\[
\pi_i\iota_j=\delta_{ij},
\qquad
\iota_X\pi_X+\iota_Y\pi_Y=1_{X\oplus Y}.
\tag{6}
\]

后一式是普通整数矩阵恒等式，由 \(J\) 保留；(4) 对 \(J\) 像内两矩阵确实就是矩阵加法。式 (5)–(6) 对任意目标态射给出分解式，故 \(X\oplus Y\) 是真正的范畴双积。例如任意 \(w:X\oplus Y\to T\) 都满足
\(w=w\iota_X\pi_X+w\iota_Y\pi_Y\)，而任意两个分量用相同公式唯一拼接。积方向相同。所有有限集对象因而是 \(1\) 的有限双积。

这是“一个整数副本迫使加法”的完整作用域：任意目标 \(C\) 的所有 Hom 集；唯一前提是存在该副本和本版完整公理。

## 第二整数副本必须与第一副本全部相同

再设 \(J':Z_F\to C\)。它固定 \(F\)，故 \(J'(s):1\oplus1\to1\) 在两个规范包含上的限制均为 \(1_1\)。刚证明的双积余积泛性质迫使

\[
J'(s)=J(s).
\]

双积积泛性质同样迫使 \(J'(d)=J(d)\)。因此由 (2)–(4) 可知 \(J'\) 保留的源加法正是 \(J\) 已经在 \(C\) 中建立的同一套加法。\(J'\) 与 \(J\) 固定 \(0,1\)，并都把 \(-1\) 送到 \(1\) 的唯一加法逆元，所以对全部 \(a\in\mathbb Z\) 有 \(J'(a)=J(a)\)。

最后，不把标量结论冒充整个范畴结论。对任意整数矩阵 \(A:X\to Y\)，令坐标包含/投影 \(\iota_x:1\to X\)、\(\pi_y:Y\to1\) 来自 \(F\)。Example 1 的逐项提取和双积分解给出

\[
\pi_yJ'(A)\iota_x=J'(a_{yx})=J(a_{yx})
=\pi_yJ(A)\iota_x,
\]

\[
J'(A)=\sum_{y\in Y,x\in X}\iota_yJ'(a_{yx})\pi_x
=\sum_{y,x}\iota_yJ(a_{yx})\pi_x=J(A).
\tag{7}
\]

空对象由零对象唯一性处理。故 \(J'=J\) 作为整个 \(F\)-环态射，证明 (1)。这没有仅凭 Example 1 的 fully faithful 一句话推出自余积，也没有未付的 size/naturality/交换假设：所有对象与求和均为原有限集对象、有限和，交换同构均来自已固定的 \(F\)。

## 自余积 fold 及不相容余锥的分别结论

由 Definition 2.9，\(F\) 是初始对象。任意 \(C\) 的 \(Z_F\) 余锥就是两个态射 \(Z_F\to C\)，其在 \(F\) 上相容自动成立。由 (1)，有这种态射时两者相同，没有时双方 Hom 集都空。因此

\[
\operatorname{Hom}(Z_F,C)\longrightarrow
\operatorname{Hom}(Z_F,C)\times_{\operatorname{Hom}(F,C)}
\operatorname{Hom}(Z_F,C),\quad J\mapsto(J,J)
\]

对每个 \(C\) 都是双射。于是 \((Z_F,1,1)\) 自身满足所需泛性质，**不依赖一般 Theorem 7.1 的任意输入存在性**。若 \(C_0=Z_F\mathbin{\circledcirc}_F Z_F\) 表示某一模型，两个结构态射 \(i_0,i_1\) 相等，fold \(m:C_0\to Z_F\) 满足 \(mi_0=1\)；由余积唯一性 \(i_0m=1\)，故 \(m\) 为同构。

同时必须保留 Definition 2.1 的忠实性约定。Example 1 的 \(F(\mathbb F_2)\)、\(F(\mathbb F_3)\) 都是非退化合法矩阵 \(F\)-环：部分置换矩阵的零/一仍彼此可区分。假设有共同目标及余锥
\(F(\mathbb F_2)\to C\leftarrow F(\mathbb F_3)\)。复合整数约化映射得到两条 \(Z_F\to C\)，(1) 迫使它们相同，记为 \(J\)。于是

\[
J(2)=0,\qquad J(3)=0,\qquad
1=J(1)=J(3-2)=0.
\]

这与 \(F\to C\) 忠实矛盾，因为 \(F(1,1)\) 的恒等与零态射不同。故这对合法输入在该字面非退化类别中**没有共同余锥**。

可消费的有限结论仅为：若把 §7.1 的存在性读成这一字面类别的“任意两输入”，必须明确允许退化零对象时的忠实性例外，或限定有相容余锥的输入范围。本文没有核定作者在全篇其它位置采用何种补充约定，不把该局部约定问题升级为整篇论文失败。\(Z_F\) 自配对已有恒等余锥，且已直接验证泛性质，所以其 fold 结论不受影响；具体紧化的有理子环图表也可能有 \(F(\mathbb Q)\) 共同目标，不能据此一概排除。

不要不加条件推广为所有普通环 \(A,B\) 的 \(F(A\otimes_{\mathbb Z}B)\) 都是这个字面类别的余积：\(A\otimes B=0\) 时正会遇到上述忠实性约定。

## Root 消费边界与净后果

对象/域：Haran 2007 有完整 \(\otimes\) 双函子的 \(F\)-Rings；仿射整数自配对。域和值域始终为同一类别的全态射；不存在范畴变换或取商代替物理空间。误差：有限代数恒等式，无近似、无数值、无源强度或成长参数。

最强局部净后果：该仿射自配对无法通过两份整数结构的差异产生新的横向整数副本；fold 等价于恒等。这可否定以该**特定仿射差异**为载体的提案前提。它不能证明紧化的边界差异消失，也不能凭“affine collapse”否定所有对应、余维类、cohomology、signed 机制。对边界/其它图表若无 \(Z_F\to C\)，(1) 没有可套用的存在前提。

相对当前强旧结果：未改 whole \(4/5\) negative-inertia UPPER，未填 actual primitive/principal/sections/mixed、dangerous signed core cross、growing \(\Xi\) 的欠账，没有物理 \(du\)/zero-extension \(D_{\log}\) 符号或范数输运。它是 source-first gate 的实际有限检验结果，不是新 RR 或 RH 定理。

本子任务不把文件、反查、标准范畴引理或相同链的 \(\mathbb F_2/\mathbb F_3\) 直接推论单独计轮；整个门如何归档/计轮由 root 结合 admission 与工作流判定。未修改 STATE、cadence、文献库、Git 或 runtime Goal；没有后台进程。下一步由 root 完整读取两份匹配当前任务的原稿，核对前提后作消费/停止决定。

## 资产固定

下列 SHA 均为实际文件字节的 SHA-256；不把当前可变 STATE 的旧摘要当作固定资产。

| 资产 | bytes | SHA-256 |
|---|---:|---|
| `goals/GOAL.20261027.md` | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| `goals/contracts/C063-rank-two-period-positive-cone.md` | 1517 | `e242d79457f2721ac77aa50d9666456e3ea77b6d7597937b4b93f061188271cb` |
| `reviews/2026-10-29/post-600-new-input/haran-fold-first-gate-admission.md` | 1814 | `9d48d6f60269d6ae80f47f45328bd4faf69c1632b429519dc72e95e3769c67c2` |
| `reviews/2026-10-29/post-600-new-input/haran-locator-scope-correction.md` | 2463 | `8f577f3e3ddd606d02c1a6ab99d17026c5875baf772c1d425266fa4d1ceb80e3` |
| 上述 `haran-non-additive-2007.pdf` | 1032382 | `1befc0e1fa8465d29a452d75bbcf02ded93a50b12c179a0b48303570ca60570f` |

文本/PNG 定位均在 `literature/local/2026-10-29-haran-section72/printed-NNN.*`，阅读边界以前述逐页范围为准，文件存在不意味着其全部内容已消费。
