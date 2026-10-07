# 原有限高素数重复四词：根节点全文独立审查

2026-10-07。审查人：root。
被审稿：[高素数报告](hybrid-high-prime-four-word-response-research.md)，
canonical LF SHA256
988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666，
19170 bytes、572 行。

结论：**PASS，限于原有限压缩 repeated-index sector 的一侧预算 [T]。**
它不证明完整四矩、额外零点比例或无零边界，也不认证 AF 的整个源定理。
本文逐段读取并重推主要恒等式和渐近费用，不以小模型替代分析。

## 1. 原算子和正规化

E 的 carrier exp(iTu) 保留，grid 的 step 为 2π/L，d=⌊XL⌋。
Plancherel 准确给 F=𝓕 Mφ E，F*F≤I。
原 M_hi=−π⁻¹Σλp cos(t logp) 与 2π/(a_LL) 压缩相乘，
两个 cosine exponent 的各系数是 −λp/(a_LL)，所以正文 Bp 正确，
没有额外 2、π 或 L。d∼N 足够；源的过强 d=N+O(L) 余项未使用。

零延拓下 logp>L/2 使相邻同向跳全部为零，正负输出处在 I 的两半，
故 Bp² 为正文 (9) 的 multiplication symbol，||Bp||op≤bp。
这个结论针对 physical Bp；Cp² 与其压缩的差 (11) 是真实正 leakage，
正文没有把 finite Cp² 免费替换为 multiplication。

## 2. 原 finite projection 的费用

对 a_s(u)=φ(u)φ(u+s)，wrap 区准确为零。
因此 carrier 共轭后的 circle rotation 只是计算原 P 的工具，
与 P 交换而没有改变 physical translation。端点 taper 保证 integration
by parts 不产生边项。

normalized Fourier coefficients 依次为
O(1)、O(1/|n|)、O(L/n²)，一阶与二阶 L¹ derivative 统一有界。
crossing count 为 min(d,|n|)，于是
Σmin(d,|n|)|â_s(n)|²=O(log(2+L))。
先各 Bp 付款，再 triangle，不假设不同 p leakage 正交：

~~~
Σp ||Q Bp E||HS² = O(log L);
||Q B E||HS² = O(X log L/L²) = o(d).
~~~

d_L 的 derivative 同样统一，Σbp²=O(1)，故 (17) 合法。
这只是二次泄漏；不能从它推全四阶的 projection removal。

## 3. carrier 与实际四阶量

对于 logp−logq，跨度<L/2，无 alias。
在有限 Kd 的 csc 项中分离 L/(πs) 与 O(|s|/L) 后，
前者的两个 endpoint phases（含 T）可直接放进 Hilbert coefficients，
后者按绝对系数求和。频率间距≥1/(2p)，
Σp log²p≪X L，最终 O(1/L) 点态 error 正确。
这不是无限 sinc 或把 finite carrier 取平均。

正负物理输出分离保证 Tr(E*B²E) 与
Tr(E*B Md_L B E) 的 diagonal 分别是 d〈d_L〉和 d〈d_L²〉。
后者在用 BE=EC+QBE 比较时，包含的 cross term 由
||C||op ||P Md_L Q||HS ||QBE||HS 支付，
是 O(X log L/L²)，不是未证明的 O(N) 第四矩。
因此

~~~
T0  = d〈d_L²〉 + O(d/L+X log L/L²);
T22 = d〈d_L²〉 + O(log L).
~~~

同一主项的证明保留了原 finite P。Tr C²=O(d) 独立先证，
后续 Tr|C|=O(d) 不循环调用待证的 Tr C⁴。

## 4. pqpq 的实际路径和三个投影

每个 internal P 从左到右删除时，Q 的右侧仍有 B_rP。
单词的 HS error 至多
O(√(d log L) bp²bq²)，两 prime 求和系数可控，
故删除总费 o(d)。这个合法 coefficient budget 无法覆盖四 distinct primes。

删除后只有两种 alternating sign pattern。
对 +−+− 的最终位移 S4=2(logp−logq)，若 S4≥L/2，
S3=S4+logq>L；若 S4≤−L/2，则 S1−S4>L。
故每条非零 physical path 都有 |S4|<L/2，原 grid alias 确实不存在。
整数 gap majorant
Σ_(√X<n<m≤X)1/[nm(m−n)]≪L/√X
足够付掉 p≠q 项。p=q 由 dΣbp⁴=o(d) 支付。
所以 T×=o(d)，未借用 prime-pair independence。

## 5. partition、显式 coefficient 和符号范围

trace cyclic words 上的 partition Möbius 系数：
六个 single pairs +1，三个 double pairs −1，四个 triple blocks −2，
全部相同 +6。四个 adjacent pair traces 是 T0，两个 opposite 是 Topp，
两个 adjacent double partitions 是 T22，另一个是 T×。
正文 (36) 的

~~~
Srep = 4T0+2Topp−2T22−T×−8T3+6T4
~~~

正确。Hermitian HS Cauchy 给 |Topp|≤T0；
Σ||Cp||op³=O(L⁻³)、Σbp⁴=O(L⁻⁴) 与已证 Tr|C|=O(d)
使 T3,T4=o(d)。由同主项得
−o(d)≤Srep≤4Sψ d+o(d)。
Srep 本身不是逐词 positive，正文对此限定正确。

Mertens measure 是 r dr，包含 bp² 的 a_L⁻²，
而 physical 窗给 ψ(v)ψ(v±r)。正文 dψ 正规化正确。
endpoint taper 宽度 O(1/L)，integrand 的 total variation 统一，
所以 squared-symbol average 的 error 为 O(1/L)。
indicator 的 dψ(v)=(|v|+v²)/2，
2∫₀^½dψ²=19/480，4Sψ=19/120。
MT 的 antiderivative r sin(c(r−v))/c+cos(c(r−v))/c²
在两个端点给正文 (44)。数值仅展示，严格结果是该积分，
不能视为有理区间认证。

## 6. 完整目标的余项

全文只将 pqpq 聚合的 P removal 付清。
四 distinct 的矩阵 sector 保留所有 P；不据此认为 physical sum 与
compressed fourth 有相同主常数。scalar Jensen 的 one-sided 路线合法，
但剩余 physical alternating correlation 仍未估计。
全 height 正积分尾的量级 O(L⁻⁴) 也正确，
不支持任意 matrix fourth 按 J/Jc 无 cross-term 分拆。

低通道、proper powers 和 background 的 mixed terms，
common centering、跨 cells 与 alias 均未因 Srep 付款而自动完成。
可以把本结果登记为 repeated-high sector 完成，不能登记为 MOM-1、
67.3% 或 RH 完成。本审查未运行外部 kernel，也未改变原源或冻结论文。
