# 原 MT 六邻域全链谱对偶及实际比例：独立全文审查

2026-10-08，twisted_research。基线 main
030576085955927fcb63742c770b5cd171cb925f。
只新增本审查；不改作者源、旧证据、math、论文或 Git。

**限定 PASS。** 完整读取作者源331行、478全部128行与最终检查器163行，
独立复跑最终均一权的全部241910个 Arb 闭cell及无限尾。
核准的是明列原解析输入下的前缀渐近简单临界线比例
\[
 p_6=\frac{65025C_0-130}{64778}
 =0.673058110110743497234833522136902492\ldots .
\]
其分母为所有非平凡零点的重数计数。本稿不核准世界纪录、外部同行评审、
Lean 全闭包、新无零条带、RH 或原 signed near 常数级第四矩。

## 1. 冻结对象与实际阅读范围

canonical UTF-8 LF 只统一 CRLF、lone CR 为 LF；不 trim 或改变 EOF。

| 文件 | canonical LF SHA-256 | bytes / 行数 |
|---|---|---|
| [作者源](hybrid-mt-six-neighbor-spectral-dual-and-actual-counting-research-compression.md) | c69dcf11fe9ed46be77dbd5c2926e6058193cf61808613a73121797aa53656a9 | 12574 / 331 |
| [478摘要](../../notes/478-original-mt-six-neighbor-dual-and-whole-chain-proportion.md) | 6ab8384289cf7470b7ee448e381f5e9afdd268b13852f95322c98c1a62dd5c54 | 6846 / 128 |
| [新全实轴检查器](../../scripts/hybrid_mt_six_neighbor_geometry_certificate.py) | b7bac147d76b7e1fb2bbe1307518acf4642cb0aedbba2c0fd8eebc610d1d3a8c | 7043 / 163 |
| [新核输出](../../output/hybrid-mt-six-neighbor-geometry-certificate.json) | 0b587847baa23014d947a7621f491a5f9175d714341b2bc9026465073aceee95 | 1587 / 58 |
| [原七点输出](../../output/hybrid-multipoint-seven-primary-replay.json) | aa6885489c1d0086bca32b72d27fc7a2a5f44a48f78483a057f23a59e5a828e6 | 2108 / 48 |
| [原严格C0及p280代数](../../output/hybrid-multipoint-cap-exact-algebra.json) | d84077ab71b47d1ea253cad9675fa8c25f9aa4dade775ad73ff53033167625c3 | 3367 / 84 |
| [304固定光滑实际桥](../../notes/304-mt-triple-geometry-and-second-moment-stability.md) | 03f21ab1749157ff45bc4d4f62709e2a5482257c7155e7e8e644da0ac4521bc4 | 26598 / 645 |
| [477完整计数源](hybrid-original-multipoint-envelope-and-actual-counting-research-compression.md) | 59b399445a3022ce9b5ee6c064660e1602dab6d5641d3793649f16f509fc5efa | 16963 / 421 |

本次回读304 §5的固定函数去权、全复零点有限自伴实现与重数账本；
回核477源的 \(j\)、惯性不等式、原七点定义及两极限。
这些已经审查的原解析定理保持为引用输入 [R]，本次不重新认证其所有外部论文。
351谱对偶、355短簇机制及ainta原七点证书的先行来源均保留。
新稿没有调用未完成的357–359连续subaction。

## 2. 全实轴核证书：包括阈值与无限尾

原 Fourier 约定为
\[
 k_0(x)=\int_{-1/2}^{1/2}
 \frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
 e^{-2\pi ixu}\,du .
\]
密度非负、实偶且积分1，故 \(k_0\) 为实偶、\(k_0(0)=1\)、\(|k_0|\le1\)。
令 \(t=\pi x,\ \beta=1/\sqrt2,\ a=\beta\cot\beta\)，直接积分确实给
\[
 k_0(x)=\frac{at\sin t-\tfrac12\cos t}{t^2-\tfrac12}.
\]
归一化与检查器一致，没有遗漏 \(2\pi\) 或把分子可去零点当成核零点。

