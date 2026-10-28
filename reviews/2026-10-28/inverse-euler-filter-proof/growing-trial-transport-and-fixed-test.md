# C053 growing trial：原Gram三段范数与条件fixed-test消费

2026-10-28；`/root/rational_first_gate`当前C053独占proof腿，非前一inverse-Euler准入终态复用。已恢复README／STATE、check→show、Goal／原0c4f／AX／当前C053合同及[root准入收据](../inverse-euler-filter-admission/root-admission-consumption-scope.json)。本腿不改STATE／Git／cadence，不web／新primary／PDF／查询／数值，不换H₀、g、n recipe或norm。

**当前终态：三段原Gram norm及其全线growing-n尾已独立闭合；第7节已全文核对另一腿实际终稿并解除本腿对全大n moment lower (L)的等待。** 由两个明确原件合成，S_X[g] lower、归一化谱逃逸及g′值∞的本腿前件已对齐；整体C053仍待不同fresh／root最终消费。J_n upper／全部finite polynomial的Sonin domain是旧输入，不冒作(L)。以下保留先按(L)组织的条件推导，实际解除位置只在第7节，不用draft代根结果。

## 1. 对象、范数及唯一conditional输入

使用合同固定的a=2、δ=log2/4、标准归一化bump ψ及actual Riesz raw函数G₂，`H₀(t)=ψhat(t)G₂(t)`。沿585已付模板，这一个fixed H₀满足

\[
 H_0\in M=\operatorname{Ran}P,
 \quad |H_0(t)|\le C_H e^{-c_H\sqrt{|t|}},
 \quad t^jH_0\in M\quad(\forall\text{finite integer }j\ge0).
                                                               \tag{H}
\]

C_H、c_H只依该H₀，先于X／n。receiver Hilbert norm始终为`L²(dt/(2π))`。这里不是completed Mellin norm或physical source du；g仍是587的固定du norm1 bump，两者角色分开。每个X所用degree有限，故(H)的逐finite degree membership足以准入；不把C050的fixed-source-degree Gram lower外推到growing degree。

记

\[
 \ell=\log X,\qquad A=\sqrt X/\ell,
 \quad n=n_X=\left\lceil\frac{2A}{\log A}\right\rceil,
 \quad R_X=\ell.
\]

X充分大使logA>0。以下是精确固定recipe，没有调整n的常数。其基本量词是全部充分大real X，有

\[
 \log A=\ell/2-\log\ell,\qquad
 n=O(\sqrt X/\ell^2),\quad n=o(A),\quad
 4n\log n=(8+o(1))A.                                  \tag{S}
\]

ceil误差≤1，贡献O(logA)=o(A)，不会改变这些式子。

同一finite Euler symbol `D_X(t)=∏_(p≤X)(1−p^(-1/2−it))`及完整Gram给

\[
 Q_X(t)=\sup_{h\in M,\ \|D_Xh\|_2\le1}|h(t)|^2,
 \quad S_X[r]=\int|\widehat r(t)|^2Q_X(t)\frac{dt}{2\pi}.
\]

记真实trial norm及两个moment

\[
 N_X^2=\|D_X t^nH_0\|_2^2,
 \quad J_n=\int |t|^{2n}|H_0(t)|^2\frac{dt}{2\pi},
 \quad J_n^g=\int|\widehat g(t)|^2|t|^{2n}|H_0(t)|^2\frac{dt}{2\pi}.
\]

本腿唯一conditional输入为另一proof腿必须在**同一H₀／g／原norm**新证的

\[
 \boxed{J_n^g\ge\exp(4n\log n-C_L n)
 \quad\text{对每个整数 }n\ge n_0.}                    \tag{L}
\]

C_L、n₀固定。只证明某子列、每fixed n positivity、nonzero entire或Gevrey upper都不能替代(L)的全大n量词。本稿不证明／预认证Riesz两波、bump saddle、good-set等(L)的新前件。

