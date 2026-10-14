# 560. 联合 finite-S Sonin：完整素数幂抵消与原范数紧误差桥

2026-10-14，root 从四份独立原稿核实际对象、全逆、双边界与原源域。
同G20261014／固定0c4f≤538。新综合限下述先固定finite-S量词；不声称外部原件已给本定理。
strongest-old whole预算仍为542+555→557的leading4/5，不能因本桥改写。

## 1. 实际对象与定理

先固定任意有限素数集F，S={∞}∪F，Sonin cutoff固定1。用原物理Hilbert范数的酉log坐标，
H=L²(R,dy)、U_a f(y)=f(y−a)、P为实位Sonin正交投影、M=RanP。原CCM有限S输入给

    B_F=∏_(p∈F)(I−p^(-1/2)U_logp)，G_F=(PB_F*B_FP)|_M，
    Π_F=B_FP G_F^(-1)PB_F*，b_F(s)=∏(1−p^(-1/2−is))。

这是真正物理正交投影；B是有界可逆同构，未把它当酉。
源r的群积分A_r=∫r(a)U_a da；裸求值k_s∈M不同于源r及Γ-window向量。
真实正迹密度为ρ_F(s)=|b_F(s)|²<k_s,G_F^(-1)k_s>，
T_F(r)=∫|hat r(s)|²ρ_F(s)ds，hat r(s)=∫r(y)e^(-isy)dy。
Γ(s)=Reψ(1/4+is/2)−logπ=actual2θ′，Plancherel为1/(2π)。

**定理。** 对每个先固定finite F，实际同源函数

    ε_F(s)=2πρ_F(s)−Γ(s)
             +2∑_(p∈F)logp∑_(n≥1)p^(-n/2)cos(nslogp)

属于C₀(R)。全部primepowers为原权logp/p^(n/2)，没有squarefree product或rational-ratio主项。
对每个固定I=(-L,L)，K_(F,I)=1_I F_unit* M_εF F_unit1_I为原L²(I,du)上的自伴紧算子。
ALL原complex zero-extension Dlog源均有真实ordinary trace

    t_F(r)=Tr(A_rΠ_FA_r*)≥0，
    t_F(r)=q_Γ(r)−∑_(p∈F,n≥1)logp p^(-n/2)[R_r(nlogp)+R_r(−nlogp)]
                      +<r,K_(F,I)r>。                                      (1)

任意固定L>0，取F_L含所有p<e^(2L)，支持外相关exact0，故完整actual Weil型为

    Q_L(r)=t_(F_L)(r)−<r,K_(F_L,I)r>
             +2|<r,cosh(u/2)>|²−2|<r,sinh(u/2)>|²。                         (2)

这支付全部fixed-window源的共同prime比较，允许未知infinite-rank紧误差。
量词∀L逐fixed成立不支付成长uniform K_L费、符号、core/coupling或通常Ξ。

## 2. 原Γ载波与全压缩逆的绝对误差

仅用532已付的实位原Γ相位、双clipping与裸求值；对ALL有限区间J、R≥R_*，

    T=Γ(R)>0，H_T=1_[0,T]，w_R=e^(iRy)1_[0,T]/sqrt(2π)，
    ||(P−H_T)e^(iRy)1_J/sqrt(2π)||≤C_*R^(-1/4)，
    ||k_R−w_R||≤C_*R^(-1/4)。

C_*/R_*独立J/F；保hard endpoints和exactΓ宽度。不能把含Euler振荡相位的F_S直接套该clipping。
置m=∏(1−q_p)、M_+=∏(1+q_p)、d=m²、u=M_+²、w0=∏(1+q_p²)、c=(u+d)/2，
ρ=(u−d)/(u+d)<1，A=I−B*B/c，Q=PAP、Q_T=H_TAH_T。二者operator norm≤ρ。
字母绝对质量Ω=1+(u−2w0)/c，一般可>1；谱收缩不等于绝对word收缩。

当Ω>1，完整逆比较的显式原账本为（v=sqrt(T/(2π))、e=C_*R^(-1/4)）

    |ρ_F(R)−|b_F(R)|²<w_R,G_(F,T)^(-1)w_R>|
      ≤u{ev[d^(-1)+A_N]+e²d^(-1)
              +d^(-1)ρ^(N+1)[(v+e)²+v²]}，
    A_N=[C_e/c](Ω^(N+1)−1)/(Ω−1)，C_e=(ρ+Ω)/(Ω−ρ)。                      (3)

