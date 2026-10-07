# 原有限矩阵重复高低四词：根节点独立全文审查

2026-10-07。限定 PASS：exactly two high/two low、且高标签或低标签
相同的整个 union，实际主项为 4D_HL,ψ+8J_HL,ψ。没有完整四阶预算。

## 1. 最终对象和检查范围

独立全文读取
[研究稿](hybrid-low-high-mixed-four-word-research.md)，最终 canonical LF SHA：

~~~text
71f62b2dd931cfda012e7dad9c4efcfece63f5cf1bb8ff5b466d3e2ac1ae89f9
~~~

22126 UTF-8 bytes、589 行；canonical 仅 CRLF、孤立 CR→LF。
数学审查期间指出 bounded-multiplication finite bridge 需明列，作者已经补入。
最后 formula 的排版及通过状态变化为元信息；最终全文包含该正确 bridge。

定义与同一 [AF v2 §2](https://arxiv.org/html/2608.13637v2#S2) 相容，
使用原 finite d、carrier、C² taper、sharp prime weights 和零延拓。
Hilbert 输入为发表的
[Montgomery–Vaughan Theorem 2](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)，
Chebyshev/Mertens 为经典输入；本报告不重证其一般定理。
项目两个旧接口与原 AF PDF 的哈希已经明列在主稿，保持旧版。
本推导不需要新 zero-free [R]。

## 2. 独立复算

**有限词与正负号。** 六种高/低位置的 cyclic partition 给 R_H=4A_H+2O_H，
R_L=4A_L+2O_L，交集为 4A_HL+2O_HL。按 inclusion–exclusion，主稿(9)正确。
这些是有符号 sums，不能当作正的独立预算。实际四移位核、五个位置权重、
carrier phase 和 span 条件均保留，alias gap 的 overlap 长度没有丢掉。

**Hilbert 合同。** composite p²q/p²r 与另一组 prime frequencies 不相交；
local spacing 必须在两集合 union 上计算，整数间距给 δ_n⁻¹≤2n。
主稿使用单侧 m≤X 或 m≤2X 的矩形，features 在变量替换后确实可分。
weighted energy p²Σ_(q≤2X/p²)q b_q²=O(X/L)，prime 侧亦 O(X/L)；
频率总 span≤L/2+log2，finite csc 的主项与 bounded remainder 可各支付。
不能将同一方式免费推广到 pair-dependent cut 或四 distinct sums。

**真实二矩。** high/low 各自同号差频跨度<L/2，Hilbert 给 o(d)；
low 正负和频率用实际 output overlap，high 两种输出分离。
故 ||Y P||HS=O(√d) 在使用 P 删除引理之前已经支付，没有循环。

**三个 internal P。** 根节点逐个删并以右 P 和相应 HS 因子复算，
三个误差分别由 a_i²Y₂ l_Y、a_i yY₂l_i、
l_Y(a_i²Y₂+a_i y l_i) 控制。Σa_i²=O(1)、Σa_i l_i=O(√logL)
使其聚合为 o(d)，关键是 repeated label 的平方权重。
adjacent 的 positive leakage、D_phy 的有界性及 HS crossing 也成立。
新补的 multiplication bridge 将 Tr(E*M Y²E)、Tr(E*Y M YE)
分别与同一个 finite compressed trace 比较，支付
O(l_Y²+y l_Y√logL)=o(d)；这一步避免了不合法的 physical cyclic rotation。

**low 的非 local square。** Σlow B_p² 的 ±2logp 项没有删除。
主稿(23)–(24)的两个 variable changes 逐点正确；第二式的额外
φ(v+logq)² 已保留。same-sign adjacent high steps 正确为空，
其余 near composite–prime 项由上述矩形 Hilbert 付款，
far m>2X 有 fixed displacement 并用实际 overlap 支付 O(L⁻²)。

**两张16-sign表。** 根节点逐行重算 cumulative positions：
high-repeat 的 ++--/+--+ 保留 q=r square paths，q≠r 的 features 可分；
2logp−logq−logr 的小位移不能直接套 fixed-gap 界，主稿将 real √X
附近不足一个整数间隔的情况先付 O(L⁻²)，余下整数 harmonic 和为 O(L)。
low-repeat 的 composite–prime 两项与其不同 common factors均正确。
2logp−logq−logr<0 的 near 区 q,r≤2√X 用
(q+r−2p)/(2√X) 与整数双 harmonic sum，far 区用 fixed log2 gap。
这些均得到 o(d)，保留了 alias gap；没有假定 √X 与 primes 有固定距离。

**交集和 constants。** pair-weight P deletion 可以用 Σhigh b_p²Σlow b_q²，
不是整个四词的 ℓ¹ mass。high square 为 multiplication，
low 的非 local 部分在 intersection 中按非零位移付款。
四个闭合 orientations 的 carrier 准确为1，原 physical square corners
经 translation/reflection 给同一 J_HL,L。
prime-square measure r dr、固定 profile 和 taper 的极限给主稿(36)–(39)。
根节点另用 Fraction 精确积分得到

\[
 D_{HL}=23/960,\qquad J_{HL}=1/640,\qquad
 4D_{HL}+8J_{HL}=13/120 .
\]

四个 finite corner paths 是实际 main，不能调用 high-only alternating
word 的 o(d) 结论把它们删去。

## 3. 有限审计与准确未付对象

[独立精确脚本](../../scripts/hybrid_background_exact_audit.py)从标准库
Counter/Fraction 出发枚举高、低标签数各1、2、3的九个模型，
核对 union/intersection 的完整 cyclic coefficients，
并计算以上有理积分；[输出](../../output/hybrid-background-exact-audit.json)
绑定最终主稿与脚本。有限枚举不认证 infinite Hilbert、projection 或
prime asymptotics；连续付款是本次全文审查的纸面范围。

最终限定 PASS：主稿(1)的 actual repeated 22 union limit。
以下仍未付：22 distinct、13/31 的 whole sums、high four-distinct，
全部 proper-power mixed transfer、whole F_T、实际 AC³ 与全比例链。
不能将 13/120、旧 high upper 与 low Jensen upper 直接相加为完整四阶常数。
没有新零点比例、无零边界、RH/RR 或外部 kernel 验收。
