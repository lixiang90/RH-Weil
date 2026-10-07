# 455：完整 proper powers 的原有限四范数与 prime-only 等价预算

2026-10-07。推导完成，全文独审通过；审查范围见本轮记录。没有新的边界或零点比例。
本稿支付原 sharp Λ channel 的**全部** proper powers，而非只处理
453 的 low prefix。结论不预设完整 prime fourth 有界：

\[
 \frac{\|E_{\rm pp}\|_{S_4}}{N^{1/4}}\ll L^{-1},
 \qquad \operatorname{Tr}E_{\rm pp}^4\ll N/L^4 .
 \tag{1}
\]

因此原 Λ channel 和原 prime-only channel 的 normalized fourth-root
差趋零；两者的有限四阶预算是等价的待证输入。若其中之一有界，
全部 proper-power mixed words 的**总差额**才自动为 o(N)。
不宣称各个 mixed word 单独为 o(N)。

## 1. 原对象：不改变 finite frame 或高度

沿用 [454](454-original-background-and-weighted-prime-mixed-traces.md)：
X=T/(2π)、L=logX、d=⌊XL⌋、α_k=T+2πk/L，
N=N(T,2T)∼d。原 C² taper φ、fixed even ψ 和 a_L=||φ||₂²/L→a>0。
E e_k=L⁻¹/²1_Ie^(iα_ku)，F=𝓕MφE，𝓕 为 unitary Fourier。
F 是 contraction，因为 ||φ||∞≤1。

\[
 C_\Lambda=\frac{2\pi}{a_LL}F^*M_{P_\Lambda}F,\qquad
 C_{\rm pr}=\frac{2\pi}{a_LL}F^*M_{P_{\rm pr}}F,\qquad
 E_{\rm pp}=C_\Lambda-C_{\rm pr}.
 \tag{2}
\]

这里

\[
 P_{\rm pp}(t)=-\pi^{-1}\operatorname{Re}Q_{\rm pp}(t),\quad
 Q_{\rm pp}(t)=\sum_{\substack{p^j\le X\\j\ge2}}
                 \frac{\log p}{p^{j/2}}e^{ijt\log p}.
 \tag{3}
\]

