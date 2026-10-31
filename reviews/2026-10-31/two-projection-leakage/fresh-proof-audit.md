# C066双cutoff泄漏：不同组织数学逆审

2026-10-31；`/root/two_cutoff_fresh_proof`。**限定PASS，无阻断性修正。** 支持固定Π_X→Π_(X²)的交叉泄漏下界、共同正scalar及下述cofinal正混合范围；不支持一般输出尺度、经典正性或长期Goal完成。

## 本次实际版本与阅读

恢复README/实际STATE，运行check后show结构通过，读原Goal完成门、C066、BB/前沿当前段。全文读6278byte域准入与6563byte相位准入，并审核两份已定稿证明：

| 原件 | bytes | raw SHA256 |
|---|---:|---|
| root-proof.md | 7777 | `bbb0fab2866b0348b078c355f992fb1a00b3899e7b0f927e65e59ac7fc54ab40` |
| full-proof.md | 12601 | `656378888d3e19ee8fc9b6ed09eb52607375f9c112d5d90a8189d69baffbf519` |

实读旧585全文、589主定理/归一化段，C052 `source-localization-proof-audit.md` §§1–6及root消费记录相关范围，560对象/全型、591对象和三测试必要段。原VK/Burnol/Hardy支链依旧root已消费范围调用；没有重审全部嵌套原证明，没有新web/primary/作者后章/数值。只读子任务`tail_readonly_check`另核root §§1–3及585 §§2–3，报告统一tail PASS、无文件修改；本稿已独立核相同预算并消费其终态复核。

父任务负责运行时、结算与远端；本稿不凭状态文件独立认证父Goal/API或发布。哈希只绑定审核版本，不代数学证明。两原件字节保持，不修改其历史执行措辞。

## 对象与严格HS域

源仍原physical complex r=e^(u/2)bare，receiver测度dt/(2π)，A_r在Mellin侧为M_(rhat)，不是M_r。Π_Z使用全部finite Euler/Gram逆/returns。560已付A_rΠ_X∈S₂，故左乘I−Π_(X²)或Π_(X²)的feature都在S₂；mixed用HS×HS严格定义，给

    E_X=t_X−C_X，0≤E_X(r)≤t_X(r).

未将Π_Z或未夹源乘积升级成S₁。逐层E一般不source-stationary，不先称W_X正分布；各层PSD若全compact源趋Q即可传正，故不应额外强加逐层消noncompact Pan。本稿也未构造几何principal/Green functor。

## 先核相位及actual输出kernel

令ell=logX、a_Z=sqrtZ/logZ。对于固定ε≤.01的S_X={h_X≤−1+ε}，写v=(1−2it)^−1 e^(−it ell)=x+iy，得|t|≤sqrtε、|y|≤sqrt(2ε)。相位倍增准确给

    h_(X²)=x²−y²+4txy
            ≥1−4ε+2ε²−4sqrt(2)ε≥1−10ε≥.9.

另一方面|t|≤π/(2ell)时h_X≥0，故S_X避开此小区间。两个相位方向、常数和下界符号均正确。

旧C052 §§5–6实际提供whole weighted Q_Y≤exp[(-4+o(1))a_Y]，uniform |t|≤(logY)^B；这个比仅fixed-away-zero的k界更强的前件已在旧root消费中闭合。证明正确再乘**actual** w_Y，得到S_X上k_Y≤exp(−7a_Y)。S_X始终位于固定小区间，故可消费uniform界，不是令δ移动或用固定Y强极限替换对角线Y=X²。

正投影的cutoff trace身份给||Π_Y1_S||²_HS=∫S k_Ydt/(2π)，因此operator norm也指数小；这里的HS资格由有限的local integral支付，不是整个Π_Y trace class。没有漏乘或重复除2π。

## 再核整个增长维trial与频率全尾

真实trial为D_XpH₀，全部有限多项式倍H₀同属原arch Sonin域。H₀在J_X有固定正lower，故Legendre pointwise账本中的∫J|p|²换成I_p=∫J|pH₀|²只改固定常数。J_X权为exp[(4−o(1))a_X]，且J_X最终在S_X。

