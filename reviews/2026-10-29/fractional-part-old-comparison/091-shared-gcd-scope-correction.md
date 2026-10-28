# 091 shared-gcd筛的前件纠正与消费冻结

2026-10-29；本次具体旧范围核读发现。原091–094文件保持历史原件；本附加记录覆盖下述宽句的当前消费。不是新研究合同或完整数学迭代，不补做Nyman未付dispersion。

## 实际反例

091§2前件为r=ga、r′=gb，g,a,b pairwise coprime squarefree，a,b>1，δ≠0，(δ,ab)=1。取

    g=2，a=3，b=5，δ=2，h=h′=1。

则bh−ah′=5−3=2，r=6、r′=10，(h,r)=(h′,r′)=1。全部原明示前件成立。取h_t=1+3t、h′_t=1+5t，在mod2中两个禁残基同为t=1，allowed t=0，故even-g并未全灭。Squarefree与primitive不排p|δ，原证明中的这一句没有依据。

Root实际执行现有scripts/qw_matrix.py的squarefree_shared_gcd_allowed_residues(2,3,5,2)，返回[0]；同g,a,b的δ=1负对照返回[]。helper本身按真实gcd枚举正确，无须改其算法。结果及输入另存helper-counterexample.json，不能把程序退出码当一般证明。

## 有限筛的正确局部范围

对每p|g，p∤ab，线性h_t、h′_t各有唯一禁残基。两残基相同，当且仅当p|δ：同零立即由方程给p|δ；反向若p|δ，则bh_t=ah′_t modp，任一为0迫另一为0。故定义κ_p(δ)=1（p|δ），否则2，有

    |T_g(δ)|=∏_(p|g)(p−κ_p(δ))，
    θ_g(δ)=|T_g(δ)|/g=∏_(p|g)(1−κ_p(δ)/p)。

Modp的非主Fourier系数为−p^-1倍**不同禁残基的集合和**，绝不能在重合时重复扣两次；其绝对值≤κ_p(δ)/p。CRT分解和对真实T_g的exact有限cotangent求和仍成立。这里仅重闭原有限筛的初等局部代数，不声称新的均值/dispersion估计。

因此原RT“两个不同/even-g全灭/∏(p−2)”与RV的原θ、两项Fourier句仅在(g,δ)=1成立；更准确even-g全灭恰要求2|g且δ为奇数。091 RS的coprime reduced kernel不使用shared-g条件，保持。RU若使用按(11)定义的真实T_g保持；若用错误count/empty分支替代T_g则冻结。

## 依赖范围与未重验部分

* 091 RT/RV/RY以及引言、RU之后的全部一般δ/even-g宽句当前冻结，须用上面的κ/真实T_g重闭。RX及092含一般δ的principal/nonprincipal分解不得继续消费错误θ；exact identity可以用真实T_g/其Fourier重写，未付bilinear输入依然未付。
* δ=±1时(g,δ)=1自动成立，所以091 shortest-stratum/RW、093 SK的本缺陷不触发；093 SJ如脱离其shortest使用环境作一般δ主张则冻结。
* 093 SL及094 SP涉及任意fixed 0<|δ|≤D；它们原证明写“θ(g)(g/φ(g))²≤1完全不变”，一般δ不成立。准确局部乘积为

      θ_g(δ)(g/φ(g))²
       =∏_(p|g,p∤δ) p(p−2)/(p−1)²
          ×∏_(p|(g,δ)) p/(p−1)
       ≤rad((g,δ))/φ(rad((g,δ)))。

  对fixed D，右侧有有限常数C_D=max_(1≤m≤D)rad(m)/φ(rad(m))。这修正了该**单个local-factor步骤**，不更改原\(\ll_D\)阶的可能性；本轮未重新审核其它row/dyadic/endpoint依赖，故不把此单步替换当SL/SP整定理已重新消费。任意growing D也未付uniform常数/净费用，不可再写完全无loss。
* 087实际Gram/affine Schur，088空间分块，089–090原有限divisor inclusion-exclusion，092不依RT的paired reciprocity/DFT，095–097的直接finite Gram/空间恒等式不因本局部纠正自动失败。它们各自未核的其余前件仍保原状态；不是整段旧资产失效。

当前固定h/B的旧去重只需081/082、405/553和421有限质量atom门，不依091错误θ，因此其“不是新Weil身份/关系下降”的结论不受影响。核心primitive/mixed/signedcross、whole4/5UPPER没有由此新增或改善；准确纠错也不作新经典后果。

下一先由不同fresh核具体反例、两种残基与下游范围，再由root追加消费，才能把冻结域的正确子分支当当前可用；不授δ/degree/conductor参数或新章节后继。
