# 完整 log derivative、双变量 twist 与实际 577 残差

2026-10-22；独占核查分支。主对象、原域与停止责任继承577／578，不新建合同、不计研究轮。结论属于标准恒等式和旧预算的直接运输：完整 Γ 确实能同源进入反射／Riccati／polarization，但尚无独立有符号小量支付实际 q_R。

## 1. 固定完整对象，不由轴上点值替换 Weil 分布

取 U(s)=−ζ′(s)/ζ(s)。经典规范完成化为

\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad A(s)=\xi'(s)/\xi(s)=V(s)-U(s),
\]
\[
 V(s)=\frac1s+\frac1{s-1}-\frac12\log\pi
                       +\frac12\psi(s/2).                 \tag{1}
\]

两个 pole、完整 digamma 而非其渐近项、Γ 的有限部分与既定 contact 都在(1)内。第一变量线性，物理源仍 r=e^(u/2)f，Fourier 为 ∫r(u)e^(−itu)du，B_W(r,s)=W(r*s*)；全部 proper powers 的权为 Λ(p^k)=log p。405 是 S_exp 中实际非 compact 的全主关系及其固定平移；原 du／zero-extension Dlog 不换域。

精确函数方程和实结构给

\[
 A(1-s)=-A(s),\qquad A(\bar s)=\overline{A(s)},
 \quad U(s)+U(1-s)=J(s):=V(s)+V(1-s).                       \tag{2}
\]

令 s=1/2+it。在非零点、非 pole 的 regular 点，1−s=bar s，且

\[
 2\Re V(1/2+it)=\Re\psi(1/4+it/2)-\log\pi=\Gamma(t).
                                                                    \tag{3}
\]

这里 1/s+1/(s−1) 的实部精确抵消，未将两个 pole 从完成化删去。(2)遂给 2Re U=Γ、Re A=0，但这只是 regular-axis 的亚纯点值恒等式，**不是** W_ζ=W_Γ+H−P 的分布恒等式，更不表示 W_ζ=H 或 W_ζ=0。

若轴上有 m 重零点 ρ=1/2+iγ，则 A(ρ+ε+iτ) 的主项为 m/(ε+iτ)。其 Re 在 ε↓0 时产生 mπδ_γ，而 |A|² 的主项 m²/(ε²+τ²) 的质量以 1/ε 发散。直接在轴上平方约为 m²/τ²，不能局部积分成为有限正测度。正则化若减去发散 δ，须另核有限部分、contact 和源费用，不能保留“平方故正”这句话。对一般源，原 Fourier 配对的发散首项为 m²|hat r(γ)|²/(2ε)；fixed 源半窗 L 只能付 |hat r(γ)|²≤2L||r||²，不能由此得到趋零费。405 在真正零点的消去也不能替代全部源的这笔费用。

若反射对有离轴零点，regular-axis 上 Re A 仍可为0；将右侧轮廓移到中心须处理越过的 pole/residue。把这些项漏掉，才会错误地从函数方程推出正性。这个域问题在下述连续负例中可直接核见。

## 2. 双变量 twist：反射确实改变和频，但不免费改变 Euler 域

先把 s,w 当独立复变量。在任何各项有定义的亚纯域，(2)给

\[
 U(s)U(w)=J(w)U(s)-U(s)U(1-w).                              \tag{4}
\]

取 w=bar s，得到 Hermitian 平方

\[
 |U(s)|^2=J(\bar s)U(s)-U(s)U(1-\bar s).                    \tag{5}
\]

在中心 regular 点，1−bar s=s，J=Γ，故

\[
 |U(s)|^2=\Gamma(t)U(s)-U(s)^2.                             \tag{6}
\]

(6)的右侧虽写有完整 Γ，仍只是把 2Re U=Γ 乘以 U。其虚部和实部均是同一关系的重写，不能从 |U|²≥0 读出所需线性 prime／pole 预算的方向。

