# C004：实际双线性源账本与有限秩近似逆审

2026-10-13。恢复 AGENTS、README、STATE、check/show、现 Goal、C004、
D20261013E 和实际工作树；只修改本文件，不结算 cadence，不改 STATE。
逆审对象是 source-audit.md 及 compact-defect-audit.md 的主要候选，
采用“完整双线性型先消去同源项，再用有限秩近似”的组织，
不从保存的 2×2 数字矩阵、ζ 零点或已有 Weyl 序列结论出发。

## 1. 原件和可用输入

核读 [Connes–Consani 作者稿](https://alainconnes.org/wp-content/uploads/Selecta.pdf)
本地 `tmp/pdfs/c004/Selecta-author.pdf` 的 Theorem 1、4.6 (84)–(85)、
4.4 (82)、(72)、Theorem 6.11 及 Appendix B 对应式。
作者稿是55页，不能把其公式号当 arXiv v1 或出版社排版的公式号。
本审查消费的旧独立输入仅为真实 Sonin 正投影 trace 恒等式

    T_S(g)=Tr(theta(g_m) S theta(g_m)*)=Gamma(g)+E(g) >= 0,
    E(g)=integral integral g(x) conjugate(g(y)) e(x-y) dxdy,
    e(t)=epsilon(exp(abs(t))).

这里 `g_m(exp y)=g(y)`，Gamma 的 actual multiplier 是
`K(t)=2theta'(t)=Re psi(1/4+it/2)-log pi`。
Theorem 4.6 的恒等式对全部紧支光滑源成立；符号比较的小窗限制不在此恒等式上。
原文的正 trace 是完整空间上的正算子 trace；Sonin 空间不由 scaling 保持，
不得使用虚假的 Sonin 子空间酉表示。
对合法 smooth g，正 trace 有限，所以 `theta(g_m)S` 是 Hilbert–Schmidt；
任意两个这种源的交叉产品是 trace class，可合法极化。
本文以下的反例全在原 smooth 类中，不要求全部 L² 源有有限 Sonin trace。

## 2. 不靠 prolate 数值的连续核认证

作者稿 (85) 的每项是单位向量间的 strongly continuous scaling 矩阵系数，
范数至多1，系数为 `lambda_n/sqrt(1-lambda_n²)`。
截断 Fourier 算子在 `[-1,1]²` 的核是 `exp(2pi ixy)`。
将其 Taylor 截断到 m 项给秩至多 m 的算子，Hilbert–Schmidt 误差至多

    2 exp(2pi) (2pi)^m / m!.

故其奇异值可求和；even 自伴截断 Fourier 的 `|lambda_n|` 同样可求和，
无需消费任何记录的 prolate 特征值近似。
若 `|lambda_n|=1`，对应源及其 Fourier 变换都紧支；Fourier 整延拓在开集为零，
只能为零，矛盾。于是每个 `|lambda_n|<1`；由 lambda_n→0，所有分母有统一正下界。
上述级数一致绝对收敛，epsilon 在 rho≥1 连续有界。
xi_n 与 zeta_n 支持正交给 epsilon(1)=0；反演扩展因此在 t=0 也连续。
这里不声称 e 在0可微；primary 的导数跳跃不影响本论证。

任意有限源区间上核 `e(x-y)` 平方可积，E 是自伴 Hilbert–Schmidt 算子。
进一步，将核以有限个矩形阶梯函数在 L² 中逼近，就给有限秩核算子并在算子范数收敛。
因此，任何有界源嵌入／限制和正交矩投影的前后复合仍紧，
并非仅依据“原件称 infinitesimal”便假定所有复合紧。
尤其这里是 E，而不是与微分生成器复合后的 `E composed with Q`；后者另有主项。

## 3. 先核完整 Weil 双线性式，再选真实 p2 域

令 `ell_s(g)=integral exp(sy)g(y)dy`。实际完整源型是

    QW(g)=Gamma(g)
          +2 Re(ell_(1/2)(g) conjugate(ell_(-1/2)(g)))
          -sum_(n=p^k) w_n [R_g(log n)+R_g(-log n)],
    w_n=Lambda(n)/sqrt(n),
    R_g(t)=integral g(y+t) conjugate(g(y))dy.

因此在合法 source 级别首先有精确差额

    QW(g)-T_S(g)=pole(g)-prime(g)-E(g).

这不是辅助反向核 H，也没有删除完整 Gamma 因子、极点或 primepowers。
取 a=log2，B=(-b,b)，令

    G(y)=u(y+a/2)+v(y-a/2).

若 `2b<a` 且 `a+2b<log3`，两 patch 不交，
`||G||²=||u||²+||v||²`；所有正相关支撑只可能在0和a的2b邻域。
0的邻域没有 primepower，a邻域恰有真实 n=2。
直接代入相关积分而非套用矩阵得到

    prime(G)=2 w2 Re <u,v>,     w2=log2/sqrt2.

正负 log2 原子各贡献一次，故对角相同源 G=(h,h) 为 `2w2||h||²`；
不存在把 w2 漏成 w2/2 或重复成2w2的歧义。
取每个 patch 满足 ell_0=ell_(1/2)=0，则移位仍保持零矩，
总 G 及所有两个源的极点双线性交叉严格为零。
此处不需要 ell_(-1/2)=0，不能错误声称三项矩均已消失。

在该域，准确差额于是为

    delta(u,v)=-2w2 Re <u,v>-E(G).

同源 Sonin 项已经保留完整交叉；不能从两个对角下界自由极化得到它。
本式也完全解释冻结 `a=log2,b=log(3/2)/4,mu=13/5` 的结果：
`a+2b=log(sqrt6)<log3`，`a/2+b=log6/4<log(mu)/2`，
后一项等价于 `mu²>6`，由 `(13/5)²=169/25>6` 精确核验。
不存在需新数值支付的支撑前件。

## 4. 生成器、额外矩及合法 smooth 密度

令 `V={h in L²(B):ell_0(h)=ell_(1/2)(h)=0}`，
`L=D(D+1/2)`。精确地

    L C_c^infty(B)=V intersection C_c^infty(B).

正向由分部积分。反向给 h，先定义 `q(y)=integral_(-b)^y h(t)dt`，
ell_0=0 使 q 紧支；再解

    eta(y)=exp(-y/2) integral_(-b)^y exp(t/2)q(t)dt.

分部积分给 `integral exp(t/2)q(t)dt=-2ell_(1/2)(h)=0`，
所以 eta 也紧支，且 `(D+1/2)eta=q`、Leta=h。
这给合法原生成器，不依赖 distributional endpoint 的猜测。

V 中 smooth 零矩源 L² 稠密：先 smooth 逼近，再以两个固定 smooth 函数纠正矩。
这些校正函数存在，因为1和exp(y/2)是独立的 L² 矩向量；
若其值域在 smooth 类上不满，某非零线性组合将与所有 smooth 函数正交，矛盾。
任意有限个 Mellin 值／jet 都在固定 B 上是连续 L² 泛函
`integral y^j exp(sy)h(y)dy`。复 s 在实域取实虚两项约束即可。
在这些约束下同一有限维值域校正证明 smooth 核类稠密；
约束作用于总 G 而耦合两个 patch 也不破坏此论证。
其平方惩罚是有限秩算子，不能消除下面的无限指数。

## 5. 有限秩近似证明整个修复类失败

在 `V directsum V` 上，J(u,v)=(v,u) 是自伴 involution；
其±特征空间 `(h,h)`、`(h,-h)` 都无限维。
上述差额的唯一 bounded L² 延拓是

    Delta=-w2 J+K,

K 是前述 E 的压缩加负号，因而紧自伴。
再加任何诱导在此源 L² 上的紧有界自伴 correction B，仍为同一主项加紧算子。
给任意 ε<w2，取有限秩自伴 K_r 使 `||K+B-K_r||<ε`。
对 J 的+空间与 ker K_r 的交，在其中有

    <z,(Delta+B)z> <= -(w2-ε)||z||²;

J 的−空间有对应严格正下界。
再施任意有限个连续源约束，只多交有限余维空间，两边仍无限维。
这证明任意这种 compact correction／有限矩修复后，正负指数皆无限，
不是只给一个特殊 h 或一个2×2负试探。
任意有限维严格负空间有 margin，可将其基底在 L² 中以合法 smooth 核类逼近，
差额有界保证负定性保持；所以原测试类也有任意大的负定子空间。

精确本质谱亦可从有限秩信息核验。
J 的两个无限维特征空间给正交单位序列；紧 K 把序列送至0，故±w2皆为本质谱点。
同时 `Delta²-w2²I` 紧。在远离±w2的闭谱区间，其绝对值有统一正下界，
该区间谱空间若无限维将违反紧性；故没有其他本质谱点。
任意有限余维约束的压缩与原算子只差有限秩（在有限维正交补上延拓即可），
所以结论不要求这些附加约束由 J 保持。

若 `Delta+B+C I>=0`，在 J+空间的弱零单位序列上取极限，必要 `C>=w2`。
`C=w2` 未获充分性；剩余紧负谱仍须另付。
这里的 compact 条件是 **诱导的有界源二次型紧**。
一个源映射本身紧，与 unbounded Gamma 型复合后未必诱导紧 Gram difference；
没有支付此前件的 source 修正不在本排除类内。

## 6. 所有支持参数与精确无费用阈值

写实际源区间 `I_lambda=(-log lambda,log lambda)`，lambda>1。
对任意 lambda>sqrt2，选

    0<b<min(log(lambda)-log2/2, (log3-log2)/2, log2/2).

本地两 patch 全在 I_lambda，全部上述结论原封成立。
lambda即使大于2，也只使用其中的这个本地合法域；
不能因全域有更多prime便说本地相关突然出现它们。
新增有限 Mellin 约束的个数和参数可任意固定，局部 V 仍有限余维无限维。
这给每个 lambda>sqrt2 的无费用桥失败，而非仅冻结 mu 的结论。

若 1<lambda≤sqrt2，source 支撑在 primary Theorem1 的窗内。
自相关在正负 log2 及外侧为零；端点时 smooth compact convolution 同样为零。
极点由 ell_(1/2)=0 消失，故 QW=Gamma；Theorem1 给 `QW>=T_S`。
额外有限矩仅缩小测试域，不破坏该下界。
因此原无费用比较 `QW>=T_archSonin` 在这些有限矩条件下的全源支持阈值
确为 sqrt2。小窗正方向是旧定理，阈值后的实际 prime／compact 失败是本次消费后果。

本质谱±w2仅指 **两 patch 上的差额 bounded L² 实现／其有限余维压缩**。
既不称完整 I_lambda 差额的本质谱恰为±w2，
也不称 QW、Gamma 或 T_S 各自的本质谱是它们。
原 smooth QW 与 T_S 共享增长的 Gamma 能量；差额负并不使 QW负，
更不提供 RH 反例、真正最低态判定或 prolate 谱排序。

## 7. 新旧比较与宏观强度判定

相对基线 `3a72930e9f9f554b03b41d17d8c8002f1813ca82`，
`git grep -i sonin` 在 notes/reviews/goals/literature 仅命中旧 literature 的一行有限S摘要。
旧 Sonin 原 trace 与 compact E 不计本次新输入；
本次新内容是将同规范完整 actual 型的首个prime主项精确接上，
给所有支持参数的精确比较阈值、无限负指数、compact／有限矩类及质量费下限。
这一基线检索不证明世界优先权，外部评议和全体文献检索仍未完成。
本审查与 source／compact审查的对象、权重、量词和域一致，没有发现数学反例。

本结论的规模明显超过一个孤立线代反例：
它排除所有 lambda>sqrt2 的全源统一桥，以及每个固定域上任意 compact bounded
source-form 修复、有限 Mellin 值／jet 惩罚和有限连续准入约束。
宏观意义是：archimedean Sonin 的正来源与其 infinitesimal 差不能免费承载
第一个实际 prime 交叉，有限消失条件和紧校正无法修复这个断点。
但其方法类仍以固定 archimedean Sonin 为比较基准，
只是 complete Weil 正性核心的一个自然候选，不是所有正 trace 或几何有效机制。
旧 Goal 第十节明确禁止把多份小障碍累积替代核心成果；
因此本审查不支持仅凭“无限指数／精确阈值／合同完成”宣告整个 Goal complete。
主代理应将它作为严格实际方法边界保存；若要主张达到宏观门槛，
须另证明此具体 fixed-source 类为何具有旧第十节要求的核心规模，
并完成全 Goal 要求的独立总审与保存审计，不能从局部合同验收倒填规模。

未排除：真正 semilocal 正来源；诱导非紧的 arithmetic signed bridge；
实际支付至少 w2 的质量费并另审剩余低谱；非有限余维的合法低域比较；
改变投影／表示同时重新证明正性、同源恒等式和增长支持费用。
完整实际联合正性、最低态／prolate 与全补空间预算仍未付，实际瓶颈未消除。
停止／重准入与两份审查一致。唯一下一动作是主代理消费上述限定范围并保存结算；
本审查无待处理后台进程，不修改研究计数。

最终主笔记消费复核：只读530与C005，没有发现关键符号、域或量词错误。
530仍只称两patch差额ess和诱导紧二次型修复；C005保留真实正交投影、
trace-class及同域同范数前件。此复核不是额外研究轮。
