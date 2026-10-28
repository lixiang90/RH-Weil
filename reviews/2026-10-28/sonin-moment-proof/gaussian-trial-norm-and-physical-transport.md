# C050：Gaussian辅助范数、完整尾及真实Sonin frame运输

2026-10-28；/root/rational_old_admission 独占证明腿。同G20261027/runtime1793085111/原0c4f。已恢复README/STATE、check后show、Goal/C050、AE、frontier/summary和当前证明动作；本稿不改STATE/Git/cadence，无新web/source。只支付本腿，不将另一Jacobi稿的未消费结论提前作为定理使用。

**交付。** 在C050固定的小c及N尺度，对全部complex degree≤N+2多项式，真实试探范数μ_H与辅助μ_G的全线norm以固定常数等价；两个范数均集中于同一fixed core，Gaussian的t²尾也有统一小量。由此得到Gaussian正交多项式的固定second-moment上界、真实Sonin试探frame的全Gram上下界及其逆，并将任意complex quadratic P的辅助多项式平方和下界运输到同一actual t_X。Gaussian从未充当Sonin向量或actual trace density。

## 1. 旧输入、尺度与角色

仅复用585 root已闭合的两原件：

- `fixed-test-lower/common-sonin-vector-and-polynomial-domain.md`§§5–7：一个固定H_0，H_0(0)≠0，连续/解析且abs(H_0(t))≤C_0 exp(−c_0 sqrt(abs(t)))；每个有限多项式q都有qH_0属于同一个actual实位Sonin域。有限Euler乘子后D_(E,X)qH_0属于RanΠ_X，按原物理全线dt/(2π)范数计。
- `fixed-test-lower/weighted-polynomial-trial-lower.md`§§2–4：全uniform Euler权(W)、ALL complex polynomial的Legendre界(P)、真实H_0的全线未加权矩费(U)、global finite-product界及完整Gevrey tail。

固定

 ℓ=log X，A=sqrt(X)/ℓ，
 D_(E,X)(t)=∏_(p≤X)(1−p^(−1/2−it))，w_X=abs(D_(E,X))²，
 dμ_H=w_X abs(H_0)²dt/(2π)，dμ_G=w_X e^(−t²)dt/(2π)。

μ_G只定义辅助多项式内积；μ_H才是实际向量D_(E,X)H_0q的物理norm。以下在旧unitary Mellin表示工作，以同一Π_X记实际投影的酉共轭，不改变内积。两套测度都不是560的actual ρ_X(t)dt，D_(E,X)也不是一个酉算子。它们的总质量无需归一为1。

令h=rhat_0，r_0固定为C050归一实偶bump。选择一次fixed δ>0，使在C_δ={abs(t)≤δ}上

 0<h_*≤abs(h(t))，0<H_*≤abs(H_0(t))≤H^*，

并令Δ=4−4/sqrt(1+4δ²)>0。该选择只用h(0)>0、H_0(0)≠0及连续性，不依X、多项式、complex系数或Jacobi结论。J_X=[π/ℓ−ℓ^(−2),π/ℓ+ℓ^(−2)]最终包含于C_δ。

下面以c_sc>0记合同的fixed小c，N=floor(c_sc A/ℓ)，和后文complex源系数c区分。具体要求是使两套未加权矩费的共同常数C_*满足2C_*c_sc<Δ/8。c_sc也取在585原ALLpoly允许范围内。对足够大X，n=N+3≤2c_sc A/ℓ；于是所有deg q≤N+2都属于deg q<n。所有阈值可依这些fixed数据，但不依q或其coefficients。固定附加degree 3是margin，没有degree随X优化。

## 2. 两套未加权全线矩费与core权gap

写I_J(q)=∫_(J_X)abs(q)²dt/(2π)。旧(P)给ALL real t及ALL complex deg q<n，

 abs(q(t))²≤C n²ℓ²[Cℓ²(1+abs(t))]^(2n) I_J(q)。                 (P0)

常数吸收2π及J_X的固定规范，且不依q/X/n。在J_X上H_0有固定上下界，所以旧(U)可改写成

 ∫ abs(qH_0)²dt/(2π)≤exp[C_* n log(n+ℓ)] I_J(q)。            (UH)

