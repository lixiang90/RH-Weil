# 491. 原高产品端周期付款与剩余带符号核心

2026-10-08。基线 main 3afd19318bf9c6fd6b3a1472929d13b4484698d3。
这是上次俯瞰复盘后的第1轮研究。沿用原数域、实际素数权、
共同参数与完整目标，不改变488—490的冻结输入。

本轮新增一个真实主项频率子族的无条件付款：
在 \(X^{1193/700}<qs\le X^{2393/1400}\) 内，共同频率窗
两端不完整模 \(q\) 周期的整个准确次弧子族，
贡献为 \(O(X^{993/1400}\log^C X)\)，指数严格低于 \(5/7\)。
完整周期以及更高产品范围仍未付；完整四矩、实际中心四阶常数、
零点比例和无零边界均保持原状态。

## 1. 准确共同端周期的付款

从[489](489-original-high-product-rational-minor-slice.md)的准确余项
\(\mathfrak K\)出发，保留两套不同删弧：
\(d\le W\) 的半径 \(W/(dS)\)，以及
\(W<d\le B\) 的半径 \(1/S\)。
它们允许全部整数平移，所以剩余mask严格模 \(q\) 周期。
先由原 \(\nu\) 的零支撑得到共同整数窗 \(J_q=[l_q,h_q]\)，
再分离共同参数；不为每个 \(s\) 另选频率端点。

固定 \(0<\eta<1/100\)，令 \(Z_2=X^{12/7-\eta}\)。
真实 \(Z<qs\le Z_2\) cap只限制随 \(q\) 移动的 \(s\) 素数区间，
与 \(n\) 无关。以 \(I_j=(jq,(j+1)q]\cap\mathbb Z\) 为网格，
完整周期的准确两端为
\[
j_0=\left\lceil\frac{l_q-1}{q}\right\rceil,\qquad
j_1=\left\lfloor\frac{h_q}{q}\right\rfloor-1.
\]
\(E_{q,S}=J_q\setminus\bigcup_{j_0\le j\le j_1}I_j\)
至多有两个长度小于 \(q\) 的端区间，含所有floor、ceil和空周期情况。

对这一实际端族直接用非负Parseval，不从完整signed界限制出子族：
\[
\sum_q b_q^2\sum_{n\in E_{q,S}\cap K}|F_{q,n}|^2
 \ll Q\log^C X,\qquad
\sum_q\sum_{n\in E_{q,S}\cap K}|G_{q,n}|^2
 \ll Q^3\log^C X.
\]
原前因子 \(S/(QX)\) 给每box费用 \(QS/X\)。
非空box满足 \(QS<qs\le Z_2\)，所有共同参数、最大标签位置、
同一空间变量和boxes恢复后只添对数。
原 \(p=s,r=s\) 及双点排除在同一端mask上重新作正能量估计，
全部为 \(O(\sqrt X\log^C X)\)。因此
\[
|\mathfrak E_\eta|\ll X^{5/7-\eta}\log^C X.
\]
取 \(\eta=1/200\)，恰有 \(12/7-\eta=2393/1400\)、
\(5/7-\eta=993/1400\)。新的准确剩余满足
\[
\mathfrak L_U=\mathfrak K_{\rm new}
 +O(X^{493/700}\log^C X)+O(X^{7/10}\log^C X)
 +O(X^{993/1400}\log^C X).
\]
在 \(Z<qs\le Z_2\) 只留完整周期，在 \(qs>Z_2\) 仍留全部旧K频率。
不重新切分已付的旧signed误差。

同一研究还从实际正频带 \(\alpha=n/q^2\asymp X/(qS)\)
的连续块间距得到统一 \(|G_{q,n}|\ll\sqrt X\log^C X\)，
保留全部twists与strict q-prefix；它单独没有支付完整K。
完整证明见[端周期研究源](../reviews/2026-10-08/hybrid-original-high-product-minor-edge-and-coherent-period-research-checkpoint-audit.md)，
不同作者审查见[端周期独审](../reviews/2026-10-08/hybrid-original-high-product-minor-edge-and-coherent-period-review-high-product.md)。

## 2. 下一项必须控制真实带符号相关

