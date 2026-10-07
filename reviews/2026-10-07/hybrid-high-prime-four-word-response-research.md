# 原 AF 高素数重复四词的真实有限压缩付款

2026-10-07。作者：`twisted_research`。本报告在提交
`f76eb72bff841c689ad2de228308720d62d880b7` 的干净工作区上继续研究。
只新增本报告，未修改原论文、notes、math 或既有审查。

本次得到的 [T] 结果是：在 AF 原 finite Fourier frame、原平滑窗和真实
zero-extended physical translations 中，高素数 `sqrt(X)<p<=X` 的四词和，
凡四个素数指标中出现重复的整个 sector，都有显式 `O(N)` 费用。若其有符号和
记为 `S_rep`，则

\[
 -o(N)\le S_{\rm rep}\le 4S_\psi N+o(N),\qquad
 S_\psi:=\int_{-1/2}^{1/2}d_\psi(v)^2\,dv.
 \tag{1}
\]

indicator 窗的 `4S_psi=19/120`。Montgomery–Taylor 窗的系数由下文的
明确初等一维积分给出，数值约 `0.12404048801445156884`；此数值仅作展示，
证明使用积分公式。这不是完整 `Tr H^4` 付款：四个不同素数的实际 signed sector
仍未控制，而且完整 Hermitian response 的背景、低素数 mixed words 仍须合法合并。
本报告没有给新比例、零自由区或 RH 证明。

## 1. 原始输入、确切维数与绑定

