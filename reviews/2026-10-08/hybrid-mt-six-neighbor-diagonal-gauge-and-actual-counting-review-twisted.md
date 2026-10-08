# 六邻域对角调节与实际计数：独立全文审查

2026-10-08。审查人：twisted_research。结论：**限定 PASS**。
已全文实读被审来源188行，回核478冻结输入及原计数传递；没有修改任何作者源、旧笔记、证书或 Git。

## 1. 最终绑定和审查范围

canonical UTF-8 LF 只统一 CRLF 与孤立 CR；不 trim，不改变 EOF。

| 文件 | canonical LF SHA256 | 字节 / 行 |
|---|---|---:|
| [本次被审对角调节来源](hybrid-mt-six-neighbor-diagonal-gauge-and-actual-counting-research-compression.md) | 361c32d6e28cfd2e5c30516b42e58297f11f4516c77407de39c5f32b8af7c30b | 7312 / 188 |
| [冻结六邻域与实际计数完整来源](hybrid-mt-six-neighbor-spectral-dual-and-actual-counting-research-compression.md) | c69dcf11fe9ed46be77dbd5c2926e6058193cf61808613a73121797aa53656a9 | 12574 / 331 |
| [478冻结笔记](../../notes/478-original-mt-six-neighbor-dual-and-whole-chain-proportion.md) | 6ab8384289cf7470b7ee448e381f5e9afdd268b13852f95322c98c1a62dd5c54 | 6846 / 128 |
| [原严格 C0 区间](../../output/hybrid-multipoint-cap-exact-algebra.json) | d84077ab71b47d1ea253cad9675fa8c25f9aa4dade775ad73ff53033167625c3 | 3367 / 84 |

本次独立检查有限矩阵对偶、全部位置的几何下界、增长一致的原固定profile准入、全重数与惯性计数，以及所有新增有理常数。只承认原前缀渐近计数合同内的极小提升；没有新的无零区域、whole四矩常数、世界纪录或最优性结论。

## 2. 负对角与单侧谱对偶确实合法

在非负实轴上
\[
j(t)=(t-1)^2-(t-2)_+^2
\]
是凸函数：在 \(0\le t\le2\) 二阶导数为2，在 \(t\ge2\) 为线性 \(2t-3\)，于2的左右一阶导数同为2。对任何实数 \(b\le1\)，作者两个差式分别为
\[
(t-1-b)^2,\qquad (1-b)(2t-3-b).
\]
后式在 \(t\ge2\) 非负，因为第二因子至少为 \(1-b\)。这里不要求 \(b\ge-1\)。

在 Hermitian \(B\preceq I\) 的本征基中，令 \(t_i=\langle v_i,Gv_i\rangle\ge0\)。对 \(G\) 的谱展开应用标量凸 Jensen 给
\(\operatorname{Tr}j(G)\ge\sum_i j(t_i)\)；再逐项用上式，得到
\[
J(G)\ge2\operatorname{Tr}B(G-I)-\operatorname{Tr}B^2.
\]
所以源式(2)不需要 \(B\succeq-I\)，也不需要 \(B\) 与 \(G\) 交换。允许负常数对角是本次有效修改，不是把旧双侧范数前件漏掉。

原分离点列的六邻矩阵 \(K\) 保留 \(1\le|i-j|\le6\) 的完整真实核条目，且对角为0；原认证行和给 \(\|K\|\le S=51/50\)。实核对称性严格给
\[
\operatorname{Tr}K(G_0-I)=\operatorname{Tr}K^2=E_6.
\]
令 \(u=(1+e)/S\) 后，
\(\lambda_{\max}(-eI+uK)\le-e+uS=1\)。
其下方谱可以低于−1，已经由上述单侧对偶覆盖。

对角为1的真实 Gram 给 \(\operatorname{Tr}(G_0-I)=0\)，而
\(\operatorname{Tr}K=0\)。因此对偶中的两项准确为
\[
2uE_6,\qquad e^2n+u^2E_6,
\]
没有遗漏交叉项。源式(4)的 \(cE_6-e^2n\)、\(c=2u-u^2\)，以及完整负对角成本均正确。

## 3. 七点覆盖、全簇和正确端点成本

冻结的同一七点证书给
\[
E_6+\operatorname{span}(y)/500\ge\tau(n-6),
\qquad \tau=19/5000.
\]
由于本次 \(c>0\)，与对角成本合并后只能得到
\[
J(G_0)\ge(c\tau-e^2)n-(c/500)\operatorname{span}(y)-6c\tau.
\]
端项严格为 \(6c\tau\)，不能改为 \(6\alpha\)。作者在式(6)、(7)及实际传递中均保留正确端项。

\(n\le6\) 时冻结七点右侧非正，仍可由 \(E_6\ge0\) 使用；空主链的span取0，产生的负常数边界有效。短簇的互不交相邻pairs数为 \(\lfloor m/2\rfloor\ge m/3\)，每pair原下界为 \(2/100\)，故每节点至少 \(1/150>\alpha\)。

