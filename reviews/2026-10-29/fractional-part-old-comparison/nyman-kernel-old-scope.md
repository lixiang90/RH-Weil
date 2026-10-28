# Fractional-part 核：Nyman 强旧范围核对

2026-10-29；`/root/moment_fresh_audit` 当前独占去重稿。恢复 README/STATE、check→show、Goal/原0c4f、AZ/formal18 与前沿；现场已是 cadence0/history54/latest590。这里只读081–084及003必要来源条目，不读新原件/章、不查询、不作数值，不编辑 STATE/cadence/board/Git，不准 C054 或新证明预算。Pan 与完整 Weil 角色另由 root 核。

**判定：核、原 Hilbert 范数和算术取样均已在081/082实际存在，净值0。** 任意 physical 源的卷积是同一 dilation carrier 的连续源版本，不是新的独立算术正性输入。必须区分两个 distance：旧整数右平移的 target distance→0仍精确等价于 RH；放宽到任意全实线源后，range 稠密本来无条件成立，不能再称该无约束 distance 等价于 RH。

## 1. 精确酉对应，不换原范数

081采用 `H=L²((0,∞),dx)`，`r_n(x)={1/(nx)}`、`χ=1_(0,1)`，Mellin `Mf(s)=∫f(x)x^(s−1)dx`。定义

\[
 (Vf)(u)=e^{-u/2}f(e^{-u}),\qquad s=\tfrac12+it.
\]

变量替换给 `||Vf||_(du)=||f||_(dx)`、`widehat(Vf)(t)=Mf(s)`，所以这是原范数的酉 log/反向坐标变换，不是 completed Mellin 加权空间。恰有

\[
 Vr_1=h(u)=e^{-u/2}\{e^u\},\quad
 V(\sqrt n r_n)=\tau_{\log n}h,\quad
 V\chi=\Phi(u)=e^{-u/2}1_{u>0},\quad\widehat\Phi=1/s.
\]

这里 `τ_a h(u)=h(u−a)`。081定理PC已经给

\[
 H(t)=\widehat h(t)=-\zeta(s)/s.
\]

候选的负号、`1/2+it` 分母与原件完全一致；不能漏掉分母或用 ξ/Γ norm 替换。physical 源 r 直接在 du 上输入 `Jr=h*r`，不再暗添 `e^(u/2)` 因子。

## 2. 候选 B 就是082的完整正核

082定义 `w(t)=|ζ(s)|²/|s|²`、`κ(a)=∫w(t)e^(ita)dt/(2π)`，并已付 `w∈L¹`、κ连续正定。当前

\[
 B(r,q)=\langle h*r,h*q\rangle_{du}
       =\int\widehat r(t)\overline{\widehat q(t)}w(t)\frac{dt}{2\pi}
\]

是同一对象；第一槽线性、Plancherel `dt/(2π)` 均不变。取有限原子源时卷积按有限平移和解释，无须将 Dirac 放进 L²：

\[
 B(\delta_{\log m},\delta_{\log n})
 =\kappa(\log(m/n)),\qquad
 \langle r_m,r_n\rangle=\kappa(\log(m/n))/\sqrt{mn}.
\]

Fourier平移先给 κ(log(n/m))；二者相同是因为实际 w 实偶，κ实偶，不是任意正谱都偶。082还已给

\[
 \|h\|_2^2=\kappa(0)=\log(2\pi)-\gamma,
 \quad\langle\tau_{\log n}h,\Phi\rangle
          =(\log n+1-\gamma)/\sqrt n.
\]

所以 normalized Gram、target coupling 和平方范数均已存在，不只是一个“相似 Nyman 标签”。仅使用 B 的 PSD 而不保 target coupling，会丢掉原 Schur-distance 的关键责任。

原 h 也直接满足：u<0时 `h=e^(u/2)`，u≥0时 `0≤h≤e^(−u/2)`，故 `h∈L¹∩L²`、`||h||₁≤4`。Young给 `||Jr||₂≤4||r||₂`，原 compact smooth/Schwartz 源均合法；这只是同核的标准域运输。不存在需要新论文才支付的 positive-carrier 存在性或原du有界性。

## 3. 哪个 target distance 仍是 RH

令 `A_N(s)=Σ_(n≤N)c_n n^(−s)`。081取 approximant `−Σc_n r_n`。当前坐标下相同 approximant 是

\[
 J\mu_N,\qquad
 \mu_N=-\sum_{n\le N}\frac{c_n}{\sqrt n}\delta_{\log n},
 \quad\widehat{J\mu_N}=\zeta(s)A_N(s)/s.
\]

因此原 target residual精确为

