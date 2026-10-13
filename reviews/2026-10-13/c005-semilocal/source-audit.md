# C005：真实S={∞,2} Sonin来源审查

2026-10-13；只写本审查，不修改STATE/cadence，不单独计研究轮。
已按AGENTS恢复README、STATE/check/show、C005及D20261013F。

## 原件、编号与实际定理

一级原件为[Connes–Consani–Moscovici, arXiv2310.18423v2](https://arxiv.org/html/2310.18423v2)，v2日期2024-05-04；[PDF](https://arxiv.org/pdf/2310.18423v2)30页。本地`tmp/pdfs/c005/2310.18423v2.pdf` SHA256为`8bc197642ee9ca4f2393b6cbfd3db292be6a315ce76ad61bfb845d9fedb47f2e`。视觉核印页21、23、24；页20–24和相关§4.1–4.4逐页文本核读。HTML部分proposition标题未渲染，编号以PDF为准。

PDF定位：Definition4.4/Proposition4.5（页20–21）给local Sonin及有限p的不变生成器；Definition4.5/Proposition4.6（页21–22）给semilocal Sonin和θS；Proposition4.7（页22–23）给Fourier互换及mixed pairing；Theorem4.6（页23，theorem和proposition各自计数，故与Proposition4.6同号）给hilbertian同构；Proposition4.8（页24）给共同entire函数空间。§4.8明确该entire空间的内积依赖S。

没有读到`Tr(ϑ_S(g)Π_Sϑ_S(g)*)`与完整Weil型的有符号比较定理，也没有这种trace-class身份。PDF全篇检索`trace class/trace-class/orthogonal projection`均0，**这一检索仅辅助定位**；相关全文核读才支持上述范围判定。Intro把trace比较作为策略，未将其写为本文已证定理。

## 对象、物理范数及scaling

记`H_S=L²(X_S)^{K_S}`，`X_S=(R×Q2)/{±2^n}`；原件(42)的`w_S`是物理Hilbert空间到multiplicative `L²`的unitary识别。使用`U_S=F_μw_S`转为`L²(R,ds)`时，scaling是unitary的实频率乘子。原件(48)、(52)涉及不同weighted measures的unitary，不能把其中相同函数的identity map说成原范数上的unitary。

在`H∞=L²(R)_ev`取`U_t=ϑ(e^t)`，即`U_t f(v)=e^(-t/2)f(e^(-t)v)`；`w∞`下是`k(y)↦k(y−t)`。令`a=log2,q=2^(-1/2)`。原件(57)–(58)精确给

    U_S θ_S U_∞^(-1) = multiplier b(s),
    b(s)=1−q e^(−ias).

把target通过unitary `J=U_∞^(-1)U_S`识别回H∞，则

    J θ_S = B,  B=I−qU_a,
    ||θ_S f||_S²=||Bf||∞²
                =(1+q²)||f||²−2q Re<f,U_a f>.

因此θS是bounded invertible，但不是unitary。其严格统一范数界为

    (1−q)||f||≤||θ_S f||≤(1+q)||f||.

scaling互换`θ_S U_t=U_t^S θ_S`是真的，由B与U_t相交换；这不表示scaling保持固定cutoff的Sonin空间。

同时(47)给`Jη_S=(B*)^(-1)`，Proposition4.7(iii)的`<θ_Sf,η_Sg>=<f,g>`是**mixed**配对，不是`<θ_Sf,θ_Sg>=<f,g>`。有限2-adic生成器`σ2=ε0−ε1/2`通过quotient正好产生B，不能只因有限处local Sonin维数为1就将全半局部projection作tensor简化。

## 真实正交投影与正trace：本审查的独立推导

固定Sonin cutoff为1；这与C005完整型的源支持`λ=√(13/5)`是两个参数。令`S`为实位Sonin cutoff1的真实orthogonal projection，`R=RanS`。Theorem4.6给

    J S_1(X_{∞,2},α) = B R.

BR因B可逆而closed。它在物理范数下的orthogonal projection是

    P2 = B S G^(-1) S B*,
    G=(S B*B S)|_R,
    (1−q)² I_R≤G≤(1+q)² I_R.

这里`G^(-1)`只在R定义，公式通过S嵌入环境空间。证明：`V=B|_R G^(-1/2)`满足`V*V=I_R`、`RanV=BR`，故`VV*=P2`。不能将`B S B*`、`B S B^(-1)`或semilocal cutoff projections的乘积冒充P2。

令`A_h=∫h(t)U_tdt`，`h∈Cc∞(R)`，与C004使用**同一source**及同一scaling/involution。C004原trace给`A_h S`为Hilbert–Schmidt。由于B与A_h相交换，

    A_h B S = B A_h S ∈HS,
    T2(h):=Tr(A_hP2A_h*)
          =||A_h B S G^(-1/2)||HS² <∞.

这是独立证明的真实positive trace，不是本文原文未写出的定理引用。所有cross产品也为trace class；因此源Gram是合法的。

对任意source h还有（仅粗范数运输界）

    ((1−q)/(1+q))² T∞(h)≤T2(h)
       ≤((1+q)/(1−q))² T∞(h),
    T∞(h)=||A_hS||HS².

证明直接用B及G^(-1/2)的上下奇异值界。这没有首素数signed主项，也不削弱完整Weil正性前件。

## 同源差的精确表达与尚未支付的一步

记`H=B*B=(1+q²)I−q(U_a+U_(-a))`，`W_h=A_h*A_h`。因为H、W_h相交换，且`AB S`为HS，

    T2(h)=Tr_R[G^(-1) S H W_h S],
    T∞(h)=Tr_R[S W_h S],
    T2(h)−T∞(h)
       =Tr_R[G^(-1) S H(1−S) W_h S]
       =−q Tr_R[G^(-1) S(U_a+U_(-a))(1−S)W_h S].

最后的cross算子**作为整体**是TC：它等于`S H W_h S−G S W_h S`，两项TC；不擅称各个未夹紧的ambient块TC。该表达精确保留physical orthogonalization费用；抽象Hilbertian同构本身没有将其算成prime显式公式。

两源`h1(t)=h(t+a/2),h2(t)=h(t−a/2)`满足

    A1=U_(-a/2)A_h, A2=U_(a/2)A_h,
    T2_ij=[[s2, t2],[conj(t2),s2]],
    s2=Tr(A_hP2A_h*),
    t2=Tr(U_(-a) A_hP2A_h*), |t2|≤s2.

任意不同u,v的patch亦可用`Tr(A_iP2A_j*)`而不假设对角相同。合法trace循环来自HS乘积，不来自P2与scaling相交换。

对C005冻结域，C004已证的完整same-source差保持

    QW−T∞ = −E∞ − w2Swap,
    w2=log2/√2,

pole为0且真实primepower只有2。故真实半局部桥现在精确是

    QW−T2 = −E∞−w2Swap−(T2−T∞).

要支付首素数非紧费用，必须审这个physical correction的同源bilinear分布及L²压缩主项；需要它在冻结域贡献所需`−w2Swap`（并付剩余signed误差），不能从positive Gram或bounded invertible B推出。本文未给这个主项或signed比较；本审查也未证明它不存在。

特别，先前530排除了**固定实位trace的诱导紧修复**，并不证明`P2−S`诱导的source trace二次型是紧。仅从B有限平移、Gbounded inverse亦不能判紧。故不可用530免费关闭这一真实半局部路线。

## 真实半局部Fourier的cutoff regularity：独立核查

本节继续主代理提出的候选；不是宣称原文已给此regularity定理。全文相关§4及kernel定位只取得上述intertwining与multipliers，未定位下述lacunar kernel/非HS结论；不能据此宣告世界优先权。

通过同一unitary J，实际Fourier为

    F2=B F∞ B^(-1).

它仍是unitary selfadjoint involution，因为`F∞ U_a=U_(-a) F∞`，故`B*B`与F∞相交换。以下在`L²(R_+,dx)`采用even函数的unitary restriction，实位Fourier核为`2cos(2πxy)`；若使用even函数但内积`2dx`，核系数会对应除以2，结论不变。

先保留一般prime p，`q=p^(-1/2),a=logp`。B的operator-norm几何展开给

    Fp=(I−qU_a)Σ_{n≥0}q^n U_(-na)F∞
      =(1−q²)Σ_{n≥0}q^n U_(-na)F∞−qU_aF∞.

因此在正x,y上的distribution kernel为

    Kp(x,y)=2[(1−1/p)Σ_{n≥0}cos(2πp^nxy)
                  −(1/p)cos(2πxy/p)].

两式不是不同Fourier规范。`q^n U_(-na)F∞`的kernel里`q^n p^(n/2)=1`，所以operator系数衰减与distribution kernel不衰减同时发生。不要把lacunary sum说成逐点或L²收敛。

令`P=1_(0,1)`（Sonin cutoff固定1），`C=P Fp P`。将最后算子式截到n≤N得smooth有限核compact算子C_N，并有精确可用尾界

    ||C−C_N||≤(1+q)q^(N+1).

所以C为compact。该尾估计是在operator norm；不证明kernel在L²收敛。

另一方面，取任意非零非负`ρ∈Cc∞(2/5,3/5)`，定义**smooth紧内部**测试

    Φ_N(x,y)=ρ(x)ρ(y)Σ_{k=0}^N cos(2πp^kxy).

所有x,y都远离0及cutoff边界；无需用在x=1边界非smooth的product-only测试。作z=xy变量，其权函数为

    r1(z)=∫ρ(x)ρ(z/x) dx/x,
    r2(z)=∫ρ(x)²ρ(z/x)² dx/x.

二者smooth紧支持在`(4/25,9/25)`。频率差`|p^n−p^k|≥(1−1/p)p^max(n,k)`（n≠k），而r1、r2的Fourier变换任意阶快速下降，故所有非对角频率的double sums均有**独立于N**的总界。cos²的高频项和`p^(-1)`单低频项亦有独立总界。于是

    ||Φ_N||L²((0,1)²)²
       = (N+1)/2 · (∫ρ² dx)² + O(1),
    <Kp,Φ_N>
       = (1−1/p)(N+1) · (∫ρ dx)² + O(1).

distribution配对的无限series对每个Φ_N可绝对求和，且O(1)统一；非零leading coefficient来自ρ非负非零。若Kp在该局部有L²代表，Cauchy–Schwarz只允许pairing为O(√N)，与上式线性增长矛盾。因此**远离0的内部核亦非L²，C不是Hilbert–Schmidt**。此结论既不说C非紧，也不把其转写成E2源二次型非紧。

最后核`||C||<1`。`B*=I−qU_(-a)`和`(B*)^(-1)=Σq^n U_(-na)`都保持`RanP`：每个term只把support`[0,1]`压缩到`[0,p^(-n)]`。所以`η=(B*)^(-1)`低support不仅有inclusion，且`ηRanP=RanP`。从F∞与B*B相交换可得

    B* Fp = F∞ B*.

若f及Fp f均在RanP，则h=B*f非零且h及F∞h均紧支持。h∈L²紧支持因而L¹，其usual even Fourier变换entire，并在实轴开尾区间为0；解析唯一性给h=0矛盾。因此P与Fp P Fp没有公共非零range。

compact C满足`||C||≤1`；若norm=1，compact性给unit vector f∈RanP达到norm，由`||P Fp f||=||f||`及Fp unitary知Fp f亦在RanP，矛盾。故实际cutnorm严格小于1；证明不给未经计算的数值gap。

## 来源任务结论

原件提供的θS的确只是hilbertian stability；但与已知实位trace输入合用，能够独立构造真实物理orthogonal projection及finite positive trace。因此“原文没有新trace定理”本身不是停工理由。可消费的准确接口是本文件P2/G及correction公式；尚未付的是其算术signed主项与误差，宏观完整正性/最低态/增长支持瓶颈仍未改变。

此外，实际Fp的cutoff是**compact、norm<1、非Hilbert–Schmidt**；这是核常数与support均已独立复核的新regularity候选。不能从nonHS跳到E2符号、fullQW负谱或source费用。唯一下一动作：主数学审查及不同组织逆审核该regularity、P2和TC循环；E2 signed桥仍保持未付。无待处理下载或计算进程。

主代理结算收据：原v2 PDF已按同一SHA保留于
`literature/background/connes-consani-moscovici-prolate-2310.18423v2.pdf`（本地忽略）；
[source-receipt.json](source-receipt.json)记录版本与核读范围。
后续唯一动作从STATE的C005最后一轮恢复，不再从本历史审查的核验任务句恢复。
