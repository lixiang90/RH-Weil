# 自由 b 正式论文独立数学审查

日期：2026-10-07。结论：**限定 PASS [T/R]**。本报告逐段审查新论文全文，而非将 note 449 的既有审查移植为论文审查。结论是明确输入包 \(\mathcal R\) 下的相对证明通过；不代表重新证明该输入包、源论文全部证明核或 RH。

## 1. 最终版本及范围

被审对象：`papers/free-b-compensated-probe-boundary-paper.tex`，876 行，canonical LF UTF-8 长度 35118 字节。

- 最终论文 canonical LF SHA-256：`5df2b6ad687572229e2c4d41292bee6cf81b57a13b762173d26732169f1688db`。
- 原输入源：`E:\codex-build\math\preprints\The-Quasi-Riemann-Hypothesis-September-30-2026\build\paper.tex`，commit `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，canonical LF SHA-256：`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。
- 独立参数推导 `hybrid-free-b-geometry-optimization.md`：`35dac7399af8507be7c39c0e3e69c37d47adf83ebda9125d2a5f62e663037f67`。
- 精确代数脚本 `scripts/hybrid_free_b_geometry_exact_audit.py`：`5a366da5e8114d158cb76b3a94060155786a0ca637a914b662ba17cd66afa63f`。
- 配套 note 449：`2d4b37628d6f68229fd687d6ac84c2ba03cb7223c412df5e00c07a0ff5e1a3bd`。

哈希仅将 CRLF 和孤立 CR 转为 LF，不删空格或空行。终审后附录命令仅由 `\src{python scripts/...}` 改为 `\texttt{python}\ \src{scripts/...}`；将此唯一改动逆替换后精确恢复已审 SHA `0fc6b3687b2545098482dbf14f7258f5fb26505eb7ba376387b4a13597caf7b7`，因此数学全文不变，PASS 绑定更新至上列最终 SHA。未编辑论文、旧笔记、旧论文或 math 源；本审查不负责 PDF 排版验收。

论文 68–82 行将 generic arithmetic/analytic/moment 输入、整个有限阶 Hecke 七分之八定理及二次转移明列为 \(\mathcal R\)。84–95 行的 \(\beta_*\) 包含 \(1/2\)、全族所有非平凡零点，明确排除主极点，并仅使用 \(\beta_*\le7/8\)。没有预设改进边界无零，也没有直接套用固定 \(b=1/8,\ell=1/6\) 的结论。最终 Theorem 1.1 是该输入包下的严格半平面命题。

## 2. 原物理对象和完整低侧

162–202 行给出同一原探针的独立物理定义。补偿子集 \(J\) 上的符号、\(q_{p_J}^{-3/2}\)、标记角色和 \(X,Y,Z\) 各自重标度正确；各槽窗口仍位于原 \(P_i\)。有限补偿展开与非有限的 completed sums 已明确区分。双留数的指数

\[
 C_b(s)=s+l_x/2-1+h/6=s-2/3-b/6
\]

和 Gaussian \(e^{(s-5/6)^2}\) 一直使用到最终 Mellin 比较，没有借另一归一化改善低侧。

204–331 行确实重证可变 \(b\) 的低侧，而非仅代入旧定理。逐 \(J\) 的 \(\ell'=\ell-d_J\)、\(M'=1-\ell-2d_J\)、\(M'+\ell'-1=-3d_J\) 正确；实际双长度满足 \(T_d\le H-3d_J+2\varepsilon_Z+|\theta_N|\)。反射式保留 \(s_{\rm hyb}\)、\(y_{\rm ref}\)、正部以及 frozen powerful part 的单次计数；\(s=z_a\) 与其余分支的 \(T_d/4\) 节省及 frozen-part 恒等式均一致。剩余标记为空的端点仍属于同一行能量输入。

