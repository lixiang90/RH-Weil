# 双因子 Perron、条件完整误差与 484 的不同作者全文审查

2026-10-08，perron_reviewer。只新增本独立审查；未修改作者源、旧冻结输入或 Git。
审查方法为不同作者 FULL READ 与逐式独立推导，有限有理计算只复核费用和隔离区间。

**结论：限定 PASS。** 普通 ζ 的全高度 [Rθ] 是引用前件，本文不重新认证该前件。
核准的新增结论是实际双因子短项、固定 H=V² 费用族、条件完整误差
43/75、完整第四矩传递误差 713/1050，以及保持 482 对象的真实素数带扩大。
核准 484 的记录与 451 既有 σ* 在该费用族中的条件新应用。
未得到新的 whole 增长、常数级四阶预算、零点比例、无零边界或 RH 证明。

## 1. 冻结身份与全文阅读范围

最终研究源：
[双因子 Perron source](hybrid-original-double-log-derivative-perron-research-checkpoint-audit.md)，
427 行、18807 UTF-8 LF bytes，
SHA256 8673c02894a1503a8e4bb9e25bfe1c693347ddfc1f5acb070b55a64b3c275b27。

最终归档笔记：
[484](../../notes/484-original-double-perron-conditional-remainder.md)，
194 行、8013 UTF-8 LF bytes，
SHA256 38c94314687ccddf1cda08b2d7611c0e1409927b0fb62fdfb0760b32256d1cad。

canonical 规则仅把 CRLF/lone CR 统一为 LF；不 trim，不改变 EOF。
本审查全文实读原 source 的 426 行和 484 的 184 行，另读回最终限定修订及 484 新增 §5。
最终 source 仅把旧第 410 行改为内部/外部理由的两行澄清；
反向替换精确回算旧 426 行 SHA
d7629521af216df4b266a2c977cee4984b5f4d67d448751bbc8532cf0b15e04c。
独立读回新第 410–411 行并核对其他字节完全不变；主数学公式未修改。
484 的前 184 行精确回算原 SHA
50feea9332f679f466bc8a7fbfec87db721e928c653572ad41270f814108cc8c，
故 194 行版本仅追加十行有限检查范围；其前三节数学结论未变。

以下相关输入均由本审查者在本轮全文重读，随后只读核对 canonical 身份。
没有以作者的结论摘要代替其完整证明，也没有用有限素数枚举代替无限估计。