Gaussian的对应式必须独立核，不能引用其为Sonin向量。由(P0)，只需估计

 ∫(1+abs(t))^(2n)e^(−t²)dt
 ≤2^(2n)[sqrt(π)+Γ(n+1/2)]
 ≤exp[C n log(n+1)]。

第一步用(1+x)^(2n)≤2^(2n−1)(1+x^(2n))；半整数Γ的乘积式给末界。连同n²ℓ²、ℓ^(4n)得到

 ∫ abs(q)²e^(−t²)dt/(2π)≤exp[C_* n log(n+ℓ)] I_J(q)。       (UG)

这是真正全实线的Gaussian矩费，对任意complex coefficients同时有效。加大一次C_*可统一(UH)/(UG)，仍fixed。

旧(W)/(G)及global有限Euler界给某η_X→0，uniform于所列区域：

 inf_(J_X) log w_X≥(4−η_X)A，
 sup_(δ≤abs(t)≤X²) log w_X≤(4−Δ+η_X)A，
 sup_(R) log w_X≤(4+η_X)A。                                 (W0)

最后一条来自finite product/global PNT，未将只在abs(t)≤X²有效的(W)外推全线。设a_H(t)=abs(H_0(t))²、a_G(t)=e^(−t²)。J_X上二者都有fixed正lower，故

 ||q||²_(μ_M)≥c_M exp[(4−η_X)A] I_J(q)，M=H,G。             (LJ)

用(UH)/(UG)和(W0)，对M=H,G均有

 ∫_(δ<abs(t)≤X²) abs(q)²dμ_M
 ≤C exp[−ΔA+2η_XA+C_*n log(n+ℓ)] ||q||²_(μ_M)。             (MID)

由于log(n+ℓ)≤ℓ及2C_*c_sc<Δ/8，上式对足够大X≤exp(−κA)||q||²_(μ_M)，某fixed κ>0。Gaussian在同一区间的t²尾另满足

 ∫_(δ<abs(t)≤X²) t²abs(q)²dμ_G
 ≤X^4 exp(−κA)||q||²_(μ_G)
 ≤exp(−κA/2)||q||²_(μ_G)。                                 (MID2)

这里4logX=o(A)。这是实际支付t²费用，不是从未经加权的“概率集中”直接推二阶矩。

## 3. X²之外：独立全线Gaussian tail及真实H_0 tail

对q≠0，以(P0)、global w界及(LJ)相除，Gaussian尾的相对上界（k=0或2）为

 [∫_(abs(t)>X²) abs(t)^k abs(q)²dμ_G]/||q||²_(μ_G)
 ≤exp[C(A+n logℓ+log(n+ℓ))]
   ·∫_(abs(t)>X²) abs(t)^k(1+abs(t))^(2n)e^(−t²)dt。        (TG)

n=O(sqrt(X)/ℓ²)，在t≥X²上，[(2n+k+1)log(1+t)]/t²的上确界趋0。因此对足够大X和全部t≥X²，

 t^k(1+t)^(2n)≤exp(t²/2)。

余Gaussian积分≤C exp(−X^4/3)；(TG)的前置指数为O(A+n logℓ+log(n+ℓ))=o(X^4)，所以整个相对尾≤exp(−X^4/4)，可再调整fixed阈值。负半线相同。这同时付了k=0和k=2，未将中间区的t²≤X^4用到无界外尾。

真实H_0尾以同一(P0)/(LJ)、abs(H_0)²≤Cexp(−2c_0 sqrt(abs(t)))给

 [∫_(abs(t)>X²) abs(t)^k abs(q)²dμ_H]/||q||²_(μ_H)
 ≤exp[C(A+n logℓ+log(n+ℓ))]
   ·∫_(abs(t)>X²) abs(t)^k(1+abs(t))^(2n)e^(−2c_0 sqrt(abs(t)))dt。

