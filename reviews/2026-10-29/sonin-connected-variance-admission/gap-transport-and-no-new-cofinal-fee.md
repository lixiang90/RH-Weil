# 同对象gap transport：只搬费用，不制造统一界

2026-10-29；root补充具体比较，待不同fresh核。并非重开10-28 fixed-fullgap来源或调整其b/H₀预算。

设source support r⊂[−L,L]，原物理M_b为arch Sonin双gap logb，固定任意b>e^L。沿旧fullgap正确log字典，M_b=H_logb∩𝔉H_logb，且𝔉U_a=U_−a𝔉。A_r=∫r(a)U_a da只把两条support下界各降低至logb−L>0，因此

    A_r M_b⊂M_1。

这只是compact source的有限传播：在第二条高腿使用r(−a)，同样support[−L,L]；不是把M_b误写成U_logb M_1，也不删第二腿。r∈L¹使所有算子有界。

Actual finite Euler B_X与A_r均为同一平移群的乘子，彼此交换，故

    A_r(B_X M_b)⊂ B_X M_1。

令Π_1=Π_X,1、Π_b=Π_X,b，原同norm全Gram逆保证它们是真嵌套正交投影Π_b≤Π_1。于是

    (I−Π_1)A_rΠ_b=0，E=Π_1−Π_b为正交投影，
    δ_X(r)=(I−Π_1)A_r E，
    V_X[r]≤||A_r E||_S2²
          =Tr(A_r(Π_1−Π_b)A_r*)=:T_rel,X,b[r]。

这里||A_rE||_S2²≤||A_rΠ_1||_S2²已由560 source trace付有限性；只保合并的完整projection差，不把两个半线bounded block各自强行取迹。第一槽/receiver du与Fourierdt/(2π)由原酉对应保留。

**该式不付任何X-uniform上界。** 10-28 fullgap来源止门已明确缺cofinal relative费用，arch固定b的projector公式本身不提供它。该旧门的具体b≤b*与H₀范围不自动等于这里的b>e^L；当前只是同类型有限传播/投影支配，不以此宣布原停门被重开或其限定预算可续。所有fixed b的cofinal费用仍须独立实际估计。

对当前root fixed rτ，L=1，可在本逻辑比较里选一个先fixed b>e；这没有给T_rel,X,b[rτ]≤C_g，也没有其fixed-source极限，更未核完整C−K+indefinitepole。不要把V正/被另一个正量支配当作signed缺陷小。

因此本附加比较和HS恒等式一样只能按标准旧设施直接后果0保存。它说明现有上界链确切停在何处；不是新cofinal费用、strict方法类边界或RH否证。无新b/degree/源/primary后继预算。
