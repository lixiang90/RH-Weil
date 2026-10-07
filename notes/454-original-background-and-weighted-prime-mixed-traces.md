# 454：原 Gamma/pole 背景与完整 Λ 压缩的实际混合迹

2026-10-07。新推导。独立全文审查限定通过，范围见
[radial 审查](../reviews/2026-10-07/hybrid-original-background-review-radial.md)。
没有新的零点比例或无零边界。本文在原 AF 有限矩阵中，直接支付
以下四个背景四阶量：

\[
 \frac{\operatorname{Tr}A^4}{N}\to V_\psi,\qquad
 \frac{\operatorname{Tr}A^3C}{N}\to0,\qquad
 \frac{\operatorname{Tr}A^2C^2}{N}\to Z_\psi,\qquad
 \frac{\operatorname{Tr}ACAC}{N}\to Z_\psi-\frac12J_\psi.
 \tag{1}
\]

C 是原 **完整 sharp Λ channel**，包括所有 proper prime powers；
A 是实际 Gamma/pole 压缩减 I。没有假设 Tr C⁴=O(N)。
真正仍未支付的背景四阶量是 Tr AC³。下文给它的准确 Cauchy 费用，
以及完整四矩的一侧条件桥梁，不冒称 prime fourth budget 已经完成。

## 1. 同一原矩阵、frame 和完整背景

令 X=T/(2π)、L=logX、d=⌊XL⌋、αₖ=T+2πk/L，
N=N(T,2T)∼TL/(2π)∼d。只用 d∼N。
固定 AF 偶正 profile ψ≤1 及其原 C² taper
φ(u)=χ(L/2+u)χ(L/2−u)√ψ(u/L)，support I=[−L/2,L/2]。
χ、ψ 在 T 前固定，a_L=||φ||₂²/L→a=∫ψ>0。

使用原 carrier isometry E eₖ=L^(−1/2)1_I exp(iαₖu)，
P=EE*、Q=1−P，F=𝓕 Mφ E（unitary Fourier）。
H 是原完整显式公式矩阵，分解为

\[
 H-I_d=A+C,\qquad
 C=\frac{2\pi}{a_LL}F^*M_{P_X}F,
 \quad P_X(t)=-\pi^{-1}\operatorname{Re}
              \sum_{n\le X}\Lambda(n)n^{-1/2+it}.
 \tag{2}
\]

A 含原 ν_X 中全部 Gamma 和 principal pole 项。
在物理空间，令

\[
 b_n=\frac{\Lambda(n)}{a_LL\sqrt n},\quad \ell_n=\log n,\quad
 B=-\sum_{2\le n\le X}b_n M_\phi(R_{\ell_n}+R_{-\ell_n})M_\phi.
 \tag{3}
\]

系数为零的 n 不贡献；仍用全部整数频率计算间距。
所有 translations 以原零延拓解释，C=E*BE。
不换成 prime-only symbol、bulk frame 或新 sampling。

