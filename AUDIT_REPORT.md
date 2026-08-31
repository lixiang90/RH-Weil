# 黎曼猜想结构研究项目审计报告

> 审计日期：2026-08-31
> 审计对象：162 篇研究笔记、正式论文 `rh-weil-structure-paper.tex/.pdf`、数值与验证脚本
> 审计性质：数学逻辑、研究方向、证据边界与可复现性审计
> 结论等级：**研究纲领具有价值，但当前没有证明 RH，正式论文尚未达到完整可发表证明标准**

## 一、执行摘要

本项目试图从有限域 Weil 猜想的证明中抽取一套可迁移到数域的结构：

1. 迹公式或行列式把算术数据转换为谱或 divisor；
2. 函数方程提供中心对称；
3. 正极化、Hodge--Riemann 型符号约束或有限负指标阻止谱离开中心线；
4. 对 Riemann zeta，通过有限 Euler--Gamma 数据、Gram 载体、Abel current、prolate/Feshbach/Vaughan 通道寻找上述结构的数域实现。

总体判断如下：

- 项目**没有证明 RH**，论文对这一点的声明基本准确。
- 有限维正 similitude、幂迹判据、Feshbach--Loewner、有限迹负部对偶和 bounded-defect normality 等基础结果大体正确。
- `component compression no-free-lunch` 是有价值的反面结果：它正确说明低秩稳定性、小 tail 和小 coupling 不能替代独立的 core Hodge 约束。
- `filtered primitive Weil`（FPW）中心线定理存在一个实质性证明缺口：当前“可见性 + Mellin 唯一性”不足以推出所写的定量范数下界。
- 正式论文在 PLF 公理、tracial determinant 和 bounded-defect 的解析假设上压缩过度，不能脱离原始笔记独立核验。
- 数值脚本通过现有自检，但它们是有限浮点一致性检查，不是区间证书，也不提供 RH 证据。
- 研究已出现横向展开过多的问题：大量等价 kernel、Gram、capacity 和有限化判据没有改变最终缺口仍为 RH 强度算术估计这一事实。

建议暂停增加新的等价结构，集中修复 FPW 定理并提出一条可证伪、非循环、直接控制 core 的算术不等式。

## 二、审计范围与方法

### 2.1 审计范围

本次审计完成了以下工作：

- 盘点全部仓库文件及 162 篇笔记的主题映射；
- 阅读正式论文的完整证明主线和结论边界；
- 重点核查决定最终结论的原始笔记：001、002、058、073、077、131、145、149、150、158、161、162；
- 检查 PLF、tempered、FPW、tracial determinant、bounded finite-trace、square-root localization、Vaughan/Feshbach 和 no-free-lunch 依赖链；
- 运行仓库提供的三组主要数值/一致性测试；
- 对 Connes--Consani--Moscovici 的谱三元组路线和 Guth--Maynard 大值估计核对原始文献边界。

本报告不是对 162 篇笔记每一行计算的独立同行证明；它采用“结论依赖图审计”，优先核验承载最终结论的定理、桥接步骤和数值证据。

### 2.2 问题等级

| 等级 | 含义 |
|---|---|
| 严重 | 会使核心定理按当前表述无法成立或无法由所列公理推出 |
| 较严重 | 结论可能可修复，但正式论文缺少必要定义、假设或证明 |
| 中等 | 不一定改变结论，但影响独立核验、可复现性或研究效率 |
| 轻微 | 排版、符号、工程组织或表达问题 |

## 三、核心结论是否成立

### 3.1 当前不构成 RH 证明

论文明确承认尚缺以下任一输入：

- 实际算术向量的 subpower Hodge tightness；
- Abel Hodge current 的统一 Cauchy 加权负谱迹界；
- prolate 候选到真实最低态的统一谱隙/加权收敛桥；
- 冻结 Vaughan 通道上的非循环 core Hodge--Riemann 不等式。

这些输入中的任何一个若以论文要求的统一强度建立，都已经具有 RH 的全部或接近全部强度。因此项目目前是条件定理和存在性审计，而不是证明。

### 3.2 基础有限维结论大体正确

以下结果属于标准或可直接核验的谱论/线性代数：

