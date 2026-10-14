# MV来源最后necessary门：parent1全部mode的实际响应

2026-10-14，独立原域/cutoff/block核查；**零数学轮**，不建立或重开合同。
本次按 AGENTS 恢复 README/STATE/check/show、同 Goal/frontier、C021 stopped、
D20261014Y、actual carry矩阵与MV原公式。结构check不认证数学。
入口HEAD `36810d109e184787027656c31fb636e880036d7f`，root正在编辑STATE/551及来源目录；
子get_goal=null，不代root运行态。只写本稿，不改STATE/cadence/Git。

## 1. 实际对象、域及需要核的量

ALL整数N≥4，ALL整数m≠0，M=|m|≥1，e(z)=exp(2πiz)。
采用550/C021的changed head Π^a，r=a_Nφ，a_N=N^−1/4sqrtx，du=dx/x，
原norm=N^−1/2||φ||²_dx，每unitcell φ mean0；不是547旧R。
actual one-sided fullcarry为

    H_N=Σ_(2≤q<N) Λ(q)/sqrtq C_q，
    C_q=(I−P_(q|k))U_q，U_qφ(x)=sqrtqφ(qx)。

full detail adjoint在flatdx是R_flat U_q*(I−P_(q|k))；保全部actual proper prime powers。
取单parentcell1单位mode e_(1,m)(x)=e(mx)1_(1,2)(x)，norm_dx=1。
它和 usual profile e(m(x−1))相等，因m为整数。其exact响应为

    H_N* e_(1,m)=R_flat g_m，
    g_m(x)=Σ_(2≤q<N,q∤m) Λ(q)/q·e(mx/q)1_(q,2q)(x)，1<x<N。 (1)

q∣m项精确被(I−P_q)删掉；其余q/phase/prefactor不另改。
定义R_N(m)=||H_N*e_(1,m)||²_dx。原du normalized源N^1/4a_Ne_(1,m)
和其响应比率恰为同一个R_N(m)，所以(1)未换实际norm。
所有有限N,m的g_m是有限piecewise smooth/BV；q、2q、N都是整数，
cutoff只在unitcell端点跳变。R_flat减mean后仍是有限BV，乘a_N回u后属于
Dlog与actualΓ operator域。**此合法域事实不付款响应Γ能量。**

本稿证明一个安全显式常数：

    R_N(m)≤10^7 log⁴(2+min(N,|m|))，ALL N≥4、ALL m∈Z\{0}。 (2)

这是单parent的**basis diagonal响应**；不称ALL cell/profile的G2。

## 2. 一个dyadic q块：完整moving index interval

写Q=2^ℓ，ℓ≥1，定义固定coefficients

    a_q=Λ(q)/q·1_(q<N,q∤m)，Q≤q<2Q，
    g_Q(x)=Σ_(Q≤q<2Q)a_q e(mx/q)1_(q,2q)(x)1_(1,N)(x)。

其support在[Q,4Q]∩(1,N)，端点都是整数。固定x时active q恰为

    [Q,2Q)∩(x/2,x)，

的一段整数index interval；q<N、q∤m的holes已按a_q=0处理，不改变interval性质。
不把这个x-dependent cutoff从积分中删除。

对长度Q的固定index row，设D_Q为标准binary dyadic tree中的全部blocks，
从singletons到整row。任意index interval可由≤2(ℓ+1)个互不相交的这些blocks覆盖：
按左右边界逐层取完整subtree；每层至多两个。每个q在全部D_Q中恰出现ℓ+1次。
逐点complex Cauchy后，将cover中的block sum平方上界为全部blocks之和，得

    |g_Q(x)|²≤2(ℓ+1)Σ_(B∈D_Q)|Σ_(q∈B)a_q e(mx/q)|²，
    x∈[Q,4Q]∩(1,N)。                               (3)

(3)保留每block的实际phase及全部q cross；只取安全upper，未设cross为零。

## 3. 原MV实线gap、自然2π规范及全block质量

distinct q,q′∈[Q,2Q)的cycles-frequency m/q满足

    |m/q−m/q′|=M|q−q′|/(qq′)≥M/(4Q²)。

原MV Cor2的angular frequency为2πm/q。对长3Q的[Q,4Q]积分，
global error2π/δ_angular在cycles规范为1/d_cycles，所以

    ∫_Q^(4Q)|Σ_(q∈B)a_q e(mx/q)|²dx
      ≤(3Q+4Q²/M)Σ_(q∈B)|a_q|²。                 (4)

起点Q只给coefficient单位phase；singleton B直接由3Q diagonal处理。
原件/π与无限域核查见primary-hilbert-formulas-and-domain-audit.md。
这里每个N与q-block都是有限sum，无预合并m/q碰撞，因为单m固定时q↦m/q严格不同。

