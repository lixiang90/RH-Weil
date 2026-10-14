# C021 G1：actual Γ 的完整 cell 域与 Fourier 能量运输

2026-10-14，代理独立主推导；只编辑本稿，不改 STATE/cadence/Git。
按 AGENTS 恢复 README/STATE、check/show、当前 Goal/frontier、C021、D20261014W、
550/changed-head 原件及543 actualΓ。check通过只说明结构合法。
现场 HEAD `8a4a53647e34f07ed962efa657057fa94d3991a9`、git status clean；
子 get_goal=null，不代 root 的同 G20261014 active 观察。
当前固定基线0c4f3a3/≤538；本稿**只付 G1**，不预付G2或独立结算数学轮。

## 1. 命题、原对象与消费范围

ALL整数 N≥4，L=(logN)/2、I_N=(−L,L)、x=e^(u+L)∈(1,N)，
a_N(u)=e^(u/2)=N^−1/4sqrt x。Π^a 为原 du norm 下 span{a_Nχ_(j,j+1)}
的正交head，R_a=I−Π^a。写 r=a_Nφ 后，

    ||r||²=N^−1/2||φ||²_(L²((1,N),dx))，
    r∈R_a iff ∫_j^(j+1)φ(x)dx=0，j=1,…,N−1。

这是550/C021的新head，**不是547旧weighted-mean R**。
每格 φ_j(v)=φ(j+v)=Σ_(k≠0)φ_jk e^(2πikv)，全 independent complex profiles。
欲付的实际能量为

    E_cell(r)=N^−1/2Σ_(j,k≠0)log|k|·|φ_jk|²。

本稿给自含常数：

    E_cell(r)≤4JΓ(r)+56 logN ||r||²，
    ALL N≥4，ALL r∈R_a∩Dlog。                       (G1)

实际上下述估计不需每cell mean0，任意r∈Dlog、支撑I_N都可对k≠0作此估计。
没有 finite Fourier cutoff、共同profile、periodic-source替换或未知zero前件。
该命题付款原 Γ/domain→cell-log bridge；不是G2/wholecount/RH/Goal完成。

Γ(t)=Reψ(1/4+it/2)−logπ=actual2θ′，Γ₀=Γ(0)，
F_r(t)=∫_R r(u)e^(−itu)du，全部源在R上zeroextension。
按543完整正jump，令

    ν(v)=e^(−|v|/2)/(1−e^(−2|v|))，v≠0，
    Φ(t)=Γ(t)−Γ₀=2∫_0^∞ν(a)(1−cos ta)da，
    JΓ(r)=(2π)^−1∫_R Φ(t)|F_r(t)|²dt
         =∫_0^∞ν(a)||τ_a r−r||²da
         =(1/2)∫_Rν(v)||τ_v r−r||²dv。               (1)

Φ与log(2+|t|)加norm的域等价已由543付；(1)明确保持2π与jump factor。
这里只用原完整型，不把regional/periodic energy标为actualΓ。

## 2. 硬cell截断域：近邻Carleman与全部远格

令 A_j=(α_j,β_j)=(logj−L,log(j+1)−L)，r_j=χ_(A_j)r。
最小 cell宽满足 β_j−α_j=log(1+1/j)≥1/(j+1)≥1/N。
取 δ=1/(4N)≤1/16，定义实际 off-cell kernel

    C_N(u,v)=ν(u−v)·1_(u,v∈I_N, belong to different A_j)。

先证明它是原du的bounded算子且

    ||C_N||≤13 logN。                              (2)

**近端 |u−v|<δ。** 两点只能跨一个相邻cell边界；不同边界的δ邻域互不交。
设距该边界左右分别为 s,t>0，则 |u−v|=s+t，实际 ν满足

    ν(s+t)≤1+1/[2(s+t)]≤1/(s+t)，s+t<δ。

