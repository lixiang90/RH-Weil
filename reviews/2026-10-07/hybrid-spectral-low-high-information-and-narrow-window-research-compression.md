# 已付低高谱信息与窄窗策略：独立研究

2026-10-07。只新增研究稿；不修改旧数学、源、Goal 或 Git。

结论：现有 low4、entire13、首二矩及 high parity 不能在其谱数据
松弛中排除二矩等号配置。窄到支撑宽度 b≤1/2 后，完整第四矩可以
支付，但出现更强的渐近有限块障碍，单靠这些矩与部分 Weil 惯性
账本不能认证正的简单零点比例。没有得到新的比例或无零边界。

## 1. 同对象范围与输入绑定

以下 SHA-256 均对 UTF-8、CRLF/CR 统一为 LF 的完整字节计算。

|输入|canonical LF SHA-256|
|---|---|
|notes/197-partial-weil-proportions-regions-four-moments.md|98bd8ea89679030e0ffb8135d324b5654900f260b3f45c9ae816d5ea870eaae7|
|notes/454-original-background-and-weighted-prime-mixed-traces.md|8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7|
|notes/455-whole-proper-power-fourth-norm-and-prime-equivalence.md|6bf2025dcc8f56d7b35d9c8b764ac2ff3b911a6e054bf9c496042c7f3e11ce41|
|notes/461-original-one-high-three-low-fourth-trace.md|f9fdf0b721c76a5cc4c4e4821748007e62975286417e6bec9700e39b6778170b|
|notes/462-original-low-prime-fourth-path-constant.md|868adfeb0d742043f39bd08e0783d66b7a9db11316067b0b3b43d80150cdf680|
|notes/463-two-sided-height-stability-for-original-fourth-words.md|6554ebc80616917d00b68f626329e8464e6ccc218c456608bff74e9da5a17d90|
|reviews/2026-10-07/hybrid-whole-fourth-compression-upper-research-radial.md|0703f66778d49de29e363f7eabede6718ef24fe579e53603ff70db4e6aeacdea|
|reviews/2026-10-07/hybrid-high-parity-gram-and-mobius-completion-research-radial.md|3f4c714bb126356389332f3674836d6edf6f110f60935a27af93a58a0e26bbb2|

采用原 X=T/(2π)、L=log X、d=floor(XL)∼N(T,2T)、interval carrier
E、P=EE*、Q=1−P。原完整 Gram 写成 G−I=A+CΛ，A 为原 Gamma/pole
减 I，CΛ 为完整 Λ channel。prime-only 再分成 C_L+C_H。

flat low4=19/240 与 Montgomery–Taylor 的二矩常数属于不同 profile。
禁止把前者直接和后者的 v 合成同对象证明。下面先给 flat 同数据
反模型，再明确一般标量 LP 松弛与真实非平背景之间的区别。

部分 Weil 谱账本为 G=P_s+Q_b，P_s≥0，rank P_s≤s，Tr P_s≤s，
n_+(Q_b)≤b_bad，以及 Tr P_s+2b_bad≤N+o(N)、s+2b_bad≤N+o(N)。
它推出 s/N≥1−v，v=Tr(G−I)^2/N，二矩等号谱为 0、1、2。
7/8 strip 是零点位置限制；它本身没有增加下述矩的上界。
双侧 height 是同类型对象替换的误差界，也没有增加内部谱限制。

## 2. 精确七原子：low4 与 entire13 仍允许 flat 二矩等号

令 C=G−I，L_0、H_0 为两个 commuting Hermitian 数据变量，C=L_0+H_0。
以下是单位总质量的七原子分布，平方根为普通实数：

* C=±1 各质量 1/6；条件于每个 C，
  L_0=C/2±sqrt(3/40) 各概率 1/2，H_0=C−L_0。
* C=0 质量 2/3；其条件分布为 L_0=0 概率 19/26，
  L_0=±sqrt(13/40) 各概率 7/52，H_0=−L_0。

直接展开给

\[
 \mathbb EC=\mathbb EL_0=\mathbb EH_0=0,\quad
 \mathbb EC^2=1/3,\quad
 \mathbb EL_0^2=\mathbb EH_0^2=1/6,\quad
 \mathbb E(H_0L_0)=0,
 \tag{1}
\]
\[
 \mathbb EL_0^4=\mathbb EH_0^4=19/240,\quad
 \mathbb E(H_0L_0^3)=\mathbb E(H_0^3L_0)=0,\quad
 \mathbb E(H_0^2L_0^2)=7/240,\quad
 \mathbb EC^4=1/3.
 \tag{2}
\]

