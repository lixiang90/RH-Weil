# Actual Sonin三源矩阵：移动rank-2门与逐fixed前件分离

2026-10-28；/root/rational_old_admission 独占具体比较稿。恢复README/STATE、check后show、Goal/C049、D20261028AE、frontier/summary及当前已派发的矩阵/前件分离动作。同G20261027/runtime1793085111/原0c4f。本稿只做560+585实际字典、有限维恒等式与指定双原子负对照；**不尝试actual D_X的新lower/proof**，不web/source/新合同，不改STATE/Git/cadence，也不消费另一独占old-coverage稿。

结论是：给定三源上，移动rank≤2补偿的统一必要费准确归结为一个actual矩量行列式比值D_X。585对每个固定源的发散不能单靠positivity/evenness升级为这项统一结论；给定模型显式分离这两层前件。这里没有证明actual D_X发散或不发散，也没有判断585更强原证明资产是否已经蕴含它。

## 1. 实际投影、实结构与Fourier规范

沿560/585，F_X={p≤X}，在原物理Hilbert范数中

 B_X=∏_(p≤X)(I−p^(−1/2)U_logp)，
 G_(Euler,X)=(PB_X*B_XP)在M=RanP的限制，
 Π_X=B_XP G_(Euler,X)^(-1)PB_X*。

Π_X是实际正交投影，保完整Gram inverse、全部returns及两个边界；B_X不是酉。以下有限三源Gram记G_X，勿与这个Euler压缩逆中的G_(Euler,X)混淆。对actual trace density

 ρ_X(t)=abs(b_X(t))²〈k_t,G_(Euler,X)^(-1)k_t〉≥0，
 t_X(r)=Tr(A_rΠ_XA_r*)=∫ abs(rhat(t))²ρ_X(t)dt，
 rhat(t)=∫r(u)e^(−itu)du。

ρ_X已含裸unitary Mellin求值的规范；最后一式**不再乘1/(2π)**。原du Plancherel则为∫abs(rhat)²dt/(2π)=||r||_du²，两个角色不混。

ρ_X确为偶函数，不只是“正密度所以偶”。531的cosine Fourier核2cos(2πxy)、实Sonin cutoff及532的真实P与复共轭C相容；U_logp、B_X及其压缩inverse也与C相容。旧`joint-sonin-cross/full-inverse-carrier-error.md`§4末已明确P/B实结构及k_(−t)=conj(k_t)。又b_X(−t)=conj(b_X(t))，故ρ_X(−t)=ρ_X(t)。这适用于每个finite X的同一actual对象。

固定X时560给2πρ_X=Γ−有界finite-prime项+ε_X，ε_X∈C0；故ρ_X(t)≪_X log(2+abs(t))。下面所有固定smooth源及其导数的矩积分有限；不把这个依X的上界当成长uniform费用。

## 2. 冻结三源及原范数

令

 r_0(u)=c exp[−1/(1−u²)]（abs(u)<1），否则0，
 c=[∫_(-1)^1 exp[−2/(1−u²)]du]^(-1/2)，
 r_1=r_0′，r_2=r_0″，E_3=span_C{r_0,r_1,r_2}。

这是三个固定real smooth compact源，support⊂[−1,1]，所有端点jets为0，||r_0||_du=1；不误称其support是(−1,1)的compact子集。它们属于任何固定L>1的原zero-extension Dlog源域。physical f_i=e^(−u/2)r_i仍合法，不把r_i误作Sonin evaluator。置h=rhat_0，h为实偶Schwartz函数且整延拓，h(0)=∫r_0>0，

 rhat_1(t)=it h(t)，rhat_2(t)=−t²h(t)。

三源复线性独立：若(z_0+it z_1−t²z_2)h(t)恒零，则h在0邻域非零，故三次项以内的这个二次多项式系数全零。

令a=||r_0′||_du²>0、b=||r_0″||_du²。分部积分及flat端点给固定du basis Gram

 H=[[1,0,−a],[0,a,0],[−a,0,b]]>0。

其中b>a²；若Cauchy等号，则r_0″=−a r_0，与非零compact smooth解不相容。也可直接由三源独立得H正定。对r_z=Σz_i r_i，有||r_z||_du²=z*Hz。

原zero-extension Dlog内积在同一basis上给另一个固定正定矩阵J；每个槽smooth compact，费用有限。因此存在固定0<c_E≤C_E<∞，使对全部z∈C³，coefficient范数、||r_z||_du与||r_z||_Dlog互相等价，常数不依X或z的移动。这里没有更换原Dlog权，也没有把global L1与global du等同。

## 3. Actual三源trace Gram和完整K字典

定义实际矩量

 m_j(X)=∫t^(2j)abs(h(t))²ρ_X(t)dt，j=0,1,2。

