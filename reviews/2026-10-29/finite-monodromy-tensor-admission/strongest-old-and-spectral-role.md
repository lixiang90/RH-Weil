# 固定 C₂ 算术 tensor：最强旧与全局谱角色

2026-10-29；`/root/moment_fresh_audit` 当前全新0预算比较。已恢复当前状态/check→show、Goal/前沿及A/formal18；只读附件§6.1–6.2、001/002/073，不建C054或计轮，不改STATE。局部 Euler、Γ/pole 和bad7由另两腿核。

**判定：当前全 n 算术实例和整个固定 C₂ 普通表示操作的后果属于强旧直接0；它不实现附件所需放大的全局零点谱责任。** 当前具体 K 确实是实际非平凡算术对象，但这份 tensor tower 的全局 L 函数只重复两个既有因子及其零点重数。073已经明确区分 local Satake tensor 与 global zero-space tensor；002的单位局部参数1／ζ例子是更便宜的全局角色检查。

## 1. 附件的实际要求，不能换掉谱对象

原附件§6.1(1)字面要求“局部 Frobenius 特征值是原特征值的 k 次对称或张量组合”；同节另要求所有偶 k 的一致弱界、适当对偶，以及据此对同一个 α 作 k→∞ 的纯度提取。§6.2明确普通乘积可能坍缩/改变 Euler 因子；需要非平凡族、全局迹/Künneth和一致控制，不能把需要的极点界定义进对象。

所以附件没有直接写一个“ζ零点ρ取ρ^k”的形式公理。本题要检验的全局消费是：普通有限 Galois 操作是否另有严格 global realization/trace，把局部 tensor 谱与**目标全局零点谱**的幂或组合联系起来。只核局部 α^k 而不核该桥，不能推出经典 RH 或 Deligne式放大。

001定理C/D的幂迹界与determinant识别作用于同一组 reciprocal roots；073也先要求真正 global Frobenius modules。不能把 local Galois fiber 的 eigenvalues 当作 number-field L 函数的全局非平凡零点。

## 2. 当前实际 tower 的全 n 直接计算

固定 `K=Q(√−7)`、`Gal(K/Q)=C₂={1,σ}`。可分二次代数的标准映射

\[
 K\otimes_\mathbb Q K\longrightarrow K\times K,
 \qquad x\otimes y\longmapsto(xy,x\sigma(y))
\]

是 Q-代数同构；归纳得

\[
 A_n=K^{\otimes_\mathbb Q n}\simeq K^{\,2^{n-1}}
 \qquad(n\ge1).
\]

这里右侧是**代数直积**。因此其整数正规化是相同数目的 O_K 的直积，正规化 scheme 是 `2^(n−1)` 个 Spec O_K 的不交并。此处没有将整 tensor `O_K^⊗n` 自动当正规；bad7 的原整模型/导子问题仍另核。

相应 permutation 表示为 regular `V=1⊕χ`，故在实际 C₂ 表示环中

\[
 V^{\otimes n}=2^{n-1}(1\oplus\chi),\qquad
 \zeta_{\operatorname{Nor}A_n}(s)
       =[\zeta_K(s)]^{2^{n-1}}
       =[\zeta(s)L(s,\chi_{-7})]^{2^{n-1}}.
\]

这不是只试 n=2：两个简单对象的乘法 `χ²=1` 已给所有 n 的精确结果。若用 n 个二元选择计数，总有 `2^(n−1)` 个偶 parity 和同数奇 parity，直接得到上述 multiplicities。这里 normal scheme 的 ζ因不交并而相乘；不是把一般 tensor 的 L 函数错误定义为普通乘积。

这些公式未逐字出现在073，但由给定 separable tower及有限表示代数直接推出，无新算术估计或目标 spectral membership；实例具体化不计新输入。

## 3. 全固定 C₂ 范畴，不只 regular tensor 幂

特征0下每个有限实际 C₂ 表示唯一写为 `W=a·1⊕b·χ`，a,b为非负整数。两个 projector `(1±σ)/2` 实现该分解。故全部普通操作都留在同一二维表示环：

| 操作 | `(a,b)` 角色 |
|---|---|
| direct sum | 两个 multiplicities 相加 |
| tensor `(a,b)⊗(c,d)` | `(ac+bd, ad+bc)` |
| dual | `(a,b)`，两个简单角色均 self-dual |
| invariant subobject/quotient | 仍为某个非负 `(a′,b′)` |
| 任一有限 Schur functor | 仍为某个非负整数 `(a_λ,b_λ)` |
| Adams ψ^k | k奇时 `(a,b)`；k偶时 `(a+b,0)` |