实际原子质量为四个 1/12、一个 19/39、两个 7/78；d 取 156 的倍数
即可由 diagonal matrices 准确实现。这里 every entire13 placement
都为零，还额外使 entire31 为零、high4 有界。依然有 G 谱质量
1/6 在 0，2/3 在 1，1/6 在 2。取 P_s=1_{G=1}、Q_b=2·1_{G=2}，
则 s=2d/3、b_bad=d/6，所有 rank、trace、inertia 预算准确取等。

因此新付 low4 与 entire13 没有单独强迫 flat centered fourth 严格
小于 1/3。它们更不能单独认证超过历史 MT 的 0.6725007…。
此模型是信息不足的证明，不是实际 prime matrix、AF feature kernel
或 zeta 零点配置的实现。已有 kernel 几何若排除此模型，是额外输入。

该分布在 (C,L_0,H_0)→(−C,−L_0,−H_0) 下不变，存在 involution U
使 UH_0U=−H_0。令 Π±=(I±U)/2、A_0=Π−H_0Π+，则 A_0²=0、
H_0=A_0+A_0*。所以抽象 high nilpotence、精确 parity 也不排除它。
这不声称 A_0 是实际带正素数权重的 physical translation sum。

## 3. 一般二矩常数的标量数据松弛

若 0<v≤1/2、v/8≤c≤v/2，令 C=±1 各质量 v/2、C=0 质量 1−v，
L_0=C/2+Z、H_0=C/2−Z。条件噪声关于零对称。取

\[
 u=\frac{c/v-1/8}{3/2}\in[0,1/4],\quad
 w=\frac{v(1/4-u)}{1-v},\quad
 k_w=\frac{v(1/16-u^2)}{1-v}.
 \tag{3}
\]

C=±1 时 Z=±sqrt u 等概率；C=0 时使 EZ²=w、EZ⁴=k_w，
可取 0 与 ±sqrt(k_w/w)，非零总概率 w²/k_w。零退化值按极限解释。
其可行性是准确因式分解

\[
 k_w-w^2=
 \frac{v(1-4u)(4u-2v+1)}{16(1-v)^2}\ge0.
 \tag{4}
\]

得到 EL_0²=EH_0²=v/2、EH_0L_0=0、EL_0⁴=EH_0⁴=c、
EH_0L_0³=0、EC⁴=v，仍是 s/N=1−v 的二矩等号。
非有理质量由对称有限矩阵序列逼近，全部所列矩收敛。

这说明仅把 v、low2、low4、13、high parity 作为 scalar trace
约束，不能一般推出新的比例。它不把非平窗的实际 A 偷改成零。
下面补充一个保留 MT 背景 marginal 与精确 parity 的更强模型，
仍明确不实现 454 的全部 joint quadratics 或原 feature kernel。

### 3.1 保留 MT Gamma marginal 的二矩等号模型

取 ψ(t)=cos(sqrt2·t)、a=∫ψ、α(t)=ψ(t)/a−1，t 在 [-1/2,1/2]
按 Lebesgue probability 分布。用 α 避免与上文 physical A_H 混名。
记 v=v_MT、V=∫α²、M4=∫α⁴、K1=∫|α|、K3=∫|α|³，
以及实际 high prime 二矩

\[
 V_H=\frac2{a^2}\int_{1/2}^1 x g(x)\,dx,\qquad
 g(x)=\tfrac12\{(1-x)\cos(\sqrt2x)+\sin(\sqrt2(1-x))/\sqrt2\}.
 \tag{3a}
\]

actual low 二矩为 V_L=v−V−V_H。下述 2×2 blocks 中 A_bg=α I，
U=diag(1,−1)，σ_x 为 offdiagonal Pauli matrix。给定 α，随机取

* 概率 |α|：C=sgn(α)I、H_0=0；
* 概率 v−|α|：C=σ_x、H_0=hσ_x；
* 概率 1−v：C=0、H_0=zσ_x。

