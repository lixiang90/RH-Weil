# C006末轮：实位大移位子项的统一源质量费用

2026-10-14；主代理独立核推，未以此文件另计轮。起始HEAD44337d2。
目标仍是完整actual D_p的统一可求和预算；本文件只支付一个明确子项。

## 1. 与完整差额的关系

实际ρ_p的完整组织为

    ρp−ρ∞=−2r cos(as)ρ∞
        +Σ_(j≥1)r^j Mj−2cos(as)Σ_(j≥1)r^(j+1)Mj,
    r=q/(1+q²), q=p^-1/2, a=logp,
    Mj=<k_s,[P(Ua+U-a)P]^j k_s>.

这里裸q²mass已精确取消。定义同源大移位二次型

    J_a(g)=∫|ĝ(s)|²cos(as)ρ∞(s)ds.

固定有界源U、跨度W，a>W时，J_a在源L²上有有界压缩延拓；
下述核证明给||J_a||≤C_U e^(-3a/2)。
所以完整差额的第一个实际子项−2rJ_a具有uniform Cp^-2源L²费用。
这不等于完整D_p预算：两组Mj仍须合并后另付，不按各项粗Γ取范数。

## 2. 真实外部核及非振荡抵消

低cut L=(0,1)、实位K=LFL、R=(I−K²)^-1，J=R−I=KRK为smooth cosine-even核。
真实P=H−HFLRLFH。对ρ=e^a>1，source trace沿x≥1的scaling-diagonal，
除ρ=1的identity分布外，其核是−√ρ∫_1∞(FLRLF)(ρx,x)dx，
此式按有限x截断及合法source trace分布理解。

bare FLF贡献等于

    −√ρ Σ_± [π(ρ±1)]^-1 ∫_1∞sin(2π(ρ±1)x)/x dx.

由∫_1∞sin(kx)/x dx=π/2−Si(k)，且k≥cρ，一次端点积分给其绝对值≤Cρ^-3/2。
这已经是actualΓ与primaryδ的全部非振荡核取消之后的实际P核，
不是单独取Gamma、δ的ρ^-1/2部分。

## 3. smooth逆核的统一端点界

令J(t,u)为低逆修正核，所有有限阶Cm界已由fixed bounded R与cosine rows支付。
其cosine-even性使t=0的奇导数为0。对

    (FLJLF)(ρx,x)
      =4∫_0^1∫_0^1 cos(2πρxt)J(t,u)cos(2πxu)dtdu,

先对t分部积分，头项为sin(2πρx)/(2πρx)乘
f_0(x)=∫_0^1J(1,u)cos(2πxu)du。
f_0(x)=O(1/x)，且f'_0(x)=O(1/x)（再对u端点积分即可）。
因此f_0(x)/x及其导数均可积；随后对x的非驻相sin(2πρx)端点积分，
该头项的x积分为O(ρ^-2)。乘√ρ后得O(ρ^-3/2)。

再对t多积分若干次：每个endpoint1头项有(ρx)^-j、sin/cos(2πρx)，
其u余弦变换及所需x导数同样O(1/x)，再次x积分给更小费用。
endpoint0奇导数全部0。取至少三阶的深余项，直接绝对估计
∫_1∞(ρx)^-3 dx=O(ρ^-3)，乘√ρ也更小。
截断x端点的boundary趋0，故整个signed外部核得到

    |j(logρ)|≤C ρ^-3/2, ρ≥ρ0>1.

核反演对称由实位trace/scaling adjoint给j(−a)=conj j(a)；实际密度为实偶。
无需g的导数，不交换非绝对prolate系数，也不对发散ambient traces逐块相减。

## 4. 固定源L²压缩及仍未付项

在源U×U上，J_a的核为j(a+t−u)的实对称化（规范取真实scaling trace即可），
|t−u|≤W，故|kernel|≤C_U e^-3a/2。Schur给

    |J_a(g)|≤C_U e^-3a/2 ||g||²,
    |−2rJ_logp(g)|≤C_U p^-2 ||g||².

有限个a接近W的p由实际固定p源连续性另取常数；末素数rate只需p足够大。
与533的fixed smooth rapid估计相比，这是较弱p-rate但更强whole源L²拓扑。
未支付完整ΣMj及−2cos cross的统一尾，尤其不能把pointwise M2在s≫p的
log(s/p)增长删掉，或用Γ窗口误差过大来构造actual反例。
本子项不单独完成C006或长期Goal；消费须不同组织逆审核归一化/分布域及核估计。
