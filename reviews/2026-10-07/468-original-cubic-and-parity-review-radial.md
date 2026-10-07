# 468 原 mixed cubic、截短31与 parity 必要界的联合独立审查

2026-10-08。radial_review。结论：完整限定 PASS。
已完整读取 root 的最终468、另外作者的两个背景源与两个 complex31 源；
本文核对其实际 finite objects、严格前件和全部恢复接口。
本文作者自己的 parity / unconditional capped31 来源只作已交另一作者
全文独审的输入，不将本报告冒称对自己来源的第二独立审查。
只新增本审查，不修改冻结 notes、来源、math、旧 checkpoint 或 Git。

## 1. 最终全文绑定及准确范围

canonical LF 为 CRLF/lone CR 转 LF，不 trim。

| 完整实读对象 | SHA-256 | UTF-8 bytes / 行 |
| --- | --- | --- |
| [468 最终稿](../../notes/468-original-mixed-cubic-and-parity-resolved-fourth-reduction.md) | ad4cf9f8bb4c77e24487b32434dc64d28162745adf3b1e0555b230be3953baf7 | 8694 / 205 |
| [背景 entire mixed cubic](hybrid-background-entire-mixed-cubic-research-compression.md) | 19c715587681c95c3e8750e4751a30bff798b372f68dc516f029c0a5e71020dd | 13926 / 289 |
| [actual cubic relative 恢复](hybrid-background-cubic-relative-actual-recovery-research-compression.md) | 1dbdad713d2694d9fce6391971fc0044fcbf18d0ad3dbdd2d3fba5111ba80d38 | 5564 / 127 |
| [nonalternating gate](hybrid-three-high-one-low-nonalternating-gate-research.md) | ce1e000572fc2eecb0fe99211c3120ac0b901fb42dd973064b8b041adc3174bd | 11593 / 279 |
| [stronger [R] capped31](hybrid-thin-high-short-low-entire-three-one-research.md) | c720b48c6e481d3c1b2f67ec36f8dd26b541e2f006eddd9022307fe9474a7128 | 11056 / 267 |

468另引用本作者冻结输入：

- [parity 必要约束](hybrid-parity-resolved-residual-necessary-constraints-radial.md)，
  SHA 6a5fb7db8467e80682d7351ee37a940af8d39de50fffe2f16b0b3a48d5dfc6f6，
  13209 bytes / 350行；
- [无条件 capped31](hybrid-thin-high-short-low-unconditional-three-one-research-radial.md)，
  SHA 74e47ca7b791656c25067793a2d9068c47675f3f60f0afc4d5c5d344fef5ea34，
  7831 bytes / 216行。

本次另逐接口核既有454、455、461–463、446及 weighted-high cubic 源。
所有涉及 [R] 的步骤仍以446明确的 conductor-one fixed-gap
zero-free / logarithmic-control为输入；本次不认证该分析内核、外部整稿、
新的 moving coefficients 或全导子合同。

## 2. mixed cubic：复权重、近核与全部 placements

原 \(D=E^*M_wE\) 对 complex w 通常不自伴。
最终源显式采用左右两方向 leakage，且二者确实相等：
\[
 \|QM_wE\|_2^2=\operatorname{Tr}E^*|w|^2E-\operatorname{Tr}D^*D,
 \quad
 \|QM_{\bar w}E\|_2^2=\operatorname{Tr}E^*|w|^2E-\operatorname{Tr}DD^*.
\]
有限 trace 给相同值，normal multiplication 的两侧没有被混用。
原 \(h_\ell=\phi^2/a_\ell-1\) 具备源要求的 bounded/C2/leakage前件。
任意 bounded w 只在 physical 证明中使用；
finite 结论并未向所有 arbitrary L-infinity coefficients 扩张。

