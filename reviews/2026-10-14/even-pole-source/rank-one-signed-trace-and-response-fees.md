# 正 even pole 来源门：rank-one signed trace 与 scalar response 的准确费用

2026-10-14；root 指派 AC 唯一来源门的独立 rank-one/trace 审查。
恢复 AGENTS/README/STATE→research_state.py check/show→当前 Goal/frontier/C023 stopped/AC战略与决策，
读 next-positive-even-pole gate、558/557、原022§5、024§1/5及543的 actualΓ域/heat证明。
入口 HEAD `43d4b0af7fe57cbf672d85fc82e7b690fa45e7ed`，当时 git status无输出；
现场 root/principal_final_reverse/theta_joint_source/theta_macro_scope running，旧empty pending只是保存观察。
不spawn代理，不改公共 STATE/Goal/cadence/Git，不建C024。本稿最终原件供root签收，来源审查0轮。
同G20261014、固定0c4f/≤538；当前最强旧由542+555闭合为whole log预算4/5，须扣除。

## 1. 原对象、全源域和三类不能合并的输出

ALL fixed L>0，original Hspace=L²(I_L,du;C)，I_L=(−L,L)，r外置0，full form-domain Dlog。
actual Γ(t)=Reψ(1/4+it/2)−logπ=2θ′，Fourier/Plancherel原因子1/(2π)。
Γ_I是同一zeroextension闭型的自伴realization，Γ_I≥Γ0I，Γ0原值由543保留。

    A_L=Σ_(q<e^(2L))Λ(q)/sqrtq (T_logn^I+T_−logn^I),
    H_L=Γ_I−A_L,
    c(u)=cosh(u/2), d(u)=sinh(u/2) on I_L,
    N_L=||c||²=L+sinhL,
    K=2|c〉〈c|, E_θ=H_L+θK, 0≤θ≤1,
    E_L=E_1,
    Q_L=E_L−2|d〉〈d|.

全部strict actual proper prime powers、原complex norm及双pole保留；K norm=2N_L，不是2或N_L。
对normalized χ=c/sqrtN，K=2N|χ〉〈χ|；不得混用两种response的系数。
555给||A_L||≤β_L；H_L≥b0I，b0=Γ0−β_L，E_θ≥H_L≥b0I。
A/K bounded，故所有E_θ的operator domain等于DomΓ_I，form domain等于原Dlog，均compact resolvent。

三类输出分别是：

* scalar response F_θ(s)=〈c,e^(−sE_θ)c〉及m_θ(λ)=〈c,(E_θ+λ)⁻¹c〉；
* relative/global heat trace Δ_L(s)、Z_H(s)、Z_E(s)；
* full Q_L 的count/PSD/core/Ξ后果。

source c与H都是实际Γ/prime数据直接定义，未按未知Q正值或ζ位置反造。
但“可以定义F”不等于已有独立算术估计，更不等于第三类输出已付。

## 2. c的原domain与source定义：小时间不免费付全高阶moment

c外置0是fixed compact BV；full Fourier hat c=O_L(1/|t|)。
actualΓ增长log(2+|t|)，故∫|Γ(t)|²|hatc(t)|²dt<∞；restriction回I给c∈DomΓ_I、亦DomH/E。
这使用whole-line zeroextension，包括endpoint jumps；不是periodic/regional Γ。
因此F_θ(s)对ALL s≥0 finite，F_θ(0)=N，F_θ'(0)=−〈c,E_θ c〉合法。
更高零时导数须另核c∈DomE_θ^k或相应spectral moments，不能用smooth内部值自动继承。
s>0时heat smoothing与semibounded谱演算允许所有s-derivatives。

F_θ(s)>0（c≠0），因为e^(−sE_θ)作为Hilbert正算子有strictlypositive spectral weights。
这是operator positivity，不要求pointwise positivecone-preserving。
谱测度确切写为

    F_0(s)=∫e^(−sμ)dσ_c(μ),  σ_c(R)=N,
    0<F_θ(s)≤N e^(−sb0).

F的源是原c及全部H action；σ_c未知时该式只是同对象spectral representation，不是算术input。
529限制保持：不能从正K、positiveΓjump或scalarF>0推完整Q保标准锥/最低态/Perron。