## 2. 先扣旧upper与真实trial准入

由(H)，直接令y=√|t|，

\[
 J_n\le\frac{2C_H^2}{\pi}
        \frac{\Gamma(4n+2)}{(2c_H)^{4n+2}}
 \le\exp(4n\log n+C_U n)\quad(n\ge1),                 \tag{U}
\]

增大一次fixed C_U可吸收常数／logn。第一式保dt/(2π)及正负两半轴；不影响最终exponent的固定2π仍在实际norm中。这个upper是已付Gevrey输入的标准直接后果，不是本轮新moment lower。

对每个X，`h_X=t^nH₀`确在M，D_X在real轴非零且bounded，所以`0<N_X<∞`。合法normalized trial是`h_X/N_X`，不是unweighted单位向量。由actual evaluator的定义逐点得

\[
 Q_X(t)\ge\frac{|t|^{2n}|H_0(t)|^2}{N_X^2},\qquad
 S_X[g]\ge\frac{J_n^g}{N_X^2}.                        \tag{V}
\]

所有factor均在原receiver范数，完整G_X逆已经由Q_X的weighted variational定义保留；没有删Gram、以B_XP B_X*冒projection或将trial upper倒作full kernel upper。

## 3. 真实N_X²的三段：所有大real X统一

旧585的两个算术接口是：

\[
 |D_X(t)|^2\le\exp[(4+o(1))A]\quad(t\in\mathbb R),     \tag{E0}
\]
\[
 \log|D_X(t)|^2
 =-4A\Re\frac{e^{-it\ell}}{1-2it}+o(A)
 \quad\text{uniform于 }|t|\le X^2.                    \tag{E1}
\]

E0是全线finite product粗界／PNT；E1有明确有限高度，下面不外推它。

**Low：|t|≤R_X=ℓ。** 用E0及|t|^(2n)≤ℓ^(2n)，

\[
 N_{X,lo}^2
 \le e^{(4+o(1))A}\ell^{2n}\|H_0\|_2^2
 =\exp[(4+o(1))A].                                   \tag{N0}
\]

这里`2n logℓ/A=O(logℓ/logA)→0`，fixed H₀ norm也只给o(A)。不能遗漏growing power的这笔费；保留后它确实为subexponential。

**Middle：ℓ≤|t|≤X²。** E1及`|1−2it|≥sqrt(1+4ℓ²)`给某个η_X≥0、η_X→0，使

\[
 \log|D_X(t)|^2\le\frac{4A}{\sqrt{1+4\ell^2}}+o(A)
                      \le\eta_X A.
\]

因此

\[
 N_{X,mid}^2\le e^{\eta_X A}J_n.                     \tag{N1}
\]

误差对该整个middle、当前n同时有效；n不进入E1误差。把积分放宽为全线J_n是positive upper，不使用未给的growing polynomial相对集中。

**Outer：|t|>X²。** 仅用E0与(H)。设y=√|t|≥X。因logy/y在y>e递减，(S)给

\[
 \sup_{y\ge X}\frac{4n\log y}{y}
 =\frac{4n\log X}{X}
 =O\!\left(\frac1{\sqrt X\,\ell}\right)\longrightarrow0.
\]

故对全部充分大X、**全部y≥X**，`4n logy≤c_H y`。从而

\[
 |t|^{2n}|H_0(t)|^2
 \le C_H^2 y^{4n}e^{-2c_H y}
 \le C_H^2 e^{-c_H y}.
\]

把growing degree统一吸收到同一个Gevrey半指数以后，