证明：Q_T^j w为区间carrier组合，绝对质量≤Ω^j；clipping给
e_(j+1)≤ρe_j+e(ρ+Ω)Ω^j，因此e_j≤eC_eΩ^j。先付有限words，再付两个谱尾。
不在发散绝对级数中换R极限。c≥w0由finite product的偶交叉项给，≥两素数时Ω−ρ>0。
取解析N(R)=floor(logR/(8logΩ))，(3)绝对误差为

    O_(显式F费用)(R^(-1/8)sqrt(logR)+R^(-δ_F)logR)，
    δ_F=−logρ/(8logΩ)>0。

Ω<1用可和递推；Ω=1用N=floor(logR)与线性word费；单prime／空F按原532／实位处理。
原稿full-inverse-carrier-error§3–5给全部prefactor／退化情形，没有普通数值扩N。
先固定F的absolute误差→0才付本节，不提前升为cofinal S_L。

## 3. 联合窗口模型：两个真实边界不可删

完整因果逆D=B_F^(-1)=∑_(n为F-smooth)n^(-1/2)U_logn，D与D*交换。
令L_-=1_(-∞,0)、H_+=1_(T,∞)、Z=DD*。真正双边界parametrix为

    S_T=H_T(Z−D L_-D*−D*H_+D)H_T。

有界半线因果inverse给exact residual

    G_(F,T)S_T−I=H_T W H_+D L_-D*H_T+H_T W L_-D*H_+D H_T。                (4)

没有将常数1当半线L²向量，也不用单边界代整个窗。
对0<γ<1/2，A_γ=∏(1−p^(-1/2+γ))^(-1)，
J_γ=A_γ∑logp p^(-1/2+γ)/(1−p^(-1/2+γ))，τ(T)≤A_γe^(-γT)。
(4)给||S_T−G_T^(-1)||≤2M_+²A_γm^(-3)e^(-γT)。

写delay x=logn、c_x=n^(-1/2)。合法L² carrier配对中whole Z的费用为
∑_(x,z)c_xc_z e^(-iR(x−z))(T−|x−z|)_+/(2π)；两个实际半线边界各给
∑c_xc_z e^(-iR(x−z))min(x,z)/(2π)+O_(F,γ)(e^(-γT))。
所有一阶矩绝对可和。逐pair使用|x−z|+2min(x,z)=x+z，合并为

    |b_F(R)|²<w_R,G_T^(-1)w_R>−T/(2π)
       =−Re∑_(p∈F)[logp α_p/(1−α_p)]/π+E_(F,T,R)，
    α_p=p^(-1/2)e^(-iRlogp)，|E_(F,T,R)|≤C_(F,γ)(1+T)e^(-γT)。           (5)

可取C_(F,γ)=M_+²{[m^(-1)J_γ+J_0A_γ]/π+A_γ²/(πγ)+M_+²A_γ/(πm³)}。
证明对ALL T>0/ALL R成立，所有mixed delay按唯一分解各有一次，无lattice／小除数前件。
最后的additive主项来自joint对数导数，不是实际投影／迹相加。
F={2,3}时log(3/2)、log6在(5)主项严格无系数；其W项仍真实存在。

## 4. 模型到actual C₀及原源域

在(5)取exact T=Γ(R)、γ=1/4，模型费O_(F)(logR R^(-1/4))。
与(3)合成，全actual ε_F在正高频趋0；原算子实结构给负高频同样成立。
原裸k_s连续norm及弱连续给强连续，fixed bounded G^-1给ρ_F低频连续／有界。
因此ε_F∈C₀，而非仅unknown signed sum或有限word结论。

