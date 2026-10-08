# 原素数短上端四矩与完整最大标签前缀付款

2026-10-08。作者 perron_reviewer；研究轮6，基线 5f85dada。
只新增本源；冻结输入、Git、index、cadence及root复盘不动。待不同作者全文审查。
新增的是同一原参数下全部最大标签不超过 Z 的完整族；不付其任意 signed 子掩码。

## 1. 对象、前件与全文输入

保留 X=T/(2π)、L=log X、d=floor(XL)、η=2π/L、s_T=T/√L，
原 even C² 零延拓 φ、a_L=L^−1||φ||₂²≥c、N_L=a_LL。
保留原 χ、Γ、Δ=1024L^(5/2)/X、I_+及所有 carrier/profile/floors；原概率密度为
ν(t)=(d s_T)^−1Σ_(k<d)χ((t−T−kη)/s_T)，supp χ⊂[3/8,5/8]、∫χ=1。
固定 17/20≤u≤1、Z=X^u、Y=√X，只在原系数上加真实条件 p≤Z：
下文空间变量记w，以区别指数u；仍是370/425共用的同一空间变量，不改变积分。
\[
 P_Z(t)=N_L^{-1}\sum_{Y<p\le Z}\frac{\log p}{\sqrt p}p^{it},
 \quad \widehat P_Z(t)=N_L^{-1}\sum_{Y<n\le Z}\frac{\Lambda(n)}{\sqrt n}n^{it},
 \quad M_{4,Z}=T^{-1}\int_J|P_Z|^4,\quad J=[T/4,4T].             \tag{1}
\]
唯一条件前件是原 [R_7/8] 的普通 ζ 部分：所有非平凡零点 β≤7/8。
不新增条带，不把这个前件替成 Dirichlet/Hecke family 密度。重数全部保留。

| 全文读取输入及使用范围 | canonical LF SHA256 |
|---|---|
| [370行 scalar 准入](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md)：两乘子、guards、proper powers | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [453行固定零点包](hybrid-original-squarefree-signed-zero-gram-research-perron.md)：§3 普通 Λ Perron，不消费 sf 修正 | 0b126138c7bf42e9be3c4352b099a6ab37d88cef93af20593593c8e849aa2a17 |
| [184行 Ivić 费用](hybrid-ivic-density-and-scalar-fourth-growth-research-twisted.md)：普通密度与固定网格 | a21a19e7bd09892ed705fa7883143e49c138ffe112c561be9413edaf44d72a1d |
| [276行 whole 桥](hybrid-whole-short-carrier-ratio-and-distinct-criterion-research-twisted.md)：whole P-crossing | c7ff142ebe15232542626e4feda3c05a1285cbf7bff64f462e734c662dafea53 |
| [456重复图](../../notes/456-high-opposite-four-word-vanishing-and-repeated-limit.md)：真实支撑、正 endpoint majorants | 7de855634f93f9d92f6d0cbdd762f9894effaaf40f788b3e02de89f961eadb96 |
| [545行 double-nn](hybrid-whole-fourth-double-nonunit-actual-research-whole.md)：exact partition、正包络、零频 | 2d27661262a1e672a9bb93846de68a661e0d17d8f5e0444117ae6a8debac4215 |
| [425行 unit/mainband](hybrid-whole-fourth-unit-unit-actual-research-whole.md)：全位置、chirp/gate/graph | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |

## 2. 短上端的 entire 显式公式：全部无限尾付款