这里使用1/(1−e^(−z))≤1+1/z。每个边界cross block被Carleman核
H(s,t)=1/(s+t) majorize。无需外部定理：Schur辅助weight w(s)=s^−1/2 给

    ∫_0^∞ w(t)/(s+t)dt=πw(s)，

由t=s z²直接积分2∫_0∞dz/(1+z²)=π。故H的L² norm≤π；
左右block [[0,H],[H*,0]]同界。边界δ条互不交，所以全部近端是这些block的direct sum，
其norm≤π，而非把N个π相加。

**远端 |u−v|≥δ。** 正kernel被full-line convolution ν(v)1_(|v|≥δ) majorize。
Young原du给其norm≤2∫_δ∞ν(a)da。由ν(a)≤1+1/(2a)及
ν(a)≤e^(−a/2)/(1−e^−2)、a≥1，

    2∫_δ∞ν(a)da≤log(1/δ)+6。

例如∫_1∞ν≤2e^−1/2/(1−e^−2)<2；其余为1+(1/2)log(1/δ)。
总norm≤π+log(4N)+6≤13logN；最后用π<4、log4<2、logN≥log4>1。
这付款全部远格，包括N成长和大小不等的u-cells。

**域证明不先假设 r_j∈Dlog。** 对ε>0先把(1)的ν截为ν1_(a≥ε)，
记 bounded 非负型J_ε、相应 off-cell kernel C_(N,ε)。有限L²代数精确给

    Σ_j J_ε(r_j)=J_ε(r)+〈C_(N,ε)r,r〉。

上述Carleman/Young证明对所有ε同样给(2)，因而

    Σ_j J_ε(r_j)≤JΓ(r)+13logN||r||²。

ε↓0时由非负integrand单调收敛，得到

    r_j∈Dlog（每j），
    Σ_jJΓ(r_j)≤JΓ(r)+13logN||r||²。                 (3)

这是原hardcell multiplier/domain证明；不用smooth cutoffs逃开实际边界。
相邻Carleman项一般非compact，但有bounded原norm費；没有声称cross为零。

## 3. 单unitcell的完整 periodic Fourier energy，只作中间工具

对任意g∈L²(0,1)，令普通Fouriercoeff g_k，k∈Z，定义真正的torus辅助型

    P(g)=∫_0^(1/2)||τ_a^per g−g||²_(L²(0,1)) da/a。

对每个a用原Parseval再Tonelli，

    P(g)=Σ_k λ_k|g_k|²，
    λ_k=2∫_0^(1/2)(1−cos2πka)da/a。

k≠0，令B=π|k|，则λ_k=2∫_0^B(1−cos t)dt/t。
对1≤B，分部积分给|∫_1^B cos t dt/t|≤3，故

    log|k|≤λ_k/2+3。

于是对全部L²源，按extended nonnegative forms，

    Σ_(k≠0)log|k||g_k|²≤P(g)/2+3||g||²。          (4)

接着直接付periodic wrap，不把它误认regional型。
令

    R(g)=∫_(0<s<t<1)|g(t)−g(s)|²/(t−s) dsdt，
    B(g)=∫_0^1[log(1/v)+log(1/(1−v))]|g(v)|²dv。

torus距离为min(t−s,1−(t−s))，所以精确的P积分可拆普通差距≤1/2与wrap差距>1/2。
前者≤R；后者用|g(t)−g(s)|²≤2(|g(t)|²+|g(s)|²)后积分
1/(1−t+s)，给

    P(g)≤R(g)+2B(g)。                              (5)

例如固定t>1/2的inner积分是log[(1/2)/(1−t)]；固定s<1/2的是log[(1/2)/s]，
都被B的对应endpoint weight支付。并未假设endpoint values相等或无jump。

## 4. √x权、原zeroextension边界与单cell常数

