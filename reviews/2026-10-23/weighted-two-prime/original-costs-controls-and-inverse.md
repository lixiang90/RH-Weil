# 有权两素数族：原费用、原域、逆费用与正反对照

2026-10-23；独立分支 `/root/weighted_controls_costs_581`。本稿只研究下述指定实际向量，供 root/fresh 消费，不改 STATE 或计轮。接 [580](../../../notes/580-kry-finite-schwartz-boundary-cocycle-and-level-alias-gap.md) 的合法逃逸“有算术来源权的非整格族”；不将其已经证明的单格、有限维或无权双格反测重记新结论。

## 1. 固定对象、权的来源与作用域

仍取 KRY 的 k=Q(√−7)、native arch Gaussian φ* 和固定 Haar，ν=||φ*||²。p=2 在该域 split；q=11 也 split，因为 −7≡4 mod11，且 11 不分歧。以下 p/q 下标都指有理素数，函数域的常数域基数另记 Q，避免混用。

设 ℓ_p=2log p、ℓ_q=2log q，a_jk=jℓ_p+kℓ_q，(j,k)∈Z²。由唯一分解，log p/log q 不可能有理；因此 a_jk 各异且集合稠密。取

\[
 s(u)=\operatorname{sech}(u/2),\quad
 c_a(r)=\int r(u)s(u-a)du,
 \quad e_{jk}=p^jq^k1_{p^jO_{k,p}}\otimes1_{q^kO_{k,q}},
\]
\[
 w_{jk}=p^{-2|j|}q^{-2|k|},\qquad
 J_wr=\phi_*\otimes\sum_{j,k}w_{jk}c_{a_{jk}}(r)e_{jk}.       \tag{1}
\]

其余有限位保持 native，固定乘法 norm 常数记 μ；两指定局部 O 的体积均为1。该权可写成有理 dilation 的对称分母高度
H(j,k)=p^{|j|}q^{|k|} 的 H⁻²；也等于两位局部 lattice covolume 与其倒数之较小者的乘积。它确实由格和两侧伸缩数据给出，不依 Qζ 或未知零点。**指数2仍是显式选择，并未由算术唯一强迫；有算术定义不等于已具算术 capacity 身份。**

原源是全部 complex S_exp，原 norm 是 du 与全线 zero-extension Dlog，即
||r||²_Hlog=(2π)⁻¹∫[1+log(2+|t|)]|r̂(t)|²dt。下面延拓到 L² 只用于计算这些同源实际费用，不能把 finite Hilbert completion 自动当原 Schwartz–Bruhat 域或算术循环域。

## 2. 全源注入、有界与真正支付的原费用

580 已付局部 Gram。两位相乘给

\[
 \langle e_{jk},e_{j'k'}\rangle
   =p^{-|j-j'|}q^{-|k-k'|},\qquad
 \gamma_-\sum|b_{jk}|^2\le\|\sum b_{jk}e_{jk}\|^2
                  \le\gamma_+\sum|b_{jk}|^2,
\]
\[
 \gamma_-=\tfrac5{18},\quad\gamma_+=\tfrac{18}5,
 \quad W_2:=\sum w_{jk}^2
   ={17\over15}{14642\over14640}={124457\over109800}.       \tag{2}
\]

全部 mixed 项由这一真实 Haar Gram 保留。||s||²₂=4，故每个实际源都有

\[
 \|J_wr\|^2\le4\nu\mu\gamma_+W_2\|r\|_{du}^2
                         \le4\nu\mu\gamma_+W_2\|r\|_{Hlog}^2. \tag{3}
\]

这次没有580无权 family 的 actual-source 发散。更准确地，r↦(w_jkc_a(r)) 是 Hilbert–Schmidt map，HS norm²=4W₂；与 (2) 的 synthesis 相复合后，J_w 的 HS norm²≤4νμγ₊W₂。因此 **J_w 是紧的注入算子**。注入证明不读谱：若 J_wr=0，Riesz 下界迫所有 c(a_jk)=0；c=r*s 连续，稠密性迫 c≡0；ŝ(t)=2πsech(πt) 处处非零，再由 Fourier 唯一性给 r=0。

从而每个537 compact 非根都被保留；580 的全单格 alias 源也被新 family 保留。这里“看见”是准确注入，不是统一 norm lower。无限维紧注入没有 L² frame lower，也没有 Hlog frame lower。§5给 actual 源上更明确的费用反测。

