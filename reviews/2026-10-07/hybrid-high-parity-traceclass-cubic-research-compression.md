# 原 high parity 的 trace-class cubic 预算

2026-10-07。独立新推导，只新增本文件。旧稿、源、Goal、Git 未改。

得到原 finite carrier 的 ||QJE||S1=O(log d)，并在原 [R] height band
上给静态背景 A0 的绝对 cubic upper。它只在更强的 θ<5/6 输入下
支付 Tr(A0 C_H³)=o(d)；原 θ=7/8 不在该范围。没有新比例或无零边界。
原实际 Gamma 背景 A=A0+R_T 还须单独恢复，不能据本稿自动丢 R_T。

## 1. 同对象与完整快照

原 X=T/(2π)、L=log X、d=floor(XL)、I=[−L/2,L/2]，
Ee_k=L^-1/2 1_I exp(iτ_k u)，τ_k=T+2πk/L，P=EE*、Q=1−P。
J=M_sgn u、S=E*JE、U=sgn S（zero eigenvalue 取 +1）。
H=E*B_HE 是 genuine primes sqrt X<p≤X 的原矩阵，实线零延拓。
D=A0=E*M_hE，h=φ²/a_L−1，||h||∞≤M_h=O(1)。

|源|canonical UTF-8 LF SHA-256|
|---|---|
|high Gram/parity research|3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2|
|notes/454 原背景|8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7|
|notes/461 原 band 13|f9fdf0b721c76a5cc4c4e4821748007e62975286417e6bec9700e39b6778170b|
|notes/463 原双侧 height|6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90|
|parity weighted high cubic research|2f883e521bd8f729084530aa8273acc397b528ce66392df1d7a803e53b43bbae|

这里仅新增 trace-class 费用。相对界 |Tr D H³|/d≪sqrt(a_T)/L
已由最后一份源的 noncommuting telescoping 得到；a_T=TrH⁴/d 未知。
本稿的 absolute bound 走另一条路线，不先假 a_T bounded。

## 2. 原 outside-carrier Hankel matrix 的 nuclear 范数

J 的 normalized interval Fourier coefficients 为
(1−(−1)^n)/(π i n)，n≠0，zero coefficient 为零。
QJE 的矩阵 rows 是 j<0 或 j≥d，columns 为 0≤k<d。
两侧重新排序后，其绝对分母均为 r+k+1，r≥0、0≤k<d。
每侧是 rectangular Hilbert matrix 的 odd filter，乘以固定常数与
row/column unitary phases。

令 H_d(r,k)=1/(r+k+1)。准确 rank-one integral 为

\[
 H_d=\int_0^1 (t^r)_{r\ge0}(t^k)_{0\le k<d}^*\,dt.
 \tag{1}
\]

积分在 S1 中收敛，因为 nuclear integrand 等于

\[
 \frac{\sqrt{1-t^{2d}}}{1-t^2}
 \le\min\left(\frac{\sqrt d}{\sqrt{1-t^2}},\frac1{1-t^2}\right).
 \tag{2}
\]

t≤1−1/d 时第二界的积分 O(log(2d))；剩余 interval 的第一界积分 O(1)。
odd filter 是 (H_d−V_r H_d V_k)/2，其中 V_r,V_k 是 diagonal signs，
故 nuclear norm 不增加阶数。两侧相加得到

\[
 \boxed{\|QJE\|_{S_1}=O(\log(2d)).}
 \tag{3}
\]

这严格使用原 finite interval basis；没有假设 P 是与 J 可交换的
global frequency band。前置 HS²=Tr(I−S²)=O(log d) 仍成立。
对 S 的每个 eigenvalue s，1−|s|≤1−s²，故还有

\[
 \|U-S\|_{S_1}\le\operatorname{Tr}(I-S^2)=O(\log d).
 \tag{4}
\]

## 3. 静态背景的 nuclear 交换误差

M_h 与 J commute，准确有限式为

\[
 [S,D]=-(QJE)^*QM_hE+(QM_hE)^*QJE.
 \tag{5}
\]

使用 ||QM_hE||op≤M_h、(3)–(4)，得到

\[
 \|D-UDU\|_{S_1}=\|[D,U]\|_{S_1}
 \ll M_h\log(2d).
 \tag{6}
\]

不需要 h 偶，也不需要已有 h 的 HS leakage 来充当一个新高矩输入。

## 4. good-height 核范数：不假 good B 与 J anticommute