原来源：[AF v2 §2、(2.3)–(2.4)、Lemma 2.2、(2.12)](https://arxiv.org/html/2608.13637v2)；
前置有限泄漏方法见
[原 high report §3](../reviews/2026-10-07/hybrid-high-prime-four-word-response-research.md)，
全 height Gamma/pole 压缩见
[446 接口 §5](../reviews/2026-10-07/hybrid-uniform-reciprocal-and-fourth-trace-interface.md)。
本稿新增的 full log-range alias 付款在第3节，不能用 high-only 的跨度<L/2
直接替代。以下只用明列经典 Chebyshev/Mertens/Hilbert 输入，
不依赖零自由包 [R] 或 RH。

令 h_L(u)=φ(u)²/a_L−1。它在圆周上为 C²，边界值均为 −1，
一、二阶 derivative L¹ 与 operator norm 统一有界。
实高度 J=[T/2,3T] 上
μ(t)=L/(2π)+O(1)，所以 Bessel 给 Gamma 的误差 Oop(1/L)。
J 外全部 μ(t)−L/(2π) 的 log weight 使用原二阶 Fourier 尾：

\[
 \sum_k\int_{J^c}
 |f_k(t)|^2\{\log(2+|t|)+L\}\,dt
 \ll dL/T^3,\qquad f_k=\widehat\phi(t-\alpha_k).
 \tag{4}
\]

除以 a_LL² 后为 O(T⁻²)。
原 |Π_X(t)|≤3√X/(1+|t|) 在 J 内付 O(√X/T)，
外侧保留 O(√X) 并用同一正压缩尾。
因此整个原背景准确满足

\[
 A=A_0+R_T,\qquad A_0=E^*M_{h_L}E,\qquad
 \|R_T\|_{\rm op}=O(1/L),\quad\|A\|_{\rm op}=O(1).
 \tag{5}
\]

低 height、负 height 和 pole 全保留在 (4) 中。
这不是预先丢掉 finite crossing 后替换背景。

## 2. 圆周 Fourier 只是原投影的计算工具

对 a_s(u)=φ(u)φ(u+s)，wrap 部分准确为零，
carrier 共轭后的 quasiperiodic rotation 与 P 交换。
normalized Fourier coefficients 满足

\[
 |\widehat a_s(j)|\ll\min(1,|j|^{-1},L|j|^{-2}),
 \qquad
 \|Q M_{a_s}P\|_{\rm HS}^2
 =\sum_j\min(d,|j|)|\widehat a_s(j)|^2
 \ll\log(2+L).
 \tag{6}
\]

不因 n≤√X 而改变这一证明。
Chebyshev/Mertens 给
Σb_n≪√X/L、Σb_n²=O(1)、||B||op≪√X/L。
Triangle 因而给

\[
 \|QBE\|_{\rm HS}^2\ll X\log(2+L)/L^2=o(d).
 \tag{7}
\]

对 h_L、h_L²、h_L³ 也有相同 O(log(2+L)) 的 multiplication 泄漏。
这些 periodic functions 的两端值/导数相接，integration by parts 合法。
带因子 a_s(u)(h_L(u)−h_L(u+s)) 的 shift 同样有统一 C²/L¹ derivative
费用，原零延拓不被周期平移替换。

## 3. 完整 log range 的加权物理二矩：全部 alias 实际付费

本节同时允许平移 coefficient

\[
 g_{\pm,n}(u)=a_{\pm\ell_n}(u)c_{\pm,n}(u),
 \quad |c_{\pm,n}(u)|\le C_0,
 \tag{8}
\]

其中 c 可以是 1 或 h_L(u)−h_L(u±ℓ_n)；
求二矩时系数仍来自同一个 physical operator。
pointwise bounds 不要求不同 n 的 c 相同。记

\[
 \mathcal B_g=-\sum_n b_n M_{g_{+,n}}R_{\ell_n}
                      -\sum_n b_n M_{g_{-,n}}R_{-\ell_n}.
 \tag{9}
\]

对这些真实 coefficients 和任何 bounded weight w，
原 finite-k norm 展开保留核

\[
 K_d(s)=d^{-1}\sum_{k=0}^{d-1}e^{i\alpha_ks}
 =e^{i[T+(d-1)\pi/L]s}
       \frac{\sin(d\pi s/L)}{d\sin(\pi s/L)}.
 \tag{10}
\]

### 3.1 同号差频率：Hilbert 主项与两端极点

把 numerator 展开为两个 endpoint exponent，
对于 −L<s<L、s≠0，有

\[
 \csc(\pi s/L)=\frac L{\pi s}+\mathcal R(s),\qquad
 |\mathcal R(s)|\ll
 \begin{cases}1,&|s|\le L/2,\\L/(L-|s|),&L/2<|s|<L.\end{cases}
 \tag{11}
\]

主项对**全部** n≠m 用原 bilinear Hilbert；
不能先截取 |s|≤L/2 后还免费调用它。
δ_n⁻¹≤2n 和 ΣΛ(n)²≪X L 给

\[
 \frac Ld\sum_n\frac{b_n^2}{\delta_n}\ll1/L.
 \tag{12}
\]

全部 carrier 相位进入 Hilbert coefficients，模不变。
小范围 remainder 费用 ≤d⁻¹(Σb_n)²=O(L⁻³)。
大差频率令 n>m，有 n>√X、m≤√X，且

\[
 L-\log(n/m)=\log(Xm/n)\ge\log m.
 \tag{13}
\]

只对此 remainder 作绝对求和，按 Λ(m)/logm≤1 和
Σ_(m≤√X)m⁻¹/²≪X¹/⁴，

\[
 \frac Ld\sum_{\substack{n>m\\\log(n/m)>L/2}}
 \frac{b_nb_m}{L-\log(n/m)}
 \ll X^{-1/4}L^{-2}=o(1).
 \tag{14}
\]

没有把接近 ±L 的原频率当成小差，也没有删除 carrier。

### 3.2 正负交叉和频率：原物理重叠消去 alias 奇点

与 high-only 情形不同，两个输出可有交集。
若 a_(ℓn)(u)a_(−ℓm)(u)≠0，则 u+ℓn、u−ℓm 同时在 I，
故 s=log(nm)≤L；其重叠长度至多 L−s。
s=L 时积分为零，包括 nm=X 的确切整数 alias。

在 s≤L/2 时，|K_d(s)|≪1/(X log4)。
由 Chebyshev 和 harmonic Λ bound，

\[
 \sum_{nm\le Y}\frac{\Lambda(n)\Lambda(m)}{\sqrt{nm}}
 \ll\sqrt Y\log(2Y).
 \tag{15}
\]

这使 s≤L/2 的全部交叉费用为 O(X⁻³/⁴/L)=o(1)。
在 L/2<s<L，ε=L−s，
|K_d(s)|≪min(1,1/(Xε))，
而 normalized physical overlap≤Cε/L，所以

\[
 |K_d(s)|\,L^{-1}\int|g_{+,n}g_{-,m}|\,du
 \ll1/(XL).
 \tag{16}
\]

(15) 取 Y=X，全部 near-alias 费用是 O(1/(√X L²))=o(1)。
这不是 triangle bound 对不存在的 full-support outputs 求和。
两种 opposite signs 都按同一账本支付。

### 3.3 真实 weighted 二矩结论

因此，取 (9) 的有限 frame norms 后，全部不同 frequency terms 为 o(d)，
只留下 n=m 的同号 diagonal：

\[
 \operatorname{Tr}(E^*\mathcal B_g^*M_w\mathcal B_gE)
 =d\left\langle
      w\sum_n b_n^2(|g_{+,n}|^2+|g_{-,n}|^2)
   \right\rangle+o(d).
 \tag{17}
\]

〈·〉=(1/L)∫_I·du；对负 w 以其绝对界付款，定义式本身保持有符号。
对本文全部固定 profiles，error 统一依赖其有限 norms。
取 g=a_s、w=1，得到 Tr(E*B²E)=O(d)、Tr C²=O(d)，
从而 Tr|C|=O(d)。未使用完整第四矩前件。

## 4. A²C² 与 commutator 的完整有限比较

令

\[
 d_L(u)=\sum_n b_n^2\phi(u)^2
            \{\phi(u+\ell_n)^2+\phi(u-\ell_n)^2\}.
 \tag{18}
\]

A0² 与 E*Mh²E 的差是正 leakage E*Mh Q MhE，迹 O(logL)。
在乘 C² 后，error 至多
||C||op² O(logL)=O(XlogL/L²)=o(d)。
对 Tr(C E*Mh²E C)，展开 BE=EC+QBE，其与真实
Tr(E*B Mh² B E) 的 difference 至多

\[
 2\|C\|_{\rm op}\|P M_{h_L^2}Q\|_{\rm HS}\|QBE\|_{\rm HS}
 +\|h_L\|_\infty^2\|QBE\|_{\rm HS}^2
 \ll X\log L/L^2=o(d).
 \tag{19}
\]

(17) 因而给 Tr A0² C²=d〈h_L²d_L〉+o(d)。
由 (5)，实际 A²−A0² 的 op 为 O(1/L)，乘 C² 的 trace error 为 O(d/L)。

对于 ACAC，不能对 Mh B Mh B 的 coupled endpoint coefficient
直接偷用 separable Hilbert。使用准确 commutator：

\[
 D=[M_{h_L},B]
 =-\sum_n b_n M_{a_{\ell_n}(h_L-h_L(\cdot+\ell_n))}R_{\ell_n}
   -\sum_n b_n M_{a_{-\ell_n}(h_L-h_L(\cdot-\ell_n))}R_{-\ell_n}.
 \tag{20}
\]

它的 (17) diagonal 是

\[
 j_L(u)=\sum_n b_n^2\phi(u)^2
 \sum_{\epsilon=\pm1}\phi(u+\epsilon\ell_n)^2
                \{h_L(u)-h_L(u+\epsilon\ell_n)\}^2.
 \tag{21}
\]

D 的真实 projection leakage 为 O(XlogL/L²)；
而

\[
 [A_0,C]-E^*DE
 =-E^*M_h QBE+E^*BQ M_hE
\]

的 HS norm≤2||B||op||QMhE||HS=O(√(XlogL)/L)=o(√d)。
(17)、(7) 保证其比较对象先有 O(√d) HS norm，所以 squared norm
差确为 o(d)，不循环使用待证的 commutator bound。
实际 [R_T,C] 的 HS≤2||R_T||op||C||HS=O(√d/L)。
所以

\[
 \|[A,C]\|_{\rm HS}^2=d\langle j_L\rangle+o(d).
 \tag{22}
\]

Hermitian 恒等式给

\[
 \operatorname{Tr}ACAC=\operatorname{Tr}A^2C^2
                     -\frac12\|[A,C]\|_{\rm HS}^2.
 \tag{23}
\]

以上已支付全部 finite projections，不从 physical trace 免费迁移 exact main。

## 5. A⁴ 与 A³C：真实单素数 alias 及全部高度

对固定 j≤4，bounded multiplication 的压缩幂与 whole multiplication
压缩之差迹范数为 O(logL)：展开 internal P+Q，每个额外项有一次
P→Q→P，两个 HS crossing 各为 O(√logL)，其余 h 因子 op 有界。
所以

\[
 \operatorname{Tr}A_0^4=d\langle h_L^4\rangle+O(\log L).
 \tag{24}
\]

A0³ 与 E*Mh³E 的 trace-norm difference O(logL) 乘 Cop 给
O(√XlogL/L)=o(d)；将 Tr(E*Mh³E C) 改成
Tr(E*Mh³ B E) 时，用 Mh³、B 的两 HS leakages 给相同 error。

后一真实 single-shift trace为
−dΣ_nb_nΣ_(±)K_d(±ℓ_n)〈h_L³a_(±ℓ_n)〉。
ℓ_n≤L/2 时核 O(1/X)，总费除以 d 为 O(1/(√X L))。
ℓ_n>L/2 时，真实 support overlap≤L−ℓ_n，
与 alias kernel 相乘至多 O(1/(XL))，
所以总费更小；ℓ_n=L 的 shift 积分恰为零。
因此 Tr A0³C=o(d)。
由 (5) 与 Tr|C|=O(d)，实际 A³C 的改动 O(d/L)；
A⁴ 的改动也为 O(d/L)。这证明 (1) 中纯背景与 single-prime 结论。

## 6. 明确 leading constants 与最后未付的背景协方差

令 h(v)=ψ(v)/a−1，延拓 ψ 为区间外零，

\[
 d_\psi(v)=\frac{\psi(v)}{a^2}
 \left\{\int_0^{1/2-v}r\psi(v+r)\,dr+
        \int_0^{1/2+v}r\psi(v-r)\,dr\right\}.
 \tag{25}
\]

标准 Mertens partial summation、taper 宽 O(1/L) 与 fixed-profile
uniform BV 给 (18)–(21) 的平均极限。
proper powers 的 Λ²/n 质量收敛，除以 L² 后趋零，但在有限矩阵中
始终保留；没有删除它们的 mixed words。
定义

\[
 V_\psi=\int_{-1/2}^{1/2}h(v)^4\,dv,\qquad
 Z_\psi=\int_{-1/2}^{1/2}h(v)^2d_\psi(v)\,dv,
 \tag{26}
\]

\[
 J_\psi=\frac1{a^2}\int_{-1/2}^{1/2}\psi(v)
 \sum_{\epsilon=\pm1}\int_0^{1/2-\epsilon v}
 r\psi(v+\epsilon r)
          \{h(v)-h(v+\epsilon r)\}^2\,dr\,dv .
 \tag{27}
\]

这些积分是严格定义，不用浮点小数代替。它们非负，且 Jψ≤4Zψ；
后一结论也由两 endpoints 对称换元与 (h−h')²≤2h²+2h'² 得到。
(24)–(27) 与 (19)、(22)、(23) 证明 (1)。

令 F_T=Tr C⁴/N≥0、Y_T=Tr AC³/N。非交换 cyclic expansion 准确给

\[
 \boxed{\frac{\operatorname{Tr}(H-I)^4}{N}
 =F_T+4Y_T+6Z_\psi-J_\psi+V_\psi+o(1).}
 \tag{28}
\]

这里 o(1) 不假设 F_T bounded；所有已替换的混合项仅用先证的二矩。
剩余 Y_T 保持实际 A，不把 (5) 的 small op error免费乘到未知 C³。
HS Cauchy 给

\[
 |Y_T|\le
 \sqrt{\frac{\operatorname{Tr}A^2C^2}{N}\,F_T}
 =\sqrt{(Z_\psi+o(1))F_T}.
 \tag{29}
\]

若未来独立证明 limsup F_T≤F<∞，则原完整中心四迹满足

\[
 \limsup\frac{\operatorname{Tr}(H-I)^4}{N}
 \le F+4\sqrt{Z_\psi F}+6Z_\psi-J_\psi+V_\psi.
 \tag{30}
\]

没有在证明 (1)、(28) 时使用这一未付 F 前件。
flat profile 的 h=0，V=Z=J=0，因此 (30) 的背景主费用为零；
这只在得到完整 finite F 后帮助传递，不提前删除 unknown prime mixed words。
MT 等非平窗必须保留全部显示积分和实际 Y_T。

## 7. 对完整目标的含义

本轮新增真实付款是：完整 Λ 的全 log-range weighted 二矩与 commutator，
原 Gamma/pole 的 static approximation，以及 (1) 的全部实际有限混合迹。
原背景的未知项被准确缩为 Y_T，prime fourth F_T 本身仍开放。
现有 low 一侧常数与 high repeated budget仍不能直接相加得到 F。
所有不同素数、high/low mixed 与 whole-cell/alias 算术仍须实际控制。

[452](452-subquarter-padding-and-fourth-trace-stability.md) 已提供同矩阵
H 到 G_P 的第四迹稳定性；有完整 F/Y 预算与正确二矩主常数后，
才能接原简单临界线 inertia/proportion chain。没有新的比例或无零边界，
本稿不触发“新边界正式论文”交付。

可复现的显示代数与两个有理 polynomial profile 积分见
[精确脚本](../scripts/hybrid_background_exact_audit.py)及
[输出](../output/hybrid-background-exact-audit.json)。它们只核非交换 cyclic
系数、commutator 恒等式和有限多项式积分；不认证本稿的 Hilbert、
projection、全高度尾或任何无限算术估计。
