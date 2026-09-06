# 独立复核：306 谱证书与同范数例子

审查者：只读子代理 Pauli；日期：2026-09-06。审查后尚有明确整改项，不能仅按通过摘要验收。以下保留返回报告；原行号对应审查时工作树，后续修订可能改变。

**审查结论：四次有限证书、两种渐近分支及 65/66 维修正均成立，未发现推翻这些核心结论的反例。但下游调用仍有遗漏，notes202 的紧致性证明也有一处需要补写的有限层步骤。**

以下可直接存档。本次只执行读取和内存计算，未修改仓库文件、commit 或 push；既有审查结果未作为证明前提。基线 HEAD 为 `483ded56401cd174252ef630ed22dd4ab86956ad`，审查对象包含当前未提交修订。

1. **[P2] 下游一侧调用尚未完全迁移，渐近常数也不能直接写成有限界。**

   [部分配置论文](/F:/codex-build/RH/RH-Weil/papers/partial-weil-configurations-paper.tex:1452) 的 MT 实例，以及 `prop:fourth-ledger`，仍引用要求第四矩存在极限的 `thm:quartic`；其实际前件只给第四矩上界。应改用 `cor:quartic-upper`，并明确继承同一配置的
   \[
   m_0,m_1\to1,\qquad E_1/N\to0.
   \]
   `prop:fourth-ledger` 当前没有自行列出这些条件。既定 AF 构造可以另行提供它们，但它们不是所列第四矩预算的推论。

   一个说明遗漏实质性的抽象反例：采用 note306 的 42 维四原子谱，却改取
   \[
   P=0,\quad Q=G,\quad N=42,\quad s=0,\quad b=D=37,\quad E_0=E_1=32.
   \]
   这仍是合法有限配置，且
   \[
   (m_0,\ldots,m_4)=(1,1,4/3,2,13/4).
   \]
   甚至形式预算 \(D_{22}=4/15,\ O_{22}=-1/60\)、其余为零，满足该命题所列的数值上界，但 \(s/N=0\)。因此必须保留小边界前件。**这不是实际 zeta 配置的反例，而是对“所列矩条件已经充分”的反例。**

   此外，`eq:conditional-mt-quartic` 应写成 \(\liminf\) 下界，或保留 \(-o(1)\)。这个区别不能省略：将 \(k\) 个 note306 的极端块与一个二阶尖锐块直和，得到
   \[
   N=42k+6,\quad s=32k+4,\quad b=5k+1,\quad D=37k+5,\quad E_1=0.
   \]
   所需矩趋于目标四矩，但每个有限 \(k\) 都有
   \[
   \frac{s}{N}-\frac{16}{21}=-\frac{2}{21(7k+1)}<0,\qquad
   \frac DN-\frac{37}{42}=-\frac1{21(7k+1)}<0.
   \]

2. **[P2，可在现有假设内修补] AEJ 的近似正性不能直接给精确 Cauchy–Schwarz 界。**

   [notes202 的证明](/F:/codex-build/RH/RH-Weil/notes/202-archimedean-localizing-weil-completion.md:170) 与[结构论文对应证明](/F:/codex-build/RH/RH-Weil/papers/rh-weil-structure-paper.tex:425) 直接使用
   \[
   |L(a)|\le R_a
   \]
   将有限近似泛函放入紧圆盘。然而有限层只要求 Gram 矩阵半正定到误差 \(1/n\)。

   例如 \(x=x^*,x^2=1,R_x=1\)，取
   \[
   L(1)=L(x^2)=1,\qquad L(x)=1+\varepsilon.
   \]
   对 \(\{1,x\}\) 的 Gram 矩阵，其特征值为 \(2+\varepsilon,-\varepsilon\)，而 \(L(1-x^2)=0\)。它满足这一有限组的近似约束，却有 \(|L(x)|>R_x\)。

   正确补法是：在逐渐扩大的有限约束集中，同时加入每个坐标的 Gram 约束和 Archimedean 约束。按 Hermitian Gram 约定，
   \[
   |L(a)|^2\le(1+\varepsilon)\bigl(L(a^*a)+\varepsilon\bigr)
   \le(1+\varepsilon)(R_a^2+2\varepsilon).
   \]
   先用较大的固定圆盘取得紧致性，再令误差趋零。此后全部 localizer 正性及 GNS 有界性可正常推出。**这是现有证明的缺步，不是 AEJ 定理的反例，也不影响 65/66 维算例。**