固定F时finite-prime symbol和ε_F有界，2πρ_F=Γ−bounded+bounded≥0，
高频与log权可比，自然positive trace型域恰为原Dlog(I)。
先缩支撑r_a(u)=r(u/a)、a↑1，再mollify，给Cc∞(I)的原log Fourier core。
ρ上界使A_(r_j)Π_F在HS中Cauchy；fixed I的L¹收敛给A_(r_j)→A_r operator norm，
故HS limit确为A_rΠ_F，ordinary trace与原密度公式运输ALLcomplex Dlog。
K_F的有限频段截断在I×I为HS，C₀尾operator norm→0，所以K_F自伴紧，极化给(1)。
所有q≥e^(2L)相关为0，包括等号的零测端点；F_L覆盖全部base primes后给(2)。

## 5. 原ratio探针的实际结论

沿唯一门d=log(3/2)，固定小χ／δ，h_R=(∂_y²−1/4)(e^(iRy)χ)/||·||，
g_R±=[h_R(·+d/2)±h_R(·−d/2)]/sqrt2。原范数逐R=1，双pole矩exact0，
支撑直径<log2使ALLactual pp相关为0；每个源在原Dlog并weak→0。
actual Γ的两个patch交叉O_k(R^(-k))，个体Q仍logR−log(2π)+O(R^(-1))。
compact K_23于是给

    [E23(g_R+)−E23(g_R−)]/2→0，E23=T23−Q_W。

W同一探针的对应交叉恒为1/sqrt6；真实fullG inverse的比较误差不是W系数。
probe仅必要门pass，但本定理另付共同ε_F与ALLDlog桥，不能从一个cross反推这些结论。
不取得Q负／新fixed窗正性；537已覆盖该小窗。

## 6. 成长费用、强旧与停止

全部费用保m_F/M_F/ρ_F/Ω_F/δ_F/A_γ/J_γ/C_(F,γ)，不能吞进统一O(1)。
F_L={p<e^(2L)}时，PNT给log(M_F²/m_F²)=(4+o(1))e^L/L，Ω_F→3，
δ_F≈(4log3)^(-1)(m_F²/M_F²)；(3)谱尾证书在logR~θe^L尺度不趋0。
这是当前充分certificate不能支付成长费用，不是actual signed error的必要下界。
允许source-adapted／joint signed／不同inverse组织／paid Γ与非有限秩compact修复。

另核真实cofinal辅助norm：m_F D_F=E U_X，X=∑logp K_p、K_p为独立几何变量。
F_L={p<e^(2L)}时E X=2e^L+o(e^L)、VarX≤C_V L e^L，
C_V=16log2/(1−1/sqrt2)²。因此对先fixed ε>0、ALL T≤(2−ε)e^L，

    m_F||1_(T,∞)D_F1_(-∞,0)||→1，
    μ_F(X>T)≥1−4C_V ε^(-2)L e^(-L)。                                  (6)

实际norm1测试是support(-3h,-h)的smooth bump，h=εe^L/8；
||mD f−U_(EX)f||≤||f'||sqrt(VarX)=O_(ε,φ)(sqrtL e^(-L/2))，后者全落右半线。
这给全physical-Hilbert inverse的真正norm下界；输入不在Sonin M，不是k_R，
未证在1_(-∞,0)D*H_Tw_R的实际像内，宽度e^L也不是Weil source I_L。
所以(6)不付actual ε_(F_L)／Q／危险core下界，不通过Goal方法类门。
它停止粗全H norm解耦主攻；下一须实际receiver像与signed费用，不能把换角色当修复。

strongest-old531的finiteS合法性与532各singlep C₀不已给(3)–(5)的共同inverse费用。
511 finiteEuler相位的周期曲率O_F(1)不能免费继承纯Γ的O(1/R)clipping。
新综合支付真正finiteS的allprimepowers、原source norm compact误差及ALLfixedL源桥。
不是新CCM外部定理、不是world优先权声明，也不重新计537/538正性。
whole预算4/5未改善，K_L符号/norm/growth/core/coupling/通常Ξ仍未付；宏观完成门open。
统一研究结算仅一次，独立稿、补域和probe不另计轮；不预建C024、不续ordinaryN或第三S标签。

停止该ratio必要门与fixed-S主项恢复。下一仅针对真实joint K_L的共同signed费用／
source比较符号或其允许修复后的成长必要费，先原证据和可判门，不将unknown domination改名。
原稿、逆审和root闭合记录见reviews/2026-10-14/joint-sonin-cross/root-consumption-scope.json。
