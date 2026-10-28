# Möbius causal Green 响应：最强旧链、次数反测与 principal 范围

2026-10-29；限定支持审查，供 root 消费。未创建数学合同、未计轮、未查 web／新论文，不改 STATE、cadence、Goal 或 Git。本文不把 analytic Green 逆命名为算术主除子。

## 1. 实际对象与不可遗漏的因子

采用 405、518–520 原对象的复化。bare 源是 \(f\in\mathcal S_{\exp,\mathbb C}\)，physical 源是 \(r(u)=e^{u/2}f(u)\)。乘以这个固定指数给 \(\mathcal S_{\exp}\) 的拓扑自同构，但这不是一个共同 du／Dlog 有界性断言。对每个实际源定义

\[
 V_r(t)=\sum_{n\ge1}\mu(n)n^{-1/2}r(\log n-t).
 \tag{1}
\]

每个紧 t 区间上的各阶导数绝对一致收敛：取任意 \(N>1/2\)，在该区间上对大 n 用 \(p_{N,j}(r)e^{Nt}n^{-N}\)；余下有限项另付。对 compact r，这些和局部有限。故 (1) 是实际的 \(C^\infty(\mathbb R)\) 函数，不是零点插值定义的符号。

518(11) 的原 Möbius 逆是

\[
 \theta_f(x)=\frac12\sum_{n\ge1}\mu(n)f(\log(nx)),\qquad x>0.
\]

直接代入得到精确同一映射

\[
 \boxed{V_r(t)=2e^{-t/2}\theta_f(e^{-t}).}                 \tag{2}
\]

因此 (1) 是 518 已付 Möbius 重建的反射和 critical 权搬运，不是一个不同的 arithmetic inverse。405 的实际 E 源包含正负整数：

\[
 E\eta(u)=2\sum_{m\ge1}\eta(me^u).
\]

由 518 的点态逆（或直接按 \(k=mn\) 绝对分组）可得

\[
 \boxed{V_{e^{u/2}E\eta}(t)=2e^{-t/2}\eta(e^{-t}).}       \tag{3}
\]

右侧的 2 不能删。双和的固定 t 绝对界可用
\(2e^{-t/2}\sum_{m,n}|\eta(mne^{-t})|<\infty\)，由 Schwartz 衰减及 \(\sum_{k\ge1}d(k)k^{-N}=\zeta(N)^2\)（N>1）支付。

还有一个等价的实际 convolution inverse：在正半线的局部有限分布

\[
 a=\sum_{n\ge1}n^{-1/2}\delta_{\log n},\quad
 b=\sum_{n\ge1}\mu(n)n^{-1/2}\delta_{\log n}
\]

满足 \(a*b=\delta_0\)；对本源类可合法写

\[
 V_r=b*\check r,\qquad a*V_r=\check r,
 \quad \check r(t)=r(-t).                                \tag{4}
\]

最后等式的换序由 \(\sum_{k\ge1}d(k)k^{-1/2}|r(\log k-t)|<\infty\) 支付。它是 080 的 Dirichlet convolution inverse 在对数源上的同一升起，而非新 geometric divisor sequence。这里没有证明 \(a*\) 在整个 \(L^2(dt)\) 上有界或定义在全空间；不得把 (4) 免费当一个 \(L^2\) Hilbert complex。

## 2. 实际 I／Pan、平移与两个次数

519 已付的强结论是

\[
 E:\mathscr S_{e,0,\mathbb C}\simeq I_{\mathbb C}
   =\{f:M_f^{(j)}(\rho)=0\ (0\le j<m_\rho),\ \forall\rho\}
\]

为明确 Fréchet 空间之间的拓扑同构；不是只知道一个稠密原像。518/519 还付实际逆的有限半范数费用、平凡零点对应的偶 Taylor 数据。对全部 \(f\in I\)，(3) 因而可用真实且唯一的合法 \(\eta\) 表示。

由 \(\eta\) 偶、\(\eta(0)=0\)，有 \(\eta(x)=O(x^2)\)；由 Schwartz 衰减有 x→∞ 任意幂衰减。故 (3) 在 t→+∞ 是 \(O(e^{-5t/2})\)，在 t→−∞ 任意指数衰减，其各阶 t 导数同样受控，特别地属于 \(L^2(dt)\)。精确范数为