三 prime 不可能净位移0，含重复标签亦然。
near 的平滑 gate、三个 shared shifted windows先共同 Fourier 分离，
再按 semiprime / prime 的整数 log-union 作 bilinear Hilbert。
LLL 的 product prefix为 \(2\sqrt X\)，HLL为low×low的原 \(X\)，
HHL为high×low的 \(2X\)；没有把 tuple inequality用作single q侧 moving mask。
三组 weighted energy给源列出的
\(\ell_0^3/(\sqrt X\ell),\ell_0^3/\ell^{3/2},\ell_0^3/\ell\) 小量。
prime与semiprime支持不交，Hilbert没有抹去真实zero diagonal。
O(1/d) remainder 的 HHL product质量使用真实 \(pr\le2X\) 截断。
这些论证覆盖八种signs、重复labels及每个placement的 complex绝对值。

## 3. HHL far / alias 和实际三个 P

不能用全 HHL 的 raw质量除 X。源先支付准确 endpoint alias：
同向 high、反向low的 physical support \(pq<Xr\)
给总质量 \(O(X/\ell^2)\)；
异向 high 的负alias强制其中一个 high
\(p\le e^{2A}\sqrt X\)，给 \(O(X/\ell^3)\)。
positive alias不可能。它们与原 overlap \(O(1/X)\) 相乘为o(1)，
没有把仅此 positive upper搬到signed middlefar。

middlefar 的 \(g_\ell(S)\) 在0及周期端点附近为零，
零延拓确为全局C2；其 Fourier-L1为 \(O(\log(2\ell))\)，
二阶tail为 \(O(1/T)\)。
它与全部 shifted windows共同分离。
unshifted w只留在原 u integral，不改变 prime prefix或原高度。
good Fourier tuple 的两原endpoint和所有固定线性组合在
absolute-height \([T/2,3T]\)，不是cycle difference。
bad tuple 用全高度 raw质量和真正 Fourier tail付款。
HHL主幂准确为
\[
 q_H^2q_L/X
 =X^{(5/2)a-9/4}\operatorname{polylog}X=o(1),
 \qquad \theta<a<9/10.
\]
LLL、HLL entire far 的 endpoint-overlap预算无需 [R]。

finite/physical比较保留三个内部P。
LLL、HLL采用raw two-crossing；HHL采用原good-band q和
\(\ell_R^g,\ell_R^{g,*}\ll\sqrt\ell\,q_R\)，
费用 \(O(\ell q_H^2q_L)\)。
complex weight左crossing用 \(QM_{\bar w}E\)，右用 \(QM_wE\)。
finite raw/good差以 bad compression 的 S1 \(O(m_R/T^2)\)处理；
physical差以原packet / first-far HS–HS处理，
\(m_H^2m_L/(T\sqrt d)=O(X^{-1/4}\ell^{-7/2})\)。
因此 (3)是actual原finite词的小量，没有提前使用 high4有界。

## 4. actual 背景与七个 proper-power cubic

完整relative源不是只重新陈述bounded-high4结论。
原二矩给 \(c_2=\operatorname{Tr}C_{\rm pr}^2/d=O(1)\)，
entirelow4与Minkowski给
\(\sqrt{f_{\rm pr}}\ll\sqrt{a_T}+1\)。
所以actual Gamma/pole误差的准确预算为
\[
 |\operatorname{Tr}R_TC_{\rm pr}^3|/d
 \le\|R_T\|_{\rm op}\sqrt{c_2}\sqrt{f_{\rm pr}},
\]
而无需粗 \(f_{\rm pr}^{3/4}\)。
static七个含low词小量与 high³ relative界在同一对象上合并。

非交换 \((C+P_{\rm pp})^3-C^3\) 的七个词均明确保留；
三个含一个P的词用 \(O(\sqrt f\,\epsilon)\)，
三个含两个P的词用 \(O(\sqrt{c_2}\epsilon^2)\)，
最后P³用 \(O(\epsilon^3)\)，其中
\(\epsilon=\|P_{\rm pp}\|_{4,d}=O(1/\ell)\)。
CPC、PCP通过有限cyclicity及S2/S4 Hölder分别付款，
没有将A、C、P交换或改变归一化d因子。
由此468(7a)的
\[
 |\operatorname{Tr}AC_\Lambda^3|/d
 \ll(\sqrt{a_T}+1)/\ell+o(1)
\]
正确，不先要求a有界。