## 3. positive rank-one resolvent/determinant的plus符号

取real λ>−b0；所有R_θ(λ)=(E_θ+λ)⁻¹ bounded positive。
令m(λ)=m_0(λ)=〈c,R_0(λ)c〉>0。
直接用(E_θ+λ)R_0=I+2θ|c〉〈c|R_0解rank-one方程，得到

    R_θ=R_0−[2θ/(1+2θm)] R_0|c〉〈c|R_0,
    m_θ=m/(1+2θm),
    D_θ(λ)=det_F(I+2θ|c〉〈c|R_0)=1+2θm.                (1)

positive evenpole的分母是plus；原022 negative oddpole criterion所含1−2m/≤1不能抄来替换。
R_0本身不需要traceclass；rank-one产品是traceclass，relative Fredholm determinant合法。
不得把compact resolvent当traceclass resolvent，Γ~logfrequency尤其没有这种免费蕴含。

m'=−〈c,R_0²c〉，所以

    Tr(R_0−R_θ)=2θ〈c,R_0²c〉/(1+2θm)
       =−∂_λ log(1+2θm)≥0.                             (2)

对于complex spectralparameter z的usual resolvent，可在共同resolvent域解析延拓；
denominator zeros记录E_θ相对H的visible eigenvalue变化，H中c-orthogonal eigendirections可能完全不动。
这个有限window relative determinant没有被识别为通常ζ/Ξ，不是RH证书。
λ安全半轴上D_θ≥1的无零性只是正coupling与shift事实。

Laplace合法性也逐项付款：λ>−b0有

    m_θ(λ)=∫_0^∞ e^(−λs)F_θ(s)ds,

由N e^(−sb0)支配，不在未付小时间globaltrace上换序。

## 4. Duhamel scalar Volterra和special response monotonicity

bounded K给ALL s≥0的operator-norm Duhamel identity

    U_θ(s)=U_0(s)−2θ∫_0^s U_0(s−t)|c〉〈c|U_θ(t)dt,
    U_θ(s)=e^(−sE_θ).

夹同一c后rank-one将整个kernel exact合成为

    F_θ(s)=F_0(s)−2θ(F_0*F_θ)(s).                       (3)

两个scalarF均positive，故0<F_θ(s)≤F_0(s)。对coupling再作Duhamelderivative，有

    ∂_θ F_θ(s)=−2(F_θ*F_θ)(s)≤0.                       (4)

这是特定same-c response的合法monotonicity；不声称U_θ≤U_0的Loewnerorder，
指数函数不是一般operator-monotone，pointwise热核也不能凭正K作此结论。
θ方向在fixed finiteL/S区间可微，rank-oneDuhamelnorm界支付换序。

Volterra Neumann系列完全合法：定义F_0^{*n}为n重正时间convolution，

    F_θ(s)=Σ_(n≥0)(−2θ)^n F_0^{*(n+1)}(s),             (5)
    F_0^{*n}(s)≤N^n e^(−sb0) s^(n−1)/(n−1)!.

因此每个finiteS的级数一致absolute收敛，所有simplex/timeword保留。
“级数可算/收敛”不支付largeL、fullheight或误差比；其absolute majorant含exp(2θNs)。
式(5)的交替符号正是原正evenpole在heat evolution中的负插入，不可改为全positive路径后沿用原相消。

## 5. relative trace ALL s>0合法；individual globaltrace另需s>1

ALLs>0，U_0(s)−U_θ(s)是traceclass，即使两个individualheat尚未认证traceclass。
Duhamel integrand是rankone且

    ||U_0(s−t)K U_θ(t)||_1≤2N e^(−sb0),
    ||U_0(s)−U_θ(s)||_1≤2θsN e^(−sb0).                 (6)

固定L的Bochner traceclass integral合法，s→0 endpoint不是把小时间heat diagonal当有限。
θ方向traceclass differentiable。相同E_θ group允许rank-one tracecyclicity，给

    ∂_θ Tr[U_θ(s)−U_0(s)]=−2s F_θ(s).