MT 满足 |α|<1/5<v，故三概率非负。置 G=I+C、L_0=C−A_bg−H_0。
此时 A_bg 与 U commute，UH_0U=−H_0 准确成立。每个 block 内
conditional normalized trace C 的平均为 α，trace C² 的平均为 v。
所以 G 仍具有旧等号谱：质量 v/2 在 0、1−v 在 1、v/2 在 2；
且 Tr(A_bg·(L_0+H_0))=0，完整 prime 二矩为 v−V。

令 B=v−K1、B2=vV−K3、Z2=(1−v)V、m=V_H/B。取 h=m±sqrt u
等概率，z 为对称三原子噪声，Ez²=w、Ez⁴=k。定义

\[
 \begin{aligned}
 c_0={}&B(1-m)^3+3B2(2-3m+m^2)
       +3V(V_H-Bm^2)+K1-4V+6K3-3M4,\\
 c_1={}&3(B-V_H+VK1-K3),\qquad
 u=(\mathcal C_L(\psi)-c_0)/c_1,\\
 w={}&\{V_H-B(m^2+u)\}/(1-v),\\
 k={}&\{B\mathbb E[h(1-h)^3]+3B2\mathbb E[h(1-h)]-3Z2w\}/(1-v).
 \end{aligned}
 \tag{3b}
\]

给 z 质量 1−w²/k 在零，±sqrt(k/w) 各质量 w²/(2k)。2×2
trace 的直接多项式展开给

\[
 \mathbb EH_0^2=V_H,\quad \mathbb EL_0^2=V_L,\quad
 \mathbb E(H_0L_0)=0,\quad
 \mathbb EL_0^4=\mathcal C_L(\psi),\quad
 \mathbb E(H_0L_0^3)=0.
 \tag{3c}
\]

所有 first moments 为零；A_bg 有实际 MT 背景的整个 scalar marginal。
conditional trace C=α 还使 E[f(A_bg)(L_0+H_0)]=0 对所有 bounded f
成立。H_0 有 bounded fourth、精确 spatial parity，但 Tr(G−I)^4/d=v，
旧 simple fraction 1−v 依然取等。

这里可行性不依赖未认证的浮点 quadrature。以下粗有理区间足够：

|量|严格包含的有理区间|
|---|---|
|v|[.32749,.32751]|
|V|[.0061271,.0061273]|
|M4|[.00007878,.00007880]|
|K1|[.0675305,.0675326]|
|K3|[.000654884,.000654885]|
|V_H|[.1499168,.1499170]|
|C_L(ψ)|[.08430,.08566]|

可复核的证书如下。设 P_j(t)=Σ_(i=0)^j (−1)^i2^i t^(2i)/(2i)!，
则 P_5≤ψ≤P_6，积分给 a 的上下界；sin(sqrt2 t)/sqrt2 也用对应
的 alternating rational Taylor polynomial。它们直接夹住 (3a)、v、V、M4。
α 的唯一正半轴根位于 [.287,.288]；|α'|≤1。对 K1、K3 用 r=.287
分段积分 odd powers，根位置的上方修正分别≤2·10^-6、10^-12。
P_5/a_upper−1 对 α 的 uniform error<10^-9，足够覆盖 V、M4 的余差。
全部分段积分是有理 polynomial integrals。

对 c，P_1≤ψ≤P_2，正路径 integrands 的 exact numerator 下、上界为
3989807597/66421555200 与 418537850292443239/6920254601035776000；
同时 11/12≤a≤147/160。除以相应 a⁴ 得
.0843050333…≤c≤.0856577989…，包含于表中的区间。
用表内有理端点作 interval arithmetic，(3b) 严格给

\[
 .04323<u<.04742,\quad .07602<w<.07768,\quad
 .01904<k<.01959,\quad k-w^2>.01301>0.
 \tag{3d}
\]

所以所有 noise probabilities 均合法。对连续 α、type probabilities
作有限 empirical approximation，可保留每个 2×2 block 的 parity，
所有所列矩收敛；0/1/2 等号谱与 partial-Weil counts 同时逼近。

严格范围：本模型匹配原 MT 的 background marginal、首二矩分解、
low4、entire13 与 high parity；它不满足原 454 中所有已付 joint
quadratics。尤其本模型 A_bg 与 prime channel commute，而原
Tr(ACAC) 与 Tr(A²C²) 的差为非零 Jψ/2。该额外数据或真实 kernel
几何仍可能排除模型。不能把本节当作实际 MT Gram 的完整实现。

