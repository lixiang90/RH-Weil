# 固定v2上游审查：加权评价、实际局部迹质量与全线尾

2026-10-28；`/root/scalar_upper_tail` 当前独占稿。恢复README／STATE、check→show、G20261027／原0c4f、最新AJ、actual scalar规则与唯一zero-mean-upper-proof-gate。现场C051已completed／预算耗尽；执行中root将AJ同一次不同用途的固定来源首门承接为C052 reviewing、预算1，本腿已实际读该合同，不另开预算、不编号／计轮、不改STATE／Git／cadence。本腿只核6.2 upper／tail及6.3所需接口，不消费6.3 localization或(6.11)的最终结论。

**上游限定通过。** 原稿667–782行的加权评价(6.7)、实际localized mass(6.8)与全线tail可闭合。它们仍不单独证明zero-mean little-o；(6.10)等局部化步骤须与另一独占腿／root对齐。本稿没有审6.4 sharp lower、6.5／§7，亦不把同章receiver strong limit与588源operator的strong resolvent混同。

## 1. 原件、实际阅读与对象字典

主原件为bramble_trace，*Sharp Schatten asymptotics and Sonin trace localization for semilocal Fourier cutoffs*，rStation固定v2（2026-10-16），本地 `literature/local/2026-10-28-core-source-location/bramble-trace-rstation-2-v2.md`，61862bytes，raw／LF SHA256 `541098314b2ddc5f8645babf82086e87d16c46188268cbc7ed6cfc1f98720058`，本次现场重核一致。

实际读§6定义510–523、upper所需667–782；沿其明确引用核§1 cosine／log／Fourier定义21–57、§4 weighted commutator kernel355–375。只核必要原输入：既有585的共同Sonin向量稿中原norm／Burnol记录，以及本地Burnol0208121v1 PDF6 Theorem8及紧邻结构定义。后者117262bytes／原SHA `1890a3867e745c342be3a70eeb2948c673bfb644fc4f392f9302d0b9c96acc3b`，本次只读固定原件，没有下载、搜索、外部新文献或数值。

源f是physical log卷积源，F(t)=∫f(y)e^(-ity)dy；f∈Cc∞先固定，F为Schwartz。receiver Mellin Hilbert为L²(dt/(2π))。原S_X是560实际Π_X的同一酉表示，非source form operator。D_X(t)=∏_(p≤X)(1−p^(-1/2−it))，S_XH=D_X S₀H只为range等式，不是未加权等距。

在固定arch空间采用 `||h||_X=||D_Xh||_2`。此finite-X norm与原norm等价但粗条件数可随X爆炸。映射U_X:h↦D_Xh从这个加权空间到actual S_XH才是等距；若用原arch Hilbert识别，其式为M_D G_X^(-1/2)，G_X=S₀|D_X|²S₀。因此下文没有丢弃全Gram逆。

## 2. 固定arch unit-ball的complex growth

需先核原稿670的原norm评价界，而不是把一条fixed-vector增长当unit-ball界。令K=C₁为L²(0,1)上的固定cosine压缩、c(x)=2cos(2πx)、g=(I−K²)^−1c。K compact且||K||<1：若norm1被达到，则某非零函数及其cosine变换均有compact支撑，解析唯一性排除之。所以g的固定norm有限。

g=c+K(Kg)，且Kg由同一compact cosine积分给出；二者均延拓为even entire，Taylor系数满足 |c_j|≤C(2π)^(2j)/(2j)!。对v=g、Kg，定义M_v(s)=∫₀¹v(x)x^(−s)dx的亚纯延拓，逐项得Σc_j/(2j+1−s)。在半整数vertical sides和高度可比的horizontal sides上，各pole距离有下界，Σ|c_j|收敛，故两个M_v在这些矩形边界一致有界。

本地Burnol Theorem8给固定gap1 completed结构函数。其ψ₊−ψ₋=−2Cg，拆分cosine Mellin积分于1，得到与原稿一致的

    E(s)=γ(s)[1+M_(Kg)(s)]−γ(1−s)M_g(1−s),
    γ(s)=π^(−s/2)Γ(s/2).

