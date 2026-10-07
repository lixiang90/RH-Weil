# 原 high 四矩的半区间 Gram、有限谱对称与 Möbius 完成接口

2026-10-07。radial_review。继续尚未验收的 whole-fourth 稿，
没有修改该稿、冻结 notes、论文、math 或 Git。
本轮未得到净 \(O(1)\) 第四矩。新增的是原对象的准确正 ratio 方差、
实际有限载波的无条件二范数谱对称估计，以及两素数列的准确
Möbius convolution 完成和未获准的长度/行接口。
这些结果不能由现有二矩输入升级成完整四矩预算。

## 1. 输入与旧稿的重新核对

使用原 \(X=T/(2\pi),L=\log X,d=\lfloor XL\rfloor\)，
\(I=[-L/2,L/2]\)，
\[
 Ee_k=L^{-1/2}1_Ie^{i\tau_ku},\qquad
 \tau_k=T+2\pi k/L,\qquad P=EE^*,\quad Q=1-P .
 \tag{1}
\]
原 even nonnegative \(C^2\) taper \(\phi\)、sharp genuine high primes
\(\sqrt X<p\le X\)、\(b_p=\log p/(a_LL\sqrt p)\) 全部不变。
平移 convention 是 \(R_sf(u)=f(u+s)\)，并在实线上零延拓。

绑定：

| 输入 | canonical LF SHA-256 |
| --- | --- |
| 尚未验收 whole-fourth 稿 | 0703f66778d49de29e363f7eabede6718ef24fe579e53603ff70db4e6aeacdea |
| high 四词报告 | 988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666 |
| 462 | 868adfeb0d742043f39bd08e0783d66b7a9db11316067b0b3b43d80150cdf680 |
| 463 | 6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90 |
| 454 | 8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7 |

以上各项均已重新计算磁盘 canonical hash；下面只引用454已付的
bounded static background 与加权二矩，未借用未付三素数项。
Compression_bridge 独立重核旧稿 §6–7 的 progression 与 nearcore；
本代理也逐步重新核对，未发现两处论证的数学错误。

旧稿 (20) 在实际 \(P,q,r\le X\)、\(q\nmid r\) 中准确。
对每个 \(p\)，先分一个 nonzero nearest residue 及
\(q\)-spacing tails，后者为 \(O(\log(2X)/q)\)；
完整 \(q\)-block 的 nearest reciprocal 总和由 \(r\bmod q\)
置换给 \(O(\log q)\)，末尾 partial block 以完整 residue 集合支付。
必须保留 \(P/q+1\)。\(q\mid p\) 的 zero center 剔除后仍有同阶 tails。
后续排序使 \(q\lesssim P\)，所以箱预算 \(PR/L\) 没有漏掉额外行计数。

旧稿 nearcore 的四 distinct tuple 数、剔除 \(O(m^2)\) 重复、
真实 \(K_d\) 的正实区和 fixed endpoint overlap 均准确。
它只给 restricted signed sum 下界，不能给完整正范数下界。
本轮不以它再次宣称完整 fourth 或 actual/physical equality。

## 2. 实际 high 算子的严格 bipartite 分解

置 \(\Pi_\pm=M_{1_{\{\pm u>0\}}}\)，
\[
 A=-\sum_{\sqrt X<p\le X}b_pM_\phi R_{\log p}M_\phi,
 \qquad B_H=A+A^*,\qquad C_H=E^*B_HE .
 \tag{2}
\]
每个步长 \(>L/2\)。非零正平移项的 output 必在 \(I_-\)，input 必在
\(I_+\)，所以
\[
 A=\Pi_-A\Pi_+,\qquad A^2=(A^*)^2=0 .
 \tag{3}
\]
这不是对有限矩阵 \(E^*AE\) 宣称 nilpotence；内部 \(P\) 可能使它的平方非零。
Physical 准确有
\[
 B_H^2=AA^*+A^*A,\qquad
 B_H^4=(AA^*)^2+(A^*A)^2 .
 \tag{4}
\]

