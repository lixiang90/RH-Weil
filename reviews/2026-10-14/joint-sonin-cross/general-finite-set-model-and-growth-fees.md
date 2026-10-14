# 一般先固定 finite-S 联合长窗：完整模型与成长费用范围

2026-10-14；只写本独占审查，不改已 final 的 S23 原稿。
恢复 AGENTS/README/STATE/check/show、同 Goal/frontier/C023/AD 战略和 ratio 门；
check/show 结构通过，现场 HEAD `ac4122a4f494be50143cfce1eb1214d7ea5295a2`。
同 G20261014/0c4f≤538、C023 stopped、原 cadence 和 strongest-old4/5保持；
当前原模型与 carrier 稿为 root 核前件阶段，本稿不代 root 消费或结算。

## 1. 量词、norm 和明确结论

**先固定任意有限素数集 F**，\(S=\{\infty\}\cup F\)。原物理 Hilbert 空间经原 unitary
\(w_S/\mathbb F_\mu\) 回到 \(H=L^2(\mathbb R,dy)\)，保
\(U_t f(y)=f(y-t)\)。CCM (58) 对应

\[
 B_F=\prod_{p\in F}(I-q_pU_{a_p}),\quad q_p=p^{-1/2},\quad a_p=\log p,
 \quad W_F=B_F^*B_F,
 \quad b_F(R)=\prod_{p\in F}(1-q_pe^{-ia_pR}).
\]

设 \(P_T=1_{(0,T)}\)、\(G_{F,T}=P_TW_FP_T|_{P_TH}\)、
\(w_{R,T}=e^{iRy}1_{(0,T)}/\sqrt{2\pi}\)。严格有

\[
 \boxed{
 |b_F(R)|^2\langle w_{R,T},G_{F,T}^{-1}w_{R,T}\rangle-\frac{T}{2\pi}
 =-\frac1\pi\Re\sum_{p\in F}\frac{a_p\alpha_p(R)}{1-\alpha_p(R)}
    +O_{F,\gamma}((1+T)e^{-\gamma T}),
 \quad\alpha_p(R)=q_pe^{-ia_pR}.
 } \tag{1}
\]

量词是 \(\forall F\text{ finite}\;\forall0<\gamma<1/2\;
\exists C_{F,\gamma}<\infty\;\forall T>0\;\forall R\in\mathbb R\)。
下文给同一证明和显式常数，不把 S23 的局部断言静默升为一般 F。
空 F 时 \(B=I,G=I\)，左端和主项精确0，也包括在结论中。

原 actual bare density 仍是
\(\rho_F(s)=|b_F(s)|^2\langle k_s,(PB_F^*B_FP|_{\operatorname{Ran}P})^{-1}k_s\rangle\)，
k_s 为 532 的裸 unitary Mellin 求值向量。此式不是 weighted Gamma-completed evaluator。
(1) 只支付 \(P_T,w_{R,T}\) 模型；实际 P/k_s 到模型的 absolute 运输另付。

## 2. 所有 mixed delay 与显式因果费用

令 \(\mathcal N_F\) 为所有 F-smooth 正整数，包括1。原完整 causal inverse 为

\[
 D_F=B_F^{-1}=\sum_{n\in\mathcal N_F}n^{-1/2}U_{\log n},\qquad
 m_F=\prod_{p\in F}(1-q_p),\quad M_F=\prod_{p\in F}(1+q_p).
 \tag{2}
\]

各 geometric series 绝对 operator-norm 可和；有限乘积允许全部换序。
unique factorization 给每个 n 的 coefficient 恰为 \(n^{-1/2}\)，没有 factorial/multinomial
额外 multiplicity。delay locally finite（\(\log n\le T\) 则 n≤e^T）；
\(\log p\) 不能放在共同等距 lattice，但证明从未需要等距纤维。
严格有 \(\|D_F\|\le D_0=m_F^{-1}\)、\(\|W_F\|\le M_F^2\)、\(G_{F,T}\ge m_F^2I\)。

对 \(0<\gamma<1/2\)，记

\[
 A_{F,\gamma}=\sum_{n\in\mathcal N_F}n^{-1/2+\gamma}
 =\prod_{p\in F}(1-p^{-1/2+\gamma})^{-1},
\]

\[
 J_{F,\gamma}=\sum_{n\in\mathcal N_F}(\log n)n^{-1/2+\gamma}
 =A_{F,\gamma}\sum_{p\in F}
        \frac{a_pp^{-1/2+\gamma}}{1-p^{-1/2+\gamma}}.
 \tag{3}
\]

它们均有限；\(A_{F,0}=D_0\)。对 c_x=n^-1/2、x=logn，有
\(\sum_{x>T}c_x\le A_{F,\gamma}e^{-\gamma T}\)、
\(\sum_{x>T}xc_x\le J_{F,\gamma}e^{-\gamma T}\)。
F 的维数只进入这些明确有限 Euler 因子，不影响 tail 证明的量词。

## 3. 同一双边界 proof 对所有 finite F 的核查

