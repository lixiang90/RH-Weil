# 同一个χ的明确affine候选对：首段趋零而全残差不能都趋零

2026-10-29；执行C056当前限定支持任务，仅写本稿。原norm稿8380bytes／SHA256 e5fd028a679685b29cd567e66ec31900c01fe800163a9fc76715b9499806c43f保持冻结。本稿不结算数学轮，不改STATE／cadence／Git，不运行数值或sign选择器。

## 1. 对象、首段与已付的实际扰动

沿081，H=L²((0,∞),dx)，rho_n(x)={1/(nx)}，χ=1_(0,1)。N≥6，X=N+2。对H中函数F，记

    H_X(F)=∫_(x≥1/(X+1)) |F(x)|²dx
          =∫₀^(X+1)|F(1/y)|²dy/y²。

这是first-X integer cells的physicalhead，不是所有periodiccell means或原Weil型。令

    h_N=((N−1)/N)rho_(N−1)−2rho_N+((N+1)/N)rho_(N+1)，
    v_N=N h_N/sqrt(2logN)。

冻结原稿§§5–6已以实际floor/pulse积分支付

    Σ d_n/n=Σd_n=0，
    ||v_N||²_H→1，H_X(v_N)=1/logN，                    (1)

其中d_n是v_N的coefficient，support={N−1,N,N+1}。Cutoff X=N+2的首段到N+3，仍只包含第一个pulse，因为下一pulse从2(N−1)>N+3开始。这里引用这个实际domain版本，不从两项源偷推额外mean约束。

## 2. 经典Mertens输入只用于m1(X)→0

令M(t)=Σ_(n≤t)µ(n)，m1(X)=Σ_(n≤X)µ(n)/n。采用525(6)已经消费的经典无条件界

    |M(t)|≤C t exp(−c sqrt(logt))，c>0，t充分大。       (2)

不优化它、不称当前最优无零区，也不把它升级为RH临界Mertens界。这个既有输入足以给出所需极限，具体步骤如下。

Stieltjes partial summation（起点M(1−)=0）给

    m1(X)=M(X)/X+∫₁^X M(t)dt/t²。                      (3)

由(2)，M(t)/t→0，而∫₁∞|M(t)|dt/t²收敛：在大t处令u=logt，支配积分为∫ exp(−c sqrtu)du<∞。对实σ>1，绝对Dirichlet series和partial summation给

    1/ζ(σ)=σ∫₁∞M(t)t^(−σ−1)dt。

当σ↓1时，右侧可用2|M(t)|/t²支配；ζ在1有简单极，故左侧趋0，得到

    ∫₁∞M(t)dt/t²=0。

因此(3)成为

    m1(X)=M(X)/X−∫_X∞M(t)dt/t²
         =O((1+sqrt(logX))exp(−c sqrt(logX)))→0。      (4)

最后一个tail估计直接使用

    ∫_logX∞ exp(−c sqrtu)du
      =2exp(−c sqrt(logX))(sqrt(logX)/c+1/c²)。

全过程只在σ>1使用Euler inverse，并由已付的绝对积分界取σ↓1；没有在临界线上交换形式和，也没有执行新的零点比例／无零区域研究。

## 3. 真实boundary修正的affine基点

定义有限coefficient

    a_n=µ(n)−X m1(X)1_(n=X)，1≤n≤X，
    R_X=χ+Σ_(n≤X)a_n rho_n。                           (5)

于是A(a)=Σa_n/n=m1(X)−m1(X)=0，且a_1=1。每个R_X都是081原feature空间中的合法finite affine residual；全范数有限，无需预知任何zero或RH。

对y∈[m,m+1)、1≤m≤X，利用实际integer divisor identity

    Σ_(n≤X)µ(n)floor(m/n)
      =Σ_(k≤m)Σ_(n|k)µ(n)=1。

而floor(m/X)只在m=X时为1。由于A(a)=0，reciprocal残差严格为

    R_X(1/y)=1−Σ a_n floor(m/n)
      =0，              1≤m<X；
      =X m1(X)，        m=X。                          (6)

对0<y<1，χ(1/y)=0且各fractional part的linear slope也被A=0消掉，所以残差亦为0。故在整个head 0<y<X+1上，只有最后一个cell[X,X+1)非零。于是精确能量为

    H_X(R_X)=|X m1(X)|²[1/X−1/(X+1)]
            =X/(X+1)|m1(X)|²→0。                     (7)

