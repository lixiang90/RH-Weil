# 固定双cutoff泄漏：完整相位集中与交叉投影下界

2026-10-31；`/root/two_cutoff_full_proof`，C066的一份独占数学原稿。Same G20261027/runtime1793085111、原冻结0c4f。已恢复README/STATE/check→show、Goal、BB/前沿、C066及6278/6563准入终稿；未读root另行准备的root-proof.md。本文提出完整证明，仍待不同组织审查与root消费，不自行结算数学轮、状态或Goal。

## 1. 实际对象、域及结论

保560/585的原物理Hilbert空间、dilation U、arch Sonin投影P和M=RanP。每个实Z>1定义

    B_Z=∏_(p≤Z)(I−p^(−1/2)U_logp),
    G_Z=(PB_Z*B_ZP)|M,
    Π_Z=B_ZP G_Z^(−1)PB_Z*.

Π_Z是到B_ZM的真实正交投影，使用完整Gram逆/全部returns；不把B_Z当酉。原physical源是r=e^(u/2)bare，r∈Cc∞(R,C)，Fourier为f_r(t)=∫r(u)e^(−itu)du。Mellin酉坐标的receiver测度dμ=dt/(2π)，A_r=∫r(u)U_u du变为M_(f_r)。它与源的du/zero-extension Dlog有不同角色。

取Y=X²，定义

    Δ_X(r)=(I−Π_Y)A_rΠ_X,
    E_X(r,s)=〈Δ_X(r),Δ_X(s)〉HS， E_X(r)=E_X(r,r).

560已付每fixed compact Dlog源的A_rΠ_X∈S₂。左乘正交投影仍S₂，故E_X是全部complex源上的严格Hermitian正半定型，第一槽linear。若

    C_X(r,s)=〈Π_YA_rΠ_X,Π_YA_sΠ_X〉HS,

则输出正交分解严格给E_X=t_X−C_X、0≤E_X(r)≤t_X(r)，其中t_X(r)=||A_rΠ_X||²_HS。mixed普通迹只取HS×HS；未夹源Π或乘积本身不声称S₁。

**定理。** 对每个先fixed非零r∈Cc∞(R,C)，令k=ord₀ f_r<∞。存在c_r>0、X_r，使

    E_X(r) ≥ c_r sqrtX/(logX)^(2k+2) →∞    (X≥X_r).       (1)

常数、起点可依r，不是moving-source或growing-I统一下界。其共同positive scalar校准及第7节明确的positive cofinal混合，不能在全部fixed compact complex源对上趋完整Weil型。逐层E_X一般不stationary；不预称一个W_X正分布，也不要求逐层消noncompact Pan。

## 2. 精确调用的最强旧输入

下列是本稿的已付依赖，未重审其所有嵌套证明。

**(H)** 585 §§2–3给同一实际arch Sonin向量的raw Mellin函数H₀，H₀(0)≠0、|H₀(t)|≤C_H exp(−a_H sqrt|t|)，且每个有限complex多项式倍pH₀∈M。常数不依X或degree；Gaussian不是该实际向量。

**(W)** 写ell_Z=logZ、a_Z=sqrtZ/ell_Z、D_Z(t)=∏_(p≤Z)(1−p^(−1/2−it))、w_Z=|D_Z|²、

    h_Z(t)=Re[e^(−it ell_Z)/(1−2it)].

585 §3已付

    log w_Z(t)=−4a_Z h_Z(t)+o(a_Z)，uniform |t|≤Z².       (2)

并有全实线w_Z(t)≤exp[(4+o(1))a_Z]。后者也由2∑_(p≤Z)log(1+p^(−1/2))≤2∑p^(−1/2)=(4+o(1))a_Z直接给出。高powers在(2)的已核误差内，未从原投影删去。

**(L)** 令ell=logX、a=a_X、J_X=[π/ell−ell^(−2),π/ell+ell^(−2)]。585 §3的全部complex polynomial Legendre账本为

    |p(t)|² ≤ C n² ell² [C ell²(1+|t|)]^(2n) I_p,
    ∫|pH₀|²dt ≤ exp[C₁ n log(n+ell)] I_p,
    I_p=∫_(J_X)|pH₀|²dt,  deg p<n.                    (3)

