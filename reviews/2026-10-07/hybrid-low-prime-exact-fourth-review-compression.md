# 原 low-prime 完整四迹独审：compression_bridge

2026-10-07。结论：**PASS，原固定 admissible profiles；不借新增 [R]**。
只新增本独审，不改被审稿、旧 notes、论文、math、Goal、脚本、output 或 Git。

全文核对
[low4 路径常数稿](hybrid-low-prime-exact-fourth-path-constant-research.md)，
canonical LF SHA256
`798947fb9cd13f25b541025f0c180945590341bbab6f55cacbcf6c50e87ee080`，
12676 bytes / 313 lines。LF hash 仅将 CRLF 与 lone CR 换成 LF。
以下独立复算原 P crossing、block gap、near/far、zero multiplicities、
general psi normalizer、weak prime measure 与 flat 积分。

## 1. 原 low crossing 可直接使用

保持原 X、L、Z=sqrt X、d=floor XL、E、P、phi、a_L 和 b_p。
原 phi、phi² 的一二阶导数 L¹ bounds 与 fixed edge taper 已明列，
不用 conditional prime-twist 输入。

更直接地，对真实 zero-extended shift s，置
`f_s(u)=phi(u)phi(u+s)`。因 phi<=1、phi 的一二阶导数 L¹ bounded，
且 `||phi'||_infty<=||phi''||_1`，f_s 的一二阶导数 L¹ 一致有界。
因此对所有原 prime shifts 都有

\[
 |\widehat f_s(\xi)|\ll\min(L,|\xi|^{-1},|\xi|^{-2}).
\]

I 上全部 integer carrier 的精确 matrix entry 为
`exp(i tau_k s) hat f_s(2pi(j-k)/L)/L`。
固定 n=j-k 的 outside pairs 数仍为 min(d,|n|)。于是

\[
 \sum_n\min(d,|n|)L^{-2}
           |\widehat f_s(2\pi n/L)|^2\ll\log(2+L).
\]

两种 shift 求和后给 `||QB_pP||_HS<<b_p sqrt(ell_0)`，不是假定
P 与 translation 交换。输出支撑 I，I 外没有遗漏的 Q 分量。
再用 Chebyshev `sum_(p<=Z)b_p<<sqrt Z/L`，确得

\[
 y=\|B_L\|\ll\sqrt Z/L,\qquad
 l=\|QB_LP\|_2\ll\sqrt{Z\ell_0}/L.
\]

这一步完全是原 finite carrier 的 individual crossing 和真实 low 质量，
不需要频带截断、canonical moving coefficients 或未知 fourth bound。

## 2. Block identity 与 projection gap

bounded selfadjoint B 按 PH⊕QH 写 `[[A,C*],[C,D]]`，
P finite rank。B² 的 PP block 为 A²+C*C，QP block 为 CA+DC。
所以

\[
 \operatorname{Tr}(PB^4P)-\operatorname{Tr}A^4
 =2\operatorname{Tr}(A^2C^*C)
  +\operatorname{Tr}(C^*C)^2+\|CA+DC\|_2^2.
\]

三项非负，分别至多 2y²l²、y²l²、4y²l²，总计<=7y²l²。
bounded D 与 finite-rank C 已保证 HS/trace 合法。
对原 B_L，gap 是 O(X ell_0/L⁴)，normalized O(ell_0/L⁵)=o(1)。
因此从 physical low4 到原 actual finite low4 的迁移已经无条件付款。

## 3. Offdiagonal near 与全部 far

四 shifted windows 同时 Fourier 分离后，每个 prime 仅携自身 unit phase；
same-product coefficient 先作真实有限聚合，multiplicity 为 pair<=2、
triple<=6。四个 window L¹ 费用 O(ell_0⁴)，固定 chi 费用 O(1)。

2+2 的 n=pq、m=rs 都<=X。先在原 tuple sum 准确剔除 n=m，再 Fourier
分离；对 union 中每个 distinct integer 只放一个 frequency，Hilbert
matrix 的 diagonal 置零。两侧 frequencies 可重叠，bilinear Hilbert
inequality 仍适用，或由同一 zero-diagonal operator 的二次型界极化得到。
union span L-log4、局部分离 c/n、两侧 E_LL<<X/L²、A_LL<<sqrt X/L²。
故 csc principal normalized O(L^-2)，remainder O(L^-4)，乘 window fees
后仍 o(1)。没有用 Hilbert 丢掉 exact zero，也没有 factor 错误的 coupled
row-dependent cutoff。

3+1 的原 chi 支持先允许把 triple n 限为<=2h<=2Z。
之后 Fourier 分离并保留该单侧 product 截断。n 为 composite、h 为 prime，
无共同 integer；union span<=L/2。E_3、E_1<<Z/L、A_3、A_1<<sqrt Z/L，
故 near normalized O(X^-1/2 ell_0⁴/L)。same-sign 4 个 prime 无 near。
其余 signs 由原 even window 与反转 signs 的共轭关系覆盖，全部16项保留。

far 先在真实 physical support 使用
`|K_d(S)|<|W|><<X^-1`；endpoint overlap 使其包括 ±L alias。
之后正质量 majorant 的三个范围确实合法：

- 2+2：全部质量 `(sum low b_p)^4<<X/L⁴`，费用 O(L^-4)。
- 3+1：support 仅要求 n<Xh；A_3(Xh)<<sqrt(Xh)/L 后乘 b_h，
  求和 `sum_(h<=Z)logh<<Z`，质量 O(X/L²)，费用 O(L^-2)。
