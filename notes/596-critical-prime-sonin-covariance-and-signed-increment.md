# 596. Actual Sonin 前驱增量：定量协方差、有限 Gram 与收缩阈值正方向

2026-10-29；G20261027/runtime1793085111，冻结0c4f。原4739-byte证明门先冻结，localization14467、domain24003、不同fresh16582三原件terminal，root实际全文核/前件对齐后统一消费一个数学迭代。来源为bramble_trace v2 Th6.5必要proof；自含补足uniform Toeplitz引理、缩窗插值与严格HS迹，actual K运输用旧560，不认证paper未展开q6.19。完整绑定见[root消费记录](../reviews/2026-10-29/critical-prime-covariance-proof/root-consumption-scope.json)。

## 1. 实际对象、量词与结果

原physical H=L²(R,dy)，U_av(y)=v(y−a)，P为gap-one arch Sonin正交投影。每个finite F，B_F=∏(I−q^(-1/2)U_logq)，G_F=(PB_F*B_FP)|RanP，Π_F=B_FP G_F^(-1)PB_F*。这是实际正交投影，Euler乘子不是酉；receiver与physical source角色分开。A_f=∫f(a)U_a da，

    t_F[f]=Tr(A_f Π_F A_f*)=||A_f Π_F||HS².

Fourier为hat f(t)=∫f(u)e^(−itu)du，receiver measure dt/(2pi)，源norm为du，裸乘法源e^(−u/2)f。旧560对任意finite F及含源支撑的I给自伴紧K_(F,I)和完整部分式。

先固定任意complex h∈C_c∞(R)，p沿素数趋无穷；L=logp、a=p^(-1/2)、w_p=La，F_<p={q<p}、F_≤p=F_<p∪{p}，J_ph=h+U_Lh。每p在同一个I_p上相减；不要求I_p固定于p。则

    t_≤p[J_ph]−t_<p[J_ph]=O_h(a L^(9/10)),                 (1)
    <J_ph,ΔK_p J_ph>=2w_p||h||du²+O_h(a L^(9/10)),         (2)
    ΔK_p=K_(F_≤p,I_p)−K_(F_<p,I_p).

对非零h，||J_ph||du²=2||h||du²（p充分大），Rayleigh quotient除w_p趋1。常数依先fixed h及有限Schwartz半范数，不依p；不对任意moving h_p或扩张Dlog球uniform。||J_ph||Dlog≤2||h||Dlog，但指数加权强源半范数可成长如p^N。合法源不等于全源覆盖。

对任意先fixed有限族h_i，极化给

    <J_ph_i,ΔK_p J_ph_j>/w_p → 2<h_i,h_j>du.              (3)

选择所有h_i支撑在(−1,1)，统一I_p=(−L−2,L+2)。任意fixed m可取du正交归一且双pole-zero的h_1,…,h_m。E_p=J_p/√2在该span上为等距，故压缩ΔK_p/w_p的Gram矩阵趋I_m。由每p实际自伴紧性和min–max，

    ∀fixed m，∃P_m，∀prime p≥P_m：
        N_+(ΔK_p; w_p/2)≥m.                              (4)

即收缩阈值w_p/2上的正特征值数趋∞。没有m随p的量化率、固定正阈值、全L²弱/强/算子收敛或ΔK_p≥0。w_p→0，(4)不支付norm非消失。三式及(4)是同一次协方差比较的直接消费，不另计轮。

## 2. 实际未加权 Toeplitz 域及统一交换子

反射Mellin使第一个physical支持条件g|_(0,1)=0等价f∈H²_+。Cosine乘子γ(s)/γ(1−s)和实核与共轭J交换，给

    M(CJg)(−t)=u∞(t)bar f(t),
    u∞=γ(1/2+it)/γ(1/2−it), |u∞|=1.