检查器以128bit Arb、精确fmpq中心/半径覆盖
\([3809/4000,7]\) 的全部宽 \(1/40000\) 闭cell。
起点index38090、终点280000，差241910；
强radius计数为五个38090和一个51460，和准确。
所有 \(r d_0\) 都是grid点；阈值两侧的闭端点没有空隙。
每格选择适用的最大 \(r\le6\)，用递减的 \(M_r\) 继承其余界，
且用包含整个cell的绝对值上界验
\(\mathrm{upper}+10^{-8}<M_r\)，不是在中心抽样。

无限尾的有理包络正确：\(0<a<5/6,\ \pi>157/50\)，
\[
 \frac{at+1/2}{t^2-1/2}
 \quad\hbox{的导数分子为 }-at^2-t-a/2<0,
 \qquad
 \frac{141125}{3619653}<\frac{203}{5000}.
 \]
故 \(x\ge7\) 的全部实轴已付，不限于有限图或有限mesh。
端点 \(k_0(d_0)>1/10\) 由严格Arb包围认证；
原正密度在 \(0\le x\le d_0<1\) 上的积分导数非正，
补齐该端点左侧的全部短簇下界。

最终实际运行：

    python -B -X utf8 scripts/hybrid_mt_six_neighbor_geometry_certificate.py --check

退出0，完整 PASS；确定字段、原七点SHA与最终脚本SHA全部一致。
closed-cell ball摘要为
42d5d94ab916327d36705f6ee1385a7779ad931cb4ade50989579891f2f7bc5e。
时间字段是显示信息，不决定任何cell验收。
本审查没有另一次执行大七点搜索；本轮根节点报告亲自完成原七点
707901节点的完整重放，本人本次执行的是新全实轴核证书。

## 3. 谱对偶不要求试探矩阵正定或全Gram有界

源(10)–(11)正确。对 \(G\succeq0,\ \|B\|_{\rm op}\le1\) 及实 \(b\in[-1,1]\)，
\[
 j(t)\ge2b(t-1)-b^2\quad(t\ge0).
\]
两分支的差分别为 \((t-1-b)^2\) 与
\((1-b)(2(t-1)-(1+b))\)，均非负。
在 \(B\) 的本征基对 \(G\) 作标量Jensen再求和即可；
不需要operator convexity，也没有令 \(B\) 与 \(G\) 交换。

478给的第二证明也合法：\(D=G-I\)，
\(J=\|D\|_{\rm HS}^2-\|(D-I)_+\|_{\rm HS}^2\)。
\(B\le I\) 给 \(D-B\ge D-I\)，逐个有序特征值的最小最大原理给
\[
 \|D-B\|_{\rm HS}^2\ge\|(D-B)_+\|_{\rm HS}^2
 \ge\|(D-I)_+\|_{\rm HS}^2 .
\]
配方得相同对偶。第二证明只需 \(B\le I\)；源的双侧范数约束足够。

分离点列第r邻点距离至少 \(r d_0\)，因而参考核构造的六邻矩阵满足
\[
 2u\sum_{r=1}^6M_r=1,\quad
 u=50/51,\quad c=2u-u^2=2600/2601.
\]
等号行预算仍合法。完整Gram一直保留，只有试探 \(B\) 被截为六邻；
代入对偶准确得到 \(J\ge cE_6\)，并非断言全Gram谱不超过2。

## 4. 全窗口累加及所有簇：每个节点只支付一次

原 \(F_6\) 的pressure是 \(1/3000\)，连续窗口聚合后是 \(1/500\)。
在全部 \(n-6\) 七点窗口中，第r邻边至多出现 \(7-r\) 次，
每gap至多出现6次。各项非负，故
\[
 E_6+\mathrm{span}/500\ge(19/5000)(n-6).
\]
\(n\le6\) 的右端非正；空/单点span定义0足够。
乘 \(c\) 后
\[
 \alpha=c(19/5000)=247/65025,\qquad
 \eta=c/500=26/13005.
\]
没有每个固定长块的重复端点费用。