Re s>1 与 Re w>1 才有两个绝对收敛正系数 Euler 展开；反射后 1−w 的实部<0，两个安全域不重叠。在中心线，Euler 级数并不由绝对收敛定义；以亚纯继续的值代回无穷正 Gram，会漏掉上述域、pole 与正则化费用。双变量 holomorphic identity 与 w=bar s 的反线性限制也不是同一个解析继续操作。对扭曲高度或 t 平均，这个区别不消失。

安全域中 −U′+U²=ζ″/ζ 编码乘积／和频；|U|² 编码比值／差频。二者同源但不是同一测度。若 p_R=Σa_nδ_log n、a_n=Λ(n)n^(−1/2)φ(log n/R)≥0，则 U_R(1/2+it)=hat p_R(t)，U_R² 对应 p_R*p_R，而 |U_R|² 对应 p_R*p_R*。后者有全部 ratio 频率 log(n/m)，以及准确 contact Σa_n²；它们不能只凭(4)成为 H−P 的线性系数。fixed 源差支撑 |u|≤2L 仍容许任意高 n,m 的 n/m∈[e^(−2L),e^(2L)]，不把这类差频自动截断到低 prime 高度。

由旧 Chebyshev，Σa_n≪e^(R/2)、Σa_n²≪1+R²；TV 上界给这些卷积原 du 费用至多 O(e^R)，并非小量。全 L² 上 |U_R|² multiplier 的准确 norm 是 (Σa_n)²（t=0 取到），但这不是任意实际受限源上的必要费用下界。扣去其 contact 也未证明剩余平方正。原 Γ(t) 是 log 级 multiplier，单独乘以 U_R 可用 Dlog 付 O(Σa_n) 的相对形式费用；把 Γ 与 Euler 项分开三角估计不能得到原 du 小费。

## 3. 贴实际 577 的双 pole 扣除：残差正是待付的 g_R

固定577已经选定的 φ_R，不按未知零点或未知正性选择系数。定义有限原数据

\[
 U_R(s)=\sum_{n=p^k\le e^R}\Lambda(n)n^{-s}\phi(\log n/R),
\]
\[
 C_R(s)=\int_0^R\phi_R(u)
               [e^{(1-s)u}+e^{-su}]\,du,\qquad
 B_R(s)=U_R(s)-C_R(s).                                      \tag{7}
\]

C_R 正是两个 pole 的同窗 Laplace 数据，不删其中一个，不把它换成轴上已经继续的有理函数。在 s=1/2+it，

\[
 2\Re C_R(s)=H_R(t),\quad2\Re U_R(s)=P_R(t),\quad
 g_R(t)=\Gamma(t)+H_R(t)-P_R(t)
       =\Gamma(t)-2\Re B_R(s).                              \tag{8}
\]

因此，全部 t 上无需零点输入就有具体 finite identity

\[
 \boxed{|B_R|^2=\Gamma(t)B_R-B_R^2-g_R(t)B_R.}              \tag{9}
\]

也可直接做 finite FE defect：E_R(w)=U_R(w)+U_R(1−w)−J(w)，则(4)右侧要准确加 U_R(s)E_R(w)。中心线上 E_R=P_R−Γ，且 g_R=H_R−E_R。减完双 pole 后，(9)准确将这个残差收为 actual g_R B_R。

这是本候选最接近目标的同源身份，但不是独立估计。actual q_R=(−g_R)_+=(E_R−H_R)_+。若要求 E_R≤H_R+ε_R 且付 ε_R 的原费用，正好又要求实际 q_R 的预算；不能将最后一项 −g_R B_R 称为已被正平方吸收。它通常为复数；取实部也只重得 |B_R|²=(Γ−g_R)Re B_R−Re(B_R²)，即 2Re B_R=Γ−g_R。

