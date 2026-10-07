# 原四词双侧高度稳定性独审：compression_bridge

2026-10-07。结论：**PASS，保留原 E、phi、全高度 multipliers 与内部 P**。
本接口不借 [R]、whole fourth 有界或新 prime cancellation。
只新增本独审，不改源研究、旧 notes、论文、math、Goal、脚本、output 或 Git。

全文核对
[two-sided height 源稿](hybrid-two-sided-height-escape-research.md)，
canonical LF SHA256
`854796abc5493cdc707ef8de03876548092e9cf919f4a9a90fc1f6f5ca5d73bc`，
7855 bytes / 194 lines。LF hash 仅将 CRLF 与 lone CR 换成 LF。
另在末节绑定正式笔记 463，原源报告和较粗 finite-band 桥均保持冻结。

## 1. Packet normalization、bad center 与 finite traceclass

保持原 `X=T/(2pi)`、`L=log X`、`d=floor XL`，tau_k 在 [T,2T)，
V=F M_phi E 为 C^d 到 L²(R) 的 bounded operator，op<=1。
unitary Fourier 与非 unitary hat 的 normalization 给每列
`(2pi L)^(-1/2)hat phi(t-tau_k)`。
原 C² zero-extended phi 的 second derivative L¹ bound 给

\[
 \|1_{J^c}V\|_2^2+\|1_{J_0^c}V\|_2^2
 \ll(d/L)T^{-3}\ll T^{-2},
\]

其中 J=[T/2,3T]、J_0=[.9T,2.1T]，两者距 carrier heights 的补集
都有固定 cT gap。HS 两项均为 O(T^-1)，不是 O(sqrt d/T)。

frequency multiplier Dbad=D1_Jc 满足精确双 guard：

\[
 C-C^g=V^*D_{bad}V=(1_{J^c}V)^*D_{bad}(1_{J^c}V).
\]

任意 bounded signed/complex D，Schatten HS–HS 给
`||A*D A||_1<=||D||||A||_2²`，无需 positivity。
因此单个 finite matrix trace-norm 差 O(m/T²)。四词逐因子 telescoping，
其余 raw/good compressed factors op<=对应 m_i，故 trace-norm 差
`O(T^-2 product m_i)`。该证明不引用原四词 trace 本身的大小。

## 2. 任意至多三 K 的 escape HS bound

K=F M_phi² F^(-1) bounded selfadjoint，op<=1。
其 kernel `(2pi)^(-1)hat(phi²)(t-s)` 的 C² envelope 给，eta=.01，

\[
 \|K_{far}\|=O(T^{-1}),\quad\|K_{near}\|\le2,
 \quad\|K_{far}1_{J'}\|_2=O(T^{-1}).
\]

最后一项对任意固定 length O(T) 的 source interval J' 一致，
其平方是 `|J'| int_|v|>etaT |hat(phi²)(v)|²dv/(2pi)²=O(T^-2)`。
这里限制的是源变量，另一个变量在整条实线上；没有把远场目标截短。

对于由<=3个 K 和 bounded diagonal M_j 组成的交替链 A，
先将 V 分成 1_J0 V 和其 HS 尾。尾项以 A 的 op norm 控制。
对带内 input，展开 near/far：all-near 至多传播3etaT，源 support 仍在
[.87T,2.13T] subset J，故其 1_Jc escape 准确为零。

每个其余词从右取首个 far。此 far 之前的 near chain 仍支撑在固定
length O(T) 的 interval J'；其 op 由有限2的幂乘对应 multiplier norms
控制，而 `||1_J0 V||<=1`。因此可使用 Kfar1_J' 的 HS O(T^-1)，
此 far 之后全部因子取 bounded op，得到

\[
 \|1_{J^c}A V\|_2\ll T^{-1}\prod_j\|M_j\|.
\]

没有在该处以 V 的 HS sqrt d 替代其 op<=1。
链中所有 multipliers 可为 raw、good 或其 complex adjoints；它们只改变
值，不扩大 support。K 自身 selfadjoint，所以 reverse adjoint chain
仍是同一种至多三 K 的交替链。empty chain 对应原 packet tail。

## 3. Physical telescoping 中的正确左伴随

原有序 fourword 的 frequency matrix 是
`V* D_1 K D_2 K D_3 K D_4 V`，这是原 M_phi² 内层卷积，
没有把三个内部 P 插入这个 physical word。
逐 factor raw/good telescoping，每项在 D_i^bad 中心处写

\[
 V^*L_iD_i^{bad}R_iV=G_{left}^*D_i^{bad}G_{right},
 \quad G_{left}=L_i^*V,\quad G_{right}=R_iV.
\]

左侧必须是 prefix 的反向伴随；源稿准确保留这一 order。
它有 i-1 个 K，右侧有4-i个 K。因 bad 中心是同一 Jc 上的 diagonal
multiplier，两端都能准确插入 1_Jc，不是只在一端取尾。
上述 escape lemma 分别给

\[
 \|1_{J^c}G_{left}\|_2\ll T^{-1}\prod_{j<i}m_j,
 \qquad
 \|1_{J^c}G_{right}\|_2\ll T^{-1}\prod_{j>i}m_j.
\]

两个 operator 都从 C^d 到全直线 L²，guard 后 HS。Schatten 配对给
整项 matrix trace-norm `O(T^-2 product m_i)`，有限四项相加同阶。
端点 i=1、4 有一个空链，也是 packet escape O(T^-1)，未漏掉。
所有 products bounded，HS 因子已明确；traceclass 无 domain 漏洞。

## 4. 全 prime 与范围

对原 genuine-prime p<=X 总 multiplier，Chebyshev 给
`m_all<<sqrt X/L`。所以 finite/physical 两类 raw-good fourth 差
各有 trace norm `O(m_all⁴/T²)=O(L^-4)`，normalized 为
`O(X^-1 L^-5)=o(1)`。将 range 取 high/low 任意顺序亦得到相应 product m_i。
这是直接对原 range-sum operator 使用绝对 op bound，不逐 tuple 再领取
额外的 prime 个数，也没有先假定全第四矩有界。

原 P=EE* 仍是 interval zero-extension finite carrier，不与 J frequency
projection 交换。结论分别比较 actual raw/good 与 physical raw/good。
它不删除三个内部 P，亦不比较 actual 与 physical 的值。
因此 31、distinct22、高全异与完整 fourth budget 仍开放；若后续在 J 上
调用 canonical 小量，须另列 [R]。本稳定性本身完全不需要 [R]。

## 5. 正式笔记 463 的最终 hash-bound 全文独审

全文核对
[463](../../notes/463-two-sided-height-stability-for-original-fourth-words.md)，
canonical LF SHA256
`6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90`，
3673 bytes / 94 lines。结论 **PASS**。

463 (2) 两个 trace-norm bound 与上述源稿完全一致，(3) 保留 d/L normalization，
(4) 取 source-band Kfar HS，(5) 只对<=3个 K 的短链使用。physical 切开后的
左反向伴随、同一 bad 中心双 guard 与两个 escape 的 HS–HS 已写明。
全 prime normalized 幂 X^-1 L^-5 复算正确，未把它当 actual/physical
crossing budget。引用 461 仅沿用模型，不继承其 conditional zero-free
作为本结论前件。最后限制仍明确保留开放 sectors，未宣布新比例或边界。