将(4)代(3)，每q出现ℓ+1次；用ℓ+1=log(2Q)/log2≤2log(2Q)，得

    ||g_Q||²≤32 log²(2Q)(Q+Q²/M)A_Q，
    A_Q=Σ_(Q≤q<2Q)|a_q|²。                         (5)

这是完整moving-cutoff费，包含binary覆盖和全block和的两个log。
不能只对某个固定index interval套MV后，免费宣称(5)。

## 4. Mean projection、整数截点与低frequency抑制

R_flat对每unitcell是g↦g−∫cellg，contraction。
g_Q在每个开unitcell内的导数只把coefficient替为

    a_q′=(2πim/q)a_q。

cutoff q、2q、N都在整数，故没有in-cell jump或额外distribution derivative；
只使用broken H¹导数，不声称g_Q在全line H¹。
同一(3)/(4)证明用于a′，并且Σ|a_q′|²≤4π²M²/Q² A_Q。
每unitcell的mean-zero Poincaré常数为1/π²（cosine/sine Parseval，首非零频率π），故

    ||R_flat g_Q||²≤min(1,4M²/Q²)
                        ·32log²(2Q)(Q+Q²/M)A_Q。    (6)

该Poincaré不要求cell两端值匹配；所有endpoint jumps留在原BV/Γ域记录中。
R_flat也保持本块support在[Q,4Q]∩(1,N)，因为support界是unitcell界，
outside cell的input与mean同时为零。无half-cell泄漏。

全部properpowers费用由旧546的自含Chebyshev ψ(X)≤4(log2)X付款：

    A_Q≤[log(2Q)/Q²]Σ_(Q≤q<2Q)Λ(q)
        ≤8 log(2Q)/Q。                              (7)

这里Λ(q)²≤log(2Q)Λ(q)，Λ始终为完整von Mangoldt；q∤m与strictN只减少(7)。
合并(6)/(7)，令z=M/Q。elementary

    (1+1/z)min(1,4z²)≤6min(1,z)，z>0，

于是

    ||R_flat g_Q||²≤1536 log³(2Q)min(1,M/Q)。         (8)

Q≤M给highmode块费；Q≫M给实际mean projection抑制。负m只改变phase共轭，
每一估计由M=|m|控制，未遗漏负mode。

## 5. 全dyadic q/cross合成与明确常数

g_m=Σ_(Q=2^ℓ,2≤Q<N)g_Q。每个x属于至多3个[Q,4Q]，
R_flat保持该support，所以逐点Cauchy保全部跨Q的complex cross，给

    R_N(m)≤3Σ_Q||R_flat g_Q||²
           ≤4608 Σ_(Q dyadic,2≤Q<N)log³(2Q)min(1,M/Q)。 (9)

没有把每块当正交，也没按全部q直接triangle损失sqrtN。
令K=min(N,M)。若M≥N，直接求和给右侧sum≤32log⁴(N+2)。
若M<N，置L=floor(log₂M)。Q≤M的部分同法≤32log⁴(M+2)。
tail Q=2^(L+t)、t≥1，M/Q≤2^(1−t)，且

    Σ_(t≥1)2^−t=1，Σ_(t≥1)t³2^−t=26，
    (a+t)³≤4(a³+t³)，a=L+1≥1。

故tail≤216log³(2M)≤1728log⁴(M+2)。合并可取

    Σ_Qlog³(2Q)min(1,M/Q)≤1760log⁴(K+2)。

4608·1760=8,110,080<10^7，证明(2)。
M=1、N=4包含在这些界中；高M≥N后费停止于logN。
全部常数绝对，未留source-dependent阈值、浮点误差或未付maximal partial sums。
本binary+MV是有限实际row的直接推导，不通过数值矩阵认证。

## 6. 最后necessary门裁定与不能消费的全profile结论

原norm、adjoint、全q/properpowers、movingcutoff、child端点、broken derivative、
Poincaré、binary blocks和跨dyadic support都闭合。(2)是actual response，
比盲收localspacing certificate更具体，排除了用该single-parent单mode响应的
超polylog增长作当前必要费反例的尝试。

但是basis Gram diagonal小，不能自动控制其全部off-diagonal。
任意parent/profile叠加时，不同m/q的exactcollision/nearcollision与不同parent的共同children
仍须按同一source保全部cross；(9)的support重叠3只用于当前一个parent、固定m的q-blocks。
它不把任意m/profile的重叠控制为3，也不产生ALL R_a∩Dlog的G2。
actualΓ始终为fullzeroextension2θ′；本稿没有给输出Γ价格或Γrelative全算子norm。
双pole/wholecount/成长全height/core/Ξ均不由(2)付款。

因此这是停止后的**最后来源necessary响应核验，零轮**。
不再延伸singlemode参数，不重开C021或以它建立新合同；无独立全joint输入时，
root按既定source规则退出此来源列表。合法fulljoint/Γrelative逃逸保持open，
不把盲certificate坏族或本basis上界扩大成G2证明/反例或Goal方法类完成。
