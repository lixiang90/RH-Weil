# 493. 连续参考项付款与原载体的近相关核心

2026-10-08。基线 main cd95587e3120cbc1b93c7ca595a56f861f23c18d。
这是上次复盘后的第3轮，接续[492](492-original-coherent-period-energy-and-product-ceiling.md)。
保留原数域、真实素数函数、原正时间权与完整目标。

本轮付清两项辅助贡献：同一实际频率mask上的双连续腿参考项为
\(O_{\phi,\chi}(\log^{-3}X)\)；真实prime/squarefree主项在原时间权下，
阈值外全部四阶系数相关为
\(O(X^{2-\sqrt{8\pi}}\log^4X)\)。
剩余分别是真实素数测度相对连续测度的联合偏差，以及平方自由系数的
完整signed近相关。两者均未得到新的省幂。
原完整四矩、中心常数、零点比例和无零边界未改善，不发布新纪录论文。

证明见[连续参考项源](../reviews/2026-10-08/hybrid-original-product-cell-continuous-main-and-prime-deviation-research-checkpoint-audit.md)、
[原载体四阶源](../reviews/2026-10-08/hybrid-original-squarefree-carrier-fourth-near-research-perron.md)；
两份源的不同作者全文审查见[综合独审](../reviews/2026-10-08/hybrid-original-reference-and-carrier-near-review-high-product.md)。

## 1. 同一实际mask上的连续参考项

写 \(X=T/(2\pi)\)、\(L=\log X\)、\(N_L=a_LL\)。
实际内腿仍是 \(\sum_p(\log p)/(N_L\sqrt p)\,\delta_p\)。
定义参考测度 \(d\mu_0(p)=dp/(N_L\sqrt p)\)，并在实际的
q-prefix、dyadic区间、产品窗g及同一个空间变量u上替换两条内腿。
这是一个明确的连续参考项，未断言素数与它的偏差已小。
外q、s仍为实际素数，原频率删弧与完整正时间权不变。

