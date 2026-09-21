# 421. 带时间测试的 Hardy 迹缺陷、循环边界与非原子限制

2026-09-21。[全文独立逆审通过；半迹归一化与定义补明采纳复核通过] 执行[有限任务单](../reviews/2026-09-21/f1-hardy-weighted-trace-defect-next-proof-plan.md)。沿用[420](420-f1-source-hardy-index-and-dual-action.md)的实际源、实平方分割c及Fourier约定，不用抽象Bott元代替原u。这里先构造真实读出，再检验它是否等于[414](414-f1-deep-boundary-unitary-and-time-defect.md)的原周期分布。

结论包含三个不同层次：固定测试权重的循环余圈障碍；原源规范环面平均的准确零值；以及固定／迹范数有界／系数BV有界的读出不能产生周期原子的限制。最后一项允许近锐源的迹范数发散，并构造其明确的频率正则化极限；不排除更奇异的相对传递或原先h平滑后的全Γ算子。

## 1. 实际星代数、乘法缺陷与范数

令H=L²(R)，P为正频率投影，Q=1−P，H+=PH。定义
\[
 \mathcal A_2=\{a\in B(H):[P,a]\in\mathcal S_2\},\qquad
 \|a\|_{\mathcal A_2}=\|a\|+\|[P,a]\|_2.                         \tag{1}
\]
由[P,ab]=[P,a]b+a[P,b]及[P,a*]=−[P,a]*，它是含单位的Banach星代数：若a_n在(1)中Cauchy，则算子范数极限a和HS极限b满足b=[P,a]，因为HS收敛也蕴含算子范数收敛。乘法次可乘性和伴随等距由上述公式直接给出。

记
\[
 T(a)=PaP|_{H_+},\qquad D(a,b)=PaQbP
       =T(ab)-T(a)T(b).                                       \tag{2}
\]
PaQ、QbP是HS，故D连续双线性取值于迹类。设
x_a=||PaQ||₂，y_a=||QaP||₂，则||[P,a]||₂²=x_a²+y_a²。
于是对任意W∈B(H+)定义
\[
 \Psi_W(a,b)=\operatorname{Tr}\bigl(W(D(a,b)-D(b,a))\bigr),\quad
 |\Psi_W(a,b)|\le\|W\|\,\|[P,a]\|_2\,\|[P,b]\|_2.              \tag{3}
\]
最后一界使用x_a y_b+x_b y_a的二维Cauchy不等式，已包含两个有符号项。
Ψ_W反对称，且Ψ_W(1,a)=0。

对h∈C_c^∞(R)，令
\[
 U(h)=\int h(s)T_s\,ds,\quad W_h=U(h)|_{H_+},\quad
 \widehat h(\xi)=\int h(s)e^{-is\xi}\,ds .
\]
W_h是正频率上的乘法算子M_{\widehat h}，且||W_h||≤||h||₁。420的u_ζ是光滑的A₂值族，故上述每项是实际合法迹。

## 2. 结合律给出的准确边界

由(2)直接展开，得到
\[
 D(ab,c)-D(a,bc)=T(a)D(b,c)-D(a,b)T(c).                         \tag{4}
\]
定义Hochschild边界
\[
 (b\Psi_W)(a,b,c)=\Psi_W(ab,c)-\Psi_W(a,bc)+\Psi_W(ca,b).
\]
对(4)作三个循环排列，有
\[
 b\Psi_W
 =\operatorname{Tr}W\bigl([T(a),D(b,c)]
              +[T(b),D(c,a)]+[T(c),D(a,b)]\bigr)
 =\operatorname{Tr}\bigl([W,T(a)]D(b,c)
              +[W,T(b)]D(c,a)+[W,T(c)]D(a,b)\bigr).            \tag{5}
\]
这里每个D都迹类，其余因子有界，故最后一次循环合法；没有把非迹类的单个T(ab)拿出来求迹。特别地，W=1给真正循环1余圈；一般测试权重不能默认满足bΨ_W=0。

## 3. 在完整A₂上，闭性恰要求标量权重

**命题。** 在H+、H−均非零的本模型中，Ψ_W在完整A₂上是循环1余圈，当且仅当W是标量算子。

标量方向由(5)。反向取任意A∈B(H+)，将a置为它在H+上的对角块，在H−上为零。取单位y∈H−及任意x,z∈H+，令
\[
 b=|x\rangle\langle y|,\qquad c=|y\rangle\langle z|.
\]
这些算子属于A₂，D(b,c)=|x〉〈z|，D(c,a)=D(a,b)=0。因此
\[
 (b\Psi_W)(a,b,c)=\langle z,[W,A]x\rangle .                   \tag{6}
\]
若边界恒零，则W与全部A交换，故W为标量。最后一步可直接由W与所有秩一投影交换得出：每条直线W不变，再对两个独立向量及其和比较特征值。