所以定义真正的relative correction

    Δ_L(s)=Tr[U_0(s)−U_1(s)]
          =2s∫_0^1 F_θ(s)dθ≥0,                       (7)
    2sF_1(s)≤Δ_L(s)≤2sF_0(s).

注意不是把different H/E semigroup不合法地合为U_H(s)；耦合积分(7)才给显式正号。
直接Duhameltrace integrand〈c,U_1(t)U_0(s−t)c〉不自行有同样pointwise非负判据。

543已核Z_Γ(s)=Tr e^(−sΓ_I)<∞ for s>1；compactresolvent alone不足。
minmax给λ_j(H)≥λ_j(Γ_I)−β，E≥H，于是

    0<Z_E(s)≤Z_H(s)≤e^(sβ_L)Z_Γ(s),   s>1.           (8)

此时两individualtrace合法，才可写

    Z_E(s)=Z_H(s)−Δ_L(s).                              (9)

ALLs>0的relative identity(7)不能把(9)两个∞quantity解释为已付热计数。
本稿也不据s≤1说individual必发散：未付合法性与证明发散是不同声明。

## 6. interlacing：relative热校正至多一条heat尺度，count只改≤1

令h_j/e_j为H/E的nondecreasing complex eigenvalues（multiplicity保留）。
positive rankone的minmax给

    h_j≤e_j≤h_(j+1),
    0≤n_−(H)−n_−(E)≤1.                               (10)

对relativeheat trace可用finiteH-spectralGalerkin直接核fullsum：
P_n投影H前n个eigenvectors、c_n=P_nc。K_n=2|c_n〉〈c_n|→K in trace norm，
fulloperatorE_n=H+K_n的Duhamelrelativeheat也trace-norm→原relativeheat。
有限n空间的positive rankone interlacing给

    0≤Tr[e^(−sH_n)−e^(−s(H_n+K_n))]≤e^(−s h_1).

tail从第J项起的paired差telescoping≤e^(−s h_J)，uniformn。
先n→∞再J→∞付款pairedsum与relativetrace相等；得到ALLs>0

    Δ_L(s)=Σj≥1[e^(−s h_j)−e^(−s e_j)],
    0≤Δ_L(s)≤e^(−s h_1).                             (11)

这给正号而不假设operatorheat order，并明确单巨大intermediate负态可主导heat correction。
旧558丢正pole的heat障碍因此没有自动扩大到E；保原pole是合法逃逸。
(10)/(11)是一般rankone旧机制，不是独立actualarithmeticfee，也不排剩余多谱方向。

fullQ加回negative oddpole：

    n_−(E)≤n_−(Q)≤n_−(E)+1.                           (12)

Γ/A反射对称，c even/d odd；E oddblock=H oddblock，Q evenblock=E evenblock。
正evenrank correction完全不作用于无限dimensionalodd subspace。
式(12)原complexcodimension只加1，不乘2、不按signedrank2加2。
s>1时genericheat预算为 n_−(Q)≤1+Z_E(s)，但实际trace上界仍须算术付款。

## 7. exact signed trace系列及全部路径的保费位置

(5)在θ∈[0,1] finite-timeabsolute一致收敛，代(7)逐θ积分合法：

    Δ_L(s)=−sΣ_(n≥1) [(-2)^n/n] F_0^{*n}(s),
    Z_E(s)=Z_H(s)+sΣ_(n≥1) [(-2)^n/n] F_0^{*n}(s), s>1. (13)

第一项correction是+2sF_0，第二项−2s(F_0*F_0)，符号与(7)/(9)一致。
因simplex convolution bound，其absolute sum≤e^(−sb0)(e^(2Ns)−1)。
这是明确fixedL收敛费；largeL时2N~e^L，该absolute majorant会丢失本门要保的相消。
不能以positive/absolute rankword sum替exact(13)，也不能凭signedsum名字就消费其净值。

sourceF_0(s)还可由actual Γ及allprime word定义：

    U_H(s)=Σ_(n≥0) ∫_(t_j≥0,Σt_j=s)
                  U_Γ(t_0) A U_Γ(t_1) A⋯A U_Γ(t_n) dt,