## 4. 实际 high 有一个无条件谱对称估计

对原 p>sqrt X 的单向 physical sum A_H，所有 log p>L/2，
输入、输出分别在 I 的两个相反半区。于是

\[
 A_H=\Pi_-A_H\Pi_+,\quad A_H^2=0,\quad
 B_H=A_H+A_H^*,\quad JB_H+B_HJ=0,
 \tag{5}
\]

这里 J=M_sgn u。置 S=E*JE、C_H=E*B_HE。原 integer interval
basis 中 J 的 Fourier coefficients 对 odd n 的模为 2/(π|n|)，
其余为零，故

\[
 \ell_J^2=\|QJE\|_{HS}^2=\operatorname{Tr}(I-S^2)=O(\log d).
 \tag{6}
\]

原有限 P 的准确剩余项为

\[
 SC_H+C_HS=-(QJE)^*(QB_HE)-(QB_HE)^*(QJE).
 \tag{7}
\]

取 U=sgn S，零特征值处选 +1。则 U²=I，
||U−S||HS²≤Tr(I−S²)。用全局 ||B_H||≤y_H≪sqrt X/L 得

\[
 \|C_H+UC_HU\|_{HS}\le4y_H\ell_J,\qquad
 d^{-1}\|C_H+UC_HU\|_{HS}^2=O(L^{-2}).
 \tag{8}
\]

Hoffman–Wielandt 给排序后 d^-1Σ|λ_j+λ_(d+1−j)|²=O(L^-2)。
固定 bounded Lipschitz odd 函数的平均因而趋零；经验 high 谱在
二次运输距离上渐近对称。原 Q 未删除，也没有更换 global Fourier band。

这个定量新估计仅控制二次谱距离。用 y_H 升级到 normalized S4
误差只得 O(X/L⁴)。稀疏的 ±大特征值可以完全对称而有增长的第四矩。
同样，A_H²=0 本身不能给 actual/physical positive compression gap
一个固定比例下界：抽象 bipartite H 与 P=I 的 gap 恰为零。
任何利用实际 gap 严格省预算的证明都须再付款 carrier/arithmetic 关联。

## 5. 支撑宽 b≤1/2：先准入，再付款完整 fourth

选择 T 前固定的 even nonnegative ψ≤1，support 位于
[-b/2,b/2]，0<b≤1/2，a=∫ψ>0，并要求 sqrt ψ 为 C² 的零延拓。
仍用原 E、d、τ_k、外层 χ，φ=χχ sqrt(ψ(u/L))。
这里不假设 ψ 在 ±1/2 正；它是新的窗口选择而非旧正窗定理的直接引用。

AF 窗准入所需的非负 feature、单位平方范数预算及 paired inertia
不需要端点严格正。具体地，原未归一化 Fourier convention 中
v_ρ=(hat φ(γ_ρ−α_k))_(0≤k<d)。support φ⊂I 保证 convolution
support 长度≤2L；Poisson 的 dual lattice LZ 上除零外均为零，给
Σ_(k∈Z)hat φ(z−α_k)²=a_LL²。对实 γ_ρ，有限平方和非负，故
||v_ρ||²/(a_LL²)≤1，simple feature 的 trace 预算不变。
functional-equation 的非实 pair 给两个共轭 features，其 2×2
Hermitian coefficient form 至多一个 positive direction；pullback
仍有 n_+≤1。线上 multiplicity≥2 项也只有一个 positive direction，
每个至少花两个零点。这个 paired inertia 论证不需要 φ 的满支撑。

对充分大 L，本节 support 远离外 χ 层，φ(u)=sqrt ψ(u/L)，
||φ||1=O(L)、||φ'||1=O(1)、||φ''||1=O(1/L)。原 Fourier C² tail
保留；复参数的 Paley–Wiener factor e^(bL|Im z|/2) 还小于原界。
padding 仍用固定导数界、a>0 和原 strip，不添加新量词。因此首二矩
及零侧账本的证明逐项保留。不能因为 support 缩小而宣称 finite E
的 Gram rank 变成 bd。

