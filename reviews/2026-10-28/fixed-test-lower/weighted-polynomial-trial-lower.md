# Theorem 6.2 lower：加权多项式试探空间核审

2026-10-28；独占分支稿，待 fresh／root 消费。恢复 STATE、G20261027、D20261028F、宏观前沿当前入口及唯一 next-fixed-test-lower-proof-gate，运行 research_state.py check／show，通过结构检查；起始工作树为空。只审固定 v2 的 6.2 lower 及必需 Lemma6.1／§6 定义，不用 6.4 或 6.5 补证明，不改 STATE、cadence、Git，不预合同或轮次。

原件 `literature/local/2026-10-28-core-source-location/bramble-trace-rstation-2-v2.md` 已现场核得 61862 字节，raw／LF SHA256 均为 `541098314b2ddc5f8645babf82086e87d16c46188268cbc7ed6cfc1f98720058`。实际逐段读原件 525–665 行：Lemma6.1 和 lower 证明全部；另读 §6 的 6.3 range／T_X 定义及旧 531／560 的 HS／完整型范围。没有浏览外网，没有重审 upper 或 sharp 证明。

## 1. 明确保留的前件与对象

本稿先条件冻结 **一个与 X、n、多项式及物理源均无关** 的 H0：

\[
 H_0\in S_0\mathcal H,\quad H_0(0)\ne0,\quad
 |H_0(t)|\le C_0e^{-c_0\sqrt{|t|}},\quad
 t^jH_0\in S_0\mathcal H\quad(j=0,1,\ldots).
\tag{H}
\]

要求 H0 在实轴 0 附近连续，原常数 C0、c0 固定；所有多项式倍必须在同一实际 Sonin gap／Hilbert 域。H0 的存在、Gevrey 平滑是否保双 gap、非零 evaluation 与全部导数域由 unit_height 独占审查，**此处不以原稿一句话认证 (H)**。若该独立支链失败，本稿下游全部条件性冻结。

\(\mathcal H=L^2(\mathbb R,dt/(2\pi))\)，
\(D_X(t)=\prod_{p\le X}(1-p^{-1/2-it})\)，\(w_X=|D_X|^2\)。§6.3 的实际 range 为 \(S_X\mathcal H=D_X S_0\mathcal H\)；它是 range 身份，不是等距。真实 S_X 是该 range 的正交投影，故保留全部 Gram 逆；不能换成 D_XS0D_X*。

固定任意非零 complex compact smooth 物理 log 卷积源 r，写 \(F(t)=\widehat r(t)=\int r(u)e^{-itu}du\)，\(\mathcal T_X(r)=\|A_rS_X\|_{HS}^2\)。物理源 r、raw Sonin 向量 H0、多项式试探向量、裸 evaluator 各保原角色。原 531／560 已付每 fixed finite-X 的普通正迹／HS；本稿不从未平滑 ambient kernel 取迹，不要求其在 X 上一致有界。

## 2. Lemma6.1 的必要 uniform 权界

只需 B=2 的绝对 uniform 结论；以原稿所引的标准 Vinogradov–Korobov 零自由区为 cited 输入，不在此优化或重证该外部定理。核其本段推导如下：