- 4same signs：support 要求 product<X，A_4(X)<<sqrt X/L，
  费用 O(X^-1/2/L)。

这些计数包含重复，也保留 middle placements 的真实长 triples。
没有在 support 外使用 carrier bound，亦没有把 product cut 当 canonical
Lambda convolution。整个 nonzero net-frequency 族已付为 o(d)。

## 4. Zero atoms 的重数与路径权重

genuine-prime 唯一分解表明，exact S=0 只出现在2+2，两侧 prime
多重集相同。对 distinct unordered pair {p,q}，四个有符号 labels
p+、p-、q+、q- 共24个有序 words；稿中3 pairings ×4 orientations
×2 ordered(p,q) 枚举各一次。

当 p=q，six two-plus/two-minus signwords 各在三配对列表中出现两次，
所以每个 signword 各减一次。其 correction 大小至多
`6d sum_p b_p⁴=O(d/L⁴)`，因 sum_p (logp)^4/p² 收敛。
该 correction 是实际 word-dependent 权重，绝非任意减3。

A 路径的 integrand 是 phi(u)^4 phi(u+sigma Lx)^2 phi(u+eta Ly)^2。
A' 作 v=u+sigma Lx 并重命名 sigma->-sigma 后，orientation sum 等于 A。
O 为四个 corners 的 phi² 乘积。这是在 exact S=0 后的实线 integral
恒等式，不是循环删除 physical P。K_d(0)=1，故主对角准确为
`d sum_(p,q)b_p²b_q² [2G_A,L+G_O,L]+O(d/L⁴)`。

## 5. General profile、prime measure 与 flat 常数

phi 是 sqrt(psi) 配固定 edge taper。故在 scaled variable t=u/L 上，
phi² 的极限是 Psi(t)，Psi 为原 psi 的 zero-extension；A 路径为 Psi²
乘两个 shifted Psi，O 为四个 shifted Psi。a_L->a_psi=int Psi。
四个 b factors 留下 a_psi^-4，未误用 int psi² 或 Jensen normalizer。

edge strips 各宽 O(1/L)，有限 translated strips 的并集给 uniform
`G_A,L-G_A=O(1/L)`、`G_O,L-G_O=O(1/L)`，即使 flat 的 zero-extension
边界不连续也成立。bounded compact Psi 的 L¹ translation continuity
给 G_A、G_O 在 [0,1/2]² 连续。

Mertens partial summation 给
`sum_(p<=Y)log²p/p=.5log²Y+O(log(2Y))`。因此原 measure
`nu_X=sum_(p<=Z)log²p/(L²p) delta_(logp/L)` weakly趋向 x dx，
总质量1/8；固定小 primes 不形成0原子。其 tensor square 与连续路径
kernel 相配，得到

\[
 \lim d^{-1}\operatorname{Tr}C_L^4
 =a_\psi^{-4}\int_0^{1/2}\int_0^{1/2}
       xy[2G_A(x,y)+G_O(x,y)]\,dx\,dy.
\]

flat 时 A 的两个同向 orientations span=max(x,y)，两个反向 span=x+y；
O 四个 orientations 全为 span=x+y，且 x+y<=1。
独立积分：int xy=1/64、int xy max(x,y)=1/160、
int xy(x+y)=1/96，故

\[
 \mathcal C_L=4(1/64-1/160)+8(1/64-1/96)=19/240.
\]

与 scalar Jensen flat upper 3/16 的差13/120正确，两个常数对应不同
观测接口。最终结论是原 entire genuine low-prime 四迹的极限，
保持原 P 与全部 path overlap。不借新增 [R]、未知 full fourth 或 prime
pair correlation；31、distinct22、高全异和完整背景混合预算仍未付款。
因此本独审不宣布全四迹常数、新比例、新无零边界或 RH。

## 6. 正式笔记 462 的最终 hash-bound 全文独审

追加于 2026-10-07。全文核对
[462](../../notes/462-original-low-prime-fourth-path-constant.md)，canonical LF SHA256
`868adfeb0d742043f39bd08e0783d66b7a9db11316067b0b3b43d80150cdf680`，
6525 bytes / 195 lines。结论 **PASS，不借新增 [R]**。
源研究与前五节所绑定版本保持不变。

462 (6) 的 signed shift entry 已准确含原负号 -b_p，与原 Fourier phase
`exp(i tau_k s)` 一致。一般 s 下 f_s=phi phi_shift 的 derivative bounds
与 outside pairs 数给 (7)，block gap (8) 为非负且<=7y²ell²，normalized
O(log(2+L)/L⁵)。这些原 P 估计没有附带 conditional prime-twist 前件。

定理 (5) 与原完整 path sum 的 general-profile formula 一致：
phi=sqrt psi，a_psi=int psi，constant 外有 a_psi^-4。
near 中准确剔除相等 products 后 zero-diagonal Hilbert 的准入合法；
triple near cut、所有 far support 与 endpoint alias 付款保持源证明。
三种 zero pairings、同prime six signwords 每项减一次、measure (10) 的
weak limit x dx 与其 product limit 均准确。

flat 的 (11) overlap 与 (12) 19/240 已独立积分复算。
将精确 actual low4 值替代同一 low target 的 Jensen upper 3/16 合法，
但其差13/120没有自动成为零点比例改善。引 461 只固定模型及 separately
paid13，不会让 low4 定理借到 [R]。剩余 high4、31、22 与背景项明确
保留，未把 partial constants 自由相加成完整 fourth budget。
