# 根affine对照：同一χ的两列实际candidate

2026-10-29；C056一个数学迭代，原始范数8380／强旧8264稿已root全文读，当前reused norm handle另核本affine对照到独占新文件。此前strongold正确警告裸h_N几乎正交target，本稿不把那个generic方向冒作optimizer失败，而给一个同χ的具体candidatepair；待不同fresh/root结算。

## 1. 可用的经典算术输入

记M(t)=Σ_(n≤t)µ(n)。525§2已消费经典无条件M(t)=O(t exp(−c sqrtlogt))，这里仅作固定输入，不优化无零区域或零点比例。Partial summation给

    m1(X)=Σ_(n≤X)µ(n)/n=M(X)/X+∫_1^X M(t)/t²dt。

该经典界使∫_1∞|M(t)|/t²绝对收敛。在σ>1，1/ζ(σ)=σ∫_1∞M(t)t^(−σ−1)dt；支配收敛及ζ在1的pole给∫_1∞M(t)/t²=0。因此m1(X)→0，且只为本head行为使用，不当RH强度的critical Mertens上界。

## 2. 实际boundary-corrected trial

取N≥6、X=N+2。定义有限实算术coefficients

    a_n=µ(n)−X m1(X)1_(n=X)， n≤X，
    R_X=χ+Σa_n rho_n，χ=1_(0,1)。

A=Σa_n/n=m1−m1=0。对整数m≤X，

    Σ_(n≤X)µ(n)floor(m/n)=Σ_(k≤m)Σ_(d|k)µ(d)=1。

故reciprocal残差R_X(1/y)在y<1为0，在integercells1≤m<X为0，仅cellX上等于X m1(X)。first-X-cells的完整head能量精确为

    E_head(R_X)=X/(X+1)|m1(X)|²→0。

原periodic boundary mean一般不是0（Σa不必−2），不偷称满足087额外affine约束。也不猜R_X本身的fullnorm是否趋0。

## 3. 双约束扰动及完整basecross

取已独立付清的v_N=N h_N/sqrt(2logN)，其Σb/n=Σb=0、fullnorm²→1、first-Xhead=1/logN。两个候选

    F_N^+=R_X+v_N， F_N^−=R_X−v_N

都仍是同χ的finite Nyman residual，并保A=0以及base的既有periodmean。更强地，head内R_X只在[X,X+1)非零，v_N只在第一pulse[N−1,N+1)非零，二者支撑分开。所以

    E_head(F_N^+)=E_head(F_N^−)
      =X/(X+1)|m1(X)|²+1/logN→0。

这不是只看generic source norm，而是同target实际affine误差的精确head读数。Full Hilbert parallelogram不需要知道basecross：

    (||F_N^+||²+||F_N^−||²)/2
       =||R_X||²+||v_N||²≥||v_N||²→1。

于是liminf_N max(||F_N^+||²,||F_N^−||²)≥1，且至少一列的fullnorm不趋0（其limsup energy≥1）。这是两个明确candidatepair的证书，不假已选出哪个固定sign。无需exact-real-sign判定、没有实际Gram数值运行；若未来要single selector须另列误差算法而不自动授预算。

## 4. 净后果和边界

本门已处理这一pair的joint signed basecross：parallelogram消去cross，非把cross假小。准确否定的是“某一列explicit candidate的短head残差趋0就保证其完整残差趋0”，或全方向N-independent head→full norm运输。它**不**证明NB最优distance不趋0，不排实际target/response-aligned Feshbach对另一列成功；同χ存在坏近似列与RH完全相容。

这组affine base只在原NB A=0类上，无087 prescribedmean=0断言；087 growingMöbius约束内只消费h_N tangent的uniform Loewner反测（合法tripleSF域另证），fixedR／受限jetcoeff／allparabolic／allmeans保留。Y_N=N^(1+o1)的更一般sourcehead必要loss来自h_N norm稿，但不自动把本R_X head公式推广到大于X的窗口。

原Weil Γ/contact/properpowers/双pole、du/Dlog与sameprimitive/mixed没有新正性身份。此是actual arithmetic shorthead证书的定量严格边界，不是RH反证或完整Goal第3门；whole4/5负惯性UPPER与关键瓶颈未改。仅C056当前这一数学迭代，不续selector、Mertens率、head长度或另一source候选。