置u=sqrt(abs(t))≥X，多项式和Jacobian只有u^(4n+2k+1)型增长；因n log u/u在u≥X上趋0，可被一半Gevrey指数统一吸收。剩余积分≤Cexp(−c_0X)，前置exp[O(A+n logℓ)]为exp[o(X)]，故相对尾≤Cexp(−c′X)。这恢复旧完整tail，并说明固定t²附加权也不留外尾孔洞。

零多项式各式直接成立。结合(MID)/(MID2)，存在fixed κ_0>0及ε_X≤Cexp(−κ_0A)→0，对全部complex deg q≤N+2同时有

 ∫_(abs(t)>δ) abs(q)²dμ_H≤ε_X||q||²_(μ_H)，
 ∫_(abs(t)>δ) abs(q)²dμ_G≤ε_X||q||²_(μ_G)，
 ∫_(abs(t)>δ) t²abs(q)²dμ_G≤ε_X||q||²_(μ_G)。               (C0–C2)

本腿不需要原中心bad区abs(t)<π/(2ℓ)的消除；core包含中心。δ外gap和完整全尾已经足够给范数比较，且没有更换585的实际向量。

## 4. 全线范数等价与Gaussian正交多项式二阶矩

在C_δ上，R(t)=abs(H_0(t))²e^(t²)有fixed上下界0<a_*≤R≤b_*。由(C0–C2)，

 ||q||²_(μ_H)≥a_*∫_(Cδ)abs(q)²dμ_G
              ≥a_*(1−ε_X)||q||²_(μ_G)，
 (1−ε_X)||q||²_(μ_H)≤∫_(Cδ)abs(q)²dμ_H
              ≤b_*||q||²_(μ_G)。

取X足够大，得到对全部deg q≤N+2的真正全线等价

 **c_H||q||²_(μ_G)≤||q||²_(μ_H)≤C_H||q||²_(μ_G)，**       (EQ)

例如可取c_H=a_*/2、C_H=2b_*。常数只依固定H_0/δ，不依X或q。不是只在core比较，也没有将两个总质量强行相等。

μ_G的权严格正且全部矩有限，故存在按μ_G正交归一的实多项式p_j、deg p_j=j，取正leading coefficient。对每个j<N+2，(C2)和归一化给

 ∫t²abs(p_j)²dμ_G
 ≤δ²∫_(Cδ)abs(p_j)²dμ_G+ε_X
 ≤δ²+ε_X≤2δ²=:C_δ                                      (T2)

于足够大X统一成立。即使p_j随X变化也合法，因为(C2)已在整个degree≤N+2空间统一；没有把仅对固定p的集中结论交换量词。这个fixed C_δ可直接供另一Jacobi腿约束乘t的系数平方和。

## 5. 真正的actual frame及其全Gram逆

令M=N+2，取

 v_j=D_(E,X)H_0p_j，0≤j<M，
 V_X:C^M→mathscr H=L²(dt/(2π))，V_Xz=Σ z_jv_j。

585的ALLpoly域及实际range身份给每个v_j∈RanΠ_X；Gaussian p_j的存在只是选择系数basis，不是将e^(−t²/2)p_j放入Sonin域。对任意z，q=Σz_jp_j的deg<M，(EQ)给其真实物理全Gram

 mathsf H_X=V_X*V_X，**c_H I≤mathsf H_X≤C_H I**。

故这些向量独立且实际维数M。到这个trial子空间的真正正交投影是

 Q_X=V_X mathsf H_X^(-1)V_X*，0≤Q_X≤Π_X。                 (FRAME)

不得省略mathsf H_X^(-1)，也不得把Q_X换成Σ|v_j〉〈v_j|。这保留了原physical范数和非正交frame代价；常数虽fixed，等式中的逆仍真实存在。

对任何本任务合法physical源r，旧531/560已经给每fixed finite X的A_rΠ_X为HS。于是有限正子空间比较和trace合法性给

 t_X(r)=||A_rΠ_X||²_HS
 ≥Tr(A_r Q_X A_r*)
 =Tr_(C^M)[mathsf H_X^(-1)V_X*A_r*A_rV_X]
 ≥C_H^(-1)Σ_(j<M)||A_rv_j||²。                            (TRACE)

