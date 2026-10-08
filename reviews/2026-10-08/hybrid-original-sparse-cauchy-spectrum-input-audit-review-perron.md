# 稀疏Cauchy谱能力审查：不同作者全文复核

2026-10-08，perron_reviewer。限定数学 PASS。
只新增本peer；没有修改作者源、Git、index、cadence或任何冻结输入。

## 1. 全文读取与冻结身份

FULL READ [root作者源](hybrid-original-sparse-cauchy-spectrum-input-audit-research-root.md)
全部184行，8156 canonical UTF-8 LF bytes，SHA256：

0dfa2258dcecef3584113aad950bade91502214a6081fe55f2a4b5a9bfb78944

本轮也全文读取189、453、184密度和188原ν输入，逐项重核作者身份表：

| 输入 | 行数 | canonical LF SHA256 |
| --- | --- | --- |
| [上端包](hybrid-original-squarefree-upper-cauchy-packet-research-perron.md) | 189 | f53579b62f4a47418644109893afc3de1c6dd6124e361ec713bbf0003403df43 |
| [固定包与全包二阶](hybrid-original-squarefree-signed-zero-gram-research-perron.md) | 453 | 0b126138c7bf42e9be3c4352b099a6ab37d88cef93af20593593c8e849aa2a17 |
| [密度全分段](hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md) | 184 | a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d |
| [原ν](hybrid-original-squarefree-carrier-fourth-near-research-perron.md) | 188 | 2142645eed724da49a3e6faae7068adb2c8ca907c196a691f09a2b7a7fd6f3ae |

LF身份只转换CRLF/lone CR，不trim。全部本地链接可解析；
494的引用只提供比较背景，未被模型当成实际算术身份。

## 2. 抽象谱计数合同

固定 \(5/6<\theta\le7/8\)，\(b=3(1-\theta)/(2\theta)\in[3/14,3/10)\)。
高点K及实部反射点均简单；临界线单一lattice有 \(N_0\asymp TL\) 点。
共轭高度只加到整个对称谱，未重复加进固定负高度包。
每单位高度局部计数 \(O(L)\)，临界线简单点比例趋于1。
Ingham及Huxley两段的指数下界至少3/7；
Ivić段单调降到b，故每个所用固定σ密度上界均与模型相容。
σ=1/2用 \(O(TL)\)，σ>θ无点；没有声称密度或精确ζ计数实际饱和。

## 3. 原相位下的分离峰

最近点之外的第r个点距t至少固定倍数rH，允许最近点并列。
因而作者(4)的全部其余项为 \(O(A\log(2K)/H)\)，对任何模1相位成立。
最近单项的p次方全实轴积分为 \(O_p(A^p)\)，\(p=2,4\)。
在J的Voronoi片上求和，得到 \(O(KA^p/T)\)；
背景误差相对它为
\[
 O\!\left((K/T)^{p-1}\log^p(2K)\right)=o(1),
\]
这里使用实际固定幂 \(K=\lfloor T^b\rfloor\)，不是只靠抽象 \(K/T\to0\)。
互不相交的 \(|t-\gamma_j|\le1\) 上自身至少cA，其余o(A)，
故给同阶下界，不需要删去交叉项或随机相位。

这些峰位于 \([1.3T,1.7T]\)，大T时连同宽1邻域处在原ν正core
\([1.2T,1.8T]\) 内。原ν在该处 \(\asymp1/T\)，全支撑上 \(\ll1/T\)，
于是作者(6)的二、四阶同阶结论也确实适用于原ν。
指数(7)严格为负；名义值分别为 \(-1/28\)、\(5/7\)。

## 4. 全entire包与背景

连续整数k的临界lattice使 \(|S_0(u)|^2\) 周期为L。
任意整周期积分准确为 \(LN_0\)，因为所有非零整数频差积分为零。
两端频率区间长度小于L，非负积分及全实轴Plancherel给
\(T^{-1}\int_J|Z_0|^2\ll1\)，没有把原J当成整个实轴。
局部计数与entire核还给 \(\sup_J|Z_0|\ll L\)，故背景四矩为polylog。

高点Y端按同一分离峰上界支付，四阶相对X端小
\((z_0/x)^{4a}\to0\)。反射点实部分母为−a，远离零；
其两个单端模长估计相同而幅度分别为 \(x^{-a},z_0^{-a}\)。
完整L²三角给全Z二阶 \(O(1)\)，完整L⁴三角的正反向界给
全Z四阶 \(T^{B_I(\theta)}/L^4\) 同阶，原ν版本也成立。
以上是独立支付各完整部件后运输完整函数差，没有signed子包单调推断。

## 5. 结论的严格范围

限定 PASS，无需修源。模型确实排除从列明抽象数据统一推出固定四阶省幂；
它比只比较密度费用提供了一个实际范数达到该幂的抽象谱族。
模型随T成族，不包含真实Euler乘积、精确零点计数余项、
实际有限素数系数、Perron全纯修正或Hecke全族算术。
因此它不是实际ζ反例，不反驳更强的实际算术四阶估计，
没有新的whole增长、中心常数、比例或无零区域，也不能撤销既有引用成果。