固定j，x=j+v、y=j+w，0<w<v<1，g=φ_j，r_j=a_Nφ在A_j外为零。
由(1)直接分解

    JΓ(r_j)=J_int(r_j)+J_bd(r_j)，
    J_int=∫_(α_j<s<t<β_j)ν(t−s)|r_j(t)−r_j(s)|²dsdt，
    J_bd=∫_(A_j)|r_j(u)|²[
             ∫_(u−α_j)^∞ν(a)da+∫_(β_j−u)^∞ν(a)da]du。 (6)

这两项都非负且属于完整killed/zeroextension Γ，不是只剩regional self能。
因为 j≥1、x/y≤2，

    ν(log(x/y))/(xy)≥1/[2sqrt2·x(x−y)]。

写ρ(x)=r_j(logx−L)=N^−1/4sqrtx φ(x)。由

    sqrtx[φ(x)−φ(y)]
       =N^1/4[ρ(x)−ρ(y)]−(sqrtx−sqrty)φ(y)

及平方Young，

    N^−1/2 R(g)≤4sqrt2 J_int(r_j)+(1/4)||r_j||²。    (7)

第二项自含： (sqrtx−sqrty)²≤(x−y)²/(4y)，所以误差integrand≤
(N^−1/2/2)(x−y)|φ(y)|²/(xy)；对x∈(y,j+1)积分≤N^−1/2|φ(y)|²/4。
没有把√x权视为常数或更换norm。

对0<a≤1，ν(a)≥e^−1/2/(2a)。cell的两侧u-distance都<log2<1，且

    u−α_j=log((j+v)/j)≤v，
    β_j−u=log((j+1)/(j+v))≤1−v。

因此原zeroextension边界penalty精确支付

    N^−1/2 B(g)≤2sqrt e J_bd(r_j)。                 (8)

把(4),(5),(7),(8)合并，使用2sqrt2<4、2sqrt e<4，得到

    N^−1/2Σ_(k≠0)log|k||φ_jk|²
       ≤4JΓ(r_j)+(25/8)||r_j||²。                  (9)

(8)是实际endpoint/domain费用；周期辅助表示只是证(9)的中间步骤。
在(3)给定域中右侧有限，故periodic cell能量确实有限。
全证明是nonnegative integral/Parseval/Tonelli，不用有限profile通过代全源。

## 5. 组合、域闭合与G2保留

对所有j相加，(3),(9)给

    E_cell(r)≤4JΓ(r)+[52logN+25/8]||r||²
             ≤4JΓ(r)+56logN||r||²，N≥4。           (10)

所以actual Dlog → finite E_cell的域运输及原N成长费用已全部支付。
绝对A=4、C=56可消费；无需最佳常数、effectively computableN阈值或数值试验。
actualΓ+Γ₀norm、两个signedpole及所有primepowers的原定义保持。
这里没有删除任何prime/pole；它们不参与G1纯Γ证明。

消费闭合：对象为原L²(du)零延拓/actualΓ，norm因子N^−1/2准确；
量词ALL N≥4和全部 independent complex R_a∩Dlog；hardcell端点、periodicwrap、
√x weight及offcell near/far均付款；实际被消费方向是完整detail上的E_cell quadratic form。
新增桥关闭G1，没有以旧547的不同P/R或旧548 canonicalΓ100替代证明。

仍未付G2：actual U_q=D_q+C_q的全部q/频率/cell/cross signed carry，
单q与fullcarry非compact只反free删除；(10)并不能以D-part occupation省C。
例如occupationεE_cell现在至多4εJΓ+56εlogNnorm，但必须另付
B_C≤δJΓ+C_δlog²Nnorm且4ε+δ<1，才有合同所写conditionalwholecount。
head/mixed PSD、成长实际谱/Ξ与完整Goal门仍另有责任。

本稿判G1 proved；它单独是domain/source bridge，不独立结算数学轮。
下一唯一动作归root：合并G2的原矩阵/全成长量词逆审后，按C021完整准入或入口止损，
不得由本稿推whole负惯性新预算或macro Goal完成。