H₀在J_X最终有fixed正lower，故第一式中把∫J|p|²改成I_p只改常数。第二式由第一式及Gevrey矩直接给出。J_X上h_X=−1+O(ell^(−2))，因此

    inf_(J_X)w_X ≥ exp[(4−o(1))a].                    (4)

**(Q)** 589/C052的source-localization-proof-audit.md §6(4)给整个weighted evaluator的上界

    Q_Z(t)=sup_(||D_Zh||₂≤1)|h(t)|²
          ≤exp[(-4+o(1))a_Z]，uniform |t|≤(logZ)^B,
    k_Z(t,t)=w_Z(t)Q_Z(t).                             (5)

每个B>0先fixed。k_Z是相对dμ的**actual** Π_Z核，ρ_Z=k_Z/(2π)。本稿使用的是乘w_Z之前的whole Q_Z界，不是将fixed-away-zero的k_Z界偷偷用于moving δ。G_Z全逆由(5)保留；不反转trial lower。

**(U)** 589对每fixed compact complex z给

    limsup t_X(z)/s_X≤4|∫z|²，s_X=sqrtX/ell².           (6)

特别∫z=0时t_X(z)=o(s_X)。此旧结论及537完整固定窗正性只在第7节消费，不是(1)的新证明。

## 3. 相位集合与输出的真实小核

先fixed 0<ε≤1/100，设

    S_X={t∈R:h_X(t)≤−1+ε}.

写b=(1−2it)^(−1)、z=e^(−it ell)、w=bz=x+iy。在S_X上x≤−1+ε、|w|≤1，且|b|=|w|≥1−ε。于是

    t²≤[(1−ε)^(−2)−1]/4≤ε， |y|≤sqrt(2ε).

因为ell_Y=2ell，且z²b=w²/b，

    h_Y=Re[(1−2it)(x+iy)²]=x²−y²+4txy
       ≥1−4ε+2ε²−4sqrt(2)ε≥1−10ε≥9/10.              (7)

其中x²≥(1−ε)²、y²≤2ε−ε²、|x|≤1；这完全是相位代数，不使用误差渐近。并且

    h_X(t)=[cos(t ell)+2t sin(t ell)]/(1+4t²)≥0
             当 |t|≤π/(2ell).

故

    S_X⊂{π/(2ell)<|t|≤sqrtε}.                         (8)

在这个固定有界区间内，(2)用于Y的误差及(5)均uniform。由(7)，

    log k_Y(t,t)≤−4a_Y(9/10)−4a_Y+o(a_Y)
               =−(38/5+o(1))a_Y.

所以最终sup_(S_X)k_Y(t,t)≤exp(−7a_Y)。正投影核的local trace/HS身份给

    ||Π_Y 1_(S_X)||op² ≤ ||Π_Y 1_(S_X)||²_HS
       =∫_(S_X)k_Y(t,t)dμ(t)
       ≤(sqrtε/π)exp(−7a_Y)=:κ_X.                    (9)

此处是实际输出的上界，源无关；没有把Q_Y本身当actual核，也没有对未付的整条实线外推(5)。

## 4. 整个增长维trial在S_X的指数集中

取c_ε>0足小，n=n_X=floor(c_ε a/ell)。定义真实子空间

    V_X={D_X pH₀:deg p<n}⊂RanΠ_X.

D_X实轴无零，H₀在J_X非零，故dim V_X=n。下证有b_ε>0，对所有v∈V_X同时

    ||1_(S_X^c)v||² ≤ exp(−b_ε a)||v||².              (10)

这是新集中责任，而非引用585已有粗频带结论。为证它，对p≠0置N_X(p)=||D_XpH₀||²_(dμ)。由(4)，

    N_X(p)≥exp[(4−o(1))a] I_p/(2π).                  (11)

在S_X^c∩{|t|≤X²}，(2)给w_X≤exp[(4−4ε+o(1))a]。再由(3)，该部分质量除以N_X(p)至多

    exp[−4εa+o(a)+C₁n log(n+ell)].                   (12)

