# 467 两残差 Schur 与负交换子预算：root 全文独审

2026-10-07。限定 PASS。全文核验七节；未修改作者正文。
被审稿：[467](../../notes/467-two-residual-schur-and-commutator-budget.md)。
canonical LF SHA-256：
0089fd92c70d5e2b7b48bef0084675707f2fe283833f8a97745766ccf6899cb8，
10830 UTF-8 bytes，312行；只改CRLF/lone CR为LF，不trim。
引用的465最终为a9290d2d…50464，466最终为0b955bdc…bbbe。
本人原创这些前置稿，本报告只作为467的独立数学复核；
前置稿另有两位作者的全文独审。

## 1. 原权重准入与残差范数

原 \(W,V\) 都是同一 carrier 上非负、bounded multiplication 的压缩，
不是 freely adjusted compensation。465的 bounded-weight 二矩证明
可对 high/low 两个原权重逐一使用；所需 derivative \(L^1\) 和
HS leakage 常数统一。其complex cross分别支付两种实际矩阵顺序。
乘法 \(WV\) 的 crossing 仅为两个 weight HS leakage 的乘积，\(o(d)\)。
所以正文(3)九项均由已付二矩准入，不是隐藏的 four-word 输入。

精确平方展开给
\[
 \|\Gamma\|_{\rm HS}^2/d=a_T-S_H+o(1),\qquad
 \|\Delta\|_{\rm HS}^2/d=e_T-S_L+o(1).
\]
误差独立于未知 high4 增长。462完整低四矩给 \(\delta_T\to e_\psi-S_L\)；
这一极限非负来自实际平方范数，未由有误差的有限差直接取平方根。
flat 原窗独立有理积分给 \(S_L=7/240\)，
因此 \(\delta_1=19/240-7/240=1/20\)。
这确实强于用整个 \(e_1\) 代替 low 残差能量。

## 2. 有限 Gram 与全部误差

三个向量 \(\Gamma,\Delta,Z=(HL+LH)/2\) 都 selfadjoint。
有限循环迹独立重推给
\[
 \langle\Gamma,\Delta\rangle=c-\chi,\quad
 \langle\Gamma,Z\rangle=b-\tau,\quad
 \langle\Delta,Z\rangle=\eta-\operatorname{Re}\operatorname{Tr}(VHL)/d,
 \quad \|Z\|_{\rm HS}^2/d=c-k/4.
\]
\(\chi\)中的三项和 \(-WV\) 符号正确；
real parts处理非selfadjoint \(HL\) 的顺序，无非法互换。
461的整个13与原复weighted cross给 \(\epsilon=o(1)\)。

对 \(\delta_T>0\) 从 \(\Delta\) 方向投影，得到正文(10)的准确Schur式。
两个右因子是实际残差平方范数，均非负；退化情况也被单独处理。
whole cyclic fourth 为 \(a+e+6c-k+4b+4\eta\)，全部31与22系数完整。
正文(12)保留 \(|p\epsilon|/\delta\)、\(\tau,\eta,\epsilon^2/\delta\)，
所以有限式不要求先有 bounded \(q\)。
只给 \(\epsilon=o(1)\) 时不能免费删除放大项；正文明确保留该限制。

## 3. 紧域极限与有理阻断点

另有 \(\limsup q_T\le Q<\infty\) 后，\(a,e,c,k\) 才都 bounded；
\(|p|\le\sqrt{q\delta_T}\) 保证centering误差消失。
因 \(\delta_\psi>0\)，平方根在可行紧域含零端点连续，
正文(13)–(15)的subsequence论证成立。
近似因子微负时可用positive part或直接在可行极限点取值，
不会偷偷变更移动端点。

实际 \(\liminf q_T\ge41/15120\) 来自466的sharp PSD不等式，
与 low Gram 的 \(k=\|[H,L]\|_{\rm HS}^2/d\) 是不同的交换子对象。
它不能提供 \(k\) 下界。
在 \(q=41/15120,c=1/30,k=0\) 的代数可行点，独立算到
\[
 R=923/29030400,\quad h=359/30240,\quad
 16R-h^2=336311/914457600>0.
\]
\(c^2<(S_H+q)e_1\) 和两个Gram残差非负也成立。
因此舍去 \(k\) 后的保守envelope大于 \(1/3\)。
这只是信息松弛的预算诊断，没有将该Gram实现为actual prime matrices，
更不能由上界较大推actual fourth较大。

## 4. 最终联合候选的全区间证书

正文最终前件是仍未证明的
\(\limsup q_T\le1/350,\ \liminf k_T\ge1/40\)。
前者与已付necessary lower相差 \(11/75600>0\)，
仅说明未被该条障碍排除，不证明两个前件的可达到性。
对固定 \(c,k\) 目标关于 \(q\) 增，对固定 \(q,c\) 关于 \(k\) 减；
因此用 \(Q=1/350,\kappa=1/40\) 放宽极限域合法。
其 radicand 在真正可行域非负，\(c\le C+\sqrt{Q/20}<863/24000\)。

独立Sympy/Fraction计算精确重现
\[
 R(c)=6367/28000-6c\ge163/14000>0,
\]
\[
 P(c)=320c^3+(56/3)c^2-(1257437/504000)c
                          +717527777/14112000000.
\]
在整个 \([0,863/24000]\) 分32等段，四个Bernstein系数的
端点/导数形式与正文(23)准确一致。128个系数全部严格正，
最小 \(665078890949/6502809600000000\)。
正Bernstein基的凸组合给全连续域结论；不是有限网格推论。
平方之前 \(R>0\)，故不会由平方引入错误分支。
于是整个条件预算严格小于 \(81/250\)。

## 5. 实际响应恢复与比例接口

只有先得到 bounded whole-prime fourth 后，才用455的 proper-power
normalized \(S_4\) 小量和454的 flat \(V=Z=J=0\) 背景付款。
452同对象padding、\(d/N\to1\) 和197/228完整finite边界前件仍保留。
独立有理核验
\[
 \frac{(1-1/3)^2}{1-2/3+81/250}=\frac{1000}{1479}>\frac{27}{40},
 \qquad (1/3-81/250)/(2/3)=7/500\in(0,3/4).
\]
这是一侧四矩接口，确实无需另有第三矩极限。
但是其 \(q\) 上界和 \(k\) 下界仍未证明；
正文没有把条件比例登记为实际67.5%以上成果。

限定 PASS：实际有限Schur、原加权二矩准入、已付low残差常数、
有界前件下的紧域预算，以及全区间精确证书。
没有付原whole high signed arithmetic、新的实际比例或无零边界。
