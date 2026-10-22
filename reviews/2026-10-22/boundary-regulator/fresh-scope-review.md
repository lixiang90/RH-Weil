# Boundary regulator 门的独立范围逆审

2026-10-22；独占审阅，不改公共状态、原稿或 Git。结论：**限定 PASS**。
已恢复 README、STATE、check/show、G20261014、C035、D20261022C及宏观前沿；
同0c4f冻结基线，长期完成门仍 open。本门没有准入新数学合同或增加cadence。

## 1. 审阅对象与方法

逐节读主稿及四份独占推导，核对405、407、411、414、430–432、437的必要定义和原证明范围，
特别重读432(8)及其有限轨道推导，防止仅扣407较弱对象而漏掉已有非零K类和HH₁电荷。
另打开CCM2007固定v1的Definition8.2、Proposition8.10、8.13与Stacks 0B5B核来源范围。
Weibel II网页本审阅工具未能打开；relative triple按所写ring map、右自由模和B中可逆态射直接核类型，
未声称独立逐页认证K-book或整个K-localization理论。审阅限于列明候选、费用和停止范围，非全部旧笔记重新证明。

## 2. 实际 relative triple 与源覆盖

- R→B_b及R→∏B_b是实际单位环同态；f(v)可逆给[R,L_f(v),R]合法relative triple。
  两项自由模的Euler类为零，与Perf中的复形非零、relative类非零是三个不同断言。
  特定Gaussian单向triple的relative非零仍unknown，未由对象非零偷换。
- 407无闭合词的det=1对所有复参数成立，所以逐fibre trace-norm及其product topology中路径
  1−tzρ_b(aU_q)始终可逆。仅这一topological connecting类为零；不推代数K类为零，
  不推共同uniform-growth拓扑可用，更不否定410/411另一个实际扩张中的已证非零类。
- 本DGA到H⁰的canonical quasiiso只约束quasiiso/derived-Morita invariant的ordinary读出。
  filtered/integral/metric pair及secondary torsion是合法额外结构，尚须独立构造和付费。
  不能把“底层经过旧商”本身当作任何新算术输入不可能的论证。

## 3. 全源指数化、原费用和414限定

加权L¹导数半范数满足p_N,m(r^{*n})≤p_N,m(r)p_N,0(r)^(n−1)，
从而exp_*r及exp_*(−r)在全S_exp中逐半范数绝对收敛，单位来自真正unitization。
由已在源单位化中的unit lift，relative exactness使这一个boundary recipe对所有r为零，
故同时消去全部Pan和537非根。这是有定义域的全源失败，不是所有boundary的零化。
Fourier端|exp(hatr)−1|≤exp(||hatr||∞)|hatr|给du/Dlog上界；
固定窗||r||₁≤√(2L)||r||du，其余Fréchet导数费未被du统包。
414的u仅在multiplier中有酉lift、在相关原单位化中无unit lift；本零化结论不适用于它。

主稿已明确扣除409–437强旧：实际非零相对K类、2a log p轴迹、两位粘合/忘却、
432规范HH₁电荷和437无共尾线性有限部的合法存在性反例。未将这些旧结果再次计作本轮新输入。

## 4. Raw物理源确已送入算子，但尚未送入regulator

h_r(s)=r(−s)、F_r=VU(h_r)V*对compact r是合法旧原时间卷积构造，
不是DGA的Schwartz dilation U_r。其||F_r||≤||V||²√(2L)||r||du及Dlog转换正确。
432(8)的单项情形适用：非零compact h_r使F_r−uF_ru*非紧；431(12)和原深p行列证明亦支持。
故q(u*)⊗q(uF_r)不是HH₁定义域中的闭链，不能赋Ω值。
全S_exp/Pan扩张仍未证明；Pan∩C_c∞=0，故仅compact域不构成全主关系通过。
原有界map的费用不自动支付尚未定义的闭链、local orders或截面lift费用。

## 5. 逐位trace与物理压缩的关系反测

圆周periodization的fixed窗L²上界可付，P=Cp的均值为−¼∫Ch<0，因而所有有限位都不消p。
537非根对足够大p可见，不能弥补关系失败。primitive source的两个pole degree也不是圆周本身的数据。

