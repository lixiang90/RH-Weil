# 455 第二独立全文审查：whole proper powers 的原有限 \(S_4\) 预算

2026-10-07。作者：radial_review。全文独立读取 455，逐项核对所有显示公式、
454 的实际背景桥梁及 452 的引用范围；另直接核对 MV 原论文与 AF 原 frame。
只新增本报告，不修改被审稿、冻结稿、脚本、输出、math 或 Git。

**限定 PASS，未发现数学阻断。**455 的
\(\|E_{\rm pp}\|_{S_4}/N^{1/4}=O(L^{-1})\) 是完整 sharp proper-power
channel、原 finite projection 和全高度范围的真实估计。
normalized fourth-root 的 prime-only 等价无需预设完整四矩有界；
fourth 总差的 \(o(1)\) 及 454 的四阶上界仍正确保留 bounded whole-budget
前件。没有付清 genuine-prime 全四矩、distinct/mixed covariance 或新比例。
唯一不阻断的符号澄清已经采纳，最终 binding 与变更验证见 §7。

## 1. 精确绑定与独立输入

当前 read-only HEAD：
5b7effad9126499583a2243e462e16e28b346265。
canonical LF 表示 CRLF 与 lone CR 转成 LF 后的 UTF-8：

| 实读对象 | canonical LF SHA256 | bytes / 行 |
|---|---|---:|
| [455](../../notes/455-whole-proper-power-fourth-norm-and-prime-equivalence.md) | 6bf2025dcc8f56d7b35d9c8b764ac2ff3b911a6e054bf9c496042c7f3e11ce41 | 9135 / 281 |
| [454](../../notes/454-original-background-and-weighted-prime-mixed-traces.md) | 8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7 | 13284 / 425 |
| [452](../../notes/452-subquarter-padding-and-fourth-trace-stability.md) | 9e6071870a7203ce97e5489cf3178ee8681abf36014db790a8b60d8fa4895bbc | 12296 / 364 |
| [新有限脚本](../../scripts/hybrid_proper_power_exact_audit.py) | 2b05fca4d29848965b581bb32220dd90f42f58aeaba765e9365ba01c2a65119e | 3875 / 83 |
| [已有输出](../../output/hybrid-proper-power-exact-audit.json) | af7bc4c541f591fee0eb7b5d56c1315cccd8caddfc544ed418ad846104ce399b | 5617 / 267 |