第二个physical支持条件等价bar u∞ f∈H²_-。因此实位range恰ker T_(bar u∞)。反射Euler D_F^+(z)=∏(1−q^(-1/2)e^(izlogq))和inverse逐finite F均属H∞，双向membership给

    Ran S=D_F^+ ker T_(bar u∞)=ker T_(bar u∞/D_F^+).

这在原未加权boundary norm中识别实际正交投影S；没有把Euler当等距，巨大逐F inverse norm不进入常数。

对任意disk Toeplitz kernel K及full-boundary Z=M_z，forward offdiag的像由rank(Tφ Z−ZTφ)≤1及Tφ在H²∩K⊥ injective得rank≤1。Backward offdiag在f(0)=0时为零，因为完整bar z f仍在K，故rank≤1；negative-Hardy分量没有丢。两block norm≤1，得到||[S,Z]||S1≤2。每个Cayley尺度d的真实boundary unitary保Hardy分解，故

    ||[S,M_(v∘b_d)]||S1≤2Σ|n||vhat(n)|,
    Σ|n||vhat(n)|≤C(||v||2+||v||2^(1/4)||v''||2^(3/4)).

第二式由Fourier在N分割的N^(3/2)||v||2+N^(−1/2)||v''||2优化，N≥1端点另吸收。常数独立d、F、symbol大小及inverse angle，不借新外部引理。

## 3. 缩窗 localization 的真实量化

消耗C052已付的all finite F weighted entire bound：sup_|z|≤R|v(z)|≤exp(CRlog(R+2))||D_Fv||2，C统一；其arch conjugation、Hardy、strip去prefactor均已核，不能换成逐F范数等价。实际对角k_F(t,t)=|D_F(t)|²Q_F(t)，Q是该weighted unit ball的evaluation norm平方，k_F=2piρ_F。

令A=√p/L。原6.1 proof的uniform twisted PNT在|t|≤p^B给绝对O_B(A/L)误差：twist已在Ψ_t中，分部积分只打y^(−1/2)/logy，端点|1/2−it|逆有界；低y及VK误差更小。Euler log高powers O(logL)。因此J=[π/L−L^(−2),π/L+L^(−2)]上log|D|²≥4A−CA/L，weighted unit v的L²(J,dt)≤√(2pi)e^(−2A+CA/L)。

对measure m的集合，half-measure good set的quantile nodes作Lagrange插值，分母j!(n−j)!消去n^n，得

    sup_|z|≤T |P_n(z)|≤C m^(−1/2)[C(T+1)/m]^n ||P_n||L²(E).

没有隐藏nlogn。取m=2L^(−2)、R=A/(logA)^3、n=ceil(3A/logA)、T=L^b，Taylor余项≤exp(−3A+O_b(AlogL/L))，插值log费O_b(AlogL/L)。于是logQ≤−4A+C_bAlogL/L。乘上uniform Euler envelope exp(4A/√(1+4t²)+CA/L)，令δ=L^(−2/5)，得到

    sup_(δ≤|t|≤L^b) k_<p(t,t)≤C exp(−cAδ²).              (5)

δ²≫logL/L。删去终点prime p只改logweight O(p^(−1/2))；在predecessor weighted unit ball重跑上述证明，allfiniteF评价保证同常数。没有假设Gram inverse单调。

## 4. 严格 trace 与完整逆更新

在反射receiver上V=M_(e^(itL))，D=I−aV，B=2I+V+V*，0≤B≤4；W0=|hat h(−t)|²、W=W0B。G=(S D*D S)|SH=(1+a)²I−aSBS≥(1−a)²I。G逆为SH上的完整逆，p≥2一致有界；新正交投影S'=DSG^(−1)SD*。

对bounded nonnegative u≤W0，定义τ_u=Tr_SH(SuS)=||√u S||HS²=∫u k dt/(2pi)。用positive compression和HS平方，不声称bare uS或WS∈S1。严格分解

    SuB(I−S)BS=(S√u)[√u B²S−√u B S B S]