这里E的组合entire来自同一Theorem8，不把两项的个别gamma极点当消失。矩形边界上Stirling／reflection给exp(CRlog(R+2))界，整函数最大模原理移到盘内。Completed de Branges双线性kernel由E(s)E(z)−E(1−s)E(1−z)除以s+z−1给出（固定归一化因子只进C）；分子在z=1−s处消零。以Cauchy导数界控制可去商，除回γ(s)γ(z)所得raw kernel仍为同阶增长，因为reciprocal gamma的增长也是exp(CRlog(R+2))。其Hermitian conjugate diagonal是evaluation norm平方，故

    sup_(|z|≤R)|h(z)|≤exp(CRlog(R+2)) ||h||₀,   R≥2.

所有C只依固定gap1空间；没有调用待证cofinal trace上界或原稿未审的raw section O(1/t)。这段所需Burnol角色为completed结构与等距kernel，不能仅由Γ的点值猜raw评价。

## 3. (6.7)的X一致性确实去掉粗条件数

反射坐标h⁺(z)=h(−z)属于上半平面Hardy空间；arch conjugation为C₀h⁺(t)=u∞(t) overline(h⁺(t))，u∞(z)=γ(1/2+iz)/γ(1/2−iz)。这对应cosine变换及复共轭，C₀h⁺也属于同一Hardy空间；boundary |C₀h⁺|=|h⁺|。

D_X⁺(z)=D_X(−z)为上半平面bounded analytic multiplier。对Im z≥1，逐因子

    |D_X⁺(z)|≥∏_(p≤X)(1−p^(−3/2))≥ζ(3/2)^−1.

所以D_X⁺h⁺和D_X⁺C₀h⁺均为H²函数，且boundary norms都等于||h||_X。Hardy评价给上侧 |h⁺(z)|≤C||h||_X/√(2 Im z)。反射关系给下侧同界乘|u∞(z)|；u∞在Im z≤−1解析，并在z=t−i上≤C(1+|t|)。因此h⁺(z)/(z+2i)在strip两条边界Im z=±1上统一≤C||h||_X。

第2节的arch增长及每fixed-X norm等价给strip内exp(C|z|log(|z|+2))增长，暂有X依赖prefactor。取0<a<π/2，乘exp[−εcosh(az)]；在闭strip Re cosh(az)=cosh(a Re z)cos(a Im z)为正。先对**每个fixed X／ε**令矩形长度→∞，vertical sides被双指数衰减压掉，再令ε↓0。边界constant本来独立X，故得到的内部界同样独立X；无须声称矩形极限对X一致。

于是strip内 |h⁺(z)|≤C|z+2i| ||h||_X；strip外由Hardy／gamma比继续控制，最终

    sup_(|z|≤R)|h(z)|≤C_R ||h||_X,
    C_R=exp(CRlog(R+2)),                         (6.7)

其中C独立有限素数集。若只写||h||₀≤m_X^−1||h||_X而不做strip步骤，就没有支付(6.7)；本核没有采用这种替代。

## 4. Taylor singular values与actual localized mass (6.8)

令J_T为加权arch空间到L²([-T,T],dt/(2π))的restriction。Cauchy估计及截去degree≥j项给rank≤j近似的operator norm误差

    s_(j+1)(J_T)≤C_R sqrt(T/π) (T/R)^j/(1−T/R).

U_X是上述真实等距，因此其localized singular values同时≤1和M_Xs_j(J_T)，其中M_X=∏_(p≤X)(1+p^−1/2)。已付PNT／Euler t=0渐近给log M_X=(2+o1)A，L=logX、A=√X/L；没有进行零自由区优化。

取T=L、R=√X/L⁴、n=ceil((4+ε)√X/L²)。有log C_R=O(√X/L³)=o(A)，nlog(R/T)=(2+ε/2+o1)A。首n项平方和≤n，其后几何尾≤exp(−εA/2)。因此对actual receiver投影

    limsup_(X→∞) (L²/√X) Tr(1_[-L,L] S_X 1_[-L,L])≤4.    (6.8)