这不是对全norm的估计；m>X的全部divisor tail仍未简化。

## 4. 同目标候选对及精确相等的head能量

取两个完全明确的序列

    F_N^+=R_X+v_N，F_N^−=R_X−v_N，X=N+2。              (8)

两者的target始终是同一个χ，coefficient分别为a_n±d_n。它们仍满足A=0及a_1±d_1=1；加入v_N不改变Σa_n，因为Σd_n=0。

在head中，v_N仅在[N−1,N+1)的两块首pulse上非零；R_X仅在[N+2,N+3)非零。两support分离，所以head mixed term**精确为0**，不用Cauchy–Schwarz损失或numeric cancellation。因此

    H_X(F_N^+)=H_X(F_N^−)
      =X/(X+1)|m1(X)|²+1/logN→0。                     (9)

全H中则不用计算未知coupling <R_X,v_N>，直接由平行四边形恒等式

    (||F_N^+||²_H+||F_N^−||²_H)/2
       =||R_X||²_H+||v_N||²_H≥||v_N||²_H。

结合(1)，得到准确的pair结论

    liminf_(N→∞) max{||F_N^+||²_H,||F_N^−||²_H}≥1。    (10)

特别至少一个**fixed sign** σ∈{+,−}满足limsup_N||F_N^σ||²_H≥1，因而那一条候选序列的full residual不趋0。不能由此声称某个预先指定sign有liminf≥1，更不能声称两个sign都失败。

因为两head能量有共同的趋零值(9)，同样有

    liminf_N max_(σ∈{+,−})∫₀^(1/(X+1))|F_N^σ(x)|²dx≥1。

这把“短窗看不见全能量”放到了同一χ的实际affine候选上，而非仅generic source norm或换target例子。

## 5. 域、成长、构造与不可偷渡的结论

**原NB合法域。** 全部coefficients是有限、明确的算术表达式。若A_N^σ(s)=Σ(a_n±d_n)n^(−s)，其完整Nyman residual仍是081的

    ||F_N^σ||²_H=(1/(2π))∫_R|1−ζ(s)A_N^σ(s)|²/|s|²dt，
    s=1/2+it。

这是同候选的全线身份；本稿用实空间证明(10)，未数值估计此积分。

**不冒087 affine mean-zero。** 基点一般Σa_n=M(X)−X m1(X)，未证明等于−2，故其periodic residual mean一般不是0。v_N只保持这个已有mean，不把它变成指定mean。这个χ-affine反测属于原NB／A=0 subclass；087上只可消费另稿已经闭合的合法tangent norm反测，不能自动把(8)纳入额外mean-zero affine base。基点a_X也一般不是0，不能偷认endpoint-preserving或Möbius-support限制；这些额外域不是(8)证明的前提。

**成长不隐藏。** v_N的三个coefficient为(N−1,−2N,N+1)/sqrt(2logN)，其ell²平方=(3N²+1)/logN，随N成长；a_X=µ(X)−X m1(X)亦非假定有界。原finite Dirichlet polynomial域允许这些系数，结论不声称在fixed coefficient norm球内仍有(10)。实际原始NB norm、coefficient norm和full-Weil du/Dlog不能相互替代。

**无需selector。** (8)是一个显式finite pair，(10)已足够否定“同candidate的首段残差趋0就必定全残差趋0”的普遍推论。本稿不选择哪一个sign、不把exact real sign判定说成已可执行；没有运行coefficient数值表、full-Gram quadrature或给出其复杂度／精度费用。若以后要求一个逐N选择的single sequence，那个有容差的实际Gram评价须另付；本门不因此续预算。

**不反驳最优distance。** 至少一个explicit candidate坏，不等于d_X=inf_c||χ+Σc_nrho_n||不趋0，也不说明actualoptimal coefficient有坏方向分量。不能从(10)升级出NB最优距离lower bound、RH反例、原Möbius基点的full误差结论或087 target-aligned optimum失败。原082 response/target alignment和全tail责任保留。

本稿是C056一个完整迭代内的支持证据，最终新颖性／同域强旧／计轮由root对齐后统一结算。完整Γ/contact/properpowers/双pole、同primitive/principal/sections/mixed及dangerous corecross/成长Ξ未由这个NB candidate比较闭合，whole4/5负惯性UPPER未改变。仅使用冻结norm稿、081/087域及525(6)旧经典界；无web、新primary、PDF、下载、数值或其它文件修改。
