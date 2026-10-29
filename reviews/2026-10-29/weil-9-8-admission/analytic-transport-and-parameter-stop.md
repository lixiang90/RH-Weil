# 固定 L=9/8 的解析迁移门与停止条件

状态：**解析准入说明；未执行数值，没有新的全对象正负结论。** 不登记研究轮次或 successor contract。本记录供 root 连同实际新输入消费；不是已消费结论。

## 1. 对象、来源与旧结果边界

沿 537 及 C009 的原 classical Weil form：任意 complex test，原 du/Dlog 范数，完整 Γ、全部 contributing prime powers、contact 与含负 odd 项的 pole form。原 source-exact 恒等式与闭形式/core 迁移可用于新固定区间，但有限矩阵不自动覆盖全对象。目标是 I=(-9/8,9/8)，autocorrelation 长度 2L=9/4 的原 Q 下界；不是 growth-RH 或 Goal 完成。

已读 `notes/537-source-exact-weil-window-positive-tail-admission.md`、`reviews/2026-10-14/c009-tail/{object-source-audit,signed-reverse-audit}.md`，及本次恢复的 `literature/local/2026-10-29-weil-9-8/source/frozen-source/publication/manuscript.tex` 的相关尾、Schur、projection、kernel、overlap、column 段和 `reproduction/source/12-raw_column_producer.py`。后者严格 FROZEN L=17/16，直接运行新参数会拒绝；没有改原文、执行 producer 或下载 PDF。

这是对同一 frozen commit b6cd2183c1e79c6c27a34267812a7b2d73ed1b59 的新读取，不是新版本。恢复的 22 小文件与旧 SHA256 manifest 匹配由 root 负责，本记录不冒充独立验包。旧最强资产仍为原 L=17/16 的完整 source/analytic/Gram 闭合；不能由旧有限 head 或尾丢弃障碍推出新 L 的符号。

## 2. 首个独立解析门：全平移算子 M

保留 Ω=256、原标量 7/2 时，M=(7/2)I−Cp。新集合为 {2,3,4,5,7,8,9}；n=p^j 的 shift 是 j log p，weight 是 log p/√n，故 9 的 weight 为 log3/3（Q 的 coefficient 为 2log3/3）。所有旧 shift 的归一化 t_n=log n/L 也改变。现有 15 个 shift（含 0）及 M² 的 **225 ordered pairs**，原 13/169 不够。

可直接执行一个不依未知 ζ 零点、不依 full-head 数据的 rational gate。取 x=u/L≥0，a=5/8，q=1+ax²，使用原 log/root 有向包围，并给 √9=3；令 t_n^±=jℓ_p^±/L，w_n^+=ℓ_p^+/√n_lower。按下列有向切点建立八 cell：

`0, 1−t3^−, t4^−−1, 1−t2^−, t5^−−1, t7^−−1, t8^−−1, t9^−−1, 1`。

负移从 {2,3} 开始，依序加入 4、5、7、8、9；正移从 {2,3} 开始，先去 3 再去 2。负移略早加入、正移略晚移除，逐 cell 上包围真实 row sum。尤其 log3/L<1，中心同时有 ±log3；旧七 cell 不适用。

在每 cell，按 multiplicity 取 W=Σw_n^+，B=Σ_negative w_n^+t_n^−−Σ_positive w_n^+t_n^+，D=Σw_n^+(t_n^+)²。检查

P_T(x)=a(T−W)x²+2aBx+(T−W−aD)，T=7/2。

在两端及凸时的内部顶点精确求最小值；若所有 cell 的共同下界 d>0，则 q(T−r_q)≥d，给 **m=8d/13>0，mI≤M≤bI，b=7−m**。同时核验切点次序、log/root 包围方向与全 cell 覆盖。原 T=83/32、m=9617/10400、b=63183/10400 均不继承。仅 triangle bound 的全 weight 和不能支付 M>0。

后续 inverse envelope 必须选 μ<m（例如明确的新 μ=m/2），不能照搬 μ=29/32。本门若未过，只表示此 q/此分解未准入；不得据此写 Q<0。到此停止，不自动进行 q、L、Ω、degree 的参数搜索。

## 3. 全 Fourier 尾：可重证的部分

4096 个原区间、h=1/32、Lagrange weight sum <2^24570 不变。||f||=1 时 |F^(j)|≤√(2L)L^j=(3/2)L^j<2L^j；若外带能量 <1/2，则某 |t0|≤256 有 |F(t0)|>1/16。新 remainder 满足

2(768L)^4096/4096! < 2(81/128)^4096 <1/32。

因此原 **δ=2^−49158** 可对全 complex H_L 重新证明。Γ 外带 A(t)−7/2>C=123/1280>1/16（|t|≥256）与 L 无关。于是 T_tail≥C(I−B_band)，仍有 τ=δ/16 的标量尾补偿。

c=ΩL 现为 288。原原始积分精确给

e0(c)=(2/π)∫_c^∞ sin²x/x² dx，e1(c)=(6/π)∫_c^∞(cos x−sin x/x)²/x² dx。

非负积分尾随 c 单调降，故原 c=272 已付的 81e0<C、27e1<C、||h0||<1/29、||h1||<3/50 在 288 保留。原下界 (c−1)/(πc²)、3(c−2)/(πc²)，配 π<4，在 c=288 仍给 ej>2^−11>δ。S=I−B_band−δI≥0、v0=(2L)^−1/2、v1=√(3/(2L))u/L、hj=Svj，parity 消交叉；同一个 complex minimization 给 U=81|h0><h0|+27|h1><h1|。这是全 tail 证明，不是 head 外零点假设。

## 4. Projection 与 cross/complement 的新付款

N=448、ellipse 3/2 时，原 projection 公式变成

