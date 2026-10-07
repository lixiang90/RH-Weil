# 完整高素数四矩：一次压缩桥、物理 R 上界与真实正 nearcore

2026-10-07。作者：radial_review；compression_bridge 对压缩正差、
完整高度账本和 nearcore 计数作了独立核对。本轮只新增本报告，
没有改旧笔记、冻结论文、math、脚本、输出或 Git。

本轮交付三个可审结果：

1. 原 Hermitian high-prime 算子的完整 physical 四矩上界，一次支配
   actual finite 四矩；不需要逐 distinct word 删除三个内部 \(P\)。
   这条一般桥已在项目中出现，本报告给正差的精确恒等式和实际准入。
2. 现有 sharp Perron 零自由输入确实可经两个原 Fourier 窗乘法，
   在整条高度轴上证明
   \(\Phi_H/d\ll_a X^{2a-1}L^2+o(1)\)，\(a>\sigma_*\) 固定。
   它支付的是物理完整过程，不只是 finite matrix 的弱 op 界。
3. 原 flat/MT taper 的实际四 distinct primes 有一个正实 nearcore，
   归一化贡献 \(\gg X/L^5\)。与第二项比较，已能证明其补集
   提供大量负 signed cancellation；但是最终残余仍为幂增长。

没有证明 \(\Phi_H=O(N)\)、actual 全 high 四矩为 \(O(N)\)、新的四阶
常数、简单临界线比例或无零边界。nearcore 是 **restricted signed
sum** 的下界，绝不是完整 positive norm 的下界。

## 1. 冻结输入、原对象与来源

canonical LF SHA256 绑定：

| 输入 | SHA256 |
|---|---|
| [446](../../notes/446-uniform-prime-twists-on-the-original-gabor-frame.md) | 08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf |
| [448](../../notes/448-canonical-type-i-admission-finite-gram-and-low-prime-fourth-norm.md) | 6a7219f929cc50a721227c722fd9553eb7eba1ed9d4dd432bd971b39c2e6eafa |
| [452](../../notes/452-subquarter-padding-and-fourth-trace-stability.md) | 9e6071870a7203ce97e5489cf3178ee8681abf36014db790a8b60d8fa4895bbc |
| [453](../../notes/453-explicit-low-prime-fourth-moment-budget.md) | 0df65e79b5875fc0e5f7110ceaa05723e4db0cca0b3cc443551c7005a700ddf6 |
| [455](../../notes/455-whole-proper-power-fourth-norm-and-prime-equivalence.md) | 6bf2025dcc8f56d7b35d9c8b764ac2ff3b911a6e054bf9c496042c7f3e11ce41 |
| [456](../../notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md) | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 |
| [原 high 四词报告](hybrid-high-prime-four-word-response-research.md) | 988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666 |

