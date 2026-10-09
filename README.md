# RH-Weil：从 Weil 猜想类比研究黎曼猜想

本项目研究：能否从素数、显式公式与数域几何自然构造一种 Weil 型结构，使黎曼 zeta 函数及相关 L 函数的零点被迫位于中心线？仓库保存结构归约、实际算术模型、机制障碍、形式化蓝图和可复现的有限检查。

**完整黎曼猜想尚未证明。** 当前成果分别有明确的适用范围；抽象存在性判据、有限数值、条件推论和引用外部结果的证明均单独标记。

## 研究问题

有限域上的 Weil 机制把迹公式、Frobenius、Lefschetz 分解及 Hodge–Riemann 正性连接起来，约束特征值的绝对值。本项目尝试把这些关系转移到数域：构造算术来源、对应与周期读出，并证明足以产生中心线结论的正性或存在性。

难点是提供来源明确、没有预先使用零点位置的算术结构。仅假设一个具有所需谱的正结构存在，可能已经与 RH 等价。F₁ 路线目前还缺完整的算术比较、主关系、全局 Weil 正性及 Riemann–Roch 实现；比例路线还缺同一物理响应中的充分四阶算术节省。

初读建议从 [本科背景讲义](docs/f1-route-from-undergraduate-math.md) 开始，再看 [研究分支看板](RESEARCH_BRANCHES.md) 与 [几何实现蓝图](formal/blueprint/geometric-realization.md)。

## 成果与论文

研究材料主要包括三类：Weil 型结构的严格蕴含与存在性审计；真实局部算术、算子和截止上的构造及障碍；部分中心线比例与无零区域的估计接口。各论文整理的范围小于全部研究笔记，证明状态以正文和审查记录为准。

| 论文 | 源文件与 PDF | 范围与状态 |
|---|---|---|
| 从 Weil 猜想到数域中心线 | [TeX](papers/rh-weil-structure-paper.tex) · [PDF](output/pdf/rh-weil-structure-paper.pdf) | 极化、过滤 Hodge 结构及存在性审计；数域目标结构的完整实现仍开放。 |
| 部分 Weil 配置 | [TeX](papers/partial-weil-configurations-paper.tex) · [PDF](output/pdf/partial-weil-configurations-paper.pdf) | 二阶、四阶预算与中心线比例接口；保留实际四阶输入的条件性。 |
| Abel 质量预算障碍 | [TeX](papers/abel-mass-obstruction-paper.tex) · [PDF](output/pdf/abel-mass-obstruction-paper.pdf) | 实际 von Mangoldt／连续 Abel 源上的响应下界与指定预算障碍。 |
| 严格边界 `69999/80000` | [TeX](papers/seven-eighths-boundary-improvement-paper.tex) · [PDF](output/pdf/seven-eighths-boundary-improvement-paper.pdf) | **cited-input derivation（引用输入下的推导）**。给出正文指定 L 函数族的严格无零半平面。 |
| 自由 b 的临界边界 | [TeX](papers/free-b-compensated-probe-boundary-paper.tex) · [PDF](output/pdf/free-b-compensated-probe-boundary-paper.pdf) | **引用输入下的推导**。优化补偿几何，严格边界为 `(1507−2√921)/1653 ≈ 0.874957069799`；最优性限于正文指定接口。 |
| κ 反馈的三次边界 | [TeX](papers/kappa-feedback-cubic-boundary-paper.tex) · [PDF](output/pdf/kappa-feedback-cubic-boundary-paper.pdf) | **引用输入下的推导**。重证 plain moment 范围并支付实际参数反馈，严格边界 σ*≈0.874957019420099。 |
| 简单临界线零点的无损八点装配 | [TeX](papers/lossless-eight-point-simple-critical-paper.tex) · [PDF](output/pdf/lossless-eight-point-simple-critical-paper.pdf) | 简单临界线比例下界 `66812491/99194997 ≈ 67.3546983423%`。无条件相关输入、已准入连续八点证书与新 majorant 的组合；计算信任范围在正文明确。 |
| 九点共享核值与简单临界线零点 | [TeX](papers/nine-point-joint-minorant-simple-critical-paper.tex) · [PDF](output/pdf/nine-point-joint-minorant-simple-critical-paper.pdf) | 比例下界提高至 `66812491/99194897 ≈ 67.3547662437%`。完整低集覆盖与289份精确有理对偶；保留原PC8连续与计算准入范围，非全链Lean内核证明。 |
| 原点表切线与扩大九点证书 | [TeX](papers/expanded-nine-point-tangent-simple-critical-paper.tex) · [PDF](output/pdf/expanded-nine-point-tangent-simple-critical-paper.pdf) | 当前简单临界线比例下界 `66812491/99194740 ≈ 67.3548728491%`。241胞完整覆盖、2399份精确对偶；独立仓库已核验完整模块化 Lean 证明，信任范围在正文明确。 |

