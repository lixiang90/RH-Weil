# KRY1999 的实际循环与 relative primitive 源门

2026-10-23；独立分支，供 root 消费，不更改 STATE／cadence。实际输入为 root 指定的二维实 Gaussian dilation 源，和 KRY1999 同一原件的 §1、Lemma 2.1(ii)、§5–6。下述直接计算不读取 Q 或未知零点作标签。

## 1. 原件的循环类型，及本门不冒用的恒等式

唯一外部原件：[Kudla–Rapoport–Yang, *On the derivative of an Eisenstein series of weight one*](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/tinynew.pdf)。本文需要的来源事实限定为：原件 Proposition 5.1 的 CM stack 有限 étale 于 Spec O_k；Theorem 3 识别有效有限循环的算术次数；§6 (6.8)、(6.16) 将有限项与负指标 arch 项放在 Arakelov divisor 群中；Lemma 2.1(ii) 固定 weight 1 Gaussian。原件 §1 的 Schwartz→section 是 (ω(g)φ)(0)。

因此底空间的 generic dimension 是 0；Spec O_H 的 divisor 次数是线性量。这些事实没有给出 C×C 上 primitive divisor 自交的 Hodge 负号，也没有给出一个可直接与 Weil Hermitian 型等同的二次配对。§6 的 Arakelov divisor／principal 商不是已构造的双边界 relative primitive 配对。

另一个必须保留的区别：λ 在 s=0 的 Weil 等变性，不能独自识别 standard s-extension 的导数与任意右平移 E′；若采用 raw dilation，标准延拓／导数项须另核。本稿不使用这种未核互换。第 4 节只使用投影回原件已证 native weight 1 线后的严格标量恒等式。

## 2. Raw Gaussian map：实际正范数有界，但不消全主关系

固定 Lebesgue dx 在 R²，Q(x)=|x|²，φ_u(x)=e^{u/2}exp(−πe^u|x|²)。物理源 r∈S_exp,C；先可取 compact smooth，再以绝对估计延拓：

\[
 (Tr)(x)=\int_{\mathbb R}r(u)\phi_u(x)\,du.                 \tag{1}
\]

每个 Schwartz 半范数由 S_exp 的带权绝对半范数控制；故 (1) 真正进入 Schwartz 空间。直接二维 Gaussian 积分给

\[
 \langle\phi_u,\phi_v\rangle_{L^2(dx)}
 =\frac{e^{(u+v)/2}}{e^u+e^v}
 =\frac1{2\cosh((u-v)/2)}=:k(u-v).                         \tag{2}
\]

以 Fourier 约定 e^{−itu}，\widehat k(t)=π sech(πt)，于是

\[
 \|Tr\|_{L^2(dx)}^2
 =\frac1{2\pi}\int_{\mathbb R}\pi\,\operatorname{sech}(\pi t)
                   |\widehat r(t)|^2dt
 \le\pi\|r\|_{du}^2.                                     \tag{3}
\]

这个全线原 du 上界也受原 Hlog／zero-extension Dlog 范数控制，无需成长窗费用。但乘子处处正，T 注入；任何非零 405 physical Pan 都有非零 raw 像。它不能同时被当成已消主关系的正能量模型。衰减的 multiplier 不是完整 Γ 的 log|t| 高频费用。

λ 也不能靠只在 identity 的评价免费修复。对 arch w n(b)，Gaussian Fourier 积分给

\[
 \lambda_\infty(\phi_u)(w n(b))
   =c_\infty\frac{e^{u/2}}{e^u-2ib},                       \tag{4}
\]

其中 c∞ 是固定非零 Weil 相位（若 Q 的 additive normalization 改变，2 随之改，注入性不变）。若 λ∞Tr 为零，则右端对所有实 b 的积分为零。令 t=e^u，其为密度 r(log t)t^{−1/2}dt 的 Cauchy transform；解析唯一性与边界恢复给 r=0。因而 λ 在这个 radial 源像上同样注入。仅 b=0 或 g=1 的双 pole 矩消失，不能代替全 λ 像消失。

## 3. Native weight 1 投影：费用精确，却同时出现 relation／nonroot 反测

先在第 2 节明确固定的 raw Lebesgue 模型中令 φ₀(x)=exp(−π|x|²)，其平方范数为 1/2。投影到该 Gaussian 线：

