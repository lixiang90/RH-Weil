# 451. 实际 κ 反馈的三次边界与全族延拓

2026-10-07。状态 [T/R]，全文独审待绑定。新的实质输入是
[450](450-plain-kappa-extension-and-actual-capacity.md)从底层 [R] 重证的
κ∈[37/50,1] plain moment；不是仅在已付几何里再次调 b。
本稿继承 445 明列的原输入包和 whole finite-order Hecke 7/8 bootstrap，
不独立认证外部整篇证明、kernel、RH 或新的简单临界线比例。

## 1. 精确命题与依赖

令 e_* 为
\[
 p(e)=657e^3-954e^2+21e+20=0
\]
在 (1/6,167/1000) 内唯一的根。它被以下有理区间严格隔离：
\[
 16683858898627/10^{14}<e_*<16683858898628/10^{14}.
\]
定义
\[
 \sigma_*=\frac{11}{12}-\frac{e_*}{4},\qquad
 \kappa_*=\frac56-\frac{e_*}{2}=2\sigma_*-1,
\]
\[
 b_*=\frac{5040e_*\kappa_*^2-900e_*\kappa_*+25e_*
              -432\kappa_*^2+36\kappa_*+3}
 {3312\kappa_*^2-936\kappa_*+67}
 =\frac{-5181+156335e_*-387630e_*^2}{81941}.
\]
于是 σ_* 是三次方程
\[
 7884\sigma^3-18819\sigma^2+14643\sigma-3686=0
\]
的指定根，小数仅作方向说明：
\[
 \sigma_*=0.87495701942009894612860385056\ldots .
\]
这严格小于已交付自由 b 边界
σ_0=(1507−2√921)/1653≈0.874957069799。
两者比较由各自有理根区间证明，不依赖浮点数字。

**相对命题。** 假设 445 的明确原 [R]，并使用 450 已重证的 lower-κ
moment，则指定有限阶 Hecke L 函数族在 Re s>σ_* 无零。
原 principal 极点允许，边界线排除。imprimitive Euler factors 与二次
Dirichlet transfer 按相同 [R] 得全部 Dirichlet 族及 zeta 的同一严格边界。

源固定 commit adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical
LF SHA-256 为 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
原 69999 与自由 b 论文保持交付版本，不修改任何旧哈希绑定。

## 2. 同一物理探针与完整低侧

几何仍为
\[
 l_x=(1-e_*-b_*)/2,\quad l_y=(1-e_*+b_*)/2,\quad
 h=(1+3e_*+b_*)/2,\quad M=1-e_*.
\]
使用原补偿子集、原 q_(p_J)^(-3/2)、同一 X,Y,Z 重标度、
shared prime windows、ray conditions 及 finite compensation。
同一双留数的 Mellin exponent 为 C_b(s)=s−2/3−b_*/6。

449 的 generic reflected energy 与完整第三项 Gram 推导只要求已显示的
长度和 sector 前件，不依赖 κ。这里逐个重核：
1/6<e_*<1/5，b_*>0，M−2d_J≥1−3e_*>0，
l_x−d_J,l_y−d_J>0，P_a≥1，full-J Gram gap>2/25。
同一
\[
 F(d)=-d+\tfrac12(11b_*/6-l_y+d)_+
           +\tfrac18(5e_*-1+d)_+
\]
的每个斜率≤−3/8，故最大值在 d=0。完整 low exponent 是
(1−e_*)/4−b_*/6，恰为 C_b(σ_*)。不得更换 normalizer 或只保留 Gram 的前两项。

## 3. 参考 κ 的连续证书

此节 κ_* 只是参考包络的代数参数，不在 β_*>σ_* 反证中作为 analytic input。
令 y=1/2−x≥0、c=1/(3κ_*)，写
\[
 D=(5/2-c)+(1+2c)y,\quad
 P=(1-c/2)+2y+2cy^2,\quad J=(5/6-\delta)D+\delta P .
\]
记 K=−1/4+5e_*/4+b_*/6、W=1/2+3e_*/2−e_*y。
原完整 high accounting 在 d=h 的参考指数为
\[
 E_*=K+(1/2+e_*)\delta+e_*\delta x-h(1-R_{*,\kappa_*}).
\]
直接展开给
\[
 -2JE_*=A(y)\delta^2-B(y)\delta+C(y),
\]
\[
 A=-2(P-D)(W-h)+hP,\quad
 B=2K(P-D)+\tfrac53D(W-h)+\tfrac56hP,\quad
 C=-\tfrac53DK .
\]
这些公式完整保留第三项与 actual whole-slot mean q。