最后一步只用mathsf H_X^(-1)≥C_H^(-1)I和有限PSD矩阵的trace，未在ambient无限空间作形式diagonal求迹。接收trial维数M与“源补偿rank≤2”是不同角色。

## 6. 全complex quadratic物理源运输

对任意a,b,c∈C，固定记

 r_(a,b,c)=a r_0+b r_0′+c r_0″，
 P(t)=a+ib t−c t²，rhat_(a,b,c)(t)=h(t)P(t)。

这就是C050的三源组；显式式避免把P(iD)的记号约定误作另一Fourier符号。r_(a,b,c)的support⊂[−1,1]，在所有X使用同一fixed I=(−17/16,17/16)，源的du/zero-extension Dlog与coefficient norm固定等价。下面所有常数同时适用于全部complex coefficients；可令abs(a)²+abs(b)²+abs(c)²=1，亦可用齐次性不归一。

对j<N，q=Pp_j的degree≤N+1，故(C0)/(EQ)适用。仅取core这一正积分即有

 ||A_(r_(a,b,c))v_j||²
 =∫abs(hPp_j)²dμ_H
 ≥h_*² a_*∫_(Cδ)abs(Pp_j)²dμ_G
 ≥h_*² a_*(1−ε_X)||Pp_j||²_(μ_G)。                       (SOURCE)

这里P可有coefficient随X变、可在core内有根；统一结论来自对整个q空间付过尾费，不依“P离零有fixed距离”。也不要求未知ζ零点。被丢掉的core外actual积分非负，且全积分原域有限：H_0有Gevrey尾、有限Euler乘子有界，p_j为有限多项式，h为Schwartz；未漏无定义的physical tail。

由(TRACE)保留j<N项并合并(SOURCE)，得到本腿的actual结论

 **t_X(r_(a,b,c))≥c_T Σ_(j<N)||Pp_j||²_(μ_G)，**            (TR)

其中可取fixed c_T=h_*²a_*/(2C_H)>0，X充分大不依a,b,c。左边是同一个真实Π_X/完整Gram inverse/returns的ordinary trace，右边只是有费辅助范数。m_j的actual ρ_X积分仍不添除2π；本腿所有trial norm内dt/(2π)从头保留，没有二次扣常数。

本腿独立闭合(EQ)/(T2)/(FRAME)/(TR)，不需要Jacobi lower。若另一腿之后根核交付

 Σ_(j<N)||Pp_j||²_(μ_G)≥B_X[abs(a)²+abs(b)²+abs(c)²]，

则(TR)给actual三源Gram的同量级统一lower；**B_X的正大小/量级及actual determinant结论在本稿保持conditional**，未以所求D_X作前件。

## 7. 自然fixed-degree范围及完整型责任

上述范数证明的实际限制是n≤2c_sc A/ℓ。故对任何先fixed有限degree d，同一证明可用N+d的fixed margin（大X阈值可依d），再对j<N和deg P≤d重复(SOURCE)/(TR)，真实源为r_0的至多d阶固定导数的complex组合。这里只如实列同一lemma的fixed-degree运输范围，不证明该族的新Jacobi gap，不优化d、不声称degree随X成长的源系数统一结论。

对C050固定E_3，完整560型身份仍在X覆盖全部自相关可见primepowers之后才是KGram_X=G_X−QGram+PGram；Q/P是同一fixed I上的固定有限矩阵。两个pole保持even正/odd负项，完整Γ=2thetaPrime/FP-contact和全部Λ(p^k)=logp没有被Gaussian替代、窗化或删除。本腿支付actual正迹一侧的试探norm与物理运输，没有证明Qζ正性或把Gaussian解释成新的Weil族。

本稿依赖585已付H_0/ALLpoly域、旧(W)/(P)/(UH)及finite-X ordinary trace；新增核清Gaussian全线/t²尾、统一范数与actual非正交frame运输。完整C050是否闭合、最强旧净后果、轮数与证据编号由root对齐Jacobi腿及fresh后统一消费；本稿不改cadence，不complete长期Goal，不续已止source/query/概率平均或degree队列。
