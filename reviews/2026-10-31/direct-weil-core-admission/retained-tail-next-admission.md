# 未用正尾的有限列供应：定义域通过，实际源值与whole余量未付

2026-10-31；`/root/whole_weil_core_admission`的新限定任务。上一稿7563bytes/SHA9065…原字节保持。当前pilot是roundoff-unresolved，未取得actual负方向；本稿不续其精度、同v或P0，也不建C067/604、不计数学轮。恢复当前STATE/check→show及C066/BC，重读595全型/正尾定义必要段；无新paper、code或数值。

## 1. 先把尾型与其operator分开

固定I=(-9/8,9/8)、H=L²(I,du;C)，J为零延拓、B=Fourier∘J，receiver测度dt/(2π)。令

    a(t)=1_(|t|>256)[AΓ(t)−7/2]≥0,
    t_tail(f,g)=∫a(t)(Bf)(t)overline((Bg)(t))dt/(2π).

其closed form domain为原Dlog；记相应positive selfadjoint operator为T。旧595给T≥tau I+U_old（型序），tau=δ/16、δ=2^-49158，U_old是已核81/27 rank-two。定义

    R=T−tau I−U_old≥0,
    D(R)=D(T), D(R^(1/2))=Dlog.

这里R通常unbounded，不能仅由e_j∈Dlog就写R e_j。

但原native正交Legendre基e_j，j=0,…,447，在I内是多项式、零延拓为compact BV。分部积分严格给

    |Be_j(t)|≤b_j/|t|,
    b_j=|e_j(-L)|+|e_j(L)|+||e_j'||₁<∞.

旧Γ增长a(t)=O(log(2+|t|))因此保证a Be_j∈L²。对任意form-domain g，有t_tail(e_j,g)=〈B*a Be_j,g〉，所以**e_j∈D(T)**且T e_j=B*a Be_j。这是额外的operator-domain论证，非把form domain当operator domain；Fourier逆只须L²意义，不能假设尾积分pointwise绝对收敛。bounded perturbation遂给e_j∈D(R)。

## 2. 有限列公式合法，但只是标准正型设施

令E:C^448→H为上述native isometry，固定eta=1，不改变N/L/Ω。于是

    V=R E:C^448→H,
    G_R=E*R E=E*V≥0,
    U_ret=V(G_R+I)^−1 V*≥0

均合法，V有有限HS范数。**G_R不是V*V，也不是旧G_M=E*M^-1E。** raw序列化Legendre坐标若用于计算，仍须原Gram的du congruence，不能裸用Euclidean norm。

对f∈Dlog、c∈C^448，

    q_R(f+Ec)+||c||²
      =q_R(f)+2Re〈f,Vc〉+〈c,(G_R+I)c〉≥0.

对c完成平方即得〈f,U_ret f〉≤q_R(f)。故0≤U_ret≤R是**型序**，并确实推出

    Q_W≥tau I+Llow+U_ret.                              (A)

U_ret是全H上的bounded finite-rank operator；其range不必在Dlog，这不影响(A)在原form domain上的消费。若改从T本身构造一个≤T的供应，就不能再免费加tau I+U_old；本式先扣R正是避免double count。

合法性也有原norm费用：

    ||V||²_HS≤3Σ_j∫a²|Be_j|²dt/(2π)
                 +3·448 tau²+3||U_old E||²_HS<∞.

这只证明fixed448列有限，不是small error、uniform growing-window或廉价计算保证。若以频率H_cut截断列，粗L²余量是O(b_j logH_cut/sqrtH_cut)；高阶常数及全部448列必须付款，不能把可积性当任意小误差已得。

## 3. 扣最强旧：连非零供应都不算新输入

这是标准positive-form shorting/Cauchy–Schwarz设施，与旧S v₀/v₁平方完成在机制上同类，不因加一个有限逆就产生新定理。更强旧常数还给：cΓ=123/1280、T≥cΓ(δI+S)、U_old≤cΓ S，因此

    R≥r_* I, r_*=(43/1280)δ>0,
    G_R≥r_* I,
    E*U_ret E=G_R(G_R+I)^−1G_R
             ≥r_*²/(1+r_*) I.

这个极小正floor也是旧尾证明的直接后果，不是新core margin；不能将“U_ret合法/非零/某head增加正量”验收为新whole净结果。

不过**实际源对象不同**：V_j=R e_j使用真实Γ-tail multiplier的operator列，G_R使用完整tail form。旧raw A/B/J0分别编码M、M²及Γ低带/双pole；旧tail-columns只编码S v₀/v₁，不给这些448个R e_j或full-tail Gram。它也不是595中同一M inverse的residual/W重新命名。因此存在具体未读取的信息差，而非改mu/N/theta或提高P0 precision。

## 4. 唯一可考虑的下一源门及其停止条件

可登记但**尚未执行**的单一门是：固定上述E448、eta1、L/Ω，形成一份retained-tail source packet，给native V_j的L²包含/余量、G_R的全矩阵包含和G_R=E*V的一致误差。所有数据必须来自同一实际a(t)、原normalization及tau/U_old扣项；不得用旧Sv₀/v₁或source中心代入R e_j。

包内最便宜的必要sign检查是新的native head

    C_ret=E*Llow E+G_R(G_R+I)^−1G_R.

若它有超过全部源误差的严格负方向，则相应bounded lower Llow+U_ret不能PSD；若只有小数正值/未决值或仅finite head PSD，仍没有whole正性。前一pilot未给actual负方向，不能借它预付此分支。源门的预算/误差应先固定；粗truncation费用若不能支付实际margin，就如实停在源门，不自动加精度/截断/基数。

whole证书还须支付新列的补空间作用。写P=EE*，已有Llow的blocks为C_old、F_old、D_old，D_old≥(m−n)I。令A=(G_R+I)^−1，则

    F_ret=F_old+(I−P)V A G_R,
    D_ret=D_old+(I−P)V A V*(I−P),
    S_ret=C_ret−F_ret* D_ret^−1 F_ret.

新独立量化输入必须是**原du下S_ret的有符号lower，余量覆盖V/G及旧source/cross全部误差**；不能只凭U_ret≥0或head增加量推出它。尤其不能把旧e/n/h直接当新U_ret的projection误差；需actual (I−P)V的norm包含/费用。G_R数值本身不包含这一whole coupling。

## 5. 裁决

**DOMAIN/FORMULA PASS；仅可作为不同actual retained-tail源门，不是数学合同准入。** 当前没有V/G新实际值、可消费的有符号head余量或whole S_ret margin。标准供应设施及其旧tiny floor均0数学；新数据若能在一个限定源门中产生充分证据，再由root按strongest-old净后果重新准入，不能把unknown Schur换名字。

原Γ/contact、所有pp、双pole均留在M/K和同一Q中；这不构造principal/整sections/mixed，不移除core/cross/成长Ξ瓶颈，不扩大固定窗或通过Goal门。一般directQ/retained-tail及其它relative/signed修复不被本稿否定，也未获预算。原稿、计数与共享状态不改。

本次只读子核`retained_form_domain_readonly`独立确认operator-domain和unbounded form shorting，已terminal、无文件修改；没有重审所有旧嵌套证明或运行source计算。
