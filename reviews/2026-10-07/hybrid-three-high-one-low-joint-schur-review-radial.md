# 原 finite entire31 联合 Schur 预算的独立全文审查

2026-10-07。radial_review。结论：限定 PASS。
全文独立核对作者报告的有限恒等式、连续优化、等号模型及原算术输入范围。
本次只新增本审查，不修改被审报告、冻结 notes、math 或 Git。

## 1. 最终证据对象

[被审全文](hybrid-three-high-one-low-joint-schur-budget-research.md)
canonical LF SHA-256：
d48a20606a81c88b5b466339c95ee6049b26d50ebc7b23209c936980dcd131b1；
13091 UTF-8 bytes，354行。CRLF/lone CR统一为LF，不trim。

本次另直接读取其原对象及主要输入：

| 输入 | canonical LF SHA-256 |
| --- | --- |
| 461 | f9fdf0b721c76a5cc4c4e4821748007e62975286417e6bec9700e39b6778170b |
| 462 | 868adfeb0d742043f39bd08e0783d66b7a9db11316067b0b3b43d80150cdf680 |
| 463 | 6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90 |

461的entire13小量沿用其明列的conductor-one zeta固定-gap [R]；
462的完整低四矩无需该[R]。本审查没有重证[R]全稿。
463是已付高度替换，不是新的whole-fourth有界性输入。

## 2. 原 finite 对象与真实 Gram 约束

作者(2)保留原interval carrier、sharp prime coefficients、窗及normalizer；
\(H=C_H,L=C_L\) 都是同一有限空间的Hermitian矩阵。
从此使用有限矩阵循环迹合法，未循环physical末端压缩或删除内部\(P\)。
作者的\(a,e,b,\eta,c,s,k,w\)分别是whole finite量，不是标签子族的替身。

直接展开可得
\[
 c=d^{-1}\|HL\|_{\rm HS}^2,\qquad
 k=2(c-s),\qquad w=4c+2s=6c-k .
\]
HS Cauchy给\(|s|\le c\)，故\(0\le k\le4c\)、
\(2c\le w\le6c\)。对\(H^2,L^2\)给\(c^2\le ae\)。
作者(5)–(7)的三个真实HS向量的Gram矩阵与全部系数均正确。

从\(L^2\)方向投影，令
\(U=H^2-(c/e)L^2\)、\(V=HL+LH-(2\eta/e)L^2\)。
其归一化内积为\(2b-2c\eta/e\)，平方范数为
\(a-c^2/e\)、\(2(c+s)-4\eta^2/e\)。
因此(8)的两个右因子都非负，且Schur/Cauchy约束准确：
\[
 \left|b-\frac{c\eta}{e}\right|^2
 \le\left(a-\frac{c^2}{e}\right)
       \left(c-\frac{k}{4}-\frac{\eta^2}{e}\right).
\]
实际\(e_T\to e_0>0\)，所以使用\(e>0\)合法。
退化\(e=0\)时\(L=0\)，报告已单独处理。

## 3. 消去变量、有限误差与 sharp 常数

固定\(a,e,w\)，真实可行域是
\(w/6\le c\le\min(w/2,\sqrt{ae})\)。
删除负项\(-\eta^2/e\)后，作者(10)的函数导数为
\[
 f'(c)=\frac{3c^2-wc-ae}{2e}
 \le\frac{2c^2-wc}{2e}\le0 .
\]
两次不等式分别使用\(c^2\le ae\)和\(c\le w/2\)。
故(12)的radical在\(c=w/6\)处达到所用上界；
centering误差的系数由\(c/e\le w/(2e)\)支付。
\(w\le6\sqrt{ae}\)保证radicand非负，\(w=0\)退化处理也正确。

这是逐\(T\)的有限不等式。仅知\(\eta_T=o(1)\)时，
\(w_T|\eta_T|/(2e_T)\)或\(\sqrt{a_T/e_T}|\eta_T|\)不能无条件写成\(o(1)\)。
报告明确保留了这一限制，未暗中假设未知的whole high4有界。

独立求极值
\[
 \max_{0\le c\le\sqrt{ae}}\left(ac-\frac{c^3}{e}\right)
 =\frac{2}{3\sqrt3}a^{3/2}e^{1/2}
\]
给\(c=\sqrt{ae/3}\)及
\(K_{\rm Schur}=\sqrt{2/(3\sqrt3)}=0.6204032394\ldots\)。
(14)–(16)正确；最后的\(o(1)\)确实需要所明列的\(a_T=O(1)\)。
该前件也给\(w_T=O(1)\)，但本报告没有证明它成立。

## 4. 整个 fourth 展开、连续 envelope 与等号模型

有限cyclic展开准确为
\[
 d^{-1}\operatorname{Tr}(H+L)^4=a+e+w+4b+4\eta .
\]
因此作者(18)–(20)是一侧联合预算，包含entire31、entire22的全部标签。
保留实际\(e_T\)避免在移动feasibility端点错误替换radicand。
当\(\limsup a_T\le A_0<\infty\)，紧域\(v\in[0,1]\)上的连续性
及\(\Phi(a,e)\)对\(a\)单调，合法给作者(19)。
给额外\(W_0\)时仍须最大化整个objective；不能只在\(w=W_0\)代入radical。

对\(a,e>0\)，\(\sqrt{v-v^3}\)在\((0,1)\)严格凹，
两端导数为正、负无穷，极值点唯一。
其导数方程平方后准确给
\[
 (3v^2-1)^2=9\sqrt{e/a}\,(v-v^3),\qquad v>1/\sqrt3 .
\]
该下界排除平方引入的错误根。

作者(22)–(25)的two-point模型也逐项正确：
\(t^2=\beta t+c/e\)、\(\mathbb Et=0\)推出所列二、三、四矩；
令两个diagonal entries的\(L_\pm^4=2ep_\pm\)，
归一化有限迹准确等于指定的\(a,e,c,b,\eta,w\)。
所以\(\eta=0\)下每个\(0<w\le6\sqrt{ae}\)均能达到radical等号；
取\(c=\sqrt{ae/3}\)证明常数sharp。
有理moment例\((a,e,c,b,\eta,w)=(6,1,2,2,0,12)\)的总fourth为27。
实矩阵entries可含根号；声称精确的是这些moment arithmetic。

这些是有限信息层的等号模型，不是实际prime matrix或零点features的实现。
它们说明现有矩约束不能推出无条件\(b=o(1)\)，没有排除更强算术结构。

## 5. 验收范围

限定PASS覆盖所有有限Schur公式、sharp连续envelope、有限模型及正确前件。
461的反向entire13小量严格改进了未来有界high4输入下的常数预算；
它没有支付actual entire high4，也没有支付完整背景的\(AC^3\)。
Repeated high极限不能代替whole \(a_T\)，窗口profile也不能跨对象相混。
本报告未给完整第四矩常数、新简单零点比例、无零边界或RH/RR证明。
