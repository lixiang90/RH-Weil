# distinct \(2+2\) prime sector 第二独立全文审查

2026-10-07。作者：radial_review。全文读取指定研究稿，独立重算 finite
csc residual、rational spacing、fixed-\(q'\) rectangle、diagonal 平移、
commutator 与所有 \(P\)-correction。只新增本报告，不改被审稿、冻结稿、
math、脚本、输出、Goal 或 Git。

**限定 PASS，无数学阻断。**稿件支付真实 physical 同号 all-distinct
\(o(d)\)、异号和 cross 的未达目标粗估计，并给 actual finite product 的
准确余额。没有将这些 physical 付款升级为实际完整 \(O(N)\) 或 sharp
fourth budget。其 actual 粗界 \(M_{22}\ll X^{3/2}/L\) 仍超过所需量级。

## 1. 规范哈希与实际输入

canonical LF 是 CRLF、lone CR 转 LF 后的 UTF-8。

| 对象 | canonical LF SHA256 | bytes / 行 |
|---|---|---:|
| [被审研究稿](hybrid-distinct-two-two-prime-sector-research.md) | daca79cd62b61b7bd82a3b4fdf5a1a956ac0f2a1f44f7e63c0ff3f3b912cfc0d | 18946 / 585 |
| [冻结 high 输入](hybrid-high-prime-four-word-response-research.md) | 988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666 | 19170 / 572 |
| [冻结 mixed 输入](hybrid-low-high-mixed-four-word-research.md) | 71f62b2dd931cfda012e7dad9c4efcfece63f5cf1bb8ff5b466d3e2ac1ae89f9 | 22126 / 589 |
| [冻结 mixed root 审查](hybrid-low-high-mixed-four-word-review-root.md) | e9a748ce81c4779577c21b6c8677c45c043c5113770b9d6ebac088171423faed | 5464 / 98 |

保留原 \(X=T/(2\pi),L=\log X,Z=\sqrt X,d=\lfloor XL\rfloor\)、
carrier \(\tau_k=T+2\pi k/L\)、\(P=EE^*\)、真实 zero-extension。
只在结尾使用 \(d/N(T,2T)\to1\)。

外部范围是 [AF 原 frame](https://arxiv.org/html/2608.13637v2#S2)、
[MV weighted local-spacing Hilbert inequality](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)、
Chebyshev/Mertens 与固定 taper 的 regularity。
本轮不重新证明这两篇外部全文，不用 RH 或新无零域付 arithmetic 剩余。

## 2. 真正 \(22\) 正量、signed sector 与物理表示

对 Hermitian \(C_H,C_L\)，报告 (7)–(9) 准确：
\[
 A_{22}=\|C_HC_L\|_2^2,\qquad
 M_{22}=6A_{22}-\|[C_H,C_L]\|_2^2,\qquad
 2A_{22}\le M_{22}\le6A_{22}.
 \tag{R1}
\]
六个 high/low 位置选择确为四个 adjacent traces 和两个 alternating
traces。commutator 的负号可改常数，不能将远大于 \(d\) 的 product norm
独自变为 \(O(d)\)。

两步 physical features
\[
 f_{p,q}^{\sigma,\eta}
 =\phi(u)\phi(u+\sigma\log p)^2
                 \phi(u+\sigma\log p+\eta\log q)
 \tag{R2}
\]
来自真实两次 multiplier 的 product；两个负号抵消。
同号 span 是 \(\log(pq)\)，故非空项严格 \(pq<X\)；
等号只能支撑在零测度端点。异号 span 是 \(\log p\)，
不强制 \(pq\le X\)。high 正/负首步的 physical 输出位于两个半轴，
但 \(P\) 后不可据此宣称正交。

报告 (13) 由实际 finite carrier geometric sum得到，
(14) 线性于首因子的 HS 内积约定与其相位一致。
所有频率求和始终保留 \(T\) 与 finite \(d\)。

## 3. 同号 unique product 的全异付款

\(n=pq\le X\) 的 high/low 分解唯一，log-frequency span小于 \(L/2\)。
局部 spacing至少 \(1/(2n)\)，没有 grid alias。
报告 (15) 的 normalization是原 \(a_L^4L^4\)；对固定 \(q\) 用
\(\sum_{p\le Y/q}(\log p)^2\ll YL/q\)，再用
\(\sum_{q\le Y/Z}(\log q)^2/q\ll\log^2(2Y/Z)\)，严格给
\[
 E_+(Y)\ll YL^{-3}\log^2(2Y/Z),\quad
 E_+(X)\ll X/L,\quad A_+(X)\ll\sqrt X/L.
 \tag{R3}
\]
若相关 cutoff低于 \(2Z\)，集合直接为空。

在固定 \(u\) 上，两个 numerator endpoint phases吸进两套 coefficients，
而 csc 的 principal term由 weighted Hilbert支付：
\[
 (L/d)E_+(X)+d^{-1}A_+(X)^2=O(1/L).
 \tag{R4}
\]
该 features 是 \(c_nf_n(u)\)，没有 pair-dependent coefficient。
remainder在 \(|s|<L/2\) 下统一可界。
所以 (17)–(18) 是实际物理二步 norm 的准确付款。

all-distinct 的最后扣除也合法：固定 \(p\) 的 repeated-\(p\) 子族只对
\(q\le\min(Z,X/p)\) 做一侧 cutoff，energy \(O(Z/L)\)；
固定 \(q\) 的 repeated-\(q\) 子族只对 \(p\le X/q\) 做一侧 cutoff，
energy \(O(X/L)\)。分别按 \(\sum b_p^2,\sum b_q^2=O(1)\) 聚合，
都为 \(o(1)\)。它们在非diagonal部分无 double-diagonal。
因此 (19) 及其镜像是全异 physical \(o(d)\)，尚无 actual \(P\) 删除。

## 4. (22)–(24) 的有限 csc residual、alias 与真 spacing

异号 rational frequencies \(\log(p/q)\) 互异，
由整数 determinant \(pq'-p'q\ne0\) 得到报告 (21)。
若 log-ratio差小于 \(1/2\)，两个交叉整数的最大者小于 \(2pq'\)，
故距离至少 \(1/(2pq')\ge1/(2pZ)\)；较远分支直接满足同界。
真实交叉 length 可到 \(XZ\)，不是同号的 \(X\)。

这一 frequency span接近 \(L\)，故报告正确保留
\[
 \csc(\pi s/L)=L/(\pi s)+h_L(s),\qquad
 |h_L(s)|\ll
 \begin{cases}1,&|s|\le L/2,\\
 L/(L-|s|),&L/2<|s|<L.
 \end{cases}
 \tag{R5}
\]
共同 feature 含位置 \(0,\log p,\log p'\)，支撑长至多
\(L-\max(\log p,\log p')\)。
同时 \(|\log(p/q)-\log(p'/q')|\le\max(\log p,\log p')\)。
因此原 endpoint overlap准确抵消 alias singularity，给 (23)。
先 Hilbert principal，再积分后单独付 remainder；没有对 moving-pair
region免费应用 Hilbert。

主项的 weighted energy确为
\[
 \left\langle\sum\delta_{p,q}^{-1}b_p^2b_q^2|f_{p,q}^{+-}|^2\right\rangle
 \ll Z\sum_p p b_p^2\frac{L-\log p}{L}\sum_q b_q^2
 \ll XZ/L^2.
 \tag{R6}
\]
最后层积分用 \(\sum(\log p)^2(L-\log p)\ll XL\)，
不是丢去 endpoint后使用 \(O(XL^2)\)。
乘 \(L/d\) 得 normalized \(O(Z/L^2)\)；
alias remainder为 \(XZ/(dL^4)=O(Z/L^5)\)。
所以 (25)成立，却不是 \(O(d)\)。

(27) 的 repeated子族按 fixed label single-prime Hilbert同样付款。
\(\Delta_X\) 保留原 features和 carrier，为 real signed余量；
(25) 只给它 \(O(1+Z/L^2)\)，未取得所需 \(O(1)\)。

## 5. (31)–(34)：固定 \(q'\) 的近矩形及 far alias

cross frequency为 \(\log(m/p')\)，\(m=nq'=pqq'\)。
\(m\) 是 composite，\(p'\) 是 genuine high prime，两个频率集合不相交。
固定 \(q'\) 后，prime-side feature仍依赖这个固定 \(q'\)，但各自与
另一求和指标无关，Hilbert bilinear准入合法。

near region是单侧 \(nq'\le2X\)，等价 \(n\le2X/q'\)；
因为 \(q'\ge2\)，它不扩大原 \(n\le X\) 支撑。
两个集合都在 \((Z,2X]\)，log span最多 \(L/2+\log2<3L/4\)
（充分大的 \(X\)）。
union中都是不同 positive integer bases，nearest log-spacing
inverse为 \(O(m)\)、\(O(p')\)，不存在两个集合碰撞的未支付零分母。
这里用的是整数间距，不是 prime independence或平方根计数猜想。

据 (R3)，
\[
 E_m=q'E_+(2X/q')\ll X L^{-3}\log^2(4Z/q'),\qquad
 E_{p'}\ll X/L.
 \tag{R7}
\]
weighted bilinear Hilbert给两个 weighted energies的几何平均；
乘 \(L/d\) 后为 \(O(\log(4Z/q')/L^2)\)。
再乘 \(b_{q'}\)，Chebyshev layer cake严格给 (32) 的
\(\sum b_{q'}\log(4Z/q')\ll\sqrt Z/L\)。
normalized principal所以是 \(O(\sqrt Z/L^3)\)。
有限 csc remainder用 \(A_+(2X/q')\ll\sqrt{X/q'}/L\)
与 \(\sum b_{q'}/\sqrt{q'}=O(1)\)，为 \(O(L^{-3})\)。

far region \(m>2X\) 使 \(S=\log(m/p')>\log2\)。
共同 physical支撑 span至少 \(|S|\)，所以其 overlap抵消
\(S\to L\) 的 csc alias，严格有
\(|K_d(S)|\langle|ff'|\rangle\ll1/X\)。
三边真实 \(\ell^1\) mass为 \(O(X\sqrt Z/L^3)\)，付款同量级。
实际非空 paths的 \(|S|<L\)；空 paths正好为零。
这是 integrated overlap，未改 finite carrier。

repeated \(p=p'\) 部分 \(\log(qq')\ge\log4\)，同样 alias付款后为 \(o(1)\)；
repeated \(q=q'\) 的 near composite \(pq^2\le2X\)
energy \(O(X/L)\)，按 \(\sum b_q^2\) 给 \(O(1/L)\)，far也 \(o(1)\)。
因此全cross与 all-distinct \(\Gamma_X\) 相差 \(o(1)\)，(34)正确。
它仍增长，且不能把所有 \(q'\) 合并后删除 prime-side 的
\(\phi(u+\log p'-\log q')\) dependence。

## 6. diagonal、profile与整个 physical norm

镜像 high signs的 norms和 real cross相同，physical输出正交；
这给 (35) 的系数2与4。diagonal net frequency正好零，
对全实线积分做普通 \(v=u+\log p\) 平移，
\[
 \sum_{\sigma,\eta}b_p^2b_q^2
 \langle\phi(u)^2\phi(u+\sigma\log p)^4
                \phi(u+\sigma\log p+\eta\log q)^2\rangle
 =\langle d_Hd_L\rangle.
 \tag{R8}
\]
这是 (37) 的 \(2(F_++F_-)=D_{HL,L}\)；
没有对带末端 \(P\) 的一般 trace作免费 cyclic rotation。

continuous profile中 middle \(\psi^2\) 也保留；
flat积分 \(F_+=1/640,F_-=1/96,D=23/960\) 逐式相符。
一般 \(F_+\) 不是 repeated四角 \(J\)。
故 (38) 是准确的 physical分解，只包含已定义的 \(\Delta_X,\Gamma_X\)。

## 7. actual finite \(P\)、同号边界和最终 signed余额

保留报告 (41) 的同一 \(V,\mathcal E,\mathcal L\)：
\[
 P B_HP B_LP=V-\mathcal E,\qquad
 \|B_HB_LP\|_2^2=\|V\|_2^2+\|\mathcal L\|_2^2.
 \tag{R9}
\]
正交 \(P/Q\) 分解与 norm expansion给 (42)，cross sign准确。
按原 one-shift Fourier crossing proof聚合，
\[
 \|\mathcal E\|_2,\|\mathcal L\|_2
 \ll\sqrt{XZ\ell_0}/L^2.
 \tag{R10}
\]
\(\mathcal L\) 必须先插入中间 \(P+Q\)，才能得到 (44) 两项；
它没有被漏掉。相应平方除以 \(d\) 为 \(Z\ell_0/L^5\)，不趋零。
cross由 physical粗 norm给 (45)，也不能据此获取 sharp \(O(d)\)。

directional \(+\) bounds来自冻结输入的逐 shift Fourier coefficient证明
和 triangle aggregation，不能只由完整 \(B_H,B_L\) 的 norm推断。
这同样给 (46) 的准确 signed corrections。
\(pq>X\) 时 physical \(U_{++}\) 为空，actual中间 \(P\)仍可产生 crossing；
实际 coefficient product length到 \(XZ\)，alias clearance未付款。
稿件没有把 (19) 免费搬到这个 actual同号全异 sector。

最终代入 finite commutator恒等式、physical分解及 repeated预算，
(47) 的所有系数准确：\(6D-4D=2D\)、\(-8J\)、
\(12\Delta\)、\(24\Re\Gamma\)、\(-\|\mathcal K\|^2\)、
\(-6\|\mathcal L\|^2\)、\(-12\Re\langle V,\mathcal E\rangle\)、
\(6\|\mathcal E\|^2\)。
flat \(17/480\) 只是这条余额的已知项，不是新 all-distinct预算。

由 (R1)、physical \(O(XZ/L)\) 与 correction的较小 log factors，
实际粗上界 \(M_{22}\ll XZ/L\) 确实成立；
normalized \(\sqrt X/L^2\) 仍趋于无穷。
existing repeated \(13/120\) 与 signed lower bound均保持原意义，
不提供 all-distinct upper saving。

## 8. 状态、量词与有限 evidence

所有结论限定 fixed taper/profile、原 finite carrier及充分大 \(X\)，
不提供有限 numerical height阈值。整个 \(E/P\) 表示保留完整 Hilbert
space和全部 height tail，没有省去低高度或 \(J^c\)。

作者记录的19个整数矩阵 / Fraction断言只作 algebra sanity evidence；
本代理没有重跑或生成输出。它们不认证 Hilbert、prime渐近、alias或
actual Schatten预算，本报告的判断来自上面的独立解析审核。

未付的是原 \(\Delta_X\) 的 rational signed cancellation、保留共享 \(q'\)
feature的 \(\Gamma_X\)、以及 actual \(\mathcal E,\mathcal L\) 与 commutator
的同一个 signed估计。不能把不同正 majorants各自付款后声称保留 sharp常数。

最终验收：**绑定 SHA 的完整研究稿限定 PASS，无数学阻断。**
稿件是具体、可核对的 physical进展与 actual余额记录；
完整 distinct \(22\)、全四矩与比例结论仍待证明。
