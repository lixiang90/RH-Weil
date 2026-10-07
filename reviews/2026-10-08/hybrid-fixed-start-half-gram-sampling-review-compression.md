# 原 fixed-start half-Gram sampling 独立全文审查

2026-10-08。compression_bridge；对 root 作者的新源独立审查。
只新增本审查，不改来源、冻结文件、math、Git 或 Goal。

结论：**限定 PASS**。完整读取199行新源，并重新读取其三个直接
依赖。实际每列的半宽频带、原 shifted eta-grid 的精确 Parseval、
positive-height guard 与 raw-growth 下的 exterior tail 均成立。
本审查不认证新的 scalar 算术 upper、比例、边界或原 AF 分析前件。

## 1. 实际字节绑定

canonical 仅将 CRLF/lone CR 统一为 LF，不 trim 或改变 EOF。
已从磁盘逐一复算：

| 实读来源 | canonical LF SHA256 |
|---|---|
| [待审 fixed-start 源](hybrid-fixed-start-half-gram-sampling-research-root.md) | 7ed68a71d4d22d0bf1d90c61cef231534737188131aad9842669cd11f19c82cc |
| [474 完整 scalar 乘子源](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [原 half-ratio 与 uniform cross](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md) | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 |
| [472 原载体与全 P 桥](../../notes/472-original-short-carrier-fourth-compression-and-ratio-variance.md) | 9856885e932a892cf7c33ece82f430c2ec13004555eb52da2f1e8b1ec6bb2683 |

主源7522 canonical bytes、199行。本审查以这一版本为对象。

## 2. 原物理 support 确实给半宽频带

逐项核对 z_u 的实际三段路径。若 phi(u-log p) 非零，
则 u-log p>=-ell/2。因为 log p>ell/2，必有 u>0。
对 v=u+log(q/p)=(u-log p)+log q，同理 v>0；
最终 phi(v) 又要求 v<=ell/2。外侧 phi(u) 只需 u∈I_+。
因此实际 ratio 频率满足

\[
 -u\le\log(q/p)\le\ell/2-u .
\]

该区间宽 ell/2，中心 ell/4-u。按源选取固定 bump 后，
multiplier 的 support 宽小于3ell/4，且在全部真实 ratio 上等于一。
这在实线逐有限频率成立，未要求两个不同 ratios 按 ell 取模相同。
其 kernel modulation 只改变相位，Schwartz decay 常数对 u 统一。
原 0<=phi<=1、uniform variation 与 a_ell>=c_phi 均由已绑定的
scalar 源明确提供，没有新增 profile 或端点 positivity 前件。

## 3. shifted-grid Parseval 的常数及适用对象

采用源的 Fourier convention，若 support 放在长度 ell 的 cell，
令 H(xi)=hat h(xi) exp(i sigma xi)，并写
a_k=ell^(-1)int_cell H(xi) exp(i k eta xi)dxi，则
h(sigma+k eta)=ell a_k/(2pi)。Fourier-series 与实线 Parseval 给

\[
 \sum_{k\in\mathbb Z}|h(\sigma+k\eta)|^2
 =\frac{\ell}{4\pi^2}\int|\widehat h|^2
 =\frac{\ell}{2\pi}\|h\|_2^2
 =\eta^{-1}\|h\|_2^2 .
\]

compact support 与 L2 同时保证 hat h∈L1，samples 为连续代表。
该恒等式对每个 sigma 成立，不需要 carrier 平均。
实际 h_u=T_(m_u)(z_u 1_Jz) 是真正 L2 函数；contraction 合法。
完整 z_u 只用于有界 finite-polynomial 的 L1 kernel 卷积，
没有对其错误使用全实线 L2 Parseval。
有限 k 集是全整数网格的子集，故源(4)费用准确为1/(d eta)。

## 4. guard 与 growth-uniform exterior 费用

所有 sigma∈[T,T+s] 的原 samples 位于[T,2T+s]。
s<T/4时至 J_z=[3T/4,5T/2] 外至少 T/4；
J_z至 J1、J1至 J2 外也有固定倍 T 的间隔。
原 C2 两乘子因此给同一 E_T(M_T)，不经过 height 0 峰。
直接积分 bump kernel 的 tail 得

\[
 |\text{exterior sample}|
 \le C_N m_T^2(\ell T)^{1-N}.
\]

有限样本 Minkowski 后按 phi(u)^2/ell 积分，
偶窗的 half mass 正好 a_ell/2，恢复源(7)的 exact floor prefactor。
N=3时 raw M_T<=C m_T^4 与 N_ell=O(1) 给 E_T<=C m_T^2。
新增 cross 与平方误差不超过 C m_T^4/(ell T)^2；
由 m_T<=C sqrt X/ell、T=2pi X，确为 O(ell^-6)。
这里仅消掉 sampling 新 tail，未消掉 E_T 内两次 C2 guard 的
显示费用。特别没有以 unknown fourth bounded 来证明此小量。

## 5. 原 same-prime 中心与 fixed-start upper

冻结 uniform cross 给
||G E_sigma||HS^2/d=r_sigma+S_T/2+O(ell^-1)；
其误差对 base phase 统一，不乘 r_sigma。
因此主源(8)的 ratio 一侧 upper 对整个原 sigma 窗口成立，
其中 T/(d eta)=X ell/floor(X ell) 保持准确。
未知增长时不能把这一 prefactor 的 relative o(1)
或 E_T 内部 cross 免费改成 additive o(1)。

若另外支付 M_T=O(X^(B+epsilon))，0<=B<1，
原 E_T 的全部项足以给同样的 growth upper。
physical B_H^4 的 half-Gram identity 与 scalar Jensen 随后给
同一固定 sigma 的 finite high fourth upper；这一单侧步骤
不需要证明 fixed sigma 的 whole fourth P-gap=o(1)。
whole low fourth 与 Schatten triangle 也只传递增长上界，
不能推出 quartic 差为 additive o(1) 或新的固定常数。
源最后 Jensen 式中的物理 H 按其前后定义读取为 B_H。

AF 末转移仍是条件步骤。本审查把正文“trace-norm o(1)”读取为
真正未归一化 Schatten S1 误差 o(1)（或其他已明确足以使 normalized
S4 有界的小量合同）；此时 normalized S4<=d^(-1/4)||error||S1，
triangle 合法。仅有 normalized S1=o(1) 一般不够：
转换至 normalized S4 可能产生 d^(3/4)。
本审查不为未陈述的较弱 tail 合同支付该转换。

## 6. 完成范围

有限数学新付款是实际窄频带、精确 shifted-grid sampling 及原
positive-height guards，使一侧 scalar upper 可传到固定原起点。
canonical scalar fourth 的新算术估计仍是外部输入；没有从采样
推得 prime cancellation、O(1)、实际新比例、无零边界或 RH。
本结论与主源上述有限证明和条件 scope 绑定，不依赖运行 PASS
代替分析证明；没有新增测试脚本或修改任何冻结材料。
