# Ivić 密度迁移：root 独立全文审查

2026-10-08。基线 5fe68395d20e9738ecc0ba64e8a762f4d93bd073。
结论：限定 PASS。新结果是原对象的增长幂加强，未得到常数预算。
canonical UTF-8 LF 只统一 CRLF/lone CR，不 trim 或改变 EOF。

| 全文实读冻结源 | canonical LF SHA256 |
|---|---|
| [Ivić 迁移作者源](hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md) | a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d |
| [原正高度完整零点包](hybrid-positive-height-zero-packet-fourth-upper-research-radial.md) | 8bcbd27da46d922d9e6e741fcf9a87012d565052f8d97b3ad12e99b3edbc2481 |
| [原 fixed-start 采样](hybrid-fixed-start-half-gram-sampling-research-root.md) | 7ed68a71d4d22d0bf1d90c61cef231534737188131aad9842669cd11f19c82cc |

主源最终 9802 bytes / 184 行，逐行读取；未修改作者源或旧证书。
后两源已在 475 束完整证明并由不同作者审查，本次核同一迁移对象。

## 1. 原作者定理与准确范围

root 独立浏览 Ivić 本人综述 *The distribution of zeros of the zeta-function*
§3 的计数定义与公式，并另用 urllib + PyMuPDF 只在内存读取作者原书
*Topics in Recent Zeta-Function Theory*，印刷第 183 页 / PDF 第 188 页。
Theorem 9.3、(9.63) 给 A(σ)≤3/(2σ)，下端 3831/4791。
前文 k=2 的导出说明与 theorem 页同时读取。原 PDF 278 页、
10538942 bytes，SHA fafac152db87abe132858fa97d8fe501c61cd261e20732ef701396fba27b61aa。
本次没有将外部 PDF 保存为仓库附件。

这给普通 ζ 的 N(σ,V)≪V^[3(1−σ)/(2σ)+epsilon]，不是 LH/RH 前件，
也不是 Hecke 家族结论。作者综述的 N 明确计 β≥σ、|γ|≤V。
主源采用严格下端，实际所有新增网格点≥4/5，且
4/5−3831/4791>0，故端点表述差异无影响。
按普通重数计数读取；即便先从 separated 代表计数出发，unit strip
O(log V) 亦可补重数，固定 epsilon 形式保持同幂。

这里以作者已证明的密度定理作外部数学输入，没有宣称本项目重新
认证其全部指数对证明或零点检测。与引用经典 Ingham/Huxley 范围相同。

## 2. 全实部网格的严格包络

不能只将 θ=7/8 的密度换成 3/14 而跳过其余零点。
主源在 [1/2,4/5] 沿用 475 的两个经典密度，函数
4σ−3+n0(σ) 各段递增、在 3/4 连续，整个低区最大值为 22/35。
在 [4/5,θ] 新函数为

\[
 f_I(\sigma)=4\sigma-3+\frac{3(1-\sigma)}{2\sigma},
 \quad f'_I=4-\frac{3}{2\sigma^2}\ge\frac{53}{32}>0.
\]

核准 f_I(5/6)=19/30、19/30−22/35=1/210>0。
所以对整个原范围 5/6<θ≤7/8，所有实部层的最大指数准确为 f_I(θ)。
在 4/5 两个可用上界的拼接不连续无妨；低层 supremum 已单独比较。
固定 epsilon 后先固定有限网格，再令 T 增大，不要求 moving σ 常数。
边界 bin 和日志各花任意小的固定指数损失；β≤1/2 的总数仅为 polylog。

准确得到
M_T≪T^[B_I(θ)+epsilon]，B_I=4θ−3+3(1−θ)/(2θ)。
根节点另算 B_I(7/8)=5/7，19/26−5/7=3/182，3/4−5/7=1/28。
一般两次节省分别为

\[
 B_H-B_I=\frac{3(1-\theta)^2}{2\theta(3\theta-1)}>0,
 \qquad
 (2\theta-1)-B_I=\frac{(1-\theta)(4\theta-3)}{2\theta}>0.
\]

这些连续代数核验不代替外部密度或 Perron 分析。

## 3. 原 cutoff、增长误差与固定起点

沿用 475 同一 combined Perron、全部 |γ|≤16T、真实 z=0 zero residue
及 ell³/T 的 full-tail Jensen 式；只换加权计数的 exponent。
same normalizer、两 sharp cutoff、正高度 [T/4,4T] 均保留。
proper powers 仍用 L4 norm 差和 Minkowski 返回 genuine primes，
没有在增长中声称四矩相差 additive o(1)。

fixed-start 的 E_T 三项与 exact floor 保留；代入 0<B_I<1 后，
所有六个平方/cross 指数都由主幂控制。所得是每个原合法固定起点的
一侧 high/whole-prime fourth 增长上界，不需 whole-P gap 在该起点 o(1)。
若再转同配置 centered zero matrix，仍须 475 明示的 AF 背景与真正
未归一化 S1 tail 合同；此末步仍相对原 AF [R]。

作者的 Theorem 50 辅助比较仅在 6/7..7/8 检查，其 Definition 37
左移计数量词经单调性支持固定 σ，未作为主结果必要前件。
Guth–Maynard 的 15/59 与 CDV Theorem 1.2 的下端 279/314>7/8
亦核对原文；均未偷用于本次顶层加强。

## 4. 范围

限定 PASS：主源在原 5/6<θ≤7/8 上得到真实 scalar 与 fixed-carrier
增长上界加强，在 7/8 为 5/7，在原 θ* 数值约 0.714198002953028。
这不是新的零点密度定理，也不声称该四矩 exponent 的文献首次性。
B_I>0，原 signed near、可用常数预算、实际新比例或无零边界仍未付。