令 \(\mathcal Jf(u)=f(-u)\)。原 even 窗和 real prime coefficients 给
\(\mathcal JA\mathcal J=A^*\)，而
\(\mathcal JEe_k=\overline{Ee_k}\)。
\(G=A^*A\) 是 real selfadjoint 算子；反射再共轭使两个 block 的
有限 trace 相同，因而
\[
 \boxed{\Phi_H:=\operatorname{Tr}(E^*B_H^4E)
       =2\|GE\|_{\rm HS}^2.}
 \tag{5}
\]
有限载波未改成 full Hilbert trace，原 absolute \(\tau_k\) 保留。

## 3. 已付 cross trace 后的准确正 ratio 方差

写 \(A=\sum_pA_p\)，并定义同素数对角
\[
 D=\sum_pA_p^*A_p=M_{D_L},\qquad
 D_L(u)=\phi(u)^2\sum_pb_p^2\phi(u-\log p)^2,\qquad
 R=G-D .
 \tag{6}
\]
\(D_L\) 仅支撑于 \(I_+\)，且
\(\|D_L\|_\infty\le\sum_pb_p^2=O(1)\)。
这里 \(R\) 是 selfadjoint 的 offdiagonal two-prime-ratio 算子，
并非从其 signed coefficients 取 positive majorant。

准确作用公式为
\[
 Rf(u)=\phi(u)\sum_{p\ne q}b_pb_q\phi(u-\log p)^2
 \phi(u+\log(q/p))f(u+\log(q/p)).
 \tag{7}
\]
对 cross trace 作 \(z=u-\log p\) 变量代换，得到
\[
 \frac1d\operatorname{Tr}(E^*DRE)
 =\frac1L\int\phi(z)^2
 \sum_{p\ne q}b_pb_q[D_L\phi](z+\log p)\phi(z+\log q)
 K_d(\log(q/p))\,dz .
 \tag{8}
\]
这一次 coupled profile 准确成为 \(p\)-only 与 \(q\)-only factors；
没有移除共享窗后再假称 separable。
各 prime frequencies 的局部间距 \(\delta_p\ge1/(2p)\)，
\(|\log(p/q)|<L/2\) 无 alias。把原 finite csc kernel 的 numerator
拆成两个 exponentials，主项用 bilateral weighted Hilbert，remainder
用正质量。Uniform 于 \(z\) 的费用至多
\[
 O\!\left(\|D_L\|_\infty
 \left[\frac Ld\sum_ppb_p^2+\frac1d\left(\sum_pb_p\right)^2\right]\right)
 =O(1/L).
 \tag{9}
\]
积分的 common \(\phi^2\) mass 除以 \(L\) 有界，因此 (8) 为 \(O(1/L)\)。
这里只需要 Chebyshev、原 finite grid 和二矩 Hilbert，不需要 [R] 或 full fourth。

令 \(d_{H,L}(u)=D_L(u)+D_L(-u)\)。两半支撑不交，故
\[
 \frac{2}{d}\operatorname{Tr}(E^*D^2E)
 =\langle d_{H,L}^2\rangle,\qquad
 \langle f\rangle=L^{-1}\int_I f .
 \tag{10}
\]
原 high diagonal profile 极限 \(d_{H,\psi}\) 与 high 报告一致；
记 \(S_\psi=\int_{-1/2}^{1/2}d_{H,\psi}(v)^2\,dv\)。
将 (5) 展开，并用 (8)–(10)，严格得到
\[
 \boxed{\frac{\Phi_H}{d}
 =S_\psi+\frac{2}{d}\|RE\|_{\rm HS}^2+o(1).}
 \tag{11}
\]
Flat 时 \(d_{H,1}(v)=|v|(|v|+1)/2\)，
\[
 S_1=2\int_0^{1/2}\left(\frac{v(v+1)}2\right)^2dv
 =19/480 .
 \tag{12}
\]
这个基线不是 whole high 的新确定常数。
旧 repeated union 为 \(2S_\psi\)，不与 (11) 冲突：
全异净 signed contribution可以降低它，最终留下非负 ratio 方差。

