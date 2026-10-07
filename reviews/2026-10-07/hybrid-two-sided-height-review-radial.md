# 原四词双侧 height 逃逸：独立全文审查

2026-10-07。审查者 radial_review。

结论：**限定 PASS**。完整逆审(1)–(14)后，双侧 packet/短链逃逸、
左侧逆序伴随、bad guards 的 HS–HS traceclass 配对及全 genuine-prime
四词截带稳定性均成立。没有发现阻断性数学问题。

这是 raw actual 与 band actual、raw physical 与 band physical 的
稳定性。它不把原 P 换成连续 Fourier projection，不自动删除三个
内部 P，也不完成31、distinct22、高全异或全四阶常数。

## 1. 精确绑定及引用范围

下列 SHA-256 对 UTF-8 文本规范 CRLF/lone CR→LF 后计算。

| 对象 | canonical LF SHA-256 |
|---|---|
| hybrid-two-sided-height-escape-research.md | 854796abc5493cdc707ef8de03876548092e9cf919f4a9a90fc1f6f5ca5d73bc |
| hybrid-one-three-mixed-prime-sector-research.md | 5db2c614ab9d009a15a70f4e0639b95df2d59a6b56bd752216537fcf71e2b405 |
| hybrid-one-three-finite-band-admission-research.md | bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f |

被审对象为7,855 canonical bytes、194行。本次完整从头至文末独立
核对新证据对象，不以原单侧桥已经通过替代这份双侧证明。
原 finite carrier、C² 窗及 Fourier 正规化逐项与冻结输入一致。

本证明只用原 C² 窗的 uniform real-axis Fourier tails、
bounded frequency multipliers、Chebyshev genuine-prime绝对质量及
Schatten理想不等式。不调用[R]、高主区canonical小量、
unknown full fourth、有界moving-gap输入或新的prime cancellation。
没有改任何被审稿、旧文件、math、脚本、output或Git。

## 2. 原 packet 的两端尾与有限四词

V=F M_φ E，E为原isometry，unitary F与0≤φ≤1给∥V∥≤1。
列函数精确为(2πL)^{-1/2}hatφ(t−τ_k)，
τ_k∈[T,2T)，相对J^c和J_0^c均有固定正份额T的距离。
所以对任一outside cutoff，原C²尾给

\[
 \|1_{\rm outside}V\|_{\rm HS}^2
 \ll(d/L)\int_{|v|>cT}|v|^{-4}\,dv
 \ll(d/L)T^{-3}\ll T^{-2}.
\]

这是两端使用的HS界T^{-1}，而非每列未归一化后乘d的界。
d=floor(XL)、T=2πX的准确floor不影响上述uniform常数。

M_bad=D_R1_{J^c}同时在其左右支撑J^c，因此

\[
 V^*M_{\rm bad}V=(1_{J^c}V)^*M_{\rm bad}(1_{J^c}V).
\]

HS–bounded–HS给trace norm≤Cm_R/T²。
不需要M_bad正；signed或complex乘子也满足此Schatten不等式。
原/good compressed factors的op均≤m_R，四次telescoping于是
给(6)的traceclass稳定性T^{-2}∏m_R。
没有额外√d，也不需要四词迹自身有界。

## 3. 任意至多三个 K 的链逃逸

K=F M_{φ²}F^{-1}，其kernel为
(2π)^{-1}hatφ²(t−s)，正规化正确。
φ²二阶导数L1一致有界，所以
|hatφ²(v)|≤C|v|^{-2}。

对|v|>ηT的far部分：

