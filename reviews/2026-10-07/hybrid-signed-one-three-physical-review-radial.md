# signed physical 13 联合共振推导：独立全文审查

2026-10-07。审查者 radial_review。

结论：**限定 PASS**。全文逐式逆审后，(8)–(23) 确实支付原零延拓
物理四词的每个 13 placement 为 o(d)，包含 repeated/distinct labels、
全部 signs、近共振、middle-far、alias 和 Fourier ghosts。
没有发现会阻断该物理结论的数学漏洞。

通过范围不含实际 finite-matrix 13 四词为 o(d)；
三个内部 P 的 signed aggregate 仍是精确、未付的余额。
原 31、distinct22、完整四阶常数、零点比例和无零边界均未由此闭合。

## 1. 证据对象与源码范围

下列 SHA-256 对 UTF-8 文本作 CRLF/lone CR→LF 规范化后计算。

| 对象 | canonical LF SHA-256 |
|---|---|
| hybrid-signed-one-three-physical-resonance-research.md | 0f7c0146e984c49d84fc057394aed1ab9ace658ae5b775b931bfd359a4c47bac |
| hybrid-one-three-mixed-prime-sector-research.md | 5db2c614ab9d009a15a70f4e0639b95df2d59a6b56bd752216537fcf71e2b405 |
| hybrid-distinct-two-two-prime-sector-research.md | daca79cd62b61b7bd82a3b4fdf5a1a956ac0f2a1f44f7e63c0ff3f3b912cfc0d |
| notes/446-uniform-prime-twists-on-the-original-gabor-frame.md | 08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf |
| notes/448-canonical-type-i-admission-finite-gram-and-low-prime-fourth-norm.md | 6a7219f929cc50a721227c722fd9553eb7eba1ed9d4dd432bd971b39c2e6eafa |
| pinned OpenAI/math September-30-2026/build/paper.tex | 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 |

被审对象为 16,387 canonical bytes、389 行，位于本报告同目录。
完整读取该对象，并核对原 AF physical window、finite carrier、
两份 frozen mixed 报告的相关前件和446 sharp Perron 原式。
原 math 固定提交为 adc7f1241b42e322a6451854ab7e4b4c146bf78a；
其 fixed-gap logarithmic-control 输入仍按 [R] 使用，本审查不独立
认证原零自由论文全稿。