- 对 \(\Psi_t(y)=\sum_{m\le y}\Lambda(m)m^{-it}\) 使用 Perron，高度取 \(T=y^{B+2}\gg |t|\)。在零自由区内的较窄直线 \(\Re z=1-\delta_{2T}\) 上，局部 zero 公式给 \(\zeta'/\zeta\) 一个 log T 的固定幂上界；靠近 ζ 的 pole 单独保留。移线只跨 \(z=1-it\)，不跨 kernel 的 z=0。
- 分母 z 的积分只付 log T，\(|m^{-it}|=1\) 使截断误差不额外依赖 t；整数 endpoint 改成半整数及再 round 的误差保持 uniform。得到原 551–553 行的绝对误差 \(y\exp[-c_B(\log y)^{1/3}/(\log\log y)^{1/3}]\)，允许改变常数并吸收 log 幂。
- prime powers 的绝对去除费 \(O(\sqrt y\log^2y)\) 足够。prime sum 在 \(y<\sqrt X\) 部分粗界为 \(O(X^{1/4})=o(A)\)，\(A=\sqrt X/\ell\)、\(\ell=\log X\)。在 \([\sqrt X,X]\) 取 Ψ 的 exponent 2B，保证 \(|t|\le X^B\le y^{2B}\)。
- partial summation 使用 \(g(y)=y^{-1/2}/\log y\)；twist 已包含在 Ψ_t，**g′ 不产生 |t|**。main term 的导数为 \(y^{-it}\)，所以得到原振荡积分；uniform 余项仍为 o(A)。随后 v=log y 的 endpoint integration 只用 \(|1/2-it|^{-1}\le2\)，余项 \(O(A/\ell)+O(X^{1/4})\) 为 o(A)。

未发现从 polynomial-height uniform 退回仅 compact-height 的隐换；误差是绝对量，不是大 t 时相对 main term 的误差。高次 Euler log 项用 \(\sum_{p\le X}p^{-1}=O(\log\log X)\) 控制，故原稿所需

\[
 \log w_X(t)=-4A\Re\frac{e^{-it\ell}}{1-2it}+o(A),
 \qquad |t|\le X^2
\tag{W}
\]

确由这条 cited-input 推导链给出。Perron／零自由区本身的既有标准定理资格与精确外部常数保持 cited；没有声称重证上游深定理。

## 3. Legendre 比较对所有 degree<n 统一

置 \(m=\pi/\ell\)、\(h=\ell^{-2}\)、\(J_X=[m-h,m+h]\)，并写
\(I_p=\int_{J_X}|p(t)H_0(t)|^2dt\)。由 (H) 的连续非零值，所有大 X 的 J_X 上 H0 有固定正下界；对任意非零多项式 I_p>0。

把 p 在 J_X 的正规 Legendre 基
\(\sqrt{(2j+1)/(2h)}P_j((t-m)/h)\) 上展开，Cauchy–Schwarz 给 point evaluation 的基平方和。有限 Legendre 多项式系数式给 \(|P_j(z)|\le[C(1+|z|)]^j\)（实 z）；\(|(t-m)/h|\le C\ell^2(1+|t|)\)。因此对 **ALL complex p，deg p<n，ALL real t**，

\[
 |p(t)|^2\le Cn^2\ell^2
 [C\ell^2(1+|t|)]^{2n}\int_{J_X}|p(v)|^2dv.
\tag{P}
\]

没有选定单个 extremizer、实多项式或固定 n；原 C 不依 p、X、n。利用 H0 在 J_X 的下界和 (H) 的全线衰减，

\[
 \int_{\mathbb R}|pH_0|^2dt
 \le \exp[C_1n\log(n+\ell)] I_p.
\tag{U}
\]

矩费可直接核：令 u=√|t|，\((1+u^2)^{2n}\le2^{2n}(1+u^{4n})\)，相应积分 ≤C^(n+1)Γ(4n+2)。因为 Γ(4n+2)=(4n+1)!≤(4n+1)^(4n+1)，连同 (P) 的 \(\ell^{4n}\)、n²ℓ² 给 (U)。这确实控制整个增长维数的多项式空间，不只是一个向量的 norm。

## 4. 全线加权 norm：两个坏区与完整 tail

F 是非零 entire，故 k=ord0F 有限。先选 fixed 小 δ>0，使 \(|F(t)|\ge c_r|t|^k\) 对 \(|t|\le\delta\) 成立；这是 complex F 的模下界，不要求偶性或实源。定义固定正 gap
\(\Delta_\delta=4-4/\sqrt{1+4\delta^2}>0\)。

由 (W)，原稿三条权界有效：

\[
 \inf_{J_X}\log w_X\ge(4-o(1))A,
 \quad\sup_{\delta\le|t|\le X^2}\log w_X
 \le(4-\Delta_\delta+o(1))A,
 \quad\sup_{|t|\le\pi/(2\ell)}\log w_X\le o(A).
\tag{G}
\]

第一条使用 tℓ=π+O(1/ℓ)，第二条用分母模，第三条用 cos(tℓ)≥0 及 t=O(1/ℓ)。这些都是 uniform bounds。全线另有 \(w_X(t)\le e^{(4+o(1))A}\)，只用有限 product 的绝对 Euler 上界及 t=0 的 PNT，不将 (W) 外推到任意 t。

选
\[
 n=\lfloor c_\delta A/\ell\rfloor
 \asymp\sqrt X/(\log X)^2,
 \qquad C_1c_\delta<\Delta_\delta/2.
\]

所有大 X 有 log(n+ℓ)≤ℓ。加权总 norm 至少为 \(e^{(4-o(1))A}I_p\)；(U) 的花费至多 \(e^{C_1c_\delta A}\)。于是 (G) 的小中心和 δ 外至 X² 两个坏区，相对 **同一全加权 norm** 的质量分别 ≤e^(−cA)，常数可取对所有非零 deg p<n 统一。这里没有先依 p 选 cδ。

对 \(|t|>X^2\) 必须另付真实全线尾。由 (P)、(H)、global Euler，除以 J_X 的加权 lower 后，尾比例至多

\[
 e^{O(A+n\log\ell+\log n)}
 \int_{|t|>X^2}(1+|t|)^{2n}e^{-c\sqrt{|t|}}dt.
\tag{Tail}
\]

写 u=√|t|≥X。因 n=O(√X/ℓ²)，\(n\log u/u\) 在 u≥X 的最大值为 O(1/(√Xℓ))→0。故整段上多项式都可由一半 Gevrey 指数吸收，剩余积分 ≤C(X+1)e^(−c′X)；前置 O(A+n logℓ) 远小于 X。尾比例仍为 O(e^(−c″X))，对全部多项式统一。没有漏掉 high-frequency tail，也没有以 compact-frequency gap 代 global bound。

记 \(\mathcal V_X=\{D_XpH_0:\deg p<n\}\)。因此 ALL v∈V_X 满足

\[
 \int_{\pi/(2\ell)\le|t|\le\delta}|v(t)|^2\frac{dt}{2\pi}
 \ge(1-\varepsilon_X)\|v\|_{\mathcal H}^2,
 \qquad\varepsilon_X\to0
\tag{C}
\]

且 ε_X 不依 v。2π 在上述所有 norm 比例中消去，不能再扣一次。

## 5. 维数、实际域与 trace lower

条件 (H) 使 pH0∈S0H；有限 X 的 D_X 及逆在实轴有界，range 身份使 V_X⊂Ran S_X。D_X 和 H0 在 J_X 非零，所以多项式到 D_XpH0 的 map 单射；V_X 的真实维数恰为 n。全线矩界保证每个向量均在原 Hilbert 空间，不是 formal polynomial。

在 V_X 取按 dt/(2π) 正规的正交基 v1,…,vn。物理卷积 A_r 在此表示为乘 F；每个 fixed X，A_rS_X 的 HS 已由旧 531／560 的实际有限 F trace 域支付。故合法 HS 基展开给

\[
 \begin{aligned}
 \mathcal T_X(r)
 &\ge\sum_{j=1}^n\|Fv_j\|_{\mathcal H}^2\\
 &\ge c_r\ell^{-2k}\sum_{j=1}^n
   \int_{\pi/(2\ell)\le|t|\le\delta}|v_j(t)|^2\frac{dt}{2\pi}\\
 &\ge c_rn\ell^{-2k}(1-\varepsilon_X)
 \ge c'_r\frac{\sqrt X}{(\log X)^{2k+2}}.
 \end{aligned}
\]

这里只求有限正项之和，不交换无限 trial／X 极限、不借 ambient diagonal 求迹。源 r 先固定，δ、cδ、k、c′r 和“充分大 X”均可依 r；没有 ALL changing-source uniform。r 非零的 Fourier entire 函数有限零阶确保覆盖每个 fixed 非零 complex 源，而非仅 hat r(0)≠0 的情形。

## 6. 判定、强旧与待根消费范围

**条件于 (H)、实际 range 字典以及原稿 cited 标准零自由区前件，6.2 lower 的加权多项式／全尾／维数／trace 推导闭合。** 本分支未发现需要 6.4 sharp 证明才能补的孔洞；也不据此认证 H0 存在或完整原稿。

最强旧短链的区别保持：531 只给合法有限 F 正迹及粗相对费；535／570 是 fixed-F 实际不定；560 的粗 inverse lower 输入在全 physical H，未属 Sonin evaluator／Weil source；571／572 和已付安全高频不含这个 fixed-source cofinal 总迹 lower。因此若 H0 独立审查与 fresh／root 均闭合，此处会支付实际 cofinal 源质量的非空 lower 信息，不能隐入“旧 positive trace 因而显然”的标准0。最终是否已有更强旧资产蕴含相同结论，仍由 root 最强旧审计结算，不由分支计轮。

这条 lower 自身没有 sharp 系数4、upper、密度集中、强投影极限或 6.5 单步结论。它也不是 Q 负、K 全 PSD、whole4/5 改善或核心 coupling／primitive 容量。只有携 root 的原 560 同源完整型／pole／cofinal字典后，才可谈其 fixed-source K 必要费用；本稿不越过该消费阶段。若 (H) 支链失败，立即冻结此条件后果并止原 recipe，不转后章修补。