3. **核心四次证明已独立核验。**

   完整阅读了 [note306](/F:/codex-build/RH/RH-Weil/notes/306-quartic-boundary-and-equal-norm-corrections.md)，并核验 `lem:deletion`、`lem:quartic-finite`、`thm:quartic`、`cor:quartic-upper`：

   - 谱删除的必要性可由最小最大原理得到
     \(\lambda_{i+\lfloor b\rfloor}(G)\le\lambda_i(P)\)；正尾谱的个数与和分别受秩、迹控制。充分性由谱基中的截取构造得到，不要求 \(P,Q\) 对易。
   - 三条标量不等式、\(L\) 的展开和 \(\Delta_\sigma\) 系数正确。两条有限界分别支付 \(4ae\) 和 \((3+\sigma)ae\)，互异界没有使用错误的 \(D\ge(N+s)/2\)。
   - \(b_4\le b_2\) 时固定 \(\sigma_*\) 后取极限合法，且 \(r_{\sigma_*}=R\)。
   - \(b_4>b_2\) 时，由
     \[
     4\operatorname{tr}G-\operatorname{tr}G^2\le3s+4b
     \]
     与同一 \(E_1\) 账本，确实得到更强的 \(1-b_2\)、\(1-b_2/2\)。无需把 \(\sigma_*<-3\) 代回四次账本。
   - 一侧版本的第四矩系数为负，证明成立；不需要第三矩独立收敛。
   - 42 维极端配置满足全部秩、迹、惯性及边界条件，确实实现 \(16/21,37/42\) 的取等。

   一个低优先级书写问题：`lem:deletion` 自身的 Weyl 下标还应统一写成整数预算，并单列 \(b\ge d\) 的平凡情形。后续有限引理已经说明取 \(\lfloor b\rfloor\)，所以不影响核心结论。

4. **65/66 维范数、矩及 localizer 修复正确。**

   对原始谱直接求和，并独立构造 localizer，结果为：

   | 项目 | 65 维原例 | 66 维扩张 |
   |---|---:|---:|
   | \(\|H_+\|,\|H_-\|\) | \(1,\ 4/5\) | \(1,\ 1\) |
   | 负谱比例 | \(1/65\) | \(1/66\) |
   | 一阶 localizer 行列式 | \(1104/105625\) | \(7/605\) |
   | \(\int xp(x)^2\,d\mu_-\) | \(-9/8125\) | \(-6/6875\) |

   66 维共同矩确为
   \[
   \left(1,\frac6{11},\frac{19}{55},\frac6{25},\frac{247}{1375}\right).
   \]
   新增原子贡献 \(p(1)^2=9/625\)，重新归一化后负方向仍保留。

   注意：二阶 localizer 使用到第五矩，因为 \(\deg(xp^2)=5\)，所以它能区分这两个实现，与前四矩不可区分并不矛盾。反例排除的是“由这些数据强制原算子正性”；它不排除存在正实现——\(H_+\) 本身就是正实现。

5. **脚本覆盖与下游边界。**

   [quartic_boundary_certificate.py](/F:/codex-build/RH/RH-Weil/scripts/quartic_boundary_certificate.py:66) 的声称与实际执行范围基本一致：双变量系数恒等式、13,965 项有理回归、漏 \(E_1\) 反例和极端矩均通过。

   13,965 项具体来自三维对角谱、七种原子、整数删除预算、三种 \(N\) 和五种参数；不覆盖一般非对易谱删除证明、负参数分支的渐近论证或任意选点过程。它也未单独以符号方式认证 \(\Delta_\sigma\) 展开；本次已独立完成该项。

   我另做了 **540 项精确有理检查**：90 个配置、维数 1–5，其中 58 个满足 \(PQ\ne QP\)，并包含分数预算及额外边界余量。全部满足两条有限界。[operator_fourth_localizer_audit.py](/F:/codex-build/RH/RH-Weil/scripts/operator_fourth_localizer_audit.py) 也实际运行通过。

   notes228 的 padded 账本在渐近层面可以接入，但应明确先对 \(J_u'\) 的计数应用证书，再使用
   \[
   |S(J_u')-S(J_u)|,\ |D(J_u')-D(J_u)|
   \le N(J_u'\setminus J_u)=o(N).
   \]
   不能在有限层只支付 \(E_1\)，就把 padded 的 \(s,D\) 当作主块计数。AF 原文的单原子迹界与块结构支持这个接口。[AF，Lemma 2.1、Proposition 4.1](https://arxiv.org/html/2608.13637v2#S4)

**未覆盖项：**实际 MT 合并有符号第四矩预算、fixed-power high-product 算术缺口、PLF 与状态迁移、完整 RH/localizer 算术实现、正式化证明及排版编译。对 note304 仅核验了其依赖二阶谱余项、未调用本次四矩渐近定理；没有重新认证其完整三点与算术证明。