\[
 \|K_{\rm far}\|\ll T^{-1},\qquad
 \|K_{\rm far}1_{J'}\|_{\rm HS}^2
 \ll |J'|\int_{|v|>\eta T}|v|^{-4}dv\ll T^{-2}
\]

对长度O(T)的任意J'一致。第一个是Schur/Young界，
第二个是真正compact input band上的HS界。K总op≤1，
故K_near总op≤2；每次near传播至多ηT。

在短链输入1_{J_0}V后，至多三个near jumps只扩展3ηT。
J_0=[.9T,2.1T]、η=.01给这个支撑位于
[.87T,2.13T]⊂[.5T,3T]=J。
all-near链的outside-J输出精确为零。

其余有限个词取从右数第一个far。far右侧只有near jumps与
diagonal frequency multipliers，故其输入确实仍在某个长度O(T)的J'。
先插入1_{J'}，far的HS≤C/T；其余operators只用bounded op，
V用op≤1。每个词因此HS≤CT^{-1}∏∥M_i∥。
右input1_{J_0^c}V另用其HS≤C/T同样支付。

所以(8)成立；这里不能仅用far op与∥V∥_HS≤√d，
本文没有这种损失。交替链至多三个K，有限词数和K_near的2幂
只给固定常数。

multipliers的频率变化再快也不传播支持。raw/good、adjoint及
complex conjugate multiplier都保留同一norm和diagonal性。
因此左侧逆序链可以使用完全相同的escape lemma。

## 4. 每个 physical bad guard 的左伴随与 S1

原physical四词展开为
V^*D_1 K D_2 K D_3 K D_4V；三次φ²卷积和两个原端点packet保留。
逐因子raw/good差额中，第i个bad multiplier的prefix/suffix记为
L_i、R_i，则

\[
 V^*L_i D_i^b R_iV
 =(L_i^*V)^*D_i^b(R_iV).
\]

左链必须是L_i的逆序伴随，不能用L_iV。
K selfadjoint；adjoints of diagonal multipliers仍满足上节前件。
左链含i−1个K，右链含4−i个K，所以每端均不超过三个。
端点i=1、4的一侧空链正是packet尾，没有例外漏项。

D_i^b=1_{J^c}D_i^b1_{J^c}，两端guards是准确恒等式，
不是人为改变了测量。应用(8)两次给

\[
 \|1_{J^c}L_i^*V\|_{\rm HS}\ll
 T^{-1}\prod_{j<i}m_{R_j},\qquad
 \|1_{J^c}R_iV\|_{\rm HS}\ll
 T^{-1}\prod_{j>i}m_{R_j}.
\]

同一个T的两端HS尾与m_{R_i}相乘，严格给
T^{-2}∏_{j=1}^4m_{R_j}的trace norm。
各项已是S1，四项求和给(13)。
这不是只对scalar trace的估计，整个physical compressed矩阵差额
也具有同一S1界。

没有用physical trace cyclicity；没有假称原P与D1_J交换。
左链的ordered adjoint还说明本估计允许复值/非正的原四词项，
无需另作positive-frequency或principal-height排除。

## 5. 全 genuine-prime第四词的量词与未付项

genuine primes≤X的全乘子m_all≤C√X/L。
因此原finite第四词与good finite第四词的差、
原physical第四词与good physical第四词的差，
各自绝对trace均≤Cm_all⁴/T²≤C/L⁴。
除d后为O(X^{-1}L^{-5})=o(1)，与(14)完全匹配。

该推导没有先假定任一完整第四迹有界。
对13、22、31任意有序ranges，仍按各自真实∏m_R支付，
所有signs、原sharp cut和finite floor均保留。
fixed profile先于T固定，C²/seminorm及band常数uniform于ranges，
没有目标后变换window或外部height预算。

两种比较分别是同类型对象内部的raw/good稳定性：
actual与actual、physical与physical。
它没有比较actual与physical，也没有控制其三个内部P的signed误差。
如果后续使用good band上的canonical q_R，仍需要相应[R]。
目前31的two-crossing power仍为正，不能从双侧尾另行宣布它闭合。

限定PASS只验收新的band稳定接口，不涉及proper powers、
背景/gamma替换、wholearithmetic saving、新比例或RH结论。

## 6. 463 综合笔记的独立全文审查

2026-10-07 追加。独立完整读取
[463](../../notes/463-two-sided-height-stability-for-original-fourth-words.md)
全部94行，逐项对照本报告已审的双侧高度研究稿。
最终 canonical LF SHA-256 为
6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90；
3673 bytes。该综合笔记限定 PASS。

§1 保留同一个原 interval finite-carrier \(E,P,\phi\)、unitary
Fourier transform、sharp genuine-prime 乘子及归一化。
\(D_i\) 可以是不同有序 prime ranges 的真实乘子；费用逐项使用
\(\prod_i\|D_i\|_\infty\)，没有将 \(P\) 变成连续频率投影或
与 \(1_J\) 交换。两个 boxed trace-norm 界分别针对 actual raw/good
以及 physical raw/good，比较对象准确。

§2 的 \(C^2\) packet 尾使用 \(d/L\asymp T\)，得两种外带
Hilbert–Schmidt 范数 \(O(T^{-1})\)。Actual 词的每个坏因子本身
属于 traceclass，有限替换用其余因子的 op 界，未假设完整四迹有界。
Physical 词的卷积核归一化、far op 界和长度 \(O(T)\) input interval
的 far Hilbert–Schmidt 界均与研究稿一致。

式 (5) 的链至多含三个 \(K\)：从 \(J_0\) 出发，三次 near jumps
仍在 \(J\) 内；其余词从输入端取首个 far，先支付 compact input
上的 Hilbert–Schmidt 范数，再用其他因子的 op 范数。
\(J_0^c\) packet 另以尾界支付。此证明适用于反向伴随链，因
\(K^*=K\) 且 diagonal multipliers 的伴随仍不扩大支撑。

在每个 \(D_i^b\) 处切开的左 prefix 必须取反向伴随，右 suffix
保留原顺序，两端各至多三个 \(K\)。坏支撑在两侧都允许准确插入
\(1_{J^c}\)，故 HS–bounded–HS 配对确实给
\(O(T^{-2}\prod_i\|D_i\|_\infty)\) 的 trace norm。四项相加支付完整
有序词，而非只估计其中一端逃逸。

全 prime \(m\ll\sqrt X/L\) 给 absolute \(O(L^{-4})\)，除以
\(d\asymp XL\) 是 \(O(X^{-1}L^{-5})\)，没有遗漏额外 \(d\) 因子。
§3 明确该结果不比较 actual 与 physical，不删除三个内部 \(P\)，
也不控制31、distinct22、高全异或完整四迹常数。未来若使用 good
band 上的算术 cancellation，仍须单独支付相应 [R] 输入。
本次 PASS 仅覆盖两种同类型对象的高度稳定性。