按gap小于 \(d_0\) 的连续簇划分，单点簇合成一条分离大链；
各非平凡簇取互不交叠的相邻两点块。
每块谱 \(1\pm|k_0(g)|\in[0,2]\)，故其 \(J=2|k_0(g)|^2>1/50\)。
\(\lfloor m/2\rfloor\ge m/3\) 也涵盖奇数簇，
给每节点至少 \(1/150>\alpha\)。
标量凸谱迹的pinching仅按这些不交坐标块使用一次，
从而所有实点配置满足源(20)，没有只覆盖某些low-F6盒子。
原点列有重合位置时同样被短簇处理；实际简单零点位置本来互异。

## 5. 原实际计数传递：参考核试探避免增长Gram误差

对每个固定光滑profile，
\(\sup_{\mathbb R}|k_\delta-k_0|\le\varepsilon_\delta\) 是实轴全域的 \(L^1\) 推论；
没有向增长的复带延伸这条近似。
分离链仍用参考 \(k_0\) 的 \(B\)，所以可行性精确保留。
实际线性项误差是
\[
 |2\operatorname{tr}B(G_\delta-G_0)|
 \le2\varepsilon_\delta\sum_{i,j}|B_{ij}|
 \le2n_s\varepsilon_\delta.
\]
这只涉及稀疏试探，不是以稠密增长Gram的全范数作免费比较。
短簇每节点的实际费用为
\((2/3)(1/10-\varepsilon_\delta)^2\)；
当 \(\varepsilon_\delta<10^{-4}\)，严格大于
\(\alpha_\delta=\alpha-2\varepsilon_\delta>0\)。
因而源(24)正确，误差为 \(O(\varepsilon_\delta N)\)。

304的原完整算子保留全部复零点及离线正负块，
\(\operatorname{tr}A=N\)、\(\|A\|_{\rm HS}^2=(R_\delta+o_\delta(1))N\)。
简单单位列给 \(P\)；重复临界点与离线共轭对给
\(n_+(A-P)\le b,\ N\ge s+2b,\ D\ge s+b\)。
有限惯性账本直接给
\[
 s\ge2N-\|A\|_{\rm HS}^2+J,\qquad
 2D\ge3N-\|A\|_{\rm HS}^2+J .
\]
联立增长一致的几何式，以 \(X_T/N(T)\to1\)，得到源(26)。
不同点第二式须将第一式代回同一账本；一般
\(D\ge(N+s)/2\) 并未被假设。
顺序是固定profile、\(T\to\infty\)、profile极限；没有取 \(\delta(T)\)。
本结论是 \(0<\gamma\le T\) 的前缀比例，未额外证明每个dyadic盒的同值。

## 6. 严格比例区间与478摘要的范围

独立读取冻结代数JSON的两份严格 \(C_0\) Fraction端点，
逐端应用递增仿射函数 \((65025C_0-130)/64778\)；
结果与源(27)两份有理数逐个完全相等。
另以精确Fraction核验：
下端 \(>673058110/10^9\)，且严格大于冻结 \(p_{280}\) 的上端。
独立192bit Arb计算得到
\[
 p_6=0.67305811011074349723483352213690249217768427454417891464\ldots,
 \quad (1+p_6)/2=0.836529055055371748617416761068451246\ldots .
\]
十进制仅作展示；核准的数字由前述有理包围支持。

478忠实总结源的全部点列、参考核误差、完整惯性账本和前缀两极限。
其无零条带仅回报旧引用输入下的值；本比例证明自身不使用 \(7/8\)。
原四阶 \(T^{5/7+\varepsilon}\) 增长界、完整TypeII与四份Λ权的signed near
没有被替成常数预算，也没有重新调低 \(\kappa\)。
原MT、ainta七点、351/355和更高公开候选的来源范围均保留。

478的本轮总检查点链接在本审查冻结时是预先登记的输出路径；
此时不以不存在/未完成的总清单宣称执行PASS。
本稿实际执行PASS仅指新核检查器及上面的独立有理核算。
总清单应由根节点在所有审查齐备后生成并另行核验。

全文未发现数学阻断。**有限证明、原解析引用下的实际前缀传递及最终数字限定 PASS。**