一般 e,b,κ 下，Q_0=4A(0)C(0)−B(0)^2 对 b 的极大点是第1节
b_* 的一般式；极大值为
\[
 -\frac{25(6\kappa-1)^2(15\kappa-2)
 [(1314\kappa-159)e^2-(36\kappa+6)e-30\kappa+5]}
 {162\kappa^2(3312\kappa^2-936\kappa+67)} .
\]
代入 κ=5/6−e/2，方括号为 −p(e)，故 Q_0=0。
在第1节有理隔离区间，通过 rational interval Horner 可严格验证：
A 的四个系数及 C 的两个系数均正；Q=4AC−B^2 的 Q_1,…,Q_4 均正。
精确系数在[审计输出](../output/hybrid-kappa-feedback-exact-audit.json)中
用基底 (1,e_*,e_*^2) 的有理数完整列出。

故连续地，对 y≥0 和任意实 δ，
\[
 -2JE_*=A(\delta-B/(2A))^2+Q/(4A)\ge0 .
\]
真实 rectangle 中 J>0，从而 E_*≤0。唯一等号为
\[
 y=0,\quad \delta_*=(5-9e_*)/(6+18e_*)=B(0)/(2A(0)),
 \quad R_{*,\kappa_*}=2/3 .
\]
δ_* 严格在 (1/50,3/4) 内。有限模型不用于外推这个连续结论。

## 4. 实际 κ 的准入与反馈费用

定义 β_* 为全部 primitive finite-order Hecke nontrivial zero 的实部
上确界，并包含 1/2、排除 principal pole。假设 β_*>σ_*，
Δ=β_*−σ_*>0。原 whole-family 输入给 β_*≤7/8，所以
\[
 \kappa_{\rm act}=2\beta_*-1\in(\kappa_*,3/4]\subset[37/50,1],
 \qquad \kappa_{\rm act}-\kappa_*=2\Delta .
\]
所有 positive-slot moments 真正调用 κ_act，满足其
β_*≤(1+κ_act)/2 条件；绝不偷用 κ_* 的未成立零自由前件。

450 的 derivative bound 在整个 actual rectangle 一致给
0≤R_(κ_act)−R_(κ_*)<Δ/25。
同一几何相对于 C_b(β_*) 的 high exponent 因而是
\[
 E_{\beta_*}(h)=E_*(h)-\Delta+
 h\{R_{*,\kappa_{\rm act}}-R_{*,\kappa_*}\}
 \le-24\Delta/25 .
\]
这个 Δ 在 mesh、K 和 target 之前固定。

actual selected range 1/2≤d≤h 的完整表达为
\[
 K_{\beta_*}+(1/2+e_*)\delta+e_*q-h(1-R)
 +(d-h)(R+\delta/2-17/50),\quad
 K_{\beta_*}=2/3+e_*+b_*/6-\beta_* .
\]
R≥1−δ、δ≤3/4，使斜率≥57/200>0，故 endpoint 控制全部该范围。
取 ζ=Δ/32，上界斜率<2 使 h 至 h+ζ 的费用≤Δ/16；
中央在其他真实 losses 之前仍留下至少 359Δ/400。

## 5. 全部物理范围与 strict slots

逐项有理区间验证如下固定前件，未照抄旧参数的余量：
\[
 l_y-e_*-11b_*/6>2/25,\quad 5e_*-h-\zeta>1/50,\quad h+\zeta<1,
\]
\[
 E_{\rm floor}=-6/25+(32/25)e_*+b_*/6<-1/200,
\]
\[
 E_{\rm middle}\le-71/600+(329/400)e_*-(421/1200)b_*<-1/50,
\]
\[
 E_{\rm small}=(13/75)h-l_y/2+63/5000<-2/25 .
\]
floor 沿 δ=1/50、R=1 的原无槽估计；middle 沿原
R=76/75−2δ/3，不制造 witness；small 相对 C_b(β_*) 直接付固定余量。
ζ≤(e_*−1/6)/128<1/384000。

实际 inverse/plain crossing 已由450重证。其 r≥3/5 的第二 inverse
width≥1/5；plain m≥1/3，全部供给 z_M,z_P<1/5。
现在 ell/(h+ζ)>1/5，比所需供给严格大。先固定 moment/count losses、
capacity decrement ν_0、rounding 和 uniform mesh，再取 even K 与原 disjoint
prime windows，后取 amplitude widths。r≥1、m≥1/2 与 zero capacity 的
原 no-slot endpoints、Θ exceptions、自然零延拓、whole conjugation、同一
cumulative T_1/2 和全部 profile/height 费用保留。