特别地，physical full-high \(O(d)\) 与
\(\|RE\|_{\rm HS}^2=O(d)\) 严格互相蕴含。
待付观测量已成为具体 columns：
\[
 \frac{\|RE\|_{\rm HS}^2}{d}
 =\frac1L\int_{I_+}\phi(u)^2\frac1d\sum_{k=0}^{d-1}
 \left|\sum_{p\ne q}b_pb_q\phi(u-\log p)^2
 \phi(u+\log(q/p))e^{i\tau_k\log(q/p)}\right|^2du .
 \tag{13}
\]
整个求和是同一原 coefficient/profile；square 展开仍含全部
four-prime ratio coincidences和signed offdiagonal。
正 nearcore 是其展开中的一部分，不能单独下界 (13)。

## 4. Actual centered-square residual 与 internal projection

令 \(\widehat D=E^*M_{d_{H,L}}E\)，
\(K=(QB_HE)^*(QB_HE)\succeq0\)。准确有
\[
 C_H^2-\widehat D
 =E^*(R+\mathcal JR\mathcal J)E-K .
 \tag{14}
\]
\(K\) 的 trace为 \(O(X\log(2+L)/L^2)=o(d)\)，
但它的 Hilbert–Schmidt平方不能由这个 first-moment界自动变成 \(o(d)\)。

已付 high 报告的 \(T_0\) 与 bounded diagonal Toeplitz 估计给
\[
 d^{-1}\operatorname{Tr}(\widehat DC_H^2)\to S_\psi,\qquad
 d^{-1}\operatorname{Tr}\widehat D^2\to S_\psi .
 \tag{15}
\]
这些输入本身不预设 \(C_H^4=O(d)\)。因此准确恒等式的 asymptotic 是
\[
 \boxed{\frac1d\operatorname{Tr}C_H^4
 =S_\psi+\frac1d\|C_H^2-\widehat D\|_{\rm HS}^2+o(1).}
 \tag{16}
\]
它把 actual 待付项写成 ratio compression减正 leakage 的整体 residual。
Physical (13) 有界是充分路线，但 actual (16) 有界并不倒推出 (13)；
禁止由 \(K\succeq0\) 给两个不交换 selfadjoint算子的平方错误排序。

## 5. 有限载波上的真实谱对称二范数估计

另令 \(J=M_{\operatorname{sgn}u}\)，\(S=E^*JE\)。
式 (3) 给 \(JB_H+B_HJ=0\)。原 interval carrier 的 Fourier coefficients
对 odd \(n\ne0\) 有绝对值 \(2/(\pi|n|)\)，对 even \(n\) 及0为零，
所以
\[
 \operatorname{Tr}(I-S^2)=\|QJE\|_{\rm HS}^2
 \ll\sum_{n\ge1}\frac{\min(d,n)}{n^2}=O(\log(2d)).
 \tag{17}
\]
保留有限投影后
\[
 SC_H+C_HS=-(QJE)^*(QB_HE)-(QB_HE)^*(QJE).
 \tag{18}
\]
无条件 \(\|B_H\|\ll\sqrt X/L\) 因此给
\(\|SC_H+C_HS\|_{\rm HS}\ll\sqrt{X\log(2d)}/L\)。
令 \(U=\operatorname{sgn}S\)，零特征值处选 \(+1\)，则 \(U^2=I\) 且
\(\|U-S\|_{\rm HS}^2\le\operatorname{Tr}(I-S^2)\)。
Consequently
\[
 \boxed{\frac1d\|C_H+UC_HU\|_{\rm HS}^2=O(L^{-2}).}
 \tag{19}
\]
这是真实 finite-carrier parity，不是把 \(P\) 换成与 \(J\) 可交换的投影。
Hoffman–Wielandt使经验谱与其反射在 quadratic transport中趋同；
按排序 \(\lambda_1\le\cdots\le\lambda_d\)，
\(d^{-1}\sum_j|\lambda_j+\lambda_{d+1-j}|^2=O(L^{-2})\)。
但该二范数结果不支付第四次方 tails。用现有 op 界把它升级为 \(S_4\)
只给 normalized \(O(X/L^4)\)，仍增长；对称稀疏大特征值也完全可能。
不能用此估计声称 full fourth有界或 odd high fourth-word自动小。

