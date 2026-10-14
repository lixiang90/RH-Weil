# 算术整除梳状源的完整 Weil 正性与 form-core 不覆盖

2026-10-14；C017 一次完整准入，固定成果基线 0c4f3a3、全部≤538。
不改变 Γ=actual2θ′、原 complex/Lebesgue norm、strict全部primepowers或双pole。
本轮不生成矩阵、扫描N、拟合ζ零点；以下对全部整数N的解析证明不是有限实验。
独立审查：[Γ自能/全cross](../reviews/2026-10-14/c017-first/full-gamma-cell-and-cross-audit.md)、
[strict整除/完整pole](../reviews/2026-10-14/c017-first/strict-prime-divisibility-and-signed-pole-audit.md)、
[最强旧/核心覆盖](../reviews/2026-10-14/c017-first/strong-baseline-coverage-and-macro-net-audit.md)。
原工具恢复零轮；新的同source joint消费与准确范围结算一次，宏观Goal保持open。

## 1. 实际对象、全profile量词与主结论

对每个整数 N≥4，冻结

    L=logN/2，M=N−1，h=1/[8N(log(2N))²]，
    x_n=−L+logn，I_n=(x_n,x_n+h)，Omega_N=union_(n≤M) I_n。

原源是所有 f∈Dlog、f=0 a.e.于Omega_N之外，零延拓到R；
Dlog={f∈L²:∫log(2+|t|)|hat f(t)|²dt<∞}，hat f=∫f(u)e^(−itu)du。
每格 f_n(v)=f(x_n+v) 完全独立complex profile，不只共同g的scalarvector。
原norm为Σ||f_n||²；无arithmetically weighted Hilbert norm。

实际完整型是

    Q_L(f)=qΓ(f)−2Σ_(q<N) Λ(q)/√q Re∫f(u+logq)bar f(u)du
           +2Re[A_+(f)bar A_−(f)]，A_±=∫f(u)e^(±u/2)du，
    qΓ(f)=(2π)^−1∫Γ(t)|hat f(t)|²dt，
    Γ(t)=Reψ(1/4+it/2)−logπ=2θ′(t)。

令 H_M=Σ_(n≤M)1/n，p_N=Mh，

    P_N=√[(e^h−1)(1−e^(−h)) M(M+1)H_M/2]，
    CΓ=γ+π/2+3log2+logπ+1/2。

本轮证明全部上述源的全Q下界

    Q_L(f)≥a_N||f||²，
    a_N=log[1/(hM)]−CΓ−4log2−2hMlog(2M)−(P_N−p_N)。        (1)

特别 a_N=2loglogN+log8−CΓ−4log2+o(1)→∞。
一个无需计算/未知zero信息的显式非空实际范围是

    N≥ceil(exp(exp4)) ⇒ Q_L(f)≥(1/2)||f||²。                 (2)

只支付Omega_N上的源类。不是全部I_L的成长正性、负惯性count改善或RH。
后面的form-core负对照表明：其补空间反而能逼近每个固定合法源，不能免费全域消费。

## 2. strict算术平移、原norm及whole域

log(N/(N−1))≥1/N>h，故所有cells不交且在I_L内。
若 I_n+logq 与I_m重叠，|log(qn/m)|<h。
当qn≠m且qn≤M，两个不同整数的log距离>1/N；qn>M时qn≥N、m≤N−1，同样距离≥1/N。
所以只有m=qn≤M，profile坐标v不变。这覆盖所有q<N、所有properprimepowers，
以及qn>N的大乘积；没有小near-overlap误差。

从而prime项精确是 −<F,(B⊗Id)F>，

    B_nm=Λ(n/m)/√(n/m) if m|n,n>m，B_mn=B_nm，B_nn=0。

平移Jacobian1，使用原ℓ²⊗L²(0,h) norm。
各格零延拓属Dlog iff整个f属Dlog：用在该格为1、他格为0的smooth cutoff，
由Γ jump form的product estimate证明其保域；反向有限和即可。
Cc∞(Omega_N)为同一form core，逐格缩支撑再mollify在weightedFourier norm收敛。
下述boundedcross/prime/pole允许从core延拓所有独立合法profile，不以光滑试探源代全域。

