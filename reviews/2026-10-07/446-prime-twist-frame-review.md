# 446 独立审查：原 sharp prime channel 与实际有限 Gabor 四迹

日期：2026-10-07。审查人：radial_review（非主稿及输入推导报告作者）。
结论：**限定 PASS [T/R]**。全文独立核验 446，包括原 sharp Perron、absolute-height 压缩、whole outer tail、Hermitian 配对、二矩接口、短窗及 additive transfer。未发现阻断本稿所声明弱界的错误。

本稿得到的是随 T 增长的实际四次迹上界，不是固定常数的 MOM-1 预算、比例改进或 RH 证明。原全族无零输入和 AF 二矩/zero tail 作为准确 [R] 保留；此次未重新证明这些原论文整体或运行其形式化工程。

## 1. 绑定与输入范围

主稿 notes/446-uniform-prime-twists-on-the-original-gabor-frame.md：
canonical LF SHA256 08060477a6ea806d559fd67533d9e6d3b96483a755842cca9a048b6ab5e110cf，
9890 字节。

OpenAI 原源：
E:\codex-build\math\preprints\The-Quasi-Riemann-Hypothesis-September-30-2026\build\paper.tex；
固定提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a，
canonical LF SHA256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3，
766316 字节。所读准确接口为 logarithmic-control 1531–1600、deleted Euler factors 1602–1645，以及全族 7/8 结论。

