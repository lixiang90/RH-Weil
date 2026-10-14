# 完整 Γ 热核、真实算术记录与共尾 Weil 惯性预算

2026-10-14；C014首轮，成果基线0c4f3a3/全部≤538固定。
Root独立消费准备稿并补核域、有限循环和严格端点；不同组织最终范围复核通过。
原准备：[Γ/profile入口](../reviews/2026-10-14/c013-moments/gamma-profile-heat-entry.md)。
独立审查：[热核域与迹](../reviews/2026-10-14/c014-first/heat-domain-and-trace-audit.md)、
[算术记录/profile](../reviews/2026-10-14/c014-first/arithmetic-record-and-profile-audit.md)、
[最强旧对照](../reviews/2026-10-14/c014-first/strong-baseline-and-macro-net-audit.md)。
本轮不运行矩阵/ζ拟合，不恢复暂停路线，不完成宏观Goal。

## 1. 实际完整对象与所证明的量词

I=(-L,L)、原Lebesgue L²、零延拓，所有complex源的自然闭型域
Dlog={f:∫log(2+|t|)|Ff(t)|²dt<∞}，Ff(t)=∫f(u)e^(-itu)du。
Γ(t)=Reψ(1/4+it/2)−logπ=actual2θ′，Γ0=−γ−π/2−3log2−logπ。
X=e^(2L)，w_n=Λ(n)/√n，A_<(x)=Σ_(n<x)w_n，A_≤(x)=Σ_(n≤x)w_n，S_L=A_<(X)。
保留全部strict primepowers，不删双pole。旧016的精确平方分解是

    Q_L=qΓ,I+Σ_(n<X)w_n E_logn−∫D_L|f|²+2|C(f)|²−2|S_pole(f)|²，
    E_a=∫_(-L)^(L−a)|f(u+a)−f(u)|²du≥0，
    D_L(u)=A_<(e^(L−u))+A_<(e^(L+u)) a.e.，
    C(f)=∫f cosh(u/2)，S_pole(f)=∫f sinh(u/2)。

本文证明对每个L>0、每个s>1的真实全源门

\[
n_-(Q_L)\le1+C_\Gamma(s)\mathcal H_L(s),\quad
C_\Gamma(s)=(2\pi)^{-1}\int_{\mathbb R}e^{-s\Gamma(t)}dt,\quad
\mathcal H_L(s)=\int_I e^{sD_L(u)}du. \tag{1}
\]

另有不依赖源f或未知ζ位置的共尾真实record primepowers n，L_n=.5logn，

\[
n_-(Q_{L_n})\le1+C e^{S_{L_n}}. \tag{2}
\]

C为绝对常数；(2)不是所有L声明，不推出实际存在负谱或PSD/RH/Ξ识别。
新增是actual Γ/profile/record的联合消费；generic heat/record工具不孤立登记创新。

## 2. Γ正跳核与原零延拓域

