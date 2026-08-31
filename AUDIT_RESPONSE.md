# 审计整改说明

日期：2026-08-31
对象：`AUDIT_REPORT.md` 对原 001--162 篇研究笔记、正式论文及计算脚本的审计；后续整改结果见新增文档 163

本文件记录已经落地的修改、仍属开放的数学输入，以及暂缓的工程事项。它不是对审计意见的反驳，也不是 RH/GRH 证明声明。

## 已完成的数学整改

| 审计项 | 调整 | 当前边界 |
|---|---|---|
| FPW 从定性 visibility 跳到 Hodge 范数幂次下界 | 将 FPW4 拆为定性 divisor compatibility 与定量 FPW4b；FPW4b 只要求受控对偶泛函的 dual norm 为 `X^(o(1))`，且在实际向量上的取值至少为 `X^(Re(rho)-c/2-o(1))`。文档 163 对 Mellin-coherent fixed-annulus Sobolev carrier 显式构造 compact-frequency dual，以 Mellin pole 横坐标和 dual Cauchy--Schwarz证明下界，并给有限 Schur margin 公式。 | adaptive Sobolev carrier 的 FPW4b 已标为 `[U]`；rank-one annular 模型也有独立证明。任意 scale-varying Gram 仍不自动满足 FPW4b，actual-cycle tightness 仍未证且与 RH 同强。 |
| PLF 定义不够完整 | 在论文中显式加入 primitive 子空间 `P^a`、Lefschetz 直和分解、primitive star 映射与 Hermitian 正定公理。 | 有限维 PLF 蕴含在所列公理下标为 `[U]`；这些公理对数域 zeta 的自然存在性仍开放。 |
| tracial determinant 概念混用 | 明确排除 Fuglede--Kadison determinant，改用带 graded trace 指数的 Weierstrass 谱乘积；写明局部有限性、genus summability、正规化多项式和 regularized resolvent trace。 | 该谱乘积定理对 zeta 的应用仍需谱实现与 adjoint symmetry，标为 `[C]`。 |
| bounded finite-trace 定理遗漏 Poisson 假设 | 显式定义边界负部 `W_n`、Cauchy 质量 `J_n`，并把完整 Poisson admissibility 不等式列为主定理的首项假设。 | 结构蕴含严格；zeta 所需统一负谱迹界仍是 RH 强度输入。 |
| tempered 证明混用有限维与无限维紧性 | 有限维定理只使用范数紧性；无限维一致有界群另用 Cesàro 平均和 weak-operator cluster subnet，并单独说明 resolvent/Laplace 谱结论。 | 不再用有限维紧性替代无限维论证。 |
| 状态与证据边界不清 | 论文统一加入 `[U]/[C]/[E]/[N]/[R]` 标签，并在摘要、引言、存在性表和结论中明确“本文未证明 RH/GRH，内部新结果仍待独立核验”。 | 浮点实验仅为 `[N]` 诊断，不作为渐近定理或 RH 证据。 |
| LaTeX 与措辞问题 | 修复 `quad/qquad` 类排版错误、canonical product 写法和一处 `rho` 断行；将“FPW 总定理”改为“FPW 条件框架”，删除结论中的过强概括。 | 最终以 XeLaTeX 双遍编译检查。 |

## 已完成的复现整改

- 新增 `requirements.txt`，固定当前脚本所需的 NumPy 与 mpmath 主版本范围。
- 新增 `scripts/run_checks.py`，统一运行 Mellin dual、prolate、QW bounds 与 Vaughan Laurent frozen tests。
- 新增 `.github/workflows/tests.yml`，在 Python 3.11 上安装依赖并运行统一检查。
- `.gitignore` 仅排除 LaTeX 中间产物、Python cache、编辑器元数据和本地秘密；最终 PDF 不被忽略。

这些检查验证恒等式、数值回归和已冻结样例，不提供 interval-certified 证明，也不验证 RH。

## 明确延期的项目

1. 将大型 `scripts/qw_matrix.py` 拆成更小模块：改动面大，先保持审计后的数学接口稳定，再单独重构。
2. 把关键浮点证书迁移为 interval arithmetic / exact rational enclosure：列为下一阶段的严格认证任务。
3. 对论文中的内部新定理进行独立同行复核，并逐条补齐可公开引用的外部文献证据。
4. 把文档 163 的 Mellin-coherent dual 机制推广到其他有共同 Dirichlet-series realization 的 carriers；对仅有 additive actual-energy approximation 的 sampled/moment Gram，不虚构全空间 FPW4b。
5. 文档 164 已把四分量压成 canonical 二通道并无条件消去 `n<=T/log^A T`。文档 165 的 Hadamard 正规形进一步证明：把“完整 hard cross Gram 加 primitive energy”列为独立较弱目标是循环的；文档 166 转而把 truncated Möbius defect 构造成 zeros-independent 的 threshold-complex Hodge heat supertrace，并给出 boundary shell 与 positive gcd-Gram 二阶矩。仍需证明该 signed complex 与 modulated interval incidence 的统一 finite-index compatibility。

## 研究方向调整

暂停继续堆叠等价 kernel、basis tuning 和未经认证的浮点搜索。近期优先级为：

1. 把文档 166 的 reduced divisor complexes、Hodge Laplacians 与 logarithmic translations组成 matrix-valued superconnection current，并证明 harmonic boundary classes 的调制 finite-trace预算；
2. 把可行的有限证书升级为 interval-certified enclosure；
3. 仅在有共同 Mellin realization 时推广 quantitative dual separation；
4. 独立复核后再扩大“已证明”范围。