## 3. logarithmic算术费，自含旧工具和leading负对照

整除恒等式Σ_(d|n)Λ(d)=logn保持properpowers；求和给
log(K!)=Σ_(q≤K)Λ(q)floor(K/q)。
每个binomial(2j,j)的primepower valuation是0/1 carries，故
ψ(2j)−ψ(j)≤log binomial(2j,j)≤2jlog2。
dyadic求和并上取到下一2的幂，得 ψ(y)≤4(log2)y。
于是所有real y≥1（K=floor y）有

    logy−(1+log2)≤R(y):=Σ_(q≤y)Λ(q)/q≤logy+4log2。

这是已知Chebyshev/Mertens工具的自含恢复，不孤立登记为新算术定理。
Schur auxiliary vector v_n=1/√n 仅用于证明，exactrow为

    (Bv)_n/v_n=logn+R(M/n)≤logM+4log2。

positive-entry matrix和weighted二次Cauchy给原norm下

    |<F,(B⊗Id)F>|≤(logM+4log2)Σ||f_n||²。                  (3)

对任意 normalized g∈Cc∞(0,h)，profile f_n=g/√(nH_M)，其prime邻接Rayleigh
在logM−(1+log2)与logM+4log2之间；leading logM确为必要费用。
此源实际Fourier为hat g(t)e^(itL)Σn^(−1/2−it)/√H_M。
完整Γ必须对这个whole Dirichletpoly支付，不能把(3)的scalarvector诊断当全profile证明。

## 4. actualΓ自能与全部cross，不能省项