这给具体非零证据：若取正频率单位x₀,x₁、负频率单位y，
a=|x₀〉〈x₁|，b=|x₁〉〈y|，c=|y〉〈x₀|，
则边界为〈x₀,Wx₀〉−〈x₁,Wx₁〉。
可取非零实偶光滑紧支h≥0且∫h=1；在接近0的正频小区间取x₀，在足够高频的小区间取x₁，
使该差实部≥3/4。这些向量可有光滑紧支Fourier变换，所得有限秩算子也在真实时间紧算子理想内。

更一般，任意非零h∈C_c^∞的\widehat h不可能在整个正半轴为常数：
其整函数延拓和恒等定理会使它处处常数，Riemann–Lebesgue极限再迫使该常数及h都为零。
所以对每个这样的非零h，Ψ_{W_h}在完整A₂上都不闭。
这是对明定代数的结论，不是断言每个较小源子代数上的限制也必然不闭。

## 4. 原源的完整频率核，保留所有交叉项

取固定有限集合F⊂Z×{0,1}包含全部非零系数，写g=(n,b)，
a_g=nL+bM，ζ^g=ζ_p^n ζ_q^b。令实函数
\[
 f_{(n,0)}(t)=-c(t)c(t-nL),\qquad
 f_{(n,1)}(t)=c(t)c(t-nL-M),\qquad
 u_\zeta=1+\sum_{g\in F}\zeta^g M_{f_g}T_{a_g}.                \tag{7}
\]
恒等项和(n,b)=(0,0)项不能合并成一个可丢弃系数；前者只因P1Q=0不进入非对角块，后者仍保留在F中。

在酉Fourier变换下，正负频之间的核为
\[
 K_\zeta(\xi,\eta)=\frac1{2\pi}
       \sum_{g\in F}\zeta^g\widehat f_g(\xi-\eta)e^{-ia_g\eta}.
                                                                    \tag{8}
\]
定义实的可积密度
\[
 d_\zeta(\xi)=\int_{\eta<0}
       \bigl(|K_\zeta(\eta,\xi)|^2-|K_\zeta(\xi,\eta)|^2\bigr)d\eta,
       \qquad \xi\ge0.                                      \tag{9}
\]
它由两个HS平方的对角密度之差给出，且
||d_ζ||₁≤||[P,u_ζ]||₂²。不是对任意迹类核作未经证明的逐点对角取值。
直接用HS核乘积和有界乘法求迹得到
\[
 \Psi_h(u_\zeta^*,u_\zeta)
   =\int_0^\infty\widehat h(\xi)d_\zeta(\xi)\,d\xi.             \tag{10}
\]
这里Ψ_h指Ψ_{W_h}。展开(9)的完整交叉项是
\[
\begin{split}
 d_\zeta(\xi)=\frac1{4\pi^2}\sum_{g,h\in F}\zeta^{h-g}
 \int_{\eta<0}\bigl[
 &\overline{\widehat f_g(\eta-\xi)}\widehat f_h(\eta-\xi)
           e^{i(a_g-a_h)\xi}\\
 -&\overline{\widehat f_g(\xi-\eta)}\widehat f_h(\xi-\eta)
           e^{i(a_g-a_h)\eta}\bigr]\,d\eta .                  \tag{11}
\end{split}
\]
第二个求和指标h只在(11)中表示群标签，不是测试函数。后续平均前未删除交叉项或混合次数。

## 5. 固定平滑源的时间函数及准确环面平均

(9)的每项在ξ→+∞快速衰减，所有ξ矩绝对可积；因为f_g光滑紧支，有限个Fourier变换均为Schwartz。
因此
\[
 k_\zeta(s)=\int_0^\infty e^{-is\xi}d_\zeta(\xi)d\xi
       \in C^\infty(\mathbb R)\cap C_0(\mathbb R),\qquad
 \Psi_h(u_\zeta^*,u_\zeta)=\int h(s)k_\zeta(s)ds .             \tag{12}
\]
Fubini由h可积及d_ζ可积保证；参数ζ的连续性、各阶s导数和范数界来自有限相位和。
C₀性质也可由L¹密度的Riemann–Lebesgue引理直接证明。