作为有符号 Fourier 测度，B_R 的物理原料为 p_R−φ_R(u)2cosh(u/2)1_(0,R)du，TV 至多 O(e^(R/2))。所以分开支付 B_R² 和 |B_R|² 给 O(e^R) 原 du upper，ΓB_R 给 log-relative 费用；(9)没有给这些大项之间的 signed 小量。这个 upper 也不是 actual q_R 的 lower，不能由其大断言修补不能消失。

在任一先固定 Re s≥1+δ，δ>0 的安全域，C_R→1/(s−1)+1/s、U_R→U；由 0≤1−φ_R≤κu²/(2R²) 和 Chebyshev，误差为 O_δ(R^(−2))，并对 Im s 一致。故

\[
 B_R(s)\longrightarrow U(s)-\frac1s-\frac1{s-1}
                                                          \tag{10}
\]

在那里确实合法。这是旧窗界的安全域运输；δ 常数不允许免费跨过 σ=1 到 σ=1/2。中心线的 finite C_R 也不收敛到其轴上有理继续值，不能用(10)删除 H_R。

## 4. 完整 Riccati 的 cutoff 误差不因 Γ 完成化而消失

令 L_R=U−U_R（先在安全域）。准确有

\[
 -U'_R+U_R^2=\frac{\zeta''}{\zeta}
                   +L_R'-2UL_R+L_R^2.                      \tag{11}
\]

完整 log derivative 则满足

\[
 A'+A^2=\frac{\xi''}{\xi}
      =\frac{\zeta''}{\zeta}-2VU+V'+V^2.                   \tag{12}
\]

Γ、cross term −2VU、两个 pole 的 V′+V² 必须同时保留。没有哪个单项因“Riccati”名称成为非负。若 A_R=V−U_R=A+L_R，则

\[
 A_R'+A_R^2=\frac{\xi''}{\xi}+L_R'+2AL_R+L_R^2.            \tag{13}
\]

安全域中可独立付 L_R 和导数的 O_δ(R^(−2))；中心线及成长高度需要的是另外的联合误差，(11)–(13)不提供它。以 Re A>0／完成 Pick kernel 正性给它方向，则回到旧131已经辨明的 RH 等价责任；本分支不重开该核。

## 5. 连续正反例与函数域：同一 identity 不决定正号

使用578已完整核查的同族真 positive primitive／g-integers：

\[
 Z_c(s)=\frac{(s-\alpha)(s-\beta)}{s(s-1)},\quad
 \alpha+\beta=1,\quad\alpha\beta=c,
\]
\[
 U_c=\frac1s+\frac1{s-1}-\frac1{s-\alpha}-\frac1{s-\beta},
 \quad V_c=\frac1s+\frac1{s-1},\quad
 A_c=\frac1{s-\alpha}+\frac1{s-\beta}.                      \tag{14}
\]

native Γ=0，(2)、(4)、(11)、(12)逐项精确成立。正例 c=5/16 有 α,β=1/2±i/4，完整 W_+=2cos(u/4)du；负例 c=3/16 有 α=3/4、β=1/4，完整 W_−=2cosh(u/4)du。两例在全部 regular-axis 点均有 2Re U_c=0、|U_c|²=−U_c²。

负例令 a=1/4、z=s−1/2，则 A_c=2z/(z²−a²)，轴上 A_c=−2it/(t²+a²) 完全虚；这不妨碍完整 W_− 非正型。其实际 compact 双 pole-moment-zero 源 r_- 及 Q_−(r_-)<0 继承578(13)，继续迫使 liminf Q_K(r_-)≥−Q_−(r_-)>0。因此，本次完成化 FE／Riccati／twisted-square 身份连同安全域正 Gram 不能排除这个实际负源；并非仅仅没找到抽象反例。

这不是保经典 Γ 的反例：两模型只能用各自 native Γ=0。有限式(7)–(9)可对各自全 prime-power 测度直接替换和式为积分；正例 hard q_R=0，负例补偿不消。这里新增的是对本具体身份的直接核对，不将旧562／578模型或同一费用反测重计为新数学轮。

