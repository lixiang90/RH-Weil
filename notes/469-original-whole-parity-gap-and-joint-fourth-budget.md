# 469：原路线的完整奇偶约束与联合第四矩

2026-10-08。承接 468，回到原 Eisenstein / AF 对象。
本轮实际进展是一个不需高第四矩增长前件的整个残差约束，
完整低素数奇偶四矩，以及相对于既定 [R] 的分别正交约束。
这些结果收紧原 31、22 联合预算；高素数残差上界仍未得到，
因此没有确认新的实际零点比例或无零边界。

## 1. 保持同一原对象

沿用 X=T/(2π)、ell=log X、d=floor(X ell)、原 finite carrier E、
原 endpoint taper、sharp genuine-prime 系数与全部实际高度。
H、L 分别为整个 high primes sqrt X<p≤X 与 low primes p≤sqrt X
的 Hermitian finite 矩阵。W、V 是其实际同素数对角。
J=M_sign(u)、U=sgn(E*JE)，零特征值选 +1；
U 是实际 finite involution，不能用物理 J 免费替换。
记 τ=Tr/d，

\[
 \Gamma=H^2-W,\quad\Delta=L^2-V,\quad Z=(HL+LH)/2,\quad
 A_e=(A+UAU)/2,\quad A_o=(A-UAU)/2 .
\]

高平方残差方差 q=τΓ²=q_e+q_o；下文 r=q_o。
它不是 H 特征基中的 diagonal/off-diagonal 分解。
本稿所有显示常数取原 flat profile，固定 endpoint taper 保留。

## 2. 新的 entire-high 必要约束，无第四矩上限前件

[完整正尾证明](../reviews/2026-10-08/hybrid-positive-tail-whole-high-parity-gap-research-compression.md)
保留 clip 的正成本，证明

\[
 \boxed{\liminf_{T\to\infty}(q_e-q_o)\ge41/15120.}        \tag{1}
\]

这增强 468 在 q 有界下的 q_e≥41/15120，并取消该增长前件。
q 本身可以未知增长；(1)仍对整个实际对象成立。
关键是 finite scalar 平方恒等式，而不是把 H 的 S2 奇偶性免费升级为 S4。

具体地，取 R²>M、0≤W≤MI，H_R=clip_R(H)、
Γ_R=H_R²−W、D_R=H²−H_R²≥0。
原输入为 M_T→3/8、
K_T=||[H,W]||2,d²→41/10080，
alpha_T=||H+UHU||2,d=O(1/ell)，omega_T=||W_o||2,d=o(1)。
原 sharp finite commutator 界以及正尾给

\[
 q_e-q_o\ge
 \frac{K_T}{4M_T}\frac{2(R^2-M_T)}{2R^2-M_T}
 -2(R\alpha_T+\omega_T)^2-R^2\alpha_T^2.                \tag{2}
\]

所有 R 依赖显式。取 R²=ell 直接得 (1)；也可先 fixed R、
再 T、最后 R，无未知尾的统一可积性前件。
整个 q 的上界没有由此推出。

每个共同有界极限 (q,r) 必须满足

\[
 0\le r\le(q-41/15120)/2.                               \tag{3}
\]

所以原方差成本不能主要藏在奇残差中。

## 3. 完整低素数的所有奇偶四词

[完整 low 证明与路径积分](../reviews/2026-10-08/hybrid-whole-low-parity-fourth-research-root.md)
对 L_e=(L+ULU)/2、L_o=(L−ULU)/2 得

| 完整实际 finite word | flat 极限 |
| --- | --- |
| τL_e²、τL_o² | 各 1/12 |
| τL_e⁴、τL_o⁴ | 各 1/60 |
| τL_e²L_o² 的四种循环排列 | 3/320 |
| τL_eL_oL_eL_o 的两种循环排列 | 1/240 |
| 含奇数个 L_o 的四词 | 有限 T 时准确为零 |

所有 low primes、three pairings、four orientations、两个 row halves
均保留；全部非零频率项、alias、重复交集和内部 P 也已付款。
固定 smooth J 后先 T、再 sharp 恢复，后一步在 normalized S4 中进行。
因此不是只用配对积分充当整个四矩。

