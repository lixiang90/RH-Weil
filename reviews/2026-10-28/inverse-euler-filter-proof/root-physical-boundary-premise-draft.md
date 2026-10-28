# Root独立前件核：同actual Riesz的物理边界路线（待终稿/fresh）

2026-10-28；C053同一数学迭代。当前moment作者提出合同已允许的等价物理边界证明，替代原示意的三Fourier波goodset；对象a2/ψ/H0/g/norm不变。本稿独立核条件链，**尚非root结算**；须读作者终稿及不同新审查后解除等待。未使用bump辅助的Fourier渐近作前件，也不以消息代terminal原件。

## 1. 实际projection与临界Riesz，不使用未付raw高频式

Positive-halfline cosine C f(x)=2∫₀∞ f(y)cos(2πxy)dy为L²酉自伴。固定a=2，E=1_(0,a)，K=ECE在L²(0,a)上compact/selfadjoint，||K||<1：若compact contraction取到norm1，则相应非零f及Cf都compact支撑，整解析唯一性排除。故I−K²、I±K均bounded invertible。K:L¹(0,a)→C^j[0,a]和K²:L²→C^j对每fixed j有界。

对real s∈(1/2,3/4]，令q_tail=1_[a,∞)x^-s∈L²；M_a=kerE∩kerEC为actual gap-a Sonin，区别于合同的arch M=M_1，且M_a⊂M_1。Cosine Mellin系数

    χ(s)=2(2π)^(s−1)Γ(1−s)sin(πs/2),
    C(x^-s)=χ(s)x^(s−1), χ(s)χ(1−s)=1, χ(1/2)=1。

积分恒等式可用正阻尼取极限/Dirichlet积分，应用时先保s开区间；不声称两个非L²幂函数是L²向量。

取w_s∈L²(0,a)解

    (I−K²)w_s=χ(s)x^(s−1)−Kx^-s。

这里x^(s−1)在(0,a)为L²；x^-s只在L¹，**仅**经K使用，不误代成L²输入。写

    w_s=χ(s)x^(s−1)+r_s,
    r_s=(I−K²)^−1[−Kx^-s+χ(s)K²x^(s−1)]。

F_s=q_tail+E K w_s−C E w_s在head为0，EFourier条件由上述方程为0，故F_s∈M_a。差F_s−q_tail属于RanE+RanCE⊂M_a^perp，因此F_s=Projection_(M_a) q_tail，非假定projection公式。对x>a，F_s=x^-s−C(Ew_s)。

## 2. L²临界极限与实际evaluation识别

Bracket输入在C¹[0,a]收敛；bounded resolvent给r_s在L²收敛，r_s=f_s+K²r_s再给C¹收敛。s↓1/2时

    r_0=−(I+K)^−1Kq，q=x^-1/2∈L¹(0,a),
    w_0=q+r_0∈L¹(0,a)。

对x>a，由full cosine power identity精确改写

    F_s(x)=χ(s) C(1_[a,∞) y^(s−1))(x)−C(E r_s)(x)。

第一项为收敛oscillatory尾；一次integration by parts用s−1<0及∫_a∞ y^(s−2)<∞给C/x，uniform s∈[1/2,3/4]。第二项用r_s的uniformC¹和sin在0为0同样≤C/x。于是F_s→F_0在L²(a,∞)，其中

    F_0(x)=x^-1/2−C(Ew_0)(x)，x>a；head置0。

对每fixed h∈M_a，<h,F_s>=∫_a∞ h(x)x^-s dx为合法raw Mellin值；旧Sonin raw/completed解析性保证其在s=1/2的连续延拓。L²极限故识别F_0为真正raw evaluation Riesz k_(a,0)，不是另造形式section。Inner product取第一槽linear，F_s/F_0为real，归一化G₂(0)=||k_(2,0)||²。旧585非零evaluation给该k不为0。后续H0以原585的大gap平滑嵌入合同arch M_1，不将gap-a projection冒作G_X所在的P。

C(Ew_0)为compact L¹函数的entire cosine transform，x^-1/2在positive轴analytic。因此F_0在a的右侧有analytic延拓到a邻域；若所有边界jets0，则analytic identity使其在x>a全零，与k非零矛盾。于是存在fixed有限m≥0及c≠0，使F_0(a+z)=cz^m+O(z^(m+1))。Realness给右侧小邻域定号；无须知道m或假定m=0。

## 3. 固定卷积边界与all-n矩

Unitary log Wk(y)=e^(y/2)k(e^y)支撑y≥log a，右边界同有限阶m。H0=ψhat G₂是ψ*Wk的Fourier；故

    h=g*ψ*Wk,
    hhat=ghat H0,
    L=log a−δ/2−1。

h=0于y<L；g、ψ光滑compact与Wk∈L²保证h∈C∞∩H^n对每finite n，并在L左侧所有derivatives为0。对0<ε小，所有卷积贡献的Wk边界距离均在[0,ε]，所以定号无cancellation。仅取两个bump边界距离s₁,s₂∈[ε/4,ε/3]的矩形，则Wk剩余距离在[ε/3,ε/2]，两个positive explicit bumps分别≥c exp(−C/ε)，面积~ε²，得到

    |h(L+ε)|≥c ε^(m+2)exp(−C/ε)。

Taylor积分余项及Cauchy–Schwarz给每n≥1

    |h(L+ε)| ≤ ε^(n−1/2) ||h^(n)||₂ /
                         [(n−1)!sqrt(2n−1)]。

ε=1/n对所有大n合法。Stirling下界将(n−1)!²与n^(2n−1)合成exp(4nlogn−O(n))，固定ε^(2m+4)只添O(logn)，所以

    ||h^(n)||₂² ≥exp(4nlogn−C′n)。

Plancherel（dt/(2π)）精确识别左侧为J_n^g。该链若在作者原稿/fresh中核闭即付C053唯一newlemma；不借receiver作source、不对h应用完整Weil型或其pole域，不丢real/complex规范。

## 4. 根消费待办

待作者逐项严写projection、条件幂函数积分、C¹/L²极限及actualevaluation识别/finite边界阶、卷积定号和Taylor常数，并绑定原输入；再与运输稿actualmoment符号一致。独立新审者须核上述全链，不能仅核J lower⇒ratio。Fourier saddle支持稿即使成立也非这条物理链的依赖，不自动多闭一个更强结论。Core/whole/Goal与cadence均未在本draft结算。
