# 临界铁磁全零谱：正 D′ 极限与一个共同紧支 Weil 反测

2026-10-29；`/root/ising_zero_weil`独占原推导。有限正零轴证明及HS原件已实际全文读/hash并独立核其用于本腿的前件，以下闭合全零谱、统一尾、完整target反测及同链正修补范围。出稿仍须不同fresh/root消费；不授C062/599，不修改STATE/cadence/Git，不声称经典RH或长期Goal完成。无web、新paper/PDF、数值或程序重放。

## 1. 恢复、实际版本与依赖地位

已读README/STATE，执行`research_state.py check`后`show`，读原Goal、当前宏观前沿/停止域及3362-byte准入。恢复时C061仍stopped，新prime-Ising三腿只在准入/原稿阶段；原cadence0/history62/latest598/formal20保持。运行Goal的live同实例由root记录承担，本子稿没有创建或更新Goal。

| 实际输入 | bytes | SHA256 |
| --- | ---: | --- |
| `goals/GOAL.20261027.md` | 9679 | `b3d2acb1f962d793f45d79b6a4e67fb87dd072cd4752108a9298204b4cefa1de` |
| `prime-ising-critical/admission.md` | 3362 | `cd09b0678e05b89ee728b372a7572697359b4bddcb351fa69c9f400ad8c0f997` |
| `prime-ising-critical/finite-positive-zero-source.md` | 3741 | `3bf8fb0d1234a635bfc98fa733a90993c630adf1d568cf28eee94bd5ad2e24bb` |
| `prime-ising-critical/hubbard-stratonovich-and-uniform-limit.md` | 12586 | `743b5c011bb4c3a65be115e175bb7d06a4b82ea4b4040f5aed498bb9dbe9825f` |
| `notes/405-f1-adelic-restriction-moments-and-radical.md` | 14633 | `fe5ee4b574954e51a69c6bbbaa772bb75a1a510c91c837ba02eed8ac406cbb7d` |
| `notes/553-principal-cyclic-closure-and-cofinal-readout-fees.md` | 6613 | `35a40c35d1eaa7fafb462361ddef1bfb9643402b5670f832b9142aeb4b74abce` |
| `notes/563-distribution-side-weil-certificates-and-heat-complete-monotonicity.md` | 11777 | `094c11cb5909eecc7f4e17468f00b43281b9fc6299042565aa792046807a5f4c` |

同日`prime-ising-critical/`相对`reviews/2026-10-29/`。405读取明确源空间、连续性及§§4–5真实关系；553核§§1、5的physical Fourier与actual Q角色；563读取完整目标/positive D′准则。没有冒称重新读它们引用的原外部PDF。

有限正性依赖现由3741自含special-case证明支付，不依赖未读的Lieb–Sokal正文：开bidisk multiaffine收缩通过对角二次根积给|A/D|≥1；边1+t(x+y)+xy在bidisk非零；逐vertex收缩保全部spin一致项；正磁场权代入z_v=exp(−2c_vz)给Re z>0无零，spinflip给另一半平面。本稿独立核了这四步及当前B>0、a>0、J_vw≥0、c_v>0假设。一般作者定理仍未被本稿审查。

HS腿提供的是原Z（含负Gaussian前因子）的局部一致极限，而非另一个积分函数。实际二阶矩必须保`−epsilon`。其全轴缺陷界/统一Gaussian尾足以支付全部固定阶导数与紧λ统一性；本稿未把形式Taylor展开当作该前件。

## 2. 有限谱、参数和精确逆平方矩

令theta=(λ,b)，λ处于固定实紧集，b处于固定J=[b_-,b_+]⊂(0,∞)。用b区别于原B_X与a_X。记

    H_X,theta(z)=Z_X,λ(bz)，H_theta(z)=F_λ(bz)，
    F_λ(z)=I_λ(z)/I_λ(0)，
    I_λ(z)=∫_R exp(−u⁴/12+λu²/2+zu)du。

每个充分大X的H_X是实系数偶exponential-type整函数，H_X(0)=1；全部零点为iγ，γ为非零实数，保全重数。对每个有限X，其阶≤1。标准Hadamard分解按±iγ配对，线性指数因evenness消失，得

    H_X,theta(z)=∏_(γ>0)(1+z²/γ²)，
    H_X,theta''(0)=2Σ_(γ>0)γ^(-2)=Σ_(all γ)γ^(-2)。       (1)

配对后乘积在复紧集正常收敛；没有任意Gaussian因子可塞入阶≤1的even函数。可能零点重数均计入两边。H_X(0)=1排零点γ=0。这里用的是经典整函数分解定理，不把其当新研究结果。

