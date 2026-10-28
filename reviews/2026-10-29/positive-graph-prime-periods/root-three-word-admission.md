# 正边图的三闭路实际反测：准入前推导

2026-10-29；同G20261027/runtime1793085111/原0c4f；不续591或Deninger来源。上一00924c8发布条件先核，当前唯一cadence1/history55/latest591/formal18未动。此为已实际形成的不同具体比较，先扣078/079/565/566/404最强旧，尚未授权C055/592或消费新定理。

## 实际对象、独立输入和首门

取有限或可数有向图，边有严格正长度l(e)、严格正活动权a(e)，闭路长度相加、活动权相乘。对primitive cyclic edge-word γ（模cyclic rotation、不是proper power）及k≥1，定义正周期测度

    ν_G=Σ_(γ primitive)Σ_(k≥1) l(γ)a(γ)^k δ_(k l(γ))。

要求它在(0,∞)为Radon；不预设全图ordinary trace、normal determinant极限或self-adjoint adjacency。目标正素数轨道measure为

    ν_ζ=Σ_pΣ_(k≥1) (log p)p^(-k/2)δ_(k log p)，
    S={klog p:p prime,k≥1}。

这是完整Weil型中的正prime-power部分，不是Q_W本身；全部Γ/contact和indefinite双pole仍由原560/577保留，不在图里免费获得。活动权p^(-1/2)是中心化约定，可用edge gauge搬权但不能改变闭路activity product。

已执行的root反测：在同一strongly connected component选基于v的闭路A、基于w的闭路B，长度a=log p、b=log q（p≠q）；任意连接路径S:v→w、T:w→v，c=l(S)+l(T)≥0。三个实际闭词为

    W1=S T A，W2=S T A A，W3=S B T A，
    lengths c+a，c+2a，c+a+b，
    activities zx，zx²，zxy，x=a(A)，y=a(B)，z=a(S)a(T)。

v=w时S/T空、c=0,z=1合法。若三长度都在S，N=e^(c+a)>1、pN、qN均为素数幂。N与pN迫N是p的幂，qN即合数且含两素数，矛盾。对任意c∈[0,C]，M=ceil[e^C p max(p,q)]、δ=1/(16M)给统一max dist(length_j,S)>δ：若各距≤δ，取近邻整数素数幂N_j，|N2−pN1|、|N3−qN1|≤4Mδ<1，故均exact0，仍矛盾。近邻N1>1，不误用单位1。

因此独立输入是正闭词拼接及素数唯一分解；最便宜门是三个词/有限δ、primitive-power系数和可数Radon域。成功将排**同一SCC内不同prime方向**的exact正edge-additive realization，并给cofinal bounded-return/nonvanishing-activity必要费用；不是所有flow或全部signed/higher几何不可能。

## 真正待核的cofinal升级

若G_j的共同ν_j在D′/vague正测度意义趋ν_ζ，并保两个marked prime闭词A_j/B_j（长度exact a,b或有控趋近）活动权≥η>0，则不应还能有同时总连接长度c_j≤C及连接activity z_j≥η的返回路径。必须支付延迟→∞或通信weight→0的相应subsequence费用。

不能把based word贡献直接写成l(W)a(W)：W可能是γ^k，真实coefficient为l(γ)a(W)。Root已形成修复：若a(W)≥η³、l(W)∈[a,L]，设d=log2/8。

* l(γ)≥d/4时，原word处贡献≥dη³/4。
* l(γ)<d/4时，利用其repeats在prime-free固定区间[d,2d]内的阶梯；因对应j≤k，a(γ)^j≥min(1,a(W))≥η³，区间总mass≥dη³/2。

这样可用一个固定非负compact smooth h，h=1于[d,2d]及[a,L]内距S≥δ的闭集、h=0于S邻域，给ν_j(h)≥dη³/4，而ν_ζ(h)=0。此步需独立核repeat计数/局部有限/近似长度版本，不能借primitive简单性漏掉高重复/细分edge。η可先减至≤1，活动权允许无上界。主证先exact marked lengths，不为近似长度领第二预算。

## 强旧与停止条件

079的prime-local正常全纯det极限、565有限双向Markov、566未减primejump闭域/ordinary trace、404真实adelic周期分别先扣；若它们或其它exact旧分解已蕴含全SCC/任意countable正图及cofinal通信结论，记旧0不造新轮。不是由“旧门未直接覆盖”授预算，而是以上实际有限词/primitive补偿测试已执行并可判。

Exact可用a=m logp、b=n logq同理；若allclosedword支持S，SCC内只能一个prime标签。原νζ在logp的atom会迫出现primitive lengthlogp（不许k次根产生非整数prime norm）；是否需要此消费另核。没有闭路的one-way edges可保；full graph connected不等于SCC混合。

合法逃逸须保：cofinal connector长或weight消失、diffuse prime atom（无单个marked activity lower）、signed cancellation、非edge-additive/依无限past的roof、一般flow/singular/higher/Hodge、另载体和非normal重整。此测度只是prime部分，exact分解为prime SCC不自己排全部后续global analytic continuation或RH。Commensurable有限域lengths均nlogq，不触此独立prime反测；可用2×2全1/2 rankone转移/统一delay logq作非空positive mixing对照，不能冒称非平凡曲线完整ζ或Weil正性。

主Goal/core/whole4/5UPPER保持。先两具体独占审：全word/primitive/Radon证明；最强旧/实际角色/逃逸净比较。若新后果确有且前件闭，才准一个C055数学迭代及不同fresh；若断点准确止，不调p/q/图/来源救题。