取使t_X(r_z)=z*G_Xz的Gram约定；ρ偶性使跨奇偶槽为0，导数符号给

 **G_X=[[m_0,0,−m_1],[0,m_1,0],[−m_1,0,m_2]]。**

采用trace第一槽线性的转置惯例时，此实对称矩阵仍相同。具体是m_0=t_X(r_0)、m_1=t_X(r_1)、m_2=t_X(r_2)；02项的负号来自rhat_2=−t²h，不能写成+m_1。

取一个固定L>1并将560的型压缩到E_3。X足够大时F_X已覆盖所有本源自相关可见prime powers，故极化后精确有

 **KGram_X=G_X−QGram+PGram。**

QGram是完整经典Weil型的固定三源Gram，PGram是完整双pole的固定Gram，不随X变化。充分覆盖条件可取X>e^(2L)；实际自相关support在[−2,2]，不需要把源窗随X增长。低X缺prime项不在此“大X已覆盖”式内，不能照抄AE平均稿的错误初读到所有层。

双pole没有删除。若α=∫r_0(u)cosh(u/2)du>0，flat端点分部积分给cosh矩为(α,0,α/4)，sinh矩为(0,−α/2,0)，所以

 PGram=2α² [[1,0,1/4],[0,−1/4,0],[1/4,0,1/16]]。

特别odd槽有负pole，不可把PGram全记为PSD。Γ/FP-contact、全部Λ(p^k)=logp的proper powers都在固定QGram及原560身份中保留；此字典不提供它们的新正号。

## 4. 最小特征值与D_X：确切两倍界

记S_X=m_0+m_2、Δ_X=m_0m_2−m_1²≥0，

 D_X=Δ_X/S_X。

这里D_X仅指本矩量比值，不是585证明中Dirichlet多项式D_X。对足够大X，旧585在r_0上已给m_0>0，分母合法；更早的零分母情形可约定D=0，不影响cofinal问题。

三维矩阵分为odd特征值m_1与even块[[m_0,−m_1],[−m_1,m_2]]。even块小特征值为

 λ_−=(S_X−sqrt(S_X²−4Δ_X))/2
     =2Δ_X/[S_X+sqrt(S_X²−4Δ_X)]。

因此D_X≤λ_−≤2D_X，进而

 min(m_1,D_X)≤λ_min(G_X)≤2min(m_1,D_X)。

故**λ_min(G_X)→∞ 当且仅当 m_1→∞且D_X→∞**。这不是只看三个diagonal。

585应用于固定r_1（其Fourier在0阶数1）已经给m_1≥c_(r1)sqrt(X)/log(X)^4→∞；r_0/r_2的固定diagonal亦已付。此处没有将585应用于随X改变的最小特征向量。是否actual D_X→∞，本稿不证明、不猜下界；“上述三源都满足逐fixed585”不能直接填这个缺口。

## 5. 任意移动rank≤2 Hermitian补偿：原du中的精确含义

令A_X=H^(−1/2)G_XH^(−1/2)，γ_X=λ_min(A_X)，即trace型在E_3单位du源上的最小值。固定basis等价给

 λ_min(G_X)/λ_max(H)≤γ_X≤λ_min(G_X)/λ_min(H)。

对任意每X可变、可读source/参数的Hermitian rank≤2补偿R_X作用于E_3，ker R_X中存在单位向量v_X，所以

 ||A_X−R_X||_op≥〈v_X,A_Xv_X〉≥γ_X。

反过来扣掉A_X最大的两个谱项即可达到γ_X。因此在有限E_3的**不受其它结构限制**的补偿类中，

 inf_(R=R*,rank R≤2)||A_X−R||_op=γ_X。

这是全部moving方向的算子范数必要费，不是假定存在一个固定源同时处于所有ker R_X。全物理Hilbert空间上的rank≤2自伴补偿压缩到E_3仍rank≤2，故同样受这个lower约束；这里的最优上界只声明允许任意E_3谱截断时成立，不冒称它满足某个额外算术/Γ条件。

再令F=H^(−1/2)(PGram−QGram)H^(−1/2)，C_F=||F||固定。实际K压缩为A_X+F。它的最佳rank≤2 Hermitian残差η_X满足

 max(0,γ_X−C_F)≤η_X≤γ_X+C_F。

下界用ker R_X的Rayleigh值；上界可扣掉A_X+F绝对值最大的两个本征项，留下的绝对特征值至多abs(λ_min(A_X+F))≤γ_X+C_F。若γ_X→∞，最终K压缩正定，η_X恰为其最小特征值，和γ_X只差O(1)。故η_X→∞也恰等价于上述actual D_X门。

