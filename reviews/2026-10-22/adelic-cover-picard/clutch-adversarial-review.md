# 实际双位指数 clutch：独立逆审与源／容量范围

2026-10-22。独占逆审稿；只修改本文件，不改 STATE、cadence、合同或其他代理原件。
已恢复 README/STATE、check/show、G20261014、C036、D20261022G 与 frontier；现场新审对象为
[精确 clutch 原稿](periodic-clutch-classification.md)，基础几何核对 [413](../../../notes/413-f1-two-place-boundaries-and-virtual-class-collapse.md) §§1–3。
以下 PASS 只认证明列命题及范围，不认证整个 Picard 群、经典 RH 或独立 RR 容量。

## 1. 审核结果

**主命题在指定范畴成立。** 固定实际 413 覆盖，等变线的同构均覆盖固定 O 上的恒等映射；
在 Wp、Wq 的指定等变平凡线间以 `exp(zx)` 粘合。
其 absolute kernel 恰为 `i[(2π/log p)Z+(2π/log q)Z]`，保持两边界指定 frame 的 kernel 恰为零；
存在 Γ 不变、连续、处处非退化的正 Hermitian metric 当且仅当 Re z=0。
独立重算未找到反例。此为旧实际几何上的一个新的精确子族引理，不声称外部首创或全 Pic 分类。

必须固定三项语义：

1. “相对带 frame”是指定 P、Q 两边界 frame 并要求同构保持它们的范畴。
   它不等于仅取 `ker(Pic(O)→Pic(P⊔Q))`；所有本族线的边界限制都平凡，后者仍按 absolute 的 iΛ 识别。
2. 参数商 C/iΛ 的 quotient topology 不是整个实际 Picard stack 的拓扑定理；
   更不能自动将它当 Hausdorff Hilbert／正能量参数空间。
3. Γ 不变 metric 的不存在，不是底层 O 上连续正 metric 的不存在。
   不变性和两边界非退化性是必要且在证明中实际使用的前件；奇异、加权或退化边界 metric 未被排除。

另见 §6 的 idele 拓扑勘误；它不影响上述使用真正开片 Wp/Wq 的证明。

## 2. 对 kernel 证明的独立重算

记 L=log p、M=log q。每个 side quotient Z_L 的螺旋加圆描述确实是
`x↦(e^x,e^(2πix/L))`，负端圆的每个相位都可由 x→−∞ 逼近。
`{x≤C}∪S¹_L` 为紧集。若 side unit a 的边界限制提升为 L 周期 A，
则 `a(x)-A(x)→0` 在整个负尾一致成立：否则坏点列的圆相位有收敛子列，
对应两函数都趋同一边界值，矛盾。边界无零且紧又给负尾上 a 的正上下界。
该论证不偷加正端有界性，所有连续 side gauges 都在范围内。

若指数 transition 可平凡化，必有 side units a、b 满足

\[
 e^{zx}=a(x)/b(x).
\]

这是充分也是必要条件：任何 base-fixed 等变同构在两个指定平凡片内的系数都 Γ 不变，
因而分别下降到 Z_L、Z_M；不存在遗漏的额外等变 gauge。
负尾正上下界立即排除 Re z≠0。

对 z=iλ，设 A、B 为周期边界值，则
`e^(iλx)B(x)-A(x)→0` 当 x→−∞。
这一步应读作整个负尾收敛，而非仅沿一个相位子列；上一紧性论证已经支付这个量词。
取无界正整数 t_n，使三相位 λt_n、2πt_n/L、2πt_n/M 同时模 2π 趋零。
紧环面的 pigeonhole／同时逼近给这样的列：若近返回时间无界，取子列；
若任意精度下反复出现有界返回时间，则其中一个正整数为精确周期，取其倍数。
沿 x−t_n 把负尾等式传回固定 x，得到

\[
 e^{i\lambda x}B(x)=A(x)\quad\text{对全部实 }x.
\]

连续无零周期函数的绕数分解给
`A=e^(2πimx/L)e^α(x)`、`B=e^(2πinx/M)e^β(x)`，其中 α、β 为有界连续周期 logarithms。
于是 `i(λ−2πm/L+2πn/M)x−α(x)+β(x)` 是连续的 2πiZ 值函数，必常数。
有界项迫其线性系数为零，故 λ∈Λ。反向的周期 units 在相应 side 上实际延拓，立即给平凡化。
对两个参数取差，即得全部所称子族分类。

明确非零类 `z*=iπ/L` 也正确：若 π/L∈Λ，则
`1/2=m+nL/M`；L/M 无理迫 n=0，继而 m=1/2 不可能。
其 absolute 类恰为非零二阶挠类，因为 2z*∈iΛ。
L/M 无理只用不同素数的唯一分解，不读取任何 ζ 零点信息。

