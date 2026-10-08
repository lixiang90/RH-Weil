# 原路线第二周期复盘：不同作者范围与预算审查

日期：2026-10-08。审查者：checkpoint_audit，非复盘作者。
结论：下列冻结文本在已列前件和范围内 **限定 PASS**；没有发现需阻断本轮复盘的数学或协议错误。
这是全文审查、独立推导和有限有理算术核对，不是新增无限解析前件的证明或上游大型计算的重放。

## 1. 冻结身份与实读范围

canonical SHA256 均按 UTF-8、LF 字节计算。主审对象：

- [第二周期复盘](../../goals/reviews/2026-10-08-original-route-review-cycle-2.md)：163 行、11117 字节，`288f2813b1b436297fc7759116ab2f533492b717a5c371385e1aa4f114d76e4f`。
- [491](../../notes/491-original-period-edges-and-signed-core-statistics.md)：`28ff712f977b3a378a7d3df52d4335bb1a603d1105c2134f51e83e741c784149`。
- [492](../../notes/492-original-coherent-period-energy-and-product-ceiling.md)：`85939d014c11eb71e76e0e78fa87d0ebafda0505aa378deb42b532d501815ceb`。
- [493](../../notes/493-original-reference-subtraction-and-carrier-near-correlations.md)：`efbefb73a457e1bda079fdb9c003ec4bcf9c50d89a1f1c2053b548153371a67a`。
- [494](../../notes/494-original-double-deviation-and-upper-cauchy-core.md)：`6abe8a6ddc66178a4f67352ee8cb4138622c8bd78a103dea377f98513c7e839c`。
- [495](../../notes/495-original-carry-covariance-and-sparse-spectrum-barrier.md)：`ba1a406481c0aa7a14f3f9beba7c0282e1a00e3dc138caf9d1625b184c546b09`。
- [496](../../notes/496-original-masked-shifted-determinant-core.md)：`87f25bb46864759e154597e732500c44fec9da351b377eee9b5ffb73a8808c2b`。
- [prime-cutoff 源](hybrid-original-prime-cutoff-fourth-and-max-label-research-perron.md)：175 行、11733 字节，`d7aaee914be30cfee19b4aa62b3efcb36adaa0f058155cc05d2e82e1c8740062`。
- [prime-cutoff 独审](hybrid-original-prime-cutoff-fourth-and-max-label-review-high-product.md)：91 行、6467 字节，`fb707a9a2b2c879542c5f85c830192294a5cc18f48e6fedcbad016145091218f`。
- [Knausgård 专项总审](../../literature/supplements/2026-10-08-knausgard-2610-08965-audit.md)：134 行、8059 字节，`3dcd29a48680715523088b29be08812ed8615a15edf516213d4123a2ac30dffa`。

已 FULL READ 六篇 note、主复盘及所用必要研究源和独审；新 cutoff 的 trace 括号修改经逐字差分、反向身份和最终段落核对。
专项总审全文读过原134行，最终唯一“17/20分离集合”限定已读回并核最终身份。
本审查没有运行大型 AM/Lean/search pipeline，没有把 hash、旧 PASS 或形式化依赖清单当作解析证明。

## 2. REVIEW_PROTOCOL 五问

1. **改变了什么实际对象？** 491 支付真实低产品 edge；492 改善共同周期正能量；493 支付连续参考和实际 far；494 支付完整 mixed 并准确留下双偏差；495 给真实 carry 系数与消费合同。496 保留全移位 near 身份并加入真正完整低 q 前缀预算。表格明确区分这些实际付款、结构重写及辅助模型。
2. **原目标更真了吗？** 是，条件完整 `q_max≤X^u` 原子族得到比 global 更小的费用；但原 untruncated whole、中心四阶、simple-critical 比例和 σ 边界都未改善。复盘没有用子族范数推任意 signed 限制。
3. **还缺什么？** 低 q 前缀要先重付 major、cap 和需要的 edge，才能 exact signed subtraction 到 minor；顶端 q≈X 仍缺原真实 carry/near 的固定幂节省。中心四阶及计数消费是另一个接口。
4. **下一周期具体命题和预算？** 优先证明完整 cutoff 前缀的 exact 分区投影；随后在全部真实 mask、原系数、同 u 和 n 外 twist 下付顶端 carry/near。复盘给出的门槛可消费且留固定 ε 余量，没有将“可能输入”写成已有定理。
5. **继续、减少或暂停由什么证据改变？** 继续实际 cutoff 分区与算术 covariance；减少仅重写 cap、一般能量、抽象稀疏谱或重复 prefix 障碍的工作。改变决定须出现带全部端点的真实固定幂节省，或证明相应实际机制不能满足门槛。

