# parity weighted high cubic：独立 compression 审查

2026-10-07。全文只读独审，只新增本文件；旧数学、源、Goal、Git 未改。

结论：限定 PASS。noncommuting cubic telescoping、原实际背景的相对
恢复、high/low actual weighted 二矩，以及 Γ 的有限 Cauchy budget
均成立。没有提前假设 high4 bounded，也没有支付未知 q_T 的上限。
flat Q=1/1600 只是数值反事实，不能当成已经存在的实际付款条件。

## 1. 完整快照

源：reviews/2026-10-07/hybrid-parity-weighted-high-cubic-research.md。
canonical UTF-8 LF SHA-256：
`2f883e521bd8f729084530aa8273acc397b528ce66392df1d7a803e53b43bbae`，
8675 bytes / 227 lines。CRLF/lone CR 仅换为 LF，不 trim。
源列出的 high Gram/parity、454、461、462 绑定与本轮此前独审一致。
本审查只接受源中 conductor-one zeta [R] 的原范围，没有引入新行族。

## 2. finite parity 与背景交换误差

J=M_sgn u、S=E*JE 的原 finite defect 为 Tr(I−S²)=O(log d)。
U=sgn S、零 eigenvalue 取 +1 后 ||U−S||HS²≤Tr(I−S²)。
JB_H+B_HJ=0 是原 high translation geometry，P 与 J 没有被假定交换。
于是 ||H+UHU||HS≪m_H sqrt(log d)，m_H≪sqrt X/L。

背景 h=φ²/a_L−1 与 J 严格交换，无需 h 偶。准确有
[S,A0]=−(QJE)*QM_hE+(QM_hE)*QJE。
QJE 的 op≤1，故其 HS norm≤2ell_h，而非 ell_h sqrt(log d)。
加上 U−S 的误差得到 ||A0−UA0U||HS=O(sqrt(log d))，
且 UA0U 的 op 与 A0 相同、有界。源 (1) 正确。

## 3. noncommuting cubic 恒等式和相对界

H'=−UHU、r=H−H' 后 Tr(UA0U H'³)=−Tr A0H³。
所以源 (2) 是准确的有限 trace identity。
源 (3) rH²+H'rH+H'²r 的展开准确等于 H³−H'³，
没有将 r 与 H/H' 交换。

对于 middle term，可循环成 Tr(H A'H' r)。用
||H A'H'||HS≤||H||S4||A'H'||S4≤||A'||op sqrt(d a_T)，
其余两项用 ||H²||HS=sqrt(d a_T)；背景交换项用
||H³||HS≤m_H sqrt(d a_T)。所以所有项 ≤C m_H sqrt(log d)sqrt(d a_T)。
m_H sqrt(log d)/sqrt d≪1/L，给源 (4)：

\[
 d^{-1}|\operatorname{Tr}A0H^3|\ll\sqrt{a_T}/L.
 \tag{R1}
\]

这个 inequality 对每个 T 成立，完全不需要 a_T bounded。
它是相对预算；只有另付 bounded a_T 才给 o(1)。
不能把 parity 的 normalized HS 小量直接乘未知 cubic energy后删掉。

## 4. actual Gamma/pole 恢复

454 的原 A=A0+R_T、||R_T||op=O(1/L) 包含 low/negative height 与 pole。
归一化 Schatten power-mean inequality 给
Tr|H|³/d≤(TrH⁴/d)^(3/4)，因此源 (5) 成立。
恢复项不是已经 o(1)，除非 whole high4 bounded。

一个可选加强是利用已付 TrH²/d=O(1)：
Tr|H|³/d≤sqrt((TrH²/d)(TrH⁴/d))≪sqrt a_T。
所以实际背景同样可以得到 O(sqrt a_T/L)；这不改变其欠账性质，
也不要求修改当前较弱但正确的源 (5)。

## 5. actual weighted 二矩与 complex polarization

w=d_(H,L) 是非负同素数 diagonal。Σ_(p high)b_p²=O(1)，
每个 translated φ² product 的 derivative L1 bounds 一致，故
||w||∞、||w'||1、||w''||1 有界。原 Fourier coefficient bound
min(1,1/|n|,L/n²) 给 ell_w=O(sqrt(log(2L)))。

将 B_R E=E C_R+X_R 代入 Tr E*B_R M_w B_S E，准确产生源 (6)
的三个 crossing；single crossing 的 E*M_wQ、QM_wE 提供 ell_w。
它们与原 m_R、ell_R 相乘的费用正确。R=L,S=H 时为
O(X^(3/4)log(2L)/L²)=o(d)，R=S=L 时更小。无需第四矩。

两种 physical 顺序必须分别处理。Tr(W H C_L) 循环对应
Tr(C_L W H)，所以 physical B_L M_w B_H 是正确顺序。
不能直接交换 H 与 C_L；源已明确区分。

复极化的完整对象应读作
Tr E*(B_H+zB_L)* M_w (B_H+zB_L)E，而非不带 adjoint 的平方。
其 diagonal 因 high/low labels 不交而为 high+|z|²low。
z=1,i 各自提取两个 cross 的 real/imaginary parts，得到源 (7)。
454 的证明可按相同有限 log-integer union、bounded complex masks
及共同 translated window 逐项扩展；这不是新增 large-sieve 定理。
±L alias 仍由 endpoint overlap majorize，w bounded 不破坏这个付款。
共同 w 的一、二阶 bounds 保留 Hilbert/Fourier 费用，不需要 w 固定于 X。

low diagonal 变量代换后准确是 <w d_low,L>，不是把 w 放到独立位置。
因此 j_T→0、v_T→∫d_H d_low 都成立。flat 的两个 polynomial profiles
正确，2∫_0^.5[(v²+v)/2][1/4−v/2+v²/2]dv=23/960。

## 6. Γ 恒等式、有限 Cauchy 与条件量词

Γ=H²−W 是实际 Hermitian residual；q_T=||Γ||HS²/d≥0。
weighted high second 与 TrW² 的已付极限给 a_T=Sψ+q_T+o(1)，
此误差只含低阶付款，不偷用 high4 bounded。

c_T−v_T=Tr Γ C_L²/d，故 c_T≤v_T+sqrt(q_T e_T)。
b_T−j_T=Tr Γ H C_L/d，HS norm 的第二因子为 sqrt(d c_T)。
即使 j_T complex，该 Cauchy 模与 source (11) 也完全合法。
entire22≤6c_T 来自 |Tr HC_LHC_L|≤TrH²C_L²，
没有对不交换 squares 做 operator ordering。

q_T 的有限 upper bound 若另行证明，才有 a_T bounded、c_T bounded。
这时 e_T→eψ、v_T→c0、j_T→0、η_T→0 的 compact error 传递合法，
得到源 (12)。缺少 bounded q_T 时，√q_T 放大的 o(1) 不能免费删除；
源正确保留此限制。

flat Q=0 的 formal budget=21/80，Q=1/1600 的三个 rational comparisons
均正确，只说明 conditional numerical余量。本审查不把它们解释成
实际 q upper bound；结构性 q lower 若由后续 commutator报告证明，
只会使某个反事实前件不可达，不会推翻这里的有限不等式。

本稿新增相对 cubic 和 actual weighted second 接口可接受。
whole high signed arithmetic、q 的可用上界、完整比例转换仍未付款。