primary 引用：
[Montgomery–Vaughan, Theorem 2 与 Corollaries 2–3](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
和 [AF v2 §2.2–2.3、Lemma 2.1](https://arxiv.org/html/2608.13637v2#S2)。
使用前者的 weighted local-spacing mean value 与后者的真实 fixed frame、
taper derivative bounds。下文还独立用实轴 Fourier-series Parseval 核准
grid 常数，不将 AF 的更一般 complex-height 展示式当成本稿所需前件。

455(1)–(21) 的连续估计仅依赖固定 \(\chi,\psi\)、Chebyshev/Mertens、
weighted MV、Parseval、scalar Jensen 和有限 Schatten norm；
不使用 math 的 [R] 无零半平面。455 §6 调用 452 时，才须保留其明列的
全高度 \(\theta=\sigma_*\) [R] 与 zero-side/inertia 输入。
本审查不重新认证外部整篇 theorem、Lean kernel 或全 RH/RR。

## 2. 实际 channel 与全部 proper powers

455(2)–(3) 保留同一原 \(X=T/(2\pi), L=\log X, d=\lfloor XL\rfloor\)、
\(\alpha_k=T+2\pi k/L\)、\(a_L\to a>0\)、\(F=\mathcal F M_\phi E\)。
\(E\) 是原 carrier isometry；\(\mathcal F\) 为 unitary Fourier；
\(\|\phi\|_\infty\le1\)，所以 \(\|F\|\le1\)。
两种 scalar multipliers 的准确差就是
\[
 P_{\rm pp}(t)=-\pi^{-1}\Re
 \sum_{\substack{p^j\le X\\j\ge2}}\frac{\log p}{p^{j/2}}e^{ijt\log p}.
 \tag{R1}
\]
因此 \(E_{\rm pp}=C_\Lambda-C_{\rm pr}\) 是 Hermitian finite matrix，
不是一个预先去掉 internal projections 的 bulk symbol。

455(5) 的全部 \(j\ge3\) absolute bound 对任意实 \(t\) 及 sharp cutoff
都一致。它可由几何级数和收敛的
\(\sum_{n\ge2}(\log n)n^{-3/2}\) 给出。
455(6) 中平方素数的 absolute bound 是 \(O(\log X)\)，保留 \(t=0\)
附近 coherent peak。没有以 \(t\sim T\) 的平均估计覆盖低/负高度。

## 3. base products 的 coefficient 与 weighted MV 准入

令 \(c_p=(\log p)/p\)、\(p\le\sqrt X\)。
\(S_2(t)^2\) 中自然频率为
\[
 2\log m,\qquad m=pq\le X.
 \tag{R2}
\]
唯一分解给 distinct primes 的 coefficient \(2c_pc_q\)，重复 prime
给 \(c_p^2\)。故 455(9)–(10) 精确：
\[
 \sum_m|c(m)|^2=2S^2-\sum_pc_p^4,\qquad
 \sum_m m|c(m)|^2=2W^2-\sum_pp^2c_p^4,
 \tag{R3}
\]
其中 \(S=\sum_pc_p^2=O(1)\)，
\(W=\sum_p(\log p)^2/p=O(L^2)\)。
后一估计由 Chebyshev \(\vartheta(y)=O(y)\) partial summation 已足够，
不偷偷调用 PNT 或 prime pair correlation。

对 distinct positive integer bases 的这组频率，有
\[
 \delta_m\ge2\log(1+1/m)\ge\frac2{m+1},
 \qquad \delta_m^{-1}\le\frac{m+1}{2}\le m.
 \tag{R4}
\]
若前一个整数频率存在，其距离更大；稀疏 subset 也只使局部间距增大。
单频率的小 \(X\) 情况可直接积分，无需定义不存在的 nearest neighbour。
这是按实际 base \(m\) 支付的间距，不是把任意 integers \(m^2\le X^2\)
的间距免费改成 \(1/m\)。

对 \(J=[A,B]\) 展开平方，非对角积分准确为
\[
 \frac1i\sum_{m\ne n}\frac{c(m)\overline{c(n)}}
 {2\log m-2\log n}
 \left(e^{i(2\log m-2\log n)B}
      -e^{i(2\log m-2\log n)A}\right).
 \tag{R5}
\]
两个 endpoint 分别调用 weighted MV；每个 endpoint coefficient 的模
都是 \(|c(m)|\)。由 (R3)–(R4)，总误差
\(O(\sum_m m|c(m)|^2)=O(L^4)\)，常数不依赖 interval 的位置。
所以 455(11) 的 \(\int_J|S_2|^4\ll |J|+L^4\) 完整合法；
也可换 \(t'=2t\)，但须同时除以2，这与 (R5) 相容。

对 \(J=[T/2,3T]\)，加入 \(R_3=O(1)\) 后用
\(|z+w|^4\le8(|z|^4+|w|^4)\)，得
\[
 \int_J|Q_{\rm pp}(t)|^4dt\ll T+L^4=O(T).
 \tag{R6}
\]
这里只要 absolute upper bound；没有将 complex \(Q\) 与 \(\Re Q\)
的未知 fourth 主常数混同。至此未调用待证的 full prime fourth。

## 4. scalar spectral Jensen 与 unitary grid 常数

对 \(E_{\rm pp}\) 的单位 eigenvector \(u\)，
\(\lambda=(2\pi/(a_LL))\int P_{\rm pp}|Fu|^2\)；
\(\int|Fu|^2\le1\)。在 scalar value0 处补足 probability mass，
对 \(x\mapsto x^4\) 使用普通 scalar Jensen，得到
\[
 |\lambda|^4\le
 \left(\frac{2\pi}{a_LL}\right)^4\int |P_{\rm pp}|^4|Fu|^2.
 \tag{R7}
\]
这不是 \(x^4\) operator convex 的断言；没有给它不成立的 operator
Jensen 用法。\(P_{\rm pp}\) 是真实有界 real multiplier，scalar 积分合法。
求完整 finite eigenbasis 的和，只使用 trace basis-invariance：
\[
 \Tr E_{\rm pp}^4\le
 \frac{16}{a_L^4L^5}\int_{\mathbf R}
 \sum_{0\le k<d}|f_k(t)|^2|\Re Q_{\rm pp}(t)|^4dt.
 \tag{R8}
\]
因 \(P_{\rm pp}=-\pi^{-1}\Re Q_{\rm pp}\)，四次 prefactor 中
\((2\pi)^4/\pi^4=16\)；又 \(Fe_k=L^{-1/2}f_k\) 给剩余 \(L^{-1}\)。
455(13) 的常数16正确。

独立核准 455(14)：对固定实 \(t\)，在长度 \(L\) 的原物理 interval 上，
carrier Fourier basis
\(L^{-1/2}e^{i(T+2\pi k/L)u}\)、\(k\in\mathbf Z\) 完备正交。
对 \(g_t(u)=\phi(u)e^{itu}\) 用 Parseval，
\[
 \sum_{k\in\mathbf Z}\frac{2\pi}{L}|f_k(t)|^2
 =\|\phi\|_2^2=a_LL.
 \tag{R9}
\]
所以 \(\sum_{k\in\mathbf Z}|f_k(t)|^2=a_LL^2/(2\pi)\)。
原 finite partial sum 的点态上界可由非负性使用这个恒等式；
它不替换任何 finite matrix product 的 internal projection。
unitary 与 AF 的未归一化 Fourier 约定在这里相差 \(\sqrt{2\pi}\)，
455(13)–(14) 的两处换算一致。

将 (R6) 与 (R9) 放入 (R8)，central 部分为
\(O(T/L^3)=O(d/L^4)\)。\(a_L\) 最终离零，其费用只依赖固定 profile。

## 5. 全高度 exterior 与归一化 \(S_4\) 结论

所有原 \(\alpha_k\in[T,2T]\)，故 \(J^c\) 上
\(|t-\alpha_k|\ge T/2\)。原 fixed C² taper 的
\(\|\phi''\|_1=O(1)\) 给这里的 uniform large-frequency tail
\(|f_k(t)|\ll |t-\alpha_k|^{-2}\)。注意只在该 large-distance 区域使用；
没有错误声称 Fourier peak 在距离0也是 \(O(1)\)。

因此
\[
 \sum_{k<d}\int_{J^c}|f_k(t)|^2dt\ll dT^{-3}.
 \tag{R10}
\]
外侧仍用全部高度上的 \(|Q_{\rm pp}|\ll L\)，不是删除
principal-height coherent peak。由 (R8)，费用
\[
 O\!\left(\frac{d}{LT^3}\right)
 =o(d/L^4).
 \tag{R11}
\]
这包括 negative/low height 以及 \(J\) 的两端；sharp powers 没有因支撑
或高度被漏掉。由于 \(d\sim N(T,2T)\)，合并即为
\[
 \Tr E_{\rm pp}^4=O(N/L^4),\qquad
 \|E_{\rm pp}\|_{S_4}/N^{1/4}=O(L^{-1}).
 \tag{R12}
\]
仅用 \(d\sim N\)，未依赖 \(d=N+O(L)\) 的过强余项。
这是 455 新证明的有效范围：原完整 proper-power response，而非
453 的 low-prefix 估计。

## 6. 四次根等价与 454 条件桥梁

两种原 channel Hermitian，故
\(\Tr C^4=\|C\|_{S_4}^4\)。Schatten reverse triangle 给
455(19)，其 \(\epsilon_T=O(1/L)\) 在 \(T\to\infty\) 趋零。
这个不等式无需假定任一 side 的 whole fourth 有界。
任意同一个 Hermitian \(A_T\) 在两边相加仍只差 \(E_{\rm pp}\)，
所以 455(20) 同样成立；\(A_T\) 可以随 \(T\) 变化或有大 norm。

非负 fourth roots 相差 \(o(1)\)，所以 limsup 等价与 extended value
\(+\infty\) 都合法；boundedness 等价也合法。
将 fourth roots 变回 fourth 时，
\[
 |F_{\Lambda,T}-F_{{\rm pr},T}|
 \le4\epsilon_T(F_{{\rm pr},T}^{1/4}+\epsilon_T)^3
 \tag{R13}
\]
是普通 mean-value inequality，未假定未知 \(F_{\rm pr}\) bounded。
只有补充有限 whole budget 后才由 (R13) 推得 normalized total
差 \(O(1/L)=o(1)\)。455 没有把不同 proper-power mixed words 各自
无条件登记成 \(o(N)\)，也没有将 fourth-root 小误差误写成总差小误差。

若未来 \(\limsup F_{\rm pr}\le F<\infty\)，则
\(\limsup F_\Lambda\le F\)，可在 454(28)–(30) 使用这个实际 full \(C_\Lambda\)。
454 已付的 \(\Tr A^2C_\Lambda^2/N\to Z_\psi\) 与
HS Cauchy 保留实际 \(A\)，给
\(|\Tr AC_\Lambda^3/N|\le\sqrt{(Z_\psi+o(1))F_{\Lambda,T}}\)。
因此 455(22) 的
\(F+4\sqrt{Z_\psi F}+6Z_\psi-J_\psi+V_\psi\) 正确，
且完全保留 conditional \(F\)；没有用 \(A=A_0+O_{\rm op}(1/L)\)
免费乘未知 \(C_\Lambda^3\)。

455 对 452 的引用也准确：同一个 centered \(H\) 的完整 upper budget
可按其已付 \(H/G_P\) stability 与明列 [R] 转移。
452 不提供缺失的 genuine-prime fourth 常数，455 也没有声称它提供。
四 distinct、distinct22、13/31 和实际 \(AC^3\) covariance 仍开放；
repeated22 的 \(13/120\) 不是完整 \(F\)。无新比例结论。

## 7. 最小措辞澄清与有限代码范围

唯一建议已采纳：455 line143 的“对任一 \(C_{\rm pp}\) 的单位 eigenvector”
已改为“对任一 \(E_{\rm pp}\) 的单位 eigenvector”。此前只定义 \(E_{\rm pp}\)
为该差矩阵，后续谱和也一直是 \(\Tr E_{\rm pp}^4\)。
这是 P3 未定义别名，数学论证可直接按 \(E_{\rm pp}\) 读取；
不是证明阻断，也不需要改 theorem 或任何合同。最终 455 另外只更新
line3 的审查状态；将这两处换回原文字，可精确恢复初审
477adbb9e7bdf79153ef664f8b4fcab11a535c7e51ae02eddcbb448df1dae9c2
的 canonical LF SHA，数学正文没有其他变更。

新脚本/output 全文只读核验通过，未执行或覆写：
十个 Fraction weighted-prime-product 模型通过 ordered pairs
直接生成 coefficients 再比较 (R3)，并非从 formula 伪造系数；
48 个 scalar checks 与 nonnegative residual
\(6b^2\epsilon^2+8b\epsilon^3+3\epsilon^4\) 也相符。
根节点已将新脚本重跑到最终 455；本审查只读核验更新后的 JSON，
其 note/script SHA 与本轮最终磁盘一致。十个 coefficient 模型和
48 个 scalar checks 的范围不变；本代理未运行或覆写脚本、输出。
它只辅助有限系数和 scalar algebra，不验证 MV、Jensen、无限 coefficient
bound、全高度尾或 Schatten theorem。本报告的连续准入由上文独立核读。

验收状态：455 当前绑定稿 **限定 PASS，无数学阻断**。
本轮付清的是 whole proper-power \(S_4\)-small 与 same-frame fourth-root
归约；full genuine-prime budget 与最终比例继续保持待证。
