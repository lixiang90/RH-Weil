# 高素数重复四词报告的独立全文审查

2026-10-07。结论：**限定 PASS**。独立读取全部 572 行并重算主要估计，未发现阻断下述重复标签 sector 结论的错误。通过范围为原 AF 有限压缩上、\(\sqrt X<p\le X\) 的重复标签四词；不是完整四矩预算、比例改进或 RH 证明。

## 1. 审查对象与版本

审查对象为 [研究报告](hybrid-high-prime-four-word-response-research.md)，canonical LF SHA256：

~~~text
988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666
~~~

canonical LF 指 CRLF 和孤立 CR 换成 LF，其余字节不变。报告为 572 行。本次没有编辑研究报告、旧笔记、论文或审计输出。

对象及 Fourier/frame 前件与 [Alpöge–Furman v2 §2](https://arxiv.org/html/2608.13637v2#S2) 核对。项目所存 AF v2 PDF 的原始 SHA256 为：

~~~text
6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444
~~~

weighted finite Hilbert 输入与 [Montgomery–Vaughan, *Hilbert's inequality*, Theorem 2、Corollary 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf) 核对。它给局部间距倒数加权的有限 Hilbert 型界，且 endpoint 相位不改变系数模；本审查不重证其通用定理。Mertens/Chebyshev 是明确的经典算术输入。研究报告不使用固定 OpenAI 无零论证作为这些估计的前件。

## 2. 原 Fourier 对象及有限投影

报告 §2–3 的归一化正确。取 \(E e_k=L^{-1/2}1_I e^{i\tau_k u}\)、单位化 Fourier 及 \(F=\mathcal F M_\phi E\)，则
\[
 F e_k=\frac{\widehat\phi(t-\tau_k)}{\sqrt{2\pi L}},\qquad F^*F\le1.
\]
乘子 \(-\pi^{-1}\sum_p\lambda_p\cos(t\ell_p)\) 在原矩阵归一化 \(2\pi/(a_LL)\) 下，确切给
\[
 C_p=E^*B_pE,\quad
 B_p=-\frac{\lambda_p}{a_LL}\,M_\phi(R_{\ell_p}+R_{-\ell_p})M_\phi .
\]
没有遗失 \(2\pi\)、\(L\)、finite carrier 或原 height 轴。

因 \(\ell_p>L/2\)，两次同向物理位移无支撑。每个 \(B_p\) 是两端区间之间的加权翻转，故 \(\|B_p\|_{\rm op}\le b_p\)，而非仅有 \(2b_p\) 的粗界；报告 (9) 的 \(B_p^2\) 乘法公式成立。

§3 的 circle 写法只用于计算 Fourier 系数：原零延拓平移等于 \(M_{a_s}\) 乘 quasiperiodic rotation，绕回部分恰因 \(a_s(u)=\phi(u)\phi(u+s)=0\) 消失。rotation 与所选 finite Fourier projection 交换，因而没有用周期平移替换物理支撑。

固定 \(\chi,\psi\) 时，\(\|a_s'\|_1+\|a_s''\|_1=O(1)\) 对所有所涉 \(s\) 统一。由
\[
 |\widehat a_s(n)|\ll\min(1,|n|^{-1},L/n^2)
\]
及 outgoing frequency 的准确计数，得到
\[
 \|Q M_{a_s}P\|_{\rm HS}^2
 =\sum_{n\in\mathbb Z}\min(d,|n|)|\widehat a_s(n)|^2
 \ll\log(2+L).
\]
报告 (14)–(17) 的 H\(^{1/2}\) 泄漏付款合法。对 \(B=\sum_pB_p\)，用 triangle inequality 得 \(X\log L/L^2\)；没有假设不同 primes 的泄漏正交。该量除以 \(d\asymp XL\) 确为 \(o(1)\)。

## 3. weighted Hilbert 与相同主项

§4 的 \(K_d(s)\) 是原有限几何核，包含完整 \(T+(d-1)\pi/L\) 相位。对 \(\ell_p-\ell_q\)，跨度小于 \(L/2\)，局部 log 间距至少 \(1/(2p)\)。将 sine numerator 分成两个 exponential 后，MV weighted Hilbert 的相位吸收保持原系数模。cosecant 的余项可由 \((\sum_pb_p)^2/d\) 支付，主项由
\[
 \frac Ld\sum_p\frac{b_p^2}{\delta_p}
 \ll\frac Ld\,\frac{X}{L}=O(L^{-1})
\]
支付。任意有界非负权 \(w(u)\) 可在这个 pointwise 界后积分。原正、负输出支撑分离，故报告 (21) 的两个 physical traces 确切给 \(d\langle d_L\rangle\) 和 \(d\langle d_L^2\rangle\)。

§5 的两个关键比较可独立成立：

- \(\widehat{\mathcal D}-\mathcal D=\sum_p E^*B_pQB_pE\ge0\)，其迹为 \(O(\log L)\)，且两者 operator norm 统一有界；
- 用 \(BE=EC+QBE\) 和 \(\|P M_{d_L}Q\|_{\rm HS}=O(\sqrt{\log L})\) 支付 weighted physical/compressed 比较，误差为 \(O(X\log L/L^2)\)。

因此
\[
 T_0=d\langle d_L^2\rangle+
 O(d/L+X\log L/L^2),\qquad
 T_{22}=d\langle d_L^2\rangle+O(\log L).
\]
第二式使用正的 \(\widehat{\mathcal D}-\mathcal D\) 和乘法压缩的 HS 泄漏；不要求这些矩阵交换。两项具有同一主项，是报告后续 signed 消去的真实依据。

## 4. \(pqpq\) 的三个 \(P\)、物理 span 与 alias

§6 的三次删除逐项成立。从左向右删除时，每个新 \(Q\) 的右邻仍保留 \(B_rP\)，可用小 HS 泄漏；另一个 HS 因子保留 rank \(d\)。例如报告给出的第二项
\[
 \operatorname{Tr}(PB_pB_qQB_pPB_qP)
\]
确由 \(\|QB_pP\|_{\rm HS}\) 和 \(\sqrt d\,b_pb_q^2\) 支付。三项合计的可求和系数是 \(\sum_{p,q}b_p^2b_q^2=O(1)\)，故误差 \(O(\sqrt{d\log L})=o(d)\)。这没有证明四 distinct primes 的 aggregate 删除合法。

原 physical 四词 kernel (30)–(31) 的全部中间位置与 endpoint 因子正确。每步大于 \(L/2\) 强制两个 alternating sign patterns。对 \(pqpq\)，非空路径进一步强制
\[
 |2(\log p-\log q)|<L/2.
\]
报告对 \(S_3\) 或 \(S_1-S_4\) 的反证恰是实际 path span 检查；因此该项可以使用原有限核的无 alias 界。

非对角整数 majorant
\[
 \sum_{\sqrt X<n<m\le X}\frac1{nm(m-n)}
 \ll\frac L{\sqrt X}
\]
成立：先对 gap \(h\) 求和给 \(H_n/n^2\)，再对 \(n>\sqrt X\) 求和。空路径的项为零，报告没有把小位移界用于 alias 附近的非空路径。\(p=q\) 项由 \(d\sum_pb_p^4=O(d/L^4)\) 支付。故 (34) 的 \(T_\times=o(d)\) 成立。

## 5. partition、显式常数与全 height

§7 的 partition Möbius 恒等式
\[
 S_{\rm rep}=4T_0+2T_{\rm opp}-2T_{22}-T_\times-8T_3+6T_4
\]
与四个位置的 equality partition 相符：六个 single pairs、三个 double pairs、四个 triples 及一个全相等 partition 的 Möbius 系数分别为 \(1,-1,-2,6\)，cyclic trace 产生所列合并系数。

Hermitian 性给 \(|\operatorname{Tr}(ABAB)|\le\operatorname{Tr}(A^2B^2)\)，故 \(|T_{\rm opp}|\le T_0\)。由 \(\operatorname{Tr}|C|=O(d)\)、\(\sum_p b_p^3=O(L^{-3})\)、\(\sum_pb_p^4=O(L^{-4})\)，可独立支付 \(T_3,T_4=o(d)\)。没有借用待证的完整 \(\operatorname{Tr}C^4=O(d)\)。报告于是得到
\[
 -o(d)\le S_{\rm rep}\le4d\langle d_L^2\rangle+o(d).
\]
它没有把 signed sector 本身说成非负矩阵。

§8 的 Mertens partial summation 与 fixed taper 的 endpoint/shifted edge 宽度正确，得到 \(S_\psi+O(1/L)\)。flat 积分独立重算为
\[
 S_{\psi_0}=2\int_0^{1/2}\left(\frac{v+v^2}{2}\right)^2\,dv
 =\frac{19}{480},\qquad4S_{\psi_0}=\frac{19}{120}.
\]
MT 的 (44) 是 \(\int r\cos(\sqrt2(r-v))\,dr\) 的准确 antiderivative；其严格结果是显示积分，浮点小数只作展示。

§9 的整条 height 轴处理正确。四次 scalar spectral Jensen 是对 eigenvector 的谱测度使用 convex \(x^4\)，不需要 operator convexity。\(J^c\) 的 positive majorant 使用 \(M_{\rm hi}^4=O(X^2)\)、Fourier 尾 \(dX^{-3}\) 及原归一化，费用为 \(d/(XL^5)=o(d)\)。这里只分割正积分，没有把矩阵四迹无 cross terms 地拆成两个 height 四迹。

## 6. 验收范围

固定原 \(\chi,\psi\)，先固定精度再取所有充分大 \(X\)，报告的统一 \(o(d)\) 和 \(N\sim d\) transfer 成立。没有提供可计算的数值 height 起点，也没有认证 MT 小数的 rational interval。

本次另作了不写文件的有限有理系数检查及 flat 积分检查。它们只辅助有限代数，不能认证无穷素数均值。原有限审计的全部数学分析仍由上面的逐项论证支付。

最终限定 PASS：仅高素数 **重复标签** sector 的原 finite signed response 预算。四 distinct high words、low/high mixed words、背景/极点算子全部 mixed terms，以及与原四矩惯性链的完整合并仍未支付；因此不能据此提高简单临界线比例或宣称 RH/RR、算术桥闭合。
