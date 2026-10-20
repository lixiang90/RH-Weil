# 实际变分准入：完整平方缺陷、真实 receiver 与最强旧比较

2026-10-20。独占原稿；不修改公共 STATE/cadence/Git，不建 C036，不独立计轮。
恢复了 README/STATE、check/show、G20261014、宏观前沿、新路线图§4、560/571/572
及 560 的完整逆/clipping 原件。所有结论仍待 root 对齐其他原稿并消费。

**本门不是只得到“旧 clipping 加未知 D_var”：完整 D_var 可以直接保留两个残差，
写成一个真实正交投影能量，并在固定安全高频尺度上支付。572 的实际 b 权费用确实
可用于这个上界，但在同一安全尺度，560 的旧残差及粗范数本来已足以支付它。
所以本稿不能把更锋利的 receiver 子界登记为新的 whole/core 或独立容量输入。
实际 Sonin 的新 cofinal 桥，若成立，须消费另稿给出的具体候选原域与残差运输。
仍不进入危险核心；更低 θ 的失败只涉及这里的充分证书。**

## 1. 原对象、域和变分量

始终用原物理 H=L²(R,dy)，U_a f(y)=f(y−a)，有限 F，

\[
 B=\prod_{p\in F}(I-p^{-1/2}U_{\log p}),\quad D=B^{-1},\quad
 W=B^*B,\quad Z=DD^*=D^*D,\quad
 m=\prod_{p\in F}(1-p^{-1/2}),\quad M=\prod_{p\in F}(1+p^{-1/2}).
\]

m²I≤W≤M²I。P=P_T=1_(0,T)，L=1_(-∞,0)，H_+=1_(T,∞)，Q=L+H_+。
G=G_T=(PWP)|_(PH) 是 window Gram，不是实际 Sonin 空间的 G_M。

\[
 S=S_T=P(Z-DLD^*-D^*H_+D)P,\quad
 w=w_{R,T}=e^{iRy}1_{(0,T)}/\sqrt{2\pi},\quad
 T=T_R=\Gamma(R)=\Re\psi(1/4+iR/2)-\log\pi.
\]

一般算子身份对 T>0 成立；实际载波消费只用完整 Γ，绝不以裸 log R 定义 T。
G、G^{-1}、S 均为 PH 上有界自伴算子，G 正且可逆。

设

\[
 \Delta=G^{-1}-S,\quad r_T=(GS-I)w=-G\Delta w,\quad
 D_{\rm var}(w)=\|G^{-1/2}r_T\|^2=\|G^{1/2}\Delta w\|^2.       \tag{1}
\]

完整 window 变分身份为

\[
 \langle w,G^{-1}w\rangle-
 \{2\Re\langle w,Sw\rangle-\langle Sw,GSw\rangle\}
 =D_{\rm var}(w)\ge0.                                      \tag{2}
\]

这是已有正 Gram 代数的直接推论。模型 signed 差
δ=〈w,Δw〉满足

\[
 2\Re\langle w,Sw\rangle-\langle Sw,GSw\rangle
 =\langle w,Sw\rangle+\delta-D_{\rm var}.                    \tag{3}
\]

所以 δ_+ 的费用不能直接替代 D_var，且忽略 −D_var 会改变候选的实际变分值。

## 2. 同一个 receiver pair、完整 J inverse 与相位

沿571，定义有界 E:PH→LH⊕H_+H，

\[
 Ew=\binom vu,\quad v=LD^*Pw,\quad u=H_+DPw,\quad
 K=LBD^*H_+,\quad J=\begin{pmatrix}I&K\\K^*&I\end{pmatrix}.
\]

外域半线因子的 Schur 身份原样给

\[
 G^{-1}=PZP-E^*J^{-1}E,\qquad S=PZP-E^*E,
\]
\[
 \Delta=E^*(I-J^{-1})E,\qquad
 D_{\rm var}(w)=\|G^{1/2}E^*(I-J^{-1})Ew\|^2.                \tag{4}
\]

δ=〈Ew,(I−J^{-1})Ew〉只是同一算子在同一 pair 上的线性二次配对；
D_var 则是再经过 E*、G 的完整平方，二者不能同一化。
(4) 中 J^{-1} 包括全部 returns，且同时保留两边界。

记 b=b_F(R)，V=bar b·v，U=b·u，η=bar b/b，C_b=diag(I,η)。则

