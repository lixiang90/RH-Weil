# 593. Nyman短窗的真实范数损失与同目标affine缺陷

2026-10-29。[T/R] C056原norm／强旧／affine及不同数学fresh均terminal/root全文消费，按一个完整数学迭代统一结算。原件和精确fresh输入快照见[本轮目录](../reviews/2026-10-29/nyman-head-tail-admission/)。本文证明一个实际RH等价模型中的短窗替代边界，未给新的Weil正性或RH反证，不主张世界优先权。

## 1. 实际域、目标和两个不同约束

沿081–083，H=L²((0,∞),dx)、rho_n(x)={1/(nx)}、χ=1_(0,1)。对finite b，g_b=Σb_n rho_n，A(b)=Σb_n/n。A=0时，y=1/x中

    g_b(1/y)=−Σb_n floor(y/n)，
    ||g_b||²=∫₀∞|g_b(1/y)|²dy/y²。

定义physical head P_Y(g)=∫₀^Y|g(1/y)|²dy/y²。First-X integercells恰是P_(X+1)，不是X个Dirichlet coefficients或Mellin频率截断。若A=0，则该head为Σ_(m≤X)|Σb_n floor(m/n)|²/[m(m+1)]。

另一个约束Σb_n=0是087 periodic-mean的homogeneous tangent，不能与A=0或405全部noncompact Pan混同。这个Hilbert模型不是原物理r=e^(u/2)f、du/Dlog的完整Weil型。

## 2. 全方向norm运输的log必要损失

N≥6、X=N+2，实际三项源

    h_N=((N−1)/N)rho_(N−1)−2rho_N+((N+1)/N)rho_(N+1)

同时满足A=Σb=0，且

    P_(X+1)(h_N)=2/N²，
    ||h_N||²=(2logN+O(1))/N²。                         (1)

证明是elementary integer pulses。K=floor((N−2)/2)以前第k对不交pulse在[k(N−1),kN)、[kN,k(N+1))，振幅−(N−1)/N、+(N+1)/N，每对能量=2/(kN²)。首K对给2H_K/N²；全局|h_N(1/y)|≤2付余下tail≤4/[K(N+1)]=O(N^-2)。First-X cells只含第一对，得到(1)所有leading常数。

所以对该合法源空间全部方向的full≤C_N·head支配必须C_N≥logN+O(1)。这不是最佳C_N的upper/sharp结论，别的方向可能更坏。取v_N=N h_N/sqrt(2logN)，则fullnorm²→1而head=1/logN→0；support x≤1/(N−1)还给v_N弱趋0。

对任意先指定／自适应Y_N≥N+3且log(Y_N/N)=o(logN)的窗口，令J=ceil(Y_N/(N+1))，早段精确积分2H_J/N²支配其head，因而P_(Y_N)(h_N)/||h_N||²→0。N²量级窗口对本源会留住1−O(1/logN)的能量；不由此授任意b的N² domination。

原two-term rho_N−(N−1)rho_(N−1)/N的Σb=1/N，不直接属087tangent；其精确周期计算仅作初始控制，不能借错域消费三项结论。

## 3. Growing Möbius空间的非空合法域

若N−1,N,N+1全squarefree，X=N+2时三项都在087的interior Möbius support；QT的full-rank Vandermonde把h_N实际放入该空间，Σb=0保证tangent归属。这个使用不控制jet坐标费用，也不覆盖fixedR或受限coeff类。

合法N无界且有正下密度：限N≡2 mod4，排oddp至多三个modp²坏类，unionbound的相对坏比例≤3Σ_(p odd)p^-2≤3(π²/8−1)<1，余项O(√T)。所以没有twin-prime／RH前件；亦不复活091错误generalδ筛。这里只需正下密度及cofinal，不另断自然密度极限存在，不作ζ零点比例研究。

## 4. 不能从generic坏方向跳到χ最优误差

旧082的target coupling给精确

    <h_N,χ>=N^-1 log(1−N^-2)=O(N^-3)。                 (2)

坏方向的boundary response也恰0。因此(1)不证明NB最优distance有正lower，不证明actual087 affineoptimizer漏能量，更不反驳RH。若需只靠短窗残差验收某个candidate，可直接作下面同χ反测而不假basecross小。

## 5. 两列具体算术candidate：head都趋0，full至少一列不趋0

记m1(X)=Σ_(n≤X)µ(n)/n，取

    a_n=µ(n)−X m1(X)1_(n=X)，
    R_X=χ+Σ_(n≤X)a_n rho_n。

A(a)=0。由Σ_(d≤m)µ(d)floor(m/d)=1，first-X cells中R_X仅在最后cell[X,X+1)为X m1(X)。经典PNT／525旧Mertens界给m1(X)→0（不是RH强度的critical估计），所以

    P_(X+1)(R_X)=X/(X+1)|m1(X)|²→0。

令F_N^±=R_X±v_N。Head内v_N与R_X的支撑分开，故

    P_(X+1)(F_N^+)=P_(X+1)(F_N^−)
      =X/(X+1)|m1(X)|²+1/logN→0。                    (3)

但全Hilbert parallelogram精确给

    (||F_N^+||²+||F_N^−||²)/2
        =||R_X||²+||v_N||²≥||v_N||²→1。               (4)

因此liminf max(fullenergy±)≥1，至少一列fullenergy的limsup≥1。两列都是明确的同χ finite residual；不须选exact sign，也没有声称运行Gram数值。此base一般Σa≠−2，不能把(3)–(4)冒作087 prescribedmean的affine反例；v_N只保base既有mean，087内仍仅消费§3合法tangent反测。

## 6. 最强旧净值与停止

082小谱不能替本physicalhead/full比较；096只有local-only finite诊断／conditionalη，097提供exact窗口公式但未给此growing向量渐近。099保全parabolic区；111保全部N² cellmeans，只截variance corrections，其polylog cutoff不是这里的physicalhead。本结果不打它们，也不消费093/094因091纠错冻结的下游。

新净值为真实双约束源的uniform shorthead必要loss、subpowergrowth失败和同χ候选pair的完整affine反测；保response/targetalignment、实际optimizer leakage、fullmetric/allmeans及有费成长修复。它只止短窗norm-only验收，不给最优距离新界或新的几何principal／sections／mixedRR。

完整Γ/contact、properpowers、双pole、sameprimitive与dangeroussignedcorecross/成长Ξ未由此关闭；whole542+555→557 leading4/5仍负惯性UPPER。Goal完整门保持open；本合同一个完整数学迭代后止，不续head-rate／degree／selector／来源队列。