令dζ为环面归一化Haar测度。积分(11)只保留g=h，此时a相位消失。
由于所有f_g实，|\widehat f_g(-ω)|=|\widehat f_g(ω)|，每个保留项在每个ξ上已相消。因此
\[
 \int_{\mathbb T^2}d_\zeta(\xi)d\zeta=0,\qquad
 \int_{\mathbb T^2}\Psi_h(u_\zeta^*,u_\zeta)d\zeta=0
 \quad\text{对全部测试函数 }h.                              \tag{13}
\]
这是逐频率的直接计算，不是由420逐点指数零推断带h的值为零。
不据此断言每个单独ζ的读出也为零。

## 6. 固定迹类读出的一般限制

对任意B∈S₁(H+)，取核型展开B=∑s_j|v_j〉〈w_j|，∑s_j=||B||₁，v_j、w_j单位。
在正频率表示中，
\[
 d_B(\xi)=\sum_j s_jv_j(\xi)\overline{w_j(\xi)}
       \in L^1(0,\infty),\qquad \|d_B\|_1\le\|B\|_1,
\]
因为逐项L¹范数≤1；该级数绝对在L¹中收敛。对有界乘法m，
Tr(M_mB)=∫m d_B。因此
\[
 k_B(s)=\operatorname{Tr}(T_sB)
      =\int_0^\infty e^{-is\xi}d_B(\xi)d\xi\in C_0(\mathbb R),
 \quad\|k_B\|_\infty\le\|B\|_1,\quad
 |\operatorname{Tr}(U(h)B)|\le\|B\|_1\|h\|_1.                \tag{14}
\]
可先对有限区间阶梯函数证明Fourier变换连续且无穷远趋零，再用L¹逼近证明C₀，无需光滑核假设。

若B_ζ迹范数连续而μ是环面上有限复测度，Bochner积分B_μ=∫B_ζdμ仍迹类，
其时间读出仍满足(14)，界为sup_ζ||B_ζ||₁·||μ||TV。
进一步，任意网或序列的此类总迹范数一致有界时，其任何分布极限F都满足
|F(h)|≤C||h||₁。它不能等于在某个孤立周期处具有非零原子的分布。
极限不必仍连续或属于C₀；这里只继承L¹测试范数界，不误用C₀的分布闭性。

## 7. BV系数允许迹范数发散，仍给统一L²限制

现在允许(7)中的实紧支系数只具有有界变差，并要求共同有限F。设
\[
 A_f=\sum_{g\in F}\bigl(\|f_g\|_1+\operatorname{Var}f_g\bigr).
\]
分部积分的测度形式给
|\widehat f_g(ω)|≤min(||f_g||₁,Var(f_g)/|ω|)，故
\[
 |\widehat f_g(\omega)|\le
 \frac{\|f_g\|_1+\operatorname{Var}f_g}{1+|\omega|},\quad
 |K_\zeta(\xi,\eta)|\le\frac{A_f}{2\pi(1+|\xi-\eta|)}.
\]
对ξ≥0、η<0积分两个平方，得到
\[
 |d_\zeta(\xi)|\le\frac{A_f^2}{2\pi^2(1+\xi)},\qquad
 \|d_\zeta\|_2\le\frac{A_f^2}{2\pi^2}.                         \tag{15}
\]
d_ζ此时不保证L¹，原未加权迹缺陷也不保证迹类。仍可对h∈C_c^∞定义(10)，并由Plancherel得到
\[
 |\Psi_h^{\rm reg}(\zeta)|\le
       \frac{\sqrt{2\pi}\,A_f^2}{2\pi^2}\|h\|_2.              \tag{16}
\]
其时间分布是一个L²函数；不声称逐点连续，也不在一般L²代表上指定k(0)。

这一定义有实际算子解释，不是自由补项。假设(7)仍给有界u_ζ（在下一节极限中它确为酉），
记m=\widehat h|_{[0,\infty)}，R_h=M_{|m|^{1/2}}，V_h=M_{m/|m|}，零集上相位取0。
(15)的核估计保证Qu_ζPR_h及Qu_ζ*PR_h均为HS。
因此，对有界的B_ζ=Pu_ζ*Qu_ζP−Pu_ζQu_ζ*P，正则化读出是
\[
 \Psi_h^{\rm reg}(\zeta)=
   \operatorname{Tr}\bigl(V_hR_hB_\zeta R_h\bigr)
   =\int_0^\infty m(\xi)d_\zeta(\xi)d\xi.                     \tag{17}
\]
两个R_h夹住的正项分别为HS平方，所以迹类。没有宣称W_hB_ζ本身必然迹类。
虽然R_h、V_h对h非线性，最后的积分式证明合成读出对h线性。
当源平滑时，合法循环使(17)准确等于原(10)。

