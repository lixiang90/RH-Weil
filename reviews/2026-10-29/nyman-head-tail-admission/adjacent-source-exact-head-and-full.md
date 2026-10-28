# 相邻 Nyman 源：首段与全线范数的实际比较

2026-10-29；限定支持推导，供root与另一strongest-old稿消费。本稿不建C056/593、不计轮、不改STATE／cadence／Git；不使用RH、ζ零点位置、second moment或数值作为证明。这里的N是feature整数截断，不是ζ零点高度、physical窗口或算术几何level。

## 1. 同一真实feature、范数和首段

采用081–083的实际空间

    rho_n(x)={1/(nx)}，x>0；H=L²((0,∞),dx)。

对b∈C^M，令g_b=Σ_(n≤M)b_n rho_n，A(b)=Σb_n/n。令y=1/x，则

    U_b(y):=g_b(1/y)=A(b)y−Σ_(n≤M)b_n floor(y/n)。

当A(b)=0时，g_b在x>1处为0，并且U_b在每个integer cell[m,m+1)常数。精确首段为

    E_M^head(b)=∫_(x≥1/(M+1))|g_b(x)|²dx
       =Σ_(m=1)^M |Σ_(n≤M)b_n floor(m/n)|²/[m(m+1)]。

这是083 reciprocal sawtooth在moment-zero子空间上的直接版本。全范数为∫₀∞|U_b(y)|²dy/y²。各finite源合法，不先用sampling Gram或formal Dirichlet coefficient norm代替它。

以下用h_j=Σ_(k=1)^j1/k表示harmonic number，避免与首段Hodge量混淆。所有区间端点的fractional-part跳点不影响Lebesgue积分。

## 2. 两项源的精确首段

设N≥3、n=N−1，取

    g_N=rho_N−(n/N)rho_n。

其A=1/N−(n/N)/n=0，且g_N在x>1/n为0。原y坐标中的响应为

    U_N(y)=(n/N)floor(y/n)−floor(y/N)。                 (1)

它以P=Nn为周期。由下述(3)的period内取值可得|U_N(y)|≤n/N；也可用(1)给出的U_N∈N^(-1)Z，再结合fractional parts给的−n/N<U_N<1得到该界。

在首段0≤y≤N+1，仅两个integer cells非零：

    U_N=n/N  在[n,N)，U_N=−1/N 在[N,N+1)。

N≥3保证N+1≤2n；因此精确得到

    E_N^head(g_N)
      =(n/N)²(1/n−1/N)+(1/N)²(1/N−1/(N+1))
      =1/[N(N+1)]。                                   (2)

两项系数之和却是1/N，不是0。因此不能把这个原始两项源直接叫087“exact boundary mean-zero”约束的tangent方向。该域区别在§5用一个必要三项修正解决；(1)–(2)本身仍完全成立。

## 3. 两项源全范数：按同一周期作精确积分

对j=0,...,n−1，第j个block[jN,(j+1)N)内有

    U_N(y)=−j/N，       jN≤y<(j+1)n；
    U_N(y)=(n−j)/N，   (j+1)n≤y<(j+1)N。             (3)

这是floor函数的实际交错：jN≤(j+1)n≤(j+1)N，因为j≤n−1。对j≥1，block积分为

    (j/N)²[1/(jN)−1/((j+1)n)]
      +((n−j)/N)²[1/((j+1)n)−1/((j+1)N)]
    =(n−j)/[N³(j+1)]。

j=0的第一个区间上源恒0，第二项单独积分也给n/N³，无需在0代入1/y。故对每个1≤J≤n，

    ∫₀^(JN)|U_N(y)|²dy/y²
       =(N h_J−J)/N³。                               (4)

取J=n，首个完整period的能量是h_n/N²−n/N³。剩余全尾由实际pointwise bound付清：

    0≤∫_P^∞|U_N(y)|²dy/y²
       ≤(n/N)²/P=n/N³。

于是有明确无条件夹界

    (h_(N−1)−(N−1)/N)/N² ≤ ||g_N||²_H
                               ≤h_(N−1)/N²。         (5)

特别地

    ||g_N||²_H=(logN+O(1))/N²，
    ||g_N||²_H/E_N^head(g_N)=logN+O(1)。                (6)

这里全量级和leading constant均由原函数积分支付；不是从082的κ连续性猜一条quantitative modulus。

## 4. 同一公式允许的首段增长范围

只消费(4)的直接量词后果，不引入第二个候选或rate优化。若所保留的reciprocal区间为0<y≤Y_N、Y_N=N^(1+o(1))，令J_N=ceil(Y_N/N)。当N充分大时J_N≤n；取上一个完整block作upper即

    ∫₀^Y_N |U_N|²dy/y² ≤h_(J_N)/N²。

而h_(J_N)=o(logN)、(5)的全能量约为logN/N²，因此该窗口对这个源仍不能给统一的全范数支配。若保留至P=N(N−1)，则(5)说明这个源的相对尾为O(1/logN)。这**只**是本源的窗口性质：不证明任意coefficients的N²窗口已足够，也不给operator domination upper bound。