\[
 \boxed{\|V_{e^{u/2}E\eta}\|_{L^2(dt)}^2
       =4\int_0^\infty|\eta(x)|^2dx.}                    \tag{5}
\]

所以模掉 ambient 的有限 \(L^2\) 响应，消掉的是**整个 I**，不只是
\(P_{\rm an}=I\cap\ker d\cap\ker c\)。Pan 的消去及其所有平移由这个更强旧事实直接给出。

physical 平移取 \((\tau_a r)(u)=r(u-a)\)，则逐项有

\[
 V_{\tau_a r}(t)=V_r(t+a).                              \tag{6}
\]

与 bare 平移的权必须分开：physical 化 bare \(\tau_a f\) 得 \(e^{a/2}\tau_a r\)，其响应为 \(e^{a/2}V_r(t+a)\)。两者都保 L² membership，不能误把 bare 平移和 physical 平移的次数权混成相同算子。

405 已提供一个不需新参数的完整反测。其真实 Gaussian \(h=E\eta_0\in I\) 满足

\[
 d(h)=c(h)=1/4,\quad B(h,h)=1/16,\quad
 B(h,g)=(d(g)+c(g))/8.
\tag{7}
\]

但 (3)–(5) 仍使 \(V_{e^{u/2}h}\) 的 ambient 模 L² 类为 0。因此仅使用这个类的双线性配对不可能同时等于 405 的完整 B 于全部源。这不是一个离开原点／无 pole 的 test：完整 B 的两次数项正是未保留的内容。特别不能由“全部 Pan 被消掉”升级成“全 Weil pairing 已下降”。

给类再加 d、c 可以恢复次数 bookkeeping，但 405(14) 早已给实际代数／拓扑分裂

\[
 \mathcal S_{\exp}/P_{\rm an}
      \simeq\mathbb C^2\times(\mathcal S_{\exp}/I).
\]

该增补不是新的乘法、principal、sections 或 mixed RR 输入。本文不要求任意合法未来映射的核必须恰为 Pan；这里只判断眼前仅凭响应类消费 full B 的实际提案。

## 3. 非零 compact 源的 bare critical L² 反测：准确旧链

以下命题不是声称 518 中逐字已有同一陈述；它是这个已知 inverse 符号加标准整函数零数／ζ零点计数及 Laplace Cauchy–Schwarz 的直接域比较，不给新的算术上界。

**命题。** 对任意非零 \(r\in C_c^\infty(\mathbb R,\mathbb C)\)，(1) 不属于普通 \(L^2(dt)\)。不假设 RH、简单零点、零点间距或正比例中心线定理。

证明核要点如下（具体域估计可与本目录另一份 domain 稿逐项交叉核对）。设 supp r⊂[−L,L]。则 \(V_r(t)=0\) 于 \(t<-L\)，并有粗上界 \(O_r(e^{t/2})\)。令

\[
 M_r(z)=\int r(u)e^{zu}du.
\]

在 Re z>1/2 中绝对 Fubini 得

\[
 \int_{-L}^{\infty}V_r(t)e^{-zt}dt
      =\frac{M_r(z)}{\zeta(1/2+z)}.                       \tag{8}
\]

若 \(V_r\in L^2\)，左边给 Re z>0 内的全纯函数并满足

\[
 |F(\sigma+i\tau)|
       \le\|V_r\|_2\,\frac{e^{\sigma L}}{\sqrt{2\sigma}},
 \quad\sigma>0.                                         \tag{9}
\]

于是右边在 Re z>0 的所有 pole 必须可去；边界 \(z=i\gamma\) 的未消整数阶 pole 也与 (9) 的 \(O(\sigma^{-1/2})\) 径向界矛盾。这里先用开半平面的 meromorphic identity／唯一性，再对固定边界点取径向极限，不假 H² 函数预先有该点边界值。

