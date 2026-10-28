# 590：Inverse-Euler滤波的growing moment与归一化谱逃逸

2026-10-28；C053，G20261027/runtime1793085111/原冻结0c4f。实际moment终稿13693b、transport终稿12520b与不同新fresh10261b已root全文核；本轮统一消费一个完整数学迭代。新输入是固定actual Riesz向量的物理边界/all-n矩lower及其growing-degree真实norm运输，不由旧裸零极限或两个lower相除得到。前件和版本以 `reviews/2026-10-28/inverse-euler-filter-proof/root-consumption-scope.json` 为准。

## 1. 同一实际规则与结论

沿560/585同一arch Sonin M=RanP、finite Euler B_X及完整Gram G_X=PB_X*B_XP|M。记

\[
 D_X(t)=\prod_{p\le X}(1-p^{-1/2-it}),\quad
 Q_X(t)=\sup_{h\in M,\ \|D_Xh\|_2\le1}|h(t)|^2,
 \quad d\nu_X(t)=\frac{\rho_X(t)}{|D_X(t)|^2}dt
               =Q_X(t)\frac{dt}{2\pi}.
\]

Receiver norm为dt/(2π)，physical源r=e^(u/2)bare、rhat=∫r(u)e^-itu du、原du/zeroextension Dlog及第一槽linear保持。取消外D没有取消G_X逆；P G_X^-1P不是arch P，B不当unitary。每finiteX的positive tempered和compact源配对域已付。

固定587的du norm1正bump g=c exp[-1/(1−u²)]（|u|<1），g1=g′，完整q0=Q_W[g]>0、q1=Q_W[g1]>0有限。置

\[
 S_X(r,s)=\int\widehat r(t)\overline{\widehat s(t)}d\nu_X(t),
 \quad A=\sqrt X/\log X.
\]

则本轮证明，存在ε_X≥0、ε_X→0，使全部充分大real X有

