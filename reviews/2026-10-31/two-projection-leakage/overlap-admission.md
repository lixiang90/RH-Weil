# 两个真实cutoff的泄漏：相位反配准入门

2026-10-31；`/root/two_projection_overlap_admission`。同G20261027/runtime1793085111、原冻结0c4f。恢复README/实际STATE，check后show结构通过，读Goal完成门、BA/前沿及最新止点；未改状态、cadence、Goal或文献。本文是可执行新证明门的准入稿，不据此宣布数学结算或通过长期完成门。

## 对象及最强旧比较

唯一候选固定为

    E_X(r,s)=⟨(I−Π_(X²))A_rΠ_X,(I−Π_(X²))A_sΠ_X⟩HS，
    E_X(r)=t_X(r)−C_X(r)， C_X(r)=||Π_(X²)A_rΠ_X||HS².

Π_Z始终是560/585的全部p≤Z、完整Gram逆/returns的真实Sonin正交投影；A_r是原physical卷积源，在Mellin receiver上乘f_r=rhat。源r先fixed complex Cc∞，原du及zero-extension Dlog，不把receiver向量或weighted norm当源范数。560付A_rΠ_X∈S₂，左乘两个投影仍S₂，故0≤E_X≤t_X，mixed由同一HS特征严格定义。

Y=X就是591；591早已使用rhat，不是只处理physical乘子。不同输出Π_(X²)不能免费归入共同R的jump+killing核；594的selfadjoint prime-linear S₁ pencil也非本形式。固定Y后X趋∞或固定X后Y趋∞的结论，均不提供这条同时成长对角线。粗C_X≤min(t_X,t_(X²))无有利相减，因而旧585/589不能仅由迹上下界判断E_X。596单prime前驱增量另有moving源/相邻cutoff责任，并非这里的双cutoff overlap。

本形式逐层不保证source平移stationarity，故不先称其一个正分布W_X；若全部compact复源上E_X→Q_W，仍足以由独立PSD推出目标正性。无需逐层要求消405非compact Pan。本门不是几何principal/Green functor。

## 可以改变选择的新测试

检查输入Euler权热点与输出Euler权的相位反配。令

    ell=logX，A_X=sqrtX/ell，
    h_X(t)=Re[e^(−it ell)/(1−2it)]，
    S_X={t:h_X(t)≤−1+eps}，0<eps≤.01先fixed.

585已付logw_X=−4A_Xh_X+o(A_X)，uniform |t|≤X²。C052的必要原件`source-localization-proof-audit.md`§6(4)实际给出更强的whole weighted-evaluator upper

    Q_Y(t)≤exp[(-4+o(1))A_Y]，uniform |t|≤(logY)^B，
    k_Y(t,t)=w_Y(t)Q_Y(t)，relative dt/(2pi).

这里Q不是actual diagonal；必须再乘w。这个已付wholeQ界，不是把仅fixed-away-zero的结论升级到moving δ，也没有读未审sharp lower或作者后章。

在S_X上有一个自含、无PNT误差的相位事实。写a=(1−2it)^−1、z=e^(−it ell)、w=az=x+iy。x≤−1+eps且|w|≤1，得|t|≤sqrt(eps)、|y|≤sqrt(2eps)。因Y=X²，

    h_Y=Re(w²/a)=x²−y²+4txy
        ≥1−4eps+eps²−4sqrt(2)eps≥1−10eps.

所以S_X位于固定小区间；由输出的uniform Euler式和wholeQ界，最终

    sup_(t∈S_X) k_(X²)(t,t)≤exp(−7A_(X²)).             (A)

父/root独立得到同一相位方向；本稿也直接核算。并且|t|≤pi/(2ell)时cos(tell)、2t sin(tell)均非负，所以S_X上|t|>pi/(2ell)。

## 新证明责任应冻结在哪里