取 z=⌊Z⌋+1/2、y=⌊Y⌋+1/2，F(w)=(z^w−y^w)/w=∫_(log y)^(log z)e^(wv)dv。
核在 w=0 entire，准确值 log(z/y)；这里落在 w=0 的真实 ζ 留数不删除。
由453§3的局部计数、避零删区，固定 h_0∈[T/32,T/16]、h_1∈[5T,6T]，
使绝对 ζ 高度 −h_i 距零点≥c_0/L；对全部 t∈J共用同一对 h_i。
初线 w=1/2+1/L+iω，端点 ω=t−h_1、t−h_0，异号且 |ω|≍T。
非对称有限 Perron 的两振荡尾分别分部积分，给通常 min(1,C/(T|log(z/n)|))。
对每个半整数 cut，近端 harmonic 和付 O(√z L²/T)，最邻近整数也包含；
远端及全部 n>Z 项用 ΣΛ(n)n^(−1−1/L)=−ζ′/ζ(1+1/L)≪L，不能在∞尾换成 n^ε。
下端同理；因 Z≥Y、z^(1/L)≍1，总截断误差 O(√Z L²/T)。
移至 Re w=−3/2，即 Re(s_0+w)=−1，s_0=1/2−it。
横线 D=−ζ′/ζ=O(L²)，|F|≪√Z/T，横线费用 O(√Z L²/T)；
左线 functional equation 给 D=O(L)，积分费用 O(Y^(−3/2)L²)。
绝对高度始终负且≍T；pole1在矩形外，未跨 trivial zeros。
因此，固定同一个完整负高度包 \(\mathcal Z_T=\{\beta-i\gamma:h_0<\gamma<h_1\}\)，
\[
 \widehat P_Z(t)=-N_L^{-1}\sum_{\rho\in\mathcal Z_T}
 m_\rho F(\beta-\tfrac12+i(t-\gamma))+e_Z(t),\quad
 \|e_Z\|_{\infty,J}\ll N_L^{-1}L^2(\sqrt Z/T+Y^{-3/2}).       \tag{2}
\]
没有 row-dependent 删除零点、上下端或任何真实系数。

## 3. 连续全部实部费用

令 k_L(v)=L/(1+L|v|)。entire 积分式和分式共同给
|F(a+iv)|≪Z^(a_+)k_L(v)，包括 a≤0、v=0和所有重数。
局部计数给 sup_JΣmρ k_L(t−γ)≪L²、∫_J k_L(t−γ)dt≪L。
对同一完整正包络使用 weighted Hölder，而非从 signed 包截取子包，得
\[
 M_4(\widehat P_Z)\ll L^3T^{-1}\sum_{\mathcal Z_T}m_\rho
 Z^{4(\beta-1/2)_+}+O(X^{2u-4}L^4+X^{-3}L^4).             \tag{3}
\]
β≤1/2 部分仅 polylog；其余用先固定有限 σ 网格、再取 T→∞。
密度分别为 n=3(1−σ)/(2−σ)（.5≤σ≤.75），
n=3(1−σ)/(3σ−1)（.75≤σ≤.8），n=3(1−σ)/(2σ)（.8≤σ≤.875）。
本轮另核读 [Ivić 原书](https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/86/6d/866d1cf0-a942-4f8a-9d30-7cb3b03e1b1c/i_ivic-66.pdf)
Th9.3、(9.56)–(9.63)及其直接证明：下端3831/4791<.8，无RH前件。
每格费用 f_u(σ)=4u(σ−1/2)−1+n(σ)。第一段递增、第二段凸；
第三段导数 4u−3/(2σ²)>0。故完整候选费用为
\[
 \max\{0,\ u-2/5,\ 6u/5-4/7,\ 3u/2-11/14\}
 =B(u):=3u/2-11/14,\qquad 17/20\le u\le1.                 \tag{4}
\]
最后一项减前两项分别为 u/2−27/70>0、3u/10−3/14>0。
有限网格损失、重数、|γ|≤6T和固定日志均吸入任意 ε，不用 moving-σ 常数。

## 4. genuine primes：直接正能量证明

平方项为 Σ_(X^(1/4)<p≤√Z) a_p e^(2it log p)，a_p=log p/(N_Lp)。
直接对这些系数，Chebyshev给 Σa_p²≪X^(−1/4)/L、Σp a_p²=O(1)。
其平方按 base pq 展开，唯一分解重数≤2；weighted MV 在 J 给
M_4≪(Σa_p²)²+T^−1(Σp a_p²)²≪X^(−1/2)L^−2+X^−1。
不是从 full proper-power polynomial 的 signed norm 推 subset norm。
对 k≥3，直接取绝对值：Σ_(p^k>Y)log p p^(−k/2)≪X^(−(k−2)/(4k))，
uniform于 k≥3，且 k≤L/log2；归一化总 sup≪X^−1/12。
因此 ||P_Z−widehat P_Z||_(L4(J,dt/T))≪X^−1/12；Minkowski与(3)–(4)给
\[
 \boxed{M_{4,Z}\ll_{\phi,u,\varepsilon}X^{B(u)+\varepsilon}.} \tag{5}
\]
这里没有在增长的第四矩上声称 additive o(1) 差。