对所有 n，有 Mφ R_log n Mφ=0 当 log n≥bL（等号只可能有零测端点）。
故完整 physical Λ sum 准确只剩 n<X^b，所有 genuine primes 都是
462 的 low 范围。462 的 crossing、far/alias、near Hilbert 及零词枚举
只用固定 C² bounds 和非负路径窗；将上限改为 b，其余证明仍成立。
可以把 462(5) 的 x,y 上限保持 1/2，因超支撑的 integrands 为零。
其证明不需要本节已经删除的端点正性。

于是 whole prime fourth=O(d)。455 的 proper-power S4-small 证明
同样只用 φ 的固定 support、tail、a>0，故 whole Λ fourth=O(d)。
454 的原 Gamma estimate 给

\[
 G=G_0+C_\Lambda+R_T,\quad
 G_0=E^*M_{\phi^2/a_L}E,\quad \|R_T\|_{op}=O(1/L),
 \qquad \operatorname{Tr}G^4=O(d).
 \tag{9}
\]

第二项的 physical norm 由 Chebyshev/partial summation 给
y_b≪X^(b/2)/L。所有常数可依赖固定 profile 与 b。
这里已支付整个 fourth；随后失败来自谱 LP 账本，不是新的算术欠账。

## 6. 原 finite carrier 的渐近块：不误称 actual rank

令 J_b=[−bL/2,bL/2]，
R_b=E*1_Jb E，Π_b=1_[1/2,1](R_b)，Q_b=I−Π_b。
indicator Fourier coefficient 为 sin(πbn)/(πn)，所以准确有

\[
 \operatorname{Tr}R_b=bd,\quad
 \operatorname{Tr}(R_b-R_b^2)
 =\sum_{n\ne0}\min(d,|n|)
       \left|\frac{\sin(\pi bn)}{\pi n}\right|^2=O(\log d).
 \tag{10}
\]

对 r∈[0,1]，|1_(r≥1/2)−r|≤2r(1−r)，
且 r·1_(r<1/2)≤2r(1−r)。因此

\[
 \operatorname{rank}\Pi_b=bd+O(\log d),\qquad
 \|M_\phi E Q_b\|_{HS}^2
 \le\operatorname{Tr}(Q_bR_b)=O(\log d).
 \tag{11}
\]

把 BΛ 写成 Mφ D_b Mφ，D_b 为有限实线 shift sum，||D_b||≤y_b。
于是 ||CΛ Q_b||HS≤y_b O(sqrt(log d))、||CΛ Q_b||op≤y_b，给

\[
 \|C_\Lambda Q_b\|_{S_4}^4
 \le\|C_\Lambda Q_b\|_{op}^2\|C_\Lambda Q_b\|_{HS}^2
 \ll X^{2b}/L^3=o(d),\qquad b\le1/2.
 \tag{12}
\]

同一右 packet 使 ||G_0 Q_b||S4⁴=O(log d)；R_T 的 normalized
S4 为 O(1/L)。用 G selfadjoint 及
G−Π_bGΠ_b=Q_bG+Π_bGQ_b，得到

\[
 d^{-1/4}\|G-\Pi_bG\Pi_b\|_{S_4}\longrightarrow0.
 \tag{13}
\]

由 (9) 及 telescoping/Hölder，对 k=1,2,3,4 有
d^-1Tr(G^k−(Π_bGΠ_b)^k)→0。这是在同一个 finite carrier 中成立的
原始矩稳定性；并不声称 G 的实际 rank≤bd。G 可仍 full rank，
只是至少约 1−b 的谱质量在此 moment 意义下收缩至零。

若 b<1/2，tilde G=Π_bGΠ_b 的 rank≤floor(d/2) 对充分大 T 成立。
若 b=1/2，仅多出 O(log d) 个方向；删去该压缩矩阵的至多 O(log d)
个 eigenvectors 即得到 rank≤floor(d/2) 的 tilde G'。因为
||G||op≪1+y_b，额外 S4⁴≤O(log d)(1+y_b)^4=O(X/L³)=o(d)。
所以四个矩的同对象稳定性仍成立，不需要把 o(d) 变成固定边界预算。

现在取 P_s=0、Q_bad=tilde G'、s=0、b_bad=floor(d/2)，N=d。
则 n_+(Q_bad)≤rank tilde G'≤b_bad，两个 count/trace 预算成立。
Tr Q_bad/d→1；前四原始矩与原 G 一致至 o(1)。若恢复实际 N∼d，
只产生 o(N) 的正规化/count 误差。

