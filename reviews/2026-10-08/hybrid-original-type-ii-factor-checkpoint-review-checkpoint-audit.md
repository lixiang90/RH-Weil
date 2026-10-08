# 原 Type II 因子归约与 MT 对角调节检查点：独立完整审查

2026-10-08。审查人：checkpoint_audit。结论：**限定 PASS**。

全文实读最终479摘要140行与最终检查器171行；另全文实读因子研究524行、
对角调节研究188行及其两份不同作者完整审查各160行，并回核476与478笔记。
独立重建实际系数分区、各成本和 MT 计数代数，再运行内存 Fraction、哈希、
链接和 guard 复算。没有修改作者源、旧笔记、原输出、核证书、论文或 Git。

## 1. 最终文件绑定

canonical UTF-8 LF 只统一 CRLF 与孤立 CR；不 trim，不改变 EOF。

| 本次文件 | canonical LF SHA256 | 字节 / 行 |
|---|---|---:|
| [479最终摘要](../../notes/479-original-type-ii-factor-reduction-and-diagonal-gauge.md) | 6b6e15f8a3a83d62e1d472cbeaa86a894c9e01740ccd682fc79ec99c2ec5a559 | 7029 / 140 |
| [最终有限检查器](../../scripts/hybrid_original_type_ii_factor_checkpoint.py) | bee0cb73218810e49a815daf7ff2c3bb398b063911d26baf93119d3d74cf149d | 9305 / 171 |
| [因子完整研究](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 | 21261 / 524 |
| [因子不同作者完整审查](hybrid-original-type-ii-short-lambda-factor-fourth-review-twisted.md) | d8d7df7390328a3d1dc4adb417f792dfd246776e0ac84567a4733db0c9792f88 | 11353 / 160 |
| [MT对角调节完整研究](hybrid-mt-six-neighbor-diagonal-gauge-and-actual-counting-research-compression.md) | 361c32d6e28cfd2e5c30516b42e58297f11f4516c77407de39c5f32b8af7c30b | 7312 / 188 |
| [MT不同作者完整审查](hybrid-mt-six-neighbor-diagonal-gauge-and-actual-counting-review-twisted.md) | b0878550dfeb1b2443772a47a197fd424f721d12fa14176a9c74c432b4c25416 | 7798 / 160 |

相对于首次审查版本，最后的摘要只把未完成的额外 compression 数学审查链接
改为已经全文实读的 twisted 审查；检查器只删除该额外文件常量、FILES 项和
review pair。算术、冻结输入、原对象、成本、比例与 scope 没有改变。
最终 REVIEW 路径指向本文件。上述两份完整研究和不同作者数学审查分别存在，
本审查没有以尚未落盘的文件充当证据。

## 2. 原对象、sharp endpoints 与各成本

最终摘要保留 \(X=T/(2\pi)\)、原正高度窗、normalizer、
\(U=V=\lfloor X^{1/8}\rfloor\)、\(Y=X^{5/6}\) 与原
\(\Lambda(m)b_V(k)\) 的全部符号。四项依次是全部 short m、large proper-power m、
large genuine-prime m 的 squarefull k、large genuine-prime m 的 non-squarefull k。
它们互不交，并覆盖原非零 \(\Lambda\) 支持；共同 \(Y<mk\le X\) 未改。

真实 divisor 展开后，short m 的内区间是
\((Y/(md),X/(md)]\)，其下端至少 \(X^{11/24}\)。统一对数和的三长度分支、
中段差分 \(|f_h''|\asymp hT/A^3\)、临界权 partial summation 与实际系数二矩
在研究源中分别支付。摘要没有将退化 Type II 乘积相位错误当成非退化二维和。
二矩费用来自真实长度至多 X 的系数 \(O(\tau_3(n)/\sqrt n)\)。

独立用有理数重算，置 \(a=1/8,b=1/4,y=5/6\)：

| 费用 | 实际指数 |
|---|---:|
| short m 的 sup | \(1/6+(a+b)/2=17/48\) |
| short m 的四矩 | \(1/3+a+b=17/24\) |
| 原 Type I 的四矩 | \(1/3+2a=7/12\) |
| squarefull k 的四矩 | \(\max(0,1-4a)=1/2\) |
| large proper-power m 的四矩 | \(\max(0,1-2b)=1/2\) |
| 冻结 lower block 的四矩 | \(2y-1=2/3\) |

最大 prefix 引理使用平方后的实际 product 长度 \(O(A^2)\)，故费用是
\(1+A^2/X\)。同层 block 的第四矩能量求和保留 \(2^{-j}\)，随后
\(\sum_j2^{-j/4}\) 收敛；两个 prefix 的差保留移动的共同乘积端点。
prime mask 必须放进实际系数重新使用此引理，摘要已列出
\(q=\Lambda1_{\rm prime}\)，没有从一个 signed 全函数范数删标签。

对 squarefull \(1<k\le V^2\)，\(\operatorname{rad}(k)\le\sqrt k\le V\)，
原全部非零 Möbius divisors 因而已收入，真实 \(b_V(k)=0\)。非零外因子从
\(k>V^2\) 起，内长度至多 \(X/V^2\)，产生 \(1+X/V^4\)。
proper-power 外权按整数项数支付，内长度至多 \(X/M_0\)，产生
\(1+X/M_0^2\)。两者均为完整原子族的直接 upper。

合成误差最大四矩指数是 \(17/24\)，L4 norm 指数是 \(17/96\)；
只在最后一次使用 \((u+v)^4\le8(u^4+v^4)\)，所以两向 coupling 中的8正确。
它不是两第四矩的 additive 等同。另独立核得
\(5/7-17/24=1/168\)、\(2/3-7/12=1/12\)、
\(8/21-1/8=43/168>1/4\)，而 \(17/24>2/3\)。
任意固定 \(\varepsilon\) 的费用需先分配小损失；声称显示幂严格低于5/7时，
仍须最后取 \(\varepsilon<1/168\)。

## 3. MT 对角代数与实际严格比例

单侧对偶允许 Hermitian \(B\preceq I\)。两个标量差式为
\((t-1-b)^2\) 与 \((1-b)(2t-3-b)\)，对 \(t\ge0,b\le1\) 非负；
凸标量 Jensen 在 B 本征基中给所用有限矩阵不等式，未要求 B 与 G 交换。
\(B=-eI+uK\) 的上方谱由 \(-e+uS=1\) 支付。
Gram 对角为1且 \(\operatorname{Tr}K=0\)，真实对角成本准确是 \(e^2n\)。

以 \(e=1/62500,S=51/50,\tau=19/5000,h=1/500\) 独立重算：

\[
u=\frac{62501}{63750},\quad
c=\frac{4062502499}{4064062500},\quad
\alpha=\frac{77187542279}{20320312500000},\quad
\eta=\frac{4062502499}{2032031250000}.
\]

七点覆盖后的端项必须是 \(6c\tau\)，且
\(6c\tau-6\alpha=6e^2>0\)。固定 profile 的线性误差准确是
\(2(1+e)n\epsilon_\delta\)。在最坏 \(\epsilon_\delta=1/10000\) 核得

\[
\alpha-\frac{2(1+e)}{10000}
=\frac{36561707377}{10160156250000}>0,
\qquad
\frac23(1/10-1/10000)^2-\alpha
=\frac{232041622759}{81281250000000}>0.
\]

全部单点簇形成一个主链，短簇由不交 pairs 付款；一次 pinching 不重叠计费，
也没有每簇端项。原完整重数与惯性预算仍保留全部离线正负块。
先固定 profile、再令高度趋无穷、最后趋原 MT profile 的极限顺序正确。

从冻结的 [C0有理输出](../../output/hybrid-multipoint-cap-exact-algebra.json)
两严格端点独立算出

\[
\frac{144883718717093990038447236655639983274406783850455}
{215261827327800757567083368853099932747578493370368}
<p_{\rm dg}<
\frac{72441859358546995019223618327819991669906394854915}
{107630913663900378783541684426549966373789246685184}.
\]

新严格下端减去冻结旧严格上端，准确为

\[
\frac{38202658750375724709585783275561655495674769405}
{223107690410244439578888423481057719096362234296731172864}>0.
\]

还分别在两个 C0 端点重建旧 \(p_6\)，核实效率增量和 same-budget gain 恒等式。
显示小数为 \(p_{\rm dg}=0.673058110281973178650699\ldots\)，
不同点下界为 \(0.836529055140986589325349\ldots\)，
严格增益约 \(1.71229681415865585\times10^{-10}\)；判定使用有理数，
不依赖浮点末位。不同点下界使用原第二条惯性预算，没有假定一般配置
都满足 \(D\ge(N+s)/2\)。

## 4. 检查器、冻结链、链接与 guard

完整核读最终 build 和 main。检查器首先冻结
[478已发布检查点](../../output/hybrid-mt-six-neighbor-proportion-checkpoint.json)
canonical SHA256
1d92dd0f51c361043d58207c62e50efc647671c52ce8c4f746830c40a0ea8c63，
随后逐项复核该记录的16个最终依赖，以及7个显式 FROZEN 值。
独立内存核算全部一致，C0 algebra 文件属于已验证的旧依赖，读取前即被冻结。
没有修改或重新执行原大核及七点覆盖。

FILES 最后一项确实是 SCRIPT，故 FILES[:-1] 对全部最终 Markdown 文件核查链接。
相对链接由各自文件目录解析；目前已有文件的局部链接全部存在，唯一生成前的
输出链接指向准确 OUT。此特例只允许本轮输出，不能宽泛豁免任意不存在的文件。
最终摘要没有未完成 compression 审查链接。

review pairs 分别绑定两个数学最终源、本最终摘要与最终脚本。
绑定是最终 SHA 在 review 文本中的检查，并由输出保存每个文件的完整快照；
它不解析审查人的 prose，也不代替本次实际全文审查。
本文件落盘前，真实 build 已在缺本 REVIEW 处报
`file exists: reviews/2026-10-08/hybrid-original-type-ii-factor-checkpoint-review-checkpoint-audit.md`，
所以不能仅凭源 hash 或另一个 PASS 越过最终审查门槛。

另以纯内存输出对象运行 main 的五个实际分支：已有输出拒绝覆盖；
`--check` 输出缺失拒绝；内容不一致拒绝；语义 JSON 完全一致接受；
首次生成写一次。前四种均没有 write 调用；该测试没有产生文件或 pycache。
`--check` 的比较是完整 JSON 对象相等，覆盖 snapshot、review pair、check labels、
有理区间和 scope，不认证 JSON 排版。正常生成仅在全部 build 检查后写 OUT，
已有 OUT 始终拒绝覆盖。

本文件是生成前的完整独审记录。本文件落盘后，由根线程首次生成本轮输出，
再独立只读执行真实 `--check`；该执行结果另向根线程返回，不回写本冻结审查。

## 5. 准入范围

[476](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md)
的 whole 四矩 \(T^{5/7+\varepsilon}\) 与
[478](../../notes/478-original-mt-six-neighbor-dual-and-whole-chain-proportion.md)
的原算子计数合同保持。引用输入下 \(\sigma_*\approx0.874957019420099\) 未变。
新比例推导没有使用原7/8条带，不是 detector 的 \(\kappa\)，不能替代
Hecke 全族 \(\beta_*\le(1+\kappa)/2\) 前件。

批准本轮完整原子族付款、Type I 强化、余项的精确收缩和同一 MT 预算内
实际极小严格比例提升。大 genuine-prime m / non-squarefull k 的完整 signed mixed4、
whole 常数四矩和联合解析桥仍未支付；没有新 whole 增长幂、无零边界、
边界论文、世界纪录或最优参数结论。有限检查器不认证无限解析估计，
也不重新认证冻结的大核或七点覆盖。上述 scope flags 与摘要和研究源一致。
