# 原 actual31 非交替符号 gate：root 独立全文审查

2026-10-07。限定 PASS：截短范围内的非交替实际有限词为 o(d)；
交替词、至少两大标签与完整31仍开放。没有新比例或无零边界。

审查对象：
[完整研究稿](hybrid-three-high-one-low-nonalternating-gate-research.md)，
canonical UTF-8 LF SHA256
ce1e000572fc2eecb0fe99211c3120ac0b901fb42dd973064b8b041adc3174bd，
11593 bytes、279 lines。完整逐节读取，未修改作者稿。

## 1. 规范前缀与非自伴算子

单方向乘子恰为原 sharp-prime prefix 或固定有限个前缀之差，
其伴随是复共轭乘子；good band 仍是 J，不迁移到 -J。
446 的原 principal 留数和 proper-power difference 均保留后才吸收进
q_i。原 L 归一化也保留。因此可使用两个独立的真实界
||QB_i^gP||_2 与 ||Q(B_i^g)*P||_2，均为 O(sqrt(L) q_i)。
原 Fourier 矩阵计算只用乘子 sup，无自伴前件。

## 2. 六项 crossing 与高度恢复

稿中 (7) 不是把自伴引理照搬到复数词。准确三项 telescoping 的
左 crossing 分别使用 ell_1*、y_1 ell_2*、y_1 y_2 ell_3*；
右链逐次插入 P+Q 得 (9)。HS–HS 配对恰有六项，且乘积中的
其他 norm 因子位置正确。

good 词的比较费为 L product(q_i)，除以 d 得
X^((a-1/2)s-1) L^4。原 P 不与连续 band 交换，也未消失。

raw/good finite 单因子差的 S1 norm为 m_i/T²，因为两端 packet
均在 bad band。physical 替换词在 D_i^b 处切开，两侧都有 bad guard；
左链取反向伴随，complex conjugation不影响支持和绝对 norm。
463 的首个大频率跳跃 HS 付款因此仍适用，给
T^-2 product(m_i)。归一化幂为 s/2-3；全部允许的 caps 有 s≤7/2，
故此尾费用无条件为小量。

## 3. 物理零与原有限词

两个相邻 high 同方向的步长和严格大于 L，原零延拓物理积确实为零。
三个连续 high 的八种方向中六种至少有一对相邻同号；乘 low 的
两种方向，得到十二种完整 signatures。另四种 high 交替词可真实存在。

物理零先通过已付 raw/good，再通过已付两crossing，最终回到实际
finite word。因此结论涵盖内部 P、carrier 和原高度；
不能仅凭物理零将不满足 gate 的全范围实际词也宣布为零。
所有 range sums 保持 factorized prefixes，重复与不同 prime labels
都在其中。没有把 distinct-only 删除后的 mask 调用为规范前缀。

原有限迹的四个 low placements可准确循环成 low 在末位。
作者只对这些有限矩阵使用循环，没有循环 E*physical word E 的端点 P。

## 4. 精确 caps 和研究限制

原 θ=7/8 可先固定 a=22/25。三 high 中至多一个超过 X^(11/20)，
另两不超过 X^(11/20)，low 不超过 X^(1/2)，所以
s≤13/5、(a-1/2)s≤247/250，
eta≥3/250，尾幂≤-17/10。只有固定四个 range words，
因此可直接相加它们的十二个非交替 signatures 得 o(d)。
这些有理数关系可以逐项精确验证。

全文明确留下同范围的四个交替 signatures、至少两大 high 标签、
whole31、whole22 和 high fourth。此结果没有支付467实际 q/k 前件，
也不能独立传到新的零点比例或新无零界。限定结论通过。

## 5. 全符号更小子范围补充

另完整读取作者
[thin-high / short-low 全符号稿](hybrid-thin-high-short-low-entire-three-one-research.md)，
最终 canonical UTF-8 LF SHA256
c720b48c6e481d3c1b2f67ec36f8dd26b541e2f006eddd9022307fe9474a7128，
11056 bytes、267 lines。限定 PASS：该明确子范围整个实际31为 o(d)。
最终两稿显示式格式更正和输入 SHA 同步已复核，不改变数学证明。

三个 high 均在 (X^(1/2),X^(11/20)]，low≤X^(1/3)。十二个非交替
物理词为空；四个交替词的两种 low 方向逐项给
7/60<|S|/L<14/15。因此固定 κ=1 的 netgate在每一个原tuple上
均准确为1，Fourier展开前后未删标签，也没有额外近核或端点余额。

f_L(S)=f(S/L) 的 Fourier L1 norm与L无关，二阶尾为 O(1/(LT))。
与三个中间 φ²、一项终点 φ 的四个 Fourier coordinates 一起分离后，
每个 prime 仍是原固定 sharp prefix。实际两个 floor endpoints
都在 [T,2T] 附近；五个小 shifts 后所有原高度仍在 [T/2,3T]
或其负区。大 shifts 的 union则完全用原 C² 尾及正质量，
包括 principal 高峰，未套高height小量。

根用有理数独立核出 s=119/60、eta=739/3000、
ghost exponent=-121/120、双高度恢复 exponent=-241/120。
physical main为 X^-eta L³(log(2+L))⁴，实际两cross多一L，
合并后为作者 (19) 的 X^-eta L⁴ 加两个严格小尾。
对十六个 signatures相加及四个实际 low placements循环均合法。

它只支付这两个固定 capped ranges；原更大 low/high 标签仍保留。
没有完整 fourth常数、实际 q/k估计或新零点比例。补充限定结论通过。

## 6. 同一capped31的无条件原载波简证

另完整读取 radial 的
[raw absolute capped31](hybrid-thin-high-short-low-unconditional-three-one-research-radial.md)，
canonical LF SHA256
74e47ca7b791656c25067793a2d9068c47675f3f60f0afc4d5c5d344fef5ea34，
7831 bytes、216 lines。限定 PASS：同一个整个capped31无需[R]也为o(d)。

作者直接重证原单方向 shift的outside carrier核，g_s=φ(u)φ(u+s)
及其两阶derivative统一有界，两次IBP无边界项。
原Ee_k在shift后额外的indicator已包含于φ(u+s)，因此该矩阵公式
并未使用周期wrap替代真实零延拓。输出仍支撑I；
outside差n的pairs数量确为min(d,|n|)。两方向raw泄漏均为
O(m_R sqrt(log(2+ell)))。

非自伴六项two-crossing原式再次自证，给
log(2+ell)m_t³m_s/d的小误差。原十二个physical空词保留，
剩四个fixed netgap使csc绝对值有固定upper，所以直接
|K_d|≤C/d。positive总系数质量为
m_t³m_s≪X^(119/120)/ell⁴，严格给
X^(-1/120)ell^-5 log(2+ell)=o(1)。

全部在raw原对象计算，不需height替换、canonical消去或未知四矩。
它降低同一观测量小量结论的前件；先前[R]稿的更强幂界仍成立。
更大high/low范围和完整fourth仍未支付。
