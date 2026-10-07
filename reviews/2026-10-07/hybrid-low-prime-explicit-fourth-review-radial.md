# 453：原低素数显式四矩预算的独立全文审查

2026-10-07。结论：**限定 PASS**。完整读取当前 321 行主稿，独立核对加权均值、不平衡项、scalar Jensen、原有限 frame、proper powers 及量词。未发现阻断所述一侧预算的数学缺口。此结论不认证完整 signed response 的四矩常数，也不提高零点比例或无零边界。

## 1. 对象、版本与输入范围

对象：[notes/453](../../notes/453-explicit-low-prime-fourth-moment-budget.md)。当前 canonical LF SHA256：

~~~text
0df65e79b5875fc0e5f7110ceaa05723e4db0cca0b3cc443551c7005a700ddf6
~~~

canonical LF 只替换 CRLF 和孤立 CR 为 LF。本次读取最终 321 行；没有编辑主稿或运行、覆盖旧审计输出。

为核对原对象，另读取 [448 §5](../../notes/448-canonical-type-i-admission-finite-gram-and-low-prime-fourth-norm.md)，其 canonical LF SHA256 为：

~~~text
6a7219f929cc50a721227c722fd9553eb7eba1ed9d4dd432bd971b39c2e6eafa
~~~

原 Fourier/frame、finite carrier、\(a_L\) 和全高度 Fourier 尾，与 [Alpöge–Furman v2 §2](https://arxiv.org/html/2608.13637v2#S2) 核对。项目原 PDF 的 raw SHA256 为：

~~~text
6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444
~~~

均值的通用输入与 [Montgomery–Vaughan, *Hilbert's inequality*, Theorem 2、Corollaries 2–3](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf) 核对：有限实频率的 weighted Hilbert 界给局部间距倒数费用，任意 interval 的积分误差来自两个 endpoint 的该 bilinear form。这里使用其已发表定理，不重证通用定理；Chebyshev/Mertens 亦为明确经典输入。453 不使用 7/8、新 \(\sigma_*\)、RH 或新 prime-correlation 前件。

## 2. genuine-prime square 与 weighted error

§2 的 unique factorization 计算准确：
\[
 c_{pq}=2b_pb_q\ (p\ne q),\qquad c_{p^2}=b_p^2,
\]
因而
\[
 \sum_n|c_n|^2=2S_Z^2-\sum_pb_p^4,\quad
 \sum_n n|c_n|^2=2R_Z^2-\sum_p(\log p)^4.
\]
这里重复标签碰撞已合并，不把 ordered pairs 当独立频率。

对实际出现的 \(\log n\)，局部间距下界 \(1/(2n)\) 合法。MV 的两个 endpoint 相位 \(e^{iA\log n}\)、\(e^{i(A+H)\log n}\) 只改变系数相位，因此 (7) 的常数与起点 \(A\) 无关，长度 \(H\ge0\) 的范围也合法。由 Chebyshev 得 \(R_Z\ll Z\log(2Z)\)，故真正误差为
\[
 O\!\left(\sum_n n|c_n|^2\right)
 =O(Z^2\log^2(2Z)).
\]
在 \(Z=\sqrt X\) 仍只有 \(O(TL^2)=o(TL^4)\)。若只保留 \(Z^2\sum|c_n|^2\)，在该 endpoint 会得到 \(O(TL^4)\)，确实无法支持本文的显式 leading constant。

\(S_Z=\tfrac12\log^2Z+O(\log(2Z))\) 的系数与 Mertens partial summation 相符，\(\sum b_p^4<\infty\)。另作的不写文件有限有理系数检查验证了这两个 collision 恒等式，但无穷素数估计仍由上述解析论证和经典输入支付。

## 3. 实部第四矩的全部不平衡项

§3 的 scalar expansion
\[
 (\operatorname{Re}Q)^4
 =\tfrac38|Q|^4+\tfrac12\operatorname{Re}(Q^3\bar Q)
  +\tfrac18\operatorname{Re}Q^4
\]
正确。后两项的实际费用足够，不能被当作自动为零。

四同号频率至少 \(\log16\)，endpoint exponential integral 至多 \(2/|\omega|\)。\(\sum_{p\le Z}(\log p)/\sqrt p\ll\sqrt Z\) 给 (9) 的 \(O(Z^2)\)，与 \(H,A\) 无关。

三正一负的系数和支撑也准确：\(C_3(n)/\sqrt n\) 仍含原三个 prime factors 的顺序 multiplicity；\(n\) 不可能等于第四个 prime，故确无零频率。去掉 \(p_j\le Z\) 的条件仅用于 positive upper bound。先估第三个 prime 的 Chebyshev sum，再付两次 prime harmonic sum，得到
\[
 \sum_{n\le y}C_3(n)\ll y\log^2(2y).
\]
near 区域 \(p/2\le n\le2p\) 中 \(n\le2Z\)、\(p\asymp n\)，且
\[
 \frac{\log p}{\sqrt{np}\,|\log(n/p)|}
 \ll\frac{\log(2Z)}{|n-p|}.
\]
对每个 \(n\) 放大成全部整数 \(1\le m\le Z,\ m\ne n\)，harmonic gap 总和为 \(O(\log(2Z))\)，包括 \(Z<n\le2Z\)。合计 near 费为 \(O(Z\log^4(2Z))\)。far 中 \(|\log(n/p)|\ge\log2\)，原正系数总 mass 给 \(O(Z^2)\)。因此 (13) 的 bound 成立；没有借用三素数乘积与第四素数的联合渐近。

与 (7) 合并，(14) 的 \(\tfrac34HS_Z^2\) 主项和所有 errors 正确。固定 \(0<\rho\le1/2\)，\(Z=X^\rho\)、\(H=O(T)\) 时，它们均为 \(o(TL^4)\)。这是 scalar mean value 的结论，尚不是 compressed matrix 的 exact main term。

## 4. 原压缩、Jensen 与显式常数

§1、§4 保留
\[
 F=U/\sqrt{2\pi L},\quad F^*F\le1,\quad
 P_Z^{\rm pr}=\frac{2\pi}{a_LL}F^*M_ZF,\quad
 M_Z=-\pi^{-1}\operatorname{Re}Q_Z.
\]
对 \(F^*M_ZF\) 的每个 eigenvector，测度 \(|Fv|^2dt\) 的不足质量放在 0，scalar convexity 给 fourth-power majorant。对 eigenbasis 求和不会遗失有限 frame 的 cross terms。

所有 normalizer 结合为
\[
 \left(\frac{2\pi}{a_LL}\right)^4
 \frac1{\pi^4}\frac1{2\pi L}
 =\frac8{\pi a_L^4L^5},
\]
故 (15) 精确。这里没有使用错误的 operator convexity 前件。

原 infinite-grid identity 给 \(\sum_{\rm finite}|f_k|^2\le a_LL^2\)。先固定 \(\epsilon>0\)，在
\(J_\epsilon=[(1-\epsilon)T,(2+\epsilon)T]\) 使用该 pointwise bound 及 scalar mean value，得到 (16)。从
\[
 \frac8{\pi a_L^3L^3}\,
 \frac3{16}(1+2\epsilon)T(\rho L)^4,\qquad
 N(T,2T)\sim\frac{TL}{2\pi},
\]
严格得到 normalized 系数 \(3\rho^4(1+2\epsilon)\)，没有额外的 factor 2 或 \(a_L\)。

所有实际 centers 满足 \(T\le\alpha_k<2T\)，故 \(J_\epsilon^c\) 距离至少 \(\epsilon T\)。原 C² 尾给 \(D_TT^{-3}\)，而整个实轴保留 \(|Q_Z|\ll\sqrt Z\)。正规化后的尾费是
\(O_\epsilon(Z^2/(T^2L^4))=o(N)\)，包括低 height 与负 height。这里只分割 (15) 的 positive integral，未将任意矩阵四迹拆成两个无 mixed terms 的四迹。

量词为固定 \(\rho,\chi,\psi\) 和固定 \(\epsilon\)，先 \(T\to\infty\)，再 \(\epsilon\downarrow0\)。Fourier 尾常数可依赖固定 \(\epsilon\)，不能免费改成 \(\epsilon_T\)。这里只需 \(D_T\sim N\)，原文中更强的 \(D_T=N+O(L)\) 未被采用。

## 5. sharp proper powers 与非交换 transfer

§5 直接针对 \(p^j\le Z,\ j\ge2\) 的原 cutoff。平方部分有 \(O(\log(2Z))\) 的绝对 mass，\(j\ge3\) 的剩余 mass 收敛；所以整个实轴的 (19) 合法，且压缩的 \(1/L\) 因子给统一 \(O(1)\) operator norm。

proper-power frequencies \(\log(p^j)\) 互异。其 squared coefficient mass 收敛，weighted Hilbert error 为
\[
 O\!\left(\sum_{p^j\le Z,j\ge2}(\log p)^2\right)
 \ll\sqrt Z\log^2(2Z).
\]
该误差在 \(Z\le\sqrt X\) 时统一为 \(o(T)\)。于是 \(J_\epsilon\) 上二矩为 \(O_\epsilon(T)\)，外侧由同一个 absolute bound 和 Fourier 尾支付。squared scalar Jensen 准确给
\[
 \operatorname{Tr}(E_Z^{\rm pp})^2\ll N/L^2,\quad
 \operatorname{Tr}(E_Z^{\rm pp})^4
 \le\|E_Z^{\rm pp}\|_{\rm op}^2\operatorname{Tr}(E_Z^{\rm pp})^2
 \ll N/L^2.
\]
没有从完整 pp 和的取消向任意 subsequence 免费转移。

prime-only 四范数已经先独立付为 \(O(N^{1/4})\)，proper powers 的四范数为 \(O(N^{1/4}/\sqrt L)\)。Minkowski 及非交换 telescoping/Hölder 因而给 (21) 的 \(o(N)\)；甚至可取 \(O(N/\sqrt L)\) 的粗 transfer 费。无需先假设完整 high/low/background response 的四范数有界，故这一 low-channel transfer 不循环。

## 6. 最终结论与未付范围

限定 PASS 的实际结论是
\[
 \limsup_{T\to\infty}
 \frac{a_L^3}{N(T,2T)}
 \operatorname{Tr}P_{\le X^\rho}^4\le3\rho^4,
 \qquad0<\rho\le\tfrac12,
\]
其中 \(\rho\) 和原合法 profile 固定。若 \(a_L\to a_\infty>0\)，可转成 \(3\rho^4/a_\infty^3\)。flat profile 的固定光滑 taper 有 \(a_\infty=1\)，故 \(\rho=1/2\) 给 \(3/16\)。MT 的 \(a_\infty\ne1\)，不能直接套 flat 常数。

这是一侧 upper budget；scalar Jensen 可损失物理路径信息，本文没有证明它是 exact main term。高素数 repeated sector 的独立预算不能与它直接相加得到完整 \(B_4\)。low/high mixed words、four-distinct high words、背景/极点 mixed words、原有限 carrier 的 cross-cell/alias 仍须支付。

本审查没有把新的有限审计当作 mean value、无穷素数或四点相关认证，没有重证 RH/RR 或全 Weil 算术桥；没有新零点比例或新无零边界。