## 8. 实际近锐Green族的极限，不丢掉算子来源

取0<ε≤ε₀<L，固定从0平滑单调上升到1、两端平坦的θ:[0,1]→[0,1]。
令c_ε在[0,ε]为sin(πθ(t/ε)/2)，在[ε,L]为1，
在[L,L+ε]为cos(πθ((t−L)/ε)/2)，其他处为0。
则c_ε∈C_c^∞，Σ_n c_ε(t−nL)²=1，||c_ε||∞=1，Var(c_ε)=2。
它几乎处处趋于c₀=1_[0,L]；端点值不影响算子。

全部f_{g,ε}的群支包含于固定有限集合
F={ (n,b):b=0,1，|nL+bM|≤L+ε₀ }，
支撑在[0,L+ε₀]，有
\[
 \|f_{g,\varepsilon}\|_1\le L+\varepsilon_0,\qquad
 \operatorname{Var}f_{g,\varepsilon}\le4,\qquad
 A_{f_\varepsilon}\le |F|(L+\varepsilon_0+4).                 \tag{18}
\]
L¹支配收敛给f_{g,ε}→f_{g,0}，所以Fourier系数逐点收敛；共同(15)包络再给
d_{ζ,ε}→d_{ζ,0}在L²(0,∞)中收敛，且对ζ一致。
原因是F有限，相位模长为1，频率积分可对每对系数分别支配收敛，再取有限和。
因此(10)的平滑源读出趋于(17)，相应时间密度在L²中收敛，不会产生周期原子。

还有直接算子核验：各乘法系数及其平移的伴随都几乎处处有界收敛，
故u_{ζ,ε}、u_{ζ,ε}*分别强收敛于(7)的u_{ζ,0}及其伴随，极限仍酉。
但不由此推出Hardy压缩Fredholm或继承420指数束。
对固定h，带R_h的两个非对角块由共同核包络在HS范数中收敛，
故V_hR_hB_{ζ,ε}R_h在迹范数中收敛到(17)的算子。
这把极限读出绑定到真实近锐源，而非只给一个任意分布模型。
(13)的环面平均零值在极限中也保持。

## 9. 与原周期分布的严格比较及量化逃逸条件

原414在h(0)=0时的非零时间部分为
\[
 \mathcal P_{p,q}(h)=
 \sum_{a\ne0}L\rho_p^{|a|}h(-aL)
 +\sum_{b\ne0}M\rho_q^{|b|}h(-bM),\quad
 \rho_p=p^{-1/2},\ \rho_q=q^{-1/2}.                           \tag{19}
\]
不同素数保证aL=bM除a=b=0外不成立。两套格点在固定有界区间内有限，
故可取δ>0，使−L的δ邻域不含0或其他周期。

固定ψ∈C_c^∞((-1,1))，ψ(0)=1；取
h_ε(s)=ψ((s+L)/ε)，0<ε<δ。则
\[
 \mathcal P_{p,q}(h_\varepsilon)=L\rho_p,\qquad
 \|h_\varepsilon\|_1=\varepsilon\|\psi\|_1,\qquad
 \|h_\varepsilon\|_2=\sqrt\varepsilon\|\psi\|_2.               \tag{20}
\]
任何固定迹类B、迹范数总预算有界的参数平均或其分布极限，
由(14)在这些测试上至多为Cε||ψ||₁，不能等于(19)。
对全部ζ、固定共同BV预算的源（包括第8节近锐族及其极限），
由(16)至多为C₂√ε||ψ||₂，仍不能等于(19)。
同一检验也适用于把q项改成负号的固定周期差，因为本测试只看p周期。
这排除的是上述完整测试类上的恒等读出，不是某个单独h偶然相等。

定量地，若在这一测试上声称误差不超过|Lρ_p|/2，则必要有
\[
 \|B\|_1\ge\frac{|L\rho_p|}{2\varepsilon\|\psi\|_1},
 \quad\text{或}\quad
 A_f^2\ge
 \frac{2\pi^2}{\sqrt{2\pi}}\,
 \frac{|L\rho_p|}{2\sqrt\varepsilon\|\psi\|_2},                \tag{21}
\]
分别适用于(14)和(16)的机制。只有在满足该具体随ε测试误差条件时才得到这些速率，
不把一般分布收敛偷换成对变化测试函数的一致误差控制。
带有限参数测度时，右侧相应由迹范数总预算或A_f²·||μ||TV支付。

## 10. 为什么这不排除原全Γ迹，也不是F₁不存在性