- 正 similitude `h(Fx,Fy)=Qh(x,y)` 强制归一化算子酉，从而得到纯权谱；
- reciprocal pairing 加全部幂迹统一平方根界强制所有 reciprocal roots 位于同一圆周；
- `Theta*=c-Theta` 在正确的定义域假设下强制谱位于中心线；
- Feshbach--Loewner upper completion 的 Schur 补证明成立；
- effect cone 上 `inf tau(HE)=-tau(H_-)` 成立；
- component compression no-free-lunch 的 rank-one 反例成立。

这些结果的主要问题不是结论错误，而是它们多为“若存在所需结构则 RH”的充分条件；真正困难仍是从不使用零点位置的算术数据构造相应结构。

## 四、发现的数学错误与证明缺口

### 4.1 严重：FPW 定理缺少定量模式分离

正式论文在 `rh-weil-structure-paper.tex:278--298`，原始笔记在 `notes/058-filtered-primitive-weil-master-theorem.md:86--108`，声称：

> 可见性和 Mellin 唯一性阻止单个 `X^(rho-c/2)` 模态被其他指数完全消去，因此正 Gram 给出沿某子列的下界。

这一论证不足以推出

```text
Q_X(v_X) >= X^(2 Re(rho)-c-o(1)).
```

现有 FPW 公理没有明确给出：

- 不同 divisor modes 在 Gram 空间中的定量线性独立性；
- Riesz sequence 或 frame lower bound；
- 可隔离单个零点的对偶测试泛函及其范数控制；
- 对无限零点族和 `Re(rho)` 接近上确界时的统一性；
- 对允许随 `X` 变化的 subpower 乘子之间相消的排除。

“不对所有尺度恒等为零”只是一项定性唯一性结论，不能直接产生精确的幂指数范数下界。

#### 建议修复

增加定量 separation 公理。一个足够清晰的形式是：对每个固定 divisor point `rho`，存在对偶泛函 `ell_(X,rho)`，使

```text
||ell_(X,rho)||_(Q_X^*) = X^(o(1)),
|ell_(X,rho)(v_X)| = X^(Re(rho)-c/2+o(1)).
```

于是由对偶 Cauchy--Schwarz 才能严格得到

```text
Q_X(v_X) >= |ell_(X,rho)(v_X)|^2 / ||ell_(X,rho)||_(Q_X^*)^2.
```

在该条件建立前，应将 FPW exponent identity 和所有直接依赖它的结论标记为“条件性框架”，不宜称为已证明的总定理。

### 4.2 较严重：正式论文的 PLF 公理不足

正式论文 `rh-weil-structure-paper.tex:118--145` 只要求存在 primitive 分解和“Hodge 星型算子 `S_n`”，随后使用

```text
S_n F = q^(n-d) F S_n.
```

这个关系不能由正式论文列出的公理自动推出。

原始笔记 001 实际给出了必要定义：

```text
S_n(L^r u)=c_(a,r)L^(d-a-r)u,
```

其中 `u` primitive、`n=a+2r`。结合 `FL=qLF` 才能算出所需交换关系。

#### 建议修复

将原始笔记中的 `P^a`、primitive decomposition 和 `S_n` 的逐分量定义完整写入论文；同时说明常数 `c_(a,r)`、相位和 Hermite 对称性需要满足的条件。

### 4.3 较严重：tracial determinant 记号可能导致错误理解

正式论文 `rh-weil-structure-paper.tex:237--251` 使用

```text
Lambda(s)=E(s) det_tau(s-Theta)
```

并断言

```text
d/ds log det_tau(s-Theta)=tau((s-Theta)^(-1)).
```

如果 `det_tau` 按标准 Fuglede--Kadison determinant 理解，这一陈述是不正确的：Fuglede--Kadison determinant 通常是正实值对象，不是这里所需的全纯 divisor determinant。

原始笔记 077 实际采用的是“带 tracial exponents 的 Weierstrass 谱乘积”，并明确表示不与其他 determinant notions 混同。因此核心想法可以修复，但正式论文必须补充：

- determinant 的精确定义；
- 谱的局部有限性；
- heat/resolvent summability；
- canonical product 的 genus；
- polynomial counterterm；
- supertrace 或有符号次数的处理；
- 局部 order 公式的适用条件。