\[
 \bar b\,Ew=C_b\binom VU,\qquad
 J_b=C_b^*JC_b=\begin{pmatrix}I&\eta K\\\bar\eta K^*&I\end{pmatrix},
\]
\[
 |b|^2D_{\rm var}
 =\left\|G^{1/2}E^*C_b(I-J_b^{-1})\binom VU\right\|^2.       \tag{5}
\]

因此独立 clean 两个 receiver 后仍必须运输 K→ηK。下节不展开 J^{-1}，
而是用完全相同的残差重组能量；这是保留完整逆的身份，不是截掉 returns。

## 3. 完整残差恰为两个 cross-window tail 的投影能量

560 已付的精确双残差是

\[
 GS-I=PW H_+DL D^*P+PW L D^*H_+DP.
\]

对本真实 w 令

\[
 q=q(w)=H_+Dv+LD^*u\in QH.
\]

于是 r_T=PWq。BPH 是闭子空间（B 有界且有界可逆），其正交投影为

\[
 \Pi_{BPH}=BP G^{-1}PB^*.
\]

这不是假设正性，也没有以 B 为酉。直接计算得到准确能量身份

\[
 \boxed{D_{\rm var}(w)
 =\langle PWq,G^{-1}PWq\rangle
 =\|\Pi_{BPH}Bq\|^2\le\|Bq\|^2.}                          \tag{6}
\]

q 的两个 summand 位于互相正交的左右外域；左/右交互仍在 B 与投影中。
没有把 ||H_+DL|| 的任意全空间下界当作实际 v 的费用。

因果展开 D=Σ_(n∈N_F)n^{-1/2}U_(log n) 在 operator norm 绝对收敛。
定义完整有限集尾

\[
 \tau_F(T)=\sum_{\substack{n\in\mathbb N_F\\\log n>T}}n^{-1/2}.
\]

H_+U_(log n)L=0 当 log n≤T，因此

\[
 \|H_+DL\|\le\tau_F(T),\qquad
 \|LD^*H_+\|\le\tau_F(T).
\]

(6) 给出

\[
 \boxed{D_{\rm var}(w)\le M^2\tau_F(T)^2
 (\|v\|^2+\|u\|^2).}                                      \tag{7}
\]

这与 m/M 导出的 J gap 不同；它由同一真实 pair 的 cross-window tail 得到。
同时它只是560双残差加一般正交投影能量的直接合成，不是新的外部容量定理。
对真实载波实系数反射给 ||u||=||v||，故实际 b 权原 dy 版本为

\[
 |b|^2D_{\rm var}(w)\le
 2M^2\tau_F(T)^2 |b|^2\|v\|_{dy}^2.                         \tag{8}
\]

本式没有除 b，没有改变 Hilbert 范数，也没有以 m² 归一替代实际权。

## 4. 完整 cross-tail 的成长账本

以下只是572已核同一 PNT/Abel 估计的权1版本。
F_L={p<e^(2L)}，固定 k>0，γ=k/(2L)，s=1/2−γ。

\[
 \tau_{F_L}(T)\le A_\gamma e^{-\gamma T},\qquad
 A_\gamma=\prod_{p<e^{2L}}(1-p^{-1/2+\gamma})^{-1}.
\]

使用572对移动指数 s 在固定紧子区间内的 PNT/Abel 统一估计，

\[
 \sum_{p<e^{2L}}p^{-s}=(e^k+o(1))e^L/L,
\quad
 \log A_\gamma=(e^k+o(1))e^L/L.                             \tag{9}
\]

二次 Euler remainder 为 O_k(log L)，因为 p^{-2s}≤e^{2k}/p；
三次及以后在 s≥1/4 后可进一步选固定 s>1/3 的最终 L 范围，uniformly 可和。
因此 remainder 为 o(e^L/L)，不能把固定 s 的 PNT 不经统一证明套到 s(L)。
该统一证明已由572实际消费；这里没有新 PNT 定理。

同一固定 F_L 的旧 Mertens/PNT 账本为

\[
 \log M^2=(2+o(1))e^L/L,\quad
 \log m^{-2}=(2+o(1))e^L/L,\quad
 \log(M^2/m^2)=(4+o(1))e^L/L.                              \tag{10}
\]

若 R≥R_0=exp(θe^L)，完整 Γ 给 T≥θe^L−O(1)。置

\[
 d(\theta,k)=\theta k/2-e^k.
\]

则 τ≤exp[−(d(θ,k)+o(1))e^L/L]，uniformly 在本高度以上。
这是全部 n 的实际尾，未留第二条无限相干尾。

