# Source-quotient endomorphic derivation: independent algebra audit

2026-10-29；仅候选准入审，不建合同、不计轮。结论：下述候选不能保留537的非根方向。此处不决定 strongest-old 增量或后续数学预算，不宣称宏观 Goal 完成。

## 对象与已付依赖

令 F=S_exp,C，乘法为卷积，M_f(s)=∫exp(su)f(u)du。沿用原 Fréchet 半范数 sup exp(N|u|)|f^(j)(u)|；d=M(1)，c=M(0)。519给出实际源像 I={全部非平凡ζ零点的 full mρ-jets 为零}，P_an=I∩ker d∩ker c；A=F/P_an。它是解析关系商，尚非几何 principal 商。

只用以下旧资产：[405 §§3–6](../../../notes/405-f1-adelic-restriction-moments-and-radical.md)、[516 §§1–3](../../../notes/516-f1-global-mixed-radical-and-mellin-jets.md)、[519 §§1–4](../../../notes/519-f1-closed-source-image-and-degree-moments.md)、[520 §§1–3](../../../notes/520-f1-source-quotient-spectrum-and-centered-growth.md)。405的完整显式公式为

    2B(f,g)=d(f)c(g)+c(f)d(g)−T(f,g),
    T(f,g)=Σρ mρ M_f(ρ)M_g(1−ρ).

ρ遍历不同零点；mρ只计一次。全部Γ、prime powers与恒等元正规化已含于B；物理源 r=e^(u/2)f 的 full Q_W 等于 T 的相应 Hermitian 对角型（552 §1）。P_an⊂rad B∩rad T，故二者下降到A。无RH或简单零点假设；各mρ有限。

候选：任意 C-linear Leibniz derivation δ:A→A，Jδ(r)=δ([e^(−u/2)r])。不附加连续性、全局单位元、F上提升或有限谱包稠密性。固定指数换元是F的拓扑自同构；没有据此输送物理 Lebesgue norm 的等距性。

## 实际局部幂等元

联合代数映射

    j:A→C²×∏ρ C[z]/(z^mρ),
    [f]↦(d(f),c(f),[M_f(ρ+z)])

由519恰为单射。这里不主张满射、无约束无限乘积模型或谱基。

固定ρ，m=mρ。520实际构造 u_m∈F，M_um=H0(s)/(s−ρ)^m，其中 H0=ξ/2、H0(0)=H0(1)=1/4，且每个非平凡零点的零阶恰为真实重数。逐次除法每步只在上一函数的ρ值为零时执行，保持两端所有指数衰减。

令 qρ(s)=s(s−1)H0(s)/(s−ρ)^m。它是实际函数 (D²+D)u_m 的 Mellin 变换，qρ(ρ)≠0。取唯一的次数<m多项式 Pρ，使 Pρ(ρ+z)qρ(ρ+z)=1 mod z^m。多项式乘子Pρ(−D)保持F，故

    Eρ(s)=Pρ(s)qρ(s)

是实际F函数的变换。其ρ full jet 为1，其余零点full jets为0，且Eρ(0)=Eρ(1)=0。令该函数的商类为eρ。Eρ²−Eρ满足全部jets与双矩零，故eρ²=eρ；不同eρ互相正交。

角代数eρA恰为C[z]/(z^m)：联合单射保证其ρ jet 决定全类；eρ乘以 (−D−ρ)^j 的实际代表给出所有z^j，0≤j<m，保证满覆盖这个有限块。此处微分算子是卷积乘子，未把−D误作Leibniz导子。

405实际 u_d=4(w−h)、u_c=8h−4w（w=h(u−log2)）在I中，双矩分别为(1,0)、(0,1)。它们在A中的类e_d,e_c为正交幂等元，角代数各为C；与全部eρ正交。这些等式仅在商中成立，无须F或A有全局单位元。

## 任意代数导子的约束

设e²=e。Leibniz给 (Id−2L_e)δ(e)=0，而L_e²=L_e，故 (Id−2L_e)²=Id，推出δ(e)=0。于是

    eδ(a)=δ(ea),   δ(eA)⊂eA.

在eρA≅C[z]/(z^m)中，m=1时导子为零；m≥2时

    0=δ(z^m)=m z^(m−1)δ(z)

迫使δ(z)常数项为零，因此该块每个δ(a)的常数项为零。e_dA、e_cA≅C的导子也为零。对每个ρ分别应用上式，即得

    d(δa)=c(δa)=0，M_δa(ρ)=0，∀a∈A，∀ρ。

这些是商上良定义的连续坐标；无需为δ选择线性或连续的提升。由516，

    δ(A)⊂N:=R_val/P_an=rad(B_A),
    R_val={f:d(f)=c(f)=0，M_f(ρ)=0 ∀ρ}。

N是Weil配对根理想。其每个有限jet块的坐标都在(z)内、因而在该块幂零；没有证明整个N为幂零代数或等于nilradical。不能暗加全体mρ有统一上界。

若全部零点简单，519给N=0，故所有这样的δ均为零。反之，若某mρ≥2，角代数上的θ=z∂z非零；δ(a)=θ(eρa)是A→A的非零Leibniz导子，因为eρab=(eρa)(eρb)，且θ的像仍在eρA。它依然只落在N。因此Der_C(A,A)=0当且仅当全部非平凡零点简单；这不是简单性证明。

## 完整配对测试及适用边界

对任意a,b∈A，有 B_A(δa,b)=T_A(δa,b)=0；经共轭极化同样成立。因此

    Q_A(Jδ(r),Jε(s))=0

对任意两个此类导子δ、ε和任意实际源r,s成立，不只是一个二次对角值为零。全Γ/prime powers/双pole被完整公式消费，未删除某项或更换配对。

[537 §2](../../../notes/537-source-exact-weil-window-positive-tail-admission.md)已给物理Lebesgue norm上的全窗正性 Q_W(r)≥2^(−49162)||r||²，r∈Cc∞((−17/16,17/16);C)。取任意非零该窗源，候选输出为full-Q根，故不能忠实保留其Q值或任何严格正的同源范数下界。这是固定实际源的零值障碍，不靠有限谱数值或改范数。

即使再加回 d(a)e_d+c(a)e_c，输出仍全部ζ值为零，所以full Q=T仍为零；B则可能保留405的双曲次数项，不能说它也恒零。552 §1的非零 r0=(D²−1/4)ψ（实偶紧支ψ）同时有两个pole矩零及Q_W(r0)>0，已排除仅恢复次数的补救。

任意源自适应或cofinal族δ_α仍逐个输出N；有限线性组合、卷积乘以A中元素仍在此理想。若实际输出在A的原商拓扑收敛，极限仍在N，因为双矩与全部零点值是连续坐标。若只对原full Q的拉回取逐点极限，每项本已为零，极限仍零。不需族有统一算子界；未定义的极限不能充当输出。此结论不排除改变目标模、secondary regulator、非Leibniz映射或另行支付的几何对象。

仅就代数Hochschild上同调的普通A双模而言，交换性使inner derivations为零，故HH^1(A,A)=Der_C(A,A)，并有上述范围约束。没有证明HH_1、Ω¹、任意模值导子或higher/relative理论为零。δ的存在也未证明解析P_an来自几何边界。

审查结果：实际函数准入、非幺论证、重数与full pairing消费均闭合；本具体同商同配对候选失败537非根测试。是否只是最强旧资产的推论，交由root的strongest-old比较记录统一裁决；本稿不作新输入/净后果/数学轮次声明。