### 4.4 中等：bounded finite-trace 主定理在正式论文中假设不完整

正式论文 `rh-weil-structure-paper.tex:325--358` 只说 `F_n` 满足“由边界负部给出的 Poisson 下界”，没有在定理中列出准确不等式和边界条件。

原始笔记 145 给出了所需形式：

```text
Re F_n(x+iy)
>= -(1/pi) integral (x-delta_n) W_n(t)
   / ((x-delta_n)^2+(y-t)^2) dt,
```

其中 `W_n=[-Re F_n(delta_n+it)]_+`。

在明确的 Poisson admissibility、Euler 开集局部一致收敛和边界可积条件下，normal-family 证明基本成立。建议将这些条件纳入正式定理，而不是用“如上”或描述性语言代替。

### 4.5 中等：tempered 酉化证明的紧致性表述不严谨

正式论文使用 Cesaro metrics 并说“取收敛子列”。若定理 intended for 一般无限维 Hilbert 空间，算子单位球在通常算子范数下并不紧；应使用 weak-operator cluster subnet，或增加可分性并说明相应可度量紧性。

原始笔记 073 的有限维版本没有该问题，连续群版本也正确使用 weak-operator cluster point。正式论文应区分有限维和无限维表述。

### 4.6 轻微：LaTeX 公式转录错误

正式论文至少有以下反斜杠丢失：

- `rh-weil-structure-paper.tex:240`：`,qquad`；
- `rh-weil-structure-paper.tex:524`：`;qquad`；
- `rh-weil-structure-paper.tex:533`：`,quad`。

它们会被 LaTeX 当作连续数学变量输出，而不是间距命令。

## 五、研究方向审计

### 5.1 有价值的方向

以下思路值得保留：

1. **把正性与函数方程分开。** 项目正确认识到函数方程只能给对称，不能给中心线。
2. **强调全局结构。** 逐素数 local purity 不等于全局 Euler 乘积零点纯性，这一判断正确。
3. **主动审计循环性。** 项目多次指出从零点直接造 Hilbert 空间、抽象 exact passive realization 和全局 Weil form 正性都可能只是 RH 的重述。
4. **finite-trace negative mass。** 用 Cauchy capacity 代替最小特征值或逐点 Loewner 下界，在分析上是合理的范数选择。
5. **no-free-lunch。** 它有效阻止继续把有限低秩数值现象误认为 Hodge 正性。

### 5.2 当前偏差

主要偏差不是方向错误，而是研究资源过度分散：

- 162 篇笔记发展了过多相互等价的坐标和判据；
- 很多“压缩”只改变开放量的表达，没有降低其逻辑强度；
- finite-rank、prolate、capacity、passivity、Nyman 和 Vaughan 分支最终都回到同一个 actual arithmetic tightness；
- 数值上越来越小的 residual 或 Feshbach excess，没有形成对共尾极限的单调证书；
- 最新 no-free-lunch 已经说明继续优化二维 basis 不会解决决定性的 core amplification。

因此项目存在“横向展开过多、纵向突破不足”的倾向。

### 5.3 bounded negative trace 的真实地位

`O(1)` negative Cauchy mass 确实弱于逐点 positivity，但项目自己已证明：对相应 Euler candidates，这个统一界仍足以推出 RH；若 RH 为假，它必须共尾发散。

所以它是一个更柔性的**等强充分条件**，目前还不能断言它在算术上更容易。要证明方向确实前进，必须展示一种现有解析数论工具能够控制 negative capacity、但不能控制逐点负深度的具体机制。

### 5.4 prolate/谱三元组路线

外部文献支持以下边界：

- 有限自伴算子和实零整函数构造存在；
- 低零点逼近具有很高数值精度；
- 严格收敛若成立将推出 RH；
- 尚缺最低特征值 simple-even 和真实最低态与 prolate 候选的足够强逼近。

参考：