对 \(PR\asymp qs\)、原支持内 \(n\asymp qX/s\)，
连续积分相位 \(npr/q^2\) 在缩放矩形上的大小为 \(X\)。
分别沿p、r分部积分一次，保留所有sharp角、边和bulk，得到
\[
 |G_0(q,s,n,u;P,R)|
 \ll_\phi \frac{\sqrt{PR}}{N_L^2X^2}.
\]
这里只用原C²空间profile给出的 \(\|\phi'\|_\infty\)；
混合导数对每条独立腿只求一次导数。没有要求额外Mellin加权矩。
区间被q截得很短也不产生反长度损失。

原正时间权准确给
\[
 \sum_n\frac{2\pi s}{q}\nu(2\pi sn/q)\ll_\chi1.
\]
保留整数计数的 \(+1\)，再用O(L)个dyadic产品对和
\(\sum_{q,s}b_qb_s\sqrt{qs}\ll X^2/N_L^2\)，得到
\[
 \boxed{|K_0|\ll_{\phi,\chi}L/N_L^4\ll_{\phi,\chi}L^{-3}.}
\]
该估计直接作用于当前准确mask及其子mask，含端周期和完整周期；
没有从旧signed全界截取子族。
但它付的是完整连续参考值，实际prime主项并没有被这一计算替代。

## 2. 必须先恢复完整参考项的相消

连续产品测度pushforward是 \(c(k)\,dk\)，不是在整数k上采样c(k)。
对于cell \(k=qz+v\)，参考系数准确是
\[
 B^0_{q,z,h,I}=\int_0^q c(qz+v)D_I(v)(v/q)^h\,dv,\qquad
 D_I(v)=\sum_{j\in I}e(-jv/q).
\]
原正高度给 \(j\ge1\)。若cell内密度为常数 \(c_z\)，
h=0的完整周期积分为零，但
\[
 B^0_{q,z,1,I}=-\frac{qc_z}{2\pi i}\sum_{j\in I}\frac1j.
\]
在 \(j\asymp X/S\)、窗长同阶时，这个h=1端点项是 \(qc_z\) 尺度。
所以完整 \(G_0\) 很小，不能推出每个Taylor阶单独都很小。
[492](492-original-coherent-period-energy-and-product-ceiling.md)的逐h能量节省仍是充分旁路，
并非所有联合方法的必要输入；不能把连续主项的相消拆散后再次索取。

按定义严格有 \(K_{\rm pr}=K_0+K_{\rm dev}\)。
固定公共参数时，真实cell偏差是原整数素数乘积和减去上述连续积分。
若按两条腿各自减去 \(\mu_0\) 展开，必须保留两个mixed项和一个double-deviation项，
以及全部实际s删除点、同u和q-prefix；不能只保留double项。
本轮未付这三个项的联合预算，普通素数前缀误差也没有自动控制它们。
下一步应在完整参考项已经恢复的顺序中估计真实signed偏差。

## 3. 原时间权付清平方自由四阶的远相关

保持[490](490-original-weighted-mobius-squarefree-conditional-remainder.md)的实际主项
\(R(t)=\sum_{Y<n\le X}r_n n^{it}\)，含原prime/squarefree负系数、
共同乘积两端和所有方面比。准确平方为
\(R(t)^2=\sum_\ell g_\ell\ell^{it}\)，其中
\[
 \sum_\ell|g_\ell|\ll XL^2,\qquad
 D_\nu=\sum_\ell g_\ell^2\ll L^{16}.
\]
原固定概率测度的时间核是
\[
 \Psi_T(u)=e^{iTu}\Gamma(s_Tu)\frac1d\sum_{k=0}^{d-1}e^{ik\eta u},
 \quad s_T=T/\sqrt L,\quad d=\lfloor XL\rfloor,\quad\eta=2\pi/L.
\]
保留全部floor、相位和几何因子。
原阈值 \(\Delta=1024L^{5/2}/X\) 给
\(s_T\Delta=2048\pi L^2\)，从原 \(\Gamma\) 衰减严格得到
\[
 |\Psi_T(u)|\le X^{-\sqrt{8\pi}}\quad(|u|\ge\Delta).
\]
因此全部真实远相关绝对付款为
\[
 \boxed{|F_\nu|\ll X^{2-\sqrt{8\pi}}L^4,}
\]
并且准确地
\[
 M_{\nu,R}=\int\nu|R|^4=D_\nu+C_{\nu,\mathrm{near}}+F_\nu.
\]
若完整signed近和的一侧上界为 \(O(X^{B+\epsilon})\)、固定 \(B\ge0\)，
即可得到同一原载体的四矩增长上界。这个近和尚未改善。
在 \(\ell\asymp X^2\) 顶端，近区仍允许
\(|\ell-\ell'|\ll XL^{5/2}\)；它不是只剩几个移位的对角问题。
对角的polylog上界也不是所需的常数级中心预算。

保持[453的固定有限零点包](../reviews/2026-10-08/hybrid-original-squarefree-signed-zero-gram-research-perron.md)，
四阶核准确是同一 \(\Psi_T(u_1+u_2-u_3-u_4)\)，不是四个独立二阶核。
原载体内部的正密度下界仍给单零点核四矩 \(X^{4\beta-2}/T\)；
名义7/8与既有密度费用仍给5/7的四阶自对角费用。
系数远相关付款不能直接搬到某个零点四重和子域。

由 \(\nu\ll T^{-1}1_J\)，490的完整函数差合法运输到该载体：
普通全高度 \([R_\theta]\) 前件下误差 \(c_\theta=1-1/(2\theta)\)，
名义7/8仍为3/7，已有完整增长合同下的矩差仍为9/14。
这些指数是已有费用的运输。
单个载体的上界不能反推任意canonical J四矩，进一步消费须另付统一覆盖合同。

## 4. 外部短区间工具的准确适用范围

本轮全文审读了Matomäki–Teräväinen的
[Theorem 1.4及其§5.2证明](https://arxiv.org/html/1911.09076v2)。
该全E2短区间定理要求固定 \(\theta>0.55\)、区间长度至少 \(N^\theta\)；
其证明的主项来自一个小素因子，固定幂大小的较小素因子落在误差中。
当前未付的 \(N=PR\asymp QS>X^{12/7}\)、\(P,R\le X\) 给
\(\min(P,R)\gg N^{5/12}\)，而cell内部相位的半周期长度为
\(N/X\ll N^{1/2}\)。故该定理既不覆盖所需频率尺度，
也不能将其全E2主项直接限制到这里的真实大因子dyadic对子。
这只是这篇原始文献的合同审查，没有宣称它是当前全部E2结果的最优状态。

本轮使瓶颈更具体：连续mean本身已付，不能再逐展开阶要求它单独消失；
远四阶相关也已付，真正要估计的是完整真实偏差和近相关。
下一轮优先尝试同一mask上的signed prime-product偏差预算，
或同一原载体的平方自由近相关一侧预算，并保留全部误差运输与覆盖条件。
达到第4轮可以提前复盘，默认第6轮复盘；本轮不重置计数。