## 3. 独立预算与量词核对

cutoff 固定 X、高度、φ/χ、normalizer 和原有限投影，真实素数截止 Z=X^u，`17/20≤u≤1`。
两端固定零点包的正费用最大值为

`max{0,u−2/5,6u/5−4/7,3u/2−11/14}=B(u)=3u/2−11/14`。

proper-power 差单独付款；原有限 repeated helper、被动 cutoff 的 physical 桥及完整 nn/unit 分区均保留。
新 trace 括号为 `|Tr((C_p C_Z)^2)|`，不能改成 `|Tr(C_p C_Z)|^2`。
该结论是完整原 χ-carrier signed 前缀，不能扩成逐 σ 界、平均绝对块、单 q 界或任意 minor 子集。
u=9/10 时 B=79/140；nn=9/20、chirp=2/5，严格次要；u=1 恢复5/7。
u=6/7+1/400 时 B=403/800，固定 dyadic 常数的准入仍须按 cutoff 源重推。

496 使用完整489周期接口；491 nonperiodic edge 子窗不能免费送入全 Poisson。
全部 b、ell aliases、原 Ω 带、Ψ 带、实际四素数与 same-u 恢复均须保留。
far 付款与 near 身份不能推出 near 小；八辅助 ν 的完整支撑不能运输固定零点包在原 J 上的估计。

前缀 minor 的待证费用正确写为 `max{B(u),B_major,Z,B_cap,Z,B_edge,Z}`。
若选优化491 remainder，则 edge 费用必须在完整差中；旧保守费用493/700、7/10、993/1400中，u=.9 时最大为993/1400。
这是待证明分区合同，复盘没有把这组数值认领为已完成 minor 付款。

真实一级 carry 输入 `∫W|T|≤Q²X^(−r)L^C` 配原 prefactor 的费用为 `QS X^(−1−r)`。
超过 nominal5/7 需 `r>u+w−12/7`；超过完整451费用 B* 需 `r>u+w−1−B*`，并有固定 ε 余量。
top u=w=1 时后一门槛约 .285801997046972；旧窄例 r=.01 的费用993/1400=5/7−1/200核对正确，但不自动投影已付 whole prefix。

## 4. 原目标与证据边界

原 nominal whole5/7、完整差3/7及 complete additive transfer9/14没有被 headline 改写。
451 的 σ*≈.874957019420099 与 B*≈.714198002953028仍依赖原全部前件，尤其 Hecke 全族输入；普通 ζ 的7/8不能删去这些依赖。
483 的 simple-critical p=`118513839290/175971686899` 与 distinct 比例分开；本轮未重放其大型有限搜索。
v=1/3 时独立有理计算 `(1−v)^2/p−1+2v=174172614863/533312276805`，中心 B4 还须同一实际 Weil 配置、误差和计数桥。
canonical 增长指数、辅助 signed covariance 与这个中心阈值不是同一个输入。

495 抽象稀疏谱模型只阻断 M2 推 M4 的一般推理，不构成 ζ 反例、actual 下界或预算饱和证明。
微宽 `(β−1/2)logT=O(1)` 不能由宏观 ordinary7/8推出；新密度命题仅作声明范围内的主来源比较，未替换已准入密度。
独核顶端 Ivic/HB 为3/14、GM为15/59、TTY另一支为11/48；publisher 下限279/314>7/8，不能外推到7/8。
这不是全库最新密度证明的重新认证。

[2610.08965v1](https://arxiv.org/abs/2610.08965v1) 的 simple-critical 主张 `1669159/2478195≈.6735382001819873` 高于483；差约 .00557702611914 个百分点。
作者公开的 [axioms 清单](https://arxiv.org/src/2610.08965v1/anc/lean/axioms.txt) 中该结论使用 `Simple673.Local.check_passes._native.native_decide.ax_1_1`，与总审记录一致。
它是计算信任前件，不是 RH 公理；本审查没有认证全部计算，也没有由此否定论文结论或替换项目比例准入。
专项总审的轻量核对、conditional formal chain 与整个 search/Lean 重放被准确区分。

完成本轮六次研究后的复盘及独审后，可按协议把轮次计数重置0；这不是终止、暂停或缩小完整原 goal。
下周期默认六轮、最早四轮、最迟八轮再复盘的安排符合协议。本审查没有修改 cadence、索引、源文件或 Git。
