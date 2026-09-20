# 401：对偶ind塔与非闭理想层的独立推导

2026-09-20。Lagrange，只读代理01a0bdae-3cd5-7052-92f6-b56121c61445。以下为完整返回报告；代理未改文件或提交。
这是内部独立推导和复核，不是外部同行评审。正文中的双对偶追加命题随后已复核通过，完整追加报告见末节。

**400 §1–6 的主审结论不变。这个新候选有效：对偶 ind 塔的通常层余极限，确实给出可实际下降的非闭理想层 \(J\)。** 它与 400 的通常逆极限不同。以下结论可以直接证明。

首先要修正数据类型：截面对偶后给的是**余截面**。具体为
\[
D_N=\mathcal Hom(\mathcal O,\mathcal O)\simeq\mathcal O,
\qquad D_N\xrightarrow{\times Q_N}D_{N+1},
\]
以及相容映射
\[
e_N:D_N\longrightarrow\mathcal O,\qquad f\longmapsto F_Nf.
\]
因为 \(F_{N+1}Q_N=F_N\)，这些映射相容；正则性保证它们单射。因此该直接系统等价于
\[
F_0\mathcal O\subset F_1\mathcal O\subset\cdots,
\]
其通常模块层余极限就是
\[
J=\sum_{N\ge0}F_N\mathcal O\subset\mathcal O.
\]

这里的“并”首先是**子层的并**。任意开集上，不应未经证明写成
\(J(W)=\bigcup_NF_N\mathcal O(W)\)：截面所需层数可能仅局部有界。不过在实际有理 affinoid \(S\) 上，该等式成立。准紧性使局部层数有共同上界；固定 \(F_N\) 正则，使局部商唯一并可粘合。

**周期下降成立，而且是普通理想层的下降。** 确切地，
\[
\Phi^*J=\sum_{N\ge0}F_{N-1}\mathcal O=J,
\]
因为新增的 \(F_{-1}\mathcal O\) 已包含于 \(F_0\mathcal O\)。这些识别是在结构层内的同一子理想，全部整数 coherence 自动相容。

沿 \(q:X\to S_\Delta\)，可直接定义
\[
\bar J(W)=
\{f\in\mathcal O_{S_\Delta}(W):q^*f\in J(q^{-1}W)\}.
\]
利用覆盖的局部切片，得到
\[
q^*\bar J\simeq J.
\]
这里已进入通常层类别，不再要求在全部周期分支上选择统一的有限层编号。

**茎的判断正确，并且“不有限生成”可以加强为确定结论。**
\[
J_x=
\begin{cases}
F_0\mathcal O_x,&x\text{ 在完整图上},\\
\mathcal O_x,&x\text{ 在图外}.
\end{cases}
\]
前者由所有 \(Q_N\) 在茎中可逆得到；后者因为某个 \(F_N\) 在茎中可逆。

若 \(J\) 在图点附近有限生成，把有限个生成截面在该点附近放入同一个 \(F_N\mathcal O\)，缩小后便有
\(J=F_N\mathcal O\)。但任意这样的邻域都有更深相位点
\[
z\in D_L\setminus D_{L+1},\qquad L\ge N.
\]
在那里 \(F_N\) 非单位，而 \(J_z=\mathcal O_z\)，矛盾。

所以 **\(J\) 在每个图点都不局部有限生成，因而不是可逆理想层，也不是通常有效 Cartier 数据。** 同时，每个茎作为模块都是自由秩一；因此 \(J\) 是通常代数意义的平坦模块层。这恰好说明逐茎自由秩一不能替代局部有限呈现条件。

**闭包关系也成立，但必须在 Banach 截面层面表述。** 对实际有理局部模型 \(S\)，398 给出
\[
\overline{J(S)}
=\overline{\sum_NF_NS}=I_S.
\]
若 \(S\) 与图相交，这个包含严格。证明：每个 \(F_NS\) 都闭，而相位见证保证没有一个 \(F_NS\) 等于 \(J(S)\)。若 \(J(S)\) 闭，它就是 Banach 空间，却是可数个闭真线性子空间 \(F_NS\) 的并，违反 Baire 定理。

因此本例确实保留了区别：
\[
J(S)\subsetneq I_S.
\]
不能把这个范数闭包公式直接移到茎上。

最后，和 400 的准确比较是
\[
\varinjlim_N\mathcal Hom(M_N,\mathcal O)
\longrightarrow
\mathcal Hom(\varprojlim_NM_N,\mathcal O),
\]
在已有识别下就是
\[
J\hookrightarrow\mathcal O.
\]
它在图点不满。这是新的**对偶与无限极限不交换**的具体表现；并不与 400 冲突。

已证明的范围是：普通理想层 \(J\)、其普通周期下降、茎描述、平坦性、图点处不局部有限生成，以及有理截面上的严格非闭性。**原 ind 塔在未层化类别中的完整下降不能由此推出；\(J\) 也不自动忠实恢复全部有限层标记。** Cartier、RR、主关系比较及 \(\tau\) 仍为 O。这个候选值得作为明确的非闭理想层记录，但尚不足以改变完整目标的验收状态。

## 双对偶与400整合版的追加独立逆审

**快审通过，无数学阻断。** 已实际读取 401 §6 和整合后的 400 §7。

[401 §6](../../notes/401-f1-dual-cartier-ideal-and-reflexive-collapse.md) 的识别正确：
\[
\mathcal Hom(J,\mathcal O)
\simeq\varprojlim_N\mathcal Hom(F_N\mathcal O,\mathcal O).
\]
以生成元 \(F_N\) 上的取值识别各项后，过渡确为乘 \(Q_N\)。400 因而给出规范同构
\[
\mathcal O\xrightarrow{\sim}J^\vee,\qquad f\mapsto(j\mapsto fj).
\]
再对偶，evaluation 正好成为 \(J\hookrightarrow\mathcal O\)。所以双对偶为结构层、图点处 evaluation 不满、\(J\) 不反身，以及下降后的对应结论，全部成立。

文中提到的内部 Hom／茎比较也正确：将
\(\operatorname{Hom}(J_x,\mathcal O_x)\) 按生成元 \(F_0\) 识别为 \(\mathcal O_x\)，比较映射明确就是乘 \(F_0\)。

[400 §7](../../notes/400-f1-cartier-tower-limit-and-stalk-defect.md) 保留了正确的 coherence、非本质常值和未层化 Čech 障碍。仅建议两处精确措辞修订：

- **§7.2**：“成为常值 \(O_x\)”改成“成为常值带截面对象 \((O_x,F_0)\)”；源为 \((O_x,1)\)，canonical 箭头为乘 \(F_0\)。
- **§7.3**：“非单位 \(p\) 次根”改成“非平凡的 \(p\) 次单位根 \(\zeta\in\mu_p\setminus\{1\}\)”；这些根本身都是单位。

两处均不改变证明。401 §6 可按现有明确范围结算通过；未写文件、未提交。

主线程已采纳两项措辞修订，未扩大数学结论范围。