Adams在表示环按 character `Tr ψ^k(W)(g)=Tr W(g^k)` 定义；C₂中上述结果甚至可由实际表示实现。若准 virtual differences，也仅把 a,b放宽为整数，并未增加简单角色。例：`∧²V=χ`、`Sym^mV=(floor(m/2)+1)·1⊕ceil(m/2)·χ`、`ψ^(2j)V=2·1`。

其 Artin L 函数始终为

\[
 \mathcal L(W,s)=\zeta(s)^a L(s,\chi_{-7})^b.
\]

所以全部实际操作的非平凡全局零点都来自原 ζ/Lχ 两个 divisor，只改变相应重数；virtual操作只会形成这两个因子的整数比及可能的共同消去。它们没有产生由原全局零点空间的任意谱对所形成的新 tensor-spectrum。Adams所做 `g→g^k` 作用在有限 Galois/Frobenius character；不能据名称声称它给全局ρ/中心化流生成元取幂。

073定理ND已付 strong/tempered 对 tensor、dual、subquotient、Schur的封闭性；有限 C₂作用可直接平均出 invariant metric，所有 g 的 powers norm为1。这份全范畴酉性完全确定了局部 ±1 的 pure weight0。它没有识别 number-field 全局零点生成元，也没有给附件另一项全 k 的 global cohomological weak bound。

## 4. 单位 realization 是不能省略的检查

单位对象是 `1=(1,0)`，满足 `1⊗W=W`，而其 Artin L函数是 **ζ(s)**。002§2早已以 ζ的每个 local参数只有1说明：局部纯性与全局解析耦合后的 RH 是不同责任。当前非平凡 C₂ tower包含 Lχ，也仍包含这个单位问题；不能把“χ不平凡”当作已经修复 global realization。

如果声称一个到普通向量/Hilbert谱对象范畴的 **strong tensor realization**，通常 tensor单位必须送至一维单位；有限 Frobenius eigenvalue为1（或加法 tensor生成元为0）。这个单位的有限谱不是 ζ全部非平凡零点谱。因此普通 finite-Galois fiber functor/酉内积不能同时免费充当上述全局 zero realization。

此检查不是宣布一切几何 realization 不可能。Relative/graded/cohomological或lax结构可能让全局 base cohomology承担 ζ，并改变单位和 Künneth 的角色；但那是需要实际新构造与完整 trace/determinant 的桥，当前普通 C₂操作没有提供。不能先把这个未付桥当已存在，再调用073的 tensor封闭性证明目标纯性。

073§4已直接写明：number-field Rankin–Selberg 的 local Satake参数虽 tensor相乘，global zero space不是两个旧zero spaces的朴素tensor，仍须独立 global trace/determinant theorem。其余纯度/极化定理均是对已具正确谱角色对象的条件定理；本测试不产生新的目标 membership。

## 5. 净值与停止范围

当前 all-n tower及full fixed-C₂操作可识别；所得ζ/Lχ powers重复旧全局 divisor。这项具体类型检查属001/002/073与标准有限表示代数的**强旧直接0**。

bad7、Γ/pole及附件全弱界不由本稿认证。其它群、非有限单值族、真正global cohomology/trace与独立极化/signed机制不在此固定C₂边界内；未排不授后继预算。

无新关键primitive/mixed/corecross或whole4/5UPPER后果；不建数学合同，不计轮/完成Goal，不开来源或另一candidate。当前稿 terminal，root消费仍须与另两腿准确角色对齐。

## 本地版本

附件仅§6.1–6.2作为数据，其外链未打开；无新source/PDF/web/数值/Git。现场LF版本：

| 文件 | bytes | SHA256 |
|---|---:|---|
| 001 | 9556 | f1f049cceb0714ba3139f93acb4f86e7e007a4fca1c6f97caad4690251504576 |
| 002 | 10963 | 65a5bbe1971ea97d5e40c1da53cba9c06001da2362f85153ec77a97da8f8df35 |
| 073 | 12906 | 3a0a9ab86a5080c4f8af0e18895ef62f31c0e5be52dfbb6ce4580b51a4a76b93 |
| 原附件 | 31170 | 23d203de066b16e6f11ddba4cf0350e3d2cd27fec732067b0768d8b050edef74 |