\[
 \|\Phi-J\mu_N\|_2^2
 =\frac1{2\pi}\int\frac{|1-\zeta(s)A_N(s)|^2}{|s|^2}dt.
\]

负号及 `n^(−1/2)` 属实际系数运输，不能省掉。081定理PD已付：对全部 length-N Dirichlet coefficients 取 infimum 得 d_N，**RH⇔d_N→0**；整数 n≥1 取样已足够。082 whitening 后同一值为 `1−g_N* K_N^(−1)g_N`（必要时伪逆），不是“Gram本身正定⇒距离消失”。

082又已付 `λ_min(K_N)→0`，仅因 log(n/(n−1))→0 的相邻节点碰撞即成立，与 RH 无关。它既不证明错误的 off-line cokernel，也不证明 target 对允许低谱方向的正确对齐。Uniform Gram gap 或粗逆范数都不能代替所需 target upper。

## 4. 任意全实线源确实更宽，但不增强 RH 结论

当前候选若让 r 遍历 `Cc∞(R)` 或全部 `L²(R)`，已不限于上节的整数非负右平移 source。H在实轴非零 a.e.：ζ(s)/s在临界线上解析、非恒零，实零离散；此事实不依赖 RH。Fourier侧 J为有界乘法 `M_H`，故其值域的正交补为 `ker M_(conj H)={0}`，从而

\[
 \overline{J(L^2(\mathbb R))}=L^2(\mathbb R),\qquad
 \overline{J(C_c^\infty(\mathbb R))}=L^2(\mathbb R).
\]

第二式由 `Cc∞` 在 L² 稠密及 J 有界。于是对 Φ 的**无约束**距离为0本来无条件成立。这不是 Nyman theorem 的新证明，而是取消了取样/半群/解析 division 限制。不能把全实线源的稠密性再放回旧受限 arithmetic span；off-line 零的解析评价障碍也不等于临界线上 H 的 a.e. kernel。

这一区别同时限定候选价值：它给一个显式、非循环、正且有界的 source carrier；“得到正 norm/无限维像/全部源可输入”不自动给旧 d_N 的 cofinal decay，更不提供新的经典完整目标身份。

## 5. 083–084已经把未付费用放在哪里

083已给 Möbius log-polynomial coefficients的完整低除数卷积和 almost-prime filtration；线性 smoothing 的 `2≤m≤N` defect恰为 `Λ(m)/logN`。这不是新的 prime-power 正号或自动 critical norm 小量。`m>N` truncated-divisor tail、其自能量及与低区 cross仍需控制。

084进一步已付线性 mollifier 的 exact局部正分解

\[
 R_N^{loc}=\{a_N^2+V_N+(N-1)|a_N-\bar u_N|^2\}/\log^2N,
 \quad R_N=R_N^{loc}+R_N^{bdry}.
\]

周期边界层 `R_N^bdry=∫_N^∞|F_N(y)|²dy/y²` 亦已精确定义；有限正表达式/低区 Λ 恒等式不估计该尾。证明相应 cofinal upper仍承载 RH责任，不能因重新写成 B(r,r)≥0而支付。082所列 Burnol lower及有额外假设的 optimal mollifier，也不是无条件 upper 输入。

**强旧净值0：** 当前同核重现/连续源运输没有新增算术输入、target alignment、global residual upper或完整 Weil 比较；不建 C054，不恢复旧mollifier优化、来源或数值预算。本稿不以 carrier positivity判 Pan/完整 Weil 等同，也不泛排 fractional-part、不同 source约束或任何真正新 signed机制。

## 本地证据

实际全文读081–084；003只读18–22及相关背景条目，作为旧引用归属，不声称重审外部证明：18 Balazard–Saias/精确division背景，19 Báez-Duarte整数族，20 de Roton一般化，21 Burnol lower，22 Bettin–Conrey–Farmer条件upper。没有打开这些URL或新原稿。

现场LF版本：

| 文件 | bytes | SHA256 |
|---|---:|---|
| 081 | 10221 | 9674636567be2e3be6d8ece3dbb76557fd139482a66b92a1401454f2b2def5da |
| 082 | 8417 | c24ac8dec4987a2c76e1758dce73633930d68b5acc9d7d83690d2204f722a340 |
| 083 | 8105 | 530af5d77c29584d65c1ecec5a894c17169ba6deed5503f61caff181b474d8c9 |
| 084 | 7368 | c4d3036bd341903ca9bb7c6dec4c5ac2b65a79d1a829c9093f1a0c5d1fd9e327 |
| 003，仅读上述条目 | 34762 | 3e45022fcb5979bf2a15eb16c0214f4f0edba2c6cd80c560553c31b2b7651887 |

当前新去重任务 terminal；本稿不代root消费/后继准入。