- A. Connes, C. Consani, H. Moscovici, [Zeta Spectral Triples](https://arxiv.org/abs/2511.22755)；
- A. Connes, C. Consani, H. Moscovici, [Zeta zeros and prolate wave operators](https://arxiv.org/abs/2310.18423)。

本项目的 residual 数值工作与该研究议程一致，但目前没有解决上述两个统一极限缺口。

### 5.5 Vaughan/Feshbach 路线

冻结 incidence basis、exact channel factorization 和 held-out 数值检查是合格的结构发现。问题在于 core channels 仍显式包含完整 `Lambda`，直接估计它们可能把目标原样放回右端。

因此下一步必须是一条新的算术 signature relation，而不是：

- 继续优化 cutoff；
- 继续降低有限 Feshbach excess；
- 继续寻找更接近 physical direction 的二维平面；
- 只证明 tail residual 小。

## 六、建议的更优研究计划

### 第一优先级：修复可发表的核心定理

建议把现有工作拆成一篇较短、自足的分析论文，集中于：

1. bounded-defect normality theorem；
2. finite-trace effect duality；
3. zeta Abel candidate 的准确构造；
4. square-root Cauchy-core localization；
5. 所有常数、截断和 Poisson admissibility 的完整证明。

这是项目中最接近独立数学成果的一条主线。

### 第二优先级：修复或降级 FPW

二选一：

- 建立定量 divisor-mode separation/Riesz lower bound，使 FPW theorem 真正成立；
- 或把 FPW 改写为研究框架和定义，不再声称 exponent identity 已由现有弱公理证明。

### 第三优先级：提出可证伪的 core 不等式

候选不等式必须直接控制 `PGe`、core signature 或 negative trace，并满足：

- 左右两端均由 primes、Gamma、continuum、Möbius/Vaughan 数据定义；
- 不引用零点位置、`Xi'/Xi` 无极点或 Weil form 全局正性；
- 在简单有限域或函数域模型中能还原已知 Hodge index；
- 对 rank-one core amplification 给出明确禁止机制。

### 第四优先级：先做平均版本

如果 individual zeta 的统一界过强，可先研究：

- primitive Dirichlet characters 按 conductor 的平均 negative trace；
- 高度区间平均；
- 函数域或有限图模型；
- 在已知 zero-density 假设下的定量 defect 上界。

这可以检验 finite-trace 架构是否真的比逐点 positivity 更适合大筛与大值估计。

Guth--Maynard 的 Dirichlet polynomial 大值估计是潜在工具，但其已发表结论并不自动包含本项目要求的 Abel 权、全 dyadic centers 和 Cauchy 可和性：

- L. Guth, J. Maynard, [New large value estimates for Dirichlet polynomials](https://annals.math.princeton.edu/2026/203-2/p06)。

相关转换必须作为新定理单独证明。

### 第五优先级：建立停止规则

建议为后续分支设定明确门槛：

- 新 kernel 必须给出比已有形式更强的可证明 bound，而不仅是等价改写；
- 新有限模型必须产生共尾可控量，而不仅是固定参数数值改善；
- 新 basis 必须来自解析主项或算术恒等式，而不仅是数据拟合；
- 若一个方向经 no-go 证明不能控制 core，应停止继续优化该方向。

## 七、数值和脚本审计

### 7.1 实际运行结果

本次审计运行了：

```text
python scripts/test_qw_bounds.py
```

结果：

```text
QW formula, row-tail, and candidate-tail sanity checks passed.
```

运行：

```text
python scripts/test_prolate_candidate.py
```

结果：

```text
Prolate boundary-correction sanity checks passed.
```

运行：

```text
python scripts/audit_vaughan_laurent_channels.py --frozen-test
```

结果：完成且无断言失败。冻结 tilted basis 在两个 `N=320` held-out blocks 上的 standardized excess 分别约为 `.139%` 和 `.0667%`，与笔记 161 一致。

### 7.2 数值证据的合法解释

这些结果支持：

- 代码实现内部的有限恒等式一致；
- 所给解析 majorant 在抽样参数下没有被反例击穿；
- prolate 修正满足预定的有限精度约束；
- frozen channel 的有限 Loewner majorant 与记录数据一致。

它们不支持：

- 无限维或共尾极限；
- uniform spectral gap；
- interval-certified positivity；
- 全部 dyadic heights 的可和性；
- RH 的统计或数值证据。

脚本自身明确写有“sanity checks”“not an interval certificate”“not evidence for RH”，这一证据边界是正确的。

### 7.3 工程与可复现性问题

1. `scripts/qw_matrix.py` 超过 16,000 行，包含大量不同研究分支，维护和独立审查困难。
2. 缺少依赖锁定文件，例如 `requirements.txt`、`pyproject.toml` 或环境说明。
3. 缺少统一测试命令和 CI。
4. 多数测试属于同一实现内部的回归，并非两套独立算法的交叉验证。
5. 关键数值未使用 interval arithmetic。
6. 缺少固定格式的机器可读实验输出和误差预算文件。

#### 建议模块划分

```text
scripts/
  weil_matrix/
  abel_current/
  prolate/
  vaughan_channels/
  nyman_capacity/
  interval_certificates/
  tests/
```

每个模块应分别标明：exact algebra、proved analytic bound、floating diagnostic、interval certificate。

## 八、论文结构与表达建议

### 8.1 拆分文档

建议形成三层文档：

1. **正式论文**：只保留自足且完整证明的 4--8 个核心定理；
2. **研究纲领/路线图**：FPW、Hodge analogies、open problems 和 no-go；
3. **实验附录**：全部有限矩阵、参数表和脚本说明。

### 8.2 统一状态标签

每个定理或命题应标记为：

- `[U]` 无条件已证明；
- `[C]` 条件定理；
- `[E]` 与 RH/GRH 等价；
- `[N]` 数值诊断；
- `[H]` 启发式或研究猜想。

### 8.3 明确新旧结果

需要逐条区分：

- 标准谱论或经典显式公式的重述；
- 外部论文已有结论；
- 本项目新证明；
- 由已有定理直接推出的推论；
- 尚未同行核验的内部笔记结论。

### 8.4 降低术语密度

目前大量新名称容易让等价改写显得像多个独立突破。建议围绕少数固定对象组织全文：

- divisor/logarithmic derivative；
- arithmetic candidate；
- Hodge/Gram form；
- negative Cauchy mass；
- core/tail decomposition；
- noncircular core inequality。

## 九、整改优先级清单

### 必须完成

- [ ] 修复 FPW 定量下界或将其降级为条件性框架；
- [ ] 补全正式论文中的 PLF primitive star 定义；
- [ ] 明确定义 tracial spectral determinant；
- [ ] 把完整 Poisson admissibility 写入 bounded-defect 主定理；
- [ ] 修复 LaTeX 中 `qquad/quad` 转录错误；
- [ ] 将“所有结构定理均严格证明”的表述改为分级状态说明。

### 建议完成

- [ ] 将 square-root localization 整理成自足证明；
- [ ] 给出全部关键常数和 uniformity 量词；
- [ ] 拆分 `qw_matrix.py`；
- [ ] 添加依赖锁定、测试入口和 CI；
- [ ] 为关键有限证书增加 interval arithmetic；
- [ ] 邀请至少一名解析数论专家和一名算子代数/谱论专家独立审阅。

### 暂停事项

- [ ] 暂停增加新的等价 kernel 或 Gram 名称；
- [ ] 暂停仅以更小有限 residual/excess 为目标的参数优化；
- [ ] 暂停没有解析来源的新经验 basis 搜索；
- [ ] 在 core inequality 明确前，不将有限通道稳定性描述为接近 RH 证明。

## 十、最终评价

本项目最重要的贡献不是证明了 RH，而是形成了较为成熟的逻辑防线：

- 知道函数方程、局部纯性和有限数值逼近为什么不够；
- 知道抽象 Hilbert--Pólya 存在性可能循环；
- 知道正 Gram 载体不等于实际算术向量 tightness；
- 知道 tail/coupling compression 不能免费产生 core Hodge 正性。

这是研究上的真实进展。但从证明角度看，项目仍缺两项决定性工作：

1. 一个严格的 divisor-mode 定量分离机制，以修复 FPW；
2. 一条由 primes/Gamma/Möbius 等算术数据产生、能够禁止 core rank-one amplification 的非循环 Hodge relation。

在完成这两项之前，最准确的成果定位是：

> **一个系统的 Weil--RH 结构研究纲领、存在性边界审计、有限化工具箱和失败机制集合。**

它可以成为后续研究的坚实基础，但不应被表述为已经完成的数域 Weil 理论或 RH 证明。
