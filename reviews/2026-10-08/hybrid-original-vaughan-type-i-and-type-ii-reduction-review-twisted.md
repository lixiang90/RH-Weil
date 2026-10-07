# 原 Vaughan Type I 与完整 Type II 归约：独立全文审查

2026-10-08。审查人：twisted_research。结论：**限定 PASS**。

完整读取作者源全部 324 行，并独立核对真实 sharp 两端、原正高度、系数恒等式、二阶导数、二矩以及新增固定 cut tradeoff。核准的结果是较低长度块和高段 Type I 的 \(X^{2/3+\varepsilon}\) 四矩费用，以及包含全部实际 Möbius-divisor 系数的 \(C_4\) norm coupling；**未证明 whole \(2/3\) 上界、有限四阶常数、新比例或无零边界。**

## 1. 最终来源绑定

canonical LF 规则为 UTF-8 解码后仅将 CRLF、lone CR 改为 LF；不 trim，不改变 EOF。

| 完整读取的对象 | canonical LF SHA256 |
|---|---|
| [被审作者源](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 |
| [原 scalar/proper-power 准入](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [已提交 476](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |

被审最终作者源为 12,260 canonical UTF-8 bytes、324 行。最初 297 行版本之外，最终版仅增加 §6.1 的固定 \(a\) tradeoff；此增项已经逐式重算，本审查绑定最终版本。作者源中的四个本地 Markdown 链接均实际存在。

外部原始来源也实际读取：

- [Montgomery–Vaughan 作者书 Volume II](https://personal.science.psu.edu/rcv4/Vol2/Vol2.pdf)，Theorem 16.7（PDF 第 18 页、印刷第 8 页）及 (17.4)–(17.7)。
- [Guth–Maynard 原论文 v2](https://arxiv.org/html/2405.20552v2)，Theorem 1.1 及其后的改善范围说明。
- [Heap 原论文摘要](https://arxiv.org/abs/2201.02108)，确认其 RH 和受限制的 transform-weight 前件。

本稿的指数付款不使用 [Rθ] 或零密度输入；476 只用于比较目前 whole 上界，既有 proper-power 范数用于返回 genuine primes。

## 2. 原对象与二矩：没有隐藏的 \(X^\varepsilon\) 输入

原对象仍是
\[
 X=T/(2\pi),\quad J_T=[T/4,4T],\qquad
 P_H(t)=\frac1{a_\ell\ell}
 \sum_{\sqrt X<p\le X}\frac{\log p}{\sqrt p}p^{it},
 \quad a_\ell\ge c_\phi>0.
\]
没有将正高度移到零附近，或将长度 \(X\) 的多项式换成长度 \(X^2\) 的免费均值。

作者式 (2) 可直接重证：对 \(m\ne n\)，真实时间积分至多
\(2/|\log(n/m)|\)。由
\[
 |\log(n/m)|\ge |n-m|/Z
\]
和 \(2|\alpha_m\alpha_n|\le|\alpha_m|^2+|\alpha_n|^2\)，每个 row 的差分 harmonic sum 付出 \(O(Z\log(2Z))\)，故
\[
 T^{-1}\int_J\Big|\sum_{n\le Z}\alpha_n n^{it}\Big|^2dt
 \ll\left(1+\frac{Z\log(2Z)}T\right)\sum_{n\le Z}|\alpha_n|^2.
\]
这适用于任意原长为 \(O(T)\) 的区间；不要求 starting height 为零。

固定 divisor 阶数和日志次方后，\(|v(n)|\ll_\delta n^\delta\) 给
\[
 \sum_{A<n\le Z}\frac{|v(n)|^2}{n}
 \ll_\delta Z^{2\delta}\log(2Z).
\]
因此下面所有 \(X^\varepsilon\) 均由明确的固定 divisor 损失与有限日志供应。先固定最终 \(\varepsilon\)，再选足够小的 \(\delta\)，随后令 \(T\to\infty\)，量词顺序合法。

## 3. 较低长度块：平方后的真实长度已付

\(Y=X^{5/6}\) 的低段仍包含原 lower cutoff \(\sqrt X<n\le Y\)。平方系数为
\[
 c_Y(n)=\sum_{\substack{ab=n\\\sqrt X<a,b\le Y}}\Lambda(a)\Lambda(b),
 \qquad |c_Y(n)|\le\tau(n)(\log Y)^2.
\]
实际平方长度为 \(Y^2=X^{5/3}\)，而非 \(Y\)。上述二矩的费用因此是
\[
 1+Y^2/T\ll X^{2/3},
\]
连同系数能量和日志，得到作者式 (6)。这里没有遗漏 lower mask，也没有把无限 \(\Lambda*\Lambda\) 当成实际系数。

## 4. 完整 Vaughan 系数与大素数抵消

独立展开作者式 (9)：
\[
 D_\zeta=F-\zeta FG-\zeta'G+(D_\zeta-F)(1-\zeta G),
 \qquad D_\zeta=-\zeta'/\zeta .
\]
利用 \(\zeta D_\zeta=-\zeta'\)，右侧准确化回 \(D_\zeta\)。又
\[
\operatorname{Coeff}_{k^{-s}}(1-\zeta G)=
 \begin{cases}0,&k\le V,\\-b_V(k),&k>V,\end{cases}
 \quad b_V(k)=\sum_{\substack{d\mid k\\d\le V}}\mu(d).
\]
故对 \(n>U\)，作者式 (8) 的负号、\(m>U,k>V\) 域及
\(g_{U,V}(d)=-\sum_{ab=d,a\le U,b\le V}\Lambda(a)\mu(b)\)
均正确。它是原书恒等式的合法重排，不是将原书另一种 \(c_4\) 系数未经验证认成同一个表达。

在 \(p,q>\max(U,V)\) 的系数层面：

- 大素数 \(p\) 的 \(c_4\) 系数为零，\(c_3(p)=\log p\)。
- \(pq\)、\(p\ne q\) 的 \(c_3=\log p+\log q\)，而 \(c_4=-\log p-\log q\)。
- \(p^2\) 的 \(c_3=2\log p\)，\(c_4=-\log p\)，返回 \(\Lambda(p^2)=\log p\)。

进入高段时还保留 \(Y<n\le X\)。这些例子不能用来把整个 \(c_4\) 扔掉，也不能把某个正 sector 当成其完整 norm 的下界。

另用形式独立的 prime-log 基向量，在 \(U,V\in\{2,3,5,9,16\}\)、\(U<n\le768\) 上检查了 19,025 个精确整数系数恒等式；均通过。该有限检查只补核符号和系数，不认证任何 exponential-sum 或分析四矩估计。

## 5. Sharp Type I：正确的二阶导数尺度和端点

作者先将实际高段分成
\[
 N<n\le\min(2N,X),\qquad N=2^jY\le X.
\]
对固定 \(d\le UV\)，内层是实际 sharp 区间
\((N/d,\min(2N,X)/d]\)，写 \(R=N/d\)。于是
\[
 f(r)=\frac{t\log r}{2\pi},\qquad
 f''(r)=-\frac{t}{2\pi r^2},\qquad |f''(r)|\asymp T/R^2
\]
对所有 \(t\in[T/4,4T]\) 一致成立；导数没有被误写成 \(T/N^2\)。

原书 Theorem 16.7 允许负二阶导数经共轭处理，且适用于任意 partial endpoint。取整数长度上界 \(\lceil R\rceil\)，其常数可统一，给
\[
 \sup_{A\subset[R,2R]\ {\rm interval}}
 \Big|\sum_{r\in A\cap\mathbb Z}r^{it}\Big|
 \ll\sqrt T+R/\sqrt T .
\]
整数端点是否落在开下端，最多改变一个单位项，已包含于此 bound。这里不需要 smooth cutoff。

\(r^{-1/2}(\log r)^j\)、\(j=0,1\) 的 supremum 和总变差均为
\(O(R^{-1/2}(\log X)^j)\)。因此 Abel 后乘外部 \(d^{-1/2}\)，费用准确为
\[
 (\log X)^j\left(\sqrt{T/N}+\frac{\sqrt N}{d\sqrt T}\right).
\]
因为 \(N\le X=T/(2\pi)\)、\(d\ge1\)，第二项由第一项的固定倍数控制。关键是 \(N\ge Y\)：本证明没有把所有较短 prefixes 都按 top length 的导数免费估计。

\[
 \sum_{d\le UV}|g(d)|\ll_\delta(UV)^{1+\delta}\log(2UV),
 \qquad \sum_{d\le V}|\mu(d)|\le V
\]
故 \(UV\le X^{1/4}\)、\(T/Y\asymp X^{1/6}\) 给
\[
 \sup_{J_T}|I_2+I_3|\ll_\varepsilon X^{1/3+\varepsilon}.
\]
两项的实际 \(n\)-系数分别由 \(\tau_3(n)\log(2n)\) 和
\(\tau(n)\log(2n)\) 控制，长度为 \(X\)。§2 的二矩因而给
\(\|I_2+I_3\|_{2,T}^2\ll X^\varepsilon\)。
最后先分配小量，再用 \(\sup^2\times L^2\)，作者式 (15) 的
\(X^{2/3+\varepsilon}\) 确实支付完整高段 Type I。

## 6. Fixed cut tradeoff 与返回 genuine primes

新增 §6.1 的一般固定 \(0<a<1/4\)：
\[
 U=V=\lfloor X^a\rfloor,\quad Y=X^y,\quad y=(2+4a)/3
\]
满足 \(2/3<y<1\)。上述相同前件和 sharp 估计均保留。低块四矩幂为
\(2y-1\)，Type I 点值幂为 \(2a+(1-y)/2\)，故四矩幂为
\(4a+1-y\)。精确相等：
\[
 2y-1=4a+1-y=(1+8a)/3.
\]
\(a=1/8\) 返回 \(2/3\)；\(a=1/7\) 为 \(5/7\)。常数可依赖先固定的 \(a,\varepsilon\)，没有 \(a\to0\) 的未支付一致性主张。改变 cut 同时改变 \(C_4\) 的实际允许因子域，不能把未付的 Type II 上界视为自动不变。

冻结 proper-power 源 (17)–(19) 实际给
\(\|\widehat P_H-P_H\|_{4,T}=O_\phi(X^{-1/12})\)；它适用于同原正高度区间。作者准确保留 norm 差，而没有在未知增长下删成 additive fourth \(o(1)\)。

Minkowski 及 \((u+v)^4\le8(u^4+v^4)\) 因而严格给
\[
 \mathcal M_T\le8\mathcal M_{C_4}+C_{\phi,\varepsilon}X^{2/3+\varepsilon},
 \quad
 \mathcal M_{C_4}\le8\mathcal M_T+C_{\phi,\varepsilon}X^{2/3+\varepsilon}.
\]
这两个式子不是第四矩差的小量恒等式。

## 7. 未付预算与外部方法范围

\(C_4\) 保留 \(b_V(k)\) 的实际 truncated-divisor 系数、全部 dyadic aspect ratios 及共同 \(Y<mk\le X\) product mask。其 generic Cauchy 差分
\((mj)^{it}\overline{(mk)^{it}}=(j/k)^{it}\)
确实没有 \(m\) 导数，因此上面的 Type I 二阶导数不能直接迁移。

Guth–Maynard Theorem 1.1 本身是一般 large-value bound；作者源正确区分了“定理可写出”与相对旧 bound 的新增改善范围。\(N\asymp T\) 不在其文中 \(N\le T^{5/6-\varepsilon}\) 的相应改善区，balanced factor 的单列较短长度也没有自动支付共同八次均值和原 product mask。Heap 结果的 RH 与 transform-weight 限制同样没有由当前原两 sharp cutoffs 和 [Rθ] 自动满足。此处都是缺少具体准入/联合估计，不是方法不可能性结论。

**完成范围：限定 PASS。** Type I 的 \(2/3\) 是原 scalar 的真实子项付款，完整 \(C_4\) 是精确实际剩余。它比 476 的 whole \(5/7\) 小 \(1/21\)，但不能因此升级原整个 fourth 或 finite response。没有修改作者源、冻结文件、脚本、输出、Git 或 math 仓库。