\[
 P_1Tr=c(r)\phi_0,\qquad
 c(r)=\int_{\mathbb R}r(u)\operatorname{sech}(u/2)du.       \tag{5}
\]

这来自 \langleφ_u,φ₀\rangle=1/[2cosh(u/2)]，不是按 Q 定义的读出。记 s(u)=sech(u/2)，有

\[
 \|c\|_{(L^2(du))^*}^2=4,
 \quad\|c\|_{L^2(-L,L)^*}^2=4\tanh(L/2),
 \quad\|P_1Tr\|^2=|c(r)|^2/2\le2\|r\|_{du}^2.             \tag{6}
\]

与原件的规范对齐须另行明确：固定 φ* 为 KRY Lemma 2.1(ii) 在其实际 Q／ψ／Haar 规范下的 weight 1 Gaussian，记 ν=||φ*||²>0；不凭 OCR 的 Gaussian 宽度将 ν 擅设为 1/2。以二维 unitary dilation D_uφ*(x)=e^{u/2}φ*(e^{u/2}x) 定义 aligned T*r=∫r(u)D_uφ*du。直接 Gaussian 积分给其 Gram=ν sech((u−v)/2)，故 ||T*r||²≤2πν||r||²；Gaussian 线投影仍为 P₁T*r=c(r)φ*，且 ||P₁T*r||²≤4ν||r||²。系数 (5) 与下述关系／非根检验完全不变。第 2 节 ν=1/2 的 raw 模型公式保持为其已声明规范下的正确结果；不未经说明把它认作原件 native 宽度。

没有 jet 或 hidden normalization 费用，原 Dlog 可由 du 付这些上界。结论没有说一个 primitive height 也已被此范数支付。

恢复 [405](../../../notes/405-f1-adelic-restriction-moments-and-radical.md) 的真实 h=Eη>0，H(u)=e^{u/2}h(u)>0，H∈S_exp，physical Pan

\[
 p=(D^2-1/4)H\ne0.                                      \tag{7}
\]

两 pole 矩为零，所有平移仍为真实关系。由于 s″−s/4=−s³/2，合法分部积分精确给

\[
 c(p)=-\frac12\int_{\mathbb R}H(u)\operatorname{sech}^3(u/2)du<0. \tag{8}
\]

对任意 H 的平移同式仍严格负；physical 平移的正标量因子不改变结果。故该 native map 在未进入容量之前，已不消 405 全关系。此处不是 compact 域近似，更不是只检双 pole 矩。

另一方面，(5) 还漏掉实际 537 非根。令 I=(−17/16,17/16)，取两个不交支撑的非零非负 ψ₁,ψ₂∈C_c∞(I)，令

\[
 a=\frac{\int\psi_1s^3}{\int\psi_2s^3}>0,\quad
 \psi=\psi_1-a\psi_2,\quad r_*=(D^2-1/4)\psi.              \tag{9}
\]

r* 非零、compact、两 pole 矩为零，且 c(r*)=0。[537](../../../notes/537-source-exact-weil-window-positive-tail-admission.md) 给完整经典型 Qζ(r*)≥τ||r*||²>0，τ=2⁻⁴⁹¹⁶²；所以 r* 不是 radical，却被 (5) 杀掉。若只取单个正 ψ，则 c((D²−1/4)ψ)<0；不能误报为所有 537 非根都被杀。失败是实际完整源像的覆盖，而非某个选定正源值为零。

## 4. 真有限循环接入及 fixed relative primitive 不可免费修复

固定 q=7，原件 native finite Schwartz 不动。此处使用第 3 节 aligned T* 及 P₁T*r=c(r)φ*，严格回到原件实际 weight 1 Gaussian。对每个正 n，native 全 Eisenstein derivative 由其线性地变成 c(r) 倍原函数；其实际有限循环 map 是

\[
 r\longmapsto c(r)Z(n)\quad\text{in }\operatorname{Div}_{\mathbb C}(M). \tag{10}
\]

这里使用实／复系数循环延拓。一般 c(r) 非整数，(10) 不自动给整系数线丛，整性／有费 approximation 是额外责任。n=1 时原件公式直接给 deg Z(1)=2 log7>0。因此 c(p)Z(1) 的 degree 非零；不能是 principal Arakelov divisor。这个实物测试不依赖未知循环类群或假设 height 正号。

任何 fixed linear relative／degree-zero／primitive operation Π 作用于同一 family，仍给