然而 \(M_r\) 非零且为有限指数型整函数，Jensen 给任意固定移心盘内的零数（含重数）O_r(T)。Riemann–von Mangoldt 与 \(\rho\mapsto1-\bar\rho\) 对称给 \(\Re\rho\ge1/2\)、\(|\Im\rho|\le T\) 的 ζ 非平凡零点数（含重数）\(\gg T\log T\)。故至少一个 \(z=\rho-1/2\) 的 pole 未被 \(M_r\) 足重数消掉，矛盾。

这个“所有非零 compact 源都失败”的结论不等于 RH 反证或全 Green 路线边界。它同时受到 RH 所允许的中心线 poles 阻碍；把 bare inverse 必须属于普通 critical L² 当全源目标，本身就是过强的目标。不同截断、范数、renormalized／relative response、源适应、signed comparison 等不在此命题的否定范围，本文不据此授参数／family 后继。

## 4. 不要把 ambient 商偷换成既有 Hausdorff 源商

(1) 是到 \(C^\infty\subset L^2_{\rm loc}\) 的合法函数映射，可以形成**代数** ambient 类

\[
 [V_r]\in L^2_{\rm loc}(\mathbb R)/L^2(\mathbb R).
\]

其 ambient 商拓扑非 Hausdorff，因为 L² 在 L²loc 中稠密（紧 crop 即可）。同理在 \(C^\infty\) 的局部 Fréchet 拓扑下，\(C^\infty\cap L²\) 由 smooth compact crops 稠密。不能继而声称响应 range \(V(\mathcal S_{\exp})\) 内相应分母也稠密：裁切后的 \(\chi V_r\) 未证明仍在该 range。本文不作这个 restricted-range 命题。

因此 compact 源给非零 algebraic 类，不意味着已经构造独立的 Hausdorff 正 Hilbert primitive；有限能量对象被模掉也不等于它们是实际 meromorphic functions 的 principal divisor。519–520 反而已经给更准确且 Hausdorff 的 Fréchet 源商、全 jets、actual resolvent 和 Jordan 数据。新 ambient 商不得冒作它的无损改进。

尤其不证明本映射的核等于 I 或 Pan。一个可核的条件对照来自 520：若存在非平凡左侧离线零点 \(\rho_0\)（Reρ0<1/2），该文 actual \(u_1\in\mathcal S_{\exp,\mathbb C}\) 满足

\[
 M_{u_1}(s)=\frac{H_0(s)}{s-\rho_0},\quad H_0=\xi/2,
       \qquad [u_1]_I\ne0.
\]

对 \(r_1=e^{u/2}u_1\)，(8) 型变换为

\[
 \frac{M_{u_1}(s)}{\zeta(s)}
 =\frac{s(s-1)\pi^{-s/2}\Gamma(s/2)}{4(s-\rho_0)}.
 \tag{10}
\]

从初始 Re s>1 移到 Re s=1/2，不跨 (10) 的任何 pole；Gamma 给高处指数衰减。逆 Mellin/Plancherel 从而给 \(V_{r_1}\in L^2(dt)\)，尽管 \(u_1\notin I\)。这是条件范围警告，不是假设 RH 失败或断言存在这样的零点。它也表明不能单从“都消 I”直接认证该响应类忠实保留 520 的全部实际商谱与重数。

## 5. 080–082 与本反测的角色分开

* 080 的有限 incidence differential 可逆、det=1，却保有第一列 μ 及 Green energy \(M(N)^2/N\)。有限 acyclicity 不会消掉所有 Green 内容；本文不反驳它。要付的仍是 RH 等价的 subpower bound。
* 081 既有一个真正的 Mellin／Hardy Hilbert completion、正 Gram／Schur distances、NB density theorem。它求的是 noncompact fractional-part features 对特定 noncompact target 的 residual closure，即 \(\|(1-\zeta A_N)/s\|_2\to0\)；不是要求每个 compact smooth 源的 bare \(M_r/\zeta\) 属于 ordinary critical L²。
* 082 已分开中心线 zeros 导致的低谱 wells 与右半平面 off-line cokernel。小奇值不反驳 RH，Gram positivity 不证明 distinguished distance 趋零。同样，本稿的中心线 pole 所致 bare inverse 发散也不反驳 NB，也不给新的 Schur margin 上界。