三篇无零边界稿引用固定二次域全 Hecke `7/8` 结果及明确列出的通用引理，研究补偿几何、真实 moment 的可用范围和参数反馈。最新稿给出指定三次根的严格边界 `σ* ≈ 0.874957019420099`。正文重证相应几何、全部物理范围与全族延拓；结论覆盖指定有限阶 Hecke 族、Dirichlet 族及 zeta，允许主极点并排除边界线。这些论文的交付版本没有独立重证外部整篇论文或改善简单临界线比例。现已在独立仓库核验其核心代数、反馈费用及通用延拓归约；完整算术输入的 Lean 实现仍开放。引用前件、连续证明、有限代数检查及独立审查分列，入口见 [论文目录](papers/README.md)。

比例论文保留全部线外零点和重数，把近对与分离集的能量无损转入实际计数。有限证书、完整解析证明和独立审查分别记录；没有宣称整条结论已获得 Lean 内核认证或外部同行评审。

零点比例的新Lean形式化、内核证书与网站提交记录集中维护在独立仓库
[RH-Zero-Proportion-Formalization](https://github.com/lixiang90/RH-Zero-Proportion-Formalization)。
本仓库继续保存对应论文与研究历史；新仓库按riemannzeta.fun的固定Lean／Mathlib合同构建，
独立仓库已通过完整模块化证明、单文件 Lean 编译及独立内核重放，署名为 Li Xiang（lixiang90）。网站的完整资源约束与正式验收仍待完成，尚未获得网站记录；提交工程期间继续暂停新的数学研究。

非零区域的新增形式化另行维护于
[RH-Zero-Free-Formalization](https://github.com/lixiang90/RH-Zero-Free-Formalization)，
并归档三篇无零边界论文的 TeX／PDF。最佳边界 σ*≈0.874957019420099 的三次根、
连续证书、真实参数反馈、高度截断闭合及实际 zeta 的逆 Mellin 主信号已通过完整构建与 224 个公开定理的传递公理审查；
独立串行 Nano 内核重放通过 58,126 个声明。主信号的局部可积性、原点快速衰减、去极点、Mellin 恒等式及最佳参数下的复数幂归一化已补齐。
实际算术的 27 个扩展模块、88 个声明已另行通过 Lean 与独立内核核验，涵盖 slot／Euler／主项、素数 normalizer、实际 source Batch 构造、移动 κ 的 marked 容量准入及固定有限源族的 marked 上界；低 κ 完整能量归纳、终端证书及先于所有角色的统一次数也已完成独立回放。验证范围与保留前提见独立仓库的[算术接口说明](https://github.com/lixiang90/RH-Zero-Free-Formalization/blob/main/upstream/plain-kappa/README.md)。
**完整最佳无零区域的算术形式化尚未完成**：实际 zeta 定理仍显式需要
`ArithmeticProbeObligation`，即算术修正因子与物理探针的低频／原始高频估计；完整 marked moments、改进 detector count、可变几何下的反射能量及全 Hecke 族结论的实例化等缺口
列于新仓库[证明状态](https://github.com/lixiang90/RH-Zero-Free-Formalization/blob/main/docs/proof-status.md)。
本仓库继续保存论文和研究历史，新增形式化代码集中放在独立仓库。

## 如何阅读证据

| 标记 | 含义 |
|---|---|
| `[T]` / 历史 `[U]` | 正文给出证明的命题／历史无条件结论；须按其对象、量词、引用输入及审查范围阅读。 |
| `[C]` | 条件性结论；前件必须另行实现或证明。 |
| `[R]` | 引用外部结果；必须核对具体版本、原始声明和全部适用前件。 |
| `[E]` | 有限计算、模型或实验；是否为精确或区间证书由自身报告说明，不能推出无限域或渐近结论。 |
| `[N]` | 指定机制或模型的严格障碍／反例；其范围不自动扩展到 RH。 |
| `[O]` | 尚未完成的研究输入、比较或验证。 |

内部独立复核与外部同行评审是不同记录。`[R]` 也不表示本项目完成了引用文献的全部证明认证。历史文档按其原有标记约定保留；例如部分早期文档用 `[E]` 标记等价性。解释优先查相应正文、[文献与证据边界](notes/003-sources.md) 和 [原始文献索引](literature/README.md)。

Lean 状态另外区分 `proved`、`classical_sorry`、`depends_on_sorry` 和 `open_research_input`。构建成功允许已登记的 `sorry`，因此必须连同传递公理输出检查；当前蓝图仍含明确登记的经典缺口及未实现的研究条件。入口见 [形式化说明](formal/README.md)、[声明缺口账本](formal/blueprint/README.md) 和 [实际验证记录](formal/checks/README.md)。

## 仓库导览

| 入口 | 内容 |
|---|---|
| [RESEARCH_BRANCHES.md](RESEARCH_BRANCHES.md) | 当前队列、最小开放输入及停止条件。 |
| [notes/](notes/) | 完整编号研究笔记；论文未覆盖的证明和失败机制也在这里。 |
| [papers/](papers/README.md) / [output/pdf/](output/pdf/) | 项目论文源文件、编译说明及生成 PDF。 |
| [formal/](formal/README.md) | 固定 Lean／mathlib 版本的源码、蓝图、admission 与验证日志。 |
| [零点比例形式化](https://github.com/lixiang90/RH-Zero-Proportion-Formalization) | 独立仓库：新增比例证明、内核证书及正式记录提交。 |
| [非零区域形式化](https://github.com/lixiang90/RH-Zero-Free-Formalization) | 独立仓库：最佳三次边界证书、反馈、高度闭合与实际 zeta 逆 Mellin 主信号；完整算术证明仍开放。 |
| [literature/](literature/README.md) | 固定版本的外部原始文献、来源与核读范围。 |
| [reviews/](reviews/) | 独立审查、精确审计和后续证明任务。 |
| [scripts/](scripts/) | 注册的有限检查、证书和探索计算；[requirements.txt](requirements.txt) 固定基本 Python 依赖范围。 |
| [goals/](goals/README.md) | 长期研究目标、任务单与进展账本。 |

## 使用与验证

从仓库根目录运行 Python 3.10+ 命令：

```powershell
python -m pip install -r requirements.txt
python scripts/check_repo_layout.py
python scripts/run_checks.py --group core
```

目录检查只验证文件布局和文档引用。`core` 运行注册的普通有限检查；`--group all` 还包含两组较重的区间证书。各脚本仅证明其声明的有限恒等式或边界，不是 RH 或新无零半平面的机器证明。

论文编译见 [papers/README.md](papers/README.md)，须保留整个仓库结构。Lean 的固定版本、依赖准备、完整构建与定向检查分别按 [formal/README.md](formal/README.md) 执行；不要用某次局部检查替代完整构建验收。

## 历史与审计

原根 README 的完整进展记录及笔记索引已迁至 [2026-10-07 历史快照](docs/history/README-progress-2026-10-07.md)，正文完整保留，相对链接按新位置修正。历史中的“当前”“下一步”和 Goal 状态属于各自记录日期。

[AUDIT_REPORT.md](AUDIT_REPORT.md) 保存早期审计快照，[AUDIT_RESPONSE.md](AUDIT_RESPONSE.md) 记录相应修改和未完成事项。当前研究判断请结合分支看板、最新正文与限定范围的审查报告。