原 low profile 在 t=|u|/ell∈[0,1/2] 分成
v_e=1/8−t/2+t²、v_o=1/8−t²/2，
high profile w=t(t+1)/2。
实际带权第二矩给

\[
 \tau WL_o^2\to19/1920,\quad
 \tau(L_o^2-V_o)^2\to1/120,\quad
 \tau\Gamma V_o\to0 .
\]

完整结果还恢复原 δ_e=||Δ_e||2,d²→11/480、
δ_o→13/480，与另一作者先前的 low-square parity 计算一致。
[有理路径脚本](../scripts/hybrid_whole_low_parity_exact.py)
独立计算 square 上所有 affine half-line cells；
它认证积分与常数，分析准入由完整源和独立审查承担。

## 4. 分别支付两个 Gram 正交

[marked13 与联合预算证明](../reviews/2026-10-08/hybrid-parity-split-schur-and-even-anticommutator-research-radial.md)
扩展整个 one-high/three-low 证明到 fixed C² row marks；
原 near、far、alias、canonical prefixes、坏高度与有限 P 全部保留。
这一部分仍相对于既定 conductor-one [R] 的 fixed gap theta<9/10；
原 7/8 输入足以满足其准确域。

sharp U 恢复明确要求 q_T=O(1)，仅在这里用已付
τH⁴=19/480+q_T+o(1) 取得 high S4 有界。
得到新实际结论

\[
 \langle\Delta_e,Z_e\rangle=o(1),\qquad
 \langle\Delta_o,Z_o\rangle=o(1).                       \tag{4}
\]

(4)另行付款，不能仅由原总正交 Δ⊥Z 拆写。
有限 Gram 保留 centering errors；共同有界极限中，令
p_j=〈Γ_j,Δ_j〉、z_j=||Z_j||2,d²，则

\[
 |b|\le\sqrt{(q-r-p_e^2/\delta_e)z_e}
          +\sqrt{(r-p_o^2/\delta_o)z_o},                \tag{5}
\]

其中 b=lim τH³L、
p_e+p_o=c−23/960、z_e+z_o=c−k/4，
c=lim τH²L²、k=lim||[H,L]||2,d²。
各因子非负，不能自由把总 covariance 分给小奇方差。

low 的新完整输入还约束真实 even anticommutator：

\[
 \sqrt{z_e}\le
 \sqrt{19/1920+\sqrt{(q-r)/120}}
       +[(q-r-41/15120)/60]^{1/4}.                     \tag{6}
\]

最后一个根号保留 high 的 even fourth tail 成本。
它来自 clip、正 tail 及 parity Jensen，不假设 tail 为零。
完整证明中先 fixed R、T、最后 R，并保留每项 finite error。

## 5. 前向预算更紧，原算术缺口仍在

只作同一既存前件的准确蕴含：若未来另行支付
limsup q_T≤Q=1/350，则 (3)给 r≤11/151200，
原 mixed covariance 必须满足

\[
 \limsup|c_T-23/960|<47/5000,
\]

比 468 的 1/100 外包更紧。两次平方有纯有理正余量。

结合 (4)–(6)，同一 Q 前件下对 entire fourth
F_T=τ(H+L)⁴ 有全连续 Young 证书

\[
 \limsup F_T\le
 U-\frac{63}{62}\liminf k_T,\qquad
 U=\frac{25710335933}{77218272000}<1/3.                 \tag{7}
\]

该证书覆盖完整必要域，不用有限网格代替优化。
它无需额外的 k≥1/40 前件就能条件地超过 flat 二矩的 2/3；
此数并不足以自动超过项目当前 0.672509329… 的优化比例。
若复用原未付 joint 前件 k≥1/40，则 RHS<77/250。
这些是更强的条件蕴含，不是当前实际四矩或比例。

真正缺口仍是整个高素数平方残差的可证明上界；
7/8 的 canonical 单 prefix 幂界尚未支付这一 signed joint quantity。
下一步继续在原 H²−W 的完整两侧乘积、near resonance 与有限 P
中寻找净 cancellation。当前实际比例及相对于 [R] 的
sigma_*=0.874957019420098946… 保持既定状态，
未确认新边界，因此本轮不新增边界论文。