原A_N(h)=Σ_g C_NP_gU(h)C_N在插入测试后确为迹类，其准确归一化为
\[
 \frac12\operatorname{Tr}A_N(h)=D_Nh(0)+\mathcal P_{p,q}(h),
 \qquad D_N=(2N_p+1)L+(2N_q+1)M.
\]
特别地，h(0)=0时(19)等于原算子的半迹。
它不是本文已经证明的某个固定迹类B与U(h)的乘积。时间截止不与U_s交换，
而未经测试的全Γ和也不能先当作一个有界或迹类算子。
例如g=0、s=0的单项C_N²在非零时间截止上含非紧乘法算子，
已经不满足本稿固定迹类B的前提。因此本稿与414相容。

这里停止“固定Hardy迹缺陷加一个时间权重（含上述近锐BV极限）直接恢复原周期分布”的候选。
若继续这一路，必须提供超出上述界的实际奇异输入、不同的全群传递或具有明确归一化的相对正则化，
并保留原Cn、完整Γ及测试依赖。自由添加目标原子、把权重按定义宣布循环、或再换一个普通指数生成元均不构成新输入。

## 11. 来源与形式化的准确范围

Connes固定v1的分布迹讨论区分几何分布与普通算子迹，局部定理采用带参数截止及有限部分；
这些是已有背景，不能当作本候选已经接合全局RH的证明。
本轮重读PDF16–18、22–24、28，目视18；也注意原文明确写固定R_Λ为迹类，
故不能把所有外部截止都说成“只有h平滑后才迹类”。本稿排除范围由自身(14)–(21)的范数／BV条件决定。
[原始版本](https://arxiv.org/abs/math/9811068v1)与[本地原件](../literature/f1/connes-trace-math-9811068v1.pdf)不重复下载。

[WeightedTraceDefect.lean](../formal/F1/Analysis/WeightedTraceDefect.lean)的三条无admission恒等式核准
乘法缺陷结合律、反对称缺陷的三项边界及带权交换子转移；
[内核报告](../formal/checks/weighted-trace-defect-verification.json)已通过固定Lean4.32.2，仅依赖propext。
HS、迹的定义域、Fourier常数、C₀／L²极限及原子比较仍由本稿分析证明和后续独立逆审负责。
完整主除子、两次数、RR、通常ζ的正性和目标F₁结构非空均仍开放。

## 12. 独立复核、定义补明与下一动作

[原核独立推导](../reviews/2026-09-21/f1-weighted-hardy-kernel-derivation.md)保留全部交叉项与固定迹类预算；
[BV极限独立复核](../reviews/2026-09-21/f1-weighted-hardy-bv-limit-review.md)核准§7–8及量化界；
[全文独立逆审](../reviews/2026-09-21/f1-weighted-hardy-full-review.md)覆盖十一节、(1)–(21)，对应原稿SHA256
cdc466cbb1ee8b280c742eb79ee1fe184e280e9d39761303d165e6e6dd642ee0。
唯一P3建议为§10显式补出原A_N的半迹和D_N归一化，已据414式(23)补明；公式(19)–(21)不变。

依独立复核补明三个定义边界：Var(f)始终是整个实线上的分布变差||Df||TV，包含端点跳跃；
(17)的有界乘法算子写法用于当前C_c^∞测试，虽标量读出延拓到L²，不自动把一般L²测试的R_h当有界；
参数测度及固定B独立于测试函数h，不能按每个h重新选择权重再声称得到同一分布。

[三项Lean报告](../formal/checks/weighted-trace-defect-verification.json)的SHA256为
9d261d1c4ddd8b33d7e376580d0544f210f1fddc4ff8abd830792484c59bb770；
[来源增量核读](../reviews/2026-09-21/f1-weighted-hardy-source-read.md)保留原文与本排除范围的差别。
下一项执行[实际径向有限部分迹及双边界异常](../reviews/2026-09-21/f1-radial-finite-part-relative-trace-next-proof-plan.md)，
从真实定义域和非循环异常检验原Cn、T、全Γ及周期读出，而非给当前缺陷自由补回目标分布。

采纳闭环：独立复核确认半迹归一化及三项定义补明准确、未扩大结论，主稿与修订快照均为 17494 字节，SHA256 为 633dafab93c8f4e26cf50620f5cce6914e6842b2f3f0f7666ffae7089b2ca80d；见[采纳复核全文](../reviews/2026-09-21/f1-weighted-hardy-adoption-review.md)及[原始报告](../reviews/2026-09-21/f1-weighted-hardy-adoption-review.raw.json)。
