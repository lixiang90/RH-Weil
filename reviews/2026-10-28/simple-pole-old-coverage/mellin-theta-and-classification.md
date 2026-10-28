# Simple poles ±A：实际 Mellin／移线／561旧分类运输

2026-10-28；G20261027/runtime1793085111/原0c4f。执行唯一 [next](../signed-replacement-source-location/next-simple-pole-old-classification-admission.md) 的实际运输腿。已恢复 README/STATE、check→show、Goal/C049、D20261028W和宏观前沿；当前稿仅支持输出，root消费前不是结算。无新source/web、finite-order延拓、数学合同或计轮。

**结果：在next明示的正测度／原simple poles ±A／同一FE／uniform exponential strip界下，实际 theta 身份、A>0、μ_A的旧561输入及最终A=1、N=普通整数计数全部闭合。** 这是561与标准Mellin运输的强旧合成0；不提供独立Weil正型或RH输入。

## 1. 精确对象与已给前件

Π是(0,∞)上的正Borel测度，某实σ0有 P_σ0:=∫e^(−σ0u)dΠ<∞。给

\[
 M=\exp_*\Pi=\delta_0+\sum_{j\ge1}\Pi^{*j}/j!,\quad
 N=(u\mapsto e^u)_*M,\quad
 Z(s)=\int e^{-su}dM(u)=\int_{[1,\infty)}x^{-s}dN(x)
\]

的真实右半面germ。Λ(s)=π^(−s/2)Γ(s/2)Z(s)按给定germ亚纯延拓全C；除0、1外无pole，两处**simple**且留数−A、A，并有精确FE Λ(s)=Λ(1−s)。A尚不预设为1或正数。

固定一次 c>max(σ0,1)。给定 C,N0,T0,η>0，使全部 σ∈[1−c,c]、|τ|≥T0有

\[
 |\Lambda(\sigma+i\tau)|\le C(1+|\tau|)^{N0}e^{-\eta|\tau|}. \tag{1}
\]

本稿直接使用(1)，不以“finite order”替代。σ-strip uniform是水平尾所需的真实量词，不是两条竖线的单独界。

## 2. M、N、单位质量与Gaussian的实际费用

对任意 d≥σ0，P_d<∞。加权正测度的卷积与Tonelli给

\[
 \int e^{-du}d\Pi^{*j}(u)=P_d^j,\quad
 \int e^{-du}dM(u)=e^{P_d}=Z(d)<\infty. \tag{2}
\]

因此级数在每个compact上定义正Radon M；Π支撑严格u>0，故每个j≥1卷积在0的质量为0，M({0})=1。于是N支撑[1,∞)、N({1})=1；不假离散计数或整数重数。

使用同一个c，由(2)

\[
 N([1,R])\le Z(c)R^c\quad(R\ge1). \tag{3}
\]

实际Theta定义为

\[
 \Theta_N(t)=2\int_{[1,\infty)}e^{-\pi t x^2}dN(x),\qquad t>0. \tag{4}
\]

它对全部fixed t有限：其绝对值≤2Z(c)sup_(x≥1)[x^c e^(−πtx²)]。N在1的单位原子另给 Θ_N(t)≥2e^(−πt)>0。若 T≥max(1,c/(2π))，上式中x的最大值在1，因而

\[
 2e^{-\pi T}\le\Theta_N(T)\le2Z(c)e^{-\pi T}. \tag{5}
\]

这是真实全N尾，不把N替成有限计数或假已识别整数。

## 3. Gamma逆Mellin与2／π／ds核账

对a>0，v↦exp(av−e^v)在S(R)。其Fourier变换是Γ(a+iτ)的符号变换，因此Fourier inversion给标准的、绝对收敛的Gamma逆Mellin：

\[
 e^{-y}=\frac1{2\pi i}\int_{(a)}\Gamma(w)y^{-w}dw\quad(y>0).
\]

令a=c/2、s=2w，则dw=ds/2，故

\[
 2e^{-y}=\frac1{2\pi i}\int_{(c)}\Gamma(s/2)y^{-s/2}ds. \tag{6}
\]

不是2/(2πi)再乘一条s线。Γ(c/2+iτ/2)的L¹(τ)有限也由上述Schwartz Fourier变换支付，不需要额外新渐近定理。

将y=πtx²代入(6)，对实际dN积分。交换绝对费为

\[
 \frac{(\pi t)^{-c/2}Z(c)}{2\pi}
 \int_{\mathbb R}|\Gamma((c+i\tau)/2)|d\tau<\infty.
\]

故全部fixed t>0有

\[
 \boxed{\Theta_N(t)=I_c(t):=
 \frac1{2\pi i}\int_{c-i\infty}^{c+i\infty}
              \Lambda(s)t^{-s/2}ds.} \tag{7}
\]

另一方向的核查是：对Res>max(σ0,0)，以该实部控制绝对积分，直接Tonelli/Fubini给

\[
 \int_0^\infty\Theta_N(t)t^{s/2}\frac{dt}{t}=2\Lambda(s). \tag{8}
\]

(8)的2与(7)没有冲突，正是s=2w的ds因子。π、positive/negative x的2与Gaussian指数均沿原定义保留。

## 4. 全矩形移线与两项留数

对固定t>0，记

\[
 K_t=\max_{\sigma\in[1-c,c]}t^{-\sigma/2}<\infty.
\]

在高度±T、T≥T0+1的水平边，(1)给