另直接读取 [Alpöge–Furman arXiv:2608.13637v2](https://arxiv.org/html/2608.13637v2)，核对 §§2.1–2.3、Propositions 4.2–4.3、Theorem 5.7 及相关原窗口定义。2026-10-07 只读请求官方 UTF-8 HTML 后，在内存将 CRLF→LF；该 HTML 响应 SHA256 为
5ba990d3cf959a118fd866be276b9d129ef7e0365b8c21428379c947da0333c9，
827188 字节。此哈希绑定所读 HTML，不冒称 AF 的 tex、PDF 或 Lean 源码哈希；没有保存或修改外部文件。

只读本地输入：

- notes/197-partial-weil-proportions-regions-four-moments.md：98bd8ea89679030e0ffb8135d324b5654900f260b3f45c9ae816d5ea870eaae7；
- notes/198-quadratic-fourth-moment-vaughan-channel.md：d7d2d9a20e9c6437b55bb23e8494f2a969b1b1ba46d63b70fadd7d42de904e66。

具体 [R] 为全族 7/8 无零性、统一 functional-equation strip growth、原 coefficient-generating functions、AF 的原显式公式和固定矩阵的 trace/second moment/zero tail。Dirichlet 的统一 logarithmic-control 需 degree-one strip growth；它不是仅从一个固定角色的无零性推出统一常数。下文核对的 Perron、压缩及谱不等式是这些输入之后的独立推导。

## 2. 统一规范块与 principal 例外

446 §2 的 fixed-gap 使用正确。先固定 \(0<\delta<1-\theta\)、\(a=\theta+\delta<1\)，再取 conductor、长度及 twist。原 Euler logarithm、uniform strip growth、Borel–Carathéodory、three-circles 和 Cauchy 的所有 disk gaps 均固定；因此全导子和全高度的常数可只依赖这些固定 gaps。

principal 的 \(L\) 上界和 log derivative 必须先作用于 regularized function。固定直线 \(\Re s=a<1\) 与极点的距离至少 \(1-a>0\)，所以恢复原 log derivative 只增加固定常数；不能把该恢复误用为穿过 \(s=1\) 的全半平面有界性。主稿随后显式取 principal 留数，处理正确。

natural imprimitive deletion 的 radical 必须与 primitive conductor 合记为 \(Q_{\rm eff}\)。source deleted-Euler-factor lemma 同时支付 inverse 的任意小幂和 log derivative 的 \(O(\log NR)\)。一般 \(Q_{\rm eff}\) 不能被静默吸收到 \(T^\epsilon\)；主稿保留了这一限制。

两种 Mellin 生成函数分别必须恰为 \(1/L_{\rm orig}\) 与 \(-L'_{\rm orig}/L_{\rm orig}\)。在固定 annulus 上，smooth transform 的任意阶衰减支付全部移线和 horizontal joins；norm twist 只是 \(s\mapsto s-i\tau\)。\(\Lambda\) 块的 principal residue 为
\(N^{1/2}\mathcal MW(1+i\tau)\)；它在 \(\tau\) 近零不能删除。任意 bounded coefficients 或 row-dependent response 不具有这些 generating functions，不获本节准入。

## 3. Sharp uniform Perron 的完整重算

446 §3 通过。这里保留的系数始终是
\(\Lambda(n)n^{-1/2+i\tau}\)，而不是新的 smooth model。

取 \(x=\lfloor X\rfloor+1/2\)。原 sharp sum 恰等于 \(n<x\) 的 sum，不存在整数 endpoint 原子。令
\[
 c=1/2+1/\log x,\qquad Y=(2x(3+|\tau|))^4.
\]
truncated Perron 的 absolute remainder 为
\[
 \sum_n\frac{\Lambda(n)}{\sqrt n}(x/n)^c
 \min\left(1,\frac1{Y|\log(x/n)|}\right).
\]
在 \(x/2<n<2x\)，用 \(|x-n|\ge1/2\)、
\(|\log(x/n)|\asymp |x-n|/x\) 和 \(\Lambda(n)\le\log n\)，harmonic sum 给
\(O(\sqrt x\log^2(2x)/Y)\)；余区用 \(\Re(s+1/2)=1+1/\log x\) 上绝对 Euler series 得同一或更小 bound。这一步对 \(\tau\) 一致，因为系数模与 twist 无关。

移至 \(\Re s=a-1/2>0\)。\(s=0\) 始终在左边，唯一跨越的 pole 是 \(s=1/2+i\tau\)。其实际 residue 是
\[
 x^{1/2+i\tau}/(1/2+i\tau).
\]
\(Y>|\tau|+2\) 使 horizontal joins 离该 pole；那里 fixed-gap logarithmic-control 与 principal regularizer 的恢复均合法。joins 只花
\(O(\sqrt x\log(2x(3+|\tau|))/Y)\)；
左线的 \(\int|s|^{-1}dt\) 花 \(O_\delta(\log Y)\)，从而得到主稿 (4) 的
\[
 O_\delta\!\left(X^{a-1/2}\log^2(2X(3+|\tau|))\right).
\]
若把 residue 中 \(x\) 换为 \(X\)，其 derivative modulus 为 \(x^{-1/2}\)，所以误差仍是 uniformly \(O(X^{-1/2})\)，不额外花 \(|\tau|\)。

高高度区 \(T/2\le\tau\le3T\) 的 principal 项为 \(O(\sqrt X/T)\)。低高度仍保留 \(O(\sqrt X)\) 的绝对 bound。该 \(\tau\) 是 AF 原 integral 的 absolute height；不是 four-cycle 的变量差。

## 4. 原 frame、Bessel 及 whole outer tail

446 §4 通过；以下计算保留原 finite column set。

令 \(U z=\sum_{0\le k<d}z_k\widehat\phi(\tau-\alpha_k)\)。
原 \(\phi\) 的 support 长度为 \(L\)、\(|\phi|\le1\)，grid spacing 为 \(2\pi/L\)。Plancherel 直接给
\[
 \|Uz\|_2^2
 =2\pi\int|\phi(u)|^2
 \left|\sum_k z_ke^{i\alpha_ku}\right|^2du
 \le2\pi L\sum_k|z_k|^2.
\]
最后一步用整个长度 \(L\) 区间上的真正 exponential orthogonality；未假定 modulated tapers 自身互相正交，也不需额外 frame lower bound。

AF 原 prime multiplier 的 compression 正是
\((a_LL^2)^{-1}U^*M_{P_X}U\)。在 \(J=[T/2,3T]\) 使用 sharp Perron 后得到主稿 (6)；这个 operator bound 不把某个 cycle 差误认成高 absolute height。

对 \(J^c\)，每个实际 \(\alpha_k\in[T,2T)\) 至少距离 \(T/2\)。固定二阶 Fourier tail 给
\[
 \sum_k\int_{J^c}|\widehat\phi(\tau-\alpha_k)|^2d\tau
 \ll dT^{-3}\ll L/T^2.
\]
这是整块 positive compression 的 trace，故同时支配其 operator norm。即使 \(P_X\) 有符号，也有 quadratic-form estimate
\[
 |\langle z,U^*1_{J^c}M_{P_X}Uz\rangle|
 \le\sup|P_X|\langle z,U^*1_{J^c}Uz\rangle.
\]
用全高度 absolute \(|P_X|\ll\sqrt X\) 除以 \(a_LL^2\)，得到主稿的
\(\sqrt X/(LT^2)\) outer cost。低绝对高度 principal 未被丢掉。

gamma density 在 \(J\) 为 \(O(L)\)。在 \(J^c\) 加入 \(\log(2+|\tau|)\) 后，单列尾积分仍为 \(O(T^{-3}\log T)\)；因此其 compression 有界。pole multiplier 在 \(J\) 为 \(O(\sqrt X/T)\)，外部用完整 \(O(\sqrt X)\) 和同一 tail。故实际背景 compression 减去 \(I_d\) 的 op 为 \(O(1)\)，无需改造为另一 bulk 或 Toeplitz 模型来证明此弱界。

## 5. Hermitian 是实际配对的结论

446 §5 的谱步骤成立，但必须使用以下真正理由，而不是仅说每项 transpose 对称。

AF 的 finite zero set 按 \(\Re\gamma_\rho\) 属于 padded interval \(I'\) 截取。\(\rho\mapsto1-\bar\rho\) 保持这一 real ordinate 和 multiplicity，故有限集合反射封闭。real even \(\phi\) 使
\(v_{1-\bar\rho}=\bar v_\rho\)。
若 \(v_\rho=x+iy\)，一个完整 off-line pair 贡献
\[
 m(v_\rho v_\rho^{\mathsf T}+
 \bar v_\rho\bar v_\rho^{\mathsf T})
 =2m(xx^{\mathsf T}-yy^{\mathsf T}),
\]
是真实 real symmetric、因而 Hermitian。on-line 零的 \(v_\rho\) 为 real，贡献同样 Hermitian。若只保留其中一个 off-line partner，这个论证失败；主稿没有这样截取。

AF 外部 zero set 也由相同 real-ordinate cutoff 给出且反射封闭。原 zero-tail [R] 提供绝对 trace-norm 可求和，故可以成对 regroup；\(E\) 也是 Hermitian，不仅是 complex symmetric。同时
\(\|E\|_{\rm op}\le\|E\|_1=o(1)\)。
原 real multiplier integral 本身也给 Hermitian \(G+E\)。因此 \(G-I_d\) 的实谱界可用。

需记录一个源文本层面的不准确措辞：AF v2 §2.2 写出 \(d=N(T,2T)+O(L)\)，但它自己的 Riemann–von Mangoldt 式与
\(d=\lfloor LT/(2\pi)\rfloor\)
实际给
\[
 N(T,2T)-d
 =\frac{2\log2-1}{2\pi}T+O(\log T).
\]
正确是 \(d=N+O(T)\)，从而 \(d\sim N\)。446 只用这个正确弱关系，没有继承过强 \(O(L)\)；所需 \(\|G-I_d\|_{\rm HS}^2=O(N)\) 完全不受影响。

确切 AF trace 和二矩输入给
\[
 \operatorname{Tr}G=N+o(N),\qquad
 \operatorname{Tr}G^2=O(N),\qquad d=O(N).
\]
因此
\(\|G-I_d\|_{\rm HS}^2=\operatorname{Tr}G^2-2\operatorname{Tr}G+d=O(N)\)。
与实际 op bound 合并，在 real eigenvalues 上使用
\(\lambda^4\le\|G-I_d\|_{\rm op}^2\lambda^2\)，得到
\[
 N^{-1}\operatorname{Tr}(G-I_d)^4
 \ll_\delta T^{3/4+2\delta}\log^2T
 \ll_\epsilon T^{3/4+\epsilon}.
\]
fixed \(\delta<\epsilon/4\) 再吸收 logs 正确。一般 fixed \(1/2<\theta<1\) 得 \(2\theta-1+\epsilon\)，445 的边界代入给 \(29999/40000+\epsilon\)。没有从这一增长幂推出 197 需要的 fixed fourth-moment constant。

## 6. 真短窗、principal Laurent 项和 additive 费用

446 §6–§7 的 scalar canonical interface 正确，且准确保留了其范围。

在 \(y=1+\eta u\)、\(\eta=H/X\le1/2\) 后，phase derivative 与 \(\eta t\) 同阶；integration by parts 给
\[
 |\mathcal MW_\eta(a+it)|\ll\eta(1+\eta|t|)^{-A}.
\]
换变量 \(v=\eta t\) 时 amplitude 与 frequency width 抵消，logarithmic weight 的 integral 仅给
\(\log^r(2Q_{\rm eff}(3+|\tau|+X/H))\)，没有免费 \(H/X\) saving。

只有完整 \(b_1=\Lambda\)、\(b_2=\Lambda*\Lambda\) 及 completely multiplicative character twist 的 generating series 是 \(D_\chi(s)^r\)。在 principal zeta 情形，
\[
 D(s)=1/(s-1)-\gamma+O(s-1)
\]
给 r=2 的实际 double-pole main
\(\int w((x-X)/H)(x/X)^{i\tau}(\log x-2\gamma)\,dx\)。
imprimitive principal 必须使用带 finite deletion 的真实 Laurent constant；主稿已经写明，不只保留最高 pole 阶后忽略低阶 residue。

这一特定 \(X^{\theta+\delta}\) error 要做到 power-small relative to \(H=X^\xi\)，需 \(\xi>\theta\)。它不是对所有分析方法的必要性定理。
\(X\asymp T^2,H\asymp T\) 的诊断比值为 \(T^{2\theta-1+2\delta}\)；
除以 \(\sqrt X\) 后 target 为 constant，而 error 仍是同一增长幂。
long-prime \(X=T^b,H=X/T\) 的 exponent 为
\(1-b(1-\theta-\delta)\)，所以 fixed \(\delta\) 可选后的 sufficient threshold 是 \(b(1-\theta)>1\)。主稿的 \(b>8\) 和 \(b>80000/10001\) 均准确；没有把它用于证明略超带宽一的 offdiagonal。

单位群上的 additive phase 以 normalized finite-group Parseval 得
\(\sum_\chi|c_\chi|^2=1\)，故 triangle/Cauchy 的实际费用是
\(\sqrt{\varphi(q)}\)，不可删除。principal main 按自己的 coefficient 保留；nonunit terms 不由该展开覆盖。all-conductor 输入能支付该 one-point interface，不能替代 modulus-averaged 或 shifted-response cancellation。

## 7. 截断与后续范围

实际 prime square 在 \(m\asymp T^2\) 的系数保留 \(a,b\le T\) 双截断；它不是完整 \(D(s)^2\) 的 coefficient。也保留原 taper、response kernel、background 及全部 mixed signed words。主稿明确没有由 scalar canonical bound 推出这个截断相关和，更没有把源 marked/inverse/plain moments 的 constrained row/Theta/mesh/width/mask 结论扩成任意 response-dependent coefficients。

198 已记载 225 的 pure-prime finite transfer 和 226 的背景化简；最终 446 尾段同时保留 232 逆审之后的实际状态：alternating high-product 区 \(ab>XL^2\) 不因原 compact support 自动消失，不能搬用 adjacent word 的 cutoff。只读 232、239–240 的准确条款后，确认当前对象是 physical quotient 后共同 centering 的实际 Möbius divisor response 和 adjacent-divisor dyadic mean-square，仍保留 six-window、determinant 与 exact finite-band kernel。该唯一尾段澄清正确，没有新数学问题；它没有把旧漏区再次宣布闭合，也没有重列已付通道。本次没有独立认证 203–240 那条旧链的整体渐近；不因此更新其研究状态。

最终 PASS 范围是：接受确切全族 strip、统一增长和 AF 原 second-moment/zero-tail [R] 后，446 对同一实际 finite Gabor matrix 的 canonical、sharp、operator 和弱第四矩接口成立，两个尺度阈值与 additive 费用正确。fixed-size signed Gram 预算、更高简单临界线比例、moving-modulus AF 二矩统一性、RH/RR 与形式化验收仍未由此证明。本次只新增本报告，未修改主稿、旧稿、math 或旧审计。
