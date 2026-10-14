# 554. Theta joint正跳：合法对象、适应修复与准确未付符号

2026-10-14；来源消费0轮。完整原推导在
[来源原稿](../reviews/2026-10-14/theta-joint-source/positive-jump-calibration-and-domain-gate.md)，
[最强旧范围](../reviews/2026-10-14/theta-joint-source/strong-old-and-next-admission.md)。
本页是root前件闭合记录，不把来源恒等式升级独立正性。

## 对象与实际消费

405实际Gaussian关系给正even g=e^(u/2)Eη、Q(g,r)=0、A±(g)=1/4；
g属于I/T-radical，不能把它当双pole零的P_an。真正principal是p_c=(D²−1/4)g。
Γ=2θ′、Fourier因子1/(2π)、完整pp Λ(p^k)=logp、signed双pole均保持。
ALL complex compact r=gf，原norm为∫g²|f|²，不是另一个μ范数。

完整恒等式为Q(gf)=E_g(f)−∫μ_g|f|²+2Re A+(gf)overline(A−(gf))，
μ_g=(1/2)cosh(u/2)g。E_g含actualΓ正跳及ALL pp正跳；
compact autocorrelation有限不允许删除E_g外窗degree尾。
概率π=8μ_g下，Q(gf)=E_g(f)−[Varπ(f)+|Eπ(tanh(u/2)f)|²]/8。
要求后项被E_g支配仍恰是原whole正性，独立gap没有支付。

## root核准的域、费用和逃逸

原single g的τ_a p_c/g在L²(μ_g) iff |a|<log2/2，端点也发散。
ALL a在自然L²(g²du)仍合法；不能从comparisonnorm失败排其自然源域。
单shift/scalar运输的平方费~exp(πe^(2L)−4L)/(8π²)只排这个族。

Gaussian infinite lattice正关系覆盖ALL fixed principal shifts；finite lattice和continuous cosh mixture
均是actual E-source，窗运输平方费O(e^L)。任一正G有finite A±时，该μ_G/originalL²费用
K²≥2L+2sinhL。因此允许窗口/源适应后sharp order为e^L，不能继承single-g巨费。
任意centered S_exp源r另有source-adaptive G_r≥m_g|r|，使r/G_r在comparisonnorm及完整E域合法。
这是依原source定义的非线性修复；不支付uniform范数、忠实quotient、Hodge或净符号。

root逐项核平方展开、pointwise ground equation、μ/自然norm方向、tail指数、endpoint、
actual scaling与全部Schwartz半范数、两个positive moments的必要下界。
global恒等式另用原稿§5/7的cutoff-control D_G≤C_G PG：Fatou先付E有限，再由μ积分控制cutoff误差，
不从compact公式直接升级全域。C_G依赖所选源，没有免费growth uniformity。

## 最强旧、净值和停止

405关系、543Γjump、016平方和529标准锥边界均是旧输入；553的global bounded闭包只限其原量词。
本来源付清的是表示/域/修复范围，主signed/core/Ξ瓶颈未变，0轮停止。
未排different Green/domain/allplace、source/window-adapted及fullsigned修复。
新C022仅消费另一条完整prime weightedrow费用；不静默改写本来源的unknowngap结论。
原稿raw版本及roothash绑定见本目录root-consumption-scope.json；语义变更必须重闭合。