令 \(L=1_{(-\infty,0)},H_T=1_{(T,\infty)}\)、
\(Z_F=W_F^{-1}=D_FD_F^*=D_F^*D_F\)。
所有 factors 是 commuting translations 的有界函数，故 normal/commutation 身份真实。
causal B_F/D_F 保持正半线，并互为其有界逆；反向 causal B_F*/D_F* 保持右端左半线。
所以两个半线 inverse 分别是

\[
 P_+(Z_F-D_FLD_F^*)P_+,\qquad
 P_{-,T}(Z_F-D_F^*H_TD_F)P_{-,T}.
\]

该因果性不依赖 |F| 或 delay 可公度。定义

\[
 S_{F,T}=P_T(Z_F-D_FLD_F^*-D_F^*H_TD_F)P_T.
\]

同一 block 减法给 **exact**

\[
 G_{F,T}S_{F,T}-I
 =P_TW_FH_TD_FLD_F^*P_T
   +P_TW_FLD_F^*H_TD_FP_T.
\]

跨窗 delay≤T 的压缩严格零，(3) 控其余全部 mixed paths，故

\[
 \|S_{F,T}-G_{F,T}^{-1}\|
 \le\frac{2M_F^2A_{F,\gamma}}{m_F^3}e^{-\gamma T}. \tag{4}
\]

这不是只保留低阶项的 approximate inverse，也不用常数1属于半线 L²。
W_F 具有有限 propagation \(\sum_{p\in F}a_p\)，但以上 block/residual norm 证明甚至
不使用该长度为统一常数；不因较大的 F 延误或删除 coupling。

同一合法 plane-wave 配对给 whole Z_F 的双和
\((2\pi)^{-1}\sum_{x,z}c_xc_z e^{-iR(x-z)}(T-|x-z|)_+\)。
两个 halfline correction 各趋于
\((2\pi)^{-1}\sum_{x,z}c_xc_z e^{-iR(x-z)}\min(x,z)\)，
每个误差≤\(A_{F,\gamma}^2e^{-\gamma T}/(2\pi\gamma)\)。
所有双和的第一矩由 (3) 绝对支付，无需任何 Diophantine 小除数估计。
因此 \(|x-z|+2\min(x,z)=x+z\) 逐 pair 消去 mixed boundary 项。

令 \(d_F(R)=\sum_xc_xe^{-iRx}=1/b_F(R)\)，
\(j_F(R)=\sum_x xc_xe^{-iRx}\)。完整 geometric product 给

\[
 j_F(R)=d_F(R)\sum_{p\in F}\frac{a_p\alpha_p(R)}{1-\alpha_p(R)}.
\]

这时才出现 additive primepower symbol，不预先相加 single-p 正迹。
合并所有上述误差和 \(\|w\|^2=T/(2\pi)\)，可取 (1) 的常数

\[
 C_{F,\gamma}=M_F^2\left\{
 \frac{D_0J_{F,\gamma}+J_{F,0}A_{F,\gamma}}\pi
 +\frac{A_{F,\gamma}^2}{\pi\gamma}
 +\frac{M_F^2A_{F,\gamma}}{\pi m_F^3}\right\}.
 \tag{5}
\]

故每个步骤在任意先 fixed finite F 上都成立。最终主项的绝对一致 Fourier series 为
\(-\pi^{-1}\sum_{p\in F}\sum_{k\ge1}a_pq_p^k\cos(ka_pR)\)；
非 primepower 的 mixed product/ratio frequencies 不留下该主项的 harmonic。

## 4. 成长费用：sufficient upper 不是必要 lower

先固定 F、再 T→∞（或 actual T=Γ(R) 后 R→∞），(5) 是常数。
F=F_L 成长时必须保留整个 \(C_{F_L,\gamma}\) 和实际 carrier/clipping 运输常数。
上述证明只给充分 upper；如
\(C_{F_L,\gamma}(1+T_L)e^{-\gamma T_L}\to0\) 是一个可消费的充分模型条件。
不是必要条件，失败不表示模型 error 实际非小，更不表示 actual Q 负或 error 不紧。

cofinal Euler factors m_F、M_F、A_F 随集合变化，不能把 fixed-F O 常数静默当全 S 一致。
但 **粗 norm 常数失控不是 actual error 或 signed comparison 的必要费 lower**。
即使某 ambient inverse norm很大，特定 k_R/source 的完整 signed 响应可较小；
已付的联合 cancellation、adapted source、不同 factorization、Γ-relative 费用或使 T 随 F
增长的合法定量运输，都未被本稿排除。若令 γ也变化，须重核 A/J 及1/γ，不能冻结旧常数。

actual finite-F 物理 density、ALL complex source Dlog 延拓、固定源 compact-error、低域 error
符号，以及 cofinal allprime coverage 是不同前件。本稿只处理模型这一项。
由 (1) 或其中 mixed消去不能判整个 joint error 的正负，也不从 fixed-S 复制 535 infinite ±。
fullsigned/core/coupling/Γrelative 小费/通常Ξ仍未付；最强旧4/5与537 fixed窗先扣。
本短审无新外定理、无下载/数值进程，不消费轮数，交由 root 与实际运输原稿一起核净值。