这是同Hilbert localized trace；dt/(2π)已在restriction norm中，不再给实际迹乘2π。n的leading4来自log M_X和Taylor指数，固定kernel／Hardy归一化常数只给o(A)，不改变4。上界同时证明该localized operator确为trace class，不由未知ρ可积性循环假定。

## 5. 全线tail：reduction、commutator与measurable weight

在physical receiver中，A_X=P F_X P为自伴contraction。S_X为P与F_XP对应的Sonin交空间投影；在此子空间A_X²=I，且它reduces A_X，所以0≤S_X≤A_X²。这里不是把Euler乘子D_X当酉，也不是source operator inequality。

转Mellin后，A_X是带反射的weighted Hardy Hankel block。反射将F(t)换成F(−t)，但|t|>T与下面的偶粗权均保持。对任意bounded measurable localization multiplier，正operator比较及kernel的Tonelli积分给相应HS upper；不需要不适用于sharp cutoff的trace-class差分式(4.4)。

具体地，commutator [Π,M_(u_X)]的difference-quotient kernel平方含

    |u_X(t+v)−u_X(t)|²/v².

两个Hardy blocks的输入域正交，所以weighted HS平方和由这个nonnegative kernel积分准确给出。全部有限primepowers的phase导数与arch Γ满足

    |φ_X′(t)|≤C(√X+log(2+|t|)).

prime部分用Σ_(p≤X) logp Σ_(k≥1)p^(−k/2)≤C√X；proper powers保原logp而非多乘k，Γ部分原digamma的log界。对|v|≤1，difference≤min(2,Ca_t|v|)，a_t=√X+log(2+|t|)；对|v|>1用2。分割|v|=1/a_t后，内积分≤Ca_t，得到

    ||M_(F 1_|t|>T) S_X||²_HS
       ≤C∫_(|t|>T)|F(t)|²[√X+log(2+|t|)]dt.              (Tail)

不需φ_X″的一致界，不删Γ／素数幂，也不借weighted trace-class差分的smooth-weight假设。f先fixed、F Schwartz，取T=L后右边为o(√X/L²)。常数及起点允许依f；对moving f／support／频率族不宣称一致。

## 6. 可交接口与未消费范围

本腿交付(6.7)、(6.8)、(Tail)，及由其直接给出的fixed-f通用上界limsup L²T_X[f]/√X≤4||F||∞²。通用上界没有k改善，仍不足判root的r₀′/r₀比值；新的zero-mean upper必须再付6.3的局部化(6.10)→(6.11)。本稿不把“weighted polynomial trial集中”冒作整个ρ_X的mass集中。

所有对象为同一actualΠ_X／完整Gram逆及physical complex log源。普通迹域沿560／585已付Cc∞接口，不将仅L²源免费当HS；Q_W、双pole和其符号不属于本上游upper的证明对象，也没有在完整目标中被删掉。root消费scalar test时仍须使用原完整q₁>0／q₀>0，不能由正trace upper本身推出Weil正性或负性。

无新web／下载／PDF渲染／数值，无STATE／Git／cadence改动。本腿不是一个独立数学轮，不自授589或额外合同；是否原来源门闭合及计轮由root对齐另一腿、fresh和最强旧后决定。Goal原完成门仍open，whole4/5负惯性UPPER／primitive／完整signed核心责任不因本上游而改变。

## 输入版本绑定

- `goals/contracts/C052-sonin-zero-mean-upper-and-scalar-normalization.md`：3776bytes；LF SHA256 `9f41e0397bc079d63d9ce7264e7ae4166f29f3864cb74683e3ea692b291de2bc`。
- `reviews/2026-10-28/sonin-scalar-normalization/next-zero-mean-upper-proof-gate.md`：2490bytes；LF SHA256 `d1ad41054ccf0843223ee552ab3dcfc9d671c90913a59d53dc0b32c8a343a069`。
- `reviews/2026-10-28/fixed-test-lower/common-sonin-vector-and-polynomial-domain.md`：16348bytes；LF SHA256 `dcdf8e91b408423e3647f116f8bd72e040feaf24cf80f9b92db30d776398af85`。
- `notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md`：9263bytes；LF SHA256 `9c2e6cd5a9eae269ad04b332699c21eec7403a230f9557afa8b895c45d4228d3`。
