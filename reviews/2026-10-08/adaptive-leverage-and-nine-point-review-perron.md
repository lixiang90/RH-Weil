# 九点 lift 与全零点适应性 leverage：不同作者限定数学审查

2026-10-08，perron_reviewer。本轮基线6666ad6；只新增本 peer，不改作者源或 Git。
结论：所列有限谱恒等式、九点合法 lift、无穷尾付款、充分接口及条件比例代数均 PASS。
九点紧核心的统一正余量和 \(N\) 归一 leverage 正下界仍未证明；
不准入任何新的实际零点比例、常数四矩或无零边界。

## 1. 实际全文读取与冻结绑定

canonical LF 为 UTF-8，仅 CRLF/lone CR→LF，保留 EOF。
本轮全文读下列前三源与完整 JSON，并自行重推证明；没有只看程序 stdout。

| 输入 | 行／LF字节 | SHA256 |
|---|---|---|
| [High九点源](am-nine-point-lift-research-high-product.md) | 161／8823 | 88bd93c28ca361a5be70a48504a186378abba57031ac0f149b08eaf5a8acf045 |
| [全零点Schur/leverage源](all-zero-schur-residual-research-checkpoint.md) | 175／10734 | 43e1d8a1dc0b0d2f885d4f3e55b5c58e0efe6638a2e6ac74f3fcc627b4adb155 |
| [root条件代数程序](../../scripts/am_adaptive_leverage_gain_certificate.py) | 97／4258 | 8d3955001ab59c2622936d969ba84cf18692b36061b34b280070311762551e6d |
| [完整输出](../../output/am-adaptive-leverage-gain-certificate.json) | 25／1500 | 4c2e9350449b598a6124cdbc7b92d76cd1cebc7fb3474676f25f1c3d94c46865 |

本轮还全文重读[483](../../notes/483-admission-of-known-am-eight-point-proportion.md)与
[498](../../notes/498-lossless-am-eight-point-simple-critical-proportion.md)，
并对此前已全文审查的635行正式论文重新核 exact 权重表、固定平滑和全零点计数段。
不重开旧PC8组合信任准入，不运行完整上游 Lean、240项大复演或优化搜索。
High 的141行 locator、106行 Arb diagnostic 与35行局部 JSON 本轮全文读；
定位浮点值不进入全连续 PASS。本审查未重跑定位或该 Arb 输出。

## 2. 九点准确 lift、全部无穷尾与充分证书