采用原 J_t=[T/2,3T]（下标 t 与空间 J 区分），
F=unitary Fourier·Mφ E，B_g=Mφ Fourier* m_g Fourier Mφ，
m_g=1_Jt m_H。令 q=||m_g||∞、m=||m_H||∞≪sqrt X/L。
于是 ||B_g||op≤q，B_H=B_g+B_bad。
原 C² packet tail 给

\[
 \|1_{J_t^c}F\|_{HS}\ll T^{-1},\qquad
 \|B_{bad}E\|_{HS}\ll m/T.
 \tag{7}
\]

有限 bad compression 还满足
||H−E*B_gE||S1≤m||1_Jtc F||HS²≪m/T²，故
||H||op≤q+O(m/T²)=:q_+。

原 raw high anticommutation 给

\[
 SH+HS=-(QJE)^*QB_HE-(QB_HE)^*QJE.
 \tag{8}
\]

将 QB_HE 分成 good 与 bad，good 只用 op≤q，bad 用 (7) 的
right packet HS，而左 QJE 用原 HS=O(sqrt(log d))。因此

\[
 \|SH+HS\|_{S_1}
 \ll q\log d+\sqrt{\log d}\,m/T.
 \tag{9}
\]

再用 (4) 与 finite ||H||op≤q_+，得到

\[
 \boxed{\|H+UHU\|_{S_1}
 \ll q_+\log d+\sqrt{\log d}\,m/T.}
 \tag{10}
\]

没有将 Jφ 当作 C² packet，也没有断言 B_g 保持空间 half-block。
good B 本身不与 J anticommute；(8) 始终是 raw 的准确恒等式。
这避开 height cut 改变空间支持的隐藏问题。

## 5. 绝对 weighted cubic 与 θ 门槛

取 H'=−UHU、D'=UDU。有限 cyclic trace 给
Tr D'H'³=−Tr D H³，且
H³−H'³=(H−H')H²+H'(H−H')H+H'²(H−H')。
每项都保持非交换顺序。S1–op trace Hölder 得

\[
 \begin{aligned}
 2|\operatorname{Tr}D H^3|
 &\le\|D-D'\|_{S_1}q_+^3
       +3M_hq_+^2\|H-H'\|_{S_1},\\
 \frac{|\operatorname{Tr}D H^3|}{d}
 &\ll M_h\left\{
       \frac{q_+^3\log d}{d}
       +\frac{q_+^2m\sqrt{\log d}}{Td}\right\}.
 \end{aligned}
 \tag{11}
\]

原 fixed-gap [R] 的 sharp Perron bound 与 pp/low 的绝对 subtraction
给 band q≪X^(a−1/2)polylog(X)，对 fixed a>max(θ,3/4)。
第二项在 a<1 下趋零；第一项是

\[
 O\bigl(X^{3a-5/2}\operatorname{polylog}X\bigr).
 \tag{12}
\]

如果另有 θ<5/6，可以选择 max(θ,3/4)<a<5/6，严格得
Tr(A0 H³)/d→0，无 full high4 bounded 前件。原 θ=7/8（及目前
接近该值的既有线）不允许此选择；(12) 仍有正幂。
这只是更强输入下的 conditional interface，不能宣布获得 θ<5/6。

原 A 的 R_T 恢复没有在 (11) 内付款。仅凭 ||R_T||op=O(1/L)、
已付 TrH²=O(d) 与 finite op≤q_+，最多给
|Tr R_T H³|/d≪q_+/L，仍可能增长。源的 relative fourth bound
保持有效，但不是无 full4 前件的 absolute 小量。

## 6. 准确的数据障碍与后续范围

S1/HS parity、paid second 和 q 的 op bound 本身允许一个低质量
spike：在一条 U=+1、D=d0≠0 的方向取 H=q、low=0，剩余空间放
bounded ±paired high spectrum。spike 的 second 占比 q²/d=o(1)，
S1 parity defect=2q，HS² parity defect=4q²/d=o(L^-2)，
low4 与 entire13 不变；weighted cubic 却为 d0q³/d。
当 a>5/6 时，该项可以增长。

这是现有 trace/defect/op 信息的模型，不是实际高素数 translations
的实现，也不排除更多物理支持或算术联合信息能支付该项。
若继续当前7/8路线，需要控制 finite parity-defect 方向上的 cubic
energy，或提供比 (12) 更强的 actual signed/weighted arithmetic。
空间 even 背景与二范数 parity 不足以替代该付款。