现有585的trial为D_X pH₀，全部有限多项式倍H₀同属实际arch Sonin域，H₀(0)非零且有Gevrey全尾；J_X=[pi/ell−ell^(−2),pi/ell+ell^(−2)]上的输入权为exp[(4−o(1))A_X]。旧Legendre账本为

    ||pH₀||²≤exp[C n log(n+ell)]∫_(J_X)|pH₀|².

需要在新合同中完整核闭的第一步，是将旧较粗频带集中细化为**相位集合S_X的整个增长维trial集中**：取n=floor(c_eps A_X/ell)，对deg p<n、按原dt/(2pi)归一的v=D_XpH₀证明

    ||1_(S_X^c)v||²≤exp(−c'_eps A_X).                 (B)

这不是已付585结论的字面引用。具体证明入口已可核验：在|t|≤X²而S_X外，w_X≤exp[(4−4eps+o(1))A_X]，相对J_X有固定4eps权gap；选择c_eps使Legendre全线费小于该gap。|t|>X²必须另外用全线w_X≤exp[(4+o(1))A_X]与Gevrey尾，不能外推有限高度prime渐近。后者吸收所有degree<n多项式后为exp(−cX)，这与585的原尾账本相同但须明确在(B)合并。所有complex系数同时成立，不可只选一条好向量。

第二步为真实crossprojection运输。由(A)，

    ||Π_(X²)1_(S_X)||op²≤||Π_(X²)1_(S_X)||HS²
       =∫_(S_X)k_(X²)(t,t)dt/(2pi)≤C_eps exp(−7A_(X²)).

若fixed非零源f_r在0的零阶为k，选eps≤delta_r²使局部Taylor lower有效。S_X上|f_r(t)|≥c_r ell^(−k)，并有全实线upper≤||r||₁。将乘f_r后的trial分为S_X与其补，(A)/(B)使输出投影norm指数小，而输入norm²至少c_r ell^(−2k)。在n维trial上求正交基和，目标为

    E_X(r)≥c_r sqrtX/(logX)^(2k+2)→∞.                 (C)

这是实际Y=X²相位反配导致的**同时成长crossprojection下界**。它没有被固定Y强极限、同R的591，或旧t_X下界本身支付；新责任是(B)及其到(A)的HS耦合。若(B)或该transport出现未付范围，保留conditional并停止，不将unknown overlap改名为输入。

## 条件净后果与准入建议

若(C)经完整证明和不同审查闭合，原始两cutoff规则在每个fixed非零compact复源上发散，不能趋有限Q_W(r)。这改变一个此前未排的实际PSD候选选择，但不改变经典正性瓶颈，也不是全部Y(X)或relative/higher/signed方法的边界。

更强的同次直接后果只需(C)的k=0：固定587非零均值bump r₀，E_X[r₀]≥c s_X，s_X=sqrtX/ell²。旧589及E_X≤t_X给所有mean-zero z的E_X[z]=o(s_X)。由PSD Cauchy，E_X(r,s)/E_X[r₀]趋(∫r/h₀)overline(∫s/h₀)。因此任何共同source-independent正scalar若匹配q₀，就杀r₀′而与537的q₁>0冲突。这个scalar后果扣清旧589，只归同次新crosslower；不另造轮次、不称完整D′收敛，也不外推逐源不同scalar或任意输出尺度。

建议：可以准入**一轮、固定Y=X²**的新证明责任，成功/失败均止于这项actual overlap门；不预授C066/603，不按本稿自计轮。输入是明确独立PSD规则和已付wholeQ/全trial资产；测试是(A)+(B)能否关闭(C)，净值是该新规则的完整fixed源失败及共同scalar范围，而非重验收旧591。若只保存本准入稿，不能声称(C)已root消费或新数学已结算。

实际读取：560定义/全型、585全文、587对象与trial比较段、589主结论及scope、591对象/三测试、594对象、596对象及quantified localization必要段；C052 localization proof-audit §§1–8。未web、下载、读新primary或运行数值；未重审所有嵌套证明。原Γ/contact、全部pp/双pole及原norm角色保持，whole4/5仍负惯性UPPER，原三个Goal门open。