原矩阵、carrier、projection、归一化和 sharp cutoff 完全保留；
只作同一个实际 channel 的准确线性分解。
经典输入为 [AF v2 §2 的原 frame、Poisson–Gabor 与 weighted Hilbert](https://arxiv.org/html/2608.13637v2#S2)，
及 Chebyshev/Mertens。没有调用 [R] 的无零半平面。
所有以下 O 常数只依赖固定 χ、ψ。

453 用 quadratic mean 与 Oop(1) 得低 prefix 的弱 fourth bound；
本稿的新步骤是平方素数项的第四矩按其**base prime products**分组。
不能把 perfect-square subset 的局部间距免费换成所有 n≤X² 的间距。

## 2. 三次以上的幂：全高度 bounded remainder

准确分成 Q_pp=S₂+R₃，令

\[
 S_2(t)=\sum_{p\le\sqrt X}\frac{\log p}{p}e^{2it\log p}.
 \tag{4}
\]

即使 sharp cutoff 随 X 改变，仍有全高度一致绝对界

\[
 |R_3(t)|\le\sum_p\sum_{j\ge3}\frac{\log p}{p^{j/2}}
 \le\frac1{1-2^{-1/2}}\sum_{n\ge2}\frac{\log n}{n^{3/2}}<\infty.
 \tag{5}
\]

没有要求不同 powers 的相消。Mertens/Chebyshev partial summation 给

\[
 |S_2(t)|\le\sum_{p\le\sqrt X}\frac{\log p}{p}\ll L,\qquad
 |Q_{\rm pp}(t)|\ll L\quad\text{对全部实 }t.
 \tag{6}
\]

这保留 t≈0 的 coherent peak，它不会被 t∼T 的估计替代。

## 3. 平方项的四矩：长度 X 而非任意整数频率 X²

记 c_p=(logp)/p、Y=√X。
S₂(t)²=Σ_(m≤X) c(m)e^(2itlogm)，非零 m=pq，

\[
 c(pq)=
 \begin{cases}2c_pc_q,&p\ne q,\ p,q\le Y,\\
 c_p^2,&p=q\le Y.\end{cases}
 \tag{7}
\]

唯一分解保证没有其他 prime-product collision。记

\[
 S=\sum_{p\le Y}c_p^2=O(1),\qquad
 W=\sum_{p\le Y}p\,c_p^2
   =\sum_{p\le Y}\frac{(\log p)^2}{p}\ll L^2.
 \tag{8}
\]

于是两项 coefficient identities 准确为

\[
 \sum_m|c(m)|^2=2S^2-\sum_pc_p^4=O(1),
 \tag{9}
\]
\[
 \sum_m m|c(m)|^2=2W^2-\sum_pp^2c_p^4\ll L^4.
 \tag{10}
\]

若将频率写成 log(m²)，它仍是 2logm；其中非零 integers m≤X。
两频率的局部间距
δ_m=min_(n≠m)|2logm−2logn|，按整数 spacing 有 δ_m⁻¹≤m。
使用 [Montgomery–Vaughan Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
并展开时间积分，保留其两个 endpoint phases，对任意 interval J 有

\[
 \int_J|S_2(t)|^4dt
 =|J|\sum_m|c(m)|^2
    +O\left(\sum_m m|c(m)|^2\right)
 \ll |J|+L^4.
 \tag{11}
\]

这里可直接对频率 2logm 用 weighted Hilbert，
也可在 standard logm mean-value formula 中换变量 t'=2t。
两个方法的 endpoint、间距和 Jacobian 均相容。
不是对任意 n≤X² 的 Dirichlet polynomial 声称 length X。

取固定 J=[T/2,3T]，(5) 与 |x+y|⁴≤8|x|⁴+8|y|⁴ 给

\[
 \int_J|Q_{\rm pp}(t)|^4dt\ll T+L^4=O(T).
 \tag{12}
\]

interval length 为 O(T)；L⁴=o(T)。未将 real Q 的四矩主常数当成
complex Q 的主常数，此处只用合法的 absolute upper bound。

## 4. 原 finite compression 的 scalar Jensen 与全高度尾

设 f_k(t)=𝓕φ(t−α_k)，所以 Fe_k=L⁻¹/²f_k。
对任一 E_pp 的单位 eigenvector u，measure |Fu(t)|²dt 总质量≤1；
在0加缺少质量后对实 multiplier 使用 x↦x⁴ 的 scalar Jensen。
对完整 finite eigenbasis求和准确给

\[
 \operatorname{Tr}E_{\rm pp}^4
 \le\left(\frac{2\pi}{a_LL}\right)^4
       \operatorname{Tr}\big(F^*M_{|P_{\rm pp}|^4}F\big)
 =\frac{16}{a_L^4L^5}\int_{\mathbb R}
       \sum_{0\le k<d}|f_k(t)|^2
                  |\operatorname{Re}Q_{\rm pp}(t)|^4dt .
 \tag{13}
\]

这是单侧 spectral inequality，不是 operator-convex x⁴ 定理。
原 unitary Fourier convention使(13)的 prefactor 为16；
若采用AF的未归一化 Fourier，f_k及prefactor同时按2π换算。
不会把不同 convention 的常数混用。

原 infinite-grid identity只用于给 finite partial sum的点态上界：

\[
 \sum_{0\le k<d}|f_k(t)|^2\le
 \sum_{k\in\mathbb Z}|f_k(t)|^2
 =\frac{a_LL^2}{2\pi}\ll a_LL^2 .
 \tag{14}
\]

原 finite k、carrier 与所有 height仍在(13)；没有把第四次矩阵乘积的
internal P 删除。J上的正 majorant费用由(12)–(14)为

\[
 O(T/L^3)=O(d/L^4).
 \tag{15}
\]

J外每个 α_k∈[T,2T] 到t的距离至少 T/2。
原 C² tail |f_k(t)|≪(1+|t−α_k|)⁻² 给

\[
 \sum_k\int_{J^c}|f_k(t)|^2dt\ll dT^{-3}.
 \tag{16}
\]

使用全高度(6)，(13)的这个 exterior费用至多

\[
 O(L^{-5}\,L^4\,dT^{-3})=O(d/(LT^3))
 =o(d/L^4).
 \tag{17}
\]

因此(1)成立。低/负 height、principal-height coherent pp peak、
所有 sharp powers和全部 finite projections均在这个支付中。
scalar Jensen 的 single positive integral分区没有丢矩阵 cross terms。

## 5. 全 fourth-root 等价：无需假设另一侧有界

令

\[
 F_{\Lambda,T}=\operatorname{Tr}C_\Lambda^4/N,\qquad
 F_{{\rm pr},T}=\operatorname{Tr}C_{\rm pr}^4/N,\qquad
 \epsilon_T=\|E_{\rm pp}\|_{S_4}/N^{1/4}\ll1/L.
 \tag{18}
\]

两个矩阵 Hermitian。Schatten Minkowski及reverse triangle准确给

\[
 \boxed{|F_{\Lambda,T}^{1/4}-F_{{\rm pr},T}^{1/4}|
          \le\epsilon_T.}
 \tag{19}
\]

这一不等式对每个充分大T成立，完全不需要 full F 有界。
进一步对任意 Hermitian same-frame background A_T，有

\[
 \left|\left(\frac{\operatorname{Tr}(A_T+C_\Lambda)^4}{N}\right)^{1/4}
 -\left(\frac{\operatorname{Tr}(A_T+C_{\rm pr})^4}{N}\right)^{1/4}\right|
 \le\epsilon_T.
 \tag{20}
\]

A_T可取454的原Γ/pole减I，甚至可随T有大norm；
它在两边保持**完全相同**，不需要提前替换为静态背景。
因此完整中心四矩的 boundedness/limsup也可由同一prime-only问题转移。

等价结论：

- limsup F_Λ<∞ 当且仅当 limsup F_pr<∞；
- 二者 limsup 相等，包括扩展实数+∞；有限时liminf同样相等；
- 任一共同背景的两个fourth sums有相同性质。

这没有独立证明其中任何 full finite upper bound。对实际大小有

\[
 |F_{\Lambda,T}-F_{{\rm pr},T}|
 \le4\epsilon_T(F_{{\rm pr},T}^{1/4}+\epsilon_T)^3.
 \tag{21}
\]

所以只有右方 whole budget有界时，fourth total差才是O(1/L)=o(1)。
没有从(19)断言未知增长的F两边总差无条件为o(1)。

## 6. 与背景、截断和比例的准确桥梁

若未来对原完整 prime-only matrix证明 limsup F_pr≤F<∞，
(19)立即支付 limsup F_Λ≤F，454的已证背景量和Cauchy给

\[
 \limsup\frac{\operatorname{Tr}(H-I)^4}{N}
 \le F+4\sqrt{Z_\psi F}+6Z_\psi-J_\psi+V_\psi.
 \tag{22}
\]

原 H−I=A+C_Λ。flat bulk的V=Z=J=0，这条条件桥梁主费用为F。
若直接研究 A+C_pr 的whole centered fourth，亦可直接使用(20)；
prime-only response本身并未被冒认为原零点Gram。

结合 [452](452-subquarter-padding-and-fourth-trace-stability.md) 的同矩阵
H/G_P稳定性后，可在已付的zero-side inertia/proportion链中使用同一
完整常数。452仍有其明列[R]适用范围，(1)–(21)本身不需零自由输入。

新增实际研究进展是：proper powers已具有全范围S₄-small估计，
并使整个whole-budget问题可等价归约到genuine-prime channel；
不再需要先逐一支付所有proper-power mixed words。
但 genuine-prime的high四distinct、22 distinct、13/31以及实际
background三prime covariance仍未付。13/120只是重复22子族，
旧low Jensen upper和high repeated upper不能直接拼成F。
当前没有新比例或边界，不触发新的边界论文。

有限显示系数核验见
[标准库精确脚本](../scripts/hybrid_proper_power_exact_audit.py)与
[输出](../output/hybrid-proper-power-exact-audit.json)：十个 weighted
prime-product 模型及四次根传递的48个scalar checks。
它们不认证MV、spectral Jensen、全height尾或Schatten定理；
这些连续估计必须由独立全文审查核读。
