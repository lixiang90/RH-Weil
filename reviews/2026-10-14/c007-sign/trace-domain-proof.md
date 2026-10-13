# C007：光滑源给实际裸角迹的核平滑与迹类域

2026-10-14；主代理独立证明，起始HEADbbbd54c。
不同组织Plancherel/Sobolev逆审已通过，最终限定消费见535及宏观完成审计。
不是复用C006未付的角强收敛；本证明给真正S1收敛。

## 1. 可核的源平滑引理

物理H=L²((0,∞),dx)，L=1_(0,1)。记F_r的核为2cos(2πrxy)，
r≥1，F_r=r^-1/2U_-logr F；K_r=LF_rL。
对fixed g∈Cc∞(R)，A_g=∫g(t)U_tdt，有

    ||A_g L F_r L||1 ≤ C_g(1+log r)/sqrt r.             (A)

C_g只含固定支持和有限多个源导数；不称whole源L²质量界。
g不须矩零，反演g和A_g*亦适用。

在输出作unitary log变量v=log x，输入仍为physical y∈(0,1)。
核准确为

    b_r(v,y)=2∫_0∞ g(v+z)e^-z/2 cos(2πr e^-z y)dz.

∂_v^j只落到g^(j)，没有频率r的导数损失。
取c>0使supp g⊂[-c,c]，输出v≤c。

near-cutoff −c≤v≤c，用t=v+z改变量后一次非驻相，低z端给phase ry；
g在上端消失，所需∂v^j kernel皆被
C_g min(1,(ry)^-1)控制。y平方积分≤C_g/r。

v<−c时原source全在积分内，写
2e^(v/2)∫_-c^c g(t)e^-t/2 cos(2πr y e^(v−t))dt。
非驻相t积分给（包括所需j）

    |∂v^j b_r(v,y)|≤C_g e^(v/2)(1+r y e^v)^-1.

所以对v∈[v₀,−c]，v₀=−log r−c−d（fixed d>0），
kernel及一阶输出log导数的HS范数平方≤C_g(1+log r)/r。
在J_r=[v₀,c]上，B_r:L²(0,1)→H¹(J_r)因此为HS，
范数≤C_g sqrt((1+log r)/r)。
H¹(J_r)→L²(J_r)的嵌入为HS：Neumann cosine谱给
Σ_(n≥0)(1+(πn/|J_r|)²)^-1≤C(1+|J_r|)。
HS×HS使输出J_r部分S1范数≤C_g(1+log r)/sqrt r。
不要求在J_r端点施加Dirichlet条件。

深输出v<v₀，全source已落入L。cos Taylor给rank-one核

    2Σ_(k≥0)(−1)^k(2πr)^(2k)/(2k)!
       ·e^((2k+1/2)v)·y^(2k)·I_k,
    I_k=∫g(t)e^(-(2k+1/2)t)dt.

输出rank norm=e^((2k+1/2)v₀)/sqrt(4k+1)，
输入rank norm=1/sqrt(4k+1)，|I_k|≤||g||1e^((2k+1/2)c)。
代入v₀后全部r^(2k)消去，仅留r^-1/2及有factorial分母的可和rank列。
深输出S1范数≤C_g r^-1/2，完成(A)。

不同组织逆审核给更短的中段HS证明：令x=e^-z，
b_r(v,y)=2∫_0¹g(v−log x)x^-1/2cos(2πrxy)dx。
对每个v，cosine Plancherel直接给
∫_(y>0)|b_r(v,y)|²dy=r^-1∫_0¹|g(v−log x)|²dx/x≤||g||²/r。
∂v只换成g′，因此有限J_r上的H¹ map HS费用直接≤C_g sqrt(|J_r|/r)。
上述深输出rank-series与自然H¹嵌入仍必需；这个证明没有把无限log长度删掉。

## 2. actual K_p与完整h(K_p)的源迹类

实际

    F_p=(1−1/p)Σ_(n≥0)q^n U_-nlogp F−qU_logp F,
    q=p^-1/2, K_p=LF_pL.

第n个low核是F_(p^n)，其实际振幅不能额外再乘q^n。
(A)使Σn A_g L F_(p^n)L在S1中收敛，因Σn(1+nlogp)p^-n/2<∞。
反向low核F_(1/p)光滑；其low算子S1，A_g有界，不影响结论。
故

    A_g L K_p ∈S1,
    A_g L h(K_p)∈S1,
    h(K)=K(I−K²)^-1,

后式只用已付||(I−K_p²)^-1||<∞。
这是一项fixed smooth source的新实际域输入，不从K_p非HS变成HS。

## 3. ambient identity及合法循环迹

真实overlap O_p=P_p+L+F_pLF_p−I。
双cutoff block公式给精确ambient身份

    O_p=Φ_p(h(K_p)),
    Φ_p(T)=L T L F_p H+F_p L T L F_p H F_p.

这里low算子按L嵌入，h(K_p)与K_p交换；可逐块直接验证而不取任何无限角迹。
令X=Lh(K_p)L F_pH，则O_p=X+F_pXF_p。

对real smooth g，A_g normal，F_p A_g*=A_g F_p，Z=A_g*A_g与F_p交换。
上一节给A_gX A_g*为S1；对反演源同样，
A_gF_pXF_pA_g*=F_p A_g*X A_g F_p亦为S1。
因此**两半source迹都单独合法**，可以循环，得到

    E_p(g)=Tr(A_g O_p A_g*)
          =2ReTr_low[h(K_p)L Z H F_p L].                (B)

Mp=LZH F_pL对fixed smooth g还可由有限boundary smooth源核确认S1；
以上证明更直接支付源夹心的域，不只定义一个局部trace。
复源可分实/虚部；actual密度为实偶，混合项抵消。

## 4. bare与完整return的真正分离

534的Schatten插值给K_p∈S_r(r>2)，特别K_p∈S3。
C_p=h(K_p)−K_p=K_p³(I−K_p²)^-1∈S1。
Φ_p(C_p)因bounded factors为ambientS1，其source迹合法。
bare Φ_p(K_p)也有(A)给的两半sourceS1域。
故实际E_p=bare B_p+return C_p是(B)中**合法ordinary trace分离**，
不是从完整TC反推任意角cutoff的迹收敛。

Σn A_gL F_(p^n)L的S1收敛允许bare第一个因子逐项取trace；
Mp中的Fp级数则在operator norm收敛，TC×bounded允许第二因子逐项。
对原冻结source边界rectangle，每个finite Fourier pair有普通核积分。
这些pair在L1源核中绝对可和（含共振列的L1 O(p^-m)），
所以actual bare源核由该double-series确定，给正log共振的消费身份。
需分别核pair L1界，不能把此最后一句当对所有word的泛许可。

## 5. ambient TC修正给source TC及连续核

对任意ambient D∈S1，fixed bounded sourceU上的
g↦Tr(A_g D A_g*)为sourceS1型，norm≤|U|||D||1。
若D=Σs_j|f_j><h_j|作nuclear展开，
V_f:g↦A_gf为HS，||V_f||HS²=|U|||f||²；
每个source rank诱导项V_h*V_f为S1，再绝对求和即可。

它的source kernel为Tr(DU_(t−u))，由D∈S1与unitary scaling强连续而连续有界，
幅度≤||D||1。因而L1有界的窄bump source在这个修正上有统一O1费用，
不需要carrier o(1/R)或假定每个裸余项sourceS1。
这将direct稿的正log裸窄源渐近接到actual E₂，只在(B)和pair核域逆审通过后升级。