关键的 Gram 第三项 \(P_a^2/Y'\) 没有遗漏。\(Q,Y'\ge1\)、固定多项式尺度及 \(P_a\ge1\) 在所述 \(1/6\le\ell\le1/5,\ 0<b\le3(1-\ell)/8\) 范围成立。总子集系数归结为

\[
 F(d)=-d+\tfrac12(11b/6-l_y+d)_+
                  +\tfrac18(5\ell-1+d)_+ .
\]

每段斜率至多 \(-3/8\)，故包括最坏负反射分支在内，最大值在 \(d=0\)。完整低指数为

\[
 \max\{(1-\ell)/4-b/6,b/2\}.
\]

所述范围选择第一支；论文没有错误将更强 all-subset Gram 条件当作必要条件，也不扩展到 \(b\le0\)。源的 reflected-energy、smooth separation、annular tails、ray/Gauss coefficient 和通用 additive Gram 估计仍是明确 [R]。

## 3. 连续证书、最优范围和有理见证

350–460 行的 \(D,P,J,R_*\) 与 endpoint 展开一致。清分母 \(-1296J E_\sigma=A\delta^2-B\delta+C\) 中 \(A,B,C\) 的所有系数、\(Q(0)\)、\(b_{\rm opt}\) 及最大 \(Q(0)\) 均与独立代数推导一致。

在 \(\ell_\circ=(33+8\sqrt{921})/1653\) 上，四个 \(A\) 系数均正；化约后的 \(Q_0=0\)、\(Q_1,\ldots,Q_4>0\) 从给定隔离区间严格推出。完成平方对整个连续矩形证明 \(E_\sigma\le0\)，并唯一允许 \(y=0,\delta=(49-\sqrt{921})/48\) 取等号；没有使用有限网格代替连续证明。

最优性仅针对固定 low intersection、相同 count envelope 和完整 amplitude rectangle。在固定等号点 \(R_*=2/3\)，endpoint 与 \(b\) 无关且随 \(\ell\) 严格增加，所以更大 \(\ell\) 不能全部非正。论文准确排除了“实际坏行达到 envelope”“存在相应零点”及“所有可能探针最优”的越界解释。

462–499 行的有理尺度及 \(\sigma_r=40773/46600\) 正确。通过 \(A_0Q-Q_0A\) 的非负系数比较后再使用 \(Q_0/A_0\)，没有错误地将 \(A(0)\) 当作 \(A(y)\) 上界。显示的严格统一 margin 和与 fixed-b critical 参数的隔离比较均成立。\(-9289/407167500\) 给出 \(\ell_r<\ell_\circ\)，因此有理值严格介于代数改进边界与旧 fixed-b critical 边界之间。

## 4. 实际 counts、全 d 和共用损失预算

501–597 行的原 unfactored 指数和一般 \(E_\sigma(d)\) 恒等式正确。初稿两处遗失的加号已经补齐。非 floor 行的正斜率允许 endpoint 控制 \(1/2\le d\le h\)；floor 与 no-slot middle 独立计算，不假设每一行都有 detector。五个严格几何/外行界与独立证书一致。

新的 \(\ell/(h+\zeta)>1/5>7/37\) 仅用作供槽准入，未冒充 moment theorem 本身。逆矩分支明确限制 \(r\ge r_*,r<1\)，plain 分支明确 \(r\le r_*,m<1/2\)，分别请求 \(z\le z_M-\nu_0\)、\(z\le z_P-\nu_0\)，因而两类 strict widths 为正。长 witness、zero-capacity、sixth-power cases、原 spike 大小、finite \(\Theta\) coefficients、共同 conjugation、原 inducing exceptions 和物理槽/pool disjointness 均保留。whole-slot rounding 在 mesh 先于 \(K\) 的选择顺序中支付。实际 detector/moment 输入本身仍属 [R]。

