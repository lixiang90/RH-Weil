# 470：中心化谱方差提高原残差下界并排除旧 Q 候选

2026-10-08。作者 root。完整新推导，待其他作者独立全文审查。
本稿继续原 Eisenstein / AF 路线，只取原 flat profile，保留固定 endpoint
taper、全部 genuine high primes、实际 finite carrier 与内部 P。
不需要新的 [R] 无零输入或 high fourth 增长前件。

本轮更强的整个实际必要下界为

\[
 \boxed{\liminf_{T\to\infty}q_T\ge
 q_*=\frac{\sqrt{104899}-275}{15120}
       =0.003232880359890941970204919231\ldots
       >\frac1{350}.}                                  \tag{1}
\]

结合本轮已经付款的正尾成本，还可无增长前件地加强为
\(\liminf(q_T^{e}-q_T^{o})\ge q_*\)；完整量词见第5节。

因此 467–469 使用的 flat 原矩阵候选 limsup q_T≤1/350
已被严格排除。其条件预算公式仍为正确蕴含，但前件不可能成立，
不能作为后续实际比例改进目标。本稿没有得到新比例或无零边界。

## 1. 全部原对象与已经付款的中心化

H=E*B_HE，W=E*M_wE，Γ=H²−W，τ=Tr/d，q=τΓ²。
其定义与 [465](465-centered-high-square-joint-fourth-budget.md)、
[466](466-high-square-variance-commutator-obstruction.md) 完全相同。
以下 finite 输入及极限均来自这些已经付款的 weighted second，
无需先有 high fourth 上限：

\[
 \begin{gathered}
 0\le W\le M_TI,\quad M_T\to3/8,\quad
 K_T=\|[H,W]\|_{2,d}^2\to41/10080,\\
 m_T=\tau W\to1/6,\quad
 \tau W^2\to19/480,\quad v_T=\tau W^2-m_T^2\to17/1440,\\
 \mu_T=\tau\Gamma=o(1),\qquad
 \varepsilon_T=\tau(\Gamma W)=o(1).
 \end{gathered}                                         \tag{2}
\]

最后两项分别为原 H² second 与 high diagonal 的差、
原 WH² weighted second 与 W² 的差。mean W 由原 flat
w(t)=t(t+1)/2、t∈[0,1/2] 给 2∫w=1/6。
本次新增的关键是把这两项中心化用于 finite H 谱基的方差，
不是重新索取任何未付算术输入。

| 冻结原输入 | canonical UTF-8 LF SHA-256 |
| --- | --- |
| [454 完整 weighted second](454-original-background-and-weighted-prime-mixed-traces.md) | 8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7 |
| [465 high residual 与 centered weighted second](465-centered-high-square-joint-fourth-budget.md) | a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464 |
| [466 谱基 finite 行不等式与 actual commutator](466-high-square-variance-commutator-obstruction.md) | 0b955bdc26b4bf950ce457dec7bf18f635f702d85a73d73c8d6263df969cbbbe |

canonical 只转换 CRLF、lone CR，不 trim 或修改 EOF。

## 2. 精确 finite 谱基 covariance

在任一 H 的正交特征基中，H_ii=λ_i、w_i=W_ii、
δ_i=λ_i²−w_i、ρ_i=Σ_(j≠i)|W_ij|²，定义

\[
 x_T=\frac1d\sum_i\delta_i^2,\qquad
 y_T=\frac1d\sum_i\rho_i,\qquad q_T=x_T+y_T.             \tag{3}
\]

x、y 是 Γ 在 H 谱基的 diagonal/off-diagonal 方差，
与 469 的 U-even/U-odd 方差不同。
不要求简单谱；任何正交特征基均满足下列必要式。
由 Γ_ij=−W_ij (i≠j)，准确有

\[
 \varepsilon_T=\frac1d\sum_i\delta_i w_i-y_T,\quad
 \mu_T=\frac1d\sum_i\delta_i,\quad m_T=\frac1d\sum_i w_i .
\]

保留 W 的全部 off-diagonal 方差，而非只用较粗的 total variance：

\[
 \frac1d\sum_i(w_i-m_T)^2=v_T-y_T\ge0 .
\]

因此 scalar centered Cauchy 给严格 finite 不等式

\[
 \boxed{(y_T+\varepsilon_T-\mu_Tm_T)^2
             \le(x_T-\mu_T^2)(v_T-y_T).}               \tag{4}
\]

两因子均非负。这是 finite covariance，不是将 o(1)与未知增长量
相乘后删除；(4)保留全部误差。

## 3. 原行 SOS 与 whole liminf 的联合量词

466 的通用 finite 引理其实保留了不同成本：

\[
 K_T\le M_Tx_T+4M_Ty_T.                                \tag{5}
\]

简核：W²≤MW 给 ρ_i≤w_i(M−w_i)，而
δ_iρ_i≤Mδ_i²/4+ρ_i²/M、
w_iρ_i+ρ_i²/M≤Mρ_i。
把这些代入 K≤4d^−1Σ_i λ_i²ρ_i 即得 (5)。
此处 (5)的 1 与 4 系数都保留，未放宽成 K≤4Mq。

