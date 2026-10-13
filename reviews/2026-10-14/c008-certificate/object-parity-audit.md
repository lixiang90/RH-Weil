# C008：固定v2的实际对象、复源奇偶及真正最低态审查

2026-10-14；起始HEAD `4377e70b35dfe1da6ce5957a31e8c9b0ba01824e`。
先恢复AGENTS/README/STATE/check/show、Goal与终态收据；起始STATE仍C007完成，
执行授权来自用户明确继续C008。随后重读主代理更新的C008运行合同及D20261014E。
不新建runtime Goal，不改STATE/cadence，不计独立轮，不运行外部代码或联系作者。

核读对象为只读原源包 `literature/background/zhu-2608.24827v2-src/main.tex`。
下述行号全部指该文件，不混用HTML/PDF页码。源包目录实见main.tex、四PNG及
00README.json；后者只登记TeX编译入口。未见论文2451–2462行声称的原证书附件。
这里给数学对象/域的独立推导；原数值声明仍为cited/open。

## 1. 完整Weil规范确与actual核一致

181–192行给实偶源的

    Q(f)=2F(i/2)²+(2π)^-1∫|F(t)|² Ψ_L(t)dt,
    F(t)=∫f(x)e^(itx)dx,
    Ψ_L(t)=Re ψ(1/4+it/2)−logπ
                −Σ_(log n<2L) 2Λ(n)n^-1/2 cos(t log n).

Γ项是本仓actual `2θ′`，没有旧half helper的因子缺失。Parseval为
`(2π)^-1∫|F|²=||f||²`，对应887行半线`π||f||²`也正确。
prime系数是两实偶原子合并后的2Λ/√n，包含全部prime powers；
L=0.8时e^(2L)=e^1.6介于4与5，故prime内容严格为2、3、4。
边界log n=2L被略去没有额外费用：两个L² compact-source相关在支持极端的值为0。
677–778行time-domain Γ推导的规范亦一致；本审查未核其全部数值quadrature。

### 与qw_matrix.py的精确basis/norm字典

记ℓ=2L=2logλ，中心窗I=[−ℓ/2,ℓ/2]。unitary log源norm为L²(I,dx)。
若取中心指数basis `e_n=ℓ^-1/2 exp(2πinx/ℓ)`，其pole矩阵不是literal w02，
而是 `(-1)^(n+m) w02(n,m,ℓ)`。本仓脚本38–57行及16058–16061行使用的
phase-adjusted basis是

    φ_n(x)=(-1)^n e_n(x)
          =ℓ^-1/2 exp[2πin(x+ℓ/2)/ℓ].

该basis正交归一。直接积分

    ∫e_n(x)e^(±x/2)dx
      =(-1)^n·2sinh(ℓ/4)/[√ℓ(1/2±i·2πn/ℓ)].

两个pole乘积合并给中心basis的相位×w02；吸收相位后正好得到脚本

    w02=32ℓ sinh²(ℓ/4)(ℓ²−16π²nm)
              /[(ℓ²+16π²n²)(ℓ²+16π²m²)].

φ_n、φ_m的双向相关为脚本q_nm：对n=m是
`2(1−t/ℓ)cos(2πnt/ℓ)`；n≠m为
`[sin(2πmt/ℓ)−sin(2πnt/ℓ)]/[π(n−m)]`。
所以原prime、pole及actualΓ合起来确为
`qw_entry=w02−w_real−w_primes`。两basis之间D_n=(-1)^n为unitary，
D_-n=D_n，保留复Hilbert谱及even/odd子空间次序。该字典不涉及改写代码。

## 2. complex pole及奇偶分裂：可独立核的正确后果

150行定义tilde f(x)=overline f(−x)。对一般complex f，正确entire身份为

    ĝ(z)=F(z) overline[F(overline z)].

因此完整pole应为

    P(f)=F(i/2)overline F(−i/2)+F(−i/2)overline F(i/2)
        =2Re[F(i/2)overline F(−i/2)].

置C=∫f cosh(x/2)dx、S=∫f sinh(x/2)dx，便有

    P(f)=2(|C|²−|S|²).                                (1)

它是完整complex源的rank-two indefinite Hermitian form；只在even子空间
降为rank-one正pole，odd子空间为rank-one负pole。
1123–1124行写ĝ(z)=F(z)F(−z)是在该proof先讨论real f的范围内成立，
不能把它搬到一般complex f；本文的complex结论可由(1)严格补足。

对complex f=f_e+f_o，C只取even部分，S只取odd部分。Γ/prime multiplier为even，
而cross `Re(overline F_e F_o)`为odd，积分为0，故
`Q(f)=Q(f_e)+Q(f_o)`。再取f=r+ih、r,h real，实源Fourier满足
F_r(−t)=overline F_r(t)，Re/Im multiplier cross为odd；(1)的pole也按实虚两部分分裂。
因此

    Q(f)=Q(Re f_e)+Q(Im f_e)+Q(Re f_o)+Q(Im f_o).

1112–1119行的pole反号、complex splitting量词正确，不是一个遗漏odd负pole的假推广。
若实偶与实奇各自下界证书成立，则1225–1227行的arbitrary complex下界确由四项相加得到，
不需要额外极化假设。1230行的`f⋆tilde f*`与150行定义不一致，疑多写一次involution；
按正确autocorrelation `f⋆tilde f`理解，不以这个notation错误否定(1)的数学推导。

## 3. full L²、closed form和算子ground域