## 3. 相对 frame、metric 和同伦风险

保持两个 boundary frames 时，允许的 a、b 在相应边界都为 1。
一致负尾渐近遂给 a/b→1，故 e^(zx)→1。
这仅在 z=0 时可能；纯虚非零参数沿振荡序列已否定极限存在。
充分性 z=0 显然。因此 framed kernel0 无须任何分离性／RR 假设。

若 metric Γ 不变，两 side metric 系数下降为 Z_L、Z_M 上正连续函数，
其负尾比值必有正上下界；transition compatibility 要求该比值为 |e^(zx)|² 或其逆，
故 Re z=0。反向用两片常数 metric1 即可。这是真正的 invariant metric 判据，
并不由 fiber positivity 推出 primitive intersection／Weil positivity。

原稿正确保留全 O 非 proper。每边 proper 不推出全覆盖 proper；
413 的近共振群元例正排除这种偷换。`s↦exp(sz*x)` 确实给从平凡到非平凡的等变连续线族。
普通 paracompact Hausdorff 底空间上 bundle 的同伦分类不能无前件地移到此非 proper 等变范畴。
本稿亦未给 crossed-product 中的有限投影、C* Pic 元或 K 非零类，不能与 413 的 projectionless 结论混读。

## 4. 全主关系、537 非根与原 norm 费用

405 的物理坐标为 r=e^(u/2)f；S_exp 乘 e^(u/2) 后仍是同一函数集合，拓扑移权另记。
405 的实际 h=Eη_h>0，H=e^(u/2)h>0，p=(D²+D)h 给真实主关系

\[
 P=e^{u/2}p=(D^2-1/4)H\in P_c.
\]

所有带权边界项由 405 的 S_exp 估计消失；因此
`μ±P=0`，而 `ℓ0(P)=−(1/4)∫H<0`。
这里不需要 ζ(1/2) 的符号、不使用 RH，也没有将谱迹关系 h 本身误当双矩零主关系。
故 z(r)=ℓ0(r) 的 line map 已失败全主关系：其主关系像有非零实部，absolute 和 framed 都非平凡，
且不存在上述 invariant 非退化边界 metric。

改为实源上的 z(r)=iℓ0(r) 虽给 unitary metric，也不修复关系：
可把同一 P 实缩放到标签 π/L，得到上一节明确的非零 absolute 类。
这里避免了“碰巧某个标签落入稠密 Λ”造成的错误单点推断。

537 付固定半窗17/16的全部 complex 完整 Q 下界。
取非零 ψ≥0、compact smooth，r0=(D²−1/4)ψ，则 r0≠0、μ±r0=0、Qζ(r0)>0，
`ℓ0(r0)=−(1/4)∫ψ<0`。
所以 mean 标签看见此确证非根，却不消全 Pan；degree-only 标签则消 Pan 但杀掉 r0。
两门必须在同一个候选上同时通过，不能把不同标签的优点相加消费。

对 supp r⊂[−A,A]，

\[
 |\ell_0(r)|\le\sqrt{2A}\|r\|_{du}
 \le\sqrt{2A/\log2}\|r\|_{Dlog}.
\]

第一 du dual norm 为精确 √(2A)，由 smooth compact 近似常函数取到 supremum；第二只是合法 upper。
对一般标签 ∫e^(zu)r，du dual norm平方为 ∫_[−A,A]e^(2Re z u)du，非零 Re z 时等于 sinh(2ARe z)/(Re z)。
在 cover 另窗 |x|≤B 上，指数及其逆 bounded by e^(B|Re z|)，这是 frame 的 chart upper，
并非所有源 lift 的必要成本，也不是全 adele／全箭头容量。
纯虚相位的 global uniform multiplier norm 对不同频率相距2；compact-open 连续不能报成全 bulk 算子范数 Lipschitz。

进一步，对线性 ℓ 要求本族 absolute 类消全部 Pan，必有 ℓ(Pan)⊂iΛ。
Pan 为向量空间，而 iΛ 可数；只要 ℓ(q)≠0，所有标量倍形成不可数直线，不可能包含其中。
故必须精确 ℓ(Pan)=0。此步骤不需要把非 Hausdorff 的 C/iΛ 当 Hausdorff target。
若 ℓ 又在全线原 du／Dlog 连续，553 的 Pan 稠密性才迫 ℓ=0。
Fréchet／变域／有费 cofinal／非线性或额外几何数据未被此判据排除；
单凭因式分解旧 source quotient 本身也不是循环的充分证据，缺的是独立的新结构和容量比较。

