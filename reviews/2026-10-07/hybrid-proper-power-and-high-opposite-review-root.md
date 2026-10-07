# 455–456 根节点全文核验与结论范围

2026-10-07。从 main `5b7effad9126499583a2243e462e16e28b346265` 继续。
根节点全文读取两篇新笔记、原 high/mixed 报告、独立 Topp 推导及 proper-power
独审；重新运行两份标准库精确脚本。下列 PASS 只覆盖明列接口，不提供完整
四阶矩、新比例或新的无零边界。

## 1. 最终正文及有限证据绑定

canonical LF：仅将 CRLF/lone CR 转为 LF，不删空白或 EOF。

| 对象 | SHA256 |
|---|---|
| [455](../../notes/455-whole-proper-power-fourth-norm-and-prime-equivalence.md) | 6bf2025dcc8f56d7b35d9c8b764ac2ff3b911a6e054bf9c496042c7f3e11ce41 |
| [456](../../notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md) | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 |
| [455输出](../../output/hybrid-proper-power-exact-audit.json) | af7bc4c541f591fee0eb7b5d56c1315cccd8caddfc544ed418ad846104ce399b |
| [456输出](../../output/hybrid-high-opposite-exact-audit.json) | 3bef191084595e821d3e6f892405d9a6dab6471b8bdfe02d858e5ea18e07e466 |

完整独审分别见 455 的
[radial](hybrid-whole-proper-power-review-radial.md)、
[twisted](hybrid-whole-proper-power-review-twisted.md)，以及 456 的
[radial](hybrid-high-opposite-prime-review-radial.md)、
[twisted](hybrid-high-opposite-prime-review-twisted.md)。
另有[独立 Topp 推导](hybrid-high-opposite-prime-research-twisted.md)。
独审结论与有限程序输出分开验收。

## 2. 455：原全部 proper powers 在 S4 中小

S2平方必须按 base m=pq≤X 分组，其频率是2logm。唯一分解给两项准确
coefficient identities，weighted local spacing 的倒数≤m，故任意时间
interval J 上四矩≪|J|+L⁴。这一步没有把任意长为X²的整数列擅自缩短。
三次以上 powers 的绝对余量全高度一致有界。

在同一个原 carrier frame 用 scalar spectral Jensen：F 是 contraction，
对差矩阵的 eigenvector 的 scalar measure 补足在0的质量，再求 finite
eigenbasis。unitary Fourier 的 prefactor16及 Parseval grid 常数
a_L L²/(2pi)一致。central J=[T/2,3T] 的费用为 O(d/L⁴)。J外使用真正
大距离的 C² Fourier tail、全高度 O(L) multiplier，其费用 O(d/(LT³))。
这包含低/负高度，且从未删除四词中的 internal P。

由 Schatten reverse triangle，normalized fourth roots 相差 O(1/L)，
无需预设任何 whole budget。故 boundedness 与 extended limsup 等价；
相同 Hermitian background 可保持在两边。转回 fourth total 的 o(1)
则确实需要 finite whole-budget 前件，正文保留了该条件。

接受：全部 proper-power S4-small 及同矩阵 prime-only 归约。
不接受为已证：full genuine-prime fourth、每个 proper-power mixed word
分别 o(N)、新零点比例。

## 3. 456：actual opposite repeated 四词为 o(N)

原 [high报告](hybrid-high-prime-four-word-response-research.md) 与
[mixed §5](hybrid-low-high-mixed-four-word-research.md) 提供实际有限二矩与
重复标签 P 删除引理；核对 root 与独立推导的三项 HS 配对，费用都由
sum b_p²、sum b_p l_p 及已有 Y2=O(sqrt d)控制，不需要未知 CH4有界。
合计 normalized projection error 为
O(sqrt(log(2+L))/L^(3/2)+log(2+L)/L³)。

真实高步长均大于 L/2，16种符号仅两种 alternating 有支撑。五个位置
还强制 |net shift|<L/2，故 finite geometric kernel 的 endpoint aliases
被物理支撑排除。carrier 单位相位保留；真实共同 overlap 至多
log(X/p)/L，后续 dummy q/r排序没有免费重排 operator。

near 的正 majorant 是 log(X/p)/(XL|p²−qr|)。较小的 q/r必须继续为
prime，才能用每个非零平方剩余至多两根；p及另一个指标只在这一步
合法扩大至整数。ell|p 的零剩余分支单独剔除唯一 zero denominator，
其余 progression retained，包含原 p=ell而第三指标不同的情况。
root普通 dyadic bins只有 Q≥c sqrtX，但 logQ≥L/2−O(1)，Chebyshev
费用 O(Q/L)仍成立；无需 Q≥sqrtX 的较强字面约束。

对固定P，可用Q的数量 O(1+log(X/P))；真实 endpoint overlap 和P/X的
几何衰减给总 near O(1/L)。far ratio 和 exact all-equal diagonal均
另已支付。最后 actual Topp/N=O(1/L)，合原 exact partition 得真正
signed repeated union→2Sψ，flat=19/240。不是把一侧预算认作等式。

接受：原 finite compression 的该交错项与重复部分的实际极限。
不接受为已证：all-distinct high/mixed、full centered fourth、AC³
covariance 或新比例。455/456 的核心连续估计均不调用零自由 [R]；
后续使用452转移到比例时仍须保留其 [R] 和 zero-side 合同。

## 4. 有限核验范围与改动记录

455脚本实跑10个 weighted prime-product模型、48 scalar algebra核验。
456脚本独立枚举1至6标签的真实 cyclic重复 words，验证整个 inclusion–
exclusion；1134个非零剩余核验、225个零剩余 progression及19/480的
有理积分全部通过。它们不认证无限素数估计、MV、Jensen、支撑或 P 删除。

455只修未定义 C_pp别名为 E_pp与状态；456只修一个 substack换行符、
状态并加有限证据范围。两文数学证明与本轮独审前版本一致。
旧论文/PDF、外部 math及已冻结来源正文保持原版；没有新 kernel认证。