\(a_T=o(\ell^2)\) 确实使该 cubic趋零。
454其余背景四次/一次/两次混合项只需已付bounded背景与原二矩，
所以此弱增长前件也足以得到468(7)的渐近等式。
它不使 \(C_\Lambda^4/d\) 获得常数上界；
468明确将中心四迹恒等式与比例转换所需的常数预算区分。

## 5. complex31 gate及 stronger [R] capped31

单向 \(B_R^\epsilon\) 的伴随为反向shift；截到原good J后，伴随乘子
是 \(\overline{D_R^\epsilon1_J}\)，支撑仍为J。
source的shifted-grid证明对任意complex multiplier absolute sup适用，
所以两个crossing均 \(\ll\sqrt\ell\,q_R\)。
非自伴六项 two-crossing通过左右 \(\ell_i^*,\ell_j\) 给出，
没有套selfadjoint的 \(\sqrt2\ell_i\) 等式。
raw/good物理两端各取bad guard，反向adjoint链与suffix链都只有至多3个K；
旧463的HS–HS \(T^{-2}\prod m_i\)完整覆盖complex方向、low/negative heights和pole峰。

三个high有相邻同向shift时physical product准确为0；
仅四个交替high signatures可能非零。
at-most-one-bulk分区的 \(s\le13/5\)，
取 \(a=22/25\)给 \(\eta\ge3/250\)，raw/good尾幂不超过 \(-17/10\)。
该较大分区仍需要同一 [R]，最终468已明写此限定。

thin-high / short-low 原 source 的全四符号 netgap
\(7/60<|S|/\ell<14/15\)和精确floor d csc核一致。
f_\ell netgate在每个tuple上等于原csc，不是新目标权重；
全部五个 Fourier coordinates同时分离才用prefix。
good主幂 \(-739/3000\)、bad尾 \(-121/120\)、
raw/good尾 \(-241/120\)及各日志因子均相符。
source明确先固定caps、profile与gap，再令T增长；没有不合法的row mask。

## 6. 468对本作者新结果的汇总核对

468(9)–(10)准确采用另经root/twisted独审的无条件简证：
原 caps的 \(m_t^3m_s\ll X^{119/120}/\ell^4\) 小于carrier尺寸幂，
netgap给 physical \(K_d=O(1/d)\)，原raw双方leakage给
finite误差 \(O(\log(2+\ell)m_t^3m_s)\)。
没有为了实际小量仍免费调用goodheight或 [R]。
另保留stronger [R]幂只作定量加强。
较大范围及其四交替signs未被(9)付清，段末 [R]范围现在明确。

468(12)准确保留 bounded-q 前件，
先fixed clip R后T、再R的顺序，以及PSD平方尾。
它未从H二范数parity推出Gamma二范数parity。
468(13)的low constants不要求bounded highq；
468(14)采用同一个共同子列 \(q,r,c\)，没有分离limsup制造更强关系。
467候选只作未付款前件，(15)的 \(11/75600\)与严格
\(|c-23/960|<1/100\)均按作者源的有理证书正确转述。
没有声称候选被排除、可实现或 \(k\ge1/40\)已付。
这属于对另一作者汇总稿的忠实性核验，不是自审自己两个证明来源。

## 7. 最终限定结论

468及本文绑定的另外作者四源完整限定PASS：
实际含low的背景cubic、relative actual恢复、明确31分区和原finite边界
均有完整对象及正确前件；最终summary没有将局部付款冒充whole fourth。
没有新的actual q上界、k下界、whole signed high4常数或新的比例。
外部 [R]、RH/RR、原完整prime/zero feature链不在本次独立认证范围。