所以不能用本候选的新记号重新领取 080 的 actual nonlocal Green inverse、081 的 Hilbert carrier 或 519–520 的 actual source quotient，亦不能把 ordinary energy domain 的失败推广到全 Hodge／Green 方法。

## 6. 已停止同域 Möbius 结果的恢复

本次另已全文核读 522、525、526，避免把 518 当成该路线的最后前沿：

* 525(1) 已给一般源的 \(W_f(x)=\frac12\sum\mu(n)f(\log(n/x))\)；本响应准确为 \(V_r(t)=2e^{-t/2}W_f(e^t)\)。525§2–3 还付一般逆的全族粗界／PNT 抵消界、实际 \(L^1(dx)\) 与零质量、截断质量费，§4 付全部 smooth 源的临界 \(\varepsilon\)-增长与 RH 等价，§5 付固定探针剩余极阶 \(\max(m_\rho-\operatorname{ord}_\rho M_f,0)\)，§6 说明无盲 Gaussian 的端点还迫简单性。本文 ordinary L² 的 compact 域反测不是这些章节逐字的命题，但完全使用同一符号／pole 检测机制；它既没有支付那条临界估计，也没有恢复同域已停止的增长或 cutoff 预算。
* 522 已付原 Hausdorff 商的最优指数下确界 \(\omega_X=\sup_\rho|\Re\rho-1/2|\)、RH 与全部统一商半范数次指数界的等价、actual 源修正版本；本 ambient 响应类比这些忠实的原商设施更弱。
* 526 已付双／固定有限多实权 Hilbert 商对原 jets 商的忠实性、实际群及真实近频率费用、无等价酉化与一族临界未重标定商范数的 fixed-class 退化。这不是 (1) 的同一个范数域定理，不能借为本响应的无条件完整 kernel 定理；但它已排除“新记号加正 norm 就有独立极化”的旧误读。

因此当前工作是恢复并比较既有同域停止范围，不是第一次准入 Möbius 模型；不新领增长、换权、截断或完成化合同。

## 7. 最强旧净后果与准入结论

最短依赖链是：**518(11)、(19) actual Möbius inverse → physical 反射权搬运 (2) → 519 actual closed image/逆连续与合法 even source → (3)–(5) 全 I 有限能量；405 Gaussian 两次数与完整 B 给现成 source-role 反测。** Critical compact test 再加标准 Jensen/RvM/FE/Laplace pole argument。没有新增独立算术／几何输入；两个 degrees、源商及 multiplication bookkeeping 也没有较强净推进。

准确可消费结论：此具体 causal Green／ordinary critical L² 类是一个实际的、可计算的解析反演与域测试，作为几何 principal／正 primitive 输入则不通过。反演主体是强旧重编码，域比较是直接标准后果，**old0 停止**；不建 C056/593，不续 damping／truncation／metric／clock／completion／新 complex 或来源队列。

本判断不说全几何主线失败，不排任何不同且有真实独立输入的 principal／relative／higher／signed 机制。原 du/Dlog、完整 Γ/contact、proper powers 与两个 poles 没有通过 (1) 得到新的完整身份或 signed 缺陷估计。核心同一非零 arithmetic primitive→principal→sections/multiplication→mixed RR 及危险 core/cross/成长 Ξ 仍欠；whole leading4/5 仍只是既有负惯性上预算。仅待 root 与另一域稿对齐及独立审查，本文本身不等于 root 结算。

依赖原件：notes/405-f1-adelic-restriction-moments-and-radical.md；notes/518-f1-quantitative-mellin-division-and-mobius-source.md；notes/519-f1-closed-source-image-and-degree-moments.md；notes/520-f1-source-quotient-spectrum-and-centered-growth.md；notes/080-divisibility-incidence-green-hodge.md；notes/081-mellin-division-nyman-beurling-hodge.md；notes/082-beurling-log-toeplitz-feshbach.md；notes/522-f1-optimal-centered-growth-and-rh-equivalence.md；notes/525-f1-smoothed-mobius-probes-and-arithmetic-strength.md；notes/526-f1-faithful-two-weight-hilbert-quotient-and-defect.md。