## 5. 原 physical/actual 完整最大标签族

A_Z=−Σ_(Y<p≤Z)b_p MφR_(log p)Mφ、G_Z=A_Z* A_Z，只作原有限系数前缀。
四次展开准确等于原四标签全部≤Z，亦即四全异中的 q_max≤Z；原有限投影P和观察配置不重选。
370的两真实乘子 φ(w−ξ)²、φ(w+ξ)仍共用同一空间w；BV L4 norm Oφ(1)、
终端 L2 contraction、两个 C² tails、J_0/J_1/J 全部保持。
将原均匀σ密度换成原χ密度，overlap bound只乘固定 ||χ||∞；
原ν仍≤Cχ/T、支撑在原J_0。其余同(370:11–14)，m_Z≪√Z/L，得
\[
 \int\chi(v)\,d^{-1}\|G_ZE_{T+s_Tv}\|_{\rm HS}^2dv
 \ll [O(1)M_{4,Z}^{1/2}+O(m_Z/T)M_{4,Z}^{1/4}
             +O(m_Z^2/T)]^2\ll X^{B(u)+\varepsilon}.         \tag{6}
\]
原反线性对称固定每列，故 physical B_Z=A_Z+A_Z* 的 fourth 是(6)的2倍。
finite compression fourth≤physical fourth：对 C_Z=E*B_ZE 的每个 eigenvector，
谱测度 Jensen 给 λ⁴≤〈B_Z⁴〉，求和；没有逐tuple删除内部P。
whole P-crossing桥亦直接稳定：原 scalar MV 对任意shift给
1+Z/(s_TL)=O(1)，原C² leakage平均≪L+Z/s_T≪L，
two-cross整词费用≪m_Z²L/d≪X^(u−1)/L²=o(1)。
这些是对前缀整词的重新估计，不从 signed whole error 反推其子族。
重复图只需 polylog 上界：opposite-sign 重复留下 log(q/r)，近区每项
≪1/(X|q−r|)，整数 harmonic 总和≪ZL/X；远区≪Z/X，另乘Σb_p²=O(1)。
same-sign重复 p²/(qr) 使用456(15)–(18)的正 endpoint majorant，限制标签只减正和；
零频 repeated mass≪(Σb_p²)²=O(1)。原支撑排除|S|≥L/2及grid aliases。
finite repeated也直接付款：令 τ=Tr/d、C_p=E*B_pE、C_Z=ΣC_p、S₂=Σb_p²=O(1)；
weighted MV和上述one-leg L2 contraction给 ∫χ(v)τC_Z²dv=O(1)。
T_⋅沿用456(20)的未归一化 trace sums。由ΣC_p²≤S₂I，
T_0/d≤S₂τC_Z²、|T_opp|/d≤S₂τC_Z²；逐项 |Tr((C_pC_Z)²)|≤Tr(C_p²C_Z²)。
T_22/d≤S₂²、|T_×|/d≤S₂²，后者用 |Tr((C_pC_q)²)|≤Tr(C_p²C_q²)。
并且 |T_3|/d≤(Σb_p³)(τC_Z²)^(1/2)、T_4/d≤Σb_p⁴；χ-Cauchy后均O(1)。
代入456(20)的同一有限 inclusion-exclusion恒等式，得 averaged absolute repeated=O(1)。
分别定义 \(\mathcal D_Z^{\rm act/phy}=\int\chi(v)\tau(\text{原四全异标签全部}\le Z)\,dv\)；
physical这里的τ指 d^−1Tr(E* word E)，actual保留全部内部P。由正whole fourth减上述重复量，
两者各自的完整 signed前缀都满足
\[
 |\mathcal D_Z^{\rm act}|+|\mathcal D_Z^{\rm phy}|
       \ll X^{B(u)+\varepsilon}.                           \tag{7}
\]
原far Ψ≤X^−4、正四权质量≪Z²/L⁴，费用≪X^(2u−4)L^C；
因此(7)亦支付原ν下完整 hard-near前缀，不更换原Δ。

