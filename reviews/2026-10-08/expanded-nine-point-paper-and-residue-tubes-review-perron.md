# 扩大九点论文与真实互素 residue tubes：不同作者限定审查

2026-10-08，perron_reviewer。结论：**限定数学 PASS，无需修订当前冻结源。**
范围是给定 PC8 连续／编译计算准入下的完整九点结论，以及实际 Gram 的 tube 子项付款。
不把有限精确检查称为完整 Lean kernel 证明；不认证新的零自由边界、全局 arithmetic 四矩或优先权纪录。

## 1. 最终输入与读审范围

canonical UTF-8 LF：CRLF/lone CR→LF，保留 EOF。以下身份均独立读回。

| 输入 | 行／LF字节 | SHA-256 |
|---|---|---|
| [正式论文](../../papers/expanded-nine-point-tangent-simple-critical-paper.tex) | 418／18130 | e69b5c4a34cc2fd3ec5c606faa175a37763fbd64534305b1e616a510afcdae31 |
| [标准库 checker](../../scripts/am_expanded_nine_point_certificate.py) | 195／8854 | 05b7500d77bdb41cb5419137a1eee354250d7569572cd5c37d44a19a66b4eb4f |
| [完整数据](../../output/am-expanded-nine-point-certificate.json) | 380105／6252220 | 3a3c8b24015162a4835f5c1d8633a4f9f8bdace26d711631dd6374c689bce04f |
| [互素 tubes 源](original-coprime-product-residue-tubes-research-checkpoint.md) | 163／8815 | b157364cebd8e7f5fcff7af8801303a2ed1483fbbc73ee55a1ac399064ae2d81 |
| [原完整产品 Gram](original-product-fiber-short-window-research-checkpoint.md) | 174／10878 | 06f4d873d5a7b181c21dfd0284a82a3657a80a159d424783deac70da8fecf5ed |
| [quartic 边界合同](../../notes/306-quartic-boundary-and-equal-norm-corrections.md) | 158／7535 | bfbc9dda9f671aca3249f3c747638238a82507e9dc14b4db9ec320e201d3c1d8 |
| [实际相对稠密块转移](../../notes/228-relative-dense-zero-block-transfer.md) | 473／13618 | 2cc8a3f5eb0e66ef0a6306a317a1e2b03c046c62b8284a87ccbee8e8130181ae |

本轮 FULL READ 最终 418 行论文、195 行程序与163行 tubes 源；完整读取数据结构并程序化独立重建全部241捕获叶和2399矩阵／dual。
原174行及前九点828行曾在本审查者[前轮不同作者审查](nine-point-paper-and-product-fiber-review-perron.md)全文核准，本轮按其完整合同对照。
306§§1–2、228§5及原197有关边界公式本轮重读；下述 flat 门槛只消费这些明示前件。
原 NumericCore／PTL／REG 的连续语义沿用已披露准入，未重跑535m搜索或把原240项重新称作kernel定理。

## 2. 新切线与完整扩大覆盖