原 frame、taper、sharp 权重取
[AF v2 §2](https://arxiv.org/html/2608.13637v2#S2)。weighted second/fourth
mean value 使用
[Montgomery–Vaughan, Hilbert's inequality](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)；
nearcore 只另用经典 PNT 在固定比例素数区间的计数，原证明见
[Selberg, 1949](https://www.math.lsu.edu/~mahlburg/teaching/handouts/2014-7230/Selberg-ElemPNT1949.pdf)。
不以该固定比例计数代替 microscopic prime-product 相关。

固定原 \(\chi,\psi\)，令

\[
 X=T/(2\pi),\quad L=\log X,\quad d=\lfloor XL\rfloor,\quad
 \tau_k=T+2\pi k/L,\quad I=[-L/2,L/2].
 \tag{1}
\]

原 \(\chi\) 在 \(s\le0\) 为零，在 \(s\ge1\) 为 1；
\(\phi=\chi(L/2+u)\chi(L/2-u)\sqrt{\psi(u/L)}\)。
\(\phi\) 偶、非负、\(C_c^2\)，\(0\le\phi\le1\)，
\(a_L=L^{-1}\|\phi\|_2^2\to a_\psi>0\)。
以下保留这个平滑 taper；没有换成裸 indicator。

\[
 E e_k=L^{-1/2}1_I e^{i\tau_k u},\quad
 P=EE^*,\quad Q=1-P,\quad F=\mathscr F M_\phi E.
 \tag{2}
\]

\(\mathscr F\) 为原 unitary Fourier。\(E\) 是 exact isometry，\(F\)
是 contraction。只在最后使用 \(d/N(T,2T)\to1\)。

写 \(\mathcal P_H=\{p:\sqrt X<p\le X,\ p\text{ prime}\}\)，

\[
 b_p=\frac{\log p}{a_LL\sqrt p},\quad \ell_p=\log p,\quad
 B_p=-b_pM_\phi(R_{\ell_p}+R_{-\ell_p})M_\phi,
 \quad B=\sum_{p\in\mathcal P_H}B_p,\quad C=E^*BE.
 \tag{3}
\]

每个固定 \(T\)，这是 finite bounded Hermitian sum；\(R_s\) 是真正的
zero-extended 平移。没有把 physical translations 周期化。

## 2. 一次压缩上界与正差的精确表达

一般地，设 \(E:\mathbf C^d\to\mathcal H\) isometry、\(B=B^*\) bounded。
令

\[
 A=E^*BE,\quad K=(QBE)^*(QBE),\quad Z=QB^2E.
 \tag{4}
\]

则

\[
 E^*B^2E=A^2+K,
\]

\[
 \boxed{
 \operatorname{Tr}(E^*B^4E)-\operatorname{Tr}A^4
 =\|Z\|_{\rm HS}^2+2\operatorname{Tr}(A^2K)+\operatorname{Tr}K^2
 \ge0.\ }
 \tag{5}
\]

证明：在 \(B^2E\) 中按 \(P+Q\) 分解，

\[
 \operatorname{Tr}(E^*B^4E)
 =\|B^2E\|_{\rm HS}^2
 =\operatorname{Tr}(A^2+K)^2+\|Z\|_{\rm HS}^2.
\]

有限迹中 \(\operatorname{Tr}(A^2K)\ge0\)，因为 \(A^2,K\succeq0\)。
这既证明一侧不等式，也明确所有 projection discrepancy 的总符号。
另一证明是对 \(A\) 的 eigenbasis 用 \(B\) 的 scalar spectral Jensen，
无需错误地假设 \(x^4\) operator-convex。

令

\[
 \Phi_H:=\operatorname{Tr}(E^*B^4E)=\|B^2E\|_{\rm HS}^2.
 \tag{6}
\]

实际 (3) 满足全部前件；不需要 \(B^4\) 在 whole \(\mathcal H\) 上
trace class，也不需要随 \(T\) 一致 bounded 的 \(\|B\|\)。
若推广至 unbounded self-adjoint \(B\)，range \(E\subset\operatorname{Dom}B^2\)
是充分前件，右侧须以 \(B^2\) quadratic form 解释；本项目没有该障碍。

**Repo 检索结果。**448 §5、453 §4、455 §4 已把 scalar spectral
Jensen 用于原 finite frame；high 四词报告第 539–544 行已经明确
\(\operatorname{Tr}C^4\le\Phi_H\) 是完整 physical upper 的充分路线。
这里不声称新发现一般压缩定理。新增的是 (5) 的总正差账本及后续
完整 physical 上界/nearcore 的可核验推导。

若另证 \(\Phi_H\le K_Hd+o(d)\)，则 actual high 四矩立即有同一
**upper**。不必为每个 all-distinct word 逐个删除三个 \(P\)，也不必
证明 (5) 的 gap 为 \(o(d)\)。这不能推出同 sharp 常数的 equality。

## 3. 完整高度保留及 tail 的实际范数

定义原高素数多项式及归一化乘子

\[
 Q_H(t)=\sum_{p\in\mathcal P_H}\frac{\log p}{\sqrt p}p^{it},
 \quad m(t)=-\frac{2}{a_LL}\operatorname{Re}Q_H(t).
 \tag{7}
\]

则 \(B=M_\phi\mathscr F^*M_m\mathscr FM_\phi\)，
\(C=F^*M_mF\)；正规化和 sharp prefix 与 (3) 完全相同。

取 \(J_1=[T/2,3T]\)。原 Fourier decay 与 carrier 的距离给

\[
 \|1_{J_1^c}F\|_{\rm HS}^2
 \ll\frac{d}{LX^3},\qquad
 \|m\|_\infty\ll\frac{\sqrt X}{L}.
 \tag{8}
\]

对 \(C_{\rm tail}=F^*1_{J_1^c}M_mF\)，以 \(1_{J_1^c}F\) 的 contraction
和 scalar Jensen 得

\[
 \|C_{\rm tail}\|_{S_4}^4
 \le\operatorname{Tr}(F^*1_{J_1^c}M_{m^4}F)
 \ll\frac{d}{XL^5}.
 \tag{9}
\]

因此 normalized fourth-root tail 无条件趋零。这里没有把
\(\operatorname{Tr}C^4\) 拆成两个无 cross terms 的高度四迹。
如果将来 \(\|C\|_4=O(d^{1/4})\)，才由 reverse triangle 或 telescoping
进一步推出中心/whole total fourth difference 为 \(o(d)\)。

physical \(\Phi_H\) 本身从整条 height 轴准确 Fourier conjugation 而来，
没有预先删去低高度 coherent peak。以下直接为 physical 两次作用
支付该尾。

## 4. 已有零自由 R 输入可付的完整 physical 上界

本节严格以 446 的原 sharp Perron、452 的已明列全族输入为 [R]。
固定

\[
 \sigma_*<a<1,\qquad \sigma_*>3/4.
 \tag{10}
\]

\(a-\sigma_*\) 在 \(T\) 之前固定。原 \(-\zeta'/\zeta\) Perron 给
全部 \(t\in[T/4,4T]\) 的 full sharp \(\Lambda\) 前缀
\(O_a(X^{a-1/2}L^2)\)，并保留 principal residue
\(x^{1/2+it}/(1/2+it)\)。

从 full \(\Lambda\) 到 genuine high primes，精确使用

\[
 Q_H=Q_{\Lambda,\le X}-Q_{{\rm pr},\le\sqrt X}-Q_{{\rm pp},\le X}.
\]

Chebyshev 给第二项 \(O(X^{1/4})\)，455 给第三项 \(O(L)\)。因 (10)，

\[
 m_R:=\sup_{t\in[T/4,4T]}|m(t)|
 \ll_a X^{a-1/2}L+X^{1/4}/L+1
 \ll_a X^{a-1/2}L.
 \tag{11}
\]

这是原绝对 height；没有把它误用成 four-cycle 的小时间差。
若讨论别的 \(\sigma_*\le3/4\)，上面低项的吸收须重新支付，不默认成立。

置 \(T_\phi=\mathscr FM_\phi\mathscr F^*\)、
\(T_{\phi^2}=\mathscr FM_{\phi^2}\mathscr F^*\)。准确恒等式是

\[
 \mathscr FB^2E=T_\phi M_mT_{\phi^2}M_mF.
 \tag{12}
\]

左侧 \(T_\phi\) contraction 可舍去。将最后的 \(F\) 分成
\(1_{J_1}F+1_{J_1^c}F\)；后半由 (8) 两次乘子付费，其 HS 平方至多

\[
 \|m\|_\infty^4\|1_{J_1^c}F\|_{\rm HS}^2
 \ll\frac{d}{XL^5}.
 \tag{13}
\]

记 \(G=M_m1_{J_1}F\)。原 grid bound
\(\sum_k|Fe_k(t)|^2\ll L\)，加 weighted MV 二矩

\[
 \int_{J_1}|Q_H(t)|^2dt
 \ll X\sum_p\frac{(\log p)^2}{p}+\sum_p(\log p)^2
 \ll XL^2
\]

给

\[
 \|G\|_{\rm HS}^2\ll d.
 \tag{14}
\]

它没有四矩前件。取 \(J_2=[T/4,4T]\)。原
\(\|(\phi^2)''\|_1=O_{\chi,\psi}(1)\) 给卷积核
\(\widehat{\phi^2}(t-s)/(2\pi)=O(|t-s|^{-2})\)。
\(J_1\) 与 \(J_2^c\) 相距 \(\asymp X\)，故 Schur 直接给

\[
 \|1_{J_2^c}T_{\phi^2}1_{J_1}\|_{\rm op}\ll X^{-1}.
 \tag{15}
\]

在 \(J_2\) 输出用 (11)，在 \(J_2^c\) 用 (8)、(15)：

\[
 \|M_mT_{\phi^2}G\|_{\rm HS}^2
 \ll m_R^2d+\frac{d}{XL^2}.
\]

最后 HS triangle 只改变固定常数。于是证明

\[
 \boxed{\quad
 0\le\frac{\Phi_H}{d}
 \ll_a X^{2a-1}L^2+\frac1{XL^2}+\frac1{XL^5}.
 \quad}
 \tag{16}
\]

这是完整 physical 一侧界，继而也支配 actual 四矩。可以取 452 已
实际准入的 \(a=87497/100000\)，但仍有正幂 \(2a-1=0.74994\)。
不能把 [R] 的零自由区或者 \(\|BE\|_2^2=O(d)\) 当作
\(\Phi_H=O(d)\)。无零自由输入时，现有
\(\|B\|\ll\sqrt X/L\)、\(\|BE\|_2^2=O(d)\) 仅给
\(\Phi_H/d\ll X/L^2\)。

## 5. 真正的 physical signed 算术对象

每个 high step 长度 \(>L/2\)，相邻同号的物理两步支撑为空。
四步只有 \(+-+-\) 与 \(-+-+\) 能存活。
对 ordered \(p,q,r,s\in\mathcal P_H\)，设

\[
 a_p=\log p,\quad S=\log(pr/(qs)),\quad
 S_0=0,\ S_1=a_p,\ S_2=a_p-a_q,\ S_3=a_p-a_q+a_r,\ S_4=S,
\]

\[
 w_L(p,q,r,s)=\frac1L\int_I
 \phi(u)\phi(u+S)\prod_{j=1}^3\phi(u+S_j)^2du,\quad
 K_d(z)=\frac1d\sum_{k=0}^{d-1}e^{i\tau_kz}.
 \tag{17}
\]

因 \(\phi\) 偶，反向 pattern 经 \(u\mapsto-u\) 的 weight 相同，
kernel 共轭。没有对 physical traces 作未付的 cyclic rotation。
准确 whole physical 账本为

\[
 \boxed{\quad
 \frac{\Phi_H}{d}
 =2\operatorname{Re}\sum_{p,q,r,s\in\mathcal P_H}
 b_pb_qb_rb_sK_d(S)w_L(p,q,r,s).
 \quad}
 \tag{18}
\]

全部 sharp primes、taper 和 finite carrier 保留，外侧 \(E\) 未删除。
若 weight 非零，\(|S|<L/2\)：\(S\ge L/2\) 使
\(S_3=S+a_s>L\)；\(S\le-L/2\) 使 \(S_1-S>L\)。
所以 alias 由真正的五点支撑排除，而不是替换成无限 sinc。
对非零 \(S\)，准确有限几何核给

\[
 |K_d(S)|\ll\min\{1,L/(d|S|)\}\ll1/(X|S|).
 \tag{19}
\]

四 distinct 时 \(pr=qs\) 不可能，故剩余确为非零 determinant
\(\Delta=pr-qs\) 的原 weighted signed sum。
(18) 的 \(O(1)\) upper 是充分待付输入；不是任意四矩名词的替代品。

## 6. 单根计数给的实际 absolute 预算仍然增长

这里记录一个可核接口，说明 456 的平方根计数不能免费变成
full distinct 付款。对奇 prime \(q\nmid r\)，整数 \(p\in[P,2P]\)、
\(1\le s\le X\)，剔除 \(pr=qs\)。乘以 \(r\) 在 mod \(q\) 上置换
非零 residues，每个 residue 只有一根。因此

\[
 \sum_{P\le p\le2P}\sum_{\substack{1\le s\le X\\pr\ne qs}}
 \frac1{|pr-qs|}
 \ll(P/q+1)\log(2X).
 \tag{20}
\]

证明和 456 progression argument 相同：对每个 \(p\) 先分最近项
及 \(q\)-间距 tails；完整 residue blocks 的最近项 harmonic sum
为 \(O(\log q)\)。\(q\mid p\) 分支的 zero center 剔除后另付
\(O(\log X/q)\)，不把它赋予非零 residue。

在 \(pr/(qs)\in[1/2,2]\)，

\[
 b_pb_qb_rb_s|K_d(S)|\ll\frac1{X|pr-qs|},\qquad
 w_L\le\frac{\log(X/M)}L,\quad M=\max(p,q,r,s).
 \tag{21}
\]

只在 positive majorant 中排序，令 \(p\) 为最大、\(q\le s\)；
有限 label multiplicity 不旋转 operator。取 \(p\asymp P,r\asymp R,
q\asymp Q\)，near 强制 \(Q\gg R\)、\(Q\ll\sqrt{PR}\)，并且
\(R\le P\)。q、r 仍是真 prime，count \(O(Q/L),O(R/L)\)，
p、s 才为上界扩大成 integers。由 (20)，每箱 determinant sum
\(\ll PR/L\)。\(Q\) 箱数 \(O(1+\log(P/R))\)，而

\[
 \sum_{R\le P}R(1+\log(P/R))\ll P.
\]

再对 \(P\) dyadic 求和，(21) 给归一化 near absolute 费用
\(O(X/L^2)\)。far 用 (19)、\(\sum_pb_p\ll\sqrt X/L\) 给
\(O(X/L^4)\)。这与前节 coarse physical norm budget 相容。
这里有两个独立 prime 自由变量 \(q,r\)；与 repeated \(p^2=qr\)
的单模数付款相比，不能删除其额外行计数而声称 \(O(1)\)。

## 7. 实际 four-distinct 正 nearcore 的定量下界

以下无条件结论使用固定 profile 的 endpoint 正性：
\(\min_{[-1/2,1/2]}\psi>0\)。AF 的 flat 和 MT
\(\psi(v)=\cos(\sqrt2v)\) 都满足。若 profile 在 endpoint 消失，
必须重新计算其幂损失，不能沿用本节常数。

固定 \(C>4\)、\(0<w<1/10\)，令
\(\beta=e^{-C}\)、\(\alpha=\beta e^{-w}\)，

\[
 \mathcal A_X=\{p:\alpha X\le p\le\beta X,\ p\text{ prime}\}.
\]

足够大的 \(X\) 时 \(\mathcal A_X\subset\mathcal P_H\)；PNT 给
\(m=|\mathcal A_X|\asymp X/L\)。所有 \(pr\) ordered products 位于
\([\alpha^2X^2,\beta^2X^2]\)。固定

\[
 0<\delta<\min\{\alpha/4,\alpha^2/(100\pi)\}.
 \tag{22}
\]

按宽 \(\delta X\) 分箱，箱数 \(O(X)\)。Cauchy 给同箱 ordered
\((p,r),(q,s)\) 的个数

\[
 \sum_j n_j^2\ge\frac{m^4}{O(X)}
 \gg X^3/L^4,\qquad |pr-qs|\le\delta X.
 \tag{23}
\]

所有重复 tuples 只有 \(O(m^2)\)，须明确剔除：

- 若正负 pairs 共享 prime，例如 \(p=q\)，则
  \(p|r-s|\le\delta X\) 强制 \(r=s\)，因 \(\delta/\alpha<1\)。
- 若内部 \(p=r\)，固定 \(p,q\) 后，\(s\) 的允许整数区间长度
  \(2\delta X/q<1\)，至多一个；\(q=s\) 同理。
- 其它共享位置对称，有限 union 仍 \(O(m^2)\)。

因此 (23) 仍留下 \(\gg X^3/L^4\) 个四 distinct tuples。
它们不是 exact multiplicative diagonal。

对这些 tuples，

\[
 |S|\le\frac{\delta}{\alpha^2X},\qquad
 \tau_k<4\pi X,\qquad \operatorname{Re}K_d(S)\ge1/2.
 \tag{24}
\]

路径五点包含两个 low positions \(0,S_2\)，两个 high positions
\(S_1,S_3\)，和 tiny \(S_4\)。其中
\(S_2\in[-w,w]\)、\(S_1,S_3\le L-C+w\)，
所有 low positions 至少 \(-w\)，故 span 至多 \(L-C+2w\)。
取

\[
 u\in[-L/2+1+w,\,-L/2+C-1-w].
\]

此区间固定正长 \(C-2-2w\)，每个 \(u+S_j\) 距两端至少 1，
原两个 \(\chi\) 因子均为 1，原 \(\phi\ge c_\psi>0\)。从而

\[
 w_L(p,q,r,s)\ge c_{\chi,\psi,\alpha,\beta}/L.
 \tag{25}
\]

若用一般过渡宽度 \(h_\chi\) 的 fixed \(\chi\)，应先取
\(C>2h_\chi+2w+1\)；单有 \(C^2\)、非负和紧支不够保证 (25)。
这里使用的是实际 taper 的 flat bulk，未以裸 indicator 替换 \(\phi\)。

每个 \(b_pb_qb_rb_s\asymp X^{-2}\)。记 (18) 限制到这一真实
nearcore 的 paired real sum 为 \(\Psi_{\rm near}\)，(23)–(25) 证明

\[
 \boxed{\quad \Psi_{\rm near}\gg X/L^5\longrightarrow\infty.\quad}
 \tag{26}
\]

因此仅靠逐 tuple 取绝对值、只估 near 且舍掉其补集，不可能经
(18) 得到 \(O(1)\) physical upper。这里并未反证完整
\(\Phi_H=O(d)\)；它可能靠其它 signed frequencies 的抵消成立。
也未反证 actual \(C\) 的有界四矩，后者还可小于 \(\Phi_H\) 的
正 compression gap。

## 8. 已有 R 确实支付了一部分 signed cancellation

令 \(\Psi_{\rm rest}\) 为 (18) 去掉 (26) nearcore 后的完整实数和。
没有改窗口、carrier 或 coefficients。恒等式为

\[
 \Psi_{\rm rest}=\Phi_H/d-\Psi_{\rm near}.
\]

在固定 \(a\in(\sigma_*,1)\) 的 [R] 下，(16) 给

\[
 X^{2a-1}L^2=o(X/L^5).
\]

所以 (26) 与 (16) 联合 **已经严格推出**

\[
 \Psi_{\rm rest}\le-cX/L^5
 \qquad(X\text{ sufficiently large}),
 \tag{27}
\]

常数依赖先固定的 band/profile/gap。这是 actual physical coefficients
中的大幅负 signed cancellation；不是用改造过的 centered mask
或者 arbitrary phases 造的模型反例。

但残余 \(\Phi_H/d\) 仍只被 (16) 的正幂控制。所缺不是再确认
“存在抵消”，而是在整个 balanced product 区域保留它，继续把
残余从 \(X^{2a-1}L^2\) 降为 \(O(1)\)，并给所需常数。
(27) 不能当作 target-independent uniform \(O(1)\) fourth budget。

## 9. 普通短窗均值与 detector R 的准确未覆盖处

未压缩 \(Q_H^2\) 的 prime-product 系数是
\(c(pq)=2\lambda_p\lambda_q\)（\(p\ne q\)）、
\(c(p^2)=\lambda_p^2\)，其中 \(\lambda_p=\log p/\sqrt p\)。
令 \(S_H=\sum\lambda_p^2\)、\(R_H=\sum p\lambda_p^2\)。weighted MV 给

\[
 \int_A^{A+H}|Q_H(t)|^4dt
 =H\left(2S_H^2-\sum_p\lambda_p^4\right)
  +O(R_H^2),
\]

\[
 S_H=\frac38L^2+O(L),\quad R_H\ll XL,\quad
 \sum_n n|c(n)|^2=2R_H^2-\sum_p(\log p)^4\ll X^2L^2.
 \tag{28}
\]

在 \(H\asymp X\)，要求一侧 \(O(XL^4)\) 时，现有误差相对预算是
\(X/L^2\)，而非 \(o(1)\)。短到 \(H<X\) 不改善这个费用。
不能把 products \(pr\le X^2\) 当作低通道的 \(pr\le X\) 再调用 453。
此外物理 (18) 的 coupled path profiles 不等于 (28) 的 unweighted
constant profile；本报告没有把二者认成同一个 exact main term。
若能独立证明完整 scalar high fourth \(O(XL^4)\)，它可通过原
scalar Jensen 另一路直接上界 actual \(C\)；目前该输入同样未付。

原 math 的 marked/plain detector 是另一个准确 family/coefficient
合同。这里的待估 columns 是真实 two-prime products、phase
\(e^{it\log(pr/(qs))}\)、原 five-point profile 和 absolute finite grid。
未构造将它们送入同一个 residue-character row、conductor、zero masks
及 strict width 的合法映射。因此不能直接引用原 inverse/plain
moments 作为 (18) 的 bound。全族零自由性在本轮只经已明确的
canonical sharp \(-\zeta'/\zeta\) 接口使用，费用见 (11)–(16)。

## 10. 可接入原比例链的桥与下一付款对象

若将来给原 (18) 一侧 \(\Phi_H/d\le K_H+o(1)\)，(5) 就一次完成
actual full high 的 upper，不再索取每个 distinct projectiondifference
的 equality。已有 low 的 \(S_4=O(d^{1/4})\)、背景的 bounded op、
455 的 proper-power 小 \(S_4\)，可由 Schatten Minkowski 给整个原
response 的某个有限 fourth upper；无需预设各 mixed words 单独小。
若要 sharp 比例常数，仍需保留完整正规化并重新评估该 coarse
合并的常数，不能简单相加 repeated/low constants。

当前可行动的算术输入已经具体化：对 (18) 的 coupled original
weights 证明 **signed product-detector residual 的净 \(O(1)\) upper**，
或者付更弱但足够的 full scalar high fourth upper。任何新使用的
短区间/平均素数相关，必须处理 \(pr\asymp qs\) 的真实长度 \(X^2\)、
分辨率 \(O(X)\)、carrier \(t\asymp X\)、原 sharp weights 和跨 bins
抵消；不能仅重新给单个 determinant 的 spacing 或正 mass bound。

本轮新增的是完整物理 R 付款、真实正 nearcore 和已迫出的负补集
抵消；净 \(O(N)\)、完整 fourth constant 和比例改进仍开放。
