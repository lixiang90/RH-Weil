# 437 双素数周期相位方程：小分母、光滑性与准确截止式

2026-10-11。独立核读437及历史复盘§5。本报告只支付固定 \(L=\log2,M=\log5\) 的周期相位方程；它也可作为任意光滑 \(M\)-周期符号的分析引理。源有限词的代数闭合、辅助分割独立性、无穷位、相对闭链和正性没有由本引理解决。

## 1. 确认实际输入是光滑周期函数

437的原合法分割 \(c,d\) 是实光滑紧支函数，\(f=cd\)。函数

\[
\alpha(x)=\sum_{j\in\mathbb Z}f(x+jM)^2,
\qquad\gamma_1=1-\alpha
\]

是光滑 \(M\)-周期函数：和在每个紧区间局部有限，所以逐阶微分合法，周期性由标签重排得到。437的 \(h=k\in C_c^\infty(\mathbb R)\)，所以

\[
C(x)=\int h(s)^2\gamma_1(x-s)\,ds,
\quad P(\theta)=\int c(t)^2C(t+\theta)\,dt
\]

均属 \(C^\infty(\mathbb R/M\mathbb Z)\)。逐阶有

\[
\|P^{(j)}\|_\infty
\le \|c^2\|_1\|h^2\|_1\|\gamma_1^{(j)}\|_\infty.
\]

由原平方分割 \(\sum_a c(t-aL)^2=1\)，在 \([0,L]\) 积分、重排局部有限非负和，得到 \(\int c^2=L\)。于是
\(\overline P=L\overline C\)，其中横线一律表示 \(M^{-1}\int_0^M\)。这些是实际源计算，未假设任意源词都先有同一周期符号。

## 2. 外部定理核对与两种 Λ 不混用

直接核读的一手研究论文是 Yann Bugeaud、Maurice Mignotte、Samir Siksek，*Classical and modular approaches to exponential Diophantine equations I. Fibonacci and Lucas perfect powers*，Annals of Mathematics 163 (2006), 969–1018。其[原刊PDF](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p05.pdf)§9.1、Theorem 9.4，pp.988–989，固定的是乘积形式

\[
\Gamma=\alpha_1^{b_1}\cdots\alpha_t^{b_t}-1\ne0,
\]

而非加法形式。在正实代数数、实数域 \(K\) 次数 \(D\)、整数 \(b_i\)、\(B\ge\max|b_i|\)、
\(A_i\ge\max\{Dh(\alpha_i),|\log\alpha_i|,0.16\}\) 下，其实数域结论是

\[
\log|\Gamma|>
-1.4\,30^{t+3}t^{9/2}D^2(1+\log D)
(1+\log B)A_1\cdots A_t.                       \tag{A}
\]