## 6. Euler、principal 和 outer 的重新核对

新的 σ_*−3/50>81/100，σ_*−1/20>82/100。
沿原 local coefficient tables，在同一 D2*(σ_*) 上支付 general good/ramified
项，4−6s−6z 保留 θ=(−Re w)_+；D1 中 epsilon_H=min(epsilon_0,1/50)。
完整 tuple 保留 G_p 的系数式；仅在已证明近1的 principal/dynamic 域使用 quotient。
whole-bin 先 global contour，再 buffered local partitions。

σ_*+1/2>4/3，small rows 以 D1(1/3) 重新核局部界；
不直接引用写成 D1(3/8) 的旧 small lemma。
large rows 在 (2,2,z_infty) 用完整绝对 tuple，其原 B_0
=7/4−3e_*/4+b_*/4。先 ζ，再目标前固定足够大的 z_infty 和所有 real exponents，
再选小 losses 和高度阶。completed c n^3 sums 不被误称有限。

principal 双留数仍是同一 c_S A_T 和同一个
H_η=∏_(p∉S)H_p(s,1,1/6)。原 positive majorant 以目标前 P_0 固定
|H_η−1|≤1/2，目标后扩大同一 S 只改善它。
fixed-ray asymptotic 给 A_T 最终非零且逆为 subpower。
相同 global s move、w=19/20、z=33/200、主 s 线仅右移至2，给真实正余量
m_w=l_y/20、m_z=h/600、μ<σ_* min_i ell_i。

## 7. 统一量词与反证闭合

几何、β_* bootstrap、Δ 和 κ_act 均先于 target 固定。以 Δ 的小份选择
count/moment losses、ν_0、mesh、rounding；uniform κ lemma 的 mesh 此时
已可选择，不能在 K 之后反向选它。随后选 even K、固定 slots，再取
μ=σ_*e_*/(2K)>0、amplitude/prime/buffer losses。
中央其他总费用<Δ/4，floor/middle/small 各保留至少一半固定 margin。

取 m_0=min{Δ,m_w,m_z,μ,1/200,1/50,2/25}、m=m_0/4。
目标 η 确定后才固定最终 arithmetic data、同一 S、internal Sobolev/height 阶，
产生 finite A_η,B_η 和 actual detector ceiling τ_(0,η)>0。
external tail order N 后选，不改变内部阶。
同一 normalized physical probe J_η 和 principal f_η 不含 cutoff T_1，且
\[
 |J_\eta-f_\eta|\ll_{\eta,N}
 Z^{C_b(\beta_*)-m}(1+T_1)^{A_\eta}+Z^{B_\eta}T_1^{-N}.
\]
选 τ_η≤min{1/10000,τ_(0,η),m/[4(A_η+1)]}、足够大的 N_η，
再 eventual Z threshold，得到共同 σ_hi=m_0/8>0。
完整 low 和 A_T 逆的总 loss 取 ω=Δ/2：
|J_η|≪Z^(C_b(σ_*)+ω)，ω<Δ。

J_η 只在足够大 Z 定义即可；f_η 在全正轴由同一 principal Gaussian integral
定义，小 Z 的右移与 rapid decay仅应用于 f_η。
445 的 Mellin/Fourier 识别由 C_b 斜率1逐式重放，初始识别线在2；
大 Z 的 saving 给 Re s>β_*−epsilon_* 上局部一致收敛，
epsilon_*=min{Δ/2,m_0/8}>0。在同一个 S 下 |H_η|≥1/2 排除 numerator 消零。
不要求 supremum attained：它提供实部>β_*−epsilon_* 的目标零点，
与该延拓矛盾。finite Euler deletions 和 quadratic factorization完成上述全族 transfer。

## 8. 证据和继续研究

[精确脚本](../scripts/hybrid_kappa_feedback_exact_audit.py)仅使用有理运算、
模三次多项式的代数域及有理区间；PASS 的149项包括49个有限直接模型。
其连续正性证明是显示的 square completion 和系数 interval 证书，
不是这49个模型。脚本不验证新 plain induction、原分析输入、实际素数、
无穷轮廓、整个源论文、Lean 或 RH。
两份新的完整451审查及最终版本将在后续检查点中绑定。

本稿未计算更高简单临界线比例。实际 four-prime response、
moving residue weights、全部 cross-cell/alias 和 finite-constant fourth moment
仍是另一主接口；不能把这里的 tiny strip gain替代比例预算。
按照用户要求，只有全文独审确认上述新边界后，才另写正式论文记录。
