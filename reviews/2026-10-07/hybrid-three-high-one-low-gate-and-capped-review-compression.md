# 原31 complex sign gate 与 entire capped sector 的独立全文审查

2026-10-08。审查者 compression_bridge，来源作者 twisted_research。
已逐行完整读取以下两源；本审查独立于作者及 root 的审查。
只新增本审查文件，冻结源、旧审查、math、Goal、Git 未改。

| 完整来源 | canonical UTF-8 LF SHA-256 | bytes / lines |
|---|---|---|
| [complex nonalternating gate](hybrid-three-high-one-low-nonalternating-gate-research.md) | ce1e000572fc2eecb0fe99211c3120ac0b901fb42dd973064b8b041adc3174bd | 11593 / 279 |
| [thin-high / short-low entire31](hybrid-thin-high-short-low-entire-three-one-research.md) | c720b48c6e481d3c1b2f67ec36f8dd26b541e2f006eddd9022307fe9474a7128 | 11056 / 267 |

canonical 定义为 CRLF 与 lone CR 转 LF，不 trim。亦复核了两源共同绑定的
446、463、finite-band 来源：08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf、
6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90、
bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f。

结论：**限定 PASS**。两源证明各自所列原 actual finite 子块为 o(d)，
不需要未知全高第四矩有界；没有阻断问题。这不是完整31、22、whole第四矩
或467实际 q/k合同的通过。新源的这些保留范围正确且必要。

## 1. 原对象、complex directions 与双方 crossing

原 E 是区间 I 上有限正交 carrier 后零延拓，P=EE* 未换成实线连续频带。
单向 B_R^ε 的乘子为 −Σ_(p∈R)b_p p^(iεt)，准确对应真实平移。
其伴随乘子是共轭值；good multiplier 仍支撑 J，不因伴随变成 −J。
每个准入 range 是固定有限个 sharp intervals 之并，因此446前缀相减
确实适用。没有 arbitrary mask 或逐标签 moving coefficients。

finite-band source 的 outside-j matrix formula与 shifted-grid Minkowski
只使用乘子绝对上界。因此 ell_i、ell_i* 均 O(sqrt L q_i)，不需要
B_i 自伴；原 I 外输出为零，未漏算实线 Q 部分。

gate (7) 的非自伴四词引理重新推导如下。三个 P 依次插入，差是
PV1QV2V3V4P、PV1PV2QV3V4P、PV1PV2PV3QV4P 的迹之和。
递归 QV2V3V4P 的 HS bound，先分 V2 后的 P+Q，得
ell2 y3 y4+y2 ell3 y4+y2 y3 ell4；其余两项同理。
左边 PV_iQ 的 HS 是 ell_i*，故所得六项正是
Σ_(i<j)ell_i*ell_j ∏_(k≠i,j)y_k。未偷用自伴 commutator 恒等式。

于是归一化 good crossing 为 L∏q_i/d。q_i 原归一化统一用 L，
cap指数总和 s，原[R] fixed a 给 X^((a−1/2)s−1)L^4。
这完整付清三个 middle P，且明确只在 (a−1/2)s<1 时趋零。

## 2. complex raw/good 恢复与物理空词

finite bad factor A*D_i^bA 的 trace norm≤m_i||A||HS²，允许 complex D。
physical bad center 左 prefix须取反向伴随；共轭不会改变 bounded op、
J^c guard或 near-jump 支持。463双侧 escape各给 m-chain/T，故
四词 physical与finite raw/good差均 O(∏m_i/T²)。这不使用未知 S4界，
也不在 τ≈0 principal峰套 good-height消去。归一化指数 s/2−3，日志L^-5。

任意相邻同号high步骤有 log p+log q>L，三个相应位置无法同时位于 I。
故该 physical二factor product准确为零。三个high中非交替有6种方向，
再乘low的2种方向共12个空词；四个交替词留开，计数准确。
gate的四个low placements只在 actual finite trace内循环，随后按循环后
的high顺序构造physical比较，没有假物理投影迹循环。

例17–18重算：a−1/2=19/50，s≤13/5，η≥3/250，height费用指数≤−17/10。
四个固定range words、每词12方向与4个实际位置只是固定有限个项，
可作绝对三角合并，不产生 moving partition费用。

## 3. capped整个31的准确netgap与Fourier独立性

thin cap α=11/20，short low cap γ=1/3。交替high (+,−,+) 时：
low负给 7L/60<S<3L/5−log2；low正给 9L/20+log2<S<14L/15。
全部反号给反向 S。因此每个原tuple都满足 7/60<|S|/L<14/15。
这是原band支持推出的完整约束，重复标签也包含，未删除 near元组。

来源的固定 κ(S/L)=1 在此完整区间，故把 csc替换为 f_L是每个原tuple
的精确等式。没有在依赖product的hard gate后非法套独立canonical前缀。
f_L=f(S/L) 的 Fourier-L1 O1、tail O(1/(LA))由缩放或二阶导数直接得到。

φ(u+S)、三个 intermediate φ²与 f_L 同时展开，共五个coordinates。
各prime phase仅是该prime的 log与固定Fourier线性组合；保留 φ(u)不展开，
normalized u integral≤1。四个真实range sums因而确实独立分解。
原位置窗与netgate均保留，其L1费用 O(log(2+L)^4)，没有漏掉nonseparable
cutoff，亦没有把截断prime convolution替换为完整Λ*Λ。

五coordinates在 T/100 内时，原floor endpoint heights约 T、2T，
每个prime最多五个偏移，总偏移≤T/20，全部绝对height在 J。
负方向由原实系数共轭处理。446 sharp Perron的principal项与proper-power
差先保留后吸收；low的长度 X^(1/3)仍使用原height T，而非偷换height。

bad union至少一个coordinate>T/100，L1 tail O(ell0^4/T)；使用全height
raw masses，覆盖相互抵消、τ≈0和principal峰。只需原C² tail，未升级窗
为Schwartz。交替四词rawphysical为o(d)，另12空词准确零。

## 4. 费用、最终范围与数值重算

s=3·11/20+1/3=119/60，(a−1/2)s=2261/3000，故η=739/3000。
m_t³m_s指数为119/120；physical Fourier ghost除以dT后为−121/120；
463双侧height除以dT²后为−241/120。L费用分别为
main L³ell0^4、cross L^4、两尾 L^-5ell0^4 与 L^-5。
最终 ell0^4≤L 对充分大 L成立，来源(19)的总界正确。

故同一个原finite carrier确有 Tr(C_t³C_s)=o(d)，其余low位置由finite
cyclicity同值。所有标签重复与distinct同时在factorized ranges里保留；
没有把distinct-only版本免费改成canonical输入。

两源只付各自明确cap/sign sectors。bulk high、更长low、交替近共振及
完整31仍保留。顺序是先固定profile、θ、a、caps和有限range个数，再取T。
通过本审查不产生新的高第四矩常数、零点比例、无零区或RH结论。