最终log(n+ell)≤ell。选c_ε≤ε/(2C₁)，再令X足大使(12)的o(a)≤εa/2，便得(12)≤exp(−3εa)。所有常数与complex p的系数无关。

**频率全尾另算。** |t|>X²不能用(2)。由(3)第一式及(H)，其未加权积分至多

    C n²ell² I_p ∫_(|t|>X²)
      [C ell²(1+|t|)]^(2n) exp(−2a_H sqrt|t|)dt.       (13)

设u=sqrt|t|≥X。因为logu/u在u≥X>e上递减，且n=O(sqrtX/ell²)，

    4n logu ≤(4n ell/X)u=o(1)u.

另外2n log(C ell²)=o(X)，log(C n²ell²)=o(X)。故对所有这些n及u≥X，吸收上述多项式因子后，(13)≤I_p exp(−c_H X)，其中c_H>0固定，可缩小常数吸收dt=2u du及两端积分。这一步对整个degree<n空间uniform，不是单个p的尾。

全线Euler upper再乘exp[(4+o(1))a]，除以(11)，全尾比值≤exp[o(a)−c_H X]，最终小于exp(−3εa)。合并(12)与此尾，因a→∞可将2exp(−3εa)放宽为exp(−2εa)。因此(10)成立，例如b_ε=2ε并取充分大起点。J_X最终位于S_X，(11)与集中集合没有冲突。未把任何多项式/Gevrey辅助测度当actual ρ_X。

## 5. 乘原源后运输到真实输出投影

固定非零r∈Cc∞。f=f_r为非零entire函数，故k=ord₀ f有限。取δ_r>0、d_r>0使|f(t)|≥d_r|t|^k于|t|≤δ_r。现在先fixed

    ε=min(1/100,δ_r²)>0,

再以上述ε选择同一证明中的n_X及起点。这只是证明trial依fixed r选择；E_X的定义、两个投影与任何校准都不依源改变。

对每个||v||=1的v∈V_X，(8)/(10)给

    ||M_fv||² ≥ d_r²(π/2)^(2k)ell^(−2k)
                   [1−exp(−b_εa)].                  (14)

全实线|f|≤||r||₁。分开S_X及其补，由(9)/(10)，

    ||Π_Y M_fv||
      ≤||r||₁[sqrtκ_X+exp(−b_εa/2)],
    ||Π_Y M_fv||²≤2||r||₁²[κ_X+exp(−b_εa)].          (15)