论文保持同一 AM13 密度、12个有理扰动系数、26个非零权重和 \(B=404350/10^8\)。
正密度且质量一保证真实平方 \(w=K^2\in[0,1]\)，这为全部 physical square 的有限 box 提供解析前件。
packed point 给 \(v\le w(p/SC)\)、\(d_-\le w'(p/SC)\le d_+\)，但这三个数本身没有全区间切线含义。
新增点逐一从原 \(\mathrm{PTL}_i\) 及其自身 PTF 取出；expanded interval 必须被同一原 REG 凸区间包含。
令 \(l\le q=p/SC\le u\)，两个安全线为
\[
 v+d_+(l-q)+d_-(x-l),\qquad v+d_-(u-q)+d_+(x-u).
\]
若 \(d=w'(q)\)，真实 tangent 与它们之差分别是
\[
 (d-d_-)(x-l)+(d_+-d)(q-l),\quad
 (d_+-d)(u-x)+(d-d_-)(u-q).
\]
各项非负。因此叶外已认证点在扩大 REG 区间内可用；不能任取跨 \(q\) 的两个 raw 导数线之最大值。
实际 \(L=U\) 时仍使用真实 singleton；常数 lookup 的 uc 扩展不是 tangent 的实际支撑。
程序的 positive pack、\(k<16\)、原表归属与 REG endpoints 检查均与该无限连续证明对应。

同一目标 \(c_*=805260/10^8\)，strong capture 为 \(c_L=805803/10^8\)。
只要任一旧帧不在 low set，
\[
 F_9\ge(c_L+c_0)/2=805403/10^8>c_*.
\]
原 COV 额外压力 \(\theta B=0.0032348\)、large-gap 额外压力
\(\theta(B-\max b_r)=0.002587136\) 均严格支付 \(c_L-c_0=0.000008\)；\(\theta=4/5\) 域没有旧 small-gap 分支。
原 walk 的返回值、guard、cursor 不变；clone strong 比较和 reward search fuel ten 只负责更宽 low set 的捕获。
最终论文220–224行准确限定原半空间 \(h_6\ge h_0\)：\(u_6<l_0\) 的 direction 叶在那里不可能含实际点，另一半由完整反射恢复。
因此241原胞加反射为482 labels；不是482互异 low domains，也不假设每个外胞都实际低。

我独立重建 \(482^2\) 全部 ordered intersections，shared gaps→4796，shared spans→2405，完整9个prefix差分闭包→2399。
35个实际距离约束使用 \(5SC\) 精确单位；负环排空，否则 shortest-path potentials 给实数可行性，无网格近似。
每个目标有8 gap和34共享 physical square，共42变量；三角关系、reflection、真实两帧共享变量均完整保留。
924 extra point occurrences／237 distinct points 全部独立核原表与凸区间；每个保留点至少有一条正乘子切线被实际消费。
移除零乘子 row 后只重编号，不改变 lower，也不声称 unused 全表具有新的已验语义。

## 3. 精确 dual、实际执行和信任范围

对每个 \(Ax\le b,\ \ell\le x\le u\)，我独推并逐记录消费
\[
 q^Tx\ge-\lambda^Tb+\sum_i r_i
 \begin{cases}\ell_i&r_i\ge0,\\u_i&r_i<0,\end{cases}
 \qquad r=q+A^T\lambda,\quad\lambda\ge0.
\]
因此 float 只提出乘子，最后无需 float 可行性、最优性、stationarity 或舍入后精确消零。
42个变量的完整 finite-box residual 均支付；objective 的量纲为 \(2\cdot10^8F_9\)。
我用独立标准库 Fraction 算式从全部 RAW／YA、原 point packs、REG、reflect 和约束重建所有2399矩阵及 lower，**未导入作者 checker**，实际退出0。
所有 rational lower 与冻结 JSON 一致，并均大于最终260目标。最小值及最终 margin 为
\[
 \frac{26386790900531855994044477203}{3276800000000000000000000000000},
 \qquad
 \frac{31220531855994044477203}{3276800000000000000000000000000}>0.
\]
旧253只是更保守选择；260由同一全域最小值直接支付，不需要新的 capture／LP。
final195程序全文读回后实际执行 \(\texttt{python -B -X utf8 ... --check}\)，**exit 0**，2399 exact domains 全通过。
另独立解析作者实际 --replay 的隔离日志：41项true、241 LOWCELL／LOWPAID／LOWRAW／LOWYA字段与冻结数据逐项完全相同，无error／panic／sorry。
该1035行／601017 LF字节日志 SHA为 4b939f71d75e98ab5f6cf974c529eb1b7f3e33cecd5f36a770ec1a116626a87d；
其 capture source SHA为 246328e2e6f30dad79b56f070ff98b8cc438a1cd5e7e67b3d3f1bc3b81615f9c，与JSON绑定一致。
本审查者没有再次运行Lean capture；作者 final --replay 实际exit0与我的日志独立字段核对应区分。
程序拒绝 -O、绑定全部依赖hash；--check 为储存有限数据验证，--replay 才增加原表来源和runtime捕获比较。
两者均不消除原 point／convexity／continuous minorant 及 compiler/runtime 准入，也不引入论文2610.08965的headline native-computation公理。

## 4. 全谱、端项和精确比例

新九点权重保持每个 index-span capacity≤2、总gap压力B；total local pair weight<16。
完整 sliding 给 \(c_*(m-8)-B\operatorname{span}\)，短集／空集仍有效，不偷删边界8\(c_*\)。
固定 smooth \(f_\epsilon=f\chi_\epsilon^2/m_\epsilon\) 的 majorant 是 \(g/m_\epsilon\)；
先取 \(m_\epsilon>61/64\)，Gram norm≤\((61/32)/m_\epsilon<2\)，不能把raw majorant的质量误当 normalized Gram bound。
每平方差≤\(2d_\epsilon\)，因此 sliding 的 \(32d_\epsilon m\) 和pair的 \(4d_\epsilon\) 足够。
近pair仍 \(K>134/825,\ K^2>1/40>c_*\)；两点Gram谱在[0,2]，全部 maximal close pairs与剩下separated集通过凸 \(\varphi_2\) pinching 合并。
于是完整 \(J(U)\ge c_*n-B\operatorname{span}-8c_*-32d_\epsilon n\)，没有把简单临界线子集替代全部零点谱。
全零点 Hermitian／real-type operator 保留重数与全部off-line反射pair；inertia及threshold trace给
\(\operatorname{tr}A^2\ge2(N-n)+\operatorname{tr}\varphi_2(U)\)。
固定smooth的 BGST 公式、weight removal 与前论文一致：先 \(T\to\infty\)，再 \(\epsilon\to0\)。
其证明依赖此前全文核验的 [BGST Lemma5](https://arxiv.org/html/2306.04799v1)、[§3更正](https://arxiv.org/html/2501.14545v3)及 [Lamzouri §3](https://arxiv.org/html/2609.02882v1)；
本轮没有将此解析链改成有限枚举或把 \(7/8\) strip 当实轴大筛间距。
原 AM 能量公式与严格 numerator 下界未变，故
\[
 p_*=\frac{66812491}{99194740}
 =0.6735487284910470051133759713468678\ldots.
\]
两项comparison独立Fraction核准：相对前九点增 \(10489561087/9839612017241780\)，
相对Knaus固定v1增 \(517622017/49164781738860\)，分别约0.0001066054及0.0010528309 **percentage points**。
credit正确区分原AM数据、Knauslossless机制、此前joint论文和本轮新增切线；不声称穷尽全球最新优先权。

306原quartic合同还要求 \(E_1/N\to0,\ m_0,m_1\to1,\ 0\le b_2<1\)、正分母和分支范围，不能丢有限边界后只比较数字。
仅在 flat \(b_2=1/3\) 且这些前件全满足时，\(\kappa_4=4/[9(B_4+1/3)]\)，故要严格超过本新比例需要
\[
 B_4<\frac4{9p_*}-\frac13
 =\frac{196341487}{601312419}
 =0.3265215897694605905021229904117\ldots.
\]
这是假设输入的比较门槛；228实际MT／AM合同需消费其真实 \(b_2\)，本审查没有证明任何新的arithmetic \(B_4\)。

## 5. 互素 residue tubes 的独立解析审查

163源保持实际四高素数、全部 \(\nu\) weighted2 tails、原 \(\varphi/g\) L¹包络、三packet、全部 \(\Omega\) 与sharp区间。
真实 \(d_k\) 允许square产品及最多两个有序factor pairs；\(A_\gamma=\sum|d_kD_\gamma(k\bmod q)|^2\ll J\) 从原174合同消费。
完整slow phase保留在 \(L_q((k'-k)/q^2)\)；a=0只是正norm延伸，不新增真实unit零频。
整数核的非零 \(q\mid h,\ |h|<q^2\) 严格为0；这只属于完整a-Gram，不能称原masked residue普遍正交。

我逐步重推(4)全行：唯一 \(h=mq+d,\ |d|\le H\le q/4\)；\(m=0,\pm q\) 全付q，包括靠近 \(\pm q^2\) 的wrap。
其余 \(a_m=\min(|m|,q-|m|)\) 给 denominator≥\(3a_m/(2q)\)、numerator≤\(\pi|d|/q\)，故核≤\(3|d|/a_m\)。
对d与正负m完整求和即源中 \(3q(2H+1)+12H(H+1)(1+\log q)\)；删实际不存在／非互素pair只减少absolute row。
对称Schur \(2ab\) 及原 \(A_\gamma\) 给 tube absolute contribution \(\ll qJ(H+1)\log(2q)\)，没有称tube为PSD子norm。
全q、参数正包络、三packet聚合后 \(E_{\rm tube}\ll Q^2(X/S+1)(H+1)L^C\)，
原外F正Parseval与 prefactor \(S/(QX)\) 精确恢复费用 \(\sqrt{QS(H+1)/X}\,L^C\)。
由 \(QS\gtrsim X^{9/5},\ q\gtrsim X^{9/10},\ B<17/20,\ \eta<2B-1\)，
\(H=\lfloor X^{1+2B-\eta}/QS\rfloor\le q/4\) 且 \(H+1\ll X^{1+2B-\eta}/QS\)；+1及两个edge没有漏付。
因此该实际Gram子项确实付 \(X^{B-\eta/2+\epsilon}\)，预先 \(\epsilon<\eta/4\) 可得严格saving。

完整coprime余额精确为 outside tubes 的 signed \(C_{\rm out}\)，只能在全部q／packet／参数聚合后取一次正部。
(10)保持 \([C_{\rm out}]_+\)；原 \(\Omega\) 可缩正norm，不能从signed whole结论限制这个covariance子项。
我独推短差展开的 \(e_q(+bk)\)、\(e_q((j+b)h)\) 符号，以及
\(p'r'-pr=h,\ r=r_0+p't,\ r'=r'_0+pt,\ pr_0\equiv-h\bmod p'\) 的完整整数解。
实际prime约束／跨腿互素／square／sharpendpoint仍保留；小非零差的coprimality不代表其相关已付款。
两点s修正、共同 \(\nu\) 恢复与graph/chirp/nn范围沿原合同保持 \(X^{1/2}L^C\) 费用。
故这是**真实部分算术付款 PASS**，没有支付完整coprime余额、原四高素数whole主项或任意signed子族。

## 6. 结论

最终版本无未解决阻断。论文的新uniform260 reward及其全零点比例运输在披露准入下成立；
tubes 新partial payment成立，外部相关和更强whole四矩仍是明确未付输入。
本报告不评价新PDF版式、不重复大搜索，也不修改任何作者源、旧冻结报告、index、cadence或Git。