η₀(x)的多项式在x≥2严格正，p₀^sharp=p₀，所以每个有限素数q均有
L_q(p₀)=2(log q)Σ_(k≥1)p₀(klog q)>0。这个反测保全部prime powers。
完整arch/contact与finite总和才抵消主关系；局部order本可非零，故未泛排协同det line/transgression。
线性原子point evaluation在du/Dlog上不连续的窄bump证明正确，且与二次correlation的
|C_r(s)|≤||r||₂²及fixed q全部pp界区分，未错推原完整prime form没有fixed窗费用。

物理半线Hankel块的HS核积分、乘法缺陷和迹公式直接成立。
正Fredholm determinant确实存在，small-t二次项是真A∂；但其在非零P上>1，未下降为Pan类。
未将此物理边界与actualρ_p认同，也未把small-t Taylor项冒称large-n RR leading项。

**本审阅发现并已修正一处域标记：**主稿§7原先把A∂≤L||r||du²写在一般S_exp源之后，
未显式给支撑假设。root已在公式(6)前补“两个含L的上界仅对supp r⊂[−L,L]成立”。
全S_exp仍只有weighted L²等式；此修正后费用量词与独占稿一致。

## 6. 截面、过滤、容量及正反控制

真曲线的连接映射δ(y)是local jets可glue的障碍；δ=0后lift构成L(D−E) torsor。
P¹上O(−2)→O(−1)例中δ:k≅H¹O(−2)确实展示非零boundary不能自动给section。
该局部gluing例未冒充407整个idele fibre复形可缩的同一事实。

P¹_Z整格的jets、kernel ideal (p^k,z^m)、另列的乘法过滤均合法；没有错误合并矩形ideal乘积。
toric sup小截面log#=a n(n+1)+O_a(nlogn)与coefficient metric下det-degree恰a n(n+1)是不同但有控比较的metric。
不能泛称det line无二次量；同det的两对角格的local elementary divisors不同，故scalar determinant不恢复全部过滤。
固定离散整格上的连续map限制已保complexification/family/Picard/变域等合法逃逸。

连续±d边界resolution在open上可缩、有效boundary length同为2，却保z†=−z时trace型号不同；
因此局部有效性与n²容量本身不足以给同一Weil极化。
函数域另需真实C×C signed对应、有效截面乘法、RR/Hodge及全部periods/两pole身份。
prime稿已将Z/deg(v)Z收窄为模数/次数方向，不将整个C_K/K_v*错误压成有限商。

## 7. 消费结论与停止范围

完整Γ finite-part/contact、所有proper powers、双pole及complex mixed在各稿均保持；
405/568的解析Q身份不是新boundary→capacity身份，后者仍欠独立整模型、可解实际lift与同源RR比较。
要求“regulator pairing=Q且正”仍是等价/充分包，未被计作已证输入。

本门是更强旧资产恢复、标准机制的具体准入和直接反测，分类为来源0/旧推论测试恰当。
未得新classic独立容量或无界成长后果；strong-old542+555→557 whole leading4/5负惯性上预算不变，
不代实际负谱lower；低频/core/coupling/Ξ与长期Goal门不变。
仅停止所写裸指数、单向det、periodization、正压缩及旧线性有限部自动扩域；
新relative边、合法无限转移、phase/自然平均、filtered integral family、真实链补偿均未被排除。

## 8. 最终审阅版本

以下是实际文件字节SHA256；hash仅绑定审阅版本，不认证数学。

| 文件 | SHA256 |
|---|---|
| goals/reviews/2026-10-22-boundary-regulator-source-and-arithmetic-sections.md | 3fc7273767165c2893a1442e8f2b9cd8e772a0bacc6029d0b7fa78e0753be57a |
| reviews/2026-10-22/boundary-regulator/relative-k-and-secondary-class.md | 30fd9fa29e595b08c02720e913c850849251fe7a5f748791dc676791813d8879 |
| reviews/2026-10-22/boundary-regulator/prime-boundary-source-and-local-orders.md | 5863240108cfd956412d89f2c0982a86be2d4b60e71c448e4bae9a574ade948c |
| reviews/2026-10-22/boundary-regulator/sections-filtration-capacity-and-controls.md | 236288c7fb6799936478f6c10b2d1a62b168352a39b500a87297016f7ad8dac4 |
| reviews/2026-10-22/boundary-regulator/physical-compression-boundary-test.md | ac2c3dcf85ad3488ddc0ff49638ca56245ace057204c3c18f04386a3073aad42 |

上述最终范围限定PASS，无剩余P1/P2；若正文或独占稿语义改变须重闭受影响前件。
