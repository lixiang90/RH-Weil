# 465–466 原联合预算与交换子方差阻断：独立全文审查

2026-10-07。twisted_research。限定 PASS。
没有修改正文、冻结研究、math、脚本、输出或 Git。

## 1. 最终绑定

| 完整被审正文 | canonical LF SHA-256 | 原字节 / 行 |
| --- | --- | --- |
| [465](../../notes/465-centered-high-square-joint-fourth-budget.md) | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 | 10069 / 272 |
| [466](../../notes/466-high-square-variance-commutator-obstruction.md) | 0b955bdc26b4bf950ce457dec7bf18f635f702d85a73d73c8d6263df969cbbbe | 8013 / 243 |

hash只替换CRLF和lone CR为LF，不trim。
465五节、466五节都实读；不是仅检查作者摘要。
465初稿已经独立全文核验，最终scope delta新增实际不可达前件，
其重绑与完整有限预算审查见
[465独审](465-centered-square-joint-budget-review-twisted.md)。
本稿另从eigenbasis重推466全部不等式及原physical→finite准入。

## 2. 任意有限PSD W的证明

在H eigenbasis，q_diag为(λ_i²−W_ii)²的均值，q_off为W的offdiagonal
HS²/d。Γ_off=−W_off，所以q=q_diag+q_off精确。
PSD和W≤MI给W²≤MW，逐diagonal得到
r_i≤W_ii(M−W_ii)≤M²/4。

交换子范数的对称求和
Σ(λ_i−λ_j)²|W_ij|²≤4Σλ_i²r_i，因两项对换求和一致。
代入λ_i²=W_ii+Δ_i、W_ii≤M，并只对正Δ_i使用r_i≤M²/4，
得到4Mq_off+M²avgΔ^+。
avgΔ^+=(avg|Δ|+μ)/2，scalar Cauchy给

K≤4Mq_off+(M²/2)√q_diag+(M²μ)/2。

μ项是signed；原稿没有不必要取绝对值，且这个强式仍正确。
完成平方
−4Mz²+(M²/2)z=−4M(z−M/16)²+M³/64，
立即得到466(4)。Γ本身不必PSD，无H⁴ bounded前件，
也没有对不交换平方排序。

## 3. 原M与traceΓ

flat原taperφ²≤1、a_L→1，且每个high步长>L/2；
fixed u仅有一个方向可非零。未tapered同素数diagonal的uniform
Mertens partial summation上界为max_t t(t+1)/2=3/8。
所以可以选M_T=3/8+o(1)作为W的operator upper。
这是渐近upper，非每个T的exact sup；正文定义准确。

物理high二矩给d〈w〉+o(d)，actual二矩减去||QB_HE||HS²=o(d)，
TrW=d〈w〉精确。因此μ_T→0，没有使用high四矩。

## 4. Actual commutator的定义、符号和两次比较

466使用C_phys=[B_H,M_w]；其coefficient为原shift窗乘
w(u±log p)−w(u)。负prime prefactor保持在定义中，最终平方不受整体
符号影响。它与[H,W]的difference恰为

−E*B_HQM_wE+E*M_wQB_HE。

原raw m_H和bounded-multiplication leakage给此HS=o(√d)。
shift coefficient包含w差，但其sup和一二阶L1 derivative由w、φ的
uniform bounds封闭；故QC_physE的HS亦为o(√d)。
原外侧E与内部P始终保留。

454的weighted物理二矩首先证C_physE的HS=O(√d)，再使用上述小量
作squared-norm比较，误差才是o(d)。没有先假actual commutator bounded
而倒过来证明它，也不需whole high4 bounded。
全部finite carrier、same-sign Hilbert、endpoint remainder及
opposite-sign物理overlap alias原样保留。

## 5. Flat K常数与liminf量词

对正high shift x∈[1/2,1]，t∈[x−1/2,1/2]，
D(t)−D(x−t)=(x+1)(t−x/2)。两signs贡献相同，故

K1=(1/6)∫_(1/2)^1 x(x+1)²(1−x)³dx=41/10080。

本次Fraction多项式积分独立重算通过。这个是完成physical→finite
桥之后的actual交换子极限，不是restricted positive path子和。

把M_T→3/8、μ_T→0、K_T→41/10080带入严格finite(4)：
若liminfq有限，取达到liminf的bounded subsequence；若为无穷则结论
自动成立。得到33479/15482880，严格大于1/1600。
此量词不需要先假q bounded。

本次还独立按q_diag/q_off精确优化：
当q≥M²/256，最大有限右侧是4Mq+M³/64；
K1>M³/32，所以反解位于该段。与root完成平方界一致，
不存在遗漏的更小q分支。

## 6. 有理预算限制与465最终scope

Fraction核验：
q0=33479/15482880>1/500，
q0·19/240>(1/80)²，
23/960+1/80=7/192，
16q0·7/192>(17/500)²。
因此B1(q0)>747/2000>1/3，466(16)–(17)准确。

465的conditional代数与LP转移公式没有因此变错；
但其q≤1/1600反事实前件已被原flat结构排除，不能再称可追求目标。
正文header、§4、§5均已明确修订。
若仅以q上界代入该monotone scalar envelope，任何可达Q≥q0时都不能
认证超过flat二矩比例。不能把upper大于1/3当成实际fourth大于1/3，
也不能据此否定更准确joint covariance/commutator预算。

## 7. 最终新增§5：sharp线性式与最强实际下界

追加§5的每一步另作独立复核。Young平方对任意实Δ_i给
Δ_i r_i≤MΔ_i²/4+r_i²/M；原rowwise PSD的
r_i≤w_i(M−w_i)又给
w_i r_i+r_i²/M≤(2w_i−w_i²/M)r_i≤Mr_i。
代回有限对称求和K≤4avg(w_i+Δ_i)r_i，
准确得到K≤Mq_diag+4Mq_off≤4Mq，完全不需要μ=0。

2×2例W的eigenvalues为M、M−2ε，H²=(M−ε)I；
q_diag=0、q_off=ε²、K=4(M−ε)ε²，故通用常数4是sharp。
这仅证明所有finite matrices上的常数不可降，未把模型实现为原算术矩阵。
原K极限与M上界不变，所以最强实际结论为
liminfq_T≥41/15120>1/400，且41/15120<1/350。
第4节旧下界仍真，但不再是已付最强值。
候选Q1/400也已被排除；Q1/350仅尚未被该标量障碍排除，
其upper和任何actual high/low commutator lower均未因此付款。

本次最终绑定只追加上述已实读的完整有限证明及其actual推论，
原加权二矩、carrier、projection与全部analytical input未变。

## 8. 限定PASS的实质边界

PASS覆盖466的finite PSD、actual K准入、严格非零variance下界，
以及465最终的conditional有限预算和已排除前件说明。
没有新的零点比例、无零边界或RH证明。
剩余工作是保留原Γ、low平方残差、actual entire13和22负交换子项的
共同Gram约束，或直接付款原whole31/22的signed cancellation；
不能重新把重复词或physical ratio范数替成actual Γ。