## 3. 原域仍失败；两条实际 boundary 评价的费用却已付

两位径向 Schwartz–Bruhat 函数恰是有限个 e_jk 的线性组合：其 compact 支撑及统一局部常值给 valuation 的两个有限界，再作 shell 差分即可。也可由正交 shell 与 (2) 核查 e_jk 的系数唯一性。若 J_wr 落回该原域，则 w_jkc(a_jk) 只能有限非零。稠密集合删去有限点仍稠密，又因 w 全正，迫 r=0。因此

\[
 r\ne0\ \Longrightarrow\ J_wr\notin
 \phi_*\otimes S(k_p\times k_q).                         \tag{4}
\]

这是本条 formula 的实际原域失守，适用于所有非零 L² 源；不是仅由“无限和”一词判断。它不排新的强完成及真正的 Schwartz/cycle 延拓定理，也不排不同基或 source-adaptive family。

但是不能复用580的 origin 例子，声称权没有付任何 boundary 费用。令 F_r 为(1)的有限两位函数。实际绝对和给

\[
 S_1:=\sum w_{jk}p^jq^k
     =\sum w_{jk}p^{-j}q^{-k}
     =\Big(1+{1\over p-1}+{1\over p^3-1}\Big)
      \Big(1+{1\over q-1}+{1\over q^3-1}\Big)
     ={15\over7}{732\over665},
\]
\[
 \|F_r\|_\infty\le2S_1\|r\|_2,
 \qquad\|F_r\|_1\le2S_1\|r\|_2.                         \tag{5}
\]

原有限向量逐项连续且 C₀，故第一式的均匀绝对和给 C₀ 的实际代表；第二式给 L¹。于是 F_r(0) 和其 Fourier 在0的评价 ∫F_r 都有同源原 du 费，分别对应 λ 的 identity 和 Fourier 两腿。固定 native 因子的评价常数需照原件保留。(5)不支付所有 g 的 section 半范数、Eisenstein 总和、Green、算术 principal 或 height 的无限延拓。

405 真实 P=(D²−1/4)H、H>0 的全部平移仍满足

\[
 c_{a_{jk}}(\tau_bP)
 =-\tfrac12\int H(v)s^3(v+b-a_{jk})dv<0.                 \tag{6}
\]

由 (5) 的绝对收敛，F_(τ_bP)(0)<0 且 ∫F_(τ_bP)<0。J_w 仍注入，所以它并未消去任何非零405关系；两条合法边界读出也没有自行变成 principal 取消。它们必须与同一实际相对链的其他边界协同，而不能按定义删去。

若额外假设 fixed bounded linear relative 读出 Π，并令 ΠJ_w 消全部405平移，则553的旧稠密机制仍迫 ΠJ_w=0；这是旧后果，不是本轮新 no-go。它不排非闭边界、强拓扑、无界比较或真正变化的相对对象。

## 4. 除权的实际费用与合法无界 inverse 分开

对每个固定非零 r，c(a) 在某个区间上绝对值≥δ>0，该区间含无穷多个 a_jk。因而

\[
 \sum_{j,k}|c(a_{jk})|^2=\infty.                         \tag{7}
\]

故若解卷积方案是**先将本实际向量逐系数除以 w**，它对每个非零实际源都离开原 finite Hilbert space；此为实际 source 费用，不是 ambient inverse norm 冒充费用。相反，J_w 在其像上确有合法无界 inverse J_w⁻¹:Ran J_w→L²，且每个 J_wr 属其 domain。该 inverse 可以从 weighted dense samples 直接恢复 r，并不必须经 (7) 的无权 Hilbert 向量。因此本稿没有排除有费无界恢复、非 Hilbert reconstruction 或更强原域；需核的是它们到同一循环/相对边界/height 的实际作用与费用。

## 5. 完整 Γ、所有素数幂及两极点的实际高频比较

### 5.1 同一580源：全源注入恢复了，但可见信号指数小

580 的显式源不需取 alias 频率才属于 S_exp。对任意 A>0 令

\[
 R_A(u)=e^{-u^2}\{\sin((A+2\pi)u)
                  +e^{-2\pi A}\sin((A-2\pi)u)\}.        \tag{8}
\]

取 g_A=e⁻ᵘ²sin(Au)；复平移恒等式精确给

\[
 R_A*s=4\pi e^{-\pi^2-\pi A}g_A,
 \qquad \mu_\pm(R_A)=0.                                \tag{9}
\]