从[NIST digamma积分](https://dlmf.nist.gov/5.9#E16)减t=0并换元，原543已付

    Γ₀=−γ−π/2−3log2−logπ，
    qΓ(f)=Γ₀||f||²+∫_0∞K(a)||τ_af−f||²da，
    K(a)=e^(−a/2)/(1−e^(−2a))。

所有源零延拓，非regional或周期Γ。若源g只在一格，a≥h时两支撑不交，
||τ_ag−g||²=2||g||²。对h≤a≤1，用2K(a)≥1/a−1/2，舍其余正项得

    qΓ(g)≥[log(1/h)−CΓ]||g||²。                            (4)

定义C_N的off-cell integral kernel为K(|u−v|)，samecell为0。
精确polarization给

    qΓ(f)=Σ_n qΓ(f_n)−<C_N f,f>。

正距离使mixed核无奇性；截核展开后Tonelli/支配收敛付完整domain。
若n≠m，d_nm=|logn−logm|≥|n−m|/M，hM≤1/8；
格间距≥(7/8)d_nm，K(a)≤1+1/(2a)。row/column积分均≤

    h[(M−1)+(8M/7)H_(M−1)]≤2hMlog(2M)，M≥3。

积分Schur给全部independent complexprofiles

    ||C_N||≤2hMlog(2M)，
    qΓ(f)≥[log(1/h)−CΓ−2hMlog(2M)]||f||²。                (5)

只用1、2格的(g,g)与(g,−g)，cross分别严格负、正：各格自能不能无费相加。
独立审稿还给合法H¹ sineprofiles在n∈[M/2,M]上的下界
||C_N||≥[32e^(−1/2)/(17π²)]hMlogM（M≥32）。
因此uniform O(hM) cross捷径确失败；冻结h付真实logM费，而不是假设mixed为0。
此为cross norm lower，不是wholeQ负值，也不能把分开的worstfees说成同一源同时极大。

## 5. 有符号双pole的完整同源费用

令a=1_Omega e^(u/2)、b=1_Omega e^(−u/2)，pole operator为|a><b|+|b><a|。
精确积分给

    ||a||²=N^(−1/2)(e^h−1) M(M+1)/2，
    ||b||²=N^(1/2)(1−e^(−h))H_M，<a,b>=p_N。

其两个nonzero eigenvalues正是p_N±P_N，故

    pole≥−(P_N−p_N)I，P_N≥p_N，
    P_N≤e^(1/2)hM√(1+logM)。                               (6)

所有complexprofile与两个真实pole保留，无parity/moment条件。
负pole方向a/||a||−b/||b||是piecewise smooth/BV合法Dlog源；不能称pole本身正。
先保2Re(A+barA−)再取费用，不能分别估C/S造成假的指数损失。
primitive/errorbook均为解析exact，未留浮点误差或未付critical inverse。

## 6. 联合净值及显式实际范围

(3),(5),(6)在同一个域与norm相加，得(1)。T=log(2N)，hM≤1/(8T²)，
cross≤1/(4T)，P_N≤e^(1/2)√(1+T)/(8T²)。因而bothfees→0，
log[1/(hM)]=log(8N/M)+2logT，得所述a_N渐近。

为显式(2)，N≥ceil(exp(exp4)) ⇒ T>e⁴>50、logT>4。
 elementary bounds γ<1、π<22/7、log2<7/10、logπ<6/5 给CΓ<13/2，4log2<14/5。
log8>2，于是主余量>10−(13/2+14/5)=7/10。
cross<1/(4T)，P_N<1/(4T)（e^(1/2)<2且√(1+T)≤T），
两负费用合计<1/(2T)<1/100。因此a_N>69/100>1/2。
这个threshold是安全上界，不做小N或h常数优化；每这样的N有无限维非零smooth合法源。

最强旧对照：016/028/543是完整profile/count预算；不直接给该实际comb全profile正性。
已有Γ尾与generic measure uncertainty单独对Omega只给Γ≥log1/(Mh)−C≈2loglogN；
再减(3)的logM还为negative leading logN。新的(5)保eachcell self与全cross，
恢复了这项logM并与actual算术和signedpolejoint抵消；不是一个弱旧子界优化。
069/080的临界norm仍RH强度，167 hard diagonal没有支付此physicalΓ/cross。
新后果准确是特殊成长源类正性；未改善whole n_-上界或证明wholenearPSD。

## 7. 补空间在原Dlog能逼近全部固定源

任意fixed g∈Cc∞((-R,R))。该compact内与Omega相交的cells数K_N=O_R(√N)。
令u_N=1_Omega g。每个截断smoothcell的Fourier由BV积分给
|hat u_n(t)|≤C_g min(h,1/|t|)，故其Dlog图能量≤C_g h[1+log(1/h)]。
FourierCauchy对K_N项求和，得

    ||u_N||Dlog²≤C_R,g K_N² h[1+log(1/h)]=O_R,g(1/logN)→0。  (7)

所以v_N=g−u_N为原Dlog源，支持Omega^c∩[-R,R]，且v_N→g于Dlog。
逐个N在有限个complement gaps内缩支撑/mollify，可取
z_N∈Cc∞((-R,R)\overline{Omega_N})与v_N的Dlog误差≤1/N。
对fixed support，actualprime只有q<e^(2R)且全部bounded，双pole也bounded；
Γform对Dlog连续。因此

    z_N→g于Dlog，Q_(L_N)(z_N)→Q_R(g)。                     (8)

这是合法smooth补空间反例门，不依赖实际负g存在。
若有任何fixed negative witness，(8)会在补空间保留其符号，同时(2)仍可成立。
薄源正性因而与未解wholeQ符号完全相容，不能凭成长支撑外包络或类内全source量词付款RH。
整体measure Mh→0、fixed L² projection→0只是更弱的负对照，(8)已在真实form拓扑成立。

## 8. 六项结算与宏观责任

问题：实际整除算术能否同Γ/dual-pole付统一joint source费用？
新增：全部independent complexprofiles的exactpp/logM、全Γself/cross与signedpole给(1)–(2)，
并付Dlog补空间的(7)–(8)。generic算术/Γ工具恢复不单独新计。
未付：危险core覆盖/补空间耦合、whole负惯性净后果、成长nearPSD、Ξ与独立Hodge符号。
瓶颈：该特殊类joint费已付；whole符号问题可保留在补空间，危险core的投影与耦合仍未定位。
停止：C017一轮止损，不继续缩h或优化小常数/positive薄域；cycle11检查下一core责任。
重准入：density-compatible source有actual near-product/Γ/pole joint及formcore桥，或不同真正算术来源。
唯一下一动作以复盘后的STATE为准；合同/本定理/推送都不完成宏观Goal。