HS腿的准确式是

    Z_X,λ''(0)=I_X,λ''(0)/I_X,λ(0)−epsilon_X,λ
               →m_2(λ)>0

并对λ紧集统一。因此对非空theta紧集K，一次选择X_0、C_K<∞后，全部X≥X_0均有

    Σ_gamma γ^(-2)=b² Z_X,λ''(0)≤C_K。                  (2)

不能把负epsilon漏掉；也没有用有限根表猜测(1)。有限之前的X不影响任何cofinal结论。

## 3. 全零谱、重数和真正的S′/D′收敛

定义计数测度与线性分布

    mu_X,theta=Σ_(all γ)δ_gamma，
    W_X,theta(phi)=Σ_gamma hatphi(gamma)，
    hatphi(t)=∫_R phi(v)e^(−itv)dv。                     (3)

对任意Schwartz phi，由(2)直接有

    |W_X,theta(phi)|≤C_K sup_t t²|hatphi(t)|，
    Σ_(|γ|>R)|hatphi(γ)|
       ≤C_K sup_(|t|>R)t²|hatphi(t)|→0。                (4)

这是全部无限谱的绝对求和与统一tail，不是只比较有限低零点。每个mu_X为正局部有限测度、mu_X([−R,R])≤C_KR²。对全部compact complex g，g*(v)=overline(g(−v))，

    Q_X,theta(g)=W_X,theta(g*g*)=Σ_gamma |hatg(γ)|²≥0。  (5)

傅里叶约定下W是`F^(-1)(2πmu)`；因mu偶，(3)没有漏反号或额外2π。该positive-type性质不要求ordinary trace，也没有给全线du/Dlog的有界读出。

HS腿给H_X,theta→H_theta在复紧集对theta∈K统一。Hurwitz与H_theta(0)=1使极限全部零点仍在imaginary axis。Rouché在每个无边界零点的小圆上保**总重数**；因此局部谱测度vague收敛到mu_theta（H_theta全零点的计数测度）。重根可分裂，但计数必须保持；不假设简单性。

由局部vague与Fatou，Σ_(mu_theta)γ^(-2)≤C_K，故(4)对极限也成立。先在有限频率compact上取极限，再用(4)同时丢掉两侧tail，得到

    W_X,theta→W_theta于S′，因而于D′。                  (6)

它对theta∈K也逐Schwartz测试一致：若不一致，取theta_n→theta_*子列；两组整函数H_Xn,theta_n、H_theta_n均局部一致趋H_theta_*，Rouché局部vague及同一tail界使其分布差趋零，矛盾。这也证明theta↦W_theta(phi)连续。

(6)覆盖所有fixed compact complex源的卷积平方及极化；不声称所有成长源的一致du/Dlog费用。该阶段没有把正型中间层额外要求为逐层消非compact Pan。

## 4. 极限的实轴增长、paired product和重数上限

对λ紧集，Young不等式给|F_λ(z)|≤C_K exp(C_K|z|^(4/3))。实正x上令u=x^(1/3)v，主指数为

    x^(4/3)[−v⁴/12+v+λ x^(−2/3)v²/2]。

有限v区间内末项一致趋零；区间外quartic一致压过|v|和Kv²，积分tail受exp(−c x^(4/3)v⁴)支配。上界用主指数sup及尾，lower用最大点v=3^(1/3)周围任意固定小区间。于是均匀Laplace principle给

    log F_λ(x)/x^(4/3)→kappa=3^(4/3)/4>0。             (7)

分母I_λ(0)在紧λ上下有界，Jacobian的log x项不影响(7)。因此F_λ的整函数阶恰为4/3；H_theta实轴leading为kappa b^(4/3)x^(4/3)，同阶。这里只需此真实增长，不从一个formal概率密度形状推出零谱结论。

H_theta阶<2、even、H_theta(0)=1，按±imaginary零点的Hadamard配对有

    H_theta(z)=∏_(γ>0)(1+z²/γ²)。                      (8)

指数多项式至多一次；evenness消一次项、归一化消常数，不存在order2的Gaussian遗失因子。有限乘积极限中可能的一般lost-Gaussian现象在这里也由(7)排除；不能对任意Gaussian极限不加检查便用(8)。