原窗、Fourier 约定和 prime multiplier 来自
[Alpöge–Furman v2 §2](https://arxiv.org/html/2608.13637v2#S2)。
唯一额外均值输入是
[Montgomery–Vaughan, Hilbert's inequality, Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
的带局部频率间距 Hilbert inequality。本报告直接将它用于原有限几何核，
不用无限 sinc、平均投影或改造后的 sampling grid。

所用本地证据为：

| 文件 | SHA256；Markdown 按 CRLF→LF |
|---|---|
| [AF v2 PDF](../../literature/baseline/2026-alpoge-furman-6725-v2.pdf) | `6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444`；二进制 |
| [448](../../notes/448-canonical-type-i-admission-finite-gram-and-low-prime-fourth-norm.md) | `6a7219f929cc50a721227c722fd9553eb7eba1ed9d4dd432bd971b39c2e6eafa` |
| [joint Type-II 报告](hybrid-joint-type-ii-fiber-research.md) | `238fd374cad6da451fd186c6f3766d79d869ff8ae92ed6441e0ca516e1398473` |

设

\[
 X=T/(2\pi),\quad L=\log X,\quad d=\lfloor XL\rfloor,
 \quad \tau_k=T+2\pi k/L\quad(0\le k<d),\quad I=[-L/2,L/2].
 \tag{2}
\]

以下用的是这个确切 `floor` 维数。仅在最后使用
`d/N(T,2T)→1`；不使用 `d=N(T,2T)+O(L)`。
后一个字样出现在 AF HTML §2.2，但与它自己 §1.1 的 Riemann–von Mangoldt
主项不一致；本报告不依赖它。

固定 AF 的偶窗 `psi`，取 indicator 或 MT；更一般的固定偶正 `C^2` 窗也适用，
只需先固定它的范数并归一化 `0<psi<=1`。令

\[
 \phi(u)=\chi(L/2+u)\chi(L/2-u)\sqrt{\psi(u/L)},\qquad
 a_L=L^{-1}\|\phi\|_2^2,\qquad a_\psi=\int_{-1/2}^{1/2}\psi(v)\,dv.
 \tag{3}
\]

真实 `phi` 是偶、非负、`C_c^2`，`a_L=a_psi+O(1/L)`，且
`||phi'||_1+||phi''||_1=O_(chi,psi)(1)`。它没有被裸 indicator 替代。

令 `H=L^2(I,du)`，所有平移先把函数以零延拓到 `R`。
定义 isometry 与 unitary Fourier transform

\[
 E e_k(u)=L^{-1/2}\mathbf1_I(u)e^{i\tau_k u},\qquad
 (\mathscr F f)(t)=(2\pi)^{-1/2}\int_{\mathbb R}f(u)e^{-itu}\,du.
 \tag{4}
\]

记 `P=EE*`、`Q=1-P`，并在必要时把 `H` 看作 `L^2(R)` 的支撑子空间。
原 AF frame 的 contraction 准确为

\[
 F=\mathscr F M_\phi E,
 \qquad F e_k(t)=\frac{\widehat\phi(t-\tau_k)}{\sqrt{2\pi L}}.
 \tag{5}
\]

## 2. 高素数物理算子及平方乘法符号

令 `P_X={p prime:sqrt(X)<p<=X}`，并写

\[
 \ell_p=\log p,\quad \lambda_p=\frac{\log p}{\sqrt p},\quad
 b_p=\frac{\lambda_p}{a_LL},\qquad (R_s f)(u)=f(u+s).
 \tag{6}
\]

真实高素数 multiplier 与其 finite compression 是

\[
 M_{\rm hi}(t)=-\frac1\pi\sum_{p\in\mathcal P_X}\lambda_p\cos(t\ell_p),
 \quad C=\frac{2\pi}{a_LL}F^*M_{\rm hi}F=\sum_{p\in\mathcal P_X}C_p,
 \tag{7}
\]
\[
 B_p=-b_pM_\phi(R_{\ell_p}+R_{-\ell_p})M_\phi,
 \qquad B=\sum_p B_p,\qquad C_p=E^*B_pE,
 \qquad C=E^*BE.
 \tag{8}
\]

式(8)由 `mathscrF R_s=e^{its}mathscrF` 与 `cos=(exp+exp)/2` 直接给出，
保留了原 `2pi/(a_L L)`。`C_p` 与 `C` 都是实际有限 Hermitian 矩阵。

因为 `ell_p>L/2`，两个相同方向的 high shifts 不可能同时落在长度 `L`
的物理支撑中。因此

\[
 B_p^2=b_p^2M_{\phi(u)^2[\phi(u+\ell_p)^2+\phi(u-\ell_p)^2]},
 \qquad \|B_p\|_{\rm op}\le b_p.
 \tag{9}
\]

正向输出只在 `u<0`，负向输出只在 `u>0`；它们严格分离。
定义

\[
 d_L(u)=\sum_p b_p^2\phi(u)^2[\phi(u+\ell_p)^2+\phi(u-\ell_p)^2],
 \quad\mathcal D=\sum_p C_p^2,\quad\widehat{\mathcal D}=E^*M_{d_L}E.
 \tag{10}
\]

则真实差额是正的投影泄漏：

\[
 \widehat{\mathcal D}-\mathcal D
 =\sum_p E^*B_p Q B_pE\succeq0.
 \tag{11}
\]

不会把 `sum C_p^2` 直接认作 multiplication。Chebyshev–Mertens 给

\[
 \sum_p b_p\ll\sqrt X/L,\qquad \sum_p b_p^2=O(1),\qquad
 \|B\|_{\rm op}\ll\sqrt X/L,
 \quad \|d_L\|_\infty=O(1).
 \tag{12}
\]

## 3. finite carrier projection 泄漏的实际付款

这节只借用 circle Fourier basis 计算原 `P`，不把物理零延拓改成周期平移。
对任意 `s`，置 `a_s(u)=phi(u)phi(u+s)`。在 `I` 上，它在发生 wrap 的区间
准确为零。在 carrier `exp(iTu)` 共轭后，`M_phi R_s M_phi` 准确等于
`M_(a_s)` 乘上对这个 Fourier basis 的 quasiperiodic circle rotation。
后者与 `P` 交换；wrap phase 无论怎样都被 `a_s=0` 消去。

`a_s` 的 periodic `C^2` 延拓满足，统一于 `s`，

\[
 \|a_s'\|_1+\|a_s''\|_1=O(1),\qquad
 |\widehat a_s(n)|\ll\min\{1,|n|^{-1},L|n|^{-2}\}\quad(n\ne0),
 \tag{13}
\]

其中系数按 `(1/L)int_I a_s(u)exp(-2pi inu/L)du` 定义。
两次 integration by parts 给最后一项，真实 taper 使端点项为零。
于是直接计数 Fourier mode 跨越有限区间 `0,...,d-1` 的次数得到

\[
 \|Q M_{a_s}P\|_2^2
 =\sum_{n\in\mathbb Z}\min(d,|n|)|\widehat a_s(n)|^2
 \ll\log(2+L).
 \tag{14}
\]

因此，每个 high prime 与整个 high multiplier 分别有

\[
 \|Q B_pE\|_2\ll b_p\sqrt{\log(2+L)},\quad
 \sum_p\|Q B_pE\|_2^2\ll\log(2+L),
 \tag{15}
\]
\[
 \|QBE\|_2^2\ll\frac{X\log(2+L)}{L^2}=o(d).
 \tag{16}
\]

式(16)只是 triangle inequality 与(12)；并未假定不同 primes 的泄漏正交。
同理，`d_L` 的一、二阶 derivative `L^1` norm 是 `O(1)`，因为(10)的
每个 `a_(±ell_p)^2` 有统一 derivative bound，而 `sum b_p^2=O(1)`。
故

\[
 \|Q M_{d_L}P\|_2^2\ll\log(2+L),\quad
 \operatorname{Tr}(\widehat{\mathcal D}-\mathcal D)\ll\log(2+L).
 \tag{17}
\]

此处 `||.||_2` 是 Hilbert–Schmidt norm。所有结论保留有限 `d` 与 carrier。

## 4. 原有限几何核上的 weighted Hilbert 支付

记准确有限复核

\[
 K_d(s)=d^{-1}\sum_{k=0}^{d-1}e^{i\tau_k s}
 =e^{i[T+(d-1)\pi/L]s}\frac{\sin(d\pi s/L)}{d\sin(\pi s/L)}.
 \tag{18}
\]

对 `ell_p-ell_q`，跨度严格小于 `L/2`，所以没有 grid alias。
每个 log prime 的局部间距满足
`delta_p=min_(q≠p)|log p-log q|>=1/(2p)`。
Montgomery–Vaughan Theorem 2 给绝对常数 `C_H`，使

\[
 \left|\sum_{p\ne q}\frac{z_p\overline{z_q}}{\ell_p-\ell_q}\right|
 \le C_H\sum_p\frac{|z_p|^2}{\delta_p}.
 \tag{19}
\]

在(18)中把 `sin(d pi s/L)` 写成两个 exponential，并用
`csc(pi s/L)=L/(pi s)+O(|s|/L)`，得到对任意实数 `0<=w(u)<=O(1)`：

\[
 \left|\sum_{p\ne q}b_pb_q a_{\ell_p}(u)a_{\ell_q}(u)
                    K_d(\ell_p-\ell_q)\right|
 \ll\frac Ld\sum_p\frac{b_p^2}{\delta_p}
       +\frac1d\Big(\sum_pb_p\Big)^2
 \ll\frac1L.
 \tag{20}
\]

`w` 可以在积分中乘上此式，费用至多乘 `||w||_infty`。
每个 numerator exponential，包括 `T`，都准确进入 `z_p` 的单位相位；
没有先删除 carrier 再声称 cancellation。最后一个界使用
`sum_(p<=X)(log p)^2≪XL`，只需 Chebyshev。

由于(9)的正负输出分离，对 `B E e_k` 展开后没有正负 mixed product。
取 `w=1` 与 `w=d_L`，式(20)的 diagonal 准确分别给

\[
 \operatorname{Tr}(E^*B^2E)=d\,\langle d_L\rangle+O(d/L),
 \qquad
 \operatorname{Tr}(E^*B M_{d_L}BE)
   =d\,\langle d_L^2\rangle+O(d/L),
 \tag{21}
\]

其中 `<f>=(1/L)int_I f(u)du`。这些是实际 finite-k sum；不是时间平均替代。
由(16)，

\[
 \operatorname{Tr}C^2=d\,\langle d_L\rangle
     +O\!\left(d/L+X\log(2+L)/L^2\right)=O(d).
 \tag{22}
\]

特别地，后续小项可以用 `Tr|C|<=sqrt(d TrC^2)=O(d)`，无需假设 `TrC^4=O(d)`。

## 5. 真正控制重复 sector 的两个四阶量

设

\[
 T_0=\operatorname{Tr}(\mathcal D C^2),\qquad
 T_{22}=\operatorname{Tr}\mathcal D^2.
 \tag{23}
\]

首先，由(11)、(12)、(17)，把 `mathcalD` 换成 `widehatmathcalD` 在 `T_0`
中的误差至多
`||C||_op^2 Tr(widehatmathcalD-mathcalD)≪X log(2+L)/L^2`。
有限迹循环给 `Tr(widehatmathcalD C^2)=Tr(C widehatmathcalD C)`。
将 `BE=EC+QBE` 代入(21)第二式，两者之差由一个 cross term 与一个 positive term 构成，
绝对值至多

\[
 2\|C\|_{\rm op}\|P M_{d_L}Q\|_2\|QBE\|_2
       +\|d_L\|_\infty\|QBE\|_2^2
 \ll X\log(2+L)/L^2.
 \tag{24}
\]

这里用的是实际 right projection 与 right adjoint，没有漏掉右侧 `P`。
因此

\[
 T_0=d\,\langle d_L^2\rangle
      +O\!\left(d/L+X\log(2+L)/L^2\right).
 \tag{25}
\]

其次，(11)、(17)与统一 operator norm 给
`Tr widehatmathcalD^2-Tr mathcalD^2=O(log(2+L))`；而

\[
 \operatorname{Tr}(E^*M_{d_L}^2E)-\operatorname{Tr}\widehat{\mathcal D}^{,2}
 =\|Q M_{d_L}E\|_2^2\ll\log(2+L).
 \tag{26}
\]

所以

\[
 T_{22}=d\,\langle d_L^2\rangle+O(\log(2+L)).
 \tag{27}
\]

这个相同主项是本次关键付款，不能仅凭 `||mathcalD||_op=O(1)` 得到。

## 6. 两对交叉指标 pqpq 的 actual path 与 projection 误差

令

\[
 T_\times=\sum_{p,q}\operatorname{Tr}(C_p C_q C_p C_q).
 \tag{28}
\]

先逐对比较(28)与 `Tr(E* B_p B_q B_p B_q E)`。在三个 internal `P`
中从左到右删除，每个差额的 `Q` 右邻仍是某个 `B_rP`，其 Hilbert–Schmidt
norm 由(15)付款。其余因子的 norm 用(12)及 `rank P=d`。故

\[
 \left|T_\times-
 \sum_{p,q}\operatorname{Tr}(E^*B_pB_qB_pB_qE)\right|
 \ll\sqrt{d\log(2+L)}\Big(\sum_p b_p^2\Big)^2
 \ll\sqrt{d\log(2+L)}=o(d).
 \tag{29}
\]

例如删第二个 `P` 的项是
`Tr(P B_p B_q Q B_p P B_q P)`；把 `QB_pP` 放在一个 Hilbert–Schmidt
因子，其余 product 的 Hilbert–Schmidt norm 至多 `sqrt(d)b_p b_q^2`。
因此单项不超过 `sqrt(d log(2+L))b_p^2b_q^2`。
这不是对所有 four-distinct words 都有效的 aggregate bound：其可求和系数是
`sum_(p,q)b_p^2b_q^2=O(1)`，而非 `(sum_p b_p)^4`。

原物理四词的精确 kernel 为：对 `s_j=epsilon_j log p_j`、
`S_j=s_1+...+s_j`、`S_0=0`，

\[
 \operatorname{Tr}(E^*B_{p_1}B_{p_2}B_{p_3}B_{p_4}E)
 =d\prod_{j=1}^4 b_{p_j}
   \sum_{\epsilon\in\{\pm1\}^4}K_d(S_4)\,\langle W_\epsilon\rangle,
 \tag{30}
\]
\[
 W_\epsilon(u)=\phi(u)\phi(u+S_4)
                 \prod_{j=1}^3\phi(u+S_j)^2.
 \tag{31}
\]

所有 physical positions `u+S_j` 都必须落在 `I`。因为每步长度 `>L/2`，
相邻同号必使某两点的距离超过 `L`，所以只有交替的两个 sign patterns 能非零。
在 `pqpq` 中，它们的最终位移是 `±2(log p-log q)`。
其非零支撑还强制该位移的绝对值 `<L/2`：对 `+−+−`，若 `S_4>=L/2`，
则 `S_3=S_4+ell_q>L`；若 `S_4<=-L/2`，则 `S_1-S_4>L`。
另一 pattern 同理。因此本项确实没有原 grid alias。

对 `p!=q`，原有限几何核满足

\[
 |K_d(2\log(p/q))|\ll\min\{1,[X|\log(p/q)|]^{-1}\}
 \ll |p-q|^{-1}.
 \tag{32}
\]

保留 `|W|<=1`，并用 `b_p^2b_q^2≪1/(pq)`，得到完全绝对的整数 majorant

\[
 \sum_{\substack{p,q\in\mathcal P_X\\p\ne q}}
 b_p^2b_q^2|K_d(2\log(p/q))|
 \ll\sum_{\sqrt X<n<m\le X}\frac1{nm(m-n)}
 \ll \frac L{\sqrt X}.
 \tag{33}
\]

最后一式逐个 `n` 用
`sum_(h>=1)1/[n(n+h)h]<=H_n/n^2`，再求和。
若对应 physical path 为空，该项为零，无须对 alias 频率错误使用(32)。
`p=q` 的 diagonal 至多 `2d sum_p b_p^4=O(d/L^4)`，因为
`sum_p (log p)^4/p^2<infinity`。合并得

\[
 T_\times=O\!\left(\sqrt{d\log(2+L)}+dL/\sqrt X+d/L^4\right)=o(d).
 \tag{34}
\]

这里未用 prime-pair PNT、未假设 independence，也没有删除 finite carrier。

## 7. 重复指标四词的确切 partition identity

把 `Tr C^4` 的全部有序四元素数词展开。令 `S_rep` 只收集四个标签不全不同的词，
并置

\[
 T_{\rm opp}=\sum_p\operatorname{Tr}(C_p C C_p C),\quad
 T_3=\operatorname{Tr}\!\left[(\sum_p C_p^3)C\right],\quad
 T_4=\sum_p\operatorname{Tr}C_p^4.
 \tag{35}
\]

partition lattice 的有限 inclusion–exclusion 准确给

\[
 \boxed{S_{\rm rep}=4T_0+2T_{\rm opp}-2T_{22}-T_\times-8T_3+6T_4.}
 \tag{36}
\]

六个单 pair 等式分成四个 cyclic adjacent pairs 与两个 opposite pairs；
三个 double-pair partitions 给 `-2T_22-T_times`；四个 triple partitions
各带系数 `-2`；全相同带 `+6`。这个组合不会把 `p=p=q=q` 等交叠 sector 重复付款。

对 Hermitian `A,B`，
`|Tr(ABAB)|<=Tr(A^2B^2)` 由 Hilbert–Schmidt Cauchy 给出。故

\[
 |T_{\rm opp}|\le T_0.
 \tag{37}
\]

由(22)和 `sum_p ||C_p||_op^3≪L^-3`，

\[
 |T_3|\le\Big\|\sum_p C_p^3\Big\|_{\rm op}\operatorname{Tr}|C|
       =O(d/L^3),\qquad
 0\le T_4\le d\sum_p b_p^4=O(d/L^4).
 \tag{38}
\]

因而(25)、(27)、(34)、(36)同时给

\[
 S_{\rm rep}=2d\langle d_L^2\rangle+2T_{\rm opp}+o(d),
 \quad |T_{\rm opp}|\le d\langle d_L^2\rangle+o(d).
 \tag{39}
\]

`S_rep` 不是有限矩阵的正 sector；这里只证明它的负部分是 `o(d)`。
上界所用的真实量是 `6T_0-2T_22+o(d)`，不把有符号 trace 改成独立词的正和。

## 8. 显式窗符号、leading coefficient 与量词

elementary Mertens formula
`sum_(p<=x)(log p)^2/p=(1/2)log^2 x+O(log x)` 给 normalized measure
`L^-2 sum lambda_p^2 delta_(log p/L)→r dr`。
真实 taper 只在 `u` 或 `u±ell_p` 的物理边带产生误差，未改变 bulk 符号。
对几乎所有 `v`，

\[
 d_L(Lv)\longrightarrow d_\psi(v):=
 \frac{\psi(v)}{a_\psi^2}
       \int_{1/2}^{1/2+|v|}r\psi(r-|v|)\,dr.
 \tag{40}
\]

`d_L` 一致有界。Mertens partial summation 的 integrand variation 统一有界；
自身 endpoint taper 占 `O(1/L)` 的 `v` 区间，其余 shifted taper 占 `O(1/L)`
的 `r` 区间。所以

\[
 \langle d_L\rangle=\int d_\psi+O(1/L),\qquad
 \langle d_L^2\rangle=S_\psi+O(1/L).
 \tag{41}
\]

式(39)证明(1)。更具体，余项除以 `d` 可取

\[
 O_{\chi,\psi}\!\left(
 L^{-1}+\frac{\log(2+L)}{L^3}
 +\sqrt{\frac{\log(2+L)}d}+\frac L{\sqrt X}\right)=o(1).
 \tag{42}
\]

所以，对固定 `chi,psi` 与任意 `epsilon>0`，存在 `X_0(chi,psi,epsilon)`，
对所有 `X>=X_0`，
`-epsilon d<=S_rep<=(4S_psi+epsilon)d`。无需零自由输入、全族假设或当前 target。
尾项常数未在本报告转换成某个数值高度阈值。

indicator 的 profile 与费用确切为

\[
 d_{\psi_0}(v)=\frac{|v|+v^2}2,
 \quad\int d_{\psi_0}=\frac16,
 \quad S_{\psi_0}=\frac{19}{480},
 \quad4S_{\psi_0}=\frac{19}{120}.
 \tag{43}
\]

对 MT，设 `c=sqrt(2)`、`a=sqrt(2)sin(1/sqrt(2))`。在 `0<=v<=1/2`，

\[
 d_{\rm MT}(v)=\frac{\cos(cv)}{a^2}
 \left[\frac{(1/2+v)\sin(c/2)}c+\frac{\cos(c/2)}2
       -\frac{\sin(c(1/2-v))}{2c}-\frac{\cos(c(1/2-v))}2\right].
 \tag{44}
\]

因此其严格 leading coefficient 是 `8 int_0^(1/2) d_MT(v)^2 dv`。
40 位工作精度的独立 quadrature 得
`S_MT≈0.0310101220036128922108340690126`，
`4S_MT≈0.12404048801445156884333627605`。
并未把浮点积分当作新的 rational positivity certificate。

## 9. 全 height 尾、projection 范围及完整 signed 余额

以上 Fourier/physical conjugation 在整条 height 轴准确进行；不先删掉低 height
或 `J^c`。如采用原 `J=[T/2,3T]` 的 scalar Jensen majorant，则
`|M_hi|≪sqrt X`，`sum_k int_(Jc)|hatphi(t-tau_k)|^2 dt≪dX^-3`，故

\[
 \left(\frac{2\pi}{a_LL}\right)^4
 \operatorname{Tr}\bigl(F^*\mathbf1_{J^c}M_{\rm hi}^{,4}F\bigr)
 \ll\frac d{XL^5}=O(L^{-4})=o(d).
 \tag{45}
\]

该 bound 支付正 scalar four-power majorant 的全 height 尾。
它没有把任意矩阵四迹拆成 `J` 和 `J^c` 两个无 cross-term 的四迹。
本文不需要那种分拆。

保留实际 finite projections，严格剩余量是

\[
 S_{\rm distinct}:=
 \sum_{\substack{p_1,p_2,p_3,p_4\in\mathcal P_X\\
                  p_i\ne p_j\ (i\ne j)}}
 \operatorname{Tr}(C_{p_1}C_{p_2}C_{p_3}C_{p_4}),
 \qquad \operatorname{Tr}C^4=S_{\rm rep}+S_{\rm distinct}.
 \tag{46}
\]

式(46)中每个词仍有 `P`。式(30)的 physical alternating-path 表达只在删除
这些 internal projections 后成立。本报告在(29)中为 `pqpq` 聚合合法支付了
这个删除；不能把相同删除免费用于(46)。比如只使用(12)、(16)得到的粗四阶
泄漏量级 `||B||_op^2||QBE||_2^2≪X^2 log(2+L)/L^4` 远大于 `d`。
这不是证明真实四阶泄漏这么大，而是说明此估计不足以闭合全域。

单向 scalar spectral Jensen 确实给
`Tr C^4<=Tr(E*B^4E)`；若另在完整 physical four-word sum 中付出上界，
它可作为充分路线。但不能把这个不等式当作带同一个 sharp 常数的 compression 等式。
four-distinct alternating physical words 的频率是
`log(p_1p_3/(p_2p_4))`，仍需它们的原窗权重、carrier、相关支撑与 signed 合并。
目前未支付其所需的净预算。

既有 [448 §5](../../notes/448-canonical-type-i-admission-finite-gram-and-low-prime-fourth-norm.md)
给低 `Lambda` 原完整压缩的四范数，`Z=exp(sqrt L)` 时为 `o(N)`，
`Z=sqrt X` 时为 `O(N)`。它们没有单独使所有 high/low mixed words 成为已付常数。
[joint 报告 §6–7](hybrid-joint-type-ii-fiber-research.md) 已给全部 proper powers
的 `o(N)` 四范数及合法稳定约化；将其 mixed words 以 `o(N)` 删除仍以剩余完整
四范数 `O(N)` 为前件。这些费用在本报告没有重新充当一次算术 saving。

本次实质新结果仅是：重复 high-prime 四词的原有限压缩预算、两对交叉词的
physical path 与 projection 的统一小量，以及控制重复 sector 所需的
`Tr mathcalD C^2` 和 `Tr mathcalD^2` 的相同明确主项。它没有替代共同 centering、
跨 factor cells 的 alias 或完整 Hermitian response 的四次 signed 余额。

下一有限任务可在 `Z=sqrt X` 的原 low compression 上，利用 `Q_Z^2` 的长度
仍不超过 `X`，把 weighted MV error 与 `Re Q_Z` 的非平衡四词分开付款，争取
一个明确的 scalar Jensen one-sided 常数。即使付出这个 low 常数，也不能将它
认作 actual fourth 的等式主项，或免费删除 high/low mixed words。本报告未把
这个后续候选列入已证明结果。

## 10. 防错核验与待独审状态

在内存中用 1、2、3、4 个非交换实对称 `2x2` 整数矩阵，完整枚举四词，
以精确整数核验(36)、`S_rep+S_distinct=Tr C^4`、(37)及两对 HS bound：
4 个模型共 16 个断言全部通过。此核验用于检查 partition 符号；
上述全高度、全 prime sum 及渐近量词由正文证明，不由小模型替代。

状态：推导完成，等待根节点全文独审及另一独立审查。
未把本报告注册成完整四阶常数、Lean 验证或新比例证书。