由两个相邻八点 frame 各取一半，新增 \((0,8)\) 权2，
对跨度 \(s\le7\) 仍有 \(\sum_iW'_{i,i+s}=\sum_iW_{i,i+s}\le2\)，跨度8恰2。
全部36对非负、逆序对称，\(\sum W'\le16\)。
独立 Fraction 使用正式论文 exact 28项表（其中26项非零），核所有跨度预算：
\[
 (199999997,199999998,199999996,199999998,
        199999998,200000000,200000000,200000000)/10^8.
\]
新费 \(b'=10^{-8}(14449,43085,66399,78242,78242,66399,43085,14449)\)，
\(\sum b'=B\)。两帧身份
\[
 F_9-c=\tfrac12[(F_8(h^-)-c)+(F_8(h^+)-c)]+2K(S)^2
\]
准确成立，所以已有连续证书只无损给 \(F_9\ge c\)。

在 \(g_r\ge4/5\) 上，所有核平方非负，最小费 \(d=14449/10^8\)，
\(F_9\ge(4/5)B+d(S-32/5)\)。
对目标 \(\delta=10^{-6}\)，独立有理核
\[
 S_\delta=2870483/72245,\quad
 U_r=(2465911/72245,\ 516091/43085,\ 891237/110665,\
       2721083/391210,\ \text{逆序}).
\]
每个 \(g_r\ge U_r\) 及 \(S\ge S_\delta\) 均直接支付 \(c+\delta\)，包括边界；
因此真正新证书的剩余范围是完整闭紧域，尾部不靠搜索准入。

旧 \(L=F_8-c\ge0\)。若任一帧 \(L\ge2\delta\)，完整 lift 已给 \(\delta\)。
否则两帧均落在 \(T_{2\delta}\)；High§5的完整连续 cover、真实 overlap 交集、
空集 Farkas 证明与全 span 核下界是充分方案，逻辑无缺口。
但旧 clear/large-gap/逆序叶只付 \(c\)，不是这个更强低集的自动 cover。
目前没有完成该 cover；指定小盒的严格 \(6.85\)–\(6.87\) 微余量只能给该盒结论
和固定 lift 的统一增益必要上界，不能认证全部紧域。
Arb 代码用弧度 sinc，\(Z_0=\sin\beta/\beta\)，未混用 normalized sinc；
核式、半径与直接36项／两帧算式正确，其包含性仍属明确计算信任范围。

如果将来全域补齐 \(c'=c+\delta<1/40\)，九点滑窗数 \(m-8\) 与每跨度预算≤2
给 \(c'(m-8)-B\,\mathrm{span}\)，小 \(m\) 由非负能量覆盖。
原 \(\theta=.8\) normalized majorant、近对和 pinching 均可原样消费；
近对核严格 \(>1/40\) 可先固定小平滑后支付 \(2c'\)。
因 \(|K_\varepsilon^2-K^2|\le2d_\varepsilon\)，新局部平滑损失≤\(32d_\varepsilon\)，
总损失≤\(32d_\varepsilon m\)，全滑窗端项只有 \(8c'\)；
先 \(T\to\infty\) 后 \(\varepsilon\downarrow0\) 全部消失。
条件比例公式 \((A_0-B)/(1-c-\delta)\) 正确，但任何 \(\delta>0\) 尚未准入。

## 3. 完整有限谱增强与真实二／三点量

保持全部零点和重数，\(P\) 是简单临界线单位列之和，**不是**正交投影；
\(Q=A-P\) 中重复点权仍为 \(\mu\)。有限指数独立性给
\(p=n_+(Q)=r+k,\ n_+(A)=n+p,\ n_-(A)=k\)，
\(S=N-n-2p\ge0\) 正是源中两个重数余项之和。
记 \(M_Q=\operatorname{tr}(Q_-),L_P=\operatorname{tr}(P E_Q)\)，\(G_-=\operatorname{tr}(A_-^2)+4\operatorname{tr}(A_-)\)。

逐项使用 \(H(\lambda)=4\lambda-\lambda^2=4-(\lambda-2)^2\)：
前 \(p\) 个正谱保留 \(D_{\rm top}\)，其后 minmax
\(\lambda_{p+j}(A_+)\le u_j(U)\) 给
\(H(\lambda)\le4u_j-\phi_2(u_j)\)；
剩余正项为零，负谱完整扣一次。独立相加得到
\[
 \operatorname{tr}A^2\ge2N-n+J(U)+G_-+2S+D_{\rm top}.
\]
真实 rank-\(p\) 投影 \(E_Q=1_{Q>0}\) 经 Ky Fan 给
\(\sum_{i\le p}(\lambda_i(A)-2)\ge S+M_Q+L_P\ge0\)；
Cauchy 因而给 \(D_{\rm top}\ge(S+M_Q+L_P)^2/p\)。
\(p=0\) 时 \(Q\le0,\operatorname{tr}Q=N-n\ge0\)，确为 \(Q=0,N=n\)，不除零。

带 \(P^{1/2}\) 的 Hilbert–Schmidt Cauchy 准确给
\((\operatorname{tr}P Q_+)^2\le L_P\operatorname{tr}(P Q_+^2)\le L_PV_{PQ}\)，
所以 \(L_P\ge[\operatorname{tr}PQ]_+^2/V_{PQ}\)；\(V=0\) 的零约定正确。
这里没有 opnorm 税，但实际已付输入只有 \(V_{PQ}\ll_\varepsilon N\log^2T\)：
局部重数计数给 \(\|P\|_{\rm op}\ll_\varepsilon\log T\)，
\(\operatorname{tr}Q^2\ll_\varepsilon N\log T\)，两份日志不能改名为 \(O(N)\)。
源(4)的线外 \(2\mu\operatorname{Re}K(\cdot+iy)^2\) 与三点 \(a^tDCDa\) 保留全部 signed 交叉；
ordinary whole pair-correlation 没有自动付它们的 typed 正下界或 \(O(N)\) 上界。

固定偶内窗 \(\tau\le f_\varepsilon\) 的前件在标准 cutoff 族可实现；
乘法收缩 \(M\) 给 \(Q_\tau=M Q_\varepsilon M\)，负迹 dual 给
\(\operatorname{tr}((Q_\tau)_-)\le M_Q\)，未使用负部算子单调性。
未归一内窗 trace 必为 \(m_\tau(N-n)\)，不能用于替代原计数 trace。
独立重算源(7)的 \(G,H,X\) 符号，其中
\(X_{iz}=-\tfrac12\operatorname{Im}[K(d+i(y_z+y_i))+K(d+i(y_z-y_i))]\) 正确。
完整规范 Gram 行和 \(\kappa<1\) 时，其逆≤\((1-\kappa)^{-1}I\)；
源(8)逐 \(h\) 的 Schur residual 与源(9)全 \(h\)-span 的 dual 下界均成立。
所有 Q 正列、真实重复权和远点仍保留；\(\kappa\ge1\) 时不能消费，条带没有证明该前件。

## 4. 实际重放、两次极限与条件目标

实际执行 C:\Python312\python.exe -B -X utf8 加脚本的 --check，退出码0；
输出：PASS conditional adaptive leverage algebra and committed report。
另独立 Fraction（不导入作者程序）重算全部九点预算、尾阈值、基准比例及目标负残差，退出0。
程序拒绝 -O，exact assertions 与整个 JSON 相等比较均实际执行。

令 \(\gamma=1-c,p_0=66812491/99194997\)，
\(h=(M_Q+L_P)/N\)。有限谱及498在每个 fixed \(\varepsilon\) 给
\(2h_T^2\le[\gamma_\varepsilon r_T-b_\varepsilon+o_{\varepsilon,T}(1)](1-r_T)\)。
源先对所有 \(r_T\) 作凹二次式上界，再依次取两次 limsup，
得 \(h^2\) 的上界 \(262156673710009/19838999400000000<.114954^2\)；
没有将 liminf 偷换成 limsup。
若另外证明尚未支付的 \(\liminf_{\varepsilon\downarrow0}\liminf_{T\to\infty}h\ge3/2000\)，
则 \(r_*=.67356\) 处
\[
 \gamma(r_*-p_0)(1-r_*)-2(3/2000)^2
 =-17817139237/62500000000000000<0.
\]
该凹式在 \([p_0,r_*]\) 的导数严格为正，排除整个区间，才条件性得到 \(r>67.356\%\)。
此目标超过499的**固定方法类** ceiling，不是违反任何实际 ζ 比例上界。
脚本／JSON明确不证明正输入、有限谱 lemma、解析运输；这些边界准确。
当前实际下界仍为498，九点统一 \(\delta\) 和归一 \(h>0\) 均未取得。