对I_λ在u作合法分部积分，quartic尾消全部端点，得到

    F_λ'''(z)=3λF_λ'(z)+3zF_λ(z)。                     (9)

若一个零点重数≥3，则F、F′、F″在该点均零，三阶analytic ODE唯一性给F≡0，与F(0)=1冲突。因此每个F_λ零点重数≤2；固定b缩放不改变此上限。

一个后续直接检验也已付：任取1<p<4/3，因log(1+y²)≤C_p|y|^p，(8)若有Σ|γ|^(−p)<∞就使logH_theta(x)=O(x^p)，与(7)矛盾。因此其p-tail moment发散；不能把这种谱误当经典RvM谱。以下使用更强的实际Pan检验。

## 5. 不假RH的真实Pan泄漏

沿405/553固定raw p=(D²+D)h=Eη_0、physical P(v)=e^(v/2)p(v)。它是真实noncompact S_exp关系，两个physical矩mu_±(P)=∫P(v)e^(±v/2)dv均为0。完整actual Weil型已有

    Q_zeta(P)=0，且Q_zeta在S_exp上连续，
    hatP(t)=s(s−1)xi_Riemann(s)/2，s=1/2−it。           (10)

这里Q=2dc−2B=T是含全部背景的actual型；离线零点也用正确partner，不能把未知谱先写成PSD和。(10)的0来自实际Pan在全部零点处的Mellin消失，不使用RH。

假设某theta的全部gamma都满足hatP(gamma)=0。对real gamma，s(s−1)=−1/4−gamma²不为0，因此全部gamma必须是actual xi在临界线上的零点高度。由(9)的重数≤2和无条件RvM计数，便有

    N_theta(T)≤2 N_xi,critical(T)≤2 N_xi,all(T)
               =O(T log(T+2))。                        (11)

这里不要求actual xi零点简单，不要求所有xi零点都在临界线上。现在对(8)取实正x，分部积分得

    logH_theta(x)=∫_0^∞ [2x²/(t(t²+x²))] N_theta,+(t)dt。

零点离0有正距离。代(11)，在t≤x及t≥x两段分别估计，均为O(x log(x+2))，与(7)矛盾。因此每个theta至少有一个gamma满足hatP(gamma)≠0。

mu_theta正且(4)保证求和，故

    q(theta):=Q_theta(P)=Σ_gamma |hatP(gamma)|²>0。       (12)

这是实际同一Pan源上的严格泄漏，比“两个整函数阶不同”更直接；没有假设RH或通过Weil正性converse先改写问题。它也没有把noncompact P误作compact测试。

## 6. 一个共同、合法、双pole-zero的固定compact源

由(4)的uniform S′界、theta谱连续性及P∈S，q(theta)在每个非空紧K连续。由(12)，

    q_K=min_(theta∈K) q(theta)>0。                       (13)

这不提供数值q_K或原du单位球费用，严格正minimum来自实际连续性/紧性。

取固定real χ∈C_c∞，χ=1于[−1,1]，support⊂[−2,2]，χ_R(v)=χ(v/R)。因为P∈S_exp，χ_RP→P于每个原指数导数半范数。若要精确保两degree，可作以下固定修正，不必假设crop本身仍是关系。

取非负非零偶ρ∈C_c∞，m=mu_+(ρ)=mu_-(ρ)>0，ρ_1=τ_1ρ。矩阵

    [ mu_+(ρ)  mu_+(ρ_1) ] =m [1 e^(1/2) ]
    [ mu_-(ρ)  mu_-(ρ_1) ]    [1 e^(−1/2)]

非奇异，故可固定两个real compact线性组合η_±，满足mu_sigma(η_tau)=δ_sigma,tau。令

    r_R=χ_RP−mu_+(χ_RP)η_+−mu_-(χ_RP)η_-。              (14)

则r_R为实际compact C∞源，两个physical指数矩**精确为零**，r_R→P于S_exp。它一般不是Pan；这里仅用它逼近真实Pan，不能把crop或修正crop冒称关系。充分大R时r_R非零。

必须分开支付两种连续性：

* 完整Q_zeta由405/553的S_exp源/显式公式延拓连续，故Q_zeta(r_R)→Q_zeta(P)=0。此处全部Γ/FP-contact、proper powers和双pole仍在目标；双pole只是对(14)这个合法源精确为0，没有从分布定义中删除。
* r_R*r_R*→P*P*于Schwartz，(4)给sup_theta∈K |Q_theta(r_R)−Q_theta(P)|→0。这里使用共同谱尾界，不能借Q_zeta的不同拓扑责任替代。

给任意m_0>0，选一个共同、之后固定的R，使

    inf_(theta∈K)Q_theta(r_R)>3q_K/4，
    |Q_zeta(r_R)|<m_0 q_K/8。                           (15)

由(6)对紧参数的统一性，再取一个X_0(R,K)，则全部X≥X_0、theta∈K有

    Q_X,theta(r_R)>q_K/2。                              (16)

这是同一个fixed compact双pole-zero测试，未把R与X共同增长来隐藏缺陷。虽然选择R依K、m_0，随后全cofinal X均用同一个源。

## 7. 同链最强正修补范围：混合、源适应与必要负修补

考虑任意positive参数混合omega_(X,r)，允许每个stage及每个物理测试源分别选择，任意多/连续components、任意rank/费用/总质量；只要求在上述fixed r_R上，紧critical部分的质量有

    omega_(X,r_R)(K)≥m_0>0

且该部分的cutoff均cofinally超过X_0。允许再加任何nonnegative per-source能量A_X(r_R)≥0；无需假设它是bounded、local、quadratic或已收敛。其在r_R上的总能量至少为

    E_X(r_R)=∫_K Q_X,theta(r_R)domega_(X,r_R)(theta)
                   +A_X(r_R) ≥m_0 q_K/2。

若还有K外的合法positive components，可并入A_X，不会减小此下界。结合(15)，统一得到

    E_X(r_R)−Q_zeta(r_R)>3m_0 q_K/8>m_0 q_K/4。          (17)

没有预设总质量upper bound；若积分∞，更不可能匹配有限target。上述uniform反测还允许不同components用不同充分大cutoff，因为(16)对全部X≥X_0成立。

若每stage混合与修补共同给一个线性positive-type分布，(17)直接否定完整D′收敛；只需取测试phi=r_R*r_R*。若逐源选择导致规则不是同一个线性分布，本稿不冒称它已定义D′对象，但(17)仍否定其对全部fixed源能量的点态Weil匹配。声明完整mixed配对或全部complex源匹配也包含这个对角必要条件，故同样失败。无需另轮再证一个mixed或pointwise版本。

特别覆盖固定λ/固定scale、紧参数source适应、任意positive mixture、无uniform rank/mass/norm约束的正修补。乘任何zero-free整因子（含任意无界Gaussian归一化）逐stage不改变原零点和重数，故不改变该结论；不能拿改变Z''后的数值重写原谱的已付(1)。

Signed/coherent cross修补仍是合法未排范围，但任何最终成功者在这个fixed源上必须贡献一份不消失的负量：由base≥m_0q_K/2、target绝对值<m_0q_K/8及最终误差<m_0q_K/8，必要有

    A_X(r_R)<−m_0q_K/4，最终全部stage。                  (18)

(18)首先只是该fixed源的必要负响应。若另有明确实现A_X(r)=<r,T_Xr>，且T_X确为原du Hilbert空间上的bounded Hermitian算子，则Cauchy界进一步给必要的最终下界 ||T_X||>m_0q_K/(4||r_R||du²)。这仅在该实际map/norm假设下成立；未定义这种算子或使用另一native norm时，不能把响应擅叫operator norm。它不是充分性，也不排所有signed机制；不能把“正添加不救”扩成“一切joint signed都失败”。

## 8. 真正逃逸、强旧和长期Goal

真正未排的是：保留的critical positive component质量趋0/无固定紧集非消失质量；λ或尺度逃出每个固定紧集（含scale→0/∞）；不满足本权Lindeberg条件或非critical regime；非rankone耦合/不同模型；有实际负贡献的signed subtraction/coherent cross；不同源域/不同target或额外独立几何信息。它们不是已成功输入，本稿也不据此授参数/纸链后继。

本稿不强迫D′中间层逐stage消noncompact Pan。主反测先允许每层完整positive spectrum，再用已付的真实Pan与**一个合法compact近似**检测完整target；因此不能以“D′只测compact”排除(17)，也不能以553全局有界exact读出直接代替本证明。

565/566的自动正模型/热身份责任、586的局部theta算子、592正orbit trace图、594自伴Euler pencil、598同B全像均不是本生成函数或它的HS/零谱极限。标准Hadamard/Rouché、positive cone闭性、405旧Pan、RvM、紧性和正混合不各自构成新研究轮。实际新增若经不同fresh/root去重后成立，应只把这个明确family的完整positiveD′构造及其全target/正修补失败统一消费；本稿不自行决定cadence，不以文件/lemma/standard consequence凑轮。

这里没有新的算术primitive/principal/整截面/mixed RR或危险core/cross有利净号；whole542+555→557 leading4/5负惯性UPPER不变。此critical rankone family及其明确正修补类的严格边界不等于所有Lee–Yang/所有positive D′或承担全部核心的方法终结。原Goal三门仍须总体独立审计，保持active/open；无RH证明、无Goal完成声明。

有限positive原件3741和HS12586已读后，本腿无未闭的数学前件；外部Lieb–Sokalgeneral theorem没有被消费为已审。原件存在仍不是root结算，当前状态/唯一轮数/发布由root处理。本分工只写本文件，没有其它修改、web/数值或待续进程。
