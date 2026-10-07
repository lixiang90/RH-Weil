# 452：三次无零边界与原 Gabor 矩阵的四次迹截断稳定性

2026-10-07。状态：新推导待独立审查。此处没有新的无零边界，也没有新的临界线零点比例。

在已交付三次边界的明确引用前件 [R] 下，本文证明一个实际矩阵接口：
保持 AF 的原有限 frame、原 Λ 权重、完整 Gamma/pole 背景及双侧零点尾，
可以取比 T^(1/4) 更短的 padding

\[
 P=T^{6249/25000}=T^{0.24996}
\]

而完整中心四次迹的截断差为 o(N(T,2T))。这将已经证明的严格
σ*<7/8 用在零点侧到素数侧的四矩比较中。它不估计素数侧四矩主常数。

## 1. 输入、对象和量词

主边界采用 [三次反馈论文](../papers/kappa-feedback-cubic-boundary-paper.tex)
及其 [最终绑定清单](../reviews/2026-10-07/kappa-feedback-paper-build-manifest.json)：

\[
 \theta=\sigma_*=\frac{11}{12}-\frac{e_*}{4},
 \qquad 657e_*^3-954e_*^2+21e_*+20=0,
\]

其中

\[
 \frac{16683858898627}{10^{14}}<e_*<
 \frac{16683858898628}{10^{14}}.
 \tag{1}
\]

相对该稿明列底层 [R]，全部 ζ 非平凡零点满足 β≤θ；
函数方程反射同时给 1−θ≤β。这不是独立源整链或新增 kernel 认证。
对本接口，只需要 ζ 的这一全高度结论及原源的标准增长、显式公式，
不另假设 RH、pair correlation 或 prime four-point correlation。

固定 AF 的一个原 C² 光滑 taper φ=φ_L，令

\[
 L=\log(T/(2\pi)),\quad X=e^L,\quad
 \operatorname{supp}\phi\subset[-L/2,L/2],\quad
 0\le\phi\le1,\quad \|\phi''\|_1=O(1).
\]

使用 AF 原 window class 的统一 Fourier 尾与
a_L=||φ||₂²/L，要求 a_L 最终离零。
profile 的平滑参数在 T 前固定；不取一个导数常数未支付的 moving taper。
有限 grid 为

\[
 \alpha_k=T+\frac{2\pi k}{L},\quad 0\le k<D_T,\quad
 D_T=\lfloor XL\rfloor,\qquad N=N(T,2T)\asymp TL.
 \tag{2}
\]

只使用 D_T∼N，不使用 D_T=N+O(L) 的过强余项。
不同整数 rounding 只改变端点 O(1/L)，不改变下面统一估计。

设 I=[T,2T)，I_P=[T−P,2T+P)，1≤P≤T/2。
按同一原显式公式与 normalizer a_LL² 定义

\[
 H=\frac1{a_LL^2}\sum_{\rho\ {\rm all}}v_\rho v_\rho^t,\qquad
 G_P=\frac1{a_LL^2}\sum_{\operatorname{Im}\rho\in I_P}
                   v_\rho v_\rho^t,\qquad E_P=H-G_P.
 \tag{3}
\]

这里 vρ 的 k 坐标是原 \(\widehat\phi(\gamma_\rho-\alpha_k)\)，
γρ=(ρ−1/2)/i；在 (3) 中 Im ρ 是实高度，γρ 可以为复数。
全部零点计重数。上式保留复转置；不能擅自把 off-line summand 换成
positive rank one。实高度截止保留函数方程反射对，使三个总矩阵 Hermitian。
全部零点和以迹范数绝对收敛，以下估计也证明这点。

中心对象为

\[
 B=H-I_{D_T},\qquad B_P=G_P-I_{D_T}=B-E_P.
 \tag{4}
\]

它们是原有限矩阵，不另选 translation-invariant bulk 或 ghost 算子。
H 的原素数、Gamma 和 pole 项全部保留。

已付输入来源：

- [438 的一般 padding 推导及全高度零点尾](438-seven-eighths-and-zero-proportion-interfaces.md)
  和 [其完整源审计 §4–5](../reviews/2026-10-07/hybrid-proportion-source-audit.md)；
