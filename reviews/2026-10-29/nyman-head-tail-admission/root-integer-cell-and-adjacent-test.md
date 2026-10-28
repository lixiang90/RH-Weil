# 实际Nyman整数cell范数比较：准入前根计算

2026-10-29；G20261027/runtime1793085111，原0c4f。前thetaRR来源0的metadata actual6a7bb0e/tree8aa2782e/parentcee6174已独立GitHub ref/commit/tree核且初始clean，不重推。上一turn是来源／校勘／归档进展，非数学输入；本次不顺读theta后章，先作一个已形成的实际比较，不预建C056/593。

## 1. 同一实际Hilbert域及本门的问题

采用081–083的rho_n(x)={1/(nx)}∈L²((0,∞),dx)。它不是原Weil物理源r=e^(u/2)f的另一个同名函数，也不是Möbius Green的L²域；不能借本正Gram直接代表完整Weil型。

对coeff b∈C^N，g_b=Σb_n rho_n。若A(b)=Σb_n/n=0，则g_b(x)=0于x>1；在y=1/x及整数cell[m,m+1)上，

    g_b(1/y)=−Σb_n floor(m/n)。

故first-M-cell head就是H_M(b)=Σ_(m≤M)|Σb_n floor(m/n)|²/[m(m+1)]，其余全线能量不能丢。这里没有把周期mean约束Σb_n=0与A=0混同。

**独立实物／可判门／净后果：** 真实integer-dilation arithmetic floor场，而非新未知几何q；用明确邻差检验能否把fullGram以N-independent常数支配于短physical y-window headGram。若该失真和允许head成长的必要范围未被最强旧支付，它能改变NB norm-only head证书的选择；但不直接给targetχ的距离上／下界或RH。若082/083/096–111等已有更强直接后果则old0止，不再调vector/degree/rate。

## 2. 两项邻差：完整精确计算

N≥3，n=N−1，取g_N=rho_N−(n/N)rho_n。A=0而Σb=1/N，后者意味着它**不是087 mean-zero affine约束的tangent**，不能越域消费。

记tilde g_N(y)=g_N(1/y)，P=Nn。它以P为period、|tilde g|≤n/N。首period内，j=0,…,n−1：

    y∈[jN,(j+1)n): tilde g=−j/N，
    y∈[(j+1)n,(j+1)N): tilde g=(n−j)/N。

每block的∫|g|²dy/y²=(n−j)/(N³(j+1))（j=0的零段单独无奇点）。于是每1≤J≤n都有

    ∫_0^(JN)|tilde g|²dy/y²=(N H_J−J)/N³，
    ∫_0^P=(N H_n−n)/N³。

P以后的tail≤(n/N)²/P=n/N³。因此

    [H_n−n/N]/N² ≤ ||g_N||² ≤ H_n/N²。

First-N-cell head（y≤N+1）精确是1/[N(N+1)]：仅cellN−1、N有贡献。这给full/head=logN+O(1)，无需ζ二阶矩、RH、零点或数值。若短窗上界Y_N=N^(1+o(1))且Y_N≥N+1，用相邻JN夹住也得head/full→0；若保至P~N²，本vector的首period已捕获1−O(1/logN)的full能量，所以不能拒绝所有成长head。

## 3. 三项修正：付清087 tangent域

为保两条约束，另明确构造N≥6的

    h_N=(n/N)rho_n−2rho_N+((N+1)/N)rho_(N+1)
       =−g_N+((N+1)/N)g_(N+1)。

Σb_n/n=0且Σb_n=0；不能把它无声替换成两项原式。对1≤k≤K=floor((N−2)/2)，整数multiples未互相交叉，真实pulses为

    [k(N−1),kN): tilde h=−(N−1)/N，
    [kN,k(N+1)): tilde h=(N+1)/N，

此前其余gap为0。每pulse能量正好2/(kN²)，故1≤J≤K：

    ∫_0^(J(N+1)) |tilde h|²dy/y²=2H_J/N²，
    ||h_N||²≥2H_K/N²。

全局fractionalparts∈[0,1)而正coeff和与负coeff绝对和都为2，故|tilde h|≤2。以上早段Y=K(N+1)~N²/2后的tail≤4/Y=O(N^-2)，给更强完整式

    ||h_N||²=(2logN+O(1))/N²。

截止N+2、以及cutoffX=N+2的firstXcells截止N+3，head能量都为2/N²（N≥6下一pulse未开始）。所有Y_N=N^(1+o(1))、Y_N≥N+3的physical heads仍为o(full)。令v_N=N h_N/sqrt(2logN)，则fullnorm²→1、firstXhead=1/logN→0；support x≤1/(N−1)给v_N弱趋0。这同时展示bounded-Dirichlet-coefficient h的失真，以及growingcoefficient归一化的unit energydefect，不把两个量词混同。

尤其须扣旧082的目标对齐：z_n=<rho_n,χ>=(logn+1−γ)/n，故

    <h_N,χ>=(1/N)log(1−1/N²)=O(N^-3)。

坏方向的Σb response恰0，对χ的coupling极小；归一化后是O(N^-2/sqrtlogN)。这里仅否定uniform full≤C shorthead全方向norm运输，不否定某个χ最优向量恰无坏方向，不推出actual affineoptimizer leakage或RH距离lower。原095/098强调response/target alignment的选择因此仍有效，不能拿本test打未核的basecross。

## 4. Möbius-support嵌入与旧域对照（待独立核）

若N−1,N,N+1均squarefree，cutoffX=N+2时三项都在087的interior reciprocal support。旧QT fullVandermonde可把此h作为实际jet向量，Σb=0说明它是exact mean-zero约束的tangent；degree成长／coefficient费用不能冒作fixedR定理。需要cofinal合法N，而非twin-prime猜测。

Elementary足够：先限N≡2 mod4，三项均不被4整除；对odd prime p至多三个modp²坏类。以此progression中K_X个N计，oddp bad数≤3K_XΣ_(p odd)1/p²+O(√X)，而Σ_(p odd)1/p²≤Σ_(oddm≥3)1/m²=π²/8−1，3(π²/8−1)<1。因此有正density cofinal triple-squarefree N。此是准入域合法性，非新零点比例优化。若独立核有边界／常数误差则按实际修，不预消费。

097的general exact cellGram和104 incidence recovery是相关旧设施；111保**全部N² cellmeans**只截variance corrections，其polylog M不是这里的physical y-window长度。本test不反驳111，也不消费已因091语义纠错冻结的093SL/094SP下游。096的local-only leverage和088 far majorant是否更强已付，由本次strongest-old原稿核；不能只因名字相近或generic公式可代入就互借结论。

## 5. 当前阶段及停止

两个独占任务分别核actual全norm和最强旧，尚未根消费／不同fresh／数学准入。原cadence2/history56/latest592/formal18、manifest132保持，无新primary/query/PDF/下载/数值。本门是一次actual test，不是恢复已停μ增长／theta／graph／Sonin参数。完整Weil的Γ/contact/properpowers/双pole、sameprimitive/principal/mixed与dangerouscorecross/成长Ξ未由NB head norm支付；whole4/5负惯性UPPER保持，Goalactive/open/noteligible。