## 5. 同时保两个scalar约束的必要三项修正

为核087的periodic-boundary约束tangent，按root新形成的实际修正取N≥6

    k_N=((N−1)/N)rho_(N−1)−2rho_N+((N+1)/N)rho_(N+1)。

它严格满足

    Σb_n/n=0，Σb_n=0，
    k_N=−g_N+((N+1)/N)g_(N+1)。                         (7)

因此它是moment-zero源，也是087中周期boundary mean约束不变的tangent方向；这两种scalar条件不同于405的全部noncompact P_an关系，不能互换。

令K=floor((N−2)/2)。对1≤j≤K，倍数满足

    j(N−1)<jN<j(N+1)<(j+1)(N−1)。

U_k(y)=k_N(1/y)在这个早段中只出现彼此分离的两块pulse：

    U_k=−(N−1)/N，   j(N−1)≤y<jN；
    U_k= (N+1)/N，   jN≤y<j(N+1)，

其余此前区间为0。每对pulse的精确能量为

    ((N−1)/N)²[1/(j(N−1))−1/(jN)]
     +((N+1)/N)²[1/(jN)−1/(j(N+1))]
       =2/(jN²)。                                    (8)

所以Y=K(N+1)处的完整早段能量严格等于2h_K/N²。全局还有一个比triangle bound更直接的尾界：正coefficients之和=2、负coefficients绝对值之和=2，fractional parts都在[0,1)，故|U_k(y)|≤2。由此

    2h_K/N² ≤ ||k_N||²_H
                ≤2h_K/N²+4/[K(N+1)]
                ≤(2h_K+16)/N²。                      (9)

最后一步用N≥6时K≥N/4。因K=N/2+O(1)，这个同一三项源其实给出

    ||k_N||²_H=(2logN+O(1))/N²。                       (10)

其highest feature是N+1。前N+1个integer cells对应0<y<N+2；N≥6时它们只包含第一对完整pulse，故

    E_(N+1)^head(k_N)=2/N²，
    ||k_N||²_H/E_(N+1)^head(k_N)=logN+O(1)。             (11)

若为保endpoint而把coefficient cutoff取M=N+2，首M个cells至N+3仍不遇第二对pulse，所以E_M^head(k_N)=2/N²。这个有限事实不自动认证087的Möbius-support限制：要进入其full Vandermonde span，还须实际µ(N−1),µ(N),µ(N+1)均非零。本稿未证明这种cofinal triple存在，不借091已冻结的一般shared-gcd sieve；root可另核这一域前件。在不限制Möbius support的两scalar共同子空间，(9)–(11)已对所有N≥6无条件成立。

## 6. 这个norm反测实际否定什么

对任意moment-zero coefficient子空间，可定义首段Gram与081原full Gram。它们各finite维均正；例如首段floor矩阵T_(mn)=floor(m/n)为lower triangular、diagonal1，所以没有把head的有限存在性判错。

但是若要求对所有该N源有共同constant C

    ||g_b||²_H≤C E_N^head(b)，

则(6)迫C≥logN+O(1)，不可能有N无关upper。同样，(11)在同时Σb/n=Σb=0的全coefficient子空间中也否定uniform constant。这里是**必要loss lower**，不是最佳domination常数的sharp asymptotic upper；其它源可能要求更大费用。

同一三项源还给可核的归一化对照

    v_N=N k_N/sqrt(2logN)，
    ||v_N||²_H→1，E_(N+1)^head(v_N)=1/logN→0。          (12)

由于moment-zero且全部n≥N−1，v_N在x>1/(N−1)恒0。故对每个fixed f∈H，Cauchy–Schwarz给< v_N,f >→0：全范数可留O(1)能量于x趋0，而首段看不见这份全量。

这个证书只说明缺少tail／alignment时首段norm不能替换完整Gram。它**没有**证明target χ的optimal residual不趋0，没有证明087实际optimal coefficient在该坏方向有何分量，没有给特定Möbius试向量的RH等价tail下界，也没有排除有费成长、full Gram或target-aligned Feshbach方法。081 NB criterion、082 gap与alignment区别、083完整tail责任均保留。

本稿未构造完整Γ/contact/properpowers/双pole的新的正Weil身份；ordinary NB feature的两个scalar约束不等于same arithmetic primitive关系。主Goal关键primitive/principal/sections/mixed、signed corecross/成长Ξ及whole4/5负惯性UPPER未由此关闭。是否已被项目更强旧推论蕴含、是否能改变实际方法选择及是否进入数学预算，留给strongest-old与root准入判断；不因本文件存在或证明自含便计轮。

## 7. 实际使用范围

081的fractional-part/Mellin/Hilbert约定、082§§1–2的Gram规范、083§4的reciprocal sawtooth已读。087 exact mean-zero tangent／endpoint/Möbius-support前件按root指出的域问题明确区分；本稿只使用其已给约束类型，不认证未核tail结论。数学证明全部为上面floor与Lebesgue积分。无web／新primary／PDF／下载／数值；只写本独占稿，不改其它files或计轮。