为避免任何阈值优化，本门统一取安全常数

\[
 \boxed{\theta=16,\quad k=\log4,\quad
 d=8\log4-4>7.}                                           \tag{11}
\]

γ 是解析证明参数，不改变完整 Γ 的定义。这个选择只是非空充分证书；
既不声称16是必要阈值，也不排除更低高度、signed 或源适应修复。

## 5. 572 的原 b 权费用确实可用于完整 D_var

取572合法 I_L=[R_0,R_0+R_0^β]，例如固定 β=1/2，R_0=exp(16e^L)。
572主结果 av_(I_L)|b|²||v||²=O(L⁴) 与(8)给

\[
 \operatorname{av}_{I_L}|b|^2D_{\rm var}
 \le O(L^4)\exp[(2-2d+o(1))e^L/L]=o(1).                    \tag{12}
\]

完整 Γ 的 T_R 变化只使 τ(T_R) 更小；估计在 Γ(R_0) 取统一上界。
两边界仍按(5)协同，没有把572的 δ_+ 误当 D_var。

还可用准确 Cauchy–Schwarz

\[
 |\delta|\le\langle w,G^{-1}w\rangle^{1/2}D_{\rm var}^{1/2},
\quad
 |b|^2\langle w,G^{-1}w\rangle\le(M^2/m^2)T/(2\pi).
\]

故 (10),(12) 给

\[
 \operatorname{av}_{I_L}|b|^2|\delta|
 \le O(L^2\sqrt{e^L})
 \exp[(3-d+o(1))e^L/L]=o(1).                               \tag{13}
\]

这在本安全高度支付 δ 的绝对值与完整 window 变分差 δ−D_var，
比只知道 δ_+ 的费用强；不过是否是“新的净输入”必须扣下节最强旧后果。

## 6. 不能把572必要化：最强旧残差在同一安全高度已足够

先用旧粗 ||v||²+||u||²≤2m^{-2}||w||²，(7) 本身就给

\[
 D_{\rm var}\le2(M^2/m^2)\tau_F(T)^2\|w\|^2,
\quad
 |b|^2D_{\rm var}\le2M^4m^{-2}\tau_F(T)^2\|w\|^2.           \tag{14}
\]

即使不使用(6)的较锋利投影能量，只用560旧残差也有

\[
 \|r_T\|\le2M^2\tau_F(T)m^{-1}\|w\|,
\quad
 D_{\rm var}\le4M^4m^{-4}\tau_F(T)^2\|w\|^2.                \tag{15}
\]

这是旧 exact residual、原范数、G^{-1}≤m^{-2}I 的直接推论。
在(11)的安全高度，(14) 的 actual b weighted exponent 为6−2d<0，
(15) 的相应 exponent 为10−2d<0；T 因子只有 log T=O(L)，不改变结论。
所以完整 D_var 的高频支付并不逻辑依赖572均值。

实际 Sonin 另稿残差运输若给

\[
 D_M\le m^{-2}\{M\sqrt{D_{\rm var}}+h\}^2,\qquad
 h\le C R^{-1/4}(1+2M^2/m^2),                              \tag{16}
\]

则用(15)保守估计，|b|²D_M 的 tail 主项 exponent 至多14−2d<0。
R^{-1/4} 在 R_0=exp(16e^L) 上远胜所有 exp(Ce^L/L) 的有限 F 费用。
并且 T e^{-2γT} 在 T≥Γ(R_0) 后单调下降，因此这不是只有平均证书：
一旦另稿在同一原域实际证明(16)，上述付费在全部 |R|≥R_0 上一致趋零。
负高频用实际实结构及 Γ 偶性运输，不更换 receiver 域。
因此(16)并不因 m^{-2} 原逆费用而在此高度失败。
本稿不独立认证(16)的 P_M/clipping 原域；必须消费实际 source/domain 原稿。

旧560 operator 证书本身还给

\[
 \|S-G^{-1}\|\le2M^2 A_\gamma m^{-3}e^{-\gamma T}.
\]

在(11)其 exponent=5−d<0，实际 b 权 δ 的粗上界 exponent=7−d<0；
T e^{-γT} 同样在本高度以后单调，故得到全高频一致的绝对差趋零。
但若只从这条 operator norm bound 推 D_M，会白付额外 condition 因子，
在 θ=16 不足；不能因此忽视(15)这个更强旧 exact residual decomposition。
因此(13)在本尺度同样已有强旧直接证书。保留更锋利的(12)有助恢复系数机制，
但不能以“改善 δ 或 D_var 的弱旧上界”登记新的全对象净后果。