用固定J代H，完全相同结论适用于E_3原Dlog范数；费用的发散性质不依fixed有限维范数选择。这仅是**rank≤2**和这个固定三维源空间的必要费；不排rank≥3、rank成长、其它有费无限补偿或完整signed机制，也不推出Qζ负或Goal核心方法类边界。

## 6. 指定双原子负对照：每个固定源发散，移动rank-2仍够

本节只用题定模型

 ν_n=e^(2n)(δ_(1/n)+δ_(−1/n))+e^(−t²)dt，n≥1。

它是实际even positive测度，对compact smooth Fourier测试所有矩有限。对任意先fixed非零complex r∈Cc∞(R)，rhat整且非零，故k=ord0 rhat有限，写rhat(t)=a_k t^k+O_r(t^(k+1))，a_k≠0。于是

 ∫abs(rhat(t))²dν_n(t)
 =e^(2n)[abs(rhat(1/n))²+abs(rhat(−1/n))²]+固定有限base
 ∼2abs(a_k)² e^(2n)n^(−2k)→∞。

所以不是只给r_0/r_1/r_2三个diagonal发散，而是全部先fixed非零compact complex源都发散。它甚至满足弱585型量级：沿X_n=e^(4n)，上式≥c_r sqrt(X_n)/log(X_n)^(2k+2)。若要逐全部大X而非序列，令n(X)=floor(log(X)/4)，同一给定族的阶梯重索引仍有e^(2n(X))≥e^(−2)sqrt(X)，故同样支付该弱lower，常数及起点依r。这里不引入actual Sonin身份。

对本稿冻结h，置a_n=1/n、A_n=2e^(2n)abs(h(a_n))²∼2h(0)²e^(2n)，

 β_j=∫t^(2j)abs(h(t))²e^(−t²)dt，j=0,1,2。

Gaussian base在E_3上固定正定，β_0β_2−β_1²>0，β_2>0。模型的矩量恰为

 m_0=A_n+β_0，m_1=A_n a_n²+β_1，m_2=A_n a_n^4+β_2。

故模型D_n准确为

 [A_n(β_2−2a_n²β_1+a_n^4β_0)+(β_0β_2−β_1²)]
 /[A_n(1+a_n^4)+β_0+β_2] → **β_2<∞**。

m_1虽趋∞，D_n却不趋∞。原子对在E_3贡献

 G_atom,n=A_n[[1,0,−a_n²],[0,a_n²,0],[−a_n²,0,a_n^4]]，

其rank≤2（最终恰2）。扣掉这一可移动Hermitian PSD矩阵，残差精确等于固定

 G_base=[[β_0,0,−β_1],[0,β_1,0],[−β_1,0,β_2]]。

在原du归一E_3中同样作congruence即得rank≤2补偿；残差operator norm固定，且Gaussian multiplier≤1及Plancherel给其≤2π。一个明确的moving避原子方向是z_n=(a_n²,0,1)，其源a_n²r_0+r_2在±a_n的Fourier值都为0，而du范数平方→b>0；585的逐fixed量词不控制这个随n变的方向。

## 7. 此比较能与不能供root消费的内容

已执行的是actual三源矩阵/固定原norm/K完整字典，以及一个弱前件负对照。它具体证明：positivity、evenness、每fixed非零测试发散（连同上述弱585 lower）不足以推出三维最小值发散或排任意moving rank-2补偿。因此不能只把旧pointwise585改称uniform rank obstruction。

ν_n不是actual Π_X/ρ_X，不满足本项目已付的全Γ/primepowers/pole/cross字典，也没有被声称满足560的actual密度/连续性/高频结构。**它不是actual Sonin、经典Weil或RH反例。** 此模型不证明actual D_X有界，不否认585完整证明中可能更强的共同向量/ALLpoly资产已决定它；那个最强旧覆盖须由另一腿及root按真实原件核，不能靠这个负对照反推出“未付/新颖”。

本稿没有证明actual D_X新lower，没有新增独立算术输入，也不自行批准下一数学合同或轮数。若root最后核出一个未付且有真实净scope的actual determinant门，再按独立前件闭合决定准入；若更强旧已经直接决定则准确0。它不复活已止概率平均、EX/fullgap/source查询或泛形成队列。原cadence0/history50/latest586/formal17与whole4/5UPPER保持，关键primitive/mixed、完整signed及actual core/cross仍未在本稿支付。

绑定原件：560为9263 bytes/LF SHA256 `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3`；585为7857 bytes/`5dca916d978eef599587ff4c6ce34144f814ddec0567a4c1b2314dcd71cd01af`；实结构旧支链`joint-sonin-cross/full-inverse-carrier-error.md`为12893 bytes/`0db8a2f5acaf6ba4a4655b944f99b450e4af114e9480d4f661cb9e3a7da1c7c2`。无新外部来源或数值计算。