本轮把实际两腿合并为相位 \(h=qs-pr\)，保留模 \(q^2\)
的正负折叠层、unit减项以及原准确频率mask。
对同一参数 \(\lambda\) 的真实能量，精确写成
\[
E_\lambda=\sum_{q,n\in K}|F_{q,n}G_{q,n}|^2
 =D_\lambda+C_\lambda,\qquad
D_\lambda\ll Q^2X/S\,\log^C X.
\]
\(D\) 是系数对角，\(C\) 是其余全部实signed covariance；
包括只有一腿发生shift的项。\(D\) 的消费给 \(\sqrt Q\) 费用，
但不是一个原signed频率子族的独立付款。

真正足够的新输入是原共同正包络 \(w(\lambda)\) 上的一侧上界
\[
\int w(\lambda)C_\lambda\,d\lambda
 \le C Q^3X^{-j}\log^{C_0}X.
\]
它给 \(K_{\rm box}\ll[\sqrt Q+
Q\sqrt{S/X}X^{-j/2}]\log^C X\)，跨过 \(5/7\) 的条件为
\(j>2u+w-17/7\)，其中 \(Q=X^u,S=X^w\)。
旧高产品域最小门槛为 \(179/1400\)，balanced顶端为 \(4/7\)。
这是所需节省，尚未证明，也不是实际能量下界。
若改用 \(\mathfrak K_{\rm new}\)，须按其新mask重新定义 \(D,C\)；
不能从旧signed covariance上界直接截取新子族。

完整周期还有另一准确接口：
\[
H_q(a;\lambda)=\sum_{j=j_0}^{j_1}
 \varepsilon_{q,a+qj}(\lambda)G_{q,a+qj}(\lambda).
\]
保留原 \(n^{it}\) 及全部外相位后，若其真实残类能量获得
\((X/S)Q^3X^{-h}\log^C X\)，需要同样
\(h>2u+w-17/7\)。普通j-Cauchy只给 \(h=0\)；
此接口单独也不覆盖 \(qs>Z_2\) 的未付端周期。
换用F高矩但只保留旧G二矩和点界，不能自动省幂。
见[shifted covariance源](../reviews/2026-10-08/hybrid-original-high-product-minor-shifted-covariance-research-high-product.md)
及[独审](../reviews/2026-10-08/hybrid-original-high-product-minor-shifted-covariance-review-peer.md)。

## 3. 平方自由主项的零点包与角色变换

对490的实际prime/squarefree核心，准确Euler身份仍保留
\(-\zeta'/\zeta\) 的普通零点留数 \(-m_\rho\)。
本轮构造对全部 \(t\in[T/4,4T]\) 共用的有限负高度零点包，
使用entire双端核 \((x^z-z_0^z)/z\)，其中
\(x=\lfloor X\rfloor+1/2,z_0=\lfloor Y\rfloor+1/2\)，
保留零点重数和全部相位。
对应二阶Gram、四阶Gram及原系数乘积的signed shifted和均已明确。

二矩可以付polylog，但不推出新四矩：
原 \(\theta=7/8\) 密度费用下，单包自对角仍有 \(5/7\) 的四阶费用。
要改善完整增长，须对整个实际四零点相关给新一侧上界，
而非只删交叉项、改善二阶正交或局部化旧signed界。
即使得到零点包更强上界，490的完整函数差仍须保留，
其中 \(3/7\) 是误差费用，不能据零点包常数界直接宣称主项常数界。
见[零点包研究源](../reviews/2026-10-08/hybrid-original-squarefree-signed-zero-gram-research-perron.md)
及[独审](../reviews/2026-10-08/hybrid-original-squarefree-signed-zero-gram-review-peer.md)。

另一尝试完整展开conductor \(q^2\) 的primitive角色。
Gauss因子及tame正交严格给出逆元 \(c/a\) 相位，但实际系数满足
\(c\equiv-apr\pmod q\)，准确求和后恢复原 \(-jpr/q\) 相位。
因此不能仅凭出现逆元就消费独立三线性估计。
普通zeta无零前件也未提供这套角色素数和的联合预算。
见[角色变换研究源](../reviews/2026-10-08/hybrid-original-unit-band-primitive-reciprocal-transform-research-root.md)
及[独审](../reviews/2026-10-08/hybrid-original-unit-band-primitive-reciprocal-transform-review-peer.md)。

下一轮优先研究原准确mask的shifted covariance和完整周期的j相消，
争取覆盖一个非平凡实际方面比区域；零点侧以完整signed四阶为目标。
端周期付款已证明，但尚未降低完整主项预算，
所以没有触发新纪录或新边界论文的发布条件。