给S1 norm≤32τ_u。对u=W0先支付整个X=SW(I−S)BS的S1，再使用速率。对一般乘子α，Sα(I−S)=[S,α](I−S)在commutator S1时给合法ordinary trace界4(1−a)^(−2)||[S,α]||S1；a仍为既定素数系数p^(-1/2)。

固定monotone even cutoffχ，W0分为u0=W0χ(t/δ)、u1=W0[χ(t/L)−χ(t/δ)]、u2=W0[1−χ(t/L)]，各非负。Center用尺度δ的二阶Cayley导数O_h((1+Lδ)²)，交换子O_h(L^.9)；middle实际至2L，用(5)的b=2支付τ_u1≤C_hLexp(−cAδ²)；tail固定尺度1，Schwartz给O_h,N(L²L^(−N))，固定N=4。故

    C_p=Tr_SH(XG^(−1))=O_h(L^.9).

令A0=SWS|SH为positive S1。DSG^(−1/2)是到新range的实际isometry，故新迹是Tr(G^(−1/2)SD*WDSG^(−1/2))。恒等SD*WDS=A0G−aX，全部换序均S1 times bounded，得exact Δt_p=−aC_p，证明(1)。C_p实性由两个有限实迹之差得，不假正号。原文bare cyclicity shorthand的字面消费冻结，严格版本已自含闭合。

## 5. 560 独立运输、prime powers、poles 和正方向

旧560的所有finite F、共同I上的实际身份是

    t_F[f]=qΓ[f]−P_F[f]+<f,K_(F,I)f>,
    P_F[f]=Σ_(q∈F,k≥1)logq q^(−k/2)[R_f(klogq)+R_f(−klogq)].

Gamma=2θ′及FP/contact保原版本。相减时qΓ精确消去；L>diam supph时R_Jph(±L)=||h||du²、所有k≥2项精确0，故新增P_p=2La||h||du²，给(2)。两侧相关产生系数2，无2pi损失。完整pole在同源差分取消，不能把partial F式叫full Q。

若需双pole-zero，取h=(D_u²−1/4)ψ，ψ非零compact smooth；IBP消两指数moments，平移仍为零，ODE uniqueness保证h非零。有限多个disjoint ψ_j给du正交归一h_j。对h_i、h_i+h_j、h_i+i h_j用(2)有限极化，给(3)；没有全源uniform boundedness偷渡。Finite-dimensional norm收敛给最终compression≥(3/4)w_p I_m，自伴紧min–max给(4)。

## 6. 最强旧扣除、符号和下一门

585的fixed-source whole K发散、587的共同fixed finite basis及whole-K正方向、589的anchor归一化rank-one fixed-pair极限、591的三测试共同occupation gap均已保留。它们不控制两个cofinal投影的signed相减，更不提供moving J_p的o(La)trace更新；两个lower bound不能相减得本结论。新增付款是实际predecessor covariance的定量小费及其同链最强直接(2)–(4)，不是旧560差分换名。它改变局部选择：这份增加的实际Sonin trace没有吸收critical-prime leading term。

在Q=t−K+pole中，本次正K增量是不利方向。不能判full Q负、whole K正、prime增量可累积或危险core/cross费用已付。强旧542+555→557仅leading4/5负惯性UPPER保持；已付safe-high原du运输不重计。算术primitive/principal/整过滤/截面mixed RR、成长Ξ及完整coercivity仍欠，长期Goal三门open。

C059预算耗尽，不续指数、δ、秩率或§7。唯一下一是零数学的同源telescoping覆盖首检：固定终点P、同一I_P和f_P=J_Ph，把K_≤P−K_empty写成Σ_q≤P ΔK_(q,I_P)，明确596只在J_qh方向控制第q项，检验q<P时所需同源cross是否已付。先给实际map/量词比对；若只差未付joint估计便停止准入，不启动prime-sum数学、另章或参数。它检验能否进入whole责任，不承诺可累积。任何新独立principal/mixed或正D′输入可按长Goal重新竞争优先。