真函数域 C/F_q 则取 ℓ=log q、T=q^(−s)，Z_C=P(T)/[(1−T)(1−qT)]，规范自对偶 completed 对象可取 ξ_C(s)=q^(gs)P(q^(−s))。于是

\[
 V_C(s)=g\ell+\frac{\ell q^{-s}}{1-q^{-s}}
                 +\frac{\ell q^{1-s}}{1-q^{1-s}},
 \quad A_C=V_C-U_C,\quad
 U_C=\ell\sum_{n\ge1}N_nq^{-ns}\quad(\Re s>1).             \tag{15}
\]

(2)、(4)、(12)照样成立；V_C 的 pole 必须保全部周期 aliases，不能只留一对。native 完整 Γ/contact 与经典不同；轴上 2Re V_C=2(g−1)ℓ，这个 regular-axis 值本身不等于全 Weil 分布的 a_0=2g contact，更说明不能漏 pole 的分布边界。true function-field 正号已由同对象 RR/Hodge index／极化 U*HU=H 与完整 trace 身份独立付清，给578(14)全部 returns／aliases 的平方和，hard q_R=0。它不是由(15)的点值平方推出，也不能靠外加经典 Γ 获得。

## 6. 405、537、原范数与三种极限责任

(7)–(13)没有改变 actual G_R、V_R 或 W_ζ，故405全主关系仍由完整 B_ζ(p,s)=0 在 S_exp 消费。577各正层的高频严格正连续谱仍使任意非零实际 p 的 Q_V_R(p)>0；不能从有限 Hermitian Gram 宣称 exact 商已下降。单独的 |U_R|² 连续谱亦在非零 finite polynomial 情形几乎处处正，故并不自动消去任何非零 L² 主关系。量值下界未由此自动付给特定源。

537半窗 L_0=17/16 的全部 complex 原源仍由旧结论无条件最终保留非根：Q_V_R≥(τ−D_L0/R²)||r||²；这不是新成长窗结论。相反，新增 Γ×twist 或导数项若分开估计，须付上述 du／Dlog／强源费用，不能只在某个有限频高正 Gram 上免费代入。

577原 fixed-L 比较保持

\[
 |Q_{V_R}(r)-Q_\zeta(r)|
 \le [D_L/R^2+\min(c_R,2Lm_R)]\|r\|_2^2,
 \qquad D_L\ll(1+L^2)e^L.                                 \tag{16}
\]

G_R→W_ζ 于 D′ 无条件；V_R 是否趋同一目标仍须 actual K_R→0。对这个特定 family，q_R 的 sup／L¹ 消失及 K_R 的 D′ 消失仍等价完整 Weil 正性／RH。D′ 本身不推出原范数统一小费；L=L(R) 成长仍要同时付 D_L/R² 与实际 q_R。全线 Hlog 的 Pan 稠密障碍及每层 full-target difference norm∞，按553／577保持。

## 7. 可消费结论与停止

真正核清的是本候选的完整对象与 residual：完整Γ确可进入同源的双变量反射和 Riccati；减完两 pole 的有限 polarization 残差精确为 g_R B_R。完成化修正并未提供独立符号或趋零误差，轴上 pointwise 平方还另有临界 pole／有限部分费用。safe-domain O_δ(R^(−2)) 只是旧窗界运输，不能跨域支付实际 q_R。

这组 identity 不构成新的经典 signed 输入，也没有强于旧131、577、578的 net consequence。建议按一次 source admission 0 止；不自动 C042／579，不调 twist／窗口／Riccati 阶数。重准入须独立算术比较实际残差（包括完整 Γ、proper powers、pole、原 norm 及成长量词），或同对象 primitive RR 容量，而非将 q_R 消失／Pick正性重新命名。最强旧542+555→557 whole4/5为上预算；actual core、coupling、Ξ与宏观独立正性瓶颈未变。
