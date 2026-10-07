# 原有限 parity 的加权 high 三次迹与 Γ 联合二矩

2026-10-07。twisted_research。新独立推导，待全文独审。
只新增本稿，不修改冻结 notes、论文、math、脚本、输出或 Git。
本稿给两个原有限矩阵上的接口：背景 high cubic 的相对小误差，
以及 high centered-square residual 对 31/22 联合项的实际约束。
没有证明未知 Γ 能量有界，没有新的比例或无零边界。

## 1. 原对象、冻结输入和确切依赖

保持 X=T/(2π)、L=log X、d=⌊XL⌋、I=[−L/2,L/2]，
Ee_k=L⁻¹/²1_I exp(iτ_k u)，τ_k=T+2πk/L，
P=EE*、Q=1−P。φ 是原 even C² taper，a_L=||φ||₂²/L。
每个 translation 在实线上零延拓，未换成周期支持模型。

记 B_H、B_L 为 genuine primes 的原 sharp physical high/low channel，
H=E*B_HE、C_L=E*B_LE。为避免与 log X 的 L 混淆，下文 low 矩阵写 C_L。
high 是 √X<p≤X，low 是 p≤√X。

| 输入 | canonical LF SHA-256 |
| --- | --- |
| [high Gram/parity](hybrid-high-parity-gram-and-mobius-completion-research-radial.md) | 3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2 |
| [454](../../notes/454-original-background-and-weighted-prime-mixed-traces.md) | 8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7 |
| [461](../../notes/461-original-one-high-three-low-fourth-trace.md) | f9fdf0b721c76a5cc4c4e4821748007e62975286417e6bec9700e39b6778170b |
| [462](../../notes/462-original-low-prime-fourth-path-constant.md) | 868adfeb0d742043f39bd08e0783d66b7a9db11316067b0b3b43d80150cdf680 |
| [high 四词](hybrid-high-prime-four-word-response-research.md) | 988f8669a771e5b913bbc546590ceac540fc1391838e948563e4b4578f8ff666 |

§2–4 只用原 raw op、finite leakage、bounded multiplication、
454 的实际背景，不依赖 [R]、low four-moment 或 full high fourth bounded。
§5 的加权二矩也不依赖 [R]。§6 的 whole-prime asymptotic 合并才使用
461/462 已明确的同一 [R] 合同；不另引一个推测性行族。

## 2. 有限 parity 与背景的交换误差

令 J=M_sgn(u)、S=E*JE、U=sgn S，零特征值处取 +1。
由前置 parity 稿：

J B_H+B_H J=0，
Tr(I−S²)=||QJE||HS²=O(log(2d))，

||U−S||HS²≤Tr(I−S²)，
||H+UHU||HS≪m_H√log(2d)，
m_H=||B_H||op≪√X/L。

U 是实际 d 维 Hermitian involution，没有假设 P 与 J 交换。
454 的背景为

A=A0+R_T，A0=E*M_hE，h=φ²/a_L−1，
||R_T||op=O(L⁻¹)，||A0||op=O(1)。

M_h 与 J 是 multiplication，所以严格交换；这里不需要 h 偶。
原圆周 Fourier 泄漏只用于计算原 finite P，给
ell_h=||QM_hE||HS≪√log(2L)。保留 internal P 得

[S,A0]=−(QJE)*QM_hE+(QM_hE)*QJE。

因此 ||[S,A0]||HS≪ell_h，
||[U,A0]||HS≪ell_h+||A0||op||U−S||HS≪√log(2d)。
记 A'=UA0U，则

||A0−A'||HS≪√log(2d)，||A'||op=O(1)。                 (1)

这一结果用 QJE 的 op≤1，不把其 HS 与 ell_h 相乘制造额外 log。

## 3. 精确有限 cubic identity

置 H'=−UHU，r=H−H'=H+UHU，
a_T=d⁻¹TrH⁴≥0，t_T=TrA0H³。
有限 unitary trace 严格给 TrA'H'³=−t_T。故