- [446 的原 sharp Λ 前缀与完整有限压缩](446-uniform-prime-twists-on-the-original-gabor-frame.md)
  和 [全高度范数接口 §2、4、5](../reviews/2026-10-07/hybrid-uniform-reciprocal-and-fourth-trace-interface.md)；
- [AF v2 的原 frame、显式公式及二矩](https://arxiv.org/html/2608.13637v2)。

外部通用解析输入仍为固定提交
[adc7f124 的原 paper.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
canonical LF SHA256 为
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
原 math 仓库只读。

## 2. 对任意固定 θ 的零点尾

令 d=θ−1/2，不与矩阵维数 D_T 混用。原二阶 Fourier 界给

\[
 |\widehat\phi(z)|\ll
 e^{(L/2)|\operatorname{Im}z|}
 \min(L,|z|^{-1},|z|^{-2}).
 \tag{5}
\]

β 的反射区间给 |Im γρ|≤d。若一个零点的实高度与 I 距离 R≥1，
对原半侧 grid 的平方尾求和得到

\[
 \sum_{0\le k<D_T}
 |\widehat\phi(\gamma_\rho-\alpha_k)|^2
 \ll T^d L R^{-3}.
 \tag{6}
\]

因为 ||v vᵗ||₁=||v||₂²，除以 a_LL² 后，单个 summand 的迹范数
至多 O(T^d L⁻¹R⁻³)。单位高度零点数 O(log(2+|t|))，所以 I_P
外的附近两尾总费 O(T^dP⁻²)；更远的完整两尾付
∫₃T^∞log t/t³ dt=O(L/T²)。P≤T/2 让它被前者吸收。故

\[
 \boxed{\ \|E_P\|_1\ll T^{\theta-1/2}P^{-2}\ }. \tag{7}
\]

常数依赖固定 profile 和 θ，不依赖 T 或 P。
同一原网格恒等式与内外端点账本给

\[
 |\operatorname{Tr}G_P-N(I)|\ll T^{\theta-1/2}L,\qquad
 |\operatorname{Tr}G_P-N(I_P)|
 \ll T^{\theta-1/2}L+PL.
 \tag{8}
\]

不把外侧 padding 零点当成所有外网格都与其分离；(8) 对其使用内 grid
的分离尾，距端点≤1 的 O(L) 个零点单独付费。这一细节沿用已经审核
的 438 完整账本。

## 3. 全部物理高度上的算子范数

在 T 前固定 θ<a<1。用无零半平面中与 Euler logarithm 相接的分支，
在实部距离 θ 为固定 a−θ 的 disks 上重放原 Borel–Carathéodory、
three-circles、Cauchy 证明。函数方程给固定 strip 内的多项式增长，
所以在所需 contour 上

\[
 |-\zeta'/\zeta(a+it)|\ll_a\log(2+|t|).
 \tag{9}
\]

principal pole 对 regularized ζ 支付；在固定 a<1 的直线上距 1
至少 1−a。在横向 joins 上须远离 pole，不能把 (9) 宣称为包括 s=1
的整个闭矩形界。因为 a−θ 固定，不使用 a−θ=1/log T 的未付常数。

保持 AF 的 sharp 前缀

\[
 Q_X(\tau)=\sum_{n\le X}\Lambda(n)n^{-1/2+i\tau}.
\]

取 x=⌊X⌋+1/2、Y=(2x(3+|τ|))⁴，原截断 Perron 将其移到
Re s=a−1/2>0，经过的唯一 pole 留数为
x^(1/2+iτ)/(1/2+iτ)。半整数端点及全 horizontal joins 的误差已由
446 §4 支付；左线的 1/s 只付 log Y。于是

\[
 Q_X(\tau)=\frac{x^{1/2+i\tau}}{1/2+i\tau}
 +O_a\!\left(X^{a-1/2}\log^2(2X(3+|\tau|))\right).
 \tag{10}
\]

此处没有一般系数 a(n)，也没有 smooth cutoff 替换。
J=[T/2,3T] 上 principal 项为 O(√X/T)。
令 (Uz)(τ)=Σₖzₖ \(\widehat\phi(\tau-\alpha_k)\)，其原 Bessel 界为
||Uz||₂²≤2πL||z||₂²。在 J 上压缩原
P_X(τ)=−π⁻¹Re Q_X(τ) 后得

\[
 \|V_J\|_{\rm op}\ll_a T^{a-1/2}\log T.
 \tag{11}
\]

在 J 外不能把 principal 主项删除。保留全高度
|P_X(τ)|≪√X，并使用 αₖ 到 J 外距离≥T/2 及真实 Fourier 尾：

\[
 \operatorname{Tr}(U^*\mathbf1_{J^c}U)
 \ll D_TT^{-3}\ll L/T^2,\qquad
 \|V_{J^c}\|_{\rm op}\ll\frac{\sqrt X}{LT^2}.
 \tag{12}
\]

Gamma 项在 J 上为 O(L)，在 J 外的 log(2+|τ|) 权重用同一正压缩
迹尾完整积分。pole 压缩在 J 内付 √X/T、外侧付 √X。这给原背景
A 的 ||A||op=O(1)，并在同一有限矩阵上保持
H=I+A+V。因此

\[
 \boxed{\ \|B\|_{\rm op}\ll_a
                1+T^{a-1/2}\log T\ }. \tag{13}
\]

(13) 是完整 H 的范数，证明不使用新的 padding 或任何四矩前件。
不能把绝对高度 τ 的局部化误用于四词中各个高度差。

## 4. 非交换四次迹比较

对任意有限矩阵 A₀,B₀，准确的 telescoping 恒等式为

\[
 A_0^4-B_0^4
 =A_0^3(A_0-B_0)+A_0^2(A_0-B_0)B_0
  +A_0(A_0-B_0)B_0^2+(A_0-B_0)B_0^3.
 \tag{14}
\]

各因子的顺序不能改成 scalar binomial expansion。
取 A₀=B_P、B₀=B、A₀−B₀=−E_P，trace ideal 不等式逐项给

\[
 \boxed{
 |\operatorname{Tr}B_P^4-\operatorname{Tr}B^4|
 \le4\|E_P\|_1(\|B\|_{\rm op}+\|E_P\|_{\rm op})^3.}
 \tag{15}
\]

若 P=T^r，且 θ−1/2−2r<0，则 ||E_P||op≤||E_P||₁=o(1)。
把 (7)、(13) 代入 (15)，除以 N≍TL，得到

\[
 \boxed{
 \frac{|\operatorname{Tr}B_P^4-\operatorname{Tr}B^4|}{N}
 \ll_a T^{\theta+3a-3-2r}\log^2 T.}
 \tag{16}
\]

这里没有先假设 ||B||₄=O(N^(1/4))，没有借用待证的第四矩常数；
使用的仅是已经付清的、虽弱但足够支付截断的 pointwise op bound。
Hermitian 性使两边的四次迹非负；(15) 的非交换证明本身更一般。

固定 θ>3/4 的本研究范围，在保持小迹范数尾与 PL=o(N) 时，
这一路证明给四次迹稳定性的充分范围

\[
 \max\left(2\theta-\frac32,\frac\theta2-\frac14\right)<r<1.
 \tag{17}
\]

具体地，先选这样的 r，再选固定 θ<a<min(1,(3+2r−θ)/3)。
第二个 r 门槛专门保证 θ−1/2−2r<0；不能仅从 θ>3/4 与第一个
门槛推出小迹范数尾。θ>5/6 时第一个门槛较强，所以当前 θ=σ*
的范围化为 r>2σ*−3/2。此处先固定 r、a，再令 T→∞；
(17) 是本组输入的充分门槛，不是所有方法的必要性结论。

## 5. 三次边界给出的严格 subquarter 实例

由 (1) 的有理隔离可直接得

\[
 \theta<\frac{437479}{500000}=0.874958.
 \tag{18}
\]

取两个固定有理参数

\[
 a=\frac{87497}{100000}=0.87497,\qquad
 r=\frac{6249}{25000}=0.24996.
 \tag{19}
\]

它们满足 θ<a<1、1≤P≤T/2（充分大 T），且

\[
 \begin{aligned}
 \theta-\frac12-2r
 &<-\frac{62481}{500000}=-0.124962,\\
 \theta+3a-3-2r
 &<-\frac{13}{250000}=-0.000052.
 \end{aligned}
 \tag{20}
\]

所以同一个有限矩阵的 tail 与 fourth transfer 分别为

\[
 \|E_P\|_1=O(T^{-62481/500000}),\qquad
 \frac{|\operatorname{Tr}(G_P-I)^4-
             \operatorname{Tr}(H-I)^4|}{N}
 =O_a(T^{-13/250000}\log^2T)
 =O_a(T^{-13/500000}).
 \tag{21}
\]

最后一步只在充分大 T 吸收日志；常数因很小但固定的 a−θ 而可能很大，
不据此声称可计算有效高度或某个有限 T 的数值比例。

仍用 P=T^(1/4) 时，(18)–(19) 还给
T^(−33/250000)log²T 的归一化四迹差。若只使用 θ=7/8，
同一路 (16) 对任何固定 a>θ 与 r=1/4 给正指数，
因而不能证明 o(N)；它允许任意固定 r>1/4。
此比较限定于这条已经支付的 op/trace-tail 证明，不否定其他技术
在 θ=7/8 下处理 r=1/4 的可能性。

(17) 在 θ=σ* 的参考下限为

\[
 2\sigma_*-\frac32
 =0.249914038840197892\ldots.
 \tag{22}
\]

只声称每个严格大于该值的固定 r；不把端点或 moving a 当成已证。

## 6. 首迹、二矩与比例接口的完整含义

(8) 在 (19) 下仍给
Tr G_P=N(I_P)+o(N)、N(I_P)=N+o(N)。
原完整 H 的 AF 二矩 ||H||HS²=O(N) 与 (7) 给
||G_P||HS²=O(N)；无需用 G_P 的二矩反证自身。
进一步，非交换二次迹差至多

\[
 2\|E_P\|_1\|H\|_{\rm op}+\|E_P\|_1^2=o(N).
 \tag{23}
\]

所以原 finite carrier、首迹/二矩归一化和零点惯性仍然可用。

若未来在**同一实际 H** 上证明

\[
 \operatorname{Tr}(H-I)^4\le B_4N+o(N)
 \tag{24}
\]

且付清所需二矩主常数、原 background/centering 与原简单临界线
inertia 账本，(21) 就把 (24) 以相同 B₄ 传到 G_P。
这一步现在不再要求另加一个未支付的 fourth-norm boundedness 前提。
四矩证书所需的实际 prime correlations、全 distinct four-word response
及所有 background mixed terms仍未由 (21) 估计。

当前只能保留原 AF 已付比例常数，不能宣布比例增加：
截断差是 o(N)，不是对素数侧 B₄ 主预算的固定正改进。
本接口也不把原 AF 的 fixed ζ 二矩自动推广为 moving q 的一致矩阵定理。
对已审核的 prime-power/low-prime 删除，仍需其各自真实 Schatten 误差
与 mixed-term 预算，不能仅因本尾部稳定性而删除任何算术项。

## 7. 本轮进展与后续任务

新增并付清的是原零点矩阵与原显式公式矩阵之间的四次迹截断，
以及在已证三次无零边界下的严格 subquarter padding 实例。
可复现的 [精确脚本](../scripts/hybrid_fourth_tail_exact_audit.py) 与
[输出](../output/hybrid-fourth-tail-exact-audit.json) 检查有理隔离、固定参数
指数及自由非交换字的 (14) 恒等式；它们不认证分析或 prime moments。
下一项实际工作仍是原有限 H 的 signed 四矩常数，或临界 count 的新不等式。
此结果未达到用户所说的“新的无零边界”，因此不据此再写一篇边界论文。
如果以后确认新的无零区域或零点比例，将独立写正式论文并完整审核。