将全部singleton簇合成一个分离主链，再一次pinch成主链、各不交pairs及剩余singletons，使用的是凸trace pinching。原整 Gram 的所有条目仍保留；不存在重叠计费，也没有每个短簇额外收一次六端成本。主链span不超过全点列span，故源式(7)覆盖全部位置与全部点数。

## 4. 原固定平滑profile与全零点账本

采用冻结304合同中的非负、实偶、单位积分固定平滑profile \(f_\delta\)。它给真正 PSD Gram，且对角精确为1。全实轴
\(|k_\delta-k_0|\le\epsilon_\delta\) 对任意维数统一。

实际试探仍用原 \(k_0\) 构造的同一 \(B=-eI+uK\)，可行性不随维数或profile变化。负对角项与 \(G_\delta-G_0\) 的迹准确为0。剩余行和是 \(uS=1+e\)，于是双线性项误差准确最多
\[
2(1+e)n_s\epsilon_\delta.
\]
本次不能沿用没有负对角时的 \(2n_s\epsilon_\delta\)；作者式(8)已支付正确费用。

短簇每节点下界为
\[
\beta_\delta=\frac23(1/10-\epsilon_\delta)^2.
\]
当 \(0\le\epsilon_\delta\le1/10000\)，作者式(9)的
\(0<\alpha_\delta\le\alpha<\beta_\delta\) 成立；下面精确核算验证最坏端点的两项余量。因此实际全部点列仍有
\[
J_\delta\ge\alpha_\delta s-\eta X_T-6c\tau,
\qquad \alpha_\delta=\alpha-2(1+e)\epsilon_\delta.
\]
没有通过全密集 Gram 的 operator norm 接近来控制增长维数。

原算子 \(A\) 的所有离线正负块保持不变。冻结计数合同给
\[
s\ge2N-\|A\|_{\rm HS}^2+J_\delta,\qquad
2D\ge3N-\|A\|_{\rm HS}^2+J_\delta.
\]
先固定profile令 \(T\to\infty\)，第一式产生
\[
\liminf s/N\ge
\frac{2-R_\delta-\eta}{1-\alpha_\delta}.
\]
再令固定profile趋原MT，得到 \(p_{\rm dg}=(C_0-\eta)/(1-\alpha)\)。
将同一第一式所得下界代入第二式，极限中的分子为
\(1+C_0-\eta+\alpha p_{\rm dg}=1+p_{\rm dg}\)，故
\(\liminf D/N\ge(1+p_{\rm dg})/2\)。
这一步使用原惯性预算；没有免费假定 \(D\ge(N+s)/2\)，也没有令profile随 \(T\) 移动。

## 5. 独立精确有理复算

本次用内存 Python Fraction 独立复算，没有修改任何脚本或输出。核得
\[
e=\frac1{62500},\quad
u=\frac{62501}{63750},\quad
c=\frac{4062502499}{4064062500},
\]
\[
\alpha=\frac{77187542279}{20320312500000},\qquad
\eta=\frac{4062502499}{2032031250000}.
\]
因此源式(1)的完整分母、线性 \(C_0\) 系数和常数项正确。

将冻结 JSON 中 \(C_0\) 的两严格有理端点代入，逐字重现被审稿§4的两巨分数。新严格下端减去478旧严格上端，准确得到
\[
\frac{38202658750375724709585783275561655495674769405}
{223107690410244439578888423481057719096362234296731172864}>0.
\]
两个最坏平滑余量也逐字重现：
\[
\alpha-\frac{2(1+e)}{10000}
=\frac{36561707377}{10160156250000}>0,
\]
\[
\frac23(1/10-1/10000)^2-\alpha
=\frac{232041622759}{81281250000000}>0.
\]
独立核对 \(\Delta c\) 展开，并在两个 \(C_0\) 端点检查源式(12)：
\[
p_{\rm dg}-p_6
=
\frac{\Delta c(\tau C_0-1/500)
 -(C_0-c_0/500)e^2}
 {(1-\alpha)(1-\tau c_0)}.
\]
分母正、分子严格正，与巨分数比较一致。

仅作显示，严格区间为
\[
0.6730581102819731786506991071279998423824\ldots
<p_{\rm dg}<
0.6730581102819731786506991071279998426863\ldots,
\]
新下端比旧上端大约 \(1.71229681415865585\times10^{-10}\)。
这些小数不是判定依据；判定使用上述原有理区间和精确代数。

## 6. 证据和结论的边界

原全实轴六邻核界、七点覆盖和304解析传递作为已经独审的冻结输入。本次没有重复运行大七点证书，也没有改任何核参数；本次实际运行的是新增常数与严格提升的内存 Fraction 复算。有限算术复算不单独认证原解析传递，后者已在上述数学审查中分开核对。

新增收益在原前缀渐近计数、同一 \(C_0\) 与全重数合同内成立。它不依赖原7/8无零输入；比例 \(p_{\rm dg}\) 与探测器的 \(\kappa\) 是不同对象。全部同源四素数相消、高四矩常数和联合解析桥仍未由本稿支付。没有最优参数、世界纪录、RH证明或无零边界更新声明。