所以本 family 在每个实际源上的费用满足

\[
 0<\|J_wR_A\|^2
 \le16\pi^2\nu\mu\gamma_+W_2e^{-2\pi^2-2\pi A}.        \tag{10}
\]

严格正来自本 family 的注入；(10)是同一源的 upper，不是某个全空间 norm lower。若仍取 A=Kπ/ℓ_p，580的p单格全部盲采样继续为零，q和混合通道确实补回信号，但信号受 (10) 控制。

完整经典目标保持 Γ(t)=Reψ(1/4+it/2)−logπ，指定 FP/contact、所有 Λ(p^m)=log p 和两pole。由580已核的Gaussian频包与全 prime tail，

\[
 \|R_A\|^2\to\tfrac12\sqrt{\pi/2},\quad
 \|R_A\|_{Hlog}^2=(\log A)\|R_A\|^2+O(1),
\]
\[
 Q_\Gamma(R_A)=(\log A)\|R_A\|^2+O(1),\quad
 |h_{R_A}(v)|\le4\sqrt{\pi/2}e^{-v^2/2},
\]
\[
 |P(R_A)|\le8\sqrt{\pi/2}\sum_{n\ge2}
       {\log n\over\sqrt n}e^{-(\log n)^2/2}<\infty,
 \quad Q_\zeta(R_A)=(\log A)\|R_A\|^2+O(1)>0.             \tag{11}
\]

prime upper 仅用0≤Λ(n)≤log n，包括所有 proper powers 和无穷尾。pole 在源上精确为零，目标没有删除它们。Γ 的完整 multiplier 先进入原 form，再在该具体源上估计；未用渐近背景替换其 FP/contact。由 (10)–(11)，任何要求 Qζ(r)≤C||J_wr||²+C₀||r||² 的 bounded-energy capacity 比较都失败。若先按 Hlog 归一化，Qζ 保正的非零极限而 J_w 能量趋零，结论更直接。

这不是新的经典正性定理；旧552/579的 Gaussian smoothing 高频机制在该有权实际对象上给出更明确费用。也没有排除独立构造的无界算术 height：若把其值按定义置为 Qζ，只得到等价改写；若由独立交数和 Γ 身份证明，则仍是合法而未付的新输入。

### 5.2 固定537窗的全部 complex 原源也无统一 frame lower

取 I⊂(−17/16,17/16)，非零 h∈Cc∞(I)；在同窗取两个已知模板 v±，μ_i(v_j)=δ_ij。令

\[
 r_T=e^{iTu}h-\mu_+(e^{iT\cdot}h)v_+
                     -\mu_-(e^{iT\cdot}h)v_-.          \tag{12}
\]

两修正系数按反复分部积分为每阶 O_N(T⁻ᴺ)，不用 Q 或零点选择。sech 的各阶导数在实线一致有界，故同样积分分部对**所有 a**一致给 |c_a(r_T)|≤C_NT⁻ᴺ。由 (2)，

\[
 \|J_wr_T\|^2=O_N(T^{-N})\ (\forall N),\quad
 \|r_T\|^2\to\|h\|^2>0,
 \quad Q_\zeta(r_T)=(\log T)\|h\|^2+O_I(1).             \tag{13}
\]

这里两pole由 (12)精确消，fixed窗全部 prime powers 的原du form有有限费用，完整 Γ 给 leading log T。537的固定窗正性是旧资产；(13)只核新family的实际费用，不是新的537定理，也不升级为成长窗。

## 6. 完整解析预算可以保留，但尚未给目标 quadratic identity

若明确使用580校准的 **right-transported** 局部 section，两split位的 normalized e_jk 对应 classical derivative
pʲqᵏφ₀(p²ʲq²ᵏτ)，包括其 constant。于是有限前缀的完整 Mellin 为 ℳ₀(z)B_(r,N)(z)，其中

\[
 B_r(z)=\sum_{j,k}w_{jk}c_{a_{jk}}(r)
                    p^{j(1-2z)}q^{k(1-2z)}.           \tag{14}
\]

由 |c|≤2||r||₂，(14)在 −1/2<Re z<3/2 的闭子带局部一致绝对收敛。这是固定原件的 ℳ₀ 中完整 Γ、全部 prime powers 和原constant的解析运输，而非任意另选 B(z)。标准 extension 在所有负levels与 transported 相同则**不在本稿中假设**；负levels的解析运输也不冒称已有算术循环定理。