这是严格的部分 Weil 谱数据模型，允许零 simple fraction。它不提供
真实零点 features 的实现；因此不能用于反驳 RH 或完整 AF 几何。
但是任何只依赖这些首四矩、rank/trace/inertia 预算的渐近证书都必须
接受它。必要条件是 b>1/2，才有希望从这条 moment route 得到正比例。
额外 feature 可见性若能辨别 tiny eigenvalues，可以超出此松弛。

## 7. 可核对的窄 flat 极限与继续研究的最低前件

作为 admissible smooth profiles 在 T→∞ 之后再趋于 indicator 的
说明性极限，ψ=1_[−b/2,b/2] 给 prime 二、四矩 b/3、4b/15，三矩为零。
两种路径积分为 b⁵/20 与 b⁵/120，fourth 为
(4·b⁵/20+8·b⁵/120)/b⁴=4b/15。背景在 bulk 等于 1/b。
所以完整 raw moments 为

\[
 m_1=1,\quad m_2=1/b+b/3,\quad
 m_3=1/b^2+1,\quad m_4=1/b^3+2/b+4b/15.
 \tag{14}
\]

具体概率模型为：质量 1−b 在 G=0；质量 b 的内部取
G=1/b+C_0，C_0=0 概率 7/12、C_0=±2/sqrt5 各概率 5/24。
它准确给 (14)，且 b≤1/2 时 positive rank fraction≤b≤1/2，
全部可以归入上述 bad 账本。hard indicator 不是本节 C² admissible
window；(14) 不冒充一个固定硬窗的有限 T 定理。

继续研究有三个真实接口：

1. 在原 MT 同 profile 下，直接支付 centered full fourth B4<v_MT。
   197 的 quartic formula 此时严格优于其二矩比例 1−v_MT。
   任意目标 p 的条件是 B4<(1−v_MT)²/p−1+2v_MT，并须满足完整边界前件。
2. 若仍用 flat 同 profile，超过历史 MT 需 B4<0.3275499074…；
   low4=19/240 与 entire13=0 不能代替 whole fourth。461 的展开尚有
   whole high4、31、22 product/commutator；454 还保留 background AC³。
   新 high residual 若付到足够小的一侧总预算，可实际进入该阈值。
3. 对 b≤1/2 的窗口，必须增加原 zero-feature 几何/visibility 约束，
   排除第6节纯 bad 块模型。单独再支付谱矩仍不区分这些模型。
   若改取 b>1/2，则 balanced products 可长于 X，原 high 算术欠账重现。

此处不是宣称所有可用结构均已穷尽。特别是历史 kernel 几何改善
和原 A 的精确 joint constraints 都强于第3节的 scalar 松弛。
本轮得到的是严格的新障碍、实际 high parity 估计及可行动前件，
没有得到新的 RH 比例或无零区域。

## 8. pending compression 稿的独立只读复核

绑定第1节 pending hash。§6(20) 的整数 progression 计数通过：
固定 q∤r，完整 q 周期由乘 r 置换非零 residues，harmonic 总量
O(log q)；残缺周期可由完整非零 residue harmonic majorize，必须保留
(P/q+1)。对固定 p 的远 q-spacing 尾为 O(log X/q)。中心 pr=qs
准确剔除；q|p 的零 residue 不引入新小分母。真实近核排序满足
Q≲P，故 +1 不会变成未付 P/Q 损失。dyadic summation 保留此项后
得到该稿的 near absolute budget，而非假设逐根平均的均匀 equidistribution。

positive nearcore 的 O(X) product bins、Cauchy X³/L⁴ tuple count，
六类重复 O(X²/L²)、fixed overlap length 与 Re K_d≥1/2 均通过。
它只下界受限配对正实子和 X/L⁵，不下界完整 signed physical norm；
剩余 bands 必须相消是诊断，不能删除内部 P 或推断 actual unbounded。

同日 high-parity 稿 §3 的 z=u−log p 变量代换和
Φ_H/d=Sψ+2||RE||HS²/d+o(1) 系数通过；§4 actual residual 与第4节
finite parity 相符。其 (21) 为 −(ζ'/ζ)'，原 Dirichlet 恒等式符号正确。
µ*log² 只是 factor-conditioned completion 候选，未支付原 masks 与 row 映射。