关键量词为先固定全族 \(\Delta=\beta_*-\sigma_\circ>0\)，再取 \(\zeta=\Delta/32\)。延长至 \(h+\zeta\) 至多损失 \(\Delta/16\)，而 \(E_{\beta_*}=E_{\sigma_\circ}-\Delta\)，所以零附加 endpoint margin 仍有共同严格节省。没有将 critical 等号误判为不能 continuation。

## 5. 完整 Euler tuple、轮廓和 principal 同源信号

599–695 行维持 coefficientwise selected-prime identity。完整 tuple 使用被选 \(G_p\) 和正常收敛的未选 product；没有除以任意局部 \(H_p\)。扩大 principal box 内 good/ramified 的所有显示 defect 为正，\(1-R,1-V,1-D\) 分母有界远离零；general good 项保留 \((-\Re w)_+\)，\(D_1\) 使用真实 \(\min(\varepsilon_0,1/50)\)。它们是全 height 正常收敛和 majorant 准入，不只是在单一点代入。

whole-bin global move 在局部标签切分之前，joint strict numerator/error estimate 仅计同一个 conductor deficit。最终 639–660 行明确

\[
 H_\eta(s)=\prod_{p\notin S}H_p(s,1,1/6)
            =\mathcal H_{\eta,1}(s,1,1/6),
\]

并使用相同 final \(S\)、physical expression、ray calibration、\(S_i,A_T,c_S\)。目标共同的 product majorant 支付 \(|H_\eta-1|\le1/2\)；最终 \(S\) 扩大只减小此 majorant。\(A_T\) 在大 \(Z\) 非零且逆为 subpower，适用于 \(J_\eta\) 的定义域。

principal 三类节省、局部四错误指数及 \(\mu<\sigma\min\ell_i\) 正确。small row 已相对于 \(C_b(\beta_*)\) 给界，不再误减一次 \(\Delta\)；其 \(D_1(1/3)\) 修补合法。large row 在固定 \(\zeta\) 后选择固定 \(z_\infty\)，没有随行或 \(Z\) 改动内部阶数。local arithmetic、prime asymptotics、buffered contours 和 absolute all-height tails 仍明确为 [R]。

## 6. 参数顺序与全族反证

697–791 行先 \(\Delta\)/真实 loss 和 decrement/mesh，再 even \(K\)，后 \(\mu\)，随后 target 与 final arithmetic datum。\(m_0,\omega\) 及最终 \(\varepsilon_*\) 都共同于尚未选定的 target；\(K\) 的选择不使用依赖 \(K\) 的 \(\mu\)。

\(J_\eta\) 只定义在足够大 \(Z\)，\(f_\eta\) 定义在正轴。二者不含 \(T_1\)。physical high 合同中 \(A_\eta,B_\eta\) 的内部阶数先于 external \(N\) 固定；先选小于 detector ceiling 的 \(\tau_\eta\)，后选 external \(N_\eta\)，从而得到 target-independent positive saving。\(T_1/2\) 的 cumulative allocation 保留。

显式 Mellin 变换在共同左移半平面局部一致收敛，并在初始线与 \(e^{(s-5/6)^2}H_\eta/L_F^S\) 识别。Gaussian 非零且 principal product 非零，排除 numerator cancellation。全族 supremum 无须达到；共同 \(\varepsilon_*>0\) 先于 target 选择，故可选择该线右侧的 target zero 得矛盾。没有跨 target 零点移 contour。有限 Euler 删除与二次 Dirichlet transfer 的结论范围正确，主极点和边界线均明确保留。

## 7. 最终结论

未发现最终冻结稿中阻断上述 **[T/R] 相对命题** 的错误或尚未列入 \(\mathcal R\) 的新前件。本审查对可变几何、显示代数、实际输入的重用域和量词顺序给出限定 PASS。原 imported arithmetic/analytic/moment 定理、全部 proof kernel 和无限运算不由 841 项有限精确代数检查认证；论文也没有声称 RH、RR 或新的简单临界线比例。