还必须保留一个明确的合法 nonlinear 对照：`z(r)=i c Qζ(r)`，c 实，
由完整旧 Q 的全 Pan 根空间性质确实消所有 principal；取
`c=π/[L Qζ(r0)]` 又把537 r0送到明确非平凡的 iπ/L 类。
固定窗上旧 form upper 支付 `|z(r)|≤|c|C_A||r||²_Dlog`，局部参数连续也真实。
但正、负 Q 都给 unitary line metric，线本身没有把 Q 的符号变成独立有效性／容量。
这是完整旧 Q 的坐标包装，不应否定为非法映射，也不应报道为独立正性新输入。

## 5. 连续正反与函数域控制实际说明什么

已付连续系统 Z_c(s)=1+c/[s(s−1)]，d=c−1/4=±1/16，
其完整 primitive 代数 R_d=C[w]/(w²+d)、w†=−w 给
`Q_c(r)=2|A_r|²+2d|B_r|²`。
取 even φ≥0、非零、支撑(−1,1)，g=uφ，r=(D²−1/4)g。
则 μ±r=0、ℓ0(r)=0、A_g=0，而 B_g>0：正 d 用 u sin(√d u)/√d，负 d 用对应 sinh。
分部积分给 a_r=−c a_g，于是 Q_c(r)=2dc²B_g²，一段严格正、一段严格负。
同一 mean-line 标签在两者都平凡，不能看见 primitive 符号或覆盖。
这些 continuous 模型没有被赋予经典 adelic base；这是对候选设施推理的控制，
而非声称它们天然具有经典 O。Γ=0 是其给定完成化，并非删掉经典 Γ。

函数域 C/F5:y²=x⁵−x+1，P=(0,1)、Q=(1,1) 的旧真例
`L0=O(P+Q−2∞)` 非平凡，h0(K)=2 而 h0(K⊗L0)=1。
这检查了“非平凡 degree-zero moving 影响同源截面”的真实目标，
不是本连续 equivariant clutch 已支付的后果。regular-unit sheaf、DVR 消失过滤、proper pushforward、
实际有效化和 mixed 容量仍需独立给出；正 fiber metric 或一参数非平凡 Pic 类都不能替代它们。

经典完整目标的三片在本轮均未被新计算删减：

\[
\begin{aligned}
Q_\zeta(r)={}&2\Re(\mu_+r\,\overline{\mu_-r})
 +[\psi(1/4)-\log\pi]\|r\|_2^2\\
&+\int_0^\infty {e^{-v/2}\over1-e^{-2v}}
  \|\tau_vr-r\|_2^2\,dv\\
&-2\sum_{p,k\ge1}(\log p)p^{-k/2}
  \Re(r*r^*)(k\log p).
\end{aligned}
\]

Γ integral coefficient independently matches Γ(t)=Re ψ(1/4+it/2)−logπ：
`||τ_vr−r||²` 的 Fourier multiplier 是2(1−cos tv)，恰给 digamma 差。
全部 proper powers、contact constant、双 pole 及 complex mixed 保留。
尚无本线族的 metric／局部消失／capacity 身份等于该完整预算的证明。

## 6. 必须纳入 root 的范围勘误与结算意见

[source-norms-and-controls](source-norms-and-controls.md) §1 当前开头将
`U=[A_Q×/Q×]` 称为“实际变换群胚及其 idele 开部分”，应改为 idele 群胚的连续限制／映入。
idele topology 比 additive adele 子空间拓扑强；A_Q× 不是 additive A_Q 的开子集。
[actual-cover-and-line-cocycles](actual-cover-and-line-cocycles.md) §1 已准确区分这点。
这项改字不撤销 full-stack character 线、实分量非零开集上的 frame 或本次 Wp/Wq 真开覆盖，
但不能让错误“开部分”留到下游的 sheaf open-cover 消费。

可 root 消费的新严格结论是本具体指数子族的 exact kernel／framed kernel／invariant metric 判据。
它修正“没有非平凡 actual relative Pic 数据”的过强表述；全 Pan／537 map 可由上述旧 Q 包装给出，
但尚无独立于这种旧输入包装、并进入同一整模型局部消失过滤或平方 RR 容量的原源比较。
按用户止损，mean、degree-only 和单纯旧谱标量重新标线的入口应停止；
不把它们扩成所有非线性／强拓扑／源依赖 actual Pic 方法的不可行定理。
strong-old 542+555→557 的 whole leading4/5 上预算、actual core/coupling/Ξ 与宏观完成门均未变。

**逆审结论：限定 PASS；上述拓扑文字勘误应在最终 root 收据前修正。**