在S_X补集且|t|≤X²，权损失为固定4εa_X。取n=floor(c_ε a_X/ell)，则C n log(n+ell)≤C c_ε a_X；先固定c_ε足小，再令X大，保留指数小余量。这个估计统一所有complex系数，并非只选择一个好向量。

|t|>X²另用全线Euler upper，未外推finite-height渐近。置u=sqrt|t|≥X，n logu/u≤n logX/X→0，n logell和log(n²ell²)均o(X)。所有poly因子、Jacobian及两端积分被Gevrey指数吸收；再除J_X denominator后仍为exp(−cX)，强于所需exp(−c_εa_X)。因此whole n维trial单位球的off-S质量界成立，原范数始终dt/(2π)，未偷换辅助Gaussian measure。

## 到原源与真实输出的运输

每fixed非零compact源的rhat整个且不恒零，k=ord₀ rhat有限。先取其local Taylor lower，再选固定ε使S_X位于该小邻域；这是证明中trial依r选取，不是把同一E_X规则改成逐源规则。由|t|>π/(2ell)，输入乘rhat后的范数平方至少c_r ell^(−2k)。全线|rhat|≤||r||₁允许把输出分成S_X与补集；前者用actual cutoff-HS，后者用trial指数小尾，得到输出捕获指数小。

故每个unit trial向量都有泄漏≥c_r ell^(−2k)。在真实RanΠ_X内取ON基、对有限正项求和，支付

    E_X(r)≥c_r sqrtX/(logX)^(2k+2)→∞.

量词为每个先fixed complex Cc∞源，常数和起点可依r；不是全源unitball、moving r或growing-I统一下界。该证明仅控制这一实际增长维trial的capture，没有声称整个C_X/t_X→0。旧t_X lower本身不能相减未知C_X；新相位集中/交叉capture填补的正是这一步。

## 校准与混合的准确范围

新k=0 lower给E_X(r₀)≥c s_X；E_X≤t_X及旧589给E_X(r₀)=O(s_X)、每fixed mean-zero z的E_X(z)=o(s_X)。同一PSD Cauchy链于是对全部fixed complex源对给

    E_X(r,s)/E_X(r₀)→(∫r/h₀)overline(∫s/h₀).

此方法和537的q₀/q₁是强旧，只有新crosslower使它适用于本双投影族；不另计功。任何共同positive scalar若校准r₀，就使r₀′极限0，与完整q₁>0矛盾。mean-zero不是pole-free，odd负pole没有删除。

full-proof第7节明确的support逃逸共同正权混合闭合。root第5节更一般的概率质量cofinal逃逸版本也成立：取X≥X₀使分母全正，F_X=E_X/E_X(r₀)。有限X区间内只有有限个prime和sqrt-prime事件，故F_X对每fixed pair locally bounded；其最终uniform接近均值极限，因而全区间bounded。ν_j([X₀,M])→0加总质量1，即给∫F_X dν_j的相同极限。未归一正权先按r₀能量质量归一、总r₀能量趋q₀且归一质量逃逸时同理。允许共同权依非局部资料或整组测试选择；不覆盖逐源不同权、非cofinal残留、负权或其它输出尺度。

## 经典身份、强旧与最终裁决

560的Q_W=t_X−K_X+Pole在fixed源的全部可见primepowers已包含后准确保留，故Q_W−E_X=C_X−K_X+Pole。actual Γ=2θ′/FP-contact、所有proper powers和双pole都仍在目标；本证明没有获得有利有限部符号或独立Q正性。

Y=X恰是591的common occupation；本不同输出没有其|k_R|²逐点非负核前件。594的prime-linear word类、596单prime增量和固定Y强极限也未支付上述同时成长capture。新的实际反配比较因此有不同的完整候选裁决，不是仅改norm/source标签或重算旧ratio1。

支持root按C066统一结算一个完整数学责任，不能把完整新失败证明藏成source0，也不能按原件、代理或审稿多计。仅固定Π_X→Π_(X²)规则及上述共同正修复被拒；一般Y(X)、source-adaptive、高阶relative/signed等仍未排。未证D′收敛，未改whole leading4/5负惯性UPPER或关键principal/sections/mixed/corecross/成长Ξ；原三个Goal门open。最终root消费和唯一cadence更新仍由root完成。