从[NIST digamma积分](https://dlmf.nist.gov/5.9#E16)减去t=0，变量换为a，得

    Φ(t)=Γ(t)−Γ0=∫_0^∞ w(a)(1−cos ta)da，w(a)=2e^(−a/2)/(1−e^(−2a))，
    ν(a)=w(|a|)/2=e^(−|a|/2)/(1−e^(−2|a|))。

全线闭Markov型J(f)=.5∫_0∞w(a)||T_af−f||²da=(2π)^−1∫Φ|Ff|²，
限制到零延拓支撑I的源给A_I≥0，Γ_I=Γ0I+A_I。
Φ与log(2+|t|)的图范数等价；缩支撑dilation后mollifier在原weighted Fourier norm收敛，
故Cc∞(I)是同一Dlog form core。这里是killed/Dirichlet realization，不是regional或周期域。

截断ν的compound-Poisson概率律以二阶矩tightness收敛，特征函数为e^(−sΦ)。
抽取ν0=e^(−|a|/2)/(2|a|)≤ν，Φ0=.5log(1+4t²)，其时s律是两个独立
Gamma(s/2,scale2)之差；与残余概率律卷积得到每个s>0的非负L¹ density p_s。
当s>1，e^(−sΦ)可积，p_s连续有界且p_s(0)=(2π)^−1∫e^(−sΦ)。
所有小时间density仅在a.e.意义使用，不假定s/n>1。

给g≥0支撑I，u=(λ+A_I)^−1g零延拓，r=(λ+A_R)^−1g≥0。
h=(u−r)_+属原共同form domain且支撑I；相减variational equations得到
λ||h||²+J(u−r,h)=0，而J(u−r,h)≥J(h)≥0，故u≤r。
迭代resolvent再取强极限，得killed半群由free半群支配。
在有限矩形分割上其正bilinear functional由p_s(u−v)du dv支配；
细化分割/单调延拓后Radon–Nikodym给对称非负核

    0≤r_s(u,v)≤p_s(u−v) a.e.。

s>1时r_(s/2)的HS平方≤2L||p_(s/2)||²=2Lp_s(0)，所以e^(−sA_I) traceclass。
此论证没有将compact resolvent偷换成heat traceclass。

## 3. 有界真实势、有限循环与完整全源运输

fixed L的D_L是bounded实step function，H=A_I−D_L的operator domain为Dom(A_I)。
令F(h)=e^(hD/2)e^(−hA_I)e^(hD/2)。图范数上(F(h)−I)/h强收敛到−H，
并一致有界；交叉项(e^(−hA_I)−I)(e^(hD/2)−I)f/h趋0，
无需D乘法保Dom(A_I)。Dom(H)与Dom(A_I)图范数等价，
{e^(−rH)f:0≤r≤s}为图紧轨道，telescoping及||F(s/n)^n||≤e^(s||D||∞)
给F(s/n)^n→e^(−sH)的强极限。

只取n=2m。半循环F(s/n)^m的核K_m由

    0≤K_m(u,v)≤e^((s/2)||D||∞)p_(s/2)(u−v)

支配，先证明其HS有限，再取平方迹；Tonelli给合法的非负n循环积分。
Scalar Jensen把exp((s/n)Σ_jD(u_j))上界为n^−1Σ_jexp(sD(u_j))。
替换killed核为free核，旋转循环并把其余n−1变量积分到全线；
偶数循环分成两半的积分为||p_(s/2)||²=p_s(0)，没有选取不合法小时间对角。
故Tr F(s/n)^n≤p_s(0)∫_I e^(sD)。强极限加positive TraceFatou得到

    Tr e^(−s(Γ_I−D))≤CΓ(s)H_L(s)。

Q_L≥Γ_I−D−2|S_pole><S_pole|，正图/evenpole只在此下界舍去。
严格负子空间交ker S_pole至少少一维，所以n_−Q≤1+n_−(Γ_I−D)。
每个negative eigenvalue在热迹贡献>1，得(1)；仅odd pole给+1，完整complex重数保留。
Γ-only保正不声称完整Q标准锥保正，529停止约束保持。

## 4. 完整双尾误差与真实finite step账本

[Binet原式](https://dlmf.nist.gov/5.9#E15)，z=5/4+it/2及recurrence给|t|≥1上

    Γ(t)=log(|t|/(2π))+ε(t)，|ε(t)|≤7/|t|。

具体费用：log|z|−log(|t|/2)≤25/(8t²)，两个reciprocal分别≤1/|t|、2/|t|，
Binet remainder≤1/(15|t|)，和小于7/|t|。head用Γ≥Γ0。
对1<s≤2，尾的e^(−sε)−1费≤s·7e^14/|t|，可积误差一致O(1)，所以

    CΓ(1+η)=2/η+O(1)，0<η≤1。

残数2来自actual Γ与双频尾，不采用half规范或单尾。
finite profile可完全保留：将0,L,|logn−L| (n<X,Λ(n)>0)排序为x_j，
每开cell D=D_j常数，则H_L(s)=2Σ_j(x_(j+1)−x_j)e^(sD_j)。
单点strict/closed无型差；PNT o(S)不能在指数中当1+o(1)费用。

## 5. 独立正权算术记录与严格cutoff

自含binomial Chebyshev已核ψ(x)≤Cψx、ψ(x)≥c0x于x≥16，
Cψ=4log2、c0=log2/2；见542独立推导§4，本轮不再登记该旧工具。
因此A_≤(x)≥c0√x、A_≤(x)≤2Cψ√x。
冻结κ=c0/2=log2/4，F(x)=A_≤(x)−κ√x无界，between jumps严格递减。
所有历史strict record只可能在actual primepowers，且有无界共尾族。
对任一记录n，F(n)≥F(y)对全部0≤y≤n成立；取y左极限给

    A_≤(n)−A_<(y)≥κ(√n−√y)。

真实窗口X=n排除record自身atom：S=A_<(n)=A_≤(n)−w_n，
w_n≤logn/√n→0，绝不把A_≤n换成原S。
取r=L−|u|。0<r<log2时short cutoff=e^r<2，故

    D≤S+w_n−κ√n(1−e^(−r/2))≤S+w_n−κ√n r/(2√2)。

log2≤r≤L时short≤√n，成本≤2Cψn^(1/4)，long record drop≥κ(1−1/√2)√n，
所以充分大记录上D≤S−c√n，c=.5κ(1−1/√2)>0。
两region积分加负半窗给所有s>1的统一账本

\[
\mathcal H_{L_n}(s)\le
\frac{4\sqrt2}{s\kappa\sqrt n}e^{s(S+w_n)}
+2L_n e^{s(S-c\sqrt n)}. \tag{3}
\]

S≍√n。冻结s_n=1+1/S，CΓ(s_n)=2S+O(1)，s_n(S+w_n)=S+1+o(1)，
第二项相对e^S为O(LS e^(−c√n))→0，得(2)。整个record选择不依赖f或未知谱。

## 6. 最强旧标量家族对照，净值严格但责任有限

记录窗上无需PNT就有M=esssup D=S：r<log2时原long sum≤S，
r≥log2时D<S；endpoint最后atom前的正宽条带恰D=S。
这只是record与旧016 profile的直接消费，不另登记新谱结果。

旧028负迹允许任意δ>0，而非固定1：

    B_old,opt=1+(L/π)inf_(δ>0)δ^−1 I(M+δ)，I(a)=∫[a−Γ(t)]_+dt。

Γ的已付渐近给I(a)=4πe^a+O(a+1)：log模型在双尾积分为4πe^a−O(a+1)，
实际epsilon仅在t≤2πe^(a+7)的有效支撑付款，积分绝对费O(a+1)，head也同阶。
相对误差对所有a=M+δ≥M一致趋0。inf e^δ/δ=e于δ=1，故

    B_old,opt=(4e+o(1))L e^M，M→∞。

沿同一records M=S，新(3)冻结热预算≤Ce^S，与最强旧标量家族之比O(1/L)→0。
这是两个实际certified upper budgets比较，绝不是actual负谱个数下界。
定向旧016/028/150/275及相关scope审查扣除generic record/trace工具；
新joint actual输出不被已付旧标量消费覆盖。没有声称全球文献新颖性或全文重验全部538件。

## 7. 变温度及局部分块仍不能消除本热账本的指数核心

对S≥1的任意fixed window令n_*为最大actual primepower<X，h=min(log2,log(X/n_*))>0。
两endpoint条带各宽h上D=S，所以H_L(s)≥2h e^(sS)。
1<s≤2时实际尾给CΓ(s)≥c1/(s−1)；s≥2时Γ0<0附近给CΓ(s)≥c2>0。
对S≥1，e^(ηS)/η≥eS、η≥1时e^(ηS)≥S，故

    inf_(s>1) CΓ(s)H_L(s)≥c h S e^S。

记录窗X=n是整数，n_*≤n−1，h≥1/n；S≍√n，于是完整优化热预算满足

\[
c'e^{S-L}\le\inf_{s>1}C_\Gamma(s)\mathcal H_{L_n}(s)
\le C'e^S,\qquad
\frac{\log(1+\inf_s C_\Gamma(s)\mathcal H_{L_n}(s))}{S}\longrightarrow1. \tag{4}
\]

不是实际count下界。甚至任意可测局部温度s(u)>1所发出的正账本
∫_I CΓ(s(u))e^(s(u)D(u))du，在D=S条带上逐点也付同一下界。
这只约束该形式账本，未声称变温度表达式自动是合法bracketing定理，
未排core/evaluation-density剥离、保正图与pole的同源signed费用或新独立几何。
记录本身还付h≤2√2 w_n/(κ√n)=O(logn/n)，不凭全局PNT删endpoint平台。

## 8. 宏观结算与停止条件

新增actual Γ/degree/record joint输入使cofinal全源计数预算严格越过强旧标量界；
同时(4)表明该热账本的leading S指数无法靠变温度/局部正温度费用消除。
成果晋级不等于宏观完成：真实危险core、成长PSD/nearPSD、Ξ识别仍未付，
此限定热预算边界不排联合signed修复，未达到Goal第3项完整method-class门。

C014首轮结算一次；准备/各逆审/generic工具恢复零额外轮。
应停止单靠degree热预算的主攻，不用剩余预算优化小常数或温度维持推进。
下一输入须保留实际prime正图/evenpole与degree的同源联合信息，
或给真正危险core/evaluation-density的独立消费；不能把未知domination改名为新来源。
唯一下一合同与精确动作由STATE/最新决策恢复，所有暂停与降级约束保持。