即使该 identity 经 root 规范复核成立，也没有证明其 source-dependent multiplier 的有符号逆、405 principal 同构或 Qζ 的 Hermitian quadratic identity。B_r 由 r 线性变化，本身不是 Qζ 的谱行列式，也不保证无零可逆；把输出命名“完整 Weil”不能代付比较。

## 7. 连续正反例与函数域：权没有产生缺少的同对象容量

连续真实 primitive 族使用579/580同一 compact 奇源
r*=(D²−1/4)(uφ_even)。取 d=±1/16 的两段 native 完整 W 分别为2cos(u/4)du和2cosh(u/4)du，含全部Euler repeats、native Γ=0和两pole。对奇 r*，正段值为2|∫r*sin(u/4)|²>0，负段值为−2|∫r*sinh(u/4)|²<0；选φ_even≥0非零即可确保两积分非零。两段具有同一 r*、J_w、(2)–(5) 的正费用，却有相反完整 Weil 号。故 universal weighted Hilbert positivity 没有提供 distribution-sensitive signed 身份。没有连续模型到CM循环的运输，不能称之反驳KRY；也不将 Γ=0 模型冒充保经典Γ的反例。

真函数域 C/F_Q 的两个有限places P,Q' 的 norms 是 Q^degP 和 Q^degQ'，所以本构造的实际步长为2degP logQ、2degQ' logQ，**总是相称**。不能把数域 p=2、q=11 的稠密双步长原样移植。该 raw sampling 的 aliases 不必是错误：完整函数域 Weil 型本来有全部周期 returns，正确 source norm 来自567同一 C×C 上

\[
 E_n=Q^{-n/2}(\Gamma_n-F_1-Q^nF_2),\quad
 -E_mE_n=a_{n-m},\quad a_n=Q^{-|n|/2}(Q^{|n|}+1-N_{|n|}),\quad a_0=2g,
\]
\[
 Q_C(r)=(\log Q)\int_0^{\log Q}
       \|\sum_jr(y+j\log Q)E_{j+j_0}\|^2dy.             \tag{15}
\]

compact 源用统一 j₀ 使实际 Frobenius 图指标非负；全S_exp另依已证 Toeplitz 型完成，不假造负Frobenius。与其 primitive 交数、RR、实际截面乘法和固定容量相接后才得正性；H⁰/H²的全部pole aliases保持。

须区分两种“Poisson 权”：(i)把某个 finite source coefficient 乘 w_j，Gram 变成 w_jw_k a_(j−k)，一般破坏Toeplitz平移身份；(ii)把 a_n 乘ρ^|n|，等于在圆周上用 Poisson核卷积原谱测度，仍正，但改变全部 N_n／trace预算，并将有限 primitive 点谱变成连续谱。这两者均不是原容量不变。这里局部球 Gram p^-|j−j'|q^-|k−k'| 只来自局部体积，其正号/无限rank与由同一点数 N_n 给出的有限 primitive mixed Gram 不同；对它加 H⁻² 权不产生后者。

## 8. 净结论及独立输入

本条有算术定义权确实支付了580没有支付的双densegrid Hilbert实际费用，并恢复全L²注入、全部537及580 alias 非根；identity/Fourier 两条有限boundary读出的原du费也可付。另一方面，它对每个非零源失去原Schwartz域，405两边界仍非零，compact smoothing带来真实 inverse费用，未付同源 signed budget 或 primitive 二次容量。上述 exact 权常数与 source-specific 费用是本family的具体进展；正号/高频机制/FF RR来源本身均是已知资产的本对象核验。

重新准入必须有：强完成中的实际 λ/E′/Green/cycle 和边界复形延拓；405全主关系的真实 principal 同构，同时保537及全S_exp非根；具有与(10)–(13)匹配的无界或额外源数据费用的算术 regulator；同一对象上的截面 lift、局部过滤、乘法与 primitive mixed RR容量；最后是完整Γ、全部prime powers及两pole到该同一二次量的身份。只定义 quotient 或将 Qζ 拉回 J_w 的像可组织等价命题，不能独立支付这些输入。

strong-old 542+555→557 whole leading4/5 负惯性UPPER、actual q/core/coupling/Ξ及长期Goal门均未改变。是否准入统一数学迭代和具体停止，由root/fresh合并其他独占分支后判定。