\[
 \left|\int_{1-c}^{c}\Lambda(\sigma\pm iT)
                        t^{-(\sigma\pm iT)/2}d\sigma\right|
 \le(2c-1)CK_t(1+T)^{N0}e^{-\eta T}\longrightarrow0. \tag{9}
\]

两竖线截断外的绝对尾亦≤CK_t∫_(|τ|>T)(1+|τ|)^(N0)e^(−η|τ|)dτ→0。无需挑一列good heights，不从FE或未知零点位置取得尾。量词是ALL先fixed t；同界可在fixed compact t区间取sup，但不是moving t→0/∞的一致额外声明。

矩形中只有simple poles0、1；对Λ(s)t^(−s/2)，其留数依次为−A、At^(−1/2)。右边竖线朝上减左边竖线朝上，正向留数公式给

\[
 I_c(t)=A(t^{-1/2}-1)+I_{1-c}(t). \tag{10}
\]

左线令w=1−s，ds=−dw同时反转上下端；由精确FE与绝对收敛，

\[
 I_{1-c}(t)=t^{-1/2}I_c(1/t).
\]

因此得到实际身份

\[
 \boxed{\Theta_N(t)=A(t^{-1/2}-1)+t^{-1/2}\Theta_N(1/t),
                  \qquad\forall t>0.} \tag{11}
\]

负留数在0给−A，不能换成+1，也不能把A先归一为1。Double poles会另带log(t)项，故前轮旧反测不属于本simple-pole输入。

## 5. 独立关闭A的符号

正实右半面germ的Schwarz对称延拓给Λ实型，故A为实数。由(5)，当t↓0时

\[
 t^{-1/2}\Theta_N(1/t)=O(t^{-1/2}e^{-\pi/t})\longrightarrow0.
\]

代入(11)，若A<0，右侧最终负；若A=0，右侧趋0。两者均与真实下界 Θ_N(t)≥2e^(−πt)→2矛盾。所以

\[
 A>0. \tag{12}
\]

这一步只使用已运输(11)、正N及单位原子，不依赖另一稿、Tauberian或先假小t主项。

## 6. μ_A进入旧561，并由x=1校准A

令check N为x↦−x的推前，设

\[
 \mu_A=A\delta_0+N+\check N.
\]

它是偶正测度；由(3)有polynomial增长，从而是tempered。例如取整数m>c，按dyadic壳求和给∫(1+|x|)^(−m)d(N+check N)<∞，实际费用由Z(c)、c、m控制。于是对φ∈S，其作用由sup_x(1+|x|)^m|φ(x)|支付，未虚报原du-Dlog有界源映射。

支撑与(4)给

\[
 \mu_A|_{(-1,1)}=A\delta_0,\qquad
 \theta_{\mu_A}(t)=A+\Theta_N(t).
\]

(11)恰好变成 θ_(μ_A)(t)=t^(−1/2)θ_(μ_A)(1/t)。由A>0，ν=μ_A/A是偶正tempered测度、单位gap δ0且有全部t的固定Gaussian身份。

旧 [561§3固定Gaussian段](../../../notes/561-beurling-positive-measures-self-duality-and-integer-recovery.md)以Gaussian求导／偶Hermite全性给νhat=ν，再由同节正性＋单位gap定理给ν=Δ_1。故

\[
 \mu_A=A\sum_{n\in\mathbb Z}\delta_n.
\]

此时才比较x=1的质量：左侧为N({1})=1，右侧为A。因此

\[
 \boxed{A=1,\quad N=\sum_{n\ge1}\delta_n,\quad Z=\zeta.} \tag{13}
\]

Z的等式先在真实收敛右半面由同一N的Mellin变换成立，再按已给解析延拓消费。若要读回Π，原无δ0的Euler-log在实右端趋0；logZ=logζ再由加权有限测度Laplace唯一性给Π=Π_ζ。这不免费恢复一个此前未给的positive primitive对象。

## 7. 依赖收据、强旧净值及停止

本稿用561§1的加权卷积指数、§3的完整Gaussian/Fourier/unitgap结论及§4的识别／Weil区别。另读旧564§2和 [HL来源核账§2](../../2026-10-20/grh-dual-pairs/hilberdink-lapidus-primary-source-audit.md)：它们已有精确Mellin反射与有限power-log缺陷的运输角色；本次按给定simple ±A和更强明示strip界将标准运输逐常数落在实际N上，没有另取外部文献或扩大HL原前件。

Object/range为正Euler-log Π→weighted M→x≥1正N→偶μ_A→旧单位整数梳。关系／quotient／physical Weil角色未混入这条链。全部t是逐一固定；c/C/N0/T0/η一次给定，A由实际留数校准。没有源窗L、频高或算术height的uniform新误差；没有把x或theta变量t当物理log源u。

**扣旧后的消费分类为0。** 在这组明示simple-pole／strip域中，model-selection已经被更强旧运输＋561分类排空，继续UD／coset乘法或A归一化设施不新增输入。本比较关闭的是准确旧覆盖，不是新经典Γ countermodel，不是否定给定strip界之外或仅极限有FE／entire的D′层。

它只识别经典ζ，不能把加法Fourier正测度的正号搬成乘法完整Weil卷积正型。原physical r=e^(u/2)f、全complex/原du与zero-extension Dlog、完整Γ/FP-contact、所有proper powers、双pole、成长core/coupling及同一非零primitive/mixed仍须独立支付；actualζ whole4/5负惯性UPPER未改。无新数学合同／轮次、cadence保持，Goal active/open/noteligible；root对齐另一腿及fresh后才可结算。
