# 本阶段独立复核与验收证据

日期：2026-09-06。三位只读子代理是内部独立模型审计，不是外部同行评审。
用户已授权本 GOAL 的后续独立复核继续使用子代理。

| 主题 | 首轮报告 | 跟进／闭环 | 范围 |
|---|---|---|---|
| 四矩、65/66 维、AEJ | [首轮](306-spectrum-review.md) | [跟进](306-spectrum-followup.md)、[最终闭环](306-spectrum-closure.md) | 有限误差证书及下游一侧矩、padded 分子；新增修复 AEJ 近似界与不可数约束 |
| 椭圆模型与 PLF | [首轮](307-model-review.md) | [闭环](307-model-followup.md) | 非循环次数正性、六条公理、全部点数；外部几何基础未全部重证 |
| Abel 障碍稿 | [全文](abel-proof-review.md) | [闭环](abel-followup.md) | 完整主链、外部输入、实尺度量词及复现；不认证后续不同记录模型 |

报告保留提出异议时的源稿位置与当时状态。最终处理见笔记 306–309，不能把首轮的“尚待修改”当作现状。

## 实际执行的验证

| 命令／检查 | 本轮结果 | 边界 |
|---|---|---|
| python scripts/quartic_boundary_certificate.py | 13965 组有理配置、双变量恒等式、漏条件反例及极端矩 PASS | 有限精确回归；一般结论依赖书面证明 |
| python scripts/partial_weil_audit.py | PASS | 有限谱与参数检查 |
| python scripts/operator_fourth_localizer_audit.py | 65/66 维范数、矩及局部化 PASS | 精确有限例子 |
| python reviews/2026-09-06/quartic_noncommuting_check.py | 540 项，90 配置，其中 58 配置非对易；最小余量 3077/6480、1/5 | 依赖 SymPy；由独立审查者提供，主代理复跑 |
| python scripts/elliptic_degree_benchmark.py | F5/F25 点数、次数 Gram、F/J 及外积 PASS | 全部 n 的点数依赖几何证明 |
| python scripts/test_mellin_dual_separator.py | Mellin dual-separator identity and Schur checks passed | 对应 Sobolev／对偶接口 |
| python scripts/abel_prime_atom_audit.py | 24 情形、126 原子、567180 有理间距 PASS | 主代理与独立审查者分别运行 |
| python scripts/abel_mass_discrepancy_probe.py --tail-factor 40 --skip-e1 | 独立审查者复跑 48 个质量样本为负 | 浮点实验，不推渐近或首次振荡高度 |
| python scripts/check_repo_layout.py | PASS | 目录与文档接口 |
| python scripts/test_check_groups.py | core=81、b1h=1、b1i=1，总 83，无遗漏／重复 | 分组注册及模拟分派；不是重跑全部 83 项 |
| python scripts/sync_goal.py --check | 4 文件镜像 PASS | 目标与历史保存，不证明数学 |
| git diff --check | PASS | 文本差异格式 |

未以旧 GitHub Actions 成功冒称本轮全部重型计算已复跑。本轮执行与变更匹配的检查；两个无关重型组未重复运行。

## PDF 与版本完整性

三篇源稿从仓库根目录按 papers/README 命令重编，最终每篇两次编译后无引用、溢出或其他 LaTeX 警告。
输出为结构稿 45 页、部分配置稿 26 页、Abel 稿 11 页，共 82 页。
全部页以 Poppler 渲染并在联系表中检查版面；PLF、AEJ、四矩证明页单独查看。
封面修订日期及 Abel 参考文献分页调整后，改变的页面再次以 110 dpi 渲染检查；其余页面抽取文本哈希未变。
未发现截断、重叠、缺字方框或失效引用；这是版面核验，不是重新认证整篇结构稿的早期数学内容。

[paper-build-manifest.json](paper-build-manifest.json) 固定全部引用 TeX 的 LF 规范化 SHA-256 和三份 PDF 的原始字节哈希。
可用 `python reviews/2026-09-06/verify_artifacts.py` 复验论文、文献与旧 GOAL 原始字节。
外部原文共 21 份 PDF、570 页；Hardy 1914 的 PDF 获取失败单列，不能记成已下载。
临时渲染、编译日志及提取文本在忽略目录 tmp/pdfs/，不写入版本库。