Hilbert 的引用输入是
[Montgomery–Vaughan Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
的局部间距实线形式；其双线性推论用于互不相交的频率子集。
原窗及有限 frame 采用
[Alpöge–Furman v2 §2](https://arxiv.org/html/2608.13637v2)。
下文主要是对这些输入的具体准入及本稿新估计的独立核算。

没有修改被审文件、前置证据、math、脚本、输出或 Git。
本审查没有用有限数值实验代替连续 Hilbert/Perron 分析。

## 2. 原物理核、carrier、signs 和 S1 准入

对一项 signed translation，连续复合精确产生

\[
 \phi(u)\phi(u+S_4)\prod_{j=1}^3\phi(u+S_j)^2 .
\]

端点只有一次 φ，内部每次两份；因此 (4) 的八个 φ 因子及所有
partial sums 都正确。每个 B_p 先在实线上零延拓，原支持已经要求
全部累计位置落在 I；没有把独立终位移限制误当成全部路径支撑。

有限 d 个 carrier 的几何和是 (6) 的两个完整 endpoint，
T−π/L 和 T+(2d−1)π/L。后者约2T，前者约T，真实 floor(d) 没有丢失。
式(5)保留 d^{-1}、L^{-1} 平均和每个 b_p 的 (a_L L)^{-1}。
四个负号总乘积为正。

原窗有 0≤φ≤1，因此端点 overlap 至多 L−|S|。
在 c≤|S|<L 中，
sin(πS/L) 的两端行为与 (L−|S|)/L 抵消，严格给
|K_d(S)|〈|W|〉≪_c X^{-1}。该估计包含 S 接近 ±L 的 alias。
在 |S|≥L 时真实 W 为零，不能改用周期翻折后的路径。

每个固定 X 的 prime sums 有限，B_L、B_H 有界；P 为有限秩。
所有 physical compressed words 和下文三个 Q telescoping terms
因此均为 trace class。没有把未压缩无限秩四词直接取迹。

偶窗使同时反转四个 signs 后，积分窗相同、K_d 共轭。
固定 high sign 为负后，按三个 low 的正 signs 个数 k=0,1,2,3
覆盖八个模式；反射给 high positive 的另八个。
high 的四个位置都只改变 partial-sum 的整数系数，不改变后续界。
本稿的“每个 placement 为复值 o(d)”足够；没有借物理迹循环
把四个 placements 提前视为同一项。

## 3. product 能量和共同 Fourier 分离

Chebyshev 与 prime harmonic sum 对 k=2,3 给
Σ_{p_1⋯p_k≤Y}∏log p_i≪Y log^{k−1}(2Y)。
唯一素因子分解保证每个 product 的有序表示至多 k!；
重复 prime 仍被这个上界涵盖。

所以任何 fixed Fourier coordinates 下的 tuple phases，都可在同一个
整数 product 内聚合为系数。其模至多对应正 coefficient mass；
Cauchy 用最多 k! 个表示，得到

\[
 E_3(2X)\ll L^{-6}X L^5=X/L,\qquad
 A_3(2X)\ll \sqrt X/L .
\]

前一个估计中每个 log²p 的第二份用 log(2Y) 控制，再用原 product
Chebyshev；后一个估计按 product norm partial summation。
单个 high prime 同样 E_H≪X/L、A_H≪√X/L。

low pair 的完整长度为 Z²=X，它给
E_LL≪L^{-4}(Σ_{p≤Z}log²p)²≪X/L²、
A_LL≪√X/L²。high-low product hr≤2X 中 h>Z≥r，
因而两范围固定分解唯一；E_HL≪X/L、A_HL≪√X/L。
没有在这个步骤假定新素数相关定理。

共享窗的准入顺序正确：
先保留同一个 near χ(S) 的支持，得到 k=3 的 product n≤2X、
k=2 的 high-low product m≤2X；再把三份 φ²(u+S_j) 和
φ(u+S)、以及 χ(S) 一同作 Fourier 分离。
固定 u、coordinates 后，各 prime 只带自身 label 的 unit phase。
聚合的 coefficient 不再依赖另一侧 high prime 或 product。

在 near 中保留这个 single-product 截断是合法的，且无需它是
canonical Dirichlet coefficient；这里只用任意有限系数的 Hilbert。
χ 的 Fourier 展开后逐点 near 限制不再存在，但已经得到的全局
frequency union 长度仍成立。不能在此步骤再按原 χ 支持逐项
压短差频；本稿没有这样做。

四份 shifted windows 的 L1 Fourier 费用为 O(ell_0^4)，χ 费用 O(1)。
φ(u) 留作 L^{-1} 平均；其值≤1，不增加 X 或 T 的幂。
这正面支付了旧逐个 negative low label 求和所产生的损失。

## 4. union spacing、finite csc 和 near 费用

k=3 的两集合是 triple product n=pqr 和 high prime h。
它们不可能有共同整数；n≥8、h>Z，最大至多2X。
整个 log union 的跨度至多 L−log4。

k=2 的两集合是 low pair n=pq 和 high-low m=hr。
后者含 high prime，前者只含 low primes，所以没有共同值。
union 最小至少4、最大至多2X，跨度至多 L−log2。
无论 low 标签是否重复，上述 disjointness 都不改变。

合并相同整数 product 后，每个 log n 到 union 其他点的间距至少
c/n；缺少相邻整数只会增加间距。局部 weighted Hilbert 的行能量
因此正是 Σn|a_n|²，不是仅总体最小间距1/X乘未加权能量。
其双线性形式可以由同一 union 上的 Hermitian Hilbert operator
界及 polarization 得到；互不相交性排除了无限 diagonal 项。

在 |s|≤L−c 上，
csc(πs/L)=L/(πs)+h_L(s)、|h_L(s)|≪_c L。
这同时保留 carrier endpoints 的 unit phases；
principal 费用为 (L/d)√(E_A E_B)，remainder 是
(L/d)A_A A_B。没有删除 finite csc 的 residual。

代入上节真实能量后，principal 的 normalized 费用分别是
1/L 和1/L^{3/2}，remainder 分别≤1/L²、1/L³。
加联合 Fourier 费用，得到(13)所示的两份 o(1)。
k=0、1 根本没有 near，因为相应 ratio 小于1/4或含8h的乘积。

## 5. k=0,…,3 的 far 和两端 alias

以下逐项核准了所有标签范围：

- k=0：|S|<L 迫使 hpqr<X。对 high prefix 使用
  √(X/(pqr))/L 后，总 coefficient mass≪√X/L；
  乘 endpoint-aware X^{-1} 得 X^{-1/2}/L。
- k=1：p≤Z<h、q,r≥2，所以 p/(hqr)<1/4。
  支撑另给 h<Xp/(qr)，总 mass≪X/L²，
  整个 far/alias 费用≤L^{-2}。
- k=2 positive alias：pq≥e^{-2}Xhr 与 pq≤X、
  h>Z、r≥2 在 X 足够大时矛盾。
  negative alias 则给 pq≤e²r，真实支持仍给 h<Xpq/r。
  使用 Σ_{pq≤e²r}log p log q≪r log(2r)，质量≪X/L³，
  normalized 费用≤L^{-3}。
- k=3 positive alias：n=pqr≤Z³ 与 n≥e^{-2}Xh
  迫使 h≤e²Z。high prefix mass≪√Z/L，
  完整 low triple mass≪Z^{3/2}/L³，费用≤L^{-4}。
  negative alias 迫使 n≤e²；实际上 n≥8>e²，故为空。

尤其 k=3 没有把 middle placement 的 n>2X 从整个 far 删除。
除了已经付款的 alias，这些长 triple 完整进入下一节的 canonical
估计。任何 placement 的路径支撑只进一步删项；这里的正上界
都在原支撑条件下使用，没有先抹掉支撑再忽略 alias。

## 6. middle-far k_L 的完整定义和 sharp canonical 准入

可把(17)明确读作：在 c≤|S|≤L−1 内取 displayed quotient，
在其余区域为0。其 numerator 在0、±L及整个外侧邻域为零，
所以得到真正的光滑紧支函数，不出现周期 csc 的其他 pole。
|S| 的0处不光滑被 near cutoff 的恒零邻域消除。
固定 cutoff 导数、csc 在距端点≥1的导数及 support 长度，
给 k_L'' 的 L1 为 L 的某个固定幂；两次分部积分给(18)。

near/alias/middle 的 partition 在真实 |S|<L 支持上精确。
同时展开 k_L 和四份 shifted window 后，五个 coordinates 使
四个 prime variables 完全独立：
每个 low prefix 是 p≤Z，每个 high prefix 是 p≤X减p≤Z。
这一步没有插入 product cutoff；长 triple 的 net ratio 仍由同一个
k_L Fourier integral 表达。

446(4) 的 uniform sharp Perron 保留真实
x^{1/2+it}/(1/2+it) principal residue、half-integer sharp endpoint
和全 height logarithmic error。
从完整 Λ 去掉 proper powers 的 pointwise 绝对质量
Σ_{p^m≤Y,m≥2}log p/p^{m/2}=O(log²(2Y))，
所以(19)的 genuine-prime prefix 形式合法。
这是系数恒等式的准入，不是把已有 proper-power S4 费用再加一次。

## 7. 高主区、所有 C2 ghosts 和显式小量

当五个 Fourier coordinates 都≤T/100时，每个 prime height是
某个真实 carrier endpoint 的带符号值，加至多五个 signed coordinates。
它的绝对值仍≍T；不会把差频的小量误作该 absolute height。
应用 sharp prefix 后，high 一份为 X^{a−1/2} 的 logarithmic 费用，
三份 low 共为 Z^{3(a−1/2)}，四个 normalizers 留下 L^{-4}。
再除 d，power 恰为

\[
 X^{a-1/2}Z^{3(a-1/2)}/d
 =X^{(5/2)a-9/4}\times\hbox{logarithmic factor}.
\]

theta=7/8、a=89/100 固定时是 X^{-1/40}；
一般 theta<9/10 可先选 theta<a<9/10。

在主区外至少一个 coordinate>T/100。
φ 或 φ² 的真实 C² Fourier tail 为 O(1/T)；
k_L tail 为 O(L^C/T)。五者 union bound 与其余 L1 norms
合成 O(L^C/T)，包含多个 coordinates 抵消、任意 principal-height峰。
这里不再借 |t|≍T 估计 primes，只用真实 absolute masses：

\[
 A_H A_L^3\ll X^{5/4}/L^4 .
\]

carrier endpoint form 的1/d仍在，因此全部 ghosts
≪X^{5/4}L^C/(dT)=X^{-3/4}L^{C'}，趋于0。
共同 u 平均只乘固定有界因子。
本论证不需要 Schwartz 窗或未知 low absolute-height cancellation。

这些费用与 near/far/alias 合并，严格给(23)每个 physical placement
为 o(d)。常数 uniform 于 prime labels、carrier index 和 placement；
profile、cutoff、gap a−theta 先固定，再令 X→∞。

## 8. finite P 的准确剩余与31范围

三个插入 P 的 algebraic telescoping 正是(24)–(25)。
每项含 finite-rank P，所以其迹准入合法。
physical trace 小量不能控制这些 Q terms 的符号或大小。
四个 finite placements 才可用矩阵迹循环化为4Tr(C_H C_L³)，
所以(26)的负号正确：

\[
 4\operatorname{Tr}(C_HC_L^3)
 =-\sum_j\Delta_j+o(d).
\]

signed aggregate 为实数至o(d)，并不要求各 isolated term 都有
实的 pointwise kernel。原报告的 Γ−K 余额与此 telescoping 相反号
吻合；现有 absolute growth bound 不能登记为 o(d)。

31 的 near products 可达 XZ，不再满足本次两个整数集合≤2X的
Hilbert 能量准入。其同样四 prefix canonical 方法的主 power
(7/2)a−11/4 在a=.89时为正，也没有免费闭合。

最终限定 PASS 只验收新的 signed physical13 小量和 accurate
finite-P reduction。若要支付实际13，还须给同一个
−ReΣ_jΔ_j 的一侧 O(d) 或o(d)预算；
若要完整四阶常数，还须另外支付31与其余未闭合 sectors。