2t_T=Tr(A0−A')H³+TrA'(H³−H'³)。                    (2)

非交换 telescoping 是

H³−H'³=rH²+H'rH+H'²r。                              (3)

没有交换 r、H、H'。HS/Schatten Hölder 分别给

||H³||HS≤m_H||H²||HS=m_H√(d a_T)，
||H'||S4=||H||S4，
||H A'H'||HS≤||A'||op||H||S4||H'||S4
             =||A'||op√(d a_T)。

所以 (1)–(3) 的每一项均至多
C m_H√log(2d)√(d a_T)。因为 d∼XL、log d=O(L)，严格得到

|TrA0H³|/d ≪ √a_T/L。                                (4)

式 (4) 是无 full4 前件的相对 bound。它没有直接证明 o(1)：
只有 a_T bounded 时右边才趋零。把旧正幂上界代入仍可能增长。

## 4. 实际 Gamma/pole 背景的相对恢复

由 454 的 actual ||R_T||op=O(1/L)，有限归一化 Schatten 单调性给

|TrR_TH³|/d≤||R_T||op·Tr|H|³/d ≪ a_T^(3/4)/L。

因此对原实际背景

|TrAH³|/d ≪ (√a_T+a_T^(3/4))/L。                     (5)

低 height 和 pole 已在 454 的 R_T 内，不在这里重新删除。
若 whole high fourth 独立有界，(5) 支付 high-only background cubic。
它可服务非平 profile 的后续合并；不是在未知 high4 之前提前
将 A 替换为 A0 后把其误差称作 o(1)。

flat whole background在 whole-prime fourth bounded 后还可直接用
454 的 Z=V=J=0 和 Cauchy 支付，无需为 flat 强行重复分扇区。

## 5. Dhat 与原 high/low 的实际加权二矩

令 w=d_{H,L} 为原 high 同素数 diagonal multiplication，
W=E*M_wE=Dhat。这里的 w 随 X 变化，但
||w||∞=O(1)、其一二阶 derivative L1 统一有界，
ell_w=||QM_wE||HS≪√log(2L)。令 Z=√X、ell0=log(2L)。

原 prime op 与泄漏为

m_H≪√X/L，m_L=||B_L||op≪√Z/L，
ell_H=||QB_HE||HS≪m_H√ell0，
ell_L=||QB_LE||HS≪m_L√ell0。

比较物理两列时始终使用
B_R E=EC_R+X_R，X_R=QB_RE。展开给

TrE*B_R M_w B_S E−Tr(C_R W C_S)
 =Tr(C_R E*M_w X_S)
  +Tr(X_R*M_w E C_S)+Tr(X_R*M_w X_S)。

两个单 crossing 中 E*M_wQ、QM_wE 提供 ell_w，故绝对差≤

m_R ell_w ell_S+m_S ell_w ell_R+||w||∞ell_R ell_S。  (6)

R=L、S=H 的误差 O(X^(3/4)ell0/L²)=o(d)，
R=S=L 的误差 O(Z ell0/L²)=o(d)。没有使用任何第四矩。

**矩阵顺序必须保留。**Tr(W H C_L)=Tr(C_L W H)，
所以对应 physical Tr(E*B_L M_w B_H E)；
physical Tr(E*B_H M_w B_L E) 对应 Tr(W C_L H)。
三因子不能直接互换。本稿分别支付这两个 complex cross。

454 的全 log-range physical weighted 二矩允许 bounded complex
coefficient masks：取 B_H+zB_L，z=1,i，保留全部 genuine frequencies。
两个支持不交，故其 diagonal 仅为 high+|z|²low；
同号 Hilbert 主项、±L remainder、正负 sum-alias physical overlap
按 454 原证明不变。复极化得到

TrE*B_L M_w B_H E=o(d)，
TrE*B_H M_w B_L E=o(d)。                              (7)

这一步保留 common w、carrier 和两种 signs，不只得到 real part。
low weighted norm 同样给

d⁻¹TrE*B_L M_w B_L E=〈w d_low,L〉+o(1)。             (8)

(6)–(8) 完成 actual finite 结论：

j_T:=d⁻¹Tr(W H C_L)→0，
v_T:=d⁻¹Tr(W C_L²)→c0,ψ=∫d_H,ψ(v)d_low,ψ(v)dv。     (9)

Mertens/profile 极限正是原两个 diagonal 的相同物理变量，
没有混入独立 profile 或新 averaging family。
flat：
d_H(v)=(|v|²+|v|)/2，
d_low(v)=1/4−|v|/2+v²/2，
c0=23/960。

## 6. Γ 的精确联合约束及量词

定义 actual Γ=H²−W，
q_T=||Γ||HS²/d≥0，
e_T=TrC_L⁴/d，
c_T=TrH²C_L²/d≥0，
b_T=TrH³C_L/d（实数）。
前置 parity 稿的原 weighted-high 二矩给

a_T=Sψ+q_T+epsilon_T，epsilon_T→0。                  (10)

先使用非负 q_T，不能将可能微负的 a_T−Sψ 直接放进根号。
有限 HS Cauchy 严格给

c_T≤v_T+√(q_T e_T)，
|b_T|≤|j_T|+√(q_T c_T)。                              (11)

第一式是 Γ 对 C_L² 的 HS pairing；第二式是 Γ 对 H C_L，
因为 ||H C_L||HS²=TrH²C_L²=d c_T。
即使 j_T 是 complex，取模也仍合法。

实际 22 cyclic union w_T=4c_T+2Tr(HC_LHC_L)/d≤6c_T，
因为 |Tr(HC_LHC_L)|≤TrH²C_L²。这不是 square operator ordering。
whole finite prime fourth 准确展开为

F_T=Tr(H+C_L)⁴/d
   =a_T+e_T+4b_T+4η_T+w_T，
η_T=TrH C_L³/d。

在 461/462 同一 [R] 上，η_T→0、e_T→eψ。
**若另有 limsup q_T≤Q<∞**，才可把 (9)–(11) 的误差统一变成 o(1)，
得到 conditional upper

limsup F_T≤Sψ+Q+eψ+6C_Q+4√(Q C_Q)，
C_Q=c0,ψ+√(Q eψ)。                                    (12)

该 upper 随 Q 增加。没有 q_T bounded 前件时，必须保持 (11) 的
实际 e_T、v_T；不能让未知 √q_T 放大一个被免费删除的低矩 o(1)。

## 7. Flat 条件阈值与尚未付款

flat S=19/480、e=19/240、c0=23/960。
Q=0 的 (12) 为 21/80，严格小于 1/3。
这说明 actual Γ 联合信息优于只用 (H²,C_L²) 的粗 Schur envelope；
它本身没有证明 q_T→0。

作为具体反事实 threshold，取 Q=1/1600。
有理比较
√(Qe)<113/16000，
C_Q<1489/48000，
√(Q C_Q)<71/16000，
故 (12) 严格小于 1293/4000<2589/8000。
这些只证明所需 conditional budget 的数值有余量，
不是实际 Γ bound，更不是已经提高零点比例。

MT/nonflat 的 Sψ、eψ、c0,ψ 必须按其原 profile 重算；
不能把 flat 的 19/240、23/960 混入未知 MT whole-prime budget。
本稿新付的是 (4)–(5) 和 (9) 的原 finite-P 接口。
未知 q_T 的足够小上限、whole high signed arithmetic 与正式比例转换
仍是后续真实任务。
