# High平方残差的sharp线性交换子不等式

2026-10-07。twisted_research。新独立推导，待全文独审。
只新增本稿，不修改冻结研究、math、脚本、输出或 Git。
本稿证明任意有限PSD W的sharp系数4，进而加强原flat实际variance下界。
它不提供q的upper或新的零点比例。

## 1. 有限定义与已付款的原输入

对d维Hermitian H、0≤W≤MI，M>0，定义

Γ=H²−W，q=d⁻¹||Γ||HS²，
K=d⁻¹||[H,W]||HS²。

原high实例H、W与465/466相同，包含原interval carrier E、
internal P、even endpoint taper和genuine high primes，
不是physical ratio范数或别的数域角色。

前置：[465](../../notes/465-centered-high-square-joint-fourth-budget.md)，
[466](../../notes/466-high-square-variance-commutator-obstruction.md)、
[独立原交换子推导](hybrid-high-square-variance-commutator-obstruction.md)。
已付款实际输入为

0≤W≤M_T I，M_T=3/8+o(1)，
K_T→41/10080。                                         (1)

(1)依赖454的完整weighted二矩和finite projection比较，
不使用[R]或high4 bounded。其准入已逐步写在前置全文，
本稿不把只算physical积分当成actual K。

## 2. 保留rowwise PSD信息的更强估计

在H的正交eigenbasis，令H_ii=λ_i，
w_i=W_ii、Δ_i=λ_i²−w_i，
r_i=Σ_{j≠i}|W_ij|²。准确地，

q_diag=d⁻¹Σ_iΔ_i²，q_off=d⁻¹Σ_i r_i，
q=q_diag+q_off。

由W²≤MW，

0≤r_i≤w_i(M−w_i)。                                    (2)

交换子对称求和给

K≤4d⁻¹Σ_iλ_i²r_i=4d⁻¹Σ_i(w_i+Δ_i)r_i。              (3)

此时不能先粗化w_i≤M再舍去(2)的w_i依赖。
对任何实Δ_i，Young严格给

Δ_i r_i≤(M/4)Δ_i²+r_i²/M。

而(2)又给

w_i r_i+r_i²/M
 ≤[w_i+w_i(M−w_i)/M]r_i
 =[2w_i−w_i²/M]r_i
 ≤M r_i。                                               (4)

最后一步等价于(M−w_i)²≥0。
把两项代回(3)，得到强于单一q界的有限式

K≤M q_diag+4M q_off≤4M q。                             (5)

没有traceΓ小量前件；Δ可以有任意符号，Γ不必PSD。
未使用平方operator排序或任何未知增长估计。
M=0时W=0、K=0，退化情形也成立。

## 3. 常数4的通用sharpness

固定M>0、0<ε<M/2，取d=2，

W=[[M−ε, ε],[ε, M−ε]]，
H=diag(√(M−ε),−√(M−ε))。

W的eigenvalues为M、M−2ε，故0≤W≤MI。
H²=(M−ε)I，Γ仅有offdiagonal −ε。
准确有

q_diag=0，q=q_off=ε²，
K=4(M−ε)ε²。

因此K/(Mq)=4(1−ε/M)→4。对全部finite H、PSD W而言，
不能把(5)的4换成一个严格小于4的常数。
这是有限代数sharpness，未宣称原arithmetical H/W达到该模型。

## 4. 原flat对象的严格新下界

对原实际H_T、W_T，(1)与finite(5)直接给

liminf q_T≥(41/10080)/(4·3/8)
          =41/15120
          ≈0.002711640211640212。                      (6)

若liminf无穷，结论显然；否则在达到liminf的bounded subsequence
传极限即可。μ_T→0不再需要，但仍为原已付输入。

有理比较：
41/15120>1/400>1/1600，
而41/15120<1/350。
所以旧Q1/1600和新提出的Q1/400均不可能成为原flat residual的upper。
Q1/350在此不等式下没有被排除，但也未被证明。

## 5. 与联合预算的范围

465的finite joint envelope、其conditional LP蕴含本身仍成立。
新下界仅纠正可追求的q条件；它不把任意coarse upper超过1/3
变成实际fourth超过1/3，也不排除joint covariance/commutator改善。

例如新的centered Γ/low-square Gram若同时使用q upper和
actual ||[H,L]||HS²/d lower，其candidate必须首先满足(6)。
这两个actual量均仍需算术付款，不能以本2×2 sharp例或
physical repeated-label reference代替。

本稿新增结果只有finite sharp(5)和实际推论(6)，没有新比例或无零区域。
