# 462：原低素数有限矩阵的完整第四矩常数

2026-10-07。原 genuine primes \(p\le\sqrt X\) 的整个 actual 四迹极限；
无需新的无零输入，也不以完整 prime 第四矩有界为前件。
全矩阵的其余高素数与混合项未由本结果闭合。

## 1. 同一个有限矩阵

采用 [461](461-original-one-high-three-low-fourth-trace.md) 的

\[
 X=T/(2\pi),\quad L=\log X,\quad Z=\sqrt X,\quad
 d=\lfloor XL\rfloor,\quad \tau_k=T+2\pi k/L,
 \quad Ee_k=L^{-1/2}1_{[-L/2,L/2]}e^{i\tau_k u}.
 \tag{1}
\]

仍取 \(P=EE^*,Q=1-P\)。原 AF 窗为

\[
 \phi(u)=\chi(L/2+u)\chi(L/2-u)\sqrt{\psi(u/L)},
 \qquad a_L=L^{-1}\|\phi\|_2^2\longrightarrow
 a_\psi=\int_{-1/2}^{1/2}\psi(v)\,dv>0.
 \tag{2}
\]

其中固定 even \(C^2\) 窗 \(0<\psi\le1\)，边缘 taper 的宽度固定；
包括 flat 及 Montgomery–Taylor 窗。注意归一化是 \(\int\psi\)，
因为 \(\phi^2\) 的 bulk 是 \(\psi\)。所有平移在实线上零延拓。
定义

\[
 b_p=\frac{\log p}{a_LL\sqrt p},\qquad
 B_L=-\sum_{p\le Z}b_pM_\phi(R_{\log p}+R_{-\log p})M_\phi,
 \qquad C_L=E^*B_LE.
 \tag{3}
\]

这不是 scalar prime polynomial 的第四矩；原有限载波、三个内部 \(P\)、
重复与全异 labels、全部 signs 都在对象内。

## 2. 定理和完整路径常数

把 \(\psi\) 在区间外零延拓为 \(\Psi\)。对 \(0\le x,y\le1/2\)，置

\[
 \begin{aligned}
 G_A(x,y)&=\sum_{\sigma,\eta=\pm1}\int_{\mathbb R}
    \Psi(v)^2\Psi(v+\sigma x)\Psi(v+\eta y)\,dv,\\
 G_O(x,y)&=\sum_{\sigma,\eta=\pm1}\int_{\mathbb R}
    \Psi(v)\Psi(v+\sigma x)\Psi(v+\sigma x+\eta y)
    \Psi(v+\eta y)\,dv.
 \end{aligned}
 \tag{4}
\]

**定理。** 只用原窗及经典 Chebyshev、Mertens、局部间距 Hilbert 输入，

\[
 \boxed{\frac1d\operatorname{Tr}C_L^4\longrightarrow
 \mathcal C_L(\psi)=\frac1{a_\psi^4}
 \int_0^{1/2}\!\int_0^{1/2}xy\,[2G_A(x,y)+G_O(x,y)]\,dx\,dy.}
 \tag{5}
\]

由于 \(d/N(T,2T)\to1\)，可以把分母换成 \(N(T,2T)\)。
完整逐词证明见
[研究稿](../reviews/2026-10-07/hybrid-low-prime-exact-fourth-path-constant-research.md)，
独立复核见
[radial](../reviews/2026-10-07/hybrid-low-prime-exact-fourth-review-radial.md)
及 [compression](../reviews/2026-10-07/hybrid-low-prime-exact-fourth-review-compression.md)。

## 3. 原内部投影的误差

个别平移项在 interval 全部整数载波基底上有准确系数

\[
 -b_pe^{i\tau_k s}\frac1L\int
 \phi(u)\phi(u+s)e^{-2\pi i(j-k)u/L}\,du.
 \tag{6}
\]

outside pairs 数为 \(\min(d,|j-k|)\)。原 \(C^2\) 窗的一、二阶导数
\(L^1\) 界统一于 \(s\)，故 Fourier 系数界为
\(O(\min(1,|n|^{-1},L|n|^{-2}))\)。对两符号求和得到

\[
 \|QB_pP\|_{\rm HS}\ll b_p\sqrt{\log(2+L)},\qquad
 y:=\|B_L\|\ll\sqrt Z/L,\quad
 \ell:=\|QB_LP\|_{\rm HS}\ll\sqrt{Z\log(2+L)}/L.
 \tag{7}
\]

不使用 [R] 或辅助 Fourier band。把 selfadjoint \(B_L\) 写成
\(\begin{pmatrix}A&C^*\\C&D\end{pmatrix}\)，则准确有