原文明确把该结论由 E. M. Matveev (2000), Corollary 2.3 推出。Matveev原论文书目与原刊入口为[Izv. Math.64:6 (2000), 1217–1269](https://www.mathnet.ru/eng/im314)，DOI `10.1070/IM2000v064n06ABEH000314`。2000英文PDF下载本次多次超时；不能声称已经全文核读它。(A)的直接文本与假设已在上述Annals原刊研究论文核读，下面明确支付从乘积形式到加法形式的转换。

另已实际核读[Matveev 1998原英文PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=190&what=fullteng)，*An explicit lower bound for a homogeneous rational linear form in logarithms of algebraic numbers*, Izv. Math.62:4 (1998), 723–772。它提供直接的加法形式备份：§1 (1.5)将strong independence定义为
\([K(\sqrt{\alpha_1},\ldots,\sqrt{\alpha_t}):K]=2^t\)；§2 Theorem 2.2、(2.16)，pp.728–729，给

\[
\log|\Lambda|>-112\,2^tC_2C'_0D^2\omega\log(2eB).
\]

这里 \(\Lambda=\sum b_i\log\alpha_i\)，\(C_2,C'_0,\omega\) 按该文(2.4)–(2.5),(2.13)–(2.15)固定；它们在固定 \(2,5\) 后不依赖 \(b_i\)。\(K=\mathbb Q,\alpha_1=2,\alpha_2=5\) 满足strong independence，因为 \([\mathbb Q(\sqrt2,\sqrt5):\mathbb Q]=4\)。实对数的实秩 \(\rho=1\)，\(D=1\)，取该定理的 \(\vartheta=E=1,C_3=2\) 和 \(A_1=L,A_2=M\) 可用；其 \(1/C_1<L\)，并且 \(C'_0>0\)。最近整数系数的修改后 \(B=\max\{|b_1|L/M,|b_2|\}\le |b_1|\)。因此该原刊定理也独立确认需要的是固定有限次数的多项式下界。以下采用(A)的较简明明确常数，不以1998原文摘要替代假设核验。

## 3. 固定素数对的小分母下界

置

\[
\kappa=1.4\,30^5\,2^{9/2}LM
\quad(\kappa\approx858754405.9967992),
\qquad c_*=\frac{4e^{-\kappa}}{M\sqrt5}>0.
\]

对整数 \(N\ge2\)，令 \(m\) 为 \(NL/M\) 的最近整数。因 \(1/3<L/M<1/2\)，有 \(1\le m\le N\)，且

\[
\xi=NL-mM\ne0,\quad |\xi|\le M/2,
\quad\Gamma=2^N5^{-m}-1=e^\xi-1\ne0.
\]

非零性由不同素数的唯一分解支付。应用(A)时逐项参数是
\(t=2,K=\mathbb Q,D=1,\alpha_1=2,\alpha_2=5,
b_1=N,b_2=-m,B=N,A_1=L,A_2=M\)；绝对对数高度为 \(h(2)=L,h(5)=M\)。所以

\[
|e^\xi-1|>e^{-\kappa}N^{-\kappa}.
\]

这一步未把(A)的 \(\Gamma\) 偷换为 \(\xi\)。利用实均值定理

\[
|e^\xi-1|\le e^{|\xi|}|\xi|
\le\sqrt5\,|\xi|
\]

才得到

\[
|NL-mM|>\frac{e^{-\kappa}}{\sqrt5}N^{-\kappa}.       \tag{B}
\]

设 \(z_n=e^{2\pi i nL/M}\)。令 \(\delta=\operatorname{dist}(NL/M,\mathbb Z)=|\xi|/M\le1/2\)，由 \(\sin(\pi\delta)\ge2\delta\)，

\[
|z_N-1|=2\sin(\pi\delta)\ge4\delta
>c_*N^{-\kappa}.                                    \tag{C}
\]

\(N=1\) 可直接支付：\(L/M\in(1/3,1/2)\) 给 \(|z_1-1|>\sqrt3\)，而 \(c_*<1\)。负 \(n\) 用共轭。因此(C)对所有 \(n\ne0\) 成立。无需优化巨大常数；所需是固定有限 \(\kappa\)，不是只用 \(L/M\) 无理或整数差所得的指数弱界。

## 4. 相位方程的无条件光滑解与连续性

**定理。** 对任意 \(P\in C^\infty(\mathbb R/M\mathbb Z)\)，存在唯一零Haar均值的 \(G\in C^\infty(\mathbb R/M\mathbb Z)\) 满足

\[
G(\theta+L)-G(\theta)=P(\theta+L)-\overline P.         \tag{D}
\]

Fourier系数约定为
\(\widehat P(n)=M^{-1}\int_0^M P(\theta)e^{-2\pi in\theta/M}\,d\theta\)。准确解为

\[
\widehat G(0)=0,
\qquad \widehat G(n)=\frac{z_n}{z_n-1}\widehat P(n)
\quad(n\ne0).                                       \tag{E}
\]

由(C)，乘子至多 \(c_*^{-1}|n|^\kappa\)；光滑函数Fourier系数快速下降，所以(E)及其任意阶微分绝对一致收敛。逐系数得到(D)。若两解不同，其差的非零Fourier系数被 \(z_n-1\ne0\) 全部消掉；零均值再消常数。这也证明零均值分布解唯一。实际437的实 \(P\) 给实 \(G\)，因为负频系数及乘子分别是正频的共轭。

定义 \(\|F\|_{H^s_n}^2=\sum_n(1+n^2)^s|\widehat F(n)|^2\)。对任意实 \(s\)，

\[
\|G\|_{H^s_n}\le c_*^{-1}
\|P-\overline P\|_{H^{s+\kappa}_n}.                  \tag{F}
\]

通常使用物理频率 \(2\pi n/M\) 的Sobolev范数，只需改变依赖 \(M,s\) 的固定等价常数。也可统一取整数损失 \(N_0=858754406\)。这个估计很粗，却真实给出 \(C^\infty\to C^\infty\) 连续线性算子。它没有证明 \(C^r\to C^r\) 连续；有限正则性输入需要承担相应损失。直接用Fourier绝对和时，整数 \(J>r+\kappa+1\) 已足够控制 \(\|G\|_{C^r}\) 于 \(\|P\|_{C^J}\)。

该算子与圆周平移、逐阶微分、复共轭相容；加常数不改变 \(G\)。这些自然性由唯一性或(E)严格得到，尚不能升级为辅助分割变化下的算术自然性。

## 5. 保留几何尾后的准确物理迹

437固定 \(r_0=1/2\)，尾函数是

\[
H(\theta)=(1-r_0)\sum_{d\ge1}r_0^{d-1}P(\theta+dL).
\]

每阶微分一致收敛，故 \(H\in C^\infty\)，并有
\(\|H^{(j)}\|_\infty\le\|P^{(j)}\|_\infty\)、\(\overline H=\overline P\)。其非零频乘子是 \((1-r_0)z_n/(1-r_0z_n)\)，分母在单位圆一致离零。这不是可以自由丢弃的尾。

对任意 \(K\ge0\)，(D)逐步相加给**准确等式**

\[
T_K=K\overline P+G(KL)-G(0)+H(KL).                  \tag{G}
\]

不需要取某条好子列，也没有 \(o(1)\)。因此有限球读出可保留由 \(P\) 决定的完整相位 \(R=G+H\)：

\[
T_K-K\overline P-R(KL)=-G(0).                       \tag{H}
\]

对原实际词 \(Y=A(h)uA(k)=VBV^*+S, S\in\mathcal S_1\)，两个独立截止的原准确迹为

\[
\operatorname{Tr}(P_{K,K_q}YP_{K,K_q})
=K L\overline C+(K_q+1)M\overline C
+R(KL)-G(0)+\operatorname{Tr}(P_{K,K_q}SP_{K,K_q}).
\]

所以减去准确体积 \(K L\overline C+(K_q+1)M\overline C\) 与实际相位 \(R(KL)\) 后，共尾极限为 \(-G(0)+\operatorname{Tr}S\)。如果体积约定改为 \((KL+K_qM)\overline C\)，常数相应为 \(M\overline C-G(0)+\operatorname{Tr}S\)；该常数是截止约定差，不能被解释成规范Weil权。

由此仅得到了在指定来源、分割、截止规则下的相位读出。437原“任意线性扣除后无有限部”反例仍然成立，因为(H)新保留了非恒定相位函数。

## 6. 可以消费的结论与不能消费的结论

可以消费：对固定 \((\log2,\log5)\) 和任意实际已经识别出的光滑 \(M\)-周期符号，(C)–(F)给不依赖RH的规范零均值相位解；对437原有限词，(G)–(H)和包含trace-class误差的双截止式成立。无需新公理，仅消费既有超越数论定理。

不能消费：该相位算子不是乘法同态。以 \(P=e^{2\pi i\theta/M}\) 为例，令 \(a_n=z_n/(z_n-1)\)，则 \(a_2\ne a_1^2\)（等号会迫使 \(z_1=1\)）。因此不能凭单个周期符号解就宣称已经得到源代数乘法或循环迹；还必须证明实际符号映射及相位余项如何在源乘积中组合。辅助平方分割变化也未必只使 \(P\) 平移，本引理未证明分割独立。更没有证明无穷位桥、403非局部配对、主商根空间条件、算术正性、RR或RH。

下一项需要支付的是实际源有限词的符号/相位运算，而非继续改善这里的巨大Diophantine常数。
