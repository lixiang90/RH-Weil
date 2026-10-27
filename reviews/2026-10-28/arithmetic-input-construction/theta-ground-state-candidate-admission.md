# 整数theta基态算子的实际定义与热迹首检准入

2026-10-28；root原创定义，G20261027/runtime1793085111/原0c4f。执行O之后“从实际整数theta数据自主生成规则”的动作。本稿只冻结实际公式与待审首检，不宣称准入通过、热迹渐近已证、新数学轮或经典正性。原wind/曲率纵投影/矩阵族不重启。

## 独立数据和唯一固定规则

采用405已付整数theta源
\[
 \eta(y)=\pi y^2(\pi y^2-3/2)e^{-\pi y^2},\quad
 h(x)=2\sum_{n\ge1}\eta(ne^x),\quad
 H_\theta(x)=e^{x/2}h(x)>0.
\]
Hθ实偶、S_exp，全n而非只截n=1；通常ξ(s)=2∫Hθ(x)e^((s−1/2)x)dx。这是已知来源数据，不是未知正极化H，也不以零点坐标选势。

算子坐标x∈(0,∞)，与物理源时间u∈R区分。固定
\[
 w=H_\theta'/H_\theta,\quad
 q_\theta[f]=\int_0^\infty|f'-wf|^2dx,
 \quad f\in C_c^\infty((0,\infty)),
\]
取Friedrichs闭包，形式算子为
\[
 A_\theta=-D_x^2+w^2+w'=-D_x^2+H_\theta''/H_\theta,
 \qquad f(0)=0.                                      \tag{1}
\]
选择半线Dirichlet一次固定，不在看见不利证据后改sector、x尺度、H的幂或常数。Hθ自身在0非零，不是Dirichlet零模。正型、闭性、compact resolvent及无零模均须在首门中实际核；目前不能只凭形式平方就领全部谱设施。

若这些设施成立，记本征值λ_j>0，定义实际正测度与cutoff分布
\[
 \nu_{\theta,T}=\sum_{\sqrt{\lambda_j}\le T}
 (\delta_{\sqrt{\lambda_j}}+\delta_{-\sqrt{\lambda_j}}),
 \quad
 W_{\theta,T}(u)=2\sum_{\sqrt{\lambda_j}\le T}
 \cos(u\sqrt{\lambda_j}).                            \tag{2}
\]
物理源仍r=e^(u/2)f、fullcomplex Cc∞/S_exp，按hat r(t)=∫r(u)e^(−itu)du有
\[
 Q_{\theta,T}(r)=\sum_{\sqrt{\lambda_j}\le T}
 (|\widehat r(\sqrt{\lambda_j})|^2+
 |\widehat r(-\sqrt{\lambda_j})|^2)\ge0.
\]
这是非局部谱生成规则；不要求各层exact消405。每层fixed源的L1费用、fixed窗du/zero-extension Dlog费用与T成长必须单列，不能把evaluation当globaldu有界。谱计数若只得O(TlogT)，足以对fixed compact/S_exp测试给D′/强源逐一极限，但不付moving源或成长窗统一费。

## 最便宜可判门

目标不是证明这个算子“像”Ξ，而是先核其完整Γ热项是否已经不匹配。令
\[
 k_t(u)=(4\pi t)^{-1/2}e^{-u^2/(4t)},\quad
 \Theta_\theta(t)=2\operatorname{Tr}e^{-tA_\theta},
 \quad\Theta_\zeta(t)=W_\zeta(k_t).
\]
完整目标采用563/566/578既定WΓ/FP-contact、全部primepowers及两个pole。由(2)得到的全cutoff极限若等于完整Wζ，则在合法Gaussian运输后须有全部t>0的热迹身份。不能用fixed-window Q_L算子的热迹替代任一侧，也不先假设RH以写Θζ为实平方频率和。

root的**未认证诊断**是正向tail的n=1主项
\[
 H_\theta(x)\sim2\pi^2 e^{9x/2}e^{-\pi e^{2x}},
 \quad V_\theta(x)=4\pi^2e^{4x}+O(e^{2x}).             \tag{3}
\]
如果导数尾和原域允许足够准确的半线计数比较，预期
\[
 N_\theta(T^2)\stackrel{?}{=}
 \frac{T}{2\pi}[\log(T/\pi)-1]+o(T),                \tag{4}
\]
其线性T项可能不同于完整Γ对应的log(T/(2π))。**(3)不代(4)证明；一般leading TlogT也不能认证线性常数。** 其中(3)的H尾和V leading已由10-14 [原g/r_p尾](../../2026-10-14/theta-joint-source/positive-jump-calibration-and-domain-gate.md)相除直接支付，先扣旧，不再当新设施。首门只做这一固定候选的两项热/计数比较：若确实存在非零t^(−1/2)热缺陷，则原正分布cutoff规则不能趋完整Wζ；若常数其实相符或证明不足，准确保留未付身份，不自动续全谱拟合、H幂或其他参数。

Γ侧完整566(13)/(15)已从显式公式支付
\[
 \Theta_\zeta(t)=
 \frac{\log(1/t)-\gamma_E-\log(16\pi^2)}{4\sqrt{\pi t}}+O(1).
\]
其中prime及全部properpowers的Gaussian小t尾、两个pole、指定contact同时保留，不用未经RH认证的实零点计数身份；本轮不重报此式为新结果。势侧仍需独立原证明，若调用新外部定理则须先固定原条件与实际来源，不能凭WKB口号。

## 最强旧与潜在信息差

565的Gaussian基态选择只独立指定Mellin核，不证明theta算子的目标谱身份。566已证明自动C*C的正性不能自动给源热迹，且在continuous控制中明确不匹配；它没有在本稿引用范围内给出(1)这个全整数theta势的热常数或实际不匹配。553不应被强套成逐层D′必须exact Pan；旧577也不是(2)的谱生成规则。所有旧后果必须由独立准入审查再核，不因本段自称新就领资格。

若最强旧已经直接决定实际(1)的同一完整后果，按标准0停止，不开合同。若没有，且(1)确实提供非空独立正D′候选、(4)/完整Γ比较有具体可判信息差，可考虑一个至多1轮的首检合同。它即使给出新的完整候选反例，也不自动成为实质方法类边界或满足长期Goal完成门；whole4/5UPPER、585必要费、独立signed/corecross/primitive mixed责任仍保持。

本稿禁止把未审诊断当proved，不预建C049/586、不计轮或修改cadence。实际准入/下一动作以STATE和独立审查为准。