withnorm≤e^(−sΓ0)β^n s^n/n!；ALLproperpowers和windowconfinement仍在每个A。
夹c给F_0全部word，scalarbound≤N e^(s(β−Γ0))；没有未付smalltime traceclass要求。

若要global Z_H wordtrace，s>1时每个interior simplex点选 Schatten p_j=s/t_j≥1：
Σ1/p_j=1、||U_Γ(t_j)||_(p_j)=Z_Γ(s)^(t_j/s)。
Holder给该wordtrace-norm≤Z_Γ(s)β^n，simplex积分与求和

    Σword ||·||_1≤Z_Γ(s)e^(sβ).

zero-timesegments按p=∞理解，measurezero边界不取非法heat diagonal；
finiteΓ-spectralcuts→Schatten/timeBochner dominatedlimit付款traceclass求和。
故完整paths式是实际合法identity，不是只finiteword或diagonal-only。
但这个费就是(8)的genericnorm主要界，未胜557最强旧4/5；
再接(13)只有signed cancellation未知，仍没有独立netarithmeticinput。

## 8. scalar响应为何不等于global谱控制

F_0/m只描述c的spectralmeasure。若Y是H-invariant且Y⊥cyclic(c)，
改变H|Y不会改变F_0，却改变globaltrace/count；rankone亦完全不作用Y。
actualH至少有整个odd Y，不能把这个角色区别当纯抽象顾虑。
evenblock内c是否cyclic、所有eigenweight及multiplicity也未被本门证明。
即使一条canonical c的完整operatorresidual=o(e^L)，仍不提供024的complementγ或whole residualGram。
old022/024的偶/奇判据、positive阈值和Feshbach接口须分别付款；不能用scalarc-response取代它们。

要用(9)发出betterwhole预算，需 independently certifiedupper J_H(s)≥Z_H(s)
和certifiedlower D_*(s)≤Δ_L(s)，并给 sameL/s/fullsource误差确保

    Z_E(s)≤J_H(s)−D_*(s)

非负且扣557 strong-old4/5后确有净值。若两项leading约exp(se^L)，
各自o(e^L) exponent标签不支付其差；必须有真正subtract后可控误差。
formula m/(1+2m)、relative determinant、finiteword或unknownfullF_0本身不提供这些certificates。
“response已定义/正号已核”只付来源合法；“Γ−A热trace有一个巨大负态”不是actualQ负；
“正evenpole消除它”亦不能免费推PSD或其余core/Ξ。

## 9. strongest-old、当前净门与停止

rankone resolvent/negativeodd+1/parity/compact-resolvent消费属022/024既有接口；
actualΓheat与2π/domain/doubletail属543，actualA/β属555；557强旧whole预算4/5必须扣。
这里的Duhamel/Volterra/relative determinant/signedtrace complete合法性是准确source恢复，
没有新独立算术谱价或globaltrace误差。不同三对象已经闭合区分，不以formalidentity计forcing。

有信息的合法未排路径：保positiveevenpole的真实signedarithmetical F_0/trace fee；
source-adapted/growingcore/paidΓ/deflation；真实allsourcecoupling或独立nonradical算术几何。
529没有授权把E/Q当标准锥正半群；single response也不覆盖全部complex/height方向。

本来源门若只上述identity、旧canonical残差子费或unknownsignedfullsum，则0停止，不建C024，
不调poleweight/s/wordlength维持。重新准入必须给同actualΓ/allpp/c源的独立joint费用，
含fullsource/growth/coverage和全部error，并明确扣4/5后的whole/core净后果。
最深PSD/Γrelative/dangerouscore/Ξ瓶颈仍open；relativeheat合法不通过宏观Goal完成门。

root前件闭合：ALLL fixed时originalcomplexL²/Dlog，operatorssameDomΓ_I；cBVzeroextension归一化N精确；
fullpp/actualΓ2θ′/正evenpoleplus与negativeodd+1；resolventsafeλ与heat时间域明确；
relativetraceALLs>0、individuals>1、scalar/global/fullQ角色分别付；
全部word/time/domain/traceclassnorm费paid；independent signednet/odd/cycliccomplement/growtherror仍open；
strongest-old净值为来源范围恢复0，公共状态由root合并其他owned审查后保存。
