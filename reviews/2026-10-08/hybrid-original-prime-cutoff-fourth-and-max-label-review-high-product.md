# 原素数截断四矩与完整最大标签族：不同作者审查

2026-10-08，审查者 high_product_joint。限定数学 **PASS**。
只新增本 peer；作者源、冻结输入、Git、index及cadence未动。
判定以 ordinary \([R_{7/8}]\) 为前件，不认证该前件本身。

## 1. 最终身份与实际全文读取

作者源 [prime cutoff / max label](hybrid-original-prime-cutoff-fourth-and-max-label-research-perron.md)
已逐行 FULL READ 最终175行；11733 canonical LF bytes；
SHA256 d7aaee914be30cfee19b4aa62b3efcb36adaa0f058155cc05d2e82e1c8740062。
前稿 f320…的 trace 平方已明确为算子乘积平方的迹；本审查只绑定以上终稿。
canonical 化仅 CRLF/lone CR→LF，不 trim、不改末尾换行。

以下输入全文读取，及其实际使用的证明已独立核对；身份只读重核匹配：

| 输入 | 行数 / LF bytes | canonical LF SHA256 |
|---|---|---|
| [scalar 两乘子](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | 370 / 14699 | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [固定 Perron](hybrid-original-squarefree-signed-zero-gram-research-perron.md) | 453 / 18782 | 0b126138c7bf42e9be3c4352b099a6ab37d88cef93af20593593c8e849aa2a17 |
| [密度迁移](hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md) | 184 / 9802 | a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d |
| [whole 桥](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md) | 276 / 11396 | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 |
| [真实重复图](../../notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md) | 270 / 8936 | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 |
| [double-nn](hybrid-whole-fourth-double-nonunit-actual-research-whole.md) | 545 / 17557 | 2d27661262a1e672a9bb93846de68a661e0d17d8f5e0444117ae6a8debac4215 |
| [unit/mainband](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425 / 16428 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [有限高素数重复证明](../2026-10-07/hybrid-high-prime-four-word-response-research.md) | 572 / 19170 | 988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666 |
| [重复指标 P 删除证明](../2026-10-07/hybrid-low-high-mixed-four-word-research.md) | 589 / 22126 | 71f62b2dd931cfda012e7dad9c4efcfece63f5cf1bb8ff5b466d3e2ac1ae89f9 |

## 2. scalar 与 fixed-zero 前件

原 \(X=T/(2\pi)\)、\(Y=\sqrt X\)、\(N_L=a_LL\)、\(J=[T/4,4T]\) 不变。
\(Z=X^u\)、\(17/20\le u\le1\) 只截真实素数列上端。
两半整数端点准确保留整数集合；\((z^w-y^w)/w\) entire，
包括 \(w=0\) 的值和真实留数。共同绝对高度 \(-h_0,-h_1\) 固定，
没有逐行零点删区，也未跨 pole1/trivial zeros。
近端误差直接有限 harmonic 支付；无限尾用
\(\sum\Lambda(n)n^{-1-1/L}\ll L\)，未在无穷尾引入 \(n^\varepsilon\)。
横线 \(O(\sqrt ZL^2/T)\)、左线 \(O(Y^{-3/2}L^2)\) 与原453证明相容。

whole entire 核正包络给费用 \(4u(\sigma-1/2)-1+n(\sigma)\)；
低实部整包 polylog。独立求导/端点比较确认
\[
 \max\{0,u-2/5,6u/5-4/7,3u/2-11/14\}=B(u)=3u/2-11/14.
\]
限定区间保证顶端项占优；固定网格先于 \(T\to\infty\)。
这里只消费已绑定184的普通 ζ 密度，不扩大为其他角色或家族。
proper powers 对新截断列直接重估：平方按 base \(pq\) 计唯一分解，
更高 powers 取绝对值；\(L^4\) 范数差 \(O(X^{-1/12})\) 由 Minkowski 消费，
未把增长第四矩之间的差写成 additive \(o(1)\)。

## 3. complete physical/finite 前缀及重复量

两乘子与终端空间保持原样，仍共享同一空间变量及真实 C² profile。
原 χ overlap 与 ν支撑 guards 足以恢复 scalar 界；\(m_Z\ll\sqrt Z/L\)
使全部 tails/cross terms 落在 \(X^{B(u)+\varepsilon}\) 内。
反线性对称给 physical fourth \(=2\|G_ZE\|_{\rm HS}^2\)；
finite compression fourth 的上界由每个特征向量的谱测度 Jensen 得到。
没有在 physical 带末端 \(P\) 的词中免费循环，也未逐 tuple 删除内部 \(P\)。
whole 桥对新列重估 leakage \(O(L+Z/s_T)=O(L)\)，
two-cross \(m_Z^2L/d=O(X^{u-1}/L^2)=o(1)\)；不是旧 signed error 的单调截取。

有限重复族独立核算如下。\(S_2=\sum b_p^2=O(1)\)、\(\sum C_p^2\le S_2I\)，
原系数二阶平均 \(\int\chi\,\tau C_Z^2=O(1)\) 由直接 weighted MV 支付。
对 selfadjoint \(A,B\)，\(|\operatorname{Tr}((AB)^2)|\le\operatorname{Tr}(A^2B^2)\)。
故 \(T_0,T_{\rm opp}\) 由 \(S_2\tau C_Z^2\) 付；
\(T_{22},T_\times\) 由 \(S_2^2\) 付；
\(|T_3|/d\le(\sum b_p^3)\sqrt{\tau C_Z^2}\)，
\(T_4/d\le\sum b_p^4\)。χ-Cauchy及原 inclusion-exclusion 给 averaged absolute \(O(1)\)。
尤其 \(T_3\) 不需要未知第四矩常数前件。
physical repeated 的非闭合 carrier、near harmonic、\(p^2/(qr)\) endpoint、
grid aliases 按456正 majorants 直接限制标签；闭合平方权重 \(O(1)\)。
上述 P 删除证明亦只聚合可平方求和的 repeated label，不用于 all-distinct 任意子掩码。
因此正 whole fourth 减实际 repeated 支付 complete signed
\(\mathcal D_Z^{\rm act/phy}\)；原 far 正四权质量 \(O(Z^2/L^4)\) 合法恢复 hard-near。

## 4. nn、chirp 与可消费的范围

half-ratio 是 physical 四全异完整平均的一半；545 exact partition 逐整体使用。
非零 nn 重新聚合 \(\sum_{q\le Z}b_q q^{-1/2}\sum_{s<q}b_s\ll\sqrt Z/L^2\)，
故费用 \(X^{u/2+\varepsilon}\)。零频的正计数、内区高阶 Euler–Maclaurin、
graph及迁移保持原 guards；未假定任意 nn signed 子块也小。
425 chirp 的直接正聚合给 \(X^{u-1/2}L^C\)，原 finite Taylor、
sharp 边界、整数 aliases及全部最大位置、\(p,r,s<q\)、原 s 排除均保留。
\(B(u)-u/2=u-11/14>0\)、\(B(u)-(u-1/2)=u/2-2/7>0\)，
故完整 unit 前缀及完整 signed mainband 同为 \(O(X^{B(u)+\varepsilon})\)。

结论只覆盖 **完整 \(q_{\max}\le X^u\) 前缀**，并非 centered 正能量或点态块界。
\(u=.9\) 的完整族允许 \(qs\le X^{1.8}\)，但不能由其总 signed 界截取
cap 外切片、minor/major 掩码、单 \(q\) 或491的私有端周期子族。
\(u=1\) 仍为 \(5/7\)；top-\(q\)、global whole、sf核心、中心常数与计数桥尚未改善。
没有新比例、无零边界或可发布的全局纪录；没有以有限采样代替解析证明。