## 7. 完整 Γ、素数幂与极点未被本模型替换

窗口平均/残差不是 actual ε_F，也不是原 Weil 源 r。若另一原稿实际闭合
(16)与候选变分值的 clipping，才可合成 actual density 的同高度估计。
尚须独立保留旧560完整模型主项，而非仅 S 与 G^{-1} 的差：

\[
 |b_F(R)|^2\langle w,S_Tw\rangle
 =\Gamma(R)/(2\pi)
 -\pi^{-1}\Re\sum_{p\in F}\frac{\log p\,\alpha_p}{1-\alpha_p}
 +E_{S,F}(R),\quad \alpha_p=p^{-1/2}e^{-iR\log p}.
\]

这是560精确 delay 配对的旧身份，完整 proper powers 来自对数导数，
不能用本稿 finite Euler μ 系数替代。本稿的完整 D_var 控制不等于该主项
所有尾已付；其 C_(F,γ)、J_γ 和 contact 核算交由同门实际 source 原稿逐项证明，
root 必须另行闭合，不能由本稿的投影能量代替。

完整原源身份仍是

\[
 2\pi\rho_F=\Gamma-2\sum_{p\in F,j\ge1}(\log p)p^{-j/2}
 \cos(jR\log p)+\epsilon_F,
\]
\[
 Q_W(r)=t_F(r)-\langle r,K_{F,I}r\rangle
 +2|\langle r,\cosh(u/2)\rangle|^2
 -2|\langle r,\sinh(u/2)\rangle|^2.
\]

本稿未令任何 pole 矩为零；双极点、全部 prime powers 和全 Γ 仍在同一源定义中。
dy receiver、window carrier、Sonin 裸求值及原 du/Dlog 源始终不同。

## 8. 净后果、停止范围与尚缺的独立输入

本稿独立核清：D_var 的完整正交投影身份、真实 pair 的完整 cross-tail 上界，
以及572实际 b 权确实能在安全高度支付该上界。它还核清：在同一高频层，
旧560残差已足，不能把572的子界改善当新的 whole 费用。
若 source/domain 原稿闭合(16)，新可消费桥限于原先未知的实际候选 cofinal 运输，
其代数/算术输入全部来自已付 clipping、有限 Euler/PNT 和实际正 Gram，
而非一个独立全局容量机制。

θ=16 远在旧555已有利的 θ>1 层。所有结论不改 θ≤1 危险核心、低频/
中频补空间、source coupling、最强旧542+555→557 whole leading4/5 或通常 Ξ 门。
不把更低 θ 下充分上界不趋零当实际误差 lower，不排 source-adapted、signed、
Γ-relative 或新的全逆组织。此门结算后不继续扫 θ/k/β、single-prime 或第三 prime。

要把这个高频桥变成独立经典 Weil 正性，仍须提供至少：

- 真正覆盖危险核心和全部原 complex Dlog 源的同对象 signed 费用，保 Γ/pp/poles。
- 将物理高频密度界合法运输到需要的原 source norm，并支付低频与 coupling。
- 或由同一 global sections/kernel/乘法对象独立给局部消失下界与全局容量，
  再识别完整 mixed 预算，而不是直接假设完整 Weil Gram PSD。

这些都是剩余责任，不是本稿已经证明的结论，也不能仅以未知支配条件改名续约。

## 9. 原件与复核范围

已读必要原件：

- `notes/560-joint-finite-place-sonin-primepower-cancellation-and-compact-weil-bridge.md` §§1–4、6。
- `reviews/2026-10-14/joint-sonin-cross/full-inverse-carrier-error.md` 全文，尤其§§3–5。
- `notes/571-actual-receiver-two-boundary-signed-comparison-and-growth.md` §§1–3。
- `notes/572-finite-euler-receiver-coherent-tail-and-original-weighted-cost.md` §§1、5–8。
- `goals/reviews/2026-10-20-generalized-weil-facilities-roadmap-after-572.md` §4。

无外网来源、数值或后台进程。本稿没有重证532实位 clipping 或完整 PNT/Mertens；
这些按现有 root 消费记录继承。新的 exact 代数和成长费用已在上文逐项给出，
原件出稿不等 root 消费，数学强度由 root 总审另定。