## 6. 真实两素数列的 Möbius convolution 完成

整数 Dirichlet coefficients准确有
\[
 (\Lambda*\Lambda)(n)=(\mu*\log^2)(n)-\Lambda(n)\log n .
 \tag{20}
\]
在 \(\Re s>1\)，由
\[
 \left(-\frac{\zeta'}\zeta\right)^2
 =\frac{\zeta''}{\zeta}
   -\left(\frac{\zeta'}\zeta\right)'
 =\frac{\zeta''}{\zeta}
   -\sum_n\Lambda(n)\log n\,n^{-s}
 \tag{21}
\]
逐系数证明。对 distinct \(n=pq\)，右边正是 \(2\log p\log q\)；
不含另外三个 distinct primes，prime-power branches也准确保留。
这给 high balanced products一个真正 inverse×plain-derivative 完成，
而非只把它们称作“某个 fourth moment”。

但是原 high sum还要求每个 factor在 \((\sqrt X,X]\)，以及
(13) 的两个路径窗口；它不是只对 \(n\le X^2\) 作一次 cutoff。
在 \(n>X\) 丢掉某个大divisor会改变 \(\mu*\log^2\)；
按 high semiprime选择本身也不是原 Möbius列的一个 multiplicative zero mask。
原 norm phase的 row在这里是 \(\tau_k\asymp X\)，并非原有限
power-residue-character family中的平均 \(u\)-row。
即使使用普通 Dirichlet inverse，必须先证明这一 factor-conditioned
convolution及共同 absolute-height columns的准入。

实际双素数 products长度 \(X^2\)，观察高度长度 \(O(X)\)；
直接 weighted MV error为 \(O(X^2L^2)\)，原所需 scalar预算为 \(O(XL^4)\)。
恒等式 (20) 未缩短 product到 \(X\)。如果形式上把 height rows记作
\(U\asymp X\)、inverse length记作 \(D\asymp X^2\)，则
\(U\ge D^{1+c}\) 的现有 raw门槛甚至方向相反。
这是长度诊断，不是一个已经构造好的 original-source row映射。
Target单行、固定height的 reciprocal bound也不能代替这个 joint平均。

## 7. 462、463能接上什么，以及本轮未得的结论

463 现在允许原 actual与同类型good actual、physical与同类型good physical
整四词比较，absolute error \(O(L^{-4})\)，无需未知 full fourth。
它严格清除远 height费用，但不改变 (13)、(16) 的内部算术 residual；
good-band op/R费用仍不能冒充净 ratio均方。

462 给 \(\|C_L\|_{S_4}=O(d^{1/4})\)，bounded static背景同样有这个界，
proper-power \(S_4=o(d^{1/4})\)。因此对普通固定 bounded centering，
完整原 response 的 normalized fourth有界，严格等价于
actual high normalized fourth有界：用 Schatten triangle正反两次即可。
这是 boundedness equivalence，绝不是 sharp常数的自由相加。
已付 entire13和exact low4也没有消除 (16) 中的未知 nonnegative能量。

本轮新的 signed付款为 (8)–(11) 对 ratio diagonal cross 的完整处理，
以及 (17)–(19) 的实际有限谱对称；新的完成映射为 (20)–(21)。
尚未证明 (13) 或 (16) 为 \(O(1)\)，更未证明严格新的 \(\chi\)。
全 high/centered fourth、新的简单临界线比例与新的无零边界仍开放。