\[
 \begin{aligned}
 \operatorname{Tr}(PB_L^4P)-\operatorname{Tr}A^4
 &=2\operatorname{Tr}(A^2C^*C)+\operatorname{Tr}(C^*C)^2
    +\|CA+DC\|_{\rm HS}^2\\
 &\in[0,7y^2\ell^2].
 \end{aligned}
 \tag{8}
\]

除以 \(d\asymp XL\)，原 physical/actual 差为
\(O(\log(2+L)/L^5)=o(1)\)。这一步先付完整低素数四词的三个内部投影。

## 4. 所有非对角词均为小量

物理词保留原累计路径窗及有限几何载波 \(K_d(S)\)。在
\(c\le|S|<L\) 中，端点 overlap 给
\( |K_d(S)|\langle|W|\rangle\ll_c X^{-1}\)，包括两端 alias。
支持外词准确为零。

近共振须先从两正两负的 product 比较中删除准确相等 \(pq=rs\)；
之后联合 Fourier 分离全部共享窗，用同一 log-integer union 的
零 diagonal 双线性 Hilbert 界。两个集合即使重叠，核的 diagonal
已删，不产生新 pole。真实加权能量为 \(O(X/L^2)\)，归一化费用
\(O(\log(2+L)^4/L^2)=o(1)\)。

三正一负的 near 支持给 \(pqr\le2h\le2Z\)。prime 与 triple
product 无准确相等项，Hilbert 费用为
\(O(X^{-1/2}\log(2+L)^4/L)\)。同号词没有 near。
所有 signs 的 far 直接使用真实路径支持与正质量；两正两负为
\(O(L^{-4})\)，三正一负为 \(O(L^{-2})\)，全同号为
\(O(X^{-1/2}/L)\)。各反向词由偶窗共轭处理。
这些界包含全部 labels 和 alias，不借用未证的 prime cancellation。

## 5. 准确零位移与 flat 值

唯一素因子分解保证四 prime 的零位移只来自两正两负的匹配。
对 ordered \(p,q\) 和 \(\sigma,\eta=\pm1\)，三种配对路径是

\[
 (p^\sigma,p^{-\sigma},q^\eta,q^{-\eta}),\quad
 (p^\sigma,q^\eta,q^{-\eta},p^{-\sigma}),\quad
 (p^\sigma,q^\eta,p^{-\sigma},q^{-\eta}).
 \tag{9}
\]

当 \(p\ne q\) 时每个 signed word 恰计一次。第二类经实线变量代换
给第一类的同一个积分；第三类给交错路径。
当 \(p=q\) 时六个 two-plus/two-minus words 各被计两次，要减去六条
各一次。其 normalized 修正是 \(O(\sum b_p^4)=O(L^{-4})\)。

Mertens 给原正测度

\[
 \sum_{p\le\sqrt X}\frac{\log^2p}{L^2p}
 \delta_{\log p/L}\ \Longrightarrow x\,dx\big|_{[0,1/2]}.
 \tag{10}
\]

固定边缘层对每个 translated path 的积分误差一致为 \(O(L^{-1})\)。
\(G_A,G_O\) 连续；flat 窗也由 translation 的 \(L^1\) 连续性保证。
所以 product measure 的 weak limit 给 \(5\)，不交换不受控的移动极限。

对 flat \(\Psi=1_{[-1/2,1/2]}\)，\(a_\psi=1\)，准确有

\[
 G_A=2(1-\max(x,y))+2(1-x-y),\qquad G_O=4(1-x-y).
 \tag{11}
\]

两项有理积分为

\[
 \int_0^{1/2}\!\int_0^{1/2}xy(1-\max(x,y))\,dx\,dy=3/320,
 \quad
 \int_0^{1/2}\!\int_0^{1/2}xy(1-x-y)\,dx\,dy=1/192.
\]

故

\[
 \boxed{\mathcal C_L(1)=4(3/320)+8(1/192)=19/240.}
 \tag{12}
\]

这替代 [453](453-explicit-low-prime-fourth-moment-budget.md) 的同一 low
部分 Jensen 上界 \(3/16\)，上界与精确值的差是 \(13/120\)。
两者对应同一低素数对象；这个差不是已经得到的零点比例改善。

## 6. 剩余完整预算

[461](461-original-one-high-three-low-fourth-trace.md) 已付 entire13；本笔记
付 entire low4。但 high4 的全异项、31、22 的 joint product norm 与
commutator，以及原背景 \(\operatorname{Tr}(AC^3)\) 尚待控制。
旧 repeated 子常数不能和 \(12\) 自由相加成整个矩阵的第四矩。

目前没有新的完整比例或无零边界；既有引用输入下
\(\sigma_*\approx0.874957019420099\) 保持。按照用户指示，只在确认完整
新边界后另写正式边界论文；本次先记录为可审查研究笔记。