| FULL READ 输入 | 行数 / LF bytes | canonical SHA256 |
|---|---:|---|
| [446 ordinary logarithmic-control](../../notes/446-uniform-prime-twists-on-the-original-gabor-frame.md) | 218 / 9890 | 08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf |
| [451 已有三次边界及依赖](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md) | 244 / 10207 | 17ce7fea8c881ebd4034657b7039e99897d4ff9532348993ba329c46e3c4d487 |
| [476 条件完整增长](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 96 / 4448 | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 |
| [481 完整费用与参数](../../notes/481-original-type-ii-squarefull-tail-and-optimized-moment-transfer.md) | 239 / 10661 | 4ce3ea2ac087d734142c8788607c1c54fc6887bcf535c806c88097447afdc63e |
| [482 条件 μ-Perron](../../notes/482-original-conditional-mobius-perron-remainder.md) | 139 / 5125 | c0abff933a180f5591412f82772634091f8db0e2079f846772f8a7047ed4a912 |
| [482 完整有限 Perron source](hybrid-original-optimized-type-ii-remainder-research-checkpoint-audit.md) | 477 / 17007 | 2d43aa69d79bde9a3aeac00ff4c9ee79696640f816df28eba051011ab255b25d |
| [482 不同作者 peer](hybrid-original-conditional-perron-remainder-review-peer.md) | 280 / 14200 | 245f4c0c89a8034224e9a031a3087796752a9f47361c367fda47ebb3c1e37784 |
| [原 short-μ 全证明](hybrid-short-mobius-twist-and-vaughan-zero-residue-research-radial.md) | 113 / 6064 | a970366e68b8d3526c0dadac49b8ee8f4a7b6984e763712a851f8b6d353a291d |
| [481 完整 squarefull tail source](hybrid-original-type-ii-large-single-prime-part-research-checkpoint-audit.md) | 401 / 15353 | 66c35eb3ed43cec836ff1d10ed01322f115684c44b771d3db7364637994c3cab |
| [479 Weyl、最大 prefix 与疏项](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | 524 / 21261 | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 |
| [477 原 Vaughan 恒等式与二矩](hybrid-original-vaughan-type-i-and-type-ii-reduction-research-radial.md) | 324 / 12260 | cf58086aeb9eee63832ccd06f5499110ea236b4bd94396893757b62e75bdb9d4 |
| [原 scalar 与 proper-power 迁移](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | 370 / 14699 | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |

451 和 476 在这里作为明确引用的条件输入消费；本轮没有重新认证其所有上游论文、
Hecke 输入包或外部密度定理。也未把 484 链接的正式论文另认作本轮全文认证范围。

## 2. 对数导数的 pole regularization、盘与量词

设 1/2≤θ<1，普通 ζ 在整个 Re(s)>θ 无零。先固定
0<δ<(1−θ)/4，α=θ−1/2+δ，则 0<α<1/2。
不能在包含 s=1 的整个右半平面声称 Dζ=−ζ′/ζ 有统一有界或 subpower 上界；
其主极点的 residue 为 +1。正确合同是
\[
 D_\zeta(s)=\frac1{s-1}+D_{\rm reg}(s),\qquad
 |D_{\rm reg}(\sigma+ih)|\ll_{\theta,\delta}\log(2+|h|),
 \quad \sigma\ge\theta+\delta.
\]

独立核对：大 |h| 时，中心 2+ih、外半径 2−θ−δ/4 的盘严格处于无零域且不含 pole 1。
中心 Euler logarithm 为 O(1)，在这个单连通盘上可选解析 logζ。
固定带的 polynomial height growth 给 Re logζ=O(log(2+|h|))。
BC 内半径 2−θ−δ/2 给 |logζ|=Oθ,δ(log(2+|h|))。
对 θ+δ≤σ≤2，中心 σ+ih、半径 δ/4 的 Cauchy 小圈完全位于内盘：
其最远距离至多 2−θ−3δ/4，严格小于内半径。
因此 ζ′/ζ 的显示 log 界成立。σ≥2 用绝对收敛 Euler series。
低高度的固定 compact 带在减去 1/(s−1) 后解析无极点；再与右侧 Euler 合并。
这里没有把 reciprocal 的 subpower 费用误写成纯 polylog，也没有免费引入 Hecke 导子族。

所有 θ、δ、guard 常数和最终损失先于 T 固定。
最终任意 ε 可选择更小的固定 δ、ρ、η，再令 T 增大；
没有 δ=1/logT 或未证明的随 T 移动常数。

## 3. 内部无限 Perron：半整数、无限尾、pole 与水平线

对全部实数 N≤X、τ∈[c0T,C0T]，N≥2 时取
x=floor(N)+1/2，c_N=1/2+1/logx，H_in=T²。
初始 ζ 参数实部为 1+1/logx，故 Dζ 的无限 Dirichlet series 绝对收敛。
截断误差的完整 majorant 是
\[
 \sum_{n\ge2}\Lambda(n)n^{-1/2}(x/n)^{c_N}
 \min\{1,(T^2|\log(x/n)|)^{-1}\}.
\]
它包含所有 n>x，不能只对原 n≤N 的有限和估计误差。

远端 n≤x/2 或 n≥2x 的对数距离有固定正下界。
令 η=1/logx，用 x^η=e 与
Σ logn/n^(1+η)≪1+η^(-2)，得到 O(√x T^(-2)log²(2x))。
近端 x/2<n<2x 有 Λ(n)≤log(2x)、|log(x/n)|≳|n−x|/x。
每个整数到 x 的距离至少 1/2，全部距离的 harmonic sum 为 O(log(2x))，
给相同费用。最近整数已支付，没有 half weight 或端点残项。

移到 Re(w)=α 后，ζ 参数实部至少 θ+δ，故无零点极点；
w=0 留在矩形左侧。唯一跨过的 pole 是 w=1/2+iτ，
其 residue 必须明确保留：
\[
 \frac{x^{1/2+i\tau}}{1/2+i\tau},\qquad
 \left|\frac{x^{1/2+i\tau}}{1/2+i\tau}\right|\ll_{c0}\sqrt N/T.
\]
α<1/2<c_N 且 C0T<T²，保证 pole 严格在内部。

左线 ζ 参数实部 θ+δ<1，到 pole 1 有固定距离 1−θ−δ>0，
包括真实 ζ 高度为零的点。Dζ=Oθ,δ(logT)，
∫|α+iω|^(-1)dω=Oδ(logT)，故左线为 O(N^αlog²T)。
两条水平线真实高度 ±T²−τ 的模至少 T²/2；
|w|≳T²，且
\[
 \int_\alpha^{c_N}x^\sigma d\sigma
 =\frac{x^{c_N}-x^\alpha}{\log x}\ll\sqrt x.
\]
得到 O(√N T^(-2)logT)。这是真正 log-derivative 费用；
μ reciprocal 的 O(√W T^(-2+ρ)) 仍按其独立合同支付。

因此 source (9)–(10) 的公式和全部 guard 均成立。
N<2 的 Q_N=0 直接支付；若仍按显示主项公式解释，其 O(T^(-1)) 主项被显示误差吸收，
不会影响全 prefix 合同。内部 T² 覆盖所有 N≤X；它不是外层产品 Perron 的高度。

## 4. 实际 +c、全 prefix Abel 与 genuine prime mask

外层 c=1/logX 与内部 c_N 不同。对 κ∈[0,c]，
\[
 Q_{N,\kappa}=N^{-\kappa}Q_N+
 \kappa\int_1^N Q_u u^{-\kappa-1}du.
\]
源已对每个真实 u≤N 证明 prefix 界，u^α、√u 和日志 error envelopes 皆单调。
正权质量 N^(-κ)+κ∫_1^N u^(-κ−1)du=1，因此相同上界保留。
这允许 c 随 X 取 1/logX，因为 Abel 上界统一于整个 κ 区间；
没有额外依赖 c 的未知常数。

prime mask 由真正 proper powers 的差得到：
j=2 的绝对和≤Σ_(n≤√N)logn/n≪log²(2N)，
j≥3 的完整 Σ_p logp Σ_(j≥3)p^(-j/2) 收敛。
这些费用统一于 κ≥0 和 τ，可被 N^αT^ρ 吸收。
任意 B<A 的带是 A、B 两个原 prefix 之差，因此 source (13) 对 q=1 或 1_prime 成立。
这不能扩大成任意 response mask；也没有从复杂带符号全 Λ norm 推出其任意子集 norm。

原 μ source 的 reciprocal BC/三圆证明在固定 buffer 下给 subpower，
内部实际高度为 O(T²)，故 reciprocal 自身的 exponent 须先选得更小。
482 已重证其全 guard 及实际 +c 的 Abel 合同；这里合法消费
|G_V|≪V^αX^ρ，v<1/4。Weyl proof 只依赖固定 c0≤τ/T≤C0，
故同样覆盖 [T/8,33T/8]，没有换成 t≈0 的相干峰。

## 5. 外层有限 product Perron 与真实短项二矩

source 的一般域
0<v<a、v<1/4、max(1/2,a+v)<y<1 保证 AV<Y<X。
展开 b_V 后，原 k>V 被 Y<mk 与 m≤A 强制，仍保留共同乘积 sharp mask。
F_(B,A,q)、G_V、W_floorX 都是有限多项式，乘积长度 Z=AV floorX<X²；
全部 n>X 的矩形系数必须保留到误差估计结束。

外层高度 T/8、实部 c=1/logX，用两个半整数端点恢复 Y<mk≤X。
归一实际矩形系数≤Cφτ3(n)/√n，冻结有限 Perron 的完整截断误差为
\[
 O_{\phi,\eta}\!\left(
 X^{2\eta}\{\sqrt Z/T+\sqrt X\,T^{-1}\log(2X)\}\right).
\]
远端包括全部 n>X，近端包含最邻近两个端点；
a+v<1 是固定余量，可在最终 ε 前选 η 使费用为真负幂。

当 t∈[T/4,4T]、|ω|≤T/8，τ=t−ω∈[T/8,33T/8]。
只在恢复共同 mask 后，才用同一 τ 的 Λ prefix、μ prefix 和 Weyl 上界：
主 sup 为 X^(1/6)(AV)^α X^(2ρ)log^C X。
Λ pole 的额外 product 指数为
1/6+a/2−1+vα+ρ<−1/3+ρ，内部 Λ 尾更小。
没有把 pole 删除或对已取绝对值的 error 再认领 μ 相消。

实际短函数只支持 n≤X，其系数仍≤Cφτ3(n)/√n。
对它自己的真实二矩用原有限均值合同给 ||S||²_(2,T)≪X^ε；
不能用长度 Z 的矩形二矩替代此步骤。
sup²×真实二矩，并预先支付 2δ(a+v)、4ρ、divisor 与日志损失，严格得到
\[
 \mathcal M_{S_{B,A,q}}\ll
 X^{1/3+(2\theta-1)(a+v)+\epsilon}.
\]
该估计对全部列明 B 和两个 q masks 统一。

## 6. H=V² 完整费用族与分界

被冻结的 low、Type I、large proper powers 和完整 r>H tail
分别为 2y−1、1/3+2v、1−2a、1−4v；
479 的实际最大 prefix proof 与 481 的 tail 系数证明保留所有 sharp endpoints。
本稿没有再次免费提高 Type I 的 μ 费用。
完整合成成本
\[
 C=\max\{2y-1,1/3+2v,1/3+(2\theta-1)(a+v),1-2a,1-4v,0\}.
\]
由 a≥(1−C)/2、v≥(1−C)/4，
Type I 给 C≥5/9，β=2θ−1≥0 的 short 给
C≥(4+9β)/(12+9β)=(18θ−5)/(18θ+3)。

θ≤5/6 的 (v,a,y)=(1/9,2/9,7/9) 达到 5/9；
short 为 2θ/3≤5/9。θ≥5/6，D=18θ+3 的
(v,a,y)=(2/D,4/D,(18θ−1)/D) 使 low、short、proper、tail 同为 (18θ−5)/D。
Type I=(6θ+5)/D，差 (12θ−10)/D≥0。
全部一般域严格成立，两分支在 θ=5/6 接合。
所以 source (20) 是所列 H=V² 费用族的精确最优值；不证明所有分区或方法的最优性。

H=V² 保证 pure-squarefull k=r≤H 时 rad(k)≤V，原 b_V(k)=0。
非零 core 仍有 s(k)≥2 及 s(k)rad(r(k))>V。
主参数 a=2v 给精确整数 V²≤floorX^(2v)=A；
m>A 为 prime 时 (m,r)=1，不能另加 (m,s)=1。
改变 H、b_V 或 Y 会改变实际函数，不能当成旧余项的免费子族。

## 7. 条件 43/75、完整传递与固定 482 的真实带

θ=7/8 时 (v,a,y)=(8/75,16/75,59/75)，五项费用精确为
(43/75,41/75,43/75,43/75,43/75)。
按 short m、large proper powers、large prime m 的 r>H tail 的不交有限分区，
剩余正是 source (23)：m>A 为真实素数、k>V、r(k)≤H、Y<mk≤X，
保留 Λ(m)b_V(k)、负号与原 normalizer。
原 scalar proper-power 范数差另由冻结合同支付。

有限次 L4 Minkowski 先合成 E，得到真实恒等式 P_H=R+E 和
M_E≪X^(43/75+ε)。476 给 M_PH≪X^(5/7+ε)，
R=P_H−E 先取得相同完整范数增长，然后才施 Hölder 差：
\[
 |\mathcal M_{P_H}-\mathcal M_R|
 \ll\|E\|_4(\|P_H\|_4+\|R\|_4)^3,\qquad
 \frac{3(5/7)+43/75}{4}=\frac{713}{1050}.
\]
独立 Fraction 复核了
5/7−713/1050=37/1050、
49/81−43/75=64/2025、
779/1134−713/1050=16/2025、
13/21−43/75=8/175、
29/42−713/1050=2/175。
这是 additive 增长误差；不要求未知主项有同阶 lower，
也不能据此声称相对主项等价或常数级 o(1)。

保持 482 的 V=floorX^(8/81)、A0=floorX^(16/81)、H、Y=X^(65/81) 与 b_V，
取 A1=floorX^(64/243)。先对 A0<m≤A1 的全部 k、prime mask 直接付
\[
 1/3+(3/4)(64/243+8/81)=49/81.
\]
再对同一 m-band 的 r>H 重用 tail proof：添加此真实带后，
其 τ(r)τ3(n) 系数 majorant 仍成立，费用 1−4(8/81)=49/81。
两个完整函数相减才得到 r≤H 带的费用；没有使用子集 norm 单调性。
A1/A0≍X^(16/243)，a1>1/4 合法，因为 Λ prefix 已覆盖全部 N≤X，
而 μ 的 v=8/81 仍<1/4。旧对象新的 remainder R1 仍付 49/81、传递 779/1134。
新主参数 R_(Λμ) 与旧 R1 不是相同函数或自动包含的子族。

## 8. whole、balanced core 与零点留数的界限

把一点 Λ prime prefix 直接用于全 P_H，sup²×二矩只给 2θ−1；
θ=7/8 时 3/4>5/7。476 的域内其差
(1−θ)(4θ−3)/(2θ)>0，故不能称 whole 改进。

若本三因子消费要求 a≥1/2 且 tail 费用≤5/7，则 v≥1/14，
short≥1/3+(3/4)(1/2+1/14)=16/21>5/7；
新 v=8/75、a=1/2 的费用为 473/600>5/7。
这些是当前 upper 费用法的障碍，并非实际带符号 balanced 子族的 norm 下界，
也不是任何可能 joint estimate 的不可能性定理。
a+v≥y 时原 k>V 不再自动，必须另付其真实 mask。

完整 C4 的生成函数仍为 (Dζ−F_U)(1−ζG_V)。
ζ 零点 ρ 处有限 F、G 全纯且 1−ζ(ρ)G_V(ρ)=1，
实际 residue −mρ 未消失。
内部 Dζ Perron 用 ζ 参数实部≥θ+δ 的无零域；
外部 F·G·W 的有限产品在实际 Re(s)=1/2+1/logX 上全纯，
这是两种不同理由，不能混称为同一次无零移线。
ordinary 一点 prefix 不供应 primitive-character、加性 phase 或原完整 joint mixed4 常数预算。

## 9. 484 最终笔记的完整一致性

484 §1 的 pole、内部 T²、外部 T/8、guard、Abel/prime mask、
实际短项二矩与 source 一致；§2 的成本族、5/6 分界、整数参数、
真实剩余和 713/1050 传递一致。
§4 保持 482 的同一个对象，以 full band−tail 迁移 r≤H，未误用 subset norm。
§5 明确检查脚本的有限范围，没有把身份、有理运算的 PASS 当成无限分析认证。

本审查 FULL READ 的最终 194 行笔记只记录已给出的条件证明和应用；
新 script/output 的实际运行结果应由其独立执行审查绑定，
本文不会在尚未读取或运行它们时认领其执行结果。

## 10. 451 已有边界的合法新应用与精确包围

451 的相对命题依赖其明确的 445 原 [R] 输入包、whole finite-order Hecke 7/8 bootstrap
及 450 重证的 lower-κ moment，然后完成 ordinary ζ transfer。
不能把这些假设缩减成普通 ζ 的单条 [R7/8] 就宣布 σ*。
在保留 451 完整依赖、接受其普通 ζ 输出后，
它恰好供应这里的 [Rθ]，θ=σ*=11/12−e*/4。
本轮只消费既有输出；不重新认证 451 全上游，也不证明新的 boundary。

451 的有理区间
\[
 e_l=16683858898627/10^{14}<e_*<
 e_u=16683858898628/10^{14}
\]
在 p(e)=657e³−954e²+21e+20 上有精确 p(e_l)>0、p(e_u)<0。
在 (1/6,167/1000) 内，
p′(e)≤1971(167/1000)²−1908(1/6)+21
=−242030781/1000000<0，故指定根唯一。
由反向线性映射严格得到
\[
 \frac{262487105826029}{300000000000000}
 <\theta_*<
 \frac{1049948423304119}{1200000000000000},
 \qquad 5/6<\theta_*<7/8.
\]
所以这里费用族的高分支与 476 整个域都适用；θ* 先于 T 固定，
没有移动参数常数或暗中改善 zero-free 前件。

精确新参数与费用是
\[
 c_*=\frac{23-9e_*}{39-9e_*},\quad
 v_*=\frac4{39-9e_*},\quad a_*=2v_*,
 \quad y_*=\frac{31-9e_*}{39-9e_*}.
\]
组合 476 的完整
\[
 B_I(\theta)=4\theta-3+\frac{3(1-\theta)}{2\theta},\qquad
 \gamma_*=\frac{3B_I(\theta_*)+c_*}{4}.
\]
c′(θ)=144/(18θ+3)²>0，B′_I(θ)=4−3/(2θ²)>0 于该域，
故 γ 也单调。标准库 Fraction 独立端点计算给
\[
 \frac{537461317478087}{937461317478087}<c_*<
 \frac{2149845269912357}{3749845269912357}.
\]
其十进制端点约为 .5733157277613751433988475… 与
.5733157277613761674833560…。
γ 的端点约为 .6789774341551112591249302… 与
.6789774341551153413157565…。
它们严格位于 484 所列的有理十进制外包围：
\[
 .5733157277613751<c_*<.5733157277613762,\qquad
 .6789774341551112<\gamma_*<.6789774341551154.
\]
B_I 的严格端点约为 .7141980029530232977002911… 与
.7141980029530283992598900…；Fraction 已核 c 的上端小于 B_I 的下端。
因此 R*=P_H−E* 可先继承 B_I，随后合法得到
\[
 \mathcal M_{E_*}\ll X^{c_*+\epsilon},\qquad
 \mathcal M_{P_H}=\mathcal M_{R_*}
                 +O(X^{\gamma_*+\epsilon}).
\]
所有最终 ε 仍须先分配固定 buffer 和各范数损失。
这仅是既有 451 无零边界在新完整误差族的消费，
既不产生新边界，也不改变 whole 输入、已知比例或中心四阶常数。

最终限定 PASS 只绑定上述 source、484 和明确引用范围。
未发现剩余实质缺口；内部/外部 Perron 的措辞区分已由作者限定勘误处理。