258、1225行写for every L²源。actualΓ multiplier在大|t|为log(|t|/(2π))+o(1)，
因此不能把Q解释成full L²上处处有限的bounded operator。自然closed form域为

    D_L={f∈L²(I):∫_R log(2+|t|)|F(t)|²dt<∞}.

域外可定义Q=+∞，此时全L²下界仍有意义；谱/min–max在D_L上定义。
该点原文没有明确form-domain/selfadjoint-realization段落，属于必须补明的对象接口，
不反驳其one-sided下界。

可独立补足如下：选常数c使Γ+c≥1且与1+log(2+|t|)双向可比。
这个positive Fourier weighted form在支持闭子空间H_L上dense且closed；
有限prime-shift form及(1)的两个pole都是bounded selfadjoint扰动。
故Q为closed、半有界Hermitian form，有唯一相应Friedrichs selfadjoint算子A_L。
form-norm单位球的高频L²尾≤C/log(2+R)；低频restricted Fourier map
L²(I)→L²([−R,R])是HS（有限rectangle核）。低频紧性与该统一尾给
D_L→H_L的compact embedding，故A_L有compact resolvent。
其底一定实际attained，谱离散，有限multiplicity；这一性质不使用RH或缺失数值证书。

Γ不可能在full L²处处有限：固定χ∈Cc∞(I)，规范化modulation χe^(iRx)
的Γ能量随R为log R+O(1)，closed everywhere-defined form若有限会bounded，矛盾。
所以原L²措辞必须采用上面的extended-form读法。

1727–1729行以sine basis的L² completeness直接推Galerkin最低值收敛到真infimum，
这在unbounded form情形不是一般有效推论；还需form-core density。
可以另证log-weight form的适当core，但本文这两行没有支付它。
该缺口不影响任意finite source的variational upper bound，也不影响下面以严格min–max
隔离证明ground simple的路径；不把dimension stabilization当真ground证明。

## 4. simple even结论所需的证书链

1186–1199行的思路在数学上正确：对head矩阵M_even−s₂I，
任一codimension-one子空间上的PSD足以由Courant–Fischer给λ₂(M_even)≥s₂。
Householder frame不须orthonormal，但须精确full rank及误差不破坏PSD。
frame/matrix/rounding证书未取得，不能只凭inverse-iteration residual认证该步骤。

head到全R的第二min–max可用同一block-bound严格扩展：
tail下界d=β−ε_D，coupling≤ε_B，则

    λ₂(R)≥min(λ₂(head),d)−ε_B.

该式来自block-diagonal operator的第二min–max及bounded coupling的Weyl界。
因为Q≥R，λ₂(Q)≥λ₂(R)。1186–1199行只简写这个lift，但它确实可严格实现，
不是把有限head底排序冒充完整排序。

若1209–1215行所有数值区间及1186–1199行frame证书同时验收，则
λ₁_even≤2.523e−16 < λ₁_odd≥8.206e−15，且
λ₁_even<λ₂_even≥2.085e−12。结合§3的closed compact-resolvent realization，
真正full-window最低eigenvalue必在even sector，且multiplicity恰1；
real eigenspace单重与complexification后的complex单重一致。
这条推理有实质内容，不能仅因证书当前缺失而误说“simple本来推不出”。

但本轮未见2451–2462行所说的matrix、Cholesky factors、frame、试探vector、
run log、误差账本、SHA及verify_certificate.py，故全部数值条件只cited/open。
1166–1177行exact upper bound还需具体truncated vector及系数/degree/积分误差；
文中poly degree≤239不对应全200 modes到398阶，或许用了较短truncation，
不能在原vector缺失时自行补造。未发现该段明确承诺使用全head，不将此作为已证矛盾。

1099–1102行作者承认未做与CCM semilocal form的line-by-line normalization dictionary，
随后以positive rescaling不改变排序作说明。该说法只在相同Hilbert norm、相同unitary
源识别且form整体为正倍数时有效；different norm/仅hilbertian非unitary θ运输
会改变Rayleigh/min–max排序。本审查§1给本仓log-source的直接字典，
但不把原句当任意semilocal Hilbert对象的排序认证。

## 5. 净后果的严格范围及下一动作

若原complex-window下界证书最终验收，本仓原C007 V的两patch支持
`±a/2+(−b,b)`外端为`a/2+b≈0.44794<0.8`，属于该窗。
因此可得到actual QW(g)≥8.9e−18||g||²（逐patch两矩零当然仍满足）。
paper symbol在更大窗含3、4，但这些相关在该小域为0，restriction与本仓same actual QW精确一致。
这不推出E₂≤0或QW≥T₂，因而不与535的无费用桥失败定理矛盾。

C001冻结12矩阵的μ=13对应ℓ=log13、source半窗L=log13/2≈1.282>0.8，
脚本枚举prime powers到13（精确端点相关为0）；这个证书不覆盖它们，不认证其ordinary高精度数据。
paper simple-even只指L=0.8/λ=e^0.8的完整window operator，
不自动给别的λ、C001有限N、成长S或最低态与prolate/Ξ相认。

本审查新增独立核是exact pole/parity字典、basis相位及closed compact-resolvent对象补足。
未取得独立数值来源，不能消费paper的正性或simple数字。
唯一下一动作：由主代理原证书审查核附件可得性、所有bounded error/PSD/frame/upper-vector；
若原件仍缺，按C008止损并保留重准入条件，不运行外部代码、不联系作者、不追加Goal。
无本辅助pending process，不改STATE/cadence或推送。