\[
 \Phi(r)=c(r)\Pi Z(1).                                   \tag{11}
\]

若 ΠZ(1)≠0，则 Φ(p)≠0，405 不消；若 ΠZ(1)=0，整个 family 为零，也杀所有 537 非根。这覆盖 fixed degree correction Z(1)−deg Z(1)A，其中 A 是任一固定 degree 1 reference，及 fixed 两边界投影。更一般地，若整个 coefficientwise native family c(r){Z(n),arch,constant} 统一作固定线性操作，同样是 rank 1，结论相同。

若先任意商掉 Φ(p) 的一维像，结果也是全零。这不是一个可保 537 的相对 primitive 构造。反之，源依赖 frame、非 Gaussian K-types、变化的有限 Schwartz、非局部非标量 relative boundary、强拓扑或有费无限完成，并不都因 (11) 被排；它们必须先给出不再经 c(r) 因子的实际公式及同对象主同构。

即使额外放入一个正 Hermitian 配对 H，(11) 至多给 H(ΠZ,ΠZ)c(r)\overline{c(s)}。它仍违反 (8)／(9)，不能等同完整 Weil 型。这里失败早于 signed 解卷积及 RR；不能用未知平方容量补救一个已错的 source map。

## 5. 全预算、函数域及 continuous 对照

native 投影的严格标量身份保留原件全式：正 n 的 finite local length；负 n 的 β₁ Green／arch 项；constant 的 log v 与 Faltings-height 项；全 Mellin 中 Λ₀Λχ[log q+Λχ′/Λχ−Λ₀′/Λ₀]。不删 Γ、不删任何 prime powers、不删两 pole 或 contact。完整 identity 的原件归属不升级为新的 primitive Hermitian identity。

raw map (1) 的正范数只来自二维 Gaussian，和 g-distribution 无关。[562/578] continuous 正反族若都送入这个额外 Gaussian Hilbert 空间，就都具有 (3) 的正范数；这不能识别它们 native 完整 Weil 型的相反符号。未构造 continuous→CM cycle 运输，所以不声称负例已满足或反驳 KRY 算术几何；它否定的是“这个外加正能量无需另一个 identity 就等于 native Weil 型”。

真实函数域 [567](../../../notes/567-function-field-positivity-origins-and-generalized-correspondence-tests.md) 在 C×C 保留全 Frobenius 图、双 degree 扣除、同对象 mixed 交数及全部 returns／aliases，RR／Hodge 或 Jacobian 的 Rosati 独立给符号。将所有源压到一个 fixed Gaussian／fixed CM divisor coefficient，不携带这条 mixed 信息。KRY 的 generic-dim-0 arithmetic curve 不能被改称该 surface，再套 primitive 自交负号。真正 higher-dimensional／relative family 尚需独立构造；本稿不以 dimension 错位断言所有算术 theta 都不可能。

## 6. 消费记录与精确停止

对象：S_exp,C 的 physical r→二维 Schwartz→native Gaussian coefficient→实际 KRY real/complex cycles。关系是 (7) 及其全部平移；非根是 (9) 的 actual 537 源；原 du／zero-extension Dlog 费用为 (3)、(6)，不是 unknown height 费。全部计算无截断误差，L 仅在 (6) 固定窗 bound 出现；未获成长 Weil 后果。

独立已付输入：405 的实际源及 H>0、537 的全 complex 固定窗型、KRY native Gaussian 与实际 finite cycles。新展示的是这一个 concrete 接入 recipe 的 exact 反测，不是经典 signed 容量。它也没有付 Λ₀Λχ 的有符号逆、相对 principal 的算术 lift 或同对象二次 RR。

相对于更强旧输入 552／553：全线 bounded positive-energy 读出消全部 Pan 必为零已是旧障碍，本稿没有改善宏观后果。这里在原件 native 线直接定位错误，费用和反测都是可算的；不将其冒称新 RH 正性，数学轮计数由 root 比较后决定。strong-old 542+555→557 whole 4/5 负惯性上预算、core／coupling／Ξ和独立容量瓶颈均未改变。

停止此 fixed finite Schwartz、native weight 1 scalar 接入及其 fixed relative projection。下一仅在有实际非标量 source formula、405 principal 同构和 537 非零比较，或源像专用 signed 解卷积 identity／原费用时重准入。不以 Pi、primitive、height 新名称代替这三份交件。