r² ≥ 72L exp((5/6)ΩL)(2/3)^896 = **81 e^240(2/3)^896**。

可用 e<68/25 的 rational 上界。若候选 r=2^−85，需独立精确检查 `81·68^240·2^1066 <25^240·3^896`；本记录未执行该整数门，不声称通过。原 r=2^−95 不继承。也可直接保留上述显式 rational r² 上界并据此编译。

pole 的 p=2^−440 可按原 Taylor 推导重证：L/2<1、exp(L/2)<2、√(2L)=3/2 仍给 residual <3/448!、全 evaluation norm <3，故 pole operator error <36/448!<2^−440。负 odd pole 始终保留。

band κ<896 的 Γ 积分界不变，||e^(itu)||=3/2；tail norm 界如上一节，故在支付新 r 后仍可取

e=1389r+p，n=896r²+p，h=11696r²+p。

分别用于 cross、complement **下界**、complement **范数**；不可互换。正 U 的 complement 仍需 10800r² 范数付款。必须检查 m−n>0 及 Certification Theorem 的全 block-Schur/inverse 条件，不能只取压缩块 PSD。

## 5. 新 kernel/column 放大是独立精度门

保留 Ω 与标量 7/2，则 1024 个 Γ moments 的定义不依 L；合法旧 interval packet 可凭同源 provenance 复用。**其误差放大依 L**：2ΩL 从 544 变为 576。原 midpoint error <2^−1023，只能据旧证明方法支付 2^−1023 cosh576；e²<8 给它 <2^−159。加新 Taylor remainder 后可保守得到 operator allowance <2^−156，不能继承 2^−204。

精确新门为

ε_H ≥ (9/4)[ R_T + ε_θ cosh576 ]，R_T ≤914·576^2048/2048!。

这里 ε_θ 包含 Binet、moment oracle 与 rounding 全误差；Binet 不能再付一遍或遗漏。由 e<3、3·576/2048=27/32、(27/32)^5<1/2，可得 R_T<2^−399，足以支持上述保守 allowance。若仍要求旧 ε_H，则必须实际提升且验证 moment/Binet 精度，或重新用该公式预算；不是只改输出 bit 数。原 Binet remainder bound 与有限 moment packet 的 provenance 必须单列。本记录不选择或执行新精度搜索。

tail column 的 sinc Taylor 门同理替换为 **576^2049/(π·2049!)**，重新支付 rational π 的误差与 rounding，不能沿用旧 2^−513。原 Machin 160-term π 本身不依 L。raw column factor ΩL² 从 289 改为 **324**。v0/v1 归一化与新 raw Γ 一起更改；896 coordinates（448 exact parity zeros）仍须全验。只有新全 column error ε_Ucol 已付，才可用 ||ΔU||≤2(81/29+81/50)ε_Ucol+108ε_Ucol²<9ε_Ucol（须满足原小误差条件）。原 9·2^−512 不自动成立。

## 6. Raw source、Gram 与整数编译

raw Γ_nn=2L/(2n+1)=9/[4(2n+1)]；旧 17/8 的归一化及 row weights 必须全部替换。若沿原 Qd=diag(8(2n+1))，则 Γ=18 Qd^−1，旧编译中的 17、289 需从新 congruence 推导为 18、324。raw U 因子由 81/Γ00=27/Γ11 得 **36**，不是 648/17。

M² 必保留三重 intersection I∩(I−a)∩(I−b)、225 ordered pairs、nonzero one-sided boundary term。B=E*M²E，与 A² 不同；D=B−A²≥0 是 complement leakage。N=448 不变时 expanded recurrence 的 i+j≤894、row-zero seed 到895 等域约束仍在，但全部新 centers、weights、边界值和 directed row widths 重算。

一个可复用结构的 source-center padding 上界：若每个 physical shift 和 weight 的误差≤η=2^−2048、i,j≤447，原 overlap Lipschitz 仍≤(4·100128+2)η=400514η。新 absolute shift weight sum W_abs<11（必须由新 log/root enclosure 认证，原 <10 已失效），14 个非零 weight。于是 raw pair padding 可取

121·400514η + 3(2·11·14η+196η²) < 48463121η <2^26η。

该式只支付 center perturbation；不是整个 recurrence interval width、不是 orthonormal operator εA/εB。仍按新 Γ 检查 max_i Σ_j radius_ij/Γ_ii，独立 oracle 全 rows，不得仅引用旧 2^−220。kernel rounding、完整 operator ε_H、columns 分别支付，不相互遮盖。

重新构造相同对象的两套完整整数 compiler、positive congruence、全部 448 rows/两个224 parity blocks、exact Gram residual row inequalities及负控制。旧 target exponents、residual packet、X Frobenius ≤8、μ、inverse allowance、compiler receipts 均不继承。一般 inverse error 公式可复用，但用新 μ、实测 y 和完整 ε；误差 ε_D 还须包含 B 与 A² 的传播。仅把 JSON 参数或 Γ 常数改掉不构成 certificate。

## 7. 单次准入与停止

最早执行新八 cell weighted-Schur scalar gate及第3节解析尾门；它们是有明确输入、可失败的完整算子准入。若通过，再由 root 决定是否接受一次新 source/precision/cross/Gram 的完整付款；本记录不预付该结论。证书的任一必要 gate 失败时保存失败对象与理由，停在固定 L=9/8，不由失败推原 Q 负，也不启动参数优化。

只有原对象/范数/域、全 prime coverage、Γ/pole、tail、M/coercivity、全 complement/cross、source intervals、inverse 与完整 residual 共同闭合，才可能产生超越旧 17/16 的新固定窗口结论。未知 full-head 数据时，9/8 的正性与负性均为 **unknown**。即使成功，仍不能消除长目标中 growing-support/主算术正性这一关键瓶颈。