若 liminf q_T=∞，(1)显然成立。否则沿达到 finite liminf 的
有界子列，再取 (x_T,y_T) 的共同收敛子列，记 (x,y)、q=x+y。
只有此处利用 x_T≤q_T 有界，才把 (2)的中心化误差从 (4)删除。
无需要预先证明整个 q_T 有界。
记 v=17/1440、A=(41/10080)/(3/8)=41/3780，则

\[
 y^2\le x(v-y),\qquad A\le x+4y,\qquad x,y\ge0.         \tag{6}
\]

因 q=x+y，第一式准确消元为

\[
 y(q+v)\le qv,\qquad
 A\le q+3y\le q+\frac{3qv}{q+v}.                       \tag{7}
\]

q+v>0，故

\[
 P(q):=q^2+(4v-A)q-Av\ge0.                            \tag{8}
\]

Av>0，P 的两根异号，q≥0 必须不小于其正根：

\[
 q\ge\frac{A-4v+\sqrt{A^2-4Av+16v^2}}2
       =\frac{\sqrt{104899}-275}{15120}.
\]

达到 liminf 的子列任意，证明 (1)。
整个推导不需要交换 H、W，不改变原 prime range 或 row profile，
也没有使用 unknown whole fourth tail 的统一可积性。

## 4. 旧 Q 的严格有理排除证书

取旧 Q=1/350，则

\[
 \boxed{P(Q)=-\frac{15199}{952560000}<0,}               \tag{9}
\]
\[
 A-\left[Q+\frac{3Qv}{Q+v}\right]
       =\frac{15199}{13967100}>0.                      \tag{10}
\]

两式均由纯有理数计算；无需数值 root search。
所以该 Q 前件在整个 flat 原对象上不可能成立，
无论是否附加原 k≥1/40 条件，都无法修复这个矛盾。

本轮早先
[469 的联合预算](469-original-whole-parity-gap-and-joint-fourth-budget.md)
及其完整 parity 源依然是有效 finite reductions；
尤其无增长前件的 q_even−q_odd≥41/15120、whole-low 常数和
marked13 分量正交的准确域保持。
其中 Q-only F<1/3 与 Q+k 的数值例子从此只属被原结构排除的前件下
的反事实蕴含，不能当作可能付成的实际比例目标。
旧记录、已审源与输出保留，以本稿和新 checkpoint 明示更新。

一般有限常数 4M 的 sharp 示例不反驳本结果：
466 的示例 x=0、y>0，但 ε=τΓW=−y≠0，
不满足本稿同时使用的 centered weighted second。
新下界利用实际对象的额外付款，不声称通用 4M 系数变小。

## 5. 正尾 coercivity 把同一下界传到 entire parity gap

这里额外使用本轮
[完整正尾源](../reviews/2026-10-08/hybrid-positive-tail-whole-high-parity-gap-research-compression.md)，
canonical SHA 568f2c80d9773db7c13bc3605e7d56ed032e3fba7f5d4dc7c34bbea5ac7cb611。
记 r_T=||Γ_o||2,d²、g_T=q_T−2r_T=q_T^e−q_T^o。
其严格 finite (9) 对任意 R²>M_T 给

\[
 g_T\ge q_{R,T}+2(R^2-M_T)t_{R,T}-\zeta_{R,T},\quad
 t_{R,T}=\tau(H^2-H_R^2),\quad
 \zeta_{R,T}=2e_{R,T}^2+R^2\alpha_T^2 .
\]

选择 R_T²=ell，该源已逐项付出 ζ_R,T=o(1)；
不是把 fixed-R 的 o_R(1) 免费用于移动 R。
因 q_R,t_R≥0，liminf g_T≥0。
若 liminf g_T=∞，结论显然；否则沿达到其 finite liminf 的有界子列，
上式自动给 q_R,T=O(1)、t_R,T=O(1/ell)。
这使用正尾的 coercivity，而非先假设 q_T或 τH⁴ bounded。

clip 的距离 ||H−H_R||2,d²≤t_R，使 K_R,T→K_*。
对 core Γ_R=H_R²−W，准确中心化差为
τΓ_R=μ_T−t_R→0、
τΓ_RW=ε_T−τ(D_RW)→0；后一项以 0≤W≤M_TI、D_R≥0
付成 |τ(D_RW)|≤M_T t_R。
W 的 mean、variance保持 (2)。
因此第2–3节的严格 finite covariance 与行 SOS 可对每个 H_R,W
应用，并在上述 bounded core 子列取极限，得到 liminf q_R,T≥q_*。
最后 g_T≥q_R,T−ζ_R,T 给

\[
 \boxed{\liminf(q_T^e-q_T^o)\ge q_* .}                  \tag{11}
\]

所有常数仍取原 flat profile；没有 high fourth 增长前件或新增 [R]。
这增强 469 的整个 parity gap，且 (1)也可从 q_T≥g_T及 (11)恢复。
第3节不依赖 U 的证明仍独立成立。

下一步仍研究原完整 signed high-square covariance 及其与 low 的联合
消去。任何新预算必须先与 (1)及已有 parity gap 相容。
当前项目实际优化比例、相对于既定 [R] 的无零边界均未提高；
没有确认新边界，因此不新增边界论文。