## 6. unit 全前缀必须整体减 double-nn

令 \(\mathcal H_{Z,\rm near}\) 是545(1)的原 physical half-ratio四全异near χ-平均，
即 \(\mathcal D_{Z,\rm near}^{\rm phy}/2\)；factor2来自反线性对称，非physical循环换词。
使用545的 exact completion、原 p≠r graph扣除及四种最大位置，
\(\mathcal H_{Z,\rm near}=\mathcal U_Z+\mathcal D_{\rm nn,Z}\)。
q≤Z 时原 q² gate、真实carry、共同空间w及 p,r,s<q 全部保持。
nn非零加性频率的直接正界仍为 |Z_(q,s)^nn,≠0|≪q^−1/2 L^(5/2)，因为
N_A≪qsΔ+1≤qL^(5/2)、Σ_(n modq)|H_n|≪N_A+qlogq及 |B_n|≤√q||A||₂||B||₂。
现在重新聚合其实际外权：
\[
 \sum_{q\le Z}\frac{b_q}{\sqrt q}\sum_{Y<s<q}b_s
 \ll L^{-1}\sum_{q\le Z}b_q\ll\sqrt Z/L^2.                  \tag{8}
\]
故 nn非零频率≪X^(u/2)L^(1/2)。零频 A≤4X 和 q−s≤4qΔ 的原证明是
正计数包络，截断后仍 polylog；内区 H_0≪X^−3L^C 对每个(q,s)一致，
保留其高阶 Euler–Maclaurin及全部aliases；原whole正聚合仍足够。
nn graph扣除545(25)与hard/smooth迁移545(14)也是直接正界，仍分别
≪X^−1/2+ε、X^−2L^C。因此 |D_nn,Z|≪X^(u/2+ε)+X^ε。
由于 B(u)−u/2=u−11/14>0，(7)与 exact整体相减给
\[
 \boxed{|\mathcal U_Z|\ll X^{B(u)+\varepsilon}.}            \tag{9}
\]
这里没有从正r、scalar norm或signed全unit的界，推任何minor/major子mask。

## 7. 实际主频带、费用及限度

425的宽near、两sharp边界、整数aliases、graph正付款在 q≤Z 后仍完整；
原C² φ未升级，ν、全部有限Taylor项、q-prefix floors和真实n频带不变。
chirp直接重聚合425(31)：Σ_(q≤Z)bqΣ_(s<q)bs√(qX/s)≪Z√X L^C；
425(28)的 X^−2 幅及 (A/q²)|I_(q,s)|≪X 给整个correction≪X^(u−1/2)L^C。
其余原正boundary union≪X^ε，actual/nn graph≪X^ε，aliases≪X^−10L^C。
故保持425(36)的完整 signed前缀主带 \(\mathfrak L_{T,Z}\)，
U_Z=L_(T,Z)+O(X^(u−1/2)L^C)+O(X^ε)；B(u)−(u−1/2)=u/2−2/7>0，
所以 \(|\mathfrak L_{T,Z}|\ll X^{B(u)+\varepsilon}\)，不是点态块或绝对块平均。
例 u=9/10 给 B=79/140；u=6/7+1/400 给 B=2821/5600=.50375。
完整 q_max≤X^.9 允许 products 至X^1.8，超过旧12/7 product cap，且其整族费用更小。
这不付款“该前缀中cap外切片”、minor掩码或单q块；需要各自exact桥和直接费用。
u=1仅回到既有5/7。q_top≈X、完整global four矩、sf核心、比例与无零边界都未改善。
本源不给新的论文级全局结论；只记录原实际完整最大标签前缀及主带的条件付款。