\[
 S_X[g]\ge e^{-\varepsilon_X A},\qquad
 \frac{S_X[g']}{S_X[g]}\longrightarrow+\infty.
\tag{1}
\]

旧S_X[g]→0保持，所以不是fixed positive lower。对**任意共同positive scalar**β_X，只要β_XS_X[g]→q0>0，即有

\[
 \boxed{\beta_XS_X[g']\longrightarrow+\infty.}\tag{2}
\]

因此该full-prime inverse-Euler commonweight＋matching-g scalar族不能在固定compact卷积平方g′*(g′)*上趋任何有限值，特别不能趋完整q1；不存在有限D′极限。已允许F_X成长及source inverse的nonlocal/infinite-delay，不排其它weights、高gain生成规则、signed/joint或非线性source适应。

## 2. 先扣更强旧资产

C052 upper proof的real strip步骤已经给全real t/X的Q_X≤C(1+t²)，而localization proof给每first-fixedB的|t|≤log^B X上

\[
 Q_X(t)\le\exp[(-4+o(1))A].\tag{3}
\]

两者使bareν_X→0 strongS′、S_X[g]和S_X[g′]都→0、exact校准β_X=q0/S_X[g]→∞，均是本轮先扣的强旧0。它们不决定0/0的ratio。只看原weight的最大增益、把β删去或把filtered非compact源放进未准的完整pole身份，均不能证明(2)。

已付585的算术式是uniform于|t|≤X²的

\[
 \log|D_X(t)|^2=-4A\Re\frac{e^{-it\log X}}{1-2it}+o(A),
 \quad |D_X(t)|^2\le e^{(4+o(1))A}\ (t\in\mathbb R).
\tag{4}
\]

中段与全尾各用其实际范围，不做零自由区优化。

## 3. 新的实际all-n矩下界

冻结a=2、δ=log2/4，k_(2,0)为positive-halfline cosine双gap空间K₂的raw Mellin原点评价Hermitian Riesz，G₂为其raw函数。取固定ψ(v)=Cδ exp[-1/(1−(2v/δ)²)]（|v|<δ/2）、∫ψ=1，H0=ψhat G₂。旧模板付H0非零/entire、Gevrey2 upper及全部finite t^nH0在arch M。

本轮新证存在fixed C,n0，使每整数n≥n0有

\[
 J_n^g:=\int|\widehat g(t)|^2|t|^{2n}|H_0(t)|^2\frac{dt}{2\pi}
       \ge e^{4n\log n-Cn}.\tag{5}
\]

其短依赖链如下。对固定a的cosine压缩K=LCL，||K||<1由compact norm-attainment与双compact解析唯一性支付。TT* block逆给真正gap-a投影。对real s↓1/2，先投影L²尾x^-s；head奇异幂只按L¹经K使用，光滑余项在C¹参数连续。Cosine power的两项先相消，再以uniform physical O(x^-1)尾得到L²极限；raw Mellin解析评价和Riesz唯一性将其识别为**原**k_(a,0)。

在x>a，原k的代表为x^-1/2减compact L¹函数的entire cosine transform，故在a右端有analytic延拓。非零Riesz不可能全部边界jets零，给一个fixed有限阶m及定号。酉log map后，h=g*ψ*Wk的左端L0=log a−1−δ/2满足

\[
 |h(L_0+\varepsilon)|\ge c\varepsilon^{m+2}e^{-C_0/\varepsilon}
 \quad(0<\varepsilon<\varepsilon_0).
\]

原因是原两个positive bumps与同号有限阶芽在同一个小矩形上可共同下估，没有振荡相位独立或子列假设。h光滑且左端flat，Taylor/Cauchy给

\[
 \|h^{(n)}\|_2^2\ge |h(L_0+\varepsilon)|^2
 ((n-1)!)^2(2n-1)\varepsilon^{-2n+1}.
\]

每个大n取ε=1/n，Stirling下界给(5)，Plancherel准确是J_n^g。该证明不需未审的raw G₂(t)=O(1/t)或Fourier two-wave/saddle主项；单独bump辅助稿不属于本定理依赖。辅助h不必在Sonin域，也不对它应用Weil型。

## 4. 真正growing-degree norm运输

固定n=ceil(2A/logA)、R=logX，N_X²=||D_X t^nH0||²_(dt/(2π))。Trial t^nH0每X为合法finite degree，不需把587的fixeddegree theorem外推。旧Gevrey upper给J_n≤exp(4nlogn+C_U n)，actual evaluation变分给S_X[g]≥J_n^g/N_X²。

三段真实费用为

\[
 N_X^2\le e^{(4+o(1))A}+e^{o(A)}J_n+e^{-cX}.
\tag{6}
\]

Low段R^(2n)的log=2nloglogX=oA；middle仅于R≤|t|≤X²用(4)；outer令y=√|t|≥X，以4nlogy/y≤4nlogX/X→0统一吸收growing power，再用Gevrey半指数吸收global Euler费。不将fixed-n尾或有限高度PNT偷换全线。

4nlogn=(8+o1)A、Cn=oA，将(5)–(6)相除即得(1)首式，保完整Gram inverse和原receiver norm。

## 5. 原fixed测试直接发散

定义actual probability π_X=|ghat|²ν_X/S_X[g]。对任意first-fixed R，(3)和(1)给π_X([-R,R])→0。每finiteX二阶矩由旧globalpoly/Schwartz有限，而

\[
 \frac{S_X[g']}{S_X[g]}=\int t^2d\pi_X
 \ge R^2\pi_X(|t|>R).
\]

先X∞、再用任意fixedR，得到ratio→∞及(2)，不假uniform integrability或选movingR。完整q0/q1保Γ/FP-contact、全部Λ(p^k)=logp与双pole；g′ mean0不等于polefree。正滤波自身的发散不是经典Q的负值或RH反例。

## 6. 净增量与结算

旧bare零极限、Gevrey上界/polydomain/PNT和条件代数消费均先扣；新的是actual Riesz的物理端点/all-n下界与同一growing norm的合成，决定了此前尚未被scalar/fixedpoly门排除的canonical nonlocal weight。技术来自标准projection/解析/Taylor，不主张世界优先权或新增独立算术正极化。

本结果改变这一个weight族的选择；一般positiveD′ target/membership、其它weights/signed/joint、非零primitive/principal/整截面/mixedRR/Ξ与危险corecross仍欠。Whole542+555→557 leading4/5仍仅负惯性UPPER且未改善。Goal同实例active/open/noteligible。

C053预算统一一数学轮耗尽：原cadence3→4、历史53→54、latest590；准入/两个proof/辅助/fresh/运输子lemma不另计。按既有连续非核心/来源触发，下一先第4轮宏观审视，再选新输入；不续本inverseEuler的α/degree/rate/normalization或后章来源预算。合同原5773-byte scope保持冻结，执行结算在STATE/root收据，不改fresh绑定原稿。