由于a_Y/a_X=sqrtX/2→∞，(15)是O_r(exp(−b'_r a))；尤其o_r(ell^(−2k))。输出投影的正交分解与(14)遂给

    ||(I−Π_Y)M_fv||² ≥ c'_r ell^(−2k)               (16)

对整个unit sphere V_X同时成立。并未先令Y→∞后代入随X移动的向量。

取V_X按原dμ的正交规范基v₁,…,v_n。它们属于RanΠ_X，HS norm的有限正项求和合法，故

    E_X(r)≥Σ_(j=1)^n||(I−Π_Y)M_fv_j||²
          ≥c'_r n_X ell^(−2k)
          ≥c_r sqrtX/ell^(2k+2).

最后一步用n_X≥c_ε a/(2ell)，对充分大X成立。这证明(1)，也说明即使输出cutoff更大，真实相位反配仍保留发散泄漏；没有用t_X的lower减去一个未知C_X。

## 6. 与完整经典型及原费用的关系

对每fixed compact源，完整Q_W(r)为有限常数，因此(1)直接给E_X(r)−Q_W(r)→+∞。这里Q_W是560/537的actual Γ=2θ′、FP/contact、所有原权properpowers及完整rank-two双pole之型，未换成裸Γ或删掉odd负pole。

更精确地，固定I含源支撑，当X包含全部自相关可见primepowers后，旧560与第1节正交分解给

    Q_W−E_X=C_X−K_(X,I)+Pole,
    Pole(r)=2|〈r,cosh(u/2)〉|²−2|〈r,sinh(u/2)〉|².

没有声称这个有符号缺陷在各层非负；恰因E_X发散，不能把它免费视为消失误差。原du及zero-extension Dlog没有改变。finite-X的feature上费为||Δ_X(r)||²≤t_X(r)，这不是uniform source-unitball或growing-I上费；新lower的常数依fixed r。weighted receiver norm只为构造真实trial，绝非原源范数的替身。

## 7. 共同positive校准与明确cofinal混合

固定587的实正du-unit bump r₀，support[-1,1]，m₀=∫r₀≠0。旧537给q₀=Q_W(r₀)>0；r₁=r₀′非零且mean0，完整q₁=Q_W(r₁)≥κ||r₁||²_du>0，κ=2^(−49162)。mean0不等于polefree。

新(1)的k=0给E_X(r₀)≥c s_X；由E_X≤t_X及旧(6)，E_X(r₀)=O(s_X)。若z为任一fixed mean-zero complex compact源，则

    E_X(z)/E_X(r₀) ≤ t_X(z)/(c s_X) →0.              (17)

对任意fixed r,s，写r=c_r r₀+z_r、c_r=(∫r)/m₀，s同理。E_X的PSD Cauchy–Schwarz与(17)控制两条cross项和z_r/z_s项，因此

    E_X(r,s)/E_X(r₀) → c_r overline(c_s).             (18)

任意共同source-independent β_X≥0若满足β_XE_X(r₀)→q₀，则由(18)

    β_XE_X(r,s)→(q₀/|m₀|²)(∫r)overline(∫s).

在r₁上极限为0，与q₁>0矛盾；缺陷趋q₁，至少κ||r₁||²_du。允许任意β_X与cofinal子序列；未限制其由哪些共同非局部资料计算。β_X逐源另选、signed补偿或其它Y(X)不在结论中。

同一直接后果覆盖如下**明确**positive混合：令ν_j为共同nonnegative Borel权，support⊂[R_j,∞)，R_j→∞，并假定每个所测fixed源r的对角积分F_j(r)=∫E_X(r)dν_j(X)有限，令F_j(r,s)=∫E_X(r,s)dν_j(X)，且F_j(r₀)→q₀。E_X按prime集合分段恒定，故可测；mixed绝对积分由Cauchy–Schwarz及对角有限支付。对充分大j，E_X(r₀)>0于该support，(18)的eventual-uniform误差给

    |F_j(r,s)−c_r overline(c_s)F_j(r₀)|
      ≤sup_(X≥R_j)|E_X(r,s)/E_X(r₀)−c_r overline(c_s)|
                                  ·F_j(r₀)→0.

故这一共同cofinal正混合亦失败r₁。未消费不逃逸的有限cutoff质量、逐源权、任意两尺度混合或signed方案。

## 8. 净后果、依赖闭合与停止范围

新付款是第4节整个增长维trial的相位集合集中、第3/5节到**同时成长**Π_(X²)的actual-kernel/HS耦合，以及据此得到(1)。585已知t_X发散没有支付该capture；591的same-output common occupation、594的prime-linear word类及596单prime增量不等于此责任。第7节的mean-collapse方法和q₀/q₁是589/537强旧，只有新k=0 crosslower使它适用于本不同双投影族，不单独计功。

本文没有得到完整Weil正性或whole预算改善，没有排一般Y(X)、source-adaptive、高阶relative或signed机制。只有固定X→X²这一实际规则及所列共同修复被拒。原principal/sections/mixed、危险core/cross、成长Ξ仍未付；542+555→557 leading4/5仍仅负惯性UPPER，三个长期Goal门open。

本稿自身不消费轮数。若不同审查/root闭合，可按C066统一一个完整数学责任结算；不能将本失败证明记为source0，也不能以其完成长期Goal。无新primary、web、作者后章或数值运行；本次实读范围限560定义/身份、585全文、589主定理/校准段、C052 localization proof §§1–6及准入原件。原H₀/prime-sum/wholeQ等依赖仅按已付范围调用，不声称本次重审全部历史证明。
