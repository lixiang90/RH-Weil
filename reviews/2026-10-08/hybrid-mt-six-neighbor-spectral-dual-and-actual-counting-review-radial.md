# 原MT六邻域谱对偶与实际计数：独立全文审查

2026-10-08。审查者：radial。结论：**限定PASS**。

独立全文读取作者源331行、新验证器163行及最终输出58行，并重新核对304§5和477作者源的有限惯性及实际前缀接口。作者证明在其明确的原固定函数二阶算术输入[R]下闭合；未发现阻断。下列绑定均按UTF-8、CRLF/CR转LF、不裁剪正文或EOF计算。

## 1. 最终证据对象与范围

| 对象 | canonical LF SHA256 | 字节/行 |
|---|---|---:|
| [被审研究源](hybrid-mt-six-neighbor-spectral-dual-and-actual-counting-research-compression.md) | c69dcf11fe9ed46be77dbd5c2926e6058193cf61808613a73121797aa53656a9 | 12574/331 |
| [新核验证器](../../scripts/hybrid_mt_six_neighbor_geometry_certificate.py) | b7bac147d76b7e1fb2bbe1307518acf4642cb0aedbba2c0fd8eebc610d1d3a8c | 7043/163 |
| [最终核输出](../../output/hybrid-mt-six-neighbor-geometry-certificate.json) | 0b587847baa23014d947a7621f491a5f9175d714341b2bc9026465073aceee95 | 1587/58 |

复核的冻结依赖为：

- [304](../../notes/304-mt-triple-geometry-and-second-moment-stability.md)，SHA 03f21ab1749157ff45bc4d4f62709e2a5482257c7155e7e8e644da0ac4521bc4；本轮回读§5.1–5.3，保留完整复零点双和、非实正负块和固定profile次序。
- [477实际计数作者源](hybrid-original-multipoint-envelope-and-actual-counting-research-compression.md)，SHA 59b399445a3022ce9b5ee6c064660e1602dab6d5641d3793649f16f509fc5efa；回核(4)–(5)、§7。
- [原七点输出](../../output/hybrid-multipoint-seven-primary-replay.json)，SHA aa6885489c1d0086bca32b72d27fc7a2a5f44a48f78483a057f23a59e5a828e6。
- [冻结有理代数输出](../../output/hybrid-multipoint-cap-exact-algebra.json)，SHA d84077ab71b47d1ea253cad9675fa8c25f9aa4dade775ad73ff53033167625c3。

本审查没有重证BGST固定函数二阶解析定理，也没有另做原七点707901盒子的第三遍完整运行。原七点全域证书和外部解析输入的已归档审查范围继续适用。351/355是机制的先行来源，不作为未核的附加不等式插入当前证明。

## 2. 完整实轴核界与代码覆盖

源(2)、(6)的核归一化一致。置 \(\beta=1/\sqrt2\)、\(a=\beta\cot\beta\)、\(t=\pi x\)，直接对正偶密度积分得到
\[
 k_0(x)=\frac{a t\sin t-\tfrac12\cos t}{t^2-\tfrac12}.
\]
本次使用的 \(x\ge3809/4000\) 远离可去点；代码逐cell先证明分母为正。

精确grid端点 \(r\,3809/4000\) 均为1/40000整数格点。验证器用fmpq中心和半径构造闭Arb球，覆盖 \([3809/4000,7]\) 全部241910格。每格使用适用的最大半径 \(r\le6\)；给定 \(M_r\) 严格递减，所以更小半径的界也随之成立。阈值与相邻闭cell端点无遗漏，最后半径覆盖51460格。成功接受是Arb严格比较加1/10^8余量，不使用浮点极值。

无限尾并非截至7的抽样替代。由 \(0<a<5/6\)、\(\pi>157/50\)，
\[
 |k_0(x)|\le \frac{a t+1/2}{t^2-1/2}.
\]
右式导数的分子为 \(-a t^2-t-a/2<0\)。因此 \(x\ge7\) 的有理上界
\[
 \frac{141125}{3619653}<\frac{203}{5000}=M_6
\]
控制全部余尾，继而控制其余五个 \(M_r\)。

在短区间，\(f_0\ge0\)、\(x\le d_0<1\) 使源(9)的sin因子非负；故 \(k_0\) 递减。Arb认证端点 \(k_0(d_0)>1/10\) 足以支付整个 \([0,d_0]\)。

审查者已实际执行最终脚本的只读
\[
 \texttt{C:\backslash Python312\backslash python.exe -B scripts/hybrid\_mt\_six\_neighbor\_geometry\_certificate.py --check}
\]
并收到完整实轴PASS：重算所有241910格、无限尾及确定输出字段；未写或覆盖输出。代码排除elapsed_seconds后比较全部其他字段，并检查原七点输出的固定hash及目标。默认生成模式拒绝覆盖已有输出。输出scope准确：核界已认证，原七点证明及解析零点传递不由该脚本单独认证。

## 3. 谱对偶与六邻域效率

