# 415独立来源复核

2026-09-21。原始工具回包另存同名raw.json；正文只作标题、文件链接和行末空白整理。

**来源侧核准：给定收缩提升 \(T\)，所写 \(W\) 是酉元；\(P=W\operatorname{diag}(1,0)W^*\) 给出的边界为 \([P]-[\operatorname{diag}(1,0)]\)，符号与 414 的 ker−coker 一致。** 一般缺陷算子不能直接当作投影。以下未涉及 415 主稿或实际缺陷读出。

**1. 已核读的原件与准确定位**

已存 Blackadar《K-Theory for Operator Algebras》，第二版作者修订本：[本地 Blackadar 原件](../../literature/f1/blackadar-k-theory-author-book6.pdf)

| 原件 | 精确定位 | 核准内容 |
|---|---|---|
| Blackadar，[book6.pdf](https://bruceblackadar.com/Mathematics/book6.pdf) | **8.3.1–8.3.2，印刷 pp.62–63／PDF pp.76–77** | 一般可逆矩阵提升定义指数边界；部分等距提升的边界是初始缺陷投影减终端缺陷投影。 |
| 同书 | **5.5，印刷 pp.30–31／PDF pp.44–45**；**3.4.2，印刷 p.18／PDF p.32** | 非幺 \(K_0\) 的单位化投影差，以及标量部分为单位的矩阵约定。 |
| Robinson，[arXiv:1803.09329v1](https://arxiv.org/pdf/1803.09329v1)，2018-03-25 | **PDF／文内 p.1，Theorem 0；p.2，Theorems 1–2 及随后说明** | Julia 算子酉性、平方根互换、Halmos 酉扩张；p.2 还明确叙述多项式与 Weierstrass 逼近证明。 |
| Blackadar，《Operator Algebras》[作者版本 Cycr.pdf](https://bruceblackadar.com/Mathematics/Cycr.pdf)，首页日期 2017-02-08 | **II.2.3.1–II.2.3.2，文内 pp.63–64／PDF pp.71–72**；**II.3.1.2(vii)，文内 p.65／PDF p.73** | 连续函数演算、一致逼近对应范数收敛、与 \(*\)-同态相容，以及正平方根存在唯一性。 |

后两份原件仅在内存中读取，未保存；以上链接可直接供主线程保存。

**2. 适用前提及直接推导**

设
\[
0\longrightarrow J\longrightarrow B\xrightarrow{\pi}C\longrightarrow0
\]
为 C* 扩张，\(T\in M_n(B^{\sim})\) 满足
\[
\|T\|\le1,\qquad \pi^{\sim}(T)=u,\qquad u^*u=uu^*=1.
\]
非幺归一化情形再要求 \(T-1_n\in M_n(B)\)。无需 \(T\) 正规、可逆或部分等距，也无需严格收缩。

若沿用 414 的 \(T=(1-Q)+QuQ\)，其相对于 \(Q\) 的分块为恒等算子与酉元的压缩，故收缩性直接成立；这只核对适用前提。

记
\[
d_{\rm in}=1-T^*T,\quad d_{\rm out}=1-TT^*,\quad
a=d_{\rm in}^{1/2},\quad b=d_{\rm out}^{1/2}.
\]
二者是正收缩；商酉性给出 \(d_{\rm in},d_{\rm out}\in M_n(J)\)，连续函数演算又给出 \(a,b\in M_n(J)\)。这是上述 Blackadar 连续函数演算条款的直接应用，**不能只引用 book6 §3.1 的全纯函数演算**，因为平方根在零点不具备所需全纯性。

平方根互换可完全在 C* 代数内直接证明：
\[
Td_{\rm in}=d_{\rm out}T
\quad\Longrightarrow\quad
Tp(d_{\rm in})=p(d_{\rm out})T
\]
对所有多项式 \(p\) 成立。取 \(p_m\to\sqrt{\cdot}\) 在 \([0,1]\) 上一致收敛，由连续函数演算取范数极限，得到
\[
\boxed{Ta=bT},\qquad aT^*=T^*b.
\]
Robinson Theorem 1 陈述同一恒等式；其 p.2 也明确记录上述传统证明。将其落实到抽象 C* 代数，是这里借助连续函数演算完成的直接推导。

**3. Robinson 的矩阵与本稿 \(W\) 的关系**

Robinson Theorem 2 使用
\[
V=\begin{pmatrix}T&b\\a&-T^*\end{pmatrix}.
\]
令 \(S=\operatorname{diag}(1,-1)\)，则本稿
\[
\boxed{W=VS=\begin{pmatrix}T&-b\\a&T^*\end{pmatrix}}.
\]
因此 \(W\) 酉。也可直接乘块验证：对角块由缺陷定义给出单位，非对角块由 \(Ta=bT\) 消去。这是**列符号变换与直接计算**，不是 Robinson 原文所印矩阵的逐字复制。

取 \(e=\operatorname{diag}(1,0)\)，因为 \(SeS^*=e\)，
\[
WeW^*=VeV^*.
\]
所以该列符号调整**完全不改变 \(P\)**，不产生指数反号。

**4. 投影归属及指数符号**

直接计算给出
\[
P=WeW^*
=\begin{pmatrix}
TT^*&Ta\\
aT^*&1-T^*T
\end{pmatrix}.
\]
酉共轭保证 \(P=P^*=P^2\)。又有
\[
\pi(W)=\operatorname{diag}(u,u^*),\qquad
P-e=
\begin{pmatrix}
-d_{\rm out}&Ta\\
aT^*&d_{\rm in}
\end{pmatrix}\in M_{2n}(J).
\]
故 \(P\in M_{2n}(J^{\sim})\)，并且 Blackadar **8.3.1 直接给出**
\[
\boxed{\partial[u]=[P]-[e]\in K_0(J)}.
\]

符号由 **8.3.2** 再次固定：若提升恰为部分等距 \(v\)，则
\[
P=\operatorname{diag}(vv^*,1-v^*v),\qquad
\partial[u]=[1-v^*v]-[1-vv^*].
\]
在 Hilbert 空间 Fredholm 情形，这正是
\[
[\ker v]-[\operatorname{coker}v].
\]
因此与 414 一致；单边正移位给负一。

这里可引用 Blackadar 的**一般定义与部分等距特例**，不能声称其 §8.3.2 已直接证明一般收缩的平方根矩阵。

**5. 缺陷算子的准确称谓**

一般的 \(d_{\rm in},d_{\rm out}\) 及其平方根只是正算子，不能写成未经证明的投影类
\[
[d_{\rm in}]-[d_{\rm out}].
\]
即使商为酉也不例外：令 \(E\) 为秩一投影、\(T=1-\tfrac12E\)，则 \(T\) 是可逆收缩且模紧算子为单位，但
\[
d_{\rm in}=d_{\rm out}=\tfrac34E
\]
均非投影。一般情形应使用上面的真实投影差 \([P]-[e]\)。

**实际原件 SHA256 与核读范围**

- **本地 book6，314 页：**
  `a20e676e9d400ebcd0cd07c13fbdbe1fac759a30c739fab23d6161ecfb1a23fb`
  相关正文核读 PDF 29–30、32–33、44–45、73、75–77；76–77 页另作内存渲染核对。
- **Robinson v1，3 页，75,604 字节：**
  `a4b45d9ad1151cec0c25d44ecdfbfd0cd382e473ca360c66d07cef20e69be0a6`
  全文读取，1–2 页另作内存渲染核对。
- **Cycr.pdf，561 页，2,495,419 字节：**
  `8cb61a8348efe6e4b36dbefed4eac2c35498d28c03e160638ad7af952457f88a`
  核读版本首页及 PDF 71–73 页，后三页另作内存渲染核对。

Williams 已存原件仅作关键词定位，未作为本结论的直接依据。未直接核读 Halmos 1950 原论文或 *Problem Book*；有关历史归属仅由 Robinson 转述。未读取 415 主稿，未计算实际缺陷读出，未修改或新增文件，未运行 Git／Lean。