\[
 \begin{aligned}
 N_{X,out}^2
 &\le C e^{(4+o(1))A}\int_X^\infty y e^{-c_Hy}dy\\
 &\le C'(X+1)e^{-c_HX+(4+o(1))A}
 \le e^{-c'X}                                         \tag{N2}
 \end{aligned}
\]

可固定c′=c_H/2并增大起点，因为A=o(X)、logX=o(X)。变量替换中的两半轴与dt/(2π)均只给已写fixed C。**没有把E1用在t>X²，也没有把fixed-n尾换名成uniform growing-n尾。** 此处n_X固定为合同recipe；不需把它缩小救题。

合并无条件得到

\[
 N_X^2\le e^{(4+o(1))A}+e^{o(A)}J_n+e^{-c'X}.
                                                               \tag{N}
\]

再用旧(U)及(S)，存在ε_X≥0、ε_X→0，使

\[
 N_X^2\le\exp(4n\log n+C_U n+\varepsilon_XA).          \tag{N*}
\]

Low exponent约4A，4nlogn约8A，故low项和常数求和均可吸入(N*)；这个domination不调用(L)。

## 4. 条件(L)若闭合：S_X[g]下界与归一化逃逸

本节所有结论仍以(L)为前件。由(V)、(L)、(N*)，

\[
 S_X[g]\ge
 \exp[-(C_L+C_U)n-\varepsilon_XA]
 =\exp[-o(A)],                                       \tag{SL}
\]

因为n=o(A)。这里的o(A)可取某个非负fixed-data函数ε′_XA，ε′_X→0，适用于全部充分大real X。旧结果S_X[g]→0保持；(SL)断言的是其cofinal decay为subexponential A尺度，不将它误记成正的固定lower。

定义与准入时同一actual probability

\[
 d\pi_X(t)=\frac{|\widehat g(t)|^2Q_X(t)}{2\pi S_X[g]}dt.
\]

质量精确为1。对任意**先fixed**K>0，589旧6.12在充分大X给`sup_|t|≤K Q_X≤exp[(-4+o(1))A]`。配(SL)，

\[
 \pi_X([-K,K])\le
 \frac{C_K e^{(-4+o(1))A}}{S_X[g]}
 \le\exp[(-4+o(1))A]\longrightarrow0.                \tag{Esc}
\]

K不随X增长。故

\[
 \frac{S_X[g']}{S_X[g]}=\int t^2d\pi_X(t)
 \ge K^2\pi_X(\{|t|>K\})
\]

给每个fixed K的liminf≥K²；再用K任意，得到

\[
 \boxed{S_X[g']/S_X[g]\longrightarrow+\infty.}         \tag{R}
\]

每finite X的second moment finite由旧全线`Q_X≤C(1+t²)`与ghat Schwartz支付。不要求uniform integrability；本处是lower bound证明发散，不是交换二阶moment与weak极限。没有用moving K、数值尾或normalized裸0/0推断。

## 5. 条件fixed compact test后果与范围

精确calibration β_X=q₀/S_X[g]给`β_XS_X[g′]=q₀·S_X[g′]/S_X[g]→∞`。更一般，任意共同positive scalar β_X若`β_XS_X[g]→q₀>0`，同式乘积也趋∞。因此与原完整finite q₁=Q_W[g′]>0不能相符；固定test就是`r=g′`的compact smooth卷积平方r*r*，不需要先借positive-D′谱运输桥证明整个target有何拓扑。

g／g′的physical原du／zero-extension Dlog与全complex槽不变；q₀／q₁保Γ／FP-contact、全部Λ(p^k)=logp及双pole。g′ mean0不等于polefree。这里没有将noncompact B_X^−1g代入一个未准域的完整Q身份，也没有把发散的filter值称为Q负源或RH反例。

唯一候选仍是finite full-Euler inverse的同一common weight再乘matching-g scalar；不覆盖其它highgain weights、非局部signed／joint、source-adapted非线性或primitive几何。n_X是receiver trial的growing degree，source g本身始终fixed；本证明不续C050 degree优化、C052 scalar或旧Gaussian可达性预算。Whole4/5负惯性UPPER及长期核心门并未由这个局部边界自动改善或完成。

## 6. Paid／conditional／open及后续版本对齐

* **本腿已闭：** (H)／旧(U)与finite-polynomial domain的正确使用；(V)的actual weighted Gram运输；(N0)–(N2)特别all-y≥X的growing tail；(L)到(SL)／(Esc)／(R)和matching-g固定test的逻辑。
* **版本对齐前的conditional责任：** (L)本身的实际G₂／g／ψ及every-large-integer n lower。另一腿未终态／未全文对齐前，本稿不称该前件已闭；当前仅按第7节实际原件解除。Fourier共同good-set不是本合同强制路线，作者实际走物理边界的等价证明，不能额外要求其重证未使用的saddle。
* **不扩执行：** 若(L)或任一实际domain／uniform量词断点，报告该断点；不换n、源、H₀、norm或追primary／6.4／6.5／后章。无第二candidate。

本腿终稿不代root结算。当前cadence3/history53/latest589/formal17保持；一个C053实际proof迭代仅在不同fresh／root前件闭合后统一结算，文件／lemma／工具不另计轮。Goal同实例active/open，不预590或最终完成。

必要已读项目输入：C053合同全文、root准入closure原件；585与共同向量原稿的Gevrey upper／所有finite polynomial domain段；589原real-strip globalpoly及6.12的kernel规范。本稿未重读其外部PDF。Moment终稿仅在实际发出、全文核对后按下节追加绑定。

## 7. 当前moment终稿的实际对齐与本腿终态

现已实际全文读[另一腿终稿](actual-sonin-gevrey-moment-lower.md)：13693 LF bytes／294 lines，LF SHA256
`96339651615d5ccf10b999fea7dd3ec3c6f91961be0594433e94de307ef3044a`，现场重核匹配。它不是旧准入稿或待证two-wave断言。其实际证明链与本腿使用处逐项一致：

1. 同一个positive-halfline cosine与a=2的两gap block投影；s↓1/2的奇异幂只作L¹，平滑余项在C¹一致，physical x^−1尾给L²极限，从而以原raw Mellin解析评价识别**冻结的**k_(2,0)。没有换一个端点较好的trial。
2. 原Riesz在x=a右的real解析代表非零，故有finite固定阶m与统一定号；原log map给支撑下端log a。这一physical tail／端点事实不冒成未付raw G₂(t)=O(1/t)。
3. 使用同一g和同一ψ的positive卷积`h=g*ψ*Wk_(2,0)`，非零贡献在其左端附近同号，小矩形给每个小ε的`|h(L₀+ε)|≥cε^(m+2)e^(−A₀/ε)`；不依赖频率子列或两个bump的假相位独立。
4. h的全部导数在原L²(du)，精确Plancherel给`J_n^g=||∂^n h||²_du`，即本稿同一个dt/(2π)moment。ε=1/n的Taylor／Cauchy直接给**每个**大整数n的(L)，固定常数可供当前n_X调用。

该原件没有未付的Riesz识别／边界／all-n接口。本腿仅核其交付和上述必要逻辑，不将作者的未用Fourier saddle写成已审前件。于是第4–5节在当前联合原件上可消费为(SL)、(Esc)、(R)及任意positive scalar matching-g的原fixed-test发散；整体不同fresh／root仍另验，不因两个局部终稿就自行结算C053。

冻结合同5773 bytes／LF SHA `94a8d147ba05067678d56b691799ee3fac54f7bda8e719d272ce0c6c082de8d1`；准入root收据4146 bytes／LF SHA `cde3a40832cd010977ebfdb5565e6df409ce384a09c9316be18c512bc3427887`；旧共同向量稿16348 bytes／LF SHA `dcdf8e91b408423e3647f116f8bd72e040feaf24cf80f9b92db30d776398af85`。这些输入与当前moment原件的raw／physical norm、固定g／ψ／H₀及n_X全部相同。

**本腿terminal：实际运输及其必要moment版本对齐闭合，待独立fresh／root总消费。** 无新源、参数、proof合同、Git／STATE／cadence操作；本条对齐不另计数学轮，不预590或Goal完成。
