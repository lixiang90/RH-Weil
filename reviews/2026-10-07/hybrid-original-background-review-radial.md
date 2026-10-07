# 454：原背景与完整 Λ weighted mixed traces 的独立全文审查

2026-10-07。结论：**限定 PASS**。完整读取冻结主稿 425 行，独立核对原 Fourier/physical normalization、全 log-range difference/sum alias、Gamma/pole 全高度费用、projection/commutator比较、leading integrals与条件第四迹桥梁。未发现阻断 (1)、(28) 或其明确条件结论的错误。没有把未知 \(\operatorname{Tr}C^4=O(N)\) 当作已付前件。

## 1. 最终绑定与明确输入

对象：[notes/454](../../notes/454-original-background-and-weighted-prime-mixed-traces.md)，canonical LF SHA256：

~~~text
8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7
~~~

主稿 13284 canonical UTF-8 bytes、425 行。最后由待审改为限定通过并加审查链接是元信息变化；数学与本次全文核验对象一致。canonical LF 仅替换 CRLF、孤立 CR 为 LF。没有编辑主稿、冻结论文/笔记或审计输出。

原对象和 normalization逐项核对 [AF v2 §2](https://arxiv.org/html/2608.13637v2#S2)：\(\nu_X=\mu+\Pi_X+P_X\)、(2.3)–(2.4)的 Gamma/pole bounds、原 frame (2.11)、Poisson–Gabor identity及 Lemma 2.2/(2.12)。项目所存原 AF PDF raw SHA256 为：

~~~text
6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444
~~~

weighted Hilbert 输入亦与 [Montgomery–Vaughan, *Hilbert's inequality*, Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf) 的局部间距倒数界相符。经典 Chebyshev/Mertens 及该发表 theorem是明确通用输入，本审查不重证其一般定理。

另只读核对两个项目接口：

| 对象 | canonical LF SHA256 |
| --- | --- |
| [high report §3](hybrid-high-prime-four-word-response-research.md) | 988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666 |
| [全高度 frame/background 接口 §5](hybrid-uniform-reciprocal-and-fourth-trace-interface.md) | 25468f8c29dc195d08083dd0fb4b60b5aea48478c9c1ce93053875d5dcc7d83c |

454 不调用固定 OpenAI 无零 source 或新的 strip/family合同。最后 H→\(G_P\) 的稳定性引用452，属于另已支付接口；它没有参与本文四个背景量的证明。

## 2. Gamma、pole和同一原背景

§1的原矩阵为 \(H-I=A+C\)，\(C=2\pi(a_LL)^{-1}F^*M_{P_X}F\)。以 unitary Fourier、\(F=\mathcal F M_\phi E\)，物理 \(B\)恰为 (3)，包括全部 sharp \(\Lambda(n)\)；没有 prime-only 替换或额外 factor 2。

在 \(J=[T/2,3T]\)，原 \(\mu(t)=L/(2\pi)+O(1)\)。常数部分在原 frame下给
\[
 a_L^{-1}E^*M_{\phi^2}E-I=E^*M_{h_L}E=A_0.
\]
Bessel 给余项 \(O_{\rm op}(1/L)\)。实际全高度尾的权
\(\log(2+|t|)+L\) 结合 \(C^2\) Fourier decay，确给 \(dL/T^3\)；除以原 \(a_LL^2\)，是 \(O(T^{-2})\)。其 operator bound来自正的 absolute-weight compression，不要求 signed \(\mu-L/(2\pi)\) 为正。

原 \(|\Pi_X(t)|\ll\sqrt X/(1+|t|)\)，在 \(J\)及外侧分别用 Bessel和正尾支付。低 height、负 height、pole均未被删除。故
\[
 A=A_0+R_T,\quad \|R_T\|_{\rm op}=O(1/L),\quad \|A\|_{\rm op}=O(1)
\]
成立。这里只用 \(d\sim N\)，未使用过强的 \(d=N+O(L)\)。

## 3. 原有限 projection及 full difference-frequency Hilbert

§2将物理零延拓平移表示为 \(M_{a_s}\) 乘 quasiperiodic rotation；wrap部分因 \(a_s=0\)消失。该rotation与原有限 carrier projection交换。由原固定 \(C^2\) tests得到
\[
 |\widehat a_s(j)|\ll\min(1,|j|^{-1},L|j|^{-2}),\qquad
 \|Q M_{a_s}P\|_{\rm HS}^2\ll\log(2+L)
\]
对所有 \(\log n\in[\log2,L]\)统一，不仅对 high primes。

原 \(\sum b_n\ll\sqrt X/L\)、\(\sum b_n^2=O(1)\)包含全部 prime powers。triangle给
\(\|QBE\|_{\rm HS}^2\ll X\log L/L^2=o(d)\)，没有假设不同 \(n\) 的泄漏正交。\(h_L,h_L^2,h_L^3\)的 periodic endpoints及derivatives相接；带 \(a_s(h_L-h_L(\cdot+s))\) 的 coefficients同样合法。

§3.1最重要的 full-range处理正确：把原 \(K_d\) 的两个 endpoint exponent全部保留，先对**全部** \(n\ne m\) 的 \(L/(\pi s)\)主项使用 Hilbert。每个固定 \(u\) 的 \(g_{\pm,n}(u)\)都是相应 bilinear coefficients，允许依赖 \(n\)；bounded \(w(u)\)可在该 pointwise估计后积分。没有先截频率再免费引用 Hilbert。

局部 spacing \(\delta_n^{-1}\le2n\) 及 \(\sum_{n\le X}\Lambda(n)^2\ll XL\)，给主费 \(O(1/L)\)。small remainder给 \(O(L^{-3})\)。large差频率时
\[
 L-\log(n/m)=\log(Xm/n)\ge\log m
\]
并且 \(n>\sqrt X,m\le\sqrt X\)。使用 \(\Lambda(m)/\log m\le1\)及两个真实系数和，(14)准确为 \(O(X^{-1/4}L^{-2})\)。这是额外付出的端点费用，不能从 high-only跨度结论直接领取。

## 4. opposite-sign sum alias与 weighted二矩

§3.2没有把 low outputs当作支撑分离。原两端同时在 \(I\)强制
\(s=\log(nm)\le L\)，overlap长至多 \(L-s\)。\(s=L\)的确切 integer alias积分为零。

\(s\le L/2\)时原 kernel为 \(O(1/X)\)。Chebyshev迭代及 prime harmonic bound给
\[
 \sum_{nm\le Y}\frac{\Lambda(n)\Lambda(m)}{\sqrt{nm}}
 \ll\sqrt Y\log(2Y),
\]
故此区间的 normalized费是 \(O(X^{-3/4}/L)\)。对 \(L/2<s<L\)，
\[
 \min(1,(X(L-s))^{-1})\frac{L-s}{L}\le\frac1{XL}.
\]
合计 near-alias费 \(O(1/(\sqrt X L^2))\)。两种 opposite signs同付，carrier始终只取原 unit phases，没有删除。

因此 (17)是真实 \(E\)-norm展开后的结论，包含全部不同 integer log frequencies。它适用于本稿指定 \(g,w\)，包括 commutator coefficients；signed \(w\)用绝对界支付 error，主项仍保持其符号。取 \(g=a_s,w=1\)，先独立得到
\[
 \operatorname{Tr}C^2=O(d),\quad\operatorname{Tr}|C|=O(d).
\]
此步骤没有第四矩输入。

## 5. \(A^2C^2\) 与 commutator的所有有限比较

§4使用正的
\[
 E^*M_{h_L^2}E-A_0^2=E^*M_{h_L}QM_{h_L}E,
\]
其迹 \(O(\log L)\)。乘 \(C^2\)时以 \(\|C\|_{\rm op}^2\)付费，得到 \(O(X\log L/L^2)=o(d)\)。

\(BE=EC+QBE\)的 weighted比较 (19)正确：cross term用
\(\|C\|_{\rm op}\|P M_{h_L^2}Q\|_{\rm HS}\|QBE\|_{\rm HS}\)，正残项用
\(\|h_L\|_\infty^2\|QBE\|_{\rm HS}^2\)。由 (17)得到
\[
 \operatorname{Tr}A_0^2C^2=d\langle h_L^2d_L\rangle+o(d).
\]
实际 \(A^2-A_0^2\)的 \(O_{\rm op}(1/L)\)只乘先证的 \(\operatorname{Tr}C^2\)，合法付 \(O(d/L)\)。

对 \(ACAC\)，使用 \(D=[M_{h_L},B]\)而没有假设 coupled endpoint coefficient可作separable Hilbert。其 physical diagonal恰是(21)的 \(j_L\)。有限压缩误差
\[
 [A_0,C]-E^*DE=-E^*M_hQBE+E^*BQ M_hE
\]
的 HS norm为 \(O(\sqrt{X\log L}/L)=o(\sqrt d)\)。先由 (17)取得 \(DE\)的 \(O(\sqrt d)\) HS bound，再减它的小 projection leakage，故 squared-norm比较不循环。实际 \([R_T,C]\)的 HS费是 \(O(\sqrt d/L)\)。

由此(22)成立，并由有限 Hermitian恒等式
\[
 \operatorname{Tr}ACAC=\operatorname{Tr}A^2C^2-\tfrac12\|[A,C]\|_{\rm HS}^2
\]
取得其真实 leading term。没有忽略任何 internal finite projections。

## 6. 纯背景、single-\(\Lambda\)项与积分常数

§5中 multiplication压缩幂与 whole multiplication压缩的 trace-norm差 \(O(\log L)\)，可由每条 \(P\to Q\to P\)路径的两个小 HS crossings支付。故 \(\operatorname{Tr}A_0^4=d\langle h_L^4\rangle+O(\log L)\)。

\(A_0^3C\)的两次有限比较分别只用 \(O(\log L)\) trace norm乘 \(\|C\|_{\rm op}\)，以及 \(h_L^3,B\) 的 HS leakages。physical single shift包含准确 \(K_d(\pm\log n)\)。small log范围的核 \(O(1/X)\)与large log范围的实际 overlap分别付清，\(n=X\)时support积分恰为零。故 \(A_0^3C=o(d)\)。实际 \(A^3C\)的替换只用 \(\operatorname{Tr}|C|=O(d)\)，不是未知的 \(\operatorname{Tr}|C|^3\)。

§6的 \(d_\psi,V_\psi,Z_\psi,J_\psi\)与 full-range normalized Mertens measure \(r\,dr\)相符。finite proper powers始终在 \(C,B\)；其 \(\Lambda^2/n\)总 mass收敛，除以 \(L^2\)后只在这些二矩主项中消失。这不支付它们在未知完整 fourth words中的贡献。

\(J_\psi\le4Z_\psi\)由交换两 endpoints的对称性及
\((h-h')^2\le2h^2+2h'^2\)准确得到。四个 leading limits (1)因此通过。flat的 \(h=0\)指 bulk leading profile；不是宣称 finite \(A\)本身为零或operator norm趋零。

## 7. 剩余 \(AC^3\)、第四迹恒等式与条件范围

完整 cyclic expansion给
\[
 \operatorname{Tr}(A+C)^4
 =\operatorname{Tr}A^4+\operatorname{Tr}C^4
 +4\operatorname{Tr}A^3C+4\operatorname{Tr}AC^3
 +4\operatorname{Tr}A^2C^2+2\operatorname{Tr}ACAC .
\]
因此(28)的 \(F_T+4Y_T+6Z_\psi-J_\psi+V_\psi+o(1)\)准确。所有已替换项只用二矩/有界背景，故此 \(o(1)\)不要求 \(F_T\) bounded。

三-\(\Lambda\) mixed量仍是实际
\[
 Y_T=\operatorname{Tr}(AC^3)/N.
\]
主稿正确地没有用 \(R_T=O_{\rm op}(1/L)\)免费替换它；未知 \(\operatorname{Tr}|C|^3\)可能使该操作失效。HS Cauchy准确给
\[
 |Y_T|\le\sqrt{Z_TF_T},\qquad
 Z_T=\operatorname{Tr}A^2C^2/N\to Z_\psi,\quad F_T=\operatorname{Tr}C^4/N\ge0.
\]
这里 \(Z_T\)是实际非负二矩 quantity。只有未来独立支付 \(\limsup F_T\le F<\infty\)后，才得到(30)。flat背景的该条件主费用为零；不能据此提前删除 unknown prime/mixed words。

未付项目明确为：完整 \(\Lambda\) fourth \(F_T\)、实际 three-\(\Lambda\) background covariance \(Y_T\)、four-distinct/high-low words、whole-cell/alias联合算术。该条件桥梁不是 prime fourth预算完成，也不是新比例、RH/RR或无零区证明。

## 8. 新有限脚本的读取范围与最终metadata

只读检查了 [新脚本](../../scripts/hybrid_background_exact_audit.py)及
[当前输出](../../output/hybrid-background-exact-audit.json)，没有运行、覆盖任何脚本输出。最终 canonical LF SHA256：

~~~text
script  dfd8aa390df5a34a3dab27154648bfc6e903894f6b2ff2514156bcfd7b0c2105
output  cc9cd60b8977a03e577f50804a3f0d811a80f7bc86c728fdb98b4fc27539b974
~~~

最终脚本 7086 canonical UTF-8 bytes、182 行，输出 2881 bytes、113 行。JSON实际 input binding已与最终454的 8ab99d60…版本，以及新增的 [mixed报告](hybrid-low-high-mixed-four-word-research.md)一致；后者 canonical LF SHA256 为：

~~~text
71f62b2dd931cfda012e7dad9c4efcfece63f5cf1bb8ff5b466d3e2ac1ae89f9
~~~

mixed报告为 22126 canonical UTF-8 bytes；script metadata亦与磁盘一致。本次只读核对最终九模型及绑定，没有运行脚本或覆盖输出；454数学正文未变。

script的 cyclic expansion与 commutator coefficients是有限 word代数。两个 rational polynomial profiles的 \(V,Z,J\)使用 Fraction积分；新增
\[
 J_{HL}=\int_0^{1/2}\int_0^{1/2-v}
 (\tfrac12+v)\,r\,(\tfrac12-v-r)\,dr\,dv=\frac1{640}
\]
及 \(D_{HL}=23/960\)、\(4D_{HL}+8J_{HL}=13/120\)是正确的 finite polynomial geometry。它们没有证明相应 actual mixed-prime asymptotic；JSON明确排除了无限 Hilbert、projection、全height尾和 prime correlations认证。

新增 mixed_partition 对 \(n_H,n_L\in\{1,2,3\}\) 的九个模型，枚举全部四字词，恰保留两个 high、两个 low且 high标签相同或 low标签相同的并集。右侧两个 repeated sectors用 \(4(ppqr)+2(pqpr)\)，再减去两个标签都重复的交集 \(4(ppqq)+2(pqpq)\)。cyclic canonicalization只作旋转，不作 reversal、交换或删除 finite projections；故有限 inclusion–exclusion 与原 trace cyclicity相符。独立组合计数给
\[
 \#\mathrm{words}=6n_Hn_L(n_H+n_L-1),\qquad
 \#\mathrm{classes}=\frac{n_Hn_L(3(n_H+n_L)-2)}2,
\]
逐项与当前九个 JSON模型吻合，包括 \(3,3\) 模型的 270 个 labelled words、72 个 cyclic classes。这只核验有限标签代数与并集扣交集；不认证这些 words 的真实 prime correlations、asymptotic或完整 fourth bound。

最终限定 PASS：454的四个已列背景 mixed limits、无第四矩前件的恒等式(28)，以及显式 \(F<\infty\)前件下的一侧 bridge(30)。通用 primary inputs未被误标成新的 whole-kernel认证；没有新零点比例或新无零边界。
