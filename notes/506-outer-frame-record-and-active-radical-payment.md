# 506：真实 closure 加强外域，与小活跃 radical 的算术付款

2026-10-11。第四周期复盘后的第一轮完整数学研究。
本轮工程与数学成果只计一次研究轮，未因代理、工具或新文件数量重复计数。

## 本轮确定的比例提升

当前新的数学下界为

\[
 p=\frac{66812491}{99194540}
 =67.355008652693989\ldots\%,\qquad c=\frac{805460}{10^8}.
\]

相对505，增加
`1002187365/122994474451826≈0.00000814823080034` 个百分点。
简单临界线与互异临界线的 dyadic、cumulative 渐近版本均成立；
分母保留全部非平凡零点及重数，量词是任意 `ε>0` 最终至少 `p-ε`。
完整连续推导、原计算准入与既有解析运输见
[新论文](../papers/outer-frame-simple-critical-paper.tex)及
[PDF](../output/pdf/outer-frame-simple-critical-paper.pdf)。

数学证书：[自包含数据](../output/am-outer-frame-certificate.json)、
[标准库 checker](../scripts/am_outer_frame_certificate.py)、
[根代理原源复验](../reviews/2026-10-11/am-outer-frame-exact-check.json)。
[完整独立算术记录](../reviews/2026-10-11/outer-frame-independent-execution.json)、
[最终发布独审](../reviews/2026-10-11/round506-independent/FINAL_REVIEW.md)及
[论文构建清单](../reviews/2026-10-11/outer-frame-paper-build-manifest.json)分别绑定实际输入。
本轮新证书没有执行新的 Lean 或 NaNoDa。
此前505比例 `66812491/99194552≈67.3550005044%` 已完成完整普通 Lean、
八个最终根公理审计和84,362声明独立内核重放，推送形式化仓库
[`14362fe`](https://github.com/lixiang90/RH-Zero-Proportion-Formalization/tree/14362fe21fa871a1a951597c573d1601f4755676)。
旧代码、证书、论文和网站提交记录均继续保留。网站验收仍未完成。

## 为什么这次能继续提高，而旧模型给出障碍

505公共证书的201胞使用原YA表示，其最弱付款不是所有原约束能够推出的最优付款。
完整形式化时已有201份只用原33变量行的另一组对偶证人。
本轮将其作为**不同的数学证人**重新精确支付；全部已高于新目标
`ell=805117/10^8`，未假称沿用原YA乘子。

余下40胞中35份505替换仍足够，只剩五个真实薄弱情形：
17的旧branch1、69、74、131、183。独立作者为它们构造精确可行的
旧线性松弛 primal，证明只换目标或旧对偶乘子不可能解决这一固定模型。
这些点被合法新anchor行排除，而且实际AM核在这五个点都明显高于目标；
所以该障碍只针对旧有限松弛，不是实际 `F8` 或 ζ 的不可达证据。
[原有限模型与实际核的执行证据](../reviews/2026-10-11/outer-frame-old-primal-obstacle-execution.json)
保留完整原程序和实际收据；复制归档不算新的算术执行。

本轮把74整胞做真实8节点closure重锚；69、131按最后跨度 `(6,7)`，
183按 `(1,2)` 各作四个完整闭branch；17也改为整个原胞的 `(6,7)` 四闭branch，
而不是只在旧不足子域附近选取样本。各段端点、空域判据、原REG扩展和盒约束完整核对。
结果是201不同baseline付款、35旧单帧付款和17新case，共253份，
覆盖全部241原胞及241反射。新增387行、529正对偶，使用288个原2196点表条目。

最低单帧为17胞第2新branch：

\[
 L=\frac{8244400676681470233488767397}{1024000000000000000000000000000},\qquad
 L-\ell=\frac{2596681470233488767397}{1024000000000000000000000000000}>0.
\]

完整原2,399拼接域每一份都在新 `c` 重算：2342原域、47旧替换84branch、
10份505替换20branch。最低仍是 `(406,70)` 的
`32992055894668884928258784247/4096000000000000000000000000000`，严格大于新 `c`。
若至少一子帧在强集，另一子帧有新全域 `ell`，故外域安全平均
`(805803+805117)/(2·10^8)=c`。这个安全界**恰等** `c`；完整有理最小值
另提供严格余量 `(L-ell)/2`。全盒残差、反射、闭端点和真正全零点费用都已独审。

## 新的解析工具：原核的强凸下界

本轮另证明原AM13核的双Fourier表示给出
`sup_R |w'''|<34`，使用卷积立方矩恰为 `1/10`。
256点的精确二阶区间加上完整导数余项，得到整个闭区间
`[9/5,21/10]` 上 `w''>17/100`。
不同作者改用未平移的原核闭式自动微分，独立重建全部点及连续余项。

证明、强凸二次minorant及可合法仿射化的公式见
[完整推导](../reviews/2026-10-11/am-fourier-curvature-proof.md)、
[程序](../scripts/am_fourier_curvature_certificate.py)和
[有理证书](../output/am-fourier-curvature-certificate.json)。
[独立闭式微分执行记录](../reviews/2026-10-11/am-fourier-curvature-independent-execution.json)
完整保留不同公式及256点、连续区间的核对。
这项工具未成为本轮 `c805460` 证书前件；也没有据此登记第二个比例提升或新的Lean成果。

## 无零路线：已经缩小真实待付交叉和

对实际 `M_long S_short² Q_selected` 卷积，设左右理想 `k,l`，
去共同gcd后剥六次幂写 `k/h=s a^6,l/h=t b^6`，`s,t` 六次无幂且互素。
活跃radical为 `Dact=rad(st)`，恰记录局部指数差非零模6的素理想；
所有因消去或纯六次幂仍存在的nonunit零继续保留。

在明列固定数域的线性理想计数输入下，本轮证明

\[
 \#\{(k,l):q_k,q_l\le CN,\ q_{Dact}\le R\}
 \ll_\epsilon N R^{1/2+\epsilon}.
\]

原真实系数有 `d_K(k)^2` subpower上界：每素理想的 inverse/two-plain 分解为
`2e+1`，一次wholeQ至多追加 `2e-1`，合计 `4e≤(e+1)²`。
左右Gram在**同一** restoration tuple 上使用同一个真实 `N'`，所以其低活跃块可绝对付款
`Oε(H R^(1/2+ε)U^ε)`。两独立height、原cutoff、finite-ray相位、mask、punctures、
恢复后独立三个尺度和有限Sobolev closure均明确保留。
不跨restoration tuples套用错误的 `1/N'`。

这一引理严格扩大504仅同六次无幂部分的付款，允许不同部分的小活跃radical。
在已限定完整连续盒 `δ∈[3/8,2/5],x∈[.49,.5],κ∈[.74,.75]` 上，
`Dact≤U^.62` 全块可付设计raw节省 `.0003` 的参考预算，并留额外正指数余量。
505单个target label可筛到 `U^.665`，这个更大阈值不外推到全盒。
一般lemma按实际 `rL` 给可变筛除阈值，固定 `.62` 实例不证明全局target几何覆盖。

[完整实际系数与无限计数证明](../reviews/2026-10-11/active-radical-mixed-cross-research.md)、
[公开复现](../reviews/2026-10-11/active-radical-mixed-cross-reproduction.md)、
[有限程序](../scripts/hybrid_active_radical_mixed_cross_budget.py)及
[原源复验](../reviews/2026-10-11/active-radical-mixed-cross-source-check.json)分别保留。
1349项默认有限检查、1352项含源检查只证明其有限范围，不代替书面的无限理想计数。
[小活跃子块独立审查](../reviews/2026-10-11/active-radical-independent/REVIEW.md)
另给3367项独立有理检查和实际公版复验；原记录按字节归档，限定范围不变。

剩余大活跃radical的有符号聚合仍未付。全行覆盖税仍是约5.4700倍，
目标 `.87495` 的必要count节省约 `3.7952664e-5`、variable-long raw门约 `.0002076021`，
还需height、width、profile、slot、mesh及全部critical-bin费用。
本轮没有新完整mixed估计、count节省或无零边界，原引用输入下的
`σ*≈.874957019420099` 保持。完整算术 `ArithmeticProbeObligation` 也仍开放。

## 各路线现状与下一步

| 路线 | 当前实际状态 | 下一个必须闭合的输入 |
|---|---|---|
| Weil／F₁全结构 | 极化、比较和存在性归约有明确scope；完整RH未证明 | 实际算术来源、主关系、全局RR／sections与全Weil正性，而非再假设所需结构存在 |
| 部分Weil与四阶能量 | 二阶接口和有限谱预算可用，原实际四阶节省未付 | 同一真实响应的中心四阶；flat端点 `v=1/3` 超过本轮比例需 `B4<196340687/601312419`，另付全部配置误差 |
| 四高prime原路线 | shared-factor／正tube部分已处理 | 原tube外 `Cout` 的聚合有符号省幂，保留实际 `k=pr`、全部mask与slow相位 |
| AM零点比例 | 本轮数学 `p=66812491/99194540`；此前p505已完整形式化 | 数学瓶颈为17胞新branch2的outer；新强凸行须整体有效并重付全域，避免仅抬存储舍入 |
| 原二次域无零区域 | 引用输入下三次边界保持；本轮低活跃块得到新真实付款 | 大活跃radical signed cross，加上新target全critical几何覆盖与全部费用 |
| 无零区域形式化 | 已有根证书、Mellin主信号和部分算术接口 | 完整HighData／Moments与 `ArithmeticProbeObligation`，不能用部分构建代表最佳无零区域全链 |
| 换数域 | 按用户要求暂停 | 原路线改进优先；没有从替换二次域登记新边界 |
| 自适应谱与正算子 | 各归约与指定模型障碍保留 | 来源明确的真实mean／error／高度输入；固定7/8条带不自动给所需深度 |

原论文、所有旧证书和旧形式化继续保持其历史版本。
当前外部79.62%候选仍不能供给已准入四阶输入；固定2610.08965v1审查的版本和
native计算信任范围保持，本轮没有重新宣布外部文献检索或全球优先权。

按第四周期复盘，比例的短期数学投入至本轮已完成一个全域净增益。
下一轮优先把已得新低活跃块用于原signedcross归约，并判断大活跃模数能否消费
真实双线性结构；比例若继续，仅尝试上述已证明强凸行，必须付全域净奖励。
本轮计数由0增至1；默认第6轮复盘，第4轮可提前，第8轮必须。