源(10)的 \(j\) 在非负轴上凸：在2处两侧导数同为2。对 \(|b|\le1,t\ge0\)，
\[
 j(t)\ge2b(t-1)-b^2
\]
的两个分支差值均正确。在 \(B\) 的本征基使用标量Jensen得到源(11)，无需operator convexity，也无需 \(B\) 为PSD或与 \(G\) 交换。

对相邻gap至少 \(d_0\) 的点列，第 \(r\) 邻点的距离至少 \(r d_0\)。零对角的真实核试探矩阵用统一权 \(u=50/51\)，独立有理核对
\[
 \sum_{r=1}^6M_r=\frac{51}{100},\qquad
 2u\sum_rM_r=1,\qquad
 2u-u^2=\frac{2600}{2601}.
\]
行和等于1仍满足 \(\|B\|_{\rm op}\le1\) 的允许闭域。此处没有要求不存在的严格范数余量。

\(\operatorname{tr}B(G_0-I)=uE_6\)、\(\operatorname{tr}B^2=u^2E_6\)，所以源(15)恰为 \(cE_6\)。被截断的是试探矩阵，完整Gram及其长距离项仍在谱对偶左侧。

## 4. 全链及全gap分簇

连续七点窗口求和时，每个gap至多计6次，第 \(r\) 邻pair至多计 \(7-r\) 次。原F6的系数因而给
\[
 E_6+\operatorname{span}/500\ge (19/5000)(n-6).
\]
所有项非负，求和方向正确；不足7点时右端非正。得到
\[
 \alpha=\frac{247}{65025},\quad
 \eta=\frac{26}{13005},\quad
 J\ge\alpha n-\eta\,\operatorname{span}-6\alpha.
\]
端项只出现一次，不因多个簇而重复支付。

按相邻gap小于 \(d_0\) 的连续分量分簇。单节点分量汇成一个主块，其相邻距离仍至少 \(d_0\)，总span不超过全列span。非单节点簇不需要总直径小于 \(d_0\)：所选不交相邻pair的每个gap小于 \(d_0\) 即足够。

每pair给 \(2k_0(g)^2>1/50\)，且 \(\lfloor m/2\rfloor\ge m/3\) 对全部 \(m\ge2\) 成立，所以每簇支付 \(m/150>\alpha m\)。这包括奇数簇的未配节点；额外单节点块的 \(j(1)=0\) 不被误当作正增益。全Gram在各主块本征基的标量Jensen允许pinching，故源(20)覆盖所有位置配置，没有剩余gap域或重复叠加Gram奖励。

## 5. 实际算子、增长列数与计数

304实际算子使用完整零点多重集。每个非实共轭对保留 \(2m(g\otimes g-h\otimes h)\)；trace为 \(N(T)\)，HS平方由共轭重排等于完整 \(K_\delta(z-w)^2\) 双和。单个复数项没有被误认成非负。

对固定平滑profile，简单临界线列精确单位，真实Gram为 \(k_\delta(x_i-x_j)\)。在分离主块上继续使用由 \(k_0\) 构造的同一个 \(B\)，其可行性不依赖平滑核的行和。于是
\[
 2\operatorname{tr}B(G_\delta-G_0)
 \ge-2\varepsilon_\delta\sum_{ij}|B_{ij}|
 \ge-2n_s\varepsilon_\delta.
\]
这避免了增长稠密Gram的operator norm误差。短簇每节点下界为
\(\beta_\delta=(2/3)(1/10-\varepsilon_\delta)^2\)；独立Fraction核对在 \(\varepsilon_\delta<1/10000\) 时 \(\beta_\delta>\alpha-2\varepsilon_\delta>0\)。

实际有限惯性账本保持 \(n_+(Q)\le b\)、\(N\ge s+2b\)、\(D\ge s+b\)。由477(4)消元得到源(25)的两式；没有假设所有零点在临界线，也没有免费采用一般不成立的 \(D\ge(N+s)/2\)。

将 \(J_\delta\ge(\alpha-2\varepsilon_\delta)s-\eta X_T-6\alpha\) 代入，利用 \(X_T/N\to1\)，得到源(26)。不同点结论从同一HS及惯性账本再次代入简单点下界推出，非独立模型恒等式。顺序严格为固定profile、\(T\to\infty\)、再profile逼近；没有 \(\delta(T)\) 的统一解析假设。

## 6. 精确比例与最终限定

独立以冻结 \(C_0\) 的有理上下端进行Fraction计算，恰好重现源(27)两端，并核对下端严格大于 \(673058110/10^9\) 及 \(p_{280}\) 的冻结上端。因此
\[
 p_6=\frac{65025C_0-130}{64778}
 =0.6730581101107435\ldots,\qquad
 (1+p_6)/2=0.8365290550553717\ldots.
\]
相对477简单比例增加约0.00484578316066个百分点，数量级和百分比换算正确。

本结论是原固定profile二阶合同下的实际前缀渐近计数下界，有限几何证书与数学传递已分别核准。它不建立新的无零条带，不支付full signed近共振或常数级高四矩，不是RH完成比例，也不声称超过305所登记的更高公开结果。无需数学修订。
